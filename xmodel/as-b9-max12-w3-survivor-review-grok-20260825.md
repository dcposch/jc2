# Hostile different-model review — AS `B9` exact `Z/27` survivor

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-max12-w3-survivor-aws-20260825.md` |
| Frozen case | `cases/as_b9_max12_w3_survivor_aws_20260825/` |
| Overall verdict | **CONFIRMED** |
| Mathematical defects | none |
| Terminology / custody / exposition defects | non-blocking only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | independent `Z[x,y]` arithmetic in python-flint and a second dense engine; no import or execution of `replay.py`; full `F_3^2` census; byte recomputation of SOURCE / MANIFEST / FREEZE |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer and case uncommitted, matching the registration basis) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

The integer pair is exactly as written, the claimed Jacobian identity holds coefficientwise in `Z[x,y]`, and it reduces to the constant `1` modulo `27` and not modulo `81`. The intermediate modulo-nine identity, actual degrees `(9,12)`, unit leading `y` faces, source reduction to `G9=A∘B9`, explicit special-fibre collision, both omission controls, and the two-host freeze all replay. `G9` is a tame right-composition, not a group conjugate. No missing determinant term, no illicit integer Frobenius, no support overflow, and no licensed promotion to an all-depth lift, characteristic-zero map, counterexample, maximum-twelve theorem, TD6 object, or JC2 resolution.

## Strongest exact claim

Let `u=x+y^3` in `Z[x,y]`. The tame elementary automorphism `B9=(u,y+u^4)` has Jacobian determinant `1` and inverse `y=t-s^4`, `x=s-(t-s^4)^3`. Over `F_3`, `G9=A∘B9=(u-u^3,y+u^4)` with `A(s,t)=(s-s^3,t)` is etale, of actual partial-`y` and total degrees `(9,12)` and `(9,12)`, with constant unit leading `y` coefficients `(-1,1)`, and is not injective. It is a source-coordinate transform of the Artin–Schreier seed, not the conjugate `B9^{-1}∘A∘B9`.

The displayed integer lift

```text
P = u - u^3 + 18 u y
Q = y + u^4 + 3 u^2 y + 18 y^2
```

satisfies, as polynomial identities over `Z`,

```text
det J(P,Q) = 1 - 81 u^4 + 54 y - 162 u^2 y + 648 y^2 = 1  (mod 27),
```

has the same actual degree pair `(9,12)` and the same unit leading `y` faces, and reduces modulo `3` to `G9`. The W2 truncation `(u-u^3, y+u^4+3u^2 y)` has determinant `1-9u^4 ≡ 1 (mod 9)` and is not determinant one modulo `27`. Omitting either coefficient-`18` term breaks the modulo-`27` gate. This is one explicit fixed-support determinant-one point over `Z/27` on the `(9,12)` checksum face.

## Sharpest non-claim

One finite-depth point over `Z/27`. Not a compatible `Z/81` or all-depth tower, not a `Z_3` or characteristic-zero polynomial map, not a Keller counterexample, not a maximum-twelve theorem, not a TD6 object, not a classification of every lift of `G9`, not a group conjugate of `A`, and not a resolution of JC2.

---

## 1. Integer expansions

Independent expansion, with binomial coefficients retained:

```text
u    = x + y^3
u^3  = x^3 + 3 x^2 y^3 + 3 x y^6 + y^9
u^4  = x^4 + 4 x^3 y^3 + 6 x^2 y^6 + 4 x y^9 + y^{12}

P = -x^3 - 3 x^2 y^3 + x - 3 x y^6 + 18 x y - y^9 + 18 y^4 + y^3
Q =  x^4 + 4 x^3 y^3 + 6 x^2 y^6 + 4 x y^9 + y^{12}
   + 3 x^2 y + 6 x y^4 + 3 y^7 + 18 y^2 + y
```

The mixed terms `-3 x^2 y^3` and `-3 x y^6` in `P` are exactly the integer binomial remainder of `-u^3`. Replacing `u^3` by the characteristic-three Freshman form `x^3+y^9` changes the Jacobian already modulo `27`. The `u^4` binomial `6 x^2 y^6` is present over `Z` and vanishes modulo `3` only because `6≡0`, which is not Freshman's dream.

## 2. Determinant, coefficientwise in `Z[x,y]`

Working in the source coordinates `(u,y)`, whose Jacobian over `(x,y)` is identically `1`,

```text
P_u = 1-3u^2+18y,   P_y = 18u,
Q_u = 4u^3+6 u y,   Q_y = 1+3u^2+36y,
```

and the product formula in the case README expands to the claimed polynomial

```text
(1-3u^2+18y)(1+3u^2+36y) - 18u(4u^3+6uy)
  = 1 - 81 u^4 + 54 y - 162 u^2 y + 648 y^2.
