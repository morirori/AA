from abstracts.AbstractDistanceCalculatorStrategy import AbstractDistanceCalculator
import math
from models.models import *
# from context.DistanceCalculatorContext import DistanceCalculatorContext
from utils.CalculationTags import CalculationTags
from utils.Helpers import calculate_vector, dot_product, check_position_between_point_and_edge, cross_product


class Calculator:
    @staticmethod
    def calculate_distance(object_a, object_b, collision_tag):
        context = DistanceCalculatorContext(collision_tag)
        return context.strategy.distance(object_a, object_b)


class PointAndPointCalculation(AbstractDistanceCalculator):
    def __init__(self):
        pass

    def distance(self, p1: Point, p2: Point):
        return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2) + math.pow(p1.z - p2.z, 2))


class PointAndEdgeCalculation(AbstractDistanceCalculator):

    def distance(self, object_a: Point, object_b: Edge):
        edge_dist = Calculator.calculate_distance(object_b.v1, object_b.v2, CalculationTags.distance_between_points)
        dist_a_to_b1 = Calculator.calculate_distance(object_a, object_b.v1, CalculationTags.distance_between_points)
        dist_a_to_b2 = Calculator.calculate_distance(object_a, object_b.v2, CalculationTags.distance_between_points)
        p = 0.5 * (edge_dist + dist_a_to_b1 + dist_a_to_b2)
        field = math.sqrt(p * (p - edge_dist) * (p - dist_a_to_b1) * (p - dist_a_to_b2))
        height = 2 * field / edge_dist
        position = check_position_between_point_and_edge(object_a, object_b)
        if position == "left":
            return dist_a_to_b1
        elif position == "right":
            return dist_a_to_b2
        return height


class EdgeAndEdgeCalculation(AbstractDistanceCalculator):
    def distance(self, a: Edge, b: Edge):
        some_small_num = 0.00000001
        a1_to_a2_vector = calculate_vector(a.v1, a.v2)  # u
        b1_to_b2_vector = calculate_vector(b.v1, b.v2)  # v
        b1_to_a1_vector = calculate_vector(b.v1, a.v1)  # w
        a = dot_product(a1_to_a2_vector, a1_to_a2_vector)
        b = dot_product(a1_to_a2_vector, b1_to_b2_vector)
        c = dot_product(b1_to_b2_vector, b1_to_b2_vector)
        d = dot_product(a1_to_a2_vector, b1_to_a1_vector)
        e = dot_product(b1_to_b2_vector, b1_to_a1_vector)
        D = a * c - b * b
        sd = D
        td = D

        if D < some_small_num:
            sn = 0
            sd = 1
            tn = e
            td = c
        else:
            sn = b * e - c * d
            tn = a * e - b * d
            if sn < 0:
                sn = 0
                tn = e
                td = c
            elif sn > sd:
                sn = sd
                tn = e + b
                td = c

        if tn < 0:
            tn = 0
            if d * (-1) < 0:
                sn = 0
            elif d * (-1) > a:
                sn = sd
            else:
                sn = d * (-1)
                sd = a
        elif tn > td:
            tn = td
            if -1 * d + b < 0:
                sn = 0
            elif -1 * d + b > a:
                sn = sd
            else:
                sn = -1 * d + b
                sd = a

        sc = 0 if abs(sn) < some_small_num else sn / sd
        tc = 0 if abs(tn) < some_small_num else tn / td
        temp = [tc * x for x in b1_to_b2_vector]
        temp2 = [sc * x for x in a1_to_a2_vector]
        temp3 = list()
        for i in range(len(temp2)):
            temp3.append(b1_to_a1_vector[i] + temp2[i])
        finall_vector = calculate_vector(Point(temp[0], temp[1], temp[2]), Point(temp3[0], temp3[1], temp3[2]))
        return math.sqrt(dot_product(finall_vector, finall_vector))


