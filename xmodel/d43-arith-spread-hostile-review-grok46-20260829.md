# Hostile review: C1 denominator hole and ARITH-SPREAD repair

**UTC:** 2026-08-29
**Role:** Grok 4.6, different-model algebraic-geometry referee
**Charge:** first-principles adjudication of Fable 5's C1 correction and the
proposed `ARITH-SPREAD` limit theorems, against the original two-frame C1
chain and the charged K0-field review.
**Write set:** this file only.

No AWS, no web, no heavy CAS, no canonical-ledger edit, no commit, no push,
and no `jc2-lean` access of any kind.  Executed checks below are hashing and
bounded stdlib integer arithmetic.  No other `ideation-20260829T0002Z-*`
lane file was read.

---

## Overall

Fable's toy constant system is a genuine refutation of the original C1
*inference*, not a refutation of the D43 modular zeros.  The arithmetic
error is exact: a Bézout identity over the field `K0` is not a `P`-integral
identity, so it does not reduce to `1=0` in the residue field.  Clearing
denominators produces only a nonzero content in the finite étale order, and
a nonempty special fibre is compatible with that content vanishing at `P`.

The strongest correct *finite*-prime replacement is a divisibility statement
for the contracted content ideal, with exponent at least one at each
observed proper maximal ideal, and with the 210-free numerator of the
absolute norm divisible by the product of the residue norms.  It is not a
nonemptiness theorem, and the informal size `about 10^{5k}` is not a
theorem.

The two Chevalley limit implications, read geometrically over an irreducible
one-dimensional noetherian base, are theorems.  Several of Fable's
operational slogans are not: a single `UNIT` is not characteristic-zero
emptiness; missing `F_p`-points are not unit fibres; a uniform point-count
does not upgrade a finite `PROPER` census to a generic point; and
complete splitting is an implementation convenience, not a hypothesis of
the image argument.

A cross-prime census is a constructible-image census only of one frozen
finite-type `A_S`-scheme.  The committed modular Euler evaluator is such a
formula; the sealed exact-row packet is not yet that formula; v3 is
unnecessary for per-prime facts about a named evaluator and is necessary
for any claim that those facts are special fibres of the unsealed
exact packet or of the 155/29 22-cell.

| # | claim | verdict |
|---|---|---|
| 1 | Toy `F={105337·105673}` refutes original two-frame C1 non-unit-ideal inference | **CONFIRMED** |
| 2 | Original C1: two honest frames ⇒ `1 ∉ (F)⊗K_i` (geometric generic nonemptiness) | **REFUTED** |
| 3 | Algorithm-memo G6: an emptiness certificate with denominators in `{2,3,5,7}` cannot exist, given those two zeros | **CONFIRMED** |
| 4 | Fable C1-repaired: any K0-emptiness certificate has content whose absolute norm is divisible by `105337·105673` | **REPAIR** |
| 5 | Informal bound `N(D) ≳ 10^{5k}` as a theorem | **REFUTED** |
| 6 | Infinitely many distinct rational primes with nonempty geometric special fibres ⇒ nonempty geometric generic fibre | **CONFIRMED** |
| 7 | Infinitely many distinct rational primes with geometrically empty (unit-ideal) special fibres ⇒ empty generic fibre | **CONFIRMED** |
| 8 | One `UNIT` fibre ⇒ empty generic fibre / “char-0 emptiness” | **REFUTED** |
| 9 | Generic nonempty ⇒ all but finitely many closed points of `Spec(A_S)` have nonempty geometric fibres | **CONFIRMED** |
| 10 | Generic nonempty ⇒ all but finitely many rational primes have an `F_p`-point | **REFUTED** |
| 11 | One maximal ideal / one frame per rational prime suffices for the image argument | **CONFIRMED** |
| 12 | Complete splitting, Galois torsors, or Galois-stability of the row set are hypotheses of the limit theorems | **REFUTED** |
| 13 | Chevalley applies without flatness; vertical components are the finite-image case | **CONFIRMED** |
| 14 | v3 unnecessary for a per-prime census of a named modular evaluator | **CONFIRMED**, with the identification repair in §5 |
| 15 | Cross-prime census is a Chevalley census only of one frozen finite-type `A_S`-scheme | **CONFIRMED** |
| 16 | Uniform character-sum / point-count upgrades a finite `PROPER` list to generic nonemptiness | **REFUTED** |
| 17 | Avenue 37 (enumerating maps over `F_q`) is a different object from `ARITH-SPREAD` | **CONFIRMED** |
| 18 | Fieldness of `K0` removes the componentwise caveat on `Spec(A)` | **CONFIRMED** (by the charged K0 review) |

Maximum promotion after this review: the Chevalley dichotomy for a
finite-type scheme over the irreducible arithmetic curve `Spec(A_S)`, the
content-ideal constraint on any K0-emptiness certificate, and the two
limit theorems in geometric language.  Nothing here is a D43 point, a
22-cell decision, a template statement, an algebraization, or JC2.

---

## 0. Custody (independently recomputed)

| file | SHA-256 | match |
|---|---|---|
| `xmodel/ideation-20260829T0002Z-fable5.md` | `db51f06128d884dd80361d866c8042c1d80afff02d616f38d3334ecec7d875e9` | charge |
| `xmodel/d43-conceptual-breakthrough-primary-research-grok46-20260828.md` | `99fb7d7c21f8c0a7754f9b33354a3963520cdcb01e22df9e7ce786b74f425588` | charge |
| `xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md` (report-body seal) | `877e451f33b24b7714c712404401f11b35b6621e80400e791c4b54cfbe5078fd` | charge |

Full-file digest of the K0 review is
`07f20be55add0fea0ff6329ce0d4ca386024af33edad33254d46451fd575a94a`; the
charge is the report-body seal, and that seal replays.

