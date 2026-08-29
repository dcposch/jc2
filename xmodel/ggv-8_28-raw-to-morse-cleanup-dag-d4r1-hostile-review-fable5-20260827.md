# Hostile review: DEP-D3 D4R1 factor-local raw-to-Morse cleanup DAG (W22)

Reviewer: Fable5 (independent hostile)  
Date: 2026-08-27  
Charge: repaired D4R1, factor-local raw-to-Morse cleanup DAG through weight 22,
five-row `U14=c` discriminator, quarantined-D4 additivity.

## Overall verdict

**CONFIRMED on all seven charged items.  No REFUTED item, no GAP/REPAIR item,
no failing node/coefficient/factor.**

`PASS-DEP-D3-D4R1-FACTOR-LOCAL-CLEANUP-DAG-W22` is upheld at exactly the
factor-local scope stated in §Promotion below.  The load-bearing exact
five-row evaluation `U14=c` was rederived by hand and by a fully independent
engine, and the entire 49,964-node generic DAG was independently verified at
random full-support points and under live mutations.

## Charged artifacts (custody verified)

All six charged SHA-256 hashes were recomputed and match:

```text
8b3dd3c29058141a8204153d53943af41d4fa423990ec2906922e4f39c7df283  xmodel/ggv-8_28-raw-to-morse-cleanup-dag-d4r1-sol-20260827.md
6beafdb470ec9c4c88fd8c6e3d2ccaf3b4312c477ddabc4576203f7e9c19c954  cases/.../FREEZE.sha256
325d1ceeb1958e9062b6d8d9825f6dc6da7fa9c9268ea750fac12c6301443fe9  cases/.../PREREGISTRATION.md
de051a0615fa470748be92df0f15abbc8d30fd6b2d526df7d5788b96f6e44fa2  cases/.../README.md
83c107b77af8aa395fa38199af84f37aba44b262e01ac397a554c7f1dfdba0f2  cases/.../RESULT.json
4a2ab0f232bc32e094b98117c8de709bd5abcd20e9071afb528f9320ae64961c  cases/.../compile_cleanup_dag_d4r1.py
```

(`cases/...` = `cases/ggv_8_28_raw_to_morse_cleanup_dag_d4r1_20260827`.)
`FREEZE.sha256` lists exactly these five case/report files with matching
hashes; the case directory contains exactly the five frozen files and nothing
else.  All nine `PINS` in the compiler (D3 freeze/report/raw/result, R2
result/review, quarantined D4 freeze/report, own preregistration) were
recomputed and match.

## Execution disclosure

This session had a shell.  I ran (a) the producer's pinned replay
`compile_cleanup_dag_d4r1.py --check` (PASS, 93.5 s), and (b) a fully
independent verification driver of my own, staged only in `/tmp`
(`/tmp/fable5_d4r1_review.py`, 231 s), which re-implements the entire
computation with different algorithms (Horner composition at `c+s(t)` instead
of Taylor-shift accumulation, direct residual verification instead of
recurrence trust, and a direct `u`-composition path for `W,V,Q,Gamma`) and
evaluates the committed DAG with my own evaluator.  No repository file was
read from `jc2-lean`, and no file was written except this review.  Producer
`PASS` strings were treated as claims, not evidence.

---

## Item 1 — Custody, 400-row support, tags, preregistration, 49,964-node commitment

**Verdict: CONFIRMED.**

Quarantine and additivity:

* The two quarantined D4 pins remain byte-identical:
  `8a79c549...` (`cases/ggv_8_28_raw_to_morse_cleanup_dag_d4_20260827/FREEZE.sha256`)
  and `bf81b905...` (`xmodel/ggv-8_28-raw-to-morse-cleanup-dag-d4-sol-20260827.md`).
  Beyond the charge, I re-verified the *entire* D4 case against its own
  freeze (`shasum -c`: all five entries OK), so nothing inside the quarantine
  moved.
* D4R1 is strictly additive: new case directory, new report, new script name.
  A full diff of the two compilers shows exactly the advertised repair and
  nothing else: rename `u/U` to `u_pre/R_pre` with the explicit annotation
  "(X-dependent before recentering; not the Morse U(t))", the new
  `evaluate_dag` function, the exact five-row DAG evaluation with the hard
  assertion `evaluated_U[14] == cpow(1)`, the two quarantine pins, and
  status-string updates.  The generic DAG construction code is byte-identical
  between D4 and D4R1, consistent with both quoting the same DAG digest.
  (D4's inaccurate "Merkle/digest manifest" wording was also corrected to
  "digest manifest"; there is a single digest, no Merkle tree.)

