# Cyclic semi-invariance repair for Sigray Statement 8.5

**Date:** 2026-08-28  
**Producer:** coordinator (Sol Ultra)  
**Primary source:** Sigray, printed pp. 10--13, 17, 19--23, 42--43

## Verdict

The printed inference

\[
p_G(\eta)=\widetilde p(\eta^\nu)
\quad\Longrightarrow\quad
p_{h,G}(\eta)=\eta r(\eta^\nu)
\]

does **not** follow from Proposition 4.6 alone.  It is nevertheless correct
for `nu > 1` after adding the cyclic semi-invariance lemma below.  For
`nu=1`, the only needed conclusion, `gcd(nu,deg p_{h,G})=1`, is automatic.
Thus Statement 8.5 is **repairable with a new elementary lemma**, and its
divisibility conclusion survives.

The residue-class decomposition proposed in
`xmodel/sigray-section8-full-hostile-review-opus5-20260828.md` Section 3.3 is
insufficient by itself: the homogeneous ODE can in principle contribute a
grade-zero term `C p^(d_h/d)`.  Semi-invariance, not the degree comparison in
that review, is the clean mechanism excluding a mixture of grades.

## 1. General cyclic semi-invariance lemma

Consider the `y`-side.  Let a branch realizing a
characteristic vertex `F=I_P(beta_j/kappa)` have Puiseux expansion

\[
x=t^{-\kappa},\qquad y=\sum_{r\geq0}c_rt^r,
\]

and characteristic gcds `e_0=kappa`,
`e_i=gcd(e_{i-1},beta_i)`.  Put

\[
e=e_{j-1},\qquad e'=e_j,\qquad \nu=e/e',\qquad
\phi(t)=\sum_{r<\beta_j}c_rt^r.
\]

By Definition 3.1, every `r<beta_j` with `c_r != 0` is divisible by
`e`: `beta_j` is the first supported exponent not divisible by `e`.
Consequently `phi(zeta t)=phi(t)` for every `zeta` in `mu_e`.

For an arbitrary polynomial `a(x,y)`, set

\[
A(t,\eta)=a(t^{-\kappa},\phi(t)+t^{\beta_j}\eta)
          =\sum_n t^n A_n(\eta).
\]

This is exactly the chart underlying Notations 3.9--3.10.  Since
`e | kappa` and `phi(zeta t)=phi(t)`, direct substitution gives

\[
A(\zeta t,\zeta^{-\beta_j}\eta)=A(t,\eta).
\]

Hence, coefficient by coefficient,

\[
A_n(\zeta^{-\beta_j}\eta)=\zeta^{-n}A_n(\eta). \tag{CS}
\]

Take `zeta` primitive of order `e`.  Then
`omega=zeta^(-beta_j)` has order
`e/gcd(e,beta_j)=e/e'=nu`.  If `A_n` is nonzero, (CS), also applied to
the kernel of `zeta -> zeta^(-beta_j)`, first forces `e' | n`; it then
says that all monomials of `A_n` have one and the same degree modulo
`nu`.  Equivalently, for a uniquely determined `s in {0,...,nu-1}`,

\[
A_n(\eta)=\eta^s R_n(\eta^\nu). \tag{CSI}
\]

In particular, the leading coefficient polynomial `p_{a,F}` selected by
Notation 3.10 is one such `A_n`, and therefore satisfies (CSI).  This is
valid for **every** polynomial `a`, not only for `f`.  No resolution theorem
or Jacobian hypothesis enters.

On the `x`-side take instead
`y=t^(-kappa)`, `x=phi(t)+t^(beta_j)eta`.  The same substitution gives
`A(zeta t,zeta^(-beta_j)eta)=A(t,eta)`, with the same coefficient character;
thus the proof is literally identical on that component.

Remarks on typing:

1. The truncated sum is finite below the fixed exponent `beta_j`, so the
   coefficient comparison is formal and harmless.
2. Under a synchronized denominator refinement `kappa'=L kappa`, put
   `t=(t')^L`.  Then `beta_j`, `e`, and every selected Laurent exponent `n`
   all scale by `L`, so `e/gcd(e,beta_j)`, the effective action, and (CSI)
   are unchanged.
3. Statement 3.16 records the corresponding shape only for `p_F=p_{f,F}`;
   it is not, by itself, a citation for the general lemma above.

## 2. Application to Statement 8.5

