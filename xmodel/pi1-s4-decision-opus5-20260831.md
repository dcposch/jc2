# PI1-S4 decision lane — `S_4` with disjoint transpositions on a one-place polynomial curve

lane: PI1-S4-DECISION
model: opus5
date: 20260831
status: **NO, proved unconditionally, on the coprime stratum `gcd(deg p, deg q) = 1`**;
typed `OPEN[PI1S4-NONCOPRIME]` off it, with the exact missing input named and two
unconditional route-1 obstructions that need no literature at all.

## 0. Provenance and input verification

Four charged inputs verified byte-for-byte with `shasum -a 256` **before any reading**
(4/4 match the boxed values):

```text
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  block-descent-a1-b0-coordinator-integration-fable5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  b0-trivial-dicritical-proof-opus5-20260831.md
8ffc0a06edcf2be3908b1486da57e7d4a024973e679f9d25577cc281ef005320  b0-proof-hostile-review-sol56-20260831.md
cd503e487e3b5277519e4d0668de2d6ca69b0f4002405bfb406cce17df6e3b82  b0-pi1-acquisition-grok46-20260831.md
```

One primary source was re-acquired and re-hashed **in this lane** (official Numdam,
`http://www.numdam.org/article/ASENS_1983_4_16_2_305_0.pdf`, 4 546 575 bytes, 41 pp.):

```text
1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45  nori_ens1983.pdf
```

This is byte-identical to the acquisition ledger's `nori_ens1983.pdf`, so the
acquisition's §1.3 statement IDs are re-usable; but every Nori statement consumed below
was re-read off *this* PDF, not off the acquisition's paraphrase, and two of them
(Def. 3.25 and the acknowledgement paragraph on p. 307) were **not** in the
acquisition's inventory and are load-bearing here.

No CAS was run. All arithmetic below is by hand. Binding stops from integration §3 are
respected: Thm 4.3(5) and its `+eps` identity are not cited; Prop 2.3 is not cited; the
acquisition §4 local-relations claim is treated as an inference and re-derived in §2.

<!-- SECTION 0 END -->

## 1. The question, normalization, standing invariants

**(PI1-S4).** `D subset C^2` irreducible, `normalization(D) = A^1`, one place at
infinity; every affine singularity a double point of two smooth branches (tangency
allowed, type `A_{2k-1}`, `k >= 1`). Is there a surjection
`phi: pi_1(C^2 - D) ->> S_4` with every meridian of `D` mapping to a transposition and
the two local meridians at each double point mapping to **disjoint** transpositions?

**Normalization of coordinates.** `normalization(D) = A^1` and `D` affine make `D` the
image of a polynomial map `gamma(t) = (p(t), q(t))`, birational onto `D`. Put
`m = deg p`, `n' = deg q`. If `m = n'` a shear `y -> y - c x` (which is an automorphism
of `C^2`, so it changes nothing) drops `deg q`; if `m < n'` swap the coordinates. So
**WLOG `d := deg p > n := deg q >= 1`** (`n = 0` forces `d = 1`, the line, excluded
because `pi_1 = Z`). Then:

* `deg D = d` (a generic line meets `D` in `max(m,n') = d` points, `gamma` birational);
* the unique point of `Dbar cap L_infty` is `Q = [1:0:0]`, and the leading form of the
  defining polynomial is `c y^d`, so `[0:1:0] notin Dbar` and the vertical projection
  `pr: (x,y) -> x` is **proper of degree `d` on `D`**: the ZvK setup below is legal;
* in the affine chart `(v,u) = (Y/X, Z/X)` at `Q`, with `s = 1/t`, the place at infinity
  is parametrized by `u = s^d . alpha(s)`, `v = s^{d-n} . beta(s)`, `alpha, beta` units.
  Hence, writing `a := d-n`, `b := d`,

  ```text
  mult_Q(Dbar) = a = d - n,        I(Dbar, L_infty; Q) = b = d,
  ```
  and `L_infty` is the tangent line of the branch at `Q` when `a >= 2`. `Q` is a smooth
  point of `Dbar` iff `a = 1` (consecutive degrees).

**Standing invariants.** Let `s` be the number of affine singular points, `k_p >= 1` the
tangency order at `p in Sing D` (so the germ is `A_{2k_p-1}` and `delta_p = k_p`), and
`delta_aff = sum_p k_p`, `delta_infty = delta_Q(Dbar)`. Geometric genus 0 gives

```text
(G)      delta_aff + delta_infty = (d-1)(d-2)/2 ,        s <= delta_aff .
```

**Vertical tangencies.** `gamma` is an immersion everywhere (a non-immersive point would
produce a singular branch, excluded by hypothesis), and `pr|_D` corresponds to
`t -> p(t)`, a degree-`d` map `A^1 -> C`. Riemann–Hurwitz for `A^1 -> C`:
`1 = chi(A^1) = d . chi(C) - V` where `V = sum_t (e_t - 1) = deg p' `, hence

```text
(V)      V = d - 1        (total vertical ramification, counted with multiplicity).
```

`(V)` is unconditional and is used twice below.

**Two standing consequences of `phi`, recorded once.** `H_1(C^2 - D) = Z` because `D` is
irreducible (Alexander duality in `C^2`), so `pi_1(C^2-D)` abelian would force
`pi_1(C^2-D) = Z`, which has no `S_4` quotient. Therefore

```text
(A)      pi_1(C^2 - D) abelian   ==>   PI1-S4 answers NO for that curve.
```

