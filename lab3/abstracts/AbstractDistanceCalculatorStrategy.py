from abc import ABCMeta, abstractmethod


class AbstractDistanceCalculator(metaclass=ABCMeta):

        @abstractmethod
        def distance(self, object_a, object_b):
            pass
