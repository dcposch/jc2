# BMFACT-964-KILL-REVIEW - gate the realized `(9,6,4)` representation kill

**Verdict: KILL-BINDING, curve-level only, with one nonblocking repair.**

The binding statement is this typed one.  Let

```text
D = image(t |-> (t^9 + 3 t^7 + (21/4)t^5 + (35/8)t^3 + (63/32)t,
                 t^6 + 2t^4 + (5/2)t^2 + 3/4)) in C^2.
```

There is no homomorphism `phi : pi_1(C^2 \ D) ->> S_4` which sends every fibre
meridian to a transposition and is compatible with the charged Sage braid
factorisation.  Equivalently, the realized six-nodal `(9,6,4)` curve has no
REP-96-admissible transitive degree-four representation.  This kills this
explicit curve at the representation gate.  It is not a row kill, not a claim
about every curve with numerical label `(9,6,4)`, and not a claim about
homomorphisms whose meridians are not transpositions.

## 0. Custody

Frozen inputs were hashed before reading.  All four matched the charge:

```text
01bac03c71000b9bc3557e1d4387864d9d5d23842434920bf70a2c6eb24949cc  bmfact964_result.json
709c08c83f99b444a89e2a4b38959a014a0d19ec990f7f2e1f8351aeaf6a755c  bmfact964_enum_run.log
9266de1542e68b64a346103eace77afd91f24b8d5195379c2f68abd19a469b79  bmfact-964-codegen-grok46-20260902.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
```

The in-place scripts also match the codegen seal, so the audited source is the
source whose hashes were reported by CODEGEN at lines 487-492:

```text
1d0d150950c1c55e9017724dbcca913d15bd492430be987e34c20038568a8f3f  box/bmfact_964.sage
e441ee8a41eb6ed15e6b8ff198b3b47a55ca230a3c78bc0bcbeca333376e2d22  box/bmfact964_enum.py
```

Line citations below use `SAGE`, `ENUM`, `RESULT`, `LOG`, `CODEGEN`, and `REP`
for the six files named above.  I also read the sealed 962 review only for the
requested final composition; I did not re-audit 962 inside this lane.

## 1. Sage Emitter Audit

`box/bmfact_964.sage` is conservative and explicit about the geometry.  It puts
`F` in `QQ[coord_x,coord_y]` with `(coord_x,coord_y)` generator order, checks
`deg_y(F)=9=deg(F)`, and therefore uses Sage's first-variable `x` projection
without a coordinate change (`SAGE:35-39`, `SAGE:265-353`, `SAGE:366-378`).
The affine, not projective, group is declared: no relation
`xi_9 ... xi_1 = 1` is imposed (`SAGE:87-90`).

The monodromy API is unpacked fail-closed for the two known forms: Sage 10.8's
four-tuple and develop's five-tuple with base point (`SAGE:21-31`,
`SAGE:650-671`).  The charged output is the four-tuple: `nstrands=9`,
`n_factors=11`, `base_point=null`, and the missing base point is serialized as a
flag (`RESULT:36-41`).  The script treats that as a labeling problem, not as a
reason to invent a strand order (`SAGE:721-731`).

The census check is strict enough for this charged run.  Factors are classified
by exponent sum, strand permutation, and CPF shape (`SAGE:607-647`), and the
964 version aborts on `other`, any `*_unexpected` CPF suffix, wrong counts, or
wrong ledger (`SAGE:823-892`).  The frozen JSON records the expected curve data:
six-dimensional Jacobian quotient, discriminant support degree 11, total
discriminant degree 20, valuation 8 at `x=0`, and valuation 2 at the new-node
quadratic (`RESULT:8-19`).  It then records the actual factor census:
eight `tangency`, one `four_node_fibre`, two `one_node_fibre`, ledger 20
(`RESULT:3269-3288`), and the independent curve entry point returns the same
braid strings (`RESULT:3290`).  The product has exponent sum 20 and a 9-cycle
permutation (`RESULT:3014-3084`), matching one place at infinity.

