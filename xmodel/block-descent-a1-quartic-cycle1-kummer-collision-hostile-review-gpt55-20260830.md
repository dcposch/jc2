# Hostile review: quartic inverse-Kummer collision control

Date: 2026-08-30
Reviewer: GPT-5.5 hostile mathematical referee
Scope: exactly the six charged files named in the assignment, plus a narrow external check of the Formanek bibliographic source.

## 0. Custody reproduction

The six charged SHA-256 hashes were recomputed before mathematical review.

```text
bcc5148aba1a6cb095401ae8871e184ba6bb3e540395a23c40edc16cb0e363a8
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md
2e8e73514d1743cdc90934f099eccffc75ef2c4d5a07a5956bbb71cf8dc08aa5
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md.artifact.json
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
70c1e16270564af7138cdc9f4b4ef396a17b398698694330ee5146ec8a273f5d
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md.artifact.json
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190
  xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
baaf9e2253135c9885ccc420e99f3538441c8d664dfe724686a6d5b968e500b6
  xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md.artifact.json
```

All six match the assignment. No `CUSTODY_FAIL` condition occurred.

The Markdown seal blocks and artifact manifests were also reproduced.

```text
block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md
  seal body bytes: 25518
  recomputed body bytes: 25518
  seal body sha256: fb9cbef56a55ca129cb5f6320c1ffa9e6de555c830ab7b83913dc9cd67ccd44a
  recomputed body sha256: fb9cbef56a55ca129cb5f6320c1ffa9e6de555c830ab7b83913dc9cd67ccd44a
  frozen basis: 7ff3257e9a5f944580cef9c7961296b6ca1db50c
  artifact file_bytes: 25851
  artifact full_sha256: bcc5148aba1a6cb095401ae8871e184ba6bb3e540395a23c40edc16cb0e363a8
  artifact published_mode: 0444
  custody opened_utc: 2026-08-30T22:48:08Z
  custody closed_utc: 2026-08-30T23:00:03Z
  custody finalized_utc: 2026-08-30T23:00:10Z
  custody lease_id: 5c035cacf5b26eccc6e778df084d9156
  custody owner: rank4_cycle1_function_pair
  custody source_bytes/source_sha256: 25518 / fb9cbef56a55ca129cb5f6320c1ffa9e6de555c830ab7b83913dc9cd67ccd44a
  schema: jc2.artifact-finalize/v1

block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
  seal body bytes: 21468
  recomputed body bytes: 21468
  seal body sha256: ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d
  recomputed body sha256: ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d
  frozen basis: 06a4110854d7ad38525daccfa7895943259a3812
  artifact file_bytes: 21801
  artifact full_sha256: 0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  artifact published_mode: 0444
  custody opened_utc: 2026-08-30T22:25:55Z
  custody closed_utc: 2026-08-30T22:37:37Z
  custody finalized_utc: 2026-08-30T22:37:41Z
  custody lease_id: b6700119e3bdb144606273f2e7ae5144
  custody owner: rank4_cycle1_function_pair
  custody source_bytes/source_sha256: 21468 / ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d
  schema: jc2.artifact-finalize/v1

block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
  seal body bytes: 8930
  recomputed body bytes: 8930
  seal body sha256: 69e0e3808e562ac8c6b561d9b778b1f50b60d696c0c0dc2d5df88d8f6dbe6bf7
  recomputed body sha256: 69e0e3808e562ac8c6b561d9b778b1f50b60d696c0c0dc2d5df88d8f6dbe6bf7
  frozen basis: 65d42c3468f115359ada65ce84ad2196c7630939
  artifact file_bytes: 9262
  artifact full_sha256: 2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190
  artifact published_mode: 0444
  custody opened_utc: 2026-08-30T22:54:56Z
  custody closed_utc: 2026-08-30T22:56:02Z
  custody finalized_utc: 2026-08-30T22:56:13Z
  custody lease_id: 9deae81757834e1d9ad0b71dbee464ce
  custody owner: coordinator
  custody source_bytes/source_sha256: 8930 / 69e0e3808e562ac8c6b561d9b778b1f50b60d696c0c0dc2d5df88d8f6dbe6bf7
  schema: jc2.artifact-finalize/v1
```

