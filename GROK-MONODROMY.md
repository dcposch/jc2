# GROK-MONODROMY.md — S_6 monodromy product test of the residue-A template

Status: COMPLETE (2026-08-12). Mission: the covering-theoretic kill of the
residue-A template proposed in xmodel/grok-eval-20260812.md avenue 2 —
independent of the Sigray combinatorics. Ground truth: SHEET6-TEMPLATE.md
secs 1a–1d (genome), SHEET6-CLASSICAL.md (splice extraction of the Newton
pairs; T2 valuation formulae), SHEET6-LROOT.md LR2 (single x-cluster).
Engine: cases/grok_monodromy.py (new, additive; exact Fraction arithmetic
and exact S_6 group arithmetic; 52 checks, 0 FAIL). No existing file was
modified.

VERDICT: **SURVIVES.** The degree-6 dicritical fibration \(\hat g:\overline{C}\to\mathbb{P}^1\)
has pinned pole monodromy of type \((3,3)\). The LR2 x-cluster, together
with the T2c contact window, forces the generic-fibre finite ramification
to be a passport of 2-cycles — type \((2)^a(2,2)^b(2,2,2)^c\) with
\(a+2b+3c=42\) (169 passports) — plus an optional B-side of Riemann–Hurwitz
slack. Every one of those 169 passports admits an explicit tuple in \(S_6\)
whose product is the identity and whose generated subgroup is transitive.
Riemann existence therefore supplies a connected degree-6 cover for every
geometrically allowed type list. A nonrealisable product would have killed
the template by topology; the product is realisable, so this test does not.

Two specialisations *do* die, and die before group theory: an unsplit
x-cluster (one \(g\)-value) and the pure leading-form collapse
\(L(a_3)=c\,a_3^{63}\) (two \(g\)-values) both violate the degree budget of
\(\hat g\). Neither is forced by the pinned genome.

## 0. The cover, and what is being tested

Let \(C=\{f=a\}\) be a generic fibre of the residue-A template
(TEMPLATE 1a: \(\deg(f-a)=168\), Newton corner \((k_f,l_f)=(126,42)\),
type \((\alpha,\beta)=(2,3)\), \(g\) of corner \((189,63)\)). The fibre is
smooth (Keller) and irreducible (\(f\) primitive). Write \(\overline{C}\)
for its smooth compactification. The restriction of \(g\) compactifies to a
holomorphic map

\[
\hat g:\overline{C}\longrightarrow\mathbb{P}^1
\]

of degree \(\mathrm{td}(f,g)=6\) (TEMPLATE 1a, CLASSICAL T4a: three independently
defined 6's agree — topological degree, geometric degree \(\mu(F)\), and
\(\deg\hat g\)). Jacobian \(J(f,g)=1\) kills every affine critical point of
\(\hat g\): along the fibre, \(dg/dt=-(dx/dt)/f_y\), and \(f_y\) is finite
and nonzero on the affine part. All ramification of \(\hat g\) therefore
sits at the places at infinity of \(C\).

Those places, from TEMPLATE 1d and CLASSICAL §0:

- \(P_1\): one place, 42 conjugate series, Newton pairs \((7,2)(3,10)(2,5)\),
  \(g\)-pole of order 3.
- \(P_2\): the same shape (the \(\sqrt{3}\)-conjugate pole).
- B-side: 42 series, 6 per direction of the 7-element \(B\)-orbit at \(F_s\);
  \(g\) finite; place partition unpinned (degrees in \(7\mathbb{Z}\)).
- x-side: 42 series; \(g\) finite; LR2 pin: one cluster, \(\kappa_G=1\).

