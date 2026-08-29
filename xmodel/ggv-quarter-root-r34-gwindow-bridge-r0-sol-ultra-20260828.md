# `R34-GWINDOW-BRIDGE` — the zero-tail Artin section misses the raw endpoint

Date: 2026-08-28 UTC  
Lane: Sol Ultra, exact desk algebra  
Status: **PROVISIONAL SUCCESSOR; BOTH PARENTS RETAIN THEIR ROLLBACK LABELS;
DIFFERENT-MODEL REVIEW REQUIRED BEFORE PROMOTION**

No canonical ledger is edited by this report.  No family exclusion, landing
claim, polynomial Keller pair, counterexample, or JC2 theorem is claimed.

## 0. Verdict

Retain the provisional zero-tail section

```text
A=X^4-1,  B=A'=4X^3,
R=Q[u,v]/(uv,u^4,v^2),  m=(u,v),

F=A^4+4uA^2B t^2+2u^2B^2 t^4+v t^6.                 (0.1)
```

For either branch `epsilon in {+1,-1}`, choose `p^2=epsilon A`.  Conditional
on the parent whole-series identity

```text
Q=P^2=epsilon A+uB s^2+(v/4)s^6,                     (0.2)
```

the **most general characteristic solution** of the exact determinant target
is

```text
W(X,s)=Phi(s)
       -(epsilon/8)(X^5/5-X)s^22
       -(u/4)A s^24-(v/8)X s^28,                     (0.3)

Phi(s)=sum_(m>=0)c_m s^m,  c_m in ker(d/dX),
c_0=1 if G_0=A^6 is imposed.                         (0.4)
```

Thus the missing `X`-constant freedom does not rescue this section.  Writing
`P_hat(X,t)=F(X,t)^(1/8)` for the selected original-coordinate root, the
correct reconstruction is

```text
G(X,t)=P_hat^12 W(X,t/P_hat)
 =sum_(m>=0)c_m t^m P_hat^(12-m)
  -(epsilon/8)(X^5/5-X)t^22 P_hat^-10
  -(u/4)A t^24 P_hat^-12
  -(v/8)X t^28 P_hat^-16.                            (0.5)
```

This is an algebraic formal series a priori, not a descended polynomial.
The literal frozen `G` polygon has no weight-22 slot: `G_22=0`.  Reducing
(0.5) modulo `m` makes `P_hat=p` independent of `t`, so

```text
G_22 mod m=p^-10(c_22-(epsilon/8)(X^5/5-X)).          (0.6)
```

Vanishing would force an `X`-constant `c_22` to equal the nonconstant
function `(epsilon/8)(X^5/5-X)`, an impossibility.  Equivalently, directly
from the raw determinant recurrence, `D_22` belongs to `m` for every allowed
`G`, whereas the target is `D_22=1`.

Hence the raw endpoint fibre product of this Artin section with the literal
`G` window is the **empty scheme**.  No nonzero nilpotent direction survives;
more strongly, even its reduced origin does not survive.  The class tower
and algebraic-primitive gate can pass consistently because they do not
encode this polynomial-window obstruction.

## 1. Custody and rollback

Exact live-byte hashes at the start of this derivation were

```text
525c408e92b7f2cb11f5152e002e60a20a331d268283f1be30fb13b5a104b990
  xmodel/ggv-quarter-root-r34-algprim-artin-bridge-r0-sol-ultra-20260827.md
e5a2c968e516a40509d136cfd57613c8be84e50041444ce8146916b976bdf24c
  xmodel/ggv-quarter-root-r30-slice-descendant-r0-sol-ultra-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
f3c758e052d95252438fb9665ac2f2b27705019e91a41c2aa851dd41e9463bf4
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/compile_d3.py
f0fe0f5dd01d9d47f6b7ee58d3e3426e482a4f8c9d31a81bfa2094782d010e00
  xmodel/ggv-8_28-raw-global-determinant-d5g35-sol2-20260827.md
ba7162fe8fd7c4f607839ce2c18525c6aa21a322343a938f738d7ec514113a2d
  xmodel/ggv-8_28-raw-global-determinant-d5g35-hostile-review-grok-20260827.md
```

The first two reports remain provisional.  The characteristic calculation
below is conditional on their exact quotient and zero-tail section.  If
`R`, (0.1), or (0.2) changes, equations (0.3)--(0.6) must be recomputed.

