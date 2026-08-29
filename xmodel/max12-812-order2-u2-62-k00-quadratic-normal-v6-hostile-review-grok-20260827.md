# Hostile different-model review — K00 quadratic coefficient-normal identities (v6)

**Substitution / low-degree census: CONFIRMED**

**Quadratic identities for `Q5,Q6,Q7`: CONFIRMED**

**Strategic scope (pure `Lambda=0` coefficient slice; no closure-first saturation): CONFIRMED**

| Field | Value |
|---|---|
| Claim under review | Frozen seven ordinary tails, after the K00 transverse substitution `c=C6`, `d0=256*C0-c^4`, `d1=C1`, `d2=16*C2-c^3`, `d3=C3`, `d4=8*C4-3*c^2`, `d5=C5` and after setting the three scaled load arguments to zero, have vanishing constant and linear parts in `(d0,...,d5)`; quadratic term counts `8,11,9,12,8,0,6`; and `Q5=-(3*c^2/128)*Q1-(c/8)*Q3`, `Q6=0`, `Q7=-(c^3/512)*Q1-(c^2/128)*Q3` coefficientwise over `Q[c,d0,...,d5]`. Quadratic `Phi7` is therefore not a new class modulo odd rows `1` and `3`. Higher coefficient-normal order and mixed `Lambda`/load terms remain open. |
| Overall verdict | **CONFIRMED** at the stated quadratic-slice scope |
| Substitution / census | **CONFIRMED** |
| Identities | **CONFIRMED** |
| Strategic scope | **CONFIRMED** |
| Smallest correction | none that breaks a numbered claim. Non-blocking: the replay JSON `scope` string writes `Lambda=k6=k2=0` while the code (correctly) also drops every `k10` monomial; the producer note already lists mixed `Lambda^2*k10` as excluded. Optional payload wording: `Lambda=k10=k6=k2=0` of the unsaturated tails, equivalently the three scaled load arguments of `r_l` set to zero. |
| Eligible for `AUDIT.md` promotion | **yes**, at exactly the quadratic pure-coefficient identity and the stated firewall. This review does not edit `AUDIT.md`. |
| Evidence tier | independent SHA-256 of producer, replay, and frozen `tails.json`; unmodified producer replay; independent binomial affine expansion in `(d0,...,d5)` with `Fraction` arithmetic, not the producer powering loop; full untruncated expansion as a second path; monomialwise coefficient check of (1); eight random `Q`-points; weight/load inventory of the frozen tails. No CAS, no AWS, no network, no `jc2-lean`, no canonical-ledger edit |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (Sol coordinator lane) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Review window (UTC) | 2026-08-27T08:30:56Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, `math.comb`, `hashlib`, `json`) |

Producer and replay reread in full before any verdict. Frozen tails parsed independently of the producer AST. `jc2-lean` was not entered, read, built, status-inspected, or modified. No other campaign artifact was written.

---

## Promotion

**Accept `PASS-K00-PURE-COEFFICIENT-QUADRATIC-NORMAL-V6` at the stated scope.**

On the frozen seven ordinary tails, in the coordinates of §1 below, after substituting the three scaled load arguments of

```text
r_l(C, Lambda^2*k10, Lambda^6*k6, Lambda^10*k2)
```

to zero (the unsaturated `Lambda=0` coefficient slice), every tail has vanishing constant and linear parts in `(d0,...,d5)`. The quadratic parts `Q_l` have monomial counts

```text
8, 11, 9, 12, 8, 0, 6
```

in `Q[c][d0,...,d5]`, and the three identities

```text
Q5 = -(3*c^2/128)*Q1 - (c/8)*Q3,
Q6 = 0,
Q7 = -(c^3/512)*Q1 - (c^2/128)*Q3
```

hold coefficientwise. In particular `Q1` and `Q3` are linearly independent over `Q(c)`, and `Q5,Q7` lie in the `Q[c]`-span of `{Q1,Q3}`. Quadratic `Phi7` on this slice is `Q7` (the target `-Lambda^19*Jdet/4` vanishes at `Lambda=0`) and is not a new class after odd rows `1` and `3`.

