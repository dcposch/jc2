# Hostile different-model review — AS109 CUBIC-Y NO-GO

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero field theorem: every Keller pair with both `y`-degrees `<=3` is a polynomial automorphism; hence no exact `det J=1` lift of the AS109 seed has both correction `y`-degrees at most three |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions in the last section; algebraic closure is a convenience, not a load-bearing extra hypothesis) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (hand Jacobian by `y`-degree, Wronskian / logarithmic derivative in `K(x)`, UFD valuations in `K[x]` and in `Kbar[x]`, integral closure of a PID, chain-rule Jacobian of the cusp form); a second sparse engine that does not import the producer replay; unmodified rerun of `verify_cubic_no_go.py` as regression control; banked Hensel lemma as previously dual-confirmed, rechecked on residue balls rather than marked sections |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T10:00:00Z – 2026-08-24T10:07:00Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-cubic-coupling-gate-20260824.md` (SHA-256 `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820`)
- `cases/as109_cubic_coupling_20260824/verify_cubic_no_go.py` (SHA-256 `7939c0d708548cf4ba2a06a6ca7a7abe64783014fb494bb1c543d308db875b42`)
- `cases/as109_cubic_coupling_20260824/FREEZE.sha256` (SHA-256 `a68afeca5c7e68e2e5df12b620eac6ab1356d9797f1007850f9476adb55a4a3a`)
- quadratic parent `xmodel/as109-quadratic-coupling-gate-20260824.md` (SHA-256 `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1`) and its different-model review `xmodel/as109-quadratic-review-grok-20260824.md` (SHA-256 `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2`); motivation only, not a logical dependency
- Hensel noninjectivity in `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and its different-model review `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`) and `xmodel/as109-carry-erratum-review-grok-20260824.md` (SHA-256 `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212`), only to confirm Hensel independence from digit bookkeeping
- local primary/secondary priority notes: `papers/paper2/PRIORITY.md`, `papers/paper2/SCOPE.md` (Magnus 1955 read in full locally; Appelgate--Onishi 1985 and Nowicki--Nakai 1988 flagged paywalled / unresolved)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No quartic or higher `y`-degree family was searched. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, `J(f,g)=f_x g_y-f_y g_x`, and `p=109`.

---

## Promotion

**Accept `CUBIC-Y NO-GO` at the stated scope.**

- Over any characteristic-zero field, every Keller pair with both coordinates of `y`-degree at most three is a polynomial automorphism of `A^2_K`.
- There is therefore no exact `Z_{109}` polynomial lift of the seed `(x-x^{109},y)` with `det J=1` whose two correction polynomials both have `y`-degree at most three.

**Do not promote this to:** a quartic or higher `y`-degree statement; nonexistence of an arbitrary finite-support AS109 lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim for the field theorem.

**Keep `CLOSED-SUPPORT + UNIT-L` as a conditional resurrection target**, now with the necessary constraint that the section allow `y`-degree at least four in one correction. Whether any such coupled block closes remains open. This file licenses no quartic grammar and no support search.

---

## Quarantine

