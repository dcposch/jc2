#!/usr/bin/env python3
"""Uniform near-axis structure: the b3^2 coefficient of T_{t,2t-1} (alpha_t, offset 0) and its
b3-linear companions are weight-forced; here we also record the Sol pivot norms that enter every
b4-carrying coefficient, showing why those have no polynomial-in-t closed form:
the C_1 pivot rhs on the b4-axis has denominator divisible by the odd part of F_C(t,1)."""
import sympy as sp
t, j = sp.symbols("t j")
A_c = (9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j+72*t**3+144*t*t+88*t+16)
B_c = (-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j-12*t**3-20*t*t-8*t)
F_c = sp.factor(-(3*B_c**2-A_c**2*(t+1))/(3*t+2)**3)
A_q = 12*t*t+16*t+4-j*(3*t+4); B_q = 2*(t+1)*(j-t)
F_q = sp.factor(-(3*B_q**2-A_q**2*(t+1))/((t+1)*(3*t+2)**2))
for tv in range(2, 8):
    print("t=%d  F_C(t,1)=%s  F_C(t,j) j=1..t-1: %s   F_Q(t,j) j=t..2t: %s" % (
        tv, sp.factorint(F_c.subs({t: tv, j: 1})),
        [int(F_c.subs({t: tv, j: jj})) for jj in range(1, tv)],
        [int(F_q.subs({t: tv, j: jj})) for jj in range(tv, 2*tv+1)]))
