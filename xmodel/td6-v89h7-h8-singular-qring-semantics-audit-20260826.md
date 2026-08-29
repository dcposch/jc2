# Audit: Singular qring semantics versus TD6 V89H7/H8

Date: 2026-08-26

Verdict: **UNAFFECTED.**

## Trigger

Singular 4.3.2 quotient-ring objects need not be canonically reduced for
assignment, equality, substitution, or differentiation.  Therefore a
`qring` assertion such as `p==0` is not reliable unless `p` is explicitly
reduced by the quotient standard basis.

## Charged artifacts

- V89H7 producer result SHA
  `49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd`.
- V89H7 hostile report SHA
  `99f7124e50db3daded967f42fe7591c06e27cfa05fe681537fed3aab5013ad6b`.
- V89H8 producer result SHA
  `646dd1162cc2e6aa36c3fe72bea5c64a44e19361323593a12fc4c7f137cc0292`.
- V89H8 hostile report SHA
  `49865ee96582302b6bb9a1aa6aa47733ab88dc738d28ed67861b804a2d90240a`.

## Dependency audit

The controlling V89H7/H8 chain is

```text
V89H8 -> V89H6 -> V89H5 -> V87 -> V86 -> V85 -> frozen Python compiler
V89H7 -> V89H6 -> V89H5 -> V87 -> V86 -> V85 -> frozen Python compiler.
```

Every executable in this chain is Python.  Exact base arithmetic is
python-flint `Q[V,U]`, `Q[C,V,U]`, their fraction fields, and the explicit
18-dimensional E3 algebra.  q arithmetic is the custom sparse `QPoly`
polynomial class, whose constructor combines equal monomials and deletes
zero coefficients.  `F=0` is applied by the explicit flint rational
substitution `C=(V^2-U^3)/U`; it is not a quotient-ring assignment.

Recursive searches of both frozen case directories and their transitive
payload found no `.sing`, `.lib`, or `.sage` executable and no `qring`
declaration.  The only `Singular` occurrences are hostile-review statements
that Singular was not used.  The decisive equalities are exact Python/flint
object equalities after canonical sparse construction: two-sided matrix
products, original-FIRST recovery, literal-P12 replay, q-support equality,
and exact rational-functional equality.  No `subst` or `diff` call from
Singular is consumed.

V89H9 and the live V89H10 clients use the same Python/flint/QPoly chain and
are likewise outside this Singular semantic hazard.

## Firewall

This note protects only the listed TD6 V89H7/H8 promotions and their direct
V89H9/V89H10 successors.  It does not validate any other campaign artifact
that used Singular quotient rings; those require explicit
`reduce(...,std(quotient_ideal))` checks at every equality/substitution/
differentiation boundary.
