# Smooth quadratic degeneracy absorption

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic_degeneracy_frontier`  
Frozen basis: `5bc4eea1c749045d54b4ee8053be8d85c4f3bc9f`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint and charged inputs

This packet absorbs the smooth degeneracies left outside the promoted
quadratic lattice theorem.  It charges the following binding integrations:

```text
c9871c92ce8748fd934dc57061f667b49952a1aba39aee43eb3af7b0aadbf392
  xmodel/bd-a2-ramification-lattice-closure-coordinator-integration-sol56-20260830.md

c8dee3199ecfaf73b6debedea625346a11babbe42082cff5bff049f8585763c2
  xmodel/bd-fix3-affine-linear-log-closure-coordinator-integration-sol56-20260830.md

ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md

f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

The new exact conclusions are:

1. a smooth class-`(2A+3B)` incidence has reduced, hence squarefree,
   infinity whenever the quadratic leading form is nonzero;
2. every coefficient basepoint on a smooth incidence produces a `-3` curve
   `E` and a residual ample different `D` meeting `E` at at least two
   physical points, so the resolved first-leg boundary has a cycle;
3. the preceding basepoint obstruction applies at infinity and, through a
   separately proved Stein-factor bridge, at an affine common coefficient
   zero; and
4. target coefficient-degree drop returns to the promoted affine-linear
   theorem, literal fibre-degree drop contradicts the generic cubic field,
   and source generic-degree one exits the proper-block hypothesis.

Consequently, conditional only on different-model review of this packet,
the promoted lattice theorem composes to the following maximum statement:

> **SMOOTH-Q2-CLOSED.**  A proper cubic intermediate block of a hypothetical
> noninvertible plane Keller map cannot admit a global trace-zero Miranda
> basis whose four coefficients have total degree at most two and whose
> exact-degree-two projective incidence hypersurface is smooth.

This is a fixed-presentation/existential-basis theorem.  It does not say that
an arbitrary cubic block has a quadratic basis, and it does not treat a
singular quadratic incidence.

## 1. Setup and two elementary perimeter reductions

Let

```text
A0=C[u,v],
B_K=A0*1 direct-sum A0*z direct-sum A0*w
```

be the normal finite-flat integral cubic algebra supplied by the promoted
proper block sandwich.  In a global trace-zero basis its Miranda cubic is

```text
Phi=bX^3-3aX^2Y+3dXY^2-cY^3.                       (1.1)
```

Assume first that `a,b,c,d` have degree at most two and at least one has
degree exactly two.  Homogenizing to target degree two gives

```text
X={Phi^h=0} subset P2 times P1,       [X]=2A+3B,     (1.2)
```

where `A,B` are the two hyperplane restrictions and `pi:X->P2` is the
incidence projection.  The theorem below assumes `X` smooth.  Smoothness and
the ample connectedness of a divisor of class `(2,3)` also force the
hypersurface to be connected and hence irreducible; retaining irreducibility
explicitly causes no harm.

Two possible degeneracies are already unavailable before boundary geometry.

**No divisorial affine coefficient-zero locus.**  If an irreducible
`h in A0` divided all four coefficients, pass to the generic DVR of `(h)`.
Modulo its uniformizer the Miranda multiplication table becomes

```text
kappa direct-sum V,       dim_kappa(V)=2,       V^2=0.              (1.3)
```

Normality makes the localized cubic order a semilocal Dedekind domain.  The
fibre (1.3) is local, so there is one prime above `(h)`.  Since the total
rank is three, the possibilities are residue degree three and ramification
index one, which gives a field fibre, or residue degree one and ramification
index three, whose radical has nonzero square.  Neither is (1.3).  Thus the
common affine zero locus has codimension two.  For quadratics it is finite;
two generic linear combinations of the coefficients have no common curve,
so Bezout bounds its scheme length by four.

