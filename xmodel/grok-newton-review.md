# Hostile review: sol-newton-lemma.md (filtered Euler/Ore Newton)

Reviewer: Grok 4.6 (hostile referee, verdict tier). Date: 2026-08-19.
Target: `xmodel/sol-newton-lemma.md` (the claimed proof of CONJECTURE
E-HENSEL, Route B).
Cross-checks: `DEPTH-STAB.md` §§2–3; `xmodel/sol-round5.md` §§1.1–1.3
and the E-HENSEL box; `xmodel/sol-round6.md` §1; `SHEET6-DIRECTIONB.md`
§8.S7 and the 8.S7-ADDENDUM.
Method: line-by-line attack on the contraction, the definition of \(e\),
the Euler/\(\sigma=0\) remainder, the characteristic-\(p\) arithmetic,
boundary cases, and the Tougeron reduction. No Singular, no msolve, no
replay of `valuation_e2.py`, no other repo file modified, no git.

The load-bearing claim is the boxed inequality (N) at
`sol-newton-lemma.md:12-13` together with the sentence at lines 5–7:
a fixed-linearization contraction, over an arbitrary field including
characteristic \(p\), lifts a residual of global \(t\)-order \(D\) as
soon as \(D\ge 2e+1\), where \(e\) is the loss of an exact causal right
section of the Euler/Ore linearization, without a nonlinear conjugation
that eliminates \(\Theta\).

---

## Verdict

**CONFIRMED — abstract theorem. Not REFUTED. Residual GAPS do not
flip the lemma and do not certify any germ.**

Theorem 3.1, Corollary 3.2, Lemma 4.1, Lemma 4.2 (finite Euler-
differential polynomials), Lemma 2.1, Remark 2.2, and Proposition 3.3
survive a hostile replay. CONJECTURE E-HENSEL, in the exact sense
stated in `sol-round5.md:171-175` (Route B: completed-ideal bridge +
delayed-parametrix loss \(\le e\) + quadratic remainder \(\Rightarrow\)
lifting for \(D\ge 2e+1\)), is closed as an abstract analysis lemma.
Euler terms do not force a conjugation: they live in \(L\), which is
allowed to be only \(k\)-linear, and they do not raise the nonlinear
filtration loss above \(\sigma=0\).

What this file does **not** earn, and its own banner already withholds:

- any promoted \(e^+\) at any point;
- any D23/D25 formal germ;
- CYCLIC-30, BRIDGE-30, PARAM-30, or FILTER-30;
- a legal all-depth completion of any banked witness.

Those remain application gates. Theorem 6.1 is the correct conditional
packaging. The germ-certification *mechanism* for a D25 survivor is now
in place; no survivor is carried through it by this document.

**Tier deserved: BANKED analysis lemma, first-lemma tier, both
characteristics. Not a promotion. Not a DEPTH \(e\). Not a germ.**

---

## Claim chain (attack results)

| Claim | Verdict | Severity if it had failed |
|---|---|---|
| Thm 3.1 contraction, filtration preserved | CONFIRMED | fatal |
| Euler terms handled without conjugation (\(\sigma=0\)) | CONFIRMED | fatal |
| \(e=\ell(L)\) well-defined; matches round-6 30×30 | CONFIRMED | fatal |
| Char \(p\): no hidden divisibility in the Newton step | CONFIRMED | fatal |
| \(e=\infty\) / missing section fail-closed | CONFIRMED | high |
| \(D=2e\) insufficient (Prop 3.3) | CONFIRMED | medium (sharpness) |
| Reduces to Tougeron \(2e+1\) when Euler terms vanish | CONFIRMED | high (DEPTH-STAB consistency) |
| Inverse/unit two-point remainder written in full | GAPS | medium for FILTER-30 discharge only |
| Any current \(e^+\) or D25 germ | not claimed; correctly withheld | — |

---

## 1. The contraction (Theorem 3.1)

Attacked lines: `sol-newton-lemma.md:289-384`.

### 1.1 Domain, definedness, self-map

\(q=D-e\). Hypothesis (3.4) gives \(q-e-\sigma\ge 1\), hence
\(q\ge e+\sigma+1\ge 1\). The ball \(B=F^qX\) therefore sits inside
the stated domain \(s+F^1X\). Completeness of \(B\) is inherited from
\(X\) (closed subspace of a complete filtered space).

