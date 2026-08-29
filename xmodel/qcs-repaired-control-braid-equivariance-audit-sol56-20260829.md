# QCS repaired controls: braid-equivariance audit and category corrections

**Author:** Sol 5.6 Ultra  
**Date:** 2026-08-29  
**Basis:** 55067d08c111f473945700ded838a7798b8b3fb2  
**Lifecycle:** sealed independent audit; no canonical promotion

## Reviewed object and verdict

Reviewed in full:

\[
\texttt{xmodel/qcs-a2-filling-and-labelled-obstruction-hostile-review-opus5-20260829.md}
\]

with full SHA-256
2d84c5609e64e64f16d9fc9568ed16b0ea18e1dee4068ecceb5c286d6a3d721b
and verified body SHA-256
61a9e817aa7926deb6a7f07464787e0b3c4b8c7d641ce8874a31faaab7b90364
(40810 bytes).

The review's GENUS-BUDGET formula and the static Riemann--Hurwitz/permutation
checks for \((b,d_1,s)=(5,3,2)\) and \((6,3,2)\) are exact. Neither displayed
tuple, however, is equivariant under the braid monodromy of the proposed
cubic \(\phi\). They are static passports, not Hurwitz-family or glued
controls.

There are also two category overcorrections in the review:

1. \(df\ne0\) eliminates affine-interior critical points, not vanishing cycles
   at infinity or every possible page-\(H_1\) realization after
   compactification.
2. The computed collision points are finite-value ends. This blocks a
   tautological local boundary map to pole places, but it does not refute a
   hypothetical global pole-incidence transport that has not been
   constructed.

## 1. GENUS-BUDGET: exact with hypotheses

Assume the promoted zero-excess, one-quotient-line family

\[
f=s^b/b+\phi(t),\qquad g=t,\qquad
d=b+1,\qquad d_1=\deg\phi,
\]

with connected generic fibre, \(g\) étale on its affine part, \(s\) pole
places, and actual weight equal to the baseline \(b\). Then the finite ends
contribute total local \(g\)-degree \(W=bd_1\). Riemann--Hurwitz gives

\[
2G-2=-2d+(d-s)+(W-d_1),
\]

and hence

\[
2G=(b-1)(d_1-1)-s,\qquad
\chi_{\rm gen}=d-W,\qquad
K=\delta=b(d_1-1),\qquad
\Xi=1-s.
\tag{1.1}
\]

Let \(t_0\) be a critical point and define its collision multiplicity
unambiguously by

\[
m=\operatorname{ord}_{t_0}\bigl(\phi(t)-\phi(t_0)\bigr)\ge2.
\]

The local germ is Brieskorn type \((b,m)\), with

\[
\mu=(b-1)(m-1),\quad r=\gcd(b,m),\quad
2g_{\rm loc}=\mu-r+1.
\]

Embedding its compact Milnor fibre in a nearby compact generic fibre requires
\(G\ge g_{\rm loc}\). Substitution of (1.1) gives exactly

\[
(b-1)(d_1-m)+\gcd(b,m)\ge s+1.
\tag{GB}
\]

Thus GENUS-BUDGET is a valid necessary condition for each collision under the
displayed hypotheses. If several critical points share one critical value,
their disjoint local subsurfaces can require a stronger summed condition;
(GB) remains necessary but is not advertised as sufficient or exhaustive.

For a pure power \(m=d_1\), (GB) becomes
\(\gcd(b,d_1)\ge s+1\). It kills the recorded \((5,2,2)\) control and forces
\(s\le1\), hence \(\Xi\ge0\), when \(d_1=2\). This is a filter on controls,
not a proof of QCS.

## 2. Static repaired passports: exact arithmetic

Use right-to-left permutation multiplication.

For \((5,3,2)\) on six letters, put

\[
A=(1\,2\,3\,4\,5),\qquad
C=(0\,1\,2\,5\,4),\qquad
I=(0\,4\,1\,5\,3).
\]

The displayed finite tuple is \(T=(A,A,C)\), and

\[
A\,A\,C\,I=1.
\]

All four cycles have type \((5,1)\); the generated group is transitive
\(A_6\) of order \(360\). Total ramification is \(16\), so \(G=3\).
The numerical data are

\[
d=6,\quad n=3,\quad s=2,\quad K=\delta=10,\quad \Xi=-1.
\]

For \((6,3,2)\) on seven letters, put

\[
A=(0\,1\,2\,3\,4\,5),\qquad C=(1\,2\,3\,4\,5\,6),
\qquad I=(A^2C)^{-1}.
\]

The three finite cycles have type \((6,1)\), \(A^2C\) and \(I\) have type
\((5,2)\), and \(\langle A,C\rangle=S_7\). Total ramification is
\(3\cdot5+5=20\), giving

\[
d=7,\quad G=4,\quad s=2,\quad K=\delta=12,\quad \Xi=-1.
\]

These statements are static Nielsen-class and genus checks only.

## 3. The necessary braid-equivariance condition

Fix an ordered branch tuple using a target basepoint and distinguished arcs.
For adjacent entries \(a,b\), use the positive right Hurwitz action