No result here proves or disproves JC2. Producer JSON strings `PASS-CUBIC-Y-NOGO-CONTROLS` and `NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-3` were not used as evidence; the identities below were re-derived. The quadratic parent is recorded as landed `CONFIRMED` and is not consumed: the cubic writeup repeats the degree-at-most-two reduction it needs. The earlier closed-support parent is not consumed. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed exact identity that Hensel consumes. Priority is quarantined from the mathematical verdict.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_{109}` for the lift, and a field theorem over an arbitrary characteristic-zero `K` (applied at `K=Q_{109}`). Arbitrary finite `x`-degree, support, and coefficient coupling are in scope *inside* both `y`-degrees `<=3`. Quartic and higher `y`-degree, series lifts, and an arbitrary-AS109 no-go are out of scope. GL2 target normalization and polynomial target shears are used only as automorphy tests over `K` (or `Kbar`); they are not integral support gauges.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | All top-degree cases for `deg_y f, deg_y g <=3` reduce, over `K` and without algebraic closure, to the quadratic base or to a genuine `(2,3)` pair: cubic/cubic leading Wronskian plus constant target `GL_2`; zero-top cases; affine/cubic shear `g-k f^3` | **CONFIRMED** | a leftover `y^5` term from lower coefficients; `3=0`; kernel of `d/dx` on `K(x)` larger than `K`; `a_1=0` admitting nonzero `b_3`; `k f^3` of `y`-degree `>3`; a missed leading pattern |
| 2 | In genuine `(2,3)`, `[y^4]J=3 a_2' b_3-2 a_2 b_3'` and `[y^3]J=2 a_2' b_2+3 a_1' b_3-2 a_2 b_2'-a_1 b_3'`; UFD valuations give `a_2=alpha h^2`, `b_3=beta h^3`; after scaling, the depression invariant is `3C/h-2E/h^2` with exact shift `-2 lambda` under `g->g+lambda f`, aligning `r_f` and `r_g` | **CONFIRMED** | a missed `y^4` or `y^3` summand; `3 ord(a_2)=2 ord(b_3)` failing to produce integer `e` in `Kbar[x]` (or in `K[x]`); sign error in `(2.9)` or `(2.10a)`; shift by `-2 lambda` failing to kill the constant; a case with `h=0` smuggled into this branch |
| 3 | Rational cusp form `f=z^2+U`, `g=z^3+V z+W`, `z=h y+r` is an identity under `(2.8)` and `(2.10)`; full Jacobian is `h((3U'-2V')z^2-2W' z+U' V)`; coefficient vanishing over `Kbar(x)` gives `V'=(3/2)U'`, `W'=0`, `h U' V=jbar` | **CONFIRMED** | chain-rule factor not equal to `h`; `{1,z,z^2}` linearly dependent over `Kbar(x)` while `h\neq 0`; a leftover `y`-degree from `U,V,W`; `ker(d/dx)` on `Kbar(x)` larger than `Kbar` |
| 4 | The monic cubic `r^3-(3D+2c)r+2(G-w)=0` has coefficients in `Kbar[x]`; integral closure puts `r` in `Kbar[x]`; then `h,U',V` are polynomials with unit product, each a nonzero constant, contradicting `V'=(3/2)U'`. No hidden pole, zero factor, or lost nonconstant-`h` case | **CONFIRMED** | a non-monic leading coefficient; `c` or `w` not constant; `Kbar[x]` failing to be integrally closed; a pole of `r` compatible with the monic equation; `h` nonconstant cancelling poles of `U' V` *after* `r` is polynomial; `U'=0` compatible with `jbar\neq 0` |
| 5 | Automorphy descends from `Kbar` to arbitrary char-0 `K` by uniqueness of the polynomial inverse (Galois-fixed coefficients) or by faithful flatness of `Kbar/K`. No source coordinate substitution or field denominator invalidates the theorem. In fact `Kbar` is unnecessary | **CONFIRMED** | inverse coefficients moving under some `K`-automorphism of `Kbar`; a completing-the-square source substitution `y |-> y-C/(2h)` used as an automorphism of `A^2_K`; inverse requiring localization of `K[x,y]`; `ker(d/dx)` on `K(x)` requiring `Kbar` |
| 6 | Correction `y`-degree `<=3` gives coordinate `y`-degree `<=3` over `Q_{109}`; field automorphy contradicts residue-ball Hensel noninjectivity. Carries and marked collisions are irrelevant. Scope exclusions hold | **CONFIRMED** | `109 A` raising `y`-degree over `Q_{109}`; Hensel uniqueness failing for unit Jacobian over a complete DVR; `a^{109}\neq a` on `F_{109}`; `J(\overline F)\neq I`; the contradiction applying only to a sheared non-integral pair; a claimed quartic or arbitrary-support no-go |
| 7 | This exact `y`-degree-at-most-three field theorem is not identifiable from accessible local primary material. No novelty claim is licensed. Mathematical confirmation does not depend on priority | **CONFIRMED** | a locally held primary source stating this exact theorem (both `y`-degrees `<=3` implies automorphy over arbitrary char-0 `K`); confirmation being made to rest on an attribution |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-cubic-coupling-gate-20260824.md` | `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | prompt and `FREEZE.sha256` |
| `cases/as109_cubic_coupling_20260824/verify_cubic_no_go.py` | `7939c0d708548cf4ba2a06a6ca7a7abe64783014fb494bb1c543d308db875b42` | prompt and `FREEZE.sha256` |
| `cases/as109_cubic_coupling_20260824/FREEZE.sha256` | `a68afeca5c7e68e2e5df12b620eac6ab1356d9797f1007850f9476adb55a4a3a` | prompt |
| `xmodel/as109-quadratic-coupling-gate-20260824.md` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | producer provenance table |
| `xmodel/as109-quadratic-review-grok-20260824.md` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | producer provenance table; landed `CONFIRMED`, not consumed |
| `xmodel/as109-closed-support-gate-20260824.md` | `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` | producer provenance table; not consumed |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | producer provenance table |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | producer provenance table |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | producer provenance table |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | producer provenance table |

Registered command, rerun unmodified:

```sh
python3 cases/as109_cubic_coupling_20260824/verify_cubic_no_go.py
```

Exit code 0. Top-level fields:

```text
verdict = PASS-CUBIC-Y-NOGO-CONTROLS
as109_conclusion = NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-3
enumeration_run = false
lift_found = false
jc2_inference = false
field_characteristic = 0
```

The case directory contains only `FREEZE.sha256` and `verify_cubic_no_go.py`. The replay is a finite regression control (formal supports `{0,1,2,5}` and `{0,1,3}` plus integer maps). The coefficient derivations below are the proofs for arbitrary `x`-degree.

