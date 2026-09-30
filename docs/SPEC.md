# 页面规格 v2

所有知识点页共同遵守的契约。新增页面只要满足本规格，重跑 `python tools/build_checklist.py` 即可进入进度清单。

## 文件与标题

- 一个知识点 = 一个自包含 HTML 文件，内嵌全部样式与脚本，不引外部 CSS/JS（MathJax、Mermaid 走 CDN 除外）。
- 文件名不含冒号等文件系统敏感字符；放在对应大类/子类文件夹。
- `<title>` 固定格式：`<页名> · <大类>/<子类>`，必须有 " · "——构建脚本按 ` · ` 前段提取标题，没有它页面进不了清单。
- 页首面包屑相对链接回 `index.html`，层级按目录深度（`../../index.html` 或 `../../../index.html`）。

## 页面骨架

```
div.wrap
├─ div.crumbs            面包屑
├─ h1 + div.meta         页名 / 适用岗位 / 形态 / 更新日期
├─ div.recap             要点速记（一段话浓缩全页）
├─ section.card.k        一、知识点梳理（公式、表格、代码）
├─ section.card.p        二、考点说明（怎么考）+ 概念自测（quiz）
├─ section.card.q        三、示例题目 / ACM 完整代码（ACM 页）
├─ section.card.s        四、解答说明 / 易错点小结
└─ <script>              判分脚本（全站逐字同一份）
```

四张卡片左上角色条区分类别：k 蓝（知识点）、p 黄（考点）、q 紫（题目）、s 绿（解答）。

## 判分交互 DOM 契约

单选题：

```html
<div class="quiz" data-answer="B">
  <p><span class="tg">单选</span><b>1.</b> 题干（&nbsp;&nbsp;）</p>
  <div class="opt" data-k="A">A. …</div>
  <div class="opt" data-k="B">B. …</div>
  <div class="opt" data-k="C">C. …</div>
  <div class="opt" data-k="D">D. …</div>
  <div class="exp" hidden><b>答案 B。</b>解析…来源：白名单措辞。</div>
</div>
```

多选题三处差异：`data-answer="ABD"`、根节点加 `data-multi`、选项后追加提交块
`<div class="opt-submit"><button class="submit" type="button">提交</button></div>`。

判分脚本全站逐字同一份（约 40 行原生 JS）：单选点击即判（选错标红、正确项标绿、揭示解析，答题后锁定）；多选可勾选，点提交后按"选对/选错/漏选"三种状态着色。

**CSS 级联关键点**：`.opt.picked` 规则必须声明在 `.opt.right / .wrong / .miss` 之前，否则多选提交后"已选"样式会覆盖判分着色（历史 bug，改样板时注意）。

计算题/口述题不进判分系统，用 `div.q + <details>` 包裹，参考答案写在 details 内。

## 图示规范（Mermaid + ASCII 双保险）

每张图两个块成对出现：

```html
<pre class="ascii-fallback">纯 ASCII 图或文字版</pre>
<pre class="mermaid">graph LR …</pre>
```

页面末尾放同一段 `<script type="module">`：加载 CDN 成功则删除 `.ascii-fallback`，失败则删除 `pre.mermaid`。任何环境都不会露出裸源码。Mermaid 节点 id 用英文，label 可中文。

## 公式（MathJax 3）

`<head>` 内先放配置再异步引 CDN；`options.skipHtmlTags` 含 `pre/code`，代码块不会被公式解析污染。行内 `$…$`，独立公式 `$$…$$`。断网时公式显示原文。

## ACM 模式（算法题与手撕题）

- 完整可运行程序：stdin 读入、stdout 输出，可直接粘贴牛客判题。Java 用 `StreamTokenizer`/`BufferedReader` 快读，Python 用 `sys.stdin.read().split()`；多组输入用 EOF 循环。
- 页面内必须有 `.io` 块写明输入/输出格式与样例，判题相关约定（下标起始、并列处理、空集输出、浮点精度）写进题面或易错点。
- 每个程序的样例输入输出**实际运行核对后**才落盘；数值不稳定实现（如 naive softmax）给反例对照。
- 网格/字符串输入按行读字符串，不用数字 tokenizer（前导零会丢）。

## 代码块

- 所有 `< > &` 转义为实体；代码块上方用 `<span class="lang">语言</span>` 角标。
- 语言规则：能 Java 的给 Java + Python 双份；只能 Python 的给 Python（必要时加伪代码）；前端用 JS/TS。
- 关键示例实跑核对（node / tsc / python），输出结果题的答案必须来自实际运行。

## 题目来源白名单

来源标注只允许以下措辞，逐字使用，多选/口述题写在解析或参考答案尾部：

- `来源：408 统考高频题型（公开真题常考形式）。`
- `来源：牛客经典题。`
- `来源：面试高频改编。`
- `来源：LeetCode 经典题（ACM 改编）。`
- `来源：剑指 Offer（ACM 改编）。`
- `来源：JavaGuide 收录题型。`
- `来源：AI 岗笔试高频。`

不编造真题年份，不收录付费题库内容。

## 构建脚本工作原理

`tools/build_checklist.py`：按固定大类顺序遍历，`rglob("*.html")` 递归收集（保证三级目录的算法题子夹不漏），排除 `index.html` 与下划线开头文件；按 `<title>` 的 ` · ` 前段提取标题、按相对父目录分组；输出 `checklist.js`（`window.CHECKLIST=…`，供 file:// 下 script 标签加载）与 `checklist.json`。页数与勾选底账见 [PAGES.md](PAGES.md)。

## 落盘前自查清单

每页交付前过一遍：

1. title 含 " · "；quiz 数 = data-answer 数 = exp 数；
2. 每个 data-multi 配一个 opt-submit + submit；
3. `.opt.picked` 声明在判分着色规则之前；
4. 代码块无裸 `< > &`；
5. 来源仅白名单措辞；
6. Mermaid/ASCII 成对、module 脚本在位（用图的页面）；
7. MathJax head 完整（用公式的页面）；
8. 样例实跑核对记录在案。

## 公开前泄漏扫描清单

对全库 grep 以下模式，命中即处理：绝对盘符路径（`D:\`、`C:\Users`）、用户名、内网/本地端口号、会话/工具内部标识、真实姓名与联系方式。
