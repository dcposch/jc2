# Hostile review — affine-Faber `A` homogeneous predecessor/direct-unit cone

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-affine-faber-a-homogeneous-direct-unit-cone-theorem-20260826.md` |
| Target SHA-256 | `c4926d0476f4df7d910b09645bf387f06292f3faaa25f2e7793b81ba2001bf71` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing valuation face | none inside the cone `(1.1)--(1.2)` with complementary-pivot dichotomy; `H>15`, `ord(a)<H/3`, `q=0`, `p=0`, `M=0`, square/more-degenerate factors, and other load slopes are identified receivers, not holes |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. No producer status line, no charged `CONFIRMED`/`PASS`/`UNIT`/`ENDPOINT` token, and no validator string is evidence |
| Method | SHA-256 of every charged pin and freeze/evidence row; independent parse of all 371 exact-`Q` monomials of `K=E*H3+H5`; exact derivatives from that support and from the inverse-Faber formulae; Singular reconstruction of the seven ordinary-Faber tails at the first quadratic face; hand polar linearization of `(3/8)N^2/Q`; Euclidean first-block / UFD factor type from the charged bridge; both directions of the `D(M)` coefficient map. Characteristic 65521 was not used as characteristic-zero algebra |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the nine files named in the review
prompt match those pins. Every freeze and evidence row of the relative-cone
artifact matches the corresponding on-disk bytes. Producer verdict
language, `PASS_A_FULL_K_MULTISUPPORT`, `PASS_RAW_K_RELATIVE_CONE_V2`,
`PASS-A-FULL-K-RELATIVE-CONE-V2`, and both charged hostile-review
`CONFIRMED` tokens were not used as characteristic-zero evidence. Exact
`Q` is the mathematical lane for the 371-term support; the F65521
exponent sequence is a software control only. No file other than this
review was written. The target, producers, shared ledgers, and
`jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On the complete characteristic-zero DVR, after finite ramification, in
the repeated-`A` affine chart on `D(E*M)`, with extracted normal scale
of valuation `h>0`, the hypotheses `v(a)>=h/3`, `q=min(v(U),v(V))>0`,
the complementary-pivot dichotomy, and `v(load),v(target)>=14h/5` for
every effective lower load and every target that can enter rows 1, 3, 4,
or 6, imply that the seven ordinary-Faber rows have no formal or Puiseux
solution. The strict range `0<q<2h/5` dies at the unloaded quadratic
face `2h+2q`, whose four displayed initial rows reconstruct from the
frozen complete tails and kill both residue charts `D(x)` and `D(y)`.
The closed range `q>=2h/5` dies because the exact 371-term polynomial
`K=E*H3+H5` has unique minimum `-E M^3 lam^3/16` of weight `3h` at the
rescaled weight vector `(3.1)`, and every coordinatewise larger
valuation in the cone strictly raises every competitor. The two halves
meet at `q=2h/5` with neither a gap nor a double-counted unsupported
face. On the delayed source ray the first square-normal block is
untied for every `0<H<=15`, forces `N \equiv m z(z^2+p)` with `p,m`
units, and the `D(M)` isomorphism sends that special fibre to the
closed point `(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0)`, hence `q>0`; the
center bound `v(a)>=H/3` is an extra hypothesis. No `K10` unit is used.
The statement is internal to this weighted affine-Faber neighbourhood
and does not close the firewalled receivers.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| homogeneous cone theorem | `c4926d0476f4df7d910b09645bf387f06292f3faaa25f2e7793b81ba2001bf71` | immutable provisional theorem (matches required pin) |
| full-`K` multisupport `RESULT.md` | `e0a64e55ea21c41ee06e635740f7b8af375ce64855638cc44109afb8b384492a` | charged (matches required pin); navigation only |
| relative-cone `RESULT.md` | `c16d31a8089dca365014a710e40d33a6e5a0b4924053439ead03f584a4e45e7b` | charged (matches required pin); navigation only |
| relative-cone `EVIDENCE.sha256` | `f7606a759e5cf6f9a52432baef1af2fb170ce04b65cbd573a96a0f17bbdc0619` | charged (matches required pin) |
| relative-cone `FREEZE.sha256` | `743742bac469af09ccb3b46b6366657fa62c4161e6b61a11361f63cbc5f2d0c8` | charged (matches required pin) |
| first-block divisibility bridge | `56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23` | charged (matches required pin) |
| first-block hostile review V2 | `85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff` | charged (matches required pin); algebra rederived, verdict ignored |
| delayed-load composition theorem | `fef0524a91c239b9086df8377e0b1270430b2fb164915eb8286bf52f9508cf32` | charged (matches required pin) |
| delayed-load composition review | `a6d434b5342a32bcefc74b78fd4526eaf1a6556a73ddcc22b970c9958d248f18` | charged (matches required pin); algebra rederived, verdict ignored |
| exact-`Q` 371-term stdout | `1fd637a6918608b488c8e30e134f9a911354f7394ea83741634e04cdc5a7606b` | freeze pin; characteristic-zero support |
| F65521 support stdout | `13f06fee7fec5eb1c5165c47db7251665a2d6658b85b9ac7f669468ae2bff5f1` | freeze pin; software control only |
| frozen ordinary-Faber tails | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete tails used to rebuild `(2.3)` |
| exponent-sequence SHA-256 | `a21e5dbbbfe7e937aa0eb2cb873047852b902b6a959f8df8f19a2b18f88dab6a` | newline-terminated exact-`Q` exponent list; matches the charged `RESULT.md` claim |

