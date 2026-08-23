# Rank-1 landing experiment: approximate-root packets and the GGV-to-Sigray gap

**Date:** 2026-08-23  
**Target:** the remaining corner/packet-to-decorated-tree part of `REDUCTION.md`
G2 / `TRANSPORT.md` Conjecture T  
**Inputs read:** `xmodel/sol-connections.md` rank 1, `REDUCTION.md` G2,
and `TRANSPORT.md`, with the relevant definitions checked against Sigray
Sections 3--5.  
**Status convention:** **EXACT** means proved here by an explicit calculation
or follows formally from the cited definitions. All new Keller-specific
coverage assertions are labelled **CONJECTURE**.

## 0. Verdict

The rank-1 idea has a precise formulation, but the data proposed in
`sol-connections.md` (1.2) are not yet sufficient to define the desired
functor.

The decisive distinction is:

1. A **complete residual approximate-root system** for every infinity place
   of the fiber does determine the Eggers--Wall tree and all the local Sigray
   decorations. This is essentially the Newton--Puiseux/approximate-root
   reconstruction, expressed invariantly by rank-two flags.
2. A finite GGV packet chain carrying only
   \(\widehat\nu_\lambda(f),\widehat\nu_\lambda(g),
   \widehat\nu_\lambda(h_j)\), discrepancy, and local pencil-ideal orders
   does **not** contain that complete residual system. It forgets the full
   residual polynomials, their unselected roots, the other infinity chart,
   zero/axis roots, and whether every pole-carrying branch has appeared.
3. Even a complete cusp tower along one packet determines only that packet's
   Eggers--Wall segment. A lower term invisible on the segment can create
   poles on a different component of the same fiber tree. Section 4 gives an
   exact two-model separation.
4. The untwisted symplectic residue does not fill the loss: it is zero once a
   Keller boundary place is chosen and cannot discover an omitted place. The
   boundary-twisted residue remains a consistency functional on an already
   chosen flag.

Thus the answer to the key test is **NO for the proposed finite enriched
packet**, and **YES only after replacing it by a fiber-tagged, two-chart,
all-root residual forest**. The latter replacement makes the local
packet-to-tree map exact, but leaves one genuinely new global assertion:

> **CONJECTURE PSC (pole-skeleton capture).** The complete eligible GGV packet
> forest of the selected polynomial Keller pair reaches every flag in the
> Sigray pole skeleton, in both infinity charts, with the correct full
> residual initial forms.

PSC is the minimal landing lemma. If PSC is proved, the remaining construction
in this note proves `TRANSPORT.md` Conjecture T at the pole-skeleton strength
needed by the sheet compiler. Nothing presently proves PSC. The worked family
shows that the local compiler is correct; its hidden-tail variant shows why
PSC cannot be replaced by a statement about one cusp chain.

Accordingly this route is **VIABLE-CONDITIONAL as a G2 program and a very good
interface experiment, but it is not presently a G2 theorem**. It isolates the
missing lemma rather than proving it.

One scope correction is important. Closing PSC would repair the
GGV-to-decorated-sheet arrow. It would not by itself prove the independent
full-configuration book coverage, off-axis termination, or an upper bound on
topological degree listed later in `REDUCTION.md`.

---

## 1. What the desired factorization actually is

Let \((P,Q)\) be the selected **pre-Laurent polynomial** GGV pair. Apply the
component sorting \(C\) and signed source rotation \(R\) of `TRANSPORT.md` and
write

\[
 (f,g)=C\circ(P,Q)\circ R.
 \tag{1.1}
\]

`TRANSPORT.md` proves that this is the same polynomial Keller pair, in a
Sigray-normalized frame, with the GGV valuation ledger exactly recoverable.
No post-Laurent \([P,Q]=x^2\) object is used below.

For a fixed fiber value \(a\in\mathbf C\), there is an **EXACT** construction

\[
 \mathsf{Pair}^{\rm GGV}_a
 \xrightarrow{\ C,R\ }
 \mathsf{Pair}^{\rm Sig}_a
 \xrightarrow{\ \mathrm{NP}\ }
 \mathsf{EW}^{\rm dec}_a .
 \tag{1.2}
\]

