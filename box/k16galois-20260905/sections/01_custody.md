
## 1. Custody

The receipt `xmodel/k16-gamma-galois-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing its
`charged_input_<i>_sha256=` / `_basename=` lines into `box/k16galois-20260905/manifest.sha256`; `sha256sum -c`
→ **10/10 `OK`** (`manifest.check.log`).  No digest was retyped.  All ten charged inputs were read before any
driver ran.

**Row provenance.**  Every job in this lane is emitted by `gen.py` from the frozen rank-lane row dumps
`box/k16rank-20260903/terminal_t{t}_exact_none.out` (t = 3..8; the charged `singular_terminal_driver.py`
`--mode exact --dump-rows` outputs, byte-unchanged; each file carries `RECURRENCE_PASS` and `DRIVER_DONE`
and no error marker).  The top-tail rows `T_{t,2t−1−r}`, r = 0..t−1, are re-parsed into
`S = K[b4,q2_0,..,q{t−1}_0,b3]`, `wp(1,2,..,t−1,t+1)` with `K = Q(yy)/(H_t)` (`minpoly`) or `GF(p)` with
`yy` a declared root of `H_t` mod p; every job re-asserts, before anything else, `T = a_r b3² + b_r b3 + c_r`,
weighted homogeneity of weight 2t+2+r, `G_r = a_0 T_{2t−1−r} − a_r T_{2t−1} = B_r b3 + C_r`, and the ELIMINANT
certificate `W_r = B_r² T_{2t−1} − G_r(a_0 G_r − 2a_0 C_r + b_0 B_r)`; a `FAIL` marker aborts acceptance (none
occurred in any accepted run).  The mod-p generators are therefore the reductions of the exact generators (ring
operations, one division by 2); `.err` streams were scanned for `div. by 0` (none).  Modular primes are the
largest split primes below 2¹⁵, both primes 𝔭 | p used (`primes.txt`).
