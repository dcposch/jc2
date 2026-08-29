# Fable 5 primary — TD12-BCHILD/v1: the shared forward Keller/source coefficient recurrence

Lane: Fable 5, equal independent primary researcher (not review). Date: 2026-08-29.
Git basis (verified at session start and again before verdict):

```text
76c746f698103d20019bfeb72654a361ccc5371d
```

Task: decide whether the frozen source data license ONE shared forward
Keller/source coefficient recurrence emitting (1) the first-child
coefficient vector for the depth-24 B direction of the td12 U1 trunk
`(nu,kbar,X,M,w) = (25,17,25,3,2/3)` and (2) the two first-child vectors for
the two depth-16 sibling directions in `(nu,dp,dq,kbar,X,M,w) =
(17,68,52,13,17,4,3/4)` — or to prove precisely that the frozen basis does
not determine/initialize such a recurrence.

Worked only in `/Users/dc/code/math/jc2`. No access of any kind to
`jc2-lean`. No web, AWS, remote shell, CAS, or heavy computation; exact desk
algebra plus one tiny stdlib `Fraction` identity check in `/tmp` (script and
output reproduced in §8.4). One file written: this report. No commit, no
push, no edit to any other file.

## 0. Custody

All sixteen manifest hashes were recomputed with `shasum -a 256` before any
read and recomputed again immediately before sealing this report; both times
every hash matched the frozen manifest exactly (pre = post):

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829  xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md
3f214db8c12d022c2852dfadbbc268d105484343a8f6d4664765a08d3efcea03  xmodel/m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
70cf67b2241b1361e958e673b81d883f34a87be9e5fe3631a3a36c35646c3060  xmodel/m2-td12-u1-sibling-exact-charge-r1-hostile-review-fable5-20260829.md
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
432a4152387cff943e220a6236912f2481a1ea3004d2c53ae95f14eb267f1ab0  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-hostile-review-grok46-20260829.md
635aecffbd226acbc29787cec86bc1fdcdfa459e1aa38a8d1a8acb5d6593b72a  xmodel/m2-20260829-promotions-theorem-interface-pass-sol56.md
91521dc126449ae217315b657493f2b9a170c630013d8c547cceab7f2e680113  xmodel/ideation-20260829T0820Z-synthesis.md
d3cf9d608427e4410ccb8b3ce04539fb22d854b9e58e6354d15115c3b48d564b  xmodel/ideation-20260829T0820Z-crosspoll-fable5.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
```

Passages actually charged (exact perimeter of use): the pinned PDF at
Notation 3.9, Statement 3.7 (5), Notation 3.10/3.11, Statement 3.9 with its
proof line `eta_G = x^{1/kappa}(eta_F - c)` (pp. 13–15); Proposition 4.1
with its proof (p. 18); Proposition 4.2 with its proof, the displayed full
identities `J(f, h_j) = h_0^{k_0-1} ... h_{j-1}^{k_{j-1}-1}` and
`J(f^F, h_j^F) = (h_0^F)^{k_0-1} ... (h_{j-1}^F)^{k_{j-1}-1} xi^{-u}`, the
Remark after it, and Proposition 4.4 (pp. 19–21); Proposition 8.1 with
proof, including `d_{h,F} = (mu_F - 1) d_F + 1 - u` (pp. 39–41). Trunk cell
and pinned top: trunk-consumer primary §§2–3 with its Opus review (REPAIR
4a `i_F = 3n i_G`). B-gate, `i = 6n` rider, interpolation freedom, residues:
discriminator §§1, 4–6 with my own Fable review (R1 ordering, formal-scope
§7). Sibling cell, charge, gates: sibling exact-charge report §§1–4 with its
Fable review (incl. finding N1); sibling T1 solve §§2–6 with its Grok review
(PASS). Child-pattern law (C), vanishing ladder (V), weight law (W)/Theorem
D and the `kappa_F`-graded re-indexing `P_k := p_{n-Qk}`: td8 first-extra-jet
primary §§2b, 8 and its Fable review §2.5 (repair R1). Direction-orbit
counting: Section 9 audit (4.6). Interface target: promotions pass §§B, 4.1.

Printed identities are cited as printed; every campaign repair used is named
as such. The stacked-fraction hazard was respected: every load-bearing
formula quoted here is a display line, and Prop 8.1(iv)'s right side is read
with the reviewed free `C*` constant (the glyph pdftotext drops).

## 1. Verdict

**`SOURCE_UNDERDETERMINED`.**

**First genuine obstruction** (reached before any vector can be emitted):
the graded Keller convolution — which the printed basis does license in
exact symbolic form (§2, §3) — couples the f-side window pieces `P_1..P_24`
to the g-side window pieces `G_1..G_24` of the *same* completion, and its
every order requires the g-side initialization pair

```text
(r, c_g)  with  G_0 = c_g * p^r,   r = i * l_0/k_0  in N*,   c_g^{k_0} = s_0,
```

i.e. the first Abhyankar resolvent step `(k_0, l_0, s_0)` of the unknown
pair (Prop 4.2(iii)). No frozen input pins `(k_0, l_0, s_0)`, nor `r`, nor
`c_g`, nor even `D_{g,F} mod anything` beyond the derived `nu_F | D_{g,F}`.
Two further independent initialization gaps: the window pieces are
contaminated by every fibre series whose contact with the F-truncation lies
within 24 (resp. 16) normalized units above the cell, and the degree caps
(`deg_y f`, `deg_y g`) are unpinned (§3.4).

Moreover — and this is the sharper half — the failure is not merely missing
constants. Granting arbitrary admissible `(r, c_g)`, the convolution
**provably cannot determine the fresh f-side piece at its own order**: an
exact absorption identity (Theorem B, §8.2, machine-checked) shows the
order-s equation is solved for *every* choice of `P_s` on the reviewed
vanishing/weight class, with an explicit polynomial g-side response. The
Keller condition at the available orders therefore *merely couples* the
freedom found by the discriminator's A/B interpolation to unknown g-side
pieces; it removes none of it at the fresh order, and pushes only a small
(codimension ≤ 1 + r-dependent divisibility) cascade of conditions onto
lower-order data (§8.3), none evaluable from the frozen basis.

What the basis does determine: the leading coefficients

```text
v_B,0   = (25 u^2 c^{24})^i                              (c^{25} = B = 9u, nonzero),
v_S_j,0 = ((B_j - A)^2 (B_j - B_{3-j}) * 17 c_j^{16})^i  (c_j^{17} = B_j, nonzero),
```

exactly (up to the recorded route gauges), plus, for every `k >= 1`, only
the residue class `e_k` and the vanishing floor of `P_k` — never a value.
So no `v_{B,k}` or `v_{S_j,k}` with `k >= 1` is determined, no vector can
be emitted, and manufacturing one from the reduced pattern data would be
exactly the forgery the brief forbids.

**Maximum safe descendant use, immediately:** (a) the derived universal
system `E_s` of §3, the absorption identity, and the cascade/cokernel
structure may be consumed as exact interface algebra by any future lane
that *supplies* the missing initialization data; (b) the depth-24 and twin
depth-16 gates remain necessary-only consumers with **no** vector to
consume; (c) the `v_.,0` values above may be used as the level-1
normalization guard (it passes structurally, §6); (d) the per-order
cascade conditions (§8.3) are a typed candidate kill lane for a future
primary — they are the first place where `J = 1` genuinely bites the
window. No standalone software implementation is licensed (§9).

Nothing here is a germ, a Keller pair, a counterexample, a degree bound, a
G2 result, or any JC2 conclusion.

## 2. Q1 — the source-facing pieces and how `J(f,g) = 1` becomes a convolution

### 2.1 Chart and completion (printed)

Fix the pinned fibre value `a` and the y-side component `T_{y,a}`; both
cells are interior vertices `F` there with `d_F > 0`. For a branch `P`
through `F = I_P(u)`, `u := pi(F)`, with Puiseux series
`y = sum_{j in Q+} c_j x^{-j}` (form (3), series at `x -> infinity`),
Notation 3.9 defines the chart

```text
eta_F := x^{u} ( y - sum_{j < u} c_j x^{-j} ),      i.e.  y = phi(x) + eta_F x^{-u},
```

and `h^F(x, eta)` by `h(x,y) = h^F(x, eta_F)` for any polynomial `h`.
Statement 3.7 (5): `h^F(x,eta) = sum_{j in Z} x^{j/kappa} p_{h,j}(eta)`,
finitely many nonzero, `kappa` suitable (Not 3.7), top index
`n_h := kappa d_{h,F}` with `p_{h,n_h} = p_{h,F}` (Not 3.10),
`D_{h,F} := kappa_F d_{h,F} in Z` (Not 3.11).

### 2.2 Graded pieces `P_k`, `Q_k` (campaign-repaired indexing, reviewed)

At suitable `kappa` with `Q := kappa/kappa_F`, the reviewed weight law
(td8 Theorem D(i), repair R1 of my td8 review — the deck-transformation
proof never uses `h = f` and applies verbatim to any polynomial) forces
`p_{h, n_h - k} == 0` unless `Q | k`. The `kappa_F`-graded pieces of this
report are therefore

```text
P_k(eta) := p_{f, n_f - Qk}(eta)          (f-side,  P_0 = p_F),
G_k(eta) := p_{g, n_g - Qk}(eta)          (g-side,  G_0 = p_{g,F}),
```

`k = 0, 1, 2, ...` counting down from the top on the `kappa_F`-lattice.
Indexing origin: the top. Top orders: `n_f/kappa = d_F = D_F/kappa_F`,
`n_g/kappa = d_{g,F} = D_{g,F}/kappa_F`. Trunk cell: `D_F = 25 i`,
`kbar_F = 17`, `t = eta^{25}`, reduced `p = (t-A)^2(t-B)`, `A = 8u`,
`B = 9u`, `u != 0`, full top `P_0 = p^i`; full index `i = 6n` only under
the direct-entry rider (Opus REPAIR 4a; the derivation below needs only
`i in N*`). Sibling cell: `D_F = 17 i`, `kbar_F = 13`, `t = eta^{17}`,
`p = (t-A)^2(t-B_1)(t-B_2)`, `P_0 = p^i`, same rider for `i = 6n`.

### 2.3 The Keller identity in the chart (printed) and the convolution (derived)

Proposition 4.1's proof contains the full-chart identity, printed:

> From the chain rule by induction we have
> `J(f^F(xi,eta), (g-b)^F(xi,eta)) = xi^{-n/kappa}` (cf. Notation 3.9),

i.e. `J_{x,eta}(f^F, (g-b)^F) = x^{-u}` as formal series — the exact chart
transport of `J_{x,y}(f,g) = 1` (independent one-line check:
`dx ^ dy = x^{-u} dx ^ d(eta)` under `y = phi + eta x^{-u}`, so
`J_{x,eta} = x^{-u} J_{x,y}`). For `F in T_a^+` Proposition 4.2 takes
`h_0 = g` outright and its Remark discharges hypothesis (7), so the
`b`-shift is not needed: `J_{x,eta}(f^F, g^F) = x^{-u}`.

Substituting the two St 3.7 expansions and collecting the coefficient of
each `x^{(j+k)/kappa - 1}` gives, for every integer `m`,

```text
sum_{j+k=m} ( j p_{f,j} p_{g,k}' - k p_{f,j}' p_{g,k} ) = kappa * [ m = kappa(1-u) ],
```

`' = d/d eta` throughout. Re-indexed from the tops on the `kappa_F`-lattice
(all off-lattice terms vanish by Theorem D(i)) with `s := a + b`:

