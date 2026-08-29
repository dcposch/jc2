# `R30-SLICE-DESC` — provisional branch-P class prefix through row 34

Date: 2026-08-27  
Lane: Sol Ultra, exact desk algebra  
Status: **PROVISIONAL DESCENDANT; BUILT WITH ROW-30 ROLLBACK; PARENT REVIEW
LANDED CONFIRMED BEFORE FINAL FREEZE; DESCENDANT UNREVIEWED**

No raw determinant row, polynomial-`G` lift, endpoint decision, family
exclusion, landing claim, or JC2 theorem is made.

## 0. Dependency, rollback, and verdict

This report is a deliberately provisional descendant of the exact bytes

```text
e487bd6f54be9762dd551abe7bd25cabed4b9daa053b57a9a424441ef269848e
  xmodel/ggv-quarter-root-r28-nonlinear-class-test-r0-sol-ultra-20260827.md
```

Its only construction-time unreviewed load-bearing input was the parent's
claim that the slice

```text
A=X^4-1,
F_1=F_3=F_5=F_7=0,
F_2=4u A^2A',
F_4=2u^2(A')^2,
F_6=v
```

passes class rows 23--29 and that class row 30 has residue ideal

```text
I_30=(uv,u^4) subset Q[u,v].                            (0.1)
```

The independent Grok46 review requested in
`ggv-quarter-root-r30-symbolic-prefix-crossreview-grok46-prompt.md` was
pending throughout the derivation, so the computation was performed with
the following **rollback rule:** if that review did not confirm the
licensed-prefix statement and (0.1), or repaired either the row-30 gauge or
ideal, then every prefix-scheme intersection and every row-34 survival
statement below would be quarantined and recomputed from the repaired
parent.  The standalone coefficient identities for `q_9,...,q_12` under the
displayed assignment would remain desk calculations, but could not be
called descendants of a licensed prefix.

The review landed before this final freeze at exact hash

```text
ccf1d9778a50351c5ee0a8b919b7e917e1baa036e73062c7a64c45bedf9ba490
  xmodel/ggv-quarter-root-r30-symbolic-prefix-crossreview-grok46-20260827.md
```

and classified the licensed slice, row-30 gauge, residue vector, and ideal
`(uv,u^4)` **CONFIRMED**, with no relevant repair.  The rollback trigger
therefore did not fire.  This later review result was used only to discharge
the parent dependency; none of the row-31--34 derivation below was taken
from it.  This descendant remains new and independently unreviewed.

Conditional on (0.1), the exact answer is:

```text
row 31: split-surjective F_9 class map; no new (u,v)-equation;
row 32: residue ideal (u^2 v,u^5), already contained in I_30;
row 33: split-surjective F_11 class map; no new (u,v)-equation;
row 34: residue ideal (v^2,u^3v,u^6), adding exactly v^2 modulo I_30.
```

Thus no smaller projected base occurs at rows 31--33.  Row 34 detects the
surviving `v` direction **quadratically**.  It kills the reduced `v`-axis,
but it does not set `v` equal to zero scheme-theoretically:

```text
Q[u,v]/(uv,u^4)              before row 34,
Q[u,v]/(uv,u^4,v^2)          through row 34.            (0.2)
```

The latter is a length-five local algebra with basis
`1,u,u^2,u^3,v`.  In particular `v` remains a nonzero square-zero tangent
direction.  Saying merely "row 34 gives u=v=0" would discard the main
scheme-theoretic information.

## 1. Reviewed inputs and source hashes

The following exact files were used.  The first was the unreviewed parent
snapshot during the derivation; the second is the subsequently landed
different-model confirmation.  The rest supply reviewed normalization,
receiver ranks, or the literal frozen source windows.

