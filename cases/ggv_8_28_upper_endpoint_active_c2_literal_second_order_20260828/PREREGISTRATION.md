# Preregistration: relaxed second-order endpoint screen

Date: 2026-08-28 09:03Z UTC.  Status: **V2 FROZEN BEFORE AWS RUN**.

## Question

At the frozen deep active-`c2` homogeneous point, the exact tangent map

```text
A : Q^308 -> Q^510
```

has rank 291 and a 17-dimensional kernel.  For a legal first direction
`v in ker(A)`, a legal second correction `w`, and the determinant's quadratic
term `Q(v,v)` (including the forced Hessian of the nonlinear reduced-prefix
parametrization), can

```text
A*w + Q(v,v) = D22[X0]
```

hold?

The first screen writes `v=sum u_i v_i`, replaces the 153 symmetric
monomials `u_i*u_j` by independent variables `z_ij`, and tests the relaxed
linear system with 308 correction columns and 153 quadratic columns.  This
relaxation deliberately enlarges the possible second-order images.

## Frozen source

```text
fbb87243a52df665df45d9db5b9fee5c0657da249d8da3c659b9fe0189036b98  probe_second_order_relaxed.py
ddcd7b5d9cc5dd37e56412f606eb4b0fb37bc976280b224ac9dcf91a04be20a1  ../ggv_8_28_upper_endpoint_active_c2_literal_tangent_20260828/probe_tangent.py
d21fc8538e908f9a1bc6705fd9e5cf99a2c3d0be3f3b8a82318906ef817c0a8b  ../ggv_8_28_upper_endpoint_active_c2_literal_tangent_20260828/aws_exact_q_r1/output/TANGENT_CERTIFICATE.json
```

The script is AWS-only and refuses a non-Linux or non-EC2 host.  It captures
the frozen producer's exact tangent directions without editing the frozen
source, reconstructs the kernel over `Q`, independently checks all kernel
vectors, includes the `S^2`, `S Z`, `S^3`, and `c2*S` prefix-curvature terms,
and then constructs the full coefficient-row union through D22.

V1 (`1c37eb60...`) was frozen but never executed: its redundant inner guard
read EC2 `product_version`, which is blank on the authorized r6i hosts, and
would have false-refused before any payload.  V2 changes only that preflight
to the campaign-standard exact check `sys_vendor == "Amazon EC2"`.

## Charged outcomes

`SECOND_ORDER_RELAXED_INCONSISTENT_AT_THIS_POINT` requires:

1. three frozen primes `65521,65519,65497` all reject the augmented target;
2. exact-Q elimination rejects it;
3. an exact left dual is emitted and replayed internally with
   `y*[A|Q]=0`, `yb=1`;
4. source/output hashes, telemetry, zero-swap status, and final empty process
   census are frozen.

That outcome proves no legal second-order lift exists at this one base point,
because even the enlarged independent-monomial system is empty.

`SECOND_ORDER_RELAXED_CONSISTENT_NO_VERDICT` means only that the linear
relaxation survives.  It does **not** produce a second-order arc.  The next
step is to impose the Veronese equations `z_ij=u_i*u_j` (equivalently the
rank-one symmetric constraint) together with the surviving affine space.
Mixed primes, timeout, memory/resource cap, source drift, custody failure, or
failed internal assertions are `NO VERDICT`.

The zero-target system with `v=w=0` is the positive control.  Omitting the
nonlinear reduced-prefix Hessian is a mutation, not an accepted computation.

## Scope firewall

Even relaxed inconsistency concerns only order-two arcs based at this one
homogeneous raw point.  It does not exclude higher ramified arcs, other base
points, the deep `A|V0` locus, unrestricted branch P, landing, Keller pairs,
or JC2.  Relaxed consistency is strictly navigation and licenses no survivor
claim.
