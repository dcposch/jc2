import sympy as sp
e,n,al,be,ga,de,ep,rho = sp.symbols('e n alpha beta gamma delta epsilonhat rho')
N3 = be - ga + de/2 - rho
N1 = al - be + de/2
N4 = n*al - 2*be - (n-2)*ga + (n-1)*de
N2 = (2*n-2*e-3)*al - 2*(3*n+2*e-4)*be + (4*n+2*e-5)*ga - (n-1)*de - ep
print("N4 - [ n*N1 + (n-2)*N3 ]  =", sp.simplify(sp.expand(N4 - (n*N1 + (n-2)*(N3+rho)))))
print("  => with rho carried:  n*N1 + (n-2)*N3 - N4 = -(n-2)*rho ;  check:",
      sp.simplify(sp.expand(n*N1 + (n-2)*N3 - N4 + (n-2)*rho)))
sol = sp.solve([N1, N3.subs(rho,0)], [al, ga], dict=True)[0]
print("homogeneous solution: alpha =", sol[al], ", gamma =", sol[ga])
print("epsilonhat on it     =", sp.simplify(sp.expand(N2.subs(sol).subs(ep,0))), " (so ep = that)")
print("check ep + 4 e alpha =", sp.simplify(sp.expand(N2.subs(sol).subs(ep,0) + 4*e*sol[al])))
print()
print("cell sizes for the job spec (vars, eqs) with a=b=A_e=1 and, for U>3e, S_sigma=1:")
from cell import build_cell
for (E,U) in [(1,3),(1,5),(1,7),(1,9),(2,6),(2,8),(2,10),(3,9),(3,11),(4,12),(4,14),(5,15)]:
    eqs,V,info=build_cell(E,U,normS=(U>3*E))
    print("   (e,U)=(%d,%2d)  g=%d sig=%d m=%d n=%d   vars=%3d  eqs=%3d"
          %(E,U,info['g'],info['sig'],info['m'],info['n'],len(V),len(eqs)))
