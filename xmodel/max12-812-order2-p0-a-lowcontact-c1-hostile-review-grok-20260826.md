# Hostile review: fixed-`p=0` residual `A` chart, `C` contact one

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_a_lowcontact_c1_20260826/` |
| Producer status | **PROVISIONAL**; dual AWS lanes printed `PASS_P0_A_C1` |
| Overall verdict | **CONFIRMED** |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Printed `PASS` tokens, validator strings, and the producer status line are not characteristic-zero algebra |
| Method | SHA-256 of every named pin; source reading of the raw-cusp V2 wrapper, V1 owner, and `FixedP0A` certificate; exact `Fraction` expansion of every frozen seven-tail monomial whose `sigma`-valuation is at most twelve under the contact-one substitutions; independent affine-`z` coefficient extraction of the collision receivers; reduction of the displayed `Q` units into `F_65521`. No Singular rerun, Sage, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

The displayed identities hold over `Q` as raw polynomial equalities on the stated residual `A` cone with `C` of exact contact one. Every DVR arc in either leading-`A` chart raises `C` contact beyond one. Nothing larger is proved.

---

## Verdict

**CONFIRMED.**

On the fixed collision fibre `p=0` of the complete seven-row ordinary source, after every moving-`p` jet and the leading `R,C` coordinates are set to zero, with an arbitrary first `R` correction retained, in the chart

```text
A0 = a1 z + a0,       C = sigma (e1 z + e0)/2 + O(sigma^2),
R  = sigma (cs1 z + rs1/4) + O(sigma^2),
```

the extracted source rows at absolute grades eleven and twelve satisfy

```text
g11_2 = (3/8) a0 e0,                                 (1a)
g11_1 = (3/8) (a1 e0 + a0 e1).                       (1b)

