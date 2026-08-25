# AS B9 complete D12 next digit through `Z/729`

Status: **producer-exact finite-depth theorem; parallel independent producer
exists; hostile review pending**.

The source rebuilds the frozen B9 `Z/243` point, divides its exact integer
determinant residual coefficientwise by `243`, and solves

```text
D(R,S)=-residual mod 3,
D(R,S)=R_x-u^3*R_y+S_y
```

over every total-degree-at-most-twelve monomial in both output digits.  There
are 182 columns.  Of the full 276 determinant rows through total degree 22,
135 are identically zero on the operator and target and are removed before
Gaussian elimination.  The resulting exact matrix is `141 x 182`, has rank
108 and kernel dimension 74, and the deterministic free-zero solution has 11
nonzero terms.  Literal integer reconstruction gives

```text
det J(P+243R,Q+243S)=1 mod 729.
```

The new map has actual partial `y`-degrees `(9,12)` and actual total degrees
`(11,12)`.  Omitting the new digit fails modulo `729`.  The replay emits the
entire divided residual, correction support, next divided residual, and a
canonical payload digest.

An independently written AS-owner implementation retains all 276 ambient rows
and reports the same rank 108/kernel 74, degree pairs, and the **identical
11-term deterministic particular solution**, but different source, matrix,
result, and stdout hashes.  That package is
`cases/as_b9_max12_full_output_mod729_20260825/`.  Agreement is corroboration;
it is parallel implementation evidence, not an independent mathematical
solution or a hostile review.

## Preserved reporter failure

The initial dual-host run
`as_b9_max12_w6_20260825T1629Z` reached and passed the determinant identity,
then returned rc 1 because the reporter incorrectly required the ordered
**total**-degree pair to stay exactly `(9,12)`.  The registered complete D12
cone requires both total degrees to be at most twelve.  The corrected source
asserts that bound and separately emits the actual pair `(11,12)`.  Both
initial stderr files are preserved as a negative custody control; their empty
stdout is not mathematical evidence.

## AWS custody

Corrected tag `as_b9_max12_w6_corrected_20260825T1634Z` ran on both hosts:

| host | remote path | UTC end | rc | max RSS | stdout SHA-256 |
|---|---|---|---:|---:|---|
| Box02 `34.203.207.55` | `/home/ubuntu/runs/as_b9_max12_w6_corrected_20260825T1634Z` | `2026-08-25T16:18:59Z` | 0 | 14,584 KiB | `6103ec3283d685c8093b055dd378995529a93fc183737fdf5148047d8d870d7a` |
| Box03 `98.80.65.144` | `/home/ubuntu/runs/as_b9_max12_w6_corrected_20260825T1634Z` | `2026-08-25T16:19:03Z` | 0 | 15,268 KiB | `6103ec3283d685c8093b055dd378995529a93fc183737fdf5148047d8d870d7a` |

The canonical payload SHA is
`313735e753e94234891898f13e180337b8d96737ee115c360dc690ec65ee417d`.

## Scope firewall

This is the complete D12 **next digit above one fixed parent point**.  It is
not the complete lower-level fibre, an all-depth compatible tower, a `Z_3` or
characteristic-zero polynomial map, a counterexample, a maximum-twelve
theorem, TD6, or JC2.  The emitted residual licenses the same exact next-digit
test modulo `2187`; finite-depth survival alone never licenses inverse-limit
language.
