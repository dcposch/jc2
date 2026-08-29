# Hostile review: TD12-GLOBAL-SOURCE-BRIDGE-B/v1 (Fable 5 primary)

Reviewer: **Grok 4.6** (xAI), equal-standing independent hostile replay,
different model from the Fable 5 producer and from the later Sol 5.6
endpoint note.
Date: 2026-08-29.
Frozen campaign basis, verified at session start and again before sealing:

```text
92ebe92ad5986a47f01af9ed901260595dfed869
```

Unique marker:
`GROK46-92E-B25-FABLE5-HR-20260829-NU25-KBAR17`.

Charged target (Fable 5 primary, not promoted):

```text
0175063f5dcef9c3ba1c70d3ad883ad28f8757d514ec387b968b29324272274b
  xmodel/td12-global-source-bridge-b-fable5-92e-20260829.md
body 39510 bytes
  539ecec1d4255067a7819bb7577e69809a1b4f0800ab8e8313d1ad026fa58278
```

Adversarial comparison only, not proof (later independent Sol note):

```text
1272b394387d744ae065680c8327ff79d0179fb994c6d03d6d8c27d41d371c61
  xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md
body 15383 bytes
  36381aca4e450047507d46cbf9f2c1a1f17a6f4d4fd3333e372b491f28f8de41
```

Worked only in `/Users/dc/code/math/jc2`. No access of any kind to
`jc2-lean`. No web, AWS, remote shell, heavy CAS, canonical/ladder/case/ops
edit, commit, or push. Exact desk algebra plus one stdlib `Fraction`
corroboration under `/tmp/b25bridge_hr/`. One repository file written: this
review.

`charge_basis=ABSENT`

## Verdict

**PASS_WITH_REPAIR**

The load-bearing algebra of the landing operator on the reduced B-cell
polynomials is correct: identically

```text
25 p q' - 17 p' q  =  25 p ( A B + (8B - 9A) t )
```

with `' = d/d eta`, `p = (t-A)^2(t-B)`, `q = eta(t-A)(t-B)`, `t = eta^{25}`.
Solvability of the cleared landing ODE in `C(eta)` is therefore equivalent
to `8B = 9A`, and on that locus the on-weight solution is unique of the
displayed scale `gamma`. Homogeneous tops of the reduced deviation below
`s*` are forced into `25 Z`, the greedy ledger is finite by slot count, and
the top drop of the reduced deviation cannot skip the unique inhomogeneous
order `s* = D_F + D_g - kbar_F`. Chart pieces of an actual pair, given a
named B occurrence, are finite polynomial functionals of the pair and the
Puiseux prefix.

The report overstates functoriality of the GGV interface constructor,
normalizes `s_0 = c_g^2` while keeping `lambda_f` explicit, calls N1 the
exact nonabsorbability mechanism rather than the sufficient route datum,
identifies the landing ODE with terminal Proposition 8.1(iv) as objects
rather than as solvability conditions on the same reduced `(p,q)`, and
writes the C4 residue 1-form with an extra `p^{i-1}` even at `j = 17`.
Theorem B remains outline-tier except for the trivial fixed-`Delta`
algebraic Keller locus. None of those defects kills the C1–C3 core after
the repairs below.

Nothing here is an occurrence, a serialized source value, a degree cap, a
gate verdict, a tree-landing/coverage theorem, a uniform packet, or a JC2
conclusion.