There is also a rollback-independent core: for the displayed `F` in (0.1),
the direct raw calculation in Section 6 proves endpoint emptiness without
using the class descendant, Hensel uniqueness, or the characteristic
theorem.  Thus a future repair of the *interpretation* of the Artin section
would not alter the algebraic statement about the displayed coefficient
ring and polynomial.

## 2. Literal frozen windows

The raw chart sends `x^i y^j` to `t^(8+3i-j)X^i` on the `F` polygon and to
`t^(12+3i-j)X^i` on the `G` polygon.  The independently frozen enumeration
therefore gives

```text
F_n: max(0,ceil((n-8)/3))  <= deg_X monomial <= 16-n,
G_n: max(0,ceil((n-12)/3)) <= deg_X monomial <= 24-n. (2.1)
```

An empty interval means the coefficient is literally zero.  In particular,

```text
G_21 in <X^3>,       G_22=0,       G_n=0 for every n>=22. (2.2)
```

The section (0.1) respects the `F` windows:

```text
deg F_2=11<=14,  deg F_4=6<=12,  deg F_6=0<=10.
```

The only support consequence needed for the decision is `G_22=0`.  The
stronger lower-row monomial bounds cannot repair a contradiction already
present in that mandatory coefficient.

## 3. Full characteristic solution, including constants

The exact characteristic identity is

```text
W_X|s=-(s^22/8)(Q+(s/2)Q_s).                          (3.1)
```

For (0.2),

```text
Q+(s/2)Q_s=epsilon A+2uB s^2+v s^6.                  (3.2)
```

Put

```text
J=X^5/5-X,       J'=A.                                (3.3)
```

Coefficientwise integration of (3.1) gives exactly (0.3).  There are no
other terms: the homogeneous equation is `W_X=0`, whose full solution is
one arbitrary `X`-constant series `Phi(s)`, not merely constants below
weight 22.  In the present geometrically integral quadratic branch over
`Q`, the constant ring is `R`; writing `ker(d/dX)` in (0.4) also covers a
harmless extension of the ground constant field.

At `s=0`, `P^12=p^12=A^6`, and the particular solution has positive
`s`-order.  Therefore the leading normalization `G_0=A^6` is precisely

```text
c_0=1.                                                  (3.4)
```

Notice that the endpoint term omitted from the parent's assembled
algebraic-primitive differential is restored here:

```text
w_22'=-(1/8)q_0=-(epsilon/8)A,
w_22=c_22-(epsilon/8)J.                                (3.5)
```

The `u` and `v` terms in (0.3) are the parent's displayed primitive tail;
(3.5) is the additional term needed to impose `D_22=1` rather than only
the post-endpoint class rows.

## 4. Correct reconstruction and its category

Use separate notation for the same selected eighth root in the two
coordinates:

```text
P_hat(X,t)^8=F(X,t),       P_hat(X,0)=p,
s=t/P_hat(X,t).                                      (4.1)
```

Substituting (0.3) into `G=P_hat^12W(X,t/P_hat)` gives (0.5), term by term.
Negative powers are legitimate in the algebraic function-field completion
because `P_hat` has nonzero constant term.  They are not evidence of
polynomial descent.

For reference, the square of the original-coordinate root is itself an
exact finite expression in this Artin quotient:

```text
P_hat^2=epsilon[
 A+(uB/A)t^2-(u^2B^2/A^3)t^4
 +(2u^3B^3/A^5+v/(4A^3))t^6].                         (4.2)
```

Raising (4.2) to the fourth power gives (0.1): the apparent `u^3t^6`
terms cancel as `8-12+4=0`.  Formula (4.2) is useful for expanding every
coefficient of (0.5), but the endpoint decision needs only its reduction

```text
P_hat mod m=p.                                         (4.3)
```

The three categories are therefore distinct:

* (0.3) is an exact **formal characteristic** solution over the Artin
  algebraic extension;
* (0.5) is an exact **algebraic formal** reconstruction in the original
  coordinate; and
* a campaign client must further lie in the literal **polynomial** module
  `R[X,t]` with every coefficient in (2.1).

The last condition fails.

## 5. Characteristic proof of window failure

Reduce the reconstructed solution modulo `m=(u,v)`.  Then

```text
F_bar=A^4,       P_hat_bar=p,
G_bar=p^12 Phi_bar(t/p)
      -(epsilon/8)J t^22p^-10.                        (5.1)
```

