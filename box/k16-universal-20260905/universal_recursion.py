#!/usr/bin/env python3
"""Universal Briot-Bouquet recursion of (UF) at x=0, written out with GENERIC jets of L.

(UF):  (theta-3)(P^2) + G P = R,  theta = x d/dx,
       G = (3/2) L (L+b) - B x,   R = (3/16) L^2 (L (L+2b) - 4 B x) - eta x^2 (b L/2 + B x),
       L = -b + l_2 x^2 + l_3 x^3 + ...  (l_0=-b, l_1=0),  P = -b^2/4 - B x + eta x^2 + w2 x^3 + ...

Row x^k:  (k-3) [x^k](P^2) + [x^k](G P) - R_k = 0.
Checks (all symbolic, t-independent):
  (A) rows 0..3 vanish identically given the jets  (row 3 = the resonance compatibility);
  (B) pivot of P_k in row k is -(k-3) b^2/2  (G_0 = 0);
  (C) the recursion is QUADRATIC in the P-coefficients (convolution term), not linear;
  (D) l_k and l_{k-1} cancel in row k; row k is LINEAR in l_{k-2} with coefficient -(b/4)(4 eta + 3 b l_2)
      (k>=5), so Phi_k depends on l_2..l_{k-2} only, and its l_{k-2}-coefficient is -(4eta+3b l_2)/(2b(k-3));
  (E) exact b-denominator of Phi_k;
  (F) tacnode: Q_P(0,L) = (3/16)(L+b)^2(L^2+b^2) where Q_P = R - G P - (theta-3)P^2 as a quartic in L;
      d_L Q_P along the branch = (b/4)(4eta+3b l_2) x^2 + O(x^3);
  (G) residue of P'/P at infinity gives exactly (UT): (4N-3)p^2 + (3/2)p - 3/16 = 0, p = omega*lc(L)^-2... (see report)
  (H) BB exponent at infinity: lambda_inf = 4N + 6d, pivot 2 omega (lambda_inf - m) for Q_m (P = x^{2N} Q(1/x)).
"""
import json, sys, time
import sympy as sp
t0=time.time()
K = int(sys.argv[1]) if len(sys.argv)>1 else 9
x,b,B,eta,w2 = sp.symbols('x b B eta w2')
ls = {j: sp.Symbol(f'l{j}') for j in range(2,K+1)}
Lser = -b + sum(ls[j]*x**j for j in range(2,K+1))
G = sp.expand(sp.Rational(3,2)*Lser*(Lser+b) - B*x)
R = sp.expand(sp.Rational(3,16)*Lser**2*(Lser*(Lser+2*b)-4*B*x) - eta*x**2*(b*Lser/2+B*x))
def coeff(f,k): return sp.expand(f).coeff(x,k)
Gc = {k: coeff(G,k) for k in range(0,K+1)}
Rc = {k: coeff(R,k) for k in range(0,K+1)}
out = {}
out['G0_zero'] = bool(sp.simplify(Gc[0])==0)
# generic P coefficients as symbols to check pivots/linearity: use symbols Pk for rows
Psym = {k: sp.Symbol(f'P{k}') for k in range(0,K+1)}
def row_generic(k):
    # (k-3) sum_{i+j=k} P_i P_j + sum_i G_i P_{k-i} - R_k, with symbolic P's
    s = (k-3)*sum(Psym[i]*Psym[k-i] for i in range(0,k+1)) + sum(Gc[i]*Psym[k-i] for i in range(0,k+1)) - Rc[k]
    return sp.expand(s)
jets = {Psym[0]: -b**2/4, Psym[1]: -B, Psym[2]: eta, Psym[3]: w2}
# (A) rows 0..3
rows_low = {k: sp.simplify(row_generic(k).subs(jets)) for k in range(0,4)}
out['rows_0_3_identically_zero'] = {k: bool(v==0) for k,v in rows_low.items()}
# row 0 without the jet: -3 P0^2 + 3b^4/16 -> P0 = +-b^2/4
out['row0_generic'] = str(sp.factor(row_generic(0)))
# (B),(C): pivots and quadratic structure
piv = {}; quad = {}
for k in range(1,K+1):
    r = row_generic(k).subs({Psym[0]: -b**2/4})
    piv[k] = sp.factor(sp.diff(r, Psym[k]))
    # quadratic part in P_1..P_{k-1}
    poly = sp.Poly(r, *[Psym[i] for i in range(1,k)])
    quad[k] = poly.total_degree() if k>1 else 0
