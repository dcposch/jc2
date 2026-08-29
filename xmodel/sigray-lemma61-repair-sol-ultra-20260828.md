# Sigray Lemma 6.1 — short tower repair

Date: 2026-08-28  
Status: **PROVISIONAL COMPLETE REPAIR — DIFFERENT-MODEL REVIEW OWED**  
Source: `refs/sigray_full.pdf`, printed p. 34  
Scope: the prerequisite used only to exclude a degree-one intermediate point
in the repaired proof of Proposition 6.8.  No claim about Sections 7--9,
landing, a degree ceiling, or JC2.

## 1. Statement

Let `F in T_a^+`, put `u=pi(F)`, and assume `deg p_F=1`.  Then

```text
J(f_F^+,g_F^+) = nonzero_constant * xi^(-u).
```

Equivalently, the Proposition 4.2 tower at `F` has length `m_F=0`.

## 2. Defect in the printed proof

The printed maximal-grid argument reaches
`deg p_(g,F)=0` and then asserts that the leading Jacobian is nonzero.  That
inference is not valid in isolation: if also `d_(g,F)=0`, then `g_F^+` is a
scalar and its Jacobian with `f_F^+` is zero.  The source supplies no argument
at that point excluding the scalar case.  Thus the printed proof is
incomplete even though the lemma is true.

## 3. Repaired proof

The reviewed no-first-constant-corner theorem says that, for every
`F in T_a^+`, the leading part `g_F^+` is not a scalar.  Hence the corrected
Proposition 4.2 applies at `F` with its ordinary positive-exponent first
relation whenever `m_F>0`.

Assume for contradiction that `m_F>0`.  Write

```text
p=p_F,   q=p_(g,F).
```

The first tower relation is

```text
(g_F^+)^k = s*(f_F^+)^l,     k,l in N*, gcd(k,l)=1.       (3.1)
```

Propositions 4.4--4.5 compare this first relation along `T_a^+` with the
normalized Newton-top relation at the two axes.  With Notation 2.4

```text
alpha/beta = k_f/k_g,   gcd(alpha,beta)=1,
```

they give exactly

```text
(k,l)=(alpha,beta).                                      (3.2)
```

Comparing the residual `eta`-polynomials in (3.1) therefore gives

```text
q^alpha = s*p^beta.                                      (3.3)
```

Taking degrees and using `deg p=1`,

```text
alpha*deg q = beta.
```

Thus `alpha | beta`.  Coprimality forces `alpha=1`, contrary to Statement
2.1 (indeed `alpha>=2`).  Hence `m_F=0`.

The terminal clause of corrected Proposition 4.2 now has `mu_F=0` and says
directly

```text
J(f_F^+,g_F^+) = nonzero_constant*(f_F^+)^0*xi^(-u)
                = nonzero_constant*xi^(-u).
```

This is Lemma 6.1.  No grid induction, auxiliary-`h` application of Statement
3.9, or assumption on `d_(g,F)` is used.  QED.

## 4. Dependency and blast-radius firewall

The repair uses only:

1. Notation 2.4 and Statement 2.1;
2. corrected Proposition 4.2 plus the reviewed no-first-corner theorem on
   `T_a^+`; and
3. Propositions 4.4--4.5 for the first-relation exponent pin.

It closes the one prerequisite left open by the Opus5 review of repaired
Propositions 6.7/6.8 (`eb37373b...`, corrected by addendum `050ccddd...`).
Until a different model reviews this short proof, Proposition 6.8 and its
next-vertex consumers may be used provisionally but should retain an explicit
review-owed label.
