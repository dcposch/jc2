# Hostile review — D1 `a>=13` grade-38 order-two odd-row recurrence

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_age13_j38_odd_recurrence_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing source monomial | none through grade 38; first pole-order-three monomial is `k2*C/L^3` at grade 39 |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and finite-field agreement are not authority |
| Method | SHA-256 of every named pin; frozen seven-row Faber tails plus D1 substitutions; lower-unitriangular Faber matrix over `Q(p)`; generating-function pole census; compiled-script inspection. No Singular re-execution, Sage, msolve, Lean, or package compiler |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the four required primary pins match. Every path named in `FREEZE.sha256` (8/8) and `EVIDENCE.sha256` (35/35) rehashes to the printed digest. Nested `compiled.sha256` on both lanes rehashes (2/2 each). Parent high-contact freeze 9/9 and V3 parenthesized-load freeze 7/7 rehash. Frozen `tails.json` is `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`; canonical all-tails digest is `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`. Exact Q is the theorem endpoint; `F_65521` is a separate compiled input and a separate engine transcript. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the registered D1 high-contact chart `D(J)`, after the cited square/D1 gates, write

```text
A = sigma^13 theta Abar,   C = sigma^14 theta Cbar,
R = sigma^13 theta eta Rbar,
```

with independent jets of the moving connection `p(sigma)`, of `A,C,R`, of the parenthesized loads `k10,k6,k2`, and of the sparse targets `mu2,mu4,mu6,J/4`. Through absolute grade 38 every source term has pole denominator at most `L^2`. The four odd Faber rows of any such source satisfy the formal identity

```text
Phi7 - (p(sigma)/4) Phi5 - (p(sigma)^2/32) Phi3
     - (p(sigma)^3/128) Phi1  =  0   mod sigma^39.
```

The only odd-row target is `-sigma^38*(J/4)` in row seven, so the same combination of the full rows is `-sigma^38 J/4` modulo `sigma^39`. Vanishing of the seven source equations therefore forces `J=0`. Adjoining `iJ*J-1` yields the unit ideal before radicals, which is emptiness on the named chart `D(J)`.

The identity is polynomial in the independent variables `theta,eta`. Substituting `theta=sigma^n`, `eta=sigma^s` covers every integer contact `a=13+n`, `c=a+1`, `r=a+s`. After a common ramification the same homogeneous substitution covers every rationally valued arc with `a>=13` and `r>=a`; extra nonnegative powers of the uniformizer only delay walls. Neither `theta` nor `eta` is inverted.

The separately compiled `a=12` block is a negative control for the proof method: the order-two combination first fails at grade 38 by a nonzero coefficient depending on the leading `k2` load, which is the newly arriving triple pole `k2*C/L^3`. That is not a survival result for `a=12`.

The Chebyshev/Pell identity is a nonempty engine heartbeat and is not an input to the D1 statement. No claim is made about `a<=12`, `V(J)`, other D1 cells, excluded lifecycle charts, the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Four primary pins | hashes | all four match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 8/8, `EVIDENCE` 35/35, both nested `compiled.sha256` 2/2 |
| 0. Ancestry | high-contact parent, V3 parentheses, tails | parent freeze 9/9, V3 freeze 7/7, tails `d72f774c…`, canonical `6eed03d4…` |
| 1. Exact Q vs `F_65521` | separate hosts, scripts, transcripts; rc, diagnostics, swap | **holds**; exact Q is characteristic 0; `F_65521` is a software control |
| 2. Seven-row reconstruction | frozen Faber, parenthesized `k10,k6,k2`, moving `p(sigma)`, jets, sparse targets | **holds**; 36,54,58,81,89,120,131 monomials; V3 counts 190/72/27 |
| 2. Smallest omitted monomial | polar support through grade 38 | **none** that can hit grade `<=38` at pole order `>=3` |
| 3. Baseline inventory | `k6 C/L` 31, `k2 R/L` 35, `AC/L` 37, `C^2/L^2`, `k10 RC/L`, `k2 A/L^2` at 38; first triple pole at 39 | **holds** by generating-function expansion of the three loads plus unloaded polar terms |
| 4. Odd-row syzygy | signs and coefficients of `(R)` for pole order `<=2` | **holds**; combination equals `h7 + p h5 + (p^2/4) h3` |
| 5. Row-seven target | full combination changes by exactly `-sigma^38 J/4`; even targets cannot enter; `iJ*J-1` is the unit ideal; `J` is the Keller constant | **holds** |
| 6. Homogeneous coverage | `theta=sigma^n`, `eta=sigma^s`; ramification; no hidden unit | **holds**; `theta,eta` are free polynomial variables, not inverted |
| 7. `a=12` negative control | order-two recurrence broken by `k2 C/L^3` at grade 38; not a survival | **holds** as a scoped method control |
| 8. Pell control and firewall | nonempty Chebyshev/Pell heartbeat; no claim beyond the registered D1 source cone on `D(J)` | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the four required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `09ca321436f4262b680801b74dc365cdff632c7630b65da50476547e5229139c` | producer report |
| `.../EVIDENCE.sha256` | `0a65d8b2e792fc7e68e9a7aa17995a51b2eb38f09fe19845b77cbeb343757491` | evidence freeze |
| `.../FREEZE.sha256` | `956090162a137a4afe3f4544f8d41c5622d38ec5627f1669f58a219c45a42358` | source freeze |
| `.../compile_age13_j38.py` | `246f6279b7801d21896936531c706dea3d22f42fa2c702f11eb6ec74e011bff5` | AWS compiler |