A second sparse engine, written for this review over `Q` with `Fraction` coefficients and not importing the producer, checked: the `[y^5]`, mixed `[y^4]`/`[y^3]`, and affine `[y^3]` identities on exponent sets `{0,1,2,5}`, `{0,1,3,7,11}`, `{0,4,8,15}`, `{0,1,...,6,10,20}`, `{0,108,109,216}`, and `{0,1,2,3,4,6,9}` (30 identity checks, 0 failures); vanishing of `y^{>=6}` and of `y^{>=4}` after killing cubic `f`; the `a_2=a_1=0` expansion `J=a_0' g_y`; the normalized depression identity and its exact `-2 lambda` numerator shift; the full cusp Jacobian including nonconstant `h` and polynomial `r`; the monic integrality identity; a pole `r=1/x` failing the monic equation (constant term `1`); forty-eight small polynomial cusp samples producing no nonzero-constant Jacobian; the leftover `z^2` residue `9 h^3` when `h,U',V` are forced constant; integer/Q tame, `GL_2`, shear, triangular, and rejection controls; AS109 shapes remaining of coordinate `y`-degree `<=3`; Fermat `a^{109}=a` on all of `F_{109}`; and `J(x-x^{109},y)=1-109 x^{108}`.

---

## Claim 1 — exhaustive top-degree reduction over `K`

**CONFIRMED.**

Write

```text
f = a_3 y^3 + a_2 y^2 + a_1 y + a_0,     g = b_3 y^3 + b_2 y^2 + b_1 y + b_0
```

with coefficients in `K[x]`. Then

```text
f_x = a_3' y^3 + a_2' y^2 + a_1' y + a_0',     f_y = 3 a_3 y^2 + 2 a_2 y + a_1,
g_x = b_3' y^3 + b_2' y^2 + b_1' y + b_0',     g_y = 3 b_3 y^2 + 2 b_2 y + b_1.
```

The only `y^5` contributions to `f_x g_y` and `f_y g_x` are `a_3' y^3 · 3 b_3 y^2` and `3 a_3 y^2 · b_3' y^3`. Lower `y`-coefficients cannot produce `y^5`, and there is no `y^{>=6}` term. Hence, as an identity in `K[x]`,

```text
[y^5] J(f,g) = 3(a_3' b_3 - a_3 b_3').                          (1.1)
```

Characteristic zero gives `3 \neq 0`. The second engine reproduced (1.1) on every tested formal support, including degrees `108,109,216`.

Kernel lemma, used repeatedly and proved over `K` with no algebraic closure: the kernel of `d/dx` on `K(x)` is `K`. Write `r=p/q` in lowest terms in the Euclidean domain `K[x]`. Then `r'=0` means `p' q = p q'`. If `q` is nonconstant then `q` divides `p q'`, hence divides `q'` because `gcd(p,q)=1`; but `deg q' < deg q` in characteristic zero, so `q'=0`, a contradiction. Thus `q` is a nonzero constant, and `p' q=0` forces `p` constant. So a vanishing Wronskian of two nonzero elements of `K[x]` means their ratio lies in `K`.

Zero-top and both-top cases, before any ratio with a possibly zero denominator is formed:

- `a_3=b_3=0`: both `y`-degrees are at most two. Enter the quadratic base, restated below, entirely over `K`.
- `a_3=0`, `b_3 \neq 0`: `f` already has `y`-degree at most two. This is shape `(2.3)` of the report, after possibly renaming.
- `b_3=0`, `a_3 \neq 0`: swap `(f,g) |-> (g,f)`, the constant matrix `[[0,1],[1,0]]` in `GL_2(K)`, sends `J` to `-J` still in `K^*`, and puts the cubic coordinate second.
- both `a_3,b_3` nonzero: (1.1) forces `(a_3/b_3)'=0` in `K(x)`, hence `a_3=lambda b_3` for `lambda in K`. The unipotent target operation `f |-> f-lambda g` is in `SL_2(K)`, preserves `J`, and kills the cubic coefficient of `f`. The new first coordinate cannot vanish identically (that would mean `f=lambda g` and `J=0`). One is left in shape `(2.3)` with `b_3 \neq 0`.

No case is lost, and no coefficient was assumed nonzero in order to form a ratio that might be undefined.

It remains to treat

```text
f = a_2 y^2 + a_1 y + a_0,     g = b_3 y^3 + b_2 y^2 + b_1 y + b_0,     b_3 \neq 0.
```

*Affine/cubic branch, `a_2=0`.* If also `a_1=0`, then `f=a_0(x)` and `J(f,g)=a_0' g_y=a_0'(3 b_3 y^2+2 b_2 y+b_1)`. A nonzero constant in characteristic zero cannot have a `y^2` term, and `a_0'\neq 0` (else `J=0`), so `b_3=0`, contrary to this branch. If `a_1 \neq 0`, the only `y^3` contributions are `a_1' y · 3 b_3 y^2` and `a_1 · b_3' y^3`, hence

```text
[y^3] J(f,g) = 3 a_1' b_3 - a_1 b_3'.                           (1.2)
```

