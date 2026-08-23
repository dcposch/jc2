# D43 characteristic-zero lift screen at B=84

**Date:** 2026-08-23

**Prime:** (p=105337), residue-A fiber `a00pp`

**Status:** **SOURCE-MODEL (p^2) SCREEN PASSES; STAGE 2 OPEN**

## Verdict

The banked D43 point has no first-order obstruction in the canonical pristine
Euler/source equations.  With the coefficient radicals lifted by their simple
Hensel equations, the all-row correction system has rank profile

\[
 \operatorname{rank}J_{\rm source}=129
 =\operatorname{rank}[J_{\rm source}\mid-F/p],
\]

and an explicit 24-coordinate correction kills all 184 pristine rows modulo
(p^2).  The correction can be chosen without the eight raw source tails
eliminated from the 184-coordinate reconstruction.

This does **not** certify that the 218-row assembled point reaches (p^2).
The shipped point bank has already evaluated the 28 parked coordinates, while
the 19 prime-specific NF checkpoints, their integral source-to-NF traces, and
a common integral 34-row parked emission are absent.  In particular, lifting
the displayed reduced coefficients or the displayed (W_i) residues as
ordinary integers would define a different (\mathbf Z_p)-scheme.

The exact full special-fiber Jacobian rank is nevertheless recoverable:

\[
 \boxed{\operatorname{rank}J_{218}(\bar x)=131},\qquad
 \dim T_{\bar x}=184-131=53.
\]

A (131\times131) minor is (810\not\equiv0\pmod {105337}).  Local Krull
dimension, localized generation by those 131 equations, and (p)-flatness
are not certified.  Therefore the minor is not a standard-smooth certificate
and Hensel/formal smoothness cannot be invoked.

\[
 \boxed{X_{43}^{\rm full}(\mathbf C)\ne\varnothing\ \textbf{remains open}.}
\]

There is no certified local obstruction to this point: the available exact
first-order source test is positive.  There is also no certified
characteristic-zero point.  **Stage 2 is not cleared.**

## 1. Integral source model and reduction audit

The exact source evaluator is the pristine 184-row Euler system behind
`valuation_e2.py`, configured to (D=43).  It is evaluated directly over the
Hensel-selected (\mathbf Z_p) embedding of

\[
 r_3^2=3,\quad \zeta^{42}=1,\quad
 A_1^3=3+r_3,\quad A_2^3=3-r_3,\quad 2h^2=3.
\]

The roots modulo (p^2=11095883569) are

| root | value modulo (p^2) |
|---|---:|
| (r_3) | 11012141449 |
| (\zeta_{42}) | 8852313585 |
| (A_1) | 786496672 |
| (A_2) | 8038065910 |
| (h) | 6003627245 |

All five defining residuals are exactly zero modulo (p^2).  These are
simple-root lifts, not integer substitutions for finite-field roots.

The raw source registry has 180 tail coordinates, eight fixed source
coordinates

```text
W1 W2 uf18 uf24 vf1_34 vf1_36 vf2_34 vf2_36
```

and independent `alpha,beta`, hence 190 coordinates.  The assembled registry
removes the eight raw tails

```text
tf1_71 tf1_73 tf2_71 tf2_73
tg1_71 tg1_73 tg2_71 tg2_73
```

and adjoins `uW1,uW2`, giving 184 coordinates.  The positive (p^2)
correction replays after the eight removed coordinates are held fixed.

Available reduction checks pass:

- point-bank SHA-256
  `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb`;
- 184 rows, 156 graph variables, 107,665 terms, degree at most 6;
- 184/184 point-bank rows vanish at the banked point;
- canonical point-bank row hash
  `e60d90ac9dd449c6aa2d4359cef30078663e7f86ce4ddb702104553eaa281eea`;
- the independent pristine evaluator agrees on all 184 values and all 180
  tail-Jacobian columns;
- all eight fixed-source Jacobian columns agree with independent
  (p^2)-finite differences;
- the `tf1_57 += 1` negative control breaks 18 rows identically in both
  evaluators.

The requested polynomial row/term/hash regression over a **common integral
218-row model cannot be run**.  Every path recorded for
`d43red_p105337_a00pp_band{6,...,42}.pkl` is absent.  The surviving
`d43_full_pointbank_p105337.pkl` is a fixed-parked-point evaluation, not the
polynomial family.  The integral NF membership traces and an integral parked
presentation are also absent.  Consequently the explicit equations
(W_i^4=\mathcal A_i) and their common-ring right sides cannot be recovered
from the displayed modular (W_i) values without changing the model.

This is a failure of Step 1's certificate input, not a proof that no common
integral model exists.

## 2. Exact (p^2) correction screen

