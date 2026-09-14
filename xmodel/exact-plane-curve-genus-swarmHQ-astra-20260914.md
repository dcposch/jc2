# Exact Liouville forms do not force genus zero for smooth closed plane curves

- Producer: swarmHQ Astra, native task `exact_curve_genus`.
- Basis: `7bc1fdfbad16daef6b5c8bf2c9469953691cfd1d`.
- Evidence tier: MANUAL / PRODUCER-CHECKED. Lifecycle: UNPROMOTED.
- Disposition: REFUTES the proposed universal exactness-to-genus-zero implication; does not refute JC2 or produce an actual Keller fiber.
- Scope: algebraic curves over C, closed and smooth in the affine plane, geometric genus of the smooth projective completion, and exactness with primitive in the coordinate ring itself.
- Method: manual algebra only. No CAS, scientific Python, test, cloud job, external-model lane, external contact, or protected nested repository was used.
- Inputs: charged APPROACHES.md SHA256 `b6004b8634639b5253900cfb71b9298817c4d900cf8ee1105521d18e7c4cbb23`; FALLACY-v2.md SHA256 `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`. No new exit-price assertion.

## Question and outcome

The tested statement was:

> If C is a smooth closed irreducible affine plane curve and x dy is the differential of an element of O(C), then C has geometric genus zero.

This statement is false. Section 1 gives the producer's independently discovered genus-one counterexample, including inverse ring maps. Section 2 checks a simpler example supplied independently by ROOT after the producer announced Section 1's construction. These are same-model manual checks, not different-model FIRST.

For an actual Keller pair J(f,g)=1, a polynomial potential dS=x dy-f dg restricts on f=c to x dy=d(S+cg). The counterexamples show that this exactness property, considered alone for smooth closed plane curves, does not imply genus zero; a proof for actual Keller fibers would have to use additional source information. Neither example below supplies an actual Keller pair, and neither addresses the sufficiency of any such additional condition.

## 1. Independent rational-translation elliptic counterexample

Put

    q=x^3-x,   D=3x^2-1,   B=D^2 y+6x,
    F=4q B^2-D^6,
    C=V(F) in A2_(x,y).

This is a closed affine plane scheme by its literal polynomial equation. We now identify its coordinate ring with an open subset of a smooth elliptic curve; this proves simultaneously that it is reduced, smooth, and irreducible.

### 1.1 The denominators are units on the closed curve

At a root of q, F=-D^6 is nonzero, because gcd(q,D)=1. At a root of D, x^2=1/3, q=-2x/3, and

    F=144q x^2=-32x != 0.

These evaluations exclude every point of C above V(qD). More algebraically, F modulo q is -D^6 with gcd(q,D)=1, so (F,q)=(1) in C[x,y]. Likewise F modulo D is -32x and gcd(D,x)=1, so (F,D)=(1). Hence q and D are units in R=C[x,y]/(F). This is not a replacement of C by an undeclared open subset: the entire closed plane curve already has these units.

An optional explicit check for D is obtained by writing

    H=4qD^3 y^2+48qDxy-D^5+16x(D-1).

Then F=DH-32x, and in R,

    D(3xH-32)=32.

Thus D^(-1)=(3xH-32)/32 is literally an element of R.

### 1.2 Inverse ring maps

Define in R

    v=2qB/D^3.

The defining equation gives

    v^2=4q^2 B^2/D^6=q.

Because q is a unit, v is a unit too. Thus there is a map from

    A=C[x,v,1/(qD)]/(v^2-q)

to R. Conversely, in A define

    y=D/(2v)-6x/D^2.

This gives B=D^3/(2v), hence 4qB^2=D^6, and defines a map R to A. Substitution recovers y and v in both directions. The maps are inverse, so R is exactly the indicated localized elliptic coordinate ring, with no assumed normalization or primitive descent.

### 1.3 Smoothness, irreducibility, and genus

The affine curve E: v^2=x^3-x is smooth: simultaneous vanishing of its two partial derivatives would require v=0 and D=0, inconsistent with v^2=q and gcd(q,D)=1. It is irreducible since q has simple zeros and therefore is not a square in C(x). Its projective closure

    V^2 Z=X^3-X Z^2

has the one point [0:1:0] at infinity, where the Z-partial is nonzero. It is a smooth plane cubic and has genus one. Localizing by qD removes finitely many points without changing its function field or the genus of its smooth projective completion. The ring isomorphism therefore proves that the literal closed plane curve C is smooth, irreducible, and has positive geometric genus.

### 1.4 A regular primitive

Since v^2=q and q'=D,

    dv=D/(2v) dx,
    d(1/D)=-6x/D^2 dx.

Consequently, in Omega^1_R,

    y dx=d(v+1/D),
    x dy=d(xy-v-1/D).

All displayed functions lie in R by the proved unit and ring-map statements. This is exactness with a REGULAR primitive on the smooth CLOSED plane curve, not merely a meromorphic primitive on its normalization.

## 2. ROOT's simpler independent example, checked after exchange

After Section 1's candidate was sent to ROOT, ROOT supplied an independently derived example. This section checks that example but does not claim independent discovery of it. It suffices to take

    p=x^2+x^11 y^3,   C_*=V(p-1),   t=x^3 y.

