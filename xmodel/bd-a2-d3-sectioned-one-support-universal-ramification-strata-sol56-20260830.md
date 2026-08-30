# D3 sectioned one-support row: universal ramification strata and the 27+28 gate

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent family-audit lane  
Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`  
Lifecycle: **EXACT PROVISIONAL REDUCTION / ROW OPEN / REVIEW REQUIRED**

## 0. Maximum-safe verdict

Consider a normal finite-flat class-`(3,3)` incidence

```text
X={G=0} subset P2_p x P1_[S:T],
pi:X -> P2_p,                         deg(pi)=3,         (0.1)
```

in the sectioned one-support Hodge row

```text
m=1,             T_GR=2t_0,          D=-2F_(t_0),
exact local CFS level 2.                                  (0.2)
```

Assume additionally that the restriction over the fixed affine target plane
is the second leg of an actual proper cubic block.  The remaining row is not
eliminated here, but its ramification is forced into a substantially thinner
and finite algebraic locus than the previously exhibited genus-two control
suggested.

1. Write the four target cubic coefficients of `G` as a basepoint-free
   coefficient morphism

   ```text
   phi:P2 -> P3=Sym^3(P1).                              (0.3)
   ```

   The binary-cubic discriminant surface has normalization

   ```text
   mu:P1_r x P1_u -> Disc subset P3,
   (double root r, residual root u) |-> 2r+u,            (0.4)
   ```

   with `mu^*O_P3(1)=O(2,1)`.  Its conductor is the
   diagonal `r=u`, mapping to the twisted cubic `TC` of triple roots.

2. The promoted cubic block theorem forces the affine ramification support
   `R` to be reduced, connected, and a rational forest.  Every normalization
   component is `A1`, `e_c(R)=1`, and there is no triple-root target value in
   the affine plane.  Consequently

   ```text
   phi^(-1)(TC) subset L_infinity                       (0.5)
   ```

   set-theoretically.  If `L_infinity` is not itself mapped into `TC`, the
   refined pullback is a zero-cycle of length

   ```text
   deg phi^![TC]=3*(3H)^2=27.                           (0.6)
   ```

3. The reduced infinity curve is connected.  In a common good completion,
   its resolved graph and the resolved closure of `R` are connected subtrees
   of the full first-leg boundary forest.  Hence they attach at exactly one
   resolved physical site.  In the clean-infinity stratum, where the generic
   cubic over `L_infinity` has three distinct geometric roots, this says

   ```text
   Rbar.C_infinity=12
   ```

   is concentrated at one source point.  Chau's one-target-point theorem
   then puts the entire length-27 cycle (0.6) at the same target-infinity
   point.

4. In that clean stratum, the complete ramification curve has arithmetic
   genus `28`, while its reduced degree-twelve plane branch has arithmetic
   genus `55`.  The finite birational source-to-branch map therefore has
   exact Euler/conductor defect `27`.  If the source boundary is a rational
   forest, its separate branch-incidence excess must be exactly `28`:

   ```text
   p_a(Rbar)=28 = sum_p(delta_p-r_p+1).                 (0.7)
   ```

   Thus an actual occurrence in the generic infinity stratum is not merely
   a rational specialization.  It is a simultaneous `27+28=55` maximal
   degeneration: all universal triple-root conductor is at infinity, and
   the ramification curve must spend its whole genus budget on cusp/contact
   excess without acquiring a positive-genus component or graph cycle.

5. The two degenerate infinity strata are also finite.  With `d_i` denoting
   degree over the coefficient base, the possibilities and the reduced
   affine ramification/branch degrees are

   | generic infinity inertia | infinity different | `deg_q Rbar` | `deg Bbar` |
   |---|---:|---:|---:|
   | unramified `1+1+1` | `0` | `9` | `12` |
   | `2+1`, double component of `q`-degree `0` | `E` | `9` | `11` |
   | `2+1`, double component of `q`-degree `1` | `E` | `8` | `11` |
   | `3`, with `C_infinity=3E` | `2E` | `7` | `10` |

   The last column is the degree of the closure of the **affine reduced**
   branch; the homogeneous discriminant also contains `L_infinity` with
   multiplicity `0,1,1,2`, respectively.

6. On every normalization component `A1_s` of the affine ramification, let
   `b` be the degree of its plane branch, `d=deg(r(s))`, and
   `e=deg(u(s))`.  Then

   ```text
   3b=2d+e,                 div(r-u)=(d+e)*infinity.    (0.8)
   ```

   The second equality is an equality of pullbacks of the diagonal on the
   projective normalization.  It is the exact no-affine-triple-root gate,
   not a heuristic about leading terms.  Summed over all components, the
   four rows above give

   ```text
   (sum b, sum d, sum e)=(12,9,18),(11,9,15),
                          (11,8,17),(10,7,16).          (0.9)
   ```

These statements reduce the actual-block problem to explicit twisted-cubic
pullback, one-site contact, and rational-parametrization equations.  They do
not prove that those equations are empty.  The existing exact global control
has a genus-two residual ramification component and a divisorial triple-root
line, so it lies outside the actual-block locus for two independent reasons.

## 1. Charged interfaces and object dictionary

The binding inputs are the promoted degree-three Hodge-row integration, the
corrected morphic rational-forest theorem, and the cubic Euler/one-place
integration:

```text
xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
```

The exact genus-two surface control is

```text
xmodel/bd-a2-d3-sectioned-global-control-ramification-obstruction-sol56-20260830.md.
```

Use `A=O_X(1,0)` and `B=O_X(0,1)`.  Thus `B` is a coefficient-base
fibre class and `A` is the pullback of a target line.  Keep the following
objects distinct:

```text
R_X       Cartier different/ramification divisor on the projective X;
R         reduced affine source non-etale support;
Rbar      closure of R, with coefficient one on every component;
B_aff     reduced affine target branch pi(R);
Bbar      ordinary projective closure of B_aff;
C_inf     scheme pi^*(L_infinity);
TC        twisted cubic of triple binary cubics in coefficient P3.
```

In particular `C_inf`, a possible homogeneous discriminant line component,
and `Bbar` are three different objects.

## 2. Universal binary-cubic geometry

Choose binomially normalized coordinates on `P3`:

```text
G=aS^3+3bS^2T+3cST^2+dT^3.                             (2.1)
```

Finite flatness of (0.1) is equivalent to the four cubics `a,b,c,d` having
no common projective zero.  They therefore define (0.3), with

```text
phi^*O_P3(1)=O_P2(3).                                  (2.2)
```

The discriminant is the quartic hypersurface of cubics having a repeated
root.  A generic point has a unique double root `r` and a unique residual
root `u`, giving (0.4).  The pullback of a coefficient hyperplane has
bidegree `(2,1)`, because `L_r^2L_u` is quadratic in `r` and linear in `u`.
The map is finite and birational.  It fails to be an isomorphism precisely
along the diagonal.  Its image is

```text
TC={[L^3]} subset P3,
I_TC=(ac-b^2, ad-bc, bd-c^2)                           (2.3)
```

up to harmless nonzero constants coming from a non-binomial coefficient
basis.  The twisted cubic has Chow class `3H^2`.

The root-incidence surface `X` is the pullback of the universal root cover.
Away from `TC`, its reduced ramification is the base change of (0.4).  Thus
on a normalization component of `Rbar`, the double and residual roots extend
to honest maps

```text
r,u:P1_s -> P1.                                        (2.4)
```

If the corresponding plane branch has normalization degree `b`, restriction
of (2.2) and `mu^*O(1)=O(2,1)` gives the first identity in (0.8).

The promoted cubic theorem says `S0=empty`: every affine target point has an
unramified block sheet.  A triple binary cubic has only one length-three
source point, so it would lie in `S0`.  This proves (0.5).  Each affine
branch component has normalization `A1`; its unique missing point is written
`infinity`.  The pullback of the diagonal has degree `d+e`, and all of its
support is outside the affine normalization.  Hence, for homogeneous pairs
representing (2.4),

```text
R_0(s)U_1(s)-R_1(s)U_0(s)=lambda*l(s)^(d+e),
lambda!=0,                                             (2.5)
```

where `l=0` is the unique puncture.  This proves the second identity in
(0.8), including multiplicity.

If `phi^(-1)(TC)` has no curve component, refined pullback of (2.3) gives

```text
length phi^![TC]
 = integral_P2 phi^*(3H^2)
 = 3*(3h)^2=27.                                       (2.6)
