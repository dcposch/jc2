# CAMPAIGN-PIN residual identification audit

## 1. Verdict

**Typed verdict: OPEN, not a promoted campaign-wide identification.**

The promoted materials do prove the conditional row facts needed after a curve
has already been placed in one of the reviewed gauges.  In that typed scope,
ROW-SWEEP/ROW-SWEEP-REVIEW promote the ledger: the `(6,3)` labels are killed by
triangular reduction to the promoted coprime theorem, nodal `(8,2)` and `(9,3)`
are killed by `M_inf <= 3d-3`, row `(6,4)` has sole survivor
`Delta=(6,4,3)`, row `(8,4)` has sole survivor `Delta=(8,4,6,3)`, and rows
`(8,6)/(9,6)` leave exactly six AM-numerical candidate types
(`row-sweep-hostile-review-grok46-20260831.md:40-67,95-191,209-226`).
ROW-NF-EXHAUSTION-REVIEW then promotes-as-corrected the conditional normal-form
bridge for curves already certified to carry `Delta=(6,4,3)` or
`Delta=(8,4,6,3)` (`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:25-37,361-378`).

What is not promoted is the quantifier jump from that finite `d <= 9` sweep to
**every** repaired `N=4` residual curve.  D1-DEGREE-REVIEW promotes the opposite
warning: raw degree is unbounded under target automorphisms if the residual
class is nonempty, and the meaningful degree target must be either a fixed
canonical target gauge or

```text
d_min = min_{T in Aut(A^2)} deg T(D_1).
```

It promotes only the Chau reduced-shape cage

```text
(d/g,n/g) in (u,1), (odd u,2), or (4,3),   g=gcd(d,n),
```

plus the explicit **through `d <= 9`** noncoprime list
(`d1-degree-hostile-review-gpt55-20260831.md:44-70,94-119,149-193,246-277`).
No charged input supplies a promoted bound `d_min <= 9`, or any replacement
finite cap.  Therefore the requested identification cannot be promoted as a
corollary chain.  The exact gap is:

```text
OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]:
For every curve D_1 in the repaired N=4 residual, prove that some target
automorphism puts D_1 in a gauge with d_min <= 9, or otherwise prove a finite
row pin strong enough to replace the d<=9 ROW-SWEEP quantifier.
```

## 2. Frozen inputs and hash status

Before mathematical use I verified all seven frozen copies in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.EuGHAr/inputs`.
Every SHA-256 matched the manifest in the charge:

```text
30eb230dca026da6d59cbc7dd733cdb4ca63af443d5069ee83f7713b83a357f3  row-nf-exhaustiveness-opus5-20260901.md
723a3cc18b1b01cb451c19dbe27bb63778d09a125048e1c94591f4f94ba4f5ac  row-nf-exhaustiveness-hostile-review-sol56-20260901.md
0549dfafe339d20c67fe0d64a0bc713c1e64850013fbaab9f07f654c7fbf8fc2  d1-degree-bound-sol56-20260831.md
028b1c03489791f8cd674cc371c8b43c8994784aa65a05c8cfbb6dae269d3129  d1-degree-hostile-review-gpt55-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
64878fe8ec85da76f492be28b78e7cec0617c147eb030bd84d981e0950f2757d  row-sweep-hostile-review-grok46-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

No CAS or long computation was run.  I did not inspect `jc2-lean`, and I did not
edit any frozen input, charged file, or canonical ledger.  This report asserts
no new exit-price assertion.

## 3. Promoted chain available for composition

The composable promoted chain has the following typed links.

First, D1-DEGREE fixes the repaired residual object only up to target gauge.  In
coordinates adapted to a polynomial parametrisation
`gamma(t)=(p(t),q(t))`, `d=deg p>n=deg q`, the ordinary degree of the embedded
curve is `d`, and the infinity orders are `(d-n,d)`
(`d1-degree-bound-sol56-20260831.md:54-64`).  The repaired residual supplies
polynomial components, branch component `D_1`, transposition meridians, and
affine singularities that are double points of two smooth branches
(`d1-degree-bound-sol56-20260831.md:54-59`).

Second, D1-DEGREE-REVIEW promotes target-automorphism invariance of the residual
cover data: postcomposing by `T in Aut(A^2)` preserves the Keller property,
asymptotic set, finite cover, branch locus, local fibre cardinalities, `a_D`,
`a_p`, monodromy classes, normalisations, and incidences
(`d1-degree-hostile-review-gpt55-20260831.md:48-70`).  This is the licence used
by ROW-SWEEP-REVIEW for the `(6,3)` triangular reductions
(`row-sweep-hostile-review-grok46-20260831.md:55-59`).

