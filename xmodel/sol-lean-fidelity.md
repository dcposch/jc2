# Lean semantic-fidelity review

Review target: `jc72108-lean/Challenge.lean` (73 lines), compared with
`paper1/main.tex` label `thm:ode` and the characteristic-p discussion in
Section 6; also `Solution.lean`, `comparator.json`, and `formalization.yaml`.

## VERDICT: FAITHFUL at statement level; source attribution is not release-ready

Both Lean declarations faithfully encode the intended polynomial ODE rigidity
claim. `TheoremA` is a sound strengthening from fields to integral domains.
`TheoremA_charP` is also mathematically sound and specializes to the paper's
characteristic-p application bound, although it is a standalone strengthening
extracted from the argument rather than a theorem stated verbatim in the paper.
Neither declaration is weaker than advertised because of quantifiers,
constant-polynomial encoding, or degree conventions.

There are, however, several high-severity source and attribution defects. Most
importantly, the current paper's ODE result is **Theorem 6.1**, while Theorem
6.5 is a materially different block-variety theorem that is not formalized.
The cited Zenodo version also predates the ODE theorem, and the Żołądek DOI in
the YAML resolves to an unrelated article. These defects do not invalidate the
Lean mathematics, but they should be fixed before this is advertised or
registered as a formalization of the cited source.

## Question one: statement correspondence

### `TheoremA`

| Item | Informal theorem | Lean declaration | Finding |
|---|---|---|---|
| Coefficient object | A characteristic-zero field `F` (the intended setting, also used by the displayed division in the proof) | `{F} [CommRing F] [IsDomain F] [CharZero F]` | Sound strengthening to every characteristic-zero integral domain |
| Weight | Integer `ν` with `ν ≥ 1` | `(ν : ℕ) (hν : 1 ≤ ν)` | Exact: a positive integer is equivalently a natural number at least one |
| Polynomials | `A, C ∈ F[y]` | `(A C : Polynomial F)` | Exact |
| Right side | Some scalar constant `c ∈ F`, with `c ≠ 0` | `(c : F) (hc : c ≠ 0)` and RHS `Polynomial.C c` | Exact; this is a nonzero **constant**, not merely a nonzero polynomial |
| Identity | `A C′ − ν A′ C = c` | `A * derivative C - (ν : Polynomial F) * (derivative A * C) = Polynomial.C c` | Exact; the cast of `ν` is a constant polynomial |
| Conclusion | `deg A ≤ 1` | `A.natDegree ≤ 1` | Exact on the possible cases; see the degree audit below |

Making `c` an explicit universally quantified argument is logically equivalent
to the prose “for some nonzero constant `c`” premise: for every witness to that
premise, the conclusion is independent of which witness was supplied.

No explicit assumptions `A ≠ 0` and `C ≠ 0` are missing. If either polynomial
were zero, the left side would be zero, contradicting `Polynomial.C c ≠ 0`,
which follows from `hc` and the nontrivial domain.

#### Why the integral-domain generalization is sound

The paper's proof uses field division only in

`D = C - (lc(C) / lc(A)^ν) A^ν`.

Over a domain, clear that denominator and instead take

`D = lc(A)^ν C - lc(C) A^ν`.

The leading terms still cancel, while

`A D′ - ν A′ D = lc(A)^ν c ≠ 0`.

Only commutativity, nontriviality, absence of zero divisors, and
characteristic-zero injectivity of natural-number casts are used. No inverse,
factorization, algebraic closure, or perfectness assumption is needed. This is
exactly the denominator-cleared construction implemented in `Solution.lean`.
Thus `CommRing + IsDomain` is stronger than the paper's field setting, not an
unsound change.

### `TheoremA_charP`

The Lean hypotheses are exactly `ν * deg A < p` and `deg C < p`, in addition
to the same positive weight, nonzero scalar constant, ODE, and domain
hypotheses. They are sufficient: the proof only needs injectivity of
natural-number casts for `deg C`, `ν * deg A`, and then the lower degree of the
top-term-cancelled auxiliary polynomial. All lie below `p`.

The paper does **not** display this standalone theorem. Its closing Section 6
remark says that the block's rigidity half holds under the conservative bound