From the charged K0 review, used below as theorems and not re-proved:
`K0` is one field, Galois of degree 432 over `Q`;
`A = Z[1/42][z,r,A1,A2,h]/(Phi_42, r^2-3, A1^3-(3+r), A2^3-(3-r), 2h^2-3)`
is finite étale of rank 432 over `Z[1/42]`; ramified rational primes are
exactly `{2,3,7}`; a registered frame is a degree-1 prime of `A`, and
Galois of degree 432 plus one degree-1 prime implies complete splitting.
5 is a Newton/source-denominator prime, not a ramified prime.  The emitter
constant `ETALE_LOCALIZATION_PRIMES=(2,3,5,7)` is a safe superset of the
ramified set.  Pointbanks remain `INTERNAL / UNREVIEWED / MOD-p`.  The
exact 184-row / 29-row packet is unsealed.

Coefficient ring for the D43 source formula: `A_S := A[1/5]`, equivalently
the same presentation over `Z[1/210]`.  This is the ring Fable writes as
the `S`-inverted order with `S={2,3,5,7}`.  It is a Dedekind domain with
fraction field `K0` (regular of dimension 1, because finite étale over
`Z[1/210]`).  Closed points are maximal ideals `P` with finite residue
field `κ(P)/F_p` of degree `f_P`, `p ∉ S`.

Executed integer check, not a primality test:

```text
105337 ≡ 1 (mod 168),  (105337-1)/168 = 627
105673 ≡ 1 (mod 168),  (105673-1)/168 = 629
105337 · 105673 = 11131276801
```

No unfinished peer ideation report was opened.

---

## 1. The original C1 inference is false, and the toy is a genuine refutation

### 1.1 What C1 actually asserted

Charged breakthrough note, chain C1.  Let `S={2,3,5,7}`.  Suppose a sealed
packet emits polynomials `F` in `K0[W1,W2,L,M,H]` with coefficients in the
`S`-inverted order, reducing to the committed `source_rows` evaluator at
both registered frames `p=105337` and `p=105673`, and those frames are
zeros of the reductions.  Then:

> If `1` lay in the ideal `(F)` over a factor `K_i` through which a
> registered frame factors, the same Bézout identity would reduce to
> `1=0` in `F_p`.  Therefore `1 ∉ (F)⊗K_i`, and the Nullstellensatz over
> an algebraic closure of `K_i` says `V(F)` is geometrically nonempty on
> that factor.

That is a two-frame nonemptiness lemma.  The Galois paragraph after it
is offered as a shield against reversing the arrow.  The Stop list
includes “a new denominator prime,” which already shows the author felt
denominators nearby and then failed to put them in the implication.

### 1.2 The exact denominator-clearing error

Work, as C1 must after the charged K0 review, with a field `K0` and a
maximal ideal `P` of `A_S` with `A_S/P ≅ F_p` (a registered frame).

A unit-ideal certificate over `K0` is a Bézout identity

```text
∑_i g_i f_i  =  1    in  K0[x] .
```

The cofactors `g_i` have coefficients in `K0`, not in the local ring
`(A_S)_P`.  Reduction modulo `P` is not defined on `K0`.  There is no
“same identity” in `F_p[x]`.

Clear denominators of the finitely many coefficients of the `g_i`.  There
is `0 ≠ d ∈ A_S` and `G_i ∈ A_S[x]` with

```text
∑_i G_i f_i  =  d    in  A_S[x] .
```

So `d ∈ (F) ∩ A_S`.  Reducing modulo `P` yields `d̄ ∈ (F̄)` in `κ(P)[x]`.
If `d ∉ P`, then `d̄` is a nonzero constant, hence a unit of `κ(P)[x]`,
and the special fibre is empty.  If `d ∈ P`, the reduction is `0=0` and
there is no contradiction with a nonempty special fibre.

C1's only arithmetic step is the sentence that the Bézout identity
reduces to `1=0`.  That sentence assumes the cofactors are `P`-integral.
The assumption is not supplied by “coefficients of `F` lie in `A_S`.”
Integrality of the equations is not integrality of a Nullstellensatz
certificate.  That is the hole.

The Stop phrase “a new denominator prime” would have been the correct
restriction if it had been attached to the *certificate*, as in G6 of the
seven-`W` memo.  G6 says: a char-0 emptiness certificate *with
denominators in `{2,3,5,7}`* would reduce to `1=0` at the two frames.
That is true, and is not C1.  C1 upgraded G6 from a constraint on
`S`-integral certificates to non-membership of `1` in `(F)⊗K_i`.

### 1.3 The toy

Let `N = 105337 · 105673 = 11131276801` and let `F = {N}` as a constant
polynomial in `A_S[x_1,…,x_n]` for any `n ≥ 0`, including the D43
ambient.  Hypotheses of the *inference*:

- coefficients lie in `A_S`;
- at each registered frame, `N ≡ 0`, so the reduced ideal is `(0)`, which
  is proper, and every frame point is a zero of the reduction.

Conclusion of C1: `1 ∉ (F)⊗K0`.  Actual: `N ≠ 0` in the field `K0`, so
`(N)=(1)` in `K0[x]` and `1 = (1/N)·N`.  The generic fibre is empty.  The
Bézout denominator is exactly `N`, which is not an `S`-unit, and `P`
divides `N` at both frames.

The toy does **not** reduce to `source_rows`.  It is not a D43 emptiness
claim.  It is a counterexample to the Bézout-reduction step, which is the
only step C1 uses.  A variant with a proper nonempty special fibre, not
the whole affine space, is `F={N, x}`: over `K0` the ideal is `(1)`; over
`F_p` it is `(x)`, zeros at the origin.

Both refute two-frame nonemptiness.  **Claim 1 CONFIRMED.  Claim 2
REFUTED.**

### 1.4 The Galois shield does not close the hole

C1's sequel: a Galois-stable nonempty special fibre cannot be emptied on
the generic fibre of the same component by averaging, norms, or descent.
False as a rescue.  The toy is Galois-stable (`N ∈ Z`) and has nonempty
special fibres at both frames.  Vertical components over a rational
integer are the standard Galois-stable countermodel.  Galois cannot
create a generic point.

