import sympy as sp

t = sp.symbols('t')
# candidate: 5 simple poles at t=0,1,2 (-> point [0:1:0]) and t=3,4 (-> [0:0:1])
x = (149*t**2 - 785*t + 1100)/(t*(t-1)*(t-2))
y = (3*t - 13)/((t-3)*(t-4))

print("x(3),x(4) =", sp.simplify(x.subs(t,3)), sp.simplify(x.subs(t,4)))
print("y(0),y(1),y(2) =", [sp.nsimplify(y.subs(t,k)) for k in (0,1,2)])
print("x'(5)=", sp.simplify(sp.diff(x,t).subs(t,5)), " y'(5)=", sp.simplify(sp.diff(y,t).subs(t,5)))

# implicit equation of the image
X,Y = sp.symbols('X Y')
nx = sp.Poly(sp.numer(sp.together(x - X)), t)
ny = sp.Poly(sp.numer(sp.together(y - Y)), t)
R = sp.factor(sp.resultant(nx.as_expr(), ny.as_expr(), t))
print("\nresultant factored:")
print(R)
