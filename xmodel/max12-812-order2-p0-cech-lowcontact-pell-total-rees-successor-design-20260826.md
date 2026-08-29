# `(8,12)` order two: collision Cech, low-contact, and Pell successor

Date: 2026-08-26

Status: **CORRECTION-AWARE SOURCE DESIGN.  IT RECORDS ONE NEW DUAL-AWS
PRODUCER, A FINITE LOW-CONTACT SHARDING, AND A LIVE PELL/CHEBYSHEV
RECEIVER.  NO TOTAL-REES, MOVING-`p`, SQUARE-BRANCH, OR ORDER-TWO
VERDICT.**

## 0. Outcome first

The `p=0,D(k10)` collision programme now has a clean three-layer
architecture.

1. Form the actual total Rees algebra of

   ```text
   J1=(rs,cs,c0,c1),
   J2=(a0,a1) on V(J1),
   ```

   before putting the Kummer separation coordinate `rho` equal to zero.
   The first two blowups give six ordered standard charts.  Their coverage
   is tautological for DVR arcs; their identification with the frozen source
   clients is not.
2. On the two residual `A` charts, the only fixed-`p=0` secondary contacts
   not already routed are a finite list: `C` contacts two and three and the
   tangent-`A`, `R`-contact-one mixed faces.  All of these occur by absolute
   grade fifteen.  Thus the defective unbounded V12 fan is unnecessary.
3. The complement `V(J1+J2)` is not empty by projectivization.  It is the
   exact-square/all-load receiver.  Its common fourth-contact face contains
   an explicit nonsquare Chebyshev/Pell family.  That family must be sent to
   the complete terminal `[6,2]` and both Taylor clients; it must not be
   projected back to the unit-`k10` cusp.

The reviewed odd and cusp units, the reviewed high-contact `A` units, and
the new `C`-contact-one producer are endpoints for this architecture.  They
do not yet constitute one total chart.

## 1. Frozen status and quarantines

The following inputs are logically usable at their stated scopes:

```text
6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92
  xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md

22d32f1840f47da09660fd8f6b37966562b6532e8bad12544953a7cbb6185c85
  xmodel/cross-empty-special-fibre-valuative-propagation-20260826.md

aaf20f09b06ea9e74d33b4f64f29778c664375c61e0589b3cf7784976e28835c
  xmodel/max12-812-order2-p0-cusp-raw-g12-cech-certificate-v2-hostile-review-grok-20260826.md

f48401b5a5635fa8212db76ac0f9f7eea44e8904e0b1aa18a4fbbc38389d56c3
  xmodel/max12-812-order2-p0-odd-grade14-unit-elimination-promotion-20260826.md

4aeee7980586fc4c7c5456c04b84b02527251f6bd68e10f5a028cc5d19ef1f16
  xmodel/max12-812-order2-p0-a-highcontact-cech-elimination-promotion-20260826.md

997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114
  xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md
```

The raw cusp identity is now hostile-review confirmed:

```text
32768*g12_6-35*k10*rs^4
  =-4096*rs*g10_2-8192*cs*g10_3.                    (1.1)
```

Thus its endpoint is a unit on `D(k10*rs)` without normalization; the
nonreduced row `g10_3` is essential.  The fixed-`p=0`, `C`-contact-one
producer is dual-AWS exact/good-prime PASS with

```text
g11_2=(3/8)*a0*e0,
g11_1=(3/8)*(a1*e0+a0*e1),
g12_2|_(a0=e0=0)=(3/32)*e1^2.                      (1.2)
```

Its result and evidence-manifest hashes are respectively

```text
162a279615931f93bd15e3ea176e46c30669449cae9e35dd41305d174559fd23,
958dd6b3336d024f3b575420413ffa26b0b7811a6972a3e955c9ea2804810de1.
```

It remains provisional until its live hostile review lands.

The generic V12 unbounded `d=1` output and every fan obtained by shifting
only its seven displayed forms are **quarantined**.  At larger contact the
frozen source has omitted `k6`, `k2`, and target terms.  Nothing below uses
that output.  The hand dominance of `kR2A` is still a valid comparison among
the named affine forms, but it is not a source-completeness theorem.

## 2. The total algebra and the exact Cech problem

Work over the Kummer base

```text
p=-2*rho^2,              Lrho=z^2-rho^2=(z-rho)(z+rho),       (2.1)
```

with `rho` not inverted.  Let `Btot` be the finite ordinary source algebra
obtained from all seven rows through absolute grade thirty-eight, retaining
every coefficient jet that can occur by that grade, all three load series,
and the four target series.  The source equations are

