# TRIPLE-COVER lane: resolvent cubic analysis of the `(6,4)` row

## 0. Scope, frozen-input receipts, and conventions

The three frozen copies were listed before use and hashed with `shasum -a 256`.
All three receipts match the charge exactly:

```text
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  pi1s4-64-fixed-tuple-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

No charged or canonical file was edited, and `jc2-lean` was not inspected.  The
row data used below are the charged, provisional data

```text
deg D=6,  Q=[1:0:0],  (v,u)=(Y/X,Z/X),
Delta=(6,4,3),  (mult_Q,I_Q(D,L_infty))=(2,6),
beta_1=15,  delta_infty=7,  delta_aff=3,
```

so the required infinity germ has one branch
`v=s^2`, `u=c_6s^6+(even powers through s^14)+c_15s^15+...`, with
`c_6c_15 != 0`.  The affine curve is irreducible and has exactly three
ordinary nodes and no other affine singularity.

There are two logically different assertions in the charged successor.  The
existence, flatness and reduced discriminant of the resolvent triple cover are
proved below.  Its asserted presentation by one global generator, and the
asserted degree bounds on that generator's cubic, are audited separately and
are not assumed silently.  All conclusions using those extra assertions are
labelled **conditional**.

## 1. From the `S_4` quotient to a connected simply branched triple cover

Let
`V={1,(12)(34),(13)(24),(14)(23)}`.  Conjugation on the three nonidentity
elements of `V` gives the quotient `q:S_4 -> S_3`, with kernel `V`.  A
transposition is sent to a transposition.  If `tau,sigma` are disjoint
transpositions, then `tau sigma` is a nonidentity element of `V`, and hence

```text
q(tau)=q(sigma).                                      (1.1)
```

Thus `psi=q o phi` is onto `S_3`; in its natural action on three letters it
defines a connected degree-three etale cover of `U=A^2-D`.  Surjectivity, not
just transitivity, says that the generic cubic extension has `S_3` Galois
closure.

By algebraic Riemann existence and normalization, this cover extends uniquely
to a finite normal map `pi:X -> A^2`.  The local models also prove flatness.
At a smooth point of `D`, with local equation `u=0`, the completed algebra is

```text
C[[u,v]]  direct-sum  C[[u,v]][t]/(t^2-u),             (1.2)
```

up to multiplying `u` by a unit.  At a node, choose `D:{uv=0}`.  Its two
meridians both act by the same transposition by (1.1), while the third sheet is
fixed, so the completed algebra is

```text
C[[u,v]]  direct-sum  C[[u,v]][t]/(t^2-uv).            (1.3)
```

The second factor in (1.3) is the normal `A_1` surface.  Both displayed
algebras are free of rank three over the completed base.  Off `D` the map is
etale; hence completion and faithful flat descent show that `pi` is finite
flat everywhere.  Notice that `X` is allowed to be singular over a node.

The algebra discriminants of (1.2) and (1.3) are respectively a unit times
`u` and a unit times `uv`.  Therefore the divisorial discriminant has no
component away from `D`, and every smooth branch of `D`, including both
branches at each node, occurs with multiplicity exactly one.  If `f` is the
reduced irreducible sextic defining `D`, factoriality of `C[x,y]` gives

```text
disc(pi_*O_X/C[x,y]) = kappa f,       kappa in C^*.     (1.4)
```

This establishes the connected, simply-branched resolvent cover and the exact
reduced branch divisor.  It does not yet choose a global algebra generator.

## 2. Global cubic form and the exact discriminant divisor

Put `R=C[x,y]` and `B=pi_*O_X`.  Division by three splits the trace:
`B=R direct-sum E`, where `E=ker(Tr)` is projective of rank two.  Quillen--
Suslin makes `E` free.  This is the point at which the charged reduction
overreaches: a free cubic algebra need not have a power basis.

The general structure theorem for a flat triple cover is Miranda's.  After a
basis of `E`, it has four polynomial coefficients `A_0,B_0,C_0,D_0`, or
equivalently a binary cubic index form

```text
I(S,T)=B_0 S^3-3A_0 S^2T+3D_0 ST^2-C_0 T^3.           (2.1)
```

Its branch polynomial (up to a nonzero numerical factor) is

```text
B_0^2 C_0^2-3A_0^2 D_0^2+4A_0^3 C_0+4B_0 D_0^3
 -6A_0B_0C_0D_0.                                      (2.2)
