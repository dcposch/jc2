# max11 68 QZero/FceZero terminal branch, κ≠0 rigidity

**Verdict: DERIVED**

**Claim.** Over an algebraically closed field \(k\) of characteristic zero, the frozen polynomial system on the wall \(9N=7S\) (written \(N=7m\), \(m\ge 1\)) is inconsistent. The closing step is an exact degree comparison, not an evaluation at roots of \(B\), and it does not use the invalid inference \(B\mid X+C(c)\wedge\gcd(B,X)=1\implies B\mid C(c)\).

**Sources.** Lean theorems cited below were read from `jc2-lean` at `e84e32b` / handoff checkpoint `5a1bacc` (clone used for reading: the nested worktree is sandbox-blocked; content matches `origin/master`). Claims present only in the prompt and not in those files are labelled UNVERIFIED.

---

## 0. Notation and frozen input

Polynomials \(A,B,c,d,e,v,W,q,s,L\in k[X]\), scalars \(\alpha,\gamma,\varepsilon,\zeta=0,\eta,\mathrm{terminal},i_3,\kappa\). Write \(C_0:=81\varepsilon\gamma+27 i_3\) and \(v_0:=4\kappa/C_0\), \(\delta:=C_0/36\), \(c_1:=162\cdot\mathrm{terminal}/C_0\). Differentiation is the polynomial derivative in \(X\).

Kernel-checked in the cloned Lean sources, and used below:

- \(\deg B=3m\) exactly, leading coefficient \(B_D\neq 0\); \(B\) squarefree (`IsCoprime B (derivative B)`).
- \(\deg d=8m\) exactly, \(d_V\neq 0\); \(\deg v=7m\) exactly, \(v_N\neq 0\); \(\deg W=5m\) exactly, \(W_R\neq 0\).
- \(C_0\neq 0\), \(\mathrm{terminal}\neq 0\).
- \(W=4A+3v^2\) as an identity of polynomials.
- \(2c+C(3\gamma)=B\cdot v\).
- \(H:=4B^2 c+9d^2\) equals \(2B^3 v-6\gamma B^2+9d^2\) after the previous line.
- \(4H-C(C_0)=B\cdot T\) with \(\deg T=N-D=4m\) exactly, and the explicit formula
  \[
  T=2\bigl(3Wd+8B^2 v-21\gamma B\bigr).
  \]
  (Lean: `fiveToSix_zetaFirst_B3_equality_support_qZero_Fce_zero_terminal_H_quotient68`.)
- \(U:=3Wd+8B^2 v\) has \(\deg U=4m\) exactly.
  (Lean: `fiveToSix_zetaFirst_B3_equality_support_qZero_Fce_zero_terminal_U_profile68`.)
- \(\mathrm{IsCoprime}\,B\,d\), equivalently \(d(x)\neq 0\) at every root of \(B\).
  (Lean: `fiveToSix_pinned_terminal_row_forces_isCoprime_B_d68`, used in the root packet.)
- Leading identity \(B_D W_R=12\,d_V\).
  (Lean: `fiveToSix_zetaFirst_B3_equality_support_qZero_Fce_zero_terminal_W_profile68`.)
- Square fibre \(36d^2-C(C_0)=B\cdot s\) with \(\deg s=13m\).
  (Lean: `fiveToSix_zetaFirst_B3_equality_support_qZero_Fce_zero_terminal_square_fiber68`.)
- \(C_0\cdot v-C(4\kappa)=B\cdot q\) with \(\deg q=4m\).
  (Lean: `fiveToSix_zetaFirst_B3_equality_support_qZero_Fce_zero_terminal_v_descent68`.)

The prompt additionally lists a W′-congruence modulo \(B\), a bridge \(B\mid B'dL+C(108\cdot\mathrm{terminal})\), a κ=0 exclusion by root-count on \(B'\), and a coordinator-derived reduction of the W′ congruence. Those are not used in the closing argument. They are recorded in §5–§7 with verification status.

---

## 1. Closing identities (algebra, no roots)

Define
\[
F:=9d^2+2B^3 v,\qquad
Z:=BW-12d.
\]
Both are elements of \(k[X]\). Expand
\begin{align*}
BU-4F
&= B(3Wd+8B^2 v)-4(9d^2+2B^3 v)\\
&= 3BWd+8B^3 v-36d^2-8B^3 v\\
&= 3d(BW-12d)\\
&= 3d\,Z.
\end{align*}
This is an identity of polynomials, with no coprimeness, degree, or evaluation hypothesis. (Spot-checked on random integer polynomials of the frozen degrees.)

