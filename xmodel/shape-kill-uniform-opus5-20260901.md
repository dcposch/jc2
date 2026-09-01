# SHAPE-KILL — uniform kills for the residual shape families

Lane: SHAPE-KILL (flagship on OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND], attacked from
the shape side). Date: 2026-09-01. Model: Opus 5.

## 0. Inputs, hashes, and scope

The three frozen inputs were hashed before any mathematical use and all three matched
the charge manifest exactly:

```text
cff4116c19728da875c141133f3b7e739e979ebcb606694272cb14ee6e5130c1  campaign-pin-gpt55-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
723a3cc18b1b01cb451c19dbe27bb63778d09a125048e1c94591f4f94ba4f5ac  row-nf-exhaustiveness-hostile-review-sol56-20260901.md
```

No CAS was run, no canonical ledger or charged file was edited, and `jc2-lean` was not
inspected. **Disclosure of the only machine work:** the finite group-theoretic case analyses
of §3.2 and §4.3 were done by hand and then re-run as brute-force enumerations over the
`24`-element group `S_4` (two short Python scripts, no library, sub-second, nothing written to
disk). Both confirmed the hand results exactly, including the `m mod 3` trichotomy of §3.2, the
three non-constant pairs per `W`, the fact that `Pi` is a double transposition in all of them,
and the single `phi`-orbit of §4.3. These are desk-scale checks of bounded size, not
computations of uncertain duration. Beyond the three charged inputs I read only already-banked
campaign artifacts in `xmodel/` for the exact statements of Theorem A, Theorem A', Lemma 3.3,
the tubular factorisation, and the (M-INF) conversion; those are cited by path and line. No new
exit price is asserted, so FALLACY-v2 requires no `charge_basis` line.

**Headline.** Family 1 is **KILLED uniformly** — but not by the mechanism the charge
proposed. The proposed mechanism (block-product collapse at `n'=1` forcing `|im| <= 6`) is
**REFUTED uniformly**, and I give a one-line proof that *no* outer-level argument can ever
kill a noncoprime shape with `g >= 2`, `d' >= 3` — the constant block-product tuple is
always an outer fixed point. Family 1 dies instead by a minimal-gauge degree descent
(Theorem SK-1). Families 2 and 3 do **not** die uniformly; but the `g = 2` slice of both is
settled completely — two thirds of family 2 at `g = 2` die (Theorem SK-4, only `u = 3 (mod 6)`
survives), and family 3's `g = 2` constant stratum dies. One further uniform result holds at
every `g`: in family 3 the total product `Pi` is a `3`-cycle outside the constant stratum
(Theorem SK-5), so the `S_3`-resolvent never descends to `P^2` and the NO-TORUS/Shirane route
is permanently unavailable there. The exact surviving (family, parameter) pairs are typed
in §6.

## 1. The cage, restated exactly

Notation throughout. `D = D_1` is the repaired `N = 4` residual branch curve, with a
birational polynomial parametrisation `gamma(t) = (p(t), q(t))`, `d = deg p > n = deg q >= 1`,
`g = gcd(d,n)`, `d = g d'`, `n = g n'`, `gcd(d',n') = 1`. `phi : pi_1(A^2 - D) ->> S_4` sends
every curve meridian to a transposition. `a := d - n`. The delta sequence is
`Delta = (delta_0, ..., delta_s)` with `delta_0 = d`, `delta_1 = n`; `S_D = <Delta>` is the
degree semigroup (Galindo--Monserrat Theorem 2.1, in the fixed row gauge repaired at
`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:38-52`); `delta_aff = #(N - S_D)`;
`delta_aff + delta_inf = (d-1)(d-2)/2`.

Promoted facts consumed (not re-proved here):

* **Cage.** Escape from the coprime Main Theorem forces `g >= 2` and reduced shape
  `(d/g, n/g) in {(u,1) : u>=2} u {(u,2) : u>=3 odd} u {(4,3)}`
  (Chau 1999 Thm B via `d1-degree-bound-sol56-20260831.md:208-248`; promoted at
  `campaign-pin-gpt55-20260901.md:141-149`). The derivation applies a *generic source*
  linear change only, so it is valid in **every target gauge**.
* **Target-automorphism invariance.** For `T in Aut(A^2)`, `T(D)` is again a residual branch
  curve of the postcomposed Keller map, with `N = 4`, the same monodromy classes and the
  same affine singularity types; and `T` induces an isomorphism of complements carrying
  meridians to meridians, so the forbidden representation transports both ways
  (`campaign-pin-gpt55-20260901.md:96-104`;
  `row-nf-exhaustiveness-hostile-review-sol56-20260901.md:140-152`).
* **Tubular factorisation.** `rho_inf = C_g(delta_{d'}^{n'}) . iota` with
  `iota in B_{g,1} x ... x B_{g,d'}`, and
  `e(iota) = (d-1)^2 - 2 delta_inf - n(d-g)`
  (`pi1s4-close-residual-r2-opus5-20260831.md:186-206`; CONFIRMED at
  `pi1s4-close-residual-hostile-review-sol56-20260831.md:51-53`). Substituting
  `2 delta_inf = (d-1)(d-2) - 2 delta_aff` gives the form used below,

  ```text
  (1.1)    e(iota) = (d-1) + 2 delta_aff - n(d-g).
  ```

* **Lemma 3.3 / Theorem A'(1)-(4).** `BP(T) = (Pi_1,...,Pi_{d'})` (ordered block products) is
  a fixed point of the Hurwitz action of `delta_{d'}^{n'}`; the sequence is `n'`-periodic;
  conjugation by `Pi` acts as the shift by `-(d' mod n')`; `H = <Pi_1, Pi>`;
  `Pi^{n'} in Z(H)`; and at `n' = 1` all `Pi_i` are equal and `Pi = Pi_1^{d'}`
  (`pi1s4-close-residual-r2-opus5-20260831.md:217-252`; CONFIRMED at
  `pi1s4-close-residual-hostile-review-sol56-20260831.md:59`). `A'(5)` is **held** (GAP), and
  is not used anywhere below.
