# `R34-ALGPRIM-ARTIN` — exact whole-series no-cut on the zero-tail slice

Date: 2026-08-27  
Lane: Sol Ultra, exact desk algebra  
Status: **PROVISIONAL SUCCESSOR; DIFFERENT-MODEL REVIEW REQUIRED BEFORE PROMOTION**

No raw determinant equation, polynomial-`G` lift, endpoint decision, family
exclusion, landing claim, or JC2 theorem is made.

## 0. Verdict

Let

```text
A=X^4-1,       B=A'=4X^3,
R=Q[u,v]/(uv,u^4,v^2).                                (0.1)
```

Take the zero-tail section of the provisional row-34 prefix family:

```text
F_0=A^4,
F_2=4u A^2B,       F_4=2u^2B^2,       F_6=v,
F_i=0 for every other i>=1.                            (0.2)
```

For either branch-P sign `epsilon in {+1,-1}`, fix `p^2=epsilon A` and
let `Q=P^2` be the selected Hensel solution of `P^8=F(X,sP)`.  Then the
**entire** selected series, not a truncation, is

```text
Q=epsilon A+uB s^2+(v/4)s^6             in R(X)[s].    (0.3)
```

Consequently Fable5's reviewed algebraic-primitive differential specializes
to

```text
alpha_F=-(s^21/16)(d_s(s^2Q)-2p^2s)dX
       =-(u/4)B s^24 dX-(v/8)s^28 dX
       =d_X beta,                                      (0.4)

beta=-(u/4)A s^24-(v/8)X s^28 in R[X,s].              (0.5)
```

Thus the `GATE-ALG-PRIM` obstruction makes **no further cut** on this
zero-tail Artin section.  Its Hermite remainder, every residue, and the full
residual de Rham class are zero because an explicit polynomial primitive is
already displayed.

There is a useful stronger operational consequence.  Equation (0.3) says

```text
q_0=epsilon A,       q_2=uB,       q_6=v/4,
q_n=0 for every other n.                              (0.6)
```

Hence this section survives the **whole coefficientwise class tower**, not
only rows 23--34, and its primitives assemble algebraically.  Continuing to
compute later class rows cannot shrink the projected Artin base (0.1) along
this section.  The next discriminator for this slice must cross the class-to-
raw boundary: raw determinant compatibility and polynomial-window descent
for `G`.

This is not an actual nonzero field-valued survivor.  Every map from `R` to a
field kills `u` and `v`, so the reviewed field-level theorem sees only the
origin, where `alpha_F=0`.  The nonreduced statement above is a direct exact
identity over an Artin coefficient ring; it must not be misreported as an
application of a theorem stated only over `K(F)`.

## 1. Dependency and exact hashes

The only load-bearing inputs are the provisional descendant's quotient and
zero-tail section, the corrected characteristic identity, and the reviewed
typing of `GATE-ALG-PRIM`:

```text
e5a2c968e516a40509d136cfd57613c8be84e50041444ce8146916b976bdf24c
  xmodel/ggv-quarter-root-r30-slice-descendant-r0-sol-ultra-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
e9f2a333ef94161e3e9c54288e4e06ed1047ee7a9c93254811787e6a2d517090
  xmodel/ideation-20260827T2259Z-fable5-crossreview-opus5.md
9c8c61a1ca6f71c3a04c396b176da4798817eff75f67e7508ed5be047d988c26
  xmodel/ideation-20260827T2259Z-carrier-hostile-review-sol-ultra.md
```

The descendant is provisional.  If its ideal `(uv,u^4,v^2)` or its
interpretation as the row-34 projected prefix is repaired, the campaign must
replace `R` in (0.1) and rerun the ten-line quotient calculation below.
The identities conditional on the displayed quotient remain exact.

## 2. The zero-tail section is licensed through row 34

The descendant's full prefix coordinate ring has 24 free newest-slot
coordinates over `R`.  Set every one of them to zero.  The row-31 and row-33
unit-pivot equations then set all dependent odd-slot coordinates to zero as
well, while the row-30, row-32, and row-34 class ideals vanish in `R`:

```text
(uv,u^4)=0,
(u^2v,u^5)=0,
(v^2,u^3v,u^6)=0.                                    (2.1)
```

This defines an honest section of the provisional **class-prefix scheme**.
It is exactly (0.2).  The upper source windows are respected:

```text
deg F_2=11<=14,       deg F_4=6<=12,       deg F_6=0<=10,
```

and all later allowed slots are simply specialized to zero.

This section statement is about the class-prefix scheme.  It says nothing
about any raw `D_m`, any `G` coefficient, or the endpoint normalization.

