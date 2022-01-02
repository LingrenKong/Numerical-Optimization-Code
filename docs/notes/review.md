# 总复习

考试题目回忆：


---

===

共计6个大题

1.凸函数与凸集

证明集合

$$
\mathcal{F}=\{x\mid c_i(x)\ge0,i=1,2\cdots m\}
$$

是凸集（$c_i(x)$是concave function）

> 知识点：凸函数诱导的集合是凸集+convex和concave关系+集合的交集还是凸集



2.最速下降法实践

书上作业3-3，删掉了结论，需要自己归纳结果



3.线搜索的全局收敛性

证明Goldstein准则的版本

> 知识点：和作业的精确搜索方法很相似，需要利用泰勒展开来推导x的变化充分小（从而使用g的一致连续）



4.牛顿法发散实例

1. 求解$f(x)=x^{\frac43}$的牛顿法
2. 证明除了$x_0=0$之外都不收敛



5.求KKT

两个不等式约束的求KKT点，不等式一个线性一个二次，难度不大



6.对数障碍函数

两个约束的函数

1. 写出对数障碍罚函数
2. 证明$\mu_k\to0$时候收敛到最优点（先求罚函数的解然后求极限）

===

---


## 第一章 引论

这一部分内容不在教材中，主要是补充

重点内容：

- 凸集
- 凸函数

要求：能够判断凸集、凸函数



### 凸集（convex set）

#### 定义：

设集合$D\subset \mathbb R^n$，若对于任意其中的两点 $x,y\in D$ ，以及实数 $\lambda \in [0,1]$ 都有
$$
\lambda x+(1-\lambda )y \in D
$$
则称集合D为凸集

>  判断的注意事项：边界点、临界情况

#### 常见例子

- 空集$\Phi$、全空间$\Omega$
- 超平面：$\{x\in \mathbb R^n | a_xx_1+\cdots a_n x_n=b\}$

- 半空间：$\{x\in \mathbb R^n | a_xx_1+\cdots a_n x_n \ge b\}$

- 超球： $\left\{ x | ||x|| \le r \right\}$ ，利用范数的三角不等式可以证明，不仅限于欧式空间



#### 凸集性质

1. 有限、无限个凸集的交集仍然为凸集
2. 设D为凸集,$\beta$ 是实数，那么集合$\beta D=\{y \mid y=\beta x, x \in D\}$还是凸集
3. 和集合$D_{1}+D_{2} = \left\{x_1+x_2 \mid  x_1 \in D_{1}, x_2 \in D_{2}\right\}$仍然为凸集



### 凸函数（convex function）

#### 定义

设函数$f(x)$**定义在凸集$D\subset \mathbb R^n$上**，若对$\forall x,y\in D,\lambda\in [0,1]$都有：
$$
f(\lambda x+(1-\lambda )y)\le \lambda f(x)+(1-\lambda )f(y)
$$
则称$f(x)$为凸集D上的凸函数

> 注，无论是凸函数还是凹函数（concave function）都定义在凸集上面，f是凸函数那么-f就是凹函数



#### 判断方式

1. 按照定义
2. 一阶充要条件（可微情况下）：$f(y)\ge f(x)+\nabla f(x)^T(y-x)$
3. 二阶充要条件（二阶可微情况下）：$\forall x\in D$，$f(x)$的Hessian矩阵半正定



例题：$f(x)=(x-1)^2$

1. 展开：

$$
\begin{aligned}
&f(\lambda x+(1-\lambda) y)-\lambda f(x)-(1-\lambda) f(y) \\
=&[\lambda x+(1-\lambda) y-1]^{2}-\lambda(x-1)^{2}-(1-\lambda)(y-1)^{2} \\
=&[\lambda(x-1)+(1-\lambda)(y-1)]^{2}-\lambda(x-1)^{2}-(1-\lambda)(y-1)^{2} \\
=&\left.\lambda(1-\lambda)(x-1)^{2}-\lambda(1-\lambda)(y-1)^{2}+2 \lambda(1-\lambda)(x-1) y-1\right) \\
=& \lambda(1-\lambda)\left[(x-1)^{2}-2(x-1)(y-1)-(y-1)^{2}\right] \\
=& \lambda(1-\lambda)\left[(x-y)^{2}-2(y-1)^{2}\right] \\
\le & 0
\end{aligned}
$$

