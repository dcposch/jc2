# Hostile review — D1 `a=6,7` complete `k6` transition V2

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_v2_t2_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, V1/V12 names, and prior reviews are not authority |
| Method | source reading, SHA-256 of every named pin and evidence file, compiled-script inspection, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the three required primary pins match. Every path named in `FREEZE.sha256` (4 rows) and `EVIDENCE.sha256` (32 rows) rehashes to the printed digest. Nested `compiled.sha256` rows on both lanes rehash to the retrieved V2 scripts and `result.json`. The three frozen V1 pins inside `compile_v2_t2.py` / `REGISTRATION.md` rehash, as do the V1 freeze rows, the V1 exact-Q / `F_65521` compiled inputs retrieved as `compiled_frozen_v1/`, the V12-era base compiler pins, `tails.json`, and the canonical all-tails digest. The `/tmp` source archive recorded in `RESULT.md` was not retrieved; the repository freeze and the 32 evidence files are the custody. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

V1 is immutable and fail-closed: both AWS engines returned `rc=0`, the validator rejected the unique marker `A6_ROW_IDENTITIES_24=1`, and the exact-Q remainders isolate a generating-series alignment error. With `H=tF` and `z=1/t`, the function `C_{\mathrm{poly}}/L` is `t C_t \mathrm{Inv}_1`, so the representative of `(3/4)k6 C/L` is `t^2 C \mathrm{Inv}_1`, not `t C \mathrm{Inv}_1`. V2 changes exactly those two generated tokens and nothing else.

On `D(p*k10)`, after the reviewed first-normal / half-weight / `M=0` hypotheses, the complete seven-row source at the fixed contacts

```text
ord(A)=a,  ord(C)=a+1,  ord(R)>=a,  a in {6,7}
```

agrees with the moving `T0+T1` image of the Laurent receiver whose only in-window polar forms are

```text
a=6, grades 23,24:  U0 ; U1 + KRC + S0
a=7, grades 25,26:  U0 + S0 ; U1 + KRC + S1
```

with

```text
U0  = [(3/4) A0 C0 / L]_-
U1  = [(3/4)((A1 C0 + A0 C1)/L - ell1 A0 C0 / L^2) + (3/8) C0^2 / L^2]_-
KRC = [(5/8) k10 R0 C0 / L]_-
S0  = [(3/4) k60 C0 / L]_-
S1  = [(3/4)((k61 C0 + k60 C1)/L - ell1 k60 C0 / L^2)]_-.
```

No `k2`, target, extra `k6`, unloaded `A^3`, or `k10 R^3` / `k10 A^2` term enters these two-grade windows. After the opposite-root allocations of nonzero linear `A0,C0` on squarefree `L=z^2+p/2` (shifted by `A0+k60` at `a=7`), the first `L`-numerator vanishes identically and the next `L^2`-numerator evaluates at the allocated `A`-root to `(3/2) lambda^2 cv^2`, nonzero on `D(p)` with nonzero leading `C`. The `a=7` locus `A0+k60 \equiv 0` is inside the contact when `k60 \neq 0` and is killed by the same double pole: the numerator is `(3/8)C0^2 + L C0 \cdot(\mathrm{deg}\le 1)` and cannot vanish for `C0 \neq 0`. No finite-order normalized arc exists in either listed contact. The statement is arcwise / set-theoretic, not scheme-theoretic, and it does not close `a\ge 8`, positive-order `k10`, `p=0`/`k10=0`, the square branch, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Three primary pins | hashes | all three match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 4/4, `EVIDENCE` 32/32, both nested `compiled.sha256` 2/2 |
| 0. V1 immutability | V1 compiler, freeze, negative-control note, compiled V1 inputs | all three V2-pinned V1 hashes match; V2 `compiled_frozen_v1` byte-identical to the V1 case outputs; V1 freeze 4/4 |
| 1. V1 fail-closed alignment | exact remainder; `t^2` not `t`; two-token V2 | **holds**; see §1 |
| 2. Seven-tail reconstruction | frozen Faber, three loads, four targets; outer `sigma` in `source_coefficients` | **holds** |
| 3. Complete support | grades 23/24 and 25/26; only new lower-load terms `S0,S1` | **holds** by binomial orders |
| 4. `SOURCE_SUPPORT_FILTER` | allowed variables exact; `diff` cannot hide a forbidden dependence | **holds** as an upper bound; completeness is the expansion plus row bridge |
| 5. `T0+T1`, analytic coefficients, both recurrences | do not trust V12 names | **holds** independently |
| 6. Three negative controls | deletion of a generically nonzero module | **holds**; KRC is analytic-side but is the unique in-window `eta` term and is carried by the row bridge |
| 7. `a=6` allocation | exhaustive; `S0`/`KRC` simple after `L^2`; residue `(3/2)lambda^2 cv^2` | **holds** |
| 8. `a=7` factor `C0(A0+k60)` | both shifted maps; moving-`L` cancel at `A0=-k60`; same `C^2` residue | **holds**, including the `A0+k60\equiv 0` face by degree |
| 9. `eta` truncation | exact `ord(R)=a`; `eta=0` complete through the next grade | **holds**; not an unbounded substitution |
| 10. Inversions, exact-Q vs `F_65521`, AWS custody, arcwise scope | every contact used | **holds** |
| 11. Firewall | no `a\ge 8`, no positive-order `k10`, no `p=0`/`k10=0`, no fan/order-two; Pell/Chebyshev not contradicted | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the three required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `f3c987b630a2895defabcc1043768497f2e8caad538f58122bb4e17b317c0a9c` | producer report |
| `.../FREEZE.sha256` | `b2a38e4f5c38166789c5d73ecae989c30ed8168c5fc6a58fc3058eb5535e1ad5` | source freeze |
| `.../EVIDENCE.sha256` | `eb0058746a406c9d36c11d00c97884e7e937f93cf693763401aa957c432990ee` | evidence freeze |

