# SHEET-GATE — locate the fixed sheets, or park (M)

lane: SHEET-GATE (primary, bounded)
model: opus5
date: 2026-08-31
inputs_verified: 4/4 SHA-256 OK

## 0. Input verification and scope

All four charged inputs verified byte-for-byte against the stated SHA-256 digests
before any reading (`shasum -a 256`, 4/4 match). No CAS, no solver, no network
fetch was run; every number below is hand arithmetic or a cited standard theorem.
Literature citations are **content-level** (from knowledge, not byte-hashed
acquisitions) and are named precisely enough to re-acquire; none of them is a
campaign artifact.

Standing setup for the whole report. `F = (F_1,F_2): A^2 -> A^2` is a polynomial
map over `C` with `Jac F ∈ C^*` (Keller), not an automorphism; `K = C(x,y)`,
`A = C[F_1,F_2]`, `d = [K : Frac A] >= 2`. `D := A_F` is Jelonek's
non-properness set. Two promoted hypotheses are used where flagged:

- **(H2)** `D` is irreducible (`m=1`, promoted at rank four);
- **(H3)** the normalization `D~` is `A^1` (promoted).

Notation fixed once: `D_0 := D \ Sing D`; `s := #Sing D`; `r_p := ` number of
local branches of `D` at `p`; `nu := sum_{p in Sing D} (r_p - 1)`;
`g in S_d` the generic meridian monodromy; `sigma := #Fix(g)`; `H_p` the image
of the local group `pi_1(Delta_p \ D)`; `s_p := #Fix(H_p)`;
`a_p := #F^{-1}(p)`; `a := a_p` for `p in D_0` (shown constant below).

<!-- SECTION 0 END -->

## 1. The claim under audit: (M) as stated, and what its conversion step assumes

Opus's Step 0 builds `Y :=` the normalization of the target `A^2` in `K`, gets
`q: Y -> A^2` finite flat of degree `d` and `A^2 =~ U ⊂ Y` open with
`B_Y := Y \ U` pure of codimension one. Step 1 is the global Euler identity

> **(E)** `1 = d*(1 - e(A_F)) + e(F^{-1}(A_F))`.

Step 2 is the **conversion**: `#F^{-1}(p) = #Fix(H_p) = s_p`. Step 3 assembles

> **(M)** `sigma*(nu + s - 1) - sum_p s_p = d*nu - 1`, `1 <= sigma <= d-2`.

Both cross-pollinators broke Step 2, correctly. This report separates four
independent questions that the packet fused, and answers each:

| # | Question | Verdict here |
|---|---|---|
| S0 | Is Step 0 (`Y`, ZMT, `A_F = q(B_Y)`) legitimate? | **CONFIRMED**; Grok-xpoll §3.1 is **REFUTED** (§2.1) |
| ii | Is `F^{-1}(D_0) -> D_0` a finite covering? | **PROVED**, but of degree `a`, **not** `sigma` (§3) |
| i | Do monodromy-fixed sheets have affine centers? | **Reduced to one integer `b`**; proved `b=0` for `d<=3`; **OPEN** at `d=4` in exactly one class (§4) |
| iii | Is there a `chi_c` lemma for (E)? | **WRITTEN** (§5) |
| iv | Must `s_p` come from Puiseux data? | **CONFIRMED**, and superseded: the identity needs `a_p`, not `s_p` (§6) |

