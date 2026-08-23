# Row 34: two-dimensional tangent sweep and pole removal

**Date:** 2026-08-23  
**Scope:** plane polynomial Keller maps over \(\mathbf C\), the rationalized
plane tangent sweep, and the promoted residue-A formal template.  
**Verdict:** **LANDING INGREDIENT ONLY; HOLLOW AS A STANDALONE ROUTE.** The
line-pullback/pole ledger is a valid dimension-two necessary-condition
instrument, but on residue A it is exactly Riemann--Hurwitz plus the already
known one-pole criterion. The literal two-dimensional tangent-sweep
polynomialization dies by an elementary one-divisor saturation. A genuine
tangent-to-\(A(F)\) experiment cannot yet be run because residue A is
single-fiber formal data, not a polynomial pair or a cross-fiber equation for
the nonproperness curve.

This executes [APPROACHES.md row 34](../APPROACHES.md) and its cheapest-test
specification. The higher-dimensional source is Gao's
[tangent-sweep construction](https://arxiv.org/abs/2608.00222); the relevant
plane pole theorem is Chau's 1999 paper, locally
[archived here](../refs/chau1999_apm71_full.pdf).

---

## 1. Three objects that must not be conflated

Let

\[
 F=(P,Q):\mathbf A^2_{x,y}\longrightarrow\mathbf A^2_{U,V},
 \qquad J(P,Q)=1,
\]

and let \(\mu=[\mathbf C(x,y):\mathbf C(P,Q)]\) be its geometric degree.
There are three different constructions behind the slogan “tangent
sweep/pole removal.”

1. **Gao--Speyer sweep.** A two-parameter surface sweeps the tangent lines of
   a parametrized plane curve. Its Jacobian has a single linear ramification
   factor. A third coordinate in Gao's construction records that factor and
   permits a monomial twist which turns ramification into escape to infinity.
2. **Rational plane version.** A rational source change can cancel the same
   factor using only two variables. This gives an exact, generically
   many-to-one *rational* plane map with constant rational Jacobian, but it has
   a pole divisor. Clearing that divisor while retaining the degree would
   produce an actual plane counterexample.
3. **Intrinsic Keller line sweep.** For an already polynomial Keller map,
   pull back a moving target line. On each normalized pullback curve the
   complementary target coordinate is a meromorphic function with no affine
   ramification. Tangent lines to the nonproperness curve \(A(F)\) then probe
   how escaping sheets split at the boundary.

Only (3) is naturally a *proof* instrument for an arbitrary Keller map. A
polynomial map \(F\) itself has no affine poles, and restricting \(F\) to a
source affine line produces polynomials, not the poles at issue. Conversely,
if \(\mu>1\), the inverse of \(F\) is algebraic and multivalued, not rational.
A rational inverse would mean \(\mu=1\); a birational Keller map is already a
polynomial automorphism. Thus “clear the poles of the rational inverse of a
hypothetical counterexample” is ill-posed.

Vitushkin's covering is also not a rational self-map of \(\mathbf A^2\): it
is a branched topological/analytic covering model. Chau's
[polynomial no-go theorem](https://math.ac.vn/uploads/files/9901109.pdf)
shows that its simplest one-smooth-exceptional-curve form cannot occur for a
polynomial plane Keller map. Row 34's two halves are related by escape
divisors, but they are not the same construction.

---

## 2. Exact rational tangent sweep in two variables

### 2.1 Normalized sweep

Choose \(p\in\mathbf C[w]\) and define \(q\), up to an additive constant, by

\[
 q'(w)=\frac w2p'(w).
\]

The curve \(K(w)=(p(w),q(w))\) has tangent direction \((2,w)\). Its tangent
sweep is

\[
 S(\gamma,w)=\bigl(p(w)+2\gamma,\ q(w)+\gamma w\bigr).
\]

With variables ordered \((\gamma,w)\),

\[
 \det JS
 =2\bigl(q'(w)+\gamma\bigr)-wp'(w)=2\gamma.                 \tag{2.1}
\]

For a target point \((X,Y)\), eliminating \(\gamma\) leaves

\[
 W_{X,Y}(w)=q(w)+\frac w2\bigl(X-p(w)\bigr)-Y.              \tag{2.2}
\]

If \(\deg p=d\ge1\) with leading coefficient \(a_d\), then \(q\) has
degree \(d+1\), leading coefficient
\(d a_d/(2(d+1))\), and (2.2) has leading coefficient
\(-a_d/(2(d+1))\). Therefore the sweep has generic degree \(d+1\).

### 2.2 Cancel the ramification factor rationally

Use the birational source map

\[
 h(x,y)=(\gamma,w)=\left(x,\frac yx\right),\qquad Jh=\frac1x.
\]

Then

\[
 R_p=S\circ h
 =\left(p\!\left(\frac yx\right)+2x,
 q\!\left(\frac yx\right)+y\right),                       \tag{2.3}
\]

and

\[
 J(R_p)=(2x)\frac1x=2.                                    \tag{2.4}
\]

Thus (2.3) is an exact rational constant-Jacobian plane map of generic
degree \(d+1\). This is the faithful two-dimensional remnant of the
tangent-sweep mechanism.

It also exposes the obstruction without any elimination. Along \(x=0\),

\[
 \operatorname{pole}_{x=0}(R_{p,1})=d,
 \qquad
 \operatorname{pole}_{x=0}(R_{p,2})=d+1.                  \tag{2.5}
\]

The leading polar monomials are

\[
 a_d y^d x^{-d},\qquad
 \frac{d a_d}{2(d+1)}y^{d+1}x^{-(d+1)}.
\]

Neither can cancel against \(2x\) or \(y\). Hence (2.3) is polynomial if
and only if \(p\) is constant. A polynomial source or target automorphism
cannot repair this: divisorial poles are preserved under a regular source
automorphism, while polynomiality after a polynomial target automorphism
would imply polynomiality before it by the polynomial inverse.

### 2.3 Lowest exact saturation and controls

For the first Gao curve degree, write

\[
 p=a_0+a_1w+a_2w^2,
 \qquad q=b_0+\frac{a_1}{4}w^2+\frac{a_2}{3}w^3.
\]

Then

\[
\begin{aligned}
R_1&=a_0+a_1\frac yx+a_2\frac{y^2}{x^2}+2x,\\
R_2&=b_0+\frac{a_1}{4}\frac{y^2}{x^2}
       +\frac{a_2}{3}\frac{y^3}{x^3}+y.
\end{aligned}                                             \tag{2.6}
\]

The polynomial-output divisibility ideal is exactly

\[
 I_{\rm poly}=(a_1,a_2).
\]

On the degree-two chart \(a_2\ne0\), its Rabinowitsch saturation is the
unit ideal:

\[
 (a_1,a_2,za_2-1)=(1).                                   \tag{2.7}
\]

This was replayed over \(\mathbf Q\) with Singular; the reduced bases were

```text
POLYNOMIALITY_IDEAL       [a1, a2]
DEGREE_2_SATURATION_GATE  [1]
```

The gate has a live positive control. On the degree-zero component
\(a_1=a_2=0\),

\[
 R_p=(a_0+2x,b_0+y)
\]

is an affine polynomial automorphism with Jacobian \(2\). It becomes a
Jacobian-one automorphism after scaling the first target coordinate by
\(1/2\). The degree-one chart likewise saturates to the unit ideal after
inverting \(a_1\).

For the exact Gao degree-two coefficients

\[
 p=-3w^2+4w,\qquad q=-w^3+w^2,
\]

the rational plane map is

\[
 R=\left(-3\frac{y^2}{x^2}+4\frac yx+2x,
          -\frac{y^3}{x^3}+\frac{y^2}{x^2}+y\right).
\]

An independent exact Laurent-polynomial replay returned

```text
J(R) = 2
pole vector on x=0 = (2,3)
leading polar coefficients = (-3,-1)
```

There is therefore no lowest-degree direct polynomial survivor to feed a
larger coefficient search.

### 2.4 What constructive success would prove

If one found birational source/target modifications of (2.3) which

- made both outputs polynomial on an actual \(\mathbf A^2\),
- retained a nonzero constant Jacobian, and
- retained generic degree \(d+1>1\),

the result would be an explicit counterexample to JC2. Nothing else would be
needed.

The exact saturation above proves only the no-go for the direct one-divisor
normalization (2.3). It does **not** classify arbitrary birational
modifications. Allowing a rational target twist can create new pole and base
divisors, and proving that all of them are removable is already the plane
Jacobian problem in a narrowed presentation.

**CONJECTURE TS-P (one-divisor pole-removal no-go).** No nonconstant
\(R_p\) in (2.3) can be converted to a polynomial constant-Jacobian map by
birational source and target modifications which are isomorphisms away from
one irreducible boundary divisor and do not create additional exceptional
curves in the affine target.

This conjecture is deliberately narrow. In the especially simple case where
the hypothetical output has a single exceptional curve
\(\Gamma\simeq\mathbf A^1\) and is an unbranched cover off \(\Gamma\), Chau's
Vitushkin theorem already proves the output is bijective; so that subcase is
a theorem, not a conjecture. Any escape from TS-P must proliferate or
singularize the exceptional set. It would no longer be “remove one pole.”

---

## 3. The intrinsic plane Keller line sweep

The construction that applies to an arbitrary polynomial Keller map does not
start with a rational inverse. It starts with target lines.

### 3.1 Every target line gives an unramified affine curve map

Fix a determinant-one target change

\[
 H=\alpha P+\beta Q,qquad T=\gamma P+\delta Q,qquad
 \alpha\delta-\beta\gamma=1.                               \tag{3.1}
\]

Then \(J(H,T)=1\). For every \(c\), the affine curve

\[
 C_c=\{H=c\}
\]

is smooth: \(dH\) cannot vanish because \(dP,dQ\) are a basis everywhere.
The tangent vector

\[
 \tau=-H_y\partial_x+H_x\partial_y
\]

satisfies

\[
 dT(\tau)=H_xT_y-H_yT_x=1.                                \tag{3.2}
\]

Thus \(T:C_c\to\mathbf A^1\) has no affine critical point. For generic
\(c\), let \(\bar C_c\) be the smooth projective normalization. The
meromorphic extension

\[
 \bar T:\bar C_c\longrightarrow\mathbf P^1
\]

has degree \(\mu\).

Separate the boundary punctures into

\[
 \Pi_\infty=\{p:\bar T(p)=\infty\},\qquad
 \Pi_f=\{q:\bar T(q)\in\mathbf A^1\}.
\]

Write \(e_p=-\operatorname{ord}_pT\) at a pole and
\(e_q=\operatorname{ord}_q(T-T(q))\) at a finite puncture. If
\(r_\infty=|\Pi_\infty|\), then the exact pole/differential ledger is

\[
\begin{aligned}
 &\sum_{p\in\Pi_\infty}e_p=\mu,\\
 &\sum_{p\in\Pi_\infty}(e_p-1)=\mu-r_\infty,\\
 &\sum_{q\in\Pi_f}(e_q-1)=2g(\bar C_c)-2+\mu+r_\infty,       \tag{3.3}\\
 &\operatorname{Poles}(dT)=\sum_{p\in\Pi_\infty}(e_p+1)p,
   \qquad \deg\operatorname{Poles}(dT)=\mu+r_\infty.
\end{aligned}
\]

Equation (3.3) is just Riemann--Hurwitz plus (3.2). It is exact and useful
for detecting a wrong pole book, but by itself it is an identity, not a
kill.

Chau proves that the universal plane Jacobian conjecture is equivalent to
the assertion that \(Q\) has only one pole on \(P=0\). At the individual-map
level, the one-pole hypothesis supplies the familiar one-place/degree
divisibility route to invertibility. Thus a successful sweep which forces
\(r_\infty=1\) for a Keller pair finishes the map; merely recovering
\(\sum e_p=\mu\) does not.

### 3.2 Sweep the tangent lines of the nonproperness curve

Assume \(F\) is not proper and let \(A_i\) be a component of its
nonproperness curve. On a smooth parametrized chart write

\[
 a(t)=(u(t),v(t)).
\]

Its tangent line is

\[
 L_t:\quad
 H_t(U,V)=c_t,qquad
 H_t=v'(t)U-u'(t)V,qquad
 c_t=v'(t)u(t)-u'(t)v(t).                                 \tag{3.4}
\]

Choose a complementary \(T_t\) over \(\mathbf C(t)\) so that
\(\det(H_t,T_t)=1\), and form the relative pullback

\[
 \mathcal C_i=
 \{(x,y,t):H_t(P(x,y),Q(x,y))=c_t\}.                       \tag{3.5}
\]

On every affine fiber, (3.2)--(3.3) apply. This is the exact plane
tangent-line family attached to \(F\).

There is a concrete local calculation at a dicritical boundary component.
After resolving \(F\), take analytic coordinates \((s,z)\) with boundary
\(z=0\), the dicritical mapping along \(a(s)\), and generic transverse
order \(m\):

\[
 \bar F(s,z)=a(s)+z^m b(s)+O(z^{m+1}).                     \tag{3.6}
\]

If \(L_t\) has contact \(\kappa=I_{a(t)}(A_i,L_t)\) and both leading
coefficients are nonzero, then the pulled-back line has initial local
equation

\[
 A(s-t)^\kappa+Bz^m+\text{higher terms}=0.                 \tag{3.7}
\]

The binomial Newton normalization of (3.7) has
\(g_0=\gcd(m,\kappa)\) branches. On each branch,
\(T_t-T_t(a(t))\) has ramification index \(m/g_0\), so the total local
ramification contribution is

\[
 g_0\left(\frac m{g_0}-1\right)=m-g_0.                    \tag{3.8}
\]

For a transverse line \(\kappa=1\), this is \(m-1\). For an ordinary
tangent \(\kappa=2\), an even \(m\) splits into two branches and lowers
the contribution to \(m-2\); an odd \(m\) stays one branch with
contribution \(m-1\). Equations (3.7)--(3.8) are the genuinely
dimension-two tangent-sweep datum: contact of two curves becomes an exact
gcd/parity constraint on escaping sheets.

### 3.3 What proof success would mean

Two possible successes have different strength.

- **Full pole removal:** prove that the algebraic inverse-coordinate
  functions on the normalization of (3.5) have no divisorial poles over
  the tangent locus. If this can be done for every component of \(A(F)\),
  sheets cannot escape, \(F\) is proper, and a proper étale endomorphism of
  \(\mathbf A^2_\mathbf C\) is an automorphism. This would prove JC2.
- **One-pole landing:** use (3.7)--(3.8), the boundary canonical divisor,
  and the global family to force \(r_\infty=1\) for one complementary
  coordinate. Chau's criterion then finishes that map. A theorem applying
  this to every hypothetical counterexample would also prove JC2.

No such theorem is presently available.

**CONJECTURE TS-L (tangent-pole landing).** For a nonproper plane Keller
map, the local tangent specializations (3.7)--(3.8), simultaneously over all
dicritical components and with the global pole divisor of \(T_t\), are
incompatible with (3.3) unless one target-linear pencil has one pole.

This is the exact missing bridge, not a proved lemma. It may be false:
Riemann--Hurwitz allows genus and other boundary components to absorb the
one-unit parity changes. A credible proof must control the *relative*
normalization (3.5), its genus jumps, and all pole sections; a single-fiber
count cannot do so.

---

## 4. Exact experiment: controls and residue A

### 4.1 Polynomial-automorphism positive control

Take

\[
 F_0=(P_0,Q_0)=(x,y+x^2),\qquad J(F_0)=1.
\]

On \(P_0=a\),

\[
 Q_0=y+a^2:\mathbf A^1_y\longrightarrow\mathbf A^1
\]

has degree one. On \(\mathbf P^1\), its exact ledger is

\[
 g=0,\quad D_\infty(Q_0)=P_\infty,\quad r_\infty=1,\quad
 \operatorname{Poles}(dQ_0)=2P_\infty,\quad R=0.
\]

Equations (3.3) give zero finite ramification. More generally, because
\(F_0\) is an automorphism, the pullback of every target affine line is an
\(\mathbf A^1\) and its complementary coordinate has one simple pole. The
line-sweep instrument accepts the positive control and reaches the one-pole
conclusion.

### 4.2 Residue-A input perimeter

The promoted shared genome in
[SHEET6-TEMPLATE.md](../SHEET6-TEMPLATE.md) and
[SHEET6-CLASSICAL.md](../SHEET6-CLASSICAL.md) gives, for the generic fiber
\(C_a=\{P=a\}\):

- \(\deg P=168\), \(\deg Q=252\), and geometric degree \(\mu=6\);
- two pole places \(P_1,P_2\), each with \(Q\)-pole order \(3\);
- no other \(Q\)-poles on \(\bar C_a\);
- finite-value B-side and x-side punctures, with their internal partitions
  and asymptotic values not fully pinned.

This is a formal boundary template, not an exhibited polynomial pair. The
experiment can therefore test only consequences determined by that genome.

### 4.3 Pole and differential count

The known vertical target line is \(P=a\), with complementary coordinate
\(T=Q\). Its pole divisor is

\[
 D_\infty(Q)=3P_1+3P_2,\qquad
 \deg D_\infty=6=\mu,\qquad r_\infty=2.                   \tag{4.1}
\]

The pole ramification is

\[
 (3-1)+(3-1)=4.                                           \tag{4.2}
\]

If \(g=g(\bar C_a)\), Riemann--Hurwitz gives total ramification
\(2g-2+12=2g+10\). Since there is no affine ramification, the finite
boundary punctures must contribute

\[
 (2g+10)-4=2g+6.                                          \tag{4.3}
\]

Meanwhile

\[
 \operatorname{Poles}(dQ)=4P_1+4P_2,qquad \deg=8,         \tag{4.4}
\]

and the canonical-degree check is

\[
 (2g+6)-8=2g-2.                                           \tag{4.5}
\]

Thus the whole sweep/pole count closes identically. It does not reveal an
obstruction.

The local product calculation also replays exactly. The contact sum for one
\(P_i\)-series is

\[
 \frac{597+624+504}{42}=\frac{575}{14},
\]

so

\[
 \operatorname{ord}_t(P_y)
 =42\left(-42+\frac{575}{14}\right)=-39.                  \tag{4.6}
\]

This equals the differential requirement
\(\operatorname{ord}_t(dx/dt)-\operatorname{ord}_t(dQ/dt)
=-43-(-4)=-39\). Independently, the \(189\) Q-series give

\[
 \operatorname{ord}_u Q
 =-63+\frac{171\cdot12+15\cdot32+3\cdot37}{42}
 =-\frac1{14},
\]

hence \(42\operatorname{ord}_uQ=-3\), recovering each order-three pole.

The repository replay

```text
python3 cases/classical_tests.py
```

returned **22 checks, 0 FAIL**, including (4.1)--(4.6), the exact symbolic
genus identity, and explicit feasible finite-puncture assignments. The
separate exact Laurent replay of Section 2 and the Singular saturation also
passed. No floating-point arithmetic entered any verdict.

### 4.4 Why the actual tangent experiment stops here

The residue-A genome supplies a single \(P=a\) fiber. A tangent line to an
asymptotic component requires the cross-fiber functions

\[
 a\longmapsto (a,c_p(a))
\]

on the B-side and their x-side analogues. To instantiate (3.4)--(3.8), one
needs at least

1. the component grouping of the punctures as \(a\) varies;
2. the functions \(c_p(a)\), or their first and second derivatives;
3. the transverse exponents \(m\) component by component; and
4. the genus and pole divisor of the *rotated tangent-line* pullback, which
   need not equal those of \(P=a\).

None is contained in the residue-A coefficient window. This agrees with
[AM-CHECK.md](../AM-CHECK.md): its 84 residual variables are fiber-internal
and carry no \(d/da\) datum. [SHEET6-CLASSICAL.md](../SHEET6-CLASSICAL.md)
establishes only that at least B-side and x-side component families must
exist. It does not give their equations.

Calling (4.1)--(4.5) a tangent sweep would therefore overstate the
experiment. It is the vertical-line pole count, and it returns a necessary
identity already built into the template. The genuine tangent run is
**not derivable from the supplied object**.

**CONJECTURE TS-A (algebraization/cross-fiber input).** The promoted
residue-A formal data algebraize to a pencil in which the finite punctures
can be grouped into algebraic sections or finite multisections
\(a\mapsto c_p(a)\), with transverse multiplicities equal to the finite
indices in (3.3).

This is not implied by nonempty finite-depth coefficient windows. It is
strictly downstream of the repository's missing char-zero germ,
all-depth, all-place, and algebraization bridges. Without TS-A, TS-L cannot
even be evaluated on residue A.

---

## 5. Adjudication

### 5.1 What is proved by this run

1. The normalized plane tangent sweep has an exact rational
   constant-Jacobian realization (2.3) of every generic degree \(d+1\).
2. Its direct one-pole polynomialization is impossible for every
   \(d\ge1\); the degree-two saturation is the unit ideal, with a live affine
   positive control.
3. Every plane Keller map has the exact target-line construction
   (3.1)--(3.3). Tangency to an actual nonproperness component has the local
   gcd/splitting law (3.7)--(3.8), under the displayed generic
   nondegeneracy hypotheses.
4. Residue A passes the only runnable pole count exactly:
   \(D_\infty(Q)=3P_1+3P_2\), finite ramification \(2g+6\), and no divisor
   deficit. The positive automorphism has the expected one simple pole.
5. A simple Vitushkin shape with one smooth exceptional \(\mathbf A^1\) is
   already excluded by Chau. Residue A avoids that theorem by requiring at
   least two asymptotic component families.

### 5.2 What is not proved

- The direct saturation does not classify arbitrary birational pole
  proliferation.
- The rational maps (2.3) are not polynomial Keller maps and do not disprove
  JC2.
- The line-pole identity (3.3) does not force one pole.
- No equation of \(A(F)\), no tangent line to it, and no relative pole
  divisor was obtained from residue A.
- Residue A itself is not known to arise from a characteristic-zero formal
  germ, still less from a polynomial Keller pair.
- TS-P, TS-L, and TS-A are **CONJECTURE**, not results.

### 5.3 Final classification

**As a necessary condition:** viable but not new. The exact line-pole ledger
is the Chau/Sigray/Riemann--Hurwitz instrument already present in the
repository. It correctly distinguishes the automorphism control
\([1]\) from residue A \([3,3]\), but the latter lies on the mandatory
multi-pole side of any hypothetical counterexample.

**As a landing ingredient:** potentially useful. Once a cross-fiber equation
for \(A(F)\) exists, (3.7)--(3.8) gives a cheap parity/splitting constraint
not visible in one fixed fiber. It could couple the B/x asymptotic components
to the pole book and is genuinely dimension-two.

**As a standalone proof or disproof route:** hollow at present. The disproof
ansatz dies before coefficient complexity begins; the proof ansatz reduces
to the unknown construction of \(A(F)\) and a conjectural relative
pole-removal theorem. There is no reason to launch a larger saturation on
residue-A tails. The next meaningful experiment is not another F4 window:
derive one algebraic cross-fiber branch \(c_p(a)\) (including \(c'_p,c''_p\))
and the tangent-line pole divisor. Until that datum exists, row 34 should be
ranked as a **conditional landing instrument, not an independent JC2 lane**.