```

If it has a curve component, (0.5) forces that component to be the whole
target line at infinity.  This gives the exact dichotomy

```text
zero-dimensional length 27 on L_infinity,
or phi(L_infinity) subset TC.                          (2.7)
```

Equation (2.6) is a cycle-length statement.  It is not, without a separate
Tor/conductor audit, an identification of the scheme `phi^(-1)(TC)` with a
particular conductor quotient.

## 3. Actual cubic block topology

Let `z` be the generic point of an affine branch component.  A length-three
fibre cannot contain two non-etale points.  Since `S0=empty`, its geometric
partition is `(2,1)`.  At the codimension-one point of the normal source the
extension is tame, so the different coefficient is `2-1=1`.  Therefore

```text
R_X|_(affine target)=R                              (3.1)
```

as Weil divisors: affine divisorial ramification is reduced.  The charged
cubic theorem further gives

```text
R connected,   every R_i^nu=A1,   incidence multigraph a forest,
e_c(R)=b0(R)=1.                                       (3.2)
```

Now restrict `X` over `L_infinity`.  It is the nonzero `(3,3)` divisor
`C_inf` in `P1 x P1`.  The sequence

```text
0 -> O(-3,-3) -> O -> O_(C_inf) -> 0
```

and Kunneth give `H^0(O_(C_inf))=C`; hence its scheme, and therefore its
reduced support, is connected.  The closure of the connected `R` is also
connected.  Resolve the projective surface and the union of these curves to
strict SNC.  Both resolved unions are connected subgraphs of the full
boundary forest supplied by the actual first leg.  Two distinct attachment
sites would give two paths between connected subtrees and hence a cycle.
Every complete closure of an affine curve meets infinity, so there is exactly
one attachment site.  Parallel local branches are retained in this graph
statement.

If no component of `R_X` lies in `C_inf`, intersection theory gives

```text
R_X.C_inf=(3A+B).A=3A^2+A.B=3*3+3=12.                 (3.3)
```

Thus the clean-infinity stratum has exact contact twelve at one resolved
source site.  In this stratum the homogeneous discriminant has no infinity
line component, so every point of (2.6) lies on `Bbar intersect L_infinity`.
Chau's one-point theorem puts its support at the unique target point at
infinity.  This is the simultaneous length-12 discriminant contact and
length-27 twisted-cubic-contact gate announced in Section 0.

## 4. Infinity inertia table

At the generic point of `L_infinity`, tame degree-three inertia has three
possibilities.  Write

```text
C_inf=sum_i a_i E_i,       sum_i a_i deg_q(E_i)=3.     (4.1)
```

The infinity part of the different is

```text
R_inf=sum_i(a_i-1)E_i.                                 (4.2)
```

In the unramified case (4.2) vanishes.  In type `(2,1)`, write
`C_inf=2E+E'`.  The components have residue degree one over the target line,
and

