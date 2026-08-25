# Hostile different-model review — `(9,12)` order-three `nu!=0` full parity genus-five exclusion

| Field | Value |
|---|---|
| Claim under review | Frozen producer: no actual `nu!=0` order-three Keller trajectory lies on the full odd/even specialization `q=x0=x2=x4=k=0`. The branches `x5=0`, `A=0`, `p=0`, and `p*x5*A!=0` are exhaustive; on the last, `v=A/(p*x5)` lands on a cyclic genus-five curve and is constant, forcing `r8` constant against the terminal row |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the order-three fibre compiler has no completed different-model review and is not consumed; tails used as evidence were rebuilt from the reviewed binomial `F_12` and `f(z(w))=w^9`. Characteristic not `2` or `3` is the ambient Faber inverse-root/`F_j` setting. `j≠0` and `u≠0` are the frozen Keller/Faber nonvanishing used to read `9 r8'=j/u≠0`) |
| Evidence tier | independent odd/even uniqueness for `f`, `w`, `F_12`, `z(w)` and the odd tails; independent exact reconstruction of `r2,r4,r6,r8` over `Q[x1,x3,x5,p]`; hand substitutions on `x5=0`, `A=0`, and `p=0`; independent rational-function solve in `v` recovering `(3.2)`–`(3.6)`; Euclidean gcd and Sylvester resultants for `A5,D,A2,A4`; Kummer-character weights; cube-divisor test in `C(v)^*`; Riemann–Hurwitz on the cyclic cover and the no-map step from `P^1_x` including extension across poles; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | none named by the launch prompt |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | `2026-08-24T20:35:34Z` – `2026-08-24T21:05:00Z` |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, frozen `x5=0` predecessor, reviewed preflight/Faber inputs, and the confirmed DZ20 coprimality/constant-field firewall reread in full before any verdict:

- `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md`
- `cases/max12_912_order3_nu_parity_genus5_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-912-order3-nu-parity-x5-boundary-20260824.md` and `xmodel/max12-912-order3-nu-parity-x5-boundary-review-grok-20260824.md`
- `xmodel/max12-partial-y-kummer-preflight-20260824.md` and `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md`
- `xmodel/max12-partial-y-shared-faber-probe-20260824.md` and `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md`
- `xmodel/max12-912-order3-dz20-stabilizer-valuation-review-grok-20260824.md` (actual-Keller constant-field and coprimality facts only)
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (pinned parent compiler; no completed fibre review exists in-tree; unused as a theorem)

No producer, case, canonical, ladder, coordination, prompt, log, run, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Accept `NO ACTUAL nu!=0 ORDER-THREE KELLER TRAJECTORY LIES ON THE FULL PARITY SPECIALIZATION q=x0=x2=x4=k=0` at the stated scopes.**

- `q=x0=x2=x4=0` makes `f` odd. Unique monic `w=z+O(z^{-1})` with `w^9=f` is odd, so `F_12=[w^{12}]_+` is even. At `k=0` one has `g=F_12` even. Unique `z(w)=w+O(w^{-1})` is odd, so odd tails vanish identically over `Q`. The loaded fibre on this slice is `r2=r4=0`, `r6=nu in C^*`, `9 r8'=j/u≠0`.
- On `x5=0`, the frozen predecessor (reconfirmed below) forces `x1=p x3`, `r6=-(4/81) x3^3=nu`, and `r8=0`, contradicting the terminal row. On `A=x3-2 p x5=0`, one has `r2=-(4/81) p x5^3`; both integral-domain branches force `nu=0`. These are identities of elements of the function field, not vanishing-at-places statements.
- On `p=0` with `x5 A≠0`, the exact rows give `x1=x5^2/3`, `x3^2=-x5^3/36`, `nu=-(11/729) x3 x5^3`, `r8=-x5^5/486`, hence `r8^9=(2*3^{25}/11^{10}) nu^{10}`. The right-hand side is a nonzero constant, so `r8` is differential-constant, again contradicting the terminal row.
- On `p*x5*A≠0`, the weight-zero quotient `v=A/(p x5)` lies in `K=C(x)`. The row `r2=0` solves `x1` reversibly; `r4=0` solves `x5` reversibly as `x5=-36 p^2 v^2 (3v^2+3v+1)/(3v^2-2)`. The denominators `v` and `3v^2-2` are nonzero as elements of `K`. Places at which they vanish are retained as branch data.
- Order-three character two writes `p=u^2 P` with `P in K`, so `p^9=(h^2 P^3)^3` is a cube in `K`. The load `nu in C^*` is a cube because `C` is algebraically closed. Thus `R6(v)` is a cube in `K`. Removing the displayed cube factors leaves `Y^3=A5(v)/D(v)` with `Y in K`.
- Over `C`, `A5` has five simple roots, `D` has two simple roots, and these seven points are pairwise disjoint. Each is totally ramified of index three. At infinity `A5/D` has pole order exactly `-3`, hence is unramified. Riemann–Hurwitz gives genus five. The affine equation is not a cube in `C(v)`, so the cyclic cover is geometrically irreducible. Its smooth projective model admits no nonconstant morphism from `P^1_x`, including after extending the rational map across poles of `v` and of `Y`. Thus `v` is constant.
- Constant `v` makes `p^9` constant, hence `p` constant in `L` (constant field `C`). Then `r8=p^{10} R8(v)` is constant, contradicting `9 r8'=j/u≠0`.

