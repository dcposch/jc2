# Hostile different-model review — AS109 QUADRATIC-Y NO-GO

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero field theorem: every Keller pair with both `y`-degrees `<=2` is a polynomial automorphism; hence no exact `det J=1` lift of the AS109 seed has both correction `y`-degrees at most two |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions in the last section) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (hand Jacobian by `y`-degree, Wronskian / logarithmic derivative in `K(x)`, Euclidean algorithm in `K[x]`, explicit polynomial inverses); a second sparse engine that does not import the producer replay; unmodified rerun of `verify_quadratic_no_go.py` as regression control; banked Hensel lemma as previously dual-confirmed, rechecked on residue balls rather than marked sections |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T09:42:00Z – 2026-08-24T09:52:00Z |
| Python | 3.14.6; stdlib only |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-quadratic-coupling-gate-20260824.md` (SHA-256 `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1`)
- `cases/as109_quadratic_coupling_20260824/verify_quadratic_no_go.py` (SHA-256 `846aaef1be5be8efd402ce8c596cf6985b6f9fb19a5553d5bcd2757de746ed69`)
- `cases/as109_quadratic_coupling_20260824/FREEZE.sha256` (SHA-256 `e0ae3f4dded38cb96bf149c3e035fbdff3976187fc7f396c0416cba65577e5ae`)
- Hensel noninjectivity in `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and its different-model review `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`), only to confirm Hensel independence from digit bookkeeping

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No cubic or higher `y`-degree family was searched.

Write `K` for an arbitrary characteristic-zero field, `J(f,g)=f_x g_y-f_y g_x`, and `p=109`.

---

## Promotion

**Accept `QUADRATIC-Y NO-GO` at the stated scope.**

- Over any characteristic-zero field, every Keller pair with both coordinates of `y`-degree at most two is a polynomial automorphism of `A^2_K`.
- There is therefore no exact `Z_{109}` polynomial lift of the seed `(x-x^{109},y)` with `det J=1` whose two correction polynomials both have `y`-degree at most two.

**Do not promote this to:** a cubic or higher `y`-degree statement; nonexistence of an arbitrary finite-support AS109 lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; or a finite Witt-level inference.

**Keep `CLOSED-SUPPORT + UNIT-L` as a conditional resurrection target**, now with the necessary constraint that the section allow `y`-degree at least three. Whether any such coupled block closes remains open.

## Quarantine

