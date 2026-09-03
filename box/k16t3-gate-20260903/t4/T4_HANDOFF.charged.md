# t=4 computation handoff (K=16 ray)

Status in this note is typed deliberately.  A finite-field unit basis is
`MEASURED-MODULAR`, not a characteristic-zero theorem.  The order chart is a
necessary superset because the tuple-level Laurent bridge is not imposed.

## Correct chart and gauge

For `t=4`,

```text
(n,m;M2,V2)=(52,36;49,3),  (e,q)=(13,9),
Phi=(delta2,delta1)=(-1,4/13),
delta1=t/(3t+1)=4/13,
ord(C_i) >= -i/13.
```

The two-disc coefficient spaces have dimensions

```text
[1,1,1,1, 2,2,2,2, 3,3,3,3, 5]
```

with bases `[1]`, `[1,A]`, `[1,A,B]`, and, at `i=13`,
`[1,gamma,A,B,z]`, respectively.  Here

```text
z=pi-gamma,
B=pi*z+b1*pi+b2,
A=pi*B+b3,
h=pi*A+b4.
```

Important audit correction: the middle triangular target gauge is
`alpha_(e-q)=alpha_t=alpha_4=0`, not `alpha_2=0`.  Indeed `alpha_4` multiplies
`h^(13-4)=h^9`, which aligns with the leading `h^9` of `Q`.  The other two
gauges are `const(beta_9)=0` and `const(alpha_13)=0`.  The initially generated
alpha_2-gauged inputs and their interrupted runs were discarded; none of
their hashes or timings below is used.

The correct chart has 48 unknowns including `c` before these three gauges and
45 after them.  The Singular ring has those 45 chart variables followed by
the Rabinowitsch variable `T`.  The main ideal has 65 Jacobian-coordinate
generators plus `T*c-1`.  Its bands are `h^0` through `h^17`; equation degrees
are

```text
degree 1: 1, degree 2: 6, degree 3: 30, degree 4: 28.
```

Correct-gauge generator text is 18,221 bytes.  The exact h-adic numerical
reconstruction and the independent actual-pair negative-classifier control
both pass.  Audit file: `t4_audit.out`, SHA-256
`7c6e9cf40c6d5f6ebe613a30ee321d309e25237bd9b5037dc6d84b2ff2c34607`;
25.32 s, 152,280 KiB, exit 0.

Driver: `t4_order_system.py`, 11,309 bytes, SHA-256
`db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee`.
The exact-Q generated input is 19,933 bytes, SHA-256
`7fb0b7bc4c801cc75a40d113cffb1ea1085e3ea1f6f274c9a3ed3664d87b5e47`.

## Wrapper and actual-pair controls

Every full main input uses `T*c-1` and passes the Rabinowitsch empty and
nonempty wrapper controls in its declared ring.  The separate
`sat_wrapper_controls.sing` makes the FALLACY-v2 extraction completely
explicit: in each of `GF(32003)`, `GF(65521)`, `GF(1000003)`, and `Q`, it
uses `list L=sat_with_exp(...); ideal S=L[1]`, asserts the list/ideal types and
the exact `nameof(basering)`, and runs both signs of the wrapper control.  All
16 checks pass.  Input SHA-256 is
`2668b0da920001ddcff0b5791cc3e3785e55b17ccb1c5dc8a80d9ffc2184cb81`;
output SHA-256 is
`acdfe5c579fb0ee7c54f9dd794746f1c09cc0e035fee29212d7c95807f08f13d`;
0.02 s, 11,628 KiB, exit 0.

The actual-pair control is `(pi,pi-gamma^2/2)`: it is monic of pi-degrees
`(1,1)`, has Jacobian `gamma`, and has the two reciprocal anchor degrees
`(2,2)`, but fails the K=16 four-tuple classifier.  It is not promoted to a
target witness.

## Several-prime standard bases

Ordinary `std(I)` reached the main computation but did not return a basis in
the 1,200-second bounds:

| field | wall s | max RSS KiB | exit | typed result |
|---|---:|---:|---:|---|
| GF(32003) | 1200.23 | 4,299,116 | 124 | MEASURED-MODULAR timeout/no basis |
| GF(65521) | 1200.25 | 4,631,104 | 124 | MEASURED-MODULAR timeout/no basis |
| GF(1000003) | 1200.28 | 4,911,592 | 124 | MEASURED-MODULAR timeout/no basis |

The same ideals with Singular's `slimgb` standard-basis algorithm completed
at all three primes.  `option(redSB)` was active, and every result was

