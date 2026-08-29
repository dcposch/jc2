# Sigray Proposition 5.4: the missing `q`-half from deck characters and the bracket equation

Date: 2026-08-28  
Status: **PROVISIONAL THEOREM — primary-source reconstruction, awaiting
different-model hostile review**  
Scope: the `q=p_{g,F}` half of Sigray Proposition 5.4 at
`F in T_{a,pole}`.  This does not prove Proposition 5.8, audit the later
Sections 7--9, supply a landing theorem, bound topological degree, or prove
JC2.

## 1. Verdict

The statement of Proposition 5.4 is correct on the normalized-counterexample
route, but its printed proof on p. 26 proves only the asserted form of
`p=p_F`.  The sentence "By (ii)" cannot prove either the zero of `q` in case
(i) or the absence of all wrong congruence classes in `q`.

The missing half follows from three already printed inputs:

1. at a pole vertex, Proposition 5.3(iii) and Proposition 4.6(11) give

   \[
     k_f p q'-k_g p'q=C,\qquad C\in\mathbf C^*;                 \tag{1.1}
   \]

2. Statement 3.16 and Proposition 5.3(iv),(v) give, for
   `nu=nu_F>=2`,

   \[
     p(\eta)=\eta^\epsilon P(\eta^\nu),\qquad
     \epsilon\in\{0,1\};                                      \tag{1.2}
   \]

3. writing `k_f=s alpha`, `k_g=s beta`, the normalized type satisfies
   `gcd(alpha,beta)=1` and `alpha>=2` (Notation 2.4 and Statement 2.1).

Decompose `q` into its `mu_nu` deck-character pieces.  Equation (1.1)
sends the piece of character `r` to character
`epsilon+r-1`.  The nonzero constant on the right has character zero, so
every component except `r=1-epsilon` solves the homogeneous equation

\[
  \alpha pR'-\beta p'R=0.                                    \tag{1.3}
\]

That homogeneous polynomial kernel is zero: at a simple root of `p`, a
nonzero solution `R` of vanishing order `m` would force
`alpha*m=beta`, impossible for coprime `alpha>=2` and `beta`.  Therefore
`q` has only the complementary character.  This gives exactly

\[
\begin{array}{c|c}
 p=P(\eta^\nu) & q=\eta Q(\eta^\nu),\\
 p=\eta P(\eta^\nu) & q=Q(\eta^\nu).
\end{array}                                                   \tag{1.4}
\]

Thus Proposition 5.4's full two-pattern conclusion is a theorem after
inserting the argument below.  No extra geometric or later-section premise
is needed.

## 2. Source-typed hypotheses

Fix a normalized counterexample `(f,g)` of type `(alpha,beta)` and a vertex
`F in T_{a,pole}` with `nu=nu_F != 1`.  Put

\[
  p=p_F,\qquad q=p_{g,F}.
\]

The following typing matters.

- Since `nu` is a positive integer, `nu!=1` means `nu>=2`.
- Proposition 5.3(iv) says `F in V_a`; its proof uses Statement 2.1 when it
  excludes a linear `p`.  Statement 3.16 therefore says both that `p` has
  more than one root and that its monomial degrees lie in one residue class
  modulo `nu`.
- Choose the exponent in Statement 3.16 canonically, by removing all powers
  of its variable from `P`.  Then it is `ord_0(p)`.  Proposition 5.3(v)
  makes `p` squarefree, hence this exponent is
  `epsilon in {0,1}` and (1.2) holds with `P(0)!=0`.
- Proposition 5.3(iii) has a suppressed nonzero scalar on its right.  At a
  pole vertex `m_F=0`, so Proposition 4.6(11) has right side
  `C*p^0=C`, `C!=0`.  This is (1.1), not a zero-bracket equation.
- Notation 2.4 gives `k_f/k_g=alpha/beta` in lowest terms.  Hence there is
  `s in N*` with `k_f=s alpha` and `k_g=s beta`; division of (1.1) by `s`
  gives

  \[
       L(q):=\alpha p q'-\beta p'q=c,\qquad c\in\mathbf C^*.  \tag{2.1}
  \]

This proof does **not** use the inverted ratio printed in Proposition
5.3(ii)/(viii).  It uses the coefficients `k_f,k_g` in Proposition 5.3(iii)
and the definition of type directly.  It also does not use Proposition
5.4 or Statement 5.2, so there is no circularity.

## 3. Deck-character decomposition

Let `zeta` be a primitive `nu`-th root of unity.  For
`r in Z/nu Z`, define the projector

\[
  q_r(\eta)=\frac1\nu\sum_{j=0}^{\nu-1}
       \zeta^{-rj}q(\zeta^j\eta).                              \tag{3.1}
\]

Then