Because `p` is now independent of `t`, different characteristic constants
do not mix weights.  The coefficient at weight 22 is exactly (0.6).  The
frozen window requires it to vanish.  Since `p` is nonzero in the function
field, this says

```text
c_bar_22=(epsilon/8)J.                                 (5.2)
```

The left side is killed by `d/dX`; the derivative of the right side is
`epsilon A/8 != 0`.  Contradiction.  This argument allows **all** constants
`c_m`, including `c_22` and every `c_m` above it.

As a check that the lower windows have not been silently ignored, their
reduced effect can be classified explicitly.  For `0<=n<=21`,

```text
[t^n](p^12 Phi_bar(t/p))=c_bar_n p^(12-n).             (5.3)
```

Polynomial descent and (2.1) permit arbitrary constants at even
`n=0,2,...,12` (with `c_bar_0=1`) because
`p^(12-n)=(epsilon A)^(6-n/2)` lies in the window.  They force the odd
constants and the even constants at `n=14,16,18,20` to vanish.  None can
contribute to weight 22 because `p` has no positive `t`-coefficients after
reduction.  Thus (5.2) is not an artifact of prematurely setting the
homogeneous series to zero.

## 6. Independent raw endpoint certificate

The frozen coefficient recurrence is

```text
D_n=sum_(i+j=n)[(12-j)F_i'G_j+(i-8)F_iG_j'].           (6.1)
```

On (0.1), with literal `G_22=0`, only three pairs can contribute at the
endpoint:

```text
D_22=
 -32u(A^2B)'G_20-24uA^2B G_20'
 -12u^2(B^2)'G_18-8u^2B^2 G_18'
 -2vG_16'.                                             (6.2)
```

This formula allows every coefficient in the frozen windows for
`G_16,G_18,G_20`; no lower determinant row is assumed.  Every term of
(6.2) lies in `m R[X]`, so

```text
D_22 mod m=0.                                          (6.3)
```

Let `S` be the polynomial ring over `R` on all allowed `G` coefficients.
The scalar coefficient equation of `D_22=1` is `-1+n=0` for some
`n in mS`.  Since `m^4=0`, this generator is already a unit, with explicit
inverse

```text
(-1+n)^-1=-(1+n+n^2+n^3).                             (6.4)
```

Therefore the endpoint ideal is the unit ideal in `S`.  This is an empty
scheme statement, not merely absence of `Q`-valued points and not merely a
tangent-space rank calculation.

This independently sanity-checks the endpoint/post-endpoint distinction:
if the target were changed from `D_22=1` to `D_22=0`, the unit obstruction
would disappear, while the class/primitive tail would remain unchanged.

## 7. What is and is not decided

**Conditionally decided on the displayed provisional section:**

1. The full `X`-constant freedom in `W` is (0.3)--(0.4).
2. The exact original-coordinate algebraic reconstruction is (0.5).
3. `G_0=A^6` fixes only `c_0=1`; it does not fix `c_22`.
4. The literal polygon forces `G_22=0`, which is incompatible with the
   endpoint primitive already after reduction modulo `(u,v)`.
5. Scheme-theoretically the raw endpoint intersection is empty.  Neither
   `u`, `v`, nor the reduced origin survives.

**Not decided or claimed:**

* The provisional row-30/row-34 class-scheme ancestry is not promoted.
* This does not exclude other choices of the 24 newest `F` slots, another
  class-prefix section, or the full branch-P family.
* No statement is made about a polynomial `G` if the frozen source polygon
  is enlarged to admit weight 22.
* Passing all class rows and the algebraic-primitive gate is not contradicted;
  those are necessary shadows that do not encode this support failure.
* No raw solution, endpoint normalization, face/family exclusion, GGV
  landing, or JC2 conclusion is exported beyond this exact slice.

## 8. Exact replay

The following uses only `fractions.Fraction` and sparse dictionaries.  It
rechecks the Artin quotient, the whole implicit `Q` identity, the full
characteristic derivative including the endpoint term, and the literal
weight-22 window.

