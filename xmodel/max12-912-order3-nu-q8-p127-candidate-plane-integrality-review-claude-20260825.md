# Hostile review: geometric integrality of the pinned candidate plane curve `H(w,v)` over `F_127`

Date: 2026-08-25
Reviewer: independent hostile algebraic-geometry / computational-algebra referee
(Claude; different model from the producer lane).
Target claim: `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
Case: `cases/max12_912_order3_nu_q8_p127_candidate_plane_integrality_aws_20260825/`
Verdict: **CONFIRMED** — no source, custody, or mathematical defect requiring
repair; optional hardenings in §9.

This review closes the "hostile different-model review required" status line
carried by the producer report, and the corresponding gap recorded as part of
finding R1 of
`xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-review-claude-20260825.md`
(for this producer only; the full-contact-Jacobian producer remains unreviewed).

## 0. Execution-environment disclosure

This review session has **no Bash, no CAS, and no network access**. I could
not execute Singular or Python, and I could not recompute any SHA-256.
Consequently the verdict rests on two explicitly separated tiers:

- **Hand-verified this session (independent of the producer):** every line of
  `generate.py`, `audit.py`, `run_remote.sh`; a full structural census of all
  8,893 lines of the pinned `interpolation_candidate.json`; 30 modular
  re-derivations of emitted specialization coefficients (including four exact
  vanishings); the proper-subset-sum arithmetic; and the complete mathematical
  argument of §§5–6 below, reproved from scratch.
- **Trusted from the frozen fail-closed attestation web (not re-executed):**
  the two Singular factorizations, the two gcd-squarefreeness values, the two
  point evaluations `H(71,50)`, `H_v(71,50)`, and all hash equalities
  (`run.meta`, `MANIFEST.sha256`, `FREEZE.txt`, report §4), which are mutually
  consistent to the byte across four documents. Singular 4.3.2 `factorize`
  over `Z/127[v]` is mature engine territory; residual engine trust and the
  single-host (Box02) replay are disclosed, not eliminated.

## 1. Files read (complete, read-only)

- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
- All fifteen files of the case:
  `README.md`, `generate.py`, `audit.py`, `run_remote.sh`, `REGISTRATION.md`,
  `MANIFEST.sha256`, `FREEZE.txt`, `aws/run.meta`, `aws/input.sing`,
  `aws/result.out`, `aws/audit.json`, `aws/audit.out`, `aws/stderr.log`,
  `aws/audit.stderr`, `aws/generator.stderr` (the last three verified empty,
  matching the empty-input SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
- The pinned candidate source, in full (8,893 lines):
  `cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json`
- Supplementary provenance:
  `cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/README.md`
  and a repo-wide search for the candidate SHA and for errata naming this case
  (none exist).

## 2. Exact claim under audit

Let `H(w,v) ∈ F_127[w,v]` be the polynomial defined by the
`nonzero_support` table of the JSON of SHA
`9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce`, under the
convention `nonzero_support[d] = [[e,c],...]` meaning the coefficient of
`v^d` is `Σ c·w^e` over `F_127`. Claimed: `H` is monic in `v` of `v`-degree
190, irreducible in `F_127(w)[v]`, and the affine plane curve `H = 0` is
geometrically integral over `F_127`. Nothing else is claimed (§7).

## 3. Item 1 — the code uses the pinned candidate and emits drift-free specializations

**3.1 Pin chain.** `generate.py` resolves
`ROOT = Path(__file__).resolve().parents[2]` (= repo root for a file at
`cases/<case>/generate.py`) and reads exactly
`cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json`,
refusing to emit a single byte unless its SHA-256 equals the hard pin
`9061...a7ce` (lines 33–35: hash first, then structural gates, then print).
The frozen `aws/run.meta` line 9 independently records `sha256sum` of that
same path on the box as `9061...a7ce`, and `generator_rc=0` with an empty
`generator.stderr` and non-empty `input.sing` proves the gate passed at run
time. The producing case's README attests the same SHA ("copied
byte-for-byte from root's AWS interpolation V6"), and four sibling cases pin
the identical value. The pin in the report §4 header matches. Coherent.

**3.2 The pinned polynomial really is monic of `v`-degree exactly 190.**
This is the one premise the runtime gates do *not* fully enforce:
`generate.py` checks `degree_v == 190` (a self-declared field) and
`nonzero_support["190"] == [[0,1]]`, but never asserts the absence of a key
above 190. A key `"191"` whose coefficient polynomial vanished at both
`w=25` and `w=47` (e.g. a multiple of `(w-25)(w-47)`) would evade every
frozen degree check and destroy the monicity premise of §5. I therefore
performed a full census of the JSON by direct reading: `nonzero_support`
contains **exactly the 191 keys "0"–"190"**, serialized in lexicographic
string order (`sort_keys` order: "0","1","10","100"–"109","11",…,"189",
"19","190","2","20",…,"99"), with every adjacency inspected — in particular
`"190": [[0,1]]` is immediately followed by `"2"`, and `"100"/"101"`,
`"20"/"21"`, …, `"98"/"99"` are adjacent, excluding any three-digit
interloper. All `w`-exponents lie in 0..21 (matching
`maximum_support_count: 21`; the `support_count_histogram` sums to 191),
and all stored coefficients lie in 1..126. So `H` is monic in `v` with
*constant* leading coefficient 1, `deg_v H = 190` exactly, `deg_w H ≤ 21`.
Premise verified against the source itself, not against metadata.

**3.3 Faithful, drift-free emission.** `specialized(payload, w0)` computes
`Σ c·w0^e mod 127` per key, skips exact zeros, and prints `c*v^d` with the
coefficient suppressed only when `c=1, d≥1` — all coefficients emitted in
0..126, so no sign or overflow issues; the term order in `input.sing` is the
JSON key order (cosmetic only; Singular re-sorts internally, so only the
`input.sing` hash depends on it — no mathematical order-drift channel
exists). I re-derived by hand, from the JSON and the power tables
`25^2≡117, 25^3≡4, …, 25^12≡2`, `47^2≡50, 47^3≡64`, `71^2≡88, 71^3≡25`
(mod 127), the following emitted coefficients and compared them with the
frozen `aws/input.sing`:

| v-deg | JSON entries `[e,c]` | w=25 | w=47 | w=71 |
|---|---|---|---|---|
| 190 | `[0,1]` | `v^190` ✓ | `v^190` ✓ | `v^190` ✓ |
| 182–189 | single `[0,c]`: 33,122,29,37,117,59,106,116 | all ✓ | all ✓ | all ✓ |
| 181 | `[0,68],[1,6]` | 91 ✓ | 96 ✓ | 113 ✓ |
| 180 | `[0,93],[1,105]` | 51 ✓ | 75 ✓ | 55 ✓ |
| 174 | `[0,96],[1,96]` | 83 ✓ | 36 ✓ | 54 ✓ |
| 173 | `[0,1],[1,93]` | 40 ✓ | 54 ✓ | **0 → term absent ✓** |
| 168 | `[0,80],[1,124],[2,19]` | 69 ✓ | **0 → term absent ✓** | 15 ✓ |
| 164 | `[0,94],[1,101],[2,96]` | 8 ✓ | 116 ✓ | 92 ✓ |
| 156 | `[0,15],[1,105],[2,43],[3,68]` | 69 ✓ | 22 ✓ | **0 → term absent ✓** |
| 76 | 13 entries, e=0..12 | **0 → term absent ✓** | (114 emitted; not hand-summed) | (102 emitted; not hand-summed) |

Sample of the zero checks: at `v^173`, `1+93·71 = 6604 = 52·127` exactly; at
`v^76`, the 13-term sum at `w=25` reduces stepwise to
`81+4+110+92+35+35+82+70+97+12+30+47+67 ≡ 0 (mod 127)`. Four independent
exact-vanishing coincidences (each of probability `1/127` under any
coefficient-drift hypothesis, jointly ≈ `4·10^-9`) plus 22 exact nonzero
matches and the constant high tail `v^182..v^189` identical across all three
specializations: **coefficient/order drift is excluded**, and the
`[exponent, coefficient]` reading of the JSON is empirically pinned (the
swapped convention already fails at `v^180`, `w=25`: `105+93·25 ≡ 17 ≠ 51`).

**3.4 Residual gap (disclosed).** I cannot hash the local JSON, so
byte-level identity of my read copy with the box's SHA-verified copy is
supported by the 30-point content check, not proven. Any future replay is
protected: a drifted local copy makes `generate.py` raise before emitting.

## 4. Item 2 — fail-closed parsing, squarefreeness, degree, and subset-sum sets

`audit.py` is genuinely fail-closed. In order: any `"   ?"` substring
(Singular's diagnostic prefix) anywhere in stdout aborts; the endpoint
marker is required; `degree_H25` and `degree_H47` must equal `"190"`
(retained degree — also structurally forced since the `v^190` coefficient of
`H` is the constant 1, so this doubles as an emission-integrity check); the
sorted factor-degree blocks must equal `[2,188]` and `[1,3,186]` exactly
(both sum to 190 ✓); the factor counts must be `2` and `3`; both
`squarefree_gcd_degree` values must be `0`; `H_71_50` must be the string
`"0"`; and `Hv_71_50` is normalized by `int(·) % 127` and must be nonzero.
`block()` int-casts every token between the begin/end markers, so any
interleaved garbage raises. The runner requires `singular_rc=0`,
`audit_rc=0`, all three stderr files empty, and an exact `status=PASS` line
before writing `rc=0`; the lane is duplicate-refusing and the tag is
sanitized. The frozen `result.out` (18 lines, each key appearing exactly
once, so the first-match `re.search` semantics is harmless here) satisfies
every gate.

Three points a hostile reader should have checked:

- **`factorize(H,1)` drops multiplicities and constants**, so the printed
  degrees are those of the *distinct* irreducible factors. The subset-sum
  argument needs the *complete* degree multiset; that is exactly what the
  two `deg(gcd(H,H'))=0` certificates supply (squarefree ⇒ every
  multiplicity is 1), and the pinned partitions summing to `190 = deg`
  cross-check completeness. Note `gcd(f,f')` of degree 0 certifies
  squarefreeness unconditionally in characteristic `p`: any repeated factor
  `q` divides both `f` and `f'` (and the degenerate `f' = 0` case would
  print gcd degree 190, failing closed). The `ideal I25=F25[1]` indirection
  is validated by the frozen output itself: `size(I25)=2, size(I47)=3` with
  per-generator degrees summing to 190 are only consistent with `I25`,
  `I47` being the distinct-irreducible-factor ideals.
- **Subset sums, recomputed by hand.** `proper_subset_sums` ranges masks
  `1 .. 2^n−2`, excluding the empty and full sets — the correct notion of
  proper nonempty sub-multiset sums. For `[2,188]`: `{2,188}`. For
  `[1,3,186]`: `{1, 3, 186, 1+3=4, 1+186=187, 3+186=189}` =
  `{1,3,4,186,187,189}`. Intersection with `{2,188}`: empty (2 and 188
  appear in neither list). Matches `audit.json` and report §2 exactly.
- **`Hv_71_50=-23` vs the advertised `104`.** Singular prints `Z/127`
  residues in the symmetric range; `-23 ≡ 104 (mod 127)`, and the audit's
  `% 127` normalization records 104. Representation difference inside an
  honest pass, not a defect.

Independent corroboration: the producing certificate JSON already records
`partition_w25=[2,188]`, `partition_w47=[1,3,186]` from root's earlier
exhaustive lane; this case recomputed them in a separate run and agreed.
(Same engine family and host class, so this is replay agreement, not
engine-independent confirmation — disclosed.)

## 5. Item 3 — the specialization argument is proved

Let `D = F_127[w]`, `K = F_127(w)`. From §3.2, `H ∈ D[v]` is monic in `v`
with `deg_v H = 190`.

**Lemma A (descent of monic factors).** If `H = A·B` in `K[v]` with `A, B`
monic, then `A, B ∈ D[v]`. *Proof.* Fix an algebraic closure `Ω` of `K` and
split `H = Π (v − r_i)` in `Ω[v]`. Each `r_i` is integral over `D` (it
satisfies the monic `H ∈ D[v]`). Since `Ω[v]` is a UFD with primes
`v − r`, the monic divisor `A` equals `Π_{i∈S} (v − r_i)` for a
sub-multiset `S`. Its coefficients are, up to sign, elementary symmetric
functions of integral elements, hence integral over `D`, and they lie in
`K`; `D = F_127[w]` is a UFD, hence integrally closed in `K`, so they lie
in `D`. ∎

**Lemma B (no degree drop).** For `c ∈ F_127`, evaluation
`ε_c : D[v] → F_127[v]`, `w ↦ c`, is a ring homomorphism, and a monic
`A ∈ D[v]` of `v`-degree `a` maps to a monic polynomial of degree exactly
`a` (its leading coefficient is the constant 1). ∎

**Theorem 1 (arithmetic irreducibility).** `H` is irreducible in `K[v]`.
*Proof.* Suppose `H = A·B` nontrivially in `K[v]`; normalize both monic
(their leading coefficients multiply to 1), so `a = deg_v A ∈ [1,189]`. By
Lemma A, `A, B ∈ D[v]`; by Lemma B, `H(25,v) = ε_25(A)·ε_25(B)` with
`deg ε_25(A) = a`, and likewise at 47. The frozen certificates give: in the
UFD `F_127[v]`, `H(25,v)` is squarefree with irreducible-degree multiset
exactly `{2,188}`, and `H(47,v)` squarefree with multiset `{1,3,186}`. By
uniqueness of factorization the multiset splits between `ε_25(A)` and
`ε_25(B)`, with both parts nonempty (`1 ≤ a ≤ 189`), so `a` is a proper
subset sum: `a ∈ {2,188}`. The same argument at 47 gives
`a ∈ {1,3,4,186,187,189}`. The sets are disjoint — contradiction. ∎

**Corollary (arithmetic integrality).** `H` is monic in `v`, hence
primitive in `D[v]`; by Gauss's lemma, Theorem 1 gives irreducibility in
`D[v] = F_127[w,v]`, so `(H)` is prime and `F_127[w,v]/(H)` is a domain:
the affine curve is integral over `F_127`. (For §6 the weaker statement
suffices: any factorization `H = G_1·G_2` in `F_127[w,v]` with both
`deg_v G_i ≥ 1` already contradicts Theorem 1 directly.)

The report's §2 wording ("factors may be taken monic … degrees therefore do
not drop … must belong simultaneously to both proper subset-sum sets … the
sets are disjoint") is exactly this argument and is **correct**.

## 6. Item 4 — arithmetic irreducibility + smooth rational point ⇒ geometric integrality: proved, with edge cases

Let `k = F_127`, `k̄` an algebraic closure. `k` is finite, hence
**perfect**, so `k̄/k` is Galois with `k̄^{Gal(k̄/k)} = k`; this is used
twice below and is the perfect-field edge case: over an imperfect base the
fixed-field step fails (and geometric reducedness of reduced schemes can
fail, e.g. `v^p − t·w^p` over `F_p(t)`), so the argument as phrased would
not survive; here it does.

**Normalization.** In `k̄[w,v]` write `H = Π_{i=1}^{r} P_i^{e_i}` with
`P_i` distinct irreducibles. Comparing leading `v`-coefficients (that of
`H` is 1), no factor can lie in `k̄[w]`: a `v`-degree-0 divisor would
divide 1. Hence every `P_i` has `deg_v P_i ≥ 1` and may be normalized
monic in `v`; the residual unit is then 1, so `H = Π P_i^{e_i}` with all
`P_i` monic in `v`. Each `σ ∈ Gal(k̄/k)` fixes `H` and permutes the
`P_i` (monicity is preserved), carrying `e_i` along.

**Step 1 (Galois transitivity — the constant-field edge case).** If the
action on `{P_1,…,P_r}` had a proper orbit `O`, then `G = Π_{i∈O} P_i^{e_i}`
and `H/G` would both be Galois-fixed, monic in `v` of positive `v`-degree,
with coefficients in `k̄^{Gal} = k` — a nontrivial factorization of `H` in
`k[w,v]` with both factors of positive `v`-degree, contradicting Theorem 1.
So Galois is transitive on the geometric components (and all `e_i` are
equal). This is precisely the case a nontrivial constant-field extension
would produce (classically: the exact constant field `k'` of the function
field embeds, via the smooth — hence normal — rational point, into its
residue field `k`, forcing `k' = k`; the component-orbit argument above is
the elementary equivalent for perfect `k`).

**Step 2 (repeated component, `r = 1, e ≥ 2`).** Three independent kills,
the first at certificate level: (i) `H = P_1^e` with `P_1` monic in `v`
gives `H(25,v) = P_1(25,v)^e` with `deg P_1(25,v) = 190/e ≥ 1`, so
`H(25,v)` would not be squarefree — contradicting the frozen
`squarefree_gcd_degree_25=0` (gcd is invariant under field extension, so
squarefreeness over `F_127` is squarefreeness over `k̄`). (ii) By Step 1's
descent, `P_1` itself is Galois-fixed, hence in `k[w,v]`, and `H = P_1^e`
contradicts Theorem 1. (iii) `∇H = e·P_1^{e−1}·∇P_1` vanishes identically
on `V(P_1) = V(H)`, contradicting `H_v(71,50) = 104 ≠ 0`. So `e = 1`: `H`
is squarefree over `k̄`. The producer report argues §3 only through
conjugate components; this non-reduced case is the one step it compresses —
the frozen certificate set nevertheless contains its refutation (kill (i)),
so this is an expository, not a mathematical, gap. See §9(H1).

**Step 3 (multiple components versus the smooth point).** Suppose `r ≥ 2`,
`H = P_1⋯P_r`. The point `x = (71,50) ∈ k^2` satisfies, per the frozen
replay, `H(x) = 0` and `H_v(x) = 104 ≠ 0`; the second is one coordinate of
the gradient, so `x` is a smooth point of the curve (Jacobian criterion —
only one nonvanishing partial is needed). Since `k̄` is a field,
`Π P_i(x) = 0` forces `P_j(x) = 0` for some `j`. For any `i`, transitivity
provides `σ` with `σ(P_j) = P_i`; applying `σ` to the equation
`P_j(x) = 0` and using that `x` is Galois-fixed (coordinates in `k`) gives
`P_i(x) = 0`. So `x` lies on **every** geometric component. Then, by the
product rule,
`H_v(x) = Σ_i (∂_v P_i)(x) · Π_{j≠i} P_j(x)`,
and each summand contains some factor `P_j(x) = 0` (a `j ≠ i` exists
because `r ≥ 2`): `H_v(x) = 0`. Contradiction with `104 ≠ 0`. Hence
`r = 1`. This makes precise the report's "would lie on every conjugate
component and would be singular".

**Conclusion.** `H` is irreducible in `k̄[w,v]` (Steps 2–3), so `(H)` is
prime there and `k̄[w,v]/(H)` is a domain: the affine plane curve `H = 0`
is **geometrically integral** over `F_127`, as claimed. (Purely for
robustness: the same conclusion also follows from the field-general fact
that an irreducible variety with a smooth rational point is geometrically
integral — a smooth connected neighborhood of a rational point is
geometrically connected and geometrically reduced, and every geometric
component of the 1-dimensional curve meets it; but over the perfect field
`F_127` the elementary Galois route above is complete on its own.)

## 7. Item 5 — standalone-plane scope enforced

The exact theorem frozen here is the integrality of the standalone explicit
`H` and nothing more. I checked every scope surface: report §5, case
README ("does **not** prove `H` belongs to the selected-Q8 quotient ideal
or that the plane curve is a quotient component"), `REGISTRATION.md`
exclusions, `FREEZE.txt` scope block, and the machine-readable
`audit.json.scope`. They agree, and no sentence in the case or report
claims quotient membership, component status, coordinate-function
rationality, Q8 contacts lying on the curve, characteristic-zero lift,
trajectory, maximum-twelve, or any JC2 conclusion. The pinned input's own
provenance disclosure ("interpolation does not bound the unreduced generic
w-degree … or prove flat specialization") is not contradicted anywhere:
this theorem consumes `H` as a pinned explicit polynomial, for which
interpolation provenance is irrelevant. Scope is exact and airtight; the
title's lane label ("Max12 (9,12) selected-Q8") is naming, not scope
leakage.

## 8. Custody web

All hash values are mutually consistent to the byte across the four
attestation surfaces I can compare (report §4, `MANIFEST.sha256`,
`FREEZE.txt`, `aws/run.meta`, plus the audit's self-reported hashes):
`generate.py ef82…c9c5`, `audit.py f75e…07b4`, `run_remote.sh 8f5d…05b0`,
`input.sing ae40…bc07`, `result.out 3e2b…6919` (also embedded inside
`audit.json` as `singular_stdout_sha256`, tying the audit payload to the
exact Singular stdout), `audit.json 0665…2ced` (also self-reported in
`audit.out`), stderr triple `e3b0…b855` (the empty-input SHA — files
verified empty). `rc=0`, `endpoint=PASS`, `generator_rc=singular_rc=audit_rc=0`,
tag and host match the report, and the sub-second wall time is plausible for
univariate degree-190 factorization over `F_127`. Two custody observations,
neither blocking: `run.meta` hashes the four sources and five outputs but
not `input.sing` (covered by `MANIFEST` and by §3.3's content tie), and this
case's `MANIFEST` does not list the cross-case pinned JSON (covered
operationally by the fail-closed SHA gate inside `generate.py` and by
`run.meta` line 9; the producing case carries no MANIFEST of its own).

## 9. Findings and smallest repairs

No defect requiring repair was found. Ranked observations with the smallest
adequate hardening for each, all optional:

- **(H1) Expository lacuna, report §3 (non-reduced case).** The written
  argument covers only the conjugate-component split; geometric
  *integrality* also requires excluding `H = G^e`, `e ≥ 2`, over `k̄`.
  The frozen `squarefree_gcd_degree_25=0` certificate already refutes it
  (§6 Step 2), so the theorem and certificate set are complete. Smallest
  repair: add one sentence to §3 — "A repeated geometric component
  `H = G^e`, `e ≥ 2`, is excluded by the `w=25` squarefreeness certificate,
  since it would force `H(25,v) = G(25,v)^e`." Non-blocking.
- **(H2) Ungated premise, `generate.py`.** The monic-degree-190 shape is
  enforced only at key `"190"`; no assert excludes support above 190 (a
  hypothetical key `"191"` with coefficient divisible by `(w−25)(w−47)`
  would evade all frozen gates and void Lemma B's premise). For the actual
  pinned source I verified by full census that no such key exists, so the
  theorem stands. Smallest repair:
  `assert max(int(k) for k in payload["nonzero_support"]) == 190`.
  Non-blocking for this frozen run; recommended for successors.
- **(H3) Custody breadth.** Add `interpolation_candidate.json` to this
  case's `MANIFEST.sha256` (or freeze the producing case) so the pinned
  input is covered by a repo-side manifest as well as by the runtime gate
  and `run.meta`. Non-blocking.

## 10. Verdict

The pinned monic degree-190 `H(w,v)` of SHA `9061…a7ce` is irreducible in
`F_127(w)[v]` and defines a geometrically integral plane curve over
`F_127`, exactly as claimed and exactly within the declared standalone
scope. The code uses the pinned source and emits drift-free
specializations (verified to 30 hand-checked coefficients including four
exact vanishings); the parsing pipeline is fail-closed at every gate; the
descent/no-drop/subset-sum argument is proved sound; and the smooth-point
upgrade to geometric integrality survives the constant-field,
repeated-component, and perfect-field edge cases, with the one compressed
write-up step independently covered by the frozen squarefreeness
certificate. Execution-environment limits (no shell/CAS/network: hashes and
CAS outputs taken from the interlocking frozen attestations) are disclosed
in §0 and do not affect the verdict.

CONFIRMED
