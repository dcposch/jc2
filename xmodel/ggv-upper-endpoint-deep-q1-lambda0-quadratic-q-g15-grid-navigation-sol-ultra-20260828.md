# Deep lambda-zero tail: quadratic-`Q` odd-receiver navigation grid

Date: 2026-08-28

Status: **exact sampled navigation evidence; not a universal theorem**

## Question and scope

After the exact fixed-`Q=X` exclusion, test whether releasing `Q` while
retaining

```text
A=X^4-1,  r=e=F8=F10=F12=F14=0
```

immediately produces an origin-endpoint survivor.  For each fixed `Q`, the
AWS runner independently:

1. reconstructs the exact `q7,q9,q11,q13,q15` linear system with all raw odd
   floors;
2. computes its rational nullspace;
3. reconstructs the complete characteristic and imposes polynomiality plus
   both literal degree bounds for `G9,G11,G13,G15`;
4. restricts
   `F11[X1]G11[X0]-F7[X0]G15[X1]` to the surviving linear space and tests the
   complete polarized quadratic form, not just chosen points.

The scalar `c2` is fixed to `1`; `c4,c6,c8` range independently over
`{-2,-1,0,1,2}`.  `c10` cannot enter by weight 15 because `F5=0`, and later
modes are unborn.

## Result

The seven exact `Q` fixtures were

```text
X, 1, 1+X, X^2, 1+X^2, X+X^2, 1+X+X^2.
```

Across all `7*5^3=875` fixed `(Q,c4,c6,c8)` systems, the endpoint quadratic
restricted identically to zero.  No nonzero witness was found.

This is not an artifact of empty receiver fibers.  Depending on the fixture
and modes, exact survivor dimensions ranged from `0` through `6`; for
example, `Q=1` had dimension `6` in all 125 mode fixtures, while generic
linear/quadratic mixtures included zero-dimensional cases.

The result strongly routes toward a symbolic arbitrary-quadratic-`Q`
identity.  It does not prove one: a finite coefficient/mode grid is navigation
evidence only, even though every individual computation is exact.

## AWS custody

Run tag:
`ggv-lambda0-quadratic-q-g15-grid-r1-20260828`.

The run completed on `ip-172-30-0-249` with exit code `0`, 226 seconds of
single-core exact arithmetic, and maximum RSS 21032 kB.  Frozen SHA256 values:

```text
source  2c9c6d0245fdb20b1c826584d852ec54b3bb63d7488698116b05754d206be527
stdout  68447f9a40fa1d902049b327d793be1132426418bf0c6a642f162bb8c17242f0
stderr  16e91dd15e26d191d116fbfc01013fa6e26b0dbcb47a8e1189bf638b1d75716b
meta    2271216930b839eda22c9cab7b61c98627d47e9f73612ea735a84028138545cf
runner  ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b
```

The frozen bundle also contains the exact upstream q15 and characteristic
engines with their already reviewed hashes.

## Light replay

```bash
python3 cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_quadratic_q_probe_20260828/verify_quadratic_q_grid.py
```

This verifies every custody hash, the AWS fail-closed source guards, run tag,
host, exit status, all 875 result records, the absence of a nonzero endpoint
witness, and the nontrivial survivor-dimension range.  Re-executing the heavy
grid remains AWS-only.