out['pivot_Pk'] = {k: str(piv[k]) for k in piv}
out['pivot_law_ok'] = all(sp.simplify(piv[k] + (k-3)*b**2/2)==0 for k in piv)
out['row_total_degree_in_P1..Pk-1'] = quad
# Now the actual recursion Phi_k (rational functions of the data)
P = {0: -b**2/4, 1: -B, 2: eta, 3: w2}
Phi = {}
for k in range(4,K+1):
    br = (k-3)*sum(P[i]*P[k-i] for i in range(1,k)) + sum(Gc[i]*P[k-i] for i in range(1,k+1)) - Rc[k]
    P[k] = sp.cancel(sp.together(br*2/((k-3)*b**2)))
    Phi[k] = P[k]
# (D) dependence
dep = {}; lin = {}; lcoef = {}
for k in range(4,K+1):
    num,den = sp.fraction(sp.together(Phi[k]))
    present = sorted([j for j in ls if Phi[k].has(ls[j])])
    dep[k] = present
    if k>=5:
        lin[k] = sp.Poly(sp.expand(num), ls[k-2]).degree()
        lcoef[k] = sp.factor(sp.diff(Phi[k], ls[k-2]))
    # den
    out.setdefault('denominator_Phi_k', {})[k] = str(sp.factor(den))
out['Phi_k_depends_on_l'] = {k: [str(ls[j]) for j in v] for k,v in dep.items()}
out['Phi_k_degree_in_l_{k-2}'] = lin
out['Phi_k_coeff_of_l_{k-2}'] = {k: str(v) for k,v in lcoef.items()}
out['Lpivot_law_ok'] = all(sp.simplify(lcoef[k] + (4*eta+3*b*ls[2])/(2*b*(k-3)))==0 for k in lcoef)
out['Phi_4'] = str(sp.factor(Phi[4]))
out['Phi_5'] = str(sp.expand(Phi[5]))
out['Phi_6_numterms'] = len(sp.Add.make_args(sp.expand(sp.fraction(sp.together(Phi[6]))[0])))
# how far does the truncated Phi_4 as polynomial in eta factor? (structure)
out['Phi_4_times_b2_over_2'] = str(sp.expand(Phi[4]*b**2/2))
# (F) tacnode
Lv = sp.Symbol('Lv')
Pgen = sum(Psym[k]*x**k for k in range(0,K+1))
Ggen = sp.Rational(3,2)*Lv*(Lv+b) - B*x
Rgen = sp.Rational(3,16)*Lv**2*(Lv*(Lv+2*b)-4*B*x) - eta*x**2*(b*Lv/2+B*x)
thetaP2 = sp.expand(x*sp.diff(Pgen**2,x) - 3*Pgen**2)
Q = sp.expand(Rgen - Ggen*Pgen - thetaP2)
Q0 = sp.factor(Q.subs(x,0).subs(Psym[0], -b**2/4))
out['Q_P_at_x0'] = str(Q0)
out['Q_P_at_x0_is_tacnode_form'] = bool(sp.simplify(Q0 - sp.Rational(3,16)*(Lv+b)**2*(Lv**2+b**2))==0)
# d_L Q along the branch, with P_k = Phi_k (truncate to order x^3 suffices) 
dQ = sp.diff(Q, Lv)
Lbr = -b + ls[2]*x**2 + ls[3]*x**3
subsP = {Psym[0]: -b**2/4, Psym[1]: -B, Psym[2]: eta, Psym[3]: w2}
subsP.update({Psym[k]: 0 for k in range(4,K+1)})  # irrelevant below order x^3 -> keep generic? P4 enters at x^4 only
dQbr = sp.expand(dQ.subs(Lv, Lbr).subs(subsP))
out['dLQ_branch_x0'] = str(sp.factor(dQbr.coeff(x,0)))
out['dLQ_branch_x1'] = str(sp.factor(dQbr.coeff(x,1)))
out['dLQ_branch_x2'] = str(sp.factor(dQbr.coeff(x,2)))
out['dLQ_x2_is_Lpivot'] = bool(sp.simplify(dQbr.coeff(x,2) - b*(4*eta+3*b*ls[2])/4)==0)
# the quartic Q_P in L: coefficients
QL = sp.Poly(Q, Lv)
out['Q_P_quartic_coeffs_in_L'] = [str(sp.factor(c)) for c in QL.all_coeffs()]
# (G) residue at infinity: P ~ om x^{2N}, L ~ lam x^N; P'/P = 3/(2x) - G/(2xP) + R/(2xP^2)
N, om, lam, pp = sp.symbols('N omega lambda p')
coef_inv_x = sp.Rational(3,2) - (sp.Rational(3,2)*lam**2)/(2*om) + (sp.Rational(3,16)*lam**4)/(2*om**2)
UT = sp.expand((coef_inv_x - 2*N)*om**2/lam**4)  # divide to normalise: p = om/lam^2
UTp = sp.expand(UT.subs(om, pp*lam**2)/ 1)
out['residue_infty_identity_in_p'] = str(sp.factor(sp.expand(UTp*lam**0)))
UTref = (4*N-3)*pp**2 + sp.Rational(3,2)*pp - sp.Rational(3,16)
ratio = sp.simplify(UTp/UTref)
out['residue_infty_over_UT_ratio'] = str(ratio)
out['residue_infty_equals_UT'] = bool(ratio.is_number and ratio!=0)
out['UT_normalised'] = str(sp.factor(sp.expand(-UTp)))
# (H) BB exponent at infinity: Q(u) with P = u^{-2N} Q(u): (4N-3)Q^2 - 2u Q Q' + Ghat Q = Rhat
d = sp.Symbol('d'); y = sp.Symbol('y')
omv = 1/(4*y**2*(2*d+1)); Ghat0 = sp.Rational(3,2)/y**2
lam_inf = sp.simplify((4*N-3) + Ghat0/(2*omv))
out['BB_exponent_at_infinity'] = str(sp.factor(lam_inf))
out['BB_exponent_at_infinity_is_4N_plus_6d'] = bool(sp.simplify(lam_inf-(4*N+6*d))==0)
m = sp.Symbol('m')
out['pivot_at_infinity_2om(lam-m)_equals_report_lambda'] = bool(sp.simplify(2*omv*(lam_inf-(2*N-m)) - 2*omv*(2*N+m+6*d))==0)
out['elapsed_s'] = round(time.time()-t0,1)
out['ALL_PASS'] = bool(out['G0_zero'] and all(out['rows_0_3_identically_zero'].values()) and out['pivot_law_ok'] and out['Lpivot_law_ok'] and out['Q_P_at_x0_is_tacnode_form'] and out['dLQ_x2_is_Lpivot'] and out['residue_infty_equals_UT'] and out['BB_exponent_at_infinity_is_4N_plus_6d'] and all(v==1 for v in lin.values()))
json.dump(out, open(sys.argv[0].replace('.py','.json'),'w'), indent=1, default=str)
for k,v in out.items(): print(k, '=', v)