| # | Charge | Verdict |
|--:|---|---|
| A.1 | `PairRef_B = (f,g)` under `J=1` and not an automorphism | **CONFIRMED** (tautology of the repaired T1 hypothesis of `ladder/REDUCTION.md`) |
| A.2 | Completion `iota_S` functorial from the pair via interface Theorem 2.1 / Prop 3.1 | **REPAIR**: functorial from `(pair, a, S)`, by native Newton–Puiseux / Sigray Notation 3.9, not by the GGV-to-tree interface and its rectangle / tower-gap / source-map riders |
| A.3 | `P_k`, `G_k` exact polynomial functionals of coefficients plus finite prefix; finitely many nonzero | **CONFIRMED** on an actual polynomial pair, after a named occurrence and chart |
| A.4 | First tower step `(k_0,l_0,s_0) = (2,3,c_g^2)` | **REPAIR**: `(2,3)` confirmed from the type pin `r/i = 3/2`; `s_0 = c_g^2 / lambda_f^3` unless the gauge `lambda_f = 1` is fixed |
| A.5 | `e_k ≡ 22k (mod 25)`, floors (V), extraction (C), `v_{B,0}` | **CONFIRMED_CONSUMED** (bchild / discriminator / trunk; not re-proved here) |
| A.6 | Ledger and `T = gamma q p^{-i}` as Theorem-A fields | **CONFIRMED** after C1–C3, as greedy-canonical functionals of the same witness |
| A.nu | `nu_F = 25`, `kbar_F = 17`, `kappa_F` kept distinct from both and from graded index `k` | **CONFIRMED** in formulas; D_F = 25 i uses `nu_F`, RHS/`gamma` keep `kappa_F` |
| Bound | `K_h = D_h + (kappa_F - kbar_F) deg_y h` | **CONFIRMED** for `h in C[x,y]`, prefix exponents `> -u`, and `kappa_F > kbar_F` (so `u = 1 - kbar_F/kappa_F > 0`) |
| B | `Occ_Delta` constructible, fields algebraic after etale/deck | **OUTLINE** as written; only the fixed-`Delta` affine coefficient space and algebraic Keller locus are promotable. No uniform cap |
| C1.Phi | Formal `(f^F)^rho` in the graded completion, pieces in `C[eta][1/p]` | **CONFIRMED** for `i rho in Z` and finite actual `V` (polynomial `f`) |
| C1.ODE | Homogeneous top solves `D_F P_0 T' - (D_g-delta) P_0' T = 0` | **CONFIRMED** (top row of `(E_s)` uses only `P_0,T_delta`) |
| C1.rat | `T_delta in C[eta][1/p]` implies `25 \| delta` | **CONFIRMED** (`p^c in C(eta)` iff `c in Z`; weight-0 second proof) |
| C1.greedy | Strict drop increase, `m <= i+r-1` | **CONFIRMED** (distinct slots `25,50,...,25(i+r-1)`) |
| C1.fin | Infinite ledger excluded without circular use of the target row | **REPAIR** write-up: slot count already terminates C1; `g^F notin cl(Phi_F)` uses `J ≠ 0` globally, not the landing row |
| C1.exh | `Dev^{(k)} ≠ 0` | **CONFIRMED** (`J(f^F,g^F) = x^{-u} ≠ 0`) |
| C2.drop | Top drop of `Dev^red` equals `s*` exactly | **CONFIRMED** (cannot stay below on a non-multiple of 25; cannot skip `s*` or the unique inhomogeneous row of `(E_s)` empties) |
| C2.N1 | N1 is the exact nonabsorbability mechanism | **REPAIR**: the exact arithmetic is `s* ≡ -kbar_F not≡ 0 (mod nu_F)`; N1 is sufficient and happens to hold on this state |
| C3.red | LANDING equivalent to the cleared ODE `(*)` | **CONFIRMED** |
| C3.id | Identity (iii) and iff `8B=9A` | **CONFIRMED** (desk expansion plus `Fraction` corroboration) |
| C3.uniq | Unique in the on-weight ring `C[eta][1/p]` | **CONFIRMED** (kernel not in `C(eta)`; indicial forces the `q`-shape; `deg_t Ntilde >= 1` uncancelled) |
| C3.gamma | `gamma = kappa_F / (25 i lambda_f A B) = kappa_F / (1800 i lambda_f u^2)` at `(8u,9u)` | **CONFIRMED** |
| C3.8.1 | Landing row is exactly terminal Prop 8.1(iv) | **REPAIR**: unconditional solvability equivalence on the reduced trunk `(p,q)`; not an object identity with `h_F`. The `m_F=1` transgression remains conditional |
| C4.L | `L_j = 25 p (·)' + (25 i + j - 17) p' (·)` | **CONFIRMED** after clearing `i lambda_f p^{i-1}` |
| C4.ker | Kernel in `C(eta)` iff `j ≡ 17 (mod 25)` | **CONFIRMED** |
| C4.fwd | Non-resonant `T_j` unique in `C(eta)` | **CONFIRMED**; existence in `C[eta][1/p]` is free only for an actual pair, not for an arbitrary `(V)/(W)` jet |
| C4.res | Residue 1-form and two orbit conditions | **REPAIR**: displayed `(p^I T_j)' = p^{I-1} RHS_j / (25 i lambda_f)` is off by `p^{i-1}` already at `j=17`. Correct first-row form is `(p^i T_17)' = RHS_17 / (25 i lambda_f)`. Two deck-orbit conditions survive after the repair. Not an identity with cokernel `q=2` |
| C4.early | `j=17` earliest unspent route-local row | **CONFIRMED** as the first below-landing resonance, only with the envelope rider `i` even and `i >= 16` for window transparency |
| C4.cons | Residue functionals consume `P_1..P_17` and ledger constants `c_g,C_k` | **REPAIR**: in the `Dev^red` formulation they consume `P_1..P_17` and `T_0 = gamma q p^{-i}` (hence `kappa_F, lambda_f, i, A, B, p, q`); `c_g` and `C_k` appear only if one converts `T_j` back to original `G`-pieces |
| Sol.5.1 | Binomial polynomiality for every `s < nu` | **REFUTED** as a promotion: licensed range is `s <= r` with clamped floors when `s > i`. On B with `i >= 16` the two ranges meet at the window, but that coincidence is not a general theorem |
| Sol.H | Endpoint Hermite class as a rival to C2–C3 | **NOT IDENTIFIED**: Sol’s `K_(s*)` is the original-pair cross-sum; Fable’s `T` is the reduced-deviation top. Compatible, not interchangeable |
| Nov | Novelty versus frozen td12 reports | **CONFIRMED** for the C1–C4 package as a chart-completion of Prop 4.2 plus the closed form (iii); not a duplication of the window cascade or of T1 |
| Cap | CAP-B25 / OCCURRENCE-B25 / no JC2 | **CONFIRMED** as blockers / nonclaims |
| T6/T7 | Consumed as charged | **UNUSED** in the proofs; citation slop only |

## Maximum safe theorem

Fix a characteristic-zero polynomial pair `(f,g)` with `J(f,g)=1` that is
not a polynomial automorphism, Sigray-normalized of type `(2,3)`, and a
named occurrence `(a,S,F)` of the B-state
`(nu_F, kbar_F, X, M, w) = (25, 17, 25, 3, 2/3)` with
`P_0 = lambda_f p^i`, `p = (t-A)^2(t-B)`, `t = eta^{25}`, `A ≠ B`, both
nonzero, `i` even and positive, `r = 3i/2`, `G_0 = c_g p^r`, and
`kappa_F > 17`. Write `D_F = 25 i`, `D_g = 25 r`,
`s* = D_F + D_g - 17`, `' = d/d eta`. Keep `nu_F = 25`, the chart
denominator `kappa_F`, `kbar_F = 17`, and the graded drop index `k`
distinct.

Then:

1. Each graded piece `P_k`, `G_k` is a polynomial in the coefficients of
   `f` (resp. `g`) and the finite Puiseux prefix of `S` below `F`. The
   `kappa_F`-lattice index from the top is bounded by
   `K_h = D_h + (kappa_F - 17) deg_y h`.
2. In the x-graded completion of the chart, greedy subtraction of
   elements of `Phi_F` with homogeneous tops of drop `< s*` is finite,
   occupies only orders in `25 Z ∩ (0,s*)`, and cannot exhaust `g^F`.
3. The reduced deviation has top drop exactly `s*` and its top piece `T`
   satisfies the landing row of the promoted `(E_s)`.
4. In `C[eta][1/p]`, that row is solvable if and only if `8B = 9A`. On
   that locus the unique solution is
   `T = gamma q p^{-i}` with `q = eta(t-A)(t-B)` and
   `gamma = kappa_F / (25 i lambda_f A B)`.
5. For `j >= 1` the fresh operator `L_j` has a `C(eta)`-kernel iff
   `j ≡ 17 (mod 25)`. At non-resonant `j` there is at most one solution
   in `C(eta)`.

Not included: constructibility of the occurrence locus, a uniform `Delta`,
any value of `P_k` for `k >= 1`, occurrence of the B-state, a gate
verdict, tree-landing, or any identification of `T` with a coefficient of
the terminal approximate root for `m_F > 1`.

