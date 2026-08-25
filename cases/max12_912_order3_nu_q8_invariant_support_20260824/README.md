# Q8 invariant-support AWS successor

This producer-internal successor pins the frozen corrected-Q8 quotient and
specializes the selected component at rational reductions of eight Q8
contacts.  It lifts the exact six-row branch and searches for bounded plane
relations in

```text
(theta,Z), (w,q), (n,q), (theta,q),
theta=w*(1+w*c^3)^2, Z=q^9/n^10.
```

Ship the repository checkout and run:

```sh
python3 cases/max12_912_order3_nu_q8_invariant_support_20260824/run_matrix.py \
  --output-directory /local/ssd/q8-support-128 \
  --workers 8 --order 128 --max-left 24 --max-right 24 \
  --max-columns 108 --holdout 16 \
  > /local/ssd/q8-support-128-summary.json
```

The worker is pure Python/stdlib and single-threaded.  Different primes are
independent.  A local order-24 control used 20.2 wall seconds and 24.1 MB RSS
on one core.  The sequential lift is quadratic in order; budget 12--20
minutes and under 128 MB per order-128 worker, hence 8 vCPUs and under 1 GB
RAM for the default matrix.  A 60-minute fail-closed timeout is built in.

The direct Singular block elimination to `(w,q)` at prime `32003` was an
opaque no-result control: it was interrupted after 13m34s at 360 MB RSS while
still inside `slimgb`, before producing a basis or eliminant.  It certifies
nothing and is not an input to the support learner.

A modular hit is support learning only.  Promotion requires matching support
at multiple primes, rational reconstruction, and exact characteristic-zero
substitution into all six rows.  Absence of a relation in a stated rectangle
at one good specialization is an exact bounded rational-relation falsifier
after the good-reduction hypotheses are recorded; this package does not yet
freeze such a theorem.
