# Result: localized low-contact rootwise gate

Date: 2026-08-26

Status: **exact-Q producer PASS; hostile review pending**.

The exact source/Faber compiler and the moving Laurent-coordinate bridge pass
all seven rows.  The frozen V3 negative control correctly found that the c2
identity is not integral in the unlocalized root ideal.  Its raw remainder is

```text
(3/8)*ell1*a0*a1*bs1 + (3/32)*ell1*a1^2*br1.
```

After saturation by `p*k0`, the ideal remains proper and that remainder is
zero.  The exact output therefore proves the two scoped implications on
`D(p*k0)`:

1. the c1 leading correction vanishes, by the integral grade-11/12 rootwise
   identity;
2. the c2 leading correction vanishes, by the localized grade-12/14
   rootwise identity.

This is an arcwise/set-theoretic contact-raising gate on the generic square
first-normal stratum.  It does not assert a reduced scheme, eliminate any
positive horizontal contact of `A`, cover `p=0` or `k0=0`, close the square
branch, or close exact order two.

## Exact custody

- source freeze-file SHA-256:
  `beea0c90fad4da24b386333917f2fea445ae941ad059e0ec2a4ceb69fe77123e`;
- compiled exact-Q Singular input:
  `82b422dce71fe17a4e71728a0ba6a09b4c468063fd3f0236b0df8d6ce1a79827`;
- exact-Q stdout:
  `0c44047c58922c823e47c75e2ea93499fc98640545b8f4b53b926309fd4748fd`;
- exact-Q validation:
  `c014ece48be8c2f405032f2ffec87bd4484b71ee983b3b3c8b64f2fbd7c977a0`;
- exact lane metadata:
  `d32f5f6a1371805653ba4a194f0348a09d54ce64dd9f49e7b28b918f9386945f`.

The lane was
`max12_812_order2_square_lowcontact_c2_delta_v4_q_20260826T094000Z_box03`
on Box03, returned engine `rc=0`, and ended with
`validator=PASS_LOCALIZED_MEMBERSHIP`.

## Frozen negative control

Namespaced V3 freeze-file SHA-256 is
`676f97810cc0c758ba864efe3463c2798f3c5d8f3fd70d57dee8ba0fb7457b57`.
Its exact-Q and `F_65521` runs both passed every source, Laurent, recurrence,
and c1 sentinel, and both rejected only the unlocalized c2 identity.  Their
stdout hashes are respectively
`1c5399e08ce16c3cf57de093d9a22c283e47643b4d629102f6770c271c38c4b3`
and
`718d1c4c8af098c8c677b047431bd9fda50b183d96dd94ee7cfc9822245afdc6`.
That agreement is retained as a negative control, not promoted as a c2
failure.
