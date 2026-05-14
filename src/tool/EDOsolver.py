import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox
from sympy import symbols, Function, Eq, diff, dsolve, lambdify, sympify, latex
from sympy.solvers.ode import classify_ode
from scipy.integrate import solve_ivp

EDO_INICIAL = "t"   # x' = f(t, x)  (expressão inicial)
T0, TF = 0.0, 10.0  # intervalo de t (inicial, final)
X0_INIT = 1.0  # condição inicial padrão de x (dependente)
XMIN, XMAX = -10.0, 10.0  # limites do eixo x (dependente)

t, x = symbols("t x")  # símbolos para sympy (t indep, x depend)
xf = Function("x")(t)  # função x(t) simbólica


def parse_expressao(expr):
    """Retorna símbolo sympy e função numérica de f(t,x)."""
    f_sym = sympify(expr, locals={"t": t, "x": x})
    return f_sym, lambdify((t, x), f_sym, modules=["numpy"])


def resolver_numerico(expr, x0):
    """Resolve EDO numericamente em termos de t e x."""
    _, f = parse_expressao(expr)

    def rhs(t_val, u):
        try:
            v = float(f(t_val, u[0]))
            return [v if np.isfinite(v) else 0.0]
        except Exception:
            return [0.0]

    t_vals = np.linspace(T0, TF, 500)
    sol = solve_ivp(rhs, (T0, TF), [x0], t_eval=t_vals)
    return sol.t, sol.y[0]



def resolver_analitico(expr, x0):
    """Tenta obter solução analítica via sympy 'dsolve'."""
    try:
        f_sym, _ = parse_expressao(expr)
        ode = Eq(diff(xf, t), f_sym.subs(x, xf))  # x' = f(t,x)
        sol = dsolve(ode, ics={Function("x")(T0): x0})
        rhs = sol.rhs
        return lambdify(t, rhs, modules=["numpy"]), f"$x(t)={latex(rhs)}$"
    except Exception:
        return None, "Sem solução analítica"


def classificar(expr):
    """Classifica o tipo da EDO usando sympy 'classify_ode'"""
    try:
        f_sym, _ = parse_expressao(expr)
    except Exception:
        return ""
    ode = Eq(diff(xf, t), f_sym.subs(x, xf))
    types = classify_ode(ode, xf)
    if not types:
        return "Indefinida"
    return types[0]

def desenha_campo(ax, expr):
    """Desenha campo de direções"""
    ax.clear()
    xs = np.linspace(T0, TF, 40)
    ys = np.linspace(XMIN, XMAX, 40)
    X, Y = np.meshgrid(xs, ys)
    _, f = parse_expressao(expr)
    try:
        M = f(X, Y)
    except Exception:
        M = np.zeros_like(X)
    M = np.where(np.isfinite(M), M, 0.0)
    U = np.ones_like(M)
    V = M
    ax.streamplot(X, Y, U, V, density=1.0, color=M, cmap="coolwarm", linewidth=1)
    ax.set_xlim(T0, TF)
    ax.set_ylim(XMIN, XMAX)
    ax.set_title("Campo de direções")
    ax.set_xlabel("t")
    ax.set_ylabel("x")


fig, (ax_sol, ax_field) = plt.subplots(1, 2, figsize=(11, 5))
plt.subplots_adjust(bottom=0.22)

estado = {"expr": EDO_INICIAL, "x0": X0_INIT} 


def atualizar(*_):
    """Redesenha soluções e campo com estado atual."""
    expr, x0 = estado["expr"], estado["x0"]
    ax_sol.clear()

    try:
        t, xn = resolver_numerico(expr, x0)
        ax_sol.plot(t, xn, lw=2, label="Numérica")
    except Exception:
        ax_sol.text(0.5, 0.5, "Erro na solução numérica", transform=ax_sol.transAxes,
                    ha="center", va="center")

    fana, label = resolver_analitico(expr, x0)
    if fana is not None:
        try:
            tt = np.linspace(T0, TF, 500)
            xn_ana = fana(tt)
            xn_ana = np.where(np.abs(xn_ana) < 1e5, xn_ana, np.nan)
            ax_sol.plot(tt, xn_ana, "--", lw=2, label="Analítica")
        except Exception:
            pass

    ax_sol.plot([T0], [x0], "o", ms=7, label=f"x₀ = {x0:.2f}")
    ax_sol.set_xlim(T0, TF)
    ax_sol.set_ylim(XMIN, XMAX)
    ax_sol.grid(alpha=0.3)
    tipo = classificar(expr)
    ax_sol.set_title(f"x' = {expr} ({tipo})\n{label}")
    ax_sol.set_xlabel("t")
    ax_sol.set_ylabel("x")
    ax_sol.legend(loc="best", fontsize=9)

    desenha_campo(ax_field, expr)
    ax_field.plot([T0], [x0], "o", ms=6)
    fig.canvas.draw_idle()


ax_slider = fig.add_axes([0.12, 0.1, 0.55, 0.04]) 
slider = Slider(ax_slider, "x0", XMIN, XMAX, valinit=X0_INIT, valstep=0.1)
slider.label.set_text("X\u2080")

ax_box = fig.add_axes([0.12, 0.03, 0.55, 0.05]) 
box = TextBox(ax_box, "x' = ", initial=EDO_INICIAL)


def ao_mudar_slider(v):
    estado["x0"] = float(v)
    atualizar()


def ao_enviar(text):
    text = text.strip()
    if text:
        estado["expr"] = text
        atualizar()


slider.on_changed(ao_mudar_slider)
box.on_submit(ao_enviar)

atualizar()
plt.show()