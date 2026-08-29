# Hostile review — Grok 4.6 td=8 parametric Prop. 8.1(iv) theorem

Lane: Fable 5, different-model adversarial referee. Date: 2026-08-29 UTC.
Target: `xmodel/m2-td8-prop81iv-parametric-primary-grok46-20260829.md`.
Packet: `cases/m2_td8_prop81iv_parametric_grok46_20260829/`.

No web, AWS, commit, push, canonical edit, heavy CAS, or long/high-memory
process. No access of any kind to `jc2-lean`; no global `git status`; no
workspace-wide search. Arithmetic is desk `int`/`Fraction`. The packet and
the target were not modified; scratch ran in `/tmp/f5rev`. The active Sol
and Opus Prop. 8.1 consumer reports were not read at any point; my
derivation was completed first and they were never needed.

Every assertion of the target was treated as an allegation and re-derived
from the printed statements and the charged cell.

---

## 0. Verdict

**`PASS_AT_LOCAL_PROP81IV_SCOPE`.**

The target's theorem is correct as stated, at exactly the scope it
states. For every integer `t >= 0`, the R2.2-typed equal-join reduced
cell (`nu = 4+3t`, two nonzero `nu`-orbits of multiplicity 3,
`eps = k = lex = 0`, `dp = 6 nu`, `dq = 2 nu + 1`) admits an admissible
solution of the printed identity Prop. 8.1(iv) — `delta p q' - (1-u) p' q
= ⊖ p`, `⊖ != 0` — if and only if the two orbit values are opposite and
nonzero, uniquely up to the one remaining scale, with
`p = (eta^{2 nu} - a^2)^3`, `q = ⊖ eta (eta^{2 nu} - a^2)`,
`ctilde = rho * pi != 0`, `rho = 6 nu/(2 nu + 1)`. No exceptional `t`,
no log/residue obstruction. Every printed side condition holds
identically in `t`. My clean-room proves the uniqueness in a **stronger**
form than the packet tests: `q` completely free of assumed shape (exact
kernel computation), not only the `(sigma, pi)` scan.

The `PARTIAL` half is also correct and required: nothing here is an
exact-lambda, transport/landing, realizability, degree-bound, or JC2
statement, and the target claims none of them.

This PASS authorizes canonical promotion of **only** the local formal
theorem (the vertex-local Prop. 8.1(iv) survival family and its rigidity
statement). It authorizes **no AWS launch** and no promotion of any
route-, lambda-, landing-, or JC2-tier claim.

Findings: zero CRITICAL/HIGH/MEDIUM. Two LOW diction/attribution slips
and four notes, none with verdict impact (§9).

---

## 1. Custody

Independently recomputed:

```text
target full   2d9fa6fa73da2f8d276301ef9f2153eb305f3e87e5bb307d127ee4adcfcf94a1
target body   cc7035dec2949f674064f7495c209abbf1037dee3179f1abd876a8e292366416
              (first 17822 bytes; marker line + trailing newline included — matches
              the target's own appendix)
ce8bfc54d1cec0057dd840fb9f1b4613332cf4c42199e579cbd855d46a6ec320  prop81iv_td8_affine.py
46ab374fa7ae64a7c9b270e7c74829ded9c09d876e8ef319376b8f2a96188d64  test_prop81iv_td8_affine.py
024438a665672115d2b7f8f15ba01322e61a66d0b0d7cb23f51078a467e262c3  README.md
a3d59f3b75255056847d8b7d871996ae0d8c961c225df5cc9b29fd9dc585f513  charged JSON stdout
6935db46999f1da2640154ab8155223df875b8d4609851cb7e6a6094c6f107a8  certificate (in-stdout)
```

all matching §1 of the target. D2 inputs re-hashed and matching:
Sol producer full `9a778862...5a`, body `bd35c43b...d7`; Grok D2 review
body `a53a78db...49`.