The headline: **(M) is not merely parked. Its corrected form (M') is a theorem,
and the corollaries Opus advertised survive** — because the bound `a <= d-2`,
which Sol-xpoll assumed was lost with `sigma`, is provable directly for `a`.

<!-- SECTION 1 END -->

## 2. The four-box audit at the generic point of the rank-four branch

### 2.1 Step 0 is correct; the "wrong category" objection is refuted

Grok-xpoll §3.1 asserts that the integral closure `B` of `A = C[F_1,F_2]` in `K`
"need not sit inside `C[x,y]`", so that `A^2 -> Spec B` may fail to be a
morphism. That is false, for a one-line reason the attack omits:

> **Lemma 2.1.** `A ⊆ B ⊆ C[x,y]`.
> *Proof.* Let `f ∈ B`. Then `f ∈ K` is integral over `A`, hence integral over
> the larger ring `C[x,y]`. `C[x,y]` is integrally closed in its fraction field
> `K`. Hence `f ∈ C[x,y]`. ∎

So `Y := Spec B` receives a morphism `j: A^2 -> Y`, `q: Y -> A^2` is finite
(Noether, `B` is a finite `A`-module), `Y` is normal, and `q ∘ j = F`. Since `F`
is quasi-finite, so is `j`; `j` is birational; `Y` is normal; hence by **Zariski's
Main Theorem** (Mumford, *Red Book* III.9; Grothendieck's form EGA IV 8.12.6:
`j` factors as an open immersion into a finite `Z -> Y`, and `O(Z) ⊆ C[x,y]` is
integral over `B` which is integrally closed in `K`, so `Z = Y`) `j` is an **open
immersion**. `q` is **flat** by miracle flatness (Matsumura, *CRT* Thm 23.1: `Y`
normal surface ⟹ CM by Serre; base regular; fibres of dimension 0).

> **Lemma 2.2.** `B_Y := Y \ U` is nonempty and pure of codimension one.
> *Proof.* Nonempty: if `U = Y` then `q` is finite étale (it is étale on `U`
> because `F = q∘j` is étale and `j` is an open immersion) over the simply
> connected `A^2`, so `d = 1`. Purity: let `W` be a component of `Y \ U` of
> codimension `>= 2`. Pick a basic open `D(f) ⊆ Y` meeting `W` and no other
> component of `Y \ U`. `D(f)` is affine normal, `D(f) ∩ U = D_U(f|_U)` is a
> basic open of the affine `U`, hence affine, and `D(f) \ (D(f)∩U) = D(f)∩W` has
> codimension `>= 2`. For a normal Noetherian domain `R`, `R = ∩_{ht p = 1} R_p`
> (Matsumura Thm 11.5), so removing a closed set of codimension `>= 2` does not
> change global functions: `O(D(f)∩U) = O(D(f))`. Two affines with the same
> coordinate ring linked by an open immersion are equal, so `D(f)∩W = ∅`. ∎

> **Lemma 2.3.** `A_F = q(B_Y)`, and it is a curve.
> *Proof.* `⊆`: if `x_n -> ∞` in `A^2` with `F(x_n) -> p`, then `q` proper puts
> `x_n` eventually in a compact of `Y`; a limit `y` has `q(y)=p`, and `y ∉ U`
> since `x_n` leaves every compact of `U`. `⊇`: `U` is analytically dense in the
> irreducible `Y`, so any `y ∈ B_Y` is a limit of `y_n ∈ U`; these leave every
> compact of `U`, and `q(y_n) -> q(y)`. Finally `q` is finite, so no component of
> `B_Y` is contracted: `q(B_Y)` is closed and pure of dimension 1. ∎

Lemma 2.3 *reproves*, in this case, Jelonek's hypersurface theorem (Jelonek,
*The set of points at which a polynomial map is not proper*, Ann. Polon. Math.
**58** (1993) 259–266), so (E) does not consume it as an external input.

**Disposition.** Step 0 stands. Grok-xpoll's inference that `CANON-SIEVE/Y`, the
free class group `Cl(Y) =~ Z^{m_Y}`, `kappa-bar(Y) = -infty` and the row-29
reopen "inherit Step 0" and die is therefore **withdrawn as a reason**: those
clients ride a correct construction. (Their own merits are outside this gate;
`Cl(Y)` free follows from `C[Y]^* ⊆ C[x,y]^* = C^*` and the excision sequence,
and `kappa-bar(Y) = -infty` from Iitaka's monotonicity `kappa-bar(U) >= kappa-bar(Y)`
for `U ⊆ Y` open — Iitaka, *Algebraic Geometry* GTM 76, §11.)

### 2.2 The fibre decomposition and the four boxes

`q` is finite flat of degree `d`, so for **every** `p ∈ A^2`
`sum_{y ∈ q^{-1}(p)} e_y = d`, where `e_y := dim_C O_{Y,y} ⊗ κ(p)` is the local
multiplicity. Each `y ∈ q^{-1}(p)` sorts into one of four boxes by
(center in `U` vs. in `B_Y = Y-U`) × (`e_y = 1` vs. `e_y > 1`). At a generic
`p ∈ D_0`, with `B_1,...,B_{m_Y}` the components of `B_Y`,
`delta_j := deg(B_j -> D)` and `e_j := ord_{B_j}(q^*h)` (`h` = reduced equation
of `D`), the boxes are:

| | `e_y = 1` | `e_y > 1` |
|---|---|---|
| **center in `U`** | count `a = #F^{-1}(p)`. **NONEMPTY**, `a >= 1` | **EMPTY** |
| **center in `Y-U`** | count `b := sum_{j: e_j = 1} delta_j` | count `sum_{j: e_j>=2} delta_j`. **NONEMPTY** |

with `d = a + b + sum_{j: e_j>=2} delta_j e_j` and (§3) `sigma = a + b`.

**Box `(U, e>1)` is EMPTY — this is exactly where "Keller" enters.** `F` étale
⟹ `q|_U` étale ⟹ unramified ⟹ every fibre point in `U` is reduced with residue
field `C`, i.e. `e_y = 1`. This is the only box emptied by the hypothesis on the
*source*; everything else is target-side or global.

**Box `(U, e=1)` is NONEMPTY, i.e. `a >= 1`.** Let `h_i` be the equation of a
component `D_i` of `D`. `h_i ∘ F` is non-constant (otherwise `F(A^2)` lies in a
curve, contradicting dominance), so `E_i := F^{-1}(D_i) = V(h_i∘F)` is a nonempty
curve. `F` is quasi-finite, so `F(E_i) ⊆ D_i` is constructible of dimension one,
hence dense in `D_i`. So `#F^{-1}(p) >= 1` for generic `p ∈ D_i`. **No hypothesis
used** — in particular this is block-free and reducibility-tolerant.

