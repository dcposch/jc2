# Jung--van der Kulk degree descent through cusp words

**Date:** 2026-08-23  
**Task:** APPROACHES.md row 5  
**Verdict:** **CONFIRMED-BLOCKED at the cusp/leading-form layer.**

The blocker is genuine, and is stronger than failure of the two visible
triangular shears. A coprime rectangular cusp pair is already minimal for
maximum degree under **every** polynomial source and target automorphism.
Thus an affine-composed shear, a non-triangular tame word, or an arbitrarily
long reduced Jung word cannot lower its maximum degree. This follows from
the coordinate-cusp theorem already proved in
[TRANSPORT.md](../TRANSPORT.md), applied in the opposite direction from its
normalization use.

For the two requested exact records:

| record | common top monomial \(H\) | \((f_+,g_+)\) | degrees | result |
|---|---|---|---|---|
| residue A | \(x^{63}y^{21}\) | \((cH^2,dH^3)\) | \((168,252)\) | no source/target automorphism lowers \(252\) |
| pre-Laurent GGV \(A_0=(8,28),(m,n)=(3,2)\), component-sorted | \(x^8y^{28}\) | \((cH^2,dH^3)\) | \((72,108)\) | no source/target automorphism lowers \(108\) |

This is a no-descent theorem about any pair having the displayed rectangular
support, not a proof that either formal/admissible record is realized by a
Keller counterexample. Those realization gaps are labelled **CONJECTURE**
below.

---

## 1. What a Jung descent step would have to be

Let \(F=(P,Q)\in\mathbf C[x,y]^2\), with

\[
 J(P,Q)=1,\qquad p=\deg P,\quad q=\deg Q,\quad
 \Delta(F)=\max(p,q).
\]

The relevant elementary target automorphisms are

\[
 E_\phi^{(2)}(U,V)=(U,V-\phi(U)),\qquad
 E_\phi^{(1)}(U,V)=(U-\phi(V),V).
\]

Postcomposition gives

\[
 E_\phi^{(2)}\circ F=(P,Q-\phi(P)),\qquad
 E_\phi^{(1)}\circ F=(P-\phi(Q),Q).
\]

It preserves the constant Jacobian. It also preserves noninvertibility: if
\(E_\phi\circ F\) were an automorphism, then
\(F=E_\phi^{-1}\circ(E_\phi\circ F)\) would be one. Therefore, if every
nonlinear Keller pair admitted such a strict drop, a counterexample of
minimal \(\Delta\) could not exist.

This is the exact point at which Jung--van der Kulk cannot simply be quoted.
The amalgam theorem decomposes an element already known to lie in
\(\operatorname{Aut}(\mathbf A^2)\). A counterexample is an endomorphism
outside that group; the lowering factor must be produced from additional
information.

### Lemma 1 (exact elementary drop criterion)

Assume \(p<q\), and write \(P_p,Q_q\) for the ordinary top homogeneous
forms. Let

\[
 \phi(T)=a_kT^k+\cdots,\qquad a_k\ne0.
\]

Then

\[
 \Delta(P,Q-\phi(P))<q
\]

if and only if

\[
 q=kp,\qquad Q_q=a_kP_p^k.
 \tag{1.1}
\]

Indeed, \(P\) remains of degree \(p<q\). The degree-\(q\) part of the second
component can disappear only if \(kp=q\), and in that case it disappears
exactly under the second identity in (1.1). Conversely those identities
make \(\deg(Q-\phi(P))<q\), so the maximum drops. Lower coefficients of
\(\phi\) do not affect this first drop. The case \(q<p\) is symmetric.

In particular, for unequal component degrees a strict one-shear descent
requires divisibility of the larger degree by the smaller. For \(p=q\), an
invertible affine target change may first lower one linear combination when
\(P_p,Q_p\) are proportional, but an invertible linear change cannot lower
both top forms at once. After that affine preparation the same criterion
(1.1) applies to the resulting unequal degree pair.

This is exactly the automorphism proof's degree-divisibility step. It is not
forced for a normalized hypothetical counterexample.

---

## 2. The cusp obstruction for every coordinate, not just a shear

Fix coprime integers

\[
 1<m<n
\]

and nonzero \(c,d\in\mathbf C\). Give \(U,V\) weights \(m,n\), respectively,
and put

\[
 B(U,V)=d^mU^n-c^nV^m.
 \tag{2.1}
\]

The monomial-curve substitution

\[
 U=cZ^m,\qquad V=dZ^n
 \tag{2.2}
\]

has kernel \((B)\).

### Theorem 2 (coordinate-cusp exclusion)

