# V2 preregistration: first theorem-grade cyclic-D1 slice

Date: 2026-08-25  
Execution: AWS Linux only  
Parent scope: immutable V1 `PREREGISTRATION.md` SHA-256
`41385708ea2ab969b6d08ead5a48d3be4fabe20d980167528fe45840fd5137d4`

V2 does not weaken or replace any V1 boundary, load, Taylor, or replay
obligation.  It registers three executable interfaces.

## A. Independent source reconstruction

Two algorithms must agree exactly before any row is consumed.

1. The frozen-parent reference uses only the parent's Faber, inverse-root,
   and target-coefficient functions.  It does not use `compile_fibre()`.
2. `independent_reconstruct.py` imports no parent/shared arithmetic.  It
   computes `F6` and `F12` by the differential recurrence for
   `(1+U)^alpha`, computes `z(w)` by sequential Laurent coefficient
   cancellation, and extracts tails by a separately written convolution DP.

Exact plain-dictionary equality is required for `F6`, `F12`, `g`, the
inverse root through `w^-19`, and all eight tails.  The independent lane also
checks `f(z(w))=w^9`, the missing `w^0` and `w^-9` inverse-root terms, and
`g(z(w))=w^12+k*w^6-sum r_l*w^-l` through `w^-8`.  Character descent and CAS
rows consume the independent tails only.

Any mismatch is a source failure, with no mathematical inference.

## B. Stage-A generic navigation and exact section certificates

The generic job computes a characteristic-zero standard basis and
`absPrimdecGTZ` over `Q(s,k,mu,nu)` for all eight D1 incidence rows.  This is
the generic point of load space: the coefficient field inverts every nonzero
polynomial in `k,mu,nu`, not merely `k`.  It emits every absolute class,
conjugate count, dimension, degree, and generators at that generic point.

This output is **navigation only**: algebraic closure of
`Q(s,k,mu,nu)` does not distinguish a finite extension of the constant field
`Q(k,mu,nu)` from an algebraic cover whose primitive element depends on `s`.
No class is called a section from `absPrimdecGTZ` alone.

The positive certificate interface instead requires:

- a polynomial for a primitive constant `theta` over `Q(k,mu,nu)`, written
  before `s` is introduced and proved irreducible; or the trivial extension;
- eight explicit `A_i(s,theta)` rational functions;
- every denominator/open condition used.

The emitted Sage verifier reconstructs the constant extension and checks all
eight original descended rows exactly.  A pass certifies one geometric
degree-one section over `P1_s`; it does not certify that the list is complete.

An exclusion theorem remains fail-closed until every generic absolute class
and every Fitting/discriminant/load stratum (including `mu=0`, `nu=0`, their
intersection, and every new discriminant divisor) has a separately generated
exhaustive constant-field section/no-section certificate with two-sided ideal
containments.  The current certificate schema proves degree one over a finite
extension of `Q(k,mu,nu)` at the generic load point; specialized load strata
must declare their own constant base and are not silently inferred from it.

## C. Stage-B Taylor ideal for one certified section

For one passing Stage-A certificate, `stage_b_taylor.py` retains the full
18-parameter centre

```text
R0=sum_(d=-6)^(-1) c_d*s^d + sum_(d=1)^12 c_d*s^d,
r=u*R0,  u=t^2/(s-1)^2,  t^3=s.
```

It rebuilds `f`, `F6`, `F12`, and `g`; verifies the eight Stage-A rows and
the exact D1 `h`/terminal identities; then forms all 23 coefficients

```text
u^ell*f^(ell)(r)/ell!, ell=0..9,
u^ell*g^(ell)(r)/ell!, ell=0..12.
```

For each coefficient in the basis `1,t,t^2`, it kills the noninvariant
coordinates.  For the invariant coordinate `N(s)/D(s)`, write
`D=(s-1)^B D_other`.  Exact membership in `C[x]`, `x=s/(s-1)`, is imposed by

```text
D_other divides N, and deg_s(N/D_other)<=B.
```

Every resulting coefficient is an equation in the 18 centre parameters.
If any denominator depends on a centre parameter, the compiler refuses:
this prevents an unannounced saturation of a special Taylor stratum.

Before consuming a real section, the membership routine must pass four exact
synthetic controls: an arbitrary polynomial in `x=s/(s-1)`, the zero
function, a rejected pole at `s=-1`, and a rejected numerator whose degree
exceeds its `s=1` pole bound.  The zero control separately guards Sage's
`degree(0)=-Infinity` edge.

`stage_b_membership_controls.py` exposes those four checks without a Stage-A
certificate.  It runs exact `QQ` arithmetic under pinned SymPy 1.13.3, uses
the same divisibility/degree criterion, handles the zero quotient before any
degree coercion, and emits a tag-independent canonical digest.  It is code
coverage of the membership predicate only, not evidence that a D1 section
exists.

The output is an exact Taylor ideal, not a solved ideal.  SAT still requires
literal reconstruction of `P,Q`, all 23 Taylor coefficients, all eight tails,
the terminal row, resultants, and the constant Jacobian.  UNSAT still requires
an independently checked exact ideal/certificate and all Stage-A strata.

## D. Stop/firewall

- Amazon-EC2 DMI identity, a registered unique tag, and a previously absent
  result directory are mandatory; Linux alone is insufficient.
- Two-hour and 128-GiB cap per generic CAS lane.
- No theorem from generic dimension, degree, modular data, a higher cover, or
  an incomplete component list.
- Fixed-load modular `msolve` ranks/degrees and the `s`-retained
  characteristic-32003 lane are navigation only.  Even repeated fibre rank
  does not prove flatness, absolute irreducibility, or absence of a
  characteristic-zero degree-one component.
- `k=0`, `mu=0`, `nu=0`, coefficient infinity, base points
  `s=0,1,infinity`, resultants, and the D1 collision boundary retain the exact
  V1 firewall.
- V2 covers no higher passport, order-one Kummer leaf, `(8,12)`, all
  maximum-twelve maps, counterexample, or JC2 conclusion.
