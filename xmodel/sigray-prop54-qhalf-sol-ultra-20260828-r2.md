# Sigray Proposition 5.4, repaired: pole degree pin plus the missing `q`-half

Date: 2026-08-28  
Status: **PROVISIONAL REPAIRED THEOREM — R1 core confirmed by Opus 5;
source-typing repair independently tightened here**  
Scope: Proposition 5.3(iv)'s missing linear/constant branch and Proposition
5.4's missing `q=p_{g,F}` half.  No claim about Proposition 5.8, Sections
7--9 as a whole, landing, a degree ceiling, or JC2.

Frozen predecessor and hostile review:

```text
f2ee74b5c8f07048488c3b78e5f76bc293beae4b7199614ce75b8e1c18165f75  xmodel/sigray-prop54-qhalf-sol-ultra-20260828.md
c3f0bfde24fb265e6ece9fce40089868fd64b01b3f6f5eac3ef0ee5df43e1f30  xmodel/sigray-prop54-qhalf-hostile-review-opus5-20260828-r1.md
```

The review verdict is `REPAIR`, not because the deck-character proof fails,
but because R1 inherited an incomplete printed proof of Proposition 5.3(iv).
This file supplies the missing degree pin first and then gives a standalone
proof of Proposition 5.4.

## 1. Exact source defect found by hostile review

At a pole vertex put `p=p_F`, `q=p_{g,F}`.  Proposition 5.3(iii) literally
states

\[
  k_f p q'-k_g p'q=C,\qquad C\in\mathbf C^*,                 \tag{1.1}
\]

where the suppressed glyph is defined by Notation 1.1 on p. 4 to mean an
unspecified nonzero complex constant.

The printed proof of Proposition 5.3(iv) says that if `p` does not have more
than one root, then `p` is linear and (1.1) forces `k_g/k_f` to be an integer.
This omits the branch `deg q=0`.  Indeed, for every positive coprime
`alpha,beta`,

\[
  p=A(\eta-a),\qquad q=B\ne0
  \quad\Longrightarrow\quad
  \alpha p q'-\beta p'q=-\beta AB\in\mathbf C^*.             \tag{1.2}
\]

This is exactly Proposition 4.6(17)'s alternative at `mu_F=0`:
`deg p+deg q-1=0`.  Thus the bracket alone does not prove
Proposition 5.3(iv), even when `alpha>=2`.

## 2. The missing pole degree pin

### Lemma 2.1 (degree transport at a pole threshold)

Let `(f,g)` be a normalized counterexample of type `(alpha,beta)` and let
`F=I_P(u) in T_{a,pole}`.  Then

\[
 \alpha\deg p_{g,F}=\beta\deg p_F,                            \tag{2.1}
\]

and consequently

\[
  \deg p_F\in\alpha\mathbf N^*,\qquad
  \deg p_{g,F}\in\beta\mathbf N^*,\qquad
  \deg p_F\ge\alpha\ge2.                                    \tag{2.2}
\]

**Proof.**  By Proposition 5.3(i), `F` is neither axis vertex, so `u>0`.
Choose one integer `K` which

1. is suitable for the fixed fibre chart;
2. has `Ku in N`; and
3. is a multiple of all pole orders required by Proposition 3.1 for the
   finite auxiliary family `{f-a,g}` (or their squarefree factors).

This is the explicit auxiliary-`h` common-lcm rider required by Statement
3.9.  Enlarge `K` further if necessary; `Ku>=1`.  Set

\[
  G=I_P(u-1/K).
\]

The chosen Puiseux branch itself supplies its next coefficient `c`, so
`F=G*c` in Notation 3.8.  This does **not** require `G=F^circ` and does not
invoke Proposition 3.2's vertex-predecessor notation.  Statement 3.18 gives
that `c` is a root of `p_G`.  Statement 3.9(i), legally applied with the
common `K` to `h=f-a` and `h=g`, gives the next display.  For the first
equality, use the positivity verified immediately below: at `G` and `F`, the
leading polynomials of `f-a` equal those of `f`.

\[
 \deg p_F=\operatorname{mult}(p_G,c)\ge1,qquad
 \deg p_{g,F}=\operatorname{mult}(p_{g,G},c).                 \tag{2.3}
\]

Since `u-1/K<u`, Proposition 5.1(ii) gives `m_G>0`.  Statement 3.10(i)
says explicitly that `v -> d_{h,I_P(v)}` is monotone decreasing for every
polynomial `h`.  Apply it to `h=f` and `h=g`.  Because `G` is at the earlier
parameter `u-1/K`,