```text
MAIN_DONE basis_size=
1
MAIN_SATURATED_EMPTY
G[1]=1
```

| field | wall s | max RSS KiB | exit | program SHA-256 | output SHA-256 |
|---|---:|---:|---:|---|---|
| GF(32003) | 133.77 | 1,213,808 | 0 | `6b77fa946a743a115cf89cb815bce9b854d4439dba3e10c9da2a6c481d299f23` | `7b95d4e1394a211fd67d87cbb368d0e5ba01a641fbbb17ec8fd37678fce01404` |
| GF(65521) | 227.64 | 507,856 | 0 | `2a352f9613b6ea92511e5a5f42672d1bf3af149c148f0095993e181b23022da5` | `2533751f7186be347e7d6050b5b8bbd9d4f3a0991e502eb3a0e92d4c634a0fa9` |
| GF(1000003) | 241.91 | 507,792 | 0 | `b3b5e5ccc8972ee67d1e14665c8ebf326435c13f0ea49bc223b489f1e6ccda0d` | `a9c85529d1bea35031e2110b011e0f8d0585b582b4462a35c344422810d4052e` |

These three `[1]` results are `MEASURED-MODULAR`.  Without an exact-Q unit
certificate they are not a proof of theorem (T).

## Exact full-chart attempts

- Direct exact-Q `slimgb(I)` (program SHA-256
  `0b096ff42b83d7507c078961a637c64725d4dc83609b058841035908254e8ec6`)
  timed out without a basis: 1800.04 s, 609,904 KiB, exit 124.
- Exact modular lifting `modStd(I,1)`, configured with `setcores(1)`, was
  manually terminated as an exploratory non-result after 876.84 s and
  3,946,988 KiB (exit 1); it produced no basis.
- Exact modular lifting `modGB("slimgb",I,1)`, also with `setcores(1)`, was
  manually terminated to restore the global four-core cap after 1052.89 s
  and 504,532 KiB (exit 1); it produced no basis.

## Proof-preserving constant-pivot reduction

The preprocessing artifacts are in `box/k16t3-20260903/preprocessed/`:

- `triangular_preprocess.py`, SHA-256
  `f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93`;
- `t4_ring_map.tsv`, SHA-256
  `c3be44a90ae437d4fd7c28a313caa04adea7d89a57d7ff433f75bcc69303b29b`;
- `t4_emission_scalars.tsv`, SHA-256
  `b3c6eda9cf51e5bc37864c1f7bbbe2660df8656635a87b9f1839a2dd84ef772c`;
- `reduction_audit.json`, SHA-256
  `ffc4dee9eed5b738696a9a0ddcfa1d2c81500fcf7e0fe9dac314e1a4aa6cbf06`;
- `PREPROCESSING_PROOF.md`, SHA-256
  `da41ea28205dfb0fd641f6f7c0a7948d74229a4882a0e4ccd3efeaae99bd7dbb`.

Each eliminated row is `a*x+b`, where `a` is a nonzero rational constant
and `x` is absent from `b`.  Substitution `x -> -b/a` gives an exact quotient
ring isomorphism.  Composition was checked on every original generator; `c`
is fixed, so the map extends after adjoining `T` with `T*c-1`.  Every emitted
primitive integer row was checked to be a nonzero-Q multiple of its rational
substituted row.  Thus the original and residual `c!=0` ideals are unit
simultaneously over Q.

For t=4 there are 16 constant pivots, reducing 65 to 48 equations and 45 to
29 chart variables including `c`; the pivot bands are 17, 16, 15, 14, two
each at 13, 12, 11, 10, 9, and 8.  The prepared exact-Q `slimgb` input is
`t4_triangular_Q_slimgb.sing`, 186,790 bytes, SHA-256
`54abfe8f94f98d2d2baa3d46b8504e2fe793868c22eea6f1d7d894b96c34d045`.

The exact reduced run reached its 1,800-second bound without returning a
basis: 1,800.05 s, 829,468 KiB, exit 124.  All controls passed through
`MAIN_START`, and stderr was empty.  This is an exact-Q bounded non-result,
not evidence of nonemptiness.

## Positive grading and quadratic-field normalization

The 48 residual equations are weighted homogeneous.  Mechanical extraction
of all 3,650 distinct monomial-difference constraints gives a matrix of rank
28 on the 29 residual variables, hence a one-dimensional grading space.  Its
primitive positive weights include

```text
wt(q5_1)=17, wt(q9_1)=34, wt(c)=85;
wt(b1,b2,b3,b4)=(1,2,3,4).
```