```text
Phi_ell = r_ell(f,
                  sigma^4*k10(sigma),
                  sigma^12*k6(sigma),
                  sigma^20*k2(sigma))
          -sigma^(2*(12+ell))*delta_ell(sigma),

(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4).      (2.2)
```

No coefficient of (2.2) is eliminated before every later coefficient has
been emitted.  In particular `J` remains subject to the registered interior
saturation; it is not set to zero in a special-fibre convenience quotient.

Form the actual Rees algebra

```text
Rees_Btot(J1)=image(Btot[Yrs,Ycs,Yc0,Yc1]
                    -> Btot[U], Yi |-> xi*U),        (2.3)
```

using its kernel, not the symmetric-algebra equations alone.  Only after
(2.3) is formed may one set `rho=0` and take the degree-zero standard
charts.  On `V(J1)`, repeat with `J2`.  The ordered special-fibre charts are

```text
D_+(rs),
V(rs) D_+(cs),
V(rs,cs) D_+(c0),
V(rs,cs,c0) D_+(c1),
V(J1) D_+(a0),
V(J1,a0) D_+(a1).                                  (2.4)
```

The complement is exactly the named receiver `V(J1+J2)`.  The DVR
universal property proves that (2.4) covers every arc for which `J1` or
`J2` is nonzero.  It does not prove that the present specialized scalings
are the base changes of (2.3).

### Gate T

For every chart in (2.4), the total-source client must print:

1. the actual Rees-kernel presentation and a torsion/saturation check;
2. a map in both directions between its `rho=0` base change and the frozen
   odd, cusp, trivial-`C`, or `A` source algebra;
3. equality of the raw row ideals, not merely equality of radicals; and
4. a localized identity

   ```text
   s=sum_i H_i*Phi_i+rho*H,                          (2.5)
   ```

   where `s` uses only the registered unit of that chart.

The cusp identity (1.1) supplies its special-fibre endpoint but not the map
in item 2.  If all six identities (2.5) pass and the terminal receiver is
empty, the reviewed empty-special-fibre lemma excludes every positive
rational `ord(rho)` after finite ramification.  Until then, no moving-`p`
claim is licensed.

On `D(rho)`, retain both root orientations

```text
R_+-=rs/4 +- cs*rho,
C_+-=(c0 +- c1*rho)/2,
A_+-=a0 +- a1*rho,                                  (2.6)
```

and the deck `rho -> -rho`.  A cross-route to the reviewed nonsquare K3
theorem is allowed only after a complete source-row transform produces its
coordinates and proves its open `D(b*m)`.  Similar root values are not such
a transform.

## 3. A finite fixed-`p=0` secondary-contact fan

On `V(J1)` and one of the `A` opens, write

```text
L=z^2,
K=L^2+sigma^(2+r)*(B0+sigma*B1+...),
D=L*(A0+sigma*A1+...)+sigma^c*(E0+sigma*E1+...),
f=K^2+sigma^5*D,                                    (3.1)
```

where `A0=a1*z+a0`, `B0=b1*z+b0`, and
`E0=(e1*z+e0)/2`.  Here `r,c>=1` are the first secondary contacts and
`k10=k0+O(sigma)` is a unit.  Relative to absolute grade ten, the first
possible negative terms from `f^(3/2)+sigma^4*k10*f^(5/4)` have weights

```text
AC       c,             C2       2c,
RA2      2+r,           RAC      2+r+c,
RC2      2+r+2c,        kR3      3r,
kRC      1+r+c,         kR2A     3+2r,
kA2      4,             kAC      4+c,
A3       5.                                             (3.2)
```

The three terms `RAC,RC2,kAC` are strictly above `AC` or `C2`, and
`kR2A` is above one of `kR3,kA2`; they remain source sentinels but do not
index a primitive face.  Unlike V12, this is used only through absolute
grade fifteen.

The first lower-load terms, written at their actual absolute grades, are

```text
k6:
 (3/8) sigma^(16+2r) k6*B0^2/L,
 (3/4) sigma^(17+c)  k6*E0/L,
-(1/16)sigma^(18+3r) k6*B0^3/L^3,
-(3/8) sigma^(19+r)  k6*A0*B0/L^2,
-(3/8) sigma^(19+r+c)k6*E0*B0/L^3,
-(3/32)sigma^22      k6*A0^2/L^3,
-(3/16)sigma^(22+c)  k6*A0*E0/L^4,
-(3/32)sigma^(22+2c) k6*E0^2/L^5;

k2:
 (1/2) sigma^(22+r)  k2*B0/L,
-(1/8) sigma^(24+2r) k2*B0^2/L^3,
 (1/4) sigma^25      k2*A0/L^2,
 (1/4) sigma^(25+c)  k2*E0/L^3,
 ... .                                                  (3.3)
```

