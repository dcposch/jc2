# Hostile different-model review — AS109 QUARTIC-Y NO-GO

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero field theorem: every Keller pair with both `y`-degrees `<=4` is a polynomial automorphism; hence no exact `det J=1` lift of the AS109 seed has both correction `y`-degrees at most four |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions in the last section; algebraic closure is a convenience, not a load-bearing extra hypothesis) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (hand Jacobian by `y`-degree and by the five `z`-rows, Wronskian / logarithmic derivative in `K(x)`, UFD valuations in `K[x]` and in `Kbar[x]`, integral closure of a PID, chain-rule Jacobian of the depressed `(3,4)` form, monic degree-ten eliminant); a second sparse engine over `Q` with `Fraction` coefficients that does not import the producer replay; unmodified rerun of `verify_quartic_no_go.py` as regression control; banked Hensel lemma as previously dual-confirmed, rechecked on residue balls rather than marked sections |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T10:22:00Z – 2026-08-24T10:32:37Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-quartic-discriminator-gate-20260824.md` (SHA-256 `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`)
- `cases/as109_quartic_discriminator_20260824/verify_quartic_no_go.py` (SHA-256 `84fc5c3197490a405955220f95ca6f1777b0b47cc124b3763dbe158375e2e35e`)
- `cases/as109_quartic_discriminator_20260824/FREEZE.sha256` (SHA-256 `7f9b4c6795c74531b0fea9204133565d925427c5ce82347624ec3ee89d1b914a`)
- cubic parent `xmodel/as109-cubic-coupling-gate-20260824.md` (SHA-256 `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820`) and its different-model review `xmodel/as109-cubic-review-grok-20260824.md` (SHA-256 `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef`); re-proved here, not consumed as a promotion dependency
- quadratic parent `xmodel/as109-quadratic-coupling-gate-20260824.md` (SHA-256 `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1`) and `xmodel/as109-quadratic-review-grok-20260824.md` (SHA-256 `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2`); earlier context only
- Hensel noninjectivity in `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and its different-model review `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`) and `xmodel/as109-carry-erratum-review-grok-20260824.md` (SHA-256 `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212`), only to confirm Hensel independence from digit bookkeeping
- local primary/secondary priority notes: `papers/paper2/PRIORITY.md`, `papers/paper2/SCOPE.md` (Magnus 1955 read in full locally; Appelgate--Onishi 1985 and Nowicki--Nakai 1988 flagged paywalled / unresolved)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No quintic or higher `y`-degree family was searched. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, `J(f,g)=f_x g_y-f_y g_x`, and `p=109`.

---

## Promotion

**Accept `QUARTIC-Y NO-GO` at the stated scope.**

- Over any characteristic-zero field, every Keller pair with both coordinates of `y`-degree at most four is a polynomial automorphism of `A^2_K`.
- There is therefore no exact `Z_{109}` polynomial lift of the seed `(x-x^{109},y)` with `det J=1` whose two correction polynomials both have `y`-degree at most four.

**Do not promote this to:** a quintic or higher `y`-degree statement; nonexistence of an arbitrary finite-support AS109 lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim for the field theorem.

**Keep `CLOSED-SUPPORT + UNIT-L` as a conditional resurrection target**, now with the necessary constraint that the section allow `y`-degree at least five in one correction. Whether any such coupled block closes remains open. This file licenses no quintic grammar and no support search.

---

## Quarantine

