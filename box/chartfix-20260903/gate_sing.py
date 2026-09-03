#!/usr/bin/env python3
"""gate_sing.py -- emit Singular programs that build the d'=2,e'=3 two-point chart
natively (no sympy).  Top face y^{V2'}(y-x).  sigma_1 = pi (delta_1'=0):
 ord h(sigma_1) = V2'*0 + u'*(-1) = -1  => deg_x h <= 1
 ord f_2(sigma_1) >= 2*(-1)             => deg_x beta <= 2   (f = h^2 + 2 beta)
 ord g_i(sigma_1) >= i*(-1)             => deg_x g_i <= i    (g = h^3 + g1 h^2 + g2 h + g3)
Variants: R1b = corrected h, full beta, g forced (h^3+3 beta h+3/2 alpha, beta^2 = alpha h + gamma)
          R2  = corrected h, full beta, g by Theorem 1.2 only.
"""
import sys, os
n, m, M2, V2, k = [int(t) for t in sys.argv[1].split(',')]
variant = sys.argv[2]; char = sys.argv[3]
alg = sys.argv[4] if len(sys.argv) > 4 else os.environ.get('ALG', 'std')
order = sys.argv[5] if len(sys.argv) > 5 else os.environ.get('ORDER', 'dp')
from math import gcd
K = gcd(n, m); assert V2 == K - 1 and n - M2 - 1 == k + 1
hp = ['h_0_%d' % j for j in range(K)] + ['h_1_%d' % j for j in range(K - 1)]
bp = ['b_%d_%d' % (i, j) for i in range(3) for j in range(K)]
gp = []
if variant == 'R2':
    gp = ['g%d_%d_%d' % (d, i, j) for d in (1, 2, 3) for i in range(d + 1) for j in range(K)]
params = hp + bp + gp
L = []
L.append('ring S=%s,(y,x,%s,c,T),(dp(1),dp(%d));' % (char, ','.join(params), len(params) + 3))
L.append('poly h = y^%d - x*y^%d + %s;' % (K, K - 1, ' + '.join(['h_0_%d*y^%d' % (j, j) for j in range(K)] + ['h_1_%d*x*y^%d' % (j, j) for j in range(K - 1)])))
L.append('poly beta = %s;' % ' + '.join('b_%d_%d*x^%d*y^%d' % (i, j, i, j) for i in range(3) for j in range(K)))
L.append('poly f = h^2 + 2*beta;')
if variant == 'R1b':
    L.append('poly rem = reduce(beta^2, h); poly alpha = (beta^2 - rem)/h;')
    L.append('if (alpha*h + rem - beta^2 != 0) { print("DIVISION_FAIL"); quit; }')
    L.append('poly g = h^3 + 3*beta*h + (3/2)*alpha;')
else:
    for d in (1, 2, 3):
        L.append('poly g%d = %s;' % (d, ' + '.join('g%d_%d_%d*x^%d*y^%d' % (d, i, j, i, j) for i in range(d + 1) for j in range(K))))
    L.append('poly g = h^3 + g1*h^2 + g2*h + g3;')
L.append('poly J = diff(f,x)*diff(g,y) - diff(f,y)*diff(g,x);')
L.append('poly E = J - c*x^%d;' % k)
L.append('print("SANITY_GATE required_k=%d chart=%s");' % (k, variant))
L.append('print("degx_f degx_g degx_J:"); deg(f,intvec(0,1,%s)); deg(g,intvec(0,1,%s)); deg(J,intvec(0,1,%s));' % (('0,' * (len(params) + 2))[:-1], ('0,' * (len(params) + 2))[:-1], ('0,' * (len(params) + 2))[:-1]))
L.append('ideal Eq; matrix Mx = coeffs(E, x); int i; int j; matrix My;')
L.append('for (i=1; i<=nrows(Mx); i++) { My = coeffs(Mx[i,1], y); for (j=1; j<=nrows(My); j++) { if (My[j,1] != 0) { Eq = Eq, My[j,1]; } } }')
L.append('Eq = simplify(Eq, 2);')
L.append('ring R=%s,(%s,c,T),%s; option(redSB);' % (char, ','.join(params), 'lp' if order == 'elim' else 'dp'))
L.append('ideal I = imap(S, Eq); I = I, T*c-1;')
L.append('ideal CE=c,T*c-1; ideal GE=std(CE); if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }')
L.append('ideal CN=c-1,T*c-1; ideal GN=std(CN); if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }')
L.append('print("MAIN_START equations=" + string(size(I)-1) + " unknowns=" + string(nvars(R)-1) + " char=%s alg=%s order=%s");' % (char, alg, order))
L.append('ideal G = %s(I); print("MAIN_DONE basis_size="); size(G);' % ('modStd' if alg == 'modStd' else ('slimgb' if alg == 'slimgb' else 'std')))
L.append('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); print("dim="); dim(G); }')
L.append('quit;')
if alg == 'modStd':
    L.insert(0, 'LIB "modstd.lib";')
stem = '%s_%d_%d_%d_%d_k%d_%s_%s_%s' % (variant, n, m, M2, V2, k, 'Q' if char == '0' else 'mod' + char, alg, order)
os.makedirs('indep', exist_ok=True)
open(os.path.join('indep', stem + '.sing'), 'w').write('\n'.join(L) + '\n')
print(stem)
