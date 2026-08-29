# `R28-CLASS` exact zero/control and the first honest branch-P pivot

Date: 2026-08-27  
Lane: Sol Ultra, exact desk algebra  
Status: **R28 DECIDED IDENTICALLY ZERO; R30 SYMBOLIC PREFIX TEST PASS (NEW,
AWAITING INDEPENDENT REVIEW)**

No JC2 theorem, endpoint decision, raw-`D28` decision, family exclusion, or
landing claim is made.

## 0. Verdict

The charged row-28 nonlinear remainder does not exist.  The reviewed all-row
formula gives, before imposing any prefix equations,

```text
q_6 = (2/8)[t^6]F^1 = F_6/4.
```

Hence

```text
R_6(F_1,...,F_5) = 0
```

as a polynomial identity over the full source ring.  After the licensed
row-28 `p`-power normalization and branch-P gauge, the ordinary differential
is `(F_6/4)dX`, so its residue vector at
`1,-1,i,-i,infinity` is exactly

```text
(0,0,0,0;0).
```

This is universal, not a zero observed at one point.  It corrects the earlier
`R28-CLASS` proposal in
`ideation-20260827T2259Z-carrier-hostile-review-sol-ultra.md`, whose proposed
nonlinear test omitted that `(n+2)/8=1` at `n=6`.  The correction was triggered
by the independent Opus5 `NU-LAW` proposal and its exact hostile review; that
review explicitly catches the zero binomial coefficient
`binom(1,2)=0` and confirms unconditional class-row death at
`m == 4 (mod 8)`.

There is no usable nontrivial numeric prefix through row 27, or through row
29, frozen in the allowed evidence:

* the named case is explicitly **before row 23** and every serialized system
  says `"D23_imposed": false`;
* its fixed value `F_1=H=A^2` is the reviewed `q1` negative control, hence it
  fails the first upper gate, row 23;
* the case directory contains no rational witness/result, and its terminal
  custody says the terminal runs returned no algebraic result; and
* the reviewed reports propose constructing a nonzero `F*`; they do not
  serialize one.  They do record the all-positive-slots-zero class point,
  but that origin makes every nonlinear remainder zero and is not a useful
  nonlinear discriminator.

I therefore did not invent a numeric point.  Following the charge's fallback,
I built the smallest useful symbolic slice of the licensed prefix coordinate
ring.  It passes rows 23--29 exactly over `Q[u,v]`.  On that slice the first
honest uncancellable candidate, row 30, has ordinary residue vector

```text
( uv/4 + (45/2)u^4,
  uv/4 - (45/2)u^4,
  uv/4 + (45/2)i u^4,
  uv/4 - (45/2)i u^4;
 -uv ).
```

It is nonzero in `Q(i)[u,v]^5`.  Thus row 30 nonlinear carry is genuinely
nonzero on the symbolic licensed prefix family.  This row-30 result is a new
desk calculation and is not promoted beyond this report.

## 1. Evidence boundary and hashes

Only the following relevant reviewed reports and files in the named case were
used substantively:

```text
67c4038230829b7b9abea540d78ec15af8f87aa66259c0c8b79873de6106251e
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/SOURCE.sha256
60e6b274ca6daa64dd5dc2ddb9cd62984dbefff3ae04d612f2ec36fe1e1e26bf
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/PREREGISTRATION.md
93db31ce9d3c7d41e42d496039eda9f58bc1d92938d16bb71e60b0722929b96e
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/TERMINAL_CUSTODY.md
6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a
  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md
7358e6623a84ddd6b1aaad1a9b07a1c0c8966f74f75203977c0314bf3588e7ec
  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md
46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1
  xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
60670d0a7066ab0a1d1f72ad05a0ff44a858fa39dbf4d18fd225913d26b6d114
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md
70fd8be4d3e00b4e14869166186cedf218fd3cd4370d0dcc049543a6853eb762
  xmodel/ideation-20260827T2259Z-opus5-hostile-review-sol-ultra.md
9c8c61a1ca6f71c3a04c396b176da4798817eff75f67e7508ed5be047d988c26
  xmodel/ideation-20260827T2259Z-carrier-hostile-review-sol-ultra.md
b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a
  xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md
```

