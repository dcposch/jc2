# Delayed affine-Faber `A`: the `H=15` arcwise Gate-A bridge

Date: 2026-08-26

Status: **PROVISIONAL THEOREM.  THE ELEMENTARY FIRST-BLOCK INPUT IS
FROZEN BUT A DIFFERENT-MODEL REVIEW IS STILL LIVE; NO SOURCE-FAN PROMOTION
BEFORE REVIEW OF THIS COMPOSITION.**

## 1. Exact statement

Let `R` be a complete characteristic-zero DVR with uniformizer `sigma`,
after a finite ramification if necessary.  Consider a literal solution of
the seven `(8,12)` order-two source rows on the fixed delayed-load ray

```text
Lambda=sigma^3,
k10=Lambda^12*K10,  k6=Lambda^8*K6,  k2=Lambda^4*K2,
K10 a unit.
```

Perform the exact monic square division of the centered octic `C(z)`,

```text
C=Q^2+Delta,       deg(Delta)<=3,
Q=z^4+q2*z^2+q1*z+q0.                              (1.1)
```

Suppose

```text
ord_sigma(Delta)=15,
Q mod sigma=z^2*(z^2+p),       p a unit,             (1.2)
```

and suppose the induced moving-`A` coefficient coordinate defined in
(4.1) below has `ord_sigma(a)>=5`.  Then no such source arc exists.

The conclusion is arcwise and only for this registered Newton cell.  It is
not a scheme-level total-Rees atlas or a statement about another normal or
load slope.

## 2. Exact two-sided square division

Write

```text
C=z^8+C6*z^6+C5*z^5+C4*z^4+C3*z^3+C2*z^2+C1*z+C0.
```

Over `R[1/2]`, (1.1) is the polynomial coordinate isomorphism

```text
q2=C6/2,
q1=C5/2,
q0=(C4-q2^2)/2,

Delta3=C3-2*q2*q1,
Delta2=C2-q1^2-2*q2*q0,
Delta1=C1-2*q1*q0,
Delta0=C0-q0^2.                                   (2.1)
```

Its inverse is obtained by expanding `Q^2` and adding the four `Delta_i`.
Thus it is literal in both directions and has no blowup, symmetric-algebra,
or torsion ambiguity.  Under (1.2), write

```text
Delta=sigma^15*N(sigma,z),       N0=N mod sigma !=0. (2.2)
```

## 3. The raw grade-30 predecessor forces the repeated-`A` kernel

At fixed `z`, the unloaded term is

```text
(Q^2+Delta)^(3/2)
 =Q^3+(3/2)*Q*Delta+(3/8)*Delta^2/Q
   -(1/16)*Delta^3/Q^3+... .                       (3.1)
```

The first two summands are polynomials.  The first possible negative
coefficient is therefore, at sigma grade 30,

```text
(3/8)*[N0^2/Q0]_-,       Q0=z^2*(z^2+p).           (3.2)
```

Every delayed load and the first target `mu2` starts at sigma grade 42;
the cubic normal starts at grade 45.  Moving coefficients of `Q` and `N`
raise (3.2), so none ties grade 30.  Since there is no earlier negative
predecessor, the lower-unitriangular Laurent-to-ordinary connection makes
the vanishing of the first four ordinary source rows at grade 30
equivalent to the vanishing of the first four negative Laurent
coefficients of `N0^2/Q0`.

The frozen elementary bridge is

```text
56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-theorem-20260826.md
```

and gives

```text
Q0 divides N0^2.                                    (3.3)
```

Here `Q0=A0^2*D0` with `A0=z`, `D0=z^2+p`.  On `D(p)`, `A0` is coprime to
`D0` and `D0` is squarefree.  Since `deg(N0)<=3`, (3.3) is equivalent to

```text
N0=m*z*(z^2+p),              m !=0.                (3.4)
```

The nonzero scalar follows from the definition of grade 15 in (2.2).
Thus the raw first source block does not merely resemble the affine
repeated-root normal: it forces its exact central kernel.

## 4. Literal entry into the reviewed affine coefficient chart

Let `N=n3*z^3+n2*z^2+n1*z+n0` in (2.2).  Since `n3 mod sigma=m` is a
unit, define on `D(n3)`

```text
M  =n3,
a  =n2/M,
E  =q2+6*a^2,
U  =q1-2*a*(4*a^2-E),
R0 =q0-a^2*(E-3*a^2)+a*U,
V  =n1-(E-5*a^2)*M,
W0 =n0+a*(E-3*a^2)*M+a*V-M*U/2.                  (4.1)
```