Rewrite \(H\) from \(2c+C(3\gamma)=Bv\). The definition \(H=4B^2 c+9d^2\) becomes
\[
c=\frac{1}{2}\bigl(Bv-C(3\gamma)\bigr),\qquad
4B^2 c=2B^3 v-6\gamma B^2,\qquad
H=2B^3 v-6\gamma B^2+9d^2.
\]
Hence
\[
4H=8B^3 v-24\gamma B^2+36d^2=4F-24\gamma B^2,
\]
or equivalently \(4F=4H+24\gamma B^2\).

The H-descent algebra (Lean `fiveToSix_qZero_Fce_zero_terminal_H_descent_algebra68`, packaged as the explicit quotient in `..._H_quotient68`) is the polynomial identity
\[
4H-C(C_0)=B\cdot 2\bigl(U-21\gamma B\bigr)=2BU-42\gamma B^2.
\]
Substitute into the previous display:
\[
4F=2BU-42\gamma B^2+C(C_0)+24\gamma B^2=2BU-18\gamma B^2+C(C_0).
\]
Therefore
\[
BU-4F=-BU+18\gamma B^2-C(C_0).
\]
Equating the two expressions for \(BU-4F\),
\begin{equation}
3d\,Z+BU-18\gamma B^2+C(C_0)=0.\tag{\(\ast\)}
\end{equation}
This is an identity in \(k[X]\) on the frozen system.

## 2. Degree comparison: both \(Z\neq 0\) and \(Z=0\) fail

The factors on the left of \((\ast)\) have exact degrees \(\deg d=8m\), \(\deg U=4m\), \(\deg B=3m\), so \(\deg(BU)=7m\). The remaining terms satisfy \(\deg(B^2)=6m\) and \(\deg C(C_0)\in\{0,-\infty\}\).

**If \(Z\neq 0\).** Then \(\deg(dZ)=8m+\deg Z\ge 8m>7m\), so \(3dZ\) strictly dominates \(BU\) and \(18\gamma B^2\). The left side of \((\ast)\) has degree at least \(8m\) and cannot be the zero polynomial.

**If \(Z=0\).** Then \((\ast)\) collapses to \(BU=18\gamma B^2-C(C_0)\). The right side has degree at most \(6m\) (or is a nonzero constant if \(\gamma=0\) and \(C_0\neq 0\); or is zero only if \(\gamma=0\) and \(C_0=0\), forbidden). The left side has degree \(7m\). Impossible.

(The case \(U=0\) is included: it would force \(\deg(BU)=-\infty\le 6m\), contradicting exact \(\deg U=4m\). Independently, \(U=0\) and coprimeness of \(B\) with \(d\) would give \(B^2\mid W\), hence \(W=0\) by \(\deg W=5m<6m\).)

Both cases are impossible. This is `False`.

No step evaluates a constant remainder and concludes that a coprime polynomial divides a nonzero constant. The comparison is the degree of an identity in \(k[X]\).

## 3. Equivalent coprimeness form (not needed, recorded)

If one stops after the \(Z\neq 0\) half and concludes only \(Z=0\), i.e. \(BW=12d\), then \(B\) divides \(d\). This already contradicts \(\mathrm{IsCoprime}\,B\,d\) (or, evaluating, \(d(x)=0\) at every root of \(B\)). The \(Z=0\) half of §2 is stronger: it contradicts exact \(\deg U=4m\) without coprimeness. The W-profile leading identity \(B_D W_R=12 d_V\) is the degree-\(8m\) shadow of \(Z=0\) and is consistent with, but weaker than, \(Z=0\).

---

## 4. Remarks on exactness

The argument uses that \(\deg U=4m\) and \(\deg d=8m\) are exact.

