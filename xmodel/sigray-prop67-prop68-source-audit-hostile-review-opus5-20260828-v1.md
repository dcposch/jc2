# Hostile review — Sigray Prop. 6.7/6.8 source audit (producer `c3d6ff92`)

Reviewer: Opus 5, different-model hostile source-proof audit.
Date: 2026-08-28.  No AWS, no web, no CAS, no checker (none was needed).
`jc2-lean` was never entered.  Only this file was written.

## Custody

Recomputed before reading:

```text
c3d6ff9239fb136cc35b815de6e229755f7d27b640481e7751d03d63291d1ebd  xmodel/sigray-prop67-prop68-source-audit-sol-ultra-20260828.md
```

MATCHES the frozen pin.  All seven SHA-256 values in the producer's Section 1
were recomputed live and all seven MATCH.  Primary source read directly
(`pdftotext -layout` and raw), printed pp. 9--35.

## Terminal verdict

**REPAIR.**

- **Propositions 6.7 and 6.8 are TRUE** (6.7 with the producer's added lattice
  rider `kappa*pi(F) in N`).  I reconstructed every step independently.
- **The producer's repair is substantially correct** and its two headline
  diagnoses (illegal exact St. 3.9 on `h_F`; printed `u-n/kappa` wrong) are
  confirmed.  Its central inequality chain is sound.