The named case's four system JSON files containing the field all agree:

```text
RAW_DIRECT_SYSTEM.json                 D23_imposed: false
ROW_RREF/ROW_RREF_SYSTEM.json          D23_imposed: false
PREFIX_QUOTIENT/PREFIX_QUOTIENT_SYSTEM.json
                                       D23_imposed: false
HOMOGENIZED/HOMOGENIZED_SYSTEM.json    D23_imposed: false
```

The manifest was hashed but was not replayed with `shasum -c`, because it
contains a pin outside the user's allowed case directory.  No evidence from
that outside path is consumed here.

## 2. Exact row-28 calculation

The reviewed Lagrange--Buermann formula is

```text
q_n = 2/(n+2) [t^n] F(X,t)^((n+2)/8).                  (2.1)
```

Equivalently, with `F=H^2+sum_(i>=1)F_i t^i`, `p^4=H`, and

```text
S_(n,d)=sum_(i_1+...+i_d=n, i_j>=1) F_(i_1)...F_(i_d),
```

the `F`-degree-`d` part is

```text
[q_n]_d = 2/(n+2) binom((n+2)/8,d)
          p^(n+2-8d) S_(n,d).                          (2.2)
```

At `n=6`, `(n+2)/8=1`.  Therefore

```text
[q_6]_1 = F_6/4,
[q_6]_d = 0  for every d>=2,
q_6=F_6/4,
R_6=0.                                                  (2.3)
```

This also proves the result in every characteristic-zero branch and for every
prefix; rows 23--27 play no role in the identity.

### Correct normalization and ordinary residues

The row is `m=n+22=28`.  The reviewed normalization is

```text
c_28=p^-28 q_6=F_6/(4H^7) in V_28=coker(nabla_28),
nabla_28(f)=(f'+7(H'/H)f)dX.                            (2.4)
```

Multiplication by `H^7` is the licensed gauge:

```text
d(H^7 f)=H^7 nabla_28(f).
```

It sends (2.4) to the ordinary differential `(F_6/4)dX`.  In characteristic
zero this has the polynomial primitive `(1/4) integral F_6 dX`.  For the
frozen branch-P radical `A=X^4-1`, the complete ordinary residue coordinate is

```text
rho_28(X)=0 in Q[X]/(A),       res_infinity=0.           (2.5)
```

Thus the requested five-entry vector, after adjoining `i` only to label the
four roots, is `(0,0,0,0;0)`.

## 3. Why the named frozen fixture is not a licensed gate prefix

The case preregistration fixes

```text
A=X^4-1, H=A^2, F_1=H,
D_7=...=D_21=0, D_22=1,
```

and says verbatim that neither `D23=0` nor the `q1` image equation is an
input.  The reviewed branch-P row-23 theorem says

```text
[q_1dX]=0  iff  F_1 is in im(T_A),
T_A(Q)=2AQ'-3A'Q, deg Q<=12.
```

For `A=X^4-1`, the image has rank 13, while adjoining `H=A^2` raises the
rank to 14.  Hence `H` is outside the image.  The fixed case fails row 23 and
cannot be used at rows 27--30.

This is stronger than merely saying that the later rows were not run: the
literal frozen value is a reviewed negative control for the first one.
`TERMINAL_CUSTODY.md` further records no algebraic result from the terminal
runs.  The allowed evidence therefore supplies no nontrivial numeric
row-29 prefix with exact replay bytes.  No numeric assignment is introduced
below.

## 4. Reviewed pivot: row 30, not row 28

The `NU-LAW` correction makes every class row `m == 4 (mod 8)` universally
zero; row 28 is the first instance.  Row 29 is not a clean obstruction
candidate because the reviewed branch-P `F_7` newest-slot map has rank three
onto its three-dimensional receiver.  Row 30 has:

```text
n=8, m=30, (n+2)/8=5/4,
```

so it is not mod-8 dead, while its `F_8` linear class is killed by the
licensed branch-P gauge.  Its nonlinear remainder cannot be changed by the
newest slot.

### 4.1 Full exact `q_8` remainder

