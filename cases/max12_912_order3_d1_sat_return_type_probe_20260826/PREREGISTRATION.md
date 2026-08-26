# Preregistration: Singular `sat()` return-type control

Purpose: test, on AWS and against the installed `elim.lib`, the exact semantics
of direct ideal assignment and the documentation-mistyped pattern
`list L=sat(I,J); ideal C=L[1];`.

Frozen toy ring and ideals:

```singular
ring Rdp=0,(s,la,tau,rho,q1,q0,r2,r1,r0),dp;
ideal I=s*q1,s*q0;
ideal J=s;
```

The mathematical saturation is `(q1,q0)`.  The run must print the type and size
of the direct result, the type and size of the list-coerced result, and the
normal forms of `q1` and `q0` modulo both the direct ideal and the ideal formed
from `L[1]`.  It repeats the same control in the exact A-fast block order
`(lp(1),dp(8))`.

Success semantics:

- `sat(I,J)` assigned directly to an ideal has two generators and kills both
  `q1` and `q0`;
- list coercion must produce a one-element list whose first entry is the entire
  ideal, not a polynomial; the direct ideal and `L[1]` must reduce to zero
  against each other in both directions;
- `sat_with_exp(I,J)` is tested separately and must have documented list
  structure `(ideal, exponent)`.

This is a software/API control only.  It is not a mathematical D1 endpoint and
does not itself adjudicate the A-fast/B discrepancy.

AWS registration (to be completed before `GO`): r6d, at most 1 GiB virtual
memory, one Singular process, timeout 120 seconds, nice 10.
