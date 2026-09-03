# TOP-TAIL-UNIT determinant lane: proof-ready findings

## 0. Status and custody

All seventeen frozen inputs passed the receipt-derived SHA-256 manifest.  The
manifest was produced mechanically from
`xmodel/k16-terminal-determinant-sol56-20260903.run.v2` by pairing its
`charged_input_i_sha256` and `charged_input_i_basename` fields and piping the
result to `sha256sum -c`; all seventeen entries returned `OK`.

The result of this sublane is **PARTIAL**.  It does not prove uniform
TOP-TAIL-UNIT.  It sharpens the finite-quotient target, finds and verifies a
necessary correction at the split base `t=2`, computes exact/modular fixed-t
determinants, and falsifies the previously noticed three-point quotient-length
fit at `t=6`.

The probes use only the frozen coefficient recurrence
`/tmp/jc2-lane.ZvRDkK/inputs/top_tail_fast_recurrence.py`.  The local driver is
`probe_top_tail.py` (SHA-256
`63024cf4e56547dc44973a79b8cc71c915a243c55f7b9a6a7648f676e5890bc7`).
The Singular polynomial used by that emitter is `RR=-E`.  Thus the fixed
determinants below are for the stored-row normalization

```text
Fhat_r=[X^(t+r)]RR=-T_(t,t+r)|_(b4=1).
```

If `N` is the quotient rank, the determinant for the report's `F_r` differs by
`(-1)^N`; finiteness and nonvanishing are unchanged.

## 1. Correct componentwise determinant statement

For `0<=r<t`, set

```text
F_r=T_(t,t+r)|_(b4=1),
J_t=<F_1,...,F_(t-1)>,
B_t=A_t[b3,u_2,...,u_(t-1)]/J_t.
```

The `X`-rows may equivalently be replaced by the corresponding `L=X-1`
coefficients: the binomial change of basis is triangular with diagonal one,
and the spans of bands `t+1,...,2t-1` agree.  This introduces no denominator.

For a nonsplit integer `t`, `A_t` is a quadratic field.  Once `B_t` is finite,
choose a field basis `M_t`; then

```text
<F_0,...,F_(t-1)>=[1]
 iff F_0 is a unit of B_t
 iff Delta_t=det(mu_(F_0); M_t) != 0.
```

At a split index `t=3s^2-1`, however,

```text
A_t = Q[d]/((d-s)(d+s)) = Q e_+ x Q e_-,
e_+=(d+s)/(2s),  e_-=(s-d)/(2s).
```

One must form

```text
B_t^+=B_t tensor_(A_t,d->+s) Q,
B_t^-=B_t tensor_(A_t,d->-s) Q
```

and independently prove both finite.  Their dimensions need not agree.
Choose separate bases and define

```text
Delta_t^+=det(mu_(F_0):B_t^+->B_t^+),
Delta_t^-=det(mu_(F_0):B_t^-->B_t^-).
```

The chart is a unit exactly when both determinants are nonzero.  If the two
values are encoded as a class `P_t d+Q_t`, then its norm condition is

```text
3 Q_t^2-(t+1)P_t^2 != 0,
Res_y(H_t,P_t d+Q_t)=4q^2(3Q_t^2-(t+1)P_t^2) != 0.
```

This encoding does not supply a common free basis.  It merely packages the
two component values.  In particular, the wording "construct one indexed
`A_t`-basis" is false at `t=2` and must be replaced by the componentwise
statement above (or by finite locally free modules of locally varying rank).

## 2. The required `t=2` correction

Here `s=1`,

```text
A_2=Q[d]/(d^2-1)=Q x Q,
d=-1 <=> y=1/5,
d=+1 <=> y=2/5.
```

For `J_2=<F_1>` the exact frozen recurrence gives:

| component | reduced generator for stored `RR` row | quotient rank | `det(mu_Fhat0)` |
|---|---:|---:|---:|
| `d=-1`, `y=1/5` | `88*b3-295` | 1 | `-287/1408` |
| `d=+1`, `y=2/5` | `1189646642*b3^2+304374720*b3-1207034325` | 2 | `2762023282304080896/297558232675799463481` |

