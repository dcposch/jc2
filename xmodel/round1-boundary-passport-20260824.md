# Round-1 boundary passport — portfolio root P1

- **Producer/session:** Averroes (`/root/strategy_audit`)
- **Round:** `20260824`, one-day-equivalent boundary kill test
- **Status:** frozen exact report; no shared-ledger promotion
- **Arithmetic:** `QQ`, SymPy `1.14.0`, exact assertions only

## Verdict: COSTUME

No measured quantity in the mandatory suite is both stable under the allowed
equivalent presentations and stronger than determinant order / total pole
mass. The full gradient-cokernel Smith pair, log-coframe Smith pair, and action
primitive pole orders contain real information about a *chosen presentation*,
but they change under elementary and Hénon automorphisms and collapse to the
identity after exact orbit minimization. The only raw Keller-suite survivors
are the log-determinant orders `(-2,-1)` and zero residues of exact
differentials. The first is the coordinate-volume form of `J=1`; the second is
automatic for an exact meromorphic differential. Neither is a stronger
passport.

This verdict kills the advertised coordinate-free capacities below. It does
not weaken the pure-boundary Jacobian identity itself.

## Evidence perimeter

The promoted exact inputs are only:

1. the dual-confirmed pure-boundary identity and non-Keller class-kill family
   in `AUDIT.md:979-1015`;
2. the dual-confirmed Hénon automorphism tower in `AUDIT.md:1103-1124`, with
   construction independently recorded in `xmodel/sol-k2c.md:119-161`; and
3. elementary exact polynomial composition for the identity, `T_2`, `T_4`,
   and `T_4^{-1}∘T_4`.

The class-kill member is used only as a negative/schema control. No residue-A
leading pair without its unknown tails is scored as a Keller control or as
positive evidence. Earlier primitive-only experiments were not used as a
premise; the checker recomputes every displayed result.

## Smallest exact schema

Let `F,G` be the separate-degree homogenizations of `f,g`. On a generic
boundary DVR with parameter `t`, form

```text
A = [[F_X, G_X],
     [F_Y, G_Y]].
```

For a rank-two matrix its generic Smith exponents `(a,b)` are recovered from
the complete Fitting data

```text
a     = ord_t Fitt_1(coker A) = min_ij ord_t(A_ij),
a + b = ord_t Fitt_0(coker A) = ord_t(det A).
```

Thus `(a,b)` retains the distribution discarded by the determinant whenever
`a != 0`. For the meromorphic log coframe the same valuation rule is applied
to the columns `df,dg` in a logarithmic basis; negative exponents record
poles.

The primitive-polar supplement uses the two polynomial one-forms

```text
omega_P = f dg - x dy,
omega_Q = g df - y dx.
```

Their curls are respectively `J(f,g)-1` and `1-J(f,g)`. Hence they are exact
for every Keller control, and the checker constructs their polynomial
primitives, pole orders, and divisorial differential residues. For the
non-Keller decoy the nonzero curls are retained instead of inventing
primitives.

## Explicit compactification and blow-up

For the Keller suite use the `X=1` chart

```text
u=Z/X, v=Y/X, x=1/u, y=v/u;   boundary u=0.
```

Blow up `[1:0:0]` in the explicit chart

```text
u=s, v=s*w, hence x=1/s, y=w;  exceptional divisor s=0.
```

For `T_n=(x,y+x^n)` this gives the gradient matrices

```text
A_standard = [[1, n], [0, u^(n-1)]],
A_blowup   = [[1, n], [0, s^(n-1)]],
```

so both gradient Smith pairs are `(0,n-1)`. Its log-coframe matrices are

```text
L_standard = [[-u^-1, -v*u^-1 - n*u^-n], [0, u^-1]],
L_blowup   = [[-s^-1,             -n*s^-n], [0,    1]],
```

with Smith pairs `(-n,n-2)` and `(-n,n-1)`. Although the split changes under
presentation and blow-up, the log determinant orders remain `-2` and `-1`.
For the identity the blow-up matrix is `diag(-s^-1,1)`, giving `(-1,0)`.

The class-kill decoy is evaluated at its own root `[0:1:0]` in the symmetric
chart `z=Z/Y,r=X/Y`, followed by `z=s,r=s*w`.

## Mandatory covariance suite

Each `Smith` entry below is `(standard -> blow-up)`. Primitive poles list the
standard and blow-up orders; `P` and `Q` agree on these controls. A dash means
the primitive is zero.

