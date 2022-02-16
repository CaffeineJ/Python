import sympy

xi = sympy.symbols('xi')

f = xi**2/((2-xi)*(2-xi)) - 1.4

g = xi**2 - 1.4*(2-xi)*(2-xi)

print(sympy.expand(g)) 
print(sympy.simplify(g)) 
print(sympy.factor(g)) 
print(sympy.solve(f))
