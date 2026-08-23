# Vertex-gap Lean semantic-fidelity review (hostile, Palomar / Lean tier)

Review target: `/Users/dc/code/math/jc2-lean/vertex-gap/`
(`Challenge.lean` 135 lines, `Solution.lean` 450, `README.md`, `formalization.yaml`, `comparator.json`).

Informal source: `/Users/dc/code/math/jc72108/paper1/main.tex`, compiled as
`paper1/main.pdf` (numbering checked against the PDF, not guessed from labels).

Compared:

| Lean | Informal source |
| --- | --- |
| `VertexGap22` | Theorem 3.4, label `thm:22` |
| `VertexGap22_swapped` | the `(P,Q) ↦ (Q,−P)` side-symmetric companion of Theorem 3.4 |
| `CornerEnumeration` | Lemma 2.2, label `lem:enum` |
| `GapConditionSideSymm` | hypothesis (ii), as already corrected in the printed Section 8 record |

This is a statement-level fidelity review. The Lean proofs were read for
whether the *declared* hypotheses/conclusions match the paper, and for
whether the extracted keys are the keys those hypotheses actually produce.
Kernel-checking `lake build` was not part of this review.

---

## VERDICT: FAITHFUL

All four Lean declarations match their informal sources. The load-bearing
near-origin inequality `i ≤ 2j` is the correct closed-half-plane translation
of the Newton-polygon geometry of `N(Q)` at type `(2,2)`; dropping it would
admit the extra lattice point `(1,0)` and silently *change the theorem*
(the gap keys pick up an extra monomial and the gap kill fails). No support
inequality present in the paper geometry is missing from the Lean
hypotheses. The conclusion is the variety-level statement of Theorem 3.4,
not the scheme-level radical refinement of Remark 3.5. Challenge and
Solution declare identical names and types. The README / yaml scope
boundary (radical refinement, Props 3.2–3.3, Sections 4–8 not formalized)
is accurate. Divergences that exist are disclosed and are strengthenings or
harmless renderings, not weakenings.

No HIGH or MEDIUM defects. LOW documentation nits are recorded at the end;
none of them changes a theorem.

---

## Independent recomputation of the support conditions

Everything in this section is recomputed from Definition 2.1, Lemma 2.2,
the label-normalization paragraph, and the motivating quadrilateral, *not*
copied from the Lean comments.

### Weight, type `(2,2)`, corners

Direction `d = (1,2)`, weight `w(i,j) = 2i − j`. Vertex normalization (i)
plus Lemma 2.2 give `{p₀, q₀} = {(1,0), (k,1)}`. After the paper's label
normalization `p₀ = (1,0)`, `q₀ = (k,1)` at `k = 2`:

- `w_P = w(1,0) = 2`
- `w_Q = w(2,1) = 3`

So the weight bands are

- `supp P ⊆ { (i,j) ∈ ℕ² : 0 ≤ 2i − j ≤ 2 }`
- `supp Q ⊆ { (i,j) ∈ ℕ² : 0 ≤ 2i − j ≤ 3 }`

Unfolded as lattice inequalities (no subtraction, so no `ℕ` underflow):

- `P`: `j ≤ 2i` and `2i ≤ j + 2`
- `Q`: `j ≤ 2i` and `2i ≤ j + 3`

These are exactly Lean `hP` and the first two conjuncts of Lean `hQ`.

The top-edge condition “`w = 0` lies on `ℝd` through the origin” is the
closed inequality `j ≤ 2i`. The parallel bottom of `P` through `p₀ = (1,0)`
is `w = 2`. The parallel bottom of `Q` through `q₀ = (2,1)` is `w = 3`.
(S3) “no `y`-axis support except possibly the origin” is the same pair of
inequalities at `i = 0`: they force `j = 0` on both sides.

### The near-origin edge is *not* the parallel bottom

