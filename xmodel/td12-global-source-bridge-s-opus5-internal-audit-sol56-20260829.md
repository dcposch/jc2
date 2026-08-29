# Internal hostile audit — `TD12-GLOBAL-SOURCE-BRIDGE-S/v1`

Reviewer: Sol 5.6 internal independent lane.  Date: 2026-08-29 UTC.
Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
Producer audited: `xmodel/td12-global-source-bridge-s-opus5-92e-20260829.md`,
literal full-file SHA-256
`3595fb88ef01fe72dce13cbb00b817a75a040f744764a8e34f865450c01b77d1`.

This is a provisional internal audit, not a promotion premise.  It used desk
algebra and the cited PDF only: no web, AWS, CAS, canonical edit, or
formalization-tree access.

## 1. Verdict

```text
MATHEMATICS = PASS_WITH_MATERIAL_REPAIRS
CUSTODY     = FAIL_PRODUCER_BODY_SEAL
MAXIMUM SAFE DISPOSITION = BRIDGE_AVAILABLE_AT_MAP_LEVEL /
                           VALUE_LEVEL_STILL_OPEN
```

The source shear, the branch-free Newton floor, the floor Keller dichotomy,
the core equality classification, the immediate sibling-floor identity, and
the degree lower bounds are sound after the repairs below.  No source value
of a positive-order sibling jet is obtained and no route is killed.

The most important strategic correction is positive: the proposed
`FLOOR-COORD` research descendant is not needed operationally for S17.
A generic source translation `x -> x+c` gives an Aut-equivalent normalized
representative with `ord_x f = ord_x g = 0`, while preserving the S17 cell.
This closes the S17 floor-coordinate fork *without* proving that the already
fixed literal coordinates have that property.  It does not transport a
future frozen `PairRef` automatically.

## 2. Custody and source check

The charged source recomputes as

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

The PDF text and glyph geometry on printed p. 15 really do contain three
typographical defects in the proof of Statement 3.9:

```text
x^(-kappa)              must be x^(-1/kappa),
x^((n-l)kappa)          must be x^((n-l)/kappa),
sum_(j=k)^l             must be sum_(j=k)^n.
```

They are forced by the immediately preceding printed identity
`eta_G=x^(1/kappa)(eta_F-c)`, by the parent sum ending at `n`, and by the
printed conclusion `d_G=d_F-l/kappa`.  Thus the producer's corrected source
formula is right, although the heading "two literal errata" miscounts the
three repairs.  The bbox reading of Notation 2.4 also passes:
`alpha/beta=k_f/k_g`; with `k_f<k_g`, type `(2,3)` gives
`k_g/k_f=l_g/l_f=3/2`.

The producer's internal seal does **not** recompute.  The byte offset of its
literal `## Seal` heading is `42545`, and the actual preceding-body digest is

```text
c4825be2dc3603031c2aad4caa6eb1cea40e57ae6c01a9d8ce19d1101f3cc2e0,
```

not the claimed `42816` bytes /
`c0c03d4edb1838f27ed0f1b86c8041568d41366a94f678209458ca3909831ac0`.
The literal full-file hash above remains an unambiguous object identifier, so
the mathematics can be audited, but the producer report is not internally
sealed and must not be promoted under its claimed body seal.

## 3. Claim-by-claim audit

### Theorem A — `PASS_WITH_REPAIR`

Let `n` be the largest parent index, `P_k=p_{h,n-k}`, and put

```text
Q_c(xi,eta) := xi^n h^F(xi,c+xi eta)
             = sum_(k>=0) xi^k P_k(c+xi eta).
```

Then the exact source identity is

```text
h^G(xi,eta)=h^F(xi,c+xi eta),
ord_xi Q_c=l=mult(P_0,c),
ord_c(P_k)>=l-k,
p_(h,G)(eta)=[xi^l]Q_c
             =sum_(k=0)^l [(z-c)^(l-k)]P_k(z) eta^(l-k).
```

This proves A1 and the intended A2/A3.  As printed by the producer, however,
`xi^l | h^F` is not the right statement: `h^F` is Laurent and `xi` is a
unit, while its lowest exponent is `-n+l`, not `l`.  Likewise A3 must read
`[xi^l](xi^n h^F(...))`; multiplying a coefficient extraction afterward by
`xi^n` is not literal algebra.  This is a normalization/parentheses repair,
not a failure of the vanishing ladder or child-top formula.

A4 passes: the shear `(xi,eta)->(xi,c+xi eta)` has determinant `xi`, so
Jacobians transform by exactly that factor.  The later chart identity
`J_(xi,eta)(f^F,g^F)=-kappa xi^(kappa u-kappa-1)` also has the correct sign
and exponent.

### Theorem B — `PASS_WITH_MINOR_ENDPOINT_REPAIR`

