# Hostile review — V82QSF nested CURRENT-denominator factor identities

| Field | Value |
|---|---|
| Targets | V82QSF `REPORT.md`, `MANIFEST.sha256`, `FREEZE.sha256`, `PREREGISTRATION.md`; V82QSD `REPORT.md`, `MANIFEST.sha256` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim; the radical slogan names only the `x`-support |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer verdict text, `PASS` strings, flint sentinels, and good-prime/control interpretation are not evidence |
| Method | SHA-256 of every named pin and every manifest row; hand expansion in `Q[C,V,U]` and on `D(U)` from the displayed polynomials. No Singular, Sage, msolve, Lean, package compiler, python-flint, or other CAS |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of all six required primary pins match. Every path named in V82QSF `MANIFEST.sha256` (24 rows) and V82QSF `FREEZE.sha256` (1 row) rehashes to the printed digest. Every path named in V82QSD `MANIFEST.sha256` (142 rows) rehashes to the printed digest. The two V82QSF AWS hosts are distinct. Producer `TD6 V82QSF NESTED DENOMINATOR IDENTITY PASS`, the flint equality flags, and the printed expression digests were not used as algebra. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

The literal V82QSD polynomials `F,G,L` in `Q[C,V,U]`, with `F=C U-V^2+U^3`, satisfy the polynomial identities

```text
G = V^4 + 4 F^2,
L = 4 U^3 G^2 + V^4 (V^2+4U^3) (V^2+2F)^2.
```

On `D(U)`, writing `x=V^2/U^3`, `s=F/U^3`, `g=x^2+4s^2`, and `a=x+2s`, one has

```text
L/U^15
  = 64 s^4 + 4 x^2 (x+12) s^2 + 4 x^3 (x+4) s + x^4 (x+8)
  = 4 g^2 + x^2 (x+4) a^2.
```

The five stated divisor consequences hold with the hypotheses already written (characteristic zero, set-theoretic collapse of `G=A=0`, localization `D(U)` for the `(x,s)` chart, congruence on `F=0` and on `G=0`). The radical of `(g, L/U^15)` in `Q[x,s]` is covered by `x=0` or `x=-4`, and the covering does not drop `s`:

```text
rad(g, L/U^15) = (x, s) ∩ (x+4, s^2+4)
```

in characteristic not two. Geometrically that is the reduced point `(x,s)=(0,0)` together with the quadratic zero-cycle `x=-4`, `s^2=-4`. The slogan `x=0_or_x=-4` is only the `x`-support of this radical. It does not licence treating the lines `x=0` or `x=-4` as components, nor treating `V(L)` as those two branches, nor treating the identities as a CURRENT coefficient, source-fibre, covering, rank, Kuranishi, TD6, or JC2 theorem.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Six primary pins | hashes | all six match the required bytes |
| 1. V82QSF manifests | every named file | `MANIFEST.sha256` 24/24, `FREEZE.sha256` 1/1 |
| 1. V82QSD manifest | every named file | `MANIFEST.sha256` 142/142 |
| 1. Dual V82QSF AWS | hosts, tags, pid, rc, stdout | distinct Box03 / r6d; `rc=0`; stdout differ only in the registered run tag |
| 1. V82QSF vs V82QSD | archives, stamps | distinct executions; distinct source archives |
| 2. Literal `G` | `G = V^4+4F^2` | polynomial identity in `Q[C,V,U]` |
| 2. Literal `L` | nested right-hand side | polynomial identity in `Q[C,V,U]`; every monomial of the displayed `L` recovered |
| 2. `D(U)` normalisation | `L/U^15` | both displayed formulae equal `4g^2+x^2(x+4)a^2` |
| 3. On `F=0` | `L=V^8(V^2+8U^3)` | congruence modulo the prime `(F)`; holds at `U=0` as well |
| 3. On `G=0` | `L=V^4(V^2+4U^3)A^2` | congruence modulo `(G^2)`, hence on `V(G)` |
| 3. Collapse | `G-A^2+2 A V^2=2V^4` | polynomial identity; `G=A=0` forces `V=F=0` set-theoretically in characteristic zero |
| 4. Radical on `D(U)` | covered by `x=0` or `x=-4` | `x(x+4)` lies in the radical; exact support is `(0,0)` and `V(x+4,s^2+4)` |
| 4. Nontrivial `s` | slogan suppression | `s=0` on `x=0`; `s^2=-4` on `x=-4`; quadratic extension `Q(i)`; not dropped by `g=0` |
| 4. Intersections | `F=0` vs `G=0` leftover | on `F=0`, leftover `V^2+8U^3`; on `G=0`, leftover `V^2+4U^3`; `A`-branch collapses onto `V=F=0` |
| 5. Scope | coefficient / fibre / TD6 / JC2 | firewall holds; identities are denominator-divisor algebra only |