\[
H_i(\ldots,a,b,\ldots)
 =(\ldots,b,b^{-1}ab,\ldots).
\tag{3.1}
\]

It preserves the ordered product. The inverse generator acts by

\[
H_i^{-1}(\ldots,a,b,\ldots)
 =(\ldots,aba^{-1},a,\ldots).
\tag{3.2}
\]

A loop of the parameter returns the unordered target branch set to itself.
If the branched covers occur as fibres of one family over that loop, the
final cover must be isomorphic to the initial cover. With the chosen arcs,
this gives the necessary condition

\[
H_\beta(T)=hTh^{-1}
\quad\text{coordinatewise for some }h\in S_d.
\tag{3.3}
\]

Here \(h\) is the permitted relabelling of source sheets. No extra arbitrary
permutation of tuple positions is allowed: the braid action already records
the movement of target branch points. The infinity entry must also satisfy
(3.3), but failure on the finite entries is already decisive.

Changing distinguished arcs Hurwitz-transforms both \(T\) and the parameter
braid, so the stabilizer condition (3.3) is invariant under that change.
Using the inverse convention merely replaces every \(H_i\) by \(H_i^{-1}\);
both signs are checked below.

## 4. Exact obstruction for \(\phi=t^2(t-1)\)

A cubic with two distinct simple critical values has two root-collision
half-twists whose edges form a tree on the three roots. After ordering the
roots they may be taken as \(H_1^{\pm1}\) and \(H_2^{\pm1}\).

Both displayed repaired tuples have the form

\[
T=(A,A,C),\qquad A\ne C.
\tag{4.1}
\]

The first half-twist is harmless:

\[
H_1^{\pm1}(A,A,C)=(A,A,C).
\]

The second is not. From (3.1)--(3.2),

\[
H_2(T)=(A,C,C^{-1}AC),\qquad
H_2^{-1}(T)=(A,ACA^{-1},A).
\tag{4.2}
\]

Simultaneous conjugacy preserves the equality relation among the ordered
coordinates. In \(T\), coordinates \(1\) and \(2\) are equal and coordinate
\(3\) is different. In the first tuple of (4.2), coordinates \(1\) and \(2\)
are different; in the second, coordinates \(1\) and \(3\) are equal. Neither
can be simultaneously conjugate to \(T\).

This argument is independent of which collision edge receives the equal
pair. A two-edge tree on three vertices has another edge involving unequal
entries; after relabelling the same calculation applies. Therefore the
displayed \(A_6\) tuple does not descend along the two-critical-value braid
of \(\phi=t^2(t-1)\). Its product, transitivity, group order, and genus remain
correct, but it is not the claimed common family packet.

## 5. Exact obstruction for \(\phi=t^3\)

As \(a\) makes one positive loop about \(0\), the three roots of \(t^3=a\)
rotate cyclically. In \(B_3\) this is represented, according to ordering and
action convention, by \(H_2\circ H_1\) or \(H_1\circ H_2\); reverse orientation
uses their inverses.

Put

\[
D=C^{-1}AC,\qquad E=ACA^{-1},\qquad F=A^2CA^{-2}.
\]

Since \(A\ne C\), one has \(C\ne D\), \(A\ne E\), and \(A\ne F\). Direct use
of (3.1)--(3.2) gives the four convention/orientation possibilities:

\[
\begin{array}{c|c}
\text{action} & \text{resulting finite tuple}\\ \hline
H_2\circ H_1 & (A,C,D)\\
H_1\circ H_2 & (C,D,D)\\
H_2^{-1}\circ H_1^{-1} & (A,E,A)\\
H_1^{-1}\circ H_2^{-1} & (F,A,A).
\end{array}
\tag{5.1}
\]

Their ordered equality patterns are respectively different from the
\(1=2\ne3\) pattern of \(T=(A,A,C)\). None satisfies (3.3).

Consequently the displayed \(S_7\) tuple also fails the required cubic-root
braid equivariance. The weighted-homogeneous local monodromy

\[
(s,t)\longmapsto(\zeta_6s,\zeta_3t)
\]

does fix each branch of \(s^6/6+t^3=0\), but that does **not** imply that the
global seven-sheet Nielsen tuple is fixed up to simultaneous conjugacy.
The Opus statement that the “obvious equivariance objection does not bite”
is therefore unsupported and false for the displayed tuple.

This does not prove that every tuple in the relevant Nielsen class fails.
A different tuple or a different lift may exist.

## 6. Mutation and convention controls

The obstruction is not a cycle-type or composition artifact.

| control | mutated test | result |
|---|---|---|
| M1 | Check only product, cycle types, transitivity, and RH | Both tuples falsely PASS; equivariance is independent data |
| M2 | Delete the second simple-critical loop for \((5,3,2)\) | \(H_1(T)=T\), so the mutated packet falsely PASSes |
| M3 | Mutate \(C\) to \(A\) | \(T=(A,A,A)\) is fixed by all adjacent Hurwitz generators; obstruction disappears |
| M4 | Replace the \(t^3\) root-rotation braid by its cube, the full twist | The full twist acts by simultaneous conjugation, so the mutated packet PASSes |
| C1 | Reverse braid orientation and use (3.2) | Failure persists, as the last two rows of (5.1) show |
| C2 | Reverse the order of the two cyclic generators | Failure persists, as both positive rows of (5.1) show |
| C3 | Allow arbitrary sheet relabelling \(h\in S_d\) | Failure persists because simultaneous conjugacy preserves coordinate equality |

