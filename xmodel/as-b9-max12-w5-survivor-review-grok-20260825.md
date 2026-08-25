# Hostile different-model review — AS `B9` fixed-D12 survivor through `Z/243`

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-max12-w5-survivor-aws-20260825.md` |
| Frozen case | `cases/as_b9_max12_w5_survivor_aws_20260825/` |
| Parent case | `cases/as_b9_max12_w3_survivor_aws_20260825/` |
| Parent review | `xmodel/as-b9-max12-w3-survivor-review-grok-20260825.md`, overall **CONFIRMED** |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Custody | **CONFIRMED** of the frozen dual-AWS run (non-blocking timestamp notes below) |
| Terminology / exposition | non-blocking only |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | independent dense `Z[x,y]` arrays with binomial `(x+y^3)^n`; second Jacobian in source coordinates `(u,y)` after `x=u-y^3`; linearized operator over `Z` and over `F_3`; no import or execution of either `replay.py` |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer and both cases uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

With `u=x+y^3`, the displayed integer pair has Jacobian determinant identically `1` modulo `243` in `Z[x,y]`, after retaining every mixed binomial term of `u^3` and `u^4`. The `Z/81` parent is exactly `1+81(-u^4+2y-6u^2 y+32 y^2)`, and its divided residual modulo three is `2(u^4+y+y^2)` with the stated sign and factor. The operator `D(R,S)=R_x-u^3 R_y+S_y` is the special-fibre linearization of `P_x Q_y-P_y Q_x` after the tame source transform, and both claimed primitives hold over `F_3` and fail over `Z`. Actual total and partial-`y` degrees are `(9,12)`. The new digit lies in the fixed D12 box. Omitting it fails modulo `243`. Dual-AWS stdout is byte-identical and rebuilds the same payload digest. This is one selected branch at one finite modulus.

## Strongest exact claim

Let `u=x+y^3` in `Z[x,y]`. Starting from the frozen `Z/27` point, the `Z/81` continuation

```text
P4 = u - u^3 + 18 u y
Q4 = y + u^4 + 3 u^2 y + 72 y^2
```

satisfies the polynomial identity

```text
det J(P4,Q4) = 1 + 81(-u^4 + 2 y - 6 u^2 y + 32 y^2)
```

and is therefore determinant one modulo `81` and not modulo `243`. The divided residual modulo three is `2(u^4+y+y^2)`. Over `F_3`, with

```text
D(R,S) = R_x - u^3 R_y + S_y,
```

one has `D(2uy,y^2)=u^4+y` and `D(xy^2, x^4 y^2 + x y^{11})=y^2`, hence `D(R5,S5)≡-(det J(P4,Q4)-1)/81 (mod 3)` for the registered digit

```text
R5 = 2 u y + x y^2,     S5 = y^2 + x^4 y^2 + x y^{11}.
```

The integer pair

```text
P5 = P4 + 81 R5 = u - u^3 + 18 u y + 81(2 u y + x y^2)
Q5 = Q4 + 81 S5 = y + u^4 + 3 u^2 y + 72 y^2 + 81(y^2 + x^4 y^2 + x y^{11})
```

then satisfies `det J(P5,Q5)≡1 (mod 243)` coefficientwise in `Z[x,y]`, reduces modulo three to `G9=(u-u^3,y+u^4)`, and has actual total degrees and actual partial-`y` degrees both equal to `(9,12)`. Every monomial of `P5`, `Q5`, `R5`, and `S5` has total degree at most twelve and `y`-degree at most twelve. Omitting the whole order-`81` digit restores a determinant that is not `1` modulo `243`. This is one explicit fixed-D12 branch through `Z/243`.

## Sharpest non-claim

One selected branch, one finite modulus `243`. Not the complete D12 predecessor scheme, not a complete next-digit linear solve, not a classification of the W2 fibre or of every lift of `G9`, not an inverse limit, not a `Z_3` point, not a characteristic-zero polynomial map or collision, not a Keller counterexample, not a maximum-twelve theorem, not a TD6 result, and not a resolution of JC2. The identity does not hold modulo `729`.

---

## 1. Exact determinant through modulo `243`

Independent expansion uses the binomial theorem, not repeated squaring:

```text
u^3 = x^3 + 3 x^2 y^3 + 3 x y^6 + y^9
u^4 = x^4 + 4 x^3 y^3 + 6 x^2 y^6 + 4 x y^9 + y^{12}.
```

The mixed coefficients `3,3` in `u^3` and `4,6,4` in `u^4` are present in `P5` and `Q5`. Replacing either power by its characteristic-three Freshman form changes the maps already modulo `9`, and changes the Jacobian modulo `243`.

Expanded supports:

```text
P5 = x - x^3 + 180 x y + 81 x y^2 - 3 x^2 y^3 - 3 x y^6 + y^3 + 180 y^4 - y^9
Q5 = y + 153 y^2 + 3 x^2 y + 6 x y^4 + 3 y^7
   + x^4 + 4 x^3 y^3 + 6 x^2 y^6 + 4 x y^9 + y^{12}
   + 81 x^4 y^2 + 81 x y^{11}.