```text
2 deg_q(E)+deg_q(E')=3,
```

so `deg_q(E)` is zero or one.  In type `(3)`, `C_inf=3E` and
`deg_q(E)=1`.  Since `R_X.B=9`, subtracting (4.2) gives the third column of
the table in Section 0.

The target discriminant valuation at a tame divisor is
`sum f_i(a_i-1)`.  It is respectively `0,1,2`.  The full homogeneous
discriminant has degree twelve, so removing its infinity-line factor gives
reduced affine branch degrees `12,11,10`.  Affine generic inertia is simple,
so no further affine branch multiplicity is hidden in these degrees.  Summing
`3b_i=2d_i+e_i` now gives (0.9).

The one-site attachment theorem persists in the double and triple infinity
strata, but (3.3), the clean length-27 concentration, and the genus computation
below must not be copied verbatim after `C_inf` and `R_X` acquire a common
component.

## 5. The exact clean-infinity genus ledger

Adjunction on the class-`(3,3)` Gorenstein surface gives

```text
K_X=B,       R_X=K_X-pi^*K_P2=3A+B.                   (5.1)
```

The ambient intersection numbers are

```text
A^2=3,       A.B=3,       B^2=0.                      (5.2)
```

In clean infinity, every ramification prime is generically simple, so the
Cartier divisor `R_X` is reduced and equals `Rbar`.  Hence

