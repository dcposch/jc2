# Hostile review: global `D9` fibre-orbit and cap ledger

Verdict: **CONFIRM_WITH_CORRECTIONS**.

I reviewed the packet on frozen review basis
`06d8f99967ffb3ce34145d30f1e27e23dd07331b`.  The charged main artifact,
manifest, replay script, JSON data, and four named predecessor reports hash to
the values in the assignment.  The main report body through `<!-- BODY-END -->`
has byte count `26016` and SHA-256
`08484e2866fffda5ce9d2fd109f04e2f05dee3d1f4958ea28d4a08b69e8563ca`; its
artifact manifest
`xmodel/bd-a2-d9-global-fibre-orbit-cap-ledger-sol56-20260830.md.artifact.json`
hashes to `71bc7064fee68941b63b174fa723a22d05c9ca5f03c973b83dbf75cd34443bd2`.

I reran the standard-library replay and independently recomputed the counting
claims.  The generated canonical JSON has SHA-256
`88d30955fc6017770fe02cb381ab25cbcd2ce8263f7403864e8c2dc862530d96` and is
byte-identical to
`xmodel/bd-a2-d9-fibre-signatures-sol56-20260830.json`.  No heavy CAS,
Singular, AWS, staging, or `jc2-lean` access was used.  I did not edit the
producer artifacts, script, data, manifest, or dependencies; a transient Python
bytecode cache from one import was removed.

## 1. Signed-support `D9` classification

Verdict: **CONFIRMED**, with one wording repair.

The signed-support proof is correct for the stated reflection-closure
convention.  In a connected used support of size `s`, switching signs along a
spanning tree turns the tree roots into differences.  If every signed cycle is
balanced, the closure is the difference root system `B_s=A_(s-1)`.  If one
unbalanced cycle exists, a sum root is present; reflecting it by the difference
roots gives all `+-e_i+-e_j` on that support, i.e. `U_s=D_s`.  The low-rank
aliases are necessary: `U_2=D_2=A1+A1` is disconnected as a root system, while
`U_3=D_3=A3`.

There is no hidden exceptional connected type under this convention.  A
connected simple-root support graph can only generate the `A_(s-1)` or `D_s`
closure above.  Thus the older connected-only exclusions of `A9,E6,E7,E8` are
subsumed, and disconnected systems are direct sums of these signed-coordinate
blocks, except that `U_2` contributes two root components on one actual fibre.

The passage from the full signed permutation group to `W(D9)` does not split an
orbit.  A full-signed orbit would split under the index-two even subgroup only
if the stabilizer contained no odd signed element.  Every signature has such an
odd stabilizer: flip an unused coordinate; or flip one coordinate in a `U`
block; or, if all nine coordinates are covered by balanced blocks, flip every
coordinate in an odd-sized balanced block.  Exhausting all signatures gives
case counts `75` unused, `32` with a `U` block and no unused coordinate, and
`8` all-balanced full-cover cases; there are no failures.

The count is independently reproduced.  The support histogram for the
two-coloured used-support product is

```text
[1, 0, 2, 2, 5, 6, 13, 16, 30, 40]
```

and summing it gives `115`.  Root connectivity is `1` zero, `15` connected,
and `99` disconnected.  Imposing the optional ambient-span saturation
diagnostic, equivalently allowing at most one unbalanced block, gives `75`
signatures and `59` disconnected signatures.  This diagnostic is not the
charged theorem.

Repair: the word "full" must remain tied to "reflection-closed signed-support
subsystem", not to the saturated subsystem `R(D9) cap span_Q(Phi)`.  Under the
saturated convention the headline count would be `75`, not `115`.  Also,
Section 1's displayed histogram is the used-support histogram before the
unused-coordinate factor; the degree-nine coefficient of the full generating
function with `1/(1-x)` is `115`.

## 2. Fibre normal form

Verdict: **CONFIRMED**, with scope wording tightened.

The adjunction calculation is sound.  For a final smooth rational vertical
component `C`, the charged inputs give `K_Xtilde=-A+B` and `B.C=0`, hence

```text
-2=(K_Xtilde+C).C=-A.C+C^2,
A.C=C^2+2.
```

