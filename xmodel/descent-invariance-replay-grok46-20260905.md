# Replay of OPEN[SECOND-GEN-NUMERICS-DESCENT-INVARIANT] on 1,420 operative rows

Lane `descent-invariance-replay-grok46-20260905`. Drivers:
`box/descent-invariance-20260905/{replay.py,replay.json,replay.out}`.
Receipt basis `11f2b6fa6a1f8754d185a9ad7627841b7834994e`. Exact rationals.
A replay is evidence, not a proof (FALLACY-v2). No ledger edit, no `jc2-lean`.

## 0. Verdict

```text
VERDICT: the invariance identities HOLD on all rows where defined.
  Promotable as a lemma only after a printed derivation is written.
  Defined-fail count on the OPEN quantity: 0.
  Cheap refutation (a row with A'_1 not dividing A_1^{act} at u_s=1, or
  A'_1 not dividing A_1 at u_s>=2): 0 rows.  Empty own-V is not a failure.
```

No new exit-price assertion, so no `charge_basis` line.

Population: 1,420 operative (1)–(13) rows at `Kmin=2`, `16<=n<=200`, from
`box/child-own-v-20260905/enumerated-source-rows.json` (census 24,063).
Live `descend_own`: NONEMPTY 66 (singleton own V; 0 set-valued), EMPTY 1,354
(route states FIRST_SUPPORT 1,051 / WHOLE_SOURCE_TREE 213 / FINITE_POLE 90).
`u_s=1`: 1,110; `u_s>=2`: 310. Identity pass 0.72 s; SD census 16.2 s; total 16.9 s.

## 1. Frozen-input gate

Manifest built with `awk` from the paired `charged_input_<i>_sha256=` /
`_basename=` lines of `xmodel/descent-invariance-replay-grok46-20260905.run.v2`,
then `sha256sum -c` against `/tmp/jc2-lane.YXMnJ7/inputs`: **6/6 OK**.
Workspace copies of the six charged files match the same digests. Banked at
`box/descent-invariance-20260905/artifacts.sha256`.

## 2. What was run

`box/descent-invariance-20260905/replay.py` adapts `controls.py` by changing
only the row source (the 1,420 operative keys) and checking the OPEN identities
with live `descend_own` (exact `Fraction`). Parent `A_1^{moh}` is `Skel.A(1)`
(Moh p.201 (8), lcm of all `den delta_i` for `i>=2`). Parent `A_1^{act}` is the
`OwnVRouteTree` witness bottom `A1` (a zero coefficient adds no denominator).
Child `A'_1 = den(L' delta'_1)` from own metric radii. `N',M'` use the D1
identity `V'_2=V_2` (always determined) and the scaled `(n',d'_2)`. `P'_j,Q'_j`
use own `V'` at overlapping indices. `l''` at a simple point is
`d'_{s'}-3-ell` compared with `d_{s-1}/d_s - d_s`. Child Def 5.1(3) radii at
`u_s=1` (not dropped) replayed against the metric: 46/46 equal.

## 3. Empty-row handling

An empty own-V set is **not a failure**. Set-valued own-V did not occur
(66 singletons, 1,354 empty). On EMPTY rows:

* `N'=N`, `M'=M` remain **defined** (scale of `n,m,d` plus D1 `V'_2=V_2`).
* `l''` is **defined** on licensed `u_s=1` (not dropped); **undefined** on the
  90 FINITE_POLE drops (no licensed descendant; parent level `s-1` is the
  shed `n-1` tail) and on every `u_s>=2` row.
* `A'_1` and `P'_j,Q'_j` are **undefined** (no own radii / no own `V'`).
  Outer vectors of tree-empty rows were not counted as own data.

## 4. Per-identity counts

`pass/fail/undefined`. Fail listed in §5 if any.

| identity | all 1,420 | NONEMPTY 66 | EMPTY 1,354 |
|---|---|---|---|
| `N'=N`, `M'=M` (all `u_s`) | 1420/0/0 | 66/0/0 | 1354/0/0 |
| same, `u_s=1` only | 1110/0/0 | 46/0/0 | 1064/0/0 |
| `A'_1 = A_1^{act}` at `u_s=1` | 46/0/1064 | 46/0/0 | 0/0/1064 |
| `A'_1 \| A_1^{moh}` at `u_s>=2` | 20/0/290 | 20/0/0 | 0/0/290 |
| `P'_j=P_j`, `Q'_j=Q_j` copied-common | 66/0/1354 | 66/0/0 | 0/0/1354 |
| `l''=d_{s-1}/d_s-d_s` licensed `u_s=1` | 1020/0/400 | 46/0/20 | 974/0/380 |

Copied-common = child levels `j=2..s'-1` with `V'_{j+1}=V_{j+1}`
(`j+1 <= first_nonzero`), including 43 `s'=2` rows with no such `j`
(vacuous pass). Licensed `l''` undefined 400 = 310 (`u_s>=2`) + 90 (dropped).

`N'=N`, `M'=M` also holds at `u_s>=2` (310/310), stronger than the OPEN
clause. Child complete-chain radii at `u_s=1`: 46/46 match `(ell+1)·Def 5.1(3)`.

## 5. Named rows that are not OPEN failures

**No OPEN-failing row.** Three typed observations, all listed.

