import math

# 1
class Fraction:
    def __new__(cls, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен 0.")

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Числитель и знаменатель должны быть целыми числами.")

        return super().__new__(cls)

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.__normalize()  # сокращаем

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    @property
    def value(self):
        return round(self.numerator / self.denominator, 3)

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("только дроби с дробями")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("только дроби с дробями")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("только дроби с дробями")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("нельзя на 0 делить")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("только дроби с дробями")

    def __normalize(self):  # сокращ
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0: 
            self.numerator *= -1
            self.denominator *= -1


#2
class FractionMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)

        for row in matrix:
            if len(row) != self.cols:
                raise ValueError("размерности не совпадают")
            for element in row:
                if not isinstance(element, Fraction):
                    raise TypeError("только дроби должны быть")

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("матрицы должны быть одного размера для сложения")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return FractionMatrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("матрицы должны быть одного размера для вычитания.")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return FractionMatrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения")

        result = [[None for _ in range(other.cols)] for _ in range(self.rows)] 

        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = Fraction(0, 1)  # Начинаем с 0/1
                for k in range(self.cols):
                    sum_val += self.matrix[i][k] * other.matrix[k][j]
                result[i][j] = sum_val

        return FractionMatrix(result)

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return FractionMatrix(transposed_matrix)


    @property
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("матрица должна быть квадратной")

        if self.rows == 1:
            return self.matrix[0][0]
        elif self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
             raise NotImplementedError("определитель для матриц размером больше 2 не реализован")
