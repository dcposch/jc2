# max11 `(6,10)` scale-two degree-zero linear-root chamber: endgame of the vanishing tower

**Verdict: PARTIAL**

The order-69 head of the compact post-collapse numerator is the monomial
\(\frac{2}{27} p_{32}^3 q_{41}\) in the \(\mathbb{Q}\)-primitive (the live
integer \(7583143431241728\, p_{32}^3 q_{41}\) is this times the compact
clearing constant). Vanishing forces \(p_{32}(a)=0\) or \(q_{41}(a)=0\).
Two-sided total vanishing of the remaining source coefficients at the
linear root \(a\) of \(h_0\) makes \(h_0\) divide both source polynomials
and therefore the Jacobian, contradicting \(j\neq 0\). That limit is not
forced: after order 69 the live arms are genuine hypersurfaces (cofactors
are not units, and they are not killed by an exact degree comparison in
\(k[X]\)). The formal \(h\)-degree of \(Q\) is at most \(75\), so there
are at most seven frozen heads (orders \(69\) through \(75\)); at the
ceiling a holomorphic primitive cannot have derivative \(j/h_0\). Closing
the cofactor arms still needs the next Taylor objects (including
\(q_{41}'\)) and is not a referee-checkable contradiction from committed
input alone.

No exit-price is claimed.

---

## 0. Sources and verification status

Work over an algebraically closed field \(k\) of characteristic zero, on
the normalized scale-two \((6,10)\) nonzero face. Clone used for reading:
`https://github.com/dcposch/jc2-lean` at `d4e9bfe` (`origin/master` as of
this run). The nested worktree `jc2-lean/` is sandbox-blocked.

### 0.1 What was read (committed, used below)

| File / theorem | Used for |
|---|---|
| `LowScaleCore.lean`, `NormalizedCoprimeLeadingCoreSource` / `Normalized610LeadingCoreSource` | \(p.\mathrm{natDegree}=6\), \(q.\mathrm{natDegree}=10\), leading \(p_6=h^3\), \(q_{10}=h^5\), `IsPlaneKellerPair` |
| `Max11Core.lean`, `IsPlaneKellerPair` | Jacobian \(=C(j)\) with \(j\neq 0\) |
| `LowScale610ScaleTwoSourceFace.lean`, `normalized610ScaleTwo_nonzeroFace_has_linear_root` | \(H=h_0^2\), \(h_0.\mathrm{natDegree}=1\), \(N=C(\lambda)h_0^9\), \(\lambda\neq 0\), \(h_0(a)=0\) |
| `LowScale610ScaleTwoSecondFace.lean`, `nonzeroFace610_linearRoot_p5_zero`, `..._q9_zero` | \(p_5(a)=q_9(a)=0\) |
| `Sol610ScaleTwoNonzeroFourteenthComplementBackwireScratch.lean`, `nonzeroFace610_linearRoot_fourteenthComplementBackwire` | post-collapse peel recorded below |
| `LowScale68Depression.lean` / `LowScale68NormalForm.lean` | affine depression \(y=(z-r)/h\), monic depressed sextic \(z^6+Az^4+Bz^3+Cz^2+Dz+E\) |
| `LowScale68SourceBridge.lean`, `differentialJacobian_affineDepress_sourceToRatFunc68` | depressed Jacobian \(=C(j/h)\) |
| `Sol610ScaleTwoDegreeZeroPrimitiveScratch.lean`, `degreeZeroPrimitive610`, `degreeZeroPrimitive610_deriv_eq_row` | weight-15 primitive; \(d(\mathrm{prim})=W\,dE-D\,dX\) after residual constants |
| `Sol610ScaleTwoDegreeZeroLocalPoleScratch.lean`, `localLinearPoleSix_head_eval_zero_of_deriv_eq_simplePole610` | pole-six head obstruction |
| `LowScale610ScaleTwoSixthFace.lean`, `epsilonResidual610`; `...SeventhFace.lean`, `zetaResidual610` | \(T_0\) and \(U_0\) as leading polar summands |
| `LowScale810ScaleTwoThirdFace.lean`, `linearPolynomial_dvd_of_eval_eq_zero_810` | linear \(h_0\) divides a coefficient vanishing at \(a\) |
| `derive_610_degree_zero_residual.py` (`COMPUTE_SOURCE`) | \(Abar,\ldots,Xbar\), clearing by \(h^{75}\), post-collapse jet |
| `LowScale610ScaleTwoFifteenthFinalRow.lean` | degree-0 row is the last Keller coefficient; does *not* claim \(p_2,p_1,p_0,q_3\) vanish |
| `HANDOFF_2026-08-31.md` | untracked live-chain file list and intended wrapper |

Leading exactness used below: on this face \(H=h_0^2\), so
\(p.\mathrm{coeff}\,6=H^3=h_0^6\) and \(q.\mathrm{coeff}\,10=H^5=h_0^{10}\)
as polynomials. Packet tops \(h_0\neq 0\), \(\lambda\neq 0\), \(j\neq 0\).

Backwire peel (theorem
`nonzeroFace610_linearRoot_fourteenthComplementBackwire`):

\[
\begin{aligned}
p_5&=h_0^5 w_1,&
p_4&=h_0^4 a_{42},&
p_3&=h_0^2 p_{32},&
p_2&=h_0 p_{21},\\
q_8&=h_0^8 s_2,&
q_7&=h_0^6 u_2,&
q_6&=h_0^5 b_{63},&
q_5&=h_0^3 q_{53},&
q_4&=h_0 q_{41}.
\end{aligned}
\]

The coordinates \(p_1,p_0,q_3,q_2,q_1,q_0\) are not peeled further. Here
\(p_{32},p_{21},\ldots\) are *source-coefficient quotients*, not the
depressed functions \(A,B,C,D,E\) themselves. Differentiation in the
source variable \(X\) is the polynomial derivative; a prime mark on a
compact coordinate (e.g. \(q_{41}'\), or the next-jet labels \(p_{32n},
p_{21n}\)) means the next Taylor coefficient at \(a\), not a Lean name.

### 0.2 What was not read

Untracked live-chain scratch (HANDOFF list; not on `origin/master`;
re-derived where possible, otherwise quoted):

- `Sol610ScaleTwoDegreeZeroCompactSourceScratch.lean`
- `Sol610ScaleTwoDegreeZeroDifferentialBridgeScratch.lean`
- `Sol610ScaleTwoNonzeroFourteenthPostCollapseResidualScratch.lean`
- `Sol610ScaleTwoNonzeroFourteenthPostCollapseHeadSplitScratch.lean`
- `Sol610ScaleTwoDegreeZeroPostCollapseJetScratch.lean`
- `Sol610ScaleTwoDegreeZeroPostCollapseSourceBridgeScratch.lean`
- `Sol610ScaleTwoDegreeZeroPostCollapseCoordinateBridgeScratch.lean`
- `Sol610ScaleTwoDegreeZeroPostCollapseHeadSplitScratch.lean`

The name `degreeZeroPrimitive610_ratFuncDeriv_eq_simplePole` is
**UNVERIFIED** as a Lean declaration. Section 1 reconstructs the intended
composition from committed pieces.

Residual definitions `etaResidual610`, `thetaResidual610`,
`iotaResidual610`, `kappaResidual610`, `lambdaResidual610` live in
untracked `Grok610*` / `Fable610*` files imported by the committed
Twelfth/Primitive modules. Group polynomials multiplying those residuals
*are* committed (`degreeZeroEtaGroup610`, `degreeZeroThetaGroup610`).
Order 69 does not use them. Order \(\ge 70\) contributions of
\(V\cdot\eta\)-group and \(W\cdot\theta\)-group are recorded with that
caveat: the primitive multiplies the *residual*, not the raw coordinate
\(V_0,W_0\).

Live order-70/71 disjunctions and the nine-/eight-/five-term cofactors
are quoted from the prompt. They are **UNVERIFIED** as Lean identities
and are compared with the frozen polar calculus of §3.

---

## 1. The tower engine (committed pieces)

Affine depression \(y=(z-r)/h_0\) with \(r=a_5/(6h_0^5)\) produces a
monic depressed sextic and a monic decic over \(\mathrm{RatFunc}\,k\).
The source Keller identity maps to

\[
\mathrm{differentialJacobian}(\hat p,\hat q)
= C\bigl(j/h_0\bigr)
\]

(`differentialJacobian_affineDepress_sourceToRatFunc68`). The degree-zero
row of that depressed Jacobian is \(W E'-D X'\). After every residual of
the \(\alpha\)–\(\mu\) tower is a differential constant,
`degreeZeroPrimitive610_deriv_eq_row` gives

\[
d\bigl(\mathrm{degreeZeroPrimitive610}\bigr)=W\,dE-D\,dX.
\]

Composing these (the missing source wrapper) is the statement that the
primitive, as a rational function \(\rho\) of the source variable, has

\[
\rho' = j/h_0
\]

on the residual-constant locus. That is the intended content of the
untracked name `degreeZeroPrimitive610_ratFuncDeriv_eq_simplePole`.
**UNVERIFIED** as a landed theorem; the two factors are committed.

The python `COMPUTE_SOURCE` block clears the primitive by \(h^{75}\)
after substituting the depressed coordinates as rational functions of
the source coefficients (every weight-15 monomial built from coordinates
of pole/weight ratio \(5\) has denominator \(h^{75}\); \(L=-\lambda/3\)
is holomorphic). After the Backwire peel, that cleared numerator is a
polynomial \(Q\in k[h_0,w_1,a_{42},p_{32},\ldots]\). Writing
\(Q=h_0^{69}\cdot(\text{jet quotient})\) makes
\(h_0^6\rho=(\text{jet quotient})\) a polynomial. The committed pole
lemma then forces every successive head of the jet quotient to vanish
at \(a\):

> If \(h_0^6\rho=A_0\) is polynomial and \(\rho'=j/h_0\), then
> \(A_0(a)=0\)
> (`localLinearPoleSix_head_eval_zero_of_deriv_eq_simplePole610`).

Hypotheses of that lemma that are committed on this face: \(h_0.\mathrm{natDegree}=1\),
\(h_0(a)=0\), and (once the wrapper exists) the simple-pole derivative.
This is a pole identity used only after the square-core linear-root
packet (\(\lambda\neq 0\), \(H=h_0^2\)) is in force.

---

## 2. Question 1: what the tower converges to

### 2.1 Depressed valuations after Backwire

Substitute the Backwire peel into the committed numerators \(Abar,\ldots,Xbar\)
of `derive_610_degree_zero_residual.py`. Every depressed coordinate is
Laurent in \(h_0\) of degree at most \(0\):

| coord | bar min | pole | val | leading bar |
|---|---|---|---|---|
| \(A\) | 10 | 10 | 0 | \(12a_{42}-5w_1^2\) |
| \(B\) | 14 | 15 | \(-1\) | \(54 p_{32}\) |
| \(C\) | 19 | 20 | \(-1\) | \(72(2p_{21}-p_{32}w_1)\) |
| \(D\) | 24 | 25 | \(-1\) | \(27(12p_1-4p_{21}w_1+p_{32}w_1^2)\) |
| \(E\) | 29 | 30 | \(-1\) | \(-216 w_1(36p_1-6p_{21}w_1+p_{32}w_1^2)\) |
| \(P\) | 10 | 10 | 0 | \(2\lambda w_1+4s_2-5w_1^2\) |
| \(Q\) | 14 | 15 | \(-1\) | \(9u_2\) |
| \(S\) | 23 | 25 | \(-2\) | \(216 q_{53}\) |
| \(T\) | 27 | 30 | \(-3\) | \(7776 q_{41}\) |
| \(U\) | 32 | 35 | \(-3\) | \(3888(3q_3-2q_{41}w_1)\) |

(Computed from the committed \(Abar,\ldots,Ubar\) after the peel.
\(V,W,X\) likewise have val \(-3\), heads proportional to
\(w_1(3q_3-q_{41}w_1)\), \(w_1^2(9q_3-2q_{41}w_1)\),
\(w_1^3(6q_3-q_{41}w_1)\).)

In particular \(B=p_{32}/h_0+O(1)\). Vanishing of \(p_{32}(a)\) removes
the pole of \(B\), it does **not** force the depressed sextic to be
\(z^6\), and it does **not** force a root of multiplicity \(\ge 5\) at
\(z=0\): multiplicity \(\ge 5\) at \(0\) would need
\(A=B=C=D=E=0\) at \(a\), but \(A(a)=(12a_{42}-5w_1^2)/12\) is not
forced to \(0\), and after \(p_{32}(a)=0\) one still has the regular
value \(B(a)=w_1(-18a_{42}+5w_1^2)/27+p_{32n}\) in general.

### 2.2 Order-69 head

The only weight-15 monomial of valuation \(-6\) built from the groups
that actually appear in `degreeZeroPrimitive610` and the polar table
above is \(B^3 T_0\). The epsilon group is committed:

\[
\mathrm{degreeZeroEpsilonGroup610}
=\frac{-7A^3B+9A^2D+24ABC+4B^3-36CD}{54},
\]

so \(\varepsilon\cdot(\text{epsilon group})\) contains
\(\frac{2}{27} T_0 B^3\). Substituting \(B=Bbar/(54 h^{15})\) and
\(T_0=Tbar/(7776 h^{30})\) and clearing \(h^{75}\) gives

\[
h^{75}\cdot\frac{2}{27} T_0 B^3
=\frac{2}{27}\,p_{32}^3 q_{41}\, h^{69}+O(h^{70}).
\]

No other committed summand of the primitive reaches valuation \(-6\):
base-group \(B^5\) has val \(-5\); \(U\cdot(\zeta\text{-group})\) has val
\(-5\); subtracted (non-\(T_0\)) terms of `epsilonResidual610` have val
\(\ge -1\) and against \(B^3\) give val \(\ge -4\). Thus, as an identity
of the \(\mathbb{Q}\)-primitive after the committed source substitution,

\[
\bigl(Q/h_0^{69}\bigr)\big|_{h_0=0}
=\frac{2}{27}\,p_{32}^3 q_{41}.
\]

The live integer \(7583143431241728\) satisfies
\(7583143431241728=\frac{2}{27}\cdot 102372436321763328\); it is this
coefficient times the compact \(\mathbb{Z}\)-clearing constant of
`COMPUTE_SOURCE`. Vanishing is independent of that constant. In
characteristic zero,

\[
p_{32}(a)=0\quad\text{or}\quad q_{41}(a)=0.
\]

This matches the quoted live order-69 split.

### 2.3 Meaning of total vanishing at \(a\)

Evaluate the source as \(Y\)-polynomials at \(X=a\). The peel already
gives \(p_6(a)=\cdots=p_2(a)=0\) and \(q_{10}(a)=\cdots=q_4(a)=0\), so

\[
p(a,Y)=p_1(a)\,Y+p_0(a),\qquad
q(a,Y)=q_3(a)\,Y^3+q_2(a)\,Y^2+q_1(a)\,Y+q_0(a).
\]

- \(p_{32}(a)=p_{21}(a)=p_1(a)=p_0(a)=0\) implies in particular
  \(p_1(a)=p_0(a)=0\), hence \(p(a,\cdot)\equiv 0\). Since
  \(h_0.\mathrm{natDegree}=1\), `linearPolynomial_dvd_of_eval_eq_zero_810`
  lifts this to \(h_0\mid p.\mathrm{coeff}\,i\) for every \(i\), i.e.
  \(h_0\) divides \(p\) in \(k[X][Y]\).
- The \(q\)-side analogue \(q_3(a)=q_2(a)=q_1(a)=q_0(a)=0\) (the values
  \(q_{41}(a)=0\) etc. are extra order on already-zero coefficients)
  likewise gives \(h_0\mid q\).

**Two-sided limit.** If \(h_0\mid p\) and \(h_0\mid q\), write
\(p=h_0\tilde p\), \(q=h_0\tilde q\). The Jacobian is

\[
J=p_X q_Y-p_Y q_X
=h_0\bigl(h_0'(\tilde p\,\tilde q_Y-\tilde p_Y\tilde q)+h_0(\cdots)\bigr),
\]

so \(h_0\mid J\). But \(J=C(j)\) with \(j\neq 0\)
(`IsPlaneKellerPair`, last conjunct of
`NormalizedCoprimeLeadingCoreSource`). A nonconstant linear polynomial
cannot divide a nonzero constant. This is `False`.

This is the exact committed contradiction for the *two-sided*
total-vanishing limit. It is not a multiplicity statement about the
depressed sextic.

**One-sided limit.** If only \(p(a,\cdot)\equiv 0\), then at \(X=a\)

\[
J(a,Y)=h_0'(a)\,\tilde p(a,Y)\,q_Y(a,Y)=j.
\]

Here \(h_0'\) is a nonzero constant (\(h_0.\mathrm{natDegree}=1\)),
\(\tilde p(a,\cdot)\) has \(Y\)-degree \(\le 2\) (or \(\le 1\) once
\(p_{21}(a)=0\)), and \(q_Y(a,\cdot)\) has \(Y\)-degree \(\le 2\). Their
product is a nonzero constant, so each factor is (up to scalars) a
monomial of complementary degree, or both are constant. No committed
`LowScale610*` theorem forbids this. The fifteenth-face module
explicitly refuses to claim vanishing of \(p_2,p_1,p_0,q_3\).

The tower is **not** derived to reach two-sided vanishing. After order
69 the chamber splits; the surviving arms of §3 are hypersurfaces, not
the total-vanishing locus.

---

## 3. Question 2: cofactor arms

### 3.1 Frozen polar heads versus Taylor mixins

The pole lemma evaluates a polynomial in the compact coordinates at
\(a\). When a coordinate's *value* at \(a\) is the leading polar
coefficient, frozen evaluation matches the Hahn leading term. Once that
value is pinned to zero, the coordinate's Taylor

\[
p_{32}(X)=p_{32n}\,c^{-1}h_0+O(h_0^2)
\quad(h_0=c(X-a),\ c\neq 0)
\]

feeds the next jet into the same polar slot. Labels \(p_{32n},p_{21n}\)
in the live order-71 nine-term are these next jets, not Lean primes.
The five-term arm's \(q_{41}'\) is the same phenomenon on \(q_{41}\).

### 3.2 Order 70, frozen (no next jets)

On the chamber \(p_{32}=0\), with \(B\) replaced by its regular part
and \(T,U,C,D\) by their still-polar parts, the committed
\(\varepsilon\) and \(\zeta\) channels give

\[
\bigl(Q/h^{70}\bigr)\big|_{p_{32}=0}
= -\frac{p_{21}}{36}\bigl(24 p_1 q_{41}+9 p_{21} q_3-14 p_{21} q_{41} w_1\bigr)
\]

plus terms of order \(\ge 71\). This vanishes if \(p_{21}(a)=0\) *or* a
single linear relation among \(p_1,q_{41},q_3,w_1\). It is **not** the
quoted live disjunction \(p_{21}=0\lor(q_{41}=q_3=0)\). That live
disjunction is UNVERIFIED as an identity of \(Q\); it would require
either next-jet corrections (§3.1) or extra face relations not used
here.

On the chamber \(q_{41}=0\), the same two channels plus
\(S\cdot(\delta\text{-group})\), \(V\cdot(\eta\text{-group})\),
\(W\cdot(\theta\text{-group})\) (the last two using raw \(V_0,W_0\),
hence UNVERIFIED as residual values) produce a bilinear form
\(\alpha\,q_{53}+\beta\,q_3\) whose coefficients still involve
\(a_{42},p_1,p_{21},p_{32},w_1\). This is **not** identical to the quoted
live five-term \(10 p_{32}^2 q_{53}+(18 p_{32} w_1-27 p_{21})q_3\). The
live five-term is UNVERIFIED as a reduction of \(Q\).

Neither frozen head is a unit on its chamber (each is visibly zero on a
hypersurface, e.g. \(p_{21}=0\) on the first arm). They do **not** die
in the 68-terminal style (an identity in \(k[X]\) of incompatible
degrees). They define genuine subvarieties.

### 3.3 Order 71, frozen, on \(p_{32}=p_{21}=0\)

Committed \(\varepsilon,\zeta,\delta\) channels:

\[
\begin{aligned}
&(Q/h^{71})\big|_{p_{32}=p_{21}=0}\\
&\quad=-\frac{p_1}{2592}\bigl(
-432 a_{42}^2 q_{41}-864 a_{42} q_3 w_1+936 a_{42} q_{41} w_1^2
+1080 p_1 q_{53}+240 q_3 w_1^3-235 q_{41} w_1^4\bigr).
\end{aligned}
\]

This is a polynomial in \((a_{42},q_{41},q_3,w_1,p_1,q_{53})\), vanishing
if \(p_1=0\) or the six-term parenthesis vanishes. The live nine-term in
\((p_{32n},p_{21n},a_{42},q_{41},q_3,w_1,p_1,q_{53})\) is the same
object *after* restoring next jets \(p_{32n},p_{21n}\) in the polar slots
of \(B\) and \(C\). That restoration is the correct Taylor object; the
explicit nine coefficients are UNVERIFIED here. In either form the
cofactor is not a unit.

On \(p_{32}=q_{41}=q_3=0\), the frozen order-71 head is

\[
-\frac{5 q_{53}}{432}\bigl(-12 a_{42} p_{21}^2+36 p_1^2-72 p_1 p_{21} w_1+25 p_{21}^2 w_1^2\bigr),
\]

an eight-term-class polynomial in \((q_{53},a_{42},p_{21},p_1,w_1)\).
Again not a unit. Live eight-term residual UNVERIFIED as a coefficient
list.

### 3.4 The \(q_{41}'\) unblock

On \(q_{41}(a)=0\) with \(p_{32}(a)\neq 0\), the order-69 monomial is
zero at \(a\) because of \(q_{41}\). Write \(q_{41}(X)=q_{41}'(a)(X-a)+O((X-a)^2)\),
so \(q_{41}=(q_{41}'(a)/c)\,h_0+O(h_0^2)\). Then

\[
\frac{2}{27}\,p_{32}^3 q_{41}\,h_0^{69}
=\frac{2}{27}\,p_{32}(a)^3 \frac{q_{41}'(a)}{c}\,h_0^{70}+O(h_0^{71}).
\]

The correct order-70 object on this arm is the sum of

1. this first Taylor of the order-69 identity, and
2. the frozen coefficient of \(h^{70}\) in \(Q\) evaluated at \(q_{41}=0\)
   (the \(Tm2\sim q_{53}w_1\) piece \(-5 p_{32}^3 q_{53} w_1/81\), plus
   the \(U,S,\ldots\) channels).

If the frozen piece (2) is used *without* (1), one is computing a
coefficient of \(Q\) as a polynomial in a dummy \(h\) with \(q_{41}\)
held at \(0\) as a constant, which is not the Hahn expansion of the
rational function. That is the mixing obstruction. Differentiating the
order-69 identity in the source variable and then evaluating at \(a\)
is exactly (1), and it unblocks the arm: the head is linear in
\(q_{41}'(a)\) with leading coefficient \(\frac{2}{27}p_{32}(a)^3/c\neq 0\)
on \(p_{32}(a)\neq 0\), plus a frozen remainder. Vanishing solves for
\(q_{41}'(a)\) or forces the remainder to cancel it; it does not by
itself close the chamber.

The same pattern, one derivative later, is the right object at order 71
on the five-term locus.

### 3.5 Uniform death?

No. The 68 terminal closure was an identity in \(k[X]\) whose two
degree cases were both impossible. Here the cofactors are polynomials
in the *values* (and next jets) of compact coordinates at a single
point \(a\). They vanish on positive-codimension loci of those
coordinates. Leading-coefficient exactness of \(p_6=h_0^6\) and
\(q_{10}=h_0^{10}\) does not make any of those polynomials a nonzero
constant. Each arm needs its own continuation of the pole tower
(including next jets).

---

## 4. Question 3: finite bound

### 4.1 The exponent \(T\)

`derive_610_degree_zero_residual.py` clears the native primitive by
\(h^{75}\). This is forced by weight: every depressed coordinate except
\(L\) has pole/weight ratio \(5\), and the primitive is homogeneous of
weight 15, so a residual-free monomial has denominator \(h^{75}\). After
the Backwire peel every compact numerator has `bar_max = pole` (table in
§2.1), so every coordinate has \(h\)-degree \(\le 0\). Therefore

\[
\deg_h Q\le 75.
\]

The base group of the primitive contains the monomial \(B^5\)
(`degreeZeroBaseGroup610`, coefficient \(36864/2239488\)). With
\(B=p_{32}/h+B_0\) this produces an \(h^{75}\) term \(B_0^5\) unless the
degree-zero part of the *full* primitive cancels identically.
Cancellation of that \(h^0\) coefficient is UNVERIFIED, so the exact
value is \(T\le 75\), and \(T=75\) unless that cancellation occurs. The
committed jet-quotient definition is

\[
Q=h^{69}\cdot(\text{jet quotient}),\qquad
\text{jet quotient}=\mathrm{cancel}(Q/h^{69}),
\]

with \(Q\) the \(h^{75}\)-cleared native primitive after the post-collapse
jet of `COMPUTE_SOURCE`. Hence \(\deg_h(\text{jet quotient})\le T-69\le 6\).

### 4.2 What happens at the ceiling

The pole lemma can demand at most seven frozen heads (orders 69 through
75). If all seven vanish as *frozen* polynomials in the numeric values
of the compact coordinates at \(a\), the polynomial
\((\text{jet quotient})(h;\,\text{coords}(a))\) is the zero polynomial
in \(h\). That is not yet \(\rho=0\): the actual rational function uses
\(\mathrm{coords}(X)\), whose Taylor mixins (§3.1) populate lower-order
heads. Each compact coordinate is itself a polynomial in \(X\), so its
Taylor series at \(a\) is finite. After those mixins are exhausted, either
a nonzero Hahn coefficient of \(h_0^6\rho\) remains (and the pole lemma
kills it, continuing the tower) or \(h_0^6\rho\) vanishes to all orders
at \(a\).

A rational function whose numerator vanishes to infinite order at a
simple zero of \(h_0\) is identically zero (\(h_0\) is prime in \(k[X]\)).
Then \(\rho\equiv 0\), so \(\rho'=0\), contradicting \(\rho'=j/h_0\) with
\(j\neq 0\).

This is an a priori finiteness statement, not a closure of the live
arms: it does not exhibit a concrete order at which the nine-term,
eight-term, or five-term cofactor becomes a unit. There is no committed
bound on \(\deg_X\) of the source coefficients \(p_i,q_j\) (only on
\(Y\)-degree and on the leading \(X\)-degrees of \(p_6\) and \(q_{10}\)),
so one cannot quote a numerical vanishing-order ceiling in \(X\) from
landed theorems. The useful bound is the seven frozen \(h\)-heads, plus
finitely many Taylor mixins of the compact coordinates.

---

## 5. What would close the chamber, and what is missing

A referee-checkable closure of the *whole* linear-root chamber would be
one of:

1. two-sided total vanishing forced, then the Jacobian argument of §2.3;
2. every cofactor arm reduced, 68-style, to an identity in \(k[X]\) of
   incompatible degrees, or to a unit built from \(\lambda\neq 0\),
   \(j\neq 0\), or exact leading coefficients;
3. exhaustion of the seven frozen heads plus mixins down to
   \(\rho\equiv 0\).

(1) is a theorem *if* the vanishing is granted; it is not granted by
orders 69–71. (2) fails for the explicit frozen heads of §3: they are
hypersurface equations. (3) is the a priori bound of §4; carrying it
out on the live arms requires the untracked jet/wrapper files and the
next-jet algebra of §3.4.

The source-facing wrapper that instantiates
`degreeZeroPrimitive610_ratFuncDeriv_eq_simplePole` is still untracked
(HANDOFF step after Compact/Jet/CoordinateBridge). Without it the pole
lemma's derivative hypothesis is assembled on paper from committed
factors but is not a landed theorem.

---

## 6. FALLACY-v2 checks

- Pole identity used only on the square-core linear-root face with
  \(h_0.\mathrm{natDegree}=1\), \(\lambda\neq 0\), and (on paper) the
  affine-depress Jacobian \(j/h_0\).
- Floor/attainment: \(\deg_h Q\le 75\) is an upper bound; equality
  \(T=75\) needs non-cancellation of the degree-zero part of the
  primitive (not claimed as landed).
- Prime/derivative: \(p_{32n},p_{21n},q_{41}'\) are Taylor labels of
  source-coefficient polynomials, not Lean primes.
- Raw remainder: heads are taken in the polynomial ring of the dummy
  \(h\) after `cancel`, branched on vanished leaders \(p_{32},q_{41},\ldots\),
  with the zero polynomial handled as the ceiling case of §4.2.
- No flag/place/series identification; no exit-price assertion.

No `charge_basis` line: nothing here is a new exit-price claim.
)
