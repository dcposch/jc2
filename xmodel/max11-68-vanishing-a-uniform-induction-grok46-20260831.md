# max11 68 q=0 vanishing-A chamber: all-orders jet matching

**Verdict: PARTIAL**

The matching recurrence that sends a vanishing row \(A_{2N-k}=0\) to
\[
c_{Cc}\,B_{D-k}-B_D\,c_{Cc-k}=0,\qquad
B_D\,e_{E-k}+c_{Cc}\,d_{V-k}=0
\]
is uniform in \(k\) on a stated interval, with an explicit first break.
All-orders proportionality through \(k=D\) is a theorem *if* vanishing of
\(A\) is granted through that same \(k\); the producing companion split
lands vanishing \(A\) only through \(k=3\). Feeding the landed
\(k=1,2,3\) matching (or the conditional all-orders form) into the frozen
packet does not produce `False`. The terminal quotient \(2c+C(3\gamma)=Bv\)
does not apply in this chamber. The surviving residual is the degree-dropped
pair below, plus one extra discriminant coefficient once \(k=3\) is used
up.

No exit-price is claimed.

---

## 0. Sources and verification status

Work over an algebraically closed field \(k\) of characteristic zero, on
the wall \(9N=7S\). Write \(N=7m\) with \(m\ge 1\), so \(S=9m\).

### 0.1 What was read

The nested worktree `jc2-lean/` is sandbox-blocked. A clone of
`https://github.com/dcposch/jc2-lean` at `d4e9bfe` (origin `master` as of
this run) was used for reading. Kernel-checked modules actually opened:

| File / theorem | Used for |
|---|---|
| `...QZeroCompanionThirdReductionScratch.lean`, `fiveToSix_..._third_companion_split68` | producing split \(Fce_0=0\) or \(A_{p-1}=A_{p-2}=A_{p-3}=0\) |
| `...QZeroCompanionNextReductionScratch.lean`, `..._second_companion_split68` | order-two split |
| `...QZeroJetRankScratch.lean`, `..._jet_rank68` | order-one split \(Fce_0 A_{p-1}=0\) |
| `...QZeroDiscriminantNextScratch.lean`, `..._next_two68`, `..._discriminant_third68` | \(\Delta_{U-k}=0\) for \(k=1,2,3\) |
| `...QZeroTopResultantScratch.lean`, `...TopNextScratch.lean`, `...I4NextTwoScratch.lean`, `..._I4_third68` | \((Be+cd)_{K-k}=0\) for \(k=0,1,2,3\) |
| `...QZeroLoadThirdAlgebraScratch.lean` | order-three load certificate from disc\(+\)I4 jets |
| `...QZeroCompanionNextScratch.lean`, `...CompanionThirdScratch.lean` | companions as coefficients of `FullRowZero`; \(Fce=C(Fce_0)\) |
| `...QZeroRemainderScratch.lean`, `...RemainderNextScratch.lean`, `...RemainderThirdScratch.lean` | remainder cancel by shortness / \((N,S)=(7,9)\) chart |
| `...QZeroFceZeroGlobalScratch.lean`, `...FceZeroTerminalQuotientScratch.lean` | the *other* chamber; terminal quotient needs \(Fce_0=0\) |
| `...QZeroLargeReductionScratch.lean` | first companion after remainder cancel |

The discriminant polynomial is the object named
`fiveToSixCuspDiscriminantPolynomial68`. Every coefficient expansion
used below is the Cauchy product of \(A B^2+3c^2\) (the factor \(3\) is
the one that turns \((c^2)_{U-1}=2c_{Cc}c_{Cc-1}\) into the displayed
`6 c_Cc c_{Cc-1}` of `discriminant_next68`). Defining `def` not present
in the cloned tree; the identification is from those expansions and from
the Fce-zero identity \(4\Delta=4AB^2+3(Bv-C(3\gamma))^2\). Marked
UNVERIFIED as a standalone declaration, verified as an expansion.

### 0.2 What was not read

- `Grok68QZeroVanishingAJetScratch.lean` (prompt SHA
  `b567d6987263468f206347bbd74f16d3605ac3febec40f53aed92e97ec410e17`):
  untracked scratch, sandbox-blocked, not on `origin/master`, blob not
  in the submodule git objects. The prompt's landed identities for
  \(k=1,2,3\) are **re-derived** in §2 from the committed disc/I4 jets
  plus the producing split; the residual Prop name
  `FiveToSixCuspZetaFirstB3EqualitySupportQZeroVanishingAJetResidual68`
  is UNVERIFIED as a Lean declaration.
