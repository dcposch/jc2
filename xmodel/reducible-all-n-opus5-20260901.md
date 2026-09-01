# REDUCIBLE-ALL-N: the general-degree reducible cage

Lane: OPEN[B0-REDUCIBLE-N>=6/GENERAL-N] · 2026-09-01 · Opus 5
Desk-scale exact reasoning only; no CAS.

## 0. Input verification, custody, typing

Verification was the first action. The three charged inputs hash as declared:

```text
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
bd6443b34e95213b0b2950e45c896417c492487c38a0a721eae4977d1e73f5d6  b0-reducible-n5-hostile-review-sol56-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Below **N5**, **REV**, **C6** denote them in that order. Four primary sources were
opened and hashed here; the first three reproduce the custody values in N5 SS0 and
REV SS1, the fourth reproduces REV SS1's streamed value:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf                (Orevkov 1987)
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_...math0305088.pdf
644552cf8d543868f44d6fdf40420c2885e6d0e4255e18c03fe0af8980d34fdd  https://arxiv.org/pdf/1405.5391  (Palka, streamed)
```

Palka's **Theorem A** (printed p. 1) is the homogeneous Lin-Zaidenberg /
Abhyankar-Moh-Suzuki statement: *a topologically contractible algebraic curve in
`C^2` has equation `x^n = y^m` in some algebraic coordinates, `n > m > 0`
coprime*; **Theorem B** is the `m = 1` (smooth) case. This retires REV's
"no primary custody for AMS" caveat and supplies the *singular* half as well,
which is what this lane needs. Chau **Theorem 1** and **Corollaries 1-2**
(printed pp. 1-2) are consumed as stated there.

No CAS was run. A short integer-bookkeeping script (multiset enumeration of
`(mu,s,k)` profiles and set partitions) was used to *cross-check* the SS9 tables;
every kill in SS2-SS6 is proved by hand and the script only applies them. It is
disclosed as a checking device, not as evidence. No canonical ledger, no charged
file, and no part of `jc2-lean` was touched.