The coordinator file also reproduces, inside its charged body, prior review/log hashes for a different function-pair review and an Opus pseudo-plane review. Those sibling files were not opened.

## 1. Executive verdict

The inverse-Kummer collision-control report is mathematically sound as a countercontrol, subject to the provisional status of the preceding function-pair theorem. Its central correction is correct: the residual divisor in

```text
div_U(c0 o pi)=Phi+E
```

gives the inverse of the original Kummer class, not a second independent class. Consequently no `mu^2` divisibility, second bad ruling fibre, global cover, counterexample, or JC2 conclusion follows.

The quartic primitive-element and monogenic-index analysis is also internally correct once Formanek's field-generation theorem is accepted in the standard form used in the charged file. I could locate the official Houston Journal archive entry for Formanek, *Observations About the Jacobian Conjecture*, Houston J. Math. 20 (1994), pp. 369-380, at `https://www.math.uh.edu/~hjm/vol20-3.html`; its linked PDF `restricted/archive/v020n3/0369FORMANEK.pdf` returned HTTP 403 in this environment, so direct primary-text verification of Theorem 2 is a source-access GAP in this review. The algebraic use of the theorem is checked below conditionally on the standard statement `C(H_1,H_2,x)=C(x,y)` for a two-variable Keller pair and a source coordinate.

No decisive successor is forced. The one-cusp horn remains OPEN.

## 2. Charged dependencies

The inverse-Kummer report explicitly takes the function-pair theorem as provisional input: see its lines 10-14 and 107-111. This review therefore separates:

```text
CONFIRMED: follows from the charged hypotheses and standard algebraic geometry;
GAP: requires an unverified external theorem, inaccessible primary text, or a global statement not present in the charged files;
REFUTED: does not follow or is false under the charged controls.
```

I do not revalidate the external Orevkov-Chau, Chau, or Miyanishi sources beyond the charged files because the assignment allowed only a narrow Formanek check.

## 3. Inverse Kummer divisor and class

### 3.1 Pullback divisor and residual divisor

Charged claim: with `c0=0` a reduced equation of `C0=pi(Phi)`,

```text
div_U(c0 o pi)=Phi+E
```

with `E` reduced effective, no component `Phi`.

Status: CONFIRMED, conditional on the function-pair input that `Phi -> C0` is the immersive normalization and generically degree one.

Reason: `pi|U` is etale along the relevant open, so the pullback of the reduced Cartier divisor `C0` is reduced at all points of `U` lying over it. The component `Phi` appears with multiplicity one because the normalization map `Phi -> C0` has generic degree one. The remaining components form a reduced residual effective divisor `E`. This confirms lines 154-162 of the inverse report.

The result does not imply that `E` is irreducible. It also does not identify the orders of the individual component classes of `E`.

### 3.2 Class calculation

From principality,

```text
0=[div(c0 o pi)]=[Phi]+[E],
```

hence

```text
[E]=-[Phi] in Pic(U).
```

Status: CONFIRMED.

Because the charged hypotheses give `Pic(U)=Z/mu<[Phi]>`, the total class `[E]` has exact order `mu`. This is a statement about the total divisor class. It is not a componentwise statement.

### 3.3 Regularity of `r`

Define

```text
r=(c0 o pi)^mu/(t-a).
```

Using

```text
div_U(c0 o pi)=Phi+E,
div_U(t-a)=mu*Phi,
```

one gets

```text
div_U(r)=mu(Phi+E)-mu Phi=mu E >= 0.
```

Status: CONFIRMED.

Since `U` is smooth, hence normal, a rational function with nonnegative valuation at every height-one prime is regular. This confirms the regularity assertion and the identity

```text
(t-a)r=(c0 o pi)^mu.
```

No hidden unit has been lost: a nonzero scalar in `c0` merely rescales `r` by a `mu`-th power of a scalar.

### 3.4 Kummer extension equality

Let

```text
alpha^mu=t-a.
beta=(c0 o pi)/alpha.
```

Then

```text
beta^mu=r,
alpha=(c0 o pi)/beta.
```

Therefore

```text
C(U)(alpha)=C(U)(beta).
```