Since `A` is nef, `C^2>=-2`.  Every affected fibre component starts as a
square-zero original fibre component or a `-1` exceptional component, and every
later blowup lowers by one the component containing its centre.  Therefore no
component already at `-2` can be blown up later, and final affected fibre
components have square only `-1` or `-2`.

This leaves exactly the two claimed block types.  Smooth blowups on terminal
`-1` components give

```text
B_s: (-1)-(-2)-...-(-2)-(-1), beta=(1,...,1),
```

with root graph `A_(s-1)`.  The only permissible node blowup is the second
blowup on a fresh fibre, when the two components meeting at the node are still
both `-1`.  It gives

```text
U_2: two beta-one (-2) leaves joined through a beta-two (-1),
U_s, s>=3: two beta-one short leaves and a beta-two fork/long arm,
```

with root graph `A1+A1`, `A3`, or `D_s` according to `s=2`, `s=3`, or `s>=4`.
The fibre multiplicity vector satisfies `Q_t beta=0`, `gcd(beta)=1`, and the
sum of the beta weights on `-1` components is `2`, so no multiple-fibre
counterexample is hiding in these blocks.  The charged predecessor also supplies
the section that excludes global multiple fibres before the blowup marking.

I found no missed proximity tree or later node sequence.  A node blowup after
the second step would have to touch a `-2` component and would force final
self-intersection below `-2`, contradicting nef adjunction.  Smooth blowups can
only continue from the currently available `-1` terminal component.

The marked-original-component count is correct.  A `B_s` chain has `s+1`
possible original-component positions modulo reversal, i.e. `floor(s/2)+1`;
each `U_s` has one marked orbit because the original component is one of the
two symmetric short leaves.  Thus the marked species generating function is

```text
(1-x)^-1 product_{s=2}^9 (1-x^s)^-(floor(s/2)+2),
```

whose degree-nine coefficient is `362`.

Projective finiteness is exactly the right extra hypothesis for the converse
identification of final `-2` fibre vertices with Du Val exceptional curves.  If
`C^2=-2`, then `A.C=0`, so the target image is a point.  If `r(C)` were a curve
and `pi:X->P2` were finite, its image would still be a curve, contradiction.
Without finiteness, the converse fails: extra `A`-null nonexceptional vertical
curves are not excluded by the lattice calculation alone.

Repair: promote this only as a bijection between signatures and abstract
unmarked weighted blowup-forest block multisets.  It is not a bijection with
actual marked configurations, blowup locations, carrier decompositions, or
incidence moduli.

## 3. Replay, JSON, and exact combinatorics

Verdict: **CONFIRMED**.

The 244-line replay is a small deterministic enumerator.  It uses the species
`B_s,U_s` for `2<=s<=9`, treats unused coordinates as `B_1`, and recursively
lists all two-coloured partitions of total used support at most nine.  Its
canonical JSON is emitted with `sort_keys=True` and compact separators, and the
live output hash equals the archived data hash.

An independent checker verified every fibre-block record in the JSON:

```text
B1, B2, U2, B3, U3, ..., B9, U9
```

have the expected edge sets, self-intersections, beta vectors, root vertices,
root type aliases, and marked-original orbit counts.  For every block the full
intersection matrix satisfies `Q beta=0`; beta is primitive; and beta-weight on
the `-1` vertices sums to `2`.  In particular `U_2` has beta `[1,1,2]` and root
type `A1+A1`; `U_s` for `s>=3` has beta `[2,1,1,2,...,2]` with the beta-two
fork and long arm.

Every signature record was also independently checked.  The recomputed
`support_size`, `unused_coordinates_B1`, `fibre_count`, root rank, root
component count, root connectivity, saturation flag, and sort order agree with
the JSON.  The replay correctly counts `U_2` as one actual fibre but two root
components.  The script does not attempt to check geometry beyond the encoded
block identities, and that is the proper scope.

Minor note: the assertion in the script that `square+2` is `1` on `-1`
components and `0` on `-2` components is only a tautological replay of the
allowed self-intersection list.  The actual geometric input is the adjunction
and nefness argument in the report, not that assertion.

