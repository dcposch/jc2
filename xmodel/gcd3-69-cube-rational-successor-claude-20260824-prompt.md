# Focused research lane — rational trajectories in the `(6,9)` cube core

Work in `/Users/dc/code/math/jc2` at committed basis
`1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`, with frozen uncommitted
research artifacts on top. This is a new-mathematics lane, not a review.
Read in full:

- `xmodel/gcd3-69-cube-mismatch-gate-20260824.md`, SHA-256
  `6a2799dfe46828c70462d51a842a3fc0adf0515b8ded7a576cdb837d81847d20`;
- `cases/gcd3_69_cube_mismatch_gate_20260824/replay.py`, SHA-256
  `39246c1329c534adce2339ca940962cbb83951d7044b4888a8c7ea04fbd514dd`;
- the confirmed first common-cubic and aligned lower-Pfaffian producer/review
  chain, plus the target-translation erratum/review.

Treat the frozen cube report as provisional until its separate Grok hostile
review completes, but use its identities provisionally. The exact live object
is

```text
g=[H(f^(1/6))]_+,
r1'=r2'=r3'=r4'=0,
6r5'=j/s,
```

with the full target quotient, full source boundary jets, and terminal
dichotomy `s in k*` or `s=C(x-a)^m`, `m>=2`. The report explicitly leaves
`d!=0`, `d=0`, polynomiality, ramified common-component arcs, and JC2 open.

Attack the smallest global successor, not a generic coefficient rectangle:

1. Reinterpret the polynomial map
   `(a0,...,a4) -> (r1,...,r5)` using any useful exact structure: weighted
   compactification, Faber/Whitham or dispersionless Gelfand--Dickey
   coordinates, Lyashko--Looijenga maps, spectral curves, Darboux/Pfaffian
   flows, or a more elementary algebraic-curve formulation. State exactly
   which connections are identities and which are analogies requiring a
   source theorem.
2. For constant `s`, a polynomial Keller trajectory would be a polynomial
   section of `r1,...,r4=const`, with `r5` affine. Derive the sharpest
   dominant-balance/Kowalevski conditions on polynomial `a_i(x)`. Try to
   classify or obstruct every balance, beginning with the DS branch, common-
   cubic squarefree/double/triple branches, and any balance introduced by
   the mismatch constants.
3. For `s=C(x-a)^m`, use the prescribed
   `r5=c+j/[6C(1-m)](x-a)^(1-m)` together with all polynomial boundary jets.
   Determine what those jets force on finite poles of `a_i` and on the two
   ends of the invariant curve. Seek a divisor, genus, ramification, or
   semigroup contradiction that is stronger than rational exactness alone.
4. Analyze the ordinary-deformation failures and the open ramified/Puiseux
   arcs at the common component. Specify a finite Newton--Puiseux/Kuranishi
   calculation that treats every squarefree, double, and triple stratum,
   including how rational integrality of exponents and the core exponent m
   enter. If a short hand derivation closes one stratum, give it.
5. Keep `d=0` separate: its legal quotient retains
   `c7,c5,c4,c2,9c1-7c7c3`. Decide whether it is cheaper to classify before
   or after the `d!=0` rational components, and name the first exact
   discriminator.
6. Try to construct rather than only obstruct. Any putative polynomial or
   rational trajectory must be reconstructed through the inverse depression,
   both full polynomial boundaries, actual degrees `(6,9)`, and `J=1` before
   being called a Keller pair. List the exact reconstruction checks and stop
   at the first failure.
7. Return a ranked, deduplicated sequence of one-hour, six-hour, and one-day
   exact gates. Prefer a thin symbolic compiler for the source-derived
   invariant curve over broad enumeration. Explicitly falsify seductive but
   invalid shortcuts.

Do not edit producer, case, canonical, ladder, or erratum files. Do not use
AWS, generic sparse search, or claim that a local analytic survivor is a
counterexample. Write exactly one report:

`xmodel/gcd3-69-cube-rational-successor-claude-20260824.md`

At both ends state that this is research/ideation, not independent review or
promotion. Separate proved calculations, plausible connections, and proposed
tests. No statement may be promoted to a `(6,9)` exclusion, a Keller pair, or
JC2 without exact reconstruction and later hostile review.
