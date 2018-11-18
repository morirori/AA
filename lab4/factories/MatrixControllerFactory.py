from controllers.MatrixController import MatrixController
from factories.MatrixFactory import MatrixFactory


class MatrixControllerFactory:

    @staticmethod
    def create(matrices):
        controller = MatrixController()
        for matrix in matrices:
            controller.add_matrix(MatrixFactory.create(matrix))
        return controller