No result here proves or disproves JC2. Producer JSON strings `PASS-QUADRATIC-Y-NOGO-CONTROLS` and `NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-2` were not used as evidence; the identities below were re-derived. The parent `xmodel/as109-closed-support-gate-20260824.md` is provisional and is not a dependency. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed exact identity that Hensel consumes.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_{109}` for the lift, and a field theorem over an arbitrary characteristic-zero `K` (applied at `K=Q_{109}`). Arbitrary finite `x`-degree, support, and coefficient coupling are in scope *inside* both `y`-degrees `<=2`. Cubic and higher `y`-degree, series lifts, and an arbitrary-AS109 no-go are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Over char-0 `K`, `[y^3]J(f,g)=2(a_2'b_2-a_2 b_2')` for two quadratic-in-`y` polynomials; all zero-leading cases reduce by constant target `GL_2(K)` to one affine-in-`y` coordinate, and the new affine coordinate cannot vanish in a Keller pair | **CONFIRMED** | a leftover `y^3` term from lower `y`-coefficients; `2=0`; kernel of `d/dx` on `K(x)` larger than `K`; proportional tops with nonzero Jacobian |
| 2 | With `f` affine in `y`, `[y^2]J=2 a_1' b_2-a_1 b_2'`; `a_1=0` forces `b_2=0`; `a_1\neq 0` forces `b_2=k a_1^2` for `k in K`; the target shear `(f,g)->(f,g-k f^2)` is a polynomial automorphism of determinant one and kills the remaining `y^2` term | **CONFIRMED** | derivative of `b_2/a_1^2` not equal to that Wronskian up to a unit of `K(x)`; shear inverse not polynomial; `k f^2` of `y`-degree `>2`; `a_1=0` admitting a nonzero-`b_2` Keller pair |
| 3 | Every affine-in-`y` Keller pair is a polynomial automorphism: both-nonzero leading coefficients produce a linear `h in K[x]` and constant `b_1`, with the displayed inverse; one-zero cases are the same triangular form after a swap; both-zero is excluded by `j\neq 0` | **CONFIRMED** | a nonconstant factor of `h' b_1`; `h'` constant of degree `>=1` in char 0; inverse requiring an algebraic extension or a localization of `K[x,y]`; both leading coefficients zero with `J` a nonzero constant |
| 4 | Claims 1--3 prove the field theorem over an arbitrary char-0 field. No hidden algebraic closure, leftover denominator, or source coordinate change is used | **CONFIRMED** | `ker(d/dx)` on `K(x)` requiring `\overline{K}`; inverse coefficients not in `K`; a completing-the-square source substitution `y |-> y-a_1/(2a_2)`; the argument using Jung--van der Kulk as a black box |
| 5 | An exact integral AS109 lift with correction `y`-degrees `<=2` is a `Q_{109}` Keller pair of coordinate `y`-degrees `<=2`, hence an automorphism, contradicting residue-ball noninjectivity. Target transforms need not preserve the integral seed. Hensel uses the 109-to-1 ball covering, not a marked collision, and is independent of digit carry | **CONFIRMED** | `109 A` dropping `y`-degree over `Q_{109}` *upward*; Hensel uniqueness failing for unit Jacobian over a complete DVR; `a^{109}\neq a` on `F_{109}`; `J(\overline F)\neq I`; the contradiction applying only to a sheared non-integral pair |
| 6 | Arbitrary `x`-degree/support/coupling is excluded only inside both `y`-degrees `<=2`. Cubic and higher remain open. No lift, characteristic-zero counterexample, arbitrary-AS109 no-go, or JC2 conclusion is claimed or obtained | **CONFIRMED** | the report exhibiting a cubic lift; an inferred nonexistence statement for general finite support; a Hensel/Lefschetz promotion of a nonexistent lift to a complex counterexample |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-quadratic-coupling-gate-20260824.md` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | prompt and `FREEZE.sha256` |
| `cases/as109_quadratic_coupling_20260824/verify_quadratic_no_go.py` | `846aaef1be5be8efd402ce8c596cf6985b6f9fb19a5553d5bcd2757de746ed69` | prompt and `FREEZE.sha256` |
| `cases/as109_quadratic_coupling_20260824/FREEZE.sha256` | `e0ae3f4dded38cb96bf149c3e035fbdff3976187fc7f396c0416cba65577e5ae` | prompt |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | producer provenance table |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | producer provenance table |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | producer provenance table |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | producer provenance table |
| `xmodel/as109-closed-support-gate-20260824.md` | `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` | producer provenance table; **PROVISIONAL, not used** |

Registered command, rerun unmodified:

```sh
python3 cases/as109_quadratic_coupling_20260824/verify_quadratic_no_go.py
```

Exit code 0. Top-level fields:

```text
verdict = PASS-QUADRATIC-Y-NOGO-CONTROLS
as109_conclusion = NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-2
enumeration_run = false
lift_found = false
jc2_inference = false
field_characteristic = 0
```

The case directory contains only `FREEZE.sha256` and `verify_quadratic_no_go.py`. The replay is a finite regression control (formal support `{0,1,2,5}` plus four integer maps). The coefficient derivations below are the proofs for arbitrary `x`-degree.

A second sparse engine, written for this review and not importing the producer, checked: the `[y^3]`, mixed `[y^2]`, and affine `[y],[y^0]` identities on exponent sets including `{0,1,2,5}`, `{0,1,3,7,11}`, `{0,4,8,15}`, `{0,1,...,6,10,20}`, and `{0,108,109,216}` (0 failures); vanishing of `y^{>=4}` and of `y^{>=3}` after setting a leading quadratic to zero; the `a_1=0` expansion `J=a_0'(2 b_2 y+b_1)`; integer Keller, shear, `GL_2`, negative, and degenerate controls; a non-integral-`k` Wronskian; explicit triangular inverses in the both-nonzero, `a_1=0`, and `b_1=0` cases; thirty random AS109 shapes `P=x-x^{109}+109 A`, `Q=y+109 B` with `deg_y(A),deg_y(B)<=2` remaining of coordinate `y`-degree `<=2`; Fermat `a^{109}=a` on all of `F_{109}`; and `J(x-x^{109},y)=1-109 x^{108} \equiv 1 \pmod{109}`.

