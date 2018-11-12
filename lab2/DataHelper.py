class DataHelper:

    @staticmethod
    def read_data(file):
        f = open(file, "r")
        f = f.read()
        data = f.splitlines()
        to_return = list()
        for line in data:
            examined_line = line.split("\t")
            to_return.append((examined_line[0], examined_line[1], float(examined_line[2])))
        return to_return



