from os import name
import numpy as np


def golden_section_search(fun, eps=1e-5, interval=None):
    if interval is None:
        print('暂时不处理这一功能')
        return
    key = (np.sqrt(5)-1)/2
    len_interval = interval[1]-interval[0]
    right = interval[0]+key*len_interval
    left = interval[1]-key*len_interval
    while len_interval > eps:
        len_interval *= key
        if fun(left) <= fun(right):
            interval[1] = right
            right = left
            left = interval[1]-key*len_interval
        else:
            interval[0] = left
            left = right
            right = interval[0]+key*len_interval
        print(interval)
    return (interval[1]+interval[0])/2


if __name__ == '__main__':
    def foo(x): return 1-x*np.exp(-x**2)
    print('0.618法', golden_section_search(
        foo, 0.01, interval=[0, 1]), '解析解', np.sqrt(0.5))