- **But the repair is not complete.**  One genuine logical gap survives
  (§3.3's `h=h_G`), two steps are missing from the §5 bridge, one pinned
  dependency is spurious, and one displayed ratio is reciprocal.  All are
  repairable from source-internal material, which I supply below.
- **Blast radius CONFIRMED**, no rollback.

## 1. Auxiliary `h` denominator — CONFIRMED, and under-corroborated

The producer is right that exact St. 3.9 is unlicensed at `h=h_F`: St. 3.9's
hypothesis is Prop. 3.1's "`kappa` is a multiple of any order of `x`-pole" of
the fibre `h=0`, an `h`-condition, and `882485d6` exhibits an exact failure.

The producer **misses its strongest corroboration**: the source itself says so.
Prop. 6.3's proof, printed p. 30--31, reads *"Since `kappa` is not necessarily
suitable for the Puiseux series `h_j=0`, so for `d_G` we may use Statement 3.9,
but for `d_{h_j,G}` we need Statement 3.11."*  The repair is therefore not a
new device but the source's own idiom, applied two propositions earlier.  This
raises confidence and should be recorded.

**Corrected St. 3.11 re-derived from scratch, unconditionally.**  Writing
`h^F = sum_j x^(j/kappa) p_j(eta)`, `eta_G = x^(1/kappa)(eta_F-c)` gives
`h^G(x,eta) = sum_j x^(j/kappa) p_j(x^(-1/kappa)eta+c)`; distinct `j` land on
distinct `x`-powers, so the coefficient of `x^s eta^l` is exactly
`p_(s*kappa+l)^(l)(c)/l!`.  Let `n=kappa*d_(h,F)`, `n_l=max{j: p_j^(l)(c)!=0}`.
Then `n_l<=n` always, and `n_l=n` for every `l>=mult(p_(h,F),c)`.  Hence

```text
d_(h,G) >= d_(h,F) - mult(p_(h,F),c)/kappa,     d_(h,G) <= d_(h,F) - deg(p_(h,G))/kappa,
```

and combining, `deg(p_(h,G)) <= mult(p_(h,F),c)`.  **No Prop. 3.1 hypothesis is
used.**  This is precisely the producer's (3.3) with the correct directions,
and it verifies against the `kappa=1` ablation (`0 >= -1`, `0 <= 1`, `1 <= 3`).
Note the ledger records St. 3.11 as ERRATUM with the campaign using "clause (i)
and the upper bound of (ii)" only; the producer's repair is the **first**
campaign use of the corrected *lower* bound.  That row needs amending — the
clause is safe, as just proved.

**(3.4) verified.**  With `d,e,d_G,m>0`: `m*e_G - n*d_G >= m(e-n/kappa) -
n(d-m/kappa) = me-nd > 0`, and `n>=r` gives `e_G/d_G > n/m >= r/m`.  Exact.

**The choice of 3.11 over `kappa`-enlargement is not merely convenient, it is
forced.**  `882485d6` §3 offers enlargement as an alternative; but the `*`
operation is `kappa`-dependent (Notation 3.8 Remark), so enlarging `kappa`
mid-proof changes the very child `F*c` whose type is being asserted, and would
destroy Prop. 6.8's grid chain `F_j=I_P(u+j/kappa)`.  The producer should say
this; it is the real reason its route is the only one.

**GAP FOUND — the identification `h=h_G` is still unlicensed.**  Both the
source and the producer write "by Proposition 6.3 `h=h_G`".  Proposition 6.3's
`G in T_a^nearrow` branch concludes only `F <= G` (Notation 4.1), i.e.
`m_F <= m_G` with matching `K,L,S` prefixes.  That does **not** give
`m_G = m_F`, and `h_G = h_(m_G,G)`.  The producer's offered alternative
("avoid the last citation") is also insufficient on its own: it needs
`h_(m_F,G) = h_F`, which is exactly the prefix property only Prop. 6.3 supplies.

The correct argument needs **both**, in this order.  Under the indirect
assumption `G in T_a^nearrow` (legitimate: `G in T_a^+` by clause 1, then
St. 6.1):

1. Prop. 6.3 gives `F <= G`, so `h_(m_F,G) = h_(m_F,F) = h` and `m_F <= m_G`.
2. If `m_G = m_F` then `h_G = h`; (3.5) plus Prop. 6.4 gives
   `G in T_a^searrow`, contradiction.
3. If `m_G > m_F` then `J(f_G^+, h_G^+)=0` by (10).  With
   `J(xi^d P, xi^e Q) = xi^(d+e-1)(dPQ' - eP'Q)`, this is
   `d_G p_G p_(h,G)' = e_G p_G' p_(h,G)`.  Since `e_G>0` (from (3.4)) and
   `deg p_G = m >= 1`, the case `deg p_(h,G)=0` forces a nonzero right side,
   and otherwise the top coefficient gives `d_G*r = e_G*m`, i.e.
   `e_G/d_G = r/m`, contradicting the strict (3.5).

Both branches close.  This is a **defect in the producer's proof**, not in
Prop. 6.7; severity: it is the load-bearing final step of the existence clause.

## 2. Cyclic residual lemma — TRUE; producer's proof incomplete

The lemma is needed and correct.  I prove it, since the producer's sketch omits
the two facts that make it work.

Let `F=I_P(u) in V_(1,a)`, `u=alpha_j=beta_j/kappa` (for `F` not in `V_(1,a)`,
`nu_F=1` and the claim is vacuous).  Put `e_j=gcd(kappa,beta_1,..,beta_j)`,
`kappa_F=kappa/e_j`, `nu_F=e_(j-1)/e_j`, `s=x^(-1/kappa_F)`.  By Definition
3.1 every `i<beta_j` with `c_i!=0` satisfies `e_(j-1) | i`, so the truncation
`tau=sum_(i<n) c_i s^(i/e_j)` has all `s`-exponents in `nu_F*Z`, and
`gcd({i/e_j} union {kappa_F}) = nu_F`.

**Fact 1 (missing from the producer).**  The stabiliser of `tau` inside the
deck group `mu_(kappa_F)` is therefore *exactly* `mu_(nu_F)` — the same group
as in corrected St. 3.18.  This answers the review question: the group is
intrinsic and `kappa`-independent (replacing `kappa` by `lambda*kappa` scales
`e_i` by `lambda`, leaving `kappa_F` and `nu_F` fixed), so no enlarged
denominator can perturb it.

For `zeta in mu_(nu_F)`, `H(x,y)=Hhat(s,eta)` with
`Hhat(s,eta)=H(s^(-kappa_F), s^(n/e_j) eta + tau(s))` gives
`Hhat(zeta s, eta) = Hhat(s, eps*eta)` with `eps = zeta^(beta_j/e_j)`.

**Fact 2 (missing from the producer, and essential).**
`gcd(beta_j/e_j, nu_F) = gcd(beta_j, e_(j-1))/e_j = 1`, so
`zeta |-> zeta^(beta_j/e_j)` is an **automorphism** of `mu_(nu_F)`.  Without
this one only covers a subgroup, and St. 3.18's particular `eps` need not be
reached.

Writing `Hhat = sum_k s^k P_k(eta)` and equating `s^k` coefficients gives
`P_k(eps*eta) = zeta^k P_k(eta)`; at the extremal `k` this is
`p_(H,F)(eps*eta) = chi(eps) p_(H,F)(eta)`.  Hence
`mult(p_(H,F), eps*c) = mult(p_(H,F), c)` for every `eps in mu_(nu_F)` and
every nonzero `c`.  (For `H=f` this re-proves St. 3.16's second half.)

Consequently (3.2) survives the unique St. 3.18 rotation for **both** `p` and
`q` simultaneously.  **Not a gap in the source setup** — derivable, as above.
The producer's `c=0` and single-distinct-root side cases are also correct: with
one distinct root, Prop. 3.1(*) forces the next coefficient of any representing
branch to be that root, so the child exists outright.

## 3. `h=g` branch — correct conclusion, one spurious dependency, one reciprocal

`m_F=0`, so Prop. 5.1 gives `F_P^* = I_P(v)` with `v<=u`.  Prop. 5.3(v) (via
its own proof, "for any `G` with `G^(nu)=F`, `deg(p_G)<=1`") plus
`deg p_F > 1` forces `u=v`.  `d_G = d_F - 1/kappa` by 5.3(v) and St. 3.9 for
`f`.  Integrality: `kappa_F | kappa`, so St. 3.8 gives `kappa*d_F,
kappa*d_(g,F) in Z`; `kappa*d_F=1` would make `kappa*d_(g,F)` equal to the
type ratio, non-integral.  Hence `kappa*d_F >= 2` and `d_G >= 1/kappa > 0`.
**CONFIRMED.**

Two defects:

- **Spurious dependency (documentary).**  The producer's opening paragraph —
  choose a puncture, test `b_P=g(P)` finite, invoke the repaired Prop. 5.1
  centre and the no-first-corner theorem — is *not needed*.  `F_P^* in
  T_(a,pole)` follows by **definition**: Notation 5.2 is `{F_P^*} cap T_a^+`,
  and `d_(I_P(v)) >= d_(I_P(u)) = d_F > 0` by St. 3.10(i) monotonicity since
  `v<=u`.  That is the whole step.  Pinning the Prop. 5.1 repair and the
  no-first-corner theorem here inflates the dependency graph of the repair
  packet and should be struck.  (Its aside "finite thresholds lie in `T_a^-`"
  is also imprecise: Notation 7.1/Prop. 7.2 put them in `T_a^0`.)
- **Reciprocal ratio.**  Prop. 5.3(iii) is `k_f p p_g' - k_g p' p_g = const`,
  which is Prop. 4.6 (11) at `m_F=0`; comparing, `d_(g,F)/d_F = k_g/k_f`, and
  Notation 2.4 is `alpha/beta = k_g/k_f`.  So `kappa*d_(g,F) = alpha/beta`,
  not the producer's `beta/alpha`.  (The source is internally inconsistent
  here: 5.3(ii)/(iii)/(vii) agree with `alpha/beta`, while St. 5.2(i) and the
  St. 5.2(ii) proof display the reciprocal; the ledger's Prop. 5.3 erratum row
  is itself self-inconsistent, writing `(k_g/k_f)d_F = (beta/alpha)d_F`.)
  **The conclusion is invariant**: `alpha,beta >= 2` and coprime by
  Statement 2.1, so neither ratio is an integer.  The producer's stated reason
  ("`alpha>=2`") is direction-sensitive and should read "`alpha,beta>=2`".

## 4. `h!=g` and `d_G!=0` — CONFIRMED in full

`(g_F^+)^r = s(f_F^+)^t` is Prop. 4.2(iii) at `j=0`; `t>=1` genuinely needs the
no-first-corner theorem, because the printed Prop. 4.2 proof justifies
`l_j != 0` only by "`h_j` is non-constant", which does not exclude a scalar
leading part.  Correct pin.  Then `p_(g,F)^r = s p_F^t` gives
`r*mult(p_(g,F),c) = t*m`, so St. 3.9 for `g` (licensed: `kappa` common-suitable
for `f g`) yields `deg p_(g,G) = (t/r)m > 0` and `d_(g,G) = (t/r)d_G`.

Condition (7) at `G` is licensed and **non-circular**: `g_G^+ =
xi^(d_(g,G)) p_(g,G)` is not a constant because `p_(g,G)` is nonconstant — this
does not go through the p. 20 Remark's `d_G>0` route, which would be circular.
Correctly identified.  `u<1` from `T_a^searrow`, `kappa*u in N` gives
`u<=1-1/kappa`, so `1-pi(G)>=0`; Prop. 4.1 gives `(1+t/r)d_G >= 1-pi(G) >= 0`,
so `d_G>=0`.  If `d_G=0` then `d_(g,G)=0` and `pi(G)=1`, and the equality
branch of (8) demands `J = xi^(-1)`; but `d=e=0` makes the bracket
`d P Q' - e P' Q` vanish identically, so `J=0`.  Contradiction.  **CONFIRMED.**
(The producer attributes the vanishing to (2.2); it is simpler — both orders
are zero.)

## 5. Proposition 6.8 — CONFIRMED with two supplied steps

- **`u-n/kappa` is genuinely wrong**, not notation: the proof opens "Let
  `u := pi(F)`".  Nothing bounds `d_F` by `pi(F)` (take `u=0`, `deg p_F=10`,
  `d_F=5`).  The producer's `d_(F_n) <= d_F - n/kappa` follows from
  `m_n>=1` and St. 3.9 for `f`, and `d_(F_n)>0` bounds `n < kappa*d_F`.
  **CONFIRMED.**
