import numpy as np


def ufunc_reduce(ufct, *vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r, v)
    return r


if __name__ == '__main__':
    a = np.array([2, 3, 4, 5])
    b = np.array([8, 5, 4])
    c = np.array([5, 4, 6, 8, 3])
    r = ufunc_reduce(np.add, a, b, c)
    for i in r:
        print(i)
        print('*' * 40)