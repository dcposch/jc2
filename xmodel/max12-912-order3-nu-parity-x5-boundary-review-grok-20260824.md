# Hostile different-model review — `(9,12)` order-three `nu!=0` parity `x5=0` boundary

| Field | Value |
|---|---|
| Claim under review | Frozen producer: on the exact parity specialization `q=x0=x2=x4=k=0`, the `x5=0` branch of the `k=mu=0`, `nu!=0` fibre forces `r8=0` and contradicts the terminal Keller row `9*r8'=j/u`; in the remaining parity system the linear pivot `A=x3-2*p*x5` cannot vanish for `nu!=0`. Component probe only |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: `j≠0` and `u≠0` are the frozen Keller/Faber nonvanishing used to read `0≠j/u`; characteristic not `2` or `3` is the ambient Faber inverse-root/`F_j` setting. Neither is a hidden extra hypothesis of this probe) |
| Evidence tier | independent odd/even uniqueness for `f`, `w`, `F_12`, `z(w)` and the odd tails; independent exact reconstruction of `r2,r4,r6,r8` over `Q[x1,x3,x5,p]` from the reviewed binomial `F_12` and `f(z(w))=w^9`; hand substitutions on `x5=0` and `A=0`; two-method resultant `Res_x1(r2,r4)`; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | none named by the launch prompt |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`; producer hashes below are unchanged) |
| Review window (UTC) | 2026-08-24T20:05:00Z – 2026-08-24T20:35:00Z |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, named preflight/Faber inputs, and the spectral-Wronskian report (conventions only) reread in full before any verdict:

- `xmodel/max12-912-order3-nu-parity-x5-boundary-20260824.md`
- `cases/max12_912_order3_nu_parity_x5_boundary_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-partial-y-kummer-preflight-20260824.md` and `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md`
- `xmodel/max12-partial-y-shared-faber-probe-20260824.md` and `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md`
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (pinned parent compiler; no completed fibre review exists in-tree)
- `xmodel/max12-912-order3-spectral-wronskian-ladder-20260824.md` (frozen coordinates and terminal row only; its unreviewed `B`-degree claims are not consumed)

No producer, case, canonical, ladder, coordination, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Accept `ON THE EXACT PARITY SPECIALIZATION q=x0=x2=x4=k=0, THE x5=0 BRANCH OF THE k=mu=0, nu!=0 FIBRE FORCES r8=0 AND CONTRADICTS 9 r8'=j/u; FOR nu!=0 THE PIVOT A=x3-2 p x5 CANNOT VANISH` at the stated scopes.**

- `q=x0=x2=x4=0` makes `f` odd. Unique monic `w=z+O(z^{-1})` with `w^9=f` is odd, so `F_12=[w^{12}]_+` is even. At `k=0` one has `g=F_12` even. Unique `z(w)=w+O(w^{-1})` is odd, so `g(z(w))` is even and `r1=r3=r5=r7=0` identically over `Q`.
- On `x5=0`, `r2=(4/9) x3 (x1-p x3)`. The `x3=0` branch forces `x1=0` from `r4=(2/9) x1^2` and then `r6=0`. The `x3≠0` branch is `x1=p x3`, with `r2=r4=0`, `r6=-(4/81) x3^3=nu`, and `r8=0`.
- `r8=0` as a polynomial identity on that coefficient locus remains `r8=0` along any trajectory supported there. In the Kummer root field `L=C(x)(u)` the frozen Faber terminal is `9 r8'=j/u`. Keller plus `deg_z f=9` give `j≠0` and `u≠0`, so `0≠j/u`. The locus is a genuine coefficient-fibre component and is not a trajectory.
- `r2=(4/9) A x1 + (x1-free)`, `A=x3-2 p x5`. On `A=0` one has `r2=-(4/81) p x5^3`. The fibre equation `r2=0` in an integral domain is `p=0` or `x5=0`; both force `x3=0` and then `r6=0`. Hence `nu≠0` implies `A≠0`, with no division by `A`, `p`, or `x5`.
- `Res_x1(r2,r4)=(-16/59049) x5 P4` with `P4` of weighted degree `24` not divisible by `A`. Retaining the `x5` factor exposes the terminally impossible component. After that component and `A=0` are removed, reversible elimination of `x1` lives on the fail-closed chart `A x5 ≠ 0`. That chart is not claimed empty.

**Do not promote this to:** exhaustion of the loaded fibre by the parity locus; emptiness of the remaining `A x5 ≠ 0` chart; any generic loaded component; Taylor-boundary compatibility; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

