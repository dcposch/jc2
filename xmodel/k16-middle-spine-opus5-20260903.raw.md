# K16 ray theorem (T): the tuple-level Laurent bridge, resolved both ways

**Lane:** `k16-middle-spine-opus5-20260903`
**Date:** 2026-09-03
**Verdict:** **(T) NOT proved for all `t`.** Attack A is **resolved, and it is a
refutation**: the tuple-level Laurent bridge cannot supply a uniformly
inconsistent fixed-size subsystem, because on the top graded face the bridge's
vanishing conditions *are* the charged Jacobian rows `E1,E2,E3`, its one free
slot *is* the charged obstruction row `E4`, and its required nonvanishing is a
**unit** in `A_t` for every `t>=1`. The same analysis yields a positive
by-product that is promoted: a **uniform bridge normal form** (Moh's own
p.209 construction, made all-`t`) giving a necessary chart with **`6t+5`
unknowns** instead of `9t+9`, on which (T) is re-certified at `t=1,2` roughly
**18x faster** than the charged chart.
**Scope:** no ledger edit; no `jc2-lean`; no `ideation-*`; no in-progress lane
report read. New artifacts only in `box/k16spine-opus-20260903/`.

Claim types are literal. **SOURCE-READ** = the frozen Moh PDF page was rendered
and read as an image. **DERIVED** = a displayed mathematical consequence.
**MEASURED** = a reproducible program result. **PROVED-HERE** = a checked exact
proof or computation in this lane. `OPEN[...]` is never filled by analogy.

## 0. Custody and fail-closed gate

**MEASURED.** The readable receipt `xmodel/k16-middle-spine-opus5-20260903.run.v2`
was parsed with `awk`, pairing each `charged_input_<i>_sha256` with the matching
`charged_input_<i>_basename` under `/tmp/jc2-lane.EKfgZ6/inputs/`, and the
generated manifest was passed to `sha256sum -c`. **20/20 `OK`**; no digest was
retyped. The stop-on-content-mismatch gate did not fire.

**SOURCE-READ.** Printed page `N` is PDF page `N-139` in the 74-page frozen Moh
PDF. Rendered at 165 dpi to `box/k16spine-opus-20260903/moh-pages/`: pp.
**149, 150, 151, 152, 207, 208, 209**.

## 1. What the source actually says

**SOURCE-READ (p.149, Theorem 1.2).** For a coherent complete system of
`pi`-roots with multiplicities `{l_i}` and accuracy `lambda`, `d | gcd(l_i)`,
and `h` a `d`-th quasi-approximate root with `f = h^d + sum_{j=1..d} h_j h^{d-j}`,
`deg h_j < deg h = deg f / d`, one has `ord h_j(sigma_i) >= (lambda/d) j`. This
is the exact inequality the charged coefficient spaces `S_i` come from.

**SOURCE-READ (p.150, characteristic data).** `g(x,y)=eta^{-n}`,
`eta=g^{-1/n}=y^{-1}+alpha_2(x)y^{-2}+... in k[x]((eta))`, and
`f(x,y)=eta^{-m}+sum_{j>-m} f_j(x) eta^j`. Then

```text
d_1=n,  d_{j+1}=gcd(n,M_1,...,M_j),  M_j=min{i : f_i(x)!=0, d_j not| i},  M_{h+1}=inf.
```

So for the descended ray the 4-tuple `(n,m;M_2;V_2)=(12t+4,8t+4;12t+1;3)` is
**exactly**: with `eta=P^{-1/n}` and `Q=eta^{-m}+sum q_i eta^i`,

```text
q_i = 0 for every i < M_2 = 12t+1 with 4 not| i,      and   q_{M_2} != 0.
```

**SOURCE-READ (p.151, Lemma 2.1).** `J_{x,y}(f,g)=c` a nonzero constant iff
`f_i'(x)=0` for all `i<n-1` and `f_{n-1}'(x)` is a nonzero constant; Moh then
notes `M_i<=n-1` and stresses ignorance about the `M_i` (Sathaye's example: for
`X=T^6+...`, `Y=T^8+...`, `M_2` can never be 13).

