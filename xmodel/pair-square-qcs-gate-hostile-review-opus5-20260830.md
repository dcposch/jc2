# Hostile review: `PAIR-SQUARE-QCS/v1` curve/augmentation gate

Reviewer: Opus 5, different-model hostile lane
Date: 2026-08-30 UTC
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`
Lifecycle: `INDEPENDENT HOSTILE REVIEW / CURVE LEMMAS CONFIRMED / OPEN RE-TYPED`

Reviewed in full:

```text
c02c11732defca176da0ce63f71017eb497d1cf56f213a6fa2d6b6d9571f6bfa
  xmodel/pair-square-qcs-gate-sol56-20260830.md
  body 14967 bytes / 06669e22077e4b784b0490d4150ff9aa1a54900087d37d8135bf44d0635bc52a
```

Both hashes recomputed independently and match byte-exactly (full file 15300
bytes; exactly one standalone `<!-- BODY-END -->` line at line 434; body =
bytes 0..14966 inclusive of that line's terminating newline).

No heavy CAS or Singular was used.  `jc2-lean` was not inspected, listed,
searched, stat'ed, built, modified, or controlled.  No canonical file, script,
or reviewed input was edited.  All arithmetic below is desk algebra plus small
exact-rational rank computations over `Q`.

## 0. Verdict table

| # | Charged item | Verdict |
|---|---|---|
| 1 | Custody, hashes, seal, residual-Cartier formulation | `CONFIRMED` (one labelling nit) |
| 2 | Local contact `e-1`, RH length, tame coordinates, hidden multiplicity | `CONFIRM_WITH_CORRECTIONS` |
| 3 | Keller specialization, affine unramifiedness, pole length, `b_i` identification | `CONFIRM_WITH_CORRECTIONS` |
| 4 | Separation of `d-s`, `sum d_i(b_i-1)`, `sum b_i(d_i-1)`, `sum b_i` | `CONFIRMED` (one overstatement) |
| 5 | Augmentation representation and the `B`-existence equivalence | `CONFIRMED` |
| 6 | Is the report too pessimistic?  Can `B` be constructed? | `CONFIRMED` — and strengthened to two obstruction theorems |
| 7 | Degree-six passport and block-overlap controls | `CONFIRMED` |
| 8 | Sharpness of `OPEN(BASELINE-TO-POLE MAP BEFORE INJECTIVITY)` | `CONFIRM_WITH_CORRECTIONS` — do not stop, do not advance, re-type |

Headline: the report's exact curve and representation lemmas all survive a
hostile recomputation, and its central logical finding — that an abstract
transverse `B` is *equivalent to* QCS rather than evidence for it — is correct
and is the most valuable output of the packet.  Three corrections are needed,
all at the successor-typing layer, not in the mathematics.

## Typing register used throughout

```text
actual map            F=(f,g) polynomial Keller pair       -- ABSENT from this packet
curve cover           h=g|Cbar : Cbar -> P1, degree d      -- present, generic-fibre scope
formal quotient packet {U_i, phi_i=(P_i,Q_i), d_i, b_i}    -- imported, flag-indexed
flag                  index i (proper critical-value flag)
place                 physical end of the generic fibre; s poles, n finite-value
sheet                 element of Omega, |Omega|=d, fibre of h over a regular value
series                local branch expansion (e.g. t-z = c*s^5+O(s^10))
```

No identification among these is made below except where explicitly proved.
This review asserts no exit price, so it emits no `charge_basis` line.

## 1. Custody, seal, and dependency charge — `CONFIRMED`

Seal recomputation:

```text
full  15300 bytes  c02c11732defca176da0ce63f71017eb497d1cf56f213a6fa2d6b6d9571f6bfa
body  14967 bytes  06669e22077e4b784b0490d4150ff9aa1a54900087d37d8135bf44d0635bc52a
BODY-END standalone occurrences: 1 (line 434); seal block lies outside body
```

Both match the filed seal and the tasking. The body definition in the seal
("every byte through the unique standalone `<!-- BODY-END -->` line, including
its terminating newline") is the one that reproduces `14967`; no alternative
reading does.

All four section-1 dependencies charge clean.  Each named SHA-256 is the
**full-file** hash, each file is tracked at the frozen basis, and each
worktree copy is byte-identical to its committed blob:

```text
72aa958a...d297  ideation-20260829T2254Z-sol56-alt.md                          28534 B  tracked@basis SAME
cee4e1f8...b936  pcb-generic-collision-surplus-coordinator-integration-...md    7426 B  tracked@basis SAME
41209192...813f  pcb-generic-collision-surplus-sol56-20260829.md               15376 B  tracked@basis SAME
8efa07d8...6bae  qcs-repaired-control-braid-equivariance-audit-sol56-...md     13771 B  tracked@basis SAME
```

Dependency seals are internally self-consistent, and the integration's
cross-citation of the producer body hash verifies:

```text
integration  body 7094 B   85c279638f2d1320...   (matches its own seal)
producer     body 15043 B  a2cf302ad66c0198...   (matches the integration's citation)
audit        body 13438 B  bca3c47066e65c21...   (not cited by the reviewed report)
```

**Nit (not a defect).** The two labelled hashes are marked "full SHA-256";
the two control hashes at report lines 73--77 carry no type label.  They are
in fact full-file hashes, but under the campaign's hash convention the type
should be stated.  Also unstated: the integration's own frozen basis is
`31777ce9...`, not `0d7544eb`.  Neither affects any conclusion.

The report's assertion that it made no canonical or formalization-tree edit is
consistent with the worktree: `jc2-lean` and `pilot-local.log` were already
modified before this lane and are untouched by it.

### 1b. Residual-Cartier formulation — `CONFIRMED`

`Y = (h x h)^{-1}(Delta_{P1})` is a genuine Cartier divisor on the smooth
surface `S = Cbar x Cbar` (pullback of the type-`(1,1)` divisor `Delta_{P1}`
under a finite surjection), hence pure of codimension one with no embedded
components.  In characteristic zero `h` is separable, so `Delta` occurs in `Y`
with generic multiplicity one and `R := Y - Delta` is a well-defined effective
Cartier divisor not containing `Delta`.  The report's local recipe ("divide the
equation of `Y` by the equation of `Delta`") is the correct definition.

The report's distinction between the residual *before* normalization and its
normalized pullback/pushforward zero-cycle is drawn correctly and is the right
qualification: `Rtilde` is not a divisor in `S`, so `Delta . Rtilde` is
undefined, and one must instead pull back the Cartier divisor `Delta` along
`nu : Rtilde -> R` and push forward.  Since `nu` is finite and birational,
`deg nu^*(O_S(Delta)|_R) = deg(O_S(Delta)|_R)`, so the two lengths agree — the
report's `e-1` on both sides is consistent, not a coincidence.

## 2. Local contact, Riemann--Hurwitz length, and hidden multiplicity — `CONFIRM_WITH_CORRECTIONS`

**2a. Tame coordinates.** `CONFIRMED`.  At a point `p` with `e_p = e`, both
factors of the fibre square are the *same* cover at the *same* point, so one
may choose one uniformizer `u` at `p` with `h = u^e` exactly in the formal
completion (extract the `e`-th root of the unit; legitimate in characteristic
zero) and copy it to the second factor as `v`.  The displayed model
`t = u^e, t = v^e` is therefore not an assumption but a normalization, and it
is the correct one.  No tameness is being smuggled: characteristic zero makes
every ramification tame, and `e` invertible is exactly what the next step uses.

**2b. Local contact length `e-1`.** `CONFIRMED`.

```text
(u^e-v^e)/(u-v)  restricted to u=v  =  sum_{k=0}^{e-1} u^k v^{e-1-k} |_{u=v} = e*u^{e-1},
O_Delta,p / (e*u^{e-1}) = k[[u]]/(u^{e-1}),   length e-1.
```

`e` is a unit, so the length is exactly `e-1`, and `0` at unramified points.
`(2.1)` `Delta . R = Ram(h)` follows as zero-cycles on `Delta ~= Cbar`.

**2c. Global length `(2.2)`.** `CONFIRMED`, and I verify it by a second,
independent route the report does not use — pure intersection theory rather
than Riemann--Hurwitz:

```text
Delta . Y   = deg (h,h)^*O(Delta_{P1})|_Delta = deg h^*O(1)^{(x)2} = 2d,
Delta . Delta = deg N_{Delta/S} = deg T_Cbar = 2-2G,
Delta . R   = Delta.Y - Delta.Delta = 2d-(2-2G) = 2G-2+2d.
```

This agrees with the report's `2 genus(Cbar)-2+2d`.  Since the report derives
`(2.2)` from Riemann--Hurwitz and I derive it from `Delta^2` and the projection
formula, `(2.2)` is doubly certified.

**2d. Normalized model.** `CONFIRMED`.  The factorization
`(u^e-v^e)/(u-v) = prod_{zeta^e=1, zeta!=1}(u-zeta*v)` is correct; on the branch
`u = zeta*v` the equation `u-v` becomes `(zeta-1)v`, order exactly one.  So
`nu^*Delta` is `e-1` distinct reduced points with pushforward length `e-1`,
while the unnormalized `Delta cap R` is the single non-reduced point
`k[[u]]/(u^{e-1})`.  Both have length `e-1`; the report's Section 7.1 restates
this correctly.  For `e >= 3` the residual `R` is genuinely singular at the
diagonal (an ordinary `(e-1)`-fold point), and the report does not pretend
otherwise.

**CORRECTION 2e (hidden multiplicity, the charged question).** The report
proves generic multiplicity one only for `Delta`.  It then asserts (line 137)
that "`R` is the closure of the off-diagonal fibre square", which as a *cycle*
identity additionally requires that no off-diagonal component of `Y` be
non-reduced.  That is true and cheap, but unstated: at the generic point of any
component, `Y` is `Spec` of `K(Cbar) (x)_{K(P1)} K(Cbar)`, which is a finite
product of fields because the extension is separable, hence reduced.  Therefore
`R` carries no hidden component multiplicity and the cycle identity holds.  Add
this one sentence.  Nothing downstream changes: `(2.1)` is computed locally and
is correct regardless, and the `d-s` and `sum d_i(b_i-1)` splittings below are
independently cross-checked in Section 7.

**Not a defect but worth pinning:** `Delta . R` is an intersection of a divisor
with a divisor on a surface, i.e. a zero-cycle — a count of *places with
multiplicity*, not of sheets or of series.  The report never blurs this.

## 3. Keller specialization and pole length — `CONFIRM_WITH_CORRECTIONS`

**3a. `dg(T)=1` and no affine ramification.** `CONFIRMED`, and the argument is
exactly right.  With `Jac(f,g)=f_x g_y - f_y g_x = 1`:

```text
df wedge dg = Jac * dx wedge dy != 0   =>  df != 0 everywhere  =>  every affine fibre smooth,
T=(-f_y,f_x):   df(T) = -f_x f_y + f_y f_x = 0    (T is tangent to the fibre),
                T != 0                              (since df != 0),
                dg(T) = f_x g_y - f_y g_x = 1 != 0.
```

A nowhere-zero tangent field on which `dg` is identically `1` gives
`d(g|fibre) != 0` at every affine point, so `h` is unramified on the affine
part.  All of `Ram(h)` sits on `Cbar \ C`.  `CONFIRMED`.

**3b. Pole length `d-s`.** `CONFIRMED`.  `g` is a polynomial, so `h^{-1}(infty)`
is exactly the set of pole places; `sum_j e_j = d` is the degree of the fibre
over `infty`; the local calculation of 2b in the coordinate `1/g` gives
`length Ram_infty(h) = sum_j (e_j-1) = d-s`.

The report's own observation that this uses **no** Keller and **no** `A2` origin
is correct and important: `sum(e_j-1)=d-s` holds for every finite cover of `P1`.
The Keller input is used only to force `Ram(h)` onto the boundary.  Section 7
below turns this into a decisive negative control.

**3c. `b_i` = generic finite-end local degree.** `CONFIRMED as faithful`, and I
charged it against the producer rather than accepting it.  The producer defines
the cluster weight at a generic root as the local `g`-degree, i.e. the order of
vanishing of `g - g(end)` in the boundary parameter — in its own germ,
`t - z = c*s^5 + O(s^10)` gives "local `g`-degree five" with `b = 5`.  That is
verbatim the ramification index of `h` at that place over a finite value.  So
the report's `(4.1)` is sourced from the producer's definition, not assumed.

**CORRECTION 3d (two unstated identifications).** The report writes `d` for
`deg h` in Section 0/2/3 and then, from Section 4 on, feeds `d` into the
promoted package where `d = td(f,g)`.  It also writes `s` for
`#h^{-1}(infty)` and feeds it into the promoted `s = #physical pole ends`.  Both
identifications are true, but neither is stated:

```text
deg h = td(f,g):  for generic (a,b), #F^{-1}(a,b) = #{p in f^{-1}(a) : g(p)=b},
                  and by 3a g|fibre is unramified, so preimages are counted
                  without multiplicity and equal deg(h).  Requires generic-fibre
                  connectedness (otherwise deg h is a per-component number).
s (cover)  = s (places):  h^{-1}(infty) is exactly the pole-end set, since g is
                  a polynomial and hence finite on the affine part.
```

These are precisely the kind of cover-degree / place-count identifications the
guardrail asks to be declared rather than inferred.  Declare both.

**CORRECTION 3e (dropped connectedness rider).** The promoted integration
explicitly carries the rider "without connectedness, replace the Euler formula
by `chi_gen = 2c-2G-s-n`; the corresponding expression shifts by `2(c-1)`", with
generic connectedness supplied by the primitivity input.  The report's Section 2
says "smooth *connected* projective curve", but Sections 3--4 use `G`, `chi_gen`
and `2G-2+2d` without restating the rider.  Restate it.

## 4. The four separated quantities — `CONFIRMED`

This is the item most exposed to a flag/place/series conflation, and the report
handles it correctly.  I recompute all four and their relations.

```text
pole diagonal contact            d - s                    (places over infty)
finite-end diagonal contact      sum_i d_i (b_i - 1)      (places over finite values)
quotient collision capacity      sum_i b_i (d_i - 1)      (ramification of the P_i)
one baseline per quotient line   sum_i b_i                (one term per FLAG)
```

The two middle expressions are the classic trap; they differ by

```text
sum_i d_i(b_i-1) - sum_i b_i(d_i-1) = sum_i b_i - sum_i d_i = sum_i b_i - n,
```

which is nonzero in general.  The report keeps them apart explicitly.

**`(4.2)` recomputed.** From `(2.2) = (3.1) + (4.1)`:

```text
(d-s) + sum_i d_i(b_i-1) = 2G-2+2d
=> sum_i d_i b_i = 2G-2+d+s+n = d - (2-2G-s-n) = d - chi_gen.
```

This is exactly the producer's `(2.2)`, `d - chi_gen = sum_i d_i b_i`.  Verified.

**Characterization of `sum_i b_i(d_i-1)`.** The report says it "records
ramification of the parameter maps `P_i` as `f` varies, not ramification of `g`
on one fixed generic fibre".  `CONFIRMED` by direct computation: for a degree-`d_i`
polynomial `P_i : A1 -> A1`,

```text
sum_{a in A1} (d_i - q_i(a)) = deg Ram(P_i) = d_i - 1,
=> sum_a sum_i b_i (d_i - q_i(a)) = sum_i b_i (d_i - 1),
```

and the producer independently names this "the finite ramification divisor of
`P_i : A1 -> A1`".  So the fourth quantity lives on the *base* of the quotient
family, the second on *one fixed fibre*.  Distinct objects.  `CONFIRMED`.

**`(4.3)`** `Xi = d - s - sum_i b_i = length Ram_infty(h) - sum_i b_i` is a
correct rewriting of the promoted `Xi`.  `CONFIRMED`.

**OVERSTATEMENT 4f.** The report calls `(4.2)` an *independent* recovery of the
promoted deficit identity.  It is a genuine and welcome cross-check — the
Riemann--Hurwitz/ramification-divisor route differs from the producer's
Euler--Fubini pushforward route — but the two share the load-bearing input
`b_i = generic finite-end local degree` (3c).  Given `(2.2)` and `(3.1)`, the
report's `(4.1)` and the promoted identity are *equivalent*, so `(4.1)` cannot be
both an input and an independent confirmation.  Downgrade "independently
recovers" to "cross-checks against a second derivation sharing the `b_i`
definition".  The report's own conclusion — "It supplies no inequality" — is
correct and unaffected.

## 5. Augmentation representation and the `B` equivalence — `CONFIRMED`

Every dimension claim in Section 5 is correct.  I verified each symbolically and
then numerically over `Q` on the degree-six control.

```text
dim E = d,   dim V = d-1
E^sigma = {constant on each pole cycle},  dim = s     [# CYCLES, i.e. # pole PLACES]
V^sigma = E^sigma/Q*1,                    dim = s-1
W_infty = im(sigma-1) = {coordinate sum zero on every pole cycle}, dim = sum_j(e_j-1) = d-s
V = V^sigma (+) W_infty                   (d-1) = (s-1) + (d-s)   OK
```

Three points the report gets right and which a careless version would get wrong:

- `V^sigma = E^sigma/Q*1` needs exactness of invariants.  The report cites
  characteristic zero; the precise reason is that `<sigma>` is finite and
  `H^1(<sigma>, Q) = 0`, so `0 -> Q*1 -> E^sigma -> V^sigma -> 0`.  Correct.
- `W_infty` is computed in `E` but used in `V`.  This is legitimate because
  `1` has coordinate sum `e_j != 0` on each cycle, so `1 not in im(sigma-1)` and
  `E -> V` embeds `im(sigma-1|_E)` isomorphically.  Verified numerically:
  `dim im(sigma-1) = 4`, `1 not in im(sigma-1)`, image in `V` still `4`.
- `(5.3)` is Maschke/averaging (the "standard permutation pairing" also works).
  Correct either way.

**`(5.4)` — the central finding.** `CONFIRMED` exactly:

```text
B intersect V^sigma = 0  =>  m + (s-1) <= d-1  <=>  m <= d-s,
m <= d-s                  =>  any m-dim subspace of W_infty is transverse.
=> (exists B of dim m transverse to V^sigma)  <=>  sum_i b_i <= d-s  <=>  QCS.
```

The degenerate case is also fine: if `sum_i b_i > d-1` no `m`-dimensional
subspace of `V` exists at all, and both sides are false.

This is the report's strongest output, and it is right: *positing* an abstract
transverse `B` is logically identical to positing QCS.  Any successor packet
that "constructs `B`" by dimension count alone has proved nothing.  Naming `B`
canonical strictly *adds* a descent burden on top of the injectivity burden, as
the report says.  `CONFIRMED`.

## 6. Is the report too pessimistic?  — `CONFIRMED`, and strengthened

I attempted to construct the canonical sheet-labelled `B` the tasking asks for,
from normalized off-diagonal branches, local inertia, and braid descent.  All
attempts fail, and two of the failures are theorems rather than difficulties.
The report is **not** too pessimistic; if anything Section 6 understates its own
case.

**Attempted constructions, and why each dies.**

```text
A. moving spaces of all finite ends, (+)_{i,z} im(tau_{i,z}-1)
     nominal rank sum_i d_i(b_i-1) != sum_i b_i          -- wrong rank, and see N3
B. one end per line, B = sum_i Q[S_i]
     not canonical; not stable under the P_i root braid   -- report defect (1)
C. symmetrize over all d_i roots
     rank blows up to <= sum_i d_i b_i                    -- report defect (2)
D. full blocks Q[S], projected to W_infty                 -- killed outright by N2
```

**N2 (new, exact).  Constant-on-support obstruction.**  For any nonempty
`S subset Omega`, with `C_1..C_s` the pole cycles,

```text
[1_S] in W_infty   <=>   |S cap C_j| = |S| * e_j / d   for every j.
```

*Proof.* `[1_S] in W_infty` iff `1_S - lambda*1 in im(sigma-1|_E)` for some
`lambda`, iff the coordinate sum on each cycle vanishes, iff
`|S cap C_j| = lambda e_j` for all `j`.  Summing over `j` gives
`|S| = lambda d`.  Two lines.

I verified this against brute-force linear algebra over `Q` on 28408
(cover, support) pairs from 300 random pole-cycle structures with `4 <= d <= 8`:
**0 mismatches**.

Consequence: the "project the full block `Q[S]`" repair does not merely *risk*
acquiring a `V^sigma` component — it acquires one unless an exact integrality
and proportionality condition holds.  On the filed degree-six control I
enumerated all `2^6 - 2 = 62` proper nonempty supports: **not one** satisfies the
criterion.  For the relevant `b = 5` block it would need
`|S cap C_1| = 5 * 5/6`, not an integer.  So the report's defect (4) upgrades
from "can lie in `V^sigma`" to a decidable criterion that provably fails in the
only filed control.

**N3 (new, exact).  The canonical map runs the wrong way.**  Let `tau_c` be the
local monodromy at the finite branch values of `h`, with the standard relation
`tau_1 ... tau_r sigma_infty = 1`.  Since `im(alpha*beta - 1) subset im(alpha-1) + im(beta-1)`
and `im(alpha^{-1}-1) = im(alpha-1)`,

```text
W_infty = im(sigma_infty - 1) subset sum_c im(tau_c - 1),
```

so the natural inertia-built map `(+)_c im(tau_c-1) -> V ->> W_infty` is
**surjective**, never injective-by-construction.  Its source rank is exactly the
finite-end diagonal contact:

```text
sum_c dim im(tau_c-1) = sum_i d_i(b_i-1) = 2G-2+d+s   vs   dim W_infty = d-s,
excess = 2G-2+2s > 0   <=>   G+s > 1.
```

So the canonical map has a kernel of dimension `2G-2+2s` in every case with
`s >= 2` — and `s = 1` is precisely the case where QCS is already free, since
then `Xi = E_gen - 0 = E_gen >= 0` by the promoted `X(a) >= 0`.  **The canonical
inertia-to-pole map is injective only where QCS needs no proof.**

Verified numerically: on the degree-six control,
`dim(im(sigma_+ -1) + im(sigma_- -1)) = 5`, it contains `W_infty` (dim 4), and
its nominal source rank is 8.  Also checked on 400 random relation tuples with
`3 <= d <= 7` and 1--3 finite branch points: containment held **400/400**.

**Verdict for item 6.** `CONFIRMED`.  Normalized off-diagonal branches, local
inertia, and braid descent do not yield a rank-`b_i` summand, and the failure is
structural rather than a gap in effort.  The report's four defects are all real;
defects (1) and (3) as stated, defect (2) sharpened by N3, defect (4) sharpened
to a theorem by N2.

## 7. Controls — `CONFIRMED`

**7.1 local normalization control.** `CONFIRMED`; it is the `e`-line
specialization of 2b/2d and it does check both the multiplicity and the
normalization qualifier, as claimed.

**7.2 degree-six passport.** `CONFIRMED`, recomputed from scratch.

```text
sigma_+ = (1 2 3 4 5), sigma_- = (0 1 2 4 3), sigma_infty = (0 3 1 5 2)  on {0..5}
cycle types            (5,1), (5,1), (5,1)                                  OK
sigma_+ * sigma_- * sigma_infty = id under RIGHT-TO-LEFT composition        OK
                              ( FALSE under left-to-right; the stated
                                convention is load-bearing and correct )
transitive                                                                  OK
total ramification 4+4+4 = 12  =>  2g-2 = -12+12 = 0  =>  G = 1             OK
d = 6, s = 2, d-s = 4, dim V = 5, dim V^sigma = 1, dim W_infty = 4          OK
```

I checked all six orderings under both conventions: exactly the three cyclic
orderings work, and only right-to-left.  The report pins the right one.

The control is also fully consistent with the promoted identity package, which
I verified independently rather than accepting:

```text
G=1, s=2, n=2, d_1=2, b_1=5, chi_gen = 2-2G-s-n = -4
finite contact   d_1(b_1-1) = 8 ,  pole contact d-s = 4 ,  total 12 = passport ram   OK
sum_i d_i b_i = 10 = d - chi_gen = 6+4                                               OK
E_gen = d-1-sum b_i = 0 = sum b_i(d_i-1)+chi_gen-1 = 5-4-1                           OK
Xi = E_gen-(s-1) = -1 < 0   and   sum b_i = 5 > 4 = d-s                              OK
```

So the control is an exact curve-layer object satisfying *every* hypothesis used
in report Sections 2--5 — transitive finite cover, Riemann--Hurwitz, affine
unramifiedness after deleting the boundary places, the pair-square ramification
theorem, the augmentation ranks — while violating QCS.  It therefore refutes any
derivation of QCS confined to that layer.  `CONFIRMED` as a valid negative
control for the curve/pair-square layer only.

The report also reads `b = 5, d_1 = 2` off the passport itself (two finite
ramification places of index 5), so the control is self-contained at the curve
layer and does not need the germ.  Worth stating explicitly, since the whole
point is that the germ is not available.

**Prior warning respected.** `CONFIRMED`.  The report says the recorded local
germ and this passport "are not glued", and that repaired cubic passports fail
the filed braid-equivariance test.  Both are faithful to the control artifacts:
the integration says the two objects "are not glued", and the braid audit says
the `(5,2,2)` equality germ and `(5,1)^3` passport "cannot be glued by the genus
obstruction" and that the `(5,3,2)` and `(6,3,2)` tuples "fail the necessary
cubic braid-equivariance test".  The report's phrasing is *weaker* than the
audit's, i.e. on the safe side.  It correctly declines to promote the audit and
correctly restricts the control's force to the curve layer.

**7.3 block-overlap control.** `CONFIRMED`.  `dim(Q[{1,2}] + Q[{2,3}]) = 3 < 4`;
cycle types and baseline integers record neither the supports nor their
pairwise intersections.  Correctly labelled a typing control rather than a
source-compatible example.

## 8. The sharp successor — `CONFIRM_WITH_CORRECTIONS`

**Decision: `OPEN` is correct in substance.  Do not stop it.  Do not advance it
to an explicit construction — Section 6 shows the curve/monodromy layer provably
cannot supply one.  But re-scope and re-name it.**

**CORRECTION 8a (scope: the card's object was never tested).**  The card
`PAIR-SQUARE-QCS/v1` asks for the **surface** square over a two-dimensional base:

```text
Z = (X x_U X) minus diagonal,   X = F^{-1}(U),  U = maximal target open where F is finite etale,
plus a boundary pair-event chain complex functorial under admissible blowups,
plus dim C_coll(F) = E_gen,
plus iota_F : reduced H_0(pole components; Q) -> C_coll(F),  injectivity => E_gen >= s-1.
```

The report studies `Cbar x_{P1} Cbar` — a **curve** square over `P1` on one
generic fibre.  That is a different object.  The report is honest about this in
two places (it disclaims proving blowup invariance of a surface chain complex,
and it says a surface pair square "might relate these objects"), but its
headline still writes `PAIR-SQUARE-QCS/v1 = OPEN(...)`, which reads as a verdict
on the card.  The card's surface square, its blowup-functorial complex, and the
identification `dim C_coll = E_gen` are **UNTESTED**, not open-for-the-stated-
reason.  Re-type the verdict at curve-layer scope and record the surface object
as untested.

**CORRECTION 8b (undeclared arrow substitution — the substitution is sound, and
I supply the missing dictionary).**  The report replaces `iota_F` by

```text
alpha_F : A_base -> W_infty,     rank sum_i b_i  ->  dim d-s     [report]
iota_F  : reduced H_0(poles) -> C_coll(F),  rank s-1 -> dim E_gen [card]
```

without saying so.  The substitution is legitimate, and the two are equivalent
under an exact dictionary that the report should have stated:

```text
reduced H_0(pole places; Q) = V^sigma                        (both have dim s-1;
        V^sigma = {vectors constant on each pole cycle}/constants, i.e. one
        coordinate per pole PLACE, modulo the global constant)
if alpha_F : A_base >-> V is injective, set C_coll := coker(alpha_F);
        then dim C_coll = (d-1) - sum_i b_i = E_gen                      exactly,
and iota_F is the composite V^sigma >-> V ->> coker(alpha_F);
        iota_F injective  <=>  im(alpha_F) intersect V^sigma = 0  <=>  (5.4).
```

So the report's `alpha_F` programme and the card's `iota_F` programme are the
same theorem in dual form.  Declare the substitution and the dictionary.

**CORRECTION 8c (the report discarded the cheaper arrow).**  This is the
substantive correction.  `E_gen >= 0` is *already promoted*: the integration
carries `X(a) >= 0` and `sum_a X(a) = E_gen`.  Hence `sum_i b_i <= d-1 = dim V`
is settled, and the entire residual content of QCS is the increment

```text
E_gen >= s-1    on top of    E_gen >= 0,          a gap of exactly s-1.
```

The natural home for that increment is a space of dimension `s-1` — which is
precisely `V^sigma`, i.e. the card's source `reduced H_0(pole places)`.  The
card's arrow is therefore aimed exactly at the increment, while the report's
`alpha_F` must construct rank `sum_i b_i` from nothing and so re-proves
`E_gen >= 0` along the way.  The report's reformulation is strictly harder than
the card's.  Restore the pole-source direction.

**CORRECTION 8d (attribution).**  The report's conclusion largely re-derives, in
new language, the braid audit's own safe item: "Pole incidence remains a global
missing map; the known local relative boundary uses finite ends."  The report
cites that audit as a control but does not credit it for this conclusion.  The
curve/augmentation derivation is a genuine independent confirmation and the N2/N3
obstructions are new, but the *headline* is a re-derivation, not a first finding.

**The four stop tests.**  `CONFIRMED` as the right cheap gates.  I can already
report results on two of them at the curve layer:

```text
BRAID-DESCENT      -- open (needs the actual quotient family, not a passport)
BLOCK-DIRECTNESS   -- FAILS at the curve layer: N2 shows the selected blocks do
                      not even land in W_infty, let alone sum directly
TARGET-TYPING      -- FAILS at the curve layer: N3, the canonical inertia map is
                      surjective onto W_infty with kernel dim 2G-2+2s
POLYNOMIAL-INPUT   -- correctly identified as the load-bearing unknown; the
                      degree-six control is exactly the object that satisfies
                      everything else and violates QCS
```

**Recommended successor name.**  Replace

```text
OPEN(BASELINE-TO-POLE MAP BEFORE INJECTIVITY)
```

by

```text
OPEN(POLE-TO-EXCESS INCIDENCE MAP; CURVE LAYER PROVED INSUFFICIENT)
  source  : V^sigma = reduced H_0(pole places; Q),  rank s-1
  target  : a source-labelled excess module of dimension E_gen = sum_a X(a)
  content : exactly the increment E_gen >= s-1 over the promoted E_gen >= 0
  barred  : any construction from local inertia, sheet blocks, or braid descent
            alone (N2, N3)
  untested: the card's surface square (X x_U X) and its blowup-functorial complex
```

"BEFORE INJECTIVITY" mis-emphasises: numerical injectivity into `V` is already
available from `X(a) >= 0`, and by the report's own `(5.4)` an abstract injection
is again equivalent to the inequality.  What is missing is *target typing and
canonicity*, not injectivity.

## 9. Maximum safe scope

The report's five safe outputs survive, with the riders proved above:

```text
PAIR-SQUARE-RAMIFICATION  Delta.R = Ram(h) on a smooth connected generic fibre.
                          SAFE.  Add: off-diagonal components of Y are reduced
                          (separability), which licenses "R = closure of the
                          off-diagonal square" as a cycle identity.  Doubly
                          certified: RH, and Delta.Y - Delta.Delta = 2d-(2-2G).
KELLER-AFFINE-UNRAMIFIED  Ram(h) supported at the boundary places.  SAFE.
POLE-CONTACT              length Ram_infty(h) = d-s.  SAFE.  Uses no Keller and
                          no A2 origin; true for every finite cover of P1.
AUGMENTATION-POLE-RANK    dim im(sigma_infty-1) = d-s, and
                          V = V^sigma (+) W_infty with dims (s-1)+(d-s).  SAFE.
QCS-REPHRASING            Xi = length Ram_infty(h) - sum_i b_i.  SAFE, once
                          deg h = td(f,g) and s(cover) = s(places) are declared
                          (3d) and the connectedness rider is restated (3e).
```

Additionally safe, from this review:

```text
SUPPORT-OBSTRUCTION (N2)  [1_S] in W_infty  <=>  |S cap C_j| = |S|*e_j/d for all j.
                          Fails for every proper nonempty S in the degree-six control.
CANONICAL-MAP-DIRECTION (N3)  (+)_c im(tau_c-1) ->> W_infty is surjective with
                          kernel of dimension 2G-2+2s; injective only when
                          G+s <= 1, i.e. only when s=1, where QCS is already free.
DUALITY-DICTIONARY (8b)   V^sigma = reduced H_0(pole places); C_coll = coker(alpha_F)
                          has dim E_gen; iota_F injective <=> (5.4).
```

**Not proved by this review or by the reviewed report:** a baseline module inside
the sheet representation; any incidence or transport map from finite quotient
events to pole places; the card's surface square or any blowup-functorial
boundary complex; `dim C_coll(F) = E_gen` as a constructed identification;
injectivity; QCS; PCB; strictness; an actual `PairRef`; a selector; a polynomial
map; or JC2.  No exit price is asserted and no book budget is consumed.  The
degree-six object remains a curve/passport control, is not glued to the local
germ, and is not a Keller counterexample.

The pair-square card stays live as a map-construction experiment, at the card's
own surface scope, with the pole-source arrow restored.

<!-- BODY-END -->
