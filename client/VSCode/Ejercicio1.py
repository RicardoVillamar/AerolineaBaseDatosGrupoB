import math

# Función para calcular la serie de Taylor de e^x alrededor de x0
def taylor_series(x, x0, n):
    result = 0
    for i in range(n):
        result += ((x - x0) ** i) / math.factorial(i)
    return result

# Valor de e^1
exact_value = math.exp(1)

# Punto de aproximación
x = 1

# Aproximación con grado 1
n1 = 1
approximation1 = taylor_series(x, 0.2, n1)
error1 = abs(exact_value - approximation1)

# Aproximación con grado 2
n2 = 2
approximation2 = taylor_series(x, 0.2, n2)
error2 = abs(exact_value - approximation2)

# Aproximación con grado 3
n3 = 3
approximation3 = taylor_series(x, 0.2, n3)
error3 = abs(exact_value - approximation3)

# Resultados
print("Aproximación con polinomio de grado 1:", approximation1)
print("Error absoluto con polinomio de grado 1:", error1)
print("Aproximación con polinomio de grado 2:", approximation2)
print("Error absoluto con polinomio de grado 2:", error2)
print("Aproximación con polinomio de grado 3:", approximation3)
print("Error absoluto con polinomio de grado 3:", error3)