* **(M-INF).** With `a >= 2`, `M_inf = max(d, a + beta_h - 1)` and `M_inf <= 3d-3` implies
  `pi_1(C^2 - D) = Z`, killing the `S_4` quotient; equivalently the kill fires iff
  `beta_h <= 2d + n - 2`. The infinity conversion is
  `2 delta_inf = sum_i (e_{i-1} - e_i) beta_i - a + 1`, `e_0 = a`, `e_i = gcd(e_{i-1}, beta_i)`,
  `e_h = 1` (`row-sweep-sol56-20260831.md:60-80`; corrected case split at
  `pi1s4-close-residual-hostile-review-sol56-20260831.md:110-116`).
* **Row-kill.** For the explicit ROW-NF families `D_{b,c}`, `D'_{b,c}` (`c != 0`) there is no
  meridional-transposition surjection onto `S_4`
  (`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md:32-53`). This is a
  **degree-6/degree-8 explicit-family** statement; its literature input is Shirane's
  *normal triple covers with branch divisors of degree 6*, and §3.4 below types exactly why
  that input does not travel.

Convention: permutation words are composed right to left (`ABCA` means: apply the
rightmost `A` first). Every conclusion below concerns orders, cycle types, supports and
generated subgroups, all of which are invariant under the opposite convention, which acts as
an anti-isomorphism.

One elementary fact used repeatedly and recorded once. In the row gauge the branch at
infinity is `(v,u) = (s^a . unit, sum_{k >= d} c_k s^k)`
(`row-sweep-sol56-20260831.md:56-64`), so **every characteristic numerator satisfies
`beta_i >= d`**. This is used only as a lower bound.


## 2. Family (u,1): n | d — the n'=1 tube-collapse rerun

### 2.1 What is actually in `S_D` at shape `(u,1)`

Here `n = g`, `d = un`, `d' = u`, `n' = 1`. The gcd chain of `Delta` starts `d_1 = d`,
`d_2 = gcd(d,n) = n`, so `n_1 = d/n = u` and the semigroup relation `n_1 delta_1 in <delta_0>`
reads `u n = d in <d>`, which is automatically satisfied and carries no information. The
operative fact is the reverse one:

```text
(2.1)     delta_0 = d = u n = u delta_1  in  <delta_1>,
          hence  S_D = <n, delta_2, ..., delta_s>  and  d is a redundant generator.
```

So the answer to the question posed in the charge is: at shape `(u,1)` there is **no**
analogue of "`3 in S_D`". What is in `S_D` is `n = g` itself, and the degree `d` carries no
information beyond it. Concretely `q in A_D` has degree `n` and `q^u` has degree exactly `d`,
so with `lam := lc(p) / lc(q)^u`,

```text
(2.2)     deg( p - lam q^u ) < d .
```

This is the semigroup form of the EXHAUST fold step, but run *downwards*: at `Delta = (6,4,3)`
the extra generator `3 < 4` produced a fold `P = alpha R^2 + ...` at the *same* degree, whereas
at shape `(u,1)` the redundancy is of `delta_0` itself and produces a strict degree drop. That
difference is the whole content of §2.3.

`p - lam q^u` is not constant: if it were, `C(p,q) = C(q)`, which is a proper subfield of
`C(t)` because `n = g >= 2`, contradicting birationality
(`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:238-241` uses the same exclusion).

### 2.2 The proposed collapse rerun is REFUTED — and no outer-level argument can work

At `n' = 1`, `A'(4)` gives `Pi_1 = ... = Pi_{d'} = c` and `Pi = c^{d'}`. The charge asks
whether that equality forces `|im(phi)| <= 6` uniformly, as it does at `(4,2)`. It does not,
and the failure is structural rather than accidental.

> **LEMMA SK-0.** *Let `g >= 1`, `d' > n' >= 1`, `gcd(d',n') = 1`, let `c in S_4`, and let
> `BP = (c, c, ..., c) in S_4^{d'}`. Then `BP` is a fixed point of the Hurwitz action of the
> full torus braid `delta_{d'}`, hence of `delta_{d'}^{n'}`.*
>
> *Proof.* By `pi1s4-close-residual-r2-opus5-20260831.md:248-250`, `delta_{d'}` acts by
> `(u_1,...,u_{d'}) -> (Pi u_{d'} Pi^{-1}, u_1, ..., u_{d'-1})` with `Pi = u_1 ... u_{d'}`. On
> the constant tuple `Pi = c^{d'}` centralises `c`, so the first entry returns `c` and the
> shift returns the same constant tuple. `[]`

Lemma SK-0 says that `A'(1)-(4)` — the entire promoted outer battery — is **satisfiable at
every noncoprime shape and every `g`**. Therefore the outer level alone can never produce a
kill; every kill must consume the inner braid `iota`. This is the exact, uniform form of the
promoted refutation at `pi1s4-close-residual-hostile-review-sol56-20260831.md:64` ("REFUTED —
outer level alone never suffices when `n|d`" was itself refuted as *stated*, but the promoted
`(6,2)` counterexample there — blocks `((12),(12)), ((23),(23)), ((34),(34))`, all products
`1`, entries generating `S_4` — is exactly an instance of Lemma SK-0). The `(4,2)` kill is not
a template: it survives only because at `(d',g) = (2,2)` a *further* realisability accident
holds (two blocks of two transpositions with equal products cannot generate `S_4`), and that
accident fails as soon as `d' >= 3`.

So the answer to charge item 1's central question is **NO**: block-product equality does not
force `|im| <= 6` at general `(ug, g)`.

One positive by-product, obtained by adding the *free* part of the inner analysis at `g = 2`:

> **LEMMA SK-2 (`g = 2` trivial-collapse kill).** *Let `g = 2` and suppose all block products
> are trivial, `Pi_i = 1` for every `i`. Then `T` is `rho_inf`-fixed only if all `d'` blocks
> are equal, and then `im(phi) = Z/2`.*
>
> *Proof.* `Pi_i = 1` with both entries transpositions forces `B_i = (tau_i, tau_i)`. Any
> `sigma^k` in `B_2` fixes such a block: `sigma` sends `(t,t')` to `(t t' t^{-1}, t)`, which is
> `(tau,tau)` again, and `sigma^{-1}` sends it to `(t', t'^{-1} t t')= (tau,tau)`. Hence
> `iota . T = T`, and `rho_inf . T = T` reduces to `C_2(delta_{d'}^{n'}) . T = T`. By
> Lemma 3.3's cabled-crossing formula the action of `C_2(sigma_i)` on blocks is
> `(A,B) -> (Pi_A B Pi_A^{-1}, A) = (B,A)` because `Pi_A = 1`; so `C_2` of any braid acts
> through `B_{d'} ->> S_{d'}`. The image of `delta_{d'}` is a `d'`-cycle `gamma`, and
> `gcd(n',d') = 1` makes `gamma^{n'}` a `d'`-cycle too, whose fixed tuples are exactly the
> constant ones. Then every entry equals one transposition `tau`. `[]`

Lemma SK-2 is strictly stronger than `A'(4)`: it *does* dispose of the promoted `(6,2)`
counterexample tuple, which `A'(4)` alone cannot. It does not extend to `g >= 3`, because for
`g >= 3` a block with trivial product is not `B_g`-fixed and the reduction `iota . T = T`
fails; the honest scope is `g = 2`. Combining SK-2 with the two nontrivial values of `c`:

> **COROLLARY SK-2'.** *Every row with `g = 2` and `n | d` — i.e. `(d,n) = (2u, 2)`, all
> `u >= 2` — is dead.* Indeed `c = Pi_1` is a product of two transpositions: `c = 1` is
> Lemma SK-2; `c` a `3`-cycle confines every entry to the three letters of its support, giving
> `im <= S_3`; `c` a double transposition forces every block to be its two disjoint factors,
> giving `im <= V_4`.

This generalises the promoted `(4,2)` closure to the whole `n = 2` column at once, by a
shorter argument than the `(4,2)` exponent-sum computation.

### 2.3 THEOREM SK-1: the family is removable from the cage, at every degree

> **THEOREM SK-1 (uniform kill of the `(u,1)` family).** *Let `D` be an escaping `N = 4`
> residual branch curve. Put `d_min := min { deg T(D) : T in Aut(A^2) }`, the minimum being
> over projective degrees of the images. Then `d_min` is attained, and in any attaining gauge
> the degree pair `(d,n)` satisfies `n` does not divide `d`. Consequently the reduced shape of
> `D` in that gauge is `(odd u, 2)` or `(4,3)`, never `(u,1)`.*

*Proof.* The set `{deg T(D)}` is a nonempty set of positive integers, so the minimum is
attained; fix an attaining `T_0` and write `D_0 = T_0(D)`. By promoted target-automorphism
invariance `D_0` is again a residual branch curve carrying the forbidden representation, and it
has a birational polynomial parametrisation `(P,Q)`. If `deg P = deg Q` compose with the linear
`(x,y) -> (x - lambda y, y)`, `lambda` the ratio of leading coefficients, which is degree
preserving on the plane and strictly drops `deg P`; if `deg P < deg Q` compose with the swap.
So we may take `d := deg P > n := deg Q`, and then `deg D_0 = d` (the degree-`d` homogenisation
sends the single point of `P^1 - A^1` to `[1:0:0]`, a generic line pulls back with degree `d`,
so the projective image has degree `d`:
`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:55-60`). Hence `d = d_min`.

Escape forces `g = gcd(d,n) >= 2`, so `n >= 2`. Suppose `n | d`, say `d = un`, `u >= 2`. Put
`lam := lc(P)/lc(Q)^u` and apply `T_1(x,y) = (x - lam y^u, y) in Aut(A^2)`. Then `T_1(D_0)` is
parametrised by `(P - lam Q^u, Q)` with first degree `d_1 < d` by (2.2) and `d_1 >= 1` by the
birationality exclusion of §2.1. The projective degree of `T_1(D_0)` is at most
`max(d_1, n) < d`, contradicting minimality of `d`. Hence `n` does not divide `d`. The last
sentence is the promoted Chau trichotomy applied in the `d_min` gauge, which is legitimate
because Chau's derivation uses only a *source* linear change and therefore holds in every
target gauge. `[]`

**Exact typing (FALLACY-v2, floor/attainment and carrier/attainment).** SK-1 does **not** say
that no residual curve admits a `(u,1)` presentation; the promoted `T_k(u,v) = (u, v + u^k)`
construction shows every residual curve admits infinitely many of them
(`campaign-pin-gpt55-20260901.md:126-135`). SK-1 says that the `(u,1)` *row* is redundant: the
cage may be imposed in a minimal gauge, where the row is empty. Since the property being
excluded — existence of a meridional-transposition surjection onto `S_4` — is gauge invariant
in both directions (`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:140-152`), a sweep
that clears `(odd u,2)` and `(4,3)` in the minimal gauge clears every residual curve. That is
the precise sense in which family 1 "dies at every degree", and it is the sense the campaign
pin needs.

This is not new mathematics in isolation — `campaign-pin-gpt55-20260901.md:250-260` already
observes the descent and `d1-degree-bound-sol56-20260831.md:244-248` records the Jung-reduced
remark — but neither states it as a *kill*: both stop at "not a minimal-gauge representative".
The step SK-1 adds is that minimality is attained and that the Chau trichotomy may be re-run
in the attaining gauge, which converts the descent into an elimination.

### 2.4 Independent corroboration: a uniform (M-INF) window

For a second, disjoint check I record a sufficient condition for (M-INF) that is uniform in
the characteristic sequence at infinity. Write `p(a)` for the least prime factor of `a = d-n`.

> **LEMMA SK-3.** *Let `a >= 2` and let the residual be nodal, so `delta_aff = #nodes`. Then
> `M_inf <= 3d-3` holds — hence `pi_1(C^2-D) = Z` and the `S_4` quotient dies — whenever*
>
> ```text
> (2.3)     d (n - p(a))  <=  p(a) (n - 2) + 2 delta_aff + 1 .
> ```

