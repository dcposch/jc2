# Repaired residue-ball replay successor

This wrapper pins the frozen three-ball replay source and adds the explicit
coefficientwise assertions

```text
P mod 3 = x-x^3,       Q mod 3 = y.
```

Run on AWS only:

```sh
JC2_ROOT=/path/to/source python3 replay_repaired.py
```

It changes no mathematical equation or finite-Hensel calculation.
