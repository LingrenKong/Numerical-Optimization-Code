# 《数值最优化方法》高立 CHAP3 上机习题2

## 题目

Newton 型方法的数值比较. 编写下列程序:

- 线搜索程序。程序可以包含精确线搜索准则与不同的非精确线搜索准则以及不同的线搜索求步长的方法。
- 阻尼 Newton 方法和修正 Newton 方法的程序。
- SR1 方法, BFGS 方法和 DFP 方法的程序。对最优化问题
$$
\min \sum_{i=1}^{m} r_{i}^{2}(x)
$$
选择不同的规模, 即不同的 $n$ 或 $m$, 利用编好的程序进行计算, 其中 $r_{i}(x)$ 如下:

(1) Watson 函数 (见文献 [55])
$$
r_{i}(x)=\sum_{j=2}^{n}(j-1) x_{j} t_{i}^{j-2}-\left(\sum_{j=1}^{n} x_{j} t_{i}^{j-1}\right)^{2}-1
$$
其中 $t_{i}=i / 29,1 \leqslant i \leqslant 29, r_{30}(x)=x_{1}, r_{31}=x_{2}-x_{1}^{2}-1,2 \leqslant n \leqslant 31,m=31$ 。

初始点可选为 $x^{(0)}=(0, \cdots, 0)^{\mathrm{T}}$.
(2) Discrete boundary value 函数 (见文献 [55])
$$
r_{i}(x)=2 x_{i}-x_{i-1}-x_{i+1}+h^{2}\left(x_{i}+t_{i}+1\right)^{3} / 2
$$
其中 $h=1 /(n+1), t_{i}=i h, x_{0}=x_{n+1}=0, m=n$ 初始点可选为 $x^{(0)}=\left(t_{1}\left(t_{1}-1\right), \cdots, t_{n}\left(t_{n}-1\right)\right)^{\mathrm{T}}$

通过计算，可以进行关于线搜索的不同搜索准则、不同揷值方法之间的比较；也可以通过输出的信息，进行不同 Newton 型方法有效性的比较。输出信息可以包含算法的迭代次数、函数调用次数、导数调用次数及CPU时间。

## 线搜索

当前实现了黄金分割法。

## 不同的方向选取程序

### 阻尼牛顿方法

函数名称：`damped_newton`

算法 $3.2$ **改** (基本 Newton 方法+线搜索=阻尼牛顿)
步 1 给出 $x_{0} \in \mathbb{R}^{n}, \varepsilon>0, k:=0$;
步 2 若终止准则满足, 则输出有关信息, 停止迭代;
步 3 由$d_{k}=-G_{k}^{-1} g_{k}$求得 $d_{k}$;
步 4 **线捜索**求 $\alpha_{k}, x_{k+1}:=x_{k}+\alpha_{k} d_{k}, k:=k+1$转步 2

代码实现的额外修改：

* 如果出现$G_k$不可逆，则直接终止并返回`None`
* 防止死循环，设置最长迭代次数

### 混合牛顿方法

函数名称：`modified_newton`

算法 $3.3$ (混合方法)
步 1 给定 $x_{0}, \varepsilon_{i}>0(i=1,2), k:=0$.
步 2 若终止准则满足, 则迭代停止.
步 3 若 $G_{k}$ 非奇异, 则由$d_{k}=-G_{k}^{-1} g_{k}$求得 $d_{k}$; 否则, 转步 6 .
步 4 若 $g_{k}^{\mathrm{T}} d_{k}>\varepsilon_{1}\left\|g_{k}\right\|\left\|d_{k}\right\|$, 则 $d_{k}:=-d_{k}$, 转步 7 .
步 5 若 $\left|g_{k}^{\mathrm{T}} d_{k}\right| \leqslant \varepsilon_{2}\left\|g_{k}\right\|\left\|d_{k}\right\|$, 转步 6 ; 否则, 转步 7 .
步 $6 \quad d_{k}=-g_{k}$.
步 7 线捜索求 $\alpha_{k}, x_{k+1}:=x_{k}+\alpha_{k} d_{k}, k:=k+1$, 转步 2 .

代码实现的额外修改：

* 防止死循环，设置最长迭代次数
* 之前根据理论设计了正定判断，但是发现不合适，删去
* $\epsilon_1=0.1,\epsilon_2=0.01$，这个超参数对问题影响是毁灭级的，因为自始至终余弦约为0.04，如果错误设置阈值会导致每次都反向，数值溢出。



### 拟牛顿方法

由于拟牛顿方法共性较大，所以直接三合一实现。

函数名称：`quasi_newton`

算法 $3.4$ (拟 Newton 方法的结构)
步 1 给定 $x_{0} \in \mathbb{R}^{n}$, 对称正定阵 $H_{0} \in \mathbb{R}^{n \times n}, \varepsilon>0, k:=0$;
步 2 若终止准则满足, 则输出有关信息, 停止迭代;
步 3 计算 $d_{k}=-H_{k} g_{k}$;
步 4 沿方向 $d_{k}$ 进行线搜索求 $\alpha_{k}>0$, 令 $x_{k+1}=x_{k}+\alpha_{k} d_{k}$;
步 5 修正 $H_{k}$ 得 $H_{k+1}$, 使 $H_{k+1}$ 满足 (3.21) 式, $k:=k+1$, 转步2

拟牛顿计算：

$s_{k}=x_{k+1}-x_{k}$
$y_{k}=g_{k+1}-g_{k}$

SR1：
$$
H_{k+1}^{\mathrm{SR} 1}=H_{k}+\frac{\left(s_{k}-H_{k} y_{k}\right)\left(s_{k}-H_{k} y_{k}\right)^{\mathrm{T}}}{\left(s_{k}-H_{k} y_{k}\right)^{\mathrm{T}} y_{k}}
$$
DFP：
$$
H_{k+1}^{\mathrm{DFP}}=H_{k}+\frac{s_{k} s_{k}^{\mathrm{T}}}{s_{k}^{\mathrm{T}} y_{k}}-\frac{H_{k} y_{k} y_{k}^{\mathrm{T}} H_{k}}{y_{k}^{\mathrm{T}} H_{k} y_{k}}
$$
BFGS：
$$
H_{k+1}^{\mathrm{BFGS}}=H_{k}+\left(1+\frac{y_{k}^{\mathrm{T}} H_{k} y_{k}}{y_{k}^{\mathrm{T}} s_{k}}\right) \frac{s_{k} s_{k}^{\mathrm{T}}}{y_{k}^{\mathrm{T}} s_{k}}-\left(\frac{s_{k} y_{k}^{\mathrm{T}} H_{k}+H_{k} y_{k} s_{k}^{\mathrm{T}}}{y_{k}^{\mathrm{T}} s_{k}}\right)
$$
代码实现的额外修改：

* 防止死循环，设置最长迭代次数