**Do not promote this to:** parity exhaustion of the complete loaded fibre; exclusion of a non-parity component; either Taylor-boundary family; the order-one core; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

**Smallest valid successor.** Remaining non-parity components of the `k=mu=0`, `nu≠0` fibre. Do not open a generic coefficient rectangle or AWS. Do not treat this theorem as a statement that every loaded solution has parity `(1.1)`.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, proves that every loaded solution has the parity `(1.1)`, empties a non-parity component, or closes maximum twelve. Producer replay output was not used as evidence; `F_12`, the inverse root `z(w)`, the four even tails, the `x5=0`/`A=0`/`p=0` substitutions, the `v`-chart identities, the gcd/resultant ledger, the cube-divisor test, and Riemann–Hurwitz were re-derived over `Q` and `C`. The reviewed preflight is consumed only for the order-three leaf, `delta=0`, and `z=u y` with `sigma(z)=zeta z`. The reviewed Faber theorem is consumed only for `F_j=z^j [sum_k binom(j/m,k) U^k]_+`, the tail sign `H(w)-g(z(w))=sum r_ell w^{-ell}`, and `9 r8'=j/u`. The DZ20 review is consumed only for the already-confirmed facts that the constant field of `L` is `C` and that an actual Keller Jacobian `D=j/u` is a nonzero `z`-constant (the latter is used here only as `j≠0`, `u≠0`). The fibre compiler is not a reviewed theorem. Taylor boundaries remain charged and unused.

---

## Scope (not enlarged)

