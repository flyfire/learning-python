import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
    c = x + y * 1j
    z = c
    div_time = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * np.conj(z) > 2 ** 2
        div_now = diverge & (div_time == maxit)
        div_time[div_now] = i
        z[diverge] = 2
    return div_time


if __name__ == '__main__':
    plt.imshow(mandelbrot(400, 400))
    plt.show()