**Box `(Y-U, e>1)` is NONEMPTY.** `q` is étale over `A^2 \ D` (its fibres there
lie in `U` by Lemma 2.3, where `F` is étale) and étale at every point of `U`. If
`q` were unramified at the generic point of every `B_j`, its ramification locus
would be a proper closed subset of `B_Y`, hence finite, and its branch locus
finite; **purity of the branch locus** (Zariski–Nagata; Nagata, Illinois J. Math.
**3** (1959) 328–333; SGA1 Exp. X — `A^2` regular, `Y` normal, `q` finite) forces
the branch locus to be pure of codimension one or empty, hence empty, hence `q`
finite étale over the simply connected `A^2`, hence `d = 1`. Contradiction. So
**some `e_j >= 2`**, and `sum_{j: e_j>=2} delta_j e_j >= 2`.

**Box `(Y-U, e=1)` is the whole gate.** It is nonempty exactly when some
dicritical is *unramified* over its image. Its count is Sol-xpoll's `b`. §4
settles it for `d <= 3` and reduces it at `d = 4` to a single alternative.

### 2.3 Two free consequences of the box audit

> **Prop 2.4.** `a <= d - 2` and `sigma <= d - 2`, for every component of `A_F`
> lying in the branch locus of `q`.
> *Proof.* `sigma = a + b = d - sum_{j: e_j >= 2} delta_j e_j <= d - 2`, and
> `a <= sigma`. ∎

This is the load-bearing repair. Sol-xpoll wrote that with `sigma` replaced by
`a`, "`a - a_p = d-1` is compatible with `a = d-1, a_p = 0`". It is not: `a` obeys
the same `<= d-2` ceiling, proved directly and without any appeal to `g != 1`.

> **Prop 2.5.** Any Keller counterexample has `d >= 3`.
> *Proof.* Some component `D_1 ⊆ A_F` is a branch component (previous paragraph).
> Over it, `1 <= a^{(1)} <= d-2`. ∎

Consistency check, not a new theorem: `d = 2` forces `K/Frac A` Galois, and the
Galois case of JC is classical (Campbell, *A condition for a polynomial map to be
invertible*, Math. Ann. **205** (1973) 243–248). The box audit reproduces it.

<!-- SECTION 2 END -->

## 3. Attack (ii): the covering lemma over `D - Sing D`

Grok-xpoll §3.4 is right that the packet parenthetically discarded
"every component of `F^{-1}(D)` is finite over `D`" and then used a consequence of
it. The correct statement is *not* the discarded one (which is indeed false in
general: components of `F^{-1}(D)` can and do run to the boundary over `Sing D`),
and its degree is *not* `sigma`. Here is the repair, proved.

Fix `p ∈ D_0`, `Delta_p` a small bidisk with `D ∩ Delta_p = {t = 0}` a disk.
Since `q(B_Y) = D`, `q^{-1}(Delta_p^*) ⊆ U`, so `q^{-1}(Delta_p^*) = F^{-1}(Delta_p^*)`
and this is a `d`-sheeted covering of `Delta_p^* ≃ Delta × Delta^*`.

> **Lemma 3.1 (orbits = fibre points).** For `p ∈ D_0` the `H_p = <g>`-orbits on
> the `d` sheets are in bijection with `q^{-1}(p)`, the orbit at `y` having size
> `e_y`. Consequently the multiset `{e_y}_{y ∈ q^{-1}(p)}` **is the cycle type of
> `g`**, hence is the same for every `p ∈ D_0`.
> *Proof.* Shrinking `Delta_p`, `q^{-1}(Delta_p) = ⊔_{y} V_y` with `V_y` a
> neighbourhood of `y`. `Y` is normal, hence analytically irreducible at `y`
> (normal ⟹ unibranch), so `V_y` is connected; removing the proper analytic
> subset `q^{-1}(D) ∩ V_y` keeps it connected. So `V_y \ q^{-1}(D) -> Delta_p^*`
> is a **connected** covering; conservation of number for the finite flat `q`
> gives its degree as `e_y`. A connected covering is one monodromy orbit.
> Constancy over `D_0`: `D` irreducible and `D_0` connected make all meridians at
> points of `D_0` conjugate in `pi_1(A^2 \ D)` (Zariski–van Kampen), so the cycle
> type of `g` is one conjugacy invariant. ∎

Lemma 3.1 already yields the *exact* conversion law that Step 2 guessed:

> **Cor 3.2.** For every `p ∈ A^2`, `#F^{-1}(p) = #{y ∈ q^{-1}(p) : e_y = 1} -
> #{y ∈ q^{-1}(p) ∩ B_Y : e_y = 1}`, i.e. `a_p = s_p - b_p` with
> `b_p := #{y ∈ B_Y ∩ q^{-1}(p) : e_y = 1} >= 0`. In particular
> **`a_p <= s_p`, with equality iff no boundary point over `p` is unramified.**

So Sol-xpoll's countermodel is exactly right in kind: a monodromy-fixed sheet is
a *trivial `q`-orbit*, and triviality of the orbit says nothing about which side
of `B_Y` its center lies on. The packet's `#F^{-1}(p) = #Fix(H_p)` is the
special case `b_p = 0`.

