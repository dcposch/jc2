# First-order radial criterion — producer claim, not a source theorem

ROOT,2026-09-12. MANUAL / PRODUCER-CHECKED / UNPROMOTED. Read together with
canonical-polar-trace-discriminator-root-20260912.md SHA
b8374142f0aa8373a3126ec5c934f02b3ed1abe1dd5230a055cb22189a90309b.
No computation or external new theorem. This is a candidate theorem-interface
composition, not proof that the membership hypotheses hold for actual sources.

Let R=C[x,y], A=C[f,g], J(f,g)=1 and
dH=(x dy-y dx)/2-f dg. Let B=A[H] inside R. The positive-order target
derivatives through D=max(deg f,deg g) generate R over A, as proved in the
supplied root report. Then the following are equivalent:

1. F=(f,g) is a polynomial automorphism.
2. B=R.
3. Both D_f H and D_g H belong to B.

Proof of3=>2: D_f and D_g preserve A and, by the hypothesis, preserve B.
Hence every iterated derivative of H belongs to B. Finite derivative
generation recovers R.2=>3 is immediate since these are polynomial source
derivations.1=>2 follows already from A=R.

For2=>1 no external Formanek theorem is needed. Algebraic independence of
f,g and transcendence degree2 give B=A[W]/(P) for one irreducible primitive
polynomial P; its W degree is positive. The Keller identity gives
Omega_(R/A)=0. Under B=R the monogenic presentation makes this module
R/(P_W(f,g,H)) dW. Therefore P_W(f,g,H) is a unit in R, hence a nonzero
constant lambda. The polynomial P_W-lambda lies in the kernel(P), but has
W degree strictly less than P, so it is zero. Thus P=lambda W+p0(f,g),
H belongs to A and R=A. Characteristic zero and the whole polynomial ring's
constant units are essential. The conclusion does not follow from finite
A-algebra generation alone or units on a localization.

Producer controls: automorphisms make all conditions immediate. The punctured
control f=x^2,g=y/(2x),H=0 passes first-order membership but is not a whole
polynomial source, so it cannot extend the theorem to arbitrary affine opens.
The two-polar criterion is a first-order restatement, not an automatic source
membership proof or a newly resolved normality arrow.

Concrete further question, NOT a claimed theorem: for this exact whole-plane
Keller source, does D_f H in B ALONE force invertibility? D_f preserves B;
if conductor stability is used it must be proved for the actual finite graph.
Invariant conductor components would be supported on g-fibres, but vertical
conductor support is not automatically vertical nonproperness. Do not assume
that generic monogenic etale curve projection is finite or that its units
are constants. These are the cheapest exact gaps to test, not licenses to
replace the plane target by a pseudo-plane or produce another relaxed control.
