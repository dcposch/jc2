# split-window-gate-20260905 — lane notes

Report: `xmodel/split-window-gate-opus5-20260905.md`
(body 22920 B, sha256 `72ea6d61…cce226`, basis `847c4cfa…`)

## Verdicts
(1) window + `Q<=u_s`           CONFIRMED
(2) `(G)` Galois covariance     CONFIRMED
(3) `(L)` + `W`-repair          CONFIRMED-WITH-FIX  (18 slots / 17 rows, not 29 / 28)
(4) 3 random rows by hand       CONFIRMED

## The fix
`run_census.py:58-61` defines `negative_k_guard_kills_after_G` as
"G-passing, killed by L alone, k<0" = **guard firings** = 29 slots / 28 rows.
The charged report narrates that number as "otherwise missed leaves", i.e. as
**verdict changes** against the W-independent 17(iiiiii) screen. Those differ:
when some `k*lam_i` is non-integral the root is forced high under BOTH variants
and the slot dies either way. Verdict changes = 18 slots / 17 rows (`wsens.json`).
The W-independent screen can only UNDER-kill (superset of low options); on all
six `(99,66)` `u_s>=2` rows both variants give identical survivor lists.

## Instrument worth reusing
Xu §8 eq. (8.2) is an exact solution of the split-face ODE `(F)` at
`(u,v,W,rho)=(3,8,1,2)`: `p=pi^2(pi+3a)`, `q=pi(pi+3a)^2(pi-2a)`.
It realises LOW `nu=k*lam=1` at the double root and HIGH `nu=W*lam+1=2` at the
simple root — a ready positive control, with three negative controls that fail.
Xu §8 also fixes `W=(-mu_s-2)/d_s` literally (`deg q = 13*3+1`,
`T_3(sigma) ~ t^{13(-8+3delta)-1+delta}`), settling the Cor 7.5 display slip.

## Crosswalk (310 operative `u_s>=2` rows)
233 no G+L survivor -> D2 forced (142 by empty raw window; 6 already U-NEG dead)
 77 retain 113 typed ES leaves, 23 shapes, 25 degree pairs, 56 profiles
1110 operative `u_s=1` rows: NOSPLIT — `genuine(1)` is empty, so the 174 live
ones are untouched.
Corrected residual: 174 (u_s=1 live) + 227 (live D2-forced) + 77 (ES leaves) = 478.

## Files
gate_screen.py       independent screen; brute-force (L), orbit-built (G)
crosswalk-310.json   per-row ES leaves for the 310 operative u_s>=2 rows
wsens.json           the 17 rows / 18 slots whose verdict the W-repair changes
my-census.json       independent 6209-row replay (0 mismatches vs frozen run)
