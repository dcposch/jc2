# TD6-C1-FIRST-STAGE-LOCALIZED — the generic center line reduces to one quadratic stratum

Date: 2026-08-24  
Status: **EXACT PRODUCER / SOURCE-VALID POLYNOMIAL-IDEAL CERTIFICATE / STOP AT `J`**

## Verdict

For the frozen normalized TD6 control

\[
 (c_1,c_2,c_3)=(C,1,1),\qquad p=t^{15},\qquad q=t+t^{25},
\]

the exact generic transport rank is `3470/3602`, leaving 132 parameters,
and the exact first-band rank is `38/132`.  Before any first-band
substitution, the genuine current `t^12` row is a degree-two polynomial with
2,893 parameter monomials.  Exact division by the first-band linear ideal,
followed by a lift back to the original first-band rows, gives

\[
 D(C)P_{12}=-{k\over50}D(C)+\sum_i M_i(C,\mathbf u)L_i(C,\mathbf u),
\]

where

\[
\begin{aligned}
k&=252-342S+144S^2-36S^3,\\
D(C)&=C^4-C^3-{83\over4}C^2+{87\over2}C+{9\over4}\\
&={1\over4}(C-3)^2(4C^2+20C+1).
\end{aligned}
\]

All coefficients and all 28 nonzero original-row multipliers are emitted and
replayed exactly.  Hence, on the generic transport chart, every point with

\[
4C^2+20C+1\ne0
\]

is impossible.  Combining this localized identity with the separately frozen
adaptive raw-transport certificates at `C=0,3` leaves exactly the quadratic
stratum

\[
J(C)=4C^2+20C+1=0
\]

unresolved.  This report does **not** claim that the whole `c1` line is empty.

```text
TD6-C1-FIRST-STAGE-LOCALIZED / OPEN STRATUM J(C)=0 /
NOT-A-FAMILY-KILL / NOT-SP2 / NOT-JC2
```

## 1. Exact staged data

The calculation preserves the source-valid dependency order:

```text
raw 3,602-column transport -> 132 variables
original first-band rows   -> 94 variables
genuine quadratic P12      -> exact first-ideal remainder
```

It does not form the rejected all-at-once affine `110x132` system.  The exact
inventories are:

| object | exact value |
|---|---:|
| transport rank | `3470/3602` |
| first-band rank | `38/132` |
| previous/pole rank, used only as a cross-check | `38/94` |
| raw `P12` parameter degree | `2` |
| raw `P12` terms | `2,893` |
| raw `P12` digest | `2143578afd38c2f4fa0881da907999928c80dbda6c957a54a7d5a25a647083fe` |
| nonzero original first rows in the lift | `28` |
| multiplier terms | `1,489` |
| full lifted-identity digest | `31b56241f6edb79932af8ddb8b376ffc7727eea037abf741c5998867eea1ae69` |
| `D(C)` digest | `d533ae90a8c8aea5c68bb069555c26e24ec9f482032ef51ba09b8924ac25bfc2` |
| `-(k/50)D(C)` digest | `cebbda8b2101b96ff2d29cc96a168cfe04ec195f1ad7b3256ceb79df2a269fa9` |

The replay first proves the same constant remainder after the licensed
previous/pole stage.  That secondary identity covers every previous/pole
pivot root and is retained as an internal consistency check; the theorem
above uses the stronger lift through the original first-band ideal and needs
no previous/pole equation.

## 2. Why the exceptional set is exactly `J=0`

The generic transport echelon has exceptional divisor `C(C-3)`.  The cleared
first-ideal coefficient factors exactly as

```text
D = (C-3)^2 * (4*C^2+20*C+1) / 4.
```

The eight distinct nonconstant first-pivot numerators have gcd `1` with the
cleared right side except for the factors `C-3` and
`(C-3)(4*C^2+20*C+1)`.  Because the final multipliers lie in `E[C]` after
clearing first-stage denominators, the displayed identity specializes at
first-rank-jump values; it is not merely a point sample or a generic-rank
argument.  On `C(C-3) != 0`, its right side is a nonzero unit unless `J=0`.

The sibling case `cases/td6_c1_raw_transport_fibres_20260824/` rebuilds the
original transport and first rows at `C=0` and `C=3` and proves both fibres
empty.  Therefore the dependency-complete successor is a raw exact rebuild
over `E[C]/(J)`, not a list of sampled algebraic roots.

## 3. Unit check

The exact inverse used for the obstruction is

\[
\begin{aligned}
k^{-1}={}&-{388\over175625}S^5+{738\over35125}S^4
-{9181\over105375}S^3+{40993\over210750}S^2\\
&-{4948\over21075}S+{66812\over526875}.
\end{aligned}
\]

Reduction modulo the frozen degree-six polynomial for `S` gives
`k*k^{-1}=1` exactly.  Thus `-k/50` remains nonzero over every extension of
`E`; no numerical embedding or root choice is involved.

## 4. Scope

Established here:

- the source-valid first-stage polynomial-ideal identity on the generic
  transport chart;
- coverage of all generic-transport `c1` values outside `J=0`;
- exact isolation of the sole remaining quadratic stratum after combining
  with the separately frozen `C=0,3` theorem.

Not established here:

- emptiness of `J=0`;
- a statement uniform in the other center, boundary, dead-stretch, F1, or
  pole moduli;
- an SP-2, terminal-class, or JC2 conclusion.

The normalized-section transversality and source-typing caveats from the
frozen centering-tangent report remain in force.

## 5. Deterministic replay

Case directory: `cases/td6_c1_first_stage_ideal_20260824/`.

```sh
/opt/homebrew/bin/python3 cases/td6_c1_first_stage_ideal_20260824/replay.py \
  > /tmp/td6-c1-first-stage.stdout
cmp /tmp/td6-c1-first-stage.stdout \
  cases/td6_c1_first_stage_ideal_20260824/replay.stdout
shasum -a 256 -c \
  cases/td6_c1_first_stage_ideal_20260824/MANIFEST.sha256
cmp cases/td6_c1_first_stage_ideal_20260824/MANIFEST.sha256 \
  cases/td6_c1_first_stage_ideal_20260824/FREEZE.sha256
```

The replay uses exact FLINT-backed rational functions and the frozen exact
tower field only.  It performs no floating-point calculation, interpolation,
sampled-root inference, AWS job, or cached singular specialization.

**Quarantine:** the certificate emits `family_killed=false`,
`SP2_killed=false`, and `JC2_resolved=false`.