No result here proves or disproves JC2. Producer JSON strings `PASS-QUARTIC-Y-NOGO-CONTROLS` and `NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-4` were not used as evidence; the identities below were re-derived. The cubic parent is recorded as landed `CONFIRMED` and is not consumed: the quartic writeup repeats the degree-at-most-three reduction it needs, and this review re-derives those cubic identities. The quadratic parent is context only. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed exact identity that Hensel consumes. Priority is quarantined from the mathematical verdict.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_{109}` for the lift, and a field theorem over an arbitrary characteristic-zero `K` (applied at `K=Q_{109}`). Arbitrary finite `x`-degree, support, and coefficient coupling are in scope *inside* both `y`-degrees `<=4`. Quintic and higher `y`-degree, series lifts, and an arbitrary-AS109 no-go are out of scope. GL2 target normalization and polynomial target shears are used only as automorphy tests over `K` (or `Kbar`); they are not integral support gauges.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | All actual top-degree patterns for `deg_y f, deg_y g <=4` reduce, over `K` and without algebraic closure, to the cubic base or to a genuine `(3,4)` pair: equal-degree Wronskian plus constant target `GL_2`; zero/affine forcing `deg_y g=1`; `(1,4)` shear `g-k f^4`; `(2,4)` shear `g-k f^2`. Cubic base either correctly re-proved or consumed only in its confirmed scope | **CONFIRMED** | a leftover `y^7` term from lower coefficients; `2=0` or `4=0`; kernel of `d/dx` on `K(x)` larger than `K`; `a_1=0` or `a_2=0` admitting nonzero `b_4`; `k f^4` or `k f^2` of `y`-degree `>4`; a missed leading pattern; cubic `(2,3)` emptiness failing |
| 2 | In genuine `(3,4)`, `[y^6]J=4 a_3' b_4-3 a_3 b_4'` and `[y^5]J=3 a_3' b_3+4 a_2' b_4-3 a_3 b_3'-2 a_2 b_4'`; UFD valuations give `a_3=alpha_0 h^3`, `b_4=beta_0 h^4`; after scaling, the depression invariant is `4C/h^2-3E/h^3` with exact shift `-3 lambda` under `g->g+lambda f`, aligning `r_f` and `r_g`. No lost zero-leading or descent case | **CONFIRMED** | a missed `y^6` or `y^5` summand; `4 ord(a_3)=3 ord(b_4)` failing to produce integer `e` in `Kbar[x]` (or in `K[x]`); sign error in `(4.4)` or `(4.5)`; shift by `-3 lambda` failing to kill the constant; a case with `h=0` smuggled into this branch |
| 3 | Rational form `f=z^3+u z+v`, `g=z^4+a z^2+b z+c`, `z=h y+r` is an identity after aligned depression; full Jacobian is `h` times the five rows `4u'-3a'`, `4v'-3b'`, `2a u'-3c'-u a'`, `b u'+2a v'-u b'`, `b v'-u c'`, including the `2a v'` term and every sign | **CONFIRMED** | chain-rule factor not equal to `h`; `{1,z,z^2,z^3,z^4}` linearly dependent over `Kbar(x)` while `h\neq 0`; a leftover `z^5` or missing `2a v'`; `ker(d/dx)` on `Kbar(x)` larger than `Kbar` |
| 4 | Normalization `a=4u/3+alpha`, `b=4v/3`, `c=2u^2/9+2 alpha u/3+gamma`; conserved product `(4u/3+2 alpha)v=delta`; constant row `(4/3)v v'-(2/9)u(2u+3 alpha)u'`. Every branch `q=0`, `v=0`, `delta=0`, constant/nonconstant `h` is contradictory once coefficients are polynomial | **CONFIRMED** | a leftover non-integrated `z^2` residue; translating `f` failing to kill `beta`; `z^1` reducing to a false `b~u` law; a `delta=0` factorisation outside the domain; `h` nonconstant cancelling a zero of the constant row after polynomiality |
| 5 | From polynomial `D,G`, the quantities `S,E,L,M` satisfy `L u=M` without division and the eliminant `M^2+3 alpha M L-(9/2) E L^2=0`. In the indeterminate `T` this has degree ten, leading coefficient `4/3\neq 0`, no `L\neq 0` hypothesis, and is monic over `Kbar[x]` after scaling by `3/4`. Integrality plus integral closure put `r,u,v` in `Kbar[x]`. No hidden denominator or circular use of the conclusion | **CONFIRMED** | leading coefficient cancelling to `0`; `Phi` the zero polynomial; `L=0` making the identity vacuous as an equation for `r`; coefficients of the scaled eliminant leaving `R[T]`; using polynomiality of `u` to prove polynomiality of `r`; a pole of `r` compatible with a monic equation over `R` |
| 6 | After polynomiality, every conserved-product branch contradicts `jbar\neq 0` by a unit product in `Kbar[x]`. Automorphy descends from `Kbar` to arbitrary char-0 `K`. No rational source-coordinate change is treated as a polynomial automorphism | **CONFIRMED** | a nonconstant unit of `Kbar[x]`; `U'=0` or `v'=0` compatible with `jbar\neq 0` in some branch; inverse coefficients moving under a `K`-automorphism of `Kbar`; `y |-> (z-r)/h` used as an automorphism of `A^2_K` |
| 7 | Correction `y`-degree `<=4` gives coordinate `y`-degree `<=4` over `Q_{109}`; field automorphy contradicts residue-ball Hensel noninjectivity. Carries, marked collisions, and finite-support restrictions are absent | **CONFIRMED** | `109 A` raising `y`-degree over `Q_{109}`; Hensel uniqueness failing for unit Jacobian over a complete DVR; `a^{109}\neq a` on `F_{109}`; `J(\overline F)\neq I`; the contradiction applying only to a sheared non-integral pair; a claimed quintic or arbitrary-support no-go |
| 8 | This exact `y`-degree-at-most-four field theorem is not identifiable from accessible local primary material. No novelty claim is licensed. Mathematical confirmation does not depend on priority | **CONFIRMED** | a locally held primary source stating this exact theorem (both `y`-degrees `<=4` implies automorphy over arbitrary char-0 `K`); confirmation being made to rest on an attribution |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-quartic-discriminator-gate-20260824.md` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | prompt and `FREEZE.sha256` |
| `cases/as109_quartic_discriminator_20260824/verify_quartic_no_go.py` | `84fc5c3197490a405955220f95ca6f1777b0b47cc124b3763dbe158375e2e35e` | prompt and `FREEZE.sha256` |
| `cases/as109_quartic_discriminator_20260824/FREEZE.sha256` | `7f9b4c6795c74531b0fea9204133565d925427c5ce82347624ec3ee89d1b914a` | prompt |
| `xmodel/as109-cubic-coupling-gate-20260824.md` | `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | producer provenance table |
| `xmodel/as109-cubic-review-grok-20260824.md` | `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef` | producer provenance table; landed `CONFIRMED`, not consumed |
| `xmodel/as109-quadratic-coupling-gate-20260824.md` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | producer provenance table; context only |
| `xmodel/as109-quadratic-review-grok-20260824.md` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | producer provenance table; context only |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | producer provenance table |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | producer provenance table |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | producer provenance table |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | producer provenance table |

Registered command, rerun unmodified:

```sh
python3 cases/as109_quartic_discriminator_20260824/verify_quartic_no_go.py
```

Exit code 0. Top-level fields:

```text
verdict = PASS-QUARTIC-Y-NOGO-CONTROLS
as109_conclusion = NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-4
enumeration_run = false
lift_found = false
jc2_inference = false
field_characteristic = 0
```

The case directory contains only `FREEZE.sha256` and `verify_quartic_no_go.py`. The replay is a finite regression control (formal supports `{0,1,2,5}` and `{0,1,3}` plus integer maps). The coefficient derivations below are the proofs for arbitrary `x`-degree.

A second sparse engine, written for this review over `Q` with `Fraction` coefficients and not importing the producer, checked: the `[y^7]`, mixed `[y^6]`/`[y^5]`, affine `[y^4]`, quadratic `[y^5]`, and `m=0` identities on exponent sets `{0,1,2,5}`, `{0,1,3,7,11}`, `{0,4,8,15}`, `{0,1,2,3,4,6,9}`, and `{0,108,109,216}` (including vanishing of `y^{>=8}` and of `y^{>=7}` after killing quartic `f`); the cubic `[y^5]` and mixed `[y^4]`/`[y^3]` identities on the same supports; the normalized depression identity with all lower terms present, and its exact `-3 lambda` numerator shift; the full depressed `(3,4)` Jacobian including nonconstant `h` and polynomial `r`, on supports `{0,1,3}`, `{0,2,5}`, `{0,1,2,4}`; vanishing of the first three `z`-rows under the stated normalization, the identity `z^1=((4u/3+2 alpha)v)'`, and the constant row `(4/3)v v'-(2/9)u(2u+3 alpha)u'`; `S=ur+v`, `E=2u^2/9+2 alpha u/3`, the monic quadratic, and `L u-M=q v-delta`; degree ten of the `T`-eliminant with leading coefficient `4/3`, monic after `3/4`, and `L,E,M` of degrees `3,4,5` with leads `-4/3`, `1/3`, `2`; the cubic cusp Jacobian and the monic cubic identity; integer/Q tame, `GL_2`, shear, triangular, and rejection controls; AS109 shapes remaining of coordinate `y`-degree `<=4`; Fermat `a^{109}=a` on all of `F_{109}`; and `J(x-x^{109},y)=1-109 x^{108}`. Total: 112 identity checks, 0 failures.

