# 第一章 最优化方法概述

目标：求解一些问题的数值解（尤其是没有解析解的情况）



## 概念

优化（optimization）：**Mathematical optimization** (alternatively spelled *optimisation*) or **mathematical programming** is the selection of a best element, with regard to some criterion, from some set of available alternatives.[^1]

关键点--何种准则（criterion）



## 教材与推荐参考

- 《数值最优化方法》 高立
- Numerical Optimization, by Jorge Nocedal, Stephen Wright
- Optimization, 2nd ed. by Kenneth Lange, 2013
- Convex Optimization, by Stephen Boyd, Lieven Vandenberghe （凸优化，数学而非数值方法）
- Optimization in machine learning, by Suvrit Sra, Sebastian Nowozin and Stephen J. Wright （专著）
-  R-optimization （代码书）
- Optimization Toolbox in MATLAB （代码书）



## 问题与实例

优化问题：无约束优化，约束优化；统计多为无约束优化，经济多为约束优化

根据具体特点分类：

- 变量的数据类型：
  - 连续数据：课内目标
  - 离散数据：组合优化问题
- 函数的连续可微性质：
  - 光滑函数：$f,c_i\in C^{\infty}$
  - 非光滑：例如LASSO
- 函数的线性性质：
  - 线性规划：基于单纯型法，有多项式时间确定性解法，不在课内考虑
  - 非线性：比较一般性的问题

约束优化问题：
$$
\begin{aligned}
&\min f(x) \\
\text { s.t. } & c_{i}(x)=0, i \in \mathcal{E} \\
&c_{i}(x) \geq 0, i \in  \mathcal{I}
\end{aligned}
$$
其中$x\in \mathbb R^n$，$f:\mathbb R^n\rightarrow \mathbb R$

对于最优解一般使用$x^*=argmin f(x)$表示

最优化问题的一个可视化技巧：$x\in \mathbb{R}^2$情况下，利用等高线（contour）进行可视化



## 关于现代优化

现代的优化维数高，规模大，而且问题往往是复杂、非线性的

求解方法的目标是

- 高效：时间空间复杂度（所以不用牛顿）
- 精确：算法要数值稳定




[^1]: "[The Nature of Mathematical Programming](http://glossary.computing.society.informs.org/index.php?page=nature.html) [Archived](https://web.archive.org/web/20140305080324/http://glossary.computing.society.informs.org/index.php?page=nature.html) 2014-03-05 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)," *Mathematical Programming Glossary*, INFORMS Computing Society.