and it suffices throughout to prove abelianness, or merely that `phi` factors through an
abelian quotient.

<!-- SECTION 1 END -->

## 2. Local braid monodromy at `A_{2k-1}` and at a vertical tangency

Fix a generic `x_0`, `F = {x_0} x C`, `F cap D = d` points, `pi_1(F - D) = F_d` free on
meridians `xi_1, ..., xi_d`. The braid monodromy `rho: pi_1(C - Delta, x_0) -> B_d`
(`Delta` = critical values of `pr|_D`) acts on `F_d` by the Artin action
`sigma_i: xi_i -> xi_i xi_{i+1} xi_i^{-1}, xi_{i+1} -> xi_i`, and Zariski–van Kampen
gives

```text
pi_1(C^2 - D) = < xi_1,...,xi_d | xi_j = rho(g_i)(xi_j),  all i, j > .
```

No relation at infinity is imposed: `pr|_D` is proper, so `C^2 - D` is the total space of
the ZvK presentation as displayed. (The extra relation `xi_d...xi_1 = 1` presents
`pi_1(P^2 - Dbar)`, which is *not* the group in question — cf. Oka's Remark 3, quoted in
the acquisition §2 with the cuspidal-cubic witness.)

**Local braids, re-derived here (the acquisition's §4 identification is an inference and
integration §3 forbids consuming it as a source).**

*Vertical tangency.* A simple vertical tangency at a smooth point of `D` has local model
`x - x_0 = y^2`, two roots `y = +- (x-x_0)^{1/2}`, which exchange once as `x` circles
`x_0`: local braid `sigma_i`. Relations `xi_i = sigma_i(xi_i)`,
`xi_{i+1} = sigma_i(xi_{i+1})` both reduce to

```text
(T)      xi_i = xi_{i+1} .
```

*`A_{2k-1}`.* Two smooth branches of contact `k`: after an analytic change of the
`y`-coordinate the germ is `y = +- x^k` (common tangent `y = 0`, and the vertical line
`x = 0` is transverse to both branches, meeting `D` with multiplicity `2` — so the fibre
count drops by exactly one, as for a node). As `x` circles the origin once,
`x^k -> x^k` and `-x^k -> -x^k`: the two roots do **not** exchange but wind `k` times
around each other. Local braid `sigma_i^{2k}`; equivalently the local link is the
`(2, 2k)` torus link. Writing `w = xi_i xi_{i+1}`, `sigma_i^{2k}` conjugates both `xi_i`
and `xi_{i+1}` by `w^k`, so the relations are the single condition

```text
(N_k)    [ (xi_i xi_{i+1})^k , xi_i ] = 1 ,
```

`k = 1` being ordinary commutation `[xi_i, xi_{i+1}] = 1`.

**Verdict on the flagged inference — CONFIRMED, and sharpened.** Let `tau = (1 2)`,
`tau' = (3 4)` be disjoint. Then `tau tau'` has order `2`, `(tau tau')^k in {1, tau tau'}`,
and both commute with `tau`; so `(N_k)` holds for every `k >= 1`. Explicitly:
`k = 1`: `[tau, tau'] = 1` (disjoint). `k = 2`: `(tau tau')^2 = 1`, so `(N_2)` is
`[1, tau] = 1`. The acquisition's claim is therefore correct, and the strengthening that
matters below is: **a disjoint-transposition pair satisfies the strictly stronger nodal
relation `[xi_i, xi_{i+1}] = 1`, not merely `(N_k)`.** This is the hinge of §5.

