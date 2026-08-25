# Preregistered kernel classification

Using the exact `299 x 149` integer Jacobian emitted by the primary run,
compute its rational right kernel and compare it with the three source-defined
target directions

1. translation of `P` by a constant;
2. translation of `Q` by a constant;
3. the degree-compatible target shear `Q -> Q + t P`.

The third direction is licensed because `deg(P) <= 9 < 12`, so it changes no
degree-12 coefficient of `Q`; it preserves both the determinant and the two
displayed common-cubic top-form equations exactly.  Certify exact kernel
membership, independence, and exhaustion.  As a negative/interpretive
control, test the target scaling direction `(delta P, delta Q)=(P,-Q)`:
because the stored integer representative satisfies the common-cubic rows
only modulo `3^11`, this need not be an exact rational-kernel direction even
though its image is divisible by `3^11`.

This classifies only the rational right kernel of this one displayed
Jacobian.  It does not quotient the much larger mod-3 tangent kernel and does
not prove a Hensel criterion or an all-depth lift.
