# K00 higher-valuation contraction and nearest \(r=2\) preflight

**Date:** 2026-08-29  
**Status:** sealed read-only analysis; no canonical promotion  
**Frozen basis:** `93db`  
**Scope:** honest K00 source jets on the licensed \(C_6=1\) chart, through \(\Lambda^{19}\)  
**Excluded scope:** `jc2-lean`, Lean formalization, convergence, algebraization, and unlicensed support changes

## 1. Result

Let

\[
r:=\min_{0\le i\le5}\operatorname{ord}_{\Lambda}(d_i).
\]

For the exact source client specified below:

1. the normalized valuation-one branch \(r=1\) is empty on its actual source open by the bound grade-5 result;
2. no honest source-typed \(19\)-jet exists with \(r\ge7\);
3. therefore the only integer valuations not yet excluded are

   \[
   \boxed{r=2,3,4,5,6};
   \]

4. in the nearest inherited \(r=2\) lane, with leading vector in the old plane, the branch with zero \(\Lambda^3\)-coefficient already fails at grade \(8\);
5. consequently any surviving old-plane \(r=2\) reseed must carry a nonzero odd correction at \(\Lambda^3\). A smallest exact grade-7 preflight for that necessary sublane is given in Section 7.

Items 1 and 2 are exclusion theorems. Item 3 is only a list of valuations still open, not an existence statement.

## 2. Licensed normalization and source type

The normalization is

\[
\begin{aligned}
C_0&=(1+d_0)/256, & C_1&=d_1, & C_2&=(1+d_2)/16,\\
C_3&=d_3, & C_4&=(3+d_4)/8, & C_5&=d_5,\\
C_6&=1.
\end{aligned}
\]

The seven honest rows are

\[
\Phi_\ell=
R_\ell\!\left(C,\Lambda^2k_{10},\Lambda^6k_6,\Lambda^{10}k_2\right)
-\Lambda^{12+\ell}\delta_\ell,
\qquad 1\le\ell\le7,
\]

where

\[
(\delta_1,\ldots,\delta_7)
=(0,\mu_2,0,\mu_4,0,\mu_6,J_{\det}/4).
\]

An honest jet through \(\Lambda^{19}\) retains

\[
\begin{aligned}
d_i&=\sum_{n=1}^{19}d_{i,n}\Lambda^n,\\
k_{10}&=\sum_{n=0}^{17}k_{10,n}\Lambda^n,
&\kappa:=k_{10,0}&\ne0,\\
k_6&=\sum_{n=0}^{13}k_{6,n}\Lambda^n,
&k_{6,0}&=0,\\
k_2&=\sum_{n=0}^{9}k_{2,n}\Lambda^n,
&k_{2,0}&=0,\\
\mu_2&=\sum_{n=0}^{5}\mu_{2,n}\Lambda^n,
&\mu_{2,0}&=0,\\
\mu_4&=\sum_{n=0}^{3}\mu_{4,n}\Lambda^n,
&\mu_{4,0}&=0,\\
\mu_6&=\sum_{n=0}^{1}\mu_{6,n}\Lambda^n,
&\mu_{6,0}&=0,\\
J_{\det}&=J_0,
&J_0&\ne0.
\end{aligned}
\]

Thus

\[
\operatorname{ord}_\Lambda k_{10}=0,
\qquad
\operatorname{ord}_\Lambda k_6,
\operatorname{ord}_\Lambda k_2,
\operatorname{ord}_\Lambda\mu_2,
\operatorname{ord}_\Lambda\mu_4,
\operatorname{ord}_\Lambda\mu_6\ge1.
\]

Neither \(\kappa\) nor \(J_0\) is normalized to \(1\). Such a normalization would require a separately licensed and replayed group action.

For exact valuation \(r\), impose \(d_{i,n}=0\) for all \(n<r\), put

\[
x_i=d_{i,r},
\]

and retain the open condition \(x\ne0\) as the six named charts

\[
D(x_0)\cup\cdots\cup D(x_5).
\]

It is not legitimate to set a selected \(x_i=1\) without an additional licensed action. Nor may one replace \(\Lambda\) by \(\Lambda^r\): the external shifts \(2,6,10\) and the terminal grade \(19\) do not rescale with that substitution.

## 3. Exact contracted identity and degree census

Let \(\mathfrak m=(d_0,\ldots,d_5)\). The promoted exact contraction is

\[
\begin{aligned}
R_{\mathrm{mix}}
&=h\Phi_7-\sum_{i=1}^{6}u_i\Phi_i\\
&=\Lambda^2k_{10}D_{K10}
  +\Lambda^6k_6D_{K6}
  +\Lambda^{10}k_2D_{K2}\\
&\quad+\Lambda^{14}u_2\mu_2
  +\Lambda^{16}u_4\mu_4
  +\Lambda^{18}u_6\mu_6
  -\Lambda^{19}hJ_{\det}/4,
\end{aligned}
\]