- `Grok68TerminalBranchClosureScratch.lean`: not in the clone. The
  sibling *style* (exact identity, then two-case degree comparison) is
  taken from the committed Fce-zero terminal modules and from the
  parallel Fce-zero paper derivation. Those modules live in the
  **other** chamber.
- Strict-B3 / sparse-endpoint closures: no file with those names in the
  cloned `max11-partial-y/`. UNVERIFIED.

### 0.3 Notation

\[
p=2N,\quad
D=3N-2S,\quad
Cc=4N-2S,\quad
V=5N-3S,\quad
E=6N-3S,\quad
U=8N-2G,\quad
K=D+E.
\]
On the wall, \(D=3m\), \(Cc=10m\), \(V=8m\), \(E=15m\), \(p=14m\),
\(Cc-D=N=7m\), \(E-V=N=7m\). Packet tops: \(A_p\neq 0\), \(B_D\neq 0\),
\(c_{Cc}\neq 0\), \(d_V\neq 0\), \(e_E\neq 0\).

The loaded-source component `hGS` is the identification used at every
`rw [hGS]` site that proves \(p+2D=U\), \(2Cc=U\), \(V=5N-G-S\), and
\(D=3N-G\) (`FceZeroDeltaTopScratch.lean`, `have hbidx:D=3*N-G`). These
are equivalent to \(G=2S\). Used below as \(G=2S\). Defining theorem of
`hGS` not opened (imported support file absent from the clone).

Compensated I4:
\[
Fce=(Be+cd)-\tfrac19 B^3+\tfrac32\gamma\,d+\tfrac34\varepsilon\,B.
\]
On the whole \(q=0\) wall, `next68` gives \(Fce=\tfrac38\cdot C(i_4)\),
hence \(Fce=C(Fce_0)\) as polynomials
(`CompanionNextScratch.lean`, `have hFconst`). In **this** chamber
\(Fce_0\neq 0\).

Cusp discriminant \(\Delta:=AB^2+3c^2\). The packet supplies
\((\Delta.\mathrm{reflect}\,U)_i=0\) for all
\(1\le i\le \min(S,7N-2G-S)\) (`hzero` in `discriminant_next68`). With
\(G=2S\),
\[
\min\bigl(S,\,7N-2G-S\bigr)=\min\bigl(9m,\,4N/7\bigr)=4m=:K_\Delta.
\]
So discriminant jets exist through order \(K_\Delta=4m\), which is
strictly larger than \(D=3m\).

---

## 1. Question 1: uniformity of matching from vanishing \(A\)

### 1.1 What produces row \(k\)

Two independent polynomial jets, plus the vanishing row, plus previous
matching rows.

**Discriminant jet of order \(k\)** (for \(1\le k\le K_\Delta\)).
`hzero k` and `coeff_reflect` give \(\Delta_{U-k}=0\). Expanding the
Cauchy product at \(U=p+2D=2Cc\):
\begin{align*}
(AB^2)_{U-k}
&=\sum_{j=0}^{k}A_{p-j}(B^2)_{2D-(k-j)},\\
(c^2)_{U-k}
&=\sum_{j=0}^{k}c_{Cc-j}c_{Cc-(k-j)}.
\end{align*}
The named theorems are exactly these expansions for \(k=1,2,3\):

- \(k=1\): \(A_{p-1}B_D^2+2A_p B_D B_{D-1}+6c_{Cc}c_{Cc-1}=0\).
- \(k=2\): \(A_{p-2}B_D^2+2A_{p-1}B_D B_{D-1}+A_p(2B_D B_{D-2}+B_{D-1}^2)+3(2c_{Cc}c_{Cc-2}+c_{Cc-1}^2)=0\).
- \(k=3\): \(A_{p-3}B_D^2+2A_{p-2}B_D B_{D-1}+A_{p-1}(2B_D B_{D-2}+B_{D-1}^2)+A_p(2B_D B_{D-3}+2B_{D-1}B_{D-2})+6(c_{Cc}c_{Cc-3}+c_{Cc-1}c_{Cc-2})=0\).