\(T(h)=-S(A+N(h))\) is defined on \(B\): \(A\in F^DY=F^{q+e}Y\subseteq
F^eY\), and \(N(h)\in F^{2q-\sigma}Y\subseteq F^{q+e}Y\) once
\(2q-\sigma\ge q+e\), i.e. \(q\ge e+\sigma\), which is weaker than
what (3.4) already gives. The parenthetical “by \(q\ge e+\sigma\)” at
line 352 is therefore true and slightly slack; it is not an equality
case the proof relies on for the Cauchy step.

The section bound (2.3) then puts \(T(h)\in F^qX\). Self-map: CONFIRMED.

### 1.2 Is the filtration genuinely preserved?

The two-point estimate (3.8) is the only load-bearing arithmetic:

\[
\nu_X\bigl(T(h)-T(h')\bigr)
\ge (q+m-\sigma)-e
= m+(D-2e-\sigma).
\]

The identification \(c:=D-2e-\sigma\) is an equality, not an
inequality. Under (3.4) one has \(c\ge 1\), so each application of
\(T\) strictly raises the order of consecutive differences. There is
no leakage of filtration: \(S\) is applied only to elements of
\(F^{q+e}Y\subseteq F^eY\), where \(LS=\mathrm{id}\) and the delay
bound is the one hypothesized.

The first difference \(h_1-h_0=T(0)=-S(A)\) uses \(N(0)=0\) and the
self-map, not (3.8). Subsequent differences use (3.8) with
\(m=q+(j-1)c\ge q\). Induction for (3.9) closes. The sequence is
Cauchy because \(q+jc\to\infty\). Completeness supplies
\(h_\infty\in F^qX=F^{D-e}X\).

Passing to the limit uses continuity of \(T\) on \(B\), which follows
from (3.8) (or, equivalently, continuity of \(N\) from (3.3) and of
\(S\) from (2.3)). Then \(LS=\mathrm{id}_{F^eY}\) applies because
\(A+N(h_\infty)\in F^{q+e}Y\subseteq F^eY\). The identity
\(Lh_\infty=-A-N(h_\infty)\) is (3.5) by definition of \(N\).

No step uses \(k[[t]]\)-linearity of \(L\), invertibility of an
integer, a binomial coefficient, or a derivative at the Newton
iterates. Fixed-linearization is essential to the argument and is
honestly advertised.

CONFIRMED. The filtration is genuinely preserved.

### 1.3 Attacks that do not land

- **Need \(S\) on all of \(F^eY\), while the iteration only probes
  \(F^DY\).** True as a remark: every argument of \(S\) that appears
  has order \(\ge D\). The hypothesis is stronger than the Newton
  step uses. That does not break the implication as stated; it makes
  PARAM-30 slightly more expensive than a single-depth lift requires.
  Nit, not a gap in 3.1.
- **Banach contraction on a real metric.** Not used. The proof is the
  standard ultrametric/filtered Cauchy estimate. Characteristic-free.
- **Uniqueness of \(h_\infty\).** Not claimed. Germ existence does not
  need it.
- **\(F^n\) decreasing.** Used, and stated at lines 117–119.

---

## 2. Euler terms without conjugation (Lemmas 4.1–4.2)

Attacked lines: `sol-newton-lemma.md:426-524`, plus the Route B
claim at lines 5–7.

Round 5 (`sol-round5.md:171-175`) offered two headlines: (i) a
nonlinear change of source coordinates whose derivative eliminates
every \(\Theta\) term, then ordinary Smith/Tougeron; (ii) a filtered
differential Newton lemma. It explicitly warned that a row/column
conjugation of the linearization alone is not (i). Sol takes (ii).

### 2.1 Where the Euler terms live

They live in \(L=D\mathcal H_s\), via (1.6a) and (4.3). Theorem 3.1
never needs \(L\) to be \(R\)-linear. The replacement for the
adjugate is the causal section (2.2)–(2.3). That is the sense in
which conjugation is unnecessary: one does not have to manufacture
an \(R\)-matrix in order to run Hensel.

### 2.2 Do they spoil the remainder?

Lemma 4.1: \(\theta(t^nf)=t^n(nf+\theta f)\). In characteristic
\(p\), the scalar \(n\) may vanish; the right-hand side then has
order \(>n\) or \(=\infty\), never \(<n\). After the residue split,
(4.3) is an identity of formal series, including when
\(r+6j\equiv 0\pmod{p}\). Order-preserving, all \(j\ge 0\):
\(\theta^j(t^nR)\subseteq t^nR\). CONFIRMED.

Lemma 4.2, polynomial case: the remainder of a monomial in the slots
\(\{x_i,\theta^j x_i\}\) is a sum of products of at least two
variation factors. Each factor of \(\theta^jh_i\) stays in \(F^a\)
by 4.1; products add valuations; coefficients have nonnegative
order. This is (3.2) with \(\sigma=0\).

The two-point estimate (3.3) is proved by telescoping, not by
polarization. That is the load-bearing characteristic-\(p\) choice:
polarization would divide by \(2\) (and more generally by
factorials). Telescoping a product of \(r\ge 2\) factors yields one
factor \(\theta^j(h_i-h_i')\in F^m\) and at least one remaining
variation factor of order \(\ge a\). No \(1/n!\). CONFIRMED.

\(\eta\)-differentiation: linear on finitely many component labels,
does not lower \(t\)-order. In characteristic \(p\) the factor \(a\)
in \(\partial_\eta(\eta^a)\) may vanish; that can only kill a
component. CONFIRMED as an order statement.

### 2.3 Restricted series, and the inverse paragraph

The paragraph at lines 475–481 is the correct restricted-power-series
condition (finitely many monomials modulo every \(F^N\), uniformly
for the value, the linear part, and the two-point remainder) and the
correct reason the estimates pass to the limit (\(F^N\) is closed).
It is brief but not circular. FILTER-30 is defined to be the audit
that the repository formula is of this type. That is an application
gate, not a hole in 4.2.

**GAPS, severity medium for FILTER-30 discharge, not for Theorem
3.1.** Two writeup defects, neither of which produces a
counterexample:

1. The statement of Lemma 4.2 (line 456) says “Localizations at
   fixed chart units are allowed.” The proof through line 473 does
   not treat inversion; localization is postponed to the next
   paragraph. The lemma as boxed slightly overclaims relative to
   its displayed proof.
2. The source-dependent inverse argument (lines 483–504) proves
   (3.2) for \(U^{-1}\) by geometric series, which is
   characteristic-free (\(\sum(-1)^k\Delta^k\), no factorials, valid
   once \(\nu(\Delta)\ge 1\)). It then says “the same proof applies”
   for (3.3). The two-point remainder of inversion is true in this
   setting — the identity
   \(N_R(h)=-(R(h)-R(0))\,DU(h)\,R(0)-R(h)N_U(h)R(0)\) gives
   (3.2), and a further telescope gives (3.3) — but that telescope
   is not written. FILTER-30’s escape hatch (“equivalently, the
   certificate may directly prove (3.2)–(3.3) with \(\sigma=0\)”)
   makes Theorem 6.1 still well-posed. A consumer who thinks Lemma
   4.2’s boxed statement already includes source-dependent
   inverses is over-reading.

The actual map (1.6) is polynomial in \(\Phi,\Gamma\) and their
Euler/\(\eta\) derivatives. Whether \(\Phi,\Gamma\) themselves are
restricted Euler-differential expressions with unit localizations is
exactly FILTER-30. Sol does not smuggle that audit into the Newton
lemma. Honest.

---

## 3. Definition of \(e\)

Attacked lines: `sol-newton-lemma.md:200-282` and §8.

### 3.1 Well-defined

(2.1) is the minimum of a subset of \(\{0,1,2,\ldots\}\cup\{\infty\}\).
The set does not depend on a choice of section. If the set is empty,
\(\ell(L)=\infty\) by definition (line 209). Unique. CONFIRMED.

Lemma 2.1: delayed inclusion for all \(n\ge 0\) is equivalent to
existence of some continuous \(k\)-linear causal right section of
that loss. Direction \(2\Rightarrow 1\) is immediate. Direction
\(1\Rightarrow 2\) uses the homogeneous splitting of the global
\(t\)-filtration on a finite sum of shifted one-variable series
spaces. Each \(Y[m]\) is finite-dimensional (at most 30 dimensions
for \(Y^+\)); a right inverse on each degree exists by linear
algebra over any field; the series \(\sum_m S_m y_m\) converges
because the \(m\)-th term lies in \(F^{m-e}X\); continuity of \(L\)
passes the sum through. No characteristic restriction. CONFIRMED
for the spaces to which it is applied.

The section so constructed is not unique and need not be
\(k[[u]]\)-linear. Theorem 3.1 does not need either.

A certified loss \(e\) is any proved upper bound on \(\ell(L)\), not
necessarily the minimum (lines 265–266). That is the right object
for Newton: a possibly pessimistic \(e\) only makes \(D\ge 2e+1\)
harder.

### 3.2 Computable?

Not from a finite rank profile. Sol says so, repeatedly
(lines 258–263, 808, 859–860). \(\ell(L)\) is a \(\forall n\)
statement. A machine certificate needs an Ore identity or a finite-
state causal recurrence with proved transient and boundary
identities. That matches `sol-round5.md:124-134` item 3–4 and
`sol-round6.md:69-73`. CONFIRMED as a definition; no general
algorithm is claimed; PARAM-30 is the existence/certificate gate.

### 3.3 Match to the corrected 30×30 object of sol-round6 §1

| object | sol-newton-lemma | sol-round6 §1 |
|---|---|---|
| inputs | 30 streams, family-then-residue order (1.0) | same |
| \(r_\rho\) | \(6+\rho\) (\(\rho\ne 4\)), \(r_4=16\), \(\sum r_q=288\) | same |
| outputs | \(H_0,\ldots,H_{29}\), \(s_{29}=36\), \(\sum s_a=276\) | same |
| free stream | none | none |
| operator | one \(L_s^+\in\mathrm{Mat}_{30}(k[[u]]\langle\Theta\rangle)\) | same |
| \(\ell^+\) | (2.1) | identical formula |
| index diagnostic | \((e^+)^{\mathrm{idx}}=6d^+-12\) | same, tag (1) |
| 295 | “irrelevant to the corrected object” | WITHDRAWN |

The \(s_a\) override \(s_{28}=16\) (the formula \(6+2((a+1)\bmod 3)\)
would have given 10) is the Round-5 exception, retained. Sum check:
\(a=0..26\) contributes nine of each of \(\{6,8,10\}\) totalling
216; \(s_{27}=8\); \(s_{28}=16\); plus \(s_{29}=36\) gives 276.
Input sum: four ordinary families each \(6+7+8+9+16+11=57\), plus
two even `tg0` families each \(6+8+16=30\), totalling 288.

DEEPMAP registry at lines 752–755 matches `sol-round6.md:125-129`
exactly.

CONFIRMED: the \(e\) of this lemma is the delayed loss of the
corrected square operator, not the withdrawn 29-minor index 295.

### 3.4 The \(\ell^+\ge 37\) strengthening (8.7)

Not part of the Newton lemma. Attacked anyway, because a false
lower bound on the campaign object would poison the gate table.

Round 6 used \(n=6\) (since \(F^6X=X\)) and the missing degree-36
target \(t^{36}e_{29}\) to get \(\ell^+\ge 31\). Sol uses the
literal \(n\ge 0\) in (2.1): for every \(e\le 36\) that target
lies in \(F^eY^+\) and, by the finite-window rank fact plus
causality through band 40, not in \(L(X)=L(F^0X)\). Hence
\(\ell^+\ge 37\). The arithmetic is correct.

Scope is correctly restricted to the 36 sampled operators (6
witnesses × 3 deep draws × 2 primes, one radical fiber `a00pp`),
matching the 8.S7-ADDENDUM and `sol-round6.md:111`. It is not 36
atlas fibers and not a D25 completion. Causality of the sampled
pure-y operators through band 40 is inherited from the Round-6
measurement, not re-proved here. As a lower bound on those
operators: CONFIRMED. As a theorem about every D25 completion: not
claimed.

The D23/D25 threshold table (lines 897–901) is the integer
rewriting of (3.10) and agrees with DEPTH-STAB’s
\(e\le\lfloor(D-1)/2\rfloor\). At the boundary, the lift agrees
only modulo \(F^{D-e}\) (D23: \(F^{12}X\); D25: \(F^{13}X\)).
Sol is more explicit than DEPTH-STAB that the entire depth-\(D\)
jet is not frozen. Consistent, not a promotion.

---

## 4. Characteristic \(p\)

Attacks: hidden \(n!\) or \(1/p\) in the Newton step; Ore resonance
silently inverted; binomial coefficients; geometric series; the
scalar 42.

- Theorem 3.1: addition and application of a given linear map \(S\).
  No division.
- Lemma 4.2: telescoping products, not Taylor. CONFIRMED.
- Geometric inversion of units: \(\sum(-1)^k\Delta^k\). Valid
  \(t\)-adically once \(\nu(\Delta)\ge 1\). No characteristic.
- Binomial expansion of a polynomial \((s+h)^n\): coefficients
  \(C(n,k)\) may vanish in characteristic \(p\), which removes
  remainder terms and can only raise order.
- (4.5) \((\Theta+1)u^j=(j+1)u^j\): in characteristic \(p\) the
  operator misses \(u^{p-1},u^{2p-1},\ldots\). Delayed loss is
  infinite. Sol records this as a *linear inverse* obstruction,
  not a remainder obstruction, and forbids promoting a low-window
  rank profile. That is the correct split. PARAM-30 must close
  \(p\)-periodic resonance. CONFIRMED as a warning; not a hole in
  3.1.
- The equation (1.6) contains \(42t^{20}\). If \(p\mid 42\) the
  *equation* changes; the *lemma* is for a given \(\mathcal H\).
  Campaign primes 105337, 105673, 200257 are not 2, 3, or 7.
- The lift is \(t\)-adic over the same field, not a lift from
  characteristic \(p\) to characteristic 0 (lines 49–50). Matches
  DEPTH-STAB’s mod-\(p\) formal germ.

No hidden divisibility in the Newton argument. CONFIRMED.

---

## 5. Boundary and edge cases

- **\(e=\infty\).** (2.1) empty \(\Rightarrow\ell=\infty\). Then
  (3.4) is never satisfied. No lift is claimed. Matches DEPTH-STAB
  DS4c (\(x^2=t^3\) solvable mod \(t^3\), \(e=\infty\), no lift)
  in fail-closed behaviour. CONFIRMED.
- **Section does not exist.** Equivalent to \(\ell=\infty\) by
  Lemma 2.1, for the series spaces at hand. Fail-closed.
- **Section exists but is not causal.** Then (2.3) fails, \(T\)
  need not map \(F^qX\) to itself, and the correction need not lie
  in \(F^{D-e}X\). The hypothesis correctly demands causality.
  An unqualified right inverse is the wrong object; Round 5 already
  said this.
- **\(D=2e\), \(\sigma=0\).** Then \(c=0\), (3.8) does not raise
  order, and the argument does not produce a Cauchy sequence.
  Proposition 3.3 gives an explicit polynomial counterexample over
  \(k[[t]]\), any characteristic: \(x_1=-t^e\) from the first
  coordinate, second coordinate becomes \(-t^{2e}=0\). CONFIRMED
  that \(2e+1\) is the sharp *uniform* threshold. (Some maps lift
  at \(D=2e\); the lemma does not claim otherwise.)
- **\(e=0\).** Gate is \(D\ge 1\). Ordinary Hensel with a
  filtration-preserving inverse. Correction in \(F^DX\). Fine.
- **\(\nu=\infty\).** Already a root; no correction. Stated.
- **\(\nu=2e\).** (3.11) requires \(\nu>2e\). Integers, so
  \(\nu\ge 2e+1\). Consistent with (3.10).
- **Agreement modulo \(F^{D-e}\), not \(F^D\).** Stated at lines
  15–16, 403–408, 714–717, 903–906. This is Tougeron’s usual
  loss, not a bug. A D25 point with \(e=12\) produces a germ that
  is a lift of its 13-truncation, not of the full depth-25 jet.
  Anyone advertising “the D25 jet lifts” from this lemma would be
  overclaiming; Sol does not.

---

## 6. Consistency with DEPTH-STAB.md

DEPTH-STAB §2(3), committed Route B: a depth-\(D\) point whose
Jacobian *minor* has \(t\)-adic valuation \(e\le(D-1)/2\) lifts to
a formal germ agreeing with \(s\) to depth \(D-e\). Decision
constant \(D^*_{\mathrm{eff}}=2e+1\). Toy: \(e=1\) lifts from depth
\(3=2e+1\) (DS4a/b). Fail-closed at \(e=\infty\) (DS4c).

### 6.1 Numerical criterion

Corollary 3.2 with \(\sigma=0\) is the same inequality, the same
agreement \(F^{D-e}\), and the same reading
\(e\le\lfloor(D-1)/2\rfloor\). CONFIRMED.

### 6.2 Does it *reduce* to Tougeron when Euler terms vanish?

Remark 2.2: if \(L\) is an \(R\)-linear square matrix with
\(\det L=t^e\varepsilon\), \(\varepsilon\in R^\times\), the
adjugate formula \(S=(\det L)^{-1}\mathrm{adj}(L)\) is a causal
right section of loss at most \(e\). The identity
\(A\,\mathrm{adj}(A)=(\det A)I\) is valid over any commutative
ring, so this direction has no characteristic restriction.
Corollary 3.2 then *is* the ordinary minor criterion.

When Euler/\(\Theta\) terms vanish, \(L_s^+\) is a matrix over
\(k[[u]]\), hence \(R\)-linear on the unpacked \(t\)-series.
Remark 2.2 applies. CONFIRMED: the lemma specialises to Tougeron
\(2e+1\) on the \(R\)-algebraic class that DEPTH-STAB actually
proved.

Two dictionary cautions, neither a contradiction:

1. DEPTH-STAB’s \(e\)-recipe (§3) is min-val of maximal minors of
   the *window* Jacobian of finitely many coefficient equations.
   Round 5 already ruled that object inadequate for the series
   map: the decisive derivative is the Euler/Ore operator, not a
   scalar Jacobian of emitted rows. Sol does not claim that the
   window-minor \(e\) equals \(\ell(L_s^+)\). The reduction is
   for the abstract \(R\)-linear series map, which is what
   DEPTH-STAB’s Tougeron toy actually is.
2. DEPTH-STAB “Route B” is Tougeron for that algebraic window.
   Sol’s “Route B” is Round 5’s second E-HENSEL bullet (filtered
   differential Newton). The shared name is unfortunate and could
   be misread as “DEPTH-STAB already proved this.” The mathematics
   is a genuine extension, not a relabelling. Nit on wording.

DS4c remains the \(e=\infty\) control; Proposition 3.3 is the
finite-\(e\) sharpness that DEPTH-STAB did not record. Complementary.

---

## 7. Cross-check against Round 5 / Round 6 / 8.S7

### 7.1 What E-HENSEL asked for

`sol-round5.md:171-175`, quoted in `SHEET6-DIRECTIONB.md:1591-1602`
as the unbanked promotion gate: either conjugation, or

> a completed-ideal bridge, a derivative with delayed-parametrix
> loss at most \(e\), and the quadratic remainder estimate imply
> lifting whenever \(D\ge 2e+1\).

Sol proves the implication (Theorem 3.1 + Proposition 5.3), proves
the remainder estimate for Euler-differential polynomials (Lemma
4.2), and isolates the delayed-parametrix as a hypothesis
(PARAM-30) rather than a theorem. That is exactly Route B.
CONFIRMED closed as an abstract theorem.

The four leftover conjectures (lines 23–33) are the right split:
CYCLIC-30 is support/generation; BRIDGE-30 is the universal
pristine/emitted identities; PARAM-30 is the section at a named
completion, including characteristic-\(p\) resonance; FILTER-30 is
the repository-formula audit that Lemma 4.2’s hypotheses hold on
the Newton ball. Legal completion is correctly called data, not a
conjecture (lines 1011–1016).

### 7.2 8.S7 and the withdrawn 295

8.S7-ADDENDUM: \(e=295\) withdrawn as a corrected-object value;
substantive stop restated as \(\ell^+\ge 31>11\) on the 36 sampled
full 30-stream operators. Sol §8 keeps that stop, strengthens the
lower bound to 37 by using \(n=0\), and refuses to treat 295 as
input to Newton. Consistent with Round 6 §1.2 and with
`xmodel/grok-atlas-e-review.md` Object B.

8.S7’s banner still says E-HENSEL is unbanked. After this file,
that sentence is the piece that should move: the *lemma* is no
longer the obstruction; PARAM-30 / FILTER-30 / the four gates are.
That is an 8.S7 bookkeeping item, not a defect in the proof. This
review does not edit 8.S7.

### 7.3 Theorem 6.1

Conditional packaging is correct and tight: eight hypotheses, then
a germ in \(s+F^{D-e}X\) for the *pristine* system, agreeing with
the supplied point only below depth \(D-e\). The proof (lines
719–727) is the expected one-paragraph application. The remark
that right inverses at Newton iterates need not be stable is
correct and is the reason fixed-linearization matters for Ore
resonance.

Proposition 5.3 (evaluate \(g_N=U_Nh_N\) at the formal point) is
the right vanishing argument. Sol correctly refuses to use
closure-equality of ideals in a completed coefficient algebra as
the sole transfer: evaluation at an infinite tail point need not
have closed kernel. Lemma 5.2 is recorded for the completed-ideal
statement that Round 5 also asked for, and is standard.

No attack on §5 flipped a verdict. The bridge *identities* remain
BRIDGE-30.

---

## Findings (worst first)

### Issue 1 — Severity: medium (writeup, FILTER-30 path only)

- File: `xmodel/sol-newton-lemma.md:452-504`
- Description: Lemma 4.2’s statement permits “localizations at
  fixed chart units,” but the displayed proof is only for
  polynomials in \(\{x_i,\theta^j x_i\}\). Source-dependent
  inversion is treated afterwards; its two-point remainder (3.3)
  is asserted by “the same proof applies” without a telescope.
  The geometric-series argument for (3.2) on \(U^{-1}\) is
  characteristic-free and correct as far as it is written.
- Suggestion: either restrict the boxed 4.2 to polynomials and
  label the inverse as Lemma 4.3 with a written two-point
  identity, or add the two-line expansion
  \(N_R(h)=-(R(h)-R(0))DU(h)R(0)-R(h)N_U(h)R(0)\) and its
  telescope. FILTER-30 should continue to allow a direct proof of
  (3.2)–(3.3) as an equivalent discharge.
- Status: open
- Does not flip Theorem 3.1, Corollary 3.2, or the polynomial
  \(\sigma=0\) statement. Does not produce a characteristic-\(p\)
  counterexample.

### Issue 2 — Severity: nit (hypothesis stronger than the step)

- File: `xmodel/sol-newton-lemma.md:339-378`
- Description: the iteration applies \(S\) only to elements of
  \(F^DY\). A section on \(F^DY\) with delay \(e\) would suffice
  for a single residual of order \(D\). PARAM-30 as specified in
  (7.2) asks for all-depth (2.3). Safer for a uniform lemma;
  slightly more than one Newton lift uses.
- Suggestion: optional remark, not a change to (2.1).
- Status: open

### Issue 3 — Severity: nit (wording)

- File: `xmodel/sol-newton-lemma.md:5` (“Route B works”)
- Description: DEPTH-STAB’s committed Route B is algebraic
  Tougeron on the window. Round 5’s Route B is filtered
  differential Newton. The sentence is correct in the Round-5
  sense and easy to misread as “DEPTH-STAB already covers Euler.”
- Suggestion: say “Round-5 Route B (filtered differential
  Newton)” on first use.
- Status: open

No other issues. In particular there is no bug in (3.7)–(3.9), no
characteristic-\(p\) division, no mismatch with the corrected
30×30 operator, no silent promotion of 295, and no claim that a
D25 NONEMPTY point is a germ.

---

## What a D25 survivor still owes

Sol §9 is accurate. For a named NONEMPTY D25 point to become a
scoped mod-\(p\) formal germ via Theorem 6.1, a certificate must
still supply all of: a legal full completion; CYCLIC-30 or the
surplus half of BRIDGE-30; the residual bound \(\nu\ge D\);
the exact \(L_s^+\) replayed from (1.6) including x-side;
PARAM-30, a causal section of loss \(e\le\lfloor(\nu-1)/2\rfloor\)
closing every \(p\)-periodic resonance; FILTER-30 (or a direct
\(\sigma\), possibly positive); the two-sided identities (5.9);
and (7.3) or (7.4). Family-wide EMPTY still kills every scoped
germ with no Newton lemma. NONEMPTY without those certificates
is still only finite-depth survival.

The sampled-operator lower bound (8.7) says the *present* D23
`a00pp` completions are nowhere near the depth-only D23/D25
gate. Extra residual vanishing \(\nu\gg D\) could in principle
re-open (7.3) at those points; it would be a depth-\(\nu\) point,
not a depth-25 certificate of a large \(e\). Sol already says
this.

---

## Bottom line

The proof of the filtered fixed-linearization Newton theorem is
correct, characteristic-free, and the right replacement for
DEPTH-STAB Tougeron once \(\theta\) acts on the unknown. Euler
terms do not require conjugation. The quantity \(e\) is the delayed
loss of the corrected 30×30 operator, well-defined, matching
Round 6 §1, and not computable from a finite rank profile. Edge
cases fail closed. Residual writeup gaps sit on the FILTER-30
inverse path and on wording, not on Theorem 3.1.

E-HENSEL is no longer the obstruction. PARAM-30 at a legal D25
completion is.
