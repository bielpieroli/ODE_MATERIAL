import numpy as np
import matplotlib.pyplot as plt

# Definindo a EDO: y' = y - t
def f(t, y):
    return y - t

# Criando uma grade de pontos para t e y
t = np.linspace(0, 5, 20)
y = np.linspace(-1, 6, 20)
T, Y = np.meshgrid(t, y)

# Calculando as derivadas em cada ponto
DY = f(T, Y)
DX = np.ones_like(DY)  # dt/dt = 1 para normalizar as setas


# Plotando o campo de direções usando streamplot
plt.figure(figsize=(8, 6))
plt.streamplot(T, Y, DX, DY, color='blue', arrowsize=1)
plt.title("Campo de Direções para y' = y - t")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.show()