**Consequence (route 1's opening observation, made precise).** Every local braid of the
factorization acts on the image tuple as follows: the `d-1` tangency braids identify two
generators, and each `A_{2k-1}` braid acts *trivially* on the image tuple, because the
Hurwitz move of `sigma_i^{2k}` is conjugation of the pair by `(tau_i tau_{i+1})^k`, an
element that centralizes both. So all singular-point data are invisible to `phi`, and
**any obstruction must come from the tangencies and from infinity**. That is the correct
form of the acquisition's "the obstruction MUST be global".

<!-- SECTION 2 END -->

## 3. Route 1 — the braid at infinity (Theorem A, literature-free)

**3.1 The Hurwitz reformulation.** Put `T = (tau_1,...,tau_d)`, `tau_j = phi(xi_j)`. The
ZvK relations say exactly that `T` is a **fixed point of the Hurwitz action** of every
`rho(g_i)` on `S_4^d`, where `sigma_i` acts by
`(...,t_i,t_{i+1},...) -> (..., t_i t_{i+1} t_i^{-1}, t_i, ...)`. Two standing facts:
the Hurwitz action preserves the ordered product `Pi := tau_1 tau_2 ... tau_d`, and it
preserves the generated subgroup `< tau_1,...,tau_d > = S_4` (surjectivity of `phi`, since
the `xi_j` generate).

Since `rho_infty := rho(g_N ... g_1)` lies in the braid monodromy group, `T` is fixed by
`rho_infty` as well. `rho_infty` is the braid traced by the `d` roots `y_j(x)` over a
large circle `|x| = R`: the **braid at infinity**.

**3.2 Identification of `rho_infty` on the coprime stratum.** From §1,
`y ~ const . x^{n/d}` as `x -> infty` (because `y ~ b_n t^n`, `x ~ a_d t^d`). One place at
infinity with `x`-degree `d` there means the `d` roots form a single Puiseux cycle of
order `d`, so:

* `p(rho_infty) in S_d` (underlying permutation) is a **`d`-cycle** — unconditionally;
* if `gcd(n,d) = 1`, the exponent `n/d` is already in lowest terms, the `d` conjugates
  separate at first order, no further characteristic exponent is needed, and the link at
  infinity is the `(d,n)` **torus knot**; up to conjugacy in `B_d`,

  ```text
  rho_infty = delta^n ,       delta := sigma_1 sigma_2 ... sigma_{d-1} .
  ```

*Consistency check (independent of the identification).* Exponent sums: the factorization
of `rho_infty` has `V = d-1` tangency factors (`(V)` of §1) of exponent `1` and, at each
double point, one factor of exponent `2k_p`, so `e(rho_infty) = (d-1) + 2 delta_aff`.
With `(G)` and `delta_infty = (a-1)(b-1)/2 = (d-n-1)(d-1)/2` (the `(a,b)`-cusp value,
`gcd(a,b) = gcd(n,d) = 1`) this is `(d-1) + (n-1)(d-1) = n(d-1) = e(delta^n)`. The two
computations agree, which is a genuine cross-check on both `(V)` and the identification.
It also records, for later use,

```text
(D)      2 delta_aff = (n-1)(d-1)          [coprime stratum] .
```

**3.3 The action of `delta`.** Direct computation (verified at `d = 2, 3` and then by
induction on the word `sigma_1 ... sigma_{d-1}` applied right-to-left):

```text
delta . (t_1,...,t_d) = ( Pi t_d Pi^{-1}, t_1, ..., t_{d-1} ),     Pi = t_1 t_2 ... t_d ,
```

so `delta^d = Delta_d^2` acts as global conjugation by `Pi` (the classical statement that
the full twist conjugates by the total boundary word).

**THEOREM A.** *Let `D` be as in §1 with `gcd(n,d) = 1`, and suppose `phi` exists. Then,
with `Pi = tau_1 ... tau_d in S_4`:*

1. `Pi^n = 1`;
2. `sgn(Pi) = (-1)^d`, hence `dn` is even: **`d` and `n` cannot both be odd**;
3. `n >= 3` (so `d >= 4`), and moreover **either (`ord(Pi) = 3`, `3 | n`, `d` even) or
   (`ord(Pi) = 4`, `4 | n`, `d` odd)**.

*Proof.* Conjugating the whole picture we may take `rho_infty = delta^n`; the Hurwitz
action preserves the ordered product, so `Pi` is unchanged by that conjugation.

(1) `T` is `delta^n`-fixed, hence `delta^{nd}`-fixed. But `delta^{nd} = (delta^d)^n` acts
as conjugation by `Pi^n`. So `Pi^n` centralizes every `tau_j`, hence centralizes
`< tau_j > = S_4`, hence `Pi^n in Z(S_4) = 1`.

(2) `Pi` is a product of `d` transpositions.  With (1), `sgn(Pi)^n = 1`, i.e.
`(-1)^{dn} = 1`.

(3) Extend `T` to a bi-infinite sequence by `t_j = tau_j` for `1 <= j <= d` and
`t_{j-d} := Pi t_j Pi^{-1}`. By 3.3, `(delta^n T)_j = t_{j-n}`, so `delta^n`-fixedness is
`t_j = t_{j-n}` for all `j`: the sequence is `n`-periodic. Let `r := d mod n`; then
`gcd(r,n) = gcd(d,n) = 1` and `n`-periodicity turns `t_{j-d} = Pi t_j Pi^{-1}` into
`t_{j-r} = Pi t_j Pi^{-1}`. So conjugation by `Pi` acts on the `n`-periodic sequence as
the shift by `-r`, which generates `Z/n`. Hence `{tau_1,...,tau_n}` is a **single
conjugation orbit of `tau_1` under `<Pi>`**; and since `d > n` and the sequence is
`n`-periodic, `{tau_1,...,tau_n} = {tau_1,...,tau_d}`, which generates `S_4`.
Now enumerate `g in S_4` by whether the `<g>`-conjugation orbit of some transposition
generates `S_4`: `g = 1`, `g` a transposition, `g` a double transposition all give orbits
of size `<= 2`, generating a subgroup of order `<= 6` — impossible. `g` a `3`-cycle:
orbit `{(14),(24),(34)}` works (orbit `{(12),(23),(13)}` gives `S_3` only). `g` a
`4`-cycle: orbit `{(12),(23),(34),(14)}` works. So `ord(Pi) in {3,4}`; with `Pi^n = 1`
this gives `3 | n` resp. `4 | n`, and `sgn(Pi) = +1` resp. `-1` combined with (2) gives
`d` even resp. `d` odd. Finally `S_4` needs at least `3` transpositions to generate, so
`n >= 3`; and `d > n` gives `d >= 4`. `[]`

Theorem A uses **no literature at all** — only §2, the Puiseux exponent at infinity, and
finite group theory. It already kills every `(d,n)` with `d, n` both odd, and every
`n <= 2`.

<!-- SECTION 3 END -->

## 4. Route 2 — resolution at infinity and Nori's inequality (Theorem B)

**4.1 The two statements consumed, verbatim from the hashed PDF.**

> **PROPOSITION 3.27** (Nori, journal p. 331 = PDF p. 28). *Let `D` and `E` be curves in
> `X` that intersect transversally. Assume that `D` is nodal and `C^2 > 2r(C)` for every
> irreducible curve `C` lying in `D`. Then the kernel `N` of
> `pi_1(X - (D u E)) -> pi_1(X - E)` is abelian and its centraliser is a subgroup of
> finite index.*

> **DEFINITION 3.25** (journal p. 330 = PDF p. 27). *If the curve `C` on `X` is defined
> near `P in C` by `f = 0`, let `f = f_1 f_2 ... f_r` be its prime factorisation in
> `A = O_{X,P}` and let `A(C;P) = sum_{i<j} l(A/(f_i,f_j))` and
> `B(C) = C^2 - 2 sum_P A(C;P)`.* Remark following 3.26: *for a nodal curve `C`,
> `B(C) = C^2 - 2 r(C)`.*

So `r(C)` in 3.27 is the number of nodes, and Nori's own invariant for arbitrary
singularities is `A(C;P) = ` sum of pairwise branch intersection multiplicities; for
`A_{2k-1}` this is exactly `k`, whence `sum_P A(C;P) = delta_aff` for our curves.

> Journal p. 307 (Acknowledgements): *"... an application of 3.27 to the blow-up of `P^2`
> at the cusps of `C` (see 6.5) gives the same conclusion if `C^2 > 6b + 2a`"* (`b`
> cusps, `a` nodes). This is Nori's own licence for the blow-up bookkeeping used below,
> and it pins the accounting: an ordinary cusp costs `sum_j m_j^2 = 2^2+1+1 = 6` and then
> drops out of `2r`; a node is left alone and costs `2`.

