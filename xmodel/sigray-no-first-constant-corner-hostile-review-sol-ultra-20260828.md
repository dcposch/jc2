# Hostile review — no first constant corner on `T_a^+`

Reviewer: Sol Ultra, different model from the Opus5 producer.

Date: 2026-08-28 UTC.

Input claim: Theorem C and the Statement 3.9 hypothesis-ablation finding in
`xmodel/ideation-20260828T1149Z-opus5.md`, SHA-256 `882485d6...`.

Verdict: **CONFIRMED AND STRENGTHENED** for Theorem C.  The auxiliary-`h`
`kappa` finding is **CONFIRMED AS A HYPOTHESIS/CONSUMER DEFECT**, not as a
counterexample to Statement 3.9 with all of its printed hypotheses.

## 1. Strengthened theorem

Let `(f,g)` be a normalized Keller pair, let `a,b in C`, and let
`F in T_a^+`.  Then

```text
(g-b)^+_F is not a nonzero scalar constant.                 (C+)
```

Equivalently, condition (7) is automatic on `T_a^+` for **every** target
constant `b`.  In the corrected Proposition 4.2 tower of the translated pair
`(f,g-b)`, a constant corner cannot occur at index zero.  A constant corner
may still occur at a later tower index and remains subject to the promoted
`(1,0,c)` repair.

This strictly strengthens the producer's fixed-`g` statement and removes its
reported residual `{m_F=0,d_(g,F)<0,pi(F)>1}` sliver: if `d_(g,F)<0` and
`b!=0`, then `(g-b)^+_F=-b` would violate (C+).

## 2. Independent proof

Fix `b` and write `H=g-b`.  Target translation preserves the Jacobian,
noninvertibility, degrees and the Lemma 2.1 Newton normalization, while
`T_a` depends only on `f-a`; thus corrected Proposition 4.2 applies to the
normalized pair `(f,H)`.

Suppose `H_F^+=s in C^*`.  Choose one `kappa` suitable for both fixed curves
`f-a=0` and `H=0`, with `kappa*pi(F)` integral.  This is allowed by taking a
common multiple of their finitely many pole orders.  The first leading
Jacobian is zero, so the corrected tower makes the unique corner step
`(k,l,s)=(1,0,s)` at index zero.  In particular its initial defect

```text
delta_0(F)=kappa(d_(f-a,F)+d_(H,F)-1+pi(F))
```

is a positive integer.

The root flags cannot have scalar `H^+`: at `(0,y)` (respectively `(0,x)`),
`H^+` is the top `x`-coefficient (respectively top `y`-coefficient) with its
nonnegative Laurent order, and it is a scalar constant only when `H` itself
is constant.  Since `H=g-b` is nonconstant, `F` is not a root.

Let `G` be the preceding `1/kappa` flag on the same branch, so `F=G*c`.
Apply Statement 3.9 to the **fixed** auxiliary polynomial `H`; the common
choice of `kappa` satisfies its full hypothesis.  Because
`deg p_(H,F)=0`,

```text
mu_H := mult(p_(H,G),c)=0,
d_(H,G)=d_(H,F)=0.
```

Statement 3.18 applied to `f-a` gives
`mu_f:=mult(p_(f-a,G),c)>=1`, and Statement 3.9(iii) gives
`d_(f-a,G)>=d_(f-a,F)>0`.  Direct subtraction yields the exact edge law

```text
delta_0(F)-delta_0(G)=1-mu_f-mu_H=1-mu_f<=0.
```

Hence `delta_0(G)>=delta_0(F)>0`: the parent leading Jacobian also vanishes.
Lemma 2.2 and the corrected Proposition 4.2 step give

```text
(H_G^+)^k = c_0 (f_G^+)^l,
k in N*, l in N, gcd(k,l)=1.
```

Its order equality is `k*0=l*d_(f-a,G)`.  Since the latter order is positive,
`l=0`; coprimality forces `k=1`, so `H_G^+` is again a scalar constant.
Statement 3.9(ii) identifies it with the same child value, although equality
of the constants is not needed for the contradiction.

The argument repeats along the finite `1/kappa` ancestor chain to a root,
contradicting the root calculation.  Therefore (C+) holds.

This proof attacks and resolves the two points named by Opus: the delta
identity uses `alpha_0=0` by definition, and the parent tower is nonempty
because its `delta_0` is strictly positive.  It does not need the general
derived-member form of Fact A; at every step the only auxiliary polynomial is
the fixed `H=g-b`.

## 3. Consequences and exact scope

- Restore the **statement** of Sigray's p. 20 Remark, but replace its circular
  printed proof by the ancestor induction above.
- On `T_a^+`, condition (7) need no longer be carried as a separate hypothesis
  in Propositions 4.1, 4.6 or 6.2.  Proposition 4.3 is on `T_a^-` and still
  requires the correct shift/condition (7), now supplied at punctures by the
  promoted Proposition 5.1 repair.
- The theorem does not exclude later `(1,0,c)` corners, alter their terminal
  degree, create pole mass, prove landing, prove `RPMC(C)`, bound `td`, or
  prove JC2.

## 4. Statement 3.9 hypothesis ablation

The producer's exact example at `kappa=1` was replayed.  It gives

```text
mult(p_(h,F),0)=3,
deg p_(h,F*0)=1,
d_(h,F)=2,
d_(h,F*0)=0,
```

because `h=0` has an `x`-pole of order two.  Thus `kappa=1` violates
Proposition 3.1's pole-order condition for the auxiliary `h`, exactly as the
producer says.  This does **not** falsify Statement 3.9 as printed: that
statement expressly requires the Proposition 3.1 property.  It proves that
the hypothesis is load-bearing and `h`-dependent.

The consumer-level correction is therefore:

1. every use of Statement 3.9 names the auxiliary polynomial;
2. `kappa` must be suitable for the fibre and a multiple of that auxiliary
   curve's pole orders; and
3. when the auxiliary polynomial is a derived tower member, either enlarge
   `kappa` locally and prove subdivision compatibility, or use Statement
   3.11's inequality form.  A bare “`kappa` suitable” for the fibre is
   insufficient.

The proof of (C+) is insulated because it uses only the fixed `f-a` and
`g-b`.  The general Fact A / Proposition 4.4 integration still owes the
consumer rider; no global assertion that one `kappa` works for every tower in
every fibre is made here.

## 5. Replay and custody

Primary Sigray pages 14--22 were checked directly against
`refs/sigray_full.pdf` (`9bf9f032...`), including Statements 3.9/3.18,
Propositions 4.1/4.2/4.4 and the p. 20 Remark.  The producer's ephemeral exact
checker was hash-verified at
`5893a14a54844ce97069276958c12aca9e87b96c020176400e91b80d129ac143`
and replayed:

```text
edge trials:                 11349
non-vacuous corner children:   434
Fact-B trials:                5857
kappa negative control:       BREAKS as predicted
RESULT: PASS
```

The replay is corroborative.  The proof in §2 is the independent
different-model mathematical review.
