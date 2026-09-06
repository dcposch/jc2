import sys, json
from fractions import Fraction as F
from math import gcd, lcm
from collections import Counter
sys.path.insert(0, "/home/ubuntu/jc2/box/actual-stabilizer-soundness-20260906")
from verify import B, Tree, op_actual, op_coarse

# ---- Moh p.207 Appendix II descended table: 5 configurations (s=2) ---------
# (n, m, M_2, V_2, delta_2, delta_1) transcribed from the p.207 image.
P207 = [(16,12,13,3,F(-1),F(1,4)), (21,14,16,2,F(-1,2),F(7,6)),
        (21,14,18,5,F(-1),F(1,3)), (15,10,11,3,F(-1),F(1,2)),
        (15,10,11,2,F(-1),F(4,3))]
print("== Moh p.207 Appendix II table (s=2, Prop 5.5 bottom (12)/(13)) ==")
for (n,m,M2,V2,d2,d1) in P207:
    d_2 = gcd(n,m); ns, ms = n//d_2, m//d_2
    def bot(L):
        A1 = (L*d1).denominator
        c12 = (ns*V2 % A1 == 0) and ((ms*V2-1) % A1 == 0)
        c13 = (ms*V2 % A1 == 0) and ((ns*V2-1) % A1 == 0)
        return A1, c12, c13
    Ac, c12c, c13c = bot(d2.denominator)          # Moh (8): L = den(delta_2)
    Az, z12, z13   = bot(1)                        # actual, C_2 = 0
    An, n12, n13   = bot(d2.denominator)           # actual, C_2 != 0
    ok = (z12 or z13) or (n12 or n13)
    print(f"  n={n:3d} m={m:3d} M2={M2:3d} V2={V2} d2={d2} d1={d1}  n*={ns} m*={ms}"
          f" | coarse A1={Ac} (12)={c12c} (13)={c13c}"
          f" | actual C2=0: A1={Az} ok={z12 or z13}; C2!=0: A1={An} ok={n12 or n13}"
          f" | ROW SURVIVES ACTUAL = {ok}")

# ---- sandwich / negative control ------------------------------------------
class Tree1(Tree):
    """Deliberately UNSOUND over-strong rule: centre_L stays 1 always."""
    def _node(self, j, high, danger, need, cL):
        return Tree._node(self, j, high, danger, need, 1)
print()
print("== sandwich control:  L==1-always  <=  ACTUAL  <=  COARSE ==")
rows = []
for n in range(16, 201):
    for (m, Ms, V) in B.census(n, Kmin=2, full=True):
        rows.append((n, m, Ms, V))
c1 = sum(1 for (n,m,Ms,V) in rows if Tree1(n,m,Ms,True).run(V) is not None)
print(f"  L==1-always: {c1}   ACTUAL: 90   COARSE: 1420   (monotone: {c1<=90<=1420})")

# ---- where the sharpening bites -------------------------------------------
print()
print("== attribution: does the surviving ACTUAL embedding use a zero factor? ==")
def path(T, V):
    r = T.run(V); out = []
    while isinstance(r, dict) and "j" in r:
        out.append((r["j"], r["A"], r["cL"], r["mode"])); r = r.get("child")
    return out, r
zero_used = 0; cl_lt = 0; keep = []
for (n,m,Ms,V) in rows:
    if not op_actual(n,m,Ms,V): continue
    p, bot_ = path(Tree(n,m,Ms,True), V)
    keep.append((n,m,tuple(Ms),tuple(V[i] for i in range(2,len(Ms)+2))))
    if any(mode=="zero" for (_,_,_,mode) in p): zero_used += 1
    # coarse modulus at the same levels
    Tc = Tree(n,m,Ms,False); pc,_ = path(Tc, V)
    if pc and p and any(a1!=a2 for (_,a1,_,_),(_,a2,_,_) in zip(p,pc)): cl_lt += 1
print(f"  of the 90 survivors: {zero_used} use a zero selected factor on the kept path;"
      f" {cl_lt} have an ACTUAL modulus differing from coarse on the kept path")
print(f"  survivors n<=100: {sorted(set((r[0],r[1]) for r in keep if r[0]<=100))}")
json.dump([[r[0],r[1],list(r[2]),list(r[3])] for r in keep],
          open("/home/ubuntu/jc2/box/actual-stabilizer-soundness-20260906/actual90.json","w"))
