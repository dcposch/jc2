# Preregistration: A/B Rees-generator identity

This AWS-only control compares the complete polynomial content of the pinned
factored A input and expanded inverse-B input before any saturation or
elimination.

Pinned inputs:

```text
2b416cb8209dd9d220d8f57ec78044bddb7d83d5ea4899d59ab7b4b6b4f49e52  base_A.sing
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

The AWS compiler extracts exactly `E1,...,E8,LT` from both inputs, emits them
under distinct names in the same exact rational ring, and the AWS Singular
control requires each of the nine differences to be the zero polynomial.  It
runs once in `dp` and once in `(lp(1),dp(8))`.

This test distinguishes a generator-source mismatch from a downstream
saturation/elimination/order issue.  It does not compute a special fibre and
is not a D1 theorem.

AWS cap: r6d, compiler 2 GiB/120 s, Singular 4 GiB/300 s, one process each,
nice 10.  No GO before worker PID/caps are recorded.
