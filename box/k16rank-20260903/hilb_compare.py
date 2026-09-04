import re, sys, sympy as sp, pathlib
sys.path.insert(0,'.')
from en_degree import HN
s=sp.symbols('s')
for t, path in [(3,'rank_t3_exact.out'),(4,'rank_t4_mod_p32029_b1.out'),(5,'rank_t5_mod_p32009_b0.out'),(6,'rank_t6_mod_p32003_b0.out')]:
    p=pathlib.Path(path)
    if not p.exists(): print(t,'missing'); continue
    lines=p.read_text().splitlines()
    for i,l in enumerate(lines):
        if l.startswith('CURVE hilb(P/I2)'):
            coeffs=[int(x) for x in lines[i+1].strip().rstrip(',').split(',')]
            poly=sum(c*s**k for k,c in enumerate(coeffs))
            hn=HN(t)
            print(f"t={t}: Singular numerator degree {len(coeffs)-1} (with bookkeeping zero); EN formula minus Singular = {sp.expand(hn-poly)}")
            break
    else:
        print(t,'no hilb line yet')