## 0. Custody

Recomputed with SHA-256 on this host before reading and again before
sealing. Every Fable-declared frozen input matched the producer’s
manifest. Body cuts of charged files are all bytes before each file’s
terminal Seal heading.

```text
0175063f5dcef9c3ba1c70d3ad883ad28f8757d514ec387b968b29324272274b
  xmodel/td12-global-source-bridge-b-fable5-92e-20260829.md
  body 39510  539ecec1d4255067a7819bb7577e69809a1b4f0800ab8e8313d1ad026fa58278
1272b394387d744ae065680c8327ff79d0179fb994c6d03d6d8c27d41d371c61
  xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md
  body 15383  36381aca4e450047507d46cbf9f2c1a1f17a6f4d4fd3333e372b491f28f8de41
7af80df724d880a47452de96a731ff1c4e17b8244fdbae8fc76eb1461e7bcc22
  xmodel/post1224-next-wave-packet-20260829T1335Z.md
  body 6730   7a6ce89e9858572b1a7e1cc3c06217145fb7f0e29f2d727b5959c8b0a0abce65
9677e2edf9848e81beac51cc9ed091c13cd934f912bc337b6ab8e25a5da86861
  xmodel/roundview-20260829T1335Z-92ebe92a.md
0f16187346628e881628d545f43eecdc26cecdd0cc908977a16f82902a91c8af
  APPROACHES.md
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900
  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
79df783a0ed9e370621e750f4e6564dc9871b53e1481898e77dcdd037711ad1c
  xmodel/td12-bchild-v1-minimal-source-packet-audit-r1-erratum-sol56-76c-20260829.md
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84
  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
  body 33565  d5b099c2627b86d11345b8283080fcd746c1a0352cc8058182951710e5065feb
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab
  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4
  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
0f5968bf0a95d15ca5e9c119044daa9470321ae4586c20af50bd03f5587ac274
  xmodel/td12-formal-cascade-rank-v1-hostile-review-opus5-ccb-20260829.md
  body 25485  66b15f5d535d68a84c1324cdea826a067ceeb25345a637a8c53e79db07b7afc9
4c3f2236a11f296f7eb194bb26e8cdc8ff0b91f10d8d7151e6314caa62629304
  xmodel/g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md
f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1
  xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md
29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b
  ladder/REDUCTION.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271
  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
```

Printed source actually used, via `pdftotext -layout` on the pinned PDF
and the stacked-fraction convention already recorded by the bchild
primary: Notation 3.9 / Statement 3.7(5) / Notations 3.10–3.11 (chart,
`d_{h,F} = j/kappa`, `D_{h,F} = kappa_F d_{h,F}`), Proposition 4.1
(`J(f^F,(g-b)^F) = xi^{-n/kappa}`), Proposition 4.2 with `h_0 = g` on
`T_a^+` and the Remark discharging (7) when `d_F > 0`, Proposition 4.4,
Proposition 8.1(i),(ii),(iv) (printed right-hand side of (iv) is the
glyph-dropped `C*` form; this review never uses that constant, only the
operator shape and the independent expansion). Campaign objects consumed
only at promoted scope: `(E_s)` and `s*` (bchild disposition §2 PASS),
order-0 `G_0 = c_g p^r` (bchild §3.1), type pin `D_g/D_F = 3/2` hence
`r = 3i/2` with `i` even (disposition repair 2), Theorem D
`e_k ≡ 22k (mod 25)`, trunk cell `p,q` and T1 ratio `B/A = 9/8` with
`C_iv = (25/17) A B`, N1 `gcd(17,25)=1`, `P_0 = lambda_f p^i`, formal
envelope through `s <= r` (coordinator integration §§1–2), T2/T4 as
selection/normalization (T6/T7 are named in the producer custody list
and unused). The `i = 6n` rider is not used. The sibling `nu=17` route
is not used.

## 1. Scope firewall

Indices, kept distinct throughout:

- `nu_F = 25` is the reduced cover, `t = eta^{nu_F}`.
- `kbar_F = 17` is the tree/chart Jacobian landing invariant.
- `kappa_F` is the local Puiseux characteristic of Notation 3.11; it
  appears in `D_h = kappa_F d_{h,F}`, in the RHS of `(E_s)`, and in
  `gamma`. It is not identified with 25.
- Graded drop `k` (and `s = a+b`) counts down from the top on the
  `kappa_F`-lattice.
- `X = 25` is the cell datum `kbar_F * dp/dq`, not a second copy of
  `nu_F` in formulas.

The producer’s “forced landing” is the top drop of a reduced deviation
in the chart completion. It is not T10 book-landing, not pole coverage,
and not `FULL_ACTUAL_EXIT`. `REPRESENTATIVE` is not used. No exit price
is asserted.

Counterexamples for dropped hypotheses are collected in §10.

## 2. Theorem A

### 2.1 What is actually functorial

An actual pair plus a named occurrence `(a, S, F)` determines:

- the Sigray chart of Notation 3.9 along the branch `S` through `F`,
  `eta_F = x^{pi(F)} ( y - sum_{j < pi(F)} c_j x^{-j} )`, finite prefix
  because the exponents below `u = pi(F)` are a finite set;
- the expansion of Statement 3.7(5), finitely many polynomial pieces;
- the `kappa_F`-lattice reindexing `P_k := p_{f, n_f - Q k}` already
  reviewed with Theorem D.

That is a functor of `((f,g), a, S, F)` up to the recorded deck/Kummer
orbit. The branch `S` is part of the witness, not constructed from the
pair alone. Absence of an occurrence theorem is exactly OCCURRENCE-B25.

Interface Theorem 2.1 constructs `DPT_a` from GGV data `(K,P,Q,c,m,n,a)`
and was confirmed only with rectangle, `T_a^-` tower, and Prop 4.2-GAP
riders. Proposition 3.1 is local flagged transport of a GGV cylinder.
A T4 Sigray-normalized polynomial pair does not need that interface: the
native Newton–Puiseux tree of Sigray §§3–4 already supplies the chart
and the vertex data (2.11) along `S`. Citing the GGV interface silently
imports riders that the B-route packet does not discharge.