The logarithmic derivative is `(b_3/a_1^3)'=(a_1 b_3'-3 a_1' b_3)/a_1^4`, so (1.2) says `(b_3/a_1^3)'=0` in `K(x)`. The kernel lemma puts `b_3=k a_1^3` for `k in K`. The triangular target automorphism `psi(u,v)=(u, v-k u^3)` has polynomial inverse `(u, v+k u^3)` and Jacobian determinant one. Because `f` is affine in `y`, `f^3` has `y`-degree at most three and leading coefficient `a_1^3`, so `g-k f^3` has vanishing cubic coefficient. The transformed pair lies in the quadratic base.

The constant `k` lives in `K`, not necessarily in a specified integral subring. Example over `Q`: `a_1=2`, `b_3=1` gives `k=1/8`. That is why the shear is a field-level automorphy test and not an allowed `Z_{109}` support gauge. The integer control `(x+y, y+(x+y)^3)` has `k=1` and shears to `(x+y, y)`; the pair `(x+y+(x+y)^3, y+(x+y)^3)` has both displayed coordinates cubic in `y`, and the constant operation `(f+g,g) |-> (f,g)` exercises the both-top reduction.

*Quadratic base, restated over `K` and not consumed from the parent review.* If both `y`-degrees are at most two, the cubic coefficient is `2(a_2' b_2-a_2 b_2')`. The same zero-top/`GL_2` analysis as above makes one coordinate affine in `y`. For `f=a_1 y+a_0` and `g=b_2 y^2+b_1 y+b_0`, one has `[y^2]J=2 a_1' b_2-a_1 b_2'`. If `a_1=0` then `J=a_0'(2 b_2 y+b_1)` forces `b_2=0`. If `a_1\neq 0` then `b_2=k a_1^2` and `g-k f^2` kills the remaining quadratic term. Two affine-in-`y` coordinates have proportional leading coefficients (or one already zero); a constant target combination produces `h in K[x]` with `J(h, b_1 y+b_0)=h' b_1 in K^*`. A product of two elements of `K[x]` is a nonzero constant iff both are nonzero constants, so `h=alpha x+beta` with `alpha in K^*` and `b_1=gamma in K^*`. The inverse is `x=(h-beta)/alpha`, `y=(g-b_0(x))/gamma`, polynomial over `K`. This is the previously confirmed quadratic theorem, re-derived here because the cubic writeup uses it.

Together these reductions are exhaustive: every pair with both `y`-degrees at most three is, after target `GL_2(K)` and at most one polynomial target shear over `K`, either an affine-in-`y` automorphism or a genuine `(2,3)` pair. No algebraic closure was used.

---

## Claim 2 — genuine `(2,3)`: valuations, depression, `-2 lambda`

**CONFIRMED.**

Assume `a_2 b_3 \neq 0`. Expanding `J` for `f` quadratic in `y` and `g` cubic in `y`, the only `y^4` contributions are `a_2' y^2 · 3 b_3 y^2` and `2 a_2 y · b_3' y^3`, so

```text
[y^4] J = 3 a_2' b_3 - 2 a_2 b_3'.                              (2.1)
```

The `y^3` slot receives four top contributions and none from `a_0,b_1,b_0`:

```text
[y^3] J = 2 a_2' b_2 + 3 a_1' b_3 - 2 a_2 b_2' - a_1 b_3'.      (2.2)
```

(The producer replay omits `a_0,b_1,b_0` when checking the normalized form of (2.2); the omitted terms cannot produce `y^3` under `a_2=h^2`, `b_3=h^3`, which the second engine also checked by including them in the un-normalized mixed identity.)

Logarithmic derivative of the ratio in `K(x)`:

```text
(a_2^3 / b_3^2)' = a_2^2 (3 a_2' b_3 - 2 a_2 b_3') / b_3^3.
```

So (2.1) vanishes iff `(a_2^3/b_3^2)'=0`. The kernel lemma puts `a_2^3/b_3^2` in `K` if one stays in `K(x)`, and in `Kbar` after extension of scalars.

*UFD construction of `h`.* Work as the producer does, temporarily over `Kbar`. The ring `Kbar[x]` is a Euclidean domain. At each irreducible (equivalently, each linear factor) one has `3 ord(a_2)=2 ord(b_3)`. Writing `m=ord(a_2)` and `n=ord(b_3)`, the relation `3m=2n` forces `m` even, say `m=2e`, hence `n=3e` with `e` a nonnegative integer. The product of those irreducibles to the powers `e`, times a unit of `Kbar` to taste, is a polynomial `h in Kbar[x]`, and the remaining contents are constants `alpha, beta in Kbar^*`:

```text
a_2 = alpha h^2,     b_3 = beta h^3.                            (2.3)
```

No root is extracted from the fraction field: every valuation is already even or a multiple of three inside `Kbar[x]`. The same argument works verbatim in `K[x]`, which is also a UFD, with `alpha, beta in K^*` (irreducibles of `K[x]` need not be linear). Algebraic closure is therefore a convenience for linear factorization, not a missing hypothesis. Concrete check: `a_2=4 x^2 (x+1)^2`, `b_3=8 x^3 (x+1)^3` has vanishing (2.1); `a_2=x^2`, `b_3=x^2` has `[y^4]=2 x^3 \neq 0`.