Hostile search on the normalized form (6912 samples over small integer `h,r,u,v,alpha,gamma`) produced 5184 nonzero Jacobians and 0 nonzero-constant Jacobians. A raw constant-coefficient `(3,4)` grid (2187 samples with leading coefficients `1`) produced 0 Keller hits. Branch residues matched the formulas: `q=0`, `v=x` gives `J=(4/3)x`; `v=0`, `u=x`, `alpha=0` gives `J=-(4/9)x^2`.

---

## Claim 1 — exhaustive top-degree reduction over `K`

**CONFIRMED.**

Write

```text
f = a_4 y^4 + a_3 y^3 + a_2 y^2 + a_1 y + a_0,
g = b_4 y^4 + b_3 y^3 + b_2 y^2 + b_1 y + b_0
```

with coefficients in `K[x]`. The contribution of a pair of terms `(a_i y^i, b_j y^j)` to the coefficient of `y^{i+j-1}` in `J(f,g)` is `j a_i' b_j - i a_i b_j'`. Lower `y`-coefficients cannot produce a given top degree, and there is no `y^{>=8}` term. Hence, as an identity in `K[x]`,

```text
[y^7] J(f,g) = 4(a_4' b_4 - a_4 b_4').                         (1.1)
```

Characteristic zero gives `4 \neq 0`. The second engine reproduced (1.1) on every tested formal support, including degrees `108,109,216`.

Kernel lemma, used repeatedly and proved over `K` with no algebraic closure: the kernel of `d/dx` on `K(x)` is `K`. Write `r=p/q` in lowest terms in the Euclidean domain `K[x]`. Then `r'=0` means `p' q = p q'`. If `q` is nonconstant then `q` divides `p q'`, hence divides `q'` because `gcd(p,q)=1`; but `deg q' < deg q` in characteristic zero, so `q'=0`, a contradiction. Thus `q` is a nonzero constant, and `p' q=0` forces `p` constant. So a vanishing Wronskian of two nonzero elements of `K[x]` means their ratio lies in `K`.

Zero-top, both-top, and mixed-top cases, before any ratio with a possibly zero denominator is formed:

- `a_4=b_4=0`: both `y`-degrees are at most three. Enter the cubic base, restated below, entirely over `K`.
- `a_4=0`, `b_4 \neq 0`: `f` already has `y`-degree at most three. After a possible swap this is `deg_y g=4` and `m=deg_y f<=3`.
- `b_4=0`, `a_4 \neq 0`: swap `(f,g) |-> (g,f)`, the constant matrix `[[0,1],[1,0]]` in `GL_2(K)`, sends `J` to `-J` still in `K^*`.
- both `a_4,b_4` nonzero: (1.1) forces `(a_4/b_4)'=0` in `K(x)`, hence `a_4=lambda b_4` for `lambda in K`. The unipotent target operation `f |-> f-lambda g` is in `SL_2(K)`, preserves `J`, and kills the quartic coefficient of `f`. The new first coordinate cannot vanish identically (that would mean `f=lambda g` and `J=0`). One is left with `deg_y g=4` and `m<=3`.

No case is lost. After a possible swap it is enough to take `deg_y g=4` and `m=deg_y f<=3`.

*Affine / constant-in-`y` branch, `m=0`.* Then `f=a_0(x)` and `J(f,g)=a_0' g_y`. A nonzero constant in characteristic zero cannot have a `y^3` term. Also `a_0'\neq 0` (else `J=0`). Hence `g_y` is a nonzero constant, so `deg_y g=1`, contrary to the quartic branch. No `(0,4)` Keller pair exists. The second engine checked `J(a_0,g)=a_0' g_y` as a sparse identity.

*Affine-in-`y` / quartic branch, `m=1`.* The only `y^4` contributions are `a_1' y · 4 b_4 y^3` and `a_1 · b_4' y^4`, hence

```text
[y^4] J = 4 a_1' b_4 - a_1 b_4'.                                (1.2)
```

If `a_1=0` this is the `m=0` case already excluded. Logarithmic derivative: `(b_4/a_1^4)'=(a_1 b_4'-4 a_1' b_4)/a_1^5`, so (1.2) says `(b_4/a_1^4)'=0`. The kernel lemma puts `b_4=k a_1^4` for `k in K`. The triangular target automorphism `psi(u,v)=(u, v-k u^4)` has polynomial inverse `(u, v+k u^4)` and Jacobian determinant one. Because `f` has `y`-degree one, `f^4` has `y`-degree four and leading coefficient `a_1^4`, so `g-k f^4` has vanishing quartic coefficient. The transformed pair has both `y`-degrees at most three and enters the cubic base.

*Quadratic / quartic branch, `m=2`.* The only `y^5` contributions are `a_2' y^2 · 4 b_4 y^3` and `2 a_2 y · b_4' y^4`, hence

```text
[y^5] J = 4 a_2' b_4 - 2 a_2 b_4'.                               (1.3)
```

If `a_2=0` this is `m<=1`, already treated. Logarithmic derivative: `(b_4/a_2^2)'=a_2(a_2 b_4'-2 a_2' b_4)/a_2^4`, and (1.3) is `2(2 a_2' b_4-a_2 b_4')`, so `(b_4/a_2^2)'=0`. Thus `b_4=k a_2^2` for `k in K`. The shear `g |-> g-k f^2` is a polynomial automorphism of the target (inverse `g |-> g+k f^2`). Now `f^2` has `y`-degree four and leading coefficient `a_2^2`, so the new second coordinate has `y`-degree at most three. The transformed pair enters the cubic base.

