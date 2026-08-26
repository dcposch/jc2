# Preregistration — complete `U=4` terminal moment classification

Date: 2026-08-26 02:36Z

Status: **AWS-ONLY EXACT ENUMERATION; COUNTS NOT PREREGISTERED**

For each `m in {2,4}`, enumerate every unordered signed multiplicity profile
with four support points, equal positive/negative total `D`,
`3<=D<=3m`, positive parts at most `m`, and exact Kummer gcd one.  Normalize
two labelled support points to `0,1`, solve the moment equations through
degree two exactly in a rational quadratic algebra, and quotient the at-most
two solutions by affine transformations and same-sign relabelling.

Every retained class must pass all of the following independent checks:

1. four distinct support points and moments `k=0,1,2` equal to zero;
2. the degree-three moment is nonzero;
3. exact reconstruction of monic coprime `A,B`, with
   `deg(A-B)=D-3` and `A-B` squarefree;
4. the Wronskian identity
   `A'B-AB'=kappa*prod(X-c_i)^(abs(n_i)-1)`;
5. agreement between existence of a collision-free moment solution and the
   weighted-tree criterion `3*gcd(parts)<=D`;
6. canonicalization over every ordered normalization pair, so same-sign
   root relabellings do not inflate the class count.

The output count and class list are deliberately not predicted.  Any failed
identity, criterion mismatch, Python exception, non-AWS host, missing tag,
timeout, or nonzero return is no verdict.  A successful output classifies the
terminal differential equation for `U=4` only.  It proves no lower Faber
tail, Taylor boundary, source landing, `(8,12)`, or JC2 statement.
