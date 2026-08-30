# Hostile review: `BD-GAL` / closure of `BD-D2`

Reviewer: Opus 5 (different-model hostile review)
Date: 2026-08-30 UTC
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`
Verdict: **CONFIRM_WITH_CORRECTIONS**

## 0. Summary

`BD-GAL` and its corollary `BD-D2` are **correct as stated**. I reconstructed
Lemma 1, Theorem 2, the Galois-uniformity contradiction, and the rank-two
trace-zero normal form independently and could not break any of them. The
scope disclaimers in sections 5, 7 and 8 of the producer are accurate: `d1=2`,
even total degree, non-Galois `d2>=3`, imprimitivity and JC2 all remain open,
and the producer does not claim otherwise.

The corrections are of four kinds, none fatal:

* **C-A (redundant proof).** Theorem 2 is a one-line corollary of Lemma 1
  applied to `b=p`. The curve `E`, quasi-finiteness of `F`, dominance and the
  closure `T` are all avoidable. The producer's longer route is nevertheless
  valid; I checked every step.
* **C-B (under-claimed scope).** Theorem 2's proof never uses that `D` is a
  branch component. It holds for **every** irreducible `p` in `A`.
* **C-C (suppressed residue degree).** "an inertia orbit of length one" is
  true but hides `f_T`: `e_T=1` yields `f_T>=1` geometrically fixed sheets,
  not exactly one.
* **C-D (wording).** "two independent proofs" (section 0), "branch/discriminant
  divisor" (section 2) and "every quotient of prime degree" (section 7) each
  need one clause of repair.

I also derived three **strengthenings** that the producer leaves on the table
(section 8 below); they are reviewer-derived and typed as such.

## 1. Custody

Charged producer, recomputed here:

```text
file  xmodel/block-descent-d2-galois-obstruction-producer-sol56-20260830.md
      13671 bytes total
