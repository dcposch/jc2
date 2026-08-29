# Hostile review — D1 `a=9` composition through grade 30

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade30_c2_obstruction_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing monomial/variable | none that changes the compact ideal or either unit ideal |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and finite-field agreement are not authority |
| Method | SHA-256 of every named pin; frozen compiler and both compiled scripts; frozen seven-row Faber tails plus D1 substitutions; exact polynomial rewriting of the compact ideal; unit-ideal certificates; no Singular re-execution, Sage, msolve, Lean, or package compiler |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the three required primary pins match. Every path named in endpoint `FREEZE.sha256` (9/9) and `EVIDENCE.sha256` (46/46) rehashes to the printed digest. Nested `compiled.sha256` on both lanes rehashes (7/7 each). Exact Q is the theorem endpoint; `F_65521` is a separate compiled input and a separate engine transcript. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the registered fixed-contact D1 chart

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9
```

with `p*k0` inverted, the seven literal-Faber source rows have no solution in characteristic zero.

The open branch `D(k60)` is empty at grade 27 by the independently rederived identities `(3/4)c1 k60=(3/4)c0 k60=0`. The closed branch `V(k60)` splits exhaustively as `D(k60_1)∪V(k60_1)`. On `D(k60_1)`, `e28z` forces `c1=0` and `g30_4` forces `c0^2=0`; adjoining the Bezout equation of exact order ten yields the unit ideal. On `V(k60_1)`, the exact restricted identities produce `c1 c0` and `2 c0^2-p c1^2`; on `D(p)` both `c0^3` and `c1^3` lie in the ideal, and the same Bezout equation cubes to `1=0`. Neither argument takes a radical. No intermediate algebraic stratum is missed: a DVR point with `0<v(k60_1)<∞` has generic point in the empty open `D(k60_1)`.

The same holds for `0<v(k60)<∞` against the empty open `D(k60)`. Therefore the cell is empty on `D(p*k0)`.

This says nothing by itself about `a>=10`, `p=0`, `k0=0`, other D1 cells, the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Three primary pins | hashes | all three match the required bytes |
| 0. Named manifests | every named file | endpoint `FREEZE` 9/9, `EVIDENCE` 46/46, both nested `compiled.sha256` 7/7 |
| 0. Cited `D(k60)` RESULT | `3679d0db…3412a88` | **holds** |
| 0. Cited grade-27 review | prompt hash vs on-disk file | prompt hash is a transcription error; unique on-disk file and promotion pin agree; grade-27 identities rederived here from tails |
| 1. Ancestry, census, compact ideal | both containments before radicals | **holds**; explicit Q-linear certificates, not radicals/dimension/samples |
| 2. Grade-28--29 collision | four leaders and rows 3,5,7 | **holds**; tails plus D1 substitutions |
| 3. Grade-30 invariant | five identities in the claimed quotient | **holds** with every displayed correction retained |
| 4. Loads and targets | no early zero, no load/target swap, no omitted compact-changing term | **holds** |
| 5. Successor split | `D(k60_1)∪V(k60_1)` after `V(k60)` | **exhaustive** as schemes; no missed DVR stratum |
| 6. Exact-contact localization | Bezout, not a mere nonzero coefficient | **holds** over Q and over char-0 DVRs |
| 7. Controls | frozen Q input, independent `F_65521`, nonempty Pell | **holds** |
| 8. Composition and firewall | this cell on `D(p*k0)` only | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the three required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `bbb1d718a08247d7ff344033e51c988ee52f7ae88a19e98cb059b0ebd8d7cf1c` | producer report |
| `.../EVIDENCE.sha256` | `dc223883009026a2e242735563170a51f081b0c049a966751521e4fff8396f52` | evidence freeze |
| `.../FREEZE.sha256` | `6881229bb9d8f89fe1be3314a7e7a8b654cf2e8f7f101a9b6a5936add1ba3570` | source freeze |

Endpoint `FREEZE.sha256` names nine files, all matching, including

| Path | SHA-256 |
|---|---|
| grade-30 `REGISTRATION.md` | `7fb8ff42b702d88f6fd24bd4b2bd9b0fdaed4e20d9bfccb01706e80aa1f1d0d8` |
| `compile_grade30_c2.py` | `b5000c02d5f91e436cdd0b04a68d17514fc197ed292cd86d20c01bad961a0f37` |
| collision V2 `compile_v2_syntax.py` | `2aab56504850cb0f6e60697c59999c43a62a75b5930ba1b4b27dbf80ec5334cd` |
| collision V2 `RESULT.md` | `eb1b77e1731e438e732ac5f704a99d63f95f10a172855d0e5c2ca67eb39e9f47` |
| `ops/aws_exact_lane.sh` | `ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b` |

Cited `D(k60)` RESULT rehashes to `3679d0dbd883c74a4d1d7d1175daf9461c123dd83272bdf2e713ebd7c3412a88`. Its `FREEZE.sha256` (7/7) and `EVIDENCE.sha256` pin `f878c18a4163e1b94bb150e3a84e626ff3eb9d13382da8d03694b200101c2a0d` rehash.

The prompt charges grade-27 review hash `95e9990bca73d42c2b4ba513ee4bf95acfe9ad6dfbd3d461ab67201a7b2f943e`. The unique on-disk file

```text
xmodel/max12-812-order2-square-d1-a9-k60-grade27-hostile-review-grok-20260826.md
```

rehashes to `95e9990b2acbaaf0cb80afd5722d202f6874dbe10918002c5bdb6353bbb0b9fd`, which is the hash recorded in the grade-27 promotion pin. No second copy exists. The first eight hex digits coincide; this is a prompt transcription error, not a second review and not a failure of the `D(k60)` RESULT pin. Grade-27 identities are rederived from frozen tails in §8, not taken from that review.

Corrected V3 census pins rehash (`RESULT` `88609fdfc50b89625f79e7dcee3b8ceb47d61c3b6668e86ee80da67ad4129e24`, compiler `0f7b9482f214347858f61181119f52fc434de8223ae7a3c4099049bd737897ef`, freeze 7/7). Frozen tails `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`. Collision V2 freeze 9/9.

Exact Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_grade30_c2_q_20260826_box03` | `…_grade30_c2_p65521_20260826_r6d` |
| Characteristic | `0` in all four rings | `65521` in all four rings |
| Compiled script SHA | `3e0617f922dbb05592f18dee242d96b5bd7ae026fd48e07673e4b704dd565826` | `fb4faea76e1910eb79c0accf5f2a47fb5ce7cadea748c6b807cc9415f11c47ba` |
| Parent collision V2 script SHA | `24e57f1d0c47c9bab0ef63b71e086338372c7a2d1476044df791bcc46e9064e7` | distinct char-65521 parent |
| Parent V3 census SHA | `77a0b2db497f1d2276392c1b2f862b3c05aa027c677fb66778cced1c3fad8d9f` | distinct char-65521 parent |
| Engine `rc` | `0` | `0` |
| Stdout SHA | `d516013b67ef7c534bce7da116abca61354120cf855d6e79cf73efa615c35cfc` | `838c22f7fd7c8e6ace481ab0fa816efba2c58a4d41ec5bd3d22779c82b25179d` |
| Peak RSS / swaps | 1,255,328 KiB / 0 | 889,128 KiB / 0 |
| Wall | 6.06 s | 4.16 s |
| VM cap | 16,777,216 KiB | 16,777,216 KiB |

