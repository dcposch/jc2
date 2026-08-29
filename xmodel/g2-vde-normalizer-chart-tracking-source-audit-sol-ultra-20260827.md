# G2: van den Essen normalizer and boundary-chart tracking

**Date:** 2026-08-27  
**Lane:** Sol Ultra, primary-source / exact desk audit  
**Target:** van den Essen Corollary 10.2.21 as consumed by VGG
Proposition 4.7, Proposition 5.20, and Corollary 5.21  
**Computation:** none; no CAS and no AWS

## 0. Verdict

There is a clean no-go, but it comes from a stronger and narrower place than
the earlier cylinder-automorphism argument.

1. **Van den Essen Corollary 10.2.21 is not chart-rigid in its general
   statement or proof.**  Its degree-decreasing induction uses the full tame
   plane automorphism group `T(k,2)`: affine maps and triangular polynomial
   shears.  Such maps need not act on either Laurent cylinder
   `K[x^{+-1},y]` or `K[y^{+-1},x]`.  The classification of automorphisms of
   one Laurent cylinder therefore does not classify this normalizer.

2. **The VGG minimal-pair client collapses that freedom.**  The proof of VGG
   Proposition 4.7, lines 1816--1884 of the pinned arXiv TeX, does more than
   prove preservation of the two total degrees.  If `psi=phi^{-1}` and
   `M=deg psi(x)`, `N=deg psi(y)`, its divisibility/minimality argument rules
   out every case with `max(M,N)>1`.  Hence the *final composite* normalizer
   used there is affine.  Intermediate tame factors may be nonlinear; the
   composite is not.

3. **Between two oriented VGG-selected rectangle representatives, even an
   affine swap is impossible.**  Their highest total homogeneous forms are

   ```text
   c x^a y^b,       c' x^(a') y^(b'),       1 <= a < b,  1 <= a' < b'.
   ```

   Unique factorization applied to the linear part of the affine transition
   says it is either diagonal or anti-diagonal.  Anti-diagonal would exchange
   the unequal exponents and give `(a',b')=(b,a)`, contrary to `a'<b'`.
   Thus the transition is diagonal affine.  VGG Proposition 5.20 then adds
   only `y -> y+lambda`, which is the identity on the line at infinity.

4. **Consequently the VGG re-selection pipeline preserves the two physical
   infinity charts separately.**  On the normalized generic fibre it gives a
   bijection of boundary places over `x=infinity` with boundary places over
   `x=infinity`, and likewise for `y=infinity`.  It cannot move the missing
   fixed-pair `y=infinity` places into the native `x=infinity` chart of a
   second standard representative.  The proposed second-run route does not
   close `G2-PSC(4.0)`.

5. **This is a no-go only at the exact VGG perimeter.**  It applies to two
   globally minimal, subrectangular, strictly oriented representatives in
   the same source-automorphism orbit.  An arbitrary polynomial
   automorphism of an arbitrary nonminimal representative can scramble
   charts.  To use such a map one must exhibit it and track every place by
   the valuation pair of its inverse coordinate polynomials.  Corollary
   10.2.21 supplies no uniform coverage theorem of that kind.

The narrow conclusion is therefore:

```text
VGG minimal re-selection cannot expose the missing physical chart.
Use the intrinsic exact-pair two-chart constructor for coverage.
```

This does not validate the still-open Sigray decoration, landing, delay, or
degree steps, and it proves no contradiction or JC2 result.

## 1. Source custody and exact scope

### 1.1 VGG primary source

Freshly fetched `https://arxiv.org/e-print/1401.1784`:

```text
e-print gzip  e6a01769d1f017467c2cba2b1e425ed708da9b4ac917391399fb34f5ac0d86f0
TeX            b4908fd596d555c745b3bdce9613e64c056052d7237efc1419d9c24c0e6004d5
```

Exact source spans in that TeX:

| item | lines | fact used here |
|---|---:|---|
| Definition 4.3 | 1524--1533 | `(m,n)`-pair and strict standard orientation |
| Proposition 4.7 | 1665--1887 | subrectangle normalizer and its hidden affine conclusion |
| vdE invocation | 1674--1678 | Corollary 10.2.21 supplies the initial subrectangle |
| controlled post-fixes | 1682--1781 | signed flip conjugation and a translation |
| strict order | 1783--1789 | the resulting corner satisfies `a<b` |
| inverse-degree argument | 1816--1884 | `M|N` or `N|M`; nonlinear cases contradicted by minimality |
| Proposition 5.20 | 2997--3056 | final standardizer is identity or `x->x`, `y->y+lambda` |
| Corollary 5.21 | 3058--3086 | existence of the selected minimal standard pair |

