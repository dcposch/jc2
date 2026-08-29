# Hostile review: intrinsic exact-pair Newton--Puiseux L3/L4/L5

**Reviewer:** Opus 5 (`claude-opus-5`).  This is a **different-model hostile
review**: neither frozen packet was produced by this model, and no `PASS`
token, verdict, or conclusion of either Sol Ultra report is treated as
evidence below.  Everything asserted in Sections 2--4 is rederived here from
local normalization, tame Kummer base change, and the printed primary source.

**Date:** 2026-08-28
**Verdict:** **REPAIR**  (see Section 8 for the two load-bearing repairs and
Section 9 for the resulting ledger typing)

---

## 0. Custody: live hashes recomputed before use

```text
841c848eb98aa234fe6429006b3f84958c042869db395d61f2394a6c6c7c81d0
  xmodel/g2-intrinsic-exact-pair-l3-l5-newton-puiseux-sol-ultra-20260828.md      [MATCH]
5e8bc3c54007e9c471a8cb86b51929172c0b749156b1843c013c259d41ea70d9
  xmodel/g2-intrinsic-exact-pair-l5-reduced-denominator-independent-review-sol-ultra-20260828.md
                                                                                 [MATCH]
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf                                                           [MATCH]
```

All three equal the expected values given in the charge.

New artifacts written by this lane (nothing else was created or modified):

```text
26e24ec9667b2525efe20288db67aa8a7897038f8acb0f4f1a0549bb9d0f5154
  cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/verify.py
b78471a87da443f8fc7807d701ae3caa95e22a797ac09c9035a6aef526821256
  cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/README.md
```

`python3 -B cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/verify.py`
--> `RESULT: PASS   (all 264 checks passed)`, exit 0, 0.8 s, standard library
only.  Its design and its non-vacuity sabotages are described in Section 7.

Only text extraction was performed on the PDF (`pdftotext`, pages 8--16).
No CAS, no AWS, no heavy local computation.  `jc2-lean` was never entered,
listed, searched, read, built, statused, or modified.

## 1. Notation fixed for this review

`K` algebraically closed, `char K = 0`.  `h in K[x,y]` squarefree, `C = V(h)`
reduced, `C_i` its irreducible components, `Cbar^nu` the disjoint union of the
normalizations of the projective closures.  Put `u = 1/x`, `F = K((u))`, and

```text
B_x = { S in Cbar^nu \ C^nu : ord_S(x) < 0 and ord_S(y) >= 0 },
e_S = ord_S(u) > 0,
```

and symmetrically `B_y`.  Fix `kappa` with `e_S | kappa` for all `S in B_x`,
substitute `u = t^kappa`, and set

```text
L_x(kappa) = { phi in K[[t]] : h(t^-kappa, phi) = 0 }.
```

`mu_kappa` acts by `(zeta . phi)(t) = phi(zeta t)`; the equation
`h(t^-kappa, y)` is `mu_kappa`-invariant, so `L_x(kappa)` is stable and deck
conjugates of a root are automatically among the roots.

## 2. The three numerical assertions, reproved

### 2.1 The plane coordinate `y` generates the completed local factor

This is the load-bearing step, and it is the step Sol report 1 asserts with
only a gesture ("its displayed root `y` generates that factor").  It is true,
and here is the proof.

`C_i` is a plane affine curve, so `K(C_i) = Frac(K[x,y]/(h_i)) = K(x)(y)`:
`y` is a **global** primitive element for `K(C_i)/K(x)` whenever `x` is
nonconstant on `C_i`, i.e. whenever `C_i` is nonvertical.  Let `m_i in K(x)[Y]`
be its minimal polynomial.  Base changing along `K(x) = K(u) --> F = K((u))`
and using separability (char 0),

```text
K(C_i) (x) _{K(x)} F  =  F[Y]/(m_i)  =  prod_{T | u=0} F[Y]/(m_{i,T})
                                     =  prod_{T | u=0} K((z_T)),
```

where `m_i = prod_T m_{i,T}` is the factorization into `F`-irreducibles and
`Y` maps to the local expansion `phi_T(z_T)` in the `T`-factor.  The `T`-factor
is `F[Y]/(m_{i,T})`, generated over `F` by the image of `Y`.  Hence

```text
F(phi_T) = K((z_T))   for every T,
```

