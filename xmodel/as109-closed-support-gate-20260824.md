# AS109 closed-support gate: independent slots and affine-`y` corrections

**Verdict: `NO-INDEPENDENT-SLOT-CERTIFICATE / AFFINE-Y NO-GO`.**

- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Prime/seed: `p=109`, `(x-x^109,y)` over `F_109`
- Exact coefficient ring: `R=Z_109`
- Literal-slot cap: none needed; the first theorem excludes every finite cap
- Exponent rectangle, cap widening, AWS, or finite-level enumeration: none
- Exact lift found: no
- Characteristic-zero or JC2 inference: none

The smallest natural `CLOSED-SUPPORT + UNIT-L` redesign does not work.  If a
finite support is interpreted as the full coefficient module on independent
labeled monomial slots, nonlinear closure and a unit right inverse force the
residual module to contain `x^(108k)` for every `k>=1`.  It is therefore not
finite.  Essential linear coupling between slots is not optional.

The simplest coupled escape is also impossible: there is no exact
determinant-one lift whose two correction polynomials are affine in `y`, no
matter how large their `x`-degrees are.  Thus a surviving coupled certificate
must both impose genuine coefficient relations and use `y`-degree at least
two.

These are structural no-go theorems for two natural certificate families.
They do **not** exclude a finite non-coordinate gauge section with nonlinear
`y`-dependence, and they prove neither existence nor nonexistence of an
arbitrary fixed-support lift.

## 1. Exact packed equation

Put

```text
p=109,                 s=x^108,
F_(A,B)=(x-x^p+pA, y+pB),       A,B in R[x,y],
L(A,B)=A_x+B_y,
N(A,B)=(A_x-s)B_y-A_yB_x.
```

The two-by-two determinant gives the exact identity

```text
det J(F_(A,B))-1 = p (L(A,B)-s+pN(A,B)).                 (1.1)
```

There are no digit choices or base-109 carries in (1.1).  This is the packed
equation used by the already-banked conditional contraction criterion.

## 2. No finite full independent literal-slot certificate

### 2.1 Precise hypotheses

A labeled literal correction slot is one of

```text
P(a,b)=(x^a y^b,0),       Q(c,d)=(0,x^c y^d),
```

with nonnegative exponents.  For a finite slot set `S`, define the **full
independent literal-slot module**

```text
U_S = direct sum over e in S of R*e.                     (2.1)
```

Thus every declared slot is independently variable; in particular, if a
slot occurs in the support of one preimage, that individual monomial pair
itself lies in `U_S`.  This is stronger than merely saying that a coupled
submodule has support contained in `S`.

Let `W` be any finite free `R`-submodule of `R[x,y]`.  It need not be a
coordinate-monomial module.  Suppose

```text
s in W,                 L(U_S) subset W,
N(U_S) subset W,        L o R_0 = id_W                 (2.2)
```

for an `R`-linear right inverse `R_0:W->U_S`.  These are at least the
`CLOSED-SUPPORT + UNIT-L` hypotheses on the full slot module.

### 2.2 Theorem

**Theorem.**  No finite `S`, finite free `W`, and `R_0` satisfy (2.2).

**Proof.**  Write `q_1=(0,sy)`.  In `L(R_0(s))`, the coefficient of `s` can
only come from the two slots

```text
r_1=(x^p,0),             q_1=(0,sy).
```

The derivative multiplier of `r_1` is `p`; that of `q_1` is one.  If `q_1`
were absent from `S`, the coefficient of `s` would lie in `pR`, whereas
`L(R_0(s))=s` requires coefficient one.  Hence `q_1` is a declared slot.
Full independence makes `q_1` itself an element of `U_S`, and

```text
N(q_1)=-s^2.
```

Therefore `s^2` lies in `W`.

Inductively suppose `s^k` lies in `W`.  Only

```text
r_k=(x^(108k+1),0),      q_k=(0,x^(108k)y)               (2.3)
```

can contribute to the coefficient of `s^k` in `L(R_0(s^k))`.  Put
`a_k=108k+1`.  If `q_k` is declared, then

```text
N(q_k)=-s^(k+1),
```

so `s^(k+1)` lies in `W`.  If `q_k` is absent, right-invertibility forces
`r_k` to be declared and forces its multiplier `a_k` to be a unit of `R`:
otherwise an `R`-linear combination of the available contributions could
not have coefficient one.  Full independence gives `r_k,q_1,r_k+q_1` in
`U_S`, and exact polarization gives

```text
N(r_k+q_1)-N(r_k)-N(q_1)=a_k s^(k+1).                    (2.4)
```

The left side lies in `W`.  Since `a_k` is a unit in this branch,
`s^(k+1)` lies in `W`.  This closes the induction.

The monomials `s^k=x^(108k)`, `k>=1`, are `R`-linearly independent, so a
finite free `W` cannot contain all of them.  Contradiction.  QED.

The induction is robust to cancellations inside the coupled preimages
`R_0(s^k)`: it uses only the coefficient of one residual monomial to show
that a relevant slot is present.  It isolates that slot only because (2.1)
declares all slots independently variable.  Notice also that
`a_k=108k+1` is divisible by 109 exactly when `k=1 mod 109`; at those stages
the `q_k` branch is compulsory.

