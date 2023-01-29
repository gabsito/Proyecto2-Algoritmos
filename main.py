#imports
import utils
import numpy as np

#Globals

__FILE__ = "graficas.csv"

matrix = utils.readCSV(__FILE__)
#matrix = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
n = len(matrix)
m = max(len(row) for row in matrix)
for row1 in range(n):
    graficosIguales = []
    graficosSimilares = {}
    graficosDiferentes = []
    for row2 in range(row1+1, n):
        iguales = True
        similares = False
        similitudes = []
        for col in range(m):
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
                  # print("Tramo desde ", col , " a ", col+1, "iguales en :", row1, " y ", row2)
                   similares = True
                   similitudes.append(col)
                if tramo1 != tramo2:
                    iguales = False
        if iguales:
            graficosIguales.append(row2)
        elif similares:
            similitudes = np.array(similitudes)
            graficosSimilares[row2] = similitudes
        else:
            graficosDiferentes.append(row2)
    if len(graficosIguales)>0:
        print(graficosIguales)
    if len(graficosSimilares)>0:
        print(graficosSimilares)
    if len(graficosDiferentes)>0:
        print(graficosDiferentes)
        