Here the last arrow means: compute all Newton--Puiseux expansions of
\(f-a=0\) at the two points at infinity, glue them by contact order, and
evaluate \(g\) and Sigray's approximate roots on the resulting flags. The
output is canonical up to the root-of-unity/conjugation identifications in
the Puiseux presentations. This uses the **whole polynomial pair**. It does
not say that a finite GGV corner ledger determines the output.

G2 asks for a factorization of (1.2) through GGV packet data:

\[
 \mathsf{Pair}^{\rm GGV}_a
 \longrightarrow \mathsf{Pkt}^{\rm AR}_a
 \mathrel{\mathop{\dashrightarrow}^{?}}
 \mathsf{EW}^{\rm dec}_a .
 \tag{1.3}
\]

The experiment is to define \(\mathsf{Pkt}^{\rm AR}_a\) so that the dashed
arrow is a genuine, finite, choice-independent map without defining the
packet to be a disguised copy of the answer.

### 1.1 Flags and full residual forms

Let an exact GGV cut prefix produce a divisorial valuation \(\nu_E\) and let
\(\lambda\) be a selected closed point of its residue divisor. Pull the flag
back through the exact prefix and, in a Kummer chart, restrict the full deck
orbit to \(\mathbf C(x,y)\), exactly as in `sol-wtc1-round2.md` Theorem 2.1.
The result is an intrinsic rank-two flag valuation

\[
 \widehat\nu_\lambda(H)=
 \left(\nu_E(H),
       \operatorname{ord}_{\lambda}\operatorname{res}_{\nu_E}(H)
 \right).
 \tag{1.4}
\]

This flag canonically names an Enriques point sequence. That part is already
proved. For tree reconstruction, however, (1.4) is too small: it stores the
order of one residual germ at one root, not the residual polynomial itself.

Let \(X_E\) be the pole coordinate (\(x\) on Sigray's \(y\)-side and \(y\)
on its \(x\)-side). In a normalized root coordinate \(\eta\), define

\[
 d_E(H)=\frac{\nu_E(H)}{\nu_E(X_E)},\qquad
 p_{H,E}(\eta)=\operatorname{in}_{\nu_E}
       \bigl(X_E^{-d_E(H)}H\bigr).
 \tag{1.5}
\]

Fractional exponents are interpreted in the retained Kummer presentation;
the full conjugacy orbit is then descended. Formula (1.5) is precisely the
information denoted \(d_{h,F},p_{h,F}\) in Sigray's chart language. It must be
retained with its coefficient and factorization, up to the known root-coordinate
action. The pair of integers in (1.4) can be recovered from (1.5), but not
conversely.

### 1.2 The enriched packet record

At a packet flag \(\omega=(E,\lambda)\), the candidate record is

\[
\begin{aligned}
 \mathcal P_\omega(a)=\big(&
   \text{exact prefix and inverse field maps};
   \text{full root/deck orbit};\\
 & \pi_\omega,\kappa_\omega,\nu_\omega;
   d_\omega(H),p_{H,\omega}\quad
      (H=f-a,f,g,h_1,\ldots,h_m);\\
 & (k_j,l_j,s_j)_{j<m};
   A(E),\mathcal I_f,\mathcal I_g;
   \text{predecessor flag IDs}\big).
 \tag{1.6}
\end{aligned}
\]

At a vertex admitting more than one Puiseux presentation, \(\kappa_\omega\)
in (1.6) uses the audit-forced Q/jump/max convention; otherwise
\(D_{H,F}=\kappa_Fd_{H,F}\) need not be integral. This convention is part of
the output type, not a presentation choice left to the compiler.

The distinctions inside (1.6) are load-bearing.

- Both \(f-a\) and \(f\) occur. The former selects the branches of the
  specified fiber. On the positive/pole part of the tree it has the same
  leading form as \(f\), while at a zero crossing the constant \(a\) changes
  the residual polynomial.
- The actual \(p_{H,\omega}\), not only its degree or its order at \(\lambda\),
  is retained.
- Every root orbit is retained. The current nonzero-root packet convention
  is insufficient for a universal tree functor unless every zero/axis root is
  separately re-certified.
- \(A(E)\) and the weak projective pencil ideals certify the center and retain
  polynomial-origin information. They do not reconstruct unvisited residual
  roots or an omitted infinity chart.

