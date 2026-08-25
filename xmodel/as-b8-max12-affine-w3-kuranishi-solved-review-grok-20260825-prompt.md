# Hostile review charge: B8 complete affine `W2/W3` Kuranishi theorem

Review the frozen producer

```text
xmodel/as-b8-max12-affine-w3-kuranishi-solved-aws-20260825.md
cases/as_b8_max12_affine_kuranishi_aws_20260825/
```

at its strict fixed-D12, finite-depth scope.  Do not run Singular, Sage,
msolve, Lean, solver jobs, or substantive Python on the local Mac.  The
frozen Box02/Box03 evidence is the computational source; small hand and hash
checks are allowed, and any new substantive replay must be staged on AWS.

Return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`, the smallest
missing hypothesis or failing identity, and the cheapest exact successor.

## Mandatory attacks

1. **Source and support.** Check the pinned parent SHA, all 81+91 coefficient
   slots, all 276 determinant rows, actual partial-degree caps, and the direct
   versus transported linearization.  Look for any omitted determinant row
   or illicit use of the old 182-slot negative control.

2. **Complete W2 fibre.** Recheck rank 104/nullity 68 and that the displayed
   unreduced-integer parameterization really covers every `F3` digit once.
   In particular, attack the claim that coefficientwise division by three is
   polynomial in these parameters without a hidden canonical-digit carry.

3. **Quadratic formula.** Starting from

   ```text
   det(F0+3T+9W)-1
    =det(F0)-1+3L(T)+9J(T)+9L(W)+27cross(T,W)+81J(W),
   ```

   verify the cokernel projection, constant/linear/square/cross coefficients,
   and the interpolation identities at `0,e_i,2e_i,e_i+e_j` in characteristic
   three.  Check that the analytic/interpolation agreement is genuine and
   not two names for the same coefficient path.

4. **Linear elimination.** Audit the polynomial-span rank 81, quadratic rank
   42, tangent rank 41, and 39 pure-linear consequences.  Verify that solving
   those rows gives a full 29-coordinate kernel and that substitution into
   all 81 equations preserves the ideal, rather than only its point set or
   tangent cone.

5. **Exact reduced ideal.** Independently check that the five emitted
   generators

   ```text
   s22,
   s26+2*s22*s26,
   s22^2,
   s26^2+s19*s22,
   s22*s27
   ```

   generate exactly `(s22,s26)` over `F3`.  Audit both inclusions and the
   claimed reduced `A^27` scheme, not merely its radical.

6. **Projection and counts.** Check that compatibility plus the constant
   rank-104 fresh operator makes the full W3 family a trivial affine
   `A^68` bundle over `A^27`, hence `A^95`, and that the `F3` digit counts are
   `3^27` and `3^95`.  Attack the existence of a global polynomial RREF
   section and any nilpotent/multiplicity issue.

7. **Literal replay and degrees.** Check the ten reconstructed witnesses and
   their all-276-row determinant replay.  Enforce the report's distinction:
   exact partial `y`-degrees `(8,12)` for the whole family, total-degree cap
   D12 for the whole family, but actual total pair `(8,12)` claimed only for
   the emitted witnesses.

8. **Engine/custody distinction.** The analytic and interpolation methods
   live in one pinned Python compiler but were replayed on two hosts; the
   final ideal equality uses genuinely different Singular `std` and `slimgb`
   paths.  Verify hashes/manifests and do not treat host duplication alone as
   algorithmic independence.

9. **V1 false-PASS quarantine.** The first Singular verifier printed FAIL,
   then continued because aggregate zero-ideal comparison and `exit(91)` were
   invalid.  Verify that no V1 conclusion is consumed, and that V2 tests each
   generator separately and rejects any `FAIL` line.  Treat any hidden V1
   dependence as fatal.

10. **Firewall.** Refuse every inverse-limit, `Z3`, characteristic-zero,
    nonautomorphism, selected-Q8/TD6, maximum-twelve, counterexample, or JC2
    inference.  The next carry varies over all 95 parameters and cannot be
    replaced by one selected point.

As a separate routing remark only, assess whether an eventual actual-total-
degree `(8,12)` characteristic-zero lift must have binary leading forms
`P8=a*K^2`, `Q12=b*K^3` for a homogeneous quartic `K`, and whether the B8
reduction forces `K mod 3` to be associated to `y^4`.  Do not fold that
all-depth conditional sieve into the finite-depth theorem.

