# Event-triggered whole-campaign ideation — post sextic/`xy`/TD6 gates

Date: 2026-08-24T12:05Z  
Trust-state update consumed: 2026-08-24T12:12Z  
Charged committed bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **FROZEN IDEATION / HISTORY CORRECTION / FIVE BOUNDED CARDS / NO LAUNCH**

## 0. Executive verdict

No proof or counterexample follows from the new gates.  They do change what
the fastest next campaign should do.

The most important new fact is a **history/scope correction**, not a new
coefficient identity.  A large polynomial source shear appears to turn a
partial-`y` degree pair `(m,n)` into a pair whose total-degree gcd is

```text
deg(h) + gcd(m,n) L,
```

where `h` is the common leading-coefficient root.  If the gcd of
`deg(h)` and `gcd(m,n)` is at most two, one can apparently choose `L` so
that the new total-degree gcd is a prime or twice a prime and invoke the
classical Magnus/Appelgate--Onishi degree results.  If the primary-source
audit confirms the exact theorem and hypotheses, every partial-`y` pair with
`gcd(m,n)<=2` was already a known case, all pairs with both degrees at most
eight reduce to known cases, and the first possibly new bounded stratum is
`(6,9)` with `3 | deg(h)`.  The reviewed `(4,6)` and `(5,6)` calculations
remain correct alternate certificates and useful compiler controls; they
must not be advertised as new coverage.

The strongest genuinely new research connection is on the AS109 side.  Any
exact lift should make the completed source bidisc a finite etale rank-109
Artin--Schreier torsor over the completed target bidisc.  Henselian lifting
then gives a restricted-analytic deck action of `C_109`, and the Keller
identity makes that action volume preserving.  The action itself is a
control, not a contradiction: the all-Witt rational/restricted-analytic map
realizes it.  The possible obstruction is instead a **uniform-support or
boundary-conductor theorem for a free symplectic wild quotient**.  Its first
mixed-characteristic deformation equations are finite and computable modulo
symplectic conjugacy.

On TD6, the active deformation `q=t+B t^2+t^25` is the right kind of small
probe, but `q_2` alone is not a full reparametrization-orbit direction.  The
fastest companion calculation is to quotient all licensed boundary jets by
the truncated source-parameter action and pair the frozen left syzygy with
every transverse jet.  That can rank many deformations from one factorization
without repeatedly solving a 3,602-variable system.

Ranked by immediate campaign value:

| Rank | Card | First bounded output | Cost estimate |
|---:|---|---|---:|
| 1 | `PARTIAL-DEGREE-HISTORY-GATE` | Exact shear lemma, primary degree-theorem audit, and exhaustive pair table through `y`-degree 9 | 2--6 agent-hours |
| 2 | `AS109-WILD-SYMPLECTIC-CONDUCTOR` | Mod-`p^k` symplectic action normal form and a support-growth/conductor discriminator, first at `p=3,5` | 1--3 agent-days |
| 3 | `TD6-JET-ORBIT-ADJOINT` | Gauge/transverse basis and one adjoint sensitivity value for every smallest omitted boundary jet | 4--10 agent-hours |
| 4 | `GCD3-69-COMMON-CUBIC` | First unknown partial-degree normal form, split by the cubic discriminant | 1--3 agent-days, only after Card 1 |
| 5 | `RATIONAL-CATALAN-COMPILER` | Reproduce quotient lengths `5,14,42` for `(3,4),(4,5),(5,6)` or discard the analogy | 2--6 agent-hours |

Cards 1--3 can run independently.  Card 4 is explicitly blocked on Card 1.
Card 5 is an accelerator/control, not a proof lane.  No AWS expansion is
licensed by this report.

## 1. Evidence consumed and trust firewall

The full `COORDINATION.md`, the 46-row `APPROACHES.md`, `PROGRESS.md`, the
authoritative live tail of `notes.md`, every 2026-08-24 ideation synthesis and
deduplication record, and the newest relevant producer/review reports were
reread.  The mathematical news used here is:

1. **Reviewed exact `(4,6)` closure.**  The complete local-normalization gate
   and its hostile review close the genuine `(4,6)` normal form.  The review
   verdict is `CONFIRMED`.
2. **Reviewed exact `(5,6)` exclusion.**  The third integral, binary-form
   identity, finite-pole argument, and polynomial-infinity contradiction are
   `CONFIRMED`.  The leading complete-intersection lengths are `126` and
   `42`.
3. **Reviewed bounded `y<=6` field theorem.**  After the two sextic leaf
   reviews landed, the dedicated chain review returned `CONFIRMED`: every
   characteristic-zero Keller pair with both actual `y`-degrees at most six
   is an automorphism.  Hence an exact AS109 lift has at least one correction
   of `y`-degree at least seven.  Card 1 may still make the field coverage a
   classical corollary after a source shear.  That would change
   priority/novelty, not the algebra or the AS109 coordinate corollary.
4. **Reviewed AS109 `xy` gate.**  The 109 Hensel images of `xy` are distinct,
   so `[M(xy):M]>=109` and `xy` is not in the target field.  Under the
   separate `A_infinity=0` hypothesis, `xy` is instead a primitive generator
   and its tube minimal polynomial reduces to `Z^109-Z`.  Trace, norm, and
   discriminant are tautological there.  The hostile review verdict is
   `CONFIRMED`.
5. **Reviewed TD6 normalized-family kill.**  On the moduli curve
   `5E2-2E1^2=0`, the constant row cuts to an irreducible sextic family and a
   left syzygy has nonzero residue already at `t^4`.  The hostile review
   returned `CONFIRMED`.  It kills only the stated normalized boundary
   family, not SP-2 or a TD6 terminal class.
6. **Active TD6 successor.**  A local agent is already compiling the smallest
   deformation `q=t+B t^2+t^25`, first at `B=1`, over both the algebraic and
   degree-18 residue controls.  This report does not modify, run, or interpret
   those unfinished files as a result.

Reviews remain nonblocking.  No exact lift, terminal TD6 class kill, or JC2
inference is made here.

## 2. The history correction in exact algebraic form

Let a characteristic-zero Keller pair have actual `y`-degrees `m,n>0`:

```text
P=a_m(x)y^m+lower y rows,
Q=b_n(x)y^n+lower y rows.
```

Put `d=gcd(m,n)`, `m=d m0`, `n=d n0`.  The coefficient of
`y^(m+n-1)` in the Jacobian is

```text
n a_m' b_n - m a_m b_n' = 0.                    (2.1)
```

Thus `a_m^n/b_n^m` is constant.  Unique factorization, after harmless
constant scaling over an algebraic closure, gives

```text
a_m=h^m0,              b_n=h^n0,                (2.2)
```

for a polynomial `h`; write `H=deg(h)`.  Apply the polynomial source
automorphism

```text
(x,y) -> (x,y+x^L).
```

For `L` beyond the finitely many slopes determined by all lower `y` rows,
the displayed leading rows uniquely control total degree:

```text
deg(P)=m0(H+dL),       deg(Q)=n0(H+dL),
gcd(deg(P),deg(Q))=H+dL.                         (2.3)
```

If `gcd(H,d)=1`, Dirichlet supplies arbitrarily large `L` for which
`H+dL` is prime.  If `gcd(H,d)=2`, divide by two and choose `L` for which
`H+dL` is twice a prime.  The classical input to audit is the exact statement
that a complex plane Keller pair is invertible when the gcd of its two total
degrees is a prime or twice a prime (including all needed field and
normalization hypotheses).

Two consequences would follow immediately after that audit:

* every pair with `d<=2` is classical, since `gcd(H,d)<=2` automatically;
* if one partial degree divides the other, (2.2) allows a polynomial target
  shear to cancel the highest `y` row and descend to a smaller pair.

After ordering the pair and iterating target descent, there is no
nondivisibility pair with both entries at most eight and gcd at least three.
The first candidate is `(6,9)`, `d=3`.  It is classical by (2.3) when
`3` does not divide `H`; the first residual is therefore

```text
(m,n)=(6,9),           3 | deg(h).                (2.4)
```