```

The `(x,y)` Jacobian has exactly `33` terms. The constant term is `1`. Every other coefficient is divisible by `243` and not every one is divisible by `729`: the minimum `3`-adic valuation of `det J(P5,Q5)-1` is exactly `5`. Thus

```text
det J(P5,Q5) ≡ 1  (mod 243),     det J(P5,Q5) ≢ 1  (mod 729).
```

The thirty-two nonconstant terms, written as `243` times an integer coefficient, are

```text
243 * (
  2 y + 227 y^2 + 102 y^3 - 6 y^7 + 7 y^8 - 3 y^{12} + 3 y^{13} - 240 y^{14} + 3 y^{19}
  - 12 x y^4 + 4 x y^5 - 12 x y^9 + 13 x y^{10} + 600 x y^{11} + 243 x y^{12} - 5 x y^{16}
  - 6 x^2 y - 3 x^2 y^2 - 18 x^2 y^6 + 4 x^2 y^7 - 19 x^2 y^{13}
  - 12 x^3 y^3 - 8 x^3 y^4 - 960 x^3 y^5 + x^3 y^{10}
  - 3 x^4 - 2 x^4 y - 120 x^4 y^2 - 162 x^4 y^3 + 22 x^4 y^7
  + 8 x^5 y^4 - 2 x^6 y
).
```

A second Jacobian, computed in source coordinates `(u,y)` after the substitution `x=u-y^3` (chain-rule factor `det J(x,y↦u,y)=1`), is likewise `1` modulo `243`. Independently rebuilt payload SHA-256 is

`04ccf4367c5e321625e41f39faa37c69afdebdcbdc65af4ca66f14094b668850`,

matching both AWS stdout files and the producer note.

## 2. `Z/81` parent determinant and divided residual

The parent `Z/27` pair uses `18 y^2`. The W5 package continues in the same class modulo `27` by taking `72 y^2` (`72-18=54=2·27`). In coordinates `(u,y)`,

```text
(P4)_u = 1-3u^2+18y,   (P4)_y = 18u,
(Q4)_u = 4u^3+6 u y,   (Q4)_y = 1+3u^2+144y,
```

and the product formula expands by hand to

```text
(1-3u^2+18y)(1+3u^2+144y) - 18u(4u^3+6uy)
  = 1 - 81 u^4 + 162 y - 486 u^2 y + 2592 y^2
  = 1 + 81(-u^4 + 2 y - 6 u^2 y + 32 y^2).
```

The same polynomial is recovered from the `(x,y)` Jacobian. Every coefficient of `det J(P4,Q4)-1` is divisible by `81`; the quotient is exactly the displayed residual `ρ=-u^4+2y-6u^2 y+32 y^2`. Reducing `ρ` modulo three uses only integer coefficients, not Freshman's dream:

```text
ρ ≡ -u^4 + 2 y + 2 y^2 ≡ 2(u^4 + y + y^2)  (mod 3),
```

because `-1≡2` and `32≡2`, while `6≡0`. There is no sign error and no missing factor of two. The first-order lifting equation at modulus `243` is `ρ+L≡0 (mod 3)`. Since `81^2=6561=27·243`, the quadratic remainder in `R5,S5` is identically zero modulo `243`, so this linear condition is necessary and sufficient at this one step. The frozen run still expands the full integer Jacobian of `(P5,Q5)` rather than stopping at the linearization.

## 3. Linearized operator and the two primitives

At the special fibre `G9=(u-u^3,y+u^4)` over `F_3` one has `u_x=1`, `u_y=3y^2≡0`, hence

```text
P_x ≡ 1,   P_y ≡ 0,   Q_x ≡ u^3,   Q_y ≡ 1.
```

The bilinear part of `det J(P+81R,Q+81S)` is therefore `R_x-u^3 R_y+S_y`. That is the correct operator *after* the tame right-composition `A∘B9`: the `-u^3 R_y` term is the contribution of `Q_x≡4u^3`. The Artin–Schreier operator `R_s+S_t`, or the sign-reversed operator `R_x+u^3 R_y+S_y`, both fail the first primitive over `F_3`.

Over `Z`,

```text
D(2uy, y^2) = 4y - 2 u^4 - 6 u^3 y^3
            = 4y - 2 x^4 - 14 x^3 y^3 - 30 x^2 y^6 - 26 x y^9 - 8 y^{12},