# ---- dual (L-) recursion consistency: from generic data build P via the P-recursion, then recover l_3..l_{K-2}
# from the rows via  l_{k-2} = 4 (rest_k - (k-3) b^2 P_k / 2) / (b (4 eta + 3 b l_2)),  rest_k = bracket_k |_{l_{k-2}=l_{k-1}=l_k=0}
dual_ok = True
for k in range(5, K-1):
    br = (k-3)*sum(P[i]*P[k-i] for i in range(1,k)) + sum(Gc[i]*P[k-i] for i in range(1,k+1)) - Rc[k]
    rest = br.subs({ls[k-2]:0, ls[k-1]:0, ls[k]:0})
    lrec = sp.cancel(4*(rest - (k-3)*b**2*P[k]/2)/(b*(4*eta+3*b*ls[2])))
    dual_ok = dual_ok and (sp.simplify(lrec - ls[k-2])==0)
out['dual_L_recursion_recovers_l_{k-2}_for_k=5..%d'%(K-2)] = bool(dual_ok)
# Bη appears in row 3 only through G_1 P_2 and the eta-term of R_3, and cancels:
r3 = row_generic(3).subs(jets)
out['row3_Beta_terms'] = str(sp.expand(Gc[1]*eta)) + '  (G_1 P_2)  vs  ' + str(sp.expand(-Rc[3]).coeff(B,1).coeff(eta,1)*B*eta) + '  (from -R_3)'
out['ALL_PASS'] = bool(out['ALL_PASS'] and dual_ok)
json.dump(out, open(sys.argv[0].replace('.py','.json'),'w'), indent=1, default=str)
print('dual_L_recursion_ok =', dual_ok); print('row3_Beta_terms =', out['row3_Beta_terms']); print('ALL_PASS =', out['ALL_PASS'])