- **Degree-one exclusion.**  Lemma 6.1 gives `J(f^+,g^+) != 0`, hence the
  Prop. 4.2 tower terminates at `j=0`, i.e. `m_(F_n)=0`; then §2.1 puts a pole
  at `F_Q^* = I_Q(v)`.  The producer asserts this is "at a `kappa`-grid depth";
  that needs supplying: `F_Q^* in V_a` by Prop. 5.3(iv), and for suitable
  `kappa` every `V_(1,a)` depth `alpha_j` and every `V_(2,a)` depth `O(Q,Q^*)`
  lies in `(1/kappa)N`, so `v = u + j/kappa`.  `j<0` would put `F` strictly
  above the pole, forcing `deg p_F = 1`; `0<=j<n` contradicts the stopping
  rule; `j=n` contradicts `F_n not-in T_(a,pole)`.  **Supplied, sound.**
- **Sequential licensing** holds with one fixed `kappa` throughout: `F_n in
  T_a^searrow`, `deg p_(F_n)>1`, `kappa*pi(F_n)=kappa*u+n in N`.
- **Same-branch ancestors.**  Notation 3.8 / St. 3.5 give
  `F_j = I_P(u+j/kappa)` downward from `F_N`, hence `F=I_P(u)` for the *same*
  `P`.  The source's "evidently" hides exactly this.  **CONFIRMED.**
