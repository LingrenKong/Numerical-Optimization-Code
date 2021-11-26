import numpy as np
from sympy import *  # 因为sympy体系与其他内容命名不冲突
import scipy


def get_g(fexpr, xvec, display=False):
    gexpr = [diff(fexpr, x) for x in xvec]
    if display:
        print('input function:')
        pprint(fexpr, use_unicode=True)
        print('output gradient:')
        pprint(gexpr, use_unicode=True)
    return gexpr


def get_G(fexpr, xvec, display=False):
    Gexpr = hessian(fexpr, xvec)
    if display:
        print('input function:')
        pprint(fexpr, use_unicode=True)
        print('output Hessian:')
        pprint(Gexpr, use_unicode=True)
    return Gexpr


def get_fun(expr, x, method='numpy'):
    # Sympy表达式转换为数值函数
    return lambdify(x, expr, method)


def interval_check(fun, step=1):
    # 适用于一元f(x_k+alpha*d_k)，目的是找到一个先减小后增加的区间
    if fun(0) < fun(step):
        return 0, step
    key = 0
    while fun(key+step) < fun(key):
        key += step
    # 在[key-step,key,key+step]这段是先减小后增加，支持黄金分割
    return key-step, key+step


def golden_section_search(fun, eps=1e-5, interval=None, printout=False):
    if interval is None:  # 没给U型区间就需要找
        interval = interval_check(fun)
        interval = list(interval)  # 元组换成列表
    key = (np.sqrt(5)-1)/2  # 0.618
    len_interval = interval[1]-interval[0]
    right = interval[0]+key*len_interval
    left = interval[1]-key*len_interval
    while len_interval > eps:  # 黄金分割数值精确搜索
        len_interval *= key
        if fun(left) <= fun(right):
            interval[1], right, left = right, left, right-key*len_interval
        else:
            interval[0], left, right = left, right, left+key*len_interval
        if printout:
            print("interval:",interval)
    return (interval[1]+interval[0])/2


def damped_newton(fexpr, xvec, x0, eps):  # 阻尼牛顿法  x0初始点  eps精确度
    f, g, G = [get_fun(expr, xvec) for expr in (
        fexpr, get_g(fexpr, xvec), get_G(fexpr, xvec))]
    xk = np.array(x0)
    gk, Gk = g(*xk), G(*xk)
    delta = np.linalg.norm(gk, ord=2)
    while delta > eps:
        dk = -np.linalg.pinv(Gk)@gk  # 牛顿法，用的伪逆是因为阻尼不能处理Gk奇异情况下

        def fa(a):
            x_temp = xk+a*dk
            return f(*x_temp)
        ak = golden_section_search(fa)
        xk = xk + ak*dk
        gk, Gk = g(*xk), G(*xk)
        delta = np.linalg.norm(gk, ord=2)
    return xk


def is_pos_def(A):
    try:
        np.linalg.cholesky(A)  # 利用cholesky分解是否可行来判断半正定
        return True
    except:
        return False


def modified_newton(fexpr, xvec, x0, eps):
    f, g, G = [get_fun(expr, xvec) for expr in (fexpr, get_g(
        fexpr, xvec), get_G(fexpr, xvec))]  # 有点挤，但是其实就是求fgG
    xk = np.array(x0)
    print(xk.shape)
    print(*xk)
    gk, Gk = g(*xk), G(*xk)
    # print(gk,Gk)
    delta = np.linalg.norm(gk, ord=2)  # 终止条件用gk二范数
    while delta > eps:
        try:
            dk = -np.linalg.inv(Gk)@gk  # 牛顿法
            if not is_pos_def(Gk):
                dk = -dk  # 非正定反向（和书上有些区别，是判断的Gk半正定性）
        except:
            dk = -gk  # 负梯度

        def fa(a):
            x_temp = xk+a*dk
            return f(*x_temp)
        ak = golden_section_search(fa)
        xk = xk + ak*dk
        gk, Gk = g(*xk), G(*xk)
        delta = np.linalg.norm(gk, ord=2)
    return xk

def BFGS(fexpr, xvec, x0, eps):
    pass

