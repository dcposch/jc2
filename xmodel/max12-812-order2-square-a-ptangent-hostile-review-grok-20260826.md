# Hostile review — moving-`p` addendum to the generic-square high-contact `A`-prolongation

| Field | Value |
|---|---|
| Targets | V5 `RESULT.md`, `FREEZE.sha256`, `RESULTS.sha256`; V4 `compile_square_a_ptangent_v4.py`, `FREEZE.sha256`; V3 `compile_square_a_ptangent.py` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Charged reviews and producer status lines are not evidence |
| Method | source reading, SHA-256 of every named pin and evidence file, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of all six required primary pins match. Every path named in V5 `FREEZE.sha256` (6 rows), V5 `RESULTS.sha256` (31 rows), V4 `FREEZE.sha256` (7 rows), and the V3 freeze named by V4 (9 rows) rehashes to the printed digest. V3 and V4 are preserved as failures and are not accepted endpoints. Producer verdict language, both V5 status lines, and both good-prime lanes were not used as characteristic-zero algebra. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the already certified high-contact cone `ord_sigma(R)>=2`, `ord_sigma(C)>=4` on `D(p*k0)`, the first tangent `p -> p+2*sigma*ell` of the generic-square base is exactly the substitution

```text
L(sigma) = z^2 + p/2 + sigma*ell,
K = L(sigma)^2 + sigma^4 B0 + sigma^5 B1 + ...,
D = L(sigma) A0 + sigma L(sigma) A1 + sigma^4 E0 + sigma^5 E1 + ....
```

Keeping `L(sigma)` together, the complete negative receiver through total sigma grade fifteen is the frozen-`p` pair `(h14, h15fixed)` plus the single extra grade-fifteen summand

```text
Delta h = ell * partial_L(h14)
        = -(3/4) ell A0 E0 / L^2
          +(3/4) ell B0 A0^2 / L^3
          -(5/32) ell k0 A0^2 / L^2.
```

Clearing `16 L^3` yields

```text
Delta = -12 ell L A0 E0 + 12 ell B0 A0^2 - (5/2) ell k0 L A0^2.
```

Every additional piece obtained by differentiating `K` and `D` separately combines into this `Delta`; none remains outside it. In particular the denominator contribution `-(3/2) ell A0 E0 / L^2` and the numerator contribution `+(3/4) ell A0 E0 / L^2` net to `-(3/4) ell A0 E0 / L^2`, which is the first summand of `Delta h`. The prior hostile review's §6 concern is therefore a splitting artefact, not a missing term.

The polynomial identities

```text
Num14  == -12 B0 A0^2     (mod L),
Delta  ==  12 ell B0 A0^2 (mod L),
Delta  == -ell Num14      (mod L)
```

are identities of polynomials and do not require an engine. Grade fourteen already forces `L | B0 A0^2`, hence `L | Delta`. After that equation,

```text
Num15moving == -A0^3      (mod L).
```

On `D(p)`, `L` is squarefree of degree two and `deg A0 <= 1`, so `A0 = 0`. The omitted first tangent along the generic square component does not change the fixed-`p` high-contact conclusion.

The seven frozen complete-source rows, with `p` replaced by `p+2*sigma*ell` in every ordinary coefficient, remain `sigma^{14}`-divisible. Their grades fourteen and fifteen are the lower-unitriangular image

```text
g14 = T(p) h14,
g15 = T(p) h15moving + 2 ell (dT/dp)(p) h14,
```

with the factor two coming from `p+2*sigma*ell`. This is a theorem about the first `p`-tangent of one already certified high-contact cone, not a Newton-fan exhaustion, not a higher `p`-jet, not `p=0`, and not an order-two, `(8,12)`, maximum-twelve, or JC2 theorem.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Six primary pins | hashes | all six match the required bytes |
| 1. Named manifests | every named file | V5 `FREEZE` 6/6, V5 `RESULTS` 31/31, V4 `FREEZE` 7/7, V3 `FREEZE` 9/9 |
| 1. V5 dual AWS | tags, hosts, rc, validator | distinct `081800Z` tags on Box03 / r6d; engine `rc=0`; validator `PASS_SQUARE_APROL_PTANGENT_V5`; zero swap |
| 1. V3 | pre-engine wrapper-anchor failure | both lanes `compiler_rc=1`, `RuntimeError: owner analytic/end anchor missing`; empty `run/`; not an endpoint |
| 1. V4 | engine-pass / validator-prefix failure | both lanes engine `rc=0`, stdout byte-identical to V5; validator `FAIL_MISSING_OR_NONUNIQUE:SQUARE_APROL_SIGMA14_DIVISIBLE=1`; not an endpoint |
| 1. V5 vs V4 | four validator strings | compiled `.sing` files byte-identical to V4; exactly four source-extraction prefixes lengthened `APROL` to `APROLONG` |
| 2. Source substitution | `p -> p+2*sigma*ell` | exact in leading coefficient, `r`, `n1`, `n0`, and all seven loaded `Phi` rows; reconstructs `L(sigma)`, `K`, `D` |
| 3. Complete moving receiver | binomial expansion of `K` and `D` | net `ell * partial_L(h14)`; cleared numerator is the displayed `Delta`; no leftover |
| 3. Prior review §6 | extra `1/K` and `D` pieces | denominator `-3/2 ell A E/L^2` plus numerator `+3/4 ell A E/L^2` net to `-3/4 ell A E/L^2`, inside `Delta` |
| 4. Moving Faber | `g14=T(p)h14`, `g15=T(p)h15moving+2ell (dT/dp)(p) h14` | unit diagonal, even parity, factor two, and all seven compiled `T`/`dT` rows recovered by hand |
| 4. Source vs analytic | replay versus insertion | source reconstructs tails; analytic inserts `(h14, H15fixed+DeltaH)` independently; printed rows 1--3 of grade fifteen match the insertion |
| 5. Separator | `Num14`, `Delta`, `Num15moving` | three displayed congruences are polynomial identities; grade fourteen kills `Delta` modulo `L`; grade fifteen still gives `L | A0^3`, hence `A0=0` |
| 6. Scope | first tangent only | lower rays, higher `p` jets unless formally implied, `p=0`, fan exhaustiveness, the square branch, order two, `(8,12)`, maximum twelve, and JC2 remain open |