```text
p_a(Rbar)
 =1+((3A+B).(3A+2B))/2
 =1+(45+9)/2=28.                                      (5.3)
```

The target discriminant is a reduced plane curve of degree twelve, so

```text
p_a(Bbar)=(12-1)*(12-2)/2=55.                         (5.4)
```

The finite map `Rbar->Bbar` is birational and an isomorphism away from the
pullback of the conductor of the universal discriminant.  Since both curves
are connected, Euler characteristic gives the exact quotient length

```text
length(coker(O_Bbar -> pi_*O_Rbar))=55-28=27.          (5.5)
```

This arithmetic equality is independent of a transverse-cusp picture.
Equation (2.6) gives the matching universal intersection number, but the two
schemes are not identified here.

For any connected reduced complete curve `C`, let `Gamma_C` be the bipartite
branch-incidence multigraph with component and singular-point vertices.  Then

```text
p_a(C)=sum_i g(C_i^nu)+b1(Gamma_C)
       +sum_p(delta_p-r_p+1).                          (5.6)
```

The actual first-leg boundary theorem sets the first two terms to zero for
`Rbar`.  Equations (5.3) and (5.6) prove (0.7).  The integer 28 can be spent
on unibranch cusps and higher contacts, so this is a severe degeneration gate,
not by itself a contradiction.  Together, (5.5) and (0.7) account for the
full plane arithmetic genus `55` as `27+28`.

## 6. An explicit two-`(1,1)` level-two chart

The full raw coefficient space is `P^39`; finite flatness is the open where
four ternary cubics have no common zero.  Exact level two is constructible,
with the exact-level upper disjunction retained.  Rather than claiming that
one normal form covers every section, this section records one large exact
CFS chart containing the global genus-two control.

Fix `t_0=0`, put `X=x+tz`, and prescribe two successive `(1,1)` drops along
`[X:y:z]=[0:0:1]`.  For

```text
F'(t;X,y,z)=F(t;X-tz,y,z),
H=t^(-6)F'(t;t^2X,t^2y,z),                             (6.1)
```

integrality is equivalent to

```text
t^(2k) divides coeff_(X^i y^j z^k)(F')
for i+j+k=3.                                           (6.2)
```

These are twenty independent linear conditions on the forty raw
coefficients.  Imposing the moving section

```text
sigma(t)=[-t:0:1]                                      (6.3)
```

is one further independent equation: it kills the sole allowed `t^6z^3`
coefficient of `F'`.  The resulting vector space has dimension nineteen.
One raw basis is

```text
y^3,
xy^2+t y^2z,                         t y^3,
txy^2,                               x^2y+2txyz+t^2yz^2,
t^2y^2z,                             t^2y^3,
tx^2y+t^2xyz,                        t^2xy^2,
t^2x^2y,
(x+tz)^3,
t^3yz^2-tx^2y,                       t^3y^2z,
t^3y^3,
tx^3+2t^2x^2z+t^3xz^2,              t^3xyz,
t^3xy^2,
t^2x^3+t^3x^2z,                     t^3x^2y.           (6.4)
```

After projectivizing, this is a `P^18` candidate chart before stabilizer
quotients and open conditions.  The terminal reduction `H(0)` ranges over
all plane cubics through `[0:0:1]`.  The raw central fibre `F(0)` ranges over
all binary cubics in `x,y`; its three exact root strata are

```text
three distinct concurrent lines;
one double plus one simple concurrent line;
one triple line.                                       (6.5)
```

Primitivity of the intermediate models and minimality of `H` must still be
imposed.  The terminal-good-reduction open is nonempty.  For example, the
coefficient vector in the ordered basis (6.4)

```text
(-2,-1,2,-2,-2,3,3,1,3,1,-2,-1,2,3,3,3,1,3,3)       (6.6)
```

has squarefree binary `F(0)` and smooth terminal `H(0)`.  It therefore gives
an exact local level-two member after the two displayed drops.  Such a member
cannot be an actual morphic occurrence: the terminal smooth elliptic fibre
is contracted into the first-leg boundary and contributes a genus-one
component.  The terminal multiplicative strata are likewise excluded by a
boundary cycle.  Hence the only actual-block candidates in this chart lie on
the additive Kodaira strata