On branch P write `p^2=epsilon A`, `epsilon in {+1,-1}`.  Normalize the row
by `p^-30`; since

```text
nabla_30=d+15(A'/A)dX,
```

multiplication by `A^15` gauges it to the ordinary receiver.  Because
`A^15p^-30=epsilon`, the resulting ordinary representative is
`epsilon q_8`, independent of the choice of component after replacing each
`p`-power.  It is

```text
qbar_8 = A F_8/4 + R_8,

R_8 =  (1/32)       A^-3  S_(8,2)
      -(1/128)      A^-7  S_(8,3)
      +(7/2048)     A^-11 S_(8,4)
      -(77/40960)   A^-15 S_(8,5)
      +(77/65536)   A^-19 S_(8,6)
      -(209/262144) A^-23 S_(8,7)
      +(4807/8388608)A^-27 S_(8,8).                    (4.1)
```

The removed `AF_8/4` is polynomial and exact.  Formula (4.1), with no `F_8`,
is the correctly gauged row-30 nonlinear class.

## 5. Narrow symbolic prefix coordinate test

Let `A=X^4-1` and work over `Q[u,v]`.  The following coefficient-ring map is
a two-parameter slice of the frozen branch-P prefix ring:

```text
F_1=F_3=F_5=F_7=0,
F_2=4u A^2 A',
F_4=2u^2 (A')^2,
F_6=v.                                                   (5.1)
```

It respects every frozen window:

```text
deg F_2=11<=14, deg F_4=6<=12, deg F_6=0<=10.
```

It is a symbolic family, not a chosen rational point.  Its gate replay is
literal:

```text
q_1=q_3=q_5=q_7=0                         (F(t) is even),
q_2=F_2/(4A^2)=uA'=d(uA)/dX,
q_4=F_4/(4A)-F_2^2/(32A^5)=0,
q_6=F_6/4=v/4=d(vX/4)/dX.                               (5.2)
```

Thus (5.1) factors through the exact prefix coordinate ring for rows 23--29.
It uses only two parameters and is narrower than leaving the 91 coefficients
of `F_1,...,F_7` symbolic.

On (5.1), only the following ordered-composition sums survive in (4.1):

```text
S_(8,2)=2F_2F_6+F_4^2,
S_(8,3)=3F_2^2F_4,
S_(8,4)=F_2^4.
```

Substitution and exact collection give

```text
R_8 = (uv/4) A'/A + (u^4/4)(A')^4/A^3.                 (5.3)
```

For a simple root `alpha` of `A`, direct Laurent expansion gives

```text
res_alpha ((A')^4/A^3 dX)
 = (3/2)(A'''(alpha)+A''(alpha)^2/A'(alpha)).           (5.4)
```

For `A=X^4-1`, (5.4) is `90 alpha`.  Therefore, in the order
`1,-1,i,-i,infinity`, (5.3) has the residue vector printed in Section 0.
The five entries sum to zero, as required.  The common residue ideal on this
slice is

```text
(uv,u^4) in Q[u,v],                                    (5.5)
```

whose radical is `(u)`.  In particular the vector is not the zero element of
the prefix coordinate ring: row 30 nonlinear carry is real on this symbolic
licensed family.

## 6. Exact replay

This is the complete computation run locally.  It uses only
`fractions.Fraction`; there is no CAS, random seed, Groebner basis, or hidden
file input.

