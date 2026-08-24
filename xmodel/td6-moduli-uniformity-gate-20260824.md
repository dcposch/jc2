# TD6-MODULI-UNIFORMITY-GATE — generic obstruction and complex survivor

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **PROVISIONAL PRODUCER / EXACT FORMULA / SURVIVOR / STOP**

## Verdict

The numerical obstruction in `td6-two-chart-next-row-20260824.md` extends to
an exact centering-independent formula.  Let the reduced case-II(a) F1
polynomial be

\[
 R(z)=(z-C)^2(z-U)(z-V)
      =z^4-E_1z^3+E_2z^2-\cdots,
\]

where

\[
 E_1=2C+U+V,
 \qquad E_2=C^2+2C(U+V)+UV.
\]

For every first-band solution in the fixed SP-2 rectangles and with the
frozen x-boundary normalization, regardless of the licensed common centering
`c1,c2,c3` and regardless of all pole-side parameters,

\[
 \boxed{
 [s^{-1}t^{13}]J(f,g)={6\over5}\left(5E_2-2E_1^2\right).
 }
 \tag{1}
\]

Thus the obstruction is Zariski-generic and has no parameter denominator or
centering rank caveat.  It does **not**, however, kill SP-2: the complex
hypersurface

\[
 5E_2-2E_1^2=0                         \tag{2}
\]

contains source-typed points.  On a fully specified normalized slice, the
complete first-band transport plus **both** next Jacobian rows is exactly
nonempty on (2), with affine dimension `56`.  The correct verdict is therefore
`GENERIC-OBSTRUCTION / COMPLEX-SURVIVOR`, not a terminal-class kill.

## 1. Hypotheses and scope of the formula

The fixed global rectangles remain

\[
 f:\ 0\le i\le15,\ 0\le j\le60,
 \qquad
 g:\ 0\le i\le25,\ 0\le j\le100.
\]

At the x end use the arbitrary common centered chart

\[
 y=s^{-1},\qquad
 x=c_1s+c_2s^2+c_3s^3+t s^4,          \tag{3}
\]

with the same normalized boundary values

\[
 [s^0]f=t^{15},\qquad [s^0]g=t+t^{25},
 \qquad [s^{-2}]J=0.                  \tag{4}
\]

At F1 use `x=q^-5`, `y=eta q` and the monic leading patterns

\[
 q^{15}f=R(\eta^5)^3+O(q),
 \qquad
 q^{25}g=R(\eta^5)^5+O(q).            \tag{5}
\]

The source-typing open set has `C,U,V` nonzero and pairwise distinct in the
sense that the squared chain orbit `C` is distinct from the two simple extra
orbits and the two extra orbits are distinct.

Formula (1) is conditional only on the existence of a pair meeting (3)--(5)
and the first Jacobian row.  It makes no pole-chart assumption.  Consequently
it is automatically uniform in the r9 pole parameter, intervening
dead-stretch coefficients, and any later local jets.  The full survivor
certificate in sections 4--5 makes one licensed pole/dead-stretch
specialization in order to prove that the zero locus is genuine.

This gate still retains the normalized x-boundary polynomials in (4).  It
does not quantify any more general x-direction polynomial that may be
licensed in a broader SP-2 realization.

## 2. Coefficient proof and centering independence

Write

\[
 F=f\bigl(c_1s+c_2s^2+c_3s^3+ts^4,s^{-1}\bigr)
   =t^{15}+sf_1(t)+s^2f_2(t)+\cdots,
\]

and similarly

\[
 G=t+t^{25}+sg_1(t)+s^2g_2(t)+\cdots.
\]

The F1 leading line for a monomial `x^i y^j` is

\[
 j-5i=-15\quad(f),
 \qquad j-5i=-25\quad(g),             \tag{6}
\]

and all coefficients on stricter pole diagonals vanish.

There are three relevant coefficient extractions:

\[
\begin{aligned}
 [t^{14}]f_1
   &=a_{14,55}=[z^{11}]R^3=-3E_1,\\
 [t^{24}]g_1
   &=b_{24,95}=[z^{19}]R^5=-5E_1,\\
 [t^{13}]f_2
   &=a_{13,50}=[z^{10}]R^3
     =3E_2+3E_1^2.                    \tag{7}
\end{aligned}

For each extraction, every possible contribution involving at least one of
`c1 s,c2 s^2,c3 s^3` has `i` larger than the displayed value and lies strictly
below the corresponding line (6), hence is zero.  This is a coefficientwise
proof for arbitrary `c1,c2,c3`; it neither divides by a centering coefficient
nor assumes one is nonzero.

The degree-`t^14` part of the already-imposed first Jacobian row

\[
 f_1(t)(1+25t^{24})-15t^{14}g_1(t)=0
\]

then gives

\[
 [t^0]g_1=-{E_1\over5}.               \tag{8}
\]

Since `dx wedge dy=s^2 ds wedge dt`, the next row is

\[
 [s^{-1}]J=f_1g_1'-f_1'g_1+2f_2q'-2p'g_2,
 \quad p=t^{15},\ q=t+t^{25}.         \tag{9}
\]

At degree `t^13`, the first and fourth terms in (9) cannot contribute.  Using
(7)--(8),

\[
\begin{aligned}
 [s^{-1}t^{13}]J
 &= -14(-3E_1)\left(-{E_1\over5}\right)
    +2(3E_2+3E_1^2)\\
 &= {6\over5}(5E_2-2E_1^2),
\end{aligned}
\]

which proves (1) over every characteristic-zero coefficient field.

For the previous frozen values `C=1,U=2,V=28/25`, formula (1) gives exactly
`-18858/3125`, recovering the Q-empty certificate.

## 3. Parameter stratification

The quadratic controlling (1) is

\[
\begin{aligned}
 Q(C,U,V)&=5E_2-2E_1^2\\
 &=-3C^2+2C(U+V)+UV-2U^2-2V^2.       \tag{10}
\end{aligned}
\]

- **Generic stratum `Q != 0`.** The next x row is impossible, independently
  of centering and pole data.
- **Real stratum.** The symmetric matrix of (10) has leading principal minors
  `-3, 5, -25/4`; hence (10) is negative definite.  Its only real zero is
  `C=U=V=0`, outside the source-typing open set.  Thus every source-typed real
  specialization is obstructed.
- **Complex zero stratum `Q=0`.** This is a genuine codimension-one survivor.
  Complex orbit values are allowed in JC2, so the real nonvanishing cannot be
  promoted to a terminal-class kill.

Normalize the nonzero chain orbit to `C=1` and put

\[
 S=U+V,\qquad D=UV.
\]

Then

\[
 [s^{-1}t^{13}]J
 ={6\over5}(-2S^2+2S+5D-3),          \tag{11}
\]

and the survivor is the one-dimensional graph

\[
 D={2S^2-2S+3\over5}.                \tag{12}
\]

The exact source-open conditions on this graph are

\[
 D\ne0,qquad 1-S+D\ne0,
 \qquad S^2-4D\ne0,                  \tag{13}
\]

excluding respectively a zero extra orbit, collision with the chain orbit,
and collision of the two extra orbits.  After substituting (12), the three
excluded finite divisors are

\[
\begin{aligned}
 2S^2-2S+3&=0,\\
 2S^2-7S+8&=0,\\
 -3S^2+8S-12&=0.
\end{aligned}
\tag{14}
\]

There are therefore many source-typed complex points on (12).

## 4. Exact symbolic transport on the normalized survivor

To prove that (12) is not merely a formal zero of one coefficient, the replay
fixes the already licensed center `(c1,c2,c3)=(1,1,1)` and zero dead stretch,
but retains `S,D,L,A` symbolically.  Here

\[
 L=25(1-U)(1-V)=25(1-S+D)             \tag{15}
\]

is the F1-to-r9 Taylor factor and the pole patterns are

\[
\begin{aligned}
 p(\zeta)&=L^3\zeta(\zeta^5-A),\\
 q_0(\zeta)&=L^5\left(\zeta^{10}
                   -{5\over3}A\zeta^5+{5\over9}A^2\right).
\end{aligned}
\tag{16}

One exact rational factorization of all `6547` first-band rows has rank
`3508` in `3602` variables.  Propagating the symbolic right-hand sides through
that factorization produces exactly two nonzero dependent rows:

\[
\begin{aligned}
 L^3+[25(S-D-1)]^3&=0,\\
 L^5+[25(S-D-1)]^5&=0.                \tag{17}
\end{aligned}
\]

Both are identities under (15).  There is no other transport-compatibility
condition and the first-band solution space has affine dimension `94` over
the resulting parameter field.

The leading pole ODE is exactly

\[
 3p q_0'-5p'q_0={25\over9}L^8A^3.
\]

Because the chart determinant is `-25r^-9`, its first Jacobian normalization
is

\[
 L^8A^3=9.                            \tag{18}
\]

On the source-open locus `L != 0`, equation (18) always has three nonzero
solutions for `A` over `C`.

No parameter-dependent pivot denominator occurs in this calculation: the
matrix is the fixed rational matrix for center `(1,1,1)`.  Its rank is
`3508` throughout; (17) records all possible right-hand-side incompatibility.

## 5. The complete paired next row survives

The replay symbolically computes the constant part of every one of the 40
possible x-next coefficient slots and separately computes their homogeneous
directions in the 94 free coefficients.

- Degrees `37,38,39` are identities.
- Degree `13` has zero homogeneous part and constant (11).
- The remaining 36 homogeneous rows are independent.

Consequently (11) is the **only** x-next compatibility equation.  On (12),
all of `[s^-1]J=0` is solvable and leaves affine dimension `94-36=58`.

For the pole next row, let `P,Q_3,Q_8` denote respectively the homogeneous
parts of `[zeta^4]p_1`, `[zeta^3]q_1`, and `[zeta^8]q_1`.  Modulo the 36 x rows,
these three vectors are independent; the deterministic quotient pivots are
`10,25,38`.  The two actual pole-J rows modulo the x system are

\[
\begin{aligned}
 R_3={}&-{4\over9}L^5A^2P-{1\over5}L^3A Q_3,\\
 R_8={}& {2\over3}L^5A P-{3\over5}L^3Q_3
          -{4\over5}L^3A Q_8.         \tag{19}
\end{aligned}
\]

When `L A != 0`, `R_3` has a nonzero `Q_3` component and `R_8` has the unique
nonzero `Q_8` component.  They therefore add rank two for every source-typed
point, with no affine compatibility condition.  The simultaneous x-next and
pole-next system on (12)--(13),(15),(18) is nonempty of affine dimension

\[
 94-36-2=56.                           \tag{20}
\]

For a successor computation, an especially convenient exact algebraic point
keeps all pole data rational.  Let `S` be either root of

\[
 10S^2-35S+37=0,
\]

and set

\[
 C=1,\quad D=S-{22\over25},
 \quad L=3,\quad A={1\over9}.         \tag{21}
\]

The quadratic for `S` has discriminant `-255`, so this is genuinely complex.
Here `1-S+D=3/25`, hence neither `U` nor `V` equals the chain orbit.  If
`D=0`, then `S=22/25`, which is not a root of the displayed quadratic, so both
extra orbits are nonzero.  Their discriminant is
`S^2-4S+88/25`; a common zero with `10S^2-35S+37` would force
`5S+9/5=0`, and `S=-9/25` is not a root.  Thus `U,V` are also distinct.
Finally `3^8(1/9)^3=9`, so (18) holds.  Point (21) meets every
nondegeneracy condition used in this gate and certifies a genuine complex
paired-next-row survivor without introducing a cubic pole-field extension.

## 6. Smallest remaining implication

For this normalized SP-2 chart-pattern control, the next bounded proof gate is
now forced onto the complex codimension-one locus (12): impose the following
paired Jacobian band on the 56-dimensional exact family, or derive a global
condition that excludes (12).  Repeating generic samples off (12) cannot add
information.

Before any SP-2 or terminal-class claim, a campaign-level argument must also
justify that the retained x-boundary normalization exhausts the licensed
x-direction data, and must restore every omitted Eggers-tree, other-infinity,
mapping-degree, and landing condition.  Formula (1) quantifies all common
centering and pole moduli for this coefficient, but it does not by itself
quantify broader boundary-pattern freedom or the other seven td=6 classes.

## 7. Reproducibility and JC2 scope

Run:

```text
python3 cases/td6_moduli_uniformity_20260824/replay.py
```

The replay uses only exact `Fraction` arithmetic and sparse polynomials over
`Q`; no modular samples, floating point, generic sparse search, or AWS were
used.

| artifact | SHA-256 |
|---|---|
| moduli-uniformity replay | `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab` |
| canonical replay stdout | `596a3f54276d4b95ec241933a6c7ec1cf1d782e8b7d40376532e172e282da5ea` |
| symbolic certificate payload | `45cdf5d42496d3807c006cf27387cea4f91b3c3bc18155d7a0812e1d82c130f0` |
| imported next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| imported next-row report | `32124d20ec84ef59d5b116639176b12053f5da6de1a9458dd4a2095d6b1618f0` |

**JC2 scope:** this is an exact generic obstruction and an exact complex
finite-order survivor for one SP-2 chart-pattern normalization.  It neither
realizes nor kills a terminal class, supplies no Keller pair, and neither
proves nor disproves the plane Jacobian conjecture.  No canonical campaign
file was edited.
