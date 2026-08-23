# Hostile review: residue-A / tetrahedral Belyi identification

Reviewer: Grok 4.6 (hostile referee, verdict tier). Date: 2026-08-23.
Repo: `/Users/dc/code/math/jc72108`. No git. No file changes except this
review.

Target: `xmodel/sol-belyi.md`, executing rank-3 of `xmodel/sol-connections.md`
against the residue-A genome of `SHEET6-TEMPLATE.md` and the rung-36 row of
`SHEET6-DIRECTIONB.md`.

Claims under review:

1. **VERIFIED (as stated by Sol).** The residue-A collapse *is* the
   degree-4 Belyi map
   \(\beta(u)=u(u-2/3)^3/(u^2-u+1/6)^2\), passport
   \(((3,1),(2,2),(3,1))\), monodromy \(A_4\) in the four-point action,
   rigid (one Nielsen orbit), double poles in ratio \(2+\sqrt3\).
2. **REFUTED AS STATED (as stated by Sol).** The rung-36 row is *not*
   the passport tangent equation; it is the universal top-coefficient of
   the first variation of \(g^2-f^3\).
3. **Consequence.** If (1) holds, does \(A_4\) rigidity give any leverage
   on the residue-A tower (finiteness / depth bound, a characteristic-zero
   D43 certificate), or is it a beautiful-but-inert coincidence?

Method: independent exact arithmetic, not a read of Sol's SymPy log.
Polynomials over \(\mathbf Q\) and \(\mathbf Q(\sqrt3)\) were expanded
with `fractions.Fraction` (no SymPy in the environment). Nielsen triples
were enumerated on the 24 elements of \(S_4\). The banked char-0 window
row `C16.10` was decoded from `directionb_window_conditions.pkl`. The
template collapse \(W(t)\) and the two printed modular coefficients were
checked against `SHEET6-TEMPLATE.md` E4 and `SHEET6-DIRECTIONB.md`
§10.5. No D43 constructor rerun, no git.

---

## Verdict table

| # | Claim | Verdict | What would have flipped it |
|---|---|---|---|
| 1a | \(\beta\) is a Belyi map: exactly three critical values \(0,1,\infty\) | **CONFIRMED** | a zero of the exact derivative numerator off \(\{0,2/3\}\) mapping to a fourth value, or a Riemann–Hurwitz defect other than \(6=2\cdot4-2\) |
| 1b | ramification / passport of \(\beta\) is \((3,1)\) over \(0\), \((2,2)\) over \(\infty\), \((3,1)\) over \(1\) | **CONFIRMED**. Residual **GAPS** only as passport *order*: the printed triple \(((3,1),(2,2),(3,1))\) is the table order \((0,\infty,1)\), not the standard \((0,1,\infty)=((3,1),(3,1),(2,2))\) used for the displayed generators | \(N-D\) of degree \(>1\), a cancelled pole, or ramification at \(u=0\) |
| 1c | double-pole ratio \(a_1/a_2=2+\sqrt3\) over \(\mathbf Q(\sqrt3)\) | **CONFIRMED** | discriminant of \(u^2-u+1/6\) not \(1/3\), or \(\rho+1/\rho\neq4\) |
| 1d | that ratio, and the collapse \(W(t)\), really *are* the residue-A genome, not a quadratic-field coincidence | **CONFIRMED** for \(a_1/a_2\), \(a_1a_2=\sigma^2/6\), \(b=2\sigma/3\), \(b_2=3\sigma/4\). Residual **GAPS**: \(\kappa=42\) is *not* a Belyi invariant of \(\beta\); the merge scale \(\sigma\) is not pinned to \(6\) | \(W(\sigma u)/\sigma^4 \neq N-D\), or a second monic factored map of this passport with a different pole ratio |
| 1e | monodromy is \(A_4\) in the four-point action | **CONFIRMED** | a generator of odd sign, or \(\langle\sigma_0,\sigma_1,\sigma_\infty\rangle\) of order other than \(12\) |
| 1f | rigid: one simultaneous-conjugacy orbit in the Nielsen class | **CONFIRMED** as *absolute* Nielsen (one \(S_4\)-orbit of \(24\)). Residual **GAPS** as *inner* Nielsen: two \(A_4\)-orbits of \(12\), because \(\sigma_0\) and \(\sigma_1\) lie in opposite \(A_4\) three-cycle classes | a second \(S_4\)-orbit, or a second gauge-fixed solution of \((E_3,E_2)\) |
| 2 | rung-36 is not the Hurwitz tangent; it is the universal \(g^2-f^3\) first-variation top coefficient \(3\operatorname{Tr}(F)-2\operatorname{Tr}(G)-\operatorname{Tr}(H)\) | **CONFIRMED** | the first variation of \(g_\varepsilon^2-f_\varepsilon^3\) depending on \(a_1/a_2\); the rung kernel contained in the Hurwitz kernel; or a second independent row involving the pole anti-trace over \(\mathbf Q(\sqrt3)\) |
| 3 | rigidity of the tetrahedral cover does **not** bound tower depth, certify D43, or give \(\ell+\) / G5 | **CONFIRMED** (inert for the tower). The leading identification is real, not a coincidence; it is still not a constraint on tails | a proved faithful marked-jet landing from the tower into the Hurwitz tangent space, with uniformly bounded kernel |

