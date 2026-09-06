# Exact-contact Xu on R009 and R050 — Opus 5 — 2026-09-06

## 0. Custody and scope

I paired the receipt's numbered `charged_input_<i>_sha256=`/`_basename=` fields with `awk`,
piped the manifest to `sha256sum -c`, and got **7/7 OK** before any mathematical read. All
mathematical reads were the frozen copies in `/tmp/jc2-lane.69C0ak/inputs`. No ledger, no
`jc2-lean`, no other `ideation-*` submission, no uncharged artifact tree. Writes: this report
and `box/exact-contact-20260906/` (396 KB; `df -h /` checked, 1.8 GB free).

**Scope note on "reconcile the three".** Only astra's submission is a charged input. grok46's
"final major π-roots" version and sol56's "exact-contact" version are *not* in the manifest;
I reconcile against their one-line descriptions in the packet plus astra's printed lines, and
say so wherever it matters. No claim is attributed to an unread text.

Source key. **X** = the charged Xu PDF (page-free line refs to the extracted layout text):
Def. 4.3 (major/minor, principal minor roots), Def. 4.6 (`D_σ^h`, `P_M`, `P_m`), Lemma 2.1
(proportional), Lemma 4.1 (chain rule), Lemma 4.4(i),(ii), Thm 3.4, Thm 4.7, **Thm 5.1**,
Cor. 5.3, §6.1–6.2 (four worked cases). **M** = the charged Moh PDF: Prop. 4.5 p.169,
**Prop. 4.6 (1)–(5) p.170** and its p.171 `J = x^l` Remark, **Def. 5.1 (1)–(4) p.179**,
Prop. 5.2/5.3 pp.179–180, Prop. 5.4 p.183. **RS** = residual65-structure-fable5. **A** =
ideation-20260906T0000Z-astra.

No exit-price assertion is declared here, so no `charge_basis=` line: every verdict below is
an exclusion of a *configuration*, not a new exit price.

## 1. The instrument: an exact packet calculus, and what is actually determined

Write `f` for the **smaller** member (`deg_y f = m`) and `g` for the larger (`deg_y g = n`),
as in X Thm 5.1's proof; the campaign's `(n,m)` is `(deg F, deg G)`, so X's `f` is the roster's
`g`. `I_M` is symmetric under the swap, so nothing depends on the choice.

A **packet** is a set of roots of `f` still sharing a disc. Track `(ρ, λ^f, δ)` = (number of
`f`-roots, `ord f_ξ` at the disc, logarithmic radius). Two printed identities drive everything:

* **M Prop. 4.6(2),(3):** at a tower disc `D_i`, `ord T_1^*(σ_i) = (−μ_1)λ` with
  `λ = (−1+δ_i)/(n−M_i)`, i.e. `λ^f(σ_i) = m(δ_i−1)/(n−M_i)` and `λ^g(σ_i) = n(δ_i−1)/(n−M_i)`.
* **X Lemma 4.4:** a *final major* π-root has `δ = λ^f+λ^g+1` (and `δ<1`); a *final minor*
  π-root has `λ^f = λ^g = 0` (and `δ>1`).

Descending inside a packet, `λ^f(δ) = λ^f_0 + ρ(δ−δ_0)`. Put `δ_0^{zero}` for the radius where
`λ^f = λ^g = 0` and set the **packet invariant**

```
    kappa  :=  rho * (1 - delta_zero)  =  rho*(1-delta_0) - |lam^f_0|      (constant while unsplit)
```

Then, exactly:

| quantity | closed form |
|---|---|
| packet is minor | `kappa < 0`; its final minor order is `delta = 1 - kappa/rho` |
| packet is major | `kappa > 0`; it goes final at `delta = 1 - (n+m)kappa/((n+m)rho - m)` |
| its `I_M` term (X Thm 5.1) | `J = n*rho*kappa / ((n+m)*rho - m)` |
| its `I_m` term (X Cor. 5.3) | `-kappa/rho` |
| split at radius `δ_s` into `ρ_j` | `kappa_j = rho_j*(1-delta_s) - |lam^f(delta_s)|`, `Σκ_j = κ − (k−1)|λ^f|` |

