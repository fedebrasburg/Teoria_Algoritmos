from parser import Parser

parser = Parser()
parser.leerGrafoDirigido("../in/ej2/g1.txt")

E = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
H = [[4, 5, 6], [6, 4, 5], [5, 6, 4]]
Q = [7, 8, 9]
parser.escribir_stable_matching("../out.txt", E, H, Q)
