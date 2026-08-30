# Hostile review: nonnormal quadratic content-cone dichotomy

Verdict: **CONFIRM_WITH_CORRECTIONS**.

I read the sealed producer
`xmodel/bd-a2-nonnormal-quadratic-content-cone-dichotomy-sol56-20260830.md`
at commit `dca72076aa1615b0b1286fd4428a1acac7b65963`; its full-file SHA-256
matches `6b324824e0c075b938bd5b7015d4e8d134bad7cb845ac7597212b61d91dfa7a5`.
I also read the three named inputs and the underlying block/nonmonogenic
integrations used by Sections 5-6. The core algebraic dichotomy is correct,
but promotion should include the repairs below.

## Input custody

Confirmed hashes read:

```text
c8dee3199ecfaf73b6debedea625346a11babbe42082cff5bff049f8585763c2
  xmodel/bd-fix3-affine-linear-log-closure-coordinator-integration-sol56-20260830.md

410de2f569e2ad5599152fdd9414198f012dbdced7d17c5a51dde0096fe4601e
  xmodel/bd-fix3-quadratic-discriminant-conductor-coordinator-integration-sol56-20260830.md

ac7ef8f5321f579d5e193b6ae3a9b0f1aa2a64421050bb71426b94258d984ffb
  xmodel/bd-a2-smooth-quadratic-degeneracy-absorption-sol56-20260830.md

ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md

f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

Custody correction: the target calls all three displayed clients "promoted" at
lines 67-79, but `bd-a2-smooth-quadratic-degeneracy-absorption...` is itself
marked `EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED` at its
lines 1-7. The finite common-zero and Stein bridge facts used here are true,
but they must be promoted by the present proof, not by silently treating that
provisional packet as binding.

## 1. Miranda table and intrinsic content

Status: **CONFIRMED**.

The multiplication table in target lines 83-89 is the standard Miranda table
for a trace-zero basis. Directly, for `t=r*z+s*w`,

```text
t^2_E =
  (a r^2 - 2 d r s + c s^2) z
 +(b r^2 - 2 a r s + d s^2) w,
