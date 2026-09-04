# Hostile gate: the `(25,15)` general order chart

Date: 2026-09-04

## Verdict

**CONDITIONAL[ORDER-TOWER-SLICE]**, with the proposed promotion to
`CONFIRMED[2515-DEAD]` rejected on the present instrument.

The computational statement is confirmed: the charged 12/13/14-variable
order-tower ideals are saturated-empty over `Q`, over the three old primes, and
in this replay over the two new primes 32051 and 32057.  The mathematical
inference from this calculation to “no Keller pair has the `(125,75;M2=105)`
skeleton” is not established.  The charged chart is a strict subfamily of the
necessary D1/Theorem-1.2 locus, and its emptiness is forced by the standalone
coefficient equation `-c` in every `(25,15)` stratum.

The exact residual is `OPEN[FULL-ORDER-BASIS]`: prove that every descended
Keller pair admits the charged five-parameter prefix tower and that every
Theorem-1.2 coefficient lies in its stated filtered prefix basis, simultaneously
at every root; or rerun an exhaustive necessary over-approximation.  The shear
must then be re-audited in that full space.  No Keller pair or counterexample is
produced here, so this is `CONDITIONAL`, not a refutation of the underlying
nonexistence statement.

## 1. Inputs, implementation, and execution discipline

I generated `box/row2515gate-20260903/charged_input_manifest.sha256`
mechanically from the lane receipt by pairing its indexed `basename` and
`sha256` fields with `awk`; no digest was retyped.  `sha256sum -c` returned `OK`
for all 12 frozen inputs.  The manifest SHA-256 is

```text
3058f16bd02ae4f6212b5e7578ee0b1f2f40b0411b20135f0ec6d424263d2063
```

The independent drivers are:

```text
box/row2515gate-20260903/skeleton_replay.py
box/row2515gate-20260903/independent_order_gate.py
box/row2515gate-20260903/compare_charged.py
box/row2515gate-20260903/run_replays.sh
```

`independent_order_gate.py` does not import the charged generator.  It rebuilds
the closed forms, top faces, prefix tower, filtered spaces and gauges, expands
the Jacobian, and performs ascending monic division by `h` in `y`.  A direct
differentiate-then-divide run on stratum `[3]` independently returned 12
unknowns, 21 rows, and target row `-c`.  The faster bilinear h-adic
implementation then generated all rows.  `compare_charged.py` compared the
two generators by tagged `(h-power,x-power,y-power)` coordinates: all equation
polynomials, parameter counts, alpha/beta dimensions, and saturation factors
agree exactly in all three strata.

The runs used Singular 4.3.2 and SymPy 1.12.  SymPy independently reports both
32051 and 32057 prime.  Every Python and Singular job was foregrounded under
`timeout 1800`; Singular was sequential with `--cpus=1 --threads=1
--flint-threads=1` and single-thread environment caps.  No preprocessing,
Q-star pivot, grading normalization, or parameter-dependent division was used.
No ledger or `jc2-lean` action was taken, and no `ideation-*` file was created.

## 2. Skeleton first: source row and three distinct `u` quantities

The label `(25,15)` is descended data, not a query with Moh degrees
`(n,m)=(25,15)`: the latter has no row in the frozen census.  Its source is a
full `(1)`-`(13)` survivor at `(n,m)=(125,75)`.  There are two `(125,75)`
survivors with the same `V` path, at `M2=90` and `M2=105`; the requested
`M2'=21` selects the latter uniquely:

```text
s=3
M=(M1,M2,M3)=(-75,105,123)
d=(d1,d2,d3,d4)=(125,25,5,1)
V=(V2,V3,V4)=(2,4,1).
```

This is reproduced directly by `moh_skeleton_full.py` and independently
recomputed in `skeleton_replay.py`; all window and `(8)`-`(13)` checks pass.
FALLACY-v2's variable-map warning matters here:

```text
Moh top split:        u_s=d_s-v_s=5-4=1
frozen Skel.u:        V_s*d2/d_s=4*25/5=20   (a different integration capacity)
descended remainder:  u'=d2'-V2'=5-2=3.
```

The major-disc tower and denominator/division tower are

```text
D3(delta3=-1) contains D2(delta2=1/5) contains D1(delta1=17/25)

L2=1, A2=5,
V3*d2/d3=20=4*A2+0,
(TRI2,SQ2)=(4,0): condition (10) true, condition (11) false;

L1=5, A1=5, (n*,m*)=(5,3): condition (12) true, condition (13) false.
```

The characteristic/approximate-root tower is also explicit:

```text
q=(-75,180,18),
lambda=(-9375,-4875,-4785),
mu=lambda/d=(-75,-195,-957),
deg_y(T1^psi,T2^psi,T3^psi)=(75,195,957).
```

This is distinct from the charged factor-prefix `H_r` tower audited below.

Here `d_s=5`, `v_s=4`, and `u_s=1`.  Moh Proposition 6.4 supplies the
minor-radius premise for Proposition 6.3 in this `u_s=1` case.  After
normalizing the two source directions to `a=0`, `b!=0`, Proposition 6.3 gives

```text
n'=u_s*n/d_s=25,       m'=u_s*m/d_s=15,
M2'=M2/d_s=21,         V2'=2,
d2'=5, d3'=1,          k=v_s-u_s-1=2,
J_(gamma,pi)=c*gamma^2 with c=-1/b != 0.
```

The `M,V` transport is inferred from Moh's transformed-data table rather than
spelled out in the proposition, but it agrees with every printed Appendix-II
control.  This audit accepts that charged descent map; its failure is later, in
the alleged exhaustive order chart.

## 3. Rebuilt order chart and exact replay

For the descended tuple `(25,15;21;2;k=2)`, both implementations give

```text
K=5, e=5, q=3, u'=3, R=3, Pi=8,
delta2'=-(k+1)/R=-1,
delta1'=(k+1)(Pi*u'-R)/(R(Pi*V2'-1))=7/5,
B=V2'*delta1'+u'*delta2'=-1/5,
lambda_P=eB=-1, lambda_Q=qB=-3/5.
```

All source-safe top multiplicity partitions of `u'=3` are represented:

```text
[3]       Htop=y^2(y-x)^3,
          Omega=1;
[2,1]     Htop=y^2(y-x)^2(y-s2*x),
          Omega=s2(s2-1);
[1,1,1]   Htop=y^2(y-x)(y-s2*x)(y-s3*x),
          Omega=s2(s2-1)s3(s3-1)(s2-s3).
```

The charged factor-prefix recurrence is

```text
H1=L1,
H2=L2*H1+b1*y+b2,
Hr=Lr*H(r-1)+br  (r>=3),
h=H5,
```

with the noncentre factors first and the two `y` factors last.  Its weights are

```text
1:0, H1:-1, x:-1, H4:-8/5, H2:-2, H3:-3, h:-1/5.
```

The pre-gauge alpha dimensions are `[1,1,1,1,3]` and beta dimensions
`[1,1]`.  The charged scalar/embedding test passes inside this basis; the shear
kills `alpha_2`, and target translations remove the constant parts of
`beta_3` and `alpha_5`.  Post-gauge dimensions are therefore
`alpha=[1,0,1,1,2]`, `beta=[1,0]`.

The exact replays are:

| top stratum | unknowns excluding `T` | coefficient rows | `Q` | `GF(32051)` | `GF(32057)` | target row |
|---|---:|---:|---|---|---|---|
| `[3]` | 12 | 21 | `[1]` | `[1]` | `[1]` | `-c` |
| `[2,1]` | 13 | 21 | `[1]` | `[1]` | `[1]` | `-c` |
| `[1,1,1]` | 14 | 21 | `[1]` | `[1]` | `[1]` | `-c` |

Every run printed the declared-ring, forced-empty-wrapper, and nonempty-wrapper
passes before `MAIN_SATURATED_EMPTY`; every standard basis has size one and
every stderr file is empty.  Thus `SATURATED-EMPTY` for the charged sparse
chart is fully replayed and is characteristic-zero decisive.  The fresh-prime
runs are controls, not a lift from modular evidence.

## 4. Why `[1]` is tautological in this slice

After the three gauges, write scalar parameters schematically as `a_i,b`.  The
charged spaces force

```text
Q=h^3+b*h,
P=h^5+a1*h^4+a3*h^2+a4*h+ell,
ell in span{H1,x}; hence ell is linear in x,y.
```

Consequently

```text
J(Q,P)=(3h^2+b) J(h,ell).
```

The `h^0` remainder is `b J(h,ell)`.  Direct expansion and the independent
h-adic calculation both give

```text
coefficient_[x^2*y^0](J(Q,P) at h^0)=0
```

for every partition.  After imposing `J(Q,P)=c*x^2`, that tagged row is exactly
`-c`.  Rabinowitsch adds `T*c*Omega-1`, so the ideal contains one immediately.
The outcome does not depend on subtle Groebner behaviour or on the prime.

The charged sanity gate tests only `deg_x(J0)>=k`.  Here `deg_x(J0)=3`, from
terms with positive `y`-degree, so it prints `PASS` even though the required
`x^2*y^0` coefficient is zero.  The native metadata records a
`target_xk_level0_nonzero` flag but does not use it when assigning status.
This is not by itself a false equation: `-c` is an exact consequence of the
chosen ansatz.  It exposes why exhaustiveness of that ansatz is indispensable.

