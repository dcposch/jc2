# Hostile review: rational-forest first-leg gate and the first nonlinear Miranda family

Date: 2026-08-30 UTC
Reviewer: Opus 5 (independent, different-model)
Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`
Scope: bounded, exact-desk only. No shell CAS beyond exact rational arithmetic.

## 0. Custody

Both sealed inputs verify byte-exactly at the stated hashes; the producer body
is 8578 bytes with SHA-256 `42aedb00…428ecf64` as declared. The producer's own
basis is `0d7544eb…`, an ancestor of the review basis; no input was edited.

FALLACY-v2: this review asserts no exit price, so no `charge_basis` line is
emitted. Nothing here consumes cv-flag, place, or series machinery.

## 1. Overall verdict

**CONFIRM_WITH_CORRECTIONS.** Every displayed formula reconstructs. Two
statements need repair (a §2 equality clause that is strictly too strong, and
an unstated projective convention in §3 without which the displayed
countercontrol map is wrong), and one number (`barP1=18`) rests on a
hypothesis the producer never establishes in-document. The core gate and the
`d>=3` and generic-`d=2` exclusions survive intact.

Itemized:

```text
1  residue/normalization/duality formula (1.1)-(1.3)   CONFIRMED
2  unirationality + rational-forest gate                CONFIRM_WITH_CORRECTIONS
3  multisection bound (2.1), (2.2), n=1 recovery        CONFIRMED (upgraded to equality)
4  A^2 countercontrol; (3.1); lambda_i = i-1            CONFIRM_WITH_CORRECTIONS
5  K=(d-3)A+B, p_g=(d-1)(d-2)                           CONFIRMED (one exception missing)
6  d=2 rationality, genus 2, R=2A+B, 2/9/8/18           CONFIRM_WITH_CORRECTIONS
7  safe nonlinear consequence and nonclaims             CONFIRMED
```

## 2. Item 1 — the exact formula: CONFIRMED

Reconstructed independently. `omega_X(D)=Omega^2_X(log D)` for reduced SNC `D`
on a smooth surface, and `omega_X(D)|_D=omega_D` holds for *any* effective
divisor on a smooth surface (`D` is a local complete intersection, hence
Gorenstein); SNC is not needed for the residue sequence itself, only for the
log identification. The long exact sequence gives

```text
h^0(K_X+D) = p_g + h^0(D,omega_D) - rank(partial).
```

Duality on the projective Gorenstein curve `D` gives `h^0(omega_D)=h^1(O_D)`;
this is valid for **disconnected** `D`. The normalization sequence
`0 -> O_D -> nu_* O_{Dtilde} -> ⊕_nodes C_p -> 0` yields

```text
h^1(O_D) = sum_i g(D_i) + (E - V + c),   c = #connected components,
```

so `tau(D)` is exactly the producer's. **Parallel edges** are handled
correctly: two components meeting at two points give `E=2, V=2, c=1, b1=1`.
**Disconnected** `D` is handled by the `+c` term, e.g. two disjoint smooth
curves give `b1=0`. `h^1(X,omega_X)=q` by Serre duality, so
`rank(partial)<=min(tau,q)` and (1.2) follows; `q=0` forces `rank(partial)=0`
and (1.3) is an equality.

Controls: `P^2` minus one line gives `0` (`A^2`, correct); minus two lines
gives `0` (`A^1 x C^*`, `kappabar=-infinity`, correct); minus three general
lines gives `1` (`(C^*)^2`, `K+D=0`, correct); minus three *concurrent* lines
resolves to `b1=0` and gives `0` (an `A^1`-bundle, correct).

**Correction (scope, not error).** The derivation uses smoothness of each
`D_i`. Under mere normal crossings (a component with a self-node) the formula
survives only with `g` read as geometric genus of the normalized component and
the self-node read as a graph loop. State "SNC in the strict sense: each `D_i`
smooth, pairwise transverse, no triple points," or say "geometric genus"
throughout. The producer's later uses are all in the strict SNC setting, so
nothing downstream breaks.

## 3. Item 2 — unirationality and the gate: CONFIRM_WITH_CORRECTIONS

The chain is sound. A dominant morphism `A^2 -> U` with `dim U = 2` is
generically finite; `A^2 ⊂ P^2` gives a dominant rational `P^2 --> X`.

**Cleaner route than Castelnuovo.** The producer invokes unirationality plus
"over `C` this forces `q=p_g=0`", i.e. Castelnuovo's rationality theorem. That
is true but heavier than needed: resolving `P^2 --> X` as `S -> P^2` birational
and `S -> X` generically finite dominant gives injections
`H^0(X,omega_X^{⊗n}) ↪ H^0(S,omega_S^{⊗n}) = 0` and
`H^0(X,Omega^1_X) ↪ H^0(S,Omega^1_S) = 0`, and in char 0 on a smooth
projective surface `q = h^0(Omega^1_X)`. So `p_g=q=0` with no rationality
theorem. Recommend substituting this; it removes a heavy citation from a
load-bearing step.

Injectivity of log-pluricanonical pullback along a dominant generically finite
morphism of smooth quasi-projective complex varieties (Iitaka) is correctly
invoked, including in the nonproper case. Direction check: `kappabar(A^2) >=
kappabar(U)`, so `kappabar(U) = -infinity`, so `barP_n(U)=0` for all `n>=1`;
with `p_g=q=0`, (1.3) forces `sum g(D_i) = b1(Gamma_D) = 0`, both summands
being nonnegative. The gate is **correct**.

**Missing hypotheses (all repairable, none fatal).**

1. `U` must be smooth (or the conclusion must be read on a smooth model).
   `kappabar` is only defined via a smooth SNC completion. If the intended
   target is singular, replace it by a resolution `Utilde`; the dominant
   morphism restricts over the smooth locus and induces a dominant *rational*
   `A^2 --> Utilde`, which suffices (see 2 below). State this.
2. A dominant **rational** map from `A^2` is already enough. Resolve
   indeterminacy: `W -> A^2` proper birational with `W -> U` a morphism;
   `kappabar` is a proper-birational invariant of smooth varieties, so
   `kappabar(W) = kappabar(A^2) = -infinity`. This strengthening is free and
   makes the gate robust to first legs defined only rationally.
3. "Rational" must mean geometric genus zero of the component. On the
   *resolved* boundary the strict transform of a boundary curve is smooth, so
   its genus is the geometric genus of the original; a rational curve with
   nodes is allowed upstairs but its nodes create graph cycles downstairs.
4. **Monotonicity is the right robustness statement and is absent.** If
   `U' ⊆ U` is open dense with boundaries `D ⊆ D'`, then
   `n(K+D') = n(K+D) + n(D'-D)` with `D'-D` effective, so
   `barP_n(U') >= barP_n(U)`. Equivalently, `tau` is monotone under adding
   boundary components: a new component meeting the old boundary in `e` points
   spread over `j` old connected components changes `b1` by `e-j >= 0`. This
   is what licenses using **one** boundary component (e.g. `H_infinity` in §5)
   to fire the gate without knowing the rest of the boundary. Promote it.