This derivation was absent from local campaign history.  Earlier reviews
correctly observed that Magnus is a total-degree theorem while the new leaf
calculations use partial `y`-degree, but they did not test the large source
shear connecting the two notions.

### Card 1 — exact first falsification test

1. Prove (2.1)--(2.3) with an explicit domination bound on `L`, including
   the constant-root case `H=0`, the triangular cases where an actual
   `y`-degree is zero, and both source-shear orientations.
2. Retrieve and read the primary Magnus and Appelgate--Onishi statements and
   any correction/generalization needed for `prime` and `2*prime`.  Do not
   infer theorem scope from citers or snippets.  Local priority notes already
   say the Appelgate--Onishi/Nowicki--Nakai source check was unresolved.
3. Enumerate every ordered actual-degree pair through `(9,9)`, apply target
   descent, and record `KNOWN`, `RESIDUAL`, or the exact failed hypothesis.
4. Test the table against every existing cubic, quartic, quintic, and sextic
   normal form.  The transformed total degrees must agree with (2.3) on
   explicit random symbolic examples.

Outputs and stop rules:

* `HISTORY-CLOSED`: primary theorems and (2.3) verify; stop all widening to
  coprime/consecutive partial degrees and retarget only to (2.4) or higher
  gcd strata.
* `CLASSICAL-HYPOTHESIS-GAP`: freeze the exact theorem sentence or shear step
  that fails; retain only the genuinely uncovered pairs.
* `SOURCE-UNAVAILABLE`: no novelty claim and no `(6,7)` widening until the
  primary theorem is obtained.

The current `(4,6)` and `(5,6)` reports are not retracted under any output.
This is a history/portfolio correction.

## 3. Card 2 — `AS109-WILD-SYMPLECTIC-CONDUCTOR`

### 3.1 The finite analytic object

Assume, conditionally, an exact integral polynomial lift

```text
F=(P,Q) = (x-x^p,y) mod p,       det J_F=1,       p=109.
```

Let

```text
B=Z_p<U,V>,       A=Z_p<x,y>,       U|->P, V|->Q
```

denote the restricted Tate algebras on the unit bidiscs.  Modulo `p`, this is
the rank-`p` Artin--Schreier torsor

```text
x^p-x=-U,         y=V,
```

