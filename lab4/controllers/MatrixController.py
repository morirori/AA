from models import Matrix
import threading
import math
from queue import Queue
from time import time
from math import floor


class MatrixController:

    def __init__(self):
        self.matrices = list()

    def add_matrix(self, matrix: Matrix):
        self.matrices.append(matrix)

    def multiply_with_multiple_thread(self, num):
        grouped_matrices = list()
        temp = list()
        result = {}
        for idx, val in enumerate(self.matrices, 1):
            temp.append(val)
            if math.fmod(idx, floor(len(self.matrices)/num)) == 0:
                grouped_matrices.append(temp)
                temp = list()
            elif idx == len(self.matrices):
                grouped_matrices[-1].append(val)
        queue = Queue()
        for item in grouped_matrices:
            queue.put(item)
        ts = time()
        workers = self.build_worker_pool(queue, num, result)
        for worker in workers:
            worker.join()
        res = None
        for i in range(num-1):
            if res is None:
                res = result[i].multiply(result[i+1])
            else:
                res = res.multiply(result[i+1])
        print(time() - ts)
        print(res.data)

    def multiply_with_single_thread(self):
        ts = time()
        result = None
        for i in range(len(self.matrices) - 1):
            if result is None:
                result = self.matrices[i].multiply(self.matrices[i+1])
            else:
                result = result.multiply(self.matrices[i+1])
        print(time() - ts)
        print(result.data)

    def build_worker_pool(self, queue, size, result):
        workers = []
        for i in range(size):
            worker = Multiplyer(queue, result, i)
            worker.start()
            workers.append(worker)
        return workers


class Multiplyer(threading.Thread):
    def __init__(self, queue: Queue, result: dict, id):
        threading.Thread.__init__(self)
        self.result = result
        self.queue = queue
        self.id = id

    def run(self):
        data = self.queue.get()
        result = self.multiply(data)
        self.result[self.id] = result
        self.queue.task_done()

    def multiply(self, data):
        result = None
        for i in range(len(data) - 1):
            if result is None:
                result = data[i].multiply(data[i+1])
            else:
                result = result.multiply(data[i+1])
        return result
