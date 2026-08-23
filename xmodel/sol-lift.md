# The residue-A algebraization gate

**Date:** 2026-08-23

**Characteristic target:** \(0\)

**Scope:** fixed \(B=84\), residue A, representative fiber a00pp, and the
formal \(q=2,\ w=2\) carrier direction.

**Tier key.** **MOD-\(p\) EXACT** is certified only over the two banked finite
fields. **KNOWN THEOREM** is an implication with stated hypotheses. **OPEN**
means that a required certificate or construction is absent. **ROUTE
OBSTRUCTED** means that a proposed method is known to be insufficient; it
does not mean that the carrier is impossible.

The D43 statement in sol-truth.md is stale: its promotion warnings remain
valid, but its unresolved-family verdict is superseded by sol-d43full.md.

## 0. Verdict

\[
\boxed{
\begin{gathered}
X^{\rm full}_{43}(\mathbf F_{105337})\ne\varnothing,\qquad
X^{\rm full}_{43}(\mathbf F_{105673})\ne\varnothing,\\
X^{\rm full}_{43}(\mathbf C)\ne\varnothing\quad\textbf{OPEN},\\
\text{all-depth germ, algebraic branch, and polynomial Keller pair}
\quad\textbf{OPEN}.
\end{gathered}}
\]

There is no banked local obstruction to lifting either witness, but there is
also no smooth horizontal-point certificate. The ranks \(14\) and \(111\)
are smooth-ish evidence, not a Jacobian-criterion proof.

The cheapest decisive promotion is **(b): certify a \(p\)-adic/characteristic-
zero lift of one \(B=84\) witness**. Build the common integral reconstruction
scheme, certify a standard-smooth neighborhood at one modular point, and use
Hensel/formal smoothness. A \(B=168\) modular test probes scale while leaving
the same arithmetic gate unresolved.

The hardest stage is **globalization plus polynomial Keller realization**:
all local charts must be expansions of the same two polynomials, and the
global identity \(J(f,g)\in\mathbf C^*\) must hold. No Artin,
Newton--Puiseux, or Abhyankar--Moh theorem performs that promotion.

## 1. Q1: modular point to characteristic zero

### 1.1 What D43 proves

**MOD-\(p\) EXACT.** At each prime there is a \(184\)-coordinate point killing
all \(218=34+95+89\) generators and all survivor/floor gates. After choosing
\(W_1,W_2\), the parked \(28\)-coordinate component has an explicit
\(\mathbb A^{14}\) parametrization and parked Jacobian rank \(14\). With that
parked point fixed, the \(184\) graph rows have rank \(111\) in the \(156\)
graph coordinates.

The block form of the full Jacobian gives only

\[
\operatorname{rank}J_{\rm full}(\bar x)\ge14+111=125,\qquad
\dim T_{\bar x}X_{43}^{\rm full}\le184-125=59.                 \tag{1.1}
\]

No equality is certified. The record does not give the local Krull
dimension, the height of the localized ideal, or local generators matching
the Jacobian rank. The separate floor window rank \(125\) is not identified
as the full scheme Jacobian and cannot fill this gap.

The completely linear \(101\)-variable slice basis also proves no unsliced
smoothness: nonpivot coordinates were fixed for witness search. Full replay
proves membership, not transversality or local dimension.

Thus “smooth point of the characteristic-zero ideal” is not yet the right
phrase: there is no characteristic-zero point. The right question is whether
\(\bar x\) is a point where a common integral model is **smooth over the
\(p\)-adic base**.

### 1.2 Exact local lifting criterion

First define a common finite-type model

\[
X=\operatorname{Spec}R[z_1,\ldots,z_{184}]/I,\qquad
R=\mathbf Z[1/N]\ \text{or a localized number ring},          \tag{1.2}
\]

whose reductions are the tested systems. The current artifacts are
prime-specific reduced checkpoints and modular solver files. Matching row
counts, supports, and gates does not certify (1.2). The clean model should
retain \(W_i,uW_i\) and their radical/inverse equations; arbitrary integer
representatives of modular root values are not a characteristic-zero model.
Once the radical right-hand sides are defined integrally, the chosen roots
themselves are locally harmless: \(p\) is odd, \(W_i\ne0\), and
\(\partial(W_i^4-A_i)/\partial W_i=4W_i^3\) is a unit modulo \(p\).