Every freeze and evidence path in the two relative-cone manifests
recomputes to the recorded digest. Characteristic-65521 coefficients
were opened only to confirm that the exponent vectors agree
byte-for-byte with exact `Q`; they are not characteristic-zero
coefficients.

---

## Attack 1 — complete 371-term support, weights `(3.1)`, `mu4:42` versus `48`

The exact-`Q` stdout contains 371 exponent vectors of length 27 in the
compiler order

```text
J, mu6, mu4, mu2, K2, K6, K10, S0, S1, R0, R1, Y, X, a, lam, M, E,
n0, n1, n2, n3, qr, qc, qp, k2, k6, k10.
```

Every raw source slot `n0,...,k10` is identically zero after
substitution. `J` and `mu6` are identically absent (0 terms). Grouping
by the 15 valuation exponents, retaining the coefficient polynomial in
the unit variables `(M,E)` over `Q`, produces 371 nonzero groups and 0
multi-member groups: no two raw monomials were merged behind an
unrecorded `E,M` factor. The F65521 exponent sequence equals the
exact-`Q` sequence; that agreement is a software control, not a
coefficient proof.

At the integer weight vector `(3.1)`

```text
a:5, lam:15, X:Y:6, S0:S1:R0:R1:12,
K10:K6:K2:mu2:mu4:42
```

(`J` and `mu6` unused because they do not occur), the 371 weights have
minimum 45, attained at exactly one group

```text
(-1/16)*lam^3*M^3*E,
```

which is the displayed monomial `(3.2)`. There is no weight-46 group.
The next weight is 47, with exactly seven groups, coefficients in
`Q[E,M]`:

```text
(-3/8)*X^2*a*lam^2*M^2
( 3/2)*Y^2*a*lam^2*E
(25/1024)*K10*a*E^7
(-9/128)*K6*a*E^5
( 1/8)*K2*a*E^3
(-1)*mu2*a*E
( 4)*mu4*a
```

Every one of these is nonzero on `D(E*M)`. Thus every term has weight
`>45` except `(3.2)`.

The mu4/mu2 support is exhaustive, not a control bit:

```text
dK/dmu4 = 4 a,                         (single term 4*mu4*a)
dK/dmu2 = 20 a^3 - a E.               (terms 20*mu2*a^3 and -mu2*a*E)
```

These are the same identities as the inverse-Faber definitions, computed
without the support table: `P4` meets `H5` through `-B P4` with `B=4a`,
so `dK/dmu4=4a`; `P2` meets `H3` through `-(B/2)P2` and `H5` through
`(-(5/16)B^3+(3/4)B E)P2`, so

