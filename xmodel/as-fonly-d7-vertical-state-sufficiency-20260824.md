# AS F-only `p=3,D=7`: vertical D8 state-sufficiency theorem

**Status: PRODUCER EXACT; PORTABLE REPLAY PASS; SOURCE INTERPRETATION
PROVISIONAL PENDING REVIEW OF THE CORRECTED CENSUS PACKAGE.**

## Headline

The corrected vertical D8 `7 x 5` affine digit system has an exact
two-polynomial state description.  Over any field, its five current-digit
unknowns can be recovered from two adjugate numerators when
`Delta=A^2+h^3*B` is nonzero; the two degenerate `Delta=0` strata have explicit
one-line criteria.  The degree caps on the recovered quotients are essential.

An independent literal-F3 replay compares this criterion with direct Gaussian
solvability at all `3^13=1,594,323` corrected assignments.  It matches all
`314,127` compatible assignments and the complete fibre histogram with zero
mismatches.  Dropping the quotient-degree caps creates exactly `202,176`
false positives.

This is a state-compression theorem for the displayed corrected vertical row.
It does not advance the next divided carry by itself and makes no all-depth,
lift/no-lift, characteristic-zero, counterexample, or JC2 claim.

## 1. Licensed source and lifecycle

This gate consumes the source-corrected producer

```text
xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md
SHA-256 9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8

cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/generate_corrected.py
SHA-256 a71daa0cb525bac229afb91c76987c8f25c1e2d63683caa10ff45d3364c658e5

cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/audit_corrected_frobenius_rows.py
SHA-256 77485e9d583dd621c8ae412fa70bab3c2aa5b7605bebe03e0b74a3c4dc87689c
```

The omitted-Frobenius erratum is different-model confirmed at

```text
xmodel/as-fonly-d7-postd10-d98-f3-erratum-review-grok-20260824.md
SHA-256 c97330558a53ad3caa82d1bf53f642f68139d453edbe96f541a55eece331ad8a
```

At this freeze, the corrected census producer's own different-model review is
still active.  Consequently the algebra below is unconditional for the
displayed matrix and column, while its interpretation as the exact AS
successor remains conditional on that source review.  The quarantined old
post-D10 counts and affine columns are not used.

## 2. The polynomial state theorem

Let `k` be a field and write `k[z]_{≤d}` for the polynomials of degree at
most `d`.  Take

```text
A=P+Q*z,                    deg A<=1,
B=(s+w*z)*(R+T*z),          deg B<=2,
H=h^3 in k.
```

The corrected vertical core is the coefficient matrix of

```text
M : k[z]_{≤2} ⊕ k[z]_{≤1} -> k[z]_{≤3} ⊕ k[z]_{≤2},
M(X,Y)=(-A*X+B*Y,-H*X-A*Y).                         (1)
```

Put

```text
Delta=A^2+H*B,
Msharp=[[-A,-B],[H,-A]].                            (2)
```

For a target `(u,v)` in the codomain define

```text
NX=-A*u-B*v,
NY= H*u-A*v.                                        (3)
```

Then `M(X,Y)=(u,v)` is solvable under the displayed degree caps exactly as
follows.

1. **`Delta!=0`.**  Both `NX` and `NY` are divisible by `Delta`, and the
   quotients satisfy

   ```text
   deg(NX/Delta)<=2,  deg(NY/Delta)<=1.              (4)
   ```

   The unique solution is `(X,Y)=(NX/Delta,NY/Delta)`.

2. **`Delta=0` and `H!=0`.**  The single polynomial relation

   ```text
   H*u-A*v=0                                         (5)
   ```

   holds.  A capped solution is `Y=0`, `X=-H^-1*v`.

3. **`Delta=0` and `H=0`.**  Since `k[z]` is a domain, `A^2=0` forces
   `A=0`.  If `B!=0`, the criterion is

   ```text
   v=0 and u=B*Y for some deg Y<=1.                  (6)
   ```

   If `B=0`, the criterion is simply `u=v=0`.

These cases are disjoint and exhaustive.

### Proof

Direct multiplication over `Z[A,B,H]` gives