with

\[
h=20+63d_4.
\]

The exact collected census from the frozen `K_VECTOR.txt` is:

| polynomial | number of terms | minimum \(d\)-degree |
|---|---:|---:|
| \(D_{K10}\) | 79 | 3 |
| \(D_{K6}\) | 41 | 2 |
| \(D_{K2}\) | 16 | 2 |
| \(u_2\) | 7 | 1 |
| \(u_4\) | 4 | 1 |
| \(u_6\) | 2 | 1 |
| \(-h/4=-5-(63/4)d_4\) | 2 | 0 |

Equivalently,

\[
D_{K10}\in\mathfrak m^3,
\qquad
D_{K6},D_{K2}\in\mathfrak m^2,
\qquad
u_2,u_4,u_6\in\mathfrak m.
\]

The frozen contraction contains no omitted bilinear load-coordinate term.

The SHA-256 seal of the exact source artifact is

```text
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a  K_VECTOR.txt
```

The corresponding contracted target is sealed by

```text
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c  CONTRACTED_TARGET.txt
```

## 4. The \(r\ge7\) exclusion theorem

**Theorem.** Over the rational source base, no honest jet satisfying all seven rows modulo \(\Lambda^{20}\) can have

\[
\min_i\operatorname{ord}_\Lambda(d_i)\ge7.
\]

**Proof.** Suppose every \(d_i\) has order at least \(r\). The six positive terms in the contracted identity have the respective lower bounds

\[
\begin{array}{c|c}
\text{term} & \text{lower bound on its }\Lambda\text{-order}\\
\hline
\Lambda^2k_{10}D_{K10} & 2+3r\\
\Lambda^6k_6D_{K6} & 7+2r\\
\Lambda^{10}k_2D_{K2} & 11+2r\\
\Lambda^{14}u_2\mu_2 & 15+r\\
\Lambda^{16}u_4\mu_4 & 17+r\\
\Lambda^{18}u_6\mu_6 & 19+r.
\end{array}
\]

For \(r\ge7\), every displayed bound is strictly greater than \(19\). In the terminal term, the nonconstant part of \(h\) also has order at least \(r\), so

\[
[\Lambda^{19}]\left(-\Lambda^{19}hJ_{\det}/4\right)
=-5J_0.
\]

Consequently

\[
[\Lambda^{19}]R_{\mathrm{mix}}=-5J_0.
\]

If all \(\Phi_i\) vanish modulo \(\Lambda^{20}\), the left side must vanish. This would give \(5J_0=0\), impossible because \(5\) and \(J_0\) are units. \(\square\)

The same argument covers \(d=0\), with valuation interpreted as \(+\infty\).

## 5. Independent raw odd-row check for \(r\ge10\)

The uncontracted linear \(K_6\) sector in rows \(1,3,5,7\) is

\[
\left(\frac34,-\frac3{32},-\frac3{512},-\frac3{4096}\right)\mathscr L,
\qquad
\mathscr L=d_1-\frac14d_3+\frac1{16}d_5.
\]

Put

\[
p_6=\Lambda^6k_6,
\qquad
\theta=[\Lambda^{19}](p_6\mathscr L).
\]

If \(r\ge10\), then through grade \(19\):

- the unloaded rows vanish because their minimum \(d\)-degree is \(2\);
- the \(K_{10}\) contribution vanishes by shift \(2\) plus minimum \(d\)-degree \(2\);
- the \(K_2\) contribution vanishes because \(\operatorname{ord}(\Lambda^{10}k_2)\ge11\) and its minimum \(d\)-degree is \(1\);
- the nonlinear \(K_6\) contribution vanishes because \(\operatorname{ord}p_6\ge7\) and its minimum \(d\)-degree is \(2\).

Rows \(1,3,5\) have zero source target. Row \(7\) has the target term \(-\Lambda^{19}J_0/4\). Grade \(19\) in row \(1\) therefore gives

\[
\frac34\theta=0,
\]

whereas row \(7\) gives

\[
-\frac3{4096}\theta-\frac14J_0=0.
\]

Thus \(J_0=0\), contradicting the source open. The row indices, shifts, and sign are independent checks on the stronger contracted theorem. The even linear form present in row \(2\) is irrelevant, and there is no missed odd source target: only row \(7\) has one.

## 6. Combination with the valuation-one closure

On the normalized valuation-one branch, the retained leading vector is