```text
(E_s)   sum_{a+b=s} [ (D_F - a) P_a G_b' - (D_g - b) P_a' G_b ]  =  kappa_F * [ s = s* ],

        s* := D_F + D_{g,F} - kbar_F .
```

This is the exact coefficient-convolution form of `J(f,g) = 1` at `F`. It
is derived from printed identities only; no campaign object other than the
re-indexing repair enters. The right side lands at the single order `s*`
(trunk: `25(i + r) - 17`; sibling: `17(i + r) - 13`), which is far below
the gate windows `s <= 24` resp. `s <= 16`; on the whole window every
`E_s` is homogeneous.

### 2.4 What the evaluation formula is and is not

The formula `v_{c,k} = [(eta - c)^{i-k}] P_k(eta)` is the diagonal
**extraction** law (C) with the vanishing ladder (V) making it exact —
derived by `Q`-fold iteration of printed St 3.9 (td8 §2b as repaired by R1
of its review). It is *not* a Keller recurrence and is not called one here:
it presupposes the pieces `P_k`, and nothing in the frozen basis derives
them. The genuine Keller recurrence candidate is the system `(E_s)`; §§3, 8
show it cannot be initialized from the basis and, at its own order,
constrains nothing about `P_s`.

The g-side pieces `Q_k` of the task statement are the `G_k` above. The
h-side alternative (Prop 8.1's `h = h_{m_F}`, whose reduced pattern
`q = eta(t-A)(t-B)` resp. `eta(t-A)(t-B_1)(t-B_2)` *is* route-pinned)
does not yield a closed system: the printed full identity
`J(f^F, h_j^F) = (h_0^F)^{k_0-1} ... (h_{j-1}^F)^{k_{j-1}-1} xi^{-u}` has
every intermediate resolvent's full expansion on the right side — strictly
more unknowns. The pinned `q` serves the top identity 8.1(iv) (the T1
solves) and only that.