### 1.3 The approximate-root tower

Put \(h_0=g\) on the positive tree. If at a flag

\[
 (h_{j,\omega}^{+})^{k_j}
   =s_j(f_\omega^{+})^{l_j},qquad
 \gcd(k_j,l_j)=1,\quad s_j\ne0,
 \tag{1.7}
\]

define the normalized successor

\[
 h_{j+1}=h_j^{k_j}-s_j f^{l_j}.
 \tag{1.8}
\]

Stop at the first index at which (1.7) fails, equivalently at the first
nonzero leading Jacobian in the nondegenerate positive-tree setting. This is
Sigray Proposition 4.2's tower. Its known constant-leading-part gap is avoided
here by restricting the claimed compiler to pole segments, where the leading
parts used below are nonconstant.

An approximate root created on an ancestor may still be evaluated at a later
flag after the local tower has stopped. Such an inherited \(h_j\) is a useful
residual probe, but it is not counted as an entry of the later flag's local
Sigray tower. This distinction is used in (4.19).

For a sorted rectangular cusp

\[
 f_+=cH^\alpha,\qquad g_+=dH^\beta,qquad
 1<\alpha<\beta,\quad \gcd(\alpha,\beta)=1,
 \tag{1.9}
\]

the first relation has \((k_0,l_0)=(\alpha,\beta)\) and

\[
 h_1=g^\alpha-\frac{d^\alpha}{c^\beta}f^\beta.
 \tag{1.10}
\]

Up to a nonzero scalar this is exactly the cusp kernel
\(d^\alpha f^\beta-c^\beta g^\alpha\) isolated by the JvdK calculation. The
JvdK theorem says that no target **coordinate** can have this initial
cancellation. There is no conflict: \(h_1\) is deliberately a non-coordinate
polynomial. Its role is not degree descent; it exposes the next residual
layer.

### 1.4 Candidate packet-to-tree algorithm

Given records (1.6) for a fiber \(a\), define \(\mathfrak T_a\) as follows.

1. Start in both infinity charts and at every certified axis/zero packet.
2. For each node, factor the full residual polynomial
   \(p_{f-a,\omega}\). Extend the flag through **every** root orbit and pull
   each successor back to the original plane.
3. Identify two presentations exactly when their intrinsic rank-two flags
   have the same finite Enriques point sequence. Order successors by proper
   extension of that sequence. This gives the adjacency and proximity data
   without chart-dependent root-token matching.
4. Record the first exponents at which the value-group index drops and at
   which two residual branches separate. These give the characteristic and
   contact vertices; gluing by these exponents is the Eggers--Wall tree.
5. Run (1.7)--(1.8) at every positive node. On each branch, the first node
   with tower length \(m_F=0\), after a nonzero-length predecessor segment,
   is the Sigray threshold \(F_P^*\). It is a pole vertex precisely when
   \(d_F,d_{g,F}>0\). Retain the entire rooted subtree spanned by these
   vertices.
6. Emit, at every retained vertex,
   \[
   \pi(F),\ \kappa_F,\ \nu_F,\ d_F,\ d_{g,F},\
   p_F,\ p_{g,F},\ (h_j,k_j,l_j,s_j).
   \tag{1.11}
   \]
   At a pole emit
   \[
   D_F=\kappa_Fd_F,\quad D_{g,F}=\kappa_Fd_{g,F},\quad
   \bar\kappa_F=\kappa_F(1-\pi(F)),
   \tag{1.12}
   \]
   \[
   M_F=\gcd(\deg p_F,\deg p_{g,F})\quad(m_F=0),\qquad
   \Lambda(F)=\frac{D_{g,F}\deg p_F}{\nu_F}.
   \tag{1.13}
   \]
7. Attach the placewise fiber residue
   \(\operatorname{Res}(y\,dx)\) or \(\operatorname{Res}(x\,dy)\). If an
   independently certified strip chart exists, attach its boundary-twisted
   reconstruction residue. Neither residue is used to create a missing node.

**EXACT conditional statement.** If (1.6) is supplied at every node of a
two-chart all-root Newton--Puiseux forest through every pole threshold, Steps
1--7 determine the fiber-tagged decorated Sigray pole skeleton uniquely up to
decorated rooted-tree isomorphism. This is because the branch series and
pairwise contact orders define the Eggers--Wall tree, while (1.11)--(1.13)
are evaluations and definitions on its flags.

