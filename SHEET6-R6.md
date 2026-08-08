# SHEET6-R6 — deeper-tower window of the sheet-6 two-pole template (m_{G_m} = 2)

Status: PENDING (skeleton). Mission: close or characterize the survivors of the
R6 window. Level-0 kills already banked in SHEET6-TEMPLATE.md §3 R6:
(k1,l1)=(1,3) dead (level contradiction), l1 > 3k1 dead (h2-count at pole edges).

## 0. Window sanity check (bounds 4/3 < l1/k1 < 3, integrality 6·l1/k1 ∈ N)

PENDING

## 1. Per-case ledgers (Q-ladder with m_{G_m}=2, then E3/E4/E5/E6/N1 analogues)

### 1.1 Case (k1,l1) = (2,3) — PENDING
### 1.2 Case (k1,l1) = (2,5) — PENDING
### 1.3 Case (k1,l1) = (3,5) — PENDING
### 1.4 Case (k1,l1) = (3,7) — PENDING
### 1.5 Case (k1,l1) = (3,8) — PENDING
### 1.6 Case (k1,l1) = (6,11) — PENDING
### 1.7 Case (k1,l1) = (6,13) — PENDING
### 1.8 Case (k1,l1) = (6,17) — PENDING

## 2. Summary table

| (k1,l1) | l1/k1 | 6·l1/k1 | in window? | verdict | killing test / genome |
|---------|-------|---------|------------|---------|-----------------------|
| (2,3)   | 3/2   | 9       | PENDING    | PENDING |                       |
| (2,5)   | 5/2   | 15      | PENDING    | PENDING |                       |
| (3,5)   | 5/3   | 10      | PENDING    | PENDING |                       |
| (3,7)   | 7/3   | 14      | PENDING    | PENDING |                       |
| (3,8)   | 8/3   | 16      | PENDING    | PENDING |                       |
| (6,11)  | 11/6  | 11      | PENDING    | PENDING |                       |
| (6,13)  | 13/6  | 13      | PENDING    | PENDING |                       |
| (6,17)  | 17/6  | 17      | PENDING    | PENDING |                       |

## 3. Consequence

PENDING

## Layer-1 ledger (parent session, cases/r6_window.py — mechanical arithmetic)

All 8 window cases pass ladder integrality (deg p_h1 integral at R/F_s/G_m).
Discriminating layer-1 data:
- (2,3), (2,5): M*_Fs = 63, i_Fs = 2 — the SAME geometry E2 killed at m=1
  (16 <= 7 count contradiction shape). Layer-2 check expected fatal, but the
  m>=3 pattern form at F_s must be computed before claiming the kill.
- (3,5),(3,7),(3,8),(6,11),(6,13),(6,17): M*_Fs = 21, i_Fs = 6 (level-0
  geometry); binding test = suffix-edge St 8.3(ii) EQUALITY
  deg p_h1@Gm in {20,28,32,22,26,34} == mult(p_h1@Fs, c_m), plus the
  E4-analogue collapse at the NEW dead level (h3 top at G_m) and the
  E5-analogue pole-edge drops with the m=2 patterns.

LAYER 2 (pending, needs Prop 8.1(ii)/4.2 m=2 pattern forms from the thesis):
per case, compute p_h1/p_h2 patterns at F_s (m>=3) and G_m (m=2) — the
b-orbit relocation — then run the four count/collapse tests. Expected per
TEMPLATE sec 3: close or reproduce an isomorphic genome.

Status: LAYER 1 BANKED; layer 2 queued (agent retry in the morning — four
subagent stalls tonight were infra-level, probe agents fine, workers dying).
