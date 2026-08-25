# AS F-only D7: exact degree-one influence on three displayed Q3 fibres

**Status:** producer-exact on AWS; **PROVISIONAL pending a different-model source/compiler review**.  This is a strict successor to the selected-family theorem reviewed at SHA-256 `47eaa4b7f850e8974a27f83cd1d2328d04e8a54dd359c7716611daea4b287e8e`.  It answers that review's degree-one concern on the three actual displayed fibres, not on the global predecessor scheme.

## Exact finite statement

Fix one of the three pinned Q5 predecessor models `base0000`, `base0270`, or `base0513`, and consume its entire reviewed displayed Q4 and Q3 affine fibre.  Starting from the literal integer map, retain the earlier arbitrary homogeneous degree-three and degree-two digits and add every homogeneous degree-one output digit

\[
  27(W_1,Z_1)+81(H_1,J_1).
\]

The compiler rebuilds `det J(P,Q)-1` over the integers and imposes all 91 coefficient rows of total degree 0 through 12, in the fixed order

\[
  (i,d-i),\qquad 0\le d\le12,\quad0\le i\le d.
\]

It first divides all 91 coefficients exactly by 27 and reduces modulo 3.  It solves the complete active-coordinate affine system and exhausts all 81 accepted assignments.  For each assignment it divides the same 91 literal coefficients exactly by 81, proves the remaining map affine by the complete quadratic design, and solves it.  Thus the audit covers exactly `3 * 81 = 243` branches.

| pinned predecessor | variables before/after degree one | `/27` rank | accepted `/27` assignments | every `/81` rank / augmented rank | row-8 constant | survivors |
|---|---:|---:|---:|---:|---:|---:|
| `base0000` | 42 / 50 | 6 | 81 | 7 / 8 | 2 | 0 |
| `base0270` | 38 / 46 | 6 | 81 | 9 / 10 | 2 | 0 |
| `base0513` | 38 / 46 | 6 | 81 | 9 / 10 | 1 | 0 |

In every branch, row 8 is `[x^2y]`.  Its entire remaining-variable coefficient row is zero, while its constant is respectively 2, 2, or 1.  Therefore every one of the 243 exact branch systems is inconsistent over `F_3`; no `/243` successor exists inside these displayed fibres.

## Degree-zero and trace chronology

Constant output corrections are not variables because their partial derivatives vanish identically, at every precision.  They cannot alter any Jacobian determinant coefficient.

Degree-one digits are not normalized away.  At `/27`, the two diagonal derivative columns occur explicitly in the degree-zero determinant row with coefficient 1.  They enlarge the source rank from the earlier selected-family value 5 to 6 and enlarge the accepted branch set from 27 to 81.  The exact active added columns are `(43,44)` for `base0000` and `(39,40)` for the other two parents; in source names these are the `x` coefficient of `W1` and the `y` coefficient of `Z1`.  Hence the trace/determinant-constant constraint is imposed chronologically before the `/81` systems are formed.

## Inclusion negative control

The conclusion is not an artifact of accidentally dropping the new columns.  The frozen branch payload records their full nonzero support.

- At `/27`, both added trace columns occur in row 0, `[1]` each.
- At `/81`, every one of the 81 branches has nonzero added-degree-one columns elsewhere in the matrix: exactly 3 such columns on `base0000` and 4 on each other parent.
- These columns hit rows including `[xy]`, `[x^3]`, and the degree-zero row, depending on the parent and branch.  None hits row 8.
- Correspondingly the branch ranks rise from the reviewed selected-family values `6,7,7` to `7,9,9`.

This is the requested negative control: the extra digits are source-present and mathematically active, but the singleton `[x^2y]` obstruction is invariant on these fibres.

## Source boundary and uncovered scheme

The reviewed parent at SHA-256 `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973` licenses the displayed Q3 fibres.  The present successor covers all displayed degree-three, degree-two, and degree-one order-27/order-81 output digits over exactly three pinned Q5 predecessor points.

It does **not** prove that these are whole structural bases, does not classify other Q5 predecessor solutions under the same base labels, and does not cover the rest of the accepted global Q5/Q4/Q3 predecessor scheme.  The separate affine-output normalization lemma only says that every genuine complete `Z_3` Keller map has a normalized representative somewhere in a full normalized scheme; it does not identify an arbitrary incomplete predecessor fibre with one of these three.  Therefore no `79 -> 76`, global-Q3, all-depth, algebraization, counterexample, or JC2 inference is licensed.

## Custody

Case: `cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/`

- preregistration SHA-256: `d42734629549332c2f01b3db7ff521def0cd00d5bcd005ae3dfd56640dd7aed2`
- V2 source `audit_degree1_v2.py` SHA-256: `219b1038e7e6779220795d2f9d4acab73d6d482d061c7a0fe01c05fdcebe8554`
- portable V2 runner SHA-256: `f762597271c963592ba9421d1204c3a94ac0a97c5e98e297440c7fd59a173a0a`
- output verifier SHA-256: `3bc77959afd3eeefa94725cce01e27414f5f1da737131eb470bd05d01ed2681c`
- portable all-three replay SHA-256: `890d6d69d0cb8a9a177d3d585fe3e94dc977dba65777120d0cc6ba6084b14b73`
- pinned two-level parent SHA-256: `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd`
- result JSON SHA-256 values: `9afa22f0c886bab3d5a2f4dbeb0f81c0e309b0cf0065fb360abe49c0ae2acf0f`, `d9a96fb1962e0505d2eab2acd53ac7c9f072725a3201c7ad89016aff4236f12d`, `6ad3142aff123e5fbc01aa77c56295119a5d3f16d2eb6c5c71785d826d6baa27`
- AWS endpoint: Box02, `/home/ubuntu/jobs/as_q3_q2q1_degree1_influence_20260825T1343Z_v2`, three rc0 runs under 32-GiB VM caps
- AWS output-verifier stdout SHA-256: `77b52eeaef50210b4260ca194d891de10a90b8a4b42cbb8ebfccba78f047389b` (`PASS`); stderr is resource custody only, SHA-256 `684d674b5c2337a157e50c762944a692cb9d57c629a9784983658f70fc740ee1`

The AWS deployment staged the V2 source bytes under the legacy filename
`audit_degree1.py` and invoked the legacy runner (SHA-256
`65e8b7301d722ff371e59bff54d615f5130555ad68c2c2871c88c317dc4bda55`).
The staged source hash is exactly the V2 hash above.  The portable frozen
successor uses the nonmutating filenames `audit_degree1_v2.py` and
`run_remote_v2.sh`; the original V1 source freeze remains byte-identical.

Portable AWS replay from a staged repository closure:

```bash
export JC2_ROOT=/path/to/jc2
export OUTPUT_ROOT=/path/to/fresh/output
bash "$JC2_ROOT/cases/as_fonly_d7_q3_q2q1_degree1_influence_20260825/replay_all_v2.sh"
```

## Refusal scope

No claim is made about any predecessor outside the three pinned displayed fibres, global normalized-chart coverage, a complete fixed-support map modulo a higher power, an all-depth lift, a characteristic-zero map, a counterexample, or JC2.