`FREEZE.sha256` names four files, all matching:

| Path | SHA-256 |
|---|---|
| `REGISTRATION.md` | `d9053b80997efd1e5ed6f5072a76a75ae1e8db587dc59b464473260d4c2dcf19` |
| `compile_v2_t2.py` | `03a766427b4e80f60590ab13cdbd2cbed56eb6b0d90b5269ad764c0ed9237d98` |
| `run_aws.sh` | `e7dd9fde7f45ab0e104d3f814457fb7e57529e7cdaa995e9b0b15c0ede6ba6b5` |
| `launch_host.sh` | `612598704d6a19ce79dfea73f5176dedfd84be870ced35f1653a038d1ea8487a` |

`EVIDENCE.sha256` names 32 files; all 32 rehash. Both nested `compiled.sha256` files rehash to the retrieved V2 `.sing` and `result.json`.

Frozen V1 pins inside the V2 compiler:

| Path | SHA-256 |
|---|---|
| V1 `compile_load_transition.py` | `158ebf84bf8c13143d606b0ffbd2cd4c56e0a6033f1a57d11d61ae30ce220a4e` |
| V1 `FREEZE.sha256` | `71e076ff360c8bd7d0ca00feee153d7e1794619b980391aa49a473c098bcb721` |
| V1 `RESULT_NEGATIVE_CONTROL.md` | `df29e2d45d880d734dafbd2a26004d4dc3a32d27f002dd51cddc71c93e63fa22` |

V1 freeze 4/4 rehashes. The V2-retrieved `compiled_frozen_v1` scripts are byte-identical to the V1 case compiled inputs (`fba3ca15…` exact Q, `ac94aeba…` `F_65521`). V1 exact-Q / `F_65521` stdout hashes are `ffb45c28…` / `d2cb6b8a…`, matching the negative-control note.

Ancestry pins consumed by V1 also rehash: base `compile_r1_d1_ac.py` `e024a13d…`, its freeze `34b0f325…`, the V12 source-support erratum `997dda08…`, first-normal promotion `40790378…`, closure criterion `3c0a33ce…`, CGE3 compiler `352ad4f2…`, load-ladder `77f25216…`, `tails.json` `d72f774c…`, canonical all-tails `6eed03d4…`. All seven Faber rows contain `k10`, `k6`, and `k2` monomials.

