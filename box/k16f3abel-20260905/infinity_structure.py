#!/usr/bin/env python3
"""Exact universal identities for the F3 infinity recursion; no root division.

The parameter relation is eliminated by t=3*d**2-1. y stays a nonzero
scalar, so every identity holds after the normalized value of y is inserted.
This script does not claim all-t polynomial nonexistence.
"""
import sympy as s

d, y, k = s.symbols('d y k', nonzero=True)
t = 3*d**2-1
q = 2*t+1
alpha = 3/(4*y**2)
omega = 3*(2*d-1)/(4*y**2*(4*t+1))

def check(name, f):
    ans = s.factor(f)
    assert ans == 0, (name, ans)
    print(name + '_PASS', flush=True)

check('OMEGA_SIMPLIFICATION', omega-1/(4*y**2*(2*d+1)))
check('LEADING_BALANCE', (2*q-1)*omega**2+2*alpha*omega-alpha**2/3)
check('HIGH_DIAGONAL', 2*((q+k-1)*omega+alpha)-2*omega*(k+2*t+3+6*d))
check('B_DIAGONAL', -((2*q-1)*omega+alpha)+2*d*alpha)
kstar = -2*t-3-6*d
check('RESONANCE', 2*((q+kstar-1)*omega+alpha))
check('RESONANCE_INTEGER_FORM', kstar+6*d*(d+1)+1)
check('RESONANCE_EQUATION_DEGREE', q+kstar+6*d+2)

nu = -1/(2*y*(3*d+2))
delta = 3/(2*y)
check('MONOMIAL_LINEAR_B', nu*(2*omega*(q+t-1)+2*alpha)+delta*(alpha/3-omega))
e2 = (2*t-1)*nu**2-delta*nu-(2*t-1)*omega/2-alpha/2
e3 = (2-t)*nu/2
print('MONOMIAL_B2_COEFFICIENT=' + str(s.factor(e2)), flush=True)
print('MONOMIAL_B3_COEFFICIENT=' + str(s.factor(e3)), flush=True)
check('T2_MINUS_B2', e2.subs({d:-1,y:s.Rational(1,5)}))
check('T2_MINUS_B3', e3.subs({d:-1,y:s.Rational(1,5)}))
check('T2_PLUS_B2', e2.subs({d:1,y:s.Rational(2,5)})+2)
check('T2_PLUS_B3', e3.subs({d:1,y:s.Rational(2,5)}))

# Formal series at x=0: parameters B,eta,w2,C_j are free if b!=0;
# subsequent coefficient w_(n+1) has diagonal (1-n)b^2/2.
x, b, B, eta = s.symbols('x b B eta')
ws = s.symbols('w2:9')
cs = s.symbols('c0:8')
W = -B+eta*x+sum(a*x**j for j,a in enumerate(ws,2))
C = sum(a*x**j for j,a in enumerate(cs))
A = alpha*x**3*C**2
D = 3*b*x*C/(2*y)
K = x**2*C-y*b
F = s.Poly(s.expand(2*(x*W-b**2/4)*s.diff(W,x)-W**2-(B-2*A+D)*W
                   -A*(A-D)/3+B*(A-D)+b*eta*K/(2*y)+B*eta*x
                   -b**2*A/(2*x)+b**2*(B+W)/x),x)
check('LOCAL_CONSTANT', F.nth(0))
check('LOCAL_LINEAR', F.nth(1))
for n in range(2,8):
    check(f'LOCAL_BNONZERO_DIAGONAL_{n}', s.diff(F.nth(n),ws[n-1])-(1-n)*b**2/2)
for n in range(2,9):
    check(f'LOCAL_BZERO_DIAGONAL_{n}', s.diff(F.nth(n).subs(b,0),ws[n-2])+(2*n-1)*B)
print('INFINITY_AND_LOCAL_STRUCTURE_DONE', flush=True)
