# Degree-six labelled PALF test: local-genus obstruction and mixed defect

**Author:** Sol 5.6 Ultra  
**Date:** 2026-08-29  
**Basis:** 31777ce90994a106aade85064c0d868e32863f94  
**Lifecycle:** sealed research report; no canonical promotion

## Verdict

The requested matched realization is **obstructed before Kirby calculus**, if
the label \(P=z^2,\ b=w=5\) means the exact zero-excess boundary collision used
in the degree-six control.

The reason is categorical, not numerical. The local equality germ

\[
f=t^2+s^5/5,\qquad g=t
\]

has an \(A_4\) plane-curve singularity. Its compact Milnor fibre has genus
\(2\), whereas the \((5,1)^3\) degree-six passport forces the compact generic
fibre to have genus \(1\). A genus-two Milnor subsurface cannot embed in a
genus-one fibre. Thus the exact local collision and the abstract passport,
although their Euler jumps both equal \(5\), cannot occur in one labelled
surface family.

Moreover \(K=5\) is not five ordinary Picard--Lefschetz critical points. The
local morsification supplies four interior vanishing cycles; the fifth unit is
the merger of two boundary/end points into one. In the abstract Hurwitz
control the same integer splits differently: four dimensions of \(H_1\) are
lost and one dimension of \(H_0\) is created. A five-cycle \(D^4\) PALF can be
put on the same *unlabelled* abstract page, but that is an independent overlay,
not a lift of the quotient collision or passport.

Consequently the earlier five-stabilization control remains valid for the
claim that filling plus counts alone is insufficient. It must not be called a
labelled realization of the degree-six matched control.

## 1. The two exact tiers

### Passport tier

The branch cycles

\[
\sigma_+=(1\ 2\ 3\ 4\ 5),\quad
\sigma_-=(0\ 1\ 2\ 4\ 3),\quad
\sigma_\infty=(0\ 3\ 1\ 5\ 2)
\]

all have type \((5,1)\). Their total ramification is \(3(5-1)=12\), so
Riemann--Hurwitz for a connected degree-six cover gives

\[
2G-2=-2(6)+12=0,\qquad G=1.
\]

Removing the two points over infinity and the ramified point over each of the
two finite branch values gives four labelled ends: two pole places and two
finite-value places. The generic affine page is therefore

\[
F_{\rm Hur}=\Sigma_{1,4},\qquad b_1(F_{\rm Hur})=2+4-1=5.
\]

After the two finite branch values coalesce, the recorded normalization is
\(\mathbb G_m\coprod\mathbb A^1\).

### Exact local equality tier

The zero-excess chart has smooth surface coordinates \((s,t)\), boundary
divisor \(D=\{s=0\}\), and

\[
g=t,\qquad f=t^2+s^5/5,\qquad
df\wedge dg=s^4\,ds\wedge dt.
\]

On \(D\), this gives \(P(t)=t^2,\ Q(t)=t\), baseline and actual weight
\(b=w=5\). For \(a\ne0\), the extended fibre meets \(D\) in the two points
\(t=\pm\sqrt a\); for \(a=0\), its normalization has one point over the
collision. This is the licensed meaning of the local equality datum. It does
not by itself identify either point with a pole place; here they are
finite-value end places.

## 2. Exact local topology

At the collision, the Jacobian ideal of the fibre singularity is

\[
(\partial_t f,\partial_s f)=(2t,s^4),
\]

hence

\[
\mu=\dim_{\mathbb C}\mathbb C\{s,t\}/(t,s^4)=4.
\]

The singularity \(t^2+s^5=0\) has
\(\gcd(2,5)=1\) branch. Its compact Milnor fibre \(M_a\) is connected and

\[
\chi(M_a)=1-\mu=-3.
\]

It has one boundary component, so

\[
-3=2-2g(M_a)-1,\qquad g(M_a)=2.
\]

Equivalently, a morsification has four positive vanishing cycles with
\(A_4\)-chain intersection pattern. A regular neighbourhood of that chain is
a genus-two surface with one boundary component.

The divisor \(D\) meets \(M_a\) in two points for \(a\ne0\). Removing those
points gives a genus-two surface with three ends/boundary components:

\[
\chi(M_a\setminus D)=-5,\qquad b_1(M_a\setminus D)=6.
\]

The normalization of the central local fibre is a disk; after removing its
single point over \(D\), it is a punctured disk, with

\[
\chi=0,\qquad b_1=1.
\]

Thus the affine local jump is exactly

\[
0-(-5)=5=\underbrace{\mu}_{4}
       +\underbrace{(2-1)}_{\text{end merger}}.
\tag{2.1}
\]

Equation (2.1) is the typed form of the numerical collision contribution
\(b(\deg P-q)=5(2-1)=5\). Only four units are ordinary interior
Picard--Lefschetz cycles. The remaining unit is boundary/relative vanishing
homology. For example, it appears as the extra
\(\widetilde H_0\) term in the exact sequence for the two marked divisor
points,