Nonblocking repair: `free_auto_F9` remains diagnostic-only.  The Sage helper
`artin_auto_images` applies multi-letter free automorphisms rightmost-first
(`SAGE:247-262`), the same metadata defect isolated in the 962 review.  The
native enumerator never reads `free_auto_F9`; it consumes raw `tietze` words.
Do not cite `free_auto_F9` as Sage's free-group action until regenerated.

## 2. Enumerator Audit

The decision path is the native transposition universe, not the REP-96 class
carrier and not an adjacent-block strand map.  The header states this directly:
all `6^9` labelled assignments in Sage strand order, per-relation pruning,
subsample certification, both orientations, and never a row-level kill
(`ENUM:11-15`, `ENUM:26-32`).

The tuple-side ZvK convention is correct.  Permutations are image tuples and
`compose_perm(first,second)` means `first o second` (`ENUM:66-118`).  A positive
Artin generator sends adjacent tuple entries `(a,b)` to `(a b a^-1, a)`, and a
negative generator sends them to `(b, b^-1 a b)` (`ENUM:248-276`,
`ENUM:878-896`).  A Sage Tietze word is applied rightmost letter first on
tuples (`ENUM:279-293`, `ENUM:899-905`), which is the dual of the free action
used to evaluate `x_j = beta(x_j)`.  I additionally checked all adjacent
transposition pairs for inverse recovery and all 216 local triples for the
braid relation; both tests returned zero failures.

The generating test is exactly the REP-96 condition in this universe.
`tuple_generates_s4` and `generates_int` build the graph on `{1,2,3,4}` whose
edges are the transposition supports and test connectedness (`ENUM:195-220`,
`ENUM:908-922`).  A subgroup generated by transpositions is the product of full
symmetric groups on the graph components.  Hence connectedness is equivalent to
image `S_4`, and also to transitivity on four letters.  This is not a
transitivity-only shortcut.

The native words are built directly from the Sage `tietze` lists.  Product-only
concatenates the 11 listed local words; full-ZvK uses the 11 words separately;
the inverse variant reverses and negates each word (`ENUM:943-957`).  The final
decision requires API/census success, product-only generating count 72 in at
least one orientation, then zero full-ZvK generating count in both orientations
before emitting `NATIVE_ZERO_CURVE_ONLY` (`ENUM:1228-1282`).

## 3. Pruner Audit

The pruning path is exact set intersection, not a heuristic.  `prune_native`
initializes by iterating every tuple in `product(range(6), repeat=9)` and keeps
exactly those fixed by word 0; for each later word it filters the current list
by the same fixed predicate (`ENUM:960-998`).  Therefore after word `j` the
list is exactly

```text
{T in Transp(S_4)^9 : T fixed by words 0,...,j}.
```

A true full survivor is fixed by every word, so it cannot be removed at an
earlier pruning stage.  Ordering changes runtime only.  This code-level
invariant is the load-bearing pruner bound.

The certification is also real, but it is a subsample certificate rather than a
global proof by itself.  `unpruned_native` iterates the deterministic residue
class `combo_id(T) = 0 mod 1021` and checks all words at once (`ENUM:1001-1019`);
`certify_prune_against_unpruned` compares the pruned and unpruned survivor sets
and records the symmetric difference (`ENUM:1022-1040`).  `run_native_scan`
aborts if the certificate fails (`ENUM:1080-1118`).  Thus a mutation/order bug
on the sampled slice is caught before interpretation.  Unsampled tuples are
covered by the simple set-intersection invariant above, not by pretending the
subsample is exhaustive.