```text
dK/dmu2 = E*(B/2) - (-(5/16)B^3+(3/4)B E)
        = (5/16) B^3 - (1/4) B E
        = -a E + 20 a^3.
```

The frozen relative-cone analyzer assigned `mu4:48` (and `mu6:54`,
`J:57`). Replacing `mu4` by 42 introduces the unique mu4 monomial at
weight `42+5=47` and does not create a weight-45 competitor. The same
holds for `mu2` at 42: both of its monomials have a positive power of
`a`, hence first weight 47. There is no `q`-independent competitor at
or below 45 after the lowering.

Pareto-minimal load forms in `K`, among monomials that carry exactly
one of `K2,K6,K10` and no kernel/complement, are

```text
(a exponent, lam exponent) = (1,0) and (0,1)
```

for each of the three loads. Consequently the lightest load monomials
in `K` are `v(K_i)+v(a)` and `v(K_i)+v(lam)`. At `(3.1)` those are 47
and 57. There is no load term in `K` with `(a,lam)=(0,0)` and no
kernel/complement; every `(a,lam)=(0,0)` load monomial still carries a
positive power of `X`, `R0`, or `R1`, hence weight at least 48.

The intrinsic coefficient is a polynomial identity on the central
slice, independently of grouping: after setting
`a=X=Y=R*=S*=K*=mu*=0`, the unique remaining term is `(3.2)`.

---

## Attack 2 — homogeneous rescaling after ramification

Every one of the 371 groups is a monomial in the valuation variables
times a coefficient in `Q[E,M]`. Weights are therefore linear in the
input valuations. Multiplying `(3.1)` by a positive rational `h/15`
sends the unique minimum to weight `3h` and every listed competitor to
weight `>= 47h/15 > 3h`. After the finite ramification that makes `h`
integral in the value group, this is an integer identity; the same
linear comparison holds for a `Q`-valued valuation without
re-integrality.

The closed cone is the set of valuations at or above the rescaled
corner: `v(a)>=h/3`, `q>=2h/5`, genuine complements `>=2q>=4h/5`, and
every effective load/target `>=14h/5`, with `v(lam)=h` the extracted
normal scale. The unique minimizing monomial `(3.2)` depends only on
`lam,E,M`. Raising any of `a`, `X`, `Y`, `R*`, `S*`, `K*`, `mu2`,
`mu4` therefore strictly raises every competitor and cannot create a
new equality with `(3.2)`. Explicit integer checks of the 371-term
table, all preserving unique minimum 45 at the intrinsic group:

- `v(Y)>v(X)`, `v(X)>v(Y)`, either kernel series identically zero, both
  zero (`q=infinity`);
- complements raised to 13, or all complements sent to infinity;
- `v(a)=6`;
- all loads/`mu2`/`mu4` raised to 43;
- `q=6,7,8,9,10,15,100` with complements `=2q`.

The `q=5` raw-`K` equality wall of the charged relative-cone `RESULT.md`
(four center/kernel/complement monomials tying weight 45) lies at
`q=h/3 < 2h/5` and is outside this half of the cone. It is not a
hidden face of `q>=2h/5`.

`q=infinity` is the specialization `X=Y=0`; `(3.2)` remains the unique
minimum, now among the terms that do not use a kernel variable. Center
and tangent series of order strictly larger than the chart weights are
the same coordinatewise increase. Common ramification `t=tau^e`
multiplies every weight by `e` and preserves uniqueness at grade
`3h e`.

The sentence “increasing any input valuation cannot create a new tie”
is true inside the cone relative to the extracted `h`. It is not a
licence to raise `h` while freezing absolute load numbers: that would
violate `(1.2)`, which scales with `h`. The delayed-ray family `H<15`
with loads fixed at 42 is the opposite direction (loads strictly above
`14H/5`) and remains inside the cone.

---

## Attack 3 — low-kernel initial rows, `0<q<2h/5`, equality wall

For `h>0` and `0<q<2h/5`,

```text
2h+2q < 2h+4h/5 = 14h/5 < 15h/5 = 3h.
```