## 4. Item 3 — multisection bound: CONFIRMED, and it is an equality

I reconstructed `b1` of the resolved dual graph by direct vertex/edge counting
and obtained more than (2.1). Let `H` be any reduced curve on a smooth
projective surface with components `H_1..H_s`, `c` connected components, and
`m_q` analytic branches at each `q in Sing(H)`. Embedded-resolving,

```text
tau(H_res) = sum_i g(Htilde_i) + sum_{q in Sing H} (m_q - 1) - s + c.   (R1)
```

Proof of the graph term: the exceptional divisor over each blown-up point is a
connected **tree** with `t_q` vertices and `t_q - 1` internal edges; after
embedded resolution each of the `m_q` branches meets that tree in exactly one
point, at `m_q` distinct points. Then `E - V + c` telescopes: the `t_q` cancel
and only `sum_q (m_q-1) - s + c` survives. (R1) is resolution-independent, as
it must be: blowing up a free point changes `V,c` by `+1` each; a smooth point
of the boundary changes `V,E` by `+1` each; a node changes `V` by `+1` and `E`
by `+1`. All leave `b1` fixed.

Specialize to `H = C ∪ D_infinity` on a ruled surface over `P^1` (so
`p_g = q = 0`), `s = 2`, `D_infinity` smooth. Points of `C ∩ D_infinity` have
`m_q = r_q + 1`, so `sum_q (m_q-1) = r + sum'_q (m_q - 1)` where `sum'` runs
over singular points of `C` off `D_infinity`. With `c=1` when `r>=1` and `c=2`
when `r=0`:

```text
barP_1(P \ (C ∪ D_infinity))
  = g + max(r-1,0) + sum_{q in Sing(C) \ D_infinity} (m_q - 1).   (R2)
```

So **(2.1) is confirmed and sharpened to an exact equality**, with the excess
term named. Every audited item behaves:

- *Several branches at one boundary point.* Two branches at `p`, distinct
  tangents, transverse to `D_infinity`: one blowup, `V=3`, `E=3` (two of them
  parallel `C'–E_1` edges), `b1=1=r-1`. Three branches: `V=3`, `E=4`,
  `b1=2=r-1`.
- *Paths sharing exceptional vertices.* Two branches mutually tangent to order
  2 at `p`: two blowups, `V=4`, `E=4`, `b1=1=r-1`. One branch transverse and
  one tangent to `D_infinity`: two blowups, `V=4`, `E=4`, `b1=1=r-1`. Sharing
  exceptional vertices never destroys the count, because each extra shared
  vertex brings its own extra edges.
- *Two distinct transverse contacts.* `V=2`, `E=2` parallel edges, `b1=1`.
  This is exactly where the parallel-edge convention of §1 is load-bearing.
- *`r=0`.* `c=2` and (R2) returns `g + sum'`, matching `max(r-1,0)=0`.
- *Recovery of the reviewed `n=1` two-section formula.* `C=D_0` a section, so
  `g=0`, unibranch at each of the `#S` collisions, `sum'=0`, giving
  `barP_1 = #S - 1`. The coordinator's `barP_n = n(#S-2)+1` at `n=1` gives
  `#S-1`. **Agreement.** `#S<=1` gives `0` on both sides.

**Repair (small, real).** §2's equality clause reads "Equality holds if `C` is
smooth away from the displayed contacts…", which is strictly stronger than
needed and contradicts the producer's own next sentence. The correct condition
from (R2) is: **`C` is unibranch at every singular point off `D_infinity`.**
Cusps, ramphoid cusps and all unibranch singularities are permitted.

**Unstated hypothesis.** §2 never says `p_g(P)=q(P)=0`; it is true for a
`P^1`-bundle over `P^1` but is what licenses (1.3). Over a base of genus
`h>0`, `q=h` and only the weaker (1.2) applies. State the base is `P^1`.

`k` (the multisection degree) never enters (R2). That is correct and is the
content of §3's countercontrol.

## 5. Item 4 — countercontrol, discrepancies, tangency losses

**The `A^2` identification: CONFIRMED.** `C = closure{z=w^k}` has class
`A + kB`, `D_infinity = {w=infinity} ~ B`, so `C.D_infinity = 1`: they meet
transversally at one point and the boundary is already SNC, `V=2, E=1, b1=0`,
`g=0`, hence `barP_1 = 0` by (1.3) — consistent with the complement being
`A^2`. Structurally: deleting `{w=infinity}` leaves `A^1_w x P^1_z`, and
`{z=w^k}` is a section of that `P^1`-bundle, so the complement is a
`P^1`-bundle minus a section over an affine line, `≅ A^2`. Sharpness of the
gate at this type is established: arbitrarily large multisection degree, no
obstruction.