## 3. Q2 — the universal system, order by order

### 3.1 Order 0 (forced shape; no new source datum)

`s = 0 != s*` gives `D_F P_0 G_0' - D_g P_0' G_0 = 0`, hence
`G_0^{D_F} = const * P_0^{D_g}`. Unique factorization of the known
`P_0 = p^i` (roots: the `nu_F` A-roots at multiplicity `2i`, the `nu_F`
B-roots — resp. `B_1`,`B_2`-roots — at multiplicity `i`; no zero root,
`eps = 0`) forces

```text
G_0 = c_g * p^r,     r := i D_g / D_F in N*,     D_g = nu_F * r,     c_g in C*.
```

`r >= 1` is forced: `r = 0` would give `m_F = 0`, i.e.
`D_F + D_g = kbar_F` (Prop 4.2(iv) with `mu = 0`), impossible since
`D_F = nu_F i > kbar_F`. By Prop 4.2(iii), `r/i = l_0/k_0` and
`c_g^{k_0} = s_0`. **Derived, not assumed**: the g-side top is a pure
power of the reduced `p` with the same weight lattice
(`D_g == 0 mod nu_F`), and the same residue progression as the f-side
(§5.2). The *value* `r` and the scale `c_g` are the unpinned
initialization.

### 3.2 Orders `1 <= s < min(nu_F, s*)` (the whole gate window)