**Smallest valid successor.** The remaining parity chart `A x5 ≠ 0`, treating subsequent resultants as licensed only there. Do not open a generic coefficient rectangle or AWS. Do not treat this probe as a parity-exhaustion theorem.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, proves that every loaded solution has the parity `(1.1)`, closes `A x5 ≠ 0`, empties a generic `nu≠0` component, or closes maximum twelve. Producer replay output was not used as evidence; `F_12`, the inverse root `z(w)`, the eight tails, the `x5=0` and `A=0` substitutions, and `Res_x1(r2,r4)` were re-derived over `Q`. The reviewed preflight is consumed only for the order-three leaf, `delta=0`, and `z=u y`. The reviewed Faber theorem is consumed only for `F_j=z^j [sum_k binom(j/m,k) U^k]_+`, the tail sign `H(w)-g(z(w))=sum r_ell w^{-ell}`, and `9 r8'=j/u`. The fibre compiler is not a reviewed theorem. The spectral-Wronskian report is used only for the frozen names `K=z^3+p z+q`, `k=0` with `g=w^{12}-T`, and the same terminal row; its `B`-degree table is unused.

---

## Scope (not enlarged)

Exact parity `x5=0` trajectory exclusion and `A`-chart reversal on `q=x0=x2=x4=k=0`. Parity exhaustion, the remaining `A x5 ≠ 0` chart, the generic loaded fibre, Taylor boundaries, all `(9,12)`, maximum twelve, a counterexample, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `K=z^3+p z+q` and exact `F_12`, the specialization `q=x0=x2=x4=k=0` makes `f` odd, `g` even, and `r1=r3=r5=r7=0` identically, with no hidden characteristic or normalization assumption | **CONFIRMED** | a non-odd term in `f` on this slice; a non-even polynomial part of `w^{12}`; a uniqueness failure for `w=z+O(z^{-1})` or `z=w+O(w^{-1})` in characteristic zero; an odd tail monomial in the independent expansion |
| 2 | On `x5=0`, the `x3=0` branch forces `x1=0` then `r6=0`; the `x3≠0` branch is `x1=p x3` with `r6=-(4/81) x3^3=nu` and `r8=0` identically | **CONFIRMED** | `r2` not equal to `(4/9) x3 (x1-p x3)` at `x5=0`; `r4` not equal to `(2/9) x1^2` at `x3=x5=0`; a surviving `r8` monomial after `x1=p x3`, `x5=0`; `r6` not equal to `-(4/81) x3^3` on that branch |
| 3 | The locus is a coefficient-fibre component and cannot be a trajectory: `9 r8'=j/u` in `L=C(x)(u)`, and `r8=0` contradicts `j/u≠0` | **CONFIRMED** | a hidden extra hypothesis beyond frozen Keller `j≠0` and leading-root `u≠0`; `r8` depending on `x`-derivatives of the coefficients; a sign error making the terminal `-j/u`; `r8` not identically zero as a polynomial on the locus |
| 4 | `A=x3-2 p x5`; `r2|_{A=0}=-(4/81) p x5^3`; both integral-domain branches of `r2=0` force `nu=0`; therefore `nu≠0 ⇒ A≠0` with no division by a possibly zero quantity | **CONFIRMED** | `r2|_{A=0}` not equal to `-(4/81) p x5^3`; `r6` not in the ideal `(p,x3)`; `r4|_{x3=x5=0}` not `(2/9) x1^2`; a third branch of `p x5^3=0` in an integral domain |
| 5 | `Res_x1(r2,r4)=(-16/59049) x5 P4`; the remaining fail-closed chart is exactly `A x5 ≠ 0`; no emptiness statement about that chart is in the producer conclusion | **CONFIRMED** | a different scalar or missing `x5` factor; `P4` identically zero; a smuggled emptiness or Taylor claim about `A x5 ≠ 0` in the report, registration, or replay payload |
| 6 | Scope is only this parity component probe | **CONFIRMED** | a hidden promotion in the report, registration, README, FREEZE, or replay payload |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-nu-parity-x5-boundary-20260824.md` | `9f62c226b0bb9ce3ec7ce9d96543ebae5cb6f6ee4bcfd32c00d25f4f27fe51e7` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `92db1e820f2562143aa2192fac90e7bc61912324c9bf14df6c2132ed80455731` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `0b6405b069ac2cf7a87501154016ab0401fb3561d60f30898d4004c9d06a3b7a` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `9f05a4ed65dc544cad2753a77e599dd58a141e841bc27fe18a38436790c69742` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `30581351bb0d92b128d49dbaf0a06dd81e802149ef408541adf99851444f60ff` | `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `be8dd3efa89cb5e767e63b25080322cdeddc506c39aca8f2f313f2dd0ba92ace` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `b572ed0d90de10a6e0068ee36bd6632f9c356860cbce7bc1308d63648f9876b4` | prompt only |