i.e. **a global primitive element is automatically a local primitive element
at every place**.  This is exactly why "the actual plane coordinate `y`"
matters: an arbitrary function on the branch would only generate a subfield.

`K` algebraically closed gives residue degree one, so
`[K((z_S)) : F] = e_S`.  Tame Kummer normalization: `u = z^{e_S} v(z)` with
`v(0) != 0`, and in char 0 the unit `v` has an `e_S`-th root, so a uniformizer
may be chosen with `u = z^{e_S}` exactly.  Write

```text
y = phi_S(z) = sum_{n >= 0} b_n z^n,    d = gcd(e_S, {n : b_n != 0}).
```

If `d > 1` then `phi_S in K((z^d))`, the fixed field of `mu_d <= Gal(K((z))/F)`,
so `F(phi_S) subsetneq K((z_S))` — contradiction.  Therefore `d = 1`: the
Puiseux denominator of `y = sum b_n u^{n/e_S}` is **exactly** `e_S`, not merely
a divisor of it.

**Constant-series edge case.**  `y` is constant on the branch iff `y - b_0 = 0`
in `K((z_S))`, iff `y - b_0 = 0` in `K(C_i)` (a nonzero element of `K(C_i)` has
finite order at `S`), iff `C_i` is the horizontal line `y = b_0`.  Then
`K(C_i) = K(x)`, `C_i^nu = P^1_x`, and the unique place over `x = infinity` has
`e_S = 1`.  So **a constant series forces `e_S = 1`; this is a conclusion of the
theorem, not a case that has to be excluded**.  Checker: `C6 (y-3)` with both
`kappa = 1` and the oversized `kappa = 6`, and `C7 (y)` with `kappa = 4`.

**Horizontal lines** are therefore in scope with `e_S = 1` and support `{0}`
or empty.  **Vertical components** `x = c` have `x` constant, so no place has
`ord_S(x) < 0`: they are absent from `B_x` by definition, not by an argument,
and their boundary place `(x,y) = (c, infinity)` is recovered in `B_y`.  In the
`x`-chart the factor `(t^-kappa - c)` is a unit of `K((t))[y]` and contributes
no root.  Checker: `C11 = (x-5)(xy-1)`.

### 2.2 Orbit `e_S`, stabilizer `kappa/e_S`

Write `kappa = e_S q`.  Over `u = 0`,

```text
K[[z]] (x)_{K[[u]]} K[[t]] = K[[z,t]] / (z^{e_S} - t^{e_S q})
                           = prod_{xi in mu_{e_S}} K[[t]],   z = xi t^q,
```

so there are **exactly `e_S` points above `S`** on the base-changed normalized
curve — independently of how oversized `kappa` is — and `t` is a uniformizer at
each.  The presentations are `phi_xi(t) = sum_n b_n xi^n t^{qn}`, and
`zeta . phi_xi = phi_{xi zeta^q}`.  The map `mu_kappa --> mu_{e_S}`,
`zeta |-> zeta^q`, is onto with kernel `mu_q`, so the action is transitive:
orbit size `e_S`, stabilizer size `q = kappa/e_S`.

In displayed-support form (this is the form an implementation uses):

```text
g = gcd(kappa, supp phi),   convention gcd(kappa, {}) = gcd(kappa, 0) = kappa,
Stab(phi) = mu_g,   |Stab| = g,   |Orb| = kappa/g,
K((u))(phi) = K((t))^{mu_g} = K((t^g)),  of degree kappa/g over K((u)).
```

The exponent `0` imposes no condition (`zeta^0 = 1`), and `gcd(kappa,0) = kappa`
absorbs it, so the zero/constant-support convention is not a patch: it is the
correct value of the same formula.  Combined with 2.1, `kappa/g = e_S`.

**Oversized covers are handled, and are not exotic.**  A common `kappa` must be
a common multiple, so within a single run it is oversized at every place whose
`e_S` is smaller than the maximum.  Checker instances, all confirmed:

| curve | `kappa` | root | support | `g` | `|Orb|` | geometric `e_S` |
|---|---|---|---|---|---|---|
| `x y^2 - 1` | 2 | `t` | `{1}` | 1 | 2 | 2 |
| `x y^2 - 1` | 4 | `t^2` | `{2}` | 2 | 2 | 2 |
| `x y^2 - 1` | 6 | `t^3` | `{3}` | 3 | 2 | 2 |
| `x y^3 - 1` | 6 | `t^2` | `{2}` | 2 | 3 | 3 |
| `x^5 y^2 - (x^2+1)^2` | 2 | `t + t^5` | `{1,5}` | 1 | 2 | 2 |
| `x^5 y^2 - (x^2+1)^2` | 4 | `t^2 + t^10` | `{2,10}` | 2 | 2 | 2 |
| `y - 3` | 6 | `3` | `{0}` | 6 | 1 | 1 |
| `y` | 4 | `0` | `{}` | 4 | 1 | 1 |
| `(y^2-x)(xy-1)` | 2 | `t^2` | `{2}` | 2 | 1 | 1 |

The last row is the "oversized for this place, tight for the run" case: the
common `kappa = 2` is forced by the escaping component `y^2 = x`, not by the
place being described.  Every geometric `e_S` in the table is read off from an
independently certified birational parametrization, not from the orbit.

Part A of the checker sweeps this exhaustively: `kappa = 1..12` against all
`2^12` supports in `{0,...,11}`, comparing the brute-force stabilizer against
`gcd(kappa, gcd(S))` and the orbit against `kappa/g`, with no failure and with
`|Orb| != kappa` recorded on the overwhelming majority — the standing
refutation of "reduced denominator = ambient index".

### 2.3 No collision across places or components; the bijection

*Injectivity within a component.*  Distinct places `T != T'` over `u = 0`
correspond to distinct `F`-irreducible factors `m_{i,T}`, `m_{i,T'}` of the
separable `m_i`; coprime irreducibles share no root, so no series presents two
places of one component.

*Injectivity across components.*  For coprime `h_i, h_j` of positive
`y`-degree there are `A, B` and `0 != R(x) in K[x]` with `A h_i + B h_j = R(x)`
(the `y`-resultant).  A common root `phi` would force `R(t^-kappa) = 0`, but
`R(t^-kappa)` is a nonzero Laurent polynomial.  Components with `y`-degree 0
are the vertical ones and have no root in this chart at all.

*Deck-invariance.*  The projection of the base change to `Cbar^nu` is
`mu_kappa`-equivariant with trivial action on the target, so an orbit lies in
one fibre; 2.2 gives transitivity on that fibre.  Orbits therefore neither
split a place nor merge two.

*Surjectivity.*  Any `phi in L_x(kappa)` gives `K[x,y]/(h) --> K((t))`,
`x |-> t^-kappa`, `y |-> phi`; the kernel is prime and contains some `h_i`,
and cannot be larger since `x` is not sent to a constant, so `K(C_i)` embeds
over `K(u)`.  Then `ord_t` restricts to a valuation with `ord_t(u) = kappa > 0`
and `ord(y) >= 0`, i.e. a place `S in B_x`, and

```text
ord_t |_{K(C_i)} = (kappa / e_S) . ord_S.                                (2.3.1)
```

Hence `L_x(kappa)/mu_kappa <--> B_x` is a bijection.  Checker: the reducible
`(y-3)(x y^2 - 1)` (two components, `e_S = 1` and `2`), the vertical-component
`(x-5)(xy-1)`, and the escaping `(y^2-x)(xy-1)`; in every instance the number
of deck orbits equals the number of certified places, orbit sizes equal the
geometric ramification indices, and distinct orbits are disjoint.

*(2.3.1) is a typing trap worth recording:* a raw `t`-order on the cover is
`kappa/e_S` times the place order.  Sigray's own `d_{h,F} := j/kappa`
(Notation 3.10, p. 13) is already the intrinsic `x`-degree, so the source is
safe, but Sol report 1 §4.1's "substituting `g` in a leaf field gives its
pole/finite tag" is only **sign**-safe; any *order* extracted this way must be
divided by `kappa/e_S`.  Checker mutation `M8`.

## 3. What Sigray Proposition 3.1 actually counts

Verified page map (PDF page = printed page, offset 0, confirmed page by page):

| item | page |
|---|---|
| Lemma 2.1 (statement + proof) | 8 |
| **Statement 3.1**, Definition 3.1, Definition 3.2 | **10** |
| Definition 3.3, Notation 3.1--3.2, Statement 3.2--3.3 | 11 |
| Notation 3.3--3.6, Statement 3.4, **Notation 3.7**, Notation 3.8 | 12 |
| Statement 3.5--3.7, **Notation 3.9**, **Notation 3.10**, Notation 3.11 | 13 |
| Statement 3.8, Notation 3.12, **Proposition 3.1 (statement)** | **14** |
| **Proof of Proposition 3.1**, **Statement 3.9 (statement + proof)** | **15** |