Status: CONFIRMED.

This is field equality, not just an isomorphism of abstract cyclic extensions. Since `[Phi]` has exact order `mu`, `t-a` cannot be a proper `d`-th power in `C(U)` for `d>1` dividing `mu`; otherwise `(mu/d)Phi` would be principal, contradicting exact order. The same argument applies to `[E]`. Thus the Kummer field is genuinely degree `mu`, but the residual Kummer class is the inverse class, not an independent class.

Blast radius: any successor claiming independent `mu^2` divisibility from `Phi` and `E` is REFUTED.

## 4. Source factorizations and roots on `x=0`

### 4.1 Original source `F`

Charged formulas:

```text
t o g1-a=cP^mu,
c0 o F=P*S_F,
r o g1=c^(-1)S_F^mu.
```

Status: CONFIRMED.

The divisor of `P` is `g1^*Phi`, so `P` is squarefree because `g1` is etale over `Phi`. The polynomial `c0 o F` is squarefree because `F` is Keller and the pullback of a reduced divisor by an etale morphism is reduced. Since the `Phi` component has been accounted for once, the remaining factor is coprime to `P`. Substitution in `(t-a)r=(c0 o pi)^mu` gives the displayed formula for `r o g1`.

The statement does not show that `S_F` is irreducible. It only shows reducedness and `gcd(P,S_F)=1`.

### 4.2 Canonical cyclic source `H`

Charged formulas:

```text
t o f_mu=a+c x^mu,
c0(H)=x*S(x,y),
r o f_mu=c^(-1)S(x,y)^mu.
```

Status: CONFIRMED.

The line `x=0` is the retained copy of `Phi`. The same etale pullback argument makes `c0(H)` reduced, so both factors `x` and `S` occur with multiplicity one in `C[x,y]` and `gcd(x,S)=1`.

Important specialization warning: `S` squarefree in `C[x,y]` does not imply `S(0,y)` is squarefree in `C[y]`.

### 4.3 Two distinct roots, not simple roots

The function-pair theorem gives distinct `p,p' in Phi` with `pi(p)=pi(p')`. In the canonical source, these are distinct points `(0,y_p)` and `(0,y_p')`. At each preimage point, all other local branches of `C0` pull back into the residual divisor after the `x` factor is removed. Therefore

```text
S(0,y_p)=S(0,y_p')=0,
y_p != y_p'.
```

Status: CONFIRMED.

The multiplicity of a root of `S(0,y)` is the local intersection multiplicity of the retained branch with the residual branch or branches. The charged inputs give immersion of the normalization, not transversality of distinct branches. Therefore the stronger statement "the two roots are simple" is REFUTED.

## 5. Euler ledger for `D0=Supp(Phi+E)`

Let

```text
D0=pi^{-1}(C0) cap U=Supp(Phi+E).
```

Let `o` be the number of ordinary points of `C0 cap B`, and let `epsilon_c` be `1` if the charged cusp `c` lies on `C0`, else `0`. The omitted node `n` does not lie on `C0` by the charged function-pair result.

### 5.1 Constructible fibre count

Over `C0-B`, the finite etale quartic cover has four points. Over an ordinary point of `B`, the charged companion fibre cardinality is two. At the cusp `c`, it is one. The omitted node contributes nothing because `n notin C0`.

Thus

```text
e(D0)=4e(C0)-2o-3epsilon_c.
```

Status: CONFIRMED.

This is a set-theoretic Euler count. It uses cardinalities of constructible fibres, not intersection multiplicities.

### 5.2 Euler characteristic of `C0`

The normalization of `C0` is `A1`. If a singular point `z` has `r_z` normalization preimages and

```text
delta_top=sum_z(r_z-1),
s=#Sing(C0),
```

then

```text
e(C0)=1-delta_top.
```

Status: CONFIRMED.

This `delta_top` is topological branch-loss, not algebraic delta. Tangential intersections and higher contact do not change this Euler formula unless they change the number of branches/preimages.

### 5.3 Intersection of `Phi` and `E`

At a singular point `z` of `C0`, each of the `r_z` retained branch preimages on `Phi` meets the residual pullback of the other branch or branches. At smooth points of `C0`, no residual branch meets `Phi`. Therefore

