# Hostile review — `td=8` trunk exit-set charge is at least three

Lane: Opus 5, different-model hostile review, adversarial and independent.
Date: 2026-08-29 UTC. Executed from `/Users/dc/code/math/jc2`.

Target: `xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md`
(Sol 5.6 primary, lifecycle `PRODUCER_CHECKED`).

Perimeter honoured, without exception: no access, listing, search, build,
status, or control of `jc2-lean` or any nested formalization tree; no web; no
AWS; no CAS (no Singular, msolve, Sage, PARI, Macaulay); no canonical file,
source packet, prompt, adapter, or target edited; no commit; no push; no
workspace-wide `git status`. Desk arithmetic is exact `int`/`Fraction` in a
single throwaway `/tmp` heredoc (87 checks, 0 failures, reproduced in §8).
`refs/sigray_full.pdf` was re-read on-page with `pdftotext`; every
load-bearing formula was taken from a display line or a numbered statement,
respecting the recorded stacked-fraction hazard. Only this report was
written.

---

## 0. Verdict

**`PASS_WITH_REPAIR`** at claim level.

**Theorem truth — CONFIRMED.** The headline inequality (0.1),

```text
lambda_F^exit(c_*) = sum_{H in E_F(c_*)} kappa_H(pi(H)-1) >= 3,
```

is **true** on every member of the reviewed `td=8` equal-join affine family,
uniformly for every integer `t >= 0`. The route kill in §4 is **valid**: the
four selected critical-value flags are pairwise distinct elements of
`T_{a,cv}` for one fibre `a`, their total actual weight is at least
`2+2+3+1 = 8`, and repaired Corollary 7.1 caps any such set at
`td(f,g)-1 = 7`. The central diagnosis is right: the old criterion priced one
selected ray and consumed it as the whole exit-set charge.

**One genuine repair — R1 (§4 below).** The §3 **arity dichotomy is not a
valid proof**. Its Case B step "`|E_F(c_*)|=1` implies `N(tau)=2i` on
`(0,tau_0]`" **conflates Puiseux series with places**. The Eggers–Wall tree of
Definition 3.3 is built on the *finite point set* `Ra_bar \ Ra` with
`O(P,P*)` defined in Definition 3.2 as the **maximum** contact over
corresponding series, so a single place can shed Galois-conjugate series at
its own characteristic exponents **without splitting its ray, its flag, or its
`E_F(c_*)` entry**, while `deg(p_{I(u)})` counts series (Proposition 3.1(*),
proved in the `kappa`-cover `R^*`). Hence `tau_0 = 17/2` is **not** forced in
the single-flag case, `w_H = 3q/2` is **not** the general single-flag value,
and "`3q/2` integral, so `q` is even" does **not** follow. The target's own
reviewed dependency contains the counterexample in miniature: the confirmed
A-step **conjugate regime** (`E_+ = 2`) is a single place, a single ray, a
single cv flag, and `N` dropping `2 -> 1`.

The repair is two lines inside the target's own dependencies, replaces the
arity dichotomy by a **ramification dichotomy**, and yields the same bound:

```text
q := kappa_H/kappa_F in N* (Theorem A(4)), tau_0 >= D_F/m = 17/2 always.
(1) some flag has q >= 2   ->  w_H = q(tau_0-7) >= 2*(3/2) = 3.
(2) a flag has q = 1       ->  no characteristic level in (pi(F),u_0], so no
    conjugate shedding; if additionally |E_F(c_*)|=1 then N == 2i, tau_0=17/2,
    w_H = 3/2 not in N*, contradicting (INT).  So q=1 forces |E_F(c_*)|>=2,
    with a second, non-conjugate flag; both weigh >= 2, total >= 4.
Hence lambda_F^exit(c_*) >= 3, with equality only at q=2, tau_0=17/2.
```

**Terminology — no repair needed.** Calling the sum a trunk first-exit charge
is legitimate: it is literally `lambda_i^exit` of the reviewed Section-9
first-separation repair (4.2), restricted to one direction. §4 does not even
need the name.