### 1.5 What two frames do prove

**Claim 3 CONFIRMED**, restated:

> Suppose `F ⊂ A_S[x]` reduces at two frames `P,Q` to systems with
> nonempty special fibres.  Then there does not exist a Bézout identity
> `∑ g_i f_i = 1` with all coefficients of all `g_i` in `A_S`.  Equivalently,
> `1` does not lie in the ideal `(F)` of `A_S[x]`.  Equivalently, any
> K0-emptiness certificate, after clearing, produces `0 ≠ d ∈ (F) ∩ A_S`
> with `d ∈ P ∩ Q`.

That is G6, plus the charged field theorem which deletes the “on a factor
`K_i` through which a frame factors” bookkeeping.  It is a
certificate-shape constraint, not nonemptiness.

---

## 2. Strongest correct finite-prime replacement

### 2.1 Setup

Let `K0/Q` and `A` be as in the charged K0 review.  Let
`A_S = A[1/5]`.  Let `x=(x_1,…,x_n)` and let `F=(f_1,…,f_m) ⊂ A_S[x]` be
finite.  Write `X = Spec(A_S[x]/(F))`, a finite-type `A_S`-scheme, with
structure morphism `π: X → Spec(A_S)`.  Write `I := (F) ∩ A_S`, an ideal
of the Dedekind domain `A_S`.  For a maximal ideal `P` write `X_P` for
the scheme `Spec(κ(P)[x]/(F̄))`.

Absolute norm: for `0 ≠ a ∈ K0`, `N_{K0/Q}(a) ∈ Q`.  For a nonzero ideal
`𝔞 ⊂ A_S`, the ideal-norm `N(𝔞)` is the positive generator of the norm of
the extension of `𝔞` to a fractional ideal of the ring of integers,
viewed in `Q_{>0}`.  Concretely `N(P) = p^{f_P}` for maximal `P` over
`p`, and `N` is multiplicative.  Because `A_S` is a `Z[1/210]`-algebra,
every such norm lies in `Z[1/210]_{>0}`.  The **210-free numerator**
`N^♯(𝔞)` is the unique positive integer coprime to `210` such that
`N(𝔞) = N^♯(𝔞) · 210^{v}` in `Q_{>0}` for some `v ∈ Z`.  For an element
`d`, write `N^♯(d) := N^♯((d))`.

### 2.2 Certificate, contraction, and reduction

**Lemma 2.1 (clearing).**  `1 ∈ (F)` in `K0[x]` if and only if `I ≠ (0)`.
If so, there exist `d ∈ I \ {0}` and `G_i ∈ A_S[x]` with `∑ G_i f_i = d`.

Proof.  A K0-Bézout identity clears to such a `d`.  Conversely a nonzero
constant in `(F)` is a unit in `K0[x]`.

**Lemma 2.2 (one-way location of nonempty fibres, emptiness case).**
Assume `I ≠ (0)`.  If `X_P` is nonempty, then `I ⊆ P`.  Consequently, if
`P_1,…,P_k` are distinct maximal ideals with nonempty fibres, then
`∏_{i=1}^k P_i` divides `I`, and

```text
∏_{i=1}^k p_i^{f_i}    divides    N^♯(I) .
```

For any single certificate `d ∈ I \ {0}`, the same product divides
`N^♯(d)`.  At each such `P_i` one has `v_{P_i}(d) ≥ v_{P_i}(I) ≥ 1`.  No
sharper universal exponent is implied by mere nonemptiness of `X_{P_i}`.

Proof.  A constant `d ∈ I \ P` reduces to a nonzero constant in
`κ(P)[x]`, so `X_P` is empty.  Dedekind unique factorization of `I` then
gives the product of the `P_i` dividing `I`.  Norms are multiplicative,
and primes outside `S` are 210-free.

The converse is false even under `I ≠ (0)`: `P | I` does not force `X_P`
nonempty.  Countermodel `F = {pq,\, qx-1}` over `Z` (after inverting `S`
if needed): `p` lies in the contracted ideal, the fibre at `q` is unit,
the fibre at `p` is proper.  So one must not identify `V(I)` with the
set of nonempty special fibres.  Divisibility is only at observed
`PROPER` places.

If `I = (0)`, Lemma 2.2 is vacuous.  That is the nonempty-generic case,
and empty special fibres can still occur (Lemma 3.3).  They are not
located by `I`.

### 2.3 The two registered frames

Both registered frames are degree-1 primes of `A` (charged K0 review,
item 6), unramified, and do not meet `S`.  Residue norms are the rational
primes themselves.  Banked vanishing of the modular evaluator at those
frames, *if* those zeros are zeros of the reduction of the same `F`,
gives `X_P ≠ ∅` and `X_Q ≠ ∅`.  Lemma 2.2 then yields

```text
105337 · 105673    divides    N^♯(d)
```

for every K0-emptiness certificate `d` of that `F`, and divides `N^♯(I)`.
Numerically `105337 · 105673 = 11131276801`.  This is Fable's repaired
C1, after the following repairs.

**Claim 4 REPAIR.**  Fable writes “content `D` with `N_{K0/Q}(D)`
divisible by every prime whose frame is a zero of the reduction.”  Make
all of the following explicit.

1. The content is an ideal `I ⊂ A_S`, not necessarily principal.  Class
   number of `K0` is not computed and is not needed.
2. `N_{K0/Q}(D)` lies in `Q`, not in `Z`.  The divisibility statement is
   for the 210-free numerator `N^♯`.
3. The divisor is the residue *norm* `p^{f_P}`, not “the rational prime
   under any frame.”  For the two registered frames `f_P=1`, so the
   rational primes appear to the first power.
4. The exponent on each `P` in `I` is some `e_P ≥ 1`, not exactly 1, and
   not read off from the two zeros.
