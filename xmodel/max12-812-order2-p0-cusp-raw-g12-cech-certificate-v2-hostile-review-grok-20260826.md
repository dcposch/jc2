# Hostile review: direct raw cusp grade-12 Čech certificate V2

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_cusp_raw_g12_cech_certificate_v2_20260826/` together with frozen V1 and the owner `p=0` cusp source |
| Producer status | **PROVISIONAL**; dual AWS lanes printed `PASS_P0_CUSP_RAW_G12_CECH_CERTIFICATE_V2` |
| Overall verdict | **CONFIRMED** |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Printed `PASS` tokens, validator strings, and the producer status line are not characteristic-zero algebra |
| Method | SHA-256 of every named pin; source reading of V2, frozen V1, and the grade-10/11 owner; exact `Fraction` truncated-series collection of all seven frozen tails in the unparameterized `p=0` jet ring; hand identity on those collected polynomials; reduction of the same `Q` polynomials into `F_65521`. No Singular rerun, Sage, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

The displayed identities hold over `Q` as raw polynomial equalities on the unparameterized post-`M=0`, fixed-`p=0` source. On `D(k0*rs)` they make the sixth grade-twelve row a registered unit. Nothing larger is proved.

---

## Verdict

**CONFIRMED.**

On the complete unparameterized post-`M=0`, fixed-`p=0` seven-row ordinary source, writing `k` for the constant term of `k10` (the producer’s `k0`), the independently collected raw sixth row at absolute `sigma`-grade twelve is the four-term polynomial

```text
g12_6 = (15/32768)*k*rs^4 - (3/64)*rs*a0*c0
         - (3/64)*cs*c0*c1 - (3/256)*rs*c1^2.          (1)
```

Together with the literal grade-ten rows

```text
g10_2 = (5/1024)*k*rs^3 + (3/8)*a0*c0 + (3/32)*c1^2,
g10_3 = (3/16)*c0*c1,                                  (2)
```

the same collection gives the ambient polynomial identity

```text
32768*g12_6 - 35*k*rs^4
  = -4096*rs*g10_2 - 8192*cs*g10_3.                    (3)