The word “if” contains the whole unresolved G2 content.

---

## 2. The information-sufficiency test

### 2.1 What complete approximate roots do determine

For one reduced plane curve germ, a complete characteristic/approximate-root
system with all residual factors determines its embedded equisingularity
type. For a fiber \(f-a=0\), doing this in both infinity charts and retaining
pairwise contacts determines its Eggers--Wall forest. Evaluating a specified
second polynomial \(g\) and the tower \(h_j\) at every resulting flag then
determines pole/finite status and the Sigray numerical decorations.

Thus there is no local mystery after the **complete residual system** is in
hand. The problem is that a GGV admissible chain is not presently proved to
be such a system.

### 2.2 Why the values in the rank-1 proposal are insufficient

The datum

\[
 \bigl(\widehat\nu_\lambda(f),\widehat\nu_\lambda(g),
       \widehat\nu_\lambda(h_1),\ldots\bigr)
 \tag{2.1}
\]

does not determine \(p_{f-a,F}\) or \(p_{g,F}\). It gives only one order at
one selected residual point. In particular it does not determine:

- all roots and their multiplicities;
- root-of-unity orbits and the number of geometric places;
- the next unselected tangent directions;
- pairwise contacts between different places;
- residual pattern polynomials consumed by Sigray's merge calculus; or
- coefficients \(s_j\) needed to compare towers at adjacent vertices.

Degrees do not repair this loss. Two squarefree polynomials of the same
degree can have different root configurations relative to the residual
polynomial of the other component, while giving the same value at the one
marked root.

### 2.3 The exact global loss

Even the full residual germ along one flag is local. Dicritical decoration is
a statement about all infinity places of the fiber and the value of \(g\) at
each place. A term that is lower order at one boundary component can be the
dominant pole term at another. Therefore no one-packet tower can decide the
number of pole vertices or the global pole mass.

This is not repaired by the log discrepancy or by the two weak pencil ideals
at the selected point. Those data control that center. They do not certify
that every other center has been visited.

There is one important typing fork here. If “retain the ideals” means retain
only their local base-ideal/order data, the preceding objection applies. If
it means retain the complete marked polynomial generators with their exact
inverse coordinate maps, then the packet has effectively reinserted the whole
polynomial pair; one can use (1.2), but this no longer proves that the finite
GGV packet data themselves determine the tree.

The fiber tag is also essential. The tree is the tree of \(f-a\), not of the
top form of \(f\). Special values of \(a\) can change the number and contacts
of branches without changing the GGV rectangle or global cusp remainder.

### 2.4 Why the symplectic residue cannot restore the loss

For a Keller pair the untwisted action form is globally exact, so its
divisorial residues vanish on every resolution. The per-fiber residue is a
coefficient pin **after** a place and a parameter have been supplied. It has
no operation that enumerates places. The boundary-twisted strip residue also
requires the flag, toric twist, and strip support in advance; it is exactly a
consistency test on that richer object.

Consequently residues can reject or constrain an emitted edge. They cannot
make the finite packet forest surjective onto the pole skeleton.

---

## 3. Why the live `(8,28)` record cannot perform the requested test

The live pre-Laurent record has

\[
 A_0=(8,28),\qquad (m,n)=(3,2),\qquad
 (\deg P,\deg Q)=(108,72),
 \tag{3.1}
\]

and `TRANSPORT.md` carries it to a type-\((2,3)\) Sigray frame with corners
\((56,16),(84,24)\). This is an exact support/valuation fixture. It is not an
explicit polynomial Keller pair: no coefficients, fibers, or realization are
known. Therefore one cannot compute any of

\[
 p_{f-a,F},\quad p_{g,F},\quad
 \operatorname{Roots}(p_{f-a,F}),\quad
 O(P,P^*),\quad T_{a,\mathrm{pole}}
 \tag{3.2}
\]

from that record. Producing an Eggers--Wall tree for (3.1) would silently
invent the missing coefficients. This is not a computational inconvenience;
it is precisely the information-sufficiency failure under test.

