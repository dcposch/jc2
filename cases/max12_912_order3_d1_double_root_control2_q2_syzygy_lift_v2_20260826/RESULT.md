# Exact first `q2` syzygy lift

Date: 2026-08-26 UTC

Status: **DUAL-AWS EXACT ONE-WEIGHT OBSTRUCTION, HOSTILE REVIEW PENDING.**

The five weight-75 terms in the unchanged-multiplier negative control are
cancellable in the original eight-row module.  With the frozen full-`q2`
rows, the complete weight-52 coefficient satisfies both

```text
C_52 = (1/9) in_52(E2) - (1/12) in_52(E1)
```

and the earlier special-fibre-basis expression

```text
C_52 = (2/81) GH3 - (1/27) GH5 + (2/27) GH6.
```

These are two representations of the same polynomial.  Exact RREF of all
eight row initials has rank 3 and gives the canonical free-zero correction

```text
g1=1/12, g2=-1/9, g3=...=g8=0.
```

Thus set

```text
F1' = F1 + q2/12,
F2' = F2 - q2/9,
Fi' = Fi                    (3 <= i <= 8),
W'  = sum_i Fi' Ei(full q2).
```

Both independent expanded encodings verify this as a literal polynomial
identity, verify `W'|q2=0=W`, and give the same canonical hashes

```text
W' SHA-256                 ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b
(W'-W)/q2 SHA-256          ac7d43b5e71444f5cd487328f7aff6b2312d198649a2c0b001d4a13ef006956c
old first-bad C52 SHA-256  4493daefdd98d9158f556735b8adf50978ec5b8e61295c58fd79e65d1e907b28
```

The corrected polynomial has 37 terms and `(W'-W)/q2` has 29 terms.  At the
exact registered weight

```text
(L,T,H; wt(q2); wt(q1),wt(q0); wt(r2),wt(r1),wt(r0))
= (4,1,1; 23; 22,22; 30,30,30),
```

its unique least-weight term is `la^20`, of weight 80.  Therefore, for this
fixed source, fixed axis/cusp, fixed loads `k=nu=0, mu=2/3`, and full
`Q=q2*z^2+q1*z+q0` support, `la^20` lies in the weighted initial ideal and
the coordinate torus has empty special fibre.  There are no further terms
below weight 80 to iterate at this weight.

## Dual AWS custody

- Box03 A/global `dp`: tag
  `max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826T032200Z_box03_A`,
  worker PID `150218`, selected input SHA
  `cafa685fc2219b81180eee892487dd56d5597eaca6dd40dc499bfe46b7b2831e`,
  compiler stdout SHA
  `a0a69d7fafd3329e3b06de67995389e70b003df0d98d56e6f8a3e2704709ff6d`,
  Singular stdout SHA
  `11a85cbd99fbb0a0e3df74063142a211fd535e9adb35acbd685d3b1616a5f7c2`.
- r6d B/`(lp(2),dp(8))`: tag
  `max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826T032200Z_r6d_B`,
  worker PID `217964`, selected input SHA
  `12bc04b6f876974a95d539fc75063800c2de13bd4cf99791f9f1d11455354c2a`,
  compiler stdout SHA
  `d55e6decdc90cab95e7e68950b662505fb90a7d074778a4d44b6b24969f3368b`,
  Singular stdout SHA
  `ca117052f0a11b03517692c376b130fafef20a02c6bd5260e4a325b1882505d4`.

Both workers returned compiler rc 0 and Singular rc 0 with empty compiler
stderr, CAS stderr, and stdout diagnostics.  Each exact check used about 10
MiB RSS and zero swap.  Source closure was checked on each AWS host before
compiler GO; each selected expanded input was separately hash-pinned before
solver GO.

## Firewall

This is an exact obstruction for one charged weight and support mask.  It is
not yet a complete Groebner cone, an all-`q2`-valuation statement, a moving
axis/cusp or moving-load theorem, a formal-lift theorem, a whole double-root
fan result, D1, or JC2.  The next proof-discriminating calculation is the
finite list of strict halfspaces attached to all 37 terms of this explicit
witness, followed by the next omitted normal direction.