```

No coefficient of (1) or (3) is obtained by a radical, a saturation, a `cuspNorm` substitution, a grade-eleven pivot, or a localization. In the raw predecessor quotient `g10_2=g10_3=0` one therefore has

```text
g12_6 = (35/32768)*k*rs^4,
```

which is a unit on the already registered open `D(k*rs)=D(k0*rs)` in characteristic zero. This removes the cusp normalization / finite-cover debt from **this one specialized chart**. It does not prove that the chart is the base change of a total unspecialized-`p` Rees family, and it does not speak for any other Čech chart.

V2 changes only V1’s false ordinary/Faber row assertion and the four explicit multipliers that go with it. Frozen V1 is a genuine fail-closed negative control.

---

## 0. Custody

Independently recomputed SHA-256 of every hash named in the review assignment matches:

| Artifact | SHA-256 |
|---|---|
| `cases/..._v2_20260826/RESULT.md` | `bb6cea00d5665e81769b9f687cfde345569e82e4273cbb22d0c1f172af103675` |
| `cases/..._v2_20260826/RESULTS.sha256` | `e32ab337c37eebedc81d901b4c465accca087d8909fb9db62bc6dafc9695b706` |
| `cases/..._v2_20260826/FREEZE.sha256` | `9616ff0af8d551a6becb482d95ea1ca7d899a3b9d04df05c7f2cc04af863de7c` |
| V2 compiler `compile_raw_cusp_g12_cech_v2.py` | `8abeda327a7362e0cd5bdc8b73135bc59e1883664e3824783e34c9182743686d` |
| V1 compiler `compile_raw_cusp_g12_cech.py` | `feb3711636b57457069c36f79904325d901f68a3cda93742ac5dc737cc1a3c7a` |
| V1 `FREEZE.sha256` | `213e55fe0b59b3979edd2dfe6c2265109a5739438bef7fec6c7beefe1c6b3721` |
| `xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md` | `6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92` |

Every path named in V2 `RESULTS.sha256` (35/35), V2 `FREEZE.sha256` (7/7), V1 `FREEZE.sha256` (8/8), and the owner `FREEZE.sha256` (12/12) rehashes to its printed digest. Transitive pins charged by V1 and by `compile_p0_cusp_g10_g11.py` likewise match, including

```text
tails.json          d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
canonical JSON      6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8
owner compiler      9d49988213806d42ea4523881595837007fa861369f31fd18d0c83b7adf494d4
owner FREEZE        8fe97cd6972cc1f92d2380bfec4b7a7db6e6b71c1b2a348eb749f3bf71aaaa67
```

The two registered executions are distinct.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `max12_812_order2_p0_cusp_raw_g12_cech_v2_20260826T114504Z_Box03_q` | `max12_812_order2_p0_cusp_raw_g12_cech_v2_20260826T114504Z_r6d_p65521` |
| Characteristic | `0` | `65521` |
| Compiled script | `726b0feaa3bae6fa0e23b0ffdb0f2e9ca8d1e1eda0396af376034a6707eb1176` | `73bd8cc77e94e4a33adefb11829e3e88541b0add4853773ef80e08e02553fd9e` |
| `result.json` | `6531902f7be531022788d225ad5ea69fb5ae805213a99763acdb24f142df39b7` | `6f46044b395e0716d725c0aa6fc71dc397fc16f2fc92dacfb91b44ddd42d2c80` |
| Stdout SHA | `d2dc25cb9b8f0da7f713d49e2796e9d568409621e19e1f89ca8c31de1c07dc91` | `69382f5248153bb69d083dcde9c4abc72fb34bdb16f88ab089adc55fbd722494` |
| Engine | `rc=0`, `0.29 s`, `39844 KiB`, swap `0` | `rc=0`, `0.12 s`, `29144 KiB`, swap `0` |

The two compiled Singular scripts differ only in the opening ring characteristic. After that first line the bodies are byte-identical. Meta `stdout_sha256` values match the stored stdout files, which themselves match `RESULTS.sha256`. No file other than this review was written.

---

## 1. V2 delta versus frozen V1 — PASS

V2 does not emit source. It loads frozen V1, which loads the frozen grade-10/11 owner, emits the complete seven `Phi` polynomials, appends V1’s grade-twelve extractor, then applies exactly five string replacements:

| V1 assertion (false against source) | V2 assertion |
|---|---|
| `ExpectedRow6=-(3/128)*rs*c1^2-(3/32)*rs*a0*c0-(3/16)*cs*c0*c1-(5/32768)*k*rs^4` | `(15/32768)*k*rs^4-(3/64)*rs*a0*c0-(3/64)*cs*c0*c1-(3/256)*rs*c1^2` |
| `DirectCert=...+8192*rs*g10_2+32768*cs*g10_3` | `...+4096*rs*g10_2+8192*cs*g10_3` |
| `OmitNilpotentRow=...+8192*rs*g10_2` | `...+4096*rs*g10_2` |
| residue `-6144*cs*c0*c1` | residue `-1536*cs*c0*c1` |
| certificate text `-8192*rs*g10_2-32768*cs*g10_3` | `-4096*rs*g10_2-8192*cs*g10_3` |

Each old string occurs once in V1 and zero times in the compiled V2 scripts. Each new string occurs once in both compiled scripts. Reversing the five replacements restores V1’s certificate block. `Phi1`–`Phi7`, the `sigma^10` / `sigma` quotient identities, the jet ring, the load expansions, and the target subtractions are untouched.

V1 is frozen at the hashes above and is not rewritten. Its `ExpectedRow6` is internally consistent with its own multipliers and with the true rows (2): if the sixth grade-twelve row had been V1’s polynomial, V1’s `DirectCert` would have vanished. Against the actual source it does not. Independently,

```text
32768*g12_6 - 35*k*rs^4 + 8192*rs*g10_2 + 32768*cs*g10_3
  = 20*k*rs^4 + 1536*rs*a0*c0 + 4608*cs*c0*c1 + 384*rs*c1^2  ≠ 0.
