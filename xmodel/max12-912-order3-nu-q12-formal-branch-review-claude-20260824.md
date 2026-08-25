# Hostile different-model review — max12 `(9,12)` order-three `nu!=0` `Q12` non-parity formal branch

| Field | Value |
|---|---|
| Claim under review | Frozen producer: at every loaded parity point above a root of `Q12`, the seven-row `k=mu=0`, `nu!=0` coefficient fibre carries exactly two reduced smooth formal curve branches — the parity fixed curve `t=0` and a second non-parity branch `Phi(s,t^2)=0` — via block ranks `(2.4)`, the determinant identity `(2.3)`, the gcd ledger `(2.5)`, and an equivariant formal implicit-function normal form `t*Phi(s,t^2)=0` with `Phi(s,0)=unit*det(J_N)`. FREEZE verdict line: `EVERY LOADED Q12 PARITY CONTACT HAS A SECOND SMOOTH FORMAL BRANCH` |
| Overall verdict | **REFUTED** |
| Smallest failing identity | `(2.3)`: `det(J_N)=p^20*(-8388608/243)*v^14*(3v^2+3v+1)^7*Q12(v)/(3v^2-2)^10` on the chart the report names (the genus-five `r2=r4=0` solves). Counterexample `p=1`, `v=1` (`x5=-252`, `x3=-756`, `x1=27720`): genuine `det(J_N)=25275425185572323328`, an integer, while the `(2.3)` right-hand side is `169664962152837939200/243`, whose numerator is not divisible by `3` (hand-verified below) |
| Smallest failing hypothesis | `(2.4)`'s `rank J_N = 3` at loaded `Q12` roots. On the genuine fibre `det(J_N)` is a unit there (`gcd(Q8,Q12)=1`), so `rank J_N = 4`, `Phi(0,0)=unit != 0`, and the claimed second branch `Phi(s,t^2)=0` is the empty germ |
| Root cause | `cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.py:166-170` substitutes `x1 = x5*(v+1) + x5^2*(1/3)/(9v)` (`genus.Rat.constant(Fraction(1, 3))`), while the reviewed genus-five chart requires the polynomial numerator `x1 = x5*p^2*(v+1) + x5^2*(3v+1)/(9v)` (`Rat((Fraction(1), Fraction(3)))` in the confirmed genus-five replay). On the replay slice `r2 = -(4/243)*p*x5^3*(9v+2) != 0`: every determinant, rank, and minor certificate in the package is evaluated off the fibre. This is byte-inherited from the predecessor `Q12` checkpoint, which was already **REFUTED** by its own hostile review |
| Evidence tier | hand-proved involution/character theorem for all eight rows; hand-proved off-fibre identity for the replay slice from the confirmed genus-five theorem (weight argument plus the unique reversible `r2=0` solve); digit-exact hand verification of both sides of the `p=1, v=1` counterexample; cross-attestation of the genuine octic determinant identity by two independent frozen exact computations (the hostile grok refutation of the predecessor, and the producer's own erratum replay with old-pass/new-fail asserts); byte-level audit of every charged and pinned artifact. **Live replay execution and hash recomputation were not possible in this session** — see Execution disclosure |
| Reviewer / model | Claude (Anthropic), Fable 5. Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | frozen parity-normal `Q12` checkpoint (`xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md`), named by the launch prompt and pinned by the charged replay |
| Git HEAD | session-start snapshot `2e6104a` (`Promote max12 DZ20 exclusion and source audits`), matching the full hash `2e6104a417cfe15a93a901aa0a9129094a2ae11b` recorded by the in-tree grok reviews at the same HEAD. All charged artifacts are untracked on top of it |
| Review date | 2026-08-24 (UTC times not captured: the session had no clock or shell access) |
| Python | not executed — static review; reproduction staged, see Execution disclosure |

Producer, case, predecessor, and the named parity/Faber dependencies reread in full before any verdict:

- `xmodel/max12-912-order3-nu-q12-formal-branch-20260824.md`
- `cases/max12_912_order3_nu_q12_formal_branch_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md` and `cases/max12_912_order3_nu_parity_normal_q12_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}` (frozen predecessor and case)
- `xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md` (completed hostile refutation of the predecessor)
- `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md`, `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md` (CONFIRMED), and `cases/max12_912_order3_nu_parity_genus5_20260824/replay.py` (pinned by SHA-256 in the charged replay)
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (pinned parent compiler) and `cases/max12_high_row_probe_20260824/shared_faber_probe.py` (its engine)
- `xmodel/max12-912-order3-nu-parity-normal-q8-erratum-20260824.md`, `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/{QUARANTINE.md,replay.py (controls section)}`, and the header of `xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md` (producer-side corroboration only; not consumed as reviewed truth)

No producer, case, canonical, coordination, prompt, log, run, or other review file was edited. The only repo write is this review file. Reviewer scratch lives in `/tmp`.

---

## Promotion

**Do not accept `EVERY LOADED Q12 PARITY CONTACT HAS A SECOND SMOOTH FORMAL BRANCH`.**

The involution typing of all eight rows, the block decomposition, the existence of loaded algebraic parity points above `Q12` roots, the Euclidean ledger `(2.5)` for the polynomial `Q12`, and the equivariant formal-IFT machinery of §3 all survive. The rank input does not. On the genuine `r2=r4=0` chart the normal determinant is not `(2.3)`; it is (in the notation of the report, established independently twice — see Genuine identity below)

```text
det(J_N) = p^20 * 226492416 * v^16 * (3v^2+3v+1)^8 * Q8(v) / (3v^2-2)^10,
226492416 = 2^23*3^3,
Q8(v) = -999v^8-1539v^7+1782v^6+6498v^5+7320v^4+4428v^3+1548v^2+296v+24,
```

with `Q8` squarefree and `gcd(Q8,Q12)=1`. Hence at **every** loaded `Q12` root the four-by-four normal block `J_N` is invertible, not rank three. The equivariant elimination then leaves `t*Phi(s,t^2)` with `Phi(0,0)=unit*det(J_N)(0) != 0`: `Phi` is a formal unit, the locus `Phi(s,t^2)=0` is the **empty germ**, and the fibre germ is a single reduced smooth branch — the parity curve. Worse for the headline: `J_N` invertibility plus the formal implicit-function theorem forces `a0=a2=a4=a6=0` identically along the germ (see the independent formal-local proof), i.e. loaded `Q12` contact points are **parity-trapped at all orders** — the exact opposite of §4's "generic parity trapping cannot close the leaf" at `Q12`.

The charged conclusion is therefore false at every point it quantifies over. The correct residual locus for the intended two-branch theorem is the octic `Q8`, which is out of scope here and under separate producer/review artifacts.

**Do not promote this to:** any statement at `Q8` (separate packages, separately reviewable); non-parity exhaustion; trapping of the full loaded fibre; Taylor boundaries; all-`(9,12)`; maximum twelve; a counterexample; or JC2.

---

## Provenance failure

The report's §1 says "The exact predecessor isolated the residual parity-normal rank divisor `Q12(v)=0`" and §2 says "the predecessor proved (2.3)". Both are false as provenance:

- The predecessor's own FREEZE says `PRODUCER-EXACT; HOSTILE DIFFERENT-MODEL REVIEW REQUIRED`. That review exists in-tree (`xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md`) and returned **REFUTED**, with `(3.1)` ≡ `(2.3)` failing at `p=1, v=1` on the genuine chart.
- The producer subsequently accepted the refutation: `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/QUARANTINE.md` lists, byte-for-byte, the **charged report, manifest, and freeze hashes of this very package** (`fd4db3e2...`, `3ced4884...`, `aa17408d...`) as "invalid descendant" artifacts that "must not be consumed as mathematical input", and the successor `Q8` formal-branch report calls this package "quarantined".

A package that consumes a refuted, review-gated identity as "proved" fails independently of any new computation. The refutation below is nevertheless established on the mathematics itself.

---

## The wrong-slice mechanism (hand proof, no execution needed)

This section is a complete reviewer-owned proof that the charged replay certifies nothing about the loaded fibre. It consumes only the CONFIRMED genus-five theorem.

The reviewed genus-five chart (report `(3.2)`–`(3.4)`, confirmed by hostile review with independent reconstruction) solves `r2=r4=0` on `p*x5*A != 0`, `v=A/(p x5)`:

```text
x3 = p*x5*(v+2),
x1 = x5*p^2*(v+1) + x5^2*(3v+1)/(9v),                    (G.1)
x5 = -36*p^2*v^2*(3v^2+3v+1)/(3v^2-2).
```

Uniqueness of `(G.1)`: the even tails are weighted-homogeneous with `wt(p,x5,x3,x1)=(2,4,6,8)` and `wt(r2)=14` (verified assertions of the confirmed genus-five replay). Since `wt(x1^2)=16>14`, `r2` is at most linear in `x1`; its `x1`-coefficient is `(4/9)A`, nonzero on the chart (confirmed review, claim 3). Hence `(G.1)` is the unique solution of `r2=0` in the function field.

The charged replay instead substitutes (replay.py lines 166–170)

```text
x1_replay = x5*(v+1) + x5^2*(1/3)/(9v)        [p=1 normalization],
```

i.e. `genus.Rat.constant(Fraction(1, 3))` where the confirmed genus-five replay (its lines 246–250) has the polynomial `Rat((Fraction(1), Fraction(3))) = 1+3v`. These differ as rational functions (they agree only at `v=-2/9`). Because `r2` is linear in `x1` with coefficient `(4/9)A`, `A=p x5 v`:

```text
r2(x1_replay) = (4/9)*A*(x1_replay - x1)
             = (4/9)*(p x5 v)*(-x5^2*(9v+2)/(27v))
             = -(4/243)*p*x5^3*(9v+2)  !=  0.             (W.1)
```

So the slice on which the charged replay computes `(2.3)`, both `(2.4)` unit minors, and both minor gcd certificates satisfies `r2 != 0` (and correspondingly `r4 != 0`): it is **not** the loaded fibre. The frozen replay passing (`replay.json` matching) is regression of an off-fibre identity and is evidence for nothing in §2–§3 of the report. This alone reduces the package to at most GAP; the next section closes it to REFUTED.

---

## Genuine identity and the counterexample

Two independent, mutually adversarial exact computations of `det(J_N)` on the genuine chart `(G.1)` are frozen in-tree:

1. the hostile grok review of the predecessor (independent Gaussian elimination over `Q` and exact `Q(v)` reconstruction, plus twenty-four sample controls), and
2. the producer's own erratum replay `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.py`, which asserts, as executable controls (its lines 185–237): `r2, r4` nonzero on the `1/3` slice; the old `Q12` identity reproduced **on that slice**; the old identity failing on `(G.1)`; the octic identity holding on `(G.1)`; and the exact values below at `p=v=1`.

Both give the identity displayed in Promotion, with `Q8` squarefree, `Q8(0)=24 != 0`, and `gcd(Q8, v) = gcd(Q8, A2) = gcd(Q8, D) = gcd(Q8, A5) = gcd(Q8, Q12) = 1`.

This review adds digit-exact hand verification of the discriminating point `p=1`, `v=1` (`A2(1)=7`, `D(1)=1`):

- Chart values: `x5 = -36*1*7/1 = -252`; `x3 = -252*3 = -756`; `x1 = -252*2 + (-252)^2*(3+1)/9 = -504 + 28224 = 27720`. All three match both frozen computations.
- `Q12(1) = -24559300` (direct signed sum of the thirteen displayed coefficients). Its digit sum is `28`, so `3` does not divide `Q12(1)`; neither `2^23` nor `7^7` contributes a factor `3`, so the `(2.3)` right-hand side at this point, `(-8388608/243)*7^7*Q12(1)`, is a rational with exact denominator `243` — **not an integer**.
- Hand multiplication: `2^23*7^7 = 8388608*823543 = 6908379398144`, and `6908379398144 * 24559300 = 169664962152837939200`. So the `(2.3)` right-hand side equals `169664962152837939200/243` exactly — matching both frozen computations.
- `Q8(1) = 19358` (direct signed sum). Hand multiplication: `226492416 * 5764801 = 1305683706249216` (`7^8 = 5764801`), and `1305683706249216 * 19358 = 25275425185572323328` — exactly the frozen genuine determinant value. The octic identity and the recorded determinant are digit-consistent.

Since `25275425185572323328` is an integer and `169664962152837939200/243` is not, `(2.3)` fails at `p=1, v=1` on the chart the report names. Since `gcd(Q8,Q12)=1` and `v`, `A2`, `D` are units at every `Q12` root (the `(2.5)` ledger, which is slice-independent and true), `det(J_N)` is a **unit at every loaded `Q12` point**: the contact hypothesis of the whole package is empty.

---

## Independent formal-local proof (what is actually true at a loaded `Q12` point)

The launch prompt asks for an independent formal-local proof alongside the replay. The replay could not be executed here (see Execution disclosure); the following is the reviewer's own formal-local analysis. Work over an algebraically closed constant field of characteristic zero.

**(a) Involution typing, proved rather than replayed.** Let `sigma: f(z) |-> -f(-z)`, so `a_i |-> (-1)^{i+1} a_i`: the fixed locus is `a0=a2=a4=a6=0` and `(p,x1,x3,x5)` are invariant via `(2.1)` (`a7=3p, a5=3p^2+x5, a3=p^3+x3, a1=x1`, a biregular triangular change on the invariant subspace). Let `z(w)=w+O(w^{-1})` be the normalized inverse of `f(z)=w^9`, and `F_j(f)` the Faber solution, characterized as the unique monic degree-`j` polynomial with `F_j(f)(z(w)) = w^j + O(w^{-1})`. If `f~ = sigma f` then `-z(-w)` inverts `f~` with the right normalization, so `z~(w) = -z(-w)` by uniqueness; and `F_j(f)(-z)` is monic of degree `j` (as `j` is even here) with `F_j(f)(-z~(w)) = F_j(f)(z(-w)) = (-w)^j + O(w^{-1})`, so `F_12(f~)(z) = F_12(f)(-z)` and likewise `F_6`, with `k` invariant. Hence

```text
r_l(sigma a) = -[w^{-l}] g(z(-w)) = (-1)^l r_l(a).
```

Every monomial of `r_l` therefore has `a_even`-degree `≡ l (mod 2)`. Corollaries, with no further computation: the odd rows `r1,r3,r5,r7` vanish identically on parity; `d(r_odd)/d(invariant)` and `d(r_even)/d(a_even)` vanish on parity; the Jacobian of the seven equations `r1,...,r5,r6-nu,r7` (`r6-nu` has the differentials of `r6`) is block diagonal `J_N ⊕ J_I` exactly as in `(2.2)`. Item 1 of the charge is **confirmed**; the replay's monomial-parity check is a faithful mechanization of a true theorem.

**(b) Base points exist.** `Q12` is squarefree and coprime to `v`, `A2`, `D`, `A5` (true, slice-independent ledger), so at any root `v0`, `R6(v0) = -2304 v0^6 A2^3 A5 / D^4` is a nonzero constant and `p0^9 R6(v0) = nu` has nine nonzero solutions over the algebraic closure; the chart conditions `p0*x5*A != 0`, `D(v0) != 0`, `9v0 != 0` all hold. The genus-five theorem excludes actual Keller **trajectories** on parity, not algebraic coefficient **points**; the attack "the parity theorem leaves no legitimate base point" does not land. Item 3 is **confirmed** — but the points are ordinary.

**(c) What happens at those points.** On the genuine chart `det(J_N)(v0) != 0` (Genuine identity section). The four anti-invariant equations `r1=r3=r5=r7=0` have, at the base point, an invertible `4x4` Jacobian in the four anti-invariant variables. By the formal implicit-function theorem in the completed local ring, there is a **unique** 4-tuple of formal series in the invariant coordinates solving those four equations through the point; `a0=a2=a4=a6=0` is such a solution (the odd rows vanish identically on parity, by (a)); therefore the germ of the seven-equation fibre satisfies `a0=a2=a4=a6=0` **identically**. Every formal branch through a loaded `Q12` point lies inside parity: there is **no non-parity formal branch**, reduced or otherwise, and the point is parity-trapped at all orders. If additionally `rank J_I = 3` there (not certified on-fibre by anyone — the charged certificate is off-slice — and not needed for this refutation), the germ is exactly the smooth parity curve: one branch, tangent dimension one, full Jacobian rank seven — against the report's "rank six / tangent dimension two".

**(d) Audit of the equivariant machinery (items 4–6 of the charge).** The abstract skeleton of §3 is correct formal algebra, and would apply verbatim at a genuine simple rank-drop point. Specifically, granting `rank J_N = 3` with unit minor on `(r3,r5,r7)x(a2,a4,a6)`, `rank J_I = 3` with unit minor on `(r2,r4,r6)x(x1,x3,x5)`, squarefreeness of the residual, and `gcd(residual, num R6') = 1`:

- *No omitted equation.* The seven equations split `3+3+1`: six pivots with invertible block Jacobian generate, by the formal IFT, the same ideal as `(a_j - alpha_j(s,t))_{j=2,4,6} + (x_k - xi_k(s,t))_{k=1,3,5}`; the quotient presents the germ as `k[[s,t]]/(rho)` with `rho` the reduced `r1`. Exactly one residual equation, as claimed.
- *Equivariance and parity of the residual.* `sigma` fixes the six-pivot system setwise (three anti-invariant equations, three invariant ones), acts as `(s,t) -> (s,-t)` on the retained coordinates, and uniqueness of the IFT solution forces `alpha` odd and `xi` even in `t`; anti-invariance of `r1` then gives `rho(s,-t) = -rho(s,t)`, i.e. `rho = t*Phi(s,t^2)` exactly — no extra unit is dropped and no nilpotent appears; `t` divides `rho` exactly once because `Phi(s,0)` is not the zero series (next point). Item 4's mechanism is **confirmed**.
- *Schur complement.* Along `t=0`, differentiating the three anti-invariant pivots in `t` and eliminating gives `Phi(s,0) = d(r1)/da0 - row*(N33)^{-1}*col = det(J_N)/det(N33)` evaluated along the loaded fixed curve — `(3.2)` is a correct identity whenever `det(N33)` is a unit. Item 5's identity is **confirmed as machinery**.
- *Transversality.* With the invariant unit minor, `s=p-p0` is a legitimate retained coordinate and `v(s)` is a formal series along the curve; differentiating `p(s)^9 R6(v(s)) = nu` gives `9p^8 R6 + p^9 R6' v' = 0`, so `R6'(v0) != 0` and `v'(0) = -9R6/(p0 R6') != 0` are forced (the `gcd(Q12, num R6')` check is indeed a redundant control, as the report says). Then `d/ds[det J_N |curve](0) = unit * residual'(v0) * v'(0)`, nonzero for a squarefree residual — this is exactly "a simple zero along the fixed loaded curve rather than merely in ambient `v`". Correct machinery.
- *Second IFT and branch geometry.* Given `Phi(0,0)=0`, `dPhi/ds(0,0) != 0`: `Phi(s,u)=0` solves uniquely as `s=psi(u)`, so `k[[s,t]]/(t*Phi(s,t^2))` is reduced with exactly two minimal primes `(t)` and `(s-psi(t^2))`, both smooth, with distinct tangents `ds` and `dt`. Item 6's implication is **confirmed as machinery**.

The package fails not in this machinery but in its rank input: at `Q12` roots `Phi(0,0) = unit*det(J_N)(0)` is a **unit**, so `Phi=0` is empty and (c) applies. The two-branch geometry belongs, if anywhere, to the octic locus — a different, uncharged theorem.

**(e) Scope (item 7).** The package's negative list (no algebraic/rational Keller trajectory, no Taylor pair, no terminal `r8`, no counterexample, no JC2) is observed in report, README, REGISTRATION, FREEZE, and payload; the formal branch is not overpromoted to a global or algebraic object. What fails is the positive registered content itself, plus the provenance line examined above.

---

## Headline and subclaim table (launch-prompt items)

| # | Charged item | Verdict | Basis |
|---|---|---|---|
| 1 | Seven-row/eight-variable fibre; involution block decomposition | **CONFIRMED** | hand proof (a); `7 = (r1,r3,r5,r7) + (r2,r4,r6-nu)`, `8 = (a0,a2,a4,a6) + (p,x1,x3,x5)`; biregular `(2.1)` |
| 2 | Rank-three normal and invariant minors at every `Q12` root, with chart units and the loaded equation | **REFUTED** | `(2.3)` is false on the genuine chart (counterexample `p=1,v=1`, hand-verified); `det(J_N)` is a unit at every loaded `Q12` root, so `rank J_N = 4`, not `3`; all four charged certificates were evaluated on the off-fibre slice `(W.1)`; the on-fibre invariant-minor unit claim is unsupported as charged (and unneeded for the refutation) |
| 3 | Existence of charged algebraic parity points; `gcd(Q12,Q12')=gcd(Q12,num(R6'))=1` | **CONFIRMED** (and non-rescuing) | proof (b); the gcd ledger is a slice-independent statement about fixed polynomials, verified independently in the predecessor's hostile review; the points are ordinary rank-`4+3` points |
| 4 | Six-variable formal elimination; exactly one odd equation `t*Phi(s,t^2)=0` | **CONFIRMED as machinery**, inapplicable as instantiated | proof (d); no omitted equation; equivariance/uniqueness argument is sound |
| 5 | Schur identity `Phi(s,0)=unit*det(J_N)`; simple zero along the fixed loaded curve | Identity **CONFIRMED**; premise **REFUTED** | `Phi(0,0)=unit != 0` at `Q12` roots: `det(J_N)|curve` has no zero over `Q12` at all; its zeros lie over the octic |
| 6 | Two reduced smooth distinct branches | **REFUTED** at every charged point | proof (c): the germ is a single branch inside parity; the "second component" is the empty germ |
| 7 | Strict scope (completed high-row coefficient fibre only) | **CONFIRMED** as hygiene; registered positive verdict **REFUTED**; provenance line false | §4/FREEZE verdict falls with items 2, 5, 6; "the predecessor proved (2.3)" contradicts the in-tree refutation and the producer's own quarantine |

---

## Attacks that land

- **Wrong `x1` in the consumed chart.** `Rat.constant(Fraction(1,3))` versus the genus-five `Rat((Fraction(1), Fraction(3)))` (= `1+3v`). Hand-derived consequence `(W.1)`: the certificate slice has `r2 = -(4/243) p x5^3 (9v+2) != 0`. Byte-identical to the substitution refuted in the predecessor's hostile review, inherited into lines 166–170 of the charged replay.
- **`Q12` is not a factor of the genuine `det(J_N)`.** Twice-frozen exact computations plus this review's digit-exact hand checks at `v=1`; `gcd(Q8,Q12)=1`. Every loaded `Q12` point is a rank-four point; the contact hypothesis quantifies over an empty set of rank-three points.
- **The conclusion inverts.** At loaded `Q12` points, `J_N` invertibility forces `a_even ≡ 0` along the germ (proof (c)): parity trapping at all orders, so "`generic parity trapping cannot close the leaf`" is exactly wrong at the charged locus.
- **Passing replay is not evidence.** The frozen replay proves rational-function identities on its own slice; the slice is off-fibre, so `replay.json` regression has no bearing on §2–§3.

## Attacks that do not land

- **"The parity theorem means there is no legitimate algebraic base point."** No: the genus-five theorem empties actual trajectories, not coefficient points; loaded algebraic points above `Q12` roots exist (proof (b)) — they are just ordinary.
- **"An eliminated equation was omitted."** No: `3+3+1=7` accounts for all seven equations; the elimination generates the full ideal (proof (d)).
- **"The odd equation has an extra unit or nilpotent factor."** No, as machinery: `rho = t*Phi(s,t^2)` exactly, with `t` exactly once; the germ ring `k[[s,t]]/(t*Phi)` is reduced whenever the intended hypotheses hold. (At `Q12` the actual failure is `Phi` being a unit, not a hidden factor.)
- **"`s` is not a local coordinate."** As machinery the invariant unit minor legitimizes `s`, and `R6'(v0) != 0` is forced (proof (d)). The charged on-fibre certificate for that minor is off-slice, but nothing in the refutation needs it.
- **"A formal branch was overpromoted to an algebraic/global component."** The scope prose correctly disclaims this; the failure is elsewhere.

---

## Hashes and replay

**Execution disclosure.** This review session had no shell: no Bash tool exists in the environment, the only shell-capable tool (Monitor) was permission-denied ("don't ask mode"), and spawned subagents inherit the same restriction. Consequently the reviewer could not run `shasum -a 256 -c`, could not execute the three frozen replays, and could not execute its own staged verification script. No hash below was recomputed in-session; no replay was run in-session; nothing is asserted as run output. The refutation above deliberately rests only on (i) hand-proved algebra from the CONFIRMED genus-five theorem, (ii) byte-level reading of the frozen sources, and (iii) two mutually adversarial frozen exact computations whose discriminating values were re-verified by hand to the last digit.

Byte-level cross-references of the charged hashes (read, not recomputed):

| Value | Appears in |
|---|---|
| report `fd4db3e2125a11c05dac3c9613b8f4305942150d0e92a3200259e595c2afce62` | launch prompt; `MANIFEST.sha256` line 1; `FREEZE.txt`; `QUARANTINE.md` ("invalid descendant") |
| manifest `3ced488452275f29a4645efb098c87a987e54eb3df85b9f5646da8da8bdbe099` | launch prompt; `FREEZE.txt` (`manifest_sha256`); `QUARANTINE.md` ("invalid descendant manifest") |
| freeze `aa17408d0f860158fdd55577315299f9d9298599f8c7d37c72cb306fbb29b83c` | launch prompt; `QUARANTINE.md` ("invalid descendant freeze") |

Pins inside the charged `replay.py` match the on-disk dependency chain as read: parent compiler `a4fdac5d...`, genus-five replay `c965bb66...`, predecessor replay `bff291fc...`, predecessor report `96163967...`; the same values appear in the predecessor's `MANIFEST.sha256`/`FREEZE.txt` and in the completed grok reviews' recomputed-hash tables at the same git HEAD.

**Reproduction (one command each, in a shell-enabled session).** The reviewer's independent verifier is staged at `/tmp/q12fb_independent.py` (stdlib-only; residue-identity reconstruction of all eight rows and all `d r_l/d a_j` on both slices at 130 exact points; exact interpolation of `det(J_N)*D^10` and both `3x3` minors; factor peeling; full gcd ledgers; Faber high-coefficient self-checks; and a terminal cross-check of every row and Jacobian entry against the hash-pinned compiler at `v=1`):

```sh
python3 /tmp/q12fb_independent.py            # expects exactly one failing check:
                                             #   identity_2_3_true_on_genuine_chart
shasum -a 256 -c cases/max12_912_order3_nu_q12_formal_branch_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.json -
```

A passing frozen replay would not rehabilitate the package: by `(W.1)` its slice is off-fibre, so its identities are true and irrelevant.

---

## Non-blocking remarks

- The charged replay's `evaluate_rat` performs the `p=1` normalization without the predecessor's monomial weight assertion. Harmless: homogeneity of the tails (`wt(a_i)=9-i`, `wt(k)=6`, `wt(r_l)=12+l`) follows from the scaling `z -> λz`, `w -> λw` and is asserted in the confirmed genus-five replay for the even rows and in the predecessor replay for `det(J_N)`.
- The involution-character check, tail supports, and tail SHA-256 fingerprints in the charged replay are slice-independent and stand (item 1).
- `replay.json` fields `full_jacobian_rank: 6`, `full_tangent_dimension: 2`, `normal_rank: 3` are false on the genuine fibre at `Q12` roots (rank 7, dimension 1, rank 4).
- The two slices intersect only over `v=-2/9`; nothing special happens there.
- Corrected sibling packages exist in-tree (`Q8` erratum with `QUARANTINE.md`; `Q8` formal branch using the genuine `1+3v` chart) with their own pending hostile reviews. They are cited here only as producer-side corroboration (statements against interest), not as reviewed truth, and this review certifies nothing about them.
- The smallest valid successor is exactly what the producer already registered: re-prove the two-branch theorem at the octic residual with on-fibre certificates (`rank J_N = 3` with unit minor at `Q8` roots, on-fibre invariant minor, `gcd(Q8,Q8')=gcd(Q8,num(R6'))=1`, loadedness `gcd(Q8, v A2 D A5)=1`), under its own hostile review.

---

## What this does not license

This review does not license: any `Q8`-locus theorem (unreviewed here); trapping or non-trapping statements anywhere except the all-orders parity trapping proved at loaded `Q12` points on the generic chart; parity exhaustion of the loaded fibre; exclusion or construction of non-parity components elsewhere; Taylor boundaries; all-`(9,12)`; maximum twelve; a counterexample; or JC2.

---

**Verdict.** `REFUTED`

Smallest failing identity: report `(2.3)` — `det(J_N) = p^20*(-8388608/243)*v^14*(3v^2+3v+1)^7*Q12(v)/(3v^2-2)^10` on the chart cut by the genus-five solves `(G.1)`. Counterexample `p=1`, `v=1` (`x5=-252`, `x3=-756`, `x1=27720`): the genuine determinant is the integer `25275425185572323328 = 226492416 * 7^8 * 19358` (hand-verified digit-exact), while the `(2.3)` right-hand side is `169664962152837939200/243 = 2^23*7^7*24559300/243`, a non-integer since `3` does not divide `24559300`. Root cause: `replay.py` line 168 substitutes the constant numerator `1/3` for the genus-five polynomial `1+3v` in `x1`, so `r2 = -(4/243)*p*x5^3*(9v+2) != 0` on the certified slice. Smallest failing hypothesis downstream: `(2.4)`'s `rank J_N = 3` at loaded `Q12` roots — the genuine rank is `4`, hence `Phi(0,0)` is a unit, the second branch `Phi(s,t^2)=0` is the empty germ, and every loaded `Q12` contact point is parity-trapped at all orders rather than carrying a second smooth non-parity formal branch.