\[
  d_G\ge d_F>0,\qquad d_{g,G}\ge d_{g,F}>0.                 \tag{2.4}
\]

Here `d_F>0` follows from `F in T_{a,pole}\subset T_a^+`, and `d_{g,F}>0`
is Proposition 5.3(ii).  Thus `G in T_a^+`.  Hence the first Proposition
4.2 relation at `G` is an ordinary positive-exponent step, not a constant
corner:

\[
   (g_G^+)^{k_0}=s_0(f_G^+)^{l_0},qquad k_0,l_0\in\mathbf N^*.
                                                                    \tag{2.5}
\]

The pre-threshold comparison already printed in the proof of Proposition
5.3(ii), using Propositions 4.4--4.5 and the normalized Newton top, gives
`k_0/l_0=k_f/k_g=alpha/beta`.  Coprimality therefore gives

\[
  (k_0,l_0)=(\alpha,\beta).                                  \tag{2.6}
\]

Comparing the residual `eta`-polynomials in (2.5),

\[
  p_{g,G}^{\alpha}=s_0p_G^\beta.                              \tag{2.7}
\]

Taking the multiplicity at `c` and using (2.3) yields (2.1).  Since
`gcd(alpha,beta)=1`, (2.1) implies `alpha | deg p_F`; (2.3) makes that
degree positive, and Statement 2.1 gives `alpha>=2`.  This proves (2.2).
\(\square\)

### Consequences

Because Proposition 5.3(v) makes `p_F` squarefree, (2.2) says it has at
least two distinct complex roots.  Statement 3.16 now proves
`F in V_a`, completing Proposition 5.3(iv) without the printed
linear/constant gap.  Lemma 2.1 also proves the degree half of Statement
5.2(i) without Proposition 5.3(vii).

The proof does not need Proposition 4.2's constant-corner terminal formula:
`d_{g,G}>0` in (2.4) excludes that branch from (2.5).  It does use the ordinary first
relation of Proposition 4.2 at the immediate pre-threshold flag.  This is the
precise firewall; saying that Proposition 4.2 never enters would be false.

## 3. The pole-character form of `p`

Assume now `nu=nu_F!=1`, hence `nu>=2`.  Proposition 5.3(i), repaired (iv),
and Statement 3.16 give

\[
  p(\eta)=\eta^lP_0(\eta^\nu).
\]

Remove all powers of the variable from `P_0`, so that the displayed
exponent is `ord_0(p)`.  Proposition 5.3(v) makes `p` squarefree, hence

\[
  p(\eta)=\eta^\epsilon P(\eta^\nu),qquad
  \epsilon\in\{0,1\},\quad P(0)\ne0.                          \tag{3.1}
\]

Let `k_f=s alpha`, `k_g=s beta`, as licensed by Notation 2.4.  Dividing
(1.1) by `s` gives

\[
  L(q):=\alpha p q'-\beta p'q=c,qquad c\in\mathbf C^*.       \tag{3.2}
\]

This uses Proposition 5.3(iii) as printed.  If instead one reconstructs it
from Proposition 4.6(11), one must use the **corrected** order ratio
`d_{g,F}=(k_g/k_f)d_F`; R1's claim that the reconstruction avoids the
inverted Proposition 5.3(ii) was too broad.

## 4. Deck characters force the `q`-half

Let `zeta` be a primitive `nu`-th root of unity and define

\[
  q_r(\eta)=\frac1\nu\sum_{j=0}^{\nu-1}
      \zeta^{-rj}q(\zeta^j\eta),\qquad r\in\mathbf Z/\nu.     \tag{4.1}
\]

Then `q=sum_r q_r` and `q_r(zeta eta)=zeta^r q_r(eta)`.  From (3.1),
`p` has character `epsilon` and `p'` has character `epsilon-1`; similarly
`q_r'` has character `r-1`.  Therefore

\[
 L(q_r)(\zeta\eta)=\zeta^{\epsilon+r-1}L(q_r)(\eta).          \tag{4.2}
\]

The character decomposition of `C[eta]` is direct, and the nonzero constant
in (3.2) has character zero.  Thus

\[
 L(q_{1-\epsilon})=c,qquad
 L(q_r)=0\quad(r\not\equiv1-\epsilon\pmod\nu).                \tag{4.3}
\]

### Lemma 4.1 (zero homogeneous polynomial kernel)

For the coprime normalized type with `alpha>=2`,

\[
  \alpha pR'-\beta p'R=0,\quad R\in\mathbf C[\eta]
  \quad\Longrightarrow\quad R=0.                             \tag{4.4}
\]