## 3. Whole-series Hensel calculation

From `P^8=F(X,sP)` and `Q=P^2`, (0.2) gives the exact implicit equation

```text
Q^4=A^4+4uA^2B s^2Q+2u^2B^2s^4Q^2+v s^6Q^3.          (3.1)
```

Put

```text
Q_*=epsilon A+uB s^2+(v/4)s^6.                        (3.2)
```

Direct expansion of (3.1) at `Q_*` leaves only monomials divisible by
`uv`, `u^4`, or `v^2`; hence it is zero in `R(X)[s]`.  At `s=0`,

```text
Q_*(0)=epsilon A=p^2.
```

The derivative of the left side of (3.1), moved to one side, with respect
to `Q` is `4epsilon A^3` at `(s,Q)=(0,epsilon A)`.  It is a unit in
`R(X)`.  Formal implicit-function uniqueness therefore identifies `Q_*`
with the selected Hensel branch.  This proves (0.3) as a **whole-series
identity**.  It is not an extrapolation from the checked rows 23--34.

Equivalently, (0.6) is the complete list of nonzero `q_n` in the Artin
quotient.  The familiar prefix identities become

```text
q_2dX=d_X(uA),       q_6dX=d_X(vX/4),                 (3.3)
```

and all remaining positive-index class rows vanish identically.

## 4. `GATE-ALG-PRIM` specialization

The reviewed repaired filter is

```text
alpha_F=-(s^21/16)(d_s(s^2P^2)-2p^2s)dX.              (4.1)
```

Using (0.3),

```text
s^2Q=epsilon A s^2+uB s^4+(v/4)s^8,
d_s(s^2Q)-2p^2s=4uB s^3+2v s^7.                      (4.2)
```

Substitution gives (0.4), and differentiating (0.5) gives it back exactly.
The primitive begins at order `s^24`, which is compatible with (and stronger
than) the redundant `s`-order-at-least-23 normalization.

No algebraic integration algorithm is needed on this section:

* there are no finite poles to reduce;
* exact polynomial differentials have zero residue, including at infinity;
* the second-kind/de Rham remainder is zero by the explicit primitive; and
* `beta` lies in the rational base ring before adjoining either `p` or `P`.

Thus it is also a primitive in the natural base change

```text
E'_R=R(X,s,p,P)/(p^2-epsilon A, P^2-Q),                (4.3)
```

localized at the selected branches.  There is no trace or constant-field
descent issue in this calculation.

## 5. Field, Artin, class, raw, and descent firewalls

### 5.1 Field versus nonreduced coefficient ring

`R` is a length-five local Artin algebra with basis
`1,u,u^2,u^3,v`; it is not a field.  The reviewed necessity theorem for an
actual polynomial client is stated over a characteristic-zero field and the
finite algebraic function field `E'`.  Therefore the literal field theorem
does not by itself certify tangent or nilpotent directions.

What is proved here is stronger at the level of formulas but narrower in
scope: (0.4)--(0.5) are direct identities over `R`.  If one extends the
algebraic-primitive test functorially to Artin coefficient rings, its pullback
to this section is identically zero.  On every actual field-valued point of
this quotient, `u=v=0`, and the same conclusion reduces to the vacuous
identity `alpha_F=0`.

### 5.2 Rational versus algebraic integration

The selected `P` is algebraic, but `alpha_F` and `beta` on this quotient
already lie in `R[X,s]dX` and `R[X,s]`, respectively.  Hence rational
integration succeeds before algebraic extension.  This is not an example
where residues vanish but a positive-genus de Rham class survives.

### 5.3 Whole series versus truncation

The row-34 report supplied a finite prefix.  The Hensel argument in Section 3
is what licenses the infinite conclusion.  Without formal uniqueness, checking
only `q_1,...,q_12` would not license (0.6) or the assembled primitive.

### 5.4 Class versus raw determinant

Equations (0.4) and (3.3) establish class exactness and algebraic assembly of
the class primitives.  They do not impose or solve

```text
D_0=...=D_21=0,       D_22=1,       D_23=...=D_35=0.
```

No `D_m` is computed in this report.  In particular, a class row that is
exact can still carry a nontrivial polynomial-window compatibility condition
in the raw determinant system.

### 5.5 Polynomial-`G` window descent

The polynomial `beta(X,s)` is only an `X`-primitive of `alpha_F`.  It does not
construct a polynomial

```text
G(X,t)=P^12 W(X,t/P),
```