2. $(y-1)^2-(x-1)^2-2(x-1)(y-x)=(y-x)^2\ge0$

3. $G(x)=2>0$



#### 凸函数性质

1. 几何性质（一元情况下为例子）：
   1. 函数两点中间的曲线在两点连线以下（凸函数定义）
   2. 过任何一点的切线在曲线以下（一阶充要条件）
2. 凸函数的**非负**系数线性组合仍为凸函数
3. 凸函数导出凸集：$S(f,\beta)=\{x|x\in D,f(x)\le\beta\} $



## 第二章 无约束最优化的基本结构

重点内容：收敛速度判定



### 最优性条件

一阶必要条件：$\nabla f(x^*)=0$ ，梯度为0

二阶必要条件：$G(x^*)\succeq 0$，Hessian半正定



### 收敛性与速度

收敛性：

- 全局收敛
- 局部收敛：对于满足条件的初值具有收敛性

收敛速度：

- 线性：$\lim _{k \rightarrow \infty} \frac{\left\|x_{k+1}-x^{*}\right\|}{\left\|x_{k}-x^{*}\right\|}=a$
- 超线性：a=0
- 二阶收敛$\lim _{k \rightarrow \infty} \frac{\left\|x_{k+1}-x^{*}\right\|}{\left\|x_{k}-x^{*}\right\|^2}=a$

习题二-4：证明序列的收敛速度

- 首先确定$x^*$的结果，这里是数列问题，所以按照$\lim a_n=a^*$理解
- 然后按照公式计算验证速度



### 线搜索

精确方法：
$$
\alpha_k = argmin_\alpha f(x_k+\alpha d_k)
$$
精确搜索的验证方式是（求导可得）：
$$
\nabla f(x_k+\alpha d_k)^T d_k=0
$$


非精确方法：

- 有四个准则，核心思想是要下降而且步长不要太小
- 常用Goldstein和Wolfe准则（充分下降的要求相同）

Goldstein：$\rho\in [0.5,1]$

$$
\begin{aligned}
&f\left(x_{k}+\alpha d_{k}\right) \leq f\left(x_{k}\right)+\rho \nabla f\left(x_{k}\right)^{\top} d_{k} \alpha_{k} \\
&f\left(x_{k}+\alpha d_{k}\right) \geq f\left(x_{k}\right)+(1-\rho) \nabla f\left(x_{k}\right)^{\top} d_{k} \alpha_{k}
\end{aligned}
$$
Wolfe准则：
$$
\begin{aligned}
&f\left(x_{k}+\alpha d_{k}\right) \leq f\left(x_{k}\right)+\rho \nabla f\left(x_{k}\right)^{\top} d_{k} \alpha_{k} \\
&\nabla f\left(x_{k}+\alpha d_{k}\right)^{\top} d_{k} \geq \sigma \nabla f\left(x_{k}\right)^{\top} d_{k}
\end{aligned}
$$

### 线搜索收敛性证明（还没弄完）

课内主要是讲解了定理2.8，对Wolfe的收敛性证明；这个方式对精确线搜索也成立（习题2-12）。基本的模式就是在梯度$g(x)$一致连续的条件下，夹角满足有界性，根据准则可以导出全局收敛。

定理2.8：设在水平集$L=\{x\in \mathbb R^n|f(x)\le f(x_0)\}$上面函数$f$有下界，梯度$\nabla f(x)$存在且一致连续，方向$d_k$与$-\nabla f(x_k)$的夹角满足

$$
\theta_k \le \frac{\pi}{2}-\mu,\mu>0,\forall k
$$

采用Wolfe准则的方法下，或者有限次后$g(x_N)=0$，或者$g(x_k)\to 0,k \to \infty$

证明：





---




习题2-12：设梯度$\nabla f(x)$在水平集$L=\{x\in \mathbb R^n|f(x)\le f(x_0)\}$上面存在且一致连续，方向$d_k$与$-\nabla f(x_k)$的夹角满足：
$$
\theta_k \le \frac{\pi}{2}-\mu,\mu>0
$$
采用精确线搜索的方法，或者有限次后$g(x_N)=0$，或者$g(x_k)\to 0,k \to \infty$



