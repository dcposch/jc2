# Hostile review — Sigray Proposition 5.1 forced-puncture-shift repair

Reviewer model: **Claude Opus 5** (`claude-opus-5`), independent adversarial referee, round r1.
Date: 2026-08-28.
Producer under review: `xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md`.

# REPAIR

The mathematical core — Theorem 3.1, clauses (1)–(6) — **survives every attack I
mounted**. `b_P = g(P)` is correct and forced; condition (7) does hold at every
rational `v`; the bracket identity, the slope law, the descent, and the
existence/persistence/rationality of the first zero are all correct, and I
re-derived each from the primary source rather than from the producer's prose.
Three exact repairs are nevertheless required, one of them load-bearing:

* **R1 (load-bearing).** The producer's §7 "pole firewall" is written as a
  *usage discipline*. It is not: Notation 5.2 (p. 25) **defines**
  `T_{a,pole} := {F_P^* : P in Rbar_a \ R_a} ∩ T_a^+`, quantifying over *every*
  puncture. Under the printed reading a finite-nonzero puncture had **no**
  `F_P^*` at all (that is the GAP); under the repair it acquires one. Unless one
  proves the new elements land outside `T_a^+`, `T_{a,pole}` can grow, and
  Propositions 5.5–5.8, `Lambda(F)` (19) and the topological-degree formula (20)
  all over-count. The producer never proves non-leakage. It is true; §3 below
  supplies the proof (it is exactly the source's own **unproved** Statement 7.2,
  p. 35). This must be stated as a theorem, not a discipline.
* **R2.** The all-`v` typing correction is right but **over-corrected**. The
  single untyped flag on each branch is the unique `T_a^0` point, and
  `F_P^*` is **never** that point. The clean erratum keeps the sided towers and
  adds a sidedness dichotomy; the producer's replacement text records it only
  on the pole side.
* **R3.** §3's condition-(7) proof invokes "the corrected value dictionary of
  Statement 3.15", but uses only clause (ii), which is the **fixed point** of the
  audited (i)↔(iii) swap. The swap *is* load-bearing, but in §4, not §3. The two
  invocations must be split, or a reader will believe the theorem depends on an
  erratum it does not depend on.

Plus one checker-coverage defect (**R5**, §8: the frozen checker cannot detect a
sign error in the very identity it exists to certify) and minor textual nits.

None of this touches the promoted Proposition 4.2 repair, the pole book as
actually consumed, or any JC2 landing claim.

---

## 1. Custody, reproduction, and what I ran

Frozen inputs, recomputed at review time:

```
a0470416481378c02cc5a20e8aef826be1203c32c6dbfe664ae197cfdc34b9dc  xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md
f719ef535d1d27ac0a172eb41c6eef6f4027b484404cb7bb7b1df63586507fab  cases/sigray_prop51_forced_puncture_shift_20260828/verify_threshold.py
f3ece41268fdc1af9119dad3b598a3c4d9e819bc9101c6bdb2ba27b4224395c6  cases/sigray_prop51_forced_puncture_shift_20260828/CUSTODY.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

All four **match** the values in the charge.

Frozen checker, run verbatim (0.39 s, CPython 3, stdlib only):

```
SIGRAY_PROP51_FORCED_PUNCTURE_SHIFT_PASS
constant-q bracket classification: 47040
piecewise threshold profiles: 2814
forced-shift tail and negative controls: 5000
total grouped checks: 54854
```

I did **not** rest on it. I wrote and ran an independent stdlib replay
(`/tmp/p51rev/indep.py`, `/tmp/p51rev/witness.py`, `/tmp/p51rev/mutate.py`),
sharing no code with the producer's checker, implementing an exact
Laurent-in-`xi` / polynomial-in-`eta` bivariate ring with `Fraction`
exponents, plus an exact Puiseux-substitution engine over a real curve:

```
leading-bracket identity (rational xi-exponents): 4000
constant-q classification over rational d,e:      136080
deg p = 0 countermodel hits (must be > 0):        72
zero-bracket trichotomy realizable cases:         24000
e < 0 never zeros the bracket (deg p >= 1):       8000
first zero rational and attained:                 3000
INDEP_OPUS5_PROP51_ALL_PASS
```

I did not read or touch `jc2-lean`, and I edited no repository file other than
creating this report.

Page custody re-verified against the PDF (printed page = PDF page throughout):
Prop 4.1 + (7) + (8) **p. 18**; Prop 4.2 + the "(7) is automatic" Remark
**pp. 19–20**; Prop 4.3 + Not 4.2 **pp. 20–21**; Prop 4.6 **p. 23**;
Prop 5.1 **pp. 23–24**; Not 5.1, St 5.1 **p. 24**; Not 5.2, Prop 5.3 **p. 25**;
Prop 5.5 **p. 26**; Prop 5.6/5.7 **p. 27**; Prop 5.8, Not 6.1 **pp. 28–29**;
Not 7.1, St 7.1–7.3, Prop 7.1 **p. 35**; Prop 7.2, Not 7.2, Prop 7.3 **p. 36**;
Prop 7.3 proof **p. 37**; Not 8.1 **p. 39**. The producer's §2 custody list is
accurate.

---

## 2. Charge 1 — does `p_{f-a,F_v}` have positive degree at *every* rational truncation?

**CONFIRMED, and the producer's sourcing is better than it needed to be.**

Two independent derivations, both valid at non-vertices and past the last
characteristic exponent:

*Combinatorial (the producer's).* Fix rational `v >= 0` and choose a suitable
`kappa` (Not. 3.7, p. 12) with `kappa*v in N` — always possible, since any
multiple of a suitable `kappa` is suitable, and `p_{h,F}`, `d_{h,F}` are
`kappa`-independent (Not. 3.9/3.10, p. 13, define `eta_F` and `h^F`
intrinsically from the truncation). Then `F_v * c` exists for `c` the next
Puiseux coefficient of `P` (Not. 3.8, p. 12), so Statement 3.18 (p. 18) makes
`c` a root of `p_{F_v}`, hence `deg p_{f-a,F_v} >= 1`.

*Geometric.* Proposition 3.1(∗) (p. 14) says `deg p_{h,F}` counts the Puiseux
series of `h = 0` agreeing with the truncation. For `h = f-a` the branch `P`
itself is counted, so the count is `>= 1` for every `v`, including past
`alpha_m` where it drops to exactly 1.

Both require the audit-corrected Notation 3.13 reading `p_F := p_{f-a,F}`
(SIGRAY-AUDIT row Not 3.13, "load-bearing slip"); the producer says so
explicitly. Under the printed `h = f` reading the claim is false on `T_a^-` for
`a != 0`, exactly as the audit's Statement 3.13 erratum records.

Machine witness (`witness.py`, exact rational Puiseux substitution on the real
branch `y = 1/x` of `xy-1 = 0`), at `v in {0, 1/2, 1, 3/2, 2, 5/2, 7/2, 5}` —
i.e. vertices, non-vertices, half-integer flags, and the stable tail:

```
v=0    d=1     deg p=1        v=3/2  d=-1/2  deg p=1
v=1/2  d=1/2   deg p=1        v=2    d=-1    deg p=1
v=1    d=0     deg p=1        v=5    d=-4    deg p=1
```

`deg p >= 1` at every sampled `v`, with the slope `-1` tail predicted by
Statement 3.10(iii).

**This is where the producer separates cleanly from the promoted Prop 4.2
note.** That note's Lemma 2.1 proves `deg p >= 1` *only for* `F in T_a^+`
("since `d>0`, the coefficient of the largest positive power of `xi` must
vanish"). Proposition 5.1 needs it on all of `T_a`, including `T_a^0` and
`T_a^-`, where that argument is silent. The producer correctly reaches for
Statements 3.9/3.18 instead. No borrowing, no gap.

I also confirmed `deg p >= 1` is genuinely load-bearing and not decorative: with
`deg p = 0` allowed, my sweep finds **72** cases where the bracket vanishes with
`e != 0` and constant `q`, which would break step (3.8) outright.

---

## 3. Charge 2 — the forced `B_P = g - b_P` and condition (7)

### 3.1 The proof of clause (1) is correct

Condition (7) on p. 18 reads `(g-b)^+_F !≡ c in C`. Since `h^+_F = xi^{d_{h,F}}
p_{h,F}(eta)` with `p_{h,F} !≡ 0` by Notation 3.10, "identically a constant" is
exactly `d_{h,F} = 0` **and** `deg p_{h,F} = 0`. The producer's reading ("a
nonzero constant") is right.

Suppose `B_P^+_{F_v} = q in C^*`. Then `d_{B_P,F_v} = 0` and `p_{B_P,F_v} = q`
is a nonzero constant, which has **no roots at all**; so the hypothesis of
Statement 3.15 (p. 17), "`p_F` and `p_{h,F}` have no common root", holds
vacuously. Clause (ii) gives `B_P(P) in C^*`. But `B_P(P) = g(P) - g(P) = 0`
in the finite case and `= infinity` in the pole case. Contradiction. Hence (7)
holds for `b_P` at **every** rational `v`. **CONFIRMED.**

### 3.2 The label swap — the producer mis-attributes its own robustness (R3)

The audited erratum on Statement 3.15 is that (i) and (iii) are **swapped**.
Correct dictionary (re-derived: on the branch, `x(P) = infinity` by Statement
3.1(i), p. 10, and `h(P) ~ C x^{d_{h,F}}` with `C = p_{h,F}(eta_F(P)) != 0`):

```
d_{h,F} > 0  =>  h(P) = infinity      (printed: 0    -- WRONG)
d_{h,F} = 0  =>  h(P) in C^*          (printed: same -- CORRECT)
d_{h,F} < 0  =>  h(P) = 0             (printed: oo   -- WRONG)
```

Exact witnesses on `xy-1 = 0`, branch `y = 1/x`:

| `h` | `h(P)` | `d_{h,F_v}` (v>=3/2) | `deg p_{h,F_v}` | printed 3.15 | corrected 3.15 |
|---|---|---|---|---|---|
| `x`   | `oo` | `+1` | 0 | says 0 — **false** | says `oo` — **true** |
| `y`   | `0`  | `-1` | 0 | says `oo` — **false** | says 0 — **true** |
| `x*y` | `1`  | `0`  | 0 | says `C^*` — true | says `C^*` — true |

The row that clause (1) actually uses is the **third** one — the swap-invariant
case (ii). So the producer's phrase "the *corrected* value dictionary" is
misleading: clause (1) is immune to the E10 erratum, which is a robustness
*strength* that the current wording throws away. The corrected clause (iii) *is*
load-bearing, but in §4, where `r > 0` (i.e. `d_{g-b_P} < 0` at a zero value) is
asserted. Split the two citations. **REPAIR R3.**

Also confirmed by the same witnesses: the no-common-root hypothesis is not
decorative. For `h = f-a` one has `p_{h,F} = p_F`, which shares every root, so
Statement 3.15 is simply inapplicable to `f-a` — as it must be, since
`(f-a)(P) = 0` identically while `d_{f-a,F} > 0` below `u_0`.

### 3.3 Where (7) is and is not needed — a presentational correction

The producer writes "Proposition 4.1 applied to `(A,B_P)` now gives (2)",
immediately after proving (1), implying (7) is needed for `rho >= 0`. It is not.
Re-deriving Prop 4.1's proof: every term of `J_{(xi,eta)}(A^F, B^F)` has
`xi`-index `<= d_{A,F} + d_{B,F} - 1` unconditionally (`d_xi` lowers the index by
one, `d_eta` preserves it), while the chain rule forces `J = xi^{-u}`; hence
`rho >= 0` with **no hypothesis**. This matches the SIGRAY-AUDIT nit on Prop 4.1
("hypothesis (7) not load-bearing for 4.1 itself"). Condition (7) is load-bearing
in **two other places**, both of which the producer needs and gets right:

* step (3.8) — without (1), the case `deg q = 0, e = 0` gives a permanently zero
  bracket and `rho` never reaches zero (this *is* the printed defect);
* Proposition 4.3 (p. 20), whose hypothesis is literally "`b in C` satisfies (7)".

Recommend one clarifying sentence; no mathematical change.

---

## 4. Charge 3 — the leading bracket `d p q' - e p' q`

**CONFIRMED**, re-derived and machine-verified.

With `A^+_F = xi^d p(eta)`, `B^+_F = xi^e q(eta)`, `d, e in Q`:

```
J_(xi,eta)(xi^d p, xi^e q)
  = (d xi^{d-1} p)(xi^e q') - (xi^d p')(e xi^{e-1} q)
  = xi^{d+e-1} ( d p q' - e p' q ).