Exact 400-row support (independently recounted from the pinned D3
`RAW_INPUT.json`, sha `28b9b05c...`):

* `F`: 141 slots = 17 weight-0 + 124 positive-weight; `G`: 301 = 25 + 276.
  Positive-weight total = **400** exactly.  No duplicate slot names, no
  duplicate `(weight, x)` keys.
* Slot naming/weight/chart consistency holds on all 442 slots:
  `f_i_j ↔ x^i y^j ↦ t^w X^i` with `w = 3i − j + 8`, and
  `g_i_j` with `w = 3i − j + 12`; `j ≥ 0` throughout.  This confirms the
  structural impossibility of a raw `F14:X` slot: `(w,i)=(14,1)` forces
  `j = −3`, i.e. the pullback `x*y^-3` — exactly the artifact's claim.
* Maximum positive-weight x-degree is 15 (F) and 23 (G), strictly within the
  compiler's Taylor bounds `max_degree = 16/24`, so `compose_total` drops no
  derivative term (an attack I checked explicitly).
* The rebuilt DAG's `Raw` leaf set equals the 400 positive-weight slot names
  exactly (set equality, my own extraction).
* Positive F weights present are `1..14` and positive G weights `1..21`; in
  particular **no slot exists at weight 22**; "through weight 22" is the
  compiled output range, which the artifacts state correctly.

Tags: the four factor IDs match the D3 `factor_registry`
(`fac_X_minus_1`, `fac_X_plus_1`, `fac_X2_plus_1`, `fac_X4_plus_1`); chart
`X=xi(t)+z`, deck `ORIENTED_PLUS_H`, orientation `u=H mod t`, determinant
`u_X(c,0)=H'(c)=8c^7` are all present and semantically verified below
(item 5, closed fibre).

49,964-node full-encoding commitment: I reconstructed the committed DAG in my
own driver (producer primitives, my own byte/census extraction) and verified

```text
node_count 49964 = Raw 400 + ConstA 1204 + Add 18332 + Mul 30028,
canonical compact encoding 8,400,824 bytes,
sha256 bc3bd04c453eef74d19682b020541f64ca1f42557f2c177692f02485ed1a17d7,
```

and that all twelve output node-ID tables (0..22 each), all 22
`critical_section_equations` known/solution node pairs, and the three-entry
`unit_inversions` log in the frozen `RESULT.json` match the rebuild exactly.
The digest is computed from the constructed DAG, not hard-coded; the frozen
`RESULT.json` is byte-identical to the deterministic rebuild in two
independent processes (producer `--check` and my driver), so serialization is
deterministic (sorted keys, sorted args, canonical JSON).  Node args are
strictly decreasing-free (`args < id`), ops are exactly
`{ConstA, Raw, Add, Mul}`.

Preregistration compliance: verified clause by clause — additive custody;
five rows replayed against literal D3 support before acceptance; acceptance
gated on the exact DAG evaluation `U14=c=(0,1,0,0,0,0,0,0)`; the sparse
identity alone not used as acceptance; generic contract (`F0=H^2`, `G0=H^3`,
400 leaves, `F_X(c+s,t)=0`, coefficients 0..22 of `U,W,V,Q,Gamma`); node-type
restriction; displayed constant-unit inversions only; mandatory tags;
firewall/scope lists.  One nit is recorded as Observation B under item 6
(`delete_supporting_row` is narrative-only in the producer code; my live test
settles what it actually does).

Custody note (non-blocking): both the D4 and D4R1 cases and reports are
currently git-untracked; custody rests entirely on the verified freezes and
pins, which is sufficient, but committing them would harden it.

Descendant firewall spot-check: the only successor artifacts referencing
D4R1 (`d5g` case, D5 gluing design) declare the D4R1 path
`LOCKED_PENDING_FRESH_HOSTILE_REVIEW` / HOLD and do not read its result.  No
premature consumption found.

## Item 2 — Precursor distinction and literal 2S rows

**Verdict: CONFIRMED.**

Hand expansion (independent):

```text
u_pre^2 = H^2 + 2t^6 H X - t^8 H + t^12 X^2 - t^14 X + (1/4)t^16,
u_pre^2 + R_pre = H^2 + 2t^6 H X - t^8 H + t^12 X^2,
```