`FREEZE.sha256` names eight files, all matching:

| Path | SHA-256 |
|---|---|
| `REGISTRATION.md` | `2dc25ae1ec6ddac96ce828254bc1895649144c729524882d0f735e9cdd13e5c0` |
| `compile_age13_j38.py` | `246f6279b7801d21896936531c706dea3d22f42fa2c702f11eb6ec74e011bff5` |
| `run_aws.sh` | `48673588b13b65a730add970b7634039951b3ee8f59e80bfd83886dad671e58b` |
| `launch_host.sh` | `cf679e19e414680a601f620302f4ef0d48312dcb3261eaad7809f3be60e41f02` |
| parent `compile_highcontact_c2_shadow.py` | `c6eeb50e25cd814855785203165a06da39404c792698e22992efef954c79855c` |
| parent `REGISTRATION.md` | `38f912f271f5cb07d4eaa7c871f4515be19b2918ca01bf5bb751522110cdc1c7` |
| parent `FREEZE.sha256` | `fa3d24f86bc208a909f15b161f6a6a1fab4450c9304c8b2950fdf90dc84a95f3` |
| `ops/aws_exact_lane.sh` | `ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b` |

`EVIDENCE.sha256` names 35 files; all 35 rehash. Nested `compiled.sha256` files rehash to the retrieved `.sing` and `result.json` on each lane. Parent high-contact freeze 9/9 and V3 freeze 7/7 rehash, including

```text
0f7b9482f214347858f61181119f52fc434de8223ae7a3c4099049bd737897ef
  compile_v3_parenthesized_loads.py
88609fdfc50b89625f79e7dcee3b8ceb47d61c3b6668e86ee80da67ad4129e24
  V3 RESULT.md
8a36f5edee279964f547a5ce0d2bbe0511e9cfaf6c5261cce6d115f4b3fcf46f
  V2 compile_a9_recursive.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  tails.json
6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8
  canonical all-tails
```