Exact Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_v2_t2_q_20260826T123000Z_box03` | `…_v2_t2_p65521_20260826T123000Z_r6d` |
| Characteristic | `0` in both rings | `65521` in both rings |
| V2 compiled script SHA | `ef494de76514760830e4838e7d336cd8982f4a56cacbe8d8cf147c1f0946ab6d` | `16ed9782ab3d2e02ccc79e026b3b598fede5ef7a54f3b318aaca264011ae6074` |
| V1 compiled script SHA | `fba3ca15122e8513f5a051950289a9d7c79d99656823b604d61e2124d9ac64fc` | `ac94aeba096e2db35b2c49a669f1eaacccb50b6eb5abd9f591d02a28601c8526` |
| `replacement_count` | `2` | `2` |
| Engine `rc` | `0` | `0` |
| Validator | `PASS_D1_LOAD_TRANSITION_A6_A7_V2_T2` | `PASS_D1_LOAD_TRANSITION_A6_A7_V2_T2` |
| Stdout SHA | `5608226c57b3af5764d384a2698efb1c9d78d2ebc5520246df9985a8a81c2f4e` | same sentinel payload |
| Stderr SHA | `d5eb429c6662fee05697265c06aa5803b4f7bbffbf4f91610edf5f4d18c67897` | `bd1988d54d7e5df3015239761045e1a847f7a6e5a873739862e9dfee2a4c9421` |
| Peak RSS / swaps | 16,368 KiB / 0 | 13,360 KiB / 0 |
| User time | 0.05 s | 0.03 s |

The two V2 compiled scripts differ by exactly the four ring-characteristic tokens (`Ra6`, `Ea6`, `Ra7`, `Ea7`). Substitutions, `t*t` repair, recurrences, maps, and sentinels are otherwise identical. The two validation files are byte-identical (`engine_rc=0` plus the same validator line), hash `6478937a…`; that common payload is not evidence that the runs were copied. Identical stdout is expected: on success the script prints only `0/1` markers. Both `freeze_check.stdout` records report every `FREEZE` row OK. Both metas record `argv` as `timeout 1800 Singular -q` on the lane-local V2 script, return code 0, and stdout hashes matching `EVIDENCE.sha256`. Caps were 24 GiB virtual (`25165824` KiB), 600 s compile, 1800 s engine. Compiler stderr is the empty-file digest `e3b0c442…` on both lanes. The validator rejects `=FAIL`, `// **`, a leading `?`, and `error occurred`.

A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

---

## 1. V1 immutability, fail-closed remainder, and the two-token repair

V1 is pinned by digest and was re-emitted unchanged as `compiled_frozen_v1/` on both V2 lanes. It is AWS-only, refuse-if-exists, and pin-checks the r1/d1 base, the V12 erratum, first-normal, and closure before writing. Both V1 engines returned `rc=0`. Source extraction at `a=6` passed (`SOURCE_DIVISIBLE`, `SOURCE_QUOTIENT_IDENTITIES`, `SOURCE_SUPPORT_FILTER`, `ROW_IDENTITIES_23` all `1`). The fail-closed validator rejected the unique required marker `A6_ROW_IDENTITIES_24=1`. Exact-Q remainders, reproduced from the frozen V1 stdout, are

```text
row 1: -(3/4) c0 k60 + (3/4) c1 k60
row 2:  (3/8) p c1 k60 + (3/4) c0 k60
row 3:  (3/16) p c0 k60 - (3/16) p c1 k60
row 5:  (3/128) p^2 c0 k60 - (3/128) p^2 c1 k60
row 7:  (3/512) p^3 c0 k60 - (3/512) p^3 c1 k60.
```

Rows 4 and 6 printed no remainder (so those checks were `0`). The defect is isolated to the new analytic comparator: source rows and the grade-23 bridge already passed.

Convention: the generating function used by `analytic_extract` satisfies `h_{\mathrm{row}}=[t^{\mathrm{row}+1}]H`, and `H=tF` where `F` is the meromorphic function of `z=1/t`. Then `L=z^2+p/2=t^{-2}(1+\mathrm{sp}\,t^2)` and `1/L=t^2\mathrm{Inv}_1`. Direct polynomial coefficients give `C_{\mathrm{poly}}=c_1 z+c_0`, so `C_t=c_1+c_0 t` and

```text
C_poly / L = t C_t Inv1.
```

The binomial expansion of `sigma^{12} k6 f^{3/4}` (recomputed in §3) contributes exactly `(3/4)sigma^{17} k6 C/L` as the first `C/L` polar piece. Therefore

```text
F_S = (3/4) k6 t C Inv1,     H_S = t F_S = (3/4) k6 t^2 C Inv1.
```