**Typing.** `[P]` promoted (C6 SS1, or REV SS7's promote list); `[D]` derived here;
`[L]` primary literature consumed here; `[O]` typed OPEN; `[A]` audit against a
consumed item. Nothing below is an attainment claim: every configuration is a
*necessary* cage, never a witness.

**Scope (RED-N).** `F` a noninvertible plane Keller map of geometric degree `N`;
`A_F = D_1 u ... u D_m` with `m >= 2`; at least one affine-image dicritical has
`mu = 1`. Theorem 7.B `[P]` (C6 SS1.1) closes the complementary irreducible case at
every degree, so RED-N is exactly the surviving front.

## 1. Uniform objects: the budget is one identity

Notation as in N5 SS1.1: dicritical `l`, source `l' ~ A^1`, target `D_{tau(l)}`,
`phi_l = eta_i o h_l`, `s_l = deg h_l`, `mu_l`, `corr_l`, `M_t = mu_{pi(t)}f^*`,
`k_t = M_t - e_t mu_l >= 0`, `K_l = sum_t k_t`, `W_i = sum_{l->i} s_l mu_l`,
`a_i = N - W_i >= 1`. Promoted and reviewed inputs used verbatim: the Orevkov
budget `sum_l (mu_l + corr_l) = N - 1` (Lemma 4.2 of `jc86.pdf`, printed p. 8);
the pointwise jump law (Zoladek Prop. 6.5(b)); **Lemma A** (every component is a
polynomial curve: `D~_i ~ A^1`, one place at infinity, `sum_t (e_t - 1) = s_l - 1`)
and **Lemma B** (`corr_l = mu_l(s_l - 1) + K_l`), both promoted by REV SS7 at
their stated scopes and both degree-free.

Write the **cost** of a dicritical as `c_l := mu_l + corr_l`. Lemma B gives at once

```text
(COST)   c_l = mu_l s_l + K_l ,
```

so the Orevkov budget *is* the aggregate identity:

```text
(BUD)    sum_i W_i + K_tot = N - 1 ,     K_tot = sum_l K_l .
```

N5 SS1.4 proved "(AGG) carries no information beyond the budget" by an Euler
computation at `N = 5`; (COST) shows it is a one-line algebraic identity at every
degree, so the Euler route need never be run again. `[D]`

Summing Orevkov's constant-multiplicity relation at an arbitrary `q in C^2`, with
`r_{i,q}` the number of branches of `D_i` at `q`:

```text
(LOC)    a_q + sum_t M_t = a_q + sum_i r_{i,q} W_i + K_q = N ,
```

the middle expression being the sum over the points `t` at infinity lying over `q`
(`sum_{t -> z} e_t = s_l` for every place `z`, so each place of `D_i` over `q`
contributes `W_i` plus its `k`'s). This is N5's (LOC), re-derived here at general
`N` and used constantly below. `[D]`

Cycle types: over a small transversal at a generic point of `D_i` the `N` sheets
are `a_i` affine preimages (fixed, `F` etale) and, for each `l -> i` and each of
the `s_l` points of the fibre, one `mu_l`-cycle (Orevkov Lemma 3.1 normal form).
So the meridian `gamma_i` has cycle type `1^{a_i} prod_{l->i} mu_l^{s_l}`, and its
**index** (`N` minus its number of cycles) is

```text
(IND)    iota_i = sum_{l -> i} s_l (mu_l - 1) ,     sum_i iota_i = N - 1 - K_tot - sum_l s_l .
```

Call `D_i` *branched* iff `iota_i >= 1`, i.e. iff some `mu_l >= 2`; let `b` be the
number of branched components and `D_br` their union. Meridians of unbranched
components die, so `rho : pi_1(C^2 - A_F) -> S_N` factors through
`pi_1(C^2 - D_br)`, and `rho` is transitive because `C^2 - F^{-1}(A_F)` is the
complement of a curve, hence connected. `[D]`

## 2. Uniform structure bounds (b, m, s, a_i)

Every component owns at least one dicritical, so `W_i >= 1`; a branched one has
`W_i >= 2`; and RED-N forces at least one trivial dicritical (cost 1). Feeding
this into (BUD):

> **Proposition RC `[D]`.** In scope RED-N, for every `i` and every `l`,
> ```text
> (RC1)  W_i <= N - m - K_tot ,   hence   a_i >= m + K_tot >= 2 ;
> (RC2)  1 <= b <= floor((N-2)/2) ;
> (RC3)  m <= N - 2 - K_tot ;
> (RC4)  s_l <= (N - m)/2 <= floor((N-2)/2) .
> ```

*Proof.* (RC1): the other `m-1` components contribute `>= 1` each to (BUD).
(RC2): if some component is unbranched, `sum_i W_i >= 2b + (m - b) = m + b` and
`m >= b+1`, so `2b <= N-1-K_tot-1`; if all `m = b` components are branched the
trivial dicritical sits on one of them, raising its `W` to `>= 3`, so
`sum_i W_i >= 2b+1`. Both give `2b <= N-2-K_tot`. (RC3): from `2b + u <= N-1-K_tot`
with `b >= 1`. (RC4): a carrier with `s_l >= 2` has `mu_l >= 2` (a `mu = 1`
carrier has `corr = 0`, hence `s = 1`), so `c_l = mu_l s_l + K_l >= 2 s_l`, and
the other `m-1` components cost `>= 1` each. []

(RC2) is the sharp break with the closed degrees. At `N = 4, 5` it forces `b = 1`
— N5 SS2.3's "the branch locus is irreducible" — but at `N = 6` it permits `b = 2`,
and the two-branched-component row `(2,0)|(2,0)+(1,0)` meets every constraint.
**Finding `[D]`: the branch locus of the covering first becomes reducible at
`N = 6`; N5's single most useful structural fact is a low-degree accident.**

(RC1) is new and is used throughout: *every* meridian fixes at least `m >= 2`
letters, so no meridian is an `N`-cycle and no `gamma_i` is fixed-point-free.

(RC4) reproduces N5 SS2.2 (`s_l = 1` at `N <= 5`) and gives the numerically first
ramified degree as `N = 6`, confirming REV SS5 against N5's "`N = 7`". SS5 below
raises the true threshold to `N = 10`.

## 3. No component is a line; the two embedding gates

> **Lemma NL `[D]`+`[L]`.** No irreducible component of `A_F` is a line.

*Proof.* First, after a **linear target change** we may assume
`deg P != deg Q`; a linear change carries lines to lines, so the conclusion is
unaffected. Indeed suppose `deg P = deg Q = K`. `K = 1` makes `F` affine, hence
invertible; so `K >= 2` and the degree-`(2K-2)` part of `J(P,Q)`, namely
`J(P_K, Q_K)` in the top forms, must vanish because `J(P,Q)` is a nonzero
constant and `2K - 2 > 0`. For forms of equal degree `K` in two variables Euler's
identity gives `x J(P_K,Q_K) = K (P_K (Q_K)_y - (P_K)_y Q_K)`, so `J = 0` forces
`(P_K/Q_K)_y = 0`; being homogeneous of degree `0`, `P_K/Q_K` is then a constant
`c`, and `P - cQ` has degree `< K`.

Now apply Chau **Theorem 1** `[L]` to `(P,Q)` (its monic normalisation is a
*source* linear change, which does not move `A_F`): with
`K' = gcd(deg P, deg Q)`, `d = deg P/K'`, `e = deg Q/K'`, `gcd(d,e) = 1`, every
component of `A_F` is parametrised by
`xi -> (A xi^{md} + ..., B xi^{me} + ...)`, `m >= 1`. If the parametrisation is
`kappa`-to-one onto its image then `kappa | gcd(md,me) = m`, so the component has
degree `(m/kappa) max(d,e)`, a positive multiple of `max(d,e)`. Since
`deg P != deg Q` and `gcd(d,e) = 1` we have `d != e`, so `max(d,e) >= 2`. Hence
every component has degree `>= 2`. []

Two immediate consequences, both uniform in `N`:

> **Gate EMB `[D]`.** No component of `A_F` is a smoothly embedded `A^1`.
> (Palka Theorem B rectifies such a curve to a line by some `T in Aut(C^2)`;
> `T o F` is Keller, noninvertible, of the same geometric degree and with the same
> profile, and `A_{ToF} = T(A_F)` would have a line component.)

> **Gate SELF `[D]`.** If `corr_l = 0` for every `l -> i` — in particular for every
> unbranched component — then `eta_i` is immersive, so `D_i` cannot also be
> injective; it has a point with `r_{i,p} >= 2`, and (LOC) gives `2 W_i <= N`.

Gate SELF supersedes N5's Gate AMS: at `N = 5` it kills P2 (`W = 3`) and P3c
(`W = 3`) without the transitivity step, and it applies to *unbranched*
components, which Gate AMS could not reach.

Chau's Corollary 2 `[L]` adds the standing global picture used in SS7-SS9: `A_F` has
**one point at infinity**, every component passing through it with a single place
of Newton-Puiseux type `u = c v^{d/e}`. So the cage is a bouquet of polynomial
curves of degrees all divisible by `max(d,e) >= 2`, pairwise tangent at one common
point of `L_inf`.

## 4. Clusters, local transitivity, and the Lin-Zaidenberg kill

Fix `p in A_F` and let `G_p = rho(pi_1(B_p - A_F))` be the local monodromy group.
The `N` letters over `p` are the sheets of `F` over a nearby generic point.

> **Lemma D (clusters) `[D]`.** The letters over `p` partition into `a_p` singletons
> (the affine preimages, fixed by `G_p`) and one **cluster** of size `M_t` for each
> point `t` at infinity over `p`. Each block is `G_p`-invariant, and `G_p` acts
> **transitively on each cluster**.

*Proof.* The blocks are the connected components of `F^{-1}(B_p - A_F)`, which are
the `G_p`-orbits. Each such component lies in a unique connected component of
`(f^*)^{-1}(B_p)` in `X~^*`, i.e. in a unique affine preimage or a unique `t`;
this gives invariance, and (LOC) gives the sizes. Conversely, a neighbourhood of
`t` minus the curve `f^{-1}(A_F)` is a ball minus a curve, hence connected, so the
cluster of `t` is a single orbit. []

Lemma D replaces the case-by-case node analysis of the closed degrees. In
particular the local meridians of *distinct* branches at `p` have supports in
*distinct* clusters, so they are **disjoint permutations** — the "disjoint
transpositions at a node" law of the `N = 4`/`N = 5` lanes, now automatic and
degree-free.

> **Gate TRANS-LOC `[D]`.** In scope RED-N no local monodromy group `G_p` is
> transitive on the `N` letters.

*Proof.* Transitivity forces a single block: `a_p = 0` and one cluster with
`M_t = N`. But a single `t` over `p` means a single place `z`, hence one component
`D_i` through `p` with `r_{i,p} = 1` and one dicritical on it, so
`M_t = s_l mu_l + k_t <= W_i + K_i <= N - 1 - (m-1) <= N - 2`. []

> **Gate LZ-KILL `[D]`+`[L]`.** If `b = 1` and `2 W_br > N`, the profile is dead.

*Proof.* `2W_br > N` and (LOC) give `r_{br,p} <= N/W_br < 2`, so `eta_br` is
injective; being a finite bijective morphism from `A^1` (Lemma A) it is a
homeomorphism, so `D_br` is topologically contractible. Palka **Theorem A** `[L]`
supplies `T in Aut(C^2)` with `T(D_br) = {x^n = y^m}`, `n > m > 0` coprime;
replace `F` by `T o F` (same `N`, same profile, `A_F` moved by `T`). `m = 1` is a
line, excluded by Lemma NL, so `m >= 2`. The curve `x^n = y^m` is
weighted-homogeneous for the weights `(m,n)`, so the weighted-radial flow retracts
`C^2 - D_br` onto the link complement of its unique singular point `p_0 = 0`; hence
`pi_1(B_{p_0} - D_br) -> pi_1(C^2 - D_br)` is onto. Since `b = 1`, `rho` factors
through `pi_1(C^2 - D_br)`, so `G_{p_0} = rho(pi_1(C^2 - A_F))` is transitive —
contradicting Gate TRANS-LOC. []

Gate LZ-KILL strictly contains N5's Gate AMS: it drops the hypothesis `corr = 0`
on `D_br` and needs no cyclic-image argument. At `N = 5` it kills P2 and P3c; at
`N >= 6` it kills every "starved" branched row, and it is the only gate in this
report that consumes the *singular* half of Lin-Zaidenberg.

## 5. The local analytic gate at mu = 2: cusp dictionary and NO-RAM-2

Everything so far is topological or numerical. The following is a local analytic
computation at a jump point, and it is the sharpest new tool in this lane.

Fix `t in l'` with `phi_l(t) = p`. Choose coordinates `(x,y)` at `t` with
`l = {y = 0}` and `p = 0` in the target; write `u = sum_j y^j u_j(x)`,
`v = sum_j y^j v_j(x)`, so `(u_0, v_0) = phi_l` near `t`. Because `F` is etale off
`l` and the critical divisor of the germ is exactly `(mu_l - 1) l`, we have
`J = y^{mu_l - 1} h` with `h` a unit (a zero of `h` would force a curve of zeros
of `J` off `l`). Put `alpha = ord u_0`, `beta = ord v_0`; a *linear target change*
(allowed, and harmless for `J`, `mu`, `M_t`) makes `alpha != beta`, and we may
assume `alpha < beta`.

> **Lemma CUSP-2 `[D]`.** Let `mu_l = 2` and suppose the branch of `A_F` at
> `phi_l(t)` is singular. Then `beta = alpha + 1`, `u_1(0) != 0`, and
> ```text
> M_t = alpha + 1 ,        k_t = M_t - e_t mu_l  with  e_t = 1 .
> ```
> Consequently `e_t = 1`, the image branch has multiplicity `nu = alpha`, its
> unique Puiseux characteristic pair is `(nu, nu+1)`, and `k_t = nu - 1`.

*Proof.* `J = y h`, so `[y^0]J = u_0' v_1 - u_1 v_0' = 0` and `[y^1]J` must be a
unit, where
`[y^1]J = 2u_0'v_2 - 2u_2v_0' + (u_1'v_1 - u_1v_1')`. Singularity of the branch
means `alpha >= 2`, so `ord(2u_0'v_2) >= alpha - 1 >= 1` and
`ord(2u_2v_0') >= beta - 1 >= 1`: neither can be a unit. If `u_1 = 0` then
`v_1 = 0` and `[y^1]J` is not a unit. So `u_1 != 0` and
`v_1/u_1 = v_0'/u_0' = x^{beta-alpha} w` with `w` a unit; then
`u_1'v_1 - u_1v_1' = -u_1^2 (v_1/u_1)' = -u_1^2 x^{beta-alpha-1} w~`, `w~` a unit,
of order `2 ord(u_1) + beta - alpha - 1`. It is a unit iff `ord(u_1) = 0` and
`beta = alpha + 1`. For `M_t`: write `u_0 = A x^alpha(1+..)`, `u_1 = a(1+..)`,
`v_0 = B x^{alpha+1}(1+..)`; then `v_1 = aB(alpha+1)/(A alpha) x(1+..)`, solving
`u = 0` gives `y = -(A/a)x^alpha(1+..)`, and substituting,
`v = B x^{alpha+1}(1 - (alpha+1)/alpha) + O(x^{2 alpha}) = -(B/alpha)x^{alpha+1}+...`,
so `M_t = dim O/(u,v) = alpha + 1`. Finally `ord phi_l = e_t . nu` in *both*
coordinates, so `e_t | (beta - alpha) = 1`, whence `e_t = 1` and `alpha = nu`. The
Puiseux expansion `v = c u^{(nu+1)/nu} + ...` has `gcd(nu, nu+1) = 1`, so
`(nu, nu+1)` is the only characteristic pair. []

> **Theorem NO-RAM-2 `[D]`.** Every dicritical with `mu_l = 2` has `s_l = 1`.

*Proof.* If `s_l >= 2`, Lemma A gives a `t` with `e_t >= 2`; then
`M_t >= e_t mu_l > mu_l`, so the branch at `phi_l(t)` is singular (Orevkov
Lemma 5.2), and Lemma CUSP-2 forces `e_t = 1`. Contradiction. []

Two corollaries `[D]`. (i) **Cusp dictionary.** For a `mu = 2` carrier,
`corr_l = K_l = sum (nu - 1)` over the singular branches it produces, each an
ordinary `(nu, nu+1)` cusp. So a `(2,1,k)` carrier produces cusps of types
`(nu_1,nu_1+1), ...` with `sum (nu_j - 1) = k`, and **nothing else**: germs
`(2,5)`, `(2,7)`, `(2,9)`, `(3,5)` are all excluded. This *sharpens* N5 SS6, which
admitted `(2,9)` on the Fox-determinant criterion; `[A]` **AUDIT-1**: N5's
"`(2,9)` is admissible" is refuted — the Fox test is necessary, not sufficient,
and the local Jacobian order is the sharper gate. The `N = 5` survivor S1 is
therefore pinned to **exactly one ordinary cusp** `(2,3)` with `M_{t_0} = 3`.
(ii) **Threshold.** Combining NO-RAM-2 with (RC4) and Gate LZ-KILL: a ramified
carrier needs `mu >= 3`, `s >= 2`, so `W >= 6`; with `b = 1` Gate LZ-KILL demands
`2W <= N`, i.e. `N >= 12`, and with `b >= 2` the budget needs
`N - 1 >= 6 + 2 + 1`. Hence **no ramified carrier survives below `N = 10`**, and
`N = 10` is attained numerically by `(3,2,0) | (2,1,0) | (1,1,0)`,
`W = (6,2,1)`. This corrects N5 (`N = 7`) and REV (`N = 6`) upward. `[A]` **AUDIT-2**.

## 6. Degree at general N: transversal identity, per-component floor, NO-DEG-CAP

> **Gate TG-N `[D]`.** For a generic target line `L`, let `g` be the genus of the
> smooth model of `F^{-1}(L)` and `Sigma_inf >= 1` its number of places over
> `L n L_inf`. With `d_i = deg D_i`,
> ```text
> (TG-N)   sum_i d_i . iota_i  =  N - 2 + 2g + Sigma_inf  >=  N - 1 .
> ```

This is N5's Gate TG with the ad-hoc factor `s_l(mu_l - 1)` recognised as the
permutation index `iota_i` of (IND); the proof is unchanged (Euler characteristic
of the `N`-sheeted cover `F^{-1}(L \ A_F) -> L \ A_F`, one branch of `F^{-1}(L)`
over each point of each dicritical fibre, plus `Sigma_inf` at infinity), and it
is exactly Riemann-Hurwitz for `F^{-1}(L) -> L`. `F^{-1}(L)` is smooth because the
gradients of `P` and `Q` are everywhere independent, and connected because
`rho` is transitive and `pi_1(L \ A_F) ->> pi_1(C^2 - A_F)` for generic `L`
(Zariski; `[O]` custody, see SS10).

The floor is equivalent to the group-theoretic connectivity bound: a transitive
group generated by `sum_i d_i` conjugates of the `gamma_i` needs
`sum_i d_i iota_i >= N - 1`. Sharper:

> **Lemma DEG-PER `[D]`.** If the image `G` is primitive — in particular whenever
> some meridian is a transposition, which forces `G = S_N` — then for **each**
> branched component separately, `d_i . iota_i >= N - 1`.

*Proof.* The set of `D_i`-meridian images is closed under `G`-conjugation, so the
subgroup `H_i` it generates is normal in `G`; `H_i != 1`, and a nontrivial normal
subgroup of a primitive group is transitive. Apply the connectivity bound to the
`d_i` generators of `H_i`. []

So in the "spine" rows (`iota_br = 1`, a transposition meridian) every branched
component has `d_i >= N - 1`, and (TG-N) then forces
`2g + Sigma_inf >= (b-1)(N-1) + 1`.

> **Theorem NO-DEG-CAP `[D]`.** `deg A_F` admits **no** bound in terms of `N`.

*Proof.* For `T in Aut(C^2)`, `T o F` is Keller, noninvertible, of geometric
degree `N`, with the same dicritical profile `(mu_l, corr_l, s_l)` and the same
ownership, and `A_{ToF} = T(A_F)`. Taking `T(x,y) = (x, y + x^k)` multiplies
component degrees without bound. []

This **refutes N5's DQ-3** (`OPEN[N5-DEGREE-CAP]`, flagged there as the highest-
leverage question): no Jelonek-type bound `deg A_F <= N-1` can exist, at `N = 5`
or anywhere. `[A]` **AUDIT-3.** The consequences are structural, not cosmetic:

- degree, arithmetic genus and delta-budget statements are *gauge-dependent* and
  therefore vacuous as gates; only `d_min = min_T deg T(D)` statements survive,
  which is precisely the promoted D1-DEGREE discipline (C6 SS1.3);
- (TG-N) and Lemma DEG-PER hold in *every* gauge, hence give
  `d_min(D_i) . iota_i >= N - 1` — a floor that **grows linearly in `N`**, and
  which is the reducible-lane counterpart of `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`;
- since degrees, genera and singularity counts are all unbounded, **no gate whose
  inputs are the profile together with degree/genus/delta data can close RED-N.**
  The numeric layer is exhausted by (BUD), (LOC), (TG-N) and the local gate of
  SS5. Every remaining kill must consume `pi_1(C^2 - D_br)` itself. That is the
  exact obstruction to uniformity the charge asks for.

## 7. S_N representation constraints and the resolvent question

Standing facts, all uniform in `N` `[D]`: `rho` is transitive; `rho` factors
through `pi_1(C^2 - D_br)`; each `gamma_i` has cycle type
`1^{a_i} prod mu_l^{s_l}` with `a_i >= m >= 2` by (RC1); the local groups obey
Lemma D and Gate TRANS-LOC.

**(S1) The image is never abelian.** A transitive abelian subgroup of `S_N` is
regular, so each of its nonidentity elements is fixed-point-free; but every
`gamma_i` fixes `a_i >= 2` letters, so all `gamma_i = 1` and `G = 1`, forcing
`N = 1`. Hence `pi_1(C^2 - D_br)` is nonabelian, and every "abelianising"
criterion is a kill: Gate SELF/Gate EMB (line, `pi_1 = Z`), Gate LZ-KILL, and
Corollary N-A-RES `[P]` in the reviewed scalar gauge `M_inf + 2T <= 3d - 3`
(REV SS6; the theorem-level form is `C'^2 > 2r_1 + 4T`, and `OPEN[NORI-BC-
SELF-TANGENT-COEFF]` bars improving `4T` to `2T` at theorem level only).

**(S2) The group is pinned.** If any branched component has a transposition
meridian — `iota_i = 1` with a single `(mu,s) = (2,1)` carrier, the type
`(2, 1^{N-2})` of the charge — then `G` is transitive and generated by
transpositions, hence `G = S_N`. If all meridians are `3`-cycles, `G = A_N`.

**(S3) The resolvent trick is provably unavailable for every `N >= 5`, and there
is no uniform substitute of the same kind.** For `N = 4` the campaign used
`V_4 <| S_4` with `S_4/V_4 = S_3` to descend a transposition-meridian cover to an
explicitly computable triple cover (Tschirnhaus/Cardano, Shirane's torus-type
route). For `N >= 5` the only proper quotients of `S_N` are `1` and
`S_N/A_N = Z/2`, and the `Z/2` quotient carries no information here: `sgn o rho`
is determined on `H_1(C^2 - A_F) = Z^m` (free on the meridians), so it exists for
every profile, and its one global relation — the product of the `d` generic-line
meridians equals the monodromy at infinity — reduces to (TG-N) mod 2, namely
`sum_i d_i iota_i = N - Sigma_inf (mod 2)`. So the descent trick is **not
replaced**; it is *provably absent*, and `N = 4` is the unique exceptional degree.
`[D]`

What does carry uniformly is a *sub*-object rather than a quotient: the local
monodromy at singular points. Lemma D says the local group of each branch acts
transitively on its own cluster and the branches at a point are supported on
disjoint clusters; Gate TRANS-LOC says the local group is never globally
transitive; Lemma CUSP-2 pins the germ produced by every `mu = 2` correction to
`(nu, nu+1)`. Concretely, at a `(nu, nu+1)` cusp of a transposition-meridian
component the cluster has size `M = nu + 1` and the local group is transitive on
it and generated by transpositions, so it equals `S_{nu+1}`; the germ's knot group
`<a,b | a^{nu} = b^{nu+1}>` must therefore surject onto `S_{nu+1}` with meridian a
transposition. **That condition is always satisfiable**: take `B` the
`(nu+1)`-cycle `(1 2 ... nu+1)` and `A = B.(12)`, a `nu`-cycle fixing one letter;
`B^{-1}A = (12)`, and Jordan's theorem plus the odd element give
`<A,B> = S_{nu+1}`. So the cusp sites impose **no** local obstruction at any `nu`
— a load-bearing negative that tells the campaign where not to spend effort, and
one that N5 SS6 could not see because its Fox test only ran at `nu = 2`. `[D]`

## 8. THEOREM CAGE-N and the survivor shape

> **THEOREM CAGE-N `[D]` (the general-degree reducible cage, at its true scope).**
> Let `F` be a noninvertible plane Keller map of geometric degree `N >= 4` in scope
> RED-N. Then:
>
> 1. **Curves.** Every component `D_i` is a polynomial curve (`D~_i ~ A^1`, one
>    place at infinity); all components meet `L_inf` in one common point with one
>    place each, of a common Newton-Puiseux type `u = c v^{d/e}`; all component
>    degrees are positive multiples of `max(d,e) >= 2`; **no component is a line
>    or a smoothly embedded `A^1`**.
> 2. **Budget.** `sum_i W_i + K_tot = N - 1` with `c_l = mu_l s_l + K_l`;
>    `a_i >= m + K_tot >= 2`; `1 <= b <= floor((N-2)/2)`; `m <= N - 2 - K_tot`;
>    `s_l <= floor((N-2)/2)`.
> 3. **Local.** `a_p + sum_i r_{i,p} W_i + K_p = N`; the letters over `p` split
>    into `a_p` fixed singletons plus clusters, each `G_p`-invariant with `G_p`
>    transitive on it; distinct branches at `p` carry disjoint meridians; no `G_p`
>    is transitive on all `N` letters.
> 4. **Kills.** `2 W_i <= N` whenever `corr = 0` on `D_i` (Gate SELF); `2 W_br <= N`
>    when `b = 1` (Gate LZ-KILL); `s_l = 1` whenever `mu_l = 2` (NO-RAM-2), so no
>    ramified carrier exists below `N = 10`.
> 5. **Corrections.** Every correction of a `mu = 2` carrier is an ordinary
>    `(nu, nu+1)` cusp of the image with `k = nu - 1`; no other germ occurs.
> 6. **Monodromy.** `rho : pi_1(C^2 - D_br) ->> G <= S_N` is transitive with
>    nonabelian image; `gamma_i` has cycle type `1^{a_i} prod_{l->i} mu_l^{s_l}`;
>    a transposition meridian forces `G = S_N`.
> 7. **Degree.** `sum_i d_i iota_i = N - 2 + 2g + Sigma_inf`, and if `G` is
>    primitive then `d_min(D_i) . iota_i >= N - 1` for each branched `i`; no upper
>    bound on `deg A_F` in terms of `N` exists.

**Survivor shape (conjectured in the charge, proved here).** Write `Gamma` for the
total cost of the *nontrivial* dicriticals (`mu >= 2`) and `T = N - 1 - Gamma >= 1`
for the number of trivial ones. Then a profile survives 1-6 iff it consists of

- a **core**: a multiset of `c >= 1` nontrivial dicriticals `(mu_j, s_j, k_j)` of
  total cost `Gamma <= N - 2`, partitioned into `b <= c` branched components; plus
- `T` trivial dicriticals distributed over the branched components and over
  `u >= max(0, 2-b)` new unbranched components;

subject only to `2W_i <= N` on every correction-free component, `2W_br <= N` when
`b = 1`, and `s_j = 1` whenever `mu_j = 2`. **The monodromy problem depends only
on the core**: trivial dicriticals contribute `1`-cycles, unbranched components
have trivial meridians and are invisible to `rho`; they only consume budget,
tighten (LOC), and add curves to `A_F`. Since `c <= floor((N-2)/2)` and the cost
of a minimal nontrivial carrier is `2`, the number of cores grows with `N` roughly
like the number of partitions of `N-2` into parts `>= 2`. **There is therefore no
uniform finite survivor list**, and by NO-DEG-CAP no numeric gate can produce one:
the residual is a growing but explicitly enumerable family of `PI1-S_N` questions.
`[D]`

At the two closed degrees the shape specialises correctly, which is the control on
the whole machine: `N = 4` gives exactly one row (core `(2,1,0)`, `W = (1,2)`) —
the promoted `N = 4` residual; `N = 5` gives exactly the two promoted survivors,
S2 (core `(2,1,0)`, `W = (1,1,2)` or `(2,2)`) and S1 (core `(2,1,1)`, `W = (1,2)`),
with P2 and P3c killed by Gate SELF/LZ-KILL. No row of the closed degrees is lost
and none is added.

## 9. Residual list through N = 8, typed PI1-style

Notation: a class is written `[lambda_1^{(k_1)} + ... + lambda_b^{(k_b)}]`, one
entry per branched component, `lambda_i` its meridian's moved cycle type and
`k_i` its correction weight (omitted when `0`); `#` is the number of trivial
placements (= profiles) in the class. All entries have `s = 1` (SS5). Every class
is the decision question `PI1-S_N(class)` below.

```text
N=6  (14 profiles, 6 classes)          N=7  (31 profiles, 10 classes)
  [2]        b=1 iota=1  # 4             [2]        b=1 iota=1  # 6
  [2^(1)]    b=1 iota=1  # 3             [2^(1)]    b=1 iota=1  # 4
  [2^(2)]    b=1 iota=1  # 1             [2^(2)]    b=1 iota=1  # 3
  [3]        b=1 iota=2  # 2             [2^(3)]    b=1 iota=1  # 1
  [3^(1)]    b=1 iota=2  # 1             [3]        b=1 iota=2  # 3
  [2 + 2]    b=2 iota=2  # 2             [3^(1)]    b=1 iota=2  # 2
                                         [3^(2)]    b=1 iota=2  # 1
                                         [2 + 2]    b=2 iota=2  # 4
                                         [2 + 2^(1)] b=2 iota=2 # 2
                                         [2 + 3]    b=2 iota=3  # 2

N=8  (104 profiles, 26 classes)
  b=1 : [2] #10, [2^(1)] #8, [2^(2)] #5, [2^(3)] #3, [2^(4)] #1,
        [22] #3, [22^(1)] #2, [22^(2)] #1,
        [3] #7, [3^(1)] #5, [3^(2)] #3, [3^(3)] #1,
        [4] #3, [4^(1)] #2, [4^(2)] #1
  b=2 : [2+2] #7, [2+2^(1)] #5, [2+2^(2)] #2, [2^(1)+2^(1)] #2,
        [2+22] #2, [2+3] #5, [2+3^(1)] #3, [2^(1)+3] #3,
        [3+3] #2, [2+4] #2
  b=3 : [2+2+2] #2
```

> **`OPEN[PI1-S_N-CAGE(class)]`** (one per class above). Let
> `D = D_1 u ... u D_b` in `C^2` with each `D_i` an irreducible polynomial curve
> (normalisation `A^1`, one place at infinity), all `D_i` through one common point
> of `L_inf`, no `D_i` a line, `D_i` having exactly the cusps prescribed by `k_i`
> (each an ordinary `(nu,nu+1)` germ with `sum (nu-1) = k_i`) and otherwise only
> multibranch points. Does there exist a transitive
> `rho : pi_1(C^2 - D) -> S_N` with `gamma_i` of moved type `lambda_i` and
> `1^{a_i}` fixed, obeying Lemma D at every point of `D` and
> `sum_i d_i iota_i = N - 2 + Sigma_inf + 2g`? A negative answer kills the class.

Structural remarks, all `[D]`, that a decision lane should consume first:

- **The `[2...]` classes are the spine.** `G = S_N`, all meridians transpositions,
  `d_min(D_i) >= N - 1` for every branched `i` (Lemma DEG-PER). The `b = 1`,
  `k = 0` class `[2]` is the exact `PI1-S_N`-nodal analogue of the promoted
  `OPEN[PI1-S4]`/`OPEN[PI1-S5-NODAL]`; the `k > 0` classes are its cuspidal
  siblings with the germ now pinned to `(nu, nu+1)` (SS5), which is *outside* the
  hypothesis class of Theorem N-A / Corollary N-A-RES.
- **`b >= 2` is genuinely new at `N >= 6`.** `[2+2]` (`N=6`), `[2+2]`, `[2+3]`
  (`N=7`), and ten classes at `N = 8` have reducible branch locus; the promoted
  `S_5` machinery (`THEOREM S5-COPRIME-KILL`, C6 SS1.4) and all `N <= 5` reasoning
  assumed `b = 1` and does **not** transfer. These are the highest-value new
  targets.
- **`[3...]`, `[4...]`, `[22...]` are the non-transposition classes.** `[3]` and
  `[22]` give `G <= A_N` (all meridians even), so the `PI1` question is an `A_N`
  question and the transposition-graph tools are unavailable; `[4]` gives odd
  meridians. `[3]` first appears at `N = 6`, `[4]` and `[22]` at `N = 8`.
- **Cheapest live kill.** N-A-RES `[P]` (scalar gauge) applies row-by-row to the
  `k = 0`, `b = 1` classes only; nothing promoted reaches `k > 0` or `b >= 2`.

## 10. OPEN items, audits, lane status

**Settled here (all `[D]`, all UNREVIEWED, none an attainment claim).** (COST)/(BUD)
retires the Euler route; the bounds of Proposition RC; Lemma NL, Gate EMB, Gate
SELF; Lemma D and Gate TRANS-LOC; Gate LZ-KILL, superseding Gate AMS; Lemma CUSP-2
and NO-RAM-2 with the dictionary `k = nu - 1`; Gate TG-N with `iota_i` identified
as the permutation index, and Lemma DEG-PER; NO-DEG-CAP; the non-abelian-image
law; the absence of any `S_4`-resolvent analogue at `N >= 5`; THEOREM CAGE-N; and
the SS9 tables, which reproduce the promoted `N = 4` and `N = 5` residuals exactly.

**Audits against consumed items.**
`[A]` **AUDIT-1** — N5 SS6 lists the `(2,9)` germ as admissible at the `S1`
correction site on the Fox criterion `3 | det(K)`. Lemma CUSP-2 refutes this: at
`mu = 2` the germ is `(nu, nu+1)`, so `(2,5)`, `(2,7)`, `(2,9)` are all impossible
and only `(2,3)` occurs at `k = 1`. The Fox test is necessary, not sufficient.
`[A]` **AUDIT-2** — the first degree admitting a ramified carrier is `N = 10`, not
`N = 7` (N5 SS2.2, SS8) and not `N = 6` (REV SS5). REV's `N = 6` packet
`(2,2,s=2)+(1,0)` is budget-consistent but violates NO-RAM-2, and REV's stop
"do not promote absence of ramification at `N = 6`" should be replaced by
"ramification is absent for `N <= 9`, by NO-RAM-2 plus LZ-KILL".
`[A]` **AUDIT-3** — N5's DQ-3 (`OPEN[N5-DEGREE-CAP]`), flagged there as the
highest-leverage question, is refuted for every `N` by NO-DEG-CAP; it should be
closed NEGATIVE rather than left as a literature-custody item.
`[A]` **AUDIT-4** — N5 SS8's GAP-CANDIDATE against the irreducible chain (its
(4.6) vs smooth-point corrections) is *not* reached by this lane and is untouched;
nothing here depends on it. Independently, Lemma CUSP-2 says that at `mu = 2` a
correction always sits over a **singular** image point, which is the repair target
that lane was asking for, at `mu = 2` only.

