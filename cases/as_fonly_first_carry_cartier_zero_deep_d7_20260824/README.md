# Universal first-carry Cartier zero and deep D7 branch

This portable producer contains:

- the all-prime termwise proof that the basic Cartier coefficient of the AS
  first carry vanishes;
- a nonzero source-honest carry control at `p=3`;
- the complete 40-variable/29-row first-digit acceptance scheme on the
  `U7=V7=0`, degree-six-Frobenius branch; and
- its exact nonradical equality with two saturation branches.

Replay:

```sh
python3 replay_universal_cartier.py
python3 generate_deep_branch_gate.py | Singular -q
DECOMP=1 python3 generate_deep_branch_gate.py | Singular -q
Singular -q audit_cartier_control.sing
shasum -a 256 -c MANIFEST.sha256
```

Scope stops before accepted-second-digit classification, the next carry, or
coverage of the other associated-top branches.