with the two displayed cancellations `t^14: -X + X = 0` and
`t^16: 1/4 - 1/4 = 0`.  Expanding `H = X^8 - 1` gives exactly the five
nonleading rows, each verified to be a literal D3 `2S` (F-side) slot with the
right weight and x-degree:

| slot | chart row | coeff | in D3? |
|---|---|---:|---|
| `f_1_5`  | `t^6 X`    | `-2` | yes (`x^1 y^5`,  w=6) |
| `f_9_29` | `t^6 X^9`  | `2`  | yes (`x^9 y^29`, w=6) |
| `f_0_0`  | `t^8`      | `1`  | yes (`x^0 y^0`,  w=8) |
| `f_8_24` | `t^8 X^8`  | `-1` | yes (`x^8 y^24`, w=8) |
| `f_2_2`  | `t^12 X^2` | `1`  | yes (`x^2 y^2`,  w=12) |

The weight-14 F slice of D3 is `{f_2_0}` (`X^2` only, as claimed) and the
weight-16 F slice is empty (so the `+1/4` flip really has no landing slot).

Type discipline: every occurrence of `R_pre` in the D4R1 report, the
preregistration, `RESULT.json`, and the compiler carries the X-dependent
precursor typing; nowhere is `R_pre` identified with the scalar `U(t)`.  The
distinction is not merely verbal: the exact evaluation output differs from
`R_pre|_{X=c}` at weights 20 and 22 (`R_pre|_{X=c} = c t^14 - t^16/4` has
nothing there, while `U20 = -c^2/8` and `U22 = c/16` are pure recentering
terms, equal to `s_6` and `s_8`; see item 3).  So D4R1's acceptance criterion
genuinely tests the Morse critical value, not the precursor.  The quarantined
D4 report did commit the charged type error (it printed
`U = t^14 X - (1/4)t^16` and `F = u^2 + U`); D4R1's characterization of that
history is accurate.

## Item 3 — Exact five-row evaluation in `A=Q[c]/(c^8-1)` (load-bearing)

**Verdict: CONFIRMED**, by three mutually independent routes: hand
derivation, my independent engine, and the committed DAG.

Hand derivation (ordinary power series, no divided-power or factorial
convention anywhere).  Under the five-row assignment,
`F = u_pre^2 + R_pre` exactly, so `F_X = 2 u_pre (H' + t^6) + t^14` and the
critical section `X = c + s(t)` satisfies

```text
v := u_pre(c+s,t) = -t^14 / (2(H'(c+s) + t^6)),
U  = F(c+s,t) = v^2 + t^14 (c+s) - (1/4)t^16.
```

Expanding with `1/c^7 = c` and `s = O(t^6)`:

```text
v = -(c/16) t^14 + (c^2/128) t^20 + (7/16) t^14 s + O(t^26),   v^2 = O(t^28),
```

so through `t^22`:

```text
U = c t^14 - (1/4) t^16 + t^14 s(t)   =>   U14 = c, U16 = -1/4, U20 = s6, U22 = s8.
```

The recentering contributions are therefore fully visible at weights 20/22.
The scalar equation `H(c+s) + t^6 s + t^6 c - t^8/2 - v = 0` with
`H(c+s) = 8c^7 s + 28c^6 s^2 + 56c^5 s^3 + O(s^4)` solves order by order to

```text
s6  = -c^2/8      s8  = c/16       s12 = -5c^3/128   s14 = 5c^2/128
s16 = -7c/512     s18 = -c^4/64    s20 = 41c^3/2048  s22 = -7c^2/512
```

(all other coefficients through 22 zero; representative steps: at `t^12`,
`8c^7 s12 + 28c^6 s6^2 + s6 = 0` gives `-5c^3/128`; at `t^20`,
`8c^7 s20 + 28c^6(2 s6 s14 + 2 s8 s12) + 56c^5·3 s6^2 s8 + s14 - v20 = 0`
with `v20 = c^2/128 + (7/16)s6 = -3c^2/64` gives `41c^3/2048`).  Hence

```text
U14 = c,   U16 = -1/4,   U20 = s6 = -(1/8)c^2,   U22 = s8 = (1/16)c,
```

which is exactly the frozen `nonzero_Morse_U_coefficients` and
`nonzero_critical_shift_coefficients` lists, including the `(0,1,0,0,0,0,0,0)`
encoding of `U14=c`.

