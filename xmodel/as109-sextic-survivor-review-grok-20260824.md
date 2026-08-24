# Hostile different-model review — AS109 sextic `(4,6)` survivor discriminator

| Field | Value |
|---|---|
| Claim under review | After the imprimitive `(4,6)` split `N^2=kappa H^5`, both `kappa=0` and `kappa!=0` have one depressed normal form in a quadratic algebraic differential extension; every Jacobian row except the last integrates; the remaining object is an explicit algebraic curve with one-form `eta` and two polynomial `y=0` boundary equations, whose weighted compactification has exactly one infinity point, the compositional square/cube degeneration. The `(4,6)` family is an exact algebraic survivor, not a closed theorem |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions in the last section: `r,B` are Galois-odd on the nonsquare `L=0` branch rather than “initially rational”; the producer replay does not itself enumerate weighted charts) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (hand Jacobian by `y`-degree for the parent split, UFD valuations in `Kbar[x]`, chain-rule Jacobian of the depressed `(4,6)` form, integration of all eight `z`-rows, `U=A^2-4C` substitution, weighted initial forms in `P(1,2,3,4)`, Galois involution on `Kbar(x)(h)/Kbar(x)`, monic degree-eight resultant, unit product in `Kbar[x]`); a second engine (`sympy==1.14.0` over `Q`, plus a separate Singular 4.4.1 Groebner pass) that does not import the producer replay; unmodified rerun of `verify_46_discriminator.sing` as regression control |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:00:00Z – 2026-08-24T11:18:29Z |
| Python | 3.14.6; `uv run --no-project --with sympy==1.14.0`; Singular 4.4.1 (`lp`/`dp` over `Q`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-sextic-survivor-discriminator-20260824.md` (SHA-256 `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552`)
- `cases/as109_sextic_survivor_discriminator_20260824/verify_46_discriminator.sing` (SHA-256 `d2c29ef530f7bd3aa511d245db2f9fb6eb72cfb001f5dc14d92b74c16345723f`)
- `cases/as109_sextic_survivor_discriminator_20260824/FREEZE.sha256` (SHA-256 `6bdf4935fb32a3506c32a19167c65ecf675f13cefe77ae1ab240510ee5cc99e7`)
- frozen parent `xmodel/as109-sextic-frontier-preflight-20260824.md` (SHA-256 `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4`) and `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` (SHA-256 `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad`). The different-model preflight review has **not** landed. The `(4,6)` leading split consumed from that parent is re-derived below and is not taken on trust. The parent `(5,6)` Pfaffian system is not consumed
- quartic producer `xmodel/as109-quartic-discriminator-gate-20260824.md` (SHA-256 `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`) and its completed different-model review `xmodel/as109-quartic-review-grok-20260824.md` (SHA-256 `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e`); confirmed background only, not used in the `(4,6)` identities

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No Puiseux successor was continued. No enumerator was written or run. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, and `J(f,g)=f_x g_y-f_y g_x`. Actual `y`-degrees are used throughout.

---

## Promotion

**Accept `EXACT ALGEBRAIC SURVIVOR` at the stated `(4,6)` scope.**

- Over any characteristic-zero field, a genuine Keller pair of actual `y`-degrees `(4,6)` is carried, after constant target operations, to the depressed form (2.2) in the working differential field `Kbar(x)` or the quadratic algebraic differential extension `Kbar(x)(h)` with `h^2=H`. Every Jacobian row except the last integrates. The remaining object is the complete intersection `C_(L;k1,k2)` in `A^3_(A,B,U)` with one-form `eta` and both polynomial boundary equations (5.2), (5.3). Its weighted compactification in `P(1,2,3,4)` has exactly one point at infinity, `[r:q:B:U]=[1:0:0:0]`, the compositional square/cube degeneration. For `L=0` the coefficient object is the plane curve (7.4). Two obvious affine-line components of that plane curve are closed. A nonlinear rational coefficient component exists and is **not** a Keller pair.
- The `(4,6)` family is therefore not closed. The fastest next exact calculation is local normalization / Puiseux analysis at that unique infinity point, using both boundary equations and `eta`, separately for `L=0` and `L!=0`.

**Do not promote this to:** a `y`-degree-at-most-six theorem; a stronger AS109 degree floor (five, six, or seven); a found lift or counterexample; a characteristic-zero point; a JC2 decision; a claim that the two line families exhaust (7.4); a claim that every formal branch through `[1:0:0:0]` is eliminated; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim.

**Do not treat the nonlinear control (7.11) as a Keller solution.** For nonconstant polynomial `t` and polynomial `h` the pulled-back last row is a nonconstant polynomial. The control exists only to stop the false inference that (7.4) consists solely of the two closed lines.

**Do not start a `(5,6)` Pfaffian closure as if `(4,6)` were done.**

---

## Quarantine

No result here proves or disproves JC2. Producer PASS strings were not used as evidence; the identities below were re-derived. The sextic-frontier parent is recorded as frozen but its different-model review has not landed: only the `(4,6)` leading split is used, and it is re-proved. The parent `(5,6)` surviving Pfaffian gate is independent and unconsumed. The confirmed quartic theorem is campaign background only. Quintic work is neither consumed nor promoted. Generic uncarried two-layer digit equations and finite-Witt data are absent.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, and a characteristic-zero field calculation for actual `y`-degrees `(4,6)` after the imprimitive split. Arbitrary finite `x`-degree and coefficient coupling are in scope *inside* that pair. The calculation is a family normal form, not an existence theorem: a rational point or trajectory on the coefficient curve is not a Keller pair until both polynomial boundary equations and the nonzero constant last row hold simultaneously. Coprime `(5,6)`, all `y`-degrees `<=5` or `<=6` as a theorem, series lifts, and an arbitrary-AS109 no-go are out of scope. Target `GL_2` and polynomial target shears are automorphy tests over `K` (or `Kbar`), not integral support gauges. The algebraic extension `h^2=H` is a working-field device, not a polynomial source automorphism.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Both `kappa=0` and `kappa!=0` have the common depressed form (2.2) over the working differential field, with `L` constant, `L=0` iff `kappa=0`. Adjoining `h` with `h^2=H` is a quadratic algebraic differential extension with the same constant field `Kbar`. Every hidden division/zero is either excluded by genuine degree four or invertible in characteristic zero. The form is an identity, not a polynomial source change | **CONFIRMED** | a leftover `z^3` in `f` after depressing the degree-four coordinate; `L` nonconstant; `r_f-r_g` not equal to `lambda/12`; constants of `Kbar(x)(h)` larger than `Kbar`; `h=0` smuggled into the branch; `2=0` or `4=0`; using `z=(z-r)/h` as an automorphism of `A^2` |
| 2 | The eight rows of `J_(x,z)` are exactly (3.1). Chain rule `J_(x,y)=h J_(x,z)` holds in the extension. The first five rows integrate to (3.2) with constants `alpha,...,epsilon in Kbar`. `E2=I_2'`, `E1=I_1'` identically after (3.2), including every constant and sign. Last row is `h E0=jbar!=0` | **CONFIRMED** | a leftover `z^8` or missing summand in (3.1); chain-rule extra terms from `h',r'` failing to cancel; a non-integrated residue in `E7..E3`; `I_2'` or `I_1'` mismatch; `alpha` or `epsilon` surviving in `I_2,I_1,E0`; `ker(d/dx)` on the working field larger than `Kbar` |
| 3 | `U=A^2-4C` is an isomorphism of `A^3`. The transformed equations are the complete intersection (4.2)--(4.4), generically a curve (dimension 1 over the parameter field). The last-row form is (4.5). No non-exact intermediate Pfaffian row remains. No case is lost by the `C <-> U` change | **CONFIRMED** | `dU/dC=0`; `J_2` or `J_1` not equal to the substituted `I_2,I_1`; generic rank of `(dJ_2,dJ_1)` dropping to `<=1` identically; an intermediate row among `E7..E1` remaining non-exact; a component of `{I_2=k_2,I_1=k_1}` missed by `U` |
| 4 | After `q=r^2+A/2`, both `y=0` identities are (5.2) and (5.3). `D_0=f(x,0)` and `E_0=G_0-alpha D_0-epsilon` are polynomials in `x`. The quantities `h,r,A,B,C,q,U` need not be polynomial; on the nonsquare `L=0` branch `r,B` live in the quadratic extension (Galois-odd) while `q,A,U,C` descend. Dropping either boundary enlarges the survivor | **CONFIRMED** | a remainder in `f(x,0)-(r B+q^2-U/4)`; a remainder in `g(x,0)-alpha D_0-epsilon-E_0`; `alpha` or `epsilon` surviving in `E_0`; treating the linear change `z=hy+r` as making `r` polynomial; a descent of (5.2) or (5.3) that requires dividing by `h` or `r` |
| 5 | Weights `(r,q,B,U)=(1,2,3,4)` have highest parts (6.1). The only weighted-projective point is `[1:0:0:0]`. It is the compositional degeneration `f_inf=w^2`, `g_inf=w^3`. Charts `q=1`, `B=1`, `U=1` are empty. No extra initial component, and the affine cone is the `r`-axis | **CONFIRMED** | a second common zero of (6.1); `G_inf` vanishing at `U=0,q=r^2,B=-r^3`; a weight-`7` or weight-`8` term of `J_2,J_1` other than those displayed; a chart at `[0:1:0:0]`, `[0:0:1:0]`, or `[0:0:0:1]`; claiming every Puiseux branch through the point is already eliminated |
| 6 | For `L=0` the shifts (7.1)--(7.3) hold and the plane model is (7.4). The first line has `eta=0`. The second line has monic degree-eight eliminant (7.7) and is closed by a unit product, both when `H` is a square and when it is not. The parametrization (7.11) lies on the coefficient curve, pulls back to (7.12), and is a negative control, not a Keller pair | **CONFIRMED** | a leftover `L=0` term after the `X,V` shift; `Phi^2-X^2 R` identically zero as a polynomial; `eta` nonzero on the first line; resultant leading coefficient `0`; a nonconstant unit of `Kbar[x]`; conjugation failing to force `beta=0` on the nonsquare second line; (7.11) giving a nonzero constant last row for polynomial `h,t` |
| 7 | Frozen hashes match, the Singular replay is deterministic and prints the advertised flags, and the only admissible conclusion is an exact algebraic survivor. No degree-`<=6` theorem, no stronger AS109 floor, no lift, no JC2 decision. Smallest next gate: Puiseux / local normalization at `[1:0:0:0]` with both boundaries and `eta` | **CONFIRMED** | a hash mismatch; a hidden enumerator in the case directory; `full_sextic_theorem_proved=true` or `lift_found=true` or `jc2_inference=true`; promoting `(4,6)` as closed; skipping either boundary equation at the next gate |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-sextic-survivor-discriminator-20260824.md` | `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_survivor_discriminator_20260824/verify_46_discriminator.sing` | `d2c29ef530f7bd3aa511d245db2f9fb6eb72cfb001f5dc14d92b74c16345723f` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_survivor_discriminator_20260824/FREEZE.sha256` | `6bdf4935fb32a3506c32a19167c65ecf675f13cefe77ae1ab240510ee5cc99e7` | prompt |
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | producer provenance table |
| `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` | `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad` | producer provenance table |
| `xmodel/as109-quartic-discriminator-gate-20260824.md` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | producer provenance table; confirmed background only |
| `xmodel/as109-quartic-review-grok-20260824.md` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | producer parent table; landed `CONFIRMED`, not consumed |

The case directory contains only `FREEZE.sha256` and `verify_46_discriminator.sing`. No enumerator, exponent rectangle, or AWS helper is present.

Registered command, rerun unmodified:

```sh
Singular -q cases/as109_sextic_survivor_discriminator_20260824/verify_46_discriminator.sing
```

Exit code 0. Exact output:

```text
PASS-SEXTIC-46-SURVIVOR-DISCRIMINATOR
full_sextic_theorem_proved=false
lift_found=false
jc2_inference=false
```

A second engine, written for this review over `Q` with `sympy==1.14.0` and not importing the producer, checked from undifferentiated `f,g`: every displayed row of (3.1); vanishing of `E7..E3` after (3.2); `E2-I_2'` and `E1-I_1'`; the `U`-transforms (4.2)--(4.3); every coefficient of (4.5); both boundary identities; weighted degrees `(4,6,7,8)` of `(F,E,J_2,J_1)` and equality of their top parts with (6.1); `G_inf=-r^6/8` on the rejected branch; all four weighted charts of (6.1); the `L=0` identities (7.3); the type-II resultant; the control (7.11)--(7.12). An independent Singular Groebner pass, also not importing the producer, gave: affine cone of (6.1) of dimension 1 (the `r`-axis); charts `q=1`, `B=1`, `U=1` equal to `(1)`; generic complete-intersection dimension 1 over `Q(L,beta,gamma,delta,k1,k2)`; plane polynomial (7.4) not identically zero, dimension 1, leading term `-8 A X^4`.

A polynomial instantiation with nonconstant `h,r,A,B,C` and the formulas (3.2) reproduced

```text
J_(x,y) = h (I_2' z^2 + I_1' z + E0)
```

identically, with `z=hy+r`. On the control (7.11) with `t=x`, `h=1`, one has `I_2=I_1=0` and `J` equal to the displayed factor (7.12), a nonconstant polynomial of degree 11, hence not a Keller pair. Both boundary polynomials matched `f(x,0)` and `g(x,0)-alpha D_0-epsilon`.

The parent preflight replay was rerun only as integrity control (`verdict = SEXTIC-Y-PREFLIGHT-SURVIVING-PFAFFIAN-GATE`, `lift_found=false`, `jc2_inference=false`). Its `(5,6)` content is not used.

---

## Claim 1 — common depressed normal form

**CONFIRMED.**

For a genuine pair of actual `y`-degrees `(4,6)`, the top Jacobian row is `6 a_4' b_6 - 4 a_4 b_6' = 0`. Unique factorization in `Kbar[x]` and constant target scaling give `a_4=H^2`, `b_6=H^3` with `H in Kbar[x]`, `H!=0`. Write `N=3 a_3 H - 2 b_5`. The next row expands as an identity of derivations

```text
5 a_4' b_5 - 4 a_4 b_5' + 6 a_3' b_6 - 3 a_3 b_6'
  = H (2 H N' - 5 N H').
```

The second engine checked this as a differential-polynomial identity, and also

```text
(N^2 / H^5)' = N (2 H N' - 5 N H') / H^6.
```

Vanishing of the row therefore gives `(N^2/H^5)'=0`. The kernel of `d/dx` on `Kbar(x)` is `Kbar` (Euclidean argument: a ratio `p/q` in lowest terms with vanishing derivative forces `q` to divide `q'` and hence `q` constant in characteristic zero). Thus `N^2=kappa H^5` for a constant `kappa in Kbar`. Hidden division by `H` is polynomial: `N^2-kappa H^5=0` in `Kbar[x]`, and `H=0` is excluded by genuine degree four.

If `kappa!=0`, then `2 v(N)=5 v(H)` at every valuation of `Kbar[x]`. So every valuation of `H` is even, and units of `Kbar` are squares, hence `H=h^2` for some `h in Kbar[x]`, `h!=0`, and `N=lambda h^5` with `lambda in Kbar^*`, `lambda^2=kappa`. The two linear depressions are `r_f=a_3/(4 h^3)` and `r_g=b_5/(6 h^5)`. Direct substitution gives `N=12 h^5 (r_f-r_g)`, so `r_f-r_g=lambda/12`. Dividing by `4` and `6` is legal in characteristic zero; `h=0` is excluded. Depressing the degree-four coordinate by `z=h y+r_f` kills the `z^3` term of `f`. In this variable,

```text
(z - (r_f-r_g))^6 = z^6 - 6(lambda/12) z^5 + ... = z^6 - (lambda/2) z^5 + ...,
```

so the `z^5` coefficient of `g` is the constant `L=-lambda/2!=0`. The opposite square root `h |-> -h` sends `L |-> -L` and `z |-> -z`, an equivalence, not a second branch. Adding a multiple of `f` to `g` cannot change the degree-five coefficient of a degree-six coordinate, so `L` is not a target shear.

If `kappa=0`, then `N=0` and the two linear shifts agree whenever `h` with `h^2=H` is available. If `H` is already a square in `Kbar[x]`, then `h in Kbar[x]` and one works in `Kbar(x)`. If not, adjoin `h` with `h^2=H` to `Kbar(x)` and extend the derivation by `h'=H'/(2h)`. This is a degree-two Galois extension. Constants remain `Kbar`: if `p+q h` has derivative zero with `p,q in Kbar(x)`, linear independence of `{1,h}` forces `p'=0` and `(q^2 H)'=0`; then `p in Kbar`, and `q^2 H` constant with `q!=0` would make `H` a square in `Kbar(x)`, contrary to the adjunction. The common depression is then (2.2) with `L=0`. The linear form is strictly more general than a quadratic-generator ansatz `H y^2+rho y+sigma`: odd residual coupling (the `B z` term) is retained.

In both cases, over the working differential field,

```text
f = z^4 + A z^2 + B z + C,
g = z^6 + L z^5 + P z^4 + Q z^3 + R z^2 + S z + T,
```

with `L` constant. This is an identity in that field, not a claim that `z` is a polynomial coordinate. Target translations of `f` and `g` may still be used later as automorphy tests; they are not used here to drop `C` or `T`.

---

## Claim 2 — Jacobian rows, integrations, first integrals

**CONFIRMED.**

Let `z=h y+r` with `h,r` in the working field. Treating `z` as independent of `x` for the partials of the depressed form, the extra terms from `z_x=h' y+r'` cancel in `J_(x,y)`, and

```text
J_(x,y) = h J_(x,z)
```

holds in the extension (no hypothesis that `h,r` be polynomial). Write `f_x|_z=A' z^2+B' z+C'` and `g_x|_z=P' z^4+Q' z^3+R' z^2+S' z+T'` (`L'=0`). Expanding `f_x g_z - f_z g_x` from undifferentiated coefficients produces degree 7 in `z` and no `z^8` term. The eight coefficients match (3.1) with every summand and sign, including the mixed terms `-2 A P'`, `-B P'`, `5 L C'`, and `E0=-B T'+S C'`.

`E7=6A'-4P'=0` integrates to `P=3A/2+alpha` because the coefficient of `P'` is `-4!=0` and constants of the working field are `Kbar`. Likewise `E6` gives `Q=5 L A/4 + 3B/2 + beta` (`L` constant). Substituting these into `E5,E4,E3` and integrating produces exactly (3.2), including the signs of `-A^3/16` in `T` and `+5 L A^2/32` in `S`. Each of `P',Q',R',S',T'` occurs with coefficient `-4` in the corresponding row, so there is no extra kernel beyond a constant of integration. Characteristic zero makes `2,4,8,16,32` invertible.

After (3.2), the second engine obtained `E2=I_2'` and `E1=I_1'` identically as differential polynomials, with `I_2,I_1` exactly (3.3), (3.4). In particular `alpha` and `epsilon` cancel from `I_2`, `I_1`, and `E0`: `alpha` is the remaining target shear `g |-> g+alpha f`, which preserves `J`, and `epsilon` is a constant added to `g`. Thus a Keller trajectory lies on a fixed level `I_2=k_2`, `I_1=k_1`. The last equation is `h E0=jbar!=0`.

---

## Claim 3 — complete intersection, `eta`, no intermediate Pfaffian

**CONFIRMED.**

The substitution `U=A^2-4C` is inverted by `C=(A^2-U)/4`, with `dU/dC=-4!=0`. It is an isomorphism `A^3_(A,B,C) -> A^3_(A,B,U)` and loses no component, singular or otherwise. Direct substitution of `C=(A^2-U)/4` into `I_2` and `I_1` produces exactly the left-hand sides of (4.2) and (4.3); the `A^2 B` and `A^4` terms cancel with the signs as written. So `{I_2=k_2, I_1=k_1}` is the same scheme as `{J_2=k_2, J_1=k_1}`.

Over the parameter field `Q(L,beta,gamma,delta,k_1,k_2)` the ideal `(J_2-k_2, J_1-k_1)` in `Q(...)[A,B,U]` has dimension 1. Sample gradients at points of level sets (choose `k_1,k_2` to pass through the point) have rank 2, both for `L!=0` and for `L=0`. The object is therefore a complete intersection of expected dimension one, i.e. a curve, for generic parameters. Special parameters can make it a union of lines (still dimension 1) or empty; they cannot make `J_2` a constant polynomial (`-3 B U/4` survives in characteristic not 3) and, for `L=0`, the shifted system `X V=Phi`, `V^2=R` never becomes `0=0` identically in both equations (`R` has an `8 A X(X-beta)` term). There is no dimension jump to a surface among the specializations used in the report.

Chain rule on `C=(A^2-U)/4` gives `C'=(A/2)A'-U'/4`. Substituting into `E0` produces exactly (4.5). The second engine matched all three coefficient functions, including `15 L A^3/64` in `eta_A` and `-15 L A^2/128` in `eta_U`. After (3.2), the Jacobian in `z` is `I_2' z^2 + I_1' z + E0`; on a level trajectory it reduces to `E0=eta(X')`. There is no leftover intermediate row: `E7..E3` determine `P,...,T`, and `E2,E1` are exact. This is the precise difference from the parent `(5,6)` gate, whose corresponding intermediate row `omega` is not closed. (The last-row form `eta` itself is not closed: `d eta != 0` as a 2-form on `A^3`. That is expected and unused.)

Singular points of the level curve, where `dJ_2` and `dJ_1` drop rank, are not claimed to be absent. They are a reason the next gate is a normalization, not a refutation.

---

## Claim 4 — both polynomial boundary equations

**CONFIRMED.**

Set `D_0=f(x,0)`, `G_0=g(x,0)`, `q=r^2+A/2`, and `E_0=G_0-alpha D_0-epsilon`. Then `D_0,E_0 in Kbar[x]`, because `f,g in Kbar[x][y]` and `alpha,epsilon` are constants. The change `A=2q-2r^2` is an isomorphism in `(r,A) <-> (r,q)`; division by 2 is legal in characteristic zero. Exact expansion gives

```text
D_0 = r^4 + A r^2 + B r + C = r B + q^2 - U/4
```

with `C=(A^2-U)/4`, no remainder. Substituting (3.2) into `G_0` and subtracting `alpha D_0+epsilon` produces exactly (5.3), with no `alpha` and no `epsilon`. The second engine checked the identity as a polynomial in `r,q,B,U,L` and the constants. Both displayed equations are polynomial in `(r,q,B,U)` with coefficients in the constant field (and `L`). They therefore descend as algebraic equations; neither requires dividing by `h` or `r`.

What must be polynomial, versus what may live only in the working field:

- Must be polynomial in `x`: `f,g` themselves, hence `D_0` and `G_0`, hence `E_0`.
- Need not be polynomial: `h,r,A,B,C,q,U,P,...,T`. The report correctly refuses to assert that `z` is a polynomial source coordinate.
- On `kappa!=0` (`L!=0`): `h in Kbar[x]` already, and `r=a_3/(4 h^3)` is rational in `Kbar(x)`.
- On `kappa=0` with `H` a square: same, no extension.
- On `kappa=0` with `H` nonsquare: `r=(a_3/(4 H^2)) h` is Galois-odd, `B` is Galois-odd, while `q,A,U,C` are Galois-even and lie in `Kbar(x)`. The product `r B` is even, so (5.2) still takes values in `Kbar[x]`. Section 5's phrase “four initially rational quantities `r,q,B,U`” is therefore slightly too strong on this one branch; it does not feed a later illegal descent, because the nonsquare line-family argument in §7.1 uses the involution `h,r,B |-> -h,-r,-B` rather than rationality of `r,B`. A successor must keep that involution (see non-blocking remarks).

Dropping (5.2) or (5.3) would replace the boundary cover by a strictly larger scheme. Both equations are required.

---

## Claim 5 — unique weighted infinity point

**CONFIRMED.**

Assign weights `(r,q,B,U)=(1,2,3,4)`, hence `A=2q-2r^2` of weight 2. Constants `L,beta,gamma,delta,k_1,k_2` and the polynomial values `D_0,E_0` have weight 0, so they are strictly lower order than the tops of the four equations. Extracting highest-weight parts independently produced degrees `4,6,7,8` and exactly (6.1). In particular the unique weight-7 term of `J_2` is `-3 B U/4`, and the weight-8 part of `J_1` after substituting `A` is `(3/2) r^2 B^2 - (3/2) q B^2 + 3 U^2/32`. Homogenizing with an extra variable `t` of weight 1, the `t=0` fibre is the common zero locus of those four initial forms in `P(1,2,3,4)`.

Case analysis on `J2_inf=0`, i.e. `B=0` or `U=0`:

- `B=0` implies `U=0` from `J1_inf`, then `q=0` from `F_inf`. The point `[r:0:0:0]` is invalid if `r=0` and is `[1:0:0:0]` otherwise (weight of `r` is 1).
- `U=0` and `B!=0` implies `q=r^2` from `J1_inf`. If `r=0` then `G_inf=3 B^2/8!=0`. If `r!=0` then `F_inf` gives `B=-r^3`, and `G_inf=-r^6/8!=0`.

The second engine solved the four affine charts of `P(1,2,3,4)`: `r=1` has the single solution `(q,B,U)=(0,0,0)`; `q=1`, `B=1`, and `U=1` are empty (`GB=(1)`). The affine cone in `A^4` has dimension 1 and, as a set, is the `r`-axis (`q=B=U=0`), i.e. the cone on that unique weighted-projective point. Nilpotents `U^3,B^3` in a Groebner basis record multiplicity at the square/cube degeneration; they do not add reduced points. The points `[0:1:0:0]`, `[0:0:1:0]`, `[0:0:0:1]` are not zeros of (6.1).

At `[1:0:0:0]` one has `q=B=U=0` in the chart `r=1`, so `A=-2 r^2` and `C=A^2/4`, hence

```text
f = z^4 - 2 r^2 z^2 + r^4 = (z^2 - r^2)^2.
```

The weight-6 initial form of `g` is `(z^2-r^2)^3`. Setting `w=z^2-r^2` gives the compositional degeneration `f_inf=w^2`, `g_inf=w^3`. This is why a naive monic elimination in `r` cannot close the family: the leading Jacobian vanishes, and the last row is carried by lower-weight terms, including `L`. The report does not claim that every formal branch through the point is eliminated. Homogenizing generators separately cannot hide an extra infinity point, because `V(in(f_i))` already consists of one point; the actual infinite locus is a subset of that, and an affine curve is never complete, so the locus is exactly that point whenever the boundary cover is one-dimensional.

---

## Claim 6 — aligned plane curve, two lines, control

**CONFIRMED.**

For `L=0`, the translations `X=B+beta`, `V=U-8 gamma/3` are isomorphisms. Direct expansion gives

```text
J_2 - k_2 = (3/4)(Phi(A) - X V),
J_1 - k_1 = (3/32)(V^2 - R(A,X))
```

with `Phi` and `R` exactly (7.1), (7.2). Hence (7.3), and eliminating `V` produces the plane model (7.4). The second engine checked both identities. The polynomial `Phi^2-X^2 R` is not identically zero (leading term `-8 A X^4` over the parameter field) and cuts a dimension-1 scheme in `A^2_(A,X)`. Bidegree at most `(4,4)` is correct (`Phi^2` has `A^4`, `X^2 R` has `A X^4`). The projection `(A,X,V) -> (A,X)` is birational onto its image away from `X=0`; the non-injective locus `X=0`, `Phi=0` is the first line family treated below, or a finite set of points. Using the plane model as the generic aligned survivor is therefore legitimate, provided the spatial cover and both boundaries travel with it.

The first obvious line: `beta=delta=0`, `B=0`, `k_2=0`, `A` free, `V` constant. Then `eta` vanishes identically as a 1-form (all three coefficient functions are zero). This contradicts `h eta(X')=jbar!=0`, independently of whether `H` is a square. Closed.

The second obvious line: `delta=0`, `A=0`, `V=0`, `B` variable, with levels fixed so that (7.3) holds. Then `eta=-(3/4) B(B+beta) dB` exactly. Target translation `f |-> f-c` preserves `V` and may be used to set `C=0`; combined with `V=0` and `A=0` this forces `gamma=U=0`. The two boundaries become `D_0=r^4+B r` and `E_0=r^6+((3/2)B+beta) r^3+(3/8)B^2+(3/4) beta B`. Their resultant in `B` is

```text
(1/8) r^8 - (1/4) beta r^5 - (3/4) D_0 r^4 + E_0 r^2 - (3/4) beta D_0 r - (3/8) D_0^2,
```

which is the advertised monic degree-eight equation after multiplying by `8` (leading coefficient `1`). The second engine matched the resultant identically. At `r=0` it reduces to `-3 D_0^2/8`, so it does not vanish spuriously: if `r=0` and `D_0=0`, `B` is still integral over `Kbar[x]` by the quadratic `B^2+2 beta B-8 E_0/3=0`. Thus `r` is integral over `Kbar[x]`, and so is `B`.

If `H` is a square in `Kbar(x)`, then `h in Kbar[x]` (integrally closed), and `r,B in Kbar(x)` plus integrality give `r,B in Kbar[x]`. The last row is `-(3/4) h B(B+beta) B'=jbar!=0`. In `Kbar[x]` a product equal to a nonzero constant forces every factor to be a unit, hence constant, so `B` is constant and `B'=0`, a contradiction. Zero factors `B=0` or `B=-beta` make `eta=0` already.

If `H` is nonsquare, conjugation of `Kbar(x)(h)/Kbar(x)` sends `h |-> -h`. On this line `A=C=0` and `r` is odd, so `z |-> -z`. Invariance of `g` forces the `z^3` coefficient `Q=3B/2+beta` to be odd, hence `beta=0`, and forces `B` odd. The invariants `K=B^2` and `M=h B` are then Galois-even and integral over `Kbar[x]`, hence lie in `Kbar[x]`, and `M^2=H K`. The last row becomes `-(3/8) M K'=jbar`. Thus `M` is a unit of `Kbar[x]`, so `H` and `K` are units, so `K'=0`, contradicting `jbar!=0`. The second line is therefore closed on both square and nonsquare leading branches. No step uses a nonconstant unit, and the argument is not a Keller construction.

The parametrization (7.11) at `beta=1`, `gamma=delta=k_1=k_2=L=0` satisfies both first-integral equations identically. Its pullback of `eta` is exactly (7.12). For a polynomial `t` of degree `d>=1` the form has degree `12d-1>=11` and cannot be a nonzero constant; an independent instantiation with `t=x`, `h=1` produced `J` equal to that degree-11 polynomial. Constant roots of the displayed factor make `eta=0`. The control is therefore a genuine nonlinear rational component of (7.4) and a genuine failure of the last row for polynomial `h,t`. It is not a lift, not a counterexample, and not a reason to declare (7.4) closed. Any claimed general closure of the aligned branch must handle nonlinear components, not only the two lines.

---

## Claim 7 — hashes, replay, scope, next gate

**CONFIRMED.**

Hashes match the prompt, the freeze file, and the on-disk bytes. The freeze lists exactly the report and the replay. The Singular replay is deterministic over `Q`, contains no support search, and prints `full_sextic_theorem_proved=false`, `lift_found=false`, `jc2_inference=false`. The parent preflight review has not landed; the only parent identity used is the `(4,6)` split, re-proved in Claim 1. Quartic work is background. Quintic work is unused. AWS, Hensel, and finite-Witt data are absent.

The admissible conclusion is exactly the one advertised: an exact algebraic survivor for actual `y`-degrees `(4,6)`, with an explicit curve, one-form, boundary cover, and a unique infinity point. It is not a degree-`<=6` theorem, not a stronger AS109 exclusion, not a lift, and not a JC2 decision.

The smallest valid next gate is the one in producer §10, which this review endorses rather than replacing:

1. homogenize (4.2), (4.3), (5.2), (5.3) with weights `(1,2,3,4)`;
2. compute every Puiseux branch through `[1:0:0:0]`, separately for `L=0` and `L!=0`;
3. pull back `eta` and both boundary polynomials to each branch;
4. reject a branch only if a pole remains in a boundary polynomial or `h eta` cannot be a nonzero constant.

On the nonsquare `L=0` branch, keep the Galois involution (`beta=0`, `r,B` odd, `q,A,U` even) while doing that calculation. Only after every branch is rejected may `(4,6)` be closed and attention move to the parent `(5,6)` Pfaffian system.

---

## Dependency status

| Input | Status | Use in this review |
|---|---|---|
| Sextic-frontier preflight producer | frozen, hashes match | `(4,6)` split re-derived; `(5,6)` Pfaffian unread as a theorem |
| Sextic-frontier preflight different-model review | **has not landed** | not consumed |
| Quartic discriminator + its `CONFIRMED` review | landed | background only; no quartic identity used in the `(4,6)` algebra |
| Quintic-y work | present in the tree | unused, not promoted |
| Hensel / closed-support / carry erratum | landed previously | unused |

This child does not inherit a gap from the missing preflight review, because the only parent identity it needs was re-proved from the leading `(4,6)` Jacobian.

---

## Non-blocking precisions

None of the following changes a numbered verdict.

1. *Galois parity on nonsquare `L=0`.* Section 5's wording “initially rational quantities `r,q,B,U`” is accurate for `L!=0` and for square `H`, and is too strong when `H` is nonsquare: `r` and `B` are odd, `q,A,U,C` even. The same involution, applied globally rather than only on the second line, forces `beta=0` on the whole nonsquare aligned branch (the `z^3` coefficient of `g` must be odd, and `Q=3B/2+beta`). The nonlinear control with `beta=1` therefore cannot live on that Galois eigenspace. A Puiseux successor should impose this at the start of the nonsquare `L=0` case, not rediscover it per component.

2. *Replay coverage.* The producer Singular file checks every displayed coefficient identity it claims, including (6.3), (7.3), (7.7), (7.11), and (7.12). It does not itself enumerate the four weighted charts or run the unit-product argument. Those were filled by the second engine and by hand. This is a coverage remark, not a missing identity.

3. *`eta` is not closed.* The exterior combination `d eta` is nonzero as a 2-form on `A^3_(A,B,U)`. The report never claims otherwise. Exactness is used only for `E2` and `E1`.

4. *Multiplicity at infinity.* A Groebner basis of the initial ideal contains `U^3` and `B^3`. The reduced infinity locus is still one point. Embedded structure is exactly what a local-normalization successor must see.

5. *Plane versus spatial model.* For generic parameters the map from `{XV=Phi, V^2=R}` to the plane curve (7.4) is birational. Along the closed first line it is two-to-one in the sign of `V`. Normalization of the plane curve is an acceptable generic presentation of the aligned survivor only together with `eta` and both boundaries; the spatial complete intersection remains the actual object.

6. *Choice of square root.* `L |-> -L` under `h |-> -h` is an equivalence via `z |-> -z`. It is not a second mismatch branch.

---

## Promotion advice

Accept the file as a completed `(4,6)` *discriminator*, not as a `(4,6)` *closure*.

- Bank it as: exact algebraic survivor; unique infinity point `[1:0:0:0]`; two aligned lines closed; nonlinear coefficient components exist and are not Keller pairs; mismatch `L!=0` retained.
- Do not raise the AS109 correction `y`-degree floor. The confirmed quartic theorem (floor five) and whatever quintic status the campaign later promotes remain the floor-bearing statements. This file does not touch them.
- Do not authorize a `(5,6)` closure attempt that assumes `(4,6)` is empty.
- Do not feed (7.11) into a search for polynomial automorphisms or into an AS109 lift.
- Next bounded calculation, and the only one this review licenses: Puiseux / local normalization at `[1:0:0:0]` with both (5.2), (5.3) and `eta`, split on `L=0` / `L!=0`, with Galois parity on nonsquare `L=0`.

No result in this review proves or disproves JC2.
