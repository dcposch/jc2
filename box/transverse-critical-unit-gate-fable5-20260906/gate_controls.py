#!/usr/bin/env python3
"""Fable gate controls: literal identity over symbolic base + nilpotent, essential-row mutations,
toy block-det with G-dependent off-diagonals, D108 sign formula."""
import resource, json, itertools
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2); resource.setrlimit(resource.RLIMIT_CPU,(30,30))
import sympy as S
X,W,Z,l,m,eps=S.symbols('X W Z l m eps')
out={}
def jac(F,G): return S.expand(S.diff(F,X)*S.diff(G,W)-S.diff(F,W)*S.diff(G,X))
def coeffs(P):
    P=S.Poly(S.expand(P),X,W); return {mon:c for mon,c in zip(P.monoms(),P.coeffs())}
# (1) fully symbolic F (deg_X 4, deg_W 3) and G = X^2+lX+m + W*g1 + W^2*g2 + W^3*g3, all coefficients symbols
g=[[S.Symbol(f'g{i}_{j}') for i in range(4)] for j in range(1,4)]
f=[[S.Symbol(f'f{i}_{j}') for i in range(5)] for j in range(4)]
G=X**2+l*X+m+sum(W**(j+1)*sum(g[j][i]*X**i for i in range(4)) for j in range(3))
F=sum(W**j*sum(f[j][i]*X**i for i in range(5)) for j in range(4))
s=-l/2
def at(p): return S.expand(p.subs({X:s,W:0},simultaneous=True))
Delta=at(S.diff(G,W)); J=jac(F,G); cj=coeffs(J)
J00=cj.get((0,0),0); tail=sum(s**i*cj.get((i,0),0) for i in range(1,max(k[0] for k in cj)+1))
lhs=S.expand(1-Z*at(S.diff(F,X))*Delta); rhs=S.expand(-(Z*J00-1)-Z*tail)
out['1_identity_symbolic_base']= (S.expand(lhs-rhs)==0)
out['1_GX_at_s_zero']=(at(S.diff(G,X))==0)
out['1_identity_uses_only_W0_rows_and_inverse']=True  # by construction: rhs built from J_i0, i>=1, and Z*J00-1 only
# nilpotent base: substitute every f,g coefficient by (rational + eps*rational) and reduce mod eps^2
subs={}
import random; random.seed(7)
for row in f+g:
    for sym in row: subs[sym]=S.Rational(random.randint(-5,5))+eps*S.Rational(random.randint(-5,5))
subs[l]=S.Rational(3)+eps*2; subs[m]=S.Rational(-1)+eps*5
def modeps2(p): return S.expand(S.rem(S.expand(p),eps**2,eps)) if p!=0 else 0
d=S.expand((lhs-rhs).subs(subs)); out['1_identity_nilpotent_base']= (modeps2(d)==0)
# also check the inverse: (Z*F_X(s,0)) * Delta == 1 mod (Zj00-1, tail rows) in nilpotent example: 1 - Z FX Delta reduces to rhs which is in ideal
out['1_inverse_is_Z_FX']= S.expand((lhs-rhs).subs(subs))==0
# (1b) essential-row mutations
# drop inverse relation: F=G, G=X^2+W^2: all J_ij=0, Delta=0 -> Delta not a unit without Z*J00-1
G1=X**2+W**2; out['1b_drop_inverse_F=G_allrows0_Delta']=(jac(G1,G1)==0, S.expand(S.diff(G1,W).subs({X:0,W:0}))==0)
# drop one W=0 positive row: F=X, G=X^2+2X+(X+1)W: J=X+1, J00=1 unit, J10=1, Delta=G_W(-1,0)=0
G2=X**2+2*X+(X+1)*W; J2=jac(X,G2); c2=coeffs(J2)
out['1b_drop_row_J10_only']={'J':str(J2),'J00':str(c2.get((0,0))),'J10':str(c2.get((1,0))),'others_zero':all(v==0 for k,v in c2.items() if k not in[(0,0),(1,0)]),'Delta':str(S.diff(G2,W).subs({X:-1,W:0}))}
# l=0 case: no positive row needed at all
out['1c_l0_needs_no_positive_row']=(S.expand((1-Z*at(S.diff(F,X))*Delta-(-(Z*J00-1))).subs(l,0))==S.expand((-Z*tail).subs(l,0)))
# (2) evaluation annihilates V0 and gives beta*Delta, for symbolic G
beta,gamma=S.symbols('beta gamma'); v=[[S.Symbol(f'v{i}_{j}') for i in range(4)] for j in range(1,3)]
C=beta*X+gamma+sum(W**(j+1)*sum(v[j][i]*X**i for i in range(4)) for j in range(2))
C0=C.subs({beta:0,gamma:0})
out['2_eval_V0_zero']=(at(jac(C0,G))==0); out['2_eval_beta_Delta']=(S.expand(at(jac(C,G))-beta*Delta)==0)
# toy block-determinant: V0 basis = monomials X^i W^r, r=1,2, i=0..3 (8 columns), pivot rows (i+1,r-1)
cols=[(i,r) for r in (1,2) for i in (3,2,1,0)]  # r ascending, i descending
rows=[(i+1,r-1) for (i,r) in cols]
Mtoy=S.zeros(8,8)
for a,(i,r) in enumerate(cols):
    cP=coeffs(jac(X**i*W**r,G))
    for b,(ii,rr) in enumerate(rows): Mtoy[b,a]=cP.get((ii,rr),0)