Predecessor hashes recomputed, not used as mathematical evidence:

| Artifact | SHA-256 |
|---|---|
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` |
| `cases/max12_high_row_probe_20260824/FREEZE.sha256` | `3a25edb31a53ecee9c96e039ab4a947908ebc0542123fb131447e1a661f45a28` |
| `cases/max12_partial_y_preflight_20260824/FREEZE.sha256` | `59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558` |
| `xmodel/max12-912-order3-spectral-wronskian-ladder-20260824.md` | `6a7715597126b2b655bf0f8cc955597c093420132b240c1d31780f6221ef3a05` |

The parent-compiler pin inside `replay.py` matches the fibre-compiler hash above. `shasum -a 256 -c cases/max12_912_order3_nu_parity_x5_boundary_20260824/MANIFEST.sha256` exits `0`. `python3 cases/max12_912_order3_nu_parity_x5_boundary_20260824/replay.py | diff -u cases/max12_912_order3_nu_parity_x5_boundary_20260824/replay.json -` exits `0`. The replay checks odd-tail vanishing, the `x3=x5=0` strings for `r4` and `r6`, the branch `x1=p x3` with `r6=-(4/81) x3^3` and `r8=0`, the `A=0` string for `r2`, and `r6=0` on `p=x3=0`. It does not expand the full even tails, does not compute `Res_x1(r2,r4)`, and does not differentiate `r8`. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present.

---

## Claim 1 — odd `f`, even `g`, odd tails zero

**CONFIRMED.**

Work in characteristic zero. Approximate-cubic coordinates are already monic and depressed: `K=z^3+p z+q` and `f=K^3+sum_{i=0}^5 x_i z^i`. Specializing `q=x0=x2=x4=0` gives

```text
K=z^3+p z,          K(-z)=-K(z),
K^3 odd,
x1 z+x3 z^3+x5 z^5 odd,
```

so `f(-z)=-f(z)`. Explicitly

```text
f=z^9+3p z^7+(3p^2+x5) z^5+(p^3+x3) z^3+x1 z.
```

Let `w` be the unique element of `C((z^{-1}))` with `w^9=f` and `w=z+O(z^{-1})` (reviewed Faber normalization). Then `-w(-z)` has the same leading term and the same ninth power, because `9` is odd, so uniqueness forces `w(-z)=-w(z)`. Thus `w^{12}` is even, and the polynomial part `F_12=[w^{12}]_+` is an even polynomial. Independently, the reviewed binomial

```text
F_12=z^{12} [sum_{k=0}^6 binom(4/3,k) U^k]_+,
U=f/z^9-1=3p z^{-2}+(3p^2+x5) z^{-4}+(p^3+x3) z^{-6}+x1 z^{-8}
```

has only even powers of `z` because `U` is even. Direct expansion produces support `{12,10,8,6,4,2,0}` with leading term `z^{12}`. At `k=0` one has `g=F_12`, hence `g` even. (`k F_6` would be even as well, since `F_6=[w^6]_+` is even; `k=0` is the fibre specialization as stated, not a hidden extra hypothesis for evenness.)

The inverse root `z(w)` with `f(z(w))=w^9` and `z=w+O(w^{-1})` is likewise unique and odd. An even polynomial in an odd series is even, so `g(z(w))` has only even powers of `w`. The reviewed tail sign is `H(w)-g(z(w))=sum_{ell>=1} r_ell w^{-ell}` with `H(w)=w^{12}` at `k=0`, so `r_ell=-[w^{-ell}] g(z(w))`. Therefore `r1=r3=r5=r7=0` identically. Independent inversion through `w^{-19}` (the order needed for `[w^{-8}]` of `z^{12}`) produces only odd powers of `w` in `z(w)` and identically zero odd tails.

No further normalization is used: depression is already built into `K`, and the only uniqueness is the frozen monic root. Denominators in `binom(4/3,k)` and in the inverse-root step `1/9` require characteristic not `3`; odd/even requires characteristic not `2`. Both are the ambient Faber/Keller setting, not a hidden hypothesis of this probe.

---

## Claim 2 — even tails on `x5=0`

**CONFIRMED.**

Independent reconstruction over `Q[x1,x3,x5,p]` gives the even tails (odd tails already zero)

```text
r2 = (4/9)(x3-2 p x5) x1
     - (4/9) x3^2 p - (4/27) x3 x5^2 + (4/3) x3 x5 p^2 + (20/81) x5^3 p - (8/9) x5^2 p^3,