- The relation \(T=2(U-21\gamma B)\) is the definition of \(T\) in H-quotient. U-profile obtains \(\deg U=4m\) from \(\deg T=4m\) and \(\deg(21\gamma B)\le 3m<4m\). For \(\gamma=0\) one has \(T=2U\) and the comparison is \(-\infty<4m\).
- An upper bound \(\deg U\le 4m\) would already make \(\deg(BU)\le 7m\), which is all the \(Z\neq 0\) half needs. The \(Z=0\) half needs exactness (or at least \(\deg U>3m\)).
- The coefficient \(21\) in H-descent and the coefficient \(24\) in \(4H=4F-24\gamma B^2\) are not a bookkeeping mismatch: their difference is the explicit remainder \(18\gamma B^2\) in \((\ast)\). Replacing \(21\) by \(24\) would cancel that remainder and break the \(Z=0\) half; the Lean algebra theorem fixes the \(21\).
- The scalars \(v_0\), \(\kappa\), \(c_1\), and the W′ congruence are not used. The argument does not split on \(\kappa=0\) versus \(\kappa\neq 0\). (The prompt’s κ=0 exclusion is a strictly weaker, already-closed subcase.)

---

## 5. Coordinator-derived congruence (verified, unused)

The prompt asks to verify, before use,
\[
C_0\,d\,W'+36 v_0^2\delta\,B'W-\frac{288\delta}{v_0}B'd-C\Bigl(\frac{144 c_1\delta}{v_0}\Bigr)d\equiv 0\pmod{B},
\]
of degree \(13m-1\). This section records the algebra. The identity is not used in §1–§3.

**Input used here.** The prompt’s kernel-checked W′ congruence
\[
C_0 W'+6B'd\bigl(W^2+6v_0^2 W-72\gamma\bigr)\equiv 0\pmod{B},
\]
the square fibre \(d^2\equiv\delta\pmod{B}\), the evaluation \(v\equiv v_0\pmod{B}\), and the cleared bridge \(B'L+C(24c_1)d\equiv 0\pmod{B}\) with \(L=v(W^2-C(72\gamma))+48d\). (W′ congruence and bridge: UNVERIFIED as Lean theorems in the cloned HEAD; re-derived from the frozen *row* identities in §6.)

Multiply the W′ congruence by \(d\) and reduce \(d^2\equiv\delta\):
\[
C_0\,d\,W'+6\delta B'(W^2+6v_0^2 W-72\gamma)\equiv 0\pmod{B}.
\]
The bridge at roots of \(B\), with \(v(x)=v_0\neq 0\), rearranges to
\[
B'W^2\equiv 72\gamma\,B'-\frac{48}{v_0}B'd-\frac{24c_1}{v_0}d\pmod{B}.
\]
Substitute:
\begin{align*}
6\delta B'W^2
&\equiv 6\delta\Bigl(72\gamma B'-\frac{48}{v_0}B'd-\frac{24c_1}{v_0}d\Bigr)\\
&=432\delta\gamma B'-\frac{288\delta}{v_0}B'd-\frac{144 c_1\delta}{v_0}d.
\end{align*}
The terms \(\pm 432\delta\gamma B'\) cancel against \(-6\delta B'\cdot 72\gamma\), leaving exactly the displayed coordinator polynomial. Its naive top is \(C_0 d W'\) of degree \(8m+5m-1=13m-1\), leading coefficient \(5m C_0 d_V W_R\neq 0\).

Status: algebraically correct as a consequence of the listed congruences, assuming \(v_0\neq 0\). Unused.

---

## 6. Riccati / Möbius / Theorem A (does not close)

This is the prompt’s first candidate. It is recorded because the algebra is exact and shows why that route, by itself, does not produce `False`.

### 6.1 Reduction of row one to \(L\)

At a root \(x\) of \(B\), the frozen packet gives \(v(x)=v_0\), \(d(x)^2=\delta\), \(A(x)=(W(x)-3v_0^2)/4\), \(A'(x)=(2B'(x)+c_1)/v_0\) (from \(C_0(A'v-2B')=162\cdot\mathrm{terminal}\)), \(d'(x)=B'(x)W(x)/12\), \(q(x)=-6v_0 W(x)d(x)\), and \(v'(x)=B'(x)q(x)/C_0\). Substitute into the frozen row-one identity
\[
B'(AW-18\gamma)+6A'd-9dvv'-9d'v^2=0.
\]
The terms in \(v_0\) cancel, and one is left with
\[
B'(W^2-72\gamma)+24 A'd=0
\]
at \(x\). Inserting \(A'=(2B'+c_1)/v_0\) recovers
\[
B'L+24 c_1 d=0,\qquad L=v_0(W^2-72\gamma)+48d,
\]
which is the cleared bridge. So the bridge is not independent of the row packet. (UNVERIFIED as a Lean file; the handoff at `HANDOFF_2026-08-31.md` presents this as the next source-honest module after `5a1bacc`.)