\[
\ell(s,t)=(2s,t/8,s,t,s,2t).
\]

The bound grade-5 equations force \(s=t=0\). The bare affine grade-5 ideal remains proper because it contains the origin, but that origin is not a valuation-one point: the actual source open is

\[
D(s)\cup D(t).
\]

Hence the correct point-set conclusion is:

\[
r=1\text{ is excluded},
\qquad
r\ge7\text{ is excluded},
\]

and only

\[
\boxed{r=2,3,4,5,6}
\]

remain open in this exact \(C_6=1\), \(k_{10,0}\ne0\), fixed-boundary source client.

A different support with \(k_{6,0}\) or \(k_{2,0}\) a unit is not a branch of this client. Here

\[
k_{6,0}=k_{2,0}=0,
\qquad
k_{10,0}\ne0.
\]

Changing that support requires a separate source/admissibility theorem; it cannot be inferred by relabeling the present variables.

## 7. Exact grade-8 kill of the even old-plane \(r=2\) reseed

Consider the nearest inherited higher-valuation ansatz

\[
d=\Lambda^2\ell(s,t)+\Lambda^3y+\Lambda^4z+O(\Lambda^5),
\qquad
(s,t)\ne(0,0).
\]

Set \(y=0\), leaving \(z\) arbitrary. Define

\[
a(s,t)=(s^2,st/8,16t^2,0,0,0),
\qquad
w=z-a(s,t),
\]

and

\[
A=16w_1-4w_3+w_5,
\qquad
B=w_0-4w_2+2w_4.
\]

After the coefficients that provably do not enter grade \(8\) are removed, the exact rows have the form

\[
E_i=Q_i(w)+\kappa\mathcal L_i(s,t,z).
\]

The frozen quadratic identities are

\[
Q_1(w)+8Q_3(w)=\frac3{2048}AB,
\]

and

\[
Q_4(w)=\frac3{524288}(B^2-64A^2).
\]

The corresponding exact load identities are

\[
\mathcal L_1+8\mathcal L_3=0,
\qquad
\mathcal L_4=0.
\]

Therefore \(E_1+8E_3=E_4=0\) gives

\[
AB=0,
\qquad
B^2-64A^2=0.
\]

In characteristic zero this forces \(A=B=0\). On this locus every \(Q_i(w)\) vanishes, and two remaining rows reduce exactly to

\[
E_1=\frac{5\kappa}{4096}\,t(3s^2-64t^2),
\]

\[
E_2=\frac{5\kappa}{65536}\,s(s^2-192t^2).
\]

These have no common zero on

\[
D(\kappa)\cap(D(s)\cup D(t)).
\]

Indeed, if \(t=0\), the second equation forces \(s=0\). If \(t\ne0\), the first equation forces \(s\ne0\) and \(s^2=(64/3)t^2\), while the second forces \(s^2=192t^2\), a contradiction.

Thus:

> No old-plane valuation-two source jet with \(d_{*,3}=0\) extends through grade \(8\), regardless of the arbitrary coefficient \(d_{*,4}=z\).

Higher \(d\)-coefficients and higher \(k_{10}\)-coefficients either do not enter this grade or multiply identities already zero; the other source loads begin too late. This is a finite-jet exclusion, not an exclusion of every \(r=2\) leading support.

The coefficient extraction behind the displayed identities used exact rational arithmetic on the frozen 25 KB tails, completing in under \(0.1\) seconds with approximately 11 MB RSS. No local algebra decomposition or heavy CAS was used.

## 8. Smallest exact preflight for the necessary odd \(r=2\) lane

The nearest unresolved old-plane lane must retain

\[
d=\Lambda^2\ell(s,t)+\Lambda^3y+\Lambda^4z+O(\Lambda^5),
\]

with

\[
(s,t)\ne(0,0),
\qquad
y\ne0,
\qquad
\kappa\ne0,
\qquad
J_0\ne0.
\]

Retain \(k_{10}=\kappa+O(\Lambda)\). Through grade \(7\), the displayed equations do not require a nonconstant \(k_{10}\)-coefficient: the possible \(k_{10,1}\)-term multiplies \(M_4(\ell)=0\). The \(k_6,k_2,\mu_2,\mu_4,\mu_6\), and determinant targets enter too late to alter these rows, although their boundary conditions remain part of the source type.

Write \(Q=(Q_1,\ldots,Q_7)\) for the unloaded quadratic row vector, \(c_3\) for its pure cubic part, and \(M_4\) for the homogeneous quadratic coefficient of the leading \(k_{10}\)-load. The coefficient equations are:

### Grade 4

\[
Q(\ell)=0.
\]

### Grade 5