```

Direct `(x,y)` Jacobian of the expanded pair equals that same polynomial after substituting `u=x+y^3`. The eleven monomials are

```text
1 + 54 y + 648 y^2 - 162 y^7 - 81 y^{12}
  - 324 x y^4 - 324 x y^9 - 162 x^2 y - 486 x^2 y^6
  - 324 x^3 y^3 - 81 x^4.
```

No further term exists. Every nonconstant coefficient is divisible by `27`, and the constant term is `1`, so the reduction is the constant polynomial `1` modulo `27`. The 3-adic valuations are sharp: `54 y` has valuation exactly `3`, so the identity does not hold modulo `81`. The README's rejection of the older `+18 u^4` shorthand is correct: the cross term contributes `-72 u^4 ≡ +9 u^4 (mod 27)`, which cancels the product's `-9 u^4`.

python-flint, a second dense engine, and integer point samples all agree. Independently rebuilt payload SHA-256 is

`d4482e42f617a4693e7142725ae37de45e3285926408d56c6ad1b746cb405f2e`.

## 3. W2, degrees, faces, reduction, collision

W2 pair `(u-u^3, y+u^4+3u^2 y)` has Jacobian `1-9u^4`, hence `1` modulo `9` and not modulo `27` (residue `18` on the `u^4` face). Both actual partial-`y` degrees and both actual total degrees of `(P,Q)` and of `G9` are `(9,12)`. Leading `y` faces are the constants `-y^9` and `y^{12}`; they are units in `Z`, in `F_3`, and in `Z/27`. No term of `y`-degree or total degree exceeds twelve. Reduction modulo `3` is exactly `G9`; reduction modulo `9` is exactly the W2 pair.

On `F_3^2` the fibres of `G9` (and of `(P,Q)`) are

| image | sources |
|---|---|
| `(0,0)` | `(0,0),(0,2),(2,2)` |
| `(0,1)` | `(1,0),(2,0),(2,1)` |
| `(0,2)` | `(0,1),(1,1),(1,2)` |

The displayed collision `(0,0),(2,2)↦(0,0)` is correct; it is an existence witness, not a claim that the fibre has size two. Over `Z/27` those two points do not collide (`(2,2)↦(18,9)`), so noninjectivity is special-fibre only, as written. Independently, `B9^{-1}∘A∘B9` differs from `G9` in hundreds of monomials.

## 4. Omission controls, hashes, AWS, replay

Omitting `18uy` leaves a modulo-`27` determinant with a `9y` term and an `18 u^4` face. Omitting `18y^2` leaves `18y`. Both gates fail, as claimed.

All SOURCE, MANIFEST, and FREEZE hashes recompute. The two `replay.stdout` files are byte-identical at

`f9e55a4f3cfc6c3b85b2d4c9ec724e0d757e083b0e82e0ff0e387d7125ea1aef`,

both `replay.rc` are `0`, both source-checks pass on `REGISTRATION.md` and `replay.py`, both terminal markers are `AS-B9-MAX12-W3-SURVIVOR PASS`, and `/usr/bin/time -v` RSS values `14620` / `15192` KiB match the README table. Stderr hashes differ only in host-specific resource fields. `replay.py` was not executed locally; the identities and payload digest were rebuilt from the displayed formulae.

## 5. Terminology and scope

The producer constructs `G9` by right-composition `A∘B9` and later calls it “tame-equivalent to the old residue seed”. That is source-transform language, not conjugacy, and it is consistent with the already-reviewed residue-seed package: `G9` is not a new residue isomorphism class. TD6 is correctly refused: the special fibre has separable function-field degree three, while the frozen TD6 source is the unrelated pole pair `p=t^{15}, q=t+t^{25}` plus SP-2. The `(9,12)` face is one of the two primitive characteristic-zero maximum-twelve *checksums*; that is a name for the degree pair, not a maximum-twelve theorem. The body, registration, and README refusal lists match the licensed object.

## Mathematical defects

None.

## Terminology, custody, or exposition defects (non-blocking)

1. “Tame-equivalent” is slightly looser than “right-composition / source transform”. The construction paragraph is exact and never says conjugate. Independently, the conjugate is a different pair.
2. Replay prints `source_reduction=B9`. The asserted reduction is to `G9=A∘B9`. Harmless label.
3. Job tag `T1607Z` sits after the recorded end times `16:05:40Z` / `16:05:44Z`. Same timestamp-versus-tag pattern as the residue-seed freeze; not used as mathematics.
4. Empty `launcher.stdout` / `launcher.stderr` on both hosts. Two-host identity is carried by `replay.stdout`, `replay.rc`, `end.utc`, and distinct `time -v` fields.
5. “Serious counterexample-side client” is promotional colour. The next sentences refuse a counterexample, a characteristic-zero map, and an all-depth tower.

None of these defects changes an identity or licenses a broader claim.