Constant diagonal target scaling `(f,g) |-> (mu f, nu g)` multiplies `J` by `mu nu in Kbar^*`. Choosing `mu=1/alpha` and `nu=1/beta` reduces (2.3) to

```text
a_2 = h^2,     b_3 = h^3                                    (2.4)
```

while keeping the Jacobian a nonzero constant. (Over `K`, the same scalings lie in `K^*`.)

Put `C=a_1` and `E=b_2`. Substitute (2.4) into (2.2), using `(h^2)'=2 h h'` and `(h^3)'=3 h^2 h'`:

```text
[y^3] J = 4 h h' E + 3 C' h^3 - 2 h^2 E' - 3 C h^2 h'.
```

Independently,

```text
(3 C/h - 2 E/h^2)'
  = 3(C' h - C h')/h^2 - 2(E' h^2 - 2 E h h')/h^4,
```

and multiplication by `h^4` recovers exactly the displayed `[y^3]`. Thus

```text
[y^3] J = h^4 (3 C/h - 2 E/h^2)'.                              (2.5)
```

Since `h \neq 0` as a polynomial (`a_2 \neq 0`) and `char K=0`, vanishing of `[y^3]` forces `3 C/h - 2 E/h^2` to be constant in `Kbar` (the constant field of `Kbar(x)`). Equivalently, clearing the displayed denominator, the polynomial `N=3 C h - 2 E` satisfies the cross-multiplied derivative identity used by the replay.

The two rational depression shifts of the quadratic and cubic forms are

```text
r_f = C/(2 h),     r_g = E/(3 h^2),     6(r_f - r_g) = 3 C/h - 2 E/h^2.   (2.6)
```

(Signs: completing the square, `z=h y+r` gives `z^2=h^2 y^2+2 h r y+...`, so `C=2 h r_f`; the binomial of `z^3` gives `E=3 h^2 r_g`.) The cubic equation says only that their difference is constant, not that they were equal initially.

Target addition `g |-> g+lambda f` with `lambda in Kbar` replaces `E` by `E+lambda h^2` (`f` has `y^2` coefficient `h^2`) and leaves `C` unchanged. Then

```text
N |-> N - 2 lambda h^2,     3 C/h - 2 E/h^2 |-> (old) - 2 lambda,
r_g |-> r_g + lambda/3.
```

Every factor and sign matches the report. Choosing `lambda` equal to half the constant kills it, which is `E=(3/2) h C` as a polynomial identity and `r_f=r_g`. Only after this operation is a common `r` used. Characteristic zero is used to divide by `2`.

No case with `h=0` enters this branch. Poles of `C/h` are not yet forbidden; they are the subject of claim 4.

---

## Claim 3 — rational cusp normal form and Jacobian

**CONFIRMED.**

In `Kbar(x)` define

```text
r = C/(2 h),     z = h y + r,
U = a_0 - r^2,     V = b_1/h - 3 r^2,     W = b_0 - r^3 - V r.
```

Under (2.4) and `E=(3/2) h C` one has `2 h r=C` and `3 h^2 r=E`, so as identities in `Kbar(x)[y]`

```text
z^2 + U = h^2 y^2 + 2 h r y + a_0 = f,
z^3 + V z + W = h^3 y^3 + 3 h^2 r y^2 + (3 h r^2 + V h) y + b_0 = g,
```

because `3 h r^2 + V h = 3 h r^2 + b_1 - 3 h r^2 = b_1`. These are identities of the original polynomials: rational terms cancel. No source automorphism of `A^2` is being applied.

View `f,g` as polynomials in `(x,z)` over `Kbar(x)`, with `z=h(x) y+r(x)`. The Jacobian matrix of `(x,z)` with respect to `(x,y)` has determinant `h`. Chain rule therefore gives `J_{x,y}(f,g)=h J_{x,z}(f,g)`, where the `x`-derivatives on the right are at constant `z`. For `f=z^2+U(x)` and `g=z^3+V(x) z+W(x)`,

```text
f_x = U',     f_z = 2 z,     g_z = 3 z^2 + V,     g_x = V' z + W',
J_{x,z} = U'(3 z^2 + V) - 2 z (V' z + W')
        = (3 U' - 2 V') z^2 - 2 W' z + U' V.
```

Hence

```text
J_{x,y}(f,g) = h ((3 U' - 2 V') z^2 - 2 W' z + U' V).            (3.1)
```

The second engine reproduced (3.1) on every tested support, including nonconstant `h` and nonconstant polynomial `r`. The left side is the nonzero constant `jbar`. As an element of `Kbar(x)[y]`, `z` has `y`-degree one (`h \neq 0`), so `{1,z,z^2}` are linearly independent over `Kbar(x)`. Coefficient vanishing therefore yields

```text
V' = (3/2) U',     W' = 0,     h U' V = jbar                     (3.2)
```