---

## Claim 1 — cubic Jacobian coefficient and `GL_2` reduction

**CONFIRMED.**

Write

```text
f = a_2(x) y^2 + a_1(x) y + a_0(x),
g = b_2(x) y^2 + b_1(x) y + b_0(x)
```

with coefficients in `K[x]`. Then

```text
f_x = a_2' y^2 + a_1' y + a_0',     f_y = 2 a_2 y + a_1,
g_x = b_2' y^2 + b_1' y + b_0',     g_y = 2 b_2 y + b_1.
```

The only `y^3` contributions to `f_x g_y` and `f_y g_x` are `a_2' y^2 \cdot 2 b_2 y` and `2 a_2 y \cdot b_2' y^2`. Lower `y`-coefficients of `f` and `g` cannot produce `y^3`. Hence, as an identity in `K[x]`,

```text
[y^3] J(f,g) = 2 a_2' b_2 - 2 a_2 b_2' = 2(a_2' b_2 - a_2 b_2').     (1.1)
```

Characteristic zero gives `2 \neq 0`. The second engine reproduced (1.1) on every tested formal support, including degrees `108,109,216`, and found no `y^{>=4}` term.

Zero-leading cases, before any ratio is formed:

- `a_2=0`, `b_2` arbitrary: `f` is already affine in `y`.
- `b_2=0`, `a_2` arbitrary: `g` is already affine in `y`. The swap `(f,g)\mapsto(g,f)` is the constant matrix `[[0,1],[1,0]]` in `GL_2(K)`, sends `J` to `-J` still in `K^*`, and puts the pair in the shape (2.2) of the report.
- `a_2=b_2=0`: both coordinates are already affine in `y`.

If both `a_2` and `b_2` are nonzero, (1.1) forces the Wronskian `a_2' b_2 - a_2 b_2'=0`, i.e. `(a_2/b_2)'=0` in `K(x)`. Lemma (char 0, no algebraic closure): the kernel of `d/dx` on `K(x)` is `K`. Proof: write `r=p/q` in lowest terms in the Euclidean domain `K[x]`. Then `r'=0` means `p' q = p q'`. If `q` is nonconstant then `q` divides `p q'`, hence divides `q'` because `gcd(p,q)=1`; but `deg q' < deg q` in characteristic zero, so `q'=0`, a contradiction. Thus `q` is a nonzero constant, and `p' q=0` forces `p'=0`, so `p` is constant as well. Therefore `a_2/b_2=\lambda` lies in `K`, and `a_2=\lambda b_2` as an equality in `K[x]`.

The unipotent target operation `f \mapsto f-\lambda g` is the matrix `[[1,-\lambda],[0,1]]` in `SL_2(K)`. It preserves `J` and is inverted by `f \mapsto f+\lambda g`. The new `y^2` coefficient is `a_2-\lambda b_2=0`. The new first coordinate cannot vanish identically: that would mean `f=\lambda g` as polynomials, hence `J=0`. So after a constant target `GL_2(K)` change one may assume the displayed shape (2.2), with the affine coordinate not the zero polynomial.

No source substitution is used. In particular there is no completing-the-square `y \mapsto y-a_1/(2 a_2)`, which would have introduced a denominator in `K(x)` and need not be polynomial.

---

## Claim 2 — mixed quadratic coefficient, `b_2=k a_1^2`, and the shear

**CONFIRMED.**

Now

```text
f = a_1(x) y + a_0(x),
g = b_2(x) y^2 + b_1(x) y + b_0(x).
```

The `y^3` slot is empty. Expanding,

```text
[y^2] J(f,g) = 2 a_1' b_2 - a_1 b_2'.                         (2.1)
```

(The factor `2` sits only on `a_1' b_2`, because `f_y=a_1` has no `y`.) The second engine reproduced (2.1) on every mixed formal support.

