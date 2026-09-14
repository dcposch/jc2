# K=7 logic and b=8 negative-control audit

All source-line citations below are to the frozen copies under
`/tmp/jc2-lane.qb6I1q/inputs/`.

## Custody

The required receipt-derived check was run mechanically (not by retyping the
digests):

```bash
awk -F= '/^charged_input_[0-9]+_basename=/{split($1,a,"_"); b[a[3]]=$2}
  /^charged_input_[0-9]+_sha256=/{split($1,a,"_"); h[a[3]]=$2}
  END{for(i=1;i<=7;i++) print h[i] "  /tmp/jc2-lane.qb6I1q/inputs/" b[i]}' \
  xmodel/k7-strata-gate-sol56-20260905.run.v2 | sha256sum -c
```

Result: 7/7 `OK`, with no content mismatch.

## Independent range recomputation

The degree-tower input declares `b = deg beta`, `b <= 2K-1` at lines 55--57,
proves that the `3b <= 2K` cases are impossible at lines 97--108, and gives the
post-LEVEL-4 interval explicitly at lines 349--362:

```text
b_min = max(ceil((2K+1)/3), ceil(2(K-1)/3)+1)
b_max = 2K-1.
```

At `K=7`:

```text
smin = ceil(2*(7-1)/3) = 4
ceil((2*7+1)/3) = 5
smin+1 = ceil(2*(7-1)/3)+1 = 5
b_min = 5
b_max = 13
residual integer degrees = {5,6,7,8,9,10,11,12,13}.
```

The second lower bound also follows directly from the full LEVEL-4 shape:
`P = y^smin (y-x) Q`, so a nonzero degree-`b` leading form has degree at least
`smin+1`; see beta-strata lines 41--56.  This is a necessary floor, not an
attainment statement.

The exclusions partition cleanly:

* `b=0`: the composite argument only.  Its exact scope is `beta in k`, not
  `deg beta < K` (degree-tower lines 332--341).
* Positive `b=1,2,3,4`: `3b <= 14 = 2K`, contradicted by the proved necessary
  inequality `3b >= 15` (degree-tower lines 85--111).
* `b=5`: the banked exact-Q chart unit (beta-strata lines 73--75; the pinned
  leading form is recorded at degree-tower lines 369--378).
* `b=9,10,11,12,13`: the five proposed closures, each requiring both cover
  charts (strata-solve lines 192--200 and 252--270).

Therefore, **if and only if the ten proposed charts are validated**, the
remaining open K=7 degrees are exactly `{6,7,8}`.  The chain does not misuse the
composite arm to cover `1 <= b < K`, and it does not turn the floor into an
equality.

## b=8 control: cover and fresh emission

For K=7, b=8, `smin=4`, `d=3`, and
`Q=q0*x^3+q1*x^2*y`.  The two charts are the exhaustive cover

```text
q0 != 0                         (q1 free),
q0 = 0, q1 != 0.
```

See beta-strata lines 43--58.  A unit on only one chart is not a unit on their
union and does not close the stratum.

Fresh exact-Q, denominator-cleared `.ms` emissions were produced with:

```bash
python3 -u box/k4ray-strata-solve-20260905/msolve_export.py 7 8 \
  --pin-index 0 --char 0 --dump-timeout 600 \
  --outdir box/k7-strata-gate-20260905/logic-negative/emission
python3 -u box/k4ray-strata-solve-20260905/msolve_export.py 7 8 \
  --pin-index 1 --char 0 --dump-timeout 600 \
  --outdir box/k7-strata-gate-20260905/logic-negative/emission
```

They agree byte-for-byte with the hashes recorded by the frozen solve:

```text
q0: 65 variables, 221 generators, 7,580,109 bytes
    sha256 24507c39c2e3e6385e233fc79bb58dc586338de50c3c06851d96e2192b5f068b
q1: 64 variables, 215 generators, 6,701,623 bytes
    sha256 062ccc0c7dc7e83aee99f2cf1a8d2a6b7c05c82e1a468e9d6a97557eae511f25
```

Both fresh preludes report `DUMP__DONE 1`, `PRE__CST_ZERO 0`,
`PRE__HOMOG_I 1`, `PRE__HOMOG_CST 1`, `TARGET_FOUND 1`, and the correct
Rabinowitsch localizer.  Full markers are in the two JSON files in `emission/`.

### Frozen actual status

* q0 exact Q: **UNIT**, reduced basis `[1]`, basis length 1; msolve time
  1424.280 s and total time 1463.834 s, hence inside 40 minutes.  This is not a
  successful non-unit negative control.  Source artifact:
  `box/k4ray-strata-solve-20260905/fleet-pull/172.30.0.246/msolve/K7_B8_Q0_p0.{json,msout}`.
* q1 exact Q: **no mathematical result**.  The process was deliberately
  preempted/SIGKILLed (`rc=-9`) after 2454.917 solver seconds, with a zero-byte
  output.  The solve report calls this preemption explicitly at lines 285--289.
  Source artifact:
  `box/k4ray-strata-solve-20260905/fleet-pull/172.30.0.88/msolve/K7_B8_Q1_p0.{json,msout}`.

The frozen report consequently labels b=8 partial, not dead (lines 192--200,
298--300).  It would be a carrier/attainment error to infer either q1 or the
whole b=8 stratum from q0.

### Fresh q1 exact-Q run

Completed with an exact 2400-second hard cap and the byte-identical q1 input:

```bash
timeout --signal=TERM --kill-after=20s 2400s /usr/bin/time -v \
  box/moh14-charts-20260905/tools/msolve-0.10.1-official-intel-avx512/msolve \
  -g 2 -t 2 \
  -f box/k7-strata-gate-20260905/logic-negative/emission/K7_B8_Q1_p0.ms \
  -o box/k7-strata-gate-20260905/logic-negative/emission/K7_B8_Q1_p0.fresh.msout
```

Binary: msolve 0.10.1, SHA-256
`0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`.

Result: **exact-Q timeout / OPEN**.  GNU `timeout` returned `124` at the
2400-second boundary; both the solver stdout and `.msout` are zero bytes, so no
basis (unit or non-unit) was produced.  No child process remained afterward.
The last pre-timeout observation was 37,099,468 KiB RSS (about 35.4 GiB).
Consequently the fresh independent-build run agrees with the frozen q1 status
at the only level justified: **undecided**, never `NONUNIT`.

Combined b=8 control status: q0 is an exact-Q unit, q1 is an exact-Q timeout,
so b=8 remains `OPEN (one-cover partial)`.  The requested negative control did
return `[1]` on q0, and that actual status must be disclosed; it did not return
`[1]` on the unresolved q1 run within 40 minutes.

## FALLACY-v2 disposition

* **Floor/attainment:** pass.  Use `3b>=2K+1` only to exclude `b<=4`; do not
  infer `b=5` or any witness from the lower bound.
* **Carrier/attainment / cover:** pass only with both charts per degree.  The
  b=8 q0 unit cannot be promoted to a b=8 closure while q1 is unresolved.
* **Composite scope:** pass only when stated as `b=0`; claiming it kills all
  `b<K` would be the exact false meeting-point argument rejected by the degree
  report at lines 332--341.
* **Timeout/resource status:** a timeout or `rc=-9` is typed `OPEN`, never a
  non-unit, survivor, or counterexample (FALLACY-v2 lines 29--30).
* **Variable/ring and localization:** the fresh markers confirm a nonzero
  target image and explicit localizer; `sat()` is not used.  This does not by
  itself prove a GB result.
* No exit-price assertion is made, so no `charge_basis=` declaration belongs
  in this audit.
