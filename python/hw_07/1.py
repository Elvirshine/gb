print("Задание №1")


class Matrix:
    def __init__(self, my_array):
        self.my_array = my_array

    def __str__(self):
        result = ''
        for a in self.my_array:
            result += f"{' '.join(str(v) for v in a)}\n"
        return result

    def __add__(self, other):
        for i in range(len(self.my_array)):
            for j in range(len(self.my_array[i])):
                self.my_array[i][j] += other.my_array[i][j]
        return self


m = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
p = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(m)
print(p)
print(m + p)