| Exact map | `(deg f,deg g)` | gradient Smith | log Smith | primitive poles | exact minimized representative |
|---|---:|---|---|---:|---|
| identity | `(1,1)` | `(0,0) -> (0,0)` | `(-1,-1) -> (-1,0)` | `(-,-)` | identity |
| `T_2` | `(1,2)` | `(0,1) -> (0,1)` | `(-2,0) -> (-2,1)` | `(3,3)` | identity |
| `T_4` | `(1,4)` | `(0,3) -> (0,3)` | `(-4,2) -> (-4,3)` | `(5,5)` | identity |
| `T_4^{-1}∘T_4` | `(1,1)` | `(0,0) -> (0,0)` | `(-1,-1) -> (-1,0)` | `(-,-)` | identity |
| Hénon `r=0` | `(42,84)` | `(0,124) -> (36,88)` | `(-84,82) -> (-12,11)` | `(126,18)` | identity |
| Hénon `r=1` | `(84,168)` | `(0,250) -> (72,178)` | `(-168,166) -> (-24,23)` | `(252,36)` | identity |

Before minimization, degrees, both gradient Fitting orders, the gradient Smith
split, the log Smith split, and primitive pole orders differ among equivalent
automorphism presentations. `T_4^{-1}∘T_4` simplifies exactly to the identity,
so no word-history datum survives even before a minimizer is invoked. The
Hénon maps are explicit compositions of polynomial automorphisms with explicit
inverses; minimization to the identity is therefore certified, not heuristic.
After that minimization every Keller row has the identity metrics.

For every Keller row the log determinant has orders `(-2,-1)` and every
primitive differential residue is exactly zero. The former follows directly
from `df∧dg=dx∧dy`; the latter follows because the residue of an exact
meromorphic differential vanishes. These are stable but not stronger than
the determinant/volume identity.

## Negative control

For `(B,alpha,beta)=(2,2,3)`, the class-kill map is

```text
f=x^4+y,  g=x^6+y^5,
J=-2*x^3*(3*x^2-10*y^4),
```

so it is not Keller. Its gradient Smith pair is `(0,1) -> (1,3)`, its log
pair is `(-6,-3) -> (-5,0)`, and its log determinant orders are `(-9,-5)`.
In the standard class-kill chart the gradient determinant is

```text
-2*r^3*z*(3*r^2*z^2-10),
```

which exposes the residual Jacobian curve. Both action forms are nonclosed.
This confirms that the schema can see a gross non-Keller failure; it is not a
positive counterexample-side control and supplies no evidence for a Keller
capacity.

## Variants killed precisely

1. **Untwisted action residue / period charge.** Both action forms are exact
   on every `J=1` control, and their divisorial differential residues vanish.
   A nonzero charge cannot arise from these untwisted exact forms.
2. **Action-primitive pole order as an invariant budget.** It is `3,5,126,252`
   already on equivalent tame/Hénon presentations, changes under the explicit
   blow-up, and becomes zero after minimization.
3. **Raw gradient `Q`, `Fitt_1`, or its Smith filtration as a coordinate-free
   passport.** `T_n` gives arbitrary `(0,n-1)` and the Hénon blow-up gives
   `(36,88)` then `(72,178)`, while all minimize to `(0,0)`.
4. **Raw log-coframe Smith split or unsigned localized-Chern charge.** The
   individual exponents change under presentation and blow-up. Only their
   determinant sum has the universal volume meaning.
5. **Raw boundary exponent/Smith size as a uniform consumable cap.** It grows
   with `n` and along the Hénon automorphism tower, so it measures presentation
   complexity rather than an intrinsic noninvertibility budget.

## Narrow remainder, not a promoted claim

The computation does not rule out using `Q` as a checksum attached to one
fixed, certified, choice-independent minimal compactification of an actual
nonautomorphic Keller map. It also does not rule out a boundary-twisted form or
a signed global invariant built from complete polynomial data. Those redesigns
would first need a proved covariance/minimality theorem, a genuine positive
Keller-side control (presently unavailable without solving the problem), and a
positivity or finite-charge statement. Until then they are source-schema
possibilities, not proof invariants.

No theorem lane is opened from this result.

## Reproducible artifacts

- Exact checker: `cases/round1_boundary_probe/boundary_probe.py`
- Frozen compact output: `cases/round1_boundary_probe/results.json`
- Replay contract and schema: `cases/round1_boundary_probe/README.md`
- Full audit JSON SHA-256 (default checker output):
  `a7168b569fe07c622125b68cb9bb14775687af3bbefe777ffa62cb980b0a9a9b`

Replay the pinned command in the README and require a byte-for-byte diff
against `results.json` before reusing the figures.