as equalities in `Kbar(x)`. The constant field of `Kbar(x)` in characteristic zero is `Kbar`, so `V=(3/2)U+c` and `W=w` for constants `c,w in Kbar`. (A rational function with vanishing derivative cannot have a pole, so `W` is a genuine constant, not a cancelled principal part.)

The identities (3.2) are still in `Kbar(x)`. Polynomiality of `r` is not used yet. That is the next claim, and it is where a hidden-pole attack has to live.

---

## Claim 4 — polynomiality of `r` and the unit-product contradiction

**CONFIRMED.**

Let `D=a_0` and `G=b_0`, both in `Kbar[x]`. From the cusp form,

```text
D = r^2 + U,     G = r^3 + V r + w.
```

Substitute `U=D-r^2` and `V=(3/2)U+c=(3/2)(D-r^2)+c`:

```text
G = r^3 + ((3/2)(D-r^2)+c) r + w
  = -(1/2) r^3 + (3/2) D r + c r + w.
```

Multiplication by `2`, legitimate in characteristic zero, rearranges to the monic identity

```text
r^3 - (3 D + 2 c) r + 2(G - w) = 0.                             (4.1)
```

Every coefficient lies in `Kbar[x]`: `D,G in Kbar[x]` and `c,w in Kbar`. The identity holds in `Kbar(x)` whether or not `r` has poles. Thus `r in Kbar(x)` is integral over `Kbar[x]`.

The polynomial ring `Kbar[x]` is a PID, hence integrally closed in its fraction field. Therefore `r in Kbar[x]`. Explicitly: write `r=p/q` in lowest terms with `q` monic. Then `p^3 = (3D+2c) p q^2 - 2(G-w) q^3`, so `q` divides `p^3`, hence `q` is a unit, hence `q in Kbar^*`.

*Hidden-pole attack.* The dangerous-looking expression is `r=C/(2h)`, which may have poles at zeros of a nonconstant `h`. A rational function with a pole is not integral over `Kbar[x]`. The monic equation forbids poles, so those zeros of `h` must already have divided `C`. The second engine checked the model pole `r=1/x` with polynomial `D`: the cleared form of (4.1) has constant term `1`, so it is not the zero polynomial. No case is lost when `h` is nonconstant: that case is included, and integrality forces the apparent denominator to cancel.

*Zero-factor / unit-product attack, after `r` is a polynomial.* Then `U=D-r^2` is a polynomial and `V=(3/2)U+c` is a polynomial. The three factors in `h U' V = jbar in Kbar^*` are therefore elements of `Kbar[x]` whose product is a nonzero constant. Units of `Kbar[x]` are `Kbar^*`, so each factor is a nonzero constant:

```text
h in Kbar^*,     U' in Kbar^*,     V in Kbar^*.
```

In particular `V` is constant, so `V'=0`, while `U'` a nonzero constant in characteristic zero means `deg U=1`. Then `V'=(3/2)U'` says `0` equals a nonzero constant, a contradiction.

This does not lose the nonconstant-`h` case: that case is forced to `h` constant by the unit product, and still contradicts. It does not lose `V=0` or `U'=0`: either would make the product zero, contrary to `jbar \neq 0`. It does not permit pole-zero cancellation between `U' V` and `h` *after* polynomiality, because there are no poles left. Before polynomiality one does not need that analysis: integrality is applied first, and (4.1) has polynomial coefficients independently of `h`.

The genuine `(2,3)` branch is therefore empty over `Kbar`. Combined with claim 1, every Keller pair with both `y`-degrees at most three is an automorphism over `Kbar`.

---

## Claim 5 — descent to arbitrary characteristic-zero `K`

**CONFIRMED.**

Two independent descents, either of which suffices.

*Uniqueness / Galois invariance.* A polynomial endomorphism of `A^2` has at most one polynomial inverse. If `(f,g)` is defined over `K` and becomes an automorphism over `Kbar`, that inverse `G` is unique as a morphism. For every `K`-automorphism `sigma` of `Kbar`, the coefficientwise conjugate `sigma(G)` is also a polynomial inverse, hence equals `G`. Characteristic zero makes `K` perfect, so the fixed field of `Gal(Kbar/K)` is `K`. The coefficients of `G` therefore lie in `K`, and `(f,g)` is an automorphism of `A^2_K`.

*Faithful flatness.* Any field extension is faithfully flat. An endomorphism of an affine scheme that becomes an isomorphism after faithfully flat base change is an isomorphism. Equivalently, polynomial-coordinate-ring isomorphy descends along `K -> Kbar`.

*Injectivity, which is all AS109 needs, descends even more cheaply.* If `F(a)=F(b)` for `a,b in K^2`, the same holds in `Kbar^2`, so `a=b`.

*Algebraic closure is unnecessary.* Claim 1 never left `K`. In claim 2, `K[x]` is a UFD, so `h, alpha, beta` may be taken in `K[x]` and `K^*`; the kernel of `d/dx` on `K(x)` is `K`; the depression constant and the aligning `lambda` lie in `K`. Claims 3--4 then run with `K` in place of `Kbar`: the monic equation has coefficients in `K[x]`, and `K[x]` is integrally closed in `K(x)`. The `(2,3)` branch is empty over `K` itself. Surviving pairs are reduced by target operations with constants in `K` to the quadratic base, whose inverse is polynomial over `K`. The producer's `Kbar` detour is correct and is not load-bearing.