**Do not promote this to:** a closure-first saturation `I:Lambda^infinity:Jdet^infinity`; emptiness or nonempty of a K00 arc; a cubic-or-higher coefficient-normal identity; a mixed `Lambda^2*k10` / `Lambda^6*k6` / `Lambda^10*k2` calculation; a receiver, Gate-T, order-two, maximum-twelve, or JC2 decision.

The same linear combinations **fail** at d-degree `>=3`. The qualifier “quadratic” is load-bearing.

---

## Quarantine

No result here proves or disproves JC2, existence of a K00 source arc, or emptiness of the closure-first incidence

```text
H_K00 = (I:Lambda^infinity:Jdet^infinity) + (Lambda) + M_K00
        colon (C6*k10*Jdet)^infinity.
```

Restriction-first vanishing of the literal section (`d_i=0`) is a different operation, already recorded elsewhere as `Phi7|K00 = -Lambda^19*Jdet/4`. The present identities do not re-prove that unit, and they do not commute with saturation. Producer string `PASS-K00-PURE-COEFFICIENT-QUADRATIC-NORMAL-V6` was not used as evidence: the tails were re-expanded.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Producer SHA-256 `d7849d1a…eea3`, replay SHA-256 `5e2f100d…8835`, frozen `tails.json` SHA-256 `d72f774c…3848` match the launch prompt and the replay pin | **CONFIRMED** | any byte mismatch |
| 2 | Monomials are 10-tuples `(C0,...,C6,k10,k6,k2)` of weight `12+l`, affine-linear in the three loads | **CONFIRMED** | a tenth coordinate that is not a load; a load exponent outside `{0,1}`; a weight failure |
| 3 | K00 generators `d0=256*C0-c^4`, `d2=16*C2-c^3`, `d4=8*C4-3*c^2`, `d1=C1`, `d3=C3`, `d5=C5` are the coefficient part of the registered common-quartic/load core, inverted by the replay substitutions | **CONFIRMED** | a different even relation (e.g. `8*C4-C6^2`); `C6` identified with `p` rather than `2p` |
| 4 | All seven load-free expansions have zero constant and linear parts in `(d0,...,d5)` | **CONFIRMED** | a surviving `c`-only term, or a surviving linear form in any `d_i` |
| 5 | Quadratic monomial counts `8,11,9,12,8,0,6`; each count equals the number of distinct `d`-monomials (one `c`-power per `d`-pair) | **CONFIRMED** | a merge/cancellation changing a count; `Q6` a nonzero quadratic |
| 6 | Identities (1) hold coefficientwise over `Q[c,d0,...,d5]`; equivalently the producer residuals are the zero polynomial | **CONFIRMED** | any nonzero residual monomial |
| 7 | `Q1,Q3` are independent over `Q(c)`; `Q7` (and also `Q5`) lie in their `Q[c]`-span | **CONFIRMED** | a `Q(c)`-relation `Q3=f*Q1`; a residual of `Q7+(c^3/512)Q1+(c^2/128)Q3` |
| 8 | Load-zero is the unsaturated `Lambda=0` coefficient slice, not `I:Lambda^infinity` and not a full normal cone | **CONFIRMED** | mixed weight-`2` `k10` terms retained; a saturation colon in the replay |
| 9 | Quadratic `Phi7` gives no new class modulo rows `1` and `3`; cubic+ and mixed loads remain open | **CONFIRMED** | the degree-`2` syzygy surviving at degree `3`; the producer claiming a K00 decision |
| 10 | Unmodified replay exits `0` with `PASS-K00-PURE-COEFFICIENT-QUADRATIC-NORMAL-V6` | **CONFIRMED** | replay `RuntimeError` or a census/residual failure |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## 0. Custody

Independently recomputed this session.

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/max12-812-order2-u2-62-k00-quadratic-normal-v6-sol-20260827.md` | `d7849d1af5dbb8f9e11db6563759a87c1e3a689cc51f15c9f7affc9257efeea3` | launch prompt |
| `cases/max12_812_order2_u2_62_k00_quadratic_normal_v6_20260827/replay_k00_quadratic_normal_v6.py` | `5e2f100de529cb3980fd9db08e74adae89cfcc60f5377d7c60bc67f6ed798835` | launch prompt |
| `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | producer replay pin |

