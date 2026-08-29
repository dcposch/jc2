# M2 case-III two-pole E5 merge-local index — R3 repair packet

Primary repair (Fable 5, 2026-08-29) of
`cases/m2_caseiii_two_pole_e5_local_index_r2_20260829/` after the Opus 5
hostile review
(`xmodel/m2-caseiii-two-pole-e5-local-index-r2-hostile-review-opus5-20260829.md`,
verdict REPAIR_REQUIRED, body `c12bbca2…7b4c`).  **R1 and R2 are
byte-untouched.**  The review confirmed the entire theorem layer (Lemma
A, Theorem B, Theorem C, both equality laws, the 12-of-17 attainment,
the no-incoming-bound proposition, the corrected Opus adjudication);
this packet repairs its two blockers and the majors/nits:

* **Theorem D (new; replaces the FALSE R2 §7.4).** The pattern-cell
  fibre over a fixed `(kbar, nu_G)` menu entry is **always finite**:
  with `r = dq/D = kbar/(mu*w)` and `u = mu - 1/r > 0`,
  `s*(1 + u - ceil(u)) <= (1+nu)/(r*nu) + delta/nu`, each member pinned
  by its `s`.  The §7.4 fibre is exactly `{(20,10), (26,13)}`; R2's
  `(38,19)`, `(62,31)`, `(134,67)` and the inline `s=45` member are
  NE-illegal and deleted everywhere (every candidate pattern
  machine-refuted; canonical `cell_check` cross-check imported
  read-only).  Census: the review's box figures replay **exactly**
  (92,772 fibres, histogram `{1:92083, 2:486, 3:136, 4:63, 5:4}`, 0
  bound violations); a **cap-free complete census** of all 90,957
  `mu>=2` fibres gives max size **12** and the bound **attained with
  equality** at `(7,15,13,170/1019)`, member `s = 1202`.  (The review's
  capped 57,960/9/27 deep-search figures did **not** replicate and are
  not incorporated.)
* **Lemma T1′ (replaces the false `{3,4}` migration gate).** At the
  `mu = 1` pinned solve: `dp | dq  <=>  M = dp  <=>  w/(kbar-w) in
  Z>=1`; for integer `w`, `kbar`: `kbar in {w + d : d | w}` (`w=2`
  recovers `{3,4}`; `w=1 -> {2}`, `w=3 -> {4,6}`).  `e5_solve_mu1` is
  now **total** on every legal `w` (the R2 version raised ValueError on
  `w = 1, 3`); the verdict is the direct `dq % dp == 0` with the closed
  form enforced as a theorem gate.
* **Theorems E & F (new; the §7.1 disclosure).** All six r0=2
  countercells are `D = 1, M = 1`: **MP2-dead as interior merges**, and
  they attain the new arity-graded bound
  `dq/D <= (r0+1) + ((r0+1)*delta+1)/M` with equality.  Theorem F: at
  `r0 in {2,3}` **every** two-pole-constant violator has `M = 1`
  (proved, census-confirmed: 96 + 248 violators, all M=1); false at
  `r0 = 4` (`(44,46)`, `M = 2`, `dq/D = 23 > 17`, graded equality) —
  outside the campaign range `r0 <= 3` (MP1 `r(G) <= m`, engine
  `m <= td//3 <= 4` at `TDMAX = 14`).
* Corrected glosses: `nu_U = 13` is **not** arrival-legal at
  `(2/5, M5)` (neutral is 4 mod 5; direct `{2,7,12}`), so the mixed pin
  **kills** `(18,27,13,9)@5`; the `(4m-2, 6m-3)` family covers the 12
  alive rows at odd `m = 3..25` only (even `m = 4..10` are §11a's four
  N1 kills; termination at `m = 25` is closure-forced).

Run:

```sh
python3 test_caseiii_two_pole_e5_r3.py       # 1,532,749 checks, ~11 s
python3 -O test_caseiii_two_pole_e5_r3.py    # same count, -O parity
python3 caseiii_two_pole_e5_r3.py            # print sealed certificate
```

`certificate_r3.json` is the sealed output (rebuilt from legal cells
only; the R2 field `pattern_fibre_infinite_at_fixed_kbar_nu_G` is gone
and the test requires its absence).  Ten staged mutations run on `/tmp`
copies inside both suites: R2's `MUT_A`–`MUT_F` plus the permanent
`MUT_G` (the `(38,19)`-style NE bypass: true strict-NE cap → `mu-1`
proxy; dies "strict NE law failed"), `MUT_H` (T1 re-specialised to
`{3,4}`; dies "Lemma T1' closed form disagrees with dq % dp"), `MUT_I`
(Theorem-F violator-M misstatement) and `MUT_J` (countercell M=1
disclosure flip).  The packet is never modified; the canonical engine
is imported read-only for the `cell_check` cross-check only.

Firewall: this packet licenses **no** canonical-engine change (`NUCAP`
stays; wholesale cap replacement is UNSOUND on `r0>=2`/inner-arrival
rows — all `M_G = 1` at `r0 <= 3` by Theorem F), no `U_7C`
adjudication, no equal-join `kbar` bound, no multipole or inner-merge
coverage, no realizability, no landing, no degree bound, no JC2, no AWS
or fleet action.  Status: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`.
Report:
`xmodel/m2-caseiii-two-pole-e5-local-index-r3-repair-fable5-20260829.md`.