Files read for mathematics, and only these: the target and packet; the
Sol D2 producer and its Grok hostile review (both hashes above; the D2
route typing is used as reviewed input, not re-proved); `refs/sigray_full.pdf`
pages containing Not. 8.1 / St. 8.1 / Prop. 8.1 + proof / St. 8.2 + proof /
St. 8.3 (pdf pp. 39–41), Prop. 4.6 with (11)–(17) (p. 23), Cor. 6.1 +
proof (p. 32 region), St. 3.16–3.18 + Prop. 3.2 (pp. 17–18), Not. 9.1 /
St. 9.1 (p. 48); `ladder/SHEET6-DEPTH.md` §§0–2 (i-normalization,
equal-quotient transport, DS1); `ladder/BOOK-OFFAXIS.md` §§6–7
(R1.0–R2.3) and §11 (T1); `ladder/BOOK-OFFAXIS-REVIEW.md` §0–§1 verdict
lines (R1.0/R2 CONFIRMED); anchor greps of `ladder/SHEET6-L1.md`
(family C, `B = (3/2)A`), `ladder/SHEET6-A3L1-REVIEW.md` (Front 6),
`ladder/SHEET6-MULTIPOLE.md` (MP1–MP2), `cases/l1_ode_check.py`
(family A E-form).

Ordinary and `-O` replays of the packet suite each print
`TD8_PROP81IV_PARAMETRIC_GROK46_TEST_PASS checks=1362`. The packet
contains no `assert` statements (verified), so `-O` equivalence is
structural, not accidental. The check census 1 + 81·16 + 39 + 4 + 10 +
11 + 1 = 1362 was recounted from the test source and matches.

---

## 2. The printed statements, re-read on-page

Verified verbatim against the pdf text layer (stacked-fraction hazard
respected; every load-bearing formula here is display-line, not inline
fraction):

- **Not. 8.1**: `M_F := gcd(deg p_F, deg p_{h_0,F}, ..., deg p_{h_m,F})`;
  `M*_F` omits the `h_m` term. As quoted.
- **Prop. 8.1** (`F ∈ T_a^&`, `u := pi(F)`, `i := deg(p_F)/M*_F ∈ N*`):
  (i) `(xi^delta p(eta))^i = ⊖ f_F^+`; (ii) `h_F^+ =
  xi^{1-u}(xi^delta p)^k q(eta)`, `k = i(mu_F - 1)`; (iii)
  `J(xi^delta p, xi^{1-u} q) = ⊖ xi^{delta-u} p`; **(iv)
  `delta p q' - (1-u) p' q = ⊖ p`**; (v) `M_F = gcd(deg p, deg q)`.
  The proof states `deg(p) = M*_F` explicitly, and "(iv) is a simple
  corollary of (iii)". I expanded the Jacobian myself:
  `J(xi^delta p, xi^{1-u} q) = xi^{delta-u}[delta p q' - (1-u) p' q]` —
  (iii) ⟺ (iv) exactly, as the target claims.
- **St. 8.2** (F searrow, in `V_a`, not a pole; `G = F + c`):
  `deg(q) mult(p,c) != deg(p)`, and `G ∈ T_a^&` iff
  `deg(q) mult(p,c) > deg(p)`. Its proof derives
  `deg(p)/deg(q) = delta/(1-u)` from St. 3.16 (p has more than one root)
  and (iv). As quoted.
- **Prop. 4.6**: identity (11) with the printed dichotomy — either
  (15) `deg p + deg q - 1 > mu_F deg p` and then **(16)
  `deg p/deg q = d_F/d_{h,F}`**, or (17) equality, and (16) fails.
- **Cor. 6.1** (`F ∈ T_a^& ∩ V_a \ {(0,y)}`): excludes case (17) — its
  proof shows (17) plus Prop. 6.7 would force a single root, i.e.
  `F ∉ V_a`. So the case-(16) ratio holds at every searrow `V_a` vertex.
  Transporting through (i)/(ii) (`deg p_F = i·deg p`,
  `deg p_{h,F} = k·deg p + deg q`, `d_F = i·delta`,
  `d_{h,F} = (mu_F - 1)d_F + 1 - u`, all from the printed proof) gives
  exactly `deg(p)/deg(q) = delta/(1-u)` for the **reduced** pair. The
  target's "Cor. 6.1 supplies case (16)" is a correct citation, and
  St. 8.2's proof provides an independent second route.
