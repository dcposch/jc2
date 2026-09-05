#!/usr/bin/env python3
"""Moh 1983 (J. reine angew. Math. 340), Definition 5.1 (p.179) -> the identity
   used unlabelled in the proof of Prop 5.4 (p.183) and quoted in Lemma 5.3 (p.185):

       delta_i = -1 / (n - M_i - 1).

Def 5.1(2):  V_{j+1} d_j / d_{j+1} >= V_j > d_j/(n-M_j)  for j=r+1..s,  V_{s+1}=d_{s+1}.
Def 5.1(3):  delta_i = 1 - [ (n-M_i)   prod_{j=i+1..s} (V_j (n-M_j)     - d_j) ]
                         / [ (n-M_s-1) prod_{j=i+1..s} (V_j (n-M_{j-1}) - d_j) ].

Prop 5.4 picks i = max { r : V_{r+1} d_r / d_{r+1} > V_r }.  By maximality of i and the
">=" of Def 5.1(2), equality V_{j+1} d_j = V_j d_{j+1} holds for every j = i+1..s, i.e.
V_j/d_j is constant on j=i+1..s+1; with V_{s+1}=d_{s+1} this gives V_j = d_j there.
Substituting, the products telescope.  NOTE: the derivation uses NO hypothesis on the
sign of delta_i, so the identity -- hence delta_i >= -1 -- is unconditional.
"""
import sympy as sp

ok = True
for s in range(1, 9):
    for i in range(1, s + 1):
        n = sp.Symbol('n')
        M = [None] + [sp.Symbol('M%d' % j) for j in range(1, s + 1)]
        d = [None] + [sp.Symbol('d%d' % j) for j in range(1, s + 2)]
        V = [None] * (s + 2)
        for j in range(i + 1, s + 2):
            V[j] = d[j]                      # forced, see docstring
        num = (n - M[i]) * sp.prod([V[j] * (n - M[j]) - d[j] for j in range(i + 1, s + 1)])
        den = (n - M[s] - 1) * sp.prod([V[j] * (n - M[j - 1]) - d[j] for j in range(i + 1, s + 1)])
        delta = sp.simplify(1 - num / den)
        resid = sp.simplify(delta - sp.Integer(-1) / (n - M[i] - 1))
        status = 'OK' if resid == 0 else 'MISMATCH %s' % resid
        ok &= (resid == 0)
        print('s=%d i=%d  delta_i - (-1/(n-M_i-1)) = %s   [%s]' % (s, i, resid, status))
print()
print('IDENTITY_UNCONDITIONAL=%s' % ok)
# n - M_i - 1 >= 1 because M_i <= M_s and M_s := largest M_i strictly less than n-1 (p.176,
# Prop 5.2).  Hence delta_i = -1/l with l >= 1 integer, so delta_i in {-1,-1/2,-1/3,...}:
print('CONSEQUENCE: delta_i >= -1 always, with delta_i = -1 <=> n - M_i - 1 = 1 <=> M_i = n-2.')