The correct exact experiment is therefore an explicit rectangular cusp
family in the ambient GGV normal-form class. It tests the proposed compiler
without claiming a counterexample realization.

---

## 4. Worked GGV cusp family

### 4.1 The pair and its status

Put

\[
 H=x^2y^3,\qquad
 f=H^2-x=x^4y^6-x,\qquad
 g=H^3-2x^2y=x^6y^9-2x^2y.
 \tag{4.1}
\]

The supports lie in the proportional rectangles

\[
 \operatorname{Supp}f\subset[0,4]\times[0,6],\qquad
 \operatorname{Supp}g\subset[0,6]\times[0,9],
 \tag{4.2}
\]

with northeast corners \(2(2,3)\) and \(3(2,3)\). The ordinary leading pair is

\[
 f_+=H^2,\qquad g_+=H^3.
 \tag{4.3}
\]

Thus (4.1) is an exact type-\((2,3)\) GGV rectangular-cusp control with
positive base \(A=(2,3)\).

It is **not** a Keller pair:

\[
 [f,g]=-9x^6y^8+16x^5y^6+2x^2.
 \tag{4.4}
\]

Accordingly this section proves the information and reconstruction claims in
the ambient cusp class. It does not realize a GGV counterexample or prove a
Keller-specific restriction.

Fix \(a\in\mathbf C^*\) and write \(C_a=\{f=a\}\). Its projective equation is

\[
 X^4Y^6-XZ^9-aZ^{10}=0.
 \tag{4.5}
\]

### 4.2 The complete Eggers--Wall forest

At \([1:0:0]\), put \(u=Z/X\), \(v=Y/X\). Equation (4.5) becomes

\[
 v^6-u^9-au^{10}=0.
 \tag{4.6}
\]

It has three geometric branches. With \(\zeta^6=1\), their conjugate
parametrizations are

\[
 u=t^2,\qquad
 v=\zeta t^3(1+at^2)^{1/6},
 \tag{4.7}
\]

where \(\zeta\) and \(-\zeta\) give the same place. In affine coordinates,

\[
 x=t^{-2},\qquad
 y=\zeta t(1+at^2)^{1/6}
   =\zeta x^{-1/2}\left(1+\frac a6x^{-1}+\cdots\right).
 \tag{4.8}
\]

Every branch has Puiseux characteristic \((\kappa,\beta_1)=(2,1)\).
Distinct geometric branches first differ at exponent \(1/2\). Hence the
\(y\)-side Eggers--Wall component is

\[
 (0,y)\;\longrightarrow\;
 F_y\ (\pi=1/2,\ \nu=2)
 \;\substack{\longrightarrow P_1\\[-1mm]
              \longrightarrow P_2\\[-1mm]
              \longrightarrow P_3}.
 \tag{4.9}
\]

The displayed vertex is simultaneously the characteristic and separation
vertex.

At \([0:1:0]\), put \(s=X/Y\), \(u=Z/Y\). The equation is

\[
 s^4-su^9-au^{10}=0.
 \tag{4.10}
\]

There are two geometric branches. For \(c^4=a\), with \(c\sim-c\),

\[
 y=t^{-2},\qquad
 x=ct^3+\frac{1}{4c^2}t^6+\cdots
   =c y^{-3/2}+\frac{1}{4c^2}y^{-3}+\cdots .
 \tag{4.11}
\]

Each has characteristic \((2,3)\), and the two places separate at exponent
\(3/2\). Thus

\[
 (0,x)\;\longrightarrow\;
 F_x\ (\pi=3/2,\ \nu=2)
 \;\substack{\longrightarrow Q_1\\[-1mm]
              \longrightarrow Q_2}.
 \tag{4.12}
\]

Equations (4.9) and (4.12) are the complete fiber-tagged Eggers--Wall forest
for \(a\ne0\).

### 4.3 The cusp remainder detects the pole breakpoint

Along the common \(y\)-side trunk, let \(0\le u<1/2\) and put
\(\eta=x^u y\). Then

\[
 f=x^{4-6u}\eta^6-x,qquad
 g=x^{6-9u}\eta^9-2x^{2-u}\eta.
 \tag{4.13}
\]

Therefore

\[
 f^+=x^{4-6u}\eta^6,qquad
 g^+=x^{6-9u}\eta^9,qquad
 (g^+)^2=(f^+)^3.
 \tag{4.14}
\]