At a prime \(\mathfrak p\mid p\), a cheapest positive certificate is a
**standard-smooth presentation near \(\bar x\)**:

1. Compute the full relative Jacobian rank \(c\) at \(\bar x\).
2. Find \(c\) local generators and \(c\) variables with a \(c\times c\)
   Jacobian minor nonzero modulo \(\mathfrak p\).
3. After localizing at that minor, certify that those \(c\) equations
   generate the same local ideal as all \(218\) rows and that the local model
   is \(\mathfrak p\)-flat. Equivalently, provide the required local
   complete-intersection/dimension and flatness certificates.

Then \(X\to\operatorname{Spec}R\) is smooth at \(\bar x\). For a
finite-presentation morphism, smoothness is equivalent to formal smoothness;
therefore \(\bar x\) lifts compatibly through every
\(R/\mathfrak p^n\). This gives an
\(R_{\mathfrak p}^{\wedge}\)-point and hence characteristic-zero
nonemptiness. This is the applicable Hensel theorem; see the
[infinitesimal lifting criterion](https://stacks.math.columbia.edu/tag/02H6).

Two cautions are load-bearing.

- Positive dimension is **not** an obstruction. A smooth
  positive-dimensional point is favorable: lift free coordinates and solve
  for pivots.
- Singularity does not prove nonliftability; it only removes the automatic
  Hensel implication. Conversely, a point can be smooth on the special fiber
  but lie on a vertical component. Relative smoothness/flatness excludes
  that.

### 1.3 Cheapest obstruction screen and decisive tests

After (1.2) is available, choose integral lifts \(x_1\) of \(\bar x\). The
first correction equation for a lift modulo \(p^2\) is

\[
J(\bar x)\delta=-\frac{F(x_1)}p\pmod p.                         \tag{1.3}
\]

Failure of (1.3), using all \(218\) rows and the integral syzygies, is a real
first-order obstruction to lifting **that point**. It does not prove the
whole characteristic-zero family empty. Success proves only a \(p^2\)-lift
unless formal smoothness controls every later step.

| certificate | conclusion | status |
|---|---|---|
| Solve (1.3) | This witness reaches \(p^2\) | **CHEAP SCREEN; NOT DECISIVE POSITIVELY** |
| Standard-smooth certificate at one prime | Compatible lifts to all \(p^n\), hence \(X_{43}(\mathbf C)\ne\varnothing\) | **CHEAPEST DECISIVE POSITIVE TEST** |
| Exact \(\overline{\mathbf Q}\)-point and replay | \(X_{43}(\mathbf C)\ne\varnothing\) | **DECISIVE; LIKELY DEARER** |
| Rational Nullstellensatz certificate \(1\in I\otimes\mathbf Q\) | \(X_{43}(\mathbf C)=\varnothing\) | **DECISIVE NEGATIVE FOR ALL FIXED-D43 COMPONENTS** |

### 1.4 Why two primes and CRT do not promote the result

If \(I\otimes\mathbf Q=(1)\), clearing denominators gives some nonzero
integer \(M\in I\). Modular nonemptiness can occur at primes dividing such a
bad integer. Two large primes are good robustness evidence, but without an
effective bound excluding both as bad, they do not prove a horizontal
component.

CRT combines residues; it does not identify points on two fibers. Rational
reconstruction would require a common integral ideal, a matched component,
height/denominator bounds, and a reason the point is rational rather than
algebraic or \(p\)-adic. None is banked.

One actual \(\mathbf Z_p\)-point is enough: it makes
\(I\otimes\mathbf Q\) proper, so the finite-type \(\mathbf Q\)-scheme and its
base change to \(\mathbf C\) are nonempty. Finite CRT data alone do not.

## 2. Q2: characteristic-zero jet to polynomial Keller pair

| stage | required object/certificate | status |
|---:|---|---|
| 0 | Full D43 witness at \(p=105337,105673\) | **MOD-\(p\) EXACT / DONE** |
| 1 | Common integral/number-ring reconstruction scheme with the tested reductions | **OPEN / CERTIFICATE ABSENT** |
| 2 | One characteristic-zero point of the finite D43 scheme | **OPEN**; relative smoothness settles it by a **KNOWN THEOREM** |
| 3 | Compatible points at every depth \(D\), not independently chosen nonempty \(X_D\) | **OPEN** |
| 4 | Inverse-limit coefficients satisfying every reconstruction, no-log, primitivity, and survivor equation: a formal Puiseux germ | **OPEN** |
| 5 | The prescribed formal series are convergent and algebraic over the appropriate rational-function field | **OPEN FOR THIS CARRIER** |
| 6 | All pole charts, trunk/merge, conjugates, contacts, and the \(w=2\) quotient glue on one compactification, with no extra places | **OPEN** |
| 7 | The global data arise from the same \(f,g\in\mathbf C[x,y]\), with the Sigray rectangles and every coefficient of \(J(f,g)-j\) zero for some \(j\ne0\) | **OPEN; HARDEST** |
| 8 | Such pairs exist at unbounded carrier scale, e.g. \(\kappa_i(r)=42\,2^r\), \(B_r\to\infty\) | **OPEN**; required to refute A-SCALE |

### 2.1 Inverse-limit survival

D43 is one finite jet. It says neither that
\(X_{45},X_{47},\ldots\) are nonempty nor that there is a chain

\[
\cdots\longrightarrow x_{47}\longrightarrow x_{45}
\longrightarrow x_{43}.                                      \tag{2.1}
\]

If the systems are proved nested, all finite subsystems are solvable over
characteristic zero, and coefficient-field issues are controlled, algebraic
compactness can provide a formal solution; an explicit inverse-limit point is
the direct certificate. Formal smoothness of every truncation transition is
another known sufficient mechanism. None is banked.

The bound \(\ell^+\ge37\) says D75 is the first possible depth for the named
Newton certification. It is neither an extension theorem nor a kill.

### 2.2 Convergence and algebraicity

Any finite Puiseux jet with finite denominator can be completed to a finite
\(t\)-parametrization and eliminated to give **some** algebraic plane branch
with that jet. Admissible finite plane-branch topological types are likewise
locally realizable. This does not preserve the all-depth coefficients, second
pole, or Keller identity.

For an all-depth series,

\[
\text{formal}\not\Rightarrow\text{convergent}
\not\Rightarrow\text{algebraic}.                              \tag{2.2}
\]

Newton--Puiseux says that a complex algebraic plane branch has a convergent
Puiseux expansion. It does not make an arbitrary formal expansion algebraic.
Thus algebraicity would settle convergence here, but neither is banked.

Artin approximation is a **KNOWN THEOREM but not this promotion**. For a
formal solution of a suitable finite system, the analytic version gives
convergent approximants and the algebraic version gives algebraic-power-series
approximants, at each prescribed finite order. It need not make the given
formal series convergent, give one solution agreeing at all orders, or impose
global polynomiality. See Artin's
[analytic-approximation paper](https://eudml.org/doc/141922).

### 2.3 Passport versus carrier

The residual quotient

\[
\beta(u)=\frac{u(u-2/3)^3}{(u^2-u+1/6)^2}
\]

is an explicit rational map with passport
\(\{(3,1),(2,2),(3,1)\}\): **EXACT / DONE**. It supplies no carrier
algebraization because

\[
\frac{(C^4h_1)^3}{(C^3f)^4}=\frac{h_1^3}{f^4}.                 \tag{2.3}
\]

The quotient forgets characteristic factors of \(C\); the banked factor \(7\)
is absent from the passport. Belyi/Riemann existence solves the residual
cover, not the common-carrier realization.

### 2.4 Global compatibility and polynomiality

Even algebraic local branches must arise simultaneously from one global
object. Required compatibility includes:

- one normalization and one infinity divisor;
- both poles, shared characteristic trunk, merge, conjugates, and contacts;
- all genus, conductor, intersection, and pole-divisor ledgers;
- no extra finite asymptotic punctures or infinity branches;
- descent of every local coefficient choice to the same global \(f,g\).

Polynomiality then requires the functions to be regular on \(\mathbb A^2\),
to have only the prescribed poles at infinity, and to have finite Sigray
support. Finally \(J(f,g)=j\) must be replayed as a global polynomial
identity, not inferred from finitely many branch valuations.

No Newton-polygon realization theorem gives this simultaneous two-function
Keller realization. The
[Abhyankar--Moh theorem](https://doi.org/10.1515/crll.1975.276.148)
concerns an embedded affine line; residue A is multi-place, and the theorem
neither glues the two-pole tree nor constructs a second polynomial with
constant Jacobian. Its use here is **ROUTE OBSTRUCTED / WRONG HYPOTHESES**,
not an obstruction to the carrier.

This is the hardest gate. A positive \(B=84\) realization in the intended
nonproper class would already be a plane-Jacobian-Conjecture counterexample;
there is no routine theorem expected to manufacture it from local data.

## 3. Q3: obstruction, verdict, and next move

### 3.1 Candidate obstructions

| candidate | theorem/certificate needed | status |
|---|---|---|
| Vertical or obstructed modular component | Failure of (1.3), or proof every special-fiber component is vertical | **UNTESTED**; pointwise failure is not family-wide |
| Eventual depth death | Unit ideal at some finite \(D\), or failure of every compatible inverse-limit branch | **OPEN**; D43 survives |
| Nonalgebraic formal coefficients | Finite-determinacy, recurrence, or differential-algebraic theorem excluding every algebraic Puiseux completion | **NO SUCH THEOREM BANKED** |
| **GCT-A** | Every polynomial-origin excess carrier globalizes to a Hénon coordinate tail; minimality then removes it and gives \(K_A=42\) | **CONJECTURAL** |
| **K2C / A-SCALE** | Polynomial origin plus the pure boundary Jacobian identity bounds internal characteristic products or \(B\) | **CONJECTURAL** |
| **A-CONDUCTOR** | Scale-independent upper bound on residue-A pole conductors | **CONJECTURAL**; \(c(P_i)\ge2(\kappa_i-1)\) has the wrong sign |

GCT-A is the sharpest named algebraization obstruction: with minimality it
forbids every excess \(q=2\) insertion. But sol-ucda.md explains why it is
new. Type-\((2,3)\) cusp protection makes every rectangular realization
orbitwise degree-minimal at every scale; a local approximate root is not a
global coordinate tail. Neither Abhyankar--Moh nor leading-form automorphism
calculus supplies GCT-A.

Other standard ledgers give no obstruction:

- \(\operatorname{ord}_t f_y=3-\kappa_i\) remains compatible as scale grows;
- the boundary cancellation order \(5B-2\) grows with \(B\);
- the genus/conductor budget grows with polynomial degree;
- the Belyi quotient cancels the carrier exactly.

These remove easy obstruction proposals. They are not evidence that a
polynomial Keller pair exists.

### 3.2 Honest verdict

\[
\boxed{\textbf{No known obstruction and no known construction.}}
\]

At finite jet and fixed \(B\), the carrier is robust: it survives the fully
reconstructed D43 system at two primes and passes independent replay. Similar
rank profiles mildly disfavor a one-prime accident. They do not decide
horizontal lifting, all-depth survival, algebraicity, or polynomial origin.

The carrier is therefore **modularly viable**, not demonstrably
**algebraizable**. There is no calibrated basis for optimism or pessimism at
the polynomial Keller tier.

### 3.3 Single next step

Choose **(b): characteristic-zero lift of a \(B=84\) witness**:

1. Re-emit all \(218\) equations over a common \(R\), or directly over
   \(\mathbf Z_p\), retaining the radical variables; audit the reduction.
2. Run the all-row \(p^2\) correction test (1.3).
3. Compute the full Jacobian rank and local dimension at the witness.
4. Emit a nonzero minor plus localized-generation/flatness certificate.

If step 4 succeeds at either prime, Hensel gives the first certified
characteristic-zero D43 point. If step 2 fails, it exposes an immediate local
obstruction worth deciding family-wide. If the point is singular but reaches
\(p^2\), search its modular component for a relatively smooth point before
deep singular deformation theory.

Option (a), the \(B=168,\ \kappa=84\) modular test, is the next **scale**
test, not the next **algebraization** test. Option (c) is ultimately decisive,
but GCT-A/K2C/A-CONDUCTOR currently name research programs rather than bounded
certificate computations.

\[
\boxed{
\text{D43 mod }p
\xrightarrow[\textbf{next}]{\text{relative smoothness/Hensel}}
\text{D43 char }0
\xrightarrow[\textbf{open}]{\varprojlim D}
\text{formal germ}
\xrightarrow[\textbf{open}]{\text{algebraize and glue}}
\text{global data}
\xrightarrow[\textbf{hardest/open}]{\text{polynomial Keller}}
(f,g).}
\]