```text
II, III, IV, I_n* (0<=n<=4), IV*, III*, II*.           (6.7)
```

The sparse vector with coefficients one on `(x+tz)^3`, `ty^3`, and
`t^3x^2y` is the exact global control already frozen by the campaign.  It
lies in the triple-line/additive degeneration of (6.5), has a divisorial
triple-root section and a residual genus-two ramification component.  It is
therefore a surface-level positive control, not a point of the actual-block
locus.

Other CFS pair sequences, other nullcone orbit types, other moving-section
degrees, and stabilizer charts remain separate.  No coverage claim beyond
(6.1)--(6.4) is made.

## 7. Exact finite successor

The next computation should use (0.3), not normalize ramification curves one
raw family at a time.

1. Enumerate every soluble two-pass CFS chart for the five central nullcone
   types, retaining the exact-level principal-open disjunction.  Use (6.4)
   as a regression chart.
2. Split each chart into the four infinity rows of Section 0.  In the clean
   row impose

   ```text
   I_TC(phi)=(ac-b^2,ad-bc,bd-c^2),
   Supp Proj(P2/I_TC(phi))={p_infinity},
   length=27,                                           (7.1)
   Disc(phi)|_(L_infinity)=lambda*l^12.
   ```

   The three sextics in (7.1) retain the two cubic Hilbert--Burch syzygies
   pulled back from the twisted cubic; those syzygies should be used rather
   than discarded by a generic zero-dimensional ansatz.
3. In the double and triple rows impose respectively the target-discriminant
   factors `L_infinity` and `L_infinity^2`, then work with residual degrees
   eleven and ten.  Keep the cases `deg_q(E)=0,1` separate.
4. Factor the reduced residual branch by degree partitions.  For every
   component introduce polynomial normalization data and root maps satisfying
   (0.8).  The integer possibilities are finite because of (0.9).  The
   determinant identity (2.5) is cheaper than a full normalization and should
   be imposed first.
5. Only after the twisted-cubic, one-site and degree gates survive, compute
   the ramification normalization and resolved branch-incidence graph.  In
   clean infinity the survivor must realize (0.7) exactly.
6. Check global coefficient-base defects, normality, finite flatness and the
   plane-net polarization partitions last.  A finite jet or Hilbert function
   is not an occurrence.

The saturated sextic/Hilbert--Burch and normalization shards are suitable for
AWS, not local execution.  Shard keys should include CFS sequence, central
root stratum, infinity inertia row, residual branch degree partition, and
the exact open chart.

## 8. Desk replay

The following desk-scale replay verifies the linear chart, the section
condition, the terminal and central coefficient coverage, the smooth example,
and the universal degree ledgers.  It does not verify global normality or
emptiness of (7.1).

