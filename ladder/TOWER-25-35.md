# TOWER-25-35.md — tower certificate for (25,35,17,5)@mu0=8 (rollout PROBE 3, the kbar=7 outlier)

Status: **PROBE 3 EXECUTED (2026-08-14) — spine complete, rollout row
verified EXACTLY (no wrong-object alarm), tower tier OBSTRUCTED; NEW
RESULT, pending hostile review. kbar = 7 audit: NOTHING in the window
arithmetic used kbar <= 6.**
Engine: `cases/tower_check.py` (five certificates, 1435 checks incl. 21
perturbation controls, exit 0). Certificate: `cases/towers/t25_35.json`.
Baseline: `TOWER-9-15.md`, `TOWER-10-15.md`.

## 1. Spine and rollout match

The only kbar = 7 / X = 5 frame in the book; single DAG; displayed
route = the direct case-IV terminal `(2/5,5,psi=1)` at G with
`lambda = 4 < 5` — the first SLACK displayed route in the series
(saturation flag generalized; L-A carries the residue).

```text
R0 — G (25,35,17)@8, terminal (2/5,5,1), lambda 4 (slack, budget 5)
     +-- X(25,26) nu=25 — P1              (product 25)
     +-- U(40,16,5) — V1(20,16,5) — P2    (direct arrival (5,8))
```

Frames: G `(1/5,7,17;2/5,5)` — `kbar = 7` — U `(1/8,2,5;3/8,8)`,
V1 `(1/4,4,5;3/4,4)` = (C), X `(2,52,25;2,1)`; kappas
`17, 5, 25, 425, 850/75`; `K = 2550`; `(k_f, l_f) = (1250, 750)`.
Rollout row: `kbar=7, X=5`, arrival `(3/8; 4; M8)`, single DAG
`(C) -> (40,16)`, `min deg p_{f,U} = 400`, `i_G = 50`, `P = 25`,
`gapmax = 2/5`, census `3(2)` — **all EXACT against the spine; no
alarm** (and the E5 vertex filter passes here: `n = 5*7 - 17*2 = 1`).

All C1 families close: E5 `(h') (17*2+1)/5 = 7`, `(g') (17*50+400)/5 =
250 = (1/5)*1250`, H5a `kappa_U = 5*17/17 = 5`, (H6)
`8*(7 - 17*(3/8)) = 5`, (H8) `400 = 50*8`, BOOK-2.1 `n = 7, 6`, R1.2
`tau = 4, n = 99`, R2.1-II `n = 25*7 - 52 = 123`, pole identities
`5/850`, `5/75`, derived edge data, terminal `j = 5*(3/5) = 3`,
`R_term = 5/3`, `psi = 1`. T1 rows (checker-derived): G:
`B = (2/5)A, C = -102A^2/35` (new cell); U `(40,16,5)` `(m_j) = (2,2)`:
`sigma = 3A, pi = 3A^2` (the (9,15)-F1 quadratic again),
`C = -15A^3/2`; V1 = (C); X neutral `26C + 25A = 0`.

## 2. The kbar = 7 audit (this probe's purpose)

kbar enters the certificate only through data-driven frame identities,
each verified at kbar = 7: E5 (I4) `(8*17*(3/8) - 2)/7 = 7`; the
chain-1 handshake `X_G = kbar - 2 = 5`; the terminal `j = 3`,
`R = 5/3`. The clash apparatus is kbar-FREE: the window is
`(gap(X), 5/2)` with `gap(X) = (nu_X+1)/(2nu_X)` (P1-anchored, kbar
never appears); the prefix menu is the half-integer grid vs `alpha_1 =
3/2` (type-level); the cap carrier is (C) with `i = 2` (P2-anchored);
chain-2 gaps `2/5, 1/25, 7/250` are `d_q/deg p_f`. The perturbation
control "kbar=7 flattened to 6" raises 10 failures — the frame is
load-bearing where it should be and only there. **No secret
kbar <= 6 dependence exists.**

## 3. The kill

Death gaps: `X: 13/25 > 1/2`; `V1: 2/5, U: 1/25, G: 7/250` — window
empty. Universal three-case exhaustion (divisor classes {5, 25} of the
displayed product instantiated; coverage universal in `nu_X >= 2`);
single-M_U class 8 realized by U (`gcd(40,16) = 8`); menu variant (C)
locked to `first_charged_gaps = [2/5]`; N1–N4 insertion closure at
`(3/2,2)` [caps], `(3/4,4)`, `(3/8,8)` [the neutral-arrival family
`nu = 7 (mod 8)`], chain-1, `(2/5,5)` [terminal side]; the `(6,4)`
insertion example replayed (`i`-chain `2/6/30`, `i_G 50 -> 150`,
product 75); V1→P2 dead-member handoff `mult = 3` exact. Terminal
table: all 3 filed endpoints (direct slack + two eq trunk-1 to
`(2/7,7,1)` and `(2/9,9,1)`), L-A (restated per grok-t10 as the
corollary of R1.3 + St 8.4/P3) carrying the slack residue.
**VERDICT (pending review): all 3 filed routes (2 eq) of
(25,35,17,5)@8 are TOWER-DEAD over their full realization families.**

## 4. Reproduction

```bash
python3 cases/tower_check.py    # 5 certificates, 1435 checks, exit 0
```

Perturbation controls: kbar flattened to 6 (10 failures); slack route
claimed saturated. No git commit. "Untouched" = not machine-checked.