```

so

```text
det((r,s), t^2_E)
= b r^3 - 3 a r^2 s + 3 d r s^2 - c s^3 = Phi(r,s).
```

A global trace-zero basis change is an element of `GL_2(C[u,v])`, whose
determinant is in `C^*`. The binary-cubic coefficient vector is carried by the
rank-four binary-cubic representation with a determinant twist, and both the
matrix and inverse have entries in `C[u,v]`. Therefore the ideal `(a,b,c,d)`
is unchanged. The discriminant principal ideal, the branch support, the local
orders `ord_q(I_B)`, and the minimum coefficient degree over all bases are
intrinsic to the fixed algebra.

Repair: keep saying that the leading form at infinity, the divisor `H`,
projective coefficient basepoints, and projective normality are presentation
data. They are not invariants of the cubic algebra. The target already says
this at lines 114-120; retain it.

The proof that `V(I_B)` has no height-one component is correct. At the generic
DVR of such a component, the special fibre would be `kappa direct-sum V` with
`V^2=0`. A normal finite rank-three order over a DVR has semilocal Dedekind
localization; a length-three local fibre is either unramified of residue degree
three or totally ramified of ramification index three, and the latter has
radical square nonzero. Thus this fibre cannot occur.

## 2. Affine R1 criterion

Status: **CONFIRMED WITH REQUIRED PROOF INSERTION**.

The criterion

```text
X_aff normal iff I_B is not contained in m_q^2 for every q in V(I_B)
```

is correct.

The missing insertion is the full Stein bridge. For
`pi_0:A^2 x P^1 -> A^2`, the sequence

```text
0 -> O(-3) --Phi--> O -> O_X_aff -> 0
```

pushes forward to a locally free rank-three algebra. Off the finite set
`Z=V(I_B)`, the incidence is finite and is the Miranda cubic algebra. Since
both this pushforward and `B` are reflexive over the regular surface `A^2`,
the algebra isomorphism extends uniquely across `Z`; multiplication extends
because it agrees on the dense open. This proves the Stein morphism
`X_aff -> Spec(B)`, isomorphic off `Z`, and identifies the exceptional fibre
over `q in Z` with `{q} x P^1`.

At such a `q`, write

```text
Phi=s*p(X,Y)+t*r(X,Y)+terms in (s,t)^2.
```

Along `E_q`, fibre derivatives vanish and the two base derivatives are
`p,r`. The generic point of `E_q` is singular exactly when `p=r=0` as binary
cubics, equivalently every coefficient has zero first jet, equivalently
`I_B subset m_q^2`. If not, the singular points on `E_q` are a finite
zero-scheme in `P^1`, hence codimension two on the surface. Since `X_aff` is
an integral hypersurface, it is `S_2`; Serre then gives the criterion. No other
affine codimension-one nonnormal locus remains, because away from the
exceptional curves the Stein map is an isomorphism to the normal surface
`Spec(B)`.

## 3. Quadratic content cone

Status: **CONFIRMED WITH WORDING REPAIR**.

If `I_B subset m_q^2`, translate `q` to the origin. Degree at most two then
makes all four coefficients homogeneous quadratics. With

```text
deg(s)=deg(t)=1,  deg(z)=deg(w)=2,
```

the Miranda table is homogeneous and

```text
B=C[s,t] direct-sum C[s,t](-2)z direct-sum C[s,t](-2)w.
```

The ring is a connected positively graded normal domain finite over
`C[s,t]`. Hence `C0=Proj(B)` is a smooth projective integral curve finite of
degree three over `P^1`, with `O_C0(1)` the pullback of `O_P1(1)`. For large
`n`, and already for `n>=2`,

```text
dim_C B_n=(n+1)+2(n-1)=3n-1.
```

Riemann-Roch for `O_C0(n)` gives `3n+1-g`, so `g(C0)=2`.

The clean contradiction should be stated function-field first. For any
nonzero degree-one element `s`,

```text
Frac(B)=C(C0)(s).
```

The promoted first leg gives an inclusion `Frac(B) -> C(x,y)`. Therefore
`C(C0)` embeds in `C(x,y)`, producing a dominant rational map from the rational
surface `P^2` to `C0`; after resolving indeterminacy this is a morphism from a
smooth rational surface to a genus-two curve, impossible. This kills the
content cone and proves affine normality through the R1 test.

Repair: phrase this as a rational-map/function-field contradiction, not as if
the affine morphism to the cone itself automatically extends to a morphism to
`Proj(B)` everywhere.

## 4. Projective R1 and repeated components

Status: **CONFIRMED WITH PRECISION REPAIR**.

Because `X_aff` is normal, every divisorial nonnormal locus of `Xbar` lies in
`H`. Primitivity is correctly handled: a common coefficient divisor other than
`T=0` gives an affine height-one component of `V(I_B)`, and a common `T`
factor would mean all affine coefficients have degree at most one, contrary to
exact quadratic degree. Generic irreducibility plus Gauss gives `Xbar`
integral, hence `S_2`.

At a reduced generic component of `H`, some tangent derivative in
`L_infinity x P^1` is nonzero. If an integral component `C` occurs with
multiplicity `m>=2`, all tangent derivatives vanish generically, and the
normal derivative is exactly the first normal jet `Phi_1|C`. Thus `C` is a
generic `R_1` failure exactly when `Phi_1|C=0`.

The repeated integral component list is exhaustive. For class `(2,3)` on
`P^1 x P^1`, an integral repeated component of class `(alpha,beta)` must
satisfy `m alpha<=2`, `m beta<=3`, `m>=2`; the only possibilities are:

```text
2(0,1)+(2,1)
3(0,1)+(2,0)
2(1,0)+(0,3)
2(1,1)+(0,1)
```

Repair: call this the list of possible repeated integral components with their
residual classes, not the list of all decompositions of `H`. The residual may
split further; the later eliminations are componentwise and still apply.

The bidegree convention is internally consistent: `(1,0)` is a vertical fibre
over a point of `L_infinity`; `(a,1)` maps degree one to `L_infinity` and is a
section when integral.

## 5. Repeated constant sections and vertical fibres

Status: **CONFIRMED WITH SCOPE REPAIRS**.

For a repeated constant section with fibre value `[r:s]`, repetition gives
`Phi_2(r,s)=0` and generic nonnormality gives `Phi_1(r,s)=0`; hence
`Phi(r,s)=Phi_0(r,s) in C`. If this scalar is nonzero, the determinant
criterion makes `1,t,t^2`, `t=r*z+s*w`, a global basis and `B=A[t]`. If it is
zero, the generic binary cubic has the fixed root `[r:s]`, impossible for a
cubic field: the corresponding nonzero trace-zero element would have degree at
most two over the base field, which cannot occur inside a degree-three field.

The monogenic contradiction is licensed by the binding block theorem:
`block-descent-galois-coordinator-integration...` promotes nonmonogenicity of
`B_K` over `C[f,g]` and nonprincipality of the different in its lines 70-107.
The affine-linear packet also records the exact determinant criterion at its
lines 71-79.

For a repeated vertical fibre, the descent is valid. If `ell(U,V)` cuts the
fibre, then

```text
Phi_2=ell^2 P,  Phi_1=ell Q.
```

With affine coordinates `p=ell(u,v)` and complementary `r`, all coefficients
belong to `C[p]`, so the Miranda table defines a finite free rank-three
`C[p]`-algebra `D` and

```text
B=D[r].
```

Since `B` is a normal domain, `D` is a normal domain: an element integral over
`D` in `Frac(D)` is integral over `D[r]`, hence lies in
`D[r] cap Frac(D)=D`. The field identity
`Frac(B)=Frac(D)(r)` and the first-leg function-field inclusion force the
smooth completion of `Spec(D)` to have genus zero. The structure theorem gives
`B subset C[x,y]`, so `B^*=C^*` and hence `D^*=C^*`.

As `D` is the integral closure of `C[p]` in its fraction field, `Spec(D)` is
`P^1` minus the points over `p=infinity`. Over `C`, two or more removed points
give a nonconstant unit, so exactly one point is removed. Therefore
`D=C[t]`, and because the finite map to `A^1_p` has degree three, `p=P(t)` has
degree three. Hence `B=C[p,r][t]`, again monogenic. This excludes hidden
multi-point, residue-degree, and affine-unit escapes.

Repair: say the unit argument uses both the dominant first-leg inclusion
`B subset C[x,y]` and algebraic closedness of the ground field; dominance
alone is not the whole reason.

## 6. Survivor and discriminant degree

Status: **CONFIRMED WITH PROOF DETAIL REQUIRED**.

After the constant and vertical cases are removed, a projective nonnormal
generic component must be a double irreducible `(1,1)` curve. Thus

```text
H=2C+L,       C=(Q=0),       L=(0,1),
```

and unique factorization on `P^1 x P^1` gives

```text
Phi^h=Q^2 L + T Q S + T^2 R,
```

with `Q` irreducible of bidegree `(1,1)` and `L,S,R` fibre forms of degrees
`1,2,3` independent of the base.

The discriminant bound `deg Delta<=6` is also correct, but the proof must
explicitly handle the direction-dependent fibre change. On a generic affine
line `(u,v)=lambda*(u0,v0)`, work over `C(theta)` for the direction
`theta=(u0:v0)`. Since `Q` is irreducible, `Q_theta` is not generically
proportional to the fixed fibre linear form `L`; use

```text
x=Q_theta(X,Y),  y=L(X,Y)
```

as fibre coordinates. The change has determinant `delta(theta) != 0` and is
independent of `lambda`; the binary-cubic discriminant is multiplied by
`delta(theta)^6`, also independent of `lambda`. In the affine chart `y=1`, the
coefficient degrees in `lambda` are bounded by

```text
c0:0,  c1:1,  c2:2,  c3:1.
```

Each term of the cubic discriminant has `lambda`-degree at most six. Therefore
`Delta(lambda*u0,lambda*v0)` has degree at most six for generic direction.
The coefficients of `lambda^k`, `k>6`, are the restrictions of the homogeneous
degree-`k` parts of `Delta`; vanishing on a generic direction forces them to be
zero. No denominator depending only on direction can create a higher total
degree in `lambda`.

## Maximum theorem safe to promote

The following is safe after the corrections above.

Let `B` be the normal finite-flat integral cubic algebra of a proper cubic
intermediate block of a hypothetical noninvertible plane Keller map, with the
promoted dominant first leg and the promoted nonmonogenic obstruction. Suppose
some global trace-zero Miranda basis has coefficient degrees at most two and
at least one coefficient has degree exactly two. Then:

```text
1. The affine incidence X_aff is normal.
2. If the exact projective quadratic incidence Xbar is nonnormal, then every
   generic divisorial nonnormal component lies at infinity.
