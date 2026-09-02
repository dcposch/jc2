# MPRIME-ALLN-H2 — the `(M')` identity at every degree under `H2`

lane: MPRIME-ALLN-H2 (Path-1 flagship)
model: opus5
date: 2026-09-02
inputs_verified: 3/3 SHA-256 OK

## 0. Custody, scope, method

The three charged inputs were hashed before any mathematical reading; 3/3 match
(`shasum -a 256`). No file outside `xmodel/mprime-alln-h2-opus5-20260902.*` was
written. Four small `python3` scripts were run (integer enumeration and one
`S_4` permutation search); they are listed with their exact roles in §10 and
every conclusion they support is stated so that it can be re-derived by hand or
re-run in ten lines. No CAS, no solver, no network fetch.

**What this lane consumes.** The identity `(M')` and its supporting lemmas as
promoted in `round1033-sheet-gate-opus5-20260831.md` (hostile review
`round1033-sheet-gate-hostile-review-sol56-20260831.md`: (M') **CONFIRMED** as a
theorem under explicit `H2 + H3`); the all-degree dicritical facts `[P3]`,
`[P4]`, `[P7]`, `[P8]` and Orevkov Lemmas 2.1/3.1 as re-derived from primary
source in `n20-escape-kill-opus5-20260901.md` (review-CONFIRMED); THEOREM 7.B
from the charged all-degree coordinator integration.

**What this lane does not consume.** No claim from the `(9,6)` REP-96 lane is
used as an input to a proof here; REP-96 §7 (R4) is used only as the statement
of the charge and as a control (§10). The `N = 4` *reducible* cage is untouched:
everything below is the `H2` (irreducible `A_F`) branch.

**Standing setup.** `F = (F_1,F_2) : A^2 -> A^2` is a Keller map over `C`
(`Jac F ∈ C^*`), **not** an automorphism; `N = d = [C(x,y) : C(F_1,F_2)] >= 2`;
`D := A_F` is Jelonek's non-properness set, a curve. `(H2)`: `D` irreducible.
Notation as in the sheet gate: `D_0 = D \ Sing D`, `s = #Sing D`, `r_p` = number
of local branches of `D` at `p`, `nu = sum_{p ∈ Sing D}(r_p - 1)`,
`a_p = #F^{-1}(p)`, `a = a_p` for `p ∈ D_0`, `W := N - a`.

**Two notation traps, disarmed once.** (i) `ALL-N` writes `sigma` for `#Sing D`
and `d` for `2a - N`; I write `s` and `D_gap := 2a - N`, and reserve `d = N` for
the geometric degree, as the charge does. (ii) `mu_l` (Orevkov dicritical
multiplicity) `= e_j` (sheet-gate boundary multiplicity) and `s_l` (dicritical
cover degree) `= delta_j`; the dictionary is proved, not assumed, in §1.

**Verdict headline** (details in §10). Under `H2`, at **every** degree `N >= 3`:
`A_F` is singular (§3); `H3` holds unconditionally (§2); if every branch of
`A_F` is smooth — this contains the entire nodal case — then `N >= 17` (§5); the
`N <= 16` residual is exactly "`A_F` carries a singular branch", split into a
cuspidal horn that is caged but not empty (§7) and a mixed horn that is the
campaign's one-cusp horn (§8). The `N = 4` `H2` residual is pinned to a single
profile which reproduces the promoted rank-four census exactly.

## 1. Notation, the promoted dictionary, and the exact hypotheses of `(M')`

### 1.1 The two pictures and the bijection between them

Two constructions are in play and the whole lane depends on them agreeing.

*Target-side (`Y`).* `Y := Spec B`, `B` the integral closure of `A = C[F_1,F_2]`
in `K = C(x,y)`; `q : Y -> A^2` finite flat of degree `N`, `A^2 ≅ U ⊂ Y` open,
`B_Y := Y \ U` pure of codimension one (sheet gate §2, review-CONFIRMED). For
`p ∈ A^2`, `sum_{y ∈ q^{-1}(p)} e_y = N`. Components `B_1,...,B_m` of `B_Y`,
`delta_j := deg(B_j -> D)`, `e_j := ord_{B_j}(q^*h)`.

*Source-side (Orevkov).* `X ⊃ A^2` a smooth compactification on which
`Phi : X -> P^2` is a morphism; dicriticals `l ⊂ X \ A^2` with affine image;
`mu_l := ord_l(h ∘ F)`; `l' := l ∩ Phi^{-1}(A^2) ≅ A^1` (Orevkov Lemma 2.1,
degree-free `[R1]`); `phi_l := Phi|_{l'} : A^1 -> D`, factoring as
`phi_l = eta ∘ h_l` with `eta : D~ -> D` the normalization and
`s_l := deg h_l`.

> **Lemma 1.1 (dictionary).** Under `H2`, `j ↦ l` is a bijection between the
> components of `B_Y` and the affine-image dicriticals of `F`, with
> `e_j = mu_l` and `delta_j = s_l`.
>
> *Proof.* Let `l` be a dicritical with affine image. For `f ∈ A`, `Phi^*f` is
> regular at the generic point of `l` because `Phi(l) = closure(D) ⊄ L_infty`;
> so `ord_l >= 0` on `A`, hence on its integral closure `B`, so `ord_l` has a
> centre on `Y`. That centre maps onto `D`, so it is a curve; it is not in
> `U ≅ A^2` because `l` is a divisor at infinity of the source, so `ord_l` is
> negative on some element of `C[x,y]`. So the centre is a component `B_j`, and
> `ord_{B_j} = ord_l` as valuations of `K`. Conversely `B_j ⊄ U` makes
> `ord_{B_j}` a valuation at infinity of the source, i.e. `ord_l` for a divisor
> `l` on some `X`, dicritical with image `q(B_j) = D`. Equal valuations have
> equal value groups and residue fields, so `e_j = ord_{B_j}(q^*h) =
> ord_l(h∘F) = mu_l` and `delta_j = [kappa(B_j) : C(D)] = [C(l) : C(D)] = s_l`
> (the last because `eta` is birational). ∎

Consequences, all previously promoted and now with matching symbols:
`N = a + sum_l s_l mu_l` `[P3]`; `W := N - a = sum_l s_l mu_l >= 2`, so
`1 <= a <= N - 2` (sheet gate Prop 2.4, review-CONFIRMED at exactly this scope);
`b := sum_{mu_l = 1} s_l`. **THEOREM 7.B** says no affine-image dicritical has
`mu_l = 1`; under `H2` every dicritical has affine image `= D`, so

> **(7.B')  every `mu_l >= 2`; hence `b = 0`, `m >= 1`, and `2 sum_l s_l <= W`.**

### 1.2 What `(M')` needs, precisely

`(M')` is
`a(nu + s - 1) - sum_{p ∈ Sing D} a_p = N nu - 1` with `1 <= a <= N-2`,
`0 <= a_p <= a`; equivalently the defect form
`sum_p (a - a_p) = (a-1) + nu(N-a)`. Its proof (sheet gate §7, review §6:
"Every substitution checks") uses exactly three ingredients: Theorem (E)
`1 = N(1 - chi_c(D)) + chi_c(F^{-1}(D))` (Keller only); the covering lemma
`F^{-1}(D_0) -> D_0` of degree `a` (Keller + `H2`); and
`chi_c(D) = 1 - nu`, which is **`H3`** — the statement that the normalization
`D~` is `A^1`.

`H3` is therefore load-bearing, and it is the first thing this lane has to
secure. The promoted derivation of `H3` (`[P5]`, `b0-all-n` Thm 4.1(1)) has the
hypothesis *"some dicritical has `mu_0 = 1`"* — which THEOREM 7.B refutes. The
implication survives 7.B only vacuously; it does **not** deliver `H3`. §2 fixes
this, and the fix is cheaper than the original.

For the record I also carry the `H3`-free form. Writing `theta` for the number
of places of `D` at infinity, `chi_c(D~) = 2 - theta - 2g` for `D~` of genus
`g`, and the same assembly gives

> **(M'_theta)** `sum_p (a - a_p) = (a-1) + T(N-a)`, `T := nu + theta + 2g - 1`.

Since `theta >= 1` and `g >= 0`, `T >= nu`, so relaxing `H3` only **raises** the
right-hand side: every kill below is a fortiori valid without `H3`. §2 shows
`T = nu` anyway.

## 2. LEMMA A — `H3` is a theorem under `H2` (repair of a vacuous promotion)

> **LEMMA A.** Let `F` be a noninvertible plane Keller map and `D_l` any
> irreducible component of `A_F` that is the image of a dicritical. Then the
> projective model of `D_l` is rational, `D_l` has exactly **one** place at
> infinity, and `D~_l ≅ A^1`. Under `H2` this is `H3`, and it needs **no**
> trivial dicritical.
>
> *Proof.* Fix a dicritical `l` with `Phi(l) = closure(D_l)`. By Orevkov Lemma
> 2.1 (`[R1]`, degree-free, re-derived from `refs/jc86.pdf` p. 2 in N20 and
> review-CONFIRMED "without H2 or H3"), `l ≅ P^1` and `l' := l ∩ Phi^{-1}(A^2)`
> is `l` minus a single point, so `l' ≅ A^1`. `Phi|_l : P^1 -> closure(D_l)` is
> a finite surjective morphism of projective curves, and
> `l' = (Phi|_l)^{-1}(D_l)`, so `phi_l := Phi|_{l'} : A^1 -> D_l` is finite and
> surjective. Factor it through the normalization, `phi_l = eta_l ∘ h_l` with
> `h_l : A^1 -> D~_l` finite surjective of degree `s_l`.
>
> (i) *Rationality.* `h_l` extends to a surjection `h̄_l : P^1 -> \bar D~_l` of
> smooth projective curves, so `\bar D~_l` is rational by Lüroth; `g = 0`.
>
> (ii) *One place at infinity.* `D~_l` is affine (finite over the affine `D_l`),
> so `S := \bar D~_l \ D~_l ≠ ∅`. `h_l(A^1) ⊆ D~_l`, so
> `h̄_l^{-1}(S) ⊆ {∞}`. `h̄_l` is surjective, so every point of `S` has nonempty
> preimage inside the one-point set `{∞}`: `#S = 1`.
>
> So `D~_l ≅ P^1 \ {1 point} ≅ A^1`. ∎

Three remarks, because this is a repair of a promoted item and must not be
oversold.

1. **What is new.** The promoted route (`[P5]`; `b0-all-n` §2.3, hostile-review
   CONFIRMED) reaches `H3` through Riemann–Hurwitz applied to `h̄_0` *after*
   using `mu_0 = 1` to force `h_0` étale, and its extra output is `s_0 = 1`.
   Lemma A drops `s_l = 1` — which nothing downstream of 7.B needs — and buys
   `H3` from Lüroth plus a one-line covering argument. It is strictly weaker in
   conclusion and strictly weaker in hypothesis.
2. **Why the repair is necessary and not cosmetic.** After THEOREM 7.B no
   dicritical has `mu = 1`, so `[P5]`'s antecedent is empty and its consequent
   is not asserted. The coordinator's bullet "`H3` as a conclusion"
   (all-degree integration §1.1) is, read literally against `[P5]`, a vacuous
   implication. Every downstream consumer of `(M')` — including REP-96 §7 (R4)
   and this lane — needs `H3` as a *fact*, not as an implication with an
   emptied hypothesis. Lemma A supplies it.
3. **Scope.** Lemma A is componentwise and needs neither `H2` nor `H3`. It
   applies to every component of a reducible `A_F` that carries a dicritical;
   by promoted dicritical surjectivity onto `Irr(A_F)`, that is every component.
   So `chi_c(D_i) = 1 - nu_i` componentwise in the reducible branch too — a free
   sharpening of the block-free identity, flagged for the reducible lanes but
   **not** used below.

Consequences used from here on, all now unconditional under `H2`:
`D~ ≅ A^1`; `chi_c(D) = 1 - nu`; `chi_c(D_0) = 1 - nu - s`; `T = nu` in
`(M'_theta)`, so `(M')` and `(M'-def)` hold verbatim; each `h_l : A^1 -> A^1` is
a degree-`s_l` polynomial map, totally ramified at `∞`, so by Riemann–Hurwitz

> **(RH_l)  `sum_{t ∈ A^1} (e_t - 1) = s_l - 1`**, hence `h_l` has at most
> `s_l - 1` finite critical points; write `R := sum_l (s_l - 1)`.

## 3. THEOREM SMOOTH-KILL — `A_F` is singular at every degree

REP-96 §7 (R4) runs the nodal collapse at `N = 4` in the two branches `a = 2`
and `a = 1`, and the `a = 1` branch is refuted "for every `s >= 1`". The
boundary case `s = 0` is therefore *not* covered: a nodal curve with no nodes is
a smooth curve, and `(M')` is **satisfied** there. This is the first thing a
general-`N` treatment has to close, and it closes completely.

> **THEOREM SMOOTH-KILL.** Let `F` be a noninvertible plane Keller map with
> `A_F` irreducible. Then `A_F` is **singular**: `s >= 1`.
>
> *Proof.* Suppose `s = 0`. Then `nu = 0` and `D = D_0` is smooth, irreducible,
> with `D~ ≅ A^1` (Lemma A); a smooth curve equals its normalization, so
> `D ≅ A^1` and `chi_c(D) = 1`.
>
> (a) *`a = 1`.* Lemma 3.3 makes `E := F^{-1}(D) -> D` a covering of degree `a`,
> so `chi_c(E) = a·chi_c(D) = a`. Theorem (E) gives
> `1 = N(1 - chi_c(D)) + chi_c(E) = N·0 + a`. Hence `a = 1`.
>
> (b) *Both curves are coordinate lines.* `D ⊂ A^2` is closed and isomorphic to
> `A^1`, so by **Abhyankar–Moh–Suzuki** there is `α ∈ Aut(A^2)` with
> `α(D) = {v = 0}`. Replace `F` by `α ∘ F`: still Keller, still noninvertible,
> and `A_{α∘F} = α(A_F) = {v = 0}`. Now `a = 1` makes `E -> D` an étale map of
> degree one, i.e. an isomorphism, so `E ≅ A^1`; `E` is closed in `A^2`, so AMS
> again gives `β ∈ Aut(A^2)` with `β^{-1}(E) = {x = 0}`. Replace `F` by `F ∘ β`.
>
> (c) *Contradiction.* `D = {v = 0}` has reduced equation `h = v`, so
> `h ∘ F = F_2` and `F^*(D) = div(F_2)`. `F` is étale, so `F^*(D)` is reduced
> (sheet gate Cor 3.4): `F_2` is square-free with zero set `E = {x = 0}`, i.e.
> `F_2 = c·x`, `c ∈ C^*` (units of `C[x,y]` are constants). Then
> `Jac F = -c·∂F_1/∂y ∈ C^*`, so `∂F_1/∂y = λ ∈ C^*` and
> `F_1 = λ y + g(x)`. Then `F = (λ y + g(x), c x)` is an automorphism —
> contradicting noninvertibility. ∎

Three notes.

* **Hypotheses actually used**: Keller; `H2` (only through Lemma A, to know `D`
  irreducible with `D~ ≅ A^1`); Theorem (E) (Keller only); Lemma 3.3 and
  Cor 3.4 (Keller + `H2`); AMS (char 0). No `(M')`, no 7.B, no budget.
* **It is not the promoted "smooth-`A_F` law".** The sheet-gate table states
  *`A_F` smooth ⟹ `a = 1`* and stops there. SMOOTH-KILL uses that as step (a)
  and then closes the case. I did not find this closure anywhere in the campaign
  record; it is typed PROVED-HERE, UNREVIEWED.
* **Immediate corollary.** Every statement below may assume `s >= 1`, i.e. the
  `(M')` sum over `Sing D` is non-empty. In particular the `a = 1`, `s = 0`
  escape that REP-96 §7 (R4) leaves open at `N = 4` is closed at every degree.

## 4. The local law `[P7]`, re-derived, and the master defect identity

`(M')` is a *global* identity; every kill below comes from its **pointwise
refinement**, which the campaign has as `[P7]` (`ALL-N (4.5)`, review §4.3
CONFIRMED). Because `[P7]` is quoted in `N20` inside a `[P5]`-flavoured context
(`r_p >= 2` there comes from `[P5]`), I re-derive it, to fix that the identity
itself is `[P5]`-free.

> **LEMMA 4.1 (fibre law).** For every `p ∈ D`,
> `N - a_p = r_p·W + K_p` with `K_p := sum_l sum_{t ∈ h_l^{-1}(eta^{-1}(p))} k_t
> >= 0`, where `k_t := mu_t - e_t mu_l >= 0` (`[P8]`/`ALL-N (4.3)`, from Orevkov
> Lemma 3.1) and `e_t` is the local degree of `h_l` at `t`.
>
> *Proof.* Fix `x` near `p`, `x ∉ D`. `F` is proper of degree `N` over
> `A^2 \ D`, so `#F^{-1}(x) = N`. Of these, exactly `a_p` stay near
> `F^{-1}(p) ∩ A^2` (`F` étale: each of the `a_p` points has exactly one
> preimage of `x` in a small neighbourhood). The remaining `N - a_p` escape, and
> by Orevkov Lemma 3.1 the number escaping near a boundary point `t ∈ l'` with
> `phi_l(t) = p` is exactly `mu_t` (normal form `u = x'`, `v = y'^{mu_t}`).
> Orevkov Lemma 2.1 separates the finite points of distinct chains, so no `t` is
> counted twice. Hence `N - a_p = sum_l sum_{t ∈ phi_l^{-1}(p)} mu_t`. Now
> `phi_l^{-1}(p) = h_l^{-1}(eta^{-1}(p))` and `#eta^{-1}(p) = r_p`; for each of
> those `r_p` places `z`, `sum_{t ∈ h_l^{-1}(z)} e_t = s_l` (degree of a finite
> map of smooth curves). So
> `sum_{t} mu_t = sum_l (mu_l · r_p · s_l) + K_p = r_p W + K_p`. ∎

At `p ∈ D_0` (`r_p = 1`, `K_p = 0`) this is `N = a + W` — the promoted `[P3]`,
a positive control. Subtracting from `N = a + W` gives the form used throughout:

> **(L)  `a - a_p = (r_p - 1)·W + K_p`,  `K_p >= 0`,  `a_p >= 0`.**

Summing `(L)` over `Sing D` and comparing with `(M'-def)`
`sum_p (a - a_p) = (a-1) + nu W` gives, with `nu = sum_p (r_p - 1)`,

> **(K)  `sum_{p ∈ Sing D} K_p = a - 1`.**

`(K)` is `ALL-N (4.6)`; note it is *equivalent* to `(M')` given `(L)`, so `(M')`
is not an extra input once `(L)` is available — and it also equals Orevkov's
`sum_l (mu_l + corr_l) = N - 1` after substituting
`corr_l = mu_l(s_l - 1) + sum_t k_t` and `(RH_l)`. Three independent routes,
one answer: a positive control on the whole apparatus.

Two immediate structural consequences of `a_p >= 0` in `(L)`:

> **(C1) `r_p·W <= N` for every `p ∈ Sing D`.** In particular if some `p` has
> `r_p >= 2` then `2(N - a) <= N`, i.e. **`2a >= N`**, and then `K_p <= N - 2W =
> 2a - N =: D_gap` at every multibranch `p`.
>
> **(C2)** If `p` is unibranch (`r_p = 1`) then `a - a_p = K_p`, and `a_p >= 0`
> gives only `K_p <= a`. **The `D_gap` ceiling is available exactly at
> multibranch points.** This single asymmetry is what separates the nodal case
> from the cuspidal one; it is not an artefact of the bookkeeping.

Finally, two localization lemmas, in both directions. Write `NI` for the set of
places `z ∈ D~` with `d eta_z = 0` — equivalently, places whose branch of `D` is
a **singular** branch.

> **LEMMA 4.2 (forward localization).** If `k_t > 0` then either `e_t >= 2` (so
> `t` is a critical point of `h_l`) or `h_l(t) ∈ NI`.
> *Proof.* If `e_t = 1` then `k_t = mu_t - mu_l > 0`, so `d phi_l(t) = 0` by
> `[P4]` (`[Z-6.5b]`), and `d phi_l(t) = d eta_{h_l(t)} ∘ d h_l(t)` with
> `d h_l(t) ≠ 0`; hence `d eta_{h_l(t)} = 0`. ∎
>
> **LEMMA 4.3 (reverse localization).** If `z ∈ NI` lies over `p` and some
> dicritical `l` has a point `t ∈ h_l^{-1}(z)` with `e_t = 1`, then `K_p >= 1`.
> In particular this holds whenever some `s_l = 1`.
> *Proof.* `d phi_l(t) = d eta_z ∘ d h_l(t) = 0`, so `mu_t > mu_l` by `[P4]`,
> and `k_t = mu_t - e_t mu_l = mu_t - mu_l >= 1`. ∎

Writing `beta := #{p ∈ Sing D : some branch of D at p is singular}` and using
`(RH_l)`, Lemma 4.2 gives the counting bound this lane runs on:

> **(C3)  `#{p ∈ Sing D : K_p > 0} <= R + beta`,  `R = sum_l (s_l - 1)`.**

## 5. Task (1): the nodal collapse at general `d = N`

### 5.1 The crude collapse, and exactly how far it goes

"Nodal" in the charge means `nu = s`, i.e. **every singular point has exactly
two branches**. (It therefore also covers tacnodes, ordinary tangencies and all
`A_{2k+1}`; I flag below where genuine smoothness of the branches is needed.)
With `nu = s`, `(M'-def)` is

```text
(5.1)   sum_{p ∈ Sing A_F} (a - a_p) = (a - 1) + s(N - a),   0 <= a_p <= a.
```

`LHS <= s·a`, so a solution needs `s·a >= (a-1) + s(N-a)`, i.e.

```text
(5.2)   s·(2a - N) >= a - 1.
```

Exact case analysis, `1 <= a <= N-2`, `N >= 3`, and `s >= 1` by SMOOTH-KILL:

* `2a <= N`. If `a >= 2` then `LHS <= 0 < a-1 = RHS`: impossible. If `a = 1`
  then `(5.2)` reads `s(2 - N) >= 0`, i.e. `s(N-2) <= 0`; `N >= 3` forces
  `s = 0`, contradicting SMOOTH-KILL. **No solution.**
* `2a > N`. `(5.2)` holds for `s >= (a-1)/(2a-N)`, so solutions exist
  numerically. But `a <= N-2` and `2a > N` require `N/2 < a <= N-2`, hence
  `N > 4`.

> **PROPOSITION 5.1.** For `N = 3` and `N = 4` there is no nodal `A_F` under
> `H2` — in fact, by `(C1)`, no `A_F` with **any** multibranch point, nodal or
> not, because `2a >= N` and `a <= N-2` already force `N >= 4`, and `N = 4`
> forces `a = 2`, `D_gap = 0`, so `K_p = 0` at every multibranch `p`, and then
> `(K)` puts all of `a - 1 = 1` on unibranch points.

Proposition 5.1 subsumes REP-96 §7 (R4) at `N = 4`: R4 kills nodal `A_F` there
in the two branches `a ∈ {1,2}` with `s >= 1`; SMOOTH-KILL closes `s = 0`; and
`(C1)` upgrades "nodal" to "multibranch". **`N = 3, 4` are closed under `H2` for
every profile with a multibranch point.** The `a = d-2` boundary is not
hand-waved: at `N = 4` it is `a = 2` and it dies because `s(2a-N) = 0 < a-1 = 1`;
at general `N` it dies inside the `2a > N` branch below.

But the crude bound `LHS <= s·a` is **not** enough for `N >= 5`, and reporting
otherwise would be the error the charge warns about. The `2a > N` branch is
genuinely non-empty as far as `(5.2)` is concerned. The sharpening comes from
`(L)`, `(K)`, `(C3)` and 7.B.

### 5.2 The sharp form: all branches smooth

Assume every branch of `A_F` is smooth. Then a singular point cannot be
unibranch, so `r_p >= 2` for all `p ∈ Sing D`, `beta = 0`, and `nu >= s` (nodal
is the case `nu = s`). By `(C1)`, `K_p <= D_gap := 2a - N` for every `p`; by
`(C3)`, at most `R` points have `K_p > 0`; by `(K)` their total is `a - 1`. So

```text
(5.3)   a - 1 <= R · D_gap ,     D_gap = 2a - N,   R = sum_l (s_l - 1).
```

If `a = 1` then `(K)` is `0 = 0`, but `(C1)` gives `2 >= 2a >= N >= 3`:
impossible. So `a >= 2`, `D_gap >= 1`. Now 7.B enters through `R`: since every
`mu_l >= 2` and `sum_l s_l mu_l = W`, we have `sum_l s_l <= floor(W/2)` and
`R = sum_l s_l - m <= floor(W/2) - 1` (`m >= 1`). Writing `R_max(W)` for the
exact maximum of `R` over dicritical profiles of weight `W` with all `mu_l >= 2`
(`= W/2 - 1` for `W` even; `max(W/p_min(W) - 1, (W-5)/2)` for `W` odd), the
system to solve is

```text
(5.4)   a - 1 <= (2a - N)·R_max(N - a),    N/2 < a <= N - 2,   N - a >= 2.
```

Using the clean bound `R <= W/2 - 1` and `a = (N + D_gap)/2`, `W = (N-D_gap)/2`,
`(5.4)` becomes `2(N + D_gap - 2) <= D_gap(N - D_gap - 4)`, i.e.

```text
(5.5)   N·(D_gap - 2) >= D_gap^2 + 6 D_gap - 4.
```

`D_gap = 1` gives `-N >= 11`, `D_gap = 2` gives `0 >= 12`: both impossible, so
`D_gap >= 3`; then `D_gap = 3 ⟹ N >= 23`, `4 ⟹ N >= 18`, `5 ⟹ N >= 17`,
`6 ⟹ N >= 17`, `7,8 ⟹ N >= 18`, and the right side of `(5.5)` divided by
`D_gap - 2` is increasing for `D_gap >= 6`. Parity (`D_gap ≡ N mod 2`) removes
`D_gap = 6` at `N = 17`.

> **THEOREM NODAL-ALL-N.** Let `F` be a noninvertible plane Keller map of
> geometric degree `N` with `A_F` irreducible, and suppose every branch of
> `A_F` is smooth (in particular, `A_F` nodal). Then **`N >= 17`**, and the
> admissible data are exactly the solutions of `(5.4)`. At `N = 17` the unique
> solution saturates both inequalities:
> `a = 11, W = 6, D_gap = 5, m = 1, (s_1,mu_1) = (3,2), R = 2`, with
> `sum_p K_p = 10` concentrated as `K = 5` at exactly two singular points, each
> then having `r_p = 2` and `a_p = 0`; every other singular point has `r_p = 2`,
> `K_p = 0`, `a_p = 5`; `s >= 2`.

The first admissible `(N, a, W, D_gap, R_max)` tuples, by exhaustive integer
enumeration of `(5.4)`:

```text
N=17: (11, 6, 5,2)                      N=20: (12, 8,4,3) (14,6, 8,2)
N=18: (12, 6, 6,2)                      N=21: (13, 8,5,3) (15,6, 9,2)
N=19: (13, 6, 7,2)                      N=23: (13,10,3,4) (15,8,7,3) (17,6,11,2)
```

**Robustness.** If THEOREM 7.B were withdrawn (allowing `mu_l = 1`, i.e.
`b > 0`), `R` could reach `W - 1` and the same enumeration gives only `N >= 8`
(first survivor `a=5, W=3, D_gap=2, R=2`). So 7.B carries exactly the range
`8 <= N <= 16`, and the `N <= 7` part of THEOREM NODAL-ALL-N is 7.B-free.

## 6. Task (2): the exact non-nodal classification

Let `Sing D = Sigma_1 ⊔ Sigma_{>=2}` by `r_p = 1` (unibranch — a **cusp** in
the wide sense: any unibranch singular germ) versus `r_p >= 2`. Cusps contribute
`0` to `nu`, so `nu - s = sum_p (r_p - 2)` can be negative; the crude bound
`(5.2)` is then not available and must not be quoted.

The classification is driven by `(C2)`: the ceiling `K_p <= D_gap` holds exactly
at multibranch points, and by Lemma 4.2 the localization `#{K_p>0} <= R`
degrades to `<= R + beta` exactly when `A_F` has a **singular branch**. Those
are two different degradations and they must be kept apart.

> **THEOREM PROFILE (classification under `H2`, all `N >= 3`).** Exactly one of
> the following holds for `A_F`.
>
> **(0) `A_F` smooth.** — **EMPTY** at every `N` (SMOOTH-KILL, §3).
>
> **(A) `A_F` singular, every singular point unibranch.** Then `s = 1` and
> `A_F` is a quasi-homogeneous cusp; see §7. Caged, not empty.
>
> **(B) `A_F` has a multibranch point.** Then `2a >= N`, `a <= N-2`, so
> `N >= 4`, and:
>  * **(B1) every branch of `A_F` smooth** (`beta = 0`; contains the nodal
>    case): **EMPTY for `N <= 16`** (THEOREM NODAL-ALL-N).
>  * **(B2) `A_F` has a singular branch, but no cusp** (`Sigma_1 = ∅`,
>    `beta >= 1`): `a - 1 <= (R + beta)·D_gap`; **EMPTY for `N <= 4`**, and
>    `beta >= 2` is forced for `5 <= N <= 10`, `beta >= 1` for `11 <= N <= 16`.
>  * **(B3) `A_F` has a cusp and a multibranch point.** The `D_gap` ceiling is
>    unavailable at the cusp, `K_cusp <= a`, and the counting collapses. **This
>    is the genuine residual**, and it is the campaign's one-cusp horn (§8).

*Proofs of the pieces not already given.* `(B)`: `(C1)` with `r_p >= 2`.
`(B2)`: identical to §5.2 with `(C3)` in place of `#{K_p>0} <= R`; the
enumeration of `a - 1 <= (R_max(W) + beta)(2a - N)` under `N/2 < a <= N-2`,
`W = N-a >= 2` gives minimal admissible `beta` equal to `∞` for `N <= 4`, `2`
for `5 <= N <= 10`, `1` for `11 <= N <= 16`, `0` for `N >= 17`. `(B3)`: at a
cusp, `(K)` alone gives `K_cusp <= a - 1`, and a single cusp can absorb the
whole excess; no contradiction arises, and none is claimed.

Two sharpenings that cost nothing and are used in §8.

> **PROPOSITION 6.1 (`s = 1` forces a cusp).** If `s = 1`, say `Sing D = {p}`,
> then `(M'-def)` reads `a - a_p = (a-1) + (r_p - 1)W`, so
> `a_p = 1 - (r_p - 1)W`. Since `a_p >= 0` and `W >= 2`, `r_p = 1` and
> `a_p = 1`.
>
> This is the exact all-degree form of the promoted "one-node exclusion"
> (`s = 1, nu = 1` impossible): the true statement is that a **single** singular
> point must be unibranch, with exactly one affine preimage. Conversely
> `r_p >= 2` somewhere forces `s >= 2`.

> **PROPOSITION 6.2 (charged singular branches).** If some dicritical has
> `s_l = 1`, then by Lemma 4.3 **every** point of `A_F` carrying a singular
> branch has `K_p >= 1`; combined with `(K)`, the number of such points is at
> most `a - 1`. In particular `beta <= a - 1`.

**What survives, stated as the charge asks.** Under `H2`, a Keller map at degree
`N` forces the singularity profile of `A_F` into the explicit family

```text
    N <= 3 :  EMPTY.
    N  = 4 :  exactly one cusp (a_cusp = 1, K = 1) plus k >= 0 double points
              with smooth branches (r = 2, a_p = 0, K_p = 0); a = 2, W = 2,
              one dicritical (s,mu) = (1,2);  or the k = 0 sub-case of (A).
 5..10  :  (A), or (B2) with beta >= 2, or (B3).
 11..16 :  (A), or (B2) with beta >= 1, or (B3).
 N >= 17 :  the above, plus (B1) with data solving (5.4).
```

The family is **not empty**, and the obstruction to emptiness is concentrated in
a single structural feature — a singular branch of `A_F`, and above all a
unibranch one. That is the honest boundary of the `(M')` instrument, and it is a
boundary in the mathematics (`(C2)`), not in the bookkeeping.

## 7. The cuspidal horn: Lin–Zaidenberg, CUSP-KILL, and the `pi_1` cage

Case **(A)** — every singular point of `A_F` unibranch — collapses to a single
curve up to a target automorphism, and then to a covering-space question.

> **PROPOSITION 7.1.** In case (A), `A_F` is homeomorphic to `C`, hence by the
> **Lin–Zaidenberg** theorem there is `α ∈ Aut(A^2)` with
> `α(A_F) = {x^p = y^q}`, `gcd(p,q) = 1`; SMOOTH-KILL forces `p, q >= 2`.
> Moreover `s = 1`, `a_p = 1`, `nu = 0`, `K_p = a - 1` (Prop. 6.1 and `(L)`).
>
> *Proof.* `eta : D~ ≅ A^1 -> D` (Lemma A) is a proper morphism, bijective
> because every point of `D` — smooth or singular — is unibranch. A proper
> continuous bijection is a homeomorphism, so `D` is a topologically embedded
> line. Lin–Zaidenberg (Invent. Math. 68 (1982) 1–17: an irreducible plane
> affine curve homeomorphic to `C` is `Aut(C^2)`-equivalent to `{x^p = y^q}`)
> applies. `s = 1` because `{x^p=y^q}` with `p,q >= 2` has exactly one singular
> point. ∎

Write `G_{p,q} := pi_1(C^2 \ {x^p=y^q}) = <α, β | α^p = β^q>` (the curve is a
cone over the `(p,q)` torus knot, so the complement deformation retracts to
`S^3 \ K_{p,q}`); `Z := Z(G_{p,q}) = <z>`, `z = α^p = β^q`, and
`G_{p,q}/Z ≅ Z/p * Z/q` with trivial centre. `F` is proper and étale over
`A^2 \ D`, so

```text
(7.1)  F : C^2 \ E  -->  C^2 \ D ,  E := F^{-1}(D),  finite etale of degree N,
       H := pi_1(C^2 \ E)  <=  G_{p,q}  of index N.
```

`D_0 = D \ {p} ≅ C^*`, so `E_0 := F^{-1}(D_0) -> C^*` is an `a`-sheeted
covering; let `j` be its number of connected components, so `j <= a`, and `E`
has exactly `j` irreducible components (`a_p = 1` puts a single, unibranch point
of `E` over `p`, so at most one component of `E_0` acquires it).

> **THEOREM CUSP-KILL.** In case (A), if `E` is irreducible (equivalently
> `j = 1`; in particular whenever `a = 1`) then `F` is an automorphism —
> contradiction. Hence `j >= 2` and `a >= 2`.
>
> *Proof.* `j = 1`: `E_0` is a connected `a`-sheeted cover of `C^*`, so
> `E_0 ≅ C^*`; `E_0` is smooth (`F` étale over the smooth `D_0`); `E = E_0 ∪
> {y_0}` with `(E,y_0) ≅ (D,p)` analytically (`F` a local biholomorphism), hence
> unibranch and singular. So `E~ = C^* ∪ {1 place} ≅ A^1` (affine, so not
> `P^1`), the normalization of `E` is bijective, and `E` is homeomorphic to `C`.
> Lin–Zaidenberg again: `E ≅ {x^{p'} = y^{q'}}`, and the analytic type of its
> unique singular point identifies `{p',q'} = {p,q}`. Hence `H ≅ G_{p,q}`.
>
> Put `Z_H := Z ∩ H`, `Delta := H/Z_H ≅ HZ/Z <= G/Z = Z/p * Z/q` of index `M`,
> and `N = M·[Z : Z_H]`. `Z/p * Z/q` is virtually free, infinite and
> nonelementary (`p,q >= 2`, `gcd(p,q) = 1` excludes `Z/2 * Z/2`), so the
> centralizer of its finite-index subgroup `Delta` is trivial; hence
> `Z(H) = Z_H` and `Delta ≅ H/Z(H) ≅ Z/p * Z/q`. Rational Euler characteristic
> is multiplicative in finite index: `chi(Delta) = M·(1/p + 1/q - 1)` and also
> `= 1/p + 1/q - 1 ≠ 0`, so `M = 1`, i.e. `HZ = G`. `Z` central then makes
> `H ◁ G` with `G/H ≅ Z/Z_H` cyclic of order `N`: the covering (7.1) is Galois,
> so `C(x,y)/C(F_1,F_2)` is a Galois extension. By **Campbell** (Math. Ann. 205
> (1973) 243–248) a Keller map with Galois field extension is invertible. ∎

For `j >= 2` the same computation is a cage rather than a kill. `H^{ab} =
H_1(C^2 \ E) = Z^j` is torsion-free, and `Delta^{ab}` is `H^{ab}` modulo the
image of the cyclic `Z_H`, so `Delta ≅ F_r * (Z/p)^{*u} * (Z/q)^{*v}` (Kurosh)
has `r ∈ {j-1, j}` and cyclic torsion, forcing `u <= 1`, `v <= 1`; and
`chi(Delta) = 1 - r + u(1/p - 1) + v(1/q - 1) = M(1/p + 1/q - 1)`.

> **THEOREM CUSP-CAGE.** In case (A) with `j >= 2`, writing `t := pq - p - q`:
> `(u,v) = (1,1) ⟹ r = (M-1)t/(pq)`, and `gcd(pq, t) = 1`, so `pq | M - 1` and
> **`N >= M >= pq + 1`**; `(u,v) = (1,0) ⟹ p | M-1` and `q | M`;
> `(0,1) ⟹ q | M-1`, `p | M`; `(0,0) ⟹ pq | M`. In every case `M >= 2`, so the
> covering (7.1) is **not** Galois-cyclic and `N` has a divisor `M >= 2` of the
> listed congruence type. Equivalently, in the global Milnor fibration
> `h ∘ F : C^2 \ E -> C^*` (pullback of the quasi-homogeneous fibration of
> `x^p - y^q`), the monodromy on `H_1` of the generic fibre has eigenvalue `1`
> with multiplicity `j - 1 >= 1`.

**Honest limits.** The cage does not empty case (A). Worked check at `N = 4`
(brute force over `S_4`, §10 script 4): `a = 1` is killed by CUSP-KILL (`j = 1`);
`a = 2` requires the meridian `m = α^s β^t` (`sq + tp = 1`) to map to a
transposition under a transitive `rho : G_{p,q} -> S_4`, which happens (e.g.
`(p,q) = (3,4)`), and `(p,q) = (3,4)`, `M = 4`, `(u,v) = (1,0)`, `r = j = 2`
satisfies every congruence above. So case (A) at `N = 4` is **not** closed by
this lane; it is typed `OPEN[MPRIME-CUSP-J2]` in §9.

## 8. Task (4): interface with the one-cusp `A2` horn; the `N = 4` residual pinned

The charge asks for a theorem-interface composition pass: does the all-`N` nodal
kill compose with the one-cusp horn work, and does the horn sit inside a profile
§6 kills or keeps? The answer is **keeps**, and the interface is exact.

### 8.1 The `N = 4` `H2` residual, pinned

> **THEOREM N4-PIN.** Let `F` be a noninvertible plane Keller map of geometric
> degree `4` with `A_F` irreducible. Then, in case (B) (some multibranch point):
>
> ```text
>   a = 2 ,  W = 2 ,  m = 1 ,  (s_1, mu_1) = (1, 2) ,  R = 0 ,  D_gap = 0 ;
>   A_F has EXACTLY ONE point p_0 carrying a singular branch;
>   p_0 is unibranch (a cusp), with a_{p_0} = 1 and K_{p_0} = 1 ;
>   every other singular point has r_p = 2, both branches SMOOTH,
>       a_p = 0 and K_p = 0 ;
>   generic meridian cycle type (2,1,1); at p_0 (3,1); at each double point (2,2);
>   chi_c(F^{-1}(A_F)) = 1 - 4k,  k := #double points = nu .
> ```
>
> *Proof.* `(C1)` gives `2a >= 4` and `a <= N-2 = 2`, so `a = 2`, `W = 2`,
> `D_gap = 0`. `W = 2 = sum_l s_l mu_l` with every `mu_l >= 2` (7.B') forces the
> single dicritical `(1,2)`, so `R = 0`. `(K)`: `sum_p K_p = 1`. At a
> multibranch `p`, `K_p <= D_gap = 0`, so `K_p = 0` and
> `a_p = 4 - 2r_p >= 0` forces `r_p = 2`, `a_p = 0`. Lemma 4.2 with `R = 0`
> makes every `K_p > 0` point carry a singular branch; Lemma 4.3 (applicable
> because `s_1 = 1`) makes every singular-branch point have `K_p >= 1`. With
> `sum K_p = 1` these two give **exactly one** singular-branch point `p_0`, with
> `K_{p_0} = 1`; then `a_{p_0} = 4 - 2 r_{p_0} - 1 >= 0` forces `r_{p_0} = 1`,
> `a_{p_0} = 1`. Fibre partitions are `{e_y}` read off Lemma 4.1; `chi_c` from
> Theorem (E) with `chi_c(A_F) = 1 - nu`. ∎

### 8.2 Control against the promoted rank-four census — four independent hits

The reviewed rank-four surface census
(`block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md:390`) is

```text
generic B: (2,1,1),   cusp c: (3,1),   omitted node n: (2,2),   e(T) = -3,
```

with `B = A_F` irreducible and normalization `beta_B : A^1 -> B`. THEOREM N4-PIN
reproduces **all four numbers** — `(2,1,1)`, `(3,1)`, `(2,2)`, and
`chi_c(F^{-1}(A_F)) = 1 - 4·1 = -3` at `k = 1` — from `(M')`, `(L)`, `(K)` and
7.B alone, with no census input. Together with the three-route agreement on
`(K)` (§4) this is the strongest positive control available to this lane, and it
is what licenses the `N >= 17` claim built on the same apparatus. `beta_B :
A^1 -> B` is Lemma A, independently.

### 8.3 The exact interface

* **The horn sits in case (B3)** of THEOREM PROFILE: a cusp *and* a multibranch
  point. THEOREM NODAL-ALL-N does **not** apply to it — its hypothesis "every
  branch of `A_F` smooth" fails precisely at the cusp — so there is no
  composition conflict and no double counting. The nodal kill and the horn are
  disjoint in scope by construction, not by accident: `(C2)` is the single
  inequality that separates them.
* **What the nodal work newly gives the horn.** Two pins the horn lane did not
  have from `(M')`: (i) `A_F` has **exactly one** cusp — more precisely exactly
  one point with a singular branch — so no second cusp and no singular branch at
  the node; (ii) every non-cusp singularity of `A_F` is a **double point of two
  smooth branches** (node or tacnode, `r = 2`), with `a_p = 0`: *the node of
  `A_F` has no affine preimage at all*. Neither is derivable from the census as
  frozen.
* **What the horn still owes.** `(M')` does **not** pin `k = nu`, the number of
  double points. The census value `k = 1` is an input from elsewhere; this lane
  neither confirms nor refutes it, and `k = 0` is exactly the case-(A)
  sub-branch, which CUSP-KILL reduces to `j >= 2` but does not close.
* **Relation to `OPEN[A2-CELL-32]`.** That OPEN lives one level down, inside the
  `(alpha,beta)` `A`-degree census of the horn's normal form; nothing here
  touches its cell `(3,2)` arithmetic. The composition is one-directional:
  N4-PIN is an **input** the `A2` lane may consume (it fixes the ambient
  profile: one cusp, `r = 2` elsewhere, `a = 2`, one `(1,2)` dicritical), not a
  competitor to its computation. No claim of this report depends on
  `A2-CELL-32` resolving either way.
* **Degree generality of the interface.** At `N >= 5` the same argument pins
  much less: `D_gap` can be positive, so multibranch points may carry excess and
  `R` may be nonzero, and `s_l = 1` (needed for Lemma 4.3) is no longer forced.
  The `N = 4` sharpness is a genuine small-degree phenomenon and must not be
  extended by analogy.

## 9. Task (3): typed OPENs and the cheapest decisive instrument for each

Four survivors. Each is named with its exact data and its cheapest decisive
instrument from the campaign's current toolset.

```text
OPEN[MPRIME-B1-N>=17]
```
Case (B1) at `N >= 17`: every branch of `A_F` smooth, data solving `(5.4)`; the
`N = 17` cell is fully rigid (§5.2). **Instrument:** not a computation — the
cheapest kill is an *upper* bound on `R = sum_l (s_l - 1)`, i.e. on the total
finite ramification of the dicritical covers `h_l : A^1 -> A^1`. `R <= 1`
would give `a - 1 <= D_gap = 2a - N`, i.e. `a >= N - 1`, against `a <= N - 2`:
**the whole of (B1) dies at every `N` as soon as `R <= 1` is proved**
(`R = 0` gives `a = 1`, already excluded in case (B)). `R = 0`
is exactly "every dicritical is birational onto `A_F`"; `R <= 1` is one step
weaker. This is a valuation-theoretic statement about a single polynomial map
and is the highest-value successor in this lane.

```text
OPEN[MPRIME-B2-SINGBRANCH-COUNT]
```
Case (B2): no cusp, `beta >= 1` singular branches at multibranch points,
`a - 1 <= (R + beta) D_gap`. **Instrument:** a bound `beta <= B`. By the
enumeration of §6, `B = 0` gives `N >= 17`, `B = 1` gives `N >= 11`, `B = 2`
gives `N >= 5`; and `beta <= a - 1` is already free whenever some `s_l = 1`
(Prop. 6.2). The natural source is the delta-invariant budget of the projective
model: `A_F` is rational with one place at infinity (Lemma A), so
`sum_{Sing} delta_q = (n-1)(n-2)/2` with `n = deg closure(A_F)`; a bound
`n <= f(N)` converts directly into a bound on `beta`. **`OPEN[DEG-AF-VS-N]`** —
is `deg A_F` bounded in terms of the geometric degree `N`? — is the sub-question,
and I could not find it promoted anywhere in the record.

```text
OPEN[MPRIME-CUSP-J2]
```
Case (A) with `j >= 2`: `A_F ≅ {x^p=y^q}` (`p,q >= 2`, coprime), `s = 1`,
`a_p = 1`, `a >= j >= 2`, `E = F^{-1}(A_F)` with `j` components, and
`H = pi_1(C^2 \ E) <= G_{p,q}` of index `N` with the Kurosh/congruence cage of
THEOREM CUSP-CAGE. **Instrument (cheapest, finite, decidable):** the `S_N`
representation gate the campaign already runs. Enumerate transitive
`rho : G_{p,q} -> S_N` with `rho(α)^p = rho(β)^q`, meridian cycle type
`1^a · prod_l mu_l^{s_l}` (`mu_l >= 2` by 7.B, `a = #Fix >= 2`), and
`[G/Z : rho`-point-stabilizer image`] = M` satisfying the CUSP-CAGE
congruences. This is `TB-GERM`/`CABLE-3`-shaped work on a group presented by two
generators and one relation — cheaper than any of the `(9,6)` gates already run.
A worked `N = 4` instance is in §7; it shows the gate is non-vacuous and that it
does not, by itself, close `N = 4`.

```text
OPEN[MPRIME-B3-CUSP-PLUS-NODE]
```
Case (B3), the one-cusp horn: `A_F` has one or more cusps together with
multibranch points; at `N = 4` it is pinned completely by THEOREM N4-PIN.
**Instrument:** this is not an `(M')` question any more — `(C2)` says the
identity is structurally blind here. The decisive instruments are the ones the
horn lane already uses (braid monodromy / ZvK on the pinned profile, or the
`pi_1(C^2 \ A_F)` representation gate with the N4-PIN cycle types `(2,1,1)`,
`(3,1)`, `(2,2)` as the local data). The new N4-PIN facts — exactly one
singular-branch point, `a_node = 0`, `a_cusp = 1` — are the input to feed them.

**Not raised as OPENs, but flagged for the coordinator.**

* The promoted bullet "`H3` as a conclusion" (all-degree integration §1.1) is,
  as derived via `[P5]`, vacuous after THEOREM 7.B. §2 supplies an independent
  proof; the bullet should be re-cited to Lemma A, not to `[P5]`.
* `beta_min(N) = ∞` for `N <= 4` in the case-(B2) enumeration is *not* a
  statement about cusps; the `N <= 4` kill in case (B) comes from
  `2a >= N`, `a <= N-2` and is independent of `beta`.

## 10. Task (5): typed verdict block, controls, deviations

## 11. FALLACY-v2 audit
