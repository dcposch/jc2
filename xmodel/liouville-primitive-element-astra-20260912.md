# Liouville primitive as a field generator

Manual independent co-research, not promotion. First action2026-09-12 12:09:59 UTC; original reserve12:25/HARD12:28 unchanged. COORDINATION and TASK hashes matched; both freshly read WHOLE in order. Own output destinations absent. No other mathematical input or scientific execution.

## Exact quantity

For polynomial f,g over C with J(f,g)=1 and dS=x dy−f dg, decide whether C(f,g,S)=C(x,y). ROOT's suggested route is unreviewed guidance, not an accepted theorem. Ring equality, finite/injective lift and JC2 are separate claims.

## Result

YES, at the stated field level. For every f,g in C[x,y] with J(f,g)=1 and every polynomial S satisfying dS=x dy-f dg,

    C(f,g,S)=C(x,y).

This is a MANUAL theorem candidate requiring independent review, not a JC2 result. The proof below independently fills the suggested derivation-descent and polynomial-Luroth steps; it does not assume an integrated multiplicative-group action on the intermediate field.

## 1. Derivation descent

Write L=C(x,y), F=C(f,g), K=F(S). The Jacobian identity makes f,g algebraically independent. Thus L/F is a finite extension: it is finitely generated and algebraic because both fields have transcendence degree two. Characteristic zero makes it separable. Consequently the derivations partial_f, partial_g on F extend uniquely to K and L, compatibly with inclusion. Explicitly, for an algebraic element a with separable minimal polynomial m, extension is forced by D(a)=-(D m)(a)/m'(a); this also proves its value belongs to the relevant intermediate field.

On L, inverse-Jacobian differentiation gives

    partial_f = g_y partial_x-g_x partial_y,
    partial_g = -f_y partial_x+f_x partial_y.

Applying these to dS=x dy-f dg yields

    S_f=-x g_x,       S_g=x f_x-f.

Both belong to K. For E=x partial_x it follows that

    E(f)=f+S_g,       E(g)=-S_f,       E(S)=f S_f.

The last equality follows from S_x=-f g_x and must not be omitted: preservation of f and g alone would not establish preservation of F(S). Since f,g,S generate K as a field, the product and quotient rules now imply E(K) is contained in K. This proves descent directly, without a prior group-action assertion.

## 2. Finite weight projections and the axis equation

If A=sum_(i=0)^N x^i A_i(y) is polynomial and belongs to K, then E acts on its i-th term by multiplication by i. Finite interpolation therefore gives

    x^i A_i(y) = [product_(0<=j<=N,j!=i) (E-j)/(i-j)] A in K.

All denominators here are nonzero complex constants. No infinite series, analytic integration or parameter specialization is involved. Applying this separately to f and g puts f_0(y), g_0(y), x f_1(y), x g_1(y) in K, with missing coefficients interpreted as zero. Restriction of the original polynomial Jacobian identity to x=0 is

    f_1 g_0' - f_0' g_1 = 1.                         (1)

Thus f_0,g_0 are not both constant, and f_1,g_1 are not both zero.

## 3. Polynomial generator, including the constant cases

Here is a proof of the needed polynomial-Luroth refinement, rather than an assumption that a rational generator is polynomial. Put M=C(f_0,g_0), a nonconstant subfield of C(y). The extension C(y)/M is finite. Let X be the smooth projective complex curve with function field M; the field inclusion gives a finite morphism pi:P1_y -> X. Riemann-Hurwitz,

    -2=deg(pi)*(2 genus(X)-2)+total ramification,

forces genus(X)=0. A smooth projective genus-zero curve over C is P1. Choose a nonconstant polynomial u among f_0,g_0. On P1_y its only pole is infinity. On X its pole support must therefore be a single point q, and the support of pi^*(q) is only infinity: orders in a finite pullback are positive, so any further pole or point above q would produce another pole of u on P1_y.

Choose a coordinate h on X=P1 with its unique simple pole at q. Its pullback has no finite pole on P1_y, hence h belongs to C[y] and is nonconstant. The same pole argument says f_0,g_0 are regular on X minus q. Consequently

    M=C(h),       f_0=F_0(h),       g_0=G_0(h)

for polynomials F_0,G_0 in C[T], allowing either to be constant. By the chain rule (1) becomes the polynomial identity

    1=h'(y)*( f_1 G_0'(h)-F_0'(h) g_1 ).             (2)

