# AS F-only D7: exact Gaussian exclusion on three displayed Q3 fibres

**Status:** producer-exact and independently certificate-replayed on AWS; **PROVISIONAL pending a different-model source/normalization audit**.  The finite linear-algebra conclusion below is exact for the displayed normalized digit family.  It is not yet promoted as a source-complete exclusion of the three Q3 fibres.

## Typed finite claim

Fix one of the three Q5 predecessor models `base0000`, `base0270`, or `base0513`, and consume its entire reviewed Q4 and Q3 affine fibre.  Starting from the literal integer map produced by the reviewed Q3 compiler, add

\[
  27(W_3+W_2,\,Z_3+Z_2)+81(H_3+H_2,\,J_3+J_2),
\]

where every subscript denotes an arbitrary homogeneous binary form of that total degree.  The producer then uses the literal integer Jacobian determinant; it does not replace a carry by a formal linearization.

For all 91 coefficient slots of total degree 0 through 12 it performs the following accepted-digit tower over `F_3`.

1. Divide every coefficient of `det J(P,Q)-1` exactly by 27 and reduce modulo 3.  The source matrix has rank 5.  Only eight raw coordinates occur:
   `w3_1,w3_2,z3_1,z3_2,w2_1,w2_2,z2_0,z2_1`.
   Exhausting their `3^8` values gives exactly 27 accepted assignments.
2. For each accepted assignment, retain **all** remaining Q3-fibre and fresh digit coordinates.  Divide the same 91 literal determinant coefficients exactly by 81 and reduce modulo 3.  A complete quadratic design proves that this restricted map is affine on the whole remaining cube.
3. Every one of the 27 branch systems is inconsistent.  Consequently the planned `/243` terminal layer is never reached.

The exact results are:

| fixed Q5 predecessor | raw variables | variables after the eight-coordinate branch | affine-design points per branch | branch rank / augmented rank | branches excluded |
|---|---:|---:|---:|---:|---:|
| `base0000` | 42 | 34 | 630 | 6 / 7 | 27 / 27 |
| `base0270` | 38 | 30 | 496 | 7 / 8 | 27 / 27 |
| `base0513` | 38 | 30 | 496 | 7 / 8 | 27 / 27 |

There is a particularly small obstruction in every branch.  Row 8 in the fixed slot order is the coefficient of `x^2 y`.  Its entire `/81` coefficient row is zero, while its equation has nonzero right side.  Equivalently, the literal residual

\[
  [x^2y]\,(\det J(P,Q)-1)/81 \pmod 3
\]

is independent of every remaining displayed coordinate and equals `2`, `2`, and `1` on `base0000`, `base0270`, and `base0513`, respectively.  Each stored singleton left-null vector normalizes its pairing with the right side to 1.

## Exhaustive certificates and controls

For every one of the 81 branches the frozen JSON stores the full matrix, right side, their hashes, and a sparse left-null vector `lambda` satisfying

\[
  \lambda^T M=0,\qquad \lambda^T b=1\quad\text{in }\mathbf F_3.
\]

The independent verifier:

- exhausts all `3^8=6561` first-stage assignments and reproduces exactly the 27 accepted assignments for each parent;
- checks all 81 left-null certificates directly from the stored matrices;
- checks an inclusion-minimal multirow omission control on every branch.

The omission control reconstructs raw digits, literally verifies every `/27` row and every retained `/81` row, and verifies that at least one omitted `/81` row is nonzero.  Omission-set sizes are 2--4 for `base0000`, 3--6 for `base0270`, and 2--5 for `base0513`.  The frozen V1 attempt requiring a *single*-row omission control is retained as a negative control: redundant obstruction rows make that stronger preregistration false, while leaving every rank and left-null certificate intact.

## Load-bearing audit boundary

The calculation is complete for the displayed homogeneous degree-3/2 order-27 and order-81 digit family, including all 63 over-cap slots of degrees 7 through 12 among the 91 rows.  Promotion to a source-complete exclusion of a Q3 fibre requires a reviewer to verify that this is the full normalized derivative-effect cone at these precisions.  In particular, the review must decide whether omitted degree-1 (and possible constant) order-27/order-81 digits are legally removed by the source/symplectic affine normalization when the degree-zero determinant row remains zero.  If that normalization is not licensed, the exact theorem stops at exclusion of the selected normalized digit family.

## What is and is not covered upstream

The three inputs are three **fixed Q5 predecessor points** harvested from the structural-base fanout.  For each point, the parent theorems cover its entire displayed Q4 affine fibre and entire displayed Q3 affine fibre; the present certificate covers every accepted branch of the displayed Q2/Q1 digit family over that fibre.

This does **not** exclude three whole structural bases.  Other Q5 predecessor solutions may exist under the same base labels.  Nor does it classify the complete 79-structural-base predecessor scheme.  The exact global remainder is therefore the whole accepted Q5/Q4/Q3 parameter scheme outside these three pinned predecessor fibres, plus any source directions rejected by the normalization audit.

## Custody and replay

Case: `cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/`

- preregistration SHA-256: `15dd551af28019dc31cf9da3a752602c898235f2cada971f73e1b8cf6e86915e`
- producer SHA-256: `cb9d30f6d47ea65b317cbc93b68da4b4eec5e26a0c9b7d00aa68edfb73939a31`
- independent verifier SHA-256: `68990434ef78a3709883e7443e45d258a1911f2741345403d3b9cdbb059b7e04`
- remote runner SHA-256: `6a13ce08c95eb25db04165863842864a4a7eb2d9ea874b835cf83b19916c41ff`
- pinned Q3 producer SHA-256: `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b`
- Q3 different-model review SHA-256: `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` (`CONFIRMED`)
- AWS endpoint: Box02, `/home/ubuntu/jobs/as_q3_q2q1_gaussian_exclusion_v2_20260825T1340Z`
- exact certificate JSON SHA-256 values: `8e563b395d4181d90967c75c35242abc557a8979b4c3f6d89757ce3d234b3f1b`, `5659a16810515290ede2dc78f404330971103f8cbc14fa3116901327f5dee2e9`, `5ebacfe12f4492607f69e9518bb6a1ef6102179725f5033550d0b8397bae8015`
- all six producer/verifier runs returned PASS with empty substantive stderr.

Portable AWS replay from a staged repository closure:

```bash
export JC2_ROOT=/path/to/jc2
export OUTPUT_ROOT=/path/to/fresh/output
bash "$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_v2_20260825/replay_all.sh"
```

## Refusal scope

No claim is made about another Q5 predecessor, an entire structural base, the whole Q5 locus, omitted source directions, all-depth lifting, algebraization, a characteristic-zero map, a counterexample, or JC2.