> **Lemma 3.3 (covering lemma, repaired).** `q^{-1}(D_0) -> D_0` is an **unbranched
> covering** of degree `c = #cycles(g)`; `B_Y ∩ q^{-1}(D_0)` and
> `E_0 := F^{-1}(D_0)` are each unions of connected components of it. Hence
> `F^{-1}(D_0) -> D_0` **is a finite covering**, of constant degree `a`, and
> `B_Y ∩ closure(F^{-1}(D)) ` lies entirely over `Sing D`.
> *Proof.* (1) Unbranched: for `p'` near `p` in `D_0`, `q^{-1}(p') ⊂ ⊔_i V_{y_i}`
> and `sum_{y' ∈ V_{y_i}} e_{y'} = e_{y_i}`; the total number of points is `c` for
> both `p` and `p'` by Lemma 3.1, and each `V_{y_i}` contains at least one, so each
> contains exactly one, with the same `e`. So `q^{-1}(D_0) -> D_0` is a covering
> and `y ↦ e_y` is locally constant.
> (2) `B_Y ∩ q^{-1}(D_0)` is **open** in `q^{-1}(D_0)`: for `y` in it,
> `q^{-1}(D_0) ∩ V_y` maps bijectively and properly onto the disk `D_0 ∩ Delta_p`,
> hence is an irreducible 1-dimensional analytic set; `B_Y` is pure of dimension 1
> (Lemma 2.2) and contained in `q^{-1}(D)`, so `B_Y ∩ V_y` is a 1-dimensional
> closed analytic subset of that irreducible arc containing `y`, hence equals it.
> It is closed too, so it is a union of components; so is its complement `E_0`. ∎