*No source coordinate substitution.* The auxiliary `z=h y+r` is used only to expand a Jacobian in `Kbar(x)[y]` (or `K(x)[y]`). The pair `(f,g)` is never replaced by a source change `y |-> y-C/(2h)`, which would not be a polynomial automorphism of `A^2` when `h` is nonconstant. Target `GL_2` and triangular shears are polynomial automorphisms of the target plane, used only to decide automorphy.

*No invalidating field denominator.* Ratios `a_3/b_3`, `b_3/a_1^3`, `a_2^3/b_3^2`, and `C/(2h)` are formed in a rational function field as proof devices. Vanishing derivatives or integral closure return them to the polynomial ring (or to `K`). The maps `f-lambda g`, `g-k f^3`, and `g+lambda f` remain in the polynomial ring over the field in which the constants live. The triangular inverse of the quadratic base divides only by elements of `K^*`. Jung--van der Kulk is not a dependency.

Characteristic zero is load-bearing for the global factors `2` and `3`, for `deg pi'=deg pi-1` on nonconstant polynomials, and for invertibility of `2` in the depression. All are stated.

---

## Claim 6 — AS109 consequence, Hensel, and scope exclusions

**CONFIRMED.**

Suppose, for contradiction,

```text
F=(P,Q)=(x-x^{109}+109 A,  y+109 B),
A,B in Z_{109}[x,y],     deg_y(A), deg_y(B) <= 3,     det J(F)=1.
```

*Correction `y`-degree implies coordinate `y`-degree.* View `P,Q` in `Q_{109}[x,y]`. The summand `x-x^{109}` is independent of `y`, and `109 \neq 0` in `Q_{109}`, so `deg_y(P)=deg_y(A)` if `deg_y(A)>=1`, and `deg_y(P)=0` otherwise. Likewise `deg_y(Q)=max(1, deg_y(B))` except possibly if the linear term of `109 B` cancelled the seed `y`. That cancellation would *drop* degree, so `deg_y(Q)<=3` still. (For completeness: it cannot occur for integral `B`, because the coefficient of `y` in `Q` is `1+109 b_1(x)` with `b_1 in Z_{109}[x]`, and `-1/109` is not in `Z_{109}`.) Thus `deg_y(P), deg_y(Q)<=3`. The identity `det J(F)=1` survives `Z_{109} -> Q_{109}`. Claim 5 over `K=Q_{109}` makes `F` a polynomial automorphism of `A^2_{Q_{109}}`, hence injective on `Q_{109}^2`.

*Target transforms are not applied to the integral seed.* The `GL_2` steps, the shears, and the auxiliary `z` are internal to the proof of the field theorem. They may take coefficients out of `Z_{109}` and may destroy the special fibre `(x-x^{109},y)`. The contradiction is for `F` itself: an automorphism is injective. No claim treats a sheared pair as an AS109 representative.

*Residue-ball noninjectivity, rechecked, not a marked collision, independent of carry.* Reduction modulo `109` is `\overline F=(x-x^{109},y)`. Over `F_{109}` one has `d(x^{109})=109 x^{108}=0`, so `J(\overline F)=I` as a matrix of polynomials, and Fermat `a^{109}=a` for every `a in F_{109}`, so `\overline F(a,b)=(0,b)`. Direct check: `J(x-x^{109},y)=1-109 x^{108} \equiv 1 \pmod{109}`, and `a-a^{109} \equiv 0` for all `109` residues. Multivariate Hensel on the complete DVR `Z_{109}`, using that `det J_F` is the constant `1` (hence a unit at every integral point), says that `F` maps each source ball `(a,b)+109 Z_{109}^2` bijectively onto the target ball `(0,b)+109 Z_{109}^2`. The `109` distinct source balls for fixed `b` therefore all cover the same target ball, so any integral target in that ball has `109` distinct preimages in `Z_{109}^2 subset Q_{109}^2`. This is noninjectivity of `F` over `Q_{109}`, contradicting the field theorem.

The collision is a pair of Hensel preimages in distinct residue balls. It is not the frozen marked-section condition `F(0,0)=F(1,0)` as integral lattice-point values. The packed identity `det J=1` over `Z_{109}` is the hypothesis; the truncated two-layer expansion and its base-109 carry are not used. The erratum leaves the Hensel lemma intact, and the different-model carry review confirmed that independence.

*Scope exclusions, audited.*

