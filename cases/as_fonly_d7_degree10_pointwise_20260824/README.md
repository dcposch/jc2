# AS F-only `p=3,D=7` degree-ten pointwise gate

This package consumes the different-model-confirmed 40-variable/30-row
divided-carry predecessor, derives the exact degree-ten `8 x 9` affine digit
system, and classifies every field-valued rank stratum by augmented Fitting
ideals without replacing the nonreduced predecessor.

Exact outcome: rank zero is the degree-five-zero vertical branch; every
nonzero point has rank three.  The vertical branch survives.  On the
nonzero cone, only the two endpoint branches survive the degree-ten row.
Integer controls show that the vertical and `g` endpoint extend mod 81,
while the `a` endpoint subsequently fails a degree-eight cap-boundary row.

Replay:

```sh
python3 audit_source_compression.py
python3 replay_degree10_controls.py
Singular -q audit_high_radical_components.sing
Singular -q audit_pointwise_static.sing
python3 generate_reduced_pointwise.py | Singular -q
python3 audit_main_a_chart.py | Singular -q
python3 audit_main_g_chart.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

The independent static Fitting/radical replay is the single command
`Singular -q audit_pointwise_static.sing`; the generated replay is a second
implementation.  Each pointwise replay takes about 75 seconds on the
producer host.
Scope stops before the remaining next-carry rows on the full survivor locus,
other associated-top branches, full `D=7`, all-depth lifting,
characteristic zero, a counterexample, or JC2.
