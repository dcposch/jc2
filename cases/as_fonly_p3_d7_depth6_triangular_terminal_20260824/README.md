# AS map-only triangular D7 depth-six point

Portable producer payload for the exact map

```text
P=x+2x^3+441x^5+108x^7,
Q=y-6x^2y+18x^4y-27x^6y
```

with `det J(P,Q)=1 mod 729` and residual `-x^12 mod 3` at the
next level.  The point is terminal at fixed total-degree cap seven; the full
map-only D7 locus is not classified.

Replay:

```sh
python3 compile_triangular_first_survivor.py
python3 replay_triangular_terminal.py
python3 replay_accepted_digit_trace.py
Singular -q audit_triangular_terminal.sing
shasum -a 256 -c MANIFEST.sha256
```