For `u>0`, every prefix exponent is strictly smaller than `u`; hence in a
monomial `x^J y^m` the pure `eta^m` term uniquely has least exponent
`J-um`.  Distinct support points on the minimal face have distinct
`eta`-degrees, so cancellation cannot erase the floor.  Therefore

```text
minexp_x h^F = sigma_h(u),
p_(h,min)=h_u^down(1,eta),
```

independently of branch, fibre value, and prefix.  At `u=0` the same theorem
holds because the prefix is empty and distinct `m` still prevents
cancellation, but the producer's slope-`1/u` sentence does not cover that
endpoint.  S17 has `u>0`, so this is harmless.

### Theorem C — `C1--C4 PASS_WITH_NOTATION; C5 SCOPE_REPAIR_REQUIRED`

The least-index row of the exact Keller convolution proves C1 and C2.  A
direct calculation for weighted-homogeneous faces gives

```text
J(f_u^down,g_u^down)
 = x^(-Gamma(u))
   (sigma_f P G' - sigma_g P' G),
```

so it is `1` when `Gamma=0` and `0` when `Gamma>0`.  C3 is correct on the
charged `kappa_F` lattice: `kappa_F u` and `kappa_F sigma_h(u)` are integral,
and the floor offset is `s*+kappa_F Gamma(u)`.  C4 is also correct, but powers
with rational or negative `sigma` must be read after clearing denominators
as an equality in `C(eta)^*`; "homothetic" is a divisor/UFD statement, not a
choice of fractional polynomial powers.

C5 is false at the theorem's stated scope of *any* Jacobian pair.  For
`(f,g)=(x,y)`, `Gamma(u)=0` for every `u`, so it does not tend to infinity.
The limit proof explicitly imports Lemma 2.1's normalized-counterexample
hypothesis `l_f,l_g>=1`.  Repair C5 to normalized counterexamples (or at
least `deg_y f+deg_y g>1`).  Also, convexity and nonnegativity alone do not
show that a nonempty zero set contains `0`; that conclusion uses Theorem D's
equality classification.  On the S17 normalized-counterexample scope, the
repaired C5 is valid.

### Theorem D — `CORE PASS; CONSEQUENCES PASS_WITH_SCOPE_AND_SIGN_REPAIRS`

For `u=q/p>0`, writing the two minimal faces as

```text
x^A y^B Phi(x^q y^p),   x^C y^D Psi(x^q y^p)
```

gives exactly the producer's bracket.  If its Jacobian is `1`, exponent
counting forces `A+C=B+D=1`; the nonzero determinant leaves only the two
coordinate orientations.  The leading bracket coefficient is respectively
`1+p deg(Psi)+q deg(Phi)` or its negative analogue, so both one-variable
factors are constant.  Thus the equality classification is sound.

State the orientation explicitly:

```text
(f_u^down,g_u^down)=(c1 x,c2 y), c1*c2=1,
or                       (c1 y,c2 x), c1*c2=-1.
```

"Up to swapping" without the sign repair is imprecise.  The inference
`x|f` follows because `J-um>=1` for *every* support point and `m>=0`; the
producer's phrase "taking m=0" does not itself exclude points `(0,m)` with
`m>0`.  The conclusion is nevertheless correct.

The bounded interval and formulas using `(k_f,l_f),(k_g,l_g)` require the
normalized-counterexample scope of Lemma 2.1, not an arbitrary Jacobian
pair.  At that scope, if equality occurs at positive `u`, then one member is
divisible by `x`, `Gamma(0)=0`, and convexity makes the zero set an initial
interval.  The contrapositive used below is valid.

### Theorem E — `PASS_WITH_SCOPE_QUALIFIERS`

Immediate children at the same height have identical floors because
Theorem B depends only on support and height.  The same holds at a deeper
level only conditionally when both actual towers exist at the same height on
the same fixed lattice; it supplies no occurrence.  Equality of `rho` should
be stated only where C4 defines it (`sigma_f sigma_g !=0`).  Equality of row
distances also presupposes the same `kappa_F` lattice.  With those qualifiers,
the floor identity is correct.  It neither equates positive-order sibling
vectors nor creates a trace/norm constraint.

### Theorem F — `PASS_WITH_ONE PROSE REPAIR`

The coefficient of `eta^(deg_y f)` in the full chart is nonzero, so every
row has eta-degree at most `deg_y f` and

```text
l_f=deg_y f >= deg_eta(p_(f,F))=68i.
```

Lemma 2.1 gives `l_f<=k_f`, retains the corner `(k_f,l_f)`, and confines the
support to its rectangle.  Hence

```text
k_f>=68i,  deg f=k_f+l_f>=136i.
```

For type `(2,3)`, the verified ratio `3/2` gives
`l_g,k_g>=102i` and `deg g=(3/2)deg f>=204i`.  The transposed bounds are also
safe.  No ceiling follows.  Section 8 remark 2 begins with the contradictory
sentence "Only the deg f half needs the type"; it must say **only the g-side
bounds need the type**.  The displayed theorem and the next sentence already
use the correct logic.