```text
Msharp*M=M*Msharp=Delta*I.                           (7)
```

If `Delta!=0`, (7) proves necessity of (4).  Conversely, let `(X,Y)` be the
two quotients in (4).  Then `Msharp(u,v)=Delta(X,Y)`.  Multiplying by `M` and
using (7) gives

```text
Delta*M(X,Y)=Delta*(u,v).
```

Cancellation in the domain `k[z]` proves sufficiency; the quotient bounds are
exactly the source caps.

If `Delta=0,H!=0`, (7) gives the necessary relation (5).  Conversely set
`Y=0` and `X=-H^-1*v`.  The second coordinate of (1) is `v`; relation (5)
makes the first coordinate `A*H^-1*v=u`.  Since `deg v<=2`, the cap on `X`
is automatic.

If `Delta=H=0`, then `A=0` and (1) becomes `(X,Y)->(B*Y,0)`, proving (6) and
the zero-matrix subcase.  This also proves the geometric ranks `5,3,2,0` on
the four respective strata and explains why ranks one and four do not occur.

The portable formal replay checks (7) coefficient-free over the integers.

## 3. Exact corrected-F3 comparison

For every structural base

```text
(P,Q,R,T,s,w,h) in F3^7
```

and every corrected degree-six Frobenius choice

```text
(fua,fa,fb,fc,fd,fvb) in F3^6,
```

the replay regenerates the source matrix and inhomogeneous column from the
frozen corrected producer.  Since its affine equations are `M(X,Y)+b=0`, it
applies the theorem to target `(u,v)=-b` and independently compares the result
with direct rank equality of `[M|-b]`.

The exact stratum totals are

```text
state stratum                         all points   compatible
Delta!=0                              1487160       305208
Delta=0, H!=0                           48114         6642
Delta=0, H=0, B!=0                      46656         1404
Delta=0, H=0, B=0                       12393          873
total                                  1594323       314127.       (8)
```

The structural fibre histogram is exactly

```text
compatible Frobenius choices   structural bases
0                                  12
3                                  36
9                                  16
81                               1904
729                               219.                              (9)
```

There are zero theorem/direct-rank mismatches.  The inherited direct-rank
stream and the new state stream have hashes

```text
rank stream   e86fd1ec2724b5089039378c07e1a19a089042eeb4172b0342474f85d4d8b23d
state stream  98b9395a186f04acd1db001fe5457fa5dca8c5bd8d5c2c3d6e52df79f8981f77. (10)
```

## 4. Load-bearing cap negative control

On `Delta!=0`, requiring only `Delta|NX,NY` but omitting the quotient caps in
(4) accepts exactly `202,176` incompatible points.  Their quotient-degree
patterns are

```text
(deg X,deg Y)   count
(-1,2)           1968
(0,2)            2208
(1,2)            9648
(2,2)           28944
(3,-1)           4320
(3,0)            3456
(3,1)           15552
(3,2)           54432
(3,3)           23328
(4,2)           34992
(4,3)           23328.                            (11)
```

Here degree `-1` denotes the zero polynomial.  Thus the adjugate divisibility
classes alone are not the bounded state: the two quotient endpoint caps are
load-bearing.  This is the registered negative control for every successor.

## 5. Replay and refusal scope

Portable case:

```text
cases/as_fonly_d7_vertical_state_sufficiency_20260824/
```

One-command replay:

```sh
cd cases/as_fonly_d7_vertical_state_sufficiency_20260824
./replay_all.sh
```

The replay uses Python 3 only.  It verifies the formal adjugate identity,
regenerates the corrected matrix and column, exhausts all literal-F3 points,
checks every state criterion against direct Gaussian rank, checks both stream
hashes/counts, and verifies the package manifest.

The field-theoretic criterion in Section 2 applies over arbitrary fields to
the displayed matrix.  The census in Sections 3--4 classifies literal F3
points only; it is not an algebraic-closure classification of the corrected
inhomogeneous family.  No later divided carry has been imposed.  No statement
here proves the full cap-seven tower empty or nonempty, constructs a lift,
algebraizes a formal branch, produces a counterexample, or decides JC2.
