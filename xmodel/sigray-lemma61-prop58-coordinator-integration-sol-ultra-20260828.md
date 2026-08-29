# Coordinator integration: Sigray Lemma 6.1 and Proposition 5.8

Date: 2026-08-28 14:00Z  
Role: campaign coordinator  
Verdict: **PROMOTE BOTH CAMPAIGN REPLACEMENTS; RETAIN THE TWO SOURCE DEFECTS**

This note separates statements about Sigray's printed thesis from statements
proved by the campaign.  It changes no claim about landing, full-book
completeness, `RPMC(C)`, a cofinal degree ceiling, or JC2.

## 1. Lemma 6.1 / Proposition 6.8

The printed final inference of Lemma 6.1 is incomplete.  The repaired proof
is review-closed:

```text
2fdbbee9ec04db1f3ff1220eeda4ffb84c1c1580948d76a0015119a85602bc5e  R2 producer
5193e7b0a7741b6a202ddf7f55666f4a5b11caa7671e3e7b3784a69181cecbd9  Opus5 hostile review
607e0dcf2459a6b509388bb41b89ba04648f41d1c7cdd0f457abd4d749d0689a  mandatory correction
```

For a fixed pair `f-a,g`, choose one grid denominator divisible by every
relevant curve-pole order.  The defect

```text
rho(F_j)=d_(f-a,F_j)+d_(g,F_j)+j/K-1
```

obeys the exact edge law

```text
rho(F_(j+1))-rho(F_j)=(1-r_j-t_j)/K <= 0.
```

Thus a hypothetical nonempty tower at a positive vertex with
`deg p_F=1` remains nonempty at every ancestor.  Proposition 4.4 transports
its fixed first relation to an axis, where its primitive exponent pair is
`(alpha,beta)`.  Back at `F`,

```text
p_(g,F)^alpha=s*p_F^beta.
```

Taking degrees gives `alpha | beta`, hence `alpha=1`, contradicting
Statement 2.1.  Opus independently confirmed the sign, the two chart
orientations, the fixed-polynomial use of Statement 3.9, the residual
degree argument, and Proposition 6.8's consumption of the lemma.  Its two
required insertions merely spell out the common-divisibility choice of `K`
and the equality of the positive leading data for `f` and `f-a`.

**Status.** Lemma 6.1 is a repaired theorem.  Repaired Proposition 6.8 and
the Proposition 6.7/6.8 microstep-to-next-vertex bridge are promoted without
a Lemma-6.1 rider.  Statement 6.2 remains a source GAP: its printed “in
particular” clause omits `H in V_a cap T_a^+`.  Concrete consumers are sound
only when they first establish that domain, as the repaired bridge does.

## 2. Proposition 5.8

The thesis prints equation (20) for every finite fiber and supplies no
proof.  That source verdict remains `GAP`, but the campaign theorem is
already promoted at the printed strength by the relative-surface proof in
`ladder/SOL-PROP58.md`, the adversarial review in
`ladder/SOL-PROP58-REVIEW.md`, and Chau, Theorem 4.4(E1).  A new independent
audit also gives a second, internal positive-pole transport proof:

```text
47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf  independent audit
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7  full Chau source
```

The external proof has the exact defect formula

```text
sum_F Lambda(F)=td-Delta_a,
Delta_a=sum_E ord_E(f-a)*deg(g|E)>=0,
```

and Chau's positive degree-ratio theorem excludes every vertical
defect-carrying component.  The new internal proof uses the promoted
Proposition 5.1 sidedness theorem: every pole threshold has positive
`f-a` order, so changing the fiber constant cannot alter its strict
Newton--Puiseux truncation.  Transport of the complete presentation set
preserves `d_g`, `deg p`, the jump/max `kappa`, and `nu`, hence every
`Lambda` summand.  It does not rely on Statement 3.14's exact `eta`
alignment.

**Status.** Proposition 5.8 remains `GAP IN SOURCE / CAMPAIGN REPLACEMENT
PROMOTED`.  The mass partitions and every-fiber consumers have no
Proposition-5.8 rider.  Proposition 5.4 is not needed for equation (20), but
is still needed for the downstream `nu` menu, `Lambda>=beta`, and entry
enumeration.  No later landing, merge, suffix, or book-completeness rider is
discharged by this result.
