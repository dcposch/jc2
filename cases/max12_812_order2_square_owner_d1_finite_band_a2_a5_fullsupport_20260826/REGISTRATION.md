# Registration: order-two square D1 finite band `a=2..5`

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS PRODUCER; NO ENDPOINT YET.**

## Objective

Repair the source-support defect in the quarantined symbolic-D1 V12 client by
checking four fixed contacts

```text
ord(A)=a,  ord(C)=a+1,  ord(R)>=a,  a in {2,3,4,5}
```

on the reviewed generic-square first-normal chart `D(p*k10)`.  Each fixed
contact is compiled directly from all seven frozen Faber tails, all three
load summands `k10,k6,k2`, and all four charged target rows.  No symbolic
`theta=sigma^n` extrapolation is allowed.

For each `a`, consume exactly the two absolute grades

```text
g=11+2*a,  g+1=12+2*a.
```

The compiler must prove:

1. the complete seven source rows are divisible through grade `g` and their
   successive quotients are exact;
2. no `k6`, `k2`, `mu2`, `mu4`, `mu6`, or `J` coefficient occurs through
   grade `g+1` (this is a checked output, not an assumption);
3. both grades equal the moving lower-unitriangular Faber image of the exact
   Laurent receiver, including moving `p`, first `A/C` corrections, the
   `r=a` `RC` term, and the exceptional `a=r=2` `R^3` term;
4. the first grade has denominator `L=z^2+p/2`, the next has denominator
   `L^2`, and the recurrence/numerator identities hold exactly;
5. on both root allocations of squarefree `L`, the first numerator vanishes
   and the next numerator has the nonzero `C^2` value
   `(3/2)*lambda^2*cv^2`.

The coefficient `eta` represents the grade-`a` section of `R`: arbitrary
`eta` covers `r=a`, while `eta=0` is precisely the truncation seen through
grade `g+1` when `r>a`.  This is a finite truncation statement, not an
unbounded valuation substitution.

## Frozen ancestry

```text
e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py
34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/FREEZE.sha256
997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114
  xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md
40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94
  xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md
3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95
  xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md
```

The transitive frozen common-tail hashes are rechecked by the imported
compiler before any output is written.

## AWS lanes and acceptance

Run independently over exact `Q` and `F_65521`, on distinct registered AWS
hosts, each with a 24-GiB virtual-memory cap, 600-second compile cap, and
1800-second Singular cap.  Timeout, nonzero return, any missing/duplicate
marker, any `=FAIL`, `// **`, leading `?`, or `error occurred` diagnostic is
no verdict.

Exact `Q` is the characteristic-zero producer.  `F_65521` is an independent
software control.  Even dual PASS is producer-tier until hostile review.

## Firewall

This package can eliminate only the four normalized finite D1 contacts
listed above, subject to the already-reviewed first-normal/half-weight
hypotheses.  It does not cover `a>=6`, positive-order `k10`, `p=0`, `k10=0`,
zero/infinity sections, arbitrary fan faces, scheme structure, the full
square branch, order two, `(8,12)`, maximum twelve, or JC2.  In particular,
it makes no blanket square-forcing assertion in the all-load problem; the
Chebyshev/Pell lower-load survivor is outside these two early grades and is
an expected control for later complete-support clients.