Use the notation of the printed proof.  If `nu_G=1`, then
`gcd(nu_G,deg p_{h,G})=1` is immediate, and no eta-factor claim is needed.

Assume `nu=nu_G>1`.  Then `G` is a characteristic vertex.  Statement 3.16
puts the roots of `p_G` into zero plus nonzero effective `mu_nu`-orbits.  A
second nonzero orbit, or zero together with a nonzero orbit, gives by
Statement 3.18 two realized branches whose first distinct coefficient is at
`pi(G)`; Definition 3.4 would then put `G` in `V_{2,a}`.  Only the zero orbit
would make `p_G` single-rooted, contradicting Statement 3.16 because
`G in V_{1,a}`.  Therefore exactly one nonzero orbit occurs, with one common
multiplicity, and

\[
p=p_G=C(\eta^\nu-c^\nu)^l,
\qquad C,c\ne0.
\]

The scalar is harmless and `p(omega eta)=p(eta)` for `omega in mu_nu`.

The ODE packet is also correctly typed.  Here `F in T_a^&` means
`F in T_a^+`.  Write `u=pi(F)>v=pi(G)` and `F=G+c`.  Statement 3.17 gives

\[
d_G=d_F+(u-v)\deg p_F>0,
\]

so, noncircularly, `G in T_a^+`.  Proposition 4.2 then defines its terminal
polynomial `h_G=h_(m_G,G)` with `h_0=g`; Corollary 6.1 and tower persistence
identify the packet used in Statement 8.5.  The promoted corrected
Proposition 4.2 package (`10bc55d5...`, hostile review `47f2b608...`) supplies
the repaired condition-(7) premise on `T_a^+`; the circular printed remark
is not used.  Proposition 4.6 therefore applies to this exact terminal
packet.  Apply the lemma to `h=h_G`: for some residue `s`,

\[
q=p_{h,G},\qquad q(\omega\eta)=\omega^s q(\eta).
\]

Proposition 4.6 gives the nonzero polynomial identity

\[
d_Gp q'-d_{h,G}p'q=\ominus p^{\mu_G}. \tag{11}
\]

Under `eta -> omega eta`, the left side has character `s-1`, whereas the
right side has character zero.  Because the right side is nonzero,

\[
s-1\equiv0\pmod\nu.
\]

As `0<=s<nu`, `s=1`; hence

\[
p_{h,G}(\eta)=\eta r(\eta^\nu),\qquad
\deg p_{h,G}\equiv1\pmod\nu,
\]

and therefore `gcd(nu,deg p_{h,G})=1`.

This supplies exactly the missing last step of Statement 8.5.  Combined with
the corrected subscripts and degree-ratio orientation already recorded in the
Section 8 audit, its conclusion `M_G | M_F` follows.

## 3. Why the homogeneous ODE term is not a counterexample

If one ignores the Puiseux chart and decomposes an arbitrary polynomial `q`
by eta-degree modulo `nu`, the homogeneous equation does allow
`q_0=Cp^(d_h/d)` when that exponent is integral.  Thus the Opus review's
degree-only exclusion of `q_0` is not established.

At a genuine characteristic vertex, however, `p_{h,G}` is a single
`mu_nu`-eigenvector by (CSI); it cannot be `q_1+q_0` with two different
characters.  Equation (11) then forces that sole character to be one.  A bare
ODE packet containing both characters is therefore not a typed Sigray-vertex
packet.

## 4. Blast radius and promotion state

- **Statement 8.5:** repaired by the independently checked cyclic lemma,
  the explicit one-orbit argument, and the typed Proposition 4.6 packet.
- **Corrected Proposition 8.3(i):** its use of Statement 8.5 is restored; its
  separate `(Reg)`, singleton-pole/microstep, and existence hypotheses remain
  exactly as listed in the Section 8 hostile review.
- **Corrected nonroot Proposition 8.4:** no new rollback beyond the already
  identified root quarantine.
- **Campaign eta law:** the previously informal phrase "nu-equivariance"
  now has a direct proof.  ODE order arguments are still needed separately to
  pin the eta multiplicity exactly to one at roots.
- **Section 7:** this lemma may supply its missing zero-order cyclic descent,
  but it does not by itself identify coefficient-chart directions with
  components on a common final graph resolution.

**Promotion:** the different-model review `008a7e6949...` passed the cyclic
lemma.  Its addendum identified the final positivity/citation line, now
inserted explicitly.  One checksum-pinned recheck of this last insertion is
still required before canonical promotion.