(S2) says the *parallel* bottom edges run in direction `d`. Separately, a
strip polygon whose top edge starts at the origin and whose bottom corner
is `q₀ = (2,1)` is closed on the origin side by the segment `(0,0)—(2,1)`.
The paper’s own prose at hypothesis (ii) calls this segment “the bottom
edge of `N(Q)`” (a terminology collision with (S2), but the geometry is
unambiguous): gap-column points at `x = g` are `(g,y)` with
`1 ≤ y ≤ d₂ g`, strictly above that segment.

The line through `(0,0)` and `(2,1)` is `x = 2y`. The closed half-plane
containing the strip (the side *above* the segment, in the usual
`(x,y)`-plane) is `y ≥ x/2`, i.e. **`i ≤ 2j`**.

The motivating quadrilateral confirms it:
`N(Q) = hull{(0,0),(2,1),(12,21),(12,24)}`.

- `(1,1)`: on the origin side of the hull, `1 ≤ 2·1`, in.
- `(1,0)`: below `(0,0)—(2,1)` (`y = 0 < 1/2`), out.
- `(2,1)`: the corner itself, `2 ≤ 2·1`, on the line, in.

### `i ≤ 2j` is load-bearing, and it is the *only* extra lattice cut at `(2,2)`

Inside the first-quadrant weight band `0 ≤ 2i − j ≤ 3`, the inequality
`i ≤ 2j` excludes exactly one point: **`(1,0)`**.

- Column `i = 1`: band points `(1,0),(1,1),(1,2)`; `i ≤ 2j` drops `(1,0)`.
- Column `i ≥ 2`: the parallel bottom `j ≥ 2i − 3` already lies on or
  above `j ≥ i/2`, so `i ≤ 2j` is redundant there.

Without `i ≤ 2j`, the vertex key `E_{(3,1)}` is still `a_{(1,0)} b_{(2,1)}`
(the competing pair `(2,1)_P + (1,0)_Q` is killed by `P`’s band: `w(2,1) = 3 > 2`).
The *gap* key `E_{(2,1)}` is not:

```
E_{(2,1)} = det((1,0),(1,1)) a_{(1,0)} b_{(1,1)}
          + det((1,1),(1,0)) a_{(1,1)} b_{(1,0)}
          = a₁ β₁ − a₂ b_{(1,0)}
```

The paper’s displayed gap kill `E_{(2,1)} = a₁ b_{(1,1)}` holds only after
`(1,0)` is forbidden as a `Q`-exponent. That is why the inequality is
load-bearing, and why a missing copy of it would be a silently *different*
theorem, not a harmless relaxation.

Closed (`i ≤ 2j`) rather than strict (`i < 2j`) is mandatory: strict would
exclude the corner `q₀ = (2,1)` itself.

### `P` does not need a matching extra inequality

After normalization the near-origin edge of `N(P)` is `(0,0)—(1,0)`, the
nonnegative `x`-axis. “On or above” is `j ≥ 0`, automatic for
`MvPolynomial` exponents. Lean is right not to add an extra conjunct on
`hP`.

### Far edge / strip length

The finite motivating polygon also has a vertical far edge `x = 12`.
Theorem 3.4 explicitly allows “strips of any lengths containing the block
columns”. Omitting a far-edge bound is the paper’s own relaxation, not a
Lean gap.

### Translation table (normalized labels)

| Paper geometry | Lattice form | Lean |
| --- | --- | --- |
| `supp P` in strip `0 ≤ w ≤ 2` | `j ≤ 2i ∧ 2i ≤ j+2` | `hP` |
| `supp Q` in strip `0 ≤ w ≤ 3` | `j ≤ 2i ∧ 2i ≤ j+3` | `hQ` first two conjuncts |
| `N(Q)` on or above `(0,0)—(2,1)` | `i ≤ 2j` | `hQ` third conjunct |
| (S3) no `y`-axis except origin | `i = 0 ⇒ j = 0` | implied by the band at `i = 0` |
| (S2) saturation `a_{p₀} b_{q₀} ≠ 0` | vertex equation | *derived* from `[P,Q] = x²` |
| (i) unique Minkowski splitting of `(3,1)` | only live pair is `(1,0)+(2,1)` | *derived* from the same support |
| any strip length | no far bound | no far bound |

