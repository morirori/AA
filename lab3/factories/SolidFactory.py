from models.models import Face, Solid
from factories.FaceFactory import FaceFactory


class SolidFactory:

    @staticmethod
    def create(coordinates: list):
        faces = list()
        for face in coordinates:
            faces.append(FaceFactory.create(face))
        return Solid(faces, len(faces))