The constants `k` live in `K`, not necessarily in a specified integral subring. Example over `Q`: `a_1=2`, `b_4=1` gives `k=1/16`. That is why the shears are field-level automorphy tests and not allowed `Z_{109}` support gauges. The integer control `(x+y, y+(x+y)^4)` has `k=1` and shears to `(x+y,y)`; `(x+y^2, y+(x+y^2)^2)` shears by `f^2`; the pair `(x+y+(x+y)^4, y+(x+y)^4)` has both displayed coordinates of `y`-degree four, and `(f+g,g) |-> (f,g)` exercises the both-top reduction.

*Cubic base, restated over `K` and not consumed from the parent review.* If both `y`-degrees are at most three, the same equal-degree / zero-top / `m=1` analysis applies with `n<=3`. Equal actual degrees `m=n>0` give top coefficient `m(a_m' b_m-a_m b_m')=0`, so a constant target `GL_2` lowers one degree. If `m=0`, then `a_0' g_y=j` forces `g_y` constant, hence a triangular pair. If `m=1<n`, then `b_n=k a_1^n` and `g-k f^n` lowers `n`. Iteration leaves only the genuinely coprime pattern `(2,3)`.

For that pattern, independently re-derived here:

```text
[y^4] J = 3 a_2' b_3 - 2 a_2 b_3',
[y^3] J = 2 a_2' b_2 + 3 a_1' b_3 - 2 a_2 b_2' - a_1 b_3'.
```

UFD valuations in `Kbar[x]` (or already in `K[x]`) give `a_2=h^2`, `b_3=h^3` after constant target scaling. The cubic coefficient is `h^4(3 a_1/h-2 b_2/h^2)'`. Constant target addition `g |-> g+lambda f` shifts the parenthesis by `-2 lambda`, so the two depression shifts `r_f=a_1/(2h)` and `r_g=b_2/(3 h^2)` can be aligned. With `z=h y+r` one has the identity `f=z^2+U`, `g=z^3+V z+W` in `Kbar(x)[y]`, and

```text
J_{x,y}(f,g) = h((3U'-2V')z^2 - 2W' z + U' V).
```

Thus `V=(3/2)U+c`, `W=w`, and `h U' V=jbar`. From `D=f(x,0)` and `G=g(x,0)` the monic equation `r^3-(3D+2c)r+2(G-w)=0` has coefficients in `Kbar[x]`. Integral closure puts `r` in `Kbar[x]`; then `h,U',V` are polynomials with unit product, each a nonzero constant, contradicting `V'=(3/2)U'`. The `(2,3)` pattern is empty. (The second engine reproduced the mixed cubic identities, the cusp Jacobian, and the monic cubic identity. The parent cubic review landed `CONFIRMED`; that landing is not used as a logical step.)

Together these reductions are exhaustive: every pair with both `y`-degrees at most four is, after target `GL_2(K)` and at most one polynomial target shear over `K`, either an automorphism coming from the cubic base or a genuine `(3,4)` pair. No algebraic closure was used in the reduction.

---

## Claim 2 — genuine `(3,4)`: valuations, depression, `-3 lambda`

**CONFIRMED.**

Assume `a_3 b_4 \neq 0` and `a_4=0`. Expanding `J` for `f` cubic in `y` and `g` quartic in `y`, the only `y^6` contributions are `a_3' y^3 · 4 b_4 y^3` and `3 a_3 y^2 · b_4' y^4`, so

```text
[y^6] J = 4 a_3' b_4 - 3 a_3 b_4'.                               (2.1)
```

The `y^5` slot receives four top contributions and none from `a_1,a_0,b_2,b_1,b_0`:

```text
[y^5] J = 3 a_3' b_3 + 4 a_2' b_4 - 3 a_3 b_3' - 2 a_2 b_4'.     (2.2)
```

(The producer replay omits those lower terms when checking the normalized form of (2.2); they cannot produce `y^5`. The second engine included them in both the un-normalized mixed identity and the normalized depression identity.)

Logarithmic derivative of the ratio in `K(x)`:

```text
(a_3^4 / b_4^3)' = a_3^3 (4 a_3' b_4 - 3 a_3 b_4') / b_4^4.
```

So (2.1) vanishes iff `(a_3^4/b_4^3)'=0`. The kernel lemma puts `a_3^4/b_4^3` in `K` if one stays in `K(x)`, and in `Kbar` after extension of scalars.

*UFD construction of `h`.* Work as the producer does, temporarily over `Kbar`. The ring `Kbar[x]` is a Euclidean domain. At each irreducible, `4 ord(a_3)=3 ord(b_4)`. Writing `m=ord(a_3)` and `n=ord(b_4)`, the relation `4m=3n` forces `m` a multiple of `3`, say `m=3e`, hence `n=4e` with `e` a nonnegative integer. The product of those irreducibles to the powers `e`, times a unit of `Kbar` to taste, is a polynomial `h in Kbar[x]`, and the remaining contents are constants `alpha_0, beta_0 in Kbar^*`:

```text
a_3 = alpha_0 h^3,     b_4 = beta_0 h^4.                        (2.3)
```

No root is extracted from the fraction field: every valuation is already a multiple of three or four inside `Kbar[x]`. The same argument works verbatim in `K[x]`, which is also a UFD, with `alpha_0, beta_0 in K^*`. Algebraic closure is therefore a convenience for linear factorization, not a missing hypothesis. Concrete check: `a_3=x^3`, `b_4=x^4` has vanishing (2.1); `a_3=x^3`, `b_4=x^3` has `[y^6]=-3 x^5 \neq 0`.

Constant diagonal target scaling `(f,g) |-> (mu f, nu g)` multiplies `J` by `mu nu in Kbar^*`. Choosing `mu=1/alpha_0` and `nu=1/beta_0` reduces (2.3) to `a_3=h^3`, `b_4=h^4` while keeping the Jacobian a nonzero constant. No case with `h=0` enters this branch (`a_3\neq 0`). A lost zero of `a_2` is not a lost case: `C=0` simply gives `r_f=0`.

Put `C=a_2` and `E=b_3`. Substitute the scaled leading form into (2.2), using `(h^3)'=3 h^2 h'` and `(h^4)'=4 h^3 h'`:

```text
[y^5] J = 9 h^2 h' E + 4 C' h^4 - 3 h^3 E' - 8 C h^3 h'.
```

Independently, with numerator `N=4 C h-3 E`,

```text
h^6 (4C/h^2 - 3E/h^3)' = h^3 N' - 3 h^2 h' N,
```

which expands to the same expression. Thus