*Proof.* `beta_i >= d` for every `i` (§1). With `E := e_{h-1} >= 2`, `E | a`, and
`sum_{i<h} (e_{i-1} - e_i) = a - E`, the conversion identity gives
`2 delta_inf + a - 1 = sum_i (e_{i-1}-e_i) beta_i >= (a-E) d + (E-1) beta_h`, so
`beta_h <= Phi(E) := (C + E d)/(E-1)` with `C := 2 delta_inf + a - 1 - a d`. Since
`Phi'(E) = -(C+d)/(E-1)^2` and `C + d = 2 delta_inf - (a-1)(d-1)`, `Phi` is decreasing in `E`
exactly when `2 delta_inf > (a-1)(d-1)`; in the complementary regime the worst case is
`E = a` (`h = 1`), where `beta_1 = (2 delta_inf + a - 1)/(a-1) <= (d-1) + 1 <= 2d+n-2` and
(M-INF) holds outright. In the decreasing regime the worst case is `E = p(a)`. Substituting
`2 delta_inf = (d-1)(d-2) - 2 delta_aff` into `Phi(p) <= 2d + n - 2` and clearing gives
exactly (2.3). `[]`

Two consequences. If `n <= p(a)` the left side of (2.3) is `<= 0` and (M-INF) fires
unconditionally; in particular **every row with `n = 2` is dead by (M-INF) alone**, matching
the promoted `(8,2)` and `(10,2)` verdicts (`campaign-pin-gpt55-20260901.md:263-280`) without
any row census. And for `n = 3` with `a` even, (2.3) reads `d <= 2 delta_aff + 3`. Lemma SK-3
is sufficient, not sharp — it loses the exact values of `beta_i` for `i < h` — so it does not
reproduce every promoted row kill (e.g. the small-`c` end of `(9,3)`); it is recorded here
only as a family-level cross-check on SK-1's conclusion, and it is used nowhere below.

## 3. Family (odd u, 2) — coprime Theorem A at the outer level

Here `d' = u` odd `>= 3`, `n' = 2`, `d = gu`, `n = 2g`, `a = g(u-2)`. Write `u = 2m+1`.

### 3.1 The exact outer relation

`A'(2)` at `(d',n') = (u,2)` says: the block-product sequence is `2`-periodic, so it has at
most two values `X := Pi_1 = Pi_3 = ...` and `Y := Pi_2 = Pi_4 = ...`; and, since
`r = d' mod n' = 1`, conjugation by `Pi` is the shift by `-1`, i.e. `Pi X Pi^{-1} = Y` and
`Pi Y Pi^{-1} = X`. The total product is the alternating word of length `u`,

```text
Pi = Pi_1 Pi_2 ... Pi_u = X Y X Y ... X = W^m X ,     W := X Y .
```

Substituting into `Pi X Pi^{-1} = Y` gives `Y = W^m X W^{-m}`, hence `W = XY = X W^m X W^{-m}`,
i.e.

```text
(3.1)     X W^m X = W^{m+1} ,        W = XY ,   u = 2m+1 .
```

Conversely (3.1) implies both conjugation relations: from `W^{m+1} X^{-1} = X W^m` one gets
`Pi Y Pi^{-1} = W^m X . X^{-1} W . X^{-1} W^{-m} = W^{m+1} X^{-1} W^{-m} = X`. So **(3.1) is
exactly the outer fixed-point condition at shape `(u,2)`** — a single equation in two unknowns.
At `m = 1` (`u = 3`, the reduced shape of the promoted `(6,4)` row) it reads `X . XY . X = (XY)^2`,
i.e. `XYX = YXY`: the braid relation. So the outer condition at general odd `u` is a
*deformed braid relation*, `X W^m X = W^{m+1}`, and the promoted `(6,4)` row sits at its
first instance. Two identities that fall straight out and are used below:

```text
(3.2)     Pi = W^m X = X^{-1} W^{m+1} ,       Pi^2 = W^{2m+1} = W^u .
```

### 3.2 Complete solution at `g = 2`: only `u = 3 (mod 6)` survives

At `g = 2` each block product is a product of two transpositions, so `X, Y in A_4`, and every
element of `A_4` has order `1`, `2` (double transpositions) or `3` (`3`-cycles). Since `A_4`
contains no element whose square is a double transposition, (3.1) can be solved outright.

* **`ord W = 1`.** `Y = X^{-1}` and (3.1) gives `X^2 = 1`. If `X = 1` then `X = Y = 1` and
  Lemma SK-2 gives `im(phi) = Z/2`. If `X` is a double transposition then `Y = X` and every
  block is the ordered pair of the two disjoint factors of `X`, so `im(phi) <= V_4`. Dead.
* **`ord W = 2`.** `m` even gives `X^2 = W`; `m` odd gives `X^2 = W^{-1}`. Both need `X^2` to
  be a double transposition — impossible in `A_4`. **No solutions.**
* **`ord W = 3`, `m = 0 (mod 3)`.** (3.1) reads `X^2 = W`, so `X` is a `3`-cycle with
  `X = W^2`, whence `Y = X^{-1}W = W^2 = X`: the constant tuple with `c` a `3`-cycle. Every
  block is a pair of transpositions inside the three letters of `supp(c)`, so
  `im(phi) <= S_3`. Dead.
* **`ord W = 3`, `m = 2 (mod 3)`.** (3.1) reads `X W^2 X = 1`, i.e. `X^2 = W`; the same
  constant solution, dead for the same reason.
* **`ord W = 3`, `m = 1 (mod 3)`.** (3.1) reads `X W X = W^2`. Taking `W = (123)`, an
  exhaustive check over the twelve elements of `A_4` gives exactly four solutions,
  `X in {(132), (124), (143), (234)}`. The first is `W^2`, the constant solution already
  killed. The other three give the **non-constant** pairs

  ```text
  (X,Y) in { ((124),(234)),  ((143),(124)),  ((234),(143)) } ,     W = XY = (123).
  ```

  In each, `X` and `Y` are distinct `3`-cycles whose supports are two of the three `3`-subsets
  containing the letter fixed by `W`. The available transpositions are those inside `supp X`
  and inside `supp Y`; since `supp X u supp Y = {1,2,3,4}`, they generate `S_4` (e.g.
  `(12),(23),(34)` for the first pair). So these configurations are realisable and survive.