Claim 1 as a statement about the *leading collapse* stands. Claim 2's
reassignment stands. The conditional rank-3 payoff does not fire.

---

## Claim 1 — the map, the passport, the genome, the group

### 1.1 \(\beta\) is genuinely Belyi

Put \(N=u(u-2/3)^3\) and \(Q=u^2-u+1/6\), \(D=Q^2\), \(\beta=N/D\). Exact
expansion over \(\mathbf Q\):

\[
\begin{aligned}
N&=u^4-2u^3+\tfrac43 u^2-\tfrac8{27}u,\\
D&=u^4-2u^3+\tfrac43 u^2-\tfrac13 u+\tfrac1{36},\\
N-D&=\tfrac{4u-3}{108}.
\end{aligned}
\]

The quotient formula gives \(\beta'=(N'Q-2NQ')/Q^3\). The numerator
divides exactly as

\[
N'Q-2NQ'=-\tfrac19(u-2/3)^2,
\]

remainder \(0\). So the printed derivative is literal, not a numerical
fit:

\[
\beta'(u)=-\frac19\frac{(u-2/3)^2}{(u^2-u+1/6)^3}.
\]

Finite ramification of \(\beta\) therefore occurs only at \(u=2/3\)
(value \(0\)). The two simple roots of \(Q\) are double poles (value
\(\infty\)). At infinity both \(N\) and \(D\) are monic of degree \(4\),
so \(\beta(\infty)=1\), and \(u^3(\beta-1)\to 1/27\), a triple point over
\(1\). The remaining point of \(\beta^{-1}(1)\) is the simple zero of
\(N-D\) at \(u=3/4\), with \(D(3/4)=1/2304\neq0\).

Riemann–Hurwitz for a degree-4 map \(\mathbf P^1\to\mathbf P^1\):

\[
(3-1)+(2-1)+(2-1)+(3-1)=6=2\cdot4-2.
\]

The defect is saturated. There is no room for a fourth critical value,
an omitted critical point, or hidden ramification at the simple zero
\(u=0\) (\(D(0)=1/36\neq0\), \(\beta'(0)\neq0\)).

\(\gcd(N,D)=1\): it would have to divide \(N-D=(4u-3)/108\), and neither
\(N\) nor \(D\) vanishes at \(u=3/4\). Degree \(4\) is honest.

This is a Belyi map, with critical values exactly \(\{0,1,\infty\}\).

### 1.2 Passport, with one labelling nit

| value | fibre | partition |
|---|---|---|
| \(0\) | \(u=2/3\) triple, \(u=0\) simple | \((3,1)\) |
| \(\infty\) | two simple roots of \(Q\), each a double pole | \((2,2)\) |
| \(1\) | \(u=\infty\) triple, \(u=3/4\) simple | \((3,1)\) |

Confirmed from the factorisations above, not from Sol's table.

**GAPS, notation only.** The note prints the passport as
\(((3,1),(2,2),(3,1))\), which is the table order \((0,\infty,1)\). The
monodromy generators are written in the standard order
\((\sigma_0,\sigma_1,\sigma_\infty)\) of types \((3,1),(3,1),(2,2)\). The
standard Belyi passport \((C_0,C_1,C_\infty)\) is therefore
\(((3,1),(3,1),(2,2))\). This is a labelling slip, not a wrong fibre.

### 1.3 Identification with the residue-A collapse is sound

The genome, from `SHEET6-TEMPLATE.md` E4 (and independently from the
degree drop \(\deg_t W\le1\)):

\[
W(t)=t(t-b)^3-(t-a_1)^2(t-a_2)^2,
\qquad
a_1+a_2=\sigma,\;
a_1a_2=\sigma^2/6,\;
b=2\sigma/3.
\]

These two coefficient equations are *the same* as the Hurwitz conditions
that a monic factored map of type \(((3,1),(2,2))\) over \(\{0,\infty\}\)
have triple contact with \(1\) at infinity. Substituting and scaling
\(t=\sigma u\) gives, exactly, for \(\sigma\in\{1,2,6\}\) and hence by
homogeneity for all \(\sigma\),

\[
\frac{W(\sigma u)}{\sigma^4}=N-D=\frac{4u-3}{108}
=\frac1{27}\Bigl(u-\frac34\Bigr).
\]

So \(W(t)=(\sigma^3/27)(t-3\sigma/4)\) is the numerator of \(\beta-1\).
The residue-A \(h_2\)-collapse *is* the defining identity of this Belyi
map, after the source scale \(t=\sigma u\). The assignments
\(b=2\sigma/3\) and \(b_2=3\sigma/4\) are the triple zero of \(\beta\)
and the simple point over \(1\).

The pole ratio is not “some unit of \(\mathbf Q(\sqrt3)\)”. The
normalised quadratic \(u^2-u+1/6\) has discriminant \(1-2/3=1/3\) and

\[
\frac{u_1}{u_2}+\frac{u_2}{u_1}
=\frac{(u_1+u_2)^2-2u_1u_2}{u_1u_2}
=\frac{1-1/3}{1/6}=4,
\]

so \(\rho=u_1/u_2\) solves \(\rho^2-4\rho+1=0\), hence
\(\rho=2\pm\sqrt3\). Directly over \(\mathbf Q(\sqrt3)\),

\[
a_\pm=\tfrac12\pm\tfrac{\sqrt3}6,
\qquad
\frac{a_+}{a_-}=2+\sqrt3.
\]

Any other pair of conjugate poles in \(\mathbf Q(\sqrt3)\) would give a
different ratio and a different remainder degree. The \(6\) in
\(a_1a_2=\sigma^2/6\) is forced by the \(t^2\)-cancellation at
\(b=2\sigma/3\); it is the Belyi modulus of this factored shape, not an
accident of the field.

**GAPS, on the extra genome numbers the prompt asked about.**

- The merge scale \(\sigma\) itself is a source coordinate, not a Belyi
  invariant. Setting \(\sigma=6\) makes \(a_1+a_2=6\) and \(a_1a_2=6\),
  still ratio \(2+\sqrt3\). The template's \(M^*(G_m)=6\) is a *different*
  six: \(\gcd(12,18)\) of the merge patterns, which is why the reduced
  coordinate \(t=\eta^3\) has degree \(4\). Related through the \((2,3)\)
  tower, not an extra match of \(\beta\).
- \(\kappa=42\) does not appear in \(\beta\). It is the Puiseux lcm
  \(7\cdot3\cdot2\) of the full Newton chain. The Belyi map lives in the
  reduced \(t\)-chart at \(G_m\) (degree \(4\) in \(t\), pattern degree
  \(12\) in \(\eta\)). `C7SUB = {42: 6, 21: 3}` is how the \(42\)-series
  sit over the reduced double factors; it multiplies the first-variation
  identity by three (see Claim 2), and is not a tetrahedral invariant.
  Using \(\kappa=42\) as evidence *for* the identification would be the
  coincidence the attack was looking for. Sol does not so use it.

The identification that *is* claimed — collapse \(=\) this \(\beta\),
pole field \(=\) pole field of \(\beta\) — is exact.

### 1.4 Monodromy \(A_4\), absolute rigidity, inner split

Displayed generators, 1-based, with composition \(p\circ q\) meaning
“apply \(q\) then \(p\)”:

\[
\sigma_0=(1\,2\,3),\qquad
\sigma_1=(2\,3\,4),\qquad
\sigma_\infty=(1\,2)(3\,4).
\]

Product \(\sigma_0\circ\sigma_1\circ\sigma_\infty=\mathrm{id}\). All three
are even, so the group lies in \(A_4\). The generated group is all of
\(A_4\) (order \(12\)), acting transitively on four letters. This is the
standard four-point action, not the regular representation of degree
\(12\). (The Klein tetrahedral function of degree \(12\) is the Galois
closure, not \(\beta\). Naming \(\beta\) “tetrahedral” is the usual
name for this monodromy; it is not a claim that \(\beta\) *is* Klein's
degree-12 quotient.)

Enumeration of ordered triples of cycle types \((3,1),(3,1),(2,2)\) in
\(S_4\) with that product:

- \(8\) three-cycles, \(3\) double transpositions;
- \(24\) triples, not \(8\times8\times3\) filtered — every pair
  \((\sigma_0,\sigma_\infty)\) determines a three-cycle
  \(\sigma_1=\sigma_0^{-1}\circ\sigma_\infty^{-1}\);
- all \(24\) are transitive and all generate a group of order \(12\);
- \(S_4\) acts by simultaneous conjugacy with **one orbit of size \(24\)**.

Absolute Nielsen number \(24/24=1\). In the factored affine chart with
source gauges \(r=0\), triple-over-\(1\) at infinity, and \(a+c=1\), the
two Hurwitz equations cut out a single point (up to swapping the poles):
the \(4\times4\) Jacobian of \((E_3,E_2,r,a+c-1)\) has determinant
\(-2\sqrt3\neq0\). That is an independent uniqueness proof which does not
use permutations. Absolute rigidity is not in doubt.

**GAPS, inner Nielsen, does not flip uniqueness of \(\beta\).** The same
\(24\) triples form **two** \(A_4\)-orbits of size \(12\). The displayed
\(\sigma_0=(1\,2\,3)\) and \(\sigma_1=(2\,3\,4)\) lie in *opposite* \(A_4\)
three-cycle classes (\(\sigma_1\) is \(A_4\)-conjugate to
\(\sigma_0^{-1}\), not to \(\sigma_0\)). Inner Hurwitz number \(24/12=2\).
This is the expected rational class of a \(\mathbf Q\)-defined \(A_4\)
cover (inversion of loops). It does not produce a second isomorphism
class of covers, and Sol's text explicitly conjugates by \(S_4\). It
*would* be a wrong claim if “the Nielsen class has one orbit” were read
as inner. Flag it; do not flip Claim 1.

Infinitesimal rigidity at the tetrahedral point was recomputed:

\[
J_H
=\begin{pmatrix}
-1&-3&2&2\\
2&4&-3+\sqrt3/3&-3-\sqrt3/3
\end{pmatrix},
\quad
\operatorname{rank}2,
\]

kernel spanned by translation \((1,1,1,1)\) and scaling
\((0,2/3,a_1,a_2)\), both killed. Gauge-fixed determinant \(-2\sqrt3\).
The printed matrices are correct.

---

## Claim 2 — rung-36 is the universal \(g^2-f^3\) top coefficient

### 2.1 The banked modular shape really is \(3:-2:-1\)

Printed at both primes
(`SHEET6-DIRECTIONB.md` §10.5):

\[
c_1(\mathrm{tf}1_{48}+\mathrm{tf}2_{48})
+c_2\bigl(2(\mathrm{tg}1_{48}+\mathrm{tg}2_{48})
+\mathrm{tg}01_{48}+\mathrm{tg}02_{48}\bigr)=0
\]

with \((c_1,c_2)=(48635,54013)\) at \(p=105337\) and
\((50809,18288)\) at \(p=105673\). Directly:

\[
48635+3\cdot54013=2\cdot105337,\qquad
50809+3\cdot18288=105673.
\]

So \(c_1\equiv-3c_2\pmod p\) at both primes, and the rational candidate
is \(L=3\operatorname{Tr}(F)-2\operatorname{Tr}(G)-\operatorname{Tr}(H)\).
This is a check of the *printed* pair, not a reconstruction of the D43
left kernel (that constructor was not rerun).

### 2.2 `C16.10` independently has this linear part, and more

The char-0 window pickle, band \(16\), last echelon row, decoded on
branch \((s_1,s_2)=(1,1)\), has exactly twelve terms:

| monomial | coefficient |
|---|---|
| \(\mathrm{tf}1_{48},\mathrm{tf}2_{48}\) | \(3/184\) |
| \(\mathrm{tg}1_{48},\mathrm{tg}2_{48}\) | \(-1/92=-2/184\) |
| \(\mathrm{tg}01_{48},\mathrm{tg}02_{48}\) | \(-1/184\) |
| \(\mathrm{uf}18\cdot\mathrm{tf}1_{42},\mathrm{uf}18\cdot\mathrm{tf}2_{42}\) | \(-3/2\) |
| \(\mathrm{uf}18\cdot\mathrm{tg}1_{42},\mathrm{uf}18\cdot\mathrm{tg}2_{42}\) | \(1\) |
| \(\mathrm{uf}18\cdot\mathrm{tg}01_{42},\mathrm{uf}18\cdot\mathrm{tg}02_{42}\) | \(1/2\) |

The six level-\(48\) coefficients are \(L/184\). The six “nonlinear
terms” of the printed `C16.10` are bilinear
\(\mathrm{uf}18\times(\text{level }42)\), and they are *the same*
\(3:-2:-1\) combination at level \(42\): they equal
\(\mathrm{uf}18\) times the printed `C10.6`. On the locus of `C10.6`
the extra terms drop and `C16.10` becomes \(L_{48}=0\). That is why a
D43 compatibility supported only on the six level-\(48\) tails can be
exactly this row.

This already shows the combination is a recurring window identity, not a
Hurwitz equation (no \(\sqrt3\), no anti-trace).

### 2.3 First variation of \(g^2-f^3\), universal in the poles

Reduced carriers at two distinct poles \(a,c\), dual numbers:

\[
f_\varepsilon=\prod_{i=1}^2(q_i+\varepsilon F_i)^2,\qquad
g_\varepsilon=\prod_{i=1}^2(q_i+\varepsilon G_i)^2(q_i+\varepsilon H_i),
\]

\(q_1=u-a\), \(q_2=u-c\). Logarithmic derivatives at \(\varepsilon=0\),
using \(g^2=f^3=q_1^6 q_2^6\) on the nose:

\[
\frac{d}{d\varepsilon}(g_\varepsilon^2-f_\varepsilon^3)\Big|_0
=2q_1^5 q_2^5\bigl(R_1 q_2+R_2 q_1\bigr),
\qquad
R_i=2G_i+H_i-3F_i.
\]

The identity was checked two ways: the logarithmic computation above,
and an exact polynomial expansion at the *non-tetrahedral* sample
\((a,c)=(5,-2)\) with random \((F,G,H)\), where it holds coefficient-wise.
The poles never enter \(R_i\). The coefficient of \(u\) in the braces is
\(R_1+R_2=-L\). Full first-order common-power cancellation is
\(R_1=R_2=0\), two conditions; the rung keeps only the trace.

Unreduced `C7SUB` sizes \(6,6,3=3\cdot(2,2,1)\) replace the overall
factor \(2\) by \(6\) and leave the same \(R_i\). Sol's “merely
multiplies by three” is correct.

The dictionary “D43's \(\mathrm{tf}_i,\mathrm{tg}_i,\mathrm{tg}0_i\) are
these \(F_i,G_i,H_i\)” is the modelling step. It is the natural reading
of the three pole-cluster streams (f multiplicity \(2\), \(G_p\)
multiplicity \(2\), \(G_{0p}\) multiplicity \(1\)), and it matches both
the modular shape and `C16.10`. It was not replayed from
`directionb_window.py`'s jet product. Residual GAPS on that last inch of
dictionary; not enough to restore a Hurwitz reading.

### 2.4 Why this is not the passport tangent

Hurwitz, after putting the triple over \(1\) at infinity, is two
equations on four finite marks \((r,b,a,c)\):

\[
E_3=2a-3b+2c-r=0,\qquad
E_2=-a^2-4ac+3b^2+3br-c^2=0.
\]

The first differentiates to \(3\,db-2\,d(a+c)+dr=0\). One can *make*
\(L\) look like that by declaring
\(db=\operatorname{Tr}(\mathrm{tf})\),
\(d(a+c)=\operatorname{Tr}(\mathrm{tg})\),
\(dr=-\operatorname{Tr}(\mathrm{tg}0)\). Those are not the source
meanings: the three tails at cluster \(i\) perturb three coincident
carriers over the *same* pole, not the three distinct Belyi marks
\(b\), \(a+c\), \(r\).

Four separators, all recomputed:

1. **Universality.** (3.2) holds for arbitrary distinct poles. Neither
   \(a_1a_2=1/6\) nor \(a_1/a_2=2+\sqrt3\) enters. A passport tangent
   would detect the tetrahedral modulus.
2. **Missing row.** Hurwitz has a second independent equation, whose
   linearisation at the tetrahedral point contains the pole anti-trace
   over \(\mathbf Q(\sqrt3)\). The rung is a single rational trace.
3. **Kernel.** \(F_1=1\), \(F_2=-1\), \(G=H=0\) kills \(L\). The natural
   pole-position projection \((dr,db,da,dc)=(0,0,-1,1)\) is *not* in
   \(\ker J_H\):

   \[
   J_H\begin{pmatrix}0\\0\\-1\\1\end{pmatrix}
   =\begin{pmatrix}0\\-2\sqrt3/3\end{pmatrix}\neq0.
   \]
4. **Orientation.** The residual Belyi quotient is the leading piece of
   \(h_1^3/f^4\) (common \(P^6\) removed; \(f\) supplies the double-pole
   denominator). A literal pullback of Hurwitz would attach multiplicity
   \(2\) to \(\mathrm{tf}\). The rung attaches \(3\) to \(\mathrm{tf}\),
   which is the exponent of \(f\) in the *previous* cancellation
   \(h_1=g^2-f^3\). Coefficient orientation places the row one collapse
   upstream of the passport.

Sol's CONJECTURE 3 of `sol-connections.md`, in the form “rung-36 is the
unique non-gauge first-order obstruction to deforming \(\beta\) while
preserving the passport”, is therefore false. The weaker surviving
conjecture in `sol-belyi.md` §3 (a later D43 class might pull back a
Hurwitz row after a marked residual-jet map is constructed) is a
different statement and was not tested here.

The \(3:2:1\) resemblance to ramification indices in the passport is the
trap that produced CONJECTURE 3. Those integers are also the derivative
exponents of \(f^3\), of the doubled \(g\)-carrier, and of the leftover
simple carrier. The first-variation identity uses them in the second
sense.

---

## Claim 3 — leverage: sound leading name, inert for the tower

The identification in Claim 1 is not a coincidence. It recasts two
exact template facts (E4: \(W\) drops to degree \(1\); the pole
quadratic) as the unique rigid degree-4 \(A_4\) Belyi map of this
passport. What that recasting *buys*:

**A classical name for leading data already proved in characteristic
zero.** Passport, field of moduli \(\mathbf Q\), pole field
\(\mathbf Q(\sqrt3)\), ratio \(2\pm\sqrt3\), \(b=2\sigma/3\),
\(b_2=3\sigma/4\), uniqueness of the marked degree-4 quotient modulo
source/target \(\mathrm{PGL}_2\). Independently re-derived above. This
is a certificate that those numbers are tetrahedral invariants, not a
new derivation of them. Template E4 already had them over
\(\mathbf Q(\sqrt3)\) from branch counting.

**Not a finiteness or depth bound on the residue-A tower.** Every Belyi
passport has a finite Hurwitz space (three branch points, target
\(\mathrm{PGL}_2\) used up). Uniqueness is extra and is uniqueness of
the *leading* degree-4 map. The tower contains common factors stripped
before forming \(h_1^3/f^4\), Puiseux tails, seven dead-stretch
coefficients, B-side and \(x\)-side, and later Jacobian graph equations.
Those can move while \(\beta\) stays literally constant. Claim 2
*exhibits* such directions: \(R_1=-R_2\neq0\) deforms the \((2,3)\)
carriers and is invisible to the residual cover.

So “rigidity of a tetrahedral cover” does not, by itself, give:

- a bound on formal tower depth,
- the \(\ell+\) dichotomy,
- G5,
- emptiness or a dimension of graph-preserving D43,
- a characteristic-zero certificate that the *entire* modular D43
  left-kernel construction is the reduction of one char-0 row (two
  primes plus a window linear part are not that theorem; Sol already
  says so).

A route of that kind would need the “faithful marked-jet landing”
conjecture stated in `sol-belyi.md` §4. The naive landing into ordinary
Hurwitz space is already false, by (3.2). Absolute rigidity of \(\beta\)
proves neither existence nor faithfulness of an enriched landing map.

**Beautiful, not inert as a *name*; inert as a *constraint*.** The
honest one-line: the leading residue-A collapse is a rigid tetrahedral
Belyi map, and the residue-A tower is not thereby identified with that
map. Rank 3's hoped-for payoff — a classical rigidity theorem that
bounds the tower — does not fire. That is Sol's own final disposition,
and the recomputation agrees.

---

## Writeup nits that do not flip a verdict

- Passport printed in \((0,\infty,1)\) order, monodromy in \((0,1,\infty)\)
  order (§1.2).
- Inner Nielsen split omitted (§1.4). Absolute rigidity is what was
  claimed, and it holds.
- “Tetrahedral Belyi map” is the degree-4 four-point quotient, not
  Klein's degree-12 function. Harmless if read as monodromy.
- `C16.10`'s six extra terms are bilinear \(\mathrm{uf}18\times\)
  level-\(42\), and they repeat the same \(3:-2:-1\) combination. Calling
  them “nonlinear” is true and slightly vague; the repetition is
  evidence *for* the first-variation reading.
- The SymPy block in §5 is correct (every assertion in it was
  independently reproduced). It does not include the Nielsen
  enumeration; that count was stated as “found 24 / one orbit / order
  12” without a listing. Re-enumeration confirms it.

## What was not recomputed

- The D43 left-kernel that emitted \((c_1,c_2)\) at the two primes. The
  printed pair was checked modulo \(p\); the constructor was not rerun.
- A line-by-line replay of `directionb_window.py` jets identifying
  \(\mathrm{tf},\mathrm{tg},\mathrm{tg}0\) with the dual-number carriers
  of (3.2). The window row `C16.10` was decoded from the banked pickle
  and matches.
- Existence or non-existence of a later D43 class that pulls back the
  second Hurwitz row. That is Sol's weaker surviving conjecture, not
  Claim 1 or 2.

## Final disposition

Claim 1, read as a statement about the leading \(h_2\)-collapse and its
pole field: **CONFIRMED**, with the inner-Nielsen and \(\kappa=42\)
precision gaps above. Claim 2's reassignment of rung-36: **CONFIRMED**.
Consequence for the tower: **CONFIRMED as inert**. The quadratic unit is
a real Belyi invariant. The \(3:2:1\) row is a real common-power tangent
invariant. They are adjacent layers of the nested collapse, not two
coordinates of one Hurwitz-rigidity theorem, and rigidity of
\(\beta\) does not bound the rest.
