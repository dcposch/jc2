# Rank-four `R4-CYCLE-1`: ruling-aligned logarithmic-Jacobian obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`genus3_cable_recovery` successor lane)  
Frozen basis: `30f89ce1b911f997758a9bf980c72ed19dca0fed`  
Lifecycle: **FINAL+VERIFIED EXACT NARROW OBSTRUCTION / HORN OPEN**

## 0. Verdict

Work conditionally in the charged one-cusp cyclic pseudo-plane package.  In
the Laurent deck coordinates one has

```text
M=C(U)=C(X,S),             X=x^mu,
S=x(y+g(x)),               mu>=2,
J_(X,S)(F,G)=c/(mu X),     c!=0,                       (0.1)
```

where `F,G in O(U)` pull back to polynomials on the retained affine plane
`A2_(x,y)`, and `K=C(F,G)` has `[M:K]=4`.

The new exact obstruction is:

> **Ruling-aligned coordinate theorem.**  Neither `F` nor `G` can belong to
> `C(X)`.  More invariantly, after any polynomial automorphism of the target,
> neither new target coordinate can pull back to a rational function of the
> ruling coordinate `X` alone.

Indeed, regularity and surjectivity of the ruling first turn an alleged
`F in C(X)` into `F=phi(X)` with `phi in C[X]`.  The logarithmic Jacobian
equation then has the unique general solution

```text
G=c*S/(mu*X*phi'(X))+h(X),       h in C(X).            (0.2)
```

After pullback to the retained plane, its `y`-derivative is

```text
partial_y G
  =c*x/(mu*x^mu*phi'(x^mu)).                          (0.3)
```

If `k=ord_(X=0)(phi')>=0`, the right side has `x`-adic order

```text
1-mu*(k+1)<0,                                           (0.4)
```

contradicting polynomiality of `G`.  The same argument with the coordinates
interchanged excludes `G in C(X)`.

The field-degree condition makes the statement still sharper.  Equation
(0.2) gives `M=K(X)` directly and

```text
[M:K]=deg(phi).                                        (0.5)
```

Thus any ruling-aligned coordinate in the charged row would have to be a
quartic polynomial in `X`; (0.3)--(0.4) exclude it.  No use of Formanek's
theorem is needed for this narrow result, so the existing primary-source
access gap for the stronger Formanek input is preserved rather than silently
upgraded.

This is not a full exclusion of the one-cusp horn.  It proves that any
surviving pair is genuinely mixed: **both** target coordinates must depend
essentially on the fibre variable `S`.  The inverse-Kummer and monogenic-index
controls remain intact.

## 1. Frozen inputs and exact scope

The committed inputs are:

```text
0e2e09c8a81cead797483cfd91f093c98ccba48ca50767056aa42ac709214b94
  xmodel/block-descent-a1-quartic-cycle1-invariant-ring-quartic-gate-control-sol56-20260830.md
bcc5148aba1a6cb095401ae8871e184ba6bb3e540395a23c40edc16cb0e363a8
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md
4eb16c9422fd167646d7161a359d05f95deaf5925d4650b3822b395329e124b4
  xmodel/block-descent-a1-quartic-cycle1-index-at-infinity-resultant-control-sol56-20260830.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190
  xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
```

Only the following consequences are charged here.

1. `U` is a smooth affine surface with an `A1`-fibration whose unique
   multiple fibre is `mu*Phi`, `mu>=2`.
2. The canonical cyclic source has retained chart `A2_(x,y)` and
   `X=x^mu`; after the Laurent translation the second invariant coordinate is
   `S=x(y+g(x))`, with `g in C[x,x^(-1)]` and no `y`-dependence.
3. Every element of `O(U)` pulls back to a polynomial in `C[x,y]`.
4. The charged quartic pair `F,G in O(U)` obeys (0.1) and
   `C(U)=C(X,S)` with `[C(U):C(F,G)]=4`.

The proof does not use the detailed `(3,1)+(2,2)` boundary packet.  It is
therefore a degree-independent ruling-alignment obstruction followed by the
degree-four specialization (0.5), not an exclusion of arbitrary mixed pairs.
It also does not assert that `X` is a target coordinate or that the ruling
descends to the target.

## 2. Regular functions of the ruling variable

We first record the small intersection fact used in the proof:

```text
O(U) intersect C(X)=C[X].                              (2.1)
```

To see this, write an element of the left side as `R(X) in C(X)`.  The ruling
`X:U->A1` is surjective.  For every `lambda!=0`, the divisor of
`X-lambda` is the corresponding reduced irreducible ruling fibre.  At
`lambda=0`, it is `mu*Phi`.  A finite pole of `R` at `lambda` therefore has
negative order at the generic point of that nonempty fibre (multiplied by
`mu` at zero), contradicting regularity on the normal surface `U`.  Hence
`R` has no finite pole and lies in `C[X]`.

This argument uses the actual ruling fibres.  It is not the false shortcut
that replaces the single-valuation intersection defining `O(U)` by a scalar
weight inequality.

## 3. Exact logarithmic-Jacobian obstruction

Assume for contradiction that `F in C(X)`.  By (2.1),

```text
F=phi(X),                    phi in C[X], phi nonconstant. (3.1)
```

The logarithmic equation (0.1) becomes

```text
phi'(X)*partial_S G=c/(mu X).                          (3.2)
```

The constants of `partial_S` in `C(X,S)` are exactly `C(X)`.  Integrating
(3.2) in characteristic zero gives the full solution set

```text
G=c*S/(mu*X*phi'(X))+h(X),       h in C(X),            (3.3)
```

with no omitted nonlinear `S`-term.

Pull (3.3) back along the retained cyclic chart.  Since
`X=x^mu` and `S=x(y+g(x))`, differentiation with respect to `y` kills both
`g(x)` and `h(x^mu)` and yields