```

Verified symbolically on 4000 random instances with **rational** `xi`-exponents
(denominators up to 4, negative allowed) against a full bivariate Jacobian
computed in the Laurent ring — not the producer's shortcut. Consistency with
Prop 4.1's chain rule (`J_(x,y)(f,g) = 1`, `det ∂(xi,eta)/∂(x,y) = x^u`, so
`J_(xi,eta) = xi^{-u}`) also checks out.

`rho > 0 => deg q >= 1`, with all the corner cases the charge names:

* **`rho > 0`** forces the bracket `= 0` by (8) (this direction of (8) is
  unconditional; see §3.3).
* **`deg q = 0`**: then `q' = 0`, so the bracket collapses to `-e p' q`. Because
  `deg p >= 1` and we are in characteristic 0, `p' != 0`; and `q != 0`. Hence
  `e = 0`. Then `B^+ = q in C^*`, contradicting clause (1).
* **`d = 0`** is harmless: the argument never divides by `d` and never uses it.
  (This is the case the producer must handle and does — `d = 0` is the `T_a^0`
  flag, which occurs on *every* branch by Statement 3.13.)
* **`e = 0`** is the conclusion, not an assumption.
* **Laurent / inverse `e < 0`**: covered automatically. `e < 0` with `deg q = 0`
  gives bracket `= -e p' q != 0`, hence `rho = 0`, contradicting `rho > 0`. I
  verified independently that with `deg p >= 1` and `e < 0` the bracket is
  **never** zero (8000 random rational trials, zero exceptions) — this is
  the promoted Prop 4.2 note's Lemma 2.2(1), reproved here from scratch as
  `(q^{Nd} p^{-Ne})' = 0` forcing a nonconstant polynomial to be constant.

Constant-`q` classification over **rational** `d, e` (the frozen checker only
sweeps integers): 136 080 cases, bracket `= 0` iff `e = 0`, exactly as claimed.

---

## 5. Charge 4 — continuity, monotonicity, slope, descent, and the first zero

**CONFIRMED.** No jump and no open-endpoint countermodel exists, for structural
reasons:

* **Continuity**: Statement 3.10(ii) (p. 16) states `omega(u) = d_{h,I(u)}` is
  continuous, for each of `A` and `B_P` separately; `rho_P` adds a linear term.
* **Piecewise linearity with *finitely many* breakpoints**: Statement 3.10(iii),
  "except of finitely many rational points, the graph of `omega(u)` is locally on
  a line with slope `-omega^*(u)`". This is what licenses the producer's
  "integration across the finitely many rational breakpoints".
* **Slope (3.1)**: `rho_P' = d_A' + d_{B_P}' + 1 = 1 - deg p_{A,F_v} -
  deg p_{B_P,F_v}`. Cross-checked against Statement 3.9(iii) (`d_{h,F*c} =
  d_{h,F} - mult(p_{h,F},c)/kappa`) and 3.9(i) (`mult(p_{h,F},c) =
  deg(p_{h,F*c})`), which give the same slope on each linearity interval.
* **Monotonicity**: `deg p_A >= 1` (§2) makes the slope `<= -deg p_{B_P} <= 0`.
* **Descent**: wherever `rho_P > 0`, `deg p_A >= 1` and `deg q >= 1` give slope
  `<= -1`, so `rho_P(w) <= rho_P(v) - (w-v)`; with `rho_P >= 0` this cannot hold
  for all `w`, so a zero exists.
* **Attainment and rationality**: extend `rho_P` to `R_{>=0}` by its own
  piecewise-affine formula. `u_P := inf{v : rho_P(v)=0}` satisfies
  `rho_P(u_P)=0` by continuity, so the infimum is **attained** — no open
  endpoint. Rationality is forced twice over: breakpoints are rational
  (St 3.10(iii)); values are rational because `D_{h,F} = kappa_F d_{h,F} in Z`
  (Statement 3.8, p. 14); slopes are **integers**; so `u_P` is either a rational
  breakpoint or the zero of a rational-valued affine map with nonzero integer
  slope.
* **Persistence**: `rho_P >= 0`, nonincreasing, `rho_P(u_P) = 0` gives
  `rho_P ≡ 0` on `[u_P, ∞)`.
* **`u_P > 0`**: `rho_P(0) = d_{f-a,F_0} + d_{g-b_P,F_0} - 1`, and by Lemma 2.1(i)
  (p. 8) all four Newton degrees `k_f, l_f, k_g, l_g` are **positive**, so
  `rho_P(0) >= 1`. (This is the same fact Prop 5.3(i), p. 25, uses to exclude
  `(0,x),(0,y)` from `T_{a,pole}`.) Subtracting the constants `a, b_P` does not
  change these degrees.

I searched for a countermodel by randomly generating 3000 continuous
rational-breakpoint PL profiles with integer slopes `<= -1` while positive: in
every case the first zero was attained and rational. A jump would have to
violate St 3.10(ii); an irrational first zero would require a non-integer slope
or an irrational breakpoint, both excluded above.

---

## 6. Charges 5 & 6 — translation licence, `m = 0 iff rho = 0`, and the typing point

### 6.1 The translation is licensed (charge 5)

Proposition 4.3 (p. 20) is stated **verbatim** with `h_0 = g-b`, `b` satisfying
(7): no translation is needed at all on `T_a^-`, and the producer's clause (1)
supplies the hypothesis. Proposition 4.2 (p. 19) is stated only with `h_0 = g`,
so applying it to `B_P` does need a licence, and it is available:

* `J(f-a, g-b_P) = J(f,g)`, so `(f-a, g-b_P)` is a Keller pair with the same
  constant;
* by Notation 2.1 (p. 7), translation by constants is an automorphism `K`, so
  `(f-a, g-b_P) ~ (f,g)`, degrees are unchanged, and the pair is still almost
  normalized with the Lemma 2.1 Newton data;
* `T_a` depends only on the curve `{f = a} = {f-a = 0}`, and `d_{f-a,F}`,
  `p_{f-a,F}` are literally the same objects (this *is* the corrected Not 3.13
  reading).

One precision point the producer should state: the translated tower's recursion
is `h_{j+1} = h_j^{k_j} - s_j (f-a)^{l_j}`, i.e. Prop 4.3's form, not Prop 4.2's
printed `f^{l_j}`. This is inert at stage 0 — the only stage the theorem uses —
and inert on `T_a^+` anyway, where `f^+_F = (f-a)^+_F` (Statement 3.14's proof,
p. 17).

`m = 0 iff rho = 0` is **exact**: Prop 4.2(iv) and Prop 4.3(iv) at `m = 0` give
`mu_F = 0` and `J((f-a)^+_F, h^+_{0,F}) = xi^{-u} != 0`; Prop 4.1(8) says that
is equivalent to `rho = 0`; and `m > 0` is by construction the case
`J(f^+_F, h^+_{0,F}) = 0`, i.e. `rho > 0`. The producer's `l_j = 0` corner from
the promoted Prop 4.2 repair cannot occur at stage 0 for `B_P`, precisely because
clause (1) says `B_P^+` is never a nonzero constant. **CONFIRMED.**

### 6.2 `m_F` on `T_a^0`: the producer is right, and there is no hidden convention (charge 6)

