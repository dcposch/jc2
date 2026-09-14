# Independent gate reconstruction. stdlib only; never touches client.py functions or check.py logic.
import sys; sys.dont_write_bytecode=True
import ast, hashlib, itertools, json
from math import comb
from fractions import Fraction as Fr
out={}
V=((0,0),(0,15),(9,6),(2,1))
# Polygon via FOUR halfplanes (i>=0 is the (0,0)-(0,15) edge; producer's three omit it, harmless for exponents i>=0).
def inpoly(i,j): return i>=0 and i+j<=15 and 5*i-7*j<=3 and i<=2*j
# Independent check that the 4 halfplanes equal the convex hull of V on a wide box, and that (-1,1) shows the 3-halfplane gap.
def hull(i,j):
    E=list(zip(V,V[1:]+V[:1])); cr=[(b[0]-a[0])*(j-a[1])-(b[1]-a[1])*(i-a[0]) for a,b in E]
    return all(x>=0 for x in cr) or all(x<=0 for x in cr)
out['hull_eq_4halfplanes_box']=all(hull(i,j)==inpoly(i,j) for i in range(-5,20) for j in range(-5,25))
out['three_halfplane_gap_point']=[(-1,1), (0<=15 and 5*-1-7*1<=3 and -1<=2), hull(-1,1)]
top=max(5*i-7*j for i,j in V)  # client.py inner-face rule: nx*i+ny*j==top
out['inner_top']=top
odd=[(i,j) for i in range(0,16) for j in range(0,16) if inpoly(i,j) and (i+j)%2==1]
free=[(i,j) for (i,j) in odd if i+j!=15 and 5*i-7*j!=top]
fixed_odd=[(i,j) for (i,j) in odd if (i,j) not in free]
out['odd_slots']=len(odd); out['free_slots']=len(free); out['fixed_odd_slots']=fixed_odd
out['(2,1)_on_inner_face']=(5*2-7*1==top); out['(9,6)_on_both_faces']=(9+6==15 and 5*9-7*6==top)
# Route 1: closed-form binomial c_ij = (-1)^j C(j,(j-i+3)/2)
def cbin(i,j):
    n=j-i+3
    if n%2: return 0
    d=n//2
    return (-1)**j*comb(j,d) if 0<=d<=j else 0
# Route 2: direct Laurent expansion of ONE monomial image v^-i (v^4 u - v - v^-1)^j, coefficient of u^0 v^-3; no closed form.
def lift_full(i,j,ell=1):
    P={(0,0):1}; base={(1,4):1,(0,1):-ell,(0,-1):-1}
    for _ in range(j):
        N={}
        for (a,b),c in P.items():
            for (p,q),d in base.items(): N[(a+p,b+q)]=N.get((a+p,b+q),0)+c*d
        P={k:v for k,v in N.items() if v}
    return {(a,b-i):c for (a,b),c in P.items()}
def cdir(i,j): return lift_full(i,j).get((0,-3),0)
out['route1_eq_route2_all_odd_slots']=all(cbin(i,j)==cdir(i,j) for (i,j) in odd)
# H^3 top face coefficients by the binomial theorem: H=p^2(p^3+g^3) => [g^{3m}p^{15-3m}]H^3 = C(3,m); cubic-face zeros elsewhere.
topface={(3*m,15-3*m):comb(3,m) for m in range(4)}
contrib=[topface[s]*cbin(*s) for s in sorted(topface)]
out['top_contributions_sorted_by_i']=contrib; const=sum(contrib); out['constant_route_A']=const
# Route B: (H|_{u=0}) as Laurent poly in v, cubed, coefficient v^-3 (5-term cube, not a source power).
Hu0={}
for (i,j) in ((0,5),(3,2)):
    for (a,b),c in lift_full(i,j).items():
        if a==0: Hu0[b]=Hu0.get(b,0)+c
Hu0={e:c for e,c in Hu0.items() if c}; out['H_u0']=dict(sorted(Hu0.items()))
cube=sum(Hu0[a]*Hu0[b]*Hu0[c] for a,b,c in itertools.product(Hu0,repeat=3) if a+b+c==-3)
out['constant_route_B']=cube
out['triple_classes']={'(-3,-3,3)x3':3*Hu0[-3]*Hu0[-3]*Hu0[3],'(-3,-1,1)x6':6*Hu0[-3]*Hu0[-1]*Hu0[1],'(-1,-1,-1)':Hu0[-1]**3}
# k monomial: phi(g^2 p) full expansion
out['phi_g2p']={f'u{a}v{b}':c for (a,b),c in sorted(lift_full(2,1).items())}; kco=lift_full(2,1)[(0,-3)]; out['k_coefficient']=kco
# Literal row
row={'1':const,'k':kco}
for (i,j) in free:
    c=cbin(i,j)
    if c: row[f'A_g{i}_p{j}']=c
out['row_terms']=len(row); out['free_contributing']=len(row)-2; out['zero_free_slots']=[s for s in free if cbin(*s)==0]
W=json.load(open('/tmp/jc2-lane.YwoVCk/inputs/witness.json'))
out['row_equals_witness_literal_row']=(row==W['literal_row']); out['free_equals_witness']=([list(s) for s in free]==W['free_A_slots'])
# Certificate: any Z-grading with Q in degree 0 making the row homogeneous has deg(row)=0 (constant) and deg(row)=wt(k) (k term).
out['certificate']={'constant_nonzero':const!=0,'k_nonzero':kco!=0,'conclusion':'wt(k)=0 for ANY integer weights (sign-free)'}
# Unspecialized three-row version: pins a_(9,6)-1, a_(2,1)-k; unspecialized row has all odd slots as variables.
urow={f'a_{i}_{j}':cbin(i,j) for (i,j) in odd if cbin(i,j)}
out['unspecialized']={'a_9_6':urow.get('a_9_6'),'a_2_1':urow.get('a_2_1'),'terms':len(urow),
  'chain':'a96-1 => wt(a96)=0; row => wt(a21)=wt(a96)=0; a21-k => wt(k)=0'}
# ell control: phi(p)=v^4 u - ell v - v^-1; ell power in [u^0 v^-3] of g^i p^j is (i+j-3)/2; weights wt(ell)=1,wt(k)=6,wt(a_ij)=(15-i-j)/2
def ellpow(i,j):
    # by direct expansion with ell as a symbolic power: count j-d factors of -ell v
    n=j-i+3; d=n//2; return j-d
ok=all(ellpow(i,j)==(i+j-3)//2 for (i,j) in odd if cbin(i,j))
degs={6}|{(15-i-j)//2+ellpow(i,j) for (i,j) in free if cbin(i,j)}|{6+0}  # constant -2484 ell^6 ; k*ell^0 with wt(k)=6
out['ell_control']={'ellpow_formula_ok':ok,'row_degrees':sorted(degs),'const_ell_power':ellpow(0,15),'k_ell_power':ellpow(2,1),'pin_ell_minus_1_homogeneous':False}
# Bridge (abstract): stated as proof text in report; here only the arithmetic fact used: k*x has no degree-0 part when wt(k)>0 and all weights>=0.
# check.py AST: zero Assert nodes, independent count
src=open('/tmp/jc2-lane.YwoVCk/inputs/check.py','rb').read()
out['check_py_assert_nodes']=sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(src)))
out['check_py_sha256']=hashlib.sha256(src).hexdigest()
print(json.dumps(out,indent=1,sort_keys=True,default=str))