**It counts base-changed presentations.**  Its own proof (p. 15) says so
verbatim: "Let `R*` be the smooth closure of the finite set of Riemann surfaces
of the fiber `h(t^kappa, y) = 0` ... `deg(p_d) = #{P in R* : x(P) = infinity and
eta_n(P) in C}`".  `R*` is the compactified **base-changed** curve, whose points
over `x = infinity` are the `e_S` conjugates per original place.  Both Sol
reports read this correctly, and the Kummer quotient of Section 2 is genuinely
additional, not a restatement.

I rederived `(*)` and `(**)` without using the source proof.  Write
`H(t,y) = h(t^-kappa, y) = A(t) . prod_i (y - r_i(t))` over the algebraic
closure of `K((t))`, and

```text
eta_n = t^-n ( y - sum_{j<n} c_j t^j ),   h_n(t, eta) = sum_j t^-j p_j(eta),
```

so `p_d` is the coefficient at the **minimal** `t`-exponent, i.e. the initial
`t`-form.  Under `y = prefix + t^n eta`, roots `r_i` become
`rho_i = t^-n (r_i - prefix)`; the initial form is
`A_0 . prod_{ord rho_i >= 0} (eta - rho_i(0))`, because factors with
`ord rho_i < 0` contribute only `t`-powers to leading order.  Hence

```text
deg p_d          = #{ complete roots agreeing with the prefix below n },
mult(p_d, c_n)   = #{ complete roots agreeing with the prefix through c_n },
```

which is `(*)`/`(**)`.  Statement 3.9(i) `mult(p_{h,F},c) = deg(p_{h,F*c})` is
these two at consecutive levels, and 3.9(iii)
`d_{h,F*c} = d_{h,F} - mult(p_{h,F},c)/kappa` is the same identity read on the
minimal `t`-exponent.  Both were checked at **every node** of the all-root
recursion on all 15 curve/`kappa` instances.

**Where squarefreeness enters.**  The initial-form count is a count of roots
*with multiplicity*.  `h` squarefree means `h = prod h_i` with distinct
irreducibles, each separable in `y` over `K(x)` (char 0, positive `y`-degree),
so multiplicities are 1 and the count is the honest number of distinct series.
Mutation `M4`: for `(x y^2 - 1)^2`, `deg p_d = 4` while there are only 2
distinct series; the squarefree control gives `deg p_d = 2`.

For a Keller pair this hypothesis is free, and Sol report 1's derivation is
correct: `df ^ dg` a nonzero constant makes `df` nowhere zero, and if
`f - a = p^2 q` with `p` nonconstant then `grad(f-a) = p(2q grad p + p grad q)`
vanishes on the nonempty `V(p)`.  So every fibre is squarefree (and smooth,
though possibly reducible/disconnected).

**Strict truncation.**  At a node the accumulated sum is by construction the
truncation of every leaf in the cluster, and *every* root of `p_d` is realized
by a leaf, since `p_d = A_0 prod (eta - rho_i(0))` runs exactly over the cluster.
So all-root recursion neither skips nor invents a branch.  **Zero residual roots
are ordinary roots** and must be retained; Notation 3.12 (p. 14) already defines
`mult(p, 0)` correctly.  Mutation `M3`: dropping `c = 0` on `(y-3)(x y^2 - 1)`
retains 1 of the 3 leaves.

**Escaping branches.**  Roots with `ord_t < 0` (the `y = infinity` branches) are
excluded exactly by the initial-form degree, not by any separate rule.
Mutation `M5`: for `(y^2 - x)(xy - 1)` with `kappa = 2`, `deg_y h = 3` but
`deg p_d = 1`.

## 4. Three unrecorded source-level findings