Machine confirmation: my independent engine (Newton solve, then a **direct
verification that `F_X(c+s,t) ≡ 0` through `t^22`**, then `U = F(c+s,t)` by
Horner composition) reproduces all twelve series, and my own evaluator over
the committed DAG nodes (node 15450 for `U14`, etc.) agrees coefficient by
coefficient with the engine and with the frozen JSON.  `U14=c` is the output
of the critical-section evaluation, not a substitution into `R_pre`.

## Item 4 — Formal coordinates and the finite-étale algebra

**Verdict: CONFIRMED.**

`A = Q[c]/(c^8-1) ≅ Q × Q × Q(i) × Q(zeta_8)` via
`c^8-1 = (c-1)(c+1)(c^2+1)(c^4+1)` — a product of fields, finite étale over
`Q`, matching the four D3 factor IDs.  The complete inversion inventory
(confirmed both structurally and against the `unit_inversions` log; there are
exactly three) with factorwise images:

| inverted element | fac_X_minus_1 | fac_X_plus_1 | fac_X2_plus_1 | fac_X4_plus_1 | inverse in A |
|---|---:|---:|---:|---:|---|
| `F0''(c)=128c^6` | 128 | 128 | −128 | `128 zeta^6` | `c^2/128` |
| `2H'(c)=16c^7`   | 16  | −16 | `−16i` | `16 zeta^7` | `c/16` |
| `H'(c)=8c^7`     | 8   | −8  | `−8i`  | `8 zeta^7`  | `c/8` |

Every image is nonzero on every factor, so all three are exact units of `A`;
I re-verified each inverse by my own linear-algebra `ainv` with the product
assertion.  Formal existence then follows on all four factors
simultaneously: the implicit-function step needs only the unit `F0''(c)`
(`F0'(c) = 2H(c)H'(c) = 0` closes the recurrence, see item 5); the oriented
square root needs `(8c^7)^2 = 64c^6 = A2(0)` and the unit `16c^7`; the series
inverse needs the unit `8c^7`; the inverse coordinate `z(u)` needs the unit
linear coefficient `alpha(0) = c/8`.

No raw-variable localization: structural, not merely asserted.  Every series
constant term (`t^0` coefficient) in the DAG receives contributions only from
the *fixed* weight-0 data `F0=H^2`, `G0=H^3` (positive-weight leaves enter at
`t^{>=1}`), so every inverted leading coefficient is a raw-free `ConstA`; the
compiler additionally hard-asserts `is_const` at each inversion site.  The
DAG grammar (`ConstA/Raw/Add/Mul`) admits no division node at all.  No hidden
global-polynomial automorphism: the object is factor-local formal in `(t,z)`,
nothing glues the four factors, and the artifacts carry
`global_polynomial_automorphism_claim: false` plus the firewall list.

## Item 5 — Independent rederivation of the recurrences through weight 22

**Verdict: CONFIRMED.**

I rederived each recurrence from scratch and verified the implementations:

* **Critical section.** `[t^n] F_X(c+s) = F0''(c) s_n + (terms in s_{<n})`
  because `F0'(c)=0`, weight-`w>0` rows feed `s_n` only at order `w+n`, and
  `k>=2` powers of `s` feed it only at order `> n` (`s_0=0`).  So
  `s_n = -(F0''(c))^{-1} · known_n` is the correct implicit recurrence.  My
  engine closes the loop by directly checking `F_X(c+s,t) ≡ 0 mod t^23` at
  every tested assignment — the recurrence logic is verified, not trusted.
* **Morse square root.** `q0^2 = A2` with `q0(0) = +H'(c) = 8c^7`
  (`ORIENTED_PLUS_H`); recurrence
  `q0_n = (2q0_0)^{-1}(A2_n - sum_{i=1}^{n-1} q0_i q0_{n-i})` rederived; my
  engine verifies `q0^2 = A2` exactly through `t^22`.  Then `q1 = A3·alpha/2`
  and `q2 = (A4 - q1^2)·alpha/2` give the Morse identities
  `2 q0 q1 = A3` and `q1^2 + 2 q0 q2 = A4` (both re-verified exactly), i.e.
  `u = z(q0 + q1 z + q2 z^2)` satisfies `u^2 = A2 z^2 + A3 z^3 + A4 z^4 + O(z^5)`.
