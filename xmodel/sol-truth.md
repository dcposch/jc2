# Truth test for the two terminal conjectures

**Date:** 2026-08-23

**Characteristic:** \(0\).

**Scope:** sol-bridge2, sol-pc, sol-ucda, the specified AUDIT entries, and
the banked D43 status needed to interpret the requested depth ladder.

**Tier key.** **EXACT** means a proved identity or direct arithmetic from the
accepted record. **KELLER CONTROL** means an actual constant-Jacobian example,
possibly outside the degree-minimal nonautomorphic target. **BOOK-RELATIVE**
means only the filed finite inventory. **MOD-\(p\)** and **INTERNAL** retain
their stated campaign scopes. **FORMAL** means exact tree/H1 arithmetic without
polynomial/Keller algebraization. **INFERENCE** and **VERDICT** are assessments,
not theorems.

## 0. Short verdict

| terminal statement | evidence on truth | calibrated read |
|---|---|---:|
| existence of some finite \(C\) in DIR(\(C\)) | **VERDICT: GENUINELY NEUTRAL, weakly pro-truth** | \(0.55\) (rough range \(0.35\)--\(0.70\)) |
| sharp claim \(C_{\rm sup}=4/3\) | **VERDICT: UNSUPPORTED** | \(0.20\) |
| A-SCALE | **VERDICT: WEAK EVIDENCE AGAINST** | \(0.40\) (rough range \(0.20\)--\(0.60\)) |

**VERDICT.** These are subjective, bank-relative epistemic probabilities,
not statistical estimates.

**VERDICT.** No banked configuration is an actual degree-minimal,
nonautomorphic Keller counterexample to either conjecture. There are, however,
two exact **FORMAL** counterexample directions: unbounded pole mass for DIR and
the non-removable type-\((2,3)\) carrier tower for A-SCALE. Only the latter is
currently accompanied by a substantial finite-window coefficient campaign.

**VERDICT.** The foundational reduction is coherent at its stated
book-relative tier: two independent terminal bounds remain. Truth testing does
not justify optimism that both bounds are true; A-SCALE has a live negative
signal, while DIR is presently under-sampled.

## 1. Q1: the DIR ratio

Put

\[
 R_P:=\frac{B\Delta_P}{\alpha\beta\mu_P}.
\]

**EXACT.** On a Keller pole branch \(\gamma\), the different/contact ledger gives

\[
 \Delta_\gamma=p_\gamma,\qquad
 \Delta_P=\sum_{\gamma\mid P,\,g(\gamma)=\infty}p_\gamma,\qquad
 R_P=\frac{B}{\alpha\beta\mu_P}\sum_{\gamma\mid P}p_\gamma.       \tag{1.1}
\]

**EXACT CONSEQUENCE.** Higher \(\mu_P\) lowers the ratio if the other data are
fixed.

**INFERENCE.** The dangerous direction is concentration of positive pole order
on a *light* root \(\mu_P/B\to0\), or growth of the pole inventory faster than
\(\mu_P/B\).

### 1.1 Filed two-pole residue A

**EXACT.** Here

\[
 (\alpha,\beta)=(2,3),\quad B=84,\quad \mu_P=63,\quad
 (p_1,p_2)=(3,3),\quad \Delta_P=6,
\]

so

\[
 \boxed{R_P=\frac{84\cdot6}{6\cdot63}=\frac43.}                  \tag{1.2}
\]

**EXACT.** The large branch invariants do not enlarge (1.2):

\[
 c(P_i)=2278,\qquad I_i=4656,\qquad \kappa_i=42,
\]

and the zero-slack cancellation is

\[
 2278+4656=(168-3)42+4,\qquad \Delta_{\gamma_i}=3.
\]

**INFERENCE.** Any universal DIR constant must satisfy \(C\ge4/3\), provided
this filed root lies in the final theorem's admissible class. One equality
case supplies no evidence that \(4/3\) is the supremum.

### 1.2 One root of high multiplicity

**EXACT ARITHMETIC.** If a single root has the full leading multiplicity
\(\mu=B\), then

\[
 R_P=\frac{\Delta_P}{\alpha\beta}.                                  \tag{1.3}
\]

For the same type-\((2,3)\), two-pole inventory \(\Delta_P=6\), (1.3) is
\(R_P=1\), below the filed \(4/3\). This is an inventory comparison, not an
existence assertion for a new residue-A Keller pair.

**KELLER CONTROL, outside the target reduced type.** The generalized Hénon
tower has

\[
 (\alpha,\beta)=(1,2),\quad B=\mu=\kappa,\quad \Delta_P=1,
\]

and hence

\[
 \boxed{R_P=\frac{\kappa}{2\kappa}=\frac12}                         \tag{1.4}
\]

for arbitrarily large \(\kappa=42\,2^r\). It is an actual Keller
automorphism, but orbit minimization reduces it to the identity and it never
realizes degree-minimal nonautomorphic residue A. It nevertheless shows that
large root/branch multiplicity alone is not a DIR counterexample signal.