g12_2 |_{a0=e0=0} = (3/32) e1^2.                     (2)
```

On `D(a0)`, (1a) and then (1b) are unit-triangular in `e0` and `e1`. On `V(a0) intersect D(a1)`, (1b) forces `e0=0` by a single raw linear equation; after only that equation, (2) is a unit on `D(a1 e1)`. No radical, saturation, division by `p`, or modular inference is used. The three displayed polynomials are independent of `cs1, rs1` (and of every later `R` jet that the ring retains). Lower loads `k6, k2` and targets `mu2, mu4, mu6, J` are present in the emitter and are absent from grades eleven and twelve by individual-term `sigma`-valuation at this specialization.

This is only fixed-`p=0`, leading `A != 0`, finite `C` contact one, with leading `R` already routed to zero. It is not a `C`-contact-two or three statement, not an `R`-contact-zero chart, not a mixed leading-`R` sheet, not the high-contact cone except through its separate theorem, and not a verdict on order two, maximum twelve, or JC2.

---

## 0. Custody

Independently recomputed SHA-256 of the six required primary pins match the review assignment:

| Artifact | SHA-256 |
|---|---|
| `cases/max12_812_order2_p0_a_lowcontact_c1_20260826/RESULT.md` | `162a279615931f93bd15e3ea176e46c30669449cae9e35dd41305d174559fd23` |
| `cases/max12_812_order2_p0_a_lowcontact_c1_20260826/RESULTS.sha256` | `958dd6b3336d024f3b575420413ffa26b0b7811a6972a3e955c9ea2804810de1` |
| `cases/max12_812_order2_p0_a_lowcontact_c1_20260826/FREEZE.sha256` | `c0b77f7effb05ec973ce367477246d6f42ca035099553a0732392064eb4059d4` |
| `cases/max12_812_order2_p0_a_lowcontact_c1_20260826/compile_p0_a_c1.py` | `acc9e10081725594d66c27b1a9c20fa9880efb37bee6c8441dcff4d1b274e38e` |
| `xmodel/max12-812-order2-p0-a-highcontact-cech-elimination-promotion-20260826.md` | `4aeee7980586fc4c7c5456c04b84b02527251f6bd68e10f5a028cc5d19ef1f16` |
| raw-cusp V2 compiler / its `FREEZE.sha256` | `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d` / `9616ff0af8d551a6becb482d95ea1ca7d899a3b9d04df05c7f2cc04af863de7c` |

Every path named in `FREEZE.sha256` (8/8) and in `RESULTS.sha256` (35/35) rehashes to its printed digest. Transitive pins charged by the V2 compiler, the V1 owner, and the cusp grade-10/11 emitter likewise match, including

```text
tails.json          d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
canonical JSON      6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8
owner compiler      9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4
V1 compiler         feb3711636b57457069c36f79904325d901f68a3cda93742ac5dc737cc1a3c7a
V1 FREEZE           213e55fe0b59b3979edd2dfe6c2265109a5739438bef7fec6c7beefe1c6b3721
```

The two registered executions are distinct.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `max12_812_order2_p0_a_c1_20260826T115224Z_Box03_q` | `max12_812_order2_p0_a_c1_20260826T115224Z_r6d_p65521` |
| Characteristic | `0` | `65521` |
| Compiled script | `13633ff1800863f9fac80ba720eb6c1051cef8ceb504e9a4f71557ff9c537a47` | `a7c43f23cdc74737279b1c2df3b30e281d13be995d311663cea46498e5b8badb` |
| `result.json` | `fd94ab82645b05166c1172693b8ed157fd959451851f0c9b296db4da3fed8be5` | `48595c316be0548fcfdbcfa549e862e6151547f21aefa9c15da8200db92cf8cd` |
| Stdout SHA | `b56684a6e2c69af3ec266021c100bc51994e3ed26899d81267573f80463c5cb5` | `867e2c3ebc1e24ec2ee795d52c3572e0c602c62dfb2d13f0965cfe1c2225ccd4` |
| Stderr SHA | `e6486f1a1c806ef2a50057703a3ca04d52ed8324423836778519b104f3a6560a` | `d7e2b864a3e8ffd874fde27193dfe37ecc6401a864f7a2476a17e3fb82983160` |
| Engine `rc` / swap | `0` / `0` | `0` / `0` |
| Wall / max RSS | 0.29 s / 39788 KiB | 0.13 s / 29124 KiB |

The two compiled `.sing` files become byte-identical after the single substitution `ring R=0` → `ring R=65521`. Both remote freeze checks are byte-identical and report every `FREEZE` row `OK`. Meta `argv` is `Singular -q` on the lane-local compiled script. Each `result.json` `input_sha256` equals the compiled script actually run. Scope strings in both `result.json` files are `FIXED_P0_A_LEADING_C_CONTACT_ONE_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT`. No file other than this review was written.

---

## 1. Compiler substitutions: moving `p` off, leading `R,C` off, first `R` retained, `C` contact one

The wrapper `compile_p0_a_c1.py` does not emit a new tail algebra. It loads the frozen raw-cusp V2 compiler, that compiler's V1 owner, and the cusp grade-10/11 emitter; checks every `EXPECTED` digest through the owner static pins and the canonical tails digest; calls `owner.emit` on all seven rows with `Lambda = sigma^2`; appends the V1 grade-twelve extractor; applies the V2 assertion repair; and only then replaces the unique V2 endpoint

```text
print("P0_CUSP_RAW_G12_CECH_ENDPOINT=PASS_DIRECT_REGISTERED_UNIT_CERTIFICATE");
quit;
```

by a `FixedP0A` certificate. The specialization is seven polynomial substitutions performed on already-extracted rows:

```text
ell1 = ell2 = ell3 = 0,     cs = rs = 0,     c0 = c1 = 0.
```

Those are exactly: every moving-`p` jet; the leading `R` coordinates of the ordinary dictionary `R0 = cs z + rs/4`; the leading `C` coordinates of `C0 = (c1 z + c0)/2`. The first `R` correction `R1 = cs1 z + rs1/4` is a ring variable and is not substituted. With `c0 = c1 = 0` the owner's `n0, n1` jets begin at `sigma^4`, which is the insertion

```text
C = sigma (e1 z + e0)/2 + O(sigma^2)
```

together with `A0 = a1 z + a0` from `n3 = sigma^3 a1`, `n2 = sigma^3 a0`. Substitution of ring variables commutes with taking `sigma`-coefficients, so applying `FixedP0A` after extraction equals extracting on the specialized source.

The cusp-normalization block (`tau`, `d`, the four unit pivots on the `rs`-chart) still runs as a prefix. It does not alter `g11_*` or `g12_*`. The residual-`A` identities below do not consume it.

The compiled scripts contain zero matches of `/p`, `sat(`, `radical(`, or `primdec`. The two `std` calls are `std(ideal(sigma^10))` and `std(ideal(sigma))`, used only as divisibility sentinels for the extraction, not as a chart Groebner basis.

---

## 2. Complete source census; later loads and targets do not enter grades eleven/twelve

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

The compiled exact-`Q` script contains one `Phi1`..`Phi7`, the load series `(k+sigma*k1+sigma^2*k2c)` in 190 places (equals the `k10` monomial count), `(k6+sigma*k6_1)` in 72 places, `(k2+sigma*k2_1)` in 27 places, and the four target charges `-sigma^{28}*(mu2)`, `-sigma^{32}*(mu4)`, `-sigma^{36}*(mu6)`, `-sigma^{38}*(J/4)` once each. Occurrence counts in both `result.json` files are `k6=174`, `k2=282`, `mu2=mu4=mu6=J=23`.

Under the contact-one substitutions the coefficient valuations are

```text
a6 : inf (identically 0),   a5 : 3,   a4 : 3,   a3 : 5,   a2 : 5,   a1 : 6,   a0 : 6.
```

`Lambda = sigma^2` places `k10` at `sigma^4`, `k6` at `sigma^{12}`, `k2` at `sigma^{20}`. Termwise:

- every `k6` monomial has remaining `a`-weight `6+ell >= 7` and, with `a6 = 0`, remaining valuation at least 3, hence absolute order at least 15;
- every `k2` monomial has absolute order at least 20;
- every target has absolute order at least 28;
- every `k10` monomial has remaining `a`-weight `10+ell >= 11` and remaining valuation at least 9, hence absolute order at least 13.

A complete monomial-by-monomial valuation census of all 569 entries finds **no** `k10`, `k6`, `k2`, or target monomial of valuation `<= 12`. The monomials that do reach grades eleven/twelve are purely unloaded, and only on rows 1--4. Absence from `g11` and `g12` is a termwise valuation fact on the complete source, not a derivative sentinel and not a cancellation.

---

## 3. Laurent / Faber convention and coefficient extractor

The owner Taylor chart for this package is affine `z`, with

```text
A0 = a1 z + a0,     C0 = (c1 z + c0)/2,     C1 = (e1 z + e0)/2,
R0 = cs z + rs/4,   R1 = cs1 z + rs1/4,
```

and `h_ell = [z^{N-ell}]` of the grade-`N` generating function. This is **not** the `t = 1/z` pole-order indexing of the high-contact `A` theorem. It is the raw-cusp owner's affine extractor, which this client inherits. The compiled `coeffAt` is

```text
for i=0..n-1: q <- (q - subst(q,z,0))/z;  return subst(q,z,0),
```

i.e. `[z^n]`. The control polynomial `7+11 z+13 z^2+17 z^3` checks degrees 0 through 3. At `p=0` the unitriangular Faber correction `((ell-2) ell1/2) h10_{ell-2}` vanishes with `ell1`, so `g_ell = h_ell`. Grade-eleven uses `N=6`, so `g11_1 = [z^5]` and `g11_2 = [z^4]`. A reversed index would swap those two displayed rows; the source expansion of §4 does not swap them.

Independent expansion of the collision receiver at this specialization (exact `Inv=1` at `p=0`, `R0=C0=ell1=0`)

```text
D0    = z^2 A0,     D1 = z^2 A1 + C1,
Num11 = (3/4) D0 D1 z^2
```

gives

```text
[z^5] Num11 = (3/8)(a1 e0 + a0 e1),
[z^4] Num11 = (3/8) a0 e0,
[z^3] = [z^2] = [z^1] = [z^0] = 0.
```

That is (1a)--(1b) together with `g11_3 = ... = g11_7 = 0`. The same generating function at grade twelve, after `a0=e0=0`, has `[z^2]` of `(3/8) D1^2` equal to `(3/32) e1^2`, which is (2); the `D0 D2` block starts at `z^3` and `k R^3` starts at `sigma^3`.

---

## 4. Recomputed raw identities from the seven tails

Every monomial of valuation `<= 12` was multiplied in exact `Q` as a truncated `sigma`-series, with first and second `R` corrections, first `A` corrections, and second `C` corrections retained. The extracted rows are

```text
g10_* = 0                                          (leading R,C already 0)

g11_1 = (3/8) a1 e0 + (3/8) a0 e1
g11_2 = (3/8) a0 e0
g11_3 = ... = g11_7 = 0

g12_1 = (3/8) aa1 e0 + (3/8) aa0 e1 + (3/8) a1 ee0 + (3/8) a0 ee1
g12_2 = (3/32) e1^2 + (3/8) aa0 e0 + (3/8) a0 ee0
g12_3 = (3/16) e0 e1
g12_4 = (3/32) e0^2
g12_5 = g12_6 = g12_7 = 0.
```

These are identities of polynomials, not localizations. They reproduce (1a), (1b), and, after the two chart/equation substitutions `a0=0` then `e0=0`, (2). The leftover `g12_1` after those substitutions is `(3/8) aa0 e1 + (3/8) a1 ee0`; it is irrelevant once (2) is a unit.

The `R1` pieces inside the coefficient jets do appear before cancellation. For row 2 at grade eleven the two surviving monomials are `-(3/16) a2 a4^2` and `(3/4) a0 a2`. Their `sigma^{11}` parts are

```text
-(3/16)(a0)(rs1/2)^2 + (3/4) a0 (e0/2 + rs1^2/16)
 = (3/8) a0 e0 + (-3/64 + 3/64) a0 rs1^2
 = (3/8) a0 e0.
```

The `rs1^2` terms cancel. The same cancellation removes `cs1 rs1` from `g11_1` and every `R` jet from (2). Independence of the retained first `R` correction is therefore a computed identity, not an omitted variable.

---

## 5. Triangular / unit deductions over `Q`

On `D(a0)`: (1a) is `(3/8) a0 e0`. The coefficient `3/8` is a unit in `Q` and `a0` is a unit on `D(a0)`, so `e0 = 0` in the raw localized quotient. After that linear substitution, (1b) is `(3/8) a0 e1`, again a unit times `e1`, so `e1 = 0`. These are monic (up to units) linear equations. No grade-twelve row is required. The compiled certificate implements exactly the two polynomial equalities `g11_2 == (3/8) a0 e0` and `subst(g11_1, e0, 0) == (3/8) a0 e1`.

On `V(a0) intersect D(a1)`: (1a) vanishes identically. (1b) is `(3/8) a1 e0`, a unit times `e0`, so `e0 = 0`. After only that raw equation (and the chart equation `a0 = 0`), (2) is `(3/32) e1^2`. The coefficient `3/32` is a unit in `Q`. The polynomial `e1^2` is a unit on `D(e1)`, hence on `D(a1 e1)` of this chart, so that open is the empty scheme over `Q`. No radical is used: `e1^2 = 0` is not promoted to `e1 = 0` in the unlocalized quotient. The contact-raising statement for DVR arcs is the emptiness of `D(e1)` together with the observation that a DVR cannot support a nonzero nilpotent. The compiled certificate implements `subst(g11_1, a0, 0) == (3/8) a1 e0` and `subst(subst(g12_2, a0, 0), e0, 0) == (3/32) e1^2`.

Denominators that appear are `2, 4, 8, 16, 32`. All are units in `Q`. None is a hidden `p`.

---

## 6. Exact-`Q` lane versus `F_65521`

The characteristic-zero algebra is the independent expansion of §4 together with the raw triangular arithmetic of §5. The r6d lane is a software control on a second host with a second ring.

Independently: the two compiled scripts differ only by the ring characteristic. The displayed units remain nonzero in `F_65521`:

```text
3/8 ≡ 40951,     3/32 ≡ 26618     (both nonzero).
```

`65521` does not divide `2, 3, 8, 32`. The modular identities cannot collapse. They also cannot prove the `Q` identities; they were not so used. As a prefix-source sanity check, the printed V2 row `g12_6` on r6d is the reduction of the printed exact-`Q` row (`15/32768 ≡ 2`, `-3/64 ≡ -13309`, `-3/256 ≡ 13053`).

Both evidence collections hash to the frozen `RESULTS.sha256` inputs. Validators on both lanes require unique occurrence of `P0_A_C1_G11_RAW_TRIANGULAR=1`, `P0_A_C1_DA0_RAISES_C=1`, `P0_A_C1_DA1_G12_SQUARE=1`, `P0_A_C1_ARBITRARY_R_CONTACT_GE1=1`, and `P0_A_C1_ENDPOINT=PASS_FIXED_P0_C_CONTACT_ONE_RAISED`, and reject `=FAIL` and leading `?`. Resource records report zero swap and `engine_rc=0`. Those tokens are not the proof; the proof is §§3--5.

---

## 7. `R` contact at least one, and no `R` contact zero

Leading collision `R0` is set to zero by `FixedP0A`, not by an extra ideal membership. The first correction `R1` remains arbitrary. Because (1a), (1b), and (2) are independent of `cs1, rs1` (and of `cs2, rs2`), the contact-raising conclusion covers every arc with `ord_sigma(R) >= 1`. It does not cover the `R`-contact-zero charts `D(cs)` or `D(rs)`, on which `R0` is a unit. Those mixed leading-`R` sheets are a different Newton cone.

---

## 8. Quarantine of generic V12 / unbounded `d=1` / eight-form fan

The generic-square `r=1` / symbolic unique-`AC` / unbounded `d=1` (V12) package stands at `ORDER2_SQUARE_R1_D1_V12_REPAIR`. Its `d=1` compiler extracts only absolute grades 15 and 16 after a high-contact substitution that omits `k6` and `k2`. The eight-form fan likewise omits lower-load terms at larger contact. Both remain quarantined navigation.

They are not inputs to this replay. The emitter is the complete `u2_62` tails with `k6` and `k2` monomials in every row (census of §2). The `p=0` contact-one absence of those loads at grades eleven and twelve is a valuation computation on that complete source: `k6` cannot reach below grade 15 and `k2` cannot reach below grade 20. This fixed-`p=0`, grades-eleven/twelve replay is therefore independent of that defect. It must not be composed with V12 or eight-form statements.

The frozen high-contact predecessor theorem (promotion SHA-256 `4aeee798...`) treats a different cone, `ord_sigma(R) >= 2` and `ord_sigma(C) >= 4`. It is a freeze pin and a separate source theorem, not an input to identities (1)--(2).

---

## 9. Scope firewall

This certificate cannot, by itself, prove any of the following:

- `C` contact two or three;
- `R` contact zero, or the mixed sheets on which leading `R` is a unit;
- the high-contact cone, except through its separate reviewed theorem;
- that the residual `A` opens, the `C` opens, the odd unit, and the cusp unit are pullbacks of one total unspecialized-`p` Kummer/Rees family, or the exact base-change maps from that family (Gate T);
- positive-valuation moving-`p` exclusion;
- emptiness of the all-zero Pell/Chebyshev / all-load receiver;
- the boundary `k0 = 0`;
- the whole square branch, all of order two, `(8,12)`, maximum twelve, or JC2.

The producer `RESULT.md` restates this firewall. This review enforces it.

---

## Maximal theorem scope

On the collision fibre `p=0` of the complete frozen seven-row ordinary source, after every moving-`p` jet and the leading `R,C` coordinates are set to zero, with the first `R` correction retained arbitrary, ordinary dictionary `A0 = a1 z + a0`, `C = sigma (e1 z + e0)/2 + O(sigma^2)`, and with `k10, k6, k2` and every target present in the emitter, the raw source rows at absolute grade eleven equal

```text
g11_2 = (3/8) a0 e0,     g11_1 = (3/8)(a1 e0 + a0 e1)
```

and are independent of every retained `R` jet. On `D(a0)` those two rows are unit-triangular in `e0, e1`. On `V(a0) intersect D(a1)`, grade eleven forces `e0 = 0` by one raw linear equation; after only that equation the complete grade-twelve row `g12_2` equals `(3/32) e1^2`, a unit on `D(a1 e1)`. Hence every DVR arc in either leading-`A` chart of this cone has `C` of contact strictly greater than one. Exact `Q` is the characteristic-zero statement; `F_65521` is an independent good-prime control.

## Remaining low-contact / glue debt

1. The two remaining `C`-contact slices of the residual `A` fan: `ord_sigma(C) = 2` and `ord_sigma(C) = 3`, still on the complete source with leading `R` zero and first `R` free.
2. The `R`-contact-zero charts `D(cs)`, `D(rs)`, and every mixed sheet on which leading `R` is a unit at contact one.
3. The high-contact cone is a separate confirmed theorem; it still must be glued to (1)--(2) and to the `C`-contact-two/three slices as one Newton fan of `V(rs, cs)` in the residual `A` charts.
4. Gate T: one total unspecialized-`p` Kummer/Rees source algebra with identities `s = sum H_i F_i + rho H` on every chart, denominators powers of registered units only, and exact base-change maps from that family.
5. Positive-valuation moving-`p` exclusion, licensed only after Gate T.
6. The all-zero Pell/Chebyshev / all-load receiver, `k0 = 0`, both Taylor families, and terminal `[6,2]`.
7. Quarantine remains in force on generic V12 / unbounded `d=1` and the eight-form fan.
8. None of the above, and not this certificate, closes the square branch, order two, `(8,12)`, maximum twelve, or JC2.

CONFIRMED
