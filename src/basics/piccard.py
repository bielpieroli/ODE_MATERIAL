import numpy as np

# Define a equacaoo diferencial dy/dx = y 
def f(y):
    return y

def piccard_approx(n_iterations, x_values):
    # Inicializa a aproximacao inicial y_0(x) = 1
    y = np.ones_like(x_values)
    for _ in range(n_iterations):
        # Atualiza y utilizando a integral de f(y) fazendo a soma cumulativa (integral aproximada)
        y = 1 + np.cumsum(f(y) * np.diff(np.insert(x_values, 0, 0)))
    return y

x_values = np.linspace(0, 1, 1000)  # Aumenta o numero de pontos para melhorar a precisao
n_iterations = 1000  # Numero de iteracoes de Picard

result = piccard_approx(n_iterations, x_values)

x_final = x_values[-1]
y_final = result[-1]

print("Aproximacao final de Picard no ponto x = 1:", y_final)
print("Valor esperado (e^1):", np.exp(1))
print("Erro absoluto:", abs(y_final - np.exp(1)))
