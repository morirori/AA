from models.Matrix import Matrix


class MatrixFactory:

    @staticmethod
    def create(data: list):
        return Matrix(data)