5. The statement assumes the modular zeros are zeros of the reduction of
   this same `F` (the emitter-reduction gate).  It does not assume v3
   beyond that identification.
6. It remains a constraint on emptiness certificates.  It does not assert
   `I=(P Q)` and does not assert generic nonemptiness.

### 2.4 The informal `10^{5k}` claim is not a theorem

**Claim 5 REFUTED** as stated.  What is true: if `P_1,…,P_k` are distinct
degree-1 primes of `A_S` at which `X_{P_i} ≠ ∅` and if `I ≠ (0)`, then

```text
N^♯(I)  ≥  ∏_{i=1}^k p_i .
```

If each `p_i ≥ 10^5`, the product is at least `10^{5k}`.  The two
registered primes are about `10^{5.02}`, and their product is about
`1.11 · 10^{10}`, which is why the slogan looks right for `k=2`.  The
slogan is a lower bound under those extra size and residue-degree
hypotheses, not a law of the content.

There is no matching *upper* bound in Fable.  Finite `k` yields generic
nonemptiness only if an independent height bound on a primitive
certificate is available (effective Nullstellensatz: cofactor-degree
bounds in terms of `n` and `deg F`, then a height bound in terms of the
coefficients of `F`).  No such bound is proved for any D43 packet, and
the exact rows are unsealed, so the coefficients are not even a reviewed
input.  Do not treat “`k` large” as a nonemptiness theorem.

### 2.5 Finite-prime statement, AUDIT-ready

See Theorem A in §8.  That is the strongest correct replacement of C1 at
finite prime count.

---

## 3. ARITH-SPREAD limit implications

### 3.1 Chevalley on an irreducible arithmetic curve

**Lemma 3.1 (dichotomy).**  Let `Y` be an irreducible noetherian scheme of
dimension 1 (here `Y=Spec(A_S)`).  A constructible subset of `Y` either
(i) contains the generic point, in which case it contains a nonempty open
and therefore contains all but finitely many closed points, or (ii) is a
finite set of closed points.

Proof.  Closed subsets of `Y` are: empty, finite sets of closed points, or
`Y`.  Opens are empty or cofinite.  A locally closed subset is therefore
either finite (open in a finite closed set) or cofinite (open in `Y`).
A finite union contains the generic point if and only if some piece does,
if and only if the set is cofinite.

**Lemma 3.2 (Chevalley).**  `π: X → Spec(A_S)` is finitely presented
(`A_S` noetherian, `X` finite type).  The set-theoretic image is
constructible.

Hence: either `π(X)` contains the generic point, or `π(X)` is finite.

The generic point of `Spec(A_S)` lies in `π(X)` if and only if the scheme
`X_{K0}` is nonempty, if and only if `1 ∉ (F)` in `K0[x]`, if and only if
`X_{\overline{K0}}` is nonempty (Hilbert Nullstellensatz over a field:
a proper ideal in a polynomial ring has a zero in an algebraic closure).
Fieldness of `K0` is used here to have a single generic point; that is
Claim 18, supplied by the charged K0 review.  If `A_S` split as a product,
the dichotomy would run componentwise and infinitely many closed points
could pile on one factor while another factor stayed empty.  That is the
deleted `K_i` caveat of original C1.

Flatness is not used.  Properness of `π` is not used.  If `π` were proper,
the image would be closed, hence either finite or all of `Spec(A_S)`, and
a nonempty generic fibre would force *every* special fibre nonempty.  The
D43 scheme is affine.  Finitely many empty special fibres are allowed
when the generic fibre is nonempty.  Fable correctly cites constructible
image, not closed image.

### 3.2 Three fibres, not one slogan

At a closed point `P` of `Spec(A_S)` there are three different questions.

1. **Scheme-theoretic / ideal-proper.**  `1 ∉ (F̄)` in `κ(P)[x]`.
   Equivalent to `X_P` nonempty as a scheme.
2. **Geometric.**  `X_{\overline{κ(P)}}` nonempty.  Equivalent to (1),
   again by Nullstellensatz over the field `κ(P)`.
3. **`F_p`-rational.**  An `A_S`-morphism `Spec(F_p) → X`.  This requires
   `κ(P) ≅ F_p` (residue degree 1) *and* an `F_p`-point of `X_P`.  It is
   strictly stronger than (1)–(2).

Fable's per-prime question, “is the reduced ideal proper over the residue
field?”, is (1)=(2).  That is the correct input to Chevalley.  An
`F_p`-point, such as a pointbank witness, implies (1).  Failure to find
an `F_p`-point does not imply unit ideal.

**Claim 6 CONFIRMED.**  Nonempty geometric fibres at closed points lying
over infinitely many distinct rational primes imply infinitely many closed
points of `Spec(A_S)` in `π(X)` (finitely many `P` per `p`), hence `π(X)`
is infinite, hence contains the generic point by Lemma 3.1, hence
`X_{\overline{K0}} ≠ ∅`.

**Claim 7 CONFIRMED**, with the geometric reading.  Geometrically empty
fibres are unit ideals over `κ(P)`.  Infinitely many such closed points
are infinitely many closed points omitted from `π(X)`.  A constructible
set omitting infinitely many closed points cannot contain the generic
point.  Hence `X_{K0}=∅`.

**Claim 8 REFUTED.**  One unit fibre is the `(2x-1)` phenomenon at `p=2`:
generic nonempty, exactly one empty special fibre.  Wording a single
`UNIT` as “the first genuine char-0-emptiness signal” in any sense that
a consumer could copy as a characteristic-zero conclusion is forbidden.
A single `UNIT` is a theorem about that fibre, and a surprise relative to
a two-frame shield, and a pivot for certificate search.  It is not
emptiness of `X_{K0}`.

