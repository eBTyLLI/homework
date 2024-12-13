import matplotlib.pyplot as plt
import numpy as np
import os

def f(x, alpha, beta):
    return (x ** beta + alpha ** beta) / x ** beta

#1
x = np.array([i for i in range(11)])

x = np.linspace(-10, 10)
plt.plot(x, f(x, 1, 1), label = '1 функция', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')
plt.grid()
plt.title('Графики')
plt.xlabel('Абсцисс')
plt.ylabel('Ординат')
plt.legend()
plt.show()
plt.savefig(dir + '9_1.png', dpi = 300)

#2
plt.plot(x, f(x, 1, 1), label = '1', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')
plt.grid()
plt.title('Графики')
plt.xlabel('Абсцисс')
plt.ylabel('Ординат')
plt.legend()

plt.axes([0.25, 0.50, 0.10, 0.15])
plt.title('для малых х')
plt.plot(x, f(x, 1, 1), label = '1', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')

plt.axes([0.45, 0.60, 0.25, 0.25])
plt.title('для больших х')
plt.plot(x, f(x, 1, 1), label = '1', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')

plt.show()
plt.savefig(dir + '9_2.png', dpi = 300)

#3
dir = os.getcwd()
x = np.linspace(-5, 0, 1000)
plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams['figure.autolayout'] = True

def f(x, alpha, beta):
    y = (x ** beta + alpha ** beta) / x ** beta
    y[y > 100] = np.nan
    y[y < -100] = np.nan
    return y

plt.plot(x,f(x, 1, 1), color = 'indianred', label = '1 случай')
plt.plot(x,f(x, 2, 1), color = 'palegoldenrod', label = '2 случай')
plt.plot(x,f(x, 1, 2), color = 'darkblue', label = '3 случай')
plt.plot(x, [0] * len(x), color = 'gold', label = 'f(x) = 0')
plt.grid()
plt.title('График')
plt.xlabel('Абсцисс')
plt.ylabel('Ординат')
plt.legend()
plt.axes([0.21, 0.17, 0.50, 0.25])

def f(x, alpha, beta):
    y = (x ** beta + alpha ** beta) / x ** beta
    y[y > 3] = np.nan
    y[y < -3] = np.nan
    return y

x = np.linspace(-5, 0, 1000)
plt.plot(x, [0] * len(x), color = 'purple', label = 'x = 0')

#4
dir = os.getcwd()
x = np.linspace(-5, 5, 1000)
plt.rcParams['figure.figsize'] = [3, 3]
plt.rcParams['figure.autolayout'] = True

def f(x, alpha, beta):
    y = (x ** beta + alpha ** beta) / x ** beta
    y[y > 100] = np.nan
    y[y < -100] = np.nan
    return y

plt.plot(x,f(x, 1, 1), color = 'indianred', label = '1 случай')
plt.plot(x,f(x, 2, 1), color = 'palegoldenrod', label = '2 случай')
plt.plot(x,f(x, 1, 2), color = 'darkblue', label = '3 случай')
plt.plot(x, [0] * len(x), color = 'gold', label = 'f(x) = 0')
plt.grid()
plt.title('График')
plt.xlabel('Абсцисс')
plt.ylabel('Ординат')
plt.legend()
x = np.linspace(-1, 2, 1000)

def C_P(ax, x, a, b1, b2, array_b, k, fontsize = 12, hide_labels = False):
    ax.plot(x, f(x, a, b1), color = 'orange', label = '1 случай')
    ax.plot(x, f(x, a, b2), color = 'yellow', label = '2 случай')   
    ax.grid()
    ax.plot(x, f(x, a, array_b[k][0]), color = 'darkblue', label = '1 случай')
    ax.plot(x, f(x, a, array_b[k][1]), color = 'pink', label = '2 случай')
    ax.legend()
    ax.locator_params(nbins = 3)
    if hide_labels:
        ax.set_xticklabels([])   
        ax.set_yticklabels([]) 
    else:
        ax.set_xticklabels('Абсицсс', fontsize = fontsize)
        ax.set_yticklabels('Ординат', fontsize = fontsize)

plt.savefig(dir + '/9_4.png', dpi = 300)