\[
H_1(M_a)\longrightarrow H_1(M_a,\{p_+,p_-\})
\longrightarrow\widetilde H_0(\{p_+,p_-\}).
\]

Treating the coefficient \(b=5\) as five geometric copies of the quotient
half-twist erases this distinction.

## 3. The labelled realization is impossible

A Milnor fibre in a smooth surface degeneration embeds as a subsurface of
every sufficiently nearby smooth compactified fibre. Genus is monotone under
embedding of compact orientable subsurfaces. Therefore the exact local chart
forces

\[
G_{\rm global}\ge g(M_a)=2.
\]

The passport calculation forces \(G_{\rm global}=1\). These conclusions are
incompatible. Equivalently, the \(A_4\) vanishing chain has a genus-two regular
neighbourhood and cannot be supported on \(\Sigma_{1,4}\).

This obstruction uses the actual attachment required by the word
“labelled.” It does not identify a quotient flag with a pole: the two moving
points in the local chart are finite-end places, while the passport separately
has two pole places.

There is a second view of the mismatch. At the abstract-cover tier,

\[
(b_0,b_1)_{\rm gen}=(1,5),\qquad
(b_0,b_1)_{\rm special}=(2,1),
\]

so its Euler jump \(5\) is

\[
\Delta b_0-\Delta b_1=1-(-4)=5.
\tag{3.1}
\]

The local germ instead has connected normalization and realizes (2.1): four
compact Milnor cycles plus an end merger. Equations (2.1) and (3.1) have the
same decategorified Euler value but different homological degree and
attachment data. This is exactly why the earlier report correctly called the
construction a matched local/Hurwitz **control**, not one global family.

Finally, a pure PALF on \(\Sigma_{1,4}\) with five critical points and total
space \(D^4\) has five surface 1-handles and five Lefschetz 2-handles. Its
integral thimble-to-handle matrix must be unimodular; in particular the five
vanishing-cycle classes span \(H_1(\Sigma_{1,4};\mathbb Z)\) with rank five.
The passport degeneration loses only four \(H_1\) dimensions and creates one
\(H_0\) dimension, while the exact local germ has only four interior critical
cycles. Neither is the unimodular five-cycle PALF. A boundary degeneration or
relative handle is required, and ordinary PALF data do not specify it.

## 4. Why an unlabelled search gives a false positive

Independently, both of the following exist:

1. the topological degree-six branched cover on a genus-one compact surface,
   with its four marked ends; and
2. a five-positive-stabilization PALF on the underlying
   \(\Sigma_{1,4}\), with total space \(D^4\).

A diffeomorphism lets one place both structures on the same abstract page and
label two boundary components “pole” and two “finite.” One can also choose an
arbitrary vector-space bijection from five formal coefficient copies of the
single \(P=z^2\) half-twist to the five PALF cycles.

That construction satisfies the untyped list of counts but no compatibility
law. It does not make the PALF cycles lifts of the quotient braid, does not
recover the source-sheet passport under degeneration, and does not attach
finite-end places or pole places to quotient generators. Therefore a search
over unrestricted five-tuples in \(\operatorname{Mod}(\Sigma_{1,4})\) is not
a discriminator; it is guaranteed to find this irrelevant overlay.

## 5. Minimum packet for any successor test

A different degree-six test can be posed only after filing all of:

1. a common one-parameter surface and boundary-divisor germ, not separate
   local and Riemann-existence models;
2. a lift of the quotient half-twist to the decorated mapping class group
   that records the six source sheets and the two finite-end places;
3. separate chain groups for interior Lefschetz thimbles and
   boundary/end-merger classes, with their map to relative page homology;
4. the two pole-place labels, without replacing them by quotient flags,
   Puiseux series, or finite-end points; and
5. an integral handle matrix plus the boundary 3-manifold/fundamental-group
   check for the claimed \(D^4\) filling.

For the exact equality germ no such packet is needed: the genus
\(2>1\) obstruction already returns **NO**. For an alternative germ, the
cheapest finite calculation is first its Milnor fibre genus and marked-end
exact sequence. Kirby or mapping-class enumeration should run only if that
local surface embeds in \(\Sigma_{1,4}\).

## Consequence and nonclaims

This result invalidates neither QCS nor the degree-six dependency control. It
shows that the control is not source-complete and identifies a concrete
global constraint absent from its separate pieces. It does not prove that
every polynomial Keller collision has the displayed \(A_4\) form, does not
derive QCS from a genus sum, and does not claim that all boundary
degenerations admit PALF models.

The exact conclusion is narrower: the particular zero-excess local chart and
the particular genus-one passport cannot have a common labelled PALF
realization, and \(K=5\) cannot be promoted to five ordinary positive
vanishing cycles by an \(A^2\)-filling slogan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9434`.
- Body SHA-256:
  `181e5bdd06b053d790f7d8e08391927aec363d986f8a5ef04809ad2468ff1b9f`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