r4 = (2/9) x1^2
     + x1 ( -(16/27) x3 p - (4/27) x5^2 + (20/27) x5 p^2 )
     + (10/27) x3^2 p^2 - (4/27) x3^2 x5 + (52/81) x3 x5^2 p - (8/9) x3 x5 p^3
     + (5/243) x5^4 - (140/243) x5^3 p^2 + (14/27) x5^2 p^4,

r6 = - (4/81) x3^3 - (4/27) x1^2 p - (16/81) x1 x3 x5 + (8/27) x1 x3 p^2
     + (28/81) x1 x5^2 p - (8/27) x1 x5 p^3 + (4/9) x3^2 x5 p - (4/27) x3^2 p^3
     + (4/81) x3 x5^3 - (80/81) x3 x5^2 p^2 + (8/27) x3 x5 p^4
     - (20/243) x5^4 p + (152/243) x5^3 p^3 - (4/27) x5^2 p^5,

r8 = - (4/81) x1 x3^2 - (4/81) x1^2 x5 + (2/81) x1^2 p^2 + (4/81) x3^3 p
     + (further 15 monomials in x1,x3,x5,p).
```

Every monomial of `r2` is weighted-homogeneous of weight `14` for `wt(z)=1`, `wt(p)=2`, `wt(x_i)=9-i`. Similarly `r4,r6,r8` have weights `16,18,20`. The coefficient of `x1` in `r2` is exactly `(4/9)A` with `A=x3-2 p x5`. Degree in `x1` is `1` for `r2` and `2` for `r4`.

On `x5=0`:

```text
r2 = (4/9) x3 (x1 - p x3),
r4 = (2/9) x1^2 - (16/27) x1 x3 p + (10/27) x3^2 p^2,
r6 = - (4/27) x1^2 p + (8/27) x1 x3 p^2 - (4/27) x3^2 p^3 - (4/81) x3^3,
r8 = (2/81) x1^2 p^2 - (32/729) x1 x3 p^3 + (14/729) x3^2 p^4 - (4/81) x1 x3^2 + (4/81) x3^3 p.
```

If `x3=0` as well, then `r2=0` automatically and `r4=(2/9) x1^2`. In characteristic not `2` or `3`, `r4=0` forces `x1=0`, and then `r6=0` (equivalently the slice identity `r6=-(4/27) x1^2 p` vanishes). This contradicts `r6=nu≠0`. Thus `x3≠0`, and `r2=0` is `x1=p x3` with no division by a vanishing `x3` on this branch.

Substituting `x1=p x3` and `x5=0` into the four even tails yields

```text
r2=r4=0,     r6=-(4/81) x3^3,     r8=0
```

identically in `(x3,p)`. The identity `r6=-(4/81) x3^3` is the fibre load `nu`. The normalized slice `x3^3=-81/4` is `nu=1` and is not required for `r8=0`.

---

## Claim 3 — coefficient fibre versus trajectory

**CONFIRMED.**

The equations `x5=0`, `x1=p x3`, `x3^3=-(81/4) nu` cut a nonempty algebraic set in the coefficient ring (three constant cube roots of `-(81/4) nu`, with `p` free at this stage). On that set `r2=r4=0` and `r8=0` as polynomial identities, so the locus is a genuine coefficient-fibre component of the parity system. It is not thereby a trajectory.

A trajectory specializes the coefficients to elements of the Kummer root field `L=C(x)(u)`, `u^3=h`, with derivation extending `d/dx`. Polynomial identities remain identities after specialization, so `r8` is the zero element of `L` along any such map, hence `r8'=0`.

The reviewed Faber terminal for `(m,n)=(9,12)` is

```text
r1'=⋯=r7'=0,     9 r8'=j/u.                          (0.1)
```

The field is `L`. Nonvanishing: `j` is the original Keller constant, nonzero by definition of a Keller pair; `u` is the leading root with `a_9=u^9≠0`. Equivalently `9 u r8'=j` still yields `0=j`. The producer’s comparison `9 r8'=0 ≠ j/u` is therefore exactly the terminal equation on this locus. There is no sign ambiguity: the reviewed fixed-`w` identity puts a plus sign on `sum r_ell' w^{-ell}` relative to `H(w)-g(z(w))`.

`r8` is an algebraic function of the coefficients, not of their `x`-derivatives, so a coefficient identity `r8=0` cannot hide a nonzero derivative. Weight `2` writes `r8=u^2 R` with `R=0` here; the descended ODE `9 h R'+6 h' R=j` likewise becomes `0=j`. Taylor boundaries are unused.

