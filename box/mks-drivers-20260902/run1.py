import sympy as sp
from tree import analyse, Skip, x, y

maps = [
 ("id",            x, y),
 ("(x,y+x^2)",     x, y+x**2),
 ("(x,y+x^3)",     x, y+x**3),
 ("(x,y+x^4)",     x, y+x**4),
 ("(x,y+x^5)",     x, y+x**5),
 ("(x+y^2,y)",     x+y**2, y),
 ("(x,xy)",        x, x*y),
 ("(xy,y)",        x*y, y),
 ("(x,y^2)",       x, y**2),
 ("(x,y^3)",       x, y**3),
 ("(x,xy^2)",      x, x*y**2),
 ("(x,x^2y)",      x, x**2*y),
 ("(x,x^2y^2)",    x, x**2*y**2),
 ("(x^2,y^2)",     x**2, y**2),
 ("(x^3,y^2)",     x**3, y**2),
 ("(x^2y,y)",      x**2*y, y),
 ("(x,x^3y^2)",    x, x**3*y**2),
 ("(x,y+x^4)b",    x, y+x**4),
 ("(xy^2,xy)",     x*y**2, x*y),
 ("(x^2y,xy)",     x**2*y, x*y),
 ("(x,x(x-1)(x-2)y^2)", x, x*(x-1)*(x-2)*y**2),
]
hdr = "%-22s %4s %3s %6s %5s %4s %4s %4s %5s %5s %6s %6s %5s %4s %4s %4s %4s %4s"
print(hdr % ("map","D","N","sum a","suma2","kap","Sn","T","Lam","Psi","Z.K1","Z.K2","Theta","lvs","frk","vE0","xi","ell"))
for nm,P,Q in maps:
    try:
        r = analyse(P,Q)
    except Skip as e:
        print("%-22s SKIP %s"%(nm,e)); continue
    ok = (r['Zsq']==r['N']) and (r['ZK1']==r['ZK2']) and r['okc'] and (r['sa2']==r['D']**2-r['N'])
    fg = (r['ZK1'] == r['Psi']-r['Lam']-r['kappa'])
    th = (r['ZK1'] == r['Theta']-r['kappa']-r['Sn'])
    lb = (r['leaves'] <= r['xi']+r['ell'] + (1 if r['divs']['E0']['deg']==1 else 0))
    print(hdr % (nm,r['D'],r['N'],r['sa'],r['sa2'],r['kappa'],r['Sn'],r['T'],r['Lam'],r['Psi'],
                 r['ZK1'],r['ZK2'],r['Theta'],r['leaves'],r['fork'],r['valE0'],r['xi'],r['ell']),
          " ok" if ok else " **FAIL**", "FG" if fg else "**FG-FAIL**", "TH" if th else "**TH-FAIL**",
          "LB" if lb else "**LB-FAIL**")