Write the two fresh-unknown operators

```text
A_s[P] := (D_F - s) P G_0' - D_g P' G_0     = c_g p^{r-1} [ (D_F - s) r p' P - D_g p P' ],
B_s[G] := D_F P_0 G' - (D_g - s) P_0' G     = p^{i-1} [ D_F p G' - i (D_g - s) p' G ],
```

so that `E_s` reads `A_s[P_s] + B_s[G_s] = -K_s` with the cross sum
`K_s := sum_{0<a<s} [ (D_F - a) P_a G_{s-a}' - (D_g - s + a) P_a' G_{s-a} ]`
(`K_1 = 0`). Ledger:

- **Solved:** `G_s`, uniquely if at all. The kernel of `B_s` is
  `C * p^{(D_g - s)/nu_F}` (in `p`-power form `p^{r - s/nu_F}`), which is a
  polynomial iff `nu_F | s`; on the window `B_s` is injective. Indicial
  checks (trunk; sibling identical with 17): at `t = 0` the piece weight
  `e^g_s == 22 s (mod 25)` is nonzero on the window, so no resonance; at
  `t = A` resonance needs `25 | 2(D_g - s)`, at `t = B` it needs
  `25 | (D_g - s)` — both need `25 | s`, off-window. The unique always-on-
  lattice resonance is at `t = infinity`: eta-degree `N_res = 75r - 3s`
  (sibling: `68r - 4s`, same mechanism), which is what produces the
  cascade condition of §8.3.
- **Free:** `P_s` — completely, at its own order (Theorem B, §8.2), on the
  admissible class: weight `e_s` (§5.2), vanishing floor
  `ord >= mult - s` at every root of `p` ((V), derived), `p^{i-r} | P_s`
  additionally required only if `r < i` (automatic on the (V)-class for
  `s <= r`, and for the level-1 exhibits for every `r >= 1`).
- **Gauge:** the route gauges — unit scalings of `f`,`g`, the eta-dilation
  (`t`-dilation, the `u`-scale of `(A,B)` resp. `A`), and the deck
  `mu_{nu_F}` — plus, at each resonance order `s in nu_F N`, one new
  g-side kernel direction `c * p^{r - s/nu_F}`.
- **Denominator/nonvanishing hypotheses:** `p != 0` squarefree-by-orbits
  with distinct nonzero roots (T1-reviewed: `B/A = 9/8`;
  `B_j/A = (9 ± 3i)/8`), `c_g != 0`, `u != 0`, `D_g = D_F r / i` exact,
  and the stripping of `p^{i-1}` resp. `p^{r-1}` shown above.

### 3.3 Universality across the three roots

The derivation of `(E_s)` used only: `F in T_a^+ cap V_{1,a}`, the pinned
reduced top `p`, and `P_0 = p^i`. It is therefore **one** recurrence form
serving all three evaluations:

- trunk B root: chart `t = eta^{25}`, state `(D_F, kbar, i) = (25i, 17, i)`,
  evaluation root `c`, `c^{25} = B`;
- sibling roots: one shared chart `t = eta^{17}`, one shared state
  `(17i, 13, i)`, two evaluation roots `c_j`, `c_j^{17} = B_j` — the two
  sibling vectors are evaluations of the *same* `P_k` family with only the
  root changed;
- across the two cells the g-side initialization is *shared*: both cells
  lie on the same `T_a^+` and inherit the same first resolvent step
  `(k_0, l_0, s_0)` (Prop 4.4 prefix law through the common parent, whose
  `m >= 1` is forced as in §3.1). Hence the same `r = i l_0/k_0 = 6n l_0/k_0`
  at both cells and `c_g^{k_0} = s_0` at both. One shared unknown pair
  `(l_0/k_0, s_0)` initializes all three evaluations — but it is unknown.

### 3.4 Why the system still cannot be initialized

Three independent gaps, each fatal to emission:

1. **`(r, c_g)` unpinned.** Every operator `A_s`, `B_s` and every cascade
   condition depends on `r` (and `c_g` scales the coupling). `r` encodes
   `d_{g,F}/d_F = l_0/k_0`, a global invariant of the unknown pair; the
   frozen route data `(nu, kbar, X, M, w)`, `i`, tops, and charges nowhere
   constrain it beyond `r in N*`.