> **THEOREM SK-4 (`g = 2` slice of family 2).** *Let `g = 2` and `(d,n) = (2u, 4)` with `u`
> odd. If `u` is not congruent to `3` modulo `6`, then no `rho_inf`-fixed tuple has image
> `S_4`; the row is dead at every such degree. If `u = 3 (mod 6)`, the surviving outer data is
> exactly one `<Pi>`-orbit of non-constant `3`-cycle pairs as displayed, and in every one of
> them*

```text
(3.3)     Pi = W X   is a double transposition;  in particular  Pi in V_4 .
```

*Proof.* Everything but (3.3) is the case analysis above, plus `u = 2m+1` and
`m = 1 (mod 3) <=> u = 3 (mod 6)`. For (3.3): `m = 1 (mod 3)` and `W^3 = 1` give
`Pi = W^m X = W X`, and the three products `(123)(124) = (13)(24)`, `(123)(143) = (14)(23)`,
`(123)(234) = (12)(34)` are all double transpositions. `[]`

**What SK-4 removes.** Two thirds of the `g = 2` slice die uniformly: `u = 5, 7, 11, 13, 17,
19, ...` — i.e. rows `(10,4), (14,4), (22,4), (26,4), (34,4), (38,4), ...` — all dead at once,
with no row census, no delta-sequence enumeration and no (M-INF) evaluation. The survivors are
`u = 3, 9, 15, 21, ...`, i.e. `d in {6, 18, 30, 42, ...}`; and `d = 6` is separately dead by
the promoted explicit-family ROW-KILL, conditional on the ROW-NF identification. `(10,4)` was
listed at `campaign-pin-gpt55-20260901.md:286-290` as having *no promoted general kill*; SK-4
supplies one.

### 3.3 `g >= 3` in family 2: the exact residual

For `g >= 3` the classification stalls, and the reason is precise rather than a lack of
effort. All three ingredients used above are `g = 2` phenomena:

1. `X, Y in A_4` requires `g` even; for `g` odd both are odd permutations (transpositions or
   `4`-cycles), and (3.1) then has different solution sets. (For `g` odd, `sgn Pi = -1` when
   `u` is odd, so `Pi` is a transposition or a `4`-cycle; `Pi^2 = W^u` with `W` even.)
2. The realisability filters — "`c` a `3`-cycle confines the entries to three letters", "`c` a
   double transposition pins the block entrywise" — are exactly the statements that a product
   of **two** transpositions determines its factors up to order. They are vacuous for `g >= 3`:
   a product of `g >= 3` transpositions with prescribed value can have factors generating all
   of `S_4`.
3. Lemma SK-2 needs the block `(tau, tau)`; for `g >= 3` a block with trivial product is not
   `B_g`-fixed, so `iota . T = T` is a genuine condition and cannot be discharged for free.

Consequently, for `g >= 3`, the outer level yields only (3.1) plus `Pi^2 = W^u`, both of which
are satisfied by the constant tuple (Lemma SK-0). **Typed:
`OPEN[SHAPE-2-INNER-g>=3]` — the family `(gu, 2g)`, `u` odd `>= 3`, `g >= 3`, is not decided
here; the missing ingredient is the inner braid `iota`, numerically pinned by (1.1) to
`e(iota) = (d-1) + 2 delta_aff - n(d-g) = gu - 1 + 2 delta_aff - 2g(gu - g)` but not otherwise
constrained without a `delta_aff` census.**

### 3.4 The NO-TORUS / Shirane mechanism does not travel; what does

The charge asks whether the degree-free half of the `(6,4)` kill (INF-TRIVIAL plus the even
word, plus the `S_3`-resolvent descent) can be completed by a degree-independent
classification input. Typing each half exactly:

**The descent half is degree-free, and at `g = 2` it is automatic.** The composite
`pi_1(A^2 - D) ->> S_4 -> S_3 = S_4/V_4` descends to `pi_1(P^2 - Dbar)` precisely when the
class of the loop at infinity dies, i.e. when `Pi in V_4`. By (3.3) that holds in *every*
surviving `g = 2` configuration of family 2 — so no separate INF-TRIVIAL theorem is needed
there, it is forced by the outer relation. It also forces `sgn Pi = +1`, hence `d` even, hence
(with `u` odd) `g` even: **family 2 has no surviving odd-`g` row that admits the `S_3`
descent.** The remaining odd-`g` rows are not killed — they simply lose the `S_3` route.

**The classification half is degree-6-specific, literally.** The consumed input is Taketo
Shirane, *A note on normal triple covers over `P^2` with branch divisors of degree 6*,
arXiv:1211.2526v1; the promoted TORUS-CHECK gate hashed it and states Corollary 0.6 with the
weighted branch divisor `S_pi + 2 T_pi`
(`pi1s4-64-torus-check-hostile-review-sol56-20260901.md:185-208`). Its hypothesis is
`deg(branch) = 6`. In family 2 the branch is `Dbar` of degree `d = gu`, which equals `6` only
at the promoted `(6,4)` row. There is no degree-`2k` analogue in the promoted set, and none is
expected: the sextic statement is a double-plane/K3 statement, and for `deg B >= 8` the double
plane is of general type with no comparable classification.

**The Tokunaga/Cardano divisibility, typed exactly.** For a normal triple cover
`Z -> P^2` with `pi_* O_Z = O + E^v` (`E` rank two), the branch divisor lies in `|2 det E|`, so
`deg B` is **even** and nothing more. The Cardano normal form `F = -4a^3 - 27 b^2` with
`a in H^0(O(2k))`, `b in H^0(O(3k))` corresponds to the *split Weierstrass* case
`E^v = L^{-1} + L^{-2}`, `L = O(k)`, where `deg B = 6k` and therefore `6 | deg B`. Rank-two
bundles on `P^2` need not split (Horrocks), so the `6 |` conclusion is **not** available in
general. This is a genuine, degree-independent obstruction, but only under a hypothesis that
is not in the promoted set:

```text
OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]:
Does the S_3-resolvent triple cover of P^2 attached to a residual D have split
Tschirnhaus bundle E = O(k) + O(2k)?  If yes, 6 | d, which kills every family-2 and
family-3 row with 6 not dividing d — including the promoted (8,6) types (d = 8).
```

I flag it as the highest-value successor of this lane and explicitly do **not** consume it.

**A degree-free structural fact I can prove, and which sharpens the successor.** Assume the
descent (`Pi in V_4`). Let `W_2 -> P^2` be the double cover of `P^2` branched along `Dbar`
(it exists because `d` is even), and let `Y -> P^2` be the Galois `S_3`-cover. Then
`Y -> W_2` is a cyclic `Z/3`-cover, and it is **unramified over every affine node**. Reason:
at an affine double point the two branch meridians map to *disjoint* transpositions of `S_4`
(`row-sweep-sol56-20260831.md:108-110`), and disjoint transpositions lie in the same coset of
`V_4` — `(12)V_4 = {(12),(34),(1324),(1423)}` — so they have the **same** image in `S_3`. The
local inertia in `S_3` is therefore the single group `<tau_bar>` of order `2`, which meets
`A_3` trivially; hence `Y -> W_2` is étale there, and the corresponding surface point of `W_2`
is an ordinary `A_1` whose local fundamental group `Z/2` admits no `Z/3` quotient. So

```text
(3.4)     the entire Z/3-obstruction of the S_3-resolvent is concentrated at the single
          point of W_2 over the place at infinity.
```

That is degree-free and it is exactly the shape a uniform kill would need: one local
contribution against one global divisor-class condition. Converting (3.4) into a contradiction
requires the Tokunaga divisor-class criterion evaluated at the infinity singularity, which is
outside this lane's desk-scale budget. **Typed `OPEN[SHAPE-2-INFINITY-Z3]`.**

## 4. Family (4,3) scalings (4g, 3g)

Here `d' = 4`, `n' = 3`, `d = 4g`, `n = 3g`, `a = g`. The coprime member `(4,3)` itself is
closed by the promoted coprime Main Theorem (not by Theorem A alone: `(d,n) = (4,3)` passes
`A(2)` and the first fork of `A(3)`, `ord Pi = 3`, `3 | n`, `d` even — the closure comes from
the `B`/`C` half of that theorem). What is at issue is `g >= 2`.

### 4.1 The outer relation at `(4,3)`

`A'(2)` gives a `3`-periodic block-product sequence, so `Pi_4 = Pi_1`; write
`A = Pi_1 = Pi_4`, `B = Pi_2`, `C = Pi_3`. Then `Pi = Pi_1 Pi_2 Pi_3 Pi_4 = A B C A`, and
`r = d' mod n' = 1` makes conjugation by `Pi` the shift by `-1`:

```text
(4.1)     Pi A Pi^{-1} = C ,   Pi C Pi^{-1} = B ,   Pi B Pi^{-1} = A ,
          Pi = A . phi^2(A) . phi(A) . A ,    phi := conj_Pi ,   phi^3 = id on H
```

(the last because `Pi^{n'} = Pi^3 in Z(H)` by `A'(3)`). So the whole outer datum is one
element `A in S_4` together with `Pi`, subject to the single word equation in (4.1).

> **LEMMA 4.2 (dichotomy).** *Either `A = B = C`, or `A, B, C` are pairwise distinct.*
>
> *Proof.* If `A = C` then `phi(A) = A`, so `B = phi^2(A) = A`. If `A = B` then
> `phi^2(A) = A`; applying `phi` and using `phi^3 = id` gives `phi(A) = A`, so `C = A`. If
> `B = C` then `phi^2(A) = phi(A)`, so `phi(A) = A` and again all three agree. `[]`

> **THEOREM SK-5 (uniform, every `g`).** *In the non-constant stratum of family 3, `Pi` is a
> `3`-cycle. Consequently the `S_3`-resolvent `pi_1(A^2-D) ->> S_4 -> S_4/V_4 = S_3` does
> **not** descend to `pi_1(P^2 - Dbar)`, and the projective NO-TORUS / Shirane route is
> structurally unavailable at every `g >= 2`.*
>
> *Proof.* By Lemma 4.2 the three block products are pairwise distinct, and (4.1) makes
> `conj_Pi` cycle them, so `conj_Pi` has order divisible by `3`. `S_4` is centreless, so
> `ord(Pi)` is divisible by `3`; since `ord(Pi) <= 4`, `ord(Pi) = 3`. A `3`-cycle is not in
> `V_4`, so the loop at infinity has nontrivial image in `S_3` and the composite does not
> factor through `pi_1(P^2 - Dbar)`. `[]`

SK-5 is the exact structural reason the campaign never had a Shirane attack on `(8,6)`: unlike
family 2 at `g = 2` — where (3.3) *forces* `Pi in V_4` and the descent is automatic — family 3
forces the opposite. It also means that closing `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` would
not by itself touch family 3's non-constant stratum: there is no triple cover of `P^2` to
apply it to. (It would still bite on the constant stratum, where `Pi = c^4` can lie in `V_4`.)

### 4.3 The `g = 2` slice is settled

`g = 2`, `(d,n) = (8,6)`. Block products are products of two transpositions, so `A,B,C in A_4`,
and `sgn(Pi) = (-1)^8 = +1` puts `Pi in A_4` as well.

*Constant stratum, `A = B = C = c`.* `gcd(n',d') = gcd(3,4) = 1`, so Lemma SK-2 applies to
`c = 1` and forces all four blocks equal, giving `im(phi) = Z/2`. `c` a `3`-cycle confines every
entry to `supp(c)`, giving `im(phi) <= S_3`. `c` a double transposition pins each block to its
two disjoint factors, giving `im(phi) <= V_4`. **The constant stratum is dead.**

