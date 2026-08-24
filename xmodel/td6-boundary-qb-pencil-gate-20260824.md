# TD6-QB-PENCIL — the licensed q2 boundary family is empty

Date: 2026-08-24  
Producer basis: `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`  
Status: **EXACT PRODUCER / SCOPED ONE-PARAMETER FAMILY KILL / STOP**

## Verdict

At the degree-18 sextic points of the frozen normalized SP-2 control, retain
the licensed transverse boundary family

\[
  p(t)=t^{15},\qquad q_B(t)=t+B t^2+t^{25}.
\]

The complete staged system through the current centered band has no solution
for any `B`, even after extending the exact residue field.  Exact elimination
over the untruncated polynomial ring `E[B]` has globally constant ranks

\[
3470/3602\longrightarrow 38/132\longrightarrow 38/94
\longrightarrow 25/56.
\]

All `38+38+25=101` normalized leads are nonzero constants in `E`.  Hence the
pivot exceptional polynomial is `1`: there is no rank-jump or denominator
stratum to specialize.  Ten exact left-null compatibilities occur at centered
degrees `t^4,...,t^13`.  Two suffice:

\[
\begin{aligned}
N_4(B)={}&\rho-{4720\over29}B+{11364\over145}B^2
             -{4096\over145}B^3+16B^4,\\
N_{13}(B)={}&{252-342S+144S^2-36S^3\over25}\,B,
\end{aligned}                                                    \tag{1}
\]

where

\[
\rho={2495634-4154976S+4405068S^2-2488119S^3+761922S^4-105084S^5\over3625}
     +{136875\over29}A.                                         \tag{2}
\]

The coefficient of `B` in `N_13` is a unit.  Thus `N_13=0` forces `B=0`,
whereas `N_4(0)=rho` is nonzero.  The replay also verifies an explicit
Bezout identity between `N_4` and `N_13`, so their gcd is `1` over `E[B]`.
Consequently no quartic-root stratum survives to rebuild.

The exact verdict is

```text
TD6-QB-LICENSED-FAMILY-EMPTY / PIVOT-EXCEPTIONAL-PRODUCT-ONE /
EXACT-E[B]-BEZOUT / NOT-SP2 / NOT-JC2
```

This kills only the one-dimensional `q2` boundary pencil in the fixed
normalized section.  It does not kill the full SP-2 ansatz, the centering or
dead-stretch pencils, or JC2.

## 1. Frozen scope and quotient caveat

This gate is the exact successor to `TD6-JET-ORBIT-ADJOINT`.  It retains the
same rectangles, three charts, degree-18 field, pole normalization, dead
stretch, and centered source data.  In particular,

\[
E=\mathbb Q[S,A]/(F(S),A^3-9/L^8),\qquad
L=25(1-S+D),
\]

with the frozen sextic `F` and `D=(2S^2-2S+3)/5`.

The predecessor source audit remains essential.  Under
`t -> t + epsilon*t^2`, the full source-coordinate tangent is

\[
(\delta T,\delta p,\delta q)
=(t^2,15t^{16},t^2+25t^{26}),
\]

not the q2-only vector.  After the registered linear-chart section and
`p=t^15`, the q2-only vector raises the truncated orbit rank by one and is a
genuine transverse class.  Target translations, reciprocal scaling, and the
lower shear are gauge-zero controls; the normalized `(S,D,L,A)` tangent is
rigid of rank `4/4`.  Common centering and dead-stretch coefficients are
licensed but frozen here, not silently quotiented out.  Therefore the present
conclusion is exactly a kill of the smallest transverse q-boundary pencil,
not a statement about every normalized source deformation.

## 2. Exact staged polynomial elimination

The transport matrix is independent of `B`; only its right-hand side changes,
affinely.  Its frozen rank-3470 echelon gives 132 rational homogeneous
directions and an affine particular response.  A portable cache retains only
the x-band and pole sections consumed downstream.  The cache is not trusted
as an oracle: `build_transport_cache.py` reconstructs it from the raw
3,602-column transport equations and requires byte-for-byte equality with the
canonical JSON.

The fast replay then performs normalized elimination directly in `E[B]`.
No Taylor truncation, numerical evaluation, interpolation, or finite-field
lifting occurs.  The observed and certified degree bounds are:

| object | constant/RHS degree | direction/matrix-entry degree |
|---|---:|---:|
| cached transport sections | `<=1` | `0` |
| first-J input rows | `<=1` | `<=1` |
| 94-parameter forms | `<=1` | `0` |
| previous centered + pole rows | `<=1` | `<=1` |
| 56-parameter forms | `<=1` | `0` |
| current centered input rows | `<=1` | `<=1` |

Every normalized lead is asserted to have B-degree zero before inversion.
After all leads are removed, every dependent homogeneous row is asserted to
be the zero polynomial row.  Thus a hidden B-only pivot cannot be discarded:
it would stop the replay.  The first and previous/pole affine
parameterizations are substituted back into every original equation and
checked coefficientwise in all free parameters.