The monodromy representation of \(\hat g\) is a homomorphism
\(\pi_1(\mathbb{P}^1\setminus B)\to S_6\), \(B\) the finite set of branch
values. A standard generating system of loops, one around each point of
\(B\cup\{\infty\}\), multiplies to a contractible curve. Hence a necessary
condition for the cover to exist is the **product relation in \(S_6\)**:
there exist permutations of the pinned local types whose product is \(1\)
and which generate a transitive subgroup. That is the test. Failure is a
kill; success is only a necessary condition (Riemann existence produces
some compact Riemann surface, not necessarily a plane fibre of a polynomial
pair).

## 1. Cycle-type derivation

### 1a. Newton pairs \(\to\) one place of \(x\)-degree 42 at each pole

Standard conversion (Eisenbud–Neumann, *Ann. of Math. Studies* 110, Ch. I;
the same formulae as CLASSICAL T1a). For Newton pairs \((p_i,q_i)\),

\[
m_1=p_1,\quad m_{i+1}=m_i\,p_{i+1},\qquad
\beta_1=q_1,\quad \beta_{i+1}=\beta_i\,p_{i+1}+q_{i+1},
\]

and the characteristic exponents are \(\beta_i/m_i\). On
\((7,2)(3,10)(2,5)\):

\[
m=(7,21,42),\qquad \beta=(2,16,37),\qquad
\frac{\beta}{m}=\frac{2}{7}<\frac{16}{21}<\frac{37}{42}
=\frac{12}{42}<\frac{32}{42}<\frac{37}{42}.
\]

The last multiplicity \(m_3=42\) is the \(x\)-degree of the place: a single
Puiseux place, parametrised by \(u=t^{42}\) (\(u=1/x\)), not 42 geometric
points of \(\overline{C}\). Cabling weights
\(a_1=q_1\), \(a_{i+1}=q_{i+1}+p_i p_{i+1}a_i\) recover CLASSICAL's
\((2,52,317)\). The local-chart pairs at \([1:0:0]\) (every contact shifted
by \(+1\)) are \((7,9)(3,10)(2,5)\), exponents \(54/42<74/42<79/42\). Both
poles have this shape.

(The pairs describe the embedding of \(C\) in the \((x,y)\)-plane, i.e. the
projection \(\overline{C}\to\mathbb{P}^1_x\). They enter the \(\hat g\)
monodromy only through the place count and through the valuation that
computes the pole order of \(g\).)

### 1b. Pole order 3 at each place \(\to\) type \((3,3)\) at \(\infty\)

TEMPLATE 1a: at \(P_i\), \(d_g=1/14\), \(\kappa=42\), so
\(\mathrm{ord}_t g=\kappa\,d_g=-3\). Independently, CLASSICAL T2a' recovers
the same number from the product formula along a \(P_1\)-branch:
\(\mathrm{ord}_u g=-1/14\), hence \(\mathrm{ord}_t g=-3\). Two poles, no
other poles at infinity on \(C\) (td \(=3+3\) is exhausted; \(g\) is finite
at every B-place and every x-place). Therefore

\[
\hat g^{-1}(\infty)=\{P_1,P_2\},\qquad e_{P_1}=e_{P_2}=3.
\]

**Local monodromy cycle type** (standard, e.g. Miranda, *Algebraic Curves
and Riemann Surfaces*, Ch. III; or Hartshorne IV.2): the conjugacy class of
the monodromy around a value is the partition of \(\deg\hat g\) given by
the ramification indices of the preimages. At \(\infty\) that partition is
\((3,3)\). It is not a 6-cycle (that would be one place of ramification 6)
and not \((3,2,1)\) (that would require a third preimage of \(\infty\)).

The two 3-cycles live on complementary triples of sheets: three sheets
approach \(P_1\), three approach \(P_2\). In a generating tuple one may
write them as two adjacent factors \(\sigma_{P_1}\sigma_{P_2}\) of types
\((3)\) and \((3)\); because they lie over the same point of \(\mathbb{P}^1\)
the geometrically correct object is the single permutation
\(\sigma_\infty=(1\,2\,3)(4\,5\,6)\) of type \((3,3)\). The two writings
differ by a Hurwitz move that does not change the existence question.

