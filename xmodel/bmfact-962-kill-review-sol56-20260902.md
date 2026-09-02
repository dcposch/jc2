# BMFACT-962-KILL-REVIEW — gate of the realized `(9,6,2)` representation kill

**Verdict: KILL-BINDING, with nonblocking repairs.**

The binding statement is the following precisely typed one.  Let

```text
D = image(t |-> (t^9 + 12 t^5 + 24 t, t^6 + 8 t^2)) in C^2.
```

There is no homomorphism

```text
phi : pi_1(C^2 \ D) -> S_4
```

which sends every fibre meridian to a transposition and has image `S_4`.
Equivalently in this transposition-meridian universe, there is no transitive
degree-four representation of the kind required by REP-96.  This kills **this
explicit realized curve** at that representation gate.  It does not kill all
curves with numerical label `(9,6,2)`, the `(9,6)` row, arbitrary homomorphisms
whose meridians are not transpositions, or a numerical type in another degree.

The full native result, not either BLOCK calculation, is load-bearing.  The
missing inverse-full run is covered by a proof: each braid and its group inverse
have exactly the same fixed set.  The missing Sage base point affects physical
strand names and the `tau`/tube interpretation, but not existence or
nonexistence in the complete native universe.

## 0. Custody and decision ledger

I hashed every frozen input before reading it and both repository scripts before
auditing them.  All six digests match the charge exactly.

| Input | SHA-256 | Gate |
|---|---|---|
| frozen `bmfact962_result.json` | `7ad79c5c1edcb9ecad97d068fd7aa684f03b0e0a7f3427d08d15c5560cfeed70` | MATCH |
| frozen `bmfact962_native_enum.log` | `537e0fa036a9915ba123cee164ab66ec047730aee1e7b68cad71e6260ff6b424` | MATCH |
| frozen `ideation-20260902T0022Z-sol56.md` | `4b0e4dde91a8bbe06dfde68e0c8c4559d92bcb8355a0b57acf32ba8b36a7d3b4` | MATCH |
| frozen `rep-96-inner-opus5-20260901.md` | `a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401` | MATCH |
| `box/bmfact_962.sage` | `2d18c1183d8ba5d7db8db767b38929064303422deadab41857e4c1a49d82d916` | MATCH |
| `box/bmfact_enum.py` | `b51813adcf7a407f97c486995f7f99ba73f616d0f04594506a069757bdbf832b` | MATCH |

The banked JSON identifies the parametrization and implicit polynomial, records
degrees `(deg_x,deg_y,total_degree)=(6,9,9)`, irreducibility, discriminant
support degree `9`, and discriminant valuation `8` at zero (frozen JSON
lines 2–17).  It records nine `B_9` factors, the absent fifth/base-point return
slot (lines 26–31), eight exact `tangency` labels and one exact `node_fibre`
label with exponent ledger `16` (lines 3966–3981), and a product whose strand
permutation is a 9-cycle (lines 3707–3721).  The two Sage entry points returned
identical braid strings (`curve_method_matches_module_function=true`, line
3983).  These facts tie the words consumed by the enumerator to the named
realized curve.

The frozen enumeration log records the decisive numbers twice: the run summary
has native full generating count zero and product-only generating count `144`
(lines 68–72), while its JSON block gives native full `n_fixed=6`,
`n_generating=0`, and `n_words=9` (lines 248–254).  Product-only has
`n_fixed=246`, `n_generating=144` in both orientations (lines 256–270).

## 1. Audit of `bmfact_962.sage`

### 1.1 Curve, ring map, and projection

The variable/ring map is explicit and sound.  The coefficient field is `QQ`,
the ordered generators are `(coord_x,coord_y)`, and `param_t` is introduced in
the univariate extension of that ring (`box/bmfact_962.sage:233-251`).  The
script forms `p(t)-coord_x` and `q(t)-coord_y`, takes their resultant, coerces it
back to the declared ring, rejects zero, and removes only rational content
(`:252-261`).  It then requires equality up to sign with the independently
written closed form and chooses the sign with positive `coord_x^6`
(`:263-286`).  Thus matching variable names are not being used as a substitute
for a declared map or image check.