```text
[y^5] J = h^6 (4C/h^2 - 3E/h^3)'.                               (2.4)
```

Since `h\neq 0` as a polynomial and `char K=0`, vanishing of `[y^5]` forces `4C/h^2-3E/h^3` constant in `Kbar`.

The two rational depression shifts of the cubic and quartic forms are

```text
r_f = C/(3 h^2),     r_g = E/(4 h^3),
12(r_f - r_g) = 4C/h^2 - 3E/h^3.                                (2.5)
```

(Signs: `z=h y+r` gives `z^3=h^3 y^3+3 h^2 r y^2+...`, so `C=3 h^2 r_f`; the binomial of `z^4` gives `E=4 h^3 r_g`.) The quintic equation says only that their difference is constant, not that they were equal initially.

Target addition `g |-> g+lambda f` with `lambda in Kbar` replaces `E` by `E+lambda h^3` (`f` has `y^3` coefficient `h^3`) and leaves `C` unchanged. Then

```text
N |-> N - 3 lambda h^3,     4C/h^2 - 3E/h^3 |-> (old) - 3 lambda,
r_g |-> r_g + lambda/4.
```

Every factor and sign matches the report. Choosing `lambda` equal to one-third of the constant kills it, which aligns `r_f=r_g`. Only after this operation is a common `r` used. Characteristic zero is used to divide by `3`.

Poles of `C/h^2` are not yet forbidden; they are the subject of claim 5. No zero-leading-coefficient case is lost: if `C=0` already, the constant is `-3E/h^3`, and `lambda` still aligns.

---

## Claim 3 — depressed normal form and the five Jacobian rows

**CONFIRMED.**

After the alignment of claim 2, there are `u,v,a,b,c in Kbar(x)` such that, as identities in `Kbar(x)[y]`,

```text
f = z^3 + u z + v,     g = z^4 + a z^2 + b z + c,     z = h y + r.
```

Explicitly: `z^3` accounts for the `y^3` and `y^2` terms of `f`, and the leftover affine-in-`y` piece is `u z+v` with `u=(a_1/h)-3 r^2`. Likewise `z^4` accounts for the `y^4` and `y^3` terms of `g`, and the leftover is `a z^2+b z+c`. Rational terms cancel against the original polynomial coefficients. No source automorphism of `A^2` is being applied.

View `f,g` as polynomials in `(x,z)` over `Kbar(x)`. The Jacobian matrix of `(x,z)` with respect to `(x,y)` has determinant `h`. Chain rule therefore gives `J_{x,y}(f,g)=h J_{x,z}(f,g)`, where the `x`-derivatives on the right are at constant `z`. The two `z_x` terms cancel:

```text
f_x|_y = f_x|_z + f_z z_x,     g_y = g_z h,
J_{x,y} = (f_x|_z + f_z z_x)(g_z h) - (f_z h)(g_x|_z + g_z z_x)
        = h (f_x|_z g_z - f_z g_x|_z).
```

Now `f_x=u' z+v'`, `f_z=3 z^2+u`, `g_z=4 z^3+2 a z+b`, `g_x=a' z^2+b' z+c'`. Expanding the product independently:

```text
(u' z + v')(4 z^3 + 2 a z + b)
  = 4 u' z^4 + 2 a u' z^2 + b u' z + 4 v' z^3 + 2 a v' z + b v',
(3 z^2 + u)(a' z^2 + b' z + c')
  = 3 a' z^4 + 3 b' z^3 + 3 c' z^2 + u a' z^2 + u b' z + u c'.
```

Subtracting and collecting powers of `z` yields exactly

```text
J_{x,z} = (4u'-3a') z^4
        + (4v'-3b') z^3
        + (2 a u' - 3 c' - u a') z^2
        + (b u' + 2 a v' - u b') z
        + (b v' - u c').                                        (3.1)
```

Hence `J_{x,y}=h` times (3.1). There is no `z^5`: `f_x` has `z`-degree one and `g_z` has `z`-degree three. The second engine reproduced the identity on every tested support, including nonconstant `h` and nonconstant polynomial `r`.

The term `2 a v'` in the `z^1` row is present and essential. Omitting it would leave `b u'-u b'`, a Wronskian suggesting the false law `b\sim u`. With the actual row, claim 4 produces a conserved product involving `v`, not a linear relation `b\sim u`. The left side of `J_{x,y}` is the nonzero constant `jbar`. As an element of `Kbar(x)[y]`, `z` has `y`-degree one (`h\neq 0`), so `{1,z,z^2,z^3,z^4}` are linearly independent over `Kbar(x)`. Coefficient vanishing of the five rows is therefore legitimate.

---

## Claim 4 — normalization, conserved product, and branches

**CONFIRMED.**

The first three rows of (3.1) integrate in `Kbar(x)` because the kernel of `d/dx` is `Kbar`:

```text
4u'-3a'=0  =>  a = 4u/3 + alpha,
4v'-3b'=0  =>  b = 4v/3 + beta,
```

with `alpha,beta in Kbar`. Substitute into the `z^2` row:

```text
2(4u/3+alpha) u' - 3 c' - u (4u'/3) = (4u/3) u' + 2 alpha u' - 3 c' = 0,
```

so `c'=(4u/9)u'+(2 alpha/3)u'` and

```text
c = 2 u^2/9 + (2 alpha/3) u + gamma,     gamma in Kbar.
```

A constant translation of the target coordinate `f |-> f+t` replaces `v` by `v+t` and, to keep `g` (hence `b`) unchanged, replaces `beta` by `beta-4t/3`. Taking `t=3 beta/4` makes `beta=0` without changing the Jacobian or automorphy. Thereafter `b=4v/3`. The constant term `D=f(x,0)` used in claim 5 is computed *after* this translation, so it remains in `Kbar[x]`.

The `z` row is then

```text
(4v/3) u' + 2(4u/3+alpha) v' - u (4v'/3)
  = (4v/3) u' + (4u/3) v' + 2 alpha v'
  = ((4u/3 + 2 alpha) v)'.
```

Vanishing gives the conserved product

```text
q v = delta,     q = 4u/3 + 2 alpha,     delta in Kbar.          (4.1)
```

The constant row, after substituting `c'=(2/9)(2u+3 alpha)u'`, is

