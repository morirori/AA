from models.models import*
import pprint


def calculate_vector(p1: Point, p2: Point):
    return [p2.x-p1.x, p2.y-p1.y, p2.z-p1.z]


def dot_product(v1: list, v2: list):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


def cross_product(v1: list, v2: list):
    return [v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]


def subtract_vectors(v2: list, v1: list):
    return [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]]


def import_data(file):

    f = open(file, "r")
    f = f.read()
    data = f.splitlines()
    to_return = [list(), list()]
    counter = -1
    face_list = list()
    for line in data:
        if line.find("--- SOLID") != -1:
            counter = counter + 1
        elif line != '':
            examined_line = line.split(";")
            face_list.append([float(examined_line[0]), float(examined_line[1]), float(examined_line[2])])
        else:
            to_return[counter].append(face_list)
            face_list = list()
    return to_return


def check_position_between_point_and_edge(p: Point, e: Edge):
    edge_vector = calculate_vector(e.v1, e.v2)
    b1_to_a_vector = calculate_vector(e.v1, p)
    b2_to_a_vector = calculate_vector(e.v2, p)
    c1 = dot_product(b1_to_a_vector, edge_vector)
    c2 = dot_product(b2_to_a_vector, edge_vector)
    if c1 <= 0:
        return "left"
    elif c2 >= 0:
        return "right"
    return "between"