* **Inverse coordinate.** Substituting `z = alpha·u + beta·u^2 + gamma·u^3 + O(u^4)`
  into `u(z)` and matching orders gives `alpha = q0^{-1}`,
  `beta = -q1 alpha^3`, `gamma = 2 q1^2 alpha^5 - q2 alpha^4` — my derivation
  reproduces the compiled closed forms, and my engine verifies the defining
  conditions `q0 alpha = 1`, `q0 beta + q1 alpha^2 = 0`,
  `q0 gamma + 2 q1 alpha beta + q2 alpha^3 = 0` exactly.
* **G-side.** `G(xi+z) = g0 + g1 z + g2 z^2 + g3 z^3 + O(z^4)` with
  `g_k = G^{(k)}(xi)/k!` composed with `z(u)` gives
  `W=g0, V=g1 alpha, Q=g1 beta + g2 alpha^2,
  Gamma = g1 gamma + 2 g2 alpha beta + g3 alpha^3` — rederived; moreover my
  engine computes `W,V,Q,Gamma` by a *different route* (direct Horner
  composition `G(X0 + z(u))` in `u`-truncated arithmetic, no `g_k` formulas)
  and agrees with the DAG everywhere tested.
* **Truncation boundaries.** All series are exact through `t^22` with pure
  truncation above (no wraparound); `compose_total`'s Taylor depth 16/24
  covers the actual slot degrees 15/23 (item 1); coefficient extraction
  windows `weight + tdeg <= cutoff` are correct.
* **Aliases.** `critical_shift_s = s`, `coordinate_q0/q1/q2 = (q0,q1,q2)`,
  `inverse_alpha/beta/gamma = (alpha,beta,gamma)` all verified semantically
  against their defining identities; no alias is consumed as anything else.
* **`u^4+` custody.** The `u^0..u^3` coefficients of `G(xi+z(u))` depend only
  on `z(u) mod u^4`, so
  `R_ge4 = G(xi+z(u)) - W - V u - Q u^2 - Gamma u^3` is well defined with
  `ord_u >= 4` given the compiled jet; full formal `z(u)` exists since
  `alpha(0)=c/8` is a unit.  D4R1 claims no coefficientwise expansion and
  correctly attributes the constant-channel irrelevance theorem to R2 (both
  R2 pins verified).
* **Closed-fibre values.** By hand and by engine:
  `s0=U0=W0=V0=Q0=0`, `Gamma0=1` (via `g3(0) alpha(0)^3 = 512c^5 · c^3/512 = c^8 = 1`),
  `q0(0)=8c^7=H'(c)`, `q1(0)=28c^6=H''(c)/2`, `q2(0)=56c^5=H'''(c)/6` — so
  `u ≡ H(c+z) mod t` through the compiled `z`-order, verifying the
  orientation/deck/determinant tags; also `alpha(0)=c/8`,
  `beta(0)=-7c/128`, `gamma(0)=35c/1024`.

## Item 6 — DAG rebuild, commitment attacks, live mutations

**Verdict: CONFIRMED.**

Commitment attacks (all negative): the DAG digest is computed from the
constructed nodes, not hard-coded (the only hard-coded hashes are the nine
external custody pins); `--check` compares a full deterministic rebuild
against the frozen bytes, no self-comparison; serialization is canonical and
was reproduced identically in two independent processes; the evaluation order
is well-founded (`args < id` verified on all 49,964 nodes).

Omitted-term / wrong-node attacks: my independent engine and my own evaluator
over the committed DAG agree on **all 12 output series × 23 coefficients** at
every tested assignment:

* the five-row assignment;
* two random full-support assignments (seed 20260827, integer values in
  `[-3,3]` on all 400 leaves; 349 and 341 nonzero leaves respectively) —
  this exercises the generic DAG, not just the sparse discriminator;
* all four live mutants below.

Live exact mutations (desk-scale, engine and DAG in agreement throughout):

| mutation | result |
|---|---|
| `f_2_0 = +1` (weight-14 `X^2`, **high-weight raw coefficient outside the five rows**; weight 14 is the maximal F weight in the D3 support — no F/G slot exists at weight 22) | `U14 = c + c^2`, `U16 = -1/4`, `U20 = -c^2/8 - c^3/4`, `U22 = c/16 + c^2/8` — each equal to my closed-form hand prediction (envelope argument: `Delta U = t^14 · [(c+s)^2]` contributions), proving the committed DAG is live and exact at that leaf |
| `g_3_0 = +1` (weight-21 G row) | `W21` shifts by exactly `c^3`; `U` and `s` bit-identical to the five-row run (correct F/G separation) |
| `f_1_5 = -3` | `U14 = 15c/16 ≠ c` — the discriminator's `U14=c` assertion fails, as required |
| delete `f_2_2` | sparse precursor identity breaks as claimed, **but `U14 = c` still holds** (see Observation B) |