- **Open dependency.**  Lemma 6.1 itself is used but audited nowhere; its
  printed proof is visibly garbled (`p_(g,F,n)`, a truncated
  `J(f^+,g^+) = .`).  Flag as an unaudited prerequisite of Prop. 6.8.

## 6. Microstep versus next vertex — diagnosis CONFIRMED, bridge needs two steps

`G*_(kappa)c` (Notation 3.8) and `H=G+c` (Prop. 3.2) are different points; the
r1 sweep conflated them, and Prop. 6.7 alone does not discharge St. 6.2's
missing `H in T_a^+`.  **Correct and important.**

- **First microstep is searrow.**  `d_E < (1-pi(E))deg p_E` is *equivalent* to
  (5.1) — verified by direct substitution.  **But the producer omits
  `d_E>0`**, which `T_a^searrow` requires (Notation 6.1).  It is available:
  Prop. 6.7 clause 1 at `G`, whose `deg p_G>1` hypothesis holds by St. 3.16
  (`G in V_a`, and `pi(G)=0` with `G=(0,y)` still gives
  `deg p_((0,y)) = k_f > 1`).  Missing step, repairable.
- **`m=1` is genuinely impossible** — I tested it rather than assuming.
  St. 3.17(i) gives `deg p_H = mult(p_G,c) = m` *exactly*.  `H` is a vertex
  with `pi(H) > pi(G) >= 0`, so `H != (0,x),(0,y)`, so St. 3.16 gives `p_H`
  more than one distinct root, so `m = deg p_H >= 2`.  The producer's route via
  `deg p_H <= deg p_E` also works but the equality is cleaner.
