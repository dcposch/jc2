# Correction delta — one-P0 nested-U2 semilinear family record R1

Date: 2026-08-29  
Producer: Sol 5.6 coordinator delta after independent Opus 5 review  
Status: `CORRECTED_RECORD_INTERFACE`; the sealed R1 producer is preserved
unchanged as evidence.

## 0. Custody and verdict

This delta corrects exactly one record field in
`xmodel/m2-u2-one-p0-semilinear-family-record-r1-sol56-20260829.md`, full
SHA-256
`19fcd0133c72eba01dc4a554638111760a8813231a3b983a752d7d7528f58f82`,
body
`ce5cf26906d3c736e75c791c3600be201b65279aabbbacbf0b12014d51497c29`.
The independent Opus 5 review is
`xmodel/m2-u2-one-p0-semilinear-family-record-r1-hostile-review-opus5-20260829.md`,
full SHA-256
`84c648a721f42d8197a9c78648795e9830e5bb75521a3e00a8a9d5a80f495cb6`,
body
`11bcc272d379622cc0105f50a7351fc728f4609f87e7e711cf8bf7a28d40b06c`,
verdict `PASS_WITH_REPAIR`.

The family theorem survives.  In every conforming consumer, replace

```text
inner_u2.dq = 4
```

by

```text
inner_u2.dq = 3.
```

The old value is not an alternate convention.  It is the illegal
eta-not-absorbed `nu=1` degree and must never enter a canonical family key.

## 1. Five exact checks

At the inner U2 vertex

```text
nu=1, r=2, mu=3, L=1, dp=6, kbar=3, rho=1, w=2, M=3.
```

The absorbed normal form gives `dq=r+L=3`.  Independently,

```text
gcd(dp,dq)=gcd(6,3)=3=M,
mu | M,
E=mu*dq-dp=3=mu*L,
rho=kbar/dq=1,
D=rho*degp=6
```

in primitive full-index normalization.  The rejected value `dq=4` would
instead give `M=2`, `E=6`, `rho=3/4` from the displayed fields, and would
falsely fail the required arrival divisibility.  No formula downstream of
R1 used the displayed `4`; the repaired `t=5`, `K=6q+1` ray, its N1/L6
classification, edge transport, full degrees, and semilinearity are
unchanged.

## 2. Corrected minimum record fragment

The R1 record is consumed only after applying this delta:

```text
inner_u2 = {nu:1,r:2,mu:3,L:1,dp:6,dq:3,
            kbar:"3/1",rho:"1/1",w:"2/1",M:3,lambda:0}
n1_certificate = {
  kbar_mod_nu:"2",
  reason:"t and K odd imply gcd(2,t*K)=1"
}
coverage_debt += ["absolute_index_or_prod_nu_bound"]
```

The last two lines adopt the review's safe interface narrowing.  Full
`i`-synchronization proves the primitive ratio
`(i0,i1,i2)=(1,2,2tK)`; it does not prove that the absolute index or
`prod(nu_seg)` is unbounded at a fixed source entry.  Any future theorem
bounding either quantity can cut the ray to a finite prefix.

## 3. Maximum safe result after repair

For the labelled route

```text
inner U2 -- case II, l=3 --> neutral P0
         -- case I, h=3 --> outer U2,
```

the old `t=2`, `nu=tK` ray is dead for every `K=6q+1` by N1/L6:
`gcd(4K+2,2K)=2`.  The repaired route passes the reviewed local arithmetic,
ODE, T1 and full-degree-ratio predicates exactly when
`t=5 mod 6` and `K=1 mod 6`.  For every fixed admissible `t`, it is one
semilinear family; allowing `t` and `K` to vary introduces the bilinear
product `nu=tK` and is not one semilinear family.

This is a formal labelled-route theorem.  It proves neither source landing,
coefficient gluing, absolute-index unboundedness, polynomial realization,
a finite or infinite complete configuration book, a degree ceiling, a
counterexample, nor JC2.

*End of sealed correction body.*

## Seal

- Body byte count: `3255`.
- Body SHA-256:
  `2ac65012d3ca3a56feef184d42b374525f8a1e5767914ca46674df18ed53d20f`.