```text
e487bd6f54be9762dd551abe7bd25cabed4b9daa053b57a9a424441ef269848e
  xmodel/ggv-quarter-root-r28-nonlinear-class-test-r0-sol-ultra-20260827.md
ccf1d9778a50351c5ee0a8b919b7e917e1baa036e73062c7a64c45bedf9ba490
  xmodel/ggv-quarter-root-r30-symbolic-prefix-crossreview-grok46-20260827.md
6fac1961e85730b2909ce05ecbdee19c2b5b1f61831844cd409d97e88b4bff29
  xmodel/ggv-quarter-root-r30-symbolic-prefix-crossreview-grok46-prompt.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
60670d0a7066ab0a1d1f72ad05a0ff44a858fa39dbf4d18fd225913d26b6d114
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md
5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55
  xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
```

The landed review is consumed only for the parent-dependency verdict, not
for any descendant formula.

## 2. Frozen newest slots and receiver firewall

Write `B=A'=4X^3`.  Adjoin exactly the source slots licensed by the frozen
window, and no others:

```text
P_8 =F_8 =sum_(a=0)^8 a_a X^a,
P_9 =F_9 =sum_(a=1)^7 b_a X^a,
P_10=F_10=sum_(a=1)^6 c_a X^a,
P_11=F_11=sum_(a=1)^5 d_a X^a,
P_12=F_12=sum_(a=2)^4 e_a X^a.                         (2.1)
```

The dimensions are respectively `9,7,6,5,3`.  In the reviewed licensed
new-slot table the five maps at rows 30--34 have ranks

```text
row m       30       31       32       33       34
new slot    P_8      P_9      P_10     P_11     P_12
rank         0        3        0        3        0
receiver     4        3        4        3        4.     (2.2)
```

The zero and nonzero maps in (2.2) must not be conflated.  On the even rows
the correctly gauged linear representatives are ordinary polynomial
differentials

```text
row 30: (A   P_8/4)dX,
row 32: (A^2 P_10/4)dX,
row 34: (A^3 P_12/4)dX,                                (2.3)
```

so their classes vanish for every licensed slot value.  On rows 31 and 33,
the odd-slot maps are full onto their three-dimensional receivers.  They
impose three equations on the new slot, rather than vanishing.

This is solely a statement about class receivers.  Rank zero in (2.2) does
not say that a raw `D_m` row omits that coefficient, and rank three does not
construct a polynomial `G`.

## 3. Correct gauges for rows 31--34

The physical coefficient formula is

```text
q_n=sum_(d>=1) c_(n,d) p^(n+2-8d) S_(n,d),
c_(n,d)=2/(n+2) binom((n+2)/8,d),                       (3.1)
```

where `S_(n,d)` is the ordered-composition sum in the parent.  Put
`m=n+22`, `H=A^2`, and choose a branch-P component `p^2=epsilon A`,
`epsilon in {+1,-1}`.

For the odd rows, gauge to the least-character receiver:

```text
row 31: H^7 p^-31 q_9  =p^-3 q_9  in V_3,
row 33: H^8 p^-33 q_11 =p^-1 q_11 in V_1.              (3.2)
```

Here

```text
nabla_j=d+(j/2)(B/A)dX,       j=1,3.                   (3.3)
```

For the even rows, multiplication by `A^(m/2)` gives an ordinary rational
differential.  The component-independent representatives are

```text
row 32: A^16 p^-32 q_10=q_10,
row 34: A^17 p^-34 q_12=epsilon q_12.                  (3.4)
```

Every `epsilon` cancels after replacing the even powers of `p`.  Equations
(3.2) and (3.4), rather than a shifted operator with a dropped `H`-power,
are the gauges used below.

## 4. Row 31: exact `q_9` and its nonzero linear receiver

All nonlinear ordered compositions of `9` contain one of the already-zero
odd slots `F_1,F_3,F_5,F_7`.  Hence

```text
q_9=(1/4)p^3P_9,
p^-3q_9=P_9/4,
R_9=0.                                                  (4.1)
```

In `V_3`, take the basis represented by
`X dX,X^2 dX,X^4 dX`.  Direct `nabla_3` identities give

