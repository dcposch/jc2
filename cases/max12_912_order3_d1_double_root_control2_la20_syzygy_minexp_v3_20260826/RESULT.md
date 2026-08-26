# Minimum individual saturation exponent for the `la^20` witness

Date: 2026-08-26 UTC

Status: **EXACT AWS CERTIFICATE COMPLETE.**  This corroborates and shortens the
already hostile-reviewed V2 witness; it does not enlarge its mathematical
scope.

## Custody

- AWS Box03 `98.80.65.144`
- tag `max12_912_order3_d1_double_root_control2_la20_syzygy_minexp_v3_20260826T023300Z_box03_LPDP`
- worker PID `142191`; solver PID `142340`
- 64-GiB cap; 21600-s timeout
- compiled source SHA
  `c47c5d30db898f7fdc775ba45565b00d5bca545d384fe24ea15345bf23166de9`
- stdout SHA
  `7443e30c68d1cbe415a16eb29278d066ba022d990d229acd0ba2d36a30d15a5f`
- exit `0`; compiler stderr, CAS stderr, and stdout diagnostics all empty
- elapsed `14:14.09`; maximum RSS `13,115,888 KiB`; swaps `0`

## Exact endpoint

The global saturation exponent used to construct the contraction remains 96.
For the single used contraction generator giving the target witness, exact
reductions of `s^m*g` modulo `std(I)` were tested successively from `m=0`.
The first zero reduction occurs at

```text
INDIVIDUAL_SATURATION_EXPONENT=80.
```

The run then lifts that `s^80*g` to the original nine Rees generators and
checks the resulting identity literally.  Dehomogenizing at `s=1` gives the
same witness as V2:

```text
W = la^20*tau + la^20
  + (1/243)*q1*q0^3
  + (1/54)*q1*r2*r1
  + (7/108)*q1*r1^2
  + (1/54)*q1*r2*r0
  - (1/54)*q0*r1*r0
  + (1/108)*q1*r0^2.
```

Thus exponent 80 is minimal for this particular used contraction generator
under the preregistered successive-reduction test.  Minimality is not needed
for the dehomogenized membership theorem, and no claim is made that 80 is a
global saturation exponent or a fan invariant.