**Proof.**  If `R!=0`, choose a simple root `a` of the nonconstant
squarefree polynomial `p`.  Evaluation of (4.4) gives `R(a)=0`.  If
`m=ord_a(R)>=1`, write locally
`p=A(eta-a)+...`, `R=B(eta-a)^m+...`, with `AB!=0`.  The coefficient of
`(eta-a)^m` in (4.4) is `AB(alpha*m-beta)`.  Hence
`alpha*m=beta`, impossible for coprime `alpha>=2,beta`.  \(\square\)

Applying Lemma 4.1 in (4.3), every wrong component vanishes.  Therefore

\[
\begin{array}{c|c}
 p(\eta)=P(\eta^\nu)&q(\eta)=\eta Q(\eta^\nu),\\
 p(\eta)=\eta P(\eta^\nu)&q(\eta)=Q(\eta^\nu).
\end{array}                                                   \tag{4.5}
\]

This is the complete statement of Proposition 5.4, including its omitted
`q`-half.

## 5. Sharp `alpha=1` control

Deleting the normalized gate admits the exact mixer

\[
 (\nu,\alpha,\beta,p,q)=(3,1,2,\eta,1+\eta^2),qquad
 pq'-2p'q=-2.                                                 \tag{5.1}
\]

It has squarefree coprime `p,q` and the correct degree ratio, but `p` has
character `1` while `q` mixes characters `0,2`.  It fails precisely the pole
degree pin: `deg p=1`.

More exactly, for `alpha=1` and linear `p=A(eta-a)`, all solutions are

\[
 q=-\frac{c}{\beta A}+\lambda p^\beta.                        \tag{5.2}
\]

For `deg p=n>=2`, no polynomial solution exists.  Indeed the leading
coefficient of `p q'-beta p'q` is proportional to
`deg(q)-beta*n`; if it does not vanish the result has positive degree.  If
it vanishes, subtract the unique multiple of `p^beta` cancelling the top
term.  The nonzero lower-degree remainder still has the same nonzero
constant bracket, where its leading term cannot cancel, a contradiction.

Accordingly, the audit phrase "for alpha=1 genuine counterexample solutions
exist" must be qualified: they are counterexamples to the abstract bracket
lemma exactly on the linear branch, not counterexamples satisfying the
repaired pole-vertex degree pin.

## 6. Downstream typing

The two patterns give

\[
\begin{array}{c|cc}
 &\deg p&\deg q\\ \hline
 \epsilon=0&0\pmod\nu&1\pmod\nu,\\
 \epsilon=1&1\pmod\nu&0\pmod\nu.
\end{array}                                                   \tag{6.1}
\]

Together with Lemma 2.1's ratio, case `epsilon=0` has
`nu | deg p` and `gcd(nu,deg q)=1`, so
`nu | beta deg p=alpha deg q` implies `nu|alpha`.  The other case gives
`nu|beta` symmetrically.  Hence the exact Statement 5.2(ii) menu is

\[
 (\nu\mid\alpha,\ \nu\mid\deg q-1)
 \quad\text{or}\quad
 (\nu\mid\beta,\ \nu\mid\deg p-1).                          \tag{6.2}
\]

This supplies exactly the inputs used by TDUNIFORM R2, AF3's
type-`(3,5)`, `nu=5` parity pin, and the beta-minimal/prime-pole arithmetic
in `SHEET6-MULTIPOLE.md`.  It does not make the menu sufficient for
realizability.

There is one additional source erratum: Statement 5.2(i) prints
`D_{g,F}/D_F=alpha/beta`.  The correct middle term is

\[
  D_F/D_{g,F}=\alpha/\beta,
  \qquad D_{g,F}/D_F=\beta/\alpha.                            \tag{6.3}
\]

The campaign's consumers already use (6.3).  Proposition 5.8 and every
later landing/propagation obligation remain separate.

## 7. Exact controls

The frozen R1 checker still passes 1,788 grouped assertions.  The R2 checker
`cases/sigray_prop54_qhalf_20260828/verify_degree_pin_r2.py` adds:

- exact pre-threshold multiplicity/degree transport controls;
- the linear/constant bracket counterbranch (1.2);
- the full linear `alpha=1` family (5.2); and
- a two-deck-orbit nonconstant solution, independent of every R1 fixture:

\[
\begin{aligned}
 p&=\eta^4+A\eta^2+A^2/8,\\
 q&=\eta^5+(5A/4)\eta^3+(5A^2/16)\eta,\\
 4pq'-5p'q&=5A^4/32.
\end{aligned}                                                  \tag{7.1}
\]

At `A!=0`, `p` has two distinct nonzero `nu=2` deck orbits and the predicted
complementary characters.
