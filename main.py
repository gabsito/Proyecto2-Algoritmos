#imports
import numpy as np
import statistics as st

import utils

#Globals

__FILE__ = "graficas.csv"

matrix = utils.readCSV(__FILE__)

#muestra de como obtener la linea media de cada grafica:
a = np.min(matrix[3], axis=0)[1]
b = np.max(matrix[3], axis=0)[1]
media = st.mean([a, b])


#matrix = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
n = len(matrix)
m = max(len(row) for row in matrix)
for row1 in range(n):
    for col in range(m):
        for row2 in range(row1+1, n):
            if col+1 < len(matrix[row1]) and col+1 < len(matrix[row2]):
                tramo1 = ""
                tramo2 = ""
                if matrix[row1][col][1] - matrix[row1][col+1][1] < 0:
                    tramo1 = "creciente"
                elif matrix[row1][col][1] - matrix[row1][col+1][1] > 0:
                    tramo1 = "decreciente"
                elif matrix[row1][col][1] - matrix[row1][col+1][1] == 0:
                    tramo1 = "constante"
                if matrix[row2][col][1] - matrix[row2][col+1][1] < 0:
                    tramo2 = "creciente"
                elif matrix[row2][col][1] - matrix[row2][col+1][1] > 0:
                    tramo2 = "decreciente"
                elif matrix[row2][col][1] - matrix[row2][col+1][1] == 0:
                    tramo2 = "constante"
                if tramo1 == tramo2:
                    print("Tramo desde ", col , " a ", col+1, "iguales en :", row1, " y ", row2)