If \(h(U,V)\) is a coordinate of a polynomial automorphism of
\(\mathbf A^2\), then

\[
 \operatorname{in}_{m,n}h\notin(B),\qquad
 \operatorname{in}_{m,n}h(cZ^m,dZ^n)\ne0.
 \tag{2.3}
\]

This is TRANSPORT.md, Theorem 1.1. A compact replay matters here because
(2.3) decides the proposed cusp-word experiment at every word length.

Choose a coordinate mate \(k\) and set
\(\partial=J(h,-)\). In coordinates \((h,k)\), this is a nonzero constant
multiple of \(\partial/\partial k\), hence is locally nilpotent. Its highest
\((m,n)\)-homogeneous part is

\[
 D=J(\bar h,-),\qquad \bar h=\operatorname{in}_{m,n}h,
\]

and the associated-graded argument shows that \(D\) is also a nonzero locally
nilpotent derivation.

For an LND on a characteristic-zero domain define

\[
 \delta_D(a)=\max\{j:D^j(a)\ne0\}.
\]

The Leibniz formula gives
\(\delta_D(ab)=\delta_D(a)+\delta_D(b)\), so \(\ker D\) is factorially
closed. If \(\bar h=Bq\), then \(D(\bar h)=0\) would force
\(B\in\ker D\). Therefore

\[
 n d^mU^{n-1}D(U)=m c^nV^{m-1}D(V),
\]

and coprimality of the displayed \(U\)- and \(V\)-powers gives

\[
 V^{m-1}\mid D(U),\qquad U^{n-1}\mid D(V).
\]

Neither derivative is zero. With
\(a_0=\delta_D(U)\), \(b_0=\delta_D(V)\), additivity gives

\[
 a_0-1\ge(m-1)b_0,\qquad
 b_0-1\ge(n-1)a_0.
\]

Adding yields

\[
 (n-2)a_0+(m-2)b_0\le-2,
\]

impossible for \(m,n>1\). This proves (2.3). The proof is
characteristic-zero; a finite-field word sweep is not a substitute because
LND degrees and the surviving Leibniz coefficient have characteristic-\(p\)
exceptions.

### Theorem 3 (rectangular cusp pairs are Aut-orbit max-degree minimal)

Suppose, for positive integers \(a,b\),

\[
\begin{aligned}
 \operatorname{Supp}P&\subseteq[0,ma]\times[0,mb],
 & [x^{ma}y^{mb}]P&=c\ne0,\\
 \operatorname{Supp}Q&\subseteq[0,na]\times[0,nb],
 & [x^{na}y^{nb}]Q&=d\ne0.
\end{aligned}
\tag{2.4}
\]

Then for every source automorphism \(L=(u,v)\) and every target coordinate
\(h(U,V)\),

\[
 \deg h(P\circ L,Q\circ L)
 =D_L\deg_{m,n}h,\qquad
 D_L=a\deg u+b\deg v.
 \tag{2.5}
\]

Consequently, for every source and target automorphism \(L,K\),

\[
 \Delta(K\circ(P,Q)\circ L)\ge n(a+b)=\Delta(P,Q).
 \tag{2.6}
\]

**Proof.** The northeast monomial is the unique maximizer of the functional
\((i,j)\mapsto i\deg u+j\deg v\) on each rectangle. With \(u_+,v_+\) the
ordinary top forms, put

\[
 H=u_+^av_+^b.
\]

Then

\[
 (P\circ L)_+=cH^m,\qquad (Q\circ L)_+=dH^n,\qquad \deg H=D_L.
\]

The only possible cancellation at degree
\(D_L\deg_{m,n}h\) is precisely
\(\operatorname{in}_{m,n}h(cZ^m,dZ^n)=0\), forbidden by Theorem 2. This proves
(2.5).

Now \(D_L\ge a+b\), since both source coordinates are nonconstant. If a
target coordinate has \((m,n)\)-degree below \(n\), it contains no \(V\) and
lies in \(\mathbf C[U]\). Such a coordinate must be affine linear in \(U\):
from \(J(p(U),k)=p'(U)k_V\in\mathbf C^*\), \(p'\) is constant. The two
components of an automorphism cannot both be affine functions of \(U\), so
at least one has weighted degree at least \(n\). Equations (2.5) and
\(D_L\ge a+b\) give (2.6). Equality is attained by the original pair.
\(\square\)

Theorem 3 is stronger than needed for the requested test. It rules out not
only the first elementary move but also a word which first raises degrees and
later tries to descend. Every component of every Jung word is a coordinate,
so Theorem 2 prevents the only cusp cancellation that could defeat (2.5).