These are the exact inverse coordinates of

```text
A=z-a,       D=A^2+4*a*A+E,
Q=A^2*D+U*A+R0,
N=M*A*D+V*A+M*U/2+W0.                            (4.2)
```

No moving root of the full quartic has been adjoined: (4.1) is a regular
coefficient-ring map on `D(M)`.  Formulae (1.2) and (3.4) give at the
closed point

```text
(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0).               (4.3)
```

Therefore

```text
q=min(ord_sigma(U),ord_sigma(V))>0                (4.4)
```

with `q=infinity` allowed.  This is a consequence of the central ideal,
not an omitted assumption.  By contrast, `ord_sigma(a)>=5` is the named
moving-center Newton-cell hypothesis in Section 1; it does not follow from
first-block divisibility alone.  Cells with `0<ord_sigma(a)<5` must be
routed to their earlier center faces.

Factoring the known `sigma^15` in (2.2) supplies the normal scale of the
promoted affine theorem; a residual unit may be placed in `lambda` or
absorbed into `M`.  Equations (4.1)--(4.2) retain arbitrary later center,
tangent, kernel, and complementary jets.  The reviewed complement pivot is
therefore available without a further Rees presentation.

## 5. Composition with the promoted direct-unit theorem

The charged theorem, review, and promotion are

```text
fef0524a91c239b9086df8377e0b1270430b2fb164915eb8286bf52f9508cf32
  xmodel/max12-812-order2-affine-faber-a-delayed-load-valuative-composition-theorem-20260826.md
a6d434b5342a32bcefc74b78fd4526eaf1a6556a73ddcc22b970c9958d248f18
  xmodel/max12-812-order2-affine-faber-a-delayed-load-valuative-composition-hostile-review-grok-20260826.md
0c4d242775572faef3578c42721c9d6cad483c3073dd9b98cffec5119783291c
  xmodel/max12-812-order2-affine-faber-a-delayed-load-valuative-composition-promotion-20260826.md
```

By (4.3)--(4.4), the literal arc lies in the weighted repeated-`A` formal
neighbourhood on `D(p*m*K10)` with positive rational kernel order.  The
assumed center bound is exactly the remaining chart weight.  The promoted
theorem kills every `0<q<6` by the complete grade-`30+2q` predecessor and
every `q>=6`, including `q=infinity`, by

```text
[sigma^45](E*H3+H5)=-E*lambda^3*M^3/16,
```

a unit.  This contradicts the seven literal source rows and proves the
statement of Section 1, conditional only on confirmation of the frozen
elementary bridge and of this source composition.

## 6. Exhaustive routing at the boundary of the claim

The first-block argument gives the following fail-closed split.

| Boundary | Route |
|---|---|
| `Q0` squarefree | Divisibility forces `N0=0`, contradicting the declared first normal; reset the normal order. |
| `Q0=A0^2*D0` with `gcd(A0,D0)=1`, `D0` squarefree, `m!=0` | The present repeated-`A` coefficient chart; excluded only at `H=15`, `ord(a)>=5`, and on `D(p*m*K10)`. |
| `Q0` a square, or `D0` nonsquarefree / not coprime to `A0` | Separate square/Pell, triple-root, quadruple-root, collision, `p=0`, or `D=0` receiver. |
| `m=0` | The proposed coefficient was not the first nonzero normal; raise `H`. |
| `H<21`, `H!=15` | First-block factor routing remains valid, but the promoted weight-15 theorem does not apply. |
| `H>=21` | Loads/`mu2` can tie or precede the quadratic block; retain forcing and recompute the predecessor ideal. |
| `q=0` or `0<ord(a)<5` | Earlier special-fibre or moving-center receiver, outside the weighted formal neighbourhood. |
| `K10=0`, `p=0`, or another load slope | Separate zero-load, collision, or relative-load Newton fan. |

## 7. Firewall

This proof uses exact coefficient isomorphisms on a single DVR and hence
does not need a monolithic total-Rees algebra for this one cell.  It does
not prove flatness or torsion statements for a global blowup, cover all
arcs of the original source boundary, identify pairwise chart overlaps,
or commute saturation with specialization.  It does not close any routed
boundary in Section 6, terminal/Taylor, order two, `(8,12)`, maximum
twelve, or JC2.