Observations (none blocking):

* **A.** The producer's in-code mutation checks are weaker than live
  evaluations: two are inequality/absence asserts and
  `delete_supporting_row` is narrative-only (no executable counterpart).
  The prereg's "must fail" is nonetheless satisfied in the meaningful sense —
  each mutation destroys the certificate (identity or slot legality) — and my
  live tests above supply the executable content.
* **B.** The four-row assignment `{f_1_5=-2, f_9_29=2, f_0_0=1, f_8_24=-1}`
  (drop `f_2_2`) **also** evaluates to `U14=c` (both engines agree).  So the
  five-row certificate is not minimal.  This does not contradict any charged
  claim — the promoted statement is existence of a legal synthesis, and a
  smaller one only strengthens the non-obstruction — but the mutation table's
  "delete_supporting_row: REJECTED" must be read as "the displayed precursor
  identity breaks", not as "deletion kills `U14=c`".  Successor work should
  not cite five-row minimality.
* **C.** 27,290 of the 49,964 committed nodes are reachable from the twelve
  output root tables; the remainder are interned intermediates (plus the
  `known_node` chain) that are committed but inert.  Harmless; recorded for
  transparency.

## Item 7 — Scope

**Verdict: CONFIRMED.**  The report, preregistration, README, and
`RESULT.json` firewall are mutually consistent and nowhere exceed the
factor-local scope: `global_E22_compiled: false`,
`global_H_multiple_controlled: false`, no Keller specialization, no global
automorphism, no face/family exclusion, no `G2-PSC`/`G2-BD`, no Keller pair,
no counterexample, no JC2, no cofinality.  D4R1's statement of the remaining
global gap accurately reflects D3 ("the global `H`-multiple can move every
one of the seven coordinates" — D3 report §3).  The single "consequence"
claim — "raw F14 support alone cannot exclude local U14=X" — is exactly what
the confirmed evaluation establishes.

## Promotion (exact wording)

> **CONFIRMED — `PASS-DEP-D3-D4R1-FACTOR-LOCAL-CLEANUP-DAG-W22`.**
> D4R1 is a factor-local formal raw-to-Morse compiler through weight 22 for
> the frozen data `H=X^8-1`, `F0=H^2`, `G0=H^3`, over `A=Q[c]/(c^8-1)`
> projected to the four D3 factors, with deck `ORIENTED_PLUS_H`, orientation
> `u=H mod t`, determinant `H'(c)=8c^7`, the 400 positive-weight D3 raw slots
> as free leaves, outputs `s,U,q0,q1,q2,alpha,beta,gamma,W,V,Q,Gamma`
> coefficients `0..22`, and the `u^4+` part retained only as a typed residual
> of `u`-order `>= 4`; **plus** the exact five-row discriminator: the legal
> D3 assignment `{f_1_5=-2, f_9_29=2, f_0_0=1, f_8_24=-1, f_2_2=1}` evaluates
> under this compiler to `U14=c` exactly (with `U16=-1/4`, `U20=-c^2/8`,
> `U22=c/16`), so raw `F14` support alone cannot exclude local `U14=X` — a
> non-obstruction to any support-only argument.
> It does **not** impose all Keller equations, glue one global polynomial
> `E22`, control the global `H`-multiple, give a global polynomial
> automorphism, exclude an `8_28` face or family, prove `G2-PSC`, `G2-BD`,
> or cofinality, provide a Keller pair or a counterexample, or bear on JC2.
> Five-row minimality is not promoted (Observation B: four rows already
> suffice).  Descendants may now consume D4R1 only at this scope and citing
> this review.

## Verdict summary

| item | verdict |
|---|---|
| 1. Custody / 400-row support / tags / prereg / 49,964-node commitment | CONFIRMED |
| 2. Precursor distinction and literal `2S` rows | CONFIRMED |
| 3. Exact five-row evaluation `U14=c, U16=-1/4, U20=-c^2/8, U22=c/16` | CONFIRMED |
| 4. Formal coordinates / finite-étale inverses on all four factors | CONFIRMED |
| 5. Generic recurrences, truncations, aliases, `u^4+`, closed fibre | CONFIRMED |
| 6. DAG commitment, determinism, live mutations | CONFIRMED |
| 7. Scope and firewall | CONFIRMED |

Smallest failing node/coefficient/factor: **none**.
