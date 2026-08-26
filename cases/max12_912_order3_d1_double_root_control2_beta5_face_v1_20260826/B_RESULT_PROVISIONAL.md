# Control-2 beta=5 equality face: inverse-encoding B result

Date: 2026-08-26 UTC

Status: **PROVISIONAL SINGLE-ENCODING CERTIFICATE.**  Promotion requires agreement
with the independently ordered direct-saturation encoding A and hostile source
review.

## Exact scope

This result concerns only the frozen control-2 source, fixed load
`mu=2/3`, fixed support `a-1=h=q2=k=nu=0`, and the single equality-face
weight

```text
(la,tau,rho,q1,q0,r2,r1,r0) = (4,1,1,20,20,30,30,30).
```

It is not a whole-cone, whole-fan, moving-load, or larger-support statement.

## AWS custody

- host: r6d (`100.26.198.153`)
- tag: `max12_912_order3_d1_double_root_control2_beta5_face_v1_20260826T025500Z_r6d_B`
- encoding: expanded double-inverse elimination, LPDP
- worker PID: `212593`
- source SHA: `023dc47323a3511a2457048166e50dadc05333b1ae9a9280003d1cb30f43d6eb`
- stdout SHA: `069a3428c77231a7bb079b7e161055f76a061784c218fc19663e3d199d0abf63`
- exit: `0`; CAS stderr and stdout diagnostics: empty
- elapsed: `2.80 s`; maximum RSS: `25,676 KiB`; swaps: `0`

## Exact endpoint

The inverse contraction has 319 generators.  Its special fibre has 41
standard-basis generators.  It contains both

```text
GH[40] = la^20
GH[41] = s.
```

The displayed beta=5 residue is killed.  After saturating the special fibre
by the product of the eight torus variables, the standard basis is

```text
GHT[1] = 1.
```

Thus encoding B proves that this exact fixed-weight, fixed-support torus
fibre is empty.  The simultaneous equality of the `q1*q0^3` and five `qrr`
terms in the previously extracted witness does not produce a surviving torus
residue in this encoding.

## Firewall

This file records only the completed B computation.  It must not be used to
exclude neighboring weights, omitted tail directions, moving loads, or the
whole double-root fan.  Those require separate identities or saturated-face
certificates.