The target grades are exactly `28,32,36,38`.  Formula (3.3) is a
through-grade-fifteen exclusion and a source-census control, not a claim
that the displayed truncation is the full later fan.  It proves that no
lower load or target can enter any shard below.

### 3.1 Constant `A` open

On `D(a0)`, the first `AC` face has two deepest coefficients and forces the
leading `E0` to vanish whenever it appears before an `R` face.  If `r=1`,
the deepest poles of `-3*B0*A0^2/(8L^2)` force `b0=b1=0` before a loaded
`R^3/L` term can cancel them.  Once `r>=2,c>=4`, the separately reviewed
high-contact theorem supplies the grade-fifteen pure cube.  Thus a source
replay needs only to bridge `c=2,3` to those two elementary statements; no
unbounded fan is required.

### 3.2 Tangent `A` open

Put `a0=0` and localize at `a1`.  The first `AC` equation kills `e0` but
allows the tangent allocation `E0=e1*z/2`.  The contact-one source has
already raised this allocation by the raw square `(3/32)e1^2`.

There is a necessary horizontal routing before using the deepest formulas
below.  Write the complete constant coefficient of `A` as

```text
A_const(sigma)=a0+sigma*(A1)_0+sigma^2*(A2)_0+... .  (3.3a)
```

If (3.3a) is not identically zero, its first nonzero coefficient is a moving
exit to the constant-`A` receiver.  It must be excluded there by a raw total
chart identity; setting it to zero in the tangent client is not legitimate.
If every coefficient in (3.3a) vanishes, then

```text
A(sigma,z) belongs to z*Q[[sigma]][z]_(degree<=1),   (3.3b)
```

and every constant part `(Aj)_0` is genuinely zero.  This exact dichotomy is
the horizontal module/contact-raising induction.  It removes apparent
cancellations such as `(A1)_0*(E1)_0/z^2` only after the moving exit has been
source-certified.  Each tangent shard must therefore have two outputs:
`ROUTE_CONSTANT_A` with its raw overlap map, and `STAY_TANGENT` satisfying
(3.3b).  The equations below are preregistered only on `STAY_TANGENT`, after
the preceding constant-`C` connection rows have also been imposed raw.

The remaining finite shards and their deepest preregistered equations are:

1. `c=2,r>=3`: after the grade-twelve `AC` row and its grade-thirteen
   connection, the grade-fourteen deepest pole is

   ```text
   (3/32)*e1^2.                                      (3.4)
   ```

   It should raise `C` on `D(e1)` in the `STAY_TANGENT` quotient.  Before
   (3.3b), the grade-fourteen pole also contains correction products and
   (3.4) is not a raw ambient identity.
2. `c=2,r=2`: the grade-fourteen deepest pole is instead

   ```text
   (3/32)*(e1^2-4*a1^2*b0).                         (3.5)
   ```

   The possible sheet `e1^2=4*a1^2*b0` must be carried, with every
   grade-twelve/thirteen row raw, to grade fifteen.
3. `c=3,r>=3`: after the first `AC` connection rows, no competing term
   reaches pole three at grade fifteen, whose predicted coefficient is

   ```text
   -(1/16)*a1^3.                                    (3.6)
   ```

4. `c=3,r=2`: the grade-fourteen `RA2` row must first force the constant
   part of `B0` to zero; the same deepest cube (3.6) is then predicted.
5. `r=1`: before any radical, the grade-thirteen `RA2+kR3` face has

   ```text
   [z^-2]=(1/16)*b0*(5*k0*b0^2-6*a1^2),
   [z^-1]=(1/16)*b1*(15*k0*b0^2-6*a1^2)
           + connection.                            (3.7)
   ```

   For `c>=4` the connection in (3.7) is zero.  Hence either `B0` contact
   rises, or

   ```text
   b1=0,                 5*k0*b0^2=6*a1^2.          (3.8)
   ```

   This constant-`R` Kummer sheet is a live grade-fourteen/fifteen
   receiver.  For `c=3`, the connection is `(3/8)*a1*e0`; for `c=2`, after
   the preceding grade-twelve row it is
   `(3/8)*(a1*(E1)_0+(A1)_0*e1)`.  These two mixed sheets must be emitted
   separately rather than obtained by setting a correction to zero.