---

## Claim 4 — `A=0` and `nu≠0 ⇒ A≠0`

**CONFIRMED.**

Substitute `x3=2 p x5` into `r2` (equivalently, the `x1`-coefficient `(4/9)A` vanishes and the remaining polynomial is the constant term). Direct expansion:

```text
p^3 x5^2 terms:  -16/9 + 8/3 - 8/9 = 0,
p x5^3 terms:    -8/27 + 20/81 = -4/81,
```

so `r2|_{A=0}=-(4/81) p x5^3`. In an integral domain the fibre equation `r2=0` is `p=0` or `x5=0`. No division by `A`.

- If `x5=0`, then `A=0` forces `x3=0`. Claim 2 gives `r4=(2/9) x1^2`, hence `x1=0`, hence `r6=0`.
- If `p=0`, then `A=0` forces `x3=0`. Every monomial of `r6` is divisible by `p` or by `x3`, so `r6∈(p,x3)` and `r6|_{p=x3=0}=0` identically in `(x1,x5)`.

Both branches yield `nu=0`. Contrapositively, `nu≠0` implies `A≠0`. The two branches exhaust `p x5^3=0` in an integral domain; there is no residual branch in which `A=0` and `r2=0` with `nu≠0`.

---

## Claim 5 — resultant, remaining chart, no smuggling

**CONFIRMED.**

`r2` is linear in `x1` and `r4` is quadratic. The Sylvester determinant and the evaluation formula `a1^2 r4(-a0/a1)` agree, and

```text
Res_x1(r2,r4) = (-16/59049) x5 P4,
59049 = 3^{10},
P4 = 108 x3^4 - 756 p x5 x3^3 + (1980 p^2 x5^2 + 3 x5^3) x3^2
     - (2304 p^3 x5^3 + 12 p x5^4) x3 + 1008 p^4 x5^4 + 10 p^2 x5^5.
```

In the chart coordinate `A=x3-2 p x5`,

```text
P4 = 108 A^4 + 108 p x5 A^3 + (36 p^2 x5^2 + 3 x5^3) A^2 - 2 p^2 x5^5.
```

The `A`-valuation is `0`, so `A` does not divide `P4`. The `x5` factor of the resultant is exact (valuation `1` on the primitive polynomial). Retaining it is what makes the `x5=0` component of `r2=r4=0` visible; that component is the terminally impossible locus of Claim 2. `A=0` is not a resultant component except along `x5=0` or `p=0`, which is why `A=0` is excluded by Claim 4 rather than by `P4`.

After `x5=0` is killed by the terminal row and `A=0` is killed by `nu≠0`, the remaining parity route lies on `A x5 ≠ 0`. There `deg_{x1} r2=1` and the leading coefficient `(4/9)A` is a unit of the chart, so `r2=0` solves `x1` reversibly. That is exactly the fail-closed chart `(3.3)`. Subsequent resultants are licensed only there: a routing statement, not an emptiness claim.

Producer conclusion, registration, README, FREEZE, and replay payload assert only: the parity `x5=0` branch is incompatible with the terminal Keller row, and `A=0` is empty for `nu≠0`. None of them asserts emptiness of `A x5 ≠ 0`, Taylor compatibility, generic-fibre emptiness, all `(9,12)`, maximum twelve, a counterexample, or JC2.

---

## Claim 6 — scope

**CONFIRMED.**

The report’s “Not concluded” list, the registration’s last sentence, the replay `scope` string, and the FREEZE `scope` block all stay inside this parity component probe. The specialization `(1.1)` is stated as a component probe, not as an assertion that every loaded solution has that parity. No numbered claim is enlarged.

---

## Non-blocking remarks

- The replay is a correct regression of a subset of the identities. Absence of an in-replay resultant is not a mathematical gap: `Res_x1(r2,r4)` was recomputed independently by two methods.
- `k=0` is not needed for evenness of `g` (`F_6` is even whenever `f` is odd). It is the `k=0` fibre being probed, as written.
- The inverse series `z(w)` has vanishing `w^{-9}` coefficient on this parity slice. That is a vanishing, not a missing term in the inversion, and is unused.
- The fibre compiler has no completed different-model review. Tails used as evidence were rebuilt from the reviewed `F_12` binomial and `f(z(w))=w^9`. A post-hoc comparison with the pinned parent compiler matches coefficient-for-coefficient and is not evidence.

---

## What this does not license

This review does not license: parity exhaustion of `nu≠0`; emptiness of `A x5 ≠ 0`; any generic loaded component; Taylor-boundary reconstruction; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.