```text
partial_y(f_mu^*G)
  =c*x/(mu*x^mu*phi'(x^mu)).                           (3.4)
```

Let `k=ord_0(phi')`.  Because `phi` is a nonconstant polynomial, `k` is a
finite nonnegative integer.  The `x`-adic order of (3.4) is

```text
1-mu-mu*k=1-mu*(k+1)<=1-mu<0.                         (3.5)
```

But `G in O(U)` pulls back to `C[x,y]`, so its `y`-derivative must lie in
`C[x,y]` and cannot have a negative `x`-adic order.  This contradiction
proves `F notin C(X)`.

Interchanging `F` and `G` changes the sign of the Jacobian but not the
argument, so `G notin C(X)` as well.

Notice that (3.4) reads off the coefficient of `y`; no Laurent term in
`g(x)` and no choice of `h(X)` can cancel it.  Thus the conclusion is valid
for the full committed Laurent deck normal form, not only for the primitive
single-pole control model.

## 4. The quartic field consequence

Keep the contradictory assumption (3.1) temporarily and put
`K=C(F,G)`.  Equation (3.3) has a nonzero coefficient of `S`, so after
adjoining `X` one recovers `S`:

```text
C(X,S)=K(X).                                           (4.1)
```

Moreover `G` is transcendental over `C(X)` and (3.3) is a linear change of
the variable `S` over `C(X)`.  Consequently

```text
[C(X,S):C(phi(X),G)]
  =[C(X,G):C(phi(X),G)]
  =[C(X):C(phi(X))]
  =deg(phi).                                           (4.2)
```

Thus the charged equality `[M:K]=4` forces `deg(phi)=4`.  This derivation of
`M=K(X)` in the alleged aligned case is elementary and does not invoke the
stronger Formanek field theorem.  In particular, it neither repairs nor
erases the campaign's recorded inability to inspect Formanek's official
primary text.

There is a coordinate-free target corollary.  Let `P in C[u,v]` be a
polynomial coordinate, and choose its polynomial mate `Q` so that
`(P,Q)` is an automorphism of `A2`.  Then

```text
(P(F,G),Q(F,G))
```

is another regular Keller pair with the same field `K` and the same quartic
degree.  Applying Sections 2--3 shows

```text
P(F,G) notin C(X)                                      (4.3)
```

for every nonconstant target coordinate `P`.  Hence no polynomial change of
target coordinates can make the pair triangular with respect to the
pseudo-plane ruling.

## 5. Sharp Laurent control

The reattachment valuation is essential.  If one deletes `Phi` and works
only in the Laurent field/ring, then for every `n>=1`

```text
F_n=X^n,
G_n=c*S/(n*mu*X^n)                                    (5.1)
```

satisfy

```text
J_(X,S)(F_n,G_n)=c/(mu X),
C(X,S)=C(F_n,G_n)(X),
[C(X,S):C(F_n,G_n)]=n.                                (5.2)
```

For `n=4`, (5.1) realizes the logarithmic equation, primitive-element
condition, and exact quartic field degree simultaneously.  Its failure is
precisely polynomiality at the retained fibre:

```text
partial_y(f_mu^*G_4)=c/(4*mu)*x^(1-4mu),              (5.3)
```

which has a pole for `mu>=2`.  This is an exact falsifier to any attempted
proof using only the abstract field `C(X,S)`, the logarithmic symplectic
form, and degree four.  The single reattachment valuation cannot be dropped.

The control also explains why the theorem is narrow.  A genuinely mixed
pair can arrange cancellations among several `S`-degrees inside `O(U)`;
equation (3.2) becomes a two-variable Poisson equation and no longer forces
the linear form (3.3).

## 6. Firewalls and next exact gate

Nothing above turns the primitive quartic discriminant into normalized
ramification.  The square monogenic-index divisor from the inverse-Kummer
control may remain nonempty, and no Orevkov--Chau increment is inferred.
Likewise, the theorem does not make the inverse Kummer divisor a second
`A1`-fibre, does not constrain its intersection with the companion divisor,
and does not use a typed canonical-class formula for arbitrary
pseudo-planes.

The surviving problem is now more sharply typed:

```text
Find or exclude F,G in O(U) such that
  J_(X,S)(F,G)=c/(mu X),
  [C(X,S):C(F,G)]=4,
  both partial_S F and partial_S G are nonzero,
  and the charged (3,1)+(2,2) boundary packet holds.   (6.1)
```

The best next moves, in order, are:

1. pass (6.1) to the associated graded ring of the retained-fibre valuation
   and classify the lowest nonzero `S`-degrees of both coordinates; the
   present theorem removes the entire zero-`S`-degree triangular branch;
2. compute the actual logarithmic ramification divisor on one fixed SNC
   completion and compare it with the saturated boundary budget, keeping it
   separate from the monogenic index divisor;
3. run the already specified bounded invariant-Hilbert-basis search, but
   quotient first by target affine/symplectic changes and require both
   `S`-derivatives to be nonzero before testing quartic degree;
4. use the two lifted target derivations on `O(U)` to test whether the
   charged boundary packet forces a second locally nilpotent derivation; only
   such a theorem would legitimately enter the known `ML_0` pseudo-plane
   exclusion route.

No replay is attached.  Equations (3.2)--(3.5), (4.2), and (5.1)--(5.3) are
symbolic identities for arbitrary `mu>=2`; finite sampling would verify less
than the displayed proof.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10671`.
- Body SHA-256:
  `a9a6567fffa872c0317d74f45b708c6272f2d16ff8f08b4c7ae14af15a4f9f9d`.
- Frozen basis: `30f89ce1b911f997758a9bf980c72ed19dca0fed`.