The frozen run has the required certification in every native variant.  The
synthetic pruner has `550=550` and symmetric difference 0 (`LOG:39-42`,
`LOG:185-208`).  Product-only forward and inverse each have pruned/unpruned
`1=1` on the 9871-tuple subsample (`LOG:44-55`, `LOG:254-325`).  Full-ZvK
forward and inverse each have pruned/unpruned `1=1` on the same subsample and
then run the full `6^9` scan (`LOG:56-70`, `LOG:82-96`, `LOG:326-635`).  There
is no silent pruner-only path left unaudited for this result.

## 4. The 72 Control

REP-96 lists exactly the three `(9,6,4)` classes used by the control:
two `noncst-T` representatives and one `const-4c` representative (`REP:491-504`).
It states the `T_2,T_3` reconstruction and verifies full image on each class
(`REP:506-509`).  CODEGEN imports the same three representatives and explicitly
labels the class list as control-only, not a strand map for the decision
(`CODEGEN:314-350`).

I independently recomputed the simultaneous `S_4` conjugacy expansion from the
three displayed representatives, without importing the enumerator.  Each
representative has trivial simultaneous stabilizer in `S_4`, so each orbit has
24 elements; the three orbits are pairwise disjoint, giving `3*24=72`.  With the
CABLE-3 reconstruction at `k_*=-8`, the same independent check gave 72 unique
nine-tuples, all `rho_inf`-fixed in the adjacent-block product control and all
generating, split 24/24/24 by class.

The charged run agrees.  The class control prints expansion 72, Pi-type
`48` transposition plus `24` four-cycle, positive control 72, negative
projective control 0 (`LOG:35-38`), and the JSON tail records
`n_expanded=72`, `n_reconstructed_nines=72`, positive-control `n_generating=72`,
negative-control count 0 (`LOG:158-184`).  The independent brute adjacent-block
`6^9` product control gives `n_product_fixed=174`, `n_generating=72`
(`CODEGEN:343-350`; reproduced locally by `--selftest --curve-check`).  The
native product-only scans also give `n_fixed=174`, `n_generating=72` in both
orientations (`LOG:48-55`, `LOG:108`, `LOG:254-325`).  This is exactly the
expected product-only control, not the full decision.

## 5. Both Orientations and Full Variant

This run did not repeat the 962 first-pass omission.  The main routine runs four
native variants in sequence: product-only forward, product-only inverse,
full-ZvK forward, full-ZvK inverse (`ENUM:1561-1586`), then prints both summary
counts (`ENUM:1587-1595`).

The frozen log shows the full variants actually ran.  Forward full-ZvK starts at
`LOG:56`, certifies at `LOG:57-69`, and begins the full `6^9` pruning at
`LOG:70`; the full prune ladder has 11 words and ends with 6 fixed tuples at
`LOG:71-81`.  Inverse full-ZvK starts at `LOG:82`, certifies at `LOG:83-95`,
and begins full pruning at `LOG:96`; its 11-word ladder also ends with 6 fixed
tuples at `LOG:97-107`.  The summary is explicit:

```text
SAGE-NATIVE product-only generating as-written=72 inverse=72
SAGE-NATIVE full generating as-written=0 inverse=0
DECISION NATIVE_ZERO_CURVE_ONLY
```

Those are `LOG:108-110`; the scope sentence at `LOG:111` says this decides the
realized `(9,6,4)` curve only and is not a row-level kill.  The JSON tail
confirms forward full `n_words=11`, `n_fixed=6`, `n_generating=0`,
`survivors_verbatim=[]`, `total_survivors=0` (`LOG:326-404`), and the same
numbers for inverse full (`LOG:481-559`).  `survivors_verbatim=[]` is a list of
generating survivors only; six non-generating fixed tuples remain, so the kill
is specifically the absence of full-image/transitive representations.

## 6. Base Point

The absent Sage base point does not affect this zero/nonzero decision.  It would
matter for naming physical branches, comparing Sage order to REP-96 tube order,
or making a tau/leftover-strand claim.  This report makes none of those claims.