Thus the equality pattern \(A,A,C\), the second collision loop, and the
one-loop rather than three-loop parameter braid are all load-bearing.
Comparing only passports is a detected false-positive mutation.

## 7. Correction to C13/T1: affine interior versus infinity

For a Keller pair,

\[
df\wedge dg\ne0
\]

implies \(df\ne0\), so \(f:\mathbb A^2\to\mathbb A^1\) has no **affine
interior** critical points. Its affine Milnor contribution is zero.

It does not follow that page-\(H_1\) vanishing cycles cannot exist. A
nonproper submersion can have atypical values and vanishing homology at
infinity; indeed the reviewed Suzuki package identifies the total infinity
defect with

\[
\delta=1-\chi_{\rm gen}=b_1(F)
\]

for the connected generic fibre. Such cycles live on the generic page but
arise from boundary/relative monodromy after compactification, not from
critical points inside \(\mathbb A^2\).

The safe correction is therefore:

* \(K\) has no automatic page-\(H_1\) interpretation, because no comparison
  from auxiliary quotient zero-cycles has been constructed.
* An ordinary PALF whose critical points are asserted to be the affine
  critical points of \(f\) cannot model a Keller coordinate.
* A compactified boundary, relative Lefschetz, or vanishing-at-infinity model
  is not ruled out by \(df\ne0\); it needs separate typing.
* The five-stabilization \(D^4\) example remains a valid abstract
  count-only control. Call it a contractible positive-Lefschetz filling, not
  an identification \(D^4\cong\mathbb A^2\).

Accordingly, Opus C13's “category is empty,” T1's “none can exist,” and the
instruction to kill every PALF-related lane are too strong.

## 8. Correction to C9: finite ends do not refute global pole transport

In the computed boundary germ, the points \(t=\pm\sqrt a\) are finite-value
end places. The natural local relative sequence is

\[
H_1(M_a)\longrightarrow H_1(M_a,M_a\cap D)
 \longrightarrow\widetilde H_0(M_a\cap D),
\]

so its local vertices are finite ends, not pole places. This refutes any
*tautological identification* of collision roots with poles.

It does not refute a hypothetical global map

\[
V_{\rm aux}\longrightarrow\widetilde H_0(\text{pole places})
\]

built by transport through a compactification or boundary tree. No such map
is known, and the nongluable local/Hurwitz control cannot prove its
nonexistence. The safe wording is:

> A QCS boundary-complex proof would require a new global incidence from
> quotient collisions to pole relations. The computed local boundary map
> lands instead on finite-end relations, so it cannot supply that incidence
> without additional transport.

Do not automatically replace the pole vertex set by all \(s+n\) ends: that
changes the target inequality and is a different conjectural complex.

Also, the equality of the local defect dimension with
\(\dim H_1(M_a,M_a\cap D)\) does not by itself construct an isomorphism from
\(V_{\rm aux}\). That comparison remains missing.

## 9. Maximum safe coordinator integration

The following package is safe.

1. **Auxiliary count:** \(K=\sum_i b_i(\deg P_i-1)\) is an exact weighted
   vanishing-zero-cycle/positive auxiliary-braid count. No automatic map to
   page \(H_1\) is filed.
2. **Conditional QCS complex:** the two stated surjections imply QCS by
   rank-nullity, but neither is constructed. Pole incidence remains a global
   missing map; the known local relative boundary uses finite ends.
3. **Recorded degree-six control:** the \((5,2,2)\) equality germ and
   \((5,1)^3\) passport cannot be glued by the genus obstruction. Retain them
   only as separate local and numerical/Hurwitz controls.
4. **GENUS-BUDGET:** retain (GB) as a necessary condition on one-quotient-line
   zero-excess controls, with its hypotheses and multiplicity convention.
5. **Repaired candidates:** the \((5,3,2)\) and \((6,3,2)\) numerical data and
   static passports are correct, but both displayed tuples fail the necessary
   cubic braid-equivariance test. They do not restore a joint witness.
6. **Open discriminator:** search for a different Nielsen tuple stabilized,
   up to simultaneous conjugacy, by the appropriate polynomial-root braid;
   only then attempt a common surface/boundary realization. No Kirby search is
   warranted before that gate.
7. **Category:** \(f\) has no affine critical points, while vanishing cycles at
   infinity remain possible. Use boundary/relative language; retain the
   \(D^4\) PALF only as an abstract slogan-control.

No QCS, PCB, Keller, polynomial-map, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13438`.
- Body SHA-256:
  `bca3c47066e65c218205fb8895e60a5799eade29d8f0d5c603844ade57abb654`.
- Frozen basis: `55067d08c111f473945700ded838a7798b8b3fb2`.