`p > (k + 1) d₂`.

In that application, `ν = k`, `deg A ≤ d₂`, and `deg C ≤ k d₂`; hence
`ν * deg A ≤ k d₂ < p` and `deg C ≤ k d₂ < p`. So the paper's bound implies
both Lean side conditions.

The Lean theorem is a valid, more general ODE-only result. It does not
formalize the other parts of the paper's block-level characteristic-p remark,
such as triangular pivots and bridge uniqueness; `formalization.yaml`
otherwise correctly says that the bridge and block combinatorics are out of
scope.

The absence of a separate premise saying that `p` is positive and prime is
not a weakness. `hνA` rules out `p = 0`, and an integral domain carrying a
positive `CharP F p` instance has prime characteristic; the composite and
`p = 1` cases have no such nontrivial-domain instance.

## Question two: hostile-reader / degree audit

There is no degree-convention loophole.

- Mathlib defines `natDegree 0 = 0`, whereas `Polynomial.degree 0 = ⊥`.
  The ODE with `c ≠ 0` makes `A = 0` impossible anyway.
- For `A ≠ 0`, `A.natDegree` is exactly its ordinary natural-valued degree,
  so `A.natDegree ≤ 1` says precisely that `A` is constant or linear.
- Even without using nonzeroness, both standard conventions make the
  inequality true for the zero polynomial (`0 ≤ 1` for `natDegree`, and
  `⊥ ≤ 1` for `degree`); there is no extra hostile counterexample hidden at
  `A = 0`.
- A nonzero constant `A` has degree zero and is intentionally admitted by
  `deg A ≤ 1`. A nonzero linear `A` has degree one. The conclusion does not
  assert that `A` has degree exactly one.
- The same observations apply to the characteristic-p degree bounds; `C = 0`
  is also impossible from the ODE and `c ≠ 0`.

Thus no reader can fairly claim that `natDegree` makes either Lean theorem
weaker than the advertised `deg A ≤ 1` statement.

## Comparator audit

`Challenge.lean` and `Solution.lean` have exactly the same two public theorem
names and types:

- `TheoremA`
- `TheoremA_charP`

Every binder, typeclass, hypothesis, cast, polynomial identity, and conclusion
matches; only the proof bodies differ. `comparator.json` lists exactly these
two root declarations and no definitions. `Solution.lean` elaborates cleanly.
There is no comparator defect.

## DEFECTS

### HIGH — the ODE theorem is misidentified as Theorem 6.5

Evidence:

- `paper1/main.tex:320-322`, label `thm:ode`, compiles as **Theorem 6.1
  (ODE rigidity, all weights)**.
- `paper1/main.tex:362-368`, label `thm:R`, compiles as **Theorem 6.5
  (log-residue description of the block variety)**.
- Theorem 6.5 includes the bridge, binomial locus, and residue-functional
  description. None of that theorem is formalized here.

Impact: saying that `TheoremA` formalizes “Theorem 6.5” points to a different,
substantially stronger result and can make the formalization look broader than
it is.

Exact fix: replace “Theorem 6.5” by “Theorem 6.1 (`thm:ode`)” at:

- `Challenge.lean:20` and `Challenge.lean:54`;
- `Solution.lean:11` and `Solution.lean:179`;
- `README.md:6`;
- `formalization.yaml:29`, `:38`, `:103`, `:155`, and `:164`.

Alternatively, retaining “Theorem 6.5” would require actually formalizing
`thm:R`, which the current challenge does not do.

### HIGH — DOI 10.5281/zenodo.21894922 is not the asserted theorem source

The live Zenodo record (checked 2026-08-19) is titled *Artifact for: A
Vertex-Gap Obstruction for Low-Degree Strip Pairs in the Plane Jacobian
Conjecture*, is resource type **Software**, and is MIT-licensed. The YAML
instead supplies a different title, calls it an article, and gives
`CC-BY-4.0`.

More seriously, the paper archived in that version predates `thm:ode`. It has
no Theorem A and still presents the uniform log-residue result as a conjecture.
Consequently that version cannot be the source whose “Theorem 6.5” is being
formalized.