Meta `argv` on each host is `timeout 1800 Singular -q` of the frozen compiled input whose SHA is in `result.json` and `compiled.sha256`. Compiler stderr is the empty-file digest `e3b0c442…` on both lanes. Engine stderr is GNU `time` only (no `?`, `error occurred`, `=FAIL`). Caps were 16 GiB virtual, 600 s compile, 1800 s engine.

The two compiled scripts are byte-identical after replacing the four ring-characteristic tokens. Substitutions, maps, recurrences, sentinels, and the grade-30 receiver are otherwise identical. Exact Q prints `3/4*c1*k60` and `g30_4=-3/16*p*c1^2+3/8*c0^2`; `F_65521` prints `16381*c1*k60` and `12285*p*c1^2-24570*c0^2`, and `3·4^{-1}≡16381`, `-3·16^{-1}≡12285`, `3·8^{-1}≡40951≡-24570 (mod 65521)`. The validator string is not a mathematical verdict.

Parenthesized complete jets times full Faber weights occur in the exact-Q script at the V3 cardinalities `k10` 190, `k6` 72, `k2` 27, with no unparenthesized remnant.

---

## 1. Ancestry, grade convention, source completeness, compact ideal

The recursive emitter substitutes

```text
az = sigma^9 (a1 + … + sigma^4 a1_4),   ac = sigma^9 (a0 + …),
cz = sigma^10 (c1 + … + sigma^4 c1_4),  cc = sigma^10 (c0 + …),
rz = sigma^9 (b1 + sigma b1_1 + sigma^2 b1_2),
rc = sigma^9 (b0 + …)
```

