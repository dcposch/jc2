# Hostile review: fixed `p=0` residual `A`-Cech grade-14/15 replay

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/` together with the ramified-closure design |
| Producer status | **PROVISIONAL**; dual-source replay printed `PASS_P0_A_CECH_G14_G15` |
| Overall verdict | **CONFIRMED** |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Printed `PASS` tokens, validator strings, and the producer status line are not characteristic-zero algebra |
| Method | SHA-256 of every named pin; source reading of the owner emitter and the `p=0` wrapper; exact `Fraction` census of the frozen seven tails under the high-contact substitutions; independent Taylor expansion of the collision Laurent receivers in `t=1/z`; specialization of the printed exact-`Q` rows; reduction of those rows into `F_65521`. No Singular rerun, Sage, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

The displayed identities hold over `Q` as raw polynomial equalities on the stated high-contact cone. The two residual `A` opens of that cone are empty. Nothing larger is proved.

---

## Verdict

**CONFIRMED.**

On the fixed collision fibre `p=0` of the complete seven-row ordinary source, in the registered high-contact cone

```text
Lambda = sigma^2,
R      = sigma^2 (B0 + sigma B1),
C      = sigma^4 (E0 + sigma E1),
A      = A0 + sigma A1,
k10    = k0 + sigma k1,
```

with ordinary dictionary `B0 = bs0 z + br0/4`, `E0 = (e1 z + e0)/2`, and `A0 = a1 z + a0`, the extracted source rows at absolute grades fourteen and fifteen satisfy

```text
g15[6] = -(1/16) a0^3,                                  (1)

g14[2] |_{a0=0} = -(3/32) a1^2 br0,                     (2a)
g14[1] |_{a0=0} =  (3/8) a1 (e0 - a1 bs0),              (2b)

