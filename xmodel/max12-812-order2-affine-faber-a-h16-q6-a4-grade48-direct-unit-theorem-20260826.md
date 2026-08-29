# Affine-Faber `A`: fixed H16 equality-wall direct unit

Date: 2026-08-26

Status: **PRODUCER-TIER THEOREM; HOSTILE REVIEW REQUIRED.**

## Theorem

Work over a characteristic-zero complete DVR with uniformizer `s` in the
fixed integral delayed-load source family

```text
H=ord_s(lambda)=16,
q=min(ord_s X,ord_s Y)=6,
ord_s(a)=4,
```

with the complete moving-discriminant graph substitutions registered in the
V4 and V6 producer packages.  Let `P1,...,P7` be the seven complete raw
ordinary-Faber source rows, including their typed targets.  On `D(p*m)`, where
`p=E(0)` and `m=M(0)`, the simultaneous vanishing of their coefficients
through absolute grade 48 is impossible.

## Proof

Form the two row-series combinations

```text
F=P7-E(s)^2 P3/32+E(s)^3 P1/64,
G=E(s)^2 P3+16 E(s) P5+96 P7.
```

These are literal linear combinations of raw source rows over the source
coefficient ring.  Complete exact-Q coefficient extraction from the frozen
tails gives

```text
[s^48]F
 = (3/32)a p^2m^2r0 -(3/32)a p^2y^2
   -(1/16)a p^4d2 +(3/128)a p^6d6 -(1/64)p^2m^3,

[s^48]G
 = 3a p^2m^2r0 -3a p^2y^2
   -2a p^4d2 +(3/4)a p^6d6 -(5/2)p^2m^3.
```

Therefore

```text
[s^48](G-32F)=-2p^2m^3.                            (1)
```

If every raw row coefficient through grade 48 vanishes, then the coefficient
of every source-series multiple of those rows through grade 48 vanishes; in
particular the left side of (1) is zero.  On `D(p*m)` its right side is a
unit, a contradiction.  This argument needs neither the grade-44 predecessor
elimination nor the projective `D(x),D(y)` split.

Target timing is explicit.  Rows `P1,P3,P5` have no affine target.  The
`-J/4` in `P7` contributes `-J/4` to `F` and `-24J` to `G`, but the registered
source target begins at grade 57, so it does not enter (1).  The load terms
and all moving center, tangent, kernel, complement, and transverse-deviation
jets retained by the source map are present in both exact extractions and
cancel in (1).

## Custody

First functional:

```text
RESULT   3b99f6f198b8e149fbebac443ce4c59faed4fd2289275c6b4680cc673ed790bb
EVIDENCE 922e10cab6f8b4b9ad9db45898721c68e4f6829b6e1e69ee2a51918cc4d89667
FREEZE   1a9411e67f2ef2efed48efffaf2afb066f2a5e8ab97d3ca5fe458693cbefaef6
Q sparse d71d23a8d88add84dc5e579b1fdcc3570fdde71c6d77440b68c5495f178f1386
```

Secondary functional:

```text
RESULT   02a005dd4bac2db1ef891a55d4377148ce4a485ea0d61d9dd4bc73da541863af
EVIDENCE 7524ed35265f551ea03034b16279bd219d243f3225e3764748166208e758c5c8
FREEZE   3b8c42ba206668298c65e725bc640461665c2aeacdf19128dc8499939f69ef94
Q sparse da16e1ce0a309f6fde5d280493f162f88b1ba4317f80219e2e1e407ca771a264
```

Exact Q is evidence; `F65521` is a software and support control.

## Scope firewall

This theorem closes only the displayed fixed integral H16 equality
representative in the internal moving-discriminant source graph on `D(p*m)`.
It does not prove rational-regrading invariance, all rational equality walls,
neighboring `H,q,a` cones, literal total-Rees coverage, factor-degenerate
opens, order two, maximum twelve, or JC2.