Both determinants are nonzero, hence TOP-TAIL-UNIT holds on both components,
as charged.  But the ranks are `1` and `2`, so `B_2` is not a free `A_2`
module of one rank.  The displayed determinant denominators factor as

```text
1408=2^7*11,
297558232675799463481=29^14.
```

The exact outputs have SHA-256
`cdefefef864419a92ee428a6b5ae85fc4a0d04b54ff9b5634d0cd2d29e1b7280`
and
`da6366f002a2996348bff9e5c3136fefdc75ddf3f0493bbf2a25df3ec8f7af9e`.
Modulo `1009` the same determinants are `194` and `758=-251`, respectively.

This is not the RESIDUAL-ZERO base: as charged, that statement is false in
the product algebra at `t=2`; the band-zero row instead closes the `b4=0`
chart.

## 3. Fixed quotient and determinant computations, `t=3,...,6`

The descending-prefix computations use degree-reverse-lex (`dp`) in the
declared residual-variable order `(b3,u2,...,u_(t-1))`.  At `p=1009`, both
roots of `H_t` were run independently.

| `t` | `y` roots mod 1009 | quotient dimensions | GB sizes | stored-row determinants | norm/product mod 1009 |
|---:|---:|---:|---:|---:|---:|
| 3 | `632,810` | `8,8` | `3,3` | `998=-11, 627=-382` | `166` |
| 4 | `468,990` | `44,44` | `21,20` | `202, 740=-269` | `148` |
| 5 | `433,760` | `224,224` | `102,102` | `231, 844=-165` | `227` |
| 6 | `380,940` | `1224,1224` | `525,525` | not completed | not completed |

All displayed determinants are nonzero.  The `t=6` dense `1224`-square
multiplication-matrix calculation was stopped after a bounded exploratory run;
this is `INCONCLUSIVE`, not zero.  The charged full top-tail ideals are unit
modulo `1009` on both `t=6` fibres, but the exact characteristic-zero top-tail
job remains the charged `INCONCLUSIVE_TIMEOUT`.

At `t=3`, the quotient and determinant were also computed exactly over
`Q[a]/(a^2-12)`, `a=3d`.  The quotient has dimension `8`.  The determinant is
a nonzero linear class with a 332-digit common denominator (full value in the
artifact), and its exact rational norm is nonzero (negative).  Reduction at
the two roots `a=298,711 mod 1009` gives `998,627`, with product `166`.
The exact-output SHA-256 is
`a8db281e68dca8dd82a9c773c8c5e03abefaa2780dd02231e6a663e04be00e4a`;
`factor_exact_determinants.py` mechanically parses the exact class and checks
the norm.

At `t=4`, `J_4` was independently computed exactly over
`Q[a]/(a^2-15)`, `a=3d`; it is zero-dimensional of dimension `44` with GB size
`21`.  The charged exact full top-tail unit computation then implies that the
exact omitted-row multiplication determinant is nonzero.  Direct expansion of
that 44-square determinant was stopped; no closed determinant class is claimed.
The exact finite-quotient output SHA-256 is
`0e9269745aecf2a7c096d72016c3d4d70a485fab833763ef93e06b0d54a64cca`.

The modular determinant-output SHA-256 values, in row order `t3 +/-`, `t4
+/-`, `t5 +/-`, are

```text
c1fe9aff617789b4287dadb746416cc9f837514933c39ea626f2fde30ea0b49a
0e5795eef8a37e4b3104eaced7bf9afae0be1f8bba9b2c2eaf6fb4367a24e0d8
1c3b011037b75dba0a6329a50707d692b2d3ff2c073e847631500ac2ceecb86d
fc989c0600e27740dae70ec2c01e5390bf775b281227564614f274c119a8fad0
2561f91e7d2c6ca003534e687f32a1c71a7a58d686c419adac74492863f3b3d2
bdc2f53b0676b48a9b6755c6399326adf1406f6fb7f5b92926e1f169cabc7f0e
```

The `t=3,4,5` dimensions reproduce the charged descending-prefix values
`8,44,224`.  The `t=6` value is new and supplies the essential negative
control:

```text
9*5^(t-3)-1 gives 1124 at t=6, but dim(B_6 mod p)=1224
on both fibres.
```

Therefore the three-point fit in the charged audit is false as a recurrence.

## 4. Measured staircase structure and the exact finite target

The modular leading ideals contain the following pure powers on every checked
first fibre:

```text
t=3: b3^3, u2^4
t=4: b3^5, u2^5, u3^6
t=5: b3^7, u2^6, u3^7, u4^8
t=6: b3^9, u2^7, u3^7, u4^9, u5^10
```

At `t=6`, `u3^7` is stronger than the uniform-looking `u3^8`.  Thus all four
tests support the finite certificate

```text
M_t=<b3^(2t-3), u_i^(t+i-1) : 2<=i<t> subset in_dp(J_t),   t>=3.   (A)
```

Both `t=6` fibres have exactly the same 525 leading monomials.  The `t=3` and
`t=5` fibres also agree; at `t=4` two modular leading ideals differ slightly
(GB sizes `21` and `20`) but have the same dimension and all the displayed
pure powers.  This is why the safe candidate is the pure-power containment,
not equality with one measured initial ideal.

For reference, the first-fibre standard-monomial Hilbert counts by ordinary
total degree are

```text
t=3: 1,2,3,2                                      (length 8)
t=4: 1,3,6,10,15,9                                (length 44)
t=5: 1,4,10,20,35,56,72,26                        (length 224)
t=6: 1,5,15,35,70,126,210,316,358,88              (length 1224).
```

Their top filtered degree is uniformly `2t-3`, but the interiors and GB
generator counts `3,21,102,525` do not yet give an indexed recurrence.
Statement (A), if proved by explicit indexed S-polynomial reductions with all
leading coefficients shown to be units, would prove `B_t` finite.  It is only
a measured conjecture here.

The support weights give a useful cost benchmark, not a theorem.  The `J_t`
row weights are `3t,3t-1,...,2t+2`, while the residual-variable weights are
`t+1,2,...,t-1`.  Their formal weighted Bezout ratio is

```text
W_t=(3t)!/((2t+1)!(t+1)(t-1)!).
```

It equals `44` and `1224` at `t=4,6`, but equals `9` versus the actual `8` at
`t=3`, and `455/2` versus `224` at `t=5`.  Hence it cannot be quoted as the
quotient length without a boundary/toric correction theorem.  At `t=11` it is
`7713420`, which explains why a dense multiplication matrix is an unattractive
test, but is not asserted to be the actual rank.

## 5. Exact remaining uniform statement

The unresolved TOP-TAIL statement can now be written without the false
freeness premise:

1. For every nonsplit integer `t>=3`, prove `B_t` finite and construct an
   indexed field basis.  For every split `t=3s^2-1`, prove both `B_t^+` and
   `B_t^-` finite and construct separate bases (allowing unequal ranks).
   Proving (A), with componentwise nonvanishing of its reduction coefficients,
   is one concrete sufficient statement.
2. In those bases compute the omitted-row determinants.  After reduction in
   `d^2=(t+1)/3`, write the indexed result as

   ```text
   Delta_t=(P_t(t)d+Q_t(t))/D_t(t).
   ```

3. List and exclude every positive-integer zero of `D_t`, and prove

   ```text
   3Q_t(t)^2-(t+1)P_t(t)^2 != 0
   ```

   for all remaining integers.  At every split index this means checking the
   two values separately before any norm/product packaging.

No indexed basis, `D_t`, or determinant recurrence is derived here.  That is
the exact remaining determinant statement; fixed ranks and modular residues do
not fill it.

## 6. Denominators and specialization set

Specializing `b4=1` introduces no denominator.  The full parameter-dependent
denominator/unit list inherited from the proved coefficient recurrence is:

```text
2, 3, 6,
q, q^2, q^3, t, e, t+1, 3t+2, 4t+1,
m+1                       (0<=m<t),
2m+1                      (0<=m<=2t),
4t-2j+1                   (1<=j<t and t<=j<=2t),
q-j                       (t<=j<=2t),
F_C(t,j)                  (1<=j<t),
F_Q(t,j)                  (t<=j<=2t),
```

