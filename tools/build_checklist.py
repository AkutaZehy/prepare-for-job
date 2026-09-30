#!/usr/bin/env python3
"""扫描四大类目录树，生成进度清单数据 checklist.js / checklist.json。

用法：python tools/build_checklist.py （在仓库根目录执行）
新增/删除知识点页后重跑一次即可；进度存浏览器 localStorage，不受本脚本影响。
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREFERRED = ["408基础", "编程题与Java基础", "深度学习与Python进阶", "前端"]
EXCLUDE_FILES = {"index.html"}
OUT_JS = ROOT / "checklist.js"
OUT_JSON = ROOT / "checklist.json"


def title_of(html_path: Path) -> str:
    try:
        head = html_path.read_text(encoding="utf-8", errors="ignore")[:2048]
    except OSError:
        return html_path.stem
    m = re.search(r"<title>(.*?)</title>", head, re.S | re.I)
    if not m:
        return html_path.stem
    title = m.group(1).strip().split("·")[0].strip()
    return title or html_path.stem


def main() -> None:
    top_dirs = sorted(
        (d for d in ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")),
        key=lambda p: (
            PREFERRED.index(p.name) if p.name in PREFERRED else len(PREFERRED),
            p.name,
        ),
    )
    categories = []
    for cat in top_dirs:
        groups: dict[str, list] = {}
        for f in sorted(cat.rglob("*.html")):
            if f.name in EXCLUDE_FILES or f.name.startswith("_"):
                continue
            sub_key = f.parent.relative_to(cat).as_posix()
            groups.setdefault(sub_key, []).append(
                {"t": title_of(f), "p": f.relative_to(ROOT).as_posix()}
            )
        subs = [
            {"name": key, "items": items} for key, items in sorted(groups.items())
        ]
        if subs:
            categories.append({"name": cat.name, "subs": subs})

    data = {
        "generatedAt": datetime.date.today().isoformat(),
        "categories": categories,
    }
    OUT_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    OUT_JS.write_text(
        "window.CHECKLIST=" + json.dumps(data, ensure_ascii=False) + ";",
        encoding="utf-8",
    )
    total = sum(len(s["items"]) for c in categories for s in c["subs"])
    print(f"OK: {len(categories)} categories, {total} items -> checklist.js / checklist.json")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
