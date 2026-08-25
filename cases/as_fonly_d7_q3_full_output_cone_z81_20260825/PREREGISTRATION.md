# Preregistration — first nonlinear full-output successor modulo 2187

Date: 2026-08-25

Consume the frozen modulo-729 solver source at SHA-256
`f6eaa0a0f1dabb785bdd4358fa84739d907820bc539cc619a1b692ad5755cb19`
and one of its three pinned reviewed Q3 parents.  Reconstruct, rather than
sample, its entire affine solution torsor

```text
F = F0 + 27*T,       T in (Z/27)^72,
det J(F) = 1 mod 729.
```

For a fresh order-729 output digit `W`, compile the exact next equation

```text
(det J(F0+27*T)-1)/729 + L_F0(W) = 0 mod 3.
```

Equivalently, retain the source-derived quadratic term
`det J(T_P,T_Q)` and all 91 determinant rows.  It is forbidden to replace
this by a fourth linear Bockstein.

First test the two source-honest linear subfamilies `T_P=0` and `T_Q=0`, on
which the quadratic term vanishes identically.  If neither contains a point,
emit the complete quadratic ANF and a non-overflow QF_BV formula in all affine
torsor coordinates.  A SAT result is accepted only after reconstructing
`T,W` and literally replaying every integer determinant coefficient modulo
2187.  An UNSAT claim requires a separately checked proof certificate.

Success proves only existence of a fixed-D7 lift modulo 2187 over the one
displayed Q3 fibre.  It proves no deeper/all-depth lift, collision over
characteristic zero, counterexample, or JC2 statement.