Every edge the paper uses is present. The two clauses Lean does *not*
assume (saturation, uniqueness) are consequences of `hP`, `hQ`, and `hJ`,
so the formal statement is stronger than the printed one, as the README
and yaml both say.

---

## 1. `VertexGap22` vs Theorem 3.4 (`thm:22`)

Compiled numbering (PDF p. 5): **Theorem 3.4**, not 3.1 or 3.5.
Section-3 counter: Lemma 3.1 gap-kill, Prop 3.2, Prop 3.3, Theorem 3.4,
Remark 3.5 radical, Remark 3.6 position, Remark 3.7 excluded primes.
The Lean / README / yaml numbering is correct.

### Hypotheses

| Item | Paper Theorem 3.4 | Lean `VertexGap22` | Finding |
| --- | --- | --- | --- |
| Ground ring | field, `char ∉ {2,3,5}` | `[Field K]`, `(2:K)≠0`, `(3:K)≠0`, `(5:K)≠0` | equivalent, for fields |
| Objects | `P, Q ∈ K[x,y]` | `MvPolynomial (Fin 2) K` with `X 0 = x`, `X 1 = y` | exact; documented |
| Shape | reduced strip pair of type `(2,2)` satisfying (i), any length containing the block columns | support in the `(2,2)` bands, plus `i ≤ 2j` on `Q` | correct translation; see recomputation |
| Bracket | `[P,Q] := P_x Q_y − P_y Q_x = x²` | `pderiv 0 P * pderiv 1 Q − pderiv 1 P * pderiv 0 Q = X 0 ^ 2` | exact Jacobian, exact RHS |
| Saturation / uniqueness | assumed via (S2) and (i) | not assumed; forced by the bracket | disclosed strengthening |

`pderiv` is the ordinary partial derivative (`coeff_pderiv` multiplies by
the source exponent). That is the same operation as the paper’s monomial
rule `[x^{p₁} y^{p₂}, x^{q₁} y^{q₂}] = det(p,q)\, x^{p₁+q₁−1} y^{p₂+q₂−1}`.
It is *not* a Hasse derivative, and the paper is not using one.

`(5:K) ≠ 0` is retained in the *statement* even though `Solution.lean`’s
cascade keeps the factor `5` on the `b₉`-pivot and never inverts `5`.
That is a printed-statement fidelity choice, not hypothesis drift: the
declaration is exactly as strong as Theorem 3.4, and the unused binder is
disclosed in the README, yaml, and the `set_option linter.unusedVariables`
on the Solution proof. Remark 3.7 claims sharpness of `{2,3,5}` only for
the paper’s own (dividing) derivation and explicitly makes no claim in
those characteristics.

Quantifiers: Lean is `∀ P Q` with the support constraints and the
polynomial identity `[P,Q] = x²`. That is the correct reading of “let
`(P,Q)` be a reduced strip pair … with `[P,Q] = x^k`”. There is no hidden
algebraically-closed / characteristic-zero / finite-length quantifier in
the paper that Lean dropped, and no extra Lean quantifier that shrinks
the class.

### Conclusion

Paper: “every solution satisfies `a₃ = 0` and `a₂² a₆ = 0` … the locus
`a₂ a₆ ≠ 0` is empty, and the block variety is contained in
`{a₃ = 0} ∩ ({a₂ = 0} ∪ {a₆ = 0})`.”

Lean:

```lean
coeff (single 0 1 + single 1 2) P = 0 ∧
  coeff (single 0 1 + single 1 1) P ^ 2 *
    coeff (single 0 2 + single 1 4) P = 0
```

Coefficient dictionary, from the paper’s own display
`a₁ = a_{(1,0)}, a₂ = a_{(1,1)}, a₃ = a_{(1,2)}, …, a₆ = a_{(2,4)}`:

| name | lattice point | monomial | Lean `Finsupp` |
| --- | --- | --- | --- |
| `a₃` | `(1,2)` | `x y²` | `single 0 1 + single 1 2` |
| `a₂` | `(1,1)` | `x y` | `single 0 1 + single 1 1` |
| `a₆` | `(2,4)` | `x² y⁴` | `single 0 2 + single 1 4` |