Emptiness of actual `nu≠0` order-three trajectories on the specialization `q=x0=x2=x4=k=0`. Parity exhaustion of the loaded fibre, non-parity components, Taylor boundaries, the order-one core, all `(9,12)`, maximum-twelve coverage, a counterexample, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The four branches `x5=0`, `A=0`, `p=0` with `x5 A≠0`, and `p*x5*A≠0` exhaust the parity locus. Zero-as-element is distinguished from vanishing-at-places; places are retained in the divisor calculation | **CONFIRMED** | a fifth integral-domain branch of `p x5 A=0`; `A=0` compatible with `nu≠0`; a place-vanishing of `D` or `A2` smuggled into an element-identity exclusion; a residual chart with `x5=0` and `A≠0` not already killed by `r8=0` |
| 2 | On `p*x5*A≠0`, `x1=x5 p^2 (v+1)+x5^2 (3v+1)/(9v)` and `x5=-36 p^2 v^2 (3v^2+3v+1)/(3v^2-2)` are reversible in `K`; `r6=p^9 R6(v)` and `r8=p^{10} R8(v)` match `(3.5)`–`(3.6)`. On `p=0`, `r8^9=(2*3^{25}/11^{10}) nu^{10}` | **CONFIRMED** | a different `x1` or `x5` identity; `Res(3v^2-2, 3v^2+3v+1)≠27`; `R6` or `R8` not equal to the displayed rational functions; a different scalar in the `p=0` projection; a surviving nonconstant `r8` on `p=0` |
| 3 | `v` has weight zero, hence lies in `K=C(x)`. Character two writes `p=u^2 P` with `P in K`, so `p^9=(h^2 P^3)^3` is a cube in `K`. The constant `nu` is a cube in `C subset K` | **CONFIRMED** | `wt(A/(p x5))≠0 mod 3`; `p/u^2` not Galois-invariant; `p^9` a cube only in `L` and not in `K`; constant field of `L` larger than `C`; `nu` of nonzero character |
| 4 | Removing cubes from `R6` leaves `Y^3=A5(v)/(3v^2-2)` with `Y in K`. The leftover `A5/D` is not a cube in `C(v)` | **CONFIRMED** | a cube factor of `A5` or of `D` incorrectly discarded or retained; `A5/D` already a cube in `C(v)`, collapsing the cover to `P^1`; `Y` only in a proper extension of `K` |
| 5 | `gcd(A5,A5')=gcd(D,D')=gcd(A5,D)=1`, `Res(A5,D)=97200`. Seven finite simple branch points of index three; infinity of order `-3` unramified; `2g-2=8`, `g=5`. No hidden plane-model singularity changes the function-field genus | **CONFIRMED** | a multiple root of `A5` or of `D`; a common root of `A5` and `D`; leading-coefficient cancellation at infinity making the pole order not divisible by three, or making it ramified; Riemann–Hurwitz off by a ramification unit |
| 6 | A nonconstant `v in C(x)` would give a nonconstant morphism `P^1_x to` the smooth projective model of `(4.1)`, impossible by Riemann–Hurwitz. Rational maps from a smooth curve to a projective curve extend across poles | **CONFIRMED** | `Y` not in `C(x)`, so the source would be a positive-genus Kummer cover of `P^1_x`; a non-extendable pole of `(v,Y)`; a constant morphism with nonconstant `v` |
| 7 | Constant `v` forces `R6(v) in C^*`, hence `p^9` constant, hence `p` constant in `L`, hence `r8` constant, contradicting `9 r8'=j/u≠0`. No `D=0` or `A2=0` constant value of `v` survives the chart | **CONFIRMED** | `R6(v)=0` compatible with `nu≠0`; a nonconstant 9th root of a constant in `L`; `r8` moving while `p` and `v` are constant; `j/u=0` on an actual Keller trajectory |
| 8 | Strongest licensed conclusion is emptiness of this parity locus. Not the full loaded fibre, not Taylor, not all `(9,12)`, not maximum twelve, not a counterexample, not JC2 | **CONFIRMED** | a hidden promotion in the report, registration, README, FREEZE, or replay payload |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` | `f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `5e86d300600d05af87b3791bb641e2e9168b5191ec2c007927fec3e9cb812c7d` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `7e10100f50c7b80502354a528500c035d11e1c60d21ccda041a461626adb8cde` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `c965bb660cf2f0f55c7ebbed3126b22bfb5d67e178565426aa94ce56f6ce1d9a` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `4b397ff751d31fb14f9dfafc669549c453e292b94ca952ff21f7f58507c03fb0` | `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `07bde6525d798777afee038560a77cb0b02e908808ecd0a2abb857ebf0151010` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `5bc9e303bc9d9e9fb16956d7bdc2afade902ba5a51238e5925f9e1cf8dfb8537` | prompt only |

Predecessor hashes recomputed, not used as mathematical evidence beyond the licensed inputs named above:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-912-order3-nu-parity-x5-boundary-20260824.md` | `9f62c226b0bb9ce3ec7ce9d96543ebae5cb6f6ee4bcfd32c00d25f4f27fe51e7` |
| `xmodel/max12-912-order3-nu-parity-x5-boundary-review-grok-20260824.md` | `ae5f5d54dea1727e8bd413f21b8adacb1793ee81d8d44b85d02fde21d2683176` |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` |
| `xmodel/max12-912-order3-dz20-stabilizer-valuation-review-grok-20260824.md` | `a8d7282ff98a0dfd998c52bfc60eed7e9f64ff89e6a988682ef8e80202229300` |
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` |

The parent-compiler pin inside `replay.py` matches the fibre-compiler hash above. `shasum -a 256 -c cases/max12_912_order3_nu_parity_genus5_20260824/MANIFEST.sha256` exits `0`. `python3 cases/max12_912_order3_nu_parity_genus5_20260824/replay.py | diff -u cases/max12_912_order3_nu_parity_genus5_20260824/replay.json -` exits `0`. The replay checks the generic `v`-chart identities against the pinned compiler, the gcd/resultant/genus ledger, and the unreduced `p=0` tail strings together with two scalar reductions. It does not prove that `v` is Galois-invariant, does not construct a morphism from `P^1_x`, and does not differentiate `r8`. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present.

---

## Claim 1 — exhaustion, elements versus places

**CONFIRMED.**

