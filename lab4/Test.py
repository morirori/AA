from utills.helpers import import_data
from factories.MatrixControllerFactory import MatrixControllerFactory


data = import_data("data/data.txt")
controller = MatrixControllerFactory.create(data)
threads = 4
print("{} threads".format(threads))
controller.multiply_with_multiple_thread(threads)
print("------------------------------------------------")
print("1 thread")
controller.multiply_with_single_thread()