```text
[X^5 dX]=(1/6)[X dX],
[X^6 dX]=(3/13)[X^2 dX],
[X^3 dX]=[X^7 dX]=0.                                  (4.2)
```

The three row-31 equations are therefore

```text
6b_1+b_5=0,
13b_2+3b_6=0,
b_4=0.                                                  (4.3)
```

They have constant unit pivots over `Q`; the map remains split-surjective
after base change to the nonreduced ring (0.1).  Thus row 31 leaves four
free new-slot coordinates, which may be taken as
`b_1,b_2,b_3,b_7`, and its contraction to `Q[u,v]` adds nothing.

## 5. Row 32: exact `q_10`, class, and redundant residue ideal

Only the following composition sums survive:

```text
S_(10,2)=2F_2P_8+2F_4F_6,
S_(10,3)=3F_2^2F_6+3F_2F_4^2,
S_(10,4)=4F_2^3F_4,
S_(10,5)=F_2^5.                                        (5.1)
```

The correctly gauged full coefficient is

```text
qbar_10=q_10
 = A^2P_10/4
   +(1/16) A^-2 S_(10,2)
   -(1/96) A^-6 S_(10,3)
   +(1/256)A^-10S_(10,4)
   -(1/512)A^-14S_(10,5).                              (5.2)
```

After the exact substitution from Section 0,

```text
qbar_10
 = A^2P_10/4 +(u/2)BP_8
   -(u^2v/4) B^2/A^2
   -(u^5/2) B^5/A^4.                                   (5.3)
```

Thus, relative to the newest linear slot, the full gauged nonlinear
remainder is

```text
R_10=(u/2)BP_8-(u^2v/4)B^2/A^2-(u^5/2)B^5/A^4.
```

The first two terms in (5.3) are polynomial differentials and hence
ordinary exact.  Thus the reduced **class representative**, not the raw
coefficient, is

```text
[qbar_10 dX]
 =[-(u^2v/4) B^2/A^2 dX-(u^5/2)B^5/A^4 dX].           (5.4)
```

For a root `alpha` of `A=X^4-1`,

```text
Res_alpha(B^2/A^2 dX)=3alpha^3,
Res_alpha(B^5/A^4 dX)=256,                             (5.5)
```

and the second differential has infinity residue `-1024`.  In the order
`1,-1,i,-i,infinity`, (5.4) has residue vector

```text
(-3u^2v/4-128u^5,
  3u^2v/4-128u^5,
  3i u^2v/4-128u^5,
 -3i u^2v/4-128u^5;
 512u^5).                                               (5.6)
```

Its common residue ideal is

```text
J_32=(u^2v,u^5) subset (uv,u^4)=I_30.                  (5.7)
```

Consequently row 32 makes no further scheme-theoretic cut after row 30.
Notice that this is stronger than substituting the reduced equation `u=0`:
both terms in (5.4) vanish already in the full nonreduced quotient by
`(uv,u^4)`.

## 6. Row 33: exact `q_11` and affine newest-slot cancellation

The only nonlinear surviving composition is
`S_(11,2)=2F_2P_9`.  From `c_(11,2)=5/64`, (3.2) gives

```text
q_11=(1/4)p^5P_11+(5/32)p^-3F_2P_9,
p^-1q_11=A^2P_11/4+(5u/8)BP_9.                         (6.1)
```

Thus the gauged nonlinear remainder is `(5u/8)BP_9`; it is not silently
discarded merely because it is polynomial.  Polynomial coefficients in the
odd `V_1` receiver need not be `nabla_1`-exact.

In the same notation as the adjacent rows,
`R_11=(5u/8)BP_9` in the fixed `V_1` gauge.

Choose receiver coordinates in which

```text
[A^2P_11 dX] -> (d_1+d_5/8, d_2, d_4),
[BP_9 dX]    -> ((8b_2+4b_6)/5,
                  (13b_3+7b_7)/5,
                  11b_1+5b_5).                        (6.2)
```

The three row-33 equations, with denominators cleared, are