- **The transport is valid, by a shorter route than the producer's.**  The
  producer asserts "its first vertex above `G` is precisely `H`" without proof.
  Supply: (a) any branch `Q` through `E` that separated from `H`'s branch at
  `w < pi(H)` would produce a `V_(2,a)` vertex strictly between `G` and `H`,
  impossible by Notation 3.3, so **every** branch through `E` passes through
  `H`; (b) Prop. 6.8 at `E` gives a pole `I_P(v)`, and Prop. 5.3(ix) says
  `I_P((v,inf]) cap V_a = empty`, so `pi(H) <= v`; (c) St. 3.10(i) then gives
  `d_H >= d_(I_P(v)) > 0`.  With `G,H in V_a cap T_a^+` and (5.1), St. 6.2's
  verified iff gives `H in T_a^searrow`.  This uses only the *statement* of
  Prop. 6.8, not its internal recursion.
- Note `pi(E) <= pi(H)` always (suitable `kappa` are the multiples of one
  `kappa_0`, and vertex depths lie on the `kappa_0` grid); when
  `pi(E) = pi(H)` the bridge is vacuous and Prop. 6.8 is not needed.

## 7. Blast radius — CONFIRMED, documentary only

Because `Prop. 6.7` types only the microstep, repaired **Prop. 6.8 is
load-bearing for every St. 6.2 next-vertex consumer** — AF2 (R1/R2), III (S3),
A2P-REVIEW, MULTIPOLE (D5(c)/D6(a)), and the St. 9.6--9.11 template — and not
only for explicit pole manufacture.  Confirmed, with the sharpening that the
bridge is needed exactly when `kappa_0*(pi(H)-pi(G)) >= 2`.

The consumers' actual use is the contrapositive ("`H` not searrow, hence a
strict multiplicity inequality"), which is the implication the §5 composition
proves; so the composition really does discharge the dependency, not merely
weaken it.  **No mathematical rollback.**  The only actual changes are
documentary: St. 6.2's added `H in V_a cap T_a^+`, the Prop. 6.7 lattice rider,
the ledger's St. 3.11 usage row, and the r1 sweep rows.

## Required amendments before promotion

1. Close §3.3's `h=h_G` with the two-case argument of §1 above (Prop. 6.3 for
   the prefix, zero bracket for `m_G>m_F`).  **Load-bearing.**
2. Insert `d_E>0` (Prop. 6.7 clause 1) and steps (a)--(c) into §5.
3. Complete the cyclic residual lemma with Facts 1 and 2.
4. Strike the Prop. 5.1 / no-first-corner pins from §2.1; keep them in §2.2.
5. Fix the `beta/alpha` display and restate the reason as `alpha,beta>=2`.
6. Supply the `kappa*v in N` step in §4, and open Lemma 6.1 as an audit item.
7. Add the "enlargement would move the grid" justification.

Nothing here audits Sections 7--9, the mass formula, landing, or JC2.
