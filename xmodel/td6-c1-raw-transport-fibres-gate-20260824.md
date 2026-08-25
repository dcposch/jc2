# TD6-C1-RAW-TRANSPORT-FIBRES — the two transport-exceptional center fibres are empty

Date: 2026-08-24  
Status: **EXACT PRODUCER / ADAPTIVE RAW-FIBRE THEOREM / STOP**

## Verdict

In the frozen normalized TD6 control with

\[
 (c_1,c_2,c_3)=(C,1,1),\qquad p=t^{15},\qquad q=t+t^{25},
\]

the generic two-chart transport echelon has exceptional divisor
`C(C-3)`.  Rebuilding the original 3,602-column transport system at both
fibres, rather than evaluating a singular generic parameterization, gives

```text
C=0: transport 3470/3602, first band 38/132, current t12 = -k/50 != 0
C=3: transport 3470/3602, first band 38/132, current t12 = -k/50 != 0
```

where

\[
 k=252-342S+144S^2-36S^3.
\]

Thus both raw transport-exceptional fibres are empty in this fixed normalized
section.  The calculation uses no previous/pole or current-band
parameterization.  It retains the genuine quadratic current `t^12`
polynomial and reduces it through an adaptively rebuilt first-band echelon.

```text
TD6-C1-C0-C3-EMPTY / RAW-TRANSPORT-REBUILT /
FULL-FIRST-ROW-POLYNOMIAL-CERTIFICATES / NOT-A-FAMILY-KILL
```

This is not an SP-2, terminal-class, or JC2 conclusion.

## 1. Exact adaptive ranks

The replay specializes the common center before any elimination and rebuilds
both global transport charts from their original rows.  Each fibre has exact
rank `3470/3602`, zero dependent-row compatibility, and 132 affine transport
parameters.  The selected adaptive transport-minor digests are:

| fibre | selected-minor digest |
|---|---|
| `C=0` | `3349b4fba349972a0170e27007cbfe35a1dfe11683b352d8c906459f01e2477a` |
| `C=3` | `be8c39325d598716e800459c91334c015cf8995d83da90b7fb2daed477940036` |

On each adaptive transport chart the first centered Jacobian system is
consistent of rank `38/132`.  This rank is also rebuilt after specialization;
no generic first-stage pivot list is evaluated at either fibre.

## 2. Genuine current polynomial and exact reduction

Before the first equations are imposed, the current `t^12` equation is a
genuine degree-two polynomial in the 132 adaptive transport parameters:

| fibre | terms | raw-polynomial digest |
|---|---:|---|
| `C=0` | 2,824 | `be8e80ffa067a37b30418361812656405ef843a0fa5398766f12268dd1de55a1` |
| `C=3` | 2,885 | `1bd39dc9756dd7e83c17ab04a0ccfd2655514a5a42f593eac80df88ce8a18275` |

The replay performs exact multivariate division by the normalized adaptive
first-band echelon and simultaneously lifts every quotient multiplier to the
original 38 first-band rows.  It then replays, coefficient by coefficient,
the identity

\[
 P_{12}= -{k\over 50}+\sum_i M_i L_i,
\]

where `P12` is the raw current polynomial, the `L_i` are original first-band
rows, and the `M_i` are emitted parameter polynomials.  The complete
certificate inventories are:

| fibre | nonzero original rows | multiplier terms | full relation digest |
|---|---:|---:|---|
| `C=0` | 28 | 1,423 | `3c44f2dc21490bed6b402ea89a3653dade1fbd7f81c6cc4fa311a11bd31115e7` |
| `C=3` | 28 | 1,515 | `617017b265be79efafbc155fa002f9e7597070e3e2623ade5fdd88deabca5581` |

Every monomial and exact coefficient of both original-row certificates is in
`replay.stdout`; the replay reconstructs and checks the identity before
printing it.  The reduced one-term polynomial has digest
`233c0ce8f90585ed8da5085cd33f178f5c0e2300d87e4a44b4deeb9eb06644c7`
at both fibres.

## 3. Why the constant is a contradiction

The imported exact coefficient presentation is the degree-18 field
`E=K[A]/(A^3-alpha)`, with

\[
 K=\mathbf Q[S]/(24S^6-252S^5+1170S^4-3045S^3
                  +4680S^2-4032S+1411).
\]

The whole-`B` producer and independent review already certified

\[
\begin{aligned}
k^{-1}={}&-{388\over175625}S^5+{738\over35125}S^4
-{9181\over105375}S^3+{40993\over210750}S^2\\
&-{4948\over21075}S+{66812\over526875}.
\end{aligned}
\]

Consequently `-k/50` is a nonzero unit over `E` and over every field
extension of `E`.  A point satisfying all first-band rows would make the
right-hand sum vanish; imposing the current `t^12` row would then force this
unit to vanish, which is impossible.

## 4. Scope and remaining gate

What is proved is exactly the emptiness of the two fibres `C=0` and `C=3`,
the only exceptional fibres of the generic **transport** echelon for this
one-parameter common-centering line.

What is not proved here:

- coverage of the nontransport exceptional roots of the generic first-band
  echelon;
- emptiness of the whole `c1` line;
- a statement uniform in the other center, boundary, dead-stretch, F1, or
  pole moduli;
- an SP-2, terminal-class, or JC2 decision.

The running source-valid successor lifts the same `t^12` identity over
`E[C]` through the generic first-band ideal.  Until its denominator-cleared
identity covers every first-stage pivot root, the line-family claim remains
quarantined.

## 5. Reproducibility

Case directory: `cases/td6_c1_raw_transport_fibres_20260824/`.

```sh
/opt/homebrew/bin/python3 cases/td6_c1_raw_transport_fibres_20260824/replay.py 0 3 \
  > /tmp/td6-c1-raw-fibres.stdout
cmp /tmp/td6-c1-raw-fibres.stdout \
  cases/td6_c1_raw_transport_fibres_20260824/replay.stdout
shasum -a 256 -c cases/td6_c1_raw_transport_fibres_20260824/MANIFEST.sha256
cmp cases/td6_c1_raw_transport_fibres_20260824/MANIFEST.sha256 \
  cases/td6_c1_raw_transport_fibres_20260824/FREEZE.sha256
```

The replay uses exact FLINT-backed rational functions and the exact tower
field only.  There is no floating-point embedding, interpolation, sampled
parameter value beyond the two theorem fibres themselves, AWS job, or cached
generic later-stage parameterization.

**Quarantine:** `family_killed=false`, `SP2_killed=false`, and
`JC2_resolved=false` are emitted by the certificate.