**I4 jet of order \(k\)** (for \(0\le k<S=9m\)). Because \(Fce\) is
constant, \(Fce_{K-k}=0\). For \(k<S\) one has \(3D=9m=K-S<K-k\), and
also \(\deg d=V<K-k\), \(\deg B=D<K-k\), so the secondary summands
\(B^3\), \(\gamma d\), \(\varepsilon B\) do not reach degree \(K-k\).
Hence
\[
(Be+cd)_{K-k}=0.
\]
Named theorems: \(k=0\) (`top_resultant68`), \(k=1\) (`top_next68`),
\(k=2\) (`I4_next_two68`), \(k=3\) (`I4_third68`). The comments on
`I4NextTwo` and `TopNext` state this shortness is uniform, including on
the exceptional chart \((N,S)=(7,9)\).

**Input from the producing split.**
`third_companion_split68` on \(Fce_0\neq 0\) gives
\(A_{p-1}=A_{p-2}=A_{p-3}=0\). That is vanishing through \(k=3\), not
through \(k=D\) except on the chart \(m=1\) (where \(D=3\)).

**No other rows enter the matching.** Companion load algebra
(`third_load_algebra68`, `second_load_algebra68`) uses the same disc/I4
jets to cancel the *companion* polynomial; it is not an input to
matching. Remainders \(W_0,W_2\) likewise cancel in the companion, not
in \(\Delta\) or \(Be+cd\).

### 1.2 The recurrence (inductive step)

Set \(\lambda:=c_{Cc}/B_D\). This is legal: \(B_D\neq 0\) and, from the
cusp \(A_p B_D^2+3c_{Cc}^2=0\) with \(A_p\neq 0\), also \(c_{Cc}\neq 0\),
so \(\lambda\neq 0\) and \(A_p=-3\lambda^2\).

**Claim.** Suppose \(A_{p-j}=0\) for \(1\le j\le k\), \(\Delta_{U-j}=0\)
for \(0\le j\le k\), and \(c_{Cc-j}=\lambda B_{D-j}\) for \(0\le j<k\),
with the convention \(B_{D-j}=0\) when \(j>D\). Then
\(c_{Cc-k}=\lambda B_{D-k}\).

Proof. The terms of \(\Delta_{U-k}\) that involve \(A_{p-j}\) for
\(1\le j\le k\) vanish, leaving
\[
A_p(B^2)_{2D-k}+3\sum_{j=0}^{k}c_{Cc-j}c_{Cc-(k-j)}=0.
\]
Substitute \(A_p=-3\lambda^2\) and the inductive matching of \(c\) except
at \(j=k\):
\begin{align*}
A_p(B^2)_{2D-k}
&=-3\lambda^2\Bigl(2B_D B_{D-k}+\sum_{j=1}^{k-1}B_{D-j}B_{D-(k-j)}\Bigr),\\
3\sum_{j=0}^{k}c_{Cc-j}c_{Cc-(k-j)}
&=6\lambda B_D\,c_{Cc-k}+3\lambda^2\sum_{j=1}^{k-1}B_{D-j}B_{D-(k-j)}.
\end{align*}
The middle sums cancel, and \(B_D\neq 0\), \(\lambda\neq 0\) give
\(c_{Cc-k}=\lambda B_{D-k}\).

The same cancellation with I4, using the matching of \(c\) already
obtained and \(e_E=-\lambda d_V\) from the I4 top, yields
\(e_{E-k}=-\lambda d_{V-k}\), i.e.
\(B_D e_{E-k}+c_{Cc}d_{V-k}=0\).

This is the exact recurrence. It does not use a \((p-k)\) factor, does
not invert anything except \(B_D\) and \(\lambda\), and does not call
the companion.

### 1.3 Landed check for \(k=1,2,3\)

These are the prompt's identities, now computed from the named jets.

**\(k=1\).** Vanishing \(A_{p-1}=0\) in `discriminant_next68`:
\[
2A_p B_D B_{D-1}+6c_{Cc}c_{Cc-1}=0.
\]
Insert \(A_p=-3\lambda^2\), \(c_{Cc}=\lambda B_D\):
\(c_{Cc-1}=\lambda B_{D-1}\). Then `top_next68` collapses to
\(B_D e_{E-1}+c_{Cc}d_{V-1}=0\).

