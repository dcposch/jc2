# D1 smooth-discriminant coordinate-action design

Date: 2026-08-26 UTC

Status: **EXACT DESIGN; UNIVERSAL IDENTITY TEST TO RUN ON AWS.**

## Smallest theorem sought

Write the depressed cubic near its double-root discriminant as

```text
p=-3a^2,  c=2a^3+h,  K=z^3+pz+c.
```

The map `(a,h)->(p,c)` has Jacobian determinant `-6a`; hence it is etale
where `a` is a unit.  Its discriminant is exactly

```text
Delta=-4p^3-27c^2=-27h(4a^3+h).
```

The source scaling

```text
f(z)       -> a^-9 f(a z),
Lambda,rho -> a^-1 Lambda,a^-1 rho,
h           -> a^-3 h,
(q2,q1,q0) -> (a^-4 q2,a^-5 q1,a^-6 q0),
(r2,r1,r0) -> (a^-7 r2,a^-8 r1,a^-9 r0),
tau         -> tau
```

should send row `E_i` to `a^-(12+i)E_i`, with fixed `k,mu,nu`.  Therefore
the V8 combination transports using multiplier
`a^(8-i)F_i(hat variables)`.  The fixed V8 multipliers require exactly the
common denominator `a^3`.  After clearing it, the proposed universal
polynomial identity is

```text
sum_i [a^(11-i) F_i(hat variables)] E_i(a,h,Q,R)
    = a^23 W_V8(hat variables).
```

Its distinguished term is `a^3 Lambda^20`.  If this identity and the row
covariance hold coefficientwise, then after localizing at `a` the reviewed
V8 initial-term obstruction transports to every unit-axis point with the
same normalized valuation inequalities.  For arcs centered at `h=0`,
`4a^3+h` is a unit, so `v(Delta)=v(h)`.

## Smallest exact experiment

On two AWS hosts, reconstruct the charged rows twice: first at
`a=1,p=-3,c=2+h`, then universally at `p=-3a^2,c=2a^3+h`.  Reconstruct the
literal V8 multipliers and 48-term witness from source.  Verify separately:

1. every row covariance, including row-3 and row-8 target loads;
2. minimum common denominator exponent exactly three;
3. the cleared full combination above as a literal polynomial identity;
4. `a=1` specialization equals the frozen V8 witness SHA;
5. the discriminant factorization and the unique `a^3 Lambda^20` target;
6. all universal monomial/weight records, preserving a possible later
   positive-axis-valuation cone analysis.

Opposite arithmetic traversals must agree after deleting custody fields.

## Firewall

Success proves covariance only on `D(a)` with fixed loads and the frozen
ordinary-tail presentation.  It does not cover the singular point `a=h=0`,
moving loads, another source chart, or the global landing theorem.  A cleared
identity with target `a^3 Lambda^20` is an `a`-localized initial-term
certificate, not an unlocalized assertion that `Lambda^20` itself lies in
the row ideal.  The triple-root weighted blow-up remains separate.
