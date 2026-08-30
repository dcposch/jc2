# Hostile review: quadratic trace-zero basis-change coverage

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The producer's internal algebra is substantially correct: the Miranda
transformation law, content and discriminant invariance, the top-degree
leading-section obstruction, affine-linear shear reduction, the shear
degree-band calculation, and the displayed normal monogenic counterexample all
check out. The correction is a campaign-scope one. The proper-block file
actually charged in Section 4,
`xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md`,
does not itself promote nonmonogenicity. The affine-linear constant-only
proper-block corollary is licensed only after either adding nonmonogenicity as
an explicit hypothesis or also charging the actual Galois/nonmonogenicity
integration `f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8`.

Custody checks: the repository head is
`002d4a88b3496838a3ff8cf3bf55ec5cedbdb5a4`. The reviewed producer body is
`16198` bytes with SHA-256
`bef1361e4eb32211b857a67290ecf335b2f284d3938023c83dbdb121fe841130`.
The charged sandwich file has whole-file SHA-256
`ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778`
and body SHA-256
`85db7afd1e8b9f1039bbf977b78a6ea1f64cef9b6fb9323f2233281cf1be6e9f`.

## Itemized audit

1. `CONFIRMED`: transformation law and intrinsic invariants.

With the producer's convention

```text
Phi_e(X,Y)=bX^3-3aX^2Y+3dXY^2-cY^3,
```

and with `e'=e*g`, a new coordinate column `x` has old coordinates `gx`.
The trace-zero coordinate column of the square is converted back to the new
frame by `g^{-1}`. Therefore

```text
Phi_(e')(x)=det(g)^(-1) Phi_e(gx).
```

If `x,y` are the two columns of `g` and `T_Phi(x,x,x)=Phi(x)`, expansion gives
exactly

```text
b' = det(g)^(-1) Phi(x),
a' = -det(g)^(-1) T_Phi(x,x,y),
d' =  det(g)^(-1) T_Phi(x,y,y),
c' = -det(g)^(-1) Phi(y).
```

The signs match the `b,-3a,3d,-c` convention. Since
`GL_2(C[u,v])` has determinant in `C^*`, the determinant twist does not change
degree. The coefficient vector is acted on by an invertible rank-four matrix
over `C[u,v]`, with inverse supplied by `g^{-1}`; hence `(a,b,c,d)` generates
the same content ideal in every trace-zero frame. The trace Gram determinant
changes by `det(diag(1,g))^2=det(g)^2`, hence only by a scalar square. Content
and trace discriminant are intrinsic in this frame groupoid; coefficient
degree, leading infinity cubic, projective basepoints at infinity, and
projective incidence normality are not.

2. `CONFIRMED_WITH_CORRECTIONS`: arbitrary-matrix leading-section theorem.

Let `Phi_d` be the highest nonzero homogeneous target part of the coefficient
cubic, `d<=2`, and let `g_m` be the highest nonzero homogeneous target part of
a nonconstant polynomial matrix `g`, `m>0`. Since `det(g)` is constant, the
degree-`2m` determinant term is `det(g_m)=0`. The matrix `g_m` is nonzero, so
over `C(P^1)` it has generic rank one.

The degree `d+3m` term of `Phi(gx)` is uniquely `Phi_d(g_mx)`: every lower
coefficient part lowers the target degree, and every lower matrix part lowers
one of the three input degrees. Since the transformed coefficients have degree
at most two and `d+3m>2`, this term vanishes. For the generic rank-one matrix,
`g_mx` spans its image line, so `Phi_d` vanishes on that line.

Write the image line after cancelling common factors as `[R:S]`, with
`R,S` coprime homogeneous forms of the same degree `e`. The graph is cut out
by `S X - R Y`. The vanishing of `Phi_d(U,V;R,S)` puts `Phi_d` in the saturated
graph ideal, which is principal, so `S X - R Y` divides `Phi_d`. Comparing
bidegrees gives `e<=d<=2`. Basepoints and rank drops at special target
directions do not defeat the argument; they only get absorbed in the cancelled
common factor before `[R:S]` is formed.

For an actual quadratic frame, the only divisor-class decompositions of the
leading `(2,3)` form after extracting the section are

```text
(0,1)+(2,2),
(1,1)+(1,2),
(2,1)+(0,2).
```

The residual `(0,2)` splits over `C`, with multiplicity. Applying the same
argument to `g^{-1}=det(g)^(-1)adj(g)` is legitimate: `adj(g_m)` is nonzero
rank one over the generic field, has the same entry degree `m`, and its image
is `ker(g_m)`. The producer should add the saturated-graph/gcd sentence above
so the theorem is immune to basepoint objections.

3. `CONFIRMED_WITH_CORRECTIONS`: affine-linear unimodular matrices.