```

which is not `u^4+y`. Over `F_3` it is `u^4+y`. Over `Z`,

```text
D(xy^2, x^4 y^2 + x y^{11}) = y^2 + 9 x y^{10} - 6 x^2 y^7 - 6 x^3 y^4,
```

which is not `y^2`. Over `F_3` it is `y^2`, because the extra terms are the integer remainder of `u^3-x^3-y^9=3(x^2 y^3+x y^6+y^9)`. Characteristic-three Frobenius is used only where it is valid, namely over `F_3`. The producer states both identities as mod-three primitives; that is exact. Summing them gives `D(R5,S5)≡u^4+y+y^2≡-ρ (mod 3)`.

## 4. Source reduction, degrees, D12 support, negative control

`81≡0 (mod 3)` and the inherited `18,3,72` coefficients are `0 (mod 3)`, so `(P5,Q5)≡(u-u^3,y+u^4)=(G9) (mod 3)`. Leading `y` faces remain `-y^9` and `+y^{12}`, units in `Z` and in `F_3`. Actual degrees:

| map | total | `y` |
|---|---:|---:|
| `P5` | 9 | 9 |
| `Q5` | 12 | 12 |
| `R5` | 4 | 4 |
| `S5` | 12 | 11 |

`R5=2xy+2y^4+x y^2` and `S5=y^2+x^4 y^2+x y^{11}` lie in the fixed box of total degree `≤12` and `y`-degree `≤12`. No overflow is hidden by writing `2uy`: that monomial expands to `2xy+2y^4`. Rewriting `x y^{11}` alone as `(u-y^3)y^{11}` would produce a `y^{14}` term, but the compensating `x^4 y^2` contributes `+y^{14}` in the same coordinates and the two cancel. In `(u,y)`, `S5` has `y`-degree `11` and `R5` has `y`-degree `5`. The displayed branch is therefore inside D12 both as `(x,y)` polynomials and as `(u,y)` polynomials. It uses six monomials, not the complete D12 output-digit cube.

Omitting the whole order-`81` digit leaves `det J(P4,Q4)=1+81ρ`, and `ρ≢0 (mod 3)`, so the parent without the new digit fails modulo `243`.

## 5. Manifests, freeze, dual-AWS custody, stdout

All SOURCE, MANIFEST, and FREEZE hashes of both the W5 package and the parent W3 package recompute. Box02 and Box03 `replay.stdout` are byte-identical. Both `replay.rc` are the single byte `0`. Both source-checks pass on `REGISTRATION.md` and `replay.py`. Both terminal markers are `AS-B9-MAX12-W5-SURVIVOR PASS`. `/usr/bin/time -v` RSS values `14616` / `14772` KiB match the README table. Stderr hashes differ only in host-specific resource fields.

| pin | digest |
|---|---|
| W5 stdout (both hosts) | `86afa339d260ac31d09a1ec59cd189c5adaa02212acd3d7c40bcd4c07678a853` |
| W5 payload | `04ccf4367c5e321625e41f39faa37c69afdebdcbdc65af4ca66f14094b668850` |
| W5 `replay.py` | `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` |
| W5 producer note | `9597217ab722593b5f114f81755482691fd16473b8a571ba147d25c45cf6b0e7` |
| parent W3 stdout | `f9e55a4f3cfc6c3b85b2d4c9ec724e0d757e083b0e82e0ff0e387d7125ea1aef` |

`replay.py` was not executed locally. The identities, the thirty-three-term Jacobian, and the payload digest were rebuilt from the displayed formulae.

## 6. Scope

The producer body, registration, and README all refuse the complete W2 fibre, a compatible all-depth tower, a `Z_3` or characteristic-zero map, a counterexample, a maximum-twelve theorem, TD6, and JC2. The immediate successor named in the note is the complete next-digit linear solve in the same D12 box, not a promotion of this selected pair. “Exact maximum-twelve frontier” names the checksum degree pair `(9,12)` already confirmed for the parent; it is not a maximum-twelve theorem. The special fibre is still `G9`, hence still a tame right-composition `A∘B9` and still not a group conjugate.

## Mathematical defects

None. In particular: no sign or factor error in the divided residual; no wrong derivative operator after the tame source transform; no characteristic-three Frobenius used over `Z`; no degree overflow hidden by `u`; no claim that this selected branch is the full affine D12 family.

## Terminology, custody, or exposition defects (non-blocking)

1. Registration says `2026-08-25T16:14Z, before execution`, while both AWS `end.utc` stamps are `16:10:57Z` / `16:11:01Z` and the job tag is `T1617Z`. Same timestamp-versus-tag pattern as the CONFIRMED parent freeze; the registration file itself is in `SOURCE.sha256` and passed both source-checks. Not used as mathematics.
2. Replay prints `source_reduction=B9`. The asserted reduction is to `G9=A∘B9`. Harmless label, inherited from the parent.
3. Empty `launcher.stdout` / `launcher.stderr` on both hosts. Two-host identity is carried by `replay.stdout`, `replay.rc`, `end.utc`, and distinct `time -v` fields.
4. W5 replay does not explicitly assert the mixed binomial coefficients of `u^3`, unlike the parent replay. Those coefficients are present in the payload-matching expansion and are load-bearing modulo `243`.
5. The producer note writes the W5 pair in one display and does not mention the intermediate change `18 y^2 → 72 y^2`. The case README does. Both representatives are the same modulo `27`; only `72 y^2` is the `Z/81` parent used here.

None of these defects changes an identity or licenses a broader claim.
