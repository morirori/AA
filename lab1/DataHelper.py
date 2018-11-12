class DataHelper:

    @staticmethod
    def read_data(file):
        f = open(file, "r")
        f = f.read()
        data = f.splitlines()
        return list(tuple(map(int, line.split(";"))) for line in data)



