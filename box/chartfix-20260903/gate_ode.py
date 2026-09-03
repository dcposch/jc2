#!/usr/bin/env python3
"""gate_ode.py -- level-1 chart at delta_1'=0 (sigma_1 = pi): the x^k coefficient of
J(f,g)=c x^k is Moh's r=1 ODE  D(n',-M_1', g_top, f_top) = const  (p.187 / Prop 4.6),
with f_top = x^{d'} coefficient of f (deg m*V2'), g_top = x^{e'} coefficient of g (deg n*V2').
Top faces y^{m*V2'}(y-x)^{d'}, y^{n*V2'}(y-x)^{e'} fix the leading coefficients.
   d'=2, e'=3:  2 f2 g3' - 3 f2' g3 = c,  f2 = y^12 + ..., g3 = -(y^18 + ...)   [row (21,14;15;6;4)]
"""
import sys, os
n, m, M2, V2, k = [int(t) for t in sys.argv[1].split(',')]; char = sys.argv[2]
alg = sys.argv[3] if len(sys.argv) > 3 else os.environ.get('ALG', 'std')
order = sys.argv[4] if len(sys.argv) > 4 else os.environ.get('ORDER', 'dp')
from math import gcd
K = gcd(n, m); e = n // K; d = m // K; assert (d, e) == (2, 3)
df, dg = d * V2, e * V2          # deg f2 = m* V2', deg g3 = n* V2'
a = ['a%d' % j for j in range(df)]; b = ['b%d' % j for j in range(dg)]
L = ['ring S=%s,(y,%s,c,T),(dp(1),dp(%d));' % (char, ','.join(a + b), len(a) + len(b) + 2),
     'poly f2 = y^%d + %s;' % (df, ' + '.join('a%d*y^%d' % (j, j) for j in range(df))),
     'poly g3 = -(y^%d + %s);' % (dg, ' + '.join('b%d*y^%d' % (j, j) for j in range(dg))),
     'poly E = %d*f2*diff(g3,y) - %d*diff(f2,y)*g3 - c;' % (d, e),
     'ideal Eq; matrix My = coeffs(E, y); int j; for (j=1; j<=nrows(My); j++) { if (My[j,1] != 0) { Eq = Eq, My[j,1]; } }',
     'ring R=%s,(%s,c,T),%s; option(redSB); ideal I = imap(S,Eq); I = I, T*c-1;' % (char, ','.join(a + b), 'lp' if order == 'elim' else 'dp'),
     'ideal CE=c,T*c-1; ideal GE=std(CE); if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
     'ideal CN=c-1,T*c-1; ideal GN=std(CN); if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
     'print("SANITY_GATE deg_x_J=%d required_k=%d chart=R3_level1_only");' % (k, k),
     'print("MAIN_START equations=" + string(size(I)-1) + " unknowns=" + string(nvars(R)-1) + " char=%s alg=%s order=%s");' % (char, alg, order),
     'ideal G = %s(I); print("MAIN_DONE basis_size="); size(G);' % ('modStd' if alg == 'modStd' else ('slimgb' if alg == 'slimgb' else 'std')),
     'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); print("dim="); dim(G); }',
     'quit;']
if alg == 'modStd':
    L.insert(0, 'LIB "modstd.lib";')
stem = 'R3ode_%d_%d_%d_%d_k%d_%s_%s_%s' % (n, m, M2, V2, k, 'Q' if char == '0' else 'mod' + char, alg, order)
os.makedirs('indep', exist_ok=True)
open(os.path.join('indep', stem + '.sing'), 'w').write('\n'.join(L) + '\n'); print(stem)