精确搜索的证明：基于反证法，要对于下降的情况构建一个

假定$\nabla f(x_k)\nrightarrow 0$，那么$\exist \epsilon>0,子列||\nabla f(x_k)||\ge \epsilon $，从而
$$
-\frac{\nabla f\left(x_{k}\right)^{\top} d_{k}}{\left\|d_{k}\right\|}=\left\|g_{k}\right\| \cos \theta_{k} \geq \varepsilon \sin \mu
$$
下面通过展开得到梯度之差的项（这一步和定理是主要区别）
$$
\begin{aligned}
f(x_k+\alpha d_k)&=f(x_k)+\alpha \nabla f(\xi_k)^T d_k \quad \text{中值定理}\\
&= f(x_k)+\alpha\nabla f(x_k)^T d_k+\alpha[\nabla f(\xi_k)^T d_k-\nabla f(x_k)^T d_k] \quad \text{加一项减一项}\\
&\le f(x_k)+\alpha\left\|d_{k}\right\|\left(\frac{\nabla f\left(\xi_{k}\right)^{\top} d_{k}}{\left\|d_{k}\right\|}+\left\|\nabla f\left(\xi_{k}\right)-\nabla f\left(x_{k}\right)\right\|\right) \quad \text{柯西不等式}
\end{aligned}
$$

精确线搜索的$\alpha$是最小的情况，



### 线搜索VS信赖域

线搜索：先选方向，再定步长

信赖域：限定步长范围，再求方向

信赖域算法全书中讲的比较少。



## 第三章 负梯度方法与牛顿方法

深度学习的负梯度改进（如ADAM），特化算法（L-BFGS）不考

拟牛顿BFGS的公式不要求背下来，考的情况下会给出



### 负梯度

迭代方向：$d_k=-g(x_k)$

收敛性：全局收敛（夹角足够，根据线搜索定理可知）

收敛速度：取决于最优点Hessian矩阵的条件数，正常情况是线性收敛

几何性质：精确线搜索有$d_{k+1}^Td_k=0$，一条正交的迭代轨迹，所以并不够好。



### 牛顿法

迭代方向：$d_k=-G_k^{-1}g(x_k)$

收敛性：局部收敛，**依赖于初值！**可能到鞍点、不收敛、出现奇异矩阵等

收敛速度：二阶收敛

优点：

- $x_0$充分接近极小值的情况下，二阶收敛
- 有二次终止性（正定二次函数的优化只需要一次）

缺点：

- $x_0$不接近极小值的情况下，有可能出现$G_k$不正定或者奇异矩阵，无法收敛
- 每次都要求Hessian
- 矩阵逆运算复杂度大



### 拟牛顿

思路来自于对$g$在$x_{k+1}$位置的泰勒展开：
$$
g(x_k)=g(x_{k+1})+G_{k+1}(x_k-x_{k+1})+o(||x_k-x_{k+1}||)
$$
拟牛顿法的符号：
$$
s_k=x_{k+1}-x_k,y_k=g_{k+1}-g_k
$$
思路上要求$B_{k+1}s_k=y_k,B\sim G$或者$H_{k+1}y_k=s_k,H \sim G^{-1}$

有对称秩1的SR1方法，也有从对称秩2角度推导的BFGS/DFP

拟牛顿：一定条件下全局收敛+超线性速度



## 第四章 共轭梯度方法

### 定义

共轭可以理解成一种推广形式的内积与正交

共轭：$d_i^TGd_j=0,\forall i\ne j$，如果从内积角度可以写成$<d_i,d_j>_G=0$

正交是一种特殊的共轭方向：$G=I$

共轭向量组中的向量必然线性无关，可以从定义或者内积的性质证明。



### 共轭方法的性质

要求初始必须是$d_0=-g_0$。这一点不是技巧而是必须的理论要求



（线性共轭）对于正定二次函数$f(x)=\frac{1}{2}x^TGx-b^Tx$。任意初始点$x_0$取$d_0=-g_0$。假定共轭梯度方法经过k步迭代（$k\le n$）未达到极小值，则下列关系成立：