*Non-constant stratum.* By SK-5, `Pi` is a `3`-cycle; take `Pi = (123)`. Then `C = phi(A)`,
`B = phi^2(A)`, and the word equation `A phi^2(A) phi(A) A = Pi` is checked over the twelve
elements of `A_4`. The outcome is uniform and striking: `A B C A = A` for **every** `A` except
the three elements of one `phi`-orbit,

```text
A in { (134), (142), (243) } ,   for which  A B C A = Pi = (123) .
```

(The `phi`-fixed `A in {1, (123), (132)}` give the constant stratum, of which only `A = Pi`
is a solution here, already dead above; if `A` is a double transposition then
`{A, phi(A), phi^2(A)} = V_4 - {1}` and the product collapses in the abelian group `V_4` to
`A != Pi`.) For `A = (134)`, `C = phi(A) = (142)`, `B = phi^2(A) = (243)`:

```text
A B C A  :  1 -A-> 3 -C-> 3 -B-> 2 -A-> 2      so 1 -> 2
            2 -A-> 2 -C-> 1 -B-> 1 -A-> 3      so 2 -> 3
            3 -A-> 4 -C-> 2 -B-> 4 -A-> 1      so 3 -> 1
            4 -A-> 1 -C-> 4 -B-> 3 -A-> 4      so 4 -> 4
```

i.e. `ABCA = (123) = Pi`. So the non-constant solutions form a **single `phi`-orbit**,
`{A,B,C} = {(134),(243),(142)}` — the three `3`-cycles whose supports contain the letter fixed
by `Pi`, exactly the same pattern as the family-2 solutions of §3.2. The three supports are
`{1,3,4}, {2,3,4}, {1,2,4}`, whose transpositions exhaust all six transpositions of `S_4`, so
the configuration is realisable with `im(phi) = S_4`. **The `(8,6)` row therefore survives the
whole outer battery**, consistent with its status as one of the six open AM-numerical types
(`campaign-pin-gpt55-20260901.md:200-207`).

### 4.4 General `g`: survives, with the residual typed

For `g >= 3` the two realisability filters of §3.3 are again vacuous, and solutions exist. At
`g = 3` (`(d,n) = (12,9)`) block products are odd, and with `Pi = (123)` both
`A = (12)` (giving `C = (23)`, `B = (13)`) and `A = (14)` (giving `C = (24)`, `B = (34)`)
satisfy `ABCA = Pi`; blocks of three transpositions with a prescribed transposition product are
unconstrained enough to generate `S_4` (e.g. `((12),(34),(34))` and `((13),(23),(13))` both have
product `(12)`). So `(12,9)` survives the outer level too, and the same construction runs at
every `g`.

**Typed: `OPEN[SHAPE-3-ALL-g]`.** Family 3 is *not* killed uniformly. What this lane adds is
(i) the exact outer normal form (4.1); (ii) SK-5, which uniformly removes the `S_3`/Shirane
route and so redirects any future attack; and (iii) the complete `g = 2` split — constant
stratum dead, non-constant stratum a single explicit orbit. The residual mechanism is again the
inner braid, pinned by (1.1) to

```text
(4.2)     e(iota) = (4g - 1) + 2 delta_aff - 3g(4g - g) = 4g - 1 + 2 delta_aff - 9g^2 ,
```

which for `g = 2` is `2 delta_aff - 29` and for `g = 3` is `2 delta_aff - 70`. `iota` lies in a
product of `d' = 4` copies of `B_g`; at `g = 2` that group is `Z^4` and (4.2) is a single
linear condition on four integers, leaving a three-parameter family, and for `g >= 3` the
factors are nonabelian and (4.2) constrains only the total exponent. That is the precise sense
in which the `(4,2)` template does not repeat: there `iota` ranged over `Z^2` with one
condition, i.e. a one-parameter family, which the promoted computation could enumerate.

## 5. Assembly: what closes, what stays OPEN

**Charge item 4 answers NO to the first alternative.** Only family 1 dies uniformly; families
2 and 3 survive, and the exact surviving pairs are typed below. The `d_min` bound of
`OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` is therefore still required — but it is now required over a
strictly smaller cage, and one of its three columns has been deleted rather than bounded.

1. **Family `(u,1)` — KILLED, every degree** (Theorem SK-1). The mechanism proposed in the
   charge is refuted (Lemma SK-0: the constant block-product tuple satisfies `A'(1)-(4)` at
   every noncoprime shape, so the outer level can never kill anything); the working mechanism
   is minimal-gauge degree descent. Corollary SK-2' independently kills the whole `n = 2`
   column at `g = 2`, and Lemma SK-3 kills every `n = 2` row by (M-INF) — three disjoint
   confirmations.
2. **Family `(odd u, 2)`.** Outer fixedness is exactly the deformed braid relation
   `X W^m X = W^{m+1}` (3.1). At `g = 2` this is solved completely: the row is dead unless
   `u = 3 (mod 6)` (Theorem SK-4), which deletes `(10,4), (14,4), (22,4), (26,4), ...` at a
   stroke; the survivors are `d = 6, 18, 30, 42, ...` and `d = 6` is separately dead by the
   promoted explicit-family ROW-KILL. For every `g = 2` survivor `Pi in V_4`, so the
   `S_3`-resolvent descends automatically — the descent half of the `(6,4)` chain is
   degree-free and available. The classification half is not: the consumed input is literally
   a *degree-6* theorem. `OPEN[SHAPE-2-INNER-g>=3]`, `OPEN[SHAPE-2-INFINITY-Z3]`.
3. **Family `(4,3)`, i.e. `(4g, 3g)` — NOT killed.** Outer fixedness is (4.1). Theorem SK-5
   holds at every `g`: outside the constant stratum `Pi` is a `3`-cycle, so the `S_3`-resolvent
   never descends and the NO-TORUS/Shirane route is structurally unavailable — a permanent
   redirection, not a gap. At `g = 2` the constant stratum is dead and the non-constant stratum
   is a single explicit `phi`-orbit; `(8,6)` survives, as the promoted ledger already has it.
   `OPEN[SHAPE-3-ALL-g]`.