with deck translations `(x,y)->(x+a,y)`.  The first gate is to prove exactly
that topological Nakayama plus `det J_F=1` makes `A/B` finite etale of rank
`p`.  For the Henselian pair `(B,pB)`, finite-etale lifting is an equivalence
([Stacks Project, Tag 09ZL](https://stacks.math.columbia.edu/tag/09ZL)).
It would therefore lift the special translation uniquely to a restricted-
analytic automorphism `tau` with

```text
tau^p=1,        F o tau=F,        tau=(x+1,y) mod p.       (3.1)
```

The chain rule gives `det J_tau=1`, since both occurrences of `det J_F` are
one.  Hence a hypothetical exact AS109 lift canonically produces a free
volume-preserving wild `C_p` action on the Tate bidisc.

This is not yet rational descent and not a contradiction.  The all-Witt
rational/restricted-analytic control

```text
(g(x), y/g'(x)),        g=x-x^p,
```

has Jacobian one and realizes the expected cotangent-type quotient with a
denominator.  The useful question is whether such a quotient can have **two
polynomial invariant coordinates with a fixed finite exponent support**.

### 3.2 First-order finite equations

Write, modulo `p^2`,

```text
tau(x,y)=(x+1,y)+p(a,b).
```

Let `Delta f=f(x+1,y)-f(x,y)` and
`N=sum_(i in F_p) f(x+i,y)`.  Iterating (3.1) and imposing volume gives the
finite equations over `F_p[x,y]`

```text
N(a)=-1,         N(b)=0,          a_x+b_y=0.       (3.2)
```

Volume-preserving conjugacy changes `(a,b)` by a `Delta`-coboundary of a
divergence-free vector field.  If

```text
P=x-x^p+pP1,        Q=y+pQ1,
c(x)=((x+1)^p-x^p-1)/p mod p,
```

invariance and the Keller row give

```text
a=c-Delta(P1),      b=-Delta(Q1),
P1_x+Q1_y=x^(p-1).                                  (3.3)
```

Equations (3.2)--(3.3) are a concrete replacement for the previous literal-
support motif proposal.  They also prove that Witt level two alone cannot be
an obstruction.  Explicitly, the first digit of the rational control is

```text
P1=0,       Q1=x^(p-1)y,       a=c,       b=-Delta(x^(p-1)y),
```

which satisfies (3.2)--(3.3); this was also checked coefficientwise at
`p=3,5,7`.  The obstruction, if any, must be a gauge-invariant lower bound on
support/degree growth with Witt depth, or an equivalent wild
conductor/different at infinity.

The Oort--Sekiguchi--Suwa deformation of Artin--Schreier to Kummer
([primary 1989 paper](http://www.numdam.org/item/ASENS_1989_4_22_3_345_0/))
is relevant normal-form language.  It is not itself a polynomial-coordinate
no-go and must not be cited as one.

### Exact first falsification test

1. Prove the finite-etale rank statement and the lifted action (3.1) inside
   the registered completion.  Stop on any flatness or completion gap.
2. Over `p=3` and `p=5`, compute (3.2)--(3.3) and the next two Witt layers in
   the invariant-module basis
   `F_p[x^p-x,y]{1,x,...,x^(p-1)}`.
3. Quotient by volume-preserving conjugacy.  Use the Cartier/de Rham split of
   divergence-free polynomial vector fields in characteristic `p`; do not
   assume every closed one-form is exact.
4. For depths `2,3,4`, minimize the largest required source exponent among
   invariant coordinate pairs with Jacobian one.  The rational cotangent
   control must be recovered and should exhibit growing degree.
5. Only after a symbolic depth-uniform recurrence is visible should the
   calculation be instantiated at `p=109`.  No direct 109-by-depth brute
   force is licensed.

Outputs and stop rules:

* `UNBOUNDED-WILD-CONDUCTOR`: prove every symplectic quotient-coordinate
  tower leaves every fixed exponent support.  This would close fixed-support
  AS109 lifts.
* `FINITE-MIXED-CLASS`: exhibit a genuinely mixed, gauge-invariant bounded
  class.  Feed it to `CLOSED-SUPPORT + UNIT-L` as a counterexample motif;
  do not call it a lift.
* `CONTROL-ONLY`: if no support-growth invariant survives through depth four
  at both small primes, stop the raw cohomology lane.  The analytic action
  remains a control, and rational descent remains independently open.

This card refines the 11:03Z `AS109-TROPICAL-GROUPOID` card.  Vertices should
be symplectic conjugacy/conductor classes, not literal monomial supports.

## 4. Card 3 — `TD6-JET-ORBIT-ADJOINT`

This card is an **active-lane refinement**, not a genuinely new proof idea.
The 11:03Z ideation already proposed transport-covariant left syzygies, and
the current TD6 producer is already testing the smallest visible boundary
coefficient.

The missing correctness/speed layer is the jet-group quotient.  Under the
infinitesimal reparametrization

```text
t -> t + epsilon*a*t^2,
```

the frozen boundary pair transforms, to first order, as

```text
p=t^15       -> p + epsilon*15a*t^16,
q=t+t^25    -> q + epsilon*a*t^2 + epsilon*25a*t^26.     (4.1)
```

Thus changing `q_2` alone is not a full gauge-orbit tangent.  Depending on
the licensed truncation, it can be a transverse deformation, a gauge choice,
or an incomplete vector missing induced `p`, centering, pole, and dead-
stretch columns.  The active `B=1` probe remains useful provisionally; (4.1)
controls how its output may be generalized.

Let the centered-band system be

```text
A(theta) u = b(theta)
```

and let `lambda(theta)` be a normalized exact left-null vector.  Its
compatibility function is

```text
c(theta)=lambda(theta)^T b(theta).                   (4.2)
```

At the frozen normalized point `c(0)=rho!=0`.  This is important: the base
system is inconsistent, so the familiar compatible-base formula
`lambda^T(delta b-delta A*u)` is incomplete here unless its cokernel residual
term is retained.  The safe acceleration is to differentiate (4.2) itself,
including the derivative of the left syzygy obtained from
`lambda(theta)^T A(theta)=0`.  A nonzero first derivative does not kill the
direction; it says that the direction can change the obstruction and merits
an exact finite-parameter compatibility polynomial.  A true gauge orbit
must preserve the nonvanishing of (4.2), up to the registered unit used to
normalize `lambda`.

The derivatives and, on rank-stable strata, the full univariate
compatibility can be evaluated from a parametric version of the existing
factorization.  One need not re-solve all 3,602 global coefficients for every
candidate jet.

### Exact first falsification test

1. Compute the complete truncated action of source reparametrization, target
   normalization, common centering, pole normalization, and dead stretch on
   exactly the rows entering the constant equation and the `t^4` syzygy.
2. Row-reduce those orbit tangents and choose a canonical transverse basis.
3. Express the current `q_2`-only vector in orbit plus transverse components.
4. Differentiate (4.2) for every transverse basis vector over the same
   degree-18 field, with `lambda'` computed from the differentiated left-null
   equations.  On a true orbit, verify directly that the normalized
   compatibility changes only by a unit and never acquires a zero.
5. For every direction that enters (4.2) at the first preregistered order,
   derive the exact univariate compatibility polynomial before a full solve.
   Run a full exact rebuild only at its source-open roots or on certified
   rank-change strata.

Outputs and stop rules:

* `PURE-GAUGE`: normalize the coefficient away and do not widen on it.
* `NO-ENTRY-THROUGH-r`: the transverse coefficient does not enter the
  compatibility through a preregistered Taylor order `r`; stop that direction
  unless another row supplies an independently named mechanism.
* `COMPATIBILITY-POLYNOMIAL`: freeze the exact nonconstant polynomial, solve
  it with all source-open and rank-minor saturations, and rebuild only above
  its surviving roots.  The active `B=1` probe is one exact point control, not
  a substitute for this root calculation.
* `RANK-STRATIFIED`: if rank jumps, stop the one-syzygy shortcut and rebuild
  separately on the finitely certified rank strata.

This is also the main software acceleration recommendation for TD6: cache
the transport echelon form, its left-null basis, and parameter derivatives as
a reusable certificate rather than compiling each deformation from scratch.

## 5. Card 4 — `GCD3-69-COMMON-CUBIC`

This card launches only if Card 1 verifies that (2.4) is the first genuinely
uncovered partial-degree stratum.

The `(5,6)` binary argument works so cleanly because coprimality forces the
common homogeneous root to be linear.  For weighted initial binary forms of
degrees six and nine, vanishing Jacobian instead gives

```text
F=H^2,             G=H^3,                         (5.1)
```

for a monic cubic binary form `H`.  The surviving cubic is exactly the new
modulus that the coprime leaf calculations cannot see.  It supplies a finite
three-stratum split:

```text
Disc(H) != 0,       one double root,       one triple root.   (5.2)
```

On the squarefree stratum, after dehomogenizing one projective chart the
algebra `K[z]/(H(1,z))` over the coefficient field `K` is finite etale of rank
three.  After a splitting extension it has three geometric idempotent
factors; the final answer must descend symmetrically to `K`.  Projecting the
terminal Jacobian one-form and both polynomial boundary conditions to those
factors may turn the old one-root argument into three simultaneous residue
constraints.  On the singular strata, multiplicity may allow target descent
or reduction to already known lower-degree normal forms, but that must be
proved rather than presumed.

### Exact first falsification test

1. Normalize a genuine `(6,9)` pair over `k(x)` without dividing by the
   discriminant and retain the polynomial leading root `h` from (2.2).
2. Solve only the high Jacobian rows needed to expose the common cubic and
   the first exact coefficient-space integrals.  Use sparse rational linear
   algebra; do not build a generic exponent rectangle.
3. Derive (5.1) as a binary-form identity and split (5.2) exactly.
4. On `Disc(H)!=0`, reduce the last-row form and both boundaries modulo `H`.
   Compute whether their three geometric component residues give a nonzero
   symmetric resultant after saturation by `Disc(H)`.
5. On the double/triple-root strata, run target descent first and record the
   smallest genuinely new residual normal form.

Outputs and stop rules:

* `THREE-ROOT-OBSTRUCTION`: a nonzero saturated symmetric resultant closes
  the squarefree cubic stratum, with separately certified singular strata.
* `CUBIC-MODULI-SURVIVOR`: freeze an exact positive-dimensional coefficient
  family and stop; the next question is polynomial infinity, not a larger
  degree pair.
* `HISTORY-KNOWN`: if Card 1 or a stronger primary degree theorem covers the
  stratum, stop this computation before coefficient expansion.
* `TYPE-FAIL`: if the normalization requires unbounded denominator or loses
  polynomial boundary provenance, do not treat its binary model as a Keller
  leaf.

The old proposed `(6,7)` consecutive expansion is not a valid research
successor after the history correction.  It remains a regression test for a
normal-form compiler.

## 6. Card 5 — `RATIONAL-CATALAN-COMPILER`

The `(5,6)` leading infinity ideal has quotient length `42`.  This is exactly
the rational Catalan number

```text
Cat(5,6) = 1/(5+6) * binom(11,5) = 42.             (6.1)
```

The observed consecutive-degree pattern predicts lengths

```text
(3,4): 5,          (4,5): 14,          (5,6): 42.  (6.2)
```

These are the rational Catalan numbers associated with the coprime plane
curve singularities `z^m=t^(m+1)`.  Compactified Jacobians/semigroup ideals
carry this combinatorics; see, for example, Gorsky--Mazin,
[arXiv:1105.1151](https://arxiv.org/abs/1105.1151).  The match may explain why
the `(5,6)` weighted leading scheme was finite and why the noncoprime `(6,9)`
case retains a common cubic.  At present this is a structural analogy, not an
identification of schemes or a novelty claim.

The companion boundary complete-intersection length in the `(m,m+1)`
compiler is predicted to be

```text
product_(j=m)^(2m-1) j / m! = binom(2m-1,m),
```

giving `126` at `m=5`.  The exact first test is to regenerate the leading
ideals for `(3,4)` and `(4,5)` from the campaign normal forms and check both
the quotient length and graded Hilbert series.  A copied numerical sequence
is not evidence.

Outputs and stop rules:

* If (6.2) and the Hilbert series match, use semigroup-cell indexing to
  generate first-integral and infinity certificates, and apply the compiler
  to the multibranch cubic of Card 4.
* If either earlier case mismatches, discard the compactified-Jacobian
  analogy.  Keep the `(5,6)` length as an isolated exact certificate.

This card is new in local campaign history, but all coprime coverage it
touches is expected to be classical after Card 1.  Its value is automation
and conceptual compression.

## 7. Deliberately rejected near-misses

### 7.1 Primitive-element norm / horizontal-line factor

The reviewed `xy` gate suggests translating the primitive observable to
`w_(c,d)=(x+c)(y+d)`.  On the `V=1` tube its residues remain pairwise distinct
when `1+d` is nonzero modulo `p`, and norms factor multiplicatively.  For
`c,d in F_p`, the special Artin--Schreier fibre has the exact relation

```text
W^p-(V+d)^(p-1)W+U(V+d)^p=0.                       (7.1)
```

It is tempting to interpret the `p`-fold line factor in the constant term as
a boundary obstruction in characteristic zero.  This is **not launch-ready**.
The confirmed `xy` review already shows that local trace/norm/discriminant
data are split-etale tautologies.  Globally the field norm is rational, and
uncontrolled infinity denominators can absorb the apparent line
multiplicity.  Reopen only after an independent integrality or denominator
bound for the norm; otherwise this is a reformulation of the missing
different/asymptotic-set receiver.

### 7.2 Consecutive-degree first integrals as new coverage

The `(5,6)` identities strongly suggest a uniform `(m,m+1)` hierarchy with
`m-2` polynomial first integrals, complete-intersection length
`binom(2m-1,m)`, and Catalan infinity length.  This is a genuinely useful
compiler pattern, and its fractional-power form resembles dispersionless
Gelfand--Dickey constructions.  It is **not** a new JC theorem if Card 1 is
correct: every consecutive pair has partial-degree gcd one and is already
classical after shear.  Do not spend a research lane on `(6,7)` except as a
small regression for Card 5.

### 7.3 The analytic deck action as a contradiction

Finite-etale/Henselian lifting is expected to produce the analytic
`C_109`-action for every exact lift.  The all-Witt rational control does the
same.  Only a bounded polynomial-invariant or boundary-conductor obstruction
has discriminatory content.  Formal permutations, symmetric functions, and
the existence of the action itself do not descend a rational deck map.

### 7.4 TD6 `q_2` as an intrinsic modulus

Until the orbit computation (4.1) is done, `q_2` is a coordinate on the
chosen slice, not an invariant modulus.  A positive or negative `B=1` result
is exact for that family but cannot be extrapolated to all licensed boundary
data without the jet quotient.

## 8. All-46 disposition

Every canonical approach row was reconsidered.  The following partition
accounts for all 46 rows; a raise means a new named client, not a theorem.

* **Raised/redesigned by a concrete client:** `2,19,21,38,46`.
  These are TD6 global realization, AS/Witt lifting, p-adic Hensel, symbolic
  initial/gauge geometry, and certificate software.
* **Conditional client after the history audit:** `3,6,8,9,29,43,45`.
  The common-cubic/approximate-root compiler touches strip ODEs, one-place
  semigroups, formal inverse/Magnus identities, Hamiltonian coefficient
  flows, composite coordinates, and differential algebra.  None is raised
  independently until Card 1 leaves a genuinely new stratum.
* **Adjacent but absorbed, no independent vote:** `7,25,26,28,31,33,34,39`.
  Asymptotic sets, monodromy, log surfaces, integrality, action forms, pole
  removal, and cohomology supply language for the wild conductor or common
  cubic; their old global receiver gaps remain.
* **Lowered:** `44`.  The Moskowicz prime-degree proof is now hostile-review
  confirmed unsupported in its first case; it cannot consume AS109.
* **No rank-changing delta:**
  `1,4,5,10,11,12,13,14,15,16,17,18,20,22,23,24,27,30,32,35,36,37,40,41,42`.
  Existing stops/holds remain.  No new book cell, unrestricted D/Witt depth,
  generic sparse search, dim-3 descent, ordinary residue, or collision-
  connectedness sequel is reopened.

## 9. Parallel allocation for speed

With four live reasoning slots, the best immediate allocation is:

1. **Coordinator/integrator:** Card 1, because it can cancel entire known-case
   queues and changes what counts as progress.
2. **TD6 producer:** continue the active exact `q_2` deformation without
   waiting for review; run Card 3 as its parallel diagnostic or immediate
   follow-up.
3. **AS producer:** Card 2 at small primes, beginning with the finite-etale
   theorem and exact mod-`p^2` normal form, not with `p=109` brute force.
4. **Adversarial/certificate slot:** independently audit whichever new
   producer lands first; otherwise build Card 5 or attack the first nonzero
   conductor invariant.

As soon as Card 1 returns `HISTORY-CLOSED`, retarget any `(6,7)`/consecutive
coefficient work to Card 4.  Producer-positive results freeze immediately and
enter hostile review in the background; independent work continues on their
provisional scope.  A review finding changes downstream only when it attacks
a consumed hypothesis.

Do not allocate AWS.  The next expensive computation should be licensed by
one of: a finite symplectic normal-form grammar, a TD6 transverse direction
with vanishing adjoint obstruction, or a source-honest `(6,9)` normal form
surviving Card 1.

## 10. Deduplication record and source limits

Local history was searched before ranking for the exact mechanisms
`large source shear + partial degree`, `wild symplectic C_p action`, the carry
equations (3.2)--(3.3), `rational Catalan`/`length 42`, and the full TD6
reparametrization orbit.  Results:

* the AS literal-support/groupoid, cotangent/Fitting, Witt escape, different,
  trace, and action-residue themes already existed, but the finite-etale deck
  action plus symplectic carry/conductor quotient did not;
* transport-covariant TD6 left syzygies were proposed at 11:03Z, so Card 3 is
  explicitly a refinement;
* one-place normalization already paid off on `(4,6)` and is not relaunched;
* the consecutive complete-intersection pattern and rational-Catalan match
  were absent locally, but their mathematical coverage is expected to be
  prior art after Card 1;
* the source-shear bridge was absent from the bounded-`y` reports and their
  reviews and therefore receives the highest-priority history gate.

Closest literature context was checked only far enough to avoid a false
novelty claim.  Abhyankar--Assi
([arXiv:math/0209159](https://arxiv.org/abs/math/0209159)) treats meromorphic
Jacobian pairs and approximate roots; it does not by itself certify the exact
campaign normal forms.  Oort--Sekiguchi--Suwa supplies mixed-characteristic
cyclic-cover context, not the desired polynomial invariant obstruction.
Gorsky--Mazin supplies the rational-Catalan/compactified-Jacobian context, not
an identification with the campaign quotient ideal.  The Appelgate--Onishi
primary theorem remains the explicit unresolved source item of Card 1.

## 11. Frozen provenance checksums

These are the exact bytes consumed for the core state and event gates.  The
working tree was concurrently active; a checksum is provenance, not a claim
that another agent did not later append or edit its own file.

| Input | SHA-256 |
|---|---|
| `COORDINATION.md` | `b41f4ffca4a528038a1a226d46612b25067f5b777f270ad5781eca7327f30060` |
| `APPROACHES.md` | `9adc385de0d2f1a9f3cecdd1f8fc9114154143e2825c445c019a60ecabc3849d` |
| `PROGRESS.md` | `3a378509ea61c7f987187fe81d4008d19a195683302b3b320af66f49eb51abe1` |
| `notes.md` | `80e47682ac95e3e2193e6bcb821a64ed8e52f7364a2f25e24e8e9fb699cb1290` |
| `xmodel/ideation-20260824T1103Z-fresh-connection.md` | `fecc476e369989e7a03a603ae24ad30544f90dad649d7813bc76b83bf8d39db1` |
| `xmodel/as109-bounded-y6-chain-audit-20260824.md` | `1078bbdd47ccf085900b93b165ee268d314d2cc4e387b30ad81c4a40817e12f3` |
| `xmodel/as109-bounded-y6-chain-review-grok-20260824.md` | `81669337bf038ae2bb2d81c20bec7ef92a97eaeaa03f906d0a20c33bf20a9115` |
| `xmodel/as109-sextic-46-local-normalization-gate-20260824.md` | `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac` |
| `xmodel/as109-sextic-46-closure-review-grok-20260824.md` | `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c` |
| `xmodel/as109-sextic-56-exclusion-20260824.md` | `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4` |
| `xmodel/as109-sextic-56-exclusion-review-grok-20260824.md` | `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70` |
| `xmodel/as109-xy-membership-gate-20260824.md` | `09d5654aeeeee55f9c5766e75f1a975db12a5701258efb25b04606fb4fc72729` |
| `xmodel/as109-xy-membership-review-grok-20260824.md` | `04c4d3dc8342141c4b1cb615e232a00053a056825fddbe55dd3ba5c2b44b8ac0` |
| `xmodel/td6-moduli-uniform-third-band-20260824.md` | `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` |
| `xmodel/td6-moduli-uniform-third-band-review-grok-20260824.md` | `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` |

## 12. Scope and freeze

This is an ideation report.  It edits no canonical top-level file, launches no
agent or external reviewer, makes no AWS call, and proves or disproves no
instance beyond the frozen inputs it cites.  Every proposed card has a first
falsification test, dependency, and stop rule.  The main portfolio change is
to audit history before widening bounded partial degree, and to replace
literal AS109 supports by a symplectic wild-quotient invariant.
