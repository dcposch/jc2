import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B, opus5_probe as OP

def trace(n, m, Ms, V, tag):
    T = OP.Tree(n, m, Ms); T._memo = {}
    s = T.s
    print(f"\n--- {tag}: n={n} m={m} M={list(Ms)} V={dict(sorted(V.items()))} (s={s}) ---")
    high = (V[s],)
    for j in range(s-1, 1, -1):
        dl, L, A, P, Q, lo = T.node(j, high)
        print(f"  D_{j}: delta_{j}={dl}  L={L}  A_{j}={A}  P={P}=deg p  Q={Q}=deg q  "
              f"S=(Q-1)/A={(Q-1)//A if (Q-1)%A==0 else 'n/a'}  threshold d_{j}/(n-M_{j})={lo}")
        print(f"        selected V_{j}={V[j]};  P mod A = {P%A}  => admissible zero "
              f"multiplicities b in {list(range(P%A,P+1,A))[:6]}")
        for b in range(P % A, P+1, A):
            if F(b) > lo:
                # does the forced zero sibling have a lower tower?
                nh = (b,)+high
                if j == 2:
                    good, A1, c12, c13 = T.bottom(nh)
                    print(f"        b={b} > {lo}: forced MAJOR zero sibling -> bottom with "
                          f"V_2={b}: A_1={A1}, (12)={c12}, (13)={c13} -> "
                          f"{'ok' if good else 'FAILS (12)/(13)'}")
                else:
                    T._memo = {}
                    r = T.ok(j-1, nh, False, None)
                    print(f"        b={b} > {lo}: forced MAJOR zero sibling -> "
                          f"{'has a lower tower' if r else 'NO lower tower'}")
            else:
                print(f"        b={b} <= {lo}: zero factor minor (stops, p.200(5))")
        # selected as nonzero orbit?
        if j == 2:
            good, A1, c12, c13 = T.bottom((V[j],)+high)
            print(f"        selected V_2={V[j]} at the bottom: A_1={A1}, (12)={c12}, (13)={c13}")
        high = (V[j],)+high

for t in range(2):
    P = 7*t+6
    trace(9*P, 6*P, (4*P, 9*P-2), {2:1, 3:6*t+5}, f"A2=6 ray t={t}")
for a in range(2):
    L = 8*a+5
    trace(21*L, 14*L, (7*(3*L+1)//4, 21*L-2), {2:1, 3:5}, f"Sol ray a={a} (L={L})")