**SOURCE-READ (p.152, Prop. 2.2).** With `E := ord_eta(sum f_j(x)eta^j - sum f_j(0)eta^j)`
and `M_r <= E`: `deg_y T_r(f,g) = -mu_r`, and `T_r` is monic in `y` when `M_r<E`.

**SOURCE-READ (p.207, Appendix II).** Moh's first descended table row is
`(n, m=-M_1, M_2, V_2, delta_2, delta_1, Jacobian) = (16, 12, 13, 3, -1, 1/4, X)`.
That is **exactly the `t=1` member of the ray**, with the monomial Jacobian `X`.

**SOURCE-READ (p.208-209).** Moh writes `h(x,y)=y^3(y-x)+b_1y^3+b_2y^2+b_3y+b_4
= yA+b_4 = y^2B+b_3y+b_4`, `gbar=h^4+alpha_1h^3+alpha_2h^2+alpha_3h+alpha_4`,
`fbar=h^3+beta_2h+beta_3` (no `beta_1`), with `alpha_1` constant,
`alpha_2=c_1A+c_2`, `beta_2=c_3A+c_4`, `alpha_3=c_5A+c_6B+c_7` (the frozen page
prints `c_5A+c_5B`, an evident source typo), `beta_3=c_8A+c_9B+c_{10}`,
`alpha_4=c_{11}A+c_{12}B+c_{13}(y-x)`: **17 coefficients**. He then applies the
tuple condition in the *reciprocal* parameter,

```text
f=eta^{-12},  g=eta^{-16}+a_1eta^{-12}+a_2eta^{-8}+a_3eta^{-4}+a_4+...,
gauge (f,g) -> (f-(3/4)a_3,  g-a_1f-a_4),
g = h^4+(4/3)(beta_2h^2+beta_3h)+(2/9)(beta_2^2+2gam)-(4/81)del+a_2h^2,
beta_2beta_3=gam*h+gam*,  beta_2^3=del*h^2+del*,  deg gam*<4, deg del*<8,
```

**reducing 17 coefficients to 10.** This is the bridge, done by the source, at
`t=1`. The charged reports use the order chart only and never import it.

## 2. The reciprocal exponent dictionary (charged as conditional; proved here)

**PROVED-HERE.** Let `eta=P^{-1/n}`, `Q=eta^{-m}+sum_i q_i eta^i`, and
`etat=Q^{-1/m}`, `P=etat^{-n}+sum_j p_j etat^j`. Write `U:=sum_i q_i eta^{i+m}`,
so `Q=eta^{-m}(1+U)` and `etat=eta(1+U)^{-1/m}`, hence

```text
P*etat^{n} = (1+U)^{-n/m}.
```

Suppose `U = U_4 + U_bad` with `U_4` supported on `4Z` and `ord_eta U_bad = M_2+m`.
Then `(1+U)^{-n/m} = (1+U_4)^{-n/m} * (1 + U_bad/(1+U_4))^{-n/m}`, whose first
non-`4Z` exponent is `M_2+m` with coefficient `-(n/m) q_{M_2} != 0`
(the `U_bad^2` correction has order `2(M_2+m)`). The substitution
`eta -> etat = eta*(4Z-supported)*(1+O(eta^{M_2+m}))` preserves `4Z`-support and
scales that coefficient by a unit. Since `4 | n`, the `etat`-exponent
`M_2+m` corresponds to `p_j` with `j+n=M_2+m`, i.e.

```text
N = M_2-(n-m) = m-3 = 8t+1,        M_2+m = 20t+5 = 5(4t+1).
```

The argument is symmetric, so the two tuple statements are **equivalent**, not
merely dictionary-compatible. This removes the "conditional on the reciprocal
exponent dictionary" qualifier in the charged `OPEN[DESCENT-ANCHOR]` entry.
At `t=2` it reproduces `N=17` and relative order `45`, as charged.

## 3. Attack A, part 1: the bridge is *implied* on the graded face

Write `e=3t+1`, `q=2t+1`, `r=e/q`, `xi=h^{-1/4}`, and

```text
G_P := P h^{-e} = 1+sum_i alpha_i h^{-i},   G_Q := Q h^{-q} = 1+sum_j beta_j h^{-j},
Phi := Q eta^m = G_Q * G_P^{-q/e}.
```

