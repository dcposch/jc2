# Selected-Q8 hierarchical Padé gate at orders 16 and 32

Date: 2026-08-25  
Status: **PRODUCER-EXACT BOUNDED NEGATIVE; review required**

An AWS Box03 replay refined the frozen all-1330 common-denominator test into
the following hierarchy:

```text
seven individual coordinates: 190 sequences each
normal triple (c,d2,d4):       570 sequences
invariant triple (x1,x3,x5):   570 sequences
six true-centre coordinates:  1140 sequences
all seven including inv:       1330 sequences
```

The independent order-16 jet is an exact prefix of the order-32 jet in every
sequence.  For every one of the eleven groups, exact Gaussian elimination
found no unique full-rank scalar denominator in the complete order-32
rectangle

```text
1 <= denominator degree d <= 31,
0 <= common numerator bound m <= 30.
```

The replay completed rc zero in 6.97 seconds with 20,464 KiB maximum RSS.
Its source and controls are pinned by the portable verifier.

This does not exclude rank-deficient affine fits, any higher-degree formula,
or denominators singular at the base point.  It proves no quotient-component
membership and supplies no original-row, characteristic-zero, boundary, or
trajectory conclusion.  Order 64 and higher remain charged; a later unique
candidate must survive a strict higher-order holdout and exact substitution
in every original quotient row modulo `H(w,v)`.

