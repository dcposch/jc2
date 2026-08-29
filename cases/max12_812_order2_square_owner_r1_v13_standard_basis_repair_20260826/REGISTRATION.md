# Registration: order-two square `r=1` V13 standard-basis repair

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS REPAIR CLIENT.  NO D1, SQUARE-BRANCH, OR
ORDER-TWO VERDICT.**

V13 is a lifecycle root for the normalized `r=1` receiver only.  It pins the
immutable V12 compiler and freeze, compiles the V12 exact source on AWS, and
changes exactly the invalid support block

```text
ideal R1_rad=radical(R1_I);
```

to

```text
ideal R1_rad_raw=radical(R1_I);
ideal R1_rad=std(R1_rad_raw);
```

before any `reduce` membership test.  It also inserts an exact check of

```text
(b1*z+b0)^3 mod (z^2+p/2)
 = b1*(3*b0^2-(p/2)*b1^2)*z
  +b0*(b0^2-(3*p/2)*b1^2).
```

The validator rejects every `// **`, leading Singular `?`, `=FAIL`, nonempty
stderr, missing marker, duplicate marker, timeout, or nonzero engine return.

Run exact Q on one registered AWS host and `F_65521` on a different host,
with 24-GiB virtual-memory, 600-second compile, and 1800-second engine caps.
Exact Q carries the producer statement; the finite field is a software
control.  The only possible producer statement is the grade-thirteen
normalized receiver

```text
ord(A)>=1, ord(C)>=3, ord(R)=1, p*k10!=0  =>  R_lead=0,
```

which is an empty normalized leading section/contact raise, not an empty
square branch.  This package does not compile or consume the V12 unbounded
`d=1` statement.

