# Source-complete Q3 gate over the full Q4 affine kernel

Consume the complete 68-row Q4 producer at SHA-256
`ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4`.
Retain every Q4 kernel coordinate and adjoin all ten coefficients of
homogeneous `(H4,J4)` at order 81.

The exact gate has four degree-three source rows and all 63 recomputed
over-cap terminal rows in degrees 7 through 12.  Extract it from the literal
integer determinant, proving that the degree-three coefficients are exactly
divisible by 81 and the terminal coefficients by 243.  Prove the resulting
map is affine on the whole ternary cube by a complete quadratic design, solve
all rank strata exactly, reconstruct a particular on SAT, and directly replay
Q4, Q3, and terminal rows.

Also emit the coefficientwise 3-adic valuation minimum of every determinant
degree 0 through 12 before and after Q3.  This table is a typing diagnostic:
it must identify where the naive fused order-81-only Q2--Q0 successor lacks
earlier source pieces.  No complete-map claim is permitted.

All substantive execution is AWS-only.  Initial mandatory points are the
structurally distinct base0000 and base0270 full-Q4 fibres; base0513 is a
comparison control.