Two corollaries that make the census-level "floor" reading unnecessary:

* **The Moh threshold is the Xu dichotomy.** A sub-disc of `D_i` at a root of `p_i` of
  multiplicity `r` has `δ_zero = δ_i + (1−δ_i)·lo_i/r` with `lo_i = d_i/(n−M_i) = P_i/Q_i`.
  Hence it is **minor iff `r < lo_i`, major iff `r > lo_i`** (`r = lo_i` is excluded by
  M Prop. 4.6/A.3). This is a one-line identity, not a bound: `δ_zero>1 ⟺ (1−δ_i)(lo_i/r−1)>0`.
* **The principal minor packet is forced.** At level `s` (`δ_s=−1`, `M_s=n−2`) the two points
  at infinity (M Prop. 4.5) have `r = u_s` and `r = V_s`, `lo_s = d_s/2`; the `u_s` packet gets
  `δ_zero = −1 + d_s/u_s = V_s/u_s` exactly, which is X's printed principal split order.
* **Minor packets cannot be continued.** If a minor packet's `f`-pattern had a multiple root at
  `δ_zero`, X Lemma 2.1(ii) makes `f_σ^n/g_σ^m ∈ K^*`, so that root is a root of `g_σ` too and
  the branch would carry `ord g(α) > 0`, contradicting X Def. 4.3. It may still *split* earlier,
  and any split strictly raises `I_m` — which is what pins the margin-0 rows below.

**The new exact test.** X §2 *defines* `I(f,g) = deg_x Res_y(f,g)`, a non-negative integer;
X Thm 5.1 *equates* `I(f_ξ,g) = I_M(f,g)`. Therefore

```
        I_M  =  (n/(n+m)) * sum_{sigma in P_M} |D^f_sigma| (1 - delta_sigma)   is an INTEGER.
```

Xu never states this. It is the difference between using Cor. 5.3 as a floor (`I_M ≥ I_m`) and
using Thm 5.1 as an equality: with exact contacts, `I_M` is a *rational number computed from
the configuration*, and integrality is a genuine second condition. **PROVED-HERE** from
X §2 (definition) + X Thm 5.1 (equality); no unprinted step.

**Positive controls.** The calculus reproduces all four of Xu's printed worked cases exactly —
degrees, contact orders, `I_M` and `I_m`:

| Xu case | roster row | `I_M` mine / Xu | `I_m` mine / Xu | final-major display |
|---|---|---|---|---|
| §6.1 (75,50)(i) | R002 `p_2=(π^5−c_1)^2(π^5−c_2)^2` | 8 / 8 | 4 / 4 | `π(π^3−a)`, `ρ_f=4` |
| §6.1 (75,50)(ii) | R002 `(2,1,1)` | 4 / 4 | 6 / 6 | minor sibs at `6/5` |
| §6.2 (84,56)(i) | R001 `(2,1)` | 4 / 4 | 5 / 5 | minor sibs at `9/7` |
| §6.2 (84,56)(ii) | R007 `z=1,(5)` | 10 / 10 | 4 / 4 | `π(π^3−a_1)(π^3−a_2)(π^3−a_3)`, `ρ_f=10` |

The final-major *shape* is also reproduced: at `D_1`, `A_1 = den(L_1 δ_1)` and the squarefree
pattern lies in `π^z k[π^{A_1}]` with `z ≤ 1`, so `ρ_f ≡ 0 or 1 (mod A_1)`. All four Xu displays
satisfy it, and **0 of 66 roster rows violate it** — a clean negative control (it is the
already-applied `(GO)` law, so it must kill nothing).

## 2. R009 = (192,128): the determined configuration, and its exact margin