```bash
python3 - <<'PY'
from fractions import Fraction as Q

# Sparse polynomials in (X,s,u,v,epsilon), reduced by
# uv=u^4=v^2=0 and epsilon^2=1.
def norm(p):
    z={}
    for (ix,is_,iu,iv,ie),c in p.items():
        c=Q(c)
        if not c or iu>=4 or iv>=2 or (iu and iv):
            continue
        m=(ix,is_,iu,iv,ie&1)
        z[m]=z.get(m,Q(0))+c
    return {m:c for m,c in z.items() if c}
def add(*ps):
    z={}
    for p in ps:
        for m,c in p.items(): z[m]=z.get(m,Q(0))+c
    return norm(z)
def sc(c,p): return norm({m:Q(c)*a for m,a in p.items()})
def neg(p): return sc(-1,p)
def mul2(p,q):
    z={}
    for a,c in p.items():
        for b,d in q.items():
            m=tuple(a[i]+b[i] for i in range(5))
            z[m]=z.get(m,Q(0))+c*d
    return norm(z)
def mul(*ps):
    z={(0,0,0,0,0):Q(1)}
    for p in ps: z=mul2(z,p)
    return z
def pw(p,n): return mul(*([p]*n))
def dx(p):
    return norm({(a-1,b,c,d,e):k*a
                 for (a,b,c,d,e),k in p.items() if a})
def ds(p):
    return norm({(a,b-1,c,d,e):k*b
                 for (a,b,c,d,e),k in p.items() if b})
def mono(c=1,X=0,s=0,u=0,v=0,e=0):
    return norm({(X,s,u,v,e):Q(c)})

ONE=mono(); XX=mono(X=1); SS=mono(s=1)
U=mono(u=1); V=mono(v=1); EPS=mono(e=1)
A=add(pw(XX,4),neg(ONE)); B=dx(A)
J=add(sc(Q(1,5),pw(XX,5)),neg(XX))
assert dx(J)==A

Qsel=add(mul(EPS,A),mul(U,B,pw(SS,2)),
         sc(Q(1,4),mul(V,pw(SS,6))))
rhs=add(pw(A,4),
        sc(4,mul(U,pw(A,2),B,pw(SS,2),Qsel)),
        sc(2,mul(pw(U,2),pw(B,2),pw(SS,4),pw(Qsel,2))),
        mul(V,pw(SS,6),pw(Qsel,3)))
assert add(pw(Qsel,4),neg(rhs))=={}

Wpart=add(sc(Q(-1,8),mul(EPS,J,pw(SS,22))),
          sc(Q(-1,4),mul(U,A,pw(SS,24))),
          sc(Q(-1,8),mul(V,XX,pw(SS,28))))
char_rhs=sc(Q(-1,8),mul(
    pw(SS,22),add(Qsel,sc(Q(1,2),mul(SS,ds(Qsel))))))
assert dx(Wpart)==char_rhs

def ceil_div(a,b): return -((-a)//b)
def window(kind,n):
    shift,mx=(8,16) if kind=='F' else (12,24)
    lo=max(0,ceil_div(n-shift,3)); hi=mx-n
    return list(range(lo,hi+1)) if lo<=hi else []
assert window('G',21)==[3]
assert window('G',22)==[]
assert window('F',2)==list(range(15))

print('Q implicit identity in R: PASS')
print('W_X characteristic identity in R: PASS')
print('G21 window:',window('G',21),'; G22 window:',window('G',22))
print('mod (u,v): F_i=0 for i>0 and G22=0, hence D22=0 != 1: PASS')
PY
```

Exact output:

```text
Q implicit identity in R: PASS
W_X characteristic identity in R: PASS
G21 window: [3] ; G22 window: []
mod (u,v): F_i=0 for i>0 and G22=0, hence D22=0 != 1: PASS
```

## 9. Stop/continue recommendation

**STOP this zero-tail Artin section.**  It is not a raw endpoint survivor,
so neither later class rows nor a larger raw elimination on this same
section can add useful information.  The clean certificate is the one-line
unit obstruction (6.3)--(6.4).

**CONTINUE the class-to-raw bridge on a section with a genuine reduced raw
endpoint point.**  A useful prerequisite for the next slice is that some
positive-weight `F_i` have nonnilpotent reduction, so the pairs
`F_i G_(22-i)` can supply the scalar endpoint without a forbidden `G_22`.
Only after that test passes is it worth solving the lower raw rows or the
full polynomial-window descent equations.

No AWS resource was used; all work was exact desk algebra.  No heavy local
CAS ran.  No path under `jc2-lean` was listed, searched, read, built,
statused, or modified.  This report is the only write.