**S1.  Statement 3.1 (p. 10) is asserted with no proof, and occurs exactly
once in the entire 67-page paper.**  I grepped every page: the string
`Statement 3.1` appears only at its own statement.  It is nevertheless the sole
source citation for both-chart coverage (L4).  It *is* provable, from
Lemma 2.1(i) (p. 8): `N_f` lies in the rectangle with vertices
`(0,0),(0,l_f),(k_f,l_f),(k_f,0)` and the corner monomial `x^{k_f} y^{l_f}`
occurs in `f` with `k_f, l_f > 0`.  Suppose a place `S` had
`ord_S(x) = -p < 0` **and** `ord_S(y) = -q < 0`.  For any other `(i,j) in N_f`,
`i <= k_f`, `j <= l_f` with strict inequality somewhere, so
`pi + qj < p k_f + q l_f`; the corner is therefore the **strict** minimum of
`ord_S` among all monomials of `f`, and it is `< 0 = ord_S(a)`.  Hence
`ord_S(f - a) = -(p k_f + q l_f) < 0`, contradicting `f - a = 0` on the fibre.
So no boundary place has both coordinates infinite; a place with both finite is
affine; "exactly one" follows.

The consequence for typing is sharp: **coverage is conditional on the
normalized rectangle/NE-corner hypothesis and is FALSE for general squarefree
`h`.**  For `h = y - x^2` the single boundary place has `x = y = infinity` and
lies in neither `B_x` nor `B_y`.

**S2.  Definition 3.1's termination clause is the reduced-denominator claim,
and is also unproved in the source.**  With `kappa` the multiplicity of `x` at
`P`, Definition 3.1 (p. 10) sets `e_0 = kappa`,
`beta_i = min{ j : c_j != 0, e_{i-1} does not divide j }`,
`e_i = gcd(e_{i-1}, beta_i)`, and asserts "After finitely many steps we obtain
`e_m = 1`".  That is exactly `gcd(kappa, {j : c_j != 0}) = 1`.  So Section 2.1
above is not a decorative strengthening of the source: it supplies a
load-bearing step the source only asserts, and the entire Eggers--Wall
decoration layer that reads `nu_F` and `kappa_F` off the characteristics
(Notations 3.4--3.5, p. 12) inherits it.

**S3.  The proof of Proposition 3.1 uses the same unproved fact.**  Its
"one-to-one correspondence between the set of Puiseux series ... and the set
`{P in R* : x(P) = infinity and y(P) in C}`" is a bijection only because
distinct points of `R*` over one `S` give **distinct** series — which is
`gcd(e_S, supp) = 1`.  Without it the map is `e_S`-to-`(e_S/d)` and `deg p_d`
would count points rather than series.

*Two printed typos, for the pin record (no downstream damage; both Sol reports
already use the corrected forms).*  On p. 14 the displayed
`eta_n := x^{n/kappa}(y - sum_{j=0}^{n-1} c_j x^{-j})` disagrees with `(*)`/`(**)`
on the same page, which use `c_j x^{-j/kappa}`; the latter is correct (and
matches Notation 3.9, p. 13, where `j` ranges over `Q`).  On p. 15 the proof's
"the set of Puiseux series in the form (4)" must read "in the form (3)", since
the set it is matched to is `{x(P) = infinity, y(P) in C}`.

*Citation drift.*  Sol report 1 §3 pins "Proposition 3.1 and proof, PDF
pp. 13--14"; it is pp. 14--15.  "Statement 3.9, PDF pp. 14--15" is loose:
Statement 3.9 and its proof are entirely on p. 15.  Its other two pins are
correct.

## 5. The finite terminal replacement: audit and repair

The charge asks whether "an exact local factor plus a prefix longer than every
pairwise contact (including deck conjugates)" is **sufficient and necessary**.

**Sufficient: yes, and I prove the part that is not obvious.**  Let `R` be the
set of complete roots and let the prefix `F` at level `N` satisfy
`N > ord_t(phi - psi)` for the recorded `phi` and every `psi in R \ {phi}`.
`R` is `mu_kappa`-stable, so deck conjugates are automatically among the `psi`
and the parenthetical is redundant.  Then:

* `F` determines `phi` uniquely, hence its orbit, hence its place;
* the support gcd is already final.  Suppose
  `g' = gcd(kappa, supp F) > g = gcd(kappa, supp phi)`.  Then `Stab(F) = mu_{g'}`
  strictly contains `Stab(phi) = mu_g`, so some `zeta` fixes `F` but not `phi`;
  `zeta.phi != phi` lies in `R` and agrees with `phi` below `N`, contradicting
  the separation.  Hence `e_S = kappa/gcd(kappa, supp F)` may be read off the
  **truncation**.

