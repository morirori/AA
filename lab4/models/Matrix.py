from models import Matrix


class Matrix:
    def __init__(self, data: list):
        self.data = data
        self.size = self.calculate_size()

    def multiply(self, matrix: Matrix) -> Matrix:
        result = Matrix._gen_init_matrix(self, matrix)
        for i in range(len(self.data)):
            for j in range(len(matrix.data[0])):
                for k in range(len(matrix.data)):
                    result[i][j] += self.data[i][k] * matrix.data[k][j]
        return Matrix(result)

    def calculate_size(self):
        return [len(self.data[0]), len(self.data[1])]

    @staticmethod
    def _gen_init_matrix(matrix_a, matrix_b):
        result = list()
        for i in range(len(matrix_a.data)):
            for j in range(len(matrix_b.data[0])):
                if j == 0:
                    temp = list()
                temp.append(0)
            result.append(temp)
        return result