---

## 1. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `cases/td6_current_denominator_nested_identity_v82qsf_aws_20260826/REPORT.md` | `ef88290d0957519cfd1dbb64389836a1c6bb5d1cdbe8228010dac1837339dee9` | V82QSF endpoint |
| `.../td6_current_denominator_nested_identity_v82qsf_aws_20260826/MANIFEST.sha256` | `1c2a10703496cb066173d2958942e6768d2403e5f691023e066482da42073e65` | V82QSF evidence manifest |
| `.../td6_current_denominator_nested_identity_v82qsf_aws_20260826/FREEZE.sha256` | `a5dabcd1a251f4d5cd504b79ca2a9eff737405833426590c1a6b3a1931c0fc49` | V82QSF freeze (pins the manifest) |
| `.../td6_current_denominator_nested_identity_v82qsf_aws_20260826/PREREGISTRATION.md` | `59ea9c0762eef4c3d3dbe3fdc200ec4db95bea8f9eb9e5e73cf4e764612e15e9` | V82QSF preregistration |
| `cases/td6_c1_c2_c3_all_q_current_denominator_diagnostic_v82qsd_aws_20260826/REPORT.md` | `764ec76b61f0fdbdc6392cbab73b70fdf3abda63264455745e06d00fd6a3a283` | V82QSD endpoint (source of `G,L`) |
| `.../td6_c1_c2_c3_all_q_current_denominator_diagnostic_v82qsd_aws_20260826/MANIFEST.sha256` | `cdafda8a70ae814083378e0fd9e6be7733fe3843ef1950a2f9a4d2710b356ac4` | V82QSD evidence manifest |

Git HEAD is `418e413593120d19e15e6546eb50c985f4b1f038`, matching the requested basis. Both case directories are untracked relative to that commit. Custody is the pinned bytes on disk, not git objects of `418e413`.

V82QSF `FREEZE.sha256` contains the single row `MANIFEST.sha256` with digest equal to the primary pin. V82QSD `FREEZE.sha256` likewise pins its `MANIFEST.sha256` to `cdafda8a70ae814083378e0fd9e6be7733fe3843ef1950a2f9a4d2710b356ac4`. A passing manifest is not mathematics.

The V82QSF source archive `source/source.tar.gz` hashes to `ef0c0969e5fd1a8260ed8c1ed1f652fa958eb9c47e6e1317a0ef0d5d4191a2a0`. Its members `replay_v82qsf.py`, `run_v82qsf.sh`, and `launch_v82qsf_host.sh` rehash to the three rows of `source/SOURCE.sha256` and to the corresponding disk files. The replay was read as a display of the claimed identities; it was not executed.

---

## 2. Distinct registered AWS executions

V82QSF ran two hosts under a 1 GiB cap and a 600-second timeout.

| | Box03 | r6d |
|---|---|---|
| hostname | `ip-172-30-0-249` | `ip-172-30-0-45` |
| `AWS_RUN_TAG` | `td6_v82qsf_nested_box03_20260826T083035Z` | `td6_v82qsf_nested_r6d_20260826T083035Z` |
| PID | `186724` | `251961` |
| `rc` | `0` | `0` |
| start/finish UTC | `2026-08-26T08:30:47Z` | `2026-08-26T08:30:47Z` |
| peak RSS (KiB) | `30440` | `29520` |
| stdout SHA-256 | `646156c5766564c3ebe8164a879afd917b28be2da73612124b3191bcfb47f438` | `4554f0d7153b59bbb685eb574aa65f1ed98ca6def7a26132a826f121ddd453f7` |