**CORRECTION (convention, load-bearing).** The displayed map
`(w,t) |-> (w, z=[t : t*w^k+1])` with `t = Z0/(Z1 - w^k Z0)` is correct **only**
under the convention `z = Z1/Z0`, i.e. `z = w^k + 1/t`. Under the opposite
reading `z = Z0/Z1` the map is `z = t/(1+t w^k)` and it **lands on the deleted
curve**: `z = w^k` whenever `t(1-w^{2k}) = w^k`, e.g. `(w,t)=(0,0)` and, for
`k=3`, `(w,t)=(2,-8/63)`. Both displayed formulas are mutually consistent
(`Z1 - w^k Z0 = 1` identically), so this is a notational omission, not a
mathematical error, but the convention must be printed. Recommended
replacement, convention-free: `(w,t) |-> (w, [t : 1 + t w^k])` with `z` the
ratio *second-over-first*, equivalently `z = w^k + 1/t`, `t=0 |-> z=infinity`.

**The discrepancy identity (3.1): CONFIRMED.** With `Dtilde` the reduced total
transform, `K+Dtilde = rho^*K + sum a_E E + rho^*D - sum N_E E + sum E`, giving
`lambda_E = N_E - a_E - 1` exactly. The section characterization is valid even
where `lambda_E < 0` (blowup at a smooth point of `D` gives `lambda=-1`, off
`D` gives `-2`), because `rho_* O(sum m_E E) = O` for effective exceptional
`sum m_E E`; such `E` simply impose no condition. Note `lambda_E <= 0` for all
`E` is precisely log canonicity of `(X,D)`, which is the hypothesis §5 uses.

**Tangency losses `lambda_i = i-1`: CONFIRMED.** For two smooth branches of
contact order `mu` (`y=0`, `y=x^mu`), the chain of `mu` blowups has each
`p_{i+1}` on `E_i` only, so `a_i = i`, and `N_i = 2i` by direct multiplicity
bookkeeping (`N_1=2, N_2=1+1+2=4, N_3=1+1+4=6, …`). Hence
`lambda_i = 2i - i - 1 = i-1` for `i=1..mu`, matching the coordinator's
`sum_{i=1}^{m_s} (i-1) E_{s,i}`.

**Unibranch cusps stay distinct: CONFIRMED, with a numerical correction to the
narrative.** For `y^2=x^3` the resolution has `N=(2,3,6)`, `a=(1,2,4)`, hence
`lambda = (0,0,1)`. So a cusp contributes `0` to `b1` (invisible to the
rational-forest test) but imposes one genuine vanishing condition in (3.1).
The producer's claim that a unibranch cusp "can consume an effective `K+D`
without creating a graph cycle" is therefore correct; if any exponents are
ever printed, they are `(0,0,1)` for `A_2`, not `(0,1,2)`.

## 6. Item 5 — `(d,3)` incidence surface: CONFIRMED

`X_d` a smooth divisor of class `dA+3B` in `P^2 x P^1`, `K_{P^2 x P^1} =
-3A-2B`, so adjunction gives `K_{X_d} = (d-3)A + B`. (4.1) confirmed; only
smoothness of the divisor is needed for the class.

For `p_g`, restrict:
`0 -> O(-3A-2B) -> O((d-3)A+B) -> K_{X_d} -> 0`. By Künneth,
`H^*(P^2,O(-3))` is `C` in degree 2 and `H^*(P^1,O(-2))` is `C` in degree 1,
so `O(-3A-2B)` has cohomology only in total degree 3; in particular
`h^0 = h^1 = 0`. Hence

```text
p_g(X_d) = h^0(P^2,O(d-3)) * h^0(P^1,O(1)) = 2*C(d-1,2) = (d-1)(d-2),
```

verified for `d=3..8` (`2,6,12,20,30,42`). (4.2) **CONFIRMED**, and `>0` for
`d>=3`. The exclusion is then immediate and does not even use the boundary:
`p_g>0` is a birational invariant, so no smooth projective model is
unirational, so no dominant (even rational) map from `A^2` to any dense open.

