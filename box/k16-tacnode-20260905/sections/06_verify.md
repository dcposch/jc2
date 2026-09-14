## 6. Task (3): exact verification at t = 3, 4, 5 against the frozen certificates

Driver `custody_tacnode.py` (`custody_tacnode_t{3,4}.sing` exact over `Q(d)`, `minpoly 3d² - N`; `_t{3,4,5}_p31991_d{14162,4933,6434}.sing`
modular controls, `--hensel` adds the b = 1 Hensel replay) replays the frozen top-down data as the charged `custody_bu.py` does,
builds `Q_P(x, Y)` with a ring variable Y, `D = d_Y Q_P(x, L)`, `Lpivot`, `piv_2`, `T_2`, and tests in `S = k[c, b]` (weights `wt c_j = j`, `wt b = N`).

```text
t  frozen rows/B/eta/T   [x⁰]D=[x¹]D=0  [x²]D=(b/4)Lpivot  deg D, lc   [x³]D-(3/4)piv_2  Lpivot²+4T_2+24E_2  Q_P(x,L)+UF  std(J) dim,vdim  socle
3  equal (exact)         yes            yes                12, yes     0 (cofactor 0)    0 (exact)            0 (exact)    0, 66            14
4  equal (exact)         yes            yes                15, yes     0 (cofactor 0)    0 (exact)            0 (exact)    0, 338 (10 s)    21
5  (mod p control)       yes            yes                18, yes     0 (cofactor 0)    0 (mod p)            0 (mod p)    0, 1709          30
```

Every entry in the first eight columns is a polynomial identity in `k[c, b]` (not a membership), hence non-vacuous; `homog` and
the weight of every `[x^j]D` were checked (`D_WEIGHTS_CHECKED`).

**Memberships in J** (charged §5 caveat: a membership above the socle degree is weight-forced; a NON-membership at weight
<= socle is non-vacuous; `wt [x^j]D = 3N - j`, `wt Lpivot = 2t`, `wt piv_2 = 3t`, `wt T_2 = 4t`, `wt B*eta = 4t + 1`):

```text
t  Lpivot in J / min power  piv_2 / min power  T_2 / min power  [x^j]D in J (j = 2..3N-1)  Lpivot^2, Lpivot*B, Lpivot*eta in J (non-vacuous)
3  no / 3 (vacuous)         no / 2 (vacuous)   no / 2 (vac.)    none (min powers 2,2,2,3,3,3,4,5,8,9)   no, no, no
4  no / 3 (vacuous)         no / 2 (vacuous)   no / 2 (vac.)    none                                    no, no, no
5  no / 4 (Lpivot^3 notin J non-vac.)  no / 3 (piv_2^2 notin J non-vac.)  no / 2 (vac.)  none          no, no, no
```

**The degenerate stratum `J_deg = J + (Lpivot)` and the target (new, exact).**

```text
t  vdim J_deg   (B*eta)^n ∈ J_deg: min n   non-vacuous?          B, eta, piv_2 ∈ J_deg   vdim J+(B*eta)   Lpivot^m ∈ J+(B*eta)   Lpivot^m ∈ J+(eta)   Lpivot^m ∈ J+(B)
3  41           n = 1                      YES (wt 13 <= 14)      no, no, no              64               m = 3                  m = 2 (wt 12: non-vacuous)   m = 3
4  215          n = 2                      B*eta ∉ J_deg is non-vacuous (wt 17 <= 21); n = 2 vacuous   no, no, no   327   m = 3 (Lpivot² ∉: non-vac.)  m = 3   m = 3
5  1099 (mod p) n = 2                      B*eta ∉ J_deg non-vacuous (wt 21 <= 30); n = 2 vacuous      no, no, no   1651  m = 3 (Lpivot² ∉: non-vac.)  m = 3   m = 3
```

Reading: "degenerate tacnode ⇒ (R)" holds at the IDEAL level at t = 3 (n = 1, weight 13 in a ring of socle degree 14) and only
at the radical level at t = 4, 5; the converse needs m = 3 everywhere with `Lpivot² ∉ J + (B*eta)` non-vacuous. Neither
direction is uniform at the ideal level.

**Hensel replay (modular controls, b = 1, order M = 2N+2; t = 3 `d -> 14162`, t = 4 `d -> 4933`, 157 s; t = 5: §10).** All lines
pass at t = 3, 4: `Q_P = (3/16)F_0F_1` mod `x^{M+1}`; `F_0(L)F_1(L) + (16/3)UF = 0` (L is a root of `F_0` modulo J); `s_1 = p_1 = 0`,
`s_2 = p_2 = 8eta/3`, `s_3, p_3, s_4, p_4` as in Prop. 2.4; `Disc(F_0) = O(x⁴)`; `[x⁴]Disc(F_0) + (16/9)T_2 = 0` and
`[x⁴]Disc(F_0) - (4/9)Lpivot² in (E_2)`; the direct `resultant(Q_P, d_Y Q_P, Y)` confirms `[x⁴]Disc_Y(Q_P) ∝ T_2` (`hensel_debug2`). (The rejected draft with total-degree `jet` truncation is in `hensel_debug*`; §8.)

The generic-jet checks (K = 10, 20 named checks, ALL_PASS) and the reproduction of the frozen `universal_recursion.json`
values (pivot laws, `Φ_4`, `Φ_5`, `Q_P(0, L) = (3/16)(L+b)²(L²+b²)`, `d_L Q_P = (b/4)Lpivot*x² + ...`) are in `tacnode_involution_K10.json`.