The one-parameter compiler in this repository already pins the same `tails.json` digest and the same ten-name order `(C0,...,C6,k10,k6,k2)` with load-`Lambda` weights `(2,6,10)`. That file was used only as a coordinate dictionary, not as a substitute for re-expanding the tails.

Registered command, rerun unmodified:

```text
python3 cases/max12_812_order2_u2_62_k00_quadratic_normal_v6_20260827/replay_k00_quadratic_normal_v6.py
```

Exit `0`. Payload status `PASS-K00-PURE-COEFFICIENT-QUADRATIC-NORMAL-V6`. Low-degree census and the three displayed relations match the producer note. Quadratic SHA-256 values are recorded in §2; the independent expansion reproduced all seven.

---

## 1. Substitution and census

### 1.1 Frozen tails

Keys `{1,...,7}`. Every monomial is a length-`10` exponent vector of weight `12+l` against `(8,7,6,5,4,3,2,2,6,10)`. Every load triple is in `{0,1}^3` with at most one `1`. Independent support:

| row | total | pure `C` | `k10` | `k6` | `k2` | `C6`-only | max `C0..C5` deg |
|---|---|---|---|---|---|---|---|
| 1 | 36 | 19 | 12 | 4 | 1 | 0 | 4 |
| 2 | 54 | 27 | 18 | 7 | 2 | 1 | 4 |
| 3 | 58 | 30 | 19 | 7 | 2 | 0 | 5 |
| 4 | 81 | 40 | 27 | 10 | 4 | 1 | 5 |
| 5 | 89 | 44 | 30 | 11 | 4 | 0 | 5 |
| 6 | 120 | 57 | 40 | 16 | 7 | 1 | 6 |
| 7 | 131 | 63 | 44 | 17 | 7 | 0 | 6 |

Lambda-load weights of all terms are only `{0,2,6,10}`, as required by affinity in one of `k10,k6,k2`. The unsaturated substitution `Lambda=0` therefore drops every mixed term and retains only the `Lambda`-weight `0` column. A closure-first colon by `Lambda` would keep the weight-`2` `k10` column as the leading mixed boundary; that column is not present in this calculation.

Even rows each contain exactly one pure `C6` monomial (weight parity). Odd rows contain none. Those even constants in `c` cancel against the K00 core values of `C0,C2,C4` after substitution; that cancellation is part of the constant census and is not visible before the change of coordinates.

### 1.2 K00 coordinates

The registered coefficient core (leaving `C6` and the Jacobian free) is

```text
C1 = C3 = C5 = 0,
8*C4 - 3*C6^2 = 0,
16*C2 - C6^3 = 0,
256*C0 - C6^4 = 0.
```

This is the even-coefficient part of `F = (z^2 - rho^2)^4` with `C6 = -4*rho^2 = 2p`. The producer names those six generators `d0,...,d5` with `c=C6`. The inverse

```text
C0 = (c^4 + d0)/256,   C1 = d1,   C2 = (c^3 + d2)/16,
C3 = d3,               C4 = (3*c^2 + d4)/8,   C5 = d5,   C6 = c
```

is an affine automorphism of `A^7`, so it is a valid transverse chart around the K00 coefficient ray. It is not a saturation, not a blowup chart, and not a mixed-load coordinate.

### 1.3 Independent expansion

Each `C_i` is affine in a single `d_i` (or is `c`). The independent check expands `(core(c) + transverse(d))^n` by the binomial theorem, truncated at d-degree `2` for the quadratic slice, and also expands untruncated. Both paths use `Fraction` dictionaries keyed by `(d0,...,d5,c)` exponents. Load monomials are killed by substituting `k10=k6=k2=0`, not by sharing the producer `continue` on a slice of a 10-tuple.

Constant and linear parts: empty for every `l=1,...,7` on both paths. Directional one-hot evaluation of the full expansion in each `d_i` likewise finds no linear form.

Quadratic monomial counts, both paths: `8,11,9,12,8,0,6`. Full untruncated census (d-degree of remaining terms):