The first approximate root is

\[
\begin{aligned}
 h_1=g^2-f^3
   ={}&3x^9y^{12}-4x^8y^{10}-3x^6y^6\\
     &+4x^4y^2+x^3.
 \tag{4.15}
\end{aligned}
\]

For \(u<1/2\), its leading form is

\[
 h_1^+=3x^{9-12u}\eta^{12}.
 \tag{4.16}
\]

The exponent vector of (4.16) is not a multiple of that of \(f^+\): twice
the latter has \(x\)-exponent \(8-12u\), not \(9-12u\). Hence the tower has
length exactly one on the open trunk.

At \(F_y\), put \(\eta=x^{1/2}y\). The full initials are

\[
 f=x(\eta^6-1),\qquad
 g=x^{3/2}(\eta^9-2\eta),
 \tag{4.17}
\]

so

\[
 d_F=1,\quad p_F=\eta^6-1,qquad
 d_{g,F}=\frac32,\quad p_{g,F}=\eta^9-2\eta.
 \tag{4.18}
\]

The two initials in (4.17) are no longer powers of one polynomial. Thus the
tower length drops from one to zero exactly at \(F_y\). Evaluating the global
cusp remainder there gives

\[
 p_{h_1,F}=(\eta^9-2\eta)^2-(\eta^6-1)^3
 =3\eta^{12}-4\eta^{10}-3\eta^6+4\eta^2+1.
 \tag{4.19}
\]

This is the desired local mechanism: the non-coordinate cusp remainder sees
the residual term \(-2x^2y\) precisely when it reaches the characteristic
flag, and that term breaks the common-power relation.

### 4.4 The decoration is forced

At \(F_y\),

\[
 \kappa_F=2,\qquad \nu_F=2,qquad
 D_F=2,\qquad D_{g,F}=3,qquad
 \bar\kappa_F=2(1-1/2)=1.
 \tag{4.20}
\]

Both residual polynomials are squarefree and coprime:

\[
 \gcd(\eta^6-1,\eta^9-2\eta)=1.
 \tag{4.21}
\]

Indeed, a common nonzero root would satisfy \(\eta^6=1\) and \(\eta^8=2\),
hence \(\eta^2=2\) and then \(\eta^6=8\), a contradiction. Their derivatives
also have no common factor with the respective polynomial: the zero root of
\(p_g\) has derivative \(-2\), and at a nonzero root \(\eta^8=2\) the
derivative is \(9\eta^8-2=16\).

The polynomial identities and coprimality assertions were also replayed over
\(\mathbf Q\) in the installed exact Singular engine. It returned

    h1_minus_expected: 0
    residual_h1: 3e12-4e10-3e6+4e2+1
    gcd_pf_pg: 1
    gcd_pf_derivative: 1
    gcd_pg_derivative: 1

The six roots of \(p_F\) fall into three \(\nu_F=2\) conjugacy orbits, exactly
the three places in (4.9). Along each place, (4.8) gives

\[
 g=(\zeta^9-2\zeta)t^{-3}+O(t^{-1}),
 \tag{4.22}
\]

and \(\zeta^9-2\zeta=\zeta(\zeta^2-2)\ne0\). Thus all three places have
\(g\)-pole order three. On the two places in (4.11), \(H=x^2y^3\) is finite
and \(x^2y\to0\), so \(g\) is finite. Consequently \(F_y\) is the unique pole
vertex and represents all three pole places.

Every requested local decoration is now forced:

\[
\boxed{
 (\alpha,\beta)=(2,3),\quad
 (D_F,D_{g,F})=(2,3),\quad
 (\deg p_F,\deg p_{g,F})=(6,9),
}
 \tag{4.23}
\]

\[
\boxed{
 \nu_F=2,\quad M_F=\gcd(6,9)=3,\quad
 \bar\kappa_F=1,\quad
 \Lambda(F)=\frac{3\cdot6}{2}=9.
}
 \tag{4.24}
\]

The mass agrees with the direct place calculation \(3+3+3=9\). Notice that
this control even satisfies the local simple-root/disjoint-root pattern used
at a Sigray pole. Its failure to be Keller is global and already displayed in
(4.4).

