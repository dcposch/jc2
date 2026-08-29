# Sigray Proposition 4.2: the constant-shift repair closes the positive-tree recursion

Date: 2026-08-28  
Status: **PROVISIONAL THEOREM — exact paper proof, awaiting independent hostile review**  
Scope: Sigray Proposition 4.2 on `T_a^+`; no claim about Proposition 4.3 on
`T_a^-`, Proposition 5.1 at finite nonzero puncture values, landing, bounded
delay, a degree ceiling, or JC2.

## 1. Question and answer

`ladder/SIGRAY-AUDIT.md` correctly identifies the hole in the printed proof
on thesis pp. 19--20.  From

\[
 J(f_F^+,h_{j,F}^+)=0
\]

the proof seeks unique coprime `k_j,l_j in N*` with

\[
 (h_{j,F}^+)^{k_j}=s_j(f_F^+)^{l_j}.
\]

The assertion that `l_j != 0` because the global polynomial `h_j` is
nonconstant is invalid: its leading Laurent part can be a nonzero constant.

The proposed minimal repair is sound and complete:

\[
 h_{j,F}^+=c\in\mathbf C^*
 \quad\Longrightarrow\quad
 (k_j,l_j,s_j)=(1,0,c),\qquad h_{j+1}=h_j-c.       \tag{CS}
\]

After (CS), the new leading order is strictly negative and its leading
Jacobian with `f_F^+` is necessarily nonzero.  Thus (CS) is always the **last
step**: there is no second inverse/Laurent stuck case at a genuine Sigray
fiber flag.  The repaired recursion terminates, is unique, preserves the
terminal Jacobian formula, and supplies all approximate-root degrees needed
to define `M_F` and `Q(F)`.

An inverse stuck case is real in an abstract Laurent ring: `A=xi` and
`B=xi^(-1)` have zero two-variable Jacobian and `B=A^(-1)`, with no
positive-power cancellation.  It is excluded here by a load-bearing fact:
for `F in T_a^+`, the residual polynomial `p_F` has a root and is therefore
nonconstant.  The repair must not be exported to arbitrary Laurent charts
after forgetting that fiber-origin condition.

## 2. Local leading-form lemma

Fix `F in T_a^+`, put `u=pi(F)`, and choose a suitable denominator so all
orders below lie in one rational lattice.  In either the x- or y-chart write

\[
 f_F^+=\xi^d p(\eta),\qquad H_F^+=\xi^e q(\eta),             \tag{2.1}
\]

where `d=d_F>0` and `p,q` are nonzero polynomials.  Vanishing is unchanged
by the nonzero monomial factor relating the original Jacobian to the
`(xi,eta)` Jacobian.  Hence

\[
 J(f_F^+,H_F^+)=0
 \quad\Longleftrightarrow\quad
 d p q'-e p'q=0.                                           \tag{2.2}
\]

### Lemma 2.1 (the fiber residual is nonconstant)

`p` has a root, so `deg p >= 1`.

**Proof.** Represent `F=I_P(u)` by a Puiseux branch of `f=a`.  Along that
branch the residual variable tends to its next coefficient `gamma`.  Since
`f=a` is finite while `d>0`, the coefficient of the largest positive power
of `xi` must vanish: `p(gamma)=0`.  This argument is identical in the two
charts.  It is also the reason the abstract example `p=1` above is not a
Sigray `T_a^+` flag.  \(\square\)

### Lemma 2.2 (complete zero-bracket trichotomy)

Under (2.1), (2.2), and `deg p>=1`:

1. `e<0` is impossible;
2. if `e=0`, then `q` is a nonzero constant;
3. if `e>0`, there are unique coprime `k,l in N*` and unique `s in C*`
   such that `q^k=s p^l`, equivalently
   `(H_F^+)^k=s(f_F^+)^l`.

**Proof.** If `e=0`, (2.2) gives `dpq'=0`, hence `q` is constant.  If
`e<0`, choose a positive integer `N` clearing the denominators of `d,e` and
put `A=Nd>0`, `B=-Ne>0`.  Equation (2.2) says

\[
 A p q'+B p'q=0,
\]

so `(q^A p^B)'=0`.  Thus the product of two nonzero polynomials, one of
which (`p`) is nonconstant, would be a nonzero constant, a contradiction.
If `e>0`, logarithmic differentiation in (2.2), followed by reduction of
`e/d=l/k`, gives `q^k=s p^l`; unique factorization and
`gcd(k,l)=1` give uniqueness.  \(\square\)

This lemma is the missing one-line case split in the printed proof.  In
particular, negative-order inverse dependence is not merely unlikely: it is
algebraically impossible at a fiber flag.

## 3. Repaired Proposition 4.2

Equality below is understood up to the fixed nonzero scalar suppressed in
the thesis's Jacobian displays.