## 4. Total-transform identity and shared caps

Verdict: **CONFIRMED**.

The total-transform identity is correct.  With `E_i.E_j=-C_ij`,
`r^*D=D'+xE`, and `r^*G=G'+yE`, orthogonality gives `D'.E=Cx` and `G'.E=Cy`.
The three exceptional cross terms are

```text
D'.(yE)=x^t C y,
(xE).G'=x^t C y,
(xE).(yE)=-x^t C y,
```

so exactly one copy remains:

```text
D.G=D'.G'+x^t C y.
```

Every cap in the packet is an instance of this identity plus nonnegativity of
the residual strict-transform intersection, and every cap is correctly typed
as conditional on no common strict carrier.

The ownership rules are correct:

* Target-line caps are shared per target image.  All singular points over the
  same target point consume the same `A.R=8` or, on the infinity line, `A.H=3`
  budget.
* Actual source-fibre caps are shared per actual fibre and must use the exact
  fibre beta weights.  In particular the two `A1` points in one `U_2` block do
  not receive two independent `B.R=4` or `B.H=2` budgets.
* The infinity/different cap `H.R=8` is global along the one fixed infinity
  divisor, with contribution `h^t n`, not a per-point allowance.
* If a common nonexceptional carrier is present, the cap is suppressed.  The
  replacement formula contains `de Gamma^2`, which can be negative, so a
  common-carrier stratum is not a large finite capped row.

The finite-flat statement is safe exactly under projective finiteness.  A finite
degree-three map from the normal surface `X` to the regular surface `P2` is
flat by the Cohen--Macaulay/regular target criterion, so each fibre has length
three and hence at most three source points.  If `pi` is only generically
finite, this statement is unavailable.

I found no conflation of the two Cartier vectors.  The report keeps
`n=Cm` for the different and `a=Ch` for infinity.  The formulas use
`ell^t n`, `ell^t a`, `beta^t n`, `beta^t a`, `h^t n`, and `h^t a` in their
proper places.

## 5. Reduced-`H` genus/drop filter

Verdict: **CONFIRM_WITH_CORRECTIONS**.

The arithmetic is correct for reduced `H`.  On the fixed infinity surface
`L_infinity x P1`, the divisor has bidegree `(2,3)`, so `p_a(H)=2`; reducedness
and the bidegree argument make its support connected.  Writing
`r^*H=H'+Z`, `Z=sum h_iE_i`, crepancy gives `K.E_i=0`, and orthogonality gives

```text
H'.Z=-Z^2=h^t C h=h^t a.
```

Adjunction then gives the exceptional arithmetic-genus contribution

```text
p_a(r^*H)-p_a(H')=h^t a/2.
```

Equivalently, localizing the normalization sequence gives

```text
delta_p(H)=h^t a/2 + sum_{q over p} delta_q(H').
```

Thus `h^t a` is even, and `h^t a/2` is a lower bound for the local delta unless
the lifted strict transform is already locally nonsingular over `p`.

The branch inequality is also correctly oriented.  Every physical branch of
`H` through the Du Val point must meet the exceptional set after strict
transform, and a branch through an exceptional node may contribute to two
entries of `a` while still being one branch.  Hence
`r_p<=sum_i a_i`, not equality in general.

The global defect budget follows from the normalization graph:

```text
p_a(H)=g + sum_p(delta_p-r_p+1) + b_1 = 2.
```

Since `g,b_1>=0`, summing only Du Val points gives

```text
sum_p max(0, h_p^t a_p/2 - sum_i a_{p,i} + 1) <= 2.
```

The individual inequality `h^t a<=2(sum a_i+1)` follows.  Under the proper
`B/H` cap, `sum a_i<=beta^t a<=2`; therefore `h^t a<=6`, so every local row
with `h^t a=8` is eliminated in that stratum.  If `h^t a=6`, then `sum a_i=2`
and that one point consumes the entire genus-two defect budget.

Repair: the theorem statement should say "the exceptional crepant genus
contribution is exactly `h^t a/2`."  The full local delta is exactly
`h^t a/2` only after separately proving that the lifted strict transform has no
remaining local singularity over the Du Val point.  This is a wording repair,
not a failure of the displayed inequalities, because the packet later states
the refined formula with the extra lifted-delta terms.