sha   766a843a25eaf560840f15afa8971dd39246fc8b15290491d18e7f4a4c6bb7f7   MATCH
body  13338 bytes                                                        MATCH
sha   f03368f61177ea1cd1819832184d6df559412e3afdc20d30cef5aeb43f3d2bf8   MATCH
basis 0d7544ebd5cb12def6bac892646010301098be3c                           MATCH (HEAD)
```

Body-marker uniqueness was checked **byte-exactly**, not by `splitlines`: the
marker string occurs at two offsets, 13320 and 13409, but only the first is
standalone (preceded by `\n`, followed by `\n`). The second sits mid-line
inside backticks in the seal's own body definition and is correctly excluded.
No `\r` anywhere. Body = bytes `[0,13338)`, ending `used.\n\n<marker>\n`. The
sealed length and hash are therefore consistent with the stated body
definition, and the definition is unambiguous.

Binding dependency:

```text
file  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
sha   ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
body  8285 / 85db7afd1e8b9f1039bbf977b78a6ea1f64cef9b6fb9323f2233281cf1be6e9f  MATCH
```

The dependency's worktree copy is byte-identical to its committed blob at the
frozen basis (`git cat-file` digest agrees), it is tracked, and its own seal
verifies. Its declared basis `0f7ee003...` is the parent of the review basis,
which is consistent: it was authored on the parent and committed in
`0d7544eb`.

Lane custody also verifies: `prompt_sha256=867cb269...`, `fallacy_sha256=
e47fd16c...` with `fallacy_bytes=1985`, `charge_basis_validator_sha256=
a89658bc...`, all recomputed and matching the `run.v2` receipt.

**Verdict V1: PASS.** The producer may be used.

### 1.1 What the dependency actually licenses

The producer's section 0 recital of the promoted theorem is faithful. I
checked each cited clause against the dependency:

| producer recital | dependency clause |
|---|---|
| `B_K subset C[x,y]` | item 1 |
| `g1` dominant, quasi-finite, everywhere etale | item 3 |
| `g2` finite flat (surjective, generic degree `d2`) | item 2 |
| `g1(A^2)` misses the whole non-etale locus `R`; `R` nonempty, pure codim 1 | item 4 |
| `g2(R)=V(Disc(g2))` | item 5 |

No clause is over-read. In particular the producer does **not** import the
withheld polynomial-parametrization decoration (dependency section 3 item 5),
and does not use `A(F)=g2(A(g1))` anywhere. Good hygiene: `A(F)` never appears
in a load-bearing step, so the nonproperness locus stays distinct from the
branch, ramification and discriminant loci throughout.

### 1.2 Execution scope

I had a shell. What I ran: `shasum`, `git cat-file`, and five short `sympy`
/pure-Python controls (each under a second). What I did **not** run: any local
Singular, any heavy CAS, any AWS job, any web search, any formalization tree.
I did not read, list, stat, build or modify `jc2-lean`. No canonical file,
script or producer was edited. Everything below marked "verified" was either
desk-checked by hand or by one of those five controls, which are reproduced
inline.

## 2. Lemma 1 (missed principal divisor) — CONFIRMED

**Statement.** If `0 != b in B_K` is a nonunit and `V_Y(b)` is contained in
`Y minus g1(A^2)`, contradiction.

**Reconstruction.** Let `x` be a closed point of `A^2`. Then `g1(x)` is a
closed point of `Y` not in `V_Y(b)`, so `b(g1(x)) != 0`. Since
`b(g1(x)) = (g1^* b)(x)`, the polynomial `g1^* b` in `S=C[x,y]` has no zero on
`A^2(C)`. Hence `(g1^* b)` lies in no maximal ideal of `S`, so `(g1^* b)=S`, so
`g1^* b` is a unit of `S`, so `g1^* b` lies in `S^*=C^*`. Since `B_K subset S`
is a literal containment of subrings of `C(x,y)` (dependency item 1),
`b = c` with `c` in `C^*`; and `C subset C[f,g] subset B_K`, so `b` is a unit of
`B_K`. Contradiction.

**Answers to the two charged sub-questions.**

1. *Must a nowhere-zero regular function on the source `A^2` be constant?*
   **Yes.** Two separate facts are being used and the producer merges them:
   (i) weak Nullstellensatz — a polynomial over an algebraically closed field
   with no zero generates the unit ideal; (ii) `C[x,y]^* = C^*`. Fact (i) is
   where algebraic closedness of `C` enters and it is load-bearing: over `R`,
   `x^2+y^2+1` is nowhere zero on `A^2(R)` and is a nonunit. The producer
   cites only "weak Nullstellensatz" and leaves (ii) implicit. Both are true
   here; record the two-step structure.
2. *Is injectivity used in the right ring?* **Yes, but the appeal is
   redundant.** Because `B_K subset S` is an inclusion of subrings of
   `C(x,y)`, `g1^*` **is** that inclusion; there is no separate map whose
   injectivity needs invoking. What the step actually needs is `C subset B_K`,
   so that the constant `c` is a unit *of `B_K`* and not merely of `S`. That is
   immediate. No error, but the sentence "Injectivity then says that `b` was
   the same nonzero constant in `B_K`" would be cleaner as "`b=c` in `S`, and
   `c` is already a unit of `B_K`."

**Two precision notes.**

* `V_Y(b)` nonempty is *not* needed as a hypothesis. The contradiction is
  purely "`b` is a nonunit and `b` is in `C^*`". Nonemptiness is only used
  downstream, to certify that a particular `b` is a nonunit.
* Nonemptiness of `V_Y(b)` for a nonunit `b` is legitimate: `B_K` is a
  finitely generated `C`-algebra (module-finite over `C[f,g]`), so every
  maximal ideal has residue field `C` and `V_Y(b)` has closed `C`-points.

**Consequences 1–4, each rechecked.**

1. *No nonempty principal closed set of `Y` is supported inside `R`.* Correct.
   `V_Y(b) subset R subset Y minus g1(A^2)` (dependency item 4); `V_Y(b)`
   nonempty forces `b` a nonunit; `b != 0` is automatic since `V_Y(0)=Y` is not
   inside the proper closed set `R`.
2. *No irreducible component of `R` has principal height-one prime.* Correct;
   `R` is pure codimension one, so its components are height-one primes.
3. *`B_K` is not factorial, so `Cl(Y) != 0`.* Correct. `B_K` is a Noetherian
   normal domain, so factorial is equivalent to `Cl=0` and to every height-one
   prime being principal; item 2 kills that.
4. *Nonmonogenicity.* Correct. If `B_K=A[t]/(P(t))` with `P` monic of degree
   `d2>=2`, then `Omega_(B_K/A)=B_K/(P'(t))dt`, so the non-etale locus is
   `V_Y(P'(t))`, principal and nonempty; `P'(t) != 0` in `B_K` because the free
   basis is `1,...,t^(d2-1)` and the leading coefficient `d2` is invertible in
   characteristic zero. Lemma 1 applies.

The disclaimer attached to item 4 ("finite locally free algebras of rank at
least three need not be globally monogenic") is correct and correctly limits
the claim.

**Verdict V2: CONFIRMED**, with the two precision notes above.

**Available strengthening (see section 8):** the hypothesis can be relaxed
from `V_Y(b) subset R` to `V_Y(b) subset Y minus g1(A^2)`, which is a genuinely
larger *closed* set (`g1` is open by dependency item 3) also containing
`Sing(Y)`.

## 3. Theorem 2 (fixed sheet) — CONFIRMED, proof longer than necessary

### 3.1 The producer's route, step by step

Every step survives.

* *`A -> S` injective.* Keller implies etale implies open implies dominant
  (image is a nonempty open of the irreducible `A^2`); dominant implies `F^*`
  injective. Alternatively `Jac != 0` implies `f,g` algebraically independent.
  **OK.**
* *`p(f,g)` is a nonconstant nonunit.* If `p(f,g)=c` then `p-c` is a nonzero
  element of the kernel (nonzero because `p` is irreducible hence nonconstant).
  Nonunit follows from `S^*=C^*`. **OK.**
* *Choice of `E`.* `p(f,g)` nonzero nonconstant implies `V_S(p(f,g))` is a
  nonempty curve; take an irreducible component. **OK.**
* *`F(E) subset D`.* Immediate. **OK.**
* *`E` dominates `D`.* `closure(F(E))` is irreducible closed inside the
  irreducible curve `D`, hence a point or all of `D`. A point would put the
  curve `E` inside one fibre of `F`, contradicting quasi-finiteness. **OK.**
* *`T := closure(g1(E))` is a curve.* `g1` quasi-finite implies
  `dim g1(E) = dim E = 1`; `E` irreducible implies `T` irreducible. **OK.**
* *`T` dominates `D`, indeed `g2(T)=D`.* `g2` finite hence closed, so `g2(T)` is
  closed, contained in `D` by continuity and containing the dense `F(E)`.
  **OK.**
* *`T` is a component of `g2^{-1}(D)`.* Every component `W` of `g2^{-1}(D)` has
  `dim W = dim g2(W) <= 1` because `g2` is finite; `T` is irreducible closed of
  dimension 1 inside `g2^{-1}(D)`, hence equals the component containing it.
  **OK.** (Krull additionally forces every component to have dimension exactly
  1, since `V_Y(p)` is a nonzero principal closed set in a domain.)
* *`T` is not inside `R`; generic point etale.* `g1(A^2)` meets `R` nowhere
  (dependency item 4) and `g1(E)` is nonempty, so `T` is not inside the closed
  `R`, so `T inter R` is a proper closed subset of `T` and the generic point
  `eta_T` avoids it. **OK.**
* *`e=1` at the divisorial valuation.* `Y` normal gives R1, so `O_(Y,eta_T)` is
  a DVR; `g2` flat and unramified at `eta_T` gives `e(eta_T | p)=1`. **OK.**

The paragraph defending the closed-point-to-generic step is correct and is
exactly the `FALLACY-v2` carrier/attainment discipline: a single unramified
closed point over `D` is only a carrier and would supply nothing; the upgrade
to a *dominating component* is what converts it into a statement about the
divisorial valuation. The producer flags this itself.

### 3.2 Correction C-A: Theorem 2 is one line from Lemma 1

Apply Lemma 1 to `b=p`, viewed in `A subset B_K`.

`V_Y(p) = g2^{-1}(D)` set-theoretically; it is nonempty because `g2` is
surjective, so `p` is a nonunit of `B_K`; and `p != 0`. If every irreducible
component of `V_Y(p)` were contained in `R`, then `V_Y(p) subset R subset
Y minus g1(A^2)`, contradicting Lemma 1. So some component `T` has generic
point outside `R`, hence `e_T = 1`. Every component of `V_Y(p)` has dimension
one (Krull) and is finite onto the irreducible curve `V_A(p)`, hence surjects
onto it. Done.

This uses no curve `E`, no quasi-finiteness of `F` or of `g1`, no injectivity
of `F^*`, and no closure argument. It is strictly weaker in hypotheses and
therefore strictly more robust. The producer's route is not wrong; it is
redundant. I recommend the report keep the short proof and demote the long one
to a remark, because the long one is where a reader would most plausibly look
for a hole.

### 3.3 Correction C-B: the branch hypothesis is unused

Neither proof uses that `D` is a component of the branch divisor. The true
statement is: **for every irreducible `p` in `A`, some component of
`g2^{-1}(V(p))` surjects onto `V(p)` with generic point outside `R`.** The
branch hypothesis is consumed only in section 3, to know that *some* prime
above `(p)` is ramified. The producer under-claims here.

**Verdict V3: CONFIRMED** with C-A and C-B.

## 4. Equivalence with a fixed block of geometric divisorial inertia

### 4.1 The dictionary, made precise

Let `A_(p)` be the DVR at the height-one prime `(p)`, residue field
`kappa(p)=C(D)`, and let `q_1,...,q_r` be the height-one primes of `B_K` over
`(p)`, with `e_i` and `f_i = [kappa(q_i):kappa(p)]`. Flatness of `g2` gives
`sum e_i f_i = d2`.

Geometrically: for a *general* closed point `z` of `D`, take a transversal
disc `Delta` meeting `D` transversally at `z`. Each component `T_i` of
`g2^{-1}(D)` meets `g2^{-1}(z)` in `deg(T_i/D)=f_i` points, each with local
ramification `e_i`. So the topological local monodromy around `D` acts on the
`d2` sheets with cycle type

```text
( e_1^{f_1}, e_2^{f_2}, ..., e_r^{f_r} ),      sum e_i f_i = d2.
```

Its fixed points number `sum_{e_i=1} f_i`. Hence:

> some `e_i = 1`  <=>  geometric codimension-one inertia has a fixed sheet.

Both directions hold, so the producer's "Equivalently" is genuinely an
equivalence and not a one-way implication. In Galois-closure language, with
`I` the inertia group at a place of `E` over `(p)`: `I`-orbits on `G/J`
correspond to the `(i, 1..f_i)` and have length `e_i`, so a fixed point of `I`
is exactly an orbit of length one.

### 4.2 Correction C-C: the residue degree is suppressed

"Over the geometric generic point of `D`, this is an inertia orbit of length
one" is **true** — such an orbit exists — but a reader may take it to mean
exactly one fixed sheet. `e_T=1` yields `f_T >= 1` fixed sheets, where
`f_T = [C(T) : C(D)]` may exceed one. The residue field `kappa(p)=C(D)` is not
algebraically closed, and the passage to the geometric generic point splits
`kappa(q_T)` into `f_T` distinct reduced points precisely because
characteristic zero makes `kappa(q_T)/kappa(p)` separable. This *helps* the
producer (more fixed sheets, not fewer), so the correction is expository, not
substantive. The sharp form is: the number of geometrically fixed sheets is
`sum_{e_i=1} f_i`, and Theorem 2 says this is at least one.

**Verdict V4: CONFIRM_WITH_CORRECTIONS** (C-C).

## 5. Galois uniformity over a possibly singular normal `Y`

### 5.1 The uniformity theorem

With `K/C(f,g)` Galois of group `Gamma`, `A` integrally closed in its fraction
field, and `B_K` the integral closure of `A` in `K`, `Gamma` acts on `B_K` and
acts **transitively** on the primes of `B_K` over any prime of `A` (Bourbaki
AC V.2.2). Conjugation by an element carrying `q_1` to `q_2` is an
`A_(p)`-isomorphism `B_(q_1) -> B_(q_2)`, so all `e_i` agree and all `f_i`
agree.

**Singularity of `Y` is harmless, and this is the crux of the charged
question.** The theorem needs only that `A` is integrally closed and `B_K` is
its integral closure — no regularity of `B_K`, no Noetherian hypothesis, no
smoothness of `Y`. Separately, `B_K` normal gives Serre R1, so every
height-one localization is a DVR and `e_i`, `f_i` and divisorial inertia are
well defined even when `Sing(Y)` is nonempty. Since `Sing(Y)` has codimension
at least two in a normal surface, it never meets a codimension-one point and
cannot perturb the divisorial computation. Nothing in section 3 touches the
singular locus.

### 5.2 Where each hypothesis enters — exact localization

* **Characteristic zero** enters at exactly three places.
  1. Section 4, `Tr(1)=2` invertible: without it the trace retraction
     `b |-> Tr(b)/2` does not exist and the whole rank-two normal form
     collapses.
  2. Section 3, "at least one prime above `(p)` is ramified": at a height-one
     point, non-etale is equivalent to `e>1` **only because** residue
     extensions are automatically separable in characteristic zero. In
     characteristic `p` a point of `R` could be unramified-with-inseparable-
     residue, and the contradiction with `e_T=1` would evaporate. This is the
     single most load-bearing use of characteristic zero in section 3 and the
     producer does not name it.
  3. "In characteristic zero every quadratic field extension is Galois",
     converting `BD-GAL` into `BD-D2`.
* **Separability** enters as: existence of the Galois closure `E` (section 7);
  nondegeneracy of the trace form, used for `disc=4h != 0` in section 4 and for
  the different in my section 8; and tameness, so that
  `v_(T_i)(different) = e_i - 1`.
* **Branch nonemptiness** enters only in section 3, to supply a `(p)` carrying
  a ramified prime. It is supplied by dependency item 4, whose proof is: if
  `R` were empty, `g2` would be a connected finite etale cover of `A^2_C` of
  degree `d2>=2`, impossible. The producer's non-circularity defence is
  **correct**: `g2`, not `g1`, is the finite map, so no properness of `g1` is
  used anywhere. Section 4 additionally re-derives nonemptiness purely
  algebraically (`h` nonconstant), so section 3's dependence on item 4 is not a
  single point of failure in the quadratic case.

### 5.3 The contradiction

`D=V(p)` is the closure of the image of a component of `R`; since `g2` is
finite, that image is an irreducible curve, hence `V(p)` for an irreducible `p`
(`A` is a UFD). Some prime above `(p)` has `e>1`; Theorem 2 gives one with
`e=1`; uniformity forbids both. Hence no proper block field is Galois over
`C(f,g)`; hence `d2 != 2`.

**Verdict V5: CONFIRMED.**

## 6. Rank-two trace-zero normal form — independently re-derived

I re-derived the whole of section 4 from scratch and machine-checked the two
computational claims.

* **Trace splitting.** `Tr(1)=2` is invertible, `e(b)=Tr(b)/2` is an `A`-linear
  retraction of `A -> B`, so `B = A.1 (+) M` with `M = ker(Tr)`. **OK.**
* **Projectivity and `Pic(A^2)=0`.** `B` is finite flat over Noetherian `A`,
  hence projective; `M` is a direct summand, hence projective of rank one;
  `Pic(C[u,v])=0` (already because `C[u,v]` is a UFD, a fortiori by
  Quillen-Suslin) makes `M` free. **OK.**
* **`w^2=h`.** With `w^2=a+bw`, multiplication by `w` in the basis `(1,w)` has
  matrix `[[0,a],[1,b]]` and trace `b`; `Tr(w)=0` forces `b=0`. *Verified
  symbolically.* Hence `B = A[T]/(T^2-h)` (a map of free rank-two modules
  carrying basis to basis). **OK.**
* **Domain consequences.** `h != 0` (else nonreduced) and `h` is not a square.
  `h` cannot be a nonzero constant because every nonzero complex constant is a
  square — this is a second, independent use of algebraic closedness of `C`.
  So `D=V_A(h)` is a nonempty curve, obtained **without** properness, topology
  or dependency item 4. **OK, and this is the strongest structural point in the
  packet.**
* **Squarefreeness.** If `q^2 | h`, then `w/q` is integral over `B` (monic
  `(w/q)^2 - h/q^2 = 0`), hence in the normal `B`; writing `w/q = alpha+beta w`
  and clearing gives `q.alpha=0`, `q.beta=1`, so `q` is a unit. **OK.**
* **Discriminant and differentials.** Gram matrix of the trace form in
  `(1,w)` is `[[2,0],[0,2h]]`, determinant `4h`. *Verified symbolically.*
  `Omega_(B/A) = B/(2w) dw`, so `R = V_Y(w)` (using `2` invertible), and
  `g2^{-1}(D)_red = V_Y(h)_red = V_Y(w) = R`. **OK.**
* **Singularities kept visible.** Jacobian criterion on `w^2-h(u,v)` gives
  `Sing(Y)=V_Y(w, h_u, h_v)`, contained in `R`, finite by squarefreeness,
  possibly nonempty. Nothing smuggles smoothness of `Y` or of `D`. **OK.**
* **Final contradiction.** `w` is an actual element of `B_K subset S`;
  `g1(A^2)` misses `R=V_Y(w)`, so `w o g1` is nowhere zero on `A^2`, so it is a
  constant `c` in `C^*`, so `w=c` in `B`, contradicting `Tr(w)=0` (and, more
  cheaply, `h=c^2` would be constant). Uses neither smoothness of `Y` nor
  properness of `g1`. **OK.**
* **Downstairs restatement.** `F^{-1}(D) = g1^{-1}(g2^{-1}(D)) = g1^{-1}(R)`
  is empty, so `h(f,g)` is a unit, so constant, contradicting injectivity of
  `F^*` on the nonconstant `h`. **OK.**

### 6.1 The one hypothesis whose failure mode is not stated

`Pic(A)=0` is named but its failure mode is not. Over a base `X` with
`Pic(X) != 0`, trace splitting still gives `B = O_X (+) L^{-1}` for a line
bundle `L`, with `h` a section of `L^2` and `w` a section of `L`; then
`R = V(w)` is an effective divisor in `|L|` that need **not** be principal, and
Lemma 1 does not apply. So `Pic(A^2)=0` is not cosmetic: it is exactly what
turns `R` into a *principal* closed set. Recording this makes the degree-two
argument's mechanism explicit and connects it to the general criterion in
section 8 below.

### 6.2 Correction C-D(i): "two independent proofs"

Section 0's "two independent proofs" overstates. Sections 2-3 and section 4
both run on the *same* Lemma 1 mechanism: `B_K subset S`, `O(A^2)^* = C^*`, and
avoidance of `R`. What section 4 is independent **of** is Galois theory, the
Galois closure, and dependency item 4's nonemptiness of `R` — which it
re-derives. The accurate wording is "a second proof of the quadratic case
independent of sections 2-3", not "independent".

**Verdict V6: CONFIRMED** (independently re-derived), with C-D(i).

## 7. Decorations, itemized

Per mandate item 7, these are separated so that a flaw in any of them cannot
be conflated with a flaw in `BD-GAL`. **None of D1-D5 is load-bearing for
Lemma 1, Theorem 2, section 3 or section 4.**

* **D1 `Cl(Y) != 0`.** CONFIRMED (section 2 above). Strengthened in section 8.
* **D2 Nonmonogenicity.** CONFIRMED. Correctly limited: rank `>= 3` finite
  locally free algebras need not be monogenic, so this does not close higher
  degree. Strengthened in section 8.
* **D3 Section 6 log/topological bookkeeping.** CONFIRMED as decoration. The
  double cover `U -> V` is `g2` restricted over `A^2 minus D`, finite of degree
  two and etale, and `U` is an open of the irreducible `Y` hence connected; the
  class in `Hom(pi_1(V), Z/2)` is nontrivial on the meridian of each component
  because `h` is squarefree, so each valuation is `1`, odd. The identity
  `2 div(w o g1) = div(h(f,g)) = F^* D` is correct. The producer's disclaimer
  that simple connectivity of `A^2(C)` is *not itself* the contradiction is
  correct and is the right call: the contradiction is that the lift is a global
  unit.
* **D4 Section 6 boundary control `X_m`.** CONFIRMED, and it is a good control.
  On `Y=V(w^2-uv)`, parametrised by `(u,v,w)=(p^2,q^2,pq)` (so `Y=A^2/mu_2`,
  normal, singular exactly at the origin), the rulings give `div(u)=2L_1`,
  `div(v)=2L_2`, `div(w)=L_1+L_2`. Hence `v_(L_1)(w)=1` is odd, so `w` is not a
  `d`-th power in `Frac(B)` for any `d>=2` (and not in `-4.Frac(B)^4`), so
  `s^m-w` is irreducible and `X_m` is connected. `s` is a unit because
  `s^m = w` is invertible on `U`, and `s` is nonconstant — so `O(X_m)^*`
  strictly contains `C^*`. The control therefore isolates the source-unit input
  while *retaining* a singular, non-`A^2` intermediate surface, exactly as
  claimed. **Verified.**
* **D5 Section 6 control `(w,v) |-> (w^2,v)`.** CONFIRMED: `Jac = 2w` is
  nonconstant, so avoidance of `R` is load-bearing and not free.

**Verdict V7: all decorations CONFIRMED.**

## 8. Reviewer-derived strengthenings

These are **mine**, not the producer's. They are proved here and should be
independently confirmed before any load-bearing downstream use.

### 8.1 S1 — Lemma 1 upgrades to a class-group injection

**Claim.** The free abelian group on the codimension-one components of the
closed set `Y minus g1(A^2)` — in particular on the components `R_1,...,R_k`
of `R` — injects into `Cl(Y)`. Hence `Cl(Y)` is infinite and each `[R_i]` has
infinite order.

*Proof.* `g1` is open (dependency item 3), so `Z := Y minus g1(A^2)` is closed
and contains `R`. Suppose `sum n_i R_i = div(b)` for some `b` in `K^*`, with
all `R_i` inside `Z`. Split `div(b) = P - N` into effective parts with
disjoint supports, both inside `Z`. Since `B_K` is a normal (Krull) domain,
`b` is regular on `Y minus Supp(N)` and `b^{-1}` is regular on
`Y minus Supp(P)`. Both opens contain `g1(A^2)`, and `g1^{-1}` of either
complement is a closed subset of `A^2` with no closed point, hence empty; so
`g1` factors through both opens as a morphism. Therefore `g1^* b` and
`g1^*(b^{-1})` both lie in `C[x,y]`, so `g1^* b` lies in `C[x,y]^* = C^*`.
Since `g1^*` on function fields is the inclusion `K subset C(x,y)`, `b` is in
`C^*` and `div(b)=0`, so all `n_i=0`. `square`

This subsumes the producer's `Cl(Y) != 0`. It is *conditional on the
hypothetical sandwich*, as it must be: the quadric cone has `Cl = Z/2` finite,
and correspondingly admits no dominant `g1` avoiding `V(w)` (section 9.1).

### 8.2 S2 — the different is not principal (subsumes nonmonogenicity)

**Claim.** `omega_(B_K/A) = Hom_A(B_K, A)` is **not** a free `B_K`-module;
equivalently the different ideal `d_(B_K/A)` is not principal.

*Proof.* Suppose `omega` is free with generator `lambda`. Under the standard
identification of `omega` with the inverse different (valid because `K/C(f,g)`
is separable), freeness means the different is a principal ideal `(dd)` with
`dd != 0`. In characteristic zero every codimension-one point is tame, so
`v_(T_i)(dd) = e_i - 1` at each height-one prime; hence
`div(dd) = sum (e_i - 1) T_i`, whose support is exactly the set of ramified
codimension-one points, i.e. `R` (pure codimension one by dependency item 4).
Since `B_K` is normal and `dd != 0`, `V_Y(dd) = Supp(div(dd)) = R`, and `dd` is
a nonunit because `R` is nonempty. Lemma 1 applies. `square`

Consequences, in strictly decreasing strength: `omega` not free implies `B_K`
is not a complete intersection over `A`, implies `B_K` is not monogenic (the
producer's item 4, since monogenic gives the principal different `(P'(t))`),
and implies `Cl(Y) != 0` (as `omega` is a rank-one reflexive `B_K`-module —
it is `A`-free hence maximal Cohen-Macaulay over `B_K` — so `Cl(Y)=0` would
force it free). S2 is also consistent with S1: `[omega] = [sum (e_i-1)T_i]` is
one of the classes S1 shows to be non-torsion.

**S2 reorganizes the whole packet.** The uniform statement behind both
degree-two proofs and the nonmonogenicity corollary is:

> the obstruction is exactly that **`R` supports no nonzero principal effective
> divisor**; degree two dies because rank two forces `B = A[T]/(T^2-h)`, a
> complete intersection, whose different `(2w)` is principal.

Section 5 of the producer explains the degree-two specificity in terms of the
set equality `g2^{-1}(D)_red = R`; the divisor-theoretic explanation above is
equivalent for rank two and generalizes.

### 8.3 S3 — Theorem 2 holds for every irreducible `p`

Already stated as C-B. Worth promoting because it says the fixed-sheet
phenomenon is not about the branch locus at all.

## 9. Countercontrols in degrees two and three

### 9.1 Degree two: no escape found

I could not construct any degree-two countercontrol, and the structural reason
is sharp: **in rank two `R = V(w)` is always principal**, `w` being the
trace-zero generator, so Lemma 1 always fires. There is no room to manoeuvre.

Hardest available shape — `Y = V(w^2-uv)`, the quadric cone, which has
`Cl(Y)=Z/2` nonzero and `Sing(Y)` nonempty, i.e. both of the "escape hatches"
one would want. Direct check: a `C`-algebra map `B[1/w] -> C[x,y]` must send
`w` to a unit of `C[x,y]`, i.e. a constant `c != 0`; then the images of `u` and
`v` multiply to `c^2`, so both are units, so both are constants; so every such
map is constant and none is dominant. **No `g1` exists**, matching Lemma 1
with `b=w`. Verified.

This also shows S1 is not vacuous as a filter: the cone's `Cl` is finite, and
correspondingly it is not a sandwich candidate.

### 9.2 Degree three: why transposition inertia evades the quadratic argument

The producer's model `(w,v) |-> (u = w^3-3w, v)` checks out exactly:

```text
disc_T(T^3-3T-u) = -27(u-2)(u+2)            branch lines u = +-2
w^3-3w-2 = (w-2)(w+1)^2                     e=1 sheet at w=2, e=2 at w=-1
w^3-3w+2 = (w+2)(w-1)^2                     e=1 sheet at w=-2, e=2 at w=1
R = V(P'(w)) = V(w^2-1)                     lines w = +-1
g2^{-1}(D) = V((w-2)(w+1)^2(w-1)^2(w+2))    lines w in {2,-1,1,-2}
```

All verified symbolically. So `R` is a **proper** subset of `g2^{-1}(D)_red`:
the sheets `w = +-2` lie over the branch lines yet are unramified.

**That is precisely the evasion.** The quadratic contradiction needs the set
equality `g2^{-1}(D)_red = R`, because only then does "the composite avoids
`R`" force "the composite avoids `D`", hence `p(f,g)` a unit, hence a
contradiction with injectivity of `F^*`. In degree three the composite may
avoid `R` while still meeting `D` along the fixed sheet, so `p(f,g)` need not
be a unit and nothing contradicts. What survives in all degrees is only the
fixed-sheet condition — which is what Theorem 2 asserts and no more. The
producer states this correctly.

Two additions to the producer's own disclaimer about this control. It notes
that the control's intermediate surface is `A^2` and its algebra is monogenic,
both already forbidden. Stronger and simpler: `B = C[w,v]` is **factorial** and
`R = V(w^2-1)` is **principal**, so Lemma 1 kills it outright — indeed no
polynomial `w(x,y)` can avoid both `w=1` and `w=-1` without both `w-1` and
`w+1` being constants. So the control is a local-inertia control only, never a
sandwich candidate, exactly as claimed.

### 9.3 Permutation countercontrols

Computed explicitly (order-48 permutation group on six points):

```text
G = C2 wr S3 on 6 points, blocks {0,1},{2,3},{4,5}
|G| = 48,  |H| = 8 (point stabiliser),  |J| = 16 (block stabiliser)
d1 = [J:H] = 2      d2 = [G:J] = 3
J normal in G ?  False
block action of a block-transposition: (1,0,2)  -> fixed blocks: [2]   (one)
block action of a block-3-cycle     : (1,2,0)  -> fixed blocks: []    (none)
fixed-sheet counts on d2=3: identity 3, transposition 1, 3-cycle 0
```

Every claim of the producer's section 7 is reproduced. In particular a
`d1=2, d2=3` configuration exists with `J` non-normal, `[G:J] != 2`, and a
transposition inertia fixing exactly one block — fully compatible with
`BD-GAL`. **The report does not accidentally exclude two-element blocks.**

## 10. Group-theoretic translation — CONFIRMED

`H subset J subset G` with `d1 = [J:H]` the block size and `d2 = [G:J]` the
number of blocks is the standard correspondence between intermediate fields
`C(f,g) subset K subset C(x,y)` and block systems of `G` acting on `G/H`; the
block containing `H` is `J/H`. `K/C(f,g)` Galois is equivalent to `J` normal in
`G` (separability is automatic in characteristic zero), and an index-two
subgroup is normal, so `d2=2` is excluded. All verified.

The theorem constrains `[G:J]`, never `[J:H]`. Structurally this is why `d1=2`
survives: the rank-two normal form of section 4 is applied to `g2`, which is
the finite flat map of rank `d2`; `g1` is not finite, has no trace, and admits
no such normal form. Nothing in the packet reaches `d1`.

### Correction C-D(ii) and C-D(iii)

* Section 2's "branch/discriminant divisor" merges two objects that agree here
  only as **supports**: `g2(R) = V(Disc(g2))` as sets by dependency item 5, but
  the discriminant *divisor* carries multiplicities that the branch set does
  not. Every use in the packet is set-theoretic, so nothing breaks, but per
  `FALLACY-v2` the wording should read "an irreducible component of the support
  of the discriminant".
* Section 7's "does not exclude ... every quotient of prime degree" is
  ambiguous. It *does* exclude every **Galois** prime-degree quotient (so
  `d2=2` always, and `d2=3` whenever cyclic); it does not exclude non-Galois
  `d2 = p >= 3`. Recommend the explicit wording.
* Minor terminology drift: "sheet" in section 2 means a sheet of `g2`, which is
  a *block* of `F`; section 7 calls the same objects blocks. One clarifying
  sentence would remove the ambiguity.

**Verdict V8: CONFIRMED** with C-D(ii), C-D(iii).

## 11. Prior-art flag (not a mathematical defect)

The same mechanism, applied with `K = C(x,y)` (that is, `d1 = 1`), would say
that `C(x,y)/C(f,g)` itself is never Galois for a non-invertible Keller map —
which I believe is a classical theorem (the "Galois case" of the plane
Jacobian conjecture, associated with Campbell, Razar and Wright around
1973-1981). I could not check this: web search was outside the allowed
envelope for this lane, so I am recording it as a **recollection, not a
finding**.

Two consequences. First, this is a **positive consistency signal**: a new
argument that specializes to a known theorem is more likely correct, not less.
Second, before any *external* promotion of `BD-GAL` as new, someone with search
access should confirm that the *proper intermediate field* case — which is the
genuinely new content, since `d1 >= 2` is outside the classical statement — is
not already in that literature. This is a custody action, not a defect, and it
does not affect the verdict. Note also that the charged dependency states its
theorem only for `d1 >= 2`, so the `d1 = 1` specialization is **not** licensed
by the promoted basis and must not be asserted.

## 12. Itemized verdict

```text
V1  custody / seals / basis / marker uniqueness      PASS
V2  Lemma 1 (missed principal divisor)               CONFIRMED  (2 precision notes)
V3  Theorem 2 (fixed sheet)                          CONFIRMED  (C-A redundant, C-B under-claimed)
V4  fixed-block / geometric divisorial inertia       CONFIRM_WITH_CORRECTIONS  (C-C)
V5  Galois uniformity, singular normal Y             CONFIRMED
V6  rank-two trace-zero normal form                  CONFIRMED  (re-derived; C-D(i))
V7  decorations D1-D5                                CONFIRMED  (none load-bearing)
V8  group-theoretic translation                      CONFIRMED  (C-D(ii), C-D(iii))
V9  degree-2 and degree-3 countercontrols            CONFIRMED  (no escape found in degree 2)
V10 prior-art status of the d1=1 specialization      OPEN (search-blocked; custody action)

OVERALL: CONFIRM_WITH_CORRECTIONS
```

No claim in the packet was refuted. No gap was found in `BD-GAL` or `BD-D2`.

## 13. Maximum exact statement safe to promote

> **Theorem `BD-GAL`.** Let `F=(f,g): A^2_C -> A^2_C` be a hypothetical
> non-invertible Keller map, let `C(f,g) proper-subfield K proper-subfield
> C(x,y)` be a proper intermediate field with `d1=[C(x,y):K] >= 2` and
> `d2=[K:C(f,g)] >= 2`, let `B_K` be the integral closure of `C[f,g]` in `K`,
> `Y=Spec(B_K)`, and `A^2 --g1--> Y --g2--> A^2` the promoted factorization,
> with `R` the non-etale locus of `g2`. Then:
>
> (a) *(missed principal divisor)* no nonzero nonunit `b` of `B_K` has
> `V_Y(b)` contained in `Y minus g1(A^2)`; in particular no nonempty principal
> closed subset of `Y` lies inside `R`;
>
> (b) *(fixed sheet)* for **every** irreducible `p` in `C[f,g]`, some
> irreducible component of `g2^{-1}(V(p))` surjects onto `V(p)` and has generic
> point outside `R`; equivalently, for every component of the support of the
> discriminant, geometric codimension-one inertia on the `d2` sheets of `g2`
> fixes at least one sheet — in fact `sum_{e_i=1} f_i >= 1` of them;
>
> (c) `K/C(f,g)` is **not Galois**; equivalently `J=Gal(E/K)` is not normal in
> `G=Gal(E/C(f,g))`;
>
> (d) *(`BD-D2`)* in particular `d2 = [G:J] != 2`: **no two-block system**;
>
> (e) `B_K` is not monogenic over `C[f,g]` and `Cl(Y) != 0`.
>
> Conditional on the promoted block-descent sandwich; proves neither that such
> a `K` exists nor that a counterexample exists.

Reviewer-derived, promotable only after independent confirmation:

> (f) `Hom_(C[f,g])(B_K, C[f,g])` is not a free `B_K`-module, i.e. the different
> `d_(B_K/A)` is not principal — which implies (e) and implies that `B_K` is
> not a complete intersection over `C[f,g]`;
>
> (g) the free abelian group on the codimension-one components of
> `Y minus g1(A^2)` injects into `Cl(Y)`; in particular `Cl(Y)` is infinite and
> each `[R_i]` has infinite order.

**Explicitly not proved, and not to be paraphrased away:** `d1 != 2`;
exclusion of any non-Galois `d2 >= 3`; primitivity of the monodromy; any
constraint on the parity of the topological degree; identification or
parametrization of `A(F)`; smoothness of `Y`; properness or surjectivity of
`g1`; JC2.

## 14. Cheapest decisive successor

`BD-FIX3` is the right target but as worded ("determine whether those three
constraints ... force a contradiction; otherwise construct a control") it is
open-ended and does not name a decidable object. I judge it **justified only
in the sharpened form below**, which is strictly cheaper because it replaces
a search over normal cubic covers by a search over explicit forms.

Two structural facts make the sharpening available. First, `B_K` is finite flat
over `A=C[u,v]` hence projective hence **free** of rank `d2` (Quillen-Suslin),
and characteristic-zero trace splitting gives `B_K = A (+) M` with `M` free of
rank `d2-1`. Second, for `d2=3`, `M` free of rank two puts `B_K` into the
Delone-Faddeev / Gross-Lucianovic correspondence with a **binary cubic form**
`f = aX^3+bX^2Y+cXY^2+dY^3` over `A`, up to twisted `GL_2(A)`. I verified the
correspondence in place: the multiplication table
`om.th = -ad`, `om^2 = -ac+b.om-a.th`, `th^2 = -bd+d.om-c.th` is associative,
and the determinant of the trace Gram in `(1,om,th)` equals
`b^2c^2 - 4ac^3 - 4b^3d - 27a^2d^2 + 18abcd`, the discriminant of `f`, exactly.

Under this dictionary the two obstructions become explicit form conditions.
Writing `M(phi)` for the matrix of `(phi, om.phi, th.phi)` in the dual basis,
with `phi = alpha.1^* + beta.om^* + gamma.th^*`, I computed

```text
Delta(alpha,beta,gamma) := det M(phi)
  = -a^2 d^2 al^3 + abcd al^3 + abd al^2 ga - acd al^2 be + ac^2 al^2 ga
    - 3ad al be ga + 2ac al ga^2 + a ga^3 - b^2 d al^2 be + 2bd al be^2
    - bc al be ga - b be ga^2 - d be^3 + c be^2 ga
Delta(0,be,ga) = -f(-ga, be)          Delta(0,0,1) = a       Delta(0,1,0) = -d
```

so that

* `B_K` is **monogenic** iff `f` represents a unit of `A`;
* the **different is principal** (equivalently `omega_(B_K/A)` is free, my S2)
  iff the ternary cubic `Delta` represents a unit of `A`. Since
  `Delta(0,be,ga) = -f(-ga,be)`, monogenic implies different principal, as it
  must; the converse can fail, so S2 is strictly stronger than
  nonmonogenicity.

Positive control: `a=1, b=0` (the monogenic cubic `A[t]/(t^3+ct+d)`) gives
`Delta(0,0,1)=1`, a unit. Negative control: the classical non-Gorenstein cubic
`k[t^3,t^4,t^5]` over `k[t^3]` has DF data `a=-z, b=c=0, d=z^2`, and
`Delta = -z(z^5 al^3 - 3z^2 al.be.ga + z be^3 + ga^3)` lies in `(z)`, never a
unit — the criterion correctly reports a non-free `omega`. Both controls run.

**Recommended successor, `BD-FIX3'` (cheapest decisive form).**

> Over `A=C[u,v]`, decide whether there exists a binary cubic form
> `f = aX^3+bX^2Y+cXY^2+dY^3` whose Delone-Faddeev ring `B` satisfies all of:
> (i) `B` is a normal domain; (ii) `disc(f)` is a nonzero nonunit, and every
> codimension-one inertia of `Spec B -> A^2` is a transposition (forced by
> `BD-GAL` (b), and equivalent to: every component of `V_B(disc)` that is
> ramified has `e=2` with a fixed sheet alongside); (iii) `Delta` represents no
> unit of `A` (equivalently the different is not principal — forced by S2);
> (iv) no nonzero effective divisor supported on `R` is principal (forced by
> Lemma 1), and `Cl(Spec B)` is infinite (forced by S1).
> If no such `f` exists, `d2=3` closes and the block index is pushed to `>= 4`.
> If one exists, it is an explicit, checkable candidate cubic sandwich and the
> next obstruction must come from the etale `A^2` first leg.

This is decisive either way, is a finite explicit form computation rather than
an open-ended geometric search, and the deciding invariants (`disc(f)`,
`Delta`, `Cl`) are all already reduced to polynomial data above. Conditions
(iii) and (iv) are the new filters that `BD-FIX3` as originally worded does not
name; they are what makes the search cheap, since (iii) alone eliminates every
monogenic `f` and every `f` with `a` or `d` a unit.

A cheaper *pre-test* is not needed: the natural one, "prove the different is
never principal", is exactly S2 and is proved above, so `BD-FIX3'` is the
cheapest remaining decisive step. Nothing here licenses attacking `d1=2` by the
same route — `g1` is not finite, carries no trace form, and admits no normal
form of this kind, so that case needs a different mechanism.

<!-- BODY-END -->