Work in characteristic zero. Approximate-cubic coordinates are already monic and depressed: `K=z^3+p z+q` and `f=K^3+sum_{i=0}^5 x_i z^i`. Specializing `q=x0=x2=x4=0` gives

```text
f=z^9+3p z^7+(3p^2+x5) z^5+(p^3+x3) z^3+x1 z,
```

which is odd. Unique monic `w=z+O(z^{-1})` with `w^9=f` is odd because `9` is odd, so `F_12=[w^{12}]_+` is even. At `k=0` one has `g=F_12`. Unique `z(w)=w+O(w^{-1})` is odd, so `g(z(w))` is even and `r1=r3=r5=r7=0` identically. Independent inversion through `w^{-19}` produces only odd powers of `w` in `z(w)` and identically zero odd tails. Independent binomial expansion of `F_12` has support `{12,10,8,6,4,2,0}`.

The fibre equations on this slice are therefore `r2=r4=0`, `r6=nu in C^*`, and the terminal `9 r8'=j/u≠0`. Independent reconstruction over `Q[x1,x3,x5,p]` yields seven monomials in `r2`, eleven in `r4`, fourteen in `r6`, and nineteen in `r8`, all weighted-homogeneous of weights `14,16,18,20` for `wt(z)=1`, `wt(p)=2`, `wt(x_i)=9-i`. The coefficient of `x1` in `r2` is exactly `(4/9)A` with `A=x3-2 p x5`:

```text
r2 = (4/9) A x1
     - (4/9) x3^2 p - (4/27) x3 x5^2 + (4/3) x3 x5 p^2 + (20/81) x5^3 p - (8/9) x5^2 p^3.
```

This matches the frozen `x5=0` predecessor coefficient-for-coefficient.

**`x5=0` as an element.** Already confirmed in the frozen predecessor and reconfirmed here. The `x3=0` sub-branch forces `x1=0` from `r4=(2/9) x1^2` and then `r6=0`. The `x3≠0` sub-branch is `x1=p x3`, with `r2=r4=0`, `r6=-(4/81) x3^3=nu`, and `r8=0` identically. Polynomial identity `r8=0` remains `r8=0` after specializing coefficients into `L=C(x)(u)`, so `r8'=0`, contradicting `j/u≠0`.

**`A=0` as an element.** Substitute `x3=2 p x5`. Direct expansion of the `x1`-free part of `r2` cancels the `p^3 x5^2` terms and leaves `r2=-(4/81) p x5^3`. In an integral domain this is `p=0` or `x5=0`. Both force `x3=0` and then `r6=0` (every monomial of `r6` lies in the ideal `(p,x3)` on this slice; independently, `r6|_{p=x3=0}=0` as a polynomial in `(x1,x5)`). Thus `nu≠0` implies `A≠0` as an element of `L`. No division by `A`.

**`p=0` as an element, with `x5 A≠0`.** Treated in Claim 2. It is a genuine remaining branch: `A=x3` when `p=0`, and `A≠0` has already forced `x3≠0`.

**`p*x5*A≠0` as elements.** The complementary chart. Places of `P^1_x` at which `p`, `x5`, or `A` vanish are allowed; those places are not a fifth branch of the coefficient tree.

The four-row table in the producer’s §5 is therefore complete. Zero-as-element versus vanishing-at-places is observed throughout: `3v^2-2` and `3v^2+3v+1` are forbidden as zero elements of `K` (Claim 2) and are retained as places in the ramification divisor (Claim 5). A place at which `D(v)=0` is a branch point of the cyclic cover, not a missed coefficient component.

---

## Claim 2 — the `v`-solve, denominators, and the `p=0` projection

**CONFIRMED.**

### Generic chart

On `p*x5*A≠0` set `v=A/(p x5)`, so `A=p x5 v` and `x3=p x5 (v+2)`. From `r2=0` and the displayed `x1`-coefficient,

```text
x1 = -(9/4) C / A,
```

where `C` is the `x1`-free part of `r2`. Substituting `x3=p x5 (v+2)` groups as

```text
C = -(4/9) v(v+1) p^3 x5^2 - (4/81)(3v+1) p x5^3,
```

hence

```text
x1 = x5 p^2 (v+1) + x5^2 (3v+1)/(9v).                 (3.2)
```

The denominator `9v` is nonzero as an element because `v=0` is `A=0`, already excluded. Characteristic not `3` is ambient.

Independent substitution of `(3.2)` into `r4` produces the identity