### 4.5 Symplectic residue check

On a pole place, (4.8) gives

\[
 y\,dx=-2\zeta t^{-2}(1+at^2)^{1/6}\,dt.
 \tag{4.25}
\]

Only even increments occur after the leading \(t^{-2}\), so there is no
\(t^{-1}dt\) term:

\[
 \operatorname{Res}_{P_i}(y\,dx)=0\qquad(i=1,2,3).
 \tag{4.26}
\]

The placewise no-log selector therefore passes. It neither creates the three
places nor distinguishes the pole vertex; all of those were fixed before the
residue was evaluated. Since (4.1) is not Keller, (4.26) is a control
calculation, not an application of global action exactness.

### 4.6 Exact hidden-tail separation

Now keep \(f\) fixed and set

\[
 g_\tau=g+\tau y^9,qquad \tau\in\mathbf C^*.
 \tag{4.27}
\]

The added monomial lies in the same GGV rectangle, and the northeast leading
form remains \(H^3\). On every flag of the selected \(y\)-side cusp trunk
\(0\le u\le1/2\), it has exponent \(-9u\), strictly below the terms used in
(4.13)--(4.19). Therefore \((f,g)\) and \((f,g_\tau)\) have on that entire
packet segment the same:

- rectangular cusp and type \((2,3)\);
- rank-two leading values of \(f,g,h_1\);
- full residual polynomials (4.18)--(4.19);
- tower-length transition \(1\to0\);
- pole decoration (4.23)--(4.24); and
- placewise residue (4.26).

But on each of the two \(y=\infty\) places (4.11),

\[
 \tau y^9=\tau t^{-18}.
 \tag{4.28}
\]

Thus \(g_\tau\) has a pole of order eighteen at both places where \(g\) was
finite. The Eggers--Wall topology of \(f-a\) is unchanged, but its dicritical
decoration changes from one pole vertex/three pole places to additional poles
on the other component. All data on the selected cusp packet remain
unchanged.

This proves the exact ambient non-injectivity:

> **EXACT SEPARATION.** A complete approximate-root tower on one GGV cusp
> packet, even with its full local residual polynomials and residue label,
> does not canonically determine the global dicritical decoration.

The two pairs are not Keller pairs, so this does not refute a theorem stated
only on the hypothetical Keller locus. It proves that such a Keller theorem
must use a global coverage/polynomial-origin assertion not contained in the
local cusp data. That required assertion is PSC.

For completeness, the same \(f\) also shows why the fiber tag cannot be
dropped. At \(a=0\),

\[
 f^{-1}(0)=\{x=0\}\cup\{x^3y^6=1\},
 \tag{4.29}
\]

and the \(x\)-side branch/contact structure differs from the generic
two-branch characteristic vertex (4.12), although the global GGV rectangle
and cusp remainder are unchanged.

---

## 5. The minimal lemma

Let \(T^{\rm pole}_a\) denote the smallest rooted subforest of Sigray's
Eggers--Wall tree containing both roots, every pole vertex, and every
characteristic or merge vertex on a path from a root to a pole vertex. This,
not every finite branch of \(f-a\), is the minimal object needed to emit the
pole entries and their ancestry.

Let \(\Omega^{\rm GGV}_a\) be a proposed factor-expanded packet forest formed
from the selected pre-Laurent polynomial pair, retaining exact prefix maps,
both infinity charts, all nonzero root orbits, and separately certified
zero/axis roots. Each occurrence has the intrinsic flag ID of (1.4) and the
full record (1.6).

> **CONJECTURE PSC (pole-skeleton capture; minimal G2 lemma).** For every
> fiber \(a\) of the selected GGV-minimal polynomial Keller pair:
>
> 1. for every infinity place \(P\) with \(g(P)=\infty\),
>    \(\Omega^{\rm GGV}_a\) contains a finite occurrence path whose intrinsic
>    flags are exactly all characteristic/merge predecessors through the
>    Sigray threshold \(F_P^*\);
> 2. at each such occurrence, the descended residual forms of
>    \(f-a,f,g,h_j\) agree, up to the recorded root-coordinate/deck action,
>    with Sigray's \(p_{f-a,F},p_F,p_{g,F},p_{h_j,F}\); and
> 3. quotienting occurrences by intrinsic flag ID introduces no missing or
>    spurious adjacency and terminates in the finite forest
>    \(T^{\rm pole}_a\).

