import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self):
        self.h = 1e-5

    def __get__(self, instance, owner):
        self.instance = instance
        return self

    def __call__(self, x):
        return (self.instance(x + self.h) - self.instance(x - self.h)) / (2 * self.h)


class ExponentialFunction:
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative()  

    def __call__(self, x):
        return self.a * np.exp(x)

    def plot(self):
        x = np.linspace(-2, 2, 400)
        y = self(x)
        y_derivative = self.derivative(x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'f(x) = {self.a} * exp(x)')
        plt.plot(x, y_derivative, label=f"f'(x) = {self.a} * exp(x)")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('график функции и её производной')
        plt.legend()
        plt.grid(True)
        plt.show()