**Presentation/basis dependence.** The producer's own caveat is correct and
should be kept verbatim: `d` is a property of the chosen global trace-zero
Miranda basis, not of the cubic algebra. Nothing here makes it intrinsic.

**Projective-closure exceptions.** The producer lists singular or degenerate
infinity closure, reducible/extraneous projective component, and degree drop
after cancellation. One further exception is **missing and is real**: a drop
in the `[X:Y]` degree. For bidegree `(d,e)` the same computation gives
`K = (d-3)A + (e-2)B` and `p_g = h^0(O_{P^2}(d-3)) * h^0(O_{P^1}(e-2))`. For
`e=2` this is `C(d-1,2) > 0` for `d>=3`, so the gate survives; but for `e=1`
it is **`0`** (`X_d -> P^2` is then birational and `X_d` is rational). So
"cubic in `[X:Y]`", i.e. nonvanishing of the leading `[X:Y]` coefficient after
homogenization, is a load-bearing hypothesis and must be listed alongside the
`(u,v)`-degree drop. Also worth stating explicitly: the projective closure of
the affine incidence variety is a *component* of `{Phi^h=0}`; equality needs
`Phi^h` irreducible, which is the stated hypothesis but is a separate check
from smoothness.

## 7. Item 6 — `d=2`: CONFIRM_WITH_CORRECTIONS

**Rationality: CONFIRMED.** `X_2 -> P^1` has plane-conic fibres; if `X_2` is
smooth irreducible and dominates `P^1`, the generic fibre is a smooth conic
over `C(t)`, which is `C_1` by Tsen, hence has a rational point, hence is
`P^1_{C(t)}`; `X_2` is rational and `p_g=q=0`. Cross-check by the §5 method:
`h^0(P^2 x P^1, -A+B) = 0` and `h^1(-3A-2B)=0`, so `p_g(X_2)=0` directly.

**Infinity curve: CONFIRMED.** `{z=0} x P^1 ≅ P^1 x P^1` and `(2A+3B)` restricts
to bidegree `(2,3)`; `(2,3)` is very ample on `P^1 x P^1`, so Bertini gives a
smooth irreducible general member, of genus `(2-1)(3-1) = 2`. Combined with §3
monotonicity, `barP_1(X_2 \ H_infinity) = 0 + 2 + 0 = 2 > 0`, and any dense
open of it inherits `barP_1 >= 2`. **The generic quadratic block is excluded
from `H_infinity` alone.** This is the strongest safe statement in the
document and it does not depend on anything in the rest of §5.

**Projectively finite locus: all six numbers CONFIRMED.** Intersection numbers
on `X_2 = 2A+3B` recomputed independently: `A^2 = 3`, `A.B = 2`, `B^2 = 0`.
With `pi` finite of degree 3, `R_pi = K_{X_2} - pi^*K_{P^2} = (-A+B) + 3A =
2A+B`; `H_infinity = pi^*{z=0} ~ A`; `K + H_infinity + R_pi = 2A+2B`. Then
`p_a(H_infinity) = 1 + (A.(A+K))/2 = 1 + (A.B)/2 = 2`;
`p_a(R_pi) = 1 + ((2A+B).(A+2B))/2 = 1 + 16/2 = 9`;
`H_infinity . R_pi = 2A^2 + A.B = 8`; and with `V=2, E=8, c=1`,
`b1 = 7`, giving `barP_1 = 0 + 2 + 9 + 7 = 18`. Consistency check: `pi_*R_pi`
has degree `R.A = 8`, matching the degree-8 discriminant of a cubic with
quadratic coefficients, and a degree-8 plane curve of geometric genus 9 has
`delta = 12`, which is unremarkable for a generic triple cover.

The ampleness claim also checks: `A = pi^*H` with `pi` finite is ample, `B` is
nef, so `2A+2B` is ample. And `lambda_E <= 0` for all `E` is exactly log
canonicity, so "log canonical `=>` log general type" is correct:
`rho^*(ample) + effective` is big.

