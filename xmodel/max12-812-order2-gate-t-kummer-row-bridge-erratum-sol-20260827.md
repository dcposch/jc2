# Gate T Kummer row bridge: additive erratum and corrected promotion scope

Date: 2026-08-27

This is an additive correction to the immutable producer

```text
1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md
```

after the independent Opus5 hostile review

```text
d62b3f22bcad7de1bacecfa13c455f90bd654b578dd23cc5d2439054993f76f3
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-hostile-review-opus5-20260827.md
```

The producer remains immutable.  Where this erratum and the producer differ,
this erratum controls.

## 1. Withdrawn statement

Withdraw the sentence in producer section 6 asserting that the stage-zero
root matrices (5.1)--(5.3), after the map `delta_D1`, give the two root
orientations used by the charged `D1AC` endpoint.  In fact

```text
delta_D1(rs)=delta_D1(cs)=delta_D1(c0)=delta_D1(c1)=0,
delta_D1(a0)=delta_D1(a1)=0.
```

Thus `delta_D1` annihilates `J1+J2`; all six stage-zero root values are zero,
and that composed root-chart map is trivial.  The `D1AC` compiler applies an
analogous plus/minus allocation one contact level deeper, to the shifted
pairs built from `rs2/cs2`, `ec3/ez3`, and `aaa0/aaa1` (with indices shifted
again for later contacts).  Compatibility of those deeper pairs is a
separate finite-jet obligation and does not follow from producer section 5.

Consequently, withdraw the producer's claim that it has composed the Kummer
base change, staged Rees root charts, and the instantiated `D1AC` endpoint,
and withdraw the associated strategic-narrowing/stop claim.  Any downstream
contact import must exhibit and check its shifted finite-jet map explicitly.

## 2. Exact statements that survive

The following statements are independently confirmed.

1. `k[p0] -> k[rho]`, `p0 |-> -2*rho^2`, is finite faithfully flat of rank
   two, including at `rho=0`.  Rees algebras, their Proj blowups, the six
   named standard charts, and the terminal quotient commute with this flat
   base change.
2. The three stage-zero root-coordinate matrices are invertible exactly on
   `D(rho)` and degenerate at `rho=0`.  They correctly identify the named
   stage-zero ideals there, but they do not instantiate the deeper `D1AC`
   roots after `delta_D1`.
3. For every row and every grade `g<=16`, polynomial functoriality gives

   ```text
   delta_D1([sigma^g] Phi_l^total)=[sigma^g] Phi_l^D1.
   ```

   At grade 15 the actual-total rows have frozen custody and are all
   `rho`-even, so the comparison descends uniquely by `rho^2 |-> -p/2` to
   the unsplit `D_16` ring.  Grade 16 is an exact formal-emitter identity,
   not a frozen actual-total row comparison.
4. The grade-15 image is much smaller than the producer headline suggests.
   With irrelevant nonzero rational scalar factors suppressed, it is the
   two-generator ideal

   ```text
   ( theta^2*(a0D*c1D+a1D*c0D),
     theta^2*(2*a0D*c0D-p*a1D*c1D) ).
   ```

   Rows 4 and 6 map to zero; rows 3, 5, and 7 are respectively
   `-p/4`, `-p^2/32`, and `-p^3/128` times row 1.  The factor `4` in the
   `R` map and the moving term `2*sigma*ell1` are first detected at grade
   16, while the named `k10`-jet clauses are detected at neither grade.
5. The exact induced map lands only on the terminal raw-row quotient
   `U_16/(I_16+J1+J2)`.  It cannot extend to any of the six standard charts,
   because each chart denominator maps to zero.  Therefore it yields only
   the forward implication: emptiness of the total terminal raw-row scheme
   implies emptiness of this charged raw-row scheme.  It yields no converse
   and no chart coverage.

## 3. Custody and countermodel repairs

The total grade-15 bytes were produced by the repaired R1 wrapper
`export_allrows_g15_v22r1.py`, not by the V1 exporter that failed closed.
The total and `D1AC` branches use semantically agreeing but distinct row
builders; they do not literally call the same `tail_text` function.  Future
replays should pin the R1 wrapper and all seven `.poly` bytes.

Replace the producer's weak parity example by the ramified descent
counterexample `(rho) subset k[rho]`: it is deck invariant, but it is not
extended from `k[rho^2]`, since its contraction is `(rho^2)`.  Hence deck
invariance alone does not imply descent at the ramified fibre.

## 4. Scope

This correction changes no promoted ramified-fibre, Rees-chart, generic-fan,
Gate-T, order-two, maximum-twelve, or JC2 conclusion: the producer had none.
It does invalidate using the old section-6 sentence as a proof dependency.
The subsequent contact-composition artifacts explicitly use shifted roots
and require their own hostile review; they are not certified by the old
stage-zero root matrices.