I searched the whole thesis. `m_F` is introduced only at Proposition 4.2 (p. 19,
"Set `F in T_a^+`") and `m_{F,b}` only at Proposition 4.3 (p. 20, "Set
`F in T_a^-`"); the index entry (p. 65) lists `m_F` at page 19 alone. There is
**no** convention, extension, or default anywhere on `T_a^0`. The producer is
correct.

Worse than the producer says: by Statement 3.13 (p. 16, under the corrected
`d_{f-a}` reading) **every** branch has exactly one `T_a^0` flag `u_0`, and
`d_{f-a,I_P(·)}` is strictly decreasing (slope `<= -1`), so the path crosses
`T_a^+ -> T_a^0 -> T_a^-` exactly once. So the untyped point is never vacuous:
one of Proposition 5.1's clauses (ii)/(iii) is untyped for **every** puncture,
not just for pathological ones. The same over-broad typing recurs at
**Notation 8.1** (p. 39, "Set `F in T_a`") and **Statement 8.1** (p. 39, "Set
`F in V_a`"), both of which then invoke `m_F` — a pre-existing source-wide slip
family worth adding to the audit.

### 6.3 But the producer over-corrects (R2): `F_P^*` is never on `T_a^0`

Here is the sharpening the producer misses, and it changes the recommended
erratum.

**Lemma (sidedness).** Let `P in Rbar_a \ R_a`, and `b_P, B_P, u_P, F := F_P^* =
I_P(u_P)` as in the producer. Then

```
d_{B_P,F} != 0  and  d_{f-a,F} != 0,   and
g(P) = infinity  <=>  F in T_a^+  <=>  d_{B_P,F} > 0,
g(P) in C        <=>  F in T_a^-  <=>  d_{B_P,F} < 0.
```

*Proof.* (a) *No common root at `F`.* By Theorem 3.1(5), `rho_P(u_P) = 0` gives
`J(A^+_F, B^+_F) = xi^{-u_P} != 0`, i.e. `d p q' - e p' q` is a nonzero constant.
A common root `c^*` of `p` and `q` would make the left side vanish at
`eta = c^*`. So Statement 3.15 applies to `h = B_P` at `F`.

(b) *`d_{B_P,F} != 0`.* Otherwise 3.15(ii) gives `B_P(P) in C^*`, but
`B_P(P) in {0, infinity}`.

(c) *Sign reads the value.* Corrected 3.15: `d_{B_P,F} > 0 => B_P(P) = infinity
=> g(P) = infinity` (as `b_P` is finite); `d_{B_P,F} < 0 => B_P(P) = 0 =>
g(P) = b_P in C`. With (b) this is an equivalence.

(d) *`d_{f-a,F} != 0`, and it has the same sign.* By §5, `u_P > 0` and
`u_0 > 0`. Suppose `d_{f-a,F} >= 0`, i.e. `u_P <= u_0`. For every `w < u_P` we
then have `I_P(w) in T_a^+` and `rho_P(w) > 0`, so the repaired Proposition 4.2
applied to `(f-a, B_P)` gives `m_{I_P(w),b_P} >= 1`; its stage-0 relation is
`(B_P^+)^{k_0} = s_0 ((f-a)^+)^{l_0}` with `k_0 in N^*`, `l_0 in N`. Here
`l_0 = 0` would force `B_P^+` to be a nonzero constant (the repaired normal form
`(k,l,s) = (1,0,c)`), contradicting clause (1); so `l_0 >= 1`. By Proposition 4.4
(p. 21) the ratio `l_0/k_0` is independent of `w`; comparing `xi`-orders,
`d_{B_P,I_P(w)} = (l_0/k_0) d_{f-a,I_P(w)}`. Letting `w -> u_P` and using
continuity (St 3.10(ii)) gives `d_{B_P,F} = (l_0/k_0) d_{f-a,F} >= 0`, and with
(b) both are `> 0` — so `d_{f-a,F} = 0` is impossible and `d_{f-a,F} > 0`
implies `g(P) = infinity` by (c).
Conversely suppose `d_{f-a,F} < 0`, i.e. `u_P > u_0`, and suppose `g(P) =
infinity`. Then `b_P = 0`, `B_P = g`. For `v` large, `deg p_{g,I_P(v)} = 0`
(otherwise some branch of `{g = 0}` would agree with `P` to infinite order,
forcing a common irreducible factor of `f-a` and `g`, impossible since any such
factor divides `J(f,g) = 1`), so `d_{g,I_P(v)}` is eventually a constant
`e_inf`, and 3.15 (vacuous hypothesis) with value `infinity` gives `e_inf > 0`;
monotonicity (St 3.10(i)) then gives `d_{g,I_P(v)} > 0` for **all** `v`. But the
displayed stage-0 relation for `w < u_0 < u_P` gives `d_{g,I_P(w)} =
(l_0/k_0) d_{f-a,I_P(w)} -> 0` as `w -> u_0`, so `d_{g,I_P(u_0)} = 0`.
Contradiction. Hence `g(P) in C`. ∎

*Dependencies of this Lemma, disclosed.* Step (d) uses Proposition 4.4 (p. 21)
for the `w`-independence of `l_0/k_0`. Pointwise positivity of `d_{B_P,I_P(w)}`
needs only `k_0, l_0 in N^*`, but the converse half genuinely needs the ratio to
stay bounded as `w -> u_0`, and Proposition 4.4 is where that comes from. This is
also the step the printed Statement 5.1 (p. 24) takes, so the Lemma is no more
exposed than the source's own pole/finite separation. Note however that
Proposition 4.4's proof runs Statements 3.9/3.11 on a *general* `h`, and the
`kappa`-suitability hypothesis of Statement 3.9 is `h`-dependent (it asks that
`kappa` be a multiple of every `x`-pole order of `{h = 0}`, not of the fibre);
that `kappa`-enlargement clause is an open campaign item and is inherited here.
It does not affect Theorem 3.1 itself: the theorem's own chain uses Statement
3.18 and Statement 3.10 with `h in {f-a, g-b_P}` fixed, where "suitable" is the
ordinary notion for the two named curves.

Two immediate consequences.

1. **Proposition 5.1's clauses (i)/(iii) are typed at `F_P^*` in *both* cases**:
   `m_{F_P^*} = 0` in Prop 4.2's notation when `g(P) = infinity`, and
   `m_{F_P^*, b_P} = 0` in Prop 4.3's notation when `g(P) in C`. Only the single
   flag `u_0` — which is *never* `u_P` — is untyped, and it sits inside clause
   (ii) in the finite case, clause (iii) in the pole case.
2. **This is exactly the source's Statement 7.2** (p. 35: "`F^* !in T_{a,pole}`"
   for a `T_{a,cv}` flag), which is printed **without proof**. It is also
   exactly what Proposition 7.3's proof (p. 37) asserts as its step (i)
   ("`H in T_a^-`" for `w in (u,v)`).

So the producer's conclusion "the exact global statement is therefore the
`rho`/leading-Jacobian threshold. Its `m=0` translations are sided corollaries"
is *sufficient* but not the sharpest erratum: the sided towers can be kept, at
the cost of one extra sentence naming the side. Replacement text in §9.

---

## 7. Charges 7, 8, 9 — necessity of `b_P`, Section 7, and the pole firewall

### 7.1 Uniqueness/necessity of `b_P = g(P)` at finite punctures (charge 7)

**CONFIRMED.** For `b' != b_P = g(P) in C`, `(g-b')(P) = b_P - b' in C^*`. For
`v` large, `deg p_{g-b',I_P(v)} = 0` (same coprimality argument as in the Lemma),
so `d_{g-b',I_P(v)}` is eventually constant, and by 3.15(ii) — again the
swap-invariant clause — the value being in `C^*` forces that constant to be `0`.
Hence `(g-b')^+_{F_v}` is eventually a nonzero constant and (7) **fails**.
`b_P = g(P)` is the unique admissible centre at a finite puncture.

At a **pole** the situation is strictly stronger than the producer states, and
this is worth recording because it is the cleanest form of the firewall:
`d_{g,I_P(v)} > 0` for **all** `v` (proof in the Lemma, part (d)), so for every
`b in C` the constant `b` sits strictly below the leading `xi`-order and
`(g-b)^+_{F_v} = g^+_{F_v}` identically. Therefore at a pole

```
rho_b ≡ rho_0   for every b in C,
```

so the threshold, `F_P^*`, `m_{F_P^*}`, `h_0 = g`, `M_F`, `Q(F)` and `Lambda`
are *literally* `b`-independent — not merely "unchanged by the canonical choice
`b_P = 0`". The producer's weaker phrasing ("subtracting a finite constant does
not change the leading tail") is true but only about the tail.

**Stable-tail model (4.1)–(4.2): what is proved vs. what is sampled.**
`r := -d_{g-b_P,F_v} > 0` in the tail is a *geometric* consequence of corrected
Statement 3.15(iii) (value `0` at `P`). `deg p_A = 1` past the last
characteristic exponent is geometric (Prop 3.1(∗)). But `d_A(v) = r+1-v` is
**not** independent input: it is exactly `rho_P(v) = 0`, i.e. the conclusion of
Theorem 3.1 read backwards. Consequently the checker's
`check_stable_tail_and_negative_controls` assertions `rho_shifted == 0` and
`rho_unshifted == r` (lines 127–128) are algebraic tautologies of that
substitution and prove nothing on their own; the only non-tautological content in
that group is the bracket comparison on lines 133–134 (`e = -r != 0` gives a
nonzero bracket; `e = 0` gives zero). I confirmed this by direct expansion, and
by noting that the very same profile with a **non**-Keller pair (`f-a = xy-1`,
`h = y`, giving `rho ≡ -1 < 0`) is arithmetically consistent — so `rho >= 0` is
Keller-specific and comes from Prop 4.1, not from the checker.

### 7.2 Proposition 7.3: corroboration, not circularity (charge 8)

**No circularity.** The producer's Theorem 3.1 (§3 of the producer) cites only
Statements 3.9, 3.10, 3.15, 3.18 and Propositions 4.1/4.2/4.3. Nothing from
Section 7 enters. Section 7 is used solely as authorial-intent evidence in the
producer's §6. That is legitimate and the evidence is strong — stronger than the
producer claims:

Proposition 7.3's proof (p. 37) sets `b := q(c)` and then writes, at
`G := F_P^*`,

```
1 - v = d_{f-a,G} + d_{g-b,G},
```

which is verbatim `rho_P(v) = 0` **for the shifted `rho`**. It also asserts
`J((f-a)^+_H, (g-b)^+_H) = 0` for all `u < w < v` — verbatim "`rho_P > 0` below
the threshold". And `q(c) = g(P)` is itself correct: at `F in T_{a,cv} ⊂ T_a^0`
one has `d_{g,F} = 0`, so `g(P) = p_{g,F}(eta_F(P)) = q(c)`.

So **Section 7 is internally consistent only with the repaired, shifted
Proposition 5.1.** The repair therefore *fixes* Proposition 7.3's proof, and in
particular supplies the (7) hypothesis that Prop 7.3 needs to invoke Prop 4.3
with `b = q(c)` and never verifies. The producer's §6 ("The repaired threshold
does not by itself repair any other Section 7 input") **under-claims**; this
should be corrected in the producer's favour.

**What remains open downstream** (I checked each):

| item | page | status after the repair |
|---|---|---|
| Prop 5.1 clauses (ii)/(iii) | 23–24 | untyped at the single `T_a^0` flag `u_0`; needs the §9 wording |
| Not 5.1 | 24 | fine, but must now carry `b_P` and the side (R2) |
| St 5.1 (`d_{g,F} > 0 iff d_F > 0`) | 24 | **survives verbatim**: on `T_a^+` below `u_P`, `d_{B_P} > 0` so `g^+_H = B_P^+_H` and the stage-0 relation is the same, which is all its proof uses |
| Not 5.2 / `T_{a,pole}` | 25 | **needs the Lemma of §6.3** — see R1 below |
| Prop 5.5, 5.6, 5.7, 5.8 | 26–28 | unchanged *given* R1 |
| Prop 7.2 | 36 | still **no printed proof** (producer is right) |
| Prop 7.3 | 36–37 | proof now closes; its unstated (7) hypothesis is supplied |
| St 7.2 | 35 | still unproved in the source; proved here in §6.3 |
| St 3.14 conjugation twist | 16–17 | untouched, as the producer says |
| Not 8.1 / St 8.1 typing | 39 | pre-existing over-broad domain, unaffected |
| "By Proposition 8" | 24 | occurs **twice**, not once (producer says "citation", singular) |

### 7.3 The firewall is a theorem obligation, not a discipline (charge 9, **R1**)

This is the one place the producer is materially incomplete.

`Notation 5.2` (p. 25) reads
`T_{a,pole} := {F_P^* : P in Rbar_a \ R_a} ∩ T_a^+` — a quantifier over **all**
punctures. Under the printed reading a finite-nonzero puncture had no `F_P^*`
(the GAP), so the set was implicitly the pole set. **The repair changes this**:
every puncture now has an `F_P^*`. If a finite puncture's `F_P^*` could land in
`T_a^+`, `T_{a,pole}` would strictly grow and then

* `Lambda(F)` (19, p. 27) would sum over the wrong `P`,
* `td(f,g)` (20, p. 28) would over-count,
* Prop 5.3's structural consequences and every AF3/A3L1/TDUNIFORM entry-`M`
  pin would be asserted at flags where they are false.

The producer's §7 handles this by *instructing consumers* ("require
`g(P) = infinity` explicitly", "must not be inserted into `T_{a,pole}`"). That is
not enough: a definition cannot be firewalled by convention. The needed fact is
the Lemma of §6.3(c)–(d), i.e. the source's unproved Statement 7.2. With it,
`{F_P^* : g(P) in C} ⊂ T_a^-`, so the `∩ T_a^+` in Notation 5.2 still does all
the filtering and `T_{a,pole}` is **provably unchanged**.

Given that, I confirm the rest of charge 9 item by item, for `g(P) = infinity`:
`b_P = 0` and `B_P = g`; `rho_b ≡ rho_0` for every `b` (§7.1), so the selected
positive pole vertex `F_P^*` is literally the printed one; `m_{F_P^*} = 0` in
Prop 4.2's own notation; `h_0 = g`; `M_{F_P^*} = gcd(deg p_{F_P^*},
deg p_{g,F_P^*})` by Notation 8.1 at `m = 0` (matching the producer's §7 item 5
and AF3 §1 step 4); `Q(F) = (D_F, deg p_F, nu_F, M_F, kappa_F(1-pi(F)))`
unchanged; `Lambda(P)` (18) and `Lambda(F)` (19) unchanged.

**Leakage audit of live consumers.** I read the actual uses:
`SHEET6-AF3.md` §1 steps 1–4, `SHEET6-A3L1-REVIEW.md` front 1,
`SHEET6-TDUNIFORM.md` §68, `SHEET6-CAMPAIGN.md` §273. Every one of them invokes
Prop 5.1 **only at `F_P^*` itself** (`u^* = u`) and only to obtain `m_{F_P^*}=0`;
A3L1 even states "the (iii) `u^* >= u` clause is not even needed". So none of
them touches the untyped `T_a^0` flag or any finite threshold. **No leakage
found**, conditional on R1 being proved. One residual note: `A3L1` derives
"pole vertices are always searrow" from `d_F + d_{g,F} = 1-u`, i.e. from
`rho ≡ 0` at `F_P^*` — at a pole this is the *unshifted* `rho`, which by §7.1
equals the shifted one, so it is safe.

### 7.4 Separation from the promoted Proposition 4.2 repair (charge 10)

**Clean in both directions.**

*Prop 4.2 -> Prop 5.1:* the promoted note's §6.5 explicitly disclaims
("**No Proposition 5.1 promotion.** The separate finite-puncture defect in the
printed `b=0` threshold argument remains"). The producer draws exactly two
things from it: (a) that Prop 4.2 is well-defined at all (needed so that "the
tower has length 0" is a statement), and (b) the `(k,l,s) = (1,0,c)` normal
form, which I used above to conclude `l_0 >= 1`. Both are correctly attributed.
Crucially, the producer does **not** import that note's Lemma 2.1, which is
`T_a^+`-only and would not have sufficed (§2).

*Prop 5.1 -> Prop 4.2:* the producer claims nothing about Prop 4.2. One caution
for future consumers: clause (1) of Theorem 3.1 must **not** be quoted as
reinstating the p. 20 Remark ("condition (7) automatically holds in the case
`d_F > 0`"), which the promoted repair deleted as circular. Clause (1) is about
`b = b_P` at all flags, a different statement. (As a by-product of §6.3(d) the
Remark *is* recoverable — on `T_a^+` below `u_P` one gets `d_{B_P,F} > 0`, hence
`(g-b)^+_F = B_P^+_F` has positive `xi`-order for every `b in C`, hence (7); and
above `u_P` we are in the pole case where `d_g > 0` everywhere. But that
derivation runs through the Prop 5.1 repair, so it must be filed there, not
restored to p. 20 as if it were the printed argument.)

---

## 8. Checker audit (R5)

The frozen checker is honest about its scope and its arithmetic is correct
(I re-implemented all three groups independently and got matching results). Its
falsification power is uneven; I mutation-tested it:

| mutation | detected? |
|---|---|
| M1 bracket sign: `d p q' **+** e p' q` | **NOT DETECTED — still PASSes** |
| M2 bracket swap: `e p q' - d p' q` | detected |
| M3 allow `deg p = 0` in the constant-`q` sweep | detected |
| M4 slope allows `deg p_A = 0` | detected |
| M5 affine-piece slope allows `deg q = 0` | detected |
| M6 drop the shift in the tail (`rho_unshifted := d_a - r + v - 1`) | detected |
| M7 wrong shift `e=0` declared to have nonzero bracket | detected |
| M8 stable-tail `d_A` off by one | detected |
| M9 `d_shifted := +r` | detected |
| M10 profile descent bound reversed | detected |

**M1 is a real coverage hole.** Both call sites of `bracket_coefficient`
(lines 62–66 and 133–134) pass a **constant** `q`, so `q' = 0` and the first term
`d*p*q'` is identically zero. The checker therefore never evaluates the identity
it is named for on a non-constant `q`, and cannot distinguish
`d p q' - e p' q` from `d p q' + e p' q` — the exact sign that Proposition 4.1's
equation (8) and the producer's (3.7) turn on. The sign is **correct** (I verified
it symbolically against the full bivariate Jacobian over rational `xi`-exponents),
but the artifact does not certify it. Minimal fix: add one group evaluating
`bracket_coefficient` against an independently computed
`J(xi^d p, xi^e q)` for non-constant `p` and `q`.