## 6. Scope and promotion boundary

Verdict: **CONFIRMED**.

The packet enforces the necessary firewall.  A root/fibre signature is not an
effective marked configuration, not a proximity history, not a carrier
decomposition, not a target-image labelling, not an analytic germ, not a finite
map, and not a JC2 conclusion.  Adding beta weights, original-component
markings, physical attachment points, `(m,n,h,a)`, target labels, and carrier
IDs can break the stabilizer used for the unmarked `W(D9)` quotient.  In
particular `B_4` and `U_3` are both abstract `A3` but have different coordinate
and fibre meanings, and `U_4` retains fibre weights that break full `D4`
triality down to the transposition of the two short leaves.

Maximum promotion-ready theorem:

> In the stated normal class-`2A+3B` incidence scope, with the ruled nine-blowup
> marking and, where used, projective finiteness, the unmarked
> reflection-closed signed-support subsystems of the actual `D9(-1)`
> orthogonal complement are classified by signatures
> `sigma=(u;b_2,...,b_9;d_2,...,d_9)` with
> `u+sum_s s(b_s+d_s)=9`.  There are exactly `115` signatures, consisting of
> one zero, `15` connected nonzero root systems, and `99` disconnected root
> systems; the optional saturated diagnostic is `75` total and `59`
> disconnected.  These signatures correspond exactly to abstract unmarked
> weighted blowup-forest block multisets `B_s/U_s`, with marked-original
> refinement count `362`.  In declared proper-intersection strata only, the
> total-transform identity gives shared target-image, actual-fibre, and
> fixed-infinity caps; for reduced `H`, the exceptional genus contribution
> `h^t a/2` and the global genus-two defect budget eliminate `h^t a=8` under
> the proper `B/H` cap.  No converse effectivity, carrier enumeration,
> analytic-incidence realization, nonnormal extension, polynomial-map result,
> or JC2 result is promoted.

Cheapest exact successor:

Build the carrier-disjoint numerical-decoration allocator, not an incidence
realizability search.  Expand each of the `115` signatures to physical ADE
points, remembering that `U_2` gives two `A1` points on one actual fibre with
one beta-weighted fibre budget.  Partition points into target-image blocks of
size at most three, mark infinity blocks, enumerate local `(m,n)` and `(h,a)`
from Cartan congruences, and allocate the shared target, fibre, fixed-infinity,
and reduced-genus budgets only in proper no-common-carrier strata.  Then add
physical atom partitions and carrier restricted-growth labels, canonicalized by
the actual stabilizer of the chosen fibre representative.  Common carriers
must remain a separate residual-intersection problem governed by the
`Gamma^2` formula.

## Required repairs before promotion

1. Replace any unqualified phrase "full reflection subsystem" by
   "reflection-closed signed-support subsystem under the non-saturated
   convention"; state that the saturated convention gives `75`, not `115`.
2. Reword the support histogram as the coefficient list for used support before
   multiplying by the unused-coordinate factor.  Keep the degree-nine
   coefficient of the full generating function equal to `115`.
3. State the fibre correspondence as an abstract weighted blowup-forest
   block-multiset classification.  Do not promote it as an effective or moduli
   classification.
4. In the reduced-`H` theorem sentence, replace "local genus drop is exactly
   `h^t a/2`" by "exceptional crepant genus contribution is exactly
   `h^t a/2`; the full local delta also includes lifted strict-transform
   singularities."
5. In any use of the replay script, do not cite the self-intersection assertion
   as a proof of adjunction or nefness.  It is only an internal consistency
   check after the block shapes have been supplied.

With those repairs, I find no gap or refutation in the charged root/fibre
classification, replayed counts, total-transform cap ledger, or reduced-`H`
conditional filter.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16223`.
- Body SHA-256:
  `cc578954a1e49fc5f7b1a32d5af5974107f31bbc4260414265286ddb20e6edcc`.
- Frozen basis: `06d8f99967ffb3ce34145d30f1e27e23dd07331b`.