This is the same `t` convention as the frozen universal emitter: `H_{AC}=(3/4)sigma^{10} t A C \mathrm{Inv}_1` because `A_{\mathrm{poly}}C_{\mathrm{poly}}/L=A_t C_t\mathrm{Inv}_1`, and `H_{C^2}=(3/8)sigma^{10} t^3 C^2\mathrm{Inv}_2` because `C_{\mathrm{poly}}^2/L^2=t^2 C_t^2\mathrm{Inv}_2`. V1 encoded `k6 C/L` as if it already had two polynomial factors.

Independent check of the printed remainder: V1 used `H=(3/4)k60\, t(c_1+c_0 t)\mathrm{Inv}_1`. Then `[t^2]H=(3/4)k60 c_0` and `[t^3]H=-(3/8)p k60 c_1`. For rows 1–2, `T_0=1` and `T_1=0`, so the predicted `g_1,g_2` are those coefficients. The source image of `t^2 C\mathrm{Inv}_1` is `g_1=(3/4)k60 c_1`, `g_2=(3/4)k60 c_0`. Subtracting yields exactly the printed row-1 and row-2 remainders. The error is a tail-row alignment of the new analytic comparator, not a source defect and not evidence about the D1 contact.

V2 runs frozen V1, then replaces the unique token

```text
(3/4)*sigma^17*t*(k60+sigma*k61)
```

by

```text
(3/4)*sigma^17*t*t*(k60+sigma*k61)
```

and refuses unless the occurrence count is exactly 2. Byte reconstruction from each V1 script by that replacement equals the corresponding V2 script. Each pair differs in exactly two lines (`A6_Hshift`, `A7_Hshift`); lengths grow by four characters; the old token is absent from V2 and the new token occurs twice. Nothing else changes. The compiled `Hshift` lines retain every universal summand and append the repaired `t*t` term.

---

## 2. Source compiler, tails, loads, targets, outer `sigma`

`extract_source` emits, for each of the seven rows, `tail_text` of the frozen Faber row with

```text
loads = {k10: k0,  k6: (k60+sigma*k61),  k2: k2load},
targets = {1: 0, 2: mu2, 3: 0, 4: mu4, 5: 0, 6: mu6, 7: J/4},
```

subtracting `sigma^{2(12+\mathrm{row})} \times` target when the target is nonzero. Compiled `A6_Phi1..Phi7` and `A7_Phi1..Phi7` are those expansions, not the eight-term analytic. Every tail row contains `k10`, `k6`, and `k2` monomials. Weight bookkeeping in the ladder is `Lambda^{2,6,10}` for `(k10,k6,k2)`, i.e. `sigma^{4,12,20}`, matching `sigma^4 k10 f^{5/4}`, `sigma^{12} k6 f^{3/4}`, `sigma^{20} k2 f^{1/4}`.

`source_coefficients` realises `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R`, `D=LA+C`, `L=z^2+\mathrm{pp}/2`, `pp=p+2 sigma ell1`, after the documented factors 2 and 4 (direct polynomial `C,R`, not the older `2C` / `R/4` emitter). Outer `sigma` then contact `sigma`:

```text
kc = sigma^2 * rz,   rz = sigma^a * eta * b1
kr = (pp)^2/4 + sigma^2 * rc
n3 = sigma^3 * az,   az = sigma^a (a1+sigma aa1)
n1 = sigma^3 ((pp*az)/2 + cz),   cz = sigma^{a+1} (c1+sigma cc1)
```

and cyclic in the constant terms. The compiled `Phi` display these compositions explicitly: e.g. `sigma^2*((sigma^6*eta*b1))` at `a=6`. No doubled or dropped outer `sigma` after the contact substitution. Quotient extraction is `Phi / sigma^{11+2a}` with a `reduce` divisibility check and the polynomial identity `sigma^g Q = Phi`, then one further exact `/sigma` step to the next grade.

---

## 3. Complete support through grades 23/24 and 25/26

Write `f=L^4(1+\varepsilon)` with `varepsilon=2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 D/L^4` and `D=LA+C`. Binomial `(1+\varepsilon)^{3/4}` times `L^3`, then `sigma^{12} k6`, gives the polar pieces

```text
(3/8) sigma^{16} k6 R^2 / L
(3/4) sigma^{17} k6 C / L
```

as the first two nonpolynomial terms: the `(3/4)\varepsilon L^3` contribution `(3/4)sigma^4 R^2/L` is corrected by `(-3/32)\varepsilon^2 L^3` to `(3/8)sigma^4 R^2/L`, while `C/L` at `sigma^{17}` receives no `\varepsilon^2` contamination (that starts at `sigma^{19}`). Independently, `f^{3/2}` contributes

