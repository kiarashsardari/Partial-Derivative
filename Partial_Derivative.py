import sympy as sp
def d(f, *sympols_list):
    sympols_list = [sp.Symbol(s) for s in sympols_list]
    return [sp.diff(f, x) for x in sympols_list]


if __name__ == "__main__":
    x = sp.Symbol('x')
    f = x**3 + 3*x - 4 + sp.Symbol('y')
    sp.pprint(d(f,"x", "y", "g"))