Repair A.2: replace the Theorem A.2 citation by Notation 3.9 + Statement
3.7(5) + standard Newton–Puiseux from a T4 pair and a named place `S`.
Do not call the completion “not an extra datum”: it is extra relative to
the pair, and not extra relative to the occurrence witness.

### 2.2 First tower step

Order 0 of `(E_s)` gives `G_0 = c_g p^r` with `r = i D_g / D_F`. The
promoted type pin is `D_g/D_F = 3/2`, so `r = 3i/2` and `i` even. Then
`l_0/k_0 = r/i = 3/2` in lowest terms, `(k_0,l_0) = (2,3)`, and
`gcd(2,3)=1` matches Prop 4.2(i). Prop 4.4 shares the step along the
`T_a^+` branch.

The scale is not `s_0 = c_g^2` once `P_0 = lambda_f p^i` is kept. Tops:

```text
f^+  ~  x^{d_F} lambda_f p^i ,     g^+  ~  x^{d_g} c_g p^r .
```

Prop 4.2(iii) at `j=0` is `(g^+)^2 = s_0 (f^+)^3`. Type pin matches
x-orders and `p`-powers (`2r = 3i`), hence

```text
s_0  =  c_g^2 / lambda_f^3 .
```

This collapses to the producer’s `s_0 = c_g^2` only in the gauge
`lambda_f = 1` used by the bchild primary (`P_0 = p^i`). Theorem C3
keeps `lambda_f` explicit, so the two normalizations collide.

Repair A.4: either fix `lambda_f = 1` globally in Theorem A, or write
`s_0 = c_g^2 / lambda_f^3`. The pair `(2,3)` does not need repair.

The sign/root choice that cancels the order-0 pieces of `g^F` and
`c_g (f^F)^{3/2}` is a finite gauge (`lambda_f^{3/2}`), recorded in the
deck/gauge orbit. That is allowed.

### 2.3 Audit-table reading

Every `TD12LocalPairJet_B` field is a functional of a hypothetical pair
**and** a named B occurrence. It is not a functional of the pair alone,
and the reduction T2/T4 does not map an arbitrary minimal pair to this
route. The producer’s slogan “the bridge is a proven functor, and only
instances, caps, and occurrence are missing” is correct only after
“functor of `(pair, occurrence)`” is inserted. `PAIRREF_ABSENT` is the
wrong name for the emission blocker; CAP-B25 and OCCURRENCE-B25 are the
right names, as the producer says in §8.

## 3. Support bound and Theorem B

### 3.1 The bound

Notation 3.9 prefix: every term of `phi` has x-exponent `-j` with
`j < u`, hence strictly greater than `-u`. For a polynomial
`h in C[x,y]` of `deg_y h = d_y`, the chart substitution
`y = phi + eta x^{-u}` is monic of degree `d_y` in `eta`. The unique
lowest x-order is `-u d_y`, attained by `eta^{d_y} x^{-u d_y}`. Leading
y-coefficients lie in `C[x]`, so they cannot push the order lower.
Statement 3.7 then puts the x-support of `h^F` in `[-u d_y, d_{h,F}]`.

On the `kappa_F`-lattice, drop from the top is at most
`kappa_F ( d_{h,F} + u d_y )`. Notation 3.11 gives `D_h = kappa_F d_{h,F}`.
The Jacobian landing of Proposition 4.1 together with the promoted
identification `s* = D_F + D_g - kappa_F(1-u) = D_F + D_g - kbar_F`
supplies `kbar_F = kappa_F (1-u)`, hence `kappa_F u = kappa_F - kbar_F`,
and

```text
K_h  =  D_h + (kappa_F - kbar_F) deg_y h .
```

Hypotheses that must be kept:

- `h` is polynomial, not Laurent (negative x-powers in the leading
  y-coefficient would break the lower bound);
- prefix exponents strictly `> -u` (Notation 3.9);
- `kappa_F > kbar_F`, equivalently `u > 0`, so the chart is at positive
  height and the second equality does not flip sign;
- off-lattice pieces vanish (Theorem D); this only improves the bound.

Counterexample if `kappa_F <= 17`: then `u <= 0` and the identity
`J_{x,eta} = x^{-u}` plus the interval `[-u d_y, d_{h,F}]` change
character. No frozen theorem pins `kappa_F` at this vertex, which is
exactly CAP-B25, but the cell arithmetic `1-u = 17/kappa_F` with
`pi(F) > 0` forces `kappa_F > 17` on any actual occurrence in `T_a^+`
of positive height. That inequality is a hypothesis of the bound, not a
cap on `kappa_F` from above.

The bound is per pair, not uniform. Sharpness can fail if the leading
y-coefficient vanishes in the chart; that only lowers `K_h`.

### 3.2 Theorem B

For a **fixed** support vector `Delta`, the coefficient space `A_Delta`
is a finite-dimensional affine space and `J(f,g)-1 = 0` is a finite set
of polynomial equations. That fragment is promotable and trivial.

That the occurrence locus `Occ_Delta` is constructible, that Newton–Puiseux
with parameters admits a finite constructible partition on which prefix
coefficients are algebraic, and that every Theorem-A field is regular
after a finite etale/deck base change, is a standard-machinery outline,
not a written proof. Tree-depth bounds “polynomial in `Delta`” are not
cited. No part of that outline is promoted here.

The union over `Delta` is not finite-dimensional. `ladder/REDUCTION.md`
T10: no upper bound on degree-type complexity. Bezout
`td = deg f deg g - sum i_p` at fixed `td = 12` allows unbounded
`(deg f, deg g)` once intersection mass at infinity grows. The producer
correctly names this CAP-B25 and does not grant a uniform packet. Do not
silently promote anything past the per-fixed-`Delta` algebraic Keller
locus.

## 4. Theorem C1

`f^F` of an actual polynomial has finitely many pieces, so
`V = sum_{k>=1} (P_k/P_0) x^{-k/kappa_F}` is a finite sum. For
`i rho in Z`, `(f^F)^rho := lambda_f^rho x^{rho d_F} p^{i rho} (1+V)^rho`
is a well-defined graded formal series: at each x-order only finitely
many binomial terms contribute, and each piece lies in `C[eta][1/p]`.
The ring is a `Q`-algebra, so the chain rule gives
`J(f^F, (f^F)^rho) = 0`; continuity in the graded topology extends this
to the closure of `Phi_F`. Finite sums of such elements remain in
`C[eta][1/p]` on each grade. Weight 0 of `p` plus Theorem D on the
`P_k/P_0` factors preserves `e ≡ 22 * (drop) (mod 25)`.

