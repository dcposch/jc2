# Focused hostile review: V20 overlay claims from the Fable5 adjudication

You are Opus 5, acting as a different-model hostile mathematical reviewer.
Work read-only in `/Users/dc/code/math/jc2`. Do not edit any campaign file,
case file, canonical ledger, or `jc2-lean`. Your sole permitted repository
write is:

`xmodel/ideation-20260827T0145Z-v20-overlay-hostile-review-opus5.md`

Target report:

```text
xmodel/ideation-20260827T0145Z-crosspollination-hostile-review-fable5.md
SHA-256 1481d3cadc30ee024c7d4e07e746a6e15ce000a52358e589a1fdf5add3e755c1
```

You already independently reviewed the V20 grade-13/14 export in
`xmodel/max12-812-order2-p0-total-rees-allrows-g13-g14-v20-hostile-review-opus5-20260827.md`
(current SHA-256
`8665e43cd9df2b6c55aeccde72daa10ddff4768813df045feeb97cb593264bf5`).
Do not merely cite that review. Reuse its independently parsed/reconstructed
objects where sound, but recompute the following new claims from frozen bytes.

Audit each item separately:

1. The exact characteristic-zero delayed-load point in Fable §4.2. Verify the
   displayed algebra `Q[w,s]/(w^4+1,s^2-5/12)` is nonzero, substitute every
   coordinate into all 22 V9/V17 rows, and decide whether it extends to the
   honest ordered `T-cs` presentation with `cs*k1*rho` a unit and `k=0`.
2. Evaluate all fourteen V20 grade-13/14 rows at that point. Verify or refute
   “13/14 nonzero, only `Tg14_5` zero, `Tg13_6=35/128`.”
3. Verify coefficientwise the claimed identity

   ```text
   Tg13_6 + (1/2)*cs*rho^2*Tg11_1 - (35/128)*cs^4*k1*rho^4
       in (k,rs,c0,c1).
   ```

   Then audit every hypothesis in the stated set-theoretic conclusion that
   `V(k) intersect D(cs*k1*rho)` dies at grade 13 on the ordered `T-cs`
   stratum. Distinguish ideal membership, radical/set-theoretic use, and
   characteristic exclusions. Check whether `qrs=0` is really available.
4. Verify `RS0` (`rs=1`, all other non-rho source names zero) annihilates all
   22 frozen rows and all fourteen V20 rows and is compatible with whichever
   honest ordered chart equations Fable invokes. State its exact scope.
5. Recheck Fable's factor-two repair of the shifted-core `e0*e1` identity in
   both `V(J1)` and `V(k)` columns. Give the exact correct formulas and the
   residual of the incorrect Opus cross-pollination formula.
6. Recheck the scope repair for `Tg14_5|_{J1}`: enumerate its k-containing
   terms or otherwise prove whether the correction terms lie only in
   `(cs1)` or instead in `(cs1,cs2,rs1,rs2,e0,e1)`, and decide whether the
   row dies on `qa1=0` alone.
7. Verify the `M>=1` certificate-typing gate by the promoted `CS0` section,
   independently of the refuted `deg_2` proof. Be exact about the certificate
   shape and the honest ideal generators needed for evaluation.
8. Verify the parity-refined torsion composition: from a cleared containment
   modulo `(rho)`, rho-even generators, and the promoted
   `cs^6*k^2*rho^6` membership, determine whether an existence-only
   `cs^(3m+6)*k^(3m+2)` honest membership follows. Identify any hidden use of
   saturation, a false converse, or an unjustified even-part operation.

For each claim use `CONFIRMED`, `REFUTED`, or `GAP`, show exact arithmetic,
and identify the strongest theorem and precise scope. Model agreement is not
evidence; inspect and recompute. Use only bounded local read-only work and
temporary files under `/tmp`; uncertain/heavy algebra belongs on AWS and
should be left as a gap, not run locally. No web, no AWS mutation, no launch.
End with an explicit list of ledger corrections that are safe to promote now.
