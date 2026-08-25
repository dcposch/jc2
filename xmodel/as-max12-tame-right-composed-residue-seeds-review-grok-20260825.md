# Hostile different-model review — AS max-12 tame right-composed residue seeds

| Field | Value |
|---|---|
| Producer | `xmodel/as-max12-tame-right-composed-residue-seeds-producer-20260825.md` |
| Frozen case | `cases/as_frontier_conjugate_seeds_20260825/` |
| Overall verdict | **CONFIRMED** |
| Mathematical errors | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | independent bivariate polynomial arithmetic over `Z` (no SymPy, no `verify_seeds.py` import); complete `F_3^2` pointwise census; byte hashes of the freeze |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer and case uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

No load-bearing identity fails. Right-composition is not conjugation. Both displayed inverses and `det J(B)=1` hold over `Z`. The partial-`y` and total-degree pairs are exactly `(9,12)` and oriented `(8,12)`, with constant unit leading `y` coefficients. Over `Z`, `det J(A∘B)=1-3u^2`; the target swap/sign has determinant one and preserves that Jacobian. The `F_3^2` census is three fibres of size three. Source/output hashes, rc files, environments, two-host agreement, and scope markers match. No hidden promotion to a mod-9 lift, Q8/TD6 landing, characteristic-zero map, counterexample, maximum-12 theorem, or JC2 was found.

## Strongest exact claim

Let `A(s,t)=(s-s^3,t)`. For integers `m,k>=1` put `B_{m,k}=(u,v)` with `u=x+y^m` and `v=y+u^k`. Then over `Z`:

- `B_{m,k}` is inverted by `y=t-s^k`, `x=s-(t-s^k)^m`, both composition directions are the identity, and `det J(B_{m,k})=1`;
- `det J(A∘B_{m,k})=1-3u^2`.

In particular, with `G9=A∘B_{3,4}=(u-u^3,v)` one has

```text
deg_y(G9)=(9,12),    totaldeg(G9)=(9,12),    lead_y(G9)=(-1,1).
```

With `φ(P,Q)=(Q,-P)`, whose Jacobian determinant is `1`, put `G8=φ∘A∘B_{4,2}=(v,-(u-u^3))`. Then

```text
deg_y(G8)=(8,12),    totaldeg(G8)=(8,12),    lead_y(G8)=(1,1),
det J(G8)=1-3u^2.
```

The leading `y` coefficients are constants in `Z^x` and remain units in `F_3`. Reduction modulo `3` makes both Jacobian determinants the constant polynomial `1`. On `F_3^2` each reduced map has image size `3` and every fibre size `3`, hence is noninjective. These maps are source-coordinate transforms of `A` (for `G8`, after a determinant-one target orientation). They are not the group conjugates `B^{-1}∘A∘B`.

## Sharpest non-claim

Finite-field residue seeds with those degree faces only. This does not land either seed on a normalized Q8 or TD6 source-typed chart, does not produce a lift modulo nine, does not give a compatible all-depth branch, does not give a characteristic-zero Keller map, does not give a counterexample, does not prove a maximum-12 theorem, and does not resolve JC2.

---

## 1. Right-composition is not conjugation

The displayed maps are `A∘B`, i.e. source substitution `(x,y)↦(u,v)` into `A`. Independently, the group conjugates `B^{-1}∘A∘B` were expanded in the same generators. For both `(m,k)=(3,4)` and `(4,2)` both coordinate differences are nonzero as polynomials over `Z`. The two operations are distinct.

`G8` is not a pure right-composition: it is `φ∘A∘B_{4,2}`. Unoriented `A∘B_{4,2}` has `deg_y=(12,8)`. The producer construction paragraph and the preregistration state the extra target operation; that is the object that has oriented pair `(8,12)`.

## 2. Inverses and `det J(B)=1`

For both displayed `B`, the maps `y=t-s^k`, `x=s-(t-s^k)^m` satisfy

```text
B^{-1}∘B = id,    B∘B^{-1} = id
```

as polynomial identities over `Z`. Direct expansion of `u_x v_y - u_y v_x` is the constant `1` (the elementary factors `(x+y^m,y)` and `(s,t+s^k)` each have Jacobian `1`).

## 3. Degrees and leading `y` faces

Independent expansion over `Z`:

```text
G9_P = -y^9 - 3x y^6 - 3x^2 y^3 + y^3 - x^3 + x
G9_Q =  y^{12} + 4x y^9 + 6x^2 y^6 + 4x^3 y^3 + y + x^4

G8_P =  y^8 + 2x y^4 + y + x^2
G8_Q =  y^{12} + 3x y^8 + 3x^2 y^4 - y^4 + x^3 - x
```

Partial-`y` degrees `(9,12)` and `(8,12)`; total degrees the same pairs; leading `y` coefficients the constants `(-1,1)` and `(1,1)`. Those constants remain units modulo `3` after the `3`-divisible inner terms drop. No hidden `x`-dependence in either leading face.

## 4. Jacobian identities and the target orientation

Chain rule gives `det J(A∘B)=(1-3u^2)det J(B)=1-3u^2`. Direct expansion of both Jacobians recovers the same polynomial:

```text
G9:  1-3u^2 = 1-3(x+y^3)^2 = 1-3y^6-6x y^3-3x^2
G8:  1-3u^2 = 1-3(x+y^4)^2 = 1-3y^8-6x y^4-3x^2
```

The linear map `φ(P,Q)=(Q,-P)` has matrix `[[0,1],[-1,0]]` and determinant `1`. Direct Jacobian of `φ∘A∘B_{4,2}` equals `1-3u^2` over `Z`, so the orientation preserves the determinant as a polynomial, not merely modulo `3`. Reducing `1-3u^2` modulo `3` is the constant `1`.

## 5. Complete `F_3^2` fibre census

Evaluated at all nine points by integer substitution then `% 3` (not by the `a-a^3=0` formula alone).

`G9`:

| source | image |
|---|---|
| `(0,0),(0,2),(2,2)` | `(0,0)` |
| `(1,0),(2,0),(2,1)` | `(0,1)` |
| `(0,1),(1,1),(1,2)` | `(0,2)` |

`G8`:

| source | image |
|---|---|
| `(0,0),(0,2),(1,2)` | `(0,0)` |
| `(1,0),(2,0),(2,1)` | `(1,0)` |
| `(0,1),(1,1),(2,2)` | `(2,0)` |

Three image points, every fibre size three, hence noninjective. This matches the Artin–Schreier count for `A` (image `{0}×F_3`, fibres of size three) transported by the bijection `B`, and for `G8` by the further bijection `φ`.

## 6. Custody

All twenty `MANIFEST.sha256` entries rehash to the recorded digests. `FREEZE.sha256` rehashes `MANIFEST.sha256` to `1c39d8af63fee28111debbdb06d02809ccd1d1d83baf7ac82aa6c697f353eec8` and the review prompt to `b58529d8366a7c8cf1cced18683cd1f8875400872b428225444d2fd2e965c5db`. Authoritative source hashes match the producer:

- `PREREGISTRATION.md` `d7196367ba917d692a965eb6d5eab44bdecb8157ca43712a08a873d9e07b574a`
- `README.md` `f0ed37894c2208828b3068245041b29c34be09a72bedbe903563467fde7fd086`
- `verify_seeds.py` `3bca7ac19da1eeda9c5999f578a3717121fe970afebb12b801db6cb5ea784947`

Box02 (`ip-172-30-0-186`) and r6d (`ip-172-30-0-45`) have identical `ENVIRONMENT.txt` (`3.12.3` / `1.13.3`), `replay.rc` (`0`), empty `replay.stderr` (`e3b0c442…`), `SOURCE.sha256`, and stdout SHA-256 `1653dd2c98046bcb188ea6a5cf07bb77237dc241f9fa19d722e2d34ae0d3ca38`. Hostnames and finish timestamps differ, as required of two hosts. Stdout prints the claimed degree pairs, leading coefficients, `det_raw=1-3*u^2`, fibre size histogram `[(3, 3)]`, the PASS token, and the scope line forbidding mod-9 / all-depth / counterexample / Q8/TD6 / maximum-12 / JC2 promotions. `verify_seeds.py` imports no campaign solver.

## 7. Hidden-inference search

Read in full: producer, preregistration, README, `verify_seeds.py`, both AWS stdout files, and the scope print. Searched for lift, mod-9, Q8, TD6, Keller, counterexample, maximum-12 theorem, characteristic zero, and JC2.

The firewalls are actual non-claims, not covert proofs of absence. “Live maximum-12 frontiers” names the two degree pairs; it does not prove a maximum-12 theorem or chart landing. “Prove no lift modulo nine, …” is the campaign’s standard refusal list; preregistration and stdout make the same stop. No identity in the freeze reconstructs a mod-9 map, a Q8/TD6 source, a characteristic-zero Keller pair, or a JC2 conclusion.

## Mathematical errors

None.

## Naming, custody, or exposition defects (non-blocking)

1. The frozen directory is named `as_frontier_conjugate_seeds_20260825` while the theorem is that the maps are *not* conjugates. README, preregistration, producer body, and AWS job name `as_frontier_tame_right_composed_seeds_20260825T1612Z_v4` are correct. Renaming would break this freeze; do not read the path as mathematics.
2. One producer sentence calls both displayed maps “tame right-compositions `A∘B`”. `G8` is `φ∘A∘B`. The construction paragraph is exact; the later slogan is not.
3. The replay asserts partial-`y` degrees and prints total degrees without asserting them. AWS stdout and the independent expansion both give the claimed total-degree pairs.
4. The replay asserts `det J(A∘B)=1-3u^2` only for the unoriented composite, and `det≡1 (mod 3)` after orientation. Direct expansion shows the oriented `G8` Jacobian is still `1-3u^2` over `Z`.
5. `FINISHED_UTC` values `16:03:50Z` / `16:03:54Z` sit nine minutes before the `T1612Z` job stamp. Not used as mathematics; two-host stdout hashes agree.

None of these defects changes an identity or licenses a broader claim.
