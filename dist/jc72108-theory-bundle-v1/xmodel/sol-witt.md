# Witt–Bockstein search around characteristic-two plane collisions

**Date:** 2026-08-14  
**Engine:** cases/witt_check.py  
**Primary verdict:** **NEVER-VANISHES-PROVED** on the registered Mondello-hull-plus-one-shell stratum

## Executive summary

For a plane Keller pair \(P,Q\in\mathbf F_2[x,y]\), take the coefficientwise
0/1 lifts and put

\[
E_F=\frac{[\widetilde P,\widetilde Q]-1}{2}\pmod 2.
\]

The unrestricted first lifting obstruction is exactly

\[
o_2(F)=[E_F\,dx\wedge dy]\in H^2_{dR}(\mathbf F_2[x,y]).
\]

It vanishes if and only if \(E_F\) has no monomial \(x^iy^j\) with both
\(i,j\) odd. This is the complete arbitrary-support determinant-one
\(W_2(\mathbf F_2)=\mathbf Z/4\) obstruction, not merely a necessary Cartier
screen. Marked collision points add no first-order obstruction when allowed to
move in their residue classes.

The registered finite search allowed every lattice monomial in Mondello's two
Newton hulls and one nonnegative Manhattan shell, retained the original hull
vertices, fixed the linear jet to \((x,y)\), and imposed

\[
(0,1),(1,0),(1,1)\longmapsto(0,1).
\]

| stage | exact count |
|---|---:|
| \(P\)-support masks | \(2^{14}=16{,}384\) |
| \(P\)-masks satisfying its collision rows | \(4{,}096\) |
| \(P\)-masks admitting a Keller \(Q\) | \(4\) |
| normalized Keller-collision data | **1,152** |
| odd generic degree | **8** |
| nonzero unrestricted Cartier obstruction | **1,152** |
| vanishing unrestricted obstruction | **0** |

Thus no member of the registered stratum lifts to a plane Keller map over
\(\mathbf Z/4\), regardless of correction support. In particular, all eight
odd-degree data are obstructed. This is an exact rigidity result, not a miss
count.

There is one boundary finding. If the original hull-vertex guards are dropped
and all normalized masks inside the unshelled hulls are admitted, there are 288
Keller collisions and **48 have vanishing unrestricted \(W_2\) class**. Exact
generic-degree computation shows that all 48 have even degree. They are outside
the registered core-vertex/odd-degree stratum, but the engine banks them and
constructs first-stage witnesses.

## Premise correction: the nonzero pilot is two-dimensional

The task prompt calls the prior nonzero pilot the “3D counterexample map.” That
is not what xmodel/sol-lateral.md established. The nonzero pilot is
**Mondello's plane map**. The literal three-dimensional Huq–Kuruvilla datum has
the opposite verdict.

For

\[
G=(x+x^2y,\ y+xz+x^2yz,\ z+x^2z^2)
\]

the coefficientwise integer lift has half-determinant error

\[
E_G=xy+x^2z+x^4z^2+x^5yz^2.
\]

No term has all three exponents odd, so its top \(H^3_{dR}\) Cartier class
vanishes. More decisively, the engine verifies

\[
\begin{aligned}
H_1&=x^3z+x^5z^2,\\
H_2&=x^3z^2+x^5z^3+x^2yz+x^3y^2z+x^6yz^3+x^7y^2z^3,\\
H_3&=xyz+x^5yz^3
\end{aligned}
\]

and

\[
\det D(G+2H)\equiv1\pmod4.
\]

The points \((0,1,0),(3,1,0),(3,1,3)\) all map to \((0,1,0)\) modulo \(4\)
and reduce to the three original collision points. The command

    python3 cases/witt_check.py audit-3d

