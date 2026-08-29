# Registration: H17/q7/a3 sequential reduction through grade 51

Date: 2026-08-26

Status: preregistered exact sparse producer; fixed normalized graph only.

## Question

Starting with the complete frozen V5 rows in absolute grades 48--51, does
the corrected grade-48 predecessor prolong on each of the two surviving
projective charts, and is the candidate grade-51 Kummer equation the sole
residual compatibility through that grade?

## Exact input

Use the immutable V5 exact-Q and F65521 row/function payloads.  Their
canonical hashes are checked by the engine before any reduction:

```text
Q rows       1e626d0832d511a2bea5936eb1d687084f51a58f7f44062af23c3f71e88318ee
Q functions  71ff2027b1d17c421bb84738a7298eed3f8136d8f488b39ab5f9414767c2542a
F65521 rows  f33ab36df9f3a2db2684de2feab0195420926729a8cb8a1bcf43b2b4842d857e
F65521 funcs 70ffdc19efde934dde590fa5b475b0a73df5b709ded8de9a9a878d9bca41c1a0
```

The V5 producer remains the complete-source compiler.  V6 is a second,
independent Laurent-polynomial reducer and does not reconstruct or trim
the source rows.

## Preregistered pivots

For each grade `g=48,49,50,51`, put `j=g-48`.  On `D(x0*p*m)` solve in
the order

```text
P1 -> s0j,  P3 -> yj,  P6 -> d2j,  P2 -> dmj,  P4 -> d4j.
```

On `D(y0*p*m)` use the same order with `P3 -> xj`.  Every pivot must be a
single Laurent monomial unit in the registered localization.  After each
solve, substitute into every remaining row and both frozen grade-51
functionals.  Grades 48--50 must leave `P5=P7=0` on both charts.

At grade 51, after the five ordinary pivots, require the literal identities

```text
K51 = P5_51,
H51 = 16*p*P5_51 + 64*P7_51.
```

Then `K51=0` must solve the still-free `d60` with

```text
d60 = 36*(r00*m^2-y0^2)/p^4
      -5*kk0*a3^2*p - 2*m^3/(a3*p^4),
```

interpreted after the chart's earlier substitutions.  The final residual
must be exactly

```text
P7_51 = H51/64,
H51 = -2*m^3*p^2 + (5/4)*kk0*a3^3*p^7.
```

## Controls and stop conditions

- Arithmetic is exact over Q; F65521 is an independent software/control
  lane and every registered pivot denominator is nonzero there.
- A missing input hash, non-monomial/nonlinear pivot, nonzero lower
  residual, failed K/H row identity, wrong `d60`, or extra grade-51
  residual is an immediate fail-closed stop.
- The engine emits the final Laurent solutions and residuals for both
  charts, rather than relying on PASS tokens alone.

## Scope firewall

A PASS proves only finite prolongation through grade 51 in the fixed
normalized `(H,q,ord(a))=(17,7,3)` graph on the two registered charts.  It
does not prove an all-orders formal arc, literal-source/total-Rees
accessibility, terminal `[6,2]`, either finite Taylor pullback, order-two,
maximum-twelve, or JC2 closure/counterexample.