Writing `u=q5_1` and `v=q9_1/u^2`, the two decisive residual rows are

```text
35*u^4 - 270*u^2*q9_1 + 486*q9_1^2 = 0,
-2187*c + 130*u^3*q9_1 - 1404*u*q9_1^2 = 0.
```

The condition `c!=0` forces `u!=0`.  Over an algebraic closure, weighted
scaling therefore normalizes `u=1`.  The first row becomes
`H4(v)=486*v^2-270*v+35`.  Its discriminant is `4860=18^2*15`, so it is
irreducible over Q.  The second row gives
`cbar=v*(130-1404*v)/2187`; exact gcd checks with `H4` show that `v`,
`130-1404*v`, and hence `cbar` are units in `Q(v)/(H4)`.

`build_t4_normalized.py` mechanically rechecks the source hash, all grading
constraints, these two rows, irreducibility/unit conditions, and every
coefficient-field reduction.  It substitutes `u=1`, `q9_1=v`, and
`c=cbar`, reduces modulo `H4`, clears only rational denominators, and verifies
each emitted row is a nonzero rational multiple of the corresponding reduced
row.  After deleting zero rows and exact duplicates, the normalized system
has 38 equations in 26 variables over `Q(v)/(H4)`.

- builder SHA-256:
  `e359327c0b7f96fe87657491b909899aa6848e17f6d38e8ef5364e313ba380d4`;
- audit `t4_normalized_audit.json` SHA-256:
  `00f114c02923570e4918cc55bfc54771d58c33d755c35afcf148180b558ac0ee`;
- Singular input `t4_normalized_Qv_slimgb.sing`, 151,168 bytes, SHA-256:
  `848c2c6aa4215b9e15d87a3dd9b8903a7d1b395e2960284f4232458bf1b84bd7`.

The generated input includes an actual-pair control, positive and negative
Rabinowitsch-style wrapper controls in the declared quadratic coefficient
field, an explicit check that `cbar*(1/cbar)=1`, and a ring-name assertion.
It was launched immediately after the reduced exact-Q run capped and stayed
within the global four-Singular-core cap.  It was stopped at the lane cutoff
after 774.00 s and 990,404 KiB (exit 1), without a basis or `MAIN_DONE`.
All controls passed through `MAIN_START`; stderr was empty and stdout ended
with Singular's `halt 1`.  This is an exact bounded diagnostic only.  Output
SHA-256 is
`570a7ba4d6502a3d90f542f01b2b57bea638891ae4983e5b56aed82060baaac4`;
resource SHA-256 is
`248a1f951963628f47e3e0f7c2a99b958b907abd2ec8f0928030c912f19707d9`.

An exploratory exact quadratic-field affine scan locally checked five unit
pivots, in order `(source 41,a1_0)`, `(20,q6_1)`, `(36,q2_0)`,
`(14,q7_1)`, `(31,q8_1)`, reaching 30 rows in 21 variables.  It was
interrupted before emitting an audited residual program or running Singular;
it is therefore typed partial/measured only and is not used for the verdict.
The reproduction driver `t4_quadratic_reduce.py` has SHA-256
`a25c2ec97e4dfcdf7e65144aaec971d93a41628d9c2589bb236773eed52735e6`.

## Typed t=4 verdict

`OPEN (characteristic zero); MEASURED-MODULAR only.`  The three corrected
full-chart finite-field computations all give reduced basis `[1]`, but no
exact characteristic-zero basis or hand unit certificate completed in the
bound.  In particular, the several t-wise modular kills are not promoted to
theorem (T).

## Reproduction commands

```bash
python3 box/k16t3-20260903/t4/t4_order_system.py --gauged
python3 box/k16t3-20260903/t4/t4_order_system.py --gauged --prime 32003 --emit-singular
Singular -q box/k16t3-20260903/t4/t4_mod_32003_slimgb.sing
Singular -q box/k16t3-20260903/t4/t4_mod_65521_slimgb.sing
Singular -q box/k16t3-20260903/t4/t4_mod_1000003_slimgb.sing
Singular -q box/k16t3-20260903/t4/sat_wrapper_controls.sing
python3 box/k16t3-20260903/preprocessed/triangular_preprocess.py
Singular -q box/k16t3-20260903/preprocessed/t4_triangular_Q_slimgb.sing
python3 box/k16t3-20260903/t4/build_t4_normalized.py
Singular -q box/k16t3-20260903/t4/t4_normalized_Qv_slimgb.sing
```
