# Hostile review charge: D1 primary-C2 `c=8` first connection wall

You are an independent hostile mathematical reviewer. Work read-only in
`/Users/dc/code/math/jc2`. Review the frozen producer

```text
cases/max12_812_order2_square_owner_d1_c2_c8_k6_connection_split_20260826/
```

and write your report only to

```text
xmodel/max12-812-order2-square-d1-c2-c8-first-connection-hostile-review-grok-20260826.md
```

Return exactly one top-level verdict: `CONFIRMED`, `REFUTED`, or
`INCONCLUSIVE`. This is a narrow cell review. Do not promote it or compose it
with another D1/global theorem.

## Mandatory custody checks

1. Recompute the SHA-256 of `RESULT.md`, `EVIDENCE.sha256`, `FREEZE.sha256`,
   `AWS_LAUNCH_METADATA.md`, `PREREGISTRATION.md`,
   `compile_c2_c8_connection.py`, and `PRODUCER_FREEZE.sha256`; rehash every
   path named in the three manifests. The producer-freeze SHA is
   `a44cfc000e3f5156ceed2aff58fbaae24ca78316c6eeb405e8a7a800dd0a2d2b`.
2. Establish that exact Q on Box03 and `F_65519`,`F_65521` on Box02/r6d are
   three distinct registered AWS executions of the same frozen source
   archive, with on-host freeze checks, compiler rc zero, empty compiler
   stderr, runner rc zero, terminal PASS, no diagnostic, and zero swap.
   Exact Q is the characteristic-zero endpoint; the two primes are controls.
3. Audit the Singular 4.3.2 quotient-ring hazard. Verify directly that the
   compiled programs use ordinary polynomial rings and that no conclusion
   relies on noncanonical `qring` assignment, `==0`, `subst`, or `diff`
   without explicit reduction.

## Mandatory mathematical checks

4. Independently rebuild the primitive support census through grade 26 at
   boundary `(ord(A),ord(C),ord(R))=(8,8,7)`, including a padded replay.
   Verify there are no omitted source, load, moving-`p`, or target monomials
   capable of entering any of the seven literal equations through grade 26.
   Check the mechanically derived jet ceilings and sentinels: `k60_1`, both
   next-`C` coefficients, and `ell1` must actually enter.
5. Recompute from the literal seven-row program, without trusting PASS
   strings, the unique grade-25 source `(3/4)k60*C/L` and the complete
   grade-26 pole-two numerator

   ```text
   N2 = (3/4)AC L + (3/8)C^2 + (5/8)k0 RC L
      + (3/4)(k60_1 C+k60 Cnext)L - (3/4)ell1 k60 C.
   ```

   Check every coefficient and sign, especially the moving connection for
   `p(sigma)=p+2 sigma ell1+...`. Verify the analytic/literal coefficient
   bridges for all seven rows and both grades, and verify that all target
   rows truly begin after grade 26.
6. Audit the exhaustive scheme split `D(k60) union V(k60)`. On `D(k60)`,
   independently verify that the grade-25 seven-row ideal contains `1`
   before radicals on each exact-`C` chart
   `D(c1)` and `V(c1) intersect D(c0)`. State precisely which inverses are
   introduced and confirm that no leading coefficient of `A` or `R` is
   inverted.
7. On `V(k60)`, verify that every connection and next-`C` contribution
   proportional to `k60` vanishes while the free `k60_1*C/L` term remains
   pole one. On the finite etale cover `lambda^2=-p/2`, independently derive
   the exact pole-two pair

   ```text
   (3/8)(lambda*c1+c0)^2,
   (3/8)(-lambda*c1+c0)^2.
   ```

   Verify both exact-`C` chart ideals contain `1` before radicals, and explain
   descent from the finite etale cover. The Faber/root bridge is asserted
   only after adjoining `k60=0`; explicitly test that the unconditional
   moving-root gap is nonzero before the split.
8. Inspect the frozen V2 failure rather than discarding it. Decide whether
   its failed `ROOT_FABER=0` assertion is exactly the over-strong pre-split
   fixed-root bridge described by `RESULT_V2_FAILED.md`, and whether V3
   repairs that logical placement without hiding a mathematical failure.
   Also verify the controls: deleting the moving-connection term must break
   the full numerator identity, and deleting `C^2` must kill both root
   terminals.
9. Audit the claimed closed tail `ord(A)>=8, ord(R)>=7`: prove that increasing
   either contact cannot introduce a new lower-grade primitive family,
   change the pole ceiling, or advance a target through grade 26. Decide
   whether the four localized unit ideals establish scheme-theoretic
   emptiness of exactly

   ```text
   D(p*k0), ord(C)=8, ord(A)>=8, ord(R)>=7
   ```

   after the stated frozen generic-square/D1 unit-load source gates.

## Firewall

Do not extrapolate to `c>=9`, another primary or tied face, positive-order
leading load, `p=0`, `k0=0`, the exact-square zero section, a terminal/global
chart, fan exhaustiveness, order two, maximum twelve, or JC2. If anything is
wrong, identify the smallest failing byte, row, coefficient, branch,
localization, or contact value, and state the narrow surviving scope.
