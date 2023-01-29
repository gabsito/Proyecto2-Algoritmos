import numpy as np


def readCSV(file: str) -> np.array:
    rtn = []
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        graph_id, points_str = line.strip().split(":")
        points = [tuple(map(int, point.replace('(', '').replace(')', '').split(','))) for point in
                  points_str.split(';')]
        rtn.append(points)
    rtn = np.array(rtn)
    print(rtn)
    return rtn