Exact Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_q_20260826_box03` | `…_p65521_20260826_r6d` |
| PID | `237125` | `295178` |
| Characteristic | `0` in both rings | `65521` in both rings |
| Compiled script SHA | `403a66224a3111c6e387a06ccab9daf308c7297619abda72f3abba69402cb277` | `e4202be6ae82f9167967439c2deba75decd78dcfc6e2d990577bd7fba4530a1b` |
| Engine `rc` | `0` | `0` |
| Stdout SHA | `74591b2cc4bcd9fe1102fd8de31800659f3eb9e0f1747e1433a3e8ad3cfff27c` | same boolean transcript |
| Stderr SHA | `08c80e709f85d19f065c2bc8c86c7d8d8a6051fd344bb2d3427a7809e0658cc8` | `b0e2ad794a1afa56a57000945fd2d6f56c38d01ca33e49126182ecef5e46cd2e` |
| Peak RSS / swaps | 1,601,328 KiB / 0 | 1,263,580 KiB / 0 |
| Wall | 2:27.51 | 1:52.35 |
| VM cap | 33,554,432 KiB | 33,554,432 KiB |

Meta `argv` on each host is `timeout 3600 Singular -q` of the frozen compiled input whose SHA is in `result.json` and `compiled.sha256`. Compiler stderr is the empty-file digest `e3b0c442…` on both lanes. Engine stderr is GNU `time` only: no `?`, `error occurred`, or `=FAIL`. Caps were 32 GiB virtual, 1200 s compile, 3600 s engine.

The two compiled scripts are byte-identical after replacing the two ring-characteristic tokens (`ring R13=…` and `ring R12=…`). Size gap 8 bytes equals `65521` versus `0` twice. Substitutions, parenthesized loads, recurrences, unit test, `a=12` control, and Pell block are otherwise identical. Stdout hashes coincide because both engines print only the boolean sentinels `=1`; that agreement is not a coefficient check and is not used below. The validator string is not a mathematical verdict.

A passing manifest is not a theorem. What follows is the source.

---

## 1. Seven literal rows from frozen tails

The compiler does not emit an eight-term Laurent polynomial as source. It imports frozen `compile_highcontact_c2_shadow.py`, which walks V3 parenthesized loads to V2 to V1 to `compile_r1_d1_ac.py` to `compile_cge3_universal.py` to `compile_square_load_ladder.py` and `tails.json`. Before any `.sing` is written it rechecks every imported pin and the canonical all-tails digest. Each ordinary coordinate is

```text
tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
```

with target subtractions `-sigma^{2(12+row)}*(mu20-jet | mu4-jet | mu6-jet | J/4)` on rows 2, 4, 6, 7. `tail_text` refuses a monomial whose length is not the frozen name list, whose load exponents are not in `{0,1}` with at most one load, or whose weighted degree is not `12+row`. Load weights in `Lambda` units are `k10:2`, `k6:6`, `k2:10`, i.e. `sigma^4 k10`, `sigma^{12} k6`, `sigma^{20} k2` after `Lambda=sigma^2`.

Frozen Faber `tails.json` has seven rows with 36, 54, 58, 81, 89, 120, 131 monomials. Load monomials total `k10` 190, `k6` 72, `k2` 27, matching the V3 distributivity census. The compiled exact-Q `a=13` block contains those parenthesized jets at exactly those cardinalities,

```text
(k0+sigma^1*k0_1)                                             190 times, always times (sigma^2)^2
(k60+sigma^1*k60_1+...+sigma^7*k60_7)                         72 times, always times (sigma^2)^6
(k20+sigma^1*k20_1+sigma^2*k20_2+sigma^3*k20_3)               27 times, always times (sigma^2)^10
```

with no unparenthesized `k0+sigma`, `k60+sigma`, or `k20+sigma` remnant. The `a=12` block has the same three cardinalities with the longer `k60` and `k20` jets required by the earlier walls.

D1 substitutions, from frozen `source_coefficients` of `compile_r1_d1_ac.py`, are the dictionary of `K=L(sigma)^2+sigma^2 R` and `D=L A+C`:

```text
pp = p + 2 sigma ell1 + ... + 2 sigma^{10} ell10
kc = sigma^2 rz,     kr = pp^2/4 + sigma^2 rc
n3 = sigma^3 az,     n2 = sigma^3 ac
n1 = sigma^3 ((pp az)/2 + cz),   n0 = sigma^3 ((pp ac)/2 + cc)
a6=2 pp, a5=2 kc, a4=pp^2+2 kr, a3=2 pp kc + sigma^2 n3,
a2=kc^2+2 pp kr+sigma^2 n2, a1=2 kc kr+sigma^2 n1, a0=kr^2+sigma^2 n0.
```

The compiled `a=13` rows substitute

```text
az,ac = sigma^{13} theta (a1-jet, a0-jet),
cz,cc = sigma^{14} theta (c1-jet, c0-jet),
rz,rc = sigma^{13} theta eta (b1-jet, b0-jet),
```

with `a_index=1`, `c_index=7`, `r_index=3`, sized from the first-arrival formulae `25+a`, `18+a`, `22+a` against ceiling 38. The moving connection is the same `pp` in the square coefficients and in the odd combination. Sparse targets occur once each, only on the licensed rows, as

```text
row 2: -sigma^28*(mu20+...+sigma^{10} mu20_10)
row 4: -sigma^32*(mu4+...+sigma^6 mu4_6)
row 6: -sigma^36*(mu6+sigma mu6_1+sigma^2 mu6_2)
row 7: -sigma^38*(J/4)
```

Odd compiled `Phi` contain no `mu20`, `mu4`, `mu6`, or `J` except that one row-seven target. `J` is absent from the frozen tails.

---

## 2. Pole census through grade 38

Write `L=z^2+p(sigma)/2`, `K=L^2+sigma^2 R`, `D=LA+C`, and expand the three load generating functions `sigma^4 k10 f^{5/4}`, `sigma^{12} k6 f^{3/4}`, `sigma^{20} k2 f^{1/4}` together with the unloaded polar part of the inverse-Faber generating function. At the baseline `a=r=13`, `c=14` the polar families which can enter by grade 38, with their first grade and pole order, are exactly

| first grade | family | pole | leading coefficient |
|---:|---|---:|---|
| 31 | `k6 C/L` | 1 | `(3/4) sigma^{17} k6 C/L` |
| 35 | `k2 R/L` | 1 | `(1/2) sigma^{22} k2 R/L` |
| 37 | `A C/L` | 1 | `(3/4) sigma^{10} A C/L` |
| 38 | `C^2/L^2` | 2 | `(3/8) sigma^{10} C^2/L^2` |
| 38 | `k10 R C/L` | 1 | `(5/8) sigma^{11} k10 R C/L` |
| 38 | `k2 A/L^2` | 2 | `(1/4) sigma^{25} k2 A/L^2` |

These six first-arrival grades are the substitutions `18+a`, `22+r`, `10+a+c`, `10+2c`, `11+r+c`, `25+a` at `a=r=13`, `c=14`. Direct expansion of the next binomial terms gives the first pole-order-three family

```text
(1/4) sigma^{25} k2 C / L^3     at grade 25+c = 26+a = 39.
```

Every other family of pole order three or higher begins strictly later at this baseline:

| family | pole | first grade at `a=r=13` |
|---|---:|---:|
| `k10 A^2/L` | 1 | 40 |
| `k10 A C/L^2` | 2 | 41 |
| `k6 R^2/L` | 1 | 42 |
| `k10 C^2/L^3` | 3 | 42 |
| `k6 R C/L^3` | 3 | 46 |
| `k2 R^2/L^3` | 3 | 50 |
| `R A^2/L^2` | 2 | 51 |
| `k10 R^3/L` | 1 | 49 |
| `A^3/L^3` | 3 | 54 |

Raising `a` or `r` only adds nonnegative powers of `sigma` to every listed monomial, so no omitted wall can move earlier. The compiled polar jets are cut exactly to these first-arrival formulae against ceiling 38: `c_index=7` for `k6 C/L` at 31, `r_index=k2_index=3` for `k2 R/L` at 35, `a_index=1` for `AC/L` at 37 and `k2 A/L^2` at 38, `k10` through `k0_1` because `k10_1 R C/L` starts at 39. Polynomial (pole-order-zero) first-normal modules in `A,C,R,k10` appear in the raw tail expansion at lower grades; they are annihilated by the same odd combination derived in §3 and cannot cancel `J`. No tail monomial produces a pole of order `>=3` at grade `<=38`.

The smallest source monomial outside the window is therefore `k2 C/L^3` at grade 39. It is not missing from a grade-38 theorem.

---

## 3. Odd-row syzygy, rederived

The frozen Faber transport is the lower-unitriangular matrix `T` of `compile_cge3_universal.py`. For even index gap `i-j=2n`,

```text
T_{ij} =  ((j/2)_n / n! / 2^n)  p^n,
```

and `T_{ij}=0` if `i-j` is negative or odd. The odd block is

```text
Phi1 = h1
Phi3 = h3 + (p/4) h1
Phi5 = h5 + (3p/4) h3 + (3p^2/32) h1
Phi7 = h7 + (5p/4) h5 + (15p^2/32) h3 + (5p^3/128) h1.
```

The claimed combination with coefficients `1`, `-p/4`, `-p^2/32`, `-p^3/128` expands in the `h`-basis as

```text
h7:  1
h5:  5p/4 - p/4 = p
h3:  15p^2/32 - 3p^2/16 - p^2/32 = p^2/4
h1:  5/128 - 3/128 - 1/128 - 1/128 = 0
```

so

```text
Phi7 - (p/4) Phi5 - (p^2/32) Phi3 - (p^3/128) Phi1
  = h7 + p h5 + (p^2/4) h3
  = (S + p/2)^2 h3,