```text
8d_1+d_5+32u b_2+16u b_6=0,
2d_2+u(13b_3+7b_7)=0,
2d_4+5u(11b_1+5b_5)=0.                                (6.3)
```

After (4.3), they solve without localizing at `u`:

```text
d_1=-d_5/8+(14/3)u b_2,
d_2=-(u/2)(13b_3+7b_7),
d_4=(95/2)u b_1.                                       (6.4)
```

The allowed coordinates `d_3,d_5` remain free.  The pivots in (6.3) are
rational units, so this is a split affine cancellation over the entire
nonreduced row-30 base, not a generic-point solve.  Row 33 therefore adds no
equation to `Q[u,v]`.

## 7. Row 34: exact `q_12` and the quadratic `v` obstruction

The surviving ordered-composition sums are

```text
S_(12,2)=2F_2P_10+2F_4P_8+F_6^2,
S_(12,3)=3F_2^2P_8+6F_2F_4F_6+F_4^3,
S_(12,4)=4F_2^3F_6+6F_2^2F_4^2,
S_(12,5)=5F_2^4F_4,
S_(12,6)=F_2^6.                                        (7.1)
```

The component-independent ordinary coefficient is

```text
qbar_12=epsilon q_12
 = A^3P_12/4
   +(3/32) A^-1 S_(12,2)
   -(1/128)A^-5 S_(12,3)
   +(5/2048)A^-9 S_(12,4)
   -(9/8192)A^-13S_(12,5)
   +(39/65536)A^-17S_(12,6).                           (7.2)
```

Exact substitution and collection give

```text
qbar_12
 = A^3P_12/4 +(3/4)uABP_10
   +(3/32)v^2/A
   +(1/4)u^3v B^3/A^3
   +(1/2)u^6 B^6/A^5.                                  (7.3)
```

Accordingly the full gauged nonlinear remainder relative to `P_12` is the
last four terms of (7.3); its class-reduced remainder is (7.4).

Two cancellations in (7.3) are load-bearing:

* the `P_8` terms are `+(3/8)u^2B^2P_8/A` and
  `-(3/8)u^2B^2P_8/A`, so they cancel identically;
* the `P_10` term and the newest `P_12` term are polynomial ordinary
  differentials, so they are exact and cannot alter any residue.

The odd slots do not occur in weight 12 because all earlier odd slots are
zero and no two of `P_9,P_11` can have total weight 12.  Hence none of the
licensed slots `P_8,...,P_12` can cancel the remaining even-row class.

The reduced class is

```text
[qbar_12 dX]
 =[(3/32)v^2/A
   +(1/4)u^3v B^3/A^3
   +(1/2)u^6 B^6/A^5]dX.                               (7.4)
```

At a fourth root of unity `alpha`, the needed exact residues are

```text
Res_alpha(dX/A)         =alpha/4,
Res_alpha(B^3/A^3 dX)  =6alpha^2,
Res_alpha(B^6/A^5 dX)  =(1155/2)alpha^3.               (7.5)
```

All three infinity residues vanish.  Thus the complete row-34 vector is

```text
( 3v^2/128 +(3/2)u^3v +(1155/4)u^6,
 -3v^2/128 +(3/2)u^3v -(1155/4)u^6,
  3i v^2/128-(3/2)u^3v -(1155i/4)u^6,
 -3i v^2/128-(3/2)u^3v +(1155i/4)u^6;
  0).                                                   (7.6)
```

Its residue ideal is exactly

```text
J_34=(v^2,u^3v,u^6).                                   (7.7)
```

Modulo the full parent ideal, `u^3v=u^2(uv)` and
`u^6=u^2(u^4)` already vanish.  The only new equation is therefore `v^2`:

```text
I_30+J_32+J_34=(uv,u^4,v^2).                           (7.8)
```

## 8. Full coefficient-ring description

Let `S` be the polynomial ring over `Q` in `u,v` and all coefficients in
(2.1).  Through class row 34 the provisional descendant is defined by

