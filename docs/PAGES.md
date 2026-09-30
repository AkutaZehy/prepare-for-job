# 铺量总表（目标 112 页，已对照首轮考点清单逐项回补）

勾选 = 已落盘。每批完成后更新本表并重跑 `python tools/build_checklist.py`。优先级：408 与 Java 八股 > 算法题专题 > DL/LLM > 前端。
标注（补）= 2026-09-30 对照首轮考点清单回补的漏项。

## 408基础/数据结构（10）
- [x] 排序算法全对比
- [x] 栈与队列
- [x] 二叉树性质、遍历与哈夫曼
- [x] 链表与线性表
- [x] 串与 KMP
- [x] 图的存储与遍历（DFS/BFS/并查集）
- [x] 最小生成树与最短路
- [x] 拓扑排序与关键路径
- [x] 查找：折半/BST/AVL/B 树
- [x] 散列查找与冲突处理

## 408基础/操作系统（6）
- [x] 进程与线程
- [x] 进程同步与死锁
- [x] 内存管理与页面置换
- [x] 处理机调度与周转时间计算
- [x] 文件系统与磁盘（混合索引/位示图/磁盘调度）
- [x] I/O 管理与中断 DMA

## 408基础/计算机网络（8，+1）
- [x] TCP 三次握手与四次挥手
- [x] 子网划分与 CIDR
- [x] TCP 可靠传输与拥塞控制
- [x] 分层模型与协议归属（OSI/TCP-IP/设备） （补）
- [x] 应用层：HTTP/HTTPS/DNS
- [x] 数据链路层：CRC/滑动窗口/CSMA-CD
- [x] 物理层速览：奈氏/香农/编码/复用
- [x] 网络层杂项：ARP/DHCP/ICMP/NAT/IPv6/路由协议

## 408基础/计算机组成原理（4）
- [x] 数据表示与运算
- [x] Cache 与虚拟存储
- [x] 指令系统与流水线
- [x] 总线与 I/O（中断 vs DMA）

## 编程题与Java基础/Java语言基础（5，+1）
- [x] String 不可变与常量池
- [x] 面向对象与初始化顺序
- [x] 异常体系与 finally 陷阱
- [x] 泛型、反射与枚举
- [x] 基本类型、装箱与常用类陷阱（Integer 缓存/BigDecimal） （补）

## 编程题与Java基础/集合并发JVM（12，+4）
- [x] 线程基础与 synchronized
- [x] HashMap 全解
- [x] 集合框架总览与 ArrayList/LinkedList
- [x] ConcurrentHashMap 与线程安全集合
- [x] 线程池全解
- [x] JVM 内存区域与对象创建
- [x] 垃圾回收与收集器（CMS/G1）
- [x] 类加载与双亲委派
- [x] JVM 调优与排障工具（OOM/jmap/jstack）
- [x] CAS、原子类与 AQS （补）
- [x] ThreadLocal 与并发工具类（CountDownLatch 等） （补）
- [x] Java 8 新特性：Lambda/Stream/Optional （补）

## 编程题与Java基础/生态（8，+2）
- [x] MySQL 索引与 B+ 树
- [x] MySQL 事务与 MVCC
- [x] Redis 数据类型与持久化
- [x] 缓存穿透击穿雪崩、分布式锁与一致性
- [x] SpringBoot 核心：IoC/Bean 生命周期/自动装配
- [x] AOP 动态代理与 @Transactional 失效 （补，从 SpringBoot 页拆出）
- [x] 设计模式与手写单例 （补）
- [x] 周边高频速览：MyBatis/MQ/Linux 命令/Git （改名扩充）

## 编程题与Java基础/算法编程题（12，全部 ACM 模式）
- [x] 数组与双指针/两数之和
- [x] 数组与双指针/滑动窗口与前缀和
- [x] 链表/反转合并与判环
- [x] 栈队列堆/括号匹配与单调栈
- [x] 栈队列堆/TopK 与堆
- [x] 二叉树/遍历与递归套路
- [x] 回溯/全排列子集与组合
- [x] 图与搜索/岛屿问题与 BFS
- [x] 动态规划/背包与线性 DP
- [x] 贪心/区间调度
- [x] 二分查找/模板与旋转数组
- [x] 模拟与数学/进制转换与大数

## 深度学习与Python进阶/Python进阶（5）
- [x] 可变不可变与深浅拷贝
- [x] 作用域、闭包与装饰器
- [x] 迭代器与生成器
- [x] GIL 与并发模型选型
- [x] 魔法方法与内存管理

## 深度学习与Python进阶/NumPy与Pandas（2）
- [x] NumPy 广播、索引与向量化
- [x] Pandas 核心操作速查

## 深度学习与Python进阶/机器学习（6，+1）
- [x] 线性/逻辑回归与正则化
- [x] 决策树与集成学习（XGBoost/LightGBM）
- [x] SVM 速览
- [x] 经典模型补遗：KNN/朴素贝叶斯/KMeans/PCA/EM
- [x] 评价指标与样本不平衡
- [x] 特征工程与数据预处理 （补）

## 深度学习与Python进阶/深度学习（6）
- [x] Self-Attention 与 Transformer
- [x] 训练三件套：激活函数/优化器/初始化
- [x] 归一化：BN/LN/GN
- [x] CNN 基础与 ResNet
- [x] RNN/LSTM 与序列模型
- [x] 训练实操：过拟合排查/loss 不降

## 深度学习与Python进阶/大模型与LLM应用（6）
- [x] RAG 从原理到落地
- [x] BERT vs GPT 与预训练范式
- [x] LoRA 与参数高效微调
- [x] 推理加速：KV Cache/量化/vLLM
- [x] Agent 与 Function Calling
- [x] RLHF 与对齐速览

## 深度学习与Python进阶/深度学习手撕编程题（8，+2，ACM 模式）
- [x] 手撕多头注意力
- [x] softmax 与交叉熵（数值稳定）
- [x] KMeans 实现
- [x] IoU 与 NMS
- [x] TopK 堆与洗牌采样
- [x] 手撕量化（INT8 对称/非对称）
- [x] 手撕 AUC（概率+标签手算） （补）
- [x] 手撕 LR 前向与反向传播 （补）

## 前端/JS与HTML（5，+1）
- [x] 事件循环与异步
- [x] JS 类型与 == 陷阱、作用域
- [x] 闭包与原型链
- [x] DOM 事件与手写题（防抖节流）
- [x] CSS 布局基础：盒模型/BFC/Flex （补）

## 前端/TypeScript（2）
- [x] TS 类型系统入门
- [x] 工具类型与 TS 高频对比

## 前端/Vue（4）
- [x] 响应式原理
- [x] 生命周期与组件通信
- [x] Router 与 Pinia/Vuex
- [x] computed/watch 与 diff 概览

## 前端/React（3）
- [x] JSX 与组件：类组件 vs 函数组件
- [x] Hooks 核心：useState/useEffect
- [x] React vs Vue 对比

---
已完成 112 / 112（2026-09-30 全量完工）