### 1.3 Class-kill sanity control

**EXACT, NON-KELLER.** For

\[
 f=x^{B\alpha}+y,\qquad g=x^{B\beta}+y^{B\beta-1},
\]

there is one root with \(\mu=B\) and

\[
 \Delta_P=d(e-1)=\alpha\beta B^2-\alpha B.
\]

Therefore

\[
 \boxed{R_P=B^2-\frac{B}{\beta}\longrightarrow\infty.}             \tag{1.5}
\]

**EXACT.** This divergence is precisely the residual-Jacobian term. The
intrinsic polar excess is only \(1\), while
\(\operatorname{Fitt}_0(Q)\ne(z^M)\) and \(J(f,g)\notin k^*\). Thus (1.5)
is the required sanity divergence, not a DIR counterexample.

### 1.4 Is \(4/3\) the supremum?

**EXACT.** The available Keller identities give no rootwise upper bound for
(1.1). Adjunction controls only

\[
 \Delta_\infty-K_\infty=2-2g_C-s,
\]

with \(K_\infty\) uncontrolled, and semicontinuity bounds the displaced
intersection in the wrong direction. More pole branches increase
\(\Delta_P\); a smaller root weight increases \(B/\mu_P\). No accepted theorem
prevents either concentration.

**FORMAL counterexample signal.** The bounded-denominator/unbounded-mass
entry family has \((\alpha,\beta)=(2,3)\), fixed \(\kappa_P=6\), and
\(\mathcal E_{\rm MR}=b\to\infty\) through odd \(b\). Since

\[
 \mathcal E_{\rm MR}
 =\sum_P\frac{\Delta_P}{\alpha\beta}
 =\sum_P\frac{\mu_P}{B}R_P,\qquad
 \sum_P\frac{\mu_P}{B}=1,
\]

some root must have \(R_P\ge b\). This is unbounded DIR failure at exact
entry-arithmetic tier, but no stage has polynomial-origin Keller realization.

**VERDICT.** The bank contains no Keller-admissible unbounded ratio. It also
contains no basis for the sharp supremum \(4/3\). The observed ratios are
\(4/3\) (conditional filed residue-A root) and \(1/2\) (actual Hénon control);
the only computed polynomial divergence is non-Keller, while formal sheet
arithmetic permits divergence. Existence of
some finite \(C\) is therefore genuinely neutral, with a slight positive tilt
only because the known divergent polynomial mechanism is deleted exactly by
the Keller pure-minor identity.

**EXACT diagnostic.** Because \(\Delta_P\) is integral, finite DIR(\(C\)) forces
\(\Delta_P=0\) whenever \(B>C\alpha\beta\mu_P\).

**INFERENCE.** A decisive DIR counterexample search should therefore target
Keller-compatible roots with
\(\mu_P/B\to0\) and even one surviving pole end; high \(\mu_P\) is not the
dangerous axis.

## 2. Q2: A-SCALE versus the banked ladder

### 2.1 What the finite-\(td\) books say

**PROMOTED / BOOK-RELATIVE.** The \(td\le5\) filed books close with zero
survivors.

**PROMOTED / BOOK-RELATIVE.** At \(td=6\), the two-pole sector funnels to the
unique residue-A template. This is not a complete \(td=6\) theorem: four
single-pole \(r9/M2\) classes remain outside that two-pole statement.

**PROMOTED / BOOK-RELATIVE.** The filed \(td=7\) class-B/C panel is
17/17 tower-dead on its certified perimeter.

**PROMOTED / CONDITIONAL BOOK-RELATIVE.** The \(td=11\) 411-row audited layer
is tower-dead conditional on the seven fail-closed classes FC1--FC7; beyond-core,
refile, cap-free, and other named residues remain open.

**PROMOTED / LIST-RELATIVE.** The \(td=12\), type-\((3,5)\) book kills all 14
entry cells on the enumerated 74-candidate list. The \(u=1\), gap-\(1/3\)
NF-P candidate is explicitly unrefused, and other above-bound/type entries are
not covered.

**INFERENCE.** These books show strong pruning of *pole inventories at fixed
\(td\)*. A-SCALE concerns the orthogonal internal-carrier direction inside the
fixed \(td=6\), type-\((2,3)\), residue-A inventory. The \(td=7/11/12\) kills
therefore do not constitute a scale ceiling for residue A.

### 2.2 The carrier direction

**EXACT.** The filed scale is

\[
 (a,b)=(63,21),\quad B=a+b=84,\quad
 (\deg f,\deg g)=(168,252),\quad \kappa_i=42.                         \tag{2.1}
\]

**FORMAL.** Repeated \(q=2\), \(\ell=0\) carrier insertion preserves

\[
 td=6,\qquad \mathcal E_{\rm MR}=1,
\]

but gives

\[
 \kappa_i(r)=42\,2^r.                                                  \tag{2.2}
\]

Any polynomial realization must obey \(\kappa_i(r)\le2B_r\), hence