```text
#(Phi cap E)=sum_z r_z=delta_top+s.
```

Status: CONFIRMED, as a cardinality statement.

It is not an intersection-number statement. In tangential or multibranch cases, the scheme-theoretic intersection multiplicity can be larger.

### 5.4 Residual Euler characteristic

Using

```text
e(D0)=e(Phi)+e(E)-#(Phi cap E),
e(Phi)=1,
```

one obtains

```text
e(E)=e(D0)-1+delta_top+s
    =4(1-delta_top)-2o-3epsilon_c-1+delta_top+s
    =3-3delta_top+s-2o-3epsilon_c.
```

Status: CONFIRMED.

The examples in the inverse report are also correct:

```text
one ordinary self-node away from B: delta_top=1, s=1, o=0, epsilon_c=0, so e(E)=1;
one ordinary self-node on ordinary B: delta_top=1, s=1, o=1, epsilon_c=0, so e(E)=-1.
```

No contradiction follows from either value.

## 6. Formanek theorem, tower arithmetic, and irreducibility

### 6.1 Primary-source access

Official HJM archive location:

```text
https://www.math.uh.edu/~hjm/vol20-3.html
```

The page lists:

```text
Edward Formanek, Observations About the Jacobian Conjecture, pp. 369-380.
```

The linked official PDF path is:

```text
https://www.math.uh.edu/~hjm/restricted/archive/v020n3/0369FORMANEK.pdf
```

That PDF returned HTTP 403 in this environment. Therefore:

```text
Direct primary-text verification of Theorem 2: GAP.
Official bibliographic location of the paper: CONFIRMED.
```

I do not promote "primary theorem text was read" in this report.

### 6.2 Applicability if the standard Formanek statement is accepted

The charged inverse report states the needed dimension-two theorem as:

```text
for a Keller pair (H1,H2), the field C(H1,H2) together with either source coordinate generates C(x,y).
```

Applied to the charged Keller pair `H=(H1,H2)` and the source coordinate `x`, this says

```text
L=C(x,y)=K(x),     K=C(H1,H2).
```

Status: CONFIRMED, conditional on the theorem statement.

There is no mismatch in the chosen coordinate: `x` is a polynomial source coordinate by the cyclic normalization theorem.

### 6.3 Tower arithmetic

Set

```text
K=C(H1,H2),
M=C(U),
L=C(x,y).
```

The charged tower gives

```text
[M:K]=4,
[L:M]=mu,
[L:K]=4mu.
```

Also

```text
t-a=cx^mu,
K(t) subset M subset L.
```

Since `L=K(x)` and `x` satisfies `X^mu-(t-a)/c` over `K(t)`,

```text
[L:K(t)] <= mu.
```

But

```text
[L:K(t)]=[L:M][M:K(t)]=mu*[M:K(t)].
```

Therefore `[M:K(t)]=1` and

```text
M=K(t).
```

Status: CONFIRMED, conditional on Formanek.

Hidden separability issue: none in characteristic zero. Field-versus-product issue: none at this level because `A2`, `U`, and the retained cyclic source are irreducible, so the function rings involved have fields of fractions.

### 6.4 Irreducibility of `c^{-4}P_t(a+cX^mu)`

Let `P_t(Z)` be the monic minimal polynomial of `t` over `K`. Since `M=K(t)` and `[M:K]=4`, `deg P_t=4`. Substitution gives a monic degree `4mu` polynomial

```text
m_x(X)=c^(-4)P_t(a+cX^mu)
```

annihilating `x`. Since Formanek gives `L=K(x)` and `[L:K]=4mu`, the minimal polynomial of `x` over `K` has degree `4mu`. Hence `m_x` is irreducible.

Status: CONFIRMED, conditional on Formanek.

No independent Kummer factorization follows from the norm computations; irreducibility is compatible with the inverse-Kummer divisor relation.

## 7. Regularity of `t` on `V` and the quartic order

Let

```text
V=A2-B.
```

The inverse report uses the charged assertion that

```text
pi^{-1}(V)->V
```

is finite etale and contained in `U`.

Status: CONFIRMED as a charged input; not independently re-sourced here.

