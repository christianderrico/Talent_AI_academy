import ast


def read_file(path, sep=";"):
    with open(path, "r") as f:
        lines = [l.strip() for l in f.readlines()]
        res = [
            [
                l if "[" not in l else ast.literal_eval(l)
                for l in lines[i].split(sep=sep)
            ]
            for i in range(1, len(lines))
        ]
        return res


def print_elements(elem):
    for el in elem:
        print(el)
    print("-" * 20)
