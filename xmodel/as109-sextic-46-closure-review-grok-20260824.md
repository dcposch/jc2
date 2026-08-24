# Hostile different-model review — AS109 sextic `(4,6)` local-normalization closure

| Field | Value |
|---|---|
| Claim under review | Under the frozen `(4,6)` normal-form equations, every Puiseux branch over the unique weighted-infinity point is empty, and every polynomial coefficient trajectory has last-row pullback of positive degree or zero. After the now-landed parent reviews this is an exact closure of the genuine `(4,6)` pair, not a `y`-degree-at-most-six theorem, not an AS109 lift obstruction, and not JC2 |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions: the producer still labels the parent `PROVISIONAL`; the replay does not itself enumerate Newton faces or degree cones; the `L!=0` polynomial row “`B,U` with `A` constant” is empty at `A=0`) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (weighted substitution of the four boundary/integral equations, Z-elimination, complete monomial-order lists of the local chart, Q-valuation case analysis, Galois involution on `Kbar(x)(h)/Kbar(x)`, monic quartic and octic resultants, UFD unit products in `Kbar[x]`, integer degree-cone scan); a second engine (`sympy==1.14.0` over `Q`, plus a separate Singular 4.4.1 Groebner pass) that does not import the producer replay; unmodified rerun of `verify_46_local_normalization.sing` as regression control |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:33:00Z – 2026-08-24T11:49:04Z |
| Python | 3.14.6; `uv run --no-project --with sympy==1.14.0`; Singular 4.4.1 (`dp` over `Q`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-sextic-46-local-normalization-gate-20260824.md` (SHA-256 `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac`)
- `cases/as109_sextic_46_local_normalization_20260824/verify_46_local_normalization.sing` (SHA-256 `a705526c12675d7fba0330f9f45d17db34d87a085f877b30bc6d73de81a7e404`)
- `cases/as109_sextic_46_local_normalization_20260824/FREEZE.sha256` (SHA-256 `45134ff283f6cee97030f288ad9a1645d3f00f4b35e85fecf25c6610f1ff0aaa`)
- parent producer `xmodel/as109-sextic-survivor-discriminator-20260824.md` (SHA-256 `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552`) and its landed different-model review `xmodel/as109-sextic-survivor-review-grok-20260824.md` (SHA-256 `4f2c8b6cd1a165ed73dedb0a3fc92256199927961a6c5126afc6689408106c59`); overall `CONFIRMED`
- grandparent producer `xmodel/as109-sextic-frontier-preflight-20260824.md` (SHA-256 `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4`) and its landed different-model review `xmodel/as109-sextic-preflight-review-grok-20260824.md` (SHA-256 `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff`); overall `CONFIRMED`; `(4,6)` split consumed only as re-derived in the survivor review and again below; `(5,6)` Pfaffian unread as a theorem

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer and review artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, and `J(f,g)=f_x g_y-f_y g_x`. Actual `y`-degrees are used throughout. The working field is `Kbar(x)` on the square/mismatch branch, or the single prescribed quadratic extension `Kbar(x)(h)`, `h^2=H`, on the aligned nonsquare branch.

---

## Promotion

**Accept `EXACT CLOSURE OF THE GENUINE (4,6) PAIR` at the stated scope, after its reviewed parent.**

- The parent discriminator is now covered by a landed different-model `CONFIRMED` review, and the grandparent `(4,6)` split is covered by a landed different-model `CONFIRMED` preflight review. The producer’s `PROVISIONAL` / `CONDITIONAL` labels are therefore discharged: every solution of (1.1)–(1.6) over a characteristic-zero polynomial base has vanishing last row or violates a polynomial boundary.
- The mismatch branch `L!=0` has no Puiseux branch over `[1:0:0:0]` and no polynomial coefficient trajectory with nonzero constant Jacobian. The aligned branch is forced to `beta=delta=0`, then to `k2=0`, then to the `V=0` components, all of which die by a monic boundary eliminant plus a unit product (square and nonsquare).
- The `(5,6)` Pfaffian system is untouched. The confirmed quartic floor (correction `y`-degree at least five) is not raised.

**Do not promote this to:** a `y`-degree-at-most-six field theorem; a stronger AS109 degree floor (six or seven); a found lift or counterexample; a characteristic-zero point; a JC2 decision; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim.

**Do not start a search for leftover `(4,6)` formal branches.** The resurrection condition is an error in the reviewed parent reduction to (1.1)–(1.6), in the stated quadratic parity, or in the uniqueness of the weighted-infinity point. None of those was found.

**Smallest valid successor:** the parent `(5,6)` Pfaffian system, from the polynomial primitive recorded in the preflight review, with both polynomial boundaries. Do not treat this file as licensing a `y`-degree-`<=6` theorem once `(5,6)` is touched.

---

## Quarantine

No result here proves or disproves JC2. Producer PASS strings were not used as evidence; the identities below were re-derived. The parent discriminator and the grandparent preflight are recorded as landed `CONFIRMED` and are consumed only for the genuine `(4,6)` normal form, its unique infinity point, and the descent parities. The parent `(5,6)` surviving Pfaffian is independent and unconsumed. The confirmed quartic theorem is campaign background only. Quintic work is neither consumed nor promoted. Generic uncarried two-layer digit equations and finite-Witt data are absent.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, and a characteristic-zero field calculation for actual `y`-degrees `(4,6)` after the imprimitive split and the reviewed normal form. Arbitrary finite `x`-degree and coefficient coupling are in scope *inside* that pair. The admissible theorem is emptiness of that normal-form system, not emptiness of every sextic-`y` Keller pair. Coprime `(5,6)`, all `y`-degrees `<=5` or `<=6` as a theorem, series lifts, and an arbitrary-AS109 no-go are out of scope. Target `GL_2` and polynomial target shears are automorphy tests over `K` (or `Kbar`), not integral support gauges. The algebraic extension `h^2=H` is a working-field device, not a polynomial source automorphism.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The parent depressed form, first integrals, `eta`, both boundaries, and unique weighted-infinity point are covered by landed different-model reviews. Every child local equation is an identity after the substitutions `r=s^{-1}`, `q=Q s^{-2}`, `B=Y s^{-3}`, `U=Z s^{-4}` and after `Z=4(Y+Q^2-d s^4)`; none is inherited from a PASS string | **CONFIRMED** | a parent review still `GAP`/`REFUTED` on claims 1–5; a remainder in `Fh,Gh,J2h,J1h`; a second reduced point of the weight-`(1,2,3,4)` initial forms; `G_inf` vanishing at `U=0,q=r^2,B=-r^3` |
| 2 | For `L!=0`, every rational Puiseux valuation over `[1:0:0:0]` is empty, including identically zero `Q,Y,Z`, ramified local parameters, and leading-coefficient cancellation | **CONFIRMED** | a `J2h` monomial other than `-3YZ/4` of order `<=1`; `b+c!=1` surviving; `b!=c` after (3.2); `2a!=1/2` failing to force `z0=4y0` and `3y0^2`; the order-`3/4` face of `Gh` admitting `q0!=0` |
| 3 | For `L=0` the Newton strata `beta!=0` and `beta=0,delta!=0` have exhaustive tie tables and no missed equal-valuation face; displayed leading coefficients that can vanish are never lowest | **CONFIRMED** | a G0-tie other than the four listed; the `s^4 Q` term lowest at some `(a,b)`; a unique lowest term whose coefficient is forced to zero by the stratum; a grid point with no unique obstruction in `(G0,H2,H1)` |
| 4 | After `beta=delta=0` the shift is (5.2). `k2!=0` has no branch. `k2=0` splits into `B=0` (`eta=0`) and `V=0`; the `A=0` line and the nonlinear `AB^2=theta!=0` component both use both boundaries and produce monic eliminants | **CONFIRMED** | `A/r^2` not tending to `-2`; `v0=4w0` compatible with `v0^2=-16w0^2`; dropping `E` still making `q` integral; the quartic leading coefficient `0`; `BV=0` admitting a mixed germ that is neither `B=0` nor `V=0` |
| 5 | Square/nonsquare descent is valid: Galois parities of `h,r,B`, integrality of `K=B^2` and `M=hB`, unit-product last-row, and hidden zeros. Linear `K` is killed by `M^2=HK`, not by degree counting alone | **CONFIRMED** | a Galois-even part of `B` on the nonsquare branch; `q` integral but not in `Kbar(x)`; a nonconstant unit of `Kbar[x]`; `M=0` or `K=0` sneaking past `theta!=0` and `jbar!=0`; linear `K` with `M` a unit |
| 6 | The polynomial degree cones for `L!=0` and each `L=0` stratum are exhaustive. On every nonconstant cone the claimed top term of `eta` is unique and nonzero. Constants exhaust the residue (`eta=0`) | **CONFIRMED** | a second primitive triple with both `J2` and `J1` tied; a leftover competitor at degree `16n-1`, `12n-1`, `8n-1`, or `3n-1`; `16n-1=0` for an integer `n>=1`; a constant trajectory with `eta!=0` |
| 7 | Frozen hashes match; the unmodified replay returns the advertised flags; the only admissible conclusion is closure of the actual `(4,6)` pair after its reviewed parent | **CONFIRMED** | a hash mismatch; `as109_inference=true` or `jc2_inference=true`; a hidden enumerator; promoting a `y`-degree-`<=6` theorem or a stronger AS109 floor |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a numbered verdict.

---

## Replay and hashes

Frozen child hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-sextic-46-local-normalization-gate-20260824.md` | `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_46_local_normalization_20260824/verify_46_local_normalization.sing` | `a705526c12675d7fba0330f9f45d17db34d87a085f877b30bc6d73de81a7e404` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_46_local_normalization_20260824/FREEZE.sha256` | `45134ff283f6cee97030f288ad9a1645d3f00f4b35e85fecf25c6610f1ff0aaa` | prompt |
| `xmodel/as109-sextic-survivor-discriminator-20260824.md` | `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552` | child freeze and parent freeze |
| `cases/as109_sextic_survivor_discriminator_20260824/verify_46_discriminator.sing` | `d2c29ef530f7bd3aa511d245db2f9fb6eb72cfb001f5dc14d92b74c16345723f` | child freeze |
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | child freeze |
| `xmodel/as109-sextic-survivor-review-grok-20260824.md` | `4f2c8b6cd1a165ed73dedb0a3fc92256199927961a6c5126afc6689408106c59` | landed parent review, `CONFIRMED` |
| `xmodel/as109-sextic-preflight-review-grok-20260824.md` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | landed grandparent review, `CONFIRMED` |

The case directory contains only `FREEZE.sha256` and `verify_46_local_normalization.sing`. No enumerator, exponent rectangle, or AWS helper is present.

Registered command, rerun unmodified:

```sh
Singular -q cases/as109_sextic_46_local_normalization_20260824/verify_46_local_normalization.sing
```

Exit code 0. Exact output:

```text
PASS-SEXTIC-46-LOCAL-NORMALIZATION
mismatch_finite_pole_branches=0
aligned_finite_pole_survivors=0
polynomial_eta_trajectories=0
as109_inference=false
jc2_inference=false
```

The parent discriminator replay was rerun only as integrity control (`PASS-SEXTIC-46-SURVIVOR-DISCRIMINATOR`, `lift_found=false`, `jc2_inference=false`). Its `(5,6)` content is not used.

A second engine, written for this review over `Q` with `sympy==1.14.0` and not importing the producer, checked from the undifferentiated parent equations (2.2), (3.2), (4.2), (4.3), (5.2), (5.3), (4.5): the four weighted-chart identities; uniqueness of `[1:0:0:0]` including `G_inf=-r^6/8`; every monomial order of `Fh,Gh,J2h,J1h`; the mismatch-face identities (3.4) and `y0 z0=-5L/3`; aligned elimination (4.1)–(4.3); the shifted curve (5.2); the `k2!=0` face identity; the monic quartic (5.9) and the monic line octic (5.6); `eta` on `V=0` and on `B=0`; all three nonzero leading coefficients of Section 6; `eta` reconstructed from `E0=-B T'+S C'` after `C=(A^2-U)/4`; both polynomial boundaries. An independent Singular Groebner pass, also not importing the producer, gave: charts `q=1`, `B=1`, `U=1` equal to `(1)`; affine cone of the initial forms of dimension 1; `G_inf` rejection `0`; shifted identities `0`; `3*relsub+quartic=0`; `8*lineRes-lineMonic=0`.

A Newton-order scan of `(v(Q),v(Y))` over all positive rationals of denominator at most 12, together with the three identically-zero loci, found **zero** points at which `(G0,H2,H1)` simultaneously lack a unique forced-nonzero leading term, on each of the strata `beta!=0` and `beta=0,delta!=0`. An integer degree-cone scan with degrees `1..30` (resp. `1..24`) produced a unique primitive triple in each advertised nonconstant class: `(4,5,7)` for `L!=0` with `A,B,U` all nonconstant; `(1,1)` for `B,U` with `A` constant; `(4,3,5)` for `L=0,beta!=0`; `(4,1,3)` for `L=0,beta=0,delta!=0`.

---

## Claim 1 — parent coverage and local substitutions

**CONFIRMED.**

The grandparent preflight review is overall `CONFIRMED`. Its claims 2–3 are exactly the `(4,6)` split `a_4=H^2`, `b_6=H^3`, `N^2=kappa H^5`, with `kappa=0` aligned and `kappa!=0` a constant depression mismatch `L=-lambda/2`. The parent discriminator review is overall `CONFIRMED`. Its claims 1–5 are exactly the common depressed form (2.2), the eight Jacobian rows and two first integrals, the isomorphism `U=A^2-4C`, the last-row form `eta`, both polynomial boundaries, and uniqueness of the weighted-infinity point `[r:q:B:U]=[1:0:0:0]` in `P(1,2,3,4)`. Those reviews have landed as uncommitted artifacts on the same charged basis as the child. The child’s `PROVISIONAL` parent label is therefore historically accurate at freeze time and mathematically discharged now.

The child’s (1.1)–(1.6) were re-derived from the parent equations, not taken from the replay:

- `C=(A^2-U)/4` into `I_2,I_1` produces (1.1), (1.2) identically.
- `E0=-B T'+S C'` after (3.2) and the same substitution produces (1.6) identically, including `15 L A^3/64` in `eta_A` and `-15 L A^2/128` in `eta_U`.
- Sequential substitution `C=(A^2-U)/4`, `A=2q-2r^2` produces `D_0=r B+q^2-U/4` and the displayed (1.4).

The chart (2.2) is the standard affine chart `r=1` of `P(1,2,3,4)` with `s=r^{-1}`. Clearing weights `4,6,7,8` on `(F,E,J_2,J_1)` produces exactly `Fh,Gh,J2h,J1h`. These are the full equations, not a truncation. Because `[1:0:0:0]` is the unique infinity point, any pole of any of `r,q,B,U` at a finite base place has `Q,Y,Z` of strictly positive valuation: a valuation `0` would be a different reduced point of the initial forms, and a negative valuation would live in a chart `q=1`, `B=1`, or `U=1`.

Uniqueness of that point was re-proved independently of the parent prose. Highest weighted parts are (2.1) as displayed. `J2_inf=0` is `B=0` or `U=0`. If `B=0`, then `J1_inf` forces `U=0` and `F_inf` forces `q=0`, giving `[1:0:0:0]`. If `U=0` and `B!=0`, then `J1_inf` forces `q=r^2`; `r=0` gives `G_inf=3 B^2/8!=0`; `r!=0` gives `B=-r^3` and `G_inf=-r^6/8!=0`. Independent Groebner: charts `q=1`, `B=1`, `U=1` are `(1)`; the affine cone has dimension 1 (the `r`-axis as a set, with nilpotents `U^3,B^3` recording multiplicity at the square/cube degeneration). No extra reduced infinity point.

The aligned substitution `Z=4(Y+Q^2-d s^4)` is the identity `Fh=0` and loses no germ: `Z` is determined. Clearing harmless nonzero scalars `8,2,2` produces (4.1)–(4.3) identically. After this substitution the `QY` terms of `Gh` cancel, which is why `G0` is cubic in `(Q,Y)` rather than retaining `3 Q Y/2`.

---

## Claim 2 — `L!=0` valuations

**CONFIRMED.**

Normalize the place so that `v(s)=1`. This covers ramified local extensions: if `s=u t^e` with `u` a unit, the valuation `v_t/e` still has `v(s)=1` and the remaining valuations lie in `Q_{>0}`. Algebraic Puiseux series have rational valuations, so there is no leftover real-but-irrational face.

The complete monomial list of `J2h` has a unique term of `s`-order `0`, namely `-3 Y Z/4`. Every other term has `s`-order at least `1`. The unique term of `s`-order `1` with no `Q,Y,Z` is `-5 L s/4`. Every other `s`-order-`1` term carries a positive power of `Q`, `Y`, or `Z`, hence has order strictly greater than `1` once `a,b,c>0`. Therefore the only way to cancel `-5 L s/4` is `b+c=1` with `y0 z0=-5 L/3`. In particular `Y` and `Z` cannot vanish identically (`b+c=infty` would leave `-5 L s/4` unique), and `L!=0` forces `y0 z0!=0`.

After (3.2) the only possible lowest terms of `J1h` are `3 Y^2/2` (order `2b`) and `3 Z^2/32` (order `2c`). All other monomials have order `> min(2b,2c)`: `b+1>2b` because `b<1`; `a+2b>2b`; `b+c+1=2>1>=min(2b,2c)`; `2c>2b` if `b<c`. If `b<c` then `3 y0^2/2` is unique and `y0=0`, contradicting (3.2). If `c<b` then `z0=0`, same contradiction. Hence `b=c=1/2`. At this value the two quadratic terms of `J1h` tie at order `1` and no third term joins them (`a>0`). That tie is *solvable* over `Kbar` (`z0=\pm 4 i y0` together with `y0 z0=-5 L/3`), so `J1h` alone does not close the branch: `Fh` and `Gh` are required.

`Fh` at orders `1/2` and `4`: if `2a<1/2` then `Q^2` is unique, `q0=0`, contradicting a finite valuation. If `Q` vanishes identically, or if `2a>1/2`, then `z0=4 y0`, and the order-`1` part of `J1h` becomes `3 y0^2!=0`. Hence `a=1/4`. At `(a,b,c)=(1/4,1/2,1/2)` the complete list of `Gh` monomials has lowest order `3/4`, achieved exactly by `Q^3`, `3 Q Y/2`, and `-3 Q Z/8`. The order-`1/2` equation of `Fh` and the order-`3/4` equation of `Gh` are (3.4). Here `q0!=0` by definition of `a=1/4`. Subtracting the parenthesized relations produces `(4 y0-z0)/8=0`, hence `z0=4 y0`, hence `q0^2=0` from `Fh`. Contradiction.

Zero/infinite valuations of `Q,Y,Z` are included: identically zero `Y` or `Z` kills `J2h`; identically zero `Q` forces `z0=4 y0` and then `3 y0^2` in `J1h`. Valuation `0` is a different reduced infinity point, empty by Claim 1; independently, a lowest `Q^3` or `Y^2` of order `0` would already be unique in the local chart. Characteristic zero makes `2,3,4,5,8` invertible; no displayed leading coefficient of this face can vanish without forcing `L=0` or `y0=0`.

Thus `L!=0` has no branch above (2.1).

---

## Claim 3 — `L=0` Newton strata

**CONFIRMED.**

After `Z`-elimination the lowest candidates of `G0` for `beta!=0` are only `(3a,2b,3)`. Every other monomial is strictly above this set: `a+3>3`, `b+3>3`, `a+4>4`, `5>3`, `6>3`. The same holds in `H2`. `H1` has no naked `s^3` term; its beta terms start at `b+3`. A unique lowest term cannot vanish: `4 q0^3=0`, `-3 y0^2=0`, and `4 beta=0` are all illegal on this stratum (finite valuation means `q0,y0!=0`). So only ties of `G0` can survive, and there are exactly four:

| G0 tie | `H2` | `H1` | obstruction |
|---|---|---|---|
| `b=3a/2`, `a<1` | `2b=3a` unique (`3a<7a/2`, `3a<3`) | — | `-6 y0^2` |
| `a=1`, `b>3/2` | order-three unique | — | `3 beta` |
| `b=3/2`, `a>1` | `2b` ties `s^3` (`-6 y0^2+3 beta` *can* vanish) | `2b=3` unique | `6 y0^2` |
| `a=1`, `b=3/2` | same tie as the previous row | `2b=3` unique | `6 y0^2` |

The third row is the one place a displayed `H2` coefficient can vanish (`y0^2=beta/2`); `H1` still has unique `6 y0^2`. Identically zero `Q` or `Y` is the same unique-term obstruction: `Y=0` leaves `3 beta s^3` unique in `H2`; `Q=0` leaves `6 Y^2` unique in `H1` at the remaining tie `b=3/2`; both zero leaves `4 beta s^3` unique in `G0`. No other equal-valuation face exists among three real numbers `(3a,2b,3)`.

For `beta=0`, `delta!=0` the G0 candidates are `(3a,2b,4+a,5)`. The term `s^4 Q` is *never* among the lowest: `4+a<=3a` forces `a>=2` and `4+a<=5` forces `a<=1`. This is why a vanishing of `8 gamma+12 d` cannot open a new face: that coefficient multiplies a non-lowest monomial. Likewise `Y s^4` in `H2` would need `b>=4` and `b<=1`. The term `e s^6` would need `5>=6`. Ties of the remaining triple `(3a,2b,5)` are:

| G0 tie | obstruction |
|---|---|
| `b=3a/2`, `a<5/3` | `2b` unique in `H2` (`-6 y0^2`) |
| `a=5/3`, `b>5/2` | order-five unique in `H2` (`-4 delta`) |
| `b=5/2`, `a>5/3` | `2b=5` unique in `H1` (`6 y0^2`) |
| `a=5/3`, `b=5/2` | `H2` may cancel (`-6 y0^2-4 delta`); `H1` has unique `6 y0^2` |

Again the endpoint where a displayed `H2` coefficient can vanish is killed by `H1`. Identically zero series are immediate. A second-engine scan of all positive rationals of denominator `<=12`, plus both infinities, returned empty survivor sets on both strata. That scan is a regression, not the proof; the proof is the combinatorial tie list above, which does not depend on a height bound.

Consequently every aligned branch satisfies `beta=delta=0`.

---

## Claim 4 — `beta=delta=0` shift, `k2`, and the nonlinear component

**CONFIRMED.**

The translations `X=B+beta`, `V=U-8 gamma/3` are isomorphisms. At `beta=delta=0` they reduce (7.3) to

```text
B V = -4 k2/3,
V^2 = 8 A B^2 + (32/3)(k1 + 2 gamma^2/3),
```

which is (5.2). Independently `I_2=(3/4)(Phi-X V)` and `I_1=(3/32)(V^2-R)` at `L=0`, with `Phi=-4 k2/3` after `beta=delta=0`.

If `k2!=0` and `v(r)=-n<0`, then `v(B V)=0` so `v(V)=-v(B)`. Write `beta_B=v(B)`. The first boundary and uniqueness of infinity give `v(q)>=-n/4` and `A/r^2 -> -2` (because `v(q)>=-n/4>-2=v(r^2)`). Balancing `v(V^2)=-2 beta_B` against `v(A B^2)=-2n+2 beta_B` forces `beta_B=n/2`. The constant term of (5.2) cannot dominate: that would require `v(A B^2)>=0`, hence `beta_B>=n`, contradicting the balance. Leading coefficients then satisfy `v0^2=-16 w0^2` with `w0` the leading coefficient of `r B`.

If `v(q)>-n/4`, the first boundary gives `v0=4 w0`, hence `16 w0^2=-16 w0^2`, so `w0=0`, illegal. Over `Kbar` the relation `v0^2=-16 w0^2` is solvable (`v0=\pm 4 i w0`), but it is *not* compatible with `v0=4 w0`. If `v(q)=-n/4`, the two boundaries’ leading forms are exactly (5.4). The `B^2` term of `E` has valuation `n` (after `n=1`, valuation `1`) strictly above `-3/4`, so it is not in the face. Since `q0!=0`, subtracting produces `v0=4 w0` and then `q0^2=0`. Same mismatch as Claim 2. Both boundaries are used at equality; `V^2` is used in the strict case. No branch.

If `k2=0` then `B V=0` as an identity in the coefficient function field. A Puiseux ring is a UFD, so on each irreducible germ either `B=0` or `V=0` identically. A mixed germ would still have product identically zero and would split.

If `B=0`, then (1.6) at `L=beta=delta=0` has all three coefficient functions zero, so `eta=0`, contradicting (1.5).

If `V=0`, then `theta=A B^2` is the constant `-(4/3)(k1+2 gamma^2/3)`. If `theta=0` the components are `B=0` (already dead) and `A=0`. On `A=0` one has `q=r^2` and `U=8 gamma/3`, and the two boundaries become

```text
P - r^4 - r B = 0,          P=D+2 gamma/3,
E = r^6 + (3/2) r^3 B + (3/8) B^2.
```

The `gamma` terms in `E` cancel. The resultant in `B` is `(1/8)` times the monic octic (5.6); leading coefficient `1`. The second boundary is monic quadratic in `B` after multiplying by `8/3`. At `r=0` one has `P=0` and `B^2=8 E/3`. Hence `r` and `B` are integral over `Kbar[x]`.

If `theta!=0` set `K=B^2`, `w=r B`, `P=D+2 gamma/3`. Both boundaries plus `q=r^2+A/2` become (5.8):

```text
w = P - q^2,
E = -q^3/2 + 3 P q/2 + 3 K/8,          w^2 = q K - theta/2.
```

The first is `F`; the second uses `U=8 gamma/3` to cancel the `gamma q` terms against `-3 q U/8`; the third is `w^2=r^2 K=(q-A/2)K=q K-theta/2`. Eliminating `K,w` produces the monic quartic (5.9). Independently `3(w^2-q K+theta/2)+`quartic`=0` after the substitutions, and the leading term is `q^4`. So `q` is integral, hence so is `K=(8 E+4 q^3-12 P q)/3`. Dropping either boundary leaves a dimension too large to force this monic relation: the nonlinear component genuinely uses both.

On every `V=0` component, `U` is constant so `U'=0`, and `eta_A=B(3U/16-gamma/2)` vanishes at `U=8 gamma/3`. Thus `eta=-(3/4) B^2 dB` identically, which is (5.10).

---

## Claim 5 — square/nonsquare descent

**CONFIRMED.**

The involution (1.7) is the Galois action of `Kbar(x)(h)/Kbar(x)` on the nonsquare aligned branch, supplied by the common depression, not by the finite boundary system. Because `f,g` lie in `Kbar[x][y]` and conjugation sends `z=h y+r` to `-z` with `y` fixed, even-in-`z` coefficients of `f,g` are Galois-even and odd-in-`z` coefficients are Galois-odd. Constants are even, so:

- `L` constant and odd forces `L=0` (already the aligned branch);
- `Q_3=3 B/2+beta` odd and `B` odd force `beta=0`;
- `S=3 A B/4+alpha B+delta` (after `L=beta=0`) odd forces `delta=0`;
- `B V=-4 k2/3` is odd equal to an even constant, so `k2=0`.

This is (6.1). On the nonsquare aligned branch one therefore jumps directly to the components of Claim 4; the `beta!=0` and `delta!=0` Newton strata are empty on that Galois eigenspace. The quantities `q,A,U,C` are even, so they lie in `Kbar(x)`; `r,B,h` are odd.

After Claim 4, `q` satisfies a monic equation over `Kbar[x]` and is Galois-even, hence `q in Kbar(x)`. The integral closure of `Kbar[x]` in `Kbar(x)` is `Kbar[x]`, so `q in Kbar[x]`. Then `K=B^2` is a polynomial in `q,E,P`, hence `K in Kbar[x]`. On the square branch `B in Kbar(x)` and `B^2 in Kbar[x]` force `B in Kbar[x]` (UFD: a denominator dividing the square of the numerator is a unit). On the nonsquare branch `M=h B` is Galois-even, and `M^2=H K in Kbar[x]`, so `M` is integral over `Kbar[x]` and lies in `Kbar(x)`, hence `M in Kbar[x]`.

Last row: `h eta=-(3/8) M K'` on the nonsquare side (because `K'=2 B B'` converts `-(3/4) h B^2 B'` into `-(3/8) M K'`), and `-(3/4) h B^2 B'` on the square side. Units of `Kbar[x]` are `Kbar^*`. A product equal to a nonzero constant forces every factor to be a unit.

Hidden zeros: `M=0` is `h=0` or `B=0`, excluded by genuine degree four and by `theta=A B^2!=0` (or by `eta=0` on `B=0`). `K=0` is `B=0` again. `H=0` is genuine degree four.

The one trap that degree counting does *not* kill by itself is linear `K` on the nonsquare side: `deg(M K')=deg M+deg K-1` can vanish with `M` constant and `K` linear. That case is still illegal. `M` a unit and `M^2=H K` would make `H K` a unit, hence `K` a unit, contradicting `deg K=1`. Equivalently `H=M^2/K` would fail to lie in `Kbar[x]`. Equivalently, if `K` divides `M^2` in `Kbar[x]` with `M` nonconstant, then `deg H=2 deg M-1` is odd, so `H` is not a square. The producer’s unit-product-plus-`M^2=HK` argument is the right one; a pure degree count on `M K'` would have been a gap, and that is not the argument used.

On the square side, `deg(h B^2 B')=deg h+3 deg B-1` is never zero for `deg B>=1` (already `>=2` when `h` is constant and `B` is linear). The unit product is still valid and is what the producer writes. The `A=0` line after (5.6) is the same last-row form, so the same descent applies.

---

## Claim 6 — polynomial degree cones and the last-row residue

**CONFIRMED.**

Finite poles being empty, `L!=0` has `h in Kbar[x]` by the parent UFD relation, and `r,q,B,U,A` have no finite poles, hence are polynomials. The last row is then a product of polynomials, so `h` and the pullback of `eta` would both have to be nonzero constants. It remains to classify polynomial `(A,B,U)`.

The top-degree supports of `(J2,J1)` are (6.2). Every structural leading coefficient of those four-plus-four monomials is nonzero for `L!=0` (`5L/32`, `-5L/16`, `5L/8`, `-3/4` and `-5L/32`, `-3/4`, `-5L/16`, `3/32`). An integer scan of `a,b,u in {1,...,30}` found a unique primitive triple at which both maxima are achieved at least twice: `(deg A, deg B, deg U)=(4n,5n,7n)`. Direct solution of the two leading equations on that triple recovers (6.3). The unique degree-`16n-1` contribution to `eta` is `eta_A A'`: `eta_B B'` and `eta_U U'` have degree `15n-1`. Its coefficient is `15 L a0^3/64+3 b0 u0/16=35 L a0^3/128!=0` on (6.3). For integer `n>=1` one has `16n-1>=15!=0`.

Subsets:

- `A` nonconstant, `B` constant: cancelling `A^3` in `J2` requires nonconstant `U` with `u=2a`, after which `U^2` is unique in `J1`. Scan: no tied-tied pair.
- `U` constant, `A,B` nonconstant: `J2` forces `3a=2b`, then `A B^2` is unique in `J1`. Scan empty.
- Lone nonconstant `A`, `B`, or `U`: unique `A^3`, unique `B^2`, unique `U^2` respectively.
- `A` constant, `B` and `U` nonconstant: `J2` forces equal degrees `(n,n)`, which is the second row of the table. The `J1` leading then forces the specific constant `A=-25 L^2/96`. At `A=0` that leftover is `-25 L^2 b0^2/128!=0`, so identically zero `A` is *not* in this row (non-blocking precision below). On the row, `-3 B^2 B'/4` is the unique degree-`3n-1` term of `eta` (`eta_U U'` has degree `2n-1`), and `3n-1>=2`.
- Constants: `A'=B'=U'=0`, so `eta=0`.

For `L=0`, use `X=B+beta`, `V=U-8 gamma/3`. If `beta!=0` and `A` nonconstant, the only integer solution of `x+v=2a` and `2v=a+2x` is `(4n,3n,5n)`. Lower terms of `R` (`delta X`, constants) never tie both equations at another primitive triple; a scan of degrees `1..24` returned only `(4,3,5)`. The unique degree-`12n-1` coefficient of `eta` is `3 X0 V0/16+3 beta A0^2/8=15 beta A0^2/32!=0`. Competitors `eta_B B'` and `eta_U U'` have degree `9n-1`.

If `beta=0`, `delta!=0`, the only solution of `x+v=a` and `2v=a+2x` is `(4n,n,3n)`. Scan unique. Unique degree-`8n-1` coefficient `3 X0 V0/16+delta A0/2=3 delta A0/4!=0`.

If `A` is constant and `beta!=0`, `Phi` is constant. A nonzero constant forces `X,V` constant. `Phi=0` forces `X=0` or `V=0`, both of which make the remaining equation algebraic of positive degree in the leftover variable unless one specialises further to constants, except the line `A=V=delta=0` already closed in the parent (and here `eta=-3 X(X-beta) dX/4` has degree `3 deg X-1`, never a nonzero constant). If `beta=delta=0`, then `X V` is constant: a nonzero constant freezes `X,V` and then `A`; the zero-product components are those of Claim 4, with pullback `0` or degree `3 deg(B)-1`.

Constants therefore exhaust the residue of every cone: the only way to get a degree-zero pullback is `A,B,U` constant, which gives `eta=0`, or a unit-product degeneration already killed in Claim 5.

---

## Claim 7 — hashes, replay, dependencies, scope

**CONFIRMED.**

Hashes match the prompt, the freeze file, and the on-disk bytes. The freeze lists the child report, the child replay, the parent discriminator, the parent replay, and the grandparent preflight. The case directory contains only those two child files. The Singular replay is deterministic over `Q`, contains no support search, and prints `as109_inference=false` and `jc2_inference=false`. It verifies the weighted chart, the unique-infinity rejection, aligned elimination, both leading-face identities, the shifted curve, the monic quartic, the line resultant, restricted `eta`, and the three leading `eta` coefficients of Section 6. It does not enumerate Newton faces or degree cones; those were filled by the second engine and by the case analysis above.

The admissible conclusion is exact closure of the genuine `(4,6)` pair after its reviewed parent. It is not a `y`-degree-at-most-six theorem (the coprime `(5,6)` Pfaffian remains), not a stronger AS109 exclusion, not a lift, and not a JC2 decision. The confirmed quartic theorem still supplies the AS109 correction-degree floor of five; this file does not raise it.

---

## Dependency status

| Input | Status | Use in this review |
|---|---|---|
| Sextic-frontier preflight producer + landed `CONFIRMED` review | frozen, hashes match; review landed | `(4,6)` split recorded as covered; re-used only as already re-derived in the parent discriminator review; `(5,6)` unread as a theorem |
| Sextic-survivor discriminator producer + landed `CONFIRMED` review | frozen, hashes match; review landed | normal form (1.1)–(1.6), unique infinity, and Galois parities; child equations re-derived independently |
| Quartic discriminator + its `CONFIRMED` review | landed | background only; no quartic identity used in the `(4,6)` algebra |
| Quintic-`y` work | present in the tree | unused, not promoted |
| Hensel / closed-support / carry erratum | landed previously | unused |

The child producer froze the parent as `PROVISIONAL`. That label is now obsolete: both parent different-model reviews have landed `CONFIRMED` on the same charged basis. No numbered child claim inherits a parent gap.

---

## Non-blocking precisions

None of the following changes a numbered verdict.

1. *Producer still says `PROVISIONAL`.* Historically correct at freeze time. After the two landed parent reviews and this child review, the closure is actual, not conditional. A later freeze may relabel the parent status; no identity changes.

2. *Replay coverage.* The producer Singular file checks every displayed coefficient identity it claims. It does not enumerate the Newton fan of `(G0,H2,H1)` or the degree cones. Those were filled here. Same coverage remark as in the parent discriminator review, not a missing identity.

3. *`A=0` is not in the `L!=0` second polynomial row.* With `A` identically zero and `deg B=deg U=n`, the `J2` relation `u0=5 L b0/6` leaves a `J1` leading term `-25 L^2 b0^2/128!=0`. The table’s phrase “`B,U` with `A` constant” should be read as “`A` a specific nonzero constant `-25 L^2/96`”. The empty `A=0` case does not create a constant-`eta` trajectory.

4. *Nilpotents at infinity.* The initial ideal contains `U^3` and `B^3`. The reduced infinity locus is still one point. Local analysis in the chart `r=s^{-1}` sees that multiplicity and kills every formal branch through it.

5. *Linear `K` on the nonsquare side.* Degree of `M K'` can vanish for linear `K`. The producer does not rely on that degree: `M^2=H K` with `M` a unit forces `K` a unit. Recorded in Claim 5 because it is the only unit-product step that is not redundant with a degree count.

6. *Choice of square root.* `L |-> -L` under `h |-> -h` is an equivalence via `z |-> -z`. It is not a second mismatch branch. Already in the parent review.

---

## Promotion advice

Accept the file as a completed `(4,6)` *closure*, after its reviewed parent, not as a `y`-degree-at-most-six theorem.

- Bank it as: every solution of the frozen `(4,6)` normal-form equations (1.1)–(1.6) over a characteristic-zero polynomial base has zero last row or violates a polynomial boundary; mismatch `L!=0` has no Puiseux branch at `[1:0:0:0]`; aligned poles die by Newton strata then a monic boundary eliminant; polynomial trajectories have last-row pullback of positive degree or zero.
- Do not raise the AS109 correction `y`-degree floor. The confirmed quartic theorem (floor five) remains the floor-bearing statement until `(5,6)` and the divisible shears into the quintic range are separately reviewed and promoted.
- Do not authorize a claim that every sextic-`y` Keller pair is an automorphism.
- Do not feed the closed `(4,6)` system into a search for polynomial automorphisms or into an AS109 lift.
- Next bounded calculation, and the only one this review licenses: the parent `(5,6)` Pfaffian, from the polynomial primitive already recorded in the preflight review, with both polynomial boundaries.

No result in this review proves or disproves JC2.