If every entry of `g` has degree at most one, then `g(0)` is invertible because
`det(g)` is a nonzero constant. Replacing `g` by `g(0)^{-1}g` gives
`g=I+L`, with `L` homogeneous linear and `det(I+L)=1`. Separating degrees gives
`tr(L)=0` and `det(L)=0`, so the linear span of the coefficient matrices lies
in the nilpotent cone in `sl_2`. Its projectivization is a smooth conic in
`P(sl_2)` and contains no projective line; therefore the span has dimension at
most one. Thus `L=p(u,v)N` with `p` linear and `N^2=0`.

A constant conjugation carries `N` to an elementary nilpotent, giving the
normal form

```text
g = [[1,-p],[0,1]],       Phi'(X,Y)=Phi(X-pY,Y),
```

after constant changes of the source and target frames. The only repair is
wording precision: before the conjugation step, constant frame changes act as
`g -> C^{-1} g D`; after the normalization `g(0)=I`, one may take `C=D` to
conjugate the fixed nilpotent. Constant changes preserve the degree cap,
fixed constant roots, and monogenicity.

4. `CONFIRMED_WITH_CORRECTIONS`: shear expansion and the exact use of
nonmonogenicity.

The expansion for `g=[[1,-p],[0,1]]` is correct:

```text
b'=b,
a'=a+bp,
d'=d+2ap+bp^2,
c'=c+3dp+3ap^2+bp^3.
```

For homogeneous linear nonconstant `p`, the degree bands force exactly

```text
b in C,
a_2=0,
d_2=-a_1 p - (b/3)p^2.
```

Necessity: the degree-three part of `a+bp` gives `b_2=0`; the degree-three
part of `d+2ap+bp^2` gives `2a_2+b_1p=0`; the degree-four part of `c'` is then
`-(1/2)b_1p^3`, hence `b_1=0` and `a_2=0`; the remaining degree-three part is
`3p(d_2+a_1p+(b/3)p^2)`. Sufficiency is immediate by substituting these
conditions back into the four displayed formulas.

For arbitrary nonconstant `p`, the producer's weaker dichotomy is also
correct. If `deg(p)>=3`, the equations successively force `b=0`, `a=0`,
`d=0`. If `deg(p)=2` and `b!=0`, then `a+bp` first forces `b` constant, and
the top part of `d+2ap+bp^2` forces `a_2=-(b/2)p_2`; the degree-six part of
`c'` is then `-(1/2)b p_2^3`, impossible. Thus `deg(p)>=2` forces `b=0`.
For `deg(p)=1`, the exact linear classification above applies.

The final dichotomy is:

```text
b=0      => Phi(1,0)=0, a fixed constant projective root;
b in C^* => det(z,z^2)=b is a unit, so 1,z,z^2 is a global basis and B=A[z].
```

Here the two exclusions use different hypotheses. The fixed-root case is
forbidden by the generic cubic-field condition: over `Frac(A)`, a nonzero
trace-zero element with `1,t,t^2` dependent would generate degree at most two,
contradicting a degree-three field. The `b in C^*` case is forbidden only by
nonmonogenicity. The sandwich input charged in Section 4 promotes the
existence and structure of `Y=Spec(B_K)` and says `Y` is not `A^2`; it does
not state `B_K` is nonmonogenic. The actual promoted-looking source for that
is `xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md`,
lines 70-75, whole-file hash
`f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8`.

So the algebraic statement "integral cubic-field plus nonmonogenic implies no
nonconstant affine-linear quadratic-to-quadratic change" is confirmed. The
proper-block corollary as charged only to `ba69...` has a citation-scope gap.

5. `CONFIRMED`: normal finite monogenic counterexample.

For

```text
B=C[u,v,t]/(t^3-u^2t-v^2),
```

the cubic is irreducible over `C(u,v)`: any rational root of the monic
polynomial is integral over `C[u,v]`, hence polynomial, and specialization at
`u=0` would give a polynomial cube root of `v^2` in `C[v]`. The hypersurface
singular equations

```text
3t^2-u^2=0,  -2ut=0,  -2v=0
```

have only the origin as solution. The domain is a hypersurface, hence
Cohen-Macaulay, and it is regular in codimension one; therefore it is normal.
It is finite free of rank three over `C[u,v]`.

With

```text
z=t,       w=t^2-(2/3)u^2,
```

both elements are trace zero, and they form the trace-zero frame. The products
give

```text
z^2 = w + (2/3)u^2,
zw  = (1/3)u^2 z + v^2,
w^2 = v^2 z - (1/3)u^2 w + (2/9)u^4,
```

so

```text
Phi = X^3-u^2XY^2-v^2Y^3,
(a,b,c,d)=(0,1,v^2,-u^2/3).
```

The nonconstant determinant-one change `z'=z`, `w'=w-uz` gives

