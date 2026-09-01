# max11 68 q=0 vanishing-A chamber: identity hunt

**Verdict: PARTIAL**

The generating move that produced the sibling identity \(4H-C(C_0)=BT\)
is a three-term linear combination of the exact \(I3\) formula, the
quotient form of \(e\), and \(2c+C(3\gamma)=Bv\). The last two inputs
need \(Fce_0=0\) and are off-chamber. Three exact identities *do* land
in this chamber, all invisible to the \(19m+4\) count:

1. **Charged \(I4\) fibre.** Matching plus \(Fce=C(Fce_0)\) gives
   \(B\mid(2r_c+3\gamma)\bigl(d(2r_c+3\gamma)-2Fce_0\bigr)\). The factor
   \(B\mid(2c+C(3\gamma))\) is impossible (\(Fce\) would be \(B\) times a
   polynomial, hence \(Fce_0=0\)). This is the \(Fce_0\)-charged analogue
   of the square fibre, linear rather than quadratic.
2. **Charged row-two integral.** On the whole \(q=0\) wall, \(Fce\) is
   constant, so \(Fce'=0\). The source row `FullRowTwo`\( =0\) together
   with the load-factor rewrite is the derivative of
   \(P+3\,Fce_0 A\), hence \(P+3\,Fce_0 A=C(\kappa)\). This is the
   \(Fce_0\neq 0\) form of the identity that the terminal branch used as
   \(P=C(\kappa)\).
3. **Conditional \(\Delta\)/\(H\) profiles.** If the next68 bound
   \(\deg Rce\le 2D=6m\) is granted, the degree-\(19m\) coefficient of
   the universal syzygy (S1) does not see \(Fce_0\) and forces
   \(\deg\Delta=11m\) with top \(3B_D d_V\), after which (S2) forces
   \(\deg H\le N=7m\). These are the Fce-zero profiles, now without
   \(Fce_0=0\). They do **not** produce \(4H-C=BT\) (that still needs
   \(d^2\equiv\mathrm{const}\pmod{B}\)).

None of these is a two-case degree kill. Wronskians of the matching
pairs have no degree drop. An exact rational \(m=1\) model of a proper
subsystem (matching \(+\) I4 \(+\) \(\deg J\le 14\) \(+\) vanishing \(A\)
\(+\) resultant \(+\) \(Fce_0=1\)) is displayed in §5; on that model
identities 2 and 3 fail. Groebner bases of identity 2 plus
\(\deg J\le 14\) plus I4 are the unit ideal on every sampled point of
the necessary \(J_{20}=J_{21}=J_{22}=0\) locus at \(m=1\), including a
squarefree cubic \(B\). That is computational evidence, not a theorem,
and is not promoted to `False`.

No exit-price is claimed.

---

## 0. Sources and verification status

Work over an algebraically closed field \(k\) of characteristic zero, on
the wall \(9N=7S\). Write \(N=7m\) with \(m\ge 1\), so \(S=9m\).

Clone used for reading: `https://github.com/dcposch/jc2-lean` at
`93ac345` (`origin/master` as of this run). Nested worktree `jc2-lean/`
is sandbox-blocked.

### 0.1 What was read

| File / theorem | Used for |
|---|---|
| `Grok68QZeroVanishingAJetScratch.lean` (SHA `b567d6987263468f206347bbd74f16d3605ac3febec40f53aed92e97ec410e17`) | landed matching \(k=1,2,3\); residual; \(Fce_0\neq 0\) |
| `...TerminalHDescentScratch.lean`, `..._H_descent_algebra68`, `..._H_quotient68` | generating combination for \(4H-C(C_0)=BT\) |
| `...TerminalQuotientScratch.lean` | \(2c+C(3\gamma)=Bv\), exact \(e\), \(H\) in \(v\) |
| `...TerminalUProfileScratch.lean`, `...VDescentScratch.lean`, `...SquareFiberScratch.lean` | \(U\), \(v\)-descent, \(36d^2-C(C_0)=Bs\); all need \(Fce_0=0\) |
| `Grok68TerminalBranchClosureScratch.lean` | assembly \(3dZ+BU-18\gamma B^2+C(C_0)=0\) |
| `...FceZeroGlobalScratch.lean`, `..._Fce_Rce_Delta_descent_algebra68` | universal syzygy (S1) |
| `...FceZeroHDegreeScratch.lean`, `..._Fce_J_Delta_H_algebra68` | universal syzygy (S2); \(H=4B^2c+9d^2\) |
| `...FceZeroRowTwoIntegralScratch.lean` | \(P=6(J+B^2d)+9\gamma Bc-(27/2)\varepsilon d\); \(P'=0\) on \(Fce=0\) |
| `...RemainderScratch.lean`, `..._clean_rowTwo_expansion68` | `FullRowTwo` expansion; `Load2` and `Rem2` |
| `...LoadExpansionScratch.lean` | `Load2` \(=6(B^2 d)'\) |
| `...CompanionNextScratch.lean` | load-factor rewrite used on the whole wall; \(\deg J\le p\) |
| `...FceZeroDeltaTopScratch.lean` | Fce-zero \(\Delta\) top, reused for the charged top |
| `...TopResultantScratch.lean` | I4 top and quadratic resultant |
| `xmodel/max11-68-vanishing-a-uniform-induction-grok46-20260831.md` | remainder form, matching recurrence |
| `xmodel/max11-68-vanishing-a-elimination-count-grok46-20260831.md` | \(19m+4\) count; high-jet triangulation |
| `xmodel/max11-68-kappa-rigidity-derivation-grok46-20260831.md` | paper form of the terminal close |

Index conventions as in the induction report, using \(G=2S\) at every
`rw [hGS]` site. Defining theorem of `hGS` not opened. UNVERIFIED as a
standalone declaration; used as \(G=2S\).

### 0.2 What was not read

- `Sol68...QZeroCompanionScratch.lean`, the file that *defines*
  `fiveToSix_..._qZero_next68` / `QZeroNextScalar68` and
  `fiveToSix_zetaFirst_B3_equality_support_load_factor68`: **not on
  `origin/master`** (HTTP 404). The identities \(Fce=\tfrac38 C(i_4)\),
  \(\deg Rce\le 2D\), and \(Rce=\tfrac34\gamma B^2+\tfrac98 C(i_3)\) are
  read from every consumer (same reconstruction as the count report).
  The load-factor rewrite
  \[
  \text{row-two core}= -6A\,Fce'+3A'\,Fce+6J'
  \]
  is the type used at every `hfactor.2` site in committed files
  (`CompanionNext`, `FceZeroRowTwoIntegral`). Marked UNVERIFIED as a
  Lean declaration; used below as the rewrite those files apply.
- Packet `def`s (`FullRowTwo`, `RowTwoLoad`, `EndpointRowTwoCore`,
  `fiveToSixCuspDiscriminantPolynomial68`): not on `origin/master`.
  Expansions taken from named consumer theorems.
- Strict-B3 / sparse-endpoint closures: not used.

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

Residual after matching through \(k=3\):

\[
A=A_p X^p+s,\quad \deg s\le 14m-4,
\]
\[
c=\lambda X^N B+r_c,\quad \deg r_c\le 10m-4,
\]
\[
e=-\lambda X^N d+r_e,\quad \deg r_e\le 15m-4,
\]
with \(Fce=C(Fce_0)\) and \(Fce_0\neq 0\).

\[
\begin{align*}
Fce&=(Be+cd)-\tfrac19 B^3+\tfrac32\gamma\,d+\tfrac34\varepsilon\,B,\\
Rce&=-ABd+3ce-B^2c+\tfrac32 d^2+\tfrac92\gamma\,e+\tfrac94\varepsilon\,c,\\
\Delta&=AB^2+3c^2,\\
J&=Bc^2-\tfrac19 AB^3-3de,\\
H&=4B^2c+9d^2,\\
P&=6(J+B^2 d)+9\gamma Bc-\tfrac{27}{2}\varepsilon d.
\end{align*}
\]

Differentiation is the polynomial derivative in \(X\).

---

## 1. How \(4H-C(C_0)=BT\) was originally derived

The Lean algebra theorem
`fiveToSix_qZero_Fce_zero_terminal_H_descent_algebra68` is a ring
identity in \(k[X]\), transported to `RatFunc k` and closed by
`linear_combination`. The three generators, with \(v\) the terminal
quotient, are

\[
\begin{align*}
hv&: 2c+C(3\gamma)-Bv,\\
he&: e-\bigl(\tfrac19 B^2-\tfrac12 vd-C(\tfrac34\varepsilon)\bigr),\\
hR&: Rce-\bigl(\tfrac34\gamma B^2+\tfrac98 C(i_3)\bigr).
\end{align*}
\]
The combination recorded in the file is
\[
(-24)\,hR+(36)(2c+3\gamma)\,he+(-2)(8B^2+9dv)\,hv.
\]
On \(hv=he=hR=0\) this equals
\[
2B\bigl(3Wd+8B^2 v-21\gamma B\bigr)-(4H-C(C_0)),
\]
with \(W=4A+3v^2\) and \(C_0=81\varepsilon\gamma+27 i_3\). That is
\(4H-C(C_0)=BT\) with \(T=2(U-21\gamma B)\) and \(U=3Wd+8B^2 v\).

Spot-checked as a polynomial identity in commuting symbols (sympy
`expand`, residual identically zero). The identity uses \(hv\) and
\(he\), both of which require the terminal quotient, hence \(Fce_0=0\).
It is not available in this chamber.

The U-profile, V-descent, and square fibre are downstream of this
quotient (they rewrite \(T\), \(v\), and \(H\equiv 9d^2\pmod{B}\)). They
are off-chamber for the same reason.

The row-two first integral \(P=C(\kappa)\) *is* a derivative identity,
and is the “pairing a row with the derivative of a quadratic form”
named in the prompt. Its Fce-zero form is
`FceZeroRowTwoIntegralScratch.lean`: once \(Fce=0\), the expansion of
`FullRowTwo` collapses to \(P'=0\). Section 3 charges that identity.

---

## 2. Hunt 1: H-analogue

### 2.1 Combinations already landed

- \(B r_e+r_c d\) is the I4 identity \((\ast)\), already in the count
  report. Euclidean division by \(B\) is the \(3m\) conditions
  \(B\mid(RHS-r_c d)\), counted, not a new profile.
- \(H=4B^2 c+9d^2=4\lambda X^N B^3+4B^2 r_c+9d^2\). The resultant kills
  \(H_{16m}\). Matching through \(k=3\) does not kill \(H_{16m-1,16m-2,16m-3}\):
  those are the three subleading constraints on \((B,d)\) already
  recorded as \(J_{23m-1,23m-2,23m-3}\).
- \(J\) itself has a degree drop \(\le 14m\) from the post-epsilon
  state, already counted.

### 2.2 Derivative of I4 paired with \(\Delta\)

Differentiating \((\ast)\) produces \(B' r_e+B r_e'+r_c' d+r_c d'\), a
rearrangement of I4 jets, not a new polynomial. Pairing with \(\Delta'\)
or with the generating function of the unused \(\Delta\)-jets
reproduces the triangular pin of §3 of the count report (diagonals
\(B_D^2\), \(B_D\), \(\tfrac43\lambda B_D^2\)). No leftover of the form
\(B\cdot(\mathrm{quotient})+C(\mathrm{scalar})\) appears that is not
already \((\ast)\) or (S1).

### 2.3 No \(4H-C=BT\)

By definition \(H\equiv 9d^2\pmod{B}\). The identity \(4H-C(\mathrm{const})=BT\)
is equivalent to \(36d^2\equiv C(\mathrm{const})\pmod{B}\), the terminal
square fibre. The charged fibre of §3 is linear in \(d\), not quadratic.
Without \(d^2\) constant on \(V(B)\), there is no H-quotient.

On the explicit \(m=1\) model of §5 one has \(B=X^3\) (a triple root) and
\(H\equiv 9\pmod{X^3}\), so \(4H-36\) is divisible by \(B\). That is the
one-point remainder at the unique root of \(X^3\), not a square fibre
on a squarefree cubic.

---

## 3. Hunt 2: \(Fce_0\)-charged descent

### 3.1 Universal syzygies (ring identities)

(S1), from `Fce_Rce_Delta_descent_algebra68`, checked `expand=0`:
\[
24d\,\Delta+\mathrm{Rest}+24B\bigl(Rce-\tfrac34\gamma B^2-\tfrac98 C(i_3)\bigr)
=(72c+108\gamma)\,Fce,
\]
\[
\mathrm{Rest}=16B^3 c+6\gamma B^3-36 B d^2+81\varepsilon\gamma B
+216\gamma cd+162\gamma^2 d+27 i_3 B.
\]
Also \(16B^3 c-36 B d^2=4BH-72 B d^2\).

(S2), from `Fce_J_Delta_H_algebra68`, checked `expand=0`:
\[
BJ=-\tfrac19 B^2\Delta+\tfrac13 c H-\tfrac13 B^3 d+\tfrac92\gamma d^2
+\tfrac94\varepsilon Bd-3d\,Fce.
\]

### 3.2 I4 modulo \(B\), after matching

Matching gives \(Be+cd=B r_e+r_c d\), so \(Fce=C(Fce_0)\) is
\[
B r_e+r_c d=\tfrac19 B^3-\tfrac32\gamma d-\tfrac34\varepsilon B+C(Fce_0).
\]
Reduce modulo \(B\):
\[
r_c d\equiv -\tfrac32\gamma d+Fce_0\pmod{B},
\]
i.e.
\begin{equation}
d\bigl(r_c+\tfrac32\gamma\bigr)\equiv Fce_0\pmod{B},
\qquad
d(2r_c+3\gamma)-2Fce_0\equiv 0\pmod{B}.
\tag{\(\dagger\)}
\end{equation}
This uses only matching and I4 constancy. It does not use exact \(Rce\).

### 3.3 The same fibre from (S1)

Substitute \(\Delta=sB^2+6\lambda X^N B r_c+3 r_c^2\) (cusp top plus the
definition of \(s,r_c\); checked `expand=0`) into (S1) with exact \(Rce\)
and \(Fce=C(Fce_0)\). The leftover at \(B=0\) is
\[
72 d r_c^2+216\gamma r_c d+162\gamma^2 d-72 r_c Fce_0-108\gamma Fce_0
=18(2r_c+3\gamma)\bigl(d(2r_c+3\gamma)-2Fce_0\bigr).
\]
Checked `factor` / `expand=0`. Thus (S1) plus matching plus exact \(Rce\)
gives
\begin{equation}
B\ \Big|\ (2r_c+3\gamma)\bigl(d(2r_c+3\gamma)-2Fce_0\bigr).
\tag{\(\ddagger\)}
\end{equation}
When \(\gcd(B,2r_c+3\gamma)=1\), this is \((\dagger)\). In general it is
the product.

### 3.4 Case I is impossible

If \(B\mid(2r_c+3\gamma)\), then \(B\mid(2c+C(3\gamma))\) because
\(2c+3\gamma=2\lambda X^N B+(2r_c+3\gamma)\). Write \(2c+C(3\gamma)=Bv\).
A ring computation (checked `expand=0`) gives
\[
Fce=B\Bigl(e+\tfrac12 vd-\tfrac19 B^2+C\bigl(\tfrac34\varepsilon\bigr)\Bigr).
\]
A nonzero constant cannot be \(B\) times a polynomial when \(\deg B=3m\ge 3\).
This contradicts \(Fce_0\neq 0\). So Case I is empty in this chamber.
(The terminal quotient is exactly Case I, on the other side of the
producing split.)

### 3.5 Case II is not a degree kill

If \(\gcd(B,2r_c+3\gamma)=1\), then
\(d(2r_c+3\gamma)-2Fce_0=B\cdot Q\) for some \(Q\). Naive degrees:
\(\deg(2r_c+3\gamma)\le 10m-4\), so \(\deg(\mathrm{LHS})\le 18m-4\) and
\(\deg Q\le 15m-4\). Both \(Q\neq 0\) and \(Q=0\) are compatible with the
frozen degrees (\(Q=0\) is \(d(2r_c+3\gamma)=2Fce_0\), degree \(8m\)
versus a constant, impossible unless \(2r_c+3\gamma=0\), which is Case I).
There is no two-case comparison of the terminal shape.

A mixed factorisation \(B=B_1 B_2\) is allowed; it does not improve the
degree count. Squarefreeness of \(B\) is not a landed hypothesis of this
chamber (it is a terminal-branch theorem).

### 3.6 Conditional \(\Delta\) top / \(H\) degree, without \(Fce_0=0\)

Grant \(\deg Rce\le 6m\) (the next68 bound, used as `hRceDeg` in
`I3Next`). Then \(24B(Rce-\cdots)\) has degree \(\le 9m\), and
\((72c+108\gamma)Fce_0\) has degree \(\le 10m\). The degree-\(M=19m\)
coefficient of (S1) is therefore
\[
24 d_V\Delta_{11m}+16 B_D^3 c_{Cc}-36 B_D d_V^2=0,
\]
the same row as `Fce_zero_Delta_top68`. Combined with the resultant
\(4\lambda B_D^3+9d_V^2=0\) it yields
\[
\Delta_{11m}=3 B_D d_V\neq 0,
\]
hence \(\deg\Delta=11m\) exactly. Checked by reducing the leading
coefficient of \(\mathrm{Rest}\) onto the resultant (the comparison
\(\Delta_{11m}-3B_D d_V\) vanishes after \(d_V^2=-(4/9)\lambda B_D^3\)).

The \(Fce_0\) terms never reach degree \(19m\). This profile is
**not off-chamber**. The count report listed “\(\deg H\le N\) as on the
Fce-zero branch” as off-chamber because that report obtained
\(\deg\Delta\le 11m\) only from `Fce_zero_global68`. The top coefficient
does not need \(Fce=0\).

With \(\deg\Delta=11m\) and \(\deg J\le 14m\), (S2) gives
\(\deg(cH)\le 17m\), hence \(\deg H\le 7m=N\). The term \(3d Fce_0\) has
degree \(8m<17m\) and does not raise the bound.

These \(9m-1\) vanishing coefficients of \(H\) (degrees \(7m+1\) through
\(16m-1\); \(H_{16m}\) already zero by the resultant) and the extra
\(\Delta\) coefficients of degrees \(11m+1\) through \(16m-1\) (\(5m-1\)
of them, beyond the unused `hzero` window) would cut the expected
dimension from \(19m+4\) to about \(14m+5\) if independent of the
already-counted \(J\) high jets. They still leave a linear-in-\(m\)
fibre. They do not force \(4H-C=BT\).

Without the \(Rce\) degree bound, the explicit model of §5 has
\(\deg Rce=17\) and \(\deg\Delta=12>11\), so the profile is conditional
on next68, not a consequence of matching\(+\)I4 alone.

---

## 4. Hunt 3: charged first integral, Wronskians, \(J\) drop

### 4.1 Row-two generating function

Write
\[
\mathrm{gen}:=-6A\,Fce'+3A'\,Fce+6J',
\quad
\mathrm{Load}_2:=6(B^2 d)',
\quad
\mathrm{Rem}_2:=9\gamma(Bc)'-\tfrac{27}{2}\varepsilon d'.
\]
A function-of-\(X\) expansion (sympy) gives two identities:
\[
P'=6J'+\mathrm{Load}_2+\mathrm{Rem}_2,
\]
\[
\mathrm{gen}+\mathrm{Load}_2+\mathrm{Rem}_2=P'+3A'\,Fce-6A\,Fce'.
\]
The committed expansion of `FullRowTwo` (RemainderScratch) plus the
load-factor rewrite used in CompanionNext / FceZeroRowTwoIntegral is
\[
(-\tfrac{27}{4})\,\mathrm{FullRowTwo}=\mathrm{gen}+\mathrm{Load}_2+\mathrm{Rem}_2.
\]
The packet supplies `FullRowTwo`\(=0\) as a polynomial (`hrow2`). Thus
\(\mathrm{gen}+\mathrm{Load}_2+\mathrm{Rem}_2=0\). On the \(q=0\) wall
\(Fce=C(Fce_0)\) is constant, so \(Fce'=0\) and
\[
P'+3 Fce_0 A'=0,
\]
hence
\begin{equation}
P+3\,Fce_0 A=C(\kappa).
\tag{\(\S\)}
\end{equation}
On \(Fce_0=0\) this is the landed terminal integral \(P=C(\kappa)\). The
coefficient \(3\) is the one in `load_factor.2` (the \(A'Fce\) term),
not a total-derivative guess: \(\mathrm{gen}\) has \(-6A Fce'+3A' Fce\).

Load-factor is UNVERIFIED as a Lean `def` (file absent); it is the
rewrite applied on the whole wall by committed theorems. If that rewrite
is granted, \((\S)\) is a theorem of this chamber.

At degree \(14m\), \((\S)\) reads
\[
6J_{14m}+6 B_D^2 d_V+3 Fce_0 A_p=0,
\]
i.e. \(J_{14m}=-B_D^2 d_V+\tfrac32\lambda^2 Fce_0\). Compatible with
\(\deg J\le 14m\). Not a contradiction by itself.

### 4.2 Wronskians

\[
\mathrm{Wr}(c,B)=\lambda N X^{N-1} B^2+\mathrm{Wr}(r_c,B).
\]
Leading term \(\lambda N B_D^2\neq 0\) at degree \(13m-1\). No drop.

\[
\mathrm{Wr}(e,d)=-\lambda N X^{N-1} d^2+\mathrm{Wr}(r_e,d).
\]
Leading term \(-\lambda N d_V^2\neq 0\) at degree \(23m-1\). No drop.

The \(J\) drop \(\le 14m\) versus naive \(23m\) is the post-epsilon
state. Coefficientwise, \(J_{23m}=0\) is the resultant (induction
report §3.3); \(J_{23m-1,23m-2,23m-3}\) are the three subleading
\((B,d)\) constraints, independent of remainders. For \(m=1\) these are
\(J_{22},J_{21},J_{20}\), computed exactly:
\begin{align*}
J_{22}&=108(3B_2-d_7),\\
J_{21}&=324 B_1+324 B_2^2-108 d_6-27 d_7^2,\\
J_{20}&=324 B_0+648 B_1 B_2+108 B_2^3-108 d_5-54 d_6 d_7,\\
J_{23}&=0
\end{align*}
(with \(B=X^3+B_2 X^2+B_1 X+B_0\) and \(d=2X^8+\cdots\), \(\lambda=-9\)).
These pin \((d_7,d_6,d_5)\) in terms of \((B_2,B_1,B_0)\) and are
necessary for \(\deg J\le 14\). They are not a new identity beyond the
already-counted \(J\) high jets.

---

## 5. Hunt 4: exact \(m=1\) model of a proper subsystem

### 5.1 What is modelled

Wall chart \(m=1\): \(N=7\), \(S=9\), \(p=14\), \(D=3\), \(Cc=10\),
\(V=8\), \(E=15\). The polynomials below satisfy, in \(\mathbb{Q}[X]\):

- cusp \(A_{14} B_3^2+3 c_{10}^2=0\),
- resultant \(4 B_3^2 c_{10}+9 d_8^2=0\),
- vanishing \(A_{13}=A_{12}=A_{11}=0\),
- matching \(c=\lambda X^7 B+r_c\) with \(\deg r_c=0\le 6\),
- I4 / \(Fce=C(1)\),
- \(\deg J=14\) (bound saturated),
- exact degrees \(\deg A=14\), \(\deg B=3\), \(\deg c=10\), \(\deg d=8\),
  \(\deg e=15\),
- \(Fce_0=1\neq 0\), \(\lambda=-9\neq 0\), \(B_3=1\neq 0\), \(d_8=2\neq 0\).

They do **not** satisfy \(\deg Rce\le 6\), identity \((\S)\), or
\(\deg\Delta=11\). They are a model of matching\(+\)I4\(+\deg J\le 14\),
not of the full packet.

### 5.2 The polynomials

\[
\begin{align*}
\lambda&=-9,\qquad\gamma=0,\qquad\varepsilon=0,\qquad Fce_0=1,\\
A&=-243 X^{14}+972 X^6,\\
B&=X^3,\\
c&=-9 X^{10}-1,\\
d&=2 X^8-1,\\
e&=18 X^{15}-9 X^7+\tfrac19 X^6+2 X^5.
\end{align*}
\]
Remainders: \(s=972 X^6\), \(r_c=-1\),
\(r_e=\tfrac19 X^6+2 X^5\)
(from \(e=-\lambda X^7 d+r_e\)).

Derived objects:
\[
\begin{align*}
Fce&=1,\\
J&=-\tfrac23 X^{14}+6 X^{13}-27 X^7+\tfrac13 X^6+6 X^5+X^3,\\
H&=-36 X^8-4 X^6+9,\\
\Delta&=972 X^{12}+54 X^{10}+3,\\
Rce&=-1944 X^{17}+12 X^{16}-108 X^{15}+972 X^9-6 X^8+27 X^7\\
&\qquad+\tfrac23 X^6-6 X^5+\tfrac32,\\
P+3 Fce_0 A&=-721 X^{14}+36 X^{13}-162 X^7+2912 X^6+36 X^5+6 X^3.
\end{align*}
\]

I4 check:
\[
Be+cd=\tfrac19 X^9+1=\tfrac19 B^3+Fce_0.
\]
Fibre \((\dagger)\): \(d(2r_c)-2Fce_0=-2d-2=-4 X^8\), and \(X^3\mid 4X^8\).

### 5.3 What the model shows

The chamber cannot be emptied by matching\(+\)I4\(+\deg J\le 14\) alone:
a rational point exists. Identity 3 fails here because \(\deg Rce=17>6\).
Identity \((\S)\) fails (\(\deg(P+3A)=14>0\)); the degree-\(14\)
coefficient is \(-721\), versus the value \(0\) that \((\S)\) would
require.

### 5.4 Groebner evidence at \(m=1\), not a theorem

On the locus \(J_{20}=J_{21}=J_{22}=0\) (necessary for \(\deg J\le 14\),
independent of remainders) the system I4 \(+\) \(\deg J\le 14\) \(+\)
\((\S)\) was run as a Groebner basis in the eleven coefficients of \(s\)
after linearly eliminating \(r_c\). The basis is \(\{1\}\) at every
sampled point, including:

- \(B=X^3\) with several \((d_0,d_1,\gamma,\varepsilon)\),
- \(B=X^3+X+1\) (squarefree over \(\mathbb{Q}\), discriminant \(-31\)),
  with the closed-form \((d_5,d_6,d_7)\) that kills \(J_{20,21,22}\),
- \(B=X^3+2X^2+X+1\) and several other closed-form cubics.

This is a finite sample, not a Gröbner basis in the coefficients of
\((B,d)\). It is **not** `False`. It is evidence that identity \((\S)\),
if granted as a packet theorem, overdetermines the \(m=1\) chart of
I4\(+\deg J\le 14\), and that the next honest job is a uniform (in \(m\))
degree comparison of \((\S)\) against I4, not further constraint
counting.

The same sample often gives Groebner \(\{1\}\) for I4\(+\deg J\le 14\)
plus \(\deg Rce\le 6\). Those runs used `numer(together(·))` after a
linear substitution; a purported zero-dimensional rational point on one
slice failed an independent reconstitution (\(\deg J=15\), \(\deg Rce=21\)).
No \(Rce\)-exact model is claimed.

---

## 6. FALLACY-v2 checks

- No cv-flag / place / series identification.
- No exit-price, so no `charge_basis` line.
- Floor versus attainment: \(\deg s\le 14m-4\), \(\deg J\le 14m\),
  \(\deg\Delta=11m\) (conditional), \(\deg H\le 7m\) (conditional) are
  used as upper bounds or as exactness only where a nonzero leading
  coefficient is written. The number \(19m+4\) is not treated as an
  attained dimension. The Groebner \(\{1\}\) at sampled \(m=1\) points
  is not promoted to emptiness of the chamber.
- Pole identities: none used. Vertex class not invoked.
- `sat()`: none. Groebner bases are over \(\mathbb{Q}\) in explicitly
  declared generators (coefficients of \(s\) after a declared linear
  elimination of \(r_c\)); positive control is the explicit I4+\(J\)
  model of §5.2; negative control is Groebner \(\{1\}\) when \((\S)\) is
  added on the same slice.
- Terminal quotient / \(2c+C(3\gamma)=Bv\): other chamber; used only as
  the Case I contradiction of §3.4.
- Prime marks: differentiation is the polynomial derivative.
- Gaps (definition of `next68`; load-factor `def`; packet `def`s;
  squarefreeness of \(B\); independence of the conditional \(\Delta/H\)
  profiles from already-counted \(J\) jets; Groebner sample versus a
  theorem in \((B,d)\)) left open rather than filled by analogy.
- Syzygies (S1), (S2), the H-descent generating combination, the Case I
  factorisation of \(Fce\), the matching form of \(\Delta\), and the
  leftover factorisation \(18(2r_c+3\gamma)(\cdots)\) were expanded as
  polynomial identities. The row-two generating function was expanded
  in \(k(X)\) with the product rule.

---

## 7. Verdict

**PARTIAL.**

- Generating combination for the sibling \(4H-C(C_0)=BT\): derived, and
  off-chamber (needs \(hv\) and \(he\)).
- Charged I4 fibre \((\dagger)\)/\((\ddagger)\): derived. Case I
  (\(B\mid 2c+C(3\gamma)\)) is empty. Case II is not a two-case degree
  kill and is not a square fibre.
- Charged row-two integral \((\S)\): derived from `FullRowTwo`\(=0\)
  plus the load-factor rewrite plus \(Fce'=0\), with the load-factor
  declaration UNVERIFIED. Not a degree kill by itself.
- Conditional \(\deg\Delta=11m\) with top \(3B_D d_V\), and
  \(\deg H\le 7m\): derived from (S1)/(S2) plus \(\deg Rce\le 6m\) plus
  \(\deg J\le 14m\). Independent of \(Fce_0=0\) at the top. Do not
  produce \(4H-C=BT\).
- Wronskians: no drop.
- Exact \(m=1\) model of matching\(+\)I4\(+\deg J\le 14\): constructed
  over \(\mathbb{Q}\), fully displayed. Proves that subsystem is
  nonempty. On the model, \((\S)\) and the \(Rce\) bound fail.
- Emptiness of the chamber: not derived. Groebner \(\{1\}\) for
  \((\S)+\)I4\(+\deg J\le 14\) on sampled \(m=1\) points of the necessary
  \(J_{20}=J_{21}=J_{22}=0\) locus is recorded as evidence, not as
  `False`.

New input that would close in the terminal style: a uniform degree
comparison of \((\S)\) against I4 (both cases of a remainder, both
impossible), or a proof that \((\S)+\)I4 forces \(r_c=r_e=0\) and then
the already-written comparison of \((\ast)\). New input that changes
the residual without a new identity: order-\(4\) companion,
remainder-cancel, and load certificate, as in the induction report §4.

UNVERIFIED items are labelled in §0 and at the load-factor rewrite.