```text
b v' - u c' = (4/3) v v' - (2/9) u (2u+3 alpha) u',             (4.2)
```

so `jbar/h` equals the right-hand side of (4.2). The second engine checked vanishing of the first three rows, `z^1=(q v)'`, and (4.2) as sparse identities over `Q`.

These relations still live in `Kbar(x)`. The contradiction in every branch is deferred until `h,q,u,v` are known to lie in the domain `R=Kbar[x]` (claim 5), and is recorded in claim 6. No branch is discarded at this stage: `q=0`, `v=0`, `delta=0`, `alpha=0`, and constant or nonconstant `h` all remain open until polynomiality.

---

## Claim 5 — degree-ten integrality discriminator

**CONFIRMED.**

Let `D=f(x,0)` and `G=g(x,0)`, both in `R=Kbar[x]`. From the depressed form, `D=r^3+u r+v`. Define, first at the actual rational `r`,

```text
S = D - r^3,     E = G + r^4/3 - alpha r^2 - gamma - (4/3) D r.
```

Substitution of (4.6) and the normalization of claim 4 gives the identities in `Kbar(x)`

```text
S = u r + v,     E = 2 u^2/9 + 2 alpha u/3,
u^2 + 3 alpha u - (9/2) E = 0.                                  (5.1)
```

(The `r^4` terms in `E` cancel as `1+1/3-4/3=0`; the `u r^2`, `v r`, `alpha r^2`, and `gamma` terms likewise cancel.) Using `v=S-u r`, the conserved product (4.1), and the quadratic in (5.1) gives, without division,

```text
L u = M,     L = 2 alpha r + (4/3) S,     M = 6 r E - 2 alpha S + delta.
```

Direct expansion: `L u-M = (4u/3+2 alpha)v-delta`. No `L\neq 0` hypothesis is used. Multiplying the monic quadratic by `L^2` and substituting `L u=M` produces

```text
M^2 + 3 alpha M L - (9/2) E L^2 = 0.                            (5.2)
```

When `L=0` one has `M=0` as well, and (5.2) holds as `0=0` at the actual `r`; that does not weaken the next paragraph.

Replace `r` by an indeterminate `T`, retaining `D,G in R` as coefficients:

```text
S(T)=D-T^3,
E(T)=G+T^4/3-alpha T^2-gamma-(4/3) D T,
L(T)=2 alpha T+(4/3) S(T),
M(T)=6 T E(T)-2 alpha S(T)+delta.
```

These are elements of `R[T]`: `1/3,4/3 in Kbar subset R`. Leading terms, independently of `D,G,alpha,gamma,delta`, are

```text
E(T) = (1/3) T^4 + ...,     L(T) = -(4/3) T^3 + ...,     M(T) = 2 T^5 + ....
```

(The `3 alpha M L` term has degree at most eight.) The left side of (5.2) therefore has degree ten and leading coefficient

```text
2^2 - (9/2)(1/3)(4/3)^2 = 4 - 8/3 = 4/3.                        (5.3)
```