into the frozen D1 map `K=L^2+sigma^2 R`, `D=LA+C` of `compile_r1_d1_ac.py`:

```text
kc = sigma^2 rz,     kr = p^2/4 + sigma^2 rc,
n3 = sigma^3 az,     n2 = sigma^3 ac,
n1 = sigma^3 ((p az)/2 + cz),   n0 = sigma^3 ((p ac)/2 + cc),
a6=2p, a5=2 kc, a4=p^2+2 kr, a3=2p kc+Lambda n3,
a2=kc^2+2p kr+Lambda n2, a1=2 kc kr+Lambda n1, a0=kr^2+Lambda n0,
```

with `Lambda=sigma^2` and `p` replaced by the moving connection `p+2 sigma ell1+…`. The C-summand of `a1` is `sigma^{15} c1`; of `a0`, `sigma^{15} c0`. The A-summand of `a3` is `sigma^{14} a1`; of `a2`, `sigma^{14} a0`; of `a1`, `sigma^{14}(p/2)a1`. Loads are the parenthesized jets times `Lambda^{2,6,10}`. Targets are the literal insertions `-sigma^{2(12+row)}` times `mu20`-jet, `mu4`, `mu6`, `J/4`.

Grade `n` is the coefficient of `sigma^n` in the seven source series: `g_n=subst(Q_n,sigma,0)` with `sigma·Q_{n+1}=Q_n-g_n` as polynomial identities, not truncation. There are 224 row-status markers (`7×32`). Zero of them are nonzero below grade 27. Nonzero counts by grade are 5, 5, 5, 6, 6 on grades 27–31, total 27. Rows 4 and 6 are zero through grade 29; row 6 is identically zero through grade 31. Every displayed body through grade 30 is therefore present.

On `V(k60,k60_1)` write `G_i` for `subst(subst(g30_i,k60,0),k60_1,0)` and likewise `e29z,e29c`. The full ideal

```text
I_full = (k60, k60_1, g27_*, g28_*, g29_*, g30_*)
```

equals, before radicals, the compact ideal

```text
I_c = (k60, k60_1, mu20, e29z, e29c, G_1, G_2,
       c1*c0, 2*c0^2-p*c1^2).
```

Explicit certificates, using the identities of §§2–3 and `(k60,k60_1)⊂I_full∩I_c`:

- `I_full ⊆ I_c`. Each `g27_*` is a multiple of `k60`. `g28_1 ≡ (3/4)c1 k60_1 ∈ (k60_1)`, `g28_2 ≡ -mu20`, `g28_{3,5,7}` are Q-multiples of `e28z∈(k60_1)`, `g28_{4,6}=0`. `g29_1 ≡ e29z`, `g29_2 ≡ e29c`, `g29_{3,5,7}` are Q-linear in `e29z` after `k60=k60_1=0`, `g29_{4,6}=0`. `g30_1 ≡ G_1`, `g30_2 ≡ G_2`, `g30_3 ≡ -(p/4)G_1-(ell1/2)e29z+(3/4)c1 c0`, `g30_4 = (3/16)(2 c0^2-p c1^2)`, `g30_5 ≡ -(p^2/32)G_1-(p ell1/8)e29z-(3/16)p c1 c0`, `g30_6=0`, `g30_7 ≡ -(p^3/128)G_1-(3 p^2 ell1/64)e29z-(3/128)p^2 c1 c0`.
- `I_c ⊆ I_full`. `mu20 ≡ -g28_2`, `e29z ≡ g29_1`, `e29c ≡ g29_2`, `G_1 ≡ g30_1`, `G_2 ≡ g30_2` modulo `(k60,k60_1)`, and

```text
c1*c0           = (4/3)(G_3 + (p/4)G_1 + (ell1/2)e29z),
2*c0^2-p*c1^2   = (16/3) g30_4.
```

No radical, dimension, or sample is used. The engine `std`/`reduce` both-ways test is software confirmation of these rewritings.

---

## 2. Grade-28--29 collision

Frozen tails, unique `a1 k6` / `a0 k6` monomials, val-0 square coefficients `a6_0=2p`, `a4_0=(3/2)p^2`, `a2_0=p^3/2`, and the row-2 target `-sigma^{28}(mu20+sigma mu20_1+…)` give, after `k60=0`,

```text
e28z = (3/4) c1 k60_1,
e28c = (3/4) c0 k60_1 - mu20.
```

Row 1 also has `(3/4)a1 a2` and `(3/4)a0 a3`. The C-part of `a1` times the A-part of `a2` is `(3/4)a0 c1`; the C-part of `a0` times the A-part of `a3` is `(3/4)a1 c0`; the grade-29 pieces of `(3/4)a1 k6` are `(3/4)(c1_1 k60_1+c1 k60_2)`. Hence

```text
e29z = (3/4)(a0 c1 + a1 c0 + c1_1 k60_1 + c1 k60_2).
```

Row 2: `(3/8)a1^2` contributes `(3/8)p a1 c1`; `(-3/8)a1 a3 a6` contributes `-(3/4)p a1 c1`; sum `-(3/8)p a1 c1`. `(3/4)a0 a2` contributes `(3/4)a0 c0`. With the `k6` jets and `-sigma^{29} mu20_1`,

```text
e29c = -(3/8)p a1 c1 + (3/4)a0 c0
       + (3/4)c0_1 k60_1 + (3/4)c0 k60_2 - mu20_1.
```

These are the exact printed bodies. Denominator/moving-connection rows after `k60=0`:

```text
g28_3 + (p/4) e28z = 0,     g28_5 + (p^2/32) e28z = 0,
g28_7 + (p^3/128) e28z = 0, g28_4 = g28_6 = 0,
g29_3 + (p/4) e29z + (ell1/2) e28z = 0,
g29_5 + (p^2/32) e29z + (p ell1/8) e28z = 0,
g29_7 + (p^3/128) e29z + (3 p^2 ell1/64) e28z = 0,
g29_4 = g29_6 = 0.
```

Row 4 and 6 `a1 k6` monomials all contain `a5` or `a3`, which vanish at val 0; companions in rows 3,5,7 are the same cancellations as at grade 27 (`15/128-9/64=-3/128`, `-33/512+27/256-3/64=-3/512`) times `k60_1`. Printed exact-Q bodies match these polynomials termwise.

Collision V1 is a fail-closed negative control (`p^2/32` parsed as a rational exponent). V2 changes only those four token classes; the source rows are untouched.

---

## 3. Hand-derived grade-30 invariant

C-parts of `a1,a0` are both `sigma^{15}`. Pure C² is therefore grade 30, with no loads (`k10·Lambda^2` would add 4). Independent extraction from frozen tails against val-0 square coefficients:

| Row | C² monomials | Coefficient |
|---|---|---|
| 1 | none | `0` |
| 2 | `(3/8)a1^2` | `(3/8)c1^2` |
| 3 | `(3/4)a0 a1` | `(3/4)c1 c0` |
| 4 | `(-3/32)a1^2 a6` + `(3/8)a0^2` | `(3/8)c0^2-(3/16)p c1^2` |
| 5 | `(-3/32)a0 a1 a6` | `-(3/16)p c1 c0` |
| 6 | `(9/256)a1^2 a6^2` + `(-3/32)a1^2 a4` | `9/64-9/64=0` |
| 7 | `(15/512)a0 a1 a6^2` + `(-3/32)a0 a1 a4` | `15/128-9/64=-(3/128)p^2 c1 c0` |

Thus `g30_4=(3/16)(2 c0^2-p c1^2)` and `g30_6=0` as identities in the unrestricted source, not after restriction. Printed exact-Q `g30_4=-3/16 p c1^2+3/8 c0^2` is this polynomial with no extra monomial.

On `V(k60,k60_1)` the remaining rows retain every correction (`C R k0`, `A`-jets, `k60_2,k60_3`, `ell1`):

```text
G_1 = (5/8)(c0 b1+c1 b0)k0 + (3/4)(a0_1 c1+a0 c1_1+a1_1 c0+a1 c0_1
        + c1_1 k60_2+c1 k60_3),
e29z = (3/4)(a0 c1+a1 c0+c1 k60_2).
```

Termwise cancellation in `G_3+(p/4)G_1+(ell1/2)e29z`: each of the twelve non-C² monomials of `G_3` is minus the corresponding term of `(p/4)G_1` or `(ell1/2)e29z`. Leftover `(3/4)c1 c0`. The same pairing with `(p^2/32)G_1` and `(p ell1/8)e29z` (resp. `(p^3/128)G_1` and `(3 p^2 ell1/64)e29z`) produces the row-5 and row-7 identities. Nothing is discarded: the corrections sit in `G_1` and `e29z`, which remain compact generators.

Row 2 keeps its own C² summand `(3/8)c1^2` inside `G_2`; that does not disturb the two C² generators used for emptiness.

---

## 4. Loads, targets, timing

Binomial orders from the same substitutions:

| Term | First grade | Why |
|---|---|---|
| `k60 C` | 27 | `Lambda n1` of C is `sigma^{15}`; `Lambda^6` adds 12 |
| `ell1 c1 k60` | 28 | one `sigma` from `p+2 sigma ell1` |
| `k60_1`, `mu20` | 28 | next `k6` jet; `-sigma^{28} mu20` in row 2 |
| `A C` | 29 | `sigma^{14}` times `sigma^{15}` |
| `C^2` | 30 | `15+15` |
| `C R k0` | 30 | `kc` is `sigma^{11}`; `Lambda^2` adds 4; C adds 15 |
| `k20`, `k0_1`, `k60_4` | 31 | printed `g31_1` contains `(1/2)b1 k20`, `(5/8)(c0 b1+c1 b0)k0_1`, `(3/4)c1 k60_4` |
| `mu4` | 32 | `-sigma^{32} mu4` |
| `mu6` | 36 | `-sigma^{36} mu6` |
| `J/4` | 38 | `-sigma^{38}(J/4)` |

None of `k20`, `k0_1`, `k60_4`, `mu4`, `mu6`, `J` occurs in any grade-30 body. They are present in the ring and in `Q0_*`; they are not set to zero. The delayed-load derivatives of printed `g31_1` are exactly the three displayed coefficients. Each of `mu2,mu4,mu6,J` occurs once, as the literal fragments. `mu20` is a target; `k60_1` is a load; they appear as distinct summands of `g28_2`. Jet lengths `c1..c1_4`, `k60..k60_4`, `a1..a1_4`, `mu20..mu20_3` cover the window. No omitted higher jet can contribute to grade 30.

