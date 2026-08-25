# Reusable extension-field smooth-point oracle

This is a client-neutral, AWS-only producer for a sparse plane curve
`H(w,v)=0` with coefficients in an odd prime field.  It counts affine points
over a user-supplied finite extension and filters singular points using both
partials.  The required input schema is the already-used sparse table

```text
prime
degree_v
nonzero_support[v_degree] = [[w_degree, coefficient], ...].
```

The curve must be monic of declared degree in `v`.  The extension modulus is
given by low-to-high comma-separated coefficients.  Before emitting Singular,
the generator checks the curve hash, primality, support, monicity, and exact
irreducibility of the modulus via the finite-field Frobenius criterion.

For each extension-field value of `w`, Singular computes

```text
R_w = gcd(H(w,v), v^q-v),
S_w = gcd(R_w, H_v(w,v), H_w(w,v)).
```

Because `v^q-v` is squarefree, `deg R_w` is the number of distinct affine
points above `w`; `deg S_w` is the number singular there.  Thus the aggregate
smooth count is exact.  After an independently reviewed geometric-integrality
certificate, a smooth affine count greater than `q+1` proves positive genus
of the normalization.  The count alone proves no integrality, component
membership, characteristic-zero specialization, or trajectory claim.

Every Singular or substantive Python execution is AWS-only.  Local use is
restricted to source editing, hashing, shipping, and brief status checks.

## Controls and clients

The two bundled `p=5`, quadratic-extension controls use modulus `2,0,1`:

- `selftest_smooth.json`: `v^2-w`, exactly 25 smooth affine points;
- `selftest_singular.json`: `v^2`, exactly 25 affine singular points.

Q8 is the regression client, not a new theorem client.  Two named max-12
client slots remain intentionally unregistered until their exact projected
curve tables and geometric-integrality hypotheses are frozen.  No generic
curve is inferred from an avenue label.

## AWS smoke result

The pinned sources were exercised on AWS r6a (`ip-172-30-0-34`, Singular
4.3.2) under one-thread, 300-second, 1-GiB caps.  Both complete `F_25`
censuses and their fail-closed aggregates passed:

```text
v^2-w : total=25, smooth=25, singular=0
v^2   : total=25, smooth=0,  singular=25
```

The charged tags are

```text
extension_oracle_selftest_smooth_r6a_v1
extension_oracle_selftest_singular_r6a_v1
extension_oracle_selftest_smooth_aggregate_r6a_v1
extension_oracle_selftest_singular_aggregate_r6a_v1
```

An initial combined launcher started the smooth tag correctly but attempted
the singular redirection before retaining the intended remote working
directory.  That second attempt failed before creating an output directory or
starting Singular.  The singular tag above was then launched once from the
correct directory; no charged byte was overwritten.
