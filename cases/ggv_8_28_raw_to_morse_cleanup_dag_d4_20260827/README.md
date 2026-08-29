# DEP-D3 factor-local raw-to-Morse cleanup DAG

This case deterministically compiles all coefficients through weight 22 of
`U,W,V,Q,Gamma` from the 400 positive-weight raw `2S/3S` slots, after fixing
`F0=H^2`, `G0=H^3`.  It works simultaneously over
`A=Q[c]/(c^8-1)` and retains the four factor tags and the orientation
`u=H mod t`.

Replay:

```bash
python3 compile_cleanup_dag.py --check \
  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  RESULT.json
```

The result also contains a literal positive discriminator showing that
legal lower raw rows synthesize local `U14=X` even with raw `F14=0`.

This is a factor-local formal cleanup compiler, not a global polynomial
automorphism, a global `E22`, or a face/family exclusion.
