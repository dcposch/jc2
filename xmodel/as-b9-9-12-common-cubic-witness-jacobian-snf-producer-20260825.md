# Producer report: common-cubic witness Jacobian, Smith profile, and kernel

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER; DIFFERENT-MODEL REVIEW PENDING**

## Source-typed object

At the one literal normalized `(9,12)` common-cubic witness with SHA-256
`a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`,
the source rebuilds the exact integer Jacobian of

```text
276 determinant coefficient equations
+ 10 equations P9 = P_(0,9) H^3
+ 13 equations Q12 = Q_(0,12) H^4
= 299 equations
```

in the 55 coefficients of `P`, 91 coefficients of `Q`, and the three
non-monic coefficients of
`H=y^3+h1*x*y^2+h2*x^2*y+h3*x^3`.  The compiler source has SHA-256
`f8d1a0008fc7ccaec0ca1e4fde893f42df6105069a02b2fab01583755c192911`.
The canonical matrix payload and deterministic gzip have SHA-256
`0202da0d68e4dd7cd6998751469f0d3d6ae6facc66bd18bc88d80fead8823f36`
and
`65eb73affe9e8217607650e932f0c71ae243949aac26703474045da5a6adebaf`.

## Exact rank and Smith data

The `299 x 149` matrix has

```text
rank over Q      = 146
rank over F3     = 94
Q-right nullity  = 3
F3 tangent dim   = 55.
```

The complete 3-adic Smith valuation histogram is

```text
v3 : count
 0 : 94
 1 : 29
 2 :  8
 3 :  1
10 :  3
11 :  7
12 :  2
13 :  2.
```

Two distinct conditioning numbers must not be conflated:

- the valuation of the maximal-rank determinantal ideal, equivalently the
  sum of the 146 Smith valuations, is `205`;
- the largest individual Smith valuation is `13`.

The first number controls the classical square-minor inequality.  The second
may control a sharper Smith-coordinate/right-inverse theorem only after
local row-ideal generation and the 153 left-cokernel compatibilities are
certified.  This producer proves no such sharper theorem.

## Exact failure of the classical maximal-minor shortcut

Among row subsets whose residuals all vanish to at least a common precision,
the largest precision retaining rational Jacobian rank 146 is `N=11`.
Every rank-146 minor has determinant valuation at least `205`.  Consequently
no full-rank square minor at this representative can satisfy the classical
inequality

```text
N > 2 v3(det minor),
```

since even the optimal determinantal-ideal lower bound would require
`N>410`.  The explicitly selected replay minor has valuation `350` and its
selected residual threshold is `11`, providing a direct negative control.

This is failure of that criterion at this witness, not failure of lifting.
In particular, `13` is not silently replaced by `205` as a universal Hensel
radius: a Smith-coordinate route might have a threshold near `2*13`, but its
extra hypotheses are presently open.

## Exact rational-kernel classification

Independent source `classify_kernel.py` (SHA-256
`c10e01d13c74ff1ae4bc2a769139abe44e442edf53ae9be8b8c27d1c63bc87fb`)
computes the rational right kernel and proves that it is exhausted by the
three independent source-defined target gauges:

1. constant translation of `P`;
2. constant translation of `Q`;
3. the lower target shear `Q -> Q+tP`.

The shear is degree-compatible because `deg(P)<=9<12`; it preserves the
determinant and the displayed degree-12 common-core equation exactly.  Thus
after these exact gauges there is no rational right-kernel direction at this
integer representative.  This does **not** quotient the 55-dimensional
mod-3 tangent kernel.

As a useful negative control, the target scaling direction
`(delta P,delta Q)=(P,-Q)` is not in the exact rational kernel: it has 14
nonzero images, all in the common-core rows and all divisible by `3^11`.
That is expected because the stored representative solves those rows modulo
`3^11`, not literally over the integers.  Kernel result SHA-256 is
`92593c04c9fc1b439a7d3975a75b2e5840b170f9cc0289569bdcba9d1e18d90c`.

## Custody and refusal scope

The r6d primary completed rc0 in 3m37.34s with maximum RSS 261,384 KiB.
Machine-result SHA-256 is
`d1c1ed60daf3a8f3c3c464c4e8b16c2de706623ba6184af791ebf0039716e381`.
The kernel classification completed rc0 in 0.09s with maximum RSS 31,988
KiB.  A Box03 replay of the same pinned source completed rc0 in 3m36.10s
with maximum RSS 261,084 KiB and reproduced both the result and matrix bytes
exactly (`d1c1ed60...` and `65eb73af...`).  This is an independent-host
custody replay, not an independent source implementation.  The launcher's
PID metadata landed one directory above the job because of shell grouping;
the case preserves the copied outer PID and process snapshot, and the solver
cwd, source closure, output, timing, and rc are unaffected.

Exact scope is one displayed normalized common-cubic mod-`3^11` witness.
There is no local row-ideal-generation theorem, Smith-coordinate Hensel
theorem, all-depth lift or exclusion, full-family result, maximum-twelve
theorem, counterexample, or JC2 conclusion.