The projection is the first ring generator.  Total degree and `coord_y`-degree
are both asserted to be `9`, `coord_x`-degree is asserted to be `6`, and the
leading `coord_y` coefficient is the nonzero constant `-1`
(`:289-307`).  Hence Sage's no-vertical-asymptote branch really does use the
`coord_x` projection.  The raw downstream payload is obtained directly from
each returned braid's `Tietze()` word (`:414-416`, `:632-667`); neither the
discriminant helper nor the diagnostic free automorphisms manufactures those
words.

The singular-scheme assertions at `:328-345` prove dimension zero and quotient
length four.  Those two assertions alone do not prove the accompanying prose
“four reduced affine nodes, all on `x=0`.”  For this exact polynomial the prose
is nevertheless true: independent elimination gives

```text
(F,F_x,F_y) = (coord_x, coord_y^4 + 96 coord_y^2 + 1536).
```

The quartic is squarefree.  The Hessian determinant modulo it is
`-1610612736*coord_y*(coord_y^2+72)`, coprime to the quartic, so all four points
are ordinary nodes.  This is a wording/validation repair for future jobs, not a
defect in this charged curve.

### 1.2 The line-366 `radical()` patch is correct and isolated

At `box/bmfact_962.sage:347-357`, the resultant in `coord_y` is transferred
coefficient-by-coefficient into the explicitly constructed univariate ring
`QQ[coord_x_only]`.  It is rejected if zero and checked to have degree `16`
before line 366 (`:358-364`).  The receiver of `.radical()` is therefore a
rational univariate polynomial, not an integer; squarefreeness of any large
integer coefficient is irrelevant because every nonzero rational is a unit.

An exact independent factorization is

```text
Res_y(F,F_y)
 = -2^108 * 3^9 * x^8
   * (3^9*x^8 + 2^24*5*43*x^4 + 2^47).
```

The octic factor is coprime to its derivative and has nonzero constant term.
Consequently its polynomial radical is, up to a rational unit,

```text
x * (3^9*x^8 + 2^24*5*43*x^4 + 2^47),
```

of degree `9`, exactly the degree and support shape banked in frozen JSON lines
14–17.  The old “divide by a maximal square” `squarefree_part()` semantics would
discard the even-multiplicity factor `x^8`, leave degree `8`, and trip the
assertion at `box/bmfact_962.sage:368-373`.  The banked degree `9` is therefore
also a positive witness that the patched radical semantics were used.

Nothing else consumes squarefree semantics.  `disc_squarefree` is used only for
its degree at line 367, that degree is checked and serialized at lines 368–373
and 395, and the polynomial is serialized diagnostically at line 398.  Degree
`16` and valuation `8` are computed from the original discriminant, not its
radical (`:360`, `:374-380`).  `run_monodromy` receives `poly_F`, not
`disc_squarefree`, and `bmfact_enum.py` never reads either squarefree JSON field.
Running this `.sage` source through the Sage preparser changes no part of that
typing or dataflow.

### 1.3 Charged census passes; generic census validation is not fail-closed

The charged output is genuinely the expected census.  Its eight tangency
records have transposition strand permutations and CPF alpha exponent `1`; the
node factor has exponent `8` and identity strand permutation (frozen JSON lines
1517–1539).  Its four CPF alpha words are actual squares `[6,6]`, `[4,4]`,
`[6,6]`, `[6,6]` (lines 1825–1929).  Transporting their supports by the recorded
conjugators gives the four disjoint pairs

```text
{6,7}, {2,8}, {1,9}, {3,5},
```

leaving internal strand `4`.  Sage's CPF contract says these conjugates commute
and multiply to the input factor.  The actual factorization is therefore eight
half-twists plus one fibre containing four commuting squares, with total
exponent `8*1+4*2=16`.