- In scope: every exact determinant-one lift whose two corrections both have `y`-degree at most three, with no cap on `x`-degree, number of monomials, coefficient height, or linear coupling among those coefficients.
- Out of scope: any pair in which at least one correction has `y`-degree `>=4`; series lifts; an arbitrary-AS109 no-go; a JC2 decision. No finite grammar for the quartic range is supplied.
- Not used: marked collision equations, support cap, `x`-degree bound, coefficient height, finite Witt layer, exponent/support search, AWS.
- The run produced no lift (`lift_found=false`), no characteristic-zero point, and no JC2 inference (`jc2_inference=false`). An exact lift of this shape cannot exist, so none can be embedded into `C`.
- The quadratic parent is not a logical dependency. The closed-support parent is not consumed. GL2 target normalization and polynomial target shears are exact as automorphy tests and are not integral gauges.

A future `CLOSED-SUPPORT + UNIT-L` certificate for this seed, if one exists, must include at least one monomial of `y`-degree at least four; that is a necessary condition, not a construction. This review does not license a quartic search.

---

## Claim 7 — priority hygiene

**CONFIRMED** as a hygiene decision, not as a novelty grant.

Accessible local primary material was reread only for whether *this exact theorem* (Keller, both `y`-degrees at most three, arbitrary characteristic-zero field, conclusion polynomial automorphy) is already identifiable there.

- Magnus, Math. Scand. 3 (1955) 255--260, was read in full locally. Its theorem is the coprime *total-degree* case: `m,n >= 2` coprime implies the Jacobian constant is `0` and `u,v in K[h]`. The proof is homogeneous-piece recurrences / generating functions. That is a different statement (total degree, not `y`-degree; conclusion `k=0` rather than automorphy of every `y`-degree-`<=3` Keller pair). It is an ancestor of the leading-form / differential-equation genre, not a copy of this theorem.
- Hermoso--Alcázar, arXiv 2410.18867, Theorem 4 with `n=2`, is the unweighted Wronskian `p q'-p' q = c \neq 0 =>` both degrees `<=1`. That is the affine tail of the quadratic base, not the cubic theorem.
- Appelgate--Onishi 1985 (JPAA 37) and Nowicki--Nakai 1988 (JPAA 51, correction JPAA 58) remain locally flagged as unresolved / paywalled. Żołądek Remark 3.10 points at their algebraic treatment of a chart-rationality condition for `ψ̃_N`, which is not a verified copy of this `y`-degree theorem. No attribution to either source is licensed from a search snippet, a citers' summary, or a title.
- Nowicki, Nagoya Math. J. 109 (1988), is the kernel case `J(f,g)=0`, not Keller.

The exact theorem is therefore **not** identifiable from accessible local primary material. That does **not** license a novelty or prior-art claim. The producer already makes none. This review promotes none. Mathematical confirmation of claims 1--6 does not depend on priority: the derivation above is self-contained. A later primary-source identification of the same statement would be a citation update, not a refutation.

---

## Smallest missing hypothesis or overclaim

None of the seven claims is an existence theorem, a quartic statement, an arbitrary-support AS109 no-go, a JC2 decision, or a novelty claim.

Hostile attempts to break the field theorem produced no counterexample:

- the non-Keller cusp `(x+y^2, y+y^3)` has Jacobian `1+3 y^2`, as predicted;
- polynomial cusp samples with `V=(3/2)U+c` and various degrees of `h` and `U` never gave a nonzero constant Jacobian;
- forcing `h,U',V` all constant, the only way to make `h U' V` constant, leaves the `z^2` residue `(3 U'-2 V') h^3 \neq 0`;
- a rational shift `r=1/x` fails the monic equation;
- `a_1=a_2=0` with `b_3 \neq 0` is not Keller.

The smallest precisions a reader could miss, and that this review therefore isolates, are:

- Characteristic zero is used for the factors `2` and `3`, for `deg pi'=deg pi-1`, and for invertibility of `2` in the depression. The coefficient identities are polynomial; the *implications* Wronskian `=0 =>` linear dependence over the ground field need the kernel of `d/dx`.
- Algebraic closure is a convenience for writing `Kbar[x]` as a product of linear factors. Unique factorization in `K[x]` already produces `h in K[x]`. Descent is correct as written and is not needed if one never leaves `K`.
- The replay's formal supports `{0,1,2,5}` and `{0,1,3}` are regression controls. Arbitrary `x`-degree is carried by `y`-degree counting in (1.1), (1.2), (2.1), (2.2), and (3.1). The JSON field `as109_conclusion` is a declared label, not a search result.
- Constants `lambda` and `k` lie in `K` (or `Kbar` on the producer's detour), not necessarily in `Z_{109}`. That is why the target operations decide automorphy over `Q_{109}` and are not integral gauges.
- Hensel's collision is 109-to-1 covering of residue balls. It does not use marked sections and does not use truncated digit carries.
- No novelty claim is attached to confirmation.

Those are scope reminders, not missing hypotheses in the written lemmas.

---

## Stop conditions that remain in force

No cap, degree, or prime may be changed in response to this review. Quartic and higher `y`-degree are not licensed as a search by this file. The only resurrection trigger remains a separately reviewed finite coupled section that meets `CLOSED-SUPPORT + UNIT-L` and, by claim 6, allows `y`-degree at least four in one correction.

No result here proves or disproves JC2.