Third, the promoted coprime theorem applies only after the target gauge has
coprime degree pair.  ROW-SWEEP-REVIEW uses it to kill the two `(6,3)` labels
after approximate-root shears to `(5,3)` and `(4,3)`
(`row-sweep-hostile-review-grok46-20260831.md:44-61`).  The coordinator
integration states the corrected explicit-family row-kill for all `D_{b,c}` and
`D'_{b,c}`, `c != 0`, while warning that campaign-row phrasing still depends on
the FOLD/ROW-SWEEP identification (`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md:30-63`).

Fourth, the nodal M-INF gate is promoted only at `T=0`: if
`M_inf <= 3d-3`, then the complement group is cyclic and the required `S_4`
quotient is killed (`row-sweep-sol56-20260831.md:96-103`;
`row-sweep-hostile-review-grok46-20260831.md:65-67`).  ROW-SWEEP-REVIEW
confirms it kills nodal `(8,2)` and nodal `(9,3)` at the enumerated rows
(`row-sweep-hostile-review-grok46-20260831.md:63-93,213-216`).

Fifth, ROW-SWEEP-REVIEW confirms the row ledger inside the finite sweep:
`Delta=(6,4,3)` is the unique `(6,4)` M-INF survivor; `Delta=(8,4,6,3)` is the
unique `(8,4)` M-INF survivor and is target-equivalent to the `(6,4)` survivor;
`(8,6)` leaves four numerical types; `(9,6)` leaves two numerical types
(`row-sweep-hostile-review-grok46-20260831.md:95-191,217-224`).

Finally, ROW-NF-EXHAUSTION-REVIEW repairs and promotes-as-corrected the
conditional algebraic theorem:

```text
Delta=(6,4,3) or Delta=(8,4,6,3)
  ==> target-equivalent to D_{b,c} with c != 0.
```

Its review explicitly refuses the broader campaign statement on that frozen
basis and keeps the six entries typed as AM-numerical candidates, not realised
residual curves
(`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:25-37,331-348,361-378`).

## 4. Where the chain stops

The finite sweep is not a theorem over all target gauges.  D1-DEGREE proves a
no-go for raw degree bounds: if one residual object exists, the target
automorphisms

```text
T_k(u,v)=(u,v+u^k)
```

preserve all promoted residual data and send a parametrisation `(p,q)` to
`(p,q+p^k)`, giving normalised pairs `(kr,r)` and ordinary degrees tending to
infinity (`d1-degree-bound-sol56-20260831.md:124-168`).  The hostile review
confirms this with the nonempty-class caveat and says any payoff must be
target-invariant or must first choose a canonical gauge
(`d1-degree-hostile-review-gpt55-20260831.md:44-70,223-243`).

The actual promoted cage is Chau's reduced-shape trichotomy.  With
`g=gcd(d,n)` and `(u,v)=(d/g,n/g)`, an escape from the promoted coprime theorem
has `g>=2` and

```text
(u,v) = (u,1), or (odd u,2), or (4,3).
```

This is necessary only.  In a Jung-reduced target gauge the denominator-one
family is removed by triangular degree reduction, but that gauge is not part of
the promoted residual; the infinite `(odd u,2)` family remains
(`d1-degree-bound-sol56-20260831.md:226-248`).  D1-DEGREE-REVIEW promotes the
same trichotomy and the scale warning
`g <= gcd(deg P,deg Q)-2`, which is not finite without a bound on target
coordinate degrees (`d1-degree-hostile-review-gpt55-20260831.md:94-119`).

The only finite noncoprime row list promoted by D1-DEGREE is explicitly
qualified:

```text
through d <= 9:
(4,2);
(6,2),(6,3),(6,4);
(8,2),(8,4),(8,6);
(9,3),(9,6).
```

(`d1-degree-bound-sol56-20260831.md:404-419`;
`d1-degree-hostile-review-gpt55-20260831.md:149-193,267-270`).
ROW-SWEEP then works on those rows.  Nothing in the charged set upgrades
"through `d <= 9`" to "all repaired residual curves."  The coordinator file is
consistent with this dependency: its exact-six consequence is stated "given the
ROW-NF exhaustiveness dependency", while its stops say campaign-row phrasing
requires FOLD/ROW-SWEEP identification and is not promoted
(`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md:55-60,73-76,90-100`).

Thus the missing link is not ROW-NF algebra.  It is a promoted finite pin on
`d_min` or an equivalent canonical-gauge degree bound.  Without that link, the
composition may say:

```text
If D_1 has already been placed in one of the swept d<=9 rows, the promoted
battery leaves only the two reviewed delta rows or the six AM-numerical
(8,6)/(9,6) types.
```

It may not say that every repaired residual curve has been placed in those
rows.

## 5. Residual classification after typing the gap

With the gap typed, the residual must be ranked in two layers.

