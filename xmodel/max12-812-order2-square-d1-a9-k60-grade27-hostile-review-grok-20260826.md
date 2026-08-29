# Hostile review — D1 `a=9`, `D(k60)` grade-27 exact-contact obstruction

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_v2_target_precedence_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing variable | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and prior reviews are not authority |
| Method | source reading, SHA-256 of every named pin and evidence file, compiled-script inspection, frozen Faber-tail monomials, and hand identities; no Singular re-execution, Sage, msolve, Lean, or package compiler |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the three required primary pins match. Every path named in `FREEZE.sha256` (7 rows) and `EVIDENCE.sha256` (43 rows) rehashes to the printed digest. Nested `compiled.sha256` rows on both lanes rehash to the retrieved V2 scripts and `result.json`. Frozen V1 compiler/registration/freeze pins inside `compile_v2_target_precedence.py` rehash, as do the V1 freeze rows, the parenthesized-load V3 census pins, the recursive V2 compiler, and `tails.json`. Exact Q is the theorem endpoint; `F_65521` is a separate compiled input and a separate engine transcript. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

V1 is immutable and fail-closed: both AWS engines extracted the complete source, printed every grade-27 / moving-connection / delayed-load identity, then died on `sigma^38/4` parsed as exponentiation by the rational `38/4`. The target boolean was undefined and the validator refused the unique marker `D1A9_K60_ALL_TARGETS_RETAINED=1`. V2 replaces exactly one generated token sequence

```text
diff(A9V2_Q0_7,J)+sigma^38/4==0
diff(A9V2_Q0_7,J)+(sigma^38)/4==0
```

and its exact-Q input is byte-identical to frozen V1 after that replacement. The repaired check is the literal derivative of the frozen insertion `-sigma^38*(J/4)` and cannot move grade 27.

On the registered fixed-contact D1 chart

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9
```

with `p*k0*k60` inverted, the complete seven-row literal-Faber source is exactly divisible by `sigma^27`, has no earlier nonzero row, and its grade-27 block is

```text
g27 = ( (3/4) c1 k60,
        (3/4) c0 k60,
       -(3/16) p c1 k60,
        0,
       -(3/128) p^2 c1 k60,
        0,
       -(3/512) p^3 c1 k60 ).