Each 3-cycle is an even permutation, so \(\sigma_\infty\) is even. Its
ramification contribution is \((3-1)+(3-1)=4\).

### 1c. x-side cluster (LR2 + T2c) \(\to\) 42 places of \(e=2\), types \((2),(2,2),(2,2,2)\)

LR2 (SHEET6-LROOT.md §3): the x-component of \(T_a\) carries exactly one
cv-vertex \(G\), with \(\kappa_G=1\). All 42 x-side Puiseux series form a
single cluster (pairwise contact \(\ge\pi_G\ge R=3\)), with no
characteristic exponent below \(\pi_G\).

CLASSICAL T2c squeezes the remaining slack: contacts are integers in units
of \(v=1/y\), each \(\ge 3\), and \(g\) finite forces the per-series contact
sum \(U_i\in\{123,124\}\), hence \(\pi_G\in[3,3+2/41)\). Combined with
integer contacts, the first split is at height **exactly 3**. (The St 9.4
integrality \(\kappa(\pi-1)\in\mathbb{N}\) gives the same pin
\(\pi_G=3\), but is not needed: T2c + integrality of contacts suffice.
This is the Sigray-free half of the x-side input; LR2 is used only as the
already-established single-cluster pin the mission statement asks for.)

Write the x-expansion at the point \([0:1:0]\) as
\(x=c_0'+a_3 v^3+a_4 v^4+\cdots\) (the coefficients of \(v^1,v^2\) vanish,
or else \(g\to\infty\) and the leftover td is not \(3+3\)). The 42 series
are the 42 choices of leading coefficient \(a_3\). The leading form of
\(f-a\) at this point is \(q\,a_3^{42}+\text{lower}=a\) with \(q\neq 0\)
(vanishing order of the \(y^{126}\)-form of \(f\) at \(c_0'\) is exactly 42,
or else \(\pi_G>3\)). For generic \(a\) this is a degree-42 equation with
42 distinct simple roots: **42 distinct \(a_3\)**, each a holomorphic branch
of \(x\) as a function of \(v\), hence a place of degree \(n=1\).

Contact between any two is exactly 3, so \(U=41\cdot 3=123\) and
CLASSICAL's T2 formula gives

\[
e'=n(125-U)=1\cdot 2=2.
\]

A group of \(m\) series sharing the same \(a_3\) (a multiple root of the
pattern at \(G\)) would have \(U\ge 4(m-1)+3(42-m)=m+122\). The window
\(U\in\{123,124\}\) forces \(m\le 2\). Multiplicity \(\ge 3\) pushes
\(U\ge 125\), and \(g\) is no longer finite of positive order. So the only
specialisation of \(p_G\) away from 42 simple roots is a mixture of simple
and double roots, which can only *lower* the number \(t\) of ramified
x-places (a double root either stays one place of \(e=2\), or splits into
two unramified \(e=1\) places). The generic — and, given the leading form
of \(f\), forced-for-generic-\(a\) — count is \(t=42\).

**Degree budget of \(\hat g\).** At each finite value the ramification
indices of all preimages sum to 6. Affine preimages are unramified
(\(J=1\)), so the infinite places over one value contribute a total of at
most 6. Each ramified x-place has \(e=2\), so at most three of them may
share a \(g\)-value. The local monodromy at that value is then of type
\((2)\), \((2,2)\), or \((2,2,2)\) (plus fixed points). Hence the generic
x-side passport is

\[
(2)^a\,(2,2)^b\,(2,2,2)^c,\qquad a+2b+3c=42,
\]

and there are at least \(\lceil 42/3\rceil=14\) distinct x-side \(g\)-values.
The engine counts 169 nonnegative integer solutions \((a,b,c)\).

Two configurations **die here, by the degree budget, with no appeal to
\(S_6\)**:

- Unsplit cluster (one \(g\)-value for all 42 places): \(\sum e=84>6\).
- Pure leading-form collapse \(L(a_3)=c\,a_3^{63}\) (the \(y^{189}\)-form
  of \(g\) alone). On the 42nd-roots of the fibre equation this takes
  exactly two values, 21 places each: \(\sum e=42>6\).

Neither is forced. The actual limit of \(g\) along an x-branch is a
polynomial \(L(a_3)\) of degree 63 (leading coefficient nonzero because
\(\pi_G=3\)), and a generic such \(L\) separates the 42 roots. The
template's dead-stretch coefficients and lower Newton terms are more than
enough to make \(L\) generic in this sense. The covering test therefore
proceeds with the 169-passport family, not with the collapsed specialisations.

### 1d. B-side: Riemann–Hurwitz slack, not a pinned type

B-place degrees lie in \(7\mathbb{Z}\) (first characteristic exponent \(2/7\)).
CLASSICAL T2b: a B-place of degree \(n\) has \(e=n(282-S)/42\), with
\(S\in[246,281]\) an integer and \(1\le e\le 6\). The engine's menu is
nonempty (e.g. \((n,e,S)=(7,2,270)\), \((7,1,276)\), \((42,1,281)\)).
B-ramification is optional: the unramified choice \(e=1\) on every B-place
is allowed and gives B-contribution \(R_B=0\) to Riemann–Hurwitz.

Shared B/x values (a B-place and an x-place with the same finite \(g\)-limit)
would only *merge* cycles into a coarser passport, which enlarges the
existence search, not shrinks it. The tightest test is B unramified and
no shared values, and that is the test that is run to completeness.

### 1e. Riemann–Hurwitz

**Riemann–Hurwitz formula** (Riemann 1857; modern: Hartshorne, *Algebraic
Geometry*, IV.2, or Fulton, *Algebraic Curves*, Ch. 8). For a holomorphic
map \(\varphi:X\to Y\) of compact Riemann surfaces, of degree \(d\),

\[
2g_X-2 \;=\; d\,(2g_Y-2) \;+\; \sum_{p\in X}(e_p-1).
\]

Here \(Y=\mathbb{P}^1\), \(d=6\), so \(2g-2=-12+R\) with
\(R=\sum(e-1)\). The two poles contribute 4. The generic x-side contributes
\(t=42\). B unramified contributes 0. Total \(R=46\), hence

\[
g(\overline{C})=18.
\]

This matches CLASSICAL's closed form
\(g=2763-(\mathrm{Sig}S/42+\mathrm{Sig}U+r_B+r_X)/2\) on the nose:
\(\mathrm{Sig}U=42\cdot 123=5166\), \(r_X=42\), and \(R_B=0\) forces
\(\mathrm{Sig}S/42+r_B=282\), so \(g=2763-(282+5166+42)/2=18\).

The sign condition on the passport is automatic: type \((3,3)\) is even,
type \((2)\) is odd, type \((2,2)\) is even, type \((2,2,2)\) is odd, and
\(a+2b+3c=42\) even forces \(a+c\) even.

A second, looser, RH-allowed configuration is recorded for completeness:
the specialisation \(t=0\) (all x-places unramified, 21 double roots of
\(p_G\) each split into two \(e=1\) places) with B-side six places of
degree 7 and \(e=2\). Then \(R=4+6=10\), \(g=0\), and the passport is
\([(3,3),(2)^6]\). This is the genus-0 cover of the rational function
\(z^3+z^{-3}\) plus nothing x-side; it sits inside the B-menu
(\((n,e,S)=(7,2,270)\)) and the closed-form genus is exactly 0. It is a
specialisation, not the generic fibre, but it is a legal RH completion
and is realised below.

## 2. The product computation

### 2a. Riemann existence, cited precisely

**Riemann existence theorem** (Riemann; the permutation form is Hurwitz,
*Math. Ann.* 39 (1891); modern: Völklein, *Groups as Galois Groups*, Thm
2.13; or Donaldson, *Riemann Surfaces*, Ch. 7). Given distinct points
\(b_1,\dots,b_k\in\mathbb{P}^1\) and permutations \(\sigma_1,\dots,\sigma_k\in S_d\)
such that

1. \(\sigma_1\sigma_2\cdots\sigma_k=1\),
2. \(\langle\sigma_1,\dots,\sigma_k\rangle\) is transitive on \(\{1,\dots,d\}\),

there exists a compact Riemann surface \(X\) and a holomorphic map
\(\varphi:X\to\mathbb{P}^1\) of degree \(d\), branched at most at the
\(b_i\), with local monodromy at \(b_i\) equal to \(\sigma_i\) for a
suitable numbering of the sheets. Conversely every such cover arises this
way. Simultaneous conjugation of the tuple gives an isomorphic cover.

(The braid group of the punctured sphere acts by Hurwitz moves; existence
of one tuple in a braid orbit is existence of the cover.)

Applied here: \(d=6\), \(\sigma_\infty\) of type \((3,3)\), and the remaining
\(\sigma_c\) of types \((2)\), \((2,2)\), or \((2,2,2)\) with
\(a+2b+3c=42\). The engine works throughout with left-to-right composition
on \(\{0,1,2,3,4,5\}\) and with

\[
\sigma_\infty=(1\,2\,3)(4\,5\,6),\qquad
\rho:=\sigma_\infty^{-1}=(1\,3\,2)(4\,6\,5).
\]

A finite tuple multiplies to 1 against \(\sigma_\infty\) iff it multiplies
to \(\rho\).

### 2b. Short factorisations in \(S_6\) (exact)

\(S_6\) has 720 elements, 15 transpositions, 45 elements of type \((2,2)\),
15 of type \((2,2,2)\), 40 of type \((3,3)\). The following identities are
checked by evaluating the permutations, not by cycle-notation heuristics
(composition convention is pinned in the engine):

| core | type counts \((a,b,c)\) | product |
|---|---|---|
| \((1\,3)(1\,2)(4\,6)(4\,5)\) | \((4,0,0)\) | \(\rho\) |
| \((1\,3)(4\,6)\cdot(1\,2)(4\,5)\) | \((0,2,0)\) | \(\rho\) |
| \((1\,3)(4\,6)\cdot(1\,2)\cdot(4\,5)\) | \((2,1,0)\) | \(\rho\) |
| a pair of type-\((2,2,2)\) elements | \((0,0,2)\) | \(\rho\) |
| three type-\((2,2)\) elements | \((0,3,0)\) | \(\rho\) |
| \((2,2,2)^2\cdot(2,2)\) | \((0,1,2)\) | \(\rho\) |
| \((2,2)^2\cdot(2)^2\) | \((2,2,0)\) | \(\rho\) |
| \((2,2,2)^2\cdot(2)^2\) | \((2,0,2)\) | \(\rho\) |
| \((2,2,2)\cdot(2)^3\) | \((3,0,1)\) | \(\rho\) |
| \((2,2,2)\cdot(2,2)\cdot(2)\) | \((1,1,1)\) | \(\rho\) |
| \((2,2,2)\cdot(2,2)^2\cdot(2)\) | \((1,2,1)\) | \(\rho\) |

Two non-existences, also searched exhaustively and used as negative
controls:

- No product of **two** transpositions has type \((3,3)\) (the product is
  \(1\), a 3-cycle, or type \((2,2)\)). Minimum transposition-length of
  \(\rho\) is 4.
- Type \((2,2,2)\cdot(2)\) never equals \(\rho\) (720-free: 15 candidates
  for the first factor, the second is then determined, and is never a
  transposition). Type \((2,2,2)\cdot(2)\cdot(2)\) is odd, hence cannot
  equal \(\rho\) either.

### 2c. Padding, and the 169-passport sweep

An involution-pair \((\tau,\tau)\) multiplies to 1 and may be inserted
anywhere in a tuple without changing the product (two branch points with
the same local monodromy). Padding a core of counts \((a_0,b_0,c_0)\) by
pairs therefore realises every \((a,b,c)\) with \(a\ge a_0\), \(b\ge b_0\),
\(c\ge c_0\), and \(a\equiv a_0\), \(b\equiv b_0\), \(c\equiv c_0\pmod{2}\).
A connecting pair \(((1\,4),(1\,4))\) is included whenever
\(\langle\sigma_\infty,\text{core}\rangle\) is intransitive, so every
padded tuple generates a transitive group.

The cores of §2b cover every residue class of \((a,b,c)\bmod 2\) compatible
with \(a+2b+3c=42\). The engine builds a witness for each of the 169
passports, checks product \(=\rho\), checks transitivity of
\(\{\sigma_\infty\}\cup\text{witness}\), and checks the type counts. All
169 succeed.

Printed extremal witnesses:

- Passport \((2)^{42}\). Core of four transpositions, padded by 19 copies
  of a connecting pair. Full tuple
  \(\bigl(\sigma_\infty,\,(1\,3),(1\,2),(4\,6),(4\,5),\,((1\,4),(1\,4))^{19}\bigr)\)
  multiplies to 1, is transitive, and generates all of \(S_6\) (Cayley
  enumeration, order 720).
- Passport \((2,2,2)^{14}\). Core of two type-\((2,2,2)\) elements multiplying
  to \(\rho\), padded by six further pairs. Product 1, transitive.
- Genus-0 B-only passport \((2)^6\) (the \(t=0\) specialisation):
  \(\bigl((1\,3),(1\,2),(4\,6),(4\,5),(1\,4),(1\,4)\bigr)\) multiplies to
  \(\rho\), transitive with \(\sigma_\infty\). This is the monodromy type
  of \(z\mapsto z^3+z^{-3}\) (poles of order 3 at \(0\) and \(\infty\);
  two finite values of type \((2,2,2)\), which is the \(c=2\) rewriting
  of six transpositions merged three-and-three).

### 2d. What the enumeration does *not* claim

Riemann existence produces a compact Riemann surface \(\overline{C}\) of
genus 18 and a degree-6 meromorphic function of the pinned type. It does
not produce a plane curve of degree 168 with Newton corner \((126,42)\),
nor a polynomial \(g\) of corner \((189,63)\) with \(J(f,g)=1\). Those are
algebraisation constraints, not covering constraints. The test as
proposed — “can the product equal 1 in \(S_6\) with the pinned cycle
types?” — is the covering constraint, and the answer is yes.

## 3. Verdict

**The residue-A template does not die by this topology.**

Every geometrically allowed monodromy type list — pole type \((3,3)\)
from the Newton pairs and the two order-3 poles; x-side types in
\(\{(2),(2,2),(2,2,2)\}\) from the LR2 cluster and the T2c window;
B-side whatever RH permits — is realised by an explicit transitive
factorisation of the identity in \(S_6\). The covering \(\hat g\) exists
as an abstract branched cover. The Sigray combinatorics were not used,
except as the already-promoted LR2 pin the mission asked to take as input
(and even that pin is used only to force a single cluster; the cycle
types then come from classical valuation and the degree budget of a
degree-6 map).

What the test *would* have killed, and did not get to:

1. A pole profile other than \((3,3)\) incompatible with a complementary
   x-side of odd total sign. The Newton pairs do not produce such a
   profile.
2. An x-cluster forced to one or two \(g\)-values. The degree budget
   would then kill without group theory. The genome does not force the
   collapse.
3. A finite list of passports none of which factor \(\rho\) in \(S_6\).
   The list is 169 passports and all of them factor.

Residual, not run here (and not the proposed test): the cover produced by
Riemann existence has no reason to arise as the restriction of a
polynomial \(g\) to a degree-168 plane fibre with the pinned Newton
corner. That is the algebraisation problem (TEMPLATE R1/R5, or the
\(J\)-jet at \(G_m\) of the same eval's avenue 3). The present computation
removes the hope that residue-A is already illegal as a degree-6 cover of
the line.

Variant transfer: the (1,2), (2,3)-chain, and (2,5)-chain branches of
SHEET6-R6 share the \((f,g)\)-genome (they differ only in h-tower
exponents). Every pin used above is genome data, so the same tuple
realises \(\hat g\) for every surviving variant.

## 4. Trust perimeter

Classical statements used, cited before they are applied:

- (RH) Riemann–Hurwitz, as in §1e. Applied to \(\hat g:\overline{C}\to\mathbb{P}^1\)
  of degree 6, no affine ramification. Recovers CLASSICAL's genus identity
  on the generic x-side (\(g=18\)) and on the \(t=0\) exhibit (\(g=0\)).
- (RET) Riemann existence / Hurwitz 1891, as in §2a. Applied only after an
  explicit tuple with product 1 and transitive image has been exhibited;
  the theorem is used as a *sufficient* condition, not as a black-box
  existence table.
- (LM) Local monodromy cycle type = ramification profile
  (Miranda / Hartshorne IV.2). Applied at \(\infty\) to the two poles of
  order 3, and at each finite value to the x-places of \(e=2\).
- (EN) Eisenbud–Neumann Newton-pair \(\leftrightarrow\) characteristic
  exponent / cabling conversion (CLASSICAL T1a, re-derived in-engine).
  Used only to confirm the place degree 42 and to name the pairs; the
  pole order itself is TEMPLATE 1a / CLASSICAL T2a'.
- (T2) CLASSICAL's valuation formulae \(e_p=n_p(282-S_p)/42\) (B-side)
  and \(e'_p=n'_p(125-U_p)\) (x-side), and the closed genus
  \(g=2763-(\mathrm{Sig}S/42+\mathrm{Sig}U+r_B+r_X)/2\). Re-checked as
  exact identities on the two configurations that are used as exhibits.

Inherited campaign pins, used as input not re-proved: TEMPLATE secs 1a–1d
(two poles of order 3, Newton pairs, corners, td \(=6\)); LROOT LR2
(single x-cluster, \(\kappa_G=1\)); CLASSICAL T2c (\(\pi_G=4\) dead,
\(U\in\{123,124\}\)). No unprinted Sigray lemma, no M-PAT, no Groebner
output, and no campaign hypothesis beyond those three pins enters the
argument.

Caveats, stated: (i) RET existence is necessary for a polynomial
realisation, not sufficient; (ii) shared B/x values are not enumerated
(they relax the test); (iii) the \(t<42\) specialisations of \(p_G\) are
classified but not each given a separate 169-style sweep — they have
*fewer* ramified x-places, so they fall under the \(t=0\) exhibit plus
optional B-side, already realised, or under a sub-passport of a \(t=42\)
passport obtained by dropping unramified places; (iv) composition in the
engine is left-to-right and is pinned by the in-engine product checks,
so a reader who composes cycles the other way will see the inverse
4-transposition identity \((1\,2)(1\,3)(4\,5)(4\,6)=\sigma_\infty\),
which is the same factorisation read backwards.

## 5. Reproduction

```
cd cases && python3 grok_monodromy.py     # 52 checks, 0 FAIL, exact
```

The engine is self-contained (stdlib only: `fractions`, `itertools`).
It re-derives the Newton-pair exponents, the \((3,3)\) type, the x-side
\(U/e/m\) bounds, the 169 passports, the short factorisations, the padded
witnesses, the B-menu, and both genus identities. A single FAIL aborts
nonzero.
