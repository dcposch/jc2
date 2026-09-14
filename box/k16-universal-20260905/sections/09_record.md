## 9. Computation record (`box/k16-universal-20260905/`), collision scan, completion

```text
manifest.sha256, input-verification-final.log   custody (awk manifest; sha256sum -c 4/4 OK at start and at sealing)
universal_recursion.py/.json/_K12.log           Props 2.1, 2.2, 3.1, 4.1(a,b), 4.2 with generic jets, K = 9, 12: ALL_PASS
tacnode_checks.py/.json, degenerate_pivot.py/.json   tangent cone + discriminant; P = −L²/4 reduction; second L-pivot (k = 5..10)
custody_bu.py → custody_bu_t3.*                 exact t = 3 (full numerators); custody_bu_t4.* exact TIMEOUT 1500 s at k = 16 (superseded)
custody_bu_red.py → custody_bu_red_t4.*, _t5.*  exact, numerators reduced mod std(J): t = 4 complete (std 10 s); t = 5 rows equal, std: see below
custody_bu_t4_p31991_d4933.out, custody_bu_t5_p31991_d6434{,_long}.out   modular controls (short t = 5 run: k ≤ 20 then TIMEOUT)
socle.py → socle_t{3,4}.sing, socle_t5_p31991.sing   socle degrees 14, 21, 30 (kbase max weight)
dual_chart.py → dual_chart_t3_p31991_d14162.*, dual_chart_t3.*, dual_chart_t4_p31991_d4933.*   dual charts (§5, below)
t2_controls.sing/.out                            t = 2 both roots: V(J), rad J, L-pivot ∈ rad J, P + L²/4 on c_1 = 0
prelim_report.md, collision_scan{,.filtered}.txt, artifacts.sha256, hash_artifacts.sh, finalize.sh, sections/
```

All CAS work local, `--cpus=1`, ≤ 4 Singular processes at once. One shell was lost to a self-matching `pkill -f`
(no artefact affected; three misplaced driver copies were moved from the repository root into the box).

Collision scan (`ops/open_collision.py --root .`, filtered of this lane's files): `OPEN[K16-UF-DEGENERATE-TACNODE]`:
**NONE**. Retained OPENs: 17(ccccccc), 17(jjjjjjj) (the charged sources), 17(yyyyyy)/(zzzzzz)/(hhhhhhh)/(eeeeeee) (Moh/census
deltas: lexical noise), the K16 deltas 17(xx)–(vvvvvv) for `OPEN[K16-UNIFORM-POINT]` (KNOWN), and two lines of the
same-round `ideation-20260905T1200Z-astra.md` (uncharged, not read). Nothing closes any OPEN.

Status of the long runs at sealing:
- `custody_bu_t5_p31991_d6434_long.out` (modular t = 5): COMPLETE — vdim 1709, memberships k = 4..24 all b-power 0,
  L-pivot ∉ J, its 4th power ∈ J, B³, eta⁴, b⁶ ∈ J (weight-forced above k = 4 / socle degree 30, §5).
- `custody_bu_red_t5.out` (exact t = 5): rows/B/eta/T equal (exact); the exact `std(J)` over Q(d) had not finished after
  32 min and was stopped at seal — no exact t = 5 membership is claimed (modular control only).
- `dual_chart_t3.out` (exact dual chart, t = 3): substitutions done, `std` not finished after 29 min, stopped at seal — no claim.
- `dual_chart_t4_p31991_d4933.out` (modular dual chart, t = 4): TIMEOUT at 2400 s inside `std` (the charged P-recursion
  chart is unit in 27 s): the dual chart is the more expensive instrument, as stated in §5–§6.
