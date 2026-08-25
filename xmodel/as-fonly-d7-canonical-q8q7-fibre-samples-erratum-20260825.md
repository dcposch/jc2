# Erratum: canonical Q8 fibre coordinate `s=0` is not the coefficient vector `y=0`

**Status: PRODUCER EXACT COORDINATE CORRECTION; PROVISIONAL PENDING
DIFFERENT-MODEL REVIEW.  THE EARLIER REPORT AND FREEZE REMAIN IMMUTABLE BUT
MUST BE READ THROUGH THIS ERRATUM.**

The frozen report
`xmodel/as-fonly-d7-canonical-q8q7-fibre-samples-20260825.md` and its
`FREEZE_RESULT.txt` incorrectly say that the Q8 affine particular vector is
the zero 32-vector at all 64 sampled Q9 states.  The producer actually solves

```text
y = y0 + K s,       s in F3^19,
```

and reports `first_witness=[0,...,0]` in the **RREF fibre coordinate** `s`.
The consumed coefficient vector is therefore `y=y0`, which need not vanish.

An AWS audit of every frozen predecessor JSON gives:

```text
64 total samples;
13 have y0=0;
51 have y0 nonzero.
```

The portable catalog `particulars.json`, SHA-256
`3b00529566df3850e42a29325af22de1b0e938a4d3b17de680ad91e44f6ce76c`,
displays for each sample its predecessor JSON SHA-256, all 32 entries of `y0`,
the SHA-256 of `bytes(y0)`, and the nonzero support.  In every record the RREF
fibre coordinate remains the displayed zero 19-vector.

The correction changes wording, not the underlying pointwise compatibility:
the original compiler substituted `y0+K*0=y0` into all 22 Q8 rows and the Q7
system.  Thus all 64 displayed pairs `(x,y0)` remain actual Q8-compatible
points whose Q7 cokernel RHS vanishes.  The quadratic fitted presentation and
its `MODEL_COUNT` status are also unchanged; neither is promoted to a
whole-fibre theorem.

Preservation table:

| Earlier statement | Disposition |
|---|---|
| all 64 Q9 source substitutions vanish | survives |
| Q8 rank pair `(13,13)` and fibre dimension 19 at all 64 | survives |
| the 64 consumed points have coefficient vector `y=0` | **retracted** |
| the 64 consumed points have RREF fibre coordinate `s=0` | survives |
| Q7 rank 9/cokernel 10 and zero cokernel RHS at `(x,y0)` | survives |
| fitted `kappa_5=s15`, `kappa_8=s17`, model count `3^17` | survives only as control/`MODEL_COUNT` |

The earlier fixed canonical `e17` branch is not affected.  Its displayed Q9
point is sample zero here, whose affine Q8 particular is genuinely `y0=0`;
the frozen exhaustive Q7-kernel next-high theorem directly fixed that zero
coefficient vector.  Earlier low-weight successor code likewise stored and
substituted its actual `yvalues`, so this erratum does not silently replace
those states.

The audit ran on Box02 at
`/home/ubuntu/jobs/as_q8_particular_erratum_20260825T0425Z`, return code zero,
with empty stderr.  Audit stdout SHA-256 is
`b229fcaa35f06b15f6ce55b44304b1eb3b8995b93b293cd53e932bb6ca38583d`.

This erratum adds no whole-fibre, full-chart, later-carry, fixed-cap/all-depth,
counterexample, or JC2 claim.