**Claim 9 CONFIRMED.**  If `X_{K0} ≠ ∅`, then `π(X)` contains the generic
point, hence is cofinite in the closed points of `Spec(A_S)`.  The omitted
closed points lie over finitely many rational primes.  For every other
rational prime `p ∉ S`, *every* maximal ideal `P | p` of `A_S` has
`X_P ≠ ∅` geometrically.

**Claim 10 REFUTED.**  Geometric nonemptiness of almost all fibres does
not give `F_p`-points.  Countermodel in §7.4: `X = Spec(Z[1/210][x]/(x^2-2))`.
Generic fibre nonempty of dimension 0; geometric special fibres nonempty
for all odd `p ≠ 5,7`; `F_p`-points exist if and only if `2` is a square
in `F_p`.  Infinitely many primes have no `F_p`-point.

Lang–Weil / character-sum estimates, if ever proved for a geometrically
irreducible generic fibre of dimension `d ≥ 1`, would give `F_q`-points
for large `q`.  That is a consequence of a strong geometric hypothesis on
the generic fibre, not a method for proving the generic fibre nonempty
from a finite `PROPER` list.  **Claim 16 REFUTED.**  Fable Card A's
phrase “a uniform character-sum/point-count argument upgrades to generic
nonemptiness” reverses the implication.  Chevalley already upgrades
*infinitely many* geometric `PROPER` fibres to generic nonemptiness.
Finite `PROPER` never so upgrades, by Chevalley or by Lang–Weil.

Dimension 0 is the D43 22-cell's intended regime after a leftover chart
(finitely many `W`-conditions).  In that regime even a nonempty generic
fibre need not produce `F_p`-points at density 1.  A client that searches
only for `F_p`-points and reports `UNIT` on search failure is unsound.

---

## 4. One frame per prime; splitting; Galois torsors

**Claim 11 CONFIRMED.**  The image argument is about closed points of
`Spec(A_S)`.  One maximal ideal `P | p` with `X_P ≠ ∅` puts one closed
point in `π(X)`.  Infinitely many distinct `p` with at least one such
`P` give infinitely many closed points.  That is the whole nonempty
direction.  Symmetrically, one unit frame per prime, for infinitely many
`p`, gives infinitely many omitted closed points, which is the whole
empty direction.

Complete splitting in `K0` is equivalent, for this Galois extension, to
the existence of a degree-1 prime above `p`, equivalently to an
`F_p`-valued frame `A → F_p`.  Density `1/432` among all primes; among
`p ≡ 1 (mod 168)` (complete split in `Q(zeta_168)`), density `1/9` by
Chebotarev in `Gal(K0/B) ≅ (Z/3)^2`.  Fable's cubic-character pretest is
an implementation of that Chebotarev condition, not a hypothesis of
Theorem B.  Non-split primes are legitimate census places: the residue
field is `F_{p^f}` with `f>1`, and the properness test is over that
`F_q`.  Residue degree greater than one is not a hole in the theorem; it
is a hole only in a client that insists on `F_p`-points.

**Claim 12 REFUTED** as a necessity claim.  Galois-stability of the
selected row set (Opus item H / `σ`-involution) is not used.  If the
equations are Gal(`K0/Q`)-stable, the image is Galois-stable, so one
proper frame above `p` implies all conjugate frames above `p` are proper.
That is a bonus, not an assumption.

Fable: “‘all frames unit’ is only needed on the falsifier branch.”
**REPAIR that sentence.**  The falsifier branch (generic emptiness) does
not need all frames unit.  One unit frame at infinitely many `p` already
forces `X_{K0}=∅`.  All 432 frames unit above a single `p` is the
different, stronger assertion that `X ⊗_Z F_p` is empty.  That assertion
is never required by Theorem B.

The 432 frames above one complete-split `p` are one Galois torsor
(charged K0 review, Theorem E).  Agreement of two campaign primes is
conjugate-probe evidence about one field, not two coefficient
components.  Branch indices of `q0` are frame-local.  None of this
affects Chevalley.

---

## 5. D43 client: frozen scheme, existing objects, v3

**Claim 15 CONFIRMED.**  A list of modular proper/unit bits is a
constructible-image census if and only if each fibre is the reduction of
one and the same finite-type `A_S`-scheme.  Independent per-prime
reconstructions, CRT, or “the same named cell, rebuilt from local data”
are navigation, not Chevalley.

### 5.1 What exists

| object | status as frozen `A_S`-scheme | census use |
|---|---|---|
| Finite étale order `A`, field `K0` | theorem, charged K0 review | base of `π` |
| `d43_char0_lift.source_rows` / the Euler–C7 formula (orbit products, B-block `((1+η t^{20})^7-3/2)^{6 or 9}`, Euler pairing, `+42`) | a single Python formula, uniform in the modulus except for inverses of `S`-units (`pow(2,-1,p)` and the Newton list `(1,2,3,4,5,6)`) | legitimate per-prime evaluator of *that* formula, for `p ∉ S` |
| `d43_common_integral_emitter.py` (`5420b5c0…`) | coefficient arithmetic in the 432-basis; not a row packet | coefficient ring, frame gates |
| `selected_rows_v2.py` | mathematical payload reviewed; operational contract `REPAIR/NO_LAUNCH`; `field_claim: null`; no D43 row emitted | not a frozen row list |
| exact-sparse v3 | `V3_REPAIRED_LAUNCH_NOT_AUTHORIZED`; no jet, no row, no AWS | not a frozen row list |
| 155/29 inventory | forecast until a sealed run passes `validate_exact_inventory` | not a scheme change until identities are polynomials |
| 22-support truncation; leftover seven-in-`W` on `D(Δ_*)` | different schemes from the 184-row raw-J affine scheme | must be named separately |
| pointbanks `p=105337`, `p=105673` | `INTERNAL/UNREVIEWED/MOD-p`; `F_p`-points of the modular evaluator | `PROPER` *witnesses* for that evaluator at two degree-1 primes, not UNIT tests, not char-0, not a review seal |
| displayed `E` / four `q0` branches | conditional on the hashed bridge | a different scheme (Rail E), not the J-census |