---

## 3. Direct affine-composed-shear computation

The word-level theorem has a particularly transparent first-step form for
the requested \(2{:}3\) cusp. Write

\[
 f_+=cH^2,\qquad g_+=dH^3,\qquad D=\deg H.
 \tag{3.1}
\]

Let an invertible affine map first form

\[
 X=\alpha U+\beta V+e,\qquad
 Y=\gamma U+\delta V+f,\qquad
 \alpha\delta-\beta\gamma\ne0,
\]

then apply \((X,Y)\mapsto(X,Y-\phi(X))\), with
\(\deg\phi=k\ge2\), and finally apply another invertible affine map. The
last affine map cannot erase a highest-degree vector from both components,
so it suffices to inspect \(X\).

| active linear coordinate \(X\) | \(\deg X(f,g)\) | degree of \(\phi(X(f,g))\) | outcome |
|---|---:|---:|---|
| \(\beta\ne0\) | \(3D\) | \(3kD>3D\) | maximum degree rises |
| \(\beta=0\) | \(2D\) | \(2kD\) | cancellation of the \(3D\) term would require \(2k=3\), impossible |

When \(\beta=0\), invertibility forces \(\delta\ne0\), so \(Y(f,g)\) really
retains its \(3D\) term unless a term of exactly that degree cancels it.
For \(k=1\) the operation is only affine and the maximum stays \(3D\); for
\(k\ge2\), \(2kD\ge4D\), so it rises. The opposite elementary shear is the
same calculation after exchanging the two affine coordinates.

Thus **every affine-composed elementary shear stays at \(3D\) or raises the
maximum**. This computation answers the proposed “perhaps non-triangular”
escape without invoking an enumeration. Theorem 3 then upgrades it from one
affine-composed elementary factor to an arbitrary tame word.

There is a visible polynomial cancellation at the next common multiple:

\[
 B(U,V)=d^2U^3-c^3V^2,\qquad
 B(cH^2,dH^3)=0.
 \tag{3.2}
\]

But \(B\) is not a coordinate, and Theorem 2 says more: no coordinate can
even have a top \((2,3)\)-face divisible by \(B\). The cusp cancellation is
available to arbitrary polynomials in \(f,g\), not to components of a target
automorphism. This is the precise obstruction.

---

## 4. Exact instance A: residue-A leading frame

[SHEET6-TEMPLATE.md](../SHEET6-TEMPLATE.md) records

\[
 (k_f,l_f)=(126,42),\qquad(k_g,l_g)=(189,63),\qquad
 (\deg f,\deg g)=(168,252).
\]

The rectangle bases are

\[
 (63,21),\qquad
 H=x^{63}y^{21},\qquad \deg H=84,
\]

so the unique northeast ordinary top forms are

\[
 f_+=c x^{126}y^{42}=cH^2,\qquad
 g_+=d x^{189}y^{63}=dH^3.
\]

The exact cusp coincidence is

\[
 f_+^3=c^3x^{378}y^{126},\qquad
 g_+^2=d^2x^{378}y^{126},\qquad
 \deg H^6=504.
\]

The elementary degree test is already fatal:

\[
 \frac{\deg g}{\deg f}=\frac{252}{168}=\frac32\notin\mathbf N.
\]

For \(g-\phi(f)\), \(k=1\) contributes degree \(168<252\), while \(k=2\)
contributes degree \(336>252\); no integer \(k\) cancels degree \(252\).
For \(f-\phi(g)\), a linear term leaves maximum degree \(252\), and a
nonlinear term raises it. Section 3 rules out affine conjugation, and
Theorem 3 rules out every longer source/target word:

\[
 \Delta(K\circ(f,g)\circ L)\ge252
 \qquad(L,K\in\operatorname{Aut}\mathbf A^2).
 \tag{4.1}
\]

**CONJECTURE (residue-A realization gap).** The filed residue-A object is a
formal Sigray frame with extensive coefficient data, not a known polynomial
Keller pair. If no polynomial Keller pair realizes this frame, that must be
proved from lower coefficients, global gluing, or another non-leading-form
condition. The cusp/Jung calculation neither realizes nor kills it.

---

## 5. Exact instance B: the pre-Laurent GGV \((8,28)\) family

The live [lib/families.py](../lib/families.py) record, replayed by
[cases/transport_check.py](../cases/transport_check.py), is

\[
 A_0=(8,28),\qquad (m,n)_{\rm GGV}=(3,2),\qquad
 (\deg P,\deg Q)=(108,72),
\]

with base polygon