**OPEN, typed.**
- `OPEN[PI1-S_N-CAGE(class)]` — the 6 / 10 / 26 classes of SS9 at `N = 6,7,8`, and
  the class family of THEOREM CAGE-N at general `N`. The `b >= 2` classes are new
  at every degree `>= 6` and no promoted machinery reaches them.
- `OPEN[NO-RAM-GENERAL-MU]` — extend Lemma CUSP-2 to `mu >= 3`. The method is the
  same finite computation (`[y^n]J = 0` for `n <= mu-2`, `[y^{mu-1}]J` a unit); a
  partial run at `mu = 3` gives `beta - alpha in {1, alpha}`, so ramification would
  need order pattern `(alpha, 2alpha)`. Not asserted; typed OPEN.
- `OPEN[RED-N-DMIN-BOUND]` — the reducible-lane companion of
  `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`: this lane supplies the floor
  `d_min(D_i) . iota_i >= N - 1`; no promoted input supplies a ceiling, and by
  NO-DEG-CAP none can be phrased in raw degree.
- `OPEN[ZARISKI-GENERIC-LINE-CUSTODY]` — the generic-line surjection
  `pi_1(L \ A_F) ->> pi_1(C^2 - A_F)` is used in Gate TG-N and in the connectivity
  floor; REV SS4 already held it uncustodied and this lane did not repair it. All
  of SS6 is conditional on it; SS2-SS5 and SS8.1-8.6 are not.