### 6.2 W′ congruence from \(W=4A+3v^2\)

Differentiating \(W=4A+3v^2\) and evaluating at a root gives
\[
W'(x)=4A'(x)+6v_0 v'(x)=\frac{8B'(x)+4c_1}{v_0}-\frac{36 v_0^2 B' W d}{C_0}.
\]
The combination \(C_0 W'+6B'd(W^2+6v_0^2 W-72\gamma)\) then equals
\[
\frac{4C_0(2B'+c_1)}{v_0}-144\delta\frac{2B'+c_1}{v_0}
=\frac{2B'+c_1}{v_0}\bigl(4C_0-144\delta\bigr).
\]
With \(\delta=C_0/36\) one has \(144\delta=4C_0\), so the combination vanishes at every root of \(B\). Thus the W′ congruence is a consequence of the row packet plus \(W=4A+3v^2\), not a new global ODE. (UNVERIFIED as a Lean theorem.)

### 6.3 Möbius form, and why Theorem A does not apply

Set \(Y:=W+3v_0^2\) and \(a^2:=72\gamma+9v_0^4\). Completing the square,
\[
W^2+6v_0^2 W-72\gamma=Y^2-a^2.
\]
For \(a\neq 0\) the congruence becomes
\[
C_0 Y'\equiv -6B'd(Y-a)(Y+a)\pmod{B}.
\]
The Wronskian \(\mathrm{Wr}(Y-a,Y+a):=(Y-a)(Y+a)'-(Y-a)'(Y+a)\) equals \(-2a Y'\), so
\[
\mathrm{Wr}(Y-a,Y+a)-\frac{12a}{C_0}B'd(Y-a)(Y+a)
=-2a\cdot\frac{P}{C_0},
\]
where \(P:=C_0 Y'+6B'd(Y^2-a^2)\) is the polynomial of exact degree \(21m-1\) divisible by \(B\). The right-hand side is a nonzero multiple of \(B\), not a nonzero constant. Theorem A (`A C'-\nu A' C=c\neq 0` implies \(\deg A\le 1\); Lean `theorem-a/Solution.lean`) therefore does not apply: the identity is not a constant Wronskian.

Equivalently, if the ODE held *identically* (i.e. if \(P=0\) rather than \(B\mid P\)), the logarithmic derivative of \(\zeta:=(Y-a)/(Y+a)\) would equal \(\lambda B'd\) with \(\lambda=-12a/C_0\), a polynomial of degree \(11m-1\). Logarithmic derivatives of rational functions are proper. That forbids \(P=0\), but it does not forbid \(B\mid P\). Multiplicity counting of \(Y^2-a^2\) (degree \(10m\)) against the \(3m\) roots of \(B\) yields only \(2|S_+\cup S_-|\le 10m\), which is consistent.

The degenerate case \(a=0\) likewise gives double roots of \(Y\) at those roots of \(B\) where \(Y=0\), not a triple-root forcing from the first jet of the congruence alone. A triple-root claim needs a second differentiation plus an independent formula for \(Y''\); that was not pursued because §1–§3 already close the system.

The registered `GCD369WeightedWronskianLocal/Degree` theorems control \(2H'B-3HB'\) along a shifted Davenport–Stothers ODE \(c H^4(2H'B-3HB')=j B^8\). The present Riccati is not of that shape.

### 6.4 The κ=0 root-count, reconstructed

UNVERIFIED in the cloned Lean files (prompt: kernel-checked, new). Reconstruction, not used: if \(v_0=0\) then \(L\equiv 48d\pmod{B}\), so \(B'L+24c_1 d\equiv d(48B'+24c_1)\equiv 0\pmod{B}\). Since \(d(x)\neq 0\), one has \(B'(x)=-c_1/2\) at all \(3m\) roots of \(B\). Then \(B'+C(c_1/2)\) has \(3m\) roots and degree \(3m-1\), hence vanishes, so \(\deg B'=0\), contradicting \(3m-1\ge 2\). This is the “root-count on \(B'\)”. It is a specialisation of the same coprimeness/degree discipline as §3, not a replacement for it.

---

## 7. Remaining candidate routes

**Jet tower.** Differentiating the W′ congruence produces a finite jet in \((B',W,d)\) at roots of \(B\), but every first-order relation used to close the jet is already equivalent to the \(L\) identity or to \(q\equiv -6v_0 Wd\pmod{B}\). No polynomial of degree \(<3m\), constant on \(V(B)\), appears for \(\kappa\neq 0\) (the κ=0 case is the constant \(B'+c_1/2\)). Abandoned after §1–§3 closed.

**Pin \(\kappa\).** The row-two first integral (Lean: `fiveToSix_qZero_terminal_rowTwo_normal_algebra68`)
\[
-B^3 W+24 B^2 d+9\gamma B^2 v+6v H=C(6\kappa)
\]
evaluates at roots of \(B\) to \(6v_0\cdot(C_0/4)=6\kappa\), i.e. \(v_0=4\kappa/C_0\). That is the definition of \(v_0\), not a constraint forcing \(\kappa=0\). No further exact identity constraining \(\kappa\) was found in the landed `*FceZeroTerminal*` or `*RowTwoIntegral*` modules.

**Top-profile bookkeeping.** The chain \(B'L+C(24c_1)d=B\cdot M_1\) with \(\deg M_1=17m-1\) and \(\mathrm{top}(M_1)=3m\,v_N W_R^2\) is consistent with the exact degrees and with \(B_D W_R=12 d_V\). Leading cancellation in \(U\) and in \(s=T-8B^2 v+24\gamma B\) both reduce to \(9d_V^2+2B_D^3 v_N=0\), compatible with \(B_D W_R=12 d_V\). The contradiction is not a leading-coefficient mismatch. It is the exact identity \((\ast)\) of §1, whose two degree cases are both impossible. Route 4 of the prompt, executed as an exact identity rather than as a leading-coefficient comparison, is the argument of §1–§2.

---

## 8. What was not used, and what is not claimed

- The W′ congruence, the bridge, the coordinator-derived degree \(13m-1\) congruence, Riccati factorisation, Theorem A, and weighted-Wronskian local/degree theorems are not premises of the closing argument.
- No consistent polynomial model of the frozen system exists: \(Z\neq 0\) and \(Z=0\) are both forbidden by \((\ast)\) together with the exact degrees. A toy model with those degrees would have to violate H-descent, the identity \(BU-4F=3dZ\), or exact \(\deg U=4m\).
- Lean kernel-checking of *this* closing argument is not claimed. The input theorems listed in §0 are in the cloned sources; the identity \(BU-4F=3dZ\) and the degree comparison are paper mathematics.
- The invalid constant-divisor inference is not used.

---

## 9. Lean pointers

| Fact | File / theorem in `max11-partial-y/` |
|---|---|
| \(H=4B^2 c+9d^2\) | `...FceZeroHDegreeScratch.lean`, `FiveToSixQZeroFceZeroH68` |
| \(H=2B^3 v-6\gamma B^2+9d^2\) | `...TerminalVDescentScratch.lean` (conclusion of `..._v_descent68`) |
| \(4H-C(C_0)=BT\), \(\deg T=N-D\), \(T=2(3Wd+8B^2 v-21\gamma B)\) | `...TerminalHDescentScratch.lean`, `..._H_quotient68` |
| \(\deg U=N-D=4m\), \(U=3Wd+8B^2 v\) | `...TerminalUProfileScratch.lean`, `..._U_profile68` |
| \(B_D W_R=12 d_V\), \(\deg W=2N-S=5m\) | `...TerminalWProfileScratch.lean`, `..._W_profile68` |
| \(\mathrm{IsCoprime}\,B\,d\) | `...TerminalDivisorScratch.lean`, `..._forces_isCoprime_B_d68` |
| squarefree \(B\) | `...TerminalSquarefreeScratch.lean` |
| \(d(x)\neq 0\), \(B'(x)\neq 0\) at roots | `...TerminalRootPacketScratch.lean` |
| \(36d^2-C(C_0)=Bs\), \(\deg s=2D+N=13m\) | `...TerminalSquareFiberScratch.lean` |
| Theorem A | `jc2-lean/theorem-a/Solution.lean` |
| Weighted Wronskian (unused) | `gcd3-69-noncube/Solution.lean`, `GCD369WeightedWronskianLocal/Degree` |

Handoff stating the bridge as the next unlanded calculation: `max11-partial-y/HANDOFF_2026-08-31.md`, “68 lane: landed result and next algebra”.