If `a_1=0`, then `f=a_0(x)` and `J(f,g)=a_0'(2 b_2 y + b_1)`. A nonzero constant in characteristic zero cannot have a `y^1` term, so `2 a_0' b_2=0`. Also `a_0'\neq 0` (else `J=0`). Hence `b_2=0`, and both coordinates are affine in `y`. The integer control `J(x,y^2)=2y` is the matching negative; `J(x,y+x^2)=1` is the matching positive with `b_2` already zero.

If `a_1\neq 0`, (2.1) is the numerator of the logarithmic derivative of `b_2/a_1^2`:

```text
(b_2 / a_1^2)' = (a_1 b_2' - 2 a_1' b_2) / a_1^3.
```

So (2.1) says `(b_2/a_1^2)'=0` in `K(x)`. Claim 1's kernel lemma puts `b_2/a_1^2=k` in `K`, hence `b_2=k a_1^2` in `K[x]`. Equivalently, without fractions: write `a_1^2=d q` and `b_2=d r` with `gcd(q,r)=1`; vanishing derivative of `r/q` forces `q` constant in characteristic zero and then `r` constant, so the ratio is in `K`.

The target shear `\psi(u,v)=(u,\, v-k u^2)` is triangular, with polynomial inverse `(u,\, v+k u^2)` and Jacobian matrix `[[1,0],[-2 k u, 1]]` of determinant one. Composition `\psi\circ(f,g)=(f,\, g-k f^2)` therefore preserves the Keller constant. Because `f` is affine in `y`,

```text
f^2 = a_1^2 y^2 + 2 a_1 a_0 y + a_0^2
```

has `y`-degree at most two, and the `y^2` coefficient of `g-k f^2` is `b_2-k a_1^2=0`. Both coordinates are affine in `y`. The integer control `(x+y,\, y+(x+y)^2)` has `k=1` and shears to `(x+y,\, y)`; the second engine also checked a non-monic example `a_1=2x+3`, `k=5`, including recovery of `g` by the inverse shear.

The constant `k` lives in `K`, not necessarily in a specified integral subring. Example over `Q`: `a_1=2x`, `b_2=x^2` gives `k=1/4` and vanishing `[y^2]`. That is why the shear is a field-level automorphy test and not an allowed `Z_{109}` support gauge.

---

## Claim 3 — affine-in-`y` Keller pairs are automorphisms

**CONFIRMED.**

It remains to treat

```text
f = a_1(x) y + a_0(x),        g = b_1(x) y + b_0(x).
```

Direct expansion, with no `y^{>=2}` terms,

```text
[y] J = a_1' b_1 - a_1 b_1',
[1] J = a_0' b_1 - a_1 b_0'.                                 (3.1)
```

*Both `a_1,b_1` nonzero.* The first identity of (3.1) is again a Wronskian, so `a_1=\lambda b_1` for `\lambda in K`. Set `h=f-\lambda g=a_0-\lambda b_0 in K[x]`. Then `J(h,g)=h' b_1=j in K^*`. A product of two elements of `K[x]` is a nonzero constant if and only if both are nonzero constants: degrees add, and the units of `K[x]` are `K^*`. In characteristic zero, `h'` a nonzero constant forces `deg h=1` (because `deg h'=deg h-1`), so `h=\alpha x+\beta` with `\alpha in K^*`, and `b_1=\gamma` with `\gamma in K^*`. The inverse of `(h,g)` is the polynomial map

```text
x = (h-\beta)/\alpha,        y = (g - b_0(x))/\gamma.         (3.2)
```

Division is by elements of `K^*`, so these are polynomials in `K[h,g]`, not rational functions on `A^2`. Since `(f,g)` differs from `(h,g)` by the constant `GL_2` operation `(h,g)=(f-\lambda g,\, g)`, the pair `(f,g)` is a polynomial automorphism as well: explicitly, `h` is linear in `(f,g)`, then `x` and `y` are polynomial in `(h,g)`.

*Exactly one of `a_1,b_1` is zero.* Both cannot vanish, because then `J=0`. If `a_1=0` and `b_1\neq 0`, then `[y]J=0` automatically and `[1]J=a_0' b_1=j`, so `a_0=\alpha x+\beta` and `b_1=\gamma` as before, giving the same triangular form `f=\alpha x+\beta`, `g=\gamma y+b_0(x)`. If `b_1=0` and `a_1\neq 0`, then `[1]J=-a_1 b_0'`, so `g` is linear in `x` and `f` is affine in `y` with constant `a_1`; this is the previous case after a swap.

