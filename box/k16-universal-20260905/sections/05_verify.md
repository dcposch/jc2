## 5. Task (4): exact verification at t = 3, 4, 5 against the frozen certificates

Drivers `custody_bu.py` (full numerators) and `custody_bu_red.py` (every numerator reduced modulo `std(J)` as it is
built — legitimate because J is an ideal and the recursion uses only ring operations and scalar divisions), exact
over `Q(d)` with `minpoly 3d² − N`; modular controls at `p = 31991` with the declared root of `3d² − N`.

```text
t  frozen rows/B/eta/target reproduced from (UF)   std(J): dim, vdim   T∈J  T²∈J   socle degree of J   non-vacuous membership   L-pivot: in J / power in J   B, eta, b powers in J
3  yes (5 rows)  exact                              0, 66   (0 s)       no   yes    14                  k = 4 only (wt 12)        no / 3                       3, 3, 4
4  yes (7 rows)  exact                              0, 338  (10 s)      no   yes    21                  k = 4 only (wt 16)        no / 3                       3, 3, 5
5  yes (9 rows)  exact                              0, 1709 mod p       no   yes    30 (mod p)          k = 4 only (wt 20)        no / 4  (mod p, k ≤ 24)      3, 4, 6  (mod p)
```

**What was checked.** (i) Custody: the (UF)-emitter's `E_2..E_{2t}`, `B`, `eta`, `B·eta` equal the frozen objects under
`imap` (identity on `(c_i, b)`) at t = 3, 4, 5 exactly. (ii) Consistency of the two recursions: with the top-down data
`(b, B^TD, eta^TD, w_2^TD)`, `b^{2(k−3)} P^TD_k − N_k ∈ J` (4 ≤ k ≤ 2N) and `N_k ∈ J` (2N < k ≤ 4N), b-power 0 throughout
(t = 3, 4 exact; t = 4, 5 modular). **Vacuity caveat (FALLACY-v2, floor/attainment):** J is `m`-primary with socle degrees
14, 21, 30, while `wt N_k = (2N−1)k − 4N` is 12, 16, 20 at k = 4 and 19, 25, 31 at k = 5: every membership with k ≥ 5 is
forced by weight and is NO evidence; only the k = 4 identity (row 4, `E_2 ∈ J`) is non-vacuous. The truncation conditions
are consistent with the frozen ideal, but their membership is not an independent certificate here — the dual chart is.
(iii) The L-pivot `4 eta + 3 b c_{t−1}/y` (weight 2t) is NOT in J at t = 3, 4 (non-vacuous); `B², eta² ∉ J`,
`B³, eta³ ∈ J` as charged; `b⁴ ∈ J` (t = 3), `b⁵ ∈ J` (t = 4).

**The dual chart as an instrument (Prop. 4.2), `dual_chart.py`.** Unknowns `B, eta, l_2, P_3, P_5..P_{N+2}, u`
with `u·(4 eta + 3 l_2) = 1`, `b = 1`, `l_N = 1/y`; rows 5..N+1 solved for `l_3..l_{N−1}` through `u`; conditions
row N+2 and rows 2N+1..4N.

```text
t  field           full chart (u present)   pivot locus not excluded (no u)   negative control (first t+1 conditions)   time
3  GF(31991)       UNIT  (14 s)             UNIT  (176 s)                     dim 6, NONUNIT (61 s)                    ≤ 1 s for the charged bottom_up.py
3  Q(d), 3d²=4     not finished (29 min, §9) —                                —                                        —
4  GF(31991)       TIMEOUT 2400 s (§9)      —                                 —                                        27 s for the charged bottom_up.py
```

At t = 3 the dual chart is empty even on the pivot locus (consistent with `V(J) = {0}`) and the negative control is
non-unit: the L-recursion is a correct instrument, but slower than the Theorem H rows and the P-recursion, and it
grows faster with t (the `u`-substitutions carry the pivot denominators into every row). The t = 2 controls are in §4.