\[
  q=\sum_{r\bmod\nu}q_r,\qquad
  q_r(\zeta\eta)=\zeta^r q_r(\eta).                            \tag{3.2}
\]

Equivalently, `q_r` is the sum of the monomials of `q` whose degrees are
congruent to `r` modulo `nu`.  From (1.2),

\[
 p(\zeta\eta)=\zeta^\epsilon p(\eta),\qquad
 p'(\zeta\eta)=\zeta^{\epsilon-1}p'(\eta),                    \tag{3.3}
\]

and similarly `q_r'` has character `r-1`.  Consequently

\[
  L(q_r)(\zeta\eta)
    =\zeta^{\epsilon+r-1}L(q_r)(\eta).                         \tag{3.4}
\]

Character decomposition in `C[eta]` is direct.  Since the right side of
(2.1) is a nonzero constant, (3.4) gives

\[
 \begin{cases}
   L(q_{1-\epsilon})=c,\\
   L(q_r)=0,&r\not\equiv1-\epsilon\pmod\nu.
 \end{cases}                                                   \tag{3.5}
\]

The only remaining issue is whether (2.1) has nonzero homogeneous
polynomial solutions in a wrong character.

## 4. The homogeneous kernel

### Lemma 4.1 (kernel vanishing at normalized type)

Let `p in C[eta]` be a nonconstant squarefree polynomial.  Let
`alpha,beta in N*` be coprime with `alpha>=2`.  Then

\[
   \alpha pR'-\beta p'R=0,\qquad R\in\mathbf C[\eta],          \tag{4.1}
\]

implies `R=0`.

**Proof.**  Suppose `R!=0` and choose a root `a` of `p`.  Squarefreeness
gives `p'(a)!=0`.  Evaluating (4.1) at `a` first gives `R(a)=0`.  Put
`m=ord_a(R)>=1`.  In the local parameter `t=eta-a`, write

\[
  p=A t+O(t^2),\qquad R=B t^m+O(t^{m+1}),\qquad AB\ne0.
\]

The coefficient of `t^m` in (4.1) is
`AB(alpha*m-beta)`.  Hence `alpha*m=beta`.  Since `m` is an integer and
`gcd(alpha,beta)=1`, this would imply `alpha=1`, a contradiction.  \(\square\)

This local proof is the exact place where the short repair uses the global
normal-form gate `alpha>=2`.  It needs only one simple root of `p`; the
source supplies more than one.

## 5. Repaired Proposition 5.4

### Theorem 5.1 (full pole-character pattern)

Under the hypotheses of Sigray Proposition 5.4, exactly one of the following
forms holds (the alternatives are distinguished by whether `p(0)` is zero):

\[
\begin{aligned}
 &p(\eta)=P(\eta^\nu),
 &&q(\eta)=\eta Q(\eta^\nu);                                  \tag{5.1}\
 &p(\eta)=\eta P(\eta^\nu),
 &&q(\eta)=Q(\eta^\nu).                                       \tag{5.2}
\end{aligned}
\]

**Proof.**  The source-typed argument in Section 2 gives (1.2) with
`epsilon=0` or `1`.  Sections 3--4 show that every component `q_r` with
`r!=1-epsilon` is zero.  If `epsilon=0`, all monomial degrees of `q` are
`1 mod nu`, so `q=eta Q(eta^nu)`.  If `epsilon=1`, all are `0 mod nu`, so
`q=Q(eta^nu)`.  These are (5.1) and (5.2).  \(\square\)

The theorem proves more than the missing assertion that `0` is a root of
`q` in case (5.1): it excludes every wrong nonzero deck character as well.

## 6. The `alpha=1` attack and sharp controls

The phrase in `ladder/SIGRAY-AUDIT.md` that the repair "load-bears on
`alpha>=2`" is correct for the source route, but it needs a scope
qualification.

### 6.1 A genuine mixing solution after removing the global gate

Take

\[
  \nu=3,\quad \alpha=1,\quad\beta=2,\quad
  p(\eta)=\eta,\quad q(\eta)=1+\eta^2.                          \tag{6.1}
\]

Then `p` and `q` are squarefree and coprime,
`deg p/deg q=alpha/beta`, and

\[
  p q'-2p'q=-2\ne0.                                           \tag{6.2}
\]

The polynomial `p` has character `1` modulo `3`, whereas `q` mixes
characters `0` and `2`; the conclusion (5.2) fails.  This is an exact
counterexample to any abstract q-half lemma that deletes `alpha>=2` while
retaining only the bracket, squarefreeness, coprimality and degree ratio.

It is **not** a counterexample to Proposition 5.4.  It has only one root of
`p`.  The source's Proposition 5.3(iv) plus Statement 3.16 requires more
than one root, and the proof of Proposition 5.3(iv) itself invokes Statement
2.1 precisely to rule out the linear case.  Thus (6.1) identifies the sharp
failure mode of the source chain rather than an admissible pole vertex.