g15[3] |_{a0=br0=0, e0=a1 bs0} = -(1/16) a1^3.          (3)
```

Identity (1) is an equality of polynomials, not a localization. On `D(a0)` it is a unit, so that open of the cone is the empty scheme over `Q`. On `V(a0) intersect D(a1)`, (2a) and (2b) are unit-triangular in `br0` and `e0-a1 bs0` respectively; after those two raw substitutions, (3) is a unit. No radical, saturation, division by `p`, or modular inference is used. Lower loads `k6,k2` and targets `mu2,mu4,mu6,J` are present in the emitter and are absent from these two grades by individual-term `sigma`-valuation at `p=0`.

This is only the fixed-`p=0` high-contact residual `A` chart after leading `R,C` have been routed to zero. It is not a total Kummer/Rees theorem, not a moving-`p` exclusion, and not a verdict on order two, maximum twelve, or JC2.

---

## 0. Custody

Independently recomputed SHA-256 of the five required primary pins match the review assignment:

| Artifact | SHA-256 |
|---|---|
| `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/FREEZE.sha256` | `9b162c2dff50a6ca51d0eb0e7bb352379a5e0cd5f33acb7ce9c020ab7128b8a5` |
| `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/RESULTS.sha256` | `bf9d044082ad94e5a46d7b4b8c32638bd6381cfef7964409aa91d06bd805799c` |
| `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/RESULT.md` | `0db373023a1431e3d8e266faa9b52f90a886627fa77aae1c6738f860b86853dd` |
| `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/compile_p0_a_cech.py` | `3c2f6829d17794979f5e18381d859408a9f96d7c06060d334d10b1ef41b705cb` |
| `xmodel/max12-812-order2-p0-dk0-support-exhaustion-ramified-closure-design-20260826.md` | `3518ac6c1505098a7b9e19c7b7ca2610dce42ff741e3f39065d0618b926ddb10` |

Every path named in `FREEZE.sha256` (15/15) and in `RESULTS.sha256` (23/23) rehashes to its printed digest. Transitive owner pins charged by `compile_p0_a_cech.py` and by `compile_square_a_prolongation.py` likewise match, including

```text
tails.json          d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
canonical JSON      6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8
owner compiler      2c7f051da265f5af3ee76007360e41af92f8492c5969846f8e529317d4dd5630
owner FREEZE        6dbf5b6118aac14c38facdd977e221b0e4648a9e875fe03867172c646e322f64
A-prolongation des. 36b8abd0383d901261a4b410c94a0ffb759e3dea37263852af86778e77d5589d
```

The two registered executions are distinct.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `max12_812_order2_p0_a_cech_20260826T112534Z_Box03_q` | `max12_812_order2_p0_a_cech_20260826T112534Z_r6d_p65521` |
| Characteristic | `0` | `65521` |
| Compiled script | `20b46bc7d695a73acafba01614cf1f27383520275db2522a9f3ee6c78d0b584b` | `eaefd2ff53a33a24c7c978ac4558e5ff325480411396fc789362efd026c04704` |
| `result.json` | `72fd6e5b5d90bee397e99ce4ee1c59dfbf2a98b6649caf6b471d6a54340fa98d` | `b1f38b69b251ae5b269fcc023b4f05d5762b5ac7e56008cc82f99e1b892172dc` |
| Stdout SHA | `2f2ffe2456ba6181ca940be602acf0671abd33a46af881edde947397ffed8965` | `2ae6c0fcc385738fafbd9e83a6058751f5b6d23b43ee967d8d908683cb5b8c2d` |
| Stderr SHA | `e3307667384b994429dbff282a1cd8edda87ef145f31128ac45c4fba00d7404a` | `512f5ba564ebbb9a5a854bc818a0f472cc3882fbdd1889ce0061c40e2952ea54` |
| Engine `rc` / swap | `0` / `0` | `0` / `0` |
| Wall / max RSS | 0.02 s / 12784 KiB | 0.01 s / 12328 KiB |

The two compiled `.sing` files become byte-identical after the single substitution `ring R=0` → `ring R=65521`. Both remote freeze checks are byte-identical (`113ed25f0aab68f7e65ef417fd070560e78091ceb3fd38cd998b0c1543924e95`) and report every `FREEZE` row `OK`. Meta `argv` is `Singular -q` on the lane-local compiled script. No file other than this review was written.

---

## 1. Complete source, then `p=0`, before any `D(p)`

The wrapper `compile_p0_a_cech.py` does not emit a new tail algebra. It loads the frozen owner-v2 compiler, checks that compiler's `EXPECTED_STATIC` and the canonical tails digest, calls `owner.emit` on all seven rows, and only then appends a `p=0` certificate by replacing the unique owner endpoint

```text
print("SQUARE_APROLONG_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE");
quit;
```

The owner reconstructs each `Phi_ell` from `tails.json` rows `1..7` with the high-contact substitutions of A-prolongation design §3,

```text
c  -> sigma^4*bs0 + sigma^5*bs1,
r  -> (p^2 + sigma^4*br0 + sigma^5*br1)/4,
n3 -> sigma^3*(a1 + sigma*aa1),
n2 -> sigma^3*(a0 + sigma*aa0),
n1 -> sigma^3*(p*(a1+sigma*aa1) + sigma^4*(e1+sigma*ee1))/2,
n0 -> sigma^3*(p*(a0+sigma*aa0) + sigma^4*(e0+sigma*ee0))/2,
k10 -> k0+sigma*k1,
```

plus `k6`, `k2` at their frozen `Lambda` weights and targets `-sigma^{2(12+ell)}` times `mu2, mu4, mu6, J/4`. Ring variables include `k6,k2,mu2,mu4,mu6,J`. Division in the owner is by `sigma^{14}` and then by `sigma`, with an exact quotient-identity sentinel; there is no `/p`. The compiled scripts contain zero matches of `/p`, `sat(`, `radical(`, or `primdec`. The unique `D(p)` token is the print string `P0_A_CECH_SOURCE_SPECIALIZATION=p=0_BEFORE_D(p)`.

The `p=0` certificate is twenty-eight polynomial substitutions `subst(*,p,0)` — four per row, `g14,g15,h14,h15` — performed after those rows already exist as elements of `Q[p,...]`. Specialization therefore commutes with the `sigma`-extraction and is not a localization. The owner also reduces `Num15+A^3` modulo `L=z^2+p/2`; that is a polynomial remainder, it is not used by the `p=0` identities, and at `p=0` it would be the weaker statement `z^2 | Num15+A^3`, which this client correctly does not promote.

---

## 2. Lower loads and targets: census, not assumption

Frozen tail cardinalities, with every monomial weight-checked against `WEIGHTS = (8,7,6,5,4,3,2, 2, 6, 10)`:

| row `ell` | monomials | `k10` | `k6` | `k2` | pure `a` | target |
|---|---|---|---|---|---|---|
| 1 | 36 | 12 | 4 | 1 | 19 | — |
| 2 | 54 | 18 | 7 | 2 | 27 | `sigma^{28} mu2` |
| 3 | 58 | 19 | 7 | 2 | 30 | — |
| 4 | 81 | 27 | 10 | 4 | 40 | `sigma^{32} mu4` |
| 5 | 89 | 30 | 11 | 4 | 44 | — |
| 6 | 120 | 40 | 16 | 7 | 57 | `sigma^{36} mu6` |
| 7 | 131 | 44 | 17 | 7 | 63 | `sigma^{38} J/4` |

Under the high-contact substitutions, `Lambda = sigma^2` places `k6` at least at `sigma^{12}` and `k2` at least at `sigma^{20}`. At `p=0` the top even coefficient `a6 = 2p` vanishes, and the remaining coefficient valuations are

```text
a5 : 4,   a4 : 4,   a3 : 5,   a2 : 5,   a1 : 8,   a0 : 8.
```

Every individual `k6` monomial therefore has `sigma`-valuation at least 20 on `p=0`; every `k2` monomial at least 24; every target at least 28. Zero `k6` terms reach grade `<= 15` at `p=0`. Absence from `g14` and `g15` is a termwise valuation fact, not a derivative sentinel and not a cancellation.

(The same census at generic `p` gives `k6` down to valuation 12 on even rows, which is why those monomials must remain in the emitter. They are killed at `p=0` by `a6=2p=0`, not by deleting them from the input. `k10`/`k0` does appear at grade fourteen, as the term `(5/32) k0 A0^2/L`, and is correctly retained.)

First corrections `aa0,aa1,bs1,br1,ee0,ee1,k1` are ring variables and occur in the printed `g15` rows. They are absent from printed `g14`, as required by the filtration.

---

## 3. Laurent / Faber convention

The owner Taylor chart is `t = 1/z` with

```text
A0 = a1 + a0 t,     B0 = bs0 + (br0/4) t,     E0 = (e1 + e0 t)/2,
```

and `h_n = [t^n] H = [z^{-n}]` of the analytic receiver. The unitriangular transform `g_ell = sum_j c_{ell j}(p) h_j` has `c_{ell j}(p)` equal to 1 if `ell=j` and equal to a positive power of `p` otherwise. At `p=0` it is the identity, so `g_n = h_n`. Row index `n` is pole order `z^{-n}`, not a reversed Faber index.

Independent expansion of the collision receivers (exact `Inv=1` at `p=0`, no truncated jet) yields, for `n=1..7`,

```text
h14[1] = -3/8 a1^2 bs0 + 5/16 a0 a1 k0 + 3/8 a1 e0 + 3/8 a0 e1
h14[2] = -3/32 a1^2 br0 - 3/4 a0 a1 bs0 + 5/32 a0^2 k0 + 3/8 a0 e0
h14[3] = -3/16 a0 a1 br0 - 3/8 a0^2 bs0
h14[4] = -3/32 a0^2 br0
h14[5] = 0
h14[6] = 0
h14[7] = 0

h15[1] = -3/4 a1 aa1 bs0 + 5/16 a1 aa0 k0 - 3/8 a1^2 bs1
         + 5/16 a0 aa1 k0 + 5/16 a0 a1 k1 + 3/8 aa1 e0 + 3/8 aa0 e1
         + 3/8 a1 ee0 + 3/8 a0 ee1
h15[2] = -3/16 a1 aa1 br0 - 3/4 a1 aa0 bs0 - 3/32 a1^2 br1
         - 3/4 a0 aa1 bs0 + 5/16 a0 aa0 k0 - 3/4 a0 a1 bs1
         + 5/32 a0^2 k1 + 3/8 aa0 e0 + 3/8 a0 ee0
h15[3] = -3/16 a1 aa0 br0 - 1/16 a1^3 - 3/16 a0 aa1 br0
         - 3/4 a0 aa0 bs0 - 3/16 a0 a1 br1 - 3/8 a0^2 bs1
h15[4] = -3/16 a0 aa0 br0 - 3/16 a0 a1^2 - 3/32 a0^2 br1
h15[5] = -3/16 a0^2 a1
h15[6] = -1/16 a0^3
h15[7] = 0
```

Specializing the seven printed exact-`Q` `g14` rows and seven printed `g15` rows at `p=0` (dropping every monomial containing `p`) reproduces these fourteen polynomials coefficientwise. A reversed index, a missing tail, a truncated `Inv` jet, or an off-by-one in `n` versus `z^{-n}` cannot manufacture that match: the next term of each geometric inverse is `O(t^8)`, while extraction stops at `t^7`, and at `p=0` the inverses are identically 1.

The design note's `(b1,b0)` dictionary is the same chart: `b1 = bs0`, `b0 = br0/4`, so `-(3/8) a1^2 b0 = -(3/32) a1^2 br0`.

---

## 4. Recomputed raw identities

Directly from the expansion of §3, without Singular sentinels:

- `[t^6] H15 = -(1/16) a0^3`. Every noncubic term of `H15` has `t`-degree at most 4 at `p=0` (`A,B,E` are linear in `t`; the `t B A^2` block is degree 4; `k A^2` is degree 2). This is identity (1), identically in `a1,B,E,k`.
- Restrict to `V(a0)`: `[t^2] H14 = -(3/32) a1^2 br0` and `[t^1] H14 = (3/8) a1 (e0 - a1 bs0)`. All other `h14[n]` vanish on `V(a0)`. These are (2a), (2b).
- After the two raw substitutions `br0=0` and `e0=a1 bs0`, the only remaining `t^3` term in `H15` is the cube: `[t^3] H15 = -(1/16) a1^3`. The `e0` substitution is not needed for this one coefficient (the leftover at `a0=br0=0` is already the cube), but it is the protocol the producer stated, and it is a raw triangular substitution rather than a radical. This is identity (3).

The same specializations applied to the printed exact-`Q` source rows give the same four equalities. The producer sentence that “the exact-`Q` printed rows themselves display (1)--(3)” is slightly loose — the printed generic rows still contain `p`-terms — but after the stated `p=0` (and, for (2)--(3), `a0=0` and the two pivots) they are exactly (1)--(3).

---

## 5. Triangular / unit deductions over `Q`

On `D(a0)`: (1) lies in the source ideal as a polynomial. In the localized ring `Q[a0,a0^{-1},...]`, `-(1/16) a0^3` is a unit (`16` and `a0` are units). The localized quotient is the zero ring. There is no nilpotent leftover on this open: one does not pass through `a0^3=0` unlocalized.

On `V(a0) intersect D(a1)`: (2a) is `-(3/32) a1^2 br0`. The coefficient `-3/32` is a unit in `Q` and `a1^2` is a unit on `D(a1)`, so `br0=0` in the raw localized quotient. Then (2b) is `(3/8) a1 (e0-a1 bs0)`, again a unit times a linear generator, so `e0=a1 bs0`. These are monic (up to units) linear equations. Substitution of the two solved generators into `g15[3]` is remainder modulo that triangular ideal, not a radical membership test and not a saturation. The compiled certificate implements exactly `subst(a0,0)`, then those two substitutions, then polynomial equality against `-(1/16) a1^3`. No `std`, `sat`, or `radical` occurs.

After the pivots, `g15[1]` and `g15[2]` remain nonzero (they still involve `bs1, br1, aa0, aa1, k0, ee0, e1`). They are irrelevant: a unit already empties the chart.

Denominators that appear are `2,4,8,16,32`. All are units in `Q`. None is a hidden `p`.

---

## 6. Exact-`Q` lane versus `F_65521`

The characteristic-zero algebra is the printed Box03 rows together with the independent expansion of §3. The r6d lane is a software control on a second host with a second ring.

Independently: every printed `F_65521` coefficient is the reduction of the corresponding exact-`Q` coefficient. Fourteen of fourteen rows match after `a/b |-> a b^{-1} (mod 65521)`. Sample: `-1/16 ≡ 4095`, `3/32 ≡ 26618` (so the printed r6d term `-26618 br0 a1^2` is the image of `-3/32 br0 a1^2`), `-3/8 ≡ 24570`, and printed `g15_6` on r6d is `26618 p a0 a1^2 + 4095 a0^3`, the image of `3/32 p a0 a1^2 - 1/16 a0^3`.

The units of §5 remain nonzero in `F_65521`:

```text
1/16 ≡ 61426,   3/32 ≡ 26618,   3/8 ≡ 40951,   5/32 ≡ 22523  (all nonzero).
```

`65521` does not divide `2,3,5,16`. The modular identities cannot collapse. They also cannot prove the `Q` identities; they were not so used.

Both evidence collections hash to the frozen `RESULTS.sha256` inputs. `input_sha256` in each `result.json` equals the compiled script actually run. Scope strings in both `result.json` files are `FIXED_P0_HIGH_CONTACT_A_CECH_G14_G15_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT`.

---

## 7. `R=C=0` routing and residual-chart scope

Leading collision `R = cs z + rs/4` and leading `C` are not set to zero by an extra ideal membership. They are routed by the registered high-contact substitutions: `Lambda cs` starts at `sigma^4`, so the `sigma^0` coefficient of leading `R` vanishes and the first retained jet is `B0`. Likewise `C` starts at `sigma^4`. This is the same cone the generic-square `A`-prolongation theorem already treated on `D(p)`, now specialized to the collision fibre before any `D(p)`. On that fibre the square-centre summand `p^2/4` of `r` also vanishes, which is the collision and not an omitted `R` direction.

Inside the stated cone, through grades fourteen and fifteen, the first corrections `A1,B1,E1,k1` are retained and appear in `g15`. The `C`-nilpotent thickening

```text
(c0^2, c0 c1, (3/8) a0 c0 + (3/32) c1^2, (3/8)(a1 c0 + a0 c1))
```

of ramified-closure design (1.4) is the pair of `C` opens in the candidate Cech table, not this client: those opens are already units at grade ten (`E4=(3/32)c0^2`, `E2=(3/32)c1^2` on the reduced support). This certificate is the next two opens, `V(rs,cs,c0,c1) intersect D(a0)` and `V(rs,cs,c0,c1,a0) intersect D(a1)`, in the high-contact filtration.

Omitted from the stated scope, and not claimed:

- lower Newton valuations `ord_sigma(R)=1` and `ord_sigma(C) in {1,2,3}`;
- the all-zero higher-contact receiver (the complement of the six collision opens);
- a second-correction jet `B2,E2,A2` (grades 14/15 of this cone do not see it);
- moving `p`.

None of those omissions falsifies a *fixed-`p=0` high-contact residual-`A`-chart* theorem. They falsify any attempt to read this as exhaustion of `V(rs,cs)` as a full Newton fan.

---

## 8. Quarantine of generic V12 / unbounded `d=1` / eight-form fan

The generic-square `r=1` / symbolic unique-`AC` / unbounded `d=1` (V12) package stands at `ORDER2_SQUARE_R1_D1_V12_REPAIR`. The eight-form fan is known to omit lower-load `k6/k2` terms at larger `a`. Both remain quarantined navigation. They are not inputs to this replay: the emitter is the complete `u2_62` tails with `k6` and `k2` monomials in every row (census of §2), and the `p=0` absence of those loads at grades fourteen and fifteen is a valuation computation on that complete source.

This fixed-`p=0` source replay is therefore independent of that defect. It must not be composed with V12 or eight-form statements.

---

## 9. Scope firewall

This certificate cannot, by itself, prove any of the following:

- that the cusp, odd, two `C`, and two `A` opens are pullbacks of one total raw Kummer/Rees family (Gate T);
- empty-special-fibre propagation, or exclusion of any positive-valuation moving-`p` arc;
- emptiness of the all-zero higher-contact receiver;
- the boundary `k0=0`;
- terminal or Taylor closure;
- the whole square branch, all of order two, `(8,12)`, maximum twelve, or JC2.

The generic-square `A`-prolongation theorem on `D(p)` (already reviewed) is a different open: there `L` is squarefree of degree two and `L | A0^3` forces `A0=0`. At `p=0`, `L=z^2` is not squarefree, that implication fails, and the residual Cech analysis of (1)--(3) is the replacement. The two theorems do not compose without the total-family glue.

Ramified-closure design §7 already states this firewall. The producer `RESULT.md` restates it. This review enforces it.

---

## Maximal theorem scope

On the collision fibre `p=0` of the complete frozen seven-row ordinary source, in the single high-contact cone `Lambda=sigma^2`, `ord_sigma(R)>=2`, `ord_sigma(C)>=4`, with first corrections `A1,B1,E1,k1` retained, ordinary dictionary `B0=bs0 z+br0/4`, `B1=bs1 z+br1/4`, `E0=(e1 z+e0)/2`, `E1=(ee1 z+ee0)/2`, and with `k6,k2` and every target present in the emitter, the raw source rows at absolute grades fourteen and fifteen equal the negative Laurent coefficients of the collision receivers `h14,h15`. The sixth grade-fifteen row is the polynomial `-(1/16) a0^3`, a unit on `D(a0)`, so that open is empty over `Q`. On `V(a0) intersect D(a1)` the deepest two grade-fourteen rows are unit-triangular in `br0` and `e0-a1 bs0`; after those two raw equations the third grade-fifteen row is the polynomial `-(1/16) a1^3`, a unit on `D(a1)`, so that open is empty over `Q`. Exact `Q` is the characteristic-zero statement; `F_65521` is an independent good-prime control.

## Remaining composition debts

1. Raw Cech client: prove the six ordered collision opens cover the normalized projectivized grade-ten support, print overlap maps, and route the all-zero complement explicitly. The two `C` opens are elementary from (1.1); the odd unit and the cusp grade-twelve unit are separately confirmed on their own opens; they are not yet glued as pullbacks of one total chart.
2. Gate T: one total unspecialized-`p` Kummer/Rees source algebra with identities `s = sum H_i F_i + rho H` on every chart, denominators powers of registered units only.
3. Positive-valuation moving-`p` exclusion, which is licensed only after Gate T (or, failing that, the exact three-wall Kummer fan of design §5, not sampled slopes).
4. Lower Newton cones at `p=0` with `ord_sigma(R)=1` or `ord_sigma(C) in {1,2,3}`.
5. The all-zero higher-contact receiver, `k0=0`, both Taylor families, and terminal `[6,2]`.
6. Quarantine remains in force on generic V12 / unbounded `d=1` and the eight-form fan.
7. None of the above, and not this certificate, closes the square branch, order two, `(8,12)`, maximum twelve, or JC2.

CONFIRMED
