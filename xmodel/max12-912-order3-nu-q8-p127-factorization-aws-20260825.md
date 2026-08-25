# Corrected Q8 factorization over `F_127`

Date: 2026-08-25  
Status: **PRODUCER-EXACT FINITE-FIELD FACTORIZATION; review required**

The monic corrected octic has the exact squarefree factorization

```text
Q8bar(v) = (v+60)(v-58)(v-26)
            (v^5+53v^4+38v^3+26v^2-9v-48)
```

over `F_127`.  Thus its Frobenius orbit partition is `1+1+1+5`, not one
orbit of eight contacts.  Frobenius invariance of a single geometrically
irreducible component can propagate one quintic-root contact to the other
four roots of that factor, but it does not propagate to the three rational
contacts.  A rational union of conjugate geometric components is not one
geometric component.

The first producer invocation is quarantined: Singular reported an in-script
type error but returned process status zero, and the preliminary runner's
marker check did not fail closed.  The frozen V2 replaced the faulty print
loop, rejects any Singular diagnostic in stdout or stderr, and completed with
empty stderr and the displayed factorization.  Only V2 is evidence.

This finite-field factorization has no characteristic-zero component-grouping
or trajectory consequence by itself.