```

The first two identities are the independent leading coefficients of the linear polynomial `C0=c1 z+c0`. In any `Q`-algebra, and in any characteristic-zero domain after clearing the 2-power denominator, `k60` a unit forces `c1=c0=0`, contradicting exact order `10`. The same vanishing is the unit ideal after adjoining `p^{-1},k0^{-1},k60^{-1}` and Bezout coordinates for `(c1,c0)\neq(0,0)`. No radical is taken, and `A^2\setminus\{0\}` is covered by a single Bezout chart. Over a ramified DVR of characteristic zero the elementary unit argument applies directly to the two scalar identities and does not pass through that Groebner model.

`V(k60)`, raised contact, every other D1 cell, the square component, order two, `(8,12)`, maximum twelve, and JC2 remain open.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Three primary pins | hashes | all three match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 7/7, `EVIDENCE` 43/43, both nested `compiled.sha256` 4/4 |
| 0. V1/V3 immutability | V1 compiler, freeze, registration; V3 census pins | all V2-pinned hashes match; V1 freeze 9/9; V3 compiler/registration/result/freeze/evidence rehash |
| 1. Registered cell | `ord(A)=9`, `ord(C)=10`, `ord(R)>=9` on `D(p*k0*k60)` | **holds**; see §1 |
| 2. No row before grade 27; identities `g1=(3/4)c1 k60`, `g2=(3/4)c0 k60` | frozen tails plus D1 substitutions | **holds**, including the five determined companions; see §2 |
| 3. `k60\neq 0` forces `C0=0`, including ramified DVRs, no radical, no omitted chart | unit argument; Bezout only over fields | **holds**; see §3 |
| 4. Moving connection, timed `k6/k2/k10`, `mu2/mu4/mu6/J` | binomial orders and retained targets | **holds**; nothing omitted can hit grade 27; see §4 |
| 5. V1 fractional-exponent failure; V2 one-token syntax | byte reconstruction; V1 diagnostics | **holds**; see §5 |
| 6. Exact Q vs `F_65521` | separate hosts, scripts, transcripts | **holds**; `16381 ≡ 3/4 (mod 65521)` |
| 7. Firewall | `V(k60)`, higher contacts, all D1, order two, max twelve, JC2 | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the three required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `3679d0dbd883c74a4d1d7d1175daf9461c123dd83272bdf2e713ebd7c3412a88` | producer report |
| `.../EVIDENCE.sha256` | `f878c18a4163e1b94bb150e3a84e626ff3eb9d13382da8d03694b200101c2a0d` | evidence freeze |
| `.../FREEZE.sha256` | `be2a611f119900400b7bb5a8c0fc7e9cb66815c8b3c23a70feb565b209092c48` | source freeze |

`FREEZE.sha256` names seven files, all matching:

| Path | SHA-256 |
|---|---|
| V2 `REGISTRATION.md` | `748c10651c1bc6072b118478dd12937c686ff2777a507a8414d394f721525727` |
| V2 `compile_v2_target_precedence.py` | `be60b80e2381d2c788fba6cb0517dd8be7d3b1febc9cbd066703d6f7c20857b1` |
| V2 `run_aws.sh` | `9b41ee2ca81c75e37edd4a7d614afc6522f4a1dc9a09b758561368434ba75461` |
| V2 `launch_host.sh` | `a2f763d5397edd5bc251dbd6da544f3f44f56b74cc337d503b6137cf36a5af5f` |
| V1 `compile_a9_k60_unit.py` | `abb88d2a343d0cde75cdc8c2818ccc541c9961b6eca71f3ef0cbf8e114698f74` |
| V1 `FREEZE.sha256` | `d84fef5925858f105332591df7a2027ae4f70c764517a1c1b167a60c2204d968` |
| V1 `REGISTRATION.md` | `4b5847eba158ab3965aa762de8662956537e9ee51ddd696d1b888cebec05158f` |

`EVIDENCE.sha256` names 43 files; all 43 rehash. Both nested `compiled.sha256` files rehash to the retrieved V2 `.sing`, `result.json`, `parent_v1_result.json`, and `parent_v3_result.json`.

V1 freeze 9/9 rehashes, including the parenthesized-load V3 census:

| Pin | SHA-256 |
|---|---|
| V3 `compile_v3_parenthesized_loads.py` | `0f7b9482f214347858f61181119f52fc434de8223ae7a3c4099049bd737897ef` |
| V3 `REGISTRATION.md` | `a88cc145baaa6612b73e0d44df0e012fcc99d531d50bbe8879a081449eb51b3b` |
| V3 `RESULT.md` | `88609fdfc50b89625f79e7dcee3b8ceb47d61c3b6668e86ee80da67ad4129e24` |
| V3 `FREEZE.sha256` | `7016cdba48152e5e44b285a56812f2b2e077f110cc6e5baa5adbbe9d184d2432` |
| V3 `EVIDENCE.sha256` | `d2e5d59f94d3489fd8bd3509fd0ece0dc2456c234173f5023ebad2f201bb3c06` |
| recursive V2 `compile_a9_recursive.py` | `8a36f5edee279964f547a5ce0d2bbe0511e9cfaf6c5261cce6d115f4b3fcf46f` |
| `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical all-tails | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |

Every load monomial in the seven frozen tail rows is counted by the V3 distributivity sentinel: `k10` 190, `k6` 72, `k2` 27. The compiled exact-Q script contains those parenthesized jets with full Faber weights at exactly those cardinalities, and contains no unparenthesized `*k60+sigma^1*...` remnant.

