from enum import Enum


class CalculationTags(Enum):
    distance_between_points = "distance between points"
    distance_between_edge_and_point = "distance between edge and point"
    distance_between_edges = "distance between edges"
    distance_between_edge_and_face = "distance between edge and face"
    distance_between_faces = "distance between faces"
    distance_between_solids = "distance between solids"
    distance_between_point_and_face = "distance_between_point_and_face"