Since `t` is regular on `U`, it is regular on `pi^{-1}(V)`. Because `pi^{-1}(V)->V` is finite, `t` is integral over `O(V)`. Let `A=O(V)`. The ring `A` is normal. Therefore the coefficients of the minimal polynomial `P_t` over `Frac(A)=K` lie in `A`.

Status: CONFIRMED.

Then

```text
A[t] ~= A[Z]/(P_t)
```

is a free rank-four `A`-module with basis `1,t,t^2,t^3`. Its fraction field is `M`, and its normalization in `M` is

```text
O(pi^{-1}(V)).
```

Status: CONFIRMED.

Connectedness/product issue: `pi^{-1}(V)` is a nonempty open of irreducible `U`; it is irreducible. The finite etale algebra is therefore a domain here, not a product of disconnected global components. After strict henselization or completion it can split as a product, but that is a local splitting used later and does not alter the global field argument.

## 8. Norm identity at `t=a`

The inverse report claims, in `O(V)=C[u,v,b^{-1}]`,

```text
P_t(a)=lambda*b^k*c0^mu,
lambda in C*, k in Z.
```

Status: CONFIRMED.

At the generic point of `C0 cap V`, the divisor `D0=pi^{-1}(C0) cap U` has one sheet equal to `Phi` and the other sheets residual. Along `Phi`,

```text
ord(t-a)=mu.
```

Along the residual sheets, `ord(t-a)=0`. Since the cover over `V` is etale, the residue degree at the generic `Phi` sheet is one. Thus

```text
div_V(P_t(a))=mu*(C0 cap V).
```

Since `B` is irreducible in the charged function-pair theorem and `C0 != B`, the quotient `P_t(a)/c0^mu` is a unit of `O(V)`. The unit group of `C[u,v,b^{-1}]` is `C* b^Z`. This gives the displayed identity.

The exponent `k` is not a nonnegative polynomial multiplicity unless one has separately cleared denominators along `B`. In `O(V)`, `b` is inverted, so `k` may be negative. The sign convention in the inverse report is consistent: `P_t(a)=Norm(a-t)`, and because the degree is four, this is also `Norm(t-a)`.

At the generic point of `B`, the two companion sheets in `U` have valuation zero for `t-a` because `C0 != B` and `div_U(t-a)=mu Phi`. The remaining contribution to `k` is the valuation at the ramification-boundary prime. The generic partition `(2,1,1)` fixes ramification index two but does not determine that valuation.

Status of any stronger use:

```text
k>=0: GAP unless denominators are separately controlled.
k fixed by (2,1,1), cusp, or node packet: REFUTED.
degree contradiction from exponent mu: REFUTED.
```

## 9. Discriminant, index, and self-collision

### 9.1 Index-discriminant identity

For the order

```text
A[t] subset A'=O(pi^{-1}(V)),
A=O(V),
```

the normalized algebra `A'` is finite etale over `A`, so its discriminant is a unit. At every height-one prime of `A`, the usual order discriminant formula gives

```text
div_V(Disc(P_t))=2*I_t
```

for the effective local index divisor measuring `A'/A[t]`.

Status: CONFIRMED.

This is a codimension-one divisor statement. It does not assert that every conductor/index phenomenon is visible by a single global equation on a compactification.

### 9.2 Off-`B` self-collision

At a self-identification point of `C0` outside `B`, the finite etale quartic algebra becomes split after completed strict henselization. On the two selected sheets corresponding to the two branches of `C0`, choose local reduced branch equations `u=0` and `v=0`. The divisor condition gives, after absorbing units by completed-local `mu`-th roots,

```text
t1-a=u^mu,
t2-a=v^mu.
```

Then

```text
t1-t2=u^mu-v^mu.
```

Status: CONFIRMED.

The equality of the two `t` values on the asserted sheets is not merely pointwise at the collision: it follows from the displayed completed-local functions and cuts out a divisor by `u^mu-v^mu`.

The normalized cover remains etale over `V`. The vanishing of `t1-t2` is therefore nonnormality of the monogenic order `A[t]`, not ramification of `A'`.

### 9.3 Transverse versus tangent branches

If `u` and `v` form transverse parameters, then