**Quotient/orbit caveat — resolved, and it cuts only one way.** The
"cyclically conjugate roots in one orbit count as one direction" clause of the
first-exit repair, and Terra's "one orbit is one direction", are **not extra
assumptions**: they are Definitions 3.2–3.3 plus the Statement 3.2 selector
`Omega`. Consequently distinct tree vertices **are** distinct elements of
`T_{a,cv}` (Case A is safe from over-counting), while conjugate *series* are
**not** distinct rays (Case B's inference is unsafe). The target got the safe
half right and the unsafe half wrong.

**Maximum safe consequence and campaign implication:** §9.

---

## 1. Custody and provenance

### 1.1 Target seals — verified

```text
full  3c2c9a7ed79cc6d05ec3ba7098c1dc89cabb3547791d777c4bf8971d1ae28e39   MATCHES prompt
body  688dbf41e3e3b6c777ec7267c8114569c4507261eb6dea9003dc6236c330494c   MATCHES prompt and self-footer
```

Target size 9531 bytes, 257 lines; separator `---` at line 255. Body
convention decided by experiment, not assumed: lines 1..254 hash to the
declared body value; lines 1..253 give `ae9d2a8f31f39f612bc80fa138...`, so
the convention is "all bytes up to and including the blank line preceding the
separator".

### 1.2 Pinned dependencies — all nine recomputed byte-exact

```text
910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4  m2-td8-equal-join-st39-coefficient-transport-primary-fable5-20260829.md
e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61  m2-td8-equal-join-st39-coefficient-transport-primary-hostile-review-opus5-20260829.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  sigray-section9-source-audit-hostile-review-gpt55-20260828.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

Every hash printed in the target's §1 reproduces exactly. No dependency
substitution, no stale pin, no missing file. The Section-7 amended hash
`c253bd12...` is exactly the one Terra gated **PASS** (the original
`5036f9a2...` is the FAILed version and is correctly not cited).

### 1.3 Source pages re-read directly by this lane

`refs/sigray_full.pdf`, printed page = pdf page:
pp. 10–14 (Statement 3.1, **Definitions 3.1–3.4**, Notations 3.1–3.12,
Statements 3.2–3.8, **Proposition 3.1** with its `R^*` proof, Statement 3.9
verbatim); pp. 14–16 (Statements 3.10, 3.11, 3.13, Notation 3.14, Statement
3.14); p. 28 (**Notation 6.1** `T_a^up`/`T_a^down`, Statements 6.1–6.2,
Proposition 6.3); pp. 34–39 (Notation 7.1, **Statements 7.1–7.3**,
Propositions 7.1–7.5, **Corollary 7.1** verbatim).

I did **not** take the target's word, the primaries' word, or any prior
campaign summary for: Definition 3.2's max-contact clause, Definition 3.3's
carrier set, Notation 3.5's `kappa_F` convention, Proposition 3.1(*)'s
counting object, Notation 6.1's up/down test, Statement 7.3's conclusion, or
Corollary 7.1's exact form. Each was read on-page and is quoted below where
load-bearing.

---

## 2. The claim, reconstructed from source

Frozen trunk data, re-derived and cross-checked against the pinned transport
primary (its `i`-table row `trunk (nu=17) | (85,35), mult (3,2) | 112+84t`)
and the pinned exact-lambda primary's normalization ledger:

```text
i := i_F = 112+84t = 28(4+3t)          t >= 0
reduced trunk pattern  Phi = (eta^17-A)^3 (eta^17-B)^2,  B=(4/3)A,  p_F = C Phi^i
deg p_F = 17*3i + 17*2i = 85 i         (no 0-root; two nonzero mu_17 orbits)
extra orbit = the reduced-multiplicity-2 orbit;  c_*^17 = B != 0
m := mult(p_F,c_*) = 2i                (Notation 3.12 at one root, not one orbit)
D_F = 17 i,   kbar_F = kappa_F(1-pi(F)) = 7,   chain arrival = mult-3 orbit
```

Independent consistency checks this lane ran (all pass, all `t`):
`deg p_G = 336+252t = 3i` equals `mult(p_F, c_chain)` for the mult-3 arrival,
closing Statement 3.9(i) on the chain edge; `D_F/deg p_F = 17i/85i = 1/5`
reproduces the recorded frame `rho`; and the trunk's letters differ
cosmetically between packets (`B=(4/3)A` in the target, `D=(4/3)C` in the
reviewed Prop 8.1(iv) derivation `-68C+51D=0`) but denote the same orbit with
the same ratio `4/3` and the same reduced multiplicity 2.

Corrected Statement 9.3, `c_* != 0` branch (Section-9 audit (4.1); the E6 sign
repair re-verified this lane against the proof's own chain
`kappa_F(w-1) = kappa_F(w-u) - kappa_F(1-u)`):

```text
kappa_H(pi(H)-1) >= D_F/mult(p_F,c_*) - kbar_F = 17i/(2i) - 7 = 3/2.
```

Exact separation law (my own primary's Theorem A, Fable-confirmed clause by
clause), with `tau := kappa_F(u-pi(F))`, `N(tau) := deg p_{I_P(u)}`,
`tau_0 := kappa_F(u_0-pi(F))`:

```text
(A1) N non-increasing integer step function, N(0+) = m, N >= 1
(A2) D_F = integral_0^{tau_0} N dtau                     => tau_0 >= D_F/m
(A3) kappa_F(pi(H)-1) = tau_0 - kbar_F
(A4) q := kappa_H/kappa_F = E_+/E_0 in N*, dividing E_+ <= m
(A5) w_H = kappa_H(pi(H)-1) = q(tau_0 - kbar_F) in N*    (INT)
```

`(INT)` — `kappa_H(pi(H)-1) in N*` for **every** `H in T_{a,cv}` — is proved
at printed-proof scope inside Proposition 7.3 (the perturbed point `Q` has
`Lambda(Q) = kappa_G pi(G) - kappa_G`, a pole/zero order at an actual place,
hence a positive integer). Fable's review confirms this; I re-read pp. 36–38
and concur, with the same disclosed caveat that "`p_G` squarefree" must be
read "`p_G - a*` squarefree".

---

## 3. Clause-level findings on the seven attack points

### 3.1 Point 1 — does Statement 7.3 flag every ray, and can the flags be used simultaneously?

**Answer: YES, YES, and YES — confirmed on-page, with one typing obligation
the target left implicit but which holds.**

Statement 7.3, verbatim (p. 35):

> Set `P in Ra_bar \ Ra`. Assume that there exists `u in Q+` such that
> `I_P(u) in T_a^up`. Then there exists `v in Q+` such that
> `I_P(v) in T_{a,cv}`.

The hypothesis is a **typing obligation on the exit child**, which the target
does not discharge. I discharged it directly. Notation 6.1 (p. 28):
`T_a^up := {F in T_a^+ : d_F > (1-pi(F)) deg(p_F)}`; Statement 6.2 turns this
into the parent test `d_F >= (1-pi(F)) mult(p_F,c_*)`, i.e. exactly
`D_F/m > kbar_F`. On the trunk that is `17/2 > 7`: **true**, so
`F*c_* in T_a^up`. Pleasingly, the "exit child is up" condition and the
positivity of the corrected Statement 9.3 gap are the *same inequality*; the
family sits `3/2` above the boundary, `t`-uniformly. `T_a^+` membership also
holds (`d` after the first `kappa_F`-microstep has normalized area
`17i-2i = 15i > 0`). The target's implicit reliance on singleton-pole
regularity to type the child as up is therefore **not needed** — and that
matters, because this is a *two*-pole equal-join and the singleton-pole
regularity lemma is not available at the merge (§3.6).

Flag level: `T_{a,cv} := {F in T_a^0 : d_{g,F} = 0}` (Notation 7.1) and
`T_a^0 = {F : d_F = 0}`; Statement 3.13 gives a **unique** `u` per point with
`d_{I(u)} = 0`. Hence the flag Statement 7.3 produces is forced to sit at that
same `u_0`, i.e. `H = I_P(u_0)` and `pi(H) = u_0`; `pi(H) > 1` by Statement
7.1. So every place through `F*c_*` has exactly one cv flag, at its own
Statement 3.13 level.

Remerging: impossible, and for the sharper reason the target does not give.
`I_P(u) = I_{P*}(u)` iff `u <= O(P,P*)` (Definition 3.3), so the set of levels
at which two rays coincide is a *down-set* — this is the no-remerging property
and it is definitional, not an appeal to intuition about trees.

Simultaneous use: Corollary 7.1 is stated on-page for a **set**
`{F_1,...,F_n} subset T_{a,cv}`, and the repaired actual-weight version
`(C7.1*)` is explicitly asserted "for every subset of pairwise distinct
critical-value flags" because every omitted term is positive (Statement 7.1
gives `pi(F) > 1`). So all the actual weights may be used at once. **No
selection or budget-sharing obstruction exists.**

### 3.2 Point 2 — does corrected Statement 9.3 give every descendant flag the same `3/2`?

**Answer: YES for every flag in the exit set, and the typing checks all pass.
The target's §2 claim is correct.**

The cleanest justification is not the printed Statement 9.3 but (A2)+(A4):
`N <= m` and `D_F = int N dtau` give `tau_0 >= D_F/m` for **every** ray
through `F*c_*` whatever its degree profile, and `q >= 1`, so
`w_H >= D_F/m - kbar_F = 3/2` for every `H in E_F(c_*)`. With `(INT)` this is
`w_H >= 2` per flag. This is uniform in `t` because `i` cancels.

Typing audit, each item checked:

* **`c_* != 0` branch.** Required, since the `c_*=0` branch of (4.1) carries
  an extra `1/nu_F` and would give only `3/(2*17)`. The reduced trunk pattern
  has degree `17*3+17*2 = 85 = deg`, so it has **no** `0`-root factor and
  `A != 0`; `c_*^17 = B = (4/3)A != 0`. **Correct branch used.**
* **Direction-orbit typing.** `mult(p_F,c_*) = 2i` is Notation 3.12 at a
  *single* root, and the `mu_17` orbit of `c_*` is **one direction**, not 17.
  The target does not multiply by 17 and is right not to: the tree carrier is
  the point set (Definition 3.3) with `Omega` (Statement 3.2) selecting one
  series per place, so the 17 conjugate coefficient values at the
  characteristic level `pi(F)` (`nu_F = 17`) present one child, not 17
  siblings. Had the target counted the orbit, it would have manufactured a
  spurious `17 * 3/2` and the whole report would be worthless.
* **Cyclic-quotient typing.** Same clause, from the consumer side: the
  Section-9 first-exit repair's parenthetical and Terra's ledger line
  "one orbit is one direction" are consequences of Definitions 3.2–3.3, not
  extra hypotheses. **No hidden assumption is being spent here.**
* **Same-fibre typing.** All places through `F*c_*` are points of
  `Ra_bar \ Ra` for one `a`; Corollary 7.1 fixes one `a`. **Consistent.**
* **Multiplicity typing.** `m = 2i` is the *full* multiplicity
  (`i` x reduced 2) via Proposition 8.1(i)'s `p_F = C Phi^i`; using the
  reduced value `2` would give the absurd gap `17i/2 - 7`. The target uses
  `2i`. **Correct.**

### 3.3 Point 3 — is the sum a legitimate "trunk first-exit charge"?

**Answer: YES, the terminology is exactly the reviewed definition; and the
route contradiction also goes through with the terminology deleted.**

The reviewed Section-9 replacement theorem defines, for the first-separation
partition `E_i` of y-side cv vertices along a characteristic path,

```text
lambda_i^exit := sum_{H in E_i} kappa_H(pi(H)-1),          (4.2)
```

i.e. the charge **is already a set-sum** in the promoted repair. The target's
`E_F(c_*)` is the `c_*`-direction part of `E_trunk`, so
`lambda_trunk^exit >= lambda_F^exit(c_*)`. Nothing is renamed and nothing is
strengthened by fiat. The old criterion's error is precisely that it read a
*per-ray* `Delta` as `lambda_i^exit`.

**Local ownership cannot move these flags to a later vertex.** Ownership in
(4.2) is by *first separation from the characteristic path*, and everything in
the exit subtree above `F*c_*` first leaves the path at the trunk `F` — the
path continues into the mult-3 arrival orbit, so no later path vertex is on
those rays. Internal split vertices of the exit subtree are not on the
characteristic path and never receive an `E_i`.

**Terminology-free route.** Even granting an adversarial ownership
convention, §4 needs only: four **pairwise distinct** elements of `T_{a,cv}`
for one `a`, and `(C7.1*)`. That is a direct application of the actual-weight
Corollary 7.1 and uses no `lambda^exit` vocabulary at all. So the answer to
the prompt's conditional is **yes** — the contradiction survives without the
term.

**Quotient/orbit attachment caveat, tested explicitly.** The caveat in the
global first-exit repair is that conjugate directions must not be counted
twice. I tested it in both directions:

* *Against Case A (over-counting):* harmless. Distinct tree vertices are
  distinct places-level flags by construction, so `(C7.1*)`'s "pairwise
  distinct" is satisfied by distinct elements of `E_F(c_*)`. There is no
  mechanism by which two distinct vertices of `T_{a,cv}` collapse to one
  Corollary 7.1 summand.
* *Against Case B (under-counting):* **fatal**, see §4. The same
  places-not-series structure that protects Case A destroys Case B's
  `N(tau)=2i` step.

### 3.4 Point 4 — the single-flag case

**Answer: the conclusion `>= 3` is right; two of the three sub-answers the
prompt asks about are NO.**

* *Does uniqueness force the entire `2i` group to remain unsplit through the
  cv level?* **NO.** Uniqueness forces all *places* through `F*c_*` to agree
  strictly below `u_0`. It does **not** force the `2i` *series* to. A single
  place with a characteristic exponent in `(pi(F), u_0)` sheds conjugate
  series there — `N` drops — while its ray, and hence its flag, is unchanged.
  Proposition 3.1(*) counts series (its proof counts points of `R^*`, the
  smooth closure of `h(t^kappa,y)=0`); Definition 3.3 counts places. The
  target's sentence "all `2i` series agree strictly below the common cv level"
  silently identifies the two.
* *Does the area identity then force `tau_0 = 17/2`?* **NO** in general; only
  under the extra hypothesis `q = 1`, where it is provable (see the repair).
  In general the single-flag case has `tau_0 >= 17/2` with equality only when
  nothing is shed.
* *Is `kappa_H/kappa_F` a positive integer?* **YES.** `(A4)`, from Notation
  3.5's post-jump `kappa_F = kappa/e_j` (`alpha_j <= u`) and the standard
  `gcd` divisor chain `e_j | e_{j-1}`; `q = E_+/E_0` with `E_0 | E_+ <= m`.
  I re-read Notation 3.5 and confirm the post-jump convention independently:
  `kappa_F` equals the lcm of the denominators of the characteristic levels
  `<= pi(F)`, a function of the ray-prefix, hence a well-defined vertex
  decoration.
* *Does integrality of `3q/2` force `q` even and weight `>= 3`?* The
  implication `3q/2 in N* => 2|q` is valid arithmetic, **but its premise
  `w_H = 3q/2` is exactly the unproved step**, so this is not a proof. The
  correct single-flag argument (§4) reaches `w_H >= 3` without ever computing
  `tau_0`.

### 3.5 Point 5 — the old `tau=8`, `2i -> i` profile

**Answer: it really does create at least two distinct cv flags with total at
least 4; no valid identification or selection can bring its total down to 2.
The target's §3 conclusion here is CORRECT, but only after one missing step.**

The profile lives inside Theorem C, which forces `kappa_H = kappa_F`, i.e.
**`q = 1`**. That is the missing step and it is decisive: `q = 1` means no
characteristic level of the ray lies in `(pi(F), u_0]`, so **the drop at
`tau = 8` cannot be a conjugate shedding** — it must be a divergence of
distinct places. Two distinct places diverging at `theta = 8 < u_0 = 9` give
`I_P(u) != I_Q(u)` for all `u > 8` (Definition 3.3), hence distinct flags.

Exact bookkeeping of the departing group, done independently this lane:
the leaving `i` branches carry `N = 2i` on `(0,8]` and `N = i` afterwards, so
`17i = 16i + i(tau_0' - 8)` gives `tau_0' = 9` and
`w' = q'(9-7) = 2q' >= 2`. The retained group gives `w = 1*(9-7) = 2`.
**Total `>= 4`, not `2`.**

Can an identification collapse them? No. They are distinct vertices of `T_a`,
and `T_{a,cv} subset T_a`, so Corollary 7.1 counts both. Can a *selection*
reduce the total? Corollary 7.1 permits selecting any subset — which only ever
helps the kill, since one is free to select **both**. The freedom runs in the
prover's favour, not the route's.

I also checked the adversarial alternative: if instead the `tau=8` drop were a
conjugate shedding, then `kappa_H > kappa_F`, contradicting Theorem C's
`Delta_trunk = 2`; that configuration has `q >= 2` and single-flag weight
`w = 2(17-8-7) = 4 >= 3` anyway. **Both readings kill `Delta_trunk = 2`.**

### 3.6 Point 6 — distinctness, the exact ceiling, and `t`-uniformity

**Answer: all four flags are pairwise distinct on one fibre; the ceiling is
exactly `td-1 = 7`; and `2+2+3+1 = 8` does exclude the whole affine family
uniformly in `t`. One dependency is load-bearing and worth naming.**

* **The two A-exit witnesses.** Each A-copy has exactly one extra orbit
  (reduced multiplicity 1, arrival is the mult-2 orbit), gap `14/2-5 = 2 > 0`,
  hence `A*c_* in T_a^up` by the same Notation 6.1 test, hence a cv flag with
  `w >= 2` by `(INT)`. `A_1` and `A_2` are the two chain arrivals at the
  equal-join merge `G`, therefore **incomparable** vertices on two different
  branches above `G`; their exit subtrees are disjoint, so `H_1 != H_2`.
* **The trunk witnesses.** They lie in the trunk's extra-orbit subtree, which
  hangs off the trunk in the direction *not* leading to `G`; disjoint from
  everything above `G`, hence from `H_1, H_2`.
* **The x-side unit.** `T_a^*` has two components (Statement 3.3), the x- and
  y-trees; the x-side cv vertex is in the other component, hence distinct from
  all three. Its weight is `>= psi = 1`, and independently `>= 1` from
  `(INT)` + Statement 7.1 alone.
* **One fibre.** All four are in `T_{a,cv}` for the single `a` carrying the
  pole. Corollary 7.1's hypothesis "Set `a in C` and
  `{F_1,...,F_n} subset T_{a,cv}`" is met.
* **The ceiling is exactly `td-1 = 7`.** `(C7.1*)` reads
  `td(f,g) >= 1 + sum_{F in T_{a,cv}} kappa_F(pi(F)-1)`, gated PASS by Terra
  on the amended hash. With `td = 8` the cap on any distinct set is `7`. The
  target uses **only this inequality** and does **not** invoke Proposition
  7.5's identity, printed (22), or the per-puncture `delta_a` — all three of
  which the Section-7 repair explicitly declined to restore. This is a real
  and deliberate improvement over the earlier Theorem-F accounting, which
  routed the final clause through Proposition 7.5's identity.
* **`t`-uniformity.** Every input is `t`-free after cancellation:
  `D_F/m = 17/2` (the `i = 28(4+3t)` cancels), `kbar_F = 7`, `D_A/m_A = 7`,
  `kbar_A = 5`, `psi = 1`, `td = 8`. Verified by exact arithmetic at
  `t in {0,1,2,3,7,20,100,1000}` (§8). **The kill is uniform in `t`.**

**Load-bearing dependency, named because the margin is exactly one.** Drop
the x-side unit and the y-side total is `2+2+3 = 7 <= 7`: **no
contradiction**. The kill therefore rests on the `psi = 1` x-side flag as much
as on the trunk's third unit. `psi = 1` is printed-derivable
(`psi l_f < k_f` at `psi = 1` is Theorem 6.1; H3-psi's
`ceil(M/j)-1 = ceil(5/3)-1 = 1` with `j = M(1-w) = 3` agrees) and was
confirmed in the pinned Fable review, so it stands — but it is not slack, and
any future weakening of the `psi` layer reopens this route. The target's own
alternative phrasing ("after reserving the x-side unit, the y-side budget is
6") is equivalent and equally dependent.

### 3.7 Point 7 — perimeter

**Enforced.** The target's own exclusions (§0 last paragraph, §6 last
paragraph) are accurate and I add nothing to the claim. This review confirms
the death of **one reviewed formal route** and nothing more. Explicitly **not**
established, here or in the target: any global `td=8` exclusion; the exclusion
of any other `td=8` route family; a degree range or ceiling; source landing or
`(0,y)`-side initialization; Keller realizability; any polynomial pair; any
counterexample; JC2. Also not established: that the bound `3` is **attained**
(the target correctly disclaims this, and §4 shows attainment would require the
knife-edge `q=2`, `tau_0=17/2`).

---

## 4. R1 — the defect and its repair

### 4.1 Statement of the defect

Target §3, Case B, second sentence:

> Since separated Puiseux series cannot remerge, all `2i` series agree
> strictly below the common cv level.

and the consequence drawn from it, `N(tau) = 2i` on `(0, tau_0]`, hence
`tau_0 = 17/2` and `w_H = (kappa_H/kappa_F) * 3/2`.

This is **false as an inference**. Three source facts collide:

1. **Definition 3.3** builds `T_a^*` from `(Ra_bar \ Ra) x [0,infty]`, the
   *finite point set* of the smooth compactification — one ray per **place**.
2. **Definition 3.2** defines the contact of two points as the **maximum**
   over corresponding series, and **Statement 3.2** supplies `Omega` selecting
   one series per point realizing those maxima. So conjugate series of one
   place are one ray, never two.
3. **Proposition 3.1(*)** counts *series*: its proof states
   `deg(p_d) = #{P in R^* : x(P) = infty and eta_n(P) in C}` on the
   `kappa`-cover.

Therefore `N` can strictly decrease while `E_F(c_*)` stays a singleton: a place
sheds Galois-conjugate series at each of its own characteristic exponents, and
by Notation 3.5 that is exactly where `kappa_{I(u)}` jumps. Uniqueness of the
flag constrains **place divergence**, not **conjugate shedding**.

### 4.2 The defect is realized inside the target's own dependency set

This is not a hypothetical. The pinned exact-lambda primary's A-step analysis,
confirmed clause-by-clause in the pinned Fable review, contains the
**conjugate regime** `E_+ = 2`: the two series through `A*c_*` are conjugates
of a **single place**, they separate at `theta`, `N` drops `2 -> 1`,
`kappa` jumps, and there is exactly **one** cv flag with
`Delta_A = 2(9-theta)`. Transplanted to the trunk, that is precisely a
single-flag configuration with `N` not constant — the configuration Case B
declares impossible. The target's §6 self-listed review risk 2 ("tree
non-remerging makes `|E_F(c_*)|=1` equivalent to retention of all `2i`
series") is the right thing to have worried about, and it **fails**.

Knock-on: Case A's justifying sentence ("a later split of `B_*` produces
distinct elements of `E_F(c_*)`") is over-broad for the same reason — a
*conjugate* split produces no new element. Case A's hypothesis is `r >= 2` and
its conclusion `>= 2r >= 4` is unaffected, so this is a defect of
justification, not of the case's arithmetic. The §5 replacement text inherits
the same over-broad sentence.

### 4.3 The repair

Replace the arity dichotomy by a **ramification dichotomy**. Everything used
is already pinned: `(A2)`, `(A4)`, `(A5)`/`(INT)`, Notation 3.5, Definitions
3.2–3.3.

> **Lemma R1.** For every `H in E_F(c_*)`, write `q_H := kappa_H/kappa_F in N*`
> and `tau_0(H)`. Then `tau_0(H) >= D_F/m = 17/2` and `w_H = q_H(tau_0(H)-7)`.
>
> **(a)** If `q_H >= 2` for some `H`, then
> `w_H >= 2*(17/2 - 7) = 3`, so `lambda_F^exit(c_*) >= 3`.
>
> **(b)** If `q_H = 1` for some `H`, then `|E_F(c_*)| >= 2` and
> `lambda_F^exit(c_*) >= 4`.
>
> *Proof of (b).* `q_H = 1` means, by Notation 3.5, that no characteristic
> level of the ray lies in `(pi(F), u_0]`; since conjugate series separate
> only at characteristic exponents, **no conjugate shedding occurs at or below
> `u_0`**. Suppose `|E_F(c_*)| = 1`. Then no place through `F*c_*` diverges
> below `u_0` either, so `N == 2i` on `(0, tau_0]`; `(A2)` gives
> `tau_0 = 17/2` and `w_H = 3/2`, contradicting `(INT)`. Hence
> `|E_F(c_*)| >= 2`. A second flag `H'` exists and, being a different vertex,
> is a distinct element of `T_{a,cv}`; `w_H, w_{H'} >= 2` by §3.2 plus
> `(INT)`. Non-conjugacy of `H'` with `H` is automatic here — a conjugate
> split would have needed a characteristic level in `(pi(F), u_0]`, excluded
> by `q_H = 1` — so no orbit identification can merge the two summands. QED

Since `q_H in N*`, (a) and (b) are exhaustive, giving
`lambda_F^exit(c_*) >= 3`. **The theorem is proved, uniformly in `t`.**

Sharper than the target, and worth recording: the corrected extremal analysis
is

```text
lambda_F^exit(c_*) = 3  requires  a single flag with q = 2 and tau_0 = 17/2,
i.e. an unsplit 2i-group whose conjugates separate exactly AT the cv level
(admissible because Proposition 3.1(*) counts series agreeing strictly below).
Every other configuration gives >= 4.
```

The target's Case-B numbers (`tau_0 = 17/2`, `q` even, `w = 3`) turn out to
describe **exactly this extremal configuration** — which is why the report's
conclusion is right despite the invalid general derivation. That is a
coincidence of the extremum, not a proof, and it should not be left standing
as one.

### 4.4 What R1 does and does not change

* `(0.1)` — **unchanged and true**.
* §4's route kill — **unchanged and valid**.
* §3's "one unsplit cv flag: charge `>= 3` (a denominator jump is forced)" —
  **true**, but its stated mechanism must be re-derived as in R1; "a
  denominator jump is forced" is right, "because `3q/2` must be an integer"
  is not the reason.
* §3's "two or more flags: charge `>= 4`" — **true**; justification sentence
  needs "into distinct places" inserted.
* §5's replacement text and §6's risk item 2 — inherit the same edit.
* §2, §4, §6 items 1, 3, 4, 5 — **no change**.

---

## 5. Independent audit of §4 (the route kill)

Reconstructed from scratch, not read off the target:

```text
selected set S = {H_1, H_2} u {trunk flags} u {H_x} subset T_{a,cv}, one fibre a
H_1 in A_1's extra-orbit subtree      w >= 2   (gap 14/2-5 = 2, INT)
H_2 in A_2's extra-orbit subtree      w >= 2   (identical A-copy)
trunk flags, total                    w >= 3   (Lemma R1)
H_x in the x-component                w >= 1   (psi = 1; also INT + St 7.1)
merge G contributes 0                 (St 3.18: both orbits are chain arrivals,
                                       no G*c_* exists; an identity, not a floor)
pairwise distinct                     (incomparable subtrees; St 3.3 for H_x)
(C7.1*)                               sum <= td - 1 = 7
total                                 >= 8 > 7     CONTRADICTION
```

Two structural remarks the target does not make, both favourable:

1. **The two-pole structure is handled correctly by accident of framing.**
   The Section-9 cumulative budget (4.3), `sum_i lambda_i^exit <= td-1-psi`,
   is proved for the characteristic sequence of a **singleton** pole, and this
   family is an *equal-join with two arrivals at `G`*, so the singleton-pole
   regularity lemma is unavailable at the merge. The target's §4 does not use
   (4.3); it applies `(C7.1*)` once to an explicit distinct set, which needs
   only distinctness. **This is the right route and should be kept.** A future
   consumer that "simplifies" §4 back to (4.3) would be reintroducing an
   unavailable hypothesis.
2. **`psi` is load-bearing, margin exactly 1** (§3.6).

I found no omitted charge, no double-counted vertex, and no fibre mismatch.

---

## 6. Adversarial probes that did not break the claim

| probe | result |
|---|---|
| Count the `mu_17` orbit as 17 exit directions (would give a fake `17*3/2`) | **Rejected.** Def 3.2/3.3 + `Omega`: one orbit is one direction. Target does not do this. |
| Collapse Case A's flags by conjugacy under the "one orbit is one direction" rule | **Rejected.** Distinct vertices of `T_a` are distinct `T_{a,cv}` summands; conjugate *series* were already collapsed at the ray level. |
| Use the reduced multiplicity `2` instead of `2i` | Rejected: gives `17i/2 - 7`, contradicts Prop 8.1(i) `p_F = C Phi^i`. |
| Use the `c_* = 0` branch of corrected (24) | Rejected: `A != 0` (no 0-root in an 85 = 51+34 split), `c_*^17 = B != 0`. |
| Put the extra direction on the mult-3 orbit | Rejected: `17/3 - 7 < 0`, and `deg p_G = 3i` pins the mult-3 orbit as the chain arrival. |
| `q >= 3` or multi-drop profiles evading `w >= 3` | Rejected: `w = q(tau_0-7)`, `q >= 2`, `tau_0 >= 17/2` bound it below by 3 with no profile analysis. |
| Route the kill through Prop 7.5's identity / printed (22) | Not needed, and correctly avoided: Section-7 repair did not restore them. |
| Deny `F*c_*` is up, so St 7.3 gives no flag | Rejected on-page: Notation 6.1 test is `D_F/m > kbar_F`, i.e. `17/2 > 7`. |
| Attach trunk exit flags to a later path vertex | Rejected: (4.2) ownership is by first separation; and §4 does not need ownership. |
| Drop the x-side unit | **Succeeds in removing the contradiction** (`7 <= 7`). Recorded as the load-bearing dependency, not as a defect: `psi = 1` is separately derived and reviewed. |

---

## 7. Clause ledger

| clause | verdict |
|---|---|
| Target full/body SHA-256; all nine pinned dependency hashes | **VERIFIED byte-exact** |
| Frozen trunk data `i = 28(4+3t)`, `D_F = 17i`, `m = 2i`, `kbar_F = 7`, `deg p_F = 85i` | **CONFIRMED**, `t`-uniform |
| Corrected St 9.3 gap `17i/(2i) - 7 = 3/2`, `c_* != 0` branch, all typings | **CONFIRMED** |
| `F*c_* in T_a^up`, so St 7.3 applies (target left this implicit) | **CONFIRMED and supplied** |
| Every ray in the group gets a cv flag, forced to its St 3.13 level | **CONFIRMED** |
| Per-flag weight `>= 3/2`, hence `>= 2` by `(INT)` | **CONFIRMED** |
| `q = kappa_H/kappa_F in N*` (Thm A(4), Not 3.5 post-jump convention) | **CONFIRMED** |
| Exit charge is the **sum** over the exit set, not one selected ray | **CONFIRMED** — this is (4.2), and the diagnosis of the old error is correct |
| §3 Case A conclusion `>= 2r >= 4` | **CONFIRMED** |
| §3 Case A justifying sentence ("a later split produces distinct elements") | **REPAIR** — true only for splits into distinct places |
| §3 Case B step "`|E| = 1` implies `N = 2i` on `(0,tau_0]`" | **REFUTED** — series/places conflation; A-step conjugate regime is the counterexample |
| §3 Case B consequences `tau_0 = 17/2`, `w_H = 3q/2`, "`q` even" | **NOT PROVED as stated** (true only at the extremum) |
| §3 Case B conclusion `w_H >= 3` | **CONFIRMED via Lemma R1** |
| Headline `(0.1)` `lambda_F^exit(c_*) >= 3` | **CONFIRMED** |
| Sharper extremal characterization (`= 3` iff `q = 2`, `tau_0 = 17/2`) | **NEW, PROVED here** |
| §3 `tau = 8, 2i -> i` gives `>= 2` distinct flags, total `>= 4` | **CONFIRMED**, after inserting the `q = 1` non-conjugacy step |
| §4 pairwise distinctness of `H_1, H_2`, trunk flags, `H_x`, one fibre | **CONFIRMED** |
| §4 ceiling `td - 1 = 7` from actual-weight `(C7.1*)` | **CONFIRMED**; uses only the promoted inequality |
| §4 `2+2+3+1 = 8 > 7`, uniform in `t` | **CONFIRMED** |
| §4 avoids the singleton-pole-only cumulative budget (4.3) | **CONFIRMED as a strength**; must not be "simplified" back |
| x-side `psi = 1` is load-bearing, margin exactly 1 | **RECORDED** (not a defect) |
| §5 withdrawal of the "survives iff three per-ray charges = 2" criterion | **CONFIRMED** — Theorem F's survival reading must be withdrawn for this family |
| Terminology "trunk first-exit charge" | **NO REPAIR** — it is (4.2) restricted to one direction |
| Perimeter: no global `td=8` kill, no degree range, no counterexample, no JC2 | **ENFORCED and accurate** |

---

## 8. Desk verification

One throwaway `/tmp` heredoc, exact `Fraction` arithmetic, no packet written,
nothing installed:

```text
87 checks, 0 failures, over t in {0,1,2,3,7,20,100,1000}
  i = 28(4+3t);  deg p_trunk = 17*3i + 17*2i = 85i
  trunk gap  D_F/m - kbar = 17/2 - 7 = 3/2                    (t-free)
  up-typing  D_F/m > kbar                                     (Notation 6.1)
  first-microstep positivity  17i - 2i = 15i > 0
  q=1 => tau_0 = 17/2 and weight 3/2 non-integral             (Lemma R1(b))
  q>=2 => 2*(17/2 - 7) = 3
  chain arrival  deg p_G = 336+252t = 3i                      (St 3.9(i))
  A-step gap 14/2 - 5 = 2; A up-typing
  ceiling td-1 = 7;  2+2+3+1 = 8 > 7;  2+2+2+1 = 7 <= 7 (old profile survived)
  x-side removal: 2+2+3 = 7 is NOT > 7                        (margin = 1)
  tau=8 profile: retained tau_0 = 9, w = 2; departing tau_0' = 9, w' >= 2
  q=2 conjugate split at theta: w = 2(10-theta) >= 3 for theta in {1,3/2,4,8,17/2}
  knife edge theta = tau_0 = 17/2 gives exactly w = 3
```

Hash verification used `shasum -a 256`; source extraction used `pdftotext`
with page ranges 10–16, 28–39, 34–40.

---

## 9. Maximum safe consequence and next campaign implication

### 9.1 Maximum safe consequence

> On every member of the reviewed `td=8` equal-join affine family, for every
> integer `t >= 0`: the trunk `(85,35)` extra-direction exit set has total
> actual weight `lambda_F^exit(c_*) >= 3`, with equality only if the `2i`
> group stays unsplit through the cv level and its conjugates separate exactly
> **at** that level (`q = 2`, `tau_0 = 17/2`). Together with `>= 2` at each of
> the two `(21,15)` A-copies, `0` at the merge, `>= 1` at the x-side
> `psi`-flag, pairwise distinctness of the selected flags in `T_{a,cv}` for
> one fibre, and the reviewed actual-weight Corollary 7.1 ceiling
> `td(f,g)-1 = 7`, the selected total is `>= 8 > 7`. **The reviewed `td=8`
> equal-join affine formal route is killed at the actual-weight budget tier,
> uniformly in `t`.**

Nothing beyond that sentence is licensed. In particular this proves **no**
global `td=8` exclusion, **no** statement about any other `td=8` route family,
**no** degree range or ceiling, **no** source landing, **no** counterexample,
and **nothing** about JC2. It also does not claim `3` is attained.

Consumer consequence that must be booked: the previously recorded survival
criterion "the family survives iff all three per-ray charges equal 2"
(Theorem F of the pinned exact-lambda primary, as confirmed at that time) is
**withdrawn for this family**. Its per-vertex floors were per-ray; the exit-set
floor at the trunk is `3`, so the floors sum to `2+2+0+3 = 7 > 6` against the
`(25)` ceiling `td-1-psi = 6`. The pinned Theorems A–E, the A-step menu, the
trunk per-ray criterion (Theorem C), `(INT)`, and the jet
underdetermination (Theorem E) are all **unaffected**.

### 9.2 Next campaign implication

1. **Promote the target after R1 only.** The edit is confined to §3 Case B,
   one sentence of Case A, and the mirrored text in §5/§6. `(0.1)` and §4
   stand as written.
2. **The generic hazard is now named and should be swept.** Every consumer in
   this campaign that reasons "one cv flag, therefore the branch group is
   unsplit" or "the group split, therefore the flags are distinct" is exposed
   to the same series/places conflation. The correct primitive is the
   **ramification dichotomy on `q = kappa_H/kappa_F`**, not the arity of the
   flag set. I recommend a targeted audit of the exit-set consumers that
   quantify over `E_i` rather than over rays.
3. **Do not spend the margin.** The kill has margin exactly `1` and consumes
   the x-side `psi = 1` reserve. Any future revision of the H3-psi layer, or
   any route where `psi = 0`, reopens this family at `2+2+3 = 7 <= 7`.
4. **Keep §4's framing.** The direct one-shot `(C7.1*)` application on an
   explicit distinct set is the only budget route available here, because the
   Section-9 cumulative theorem (4.3) is proved for singleton poles and this
   is a two-pole equal join.
5. **Open, and now sharper.** The remaining trunk question is no longer "is
   `Delta_trunk = 2` realizable" (it is not) but "is the knife-edge
   `q = 2, tau_0 = 17/2` realizable at all". Settling it would decide whether
   `lambda_F^exit(c_*) = 3` or `>= 4`, which matters for neighbouring
   families with slacker budgets even though it does not change this kill.

---

Report-body SHA-256 (all bytes before the separator line above):
`51f3ed7c6c77a10e21f053875a323b633fc7e6499641d0b61ad3518f521de0c5`.