There is a latent fail-open in the reusable checker.  `classify_factor()` can
return suffix states such as `tangency_cpf_missing`,
`tangency_cpf_unexpected`, `node_fibre_unsplit`, or
`node_fibre_cpf_unexpected` (`box/bmfact_962.sage:475-506`), but the census counts
every label beginning with `tangency` or `node_fibre` and counts only the literal
`other` as bad (`:682-719`).  A degraded suffix could therefore reach
`CENSUS-OK`.  Also, the nominal node branch checks four exponent sums, not that
each alpha word is `[k,k]`.  The frozen classes and words are the exact good
ones, so this cannot change the charged decision; future emitters should demand
exact labels and exact square shapes.

### 1.4 `free_auto_F9` is wrong metadata, but is not on the decision path

This audit found one material diagnostic defect.  The single-letter Fox/Artin
substitutions in `apply_artin_letter_to_word()` are right
(`box/bmfact_962.sage:169-212`), but `artin_auto_images()` processes a multi-letter
Tietze word from right to left (`:215-230`).  Sage's mapping-class action on the
free group is a **right** action: `x*(uv)=(x*u)*v`, so free words must be
substituted left to right.  See the official
[Sage mapping-class action](https://doc.sagemath.org/html/en/reference/groups/sage/groups/braid.html#sage.groups.braid.MappingClassGroupAction)
and the [ZvK relation documentation](https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html#sage.schemes.curves.zariski_vankampen.braid2rels).

For the hand-sized word `B([1,2])=sigma_1 sigma_2`, Sage's right action is

```text
x1 |-> x1 x2 x3 x2^-1 x1^-1,
x2 |-> x1,
x3 |-> x2.
```

The emitter instead records

```text
x1 |-> x1 x2 x1^-1,
x2 |-> x1 x3 x1^-1,
x3 |-> x1.
```

All nine charged factor fields and the product `free_auto_F9` field have this
reversed composition.  They must not be cited as the Sage free automorphisms.

This does **not** reach the kill.  `bmfact_enum.py` consumes only each raw
`tietze` list (`box/bmfact_enum.py:807-868`); `free_auto_F9` is never read.  More
importantly, evaluation on representation tuples reverses the free-action
composition, so the enumerator's right-to-left tuple action is the correct dual,
as the next section proves.  Repair the emitter diagnostic and its B6 prose;
neither SIROCCO nor the native enumeration needs to be rerun.

## 2. Audit of `bmfact_enum.py`

### 2.1 Fox/Artin and Hurwitz convention, including a hand check

Permutations are stored by images, and `compose_perm(first,second)` implements
`first o second` (`box/bmfact_enum.py:79-108`).  Endpoint relabeling in
`apply_perm_to_transposition` is therefore conjugation.  For adjacent tuple
entries `(a,b)`, the positive branch at lines 246–251 computes

```text
(a b a^-1, a),
```

and the negative branch at lines 252–257 computes

```text
(b, b^-1 a b).
```

These are mutually inverse Hurwitz moves and are exactly dual to
`x_i |-> x_i x_{i+1} x_i^-1`, `x_{i+1} |-> x_i`.  Transpositions being
involutions only simplifies the conjugations; it does not change their order.

For a multi-letter Sage word, `hurwitz_tietze()` applies the rightmost letter
first (`:261-271`).  This is correct, not the same bug as the emitter metadata.
If `A_b` is Sage's free-group right action and `H_b` is evaluation on a tuple,
then

```text
A_(uv) = A_v o A_u,       H_(uv) = H_u o H_v.
```

Take the explicit tuple

```text
T = ((1 2),(2 3),(3 4))
```

and the word `[1,2]`.  Direct evaluation of the three free words displayed in
§1.4 gives

```text
((1 2)(2 3)(3 4)(2 3)(1 2), (1 2), (2 3))
  = ((1 4),(1 2),(2 3)).
```

The enumerator first applies `H_2` and then `H_1` and gives the same result.  Its
inverse move restores the original tuple.  I also checked all `216`
transposition triples: positive/inverse recovery and the braid relation
`H_1 H_2 H_1 = H_2 H_1 H_2` had no failure.  An independent free-word evaluator
using Sage's left-to-right right action agreed with `hurwitz_tietze()` on 1,800
deterministic samples across all nine charged words; mismatches were zero.  By
contrast, the banked `free_auto_F9` diagnostics disagreed on 1,740 of those
samples, as expected from their composition defect.

ZvK imposes `x_j = x_j*b` for every fibre generator and each returned local
braid.  Evaluating these relations in `S_4` is exactly `H_b(T)=T`.  Thus the
fixed-set predicate at `box/bmfact_enum.py:274-275` has the correct direction
and convention.

### 2.2 The generating test is exactly `image=S_4` and transitive

`tuple_generates_s4()` builds the graph on `{1,2,3,4}` whose edges are the
transposition supports and tests connectedness (`box/bmfact_enum.py:177-202`).
For a set of transpositions, the generated subgroup is the direct product of
the full symmetric groups on the connected components of this graph.  Therefore

```text
graph connected
 <=> generated subgroup is S_4
 <=> the generated subgroup is transitive on {1,2,3,4}.
```

The requested test “`im=S_4` AND transitive” is consequently redundant but
exactly satisfied.  It is neither a weaker transitivity-only test nor an order
heuristic.  Every caller in the native run supplies only members of the explicit
six-element transposition list at lines 60–67.

### 2.3 Full-universe coverage and pruning safety

`brute_sage_native()` constructs all nine local words, then iterates over
`iproduct(TRANSPOSITIONS, repeat=9)` (`box/bmfact_enum.py:847-880`).  This is the
entire set of `6^9=10,077,696` labelled assignments.  It applies no REP class
filter, BLOCK/tube identification, product filter, conjugacy quotient, or
generation filter before the local equations.  Generation is tested only after
a tuple has passed every word (`:881-885`).

The only “pruning” is a `break` after an exact failed fixedness predicate.  Every
predicate is evaluated on the original immutable `nine`; no partial tuple is
completed heuristically.  A survivor, by definition, cannot fail any predicate,
so this short-circuit cannot drop one.  Reordering the predicates changes only
runtime, and the intersection is independent of that order.  All nine charged
Tietze lists are nonempty, with lengths

```text
25, 75, 91, 136, 43, 109, 93, 39, 17.
```

As an independent replay, I tested all `10,077,696` assignments with those same
nine frozen words, sorting only the predicate order by word length.  The replay
finished with exactly six fixed tuples and zero generating tuples.  This
reproduces the banked `6/0` without using the six REP classes.

## 3. The six fixed non-generating tuples

The frozen log reports the number six but serializes only generating survivors;
`survivors_verbatim=[]` at log lines 248–254 is **not** a list of all fixed
tuples.  The six can nevertheless be extracted uniquely from the charged count
and action.  If all nine entries equal a transposition `tau`, both elementary
Hurwitz moves leave each adjacent pair fixed:

```text
(tau,tau) |-> (tau*tau*tau^-1,tau) = (tau,tau),
(tau,tau) |-> (tau,tau^-1*tau*tau) = (tau,tau).
```

Hence `tau^9` is fixed by every braid word for each of the six transpositions.
The exhaustive banked count is six, so there can be no other fixed tuple.  The
full replay above independently printed exactly these six.

| Fixed tuple `T` | Exact image | Orbits on `{1,2,3,4}` | Result |
|---|---|---|---|
| `((1 2),...,(1 2))` (9 entries) | `{e,(1 2)} ~= C_2` | `{1,2} | {3} | {4}` | not transitive; not `S_4` |
| `((1 3),...,(1 3))` | `{e,(1 3)} ~= C_2` | `{1,3} | {2} | {4}` | not transitive; not `S_4` |
| `((1 4),...,(1 4))` | `{e,(1 4)} ~= C_2` | `{1,4} | {2} | {3}` | not transitive; not `S_4` |
| `((2 3),...,(2 3))` | `{e,(2 3)} ~= C_2` | `{1} | {2,3} | {4}` | not transitive; not `S_4` |
| `((2 4),...,(2 4))` | `{e,(2 4)} ~= C_2` | `{1} | {2,4} | {3}` | not transitive; not `S_4` |
| `((3 4),...,(3 4))` | `{e,(3 4)} ~= C_2` | `{1} | {2} | {3,4}` | not transitive; not `S_4` |

Thus the curve does carry these six non-surjective `C_2`-valued homomorphisms.
The verdict is not “no representations”; it is “no REP-96-admissible full-image
representation.”  Future runners should serialize every fixed tuple and its
generated subgroup, not only generating survivors, so this deduction need not
be reconstructed from a count.

## 4. REP-96 licenses exactly the native requirement

REP-96 does not ask for an arbitrary map to `S_4`.  Its CABLE-3 theorem assumes
explicitly a surjection

```text
phi : pi_1(C^2-D) ->> S_4
```

sending every meridian to a transposition (frozen REP-96 lines 285–300).  Its
full-factorization fork says a representation exists only when the nine-tuple is
fixed by **every** local braid, not merely by their product (lines 607–616), and
its scope block repeats that product-fixedness alone is insufficient (lines
740–750).  Those are precisely the three native conditions:

1. `T` lies in `Transp(S_4)^9`;
2. `H_beta(T)=T` for every one of the nine returned factors;
3. the entries generate `S_4` (equivalently here, act transitively).

The native run searches a superset of the six product-level classes and then
intersects all local fixed sets.  Its conclusion therefore does not depend on
REP-96's adjacent-block embedding, a split of `iota`, identification of a
leftover `tau`, or a tube-to-strand map.  Those OPENs matter to BLOCK diagnostics,
not to the native zero.

The unqualified phrase “no transitive `S_4` representation” must retain this
REP-96 transposition-meridian scope.  The computation does not exclude a
surjection whose generic meridian has another cycle type.  Within REP-96, the
scope is exact: surjectivity onto `S_4` already implies transitivity, and for
transposition generators transitivity conversely forces the full `S_4` image.

## 5. Independent derivation of the product-only count `144`

Frozen REP-96 lines 493–500 list six simultaneous-conjugacy representatives:
two `noncst-T` representatives and four `noncst-4c` representatives.  The count
can be recovered without trusting the enumerator's expansion.

For the two `noncst-T` representatives,

```text
X=(3 4),  Y=(2 3).
```

They generate the copy of `S_3` on `{2,3,4}`.  An element of `S_4` centralizing
both must preserve the unique fixed point `1` and lie in the center of that
`S_3`, hence is the identity.  Each representative therefore has trivial
simultaneous stabilizer and a conjugacy orbit of size `|S_4|=24`.

For each `noncst-4c` representative,

```text
X=(1 2 3 4),  Y=(1 2 4 3).
```

These generate `S_4`; their common centralizer is its trivial center.  Each of
the four representatives again has orbit size `24`.  The two strata cannot
meet because conjugation preserves the cycle type of `X`.  Within a stratum,
the displayed `T_1` representatives cannot meet because any conjugator fixing
the common displayed `(X,Y)` would lie in the already-trivial centralizer.
Thus the six orbits are distinct and

```text
2*24 + 4*24 = 48 + 96 = 144.
```

REP-96 verifies full image on these classes (lines 506–509).  The frozen log's
class expansion and BLOCK product control report `144` (lines 62–64 and
180–189), while the independent native product scan finds exactly `144`
generating tuples among `246` product-fixed tuples, in both orientations (lines
256–270).  The extra `102` are non-generating and do not contradict the class
count, which counts full-image tuples.  The inverse equality is also forced by
the fixed-set lemma below, so it is a useful consistency observation rather
than independent evidence for orientation.

## 6. Convention, inversion, and base-point invariance

Let

```text
Omega = Transp(S_4)^9,
H_b   = the Hurwitz bijection of Omega induced by b in B_9,
R(B)  = {T in Omega : H_b(T)=T for every local factor b in B}.
```

Every elementary Hurwitz move is invertible, preserves transposition cycle
type, and preserves the subgroup generated by the tuple entries.  These facts
give the required invariance, not just a numerical coincidence.

### 6.1 Target conjugacy and strand relabeling

For `g in S_4`, simultaneous target relabeling

```text
C_g(T)_i = g T_i g^-1
```

commutes with every Hurwitz word.  It bijects `R(B)` with itself and conjugates,
hence preserves, the image subgroup.  Zero/nonzero and full-image status are
independent of target letter names.

A change of the fibre's geometric basis or strand numbering is represented by
an Artin braid `a` (a braid lift exists for every strand permutation).  The
factors become simultaneously conjugate, say `b' = a b a^-1`, and

```text
Fix(H_b') = H_a(Fix(H_b)).
```

The map `H_a` is a bijection of `Omega` and preserves the generated subgroup,
so it bijects the full intersections and their generating parts.  This covers
strand relabeling as well as transport between fibre base points.

A change of the geometric basis of loops in the discriminant complement can
also perform Hurwitz moves on the ordered list of local factors.  Such a move
replaces two generators by conjugate/product combinations but leaves the
subgroup they generate unchanged.  A point is fixed by a generating set iff it
is fixed by the subgroup it generates.  Consequently the common fixed set is
unchanged; the order in which local factors are listed is immaterial.

### 6.2 Inversion — proof covering the absent inverse-full run

For every braid `b`,

```text
H_(b^-1) = H_b^-1.
```

For any bijection `f`, `f(T)=T` iff `f^-1(T)=T`.  Therefore

```text
Fix(H_b) = Fix(H_(b^-1))
```

**pointwise**, for each local factor.  Replacing all factors by their group
inverses gives exactly the same intersection `R(B)`, not merely one of equal
cardinality.  Reversing their list changes nothing about an intersection.
`inverse_tietze()` correctly reverses and negates a word
(`box/bmfact_enum.py:278-279`).

**NO INVERSE-FULL RUN IS REQUIRED.**  It would return the same six constant
fixed tuples and the same zero generating tuples.  This proves the inversion
variant actually at issue—group inversion of the returned factors.  It is not
a license to replace the Artin action by an arbitrary erroneous convention;
the correct Sage/Fox convention was checked separately in §2.1.

### 6.3 The absent base point

The Sage 10.9 call returned the documented four-tuple, so the JSON has
`base_point=null` and no ordered root list (frozen JSON lines 28–31).
`bmfact_962.sage:580-605` uses a returned fifth slot only to serialize root
names; the raw braid words were already computed in one coherent internal
`B_9` basis.  `bmfact_enum.py:1041-1050` merely copies this metadata, while the
native decision consumes the words and all labelled tuples.

Moving or revealing the base point transports the fibre basis by a braid and
is covered by §6.1.  Because the universe contains every labelled assignment,
an unknown permutation or Artin transport cannot create a survivor.  Therefore

```text
OPEN[BMFACT-BASEPOINT] is CLOSED for the zero/nonzero decision.
OPEN[BMFACT-BASEPOINT-LABELING] remains OPEN for physical branch, tube, and tau labels.
```

The internal CPF calculation identifies strand `4` as the node-fibre leftover,
but the current `node_fibre_leftover_strand()` returns null: it adds raw alpha
supports before also adding their transported supports
(`box/bmfact_enum.py:760-804`).  That helper feeds only optional BLOCK/`tau`
metadata and no native filter.  Fix it before making a physical `tau` claim;
it does not affect the kill.

## 7. Repairs and disposition of prior OPENs

The following repairs are required for a clean reusable instrument but are not
preconditions for this verdict.

| ID | Repair | Effect on charged kill |
|---|---|---|
| `R-AUTO` | Process free words left-to-right in `artin_auto_images()`, rewrite B6 to distinguish Sage's right free action from the dual tuple action, and regenerate or quarantine every `free_auto_F9` field. | None: native reads raw `tietze`; its dual action is correct. |
| `R-CENSUS` | Fail closed on exact class labels and require node alpha words `[k,k]`; separately prove reduced nodality rather than inferring it from scheme length. | None: charged labels, CPF squares, and exact curve all pass. |
| `R-FIXED-TRACE` | Serialize all fixed tuples, generated subgroup order/elements, and orbits, not only generating survivors. | None: count plus the six universal constant tuples already determines the list, and full replay confirms it. |
| `R-LABEL` | Correct transported-support bookkeeping in `node_fibre_leftover_strand()` and rename the base-point OPEN as labeling-only. | None: helper is not a native predicate. |
| `R-SCOPE` | State “surjective transposition-meridian `S_4` representation,” not an unrestricted ban on all maps to `S_4`. | Narrows prose to exactly the searched and REP-96-licensed set. |

Disposition of the live labels:

```text
OPEN[REP-96-BM-FACTORISATION]     CLOSED NEGATIVE for this realized curve.
OPEN[BMFACT-ORIENTATION]          CLOSED for full fixedness by Fix(b)=Fix(b^-1).
OPEN[BMFACT-BASEPOINT]            CLOSED for decision; retained as LABELING only.
OPEN[BMFACT-STRAND-VS-BLOCK]      IRRELEVANT to the native decision.
OPEN[BMFACT-IOTA-SPLIT]           IRRELEVANT to the native decision.
OPEN[BMFACT-TUBE-EMBEDDING]       IRRELEVANT to the native decision.
```

The BLOCK `0/0` results remain corroborative controls.  They are not promoted
as the reason for the kill, because their adjacent-block identification carries
the very OPENs that the complete native universe avoids.

## 8. Final gate and FALLACY-v2 audit

The full native intersection is exhaustive at the exact REP-96 type, its action
matches Sage's Fox/Artin convention, its short-circuit cannot discard a
survivor, and its six fixed points all have image `C_2`.  The independent class
orbit calculation recovers the product-only `144`.  Conjugacy, source-basis
transport, target relabeling, factor-basis Hurwitz moves, and group inversion
all preserve the decision.  The base-point absence is labeling-only.

Accordingly:

```text
BMFACT-962-KILL-REVIEW = KILL-BINDING

Surviving scope:
  D is the single explicit curve parametrized by
    (p,q)=(t^9+12t^5+24t, t^6+8t^2).
  There is no phi: pi_1(C^2\D) ->> S_4 sending every meridian
  to a transposition.
  Equivalently, there is no REP-96-admissible transitive degree-four
  monodromy representation compatible with all nine banked local braids.

Not claimed:
  no homomorphism at all (six C_2 maps exist);
  no S_4 surjection with non-transposition meridians;
  no other realized curve of numerical type (9,6,2);
  no curve in the whole (9,6) row;
  an independent theorem about arbitrary Keller maps outside this gate.
```

This respects `REPRESENTATIVE != FULL_ACTUAL_EXIT`: a computation on one
realized representative cannot be promoted to row or locus coverage.  Flag,
place, series, carrier, attainment, pole, and exit-price rules are not used in
the proof.  The variable/ring map and radical receiver are explicitly typed;
the false free-automorphism diagnostic is quarantined rather than silently
consumed.  No `sat()` or raw-remainder argument occurs.  No new exit-price
assertion is made, so no `charge_basis` declaration is present.

<!-- BODY-END -->
