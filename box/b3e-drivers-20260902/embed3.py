import sympy as sp
X,Y,t,u,w,v,z = sp.symbols('X Y t u w v z')
f = 72*X**2*Y**3 + 450*X**2*Y**2 + 823*X**2*Y + 455*X**2 - 2064*X*Y**3 - 10461*X*Y**2 \
    - 34776*X*Y - 6699*X + 14792*Y**3 + 57491*Y**2 + 332717*Y

# --- local type at the affine singular point (15,1)
g = sp.expand(f.subs({X:X+15, Y:Y+1}))
gp = sp.Poly(g, X, Y)
def homo_part(poly, d):
    return sum(c*X**m[0]*Y**m[1] for m,c in zip(poly.monoms(), poly.coeffs()) if sum(m)==d)
for d in range(0,5):
    print("order",d,"part:", sp.factor(homo_part(gp,d)))
print("Milnor number mu at (15,1):", )
gx, gy = sp.diff(g,X), sp.diff(g,Y)
# mu = dim C[[X,Y]]/(gx,gy); compute via Groebner in local ring -> use standard basis substitute:
G = sp.groebner([gx,gy],X,Y,order='lex')
print("  ideal (gx,gy) zero-set:", sp.solve([gx,gy],[X,Y],dict=True))
