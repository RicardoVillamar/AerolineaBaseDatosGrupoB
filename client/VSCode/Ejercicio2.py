import math

# Función para calcular la serie de Taylor de ln(x) alrededor de x0
def taylor_series_ln(x, x0, n):
    result = 0
    for i in range(1, n + 1):
        result += ((-1) ** (i - 1)) * ((x - x0) ** i) / i
    return result

# Valor exacto de ln(2.5)
exact_value = math.log(2.5)

# Punto de aproximación
x = 2.5

# Aproximación de primer orden (n = 1)
n1 = 1
approximation1 = taylor_series_ln(x, 1, n1)
error1 = abs(exact_value - approximation1) / abs(exact_value)

# Resultados
print("Aproximación de primer orden:", approximation1)
print("Error relativo de primer orden:", error1)