The item numbered 5.21 is a **corollary**, not a proposition.

### 1.2 van den Essen primary source

Primary bibliographic pin:

```text
Arno van den Essen, Polynomial Automorphisms and the Jacobian Conjecture,
Progress in Mathematics 190, Birkhaeuser, 2000,
Chapter 10, pp. 239--273.
DOI: https://doi.org/10.1007/978-3-0348-8440-2_10
```

The Springer chapter is subscription-gated in this environment.  I checked
the exact statement and exposed proof spine against the publisher-authorized
Google Books scan, volume ID `wKJqqd8t8KUC`, pp. 251--254.  The scan gives:

- Theorem 10.2.18: a negative-slope Newton edge permits a tame
  `phi in T(k,2)` with strictly smaller
  `delta(P)=deg_x(P)+deg_y(P)`.
- Corollary 10.2.21: induction on `delta(P)` ends either with a coordinate or
  with no negative-slope edge; in the latter case the support lies in an
  axis rectangle with an occupied northeast corner, oriented `1<=a<=b`
  after interchanging the variables if needed.
- The displayed proof of the reduction theorem explicitly uses a triangular
  shear in one case, obtains the symmetric case by interchanging `X,Y`, and
  leaves its remaining case as Exercise 2.  Thus neither the statement nor
  the proof promises a cylinder-preserving word.
- Corollary 5.1.6(a), p. 88, gives the coordinate-degree divisibility and
  leading-power relation used verbatim by VGG at TeX line 1817.

Session response hashes for the exact Google Books `SearchWithinVolume2`
records (query strings respectively `Corollary 10.2.21`, `proof Corollary
10.2.21`, `Abhyankar reduction theorem`, `Case iii follows from case i`,
`T(k,2) subgroup generated`, and `Corollary 5.1.6(a)`):

```text
bcf52c39976eec154d273a4bf549721e9e67ca089d7dbc46a5ad684aab1c669b
57cbb5b05cf0ad620c572ef47e3b82b0aa15775e3f2d786af57cb4be4c4097b8
8b8d00934c83a33ce3dae716cbf08b1c8b5be21578b9c48e425f15b96069b202
2220520de447c23f2b720a5735c092e38fa18d00c6e8515dd4de8f4367b17719
23425c4dd44909d4df47e3a3668a6fc05fc0c72dcbb2055671b5a291a35c869a
6a75288b6cdda1628a156933e60173bea07649e42224b61b01431a274dc2ff2c
```

I do not use any unexposed detail of the book proof below.  The decisive
chart theorem is re-derived from the complete VGG source.

## 2. Why the Laurent-cylinder classification does not settle vdE

Let

```text
A_x = K[x^{+-1},y].
```

Its automorphisms must send the unit `x` to a Laurent monomial unit.  In
contrast, the elementary polynomial automorphism

```text
x -> x+y^2,       y -> y
```

is in `Aut K[x,y]` but does not induce an automorphism of `A_x`, since
`x+y^2` is not a unit there.  This one example already proves that the
Laurent-cylinder classification is strictly smaller than the Jung--van der
Kulk/tame group consumed by van den Essen.

At the level of a boundary valuation `nu`, a nonlinear shear can change

```text
(nu(x),nu(y))  to  (nu(x+p(y)),nu(y)),
```

including by cancellation of leading terms.  Therefore Corollary 10.2.21
alone supplies neither a preserved chart nor a chosen relocation of one.
Its conclusion concerns the Newton polygon of the transformed polynomial,
not the identity of old boundary places.

The earlier cylinder no-go remains correct for maps inside that cylinder,
but it cannot be promoted to a statement about every polynomial
normalizer.  The promotion below instead uses global minimality.

## 3. The hidden affine conclusion in VGG Proposition 4.7

Here is the argument in a form that also makes its hypotheses explicit.

Let `(P,Q)` be a globally minimal counterexample, so

```text
B = gcd(deg P, deg Q).
```

Let `theta in Aut K[x,y]` take it to a subrectangular minimal pair
`(P',Q')=(theta(P),theta(Q))` having

```text
(P')^+ = c_P x^(m abar) y^(m bbar),
(Q')^+ = c_Q x^(n abar) y^(n bbar),
```

where `m,n>1` are coprime and `abar,bbar>0`.  This is exactly the data VGG
extracts in Proposition 4.7.  Put `psi=theta^{-1}` and

```text
M=deg psi(x),       N=deg psi(y).
```

For a plane polynomial automorphism, either `M|N` or `N|M`.  Suppose
`N=kM`.  The leading forms then have