Thus h' is a unit in C[y]. Characteristic zero gives deg(h)=1, so y belongs to M and hence K. To check all constant cases explicitly: both f_0,g_0 constant contradict (1); if f_0 is constant then f_1 g_0'=1 forces g_0 linear and f_1 a nonzero constant; if g_0 is constant the symmetric identity -f_0' g_1=1 does the same. No zero polynomial was divided by.

The curve argument uses only the usual smooth projective model of a one-variable function field, finite-curve Riemann-Hurwitz and the genus-zero classification over C. It assumes neither rational singularities nor any plane Keller conclusion.

## 4. Recovering x and the precise conclusion

By (1), at least one of f_1,g_1 is a nonzero polynomial a(y). We already have y in K, so a(y) is a nonzero element of K; the weight projection gives x a(y) in K. Division in the FIELD K yields x in K. Hence K=L, as asserted. Zeros of a(y) on divisors are harmless for this field argument but are exactly why it supplies no ring-generation assertion. Adding a constant to S changes neither K nor the proof. For the identity pair f=x,g=y one can take S constant; the conclusion still holds because F=L. The proof does not require S to be nonconstant in degree one.

## 5. Controls and stronger readings

A genuine counter-control to extending the theorem to rational pairs on a punctured plane is

    x!=0,       f=x^2,       g=y/(2x),       S=xy/2=fg.

Direct differentiation gives J(f,g)=1 and f dg=(x/2)dy-(y/2)dx, so dS=x dy-f dg exactly. Nevertheless F(S)=F is a proper degree-two subfield of L. Indeed L=F(x), x^2=f, y=2gx, and the nontrivial involution (x,y)->(-x,-y) fixes f,g,S. The global polynomial/axis hypothesis has been removed: this is NOT a counterexample to the stated full-plane theorem and is unrelated to ROOT's separately owned saturation-control construction.

Field equality alone does not entail ring equality or finiteness: the elementary non-Keller ring C[x,xy] has fraction field C(x,y) but omits y, and its associated map collapses x=0. This only controls the field-to-ring inference, not a stronger theorem under all the original Keller hypotheses. No actual polynomial Keller counterexample to C[f,g,S]=C[x,y], finiteness, graph normality or injectivity is supplied. Those stronger readings remain UNESTABLISHED here, not REFUTED. Individual-divisor saturation and JC2 likewise remain open; no denominator control is hidden in step 4.

## 6. Immediate source consequence and stopping point

The distinguished Liouville potential, up to an additive constant, is itself a primitive element; no generic linear choice of an auxiliary is needed. Thus (f,g,S) is birational onto its algebraic image, the minimal polynomial of S over F has degree [L:F], and its values distinguish the geometric generic fiber. These are generic function-field statements. They do not control special fibers, discriminant divisors, integral closure, or the missing individual-divisor saturation needed by stronger source attachments. Existence of the primitive S as a polynomial is automatic exactness, not the new quantity tested here. No literature priority or global novelty finding is asserted, and there is no downstream allocation or execution authority.

## Quantity, self-check and remaining gap

The one quantified field-generation statement is settled by the displayed identities for arbitrary polynomial coefficients; zero uncovered proof cases remain in this manual argument. The cheapest discriminator is an independent manual check of E(S), the unique-pole polynomial-generator step, and recovery of x by a nonzero coefficient. A five-minute review allocation would be UNMEASURED planning, not observed runtime or an authorized test. The remaining gap is independent review and any stronger special-divisor/source consequence, not a deferred polynomial computation. Self-check included the identity pair, both constant-coefficient cases, the punctured-plane degree-two control, field-versus-ring scope, and all derivation signs. Own-only output-collision checks precede sealing; no canonical OPEN or charge_basis is declared.

## Read scope and closeout

Exactly two inputs, both FRESH_WHOLE: COORDINATION806lines in1–220,221–440,441–660,661–806 and TASK entire. All links inert. No literature, old proof, live peer, source/code, scientific interpreter/helper/import/AST/syntax/test/CAS/dummy, network/worker/agent, corpus/protected/shared access. Only inert text/hash/UTC/JSON/presence and apply_patch, plus existing artifact_finalize administrative publication. Final WHOLE/postpins/quantity/scope/collision checks precede marker LAST. No canonical OPEN or charge_basis.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8899`.
- Body SHA-256:
  `4188592722733d09456b15b08f72fa34153ebfdc80be7a33ffe731cfb7d07787`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