Secondary, non-blocking: `check_piecewise_threshold_profiles` (lines 78–114) is
close to tautological — the first loop asserts the monotonicity and linear-descent
bound that its own construction produces, and the second asserts
`rho0 + slope*(rho0/-slope) == 0`. Mutations M4/M5 do fire (they encode
`deg p, deg q >= 1 => slope <= -1`), so it is not literally empty, but it carries
none of the theorem's content: nothing here bears on Statement 3.10's continuity,
finiteness of breakpoints, or attainment of the infimum, which is where the real
work is. The CUSTODY.md disclaimer covers this accurately.

---

## 9. Required repairs — replacement text

**R1. Replace the producer's §7 opening with a theorem.** Insert before the
numbered discipline list:

> **Proposition (non-leakage; = the source's Statement 7.2, p. 35, there
> unproved).** For every `P in Rbar_a \ R_a`, `F_P^* in T_a^+` if
> `g(P) = infinity` and `F_P^* in T_a^-` if `g(P) in C`; `F_P^* in T_a^0` never.
> Consequently
> `T_{a,pole} = {F_P^* : P in Rbar_a \ R_a} ∩ T_a^+ = {F_P^* : g(P) = infinity}`
> is unchanged by the repair, and Propositions 5.3–5.8, the pole entry book,
> `Lambda(P)` (18), `Lambda(F)` (19) and `td(f,g)` (20) are unchanged as
> statements, not merely by convention.