Clause 2 is an exact chart calculation once the occurrence and all field maps
exist. Clause 3's no-double-counting half follows from the canonical Enriques
IDs. The hard new content is Clause 1: **surjectivity onto every pole path**,
including the other chart and zero/axis paths. It is therefore reasonable to
regard Clause 1, with the residual-fidelity interface stated explicitly, as
the one minimal mathematical lemma.

### Theorem 5.1 (PSC closes the corner-to-tree arrow)

**EXACT conditional theorem.** Assume PSC. Then Steps 1--7 of Section 1.4
define a total, choice-independent map

\[
 \mathcal F_a^{\rm AR}:
 \Omega^{\rm GGV}_a/\!\sim_{\rm flag}
 \longrightarrow T^{\rm pole}_a
 \tag{5.1}
\]

which is an isomorphism of rooted forests onto the pole skeleton and preserves

\[
 \pi,\kappa,\nu,d,D,p,\deg p,
 (k_j,l_j,s_j),M,\bar\kappa,
 \text{pole tags},\Lambda,
 \tag{5.2}
\]

as well as the attached placewise/twisted residue wherever defined.

**Proof.** PSC(1) gives surjectivity on the pole-spanned vertex and edge set.
PSC(2), Sigray's definitions, and (1.7)--(1.13) give every decoration in
(5.2). Equality of intrinsic flags gives the same Enriques point sequence,
so the quotient neither duplicates vertices nor depends on a fan, Kummer
presentation, root coordinate, or graph resolution. PSC(3) gives adjacency
and termination. The residue is an evaluation at an already matched flag,
so it is preserved by the exact chart transport. \(\square\)

### 5.2 Why PSC is genuinely new

None of the available ingredients implies PSC.

- `TRANSPORT.md` transports the pair and ledger but expressly does not claim
  residual cancellation, pole status, or tree decoration.
- JvdK excludes cusp cancellation by a target coordinate; it licenses the
  non-coordinate remainder but gives no branch coverage.
- The rank-two valuation theorem makes each emitted flag canonical; it does
  not prove that all pole flags are emitted.
- Classical approximate-root/Eggers--Wall theory reconstructs the tree from
  a complete residual system; it does not identify the GGV eligible chain
  with that complete system.
- Discrepancy and weak pencil ideals live at an emitted center. KPC concerns
  concentration at such a center, not surjectivity over the boundary.
- Symplectic residues constrain a chosen place and are silent about omitted
  places.

The hidden-tail pair (4.27) is the exact warning: local fidelity without
global capture is not enough.

---

## 6. Operational verdict

The rank-1 route should be retained, but with its claim narrowed and its
packet schema strengthened.

1. **Do not call the integer tuple (2.1) an approximate-root transport
   functor.** It is a flag label and a collection of selected orders.
2. **Promote full residual forms to first-class packet fields:**
   \(p_{f-a},p_f,p_g,p_{h_j}\), their coefficients, factorization, and full
   deck/root orbits.
3. **Run two charts and certify zero roots.** A nonzero-root-only chain cannot
   be a universal pole-skeleton compiler.
4. **Use intrinsic flag/Enriques IDs for gluing.** This part is already
   theorem-level and solves presentation dependence/no-double-counting.
5. **Treat the symplectic residue as an edge check, never as coverage.** The
   twisted residue can validate a matched strip edge; the untwisted residue
   cannot discover one.
6. **Aim directly at PSC.** Any weaker lemma confined to one complete GGV
   chain is refuted as a global information principle by (4.27).

The best honest classification is:

\[
\boxed{
 \text{local enriched-packet}\to\text{decorated EW segment: EXACT};
}
\]

\[
\boxed{
 \text{finite GGV packet values}\to\text{global dicritical tree: NO};
}
\]

\[
\boxed{
 \text{all GGV packets cover the Sigray pole skeleton: CONJECTURE PSC}.
}
\]

This is a useful landing result even though it is negative: it identifies the
exact information gap and reduces the remaining G2 theorem to one
surjectivity/fidelity statement, rather than an undefined appeal to “the
cusp tower.”