### 6.2 If the vertex condition is imposed independently

For completeness, suppose `alpha=1` but independently retain that `p` is
squarefree of degree `n>=2`.  Then (2.1) has no polynomial solution at all.
Indeed its homogeneous polynomial kernel is `C p^beta`, because

\[
  \left(\frac{R}{p^\beta}\right)'
    =\frac{pR'-\beta p'R}{p^{\beta+1}}.                         \tag{6.3}
\]

If `q` solved (2.1), its top degree would be `beta*n`; subtract the unique
multiple of `p^beta` cancelling that top term.  The nonzero remainder `S`
would still solve `pS'-beta p'S=c`, but would have degree `m<beta*n`.
Its leading term in the left side has nonzero coefficient
`m-beta*n` and degree `n+m-1>=1`, impossible for a nonzero constant.

So the full vertex package does not acquire a hidden `alpha=1` mixing
family; rather, it becomes empty.  The explicit solution (6.1) is possible
exactly at the linear case that Statement 2.1 excludes upstream.  This
distinction should replace any unqualified claim that there are
`alpha=1` counterexamples satisfying every hypothesis of Proposition 5.4.

## 7. The auxiliary-`h` `kappa` rider

The newly discovered rider on Statement 3.9 does not create a gap in the
proof above.

- Sections 3--5 use only polynomials `p,q`, the deck action
  `eta -> zeta eta`, and the bracket equation.  They never invoke Statement
  3.9, compare a parent to `F*c`, or introduce a derived approximate root
  `h_j`.
- If one reconstructs the surrounding source in a common Kummer chart,
  choose at the outset one `K` divisible by: a fibre-suitable denominator,
  the denominator of `pi(F)`, and every pole order required by Proposition
  3.1 for the finite auxiliary family used here (`f-a` and `g`, or their
  squarefree factors).  Such a finite lcm exists.  Form `p` and `q` in that
  chart.  This makes every incidental Statement 3.9 use legal without
  changing the algebraic proof.
- A downstream tower containing further `h_j` must enlarge the common lcm
  to include those finitely many members before applying Statement 3.9 to
  them.  Proposition 5.4 itself supplies no license to omit that rider.

Thus the q-half is independent of the defect, while its integration record
should explicitly preserve the common-lcm policy.

## 8. Downstream consequence and firewalls

The repaired theorem licenses the exact congruences consumed by Statement
5.2(ii):

\[
\begin{array}{c|cc}
 &\deg p&\deg q\\ \hline
 (5.1)&0\pmod\nu&1\pmod\nu\\
 (5.2)&1\pmod\nu&0\pmod\nu.
\end{array}                                                   \tag{8.1}
\]

Combined separately with the corrected degree ratio
`deg p/deg q=alpha/beta`, these give the printed menu

\[
 \bigl(\nu\mid\alpha,\ \nu\mid\deg q-1\bigr)
 \quad\text{or}\quad
 \bigl(\nu\mid\beta,\ \nu\mid\deg p-1\bigr).                \tag{8.2}
\]

That downstream step is not part of the proof of Theorem 5.1.  In
particular:

- the corrected Proposition 5.3(ii)/(viii) ratio must still be used wherever
  orders, rather than the defining `k_f/k_g`, are invoked;
- Proposition 5.3(iii) is used only at `m_F=0`, so the repaired
  Proposition 4.2 recursion and its constant-corner terminal never enter;
- Proposition 5.1's finite-nonzero-puncture repair is separate: a member of
  `T_{a,pole}` comes from an actual `g`-pole, where the pole spine uses
  `b=0`;
- no assertion here proves realizability of a multiplicity datum, the pole
  mass identity, or any later decorated-tree propagation statement.

## 9. Reproduction

The standard-library checker is
`cases/sigray_prop54_qhalf_20260828/verify_qhalf.py`.  It performs exact
rational polynomial arithmetic and:

1. verifies four nonvacuous fixtures in both alternatives of (5.1)--(5.2);
2. checks character transport and zero homogeneous kernel on a grid of
   squarefree deck-character polynomials and coprime normalized types;
3. verifies the complete `alpha=1` homogeneous kernel and inconsistency at
   every tested degree-`>=2` vertex fixture;
4. verifies the sharp mixing control (6.1), including squarefreeness,
   coprimality, degree ratio and wrong character; and
5. mutates the positive fixtures with wrong-character monomials and checks
   that the constant-bracket identity breaks.

Run:

```sh
python3 cases/sigray_prop54_qhalf_20260828/verify_qhalf.py
```

Primary-source page and extraction-line custody is frozen separately in
`cases/sigray_prop54_qhalf_20260828/CUSTODY.md`.