Exact. Over a field, `a₂² a₆ = 0` iff `a₂ = 0 ∨ a₆ = 0`, so the variety
containment is the same sentence.

This is *not* Remark 3.5. Remark 3.5 (PDF p. 6) says the chart-free form
is radical membership `u² ∈ I` with `u ∉ I`, and that “every
variety-level statement in Theorem 3.4 is unaffected.” Lean formalizes
the variety-level statement. The README / yaml correctly list the radical
refinement as out of scope.

The “in particular the generic chart `a₂ a₆ ≠ 0` is empty” clause is a
field-theoretic corollary of the conjunction Lean proves; it is docstring
commentary, not a missing extra theorem.

---

## 2. `VertexGap22_swapped` vs the `(P,Q) ↦ (Q,−P)` companion

The paper never prints a second numbered theorem. It *does* say, right
after Lemma 2.2 (PDF p. 3): if the corner `(k,1)` belongs to `P` instead,
replace `(P,Q)` by `(Q, −P)`, which has the same bracket and swaps the
roles. Section 8 records that “the gap condition must be stated
side-symmetrically,” and the printed (ii) is already the corrected form.

Lean’s swapped statement is that companion, not a silent relabelling of
Theorem 3.4:

- `P` is the *wide* strip `0 ≤ w ≤ 3` with near-origin cut `i ≤ 2j`
  (corner `(2,1)` lives here);
- `Q` is the *narrow* strip `0 ≤ w ≤ 2` (corner `(1,0)` lives here);
- same bracket `[P,Q] = x²`;
- obstruction lands on the block coefficients of `Q` (the narrow member).

The proof in `Solution.lean` is literally the paper’s normalization:
`VertexGap22` applied to `Q` and `−P`. The minus is load-bearing:
`[Q,P] = −[P,Q] = −x²`, while `[Q,−P] = [P,Q]`. Putting `i ≤ 2j` on `P`
(the wide member) and *not* on `Q` is the correct swap of the
normalized-label geometry. yaml marks this declaration
`proved (adapted: the side-symmetric companion statement)`, which is the
right status, not an overclaim that the paper prints two theorems.

---

## 3. `CornerEnumeration` vs Lemma 2.2 (`lem:enum`)

Paper (PDF p. 3): “Under (i), `{p₀, q₀} = {(1,0), (k,1)}`.”

The proof of the lemma uses only the parts of (i) that are the sum
`(k+1,1) = p₀ + q₀`, `det(p₀,q₀) = ±1`, and nonnegativity of coordinates
(`β ∈ {0,1}`). It does *not* use uniqueness of the Minkowski splitting
(uniqueness is used later, for the vertex key being a single monomial).

Lean takes exactly those used hypotheses, with `p₀, q₀ : ℕ × ℕ` supplying
nonnegativity, and concludes the same disjunction. `det` is
`p₁ q₂ − p₂ q₁` on `ℤ`, matching the paper. Allowing `k = 0` is a
disclosed no-op: the same arithmetic still yields
`{(1,0),(0,1)} = {(1,0),(k,1)}`.

This is the lemma, not a weaker substitute. Omitting the unused uniqueness
clause from the *lemma* (as opposed to from Theorem 3.4) is correct.

---

## 4. `GapConditionSideSymm` vs hypothesis (ii) / the Section 8 erratum

Printed (ii) (PDF p. 3), already in the side-symmetric form the Section 8
verification note says must be used:

> `k ≥ 2`; equivalently, by Lemma 2.2, `max((p₀)ₓ, (q₀)ₓ) ≥ 2`.

Lean: under the same hypotheses as `CornerEnumeration`,
`2 ≤ k ↔ 2 ≤ max p₀.1 q₀.1`.

That is the equivalence, not a one-sided implication, and `.1` is the
`x`-coordinate of `ℕ × ℕ`. At `k = 0` both sides are false
(`max(1,0) = 1`), so the extra `k = 0` case does not break the iff.