As a diagnostic only, I freed all nine lower-`h` support coefficients for the
`[3]` face while retaining the charged coefficient basis.  The resulting
16-variable, 25-row exact `Q` system is still `[1]` and still has target row
`-c`.  Therefore adding the missing `h` coefficients alone is insufficient;
the simultaneous-order coefficient basis is part of the exact residual.

## 5. Theorem 1.2: necessary inequality, not the emitted basis

Moh Theorem 1.2, printed p.149, assumes a monic polynomial with a coherent
complete system of pi-roots and a genuine `d`-th quasi-approximate root `h`.
For

```text
f=h^d + sum_(j=1)^d h_j h^(d-j),   deg_y h_j < deg_y h,
```

it concludes, for every root `sigma_i` and every `j`,

```text
ord h_j(sigma_i) >= (lambda/d)*j.
```

These are necessary lower bounds once all hypotheses and the descended
accuracies are proved.  The theorem is not a converse, does not state an
attainment equality, and does not provide either the charged factor-prefix
recurrence or a finite spanning basis for all coefficient polynomials.  Moh
refers the proof to his paper `[M.4]`; it is not in the charged PDF.

The charged implementation first computes a nine-monomial D1 envelope for the
lower terms of `h`:

```text
y^4, y^3, x*y^3, y^2, x*y^2, x^2*y^2, y, x*y, 1.
```

It then uses five `b` parameters on seven support positions.  Besides omitting
`x^2*y^2` and `x*y`, it imposes two coefficient relations (fiberwise, with
`s_last` the last noncentre factor):

```text
[x*y^3] = -s_last*[y^4],
[x*y^2] = -s_last*[y^3].
```

Thus the sparse `h` locus has codimension four inside the code's own envelope.
The only check is

```text
support(sparse h-Htop) subset support(D1 envelope).
```

That is the wrong inclusion direction for an empty-superset proof.  The charged
report explicitly says the tower is narrower and calls the calculations
“order-tower reductions,” not generic D1 reductions (charged report
lines 117-134; frozen generator lines 147-160 and 240-280).

There is primary-source confirmation that this is a real restriction.  For
Moh's worked descended `(15,10;M2=11,V2=3;k=2)` two-root case, printed p.211,
equation (5), the required quasi-root has eight independent lower coefficients:

```text
h=(y^2-x^2+a1*y+a2*x+a3)y^3
  +(a4*x+a5)y^2+(a6*x+a7)y+a8.
```

The frozen “validation” builder instead has only

```text
h=y^3(y^2-(1+s2)xy+s2*x^2)+b1*y^4+b2*y^3+b3*y^2+b4*y+b5.
```

At Moh's normalized `s2=-1`, this deletes the independent `x*y^3`, `x*y^2`,
and `x*y` directions.  Therefore even this banked validation row is provably a
proper slice of Moh's displayed necessary form.

The second, independent gap is the fixed coefficient list
`{1,H4,H3,H2,H1,x}` with one scalar weight assigned to each prefix.  Theorem
1.2 demands simultaneous valuation inequalities at every pi-root.  It does not
say that this list spans their intersection, and the generator performs no
root-by-root evaluation, associated-graded spanning proof, or branching on
cancellations between lower-weight terms.  Such cancellations are exactly how
higher-degree combinations can acquire larger order.  Hence the raw
Theorem-1.2 inequalities are necessary, but the emitted 12/13/14-variable
coordinate chart is not proved necessary.

## 6. What is and is not encoded

The top face records the three multiplicity partitions of the noncentre root
units and saturates the symbolic slopes apart.  It does **not** encode deeper
minor-disc splits, their residue series and root allocations, the pole or
negative-power cancellation rows used in Moh's Appendix II, or all Laurent
anchors of the monomial-Jacobian Lemma-2.1 analogue.

It **does** encode every coefficient of the polynomial identity
`J(Q,P)=c*x^2` inside its chosen `h,alpha,beta` ansatz.  The h-adic Leibniz
identity is correct, division is by monic `h`, recomposition passes, and the
independent tagged comparison found no missing Jacobian row.

This distinction decides the hostile question.  Omitting additional necessary
minor, pole, or lift equations enlarges a parameter space and cannot invalidate
emptiness of a genuinely exhaustive over-approximation.  Omitting variables or
imposing an unproved normal form shrinks the space and can create emptiness.
The present chart does the latter, so absent minor/pole rows is not its fatal
defect; absent coefficient directions and a missing spanning theorem are.