- **St. 3.16**: `V_{1,a} ∪ V_{2,a}` iff more than one root; the
  semi-invariance `p_F(eta) = eta^l ptilde(eta^nu)`. **St. 3.17(i)**:
  `deg(p_F) = mult(p_G, c)` for `F = G + c`. **St. 3.18**: continuation
  exists at a unique orbit representative — one tree continuation per
  nonzero `nu`-orbit. **Not. 9.1**: `Q(F) = (D_F, deg(p_F), nu_F, M_F,
  kappa_F(1-pi(F)))` — the second slot is the FULL pattern degree.
- **DEPTH §1** (promoted): i-normalization `rho_F = D_F/deg(p_F)` with
  full degree; `p_full = ⊖(xi^delta p_red)^i`; the equal-quotient
  transport `deg(p_F) = mult(p_G, c) = i_G · mu_e` on tree edges. This is
  letter-for-letter the law the target's i-chain uses.
- **R1.0 / R2.2 / R2.3 / T1** (BOOK-OFFAXIS §§6–7, §11; R1.0 and the R2
  block CONFIRMED by BOOK-OFFAXIS-REVIEW): the valuation laws, merge
  shape, proportional kill, and the single-orbit zero-chain closed form,
  as cited.

Also re-derived from scratch (no citation needed): with `⊖ != 0` and
`deg q >= 2`, identity (iv) itself forces `1-u != 0` and `delta != 0`
(either vanishing collapses (iv) to a degree-impossible equation), and
the top-degree coefficient forces `delta·dq = (1-u)·dp`. On this cell
`dq = 2 nu + 1 >= 9`, so the ratio law needs no extra hypothesis at all.

---

## 3. Charge 1 — the Prop. 8.1 polynomials and `i = 14`, not 7

**Reduced patterns.** Prop. 8.1's `p, q` are the reduced pair with
`deg p = M*_F` (printed proof) and `M_F = gcd(deg p, deg q)` ((v)).
The R2.2 merge shape on this cell (`eps = 0`, `k = 0`, `lex = 0`, two
arrivals of `mu = 3`) is `p_red = ⊖(eta^nu - c1^nu)^3 (eta^nu - c2^nu)^3`,
and R1.0 + the degree count force `q`'s shape completely: `q` is
semi-invariant (`q = eta^{e0} s(eta^nu)`, from the printed h-pattern
structure), `e0 ≡ 1 (mod nu)` with `e0 <= 2 nu + 1`, each of the 2
p-orbits must appear simply (valuation on (iv)), and `1 + 2 nu` exhausts
`dq` — so `q = ⊖ eta (eta^nu - c1^nu)(eta^nu - c2^nu)` with **the same**
orbit values, and no off-p q-root can exist. The displayed patterns are
therefore the Prop. 8.1 polynomials of the typed cell, with the orbit
values as the only unknowns. CONFIRMED.

**The exponent.** The i-chain is the promoted equal-quotient transport
law applied twice, with the reviewed census datum as seed:

```text
Q(pole) = (2, 4, 3, 2, 5)  (Not. 9.1; reviewed D2, tdu_rows(4))
  => deg(p_pole, full) = 4                    [slot 2 is FULL]
pole = A-vertex + c_P, St. 3.17(i):  4 = mult(p_A,full, c_P)
Prop. 8.1(i) at A:  mult full = i_A · (reduced mult l_A = 2)
  => i_A = 2,  deg(p_A, full) = i_A · 21 = 42
A-vertex = G + c_A, St. 3.17(i):  42 = mult(p_G,full, c_A) = i_G · mu = 3 i_G
  => i_G = 14  ∈ N*.
```