Exact Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_v2_q_20260826_box03` | `…_v2_p65521_20260826_r6d` |
| PID | `229360` | `286619` |
| Characteristic | `0` in both rings | `65521` in both rings |
| V2 compiled script SHA | `b4db6502507c368827b6a40ad866a7792f026fb98d0a4b79f645ebc08b2a1cba` | `d85c5871137b579901989ca9586115b49ec1e1634818beb4855d3504fa53088c` |
| Parent V1 script SHA | `56c3bbe858814761a5f61af18a5e1e6a2e70424153ef538c769bb794bb9b49fa` | distinct char-65521 V1 parent |
| Parent V3 script SHA | `77a0b2db497f1d2276392c1b2f862b3c05aa027c677fb66778cced1c3fad8d9f` | distinct char-65521 V3 parent |
| Engine `rc` | `0` | `0` |
| Stdout SHA | `00066ec7a17918e4fdedd2212f358ff55a13e19b0f29ec4d0ce416e94a462b12` | `ccc17f85fbbc5c437de4fc50a67f160c0911787306b068d0b50194632c960f21` |
| Peak RSS / swaps | 1,255,352 KiB / 0 | 889,144 KiB / 0 |
| Wall | 5.78 s | 3.89 s |
| VM cap | 16,777,216 KiB | 16,777,216 KiB |

The two V2 compiled scripts differ by exactly the two ring-characteristic tokens (`ring R=…` and `ring D1A9K60=…`). Substitutions, maps, recurrences, and sentinels are otherwise identical. Compiler stderr is the empty-file digest `e3b0c442…` on both lanes. Neither V2 stdout nor stderr contains `?`, `error occurred`, or `=FAIL`. Caps were 16 GiB virtual, 600 s compile, 1800 s engine. The validator string is not a mathematical verdict. The algebra below is independent of those sentinels.

The two transcripts are not copies: exact Q prints `3/4*c1*k60`, while `F_65521` prints `16381*c1*k60`, and `3·4^{-1} ≡ 16381 (mod 65521)`. After deleting polynomial bodies, the remaining 224 row-status markers and the D1 endpoint flags agree.

A passing manifest is not a theorem. What follows is the source.

---

## 1. Registered exact-contact cell

The recursive emitter, inherited unchanged through V3 parentheses and the V1/V2 k60-unit wrappers, substitutes

```text
az = sigma^9 (a1 + sigma a1_1 + … + sigma^4 a1_4)
ac = sigma^9 (a0 + …)
cz = sigma^10 (c1 + … + sigma^4 c1_4)
cc = sigma^10 (c0 + …)
rz = sigma^9 (b1 + sigma b1_1 + sigma^2 b1_2)
rc = sigma^9 (b0 + …)
```

into the frozen D1 coefficient map `K=L^2+sigma^2 R`, `D=LA+C` of `compile_r1_d1_ac.py`. That is exact order 9 in `A`, exact order 10 in `C`, and order at least 9 in `R`. The compact obstruction ring inverts `p`, `k0`, and `k60`. The symbol `k0` is the constant term of the weight-2 jet `k10`; `k60` is the constant term of the weight-6 jet `k6`. Compiler JSON still labels the scope `D_P_K10_K6`; that is leftover naming from the `a=8` parent and is not a different cell.

Exact `ord(A)=9` is a chart hypothesis, not a generator of the localized ideal. The grade-27 identities do not mention `a1,a0`. Points with `a1=a0=0` are simply outside the registered cell; they would still be killed by the same `C`-obstruction if they kept exact `ord(C)=10`.

---

## 2. Grade 27, and nothing earlier

Frozen Faber tails are load-linear of weight `12+row`. The `k6` monomials that can see `C` are those containing `a1` or `a0`, because `C` enters the D1 substitution only through

```text
n1 = sigma^3 ((p az)/2 + cz),   n0 = sigma^3 ((p ac)/2 + cc),
coeff[1] = 2 kc kr + Lambda n1, coeff[0] = kr^2 + Lambda n0.
```

The `C`-summand of `Lambda n1` is `sigma^{15} c1`; times `k60 Lambda^6 = k60 sigma^{12}` this is grade 27. The unique row-1 `k6` monomial with `a1` is `(3/4) a1 k6`, giving

```text
g27_1 = (3/4) c1 k60.
```

The unique row-2 `k6` monomial with `a0` is `(3/4) a0 k6`, giving

```text
g27_2 = (3/4) c0 k60.
```

The remaining five rows at this order are determined by the same `C`-summand against the val-0 square coefficients `a6_0=2p`, `a4_0=(3/2)p^2`, `a2_0=p^3/2`:

```text
row 3:  (-3/32) a1 a6 k6  →  -(3/16) p c1 k60
row 4:  no val-0 a0/a1·k6 monomial              →  0
row 5:  (15/512) a1 a6^2 k6 + (-3/32) a1 a4 k6
        → (15/128 - 9/64) p^2 c1 k60 = -(3/128) p^2 c1 k60
row 6:  no val-0 a0/a1·k6 monomial              →  0
row 7:  (-33/4096) a1 a6^3 + (9/256) a1 a4 a6 + (-3/32) a1 a2
        → (-33/512 + 27/256 - 3/64) p^3 c1 k60 = -(3/512) p^3 c1 k60.