Collision V2 and the grade-30 wrapper repair only check-side precedence (`p^2/32`, `p^3/128`, `3*p^2*ell1/64`, Pell `z`-header, and the inherited `(sigma^38)/4`). Those tokens are not in the extracted `g_n`.

---

## 5. Exhaustive successor split

As schemes, `V(k60)=D(k60_1)∪V(k60_1)` for the coordinate `k60_1`. There is no third algebraic stratum.

A DVR-valued point with `0<v(k60_1)<∞` is not a third cell. Its generic point lies in `D(k60_1)` (where `k60_1` is a unit of the fraction field) and its special point lies in `V(k60_1)`. Both of those schemes are empty after exact contact (§6), so no such map `Spec(R)→X` exists. Equivalently, emptiness of the generic fibre already kills the point.

The same applies to `0<v(k60)<∞` against empty `D(k60)`. Contact-raising regradings (`a>=10`) are outside the registered cell and outside this theorem.

---

## 6. Exact-contact localization

Exact order ten means the leading coefficient `C_0=c1 z+c0` is a nonzero polynomial, i.e. `(c1,c0)≠(0,0)`. The engine adjoins the Bezout equation `u1 c1+u0 c0=1`, not a mere nonzero-coefficient test. Over a field this is equivalent to `(c1,c0)≠(0,0)` and covers `A^2\setminus\{0\}` with one affine chart; it is not a projective space and omits no field-valued point. Over a DVR, unimodular is strictly smaller than `(c1,c0)≠(0,0)` in `R^2`; those non-unimodular pairs are still killed by the domain argument below.

**On `D(k60_1)`.** `e28z=(3/4)c1 k60_1=0` with `k60_1` a unit forces `c1=0` in any Q-algebra (and, clearing the denominator, in any char-0 domain). `g30_4=(3/16)(2 c0^2-p c1^2)` is an unrestricted identity, so it holds on this open; with `c1=0` it forces `c0^2=0`. The test uses the subideal `(c1 k61, 2 c0^2-p c1^2)` of the full source, which can only be smaller; it is already the unit ideal after contact:

```text
1 = u1 c1 + u0 c0,     c1 = 0  ⇒  1 = u0 c0,
c0 = u0 c0^2 = 0,      hence 1 = 0.
```

No radical. Over a char-0 DVR, `c0^2=0` in a domain forces `c0=0`, contradicting `(c1,c0)≠(0,0)` even without Bezout.

**On `V(k60_1)`.** The compact ideal contains `c1 c0` and `q=2 c0^2-p c1^2`. On `D(p)`,

```text
2 c0^3 = c0·q + p c1·(c1 c0),
p c1^3 = 2 c0·(c1 c0) - c1·q,
```

so `c0^3` and `c1^3` lie in the ideal (2 and `p` are units over Q on `D(p)`). Then

```text
(u1 c1+u0 c0)^3 = u1^3 c1^3 + 3 u1^2 u0 c1^2 c0
                + 3 u1 u0^2 c1 c0^2 + u0^3 c0^3
```

vanishes, because `c1^2 c0=c1(c1 c0)` and `c1 c0^2=(c1 c0)c0`. Contact says the left side is `1`. Hence `1=0`. Again a subideal of the full source, no radical.

Over a char-0 domain, `c1 c0=0` splits: `c1=0` ⇒ `q=2 c0^2=0` ⇒ `c0=0`; `c0=0` ⇒ `p c1^2=0` with `p` a unit ⇒ `c1=0`. Direct contradiction with exact order ten.

Residue-characteristic-zero extensions of Q do not change the coefficients. A DVR that is a Q-algebra necessarily has residue characteristic 0, so 2 and 3 are units and the displayed rationals lie in the DVR. Mixed-characteristic DVRs are not points of a Q-scheme; they are outside the exact-Q theorem. Residue characteristics 2 or 3 are likewise outside it (the D1 encoding already inverts 2 in `L=z^2+p/2`).