The first inequality is strict precisely when `q<2h/5`. The second is
strict for every positive `h`. Thus the unloaded quadratic face
precedes every load/target of valuation `>=14h/5` and the intrinsic
cubic.

The frozen complete ordinary-Faber tails were substituted on the
unique-coordinate chart at `a=0`, loads omitted, with

```text
U = eps x + eps^2 r1,   V = eps y + eps^2 s1,
R0 = eps^2 r0,          W0 = eps^2 s0 - M eps^2 r1/2,
```

and `N` carrying the unit normal factor `lam`. Extracting the
`lam^2` piece of order `eps^2` (valuation `2h+2q`) gives, after
dividing by the unit `lam^2`, exactly `(2.3)`:

```text
G1 = -3 r1 M^2/8 + 3 s0 M/4,
G3 = -3 E r1 M^2/32 - 3 M x y/8 + 3 E s0 M/16,
G4 =  3 M^2 x^2/32 - 3 E M^2 r0/16 - 3 E y^2/16,
G6 = -3 E^2 M^2 r0/64 + 3 E^2 y^2/64.
```

The linear kernel face of weight `2h+q` vanishes in every row
(`G1,...,G4` have no `eps^1` term of weight `2h+q`; the `eps^1` terms
that do appear in `G5,G6,G7` are `lam^3` times a kernel residue, hence
weight `3h+q > 2h+2q`). So the pairing `S0 = M U/2` has already
cancelled the polar linear kernel.

The `lam^3` pieces that share the same `eps`-degree as `(2.3)` have
weight `3h+2q` and are not part of the initial form. In particular
`G3` contains the cubic `-lam^3 M^3/16` as an `eps^0` term of weight
`3h`, strictly later than `2h+2q`.

Combinations, as polynomials, not as slogans:

```text
G3 - (E/4) G1 = - (3/8) M x y,
G6 = (3/64) E^2 (y^2 - M^2 r0).
```

On `D(M)`, `x y = 0`. On `D(E)`, `G6=0` gives `r0 M^2 = y^2`.

- `D(x)`: `y=r0=0`, then `G4 = 3 M^2 x^2/32`, a unit times `x^2`.
- `D(y)`: `x=0` and `r0 = y^2/M^2`, then
  `G4 = -3 E y^2/16 - 3 E y^2/16 = -3 E y^2/8`, a unit times `y^2`.

Unequal orders: if `v(U)<v(V)` the order-`q` residue of `V` is zero,
so one is already on `D(x)`; `G6` forces the order-`2q` residue of
`r0` to vanish and `G4` remains a unit times `x^2`. The symmetric case
is `D(y)`. A vanishing kernel series is the same axis.

`G2` also lives at grade `2h+2q`, namely
`(3/8) lam^2 (y^2 - M^2 r0)`, and vanishes given `G6`. `G5` and `G7`
likewise have `lam^2` content at that grade. The theorem's word
“complete” for the displayed four rows is therefore slightly loose —
all seven ordinary rows have that grade — but the extra three cannot
cancel a unit in `G4`. Four rows already kill every residue chart. No
repair.

Center contamination: substituting a free order-zero `a` into the same
tails produces extra monomials `a y^2 lam^2`, `a r0 lam^2`,
`a^2 r1 lam^2`, and cubic-center terms `a lam^3 M^3`. With the chart
weight `v(a)>=h/3` every such monomial has weight at least
`2h+2q+h/3` or `3h+h/3`, strictly later than `2h+2q`. `(E,M)`-tangent
jets have positive valuation on the unit locus and likewise raise the
face. There is no center, load, target, cubic, or connection monomial
in the initial form `(2.3)`.

At the equality `q=2h/5` the quadratic face meets the load bound:
`2h+2q=14h/5`. The low-kernel argument is stated as the strict range
and is not used there. The high-kernel 371-term unit of Attack 2
applies at `q>=2h/5`, including equality: kernel squares cancel in
`K=E*H3+H5` (the weight-42 pair `-(3/8) E lam^2 M X Y` from `E H3`
against `+(3/8) E lam^2 M X Y` from `H5`), and the unique remaining
minimum is the cubic of weight `3h`. Loads in `K` first appear at
`14h/5+h/3=47h/15>3h`. There is neither a gap nor a double-counted
unsupported face.