```text
ell(psi(y)) = lambda ell(psi(x))^k.
```

The unique northeast monomials of `P',Q'` prevent cancellation on
substitution, giving exactly

```text
deg P = m M(abar+k bbar),
deg Q = n M(abar+k bbar).
```

Since both the source and target are globally minimal,

```text
B = M(abar+k bbar) = abar+bbar.
```

Positivity forces `M=1` and `k=1`, hence `M=N=1`.  The case `M=kN` is
symmetric.  Thus `psi`, and therefore `theta`, is affine.

This is the substance of VGG TeX lines 1816--1884.  In the paper it is
presented as the proof that the chosen normalizer preserves the two total
degrees.  The stronger intermediate conclusion `deg psi(x)=deg psi(y)=1`
is what supplies chart control.

Two scope points matter:

- Minimality of both representatives is load-bearing.  Without it the two
  displayed gcds need not agree.
- No assertion is made that the individual factors in van den Essen's tame
  reduction word are affine.  Only their final composite in this client is.

## 4. Oriented minimal re-selection is chart-rigid

> **Theorem VCR (VGG chart rigidity).**  Let `K` have characteristic zero.
> Let `(P_0,Q_0)` and `(P_1,Q_1)=theta(P_0,Q_0)` be two globally minimal
> VGG-selected subrectangular representatives in the same polynomial-source
> automorphism orbit, with the same component orientation.  Assume
>
> ```text
> (P_0)^+ = c_0 x^a y^b,       1<=a<b,
> (P_1)^+ = c_1 x^(a') y^(b'), 1<=a'<b'.
> ```
>
> Then
>
> ```text
> theta(x)=alpha x+r,     theta(y)=beta y+s
> ```
>
> for `alpha,beta in K^*` and `r,s in K`.  In particular `theta` extends to
> a projective automorphism fixing separately
> `p_x=[1:0:0]` and `p_y=[0:1:0]`.

**Proof.**  Section 3 makes `theta` affine.  Write the two nonconstant
linear parts as `L_x,L_y`.  Taking the highest homogeneous part gives

```text
c_0 L_x^a L_y^b = c_1 x^(a') y^(b').
```

The linear forms `L_x,L_y` are independent.  Unique factorization says
that, up to nonzero scalars, they are either `(x,y)` or `(y,x)`.  The second
case gives `(a',b')=(b,a)`, contradicting both strict inequalities.  Hence
they are `(x,y)`.  Constants are unrestricted and disappear on the line at
infinity.  QED.

The strict inequality is not an extra campaign hypothesis: VGG derives
`a<b` at TeX lines 1783--1789.  Proposition 5.20 preserves the highest
homogeneous forms and uses only the translation `y->y+lambda`; it therefore
preserves Theorem VCR's conclusion.  Corollary 5.21 invokes exactly
Propositions 4.7 and 5.20.

An equivalent one-line proof at infinity is useful.  The divisor of
`P_i^+` on the line at infinity is supported at `p_x,p_y` with unequal
multiplicities.  A chart swap exchanges those multiplicities, while the VGG
orientation orders them.  Therefore an oriented re-selection cannot swap
the two points.

## 5. Boundary-place action and preserved object identity

Fix a fibre value `t`.  Let

```text
C_t  : P_0=t,       C'_t : theta(P_0)=t.
```

The geometric source automorphism corresponding contravariantly to `theta`
restricts to an isomorphism `C'_t -> C_t` and therefore to an isomorphism of
their normalizations.  If `S` is a boundary place of `C_t` and `S'` its
corresponding place of `C'_t`, then for every rational function `h`,

```text
nu_(S')(theta(h)) = nu_S(h),
```

or equivalently

```text
nu_(S')(x) = nu_S(theta^{-1}(x)),
nu_(S')(y) = nu_S(theta^{-1}(y)).
```

Under Theorem VCR,

```text
theta^{-1}(x)=alpha^{-1}(x-r),
theta^{-1}(y)=beta^{-1}(y-s).
```

Adding a constant does not change a pole.  Hence

```text
nu_(S')(x)<0  iff  nu_S(x)<0,
nu_(S')(y)<0  iff  nu_S(y)<0.
```

Thus the exact place sets over the two physical points at infinity are
preserved separately.  The isomorphism also preserves the values of the
transformed component functions: a pole/finite tag for `Q_0`, local degree,
ramification index, and deck orbit are transported to the corresponding
tag/data for `theta(Q_0)`.  What is *not* automatically identified is a
particular GGV chain witness or a Sigray approximate-root decoration; those
remain structures to be transported or reconstructed.

## 6. Cheapest exact discriminator and general fallback interface

