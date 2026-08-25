# TD6-C1-LINE-KILL — the licensed common-centering line is empty

Date: 2026-08-24  
Status: **EXACT PRODUCER / SCOPED ONE-PARAMETER FAMILY THEOREM / NOT SP-2**

## Verdict

In the frozen normalized TD6 control

\[
(c_1,c_2,c_3)=(C,1,1),\qquad p=t^{15},\qquad q=t+t^{25},
\]

there is no solution for any `C` over any field extension of the exact
coefficient field `E`.

The proof is an exact dependency-complete cover of the parameter line:

| stratum | source-valid certificate | conclusion |
|---|---|---|
| `C=0` | raw 3,602-column transport and adaptive first rebuild | empty |
| `C=3` | raw 3,602-column transport and adaptive first rebuild | empty |
| `C(C-3) != 0`, `J(C) != 0` | localized first-ideal identity over `E[C]` | empty |
| `J(C)=4C^2+20C+1=0` | raw transport and adaptive first rebuild over `E[C]/(J)` | empty |

In every stratum, the contradiction is the same parameter-free current
obstruction

\[
-{k\over50},\qquad k=252-342S+144S^2-36S^3\ne0.
\]

```text
TD6-C1-LINE-EMPTY / EXACT STRATUM COVER /
FIXED NORMALIZED SECTION ONLY / NOT-SP2 / NOT-JC2
```

This kills one licensed transverse common-centering family.  It does not
kill TD6, SP-2, a terminal class, or JC2, and it does not cover simultaneous
variation of other center, boundary, dead-stretch, F1, or pole moduli.

## 1. Generic complement

The source-valid generic calculation retains the current `t^12` row as its
genuine degree-two polynomial in all 132 transport-free parameters.  Exact
division through the original first-band ideal gives

\[
D(C)P_{12}=-{k\over50}D(C)+\sum_iM_iL_i,
\]

with

\[
D(C)={1\over4}(C-3)^2J(C),\qquad J(C)=4C^2+20C+1.
\]

The lift uses 28 original first rows and 1,489 multiplier terms; its full
identity digest is
`31b56241f6edb79932af8ddb8b376ffc7727eea037abf741c5998867eea1ae69`.
Because its cleared multipliers are polynomial in `C`, this identity covers
first-rank jumps as well as generic first rank.  On the transport chart
`C(C-3) != 0`, only `J=0` remains after the unit obstruction is imposed.

The exact generic certificate and all pivot gcds are frozen separately in
`cases/td6_c1_first_stage_ideal_20260824/` and reported in
`xmodel/td6-c1-first-stage-localized-gate-20260824.md`.

## 2. Raw transport-exception fibres

At `C=0` and `C=3`, the generic transport parameterization is not evaluated.
Each original 3,602-column transport system is rebuilt after specialization;
each has exact rank `3470`, zero transport compatibility, and 132 free
variables.  An adaptive first-band rebuild has exact rank `38`, and the
genuine current polynomial reduces through a full original-row certificate
to `-k/50`.

These two certificates are frozen in
`cases/td6_c1_raw_transport_fibres_20260824/` and reported in
`xmodel/td6-c1-raw-transport-fibres-gate-20260824.md`.

## 3. Exact quadratic-stratum rebuild

The final stratum is handled without choosing, approximating, or sampling a
root of `J`.  The replay specializes the original transport rows to the
exact quotient by `J`, then performs a fresh adaptive elimination.

| object | exact result |
|---|---:|
| raw transport rank | `3470/3602` |
| transport compatibility | `0` |
| transport free variables | `132` |
| transport elimination digest | `affda5d3acb1a1cf32f42e14486293e10b66a0c449bfded6ebaaf345c7629350` |
| adaptive first rank | `38/132` |
| first incompatibility | `0` |
| exactly Bezout-checked first inverses | `38` |
| raw `P12` terms / degree | `2,893 / 2` |
| raw `P12` digest | `107615b4ba98ceaf2afe14ffa41ab82e91326a6d04f13c19b6d62593cff919c1` |
| nonzero original first rows | `28` |
| multiplier terms | `1,530` |
| full source-relation digest | `009b97df434fb59df17d954f4b8905364b9a7de9d970b0e4bbf068591544a8b3` |
| reduced `P12` digest | `a72003a48fbbbe567ea26705510aa7d41683749057d3a493f85f6573c5d60881` |

The final exact identity is

\[
P_{12}=-{k\over50}+\sum_iM_iL_i
\quad\text{in}\quad E[C]/(J)[\mathbf u].
\]

The replay does **not** assume that `J` remains irreducible over `E`.  Every
element inverted during the first-band elimination comes with an exact
Bezout inverse modulo `J`; all 38 such inverses are replayed by multiplication
in the quotient.  Consequently the identity remains valid if the quotient
splits, and it covers every geometric point above `J=0`.

## 4. Nonzero-unit certificate

The replay verifies

\[
\begin{aligned}
k^{-1}={}&-{388\over175625}S^5+{738\over35125}S^4
-{9181\over105375}S^3+{40993\over210750}S^2\\
&-{4948\over21075}S+{66812\over526875},
\end{aligned}
\]

and checks `k*k^{-1}=1` exactly before accepting the quotient-stratum
certificate.  Hence `-k/50` is a unit after every scalar extension.

## 5. Scope and provenance

The theorem is confined to the frozen normalized TD6 source typing and the
one-parameter section `(C,1,1)`.  In particular:

- it makes no claim about a simultaneous two- or three-center block;
- it makes no claim about q-boundary, p-boundary, dead-stretch, pole-scale,
  or F1-orbit moduli;
- the normalized-section transversality and target-shear caveats from the
  reviewed centering-tangent package remain active;
- it uses no previous/pole or current-band parameterization in any raw
  exceptional rebuild;
- it makes no SP-2 or JC2 inference.

The invalid all-at-once affine `110x132` model is not used.  All nonlinear
current rows remain genuine polynomials until reduced through a licensed
linear ideal.

## 6. Deterministic replay

Quadratic-stratum case:
`cases/td6_c1_quadratic_stratum_20260824/`.

```sh
/opt/homebrew/bin/python3 cases/td6_c1_quadratic_stratum_20260824/replay.py \
  > /tmp/td6-c1-J.stdout
cmp /tmp/td6-c1-J.stdout \
  cases/td6_c1_quadratic_stratum_20260824/replay.stdout
shasum -a 256 -c \
  cases/td6_c1_quadratic_stratum_20260824/MANIFEST.sha256
cmp cases/td6_c1_quadratic_stratum_20260824/MANIFEST.sha256 \
  cases/td6_c1_quadratic_stratum_20260824/FREEZE.sha256
```

The two companion manifests separately freeze the generic-complement and
`C=0,3` certificates.  All three replays are deterministic and exact.  They
use no floating point, interpolation, sampled algebraic root, AWS job, or
unrebuilt singular parameterization.

**Quarantine:** `family_killed` in the machine output is `false` because the
quadratic replay alone is only one stratum.  The scoped line-family theorem is
the exact logical union of the three separately frozen certificates above;
`SP2_killed=false` and `JC2_resolved=false` throughout.
