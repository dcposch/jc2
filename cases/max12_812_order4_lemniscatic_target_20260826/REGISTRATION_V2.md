# AWS registration: loaded order-four lemniscatic target V2

Date: 2026-08-26

Status: preregistered; no endpoint consumed.

## Scope

V2 is a fail-closed arithmetic certificate, replacing the immutable failed
V1 library-parametrization control.  It directly checks the rational map

```text
q=T^2(T-1),
v=5184/((T-1)(21T-22)(3T-2)^6)
```

against the exact residual polynomial after clearing denominators.  It also
checks the `q=-4/27` and `q=484/9261` branch identities, the value
`v(0)=81/22`, the complete charged divisor profile
`(8,-1,-1,-6)`, the fourth-power removal

```text
S=24(T-1)/(3T-2),
(1/v)/(S(S-1))=(3T-2)^8/124416,
```

and cleared identities for `Z^2=X^3-16X` and
`dX/Z=-dxi/W` on `xi^4=S(S-1)`.

This is an arithmetic/control certificate for the target theorem only.  It
does not prove source-component coverage, source nonconstancy, or eliminate
the loaded order-four leaf.  Those remain the independent projection gate.

## Frozen parents and AWS lane

- target theorem SHA-256:
  `cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756`;
- confirmed review SHA-256:
  `59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a`;
- tangent erratum SHA-256:
  `26a083fcfa805a52fdb295ceaaf94ae7497047d8545a2323a48a688ac39e2300`.

Registered tag:
`max12_812_order4_lemniscatic_param_v2_20260826T023000Z_box03`.
Host Box03, instance `i-0ece0b9a3b4a7512f`, public IP `98.80.65.144`,
expected hostname `ip-172-30-0-249`; same-named directory under
`/home/ubuntu/jobs/`; exact Singular 4.3.2; timeout `1800 s`;
virtual-memory cap `8388608 KiB`.

The remote launcher must record actual PID, hostname, UTC start, caps,
archive/input hashes, engine version, return code, and output hashes.  Any
failed identity, source/freeze mismatch, timeout, OOM, engine error, nonzero
return code, or missing final PASS token is **NO VERDICT**.