### 6.1 VGG pipeline: a two-factor test

For a claimed second VGG run, inspect only the two highest homogeneous
forms.  A relocation of old `p_y` places into the new native `p_x` chart
requires an anti-diagonal linear part.  But

```text
x^a y^b -> x^(a') y^(b'),       a<b and a'<b'
```

forces the linear part to be diagonal by unique factorization.  This is an
exact, coefficient-free discriminator; no prototype, branch expansion, or
CAS is needed.

In implementation terms, reject a claimed re-selection bridge unless it
supplies the transition automorphism and passes both checks:

```text
degree(theta^{-1}(x)) = degree(theta^{-1}(y)) = 1,
linear_part(theta) is anti-diagonal.
```

The first is forced by minimality; the second is required for chart swap;
the ordered top form forces its negation.  The claim therefore fails before
any GGV chain comparison.

### 6.2 Any route outside the VGG perimeter

For an arbitrary polynomial automorphism `gamma`, the correct chart-tracking
interface is the following finite statement on the normalized exact fibre:

```text
S |--> (nu_S(gamma^{-1}(x)), nu_S(gamma^{-1}(y))).
```

A target old `y=infinity` place lands in the new native `x=infinity` chart
exactly when

```text
nu_S(gamma^{-1}(x))<0 <= nu_S(gamma^{-1}(y)).
```

Coverage requires this for every target place, together with a proof that
the re-selected pair satisfies the printed GGV hypotheses.  A
Jung--van der Kulk word makes the valuation update executable one triangular
factor at a time, but it does not make the desired inequalities automatic.
This is the narrowest honest interface if a future route deliberately leaves
global minimality or the VGG rectangle orientation.

## 7. Implications for G2

### 7.1 `G2-PSC`

The re-selection proposal cannot pay clause (4.0).  Starting from the fixed
GGV-selected minimal pair, every second representative supplied by the same
minimal standardization perimeter sees the same native-chart place set.
The missing `y=infinity` places stay missing from that run.

This is stronger than saying that a four-map menu or one Laurent cylinder
failed.  It closes the entire oriented, globally minimal VGG re-selection
class, including any hidden nonlinear tame word whose final output is again
a minimal oriented rectangle.

It does **not** close arbitrary nonminimal detours.  Those detours owe the
valuation interface of Section 6.2 and provide no evident advantage over
constructing the two-chart tree directly.

### 7.2 Pure Sigray / exact-pair route

The no-go favors the pure exact-pair constructor for *coverage*: normalize
the actual fibre and enumerate its DVRs in both physical charts.  That route
names every place without changing the pair, so no re-selection gluing is
needed.

Nothing here repairs the separate Sigray debts: existence and typing of all
approximate-root decorations, `Q/jump/max` data, finite-leading-part scope,
landing, bounded delay, or a degree ceiling.  The theorem removes one
possible coverage shortcut; it does not promote those later steps.

### 7.3 Scope of Theorem S

I checked only the scope needed here.  The transpose-subsumption Theorem S
in the predecessor Opus5 report compares VGG Section 7 face statements for
`(P,Q)` and its signed-transposed presentation.  It is a statement about
directions, leading forms, and certified arcs under coordinate conjugation.
It neither constrains van den Essen's selected `phi` nor identifies boundary
places after a fresh polynomial automorphism.  Therefore it cannot answer
re-selection, and no step of Theorem VCR assumes it.  The conclusions are
consistent: Theorem S kills the claimed new face information, while Theorem
VCR independently kills the claimed physical-chart relocation.

## 8. Final theorem/interface slate

| item | verdict |
|---|---|
| vdE 10.2.21 uses only cylinder automorphisms | **REFUTED**; it uses `T(k,2)` |
| general vdE normalizer has a chart-preserving normal form | **NOT IN THE SOURCE** |
| VGG Prop. 4.7 final normalizer on a minimal pair is affine | **PROVED from its published proof** |
| two oriented minimal rectangle representatives can be swapped at infinity | **REFUTED by Theorem VCR** |
| VGG Prop. 5.20 can change the chart partition | **REFUTED**; it is a translation |
| VGG Cor. 5.21 supplies a second physical chart after re-selection | **REFUTED at the same-orbit minimal perimeter** |
| arbitrary nonminimal automorphism route | **OPEN but owes explicit place valuations** |
| pure exact-pair two-chart coverage | **UNAFFECTED and now the preferred coverage source** |

## 9. Custody and firewall

The only repository file written by this lane is this report.  No canonical
ledger was edited.  No AWS host or heavy algebra process was used.  The
separate user-owned formalization tree was not entered, read, searched,
statused, built, or modified.