## 4. `FLOOR-COORD` is a coordinate gauge, not the next S17 lemma

For `c in C`, set

```text
(f_c,g_c)(x,y) := (f,g)(x+c,y).
```

No target translation is needed.

1. The source translation has Jacobian one, preserves `J(f,g)=1`, total
   degrees, invertibility/noninvertibility, and the Aut-equivalence class.
   Therefore lexicographic degree minimality is preserved.
2. Expanding `(x+c)^J y^m` creates only `(x^r y^m)` with `r<=J`.  Thus the
   Lemma 2.1 Newton rectangles survive.  The corner coefficients at
   `(k_f,l_f)` and `(k_g,l_g)` are unchanged, so the same four integers,
   inequalities, nonintegral ratio, and type survive.  The translated pair
   is another normalized representative.
3. Write `f=sum_m f_m(x)y^m`, and similarly for `g`.  The corner condition
   makes `f_(l_f)` and `g_(l_g)` nonzero polynomials.  A single `c` outside
   their two finite zero sets gives nonzero coefficients
   `f_(l_f)(c)y^(l_f)` and `g_(l_g)(c)y^(l_g)` at `x^0`.  Hence
   `ord_x f_c=ord_x g_c=0`.  In fact, for every `u>0`, both translated
   support functions are strictly negative, so C4's nonzero-sigma rider is
   also automatic.
4. Projectively `[X:Y:Z]->[X+cZ:Y:Z]` fixes the line at infinity.  At an
   x-pole the local parameter changes by
   `z=1/x -> z/(1+cz)`, an analytic unit tangent to the identity.  Fibre
   values, infinity points, branch contacts, characteristic indices, and the
   Eggers--Wall tree are transported isomorphically.
5. More concretely,
   `(x+c)^(-q)=x^(-q)+sum_(n>=1) binom(-q,n)c^n x^(-(q+n))`.
   Thus every Puiseux coefficient of exponent `<1` is unchanged, and common
   lower terms contribute common corrections that cancel in branch
   differences.  In S17,
   `u=1-13/kappa_F` with `17|kappa_F`, so `4/17<=u<1`.  Its prefix and top
   weighted row are therefore unchanged.  The reduced polynomial `p`, its
   `A,B_+,B_-` roots, `D_F`, `kbar_F`, `nu_F`, `kappa_F`, and the three
   direction occurrences transport to the translated pair.

Consequently one may choose this translated normalization before consuming
the S17 cell.  Then `Gamma(0)=1`, and Theorem D gives
`Gamma(u)>0` for every positive tree height.  The floor Keller row is never
the inhomogeneous row; with the stronger generic choice above, the floor
always satisfies the homogeneous C4 relation.  Therefore §5.4's conditional
nonzero floor compatibility is not cashable in the WLOG S17 coordinates,
and `TD12-S17-FLOOR-COORD/v1` should not be launched as a research fork.

This is **not** a proof that the producer's already fixed literal coordinates
have `ord_x f=ord_x g=0`.  It is an existence/WLOG theorem for an
Aut-equivalent normalized representative.  If a future artifact freezes an
exact `PairRef`, completion, or coefficient vector, the source translation
and induced tree/chart maps must be serialized before transferring values.
No such value-level object exists in this source-bridge lane, so there is no
present transport conflict.

## 5. Maximum safe campaign consequence

Promotable only after a differently modeled review and a repaired/correctly
sealed producer or coordinator integration:

- the exact source shear and normalized child-top/vanishing formulas;
- the branch-independent Newton floor (Theorem B);
- C1--C4 and D at their repaired scopes;
- immediate sibling-floor equality with E's qualifiers;
- the S17 degree lower bounds of F;
- the generic-source-translation lemma, which closes the operational S17
  `FLOOR-COORD` fork WLOG and directs work back to intermediate/source jets.

Not supplied: any positive-order child value, `PairRef`, occurrence proof,
landing, exclusion, degree ceiling, Keller counterexample, or JC2 result.

<!-- END-SEALED-BODY::td12-global-source-bridge-s-opus5-internal-audit-sol56-20260829 -->

## Seal

- Body definition: all bytes before the literal `## Seal` heading.
- Body byte count: `12410`.
- Body SHA-256:
  `d0c1c700e60b88e64a3e317d1a0b9d09fcf2943988a5151ca7c5bc14534cf631`.
- Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
- Producer literal full SHA-256:
  `3595fb88ef01fe72dce13cbb00b817a75a040f744764a8e34f865450c01b77d1`.
- Literal full-file SHA-256 of this audit is an external custody value,
  reported to the coordinator after this immutable seal is written (a file
  cannot literally contain its own ordinary SHA-256).
