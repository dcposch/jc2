# Registration: `c>=3,r>=1` universal receiver V2 scalar repair

Date: 2026-08-26

V1 correctly failed closed after both fields passed the complete source
division and all twenty-one grade-13--15 source/Laurent row identities.  Its
last sentinel compared the unscaled common numerator with `-A0^3`; the
actual unscaled cubic term is `-(1/16)A0^3`.

This V2 pins the immutable V1 compiler and freeze, changes exactly that
normalization in the emitted Singular input, and retains every source,
moving-row, numerator-division, and dual-field check.  No mathematical scope
is changed.  Exact Q is the producer gate and `F_65521` is a control.