**Exact fibre degree.**  Over `C(u,v)`, the algebra `B_K` is a separable
cubic field.  The binary cubic (1.1) is therefore irreducible: a linear
factor gives a product component in the generic cubic algebra.  In
particular it is nonzero and has literal projective `[X:Y]`-degree three.
An affine fibre polynomial of degree at most two would homogenize with a
constant linear factor at fibre infinity and is the same forbidden
reducibility, not a new quadratic stratum.

## 2. Smoothness forces reduced infinity

Let `S=L_infinity times P1 subset P2 times P1` and

```text
H=X intersect S=div_S(Phi_infinity),
Phi_infinity in H^0(S,O_S(2,3)).                    (2.1)
```

Suppose an integral factor `C` of bidegree `(alpha,beta)` occurs in (2.1)
with multiplicity at least two.  Along the generic smooth locus of `C`, all
derivatives of `Phi^h` tangent to `S` vanish.  The first derivative normal to
`S` is intrinsically the first normal jet

```text
j_perp(Phi^h)|C in
H^0(C, O_(P2 times P1)(2A+3B-S)|C)
 = H^0(C,O_C(A+3B)).                                (2.2)
```

With the bidegree convention used in the promoted boundary packets,

```text
A.C=beta,       B.C=alpha,
deg O_C(A+3B)=beta+3alpha>0.                         (2.3)
```

If the normal jet is identically zero, `X` is singular along a dense open
of `C`.  If it is nonzero, its pullback to the normalization of the complete
curve `C` has a zero because (2.3) is positive.  At such a zero every ambient
first derivative of `Phi^h` vanishes, so `X` is singular there.  Both cases
contradict smoothness.  Hence:

> **Lemma 2.1 (smooth squarefreeness).**  If the exact quadratic incidence
> `X` is smooth, its infinity divisor `H` is reduced and the leading
> bidegree-`(2,3)` binary cubic is squarefree.

There is an independent numerical check.  Write
`H=sum_i m_i C_i`, where `C_i` has bidegree `(alpha_i,beta_i)`.  Distinct
components have

```text
C_i.C_j=alpha_i*beta_j+alpha_j*beta_i.
```

Adjunction on the smooth surface, using `K_X=-A+B` and
`p_a(C_i)=(alpha_i-1)(beta_i-1)`, gives

```text
C_i^2=2alpha_i beta_i-3alpha_i-beta_i.               (2.4)
```

Intersecting `A=H` with `C_i`, and using
`sum m_i alpha_i=2`, `sum m_i beta_i=3`, reduces exactly to

```text
(m_i-1)(3alpha_i+beta_i)=0.                          (2.5)
```

Every nonzero component class has `3alpha_i+beta_i>0`, again forcing
`m_i=1`.  The normal-jet proof is primary because it also identifies the
precise failure in the singular stratum.

## 3. Local geometry of a smooth coefficient basepoint

Let `q in P2` be a common zero of the four homogenized coefficient sections.
Then

```text
E={q} times P1 subset X.                             (3.1)
```

Choose regular parameters `(s,t)` at `q`.  Along `E`, write the first base
jet of the incidence equation as

```text
Phi^h=s*p(X,Y)+t*r(X,Y)+terms in (s,t)^2,             (3.2)
p,r in H^0(P1,O(3)).
```

The fibre derivative of `Phi^h` vanishes identically on `E`.  Therefore
smoothness of `X` along `E` is equivalent to `p,r` having no common zero.
They cannot be proportional, since a nonzero cubic section on `P1` has a
zero.  Hence

```text
rho=[p:r]:E=P1 -> P1                                (3.3)
```

is a morphism of degree three.

### 3.1 Scheme-theoretic blowup factorization

The equality `pi^* I_q=I_E` is scheme-theoretic.  On a chart where `p` is a
unit, equation (3.2) solves

```text
s=-t*r/p+terms in t^2,
```

so `(s,t)O_X=(t)` there; on a chart where `r` is a unit it is generated by
`s`.  These charts cover `E`, proving that the pulled-back ideal is the
invertible ideal `O_X(-E)`.  The universal property gives a morphism