**4.2 The surface.** Let `sigma: X' -> P^2` blow up only at `Q` and its infinitely near
points, minimally so that the strict transform `C'` of `Dbar` is smooth at infinity and
meets the reduced total transform `B_infty := sigma^{-1}(L_infty)` transversally at a
single smooth point of `B_infty`. Then

```text
X' - B_infty = P^2 - L_infty = C^2  (simply connected),
X' - (C' u B_infty) = C^2 - D ,     C' . B_infty = 1 ,
C'^2 = d^2 - sum_j m_j^2 ,          sum_j m_j(m_j - 1) = 2 delta_infty ,
```

`m_j` the multiplicities of `Dbar` at the blown-up points. Write `M_infty = sum_j m_j`
and `N_infty = sum_j m_j^2 = 2 delta_infty + M_infty`.

**LEMMA 4.3 (general numerical reduction).** *`C'^2 > 2 delta_aff` if and only if
`M_infty <= 3d - 3`.*
*Proof.* `C'^2 - 2 delta_aff = d^2 - 2delta_infty - M_infty - [(d-1)(d-2) - 2delta_infty]`
by `(G)`, `= d^2 - (d-1)(d-2) - M_infty = 3d - 2 - M_infty`. `[]`

Since `s <= delta_aff`, `M_infty <= 3d-3` implies Nori's hypothesis `C'^2 > 2 r(C')` for
the nodal case. (Equivalently `C'^2 > 2 delta_aff` says `K_{X'} . C' <= -3`.)

**LEMMA 4.4 (coprime evaluation).** *If `gcd(n,d) = 1` then, with `a = d-n`, `b = d`,*

```text
M_infty = a + b - 1 = 2d - n - 1 ,   N_infty = ab = (d-n)d ,   C'^2 = nd ,
B(C') = C'^2 - 2 delta_aff = nd - (n-1)(d-1) = n + d - 1 > 0 .
```

*Proof.* `gcd(a,b) = gcd(n,d) = 1`, so the germ at `Q` is the `(a,b)`-cusp
`u^a = v^b`-type with `L_infty` the maximal-contact smooth branch (`I = b`), and
`2 delta_infty = (a-1)(b-1)` (standard). The minimal embedded resolution runs the
Euclidean algorithm on `(a,b)`: while `b > a` a blow-up of multiplicity `a` replaces
`(a,b)` by `(a, b-a)`, symmetrically for `a > b`, terminating at `(1,1)` with one last
blow-up separating the strict transform from the previous exceptional component. Both
`M(a,b) = a+b-1` and `N(a,b) = ab` satisfy this recursion
(`a + [a + (b-a) - 1] = a+b-1`; `a^2 + a(b-a) = ab`) with the base value at `(1,1)`;
they are moreover equivalent to each other given `2delta_infty = (a-1)(b-1)`, since
`N - (N - M) = M` reads `ab - (a-1)(b-1) = a+b-1`. Sequences checked directly:
`(2,3): 2,1,1`; `(2,5): 2,2,1,1`; `(2,7): 2,2,2,1,1`; `(3,4): 3,1,1,1`;
`(3,5): 3,2,1,1`; `(3,7): 3,3,1,1,1`; `(4,5): 4,1,1,1,1` — all with `sum m_j = a+b-1`,
`sum m_j^2 = ab`, `sum m_j(m_j-1) = (a-1)(b-1)`. The case `a = 1` (flex at infinity) is
`M = N = b = d` and is included. Then `C'^2 = d^2 - (d-n)d = nd`, and `2 delta_aff` is
`(D)` of §3.2. `[]`

Note `M_infty = 2d-n-1 <= 2d-2 <= 3d-3` for `d >= 1`: Lemma 4.3's hypothesis holds
throughout the coprime stratum, with room to spare.

**THEOREM B.** *Let `D` be as in §1 with `gcd(n,d) = 1` and **all affine singularities
ordinary nodes**. Then `pi_1(C^2 - D)` is abelian, hence `= Z`, and PI1-S4 answers NO for
`D`.*

*Proof.* Apply Prop. 3.27 on `X'` with `D_{Nori} = C'` and `E = B_infty`. `C'` is
irreducible and nodal (smooth at infinity by construction of `X'`, nodal in `C^2` by
hypothesis); `C'` and `B_infty` meet transversally (§4.2); and
`C'^2 = nd > (n-1)(d-1) = 2 delta_aff = 2 r(C')` by Lemma 4.4, the inequality being
`n + d - 1 > 0`. Hence `N = ker(pi_1(X' - C' u B_infty) -> pi_1(X' - B_infty))` is
abelian. But `X' - B_infty = C^2` is simply connected, so `N` is all of
`pi_1(X' - C' u B_infty) = pi_1(C^2 - D)`. Now use `(A)` of §1. `[]`

Theorem B is the Neumann–Norbury recast of Nori named in the acquisition's §5, but with
the numbers actually evaluated for the class: the inequality is not merely satisfiable,
it holds **identically** on the coprime stratum, with slack `n + d - 1`.

<!-- SECTION 4 END -->

## 5. Removing the tangency hypothesis (Theorem C, nodalization)

Prop. 3.27 genuinely needs `D` nodal: in its proof the normalisation `H` must "intersect
the closure of `q^{-1}(R) - H` transversally" in order to invoke Nori's Lemma 1.4, and at
an `A_{2k-1}` the other branch meets `H` with multiplicity `k`. Two independent repairs
follow; the second is complete.

**5.1 Fallback (literature-only): blow up the tangential points.** Following Nori's own
recipe (p. 307), blow up each `A_{2k_p-1}` point `k_p` times — each blow-up has
multiplicity `2`, and after `k_p` of them the two branches are separated and meet the
last exceptional curve transversally at distinct points, so the strict transform is
smooth there. Put the exceptional curves into `E`; then `X'' - E = C^2 - {tangential
points}` is still simply connected and `X'' - (D u E) = C^2 - D` is unchanged. The cost
is `sum_j m_j^2 = 4 k_p` per tangential point, and `2r` now counts only the `s_1`
remaining nodes. With `K_tac := sum_{p : k_p >= 2} k_p` and `delta_aff = s_1 + K_tac`,
Nori's inequality `C'^2 - 4 K_tac > 2 s_1` becomes, on the coprime stratum,
`nd - 4K_tac > (n-1)(d-1) - 2K_tac`, i.e.

```text
(B')     2 K_tac <= n + d - 2      ==>   pi_1(C^2 - D) abelian   ==>   NO.
```

`K_tac = 0` recovers Theorem B. `(B')` is unconditional and uses only the hashed Nori.

**5.2 The complete repair: nodalization inside the parameter space.** Fix `gcd(n,d)=1`
and let `P_{d,n} = {(p,q) : deg p = d, deg q = n}`, an irreducible quasi-affine variety
(a Zariski-open subset of `C^{d+1} x C^{n+1}`). Every member is birational onto its image
(a factorisation `gamma = gamma' o psi` with `deg psi = e` would force `e | gcd(d,n)=1`)
and has one place at infinity at `Q = [1:0:0]`.

**LEMMA 5.3 (`delta` is constant).** *On `P_{d,n}` with `gcd(n,d)=1`,
`delta_infty = (d-n-1)(d-1)/2` and hence `delta_aff = (n-1)(d-1)/2` are constant.*
*Proof.* The germ at `Q` is always parametrized by `(v,u) = (s^{d-n} beta, s^d alpha)`
with `gcd(d-n,d)=1`, i.e. is always the `(d-n, d)`-cusp; then `(G)`. `[]`

**LEMMA 5.4 (generic member is nodal).** *If `n >= 3` and `d >= 4`, the generic member of
`P_{d,n}` is an immersion with only ordinary double points and no triple point.*
*Proof.* Coefficient count: `{1,t,...,t^d}` and `{1,...,t^n}` separate `1`-jets at any
two distinct parameters once `d, n >= 3`, so on `P_{d,n}` the conditions
(i) `gamma'(t) = 0` (2 conditions on a 1-parameter family of `t`),
(ii) `gamma(t_1) = gamma(t_2)` **and** the tangents agree (3 conditions on a 2-parameter
family of pairs),
(iii) `gamma(t_1) = gamma(t_2) = gamma(t_3)` (4 conditions on a 3-parameter family)
are each independent, so each bad locus has codimension `>= 1` in `P_{d,n}`. `[]`

(The hypothesis `n >= 3` is exactly what Theorem A(3) supplies once `phi` is assumed;
`n <= 2` is already dead by Theorem A.)

**LEMMA 5.5 (local shape of the degeneration).** *Let `D_0 in P_{d,n}` and let `D_t -> D_0`
be nodal members. By 5.3 the total double-point length `delta_aff` is constant, so at
each `p in Sing D_0` of type `A_{2k_p-1}` the length-`k_p` piece of the double-point
scheme of `D_0` (supported at the single pair `(t_1^0, t_2^0)`) spreads into exactly
`k_p` reduced pairs near `(t_1^0,t_2^0)`. Hence near `p`, `D_t` is two smooth branches —
deformations of the two branches of `D_0` — crossing transversally at `k_p` points.*

**LEMMA 5.6 (braid monodromy comparison).** *With the vertical projection of §1 fixed for
both curves, and `t` small, choose disjoint discs `Y_i` in the `x`-line, one around each
critical value of `D_0`, containing all critical values of `D_t` that converge to it.
Then:*
1. *over `partial Y_i` the two curves are isotopic, so the braid of `partial Y_i` is the
   same factor `beta_i` for `D_0` and for `D_t`;*
2. *for a disc around a vertical tangency or a node of `D_0` nothing splits, and the
   relation is unchanged;*
3. *for a disc `Y` around an `A_{2k-1}` point, the two relevant strands stay inside a
   thin tube while the other `d-2` strands stay away, so all local braids lie in a single
   `B_2 = <sigma>` conjugated into `B_d` by one fixed braid `w`. `B_2` is abelian, so the
   `k` factors of `D_t` inside `Y` are all equal to `w sigma^2 w^{-1}`, and the `k`
   relations they impose are the single relation `[w(xi_a), w(xi_b)] = 1`, while `D_0`
   imposes `[ (w(xi_a) w(xi_b))^k , w(xi_a) ] = 1`.*
*Consequently*

```text
(*)   pi_1(C^2 - D_t) = pi_1(C^2 - D_0) / << [w_p(xi_a), w_p(xi_b)] : p tangential >> .
```

**THEOREM C.** *Let `D` be as in §1 with `gcd(n,d) = 1`, tangency allowed. Then
`pi_1(C^2-D)` has no surjection onto `S_4` sending meridians to transpositions and the
two local meridians at each double point to disjoint transpositions.*

*Proof.* Suppose `phi` exists. By Theorem A(3), `n >= 3` and `d >= 4`. By 5.4 pick a
nodal `D_t in P_{d,n}` close to `D`; by 5.3 and 5.5 the degeneration is locally as in
5.5, and by 5.6 the group `pi_1(C^2-D_t)` is the quotient `(*)`. By §2, `phi` sends the
two local meridians at each tangential point to **disjoint** transpositions, which
commute; so `phi` kills every relator on the right-hand side of `(*)` and therefore
factors through `pi_1(C^2 - D_t)`. `D_t` is nodal with `gcd(n,d) = 1`, so Theorem B makes
`pi_1(C^2-D_t)` abelian. Hence `im(phi)` is abelian, contradicting `im(phi) = S_4`. `[]`

Two remarks. First, the deformation is used only to *transport a group-theoretic
consequence*, never to claim `D` itself is nodal; the direction of Zariski's
specialisation principle (special complement surjects onto general complement) is the
direction actually used. Second, Nori's own invariant for arbitrary singularities gives
independent corroboration: by Def. 3.25, `sum_P A(C';P) = delta_aff` for our curves, so
`B(C') = C'^2 - 2 delta_aff = n + d - 1 > 0` **identically on the coprime stratum**
(Lemma 4.4). Any extension of Prop. 3.27 from "nodal" to "`B(C) > 0`" — the shape Nori's
3.26 already has — would give Theorem C directly, without the deformation. Nori does not
state that extension, so it is not consumed; `(*)` is what carries the proof.

<!-- SECTION 5 END -->

## 6. Main theorem and decision

**MAIN THEOREM.** *Let `D subset C^2` be an irreducible polynomial curve with
`normalization(D) = A^1`, one place at infinity `Q`, and every affine singularity a double
point of two smooth branches (tangency allowed). Assume the intrinsic coprimality
condition*

```text
(C1)     gcd( mult_Q(Dbar) , I(Dbar, L_infty; Q) ) = 1
```

*(equivalently `gcd(deg p, deg q) = 1` after the normalization of §1; equivalently the
place at infinity has exactly one Puiseux pair). Then `pi_1(C^2 - D)` admits **no**
surjection onto `S_4` carrying every meridian to a transposition and the two local
meridians at each double point to disjoint transpositions.*

*Proof.* Theorem C, which invokes Theorem A for `n >= 3`, Lemmas 5.3–5.6, and
Theorem B. `[]`

**Scope of the stronger, abelian conclusion.** `pi_1(C^2-D) = Z` is proved here on `(C1)`
for `D` nodal (Theorem B) and for `D` tangential with `2 K_tac <= n + d - 2` (`(B')`).
For the remaining tangential curves on `(C1)`, what is proved is the
representation-level statement of the Main Theorem — which is exactly what PI1-S4 asks
— and not abelianness; Theorem C routes `phi` through the abelian group
`pi_1(C^2 - D_t)` of a nearby nodal curve without asserting that the two groups agree.
This distinction is recorded rather than smoothed over: an unqualified "the complement is
abelian in the whole class" would be an overclaim.

**Decision: NO on the coprime stratum, unconditionally.** No YES candidate exists there —
not merely "none found": Theorems B/C forbid one. Off `(C1)` the answer is typed
`OPEN[PI1S4-NONCOPRIME]` (§9), with the missing input a purely **local, numerical**
statement about the place at infinity — no group theory and no new topology.

**What this does and does not do for the campaign.** Integration §2 asks PI1-S4 for the
curve `D_1` of the repaired residual (Thm 4.3(1)–(4) + gate). The Main Theorem closes
`OPEN[B0-N4-REDUCIBLE-PI1]`, hence B0 at `N=4` unconditionally and `A_F = B` at rank
four, **provided `D_1` satisfies `(C1)`**. Nothing in the charged inputs pins the pair
`(deg p, deg q)` for `D_1`, so that provision is not discharged here and must not be
assumed: this is a scope statement, not a promotion. Three separate unconditional gains
do transfer regardless of `(C1)`:

* **Theorem A**, which is literature-free and holds for tangential curves too;
* the **local-relation verdict** of §2 (the acquisition's flagged inference CONFIRMED and
  sharpened to the nodal relation), which integration §3 required a successor to settle;
* the reduction of the whole remaining question to `M_infty <= 3d-3` (Lemma 4.3).

<!-- SECTION 6 END -->

## 7. Route 3 — Orevkov negativity: literature status

Orevkov, *Math. USSR Sb.* **65** (1990). The author-site copy
(`math.univ-toulouse.fr/~orevkov/fg.pdf`) that the acquisition found 504-ing was not
retried as a substitute for an official source; Math-Net.Ru and the Springer/IOP mirrors
of *Mathematics of the USSR-Sbornik* were the only official routes considered, and no
copy was obtained and hashed in this lane. Library-genesis-type mirrors are excluded by
lane rules and were not used.

**Therefore no Orevkov-1990 statement is consumed anywhere above.** The negativity
theorem is recorded here only as the acquisition's unhashed paraphrase, marked
UNVERIFIED, and it is not needed: Theorem B does not use it, and Theorem B's inequality
`C'^2 = nd > (n-1)(d-1)` is stronger than what a negativity hypothesis would buy, because
it holds identically rather than conditionally. If a hashed copy is later obtained, the
predicted overlap is that "negativity at infinity" for a one-place curve is implied by
`(C1)`; that prediction is **not** used.

<!-- SECTION 7 END -->

## 8. Route 4 — direct Zariski–van Kampen: what it does and does not add

Route 4 was executed to the extent that it is decisive, and its results are already in
place: §2 is the full local analysis (both `k = 1` and `k = 2` explicit, and general `k`),
`(V)` of §1 is the exact tangency count `V = d-1`, and §3 is the global relation at
infinity in Hurwitz form. Three further ZvK facts were derived and are recorded because
they are unconditional and constrain any future YES attempt:

1. **Minimal transitive factorization.** `p(sigma^{2k}) = id` and `p(sigma) = ` a
   transposition, while `p(rho_infty)` is a `d`-cycle. So the `d-1` tangency braids
   project to `d-1` transpositions in `S_d` whose product is a `d`-cycle: they form a
   **spanning tree** on the `d` strands. `V = d-1` is exactly minimal; there is no slack.
2. **The associated cover is smooth with `chi = 3`.** The degree-4 branched cover
   `Y -> C^2` attached to `phi` is unramified over `C^2 - D`, has profile `(2,1,1)` over
   `D - Sing D`, and exactly two points over each double point (orbits `{1,2},{3,4}` of
   `<(12),(34)>`), where it is a smooth double cover branched over one branch. Stratifying,
   with `chi_c(D) = 1-s` and `chi_c(D - Sing D) = 1-2s`,

   ```text
   chi(Y) = 4(1 - chi_c(D)) + 3 chi_c(D - Sing D) + 2s = 4s + 3 - 6s + 2s = 3 ,
   ```
   independent of `s` and of the tangency orders. Fibring `Y` over the `x`-line gives
   `chi(Y) = (4-d) + V` (a vertical tangency contributes `+1`, a double point `0`), so
   `V = d-1` again — an independent confirmation of `(V)`.
   The ramification curve `R subset Y` is **smooth** and `R -> D` is the normalization,
   so `R ~ A^1`.
3. **No local obstruction anywhere.** Both `(T)` and `(N_k)` are satisfiable by
   transposition tuples for every `k`; combined with (1) this shows that a YES, if one
   existed off `(C1)`, could not be detected by any local datum — it would have to be
   exhibited by an explicit curve plus an explicit `d`-tuple of transpositions fixed by
   the full braid monodromy group.

None of 1–3 by itself refutes PI1-S4; they are the honest yield of route 4 and they say
where a countermodel would have to live.

<!-- SECTION 8 END -->



## 9. Residual: typed OPEN and successor

**`OPEN[PI1S4-NONCOPRIME]`.** *PI1-S4 for curves violating `(C1)`, i.e. with
`g := gcd(mult_Q(Dbar), I(Dbar,L_infty;Q)) = gcd(deg p, deg q) >= 2`, equivalently with
two or more Puiseux pairs at infinity.* Exactly two inputs are missing, both narrow:

**(i) Local, numerical — the only thing Theorem B needs.** For the place at infinity of a
polynomial curve with `mult_Q(Dbar) = d-n` and `I(Dbar,L_infty;Q) = d`, prove

```text
(M-INF)   M_infty := sum_j m_j  <=  3d - 3
```

over the minimal blow-up sequence making the strict transform smooth and transverse to
`sigma^{-1}(L_infty)` at a smooth point of it. By Lemma 4.3 this is *equivalent* to
`C'^2 > 2 delta_aff`, hence gives Nori's inequality for every `s <= delta_aff`, hence
gives Theorem B verbatim in the non-coprime case. Status: **proved** when `g = 1`
(Lemma 4.4, `M_infty = 2d-n-1 <= 2d-2`); **verified** in the smallest non-coprime worked
case `(d,n) = (4,2)`, `gamma(t) = (t^4, t^2+t)`, whose place at infinity is a `(2,5)`-cusp
with multiplicity sequence `2,2,1,1`, so `M_infty = 6 <= 9 = 3d-3` (and `C'^2 = 6 > 2 = 2s`);
**not proved** in general. Note the crude route fails: `M_infty <= 2 delta_infty + tail`
is far too weak, and `M_infty <= 2b-1` is false for germs of small `I(B,L)`, so the proof
must use `I(Dbar,L_infty;Q) = d` (the shared-cluster identity
`sum_{j in S} m_j = d`, `S` an initial segment) together with `mult_Q = d-n`. The
residual content is a bound on `sum_{j notin S} m_j` by `2d-3`.

**(ii) Global, one line of geometry — what Theorem C needs.** Either
(ii-a) an **equisingular-at-infinity nodalization**: a locally closed subvariety of
`P_{d,n}` containing `D` on which `delta_infty` is constant and whose generic member is
nodal (when `g >= 2`, `delta_infty` is *not* constant on all of `P_{d,n}`, so Lemma 5.3
fails and Lemma 5.5's length bookkeeping breaks); or
(ii-b) an extension of Nori's Prop. 3.27 replacing the hypothesis "`D` is nodal,
`C^2 > 2r(C)`" by "`B(C) > 0`" in the sense of his own Def. 3.25. (ii-b) is strictly
better: it would delete §5 entirely, in the coprime case too, since `B(C') = n+d-1 > 0`
there identically. Nori proves the `B(C)`-form only in 3.26, under `C cap R = empty`,
which does not apply; the obstruction in the 3.27 proof is precisely that the
normalisation `H` must meet the rest of `q^{-1}(D u E)` transversally, which fails at an
`A_{2k-1}` for `k >= 2`.

**Without (i) and (ii), the following are already unconditional off `(C1)`:**
`p(rho_infty)` is a `d`-cycle; `V = d-1`; `chi(Y) = 3`; §2's local verdict; and, whenever
`(M-INF)` is checked for the particular curve, the criterion
`C'^2 > 2 s_1 + 4 K_tac` (the `(B')` bookkeeping) decides that curve.

**Successor's first move (route 1, non-coprime).** For `g >= 2` the braid at infinity is
an iterated-torus (cable) braid, not `delta^n`, so Theorem A's proof does not transcribe.
The natural attempt is to collapse cables: group the `d` strands into `p_1` blocks of size
`d/p_1`, take block products `Pi_1,...,Pi_{p_1}` in `S_4`, and check whether the induced
action of `rho_infty` on `(Pi_1,...,Pi_{p_1})` is the Hurwitz action of
`delta_{p_1}^{q_1}` (the internal full twists conjugate each block by its own product and
so act trivially on that product). If so, the Theorem A argument reruns at the outer
level and yields `(Pi_1 ... Pi_{p_1})^{q_1} = Pi^{q_1} = 1` provided
`<Pi_1,...,Pi_{p_1}>` is centreless. **This is stated as the successor's hypothesis, not
as a result**: neither the block-collapse compatibility nor the centrelessness is
established here, and no gap above is filled by it.

<!-- SECTION 9 END -->

## 10. Ledger

**Charged inputs** (verified before reading; §0). **Primary literature consumed** — one
item only:

```text
1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45  nori_ens1983.pdf
   M. V. Nori, "Zariski's conjecture and related problems",
   Ann. Sci. Ec. Norm. Sup. (4) 16 (1983) 305-344.
   Official source: http://www.numdam.org/article/ASENS_1983_4_16_2_305_0.pdf
   4546575 bytes, 41 pp.; re-fetched and re-hashed in this lane; byte-identical to the
   acquisition ledger's copy.
   Statements consumed, each read off this PDF:
     Prop. 3.27  (journal p. 331 = PDF p. 28)  -- quoted verbatim in Sec. 4.1
     Def.  3.25 + remark after 3.26 (journal p. 330 = PDF p. 27) -- A(C;P), B(C), r(C)
     Acknowledgements para. (journal p. 307 = PDF p. 4) -- blow-up bookkeeping licence
                                                          ("C^2 > 6b + 2a")
```

**Not consumed.** Fulton (Ann. of Math. 111), Deligne (Bourbaki 543), Oka (ICTP),
Cogolludo, Neumann–Norbury, Artal–Dimca, Dethloff–Orevkov, and Orevkov *Math. USSR Sb.*
65 (1990). No statement of any of these is used in Theorems A, B, C or the Main Theorem.
Orevkov 1990 was not obtained from an official source in this lane and is typed
UNVERIFIED (§7).

**Standard facts used without a hashed citation** (all classical, none campaign-specific):
Zariski–van Kampen for an affine curve under a proper linear projection; the Artin action
of `B_d` on `F_d`; `H_1(C^2 - D) = Z^{#components}`; `delta = (a-1)(b-1)/2` for the
`(a,b)`-cusp; blow-up formulas `C'^2 = d^2 - sum m_j^2`, `K . C' = -3d + sum m_j`, and
`p_a` drop `sum m_j(m_j-1)/2`; Riemann–Hurwitz.

**Own contributions, in dependency order.** §2 local braids and the disjointness verdict;
§3 Theorem A (literature-free); Lemma 4.3 (`C'^2 > 2delta_aff <=> M_infty <= 3d-3`);
Lemma 4.4 (`C'^2 = nd`, `B(C') = n+d-1`); Theorem B; Lemmas 5.3–5.6 and Theorem C; the
Main Theorem; §8's `chi(Y) = 3` cross-check on `V = d-1`.

**Status line.** `PI1-S4 = NO` on the coprime stratum `(C1)`, unconditional.
`OPEN[PI1S4-NONCOPRIME]` off it, with `(M-INF)` and (ii-a)/(ii-b) named as the exact
missing inputs. No YES candidate exists on `(C1)`; none is exhibited off it. No new exit
price is asserted, so no `charge_basis` line is declared.

<!-- BODY-END -->