```bash
python3 - <<'PY'
import sympy as s

x,X,y,z,t=s.symbols('x X y z t')
mons=[]
for i in range(4):
    for j in range(4-i):
        k=3-i-j
        mons.append((i,j,k,x**i*y**j*z**k))

vars=[]
F=0
for r in range(4):
    for i,j,k,m in mons:
        c=s.symbols(f'c{r}_{i}{j}{k}')
        vars.append(c)
        F += c*t**r*m

Fp=s.Poly(s.expand(F.subs(x,X-t*z)),t,X,y,z)
drop=[c for (v,i,j,k),c in Fp.terms() if v<2*k]
section=s.Poly(s.expand(F.subs({x:-t,y:0,z:1})),t).all_coeffs()
A0,_=s.linear_eq_to_matrix(drop,vars)
A1,_=s.linear_eq_to_matrix(drop+section,vars)
assert (A0.rank(),40-A0.rank()) == (20,20)
assert (A1.rank(),40-A1.rank()) == (21,19)

B=[
y**3,
t*y**2*z+x*y**2,
t*y**3,
t*x*y**2,
t**2*y*z**2+2*t*x*y*z+x**2*y,
t**2*y**2*z,
t**2*y**3,
t**2*x*y*z+t*x**2*y,
t**2*x*y**2,
t**2*x**2*y,
t**3*z**3+3*t**2*x*z**2+3*t*x**2*z+x**3,
t**3*y*z**2-t*x**2*y,
t**3*y**2*z,
t**3*y**3,
t**3*x*z**2+2*t**2*x**2*z+t*x**3,
t**3*x*y*z,
t**3*x*y**2,
t**3*x**2*z+t**2*x**3,
t**3*x**2*y]
assert len(B)==19
for f in B:
    fp=s.Poly(s.expand(f.subs(x,X-t*z)),t,X,y,z)
    assert all(v>=2*k for (v,i,j,k),c in fp.terms())
    assert s.expand(f.subs({x:-t,y:0,z:1}))==0

# F(0) spans all four binary cubics and H(0) all nine cubics through P.
raw0=[s.expand(f.subs(t,0)) for f in B]
term=[]
for f in B:
    h=s.cancel(s.expand(f.subs(x,X-t*z)
             .subs({X:t**2*X,y:t**2*y},simultaneous=True))/t**6)
    term.append(s.expand(h.subs(t,0)))
raw_vec=[s.Poly(f,x,y,z).coeffs() for f in raw0]
raw_mat=s.zeros(len(raw0),10)
spatial=[x**i*y**j*z**(3-i-j)
         for i in range(4) for j in range(4-i)]
raw_mat=s.Matrix([[s.Poly(f,x,y,z).coeff_monomial(m)
                   for m in spatial] for f in raw0])
term_mat=s.Matrix([[s.Poly(f,X,y,z).coeff_monomial(
                    X**i*y**j*z**(3-i-j))
                    for i in range(4) for j in range(4-i)] for f in term])
assert raw_mat.rank()==4 and term_mat.rank()==9

co=[-2,-1,2,-2,-2,3,3,1,3,1,-2,-1,2,3,3,3,1,3,3]
f=s.expand(sum(a*b for a,b in zip(co,B)))
h=s.cancel(s.expand(f.subs(x,X-t*z)
         .subs({X:t**2*X,y:t**2*y},simultaneous=True))/t**6)
h0=s.expand(h.subs(t,0))
J=[s.diff(h0,v) for v in (X,y,z)]
for v in (X,y,z):
    oth=[w for w in (X,y,z) if w!=v]
    gb=s.groebner([j.subs(v,1) for j in J],*oth)
    assert gb.contains(s.Integer(1))
f0=s.Poly(s.expand(f.subs(t,0).subs(z,0)),x)
assert s.discriminant(f0.as_expr(),x)!=0

# Intersection/genus and four global degree rows.
A2,AB,B2=3,3,0
R2=9*A2+6*AB+B2
RK=3*AB+B2
assert (R2,RK,1+(R2+RK)//2)==(45,9,28)
assert (12-1)*(12-2)//2==55
rows=[(12,9,18),(11,9,15),(11,8,17),(10,7,16)]
assert all(3*b-2*d==e for b,d,e in rows)
print('D3_ONE_SUPPORT_UNIVERSAL_RAMIFICATION_STRATA_PASS')
PY
```

Expected output:

```text
D3_ONE_SUPPORT_UNIVERSAL_RAMIFICATION_STRATA_PASS
```

## 9. Firewalls and conclusion

- The `27+28` statement is exact only in clean infinity.  Common infinity
  components require the separate rows of Section 4.
- A conductor length, a twisted-cubic intersection cycle, a reduced branch,
  a source different and a ramification normalization are not interchangeable
  schemes.
- Rational components plus a forest do not force arithmetic genus zero;
  `delta-r+1` can absorb the full genus budget.  Equation (0.7) is a gate,
  not an impossibility proof.
- The explicit `P^18` chart is not a coverage theorem for all soluble
  level-two cubics or all global sections.
- No finite jet, coefficient morphism, rational branch parametrization, or
  surface control supplies the actual everywhere-defined first leg.
- Nothing here addresses the primitive/no-proper-block horn.

The maximum-safe advance is therefore a universal proper-cubic-block
stratification, an exact one-site theorem, the clean `27+28` genus gate, four
finite root-degree ledgers, and a nineteen-dimensional soluble CFS regression
chart.  The sectioned one-support row remains open, but any actual occurrence
must now solve the explicit finite system in Section 7.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23733`.
- Body SHA-256:
  `ad9f2e3101074ca697a6cddd5ce6eef3dc59cb32856be0b7303f761ff5c48c63`.
- Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`.
