from sympy import symbols, Function, Eq, dsolve, classify_ode, checkodesol, exp

# Define a variavel simbolica t e a funcao y(t)
t = symbols('t')
y = Function('y')(t)

# Define a EDO simbolica: y' = y 
deq = Eq(y.diff(t), y)

# Classifica o tipo da EDO
tipo_edo = classify_ode(deq)
print("Tipo da EDO:", tipo_edo)

# Resolve a EDO simbolicamente (solucao geral)
solucao_analitica = dsolve(deq, y)
print("Solucao analitica geral:", solucao_analitica)

# Resolve a EDO com condicao inicial y(0) = 1
solucao_com_ics = dsolve(deq, y, ics={y.subs(t, 0): 1})
print("Solucao analitica com condicao inicial y(0)=1:", solucao_com_ics)

# Verifica se a solucao encontrada eh valida
verificacao = checkodesol(deq, solucao_com_ics)
print("A solucao encontrada eh valida?", verificacao)