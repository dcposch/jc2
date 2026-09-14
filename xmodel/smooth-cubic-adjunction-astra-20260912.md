# Positive sectional genus: smooth finite cubic donor exclusion

First action 2026-09-12 02:28:23 UTC; reserve 02:51 / HARD 02:54 unchanged.
Original TASK SHA a0ce883a9b9c26a711f6d357f6dfed8cfb708e2511df9192334d8566e4423196
matched before fresh WHOLE read. One separately authorized valuation
delta was subsequently pinned and freshly WHOLE-read. Manual co-research
only, not promotion; both exact scopes are recorded in PINS.json.

## Verdict and standard tools

Let φ:Y→P² be a finite degree-three morphism of complex surfaces, with Y
smooth, rational and projective. Put L=φ*O(1), R=div(det dφ)∼K_Y+3L and
g=1+(K_Y+L)·L/2. For a target line ℓ set
U=Y−(SuppR∪Suppφ*ℓ). The proposed exclusion holds: if g≥1, then for EVERY target line ℓ there
is no dominant regular morphism A²→U. No degree bound on this morphism is
needed. This is an independently derived producer proof, still unreviewed.

Standard tools used at their usual precise scope are: Riemann–Roch and
Serre duality on a smooth projective surface; finite Cohen–Macaulay maps
to a smooth surface are flat; embedded resolution of complex surface
divisors and resolution of a rational map of smooth projective surfaces
by point blowups; and the discrepancy criterion that a simple-normal-
crossing pair with coefficients≤1 is log canonical. The crucial local
discrepancy calculation and logarithmic pullback are supplied below rather
than replaced by a singular-boundary adjunction assertion.

## 1. Cubic fibres force a tame local different

The finite map φ is flat: at a target local regular ring of dimension2,
its parameters form a parameter sequence on each source local ring above
it; source smoothness gives Cohen–Macaulayness. The finite direct-image module has
depth2 and hence is locally free over that regular ring. Its rank is3,
so each local scheme fibre length n is at most3.

The differential cannot have rank0. Otherwise the two pulled-back target
parameters f,g lie in the square of the source maximal ideal m. Modulo
m³ their degree-two initial forms span at most a two-dimensional subspace
of the three-dimensional m²/m³. Thus the fibre quotient has length at
least1+2+1=4, a contradiction.

In convergent complex coordinates choose the first target parameter as
a source coordinate s, so φ=(s,h(s,t)). At the point in question,
ord_t h(0,t)=n≤3; the different is h_t, up to a unit. If n=1 it is a
unit; if n=2 its derivative in t is nonzero, so its zero divisor is
smooth and reduced. If n=3, Weierstrass preparation and completing the
square give

    h_t = unit·(t²+a(s)),       a(0)=0.

When a is nonzero, write a=s^m u(s), u(0)≠0, and absorb a holomorphic
m-th root of u into s: the divisor is t²+s^m, m≥1. When a≡0, it is
twice a smooth divisor. These local forms also establish that every
coefficient of the global ramification divisor R is at most2.

## 2. Explicit log canonicity of (Y,R/2)

A unit gives the empty boundary; a reduced smooth divisor with coefficient
1/2 is klt; twice a smooth divisor becomes coefficient1 and is log
canonical. For t²+s^m with m=1 the reduced curve is smooth, and for m=2
it is two transverse complex lines, each with coefficient1/2.

For m≥3 blow up the origin. In the chart t=st1,

    π*(t²+s^m)=s²(t1²+s^(m−2)),
    K_new=π*K_old+E.

Consequently

    K_new+(1/2)R_strict = π*(K_old+(1/2)R_old).

The crepant boundary has coefficient0 on the exceptional curve. In the
other chart s=ts1, the strict transform has equation
1+t^(m−2)s1^m=0 and misses the exceptional curve. Thus the only remaining
potential singularity is exactly the same problem with exponent m−2.
Iteration ends at m=1 or2, with all introduced exceptional coefficients0.
The final pair is klt: its nonzero boundary is a smooth half-divisor or
two transverse half-divisors. Tangencies to zero-coefficient exceptional
curves do not change this pair. Crepant invariance of discrepancies proves
the original pair klt in these finite-m cases, hence log canonical in
ALL cases. These analytic point-blowup calculations compute the same
algebraic divisorial discrepancies. No assertion that R_red itself is
log canonical was used.

The separately supplied ROOT valuation argument is also valid and gives
an independent all-valuation check. At a generic divisor on a smooth
model, for regular f,g, expansion in a uniformizer gives
ord(df∧dg)≥v(f)+v(g)−1. Cancellation can only increase this order.
For local coordinates s,t put a=v(s), b=v(t), A=1+ord(ds∧dt).
Then A≥a+b. For r=t²+a(s), the exact identity dr∧ds=2t dt∧ds gives
v(r)+a−1≤b+A−1, hence v(r)≤A+b−a≤2A. Here the repeated letter in a(s)
denotes the analytic function, not the integer v(s). This proves the
required nonnegative log discrepancy, including a(s)≡0. At point-centred
exceptional valuations a,b>0; base divisors are covered by the already
established multiplicity bound. Units and invertible analytic coordinate
changes preserve the claim. No guessed resolution or cancellation
assumption is concealed in this alternative.