Inverting `p` and `k0` is chart localization, as claimed. Neither is used to manufacture `c1=0` on `D(k60_1)`; `p` is used on `V(k60_1)` only to pass from `q` to `c1^3`.

---

## 7. Controls

Exact-Q meta names the frozen compiled file whose SHA is `3e0617f922…565826`, matching `result.json` and `compiled.sha256`. The engine ran that file (`rc=0`, stdout SHA matches the pin, GNU time `Exit status: 0`).

`F_65521` is a separately compiled script on a second host. After characteristic tokens it is byte-identical to exact Q, so it is an independent translation/software control, not a second theorem. It would catch a characteristic-independent compiler error; it would not catch a missing monomial of coefficient divisible by 65521. The identities above are over Q, with small 2-power denominators, and are derived from frozen tails rather than from that lane.

Chebyshev/Pell: `Q=z^4-1`, `P=16 Q^2+20 Q+5`, `A=16 z^{10}-20 z^6+5 z^2`. In `v=z^4`, `P=16 v^2-12 v+1` and `A=z^2(16 v^2-20 v+5)`, and

```text
v(16 v^2-20 v+5)^2 - (v-1)(16 v^2-12 v+1)^2 = 1.
```

The identity is nonempty (e.g. this polynomial solution). The client does not encode a blanket square-forcing assertion.

---

## 8. Composition and scope

Grade 27, independently from the same tails: unique row-1 monomial `(3/4)a1 k6` against `a1_C=sigma^{15} c1` and `Lambda^6=sigma^{12}` gives `g27_1=(3/4)c1 k60`; unique row-2 monomial `(3/4)a0 k6` gives `g27_2=(3/4)c0 k60`. On `D(k60)` both coefficients of `C_0` vanish, contradicting exact order ten. That is the charged `D(k60)` RESULT, rederived here, and it is the content of the on-disk CONFIRMED review.

`D(k60)∪V(k60)` exhausts the chart after inverting `p*k0`. Both pieces are empty. Therefore there is no point of

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9
```

on `D(p*k0)` in characteristic zero at which the seven literal-Faber source rows vanish.

Firewall, unchanged: this is only the fixed `a=9` contact on `D(p*k0)` after the cited upstream square/D1 gates and only for these seven rows. It does not cover contact-raising arcs (`a>=10`), `p=0`, `k0=0`, other D1 cells, the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

---

## Compact audit trail

Recomputed identities used as certificates:

```text
e28z = (3/4) c1 k60_1
e28c = (3/4) c0 k60_1 - mu20
e29z = (3/4)(a0 c1+a1 c0+c1_1 k60_1+c1 k60_2)
e29c = -(3/8)p a1 c1+(3/4)a0 c0+(3/4)c0_1 k60_1+(3/4)c0 k60_2-mu20_1
g30_3+(p/4)G_1+(ell1/2)e29z = (3/4) c1 c0
g30_4 = (3/16)(2 c0^2-p c1^2)
g30_5 = -(p^2/32)G_1-(p ell1/8)e29z-(3/16)p c1 c0
g30_6 = 0
g30_7 = -(p^3/128)G_1-(3 p^2 ell1/64)e29z-(3/128)p^2 c1 c0
c1 c0 = (4/3)(G_3+(p/4)G_1+(ell1/2)e29z)
2 c0^2-p c1^2 = (16/3) g30_4
2 c0^3 = c0·q + p c1·(c1 c0)
p c1^3 = 2 c0·(c1 c0) - c1·q
```

Exact hashes: endpoint RESULT `bbb1d718…d7cf1c`, EVIDENCE `dc223883…396f52`, FREEZE `6881229b…ba3570`; exact-Q compiled `3e0617f9…565826`; exact-Q stdout `d516013b…5c35cfc`; `D(k60)` RESULT `3679d0db…412a88`; on-disk grade-27 review `95e9990b2acbaaf0…b0b9fd`; V3 census RESULT `88609fdf…129e24`; collision V2 RESULT `eb1b77e1…9e9f47`; tails `d72f774c…13848`.

CONFIRMED