```text
I_30=(uv,u^4),
I_31=(6b_1+b_5, 13b_2+3b_6, b_4),
I_32=(u^2v,u^5),
I_33=(8d_1+d_5+32ub_2+16ub_6,
      2d_2+u(13b_3+7b_7),
      2d_4+5u(11b_1+5b_5)),
I_34=(v^2,u^3v,u^6).                                   (8.1)
```

Using the unit pivots in `I_31` and `I_33`, and the containments in
Sections 5 and 7, its coordinate ring is explicitly

```text
Q[a_0,...,a_8,
  b_1,b_2,b_3,b_7,
  c_1,...,c_6,
  d_3,d_5,
  e_2,e_3,e_4,
  u,v] /(uv,u^4,v^2).                                  (8.2)
```

There are 24 free newest-slot coordinates.  Formula (8.2) is an actual
scheme isomorphism, not just a dimension count at a generic point.

Before row 34, the reduced base is the `v`-axis because
`rad(uv,u^4)=(u)`.  After row 34,

```text
rad(uv,u^4,v^2)=(u,v),
m=(u,v),   m^2=(u^2),   m^3=(u^3),   m^4=0,
socle=<u^3,v>.                                          (8.3)
```

So row 34 removes every geometric point with `v != 0`, yet the Zariski
tangent space still has the two directions represented by `u` and `v`.
The `v` direction is detected at order two, not killed at order one.

## 9. Exact replay

The complete replay below uses only `fractions.Fraction` and small exact
Gaussian elimination.  It performs no Groebner computation and reads no
hidden input.

