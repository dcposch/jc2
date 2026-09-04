#!/usr/bin/env python3
"""Exact identities linking facial factors of rho_t to axis coefficients of the top-tail rows (toptail box rows_t*_exact.sing,
ideal TT = T_1..T_{2t-1}, variables b4,q2_0,..,q(t-1)_0,b3, parameter yy):
 t=4: [q3^8]R_2 = alpha_4^2 * ([q3^4]T_{4,5})^2      (Q_0|q3 = alpha b3^2 ; Q_2|q3 = c q3^4)
 t=5: [q3^10]R_3 = Res_b3(Q_0|q3, Q_3|q3) with Q_0|q3 = alpha b3^2 + [b3 q3^2]T_9 b3 + [q3^4]T_9, Q_3|q3 = [b3^2 q3]T_6 b3^2 + [b3 q3^3]T_6 b3 + [q3^5]T_6
 t=6: [q5^6]R_1 = alpha_6^2 * ([q5^3]T_{6,10})^2 ; [q4^8]R_2 = Res_b3(Q_0|q4, Q_2|q4): Q_0|q4 = alpha b3^2 + 0 + 0 (wt 7, 14 not multiples of 4) ; Q_2|q4: a_2 wt 2 no, b_2 wt 9 no, c_2 wt 16 -> [q4^4]T_9  => alpha^2 ([q4^4]T_{6,9})^2
Compare with the AXIS values in t*_pieces_exact.out."""
import re, sys
from fractions import Fraction
sys.path.insert(0,'.')
import norms
from macaulay_window import parse_ideal, terms
from face_resultants import A, parse_exact
def load_rows(t):
    vars_=["b4"]+[f"q{j}_0" for j in range(2,t)]+["b3"]
    polys=parse_ideal(f"/home/ubuntu/jc2/box/k16toptail-20260903/rows_t{t}_exact.sing")
    return vars_, {k+1:parse_exact(pl,vars_) for k,pl in enumerate(polys)}
def cf(P,vars_,mon,t):
    e=[0]*len(vars_)
    for v,k in mon.items(): e[vars_.index(v)]=k
    a,b=P.get(tuple(e),(Fraction(0),Fraction(0))); return A(t,a,b)
def axis_value(path,var,r):
    for line in open(path):
        m=re.match(rf"AXIS var={re.escape(var)} r={r} : (\(.*\))\*(\S+)$", line.strip())
        if m:
            a,b=norms.parse(m.group(1)); return a,b
    return None
def same(x,ab): return x.a==ab[0] and x.b==ab[1]
# t=4
t=4; vars_,T=load_rows(4)
alpha=cf(T[7],vars_,{"b3":2},t); c=cf(T[5],vars_,{"q3_0":4},t)
val=alpha*alpha*c*c; ax=axis_value("t4_pieces_exact.out","q3_0",2)
print("t=4: alpha_4 =",alpha," [q3^4]T_{4,5} =",c," N =",c.norm()); print("   alpha^2 c^2 == [q3^8]R_2 :",same(val,ax))
# t=5
t=5; vars_,T=load_rows(5)
a0=cf(T[9],vars_,{"b3":2},t); b0=cf(T[9],vars_,{"b3":1,"q3_0":2},t); c0=cf(T[9],vars_,{"q3_0":4},t)
a3=cf(T[6],vars_,{"b3":2,"q3_0":1},t); b3=cf(T[6],vars_,{"b3":1,"q3_0":3},t); c3=cf(T[6],vars_,{"q3_0":5},t)
R=(a0*c3-a3*c0)*(a0*c3-a3*c0)-(a0*b3-a3*b0)*(b0*c3-b3*c0); ax=axis_value("t5_pieces_exact.out","q3_0",3)
print("t=5: q3-axis Q_0| coefficients zero? b0:",b0.iszero(),"c0:",c0.iszero()," Q_3| a3,b3,c3 zero?",a3.iszero(),b3.iszero(),c3.iszero())
print("   Res_b3(Q_0|q3,Q_3|q3) == [q3^10]R_3 :",same(R,ax))
# t=6
t=6; vars_,T=load_rows(6)
alpha=cf(T[11],vars_,{"b3":2},t); c=cf(T[10],vars_,{"q5_0":3},t); val=alpha*alpha*c*c; ax=axis_value("t6_pieces_exact.out","q5_0",1)
print("t=6: alpha_6 =",alpha," [q5^3]T_{6,10} (=A2 of Q-PLANE) =",c); norms.describe(6,f"({c.a}*yy+{c.b})","N([q5^3]T_{6,10})")
print("   alpha^2 c^2 == [q5^6]R_1 :",same(val,ax))
print("   predicted N(A2) numerator factors at t=6: 3*t^2*(t-1)^6*(t+1)*(t+2)^6*(3t+1)^2*(4t+1)*(t^2+3t+6)*(25t^2+12t-12)*Q4^3 with Q4=102000=2^4*3*5^3*17")
c4=cf(T[9],vars_,{"q4_0":4},t); b0=cf(T[11],vars_,{"b3":1,"q4_0":1},t)
val4=alpha*alpha*c4*c4; ax4=axis_value("t6_pieces_exact.out","q4_0",2)
print("t=6: [q4^4]T_{6,9} =",c4," alpha^2 c^2 == [q4^8]R_2 :",same(val4,ax4))