---

## 1. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../owner_v5_ptangent_validator_20260826/RESULT.md` | `74551fe8b2ed1e4b9b1fd1594cee54e3bd3d87e6acee8b8c29d9384f5317d5ea` | V5 endpoint |
| `.../owner_v5_ptangent_validator_20260826/FREEZE.sha256` | `a2a665a4771f2941a8b64babb9fed35ddc877ce81af2e3fcf75f8a56b5ea1e94` | V5 source freeze |
| `.../owner_v5_ptangent_validator_20260826/RESULTS.sha256` | `380245162296ae04a2cdcc677b04d4617bd415e09665c999090bfab1741839a6` | V5 evidence freeze |
| `.../owner_v4_ptangent_retry_20260826/compile_square_a_ptangent_v4.py` | `657d0461778a3d2b0b0f532c0bf857e2ee71ac1b55abc869667f72d3fdabc11f` | V4 compiler (V5's mathematical client) |
| `.../owner_v4_ptangent_retry_20260826/FREEZE.sha256` | `6977fbcdb9f446dd5c794a1c33438bc60e3ea14784d7269b25288515b750d09c` | V4 source freeze |
| `.../owner_v3_ptangent_20260826/compile_square_a_ptangent.py` | `322f20ae93c98fe6373cf36e2c5f359646a4de44ea14188c38a4f8b0b3df6488` | V3 wrapper (source of the moving substitutions and analytic block) |

A passing sentinel or manifest is not mathematics. The algebra below is independent of those sentinels.

### Chain V5 → V4 → V3 → owner-v2

V5 `FREEZE` pins the unchanged V4 compiler and the V4 freeze. V4 `FREEZE` pins the V3 compiler and the V3 freeze. V3 `FREEZE` pins owner-v2 `compile_square_a_prolongation.py` (`2c7f051da265f5af3ee76007360e41af92f8492c5969846f8e529317d4dd5630`), owner-v2 `FREEZE.sha256` (`6dbf5b6118aac14c38facdd977e221b0e4648a9e875fe03867172c646e322f64`), owner-v2 `RESULT.md` (`eba4640a9c7da51e4297e7e0b3c236f73f2eb2f70770de0634e1d0fea652d13f`), and owner-v2 `RESULTS.sha256` (`3f3d729ed046431e92a6cbd1f5e373526525f39422a495fe9d66def8476a6e80`). All of those bytes rehash on this review.

V3 is a thin AWS wrapper around frozen owner-v2: it replaces `source_coefficients` by the moving substitutions of §2, inserts `ell` in the ring, and splices an independent analytic block in place of the owner-v2 Faber/separator. The splice is keyed on the owner-v2 endpoint string. V3 searches for the shortened anchor `SQUARE_APROL_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE`. Frozen owner-v2 emits `SQUARE_APROLONG_ENDPOINT=...`. Both V3 lanes therefore die in the compiler with `RuntimeError: owner analytic/end anchor missing`, `compiler_rc=1`, and empty `run/` directories. The on-disk V3 `.sing` files are the unfinished emit: `p+2*sigma*ell` is already present in every `Phi` row (1688 occurrences), but the ring still lacks `ell` and the analytic block is still the frozen-`p` owner-v2 separator. V3 never launched an engine. It is not an endpoint.

V4 loads frozen V3 and changes only that wrapper anchor to `SQUARE_APROLONG_ENDPOINT`. Source substitutions, `transform_pair`, `analytic_block`, and sentinels remain byte-derived from V3. Both V4 lanes compile (`compiler_rc=0`) and run (`engine_rc=0`) on distinct hosts, and print every required mathematical sentinel, including `SQUARE_APROLONG_SIGMA14_DIVISIBLE=1` and `SQUARE_APROL_PTANGENT_ENDPOINT=PASS_MOVING_P_SOURCE_ROW_ADDENDUM`. V4's validator still required the four shortened prefixes `SQUARE_APROL_SIGMA14_DIVISIBLE=1`, `SQUARE_APROL_SIGMA15_DIVISIBLE=1`, `SQUARE_APROL_QUOTIENT_IDENTITIES=1`, `SQUARE_APROL_FORBIDDEN=1`. Both validators are `FAIL_MISSING_OR_NONUNIQUE:SQUARE_APROL_SIGMA14_DIVISIBLE=1`. V4 is an engine-pass / validator-prefix failure. It is not an endpoint.

V5 invokes the same V4 compiler and changes those four validator strings to the owner-v2 spelling `SQUARE_APROLONG_*`. The compiled scripts are byte-identical to V4 (`18fdf6f936883ffe582f003a31e335c601b8898e820af053345d1a757b63863d` over `Q`, `3bc34f8a3a55dfdd0f174e4e8634b40ec8c666b8b333d8c319057f26b3df10e4` over `F_65521`). The two stdout streams are likewise byte-identical to V4. Administrative extras in V5 `run_aws.sh` / `launch_host.sh` are the V5 freeze path, the `v5` tag prefix, and the success token `PASS_SQUARE_APROL_PTANGENT_V5`; they do not touch the mathematical client. Of the validator required-list, exactly the four source-extraction prefixes changed.

### Four registered executions, of which two are the V5 endpoints

| Charge | V3 exact `Q` | V3 `F_65521` | V4 exact `Q` | V4 `F_65521` | V5 exact `Q` | V5 `F_65521` |
|---|---|---|---|---|---|---|
| Host | `ip-172-30-0-249` (Box03) | `ip-172-30-0-45` (r6d) | Box03 | r6d | Box03 | r6d |
| Tag | `..._v3_ptangent_q_20260826T081200Z_box03` | `..._v3_ptangent_p65521_20260826T081200Z_r6d` | `..._v4_ptangent_q_20260826T081500Z_box03` | `..._v4_ptangent_p65521_20260826T081500Z_r6d` | `..._v5_ptangent_q_20260826T081800Z_box03` | `..._v5_ptangent_p65521_20260826T081800Z_r6d` |
| Characteristic | never launched | never launched | `0` | `65521` | `0` | `65521` |
| Compiler | V3 wrapper | V3 wrapper | V4, pinning V3 | V4, pinning V3 | same V4 binary | same V4 binary |
| Compiled script | unfinished emit | unfinished emit | `18fdf6f9...757b63863d` | `3bc34f8a...b3df10e4` | identical to V4 | identical to V4 |
| Compiler `rc` | `1` | `1` | `0` | `0` | `0` | `0` |
| Engine `rc` | none | none | `0` | `0` | `0` | `0` |
| Validator | none | none | `FAIL_MISSING_OR_NONUNIQUE:SQUARE_APROL_SIGMA14_DIVISIBLE=1` | same | `PASS_SQUARE_APROL_PTANGENT_V5` | `PASS_SQUARE_APROL_PTANGENT_V5` |
| Stdout SHA | none | none | `933e6a87342e0797641206ede622136a841ba76cd9f5c96da3f8e33a45be1fd0` | `dfd0be88c169e258ed4d68509e77bc111a01770d94b04bd574ead6eff65b0383` | identical to V4 | identical to V4 |
| Elapsed / peak RSS / swap | n/a | n/a | 0.04 s / 15,452 KiB / 0 | 0.02 s / 12,356 KiB / 0 | 0.04 s / 15,380 KiB / 0 | 0.02 s / 12,884 KiB / 0 |
| Launcher PID | `184046` | `249537` | `184856` | `250114` | `185278` | `250560` |
| Start UTC | `2026-08-26T08:12:00Z` pre-reg | same | `2026-08-26T08:16:03Z` | `2026-08-26T08:16:03Z` | `2026-08-26T08:18:46Z` | `2026-08-26T08:18:46Z` |
| Endpoint? | no | no | no | no | **yes** | **yes** |

V5 caps are 16 GiB VM (`16777216` KiB), 600-second compiler, 3600-second engine, matching registration. Both V5 `freeze_check.stdout` records report every freeze row OK. Both metas record `argv` as `Singular -q` on the lane-local compiled script, return code 0, and stdout hashes matching `RESULT.md` and `RESULTS.sha256`. Resource figures match `/usr/bin/time -v` on the two V5 stderr streams. Within the V5 package the two compiled scripts differ by the ring-characteristic token (`ring R=0` versus `ring R=65521`); substitutions, load weights, analytic block, and sentinels are otherwise identical. The two V5 validation files are byte-identical two-line payloads `engine_rc=0` / `validator=PASS_SQUARE_APROL_PTANGENT_V5`; that shared payload is not evidence that the runs were copied.

---

## 2. Source substitution

Start from the ordinary monic-quartic chart of frozen owner-v2

```text
K = z^4 + p z^2 + c z + r,
N = n3 z^3 + n2 z^2 + n1 z + n0,
```

with

```text
c  = sigma^4 bs0 + sigma^5 bs1,
r  = (p^2 + sigma^4 br0 + sigma^5 br1)/4,
n3 = sigma^3 (a1 + sigma aa1),
n2 = sigma^3 (a0 + sigma aa0),
n1 = sigma^3 (p (a1+sigma aa1) + sigma^4 (e1+sigma ee1))/2,
n0 = sigma^3 (p (a0+sigma aa0) + sigma^4 (e0+sigma ee0))/2,
```

and loaded source rows built from the seven coefficient slots

```text
(6)  2 p,
(5)  2 c,
(4)  p^2 + 2 r,
(3)  2 p c + sigma^2 n3,
(2)  c^2 + 2 p r + sigma^2 n2,
(1)  2 c r + sigma^2 n1,
(0)  r^2 + sigma^2 n0.
```

V3's `moving_source_coefficients` (invoked unchanged by V4/V5) replaces every occurrence of the base parameter by `p+2*sigma*ell`:

```text
P  = p + 2*sigma*ell,
c  = sigma^4 bs0 + sigma^5 bs1,                          (unchanged)
r  = (P^2 + sigma^4 br0 + sigma^5 br1)/4,
n3 = sigma^3 (a1 + sigma aa1),                           (unchanged)
n2 = sigma^3 (a0 + sigma aa0),                           (unchanged)
n1 = sigma^3 (P (a1+sigma aa1) + sigma^4 (e1+sigma ee1))/2,
n0 = sigma^3 (P (a0+sigma aa0) + sigma^4 (e0+sigma ee0))/2,
```

and writes `(6)=2 P`, `(4)=P^2+2 r`, `(3)=2 P c + sigma^2 n3`, `(2)=c^2+2 P r+sigma^2 n2`. The compiled V5 `Phi` rows contain this string in every slot: 1688 occurrences of `p+2*sigma*ell`, including `2*((p+2*sigma*ell))`, `((p+2*sigma*ell))^2+sigma^4*br0`, `((p+2*sigma*ell))*(a1+sigma*aa1)`, and `((p+2*sigma*ell))*(a0+sigma*aa0)`.

This is exactly the first tangent of `L`. Because `L = z^2 + p/2`, the increment `delta L = sigma*ell` is `delta p = 2 sigma ell`. Then

```text
L(sigma) = z^2 + P/2 = z^2 + p/2 + sigma*ell,
L(sigma)^2 = z^4 + P z^2 + P^2/4,
K - L(sigma)^2 = c z + (sigma^4 br0 + sigma^5 br1)/4
               = sigma^4 (bs0 z + br0/4) + sigma^5 (bs1 z + br1/4)
               = sigma^4 B0 + sigma^5 B1,
```

with the frozen ordinary identification `B_i = bs_i z + br_i/4`. For the numerator, `M = sigma^3 (A0 + sigma A1)` remains independent of `p`, while

```text
N = L(sigma) M + Lambda S,
D = N / sigma^3 = L(sigma) (A0 + sigma A1) + sigma^4 (E0 + sigma E1) + ...,
```

with `E_i = (e1_i z + e0_i)/2` as in the fixed-`p` review: the `P A / 2` pieces of `n1,n0` are the constant term of `L(sigma)` times `A`, and the `sigma^4 e_i / 2` pieces are `C`. This is the registered high-contact cone with moving base, not a different cone.

`n3` and `n2` correctly do *not* depend on `p`. A substitution that moved those slots would have been a different, wrong tangent.

---

## 3. Complete moving receiver, and reconciliation with the prior review

Write `f = K^2 + sigma^5 D` on the cone, `X = sigma^5 D / K^2`, and keep the already-charged load `sigma^4 k10` with `k10 = k0 + sigma k1`. Through total grade fifteen the binomials are the same as in the fixed-`p` review:

```text
f^{3/2}
  = K^3 + (3/2) sigma^5 K D + (3/8) sigma^{10} D^2/K
    - (1/16) sigma^{15} D^3/K^3 + O(sigma^{20}),

sigma^4 k10 f^{5/4}
  = sigma^4 k10 K^{5/2} + (5/4) sigma^9 k10 D K^{1/2}
    + (5/32) sigma^{14} k10 D^2 / K^{3/2} + O(sigma^{19}).
```

The honest way to expand `K` and `D` together is to keep `L(sigma)` as a unit:

```text
K = L(sigma)^2 ( 1 + sigma^4 B0/L(sigma)^2 + sigma^5 B1/L(sigma)^2 + O(sigma^6) ),
D = L(sigma) (A0 + sigma A1) + sigma^4 E0 + sigma^5 E1 + O(sigma^6).
```

`L(sigma)` is polynomial in `z`, so `K^3`, `K D`, `L(sigma)^5`, and the grade-nine `D K^{1/2}` term remain polynomial in `z`. The first nonpolynomial `Y^3` piece of `K^{5/2}` is still total grade sixteen after the `sigma^4` charge. `k6` is still charged at `sigma^{12}` with first nonpolynomial at twenty; `k2` and both Taylor families and the terminal row remain later. Squared `B`-corrections start at `sigma^8` and cannot affect `D^2/K` through relative grade five.

Thus

```text
D^2 / K
  = (A0 + sigma A1)^2
    + sigma^4 ( 2 A0 E0 / L(sigma) - B0 A0^2 / L(sigma)^2 )
    + sigma^5 ( 2 (A0 E1 + A1 E0)/L(sigma)
                - (B1 A0^2 + 2 B0 A0 A1)/L(sigma)^2 )
    + O(sigma^6),
```

and the leading `(A0+sigma A1)^2` is polynomial. Negative parts of `sigma^{10} D^2/K` therefore start at total grade fourteen. Expanding `L(sigma)^{-1} = L^{-1} - sigma ell / L^2 + O(sigma^2)` and `L(sigma)^{-2} = L^{-2} - 2 sigma ell / L^3 + O(sigma^2)` splits those negative parts as

```text
grade 14:  (3/4) A0 E0 / L - (3/8) B0 A0^2 / L^2,

grade 15 frozen:
  (3/4)(A0 E1 + A1 E0)/L - (3/8)(B1 A0^2 + 2 B0 A0 A1)/L^2,

grade 15 moving from D^2/K:
  (3/8) ( -2 ell A0 E0 / L^2 + 2 ell B0 A0^2 / L^3 )
  = -(3/4) ell A0 E0 / L^2 + (3/4) ell B0 A0^2 / L^3.
```

The cubic `-(1/16) sigma^{15} D^3/K^3` contributes `-(1/16) A0^3 / L^3` at grade fifteen; the first `ell`-correction of `D^3/K^3` is grade sixteen.

The charged quadratic is

```text
D^2 / K^{3/2} = (A0 + sigma A1)^2 / L(sigma) + O(sigma^4),
```

so

```text
grade 14:  (5/32) k0 A0^2 / L,
grade 15 frozen:  (5/32)(k1 A0^2 + 2 k0 A0 A1)/L,
grade 15 moving from k10:  -(5/32) ell k0 A0^2 / L^2.
```

The `B0` correction inside `1/K^{3/2}` is `sigma^4` and is pushed to total grade eighteen. Adding these, the complete negative receivers are

```text
h14 = [ (3/4) A0 E0 / L
       -(3/8) B0 A0^2 / L^2
       +(5/32) k0 A0^2 / L ]_-,

h15moving = h15fixed + Delta h,
```

with `h15fixed` the frozen-`p` grade-fifteen receiver of the previous review and

```text
Delta h = -(3/4) ell A0 E0 / L^2
          +(3/4) ell B0 A0^2 / L^3
          -(5/32) ell k0 A0^2 / L^2.
```

Differentiating the frozen rational function `h14` in the direction `L |-> L + sigma ell` produces exactly `partial_L(h14)`, and `Delta h = ell * partial_L(h14)`. Clearing `16 L^3` yields the displayed numerator

```text
Delta = -12 ell L A0 E0 + 12 ell B0 A0^2 - (5/2) ell k0 L A0^2.
```

The compiled `DeltaH` / `DeltaNum` are this rational function and this numerator, encoded in the same `t=1/z` generating function as frozen owner-v2 (`Inv2` truncates `1/(1+(p/2) t^2)^2`, `Inv3` truncates the cube; `t^2 A0 E0 Inv2` is `A E / L^2` because `A0` is already `A/z`).

### Reconciliation with prior review §6

The previous hostile review differentiated `h14` and obtained the displayed `Delta`, then worried that a genuine moving `K = (L + sigma ell)^2 + sigma^4 B0 + ...` produces extra grade-fifteen pieces from `1/K`. The example given there is the action of the linear correction `2 sigma L ell` in `K` on the `sigma^4` piece `2 L A0 E0` of `D^2`:

```text
(3/8) sigma^{10} * (2 L A0 E0) * (-2 ell / L^3)
  = -(3/2) ell A0 E0 / L^2.
```

That term is real. It is not the whole `A0 E0` moving contribution. The same correction of `D = (L + sigma ell) A0 + sigma^4 E0 + ...` produces the cross term `2 (sigma ell A0) (sigma^4 E0)` in `D^2`, which contributes

```text
(3/8) sigma^{10} * 2 ell A0 E0 / L^2
  = +(3/4) ell A0 E0 / L^2
```

at grade fifteen. Combining rather than counting separately,

```text
-3/2 + 3/4 = -3/4,
```

so the net `A0 E0` moving piece is `-(3/4) ell A0 E0 / L^2`. This is precisely the first summand of `Delta h`, equivalently the first summand of `ell * partial_L(h14)`, equivalently the packaging `2 A0 E0 / L(sigma)` obtained by keeping `K = L(sigma)^2` in the leading part of `D^2/K`. Clearing `16 L^3` of this net term produces `-12 ell L A0 E0`, the first summand of `Delta`.

The `B0` moving piece has no numerator counterpart ( `B` lives in `K`, not in `D` ). The denominator expansion of `-(3/8) B0 A0^2 / L(sigma)^2` contributes `+(3/4) ell B0 A0^2 / L^3`, which clears to `+12 ell B0 A0^2`. The `k10` moving piece is the expansion of `(5/32) k0 A0^2 / L(sigma)` and clears to `-(5/2) ell k0 L A0^2`. No further negative contribution exists through grade fifteen: the `sigma^2 ell^2` summand inside `L(sigma)^2` cancels in the leading `D^2/K = (A0+sigma A1)^2` and does not enter the negative part before relative grade six.

The prior review's derivative identity is therefore the complete moving-`p` coefficient of `sigma^{15}`, not merely a derivative of a frozen formula. The extra `K` and `D` pieces are the splitting of that derivative, and they lie inside `Delta`. Nothing remains to quarantine.

A naive expansion of `1/K` about frozen `L^2` without the compensating `D` pieces would have produced a spurious grade-eleven term `-2 ell A0^2 / L` from `A0^2 * (-2 sigma ell / L)/L^2`. The `sigma^1` piece of `D^2`, namely `2 L A0 * (ell A0)`, supplies `+2 ell A0^2 / L` and cancels it. Keeping `L(sigma)` together never writes that phantom down.

---

## 4. Moving Faber transform

The square-base row transform is the coefficient of `w^{-ell}` in `z^{-j}` under `w^2 = z^2 + P/2`, equivalently

```text
q^2 + ((p + 2 sigma ell)/2) v^2 = 1,    q = z/w,    v = 1/w.
```

At `sigma = 0` this is the frozen `T(p)` of owner-v2. The binomial

```text
z^{-j} = w^{-j} (1 - (P/2) w^{-2})^{-j/2}
```

has `T_{ell,ell}(P) = 1`, vanishes for `ell < j` or odd `ell-j`, and otherwise equals

```text
(j/2)(j/2+1)...(j/2+n-1) / n!  *  (P/2)^n,     n = (ell-j)/2.
```

The compiled `transform_pair` writes exactly that coefficient of `p^n` as the `sigma=0` value, and writes

```text
d/dsigma T(p + 2 sigma ell) |_{sigma=0} = 2 n * (coefficient of p^n) * ell * p^{n-1}
```

as the first tangent. Because `dP/dsigma = 2 ell`, this is `2 ell (dT/dp)(p)`. The factor two is mandatory: a factor-one insertion would have been the derivative along `p |-> p + sigma ell`, which is the wrong chart.

The linearization

```text
T(P) h(sigma) = T(p) h14
              + sigma ( T(p) h15moving + 2 ell (dT/dp)(p) h14 )
              + O(sigma^2)
```

is exact at grades fourteen and fifteen: `O(sigma^2)` in the jet of `T` or of `h` is total grade sixteen relative to the `sigma^{14}` extraction. Source substitution is the full finite `p+2*sigma*ell` (including `(sigma ell)^2` in `r` and in `L(sigma)^2`); analytic comparison only needs the first-order formula, and the extra finite pieces do not reach these two grades in the negative receiver (§3).

Hand recovery of all seven compiled rows, not using the remainder sentinels:

| `ell` | `T(p)` support | `2 ell (dT/dp)(p)` support | compiled `Check15` |
|---:|---|---|---|
| 1 | `h_1` | none (`n=0`) | `g15_1 - h15_1` |
| 2 | `h_2` | none (odd gap) | `g15_2 - h15_2` |
| 3 | `(p/4) h_1 + h_3` | `(ell/2) h14_1` | matches |
| 4 | `(p/2) h_2 + h_4` | `ell h14_2` | matches |
| 5 | `(3/32) p^2 h_1 + (3/4) p h_3 + h_5` | `(3/8) ell p h14_1 + (3/2) ell h14_3` | matches |
| 6 | `(1/4) p^2 h_2 + p h_4 + h_6` | `ell p h14_2 + 2 ell h14_4` | matches |
| 7 | `(5/128) p^3 h_1 + (15/32) p^2 h_3 + (5/4) p h_5 + h_7` | `(15/64) ell p^2 h14_1 + (15/8) ell p h14_3 + (5/2) ell h14_5` | matches |

Unit diagonal is 1; odd `ell-j` is zero. Grade fourteen uses only `T(p)`, as required.

### Source replay versus analytic insertion

The frozen tails are replayed with the moving substitutions of §2; `g14_ell` and `g15_ell` are the `sigma^0` and `sigma^1` coefficients of `Phi_ell / sigma^{14}`. Independently, the analytic block inserts `H14` and `H15fixed + DeltaH` as generating functions in `t` and compares. The source does not contain `h14` or `h15`.

Independent hand checks on the exact-`Q` printed rows:

- All seven `g14` polynomials equal the frozen owner-v2 `g14` polynomials, including the vanishing sixth row. The first tangent is invisible at `sigma^0`. This is source replay, not insertion.
- `g15` row 1 equals frozen owner-v2 `g15` row 1. `DeltaH` starts at `t^2`, and `T_{1,j}` has no off-diagonal, so there is no `ell` at `w^{-1}`.
- `g15` row 2 equals frozen owner-v2 `g15` row 2 plus `[t^2] DeltaH = -(3/8) ell a1 e1 - (5/32) ell k0 a1^2`. No Faber mixing (`T_{2,1}=0`). The two extra monomials `-3/8*a1*e1*ell` and `-5/32*a1^2*k0*ell` are exactly those printed.
- `g15` row 3 equals frozen owner-v2 `g15` row 3 plus `[t^3] DeltaH + (1/2) ell h14_1`. Combining gives the four printed `ell` monomials `+(9/16) bs0 a1^2 ell - (5/32) a0 a1 k0 ell - (3/16) a1 e0 ell - (3/16) a0 e1 ell`, and no others. This is the first row at which source replay, analytic `DeltaH`, and the `2 ell dT/dp` term are simultaneously visible, and they agree.
- The cubic block `-(1/16) A0^3/L^3` is unaffected at grade fifteen. Its Faber images through `w^{-6}` remain `-1/16 a1^3` in row 3, `-3/16 a0 a1^2` in row 4, `(3p/64) a1^3 - 3/16 a0^2 a1` in row 5, and `(3p/32) a0 a1^2 - 1/16 a0^3` in row 6, matching both packages; row 6 of moving `g15` prints no `ell`.

Seven rows suffice by the same degree count as the fixed-`p` review. After clearing `16 L^3`, `Num15moving` has degree at most six, equal to `deg L^3`. A proper fraction with monic denominator of degree six vanishes if and only if its first six negative `z`-Laurent coefficients vanish. The unitriangular change identifies those with the first six ordinary coordinates. The seventh row is redundant.

---

## 5. Separator

The cleared numerators, as polynomials in `z`,

```text
Num14       = 24 L A0 E0 - 12 B0 A0^2 + 5 k0 L A0^2,
Num15fixed  = 12 L^2 (A0 E1 + A1 E0)
              - 6 L (B1 A0^2 + 2 B0 A0 A1)
              + (5/2) L^2 (k1 A0^2 + 2 k0 A0 A1)
              - A0^3,
Delta       = -12 ell L A0 E0 + 12 ell B0 A0^2 - (5/2) ell k0 L A0^2,
```

satisfy, by inspection and without an engine,

```text
Num14 + 12 B0 A0^2 = L (24 A0 E0 + 5 k0 A0^2),
Delta - 12 ell B0 A0^2 = L (-12 ell A0 E0 - (5/2) ell k0 A0^2),
Delta + ell Num14 = L (12 ell A0 E0 + (5/2) ell k0 A0^2).
```

Hence

```text
Num14  == -12 B0 A0^2     (mod L),
Delta  ==  12 ell B0 A0^2 (mod L),
Delta  == -ell Num14      (mod L).
```

(The last is a congruence, not an identity in the polynomial ring: `Delta + ell Num14` is divisible by `L` and is not the zero polynomial.)

Grade fourteen says that the seven negative Laurent coefficients of `h14` vanish. The cleared numerator `Num14` has degree at most four, equal to `deg L^2`, so `L^2 | Num14`, and in particular `L | Num14`. Combined with the first congruence, `L | B0 A0^2`, hence `L | Delta`. The moving contribution is absent from every subsequent reduction modulo `L`.

Unconditionally,

```text
Num15moving = Num15fixed + Delta == -A0^3 - ell Num14   (mod L),
```

because `Num15fixed == -A0^3 (mod L)` by the already reviewed clearing of `h15fixed`. After grade fourteen, `ell Num14` vanishes modulo `L`, and

```text
Num15moving == -A0^3    (mod L).
```

Source-row vanishing implies vanishing of the first seven `z`-Laurent coefficients of `h15moving`. By the degree count of §4, `L^3` divides `Num15moving` in `k(p,k0,...,ell)[z]`. Reduction modulo `L` then gives `L | A0^3`.

On `D(p)`, `L = z^2 + p/2` is squarefree of degree two.

- If `L` is irreducible over the base, it is prime, so `L | A0`. Then `deg A0 <= 1 < 2` forces `A0 = 0`.
- If `L` splits, `L = (z-r)(z+r)` with `r^2 = -p/2 ≠ 0`, two distinct roots. Then `A0^3` vanishes at both, hence `A0` vanishes at both. A polynomial of degree at most one with two distinct roots is zero.

A candidate `A0` supported at only one root of `L` fails `L | A0^3` because the other linear factor is missing. Grade-fourteen root allocations, the tangent coefficients `A1,B0,B1,E0,E1,k1`, and the new coefficient `ell` contribute only `L`-divisible terms to `Num15moving` and cannot cancel `-A0^3` modulo `L`. Characteristic zero is used honestly: it inverts `2,3,5,16` in the binomial coefficients and in the clearing factor.

The compiled `movingSeparator` checks `Num15fixed + Delta + A0^3 + ell Num14 == 0 (mod L)`, which is this argument written as a single reduction. It is an identity of polynomials.

---

## 6. Scope

The only proposed extension is from frozen `p` to its first tangent `p + 2 sigma ell` on the already certified high-contact cone

```text
ord_sigma(R) >= 2,       ord_sigma(C) >= 4
```

on `D(p*k0)` after the reviewed half-weight receiver. The substitution is that linear jet, including the quadratic `(sigma ell)^2` forced by `L(sigma)^2`; it is not an independent second jet `p2`. Lower rays with `ord(R)=1` or `ord(C)<=3`, higher `p` jets unless formally implied by this tangent, the degenerate locus `p=0`, fan exhaustiveness, the whole square branch, order two, `(8,12)`, maximum twelve, and JC2 remain open, and so stated in V3/V4/V5 registration and in V5 `RESULT.md`.

`F_65521` is a software control. Independently reconstructed on this review: the moving substitutions, both analytic receivers, the net `Delta`, the three separator congruences, the implication `L | A0^3 => A0=0` on `D(p)` including the split case, the unitriangular binomial with the factor two, and the matching of printed exact-`Q` rows 1--3 of moving `g15` plus the cubic `A0^3` block. Reduction of those exact-`Q` rows is the image in `F_65521`: `-3/8 ≡ 24570`, `-1/16 ≡ 4095`, `-5/32 ≡ -22523`, matching the good-prime leading blocks of `g14` row 1, `g15` row 6, and the `ell` block of `g15` row 2. No binomial denominator or localization factor `2,3,5,p,k0` vanishes in `F_65521`. Same-source dual-host custody, not independent reconstruction: `sigma^{14}` divisibility of the raw `Phi_ell` and the seven-row coefficientwise remainder sentinels.

---

## Strongest surviving theorem

On the generic square open `p≠0`, after the reviewed first-normal support, the exact third-tail reduced gate `M=0`, and the reviewed half-weight ray `C=R=0` with `A` free, impose the high-contact corrections `Lambda=sigma^2`, `M=sigma^3(A0+sigma A1)`, `R=sigma^2(B0+sigma B1)`, `C=sigma^4(E0+sigma E1)` with `A_i` linear, `B_i = bs_i z + br_i/4`, `E_i = (e1_i z + e0_i)/2`, and `k10=k0+sigma k1` with `k0≠0`, and prolong the base by the first tangent `p |-> p+2*sigma*ell`. Then the complete frozen seven-row source remains divisible by `sigma^{14}`, the divided grades fourteen and fifteen remain independent of `k6,k2` and of both Taylor families and the terminal row, and they are the charged unitriangular image of `h14` and `h15moving = h15fixed + ell * partial_L(h14)`. Grade fourteen still does not kill `A0`, and it does kill the moving contribution modulo `L`. Polynomiality of `h15moving` forces `A0=0` on `D(p*k0)` in characteristic zero, independently of every displayed grade-fourteen correction, of `A1,B0,B1,E0,E1,k1`, and of `ell`.

---

## Exact scope

Generic square chart `L=z^2+p/2` with `p≠0`, after reduced `M=0` and on `D(k0)`, at the single high-contact cone `ord_sigma(R)>=2`, `ord_sigma(C)>=4` above the half-weight ray `wt(Lambda,M,S,R)=(2,3,1,0)`, through total sigma grades fourteen and fifteen of the complete frozen seven tails, with `p` prolonged by its first tangent `p+2*sigma*ell`. Exact `Q` is the characteristic-zero promotion; `F_65521` is software control. V5 is the promotable evidence package; V3 and V4 are preserved failures.

---

## Sharpest non-claim

This is not a proof that the cone exhausts the generic-square Newton/Rees fan, not a statement at `p=0` or at the square/discriminant intersection, not a routing of lower valuations of `R` or `C`, not a second or higher independent `p`-jet, not a terminal or Taylor receiver, not an exclusion of the square component, and not an order-two, `(8,12)`, maximum-twelve, or JC2 conclusion.

ORDER2_SQUARE_A_PTANGENT_CONFIRMED
