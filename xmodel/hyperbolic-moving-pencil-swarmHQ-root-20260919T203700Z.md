# Hyperbolic moving polynomial pencils force a rational invariant

Producer: swarmHQ ROOT (Astra assigned context; hosted identity not exposed).
Date: September 19, 2026 UTC.
Frozen public basis: e0f8b2fb387b10606be17251eaa659d14b8573c7.
Evidence: MANUAL with named classical curve and coarse-moduli imports.
Lifecycle: PRODUCER-CHECKED, PROVISIONAL; different-model FIRST pending.
No literature-novelty, arbitrary-Keller pencil, or JC2-resolution claim.

## 1. Exact statement

Let F:A2_C -> A2_C be a DOMINANT polynomial endomorphism. Suppose a
nonconstant polynomial h satisfies

    h composed F = psi composed h,       psi in C[t], d=deg(psi)>=2,

and C(h) is relatively algebraically closed in L=C(x,y). Let C be the
FULL geometric generic affine h-fiber, and let Cbar be its smooth
projective completion. Assume C is smooth and

    delta=2g-2+n>0,       g=genus(Cbar), n=|Cbar minus C|.

Then there exists r in C(x,y), nonconstant even along the generic h-fiber,
such that r composed F=r. Moreover, the generic degree N(F) equals d.

Consequently, a polynomial map with Jacobian EXACTLY1 cannot satisfy
these moving-pencil hypotheses: the accepted rational-area invariant
theorem would give N(F)=1, whereas d>=2. There is no claim that a
hypothetical noninvertible Keller map has such a pencil. Generic fibers
A1 or Gm, degree-one base maps, and arbitrary constant Jacobian in the
corollary are outside this statement.

## 2. The induced map of full generic fibers

Put K=C(h), K0=C(psi(h)), and sigma=F*. Then sigma(K)=K0 and
[K:K0]=d. Relative algebraic closure and characteristic zero make L/K
a regular one-variable function field. Its isomorphic image sigma(L)/K0
is regular as well, and is therefore linearly disjoint from the finite
extension K/K0. It follows that

    [sigma(L)K:sigma(L)]=d,
    k=[L:sigma(L)K]=N(F)/d.

In particular d divides N(F); no properness of F has been assumed.
The semiconjugacy defines a REGULAR map from the full affine generic
fiber of h to the base-changed generic fiber with parameter psi(h).
Polynomiality of F is what includes the entire affine fiber. Geometric
integrality ensures the base-changed target is integral, and its function
field is sigma(L)K. Dominance of F makes this curve map nonconstant.

After extending K to its algebraic closure, both affine curves have the
same genus g and the same number n of punctures; changing the generic
base parameter does not change their geometric type. Their smooth
projective completions admit a finite map f of degree k, by the classical
curve/function-field correspondence. Write S_s and S_t for their puncture
sets. Affine regularity gives

    f^(-1)(S_t) subset S_s.

The part of the ramification divisor lying over S_t has degree

    k*n - |f^(-1)(S_t)| >= k*n-n.

Riemann--Hurwitz and nonnegativity of the remaining ramification therefore
give

    2g-2 >= k*(2g-2)+(k-1)*n,
    (k-1)*(2g-2+n) <= 0.

Since delta>0 and k>=1, k=1. Thus f is a projective isomorphism, and the
puncture inclusion, with equal cardinalities, is equality. The FULL
affine curves, including their puncture data, are isomorphic. Also N(F)=d.
This is not an assertion that a nonproper map was initially a covering.

## 3. Constant unordered pointed moduli