\[
 B_r\ge21\,2^r.                                                        \tag{2.3}
\]

Thus algebraization of infinitely many stages would directly refute
A-SCALE. Already \(r=3\) gives \(\kappa_i=336\) and forces \(B_r\ge168\),
beyond the filed \(B=84\).

**EXACT.** Type-\((2,3)\) cusp protection makes every rectangular pair
orbitwise degree-minimal at every positive scale. Consequently a polynomial
realization of (2.2) cannot be dismissed by the Hénon tail-removal mechanism;
it would be a genuinely non-removable carrier. This is evidence against the
*minimality proof strategy*, not proof that any Keller realization exists.

### 2.3 What D21--D43 actually tests

**MOD-\(p\), SCOPED.** The D21 fixed-scale residue-A fiber locus is nonempty;
the promoted D23 calculation leaves a dimension-11 survivor locus on the
named radical fiber at three primes. D25 is nonempty at both banked primes on
all 36 fibers, with 16 disjoint copies of \(\mathbb A^{14}\) per fiber.

**EXACT SCOPE.** These are deeper coefficient truncations of the filed
\(B=84\) template. They do not compute a new characteristic exponent,
\(\kappa_i\), or increasing Sigray base \(B\). Therefore

\[
 \text{D21}\to\text{D23}\to\text{D25 nonemptiness}
 \not\Rightarrow \text{unbounded A-SCALE failure}.                    \tag{2.4}
\]

**INTERNAL / UNREVIEWED, MOD-\(p\).** At D43 the commissioned 175-row
graph-row ideal is nonempty at both primes, with a witnessed smooth
dimension-81 component; its rung-\(\le38\) prefix is also nonempty. But those
witnesses fail 94 older D23/D25 reconstruction residuals. Hence the
identification with the true graph-preserving D43 survivor locus is false,
and that true family remains EMPTY/NONEMPTY unresolved.

**INTERNAL diagnostic.** Fully reconstructed point probes found 0/42 D25
points prolonging through the tested D43 equations. This is real pointwise
negative evidence, not an \(\mathbb A^{14}\)-family emptiness certificate.

**INTERNAL / SCOPED.** The existing delayed-loss ledger remains
\(\ell^+\ge37\) at the named completions. No new D43 survivor was eligible for
a floor measurement, so no D43 floor is reportable. The floor blocks the
Newton certificate at shallow depth—loss \(37\) requires depth at least
\(2\cdot37+1=75\)—but a large loss is not a kill and does not exclude a
singular extension.

**VERDICT.** The slogan “D21, D23, D25, D43 are all nonempty” is too strong.
D21--D25 are nonempty at their stated modular scopes; a D43
*overapproximation* is nonempty; the true D43 survivor family is unresolved.
The bank therefore neither confines residue A to bounded scale nor realizes
an unbounded-scale tower.

**VERDICT.** Evidence for A-SCALE is weakly negative. The negative signal is
the conjunction of (i) the exact formal tower (2.2), (ii) the scale lower
bound (2.3), (iii) automatic type-\((2,3)\) orbit minimality, and (iv) survival
of large modular fixed-scale families through D25. The counterweight is
substantial: no formal germ, characteristic-zero germ, algebraic branch, or
nonautomorphic polynomial Keller pair is banked; D43 has pointwise
obstructions and no true-family verdict. This warrants a live counterexample
signal, not a candidate counterexample map.

## 3. Q3: leads and next computation

**VERDICT: DIR.** No live Keller counterexample lead is banked. The sharp
constant \(4/3\) should not be promoted. The precise negative target is a
sequence of pure-minor/Keller boundary roots with

\[
 \frac{\mu_P}{B}\to0,\qquad \Delta_P\ge1,
\]

or, more generally, \(R_P\to\infty\). A rootwise census of every filed
admissible inventory—recording
\((B,\alpha,\beta,\mu_P,\sum p_\gamma)\)—is the cheapest direct test;
neither conductor nor \(\kappa\) is a useful proxy.

**VERDICT: A-SCALE.** The live lead is precisely the non-removable
type-\((2,3)\), \(q=2\) carrier tower

\[
 \kappa_i(r)=42\,2^r,\qquad B_r\ge21\,2^r.
\]

The next discriminating compute target is the **fully reconstructed D43
family ideal**, with both the older D23/D25 reconstruction graph and the
rung-26--42 graph imposed simultaneously, decided family-wide at both banked
primes. If nonempty, extract a witness passing the full survivor gate and then
measure \(\ell^+\); the present floor says D75, not another shallow window, is
the first possible Newton-certification depth for the named completions. If
empty, that is a fixed-\(B=84\) depth kill, not yet A-SCALE.

**FINAL VERDICT.** The book-relative program remains a coherent conditional
reduction to two bounds. DIR has no actual counterexample signal but no
credible sharp-supremum evidence. A-SCALE has the campaign's only live
counterexample-tower signal, still separated from a JC2 counterexample by
inverse-limit existence, characteristic-zero lifting, algebraization,
globalization, and polynomial Keller realization.