3. The only surviving repeated type is H=2C+L with C irreducible of bidegree
   (1,1) and L of bidegree (0,1).
4. In that case Phi^h=Q^2 L + T Q S + T^2 R, with Q irreducible (1,1), and
   the intrinsic affine target discriminant satisfies deg Delta<=6.
```

Do not promote more. The blowup `(T,Q)`, normalization/conductor quartic,
genus-one obstruction, basis-orbit coverage, polynomial-map construction,
counterexamples, and any JC2 conclusion remain separate and unproved here.

## Cheapest decisive successor

The cheapest next packet is a local normalization/conductor theorem for

```text
Phi^h=Q^2 L + T Q S + T^2 R
```

along the generic double curve `C=(T=Q=0)`. Prove, without CAS, that the
blowup chart giving `W^2 L+W S+R=0` is the normalization in the required
cases, compute the conductor over `C`, and split the quartic discriminant into
square, split, and two-branch cases. Only after that bridge is proved should
the genus-one heuristic be connected to the promoted rational-boundary forest.

No `jc2-lean` material was inspected or used, and no heavy CAS or Singular
calculation was run.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13335`.
- Body SHA-256:
  `b541732a6ea433de59e91a22a85d19913145bdbc620c5001cf701ac006c73df4`.
- Frozen basis: `dca72076aa1615b0b1286fd4428a1acac7b65963`.
