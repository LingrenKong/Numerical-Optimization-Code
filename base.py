import numpy as np
import sympy as sym
import scipy

def get_g(fexpr,xvec,display=False):
    gexpr = [sym.diff(fexpr ,x) for x in xvec]
    if display:
        print('input function:')
        sym.pprint(fexpr,use_unicode=True)
        print('output gradient:')
        sym.pprint(gexpr,use_unicode=True)
    return gexpr

def get_G(gexpr,xvec,display=False):
    Gexpr = sym.Matrix([[sym.diff(g, x) for x in xvec] for g in gexpr])
    if display:
        print('input gradient:')
        sym.pprint(gexpr,use_unicode=True)
        print('output Hessian:')
        sym.pprint(Gexpr,use_unicode=True)
    return gexpr

if __name__ == "__main__":
    xvec = sym.symbols ('x1:3') # 定义变量x1,x2
    fexpr = xvec[0]**2+xvec[1]*sym.cos(xvec[1])
    gexpr = get_g(fexpr,xvec,display=True)
    Gexpr = get_G(gexpr,xvec,display=True)
    