| row | deg 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 1 | 8 | 7 | 1 | 0 | 0 |
| 2 | 11 | 9 | 3 | 0 | 0 |
| 3 | 9 | 13 | 4 | 1 | 0 |
| 4 | 12 | 15 | 8 | 1 | 0 |
| 5 | 8 | 19 | 10 | 3 | 0 |
| 6 | 0 | 21 | 16 | 4 | 1 |
| 7 | 6 | 23 | 19 | 8 | 1 |

`Q6=0` is only the quadratic statement. Row 6 has 21 cubic terms. A reader who inferred that `r6` vanishes identically after the K00 substitution would be wrong; the producer does not make that inference.

---

## 2. Identities

Producer residuals, rewritten without the replay helpers:

```text
Q5 + (3*c^2/128)*Q1 + (c/8)*Q3  = 0,
Q6                               = 0,
Q7 + (c^3/512)*Q1 + (c^2/128)*Q3 = 0
```

in `Q[c,d0,...,d5]`. Independent binomial expansion: all three residuals are the empty dictionary. Untruncated quadratic parts: the same. Direct subtraction `Q5 - (-(3*c^2/128)Q1 - (c/8)Q3)` and the analogous `Q7` difference: empty. Eight random points in `Q^7` (seed `20260827`): identities hold on the quadratic parts.

Independent quadratic SHA-256, using the producer encoding of sorted `(exponents_d0_d5_c, [num,den])` JSON, match the replay payload:

| `Q_l` | SHA-256 |
|---|---|
| 1 | `f55356d72c1f42be2898e7f7c90e813b736d685b5bcbdeff64aa5585c7f8d351` |
| 2 | `39b6cc1b6b82da79a3acd728b4314330ee6c50c2874d21e5bd53d7dd226d198d` |
| 3 | `fdaa48b23e9d5b9396521e1d01cf75bdd4f727f5113c859f8561e2b26d50df74` |
| 4 | `b4f0128636ae68dd7a3a36400f89b8c74782336ec30bca6e38cf2f2065b0ccbe` |
| 5 | `025f9c14250ffc479d467532c48206902542699b90c578fe29b8c60a8d6184af` |
| 6 | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |
| 7 | `2580b1180e8fd2be90e85346c381b1c3d1681e468cf95479b1ce86c134c02a84` |

The empty-polynomial hash is `sha256(b'[]')`, as required for `Q6`.

Explicit odd quadratic parts (independent expansion):

```text
Q1 =
  (3/64)*d1*d2 + (3/1024)*d0*d3
  - (3/64)*d1*d4*c - (3/128)*d2*d3*c - (3/2048)*d0*d5*c
  + (9/512)*d3*d4*c^2 + (9/1024)*d2*d5*c^2
  - (3/512)*d4*d5*c^3

Q3 =
  (3/1024)*d0*d1
  - (9/512)*d1*d2*c - (9/8192)*d0*d3*c
  + (3/256)*d1*d4*c^2 + (3/512)*d2*d3*c^2 + (3/8192)*d0*d5*c^2
  - (15/4096)*d3*d4*c^3 - (15/8192)*d2*d5*c^3
  + (9/8192)*d4*d5*c^4

Q5 =
  - (3/8192)*d0*d1*c
  + (9/8192)*d1*d2*c^2 + (9/131072)*d0*d3*c^2
  - (3/8192)*d1*d4*c^3 - (3/16384)*d2*d3*c^3 - (3/262144)*d0*d5*c^3
  + (3/65536)*d3*d4*c^4 + (3/131072)*d2*d5*c^4

Q6 = 0

Q7 =
  - (3/131072)*d0*d1*c^2
  + (3/65536)*d1*d2*c^3 + (3/1048576)*d0*d3*c^3
  - (3/524288)*d3*d4*c^5 - (3/1048576)*d2*d5*c^5
  + (3/1048576)*d4*d5*c^6
```

`Q3` has the extra `d`-monomial `d0*d1` that `Q1` does not. Coefficient ratios `Q1/Q3` on the eight shared `d`-pairs are not a single element of `Q(c)` (e.g. `d4 d5` gives `-16/(3c)`, `d3 d4` gives `-24/(5c)`). So `{Q1,Q3}` is free of rank two over `Q(c)`.

Direct coefficient checks of (1), three monomials:

- `d1 d2`: `Q1=3/64`, `Q3=-(9/512)c`, `Q5=(9/8192)c^2`, `Q7=(3/65536)c^3`. Then `-(3c^2/128)(3/64)-(c/8)(-(9/512)c)=(9/8192)c^2` and `-(c^3/512)(3/64)-(c^2/128)(-(9/512)c)=(3/65536)c^3`.
- `d0 d1` (absent from `Q1`): `Q3=3/1024`, `Q5=-(3/8192)c`, `Q7=-(3/131072)c^2`. Then `-(c/8)(3/1024)=-(3/8192)c` and `-(c^2/128)(3/1024)=-(3/131072)c^2`.
- `d4 d5`: `Q1=-(3/512)c^3`, `Q3=(9/8192)c^4`, `Q5=0`, `Q7=(3/1048576)c^6`. The `Q5` combination cancels; the `Q7` combination is `(3/1048576)c^6`.

The same `Q5`/`Q7` combinations at d-degree `3,4,5,6` of the full expansion have residual term counts `(19,10,3,0)` and `(23,19,8,1)` respectively, and `Q6` is nonzero in those degrees. Quadratic is sharp.

---

## 3. Strategic scope

On the ordinary source

```text
Phi_l = r_l(C, Lambda^2*k10, Lambda^6*k6, Lambda^10*k2)
        - Lambda^(12+l) * delta_l,
```

with `(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,Jdet/4)`, the unsaturated slice `Lambda=0` is exactly `r_l(C,0,0,0)`. Targets vanish. All three scaled load arguments vanish, including the leading load `k10`. The replay implements that slice. It does not compute a colon, does not invert `Jdet` or `C6`, and does not saturate by the irrelevant coefficient origin.

Consequence, no more and no less:

1. Restriction-first evaluation at the core `d_i=0` makes every `Q_l` vanish because each `Q_l` is homogeneous of d-degree `2`. That is why a literal K00 section can be killed by `Phi7` (the leftover target `-Lambda^19*Jdet/4`) without this calculation, and why that kill is not a transverse statement.
2. Off the core, still at d-degree `2` and still at `Lambda=0`, `Q7` is in the `Q[c]`-span of `{Q1,Q3}`. A closure-first separator that uses only quadratic `Phi7` after imposing odd rows `1` and `3` has nothing left. Row `5` is likewise not a new quadratic class; the producer correctly emphasises the terminal row.
3. The next honest obstruction on this coefficient-normal slice is cubic or higher in `(d0,...,d5)`, or a mixed load term of `Lambda`-weight `2,6,10`. Both remain open. The three identities are exact syzygies that a later jet compiler may remove before elimination; they are not that compiler.

The replay JSON `scope` string `Lambda=k6=k2=0` is slightly thinner than the code and than the producer firewall (which lists mixed `Lambda^2*k10`). It does not change the algebra: `k10` monomials are dropped. The producer title word “closure” is a topic label; the status line and the firewall refuse a K00 decision. No correction of the lemma is required.

---

## 4. Attacks refused

- Treating the replay as a saturation of `I` by `Lambda` or `Jdet`. The code has no colon.
- Treating `Q6=0` as vanishing of `r6`. Degree `>=3` survives.
- Treating `{Q1,Q3}` as rank one. The `d0 d1` term of `Q3` and the inconsistent `Q1/Q3` ratios forbid it.
- Treating the identities as holding in all d-degrees. Residuals at degree `3` are already large.
- Treating term counts as `C0..C5`-degree counts before substitution. Those counts are `8,11,9,12,9,11,9` at C-degree `2` among pure terms; after the K00 chart they become `8,11,9,12,8,0,6` by core/transverse mixing and cancellation. Full expansion is necessary.
- Inflating the lemma to a K00 arc, a receiver emptiness, Gate T, order two, maximum twelve, or JC2.

---

## Firewall

This is the pure coefficient-normal quadratic slice of the frozen seven ordinary tails at unsaturated `Lambda=0`. It does not include mixed `Lambda^2*k10`, `Lambda^6*k6`, or `Lambda^10*k2` terms, does not compute `I:Lambda^infinity:Jdet^infinity`, and proves neither existence nor nonexistence of a K00 arc. It does not close the receiver, Gate T, order two, maximum twelve, or JC2.