---

## Attack 4 — load/target bound `14h/5`; `mu6`, `J`, omitted targets

The bound `(1.2)` is a hypothesis of the internal theorem, not a
conclusion of the 371-term table. It is necessary for the low-kernel
half, and it is sharp.

The frozen ordinary tails contain no pure-load monomial in rows 1, 3,
5, or 7. They do contain load times a power of `2 qp` in rows 2, 4,
and 6. At the closed point `qp=E` is a unit, so those monomials have
weight exactly `v(K_i)`. Rows 4 and 6 are in the displayed four-row
block. A naked load in `G4` or `G6` at valuation `<14h/5` would tie or
beat `2h+2q` as `q` approaches `2h/5`. The bound is therefore the
correct threshold, not a conservative estimate taken from `K`.

`mu6` and `J` cancel identically from `K` (`dK/dmu6=dK/dJ=0`, and
neither variable occurs in the 371 terms). That cancellation is
irrelevant to individual rows:

- `P6 = source(T6) - mu6`, so `mu6` reenters `G6` as a naked target of
  weight `v(mu6)`. Hypothesis `(1.2)` names every target that can
  enter rows 1, 3, 4, or 6, and therefore includes `mu6`. Under that
  bound `v(mu6)>=14h/5>2h+2q` in the strict low-kernel range, so it
  does not tie `(2.3)`.
- `J` is subtracted from `P7` only. It cannot enter `G1,G3,G4,G6`.

`mu4` is subtracted from `P4` and is likewise covered by `(1.2)`.
`mu2` is subtracted from `P2` only, so it cannot tie the four-row
block; on the delayed ray it anyway starts at 42, which is the same
number as the three loads.

A target omitted from the four-row block therefore cannot rescue a
solution that those four rows already kill. The smallest missing
weight inside the hypotheses is none. The lightest load/target
contribution that the hypotheses permit to the four-row block is
`14h/5`, strictly after `2h+2q` for `q<2h/5`, and strictly after the
cubic in `K` for `q>=2h/5` once the extra factor of `a` or `lam` in
every `K`-load monomial is counted.

On the delayed ray the later targets sit at 48, 54, and 57, all
`>=48>42>=14H/5` for `H<=15`. They cannot tie either half.

---

## Attack 5 — complementary pivot, rescaling, complete-DVR absorption

The theorem imposes the dichotomy rather than treating `v(R),v(S)>=2q`
as a free hypothesis. The linearization is algebraic and independent
of `h`.

On the principal double root `Q=A^2 D`, `N=M A D`, one has
`N^2/Q = M^2 D`, holomorphic. In unique coordinates the complementary
increments are `dQ=R0`, `dN=W0`. Then

```text
2 N dN/Q - N^2 dQ/Q^2
  = 2 M W0 / A - M^2 R0 / A^2.
```

Times `3/8`, the polar part is
`(3/4) M W0 A^{-1} - (3/8) M^2 R0 A^{-2}`. On `D(M)` a leading
complementary jet is a unit coefficient of `A^{-2}` or `A^{-1}`, or
else `R0=W0=0` at that order. The first ordinary row reconstructed in
Attack 3 is exactly the holomorphic multiple of this polar:

```text
G1 = (3/4) M lam^2 W0 = (3/4) M lam^2 (s0 - M r1/2).
```

Valuations: the polar face is `2h+r` with `r=min(v(R0),v(W0))`; the
kernel square is `2h+2q`. If `r<2q` the polar is strictly earlier and
a unit leading coefficient on a complete DVR kills the arc. If the arc
survives, `r>=2q`. Kernel-complement cross terms then have valuation
`q+r>=3q>2q` and complement squares have valuation `2r>=4q>2q`, using
`q>0` from `(1.1)`.