Hostnames, tags, PIDs, RSS, stderr, and stdout hashes all differ. After deleting the single provenance line `aws_run_tag=...`, the two stdout streams are byte-identical with SHA-256 `d5f931fbe55a645bcffe43670ba615755380558b96f00b387802fd55fc21623f`, matching the common digest recorded in V82QSF `AWS_LAUNCH.md`. Both `evidence/*/RESULTS.sha256` rows rehash to the on-disk `stdout`, `stderr`, and `rc`. Both `wrapper.log` files are empty (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`). The two V82QSF executions are distinct.

V82QSD is a different registered package: source archive `86bf989c2ac8b4e263b1f2de19004e32098cd0df10e225828f3f448b7b3b6757`, start `2026-08-26T07:34:59Z`, 2 GiB / 7200-second lanes, exponents `2..6` on Box03 and `7..10` on r6d. It is not a replay of V82QSF. This review takes from V82QSD only the displayed polynomials `F,G,L`. It does not accept V82QSD rank, kernel-dimension, or `denominator_radical_subset_U_H_B3` language as a theorem.

---

## 3. Literal V82QSD polynomials

All nine V82QSD `CURRENT_DENOMINATOR_DIAGNOSTIC.txt` files, and V82QSD `REPORT.md`, display the same three foreign factors. The V82QSF replay writes the same polynomials (Python `**` versus diagnostic `^`). After that spelling change the strings are identical:

```text
F = C*U - V^2 + U^3

G = 4*C^2*U^2 - 8*C*V^2*U + 8*C*U^4
    + 5*V^4 - 8*V^2*U^3 + 4*U^6

L = 64*C^4*U^7 - 256*C^3*V^2*U^6 + 256*C^3*U^9
    + 4*C^2*V^6*U^2 + 432*C^2*V^4*U^5
    - 768*C^2*V^2*U^8 + 384*C^2*U^11
    - 4*C*V^8*U - 328*C*V^6*U^4 + 864*C*V^4*U^7
    - 768*C*V^2*U^10 + 256*C*U^13 + V^10
    + 100*V^8*U^3 - 332*V^6*U^6 + 432*V^4*U^9
    - 256*V^2*U^12 + 64*U^15.
```

The only variation across q2..q10 is the pair of units `(U^a, V^b)` in the prefactor `(1/256) F G L U^a V^b`. This review does not re-factor the expanded `denominator_exact` polynomial and does not certify that `F,G,L` divide it. It treats the displayed `G,L` as the objects of the nested-identity claims.

Write `A := V^2+2F` throughout.

---

## 4. Identity `G = V^4 + 4 F^2`

Expand `F^2` in `Q[C,V,U]`:

```text
F = C U - V^2 + U^3,
F^2 = C^2 U^2 + V^4 + U^6 - 2 C V^2 U + 2 C U^4 - 2 V^2 U^3,
4 F^2 = 4 C^2 U^2 + 4 V^4 + 4 U^6 - 8 C V^2 U + 8 C U^4 - 8 V^2 U^3.
```

Adding `V^4` yields

```text
V^4 + 4 F^2
  = 4 C^2 U^2 - 8 C V^2 U + 8 C U^4 + 5 V^4 - 8 V^2 U^3 + 4 U^6,
```

which is the displayed `G`. This is an identity of polynomials, not a statement on `D(U)` or in characteristic `p`.

---

## 5. Nested identity for `L`

Substitute `G = V^4+4F^2` and `A = V^2+2F` into the claimed right-hand side and expand in `F,V,U` first:

```text
G^2 = V^8 + 8 V^4 F^2 + 16 F^4,
4 U^3 G^2 = 4 U^3 V^8 + 32 U^3 V^4 F^2 + 64 U^3 F^4,
A^2 = V^4 + 4 V^2 F + 4 F^2,
V^4 (V^2+4U^3) A^2
  = V^{10} + 4 V^8 F + 4 V^6 F^2 + 4 U^3 V^8 + 16 U^3 V^6 F + 16 U^3 V^4 F^2.
```

Summing and collecting gives the intermediate form

```text
RHS = V^{10} + 4 V^8 F + 4 V^6 F^2 + 8 U^3 V^8
      + 16 U^3 V^6 F + 48 U^3 V^4 F^2 + 64 U^3 F^4.
```

Now put `F = C U + P` with `P = U^3-V^2`, so

```text
P^2 = U^6 - 2 U^3 V^2 + V^4,
P^3 = U^9 - 3 U^6 V^2 + 3 U^3 V^4 - V^6,
P^4 = U^{12} - 4 U^9 V^2 + 6 U^6 V^4 - 4 U^3 V^6 + V^8,
```

and expand by powers of `C`.

- `C^4`: `64 U^3 · C^4 U^4 = 64 C^4 U^7`.
- `C^3`: `64 U^3 · 4 C^3 U^3 P = 256 C^3 U^6 P = 256 C^3 U^9 - 256 C^3 V^2 U^6`.
- `C^2`: `4 V^6 · C^2 U^2 + 48 U^3 V^4 · C^2 U^2 + 64 U^3 · 6 C^2 U^2 P^2` equals `4 C^2 V^6 U^2 + 432 C^2 V^4 U^5 - 768 C^2 V^2 U^8 + 384 C^2 U^{11}`.
- `C^1`: collecting `V^8 U`, `V^6 U^4`, `V^4 U^7`, `V^2 U^{10}`, `U^{13}` produces the coefficients `-4`, `-328`, `864`, `-768`, `256`.
- `C^0`: collecting `V^{10}`, `V^8 U^3`, `V^6 U^6`, `V^4 U^9`, `V^2 U^{12}`, `U^{15}` produces the coefficients `1`, `100`, `-332`, `432`, `-256`, `64`.

Every monomial and coefficient of the displayed `L` is recovered, and nothing else appears. Therefore

```text
L = 4 U^3 G^2 + V^4 (V^2+4U^3) A^2
```

in `Q[C,V,U]`. In particular `L - V^4(V^2+4U^3)A^2 = 4 U^3 G^2` lies in the ideal `(G^2)`, not merely in `(G)`.

---

## 6. Normalisation on `D(U)`

Give weights `wt(C)=4`, `wt(V)=3`, `wt(U)=2`. Then `F` is homogeneous of weight 6, `G` of weight 12, and `L` of weight 30. The quantities `x=V^2/U^3` and `s=F/U^3` are weight zero on `D(U)`, and

```text
G / U^6 = x^2 + 4 s^2 = g,          hence  4 U^3 G^2 / U^{15} = 4 g^2,
A / U^3 = x + 2 s = a,
V^4 (V^2+4U^3) A^2 / U^{15} = x^2 (x+4) a^2.
```

The nested identity of §5 therefore divides by `U^{15}` on `D(U)` to

```text
L/U^{15} = 4 g^2 + x^2 (x+4) a^2.
```

This is an identity of polynomials in `Q[x,s]` after the substitution; it is not the statement that `U^{15}` divides `L` in `Q[C,V,U]` (the term `V^{10}` of `L` is not `U^{15}`-divisible).

Expand the right-hand side independently:

```text
g^2 = x^4 + 8 x^2 s^2 + 16 s^4,
4 g^2 = 4 x^4 + 32 x^2 s^2 + 64 s^4,
(x+4)(x^2+4 x s+4 s^2) = x^3 + 4 x^2 s + 4 x s^2 + 4 x^2 + 16 x s + 16 s^2,
x^2 (x+4) a^2 = x^5 + 4 x^4 s + 4 x^3 s^2 + 4 x^4 + 16 x^3 s + 16 x^2 s^2.
```

Adding and grouping yields

```text
64 s^4 + 4 x^2 (x+12) s^2 + 4 x^3 (x+4) s + x^4 (x+8),
```

which is the displayed expanded form. Both displayed formulae for `L/U^{15}` are therefore the same element of `Q[x,s]`.

---

## 7. Consequence 1: on `F=0`, `L = V^8(V^2+8U^3)`

Set `F=0` in the nested identity. Then `G=V^4` and `A=V^2`, so

```text
L = 4 U^3 V^8 + V^4 (V^2+4U^3) V^4
  = 4 U^3 V^8 + V^8 (V^2+4U^3)
  = V^8 (V^2 + 8 U^3).
```

This is the congruence `L ≡ V^8(V^2+8U^3)` modulo `(F)`. The factor `F = C U - V^2 + U^3` is linear in `C`, hence prime in the UFD `Q[C,V,U]`, so the principal-ideal language is accurate. The equality is not an identity of polynomials in `Q[C,V,U]` without the relation `F=0`. At `U=0` the same congruence still holds: `F=-V^2`, so `F=0` forces `V=0`, and both sides of the claimed specialisation vanish. No localisation at `U` or `V` is required for this congruence.

On `D(U)` the same specialisation is `s=0`, whence `L/U^{15} = x^4(x+8)`. The leftover factors on `F=0` are therefore `V` (i.e. `x=0`) and `V^2+8U^3` (i.e. `x=-8`). The second leftover is *not* the `x=-4` branch of §10.

---

## 8. Consequence 2: on `G=0`, `L = V^4(V^2+4U^3)A^2`

Immediate from §5: the first summand of `L` is `4 U^3 G^2`. On the variety `V(G)` one has `L = V^4(V^2+4U^3)A^2`. Ideal-theoretically the difference lies in `(G^2)`, so the congruence also holds modulo `(G)`. No characteristic restriction.

---

## 9. Consequence 3: collapse of `G=A=0`

Direct expansion, no substitution:

```text
A^2 = V^4 + 4 V^2 F + 4 F^2,
2 A V^2 = 2 V^4 + 4 V^2 F,
G = V^4 + 4 F^2,
G - A^2 + 2 A V^2 = 2 V^4.
```

This is a polynomial identity in `Q[C,V,U]` (equivalently in `Q[F,V]`). Hence `2 V^4 ∈ (G,A)`. In characteristic zero, or merely characteristic not two, `V^4 ∈ (G,A)`, so set-theoretically `G=A=0` forces `V=0`; then `A=2F=0` forces `F=0`. The producer states the collapse as set-theoretic in characteristic zero, which is the correct strength: one does *not* have `(G,A)=(V,F)`. In characteristic two the identity becomes `0=0`, `G=V^4`, `A=V^2`, and `F` is free.

The same identity on `D(U)` is `g - a^2 + 2 a x = 2 x^2`. Thus `g=a=0` forces `x=0` and then `s=0` in characteristic not two.

---

## 10. Consequence 4: radical of `(g, L/U^{15})` on `D(U)`

Write `ell := L/U^{15} ∈ Q[x,s]`. From §6, `ell - 4 g^2 = x^2 (x+4) a^2` with `a=x+2s`. In the quotient by `(g)` one has `ell ≡ x^2(x+4)a^2` and, from §9, `a(x-2s) ≡ 2 x^2`. Multiplying the first congruence by `(x-2s)^2` produces

```text
4 x^6 (x+4) ∈ (g, ell)
```

in `Q[x,s]` (the coefficient 4 is a unit). Every prime containing `(g,ell)` therefore contains `x` or `x+4`, i.e.

```text
x(x+4) ∈ rad(g, ell).
```

The variety `V(g,ell)` is covered by `x=0` or `x=-4`. That is the producer claim, and it is true.

It is not the complete radical. Restricting `g=x^2+4s^2` to those two loci in characteristic not two:

| locus | `g=0` forces | reduced support in `A^2_{x,s}` | field of definition |
|---|---|---|---|
| `x=0` | `4 s^2=0`, hence `s=0` | the reduced point `(0,0)` | `Q` |
| `x=-4` | `16+4s^2=0`, hence `s^2=-4` | `V(x+4, s^2+4)`, two geometric points `(-4,±2i)` | `Q(i)` |
| `a=0` | `2 x^2=0` by §9, hence `(x,s)=(0,0)` | already the first point | `Q` |
| `x=0` and `x=-4` | empty | no intersection | — |

Consequently, in characteristic not two,

```text
rad(g, ell) = (x, s) ∩ (x+4, s^2+4)
```

in `Q[x,s]`. Both `(x,s)` and `(x+4,s^2+4)` are maximal (`Q[x,s]/(x+4,s^2+4) ≅ Q(i)`). The scheme `(g,ell)` itself is not reduced: on `x=0` one has `g=4s^2`, so `s` is nilpotent of index two in `Q[x,s]/(x,g)`.

The printed sentinel `normalized_radical_branches_on_DU=x=0_or_x=-4` names only the `x`-support. It does not compute a radical and it does not print `s`. That omission is not a false identity: the intersection still contains `g=0`, so `s` is not free on either branch. A successor that keeps `G=0` while specialising `x=0` or `x=-4` automatically restores `s=0` or `s^2=-4`. A successor that drops `g=0` and rebuilds on the lines `x=0` or `x=-4` has left the claimed intersection.

Pullback along `D(U) → A^2_{x,s}`, `(C,V,U) ↦ (V^2/U^3, F/U^3)`:

- `(x,s)=(0,0)` is `V=0`, `F=0`, hence `C=-U^2`, with `U≠0`. A rational curve.
- `x=-4`, `s^2=-4` is `V^2+4U^3=0` and `F^2+4U^6=0`. Substituting `F=C U+5 U^3` (the form of `F` on `V^2=-4U^3`) yields the `Q`-model `C^2 + 10 C U^2 + 29 U^4=0` on `D(U)`, discriminant `-16`. Two geometric sections `C=U^2(-5±2i)`. Nontrivial `s`, and a further quadratic for `V`.

The phrase “finite branches” is accurate in the `(x,s)`-plane (the intersection is zero-dimensional) and must not be read as “two reduced rational points with `s=0`”, nor as a cover of `V(L)` or of `V(G)`.

`L` is a *sum*, not a product. The identity of §5 does not put `V(L)` inside `V(G) ∪ V(V) ∪ V(V^2+4U^3) ∪ V(A)`. The residual hypersurface on which `4 U^3 G^2 = - V^4(V^2+4U^3)A^2 ≠ 0` is a genuine component of `V(L)` and is not among the two points above. V82QSD’s required rebuild on `L=0` is therefore not eliminated. The producer’s “recursive finite divisor tree” is a tree of leftover factors *after* specialising `F=0` or `G=0`, plus the intersections recorded here; it is not a claim that `V(F G L)` is a finite union of explicit complete-intersection curves.

Remaining intersections, for the record:

| intersection on `D(U)` | description |
|---|---|
| `F=G=0` | `G=V^4`, so `V=0` in char 0, then `C=-U^2`; equals `(x,s)=(0,0)` |
| `F=L=0` | `s=0` and `x^4(x+8)=0`: either `(0,0)` or `x=-8`, `s=0` (i.e. `V^2+8U^3=F=0`, and `G=64 U^6 ≠ 0`) |
| `G=L=0` | the radical of §10: `(0,0)` and `V(x+4,s^2+4)` |
| `F=G=L=0` | only `(x,s)=(0,0)` |
| `U=0` | excluded from the chart; the polynomial identities of §§4–5,9 still hold globally |

---

## 11. Consequence 5: scope

V82QSF preregistration and report both state that the package is a denominator/divisor diagnostic only. It does not source-lift a CURRENT coefficient, rebuild a raw fibre, or establish a cover, obstruction, family, rank, Kuranishi, TD6, SP-2, landing, or JC2 statement. The replay’s administrative token `no_current_coefficient_cover_family_TD6_SP2_landing_or_JC2_claim=true` is consistent with that firewall and is not itself a theorem. The run labels containing the string `TD6` are provenance, not a TD6 theorem. This review agrees: the nested identities are algebra among three displayed denominator factors. They do not decide whether any q2..q10 CURRENT coefficient survives, whether a source fibre is empty, or whether a presentation covers the source scheme.

---

## 12. What this review did not use

- Producer `PASS` / `true` flags, flint expression SHA-256 values, and the printed quotient digest `07f66e75d21e96bba1bea174c540b78817cd71736b3a814a04b5ad0ba7cd4676`.
- Execution of `replay_v82qsf.py`, python-flint, or any computer algebra system.
- V82QSD rank `1/1`, kernel dimension `0`, and the fail-closed foreign-factor assertion, except as the source of the displayed polynomials `F,G,L`.
- Any inference from good primes or from AWS `rc=0` to characteristic-zero algebra.

The algebra is the expansions of §§4–10.

TD6_CURRENT_DENOMINATOR_NESTED_IDENTITY_CONFIRMED