**Necessary: not as stated, in two different directions, and the phrasing is
also not effectively certifiable.**

1. A *global* `N` exceeding *every* pairwise contact in `R` is stronger than
   needed; the sharp condition is per-record separation.  Sol report 2 states
   both forms (§1 and §7 per-record, §5 global); the global one is only an
   upper bound.
2. Separation from deck conjugates is necessary for the **ramification**
   reading but **not** for **place identity**: a cluster that happens to be a
   full deck orbit already names one place.  Concretely, for `x y^2 - 1` with
   `kappa = 2` the empty prefix has `deg p_d = 2` and already determines the
   unique place, but its support gcd is `2`, giving `e = 1` instead of `2`.
   Sol report 2 §1's blanket "an arbitrary finite prefix ... is not in the
   domain of the leaf/place bijection" is therefore right about the record type
   but over-general about the reason; the reason is ramification, not identity.
3. "`N` exceeds every contact with every other complete root" is not a
   predicate a node can evaluate: the other complete roots are exactly what has
   not been computed yet.  And "the exact local factor" is undefined — a factor
   over `K((u))` already names the place with **no** prefix at all (its degree
   *is* `e_S`), whereas a factor over `K((t))` does not.

**Hensel / Laurent ambiguity: real, and located.**  `h(t^-kappa, y)` has
Laurent coefficients, so `K[[t]]`-Hensel does **not** apply to it.  One must
first shift and clear: `t^{d} h_F(t^-kappa, eta) in K[t][eta]`, whose value at
`t = 0` is precisely the residual polynomial `p_{h,F}`.  Then `deg p_{h,F} = 1`
means a **simple** root of the initial form, and Hensel lifts it uniquely.
Applying Hensel to `h` unshifted, or forgetting the clearing, is exactly how
the escaping `ord_t < 0` branches get mis-handled — those are excluded by the
initial-form degree, never by Hensel.

**Smallest exact repair.**  Define a leaf/place record as

```text
    ( h , chart , kappa , strict truncation F at level N )
    carrying the certificate      deg p_{h,F} = 1
```

with `p_{h,F}` Sigray's residual polynomial (Notation 3.10, p. 13).  This is
minimal and complete:

* by Proposition 3.1(*), `deg p_{h,F} = 1` **is** "exactly one complete root
  extends `F`", i.e. it *is* the separation condition, expressed in data the
  node has already produced;
* it is Statement 3.9(i) read at the parent: `mult(p_{h,F^0}, c) = 1`;
* it licenses `e_S = kappa/gcd(kappa, supp F)` by the argument above;
* it licenses unique Hensel continuation on the shifted cleared equation, so no
  separate "exact local factor" object is needed — `h` plus the node data is
  the factor;
* it is effective and self-certifying, whereas "longer than every contact" is
  neither.

Checker `terminal_audit` computes, for every certified root of every test
curve, the minimal `N` at which `deg p = 1`, and verifies both that it exceeds
every contact and that the truncated support gcd equals the full one.  Sample:
`(xy-1)(x^3 y - x^2 - 1)` has contact 3 and terminal `N = 4` (mutation `M6`:
`deg p = 2` at `N = 3`, `deg p = 1` at `N = 4`); `x^5 y^2 - (x^2+1)^2` at the
oversized `kappa = 4` has conjugate contact 2 and terminal `N = 3`, where the
truncation `t^2` gives `gcd(4,{2}) = 2` and `e_S = 2`, while `N = 2` would give
`gcd(4,{}) = 4` and the wrong `e_S = 1`.  Mutation `M7` records 18 such
premature-gcd failures across the suite.

## 6. Counterexample hunt: what I tried and what happened