This comparison is homogeneous in `h` and in the value group. Finite
ramification making `q` integral reduces the value group to `Z`; a
complete DVR then has a leading coefficient in the residue field. No
infinite absorption is required: unique coordinates `(U,V,R0,W0)`
already exist as regular functions on `D(M)`, and the dichotomy is a
statement about those valuations on the solution locus. Extra
`(R1,S1)` are a splitting; existence of some splitting with
`v(R1),v(S1)>=2q` is `R1=S1=0`. The 371-term table treats the four
weighted complements as independent symbols of weight `>=2q`; setting
any of them higher is Attack 2.

The earlier-polar branch kills the arc, so it is not a missing face of
the cone. The surviving branch is exactly the complement bound used in
`(3.1)`.

---

## Attack 6 — delayed-source corollary

Write `C=Q^2+Delta` with `ord_sigma(Delta)=H`, and assume the special
fibre `Q \equiv z^2(z^2+p)` with `p` a unit. This is the coprime
squarefree type `Q=A^2 D` of the charged first-block theorem, with
`A=z`, `D=z^2+p`, `E=p\neq 0`, and `(4a)^2-4E \equiv -4p \neq 0`.

The unloaded first square-normal block is the `(3/8) N^2/Q` summand at
grade `2H`. For every `0<H<=15` one has `2H<=30<42`, so no delayed
load or target occupies that grade. The charged bridge then gives the
equivalences: vanishing of the first four (hence first seven) ordinary
rows at this untied grade if and only if `Q|N^2` if and only if
`N=M A D`. Thus

```text
Delta / sigma^H  \equiv  m z (z^2+p)  mod sigma,
```

with `m` a unit. This is the factor conclusion the charge writes as
`N0=m*z*(z^2+p)`.

The maps `(2.1)` and `(2.3)` of the charged composition theorem are
inverse regular maps on `D(M)`. Numeric round-trip over `Q` on a
generic seven-tuple recovers the input. On the special fibre
`Q=z^4+p z^2`, `N=m z^3 + m p z` they return exactly

```text
(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0).
```

What is proved, versus what is hypothesized:

- `p` a unit and `m` a unit: proved by the factor type plus the
  first-block kernel, given the displayed special fibre.
- `q>0`: proved, because the unique coordinates vanish at the closed
  point, so every DVR in the formal neighbourhood has
  `min(v(U),v(V))>0` or `q=infinity`.
- `v(a)>=H/3`: not proved by the first block. The special fibre only
  gives `a\equiv 0 mod sigma`, i.e. `v(a)>=1`. The bound `v(a)>=H/3`
  is the explicit center hypothesis `(4.2)`. At `H=15` it is `v(a)>=5`,
  strictly stronger than `v(a)>=1`. The receiver `ord(a)<H/3` is the
  earlier moving-center face, and at `H=15` the first raw center/load
  equality is `v(a)+42=45`, i.e. `ord(a)=3<5`.

The extracted normal scale is `h=H`. The delayed loads and `mu2` start
at 42. The comparison

```text
42 >= 14 H/5
```

is equivalent to `H<=15`, with equality exactly at `H=15` and a strict
inequality for every `0<H<15`. Later targets 48, 54, 57 all exceed 42.
Thus `(1.2)` holds on the ray, and the internal theorem excludes the
arc. Every `H<15` is the same cone with loads strictly above the
vertex. After ramification `sigma=tau^e` the inequalities scale by
`e` and remain valid for positive rational `H<=15`.

---

## Attack 7 — claimed inclusion of `K10=0`

The older composition theorem localized at `D(p*m*K10)` and retained
`K10` as a chart unit. Identifiable uses of that unit, none of which
survive in the present argument:

1. The named open `D(p*m*K10)` in the composition theorem, §1 and §7.
2. The loaded-kernel Groebner charts `satu*p*m*kk*x6-1` (and the `y`
   twin), which invert `K10`.
3. The sentence that `K10` “is retained and a unit on the named source
   chart”, even while admitting that the cubic coefficient of `K` is
   independent of its value.

The present theorem works on `D(E*M)`, not `D(K10)`. The 371-term
polynomial `K` has unique minimum `(3.2)`, which does not contain
`K10`. Setting `K10=0` is a specialization that deletes 238 groups,
all of weight `>=47` at `(3.1)`, and leaves the unique minimum
untouched. If `K10` is a non-unit of valuation `>=14h/5`, the same
weight bound applies. In the low-kernel half, `K10` is one of the
three effective loads; under `(1.2)` it cannot enter `(2.3)`. The
displayed rows, the polar linearization, the first-block bridge, and
the `D(M)` isomorphism never invert `K10`.