4. **Net effect on the campaign-pin residual.** The "unconditional layer" of
   `campaign-pin-gpt55-20260901.md:220-240` shrinks as follows. The `(u,1)` line is **deleted**.
   The `(odd u,2)` line is cut to `u = 3 (mod 6)` at `g = 2` and is untouched for `g >= 3`. The
   `(4,3)` line is untouched. Concretely, of the twenty pairs listed there for
   `d in {10,12,14,15,16}`, **thirteen are deleted by SK-1 and two more — `(10,4)` and
   `(14,4)` — by SK-4**, leaving five:

   ```text
   d=10:  none
   d=12:  (12,8)  [g=4, shape (3,2)] ,  (12,9)  [g=3, shape (4,3)]
   d=14:  none
   d=15:  (15,6)  [g=3, shape (5,2)] ,  (15,10) [g=5, shape (3,2)]
   d=16:  (16,12) [g=4, shape (4,3)]
   d=18:  (18,4)  [g=2, shape (9,2)] ,  (18,12) [g=6, shape (3,2)]
   ```

   and the same two rules applied at every degree. `(18,4)` is the first genuinely new
   `g = 2` survivor beyond `(6,4)`.
5. **Where the remaining effort should go.** Every surviving stratum has the same shape of
   residual: the outer level is satisfiable, so the kill must come from the inner braid `iota`,
   whose exponent sum is pinned by (1.1)/(4.2) but whose individual block exponents are not.
   The `(4,2)` closure worked because `e(iota) = 1` on two parameters. Two concrete successors,
   in priority order: `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` (a positive answer gives `6 | d`
   and kills every family-2 and family-3 row with `6` not dividing `d`, including `(8,6)` — but
   by SK-5 only via the constant stratum in family 3), and `OPEN[SHAPE-2-INFINITY-Z3]`, made
   sharp by (3.4): all affine nodes contribute `A_1` points with local `pi_1 = Z/2` and hence
   no `Z/3`, so the entire `Z/3`-obstruction sits at one point over the place at infinity.

## 6. Typed verdict table

| Family | Scope | Verdict | Instrument |
|---|---|---|---|
| `(u,1)`, all `u >= 2`, all `g >= 2` | every degree | **KILLED** | SK-1 (minimal-gauge descent + Chau re-run) |
| `(u,1)`, `g = 2` | every `u` | **KILLED** (independent) | SK-2' |
| any row with `n = 2` | every `d` | **KILLED** (independent) | SK-3 ((M-INF), `n <= p(a)`) |
| proposed collapse rerun `\|im\| <= 6` at `n'=1` | all `(ug,g)` | **REFUTED** | SK-0; promoted `(6,2)` tuple |
| `(odd u,2)`, `g = 2`, `u != 3 (mod 6)` | `d = 10,14,22,26,...` | **KILLED** | SK-4 |
| `(odd u,2)`, `g = 2`, `u = 3 (mod 6)`, `u >= 9` | `d = 18,30,42,...` | **OPEN** | outer battery satisfied; `Pi in V_4` |
| `(odd u,2)`, `g >= 3` | all | **OPEN** | `OPEN[SHAPE-2-INNER-g>=3]` |
| `(4,3)`, `g = 2`, constant stratum | `(8,6)` | **KILLED** | SK-2 + realisability |
| `(4,3)`, `g = 2`, non-constant | `(8,6)` | **OPEN** | single explicit `phi`-orbit |
| `(4,3)`, `g >= 3` | all | **OPEN** | `OPEN[SHAPE-3-ALL-g]` |
| `S_3`/Shirane route in family 3 | every `g` | **CLOSED NEGATIVE** | SK-5 (`Pi` a `3`-cycle) |
| degree-free classification input for family 2 | — | **NOT FOUND** | Shirane is a degree-6 theorem |
| `6 \| deg B` Cardano divisibility | — | **CONDITIONAL** | needs split Tschirnhaus bundle; typed OPEN |

Nothing above is promoted; this is a producer report and every item is subject to hostile
review. The two items I would most want a reviewer to attack are SK-1's attainment step (the
minimum over `Aut(A^2)` is over projective degrees of images, and the elementary move must be
checked not to degenerate — §2.3 handles the constant case via birationality) and SK-4's
exhaustive `A_4` check.

## 7. Sources and hashes

Primary literature: none newly fetched. The Galindo--Monserrat and Shirane hashes used are the
ones already recorded in the frozen inputs and in the promoted TORUS-CHECK gate, namely
`637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9`
(arXiv:0910.2613v2, *The Abhyankar--Moh Theorem for plane valuations at infinity*,
`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:20-26`) and Taketo Shirane,
*A note on normal triple covers over `P^2` with branch divisors of degree 6*,
arXiv:1211.2526v1 (`pi1s4-64-torus-check-hostile-review-sol56-20260901.md:185`). Chau 1999,
*Non-zero constant Jacobian polynomial maps of `C^2`*, is consumed only through the promoted
trichotomy at `d1-degree-bound-sol56-20260831.md:208-248`. Miranda's triple-cover structure and
Horrocks' splitting criterion are cited in §3.4 as standard, and are the reason
`OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` is typed OPEN rather than consumed.

Campaign artifacts read (not edited): `campaign-pin-gpt55-20260901.md`,
`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md`,
`row-nf-exhaustiveness-hostile-review-sol56-20260901.md` (the three charged inputs, hashed in
§0), plus `pi1-s4-decision-opus5-20260831.md`, `pi1s4-close-residual-r2-opus5-20260831.md`,
`pi1s4-close-residual-hostile-review-sol56-20260831.md`, `row-sweep-sol56-20260831.md`,
`d1-degree-bound-sol56-20260831.md`, `pi1s4-64-torus-check-hostile-review-sol56-20260901.md`.


<!-- BODY-END -->