**Corrections required before any promotion of `18`.**

1. **The number `18` is conditional on a hypothesis this document never
   states, let alone proves: that `R_pi` is part of the deleted boundary.**
   §5 introduces `R_pi` with no argument that the first-leg target is
   `X_2 \ (H_infinity ∪ R_pi)` rather than `X_2 \ H_infinity`. The coordinator
   alludes to a "deleted ramification graph" from the separate `AL3-REDUCE`
   lane, which is explicitly not promoted. Label `18` as conditional on that
   reduction; the unconditional number is `2`.
2. **`p_a` is not `g`.** (1.3) needs geometric genus of each *irreducible*
   component of the *resolved* boundary. The document computes `p_a(H_infinity)`
   and `p_a(R_pi)` by adjunction and then feeds them into (1.3). This is legal
   only when each is smooth and irreducible. The producer's blanket "generic
   SNC" is doing that work silently; smoothness and irreducibility of `R_pi`
   are asserted, not proved, anywhere in the document. Under (R1) the correct
   general statement replaces `2 + 9 + 7` by
   `sum g(tilde) + sum_q (m_q-1) - s + c`, and `p_a - tau_res =
   sum_q (delta_q - m_q + 1) >= 0`, with equality contribution `0` exactly at
   ordinary nodes. So `18` is an **upper** bound over the reduced-pair stratum
   and drops on every non-nodal degeneration.
3. **Reduced support vs. ramification vs. discriminant multiplicity.** The
   producer flags this and is right to; the numbers `9`, `8`, `18` all use
   `R = R_red = 2A+B`. If the cover is totally ramified along a curve, the
   different has multiplicity `2` there and `R_red` has smaller class, changing
   `p_a`, the intersection number, and hence `18`. Likewise the reduced branch
   curve in `P^2` can have degree below `8`. Keep the three objects named
   separately in any promoted statement.
4. `H_infinity . R_pi = 8` counts intersections **with multiplicity**; the
   `b1 = 8-1 = 7` step needs 8 *distinct transverse* points. Non-transverse
   contact reduces `b1` and is exactly a rational-forest degeneration
   direction, so this is not a harmless genericity assumption — it is the
   stratum the successor must classify.

## 8. Item 7 — maximum exact theorem safe to promote

Promote exactly this, and nothing wider.

> **Theorem (rational-forest gate).** Let `U` be a smooth quasi-projective
> complex surface and `(X,D)` any smooth projective completion with `D` reduced
> SNC. Then `barP_1(U) = p_g(X) + sum_i g(D_i) + b1(Gamma_D) - rank(partial)`,
> with `rank(partial) <= min(tau(D), q(X))`. If there exists a dominant
> rational map `A^2 --> U`, then `p_g(X) = q(X) = 0`, every `D_i` is rational,
> and `Gamma_D` is a forest. The conclusion is inherited by every dense open
> subset of `U`.

> **Corollary (multisection).** For a `P^1`-bundle `P -> P^1`, a section
> `D_infinity`, and an irreducible multisection `C` of any degree with
> normalization of genus `g` and `r` analytic branches meeting `D_infinity`,
> `barP_1(P \ (C ∪ D_infinity)) = g + max(r-1,0) +
> sum_{q in Sing(C)\D_infinity}(m_q - 1)`. No dominant `A^2` first leg exists
> if `g>0`, `r>=2`, or `C` has a multibranch singularity off `D_infinity`. At
> `g=0, r<=1` and `C` unibranch off `D_infinity` the gate is silent, and
> `(P^1 x P^1) \ ({w=infinity} ∪ closure{z=w^k}) ≅ A^2` shows it must be.

