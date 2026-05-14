import numpy as np
from scipy.integrate import solve_ivp

# Define a equacao diferencial y' = y
def f(t, y):
    return y

# Define o intervalo de integracao e a condicao inicial
t_span = (0, 1)  # Intervalo de tempo de 0 a 1
y0 = [1]  # Condicao inicial y(0) = 1

# Resolve o PVI usando o metodo RK45
solution = solve_ivp(f, t_span, y0, method='RK45', t_eval=np.linspace(0, 1, 100))

# Exibe os resultados, comparando com a solucao exata y = exp(t)
print("Solucao numerica usando solve_ivp:", solution.y[0])
exact_solution = np.exp(solution.t)
print("Solucao exata:", exact_solution)
print("Erro absoluto maximo:", np.max(np.abs(solution.y[0] - exact_solution)))