# max11 68 q=0 vanishing-A chamber: elimination count

**Verdict: PARTIAL**

After matching through \(k=3\), the unused landed constraints on the
remainder coordinates do not empty the chamber and do not cut it down to
finite dimension independent of \(m\). The naive independent count is
\[
(\#\text{unknowns})-(\#\text{constraints})=19m+4,
\]
strictly positive and linear in \(m\). There is a triangular elimination
of the *high* remainder coefficients \((s,r_c,r_e)\) in terms of
\((B,d,\lambda,\gamma,\varepsilon)\), with nonzero leading coefficient
\(\frac43\lambda B_D^2\) on \(r_c\) at each unused \(\Delta\)-jet, but
the triangulation does not reach a final relation colliding with
\(Fce_0\neq 0\) or with an exact top coefficient. The compensated-\(I3\)
family is dependent on \(\Delta\) and \((\ast)\) at the first unused
order (and is related to both by a universal syzygy), so it does not
flip the count.

No exit-price is claimed.

---

## 0. Sources and verification status

Work over an algebraically closed field \(k\) of characteristic zero, on
the wall \(9N=7S\). Write \(N=7m\) with \(m\ge 1\), so \(S=9m\).

Clone used for reading: `https://github.com/dcposch/jc2-lean` at
`a2507ec` (`origin/master` as of this run). Nested worktree `jc2-lean/`
is sandbox-blocked.

### 0.1 What was read

| File / theorem | Used for |
|---|---|
| `Grok68QZeroVanishingAJetScratch.lean` (SHA `b567d6987263468f206347bbd74f16d3605ac3febec40f53aed92e97ec410e17`) | landed matching \(k=1,2,3\); residual `...VanishingAJetResidual68`; \(Fce_0\neq 0\) |
| `xmodel/max11-68-vanishing-a-uniform-induction-grok46-20260831.md` | matching recurrence, remainder form, unused \(\Delta_{U-4}\), top of \(J\) |
| `...QZeroDiscriminantNextScratch.lean`, `...DiscriminantNextTwoScratch.lean`, `...JetThirdSourceScratch.lean` | \(\Delta_{U-k}=0\) from `hzero` on \(1\le k\le\min(S,7N-2G-S)=4m\) |
| `...QZeroTopResultantScratch.lean`, `...TopNextScratch.lean`, `...I4NextTwoScratch.lean` | I4 top, jets \(k=1,2\); \(Fce=C(Fce_0)\) via `hFce` |
| `...QZeroI3NextScratch.lean`, `...I3NextTwoScratch.lean` | compensated \(I3\) degree drop \(\deg Rce\le 2D\); second jet marked dependent |
| `...QZeroFceZeroGlobalScratch.lean` | universal syzygy `Fce_Rce_Delta_descent_algebra68`; `hRce` type |
| `...QZeroFceZeroHDegreeScratch.lean` | universal syzygy `Fce_J_Delta_H_algebra68`; \(H=4B^2c+9d^2\) |
| `...QZeroCompanionNextScratch.lean` | \(J.\mathrm{natDegree}\le p\) from the post-epsilon state |
| `...QZeroCompanionThirdReductionScratch.lean` | producing split; load of companions into disc\(+\)I4 jets |

Index conventions as in the induction report, using \(G=2S\) at every
`rw [hGS]` site. Defining theorem of `hGS` not opened (imported support
file absent from `origin/master`). UNVERIFIED as a standalone
declaration; used as \(G=2S\).

### 0.2 What was not read

- `Sol68...QZeroCompanionScratch.lean`, the file that *defines*
  `fiveToSix_..._qZero_next68` / `QZeroNextScalar68`: **not on
  `origin/master`** (HTTP 404). The identities \(Fce=\tfrac38 C(i_4)\)
  and \(\deg Rce\le 2D\) are read from every consumer; the exact formula
  \(Rce=\tfrac34\gamma\,B^2+\tfrac98 C(i_3)\) is inferred from
  `Fce_zero_global68`, which returns the unpacked `hRce` at that type.
  Marked UNVERIFIED as a Lean declaration of `next68`; used below as
  reconstructed from typing.
- Packet definition files
  (`SupportRowOnePacket68`, `ContractedCuspPacket68`,
  `PostEpsilonState68`, `fiveToSixCuspDiscriminantPolynomial68`):
  not on `origin/master`. Discriminant expansions and `hzero` window
  taken from the named jet theorems and from the induction report §0.
- Full text of `FullRowZero` / `FullRowTwo` / remainder \(W_0,W_2\).
  Companions \(k=1,2,3\) are consumed; companions \(k\ge 4\) are **not**
  counted as extra independent constraints, because the landed load
  algebra for \(k=1,2,3\) places those companions in the localized ideal
  of disc and I4 jets (see §6). UNVERIFIED that this continues.

### 0.3 Notation

\[
p=2N=14m,\quad
D=3m,\quad
Cc=10m,\quad
V=8m,\quad
E=15m,\quad
U=20m,\quad
K=D+E=18m.
\]
Packet tops \(A_p\neq 0\), \(B_D\neq 0\), \(c_{Cc}\neq 0\), \(d_V\neq 0\),
\(e_E\neq 0\). Write \(\lambda:=c_{Cc}/B_D\neq 0\), so the cusp top is
\(A_p=-3\lambda^2\) and the quadratic resultant is
\(4\lambda B_D^3+9d_V^2=0\).

Residual after matching through \(k=3\), as packaged in
`...VanishingAJetResidual68` and rewritten in the induction report §3.4:

\[
A=A_p X^p+s,\quad \deg s\le 14m-4,
\]
\[
c=\lambda X^N B+r_c,\quad \deg r_c\le 10m-4,
\]
\[
e=-\lambda X^N d+r_e,\quad \deg r_e\le 15m-4,
\]
with \(Fce=C(Fce_0)\) and \(Fce_0\neq 0\). Degrees of \(s,r_c,r_e\) are
upper bounds (three vanished coefficients), not exact.

Compensated I4 and I3:

\begin{align*}
Fce&=(Be+cd)-\tfrac19 B^3+\tfrac32\gamma\,d+\tfrac34\varepsilon\,B,\\
Rce&=-ABd+3ce-B^2c+\tfrac32 d^2+\tfrac92\gamma\,e+\tfrac94\varepsilon\,c,\\
\Delta&=AB^2+3c^2,\\
J&=Bc^2-\tfrac19 AB^3-3de,\\
H&=4B^2c+9d^2.
\end{align*}

On the wall, `next68` gives \(Fce=\tfrac38 C(i_4)\). Discriminant jets:
\((\Delta.\mathrm{reflect}\,U)_i=0\) for \(1\le i\le 4m\), equivalently
\(\Delta_{U-k}=0\) for \(k=1,\ldots,4m\), together with the cusp
\(\Delta_U=0\).

---

## 1. Remainder form of the three polynomial identities

Substitute the matching into \(\Delta\), \(Be+cd\), and \(J\).

### 1.1 Discriminant

\[
\Delta=s B^2+6\lambda X^N B r_c+3 r_c^2.
\]
The \(A_p X^p B^2\) and \(3\lambda^2 X^{2N}B^2\) terms cancel by
\(A_p=-3\lambda^2\). Degree check:
\(\deg(sB^2)\le 20m-4\), \(\deg(X^N B r_c)\le 20m-4\),
\(\deg(r_c^2)\le 20m-8\). So \(\deg\Delta\le U-4\), which is the matching
through \(k=3\). The unused jets are the coefficients
\[
\Delta_{U-k}=0\qquad\text{for }k=4,\ldots,4m,
\]
i.e. degrees \(16m,\ldots,20m-4\): **\(4m-3\) equations**.

At \(k=4\), \(r_c^2\) does not reach degree \(U-4\), and
\[
\Delta_{U-4}=s_{p-4}B_D^2+6\lambda B_D(r_c)_{Cc-4}=0,
\]
hence \(A_{p-4}B_D+6\lambda(r_c)_{Cc-4}=0\), as in the induction
report §3.4. For \(4\le k\le 4m\) the same leading pair appears:
\[
\Delta_{U-k}=B_D^2 s_{p-k}+6\lambda B_D(r_c)_{Cc-k}+Q_k=0,
\]
where \(Q_k\) is inhomogeneous in previously pinned higher remainder
coefficients, in lower coefficients of \(B\), and (for \(k\ge 8\)) in
\(r_c^2\). One linear constraint on the new pair
\((s_{p-k},(r_c)_{Cc-k})\), not a kill.

### 1.2 I4 identity \((\ast)\)

Matching gives \(Be+cd=B r_e+r_c d\), so
\begin{equation}
B r_e+r_c d=\tfrac19 B^3-\tfrac32\gamma\,d-\tfrac34\varepsilon\,B+C(Fce_0).\tag{\(\ast\)}
\end{equation}
This is \(Fce=C(Fce_0)\) in remainder coordinates, a landed identity on
the whole wall.

**Degree-by-degree content of \((\ast)\).** After matching,
\(\deg(B r_e)\le 18m-4\) and \(\deg(r_c d)\le 18m-4\), so the left side
lives in degrees \(0,\ldots,18m-4\). The four I4 jets at degrees
\(18m,18m-1,18m-2,18m-3\) are exactly matching \(k=0,1,2,3\); they lie
*above* this range and are not residual constraints.

The right side has exact degree \(9m\) (leading \(\tfrac19 B_D^3\neq 0\)).
Coefficient-wise on degrees \(0,\ldots,18m-4\):

| degrees | content | # |
|---|---|---|
| \(9m+1,\ldots,18m-4\) | LHS \(=0\) (right side too short) | \(9m-4\) |
| \(9m\) | LHS \(=\tfrac19 B_D^3\) | \(1\) |
| \(1,\ldots,9m-1\) | LHS \(=\) compensated right side | \(9m-1\) |
| \(0\) | defines \(Fce_0\) (open condition \(Fce_0\neq 0\)) | \(1\) |

Total **\(18m-3\)** equations, equal to the number of coefficients of a
polynomial of degree \(\le 18m-4\). None of these \(18m-3\) is automatic
from matching \(k=0,1,2,3\).

Triangular reading: \(B r_e=P\) with
\(P:=\) RHS \(-r_c d\). The unknown \(r_e\) (degree \(\le 15m-4\),
\(15m-3\) coefficients) is uniquely determined iff \(B\) divides \(P\).
That divisibility is **\(3m\)** remainder coefficients (degrees
\(0,\ldots,3m-1\) of \(P\bmod B\)). Equivalently, from the top: for
\(k=4,\ldots,15m\), the coefficient \((\ast)_{18m-k}\) pins
\((r_e)_{E-k}\); the leftover degrees \(0,\ldots,3m-1\) are the
divisibility conditions. At \(k=4\), only the new tops survive:
\[
B_D(r_e)_{E-4}+(r_c)_{Cc-4}d_V=0.
\]

### 1.3 Jacobian degree bound

\(J.\mathrm{natDegree}\le p=14m\) is the post-epsilon state, used in
`companion_next68`. Naive degree of \(J\) is \(23m\), so coefficients
\(14m+1,\ldots,23m\) vanish: \(9m\) equations.

Remainder expansion (using \(A_p=-3\lambda^2\)):
\begin{align*}
J&=\tfrac43\lambda^2 X^{14m}B^3+2\lambda X^N B^2 r_c+B r_c^2\\
&\qquad-\tfrac19 s B^3+3\lambda X^N d^2-3d r_e.
\end{align*}
Term degrees: \(X^{14m}B^3\) and \(X^N d^2\) reach \(23m\);
\(X^N B^2 r_c\), \(s B^3\), and \(d r_e\) reach \(23m-4\);
\(B r_c^2\) reaches \(23m-8\).

**Top cancellation, \(k=0\).** As in the induction report §3.3:
\(J_{23m}=\tfrac43\lambda^2 B_D^3+3\lambda d_V^2=0\) by the resultant.
This is consistency, not a residual constraint. Remaining:
**\(9m-1\)** equations (degrees \(14m+1,\ldots,23m-1\)).

**Degrees \(23m-1,23m-2,23m-3\).** Only \(B^3\) and \(d^2\) contribute.
For \(k=1\),
\[
J_{23m-1}=4\lambda^2 B_D^2 B_{D-1}+6\lambda d_V d_{V-1}.
\]
The same combination is \(\frac\lambda3 H_{16m-1}\) (the \(r_c\) terms in
\(H=4\lambda X^N B^3+4B^2 r_c+9d^2\) do not reach \(16m-1\)). Matching
does not relate \(B_{D-1}\) to \(d_{V-1}\), so these three coefficients
are genuine constraints on \((B,d)\), equivalently the first three
subleading coefficients of \(H\). They are not automatic.

**Degree \(23m-4\).** New remainder tops enter; see §3.

### 1.4 Compensated \(I3\), and two universal syzygies

`I3Next` uses \(\deg Rce\le 2D=6m\). Naive degree of \(Rce\) is \(25m\)
(\(-ABd\) and \(3ce\)). After matching those two tops cancel:
\[
(-ABd+3ce)_{25m}=3\lambda^2 B_D d_V-3\lambda^2 B_D d_V=0,
\]
and \(\deg Rce\le 25m-4\). Coefficients \(6m+1,\ldots,25m-4\) vanishing
would be \(19m-4\) equations. The second I3 jet file states explicitly
that its new-variable row “has the same dependence on the second
discriminant and second I4 rows \ldots rather than counted as a new
independent constraint.”

Two algebraic identities, no chamber hypothesis
(`Fce_Rce_Delta_descent_algebra68`, `Fce_J_Delta_H_algebra68`):
\begin{equation}
24 d\,\Delta+\mathrm{Rest}+24 B\bigl(Rce-\tfrac34\gamma B^2-\tfrac98 C(i_3)\bigr)
=(72c+108\gamma)\,Fce,\tag{S1}
\end{equation}
\begin{equation}
BJ=-\tfrac19 B^2\Delta+\tfrac13 c H-\tfrac13 B^3 d+\tfrac92\gamma d^2
+\tfrac94\varepsilon Bd-3d\,Fce,\tag{S2}
\end{equation}
with \(\mathrm{Rest}=16 B^3 c+6\gamma B^3-36 B d^2+81\varepsilon\gamma B
+216\gamma\,cd+162\gamma^2 d+27 i_3 B\).

`Fce_zero_global68` returns the unpacked `hRce` at type
\(Rce=\tfrac34\gamma B^2+\tfrac98 C(i_3)\). That typing is the evidence
that this exact formula is already in `next68`, hence landed on the
*whole* \(q=0\) wall, not only on \(Fce_0=0\). UNVERIFIED as a
declaration of `next68` (file absent); used as reconstructed. On
\(Fce_0=0\), (S1) becomes the \(\Delta\)-descent. On this chamber
\(Fce=C(Fce_0)\neq 0\), so (S1) becomes
\[
24 d\,\Delta+\mathrm{Rest}=(72c+108\gamma)\,C(Fce_0)
\]
*if* the exact \(Rce\) formula holds. Either way, \(I3\) is not a third
independent high-jet family: §3.2 shows the \(k=4\) I3 coefficient
vanishes identically after \(\Delta_{U-4}\) and \((\ast)_{18m-4}\).

---

## 2. Unknowns and constraint census

### 2.1 Free coefficient spaces

The ambient space of the residual, as specified:

| object | bound | # coefficients |
|---|---|---|
| \(s\) | \(\deg\le 14m-4\) | \(14m-3\) |
| \(r_c\) | \(\deg\le 10m-4\) | \(10m-3\) |
| \(r_e\) | \(\deg\le 15m-4\) | \(15m-3\) |
| \(d\) | \(\deg=8m\) exact | \(8m+1\) |
| \(B\) | \(\deg=3m\) exact | \(3m+1\) |
| \(\lambda,\gamma,\varepsilon,Fce_0\) | scalars | \(4\) |

\(A_p=-3\lambda^2\) and \(c_{Cc}=\lambda B_D\) are not extra. \(B_D\) and
\(d_V\) sit in the \(B\) and \(d\) columns. The resultant
\(4\lambda B_D^3+9d_V^2=0\) is consumed at matching \(k=0\), not a
residual equation. Open conditions: \(\lambda\neq 0\), \(B_D\neq 0\),
\(d_V\neq 0\), \(Fce_0\neq 0\).

**Total unknowns: \(50m-3\).**

(If \(i_3\) is counted as an extra scalar for the exact \(I3\) formula,
add \(1\). It is absorbed by degree \(0\) of \(I3\) and does not change
the sign of the count.)

### 2.2 Residual constraint families, after automatic cancellations

| family | residual equations | independent of matching \(k\le 3\)? |
|---|---|---|
| \(\Delta_{U-k}=0\), \(k=4..4m\) | \(4m-3\) | yes |
| \((\ast)\), degrees \(0..18m-4\) | \(18m-3\) | yes |
| \(J_j=0\), \(j=14m+1..23m-1\) | \(9m-1\) | yes (\(J_{23m}\) automatic) |
| \(I3\) / \(\deg Rce\le 6m\) / exact \(Rce\) | — | **no** at high jets; see §3.2 and (S1) |
| cusp top, I4 top, resultant | \(0\) residual | consumed |
| `hzero` below degree \(16m\) | not landed | window ends at \(k=4m\) |
| FullRow companions \(k\ge 4\) | not counted | load algebra, §6 |

**Total counted: \(31m-7\).**

### 2.3 Count as a function of \(m\)

\[
(\#\text{unknowns})-(\#\text{constraints})=(50m-3)-(31m-7)=19m+4.
\]

| \(m\) | unknowns | constraints | difference |
|---|---|---|---|
| \(1\) | \(47\) | \(24\) | \(23\) |
| \(2\) | \(97\) | \(55\) | \(42\) |
| \(3\) | \(147\) | \(86\) | \(61\) |

The difference is strictly positive for every \(m\ge 1\) and grows
linearly. This is a count of polynomial equations versus coefficients,
not a proof that the Jacobian of the map has this rank. It is enough to
rule out emptiness *from these families alone*: even if every counted
equation is independent, a positive-dimensional fibre remains; if some
are dependent, the fibre is larger.

The relations are polynomial, not linear. Section 3 converts the count
into a triangular statement for the high remainders, and shows that the
triangulation does not empty the chamber.

---

## 3. Triangular elimination of high remainders

Proceed from the top, \(k=4,5,\ldots\). At step \(k\) the new remainder
coefficients are \(s_{p-k}\), \((r_c)_{Cc-k}\), \((r_e)_{E-k}\). The
coefficients \(B_{D-k}\) (for \(k\le D=3m\)) and \(d_{V-k}\) (for
\(k\le V=8m\)) belong to the already-counted spaces of \(B\) and \(d\);
they are parameters, not new remainder unknowns.

### 3.1 Leading terms at \(4\le k\le 7\) (before \(r_c^2\) reaches)

Ignoring inhomogeneous terms in already-pinned higher remainders and in
lower \(B\):

\begin{align*}
\Delta_{U-k}&=B_D^2 s_{p-k}+6\lambda B_D(r_c)_{Cc-k}+\cdots,\\
(\ast)_{18m-k}&=B_D(r_e)_{E-k}+(r_c)_{Cc-k}d_V+\cdots,\\
J_{23m-k}&=\tfrac43\lambda^2(B^3)_{9m-k}+2\lambda B_D^2(r_c)_{Cc-k}
-\tfrac19 s_{p-k}B_D^3\\
&\qquad+3\lambda(d^2)_{16m-k}-3 d_V(r_e)_{E-k}+\cdots.
\end{align*}

Solve \(\Delta\) and \((\ast)\) for \(s\) and \(r_e\):
\[
s_{p-k}=-\frac{6\lambda}{B_D}(r_c)_{Cc-k}+\cdots,\qquad
(r_e)_{E-k}=-\frac{d_V}{B_D}(r_c)_{Cc-k}+\cdots.
\]
Diagonals \(B_D^2\neq 0\) and \(B_D\neq 0\). Substitute into \(J\):
\begin{align*}
-\tfrac19 s_{p-k}B_D^3
&=\tfrac23\lambda B_D^2(r_c)_{Cc-k}+\cdots,\\
-3d_V(r_e)_{E-k}
&=\frac{3d_V^2}{B_D}(r_c)_{Cc-k}+\cdots.
\end{align*}
The net coefficient of \((r_c)_{Cc-k}\) in \(J_{23m-k}\) is
\[
2\lambda B_D^2+\tfrac23\lambda B_D^2+\frac{3d_V^2}{B_D}
=\frac{8\lambda}{3}B_D^2+\frac{3d_V^2}{B_D}.
\]
Resultant \(9d_V^2=-4\lambda B_D^3\) gives
\(\frac{3d_V^2}{B_D}=-\frac{4\lambda}{3}B_D^2\), hence
\[
\frac{8\lambda}{3}B_D^2-\frac{4\lambda}{3}B_D^2=\frac{4\lambda}{3}B_D^2\neq 0.
\]
So \(J_{23m-k}\) pins \((r_c)_{Cc-k}\) in terms of \((B,d)\) and
previously pinned data. Then \(\Delta\) pins \(s_{p-k}\) and \((\ast)\)
pins \((r_e)_{E-k}\).

This is the analogue of the matching triangulation, one step further:
three remainder coefficients expressed in the base \((B,d)\), with
nonzero diagonals \(B_D^2\), \(B_D\), \(\frac43\lambda B_D^2\).

For \(k\ge 8\), \(r_c^2\) contributes to \(\Delta_{U-k}\) and
\(J_{23m-k}\), but only through products of *already pinned* higher
\(r_c\). Those terms are inhomogeneous. The leading pair
\((s_{p-k},(r_c)_{Cc-k})\) is unchanged.

The range of unused \(\Delta\)-jets is \(k=4,\ldots,4m\). That pins
\[
s_{10m},\ldots,s_{14m-4}
\quad\text{and}\quad
(r_c)_{6m},\ldots,(r_c)_{10m-4}
\]
(\(4m-3\) coefficients each), together with the corresponding high
\(r_e\). It does **not** constrain the lower coefficients
\(s_0,\ldots,s_{10m-1}\) (\(10m\) of them) or
\((r_c)_0,\ldots,(r_c)_{6m-1}\) (\(6m\) of them), except insofar as later
\(J\) and \((\ast)\) remainder equations see them.

### 3.2 \(I3\) at \(k=4\) is dependent

Remainder form of the uncompensated high part of \(Rce\), after matching:
\[
Rce=-sBd+3\lambda X^N B r_e-3\lambda X^N r_c d+3 r_c r_e+\text{(degree \(\le 16m\))}.
\]
At degree \(25m-4\),
\[
Rce_{25m-4}=-s_{p-4}B_D d_V+3\lambda B_D(r_e)_{E-4}-3\lambda(r_c)_{Cc-4}d_V.
\]
Substitute the \(\Delta\) and \((\ast)\) pins of §3.1:
\[
(-s B_D d_V)+3\lambda B_D r_e-3\lambda r_c d_V
=(6\lambda-3\lambda-3\lambda)d_V(r_c)_{Cc-4}=0.
\]
The first unused I3 coefficient is identically zero on the locus of
\(\Delta_{U-4}\) and \((\ast)_{18m-4}\). This is the concrete content of
the “rank audit” comment on `I3_next_two68`, and of syzygy (S1). \(I3\)
is not a fourth triangular pin and is not added to §2.2.

### 3.3 What the triangulation does *not* do

- It does not pin \(B\) or \(d\). Those remain free parameters of
  dimensions \(3m+1\) and \(8m+1\), subject only to the \(9m-1\) high
  \(J\) equations (of which \(4m-3\) are used pinning \(r_c\), leaving
  \(5m+2\) equations on \((B,d)\) together with lower remainders,
  including the three subleading \(H\)-jets \(J_{23m-1,23m-2,23m-3}\)).
- It does not force \(r_c=0\) or \(r_e=0\). The leftover
  \(\frac43\lambda B_D^2\) pins \(r_c\) *in terms of* \((B,d)\), not to
  zero. The zero-remainder case of \((\ast)\) remains unlanded, as in
  the induction report §3.2.
- After \(k=4m\) the \(\Delta\) window ends. Further \(J\) coefficients
  \(k=4m+1,\ldots,9m-1\) (\(5m-1\) equations, degrees \(14m+1,\ldots,19m-1\))
  each involve a new pair \((s_{p-k},(r_c)_{Cc-k})\) and cannot pin both.
- The \(3m\) low-degree conditions that \(B\) divide the right-hand side
  of \((\ast)\) (degrees \(0,\ldots,3m-1\)) are conditions on
  \((B,d,r_c,\gamma,\varepsilon,Fce_0)\). Degree \(0\) defines \(Fce_0\);
  the remaining \(3m-1\) do not force \(Fce_0=0\). They are
  underdetermined by the same \(19m+4\) margin.

No final pinned relation collides with \(Fce_0\neq 0\) or with
\(B_D^3\neq 0\). The triangulation is a normal form, not an endgame.

### 3.4 Chart \(m=1\)

Here \(D=3=K_{\mathrm{landed}}\) and \(K_\Delta=4\). Phase \(k=4,\ldots,D\)
is empty. The single unused \(\Delta\)-jet \(k=4\) plus \((\ast)_{14}\)
plus \(J_{19}\) pin the single triple
\((s_{10},(r_c)_6,(r_e)_{11})\) in terms of \(B\) (degree \(3\), four
coefficients) and \(d\) (degree \(8\), nine coefficients). Count:
unknowns \(47\), constraints \(1+15+8=24\), difference \(23\). Still
open. Agrees with the induction report §3.4: “Still no `False`.”

---

## 4. Expected dimension after triangulation

A consistent accounting of leftover free coefficients, treating counted
equations as independent:

- High remainders \(k=4..4m\): \(3(4m-3)\) coefficients of
  \((s,r_c,r_e)\) expressed in \((B,d)\). Used: all \(4m-3\) unused
  \(\Delta\)-jets, \(4m-3\) of the \(J\)'s, and \(4m-3\) of the
  \((\ast)\)'s.
- Remaining \((\ast)\): \((18m-3)-(4m-3)=14m\) equations, of which
  \(11m\) pin the remaining \(r_e\) (degrees \(0,\ldots,11m-1\)) and
  \(3m\) are \(B\mid P\).
- Remaining \(J\): \((9m-1)-(4m-3)=5m+2\) equations on lower
  \((s,r_c)\) and on \((B,d)\).
- Unpinned lower \(s\): \(10m\). Unpinned lower \(r_c\): \(6m\).
  \(B\): \(3m+1\). \(d\): \(8m+1\). Scalars: \(4\).
  Subtotal still free before leftover equations:
  \(10m+6m+(3m+1)+(8m+1)+4=27m+6\).
- Leftover equations: \(5m+2\) remaining \(J\), plus \(3m\) from
  \(B\mid P\), total \(8m+2\).
- Difference: \((27m+6)-(8m+2)=19m+4\).

The global subtraction \(50m-3-(31m-7)=19m+4\) matches this leftover
count, so the triangulation does not hide a further cancellation. After
expressing high remainders, the same \(19m+4\) is the expected dimension
of the base \((B,d,\lambda,\gamma,\varepsilon)\) plus lower remainders,
cut by the leftover \(J\) and the \(B\mid P\) conditions.

This is an *expected* dimension, not an attained dimension. A lower
bound on dimension would need a witness family. None is constructed.
The count is used only as: the landed families of §2 do not empty the
chamber and do not make it finite-dimensional uniformly in \(m\).

---

## 5. What would flip the count

To overdetermine the residual one needs \(\gtrsim 19m+4\) further
independent equations.

| candidate | size | status |
|---|---|---|
| Independent high \(I3\) jets | \(19m-4\) | **fails**: \(k=4\) leading term is in the span of \(\Delta\) and \((\ast)\); (S1) | 
| Exact low-degree \(I3\) content beyond \(\deg\le 6m\), or \(B\)-divisibility in (S1) | \(\sim 3m\) or \(\sim 6m+1\) | would leave dimension \(\sim 16m\) or \(\sim 13m\), still open. Independence from \((\ast)\)'s own \(B\mid P\) is UNVERIFIED |
| \(\Delta\equiv 0\) (coefficients \(0,\ldots,16m-1\)) | \(16m\) | not landed (`hzero` ends at \(k=4m\)). Leaves \(\sim 3m+4\), still open |
| \(H\)-descent \(\deg H\le N=7m\) as on the Fce-zero branch | \(9m\) (coefficients \(7m+1,\ldots,16m-1\)) | off-chamber: that profile used \(Fce_0=0\) |
| Producing companions \(k=4,\ldots,D\) (or through \(4m\)) | changes the *chamber*, not the count on this residual | see §6 |

The family that actually fits the producing/matching split already
recorded in the induction report §4 is **further vanishing of \(A\)**,
obtained from a fourth (and then uniform) companion, remainder-cancel,
and load certificate. That does not add equations on the current
\((s,r_c)\) of degrees \(\le 14m-4\) and \(\le 10m-4\); it *shrinks*
those spaces and converts unused \(\Delta\)-jets into additional matching
rows. Even the maximal disc window \(K=4m\), if vanishing \(A\) were
granted that far, leaves \(\deg r_c\le 6m-1\) and does not fire the
zero-remainder comparison of \((\ast)\) (induction report §3.2). Closing
after that extension would still need a new identity (an H-profile, a
global \(\Delta=0\), or an I4-like relation forcing \(r_c=r_e=0\)).

A second I4-like identity strong enough to force \(r_c=r_e=0\) *would*
flip the chamber to empty, by the degree comparison already written:
left side of \((\ast)\) would be \(0\), right side has degree \(9m\) and
leading \(\tfrac19 B_D^3\neq 0\). That identity is not landed.

---

## 6. Remaining source rows, not counted

`FullRowZero` coefficients at \(2p-1-k\) are the companions. For
\(k=1,2,3\) the load algebra
(`second_load_algebra68`, `third_load_algebra68`) places the companion
in the localized ideal of disc jets \(0..k\) and I4 jets \(0..k\), and
the reduced companion is a nonzero multiple of the order-\(k\) jet of
\(A^2\). On \(Fce_0\neq 0\) this produced \(A_{p-k}=0\).

If that pattern continues, companions \(k=4,\ldots,4m\) are
*consequences* of \(\Delta\) and \((\ast)\), not extra constraints on
the residual coordinates of §2. Counting them would double-count.
They would, if the remainder-cancel and the numerical prefactor
\((p-k)\cdots(p-1)\neq 0\) were landed, *produce* further vanishing
\(A_{p-k}=0\) and thereby *change* the residual (smaller \(s\), more
matching). That producing recurrence is not landed past \(k=3\)
(induction report §4: missing fourth remainder-cancel and fourth load
certificate). It is the correct next input, not a family that can be
added to §2.2 today.

---

## 7. FALLACY-v2 checks

- No cv-flag / place / series identification.
- No exit-price, so no `charge_basis` line.
- Floor versus attainment: \(\deg s\le 14m-4\) and \(\deg J\le 14m\) are
  upper bounds. The number \(19m+4\) is a difference of counts, not an
  attained dimension. Not used as equality.
- Pole identities: none used. Vertex class not invoked.
- `sat()`: none.
- Terminal quotient / \(2c+C(3\gamma)=Bv\): other chamber; not applied.
- Prime marks: none. Differentiation is the polynomial derivative.
- Gaps (definition of `next68`; packet `def`s; independence of the
  \(B\mid P\) conditions in (S1) versus \((\ast)\); producing split past
  \(k=3\)) left open rather than filled by analogy.
- Syzygies (S1), (S2) were checked as polynomial identities against the
  committed algebra theorems; the \(k=4\) I3 cancellation and the
  \(\frac43\lambda B_D^2\) leftover were computed in remainder
  coordinates from those identities and the resultant, not by analogy
  with Fce-zero.

---

## 8. Verdict

**PARTIAL.**

- Residual coefficient count: derived.
  Unknowns \(50m-3\), landed independent-looking constraints \(31m-7\),
  difference \(19m+4\).
- Automatic versus residual: derived for \((\ast)\) (four top I4 jets
  consumed by matching; \(18m-3\) residual), for \(J\) (only the degree
  \(23m\) coefficient automatic; \(9m-1\) residual), and for \(\Delta\)
  (\(k=0,1,2,3\) consumed; \(4m-3\) residual).
- Triangular elimination of high \((s,r_c,r_e)\) for \(k=4,\ldots,4m\):
  derived, diagonals \(B_D^2\), \(B_D\), \(\frac43\lambda B_D^2\neq 0\).
  Expresses those remainders in \((B,d)\). No collision with
  \(Fce_0\neq 0\).
- Emptiness / finite-dimensionality: not derived. The chamber is
  genuinely open at this constraint level (expected dimension linear in
  \(m\)).
- \(I3\) does not flip the count (leading unused coefficient dependent;
  syzygy (S1)).
- New input that changes the chamber: order-\(4\) companion,
  remainder-cancel, and load certificate, as already named in the
  induction report §4. New input that would flip *this* residual
  without further vanishing \(A\): an identity forcing \(r_c=r_e=0\),
  or a landed family of length \(\gtrsim 19m+4\) (identically vanishing
  \(\Delta\) is \(16m\), short by \(\sim 3m+4\)).

UNVERIFIED items are labelled in §0 and at the reconstructed `next68`
typing of \(Rce\).
