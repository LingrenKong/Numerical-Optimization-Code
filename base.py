import numpy as np
from sympy import * #因为sympy体系与其他内容命名不冲突
import scipy

def get_g(fexpr,xvec,display=False):
    gexpr = [diff(fexpr ,x) for x in xvec]
    if display:
        print('input function:')
        pprint(fexpr,use_unicode=True)
        print('output gradient:')
        pprint(gexpr,use_unicode=True)
    return gexpr

def get_G(fexpr,xvec,display=False):
    Gexpr = hessian(fexpr,xvec)
    if display:
        print('input function:')
        pprint(fexpr,use_unicode=True)
        print('output Hessian:')
        pprint(Gexpr,use_unicode=True)
    return Gexpr

if __name__ == "__main__":
    xvec = symbols ('x1:3') # 定义变量x1,x2
    fexpr = xvec[0]**2+xvec[1]*cos(xvec[1])
    gexpr = get_g(fexpr,xvec,display=True)
    Gexpr = get_G(fexpr,xvec,display=True)
    