**Conditional finite layer.**  If a separately promoted bound puts every
residual into a gauge with `d <= 9` (or directly into the swept list), then the
ROW-SWEEP ledger applies exactly as reviewed.  The surviving ROW-SWEEP
identification is:

```text
reviewed rows:
  Delta=(6,4,3),      (beta_1,delta_inf,delta_aff,M_inf)=(15,7,3,16);
  Delta=(8,4,6,3),   characteristic (4;10,19),
                     (delta_inf,delta_aff,M_inf)=(18,3,22).

AM-numerical candidate types:
  (8,6): Delta=(8,6,11), (beta_1;delta_inf,delta_aff;M_inf)=(21;10,11;22)
         Delta=(8,6,9),                                      (23;11,10;24)
         Delta=(8,6,7),                                      (25;12, 9;26)
         Delta=(8,6,3),                                      (29;14, 7;30)
  (9,6): Delta=(9,6,4),                                      (23;22, 6;25)
         Delta=(9,6,2),                                      (25;24, 4;27)
```

The two reviewed rows are actually target-equivalent and in-class three-node
attainments at the curve level; neither attainment asserts the global residual
`S_4` representation.  The six `(8,6)/(9,6)` entries are complete Galindo
censuses after M-INF, not existence theorems for nodal `A^1` normalisations
(`row-sweep-hostile-review-grok46-20260831.md:97-150,154-191,201-203,217-226`;
`row-nf-exhaustiveness-opus5-20260901.md:526-548`).

**Unconditional layer without a `d_min` bound.**  The finite list above must be
augmented by all higher noncoprime Chau shapes not brought into the swept rows:

```text
(u,1):       (d,n)=(gu,g),       g>=2, u>=2;
(odd u,2):  (d,n)=(gu,2g),      g>=2, u>=3 odd;
(4,3):      (d,n)=(4g,3g),      g>=2.
```

The next pairs beyond the reviewed `d <= 9` range are:

```text
d=10: (10,2),(10,5) from (u,1);  (10,4) from (5,2).
d=12: (12,2),(12,3),(12,4),(12,6) from (u,1);
      (12,8) from (3,2);  (12,9) from (4,3).
d=14: (14,2),(14,7) from (u,1);  (14,4) from (7,2).
d=15: (15,3),(15,5) from (u,1);  (15,6),(15,10) from (5,2),(3,2).
d=16: (16,2),(16,4),(16,8) from (u,1);  (16,12) from (4,3).
```

Prime degrees such as `11` and `13` contribute no noncoprime escape in these
three shapes; the coprime cases are already under the promoted coprime theorem.
This enumeration is just the Chau trichotomy with `g>=2`; it is not an
existence assertion.

## 6. General-shape gate coverage

The promoted gates behave differently on the three infinite shape families.

**Shape `(u,1)`: degree descent, not an immediate coprime kill.**  Here
`(d,n)=(gu,g)` with `g>=2`.  Since `d` is a multiple of `n`, if
`p(t),q(t)` have leading coefficients `a,b`, the triangular target
automorphism

```text
(x,y) -> (x - (a/b^u)y^u, y)
```

strictly lowers the first coordinate degree.  Therefore no denominator-one
shape can be a representative in a true `d_min` gauge.  But the first descent
does **not** force a coprime pair: the next surviving degree may still have
nontrivial gcd with `g`.  If the descent eventually lands in `gcd=1`, the
promoted coprime theorem kills; otherwise it lands in a smaller noncoprime
shape needing its own gate.  So `(10,2)` and `(12,3)` are not minimal-gauge
rows, but their raw appearances are not themselves the coprime stratum.

As a desk-scale diagnostic, the nodal M-INF gate would kill the two examples
named in the charge after running the same Galindo arithmetic used in the
sweep.  For `(10,2)`, admissible residual sequences are
`Delta=(10,2,c)`, `c=3,5,7,9`; the conversion gives
`beta_2=20-c`, `M_inf=27-c`, while `3d-3=27`, so every nodal case satisfies
`M_inf<=3d-3`.  For `(12,3)`, admissible residual sequences are
`Delta=(12,3,c)`, `c=2,4,5,7,8,10,11`; the conversion gives
`beta_2=24-c`, `M_inf=32-c`, while `3d-3=33`, so every nodal case again
satisfies the promoted `T=0` gate.  This is not a promoted finite census:
outside nodal scope it does not fire, and for general denominator-one rows the
right invariant conclusion is still descent to a smaller gauge, not a raw-row
classification.