The declaration does *not* formalize the further prose “equivalent to the
existence of a gap column on exactly one side.” It does not claim to.
yaml locates it at hypothesis (ii) as corrected in Section 8, which is
accurate: Section 8 is a record that the correction was incorporated,
not a second, stronger statement of (ii).

---

## Hunt (1): polygon language → support inequalities

Covered by the recomputation above. Summary, hostile reading:

- `i ≤ 2j` is the correct translation of “`N(Q)` lies on or above the
  line through `(0,0)` and `q₀ = (2,1)`.”
- It is *not* a translation of the parallel bottom `w = 3` (that is
  `2i ≤ j+3`, already present).
- It is *not* an extra restriction beyond the paper: the weight band
  alone is a strictly larger set, and the extra point `(1,0)` is outside
  every strip polygon with those corners.
- Strict inequality would be wrong (it kills `q₀`).
- The opposite inequality `i ≥ 2j` would keep `(1,0)` and throw out the
  strip.
- No other lattice point in the `(2,2)` bands is missed, and no other
  paper edge is untranslated.
- On the swapped side the same cut is applied to the wide member only,
  which is the correct mirror.

A missing `i ≤ 2j` would be a real defect (weaker *and* false as a
statement about the paper’s pairs-plus-`(1,0)`). It is not missing.

---

## Hunt (2): quantifier / hypothesis drift

- **`(5:K) ≠ 0`.** Present, matching the print. Unused by the formal
  cascade; disclosed. Not drift.
- **Bracket via `pderiv`.** Ordinary Jacobian, same bilinear form as
  equation (1). RHS is the polynomial `x²`, which is the paper’s
  `E_{(3,1)} = 1` and all other `E_m = 0` packaged as one identity.
- **Normalization.** `x = X 0`, `y = X 1`; exponents
  `Finsupp.single 0 i + single 1 j ↔ xⁱ yʲ`; weight `w(i,j) = 2i − j`
  with `i` the `x`-exponent. Matches `P = ∑ a_p x^{p₁} y^{p₂}`.
- **No algebraic closure, no `CharZero`, no invertibility of `a₁,b₃`
  as extra binders.** The paper is over a general field with those three
  characteristics excluded; units are the vertex equation. Lean derives
  `a₁ b₃ = 1` from `hJ`.
- **`(Q,−P)` vs `(Q,P)`.** Sign is correct.

No drift that weakens or silently retargets the claim.

---

## Hunt (3): conclusion, and does the README bound the claim?

Yes.

Formalized, as claimed: Theorem 3.4 at polynomial level in both label
assignments; Lemma 2.2; side-symmetric (ii). Vertex equation and gap kill
derived, not assumed.

Explicitly *not* formalized, and this matches the paper’s remaining
content:

| Out of scope | Paper location | Check |
| --- | --- | --- |
| general-cell counts | Props 3.2, 3.3 | not Lean theorems |
| general-`(k,d₂)` gap kill | Lemma 3.1 | only the `(2,2)` instances, inside the proof |
| radical membership | Remark 3.5 | conclusion is variety-level `a₃ = 0 ∧ a₂² a₆ = 0` |
| `(2,3)` / `(2,4)` / `k ≥ 3` | Section 4 | absent |
| `(8,28)` ten-event chain | Section 5 | absent |
| log-residue functional / `thm:R` | Section 6 | absent |
| GGHV chart reduction and `(72,108)` | Sections 7–8 | absent |

The README / yaml sentence that Theorem 3.4 “is the mechanism that
discards the generic chart of the `(8,28)` subcase” is a description of
the *informal* theorem’s role in the paper (PDF p. 5 and p. 14), not a
claim that the GGHV application is a Lean theorem. `status.scope` and the
README “What is / is not formalized” list both say the application is
out. That is the correct bound.

---

## Hunt (4): comparator soundness and yaml overclaim

### Challenge vs Solution