Let `Dev` have top drop `delta < s*` and top piece `T_delta ≠ 0`. The
row of `(E_s)` at `s = delta` involves only `a=0`, `b=delta`, because
any `a >= 1` would require `b = delta - a < delta`, below the top of
`Dev`. Homogeneity of that row is the ODE
`D_F P_0 T' - (D_g - delta) P_0' T = 0`. Solutions are
`C p^{(D_g-delta)/25}`. Rationality in `C(eta)` requires the exponent
in `Z`. Combined with `25 | 25 r`, this is `25 | delta`. The independent
weight argument: a pure `p`-power has weight 0, while `T_delta` has
weight `≡ 22 delta (mod 25)`, and 22 is invertible mod 25, so again
`25 | delta`. Pieces of `g^F` are polynomials and pieces of `Phi_F` lie
in `C[eta][1/p]`, so `T_delta` does too.

Greedy subtraction of `C (f^F)^{(25 r - delta)/(25 i)}` matches the top
and strictly increases the drop. Distinct positive multiples of 25
strictly below `s* = 25(i+r)-17` number at most `i+r-1 = 5i/2 - 1`.
If some `Dev^{(k)} = 0`, then `g^F in Phi_F` and `J(f^F,g^F)=0`,
contradicting `x^{-u}`.

The producer’s last paragraph argues an infinite ledger by sending the
top below the landing order. That sentence is the C2 comparison, not a
C1 ingredient. C1 items 1–3 are already finite by the 25Z slot count
and do not mention `s*` except as the cutoff of “homogeneous”. The
honest non-circular closure fact is: `J` annihilates `cl(Phi_F)` and
does not annihilate `g^F`, so `g^F` is not a graded limit of `Phi_F`
elements. Repair the parenthetical; do not reopen C1.

Dictionary to Prop 4.2: `h_1 = g^2 - s_0 f^3` is the first resolvent
and, in the completion,
`h_1^F = Dev^{(0)} · (g^F + c_g (f^F)^{3/2})` after the `lambda_f`
repair of `s_0`. Then `nu_F | D_{h_1,F}` is C1 at the first slot.
This is a chart-completion of the tower mechanism, not a rival.

## 5. Theorem C2

After C1, every homogeneous absorbable top below `s*` has been removed.
A remaining top drop `delta < s*` with `25` not dividing `delta` is
impossible by C1. If the top drop were strictly larger than `s*` (no
piece of `Dev^red` with `b <= s*`), the convolution at `s*` would have
`a + b = s*` with `b >= s*+1`, hence `a <= -1`, empty. But
`J(f^F, Dev^red) = J(f^F, g^F) = x^{-u}` has its unique nonzero row at
`s*` with value `kappa_F ≠ 0`. Contradiction. Therefore the top drop is
exactly `s*`, the landing row is the displayed (LANDING), and `T ≠ 0`
both as a top piece and because `T=0` would again empty the row.

This uses the promoted identity `(E_s)` as the unique inhomogeneous
order. It does not assume the conclusion of C2 to prove C1.

Arithmetic: `s* = 25(i+r)-17 ≡ 8 (mod 25)`. In general
`s* ≡ -kbar_F (mod nu_F)`. Absorbability of the landing would require
`nu_F | s*`, i.e. `nu_F | kbar_F`. N1 `gcd(kbar_F, nu_F)=1` with
`nu_F >= 2` implies that, and on this cell `gcd(17,25)=1` is equivalent
to `25` not dividing 17. The exact mechanism is the congruence
`s* not≡ 0 (mod nu_F)`, not the slogan “N1”. Repair the slogan.
Counterexample to the slogan as a general identity: `kbar=10`, `nu=25`
has `gcd=5 ≠ 1` but the landing is still nonabsorbable.

C2 is not a Sigray pole-landing theorem and does not manufacture an
occurrence.

## 6. Theorem C3

### 6.1 Independent expansion

Let `W = (t-A)(t-B)`, `p = (t-A)^2(t-B) = (t-A) W`, `q = eta W`,
`t = eta^{25}`. Then `dt/d eta = 25 eta^{24}`,

```text
q'  =  W + eta W_t · 25 eta^{24}  =  W + 25 t W_t ,
p'  =  p_t · 25 eta^{24}  =  (25 t / eta) p_t ,
p' q  =  (25 t / eta) p_t · eta W  =  25 t p_t W .
```

Hence

```text
25 p q' - 17 p' q
  = 25 p (W + 25 t W_t) - 17 · 25 t p_t W
  = 25 [ p W + 25 t p W_t - 17 t p_t W ] .
```

Now `p_t / p = 2/(t-A) + 1/(t-B)`, so

```text
t (p_t / p) W  =  t ( 2(t-B) + (t-A) )  =  t (3t - A - 2B) .
```

And

```text
W + 25 t W_t
  = (t-A)(t-B) + 25 t (2t - A - B)
  = t^2 - (A+B) t + A B + 50 t^2 - 25(A+B) t
  = 51 t^2 - 26(A+B) t + A B .
```

Subtract `17 t (3t - A - 2B) = 51 t^2 - 17(A+2B) t`:

```text
51 t^2 - 26(A+B) t + A B - 51 t^2 + 17(A+2B) t
  = ( -26 A - 26 B + 17 A + 34 B ) t + A B
  = (8 B - 9 A) t + A B .
```

Therefore, identically in `C[A,B,t]`,

```text
25 p q' - 17 p' q  =  25 p ( A B + (8 B - 9 A) t ) .
```

Factors: the outer `25`, the factor `p`, and the linear
`A B + (8B-9A) t`. The cell identity `= 25 A B p` holds if and only if
`8B = 9A`. At the promoted ratio `A = 8u`, `B = 9u`,
`A B = 72 u^2`. The trunk consumer’s `C_iv = (25/17) A B` satisfies
`17 C_iv = 25 A B`, so the same identity is `= 17 C_iv p`. The linear
condition `(225/17) A - (200/17) B = 0` of the trunk consumer is
`(8B-9A)=0` times `-25/17`, as the producer says.

