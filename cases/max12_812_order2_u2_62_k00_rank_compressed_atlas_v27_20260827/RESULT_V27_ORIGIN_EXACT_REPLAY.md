# K00 V27 auxiliary exact origin replay

Date: 2026-08-27

Lifecycle: **AUXILIARY PRODUCER-CHECKED / UNREVIEWED**.

Two fresh exact Singular processes reconstructed the frozen six-variable
`A`, all seven generators of `B`, and all 90 stored nonzero generators of
`I5(A)`.  Every one reduces to zero modulo

```text
(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1).
```

All 49 entries of `A` also vanish there.  Adding `1` to the first `B`
generator or first stored `I5(A)` generator breaks the origin evaluation, as
preregistered.  Therefore

```text
(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1)=(0,0,0,0,0,0)
```

is an exact rational point of `B+I5(A)`.  For this homogeneous affine ideal,
mere existence of a rational point is thus a trivial target.  The corrected
useful target must require a **nonzero/projective point**, a point in a
specified **source-open** locus, or a point compatible with the **full prior
ideal `P6`**.  This origin check supplies none of those.

The audited r6a run used engine rc 0, Singular 4.3.2, 1.49 seconds wall time,
508,292 KiB maximum RSS, and zero swap.

Custody:

- source freeze: `5387d86e3fc1ceaa77ba9ed938699f160c1795f4e953d054ab2892fde1ac0b5d`
- immutable archive: `fb8c223c38b5a34b05926431ee60e25edceeaf0daff29228b85d999d2c034f5a`
- endpoint: `e9534c0c31b326b17e3c4e183751776529cdf28b6addabed6d3e6ac337ce8096`
- AWS evidence manifest: `de36a93c77a4001d6059aa21d4ed974194d4468400a78a1f1122837c7afac7e4`

Firewall: no nonzero/projective point, source-open point, full-`P6` point,
grade-seven compatibility, rank-pure stratum, jet, arc, closure incidence,
counterexample, or JC2 result is proved.
