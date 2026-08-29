# K00 rank-five / grade-three rank-at-most-one coordinator integration

Author: Sol 5.6, campaign coordinator  
Date: 2026-08-29  
Frozen basis: `92ebe92ad5986a47f01af9ed901260595dfed869`  
Lifecycle: **PROMOTED WITH THE REPAIRS BELOW**

## Verdict and custody

Fable 5 independently reconstructed both provisional K00 branches from the
frozen literal sources and returned `PASS_WITH_REPAIR` separately for each:

```text
review full SHA-256 = 4dbd356a8a34c4dfb057db77fdb1eea424426b20439c27a96067fb6ce0a02b37
review body bytes   = 29665
review body SHA-256 = b3dd864afaf5878fd079fc202da5ee7e89f53bc35bc353ff3eab1a0a4cb86b9f
run final status    = DONE / exit 0 / charge_basis ABSENT
```

The charged producers are Sol's rank-five report
`0a3af03ed8d07db852f833d0dc9ebe3ec151934308f4a139cf7ac72124f9b3cb`
(body `5c0397492ad5a739944343686407a909a17d0e7cc37555cb18221ba40548e200`)
and Grok's rank-at-most-one report, whose ordinary full-file hash is
`e0947368509714aa96376789914a4dbfd7141b1f77832016bf4dbe7c3caa45e4`
(body `33c9ff079d97933b3c2f59984e2593f4ee70111de8174b0fda063eeb3f08f2dc`).
The latter report's embedded `3e2b13b2...` digest is only its explicitly
declared zero-field self-hash convention, not its ordinary file identity.

The review's final generic-source ledger is misheaded `charge_basis` because
the lane prompt requested that wording.  It contains no `charge_basis=` exit
declaration, the runner correctly records `charge_basis=ABSENT`, and no exit
price is asserted.  This prompt/citation slop has no mathematical effect.

## Promoted exact algebra

Work over
`R=Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1]`.  Let `A` be the frozen `7 x 7`
newest-variable matrix, let `B2=(q1,...,q6)` use the six nonzero literal
grade-two rows `(1,2,3,4,5,7)`, and put `B=B2+(F10)`.  Here `q6` means
literal row 7, not the older zero logical slot named `Q6`.

The literal `5 x 5` census is 441 total, 351 zero and 90 nonzero.  The
nonzero minors form exactly two rational-scalar classes: 36 copies of the
`W` class and 54 copies of the `M` class, containing respectively 23 and 31
distinct exact polynomials.  Independently checked exact memberships give

```text
W in (q1,q3,q4),
M in (q1,q2,q4,q6),
I5(A) subset B2 subset B.
```

The review also directly replays `I4(A),I3(A) subset B`.  Hence, as ideal
containments rather than radical statements,

```text
I5(A), I4(A), I3(A) subset B,
J2 := B+I3(A) = B,
rank(A) <= 2 on every geometric point of V(B).
```

Since `B subset P6`, the correct variety inclusion is
`V(P6) subset V(B)`.  The review once prints the arrow backwards in section
3.3; this integration repairs that text.  The rank-three, rank-four and
rank-five loci are empty on `V(B)`, hence also on `V(P6)`.

For grade three write

```text
P3(x,u)=C(x)u+c3(x),       C=A[:,1..6],       E3=[C|c3],
J1=B+I2(A),                R1=J1+I2(E3),
J0=J1+I1(C),               R0=J0+(c3).
```

The reviewed rank-at-most-one calculation gives

```text
R0=J0=(2*d3_1-d5_1, d2_1-d4_1,
       16*d1_1-d5_1, d0_1-2*d4_1),
sqrt(R1)=J0.
```

`J0` is the reduced two-plane

```text
Pi: (d0_1,d1_1,d2_1,d3_1,d4_1,d5_1)
      = (2s,t/8,s,t,s,2t).
```

All 49 entries of `A`, including its quadratic seventh column, and all
entries of `c3` vanish modulo `J0`; consequently `P3=0` there for every
`u=(d0_2,...,d5_2)`.  Conversely, over an algebraic closure, a grade-three
solution on the rank-at-most-one base lies in `V(R1)=V(J0)`.  Thus the
rank-exactly-one compatible locus is empty and the rank-zero compatible
locus is exactly `Pi`, with every `u` free.

## Maximum composed theorem

Combine the preceding reviewed results with the already promoted
chart-free rank-two equality

```text
sqrt(B+I3(E3)) = sqrt(B+I2(A)).
```

Every point of `V(B)` has rank at most two.  If it solves `P3=0`, then
`rank(E3)=rank(C)<=2`, so it lies in `V(B+I3(E3))`; the radical equality
forces rank at most one, and the preceding theorem forces the base point
onto `Pi`.  The converse holds identically.  Therefore, set-theoretically
over an algebraic closure,

```text
V(B,P3_1,...,P3_7) = Pi x A^6_u.
```

This is the complete grade-three compatible incidence over the leading
base.  It is not an equality of the displayed defining ideals: in
particular `R1` can retain nilpotent thickness although
`sqrt(R1)=J0`; only `R0=J0` is promoted as an ideal equality.

## Binding repairs, stops and frontier

- The rank-five producer's hashed membership column comes from the `std`
  lift path, not the printed `slimgb` invocation.  Fable regenerated and
  checked every coefficient; the theorem is unchanged.  The old 6,985-byte
  scratch transcript was not archived, so future certificates must archive
  serializations or the complete generating script.
- In the rank-at-most-one producer, `I1C_NCOLS=20` is the count after
  proportionality simplification; the plain 42-slot ideal has 36 nonzero
  entries.  Replace the insufficient sampling prose by the independently
  checked normal forms `I1(A) subset J0` and `(c3) subset J0`.
- Keep the labelled/stored distinction: there are 1,225 labelled `3 x 3`
  slots, 412 zero and 813 nonzero; some Singular builds store only the 813.
- Fable's new two-minimal-prime decomposition of `J1` and its stronger
  exact-minimal-power observations originated inside the review.  They are
  not needed here and remain provisional pending separate review.

Stop all rank-three, rank-four and rank-five Fitting/localizer jobs, all
rank-two charts already stopped by the prior theorem, and every selected
rank-one `I2(E3)` chart.  Do not relabel historical capped jobs.  The only
live K00 branch after grade three is the literal grade-four system over
`Pi`, retaining `k10_0 != 0` at the first grade where it occurs.  Opus's
sealed primary on that branch is producer evidence only until a different
model replays it.

No later-grade lift, full `P6` solution, normalized source point, finite
jet, arc, K00-closure point, Keller pair, counterexample, order-two or
maximum-twelve exclusion, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6036`.
- Body SHA-256: `f288a1213feef1ca8c290fe08472b99a0cf90106738c947b84b41a249af148f1`.
- Frozen basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