### 6.2 Reduction of LANDING, uniqueness, scale

`P_0 = lambda_f p^i` in (LANDING), divide by `i lambda_f p^{i-1}`:

```text
25 p T' + (25 i - 17) p' T  =  (kappa_F / (i lambda_f)) p^{1-i} .     (*)
```

Kernel: `T = C p^{-(25 i - 17)/25} = C p^{-i + 17/25}`, not in `C(eta)`
because `25` does not divide 17. Uniqueness in `C(eta)` and therefore in
`C[eta][1/p]` and in the weight-`1` subspace.

Leibniz, independent of `i`:

```text
25 p (q p^{-i})' + (25 i - 17) p' (q p^{-i})
  = (25 p q' - 17 p' q) p^{-i} .
```

On `8B=9A` the right-hand side is `25 A B p^{1-i}`. Substituting
`T = gamma q p^{-i}` into `(*)` therefore pins

```text
gamma · 25 A B  =  kappa_F / (i lambda_f) ,
gamma  =  kappa_F / (25 i lambda_f A B)
       =  kappa_F / (1800 i lambda_f u^2)   at (A,B)=(8u,9u) .
```

The two expressions `kappa_F / (17 i lambda_f C_iv)` and
`kappa_F / (25 i lambda_f A B)` agree because `17 C_iv = 25 A B`.

Indicial at eta-roots of `p` (each A-root of `t-A` is simple in `eta`,
and `p` has eta-order 2 there; each B-root has eta-order 1). Leading
coefficients `25 sigma + 2(25 i - 17) ≡ -9 (mod 25)` at A and
`25 sigma + (25 i - 17) ≡ -17 ≡ 8 (mod 25)` at B, both nonzero, so the
indicial never degenerates. Orders: `sigma = 1-2i` at A-roots,
`sigma = 1-i` at B-roots. Thus `N = T p^i` is regular with simple zeros
exactly on the fifty roots of `W(eta^{25})`. Weight `e_{s*} ≡ 22·8 ≡ 1
(mod 25)` forces `N = q Ntilde(t)`. If `deg_t Ntilde = d >= 1`, the
term `625 t W Ntilde_t` has degree `d+2` with leading coefficient
`625 d ≠ 0`, uncancelled by `25(AB+(8B-9A)t) Ntilde` of degree `<= d+1`.
Hence `Ntilde` is constant, `(8B-9A) Ntilde = 0`, and
`25 A B Ntilde = kappa_F / (i lambda_f)`. Since `kappa_F ≠ 0`,
`Ntilde ≠ 0` and solvability holds iff `8B=9A`.

This is unconditional algebra on the declared on-weight localization
`C[eta][1/p]` with the weight-`1` constraint forced by Theorem D at
drop `s*`.

### 6.3 Relation to Proposition 8.1(iv)

The printed 8.1(iv) is an identity for the **terminal** approximate-root
polynomials `(p,q)` of `h_F`. The trunk consumer already specialized it
on this cell to `rho p q' - p' q = C_iv p` with `rho = 25/17`. C3 uses
the same reduced shape `q = eta(t-A)(t-B)`, which is the unique weight-1
polynomial with simple zeros on the roots of this `p` (R1.0), and shows
that the **original-pair** landing ODE for `Dev^red` is solvable in the
on-weight ring iff that same ratio holds.

That is a solvability equivalence on the reduced trunk `(p,q)`, licensed
by 8.1(i) supplying the top of `f^F` as `lambda_f p^i` with this `p`.
It is **not** an identification of `T` with a coefficient of `h_F`.
Sol §5.2 is right on the stronger object-level claim: if `m_F = 1`, so
`h_1 = h_F`, then `J(f,h_1)=2g` and the first surviving coefficient of
`h_1` at grade `s*` has the form `p^{i/2} q`, and the distant row
literally becomes T1 after removing the homogeneous common power. The
frozen route does not instantiate `m_F=1` or the intermediate resolvent
maps. Repair the producer slogan “the landing row is exactly Proposition
8.1(iv)” to “solvability of the landing ODE on this reduced `(p,q)` is
equivalent to the already-promoted T1 ratio”. No naive `s*`-attack with
route-local data kills the cell; that qualitative corollary survives.

## 7. Theorem C4

Clearing `i lambda_f p^{i-1}` on row `s*+j`, `j >= 1`, produces

```text
L_j[T_j]  =  25 p T_j' + (25 i + j - 17) p' T_j
          =  25 p^{1-I} ( p^I T_j )'
```

with `25 I = 25 i + j - 17`. The kernel exponent
`(17 - 25 i - j)/25` lies in `Z` iff `j ≡ 17 (mod 25)`. At
`j = 17 + 25 m` one has `I = i+m` and kernel `C p^{-I}`. C4(i) is
confirmed.

C4(ii): non-resonant kernel is not in `C(eta)`, so at most one solution
in `C(eta)`. For an **actual** pair a solution exists (the actual
piece). For a formal `(V)/(W)` jet, existence in `C[eta][1/p]` is an
extra condition already at non-resonant rows; do not treat it as free.

C4(iii) displayed derivative equation is wrong. The unreduced a=0
operator is `i lambda_f p^{i-1} L_j`. With
`RHS_j` the unreduced cross-sum as defined by the producer,

```text
i lambda_f p^{i-1} L_j[T_j]  =  RHS_j ,
(p^I T_j)'  =  p^{I-1} RHS_j / ( 25 i lambda_f p^{i-1} ) .
```

At the first resonant row `j=17`, `I=i`, this collapses to

```text
(p^i T_17)'  =  RHS_17 / (25 i lambda_f) .
```

The producer wrote `(p^i T_17)' = p^{i-1} RHS_17 / (25 i lambda_f)`,
which inserts an extra holomorphic vanishing factor `p^{i-1}` at every
root of `p`. Residues of `p^{i-1} RHS_17 d eta` at those roots are not
the residues of `RHS_17 d eta`. For `i >= 2` the extra factor can kill
simple and even double poles at the A-orbit and render a wrong 1-form
vacuous. Repair the 1-form before any residue expansion.

