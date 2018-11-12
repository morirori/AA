from calculations.Calculations import PointAndEdgeCalculation, Calculator
from utils.CalculationTags import CalculationTags
from utils.Helpers import import_data
from factories.SolidFactory import SolidFactory
from models.models import *

f1 = Face(Point(1, 0, 0), Point(0, 1, 0), Point(0, 0, 0))
f2 = Face(Point(100, 0, 0.13), Point(0, 100, 0.13), Point(-100, -100, 0.13))
dist = Calculator.calculate_distance(f1, f2, CalculationTags.distance_between_faces)
print("2a")
print("distance: {}".format(dist))


data = import_data("data/data.txt")
solid1 = SolidFactory.create(data[0])
solid2 = SolidFactory.create(data[1])
dist = Calculator.calculate_distance(solid1, solid2, CalculationTags.distance_between_solids)
print("2b")
print("distance: {}".format(dist))