\[
 S=\operatorname{conv}\{(0,0),(1,0),(8,28),(0,4)\}.
\]

Its northeast corners are \(3(8,28)=(24,84)\) for \(P\) and
\(2(8,28)=(16,56)\) for \(Q\). Sort the lower multiplier first:

\[
 f=Q,\qquad g=P,\qquad H=x^8y^{28},\qquad \deg H=36.
\]

Then

\[
 f_+=c x^{16}y^{56}=cH^2,\qquad
 g_+=d x^{24}y^{84}=dH^3,\qquad
 (\deg f,\deg g)=(72,108).
\]

The exact common cusp multiple is

\[
 f_+^3=c^3x^{48}y^{168},\qquad
 g_+^2=d^2x^{48}y^{168},\qquad
 \deg H^6=216.
\]

Again \(108/72=3/2\). A shear in \(f\) has degree \(72\) at \(k=1\) and
\(144\) at \(k=2\), never \(108\). The opposite shear preserves or raises
the maximum. The full result is

\[
 \Delta(K\circ(f,g)\circ L)\ge108
 \qquad(L,K\in\operatorname{Aut}\mathbf A^2).
 \tag{5.1}
\]

The determinant-one source rotation used in TRANSPORT.md transposes the
corners to \((56,16),(84,24)\) but preserves degrees and the same conclusion.

**CONJECTURE (GGV-family realization gap).** The \((8,28)\) object is an
admissible pre-Laurent family record conditional on a hypothetical
counterexample in that bounded branch. The later Section-4 object has
\([P,Q]=x^2\), not constant Jacobian, and is not the input to (5.1). No
polynomial counterexample realizing the pre-Laurent record is known.

The local regression script confirms the integer corners and degrees; it
does not prove Theorems 2 or 3. Their proof is the characteristic-zero
coordinate/LND argument above.

---

## 6. What happened to the proposed cusp-word experiment

[APPROACHES.md](../APPROACHES.md) proposed enumerating reduced Jung words and
asking whether a coordinate's \((m,n)\)-initial face lies in
\((d^mU^n-c^nV^m)\). In characteristic zero that experiment now has an exact
all-length answer:

\[
 \boxed{\text{there are no hits.}}
\]

Every component of every reduced Jung word is a coordinate, so Theorem 2
forbids a hit before any bounds on word length, triangular exponents, or
coefficient height are imposed. A search over \(\mathbf Q\) can only regress
the theorem. A search over \(\mathbf F_{101}\) probes a different statement
and cannot adjudicate the characteristic-zero LND proof.

For normalization transport, “no cusp-coordinate hit” was useful: it proved
that a target automorphism cannot cancel the rectangular peak. For the
present **degree-descent** program, the same fact has the opposite strategic
meaning: the peak cannot be cancelled by any tame coordinate, so it is an
absolute descent block.

---

## 7. Final verdict and precise obstruction

### Proved

1. A strict elementary reduction of \((P,Q)\) with \(\deg P<\deg Q\) exists
   exactly when the degree divisibility and top-power condition (1.1) hold.
2. For a coprime rectangular cusp pair with \(1<m<n\), every source/target
   automorphism satisfies the exact degree formula (2.5), and maximum degree
   cannot decrease.
3. The residue-A frame and the component-sorted GGV \((8,28)\) frame are both
   \(2{:}3\) instances of this theorem. Affine-composed shears are not an
   escape; neither are longer non-triangular Jung words.

### Not proved

**CONJECTURE (realizability-kill needed for JC2).** No nonautomorphic Keller
pair realizes a coprime rectangular cusp support of the form (2.4).
Establishing this would have to use more than the leading cusp: the leading
data themselves prove Aut-minimality rather than a lowering move. Through
the GGV selected-pair theorem, such a realizability kill would be a genuine
JC2 theorem, not an elementary consequence of the amalgam structure.

### Classification of row 5

**CONFIRMED-BLOCKED**, with a precise obstruction:

\[
 \boxed{
 \operatorname{in}_{m,n}h\notin
 (d^mU^n-c^nV^m)
 \quad\text{for every target coordinate }h
 }
\]

forces

\[
 \boxed{
 \Delta(K\circ(P,Q)\circ L)\ge\Delta(P,Q)
 \quad\text{for all }K,L\in\operatorname{Aut}(\mathbf A^2)
 }
\]

on the rectangular cusp records. Jung--van der Kulk explains descent once
invertibility is known; it does not manufacture the missing lowering factor
for a nonautomorphism. Here the cusp data do not merely fail to force that
factor: they rigorously forbid it.
