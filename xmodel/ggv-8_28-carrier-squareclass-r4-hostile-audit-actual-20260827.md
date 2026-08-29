# Hostile audit: `8_28` carrier square-class rigidity R4

Date: 2026-08-27  
Reviewer: `actual_total_g20`  
Target: `xmodel/ideation-20260827T1349Z-fable5.md`, §3.1 and Card 1  
Target SHA-256:
`2421096121410a0895245649204815b8efee337873567cb9e277971294ae2796`

## 0. Verdict

**CORE ARITHMETIC: CONFIRMED.  RATIONAL DESCENT: CONFIRMED.  THREE SCOPE /
WORDING REPAIRS REQUIRED.**

For a formal packet already in the frozen R2 normalization over `Q`, with

```text
H=X^8-1,       F_0=H^2,       G_0=H^3,
E_0=...=E_21=0,              E_22=lambda in Q^*,
```

the formal Morse chart descends to every rational factor residue field.  On
the R2 branch `V8(c)=0`, the exact endpoint is

```text
U11(c)^2=lambda*c/36.                                 (0.1)
```

The resulting rational square-class table is exactly:

| rational factor of `H` | residue field / representative `c` | branch 2 is possible exactly when |
|---|---|---|
| `Phi1=X-1` | `Q`, `c=1` | `lambda in (Q^*)^2` |
| `Phi2=X+1` | `Q`, `c=-1` | `-lambda in (Q^*)^2` |
| `Phi4=X^2+1` | `Q(i)`, `c=i` | `lambda in 2(Q^*)^2` or `lambda in -2(Q^*)^2` |
| `Phi8=X^4+1` | `Q(zeta_8)`, `c=zeta_8` | never, for any `lambda in Q^*` |

Thus at most one of `Phi1,Phi2,Phi4` can carry branch 2, `Phi8` never can,
and branch 1 is forced on at least three of the four rational factors.  For
`lambda=1`, only `Phi1` is square-class admissible for branch 2.  On every
forced branch-1 factor,

```text
V8(c)*U14(c)=lambda*c/48.                              (0.2)
```

These statements are necessary conditions only.  They do not construct the
local coefficients from raw rows, prove a global polynomial cleanup, exclude
the `8_28` face, or constrain the same problem over `Qbar` or `C`.

Required repairs:

1. The Morse construction **does take a formal square root of a unit**.  It
   requires no residue-field extension because the unit's closed-point value
   is the already-present square `H'(c)^2` and the orientation chooses the
   root `H'(c)`.
2. The arbitrary-`lambda` table applies to the **fixed normalized formal
   chart** with endpoint `E_22=lambda`.  It is not automatically invariant
   under an unrecorded raw target/source normalization; any scalars or Kummer
   extensions used to put a general face into `F_0=H^2,G_0=H^3` must be
   carried explicitly.  The frozen reviewed R2 case `lambda=1` has no such
   ambiguity.
3. Square class is arithmetic descent metadata, derived from the coefficient
   field, factor, `lambda`, and branch.  It is not yet an independent
   complex-`G2-PSC` packet field: over `Qbar/C` every nonzero class is a
   square.  Likewise, R2's `V8=X^4+1` fixture remains a valid mixed-factor
   *typing* example; only its completion to a normalized rational
   `lambda=1` branch-2 endpoint on `Phi8` is impossible.

## 1. Frozen inputs and audit boundary

The audit rechecked the exact statements and field constructions against:

```text
66121bddbe0b004ad1b8960f896d3691c4dd3963068fbfddb6ad3ba15dda7027
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-sol-20260827.md
d40cd78f4f0afc12d09f8d1e99724de9fd5125fddc064089d6ca0870c7d777e0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-hostile-review-grok-20260827.md
0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md
b271a2958138d8e85c0a8cab068efd7bfa59227a56e5252eb27310a50fb11e24
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-hostile-review-grok-20260827.md
74c6c78e4faf527172703d5a115767562d89d9fa20868fc431dcc1f7cd258f15
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py
```