diag=[Mtoy[k,k] for k in range(8)]; upper_zero=all(Mtoy[b,a]==0 for a in range(8) for b in range(a))
lower_entries=[Mtoy[b,a] for a in range(8) for b in range(a+1,8)]
nonconst_lower=[e for e in lower_entries if e!=0 and not e.is_number]
out['2_toy_M']={'diag':[str(x) for x in diag],'upper_zero':upper_zero,'n_nonconst_offdiag':len(nonconst_lower),'sample_offdiag':[str(e) for e in nonconst_lower[:3]],'det':str(S.factor(Mtoy.det()))}
# append beta column (X + W-part with symbols) and the evaluation row
Cbeta=X+sum(W**(j+1)*sum(v[j][i]*X**i for i in range(4)) for j in range(2))
Big=S.zeros(9,9)
for a,(i,r) in enumerate(cols):
    cP=coeffs(jac(X**i*W**r,G))
    for b,(ii,rr) in enumerate(rows): Big[b,a]=cP.get((ii,rr),0)
    Big[8,a]=at(jac(X**i*W**r,G))
cB=coeffs(jac(Cbeta,G))
for b,(ii,rr) in enumerate(rows): Big[b,8]=cB.get((ii,rr),0)
Big[8,8]=at(jac(Cbeta,G))
out['2_block_det_eq_detM_Delta']=(S.expand(Big.det()-Mtoy.det()*Delta)==0)
out['2_eval_row_on_V0_zero']=all(Big[8,a]==0 for a in range(8))
out['2_v_block_nonconst']=any((Big[b,8]!=0 and not Big[b,8].is_number) for b in range(8))
# mutation: nonquadratic restriction (add X^3 to G): 0-block fails
G3=G+X**3
out['2_mut_cubic_restriction_zero_block_fails']=any(at(jac(X**i*W**r,G3))!=0 for (i,r) in cols)
# mutation: non-monic restriction 2X^2: diagonal changes to -4r (still constant), det still constant*Delta? check
G4=G+X**2
M4=S.zeros(8,8)
for a,(i,r) in enumerate(cols):
    cP=coeffs(jac(X**i*W**r,G4))
    for b,(ii,rr) in enumerate(rows): M4[b,a]=cP.get((ii,rr),0)
out['2_mut_nonmonic_diag']=[str(M4[k,k]) for k in range(8)]
# (3) graph reconstruction: beta = j*u - F0_X(s,0) holds in B[u]/(u Delta -1) with j=J00, given W=0 rows
u,j=S.symbols('u j'); F0=F  # F0 generic; full F = F0 + C
Ffull=F0+C; Jf=jac(Ffull,G); cf=coeffs(Jf); J00f=cf.get((0,0),0); tailf=sum(s**i*cf.get((i,0),0) for i in range(1,max(k[0] for k in cf)+1))
# J(s,0) = (F0_X(s,0)+beta)*Delta  exactly
out['3_eval_identity']=(S.expand(J00f+tailf-(at(S.diff(F0,X))+beta)*Delta)==0)
# beta - (j*u - F0X) = u*(beta+F0X)*Delta - u*j - ... : show beta-(J00f*u-F0X) = (beta+F0X)*(1-u*Delta) - u*tailf  (ideal identity)
expr=S.expand((beta-(J00f*u-at(S.diff(F0,X)))) - ((beta+at(S.diff(F0,X)))*(1-u*Delta) + u*tailf))
out['3_graph_identity_in_ideal']=(expr==0)
out['3_J00_depends_on_beta']=(S.diff(J00f,beta)!=0)
out['3_J00_beta_coefficient']=str(S.diff(J00f,beta))
# (4) D108 formula
c,b,d1,d0=S.symbols('c b d1 d0'); hw=[S.Symbol(f'hw{i}') for i in range(3)]; dw=[S.Symbol(f'dw{i}') for i in range(3)]
h=-X+c+W*sum(hw[i]*X**i for i in range(3)); D=d1*X+d0+W*sum(dw[i]*X**i for i in range(3))
Gd=h**2-b*h/3+D; GdX0=S.Poly(S.expand(Gd.subs(W,0)),X)
out['4_restriction']=str(GdX0.as_expr()); ld=GdX0.coeff_monomial(X); sd=-ld/2
out['4_s']=(S.expand(sd-(c-b/6-d1/2))==0)
Dd=S.expand(S.diff(Gd,W).subs({X:sd,W:0},simultaneous=True))
out['4_Delta_formula']=(S.expand(Dd-(d1*S.diff(h,W).subs({X:sd,W:0})+S.diff(D,W).subs({X:sd,W:0})))==0)
out['4_Delta_eq_minus_J(h,D)']=(S.expand(Dd-(-jac(h,D).subs({X:sd,W:0},simultaneous=True)))==0)
# general: Delta = J(h,D)(s,0)/h_X(s,0); (99,66) sign h=+X+c gives +J(h,D)
hp=X+c+W*sum(hw[i]*X**i for i in range(3)); Gp=hp**2-b*hp/3+D; lp=S.Poly(S.expand(Gp.subs(W,0)),X).coeff_monomial(X); sp=-lp/2
Dp=S.expand(S.diff(Gp,W).subs({X:sp,W:0},simultaneous=True))
out['4_9966_sign_Delta_eq_plus_J(h,D)']=(S.expand(Dp-jac(hp,D).subs({X:sp,W:0},simultaneous=True))==0)
out['4_flip_sign_mutation_detected']=(S.expand(Dd-(jac(h,D).subs({X:sd,W:0},simultaneous=True)))!=0)
print(json.dumps(out,indent=1,sort_keys=True,default=str))