**\(k=2\).** Vanishing \(A_{p-1}=A_{p-2}=0\) in `discriminant_next_two68`:
\[
A_p(2B_D B_{D-2}+B_{D-1}^2)+3(2c_{Cc}c_{Cc-2}+c_{Cc-1}^2)=0.
\]
The \(B_{D-1}^2\) terms cancel after \(c_{Cc-1}=\lambda B_{D-1}\), leaving
\(c_{Cc-2}=\lambda B_{D-2}\). Then `I4_next_two68` collapses to
\(B_D e_{E-2}+c_{Cc}d_{V-2}=0\).

**\(k=3\).** Same cancellation in `discriminant_third68` / `I4_third68`.

Degree drops: coefficients of
\(c_{Cc}X^{Cc-D}B-B_D c\) in degrees \(Cc,Cc-1,Cc-2,Cc-3\) vanish, so
\[
\deg(c_{Cc}X^{N}B-B_D c)\le Cc-4,
\]
and likewise \(\deg(B_D e+c_{Cc}X^{N}d)\le E-4\). This matches the
prompt. UNVERIFIED that the Grok scratch packages exactly these
inequalities as
`FiveToSixCuspZetaFirstB3EqualitySupportQZeroVanishingAJetResidual68`;
the inequalities themselves are the matching through \(k=3\).

### 1.4 Side conditions, and the first \(k\) that breaks

| Condition | Holds through | First failure |
|---|---|---|
| \(B_D\neq 0\), \(\lambda\neq 0\) | all \(k\) | never, in this packet |
| Disc jet \(\Delta_{U-k}=0\) | \(k\le K_\Delta=4m\) | \(k=4m+1\): `hzero` no longer applies |
| Uncompensated I4 \((Be+cd)_{K-k}=0\) | \(k<S=9m\) | \(k=S\): \(B^3\) top \(3D=K-S\) enters |
| Naive index \(D-k\) as a `ℕ` | \(k\le D=3m\) | \(k=D+1\): Lean `D-k` wraps to \(0\); mathematically \(B_{D-k}=0\) is correct if one *defines* negative-degree coefficients as \(0\) |
| \(A_{p-k}\) exists | \(k\le p=14m\) | \(k=p+1\): automatic \(0\) |
| I4 compensation formula | \(k<S\) | \(k=S\): \((Be+cd)_{9m}=\tfrac19 B_D^3+\cdots\) |

The disc bound is the first one that actually stops the matching
recurrence: \(K_\Delta=4m<S=9m\), and \(K_\Delta=4m>D=3m\). So:

- Through \(k=D=3m\), every side condition holds (for \(m\ge 1\), \(D=3m\ge 3\)).
- For \(D<k\le K_\Delta\), matching remains valid with the convention
  \(B_{D-k}=0\), and concludes \(c_{Cc-k}=0\) (and the corresponding
  \(e\) statement with \(d_{V-k}=0\) when \(k>V\), which is not yet).
- At \(k=K_\Delta+1=4m+1\), a new input is required: either a longer
  vanishing interval of \(\Delta.\mathrm{reflect}\,U\), or an independent
  formula for \(\Delta_{U-k}\).

**I4 compensation does not degenerate on the matching interval.** It
degenerates at \(k=S=9m>K_\Delta\).

**Denominators in the companion/load algebra do not enter matching.**
The factors \((p-k)\), \((25P-28)/14\), \((25P-42)/7\) appear in
`second_load_algebra68` / `third_load_algebra68`, which cancel the
companion, not \(\Delta\). Clearing is by \(B_D^2\) or \(B_D^3\), both
nonzero. Those factors would matter for *producing* further vanishing
\(A\) rows (§4), not for matching from a granted vanishing row.

### 1.5 Answer to Question 1

Yes: the argument is uniform in \(k\) for
\[
1\le k\le K_\Delta=\min(S,7N-2G-S)=4N/7=4m,
\]
with \(B_{D-k}:=0\) for \(k>D\). It uses the order-\(k\) discriminant
jet (and, for the \(e/d\) family, the order-\(k\) uncompensated I4 jet),
the cusp and I4 tops, the vanishing rows \(A_{p-1},\ldots,A_{p-k}\), and
matching rows \(1,\ldots,k-1\). The first \(k\) at which the recurrence
as stated fails is \(k=4m+1\), where the reflected-discriminant window
ends.

