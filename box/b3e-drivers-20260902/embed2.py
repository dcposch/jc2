import sympy as sp
X,Y,t,s = sp.symbols('X Y t s')
f = 72*X**2*Y**3 + 450*X**2*Y**2 + 823*X**2*Y + 455*X**2 - 2064*X*Y**3 - 10461*X*Y**2 \
    - 34776*X*Y - 6699*X + 14792*Y**3 + 57491*Y**2 + 332717*Y
f = sp.Poly(f,X,Y)
print("irreducible over QQ:", len(sp.factor_list(f.as_expr())[1])==1, sp.factor_list(f.as_expr())[1])
print("total degree:", f.total_degree())

# affine singular locus
fx = sp.diff(f.as_expr(),X); fy = sp.diff(f.as_expr(),Y)
sols = sp.solve([f.as_expr(), fx, fy], [X,Y], dict=True)
print("affine singular points:", sols)
