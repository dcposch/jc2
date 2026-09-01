# SHAPE-3-FINISH: the non-constant (4,3)-scaled stratum

Lane: OPEN[SHAPE-3-ALL-g], family 3, `(d,n) = (4g,3g)`, outer coprime `(4,3)`,
non-constant stratum. Model: Opus 5. Date: 2026-09-01.

## 0. Input verification and scope

The three frozen inputs were hashed with `shasum -a 256` before any mathematical use.
All three matched the charge manifest exactly:

```text
189bc45d83c97df3614c65450a8c6e926938e50f7ccc0b2bacd78a7fd8d11c4d  shape-kill-uniform-opus5-20260901.md
0213fcae67bbde4d426a50f2d5d17c71db907d78718860459f14ff50e2ce4a01  shape-kill-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Below, **SK**, **REV** and **Coord** denote those three in charge order. No CAS was run,
no canonical ledger or charged file was edited, and `jc2-lean` was not inspected. One
primary source was fetched and hashed (§7); its hash reproduces the custody hash already
recorded by REV. Besides the charged inputs I read only `pi1-s4-decision-opus5-20260831.md`
for the exact text of Theorem A, cited by path and line. All reasoning below is desk-scale:
finite local power-series expansions in two variables and degree counts on `P^1`. No new
exit price is asserted, so FALLACY-v2 requires no `charge_basis` line.

**Headline.** The charged Route 1 is right in its target and wrong in its instrument. The
extended projective cover *does exist* — contradicting the explicit claim in SK §4.2 and
REV §3.2 that "there is no triple cover of `P^2` to apply it to" — but the charged parity
horn (branch degree `4g+1`, odd) is **REFUTED**: the divisor that carries the Miranda class
is the *weighted* branch divisor `Dbar + 2 L_inf` of degree `4g + 2`, which is even. The
working instrument is a different, sharper one: a **total-branch congruence** forced by the
fact that `L_inf` is a rational curve of total (index 3) ramification. It yields, at every
`g`, an exact integer identity `3*lambda = 2g + 1 + m` with `0 <= m <= 2g`, where `m` is a
single local defect at the single point `P_inf`. When `m = 0` — equivalently, when the
resolvent cover is Gorenstein over `P_inf` — the family collapses to `g = 1 (mod 3)`,
deleting `(8,6)`, `(12,9)`, `(20,15)`, `(24,18)`, ... At `g = 2` I prove `m <= 3` is
impossible, so the `(8,6)` non-constant row is pinned to the single extremal value
`m = 2g = 4`. Route 2 is structurally vacuous at `(4,3)` — the Theorem A order fork is
*entered*, not exited — but the congruence sharpens Theorem A(3) itself. The verdict is
typed in §5: not a uniform kill, but a residual reduced from a family to one integer.

## 1. The row as inherited: what SK-5 pins and what it leaves

Notation is SK §1. `D` is an escaping `N = 4` residual branch curve with birational
polynomial parametrisation `gamma(t) = (p(t), q(t))`, `d = deg p > n = deg q`,
`g = gcd(d,n) >= 2`, and here `(d',n') = (4,3)`, so `d = 4g`, `n = 3g`, `a = d - n = g`.
`phi : pi_1(A^2 - D) ->> S_4` sends every meridian of `D` to a transposition.
`Dbar` is the projective closure, irreducible of degree `d = 4g`
(`row-nf-exhaustiveness-hostile-review-sol56-20260901.md:55-60`, confirmed at REV §1.2(ii)),
with a single place at `P_inf = [1:0:0]` on the line at infinity `L_inf`.

Two promoted facts fix the boundary datum.

* **`Pi` is the image of the meridian of `L_inf`.** In the row gauge the generic fibre of the
  pencil `{x = c}` is a projective line through `[0:1:0]`, meeting `D` in `d` points and
  `L_inf` once transversally; the boundary circle of that affine line is a meridian of
  `L_inf`, and its `phi`-image is the ordered product `Pi = Pi_1 ... Pi_{d'}` of the block
  products. This is exactly the identification SK and REV already use when they equate
  "`Pi in V_4`" with "the `S_3`-resolvent descends to `pi_1(P^2 - Dbar)`" (SK §3.4, REV §3.2).
* **THEOREM SK-5** (CONFIRMED at REV §3.2, promotion recommended): in the non-constant
  stratum the three block products `A, B, C` are pairwise distinct, `conj_Pi` cycles them,
  and therefore `ord(Pi) = 3` — `Pi` is a **3-cycle** — at every `g >= 2`.

SK and REV both draw the same negative consequence and then stop: `psi(Pi)` is a nontrivial
3-cycle in `S_3 = S_4/V_4`, the resolvent does not descend, and "closing
`OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` would not touch this stratum: there is no triple
cover of `P^2` to apply it to" (SK §4.2; repeated verbatim at REV §3.2 and again at REV §7).

That inference is where the lane opens. What fails to exist is a triple cover branched
**only in `Dbar`**. What does exist, for exactly the same reason that the descent fails, is
a normal triple cover of `P^2` branched in `Dbar u L_inf`, with `L_inf` carrying inertia
`Z/3`. It is a legitimate object of Miranda's theory, and it is the object the charge asks
for. §2 builds it and reads off what it forces.

## 2. Route 1 — the extended projective cover and mixed-inertia triple covers

### 2.1 Setup: the resolvent triple cover `Z -> P^2` branched at `Dbar u L_inf`

Let `psi : S_4 ->> S_4/V_4 = S_3` be the resolvent quotient. A transposition of `S_4` acts on
the three pairings `{12|34, 13|24, 14|23}` as a transposition; a 3-cycle acts as a 3-cycle.
Write `rho := psi . phi : pi_1(P^2 - (Dbar u L_inf)) ->> S_3` (surjective, since `phi` is onto
`S_4`), using `pi_1(A^2 - D) = pi_1(P^2 - (Dbar u L_inf))`. Let `Z` be the normalisation of
`P^2` in the degree-3 subextension attached to a point stabiliser `S_2 < S_3` (equivalently,
to `D_8 < S_4`). Then:

* `Z` is an irreducible normal surface (transitivity of `S_3` on 3 letters), and
  `pi : Z -> P^2` is finite; since normal surface singularities are Cohen-Macaulay, `pi` is
  finite flat and `Z -> P^2` is a **normal triple cover** in Shirane's sense
  (`refs:1211.2526v1`, Remark 0.2).
* The inertia along a generic point of `Dbar` is generated by `psi(tau)` for a meridian
  transposition `tau`, i.e. by a transposition of `S_3`, acting on the three cosets with cycle
  type `(2,1)`: **simple branch, index 2**. So `Dbar <= S_pi`.
* The inertia along `L_inf` is generated by `psi(Pi)`, and by SK-5 `Pi` is a 3-cycle, so
  `psi(Pi)` is a 3-cycle acting on the three cosets as a 3-cycle: **total branch, index 3**.
  So `L_inf <= T_pi`.
* The branch locus is contained in `Dbar u L_inf`, `Dbar` is irreducible, and `Dbar != L_inf`.
  Hence, exactly,

```text
(2.1)     S_pi = Dbar ,     T_pi = L_inf ,     Delta_pi = Dbar + 2 L_inf .
```

This is precisely the mixed `(deg S_pi, deg T_pi) = (4g, 1)` configuration the charge asks
for; the `g = 1` shadow `(4,1)` is a case Tokunaga and Yasumura solved and Shirane's
Introduction lists as nonempty (`refs:1211.2526v1`, Remark 0.5).

**Correction to SK §4.2 / REV §3.2 / REV §7.** The sentence "there is no triple cover of `P^2`
to apply it to" is false as written. What SK-5 forbids is a triple cover branched *only* in
`Dbar`; the cover (2.1) exists for exactly the same reason. Consequently
`OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` *does* bear on family 3's non-constant stratum, and
Coord:49-50 is nearer the truth than REV's rejection of it — though, as §2.3 shows, the
splitting hypothesis is not needed, because the relevant divisibility can be obtained
outright.

### 2.2 The charged parity horn is REFUTED

The charge proposes: "branch degree `4g+1` — odd! — versus the Cardano parity constraints".
The reduced branch locus `Dbar u L_inf` does have degree `4g + 1`. But the divisor that
carries the Miranda class is the **weighted** one. With `pi_* O_Z = O ⊕ T_pi` (`T_pi` the
Tschirnhausen module, locally free of rank 2), the branch divisor `Delta_pi = S_pi + 2 T_pi`
is the discriminant divisor and its associated line bundle is `(det T_pi)^{-2}`
(`refs:1211.2526v1`, §1.1.1 and §1.1.5, quoting Miranda [8, Lemma 4.5, Prop. 4.7]). The
weights `1` and `2` are forced by the local discriminant orders: for a simple branch the
cubic factors as `(t^2 - u)(t - c)` with `c(0) != 0` and `disc = 4u(c^2-u)^2` has order 1;
for a total branch `t^3 - u` has `disc = -27u^2`, order 2. Therefore

```text
(2.2)     deg Delta_pi = deg Dbar + 2 = 4g + 2 = 2k ,      k := -deg det T_pi = 2g + 1 .
```

`4g + 2` is **even**, as it must be. The parity horn as charged is dead: no contradiction
arises from it, and the odd number `4g+1` is simply not the invariant that the structure
theory constrains. (The same computation records a fact worth keeping: the parity of
`deg Delta_pi` reproduces exactly the promoted sign rule `sgn(Pi) = (-1)^d`. `Pi in V_4` gives
`Delta_pi = Dbar`, `d` even; `Pi` a transposition or a 4-cycle gives `Delta_pi = Dbar + L_inf`
and `d` odd; `Pi` a 3-cycle gives `Delta_pi = Dbar + 2 L_inf` and `d` even. Route 1 therefore
recovers, and does not contradict, Theorem A(2).)

What is left is that `k = 2g + 1` is **odd**, and that `T_pi` contains a *rational* curve of
total ramification. That is the exploitable structure.

### 2.3 THEOREM TB — the total-branch congruence

Fix Miranda's local description as recorded at `refs:1211.2526v1`, §§1.1.1–1.1.5: the algebra
`A := pi_* O_Z = O ⊕ T_pi` is determined by `Phi : S^3 T_pi -> det T_pi`; in a local basis
`{z,w}` of `T_pi` one has `Phi = (-b, a, -d, c)` on `(z^3, z^2w, zw^2, w^3)`, and the local
branch equation is `B^2 - 4AC` with `A = a^2-bd`, `B = ad-bc`, `C = d^2-ac`. Viewing `Phi` as
a binary cubic form, a direct expansion gives the identity used repeatedly below:

```text
(2.3)     disc( alpha_0 X^3 + alpha_1 X^2 Y + alpha_2 X Y^2 + alpha_3 Y^3 )
             = -27 ( B^2 - 4AC )      for   (alpha_0,..,alpha_3) = (-b, 3a, -3d, c).
```

> **THEOREM TB (total-branch congruence).** *Let `pi : Z -> Y` be a normal triple cover of a
> smooth surface and let `T_0 ⊂ T_pi` be a smooth rational curve in the total branch locus,
> with `T_0` meeting the rest of `Delta_pi` in a single point `P`. Put
> `k_0 := -deg( det T_pi |_{T_0} )` and let `m := ord_P( Phi|_{T_0} ) >= 0`. Then*
>
> ```text
> (2.4)     k_0 + m ≡ 0   (mod 3).
> ```
>
> *Moreover `m = 0` if and only if the fibre of `pi` over `P` is curvilinear, equivalently iff
> `Z` is Gorenstein over `P`.*

*Proof.* Write `Gamma := (pi^{-1}(T_0))_red`. Over every point of `T_0` the fibre of `pi` is a
single point: over generic points by total branching, and over `P` because `pi^{-1}(T_0)` is a
curve all of whose components dominate `T_0`, of which there is exactly one. So
`pi|_Gamma : Gamma -> T_0` is finite and bijective, hence birational (char 0), hence an
isomorphism, `T_0` being normal.

Restrict `A` to `T_0` and set `A_0 := A|_{T_0}`, a rank-3 bundle of `O_{T_0}`-algebras. The
surjection `A_0 ->> pi_* O_Gamma = O_{T_0}` has kernel the nilradical `n`, a rank-2 subbundle,
and each fibre of `A_0` is a local Artin algebra of length 3 with 2-dimensional maximal ideal,
so `n^3 = 0`. Nilpotents have vanishing trace in char 0, so `n ⊆ ker(tr) = T_pi|_{T_0}`; both
are rank-2 subbundles of `A_0` and the quotient is a torsion subsheaf of the line bundle
`A_0/n`, hence zero. Therefore

```text
(2.5)     n = T_pi|_{T_0} ,      det n = det T_pi|_{T_0} = O_{T_0}(-k_0).
```

Let `N ⊆ n` be the saturation of the rank-1 subsheaf `n^2`, and `Q := n/N`, both line bundles.
Since `n · n^2 = n^3 = 0`, the product `n · N` is a subsheaf of `n` vanishing generically,
hence zero; so multiplication descends to a nonzero map of line bundles
`Q^{⊗2} -> n^2 ⊆ N`, injective, with cokernel of some finite length `m'`. Hence

```text
(2.6)     deg N = 2 deg Q + m' ,     deg det n = deg N + deg Q = 3 deg Q + m' ,
```

so `-k_0 = 3 deg Q + m'`, which is (2.4) once `m' = m` is identified.

For that, normalise the local basis. Along `T_0` the fibres are local, so `A|_{T_0}` has
`A = B = C = 0` on `T_0`; by (2.3) this says exactly that the binary cubic `Phi|_{T_0}` has
identically vanishing Hessian, i.e. is a perfect cube over the function field. Writing
`Phi|_{T_0} = rho · l^3` with `l = mu X + nu Y` primitive over the local ring at `P`, a base
change of `T_pi` carries `l` to `X`, so in that basis `a_0 = c_0 = d_0 = 0` and `b_0 = -rho`,
where `rho` has order `m := ord_P(Phi|_{T_0})`. The algebra on `T_0` is then
`z^2 = -rho·w`, `zw = 0`, `w^2 = 0`, whence `n = <z,w>`, `n^2 = <rho·w>`, `N = <w>`,
`Q = <z̄>`, and `Q^{⊗2} -> N` is multiplication by `-rho`, of cokernel length `ord(rho) = m`.
So `m' = m`. In the same basis, `rho(P) != 0` makes `n = <z>` monogenic, i.e. the fibre
`C[t]/t^3` (curvilinear, Gorenstein); `rho(P) = 0` makes the fibre `C[u,v]/(u,v)^2`. `[]`

**Sanity checks.** (i) Cyclic covers: `z^3 = f_{3e}` has `T_pi = {f=0}`, `det T_pi = O(-3e)`,
and `Phi = (1,0,0,-f)` is nowhere zero on a reduced component, so `m = 0` and `3 | 3e` ✓ —
TB reproduces the elementary fact that a `Z/3`-cover of `P^2` needs branch degree divisible by
3. (ii) Split Weierstrass `T_pi = L^{-1} ⊕ L^{-2}`, `L = O(e)`: then `k_0 = 3e` and (2.4)
holds with `m = 0`, so `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` is a *sufficient* condition for
the `m = 0` branch of TB, never a competing one. (iii) A witness for `m = 0`: with
`T_pi = O(-e) ⊕ O(-2e)` and `Phi = X^3 + z(b_0 X^2Y + c_1 XY^2 + d_2 Y^3)` on `P^2`
(`deg b_0, c_1, d_2 = e-1, 2e-1, 3e-1`), one gets `Delta = z^2 · G` with `deg G = 6e-2`, i.e.
`(deg S_pi, deg T_pi) = (6e-2, 1)`; at `e = 1` this is the nonempty Tokunaga/Yasumura case
`(4,1)`. So `deg S_pi ≡ 4 (mod 6)` when `T_pi` is a line and `m = 0` — matching (2.4). (iv) A
witness for `m != 0`: `z^2 = yw, zw = yt, w^2 = tz` (the affine cone over the twisted cubic,
normal) has `Phi = (-y, 0, 0, t)`, `Delta = y^2t^2`, and `Phi` vanishes at the origin. So the
hypothesis `m = 0` is not automatic and must be argued, not assumed.

**Application to family 3.** With `T_0 = L_inf`, `k_0 = k = 2g+1` by (2.2), and `Delta_pi`
meets `L_inf` only at `P_inf` (one place at infinity):

```text
(2.7)     3 | (2g + 1 + m) ,   equivalently   m ≡ g + 2   (mod 3).
```

In particular **if `m = 0` then `3 | 2g+1`, i.e. `g ≡ 1 (mod 3)`**, and the rows
`(8,6), (12,9), (20,15), (24,18), (32,24), (36,27), ...` are all dead, only
`(16,12), (28,21), (40,30), ...` surviving. Degree-general restatement, valid without the
`(4,3)` shape and without coprimality: *if the boundary monodromy `Pi = phi(gamma_inf)` is a
3-cycle and the resolvent cover is Gorenstein over `P_inf`, then `d ≡ 4 (mod 6)`.* This
sharpens the first fork of Theorem A(3) (`pi1-s4-decision-opus5-20260831.md:214-219`), which
gives only "`ord(Pi) = 3`, `3 | n`, `d` even", to "`d ≡ 4 (mod 6)`".

### 2.4 Local analysis at `P_inf`: the bound `m <= 2g` and the `g = 2` pin

Take local coordinates `(y, sigma)` at `P_inf` with `L_inf = {sigma = 0}`. In the row gauge
the branch of `Dbar` at `P_inf` is `(y, sigma) = (s^g u_1(s), s^{4g} u_2(s))`
(`row-sweep-sol56-20260831.md:56-64`, as quoted at SK §1). Hence `Dbar` is **unibranch** at
`P_inf` of multiplicity `g`, with tangent cone proportional to `sigma^g`, and
`(Dbar · L_inf)_{P_inf} = 4g`. Its `g` Puiseux branches `sigma_j(y)` each have `ord_y = 4`,
and — because `s -> zeta s` multiplies the leading term of `sigma` by `zeta^{4g} = 1` — they
all have the *same* leading coefficient. Consequently, with `f` a local equation of `Dbar`,

```text
(2.8)  ord_sigma f(0,sigma) = g ,   ord_y f(y,0) = 4g ,   ord_y ( d/d(sigma) f )|_{sigma=0} = 4(g-1),
```

the last because `sum_j prod_{i != j} sigma_i` has leading coefficient `g` times a nonzero
`(g-1)`-st power, and `g != 0` in char 0.

In the normalised basis of §2.3, `Phi = rho(y) X^3 + sigma · eta'` with
`eta' = alpha_0 X^3 + alpha_1 X^2Y + alpha_2 XY^2 + alpha_3 Y^3`,
`alpha_i in C{y,sigma}` and `ord_y rho = m`. Expanding the discriminant of a binary cubic
along the triple-root locus (the two lowest terms vanish because `disc` is singular there):

```text
(2.9)   disc(Phi) = -27 rho^2 sigma^2 alpha_3^2 + rho sigma^3 t(eta') + sigma^4 disc(eta'),
        t(eta') := -4 alpha_2^3 - 54 alpha_0 alpha_3^2 + 18 alpha_1 alpha_2 alpha_3 .
```

Since `disc(Phi) = -27 · (local equation of Delta_pi) = unit · f · sigma^2`, dividing by
`sigma^2`:

```text
(2.10)   unit · f  =  -27 rho^2 alpha_3^2  +  rho sigma · t(eta')  +  sigma^2 · disc(eta') .
```

Three readings of (2.10), with `gamma := ord_y alpha_3(y,0)`:

* **(a) Setting `sigma = 0`.** `unit · f(y,0) = -27 rho^2 alpha_3(y,0)^2`, so by (2.8)
  `2m + 2gamma = 4g`, i.e.

  ```text
  (2.11)     m + gamma = 2g ,     hence    0 <= m <= 2g .
  ```

* **(b) Setting `y = 0`, assuming `m >= 1`.** Then `rho(0) = 0` kills the first two terms and
  `unit · f(0,sigma) = sigma^2 disc(eta')(0,sigma)`, so by (2.8)

  ```text
  (2.12)     ord_sigma disc(eta')(0,sigma) = g - 2 .
  ```

* **(c) Differentiating in `sigma` at `sigma = 0`.**
  `d/d(sigma)(unit·f)|_0 = -54 rho^2 alpha_3 (d alpha_3/d sigma)|_0 + rho · t_0`, where
  `t_0 := t(eta')|_{sigma=0}`. The first term has `ord_y >= 2m + gamma = m + 2g` by (2.11), and
  the left side has `ord_y = 4(g-1)` by (2.8).

> **PROPOSITION TB-2 (`g = 2` pin).** *For `g = 2` — the row `(8,6)` — the non-constant
> stratum forces `m = 4 = 2g` exactly.*

*Proof.* By (2.7), `3 | (5 + m)`, so `m ≡ 1 (mod 3)`; with (2.11), `m in {1, 4}`. Suppose
`m <= 3`, so `m >= 1` and `gamma = 4 - m >= 1`. Reading (c) at `g = 2`: the left side has
`ord_y = 4`, and the first right-hand term has `ord_y >= m + 4 >= 5`, so no cancellation is
available and `ord_y (rho · t_0) = 4`, i.e. `ord_y t_0 = 4 - m = gamma >= 1`. Hence
`t_0(0) = t(eta')(0,0) = 0`. But `gamma >= 1` means `alpha_3(0,0) = 0`, so
`t(eta')(0,0) = -4 alpha_2(0,0)^3`, forcing `alpha_2(0,0) = 0`. With `alpha_2` and `alpha_3`
both vanishing at the origin, every monomial of
`disc(eta') = alpha_1^2 alpha_2^2 - 4 alpha_0 alpha_2^3 - 4 alpha_1^3 alpha_3
 - 27 alpha_0^2 alpha_3^2 + 18 alpha_0 alpha_1 alpha_2 alpha_3` vanishes there, so
`disc(eta')(0,0) = 0`. That contradicts (2.12), which at `g = 2` reads
`ord_sigma disc(eta')(0,sigma) = 0`. Hence `m = 4`. `[]`

**Why the collapse is special to `g = 2`, stated exactly.** Step (c) yields, in general,
`ord_y t_0 >= 4(g-1) - m`, and (2.12) becomes `ord_sigma disc(eta')(0,sigma) = g-2 >= 1` for
`g >= 3` — so `disc(eta')(0,0) = 0` is *required*, not forbidden, and the contradiction
evaporates. Concretely at `g = 3`, `m = 2` (the smallest value allowed by (2.7)) one needs
`gamma = 4`, `ord_y t_0 >= 6`, hence `ord_y alpha_2(y,0) >= 2`; all of these are consistent,
and `disc(eta')(0,0) = 0` with `ord_sigma disc(eta')(0,sigma) = 1` is then achievable. So no
desk-scale contradiction is available at `g >= 3` from (2.10) alone. I record this as a
scope statement, not as an obstacle I failed to clear: the three readings (a)-(c) exhaust the
information in the leading `sigma`-jets, and the next layer requires the characteristic
exponents `beta_i` of the germ at `P_inf`, which are not pinned by the row gauge beyond
`beta_i >= d` (SK §1).

### 2.5 What Route 1 kills, and where it also reaches

Under the single hypothesis `m = 0` (equivalently: the resolvent triple cover is Gorenstein
over `P_inf`), Route 1 deletes two thirds of family 3 at a stroke:

```text
non-constant (4g,3g) survives  ==>  g ≡ 1 (mod 3),  i.e.  d ≡ 4 (mod 6).
dead:      (8,6), (12,9), (20,15), (24,18), (32,24), (36,27), (44,33), ...
survives:  (16,12), (28,21), (40,30), (52,39), ...
```

Unconditionally, (2.7) and (2.11) confine the defect to `m ≡ g+2 (mod 3)`, `0 <= m <= 2g`; and
Proposition TB-2 pins `m = 4` at `g = 2`. Route 1 also reaches beyond the non-constant
stratum. In the **constant** stratum, `Pi = c^4` with `c` a product of `g` transpositions: for
`g` odd `c` is odd, so `c^4 = 1`; for `g` even `c in A_4` and `c^4 = c` exactly when `c` is a
3-cycle. Hence for even `g` with `c` a 3-cycle, `Pi` is a 3-cycle and TB applies verbatim:
under `m = 0` those configurations also require `g ≡ 1 (mod 3)`, so they die at
`g = 2, 6, 8, 12, 14, ...` The remaining constant configurations have `Pi in V_4`, where
`T_pi = 0`, TB is silent, and `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` is the only lever — as SK
and REV correctly say for that case.

## 3. Route 2 — the A-side order fork at outer coprime `(4,3)`

Theorem A (`pi1-s4-decision-opus5-20260831.md:214-219`) is stated for `gcd(n,d) = 1`; its
part (3) is the fork *either* (`ord(Pi) = 3`, `3 | n`, `d` even) *or* (`ord(Pi) = 4`, `4 | n`,
`d` odd). At noncoprime shape the promoted transport is Theorem A', whose parts (1)-(4) are
the ones SK consumes.

**The fork is entered, not exited.** At outer coprime `(d',n') = (4,3)` every clause of the
first horn is *satisfied identically*: SK-5 supplies `ord(Pi) = 3`; `3 | n' = 3` and `d' = 4`
even are arithmetic identities of the shape, true at every `g`. A'(3) contributes
`Pi^{n'} = Pi^3 in Z(H)`, which is vacuous once `ord(Pi) = 3`. So the charged combination
"`ord(Pi)=3` with the promoted divisibility (`3|n'`, `d'` parity)" has no residue: there is no
second horn to close and no arithmetic tension to exploit. Route 2 as charged is
**structurally vacuous at `(4,3)`**, and I record that as its verdict rather than manufacture
a constraint. The inner-cable side is unchanged from SK (4.2) and REV §6:
`e(iota) = 4g - 1 + 2 delta_aff - 9g^2` is one linear condition on `iota in B_g^4`, which at
`g = 2` is `Z^4` (a three-parameter family) and at `g >= 3` constrains only the total
exponent; no `delta_aff` census is available, and filling that by analogy with the `(4,2)`
closure would be a FALLACY-v2 cap.

**The traffic runs the other way.** What Route 2 supplies is not an extra constraint on
family 3 but a target for Route 1's output. Theorem A(3)'s first horn is exactly the
hypothesis of TB, so (2.4) upgrades it, in the coprime case as well:

> **COROLLARY (A(3) sharpened).** *In the situation of Theorem A, if `ord(Pi) = 3` and the
> resolvent triple cover is Gorenstein over `P_inf`, then `d ≡ 4 (mod 6)` — not merely `d`
> even.*

Two consistency checks. The coprime member `(d,n) = (4,3)` itself has `d = 4 ≡ 4 (mod 6)`, so
the sharpened fork does **not** kill it — correct, since its closure comes from the `B`/`C`
half of the coprime Main Theorem and not from A (SK §4). And the second horn `ord(Pi) = 4`
gives `psi(Pi)` a transposition, hence `T_pi = 0`, `Delta_pi = Dbar + L_inf` of degree
`d + 1 = 2k`, hence `d` odd: Route 1 recovers that clause of A(3) and adds nothing to it, as
it should, there being no total branch to carry a congruence.

## 4. Cross-check against the charged reviews

**What I consume unchanged.** SK-5 (`Pi` a 3-cycle in the non-constant stratum, every `g`) is
taken as reviewed and CONFIRMED at REV §3.2; I re-derive only the identification of `Pi` with
the `phi`-image of a meridian of `L_inf`, which SK and REV already use implicitly whenever
they equate `Pi in V_4` with descent. Lemma 4.2, the outer normal form (4.1), the `g = 2`
constant-stratum kill, and the `(8,6)` non-constant `phi`-orbit are untouched: nothing here is
an outer-level statement, so nothing here competes with them.

**Three corrections.**

1. *SK §4.2, REV §3.2, REV §7 — "there is no triple cover of `P^2` to apply it to".* False as
   written. The cover exists; it is branched at `Dbar u L_inf` with `L_inf` of inertia `Z/3`.
   The correct statement is "no triple cover branched **only** in `Dbar`".
2. *REV §7 — "Coord:49-50 ('Tschirnhaus-splitting would close family 3') is false for the
   non-constant stratum".* Refuted. If `T_pi = L^{-1} ⊕ L^{-2}` with `L = O(e)` then
   `k = 3e`, so (2.7) forces `m ≡ 0 (mod 3)` and, with `m = 0`, `g ≡ 1 (mod 3)` outright.
   Splitting *does* bear on the non-constant stratum. Coord is nearer right than REV here,
   though for a reason neither states.
3. *SK's phrasing of `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` — "if yes, `6 | d`".* That form is
   correct only on descent strata (`Pi in V_4`, `Delta_pi = Dbar`, `deg Delta_pi = d`). On a
   3-cycle stratum the weighted degree is `d + 2`, so the conclusion is `6 | d + 2`, i.e.
   `d ≡ 4 (mod 6)`. Applying the `6 | d` form to family 3's non-constant rows would be a
   flag/place conflation of the reduced and weighted branch divisors.

**What does not change.** `(8,6)` still survives the outer battery; TB is not an outer
statement and does not contradict that. The `d_min` obligation of
`OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` still stands. Family 2 is untouched by anything here,
except that the same machinery, applied to a family-2 row, gives nothing: there `Pi in V_4` at
`g = 2` by SK (3.3), so `T_pi = 0` and TB is vacuous — which is exactly the structural reason
SK's `OPEN[SHAPE-2-INFINITY-Z3]` and the present lane are different problems.

**Verification status, stated plainly.** No CAS was run. Identity (2.3) was verified by hand
coefficient matching against `disc = a1^2a2^2 - 4a0a2^3 - 4a1^3a3 - 27a0^2a3^2 + 18a0a1a2a3`,
and the expansion (2.9) by hand substitution of `(rho + sigma alpha_0, sigma alpha_1,
sigma alpha_2, sigma alpha_3)` into it. Both were then checked against two independent
witnesses (the cyclic cover and the split Weierstrass family of §2.3). Proposition TB-2 is a
finite hand computation in two power-series variables. What is *not* verified anywhere is the
existence of any residual curve in any surviving row; nothing below asserts one.

## 5. Verdict

The charge's third option is the correct one, but at a named **local** input rather than a
classification input.

| Claim | Scope | Verdict |
|---|---|---|
| Extended cover `Z -> P^2` branched at `Dbar u L_inf` exists, mixed inertia `(2,3)` | every `g >= 2`, non-constant | **ESTABLISHED** |
| Charged parity horn (branch degree `4g+1` odd) | — | **REFUTED**; weighted degree `4g+2` is even |
| `deg Delta_pi = 4g+2`, `k = -deg det T_pi = 2g+1` | every `g` | **ESTABLISHED** |
| THEOREM TB: `3 \| k_0 + m`, `m = ord_P Phi\|_{T_0}` | any normal triple cover, rational `T_0 ⊂ T_pi` | **ESTABLISHED** |
| `m ≡ g + 2 (mod 3)` and `0 <= m <= 2g` | every `g >= 2`, non-constant | **ESTABLISHED** |
| `m = 0` (Gorenstein over `P_inf`) `==> g ≡ 1 (mod 3)` | every `g >= 2` | **ESTABLISHED**, conditional on `m = 0` |
| `(8,6)` non-constant forces `m = 2g = 4` exactly | `g = 2` | **ESTABLISHED** (Prop. TB-2) |
| Uniform kill of family 3 non-constant | every `g` | **NOT OBTAINED** |
| Route 2 (A-side order fork) yields a new constraint at `(4,3)` | every `g` | **VACUOUS**; fork entered, not exited |
| Theorem A(3) fork 1 sharpened to `d ≡ 4 (mod 6)` | coprime and noncoprime | **ESTABLISHED**, conditional on `m = 0` |
| `TSCHIRNHAUS-SPLIT` is irrelevant to the non-constant stratum | — | **REFUTED** (REV §7) |
| Existence of any residual curve in a surviving row | — | **NOT ASSERTED** |

So: **not killed uniformly; not a finite list; OPEN at one named local input**, with the
family thinned by a congruence and, at `g = 2`, reduced to a single pinned integer.

## 6. Residual and named successor

**Note completing the proof of Theorem TB.** The filtration argument computes
`m' = sum_{p in T_0} ord_p( Phi|_{T_0} )`, the total cokernel length; the hypothesis that
`T_0` meets the rest of `Delta_pi` only at `P` is what makes `m' = m`. Indeed if `Phi(p) = 0`
at some `p in T_0` then `a,b,c,d` all lie in `m_p`, so `A,B,C in m_p^2` and
`mult_p Delta_pi = mult_p(B^2 - 4AC) >= 4`; but for `p` off `S_pi` one has
`mult_p Delta_pi = 2`. For family 3, `Dbar` meets `L_inf` only at `P_inf`, so the hypothesis
holds and the defect is concentrated at one point — the same concentration phenomenon SK
records at (3.4) for family 2, here obtained for the total-branch component.

**The named residual.**

```text
OPEN[S3-RESOLVENT-GORENSTEIN-AT-P-INF]:
Is the S_3-resolvent triple cover Z -> P^2 of a residual branch curve with Pi a 3-cycle
Gorenstein over the unique point P_inf — equivalently, is Phi(P_inf) != 0, equivalently
m = 0?  A positive answer gives d ≡ 4 (mod 6) at every degree, hence g ≡ 1 (mod 3) for
family 3's non-constant stratum, killing (8,6), (12,9), (20,15), (24,18), ...
```

This is not a classification input: it is one local integer at one point, and by (2.7) and
(2.11) it is already confined to `m ≡ g + 2 (mod 3)`, `0 <= m <= 2g`.

**Successors, in priority order.**

1. `OPEN[S3-TB-M0]` — the general Gorenstein question above. Highest value: it also makes the
   sharpened Theorem A(3) fork unconditional at every degree.
2. `OPEN[S3-TB-G2]` — kill `m = 4` at `g = 2`, i.e. finish `(8,6)`. The residual is fully
   explicit and bounded: normalised local data `Phi = rho(y) X^3 + sigma · eta'` with
   `ord_y rho = 4` and `alpha_3(P_inf) != 0` (forced by `gamma = 0`), against a germ of `Dbar`
   of type `A_8` in the gauge `f = unit · ((sigma - c(y))^2 - y e(y)^2)`, `ord c = ord e = 4`.
   Readings (a)-(c) of (2.10) are exhausted; the next layer is the second `sigma`-jet.
3. `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]`, **re-typed**: on total-branch strata its payoff is
   `6 | d + 2`, not `6 | d`. A positive answer implies `m ≡ 0 (mod 3)` and closes item 1 for
   family 3 immediately.
4. Untouched and unchanged: `OPEN[SHAPE-2-INNER-g>=3]`, `OPEN[SHAPE-2-INFINITY-Z3]`,
   `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`.

**Dead ends recorded, so they are not re-run.** (i) Riemann–Hurwitz on a generic line gives
integral genera for the degree-3, degree-4 and `S_4`-Galois restrictions (`2g-1`, `2g-2`,
`24g-15`): no obstruction there. (ii) The naive identity "`k = 3 Gamma^2`" is **invalid**:
`pi^* L_inf = 3 Gamma` gives `9 Gamma^2 = 3 · L_inf^2 = 3`, so `Gamma^2 = 1/3`, `Gamma` is
never Cartier, and the correction term is exactly `m`. Any argument that treats `Gamma^2` as
an integer is a floor/attainment error. (iii) On the double plane `W` (`w^2 = f_{4g}`) the
preimage of `L_inf` splits as `L_1 + L_2` — `f|_{L_inf}` is `unit · y^{4g}`, a square — and
`Y' -> W` is the `Z/3`-cover branched at `L_1 + 2 L_2`; but `(L_1 + 2L_2) · h = 3` is already
divisible by 3, so the numerical shadow of the Tokunaga class criterion carries no
obstruction, and the criterion proper needs `Cl(W)`, which is outside desk scope.

## 7. Sources fetched and hashed

```text
b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153
  https://arxiv.org/pdf/1211.2526v1   (fetched 2026-09-01, 174308 bytes)
  Taketo Shirane, "A note on normal triple covers over P^2 with branch divisors of
  degree 6", arXiv:1211.2526v1.
  Consumed: Notation (Delta_pi = S_pi + 2 T_pi; ramification index 2 along S_pi, 3 along
  T_pi; total branched point); Remark 0.2 (a finite surjective morphism from a normal
  surface to a smooth surface is a normal cover, via Cohen-Macaulayness); §1.1.1
  (Tschirnhausen module T_pi, pi_* O_X = O ⊕ T_pi); §1.1.2 (Miranda's correspondence with
  Phi : S^3 E -> det E); §1.1.3 (local a,b,c,d and A = a^2-bd, B = ad-bc, C = d^2-ac);
  §1.1.4 (X ⊂ V(E), Cohen-Macaulay); §1.1.5 (branch divisor B^2-4AC = 0, associated line
  bundle (det T_pi)^{-2}); §1.1.6 and Remark 0.5 (Weierstrass split T_pi ≅ L^{-1} ⊕ L^{-2};
  the nonempty (deg S, deg T) = (4,1) case of Tokunaga/Yasumura).
  This hash reproduces the custody hash already recorded at REV §0.
```

R. Miranda, *Triple covers in algebraic geometry*, Amer. J. Math. **107** (1985) 1123–1158,
is consumed **only** through Shirane's §1.1 restatements above; it was not fetched.
Tokunaga's Cardano paper (J. Math. Kyoto Univ. **31** (1991) 359–375) is **not consumed**: the
charge proposed routing the constraint through its building data, but Theorem TB is proved
directly from the Miranda local form, so no first-page-only citation is load-bearing anywhere.

Campaign artifacts read, none edited: the three charged inputs (hashed in §0), plus
`pi1-s4-decision-opus5-20260831.md` (Theorem A, lines 214-219). `jc2-lean` was not inspected.
No canonical ledger was touched. Nothing above is promoted; every item is subject to hostile
review, and the two I would most want attacked are the identification `n = T_pi|_{T_0}` in the
proof of TB (the trace-kernel step) and the no-cancellation claim in (2.8) for
`d/d(sigma) f |_{sigma=0}`, which Proposition TB-2 rests on.

<!-- BODY-END -->