## 3. Adjoint section and the full-boundary inequality

Rationality gives χ(O_Y)=1. Riemann–Roch and duality yield

    χ(K_Y+L)=1+(K_Y+L)·L/2=g,
    h²(K_Y+L)=h⁰(−L)=0.

Therefore h⁰(K_Y+L)=g+h¹(K_Y+L)≥1. Cube a nonzero section, using
2K_Y+R∼3(K_Y+L), to obtain a nonzero section
τ∈H⁰(Y,2K_Y+R). It is a rational tensor-square of a top form, regular
away from SuppR, with allowed pole divisor R.

Fix ANY ℓ and resolve B=SuppR∪Supp(φ*ℓ) by ρ:Y'→Y, isomorphic over U.
Let B'=Y'−U with reduced structure. Choose compatible canonical divisors.
For a strict R-component of multiplicity m, the coefficient of

    2(K_Y'+B')−ρ*(2K_Y+R)

is2−m≥0; for any other strict boundary component it is2. For an exceptional
divisor E, write k_E=ord_E(K_Y'−ρ*K_Y) and m_E=ord_E(ρ*R). Its coefficient
is2k_E+2−m_E=2(a(E;Y,R/2)+1)≥0 by the just-proved log canonicity.
Every exceptional divisor lies in B' because all centres are in B.
The entire displayed divisor is effective. Consequently the birational
pullback of τ lies in H⁰(Y',2(K_Y'+B')). This controls exceptional poles,
not merely strict-boundary multiplicities.

Extra blowups for a singular, tangent, coincident, or nonreduced pullback
of ℓ cause no gap: the inequality concerns EVERY exceptional valuation,
and B' is reduced but includes them all. No generic-line replacement is
made. The chosen adjoint section and its existence do not depend on ℓ.

## 4. Logarithmic pullback and the infinity contradiction

Suppose f:A²→U is dominant and regular. Resolve the induced rational map
P²⇢Y' by point blowups π:X→P² only over infinity; it was already regular
on A². Obtain a morphism fbar:X→Y' and reduced SNC boundary D=X−A².
Because f(A²)⊂U, the inverse image of B' is supported on D.

The logarithmic pullback is regular. In SNC coordinates a target boundary
equation y_i pulls back locally as a unit times monomials in source
boundary equations, so d(fbar*y_i)/(fbar*y_i) is logarithmic. Target
coordinates not defining boundary give regular differentials. Wedges
therefore define fbar*Ω²_Y'(log B')→Ω²_X(log D), and its tensor square
pulls τ to a section of 2(K_X+D). Dominance in characteristic zero makes
the differential generically invertible, so this section is nonzero.
Original f need not be proper or unramified.

On A² write it as h(x,y)(dx∧dy)² for a nonzero polynomial h, of degree d≥0.
At the generic point of infinity use x=1/u, y=v/u. Then

    dx∧dy=−u^(−3)du∧dv,
    h(1/u,v/u)=u^(−d)(h_d(1,v)+terms divisible by u),

where h_d(1,v) is not the zero polynomial. Thus the bicanonical form has
pole order d+6≥6 along the strict transform of infinity. Finitely many
point blowups do not change this generic valuation. A section of
2(K_X+D), however, has pole order at most2 there. Contradiction.

## 5. Controls, exact scope and completion audit

Naively replacing R by its reduced support on Y would not control
exceptional poles; the discrepancy calculation above is indispensable.
Nor is a generic smooth target line substituted for the specified line.
The local fibre-length bound uses both finiteness and smooth source and
target; it is not licensed for an arbitrary singular cubic normalization.
Rationality supplies χ(O_Y)=1; genus zero does not supply the adjoint
section by this argument. The proof makes no assertion about that case,
other compactifications, actual Keller pairs or JC2. The theorem applies
to this smooth finite cubic donor and excludes dominant regular A² maps
of every possible degree to its stated open subset.

Mathematical OPEN quantity within this stated theorem: zero. Required
next validation: one independent manual review of the local divisor,
full-boundary discrepancy and logarithmic-pullback arguments. Its cost
and outcome are UNMEASURED; this is not an execution request. No code,
coefficient payload, scientific subprocess, external lookup or peer
source was used. All reasoning above is manual. Publication readback,
input postpins and collision checks are documentary operations only.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9184`.
- Body SHA-256:
  `80fe7b4d38f5a253f469f4102d6f8f3291d935e2d73e226c85b5c9ce69185577`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