On C_*, x^2(1+t^3)=1, so x is a unit and v=1/x is regular. The inverse coordinate-ring maps are

    t=x^3 y, v=1/x;
    x=1/v, y=t v^3.

They identify C_* with {v^2=1+t^3, v!=0}. This is a smooth irreducible open subset of a smooth projective cubic of genus one. Hence C_* itself is a smooth CLOSED irreducible plane curve of genus one. Since 2v dv=3t^2 dt,

    x dy=v^2 dt+3t v dv=(1+11t^3/2)dt
        =d(t+11t^4/8),
    y dx=-t v dv=-(3/2)t^3 dt=d(-3t^4/8).

Here the primitive t+11t^4/8 is visibly the restriction of a polynomial in x,y, with no inverse needed.

ROOT subsequently pointed out the same exactness on EVERY nonzero fiber p=c. The identical substitutions give c v^2=1+t^3 and

    x dy=(1/c)(1+11t^3/2)dt
        =d((t+11t^4/8)/c).

For each fixed c!=0 this is a regular polynomial primitive on that closed smooth genus-one fiber. Thus even exactness on all generic fibers of one polynomial is not enough for the proposed conclusion. It is not a Keller control: both partial derivatives of p vanish everywhere on x=0, in the zero fiber. The primitive displayed fiberwise has a pole as a function of the parameter c; no global polynomial Keller coframe has been supplied. The conclusion remains only rejection of the exactness-to-genus-zero shortcut.

## 3. Negative controls and source scope

### 3.1 Omitting the rational translation really loses smoothness and descent

The initial unshifted elliptic construction would use y=D/(2v), giving

    C_0: 4q y^2-D^2=0.

At each of the two roots of D, the point (x,0) lies on C_0 and both partial derivatives vanish. The normalization has two points there with opposite nonzero values of v. A primitive v of y dx on the normalization cannot descend to their identified point, even after adding a global constant. Thus this unshifted construction is NOT a counterexample to the charged smooth-closed-regular statement. The translation by d(1/D)/dx in Section 1 sends both problematic sheets to infinity and, by the explicit polynomial equation and inverse ring maps, repairs exactly these defects.

### 3.2 Exactness is not automatic even in genus zero

On the smooth closed hyperbola xy=1, y dx=dx/x has residue 1 at x=0 on its completion. A rational differential of a function has zero residue at every point, so it has no regular primitive in C[x,x^(-1)]. This checks that the positive examples are using genuine exactness, not a vacuous genus or local-Poincare-lemma test.

### 3.3 What the original discussion does and does not establish

The [original Shende question and Bryant answer, September 2014](https://mathoverflow.net/questions/180815/what-are-the-exact-holomorphic-lagrangians-in-complex-2-space) were read as a discovery source. Bryant proposes taking meromorphic a,b and the image (a,db/da). That construction motivates Section 1, but its image need not itself be smooth or carry a descending regular primitive. The ring checks above, not the discussion's informal general assertion, establish the charged properties. No matching classification theorem was imported.

The bounded searches for exact Liouville/algebraic-curve/genus terminology returned no theorem used in this report. Search snippets about characteristic-p exact differentials and unrelated symplectic geometry are not evidence for the characteristic-zero claim. This was not a broad campaign sweep.

## 4. Consequence, limits, and reproducibility

The cheapest discriminator succeeded without computation: the proposed implication is false under ALL its stated smoothness, closedness, irreducibility, positive-genus, and regular-primitive requirements. ROOT's independent example also defeats the version assuming exactness for every generic fiber. This stops that implication as a route to the accepted rational-generic-fiber criterion. It does not stop every genus argument or every exactness method.

No unproved premise was needed to construct the counterexamples; standard facts used are smoothness of a separable affine cubic, the genus-one formula for its smooth projective completion, and invariance of function-field genus under deleting finitely many points. No claim of literature novelty, actual positive-genus Keller fiber, JC2 counterexample, stronger source exclusion, promotion, or new theorem dependency follows.

Manual replay consists of substituting the two inverse maps in Section 1.2, checking q and D are units as in Section 1.1, checking the cubic's affine and infinite partial derivatives, and differentiating the displayed primitives. Section 2 has its own independent two-line inverse-map and differential check. There is no computational engine/version/certificate claim and no scientific replay command. Administrative publication uses the standard artifact finalizer and its tracked manifest.

Research stopped after the counterexample and the explicitly attributed supplementary check; no genus/degree/embedding family farm, additional source hunt, or automatic successor is selected. No canonical ledger was edited.

## COLLISIONS

MANUAL: EMPTY. No new OPEN identifier is raised and no bounded quantity is commissioned. The only selected discriminator was decided by the explicit counterexamples. The whole-corpus collision scanner was not run; this is not a claim that the examples have no historical or external antecedent. ROOT supplied the canonical-history check for this targeted question, and the known exactness/conductor/surface limitations in APPROACHES.md are not reopened.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10438`.
- Body SHA-256:
  `cc4b968fa6bb49c1686dd36c3d8ae78b4a2b51993df504d9652477cdc9f2e20e`.
- Frozen basis: `7bc1fdfbad16daef6b5c8bf2c9469953691cfd1d`.