## 7. Saturation, ring, pivots, and shear

The Rabinowitsch factor itself survives attack.  On a genuine descended pair,
`c=-1/b` with `b!=0`, so `c!=0`.  On each declared stratum, `Omega!=0` says
exactly that every symbolic slope is nonzero, differs from the normalized slope
one, and differs from every other slope.  A zero factor moves to the centre or a
coarser partition.  Therefore localization by `c*Omega` is correct.

For `[3]`, the declared coefficient-ring order is

```text
b1,b2,b3,b4,b5,A1_0,A3_0,A4_0,A5_0,A5_1,B2_0,c,T,
```

with `s2` and then `s3` inserted after `b5` in the other strata.  `x,y` are
coefficient-extraction variables and are absent from the final parameter ring.
The system is exactly

```text
I=(all tagged coefficient rows, T*(c*Omega)-1)
```

over the declared field.  The fresh variable `T` has no collision.  Both
forced-empty and known-nonempty wrapper controls pass in every run.

No parameter-dependent pivot is inverted.  Symbolic construction and the
native builder divide only by the monic `y`-leader of `h`, and the final run is
direct `std(I)`.  The charged shear is also algebraically valid **inside the
charged spaces**: it is applied only after `alpha_(e-q)` is checked to be scalar
and every shifted beta basis vector is found in the target alpha space.  But
that check occurs after the unsupported basis truncation.  A nonconstant shear
coefficient would add `-Q*J(Q,a)` to the Jacobian, so the shear must be checked
again after an exhaustive simultaneous-order space is known; it must be omitted
in the generic D1 over-approximation where `alpha_2` is not scalar.

## 8. Controls

The independent generator agrees equation-for-equation with the charged one on
the two K16 count rows and on one banked validation row.  Exact `Q` results are:

| control | unknowns/rows | standard basis | interpretation |
|---|---:|---|---|
| K16 `(16,12;13;3;k=1) [1]` | 18/23 | `[1]` | charged count replayed |
| K16 `(28,20;25;3;k=1) [1]` | 27/37 | `[1]` | charged count replayed |
| banked `(15,10;11;3;k=2) [1,1]` | 18/37 | `[1]` | slice replayed; p.211 disproves completeness |

The K16 rows have `K=4,u'=1`; Moh p.208 itself gives the four-parameter form
`h=y^3(y-x)+b1*y^3+b2*y^2+b3*y+b4`.  They are good arithmetic, h-adic and CAS
controls for that one-direction case, but do not validate the multi-direction
prefix generalization.

Finally, the genuine tame automorphism

```text
(Q,P)=(y,y^2-x),  J(Q,P)=1,
inverse: y=Q, x=Q^2-P
```

prints `TAME_J_PASS` and `TAME_SURVIVES` over `Q`, `GF(32051)`, and
`GF(32057)` under the same standard-basis wrapper.  It is a positive wrapper
control, not a target-row witness: a polynomial automorphism has constant
nonzero Jacobian and cannot have `J=c*x^2`.

## 9. Promotion decision and exact residual

FALLACY-v2 forbids turning a lower bound into an exact spanning statement and
requires a safe typed OPEN when no replacement closes the gap.  No exit-price
assertion is made, so no `charge_basis` line is due.

The gate results are therefore:

```text
CONFIRMED[SATURATED-EMPTY-SPARSE]:
  all three charged (25,15) order-tower ideals are [1] over Q and two new primes;
  the ring, Rabinowitsch factor, monic reduction, and exact Jacobian rows pass.

REFUTED AS A PROMOTION INFERENCE:
  those ideals parameterize a strict slice, and each [1] is immediately forced
  by -c together with T*c*Omega-1.

CONDITIONAL[ORDER-TOWER-SLICE] / OPEN[FULL-ORDER-BASIS]:
  no skeleton kill is promoted.
```

To obtain `CONFIRMED[2515-DEAD]`, one must do one of the following:

1. Prove a normal-form theorem putting every relevant K=5, `u'=3` descendant
   into the five-parameter prefix tower and prove that
   `{1,H4,H3,H2,H1,x}` is an exhaustive adapted basis for every simultaneous
   Theorem-1.2 filtration, including all cancellation branches; then recheck
   the scalar shear and rerun.
2. Use the full necessary D1/general chart (the banked counts are
   135/136/137 unknowns and 517 rows), without the scalar shear unless newly
   justified, and prove its saturated ideal empty over `Q`.

Until one of those residuals is closed, emptiness of the order chart alone is
not a kill of the `(25,15)` skeleton.

<!-- BODY-END -->
