# Preregistration: complete D7 output-digit cone over Z/9

Consume the CONFIRMED Q3 affine fibres at the three pinned Q5 predecessor
points `base0000`, `base0270`, and `base0513`.  For one fixed Q3 particular at
each point, adjoin arbitrary polynomial output corrections of total degree at
most seven:

```text
P = P0 + 27 U + 81 V,
Q = Q0 + 27 W + 81 Z.
```

Equivalently, combine each coefficient into its unique residue
`T=U+3V in Z/9`.  Compile every determinant coefficient of total degree
0 through 12.  Since the determinant is bilinear and `27^2=729` is zero
modulo 243, the condition `det J(P,Q)=1 mod 243` is a linear congruence module
over `Z/9`.  Solve it by the exact mod-3 kernel plus Bockstein lift, not by
enumerating canonical carries.

Required checks:

1. all 91 source coefficients of `det J(P0,Q0)-1` are divisible by 27;
2. all 72 combined coefficient variables (36 per output) are present,
   including derivative-zero constants as explicit zero columns;
3. the complete reviewed Q3 kernel is absorbed by the arbitrary order-81
   output space, and every Q3-kernel/fresh-basis mixed second difference is
   divisible by `81*27=2187` coefficientwise;
4. direct degree/double/pair controls certify linearity modulo 9 after `/27`;
5. an UNSAT result carries an exact F3 left-null/Bockstein certificate; a SAT
   result reconstructs `U,V,W,Z` and replays every integer coefficient modulo
   243;
6. record exactly which fresh output degrees can hit row 8=`x^2 y`.

This gate is source-complete only for output coefficient digits supported in
the fixed total-degree-seven monomial set at orders 27 and 81 over the three
pinned Q3 fibres.  It does not include order-243 digits or require terminal
divisibility modulo 729.  A source reparametrization is covered only insofar
as its resulting output perturbation lies in this fixed support.  No global
predecessor, all-depth, counterexample, or JC2 inference is licensed.

All execution is AWS-only.