```text
u^mu-v^mu=product_(zeta^mu=1)(u-zeta v)
```

gives `mu` distinct reduced coincidence branches.

If the two branches of `C0` are tangent, `u` and `v` are branch equations in the same regular completed local ring but need not be a regular parameter pair. The factorization remains algebraically true, but the factors need not cut distinct reduced curves. For example, a difference of tangent branch equations can acquire higher order.

Status:

```text
coincidence divisor exists: CONFIRMED.
mu distinct reduced local branches without transversality: REFUTED.
use of intersection multiplicity as cardinality: REFUTED.
```

The inverse report correctly avoids claiming transversality.

### 9.4 Collision on ordinary `B`

If the self-collision lies at an ordinary `(2,1,1)` point of `B`, the two unramified companion sheets in `U` still support local functions with

```text
t1-a=u^mu,
t2-a=v^mu,
t1-t2=u^mu-v^mu.
```

Status: CONFIRMED as a completed-local companion-sheet statement.

But this is not a global index divisor on `V`, because `B` has been removed from `V`. The inverse report correctly warns that the rank-two ramified boundary factor may carry a pole of `t` and that the quartic order over `V` need not extend across `B`.

Any successor that treats this boundary collision as an interior discriminant divisor without proving extension across `B` is REFUTED.

## 10. Completed-local rank-four controls

### 10.1 Off-`B` collision model

Model:

```text
R=C[[u,v]],
S=R^4,
tau=(u^mu,v^mu,1,2),
P(Z)=(Z-u^mu)(Z-v^mu)(Z-1)(Z-2).
```

Status: CONFIRMED.

`S` is finite etale of rank four. The order `R[tau]` is generically monogenic and has normalization `S`. Near the origin, all discriminant factors except `u^mu-v^mu` are units, so

```text
Disc(P)=unit*(u^mu-v^mu)^2.
```

With local `C0` equation `uv=0`, the inverse-Kummer identities on the two selected sheets are

```text
(uv)^mu/u^mu=v^mu,
(uv)^mu/v^mu=u^mu.
```

This proves formal local compatibility of a same-fibre self-node, inverse Kummer, etale normalization, and nonnormal monogenic order.

The illustrative polynomial parametrization

```text
s |-> (s^2, s(s^2-1))
```

has image

```text
Y^2=X(X-1)^2,
```

is immersive, and identifies `s=1` and `s=-1` in an ordinary node. Status: CONFIRMED as an illustrative plane-curve control, not as a Keller construction.

### 10.2 Ordinary `(2,1,1)` boundary model

Model:

```text
R=C[[u,v]],
w=u+v,
S=R[z]/(z^2-w) times R times R.
```

Status: CONFIRMED.

The first factor is finite flat of rank two and regular; the whole algebra has rank four. At `w=0` over the closed point the geometric fibre lengths are `(2,1,1)`. The two `R` factors are unramified companions, and assigning

```text
t1-a=u^mu,
t2-a=v^mu
```

gives the same companion equality locus `u^mu-v^mu=0`.

The phrase `t-a=z^(-1)` on the ramified factor is valid only after deleting `z=0`. It is not an integral element of the finite flat algebra across the ramification boundary. The inverse report uses it only to demonstrate non-extension of `t`; that use is CONFIRMED. Any use as an integral quartic order model over all of `R` would be REFUTED.

### 10.3 Cusp packet `(3,1)`

Model:

```text
R=C[[s,w]],
S_c=R[z]/(z^3-3s*z-2w) times R.
```

Status: CONFIRMED.

The cubic discriminant is a nonzero scalar multiple of

```text
s^3-w^2.
```

At the origin the fibre lengths are `(3,1)`. At a generic smooth point of the discriminant, the fibre type is `(2,1,1)`. The hypersurface is regular because the defining equation has derivative `-2` with respect to `w`.

### 10.4 Node packet `(2,2)`

Model:

```text
R=C[[u,v]],
S_n=R[z]/(z^2-u) times R[w]/(w^2-v).
```

Status: CONFIRMED.

The discriminant support is `uv=0`. The origin has geometric fibre lengths `(2,2)`. A generic point of either discriminant branch gives one double point and two simple points after geometric splitting, i.e. `(2,1,1)`. Both factors are regular.