After the repair, `RHS_17` has the same weight class as the a=0 term at
`j=17`. Weight bookkeeping `≡ 22 j (mod 25)` with `22·17 ≡ -1 (mod 25)`
makes `h d eta` deck-invariant under `eta |-> zeta eta`, `zeta^{25}=1`.
Residues are constant on the A-orbit and on the B-orbit, so fifty point
conditions fold to two orbit conditions. That count uses the two
distinct t-roots; it is the same integer as the promoted window cokernel
`q=2` and is **not** that cokernel. The producer’s refusal to identify
them is correct and is kept.

Consumption, `Dev^red` language: the two repaired residue functionals
are bilinear in `(P_1,...,P_17)` and `(T_0,...,T_16)`, with
`T_0 = gamma q p^{-i}` and `T_1,...,T_16` the unique `C(eta)` solutions
of the non-resonant rows (existence in `C[eta][1/p]` only for an actual
pair). Constants consumed through `T_0` and `L_j`:
`kappa_F, lambda_f, i, A, B, p, q`. Not consumed in this language:
`c_g` and the ledger `C_k`. Those appear iff one rewrites `T_j` as
original `G_{s*+j}` minus binomial tails of the subtracted
`(f^F)^{rho_k}`.

`j=17` is the first below-landing resonance. It is the earliest
**unspent** route-local row only after the homogeneous window
`s <= 24` is spent. That uses the promoted envelope, whose rider is
`i` even and `3i/2 >= 24`, i.e. `i >= 16`. Rows `s=25,50,...,` below
`s*` are spent as C1 gauges, not as leftover constraints. Without the
envelope rider the window itself is not known to be polynomially
transparent (correct binomial range `s <= r`; see §8). Repair §5 of the
producer to carry `i >= 16` when calling `j=17` the earliest unspent
row.

For actual pairs the residue conditions at `j=17` are identities
(existence of `T_17`). They become a kill lane only against a formal
window class that is not already forced to satisfy them. That is the
producer’s own vacuity question and is not answered here.

## 8. Sol Hermite comparison and the binomial range

Sol’s congruence is

```text
K_(s*)  ≡  kappa_F   (mod  H_i) ,     H_i = gcd(P_0, P_0') ,
```

i.e. the original-pair cross-sum of strictly lower indices, evaluated
on the top roots, equals `kappa_F`. Fable’s `T` is the top piece of
`g^F - sum C_k (f^F)^{rho_k}`, not `G_{s*}`. The two splittings are
compatible and are not the same object. Sol’s Hermite class does not
prove or refute C2–C3. It is not used as proof.

Sol §5.1 claims `G_s = G_s^{bin}` for `1 <= s < nu` because the
polynomial kernel of `B_s` is empty off `nu Z`. The kernel argument
shows uniqueness in `C(eta)` off those slots. It does **not** prove
that the binomial piece is polynomial. The promoted formal envelope
(coordinator integration §2, Opus C6) licenses a polynomial g-side
response through

```text
s  <=  r  =  3 i / 2 ,
```

with the clamped floors `F_s` mandatory when `s > i`. Direct-entry
`i = 6n` is not a premise of that theorem.

Absent a direct-entry rider, the correct range is `s <= r`, not
`s < nu`. On the B route with `i >= 16` one has `r >= 24 = nu_F - 1`,
so `s <= r` covers the window `s <= 24`, and `s < nu` meets it
numerically. That coincidence is not a licence to write `s < nu` in
general. Counterexample: `i=2`, `r=3`, `nu=25`. Promoted polynomiality
stops at `s <= 3`. Sol’s `s < 25` would claim window transparency at
depth 24 for this `i`, which the envelope explicitly does not grant
(B window transparent only for `i >= 16`).

Fable C1’s rationality lemma is consistent with uniqueness in `C(eta)`
off `25 Z` and does not by itself upgrade binomial polynomiality past
`s <= r`. Do not read C1 as a replacement for the envelope rider.

## 9. Novelty and forbidden duplication

Frozen-history search in `xmodel/` td12 reports and the charged ladder
files: the formal-cascade producer/review/integration prove window-side
`J=0` transparency and name `s*` as the future inhomogeneous target;
the bchild primary’s Theorem B is own-order absorption **in the
window**; the trunk consumer solves 8.1(iv) on the reduced cell. No
frozen file constructs `Phi_F`, the 25Z ledger, the forced deviation
top at `s*`, the closed form `AB+(8B-9A)t`, the scale `gamma`, or the
below-landing resonance analysis.

C1–C2 are honestly a chart-completion of Prop 4.2, new in the `mod
nu_F` packaging. C3(iii) is a compact rewriting of the trunk consumer’s
quadratic, not a second T1 solve; the novelty is the identification of
that quadratic as the landing ODE for `Dev^red`. C4’s resonance is new
and must be consumed only after the 1-form repair. The universal-parameter
Theorem B is the packet’s own sanctioned construction, executed at
outline tier. Window-cascade descendants stay stopped. B and S are not
identified. Finite-pole scope and TWIN-ORDER are not touched.

The later Sol endpoint note is independent, narrower on the original
cross-sum, and over-broad in §5.1. It is not prior art for this primary
and is not a duplication of it.

## 10. Exact repairs and counterexamples

1. **A.2 constructor.** Cite Notation 3.9 / St 3.7 / native NP from a
   T4 pair and named `(a,S,F)`. Drop GGV interface Theorem 2.1 /
   Proposition 3.1 as the existence vehicle (riders not discharged).
2. **A.4 scale.** `s_0 = c_g^2 / lambda_f^3`, or fix `lambda_f = 1`.
3. **C1 closure sentence.** Delete the landing-row parenthetical;
   finite 25Z slots terminate the homogeneous ledger; `J ≠ 0` excludes
   `g^F in cl(Phi_F)`.
4. **C2 slogan.** Nonabsorbability is `s* not≡ 0 (mod nu_F)`. N1 is
   the sufficient route datum.
5. **C3 slogan.** Solvability equivalence on reduced `(p,q)`, not
   object identity with terminal 8.1. Keep `m_F=1` as a conditional
   lemma (Sol §5.2).
6. **C4(iii) 1-form.** Replace by `(p^i T_17)' = RHS_17 / (25 i lambda_f)`
   at `j=17`; in general
   `(p^I T_j)' = p^{I-1} RHS_j / (25 i lambda_f p^{i-1})`.