| attack | outcome |
|---|---|
| oversized Kummer cover, `kappa` a large multiple of `e_S` | no counterexample; orbit stays `e_S`, stabilizer `kappa/e_S`.  Checked at `kappa/e_S = 1,2,3` |
| nontrivial support gcd `> 1` | occurs exactly when the cover is oversized, and equals `kappa/e_S`.  `x^5y^2-(x^2+1)^2` at `kappa=4`: support `{2,10}`, gcd 2 |
| nonprimitive coordinate function | impossible **for a plane coordinate**: `K(C_i) = K(x)(y)` forces `y` primitive, and completion preserves it (§2.1).  The apparent counterexample `u = z^2, y = z^2` is the non-normalized 2:1 reparametrization of `xy = 1`, whose true place has `e_S = 1` |
| constant / zero series with `e_S >= 2` | impossible: a constant series forces `C_i` horizontal and `e_S = 1` |
| horizontal line | in `B_x`, `e_S = 1`, support `{0}`; correct under the `gcd(kappa,0) = kappa` convention even at `kappa = 6` |
| vertical component | excluded from `B_x` by definition; recovered in `B_y`; its factor is a unit in `K((t))[y]` |
| reducible squarefree curve | componentwise; cross-component collision refuted by the `y`-resultant |
| premature common prefix | real hazard, not a counterexample to the theorem: `(xy-1)(x^N y - x^{N-1} - 1)` has contact `N` and needs `N+1` coefficients |
| chart overlap / double counting | `B_x cap B_y = {}` **definitionally** (`ord_S(x) < 0` vs `>= 0`), unconditionally |
| chart under-coverage | **succeeds for general `h`**: `y - x^2` has a boundary place in neither chart.  Coverage needs the normalized rectangle (S1) |

Two of these are the frozen packets' own controls and I confirmed both
independently: `Y^2 - u` embedded by `u = t^4` (Sol report 2 §6.1) is my `C1`
at `kappa = 4`, orbit 2 / stabilizer 2 / reduced denominator 2, so
"reduced denominator = ambient index" is false; and
`(xy-1)(x^N y - x^{N-1} - 1)` (§6.2) is my `C5` at `N = 3`.  Sol report 2's
own artifact `cases/g2_intrinsic_exact_pair_l5_reduced_denominator_20260828/verify.py`
runs and prints `"status": "PASS"` with `8190` support sets, matching its §9;
inspecting it, it is honestly scoped — pure `Z/kappa` arithmetic plus two
*declarative* controls.  It never runs a Newton--Puiseux recursion, never
touches a curve, and cannot detect any of the curve-level hazards above.  That
is why the checker in Section 7 exists.

## 7. This lane's checker

`cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/verify.py`, pure
standard library, exact over `F_2521` (`p - 1 = 2520 = lcm(1..10)`), 0.8 s.

Independence is arranged so that no claim is checked against itself.  Each
curve test carries two objects built without any residual polynomial:

1. a **certified complete root set** — the exact Laurent identity
   `A(t) . prod_i (y - r_i(t)) == h(t^-kappa, y)`, pinning the full root
   multiset including escaping branches;
2. a **certified place list** — an explicit `s |-> (x(s), y(s))` with
   `h(x(s),y(s)) == 0` exactly *and* a birationality certificate
   `s == Num(x,y)/Den(x,y)` verified by composing back, so that
   `e_S = -ord_s(x(s))` is geometric.

Sigray's all-root recursion is a third engine, compared against both.

Result: `RESULT: PASS (all 264 checks passed)`, exit 0.  Mutations `M2`--`M8`
(Section 3, 5 and 2.3) all fire.  Because a green checker proves nothing on its
own, I additionally sabotaged it five ways out of band — corrupted certified
root, wrong `e_S` parametrization, residual extractor reading the maximal
instead of minimal `t`-exponent, `orbit == stabilizer`, trivial deck action —
and each is caught (6, 2, 47, 1 and 52 failing checks respectively).

The checker settles **finite instances only**.  Sections 2--5 are the
theorem-level argument and do not depend on it.

## 8. Verdict and the exact repairs

The mathematics of both frozen packets is **correct**.  I found no
counterexample and no false formula.  The verdict is `REPAIR` because two
statements are load-bearing for the ledger and are, as written, respectively
non-certifiable and unqualified.

**R1 — typing of the finite terminal record (replaces Sol report 2 §7's
repair, which is itself a correct repair of Sol report 1 §2.3).**
Replace "exact local factor plus a prefix cutoff `N` exceeding every contact
with every other complete root" by

> a leaf/place record is `(h, chart, kappa, strict truncation F at level N)`
> carrying the certificate `deg p_{h,F} = 1` (equivalently
> `mult(p_{h,F^0}, c) = 1`, Sigray Statement 3.9(i), p. 15).  It then holds
> that `F` names a unique complete root, a unique deck orbit and a unique
> normalized place, that `e_S = kappa / gcd(kappa, supp F)` with
> `gcd(kappa, {}) = kappa`, and that the continuation is the unique Hensel lift
> of the simple root of `p_{h,F}` **on the shifted, `t`-cleared equation**
> `t^{d} h_F(t^-kappa, eta) in K[t][eta]`.

