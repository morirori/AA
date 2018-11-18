def import_data(path):
    with open(path, 'r') as file:
        f = file.read()
        data = f.splitlines()
        matrices = list()
        matrix = list()
        row = list()
        for line in data:
            if line.find("----") != -1:
                matrices.append(matrix)
                matrix = list()

            elif line.find("Matrix #") != -1:
                matrix = list()
                row = list()
            elif line != '':
                examined_line = [s for s in line.split()]
                if examined_line[0].find("[[") != -1 and examined_line[-1].find("]") == -1:
                    examined_line[0] = examined_line[0].replace("[[", "")

                elif examined_line[0].find("[[") != -1 and examined_line[-1].find("]") != -1:
                    examined_line[0] = examined_line[0].replace("[[", "")
                    examined_line[-1] = examined_line[-1].replace("]", "")
                    for item in examined_line:
                        row.append(float(item))
                    matrix.append(row)
                    row = list()
                    continue

                elif examined_line[-1].find("]") != -1 and examined_line[0].find("[") == -1:
                    examined_line[-1] = examined_line[-1].replace("]", "")
                    for item in examined_line:
                        row.append(float(item))
                    matrix.append(row)
                    row = list()
                    continue

                elif examined_line[-1].find("]") != -1 and examined_line[0].find("[") != -1:
                    examined_line[0] = examined_line[0].replace("[", "")
                    examined_line[-1] = examined_line[-1].replace("]", "")
                    for item in examined_line:
                        row.append(float(item))
                    matrix.append(row)
                    row = list()
                    continue

                elif examined_line[0].find("[") != -1:
                    examined_line[0] = examined_line[0].replace("[", "")

                for item in examined_line:
                    row.append(float(item))
    return matrices
