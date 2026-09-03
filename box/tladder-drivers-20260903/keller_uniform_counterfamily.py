#!/usr/bin/env python3
"""Uniform negative control for the proposed gamma-degree ladder.

For integers k>=0, s>k+1, r>=2, p>=2 put
    X=x+y,  Y=x^(k+1)/(k+1),  U=Y+phi(X),
    H=X+U^r,  P=H^p+U,  Q=H,
where phi is an arbitrary monic degree-s polynomial.  Characteristic zero is
required for 1/(k+1).  We use J(A,B)=A_x*B_y-A_y*B_x.

The proof is performed in the differential ring Q(k,r,p)[X,Y,phi(X)] and
then composed with (x,y)->(X,Y).  This avoids expanding degree p*r*s
polynomials and works uniformly in all four integer parameters.
"""
import sympy as sp

X, Y = sp.symbols("X Y")
r, p = sp.symbols("r p", integer=True, positive=True)
phi = sp.Function("phi")
U = Y+phi(X)
H = X+U**r
P = H**p+U
Q = H


def jac(u, v, z, w):
    return sp.diff(u, z)*sp.diff(v, w)-sp.diff(u, w)*sp.diff(v, z)


J_XY = sp.simplify(jac(P, Q, X, Y))
assert J_XY == -1

x, y = sp.symbols("x y")
k = sp.symbols("k", integer=True, nonnegative=True)
Xxy = x+y
Yxy = x**(k+1)/(k+1)
J_change = sp.simplify(jac(Xxy, Yxy, x, y))
assert J_change == -x**k
assert sp.expand(J_XY*J_change) == x**k

print("RING: characteristic-zero polynomial ring; J=Ax*By-Ay*Bx")
print("UNIFORM_IDENTITY: J_XY(P,Q)=-1 and J_xy(X,Y)=-x^k")
print("THEREFORE: J_xy(P,Q)=x^k")
print("H_ADIC_EXPANSION: P=H^p+U, Q=H (so q=1)")
print("  exactly one nonconstant lower digit, U=Y+phi(X)")
print("DEGREE_DATA for monic deg(phi)=s>k+1, r>=2:")
print("  deg=deg_y H=r*s=d; deg=deg_y P=p*d; gcd=d")
print("  deg_x U=s, which is unbounded and exceeds k+1")
print("  phi has s free scalar coefficients; s is arbitrary")
print("KELLER_CASE k=0:")
print("  (x,y)->(X=x+y,Y=x), (X,Y)->(X,U), (X,U)->(H,U),")
print("  (H,U)->(P=H^p+U,Q=H) are polynomial triangular/linear automorphisms")
print("  and their ordered Jacobian product is +1")
print("CONCLUSION: the claimed deg_x(nonconstant digit)<=k+1 fails already")
print("  for Keller automorphisms, at fixed (k,p,q,r)=(0,p,1,r), as s grows.")
print("  The number of nonconstant digits stays 1; its x-degree and phi-moduli grow.")