Two corollaries worth stating separately, because they answer Grok-xpoll's
disjunction ("either the discarded claim is false only over `Sing D`, in which
case restate it as a lemma, or the Euler formula is missing horizontal pieces"):
**the first alternative holds, and here is the lemma.** No sheet of `F^{-1}(D)`
escapes to the boundary over a smooth point of `D`. And, independently:

> **Cor 3.4.** `F|_{F^{-1}(D)} : F^{-1}(D) -> D` is a **local homeomorphism**
> (`F` étale ⟹ local biholomorphism carrying `F^{-1}(D)` onto `D`), so `p ↦ a_p`
> is lower semicontinuous on `D`. With Lemma 3.3, `a_p <= a` for all `p ∈ Sing D`.
> Also `F^*(D)` is **reduced**, so `F^{-1}(D)` has the same local analytic types
> as `D` and `nu_{F^{-1}(D)}` is computed branch-for-branch from `nu`.

**Verdict on (ii): PROVED, with a degree correction.** The lemma the packet needed
is true; the degree is the *affine* count `a`, and `a = sigma` only if `b = 0`.

<!-- SECTION 3 END -->

## 4. Attack (i): the sheet-location theorem

By Cor 3.2 the whole of attack (i) is the single question: **is box `(Y-U, e=1)`
empty?** Three equivalent forms, all proved equivalent here:

> **Prop 4.1.** The following are equivalent.
> (α) `b = 0`, i.e. every component `B_j` of `B_Y` has `e_j >= 2`;
> (β) `b_p = 0` for every `p ∈ D`, i.e. `a_p = s_p` everywhere and (M) = (M');
> (γ) no dicritical divisor of `F` with affine image is unramified over `A_F`.
> *Proof.* (α)⟹(β): let `y ∈ B_Y`, `q(y) = p`, and pick `p' ∈ D_0` near `p`.
> `q|_{B_Y}` is finite onto `D`, so `B_Y ∩ V_y` is a curve through `y` whose image
> covers a neighbourhood of `p` in `D`; hence some `y' ∈ B_Y ∩ V_y ∩ q^{-1}(p')`,
> with `e_{y'} = e_{j'} >= 2`. Conservation of number gives
> `e_y = sum_{y'' ∈ V_y ∩ q^{-1}(p')} e_{y''} >= 2`. (β)⟹(α) and (α)⟺(γ) are the
> definitions (`B_j` ↔ the divisorial valuation of a dicritical of `F` whose
> center on the target is the curve `D`). ∎

So the gate is a statement about **dicritical multiplicities**, and it has an
exact analytic reading:

> **Lemma 4.2 (dicritical multiplicity = order of `dx ∧ dy`).** Let `X` be a
> smooth compactification of `A^2` on which `F` extends to `Phi: X -> P^2`, let
> `L_j ⊂ X \ A^2` be dicritical with `Phi(L_j) = closure(A_F)`, `v_j := ord_{L_j}`.
> Then `e_j = 1 + v_j(dx ∧ dy)`.
> *Proof.* At a generic `p ∈ D` take local target coordinates `(w,t)` with
> `D = {t=0}`; `du ∧ dv = unit * dw ∧ dt`. At a generic point of `L_j` take
> `(xi, z)` with `L_j = {z=0}`. `Phi|_{L_j}` is non-constant onto `D`, so
> `w∘F = W(xi,z)` with `W_xi(xi,0) != 0`; by definition of `e_j`,
> `t∘F = z^{e_j} T` with `T(xi,0) != 0`. Then
> `d(w∘F) ∧ d(t∘F) = e_j z^{e_j - 1} W_xi T * dxi ∧ dz + O(z^{e_j})`, so
> `v_j(F^*(du∧dv)) = e_j - 1`. But `F^*(du∧dv) = Jac(F) * dx∧dy = dx∧dy` up to a
> nonzero constant, by the Keller hypothesis. ∎

Lemma 4.2 is a genuine gain: it converts "sheet location" into a **numerical
invariant of a divisorial valuation at infinity**, computable from Enriques data.
Writing `v = ord_{E_N}` for a valuation obtained from `P^2` by blowups at
`P_1 ∈ L_inf, P_2, ..., P_N` with multiplicities `c_i = ord_{E_N}(E_i^{tot})`,

`v(dx ∧ dy) = sum_i c_i - 3 * sum_{i : P_i ∈ strict transform of L_inf} c_i`,

so `e_j = 1` iff the two sums balance. Sanity: `v = ord_{L_inf}` gives `-3`;
the first blowup gives `-2`; for the non-Keller `F(x,y) = (x, xy)` the dicritical
is the second infinitely-near divisor over `[0:1:0]`, `v(dx∧dy) = -1`, and indeed
`ord(Jac F) + v(dx∧dy) = 1 - 1 = 0 = e - 1` with `h∘F = x`, `e = 1`.

### 4.1 What is proved, and what is not

> **Theorem 4.3 (`d <= 3`).** For `d = 2` there is no counterexample (Prop 2.5).
> For `d = 3`, `b = 0`; hence `sigma = a` and **(M) holds verbatim**.
> *Proof.* `a >= 1` and `a <= d-2 = 1` give `a = 1`; then
> `sum_j delta_j e_j = 2` with some `e_j >= 2` forces a single dicritical with
> `delta = 1, e = 2`, so `b = 0`. ∎

> **Theorem 4.4 (`d = 4`: the gap is one bit, in one class).** Exactly three
> profiles are numerically admissible:
>
> | `a` | dicriticals `(delta_j, e_j)` | `b` | `sigma` | cycle type of `g` | `G` |
> |---|---|---|---|---|---|
> | 2 | `(1,2)` | 0 | 2 | transposition | `S_4` |
> | 1 | `(1,3)` | 0 | 1 | 3-cycle | `A_4` |
> | 1 | `(1,2), (1,1)` | **1** | 2 | transposition | `S_4` |
>
> Hence: in the **3-cycle class (`g ∈ A_4`), `b = 0` unconditionally** and (M)
> holds; the gap is confined to the **transposition class**, where `sigma = 2` but
> `a ∈ {1,2}`, and `b = 1` forces `m_Y = 2` with one trivial dicritical.
> *Proof.* `1 <= a <= 2`, `sum_j delta_j e_j = 4 - a >= 2` with some `e_j >= 2`;
> enumerate. `G` is the normal closure of `g` and is transitive: a transitive group
> generated by transpositions is `S_4`; one generated by 3-cycles and transitive on
> 4 letters is `A_4`. ∎

**No theorem forcing `b = 0` was found.** The obstruction is not laziness: by
Lemma 4.2 the question is whether a divisorial valuation at infinity with
`v(dx∧dy) = 0` can be dicritical for a Keller map, and `v(dx∧dy) = 0` **is
attained** among valuations at infinity in general — e.g. a chain of three free
blowups with only `P_1` on `L_inf` has `sum c_i = 3`, `deg = 1`, `v(dx∧dy) = 0`.
So no purely valuative or purely topological argument can close box 4; a
genuinely `F`-specific input is required. Typed **OPEN** at `d = 4`, transposition
class only.

### 4.2 The one promoted datum that would close it

The lane's brief names the census fibre count `f(z) = 2` at generic `z ∈ B` as an
available promoted input. Its effect depends entirely on what the census means:

> **Cor 4.5 (conditional closure).** At `d = 4`, if `f(z) = 2` is the count of
> **affine source points** `#F^{-1}(z)`, then `a = 2`, and by Theorem 4.4 the
> profile is forced to `(1,2)` with `b = 0`. **(M) then holds verbatim at rank
> four**, together with the entire quota family, with no further input. If instead
> `f(z) = 2` records `#Fix(g)` (i.e. `sigma`), or a sheet count read off a
> monodromy/colouring table, it is consistent with both `(a,b) = (2,0)` and
> `(1,1)` and decides nothing.

This is the cheapest decisive successor in the portfolio: **one typing question
against the census's own definition of `f`**, not a new computation. The brief's
own remark that "the promoted quartic census DATA are consistent with `b=0`" is
exactly the ambiguity Cor 4.5 isolates: consistency is not forcing, but if `f`
counts affine preimages then the datum *is* forcing at `d=4`, because the ceiling
`a <= d-2 = 2` is saturated and saturation kills the trivial dicritical.

Étale-ness and the companion floor are **already spent**: étale-ness empties box
`(U, e>1)` (§2.2) and is what makes `a_p <= s_p` rather than an equality of
unrelated quantities; it cannot also empty box 4, which lives entirely on the
boundary where `F` is not defined.

<!-- SECTION 4 END -->

## 5. Attack (iii): the `chi_c` additivity lemma for (E)

Grok-xpoll §3.4 is right that "`chi_c` agrees with ordinary `e` for complex
algebraic varieties" was asserted, that it was justified by an argument valid only
in the smooth case, and that `A_F` and `F^{-1}(A_F)` are singular curves. The
repair is to **never leave `chi_c`**. Then no comparison theorem is needed.

> **Lemma 5.1 (`chi_c` toolkit).** Over `C`, with `chi_c` = Euler characteristic of
> compactly supported rational cohomology:
> (a) *Additivity*: `Z ⊆ X` closed ⟹ `chi_c(X) = chi_c(Z) + chi_c(X \ Z)`.
> (b) *Multiplicativity in finite coverings*: if `pi: E -> B` is a covering of
> degree `k` of complex algebraic varieties, `chi_c(E) = k * chi_c(B)`.
> (c) *Normalization formula for curves*: for a reduced curve `C` with
> normalization `n: C~ -> C`, `chi_c(C) = chi_c(C~) - sum_{p ∈ Sing C}(r_p - 1)`.
> *Proof.* (a) is the long exact sequence of the pair for compactly supported
> cohomology. (b): `B` is triangulable (Łojasiewicz; Hironaka) by a finite
> triangulation; over each open simplex — simply connected — the covering is
> trivial, so by (a) `chi_c(E) = sum_simplices k * chi_c(simplex) = k * chi_c(B)`.
> (c): apply (a) to `C = (C \ Sing C) ⊔ Sing C` and to
> `C~ = n^{-1}(C\Sing C) ⊔ n^{-1}(Sing C)`, using that `n` is an isomorphism over
> `C \ Sing C`; subtract. ∎

Nothing in (a)–(c) needs smoothness, and nothing needs `chi_c = chi`. (For the
record, `chi_c = chi` for complex algebraic varieties is true — Laumon, C. R.
Acad. Sci. Paris **292** (1981) 209–212 — but it is **not used** here, so the
packet's shortcut is repaired by removal, not by citation.)

> **Theorem 5.2 (E).** `1 = d*(1 - chi_c(A_F)) + chi_c(F^{-1}(A_F))`.
> *Proof.* `F` is proper over `V := A^2 \ D` and étale, so
> `F^{-1}(V) -> V` is a degree-`d` covering; `F^{-1}(V) = A^2 \ F^{-1}(D)` is the
> complement of a proper closed subvariety of an irreducible variety, hence
> connected. Apply 5.1(a) to `A^2 = F^{-1}(V) ⊔ F^{-1}(D)` and 5.1(b) to the
> covering, with `chi_c(V) = 1 - chi_c(D)` from 5.1(a). ∎

Under (H3), 5.1(c) gives `chi_c(D) = 1 - nu`, hence `chi_c(V) = nu` and

> **`chi_c(F^{-1}(A_F)) = 1 - d*nu`.**

Two immediate sanity gates: `A_F = ∅` gives `d = 1` (the classical statement);
`F^{-1}(A_F) = ∅` gives `1 = d*nu`, impossible for `d >= 2`, which re-proves
`F^{-1}(A_F) != ∅` independently of §2.2. **Verdict on (iii): lemma WRITTEN;
(E) is a theorem, not a checksum candidate.**

<!-- SECTION 5 END -->

## 6. Attack (iv): `s_p` from Puiseux local monodromy

Grok-xpoll §3.5 is **confirmed on every point**, and the correction of §3 makes it
sharper than stated.

1. `H_p` is the image of `pi_1(Delta_p \ D)` for the **affine** germ `(D,p)`. That
   group is the local link group of the singularity — the iterated-torus-link
   group read off the **Puiseux pairs of the branches at `p` and their pairwise
   linking numbers** — generated by the `r_p` branch meridians, each conjugate in
   `pi_1(A^2 \ D)` to the single generic meridian class `g` (Zariski–van Kampen,
   `D` irreducible). Nothing in that data is the colouring of the link **at
   infinity** carried by the delta-sequence/splice census. Identifying the two is
   precisely the flag/place/series fallacy; the packet's "add one column to the
   banked colouring census, no new theory" experiment is **mistyped** and must not
   be run as specified.
2. `s := #Sing(D)` counts **affine** singular points of `D ⊂ A^2`; the place at
   infinity is not among them. Mixing this `s` with a projective cusp count (as in
   the `Delta_aff` dossier lane) is a second flag/place error. Confirmed.
3. **The stronger correction**: by (M') below, the quantity the identity consumes
   is `a_p = #F^{-1}(p)`, not `s_p`. Even a *correct* Puiseux computation of `H_p`
   delivers only `s_p = #Fix(H_p)`, and `a_p = s_p - b_p`. So a correct local
   monodromy computation is **necessary but not sufficient**; it becomes sufficient
   exactly when box 4 is empty (Prop 4.1(β)).
4. Sol-xpoll's group-theoretic correction is also confirmed: at `d = 4`,
   `#Fix(H_p) = 1` gives `H_p ∈ {Z/3, S_3}` — the fixed-point count does not force
   cyclicity. The packet's `#Fix(H_p) = 2` case is fine (`H_p` must then act
   trivially outside a 2-element set and be nontrivial, so `H_p = Z/2` generated by
   a transposition), and in the `A_4` class `H_p` is generated by conjugate
   3-cycles so `H_p ∈ {Z/3, A_4}`.

<!-- SECTION 6 END -->

## 7. The corrected identity

Assemble §3 and §5. `chi_c(F^{-1}(D)) = chi_c(F^{-1}(D_0)) + sum_{p ∈ Sing D} a_p`
by 5.1(a); `chi_c(F^{-1}(D_0)) = a * chi_c(D_0)` by Lemma 3.3 and 5.1(b); and
`chi_c(D_0) = chi_c(D) - s = 1 - nu - s` by 5.1(c) and (H3). With
`chi_c(F^{-1}(D)) = 1 - d*nu` from Theorem 5.2:

> ### (M′)  `a*(nu + s - 1) - sum_{p ∈ Sing A_F} a_p = d*nu - 1`
> with `a = #F^{-1}(p)` for `p ∈ A_F \ Sing A_F`, `a_p = #F^{-1}(p)`, and
> **`1 <= a <= d - 2`, `0 <= a_p <= a`** (Prop 2.4, §2.2, Cor 3.4).
> Hypotheses: Keller; (H2); (H3). **This is a theorem.**

It is exactly Sol-xpoll's corrected equation — independently re-derived here — and
it is (M) with `sigma ↦ a` and `s_p ↦ a_p`. The decisive difference from the
cross-pollination verdict is that **the ceiling travels with the correction**: `a`
obeys `a <= d-2` for the same reason `sigma` does, so nothing that used the
ceiling is lost. An equivalent and often handier form, obtained by subtracting
(M′) from `s*a`:

> ### (M′-def)  `sum_{p ∈ Sing A_F} (a - a_p) = (a - 1) + nu*(d - a)`
> — the total affine fibre deficiency over the singular points is determined.

**Scope relaxations, both proved above and both free.**
*Without (H3)*, with `chi~ := chi_c(normalization of A_F)`:
`a*(nu + s - chi~) - sum_p a_p = d*(nu - chi~ + 1) - 1`.
*Without (H2)*: run §3 component-wise. Each irreducible component `D_i` has its
own constant `a^{(i)} >= 1` on `D_i \ Sing(D)`, and
`sum_i a^{(i)} chi_c(D_i \ Sing D) + sum_{p ∈ Sing D} a_p = 1 - d*chi_c(V)`.
So **(E), Lemma 3.3 and the assembly are block-free**; only the collapse to a
single `a` and the clean corollaries use (H2)+(H3). Grok-xpoll §3.2 is therefore
right about the *corollaries* and wrong about the *mechanism*: the primitive /
no-proper-block front does get the component-wise identity and the boxes, it does
not get the quota.

**The weighted budget, proved.** `d = a + sum_j delta_j e_j` with `a >= 1`, so

> ### (B-w)  `sum_j delta_j * e_j <= d - 1`, with some `e_j >= 2`,
> i.e. `2 * sum_{j nontrivial} delta_j + sum_{j trivial} delta_j <= d - 1`;
> when every dicritical is birational onto `A_F` (`delta_j = 1`) this is exactly
> **`2*m_nt + m_triv <= N - 1`** with `N = d`. Consequences: `m_Y <= d - 2`
> always; `m_Y <= floor((d-1)/2)` **iff** `b = 0`. At `d = 4`: at most two
> dicriticals, at most one of them trivial.

(B-w) is the "separately proved weighted inequality" the synthesis authorised as
the fallback cap for the budget family. It is now available **without** Orevkov's
dicritical formula and without the un-byte-hashed acquisition; the strong form
`2*m <= N-1` is the `b = 0` specialisation and remains gated.

<!-- SECTION 7 END -->

## 8. Surviving corollaries, by scope

| Claim | Form that survives | Scope / hypotheses | Status |
|---|---|---|---|
| (E) Euler budget | `1 = d(1 - chi_c(A_F)) + chi_c(F^{-1}(A_F))` | Keller only; block-free | **PROVED** (Thm 5.2) |
| Covering lemma | `F^{-1}(D_0) -> D_0` covering of degree `a` | Keller + (H2) | **PROVED** (Lem 3.3) |
| Conversion law | `a_p = s_p - b_p`, `a_p <= s_p` | Keller | **PROVED** (Cor 3.2) |
| Master identity | (M′), (M′-def) | Keller+(H2)+(H3); component-wise otherwise | **PROVED** |
| Ceiling | `1 <= a <= sigma <= d - 2` | Keller, per branch component | **PROVED** (Prop 2.4) |
| Degree floor | `d >= 3` | Keller only | **PROVED** (Prop 2.5); classical via Galois case |
| **One-node exclusion** | `s=1, nu=1` ⟹ `a - a_p = d-1 > d-2 >= a`, contradiction | Keller+(H2)+(H3), all `d >= 2` | **PROVED** — the packet's three-line reproof survives the correction intact |
| Smooth-`A_F` law | `A_F` smooth ⟹ `a = 1` (and `d >= 3`) | same | **PROVED** |
| Node-count bound | `(d-2)(s-1) >= 2*nu - 1`; at `d=4`, `s >= nu + 1` | same | **PROVED** (put `a_p >= 0`, `a <= d-2` in (M′)) |
| Quota law, `a`-form | `nu = 0` ⟹ `sum_p a_p = a(s-1) + 1` | same | **PROVED** |
| Quota law, monodromy form | `sum_p s_p = sigma(s-1) + 1` | requires `b = 0` | **OPEN** at `d = 4` transposition class; **PROVED** at `d = 3` and at `d = 4` in the `A_4` (3-cycle) class |
| `d=4`, `A_4` class, `nu=0` | `a = 1` ⟹ every affine singularity has `a_p = s_p = 1`, i.e. `H_p = Z/3`, abelian, for **every** cusp | Keller+(H2)+(H3) | **PROVED** (Thm 4.4 + quota) |
| `d=4`, `S_4` class, `nu=0` | if `b=0`: `a=2`, exactly one cusp with `H_p = S_3`, all others `H_p = Z/2` | conditional on `b = 0` | **CONDITIONAL** |
| Orevkov budget re-derivation | (B-w) weighted form | Keller only | **PROVED**; strong unweighted form gated on `b=0` |
| `Y`-structure (`Cl(Y) = Z^{m_Y}` free, `pi_1(Y)=1`, `kappa-bar(Y) = -infty`, `Sing Y` finite ⊂ `B_Y`) | as stated | Keller only | **Construction CONFIRMED** (§2.1); the individual claims are outside this gate but no longer inherit a dead Step 0 |
| Colouring-column quota experiment | — | — | **WITHDRAWN** (§6): computes the wrong `#Fix` |

Two entries deserve emphasis. First, the **one-node exclusion is not lost**: this
was the cross-pollination's central casualty, and it is recovered because `a`
inherits the ceiling. Second, the **quota law is not lost either** — it holds in
`a`-form unconditionally; what is gated is only its *evaluability from monodromy*.

<!-- SECTION 8 END -->

## 9. OPEN list

1. **SHEET-LOCATION (`b = 0`).** Typed **OPEN**. Precise form (Prop 4.1, Lem 4.2):
   *can a divisorial valuation `v` at infinity of `A^2` with `v(dx∧dy) = 0` be
   dicritical, with affine image curve, for a Keller map?* Live only at `d >= 4`,
   and at `d = 4` only in the transposition (`S_4`) class, where it is the single
   bit `a ∈ {1,2}`. No purely valuative/topological proof exists: `v(dx∧dy) = 0`
   is attained among valuations at infinity (§4).
2. **Census typing of `f(z) = 2`** (Cor 4.5). If `f` counts affine source points,
   item 1 closes at `d = 4` immediately. This is a *definition audit of a promoted
   artifact*, not a computation, and is the cheapest successor in the portfolio.
3. **`a_p` from local data.** Even with `b = 0`, evaluating the quota needs `H_p`
   from the **Puiseux data of the affine germ**; the campaign does not currently
   carry that table (§6). A local-monodromy dictionary for the surviving
   unibranch types is the prerequisite for any attainment filter.
4. **`m >= 2` / reducible `A_F`.** The component-wise identity is available (§7);
   the corollaries are not. Needs one `a^{(i)}` per component plus the
   intersection-point bookkeeping in `Sing D`.
5. **`nu >= 1` sharpness.** (M′-def) gives `sum_p (a - a_p) = (a-1) + nu(d-a)`;
   no independent lower bound on individual `a_p` is known, so the bound
   `(d-2)(s-1) >= 2nu - 1` is not shown sharp.
6. **`Y` singular.** `Sing Y` is a finite subset of `B_Y`; the `A^1`-fibration
   consequences of `kappa-bar(Y) = -infty` (Miyanishi–Sugie/Fujita) need `Y`
   smooth or a resolution containing `U`. Not resolved here.
7. **Not attempted (out of scope, flagged so no successor re-imports them):** the
   char-`p`/Swan connection (Lemma 5.1(b) is where char 0 is used, and the
   Artin–Schreier cover is precisely its failure — but this report proves nothing
   about it); `Theta_h`; any `Delta_aff = 6` dossier claim.

<!-- SECTION 9 END -->

## 10. Verdict

**(M) is repaired, not parked.** The corrected identity (M′) — with the affine
fibre counts `a`, `a_p` in place of the monodromy counts `sigma`, `s_p` — is a
theorem under (H2)+(H3), and the ceiling `1 <= a <= d-2` is proved directly, so
the one-node exclusion, the node-count bound, the smooth-`A_F` law and the quota
law all survive. (E) is a theorem with a written `chi_c` lemma. The covering
lemma attack (ii) is answered by a proof, with a degree correction. Attack (iv)
is confirmed and strengthened. Attack (i) is confirmed as a real gap, reduced to
a single integer `b`, proved zero for `d <= 3` and for the `d = 4` `A_4` class,
and left **OPEN** at `d = 4` in the transposition class alone — where one
definition audit of an already-promoted census datum would close it.

Grok-xpoll §3.1 (Step 0 "wrong category") is **REFUTED**; every `Y`-side client
it declared dead should be restored to its prior disposition, judged on its own
merits. Sol-xpoll's §4 items 1–3 and its corrected equation are **CONFIRMED**,
with the one repair that `a <= d-2` (so `a = d-1, a_p = 0` is not admissible and
the one-node control does validate). Grok-xpoll §3.3's methodological point stands
regardless: the one-node agreement is a corollary, not a control, and (M′) is
banked here on its proof, not on its strength.

The correlated-error diagnosis in the synthesis is confirmed in kind and narrowed
in extent: "non-properness implies nontrivial inertia" is still unproved, and it
is exactly `b = 0`; but the *weighted* budget (B-w) `2*m_nt + m_triv <= N-1` is
now proved outright, Orevkov-free, so the budget family need not wait.

<!-- BODY-END -->