The `i = 7` reading is refuted two independent ways. (a) Forward: 7 is
`deg(p_A,red)/mu = 21/3`, a reduced-over-reduced quotient with no printed
meaning; the actual quotient identity is `deg(p_A,FULL) = i_G·mu`.
(b) Backward: if `i_G = 7` then `mult(p_G,full, c_A) = 21`, St. 3.17(i)
forces `deg(p_A,full) = 21`, hence `i_A = 1` and
`deg(p_pole,full) = 1·2 = 2 ≠ 4` — contradicting the reviewed census
Q-datum. Verified in the clean-room. Note the frame is **i-blind**:
`rho_frame = X/dp_red = (X·i)/(dp_red·i) = 2/3` for any `i`, so no frame
arithmetic can catch this error; only the St. 3.17(i) chain can. The
target's pin (`i` corrupts full-degree/`D` bookkeeping but not the
coefficient problem) is exactly right: (iv) is an identity in the
reduced pair and never consumes `i`. CONFIRMED, `i = 14`.

---

## 4. Charge 2 — `rho_frame` vs `rho_ODE`; ratio-only pinning

Two genuinely different constants:

- `rho_frame = X/dp_red = D/deg(p_full) = (16+12t)/(24+18t) = 2/3`,
  the DEPTH-§1 campaign slope. Constant in `t`.
- `rho_ODE = delta/(1-u) = deg(p)/deg(q) = 6 nu/(2 nu+1)`, the
  Cor. 6.1/St. 8.2 ratio in (iv). Strictly increasing in `t`
  (8/3, 14/5, 20/7, → 3⁻).

Cross-identity `X/kbar = dp/dq` verified: `(16+12t)(9+6t) =
(24+18t)(6+4t) = 144+204t+72t^2`. So the same cell data writes both
constants consistently, and confusing them is refuted by computation:
with `rho = 2/3` (or the full-degree misreading `84 nu/(2 nu+1)`, or
perturbations) the linear system on the cell has **zero** solutions even
with `q` completely free and `c = 0` allowed (§5).