7. **C4 consumption / earliest-row rider.** `Dev^red` functionals do
   not consume `c_g, C_k`. Carry `i` even and `i >= 16` when calling
   `j=17` the earliest unspent row.
8. **Theorem B.** Promote nothing past the fixed-`Delta` algebraic
   Keller locus. CAP-B25 stays the emission blocker.
9. **Binomial range.** Never write `s < nu` without the rider
   `r >= nu-1` (i.e. `i >= 16` on B) plus the envelope’s `s <= r`
   polynomiality. Drop T6/T7 from the charged list or use them.

Counterexamples for missing hypotheses:

- No occurrence `(a,S,F)`: a type-`(2,3)` T4 pair need not realize
  `(25,17,25,3,2/3)`. The packet is undefined. (OCCURRENCE-B25.)
- `lambda_f` kept and `s_0 = c_g^2`: `(g^+)^2 = c_g^2 (f^+)^3` fails
  unless `lambda_f^3 = 1`.
- `8B ≠ 9A`, e.g. `(A,B)=(8,7)`: quotient is `56 - 16 t`, not `56`;
  `(*)` has no solution in `C[eta][1/p]`.
- `i=2` (even but `< 16`): `r=3 < 24`; polynomial binomial response
  only through `s <= 3`; window `s <= 24` is not transparent.
- `kappa_F = 17`: `u=0`; support-bound second equality and
  `J = x^{-u}` degenerate.
- Uniform `Delta` at fixed `td=12`: Bezout permits unbounded degrees;
  `Occ = union_Delta Occ_Delta` is not a finite-dimensional scheme.
- `m_F > 1`: terminal `q` is a polynomial in `h_F`, not in
  `g - c_g f^{3/2}`; object-level identification with 8.1 fails.
- Formal `(V)/(W)` jet at a non-resonant below-landing row: unique
  `C(eta)` candidate need not lie in `C[eta][1/p]`.
- Displayed C4 1-form at `i=2`, simple pole of `RHS_17` at an A-root:
  `p^{i-1} RHS_17` is holomorphic there, producer-residues vanish,
  correct residues of `RHS_17` need not.

Mutations of the C3 identity (nonzero residuals): `kbar -> 16` produces
quotient `3 t^2 - 26 t + 72`; `nu -> 24` produces `-2 t^2 + 17 t + 72`;
dropping the `25 t p W_t` term produces `-50 t^2 + 425 t + 72`. All
detected.

## 11. Smallest licensed descendant

**`TD12-B25-RESROW/v1`**, desk only, B-route only, frozen basis only,
after installing repairs 6–7:

Expand the corrected recursion through `j=17` on the reduced cell
`A=8u`, `B=9u`. Emit the two orbit residue functionals of
`(p^i T_17)' = RHS_17 / (25 i lambda_f)` as explicit finite bilinear
forms in `(P_1,...,P_17)` and the rigid tail `T_0 = gamma q p^{-i}`,
with every `(kappa_F, lambda_f, i, u)` dependence typed. State the
existence domain of `T_1,...,T_16` (actual pair vs formal `(V)/(W)`
jet). Vacuity verdict on the admissible class, fail-closed as
`RESROW_VACUOUS_ON_CLASS`, `RESROW_NONVACUOUS`, or
`EXPANSION_BLOCKED(missing datum)`. No caps, no invented jets, no
value emission, no sibling objects, no window-cascade reopening.

A C3/C4 erratum that only installs repairs 2–7 is smaller as a document
and is a prerequisite, not a substitute, for that expansion.

## 12. Nonclaims

Not claimed by this review and not licensed from the producer: any
occurrence of the B-state; any serialized `PairRef`; any value of
`P_k` or `v_{B,k}` for `k >= 1`; any uniform degree or `kappa_F` cap;
any gate verdict or level advance; any tree-landing, coverage, or T10
statement; any identification of B with S; any kill of the B route; any
new exit price; any `td` bound, panel closure, G2-PSC/G2-BD progress,
counterexample, or JC2 conclusion. Theorem B stays outline. `jc2-lean`
was not entered.

## 13. Printed corroboration (not proof-of-record)

Stdlib `Fraction` only, scratch `/tmp/b25bridge_hr/`. Desk expansion of
§6.1 is the proof; the run is a mutation control.

```text
identity 25pq'-17p'q = 25 p (AB+(8B-9A)t):
  T1 (A,B)=(8,9):     rem {}  quot {0: 72}
  T1 (A,B)=(24,27):   rem {}  quot {0: 648}
  T1 (A,B)=(-8,-9):   rem {}  quot {0: 72}
  six off-ratio (A,B) in {(2,5),(3,1),(7,11),(1,2),(10,3),(5,8)}:
                      rem {}  quot {0: AB, 1: 8B-9A} exactly
mutations:
  kbar->16:  quot {2: 3, 1: -26, 0: 72}   (breaks)
  nu->24:    quot {2: -2, 1: 17, 0: 72}   (breaks)
  drop 25 t p W_t: quot {2: -50, 1: 425, 0: 72}  (breaks)
  (A,B)=(8,7): quot {1: -16, 0: 56} = AB+(8B-9A)t, and 8B≠9A
conjugation 25p(q p^{-i})'+(25i-17)p'(q p^{-i}) == (25pq'-17p'q)p^{-i}
  at i=2, (A,B)=(8,9), eta in {2,3,-1,1/2}: residual 0
L_17 Leibniz 25 p^{1-i}(p^i R)' == 25 p R' + 25 i p' R
  at i=2, R=eta+1, eta in {2,3,1/2}: residual 0
arithmetic: s* ≡ 8 (mod 25); e_{s*} ≡ 22*8 ≡ 1 (mod 25);
  22*17 ≡ -1 (mod 25); gcd(17,25)=1; 17 C_iv = 25 AB;
  gamma denominator 25*72 u^2 = 1800 u^2  all True
```

## Seal

Git basis `92ebe92ad5986a47f01af9ed901260595dfed869`, HEAD re-verified
unchanged immediately before sealing. Marker
`GROK46-92E-B25-FABLE5-HR-20260829-NU25-KBAR17`.
`charge_basis=ABSENT`.

Body = all bytes of this file before this terminal Seal heading.

report_body_bytes = 41244
report_body_sha256 = dab4058f598c05dbd5d00448c7e36c56dbbbfa7869ec3df3189f4640876a85b4
