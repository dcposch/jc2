# Different-model hostile review: unbalanced singular-F5 polar and q=8 global elimination

Date: 2026-08-30  
Reviewer: GPT-5.5, xhigh reasoning  
Requested frozen basis: `8538f9fbe0fe305b42371e43c3377d9c921530b5`  
Disposition: **CONFIRM_WITH_CORRECTIONS**

## 0. Custody, method, and verdict map

I independently reconstructed the analytic and lattice calculations. I did not
treat seals, earlier reviews, prose, or successful enumeration as proof. I did
not access `jc2-lean`, modify an input, or change Git state.

All ten supplied SHA-256 values reproduce exactly. The requested commit exists,
and `git diff 8538f9f... -- <the ten charged paths>` is empty. The checkout's
current `HEAD` is instead `4decd33d5caf8553bcbaa199b93a900ecabeee18`;
therefore this review is explicitly of the hash-pinned bytes, which are
unchanged from the requested basis, and not a claim that the checkout itself is
at that commit.

```text
6a7dc7bec108d867fe9215a85fdc09c2d2790db73d36c4123e96f7419f9511f3  xmodel/bd-a2-singular-f5-unbalanced-local-polar-sol56-20260830.md
39d7bd2320dea33af65babd9bb78641a4aacc13cfd4f7ac93b45d0bb0c67fb56  xmodel/bd-a2-singular-f5-unbalanced-local-polar-replay-corrigendum-sol56-20260830.md
ee488fbb19c243815f85254d8c2d3a06ba77991b1cf8e92d70e57b4b0317ac82  ops/f5_unbalanced_polar_replay.py
034414413db07d8a39c2b36b26eb3eb5ce0f0fe4e865cacf16d0671a0b13cfed  ops/f5_unbalanced_polar_replay_v2.py
5a31a2ab48746828f08cc0b7e2d349b2c2dc773a2faa59fa23a51cb667bbaecc  xmodel/bd-a2-q8-f5-global-lattice-elimination-b5-b6-u5-u6-sol56-20260830.md
ef689257528b850ea1c504f429eac78e2d5339f4f45ad783d6b85189fd9acd0c  ops/q8_f5_global_lattice_replay.py
fdf8f476acc86e2c07fbc472771ee49358d02c87d2667f15e6b762800eed7bc6  xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-coordinator-integration-sol56-20260830.md
a5bf78c8ab8704884e9bb3c084c88059e01ec7690c1d6f645a9e87a0aa70a884  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-coordinator-integration-sol56-20260830.md
f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md
```

The itemized dispositions are:

| item | verdict | result |
|---:|---|---|
| 1 | `CONFIRMED` | exact unbalanced cells; U3 is A3; two reduced degree-4 germs |
| 2 | `CONFIRMED` | exact square completion; `delta` separates D5 and D6; no D7 jump |
| 3 | `CONFIRM_WITH_CORRECTIONS` | partitions and reduced coefficient-one germs hold; generic D6 remainder is (O(z^{5/2})), not (O(z^3)) |
| 4 | `CONFIRMED` | minimal marked resolutions, valuations, and all three vectors/sites hold |
| 5 | `CONFIRMED` | corrigendum is accurate and v2 is optimization-safe |
| 6 | `CONFIRM_WITH_CORRECTIONS` | all total classes hold; the numerical root classification omitted (F-P_i-P_j), which is safely excluded by (S_0)-disjointness |
| 7 | `CONFIRM_WITH_CORRECTIONS` | Euler and forest gates hold; the balanced-fibre proof of horizontality contains a false sentence and needs the numerical repair below |
| 8 | `CONFIRMED` | identity, table, and B6 coefficient-two refinement hold |
| 9 | `CONFIRMED` | replay, AST, digest, and forged-survivor control hold in all modes |
| 10 | `CONFIRM_WITH_CORRECTIONS` | all four scoped conclusions survive the stated repairs |

No exit-price assertion is made in this review; absence of a receipt charge
marker is intentional.

## 1. Exact unbalanced cells and the U3 calculation — `CONFIRMED`

Expand

\[
h=(1+v)z^3-(2v+v^2)z^2+v^2z,
\qquad
f=h+u(a(z)u+b(z)v+c(z)).
\]