---

## 2. Question 2: all-orders consequence

Grant vanishing \(A_{p-j}=0\) for \(1\le j\le K\), with
\(K\le K_\Delta\). Section 1 gives matching through that \(K\):
\[
c_{Cc}X^{Cc-D}B-B_D\,c
\quad\text{has vanishing coefficients in degrees }Cc,Cc-1,\ldots,Cc-K,
\]
hence
\begin{equation}
\deg\bigl(c_{Cc}\,X^{N}B-B_D\,c\bigr)\le Cc-K-1,\tag{\(\dagger\)}
\end{equation}
and
\begin{equation}
\deg\bigl(B_D e+c_{Cc}\,X^{N}d\bigr)\le E-K-1.\tag{\(\ddagger\)}
\end{equation}
Equivalently, with \(\lambda=c_{Cc}/B_D\),
\[
c=\lambda X^{N}B+r_c,\qquad
e=-\lambda X^{N}d+r_e,
\]
\(\deg r_c\le Cc-K-1\), \(\deg r_e\le E-K-1\).

This is **not** \(B\mid c\) up to the shift. Divisibility would require
\(r_c=0\). After matching through \(k=D\) one has only
\(\deg r_c\le Cc-D-1=N-1=7m-1\), and \(\deg B=3m\), so \(B\) need not
divide \(r_c\).

Special cases:

- Landed input \(K=3\): \((\dagger)\) is \(\deg\le Cc-4\), \((\ddagger)\)
  is \(\deg\le E-4\). This is the prompt's residual, for every \(m\ge 1\).
- Conditional \(K=D=3m\): \(\deg r_c\le 7m-1\), \(\deg r_e\le 12m-1\).
  On the chart \(m=1\), \(D=3=K_{\mathrm{landed}}\), so this case **is**
  landed: \(c=\lambda X^{7}B+r_c\) with \(\deg r_c\le 6\).
- Maximal disc window \(K=K_\Delta=4m\), if vanishing \(A\) were granted
  that far: matching through \(k=D\) plus \(c_{Cc-k}=0\) for
  \(D<k\le 4m\), i.e. \(c_j=0\) for \(6m\le j\le 7m-1\), hence
  \(\deg r_c\le 6m-1\). Still not \(r_c=0\).

The producing split does **not** grant \(K=D\) except at \(m=1\). For
\(m\ge 2\), \(D=3m\ge 6>3\). All-orders through \(k=D\) is therefore
conditional on further vanishing \(A\) rows. Those rows are not an
output of matching; they have to come from further companion reductions
(§4).

---

## 3. Question 3: endgame

### 3.1 What may be used

Exact identities valid in **this** chamber (\(Fce_0\neq 0\)):

1. Cusp top \(A_p B_D^2+3c_{Cc}^2=0\).
2. \(Fce=C(Fce_0)\) with \(Fce_0\neq 0\), i.e.
   \[
   Be+cd=\tfrac19 B^3-\tfrac32\gamma\,d-\tfrac34\varepsilon\,B+C(Fce_0).
   \]
   Right-hand side has degree \(9m\) and leading coefficient
   \(\tfrac19 B_D^3\neq 0\).
3. I4 top \(B_D e_E+c_{Cc}d_V=0\) and the quadratic resultant
   \(4B_D^2 c_{Cc}+9d_V^2=0\) (`top_resultant68`).
4. Reflected \(\Delta\) through order \(K_\Delta=4m\).
5. Landed matching \(k=1,2,3\), and the degree drops of §2.
6. `J:=Bc^2-\tfrac19 AB^3-3de` has `J.natDegree≤p` (used in
   `companion_next68`).

The terminal quotient
`fiveToSix_..._Fce_zero_terminal_quotient68` has explicit hypothesis
`hf : Fce.coeff 0 = 0`. It is the other branch of
`third_companion_split68`. **It does not apply.** In particular
\(2c+C(3\gamma)=Bv\) is not available, and neither are the Fce-zero
\(H\)-descent, \(U\)-profile, or square fibre.

### 3.2 The candidate contradiction, and why it does not fire