**DERIVED.** `q_i = [eta^{i+m}] Phi`, so the tuple condition is: `Phi` has no
`eta`-exponent outside `4Z` below `20t+5`, and its `eta^{20t+5}` coefficient is
nonzero.

**PROVED-HERE (no fixed-index bridge equation exists).** `alpha_i, beta_j` are
scalars for `i,j<=t` and `h^{-i}=xi^{4i}`, so `G_P, G_Q in 1 + xi^4 k[..][[xi]]`
with the first non-`4Z` contribution at `xi^{4t+1}` (the `A`-component of
`alpha_{t+1}`/`beta_{t+1}`, `ord_xi A = -3`). The change of parameter
`eta = xi G_P^{-1/n}` is itself `4Z`-supported modulo `O(xi^{4t+2})`, so
`[eta^s]Phi = 0` identically for every `s < 4t+1` **with `4 not| s`**
(the `4 | s` coefficients are of course not zero). **Every bridge equation sits at a moving
index**; there is no `t`-independent one to add to the low bands.

**PROVED-HERE (graded face).** Let `Ubar = A h^{-(t+1)}`; since `ord_eta A = -3`
and `ord_eta h = -4`, its `eta`-order is `4t+1` (charged: `wt(x)=4t+1`). Then `Ubar^k` sits at `eta`-exponent
`k(4t+1)`, and `k(4t+1) == k (mod 4)`, so the bridge's conditions at the pure
`Ubar`-powers are exactly

```text
[Ubar^1]Phi = [Ubar^2]Phi = [Ubar^3]Phi = 0,   [Ubar^4]Phi free (exponent 16t+4 in 4Z),
[Ubar^5]Phi != 0                              (exponent 20t+5 = M_2+m, the anchor).
```

With the charged initial forms `F=1+xUbar+yUbar^2`, `G=1+g_1Ubar+g_2Ubar^2+g_3Ubar^3`,
`Phi = F G^{-1/r}`. `box/k16spine-opus-20260903/bridge_graded.py` computes, in
`Q(r)[x,y]`:

| object | value |
|---|---|
| `phi_1,phi_2,phi_3` | `0` identically once `(g_1,g_2,g_3) = (F^r)_{1,2,3}` |
| `phi_4` | `(r-1)(r^2x^4-5rx^4+12rx^2y+6x^4-24x^2y+12y^2)/24` |
| `phi_5` | `-x(r-1)(r^3x^4-4r^2x^4+10r^2x^2y+rx^4-5rx^2y+6x^4-30x^2y+30y^2)/30` |

**MEASURED / PROVED-HERE.** The driver also verifies against the charged
normalizer lemma: `g_1=rx`, `g_2=ry+C(r,2)x^2`, `g_3=2C(r,2)xy+C(r,3)x^3` all
match, and `E4/Hhat = t(3t+1)/(6(2t+1)^3)`, `c=-y g_3 = c_t` exactly. Three
consequences, all uniform in `t`:

1. **`phi_1=phi_2=phi_3=0` is precisely `E1,E2,E3`.** The bridge's three
   vanishing conditions are the charged Jacobian rows at bands `4t+1, 3t+1, 2t`.
   They add nothing.
2. **`E4 = 4e * phi_4`, identically in `x,y,t`** (`e4_phi4_identity.py`: the
   difference simplifies to `0` over `Q(t)[x,y]`). The charged obstruction row is
   `4e` times the bridge's *free* (`4Z`) slot, and
   `phi_4 = t*Hhat_t(x,y)/(24(2t+1)^3)`, so `phi_4 = 0` in `A_t=Q[y]/(H_t)`
   automatically. The Jacobian is strictly stronger there than the tuple.
3. **The anchor nonvanishing holds.** On `x=1`,

```text
num(phi_5) = (-5t(2t+1)/2) H_t(y) + (-t(t+1)(10(2t+1)y-(3t+2))/2),
phi_5 = -t(t+1)(10(2t+1)y-(3t+2)) / (60(2t+1)^4)   in A_t,
Res_y(H_t, num phi_5) = 12 t^2 (t+1)^2 (2t+1)^4 (3t+2) (4t+1)  != 0  for all t>=1.
```