\[
DQ(\ell)[y]=0.
\]

On the reviewed plane this is identically zero.

### Grade 6

\[
DQ(\ell)[z]+Q(y)+c_3(\ell)+\kappa M_4(\ell)=0.
\]

The three terms other than \(Q(y)\) vanish on the plane, so grade \(6\) is exactly

\[
Q(y)=0.
\]

Its reduced point-set locus is

\[
16y_1-4y_3+y_5=0,
\qquad
y_0-4y_2+2y_4=0.
\]

For a scheme-sensitive computation one should retain the original seven equations \(Q_i(y)\); replacing them by the radical is justified only for the reduced point-set preflight.

### Grade 7

The new coefficient \(d_{*,5}\) appears only through \(DQ(\ell)[d_{*,5}]\), hence vanishes. Likewise \(k_{10,1}M_4(\ell)=0\). The exact grade-7 system is therefore the affine-linear system in \(z\)

\[
DQ(y)[z]
+Dc_3(\ell)[y]
+\kappa\,DM_4(\ell)[y]=0.
\]

The matrix \(DQ(y)\) contains a fixed two-dimensional right kernel and has the fixed left-kernel covectors

\[
\left(\frac3{128},0,\frac18,0,1,0,0\right),
\]

\[
(0,0,0,0,0,1,0),
\]

and

\[
\left(\frac1{512},0,\frac1{128},0,0,0,1\right).
\]

Their contractions with the grade-7 right-hand side vanish identically. This removes the three generic cokernel conditions, but it does not settle the strata on which \(DQ(y)\) drops rank and acquires additional left-kernel vectors.

### Preflight decision

The smallest exact computation is therefore:

1. retain the seven equations \(Q_i(y)=0\);
2. impose the seven affine-linear grade-7 equations in \(z\);
3. split by the exact minors/Fitting ideals of \(DQ(y)\);
4. test the source charts

   \[
   D(\kappa J_0)\cap D(s),
   \qquad
   D(\kappa J_0)\cap D(t),
   \]

   together with the six named opens \(D(y_j)\).

This is a small exact rank computation, not a request for a large Gröbner decomposition. If every chart is empty, it excludes this old-plane \(r=2\) sublane through grade \(7\). If a chart is nonempty, it produces only a compatible \(7\)-jet; it must still be extended coefficientwise through grade \(19\) before it can challenge the contraction client.

The full, non-plane \(r=2\) lane begins instead with

\[
d=\Lambda^2x+\Lambda^3y+\cdots,
\qquad
x\ne0,
\]

and the unsimplified leading conditions

\[
Q(x)=0,
\qquad
DQ(x)[y]=0.
\]

The plane preflight above does not exclude other components of this quadratic leading cone.

## 9. Jets, formal arcs, and maps

An honest \(19\)-jet here is a finite coefficient tuple satisfying

\[
\Phi_i\equiv0\pmod{\Lambda^{20}}
\qquad(1\le i\le7)
\]

with the displayed source boundary and unit conditions.

A formal arc of the same source type would truncate to such a jet. Hence the \(r\ge7\) finite-jet theorem also excludes formal arcs of that type and valuation.

The converse direction is unavailable: a compatible finite jet need not extend to an infinite formal arc. Nor does any statement here produce a convergent arc, an algebraization, or a polynomial Keller map. Those require separate extension and source-to-map theorems.

## 10. Custody seals

The analysis was checked against the following frozen artifacts and reports:

```text
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a  K_VECTOR.txt
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c  CONTRACTED_TARGET.txt
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  frozen tails.json
c37cdc4ff4e652eeaf57932b7bfc25caae503d94f100fb9d47ac2460e272b08a  V20 hostile review
f834cb99afb5c7c1820c64c92825c274c8451633d860d5268f47556463e8309b  V22 hostile review
fbe5b580662b7f77326c61f5fec54b3a9a2059f1684f52994fee8652efc49448  grade-4 integration
8d4d270c70224223bbeae6a6e5285fe99303bdb73157e64e0ac3d31d5d832da9  grade-5 structural report
7e9e591672a9f1a6b1e8b5bc56053947fa3a665b8541d91e20d90894e465f546  grade-5 binding integration
f602fb81b6e90272462b2263eaeb0eb40550b7d4ce1b87d0e9916bb45322c10b  newest synthesis
```

This report adds no canonical claim beyond the displayed, source-qualified conclusions. It was banked without editing any existing canonical overlay and without inspecting, listing, status-checking, or modifying `jc2-lean` or any Lean file.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14379`.
- Body SHA-256:
  `efec8e4e94315afee74dc47f2658fccd9be1d99c078dadbc61f3f88b25235cf3`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