The four `theorem … :=` declarations are character-identical across
`Challenge.lean` and `Solution.lean` (checked by extracting each block
through `:=`):

- `CornerEnumeration`
- `GapConditionSideSymm`
- `VertexGap22`
- `VertexGap22_swapped`

Same names, binders, typeclasses, hypotheses, and conclusions. Solution
wraps helpers in `namespace JC72108.VertexGap` and closes it *before* the
four public theorems, so they live at root as in Challenge. The
`set_option` lines above Solution’s `VertexGap22` do not change the type.
`comparator.json` lists exactly these four names, no definitions, and the
three permitted axioms. Comparator-sound.

### yaml

- Source identity: Theorem 3.4 / `thm:22`, Lemma 2.2 / `lem:enum`,
  (ii) per the Section 8 record. Numbering matches the compiled PDF.
- `relationship: formalizes` is scoped by `location` and `note` to those
  pieces, not to the whole paper.
- GGHV is `background`, with an explicit note that the Lean theorems are
  unconditional and do not inherit Proposition 4.3. Matches the paper
  (PDF p. 14: “The theorems of Sections 3 and 4 are unconditional …
  only their application to `(72,108)` inherits the dependency”).
- `status.scope` lists the same out-of-scope items as the README.
- Fidelity divergences (1)–(6) are the actual divergences, and they are
  described accurately (`i ≤ 2j` made explicit; saturation derived;
  `(5:K)≠0` unused by the proof; variety-level conclusion; `k = 0`
  allowed in the lemma).
- Sibling pointer `jc72108-theorem-a` exists at
  `/Users/dc/code/math/jc2-lean/theorem-a/`.

No mathematical overclaim. One wording nit is below.

---

## LOW nits (not defects; no change to the verdict)

**LOW — yaml `sources.note` says `CornerEnumeration` is Lemma 2.2
“verbatim”.** The same file’s `fidelity.divergences` (6) already says the
declaration is for all `k : ℕ` (paper context `k ≥ 1`) and omits the
unused uniqueness clause of (i). “Verbatim” is therefore a one-word
overstatement *inside a note that also explains the extensions*. It does
not change the alignment entry, which is precise. Fix if touching the
file: replace “verbatim” by “the arithmetic content of Lemma 2.2 (sum and
`det = ±1`; uniqueness of (i) unused by the lemma and omitted).”

**LOW — `project.description` leads with the `(8,28)` / `(72,108)`
role.** A reader who stops at the first yaml paragraph could think the
GGHV application is in the Lean artifact. `status.scope` and the README
correct this. Not a statement-level infidelity. Fix if touching the file:
one clause in `project.description` that the application itself is not
formalized here.

Neither nit is a Palomar-blocking defect. Neither is a missing inequality,
a drifted quantifier, a scheme/variety swap, or a Challenge/Solution
mismatch.

---

## What was checked that could have been a defect, and is not

1. Off-by-one on the band (`2i ≤ j+1` or `j+3` on `P`) — would drop or
   add a block coefficient (`a₃`/`a₆` or the illegal `(2,1)` on `P`).
   The bounds are `+2` on `P` and `+3` on `Q`.
2. Strict near-origin cut `i < 2j` — would exclude `q₀ = (2,1)`.
3. Near-origin cut placed on the narrow member instead of the wide one,
   or on both, or on neither. Normalized: on `Q`. Swapped: on `P`.
4. Jacobian sign `[Q,P]` instead of `[Q,−P]` in the companion.
5. Conclusion coefficients on the wrong polynomial in the swapped
   statement.
6. Conclusion at scheme level (`u² ∈ I`) advertised as Theorem 3.4.
7. Theorem 3.4 misidentified as 3.5 / 6.x (the numbering trap from the
   sibling `theorem-a` review). It is 3.4 in this compilation.
8. `char 0` silently replacing `char ∉ {2,3,5}`, or dropping `5` from
   the *statement* while still citing Theorem 3.4 as printed.
9. `Fin 2` index swap (`X 0 = y`).
10. Challenge/Solution type drift around the unused `h5` binder.

None of these is present.
