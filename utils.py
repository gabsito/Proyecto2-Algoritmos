import numpy as np


def readCSV(file: str) -> dict:
    rtn = {}
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        graph_id, points_str = line.strip().split(":")
        points = [tuple(map(int, point.replace('(', '').replace(')', '').split(','))) for point in
                  points_str.split(';')]
        rtn[graph_id] = np.array(points)
    print(rtn)
    return rtn