```

V1 therefore fail-closes on `literalRow6=0` (and on `directCert=0`) before printing a Čech endpoint. That is a genuine negative control. In-tree V1 AWS run artifacts are absent; they are not required. The frozen compiler, compared with the collected source row, is the control.

V1’s coefficients are exactly twice the true `rs*g10_2` multiplier and four times the true `cs*g10_3` multiplier, matching a naive reading of the Laurent pole-six expression against the raw unparameterized row. V2 keeps that false compiler as the witness that the ordinary/Faber row is not that Laurent polynomial.

---

## 2. Independent unparameterized collection of `g12_6` — PASS

The owner extracts `g12_ell` as the coefficient of `sigma^12` in `Phi_ell`. `Phi_ell` is the frozen `u2_62` tail of weight `12+ell`, evaluated on the unparameterized `p=0` coefficient series

```text
p  = 2*ell1*sigma + 2*ell2*sigma^2 + 2*ell3*sigma^3,
c  = sigma^2*(cs + cs1*sigma + cs2*sigma^2),
r  = (p^2 + sigma^2*(rs + rs1*sigma + rs2*sigma^2))/4,
```

with `A`, `C` jets through second order, `Lambda=sigma^2`, loads

```text
k10 = (k + k1*sigma + k2c*sigma^2)*sigma^4,
k6  = (k6 + k6_1*sigma)*sigma^12,
k2  = (k2 + k2_1*sigma)*sigma^20,
```

and targets subtracted at `sigma^{2(12+ell)}`. This is coefficient extraction, not a Gröbner reduction: `reduce(-,Sigma1)` only sets a divisibility flag.

An independent truncated series ring over `Q`, consuming every frozen monomial of rows 1 through 7 (569 terms; every monomial satisfies `sum n_i wt_i = 12+ell` and load-linearity), yields

```text
g10_1 = (15/256)*k*cs*rs^2 + (3/8)*(a1*c0 + a0*c1),
g10_2 = (5/1024)*k*rs^3 + (3/8)*a0*c0 + (3/32)*c1^2,
g10_3 = (3/16)*c0*c1,
g10_4 = (3/32)*c0^2,
g10_5 = g10_6 = g10_7 = 0,
```

and, for the sixth row at grade twelve, **exactly four monomials** and no other:

```text
g12_6 = (15/32768)*k*rs^4 - (3/64)*rs*a0*c0
         - (3/64)*cs*c0*c1 - (3/256)*rs*c1^2.
```

In particular `g12_6` is independent of every first and second correction (`ell1,ell2,ell3,cs1,cs2,rs1,rs2,aa*,aaa*,e*,ee*,k1,k2c`) and of `k6,k6_1,k2,k2_1,mu2,mu4,mu6,J`. The Box03 stdout print of `g12_6` is this same polynomial; it was not used as an input to the collection.

Row 6 itself vanishes at grades ten and eleven (`g10_6=g11_6=0`). Grade twelve is its first nonzero raw jet. That is why a grade-eleven pivot cannot manufacture (1).

---

## 3. Literal coefficient identity (3) — PASS

From (1),

```text
32768*g12_6 - 35*k*rs^4
  = 15*k*rs^4 - 1536*rs*a0*c0 - 1536*cs*c0*c1 - 384*rs*c1^2 - 35*k*rs^4
  = -20*k*rs^4 - 1536*rs*a0*c0 - 1536*cs*c0*c1 - 384*rs*c1^2.
```

From (2),

```text
-4096*rs*g10_2 = -20*k*rs^4 - 1536*rs*a0*c0 - 384*rs*c1^2,
-8192*cs*g10_3 = -1536*cs*c0*c1.
```

The two sides are equal monomial by monomial in the ambient polynomial ring. The Python collection of `32768*g12_6-35*k*rs^4+4096*rs*g10_2+8192*cs*g10_3` is the zero polynomial. The compiled `DirectCert` test is this same equality; it does not call `reduce`.

The identity therefore holds before any quotient. In the raw predecessor ideal it specialises to `g12_6=(35/32768)*k*rs^4`. The factors `35` and `32768=2^15` are units in `Q`. On `D(k*rs)` the right-hand side is a unit.

Restricting (1) to the already confirmed cusp chart `c0=0`, `c1^2=-(5/96)*k*rs^3` recovers `(35/32768)*k*rs^4`, which is the previously confirmed Laurent unit `(18144/125)*k^5*tau^8=-(21/1024)*rs^3*u^2`. That restriction is a corollary, not a hypothesis: the certificate does not substitute the chart.

---

## 4. Nilpotent row `g10_3` is essential — PASS

Omitting `g10_3` from (3) leaves

```text
32768*g12_6 - 35*k*rs^4 + 4096*rs*g10_2
  = -8192*cs*g10_3
  = -1536*cs*c0*c1.