Equations (3.4)--(3.8) are preregistered leading/deep-pole identities on the
typed tangent submodule (3.3b).  They are not ambient raw identities and are
not promoted until all seven ordinary rows, the moving coefficient
connection, every correction that can tie, the `ROUTE_CONSTANT_A` overlap,
and the raw predecessor ideal are reconstructed from (2.2) in exact Q.  The
finite shard list is

```text
(c,r)=(2,>=3),(2,2),(3,>=3),(3,2),
r=1 with c=2, c=3, or c>=4.                          (3.9)
```

Together with `c=1` and the reviewed `r>=2,c>=4` theorem, (3.9) covers the
fixed-`p=0`, leading-`A` secondary fan through the cubic separator.

## 4. The all-zero exact-square/all-load receiver

On `V(J1+J2)`, a later correction can have

```text
f=Q^2,
P(T)=k10*T^2+k6*T+k2,
H=sqrt(Q)*P(Q),                                     (4.1)
```

where the square root is the branch at infinity.  If the first seven
negative Laurent coefficients of `H` vanish and `A=[H]_+`, then

```text
H-A=O(z^-8),
A^2-Q*P(Q)^2 is a polynomial of degree at most two. (4.2)
```

The bound in (4.2) is the unconditional one: `O(z^-8)` times a degree-ten
polynomial is `O(z^2)`.  A sharper constant remainder must come from the
tail equations, not from this estimate alone.

Normalize `k10` on `D(k10)` and write

```text
Q=z^4+p*z^2+c*z+r,
Delta=p^2-4*r,
T=z^2+p/2.                                          (4.3)
```

A live exact-Q/good-prime producer tests that the reduced seven-tail support
is the union of

```text
square:
 c=0, Delta=0;

Chebyshev:
 c=0,
 16*k6=5*k10*Delta,
 256*k2=5*k10*Delta^2.                              (4.4)
```

The Chebyshev component is not hypothetical.  It has the exact polynomial
identity

```text
A = k10*(T^5-(5*Delta/16)*T^3+(5*Delta^2/256)*T),

A^2-Q*P(Q)^2 = k10^2*Delta^5/262144.                (4.5)
```

Equivalently `k6^2=5*k10*k2`.  At `p=0`, (4.4) becomes

```text
4*k6=-5*k10*r,          16*k2=5*k10*r^2.            (4.6)
```

For example

```text
Q=z^4-1,
P(Q)=16*Q^2+20*Q+5,
A=16*z^10-20*z^6+5*z^2
```

satisfies `A^2-Q*P(Q)^2=1`; its negative tail begins strictly after the
seven tested coefficients.  Thus there is no theorem saying that the
all-zero receiver forces `Q` square.

The factorization `Q=(T-s)*(T+s)`, `4*s^2=Delta`, has the factor deck
`s -> -s`; (4.4)--(4.5) descend to `(p,Delta)` and require no chosen `s`.
The hyperelliptic deck `sqrt(Q)->-sqrt(Q)` and the source/root-separation
deck are separate actions and must be recorded separately.

### 4.1 Exact grading and why the cusp cannot consume it

Let `lambda=ord(Lambda)` and let `u` be the contact of `Q-L^2`.  The first
negative weights of the three loads are

```text
W10=2*lambda+ord(k10)+3*u,
W6 =6*lambda+ord(k6) +2*u,
W2 =10*lambda+ord(k2)+u.                            (4.7)
```

The target weights are

```text
Tell=(12+ell)*lambda+ord(delta_ell).                 (4.8)
```

With unit loads, the three expressions in (4.7) tie exactly at
`u=4*lambda`.  The `mu2` target can tie there as well.  Hence the literal
source face must retain `mu2`; the seven-zero-tail classifier (4.4) is a
real subface, not yet an exhaustion theorem for the affine-target row
system.  A successor must also classify

```text
h1=0, h2=mu2, h3=...=h7=0                          (4.9)
```

and its correction prolongations.

At `p=0`, the Chebyshev point has a nonzero constant leading `Q-z^4`, but
`k10,k6,k2` all contribute at the same normalized grade.  The confirmed
cusp unit was proved in a lower unit-`k10` face before `k6,k2` enter.  Using
that unit after deleting the tied lower loads would change the source and is
forbidden.

### 4.2 Terminal and Taylor successor