### 2.3 Scope and countercontrol

No coordinate-basis assumption on `W`, marked collision, eight-slot cap, or
degree bound was used.  The conclusion excludes the naive plan “choose a
finite monomial support, let every coefficient vary, and check closure.”

It does not apply to a genuinely coupled section.  For example

```text
U_cpl = R*(x^109, (1-109)x^108 y)
```

has raw support on the two slots `P(109,0)` and `Q(108,1)`, but neither slot
is independently variable.  Its generator `u` satisfies

```text
L(u)=s,                  N(u)=-108^2 s^2.                (2.5)
```

Thus it is outside the theorem and, as a scope countercontrol, still fails
closure on `W=R*s`.  Raw support alone cannot decide the coupled problem.

## 3. No exact lift with corrections affine in `y`

The full-slot theorem makes essential coupling necessary.  The following
independent theorem closes the smallest coupled polynomial motif.

### 3.1 Theorem

**Theorem.**  There are no `a,b,c,d in R[x]` such that

```text
A=a(x)+c(x)y,            B=d(x)+b(x)y                    (3.1)
```

and `det J(F_(A,B))=1`.

**Proof.**  Direct expansion separates the determinant into its constant and
linear `y` coefficients:

```text
[y] det J(F_(A,B))
  =p ((1+pb)c'-pc b'),                                      (3.2)

[y^0] det J(F_(A,B))
  =(1+pb)(1-ps+pa')-p^2 c d'.                              (3.3)
```

If the determinant is one, (3.2) vanishes.  With `h=1+pb`, which is a
nonzero polynomial, this says

```text
h c'-c h'=0.
```

In the characteristic-zero rational function field `Q_109(x)`, the kernel
of the derivative is `Q_109`.  Hence

```text
c/h=k
```

for some constant `k in Q_109`, or `c=k h`.  Substitution in (3.3) gives

```text
(1+pb)(1-ps+pa'-p^2 k d')=1.                              (3.4)
```

Both factors in (3.4) are polynomials over `Q_109` whose product is one, so
both are nonzero constants.  It follows first that `b` is constant, then
that `c` is constant.  Since `1+pb` is a unit of `R` and `c in R`, actually
`k=c/(1+pb)` lies in `R`.

The coefficient of `x^108` in the second factor of (3.4) is

```text
-p+p^2 a_109-p^3 k d_109,                                 (3.5)
```

where `a_109,d_109 in R` are the coefficients of `x^109` in `a,d`.
After division by `p`, (3.5) is `-1 mod p`, so it cannot vanish.  The second
factor is therefore not constant, contradicting (3.4).  QED.

This theorem assumes neither marked collisions nor a degree cap.  It rules
out every exact lift in this fixed seed chart with both corrections of
`y`-degree at most one.  In particular, allowing arbitrary `x`-degree does
not close the canonical `B=x^108y` ray inside the affine-`y` motif.

## 4. Consequence for the next AS109 design

No positive closed core was found.  The exact resurrection condition is now
narrower than `CLOSED-SUPPORT + UNIT-L` alone.  A surviving proposal must:

1. specify a finite **coupled** `R`-module or gauge section, rather than the
   full coefficient module on its raw monomial support;
2. prove `N(U') subset W` for every element of that coupled module, including
   all polarizations, not merely along one proposed coefficient orbit;
3. retain an integral right inverse for `L` after imposing the coupling; and
4. allow `y`-degree at least two in the fixed point (hence in the section),
   because the entire affine-`y` family is impossible.

A finite Hamiltonian/gauge-paired block with quadratic `y`-dependence is the
smallest remaining motif type.  Whether any such block closes is open.  The
two theorems above do not license an exponent rectangle, cap widening, or an
inference from a finite Witt level.

## 5. Exact replay and provenance

The standalone replay is

```text
python3 cases/as109_closed_support_20260824/verify_no_go.py
```

It uses only the Python standard library.  A sparse polynomial engine with a
formal coefficient ring checks (1.1), the affine-`y` split (3.2)--(3.3), and
the exact obstruction (3.5).  A separate integer sparse replay checks (2.4)
for every `1<=k<=220`, including three nonunit-multiplier stages, and checks
the coupled countercontrol (2.5).  The formulas in the proofs establish the
claims for every `k` and arbitrary polynomial degrees; the finite replay is
a regression control, not an exhaustive search.

Expected top-level fields are

```text
verdict = PASS-AS109-NATURAL-NOGO
affine_y.exact_lift_affine_in_y = IMPOSSIBLE
literal_slot.full_independent_literal_slot_certificate = IMPOSSIBLE
enumeration_run = false
lift_found = false
characteristic_zero_inference = false
```

Frozen hashes at production:

| Artifact | SHA-256 |
|---|---|
| `cases/as109_closed_support_20260824/verify_no_go.py` | `01d890b7f048765565203778a038a2d31a7cc8132a7f59c15ebff2655599eb50` |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` |

The prior gate, erratum, and reviews were read as provenance and not edited.
This artifact does not alter canonical ledgers.  It gives no proof or
counterexample to JC2.
