# Additive node619 probe outcome

Date: 2026-08-27

The preregistered exact expanded-polynomial probe of node619 reached its
4-GiB AWS virtual-memory cap after 3m53s and produced no expansion verdict.
Peak RSS was 4,142,632 KiB; the lane failed closed with no result JSON.
Failure-evidence manifest SHA-256:
`595199572425bcc28688b5f9622e81219d01ab31a42fc7f1236753d39a67b704`.

This resource-cap outcome is corroborative telemetry only.  It does not
weaken the exact nonzero proof used by `INVALIDATION.md`: node619 is the
polynomial

```text
K=a1^36+a1^18*m*ell1+(m*ell1)^2,
```

so the exact specialization homomorphism `ell1 -> 0` maps it to the nonzero
monomial `a1^36`.  No expanded form is required for that conclusion.