- `OPEN[RED-N-B2-STRUCTURE]` — for `b >= 2` the branched components are polynomial
  curves through one common point of `L_inf`; Gate LZ-KILL does not apply because
  `rho` no longer factors through a single component's complement. Is there a
  two-component analogue (e.g. via the normal closure `H_i <| G` of Lemma
  DEG-PER)? This is the sharpest structural successor.

**Provisional status.** Everything typed `[D]` is UNREVIEWED and should be routed
to a different-model hostile gate before promotion, in particular Lemma NL,
Lemma D + Gate TRANS-LOC, Gate LZ-KILL, Lemma CUSP-2 / NO-RAM-2, NO-DEG-CAP, and
the SS9 tables. Lemma CUSP-2 and Gate LZ-KILL carry the lane. No exit-price basis
line is declared: no new exit price is asserted anywhere above.

**FALLACY-v2 self-check.** Flag/place/series: the four objects `t in l'`,
`pi(t)`, `z = h_l(t) in D~_i`, `eta_i(z) in D_i` are kept distinct throughout,
notably in Lemma CUSP-2 where `ord phi_l = e_t . nu` separates the parametrisation
order from the branch multiplicity. Carrier/attainment: every class in SS9 is a
necessary cage; no Keller map is claimed to realise any of them, and the `S_{nu+1}`
construction in SS7 shows only that a local obstruction is *absent*. Floor/
attainment: Lemma B, (TG-N), `d_min . iota >= N-1`, `Sigma_inf >= 1` are floors and
are used only in the tightening direction; NO-DEG-CAP is stated as the absence of a
ceiling, not as a ceiling. Raw remainder degree: raw `deg A_F` is explicitly
disqualified as gauge-dependent and every degree payoff is restated for `d_min`.
Variable/ring map: the target linear changes in Lemma NL and Lemma CUSP-2 are
declared, together with what they preserve (`N`, Keller, profile) and what they
move (`A_F`, degrees). Pole/interior, `sat()`, prime-label, merge-free,
target/arrival: not in play. No gap was filled by cap or analogy; every item that
could not be closed is typed OPEN above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `34939`.
- Body SHA-256:
  `4fef439f6e20a3d3f1335c39f8d039cd0492a7ee6711bf5ba8f3eee0eb05f5d9`.
- Frozen basis: `2c562c110706b732ae8da663c57891768aede3b3`.