(Proof as in §6.3 above.) The existing numbered list may stay as consumer
guidance, but it must no longer be the load-bearing argument.

**R2. Replace the producer's §5 erratum text.** For Proposition 5.1:

> **Proposition 5.1 (corrected).** Let `P in Rbar_a \ R_a`. Put `b_P = g(P)` if
> `g(P)` is finite and `b_P = 0` otherwise, and set
> `rho_P(v) = d_{f-a,I_P(v)} + d_{g-b_P,I_P(v)} + v - 1`. There is a unique
> `u_P in Q_+` with `rho_P(v) > 0` for `v < u_P` and `rho_P(v) = 0` for
> `v >= u_P`. Equivalently, `u_P` is the first `v` at which
> `J((f-a)^+_{I_P(v)}, (g-b_P)^+_{I_P(v)})` is nonzero. Moreover
> `F_P^* := I_P(u_P)` lies in `T_a^+` when `g(P) = infinity` and in `T_a^-` when
> `g(P) in C`; it never lies in `T_a^0`. Accordingly `m_{F_P^*} = 0` in the
> sense of Proposition 4.2 in the first case, and `m_{F_P^*, b_P} = 0` in the
> sense of Proposition 4.3 in the second. At the unique flag `I_P(u_0)` with
> `d_{f-a} = 0` neither tower is defined, and the correct reading of clauses
> (ii)/(iii) there is the leading-Jacobian predicate
> `J((f-a)^+_F, (g-b_P)^+_F) = 0` (resp. `!= 0`).

For Notation 5.1:

> Define `F_P^* := I_P(u_P)` and retain `b_P` with this datum. When
> `g(P) = infinity` one has `b_P = 0` and in fact `rho_b ≡ rho_0` for every
> `b in C`, so `F_P^*`, `m_{F_P^*} = 0`, `h_0 = g`, `M_{F_P^*}`, `Q(F_P^*)` and
> `Lambda` are literally the printed objects. When `g(P) in C`, `F_P^*` carries
> the datum `b_P = g(P)` and lies strictly deeper than the unique flag
> `Fhat_P in T_{a,cv}` of Notation 7.2.