```text
X -> Bl_q(P2) -> P2.                                 (3.4)
```

Consequently `A-E` is the pullback of the basepoint-free pencil of lines
through `q` and is nef.  Adjunction also gives the useful check

```text
E^2=-3,
```

because `A.E=0`, `B.E=1`, and `K_X.E=1`.

### 3.2 Coefficient one and the Wronskian

The source Jacobian/different divisor of the generically finite map is

```text
R_pi=K_X-pi^*K_P2 ~ 2A+B.                            (3.5)
```

On the chart `p!=0`, use `t` and a fibre coordinate `z` as parameters on
`X`.  Substituting the first-order solution for `s` into the fibre derivative
gives, up to a unit and a harmless sign,

```text
(Phi^h_z)/t |_E = r_z-(r/p)*p_z
                  = (p*r_z-r*p_z)/p.                (3.6)
```

The Wronskian is not identically zero because the characteristic is zero and
`rho` has degree three.  Thus `E` occurs in `R_pi` with Cartier coefficient
exactly one.  Write

```text
R_pi=E+D,       D effective,       D~2A+B-E.          (3.7)
```

The transition-compatible zero divisor in (3.6) is precisely
`Ram(rho)`.  Therefore

```text
D|E=Ram(rho),       D.E=4.                           (3.8)
```

Riemann--Hurwitz gives total ramification four.  At one point of a degree-
three characteristic-zero map the contribution is at most `3-1=2`, so the
support of (3.8) contains at least two distinct physical points.

### 3.3 Ample residual different and the cycle

Using the blowup factorization,

```text
D=(A+B)+(A-E).                                       (3.9)
```

The first summand is the restriction of the ample ambient bundle `O(1,1)`;
the second is nef.  Hence `D` is ample.  Its reduced support is connected by
the same Hodge-index argument used in the promoted lattice integration.

In a resolved first-leg boundary, if the connected total transform of
`Supp(D)` already has positive genus or a graph cycle, the rational-forest
theorem has fired.  Otherwise it is a tree.  The curve `E` is rational and
meets it at the at least two distinct physical points from (3.8).  Resolving
tangencies only subdivides the two joining paths.  Contracting the two trees
leaves two parallel edges, hence a cycle.  We obtain:

> **Lemma 3.1 (smooth basepoint cycle).**  Whenever a coefficient-basepoint
> curve `E` belongs to the boundary of the lifted first-leg open on a smooth
> exact quadratic incidence, the full resolved boundary is not a rational
> forest.

For a projective coefficient basepoint `q in L_infinity`, `E` is already a
component of `H`.  Lemma 3.1 therefore eliminates the nonfinite `F3,F6`
types rather than merely declaring them outside projective finiteness.

## 4. Affine common-zero bridge

An affine common coefficient zero needs one additional typing step because
the block surface `Y=Spec(B_K)` is finite over `A2`, whereas the incidence
surface contains the exceptional `P1`.  The bridge is exact in the present
normal finite-flat scope.

Let `Z subset A2` be the finite common-zero scheme from Section 1 and put

```text
X_aff={Phi=0} subset A2 times P1,
pi_0:X_aff->A2.
```

The divisor sequence on the relative projective line is

```text
0 -> O(-3) --Phi--> O -> O_(X_aff) -> 0.             (4.1)
```

Relative cohomology gives an exact sequence of `A0`-modules

```text
0 -> A0 -> (pi_0)_*O_(X_aff) -> A0^2 -> 0,           (4.2)
```

so the direct image is locally free of rank three.  Over `A2 minus Z`, the
incidence is a finite cubic divisor and the standard Miranda multiplication
identifies its direct-image algebra with `B_K`.  Both algebras are locally
free, hence reflexive, over the regular surface `A2`; the isomorphism and its
inverse extend uniquely across the codimension-two set `Z`.  Multiplication
matrices extend entrywise, and their algebra identities hold globally because
they hold on the dense open.  Thus this is an algebra isomorphism, not merely
a module isomorphism, and

