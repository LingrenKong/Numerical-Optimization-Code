# 预备知识基础



## 问题类型

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



最优化问题的一个可视化技巧：$x\in \mathbb{R}^2$情况下，利用等高线（contour）进行可视化。

等高线的数学描述：

根据等距的c绘制出$f(x)=c, x\in \mathbb R^2$，可以可视化二维情况下函数的性质。





## 问题假定与符号

一般假定目标函数$f$具有一二阶导数

对于梯度$\nabla f(x)=\left[\frac{\partial f(x)}{\partial x_{1}},\cdots,\frac{\partial f(x)}{\partial x_{n}}\right]^T$，采用$g(x)$作为简化写法。

类似的，对于Hessian矩阵采用
$$
G(x)=\nabla^2f(x)=\left[\begin{array}{ccc}
\frac{\partial^{2} f(x)}{\partial x_{1}^{2}} & \cdots & \frac{\partial^{2} f(x)}{\partial x_{1} \partial x_{n}} \\
\vdots & \ddots & \vdots \\
\frac{\partial^{2} f(x)}{\partial x_{n} \partial x_{1}} & \cdots & \frac{\partial^{2} f(x)}{\partial x_{n}^{2}}
\end{array}\right]
$$

约束优化问题：
$$
\begin{aligned}
&\min f(x) \\
\text { s.t. } & c_{i}(x)=0, i \in \mathcal{E} \\
&c_{i}(x) \geq 0, i \in  \mathcal{I}
\end{aligned}
$$
其中$x\in \mathbb R^n$，$f:\mathbb R^n\rightarrow \mathbb R$

对于最优解一般使用$x^*=argmin f(x)$表示，最优解有可能是一个集合，不止一个点。