Exact fix, preferably: archive the current `paper1/main.tex`/PDF as a new
version and cite that version-specific DOI, using its actual deposited title,
resource type, creator list, and license. Map `TheoremA` to Theorem 6.1.
Whichever primary-source route is chosen, update the stale DOI at
`Challenge.lean:20`, `README.md:5`, and `formalization.yaml:33-35`, together
with the source title/type/license at `formalization.yaml:27-44`.

An already archived alternative is DOI `10.5281/zenodo.22002825`, the
CC-BY-4.0 working paper *Sheet-number obstruction theory for the plane
Jacobian Conjecture: campaign theory bundle v1*. Its bundled `MATHIEU.md`
contains Theorem A in §5.1 and the characteristic discussion in §5.4. If that
is used, cite those locators and its actual title/type rather than calling the
result Theorem 6.5 of the paper.

If `21894922` is retained at all, its source entry should use:

- the actual “Artifact for: ...” title;
- type `software`;
- license `MIT`;
- relationship `background`, not `formalizes`.

### HIGH — the Żołądek DOI points to an unrelated article

`formalization.yaml:50-52` gives `10.1016/j.top.2007.06.003`. That DOI resolves
to Bonatti–Paoluzzi, *3-manifolds which are orbit spaces of diffeomorphisms*,
Topology 47(2), 71-100.

Exact fix:

- ID and URL: `10.1016/j.top.2008.04.001`;
- author: `Henryk Żołądek`;
- locator: `Appendix, Lemma A.7` (and, where relevant, Lemma 3.9 and equation
  (3.14)).

### MEDIUM — the characteristic-p provenance is stated too literally

`Challenge.lean:32-36` says the exact degree-data theorem is “recorded” in
Section 6, and `formalization.yaml:40-42` says it “states the paper's ...
remark with the explicit hypotheses”. The paper only records the conservative
block-level bound `p > (k+1)d₂`; it does not state the Lean theorem verbatim.

Exact fix: describe `TheoremA_charP` consistently as:

> a standalone strengthening extracted from the Section 6 proof and
> positive-characteristic remark; in the paper's application, `ν = k`,
> `deg A ≤ d₂`, and `deg C ≤ k d₂`, so `p > (k+1)d₂` implies its two
> degree hypotheses.

If literal statement alignment is required, add a small Lean wrapper with the
paper's variables and conservative bound, deriving the two existing
`TheoremA_charP` premises. Keeping the stronger theorem as an auxiliary result
is harmless.

### LOW — one further source number and prior-art wording are inaccurate

- `formalization.yaml:88` calls the block-to-ODE bridge “Lemma 6.6”; in the
  current paper it is **Lemma 6.3** (`paper1/main.tex:342`). Change `6.6` to
  `6.3`.
- The Żołądek entry should not imply that Theorem A proves his full Lemma A.7.
  The direction used here is that Lemma A.7 supplies the distinct-root case of
  Theorem A, with the remaining multiple-root case handled separately.
  `background` is a safer relationship than `independently-proves` unless the
  note explicitly states that qualification. Make the same directional fix in
  `Challenge.lean:24-29`, whose “independently proves Lemma A.7” wording is too
  strong.
- For Hermoso–Alcázar, Theorem 4 at `n = 2` forces **both** polynomials to be
  affine; “min degree ≤ 1” in `formalization.yaml:75-76` is true but needlessly
  weak. Replace it by “both polynomial degrees are at most one; in particular,
  this implies `TheoremA` for `ν = 1`.” Spell `Alcázar` with its accent.
- The YAML `location` fields should give internal locators rather than repeat
  URLs: use `Appendix, Lemma A.7`, `Theorem 4 (n = 2)`, and either `Theorem 6.1
  (thm:ode); Section 6 closing paragraph` or `MATHIEU.md §§5.1, 5.4`, depending
  on the corrected primary source.

## Bottom line

No theorem-statement or comparator change is required for mathematical
fidelity. Correct the theorem numbering and source metadata, and rephrase the
characteristic-p result as a sound extracted strengthening. After those
changes, the formalization can accurately be advertised as a faithful (and in
its coefficient-ring generality, stronger) formalization of the ODE rigidity
theorem.