```text
Spec((pi_0)_*O_(X_aff)) = Spec(B_K)=Y.                (4.3)
```

The associated Stein morphism

```text
nu:X_aff -> Y                                        (4.4)
```

is an isomorphism over `A2 minus Z` and contracts the curve
`E_q={q} times P1` over each `q in Z`.  At such a point the direct Miranda
multiplication table in `B_K tensor kappa(q)` is the square-zero algebra
(1.3), so it is non-etale.  This conclusion is not obtained by base-changing
`H^0(O_(X_aff))`: formation of global functions does not commute with that
exceptional fibre.
The promoted block
structure gives

```text
g_1(A2) subset Y_sm minus R,
```

and in particular the first-leg image misses every contracted point.  It
therefore lifts through the isomorphism locus of (4.4) to a dominant morphism
whose image avoids `E_q` and the remaining source different.  In a smooth
projective incidence completion, `E_q union Supp(D)` is consequently a
boundary subconfiguration: a component of `D` in infinity is already in
`H`, and every other component is the closure of affine non-etale support.
Lemma 3.1 applies.

> **Corollary 4.1.**  In the normal finite-flat proper cubic-block scope, a
> smooth exact quadratic projective incidence cannot have an affine common
> zero of the four Miranda coefficients.

This is not a claim about an arbitrary four-tuple of quadratic polynomials.
It uses normality of `B_K`, the Miranda algebra identification in (4.3), the
promoted fact that the first leg misses the non-etale locus, and smoothness
of the incidence model along every exceptional curve.

## 5. Exact degree-drop routing

The adjacent degree drops do not create further smooth quadratic cases.

1. **Target coefficient degree.**  If all four degree-two leading forms
   vanish, the affine coefficients have degree at most one.  Homogenizing
   artificially to degree two merely adds the target-infinity ambient
   component; cancel it and apply the promoted affine-linear theorem
   `AL3-CLOSED` charged in Section 0.
2. **Fibre degree.**  A literal drop below homogeneous `[X:Y]`-degree three
   supplies a constant fibre linear factor after degree-three homogenization.
   This contradicts the generic cubic field, as in Section 1.  Vanishing of
   only one leading fibre coefficient is not by itself a target-degree drop;
   the point is the generic factor, not a chart convention.
3. **Source generic degree.**  If “source-degree drop” means
   `[C(x,y):K]=1`, then `K` is not a proper upper intermediate field and the
   promoted sandwich hypothesis has failed.  No polynomial-support theorem
   is inferred from that tautological routing.
4. **Quotient generic degree.**  A drop of the cubic quotient to degree two
   is already excluded by the promoted non-Galois theorem, since every
   separable quadratic extension is Galois; degree one is not a proper lower
   intermediate field.

These are four different typings.  None authorizes replacing a singular
degree-two presentation by a smooth lower-degree one.

## 6. Conditional composition: all smooth exact quadratics

Assume a proper cubic block has coefficients of degree at most two in the
chosen global trace-zero basis and that its exact-degree-two projective
incidence `X` is smooth.

If the coefficient degree drops, Section 5 routes to `AL3-CLOSED`.  Otherwise
the generic fibre has exact degree three.  If the four homogenized
coefficient sections have a common zero, Lemma 3.1 applies directly at
projective infinity and Corollary 4.1 applies at an affine point.  Thus a
survivor has no coefficient basepoint anywhere on `P2`.