```text
(3/4) sigma^{10} AC / L + (3/8) sigma^{10} C^2 / L^2
```

from `(3/8)\varepsilon^2 L^6` acting on `D^2/L^2`, and `sigma^4 k10 f^{5/4}` contributes the in-window simple pole

```text
(5/8) sigma^{11} k10 R C / L
```

from the mixed `\varepsilon^2` term `2\cdot(2 sigma^2 R/L^2)\cdot(sigma^5 D/L^4)`.

Orders at unit leading `k6`, `k10`, `ord(A)=a`, `ord(C)=a+1`, `ord(R)\ge a`:

| term | absolute order | `a=6` | `a=7` |
|---|---:|---:|---:|
| `AC/L` | `11+2a` | 23 | 25 |
| `C^2/L^2`, moving-`L` of `AC` | `12+2a` | 24 | 26 |
| `k6 C/L` (`S0`) | `18+a` | 24 | 25 |
| `k6` first jet / moving-`L` of `S0` (`S1`) | `19+a` | 25 (out) | 26 |
| `k10 RC/L` (`KRC`) | `12+2a` | 24 | 26 |
| `k6 R^2/L` | `16+2a` | 28 | 30 |
| `k10 R^3/L` | `10+3a` | 28 | 31 |
| `k10 A^2/L` | `14+2a` | 26 (out of 23–24) | 28 |
| `k2 R/L` | `22+a` | 28 | 29 |
| `mu2` target | 28 | 28 | 28 |

Windows are `(23,24)` and `(25,26)`. The only new lower-load terms inside those windows are `S0` and, at `a=7` grade 26, `S1`. No `k2`, target, additional `k6`, unloaded `A^3` (`sigma^{15+3a}`), or extra `k10` polar form is omitted. The analytic `Hshift` contains the higher universal summands; they simply have valuation outside the extracted grades.

---

## 4. `SOURCE_SUPPORT_FILTER`

Forbidden charges are `k60,k61,k2load,mu2,mu4,mu6,J`. Allowed, grade by grade:

```text
a=6 grade 23:  none
a=6 grade 24:  k60
a=7 grade 25:  k60
a=7 grade 26:  k60, k61
```

Compiled `diff` lines match this: `A6_g23_*` forbids `k60`; `A6_g24_*` forbids `k61` but not `k60`; `A7_g25_*` forbids `k61` but not `k60`; `A7_g26_*` forbids neither. Any nonzero derivative in a forbidden variable sets `support=0` and quits. A `diff` check cannot hide a forbidden dependence.

The filter is an upper bound. It does not require an allowed variable to appear, and it does not mention `k0` or `eta`. Completeness of `S0,S1,KRC` is the §3 expansion plus the row bridge (and, for `k6`, the source-side negative control). A missing `k10` term in both source and analytic would not trip the filter; the independent grade table is the check that no such term belongs in the window, and a source/analytic mismatch would trip `ROW_IDENTITIES`.

---

## 5. Moving `T0+T1`, analytic coefficients, recurrences

`transform_series(i,j)` is the expansion of the universal even connection in the moving parameter `p+2 sigma ell1`: `delta=i-j=2n`,

```text
T0 = c p^n,     T1 = 2 n c ell1 p^{n-1},
c = (j/2)(j/2+1)...(j/2+n-1) / (n! 2^n).
```

`row_checks` at the first grade uses only `T0`; at the next grade, `offset=1`, it uses `T0` on current `h` and `T1` on previous `h`. There is no `ell2` in the ring and `T2` is never applied. This is the moving row-basis connection, not a V12 name.

Ordinary coordinates are `h_{\mathrm{row}}=[t^{\mathrm{row}+1}]H`. Expanding the compiled `Hshift` at `a=6,7` through two grades reproduces U0, U1, KRC, S0, S1 as written in the verdict, including the moving-`L` pieces from `d\mathrm{Inv}_1/d(\mathrm{sp})=-t^2\mathrm{Inv}_2`. Marker names were not used: the coefficients come from the binomial series and the `tF` convention.