No R3 statement is needed.  No global raw-to-Morse compiler, polynomial
source automorphism, or complex-family descent theorem is assumed.

## 2. Does the Morse chart stay in the residue field?

Yes.  Let `k` have characteristic zero, let `c` be a simple root of `H`, and
put `kappa=k(c)`.  Work in `kappa[[z,t]]`, `z=X-c`.  The normalized first
coordinate satisfies

```text
F(c,0)=0,
F_X(c,0)=0,
F_XX(c,0)=2 H'(c)^2 in kappa^*.
```

The formal implicit-function theorem therefore gives a unique critical
section

```text
s(t) in t*kappa[[t]],       F_X(c+s(t),t)=0.           (2.1)
```

Every recursive coefficient uses only field operations in `kappa`, including
division by the unit `2H'(c)^2`.  Put

```text
U(t)=F(c+s(t),t).
```

Because the first derivative vanishes along the section,

```text
F-U(t)=(z-s(t))^2 Q(z,t),
Q(0,0)=H'(c)^2.                                       (2.2)
```

There is a unique Hensel square root

```text
q(z,t)^2=Q(z,t),       q(0,0)=H'(c),                  (2.3)
```

and its recursion divides only by `2H'(c)`.  Hence `q` lies in
`kappa[[z,t]]`; no quadratic extension occurs.  Set

```text
u=(z-s(t))*q(z,t).
```

Then `F=u^2+U(t)`, `u_X(c,0)=H'(c)`, and at `t=0` uniqueness gives
`q(z,0)=H(c+z)/z`, so `u=H mod t`.  Since `u_X` is a unit, formal inversion
also remains over `kappa`.  Expanding `G` in `(u,t)` therefore gives

```text
U_j(c), V_j(c), W_j(c), Q_j(c), Gamma_j(c), ... in kappa.  (2.4)
```

This construction is Galois-equivariant: conjugating `c`, all input
coefficients, and the chosen orientation conjugates the unique critical
section and unique square root.  Thus a packet defined over `Q` has a single
branch type on each irreducible rational factor of `H`.

Verdict on Fable's rationality premise: **CONFIRMED**, with the wording
repair that a formal square root is taken but is already split over the
residue field.  Card 1's proposed fallback to an unspecified quadratic twist
is unnecessary for the frozen R2 chart.

## 3. Exact carrier equation

R2 proves, over one simple-root residue field, that branch 2 satisfies

```text
(9/2)*H'(c)*U11(c)^2=lambda.                           (3.1)
```

Here the reviewed theorem has `lambda=1`; replacing the constant endpoint
`E_22=1` by `E_22=lambda` changes only the right side of the same evaluation.
Since `c^8=1`,

```text
H'(c)=8c^7=8/c.
```

Substitution into (3.1) gives

```text
(36/c)U11(c)^2=lambda,
U11(c)^2=lambda*c/36.                                  (3.2)
```

Because `36=6^2`, branch 2 is possible over `k(c)` only if `lambda*c` is a
square there.  On branch 1,

```text
6H'(c)V8(c)U14(c)=lambda
```

instead yields the exact nonzero product (0.2).

No converse is claimed: square-class admissibility supplies a scalar
`U11(c)`, but raw provenance, the other determinant channels, deck gluing,
and global polynomial realization remain open.

## 4. Independent square-class computation over `Q`

Factor

```text
X^8-1=(X-1)(X+1)(X^2+1)(X^4+1)
       =Phi1*Phi2*Phi4*Phi8.                           (4.1)
```

### 4.1 `Phi1` and `Phi2`

At `c=1`, (3.2) is soluble in `Q` exactly when `lambda` is a rational
square.  At `c=-1`, it is soluble exactly when `-lambda` is a rational
square.

### 4.2 `Phi4`