```text
Phi' = X^3-3uX^2Y+2u^2XY^2-v^2Y^3,
(a',b',c',d')=(u,1,v^2,2u^2/3).
```

Both coefficient sets have cap two and content ideal `C[u,v]`. A constant
projective root would have to satisfy the coefficient of `v^2`, hence
`Y=0`, but then the `X^3` term survives; this works for both `Phi` and
`Phi'`. The affine incidence is finite because the fibre binary cubic is
never the zero cubic. At target infinity the leading forms

```text
Phi_2  = -Y^2(u^2X+v^2Y),
Phi'_2 =  Y^2(2u^2X-v^2Y)
```

are nonzero for every `[u:v] in P^1`, so the projective incidence remains
fibrewise finite, but the infinity divisor is nonreduced. The discriminant is

```text
Delta=4u^6-27v^4.
```

The algebra is monogenic, trivially `B=C[u,v][t]=C[u,v][z]`. This refutes the
broad heuristic "nonconstant change forces a fixed full root, nonunit content,
or nonfiniteness." It does not refute the nonmonogenic proper-block theorem;
indeed it demonstrates why nonmonogenicity is the load-bearing extra input.

6. `CONFIRMED_WITH_CORRECTIONS`: maximum safe promotion and remaining gap.

The safe promoted result is:

```text
Given two already existing quadratic trace-zero frames of a finite locally
free rank-three C[u,v]-algebra with free trace-zero module, any nonconstant
polynomial change between them forces section components in the two leading
infinity cubics, supplied by im(g_m) and ker(g_m). If the change has entry
degree at most one, then up to constant frame changes it is a single linear
elementary shear; in a generic cubic-field algebra that is nonmonogenic, this
affine-linear case cannot occur.
```

This does not prove that a quadratic frame exists. It only classifies and
obstructs changes among frames already in the degree-two sublevel. The
discriminant statement is also correctly one-sided: since the cubic
discriminant is quartic in the coefficients, a displayed degree-`d` frame
gives `deg(Delta)<=4d`, hence
`d_min >= ceil(deg(Delta)/4)` when `Delta` is nonzero. This is a lower bound,
not an upper bound or existence theorem.

The exact remaining gap is the entry-degree-at-least-two orbit:

```text
classify g in GL_2(C[u,v]), deg(g)>=2, such that
Phi and det(g)^(-1)Phi(gX,gY) both have coefficient cap two,
under generic irreducibility and nonmonogenicity.
```

The leading-section theorem gives only necessary boundary section flags. It
does not exclude higher-degree cancellations among lower homogeneous bands,
does not turn the boundary section into a fixed full generic root, and does
not show monogenicity. Factoring `g` into elementary matrices is not enough,
because intermediate frames need not remain under the quadratic cap and
`GL_2(C[u,v])` is not exhausted by a cap-preserving elementary path argument.

## Precise repairs

1. At the endpoint and Section 6, keep "proper-block integral and
nonmonogenic scope", but cite nonmonogenicity separately. The charged
`ba69...` sandwich file supplies normal finite block structure and missed
branch divisors, not nonmonogenicity. Add `f972...` or demote the
proper-block corollary to the explicit hypothesis "assuming `B/A` is
nonmonogenic".

2. In Section 2, add the gcd/saturated-graph sentence: after cancelling the
common factor of the generic image vector, `[R:S]` is a morphism
`P^1 -> P^1`; the graph ideal `(S X - R Y)` is principal and saturated, so
vanishing on the graph implies divisibility. This closes the basepoint and
special-rank-drop objection.

3. In Section 3, replace "constant conjugation" by the precise frame action:
constant frame changes send `g` to `C^{-1}gD`; after normalizing `g(0)=I`,
one may take `C=D` to conjugate the fixed nilpotent to an elementary matrix.

4. In Section 4, state explicitly that the affine-linear contradiction uses
two inputs: generic degree-three field for the fixed-root branch, and
nonmonogenicity for the unit-determinant branch. Do not let
`Y not isomorphic A^2` stand in for nonmonogenicity.

## Cheapest decisive successor

First do the paper-only homogeneous-band problem for `deg(g)>=2` with

```text
g_m = h(U,V) * r(U,V) * ell(U,V)^T
```

and `Phi_2` in each of the three factor classes
`(0,1)+(2,2)`, `(1,1)+(1,2)`, `(2,1)+(0,2)`. Compare the next descending
target-degree bands of `Phi(gx)` and of the inverse transform, retaining the
image and kernel section flags. The decisive target is either a theorem that
these bands force a fixed generic root or a unit value of `Phi`, or an explicit
nonmonogenic quadratic-to-quadratic high-degree change. Until one of those is
done, entry-degree-at-least-two matrices remain genuinely open.

<!-- BODY-END -->