If all three loads vanish, the effective-load valuation is infinity,
which still satisfies `(1.2)`, and the cubic unit remains. The
inclusion `K10=0` is therefore literal when the remaining effective
loads obey the bound, and is not a silent reuse of the older chart
open.

---

## Attack 8 — firewalls

- `H>15`: `42 < 14H/5`, so the delayed effective load lies below the
  homogeneous vertex. The first new boundary is a mixed-load /
  graph-relative face. Not covered.
- `ord(a)<H/3`: earlier moving-center face. At `H=15` the raw
  center/load equality `v(a)+42=45` is `ord(a)=3`, which the chart
  weight `v(a)>=5` excludes. Affine-graph cancellation of that wall
  is not performed here.
- `q=0`: complementary first-normal open, squarefree/generic affine
  stratum, or square family. Hypothesis `(1.1)` excludes it.
- `p=0` (`E=0`): `D` is not squarefree. The factor classifier routes
  it; every unit in `(2.3)` and `(3.2)` that uses `E` would fail.
- `m=0` / reset: `D(M)` fails, unique coordinates `a=n2/M` are not
  regular, and `G4`'s `x^2` coefficient uses `M^2`.
- Square, squarefree, triple-root, quadruple-root, and other
  factor-degenerate special fibres: the first-block theorem routes
  them to separate receivers. The corollary assumes the coprime
  repeated-`A` type.
- Other load slopes: `(1.2)` is a lower bound. A lighter affine load
  graph can beat `3h` in `K` (Pareto forms `(1,0)` and `(0,1)`), and
  the charged relative-cone `RESULT.md` correctly refuses to infer
  cancellation of those from the support table alone.
- Total-Rees / saturation / base change: the source corollary is
  arcwise on the delayed ray. No atlas, no overlap from the original
  octic/load source onto the affine-Faber chart.
- Terminal / Taylor, order two, `(8,12)`, maximum twelve, JC2: not
  closed. Filenames that contain those phrases are campaign labels.

The theorem states these refusals. They were enforced rather than
treated as extra theorems.

---

## Exact proof scope

Work over a complete characteristic-zero valued field, after finite
ramification, in the repeated-`A` affine coefficient chart on `D(E*M)`

```text
Q = A^2 (A^2+4 a A+E) + U A + R0,
N = M A (A^2+4 a A+E) + V A + M U/2 + W0.
```

Let `h=v(lam)>0` be the extracted normal scale. Assume `v(a)>=h/3`,
`q=min(v(U),v(V))>0`, the complementary-pivot dichotomy of Attack 5,
and `(1.2)`. Then the seven ordinary-Faber rows have no formal or
Puiseux solution on this weighted formal neighbourhood:

1. `0<q<2h/5` dies at the unloaded quadratic face of grade `2h+2q` by
   the initial rows `(2.3)` on `D(E*M)`, including unequal orders and
   a vanishing kernel series;
2. `q>=2h/5`, including equality, unequal and ramified orders, and
   `q=infinity`, dies because `K=E*H3+H5` has unique leading monomial
   `-E M^3 lam^3/16` of weight `3h` on `D(E*M)`.

On the delayed ray `k10=Lambda^{12} K10`, `k6=Lambda^8 K6`,
`k2=Lambda^4 K2`, `Lambda=sigma^3`, for every `0<H<=15` with special
fibre `Q\equiv z^2(z^2+p)` and explicit center hypothesis
`v(a)>=H/3`, the first square-normal block is untied, the leading
normal is `m z(z^2+p)` with `p,m` units, the `D(M)` closed point has
`q>0`, and `42>=14H/5` supplies `(1.2)`. The internal theorem
excludes the arc. `K10=0` is included.

This is not a two-sided source-to-chart overlap, not a total-Rees
atlas, and not a theorem on the firewalled receivers of Attack 8.

CONFIRMED
