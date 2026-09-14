# Full necessary-chart rational survivor certificates

The explicit certificates are `print-audit-full-chart-survivor-delta2.json` and `print-audit-full-chart-survivor-delta52.json`; their executable generator is `print-audit-full-chart-survivor.py`. All row images are retained in the matching `.rows.tsv` files. The chart scope is exact: full canonical remainder coefficient boxes, the derived D2 and D1 support/face rows, all minor root and remainder rows, all F/G minor pole rows including their nonzero equality faces, the branch localizer, and **every positive-degree global Jacobian coefficient**. The Jacobian constant is recorded as0. Its nonvanishing is a separate stronger instrument, and is not silently assumed in either survivor verdict.

For each branch the generator loads the source inner chart, applies the previously certified rational assignment in `print-audit-inner-minor-<branch>.json`, and explicitly sets all6600 ambient outer coefficients to0. These assignments are point evaluations; they are not restrictions used to produce a unit. The resulting normalized polynomials are recorded coefficient by coefficient for K3,C2,C3,K2. Exact monic division of K2−K3³ by K3 independently recovers C2 and C3. Every canonical total-degree and y-degree box is checked. In particular the r=0 C2/C3 terms are absent because the derived total-degree bounds are21/32 while the normalizations are22/33, not because a numerical floor deletes them.

The entire global polynomials KF=K2³ and KG=K2² are also expanded without truncating their total-degree boxes. Delta2 has1484 and674 nonzero coefficients; delta52 has1505 and683. Their complete coefficient hashes are recorded. No unexplored high coefficient of F or G is left as an implicit zero assumption.

All source rows are then evaluated with exact rational arithmetic. The D1 substitution is evaluated on every possible coefficient label in the full ambient degree boxes, including rows redundant after the D2 equations. The complete K2 minor pullback uses all coefficients of the degree33 polynomial and is verified through local power27/63. Because its minimum local power is exactly27/63, composition as a ring homomorphism proves that KF and KG through their pole ceilings81/54 or189/126 are exactly the corresponding powers of that verified image. Higher K2 local terms cannot enter those ceilings. Thus this is full pole-row exhaustion for the explicit degree99/66 polynomials, not an empirical low truncation.

The historical lower-coefficient support counts are preserved:1134/513 on delta2 and1316/594 on delta52. The fixed highest generic-power equality coefficient is not in those lower-coefficient tag sets; the certificate checks it separately for each polynomial. Thus the F/G pole groups contain1135/514 and1317/595 rows respectively. This avoids omitting a face coefficient merely because its lower-support label is absent.

The global Jacobian identity is verified by direct symbolic differentiation of F=H³,G=H²:

```
Fx=3H²Hx, Fy=3H²Hy, Gx=2HHx, Gy=2HHy,
Fx*Gy−Fy*Gx=0.
```

This exact polynomial identity covers all13,529 positive-degree coefficients, from normalized t-power0 through162, and the constant at t-power163. Every one of the13,529 positive-degree labels is explicitly emitted in the row file. The constant is separately recorded0. Historical stages0 through8 are individually re-evaluated from the full coefficient images; delta2 cumulative schedule counts are21,160,326,493,659,824,990,1155,1319, and delta52 counts are19,156,320,483,645,806,966,1125,1285. No Gröbner dimension of the full locus is inferred from this rational point.

The complete row totals are41,774 on delta2 and42,639 on delta52. Every image is0. A subsequent mechanical check re-read the TSVs, verified their row counts and SHA-256 hashes against the JSON certificates, checked that every row ends in the exact image0, and checked every recorded source/driver file hash against the unchanged file used for the run.

There are two independent negative controls. Perturbing the single outer coefficient B1_(0,32) to1 changes G by `(y−x)^32 H`. On the top H=y9(y−x)24, direct differentiation gives `864*y35*(y−x)^127`, so the x127*y35 coefficient is−864. The engine's independent normalized Jacobian emitter also returns−864 at t1,w35. Setting rho or c to0 while its wrapper is1 gives−1. The stronger nonzero-J instrument is tested separately: Jc=ZJ=1 makes its wrapper0 but its constant-coefficient equation−1 at these points.

The gate's original points are preserved as separate controls through custody-linked artifacts, with their original assignments and exact subsequent failures. They fail the new C2/C3 source conditions before the stage schedule; on the old corrected diagnostic enlargement their first additional pole failures occur at G local10/local20. These points are not renamed or identified with the new rational assignments.

Both verdicts are **SURVIVOR OF THE FULL DECLARED POSITIVE-JACOBIAN NECESSARY CHART**. They are not Keller pairs: J=0. They also need not realize the exact characteristic degree55 or the nonzero D1 differential-face constant of Prop4.6 at r=1. The explicit root/remainder chart is a necessary enlargement, not a claim that all conclusions of Moh have been attained by each chart tuple. The separate degree55 and nonzero-J instruments are explained in `print-audit-nonchart-instrument.md`. A unit after imposing such an instrument on only these pure-power points would exclude those points, not kill either unrestricted branch.