For the native decision, the braid words are already expressed in one coherent
Sage `B_9` basis, and the enumerator ranges over every labelled assignment in
`Transp(S_4)^9`.  A change of base point or strand numbering applies a Hurwitz
bijection to that same finite universe and preserves the subgroup generated by
the tuple entries.  Therefore existence or nonexistence of a generating common
fixed tuple is invariant.  Product-only equality 72 in both orientations is a
useful API/orientation control, but the missing base point cannot hide a native
full-ZvK survivor.

Thus `OPEN[BMFACT-BASEPOINT]` is closed for the zero/nonzero decision in this
run and remains open only for labeling/tube diagnostics.

## 7. Disposition

```text
BMFACT-964-KILL-REVIEW = KILL-BINDING

Surviving scope:
  D is the single explicit six-nodal curve parametrized in the headline.
  There is no phi: pi_1(C^2\D) ->> S_4 sending every fibre meridian
  to a transposition and satisfying all 11 charged local braid relations.
  Equivalently, no REP-96-admissible transitive degree-four monodromy
  representation exists for this realized braid factorisation.

Not claimed:
  no homomorphism at all;
  no S_4 surjection with non-transposition meridians;
  no other realized curve of numerical type (9,6,4);
  no row-level kill of (9,6);
  no Keller-map conclusion outside this representation gate.
```

Repair: quarantine or regenerate `free_auto_F9` metadata in the Sage emitter.
This is not on the native decision path.  The 964 census fail-closed issue that
962 had around unexpected CPF suffixes is already repaired (`SAGE:823-851`).

## 8. Composed Consequence

Combining with the sealed 962 review gives: both currently realized substrates
in the `(9,6)` row are representation-dead at curve level.  For `(9,6,2)`, the
962 review gates the explicit four-nodal curve and states no
transposition-meridian `S_4` surjection exists for that single curve; it also
warns that this is not all curves of type `(9,6,2)` and not the row
(`bmfact-962-kill-review-sol56-20260902.md:1-21`, `:500-527`).  This 964 review
now gives the parallel statement for the explicit six-nodal `(9,6,4)` curve.

What remains at `N=4` is numerical-type orbit coverage, not geometric
attainment.  REP-96 identifies the two `(9,6)` numerical types, their invariants,
and the group-theoretic product carriers: six classes / 144 tuples for
`(9,6,2)` and three classes / 72 tuples for `(9,6,4)` (`REP:74-84`,
`REP:491-509`).  The full braid-factorisation computation kills the two realized
representatives that were available for those types.  A row-level statement
would still need either all actual curves in each type to be represented by
these braid factorizations, or a theorem transporting the full local-braid
intersection across the relevant moduli.  REP-96 explicitly blocks that
promotion: `rho_inf`-fixedness is only the product of local relations, not full
existence (`REP:607-616`, `REP:740-743`), and `REPRESENTATIVE` is not
`FULL_ACTUAL_EXIT`; passing or killing a representative is not row attainment
(`REP:799-801`).

For `N>=6`, only pipeline validation transfers.  The reusable instrument now has
two successful end-to-end validations: exact curve/census custody, Sage native
braid words, product-only controls from REP-96, both orientations, and a pruned
native `6^9` enumerator with subsample certification.  The numerical kill itself
does not transfer to higher `N`, different rows, or different meridian cycle
types.  Those require their own representation universe and their own braid
factorisation or a separately promoted structural theorem.

## 9. FALLACY-v2

No exit price is asserted, so no `charge_basis` line is present.

Flag/place/series are separated: discriminant fibres, physical affine nodes,
REP-96 product carriers, and Sage strands are not identified.  Carrier and
attainment are separated: the REP-96 class list is a product-only control, while
the decision uses native full-ZvK.  Floor/attainment is separated: the 72
control is not an existence theorem for `phi`, and the six fixed native tuples
are not full-image survivors.  No `sat()`, raw remainder, pole identity,
M-descent, or target/arrival index argument is used in this review.

<!-- BODY-END -->
