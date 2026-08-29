# V82QST0 reduced-coordinate diagnostic

Reporter-only successor to V82QSD.  Before the unchanged foreign-factor
assertion it serializes every exact reduced base-field coordinate of the
already-computed CURRENT conormal, including numerator/denominator factors,
orders along F/G/L/U/V, and scaled numerator/denominator residues modulo each
factor.  It also checks that F, G, and L occur exactly in the common
denominator.

No accepted CURRENT table is emitted when the assertion is false.  The purpose
is to localize pole-bearing rows for alternate-pivot and raw-fibre scheduling;
it makes no coefficient, cover, family, TD6, SP-2, landing, or JC2 claim.