plus constant factorial denominators if symbolic binomial coefficients are
expanded.  Here `q=2t+1`, `e=3t+1`, and

```text
F_C(t,t-n)=
 3n^4+24n^3t+42n^3+66n^2t^2+146n^2t+119n^2
 +72nt^3+238nt^2+234nt+104n
 +27t^4+134t^3+223t^2+136t+32,

F_Q(t,q-n)=n^2+4nt+6n+4t^2-3.
```

All are nonzero in their charged ranges for integer `t>=2`: the indexed odd
factor is positive, `1<=q-j<=t+1`, and `F_C,F_Q` have the charged positive
coefficient/positivity proofs.  The primitive coefficient classes and their
norm/resultant factors are `y`, `3d+2(t+1)`, `L_C`, `L_Q`, and
`3qd+(t+1)`; their resultants are exactly those in charged equations
(3.1)--(3.7).  No new denominator from a uniform Gröbner/border-basis or
determinant recurrence has been obtained.  Such leading coefficients and the
unknown `D_t(t)` must be added before promotion.  This missing list is part of
the open statement, not silently assumed empty.

The quadratic algebra splits for the infinite set

```text
t=3s^2-1: 2,11,26,47,... .
```

It is not a finite denominator-exception set.  The first two required controls
are:

```text
t=2:  d=-1,+1; y=1/5,2/5                (handled exactly above),
t=11: d=+2,-2; y=7/23,5/23;
      mod 1009: y=439,746, respectively.
```

## 7. The `t=11` component test

The charged `t=11` artifact checks only the coefficient recurrence and all high
pivots at five residual points on each factor.  It is not a quotient-dimension
or determinant test.  The charged direct positive-row `dp/std` attempt on the
`d=+2`, `y=439` fibre hit its 600-second cap; the `d=-2`, `y=746` fibre was not
run.  Consequently neither `dim B_11^+`, `dim B_11^-` nor either determinant is
known.

The cheapest determinant-route falsification test is componentwise:

1. Generate `F_1^+,...,F_10^+` at `y=439` and
   `F_1^-,...,F_10^-` at `y=746` modulo `1009` from the frozen recurrence.
2. Use an early-termination weighted/border-basis computation to seek the pure
   powers in (A), rather than first materializing a dense quotient basis.
   Failure of finiteness on either fibre falsifies the proposed `J_t`.
3. If finite, test multiplication by `F_0` separately on each fibre using a
   sparse/black-box norm or resultant.  A zero determinant on either side
   falsifies TOP-TAIL-UNIT.  A dense matrix based on the formal benchmark
   `W_11=7713420` is not the cheap implementation.

For a proof rather than a falsification, the same computation must be lifted
to an indexed reduction, with every new leading coefficient and denominator
norm factored and its integer roots checked.  One modular unit result would not
prove characteristic zero or all `t`.

## 8. Verification against charged records and guardrails

- The frozen emitter rechecks every affine pivot against charged formulas
  (2.10)--(2.12) before substitution.  Its charged controls match all terminal
  rows for `t=2,...,6`; the present probes begin only after that recurrence.
- Exact `t=2` component ranks and determinants agree independently with the
  audit lane.
- `t=3` exact recurrence and top rows agree with the frozen exact record;
  quotient rank `8` reproduces the charged subsystem audit.
- `t=4,5` modular ranks, GB sizes, and full-unit outcomes reproduce the charged
  records (`44` and `224` for the selected descending prefix).
- `t=6` both recurrence fibres pass and have matching quotient dimension
  `1224`; this is a new bounded modular measurement, not a uniform promotion.
- No `sat()` wrapper, field assumption on a product algebra, raw unchecked
  remainder, or finite-sample interpolation is used.  No exit-price assertion
  is made, so no `charge_basis` line is due.

The all-`t` verdict from this sublane is therefore **PARTIAL** with exact
residual statement `OPEN[TOP-TAIL-COMPONENTWISE-DETERMINANT-RECURRENCE]` as in
Section 5 above.
