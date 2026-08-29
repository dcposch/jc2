# D3 `8_28` raw-to-global / `M`-cokernel interface

This is a desk-scale exact, fail-closed interface prototype.  It freezes all
raw `2S/3S` coefficient slots through weight 22 and the literal artificial
R0 face assignment, retains factor/deck/orientation tags, and attempts to
compile R0's local carrier fixture to a global `E22`.

The frozen run stops at

```text
local_carrier_fixture.raw_to_morse.cleanup_DAG
```

because no reviewed input serializes that derivation.  Accordingly
`RESULT.json` contains no typed global `E22` and no typed seven-vector.  The
hand-specified identity `1+(13/12)H=M(X/48)` is replayed only as a quarantined
reducer control.

Exact replay:

```bash
python3 compile_d3.py --check RAW_INPUT.json RESULT.json
```

No artifact here proves an `8_28` face/family exclusion, `G2-PSC`, `G2-BD`,
a Keller pair, a counterexample, or JC2.
