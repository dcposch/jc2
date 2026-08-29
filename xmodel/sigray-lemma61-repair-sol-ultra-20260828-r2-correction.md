# Mandatory correction to the Sigray Lemma 6.1 R2 repair

Date: 2026-08-28 13:55Z  
Status: **INCORPORATED DOCUMENTARY REPAIR; THEOREM PROMOTED**  
Producer:
`xmodel/sigray-lemma61-repair-sol-ultra-20260828-r2.md`
(`2fdbbee9...`)  
Opus5 hostile review:
`xmodel/sigray-lemma61-repair-hostile-review-opus5-20260828-r2.md`
(`5193e7b0...`, verdict `REPAIR`)

The review independently confirmed every mathematical inference and required
only the following two typing clarifications.  They are part of the final
proof and supersede the corresponding shorthand in R2.

1. In the paragraph defining the grid, read `K` as one positive integer
   simultaneously suitable for the chart, divisible by the denominator of
   `u`, and divisible by every relevant chart-pole order of each of the two
   fixed curves `f-a=0` and `g=0`.  Such a `K` is the lcm of finitely many
   integers.  Statement 3.9's extra hypothesis is divisibility, not merely
   taking a numerically large denominator.  No derived tower polynomial is
   passed to Statement 3.9.

2. After defining `F_j` and `rho(F_j)`, insert: every `F_j` lies in
   `T_a^+`, hence its `f-a` order is positive.  The order-zero constant `a`
   cannot affect the positive leading term, so

   ```text
   d_(F_j)=d_(f-a,F_j),       p_(F_j)=p_(f-a,F_j).
   ```

   This licenses the notation switch between Proposition 4.1/Statement 3.18
   and the fixed-pair `rho` calculation.

With these insertions, the exact edge law, ancestor nonemptiness,
Proposition 4.4 transport, axis exponent orientation, degree contradiction,
and terminal clause are all review-closed.  Lemma 6.1 was the last
outstanding review rider on repaired Proposition 6.8; the
Proposition 6.7/6.8 microstep-to-next-vertex bridge may now be used without a
Lemma-6.1 provisional tag.  Statement 6.2 itself remains a printed GAP due to
its omitted positive-vertex hypothesis.