(The square erases the sign of `lead L`. The producer formula (6.6) is this identity; the second engine evaluated the full symbolic polynomial in `T` and obtained degree `10` with coefficient `4/3`, and after multiplying by `3/4` the leading coefficient `1`. The replay's denominator-cleared form has leading coefficient `24=18·(4/3)`, matching `18` times the unscaled eliminant.) Because the leading coefficient is a nonzero constant, the eliminant `Phi(T)` is never the zero polynomial. In particular the case `L=0` at the actual `r` does not collapse `Phi` to `0`; `L(T)` itself has degree three with lead `-4/3`, so is never identically zero.

After multiplication by `3/4`, (5.2) is monic in `R[T]` and vanishes at `T=r`. Hence `r` is integral over `R`. The polynomial ring `R=Kbar[x]` is a PID, hence integrally closed in `Kbar(x)`, so `r in R`. Explicitly: write `r=p/q` in lowest terms with `q` monic; then `q` divides `p^{10}`, hence `q` is a unit.

*No circularity, no hidden denominator.* The polynomial `Phi(T)` is built from `D,G,alpha,gamma,delta` only. Its vanishing at the rational `r` uses the identities (5.1)--(5.2), which hold in `Kbar(x)` before any polynomiality conclusion. Polynomiality of `u` is not used to prove polynomiality of `r`. After `r in R` one has `S,E in R`. The quadratic `u^2+3 alpha u-(9/2)E=0` is monic over `R` (here `2` is inverted in `Kbar`, which is why the monic form rather than `2u^2+\cdots` is required). The element `u` already lies in `Kbar(x)` by construction (`u=a_1/h-3 r^2`); it is therefore integral over `R` and lies in `R`. Finally `v=S-u r in R`. Poles of `C/(3 h^2)` at zeros of a nonconstant `h` are forbidden by the monic equation, so those zeros of `h` already divide `C`. A model pole `r=1/x` cannot be a root: after clearing, `x^{10} Phi(1/x)` has constant term equal to the leading coefficient `4/3\neq 0`.

This step precludes cancellation of poles by `h` in the constant Jacobian row.

---

## Claim 6 — unit-product contradiction and descent

**CONFIRMED.**

Put `q=4u/3+2 alpha`. All of `h,q,u,v` and their derivatives now lie in the domain `R`, and (4.1) says `q v=delta`. The constant row is `jbar/h=(4/3)v v'-(2/9)u(2u+3 alpha)u'`. Units of `R=Kbar[x]` are `Kbar^*`.

- If `delta\neq 0`, then `q` and `v` are units, hence constants. Thus `u` is constant as well, so the right-hand side of the constant row is zero, contrary to `jbar\neq 0`. (In this branch one need not even conclude that `h` is a unit: `jbar/h=0` is already absurd.)
- If `delta=0`, the domain property gives `q=0` or `v=0`.
  - If `q=0`, then `u=-(3/2)alpha` is constant and the constant row reduces to `jbar/h=(4/3)v v'`. The nonzero constant product `h v v'` forces each factor to be a unit, hence `v` constant, contrary to `v'\neq 0`. Independent residue: `alpha=2`, `u=-3`, `v=x`, `h=1` produces `J=(4/3)x`, not a nonzero constant.
  - If `v=0`, the constant row says that a nonzero scalar multiple of `h·u·(2u+3 alpha)·u'` equals `jbar`. Every factor is a unit; in particular `u` is constant, contrary to `u'\neq 0`. The subcase `2u+3 alpha=0` is `q=0` and `v=0` together, which makes the constant row identically zero, still contrary to `jbar\neq 0`. Independent residue: `v=0`, `u=x`, `alpha=0`, `h=1` produces `J=-(4/9)x^2`.

Nonconstant `h` is included in every branch and is forced to be a unit (or is already contradictory) by the same unit-product. Constant `h` is likewise contradictory. No factor can be zero: that would make `jbar=0`. There are no poles left after claim 5, so there is no pole-zero cancellation between `h` and the constant row.

Every branch of a genuine `(3,4)` Keller pair is contradictory. Combined with claim 1, every Keller pair with both `y`-degrees at most four is an automorphism over `Kbar`.

*Descent to arbitrary characteristic-zero `K`.* Two independent descents, either of which suffices.

Uniqueness / Galois invariance: a polynomial endomorphism of `A^2` has at most one polynomial inverse. If `(f,g)` is defined over `K` and becomes an automorphism over `Kbar`, that inverse `G` is unique as a morphism. For every `K`-automorphism `sigma` of `Kbar`, the coefficientwise conjugate `sigma(G)` is also a polynomial inverse, hence equals `G`. Characteristic zero makes `K` perfect, so the fixed field of `Gal(Kbar/K)` is `K`. The coefficients of `G` therefore lie in `K`.

Faithful flatness: any field extension is faithfully flat. An endomorphism of an affine scheme that becomes an isomorphism after faithfully flat base change is an isomorphism.

Injectivity, which is all AS109 needs, descends even more cheaply: if `F(a)=F(b)` for `a,b in K^2`, the same holds in `Kbar^2`, so `a=b`.

*Algebraic closure is unnecessary.* Claim 1 never left `K`. In claim 2, `K[x]` is a UFD, so `h, alpha_0, beta_0` may be taken in `K[x]` and `K^*`; the kernel of `d/dx` on `K(x)` is `K`; the depression constant and the aligning `lambda` lie in `K`. Claims 3--6 then run with `K` in place of `Kbar`: the monic eliminant has coefficients in `K[x]`, and `K[x]` is integrally closed in `K(x)`. The `(3,4)` branch is empty over `K` itself. Surviving pairs are reduced by target operations with constants in `K` to the cubic base, whose inverse is polynomial over `K`. The producer's `Kbar` detour is correct and is not load-bearing.

*No source coordinate substitution.* The auxiliary `z=h y+r` is used only to expand a Jacobian in `Kbar(x)[y]` (or `K(x)[y]`). The pair `(f,g)` is never replaced by a source change `y |-> (z-r)/h`, which would not be a polynomial automorphism of `A^2` when `h` is nonconstant. Target `GL_2` and triangular shears are polynomial automorphisms of the target plane, used only to decide automorphy. Jung--van der Kulk is not a dependency.

Characteristic zero is load-bearing for the global factors `2,3,4`, for `deg pi'=deg pi-1` on nonconstant polynomials, for invertibility of `2` and `3` in the depression, and for invertibility of `2` and `4` in the monic integrality equations. All are stated.

---

## Claim 7 — AS109 consequence, Hensel, and scope exclusions

**CONFIRMED.**

Suppose, for contradiction,

```text
F=(P,Q)=(x-x^{109}+109 A,  y+109 B),
A,B in Z_{109}[x,y],     deg_y(A), deg_y(B) <= 4,     det J(F)=1.
```

*Correction `y`-degree implies coordinate `y`-degree.* View `P,Q` in `Q_{109}[x,y]`. The summand `x-x^{109}` is independent of `y`, and `109 \neq 0` in `Q_{109}`, so `deg_y(P)=deg_y(A)` if `deg_y(A)>=1`, and `deg_y(P)=0` otherwise. Likewise `deg_y(Q)=max(1, deg_y(B))` except possibly if the linear term of `109 B` cancelled the seed `y`. That cancellation would *drop* degree, so `deg_y(Q)<=4` still. (For completeness: it cannot occur for integral `B`, because the coefficient of `y` in `Q` is `1+109 b_1(x)` with `b_1 in Z_{109}[x]`, and `-1/109` is not in `Z_{109}`.) Thus `deg_y(P), deg_y(Q)<=4`. The identity `det J(F)=1` survives `Z_{109} -> Q_{109}`. Claim 6 over `K=Q_{109}` makes `F` a polynomial automorphism of `A^2_{Q_{109}}`, hence injective on `Q_{109}^2`.

*Target transforms are not applied to the integral seed.* The `GL_2` steps, the shears, and the auxiliary `z` are internal to the proof of the field theorem. They may take coefficients out of `Z_{109}` and may destroy the special fibre `(x-x^{109},y)`. The contradiction is for `F` itself: an automorphism is injective. No claim treats a sheared pair as an AS109 representative.

*Residue-ball noninjectivity, rechecked, not a marked collision, independent of carry.* Reduction modulo `109` is `\overline F=(x-x^{109},y)`. Over `F_{109}` one has `d(x^{109})=109 x^{108}=0`, so `J(\overline F)=I` as a matrix of polynomials, and Fermat `a^{109}=a` for every `a in F_{109}`, so `\overline F(a,b)=(0,b)`. Direct check: `J(x-x^{109},y)=1-109 x^{108} \equiv 1 \pmod{109}`, and `a-a^{109}\equiv 0` for all `109` residues. Multivariate Hensel on the complete DVR `Z_{109}`, using that `det J_F` is the constant `1` (hence a unit at every integral point), says that `F` maps each source ball `(a,b)+109 Z_{109}^2` bijectively onto the target ball `(0,b)+109 Z_{109}^2`. The `109` distinct source balls for fixed `b` therefore all cover the same target ball, so any integral target in that ball has `109` distinct preimages in `Z_{109}^2 subset Q_{109}^2`. This is noninjectivity of `F` over `Q_{109}`, contradicting the field theorem.

The collision is a pair of Hensel preimages in distinct residue balls. It is not the frozen marked-section condition `F(0,0)=F(1,0)` as integral lattice-point values. The packed identity `det J=1` over `Z_{109}` is the hypothesis; the truncated two-layer expansion and its base-109 carry are not used. The erratum leaves the Hensel lemma intact, and the different-model carry review confirmed that independence.

*Scope exclusions, audited.*

- In scope: every exact determinant-one lift whose two corrections both have `y`-degree at most four, with no cap on `x`-degree, number of monomials, coefficient height, or linear coupling among those coefficients.
- Out of scope: any pair in which at least one correction has `y`-degree `>=5`; series lifts; an arbitrary-AS109 no-go; a JC2 decision. No finite grammar for the quintic range is supplied.
- Not used: marked collision equations, support cap, `x`-degree bound, coefficient height, finite Witt layer, exponent/support search, AWS.
- The run produced no lift (`lift_found=false`), no characteristic-zero point, and no JC2 inference (`jc2_inference=false`). An exact lift of this shape cannot exist, so none can be embedded into `C`.
- The cubic parent is not a logical dependency (its theorem is re-proved). The quadratic parent is context only. GL2 target normalization and polynomial target shears are exact as automorphy tests and are not integral gauges.

A future `CLOSED-SUPPORT + UNIT-L` certificate for this seed, if one exists, must include at least one monomial of `y`-degree at least five; that is a necessary condition, not a construction. This review does not license a quintic search.

---

## Claim 8 — priority hygiene

**CONFIRMED** as a hygiene decision, not as a novelty grant.

Accessible local primary material was reread only for whether *this exact theorem* (Keller, both `y`-degrees at most four, arbitrary characteristic-zero field, conclusion polynomial automorphy) is already identifiable there.

- Magnus, Math. Scand. 3 (1955) 255--260, was read in full locally. Its theorem is the coprime *total-degree* case: `m,n >= 2` coprime implies the Jacobian constant is `0` and `u,v in K[h]`. The proof is homogeneous-piece recurrences / generating functions. That is a different statement (total degree, not `y`-degree; conclusion `k=0` rather than automorphy of every `y`-degree-`<=4` Keller pair). It is an ancestor of the leading-form / differential-equation genre, not a copy of this theorem.
- Hermoso--Alcázar, arXiv 2410.18867, Theorem 4 with `n=2`, is the unweighted Wronskian `p q'-p' q = c \neq 0 =>` both degrees `<=1`. That is the affine tail of the quadratic base, not the quartic theorem.
- Żołądek, Topology 47 (2008), Appendix Lemma A.7 (with A.4/A.6 and Lemma 3.9), locally held, is the Darboux / Schwarz--Christoffel rigidity used as Theorem A of the local paper-2 notes. It is not a verified copy of the two-variable `y`-degree-at-most-four automorphy statement.
- Appelgate--Onishi 1985 (JPAA 37) and Nowicki--Nakai 1988 (JPAA 51, correction JPAA 58) remain locally flagged as unresolved / paywalled. Żołądek Remark 3.10 points at their algebraic treatment of a chart-rationality condition for `ψ̃_N`, which is not a verified copy of this `y`-degree theorem. No attribution to either source is licensed from a search snippet, a citers' summary, or a title.
- Nowicki, Nagoya Math. J. 109 (1988), is the kernel case `J(f,g)=0`, not Keller.

The exact theorem is therefore **not** identifiable from accessible local primary material. That does **not** license a novelty or prior-art claim. The producer already makes none. This review promotes none. Mathematical confirmation of claims 1--7 does not depend on priority: the derivation above is self-contained. A later primary-source identification of the same statement would be a citation update, not a refutation.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a quintic statement, an arbitrary-support AS109 no-go, a JC2 decision, or a novelty claim.

Hostile attempts to break the field theorem produced no counterexample:

- the non-Keller pair `(x+y^3, y+y^4)` has Jacobian `1+4 y^3`, as predicted;
- 6912 normalized polynomial samples with `V`-product structure and various degrees of `h,r,u,v` never gave a nonzero constant Jacobian;
- 2187 raw constant-coefficient `(3,4)` pairs with leading coefficients `1` never gave a nonzero constant Jacobian;
- the `q=0` residue with `v=x` produces `(4/3)x`; the `v=0` residue with `u=x` produces `-(4/9)x^2`;
- a rational shift `r=1/x` fails the degree-ten monic equation (constant term `4/3`);
- `m=0` with `b_4\neq 0` is not Keller.

The smallest precisions a reader could miss, and that this review therefore isolates, are:

- Characteristic zero is used for the factors `2,3,4`, for `deg pi'=deg pi-1`, for invertibility of `2` and `3` in the depression, and for invertibility of `2` and `4` in the monic integrality equations. The coefficient identities are polynomial; the *implications* Wronskian `=0 =>` linear dependence over the ground field need the kernel of `d/dx`.
- Algebraic closure is a convenience for writing `Kbar[x]` as a product of linear factors. Unique factorization in `K[x]` already produces `h in K[x]`. Descent is correct as written and is not needed if one never leaves `K`.
- The replay's formal supports `{0,1,2,5}` and `{0,1,3}` are regression controls. Arbitrary `x`-degree is carried by `y`-degree counting in (1.1)--(1.3), (2.1)--(2.2), and (3.1). The JSON field `as109_conclusion` is a declared label, not a search result.
- Constants `lambda` and `k` lie in `K` (or `Kbar` on the producer's detour), not necessarily in `Z_{109}`. That is why the target operations decide automorphy over `Q_{109}` and are not integral gauges.
- The `2 a v'` term is load-bearing. Without it the `z^1` row would suggest the false law `b\sim u`; with it one obtains the conserved product `(4u/3+2 alpha)v=delta`.
- The degree-ten eliminant is needed precisely when `h` is nonconstant (possible poles of `r` at zeros of `h`). If `h` is already a unit then `r=C/(3 h^2)` is polynomial at once; the monic equation still holds and is not circular.
- Hensel's collision is 109-to-1 covering of residue balls. It does not use marked sections and does not use truncated digit carries.
- No novelty claim is attached to confirmation.

Those are scope reminders, not missing hypotheses in the written lemmas.

---

## Stop conditions that remain in force

No cap, degree, or prime may be changed in response to this review. Quintic and higher `y`-degree are not licensed as a search by this file. The only resurrection trigger remains a separately reviewed finite coupled section that meets `CLOSED-SUPPORT + UNIT-L` and, by claim 7, allows `y`-degree at least five in one correction.

No result here proves or disproves JC2.