At the current band the elimination continues past the first affine
contradiction to the full homogeneous rank `25/56`.  Each of the ten
compatibilities is accompanied by an exact polynomial left-null combination
and is replayed directly against the original current rows.  Their numerator
digests are:

| row | degree | numerator SHA-256 |
|---|---:|---|
| `t4` | 4 | `dd5c7e694153beebb9ae0f08408c7b2e8a209b9671a76ad20ba66cb601b8d1ad` |
| `t5` | 4 | `62b5c40223c0b422a987d5074e842e23b7f9bb32a94088e0d21cfecc65c560ac` |
| `t6` | 4 | `f25765d7afaed5d81ec7bb222207a6756fa54364cc56152b6786c5b29db557a9` |
| `t7` | 4 | `105cb1ff3db5d6e36e9a094ff745c481b05a57b541ee12929c2a4b3dc493f062` |
| `t8` | 4 | `e3a7083f0df52cecdd8e1ff51b61de85e262a2b53cfd110f5215dbe0f201f402` |
| `t9` | 4 | `936ee036c2396784e7d24bbc2a50b9540c91c6e14f24d6831c923b51ab5387cd` |
| `t10` | 4 | `314b6a7a8f81e1ac28270ab04afabe8d1beb89dca3fb3d07d1bb4248f02d2e15` |
| `t11` | 4 | `10b3cf44d8794f83dbd2da9efb497bf656a9c1a358f7d34e1dbe8f80b9d9c5b0` |
| `t12` | 4 | `39ea7593593901fd25eb6902bc858fef0d09f835858cff062c05aae0348a4c59` |
| `t13` | 1 | `49760d07f6b8527c6eee74a8f825413fb5fd83bfb832427602906a37cace6ea3` |

The `t4` syzygy has support four and weight degree at most three; its replay
digest is
`3f6bf56c0ae16e05f04395fb3f3a5a340e5af3d170324a636ad0665373ebe149`.
The `t13` row is itself a parameter-free compatibility (support one, constant
weight), with digest
`e11690963661a8c978cdc4ef8741d4a242c5a7038a2e2402701209a911f8ffc3`.

## 3. Unit, Bezout, and exceptional-stratum certificates

Write

\[
k=252-342S+144S^2-36S^3.
\]

For the frozen sextic

\[
F=24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411,
\]

the replay verifies `gcd(F,k)=1` by checking the normalized inverse

\[
k^{-1}=-{388\over175625}S^5+{738\over35125}S^4
-{9181\over105375}S^3+{40993\over210750}S^2
-{4948\over21075}S+{66812\over526875}.             \tag{3}
\]

The inverse of `k/25` is `25*k^{-1}` and its product is exactly one in `K`.
Its digest is
`fd2476104889d51b5ddbc8adbfeb45764bf89fb9c13210319fdbf1ef33959d63`.

Let `N4=rho+B*h` and `N13=(k/25)B`.  The replay checks

\[
 {1\over\rho}N_4-{25h\over\rho k}N_{13}=1.          \tag{4}
\]

The identity digest is
`159c3b52a498e3f762545750bdfbf7e53675172264f51fe92ce70668bc46104d`;
the monic compatibility gcd is exactly `1`, digest
`832a8a790c1b7572ef7f3796644b3a6cb4c68225283f6e671494e23692ba68ef`.

There are consequently no unresolved strata:

- transport rank is constant;
- all 101 downstream pivot factors are units independent of `B`;
- the pivot exceptional product is `1`;
- the compatibility ideal is the unit ideal.

In particular, roots of the quartic `N4` are not candidate survivors: every
one has `N13 != 0` because it is nonzero, while `B=0` has `N4 != 0`.

## 4. Adjoint consistency

The coefficient of `B` in `N4` is exactly `-4720/29`, reproducing the frozen
dual-adjoint derivative that included the varying normalized syzygy
(`lambda'`).  At `B=1`, the higher coefficients sum to the frozen point
secant

\[
N_4(1)-N_4(0)=-{14012\over145}.
\]

The present untruncated polynomial left-null replay is the stronger
equivalent exact solve: it retains the complete B-dependence of the syzygy,
not only `lambda'` at zero.

## 5. Replay and provenance

From the repository root:

```bash
python3 cases/td6_boundary_qb_pencil_20260824/build_transport_cache.py
python3 cases/td6_boundary_qb_pencil_20260824/replay.py
```

The first command is the slow provenance check: it rebuilds the frozen
transport echelon/response and verifies the canonical cache byte-for-byte.
The second is the fast exact `E[B]` proof and emits all 101 pivot factors,
all ten compatibility polynomials and left-null digests, the unit inverse,
gcd, and Bezout identity.  `MANIFEST.sha256` and `FREEZE.sha256` pin every
producer file and this report.

## 6. Immediate successor

There is no B-root branch to pursue.  The next licensed TD6 work should move
to the smallest matrix-changing transverse jets omitted from this section:
common centering first, then dead-stretch coefficients in first-entering-order
blocks, always quotienting the full source reparametrization and target gauge
directions.  The same nonblocking pattern applies: provisional exact pencils
can feed successors while adversarial review runs in the background.
