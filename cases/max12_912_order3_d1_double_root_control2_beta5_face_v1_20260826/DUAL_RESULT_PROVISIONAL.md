# Control-2 beta=5 equality face: dual AWS result

Date: 2026-08-26 UTC

Status: **DUAL-ENCODING COMPUTATION COMPLETE; HOSTILE SOURCE REVIEW PENDING.**

## Exact scope

The frozen expanded source is evaluated only at fixed load `mu=2/3`, fixed
support `a-1=h=q2=k=nu=0`, and weight

```text
(la,tau,rho,q1,q0,r2,r1,r0) = (4,1,1,20,20,30,30,30).
```

This is the simultaneous beta=5 equality face for the previously extracted
eight-term witness.  It is not a whole-fan or enlarged-support theorem.

## Independent encodings

### A: direct saturation, global `dp`

- AWS Box02 `34.203.207.55`, tag
  `max12_912_order3_d1_double_root_control2_beta5_face_v1_20260826T025500Z_box02_A`
- worker PID `268278`; 256-GiB cap, 21600-s timeout
- input SHA `cb767f1fe4162a1d992cac145cd744c6d720751b4737e5434f79402bb218ef8a`
- output SHA `cc5a80afce386ff9915d932c2d08ff66e9f3e1661d3ed00c87dc6d1a82952038`
- direct contraction: 420 generators; special fibre: 41 standard-basis
  generators
- elapsed `4:37.93`; maximum RSS `516,588 KiB`; swaps `0`
- exit `0`; compiler stderr, CAS stderr, and stdout diagnostics all empty

### B: double inverse elimination, `lp,dp`

- AWS r6d `100.26.198.153`, tag
  `max12_912_order3_d1_double_root_control2_beta5_face_v1_20260826T025500Z_r6d_B`
- worker PID `212593`; 192-GiB cap, 21600-s timeout
- input SHA `023dc47323a3511a2457048166e50dadc05333b1ae9a9280003d1cb30f43d6eb`
- output SHA `069a3428c77231a7bb079b7e161055f76a061784c218fc19663e3d199d0abf63`
- inverse contraction: 319 generators; special fibre: 41 standard-basis
  generators
- elapsed `2.80 s`; maximum RSS `25,676 KiB`; swaps `0`
- exit `0`; compiler stderr, CAS stderr, and stdout diagnostics all empty

The contraction presentation sizes differ, as expected from the independent
encodings.  After specialization, their displayed reduced bases are literally
the same 41 polynomials up to the position of `s`: A lists `s` first and B
last.  In both bases `la^20` occurs as a generator.

## Exact common endpoint

Both encodings report:

```text
PASS_WITNESS_FACE_MEMBERSHIP
DISPLAYED_RESIDUE_SURVIVES=0
GHT[1]=1
TORUS_FACE_IS_UNIT=1
```

Therefore the exact fixed-weight, fixed-support beta=5 torus special fibre is
empty in both independently constructed encodings.  This closes the beta=5
endpoint for this finite source package; it does not by itself justify a
statement about omitted tail variables, moving loads, neighboring equality
faces, or the entire double-root Newton fan.

## Review gate

Promotion beyond a provisional dual computation awaits a hostile audit of the
expanded-source provenance, both contraction/special-fibre constructions,
the equality of specialized bases, torus saturation semantics, and the scope
firewall above.
