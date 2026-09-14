
## 9. Computation record (`box/k16galois-20260905/`)

```text
manifest.sha256, manifest.check.log         custody (awk-generated; sha256sum -c: 10/10 OK)
gen.py                                      the emitter (prefix from the frozen rows; jobs pattern | exactchart | boundary | colon | msolve | verifypoint)
run.sh, deploy.sh                           foreground runner (stdbuf -oL, timeout, .time), worker deployment
primes.txt, sweep_t{3,4}.sh, w18_jobs.txt, w166_jobs{,2}.txt, misc_desk.sh    prime lists and batch drivers
pattern_t{3,4}_mod_p*_b*.{sing,out,err,time}         desk sweeps (49 + 48 prime ideals; < 1 s each)
w18/pattern_t5_mod_p*_b*.*                   t = 5 sweep, 24 prime ideals (0–3 s each)
w166/pattern_t6_mod_p*_b0.*, pattern_t6_mod_p32003_b0.*   t = 6, 8 completed primes (≈ 150 s each: std 3 s, finduni ≈ 145 s, factorize ≈ 1 s)
minpoly_pattern_*_q2_0.txt                   the modular point polynomials m̄ (written by every pattern job)
exactchart_t3_exact.*                        exact chart std, finduni, factorize over A_3 (< 1 s): 7^1
exactchart_t4_exact.*                        exact chart std over A_4 (< 1 s, vdim 46); finduni not finished (see below)
w7/exactchart_t5_exact.*                     exact chart std over A_5: vdim 265 in 426 s; finduni not finished (see below)
boundary_t{3,5}_exact.*, boundary_t{4,6}_mod_*.*, w18/boundary_t8_mod_p32003_b0.*   boundary strata (exact at t = 3, 5; t = 8 re-run on W18, 179 s), with (stratum + (W)) vdim
colon_t3_exact.*, colon_t{3,4,5}_mod_*.*     (G):T_top = (G) with controls (t = 3 exact < 1 s; t = 5 mod p 5 s)
colon_t4_exact.* (W166, lost; rerun on W18)   exact t = 4 colon: std(G) 55 s, quotient not finished when W166 went down
msolve_t6_mod_p32003_b0_ci.{sing,ms}, w254/msolve_t6_param.txt, msolve_point.py    msolve calibration at t = 6 (1.5 s), parser validated
msolve_t8_mod_p32003_b0_ci.{sing,ms} (79 MB), w28/msolve_t8.log   t = 8 CI system mod 32003, msolve F4 (see §5.3 / OPEN)
verifypoint_t6_mod_p32003_b0.*               the verify job on the t = 6 point (local vdim 1, all checks 1)
analyze_patterns.py, frobenius_tables.txt    subset-sum intersection, Galois bookkeeping, the full cycle-type / instrument tables
sections/                                    the report sections as written (append-only), assembled into the report
```

Wall clock (single core unless stated): modular jobs at t ≤ 5 are seconds; t = 6 pattern 143–163 s; exact chart
`std` 0 s (t = 3, 4), 426 s (t = 5); t = 8 prefix + export 59 s, t = 8 boundary strata 190 s.  Not finished:
exact `finduni` over `A_4` (desk) and `A_5` (W7) — number-field linear algebra, > 40 min at seal although the
exact std before it took 0 s / 426 s; `nfmodStd` was killed twice (it ignores `--cpus` and forked 17–30
processes, over the core budget); the exact t = 4 `quotient` and the Singular t = 8 chart `std` were lost when
workers .166 and .254 became unreachable at ≈ 13:16Z and were re-launched on W18 (status at seal: §5.3, §6).  No
unfinished item carries a claim.