Take `c=i` and write a possible square root in `Q(i)` as `a+bi`, with
`a,b in Q`.  The equation

```text
(a+bi)^2=lambda*i
```

is equivalent to

```text
a^2=b^2,       2ab=lambda.                             (4.2)
```

Thus either `a=b` and `lambda=2a^2`, or `a=-b` and
`lambda=-2a^2`.  Conversely,

```text
(r(1+i))^2= 2r^2 i,
(r(1-i))^2=-2r^2 i.                                   (4.3)
```

This proves the two `Phi4` classes exactly.  Conjugation gives the same
answer at `c=-i`.

### 4.3 `Phi8`

Let `K=Q(zeta_8)=Q(i,sqrt(2))`, with `zeta_8^2=i`.  The extension
`K/Q(i)` is quadratic and sends `zeta_8` to `-zeta_8`, so

```text
N_{K/Q(i)}(zeta_8)=-zeta_8^2=-i.                      (4.4)
```

If `mu^2=lambda*zeta_8` for `mu in K`, taking the relative norm gives

```text
N(mu)^2=-lambda^2*i.                                  (4.5)
```

After dividing by the square `lambda^2`, this would make `-i` a square in
`Q(i)`.  It is not.  Indeed, if `(a+bi)^2=-i` with rational `a,b`, then

```text
a^2=b^2,       2ab=-1.
```

For `a=b` this says `2a^2=-1`; for `a=-b` it says `a^2=1/2`, which has no
rational solution.  Hence

```text
lambda*zeta_8 notin (Q(zeta_8)^*)^2
for every lambda in Q^*.                              (4.6)
```

This relative-norm proof independently confirms Fable's longer cyclotomic-
subfield argument and avoids any unlisted ramification case.

### 4.4 Disjointness and the complete table

The four rational square classes

```text
1, -1, 2, -2  in Q^*/(Q^*)^2                         (4.7)
```

are pairwise distinct.  Therefore the conditions for `Phi1`, `Phi2`, and
`Phi4` are mutually exclusive, proving the table in §0 and the “at most one
small factor” conclusion.

A desk exact-rational replay checked the witnesses in (4.3), the relative
norm (4.4), and the resulting table.  No floating-point or finite-field
evidence is used.

## 5. The normalized `lambda=1` case

For the frozen R2 endpoint, `lambda=1`:

- `Phi1`: branch 2 is arithmetically possible, with
  `U11(1)=+/-1/6`;
- `Phi2`: it would require a rational square root of `-1`;
- `Phi4`: class `1` is neither `2` nor `-2` modulo rational squares;
- `Phi8`: impossible by (4.6).

Thus branch 1 is forced on `Phi2*Phi4*Phi8`, and there

```text
V8*U14=lambda*X/48                                    (5.1)
```

after reduction to the product of those factor fields.  `Phi1` is only
*admissible* for branch 2; nothing here forces `V8(1)=0` or constructs the
required raw packet.

The R2 review's illustrative polynomial `V8=X^4+1` vanishes on `Phi8` and
therefore illustrates that mixed zero/nonzero factor patterns exist in the
finite etale algebra.  It did not provide `U11` or claim a complete rational
endpoint.  The corrected R4 consequence is:

> that zero pattern cannot be completed to the normalized `lambda=1`
> branch-2 carrier equation over `Q(zeta_8)`.

It is not a correction to R2 itself.

## 6. Base-field firewall: `Q` versus `Qbar` and `C`

Over an algebraically closed characteristic-zero field, every nonzero
`lambda*c` has a square root.  For example, with `lambda=1` and
`c=zeta_8`, adjoining `zeta_16` gives

```text
(zeta_16/6)^2=zeta_8/36.                               (6.1)
```

Similarly `i/6` works at `c=-1` after adjoining `i`, and `zeta_8/6` works
at `c=i`.  Thus all four branch-2 square equations are soluble over `Qbar`
and `C`.