```

Formula (1.4) says that (2.2), for the resolvent cover, is `kappa f`.
It does **not** reduce (2.2) to `4a^3+27b^2`.

Indeed, for `theta=s z+t w` in the trace-zero module,
`det(1,theta,theta^2)=I(s,t)`.  Thus a global power basis exists exactly when
there are `s,t in R` for which `I(s,t)` is a unit.  Freeness of `E` supplies
the variables in this equation, not a solution.  As a concrete negative
control, the free rank-three domain

```text
B=R direct-sum Rz direct-sum Rw,
z^2=xw,   zw=x(1-xy),   w^2=(1-xy)z
```

embeds in `C(x,y)[t]/(t^3-x^2(1-xy))` by `z=t`, `w=t^2/x`; the valuation at
`x=0` proves irreducibility.  Its index form is
`I=xS^3+(xy-1)T^3`.  The two coefficients generate the unit ideal, so this
algebra is Zariski-locally monogenic.  Were `I(s,t)=c in C^*` globally,
reduction modulo `xy-1` would give `x s^3=c` in `C[x,x^(-1)]`, impossible by
the `x`-valuation modulo three.  This example is not claimed to have the row's
reduced branch; it disproves “free and locally monogenic, therefore one
global cubic” and isolates the missing strengthened lemma.

If such a unit-representing element were proved to exist, translating it by
one third of its trace would give

```text
B = R[z]/(z^3+a z+b),
-(4a^3+27b^2)=kappa f.                                 (2.3)
```

The multiplicity-one assertion in (2.3) is valid by §1.  The further bounds
`deg a<=2`, `deg b<=3` are a second missing step.  They follow immediately
only when the top terms of `4a^3` and `27b^2` do not cancel.  Shioda's exact
order-five Davenport--Stothers example is

```text
P=x(x^9+12x^6+60x^3+96),
Q=x^15+18x^12+144x^9+576x^6+1080x^3+432,
P^3-Q^2=-1728(3x^6+28x^3+108).
```

Taking `a=-3P`, `b=2Q` gives `deg(a,b)=(10,15)` but
`4a^3+27b^2=186624(3x^6+28x^3+108)`.  The last polynomial is squarefree.
Moreover the cubic is irreducible: a rational root would be polynomial; the
resultant-square factor in its squarefree discriminant makes `3r^2+a`
constant, and substitution would make the discriminant have degree ten, not
six.  Its
generic Galois group is therefore `S_3`.  Its branch is nevertheless a union
of vertical lines, not the irreducible one-place row.  Thus excluding
high-degree cancellation needs a new argument using exactly those stronger
hypotheses.

Accordingly the unconditional route stops at the four-coefficient identity
(2.2).  The two precise missing statements are
`OPEN[PI1S4-(6,4)-TRIPLE-COVER-GLOBAL-MONOGENICITY]` and
`OPEN[PI1S4-(6,4)-TRIPLE-COVER-HIGH-DEGREE-CANCELLATION]`.  Sections 3--6 solve the charged
one-variable system **conditionally** on both statements.

## 3. Classification of the leading-form identity

Here the charged bounded-degree premise is assumed.  Let `A=a_2` and
`B=b_3` be homogeneous of degrees two and three, and let `L` be a nonzero
linear form:

```text
4A^3+27B^2=cL^6.                                       (3.1)
```

For the physical sextic `c!=0`.  Choose a linear form `M` independent of
`L`, put `t=M/L`, and set `alpha(t)=A/L^2`, `beta(t)=B/L^3`.  These are
polynomials of degrees at most two and three satisfying
`4alpha^3+27beta^2=c`.  They are coprime.  Differentiation gives

```text
2alpha^2 alpha' + 9beta beta' = 0.
```

Consequently `alpha^2 | beta'` and `beta | alpha'`.  If their positive
degrees are `m,n`, this would give `2m<=n-1` and `n<=m-1`, an impossibility.
If either is constant, (3.1) makes the other constant.  Thus all and only the
solutions for `c!=0` are

```text
A=alpha_0 L^2,   B=beta_0 L^3,
4alpha_0^3+27beta_0^2=c.                               (3.2)
```

This includes `A=0` or `B=0`; they cannot both vanish.  Equivalently,

```text
z^3+Az+B = product_i (z-r_i L),
sum_i r_i=0,
```

where the three constants `r_i` are distinct because the discriminant is
nonzero.  Hence the branch tangent cone is the nonreduced sixth power
`cL^6`, but the leading cubic itself is squarefree.  This distinction rules
out a “perfect-power therefore impossible” shortcut.

For completeness, if `c=0`, unique factorization gives
`3 ord_p(A)=2 ord_p(B)` for every irreducible `p`.  Degree then gives the
complete family

```text
A=-3Q^2,   B=2Q^3                                      (3.3)
```

with `Q` any homogeneous linear form, including zero.  Conversely (3.3)
satisfies (3.1), and its leading cubic is
`(z-Q)^2(z+2Q)`.  This singular family cannot occur for a genuine degree-six
`f_6=cL^6` with `c!=0`.

Thus the binary-form Diophantine problem is completely solved: it forces
common-`L` leading forms but is consistent.  Lower terms must be used.

## 4. Infinity analysis and comparison with the required row data

Continue conditionally and take `L=Y`.  At `Q=[1:0:0]` use
`u=Z/X`, `v=Y/X`.  Homogenizing `a,b` to degrees two and three gives

```text
AA=alpha_0 v^2+u(lambda_0+lambda_1 v)+lambda_2 u^2,
BB=beta_0 v^3+u(q_0+q_1v+q_2v^2)
   +u^2(r_0+r_1v)+r_2u^3,                              (4.1)