Every fibre of the proper morphism `pi:X->P2` is then the nonzero cubic
divisor in `P1`, hence zero-dimensional of length three.  Proper plus
quasi-finite makes `pi` finite.  With `Z` empty, (4.3) identifies
`X minus H` literally with the finite block surface `Y`, so the promoted
first-leg and unit inputs are on the required model.  Lemma 2.1 makes its
infinity divisor reduced and squarefree.  All hypotheses of the promoted
lattice integration `c9871c92...` are now met.  That theorem excludes the full
`F1,F2,F4,F5,F7` list, projective finiteness has already removed the vertical
basepoint types, and `F8,F9` have no rational-tree refinement.  This proves
`SMOOTH-Q2-CLOSED`, conditional on different-model review of the new lemmas
and bridge in this packet.

Notice that affine common zeros are not silently fed into the old lattice
theorem: they are eliminated first by Section 4.  Likewise nonreduced
infinity is not silently squarefreed: Lemma 2.1 proves it cannot occur on a
smooth `X`.

## 7. Hostile attacks and controls

The following shortcuts were attacked explicitly.

* **A repeated boundary factor might coexist with smooth total space.**
  Locally this can happen while the normal derivative is a unit, but globally
  that derivative has degree `3alpha+beta>0` on the complete component and
  must vanish.  Equation (2.5) is an independent intersection check.
* **The basepoint fibre might be only set-theoretic.**  Section 3.1 proves
  `(s,t)O_X=I_E` chartwise before invoking the blowup universal property.
* **The pencil `[p:r]` might have degree below three.**  Basepoint-freeness
  gives pullback `O(1)=O_E(3)`; proportional cubics would have common zeros.
* **`E` might have larger Cartier coefficient in the different.**  The
  nonzero Wronskian in (3.6) gives generic order exactly one.
* **Four intersection units might concentrate at one physical point.**  A
  degree-three map has local ramification contribution at most two, so the
  degree-four ramification divisor has at least two support points.
* **The residual different might be merely big.**  Formula (3.9) writes it
  as ample plus nef, so it is ample and its support is connected.
* **Resolution might erase the cycle.**  Blowups subdivide joining paths or
  add pendant vertices; they do not identify the two physical attachments.
* **The affine incidence is not finite at a common zero.**  Correct; Section
  4 uses its Stein algebra, proves that algebra is `B_K`, and only lifts the
  first leg through the isomorphism locus after showing the contracted point
  is non-etale and missed.  The square-zero fibre is read from the Miranda
  multiplication table, not from an invalid cohomology base-change step.
* **No projective basepoint might be weaker than finiteness.**  Every fibre
  is then a nonzero effective cubic divisor on `P1`; proper quasi-finiteness
  is finiteness.
* **A better basis might change the degree.**  The conclusion is existential
  in the displayed basis.  It neither minimizes coefficient degree nor
  transfers smoothness between two bases.

No CAS, finite-field sampling, or AWS computation enters any step.

## 8. Scope firewall and successor

`SMOOTH-Q2-CLOSED` is conditional on a proper cubic block, the promoted
dominant first-leg sandwich, a chosen global trace-zero basis with coefficient
degree at most two, and smoothness of the exact quadratic projective
incidence.  It does not prove that a quadratic basis exists, bound the minimum
degree over all bases, or turn the intrinsic discriminant bound around.  It
does not cover a singular or nonnormal incidence closure, a higher-degree
presentation, another block degree, a primitive extension, a polynomial map,
a counterexample, or JC2.

The next geometric packet should be singular-incidence-only.  A promising
separate provisional triage is: for a normal class-`(2,3)` hypersurface,
`H^1(O_X)=H^2(O_X)=0`; after proving that the first-leg open lifts to a
resolution completion with all singular points in the boundary, Leray would
turn `q=0` into rationality of every singularity, and the hypersurface
Gorenstein condition would reduce these to Du Val types.  That bridge and
the resulting exceptional-root lattice are not consumed here.  Nonnormal
closures and basis minimization remain still later, separate clients.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19665`.
- Body SHA-256:
  `ecff0c0f3b373e00128b10cad561a0738e8db32e60d4c04f475c5e0fa38c25bd`.
- Frozen basis: `5bc4eea1c749045d54b4ee8053be8d85c4f3bc9f`.