checks this exactly. [Huq–Kuruvilla gives the 3D map and collision](https://arxiv.org/html/2607.20968v1);
[Mondello derives the plane map as a preserved fiber in Section 10](https://arxiv.org/html/2608.02634v1).
This correction does not weaken the plane result below.

## 1. The collision object

Let \(k=\mathbf F_2\), let \(S_P,S_Q\subset\mathbf N^2\) be finite supports,
and let \(r\ge2\). The **marked Keller-collision locus**
\(\mathcal C_{S_P,S_Q,r}\) is the locally closed \(k\)-scheme of tuples

\[
\xi=(P,Q;a_1,\ldots,a_r;c)
\]

such that:

1. \(\operatorname{supp}P\subseteq S_P\) and
   \(\operatorname{supp}Q\subseteq S_Q\);
2. \([P,Q]=1\) coefficient by coefficient;
3. \(F(a_i)=c\) for every \(i\), where \(F=(P,Q)\);
4. \(a_i\ne a_j\) for \(i\ne j\).

Exact-support/nonzero-corner conditions are open conditions. A prescribed
constant term, linear jet, collision triple, or image cuts out a normalized
closed slice. Generic degree being odd is a separately certified filter, not
one of these elementary coefficient equations.

The equation \([P,Q]=1\) makes \(dP,dQ\) a basis of
\(\Omega^1_{k[x,y]/k}\). Hence \(P,Q\) are algebraically independent,
\(k(x,y)/k(P,Q)\) is finite separable, and \(F\) is étale. The finite census
fixes the special-fiber points and image to Mondello's values; in the geometric
deformation problem the marked points may lift. Freezing their literal
Teichmüller coordinates would be an extra support-dependent gauge condition.

## 2. Obstruction calculus

### 2.1 General equation-scheme class

For any integral polynomial equation map \(\Phi\), let \(\xi_0\) be an
\(\mathbf F_2\)-point and choose an integral lift \(\widetilde\xi\). Define

\[
b_{\widetilde\xi}=\frac{\Phi(\widetilde\xi)}2\pmod2.
\]

Taylor expansion gives

\[
\Phi(\widetilde\xi+2\delta\xi)
\equiv2\bigl(b_{\widetilde\xi}+D\Phi_{\xi_0}(\delta\xi)\bigr)\pmod4.
\]

Therefore

\[
o_2(\xi_0)=[b_{\widetilde\xi}]
\in\operatorname{coker}D\Phi_{\xi_0}
\]

is the first obstruction. Changing the integral lift changes \(b\) by a
linearized column, so the class is canonical. It vanishes exactly when this
square-zero lifting step has a solution.

### 2.2 Keller specialization and Bockstein

For the canonical lifts write

\[
[\widetilde P,\widetilde Q]=1+2E_F.
\]

The form \(\alpha_0=P\,dQ-x\,dy\) is closed modulo \(2\), while

\[
d\widetilde\alpha=2E_F\,dx\wedge dy.
\]

Thus \([E_Fdx\wedge dy]\) is the first integral de Rham
Bockstein/connecting class reduced modulo \(2\). This is the elementary affine
instance of the Cartier–Bockstein relation in
[Franjou, Proposition 2 and Theorem 3](https://arxiv.org/html/math/0404123v2).

A correction

\[
P_2=\widetilde P+2A,\qquad Q_2=\widetilde Q+2B
\]

has determinant one modulo \(4\) exactly when

\[
E_F+L_F(A,B)=0,\qquad
L_F(A,B)=[A,Q]+[P,B].
\]

The key identity is

\[
L_F(A,B)\,dx\wedge dy=d(A\,dQ-B\,dP).
\]

Since \(dP,dQ\) are a basis, \((A,B)\mapsto A\,dQ-B\,dP\) is an
\(R=k[x,y]\)-module isomorphism \(R^2\simeq\Omega^1_R\). Consequently

\[
\operatorname{im}L_F=d\Omega^1_R,\qquad
\operatorname{coker}L_F\simeq H^2_{dR}(R).
\]

This proves that Cartier is complete for the unrestricted plane problem.

### 2.3 Explicit Cartier rule and constructive sufficiency

In characteristic two,

\[
H^2_{dR}(k[x,y])
=\bigoplus_{a,b\ge0}k\,[x^{2a+1}y^{2b+1}dx\wedge dy].
\]

A monomial \(x^iy^jdx\wedge dy\) is a derivative if \(i\) or \(j\) is even;
it is not if both are odd. The top Cartier rule is

\[
C(x^{2a+1}y^{2b+1}dx\wedge dy)=x^ay^b dx\wedge dy,
\]

and it kills all other monomials. See also the affine-space coefficient rule in
[Stacks, Tag 0FW2](https://stacks.math.columbia.edu/tag/0FW2). Therefore

\[
o_2(F)=0
\quad\Longleftrightarrow\quad
[x^{2a+1}y^{2b+1}]E_F=0\quad\text{for all }a,b.
\]

The engine proves sufficiency constructively: it integrates \(E_F\) to a
1-form \(Udx+Vdy\), solves \(Udx+Vdy=A\,dQ-B\,dP\), and verifies the untouched
determinant modulo \(4\).

### 2.4 Collision rows

Let the marked points \(a_i\) have common image \(c\). Write their lifts and the
target lift as \(\widetilde a_i+2u_i\) and \(\widetilde c+2v\), and put

\[
e_i=\frac{\widetilde F(\widetilde a_i)-\widetilde c}{2}\pmod2.
\]

The collision equation linearizes to

\[
e_i+(A,B)(a_i)+JF(a_i)u_i-v=0.
\]

Every \(JF(a_i)\) is invertible, so after \(A,B,v\) are chosen this uniquely
determines \(u_i\). Distinct special-fiber points remain distinct. Thus the
moving-point augmented cokernel is still \(H^2_{dR}(R)\). This is also the
square-zero lifting property of an étale morphism
([Stacks, Tag 00UP](https://stacks.math.columbia.edu/tag/00UP)).

At a later step \(2^n\to2^{n+1}\), set

\[
E_n=\frac{[P_n,Q_n]-1}{2^n}\pmod2.
\]

The correction equation again uses the same special-fiber operator \(L_F\).
Each stage therefore has a class in the same \(H^2_{dR}\), although \(E_n\)
depends on earlier choices.

## 3. Mondello control

\[
\begin{aligned}
P_M&=x+x^2y+x^4+x^6y^2,\\
Q_M&=y+x^5+x^6y+x^7y^2+x^8y^3.
\end{aligned}
\]

This map has determinant one, degree \(3\), and the marked collision; the exact
degree and separability are proved via the hidden cubic and actual-target
irreducibility in
[Mondello, Theorem 1.2 and Sections 3–5](https://arxiv.org/html/2608.02634v1).

The engine obtains

\[
\operatorname{supp}E_M=
\{(1,1),(5,2),(7,1),(9,3),(10,1),(11,2),(12,3),(13,4)\}.
\]

Its odd–odd part is \(\{(1,1),(7,1),(9,3)\}\), hence

\[
C(E_Mdx\wedge dy)=(1+x^3+x^4y)dx\wedge dy\ne0.
\]

Therefore Mondello's plane map has no determinant-one lift modulo \(4\) with
any polynomial correction support, and hence no geometric \(W_2\)
Keller-collision lift.

## 4. Registered search

### 4.1 Supports and normalization

\[
\begin{aligned}
\Delta_P&=\operatorname{conv}\{(0,0),(4,0),(6,2),(2,1)\},\\
\Delta_Q&=\operatorname{conv}\{(0,0),(5,0),(8,3),(0,1)\}.
\end{aligned}
\]

Their nonnegative lattice-point sets have sizes \(10\) and \(18\). For finite
\(T\subset\mathbf N^2\), define

\[
T^+=\{u\in\mathbf N^2:\min_{t\in T}\|u-t\|_1\le1\}.
\]

The registered supports \(S_P=(\Delta_P\cap\mathbf N^2)^+\) and
\(S_Q=(\Delta_Q\cap\mathbf N^2)^+\) have sizes \(20\) and \(31\). The
coefficient slice is

\[
p_{00}=q_{00}=0,\quad p_{10}=q_{01}=1,\quad p_{01}=q_{10}=0,
\]

with retained core vertices

\[
p_{21}=p_{40}=p_{62}=q_{50}=q_{83}=1,
\]

and the three marked points map to \((0,1)\). Boolean mask equations enumerate
the special fiber only; the engine does not put them into the Witt tangent
problem.

### 4.2 Exact enumeration and complete bank

There are 14 free \(P\)-bits and 26 free \(Q\)-bits. Exactly 4,096 \(P\)-masks
satisfy the evaluation rows. For fixed \(P\), the Keller and \(Q\)-collision
equations are linear in the \(Q\)-bits. Exact \(\mathbf F_2\) reduction leaves
four \(P\)'s with \(Q\)-solution dimensions \(9,9,6,6\), giving

\[
2^9+2^9+2^6+2^6=1152.
\]

The complete \(P\)-classification is

\[
P=P_M+s(x^2+x^4y+x^5+x^6y)+t(x^2y^2+x^4y^2),
\qquad s,t\in\mathbf F_2.
\]

Write \(q_{ij}=[x^iy^j]Q\). For every solution,

\[
\begin{gathered}
q_{01}=q_{50}=q_{61}=q_{72}=q_{83}=1,\\
q_{00}=q_{10}=q_{02}=q_{11}=q_{12}=q_{21}=q_{31}=q_{51}
=q_{53}=q_{71}=q_{73}=q_{93}=0.
\end{gathered}
\]

If \(s=0\), the nine coefficients

\[
q_{20},q_{22},q_{30},q_{32},q_{40},q_{42},q_{52},q_{62},q_{82}
\]

are free and

\[
\begin{aligned}
q_{41}&=q_{30},&q_{43}&=q_{32},&q_{63}&=q_{52},\\
q_{60}&=q_{20}+q_{30}+q_{40},&&
q_{84}&=q_{22}+q_{30}+q_{42}+q_{62}+q_{82}.
\end{aligned}
\]

If \(s=1\), the six coefficients
\(q_{20},q_{22},q_{40},q_{42},q_{62},q_{82}\) are free and

\[
\begin{gathered}
q_{30}=q_{52}=0,\qquad q_{32}=q_{41}=q_{43}=q_{63}=1,\\
q_{60}=q_{20}+q_{40},\qquad
q_{84}=q_{22}+q_{42}+q_{62}+q_{82}.
\end{gathered}
\]

All unmentioned allowed coefficients are fixed by these rows. The canonical
support-pair bank has length 85,504 bytes and SHA-256

    0b2c14602c487418d57adff7d542ae5a3e94e431ad0466b8d25e5c2fffaa701c

### 4.3 Rigidity proof

For any normalized binary pair, the \(xy\)-coefficient of the half-Jacobian
error is

\[
[xy]E_F=p_{10}q_{12}+p_{21}q_{01}+p_{01}q_{21}\pmod2.
\]

A contribution to \(xy\) must come from exponent pairs summing to \((2,2)\).
The displayed pairs contribute determinant \(2\) modulo \(4\); pure quadratic
pairs contribute multiples of \(4\), while the \((xy,xy)\) determinant is zero.

The exact Keller-collision classification forces \(q_{12}=0\); equivalently,
the \((2,2)\) bracket row after substituting the four classified \(P\)'s forces
it. Since \(p_{10}=q_{01}=p_{21}=1\) and \(p_{01}=0\),

\[
[xy]E_F=1.
\]

Thus \(xy\,dx\wedge dy\) survives Cartier for every one of the 1,152 maps.
None lifts modulo \(4\), even with arbitrary new correction monomials and
moving collision points. This proves **NEVER-VANISHES-PROVED** for the
registered stratum.

There are five full odd–odd support patterns, with multiplicities
\(256,256,256,256,128\); every pattern contains \((1,1)\).

### 4.4 Exact generic degrees and the odd guard

For each datum the engine computes exactly

\[
\dim_{\mathbf F_2(U,V)}
\frac{\mathbf F_2(U,V)[x,y]}{(P-U,Q-V)}.
\]

This is the generic degree; it is not inferred from finite-field fiber samples.

| degree | 3 | 6 | 7 | 8 | 10 | 11 | 12 | 14 | 15 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 1 | 3 | 1 | 9 | 29 | 2 | 49 | 84 | 4 | 70 | 171 | 126 | 271 | 16 | 166 | 6 | 136 | 8 |

Exactly eight degrees are odd:

\[
3,7,11,11,15,15,15,15.
\]

All have \(P=P_M\). Their complete \(Q\)-support bank is:

| degree | \(\operatorname{supp}Q\), with \(ij=x^iy^j\) |
|---:|---|
| 3 | \(01,50,61,72,83\) |
| 15 | \(01,20,50,60,61,72,83\) |
| 15 | \(01,40,50,60,61,72,83\) |
| 11 | \(01,20,40,50,61,72,83\) |
| 7 | \(01,30,41,50,60,61,72,82,83\) |
| 15 | \(01,20,30,41,50,61,72,82,83\) |
| 15 | \(01,30,40,41,50,61,72,82,83\) |
| 11 | \(01,20,30,40,41,50,60,61,72,82,83\) |

The canonical odd bank has length 416 bytes and SHA-256

    9bf54d4677b31e29ebf8ae4e22ea3b19eca6193788f6ca1f2eeb1f6b6de3c9ba

The first four have odd–odd support
\(\{(1,1),(7,1),(9,3)\}\); the last four additionally have \((5,1)\).
The odd-degree guard therefore produces no vanishing lead.

## 5. Relaxed-hull vanishing controls — flagged

**VANISHING FOUND OUTSIDE THE REGISTERED STRATUM: 48 DATA.**

Drop the exact core-vertex requirements and the shell, but retain constant zero,
linear jet \(I_2\), and the marked collision. Inside the two base hulls:

| item | count |
|---|---:|
| collision-compatible \(P\)-masks | 64 |
| collision-compatible \(Q\)-masks | 8,192 |
| pairs screened | 524,288 |
| Keller collisions | 288 |
| Cartier nonzero | 240 |
| Cartier zero | **48** |

All 48 have even exact generic degree, with histogram

\[
\{4:16,\ 8:17,\ 10:4,\ 12:1,\ 14:6,\ 16:4\}.
\]

They lose at least one registered core vertex; many show Frobenius or
Artin–Schreier mechanisms such as \(P=x+x^2\) or \(P=x+x^4\). Nevertheless,
each is a genuine first-stage unrestricted lift, so they are not hidden. The
engine constructs \(A,B\) and moving marked-point lifts for all of them.

For example,

\[
P=x+x^2,\qquad Q=y+x^2+x^4y^2
\]

has (E=x+x^4y), empty odd–odd support, and the engine constructs
(A=x^5y, B=xy).  Modulo (4), the lifted points
((0,1),(3,0),(1,1)) have common image ((0,1)).

The canonical 48-record bank has length 1,664 bytes and SHA-256

    56ff42dc4080e1e257c8ad800db29392835eb059a7277e6da372752619382e6e

Print the complete bank and witnesses with

    python3 cases/witt_check.py relaxed --degrees --json-vanishing

Only four also vanish in the stricter diagnostic that locks the normalized
coefficient positions, confines corrections to the same hulls, and freezes the
displayed source points. That count is a pinned finite-slice fact, not the
geometric unrestricted obstruction.

These 48 are low-priority disproof leads, not counterexamples. They fail the
registered vertex and odd-degree guards; no \(W_3\), coherent all-level, or
characteristic-zero lift is claimed.

## 6. What vanishing would and would not prove

A vanishing \(o_2(F)\) gives a \(\mathbf Z/4\) Keller lift and, by étaleness, a
lift of the marked collision. To obtain a characteristic-zero counterexample
candidate one would still need:

1. compatible choices through every \(\mathbf Z/2^n\) level;
2. one fixed finite coefficient support, or another proof that the inverse limit
   is polynomial rather than a formal power series;
3. an exact determinant-one map over \(\mathbf Z_2\) with distinct colliding
   points;
4. descent of the finitely many coefficients and points to a finitely generated
   characteristic-zero field, followed by an embedding into \(\mathbf C\).

Only then would the generic-fiber polynomial map be a characteristic-zero plane
counterexample. One vanishing \(W_2\) class proves none of the later steps.
Neither do unrelated solutions at every finite precision, growing supports, or
a numerical 2-adic point. Conversely, nonvanishing rules out this unramified
\(W_2/\mathbf Z_2\) lane; it does not rule out every ramified
mixed-characteristic deformation.

## 7. Reproduction

    python3 -m py_compile cases/witt_check.py
    python3 cases/witt_check.py self-test
    python3 cases/witt_check.py search --degrees
    python3 cases/witt_check.py relaxed --degrees
    python3 cases/witt_check.py audit-3d

The self-test asserts Mondello's exact odd–odd support, the 1,152/0 primary
census, the 240/48 relaxed census, the four pinned finite-support controls, and
the explicit 3D lift.

The engine uses no floating point or random sampling. It forms the integer
Jacobian before exact division by two, performs bit-exact linear algebra,
verifies constructed corrections in the untouched determinant, and uses
Singular only for exact Gröbner-basis generic degrees over
\(\mathbf F_2(U,V)\).

## 8. Literature and scope

This class is an integral de Rham Bockstein specialized to the determinant
equation. It is related to Cartier and Witt lifting, but is not the same
construction as the de Rham–Witt “Witt-Jacobian” for algebraic-independence
testing by
[Mittmann–Saxena–Scheiblechner](https://arxiv.org/abs/1202.4301).
General de Rham–Witt context is due to
[Illusie](https://numdam.org/articles/10.24033/asens.1374/).
Positive-characteristic Jacobian formulations and their relationship to
characteristic zero are discussed by
[Maubach–Rauf](https://arxiv.org/abs/1507.02946).

The odd-degree filter matches
[Adjamagbo's prime-to-characteristic separable formulation](https://doi.org/10.1007/978-94-015-8555-2_5),
but the result here is only a finite-stratum lifting rigidity theorem. It does
not say that every characteristic-two Keller collision has nonzero obstruction
and does not settle JC2.

## Final verdict

**NEVER-VANISHES-PROVED** for the precisely registered two-variable
Mondello-hull-plus-one-shell stratum: 1,152 of 1,152 obstruction classes are
nonzero, including all eight odd-degree data. The forced identity
\([xy]E_F=1\), backed by the complete exact classification, is the proof.

The requested lane is closed on its registered tractable stratum. The 48
relaxed, even-degree \(W_2\)-vanishing controls are explicitly banked as
out-of-stratum first-order leads and are not promoted beyond that status.