So `phi_5` is a **unit** in the separable rank-two algebra `A_t` for every
positive integer `t` (the resultant is nonzero on the split set `t=3s^2-1` as
well, so no zero divisor is silently inverted).

**PROVED-HERE (typed refutation).** On the graded face the tuple locus is a
*consequence* of the Jacobian locus together with a nonvanishing that the
Jacobian locus already satisfies. Therefore **no fixed-size collection of bridge
equations, added to any collection of chart bands, is uniformly inconsistent in
`t` at the graded level.** The charged hope for attack A ("the bridge equations
are not chart bands, so they may do what no fixed band collection can") is
**refuted**, not merely unproved. It also explains the charged exact point
`Q=h^q+B, P=h^e+2pi-gamma, c=-1`: there `x=0,y=1,g_1=g_2=0,g_3=2`, and the
bridge kills it at `[Ubar^2]`, i.e. at band `3t+1` -- the same moving band `E2`
already kills it at.

**Residual (typed).** This settles the graded/top-weight part exactly. The
non-graded bridge equations (exponents `s` with `4 not| s`, `4t+1<s<20t+5`, `s`
not a multiple of `4t+1`) are not proved to be implied; they are all at moving
indices and cannot be a fixed-size family, so they cannot repair the argument.
`OPEN[BRIDGE-SUBLEADING]`: whether they add anything to the charged chart at all.
Bounded quantity: at ray parameter `t`, `12t - 3` such exponents.

## 4. Attack A, part 2 (promoted): the uniform bridge normal form

**PROVED-HERE.** Because `etat^{-4}=Q^{1/q}` exactly, `sum_{k=0}^{e} a_k Q^{(e-k)/q}
= sum_k a_k etat^{-n+4k}` is *exactly* the part of `P`'s `etat`-expansion with
exponent `<= 0` (using the tuple vanishing for `j<=0<N`, and `a_0=1`). Let
`S := sum_{k=0}^{e} a_k Q^{(e-k)/q}` and `S_{>=0}` its truncation to
non-negative powers of `h`. A term `c h^i` with `deg_pi c < 4` has
`ord_etat >= -4i-3`, so every `h`-negative term has strictly positive
`etat`-exponent; hence `ord_etat(P - S_{>=0}) > 0`. But `P - S_{>=0}` is a
polynomial in `pi`, and a nonzero polynomial of `pi`-degree `d` has
`ord_etat = -d <= 0`. Therefore

```text
   P  =  [ sum_{k=0}^{e} a_k Q^{(e-k)/q} ]_{h-exponent >= 0},     a_0 = 1.        (BNF)
```

**PROVED-HERE.** `a_k = p_{-n+4k}` with `-n+4k <= 0 < m-1`, so Lemma 2.1 in the
reciprocal parameter (monomial form, charged `k16-ray-T-newton-sol56-v3:70-111`)
forces `a_k in k`: they are **scalars**, not polynomials in `gamma`. This is what
makes the count finite and is exactly Moh's `a_1,...,a_4` at `t=1`.

**PROVED-HERE (gauges).** `-n+4k = -m` at `k=t` and `=0` at `k=e`; so
`P -> P - a_t Q - a_e` kills `a_t, a_e`, and `Q -> Q - (q/e) a_{e-1}` kills
`a_{e-1}` (Moh's `f-(3/4)a_3` is `q/e=3/4` at `t=1`). These are precisely the
three charged gauges `alpha_t=0`, `const(alpha_e)=0`, `const(beta_q)=0`.

**DERIVED (uniform count).** Unknowns: `b_1..b_4` (4); the `beta_j` coordinates
`sum_{j=2}^{q} dim S_j = (t-1)+2t+3 = 3t+2`; the `a_k`, `k=1..e`, minus three
gauges, `3t-2`; plus `c`. Total

```text
   4 + (3t+2) + (3t-2) + 1 = 6t+5      (charged order chart: 9t+9).
```

At `t=1` this is `10 + c`, **numerically Moh's own p.209 count**.

**MEASURED (control).** `bridge_chart.py` builds `(Q,P)` by (BNF) with `h`-adic
Laurent arithmetic (coefficients reduced to `deg_pi<4` at every product) and
checks, for each `t` run, that `deg_pi P = n`, `deg_pi Q = m`, both monic, and
that **every `alpha_i` of the bridge-built `P` lands in the charged Theorem-1.2
space `S_i`**. That control passed at `t=1` and `t=2`; it is the required
witness that the bridge chart is a *subset* of the charged order chart, hence
still a necessary superset of the tuple locus.

**PROVED-HERE (source correction).** `moh_p209_control.py` compares (BNF) at
`t=1` with Moh's displayed formula. They differ by exactly

```text
   (2/3) a_2 beta_2 .
```

Moh writes `+ a_2 h^2` where the truncation of `a_2 f^{2/3} = a_2 h^2(1+u)^{2/3}`
to `h>=0` is `a_2(h^2 + (2/3) beta_2)`. The `f^{4/3}` part of his display,
including `(2/9)(beta_2^2+2gam)-(4/81)del`, reproduces exactly. The coefficient
**count (10) is unaffected**, but the displayed family is not the correct
necessary chart; the corrected one is used here.

## 5. Certificates on the bridge chart

**MEASURED.** Singular 4.3.2, over `Q`, degrevlex, generator order = chart
unknowns, then `c`, then a single Rabinowitsch variable `Tr`; main ideal
`I = <J(Q,P)-c*gamma coefficients, Tr*c-1>`; `option(redSB); std`.

| `t` | chart unknowns (incl `c`) | ring vars | generators | reduced SB | wall | max RSS |
|---:|---:|---:|---:|---|---:|---:|
| 1 | 11 | 12 | 24 | `[1]`, `G[1]=1` | 0.03 s | 11500 KiB |
| 2 | 17 | 18 | 59 | `[1]`, `G[1]=1` | 2.04 s | 16264 KiB |

Charged comparison at `t=2` (order chart): 27 unknowns, 38 generators,
**37.33 s**, 40060 KiB. The bridge chart is ~**18x faster** and needs 10 fewer
unknowns.

**MEASURED (non-result, retained).** `bridge_chart.py 3` (23 unknowns) was
launched and had not finished the symbolic `h`-adic build when this lane's time
bound expired; no `t=3` row is claimed. The bottleneck is sympy `expand` in the
binomial series, not the Groebner step, and is the first thing to replace before
attempting `t=5,6`.

**MEASURED (controls, both `t`).** In the identical declared ring:
`EMPTY <c, Tr*c-1> -> reduce(1,G)=0` **PASS**;
`NONEMPTY <c-1, Tr*c-1> -> reduce(1,G)!=0` **PASS**.

**PROVED-HERE (logical wrapper).** (BNF) is a *consequence* of the 4-tuple
condition plus Lemma 2.1, and the Jacobian equations are exact; so the bridge
chart is a necessary superset of the requested `(12t+4,8t+4;12t+1;3;J=c gamma)`
locus. A unit ideal after `c!=0` therefore proves (T) at that `t`. This
re-proves (T) at `t=1,2` independently of the charged order-chart runs, on a
different and strictly smaller chart. It proves nothing new at `t=3,4`, which
were already promoted.

Artifacts: `bridge_t1_fixed.sing` (8683 B, sha256
`a99b483a0776e36580f50d2ab66ba9bfa3c4a7a42090709c831e79519fd51488`),
`bridge_t2_fixed.sing` (211327 B, sha256
`6dd723bd5932c98fe17bccbe7db87518856546ae20347e8864c5cacf7b8467e7`).

## 6. Attack B (induction in `t`): what is and is not delivered

**DERIVED.** The whole graded face depends on `t` only through `r=e/q=(3t+1)/(2t+1)`,
which moves monotonically in `[4/3, 3/2)`. So the graded system is *the same
system* for all `t` with a moving parameter, and it is **consistent for every
`t`** (Section 3). Any induction in `t` must therefore act on the non-graded
middle, exactly the charged blocker; a specialisation or linear change of the
auxiliaries that carries the `t`-system into the `(t+1)`-system cannot be
detected on the graded face.

**DERIVED (a new uniform reformulation, offered for the next lane).** `S` is a
formal power series in `Q`, so `J(Q,S)=0`; with `P=S_{>=0}` this gives

```text
   J(Q,P) = -J(Q, S_{<0}),        ord_etat(S_{<0}) >= 1,
```

so the entire Jacobian system on the bridge chart is a condition on the
**discarded negative-`h` tail alone**. Combined with the chain rule of Lemma 2.1
in the `etat` parameter, `J(Q,W) = -m etat^{1-m} (dW/dgamma) (1+...)`, the system
becomes `p_j in k` for `0<j<m-1` and `p_{m-1}' = const * gamma`. This is a
`t`-indexed family with a *fixed* differential shape and is the most promising
handle I found; **not developed here** -- typed `OPEN[TAIL-INDUCTION]`.
Bounded quantity: `m-2 = 8t+2` tail coefficients.

**Not delivered:** no map sending the `t`-system into the `(t+1)`-system, and no
telescoping of the terminal `2t x t` systems. I did not read the parallel
`k16-middle-spine-sol56` lane and did not reconstruct its reductions.

## 7. Attack C: structural screens

**MEASURED (`ray_numeric_screens.py`, symbolic in `t`).** From Moh p.150's
definitions on the descended ray:

```text
d_1=12t+4, d_2=4, d_3=1;  n_1=3t+1, n_2=4;
q_1=-4(2t+1), q_2=5(4t+1)=M_2+m;
lam_1=-16(2t+1)(3t+1), lam_2=-4(24t^2-1);
mu_1=-4(2t+1), mu_2=1-24t^2;  th_1=0, th_2=-12t(2t+1);
E=n-1=3(4t+1)  (Lemma 2.1),  M_2=E-2<E.
```

By p.152 Prop. 2.2 this gives `deg_y T_1 = 4(2t+1)` and `deg_y T_2 = 24t^2-1`,
both positive integers for every `t>=1`, with `T_2` monic in `y` since `M_2<E`.
The Definition 5.1 window `V_3 d_2/d_3 = 4 >= V_2 = 3 > d_2/(n-M_2) = 4/3` holds
and the Definition 5.1(3) denominator `n-M_2-1=2` is nonzero, uniformly.
**No integrality, positivity, monicity or window screen from Moh's own
machinery bites on the ray at any `t`.**

**Typed non-applicability (Xu).** The charged Xu screen promotes Xu Cor. 5.3
(= Thm 4.7(ii) + Thm 5.1) **for a Jacobian pair monic in `y`**, i.e. `J = 1`.
The descended pair has `J = c*gamma`, a non-constant monomial. Applying Xu's
`IM >= Im` identities to it would violate the FALLACY-v2 pole/interior and
source-hypothesis checks. I therefore record **not applicable without a separate
monomial-Jacobian version of Thm 5.1**, not a kill and not a survival.

**Genus / Hurwitz.** Not attempted: the affine ramification count needs the
degree of `Q` on a generic fibre of `P`, which is exactly the intersection datum
the tuple encodes; deriving it independently is a lane of its own. Typed
`OPEN[RAY-GENUS]`.

## 8. Typed verdict and OPEN accounting

- **PROVED-HERE:** the reciprocal exponent dictionary (Section 2); that no
  bridge equation exists below `eta`-exponent `4t+1`; the graded identification
  `phi_{1,2,3} <-> E1,E2,E3` and `E4 = 4e phi_4`; `phi_4 = t H_t/(24(2t+1)^3)`
  and `phi_5` a unit in `A_t` with
  `Res_y(H_t, num phi_5) = 12t^2(t+1)^2(2t+1)^4(3t+2)(4t+1)`; the bridge normal
  form (BNF) and its gauges; the `6t+5` count; the `t=1` source correction
  `(2/3)a_2 beta_2` to Moh p.209.
- **MEASURED:** `SATURATED-EMPTY` on the bridge chart at `t=1` (12 vars, 24
  generators, `G[1]=1`, 0.03 s) and `t=2` (18 vars, 59 generators, `G[1]=1`,
  2.04 s), with both wrapper controls passing; the `S_i` containment control.
- **VERDICT on (T):** **not proved for all `t`.** Nothing here promotes a new
  `t`; `t=1,2` are re-proved on a different chart.
- **Attack A: CLOSED, negative for a uniform proof.** `OPEN[DESCENT-ANCHOR]` is
  narrowed: the bridge is now explicit and uniform in `t`, its dictionary is
  proved rather than assumed, and its content on the graded face is *implied by*
  the Jacobian. It cannot be the source of the missing uniform contradiction.
- **`OPEN[BRIDGE-SUBLEADING]`.** Whether the non-graded bridge equations add
  anything to the charged order chart. Bounded: `12t-3` exponents at parameter
  `t`. Cheapest test: at `t=2`, expand `Phi` to relative order 45 in the 17
  bridge unknowns and reduce the `4 not| s` coefficients against the Jacobian
  ideal.
- **`OPEN[TAIL-INDUCTION]`.** The `J(Q,P) = -J(Q,S_{<0})` reformulation of
  Section 6. Bounded: `8t+2` tail coefficients, fixed differential shape.
- **`OPEN[T-UNIFORM-MIDDLE]` stands.** It is now bounded by `6t+5` unknowns, not
  `9t+9`. **Cheapest next test:** `python3 bridge_chart.py 5` then `6`, and
  saturate; `t=2` cost 2.04 s against the charged 37.33 s, so `t=5,6` are the
  first genuinely new data points and are now plausibly in reach.

**FALLACY-v2 audit.** No screen is called attainment: Section 7 records "no
obstruction", never "a pair exists". The graded face is an initial-form
statement and is labelled as such; the non-graded remainder is left `OPEN` and
is not filled by analogy. `A_t` is treated as a separable rank-two algebra, not
a field: the `phi_5` resultant is exhibited and is nonzero on the split set
`t=3s^2-1` too, so no zero divisor is inverted. Saturation uses an explicit
Rabinowitsch generator in a declared ring with empty/nonempty controls, and the
`sat` result is the reduced standard basis of the stated ideal. Monic `h`-adic
division carries no parameter-dependent leader and every product is re-reduced.
Xu is declared not applicable on a source-hypothesis check rather than used.
Prime marks on descended data are labels. Moh's p.208 `c_5A+c_5B` and the p.209
omission are recorded as source defects, not silently adopted. No exit-price
assertion is made, so no `charge_basis` line is due.

## 9. Reproduction

```bash
python3 box/k16spine-opus-20260903/bridge_graded.py            # graded phi_k, H_t, resultant
python3 box/k16spine-opus-20260903/ray_numeric_screens.py      # Moh p.150/p.152 screens
python3 box/k16spine-opus-20260903/bridge_chart.py 1           # BNF chart, 11 unknowns
python3 box/k16spine-opus-20260903/moh_p209_control.py         # source control + correction
sed -E 's/\^([0-9]+)/^(\1)/g' box/k16spine-opus-20260903/bridge_t1.sing > /tmp/b1.sing
Singular -q /tmp/b1.sing
python3 box/k16spine-opus-20260903/e4_phi4_identity.py         # E4 = 4e*phi_4, general x
python3 box/k16spine-opus-20260903/bridge_chart.py 2           # 17 unknowns (several min)
sed -E 's/\^([0-9]+)/^(\1)/g' box/k16spine-opus-20260903/bridge_t2.sing > /tmp/b2.sing
Singular -q /tmp/b2.sing
```

The `sed` step only parenthesises integer exponents for Singular's parser; it
changes no coefficient. Page images: `box/k16spine-opus-20260903/moh-pages/`.

**MEASURED (retained non-results, for audit).** Two exploratory drivers are kept
in the same directory and contribute nothing to this report: `laurent_bridge.py`
(a direct `eta`-series attack, superseded by the `h`-adic method of Section 4 and
never run to completion) and `jac_tail_identity.py` (a numeric control for the
Section 6 tail identity, which exceeded its 120 s bound). The Section 6 identity
is typed `DERIVED` from `J(Q,Q^s)=0` and carries no measurement.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->`
  line, including its terminating newline; this seal is outside the body.
- Body bytes: `22163`.
- Body SHA-256:
  `a3ee8ca558fa04b3fd23851d609280dc04eaa35c9013e53e45dce5163a900c42`.
- Frozen basis: `3ab29f7a0d3c8aabed5961255fb144000c770248`.