**Ratio-only.** The split of `(delta, u)` requires the chart integer
`kappa`: `kbar = kappa(1-u)` (Not. 9.1's fifth slot) and `X = kappa·delta`
(from `d_F = i·delta` in the printed Prop. 8.1 proof, `D = kappa·d_F`,
`X = D/i`). The cell records `kbar = 6+4t`, not `kappa`, so numerical
`delta, u` are NOT available at cell level, and the target correctly
claims only the ratio. The packet's code carries no `u` variable and
never uses `i` in the ODE — checked line-by-line. `1-u != 0` follows
from `kbar = kappa(1-u) = 6+4t != 0`; `delta != 0` from
`rho_ODE > 0`; both also follow chart-free from (iv) + `⊖ != 0` +
`dq >= 2` (§2). CONFIRMED. (Attribution slip on St. 8.2 noted in §9.)

---

## 5. Charge 3 — the reduction, the iff, and uniqueness up to scale

**Reduction, re-derived.** `T := eta^nu`, `r = T^2 - sigma T + pi`
(`sigma = a+b`, `pi = ab`), `p = r^3`, `q = eta r`:

```text
p' = 3 r^2 r'(T) · nu eta^{nu-1},     q' = r + nu T r',
rho p q' - p' q = r^3 · [ rho r + nu T (rho - 3) r' ]  =  ctilde · r^3,
E(T) := rho r + nu (rho - 3) T r'  =  ctilde.
```

(The target's prose says "dividing by r^2"; the factor is `r^3 = p`.
The displayed `E` is nevertheless exactly right — LOW, §9.) Coefficients:

```text
[T^2] = rho + 2 nu (rho - 3);   (2 nu + 1)·[T^2] = 6 nu - 6 nu = 0  identically;
[T^1] = -sigma · (rho + nu (rho - 3));  (2 nu+1)·(rho + nu(rho-3)) = 3 nu != 0;
[T^0] = rho · pi.
```

Both closed forms are polynomial identities in `nu` of degree <= 2 after
clearing `(2 nu+1)`; I verified them at `nu = 1..201` and
`nu = 4 + 3·10^6` (far beyond the degree bound, so they hold
identically), plus the `mu`-uniform generalization
(factor `mu·nu/(2 nu+1)` for equal multiplicity `mu = 1..7`). Hence `E`
is constant iff `sigma = 0` (orbit values opposite), and then
`ctilde = rho·pi != 0` iff `pi != 0` (values nonzero ⟺ distinct ⟺
`r(0) != 0`). The full `eta`-identity
`rho p q' - p' q = rho·pi·p` was rebuilt with my own polynomial code at
`t ∈ {0..7, 10, 15}` and gauges `a ∈ {1, 2, 5/3}`; samples
`ctilde = -8/3, -14/5, -20/7` at `t = 0,1,2` all reproduce. CONFIRMED.

**Uniqueness, strengthened.** The packet's scan holds `q`'s shape fixed
and scans `(sigma, pi)`. I dropped the shape entirely: for `nu = 4` and
`nu = 7`, `p = (eta^nu - a)^3(eta^nu - b)^3` with sample rational values,
unknowns = all `2 nu + 2` coefficients of `q` (degree <= `2 nu+1`) plus
`c`, exact Gaussian elimination over `Q` on the linear map
`(q, c) ↦ rho p q' - p' q - c p`:

- `b = -a` (4 scales incl. negative and non-integral): kernel dimension
  **1**, generator has `c != 0` and `q = scale · eta(eta^{2 nu} - a^2)`
  — the admissible line, nothing else;
- `b != -a` (6 sample pairs): kernel dimension **0** — no solution at
  all, not even a degenerate `c = 0` one;
- wrong `rho` (frame `2/3`, full-degree `84 nu/(2 nu+1)`, perturbed,
  `rho = 1`): kernel `0`;
- `rho = 3` exactly: kernel dimension 1 but the generator has `c = 0` —
  the degenerate power solution `q ∝ eta^{2nu} - a^2` (`q^3 ∝ p`,
  `3 p q' = p' q`), inadmissible since (iv) requires `⊖ != 0`. This is
  precisely the branch the printed root-mult law (R) `dp != mu★·dq`
  guards, and the family has `rho = 6 nu/(2 nu+1) != 3` identically
  (`6 nu != 6 nu + 3`). Deepening note, §9.

So the iff, the nonzero right side, and uniqueness up to the single
scale all hold in the strongest reading. The remaining gauge is real:
`eta → lambda·eta` moves `a` anywhere in `C^*`; `a = 1` gives
`p, q ∈ Z[eta]`. Swapping orbits fixes `sigma = 0`. CONFIRMED.

---

## 6. Charge 4 — every printed side condition, all `nu = 4+3t`

Each row of the target's §6 table was re-proved as an identity, not
sampled (machine check at `t = 0..299` on top):

| condition | proof |
|---|---|
| `M = gcd(6 nu, 2 nu+1) = 3` | any common divisor divides `3(2 nu+1) - 6 nu = 3`; `3 \| 2 nu+1` iff `nu ≡ 1 (mod 3)`, true for `nu = 4+3t` |
| `gcd(M, nu) = gcd(3, 4+3t) = 1` | `4+3t ≡ 1 (mod 3)` |
| `dq ≡ 1 (mod nu)` | `2 nu + 1 ≡ 1` |
| searrow both edges (St. 8.2) | `3(2 nu+1) - 6 nu = 3 > 0`, the identity `3 > 0` |
| root-mult (R) `dp != 3 dq` | `6 nu != 6 nu + 3` |
| `rho_ODE != mu = 3` | same identity |
| `eta ‖ q` | `q = eta·S`, `S(0) = -a^2 != 0` |
| p-roots simple in `q`, no off-p q-root | forced by R1.0 valuations + degree exhaustion (§3) |
| `eta` not a p-root (St. 3.16 `l = 0`) | `p(0) = pi^3 != 0` |
| two distinct `nu`-orbits (St. 3.18) | `a != -a` in char 0; not one `2 nu`-orbit since the Q-datum pins `nu_G = 4+3t` |
| `⊖ != 0` | `ctilde = rho·pi != 0`, `1-u != 0` |
| `kbar = 6+4t ∈ Z`, `nu >= 4 >= 2` | family definition; `kbar` integral iff `nu ≡ 1 (mod 3)` (checked `nu = 2..99`, no omitted neighbor) |
| Prop. 8.1(v) | `M_F = gcd(deg p, deg q)` is (v) itself; no separate full-side check owed |

Chart/gauge: only the ratio `rho_ODE` enters after §2, so the identity
is chart-independent; the `a = 1` gauge is the legal `eta`-rescale.
Full-versus-reduced: (iv) consumes the reduced pair only; the full tier
enters solely through `i = 14` in the `D`/`deg(p_full)` bookkeeping,
verified in §3. The affine constraint `nu = 4+3t` is kbar-integrality,
not an ODE constraint — the same patterns solve (iv) at every `nu`
(my sym-`nu` identities are residue-class-free), and neighboring classes
simply fail `kbar ∈ Z`. The mixed-`mu` (S)-prune of R2.3(ii) does not
fire on the equal-`mu` cell (the prune's example is `mu = (2,3)`; here
both edges are `mu = 3` and (S) is the identity `3 > 0`), T1 is a
single-orbit zero-chain closed form (`p = (t-A)^mu` shape) and does not
apply — and its dead-condition `dp \| dq` would be false here anyway
(`6 nu > 2 nu+1`), and R2.3(i) does not fire (`q = eta·r` with `p = r^3`
is not `⊖ p^h eta^s`, `h ∈ N`). All CONFIRMED.

---

## 7. Charge 5 — the exact maximum consequence

The four-gate split of the target's §7 and the §9 ledger were checked
line by line, and the firewall HOLDS everywhere:

1. **Local formal survival**: proved, with explicit coefficients — the
   theorem, and the only theorem.
2. **Lambda**: merge contribution 0 is the P2 accounting identity on a
   `k = lex = eps = 0` cell (nothing to price) — this matches the D2
   review verbatim. The two incoming `(21,15)` floors of 2 and the trunk
   `(85,35)` floor of 2 remain AF2 lower bounds; the recorded sum 6 at
   the `td-1-psi` ceiling is filter survival at equality, and if any
   actual lambda strictly exceeds its floor, St. 9.4 kills the route.
   The target claims no upgrade; its L1 family-C parenthetical
   (`B = (3/2)A` solves the A-shape) is a real promoted citation
   (SHEET6-L1 §5/§6) and is used only to say "local solvability does not
   compute lambda". Correct.
3. **Landing/realizability**: not claimed. The merge solution is rigid
   (`b = -a`) and each incoming A-step is rigid (`B = (3/2)A`), so
   whether St. 3.9 transport can match them is a genuine open
   computation; the target says exactly this.
4. **Degree bound / JC2**: none, and the sign is right — an infinite
   family of locally admissible cells at fixed `td = 8` is the opposite
   of a completeness/cap mechanism. The strategic §10 statement (a
   numerical `kbar` cap is impossible both at the recorded-book tier and
   as a (iv)-filter on this cell) follows from the D2 review plus this
   theorem.

Also confirmed: the certificate firewall booleans in the charged stdout
are `false` on all five non-local gates; the Sol D2 infinitude is
consumed as reviewed input typing only; completeness of `td = 8` merges
is not claimed anywhere in the target.

---

## 8. Replays, clean-room, mutations — commands and counts

Replays (packet, unmodified):

```sh
cd cases/m2_td8_prop81iv_parametric_grok46_20260829
python3 test_prop81iv_td8_affine.py     # TD8_PROP81IV_PARAMETRIC_GROK46_TEST_PASS checks=1362
python3 -O test_prop81iv_td8_affine.py  # TD8_PROP81IV_PARAMETRIC_GROK46_TEST_PASS checks=1362
python3 prop81iv_td8_affine.py          # stdout sha256 a3d59f3b...13, certificate 6935db46...a8
```

Clean-room (`/tmp/f5rev/cleanroom.py`, own polynomial toolkit, packet
not imported): 25 checks — sym-`nu` coefficient identities
(`nu = 1..201` and `4+3·10^6`), `mu`-uniform law (`mu = 1..7`,
`nu = 1..59`), full `eta` identities (10 `t`-values × 3 gauges),
`ctilde` samples, q-free kernel computations at `nu = 4, 7`
(4 opposite-scale + 6 non-opposite pairs each), wrong-`rho` battery,
i-chain + `i = 7` refutation + frame i-blindness, side conditions
`t = 0..299`, kbar-integrality census `nu = 2..99`, and 8 mutations.
24/25 passed on first run; the single failure was **my own check being
too strong** (demanding empty kernel at wrong `rho`, where `rho = 3`
has the inadmissible `c = 0` degenerate); the corrected admissibility
check (no `c != 0` kernel element at any wrong `rho`; degenerate
generator identified as `scale·S`) passes at both `nu = 4` and `nu = 7`.

Mutations of a producer copy in `/tmp` (packet untouched), all four
reproducing the target's §8 table messages exactly:

| mutation | observed failure |
|---|---|
| `sigma = Fr(1)` in `solve_reduced` | `reduced E is not constant after sigma=0` |
| `rho_ode = Fr(2,3)` | `ODE rho is not 6 nu / (2 nu + 1)` |
| `p = S` for `S^3` | `deg p mismatch` |
| `i_prop = 7` | `i_prop81 disagrees with the pole/A-step chain` |

Additional adversarial clean-room mutations, all failing as they must:
hidden `i`-power (`p → p^14` breaks the identity), `b = 2a` and orbit
collision `b = a` (not `c·p`), `pi = 0` (collapses to `c = 0`,
inadmissible), dropped `eta`-factor (`lhs[0] = 0` bars any `c != 0`;
`lhs = (rho-3)S^3 S' != 0`), extra q-orbit, proportional `q = eta·p`;
positive control `mu = 2` opposite-orbit solves with `c = -rho_2`
(the `sigma = 0` law is `mu`-uniform, as the target says, while the
cell's multiplicity stays 3).

---

## 9. Findings, severity order

No CRITICAL, HIGH, or MEDIUM finding. The theorem, its scope, and its
firewall all stand.

**LOW (diction, no verdict impact).** Target §4: "after dividing by the
nonzero polynomial `r^2`" — the common factor of
`rho p q' - p' q` and the RHS is `r^3 = p`, not `r^2`. The displayed
`E(t_var)` and all three coefficients are correct.

**LOW (attribution, no verdict impact).** Target §2: "`delta != 0` and
`1-u != 0` (St. 8.2's own hypotheses)" — printed St. 8.2 states no such
hypotheses; its proof divides by `1-u` silently. Both facts are true on
the cell, by the target's own kbar/rho argument and, chart-free, by
(iv) + `⊖ != 0` + `dq >= 2` (§2 here).

**NOTE (deepening, worth recording).** At `rho = mu = 3` — and only
there among tested wrong ratios — the shape ODE acquires a spurious
one-dimensional `c = 0` kernel, `q ∝ eta^{2nu} - a^2` with `q^3 ∝ p`.
Admissibility (`⊖ != 0`) and the printed (R) law both exclude it, and
`6 nu/(2 nu+1) != 3` identically, but any future automation that solves
(iv) with `c` free and forgets the `c != 0` gate would report a false
survivor on any cell with `dp = mu·dq`.

**NOTE (strengthening).** The packet's uniqueness evidence is
shape-tied (`(sigma, pi)` scan). The q-free kernel computation in §5
upgrades the uniqueness statement: no exotic `q` (with off-p roots,
wrong `eta`-order, or non-orbit structure) can rescue a non-opposite
pair even degenerately. The theorem as stated survives the stronger
reading; a future consumer may cite this review for that upgrade.

**NOTE (cosmetic).** Target §5's parenthetical "no `nu`-th root of unity
squares to `-1` in the value of `eta^nu`" is garbled as written; the
intended and correct fact is that `eta^nu` is constant (`= a` resp.
`-a`) on each orbit and `a != -a`. Also, positive `pi` gauges are
admissible too (`p = (eta^{2nu} + 1)^3 ∈ Z[eta]` at `pi = 1`, orbit
values `±i`); the `a = 1` convention is one integral choice among two.

**NOTE (test hygiene, no impact).** The in-suite `mutation-drop-eta`
check (`lhs[0] == 0` and `p[0] != 0`) refutes admissible solutions
soundly but does not separately record `lhs != 0`; my clean-room closes
that cosmetic gap (`lhs = (rho-3)S^3S'`).

---

## 10. Narrowest sound replacement theorem

None needed — the target's §0/§5 statement is already the narrowest
sound form. For the record, the promotable local theorem is:

> **Theorem (td=8 equal-join local Prop. 8.1(iv) family).** Fix an
> integer `t >= 0`, `nu = 4+3t`, and the reviewed R2.2-typed equal-join
> reduced cell (`dp, dq, M, kbar, X, w`) =
> `(24+18t, 9+6t, 3, 6+4t, 16+12t, 4/3)` with two nonzero `nu`-orbits of
> multiplicity 3 and `eps = k = lex = 0`. Then the printed identity
> Prop. 8.1(iv), with its forced ratio
> `delta/(1-u) = deg(p)/deg(q) = 6 nu/(2 nu+1)`, admits an admissible
> solution (`⊖ != 0`) — with `q` free of degree `<= 2 nu+1` — **iff**
> the two orbit values are opposite and nonzero; the solution is unique
> up to one scale, `p = (eta^{2 nu} - a^2)^3`,
> `q = ⊖ eta(eta^{2 nu} - a^2)`, `ctilde = -a^2·6 nu/(2 nu+1) != 0`;
> every printed root/eta/gcd/searrow/multiplicity/orbit side condition
> holds identically in `t`; the exceptional set is empty; the
> Prop. 8.1 exponent of the merge vertex is `i = 14`. The statement is
> vertex-local and formal: it asserts no exact lambda beyond the P2
> merge-0 identity, no St. 3.9 transport/landing, no geometric
> realizability, no degree bound, and no JC2 consequence.

A PASS here authorizes canonical promotion of exactly that statement,
and nothing else. **No AWS launch is authorized by this review.**

---

## 11. Scope firewall and blindness

This review does not assert: exact lambda on the priced steps; landing
or coefficient transport; realizability of any member; completeness of
`td = 8` merges; any degree ceiling; any JC2 consequence; or any AWS
design. It did not access `jc2-lean`, the web, or AWS; it ran no global
`git status`, no workspace-wide search, no heavy CAS, and no
long/high-memory process; it committed and pushed nothing; it modified
only this file, with scratch confined to `/tmp/f5rev`. The active Sol
and Opus Prop. 8.1 consumer reports were never read. Compute: pdf text
extraction of the cited printed pages; desk `Fraction` reconstruction of
every displayed identity; the two packet replays; the clean-room and
mutation batteries listed in §8.

**Verdict: `PASS_AT_LOCAL_PROP81IV_SCOPE`.**

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = 9e594a2343bfcdfe8b2631506543139210f1fa178f4a616c7e09d93ba54da82b
(sha256 of this file up to and including the line "*Report body ends. Self-hash below covers everything above this line.*", i.e. of the first 25122 bytes)

Full-report SHA-256 is the hash of the complete file bytes, including this appendix. Compute with:

```
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-prop81iv-parametric-hostile-review-fable5-20260829.md').read_bytes()).hexdigest())"
```