**(a) `A'_1 ∤ A_1^{moh}` at `u_s=1`, but `A'_1 = A_1^{act}` (2 rows).**
The OPEN equality is to the actual stabilizer, not Moh (8). Same two roster
exceptions (R026, R028). Zero-selected parent levels have integral child
radii, so they add no denominator.

| n | m | V | `A'_1` | `A_1^{act}` | `A_1^{moh}` |
|---|---|---|---|---|---|
| 180 | 120 | (2,4,5) | 3 | 3 | 1 |
| 180 | 120 | (3,4,5) | 2 | 2 | 1 |

**(b) `A'_1 = A_1^{act}` fails at `u_s>=2` (10 of 20 NONEMPTY prefixes).**
The OPEN claim at `u_s>=2` is `A'_1 | A_1`, which holds on all 20 (and
`A'_1 | A_1^{act}` on these 10). Equality is not claimed.

| n | m | `u_s` | V | `A'_1` | `A_1^{act}` | `A_1^{moh}` |
|---|---|---|---|---|---|---|
| 99 | 66 | 3 | (8,8) | 1 | 3 | 3 |
| 108 | 72 | 2 | (7,7) | 1 | 2 | 2 |
| 144 | 108 | 2 | (3,7) | 2 | 4 | 4 |
| 165 | 110 | 2 | (3,9) | 1 | 2 | 2 |
| 168 | 112 | 2 | (3,5) | 1 | 2 | 2 |
| 168 | 112 | 3 | (5,5) | 1 | 3 | 3 |
| 180 | 144 | 2 | (5,7) | 2 | 4 | 4 |
| 180 | 135 | 4 | (11,11) | 1 | 4 | 4 |
| 180 | 120 | 3 | (11,9) | 1 | 3 | 3 |
| 200 | 150 | 3 | (7,7) | 1 | 3 | 3 |

**(c) Index-overlap `P'_2 ≠ P_2` on 8 NONEMPTY rows with `first_nonzero=2`,
`s'=3`.** Here `V'_3` is the zero-route image `Wzero[3]`, not copied `V_3`.
The scale identity (`n'-M'_j` and `d'` scale by `u_s/d_s`) still holds on
all 1,420; the P/Q equality needs copied `V_{j+1}`. Copied-common: 66/66
pass. If “every overlapping index” were required, these 8 would fail it.
They are out of the printed derivation’s scope (Sec. 4.2 of the charged
structure report: lower levels where both scale *and* `V'` is copied).

| n | m | `u_s` | V | `P_2,Q_2` | `P'_2,Q'_2` | `V_3→V'_3` |
|---|---|---|---|---|---|---|
| 144 | 96 | 1 | (8,8,3) | 24,16 | 9,6 | 8→3 |
| 162 | 108 | 2 | (8,8,7) | 24,16 | 9,6 | 8→3 |
| 168 | 112 | 1 | (3,21,3) | 42,21 | 14,7 | 21→7 |
| 180 | 120 | 1 | (11,9,3) | 45,9 | 15,3 | 9→3 |
| 180 | 120 | 1 | (2,4,5) | 20,16 | 5,4 | 4→1 |
| 180 | 120 | 1 | (3,4,5) | 20,16 | 5,4 | 4→1 |
| 180 | 120 | 1 | (8,11,3) | 33,22 | 12,8 | 11→4 |
| 192 | 144 | 1 | (3,3,5) | 12,9 | 4,3 | 3→1 |

## 6. SD window emptiness (24,063 census, 16.2 s)

Same parent-side window as `controls.py` (d): `u_s=1`, `s>=3`,
`delta'_{s'}=-1` iff `M_{s-1}=n-d_s(d_s-1)`, `l''=d_{s-1}/d_s-d_s`,
simple-minor iff `d_{s-1}/(n-M_{s-1})>=1`. Cell
`(top=-1) ∧ (l''<0) ∧ (simple-minor)`: **0 of 24,063** (0 of 1,420
operative). Counts match `controls.out` (d) cell-for-cell, including
operative `top=-1, l''=0, simple-minor` = 41.

## 7. FALLACY-v2

Replay types counts; it does not prove the identities. Prime marks are
generation labels, not derivatives. Empty sets were not filled. Prefixes
keep the child terminal index open (no invented `M'_{s'+1}`). `A_1^{act}`
is not Moh (8) `A_1`: the two `u_s=1` rows in §5(a) are the witness.
P/Q “common level” is the copied prefix, not every overlapping index
(§5(c)). Floor/attainment: these are identities of necessary tower
numerics, not realization of a pair. No `sat()`, no flag/place/series
identification, no new exit price.

```text
OPEN[SECOND-GEN-NUMERICS-DESCENT-INVARIANT]  STATUS: HOLD on every row
  where the child quantity is defined (1,420-scale N',M'; 46 us=1 own
  A'_1=A_1^{act}; 20 us>=2 own A'_1|A_1; 66 copied P',Q'; 1,020 licensed
  l''; SD kill window 0/24063).  Still OPEN as a printed lemma.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7285`.
- Body SHA-256:
  `f8e040c3cdd98dea71726f8a290a77f1a245f5292b33eab32cb03e81764cafa6`.
- Frozen basis: `11f2b6fa6a1f8754d185a9ad7627841b7834994e`.
