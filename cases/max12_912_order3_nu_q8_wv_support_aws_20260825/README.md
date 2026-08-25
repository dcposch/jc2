# Selected-Q8 `(w,v)` / `(theta,v)` support learner (AWS-only)

This exact modular worker imports the immutable corrected-Q8 Hensel engine,
reconstructs

```text
v=(x3-2*x5)/x5
```

on the punctured branch, and searches rectangular plane-relation supports
for `(w,v)` and `(theta,v)`.  The prior order-128 matrix did not test either
pair.  A modular hit is only support evidence until cross-prime agreement,
characteristic-zero lifting, and exact substitution.  A full-rank rectangle
excludes a rational-coefficient relation only in that stated finite box.

Run only on AWS.  The default one-prime discriminator uses order 192, 16
holdout coefficients, degrees at most `24 x 16`, and at most 176 columns.

The frozen run is `aws/q8_wv_support_p10007_v1/`.  It finished with return
code zero and empty stderr.  Both pairs had full column rank in all 279
tested rectangles.  This is only a one-prime, rational-coefficient,
finite-support exclusion.  The lightweight local audit checks custody and
reconstructs the rectangle set; it does not rerun the Hensel/rank work.

```sh
python3 cases/max12_912_order3_nu_q8_wv_support_aws_20260825/audit.py
```