First-grade recurrence: `h_{k+2}+(p/2)h_k=0` for `k=1..5` is `L F` polynomial of degree `<2`, i.e. a simple pole of type `N/L`. Next-grade recurrence: `h_5+p h_3+(p^2/4)h_1=0` and cyclic is `L^2 F` polynomial of degree `<4`. Simple poles sit in that four-dimensional numerator space as `N_1 L`. Compiled `Nfirst` / `Nnext` are exactly those numerators. Both recurrences use the leading `L=z^2+p/2`; moving `ell1` is a numerator correction, not a change of denominator.

---

## 6. Negative controls

1. **Delete `T1`.** At the next grade, `g` is compared to the `T0`-only prediction. `t1needed=1` means that prediction fails. `T1` is generically nonzero for every even `i-j\ge 2`, and the first-grade `h` (U0, and at `a=7` also S0) is generically nonzero before allocation. This is a source-row test of a nonzero module, not a presentation artifact. After V2, full `T0+T1` identities pass, so the failure of `T0` alone is exactly the moving connection.

2. **Delete `k6 C`.** Source `g` is tested for `diff(-,k60)` / `diff(-,k61)`. Combined with the support filter this reduces to: `a=6` grade 24 depends on `k60`; `a=7` has a `k60` or `k61` dependence (and the `a=7` shifted maps fail unless S0 is present in the first numerator). The dependence is in the frozen Faber rows, not in `Hshift`.

3. **Delete `k10 RC`.** The compiled test is `diff(H_{g+1},eta)!=0` on the analytic generating function. In the window the unique `eta` term is KRC (every other `R` polar form has higher valuation). That makes the labelled control analytic-side. It is still a genuine module of the package: deleting KRC from `H` would drop `eta`, and deleting it from the source without dropping it from `H` would break the row identities. A stricter source `diff(g,eta)` is not present; it is not a hole in the algebra.

All three controls fail-closed (`product != 1` quits). V2 stdout has all six markers equal to `1`.

---

## 7. `a=6`: exhaustive allocation and residue

First-grade receiver is U0 only. `Nfirst` vanishes identically iff `L` divides `A0 C0`. On `D(p)`, `L` is squarefree of degree 2. Degree `<2` factors force one of: opposite roots of `L`; `A0\equiv 0`; or `C0\equiv 0`. The last two are `ord(A)>6` or `ord(C)>7`, outside the contact. Same-root allocation gives `(z-\lambda)^2`, not a multiple of squarefree `L`. Constant `A0` (`a1=0,a0\neq 0`) is linear times constant, degree 1, not a multiple of `L`. So the only in-contact solutions are the two opposite-root charts

```text
A0 = aua (z \mp lambda),   C0 = cvg (z \pm lambda),
```

which are exactly `A6_posmap` / `A6_negmap` (`p\mapsto -2\,\mathrm{rtx}^2`). Then `A0 C0 = aua\, cvg\, L` and `[U0]_-=0`.

At the allocated `A`-root, clear `L^2`. Every simple pole (`S0`, `KRC`, `(A1 C0+A0 C1)/L`) contributes an extra `L` to the numerator and vanishes. The moving-`L` term `-(3/4)ell1 A0 C0` vanishes because `A0(\lambda)=0`. The only surviving value is

```text
(3/8) C0(lambda)^2 = (3/8)(2 cvg lambda)^2 = (3/2) lambda^2 cvg^2.
```

Compiled residue identity is that polynomial. It is nonzero on `D(p)` with nonzero leading `C`.

---

## 8. `a=7`: leading factor, shifted maps, cancellation, residue

First-grade receiver is U0+S0:

```text
(3/4) C0 (A0 + k60) / L.
```

The factor is the displayed linear `A0+k60=a1 z+(a0+k60)`, not a presentation name. `L` divides the product iff opposite roots, or `C0\equiv 0` (out of contact), or `A0+k60\equiv 0`.

The two opposite-root maps are the compiled `A7_posmap` / `A7_negmap`:

```text
a0 |-> \mp aua rtx - k60,   c0 |-> \pm cvg rtx,
```

so `A0+k60=aua(z\mp\lambda)` and `C0=cvg(z\pm\lambda)`. First numerator vanishes identically on both charts.

At the shifted-`A` root, `A0(\lambda)=-k60`. Simple `S1` pieces `(k61 C0+k60 C1)/L` and KRC vanish after `L^2`. The two moving-`L` numerator values are

