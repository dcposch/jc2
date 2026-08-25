# Hostile review prompt: normalized B9 common-cubic family at `3^11`

Audit
`xmodel/as-b9-9-12-common-cubic-3p11-producer-20260825.md` and
`cases/as_b9_9_12_common_cubic_3p11_20260825/` fail-closed.

Required charges:

1. confirm the V2 zero-modulus bug and prove that no V2 UNSAT artifact is
   consumed;
2. audit every V3 bit-vector constructor call, positive modulus/divisors,
   width/overflow bound, 276 determinant rows, and 23 top-form rows;
3. verify byte equality of V3 SMT SHA `5af9efbe...` and the independently
   repaired formula;
4. inspect the independent compiler at SHA `46019958...`, which must not
   consume producer SMT, and reproduce stage ranks/family dimensions
   `94/55,123/81,131/99,132/116,132/133`;
5. verify the first quadratic split `17+116`, fresh rank/kernel/cokernel
   `94/55/205`, spectator rank 38, and zero residual equations;
6. prove the inferred exponents 95 and 150 from an injective complete
   parameterization, or reject those counts while preserving any valid SAT
   claim;
7. independently replay the witness H `[1,119880,40581,0]`, all 299 rows,
   leading units, fixed parent, and exact degree pair `(9,12)`;
8. enforce the one-parent, finite-depth refusal scope and distinguish an
   integral congruence incidence from a characteristic-zero Q8 landing.

All substantive replay is AWS-only.  Write the verdict to
`xmodel/as-b9-9-12-common-cubic-3p11-review-grok-20260825.md`.