2. **Window contamination.** The pieces `P_s`, `G_s` are global chart
   objects of `f`, `g`: every fibre series whose truncation-contact level
   `v` with the branch satisfies `kappa_F (u - v) <= 24` (resp. 16)
   contributes unknown terms to the window (a departed factor
   `x^{-v}(Delta + ... + eta x^{v-u})` enters at graded offsets
   `kappa_F(u-v), 2 kappa_F(u-v), ...`). The frozen basis pins neither the
   full contact ledger above the cells in `kappa_F` units nor any of the
   coefficient data `Delta`. (x-only content of `f - a` is window-clean:
   its offsets are multiples of `kappa_F >= nu_F >` window.)
3. **Caps unpinned.** `deg_eta P_s` is bounded by no frozen datum
   (`deg_y f` is not pinned; lower pieces may exceed the top degree
   `75i`); the same on the g-side. The exact per-order dimension counts
   (§8.3) therefore cannot be closed numerically.

## 4. Q3 — the B direction: what the basis determines

- `v_{B,0} = [(eta-c)^i] P_0` **is determined** by the pinned top alone:
  near `c` (`c^{25} = B`), `t - B = 25 c^{24}(eta - c)(1 + O(eta-c))` and
  `t - A -> B - A = u`, so

  ```text
  v_B,0 = ( (B-A)^2 * 25 c^{24} )^i = (25 u^2 c^{24})^i = (225 u^3 / c)^i != 0,
  ```

  exact up to the recorded gauges. This is St 3.9(ii) made explicit.
- For `1 <= k <= i`: the basis determines **only the residue/vanishing
  spaces** — weight `e_k == 22k (mod 25)` (Theorem D(ii) with
  `D_F == 0`, `N_1 = -17 == 8`, `8^{-1} == 22`), vanishing floor
  `ord_{A-roots} >= 2i - k`, `ord_{B-roots} >= i - k` ((V)) — and **no
  value**. The pure-power residue progression `e_k = k e_1` (discriminator
  §5, re-verified) means the weight lattice cannot obstruct or select.
- A **genuine recurrence** exists at form level (`E_s`, §2.3) but is not
  initialized by the basis (§3.4) and, by Theorem B (§8.2), does not
  constrain `P_k` at its own order even when initialized. So the honest
  trichotomy answer is: `v_{B,0}` determined; `k >= 1` residue/vanishing
  spaces only; the recurrence exists but licenses no emission.

The pinned reduced top `p_F = (T-A)^2(T-B)`, `q_F = eta(T-A)(T-B)`,
`T = eta^{25}`, `A = 8u`, `B = 9u`, `u != 0` is preserved untouched; the
full index `i = 6n` is used only under its direct-entry rider; and the
discriminator's A/B interpolation `R_k(A), R_k(B)` remains exactly what its
review left it: formal top compatibility, not source realization — §8 shows
the Keller coupling does not upgrade or destroy it at the available orders.

`C_B,1(z) = sum_{k=0}^i v_{B,k} z^{i-k}` therefore has exactly one
determined coefficient (`v_{B,0}`, nonzero, degree exactly `i`) and `i`
undetermined ones. No forward-generator data exist in the basis for
`k >= 1`, and none are manufactured here.

## 5. Q4 — the sibling: the two directions read exactly

### 5.1 The T1 report, read completely

The sibling T1 solve (Sol 5.6, PASS by Grok review) gives, at gauge
`A in C*`,

```text
p = (t-A)^2 (t-B_1)(t-B_2),   q = eta (t-A)(t-B_1)(t-B_2),   t = eta^{17},
B_1 + B_2 = 9A/4,   B_1 B_2 = 45 A^2/32,
B_1, B_2 = (9 ± 3i) A / 8      (up to swap),   B_1/B_2 = (4+3i)/5,
Theta = -765 beta A^3 / 32 != 0,
```

discriminant `-9A^2/16 != 0` (roots distinct, forced), `s(A) = 5A^2/32 != 0`
(no arrival collision), `p(0) != 0` (`eps = 0` consistent, `eta || q`).
Genuine gauges: `p`-scale, `q`-scale, common `t`-dilation; the quotient is
one unordered ratio point. **The two extra roots are not rational**: they
generate `Q(A)(i)` over `Q(A)`, and the evaluation roots `c_j`
(`c_j^{17} = B_j`) live in the further Kummer extension
`Q(A, i, B_j^{1/17}, mu_17)`. No rationality is assumed anywhere below.

### 5.2 The two vectors

With the sibling's own chart and pieces `P_k` (one family for the cell),

```text
v_{S_j,k} := [(eta - c_j)^{i-k}] P_k(eta),   c_j^{17} = B_j,   k = 1..i,
C_{S_j,1}(z) := sum_{k=0}^i v_{S_j,k} z^{i-k},   j = 1, 2.
```

Determined by the basis: the two leading coefficients. Near `c_j`
(`c_j^{17} = B_j`) the factor `t - B_j` has the simple zero
`17 c_j^{16} (eta - c_j)(1 + O(eta - c_j))` while the other factors take
the values `(B_j - A)^2` and `(B_j - B_{3-j})`, so