The Euler formula is polynomial over `A_S`: jet multiplication, finite
C7-products, and the B-block after inverting 2 are polynomial operations,
and 184 coefficient functionals are finitely many.  Finite type is not in
doubt for the formula.  What is in doubt is equality of implementations:
v1 retained independent `HW1/HW2` while claiming the `a00pp` collapse, which
is G6 escape (iii).  A census that runs `d43_char0_lift.source_rows` at
every prime is a census of that function.  A census that claims to be the
special fibres of a future sealed `a00pp` 184-row packet is unearned until
the emitter-reduction gate is a theorem.

AUDIT already records that `source_rows` is a pure-y value evaluator;
nonzero `α,β` need the x-side formula.  A 22-cell census at `α=β=0` must
say so.  Inverse-chart rows `W_i uW_i-1` change the scheme (they force
`W_i` units).  Parked NF rows are a different scheme.  Mixing these is
how a “D43 census” becomes an unnamed union.

### 5.2 v3

**Claim 14 CONFIRMED** for the claim Fable actually needs: per-prime
properness of a named modular evaluator does not wait on exact char-0
expansion.  One can specialise the Euler formula in `F_p[coords]` (or
`F_q[coords]`) and run a Gröbner/Nullstellensatz test without writing the
432-term sparse polynomials over `K0`.

v3 *is* necessary for:

- identifying those special fibres with a sealed exact-row packet;
- the 155 zero identities as polynomials, without which the 29-row 22-cell
  is not known to equal the 184-row scheme cut by the 22-support;
- leftover-chart residue, Rail J / Rail E separation, `σ`-stability of
  live rows;
- any content ledger whose `F` is “the emitted rows” rather than “the
  evaluator that was run.”

Fable's split — “v3 for the char-0 composition step, not for the census
itself” — is therefore right for Card A's cheapest discriminator and
wrong if the composition step is silently treated as already done.  A
sound client names the evaluator in the receipt.

### 5.3 Minimum sound experimental client

Input, frozen before the first prime:

1. A named finite list `F ⊂ A_S[x]`, given either as a sealed exact-row
   packet or as a named evaluator together with a statement that the
   census is of that evaluator and not of an unsealed packet.
2. The base `A_S`, the inverted set `S={2,3,5,7}`, and a frame
   certificate: an `A_S`-algebra map `A_S → F_q` with `q=p^f`, Jacobian
   units, `p ∉ S`.  Complete split is optional.
3. A Nullstellensatz engine over `F_q`, not a point search alone.

Output, per prime, exactly one of:

- `PROPER`, with either an `F_q`-point or a certificate that `(F̄)` is
  proper (e.g. a Gröbner basis not equal to `(1)`);
- `UNIT`, with a Bézout/Gröbner certificate that `1 ∈ (F̄)` in `F_q[x]`;
- `NO_VERDICT`.

Forbidden inferences from a single receipt: characteristic-zero
nonemptiness, characteristic-zero emptiness, `F_p`-points from geometric
properness, geometric emptiness from point-search failure, CRT
coordinates, template survival, 22-cell identities, JC2.

Ledger: if and only if a future K0-emptiness certificate for this same
`F` is claimed, `N^♯(I)` is divisible by `∏ N(P)` over recorded `PROPER`
places.  The ledger is not a nonemptiness proof at finite length.

Stop, mathematical: on the first `UNIT`, the image omits that closed
point; pivot to searching for an emptiness certificate whose content is
coprime to that `P`, or to proving generic emptiness by other means.  Do
not announce emptiness of `X_{K0}`.  Infinitely many `UNIT` would be that
announcement; a campaign will not obtain infinitely many by a finite
run.  Infinitely many `PROPER` is likewise not obtained by a finite run;
the finite run's honest output is the ledger plus per-prime theorems.

Engineering stop rules (six new primes, AWS caps) are not mathematics.

**Claim 17 CONFIRMED.**  Avenue 37 enumerates Keller maps over finite
fields.  This client specialises one frozen coefficient scheme.  Merging
the two is a scope conflict.

---

## 6. Exact evidential meaning

A “signal” is not a characteristic-zero conclusion.  The following is the
entire dictionary.

| observation | theorem it is | theorem it is not |
|---|---|---|
| one `PROPER` at `P` | `X_P ≠ ∅` geometrically; if `X_{K0}=∅` then `P` divides `I` | `X_{K0} ≠ ∅`; an `F_p`-point unless one is exhibited; anything about other frames above `p` |
| finitely many `PROPER` at `P_1,…,P_k` | `∏ P_i` divides `I` *under the hypothesis* `X_{K0}=∅`; lower bound on `N^♯(I)` under that hypothesis | generic nonemptiness; a numerical law `10^{5k}` |
| infinitely many `PROPER` at closed points over distinct rational primes | `X_{\overline{K0}} ≠ ∅`; then automatically all but finitely many closed points are `PROPER` | coordinates; dimension; `F_p`-points; template; algebraization |
| one `UNIT` at `P` | `X_P = ∅`; `π(X)` omits `P`; any emptiness certificate's `d` may be taken coprime to `P` after removing a `P`-factor, and `I ⊈ P` if `I ≠ (0)` | `X_{K0}=∅`; “the two-frame shield is down” as a global emptiness theorem |
| finitely many `UNIT` | `π(X)` omits those closed points; compatible with nonempty generic (standard spreading-out holes) | generic emptiness |
| infinitely many `UNIT` | `X_{K0}=∅`; then `I ≠ (0)` and only finitely many `PROPER` places exist | a constructed certificate `d`; a bound on `e_P` |
| uniform point-count / character-sum for infinitely many `q` | a geometric theorem about the generic fibre (typically: geometrically irreducible, dimension `d`, Deligne/Lang–Weil error term), implying `X_{K0} ≠ ∅` as a corollary and giving `#X(F_q)` | a deduction from a finite census; a substitute for naming `F` |
| two banked `F_p`-points | two `PROPER` witnesses for the evaluator that was run, at two degree-1 primes | a review of the pointbanks; an exact-row reduction; C1 as originally written |

