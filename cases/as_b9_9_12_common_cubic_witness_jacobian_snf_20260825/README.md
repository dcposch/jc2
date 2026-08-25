# Common-cubic witness Jacobian/SNF certificate

This case reconstructs the exact integer Jacobian of the 299 displayed
equations at one normalized `(9,12)` common-cubic witness modulo `3^11`.
It contains all 276 determinant coefficient rows and all 23 leading-form
rows, in 149 coefficient/core variables.

The primary AWS replay used python-flint 0.9.0:

```bash
case_dir=cases/as_b9_9_12_common_cubic_witness_jacobian_snf_20260825
export WITNESS_JSON="$PWD/$case_dir/AWS_R6D/witness.json"
export EXPECTED_WITNESS_SHA256=a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a
export OUTPUT_JSON=/tmp/as_b9_common_cubic_jacobian_snf.json
export MATRIX_GZIP=/tmp/as_b9_common_cubic_jacobian_snf_matrix.json.gz
python "$case_dir/jacobian_snf.py"
```

The exact rational-kernel classification reuses that matrix:

```bash
export MATRIX_GZIP="$PWD/$case_dir/AWS_R6D/matrix.json.gz"
export WITNESS_JSON="$PWD/$case_dir/AWS_R6D/witness.json"
export EXPECTED_MATRIX_GZIP_SHA256=65eb73affe9e8217607650e932f0c71ae243949aac26703474045da5a6adebaf
export EXPECTED_WITNESS_SHA256=a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a
export OUTPUT_JSON=/tmp/as_b9_common_cubic_kernel.json
python "$case_dir/classify_kernel.py"
```

Campaign policy requires substantive replays to run on AWS, not the local
workstation.  The frozen `AWS_R6D` directories preserve the producer output,
timing, inputs, and source closure.

## Exact scope

This is a pointwise conditioning/kernel theorem for one literal witness.  It
rules out one classical maximal-minor Hensel shortcut at the present
precision.  It does not rule out Smith-coordinate/dilatation methods, lifting,
the normalized family, the B9 family, maximum twelve, a counterexample, or
JC2.