Consequences:

1. R4 is a real pruning theorem for **Q-defined normalized packets** and,
   with the obvious changed table, for packets over a specified nonclosed
   coefficient field.
2. Failure of an exact-Q compiler caused solely by the square-class table is
   arithmetic descent failure, not evidence against a `Qbar`/complex
   `8_28` packet.
3. JC2 over `C` supplies no theorem forcing a hypothetical packet to descend
   to `Q`.  Even if existence descends to some number field, adjoining the
   finitely many square roots removes this obstruction.  Therefore R4 is not
   a family exclusion or a proof-side complex obstruction.
4. A proposed square-class packet entry is redundant if the packet already
   records the coefficient/residue field, `lambda`, factor, and actual
   carrier coefficient.  It can be useful as a derived arithmetic guard,
   but no new complex `G2-PSC` fidelity field is proved.

For a raw Q-defined Keller face not yet in the frozen monic chart, one must
also audit the scalars used to achieve `F_0=H^2,G_0=H^3` and the constant
endpoint.  A target scaling may preserve rational coefficients while
changing the leading cube; a subsequent square/cube normalization may
require a Kummer extension.  The arbitrary-`lambda` table must therefore be
attached to the normalized chart and its map, not to an untyped raw Jacobian
constant.

## 7. History and novelty audit

Targeted pre-R4 searches confirm that no earlier `8_28` artifact derives
(3.2), classifies the four rational factors by square class, or uses that
classification to forbid an R2 carrier branch.  R2 records Galois/conjugation
factor tags and the mixed `V8` zero pattern, but not arithmetic feasibility of
the `U11^2` equation.  Thus the **R4 carrier lemma and its application are
new**.

The broader claim “genuinely new square-class/Kummer mechanism” is too
strong.  The campaign has many prior Kummer square/nonsquare lanes, and, most
directly, the earlier same-day report

```text
1481d3cadc30ee024c7d4e07e746a6e15ce000a52358e589a1fdf5add3e755c1
  xmodel/ideation-20260827T0145Z-crosspollination-hostile-review-fable5.md
```

already uses the quadratic-subfield census of `Q(zeta_8)` to prove that
`5/12` is not a square there and adjoins its square root to construct an
exact characteristic-zero point.  Its algebraic follow-up

```text
b0fb7edaf262f0db64bef2de1a0ad1657251deab355d963855934c0284b6285c
  xmodel/ideation-20260827T0145Z-crosspollination-algebraic-claims-review-grok.md
```

also performs exact nonsquare/Kummer descent over `Q(i,sqrt(2))`.
Accordingly the correct novelty label is:

```text
NEW R2-CARRIER APPLICATION AND FACTOR TABLE;
KNOWN CAMPAIGN SQUARE-CLASS/KUMMER METHOD.
```

## 8. Promotion-ready corrected theorem and stop rule

The exact statement supported by this audit is:

> Let a formal R2-normalized packet be defined over `Q`, with
> `F_0=(X^8-1)^2`, `G_0=(X^8-1)^3`, lower determinant coefficients zero,
> and constant endpoint `E_22=lambda in Q^*`.  The oriented formal Morse
> chart is defined over each rational factor residue field.  If the R2
> `U11^2` carrier occurs on a factor, the factor must satisfy the table in
> §0.  Consequently `Phi8` is always branch 1, at most one other rational
> factor is branch 2, and for `lambda=1` only `Phi1` is branch-2 admissible.
> Every forced branch-1 factor satisfies `V8U14=lambda X/48`.  No existence,
> raw provenance, global polynomial lift, complex-family exclusion, or
> `G2-PSC` conclusion follows.

This is desk-scale and complete.  No AWS successor is warranted merely to
recheck the four square classes.  The only useful downstream consumer is the
raw-to-Morse compiler over an explicitly pinned nonclosed base field; over
`Qbar/C`, omit this pruning rule.