As soon as the exact seven-tail producer passes, proceed provisionally on
both components of (4.4), without waiting for review:

1. substitute the rational Chebyshev presentation (4.4)--(4.5) into the
   complete ordinary source, retaining all correction jets and the raw
   grade of `mu2`;
2. extract every subsequent coefficient through grade thirty-eight and
   stop at the first raw localized unit or freeze the surviving component;
3. pull the survivor to the strict terminal `[6,2]` source, retaining the
   exact toric relation between its parameter and `Lambda`; and
4. emit both finite Taylor families.  Until a two-sided source map identifies
   the coefficient functions and their germs, Taylor output is typed
   compatibility data, not a global contradiction.

The same branch is simultaneously a proof lane and a counterexample lane:
a terminal unit kills the Pell component, whereas a full grade-thirty-eight
and Taylor-compatible prolongation gives a highly structured candidate
from which to reconstruct the original pair.

## 5. Minimal AWS clients

All CAS payloads below run on AWS, one capped core per shard unless a measured
profile justifies more.

### Client L: seven low-contact shards

Use one compiler, but emit the seven independent inputs in (3.9).  For each
input run exact Q and one independent good prime on different hosts.  Every
input must:

- reconstruct all seven frozen source rows rather than insert (3.4)--(3.8);
- retain correction jets through grade fifteen, all three loads, and all
  four targets;
- verify exact coefficient extraction and the moving Faber connection;
- print the raw predecessor basis, the `ROUTE_CONSTANT_A` map, and the
  deepest-pole identity only on the certified `STAY_TANGENT` module;
- include a negative control deleting the first correction that can cancel
  the shallow pole; and
- forbid `radical`, `primdec`, or saturation before the raw identity.

Stop a shard at a registered unit, a contact raise to an already covered
shard, or one explicit normalized component.  A modular-only unit or a
source row missing a later load is no verdict.

### Client T: total Rees bridge

Emit (2.2)--(2.5) chartwise.  Shard the six charts, because the Rees kernels
and localized maps are logically independent.  The cusp chart should reuse
(1.1), not recompute its normalization.  The negative control replaces the
actual Rees kernel by the naive symmetric presentation and must exhibit a
torsion or base-change discrepancy on at least one nonreduced collision
chart; if it does not, certify equality rather than merely assuming the
control should fail.

Stop Gate T only when all six maps and raw localized identities pass, or at
the first explicit missing source direction.  Do not infer total coverage
from five passing charts.

### Client P: Pell support and prolongation

Keep the current exact-Q/good-prime seven-tail classification as `P0`.
Then run:

```text
P1: characteristic-zero triangular/Bézout proof of (4.4), not only radical;
P2: affine-target system (4.9), with raw nilpotent support retained;
P3: square and Chebyshev correction prolongations through grade 38;
P4: terminal [6,2] pullback on each survivor;
P5a/P5b: the two finite Taylor pullbacks, independently typed.
```

The exact identity (4.5) is a mandatory compiler self-control.  In every
good prime, the denominators `2,5,16,256,262144` and every decisive
coefficient must remain nonzero.  Exact Q is the theorem lane; modular
agreement is never promoted by itself.

## 6. Stop and promotion rules

The collision programme closes only after all of the following hold:

1. the seven low-contact shards terminate in reviewed units/contact raises
   or source-certified overlaps;
2. Gate T proves that all six specialized endpoints are base changes of one
   total Rees source;
3. the exact-square/all-load receiver is exhausted, including (4.9), all
   lower-load boundaries, and the grade-thirty-eight target; and
4. every surviving normalized component fails the terminal passport or one
   of the two Taylor families.

If instead one component satisfies the complete source through grade
thirty-eight and both Taylor families, freeze it immediately and run
reconstruction, Jacobian verification, and adversarial falsification in
parallel.  Review is background and nonblocking once exact-Q source evidence
has passed; a review defect quarantines downstream conclusions but does not
erase independent frozen calculations.

## 7. Explicit nonclaims

This note does not promote the live `C`-contact-one result, equations
(3.4)--(3.8), or the live Pell radical calculation.  It does not prove that
the six specialized clients are total-Rees base changes, that the
affine-target system (4.9) has only square/Chebyshev support, or that the
Chebyshev component passes or fails terminal/Taylor conditions.  It does not
exclude positive-order `p`, the `k10=0` boundary, other square Rees cones,
or any nonsquare component except by an explicit licensed overlap.  It does
not close the square branch, order two, `(8,12)`, maximum twelve, or JC2.