```bash
python3 - <<'PY'
from fractions import Fraction as Q
from math import comb, factorial

def binom(a,d):
    z=Q(1)
    for j in range(d): z*=a-j
    return z/factorial(d)
def c(n,d): return Q(2,n+2)*binom(Q(n+2,8),d)

assert [c(10,d) for d in range(1,6)] == \
       [Q(1,4),Q(1,16),-Q(1,96),Q(1,256),-Q(1,512)]
assert [c(12,d) for d in range(1,7)] == \
       [Q(1,4),Q(3,32),-Q(1,128),Q(5,2048),
        -Q(9,8192),Q(39,65536)]
assert c(11,2)==Q(5,64)

# Collected q10 coefficients: u*B*P8, u^2*v*B^2/A^2,
# and u^5*B^5/A^4.
q10_uP8=c(10,2)*2*4
q10_u2v=c(10,2)*2*2+c(10,3)*3*4**2
q10_u5=(c(10,3)*3*4*2**2
        +c(10,4)*4*4**3*2+c(10,5)*4**5)
assert (q10_uP8,q10_u2v,q10_u5)==(Q(1,2),-Q(1,4),-Q(1,2))

# Collected q12 coefficients: u*A*B*P10, cancellation of P8,
# v^2/A, u^3*v*B^3/A^3, and u^6*B^6/A^5.
q12_uP10=c(12,2)*2*4
q12_P8=c(12,2)*2*2+c(12,3)*3*4**2
q12_v2=c(12,2)
q12_u3v=c(12,3)*6*4*2+c(12,4)*4*4**3
q12_u6=(c(12,3)*2**3
        +c(12,4)*6*4**2*2**2
        +c(12,5)*5*4**4*2+c(12,6)*4**6)
assert (q12_uP10,q12_P8,q12_v2,q12_u3v,q12_u6)== \
       (Q(3,4),Q(0),Q(3,32),Q(1,4),Q(1,2))

# At a root alpha, scale X=alpha*z.  The following returns the scalar
# at alpha=1 in Res((A')^k/A^ell dX); the alpha factor is alpha^(3k+1).
def conv(a,b,N):
    z=[Q(0)]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N: z[i+j]+=x*y
    return z
def inv_series(a,N):
    b=[Q(0)]*(N+1); b[0]=1/a[0]
    for n in range(1,N+1):
        b[n]=-sum(a[k]*b[n-k]
                  for k in range(1,min(n,len(a)-1)+1))/a[0]
    return b
def pow_series(a,e,N):
    z=[Q(1)]+[Q(0)]*N
    for _ in range(e): z=conv(z,a,N)
    return z
def root_residue_scalar(k,ell):
    N=ell-1
    num=[Q(4**k*comb(3*k,j)) for j in range(min(3*k,N)+1)]
    num += [Q(0)]*(N+1-len(num))
    hinv=inv_series([Q(4),Q(6),Q(4),Q(1)],N)
    return conv(num,pow_series(hinv,ell,N),N)[N]

assert root_residue_scalar(2,2)==3
assert root_residue_scalar(5,4)==256
assert root_residue_scalar(0,1)==Q(1,4)
assert root_residue_scalar(3,3)==6
assert root_residue_scalar(6,5)==Q(1155,2)

# Small exact common-denominator quotient replay for the two odd maps.
def rref(rows):
    a=[[Q(x) for x in row] for row in rows if any(row)]
    if not a: return []
    i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None: continue
        a[i],a[k]=a[k],a[i]
        z=a[i][j]; a[i]=[x/z for x in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                z=a[k][j]
                a[k]=[a[k][h]-z*a[i][h] for h in range(len(a[0]))]
        i+=1
        if i==len(a): break
    return [row for row in a if any(row)]
def nullspace(mat):
    a=[[Q(x) for x in row] for row in mat]
    m,n=len(a),len(a[0]); piv=[]; i=0
    for j in range(n):
        k=next((k for k in range(i,m) if a[k][j]),None)
        if k is None: continue
        a[i],a[k]=a[k],a[i]
        z=a[i][j]; a[i]=[x/z for x in a[i]]
        for k in range(m):
            if k!=i and a[k][j]:
                z=a[k][j]
                a[k]=[a[k][h]-z*a[i][h] for h in range(n)]
        piv.append(j); i+=1
        if i==m: break
    free=[j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        v=[Q(0)]*n; v[f]=1
        for row,p in enumerate(piv): v[p]=-a[row][f]
        out.append(v)
    return out
def Apow_monomial(deg,N,mx,scale=Q(1)):
    z=[Q(0)]*(mx+1)
    for k in range(N+1):
        z[deg+4*k]+=scale*comb(N,k)*(-1)**(N-k)
    return z
def quotient_rows(j,M,sources,D=70):
    # source=(X-degree, extra A-power, scalar), before clearing by A^(M+1)
    mx=max([D+3]+[a+4*(M+1+e) for a,e,s in sources])
    image=[]
    for d in range(D+1):
        z=[Q(0)]*(mx+1)
        z[d+3]=Q(d+2*j-4*M)
        if d: z[d-1]=-Q(d)
        image.append(z)
    src=[Apow_monomial(a,M+1+e,mx,s) for a,e,s in sources]
    left=nullspace([[col[r] for r in range(mx+1)] for col in image])
    equations=[[sum(l[r]*s[r] for r in range(mx+1)) for s in src]
               for l in left]
    return rref(equations)

row31=[[Q(1),0,0,0,Q(1,6),0,0],
       [0,Q(1),0,0,0,Q(3,13),0],
       [0,0,0,Q(1),0,0,0]]
row33=[[Q(1),0,0,0,Q(1,8),0,Q(8,5),0,0,0,Q(4,5),0],
       [0,Q(1),0,0,0,0,0,Q(13,5),0,0,0,Q(7,5)],
       [0,0,0,Q(1),0,Q(11),0,0,0,Q(5),0,0]]
for M in (4,6):
    assert quotient_rows(3,M,[(a,0,Q(1)) for a in range(1,8)])==row31
    sources=([(a,2,Q(1)) for a in range(1,6)]
             +[(a+3,0,Q(4)) for a in range(1,8)])
    assert quotient_rows(1,M,sources)==row33

# Monomial containment checks in the parent ideal.
assert (2>=1 and 1>=1)       # u^2*v is divisible by u*v
assert 5>=4                  # u^5 is divisible by u^4
assert (3>=1 and 1>=1)       # u^3*v is divisible by u*v
assert 6>=4                  # u^6 is divisible by u^4

print('q10 reduced class = -u^2*v*B^2/(4A^2)-u^5*B^5/(2A^4)')
print('row32 residue ideal = (u^2*v,u^5) subset (u*v,u^4)')
print('row31 rank = 3; row33 rank = 3 (stable at M=4,6)')
print('q12 reduced class = 3v^2/(32A)+u^3*v*B^3/(4A^3)+u^6*B^6/(2A^5)')
print('row34 residue ideal = (v^2,u^3*v,u^6)')
print('final base ideal = (u*v,u^4,v^2); basis = 1,u,u^2,u^3,v')
print('PASS')
PY
```