Rewrite I4 in remainder coordinates. Matching through order \(K\) gives
\(Be+cd=B r_e+r_c d\), so
\begin{equation}
B r_e+r_c d=\tfrac19 B^3-\tfrac32\gamma\,d-\tfrac34\varepsilon\,B+C(Fce_0).\tag{\(\ast\)}
\end{equation}
If \(r_c=r_e=0\), the left side is \(0\) and the right side has degree
\(9m\), leading \(\tfrac19 B_D^3\neq 0\). Both \(Z\neq 0\) and \(Z=0\)
in the sibling Fce-zero closure are of this shape: an exact identity
whose two degree cases are impossible. Here the zero-remainder case is
likewise impossible.

The remainder is not zero. With landed \(K=3\),
\(\deg r_c\le 10m-4\), \(\deg r_e\le 15m-4\), so the left side of
\((\ast)\) is allowed up to degree \(18m-4\); I4 constancy already cuts
it to degree \(9m\), which is consistent with the right side. No degree
comparison remains.

Even the conditional all-orders \(K=D\) leaves \(\deg r_c\le 7m-1\) and
\(\deg(B r_e+r_c d)\) still able to reach \(9m\). The maximal disc
window \(K=4m\) (unlanded vanishing \(A\)) still leaves
\(\deg r_c\le 6m-1\), \(\deg(r_c d)\le 14m-1\), not \(<9m\).

A leading-coefficient comparison of \(J\) at degree \(23m\) cancels
identically against \(3de\) by the quadratic resultant of
`top_resultant68` (computation in §3.3). That is consistency, not
`False`.

### 3.3 Top of \(J\), for the record

\[
(Bc^2-\tfrac19 AB^3)_{23m}=\tfrac43\lambda^2 B_D^3,
\qquad
(de)_{23m}=d_V e_E=-\lambda d_V^2,
\]
using matching at \(k=0\) only. Then
\[
J_{23m}=\tfrac43\lambda^2 B_D^3-3(-\lambda d_V^2)=\tfrac43\lambda^2 B_D^3+3\lambda d_V^2.
\]
Resultant \(4\lambda B_D^3+9d_V^2=0\) gives \(3\lambda d_V^2=-\tfrac43\lambda^2 B_D^3\), so
\(J_{23m}=0\). Compatible with `J.natDegree≤p=14m`. Not a contradiction.

### 3.4 Surviving residual

After the producing split and matching through \(k=3\):

- \(Fce=C(Fce_0)\) with \(Fce_0\neq 0\).
- \(A=A_p X^{p}+s\) with \(\deg s\le p-4=14m-4\).
- \(c=\lambda X^{N}B+r_c\) with \(\deg r_c\le Cc-4=10m-4\).
- \(e=-\lambda X^{N}d+r_e\) with \(\deg r_e\le E-4=15m-4\).
- \(\Delta_{U-k}=0\) for \(k=0,\ldots,4m\) still unused for \(k\ge 4\).
  The first unused coefficient, \(k=4\), is the linear relation
  \[
  A_{p-4}B_D+6\lambda\,(r_c)_{Cc-4}=0
  \]
  (same cancellation as §1.2, with the unmatched remainder of \(c\) at
  order \(4\)). This is one linear constraint on two unknown
  coefficients, not a kill.

This is a sharply smaller jet than the pre-matching packet, but it is
not a finite-dimensional family: \(s\), \(r_c\), \(r_e\), and \(d\)
retain high-dimensional spaces of coefficients, related by \((\ast)\)
and by the unused \(\Delta\) jets \(k=4,\ldots,4m\). Counting those
\(\Delta\) jets against the unmatched coefficients of \(s\) and \(r_c\)
is a further calculation; it is not done here and is not claimed to
close.

On the chart \(m=1\) the matching already runs through \(k=D=3\), and
the extra disc jet \(k=4=K_\Delta\) is the single relation
\(A_{10}B_D+6\lambda (r_c)_6=0\). Still no `False`.

### 3.5 Answer to Question 3

No contradiction. The sibling endgame identity \(2c+C(3\gamma)=Bv\) is
off-chamber. The identity that would close in the same style is
\((\ast)\) with \(r_c=r_e=0\), which is not landed. Residual as in §3.4.

---

## 4. Question 4 / producing split: what would extend vanishing \(A\)