> **Corollary (Miranda presentations).** For a presentation whose homogenized
> incidence hypersurface `X_d ⊂ P^2 x P^1` is a smooth irreducible divisor of
> bidegree `(d,3)` with `d>=3`, `p_g(X_d)=(d-1)(d-2)>0`, so no dense open of
> `X_d` receives a dominant map from `A^2`. For `d=2` with `X_2` smooth
> irreducible and `H_infinity` smooth irreducible of bidegree `(2,3)`,
> `barP_1(X_2 \ H_infinity) = 2`, so the same conclusion holds.

Everything else is **conditional**: `barP_1 = 18` (conditional on deletion of
`R_pi`, on `R_pi` reduced/smooth/irreducible, and on 8 distinct transverse
contacts); the intrinsic meaning of `d`; and every claim about the surviving
strata. The producer's own §6 nonclaims are accurate and should be carried
forward verbatim. Explicitly **not** established: any general cubic block
theorem, primitivity, existence or nonexistence of a first leg on a surviving
stratum, any counterexample, any JC2 statement.

## 9. Repairs (precise)

- §1: say "each `D_i` smooth" (strict SNC), or read `g` as geometric genus.
- §1: replace "unirational, so over `C` `p_g=q=0`" by the direct pullback
  injection `H^0(omega_X^{⊗n}) ↪ H^0(omega_S^{⊗n}) = 0` on a resolution `S`;
  Castelnuovo becomes unnecessary.
- §1: add "dominant *rational* map suffices" and add the open-subset
  monotonicity `barP_n(U') >= barP_n(U)` for `U' ⊆ U`; §5 silently uses it.
- §2: state `p_g(P)=q(P)=0` as the hypothesis licensing (1.3).
- §2: replace the equality clause by "equality iff `C` is unibranch at every
  singular point off `D_infinity`", and upgrade (2.1) to the equality (R2).
- §3: print the projective convention `z = Z1/Z0` (equivalently
  `z = w^k + 1/t`); under `z = Z0/Z1` the displayed map meets the deleted
  curve, e.g. at `(w,t)=(0,0)`.
- §3: if cusp exponents are ever displayed, `A_2` gives `lambda=(0,0,1)`.
- §4: add "`[X:Y]`-degree exactly 3" to the exception list; bidegree `(d,1)`
  gives `p_g=0` for every `d`.
- §5: mark `barP_1=18` conditional on the `R_pi`-deletion reduction; state
  `2` as the unconditional number; replace `p_a` by geometric genus in the
  (1.3) inputs, or carry (R1) with the `sum_q(delta_q - m_q + 1)` defect term.

## 10. Cheapest next classification gate

Not the producer's four-step list as ordered. The cheapest single gate is step
(1) alone, made finite by the defect identity. Combining (R1) with
`p_a(H) = sum_i g(tilde H_i) + sum_q delta_q - s + c`:

```text
p_a(H) - tau(H_res) = sum_{q in Sing H} (delta_q - m_q + 1) >= 0,
```

each term `>= 0` and `= 0` exactly at an ordinary node. For a reduced boundary
`H` of bidegree `(2,3)` on `P^1 x P^1`, `p_a(H) = 2` is fixed by the class, so

> **Gate.** `H` has rational-forest resolution **iff** every component of `H`
> is rational **and** `sum_{q in Sing H} (delta_q - m_q + 1) = 2`.

This is a two-parameter, entirely finite classification: the total non-nodal
delta-excess must be exactly `2`, distributed over the singularities of a
`(2,3)` curve. The whole surviving stratum is therefore enumerable by hand
(`A_2 + A_2`; a single `A_4`; a tacnode plus a cusp; and the reducible
analogues), with the forest condition then checked componentwise. Only after
that enumeration is it worth paying for the ramification-curve retest or the
higher-plurigenera valuation conditions (3.1); those are strictly more
expensive and are only meaningful on the (small) surviving list. Nonreduced
infinity stays quarantined, as the producer says, since `p_a` is not fixed
there.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23670`.
- Body SHA-256:
  `40841431c554c63cedb13bda8f662e2633d97695ee8f5d91659479169e2d13e5`.
- Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`.