### Theorem 3.1 (positive-tree approximate roots with one allowed zero exponent)

Under the hypotheses of Sigray Proposition 4.2, there are unique data

\[
 h_0=g,\quad h_1,\ldots,h_m,\qquad
 (k_j,l_j,s_j)_{0\le j<m}
\]

such that

\[
 \gcd(k_j,l_j)=1,\qquad
 h_{j+1}=h_j^{k_j}-s_j f^{l_j},\qquad
 (h_{j,F}^+)^{k_j}=s_j(f_F^+)^{l_j},                \tag{3.1}
\]

where `k_j in N*`, `l_j in N`, and `s_j in C*`.  Every `l_j` is positive
except possibly `l_(m-1)`.  If a zero occurs, it occurs exactly once and

\[
 (k_{m-1},l_{m-1},s_{m-1})=(1,0,c),\quad
 h_{m-1,F}^+=c,\quad h_m=h_{m-1}-c,\quad d_{h_m,F}<0. \tag{3.2}
\]

With

\[
 \alpha_0=0,\qquad
 \alpha_{j+1}=\alpha_j+\frac{(k_j-1)l_j}{k_j},       \tag{3.3}
\]

the terminal formula remains

\[
 J(f_F^+,h_{m,F}^+)\doteq (f_F^+)^{\alpha_m}\xi^{-u}. \tag{3.4}
\]

In particular the recursion terminates after finitely many steps.

**Proof.** At a zero leading Jacobian, apply Lemma 2.2.  The positive-order
case is exactly the ordinary printed step.  The zero-order case has
`h_j^+=c in C*`; allowing `l=0` and imposing coprimality forces `k=1`, and
then (3.1) forces `s=c`.  Thus (CS) is unique.

The substitution defining `h_j^F` is injective after passing to the Laurent
extension.  Since `h_j` is a nonconstant polynomial, `h_j-c` is nonzero.
Removing its largest term leaves

\[
 (h_j-c)_F^+=\xi^e q(\eta),\qquad e<0.               \tag{3.5}
\]

Lemma 2.2 says its leading Jacobian with `f_F^+` cannot vanish.  Therefore
the next test is terminal and yields (3.4).  This proves, in particular, that
no negative-power successor is ever requested.

For termination, choose `kappa` as in the printed proof and set

\[
 \delta_j=\kappa(d_F+d_{h_j,F}-\alpha_jd_F-1+u)\in\mathbf N. \tag{3.6}
\]

For an ordinary step, (3.1) gives `k_j d_(h_j,F)=l_j d_F`, and cancellation
gives `d_(h_(j+1),F)<k_j d_(h_j,F)`, hence

\[
 \delta_{j+1}-\delta_j
 =\kappa\bigl(d_{h_{j+1},F}-k_jd_{h_j,F}\bigr)<0.    \tag{3.7}
\]

The same calculation applies to (CS): its right side is
`kappa*d_(h_(j+1),F)<0`.  More strongly, the nonzero leading Jacobian just
proved forces `delta_(j+1)=0`.  Thus positive integer descent either reaches
zero by ordinary steps or reaches a constant corner and then reaches zero in
one final step.

Finally,

\[
 J(f,h_{j+1})=k_jh_j^{k_j-1}J(f,h_j)
\]

and the zero step has `k_j=1`.  Hence every `h_j` remains nonconstant and
the usual chain-rule derivation of (3.4) is unchanged (including its harmless
nonzero scalar factors).  \(\square\)

### Exact defect drop

If the constant corner occurs at index `j`, write `mu=alpha_j` and
`e=d_(h_(j+1),F)<0`.  The terminal order equality gives

\[
 e=(\mu-1)d_F+1-u,\qquad
 \delta_j=-\kappa e>0,\qquad \delta_{j+1}=0.          \tag{3.8}
\]

So the shift does not merely preserve descent; it consumes the entire
remaining defect.

## 4. Degrees, `M_F`, and `Q(F)`

Let `a=deg p_F` and, in the constant-corner case, let

\[
 b=\deg p_{h_m,F},\qquad \mu=\alpha_m=\alpha_{m-1}.
\]

The inserted preterminal leading polynomial is constant, so

\[
 \deg p_{h_{m-1},F}=0,
 \qquad
 k_{m-1}\deg p_{h_{m-1},F}=l_{m-1}\deg p_F=0.       \tag{4.1}
\]

Thus the ordinary order and degree proportionality remains literally true
at the new step.  At the terminal member, write
`h_m^+=xi^e q(eta)`.  Equation (3.4) gives

\[
 d_F p q'-e p'q\doteq p^\mu.                         \tag{4.2}
\]

Because `d_F>0`, `e<0`, `a>=1`, and `b>=0`, the leading coefficient on the
left has factor `d_F*b-e*a>0`; it cannot cancel.  Comparing eta-degrees gives
the exact terminal-degree formula