does not supply the endpoint coefficient `w_22`, does not fix the arbitrary
`X`-constant series, and does not prove that the resulting algebraic expression
descends to the frozen `G` support window.  `GATE-ALG-PRIM` is necessary, not
sufficient, and this section passes only that necessary filter.

### 5.6 Scope inside the 24-slot descendant

The zero-tail choice is one section of the descendant's 24-dimensional
new-slot bundle.  The result does not say that `GATE-ALG-PRIM` is exact for
every nonzero choice of those slots, nor that it imposes no equations mixing
`u,v` with them.  It does show that the gate cannot remove the projected
Artin base along this section, and that there is no point in funding later
class rows merely to try to kill this section.

## 6. Exact replay

The replay uses a sparse five-variable polynomial dictionary and the quotient
rules `epsilon^2=1`, `uv=u^4=v^2=0`.  It has no CAS, random input, or hidden
file dependency.

```bash
python3 - <<'PY'
from fractions import Fraction as Q

# Sparse polynomials in (X,s,u,v,epsilon).
def norm(p):
    z={}
    for (ix,is_,iu,iv,ie),c in p.items():
        c=Q(c)
        if not c or iu>=4 or iv>=2 or (iu and iv):
            continue
        m=(ix,is_,iu,iv,ie&1)       # epsilon^2=1
        z[m]=z.get(m,Q(0))+c
    return {m:c for m,c in z.items() if c}
def add(*ps):
    z={}
    for p in ps:
        for m,c in p.items(): z[m]=z.get(m,Q(0))+c
    return norm(z)
def neg(p): return {m:-c for m,c in p.items()}
def scale(c,p): return norm({m:Q(c)*a for m,a in p.items()})
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
U=mono(u=1); V=mono(v=1); E=mono(e=1)
A=add(pw(XX,4),neg(ONE)); B=dx(A)

Qsel=add(mul(E,A), mul(U,B,pw(SS,2)),
         scale(Q(1,4),mul(V,pw(SS,6))))
rhs=add(pw(A,4),
        scale(4,mul(U,pw(A,2),B,pw(SS,2),Qsel)),
        scale(2,mul(pw(U,2),pw(B,2),pw(SS,4),pw(Qsel,2))),
        mul(V,pw(SS,6),pw(Qsel,3)))
assert add(pw(Qsel,4),neg(rhs))=={}

alpha=scale(Q(-1,16),mul(
    pw(SS,21),
    add(ds(mul(pw(SS,2),Qsel)),scale(-2,mul(E,A,SS)))))
beta=add(scale(Q(-1,4),mul(U,A,pw(SS,24))),
         scale(Q(-1,8),mul(V,XX,pw(SS,28))))
assert add(alpha,neg(dx(beta)))=={}

print('implicit equation modulo (uv,u^4,v^2): PASS')
print('alpha = d_X beta modulo (uv,u^4,v^2): PASS')
print('support(Q)=',sorted(Qsel))
print('support(alpha)=',sorted(alpha))
print('support(beta)=',sorted(beta))
PY
```

Exact output:

```text
implicit equation modulo (uv,u^4,v^2): PASS
alpha = d_X beta modulo (uv,u^4,v^2): PASS
support(Q)= [(0, 0, 0, 0, 1), (0, 6, 0, 1, 0),
             (3, 2, 1, 0, 0), (4, 0, 0, 0, 1)]
support(alpha)= [(0, 28, 0, 1, 0), (3, 24, 1, 0, 0)]
support(beta)= [(0, 24, 1, 0, 0), (1, 28, 0, 1, 0),
               (4, 24, 1, 0, 0)]
```

## 7. Stop/continue recommendation

**STOP** `GATE-ALG-PRIM` and later class-row work on this particular
zero-tail Artin section.  The whole selected `Q` series is known and its
assembled primitive is polynomial, so neither can cut it.

**CONTINUE** the slice only at the next honest interface:

1. raw determinant rows through the full possible range, with `D_22=1`; or
2. direct polynomial-`G` window descent/compatibility from the assembled
   formal solution.

Keep `GATE-ALG-PRIM` funded elsewhere: apply it to a genuine field-valued
whole-tower survivor or to a nonzero-slot family where coefficientwise
primitives are known but assembly is not.  This slice is a clean negative
control for the claim that the algebraic-primitive gate is automatically
strictly stronger than the class tower.

No option-B raw equation is asserted here because option A is completely
decided on the charged section.  Deriving a raw equation without compiling
the frozen `G` windows would cross the class/raw firewall.

No AWS resource was contacted.  No heavy local computation ran.  No
canonical ledger was edited.  No path under `jc2-lean` was listed, searched,
read, built, statused, or modified.