```text
v_{S_j,0} = ( (B_j - A)^2 (B_j - B_{3-j}) * 17 c_j^{16} )^i
          = ( (B_j - A)^2 (B_j - B_{3-j}) * 17 B_j / c_j )^i,
```

with `(B_1 - A) = (1+3i)A/8`, `(B_2 - A) = (1-3i)A/8`,
`(B_1 - B_2) = (3i/4)A` — every factor nonzero, so both leading
coefficients are nonzero and exact up to gauge. Residues: `N_1 == -13 == 4 (mod 17)`,
`4^{-1} == 13`, `D_F = 17i == 0`, so `e_k == 13k (mod 17)` on both the f-
and g-side (`D_g = 17r`), the pure-power progression again (matches finding
N1's residue check).

### 5.3 Status of the pair of vectors

- They are **independent evaluations of the same `P_k`** — one recurrence
  state per cell, two evaluation roots. This is the maximal linkage the
  basis forces.
- **T1 links only the top** (`P_0 = p^i`): it pins `B_1 B_2`, `B_1 + B_2`
  and hence both `v_{S_j,0}`, nothing at `k >= 1`.
- **Galois conjugacy is not forced.** If the actual pair were defined over
  a subfield fixed by the swap `i -> -i` (fixing `A`-data), the two vectors
  would be conjugate. The frozen basis does not pin any field of
  definition, and the level-1 exhibit below produces admissible window data
  with `v_{S_1,1} != 0 = v_{S_2,1}` — incompatible with conjugacy — so
  conjugacy is an extra hypothesis, not a consequence.
- **Not source-typed at all** is false: the typing (weights, floors,
  extraction law, leading values) is source-derived; only the values
  `k >= 1` are missing. The correct classification is the first option with
  the values open.

## 6. Q5 — normalization guard

Level 1, both cells: `C_1 != 0`, `deg C_1 = i` exactly, leading coefficient
`v_{.,0} != 0` — all three hold **structurally**, by the exact leading
values of §4/§5.2 (the pinned tops force them; no computation of unknown
data is involved). Therefore the nominal first child cannot vanish and no
delay/normalization branch is entered at level 1: no later-graded first
child, no centre change, no characteristic-denominator change, and no
degree-deficient case to classify. Deeper levels cannot be evaluated at all
from the basis (no vectors), so no deeper branch is reachable; a
denominator change before level `nu_F` remains excluded by the reviewed
charge theorems, not by anything new here. Nothing is counted as a
pure-power pass.

## 7. Q6 — the ordered tests

Cannot run: step (1) of the reviewed execution order — extract the vector
from the source polynomial identities or an initialized Keller/transport
recurrence — is exactly what §§3, 8 prove impossible from the frozen basis.
No `gcd` degree, binomial list, or catalecticant test is executed; no level
is advanced; no cap is used. For completeness the order that *would* run on
supplied data is recorded: degree/nonzero guard (passes structurally,
§6); `deg gcd(C_1, C_1') = i - 1` (`= 6n - 1` on direct entries); binomial/
catalecticant membership; recenter; repeat through level 24 (trunk) resp.
16 twice (sibling), rejecting any denominator change.

## 8. Q7 — identifiability: the theorems

### 8.1 Setting

Fix either cell, grant the unpinned `(r, c_g) in N* x C*` arbitrarily, and
ignore contamination (both concessions only *help* determinacy; the result
is that even so nothing is determined at the fresh order).

### 8.2 Theorem B (absorption identity)

> For every order `s`, every polynomial `delta P` with `p^{i-r} | delta P`
> when `r < i`,
>
> ```text
> A_s[delta P] + B_s[ (r c_g / i) p^{r-i} delta P ] = 0        (exactly).
> ```
>
> Consequently `im(A_s) subset im(B_s)`, and the solvability of `E_s` in
> `(P_s, G_s)` is a condition on the lower-order data `K_s` alone: the
> fresh piece `P_s` is unconstrained on its admissible class, and the
> g-side response is the explicit matched polynomial, which moreover
> satisfies the g-side vanishing ladder (`ord_A: 2(r-i) + (2i-s) = 2r-s`,
> `ord_B: (r-i) + (i-s) = r-s`), the g-side weight class
> (`D_g == D_F == 0 (mod nu_F)`), and the natural cap
> (`deg <= 75(r-i) + deg delta P`).

Proof: expand; the coefficient of `p^{r-1} p' delta P` is
`c_g (D_F - s) r + (r c_g/i)(D_F(r-i) - (D_g - s) i)` and
`D_F(r-i) - (D_g-s)i = -i(D_F - s)` because `D_F r = D_g i`; the
coefficient of `p^r delta P'` is `-c_g D_g + (r c_g/i) D_F = 0`. Both
vanish identically — no degree, root, or genericity input. QED.

More generally, substituting `G_s = c_g p^{r-i}((r/i) P_s + Z)` turns `E_s`
into the reduced cascade equation

```text
c_g p^{r-1} [ D_F p Z' - i (D_F - s) p' Z ] = -K_s,          (E_s-red)
```

with the `Z`-operator injective on the window (kernel `p^{i - s/nu_F}`,
non-polynomial for `nu_F` ∤ `s`).

### 8.3 The honest equation count and the cascade

Per order `s` in the window:

- fresh f-side unknowns: the (V)/(W)-admissible class of `P_s` — every
  element is `eta^{e_s} * (floor factors) * R(t)` — has dimension `2s`
  (trunk; `3s` sibling) under the natural cap `deg <= deg P_0`, and at
  least that without the cap;
- fresh g-side unknowns: `G_s`, uniquely determined by the rest when
  solvable (B_s injective);
- fresh constraints: `E_s` is one polynomial identity on one weight class;
  after Theorem B it reduces to `(E_s-red)`, whose solvability is: (c-i)
  `p^{i-1} | K_s`-side divisibility (automatic for `2r >= s - 1` at the
  A-orbit and `r >= s` at the B-orbit; genuine conditions otherwise), and
  (c-ii) exactly **one** on-lattice cokernel condition, sitting at
  `t = infinity` (the always-on-lattice resonance `N_res = 75r - 3s`; all
  finite indicial points are clean on the window, §3.2). Every such
  condition acts on `K_s`, i.e. on *lower-order* data only, with
  coefficients depending on `(r, c_g)`.

So the window system is a constraint **cascade** on lower data of
codimension `<= 1 + (r-dependent shortfall)` per order, against fresh
freedom of dimension `2s` (resp. `3s`) per order, with the fresh
diagonal values never entering their own order's conditions. It is a
constraint-propagation system, not a forward generator: nothing emits
`v_{.,k}`; the solution set is an affine family fibred over the unpinned
`(r, c_g)`, caps, and contamination data. This also corrects a natural
misreading in both directions: the coupling is *not* vacuous (the cascade
conditions are real, first bite at `s = 2`, and are the typed future kill
lane), and it is *not* determining (absorption).

### 8.4 Two-choice exhibits (underdetermination proved)

Level 1, `K_1 = 0`. Both of the following satisfy the **full** Keller
convolution at its order, the vanishing ladders and weights on both sides,
the caps, and preserve the arrival diagonal (`ord_{A-roots} = 2i > 2i - 1`,
so the order-1 arrival datum is `0` in both):

```text
Trunk (any r >= 1, any c_g != 0), e_1 = 22:
  I.   P_1 = 0,                                G_1 = 0
       => v_B,1 = 0;
  II.  P_1 = eta^{e_1}(t-A)^{2i}(t-B)^{i-1},   G_1 = (r c_g/i) p^{r-i} P_1
       => v_B,1 = c^{e_1} (B-A)^{2i} (25 c^{24})^{i-1} != 0
       (exact: ord_c(P_1) = i-1 exactly, so the leading Taylor
        coefficient is the displayed product of values).
Sibling (moving exactly one direction), e_1 = 13:
  I.   P_1 = 0,                                              G_1 = 0
       => v_{S_1,1} = v_{S_2,1} = 0;
  II.  P_1 = eta^{e_1}(t-A)^{2i}(t-B_1)^{i-1}(t-B_2)^{i},    G_1 matched
       => v_{S_1,1} != 0,  v_{S_2,1} = 0.
```

(For `r < i` the divisibility `p^{i-r} | P_1` holds for both exhibits since
`2i >= 2(i-r)` and `i - 1 >= i - r` for every `r >= 1`.) Hence the frozen
reduced/top data plus the entire order-1 Keller convolution admit distinct
values at the `k = 1` slot, for **every** admissible g-side initialization — underdetermination is proved, not
inferred from a parameter count. The sibling form of exhibit II also proves
the two sibling vectors are not rigidly linked by the window system beyond
their shared `P_k` (§5.3). Extending a *given* choice through orders
`2..24` engages the cascade conditions of §8.3, which the basis cannot
evaluate; no claim of deep extension is made for either exhibit.

Machine check of the load-bearing identities (E_0 vacuity, Theorem B at
four parameter tuples including an `r = i` and an `nu = 5, A = 8, B = 9`
stand-in, and the reduced-cascade formula with `Z != 0`), exact `Fraction`
arithmetic, scratch only:

```python
# /tmp/bchild_absorb_check.py  (stdlib only; dict eta-polynomials)
# p = (t-A)^2 (t-B), t = eta^nu; P0 = p^i; G0 = c_g p^r; Dg = DF*r/i
# checks: (1) DF*P0*G0' - Dg*P0'*G0 == 0
#         (2) A_s[dP] + B_s[(r*c_g/i) p^(r-i) dP] == 0 for
#             (nu,A,B,i,r,s,DF) in {(2,1,2,2,3,1,10),(2,1,2,2,4,2,14),(5,8,9,3,3,2,15)}
#             with dP = eta^e (t-A)^(2i-s)(t-B)^(i-s) R(t), deg_t R = 1
#         (3) A_s[dP] + B_s[c_g p^(r-i)((r/i)dP + Z)]
#             == c_g p^(r-1)(DF p Z' - i(DF-s) p' Z)   for a 3-term Z
# observed:  toy1 residual: {}   toy2 residual: {}   toy3 residual: {}
#            toy4 residual-formula check: {}   ALL_ABSORPTION_CHECKS_PASS
```

### 8.5 Disposition of `J = 1`

Answer to the trichotomy of the brief: as a *numerical* system the
convolution **cannot be formed** from the frozen basis (no exact pair,
support, or completion is supplied; `(r, c_g)`, contamination, caps all
unpinned); as a *symbolic* system it can be formed exactly (§2.3) and then
provably **merely couples** the interpolation freedom to unknown g-side
pieces (Theorem B), with a real but lower-order-only cascade (§8.3). It
does not remove the freedom `R_k(A), R_k(B)` at the available orders.

## 9. Q8 — the smallest safe `TD12-BCHILD/v1` interface

```text
TD12-BCHILD/v1 :=
(a) inputs   : PairRef(f,g) with exact completion at the cell chart
               (Not 3.9 truncation), the g-side initialization
               (k_0, l_0, s_0)  [equivalently (r, c_g) per cell],
               the window contact ledger { kappa_F(u - v) <= depth } with
               coefficient data, and the caps (deg_y f, deg_y g);
(b) state    : per cell (nu_F, kbar_F, D_F = nu_F i, i, p, P_0 = p^i,
               G_0 = c_g p^r); pieces (P_a, G_a)_{a <= s}; gauge =
               unit/dilation/deck + the matched-pair kernel of Theorem B
               (normalization = fix a complement of it, e.g. minimal-degree
               g-side response);
(c) outputs  : v_B = (v_{B,k})_{k=1..i} at the trunk;
               v_{S_1}, v_{S_2} at the sibling (evaluations of one P_k
               family at c_1, c_2) — NONE currently emittable; only
               v_B,0, v_{S_j,0} are licensed (values in §4, §5.2);
(d) states   : INIT_MISSING(r, c_g | contacts | caps);
               RESONANCE(s in nu_F N: new g-side gauge);
               RHS_LANDING(s = D_F + D_g - kbar_F);
               CASCADE_DIVISIBILITY_FAIL / CASCADE_COKERNEL_FAIL
               (typed kill candidates on supplied data);
               DELAY/NORMALIZATION(level > 1 only; level 1 structurally
               clean, §6);
(e) consumers: B depth-24 gate (24 levels, split first allowed at 25);
               sibling twin depth-16 gates (2 x 16 levels) — both
               necessary-only, both blocked on (a).
```

**No standalone software implementation is currently licensed.** The only
computable content (the identities of §8) is already verified; an `E_s`
engine without (a) could emit nothing except manufactured vectors, which
the brief forbids. The crosspoll's planned "perturbed recurrence
coefficient" control is unformulable for the same reason; its "a split
`C_1` must violate `J = 1`" control is *false as stated* at level 1 — a
split `C_1` violates the reviewed `N = i` budget lock, not the level-1
Keller convolution (Theorem B) — and this correction is part of the safe
interface.

## 10. Scope firewall

Not claimed: any value of `v_{B,k}` or `v_{S_j,k}` for `k >= 1`; any new
exit charge (the charges 8 and 4+4 are cited from their reviewed reports,
not re-derived); a germ; a Keller pair or its existence; a counterexample;
a landing; a panel exclusion or degree bound; `G2-BD`/`G2-PSC`; any JC2
consequence. The reviewed route theorems (trunk T1, B-charge 8, sibling
charge 4+4, sibling T1) are consumed at their recorded scopes with their
recorded repairs. The cascade of §8.3 is a candidate future lane, not a
result. `jc2-lean` was not touched in any way. No file other than this
report was written; nothing was committed or pushed.

## Seal

Git basis: `76c746f698103d20019bfeb72654a361ccc5371d`, verified at session
start and re-verified immediately before this seal (HEAD unchanged). This
lane wrote exactly one file: this report (scratch confined to `/tmp`).
Concurrent lanes deposited unrelated working-tree deltas during the
session; none were read, none were touched, and all sixteen manifest
hashes re-verified `OK` after those deltas appeared.

Pre-read and pre-verdict source hashes: identical, all sixteen, exactly as
listed in §0 (recomputed twice; second run immediately before this seal).

Body = all bytes of this file before the literal `## Seal` heading.

report_body_bytes = 33565
report_body_sha256 = d5b099c2627b86d11345b8283080fcd746c1a0352cc8058182951710e5065feb