Put (a_0=a(0)), (b_0=b(0)), and (c_1=c'(0)). The unbalanced locus is
(b_0=0). There are then only two cases:

1. (c_1\ne0): (b=zB, c=zC, C(0)=c_1), the U3 cell;
2. (c_1=0): (b=zB, c=z^2C), the D cells.

In either case (a_0=0) would also give (a=zA), and every term of (f)
would be divisible by (z). For U3, for example,

\[
f=z\big((z-v)((1+v)z-v)+u(Au+Bv+C)\big).
\]

Both factors are nonunits. The hypersurface local ring is not a domain and
hence cannot be normal. Normality therefore forces (a_0\ne0), including in
U3. This also shows that the displayed cells exhaust the normal unbalanced
locus.

For U3, the ((u,z))-Hessian at (v=0) has determinant (-c_1^2). Solving
(f_u=f_z=0) to first nonzero order gives

\[
u_0=-\frac{v^2}{c_1}+O(v^3),\qquad
z_0=\frac{2a_0v^2}{c_1^2}+O(v^3),
\]

and literal substitution gives

\[
f(u_0,v,z_0)=\frac{a_0}{c_1^2}v^4+O(v^5).
\]

The coefficient is forced nonzero, so the parametric Morse form is exactly
(XY+\text{unit}\,v^4): the surface singularity is A3, with no
higher-coefficient specialization.

At fixed target ((u,v)),

\[
p=f_z=h_z+u(a'u+b'v+c'),\qquad
h_z=v^2-(4v+2v^2)z+3(1+v)z^2.
\]

Since (p_u(0)=c_1), (p=0) solves uniquely for (u). With cusp weights
((v,z,u)=(2,3,4)), the needed first terms are

\[
u=-\frac{v^2}{c_1}+\frac{4vz}{c_1}+\text{higher},
\]

and substitution in (f) gives the weight-eight edge

\[
2vz^2+\frac{a_0}{c_1^2}v^4=0.
\]

The factor (v) is the face leading to the other Newton region, not a third
component. The nonvertical factor is the irreducible cusp

\[
v=t^2,\quad z=\lambda t^3+O(t^4),\quad
u=-t^4/c_1+O(t^5),\quad
2\lambda^2=-a_0/c_1^2.
\]

The two signs of (lambda) are the same germ under (t\mapsto-t). Its
(A)-degree is four.

For the tangent pair put (y=z-v). Then

\[
h=zy\{y(1-z)+z^2\}.
\]

With weights ((z,y,u)=(1,2,4)), the fixed-(v) derivative is
(partial_z+partial_y), and the leading polar equation is
(z(2y+z^2)=0). The strict solution is

\[
y=-z^2/2+O(z^3),\qquad u=z^4/(4c_1)+O(z^5),
\]

a single smooth reduced degree-four germ. The controlling coefficients
(a_0/c_1^2) and (1/(4c_1)) cannot vanish.

Finally, at (u=0), the roots of (h) in (z), after unit/monic
normalization, are (0,v,v/(1+v)). Their pairwise differences have
(v)-orders (1,1,2), so

\[
\operatorname{length}\mathbf C[[v,z]]/(h,h_z)
=\operatorname{ord}_v\operatorname{disc}_z(h)=2(1+1+2)=8.
\]

The two reduced germs already contribute (4+4=8); there is no hidden
factor, component, or coefficient cancellation. This independently confirms
the claims at the local producer's lines 44-74 and 90-158.

## 2. Exact D square completion — `CONFIRMED`

Assume (b(0)=c'(0)=0), and write

\[
b=zB,\quad c=z^2C,\quad y=z-v,\quad \Delta=B+C,
\quad L=bv+c=z(-By+z\Delta).
\]

Since (a_0\ne0), (a) is a unit. Set (x=au+L/2). Then, without
discarding a term,

\[
af=x^2+ah-L^2/4.
\]

Using (h=z(1-z)y^2+z^3y) and collecting powers of (y) gives

\[
af=x^2+zPy^2+z^3Qy-z^4\Delta^2/4,
\]

where

\[
P=a(1-z)-zB^2/4,\qquad Q=a+B\Delta/2.
\]

Completing the square with

\[
Y=y+\frac{z^2Q}{2P},\qquad
K=\Delta^2+zQ^2/P
\]

gives the exact identity

\[
af=x^2+zPY^2-\frac{z^4}{4}K.
\]

Thus every sign, unit, and factor (1/4) in producer lines 193-217 is
correct.

Now

\[
\delta=\Delta(0)=b'(0)+c''(0)/2.
\]

If (delta\ne0), then (K(0)=\delta^2\ne0), and unit changes put the
equation in D5 form (x^2+zy^2+\text{unit}\,z^4=0). If (delta=0), then
(Delta^2=O(z^2)), while (P(0)=Q(0)=a_0), so

\[
K=z(a_0+O(z)).
\]

The forced coefficient of (z^5) is nonzero. The singularity is exactly D6;
D7, a modulus-special higher jump, and any further leading cancellation are
impossible while (a_0\ne0).

## 3. D polars, exact length, and the D6 correction — `CONFIRM_WITH_CORRECTIONS`

All derivatives here remain (p=f_z) at fixed ((u,v)); the square-completed
coordinate (x) is not incorrectly differentiated as a target coordinate.

For the common transverse region take (z=t^2), (y\asymp z), and
(u\asymp t^3). The initial equations are

\[
y(y+2z)=0,\qquad a_0u^2+zy^2=0.
\]

The root (y=-2z) gives one irreducible reduced cusp

\[
z=t^2,\qquad u^2=-(4/a_0)z^3+\text{higher},
\]

of (A)-degree three. The root (y=0) enters the tangent-pair region.

For D5 put (y=Y_0z^2, u=Uz^2). With
(gamma=B(0)+2C(0)=b'(0)+c''(0)), direct expansion gives

\[
U(a_0U+\delta)=0,\qquad \gamma U+2Y_0+1=0.
\]

The roots (U=0) and (U=-\delta/a_0) are distinct. The second is a
smooth degree-two germ. At the zero root (Y_0=-1/2); substituting
(u=Wz^3) in the next surface term gives

\[
\delta W-1/4=0,\qquad u=z^3/(4\delta)+O(z^4),
\]

a second smooth degree-three germ. Together with the transverse cusp this is
exactly (2+3+3).

For D6, (delta=0), and the pair surface edge is

\[
a_0u^2-z^5/4=0.
\]

Since (gcd(2,5)=1), this is one irreducible reduced branch

\[
z=t^2,\qquad u=kt^5+\cdots,\qquad k^2=1/(4a_0),
\]

of degree five. It combines with the transverse degree-three cusp to give
(3+5).

There is one literal error in producer line 285. The generic D6 statement

```text
y=-z^2/2+O(z^3)
```

is too strong. Write

\[
y=-t^4/2+\ell t^5+\cdots,\quad z=t^2,\quad u=kt^5+\cdots.
\]

The (t^7) term of the fixed-target polar is

\[
2\ell+\gamma k=0.
\]

When (delta=0), (C(0)=-B(0)), hence (gamma=-B(0)) and generically

\[
\ell=B(0)k/2\ne0.
\]

The exact safe replacement is

\[
y=-z^2/2+O(z^{5/2})
\]

on the normalization, equivalently (y=-t^4/2+O(t^5)). The cross term in
(y(y+z^2)) cancels, so this correction first affects the surface above the
controlling (z^5) edge. It changes neither irreducibility, (3+5), nor the
resolution site below.

The same discriminant calculation as in item 1 gives total local length eight
in every cell. No polar component lies in \(u=0\). At a generic point of each
listed branch the relevant Newton root is simple, so the Cartier divisor of
\(p\) has coefficient one there. The displayed reduced
branches already contribute all eight units. This simultaneously proves
coefficient one, excludes a hidden component, and confirms the partitions.

## 4. Minimal marked resolutions and physical sites — `CONFIRMED`

### 4.1 U3/A3

In the first (v)-chart, (u=vU, z=vZ). At (v=0), the reduced
exceptional equation is

\[
U(a_0U+c_1Z)=0.
\]

Call (U=0) (E_1) and the other component (E_3). Their residual point
(U=Z=0) is A1; its blowup inserts (E_2). Since
(p=v\,\partial_Z(f/v^2)), direct generic-chart substitution gives

\[
\operatorname{ord}_{E_1}p=2,\qquad
\operatorname{ord}_{E_2}p=2,\qquad
\operatorname{ord}_{E_3}p=1.
\]

For example, on generic (E_1) the surface equation gives
(U=-v(Z-1)^2/c_1+\cdots), and
(p=2v^2Z(Z-1)+\cdots). In the residual A1 (Z)-chart
(v=ZV, U=ZW), (p=Z^2V(c_1W+V+\cdots)), giving the middle order two.

The smooth polar meets (E_1) at (Z=1). The cusp has
((v,U,Z)\sim(t^2,-t^2/c_1,\lambda t)), so after resolving the A1 it passes
through the node (E_1\cap E_2), contributing once to each component. Thus

\[
m=(2,2,1),\qquad n=2e_1+e_2.
\]

The typing matters. On the minimal ADE resolution the two section branches
and the smooth polar all reach the point (Z=1) of (E_1), but they are
three distinct germs: with (q=Z-1), their slopes (q/v) are (0,-1,-1/2).
One extra embedded blowup separates them. The cusp polar is at
(E_1\cap E_2), while (L) reaches a different smooth point of (E_2).
Formal vectors, physical points, and analytic germs are not being identified.

### 4.2 The first D chart and its label

In square-completed coordinates, put (x=zx_1, Y=zy_1). The strict surface
is

\[
G_1=x_1^2+zP y_1^2-z^2K/4=0.
\]

At generic (y_1), the reduced exceptional curve has (x_1=z=0), and

\[
z=-x_1^2/(P(0)y_1^2)+\cdots.
\]

Hence \(x_1\) is the surface uniformizer and
\(\operatorname{ord}(z)=2\), not one. In original coordinates
(y=zy_1+O(z^2)), (u=zx_1/a_0+O(z^2)), and

\[
p=z^2\{y_1(y_1+2)+O(x_1,z)\}.
\]

Thus this component has \(\operatorname{ord}p=4\). The point
\(y_1=\infty\) is A1; its resolution inserts the component met by (L),
called (E_1).
The generic first component joins that (E_1) to the residual D tree and is
therefore standard vertex (E_2). This is why the raw factor (z^2) gives
four, and why the component is (E_2), rather than a relabelled spin.

The root (y_1=-2) is the transverse degree-three polar, at a smooth point
of (E_2).

### 4.3 D5

The point (y_1=0) is residual A3. Blow it up in the (z)-chart via
(x_1=zx_2, y_1=zy_2). Then

\[
G_2=x_2^2+zP y_2^2-K/4=0,
\]

whose exceptional components are (x_2=\pm\delta/2). These are the two
spins (E_4,E_5); their point at infinity is A1, whose resolution inserts
(E_3), joining (E_2) to both spins.

For a pair polar,

\[
x_2=x/z^2=a_0U+\delta/2+\cdots.
\]

Consequently the (U=0) degree-three germ lands on the plus spin, while the
(U=-\delta/a_0) degree-two germ lands on the minus spin. Both have finite
(y_2), so both sites are smooth; they cannot specialize to the node at
infinity. Together with the transverse germ, the three distinct sites are
(E_2,E_4,E_5).

This construction also directly gives the divisorial orders

\[
(m_1,m_2,m_3,m_4,m_5)=(2,4,5,3,3).
\]

For clarity, representative valuations of ((z,y,u;p)) are
(E_1:(2,1,2;2)), (E_2:(2,2,3;4)),
(E_3:(2,3,4;5)), and (E_4,E_5:(1,2,\ge2;3)).
Literal Cartan multiplication, now only a check on the resolved calculation,
is

\[
C_{D5}(2,4,5,3,3)^t=(0,1,0,1,1)^t.
\]

Thus (n=e_2+e_4+e_5), not the earlier two-site boundary vector.

The boundary sites are separately visible. Put

\[
q_0=Q(0)/(2P(0))=1/2+B(0)\delta/(4a_0).
\]

On the retained plus spin the two sections have coordinates
(y_2=q_0,q_0-1), while the degree-three polar has
(y_2=q_0-1/2). These are three distinct points. The degree-two polar is on
the opposite spin, and (L) is on (E_1).

### 4.4 D6

Here (y_1=0) is residual D4. The same second (z)-blowup gives

\[
G_2=x_2^2+z\{P y_2^2-(K/z)/4\}=0.
\]

At (z=0) its generic reduced exceptional is the D4 central component
(E_4). The points (y_2=\pm1/2) are two residual A1 points, producing
spins (E_5,E_6); the point at infinity produces (E_3) between (E_2)
and (E_4). The corrected degree-five Puiseux expansion still has
(Y/z^2\to0), so it meets a smooth point of (E_4), not either spin node.
The transverse branch remains at (y_1=-2) on (E_2).

The direct valuation sequence is

\[
(m_1,m_2,m_3,m_4,m_5,m_6)=(2,4,5,6,3,3),
\]

with representative \((z,y,u;p)\) valuations
\(E_3:(2,3,4;5)\), \(E_4:(2,4,5;6)\), and, up to spin naming,
\(E_5:(1,2,\ge3;3)\), \(E_6:(1,3,\ge3;3)\), in addition to the
common \(E_1,E_2\) values.
Again the Cartan check is

\[
C_{D6}(2,4,5,6,3,3)^t=(0,1,0,1,0,0)^t.
\]

Hence (n=e_2+e_4). The sections instead arrive at
(y_2=\pm1/2) and meet (E_5,E_6) after those A1 resolutions; (L) meets
(E_1). Section, boundary, and polar sites have not been conflated.

## 5. Local replay corrigendum — `CONFIRMED`

The original `ops/f5_unbalanced_polar_replay.py` has 12 AST `Assert` nodes
and no explicit verification function. Under `-O` and `-OO`, all assertion
comparisons and their raises are stripped. The arithmetic expressions and
three hard-coded print rows remain, but on the hard-coded nonzero grid they
supply no live invariant gate. Thus the original ordinary run has evidentiary
content, while its optimized “passes” are vacuous. The corrigendum's diagnosis
at lines 18-32 is exact.

The v2 AST has zero `Assert` nodes, no `__debug__` reference, and 17 explicit
`require` calls. I ran:

```text
python3 ops/f5_unbalanced_polar_replay_v2.py
python3 -O ops/f5_unbalanced_polar_replay_v2.py
python3 -OO ops/f5_unbalanced_polar_replay_v2.py
```

All exited zero with identical three-row output. I then ran the deliberate D5
mutation in all three modes. Each exited one with

```text
ReplayFailure: D5 Cartan/contact mismatch
```

The old and v2 positive outputs also agree byte-for-byte apart from their
final shell capture newline handling. V2 is optimization-safe and the
corrigendum accurately supersedes only the old optimized-mode evidence.
It verifies a hand-coded arithmetic abstraction; it does not derive the
normal form, prove Newton exhaustiveness, construct the resolution, or prove
the analytic theorem.

## 6. The nine-blowup lattice and all q=8 total classes — `CONFIRM_WITH_CORRECTIONS`

### 6.1 The ruled lattice and balanced total

On (F_2),

\[
S_0^2=-2,\quad S_0F=1,\quad F^2=0.
\]

The resolved surface has (K^2=-1), whereas (K_{F_2}^2=8); hence the
(S)-adapted model has exactly nine point blowups. In the orthogonal
total-transform basis,

\[
P_iP_j=-\delta_{ij},\quad S_0P_i=FP_i=0,
\]

\[
A=2S_0+5F-\sum_{1}^{9}P_i,\quad B=F,
\quad K=-2S_0-4F+\sum_iP_i=-A+B.
\]

Direct checks are (A^2=3, A.B=2, B^2=0, K^2=-1), and

\[
r^*R_X=2A+B=4S_0+11F-2\sum_iP_i.
\]

For q=8,

\[
L=P_l,\qquad T=S_0+2F-\sum_{i\in I}P_i,\quad |I|=4,
\]

with (l\notin I), and (O) is the other four indices. From
(A=S_0+L+T+Z_H),

\[
Z_H=3F-2P_l-\sum_{o\in O}P_o.
\]

The balanced Cartan products are literally

\[
C_{A4}(2,3,2,1)^t=(1,2,0,0)^t,
\]

\[
C_{A5}(2,3,3,2,1)^t=(1,1,1,0,0)^t.
\]

They equal the corresponding infinity contact vectors. Hence the balanced
exceptional ramification cycle is (M=Z_H). Relabel
(l=1, O=\{2,3,4,5\}, I=\{6,7,8,9\}). Then

\[
C^{(0)}=r^*R_X-Z_H
=4S_0+8F-\sum_i c_iP_i,
\]

\[
c=(0,1,1,1,1,2,2,2,2),\quad
\sum c_i=12,\quad \sum c_i^2=20.
\]

### 6.2 All contracted carriers and coefficients

Independently write a contracted carrier as
(Z=aS_0+bF-\sum x_iP_i). The charged carrier identities
(B.Z=1, A.Z=0, Z^2=-3), together with (Z.S_0=0), give

\[
a=1,\quad b=2,\quad \sum x_i=5,\quad \sum x_i^2=5.
\]

Thus all nine \(x_i\) are zero or one, and exactly five are one:

\[
Z_J=S_0+2F-\sum_{j\in J}P_j,\qquad |J|=5.
\]

Disjointness from (L) gives (l\notin J), and
(Z_J.T=2-|J\cap I|=0) gives (|J\cap I|=2). Hence
(|J\cap O|=3) and there are exactly

\[
\binom42\binom43=24
\]

labelled candidates. Subtracting one gives

\[
C^{(Z)}=3S_0+6F-\sum c_i^{(Z)}P_i,
\]

with multiset

\[
(0,0,0,0,1,1,1,2,2),\quad
\sum c_i^{(Z)}=7,\quad \sum(c_i^{(Z)})^2=11.
\]

For B5, three positive strict (B)-degrees leave coefficient one for (Z).
For B6 the coarse budget permits coefficient two, but every (J) contains
three (O)-coordinates of baseline value one; subtracting (2Z_J) makes
those residual multiplicities (-1). Therefore coefficient one is the only
carrier cell in both rows.

### 6.3 Chronological U roots and totals

Chronologically, the first inverse blowup gives \(P_1\); the second, at the
node of that exceptional curve with its fibre, gives the two spins
\(F-P_1-P_2\) and \(P_1-P_2\). Successive inverse blowups along the
remaining exceptional branch give \(P_k-P_{k+1}\), and the last exceptional
is \(L=P_s\). Thus reversing the fibre contractions gives

\[
R_s=F-P_1-P_2,\quad R_{s-1}=P_1-P_2,
\quad R_{s-2}=P_2-P_3,\ldots,
R_1=P_{s-1}-P_s,\quad L=P_s.
\]

Each root has square (-2), their intersections are exactly the D diagram,
and (L.R_1=1).

The \(T\)-contacts also determine the index sets rather than merely label
them. For the two spins,
\[
T.R_s=1-\mathbf1_{1\in I}-\mathbf1_{2\in I},\qquad
T.R_{s-1}=\mathbf1_{1\in I}-\mathbf1_{2\in I},
\]
and along the chain \(T.(P_k-P_{k+1})\) is the corresponding difference of
membership indicators. In U5, \(T\) meets the retained spin and no other D
root, so none of \(1,\ldots,5\) lies in \(I\), hence
\(I=\{6,7,8,9\}\). Literal summation
with (m=(2,4,5,3,3)) gives

\[
M_5=3F-P_2-P_3-2P_4-2P_5,
\]

\[
C_5=4S_0+8F-\sum c_iP_i,\quad
c=(2,1,1,0,0,2,2,2,2),
\]

with sum 12 and square norm 22.

For U6, \(T\) meets the other spin and no other D root, forcing
\(1\in I\), \(2,\ldots,6\notin I\), and therefore
\(I=\{1,7,8,9\}\). With
(m=(2,4,5,6,3,3)),

\[
M_6=3F-P_3-P_4-2P_5-2P_6,
\]

\[
C_6=4S_0+8F-\sum c_iP_i,\quad
c=(2,2,1,1,0,0,2,2,2),
\]

again with sum 12 and norm 22. Both totals have zero intersection with
(S_0,L,T).

### 6.4 Missing root family and exact repair

Producer lines 199-201 incorrectly call (P_i-P_j) the general integral
root satisfying (A.Q=B.Q=K.Q=0, Q^2=-2). Write
(Q=bF+\sum q_iP_i). Those equations give

\[
\sum q_i^2=2,\qquad 2b+\sum q_i=0.
\]

Up to sign, there are two families:

\[
P_i-P_j,\qquad F-P_i-P_j.
\]

The omission is repairable, not fatal. An affine ADE exceptional is away from
(H) and must be disjoint from (S_0), whereas

\[
(F-P_i-P_j).S_0=1.
\]

Thus the (F)-family is excluded rather than silently omitted. For
(P_i-P_j), (L)-disjointness excludes (l), and (T)-disjointness forces
(i,j) both in (I) or both in (O). These are the two H-disjoint oriented
orbits, 12 labels each.

Subtracting (mu(P_i-P_j)) changes
(c_i\mapsto c_i+\mu, c_j\mapsto c_j-\mu). For (mu=1), either orbit has
(sum c=12,sum c^2=22). Nonnegativity allows (mu=2) only in the I/I
orbit, producing I-coordinates ((4,0,2,2)) and norm 28. No
(mu\ge3) is possible. Thus there is one possible coefficient-two orbit,
not one unlabelled physical root.

The exact replacement for lines 199-201 is:

> Solving all four numerical root equations gives, up to sign,
> (P_i-P_j) and (F-P_i-P_j). Affine ADE exceptional curves are
> (H)-disjoint; the second family meets (S_0), so only the first remains.
> Disjointness from (L,T) then gives the I/I and O/O orbits.

With this repair, the class list and replay coverage are complete.

## 7. Euler allocation, horizontality, and the forest gate — `CONFIRM_WITH_CORRECTIONS`

Let (r_0) be the marked q=8 ADE rank, (r_{\rm aff}) the affine ADE rank,
and (k) the number of distinct reduced nonexceptional ramification primes.
The charged Euler theorem gives

\[
r_0+r_{\rm aff}+k\le8.
\]

By the charged rational-forest theorem, distinct physical q-tree sites force
the local germs onto distinct global primes: if one irreducible strict prime
carried two such germs, its single proper-transform vertex and the path
between the sites in the connected exceptional tree would form a graph
cycle. The charged global identity is
\(\sum_j A.C_j=8\); exceptional cycles and contracted carriers are
\(A\)-null. The coefficient-one local germs contribute total order eight,
so they exhaust this global intersection: each displayed local order is the
full \(A.C_j\), and no additional positive-(A\) ramification prime exists.
Therefore the exact allocations are:

| row | (r_0) | forced positive-A primes | remaining choices |
|---|---:|---:|---|
| B5/A4 | 4 | 3 | baseline; one A-null (Z); or one affine A1 tree |
| B6/A5 | 5 | 2 | baseline; one A-null (Z); or one affine A1 tree |
| U5/D5 | 5 | 3 | none: the cap is saturated |
| U6/D6 | 6 | 2 | none: the cap is saturated |

An extra nonexceptional prime has (A)-degree zero and hence is one of the
charged contracted (Z) carriers. A residual affine rank one is exactly one
A1 tree. Cartier coefficients do not change (k) or rank and are separately
handled in item 6. There is no U-row escape.

For a strict positive-A prime write

\[
C_j=a_jS_0+b_jF-\sum_i x_{ji}P_i,\qquad x_{ji}\ge0.
\]

The total strict classes in every cell have zero intersection with
(S_0,L,T): for the baseline/U/root cells the total data are
((a,b,c_l,\sum_Ic)=(4,8,0,8)), and for one (Z) they are
((3,6,0,6)). Each strict prime is effective and distinct from the three
strict (H) components. Local intersection multiplicities are nonnegative,
so zero total intersection forces, prime by prime,

\[
C_j.S_0=C_j.L=C_j.T=0.
\]

In particular (b_j=2a_j), (x_{jl}=0), and
(sum_{i\in I}x_{ji}=2a_j).

Producer lines 278-280 give a false proof of (a_j>0): a balanced (B_s)
fibre does not have only (L) and the root tree; it has the opposite
nonexceptional ((-1)) endpoint as well. The clean repair is numerical. Since

\[
d_j=A.C_j=5a_j-\sum_i x_{ji}>0
\]

for every displayed local polar degree and every (x_{ji}\ge0), one must
have (a_j\ge1). Thus every strict polar prime is horizontal, but not for the
reason printed there.

Now pass to a common embedded strict-SNC resolution. Every strict prime has a
distinguished known attachment to the connected q=8 exceptional subtree, so
any two distinct primes already have a path between them through that tree. Any
additional common point supplies a second path and violates the charged
rational-forest theorem. This includes:

- two branches of the same global prime at distinct q-tree sites (the one
  strict-transform vertex closes a cycle);
- two distinct primes meeting transversely elsewhere;
- tangency, whose resolution chain still gives a second connection;
- a multiple point, whose resolution may branch rather than merely
  subdivide, but cannot remove the second connection;
- a polar through an exceptional node, where the node blowup only subdivides
  the known q-tree path and supplies its single attachment;
- any further embedded blowups, which subdivide edges or add leaves and do
  not lower the graph's first Betti number.

Unibranch self-singularities of one prime need not be excluded and do not
affect pairwise intersections. Distinctness of the local physical sites is
load-bearing; a mere formal contact vector would not suffice.

It follows on the nine-blowup smooth surface that

\[
C_i.C_j=0\qquad(i\ne j).
\]

Thus the forest gate, individual (H)-disjointness, and absence of same-prime
or embedded-resolution escapes are valid. The exact wording repairs are to
replace the false balanced-fibre horizontality sentence as above and replace
“merely subdivide” for a multiple point by the second-path argument.

## 8. Closed-form intersection obstruction — `CONFIRMED`

After item 7,

\[
C_j=a_jS_0+2a_jF-\sum_lx_{jl}P_l.
\]

For (j\ne k),

\[
C_j.C_k=2a_ja_k-\sum_lx_{jl}x_{kl}.
\]

Put (c_l=\sum_jx_{jl}) and
(Q=\sum_{j,l}x_{jl}^2). Since

\[
\sum_lc_l^2=Q+2\sum_{j<k,l}x_{jl}x_{kl},
\]

one obtains the exact identity

\[
\sum_{j<k}C_j.C_k
=2\sum_{j<k}a_ja_k-\frac{\sum_lc_l^2-Q}{2}.
\]

Every (x_{jl}) is a nonnegative integer, hence (x_{jl}^2\ge x_{jl}) and

\[
Q\ge\sum_{j,l}x_{jl}=\sum_lc_l.
\]

The resulting table is:

| cell | minimum (2\sum_{j<k}a_ja_k) | ((\sum c^2-\sum c)/2) | lower bound |
|---|---:|---:|---:|
| B5 baseline, (a=(2,1,1)) | 10 | 4 | 6 |
| B6 baseline, positive pair summing 4 | 6 | 4 | 2 |
| B5 one Z, (a=(1,1,1)) | 6 | 2 | 4 |
| B6 one Z, (a=(1,2)) | 4 | 2 | 2 |
| B5 simple affine A1 | 10 | 5 | 5 |
| B6 simple affine A1 | 6 | 5 | 1 |
| B5 affine coefficient two | 10 | 8 | 2 |
| U5/D5 | 10 | 5 | 5 |
| U6/D6 | 6 | 5 | 1 |

These reproduce every producer entry.

For the remaining B6 coefficient-two cell,

\[
c_I=(4,0,2,2),\quad c_O=(1,1,1,1),\quad c_l=0.
\]

Let the degree-two prime have \(B\)-degree \(a\), so its companion has
\(B\)-degree \(4-a\). Its disjointness equations give

\[
\sum_Ix=2a,\qquad \sum_Ox=3a-2.
\]

Nonnegativity leaves \(a=1,2\). For \(a=3\), the degree-two prime would
require O-sum seven although the total O-capacity is four; equivalently, its
degree-six companion would have O-sum \(6-3a=-3\). Since every O-total is
one, the mutual O-dot product is zero. If \(a=1\), the
maximum I-dot product under capacities ((4,0,2,2)) and I-sum two is four,
so (C_1.C_2\ge6-4=2). If (a=2), the maximum at I-sum four is six,
attained at ((2,0,1,1)), so (C_1.C_2\ge8-6=2). This completes the only
cell not covered by the uniform positive bound.

Chronological proximity, irreducibility, effectivity, and cluster conditions
only remove nonnegative integer arrays from this calculation. Omitting them
genuinely enlarges the search; positivity on the enlargement is therefore a
safe contradiction. The closed-form proof is complete without enumeration.

## 9. q=8 replay and independent arithmetic — `CONFIRMED`

I ran the q=8 replay in ordinary, `-O`, and `-OO` modes. Each exited zero and
emitted the identical SHA-256 digest

```text
dcfbe164178ea93e85c608526edb588ea96aaf6d6488c3865660c708b79f3da7
```

Its AST has zero `Assert` nodes, 23 explicit `require` calls, and no
`__debug__` gate. The forged summary with `pairwise_zero=1` is passed to the
same explicit zero-survivor predicate and rejected; the emitted JSON records
`forged pairwise_zero=1 rejected`. This control remains live in all three
optimization modes. It tests the final gate, not the analytic input.

Independent arithmetic, without importing the replay, reproduced the four
Cartan products, both U cycles, the 24 carrier residuals, the two 12-element
oriented simple-root orbits, the 12-element coefficient-two I-orbit, and the
closed-form bounds in item 8. The replay's cell counts also reproduce exactly:

| cell | linear | adjunction-valid | pairwise-zero |
|---|---:|---:|---:|
| B5 baseline | 648 | 270 | 0 |
| B6 baseline | 59 | 37 | 0 |
| U5 | 504 | 90 | 0 |
| U5 without T | 2860 | 370 | 0 |
| U6 | 67 | 21 | 0 |
| B5 one Z | 33 | 15 | 0 |
| B6 one Z | 8 | 5 | 0 |
| B5 simple O-root | 504 | 90 | 0 |
| B6 simple O-root | 49 | 19 | 0 |
| B5 simple I-root | 513 | 162 | 0 |
| B6 simple I-root | 52 | 30 | 0 |
| B5 double I-root | 234 | 18 | 0 |
| B6 double I-root | 33 | 9 | 0 |

The omitted (F-P_i-P_j) family is not an enumeration hole after the
(S_0)-disjointness repair in item 6. The replay corroborates finite lattice
arithmetic only; it does not prove the local analytic theorem, physical sites,
effectivity, the forest theorem, or existence of an incidence surface.

## 10. Separate final verdicts and maximum safe theorem — `CONFIRM_WITH_CORRECTIONS`

### 10.1 Local theorem

`CONFIRM_WITH_CORRECTIONS`. Under the stated normal, reduced,
finite-near-infinity F5 hypotheses, the unbalanced cells and their strict
polar data are exactly

| row | strict A-degrees | (m) | (n) |
|---|---|---|---|
| U3/A3 | (4+4) | ((2,2,1)) | (2e_1+e_2) |
| U5/D5 | (2+3+3) | ((2,4,5,3,3)) | (e_2+e_4+e_5) |
| U6/D6 | (3+5) | ((2,4,5,6,3,3)) | (e_2+e_4) |

Every strict germ is reduced and has Cartier coefficient one. Repair only the
generic D6 pair remainder to
(y=-z^2/2+O(z^{5/2})) on its normalization. The theorem table and all sites
are unchanged.

### 10.2 Balanced q=8 global elimination

`CONFIRM_WITH_CORRECTIONS`. B5/A4 and B6/A5 have no global lattice survivor
in the charged scope. The Euler allocation, total classes, H-disjointness,
forest pairwise-zero requirement, and positive-intersection contradiction are
complete. Promotion must include the explicit (F-P_i-P_j) exclusion and the
correct numerical proof of horizontality.

### 10.3 Conditionally unbalanced q=8 global elimination

`CONFIRM_WITH_CORRECTIONS`. As an implication from the exact local U5/U6
data, the global elimination is complete. U5 and U6 saturate the Euler cap,
their chronological total classes are correct, and the closed-form bounds are
strictly positive. The present review independently confirms the required
local input, subject only to the harmless D6 remainder repair.

### 10.4 Composition

`CONFIRM_WITH_CORRECTIONS`. The q=8 singular-F5 universe in this presentation
is

\[
\{B5/A4,B6/A5,B7/A6,B8/A7,B9/A8,U5/D5,U6/D6\}.
\]

The charged balanced integration already removes B7, B8, and B9. Items 6-8
remove B5 and B6, and the confirmed local theorem composed with the same
global argument removes U5 and U6. Therefore the maximum safe theorem is:

> In the charged normal, reduced, finite-near-infinity F5
> quadratic-incidence proper-cubic-block first-leg scope for the fixed charged
> trace-zero presentation, including the charged dominant
> \(\mathbf A^2\to U\) input used by the Euler/forest theorems, no singular-F5
> q=8 row occurs.

This is an elimination theorem, not an attainment or realization theorem. It
does not eliminate q=6 B3/A2 or U3/A3; a smooth F5 row; nonreduced infinity;
projective nonfiniteness or basepoints; degree or trace-zero presentation
drop; other quadratic strata; higher block degree; or any presentation outside
the charged first-leg hypotheses. It proves no analytic realization or
effectivity result, constructs no finite algebra or polynomial map, and gives
no counterexample or conclusion about JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31509`.
- Body SHA-256:
  `f0917ffb01e024dcc6b50503710172ac340ba765640681b304aad6ffd01dc340`.
- Frozen basis: `4decd33d5caf8553bcbaa199b93a900ecabeee18`.