Let (x_1\) be the least-residue coordinate lift, while the coefficient
radicals use the Hensel lifts above.  Among the 184 quotients
(F_i(x_1)/p\bmod p), 29 are nonzero.  Their canonical hash is

```text
0d5debb8bad4c70be88c1f38b92ebf0eff749369ae9a7642127250d4d91adad1
```

For all 190 raw source coordinates,

\[
 \operatorname{rank}J=129
 =\operatorname{rank}[J\mid-F(x_1)/p].
\]

RREF with free corrections zero gives 24 nonzero corrections.  Direct
reevaluation—not a linear prediction—gives 184/184 rows exactly zero modulo
(p^2).  The correction hash is

```text
c3f38ba90fb0b65ee497eb0a2fe663e1a28879adaa1e832a02e955b47ea486b1
```

After dropping the eight source coordinates absent from the assembled
registry, the ranks remain (129=129); a second 24-coordinate correction
again replays 184/184 rows modulo (p^2).  Its hash is

```text
e3a15fa66ed6f08e3f1c78eb793226ad750ab67a9216ce3dadbaeae82ad79c26
```

Thus the pristine point reaches (p^2) within the represented coordinates.
This is a necessary positive screen only.  The missing integral parked/NF
identities prevent replay of all 218 integral generators.

## 3. Full modular rank and local dimension

At the special-fiber point:

| block | exact rank |
|---|---:|
| 34 parked rows | 14 |
| 184 graph rows in the 156 graph columns | 111 |
| block lower bound | 125 |
| 184 pristine rows in the represented 184-coordinate registry | 129 |
| parked + pristine combined row space | **131** |

The last equality also gives the rank of the banked NF presentation.  Indeed,
each checkpoint identity is

\[
 R_{\rm raw}=R_{\rm NF}+\sum_i Q_iP_i
 \quad\text{over }\mathbf F_p.
\]

At a parked point (P_i(\bar x)=0), adjoining the parked Jacobian makes the
raw and NF combined Jacobian row spaces equal.  The original modular audit
certified these NF reductions; the integral versions of the identities are
what is missing.

The exact tangent dimension is therefore 53.  It is not the local Krull
dimension.  At the fixed `FREE=0` parked origin, all nine band-10 graph rows
are identically zero in the 156-variable point slice.  A local-order Singular
standard-basis attempt on the 175 nonzero slice rows (107,665 terms before
removing the zero rows) was capped after ten CPU minutes inside `std`; it
returned no dimension.  No rank-to-dimension equality is claimed.

The banked smooth-point search had already tested 42 ordinary D25 points
(21 per prime) and prolonged none; the present witness lies on a proper
special sublocus found by the reconstructed solver.  No smooth point of that
modular component is certified.

## 4. Minor, generation, flatness, and Hensel gate

Canonical elimination selects 131 equations and 131 variables with

\[
 \det M\equiv810\pmod {105337}.
\]

The complete row/variable lists and combined-matrix hash

```text
af4582348b561b85c47d31c1859e33047db1a488e05c540f424716a52657b143
```

are in `cases/d43_char0_lift_p105337.json`.

This certifies only the Jacobian rank.  The following required implications
are absent:

1. local dimension (=53), equivalently local height (=131);
2. the selected 131 equations generate all 218 after localizing at the minor;
3. the common integral local ring is (p)-flat;
4. the integral NF/parked equations reduce to the banked rows.

Therefore the point is not certified standard-smooth over (\mathbf Z_p),
and Stacks 02H6 does not apply from the present artifacts.

## Artifacts and replay

- `cases/d43_char0_lift.py`: exact Hensel coefficient lifts, independent
  integer source evaluator over (\mathbf Z/p^2), correction solve/replay,
  exact full modular rank, and unit-minor emitter.
- `cases/d43_char0_lift_p105337.json`: machine-readable certificate and the
  explicit promotion blockers.

Replay:

```bash
python3 cases/d43_char0_lift.py \
  --out cases/d43_char0_lift_p105337.json
```

Expected terminal line:

```text
D43 p-adic source screen p=105337: rank 129/129, correction SOLVABLE; assembled-218 certification OPEN
```

## Final tier

**Exact positive result:** the common pristine source equations admit a
represented-coordinate lift modulo (p^2); the special-fiber 218-row
Jacobian rank is 131 and has a unit minor.

**Not obtained:** an all-218 integral (p^2) replay, local dimension,
localized generation, flatness, a standard-smooth point, a (\mathbf Z_p)
point, or a characteristic-zero D43 point.

\[
 \boxed{\textbf{STAGE 2 OPEN; no local obstruction found, no Hensel certificate.}}
\]