```text
(3v^2-2) x5 + 36 p^2 v^2 (3v^2+3v+1) = 0.            (3.3)
```

Write `D(v)=3v^2-2` and `A2(v)=3v^2+3v+1`. Sylvester resultant `Res(D,A2)=27≠0`, so these two polynomials have no common root in `C`. Consequently:

- If `D` is the zero element of `K`, then `v` is constantly a root of `D`, hence `A2(v)∈ C^*`, and `(3.3)` becomes `36 p^2 v^2 A2=0`. On the chart `p≠0` and `v≠0`, this is impossible.
- If `A2` is the zero element of `K`, then `(3.3)` forces `D x5=0`, hence `x5=0` as an element, already excluded.

Every subsequent division by `D` is therefore reversible in `K`. Places at which `D` or `A2` vanish are not excluded here; they appear in Claim 5. Solving `(3.3)` gives

```text
x5 = -36 p^2 v^2 A2(v) / D(v).                         (3.4)
```

Weighted homogeneity of the even tails (weights `14,16,18,20` for `r2,r4,r6,r8`; `wt(p)=2`) writes `r6=p^9 R6(v)` and `r8=p^{10} R8(v)` after substituting `(3.2)` and `(3.4)`. Independent rational-function arithmetic in the chart `p=1`, restoring `p`-powers by weight, yields exactly

```text
R6(v) = -2304 v^6 A2(v)^3 A5(v) / D(v)^4,
R8(v) =  6912 v^8 A2(v)^4 A4(v) / D(v)^5,
```

with

```text
A5(v)=33v^5+117v^4+131v^3+69v^2+18v+2,
A4(v)=54v^4+96v^3+75v^2+32v+6.
```

As a sanity check, `D * x5|_{p=1} + 36 v^2 A2 = 0` identically, and the specialized `r2` and `r4` vanish identically as rational functions of `v`. Independently `gcd(A4,A4')=1` and `Res(A4,D)=20736≠0`; neither is needed for the cube curve, but they confirm that a constant root of `A4` would only force `r8=0`, which is already terminal.

### The `p=0` boundary

On `p=0` with `x5≠0` one has `A=x3`. The remaining chart is `x3≠0`. Then `r2=(4/9) x3 (x1-x5^2/3)`, so `x1=x5^2/3`. Independent substitution produces

```text
r4 = -(4/27) x3^2 x5 - (1/243) x5^4,
r6 = -(4/81) x3^3 - (4/243) x3 x5^3,
r8 =  (2/243) x3^2 x5^2 - (4/2187) x5^5
```

before reducing by `r4=0`. The relation `x3^2=-x5^3/36` follows from `r4=0` and `x5≠0` with no division by `x3`. Reducing `r6` and `r8`:

```text
(4/(81*36)) - 4/243 = -11/729,
-(2/(243*36)) - 4/2187 = -1/486,
```

so `nu=-(11/729) x3 x5^3` and `r8=-x5^5/486`. Eliminating `x3,x5` via `x3^{10}=(x3^2)^5=(-x5^3/36)^5` gives a pure constant:

```text
r8^9 / nu^{10} = 36^5 * 729^{10} / 486^9 / 11^{10}.
```

With `36=2^2 3^2`, `729=3^6`, `486=2*3^5` this is exactly `2*3^{25}/11^{10}`. The sign is positive (`(-1)^9` from `r8` against `(-1)^{10}` from `nu^{10}` times `(-1)^5` from `(x3^2)^5`). The right-hand side is a nonzero element of `C`. Thus `r8^9 in C^*`, so `r8` is algebraic over `C`. The constant field of `L` is `C` (Claim 3), hence `r8 in C`, so `r8'=0`, contradicting the terminal row.

No nonconstant algebraic 9th root of a constant exists in a function field over an algebraically closed constant field. The entire `p=0` parity branch is empty for actual trajectories.

---

## Claim 3 — Kummer character, `v in C(x)`, cubes in `K`

**CONFIRMED.**

The reviewed preflight supplies the order-three leaf: `u^3=h in C(x)`, `sigma(u)=zeta u`, `sigma(z)=zeta z`, and `delta=0`, so `z=u y` after depression. Coefficients of `f=sum a_i z^i` then satisfy `sigma(a_i)=zeta^{-i} a_i`, because `a_i u^i` is the Galois-invariant coefficient of `y^i` in `u^9 P(y)`. In particular:

```text
a7=3p  =>  sigma(p)=zeta^{-7} p=zeta^2 p,     character 2,
a5 contains x5  =>  sigma(x5)=zeta^{-5} x5=zeta x5,   character 1,
a3 contains x3  =>  sigma(x3)=zeta^{-3} x3=x3,        character 0.
```

Geometric weights `wt(p)=2`, `wt(x5)=4`, `wt(x3)=6` reduce to these characters modulo `3`. Then `wt(A)=wt(x3-2 p x5)=6` and `wt(p x5)=6`, so `v=A/(p x5)` has character zero and is fixed by `Gal(L/K)`. Hence `v in K=C(x)`.

Character two writes `p=u^2 P` with `P=p/u^2` Galois-invariant, so `P in K`. Then

```text
p^9=(u^2 P)^9=u^{18} P^9=(u^6 P^3)^3=(h^2 P^3)^3
```

is a cube in `K`, not merely in `L`. The identity `p^9 R6(v)=nu` therefore lives in `K`.

The load `nu=r6` is a differential constant of weight `18≡0 mod 3`, hence `nu in C`. Algebraically closed `C` makes every element of `C^*` a cube. Independently, the confirmed DZ20 constant-field fact (re-derived here from `C` being algebraically closed: any element of `L` algebraic over `C` already lies in `C`) says that the constant field of `L` is exactly `C`. Weight-nonzero constants of `L` vanish, which is why the odd tails and `r2,r4` are the only even constraints on this fibre.

Coprimality `gcd(f,g)=1` from the actual Keller Jacobian `D=j/u in L^*` is licensed by the same DZ20 firewall and is not used in the genus-five argument. The contradiction on every parity branch is the terminal row `9 r8'=j/u≠0`, which needs only `j≠0` and `u≠0`.

---

## Claim 4 — removal of cube factors

**CONFIRMED.**

In `K^*`,

```text
R6(v)=-2304 v^6 A2(v)^3 A5(v) / D(v)^4.
```

Each displayed factor other than `A5/D` is a cube, or a cube times `A5/D`:

- `-2304 in C^*` is a cube because `C` is algebraically closed (`-2304=-2^8 3^2` is not a cube in `Q`; the argument never works over `Q`);
- `v^6=(v^2)^3`;
- `A2^3` is a cube;
- `D^4=D*(D)^3`, so `1/D^4=(1/D)*(1/D)^3`.

From Claim 3, `p^9 R6(v)=nu` with both `p^9` and `nu` cubes in `K`, so `R6(v)` is a cube in `K`. Therefore `A5(v)/D(v)` is a cube in `K^*`, and there is a `Y in K` with

```text
Y^3=A5(v)/D(v).                                        (4.1)
```

The leftover function is not itself a cube in `C(v)`. Its divisor on `P^1_v` is

```text
[α1]+⋯+[α5] - [β1] - [β2] - 3[∞],
```

where the `αi` are the roots of `A5` and the `βj` the roots of `D`. Claim 5 shows these seven finite points are distinct and simple. The finite part of the divisor is therefore not divisible by `3` in `Div(P^1)`, so `A5/D` is not a cube in `C(v)^*`. The cyclic extension `C(v)[Y]/(Y^3-A5/D)` has degree exactly three and is geometrically irreducible. It does not split into three copies of `P^1`, and it does not degenerate to a genus-zero or genus-one cover.

Removing `A2^3` is necessary for the displayed equation and harmless for ramification: `v_β(A2^3)=3≡0 mod 3` at any simple zero of `A2`, so those places are unramified either way. Independently `disc(A2)=9-12=-3≠0` and `Res(A2,D)=27`, so the two zeros of `A2` are simple and disjoint from the zeros of `D`. They are not hidden extra branch points.

---

## Claim 5 — squarefreeness, seven finite branch points, unramified infinity, genus five

**CONFIRMED.**

Euclidean algorithm over `Q` gives `gcd(A5,A5')=1` (the last nonzero remainder is a nonzero constant). Thus `A5` is squarefree in `C[v]`; equivalently, `A5` and `A5'` share no root in `C`. No rational root among `{±1,±2,±1/3,±2/3,±1/11,±2/11,±1/33,±2/33}`. Likewise `gcd(D,D')=1`: `D=3v^2-2`, `D'=6v`, and `D mod 6v=-2≠0`. Discriminant of `D` is `24≠0`.

Sylvester resultant, equivalently evaluation at the two roots of `D`:

```text
v^2=2/3  =>  A5(v)=120 v + 100,
prod A5(roots)=100^2-(120)^2*(2/3)=400,
Res(A5,D)=3^5 * 400=97200.
```

Independently `Res(A2,D)=3^2 * A2(√(2/3)) A2(-√(2/3))=27`. Thus `A5` and `D` are coprime, as are `A2` and `D`. Over the algebraically closed constant field one has five simple zeros of `A5` and two simple zeros of `D`, pairwise disjoint: seven distinct finite points.

Kummer ramification of `Y^3=f` in characteristic not `3`: a place of `P^1_v` ramifies with index `3` if and only if `v_p(f)≢0 mod 3`. At each simple zero of `A5` one has `v=1`; at each simple zero of `D` one has `v=-1`. Both are nonzero mod `3`, and each is totally ramified (one point above, index `3`).

At infinity, `deg A5=5` and `deg D=2` with leading-coefficient ratio `33/3=11≠0`. The pole order of `A5/D` is exactly `-3`, with no cancellation. Then `v_∞(f)=-3≡0 mod 3`, so infinity is unramified: three distinct points of the cover lie over `∞`. Locally `v=1/s`, `Y=Z/s` reduces to `Z^3=11(1+O(s))`, étale. The producer’s `infinity_order: -3` and `infinity_branched: false` are therefore exact.

Riemann–Hurwitz for a degree-`3` cover of `P^1`:

```text
2g-2 = 3*(-2) + 7*(3-1) = 8,     g=5.
```

A plane model `Y^3 D(v)=A5(v)` may be singular as a degree-five plane curve (arithmetic genus `6`). That is an embedding artefact. The genus computed by Riemann–Hurwitz is the geometric genus of the function field, i.e. of the unique smooth projective model of `(4.1)`. Locally `Y^3=t` is smooth (`d(Y^3-t)=-dt≠0` at the origin), and the standard compactification of a cyclic cover of `P^1` branched at seven points of index `3` with unramified infinity is already that smooth model. Hidden singularities of a Weierstrass or plane equation do not alter `g=5`.

---

## Claim 6 — no nonconstant map from `P^1_x`, including poles

**CONFIRMED.**

If `v in C(x)` is nonconstant, then `Y in C(x)` by Claim 4, and the pair `(v,Y)` satisfies `(4.1)`. This is a nonconstant rational map from the affine `x`-line to the affine model, equivalently a rational map `P^1_x ⇢ C_5` to the smooth projective model of the function field of `(4.1)`.

A rational map from a smooth curve to a projective variety extends uniquely to a morphism: the valuative criterion of properness (discrete valuation rings of `C(x)` have unique extensions to a regular point of `C_5`). Concretely:

- at a pole of `v` of order `m≥1`, one has `A5/D ∼ 11 v^3`, so `Y ∼ 11^{1/3} v` and the ratio `Y/v` remains finite, landing on one of the three unramified points over `∞_v`;
- at a zero or pole of `Y` lying over a finite branch point, the map lands on the unique ramified point of `C_5` over that value of `v`;
- at a place where `D(v)=0` or `A2(v)=0` or `v=0`, the point of `C_5` is still well-defined on the projective model.

The resulting morphism `φ: P^1_x → C_5` is nonconstant because `v` is nonconstant. Riemann–Hurwitz on `φ` of degree `d≥1` would require

```text
-2 = d * 8 + (nonnegative ramification) ≥ 8,
```

which is impossible. Equivalently, a smooth projective curve of genus `≥2` admits no nonconstant map from `P^1`.

The source is `P^1_x` and not the Kummer curve of `L/K`, because both `v` and `Y` lie in `K=C(x)` (Claims 3–4). If `Y` had lived only in `L`, the source would have been a cyclic triple cover of `P^1_x` of possibly positive genus, and the obstruction would fail. Galois invariance of `v` and the cube calculation in `K` close that hole.

Constant-field extensions do not create a map: base change to an algebraic closure of `C` does nothing, and a finite extension of `C(x)` of genus zero is still `P^1` after compactification, still forbidden as a source of a nonconstant map to genus five.

---

## Claim 7 — constant `v` forces constant `p` and `r8`

**CONFIRMED.**

Now `v=v_0 in C`. The constant value cannot be a forbidden root:

- `v_0=0` is `A=0`, excluded;
- `v_0=∞` is `p x5=0` as elements, excluded;
- `D(v_0)=0` makes `(3.3)` into `36 p^2 v_0^2 A2(v_0)=0`. Here `v_0≠0` because `D(0)=-2≠0`, and `A2(v_0)≠0` because `Res(A2,D)=27`, and `p≠0` on the chart: impossible;
- `A2(v_0)=0` forces `x5=0` from `(3.4)`, excluded;
- `A5(v_0)=0` forces `R6(v_0)=0`, hence `nu=0`, excluded.

Thus `R6(v_0)∈ C^*`, and `p^9=nu/R6(v_0)∈ C^*`. So `p` is a 9th root of a constant. The constant field of `L` is `C`, hence `p∈ C`. Then `r8=p^{10} R8(v_0)` is constant (and finite: `D(v_0)≠0`). If `R8(v_0)=0` one has `r8=0` outright. In all cases `r8'=0`, so `9 r8'=0≠j/u`.

This is the same terminal contradiction as on `x5=0` and on `p=0`. There is no leftover constant-`v` trajectory.

---

## Claim 8 — scope, no promotion

**CONFIRMED.**

The report’s “Not concluded” list, the registration’s scope firewall (“full parity-locus theorem, not a proof that every loaded solution has parity”), the FREEZE `scope` block, the README, and the replay payload `scope` string all stay inside `q=x0=x2=x4=k=0`. None of them asserts emptiness of a non-parity component, Taylor compatibility, generic-fibre emptiness, all `(9,12)`, maximum twelve, a counterexample, or JC2. The loaded fibre `r2=r4=0`, `r6=nu` on the order-three leaf is strictly larger than this odd/even slice. No numbered claim is enlarged.

---

## Attacks that do not land

- **Hidden singularities of the cubic cover.** Locally `Y^3=t` is smooth. Riemann–Hurwitz is computed on the function field, not on a possibly singular plane quintic of arithmetic genus `6`. Geometric genus remains `5`.
- **Reducibility.** `A5/D` is not a cube in `C(v)` because its finite divisor is squarefree of degree `5-2=3` with seven distinct points, not `3`-divisible. The cover is geometrically irreducible of degree `3`.
- **Constant-field extensions.** `C` is algebraically closed, so the constant field of any function field over `C` is `C`; adjoining cube roots of constants does nothing; `p^9 in C^*` forces `p in C`.
- **Missed `D=0` or `A2=0` component.** As elements, both are impossible on the chart (Claim 2). As places, they are accounted for as unramified (`A2`, valuation `3`) or ramified (`D`, valuation `-1`) points of the cover, not as extra coefficient branches.
- **Cancellation at infinity.** Leading ratio `33/3=11≠0`, pole order exactly `-3≡0 mod 3`. No extra ramification and no dropped ramification unit.
- **Promotion from parity to the loaded fibre.** Absent from every charged artifact (Claim 8).
- **`Y` only in `L`.** Closed by the cube calculation in `K` (Claims 3–4); this is the hole that would have replaced `P^1_x` by a positive-genus source.
- **`A4=0`.** Forces `r8=0` after `v` is constant, which is already terminal; `A4` is squarefree and coprime to `D`, unused in the genus ledger.

---

## Non-blocking remarks

- The replay is a correct regression of the generic-chart identities, the gcd/resultant/genus ledger, and the `p=0` tail strings. Absence of a Galois-invariance or no-map check in-replay is not a mathematical gap: those steps are field-theoretic and were re-derived independently.
- `k=0` is not needed for evenness of `g` (`F_6` is even whenever `f` is odd). It is the `k=0` fibre being probed, as written.
- Geometric weights `wt(x5)=4`, `wt(x3)=6` in the producer’s character sentence are the correct lifts of characters `1` and `0` modulo `3`. The invariance of `v` uses only the characters.
- `-2304` is a cube in `C^*` and not in `Q^*`. The argument is over algebraically closed constants, as registered.
- The fibre compiler has no completed different-model review. Tails used as evidence were rebuilt from the reviewed `F_12` binomial and `f(z(w))=w^9`. A post-hoc comparison with the pinned parent compiler matches coefficient-for-coefficient and is not evidence.
- Coprimality `gcd(f,g)=1` is a true actual-Keller fact and is unused here. The present contradiction never enters the spectral Wronskian.

---

## What this does not license

This review does not license: parity exhaustion of `nu≠0`; emptiness of a non-parity component; any generic loaded component; Taylor-boundary reconstruction; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

---

**Verdict.** `CONFIRMED`

Smallest failing identity: none.
Smallest missing hypothesis: none that breaks a numbered claim.