Integer controls: `J(2y+x,\, y)=1` with inverse `(f-2g,\, g)`; `J(3x+1,\, 2y+x^2)=6`; `J(2y+x^3,\, 5x-1)=-10`; `J(x,x^2)=0`.

---

## Claim 4 — the field theorem, with no hidden extra hypothesis

**CONFIRMED.**

Composing claims 1--3: start with `deg_y(f),deg_y(g)<=2` and `J(f,g)=j in K^*`. A constant target `GL_2(K)` makes one coordinate affine in `y`. A target shear of determinant one, with polynomial inverse, kills any remaining quadratic term. The resulting affine-in-`y` Keller pair has an explicit polynomial inverse over `K`. Automorphisms form a group, so the original pair is a polynomial automorphism of `A^2_K`.

Hidden-hypothesis checklist:

- *Algebraic closure.* Not used. Wronskian vanishing is decided in `K[x]` by the Euclidean algorithm. The constant field of `(K(x),d/dx)` in characteristic zero is `K`, not `\overline{K}`. Inverse coefficients `1/\alpha`, `1/\gamma` lie in `K` because `\alpha,\gamma in K^*`. The theorem therefore applies to `K=Q_{109}`, which is not algebraically closed.
- *Denominators.* Ratios `a_2/b_2` and `b_2/a_1^2` are formed in `K(x)` as a proof device. Vanishing derivative returns them to `K`. The actual maps `f-\lambda g` and `g-k f^2` remain in `K[x,y]`. The inverse (3.2) divides only by constants in `K^*`. There is no localization of the polynomial ring and no source substitution `y\mapsto y-a_1/(2 a_2)`.
- *Coordinate change.* The only changes are target `GL_2(K)` and the triangular target shear `(u,v)\mapsto(u,v-k u^2)`. Both are polynomial automorphisms of the target plane, stated in the report, and used only to decide automorphy of the original pair. Source coordinates `(x,y)` are never changed. Jung--van der Kulk is not a dependency; the argument is elementary and self-contained for `y`-degree at most two.

Characteristic zero is load-bearing twice: the global factor `2` in (1.1) and (2.1), and `deg \pi'=deg \pi-1` for nonconstant `\pi` (so `ker(d/dx)` on `K[x]` and on `K(x)` is exactly `K`). The theorem is a field theorem: `K` must contain the inverses of the leading constants `\alpha,\gamma`. Both hypotheses are stated.

---

## Claim 5 — application to an exact integral AS109 lift

**CONFIRMED.**

Suppose, for contradiction,

```text
F=(P,Q)=(x-x^{109}+109 A,\; y+109 B),
A,B in Z_{109}[x,y],     deg_y(A), deg_y(B) <= 2,     det J(F)=1.
```

*Correction `y`-degree implies coordinate `y`-degree.* View `P,Q` in `Q_{109}[x,y]`. The summand `x-x^{109}` is independent of `y`, and `109\neq 0` in `Q_{109}`, so `deg_y(P)=deg_y(A)` if `deg_y(A)>=1`, and `deg_y(P)=0` otherwise. Likewise `deg_y(Q)=max(1, deg_y(B))` except possibly if the linear term of `109 B` cancelled the seed `y`. That cancellation would *drop* degree, so `deg_y(Q)<=2` still. (For completeness: it cannot occur for integral `B`, because the coefficient of `y` in `Q` is `1+109 b_1(x)` with `b_1 in Z_{109}[x]`, and `-1/109` is not in `Z_{109}`.) Thus `deg_y(P),deg_y(Q)<=2`. The identity `det J(F)=1` survives the inclusion `Z_{109}\to Q_{109}`. Claim 4 over `K=Q_{109}` makes `F` a polynomial automorphism of `A^2_{Q_{109}}`, hence injective on `Q_{109}^2`.

*Target transforms are not applied to the integral seed.* The `GL_2` step and the shear are internal to the proof of claim 4. They may take coefficients out of `Z_{109}` and may destroy the special fibre `(x-x^{109},y)`. The contradiction is for `F` itself: an automorphism is injective. No claim treats the sheared pair as an AS109 representative.