Exact output:

```text
q10 reduced class = -u^2*v*B^2/(4A^2)-u^5*B^5/(2A^4)
row32 residue ideal = (u^2*v,u^5) subset (u*v,u^4)
row31 rank = 3; row33 rank = 3 (stable at M=4,6)
q12 reduced class = 3v^2/(32A)+u^3*v*B^3/(4A^3)+u^6*B^6/(2A^5)
row34 residue ideal = (v^2,u^3*v,u^6)
final base ideal = (u*v,u^4,v^2); basis = 1,u,u^2,u^3,v
PASS
```

## 10. Claim ledger and strict class/raw firewalls

**Conditional exact conclusions:**

1. On the exact parent ideal (0.1), now independently confirmed as recorded
   in Section 0, the licensed frozen-slot class prefix extends through row
   34 with coordinate ring (8.2).
2. Rows 31 and 33 have genuinely nonzero, split-surjective linear receiver
   maps.  They constrain `P_9` and solve for three coordinates of `P_11`;
   they are not zero rows.
3. Rows 30, 32, and 34 have zero newest-slot class maps in the licensed
   gauges.  This does not make their nonlinear carry zero.
4. Row 32 adds no equation modulo the full nonreduced ideal `I_30`.
5. Row 34 adds exactly `v^2`; it kills the reduced `v`-axis but leaves `v`
   as a nonzero square-zero element.
6. No earlier projected `(u,v)` cut occurs at rows 31--33.  The odd rows do
   make honest linear cuts inside their newly adjoined slot fibers.

**Not claimed:**

* None of `I_30,...,I_34` is a raw determinant ideal.  They are ideals of
  de Rham class coordinates on one closed symbolic `F`-slice.
* A class equation is necessary for a polynomial determinant solution but
  is not asserted sufficient for a polynomial `G`, the frozen `G` window,
  or any raw equation `D_23,...,D_34`.
* The ordinary representatives `qbar_10,qbar_12` are not raw `D_32,D_34`.
  Removing polynomial exact terms is legal only after passing to the class
  quotient; those terms remain present in the raw coefficients (5.3) and
  (7.3).
* The split-surjectivity of the `P_9` and `P_11` class maps does not imply
  raw-row solvability or uniqueness of any `G` coefficient.
* The support collapse in (8.3) is only for this two-parameter slice.  It is
  not a generic theorem for the full branch-P prefix scheme and is not a
  branch-P family exclusion.
* The parent review has discharged the construction-time rollback condition,
  but every row-31--34 result in this descendant remains independently
  unreviewed and non-promotable from this file alone.
* No AWS resource was contacted.  No heavy local CAS ran.  No canonical
  file was edited; this report is the only write.  No path under `jc2-lean`
  was listed, searched, read, built, statused, or modified.

The maximum provisional conclusion is therefore:

```text
R31/R33: licensed odd-slot affine pivots, no base cut.
R32:     nonlinear class already zero modulo the full row-30 scheme.
R34:     first smaller base scheme; v is detected quadratically.
         Reduced v-axis dies, but the square-zero v tangent survives.
```