Rationale: the frozen condition is sufficient but not evaluable at the node
(it quantifies over roots not yet computed), and "exact local factor" is
ambiguous between a `K((u))`-factor, which needs no prefix at all, and a
`K((t))`-factor, which is insufficient.  Additionally, "separation is
necessary" holds for the ramification reading but not for place identity, so
the §1 sentence should be narrowed to the ramification reading.

**R2 — chart disjointness is unconditional; chart coverage is not.**
Sol report 2 §4 derives disjointness from Statement 3.1; disjointness is in
fact definitional (`ord_S(x) < 0` versus `>= 0`) and holds for every reduced
plane curve.  What Statement 3.1 supplies is **coverage**, and only for a
normalized counterexample fibre.  Since Sol report 2 §1 states its theorem for
an arbitrary reduced plane curve and its §8 ledger line, and Sol report 1's §0
ledger block, carry no hypothesis, relabel both as

> `L4-exact` both intrinsic charts cover all boundary places — AVAILABLE **for
> a normalized (Lemma 2.1 rectangle / NE-corner) fibre**; FALSE in general, as
> `y - x^2` has a boundary place with `x = y = infinity`, in neither chart.

and attach the Lemma 2.1 valuation proof of S1, since Statement 3.1 (p. 10)
carries no proof in the source and is cited nowhere else in it.

**R3 — precision, non-blocking.**  Record `ord_t = (kappa/e_S) . ord_S` beside
Sol report 1 §4.1: the `g`-substitution tag is sign-safe as written, but any
*order* read on the cover must be divided by `kappa/e_S`.

**R4 — pins, non-blocking.**  Correct Sol report 1 §3 to "Proposition 3.1,
statement p. 14, proof p. 15" and "Statement 3.9, p. 15", and record the two
printed typos noted in Section 4.

Nothing in Sections 2--5 requires any formula in either packet to change.

## 9. Ledger effect

With R1 and R2 applied, for the **intrinsic exact-pair two-chart constructor
only**:

```text
L3-exact  all-root prefixes are actual fibre truncations         AVAILABLE
L4-exact  both intrinsic charts cover all boundary places        AVAILABLE
          (hypothesis: normalized rectangle/NE-corner fibre)
L5-exact  terminal deck orbits biject normalized places          AVAILABLE
          (record typed as in R1)
```

Exact-pair leaves carrying the R1 certificate may be deduplicated in place
budgets; a node without that certificate is an ancestor cluster and must not
enter a refutation-grade place sum.

## 10. Hybrid firewall

Explicitly, and this review adds nothing to any of it:

```text
L3-hybrid  VGG/GGV selected translations equal fibre truncations   OPEN (H-TRUNC)
L4-hybrid  VGG/GGV source leaves cover both charts                 OPEN
L5-hybrid  an uncertified source leaf is a terminal place          OPEN / ILL-TYPED
```

No result above identifies any selected VGG/GGV translation corridor with an
intrinsic prefix, shows that such a corridor is a strict truncation of an
actual fibre branch, or shows that it is source- or place-complete.  In
particular nothing here revives `C74-PLACE`, transpose coverage, VGG minimal
re-selection, or the common `P/Q` face-root identification.  A hybrid client
that reads `L3/L5 available` off Section 9 without carrying the `deg p = 1`
certificate of R1 and an independent proof of `H-TRUNC` would be committing
exactly the error the firewall exists to prevent.

Nothing here proves repaired Sigray ancestor decorations, Proposition 4.2's
constant-leading-part existence, a landing theorem, bounded delay, `RPMC(C)`,
a type bound, a cofinal total-degree ceiling, a Keller contradiction, or JC2.

## 11. Custody statement

Files written by this lane: this report and the two files under
`cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/`.  Neither frozen
target, no canonical or top-level campaign file, and no other existing
artifact was edited; the dirty shared worktree is preserved.  `jc2-lean` was
not entered, listed, searched, read, built, statused, or modified.  No AWS and
no heavy local CAS was used.

---

**VERDICT: REPAIR**