FF=4AA^3+27BB^2.
```

Here `FF=0` is the projective discriminant germ and (3.2) holds.  Its
quadratic jet is `27q_0^2u^2`.  The required multiplicity two therefore
forces `q_0!=0`; otherwise the multiplicity is at least three.  Hence
`(v,w)=(v,BB)` are analytic coordinates.  Put

```text
AA_0(v)=AA(u(v,w=0),v),   k=ord_v AA_0.                (4.2)
```

In these coordinates `FF=27w^2+4AA(v,w)^3`.  If `AA_0` has order `k`,
its Newton face is `27w^2+gamma v^(3k)`, `gamma!=0`; all terms of `AA^3`
containing `w` lie strictly above that face.

If `alpha_0!=0`, then `k=2`.  If `alpha_0=0`, (3.2) gives
`beta_0!=0`, and solving `BB=0` gives
`u=-(beta_0/q_0)v^3+O(v^4)`.  Since then
`AA=u(lambda_0+lambda_1v+lambda_2u)`, the exhaustive list is

| coefficient condition | `k` | germ | places at `Q` | `delta_Q` |
|---|---:|---|---:|---:|
| `alpha_0!=0` | 2 | `w^2+v^6` | two smooth, contact 3 | 3 |
| `alpha_0=0, lambda_0!=0` | 3 | cusp `(2,9)` | one | 4 |
| additionally `lambda_0=0, lambda_1!=0` | 4 | `w^2+v^12` | two smooth, contact 6 | 6 |
| additionally `lambda_1=0, lambda_2!=0` | 6 | `w^2+v^18` | two smooth, contact 9 | 9 |

If all three `lambda_i` vanish, `AA=0` and `FF=27BB^2` is nonreduced.
For odd `k`, the first nonanalytic term has exponent `v^(3k/2)`, so with
`v=s^2` its first odd `s`-exponent is `3k`.  For even `k` the two signs give
two distinct smooth branches.

The charged row requires one branch of type `(2,15)` and
`delta_infty=7`; equivalently this calculation requires `k=5`.  But (4.1)
allows only `k=2,3,4,6`.  Thus, **conditional on a bounded-degree global
cubic**, every leading-form solution is incompatible with
`Delta=(6,4,3)`, `beta_1=15`: the conditional system is killed at infinity.

## 5. Affine singularities of cubic discriminant curves

Still conditionally, write `F=4a^3+27b^2`.  Let `p` satisfy `F(p)=0` and
`(a(p),b(p))!=(0,0)`.  There is a unique `r!=0` with

```text
a(p)=-3r^2,   b(p)=2r^3.
```

Direct differentiation gives

```text
dF(p)=108r^3(db+r da).                                 (5.1)
```

Thus the discriminant is singular precisely when `db+r da=0`.  At such a
point its Hessian is

```text
Hess(F)=108r^3(r Hess(a)+Hess(b))-18r^2(da tensor da). (5.2)
```

It is an ordinary node exactly when the determinant of this binary quadratic
form is nonzero.  At the point the cubic is
`(z-r)^2(z+2r)`.  The simple root splits off analytically; after the Morse
lemma the other factor of the cover is `eta^2=uv`.  Hence the cover has an
`A_1` singularity, the two ramification arcs meet there, and both node
meridians exchange the **same** two sheets.  This is exactly the local
behavior predicted by (1.1), not an obstruction.  For example

```text
a=-3,   b=2+xy,   F=108xy+27x^2y^2
```

has an ordinary node at the origin.

In contrast, if `a(p)=b(p)=0`, then

```text
the quadratic jet of F is 27(db)^2,
```

of rank at most one.  Such a point is never an ordinary node.  If
`da wedge db!=0`, the map `(x,y)->(a,b)` is locally invertible and the germ is
the standard cusp `4a^3+27b^2=0`.  More generally, if `db!=0` and the finite
integer `m=ord(a restricted to {b=0})`, its Newton type is `b^2+u^(3m)`: odd `m`
gives one branch `(2,3m)`, while even `m` gives two smooth branches of contact
`3m/2`.  Infinite order makes `b` divide `a` and gives a nonreduced `b^2`
factor.  If `db=0`, the multiplicity is at least three.  None is a node.

Therefore a nodal cubic discriminant is special in a precise way: every node
must lie over a nonzero point of the coefficient cusp and satisfy the Morse
condition (5.1)--(5.2); a transverse common zero of `a,b` produces a cusp,
not a node.

## 6. Consequences for a sextic with exactly three nodes

The affine condition strengthens the conditional kill.  By §5, `a` and `b`
have no common affine zero, since every such zero would be a non-nodal
singularity of `F`.  Let `AA,BB` be their degree-two and degree-three
homogenizations from (4.1).  They have no common component: a common factor
would occur at least squared in `FF`, contrary to the reduced irreducible
sextic.  Bezout therefore gives total intersection number six.

Every common zero lies on `FF=0`.  There is no affine one, and the sextic has
only the point `Q` at infinity, so

```text
I_Q(AA,BB)=6.                                           (6.1)
```

But `q_0!=0` makes `BB=0` smooth at `Q`; hence (6.1) is precisely the integer
`k=ord_v AA_0` in (4.2).  The table in §4 shows that `k=6` forces

```text
alpha_0=lambda_0=lambda_1=0,   lambda_2!=0,
AA=lambda_2 u^2.
```

Thus the affine coefficient `a` is a nonzero constant.  Over `C`, choose
`rho!=0` with `rho^2=-4a^3/27`; then

```text
4a^3+27b^2=27(b-rho)(b+rho),                            (6.2)
```

contradicting irreducibility of `D`.  (Here `b` really has degree three,
because (3.2) gives `beta_0!=0`.)

Consequently the bounded-degree monogenic system has no solution in the
three-node row.  There are two independent conditional obstructions: §4
excludes the required one-place `(2,15)` infinity germ, while (6.1)--(6.2)
uses only one place at infinity, multiplicity two there, irreducibility, and
the requirement that every affine singularity be a node.

## 7. Verdict and quantified scope

**Verdict: OPEN at
`OPEN[PI1S4-(6,4)-TRIPLE-COVER-GLOBAL-MONOGENICITY]`; behind it lies
`OPEN[PI1S4-(6,4)-TRIPLE-COVER-HIGH-DEGREE-CANCELLATION]`.**

The resolvent quotient does prove, uniformly for every hypothetical `phi`, a
connected finite-flat `S_3` triple cover with reduced discriminant exactly
`D`.  It proves the four-coefficient identity (2.2), not a one-variable
cubic.  Projective-module freeness is insufficient for a global power basis,
as the locally monogenic counterexample in §2 shows.  Even after a power
basis is added, an irreducible one-place/nodal argument is still needed to
exclude Davenport--Stothers cancellation and obtain degrees `(2,3)`.

On the other hand, the work after those two gaps is complete: the leading
identity is fully classified, its infinity germs are exhausted, and both §4
and §6 prove that **no** bounded-degree depressed cubic can have the charged
row data.  Thus proving the two named lemmas would promote this route to a
uniform **KILLED** verdict.  Without them, calling the row killed would use an
unproved reduction; calling it `SURVIVES` would be equally wrong, because no
general Miranda triple-cover family with the required branch curve has been
exhibited.

The unconditional reduction and the conditional contradictions use only
`phi`, irreducibility/nodality, and the numerical infinity type.  They do not
use the fold witness or any particular placement of the three nodes.  Hence
the quantified scope is the whole `(6,4)` row carrying such an `S_4`
representation, exactly as requested.  No exit-price assertion is made.

## References and exact source receipts

**Frozen charged sources.**  The hashes are in §0.  In
`pi1s4-64-fixed-tuple-opus5-20260831.md`, lines 573--586 state the charged
triple-cover successor; lines 71--87 and 109--138 fix the infinity coordinates
and Puiseux convention.  In `row-sweep-sol56-20260831.md`, lines 112--166
give the `(6,4)` census, the three-node condition, and the attained infinity
type.  Integration lines 70--91 type that row as provisional.  These are
consumed as frozen inputs, not promoted beyond their stated scope.

**Rick Miranda**, “Triple Covers in Algebraic Geometry,” *American Journal of
Mathematics* **107** (1985), 1123--1158.  Theorem 3.6 gives general triple-cover
data; Lemma 4.5 and Proposition 4.7 give the branch polynomial/divisor.  The
author-hosted PDF was fetched as a byte stream (no file saved) on 2026-08-31:

```text
https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf
SHA-256  0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875
```

**Tetsuji Shioda**, “Elliptic Surfaces and Davenport-Stothers Triples,”
*Commentarii Mathematici Universitatis Sancti Pauli* **54** (2005), 49--68,
DOI `10.14992/00008689`.  Section 5 displays the order-five B/Birch identity;
Lemma 3.1 proves its residual has simple zeros.  The official repository PDF
was fetched as a byte stream on 2026-08-31:

```text
https://rikkyo.repo.nii.ac.jp/record/8708/files/AA00610867_54-01_04.pdf
SHA-256  467701925109586976ca8f89ec614ee95c5ad740084b969a93ba3795b0cdb740
```

Other classical inputs used directly are algebraic Riemann existence,
normalization of a finite cover, Quillen--Suslin, completed Kummer models,
Bezout, the formal implicit-function theorem, and Newton--Puiseux.  No CAS or
job of uncertain duration was run.

<!-- BODY-END -->