The two-frame “shield” is the finite line of this table, not the infinite
line.  Campaign language that the two primes “forbid emptiness” must be
retired.

---

## 7. Countermodels

Each implication was attacked.  Failures of an attack are recorded as
such; successes are the refutations already tagged.

### 7.1 Non-flat families

`X = Spec(Z[1/210][x]/(p x))` for a fixed `p ∉ S`.  Not flat at `p`.
Generic fibre `{x=0}`, nonempty.  Special fibre at `p` is `A^1`.  Other
special fibres `{x=0}`.  Image is all of the base.  Infinitely many
nonempty fibres, generic nonempty.  Claim 6 survives.  Non-flat extra
vertical mass at one prime does not manufacture an infinite image without
a generic point.

### 7.2 Vertical components, generic empty

`X = Spec(A_S[x]/(N))` with `N=105337·105673`.  This is Fable's toy.
Image is the two closed points under the two frames (more precisely, the
maximal ideals of `A_S` dividing `N`, i.e. the 432+432 degree-1 primes
above those two rationals, because `N` is rational).  Finite image,
generic empty, nonempty special fibres.  Claim 2 dies.  Claims 6–7
survive: the nonempty set is finite, so the infinite hypothesis of Claim
6 is not met.

A finite-type scheme over a Dedekind domain cannot have infinitely many
distinct vertical components without dominating a generic point: that
would be an infinite constructible set omitting the generic point,
forbidden by Lemma 3.1.  Infinite type (an infinite set of equations, or
an infinite disjoint union) is excluded by the finite-type hypothesis.

### 7.3 Localized denominators

`X = Spec(A_S[x]/(2x-1))` cannot be written: 2 is already a unit on
`A_S`.  Over `Z[x]`, this is the standard hole at `p=2`.  On `A_S` the
same role is played by any element of `A_S` that is not an `S`-unit.
Example: `f = π x - 1` for a non-unit `π ∈ A_S`.  Generic point
`x=1/π`, nonempty.  Empty special fibre exactly at primes dividing `π`.
This is Claim 8's countermodel, and it is why two registered frames can
be exactly the omitted set.

Clearing coefficient denominators by multiplying equations *adds*
vertical components (`V(δ f)=V(δ) ∪ V(f)`).  Those extras are finite and
do not break Claims 6–7, but they pollute a finite content ledger: the
extra `PROPER` places divide the clearing factor, not an emptiness
certificate of the original generic fibre.  A sound client uses the
scheme-theoretic closure `(F_{K0}) ∩ A_S[x]`, or evaluates the original
fractional coefficients in `κ(P)` only when those coefficients are
`P`-integral.

Chart localizations (`W1 W2 ≠ 0`, inverted Fitting minors) are different
schemes.  A unit fibre of a chart is not a unit fibre of `X`.

### 7.4 Residue degree greater than one, and `F_p`-points

`X = Spec(A_S[x]/(x^2-2))`.  Generic nonempty.  Geometric special fibres
nonempty for `p ∉ S` (roots in `F_p` or `F_{p^2}`).  `F_p`-points fail
for infinitely many `p`.  A client that reports `UNIT` on “no `F_p`-point
found” falsely triggers Claim 7's hypothesis and would conclude generic
emptiness, which is wrong.  This is the load-bearing countermodel against
sloppy `UNIT` language, and the proof of Claim 10.

Census at a degree-`f` prime with a properness test over `F_{p^f}` is
correct for Claims 6–7.  An `F_p`-point of `X` as a `Z`-scheme still
requires a degree-1 prime of `A_S`.

### 7.5 Constructible images that omit finitely many points

Already §7.3.  In dimension 1, a constructible set containing the generic
point is precisely the complement of a finite set of closed points.  It
cannot omit infinitely many, and it cannot be “generic plus a mysterious
infinite closed set.”  There is no mixed infinite: one cannot have
infinitely many `PROPER` and infinitely many `UNIT` on an irreducible
one-dimensional noetherian base.  That is the content of Lemma 3.1, and
it is why the two limit theorems are exhaustive.

### 7.6 Attempted countermodel to Claim 6: infinite proper, empty generic

Would require an infinite constructible subset of `Spec(A_S)` omitting
the generic point.  Impossible by Lemma 3.1.  Failed.

### 7.7 Attempted countermodel to Claim 7: infinite geometric unit, nonempty generic

Would require a constructible subset containing the generic point and
omitting infinitely many closed points.  Impossible.  Failed, *provided*
`UNIT` means unit ideal over `κ(P)`.  Succeeds if `UNIT` is redefined as
missing `F_p`-points (§7.4).  That is why the dictionary in §6 is not
optional.

### 7.8 Product-algebra / several components

If `K0` were a product of fields, infinitely many proper frames on one
factor would not fill another factor.  Original C1's `K_i` restriction
was aimed at this, and then the Bézout hole remained on each factor.
The charged K0 review deletes the product.  `Spec(A_S)` is irreducible.
Claim 18 CONFIRMED as a simplification, not as a repair of C1.

### 7.9 Galois-stable vertical locus as a rescue of C1

§1.4.  Failed.

---

## 8. Clean theorems, suitable for `AUDIT.md`

Do not edit `AUDIT.md` from this review.  The following is the maximum
text that a later synthesis pass may copy.

### Theorem A (content of a K0-emptiness certificate; finite-prime replacement of C1)