Also: "At **vertices** in `T_a^+`" should read "At **flags** in `T_a^+`" —
Proposition 4.2/4.3 apply to all of `T_a^{+/-}`, not only to `V_a`; and "The
printed citation 'By Proposition 8' on p. 24" should read "The two printed
citations".

**R3. Split the Statement 3.15 invocations** in the producer's §3 and §4:

> ... so the hypothesis of Statement 3.15 holds vacuously and its clause (ii) —
> which is unaffected by the audited (i)/(iii) label swap — gives
> `B_P(P) in C^*`.

and in §4:

> ... write `r > 0` for the negative order of `g-b_P` at `P` (Statement 3.15,
> clause (iii) **as corrected by E10**: value `0` corresponds to `d < 0`).

**R5.** Extend `verify_threshold.py` with one non-constant-`q` group comparing
`bracket_coefficient(d,p,e,q)` to an independently expanded
`J(xi^d p, xi^e q)`; the present artifact passes with the sign of the second
term reversed.

**Optional but recommended.** State in the producer's §6 that the repair *does*
close Proposition 7.3's proof (which silently needs both the shifted `rho` at
`F_P^*` and condition (7) for `b = q(c)`), rather than the current
"does not by itself repair any other Section 7 input".

---

## 10. Ledger of defects, by owner

**Producer defects** (this artifact):

1. §7 firewall stated as discipline where a theorem is required (**R1**).
2. §5 erratum text omits the sidedness dichotomy and over-corrects the typing
   point (**R2**).
3. §3 mis-attributes its condition-(7) proof to the *corrected* Statement 3.15;
   it uses only the swap-invariant clause (ii) (**R3**).
4. §3's ordering suggests (7) is needed for `rho >= 0` in Prop 4.1; it is not.
5. §5 "vertices" should be "flags"; "the printed citation" should be plural.
6. §6 under-claims: the repair does close Prop 7.3's proof.
7. §4's (4.1) is presented as a model but is a corollary of Theorem 3.1; the
   checker's group 3 inherits this and is partly tautological.
8. Checker cannot certify the sign of `d p q' - e p' q` (**R5**).

**Pre-existing source defects** (Sigray, not the producer — several already
carried in `ladder/SIGRAY-AUDIT.md`):

* Prop 5.1 (pp. 23–24): unshifted `rho` and un-subscripted `m_F` over all `v`;
  "By Proposition 8" twice; `(g^+)^l = (f^+)^k` has `k,l` swapped relative to
  Prop 4.2(iii) and drops `s_j`. [The GAP the producer repairs.]
* Statement 3.15 (p. 17): (i)/(iii) swapped [E10, known]; hypothesis needs
  `p_{f-a,F}`.
* Notation 3.13 / Statement 3.13 / Notation 3.14 (p. 16): `f` vs `f-a` slip
  family [known].
* Statement 7.2 (p. 35), Proposition 7.2 (p. 36): stated **without proof**.
  St 7.2 is proved here; Prop 7.2 remains open.
* Prop 7.3 (p. 37): invokes Prop 4.3 with `b = q(c)` without verifying (7);
  "`(g_H - b)^+ = ((f-a)^+_F)^k`" mixes `F`/`H` subscripts and drops `s`.
* Prop 4.3(iv) (p. 21): writes `(f^+_F)^mu` where `((f-a)^+_F)^mu` is meant
  (inert at `mu = 0`, which is all the producer uses).
* Notation 8.1 and Statement 8.1 (p. 39): domains "`F in T_a`" / "`F in V_a`"
  while invoking `m_F`, defined only on `T_a^+` — same typing family as Prop 5.1.
* Prop 4.2/4.3 (pp. 19–20): tuple arity printed as `N^{*m-1}` for `m` entries.
* p. 20 Remark ("(7) is automatic when `d_F > 0`"): circular as printed
  [deleted by the promoted Prop 4.2 repair]; recoverable only via the present
  Prop 5.1 repair, and so must not be restored in place.

---

## 11. Bottom line

`b_P = g(P)` at finite punctures and `b_P = 0` at poles is the correct and unique
centre; condition (7) then holds at **every** flag, `rho_P` is a continuous,
nonincreasing, finitely-piecewise-linear, integer-slope, nonnegative function
whose first zero exists, is attained, and is rational; and that zero is exactly
the first flag at which the leading Jacobian of `(f-a, g-b_P)` is nonzero. The
theorem stands. What must be added before promotion is the non-leakage
proposition that keeps `T_{a,pole}` — and with it the entire pole book, the
`Lambda`-masses and `td(f,g)` — provably unchanged, together with the sidedness
sentence that types clauses (i)/(iii) on both sides and localises the untyped
point to the single `T_a^0` flag.

Verdict: **REPAIR**.

---

## 12. Hashes

Frozen inputs re-verified at review time — **all three named inputs still
match**, as does the source PDF:

```
a0470416481378c02cc5a20e8aef826be1203c32c6dbfe664ae197cfdc34b9dc  xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md      MATCH
f719ef535d1d27ac0a172eb41c6eef6f4027b484404cb7bb7b1df63586507fab  cases/sigray_prop51_forced_puncture_shift_20260828/verify_threshold.py MATCH
f3ece41268fdc1af9119dad3b598a3c4d9e819bc9101c6bdb2ba27b4224395c6  cases/sigray_prop51_forced_puncture_shift_20260828/CUSTODY.md          MATCH
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf                                                  MATCH
```

SHA256 of this report. A file cannot contain its own digest, so the seal is
taken over the report body, defined as this file with its final line removed;
the recomputation recipe is exact:

```
sed '$d' xmodel/sigray-prop51-forced-puncture-shift-hostile-review-opus5-20260828-r1.md | shasum -a 256
```

Report-body SHA256: `0566bc3a1ec19bf32cdd79ee6a382f5e27a37268e5b531917cfd6b163ff7d2f3`