Spread the smooth generic completion and its reduced puncture divisor
over a nonempty open subset B of A1_t. After a finite etale base change
the punctures can be labeled. The classical coarse moduli variety M_(g,n)
classifies smooth n-pointed genus-g curves and assigns an algebraic
classifying map to a family. These statement-level properties are recorded
in [Chaudhuri, Moduli of Curves, Section 2.2, printed page 2](https://www.niser.ac.in/~chitrabhanu/files/ModuliCurvesNISER-15Jul2017.pdf).
They are named classical imports, not a new construction or proof of
moduli existence. In particular, a coarse space does NOT provide a fine
universal family or trivialize twists.

Take the finite permutation quotient M=M_(g,n)/S_n. The existence of this
finite quotient for a quasi-projective variety, and ordinary finite
descent of the classifying map, give an unordered moduli map

    m:B -> M.

Section 2's generic affine isomorphism implies, as rational maps,

    m(psi(t))=m(t).

If m were nonconstant, the closure of its image would be an integral
curve. A nonconstant rational function on that curve would pull back to
a nonconstant v in C(t) satisfying v(psi(t))=v(t). Multiplicativity of
degrees of nonconstant rational maps of projective curves gives

    deg(v)*d=deg(v),

contradicting d>=2. Thus m is constant. Since C is algebraically closed,
its value is represented by a complex smooth pointed pair (C0,S0).
Every sufficiently general complex closed fiber is isomorphic to this
pair, with its UNORDERED puncture set. Projective moduli alone would not
justify this conclusion for the affine curves.

## 4. Geometric trivialization without a fine-moduli assumption

Here is the needed algebraization/descent step explicitly. For a smooth
pointed pair of this type, the log-canonical bundle has degree delta>0.
Its third power has degree

    3*(2g-2+n) >= 2g+1

in every permitted case: g=0,n>=3; g=1,n>=1; or g>=2,n>=1. It is thus
very ample by the classical degree criterion for line bundles on curves.
After shrinking B, relative sections give projective embeddings of the
family and the constant pair with the same Hilbert polynomial and ambient
dimension. Isomorphisms of the pairs are represented by the finite-type
projective-linear change-of-frame scheme preserving the embedded curve
and its reduced puncture divisor. This uses the functoriality of the
log-canonical bundle; arbitrary projective embeddings would not suffice.

Every closed point of a sufficiently small B has a point in this Isom
scheme over it. Its image is constructible and therefore contains the
generic point. A closed point in the nonempty generic Isom scheme has
residue field finite over K. Consequently the generic pointed pair becomes
isomorphic to (C0,S0) after a FINITE extension of K, and hence over an
algebraic closure Kbar. A twist over K is allowed throughout.

The same embedding proves that G=Aut_C(C0,S0) is an algebraic group of
finite type. Its tangent space at the identity is

    H^0(C0,T_C0(-S0))=0,

since this line bundle has degree -delta<0. Thus G is zero-dimensional
and finite. All geometric automorphisms after any algebraically closed
extension of C are already defined over C. The tangent-space statement,
finite-type Isom construction and constructibility are standard algebraic
geometry facts used at their stated scopes, not claims about a complete
moduli construction. Unordered markings cause only a finite permutation
action and do not change the tangent calculation.

## 5. Descending a fixed rational function

Choose one geometric isomorphism of pairs

    alpha:(C_Kbar,S_Kbar) -> ((C0)_Kbar,(S0)_Kbar).

Because G is finite, its invariant function field C(C0)^G has transcendence
degree one. Choose a nonconstant q in that field. Regard alpha*(q) as an
element r of Lbar=Frac(L tensor_K Kbar).

For each gamma in Gal(Kbar/K), changing alpha by gamma changes the
trivialization by an element of G: both are isomorphisms to the same
constant pointed curve. The coefficients of q are in C and q is G-invariant.
It follows that gamma(r)=r. Regularity of L/K gives the usual Galois
descent identity (Lbar)^Gal(Kbar/K)=L, so r belongs to L. It is not in K,
because it is nonconstant on the geometric generic curve.

Finally extend the embedding sigma|K:t->psi(t) to an automorphism s of
Kbar fixing C. Such an extension is surjective: Kbar is algebraic over
sigma(K), and an algebraically closed image containing sigma(K) must
contain every element of Kbar. The map sigma together with s induces a
semilinear map of the geometric generic curve. Section 2 shows that this
map is a pointed isomorphism, not merely a dominant correspondence.
In the alpha trivialization, its difference from coefficient action s
is an automorphism in G. Both operations fix q. Therefore

    sigma(r)=r.

This gives an invariant for F ITSELF; an iterate is unnecessary. It does
not require the finite trivializing extension of K to be preserved by
sigma, a chosen lift of the base map to that extension, or a section of
the original h-fibration. Using Kbar avoids all three unwarranted steps.

If J(F)=1, apply the [accepted rational-area invariant theorem](rational-area-invariant-swarmHQ-root-20260919T120200Z.md),
with its [independent review and binding scope](rational-area-first-integration-swarmHQ-root-20260919T121900Z.md).
It gives N(F)=1, contradicting N(F)=d>=2. The exact invariant standard
area form is essential to this corollary; a separate output normalization
cannot silently be made while preserving the pencil.

## 6. Controls, comparison and remaining gap

The mechanism needs both hyperbolicity and a degree>1 base map. The proof
does not impose these conditions on arbitrary Keller maps. When d=1 the
moduli-degree contradiction disappears; when delta<=0 neither the curve
degree inequality nor finite-automorphism quotient supplies the claimed
argument. These are excluded hypotheses, not classified remaining cases.

As a direct scope check, take h=(x^2-1)y and

    F(x,y)=(x,(x^2-1)*y^2).

Then h composed F=h^2, its generic fiber is A1 minus two points, N(F)=2,
and r=x is fixed, exactly as predicted. Its Jacobian is
2*(x^2-1)*y, not1. This is a simple manual consistency check, not a new
countercontrol family or a JC2 counterexample.

The [positive-genus invariant theorem](positive-genus-invariant-swarmHQ-root-20260919T035200Z.md)
starts with a FIXED invariant and uses affine punctures to bound degree.
Here a moving polynomial pencil with hyperbolic generic fiber produces a
different fixed rational function through moduli and descent. The earlier
[homogeneous-pencil theorem](homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md)
requires algebraically independent reduced numerator and denominator;
polynomial h is outside that proof. The present theorem instead requires
geometric integrality, hyperbolicity and d>=2, and its Keller corollary
uses Jacobian exactly1. Neither result supplies a pencil for arbitrary F.

The old [Hamiltonian affine-splitting test](../notes.md#2026-09-13-1610-utc--affine-splitting-does-not-control-projective-variation)
does not produce projective isotriviality from infinitesimal lifts. This
proof uses an actual degree>1 base semiconjugacy and full affine-fiber
isomorphisms, not an extension of that stopped inference. The recent
internal gradient-gcd test only reached N=lambda_1=d; the moduli argument
is a different structural input, not an improvement of that inequality.
Scoped searches in frozen public and HQ histories found no exact prior
calculation, not an exhaustive literature-novelty certification.

ROOT independently derived the argument before collecting substantive
same-model co-check findings. The native co-check completed at20:37:09,
and its whole final argument was collected with terminal status by20:39:42.
It confirms the affine isomorphism, constant pointed moduli and semilinear
descent, conditional on the stated classical inputs; it did not perform
new primary-source verification. This is not different-model FIRST.
All mathematics here is manual; no CAS, scientific code, cloud
computation or proof assistant was used. Classical curve completion,
Riemann--Hurwitz and the accepted rational-area theorem retain their named
imports; the added coarse-moduli statement was checked at lecture-note
statement scope only. No new pencil search, classification, construction
family or automatic successor is proposed. JC2 remains unresolved.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author completion: 2026-09-19 20:40:13 UTC, after whole-body readback,
the trusted collision check, and collection of the terminal native co-check.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12058`.
- Body SHA-256:
  `0e5db92d7dad304736d4a111036292f9da5e2b55277b06026765344ba44fe2b5`.
- Frozen basis: `e0f8b2fb387b10606be17251eaa659d14b8573c7`.