### 10.5 What the local controls fail to globalize

Status: CONFIRMED.

These models do not glue to the charged global `S4` cover, do not produce a global Keller map, do not realize the pseudo-plane Picard and canonical package, and do not control the boundary at infinity. Their correct role is negative: they refute purely completed-local exclusions.

## 11. `K_U~0`, adjunction, normal bundle, duality, and conductor firewalls

### 11.1 Restriction to `Phi`

Since `Phi ~= A1`,

```text
Pic(Phi)=0.
```

The class relation `[E]=-[Phi]` therefore restricts trivially to `Phi`, and adjunction gives

```text
omega_Phi ~= (omega_U tensor O_U(Phi))|Phi ~= O_Phi.
```

Status: CONFIRMED.

The normal bundle `O_U(Phi)|Phi` is trivial. The section cutting out `E cap Phi` is a regular section of a trivial line bundle on `A1`; it may have a finite zero divisor, with the balancing pole at the missing point of a completion. Hence no affine adjunction contradiction arises from two or more collision points.

Any argument importing a projective intersection degree without the boundary terms of a chosen completion is REFUTED.

### 11.2 Duality and conductor for the quartic order

The scheme

```text
X=Spec(O(V)[Z]/(P_t))
```

is a hypersurface over the regular surface `V`, hence Gorenstein. Its normalization is finite etale over `V`, so the normalized algebra has trivial relative dualizing module. Finite duality identifies the order dual with a principal fractional ideal after trivialization.

Status: CONFIRMED.

This does not force the conductor to be the unit ideal and does not force the monogenic order to be normal. The split local model explicitly has trivial normalized canonical module and a nonempty square index divisor.

### 11.3 Divisor `T=div_U(b o pi)`

The producer's `T` is principal, and adjunction gives trivial dualizing sheaf on `T` in the sense used by the charged file. The inverse-Kummer identity for `c0` introduces no new `b`-valuation term. Therefore `K_U~0` gives no new congruence for

```text
N=#(T cap Phi).
```

Status: CONFIRMED.

## 12. Successor gates

### 12.1 Index-at-infinity gate

Desired theorem:

```text
the forced monogenic coincidence/index divisor u^mu-v^mu=0 contributes a positive Orevkov-Chau boundary correction.
```

Status: GAP.

The current files prove an index divisor for the monogenic order over `V` at off-`B` collisions. They do not identify a corresponding positive infinity-budget event. The normalized cover is etale over `V`, and the charged budget is saturated. A valid lemma must distinguish monogenic-order nonnormality from ramification of the normalized cover and must show that this index cannot be absorbed without boundary cost.

Smallest missing lemma: a boundary-index theorem linking the codimension-one index divisor of `O(V)[t]` to a positive term in the regular-extension Orevkov-Chau formula for `H`, with hypotheses covering tangent self-collisions and excluding cancellation at infinity.

### 12.2 Second-fibration gate

Desired theorem:

```text
if div(r)=mu E and [E]=-[Phi], then r is an A1-fibration or is functionally tied to t.
```

Status: GAP.

The current files prove that `r` is regular with a multiple zero divisor. They do not prove that the general fibre of `r` is `A1`, that `E` is a fibre of a ruling, or that `r` is a function of `t`. Local controls show that the inverse-Kummer identity is compatible with ordinary local geometry and does not itself create a second bad ruling fibre.

Smallest missing lemma: a global pseudo-plane theorem converting this particular torsion multiple divisor `mu E`, with `E cap Phi` containing the collision set, into an `A1`-ruling. Without that theorem, uniqueness of the `A1`-ruling cannot be invoked.

### 12.3 Companion-resultant gate

Desired theorem:

```text
the norm identity P_t(a)=lambda b^k c0^mu, combined with q_H=b o H, forces the index/coincidence divisor to meet B at the cusp or node, or otherwise violates the Euler/orbit ledger.
```

Status: GAP.

The current Euler identity allows ordinary intersections and allows the self-collision to be off `B` or at an ordinary `(2,1,1)` value. The integer `k` in the norm identity is uncontrolled and may be negative in `O(V)`. No resultant computation in the charged files fixes `N`, the cusp alternative, or the location of the collision.

