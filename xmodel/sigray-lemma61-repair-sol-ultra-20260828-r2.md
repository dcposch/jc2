# Sigray Lemma 6.1 — repaired tower proof, R2

Date: 2026-08-28 13:40Z  
Status: **COMPLETE REPAIR — INDEPENDENTLY REVIEWED**  
Source: `refs/sigray_full.pdf`, printed p. 34  
R1: `xmodel/sigray-lemma61-repair-sol-ultra-20260828.md`
(`651231a8...`)  
Hostile review:
`xmodel/sigray-lemma61-repair-hostile-review-sol-ultra-20260828-r1.md`
(`b279732c...`, verdict `REPAIR`)

The review found one missing transport gate in R1 but no false conclusion.
This version incorporates its fixed-pair defect-monotonicity repair.  The
scope is only Lemma 6.1 and its use in repaired Proposition 6.8; it proves no
landing, cofinality, degree ceiling, or Jacobian-conjecture conclusion.

## Statement

Let `F in T_a^+`, put `u=pi(F)`, and assume `deg p_F=1`.  Then

```text
J(f_F^+,g_F^+) = C*xi^(-u),       C in C*.
```

Equivalently, the corrected Proposition 4.2 tower at `F` has length `m_F=0`.

## Printed defect

The source's maximal-grid proof reaches `deg p_(g,F)=0` and then asserts that
the leading Jacobian is nonzero.  This is not valid in isolation: if also
`d_(g,F)=0`, then `g_F^+` is scalar and its Jacobian with `f_F^+` vanishes.
The reviewed no-first-constant-corner theorem excludes that branch on
`T_a^+`, but that theorem is a genuine repair of the printed argument.

## Repaired proof

Assume for contradiction that `m_F>0`.  The no-first-constant-corner theorem,
applied to `(f,g)`, supplies condition (7), so corrected Proposition 4.2 gives
an ordinary first relation

```text
(g_F^+)^k = s*(f_F^+)^l,
k,l in N*,  gcd(k,l)=1,  s in C*.                         (1)
```

It remains to justify transporting `(k,l,s)` to an axis.  This was the gate
omitted in R1: adjacent comparison alone would not rule out an abstract
`nonempty -> empty -> nonempty` sequence of towers.

Write `F=I_P(u)`.  Choose one `K` suitable for this chart, with `Ku in N`,
large enough that Statement 3.9 applies to the two fixed polynomials `f-a`
and `g`.  Put

```text
F_j = I_P(j/K),
rho(F_j) = d_(f-a,F_j) + d_(g,F_j) + j/K - 1
            (0 <= j <= Ku).                              (2)
```

Every `F_j` is in `T_a^+`: Statement 3.10 makes the `f-a` order
nonincreasing as the parameter increases, while its value at `F` is
positive.  Since `m_F>0`, the initial leading bracket at `F` vanishes;
Proposition 4.1 and condition (7) therefore give `rho(F)>0`.

For each edge `F_(j+1)=F_j*c_j`, set

```text
r_j = mult(p_(f-a,F_j),c_j),
t_j = mult(p_(g,F_j),c_j).
```

Corrected Statement 3.18 gives `r_j>=1`, and `t_j>=0`.  Applying Statement
3.9(iii) to the fixed pair in (2) gives the exact edge law

```text
rho(F_(j+1)) - rho(F_j) = (1-r_j-t_j)/K <= 0.             (3)
```

Thus every ancestor satisfies `rho(F_j)>=rho(F)>0`.  The reviewed
no-first-corner theorem supplies condition (7) at each such positive flag;
Proposition 4.1 then says its initial bracket vanishes, so corrected
Proposition 4.2 gives a nonempty tower with an ordinary first relation.
Proposition 4.4 can now be applied edge by edge, with the fixed polynomial
`g`, and transports the same primitive triple `(k,l,s)` all the way to the
axis `F_0`.  No derived tower polynomial is fed to Statement 3.9.

At either possible axis, Lemma 2.1 and Notation 2.4 give

```text
d_f/d_g = k_f/k_g = l_f/l_g = alpha/beta.
```

Taking orders in `(g^+)^k=s*(f^+)^l` yields
`k/l=d_f/d_g=alpha/beta`.  Coprimality therefore forces

```text
(k,l)=(alpha,beta).                                      (4)
```

Proposition 4.5 confirms that the two axis choices give the same primitive
pair.  Returning to `F` and comparing residual polynomials in (1) gives

```text
p_(g,F)^alpha = s*p_F^beta.                              (5)
```

Taking degrees and using `deg p_F=1` gives
`alpha*deg p_(g,F)=beta`, hence `alpha|beta`.  Since
`gcd(alpha,beta)=1`, this forces `alpha=1`, contradicting Statement 2.1.
Therefore `m_F=0`.

The terminal clause of corrected Proposition 4.2 now has `mu_F=0` and gives

```text
J(f_F^+,g_F^+) = C*xi^(-u),       C in C*,
```

as required.  QED.

## Dependency and consumer verdict

The proof uses only Lemma 2.1, Notation 2.4, Statement 2.1, corrected
Statements 3.9/3.18, Statement 3.10, Proposition 4.1, corrected Proposition
4.2, Propositions 4.4--4.5, and the independently reviewed
no-first-constant-corner theorem on `T_a^+`.

The hostile review independently checked the defect sign, axis orientation,
both chart choices, condition (7), the terminal clause, and Proposition
6.8's sole use of the lemma.  Hence repaired Proposition 6.8 and the
Proposition 6.7/6.8 microstep-to-next-vertex bridge no longer carry a
Lemma-6.1 review rider.  Statement 6.2 itself remains a source GAP because
its printed “in particular” clause omits `H in V_a cap T_a^+`; concrete
campaign consumers supply that domain through the repaired bridge.