Row data: `d=(192,64,4,2)`, `V=(V_2,V_3)=(2,3)`, `δ=(19/24, 5/16, −1)`, `u_s=1`, `ℓ=1`;
derived `P_2=48`, `Q_2=33` (astra's `d_p=48, d_q=33`, A:176, independently reproduced),
`A_2=16`, `lo_2=16/11`, `lo_3=2`.

M Prop. 4.6(3),(4) (`q` squarefree of degree `Q_2`, roots of `p` are roots of `q`) plus
Def. 5.1(2) (`V_2 ∈` multiplicities, none equal to `lo_2`, one exceeding it) leave exactly
**two** level-2 patterns: `p_2 = (π^{16}−c_1)^2(π^{16}−c_2)` and `p_2 = π^{16}(π^{16}−c_1)^2`.

**Pattern (α) `z=0, (2,1)` — fully determined, no free root.**

| leaf | count | `ρ_f` | exact contact `δ` | contributes |
|---|---|---|---|---|
| principal minor (level 3, `r=u_s=1`) | 1 | 32 | `V_s/u_s = 3` | `I_m += 2` |
| level-2 minor siblings (`r=1 < 16/11`) | 16 | 2 | `21/16` | `I_m += 16·5/16 = 5` |
| final major `D_1` (`r=V_2=2`) | 16 | 4 | `δ_1 = 19/24` (`= λ^f+λ^g+1`, `λ^f=−1/12`, `λ^g=−1/8`) | `I_M += 16·1/2` |

```
    I_M = 8        I_m = 1 + 2 + 5 = 8        margin = 0        I_M in Z : yes
```

Cross-checks of the same number by two other printed routes: `I(f_ξ,f_y) = 128+62+4 = 194`
(X Thm 3.4 over the split π-roots `σ_3, σ_2`, the 16 `D_1`'s and the 16 minor sibs) equals
X Thm 4.7(i)'s right side `127 + 62 + 5 = 194` — i.e. **every inequality in X Thm 4.7 is tight**,
and `I(f_ξ,g) = Σ_{P_m}|D^f|δ + N_M − I(f_ξ,f_y) = 138 + 64 − 194 = 8 = I_M`.

**Pattern (β) `z=16, (2)` — the sibling major tower, and why it dies.** The zero root has
`z = 16 > lo_2`, so by the dichotomy the zero disc (`ρ_f=32`, `κ=20`, born at `W = n−M_2 = 44`)
is a *second major tower*. Three independent printed obstructions:

1. *If it terminates at once*: `δ = 29/79`, `I_M = 8 + 960/79 = 1592/79 ∉ Z`. **Dead by
   integrality.**
2. *Same case, Galois*: that final disc has `A = den(L·29/79) = 79` with `L = lcm(16,1) = 16`,
   while its squarefree pattern has degree `32 < 79` — so the pattern would be `π^z`, one root,
   not final. **Dead by M p.201(8).**
3. *If it extends*: exhaustive search over all admissible continuations (below) returns
   **no** completion with `I_M ∈ Z` and `I_M ≥ I_m`, at split depth ≤ 2 and for every
   admissible reduction divisor `d ∈ {2,…,64}` including the most permissive `d = gcd(n,m)`.

**Verdict R009.** The necessary configuration is **unique and fully determined**, and Xu's
equality holds on it with **exact margin 0**: `I(f_ξ,g) = I_M = I_m = 8`. R009 is **not** dead;
it is maximally rigid — *any* further splitting of *any* minor packet raises `I_m` above 8 and
kills the row, so the whole two-place configuration is pinned, contact order by contact order.

## 3. R050 = (196,56): unique configuration, exact margin 0

Row data: `d=(196,28,4,2)`, `V=(4,3)`, `δ=(19/28,1/4,−1)`, `P_2=21`, `Q_2=9` (astra's
`d_p=21, d_q=9`, A:179 — reproduced), `A_2=4`, `lo_2=7/3`. Two admissible level-2 patterns:
`p_2 = π(π^4−c_1)^4(π^4−c_2)` and `p_2 = π^5(π^4−c_1)^4`.

**Pattern `z=1, (4,1)` — determined.**

| leaf | count | `ρ_f` | exact `δ` | contributes |
|---|---|---|---|---|
| principal minor | 1 | 14 | `3` | `I_m += 2` |
| level-2 zero root (`z=1 < 7/3`) | 1 | 2 | `2` | `I_m += 1` |
| level-2 minor orbit (`r=1`) | 4 | 2 | `2` | `I_m += 4` |
| final major `D_1` (`r=V_2=4`) | 4 | 8 | `δ_1 = 19/28` (`λ^f=−1/14`, `λ^g=−1/4`) | `I_M += 4·2` |

```
    I_M = 8        I_m = 1 + 2 + 1 + 4 = 8        margin = 0        I_M in Z : yes
```

**Pattern `z=5, (4)`** puts `z = 5 > lo_2 = 7/3`, a sibling major tower `(ρ_f=10, κ=4, W_0=12)`.
Immediate termination gives `δ = 13/22`, `I_M = 8 + 35/11 = 123/11 ∉ Z`, and that disc's
`A = den(4·13/22) = 11 > 10 = ρ_f` mod-obstruction fails too. The search over continuations
returns **zero** admissible outcomes at every depth ≤ 4 and every divisor.

**Verdict R050.** Exactly **one** necessary configuration, with **margin 0** and `I_M = I_m = 8`.
Same rigidity statement as R009.

## 4. The sibling-tower search, and the two lemmas it needs

A sibling major packet is a state `(ρ, κ, W_0, L, d)`; `W = n − M` is the tower parameter,
`|λ^f(W)| = mκ/(Wρ−m)`, `δ(W) = 1 − Wκ/(Wρ−m)`, final major at `W = n+m`. Constraints imposed,
all printed: `Q = ρW/m ∈ Z` (M Prop. 4.6(2)); `#parts ≤ Q` (4.6(3),(4)); no `κ_j = 0`; some
`κ_j > 0` (Def. 5.1(2)); `ρ_j ∈ (m/gcd(n,m))Z` (Lemma 2.1(ii)); parts = one optional singleton
plus orbits of `A = den(Lδ)` equal parts (M p.201(8)); and at a final disc `ρ_f, ρ_g ≡ 0 or 1
(mod A)`. Two further lemmas, both PROVED-HERE from printed lines:

**Lemma A (primitivity).** At a split, the multiplicities `r_j = ρ_j/(m/d)` of the reduced
pattern must be setwise coprime, else `d` was not the reduction divisor of that disc.

**Lemma B (cross-tower consistency).** Moh's `d_i = gcd(n, M_1,…,M_{i−1})` is the gcd of `n`
with the exponents *strictly deeper* than `D_i`, and Prop. 4.6(1)/Def. 5.1(4) fix
`g_{σ_i} = c·p^{n/d_i}` with `deg p = V_{i+1}d_i/d_{i+1}`. A sibling sub-tower that inserts a
new exponent `M` below an ancestor disc `D` re-computes that ancestor's divisor as
`gcd(d_D, M)`; the ancestor's pattern degree is already fixed by the row, so
**`d_D | M`, i.e. `W ≡ n (mod d_D)`**, for every ancestor `D`.

Lemma B is the decisive one, and it is exactly the audit gap that astra's Q2 flagged from the
other side ("gluing equations: centres cannot remain independent", A:186). Its correctness is
witnessed by an independent target: **with it, R001 dies outright** — pattern `(2,1)` by
Xu's own §6.2(i) margin `4 < 5`, and pattern `z=7` because *no* continuation of its `ρ_f=14`
sibling is admissible at any depth ≤ 3. Without Lemma B the `z=7` branch survives with
`I_M = 7`, i.e. the census's "R001 is the sole Xu removal" would be unreproducible. This is a
retrodiction, not a fit: Lemma B was derived from Def. 5.1 before R001 was tested.

## 5. Generalisation: exact margins on the other 63 rows

I ran the calculus on all 66 rows: enumerate every level-`i` pattern (`i = s−1 … 2`; level `s`
is Prop. 4.5) with every Def. 5.1(4) tower selection, then evaluate all leaves exactly.
**1,080 configurations.** Of these, **995 have `I_M ∉ Z`** and 77 have `I_M < I_m`; **924 are
killed by integrality alone** — the new test does ~12× the pruning of Cor. 5.3 at this level.

Classify a configuration: **T1** no major sibling (fully determined); **T2** every major sibling
has multiplicity `= V_i` (a Galois-parallel copy of the tower — Xu's §6.1(i) is of this kind);
**T3** a major sibling with a different multiplicity (a genuinely new tower, set-valued).

Exact margins of the best surviving configuration, smallest first (full table in
`box/exact-contact-20260906/census.json`):

| margin `I_M − I_m` | rows |
|---|---|
| **0** | **R009** (8), **R014** (6), **R049** (10), **R050** (8) — all T1 |
| 1/2 | R016 (9) |
| 1 | R011 (6) |
| 3/2, 2, 3 | R035 (9), R036 (8), R032 (8) |
| 4 | R002 (8, T2 = Xu §6.1(i)), R003 (9), R022 (9) |
| 9/2 | R023 (12, T2), R044 (8) |
| 6 | R004, R007 (Xu §6.2(ii)), R034, R013 (T2) |
| 15/2 … 121/4 | the remaining 40 rows |

`I_M` in parentheses. Only four rows are at margin 0, and only R009 and R050 have a **single**
surviving configuration; R014 and R049 keep 2 and 3 respectively, so their margin-0
configuration is one alternative among several, not a pinned datum. RS:253's bound-based
margin list (0 on R009/R050, 1 on R011, else ≥ 3) is *conservative but not exact*: with exact
contacts R014, R049 join at 0, R016 sits at 1/2 and R035 at 3/2 — values a floor computation
cannot produce. This is the FALLACY-v2 floor/attainment separation made quantitative.

**Six new row kills.** Rows **R025, R026, R027, R028, R057, R058** — exactly RS:113's six
"two-major-tower" rows, identified there from the *child*, recovered here independently from
the *parent* — have **no** configuration without a genuine (T3) sibling major tower, and for
every one of their 14 patterns the sibling admits **no** completion with `I_M ∈ Z` and
`I_M ≥ I_m` at split depth ≤ 2. Typed **DEAD-mod-[depth ≤ 2; Lemmas A,B]**, not yet promoted:
the search is exhaustive in `W`, in the orbit shape and in the partition (≤ 4 orbits), but the
depth cap is a cap. Re-running at depth 3 on R057/R058 is minutes; the R025–R028 arms need the
combinatorial product and are the one real cost. If they hold, the residual is **59**.

Four rows (R039, R040, R048, R063) survive only through a T3 configuration and are the next
targets of the same closure; eight (R002, R013, R019, R020, R023, R024, R047, R066) survive
through T2 and need only the parallel-copy reading, which is determined.

## 6. Is exact Xu descent-invariant? No — it is `ℓ`-sensitive

With `J = c·x^ℓ` (M Prop. 6.3(3) gives the child `J_{γ,π} = −(u_s/b)γ^{v_s−u_s−1}`, `ℓ=1` on
both rows), X Lemma 4.1's right side becomes `−t^{−ℓ−2}` and the whole calculus shifts `1 → 1+ℓ`:

```
  final major : delta = lam^f + lam^g + 1 + ell  (delta < 1+ell)      minor : delta > 1+ell
  Prop 4.6(3)*: lam = (-1-ell+delta)/(n-M_r)     [M p.171 Remark, verbatim]
  Thm 5.1     : I_M = (n/(n+m)) sum |D^f|(1+ell-delta) = deg_x Res_y(f_xi,g)  in Z
```

The packet closed forms are unchanged with `κ := ρ((1+ℓ) − δ_zero)`; the *inputs* are not.
So integrality survives descent but the condition it constrains does not: `(B)` and `(GO)` are
identities with the parent's (RS §4.1, §4.2), whereas exact Xu at the child is a different
equation on a different pattern set. Concretely, on the roster's own-child data (radii
`(ℓ+1)(1−ratio)`, reproduced against `delta_prime` exactly):

* **R009 child** `(48,32)`, `M'=(−32,37)`, `δ'=(4/3,−1/5)`, `A'_2=5`, `lo'_2=16/11`: two
  patterns. `z=1,(2,1)` gives `I'_M = 8` (final major `ρ_f=4` × 5 at `δ=4/3`; minor packets
  `ρ_f=2` at `δ=3`); `z=6,(2)` gives `I'_M = 592/29 ∉ Z` — **killed by child integrality**.
* **R050 child** `(49,14)`, `M'=(−14,46)`, `δ'=(5/7,−1)`, `A'_2=1`, `lo'_2=7/3`: three patterns.
  `(4,2,1)` and `z=1,(4,2)` give `I'_M = 8`; `(4,3)` gives `146/13 ∉ Z` — **killed**.

Two observations, both typed as observations. (i) `I'_M = 8 = I_M` on both rows; I do not claim
an invariance theorem — `I(f_ξ,g) = [K(x,y):K(f,g)]` (X Cor. 4.8) is suggestive but the child is
not a Jacobian pair, so this is **OPEN**. (ii) The child's *minor* side needs the `ℓ`-shifted
X Thm 4.7, which Xu does not print; I therefore give exact `I'_M` and exact minor contact orders
but **no** child `I'_m` and no child Cor. 5.3. Typed **OPEN: ell-shifted Thm 4.7**.

This settles opus5's `ℓ`-sensitivity remark affirmatively: exact Xu **is** a uniform
second-generation condition (it applies at every generation) and it is **not** descent-invariant
(the shift `1 → 1+ℓ` changes both the finality relation and the minor threshold, and the child's
admissible pattern set differs from the parent's).

## 7. Reconciling the three instruments

* **astra's own-child linear image** (A:153–166; 600×263 over 125 base coordinates for R009).
  Orthogonal and complementary: it tests whether *one* compatible `P` exists on a fixed support;
  exact Xu tests whether the *root configuration* is arithmetically consistent. It makes astra's
  Q2 cheaper in one concrete way: the two-place configuration is now pinned, so the 600×263
  chart can be built against a single known contact ledger rather than a set. Astra's face-ODE
  table (A:176–179) is confirmed on its own terms — `A=16, d_p=48, d_q=33` and `A=4, d_p=21,
  d_q=9` are exactly my `A_2, P_2, Q_2` — and its conclusion that isolated face-ODE kills fail
  is unaffected: nothing here is a face kill. Astra's Xu paragraph (A:210–212) is the correct
  diagnosis; the equality chain does collapse, and the collapse pins the rows, not kills them.
* **grok46 "final major π-roots".** Reconciled: `I_M` really is carried entirely by the `A_2`
  conjugate `D_1` discs, and the per-disc term is `n ρ_f κ/((n+m)ρ_f − m)`. But `I_M` alone is
  *not* a kill on either row; the content is in pairing it with the exact minor packets and with
  integrality.
* **sol56 "exact contact".** Reconciled and sharpened: the exact contacts are not a hypothesis
  to be guessed — they are forced, `21/16` and `2` here, by `δ_zero = δ_i + (1−δ_i)lo_i/r`. The
  set-valued part is not the contacts; it is the *pattern*, and both rows have theirs pinned.

## 8. FALLACY-v2 ledger

*Floor/attainment.* The whole point: RS's `IM_max − Im_min` is a decoupled floor pair; the
margins in §5 are per-configuration values of the two exact functionals. Where a configuration
is not determined (T2, T3) I report a set, never its extremum as a fact.
*Carrier/attainment.* No configuration is asserted to be realised by a polynomial pair; the
roster's `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR` type is preserved throughout.
*Flag/place/series.* `ρ` counts roots of one polynomial, `κ` is a series datum, `A` is a Galois
orbit size; the child's discs are never identified with the parent's.
*Pole/interior.* The major/minor dichotomy is applied only after the vertex class (`r` vs `lo_i`)
is computed, never by analogy with a neighbouring row.
*Prime label.* `'` marks the child generation; the only differentiation is Moh's `d/dπ` in A.3.
*Variable/ring map.* X's `(f,g)` is the roster's `(g,f)`; the swap is declared in §1 and the
symmetry of `I_M` under it is checked.
*Target/arrival index.* `W = n−M` is kept distinct from `Q = ρW/m` (a degree) and from `δ`.

## 9. Verdict

```text
R009 (192,128)  UNIQUE necessary configuration (pattern p_2 = (pi^16-c1)^2(pi^16-c2)):
                16 final major discs at delta_1 = 19/24, |D^f| = 4 each
                16 final minor packets at delta = 21/16, |D^f| = 2 each
                 1 principal minor packet at delta = 3, |D^f| = 32
                I_M = I_m = 8 EXACTLY.  Xu Thm 5.1 SATISFIED, margin 0.  ALIVE, pinned.
R050 (196,56)   UNIQUE necessary configuration (pattern p_2 = pi(pi^4-c1)^4(pi^4-c2)):
                 4 final major discs at delta_1 = 19/28, |D^f| = 8 each
                 5 final minor packets at delta = 2 (1 central + 4 conjugate), |D^f| = 2
                 1 principal minor packet at delta = 3, |D^f| = 14
                I_M = I_m = 8 EXACTLY.  Xu Thm 5.1 SATISFIED, margin 0.  ALIVE, pinned.

NEW PRINTED TEST      I_M = deg_x Res_y(f_xi, g) in Z   [Xu sec.2 + Xu Thm 5.1]  PROVED-HERE
                      kills 924 of 1080 configurations that Cor 5.3 alone retains
NEW LEMMAS            A (primitivity of the reduced pattern), B (cross-tower consistency,
                      d_D | M for every ancestor)                                PROVED-HERE
CONTROL               Xu sec.6.1(i),(ii) and 6.2(i),(ii) reproduced exactly (I_M and I_m);
                      final-disc Galois law violated by 0 of 66 rows; R001 dies outright,
                      reproducing the census's sole Xu removal -- WITH Lemma B, not without.
NEW ROW KILLS         R025 R026 R027 R028 R057 R058    DEAD-mod-[depth<=2; Lemmas A,B]
                      (RS:113's six two-major-tower rows, recovered from the parent side)
                      residual 65 -> 59 if the depth cap is lifted and holds.
OPENS RAISED
  1. depth cap. The sibling closure is exhaustive in W, orbit shape and partition but capped
     at split depth 2 (3 for R001, R009, R050). Lift to 4 on the six kills. QUANTITY: depth >= 4,
     4 cores, 2 GB, 3 h.
  2. ell-shifted Xu Thm 4.7. The child's I_m has no printed inequality. QUANTITY: derive the
     l-analogue of (4.3),(4.4) verbatim from Lemma 4.1 with J = x^l, <= 2 h source work.
  3. I'_M = I_M on both rows: is I(f_xi,g) preserved by the Prop 6.3 descent? QUANTITY: run
     the same code on all 46 complete rows, <= 30 min, then a proof or a counterexample.
  4. T3 residue. R039 R040 R048 R063 survive only through a genuinely new sibling tower.
     QUANTITY: same closure on 4 rows, <= 1 h, 4 cores.
  5. No configuration here is a witness pair; only the receiver charts (RS sec.5(d)) can
     produce one. QUANTITY: R009/R050 stay the cheapest at <= 600 and <= 1953 rows.
```

Drivers, all exact-rational and re-runnable: `box/exact-contact-20260906/exact_contact.py`
(tower, Prop. 4.6 pattern enumeration, flat evaluator, census), `sibling_tower2.py` (Galois law),
`sibling_tower3.py` (+ Lemmas A,B), `child_xu.py` (`ℓ`-shift), `row_close.py`, `census.json`.

<!-- BODY-END -->