```

where `S` shifts odd index by two. A Laurent source of pole order at most two along the two roots of `L=z^2+p/2` has odd numerator coefficients annihilated by `(S+p/2)^2`. Hence the combination vanishes identically, not merely after a standard basis. Replacing the scalar `p` by the series `p(sigma)` is the same matrix identity in the formal-power-series ring: the compiled rows use one and the same `pp` in `T` (through `a6=2 pp` and companions) and in the combination coefficients. Signs and every displayed denominator are forced by this expansion; the opposite signs of the order-three recurrence `(R3)` are a different annihilator `(S+p/2)^3` and are not used here.

Even-indexed `h` never enter the odd `Phi`, so the even targets `-sigma^{28} mu2`, `-sigma^{32} mu4`, `-sigma^{36} mu6` cannot appear in the combination. The only target that can appear is the row-seven charge `-sigma^{38}*(J/4)`. Therefore the full-row combination equals the source-only combination plus `-sigma^{38} J/4`. Through grade 38 the source-only combination is `0` modulo `sigma^{39}`, and the full combination is

```text
-sigma^{38} J/4   mod sigma^{39}.
```

If every source row vanishes, this forces `J=0`. Adjoin `iJ*J-1`. The grade-38 coefficient is `-J/4`, and `(-4 iJ)*(-J/4)=iJ J=1`, so `1` lies in the ideal before any radical. `J` is the constant Jacobian of the Keller pair, inserted only as that target; it is not a discardable normal coefficient of the source. The statement is empty on `D(J)` and claims nothing on `V(J)`.

---

## 4. Homogeneous coverage

The identity is a polynomial relation in the free variables `theta,eta` together with the jets of `Abar,Cbar,Rbar`. It does not invert `theta`, `eta`, or the leading coefficients of `Abar,Cbar,Rbar`. Substituting `theta=sigma^n` and `eta=sigma^s` with integers `n,s>=0` realises every integer contact `a=13+n`, `c=a+1`, `r=a+s`. If the leading coefficient of `Abar` (resp. `theta`) vanishes, the actual order is strictly larger than 13 (resp. than `13+n`), which remains inside the cone. That is not a hidden unit hypothesis; it is a weaker statement than exact-contact localisation.

A rationally valued arc with `v(A)/v(sigma)>=13` and `v(R)>=v(A)` becomes, after a common ramification that makes the uniformizer integral, an integer point of the same cone. Every source monomial acquires a nonnegative extra power of the new uniformizer, so no wall that was at grade `>=39` in the baseline can appear at grade `<=38` after ramification. The compiled `diff(...,theta)` and `diff(...,eta)` reductions modulo `sigma^{39}` are the homogeneous-stability check of this polynomial identity, not a finite sample of contacts.

---

## 5. The `a=12` calculation is a method control

The same compiler emits a second ring with `a=12`, `theta=eta=1` (exact contact `a=r=12`, `c=13`), no symbolic raise, and the same order-two combination plus the row-seven target restored:

```text
J38N_rel = combo_{a=12} + sigma^{38} J/4.
```

At `a=12` the triple pole `k2 C/L^3` arrives at grade `26+12=38`, in the window. Pole-order-one and pole-order-two companions at this contact (`k2 R/L` at 34, `k2 A/L^2` at 37, `k10 A^2/L` at 38, `C^2/L^2` at 36, `k10 R C/L` at 36) remain of order at most two and are annihilated by `(S+p/2)^2`. The leftover at grade 38 is therefore the order-three principal part, linear in the leading `k2` load. That is exactly the compiled sharpness test `J38N_coeff != 0` and `diff(J38N_coeff, k20) != 0`. It proves that the order-two argument cannot be pushed to `a=12`. It is not a solution, not an emptiness failure, and not evidence that `a=12` survives. Residual contacts `a=10,11,12` are the separately registered order-three replay.

---

## 6. Chebyshev/Pell control and firewall

The compiled heartbeat is the polynomial identity

```text
Q = z^4 - 1,
P = 16 Q^2 + 20 Q + 5,
A = 16 z^{10} - 20 z^6 + 5 z^2,
A^2 - Q P^2 - 1 = 0.
```

Direct expansion of these three polynomials gives residual zero. The identity is the square-chart Pell relation used as an engine-positive control. It does not enter the D1 source, does not identify a Chebyshev survivor, and does not enlarge the theorem.

The registered claim excludes only the D1 source cone

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,  ord_sigma(R)=r,
a>=13,  r>=a
```

on the Keller chart `D(J)`, for the seven literal Faber rows, after the cited upstream square/D1 gates. It does not cover `a<=12`, `V(J)`, `p=0` or `k0=0` lifecycle routing, other D1 cells, the whole square component, order two, `(8,12)`, maximum twelve, or JC2. RESULT and REGISTRATION state that firewall in matching language. No charged artifact claims more.

---

## 7. Defect classification

No mathematical defect of the numbered claim was found. The T-algebra, the pole census, the target parity, the unit-ideal arithmetic, the homogeneous substitution, and the scoped `a=12` wall are independent of the AWS boolean transcript.

No custody or software defect was found. All named hashes match; exact Q and `F_65521` are distinct hosts, distinct PIDs, distinct characteristic tokens, distinct RSS and wall-clock, zero swap, empty compiler stderr, and GNU `time` as the only engine stderr.

No scope wording defect was found. The compiler's unused `J38_symbolic` flag would be false for an exact identity and is correctly not part of the pass condition; that is implementation hygiene, not a wording overclaim.

Smallest failing identity: none.

Smallest missing source monomial: none through grade 38. The first pole-order-three monomial is `k2*C/L^3` at grade 39.

CONFIRMED