class EdgeAndFaceCalculation(AbstractDistanceCalculator):

    def distance(self, e: Edge, f: Face):

        steps = 10
        dx = (e.v2.x-e.v1.x)/steps
        dy = (e.v2.y-e.v1.y)/steps
        dz = (e.v2.z-e.v1.z)/steps
        x, y, z = e.v1.x, e.v1.y, e.v1.z
        minimum = Calculator.calculate_distance(Point(x, y, z), f, CalculationTags.distance_between_point_and_face)
        for i in range(steps):
            result = Calculator.calculate_distance(Point(x, y, z), f, CalculationTags.distance_between_point_and_face)
            if result <= minimum:
                minimum = result
            x += dx
            y += dy
            z += dz
        return minimum


class FaceAndPointCalculation(AbstractDistanceCalculator):

    def distance(self, p: Point, f: Face):
        if check_position_between_point_and_edge(p, Edge(f.v1, f.v2)) == "between" and \
                check_position_between_point_and_edge(p, Edge(f.v1, f.v3)) == "between" and \
                check_position_between_point_and_edge(p, Edge(f.v2, f.v3)) == "between":

            vector = cross_product(calculate_vector(f.v1, f.v2), calculate_vector(f.v1, f.v3))
            D = -1 * (vector[0]*f.v1.x + vector[1]*f.v1.y + vector[2]*f.v1.z)
            return abs(vector[0] * p.x + vector[1] * p.y + vector[2] * p.z + D)/math.sqrt(pow(vector[0], 2) +
                                                                                          pow(vector[1], 2) +
                                                                                          pow(vector[2], 2))
        return min([
            Calculator.calculate_distance(p, Edge(f.v1, f.v2), CalculationTags.distance_between_edge_and_point),
            Calculator.calculate_distance(p, Edge(f.v1, f.v3), CalculationTags.distance_between_edge_and_point),
            Calculator.calculate_distance(p, Edge(f.v2, f.v3), CalculationTags.distance_between_edge_and_point),
        ])


class FaceAndFaceCalculation(AbstractDistanceCalculator):

    def distance(self, f1: Face, f2: Face):
        return min([
            Calculator.calculate_distance(Edge(f1.v1, f1.v2), f2,
                                          CalculationTags.distance_between_edge_and_face),
            Calculator.calculate_distance(Edge(f1.v1, f1.v3), f2,
                                          CalculationTags.distance_between_edge_and_face),
            Calculator.calculate_distance(Edge(f1.v2, f1.v3), f2,
                                          CalculationTags.distance_between_edge_and_face),
            Calculator.calculate_distance(Edge(f2.v1, f2.v2), f1,
                                          CalculationTags.distance_between_edge_and_face),
            Calculator.calculate_distance(Edge(f2.v1, f2.v3), f1,
                                          CalculationTags.distance_between_edge_and_face),
            Calculator.calculate_distance(Edge(f2.v2, f2.v3), f1,
                                          CalculationTags.distance_between_edge_and_face),
        ])


class SolidAndSolidCalculation(AbstractDistanceCalculator):

    def distance(self, f1: Solid, f2: Solid):
        minimum = 10000000000000000
        for face in f1.faces:
            for f in f2.faces:
                dist = Calculator.calculate_distance(face, f, CalculationTags.distance_between_faces)
                minimum = dist if dist < minimum else minimum
        return minimum


class DistanceCalculatorContext:

    def __init__(self, calculation_type: CalculationTags):
        if calculation_type == CalculationTags.distance_between_faces:
            self.strategy = FaceAndFaceCalculation()
        elif calculation_type == CalculationTags.distance_between_edge_and_point:
            self.strategy = PointAndEdgeCalculation()
        elif calculation_type == CalculationTags.distance_between_points:
            self.strategy = PointAndPointCalculation()
        elif calculation_type == CalculationTags.distance_between_edge_and_face:
            self.strategy = EdgeAndFaceCalculation()
        elif calculation_type == CalculationTags.distance_between_edges:
            self.strategy = EdgeAndEdgeCalculation()
        elif calculation_type == calculation_type.distance_between_solids:
            self.strategy = SolidAndSolidCalculation()
        elif calculation_type == calculation_type.distance_between_point_and_face:
            self.strategy = FaceAndPointCalculation()