**Shape `(odd u,2)`: no automatic triangular reduction.**  Here
`(d,n)=(gu,2g)` with `u` odd.  Since `n` does not divide `d`, the simple
`p-phi(q)` degree drop is unavailable.  ROW-SWEEP-REVIEW explicitly warns that
when `delta_1` does not divide `delta_0`, the approximate root need not be a
univariate Tschirnhausen polynomial in `q`; using it as an elementary target
automorphism would be false (`row-sweep-hostile-review-grok46-20260831.md:55-57`).
The finite rows `(6,4)` and `(9,6)` show the actual situation: one reviewed row
and two AM-numerical candidates survive the promoted row battery
(`row-sweep-hostile-review-grok46-20260831.md:95-125,173-191`).  Higher rows
such as `(10,4)`, `(12,8)`, `(14,4)`, `(15,6)`, and `(15,10)` have no promoted
general kill.

**Shape `(4,3)`: no automatic general kill.**  Here `(d,n)=(4g,3g)`.  The
base case `(8,6)` is exactly the reviewed row that leaves four AM-numerical
candidate types after M-INF (`row-sweep-hostile-review-grok46-20260831.md:152-171`).
Thus the promoted battery cannot contain a general `(4,3)`-shape kill.  Higher
rows such as `(12,9)` and `(16,12)` require a fresh row census, a new
noncoprime tuple theorem, or a finite `d_min` pin.

The other promoted structural tools do not close these tails.  The slice
identity `d=2g_L+c(Pi)+2` is a conversion law with no promoted bound on `g_L`
(`d1-degree-bound-sol56-20260831.md:357-390`;
`d1-degree-hostile-review-gpt55-20260831.md:121-147`).  A'(1)--(4) are used as
negative controls only; A'(5), the off-coprime order fork, AM-converse
attainment, and tangential M-INF are all withheld
(`row-sweep-hostile-review-grok46-20260831.md:197-205,222-224`).

## 7. Required replacement statement

The needed replacement is a finite, target-invariant row pin.  A sufficient
form is:

```text
THEOREM[PI1S4-D1-DMIN<=9]:
For every D_1 in the repaired N=4 residual, there is T in Aut(A^2) such that
T(D_1) admits a birational polynomial parametrisation (P,Q), deg P>d Q,
with deg P <= 9.
```

Together with target-automorphism invariance, Chau's trichotomy, and the
promoted ROW-SWEEP ledger, this would license the desired finite
identification.  In a Jung-reduced version the denominator-one shapes disappear
by degree descent, so the `d<=9` possibilities reduce to `(6,4)`, `(8,6)`,
and `(9,6)`; the known `(8,4)` gauge is then the reviewed nonminimal
`Phi^{-1}` image of the `(6,4)` survivor, not a separate geometric case
(`d1-degree-bound-sol56-20260831.md:244-248,414-419`;
`row-sweep-hostile-review-grok46-20260831.md:146-150`).

D1-DEGREE already names what such a theorem must control.  One route is to fix
a canonical target gauge, or use `d_min`, and acquire the endpoint polar vector

```text
(-ord_{z_infty}(u|l_1), -ord_{z_infty}(v|l_1)),
```

equivalently the two pullback-of-ruling coefficient vectors and base-point
multiplicities on a minimal weighted Orevkov tree.  A second route is to bound
the genus `g_L` of a generic restricted degree-four cover over a target line,
or the equivalent horizontal different / quartic-discriminant pole order; the
identity `d=2g_L+c(Pi)+2` would then convert that into a degree cap.  A third
route is a Keller-specific upper bound on `delta_aff` or directly on the last
characteristic exponent `beta_h`, strong enough to make M-INF bite
(`d1-degree-bound-sol56-20260831.md:357-390,430-474`).

Until one of those replacements is promoted, the campaign-wide statement must
be typed as:

```text
OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND].
Current safe ledger = conditional d<=9 ledger
  + unbounded higher Chau-shape tails:
    (u,1), (odd u,2), (4,3),
with only the automatic gates described in section 6.
```

## 8. Final status

The proposed identification is **not promoted** as a campaign-wide corollary.
The safe promoted statement is conditional:

```text
For a repaired N=4 residual curve already lying in the reviewed d<=9 sweep
scope, the ROW-SWEEP survivors are exactly the two reviewed delta rows
Delta=(6,4,3), Delta=(8,4,6,3), plus the six (8,6)/(9,6)
AM-numerical candidate types.
```

The unqualified campaign statement has the typed gap
`OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`.  No promoted input bounds `d_min` or fixes a
canonical target gauge with `d<=9`; D1-DEGREE instead promotes raw-degree
unboundedness and only the infinite Chau reduced-shape cage.  Therefore the
residual after this lane is the conditional finite ledger plus the higher
unbounded shape tails listed above, subject only to coprime landing, denominator-
one degree descent, nodal M-INF when its hypotheses are separately checked, and
the explicit row kills already reviewed.

<!-- BODY-END -->