*Residue-ball noninjectivity, rechecked, not a marked collision.* Reduction modulo `109` is `\overline F=(x-x^{109},y)`. Over `F_{109}` one has `d(x^{109})=109 x^{108}=0`, so `J(\overline F)=I` as a matrix of polynomials, and Fermat `a^{109}=a` for every `a in F_{109}`, so `\overline F(a,b)=(0,b)`. Direct check: `J(x-x^{109},y)=1-109 x^{108}\equiv 1\pmod{109}`, and `a-a^{109}\equiv 0` for all `109` residues. Multivariate Hensel on the complete DVR `Z_{109}`, using that `det J_F` is the constant `1` (hence a unit at every integral point), says that `F` maps each source ball `(a,b)+109 Z_{109}^2` bijectively onto the target ball `(0,b)+109 Z_{109}^2`. The `109` distinct source balls for fixed `b` therefore all cover the same target ball, so any integral target in that ball has `109` distinct preimages in `Z_{109}^2 subset Q_{109}^2`. This is noninjectivity of `F` over `Q_{109}`, contradicting the field theorem.

The collision is a pair of Hensel preimages in distinct residue balls. It is not the frozen marked-section condition `F(0,0)=F(1,0)` as integral lattice-point values. The packed identity `det J=1` over `Z_{109}` is the hypothesis; the truncated two-layer expansion and its base-109 carry are not used. The erratum leaves the Hensel lemma intact, and the different-model carry review confirmed that independence.

---

## Claim 6 — scope exclusions

**CONFIRMED.**

The field theorem and the AS109 application exclude every exact determinant-one lift whose two corrections both have `y`-degree at most two, with no cap on `x`-degree, number of monomials, coefficient height, or linear coupling among those coefficients. They say nothing about a pair in which at least one correction has `y`-degree `>=3`. Cubic and higher remain open. No finite grammar for that range is supplied.

The run produced no lift (`lift_found=false`), no characteristic-zero point, and no JC2 inference (`jc2_inference=false`). An exact lift of this shape cannot exist, so none can be embedded into `C`. The report's statement that this is one excluded exact-lift family, not an arbitrary-AS109 no-go and not a JC2 decision, is accurate. A future `CLOSED-SUPPORT + UNIT-L` certificate for this seed, if one exists, must include at least one monomial of `y`-degree at least three; that is a necessary condition, not a construction.

The parent closed-support artifact is recorded as provisional motivation and is not consumed. The affine-`y` no-go of that line is strictly subsumed by the present field theorem.

---

## Smallest missing hypothesis or overclaim

None of the six claims is an existence theorem, a cubic statement, an arbitrary-support AS109 no-go, or a JC2 decision.

The smallest precisions a reader could miss, and that this review therefore isolates, are:

- Characteristic zero is used for the factor `2` in (1.1)--(2.1) and for `deg \pi'=deg \pi-1`. The identities are polynomial, so they specialise to any ring in which `2` is not a zero-divisor; the *implications* `Wronskian=0 \Rightarrow` linear dependence over `K` need the kernel of `d/dx`.
- The replay's formal support `{0,1,2,5}` is a regression control. Arbitrary `x`-degree is carried by the `y`-degree counting in (1.1), (2.1), and (3.1), which the second engine checked on larger exponent sets. The JSON field `as109_conclusion` is a declared label, not a search result.
- Constants `\lambda` and `k` lie in `K`, not necessarily in `Z_{109}`. That is why the target operations decide automorphy over `Q_{109}` and are not integral gauges.
- Hensel's collision is 109-to-1 covering of residue balls. It does not use marked sections and does not use truncated digit carries.

Those are scope reminders, not missing hypotheses in the written lemmas.

---

## Stop conditions that remain in force

No cap, degree, or prime may be changed in response to this review. Cubic and higher `y`-degree are not licensed as a search by this file. The only resurrection trigger remains a separately reviewed finite coupled section that meets `CLOSED-SUPPORT + UNIT-L` and, by claim 6, allows `y`-degree at least three.

No result here proves or disproves JC2.
