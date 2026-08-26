# V27 strengthened clearing audit

V24 already gives an exact original-row source identity and records the LCM
of every raw, first-row, and relation denominator.  Its conservative
termwise denominator is the product of the relation and first-row LCMs.

V27 leaves the center, matrices, pivot orders, P12, division, source lift,
negative control, birational coverage, and sentinel descent unchanged.  It
adds executable assertions that every coordinate denominator divides its
reported LCM and that every individual source-multiplier/source-row product
is cleared by the reported termwise denominator.  It prints the exact number
of audited term slots.  This closes the explicit cleared-denominator custody
requirement; V24 remains the independently completed mathematical precursor.
