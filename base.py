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


def golden_section_search(fun, eps=1e-5, interval=None):
    if interval is None:
        print('暂时不处理这一功能')
        return
    key = (np.sqrt(5)-1)/2  # 0.618
    len_interval = interval[1]-interval[0]
    right = interval[0]+key*len_interval
    left = interval[1]-key*len_interval
    while len_interval > eps:
        len_interval *= key
        if fun(left) <= fun(right):
            interval[1], right, left = right, left, right-key*len_interval
        else:
            interval[0], left, right = left, right, left+key*len_interval
        print(interval)
    return (interval[1]+interval[0])/2


if __name__ == "__main__":
    print('梯度与Hessian测试：')
    xvec = symbols('x1:3')  # 定义变量x1,x2
    fexpr = xvec[0]**2+xvec[1]*cos(xvec[1])
    gexpr = get_g(fexpr, xvec, display=True)
    Gexpr = get_G(fexpr, xvec, display=True)

    print('黄金分隔法测试：')
    def foo(x): return 1-x*np.exp(-x**2)
    print('0.618法', golden_section_search(
        foo, 0.01, interval=[0, 1]), '解析解', np.sqrt(0.5))
