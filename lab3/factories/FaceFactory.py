from models.models import Point, Face


class FaceFactory:

    @staticmethod
    def create(coordinates: list):
        points_list = list()
        if len(coordinates) == 3:
            for points in coordinates:
                points_list.append(Point(points[0], points[1], points[2]))
        return Face(points_list[0], points_list[1], points_list[2])