Matching consumes vanishing \(A\) rows; it does not produce them. Further
vanishing \(A_{p-k}=0\) for \(k\ge 4\) has to come from further companion
reductions, in the pattern of `jet_rank68` / `companion_next_reduction68`
/ `companion_third_reduction68`:

- Companion at order \(k\) is the coefficient of `FullRowZero` at
  index \(2p-1-k\), after eliminating the \(J_{p-k}\) jet against
  `FullRowTwo`.
- Load of that companion lies in the localized ideal of disc jets
  \(0..k\) and I4 jets \(0..k\) (`second_load_algebra68`,
  `third_load_algebra68`); clearing is by \(B_D^{2}\) or \(B_D^{3}\).
- Remainder \(W_0,W_2\) at those indices: arithmetic split
  (`source_split68`) into the chart \((N,S)=(7,9)\) (explicit \(\gamma\)
  terms, cancelled in the companion resultant) and the chart \(14\le N\)
  (coefficients zero by degree). Higher-\(k\) remainder cancel is the
  same shortness once the index \(2p-1-k\) stays above
  \(\deg W_0\).
- On \(Fce_0\neq 0\) the reduced companion is a nonzero multiple of
  the order-\(k\) jet of \(A^2\):
  \(k=1\colon A_{p-1}\);
  \(k=2\colon 2A_p A_{p-2}+A_{p-1}^2\);
  \(k=3\colon A_p A_{p-3}+A_{p-1}A_{p-2}\).
  Previous vanishings then give \(A_{p-k}=0\).

This producing recurrence is **not** landed past \(k=3\). A uniform
extension through \(k=D\) would need, at each \(k=4,\ldots,3m\):

1. Disc jet \(k\) — available through \(k=4m\), so this is not the
   obstruction for \(k\le D\).
2. I4 jet \(k\) — available through \(k<9m\).
3. Remainder cancel at indices \(2p-1-k\) and \(p-1-k\) — not named
   past \(k=3\). This is the first missing input.
4. Load-algebra certificate at order \(k\) — not named past \(k=3\).
5. Nonvanishing of the numerical prefactor
   \((p-k)\cdots(p-1)\) — holds for \(k\le D=3m<p=14m\).

So if one asks where the *producing* recurrence (not the matching
recurrence) first requires new input, the answer is \(k=4\): a fourth
companion, a fourth remainder-cancel, and a fourth load certificate.
The disc/I4 jets for that step already exist as `hzero 4` and as
\(Fce_{K-4}=0\).

On \(m=1\), \(k=4\) is already past \(D=3\), so the producing split
through \(k=3\) has already fed matching through \(k=D\). The missing
\(k=4\) companion would be used only to kill \(A_{10}\) and then
\(r_c\) at degree \(6\), i.e. to shrink the \(m=1\) residual, not to
reach \(k=D\).

---

## 5. FALLACY-v2 checks

- No cv-flag / place / series identification.
- No exit-price, so no `charge_basis` line.
- Floor versus attainment: \(\deg\le Cc-4\) is an upper bound from three
  vanished coefficients, not exact degree. Not used as equality.
- Pole identities: none used. Vertex class not invoked.
- `sat()`: none.
- Terminal quotient consumed only as a hypothesis check (`hf: Fce_0=0`);
  not applied.
- Prime marks: none. Differentiation is the polynomial derivative, as
  in `coeff_derivative` in `companion_next68`.
- Gaps (producing split past \(k=3\); Grok scratch files; residual Prop
  name; defining `def` of \(\Delta\) and `hGS`) left open rather than
  filled by analogy.

---

## 6. Verdict

**PARTIAL.**

- Matching recurrence: derived, uniform through \(k\le 4m\), first break
  at \(k=4m+1\) (end of reflected \(\Delta\)).
- All-orders statement \((\dagger)\)-\((\ddagger)\): derived as a
  function of the vanishing depth \(K\). Landed only at \(K=3\) (and
  therefore at \(K=D\) only for \(m=1\)).
- Contradiction: not derived. The Fce-zero terminal quotient does not
  apply. The identity that would close is \((\ast)\) with zero
  remainders, which is not landed.
- New input needed to push vanishing \(A\) (hence matching) past
  \(k=3\): order-\(4\) companion, remainder-cancel, and load certificate.

UNVERIFIED items are labelled in §0 and at the residual Prop name.