Smallest missing lemma: a concrete resultant/intersection theorem for `c0(H)=xS` and `q_H=b(H)` that computes the relevant support and multiplicities rather than just their Euler defect.

## 13. Corrections and blast radius

The following are safe corrections to carry forward:

```text
[E]=-[Phi], not independent of [Phi]: CONFIRMED.
Kummer extensions from t-a and r are identical fields: CONFIRMED.
mu^2 | d1 from the two divisors: REFUTED.
E irreducible: GAP.
r is an A1-ruling: GAP.
E is another fibre of rho: REFUTED unless a new fibration theorem is proved.
S(0,y) has two distinct roots: CONFIRMED.
those roots are simple: REFUTED.
Euler ledger e(E)=3-3delta_top+s-2o-3epsilon_c: CONFIRMED.
delta_top may be replaced by algebraic delta in tangent cases: REFUTED.
Formanek official bibliographic location: CONFIRMED.
direct primary-text verification of Formanek Theorem 2 here: GAP.
M=K(t), degree arithmetic, and irreducibility of c^(-4)P_t(a+cX^mu): CONFIRMED conditional on Formanek.
t regular and integral over V, and O(V)[t] free rank four: CONFIRMED.
t regular across the ramification boundary B: REFUTED.
P_t(a)=lambda b^k c0^mu in O(V): CONFIRMED.
k nonnegative or fixed by fibre partition: GAP/REFUTED depending on use.
self-collision gives monogenic-order nonnormality off B: CONFIRMED.
self-collision gives ramification of the normalized etale cover: REFUTED.
transverse mu-branch coincidence without transversality: REFUTED.
completed-local controls exclude the horn: REFUTED.
completed-local controls block local-only contradictions: CONFIRMED.
K_U~0 or adjunction forbids finite E cap Phi: REFUTED.
```

The blast radius is narrow but important. It kills the tempting divisibility and ruling shortcuts, and it prevents promoting local index/coincidence data to an infinity contradiction without a new theorem. It does not damage the function-pair theorem's conditional maximum-safe conclusion, except that this review cannot certify the primary text of Formanek Theorem 2 from the blocked official PDF.

## 14. Maximum-safe theorem

Conditional on the charged function-pair theorem and on the standard Formanek field-generation theorem, the maximum-safe statement is:

```text
For the charged rank-four one-cusp pseudo-plane row, the residual divisor
in div_U(c0 o pi)=Phi+E satisfies [E]=-[Phi] and gives a regular function
r=(c0 o pi)^mu/(t-a) with div(r)=mu E. The Kummer extension defined by r
is the same cyclic field as the one defined by t-a. On the original and
canonical sources this is exactly c0(F)=P*S_F and c0(H)=x*S, with
r pulling back to c^(-1)S_F^mu and c^(-1)S^mu respectively. The collision
on C0 gives two distinct roots of S(0,y), not necessarily simple roots.

The quartic field is generated by t over K=C(H1,H2): M=K(t). Therefore
the monogenic order O(V)[t] is rank four and has finite-etale normalization
O(pi^{-1}(V)). An off-B same-fibre collision forces a local index divisor
with equation u^mu-v^mu=0 for the monogenic order, while the normalized
cover remains etale. The same equations have completed-local controls in
the off-B, ordinary (2,1,1), cusp (3,1), and node (2,2) packets. These
controls do not globalize to a Keller map or close the horn.

The residual Euler ledger is
e(E)=3-3delta_top+s-2o-3epsilon_c.
No canonical, adjunction, conductor, or local discriminant argument in the
charged files gives a contradiction.
```

The one-cusp horn remains OPEN. The exact missing ingredient is a global theorem forcing either a positive boundary cost from the monogenic index divisor, a second `A1`-fibration from `r`, or a companion-resultant contradiction locating the collision or computing `N` incompatibly with the charged Euler ledger.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31486`.
- Body SHA-256:
  `5447df56aef937da71623b0a8508844bfed9e5ac58fcd5f10f6c29c4f2d19efd`.
- Frozen basis: `684350d99a7386a208a14eebf461d399dcd95713`.
