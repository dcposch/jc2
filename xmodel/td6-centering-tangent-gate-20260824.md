# TD6-CENTERING-TANGENT-GATE — the full current cokernel sees all three centers

Date: 2026-08-24  
Status: **EXACT PRODUCER / FULL-COKERNEL FIRST-ORDER GATE / STOP**

## Verdict

In the frozen normalized TD6 control, the three common center jets

\[
 y=s^{-1},\qquad
 x=c_1s+c_2s^2+c_3s^3+t s^4
\]

are transverse to the reviewed regular source-reparametrization and
rectangle-preserving target gauges at `(c1,c2,c3)=(1,1,1)`.  Exact
simultaneous differentiation of the matrix-changing transport system, both
later parameterizations, and every current-band left-null compatibility gives
an injective map

\[
 D\mathcal C:E^3\longrightarrow E^{10},\qquad
 \operatorname{rank}_E D\mathcal C=3.
\]

There is no nonzero common centering direction with vanishing full adjoint
image.  The affine linearized cancellation equation
`D C(v)=-C(1,1,1)` is also inconsistent.  Every displayed base rank is stable
to first order.

This does **not** kill a center family.  The base normalized control is already
inconsistent, so the derivative is sensitivity information, not a tangent
space at a solution.  Nonlinear roots away from the base point remain open.
The licensed successor is an exact one-parameter matrix pencil; the sparsest
choice after the zero-kernel result is `c1=C`, `c2=c3=1`.

```text
CENTERING-TRANSVERSE / FULL-COKERNEL-INJECTIVE /
NO-COMMON-LINEARIZED-ROOT / C1-PENCIL-LICENSED
```

No SP-2 class, terminal class, or instance of JC2 is killed or realized.

## 1. Frozen scope and quotient typing

The replay imports by hash the reviewed TD6 jet/orbit adjoint compiler and
thereby retains the exact rectangles, boundary pair `p=t^15`,
`q=t+t^25`, F1 orbit point, zero dead stretch, pole normalization, sextic,
and degree-18 coefficient field `E` of the whole-`B` gate.

| frozen dependency | SHA-256 |
|---|---|
| `cases/td6_jet_orbit_adjoint_20260824/replay.py` | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md` | `2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9` |
| whole-`B` producer report | `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22` |
| whole-`B` different-model review | `5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319` |

At fixed registered global coordinates `(x,y)`, `y=s^-1` pins `s`.  Varying
the center while preserving `x` requires the complete chart tangent

\[
 \delta t=-\delta c_1s^{-3}-\delta c_2s^{-2}-\delta c_3s^{-1}.       \tag{1}
\]

A regular truncated source reparametrization has `delta t` in `E[[s,t]]`, so
its `s`-support is nonnegative and cannot meet the three Laurent monomials in
(1).  The boundary section gives the same conclusion independently:
`q'(t)=1+25t^24` is a unit, hence a regular reparametrization preserving
`delta q=0` has zero parameter tangent.

The complete rectangle-preserving determinant-one target list in the fixed
degree ordering consists of the two translations, reciprocal scaling, and
the lower shear `g -> g+epsilon f`.  Its rank is four, its center projection
is zero, and its Jacobian sensitivity is zero.  The previously reviewed
`(S,D,L,A)` source matrix has rank `4/4`, so no frozen F1/pole motion silently
compensates a center motion.

Thus the center quotient rank is three **in this registered normalized
section**.  This qualifier matters: a new global-domain normalization that
changes the other charts or the fixed rectangles is not being declared a
residual gauge.  Any later enlargement of that equivalence relation must
redo the quotient rather than import this rank.

## 2. Matrix-aware differentiated transport

Changing a center changes the 3,602-column transport matrix.  The replay does
not reuse a stale particular solution.  For each of `dc1,dc2,dc3` it solves

\[
 A_0\,\delta x=-\delta A\,x_0                                      \tag{2}
\]

against the frozen rank-3,470 echelon, checks every differentiated dependent
transport row, and retains the same 132 homogeneous coordinates.  The pulled
back x bands include both the variation of the global coefficients from (2)
and the direct variation of the chart row.

The exact ranks are:

| stage | rank | remaining dimension | derivative-only rank flag |
|---|---:|---:|---:|
| two-chart transport | `3470/3602` | 132 | 0 in all 3 directions |
| first centered Jacobian | `38/132` | 94 | 0 in all 3 directions |
| previous centered + inherited pole | `38/94` | 56 | 0 in all 3 directions |
| current homogeneous system | `25/56` | 31 | 0 in all 3 directions |

The first affine contradiction is again current row `t^4`, after three
current pivots.  Its base value is

\[
\begin{aligned}
\rho={1\over3625}(&2495634-4154976S+4405068S^2-2488119S^3\\
                  &+761922S^4-105084S^5)+{136875\over29}A.
\end{aligned}
\]

The exact coordinate sensitivities of this first residue are all nonzero:

```text
dc1 sha256 23afdddfcea7985ec8764c34bd5f0293f7f7f2d33a6cb7683bad5554fe09fcd1
dc2 sha256 0848e6c9a543de1600f67411fd0867ba1cca76cbbce22ace7aa2eadeb8218b92
dc3 sha256 6a65174bab17999e5ce229937e9a2d22b75a538fa32663e7d973c40e08596ec4
```

The normalized left-null vector for this row has support four and is itself
differentiated.  Thus the calculation includes the `lambda'` contribution,
not merely `lambda_0(delta b-delta A x_0)`.  Its three-direction digest is
`694e5af799f24d2ba7dc311de52322732fca11ac7ad6ff790b4e9de7b233c565`.

## 3. Full cokernel, not one sampled obstruction

The current system has 35 rows and homogeneous rank 25, hence ten exact
dependent compatibilities.  Reducing all ten against the same varying
echelon gives the joint map above.  The replay certifies:

```text
current compatibility dimension = 10
rank_E(D C) = 3
kernel dimension = 0
rank_E([D C | -C_0]) = 4
common affine linearized root = false
```

An explicit nonzero `3 x 3` sensitivity minor and nonzero augmented `4 x 4`
minor are printed in the canonical stdout, together with their source rows,
exact `E` values, and hashes.  The full ten-row multidual compatibility digest
is `8fc63678526c16182a2eb8b318b1a41de3983c6d467ae4942137ef2361117d26`.

This full reduction corrects a misleading intermediate impression: the one
functional `t^4` has an automatic two-dimensional kernel over `E`, but the
intersection of the kernels of all ten compatibility functionals is zero.
No direction should be selected from the single-row kernel.

## 4. Meaning and successor

What is proved is narrowly first order:

- all three licensed common-center jets are seen by the full current
  compatibility vector at the chosen normalized control;
- no rank jump occurs to first order in the staged matrices;
- no single infinitesimal center step cancels the complete base residue
  vector in its affine linearization.

What is not proved:

- emptiness of any positive-dimensional center family;
- absence of a nonlinear root at another center;
- a statement uniform in boundary, dead-stretch, F1, or pole moduli;
- an SP-2, terminal-class, or JC2 decision.

The next exact experiment is the line

\[
 (c_1,c_2,c_3)=(C,1,1).
\]

It must factor the genuinely changing transport matrix over `Q(C)`, carry the
affine solve into the small `E(C)` stages, record every pivot numerator and
denominator, and rebuild every exceptional specialization before any family
claim.  Certified symbolic identities are required; interpolation alone is
not licensed without a proved degree bound and deterministic identity replay.

## 5. Reproducibility and quarantine

Case directory: `cases/td6_centering_tangent_20260824/`.

```sh
python3 cases/td6_centering_tangent_20260824/orbit_audit.py
python3 cases/td6_centering_tangent_20260824/replay.py
sha256sum -c cases/td6_centering_tangent_20260824/MANIFEST.sha256
cmp cases/td6_centering_tangent_20260824/MANIFEST.sha256 \
    cases/td6_centering_tangent_20260824/FREEZE.sha256
```

Both programs use exact rational/finite-extension arithmetic.  The replay
pins its imported producer by SHA-256 and emits deterministic certificate
hashes.  No AWS job, floating-point embedding, or point interpolation enters
this gate.

**Quarantine:** `centering_family_killed=false`, `SP2_killed=false`, and
`JC2_resolved=false` are hard-coded and replayed.