Let `K0/Q` be the degree-432 Galois number field of the charged K0
review, with finite étale model `A` over `Z[1/42]`.  Let `A_S=A[1/5]`
and let `F=(f_1,…,f_m) ⊂ A_S[x_1,…,x_n]` be finite.  Let
`I=(F)∩A_S`.  Then `X_{K0}=∅` if and only if `I ≠ (0)`.  In that case,
for every maximal ideal `P` of `A_S` with `X_P ≠ ∅` one has `I ⊆ P`,
hence `v_P(I) ≥ 1`.  If `P_1,…,P_k` are distinct such maximal ideals,
lying over rational primes `p_i ∉ {2,3,5,7}` with residue degrees
`f_i`, then `∏ P_i` divides `I` and `∏ p_i^{f_i}` divides the 210-free
numerator of the ideal-norm of `I`.  The same divisibility holds for
the 210-free numerator of `|N_{K0/Q}(d)|` for every single Bézout
content `d ∈ I \ {0}`, with exponents `v_{P_i}(d) ≥ v_{P_i}(I) ≥ 1`.
No identification `I=∏ P_i`, no exponent `=1`, and no size law
`|N| ≍ 10^{5k}` is asserted.  Specialising to the two registered
degree-1 frames, *and assuming those modular zeros are zeros of this
same `F`*, one has that `105337 · 105673` divides that 210-free
numerator.

This is not geometric nonemptiness of `X_{K0}`.

### Theorem B (Chevalley dichotomy / ARITH-SPREAD)

With the same hypotheses, the image of `X → Spec(A_S)` is constructible
in an irreducible noetherian one-dimensional scheme.  Therefore exactly
one of the following holds.

1. `X_{\overline{K0}} ≠ ∅`.  Then all but finitely many closed points
   `P` of `Spec(A_S)` have `X_{\overline{κ(P)}} ≠ ∅`.  Equivalently:
   all but finitely many rational primes `p ∉ {2,3,5,7}` have
   nonempty geometric fibres at *every* maximal ideal of `A_S` above
   `p`.  This does not assert `F_p`-points.
2. `X_{K0} = ∅`.  Then only finitely many closed points have nonempty
   geometric fibres, and those points divide `I` as in Theorem A.

In particular:

- nonempty geometric fibres at closed points over infinitely many
  distinct rational primes ⇒ (1);
- unit-ideal (geometrically empty) fibres at closed points over
  infinitely many distinct rational primes ⇒ (2).

One maximal ideal per rational prime suffices.  Flatness, properness,
complete splitting, Galois-stability of `F`, and existence of
`F_p`-points are not hypotheses.  Finite type over `A_S` is a
hypothesis.  Geometric unit ideal is a hypothesis of the empty
direction; missing `F_p`-points are not.

### Theorem C (explicit correction of original C1)

Original C1, charged breakthrough note, is **false**: two honest
nonempty special fibres, even at complete-split frames of a Galois
number field, do not imply `1 ∉ (F)⊗K0`.  The error is that a Bézout
identity over `K0` need not be `P`-integral.  The Galois-stability
paragraph does not restore the implication.  Replace C1 by Theorem A at
finite prime count and by Theorem B at infinite prime count.  The
algorithm-memo G6 statement (no emptiness certificate with denominators
in `{2,3,5,7}`) remains true and is the `S`-integral special case of
Theorem A.

---

## 9. Promotion and scope limits

**Allowed.**

- Cite Theorems A–C as algebraic geometry over the charged `K0`/`A`
  coefficient ring.
- Cite Fable's detection of the C1 hole, and the toy, as a correct
  correction to this round's evidence.
- Cite the two limit implications in geometric language, with the
  dictionary of §6.
- Run, after ordinary registration, a per-prime properness client
  against a *named* frozen evaluator, producing `PROPER`/`UNIT`/
  `NO_VERDICT` as in §5.3.  This review does not register, launch, or
  authorise AWS.

**Forbidden.**

- Promoting original C1 as a non-unit-ideal or nonemptiness lemma.
- Promoting two (or any finite number of) modular zeros to a
  characteristic-zero point, a nonempty generic fibre, or “emptiness is
  impossible.”
- Promoting one `UNIT` to characteristic-zero emptiness.
- Promoting missing `F_p`-points to `UNIT`.
- Promoting a uniform point-count slogan as a proof of generic
  nonemptiness from finite data.
- Promoting `N(D) ≳ 10^{5k}` as a theorem.
- Identifying a modular-evaluator census with a sealed exact-row packet,
  with the 155/29 22-cell, with leftover seven-in-`W`, or with Rail E,
  without the corresponding gate.
- Treating v3, the pointbanks, or `field_claim: null` packets as that
  gate.
- CRT / rational reconstruction from any list of primes.
- Any implication from a D43 fibre census to template survival,
  algebraization, collision, landing, Keller, or JC2.
- Deduplicating this instrument against avenue 37.
- Editing `AUDIT.md`, `APPROACHES.md`, `PROGRESS.md`, `notes.md`,
  `COORDINATION.md`, or `ladder/REDUCTION.md` from this file.
- Any `jc2-lean` access.

**Residual obligations, not theorem defects.**

1. Sealed exact 184-row (and, separately, 29-row) packet with
   emitter-reduction to the named modular evaluator at both registered
   frames, denominators inside `S`.
2. Independent review of both pointbanks if they are to be used as
   `PROPER` witnesses rather than as internal modular navigation.
3. A Gröbner/Nullstellensatz `UNIT` engine over `F_q`; point search is
   not that engine.
4. Effective Nullstellensatz / height bound if anyone wants a *finite*
   `PROPER` list to contradict emptiness.  Absent until rows exist and
   degrees/heights are written.
5. Geometric irreducibility, dimension, and a Deligne/Lang–Weil package
   if anyone wants `F_q`-counts.  That package is not Theorem B, and is
   not available.

Fable's Card B and Card C were not charged and are not adjudicated.

No canonical ledger was edited.

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/d43-arith-spread-hostile-review-grok46-20260829.md
```

computed after the final write, recorded immediately below.
<!-- self-hash -->
f567d52adca2c43d1f9eafd09eb7c2dd1d3deb9eb6f085a3b74bd47991aa5f0c  report body above this delimiter