- 有共轭方向：$<d_k,d_i>_G=0,i=0,1,2,\cdots,k-1$
- 梯度正交：$g_k^Tg_i=0,i=0,1,2,\cdots,k-1$
- 下降性：$g_k^Td_k=-g_k^Tg_k<0$



非线性共轭梯度（从线性共轭梯度方法的步骤导出）：

- FR：$\beta_k=\frac{g_{k+1}^Tg_{k+1}}{g_k^Tg_k}$
- PRP：$\beta_k=\frac{g_{k+1}^T(g_{k+1}-g_k)}{g_k^Tg_k}$

FR有一个大缺点，一旦某一步情况比较差，后续会陷进去；而PRP在比较差点方向等效于负梯度，所以PRP更好。



## 第五章 非线性最小二乘

不考

## 第六章 约束优化理论

重点内容：KKT条件（求解KKT点，按照情况分类讨论，如习题10-2）

函数形式是：

- 目标为最小化
- 约束的不等号是$c_i(x)\ge 0$，对应乘子是要$-\lambda$

KKT条件：

$$
\begin{array}{ll}
\nabla_{x} L\left(x^{*}, \lambda^{*}\right)=0 & \Longrightarrow g\left(x^{*}\right)=\sum_{i=1}^{m} \lambda_{i}^{*} a_{i}\left(x^{*}\right)\quad\text{稳定条件} \\
c_{i}\left(x^{*}\right)=0, & i \in \mathcal{E}\quad\text{可行条件}\\
c_{i}\left(x^{*}\right) \geqslant 0, & i \in \mathcal{I}\quad\text{可行条件} \\
\lambda_{i}^{*} \geqslant 0, & i \in \mathcal{I}\quad\text{非负条件} \\
\lambda_{i}^{*} c_{i}\left(x^{*}\right)=0, & i \in \mathcal{E} \cup \mathcal{I}\quad\text{互补条件}
\end{array}
$$

注：

- 互补条件对于等式约束其实不用求，所以等式的KKT就是拉格朗日乘子法
- KKT点不一定是最优解,只是必要条件



题目类型：求解约束优化的KKT点

技巧：

- 可以适当利用函数形式来获得化简
- 主要方式是对于非负条件是否取等进行讨论，分情况求解



## 第七章 罚函数方法



### 外点罚函数：

等式约束
$$
P(x,\sigma)=f(x)=\frac12 \sigma\sum_{i\in\varepsilon}c_i^2(x)
$$
算法步骤：

1. 初始化（理论上$\sigma\to\infty$）
2. 热启动，从上一轮结果$x^*_{k-1}$为初始点，求$||\nabla P(x,\sigma_k)||\le\epsilon$
3. 检验是否近似达到等式约束，满足则结束
4. 不满足则加大$\sigma_k$回到第二步



### 障碍罚函数：

不等式约束（**对数**罚、倒数罚）

对数（更常用，注意是**负对数**）：
$$
B_L(x,\mu)=f(x)-\mu\sum_{i\in\tau}\log c_i(x)
$$
倒数：
$$
B_L(x,\mu)=f(x)+\mu\sum_{i\in\tau}c_i^{-1}(x)
$$
算法步骤：

1. 初始化（理论上$\mu\to 0^+$）
2. 热启动，从上一轮结果$x^*_{k-1}$为初始点，求$||\nabla B_L(x,\mu)||\le\epsilon$
3. 检验障碍项是否充分小，满足则结束
4. 不满足则减小$\mu_k$回到第二步



### 增广拉格朗日：

主要等式，可以用于不等式（松弛转化，并没有细讲）

也叫做乘子罚函数，相当于是外点罚加上乘子项。
$$
\Phi(x, \lambda, \sigma)=f(x)-\sum_{i} \lambda_{i} c_{i}(x)+\frac{1}{2} \sigma \sum_{i \in \varepsilon} c_{i}^{2}(x)
$$
增广拉格朗日的好处：$\sigma$不用大规模调整，不需要趋于无穷了

算法步骤相对复杂一些。