```bash
python3 - <<'PY'
from fractions import Fraction as Q
from math import factorial

def binom(a,d):
    z=Q(1)
    for j in range(d): z*=a-j
    return z/factorial(d)
def c(n,d): return Q(2,n+2)*binom(Q(n+2,8),d)

assert c(6,1)==Q(1,4)
assert all(c(6,d)==0 for d in range(2,7))
print('q6_coefficients_d1_to_d6 =', [str(c(6,d)) for d in range(1,7)])

cs=[c(8,d) for d in range(1,9)]
print('q8_coefficients_d1_to_d8 =', [str(x) for x in cs])
assert cs==[Q(1,4),Q(1,32),-Q(1,128),Q(7,2048),
            -Q(77,40960),Q(77,65536),-Q(209,262144),Q(4807,8388608)]

# F2=4u A^2 A', F4=2u^2(A')^2, F6=v.
assert Q(2,4)==Q(16,32)  # q4 linear/carry cancellation
uv=cs[1]*2*4
u4=cs[1]*4 + cs[2]*3*(4**2)*2 + cs[3]*(4**4)
assert uv==Q(1,4) and u4==Q(1,4)
print('slice_R8 = (1/4)uv*Aprime/A + (1/4)u^4*Aprime^4/A^3')

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def inv(z):
    d=z[0]*z[0]+z[1]*z[1]
    return (z[0]/d,-z[1]/d)
def div(z,w): return mul(z,inv(w))
def scale(a,z): return (a*z[0],a*z[1])
def power(z,n):
    r=(Q(1),Q(0))
    for _ in range(n): r=mul(r,z)
    return r

roots=[(Q(1),Q(0)),(-Q(1),Q(0)),(Q(0),Q(1)),(Q(0),-Q(1))]
res=[]
for a in roots:
    A1=scale(Q(4),power(a,3))
    A2=scale(Q(12),power(a,2))
    A3=scale(Q(24),a)
    res.append(scale(Q(3,2),add(A3,div(mul(A2,A2),A1))))
assert res==[(Q(90),Q(0)),(-Q(90),Q(0)),
             (Q(0),Q(90)),(Q(0),-Q(90))]
print('Res_roots(Aprime^4/A^3 dX) =',res)
print('row30_slice_residue_vector = '
      '(uv/4+45u^4/2, uv/4-45u^4/2, '
      'uv/4+45i*u^4/2, uv/4-45i*u^4/2, -uv)')
print('PASS')
PY
```

Exact output:

```text
q6_coefficients_d1_to_d6 = ['1/4', '0', '0', '0', '0', '0']
q8_coefficients_d1_to_d8 = ['1/4', '1/32', '-1/128', '7/2048', '-77/40960', '77/65536', '-209/262144', '4807/8388608']
slice_R8 = (1/4)uv*Aprime/A + (1/4)u^4*Aprime^4/A^3
Res_roots(Aprime^4/A^3 dX) = [(Fraction(90, 1), Fraction(0, 1)), (Fraction(-90, 1), Fraction(0, 1)), (Fraction(0, 1), Fraction(90, 1)), (Fraction(0, 1), Fraction(-90, 1))]
row30_slice_residue_vector = (uv/4+45u^4/2, uv/4-45u^4/2, uv/4+45i*u^4/2, uv/4-45i*u^4/2, -uv)
PASS
```

## 7. Claim ledger and firewalls

**Decided exactly:**

1. `q_6=F_6/4` and `R_6=0` over the unrestricted source ring.
2. The correctly normalized/gauged row-28 class and its complete ordinary
   residue vector are identically zero.
3. The named frozen endpoint fixture is not a row-23 prefix: it fixes the
   reviewed `q1` negative control and omits `D23` by construction.
4. The symbolic family (5.1) passes every class row 23--29 exactly.
5. The correctly gauged row-30 nonlinear remainder and residue vector on
   that symbolic family are nonzero.

**Not claimed:**

* The row-30 result is not a numeric survivor, a generic theorem for the
  whole 71-dimensional prefix locus, or an independently reviewed promotion.
* Class exactness is only a necessary consequence of a full polynomial
  determinant solution.  The symbolic family is not asserted to have a
  polynomial `G`, satisfy `D22=1`, or satisfy any raw row `D23...D30`.
* Universal class-row death at row 28 does not imply raw `D28` is the zero
  polynomial or that its polynomial-window descent condition is vacuous.
* No endpoint, face/family exclusion, Keller pair, landing, counterexample,
  finite tower bound, or JC2 conclusion follows.
* No AWS host/job was contacted.  No heavy local computation ran.  No
  canonical file was edited; this report is the only write.
* No path under `jc2-lean` was listed, opened, searched, read, built,
  statused, or modified.  No content from it is used.

The maximum licensed conclusion is therefore:

```text
R28-CLASS = IDENTICALLY ZERO (universal exact control).
R30-CLASS = NONZERO on the exact symbolic prefix slice (5.1),
            pending independent review and with every raw/endpoint firewall.
```