```

These are the complete literal-Faber grade-27 identities. The two leading rows are exactly the claimed pair; they are the only independent coefficients of `C0`.

Nothing precedes grade 27, by the same substitutions. The structurally dangerous cancellations, all identities in `p,b1,a1,k60` with no computer algebra, are:

- Pure square × `k6` at grade 12 in row 2: five val-0 monomials sum to
  `(-45 + 90 - 27 - 24 + 6)/128 p^4 k60 = 0`.
- `R×k6` at grade 23 in row 1: four monomials sum to
  `(15 - 9 - 12 + 6)/16 p^2 b1 k60 = 0`.
- `A×k6` at grade 26 in row 1:
  `(-3/8) p a1 k60 + (3/8) p a1 k60 = 0`.
- `C×k10` at grade 19 in row 1:
  `(-15/32 + 15/32) p^2 c1 k0 = 0`.

`k2×C` is grade `15+20=35`, after the window. The recursive client then divides by `sigma` from grade 0 through 31 and checks `sigma·Q_{n+1}=Q_n-g_n` as polynomial identities; that is exact divisibility, not series truncation. There are 224 row-status markers (`7×32`). Zero of them are nonzero below grade 27. Nonzero counts by grade are 5, 5, 5, 6, 6 on grades 27–31, total 27. Row 6 remains zero through grade 31.

The exact-Q printed bodies are the identities above, not merely a `=1` flag. `F_65521` prints the same polynomials reduced into `{0,…,65520}`.

---

## 3. `k60 ≠ 0` forces both coefficients of `C0` to zero

On `D(k60)` the first two rows are `(3/4) k60 c1 = (3/4) k60 c0 = 0`. In any commutative `Q`-algebra in which `k60` is a unit, `3/4` is a unit, hence `c1=c0=0`. Exact contact requires the leading coefficient of

```text
C = sigma^{10} ((c1 z + c0) + O(sigma))
```

to be a nonzero polynomial in `z`, i.e. `(c1,c0)≠(0,0)`. Contradiction.

Clearing the denominator: `4 g27_1 = 3 c1 k60`. In any characteristic-zero integral domain, vanishing of `g27_1` with `k60` a unit still forces `c1=0` (and likewise `c0`). This includes ramified DVRs of characteristic zero. Residue characteristic 2 or 3 is outside the exact-Q theorem; the D1 encoding already inverts 2 in `L=z^2+p/2`.

No radical is used. An explicit membership certificate in the polynomial ring `Q[z,p,k0,k60,c1,c0,ip,ik0,ik60,u1,u0]` for the localized ideal

```text
I = ( (3/4)c1 k60, (3/4)c0 k60, ip p-1, ik0 k0-1, ik60 k60-1, u1 c1+u0 c0-1 )
```

is the pair of ring identities

```text
c1 = (4/3) ik60 · h1 - c1 (ik60 k60 - 1),
c0 = (4/3) ik60 · h2 - c0 (ik60 k60 - 1),
1  = (u1 c1 + u0 c0) - (u1 c1 + u0 c0 - 1).
```

The Groebner test `reduce(1,I)==0` over `Q` is software confirmation of this certificate, not the proof.

Bezout `u1 c1+u0 c0=1` is equivalent to `(c1,c0)≠(0,0)` over a field, and covers `A^2\setminus\{0\}` with one affine chart. It is not a projective space and omits no field-valued point of exact contact. Over a DVR it is strictly smaller than `(c1,c0)≠(0,0)` in `R^2` (non-unimodular pairs with both coefficients in the maximal ideal). Those pairs are still killed by the unit argument: source vanishing forces `c1=c0=0` as equalities in `R`, not merely in the residue field. The theorem over ramified DVRs therefore uses the first paragraph of this section, not the Groebner/Bezout packaging.

Inverting `p` and `k0` is chart localization. Neither appears in `g27_1` or `g27_2`. On `D(p)` the companions `g27_3,g27_5,g27_7` are nonzero multiples of `g27_1`; they are not needed to force `C0=0`.

---

## 4. Custody of moving connection, timed loads, and targets

Binomial orders from the same substitutions:

| Term | First grade | Why |
|---|---|---|
| `k60 C` | 27 | `Lambda n1` of `C` is `sigma^{15}`; `Lambda^6` adds 12 |
| `ell1 c1 k60` moving connection | 28 | one `sigma` from `p+2 sigma ell1` |
| `k60_1`, `c1_1` | 28 | next jets of the same product |
| `mu20` | 28 | frozen insertion `-sigma^{2(12+2)} mu20` in row 2 |
| `A C` | 29 | wrappers `sigma^{14}` and `sigma^{15}` |
| `C R k10` | 30 | `kc` is `sigma^{11}`; `Lambda^2` adds 4; `C` adds 15 |
| `k20`, `k0_1`, `k60_4` | 31 | printed row-1 body contains `1/2 b1 k20`, `5/8 (c0 b1+c1 b0) k0_1`, `3/4 c1 k60_4` |
| `mu4` | 32 | `-sigma^{32} mu4` |
| `mu6` | 36 | `-sigma^{36} mu6` |
| `J/4` | 38 | `-sigma^{38} (J/4)` |

Each of `mu2,mu4,mu6,J` occurs once, as the literal fragments the V1 wrapper demanded. The delayed-load checks are the three partial derivatives of the displayed grade-31 row 1. The moving-connection check is the displayed grade-28 row 3

```text
-(3/8) ell1 c1 k60 - (3/16) p c1_1 k60 - (3/16) p c1 k60_1.
```

Jet lengths cover the window: `c1..c1_4` and `k60..k60_4` reach grade 31; `k0..k0_2` first appear at 30; `b1..b1_2` first appear at 30; `a1..a1_4` first appear at 29; `mu20..mu20_3` cover 28–31. No omitted higher jet, and no omitted `mu4/mu6/J`, can contribute to grade 27.

The parenthesized complete jets times full Faber weights are the V3 repair of the quarantined unparenthesized V2 census. That census is negative custody only and is not a mathematical input.

The Chebyshev/Pell identity `A^2 - Q P^2 = 1` for `Q=z^4-1`, `P=16Q^2+20Q+5`, `A=16z^{10}-20z^6+5z^2` holds by the elementary expansion in `v=z^4`: `P=16v^2-12v+1` and `v(16v^2-20v+5)^2-(v-1)P^2=1`. The client therefore does not encode a blanket square-forcing assertion.

---

## 5. V1 is a no-verdict negative control; V2 repairs only target precedence

Frozen V1 writes `diff(A9V2_Q0_7,J)+sigma^38/4==0`. Singular parses `sigma^38/4` as `sigma^(38/4)`. Both V1 engines printed, after a complete source extraction identical to V2 through the census endpoint,

```text
D1A9_K60_GRADE27_IDENTITIES=1
D1A9_K60_MOVING_CONNECTION_AND_K6JET=1
D1A9_K60_DELAYED_K2_K10_K6=1
D1A9_K60_PARENT_COUNTS=1
D1A9_K60_ALL_TARGETS_RETAINED=
```

together with the diagnostic `` `poly` ^ `number` failed `` / `` expected `poly` ^ `int` `` at the targets line, then a cascade of undefined identifiers. The V1 validator refused the unique required marker `D1A9_K60_ALL_TARGETS_RETAINED=1`. V1 exact-Q stdout through the census endpoint (first 664 lines) is byte-identical to V2 exact-Q stdout through that same endpoint. No obstruction endpoint is licensed from V1.

V2 changes only that token. Exact-Q V2 source `=` V1 source with one `replace` of `sigma^38/4` by `(sigma^38)/4`. Cardinality is `(old,new)=(1,0)` before and `(0,1)` after. The repaired predicate is `diff(Q0_7,J)+(sigma^{38})/4==0`, which is the derivative of the unique frozen insertion `-sigma^{38}(J/4)`. That insertion sits at grade 38 and cannot alter grade 27.

---

## Narrowest theorem

There is no point of the fixed-contact D1 chart

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9
```

on `D(p*k0*k60)`, in characteristic zero, at which the seven literal-Faber source rows vanish. Equivalently: the grade-27 identities `(3/4)c1 k60=(3/4)c0 k60=0` with `k60` a unit force the leading coefficient of `C` to vanish, contradicting exact order 10.

The statement is for this chart only. It is scheme-theoretic over `Q` (the two equations generate the unit ideal on the Bezout cover of exact contact) and holds for characteristic-zero DVR-valued points by the unit argument.

---

## Firewall

`V(k60)` is untouched. Its first new terms are the grade-28/29 collision of `k60_1`, `mu20`, the moving connection, and `A C`; that branch must keep delayed `k20/k0_1` and the terminal targets. Raised or dropped contact, `p=0`, `k0=0`, every other D1 valuation cell, the rest of the square component, order two, `(8,12)`, maximum twelve, and JC2 remain open. The tied-load Chebyshev/Pell survivor is not contradicted.

CONFIRMED