\[
 \boxed{\ b=(\mu-1)a+1\ }.                           \tag{4.3}
\]

Consequently Sigray Notation 8.1 remains well-defined with the standard
convention `gcd(n,0)=n`.  If

\[
 M_F^*=\gcd(\deg p_F,\deg p_{h_0,F},\ldots,
                 \deg p_{h_{m-1},F}),
\]

then the new zero contributes nothing to that gcd and

\[
 \boxed{\ M_F=\gcd(M_F^*,(\mu-1)\deg p_F+1)\ }.       \tag{4.4}
\]

The other four slots of

\[
 Q(F)=(D_F,\deg p_F,\nu_F,M_F,\kappa_F(1-\pi(F)))     \tag{4.5}
\]

are unchanged.  Thus a compiler must not stop at the constant member and
set `M_F=M_F^*`: it must emit `h_m=h_(m-1)-c`, compute its degree, and use
(4.4).  All approximate-root degrees at every ancestor remain required by
the typed source/landing contract.

The algebra in Sigray Proposition 8.1 is unaffected on its stated
`T_a^searrow` domain: the new relation has `l/k=0`, contributes degree zero,
and contributes zero to `mu`.  In fact the next section shows the exceptional
step cannot occur on that domain at all.

## 5. Location: the constant corner is necessarily `T_a^nearrow`

Combining (3.8) and (4.3) yields

\[
 b-\frac e{d_F}a
 =1-\frac{(1-u)a}{d_F}.                                \tag{5.1}
\]

The left side is strictly positive because `b>=0`, `e<0`, `d_F>0`, and
`a>=1`.  Therefore

\[
 \boxed{\ d_F>(1-u)\deg p_F\ },                       \tag{5.2}
\]

which is exactly `F in T_a^nearrow` (Sigray Notation 6.1).  Hence:

- a constant-leading step cannot occur in `T_a^searrow`;
- it cannot occur on the characteristic sequence from a pole vertex to
  `(0,y)`, whose vertices are the `T_a^searrow` vertices used by Statements
  9.4--9.5 and Proposition 9.3;
- pole vertices themselves still have `m_F=0`, so
  `M_F=gcd(deg p_F,deg p_(g,F))` and every pole-entry formula is unchanged.

This turns the landing documents' empirical/nonconstant-top guard into a
theorem for positive-side pole-spanned characteristic paths.  The repair is
not merely a pole-path repair, however: Theorem 3.1 closes Proposition 4.2
at every `T_a^+` flag.  The exceptional step lives precisely in the
finite-valued/`T_a^nearrow` sector.

## 6. Contract consequences and remaining firewalls

1. **Positive tower schema.** A general positive-tree emitter may allow
   `l_j=0` only in the normalized form `(k,l,s)=(1,0,c)`, only as the final
   step.  The existing normalized jet row (T2) then becomes the exact linear
   identity for `h_j-c`; no inverse of `f` is introduced.
2. **Pole-spanned source contract.** On the `T_a^searrow` characteristic
   paths used to form the Sigray pole book, `l_j>0` follows from (5.2).
   Existing concrete towers that certified nonconstant tops do not change.
3. **Ancestor labels.** If a future full positive-tree compiler enters a
   `T_a^nearrow` constant corner, it must retain the final shifted member and
   degree (4.3); otherwise its `M_F` and `Q(F)` can be wrong.
4. **No Proposition 4.3 promotion.** The `T_a^-` tower uses `g-b` and
   `f-a` and retains condition (7).  Nothing here removes that gate.
5. **No Proposition 5.1 promotion.** The separate finite-puncture defect in
   the printed `b=0` threshold argument remains.  Giving Proposition 4.2 a
   finite tower does not prove the claimed threshold or a full-boundary
   landing theorem.
6. **No coverage consequence.** The two-chart/all-root constructor,
   gluing, later Sigray source repairs, bounded delay, and cofinal degree
   ceiling remain separate obligations.

## 7. Audit verdict

The Proposition 4.2 entry in `SIGRAY-AUDIT.md` can, after independent review,
be upgraded from `GAP` to **ERRATUM WITH COMPLETE REPAIR**:

- replace `l_j in N*` by `l_j in N`;
- permit `l_j=0` only in the unique terminal constant-shift form (3.2);
- retain the printed recursion and `alpha/delta` formulas unchanged;
- record (4.3)--(4.4) for the terminal degree and `M_F`;
- record the scope theorem (5.2), which proves that the printed positive-
  exponent version was already sufficient on pole characteristic paths.

No computation, external web source, or unpinned reference is used.  The
proof was checked directly against `refs/sigray_full.pdf` pp. 18--21,
`ladder/SIGRAY-AUDIT.md`, `xmodel/sol-landing1.md`, and
`xmodel/sol-gluing-design.md`.  No file under `jc2-lean` was accessed.