```text
U1:  -(3/4) ell1 A0(lambda) C0(lambda) = +(3/4) ell1 k60 C0(lambda)
S1:  -(3/4) ell1 k60 C0(lambda).
```

They cancel by `A0=-k60`. The remaining value is again `(3/8)C0(\lambda)^2=(3/2)\lambda^2 cvg^2`.

The residual first-numerator component `a1=0`, `a0=-k60` (constant `A` of order 7, inside the contact when `k60\neq 0`) is not a third root chart: `Nfirst` already vanishes without allocating `C0`. On that face the moving-`L` terms cancel as polynomials and the `C1` simple-pole pair cancels, leaving

```text
N = (3/8) C0^2 + L C0 \cdot((3/4)(A1+k61)+(5/8) k0 R0).
```

If the second summand is nonzero its degree is at least 2, while if it is zero then `N=(3/8)C0^2`. Neither vanishes for `C0\neq 0`. This face is therefore empty. It is not a missing hypothesis that breaks the elimination claim; it is the remaining component of the derived factor `C0(A0+k60)`.

---

## 9. `eta` truncation

`R=sigma^a eta (b1 z + b0)` with `eta` a ring variable. Arbitrary `eta` is the exact grade-`a` section, including the closed face `eta=0`. No substitution `eta=sigma^s` or `theta=sigma^n` occurs; `a` is fixed at 6 and 7. The next `R` jet would first produce a `k10 R_1 C` term at grade `13+2a`, which is after `g+1=12+2a`. Thus `eta=0` is complete through the next grade for every `ord(R)>a`. This is a finite truncation, not a disguised unbounded substitution.

`Inv_1,Inv_2,Inv_3` are the binomial series of `(1+\mathrm{sp}\,t^2)^{-1,-2,-3}` through `t^8`. Ordinary coordinates run through `[t^8]`, so the truncation is exact for seven rows.

---

## 10. Inversions, exact-Q versus finite field, AWS, scope

Inversions / nonzero contacts actually used:

- `D(p)`: two distinct roots of squarefree `L`, `lambda^2=-p/2`, compiled as `p\mapsto -2\,\mathrm{rtx}^2`.
- `D(k10)`: ambient first-normal reduction to the square; not a factor of the residue `(3/2)lambda^2 cv^2`.
- Nonzero leading `A` and `C` for exact orders `a` and `a+1` (`aua`, `cvg` as leading `z`-coefficients).
- Characteristic not `2` or `3` (coefficients `3/4,3/8,5/8,3/2` and the `L^2` leading `1/4`). Exact Q is characteristic 0. `65521` is a software control: `2,3,5` remain units; it is not a characteristic-zero proof.

No inversion of `k60`, `eta`, `ell1`, or `L` in the ring: poles are encoded by generating functions and recurrences.

The geometry is arcwise / set-theoretic: two oriented root charts, not a scheme-theoretic initial ideal, not a radical membership, and not a fan cover. Engine `rc=0`, validator PASS, no rejected diagnostic, `/usr/bin/time -v` in stderr, zero swaps, virtual-memory cap 24 GiB, compile/engine caps 600/1800 s, AWS-only compilers, distinct hosts, distinct compiled-script hashes.

---

## 11. Firewall and Pell/Chebyshev

The compiled scope string is `TWO_K6C_TAIL_ALIGNMENT_REPLACEMENTS_ONLY_NO_FAN_OR_ORDER2_VERDICT`. `RESULT.md` claims only the fixed `a=6,7` D1 contacts on `D(p*k10)`. It claims no `a\ge 8`, no positive-order `k10`, no `p=0`/`k10=0`, no other face, no zero/infinity receiver, no scheme structure, and no full square / order-two / `(8,12)` / maximum-twelve / JC2 theorem.

At `a=8`, `k6 C/L` has order `18+8=26` while `AC/L` has order `11+16=27`, so a unit `k6 C/L` precedes the old `AC` face. That successor is correctly left open.

The all-load Chebyshev/Pell survivor is the reduced support of `sqrt(Q)(k10 Q^2+k6 Q+k2)` in which `k6` and `k2` are comparable to `k10` and may cancel off the unit-`k10` square. Emptiness of the two listed D1 contacts on `D(p*k10)` does not contradict that locus. Later complete-support clients must keep it as a positive control, as `RESULT.md` states.

---

CONFIRMED
ORDER2_SQUARE_D1_A6_A7_V2_CONFIRMED
