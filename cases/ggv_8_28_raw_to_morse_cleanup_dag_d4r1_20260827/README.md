# DEP-D3 D4R1 factor-local cleanup DAG

This additive case repairs the quarantined D4 precursor/Morse-value type
error.  It compiles the generic factor-local Morse data through weight 22
and then exactly evaluates the full DAG under the five-row discriminator,
requiring `U14=c` in `Q[c]/(c^8-1)`.

Replay:

```bash
python3 compile_cleanup_dag_d4r1.py --check \
  ../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  RESULT.json
```

The result is factor-local formal algebra only.  It supplies no global
`E22`, global `H`-multiple control, or face/family exclusion.