```

The collected polynomial equals this residue exactly, and the residue is nonzero. It is the `C`-nilpotent thickness of the raw grade-ten ideal, not a printer artifact.

Why the row is load-bearing:

1. Membership of `32768*g12_6-35*k*rs^4` in the ideal `(g10_2)` fails in the unlocalized ring. The remainder `-1536*cs*c0*c1` is a nonzero polynomial.
2. `g10_4=(3/32)*c0^2` makes `c0` nilpotent, not zero. A nilpotent remainder is still an obstruction to raw membership.
3. Killing `c0` on `D(k*rs)` uses `g10_3` itself (after `g10_2` has made `c1` a unit). Invoking `c0=0` to drop `g10_3` therefore uses `g10_3`, or else uses the cusp parametrization / finite cover that this certificate exists to avoid.

V1’s residue `-6144*cs*c0*c1` is four times this polynomial, matching V1’s fourfold `g10_3` multiplier. The sign and support were right; the coefficient was not. V2’s negative control is the correct multiple.

---

## 5. Completeness of tails, corrections, loads, targets; absence at grade twelve — PASS

Frozen tail census, every monomial weight-checked:

| Row | Monomials | `k10` | `k6` | `k2` | plain |
|---:|---:|---:|---:|---:|---:|
| 1 | 36 | 12 | 4 | 1 | 19 |
| 2 | 54 | 18 | 7 | 2 | 27 |
| 3 | 58 | 19 | 7 | 2 | 30 |
| 4 | 81 | 27 | 10 | 4 | 40 |
| 5 | 89 | 30 | 11 | 4 | 44 |
| 6 | 120 | 40 | 16 | 7 | 57 |
| 7 | 131 | 44 | 17 | 7 | 63 |

All seven rows carry `k10`, `k6`, and `k2`. The compiled ring contains the full second-correction jet

```text
ell1,ell2,ell3, cs1,cs2, rs1,rs2, aa0,aa1,aaa0,aaa1, e0,e1,ee0,ee1, k1,k2c, k6_1,k2_1
```

and those names occur inside `Phi` (not merely in the variable list). The `k10` load is expanded as `(k+sigma*k1+sigma^2*k2c)` (190 occurrences). A naive string count of `k10` is 28 and is entirely the substring `Check10_*`; it is not a source omission.

Targets are subtracted at their frozen bidegrees, once each:

```text
Phi2 -= sigma^28 * mu2,   Phi4 -= sigma^32 * mu4,
Phi6 -= sigma^36 * mu6,   Phi7 -= sigma^38 * (J/4).
```

Compiler census on both compiled scripts: 174 `k6`, 282 `k2`, 23 each of `mu2,mu4,mu6,J`, matching `result.json` and `RESULT.md`.

Absence at grade twelve is a valuation statement on that complete source, not a truncated emitter:

- `k2` carries `sigma^20`, hence is invisible at grade twelve;
- `k6` carries `sigma^12` times a nonempty weight-`6+ell` product of coefficient series, each of which has `sigma`-valuation at least 1, hence total valuation at least 13;
- targets sit at `sigma^{24+2ell} >= sigma^{26}`.

Independent collection of all seven `g12_ell` confirms that none contains `k6,k6_1,k2,k2_1,mu2,mu4,mu6,J`. The compiled `diff` tests are this same absence, not a substitute for it.

---

## 6. Exact `Q` independently of `F_65521` — PASS

The identities of §§2–4 were obtained over `Q` by truncated series, with no modular reduction and no use of the r6d stdout. `65521` is prime and does not divide any denominator in (1)–(3) (those denominators are powers of two). Reducing the collected `Q` polynomials into `F_65521` gives

```text
g12_6 ≡ 2*k*rs^4 - 13309*rs*a0*c0 - 13309*cs*c0*c1 + 13053*rs*c1^2,
```

which is exactly the r6d print (`-3/64 ≡ 52212 ≡ -13309`, `-3/256 ≡ 13053`, `15/32768 ≡ 2`). The same reduction of identity (3) is the zero polynomial in `F_65521`. The control lane is therefore the reduction of the characteristic-zero identity, not an independent modular accident, and the characteristic-zero statement does not depend on it.

---

## 7. Logical consequence on `D(k0*rs)` — PASS, and no more

Design §4 asked for an explicit raw membership certificate for `32768*row(6,12)-35*k0*rs^4` in the complete predecessor ideal, precisely so that the cusp unit would not need a separate normalization-surjectivity argument. Identity (3) is that certificate. On `D(k0*rs)` the specialized chart now has a registered-unit sixth row from the raw source, before cusp parametrization.

What this does **not** establish, and what design §§1, 3, 5 already forbid reading into it:

- that this specialized `p=0` extractor is the base change of the total blowup `Proj(Rees_A(J1))` formed over the unspecialized Kummer base `p=-2*rho^2` **before** setting `rho=0`;
- emptiness or identification of any other standard chart (`D_+(cs)`, `D_+(c0)`, `D_+(c1)`, `D_+(a0)`, `D_+(a1)`);
- a bidirectional raw-row equality between this client and a total Rees chart.

Blowing up the already specialized ring `A/(p)` is not a substitute for that base change. The raw grade-ten nilpotent `C` thickness is exactly the torsion the design warns about.

---

## 8. Scope firewall

This certificate cannot, by itself, prove any of the following:

- exclusion of positive-valuation moving `p`;
- emptiness of the all-zero higher-contact / exact-square receiver `V(rs,cs,c0,c1,a0,a1)`;
- the boundary `k0=0`;
- any square-branch statement, including generic-square `D(p)` charts and the `r=1` / V12 packages;
- order two, `(8,12)`, maximum twelve, or JC2;
- the odd unit, the two `C` opens, or the two residual `A` opens, except as already confirmed on their own specialized clients.

`RESULT.md` already states this firewall. The compiled `scope` string is `POST_M0_FIXED_P0_D_K0_RS_RAW_CUSP_CHART_ONLY_NO_TOTAL_REES_OR_ORDER2_VERDICT`. This review enforces it.

---

## Maximal source theorem

On the collision fibre `p=0` of the complete frozen seven-row ordinary source, in the unparameterized post-`M=0` jet ring with every second correction, every `k10,k6,k2` monomial, and every target retained in the emitter, the coefficient of `sigma^12` in the sixth Faber row is the polynomial (1). The ambient identity (3) holds with the literal raw grade-ten rows (2), with no normalization, radical, saturation, or grade-eleven pivot. In the raw predecessor quotient, `g12_6` is therefore the unit `(35/32768)*k0*rs^4` on the registered open `D(k0*rs)`. Omitting the nilpotent row `g10_3` leaves the exact nonzero residue `-1536*cs*c0*c1`. Frozen V1, which asserted the wrong ordinary/Faber row and the wrong multipliers, fail-closes against this source and is preserved. Exact `Q` is the characteristic-zero statement; `F_65521` is an independent good-prime control.

## Remaining glue debt

1. One finite raw algebra over `Q[rho]` with `rho` not inverted, all corrections, `k10,k6,k2`, and all targets at their true bidegrees (design §5 item 1).
2. The actual Rees presentations of `J1=(rs,cs,c0,c1)` and of `J2=(a0,a1)` on `V(J1)`, formed **before** setting `rho=0` (design §§1, 5 item 2). Specializing first and then blowing up is not a substitute.
3. On each standard total chart, bidirectional maps or raw-row ideal equalities from that base-changed chart to the frozen odd, cusp, trivial-`C`, and `A` clients (design §5 item 3). The present identity identifies the specialized cusp endpoint with a registered unit; it does not print those maps.
4. Localized identities `s=sum h_i f_i + rho*h` on the other five ordered charts, with `s` made only from each chart’s registered units (design §5 item 4).
5. Preservation of `V(J1+J2)` as the exact-square / all-load successor, with the two `A` charts as a negative control (design §5 item 5).
6. On `D(rho)`, the deck-equivariant transform to both generic-square root charts (design §5 item 6). That overlap is separate from special-fibre coverage.
7. The boundary `k0=0`, positive-valuation moving `p`, both Taylor families, terminal `[6,2]`, the square branch, order two, maximum twelve, and JC2 remain out of scope.

CONFIRMED
