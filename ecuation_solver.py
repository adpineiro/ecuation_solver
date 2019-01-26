import numpy as np


def resolve(points):
    # crear matriz vacia
    x = np.zeros((10, 2))

    z = np.zeros((10))
    # reestructurar los datos de la matriz

    for i in range(10):
        x[i] = (points[i][0:2])
        z[i] = points[i][2]

    # resolver la ecuacion

    degrees = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]  # lista de factores

    matrix = np.stack([np.prod(x ** d, axis=1) for d in degrees], axis=-1)  #

    coeff, resid, rank, s = np.linalg.lstsq(matrix, z)  # resolve o sistema

    id = 0

    # comprobación dos coeficientes
    print("Comprobacion")
    for id in range(10):
        compro = coeff[0] + coeff[1] * coeff_left_fwd[id][0] + coeff[2] * coeff_left_fwd[id][1] + coeff[3] * \
                 coeff_left_fwd[id][0] ** 2 + coeff[4] * coeff_left_fwd[id][0] * coeff_left_fwd[id][1] + coeff[5] * \
                 coeff_left_fwd[id][1] ** 2
        print(compro)

    print("Coeficientes")
    print(coeff)  # coeficientes da solucion
    print("Residuos")
    print(resid)  # residuos
    print("Rango")
    print(rank)  # rango da matriz
    print("Valores singulares")
    print(s)  # valores singulares


# datos do tfg jose lamas coeff left forward motion
coeff_left_fwd = np.array([[85.53, 0.02, 160],
                           [142.58, 0.19, 160],
                           [191.74, 0.56, 160],
                           [214.87, 0.83, 160],
                           [204.87, 1.05, 160],
                           [158.2, -0.20, 185],
                           [206.54, 0.03, 185],
                           [256.17, 0.15, 185],
                           [224.14, 0.33, 185],
                           [261.8, 0.65, 185],
                           [199.75, -0.47, 210],
                           [259.47, -0.04, 210],
                           [263.34, 0.08, 210],
                           [273.22, 0.15, 210],
                           [353.25, 0.46, 210],
                           [202.87, -0.66, 235],
                           [273.75, -0.18, 235],
                           [298.65, -0.02, 235],
                           [328.66, 0.15, 235],
                           [359.46, 0.27, 235],
                           [196.32, -0.81, 255],
                           [228.72, -0.34, 255],
                           [291.49, -0.13, 255],
                           [340.71, -0.01, 255],
                           [389.00, 0.19, 255]])

coeff_right_fwd = np.array([[85.53, 0.02, 160],
                            [158.20, -0.20, 160],
                            [199.75, -0.47, 160],
                            [202.87, -0.66, 160],
                            [196.32, -0.81, 160],
                            [142.58, 0.19, 185],
                            [206.54, 0.03, 185],
                            [259.47, -0.04, 185],
                            [273.75, -0.18, 185],
                            [228.72, -0.34, 185],
                            [191.74, 0.56, 210],
                            [256.17, 0.15, 210],
                            [263.34, 0.08, 210],
                            [298.65, -0.02, 210],
                            [291.49, -0.13, 210],
                            [214.87, 0.83, 235],
                            [224.14, 0.33, 235],
                            [273.22, 0.15, 235],
                            [328.66, 0.15, 235],
                            [340.71, -0.01, 235],
                            [204.87, 1.05, 255],
                            [261.80, 0.65, 255],
                            [353.25, 0.46, 255],
                            [359.46, 0.27, 255],
                            [389.00, 0.19, 255]])

coeff_left_turn = np.array([[38.68, -2.22, 255],
                            [36.09, -2.22, 255],
                            [40.86, -2.22, 255],
                            [35.55, -1.82, 230],
                            [37.00, -1.82, 230],
                            [45.22, -1.82, 230],
                            [44.08, -1.45, 205],
                            [42.59, -1.45, 205],
                            [38.56, -1.45, 205],
                            [30.16, -0.84, 180],
                            [37.43, -0.84, 180],
                            [23.85, -0.84, 180],
                            [13.90, -0.28, 160],
                            [7.90, -0.28, 160],
                            [12.02, -0.28, 160],
                            [70.72, 2.56, 0],
                            [48.65, 2.56, 0],
                            [60.10, 2.56, 0],
                            [43.34, 2.25, 25],
                            [50.08, 2.25, 25],
                            [42.13, 2.25, 25],
                            [32.19, 1.64, 50],
                            [32.15, 1.64, 50],
                            [30.87, 1.64, 50],
                            [23.01, 1.03, 75],
                            [24.43, 1.03, 75],
                            [22.70, 1.03, 75],
                            [23.67, 0.38, 90],
                            [19.87, 0.38, 90],
                            [24.46, 0.38, 90],
                            ])

# print("sp_left")
# resolve(coeff_left_fwd)
# print("sp_right")
resolve(coeff_left_turn)

"""
import numpy as np
x = np.random.random((100, 2))
z = np.sin(5 * x[:,0]) + .4 * np.sin(x[:,1])
degrees = [(i, j) for i in range(3) for j in range(3)]  # list of monomials x**i * y**j to use
matrix = np.stack([np.prod(x**d, axis=1) for d in degrees], axis=-1)   # stack monomials like columns
datos = np.linalg.lstsq(matrix,z)
coeff = np.linalg.lstsq(matrix, z)[0]    # lstsq returns some additional info we ignore
print("Coefficients", coeff)    # in the same order as the monomials listed in "degrees"
fit = np.dot(matrix, coeff)
print("Fitted values", fit)
print("Original values", z)"""
