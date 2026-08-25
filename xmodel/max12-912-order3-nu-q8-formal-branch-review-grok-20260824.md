# Hostile different-model review — genuine `Q8` non-parity formal branch

| Field | Value |
|---|---|
| Claim under review | Frozen producer: at every loaded root of the corrected residual `Q8`, the seven-row constant-invariant fibre `k=mu=0`, `nu!=0`, `r1=r2=r3=r4=r5=r7=0`, `r6=nu` has the parity fixed curve and a second reduced smooth non-parity formal curve branch with distinct tangents. Chart is the genuine numerator `1+3v`. No `Q12` descendant is consumed. Formal coefficient-fibre geometry only |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: characteristic not `2` or `3` is the ambient involution / Faber inverse-root setting; the order-three fibre compiler has no completed different-model review and is consumed only as the engine producing the eight tails; the `Q8` erratum is not yet different-model reviewed, but identity `(2.2)` is re-derived here by Gaussian elimination over `Q`) |
| Evidence tier | independent involution typing of all eight pinned Faber tails; Gaussian elimination over `Q` of the `4 x 4` at twenty-four chart samples (not the producer `4!` Leibniz expansion); explicit `3 x 3` formula for every minor of both blocks, then Euclidean gcd against `Q8` after reducing numerators and denominators; dual quotient-rule computation of `num(R6')`; source-level exclusion of every `Q12` descendant pin and of the constant `1/3` substitution; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | corrected `Q8` erratum; reviewed parity genus-five pair; pinned coefficient compiler. Quarantined `Q12` branch and its refutation used only as negative controls |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | `2026-08-24T21:28:56Z` – `2026-08-24T21:36:00Z` |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, corrected `Q8` erratum, original coefficient compiler, reviewed parity-genus-five pair, and the quarantined `Q12` branch plus its refutation reread in full before any verdict:

- `xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md`
- `cases/max12_912_order3_nu_q8_formal_branch_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-912-order3-nu-parity-normal-q8-erratum-20260824.md` and `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/`
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (pinned parent compiler; no completed fibre review exists in-tree)
- `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` and `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md`
- `cases/max12_912_order3_nu_parity_genus5_20260824/replay.py` (pinned by SHA-256)
- `xmodel/max12-912-order3-nu-q12-formal-branch-20260824.md` and `cases/max12_912_order3_nu_q12_formal_branch_20260824/` (negative control only)
- `xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md` (refutation; negative control only)

No producer, case, canonical, coordination, prompt, log, run, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Accept `EVERY LOADED Q8 PARITY CONTACT OF THE GENUINE SEVEN-ROW COEFFICIENT FIBRE LIES ON A SECOND SMOOTH NON-PARITY FORMAL COMPONENT` at the stated scopes.**

- All eight reconstructed tails match the pinned supports and SHA-256 digests. Each monomial of `r_ell` has involution character `(-1)^ell`. The imposed fibre is the seven-row scheme `(1.1)`; the eighth tail `r8` is reconstructed and typed, then left unimposed.
- The chart is the reviewed genus-five substitution with polynomial numerator `1+3v`, not the quarantined constant `1/3`. On that chart `r2=r4=0` identically and `r6=p^9 R6(v)` recovers the reviewed formula. The frozen replay pins the `Q8` erratum, the genus-five replay, and the compiler; it does not pin or import any `Q12` descendant.
- At every algebraic root of `Q8` both displayed rank-three minors are units in the local ring of the chart (numerators and denominators coprime to `Q8`). Independently, every `3 x 3` minor of `J_N` and every `3 x 3` minor of `J_I` is a unit there, so rank `J_N=3` and rank `J_I=3` are not an artifact of one lucky minor. The seven-row Jacobian is block diagonal at parity, hence has rank six, and the Zariski tangent space has dimension two.
- `gcd(Q8,Q8')=1` and `gcd(Q8,num(R6'))=1`. Loaded algebraic points exist because `Q8` is coprime to `v`, `A2`, `D`, and `A5`, so `p^9 R6(v)=nu` has solutions in `C^*`.
- The two unit minors eliminate `a2,a4,a6` and `x1,x3,x5`, retaining an invariant coordinate `s` (étale-equivalent to `p` or to `v`) and an anti-invariant coordinate `t=a0`. Uniqueness of the formal implicit-function theorem plus the involution force the remaining odd equation into the form `t Phi(s,t^2)=0`. The Schur complement of the normal minor identifies `Phi(s,0)=unit*det(J_N)`. Squarefreeness of `Q8` together with the unit prefactors of `(2.2)` and the étaleness of `v` against `p` give `dPhi/ds(0,0)≠0`, so `Phi=0` solves as `s=psi(t^2)`.
- The completed local fibre is two reduced smooth formal curve branches with distinct tangents: parity `t=0`, and non-parity `Phi(s,t^2)=0`.

**Do not promote this to:** an algebraic or rational Keller trajectory; pullback of `r8` or `9 r8'=j/u`; Kummer descent; Taylor, simplicity, or coprimality reconstruction; analysis of components disjoint from parity; all `(9,12)`; maximum twelve; a counterexample; or JC2.

**Smallest valid successor.** Normalize the new formal component and pull back `r8`. Do not open a generic coefficient rectangle or AWS. Do not treat the second branch as a trajectory.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, produces an algebraic or rational trajectory, imposes the terminal row, empties a component disjoint from parity, or closes maximum twelve. Producer replay output was not used as evidence of the minors, the gcds, or the determinant identity. The involution restrictions, the `4 x 4` and `3 x 4` Jacobians, both `x1` substitutions, the two determinant identities, every `3 x 3` minor, and the gcd ledgers were re-derived over `Q`. The reviewed genus-five theorem is consumed only for the chart `p*x5*A!=0`, the reversible solves of that theorem, the identity `r6=p^9 R6(v)`, and the element-versus-place exclusions of `v`, `A2`, and `D`. The `Q8` erratum is consumed only as the frozen residual polynomial and the first-order identity `(2.2)`, both of which are reconfirmed here. The fibre compiler is not a reviewed theorem. The quarantined `Q12` checkpoint, its formal-branch descendant, and the constant-`1/3` substitution are negative controls only. The already-excluded parity *trajectory* is not treated as an actual base solution: the linearization and the formal implicit-function theorem are of the coefficient scheme.

---

## Scope (not enlarged)

Formal seven-row high-coefficient fibre geometry at loaded `Q8` contacts of the genuine parity chart. Terminal `r8`, rational or differential descent, Taylor/coprimality, components disjoint from parity, all `(9,12)`, maximum twelve, a counterexample, and JC2 remain out of scope. The present confirmation stays inside that scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | All eight source tails match the pinned supports and digests; `r_ell` has character `(-1)^ell`; the imposed fibre is the seven-row scheme `(1.1)` and does not include `r8` | **CONFIRMED** | a digest or support mismatch; a monomial of the wrong character; `r8` appearing in the seven-row Jacobian; a hidden eighth equation in a charged artifact |
| 2 | The chart uses the polynomial numerator `1+3v`; `r2=r4=0` on that chart; no `Q12` descendant is imported or used as a theorem | **CONFIRMED** | a `Rat.constant(1/3)` substitution; `r2` or `r4` nonzero after the displayed `x1`; a SHA-256 pin of the quarantined `Q12` report, replay, or formal-branch case |
| 3 | At every algebraic `Q8` root, `det d(r3,r5,r7)/d(a2,a4,a6)` and `det d(r2,r4,r6)/d(x1,x3,x5)` are units; all localization factors of `(2.2)` needed to call them units are coprime to `Q8` | **CONFIRMED** | that specific normal or invariant minor sharing a root with `Q8` in numerator or denominator; a pole of a chart factor `v`, `A2`, or `D` at a `Q8` root; rank `J_N<3` or rank `J_I<3` at some algebraic root |
| 4 | `gcd(Q8,Q8')=gcd(Q8,num(R6'))=1`; loaded algebraic points exist over every `Q8` root | **CONFIRMED** | a multiple root of `Q8`; a common root of `Q8` and `A5` (or `v`, `A2`, `D`) emptying `R6`; a character obstruction to `p^9=nu/R6(v)` in `C` |
| 5 | The two unit minors remove `a2,a4,a6` and `x1,x3,x5`; the remaining odd equation is equivariantly `t Phi(s,t^2)=0` with `s` invariant and `t` anti-invariant | **CONFIRMED** | a non-unit minor blocking that elimination; a residual even equation; an odd remainder that is not odd in `t` in characteristic not `2` |
| 6 | On `t=0`, the Schur complement of the normal minor is `Phi(s,0)=unit*det(J_N)` | **CONFIRMED** | the remaining linearized odd condition not equal to `det(J_N)/det(D)`; `det(D)` vanishing at a `Q8` root (already excluded by Claim 3) |
| 7 | The loaded equation makes `p` a formal function of `v`; squarefreeness of `Q8` with the unit prefactors of `(2.2)`, and étaleness of `v` against `p`, imply `dPhi/ds(0,0)≠0` | **CONFIRMED** | `R6(v0)=0`; a multiple factor of `Q8` in `(2.2)`; the loaded curve ramified over `p` at a `Q8` root (`R6'=0` and the invariant minor both failing) |
| 8 | The local fibre is two reduced smooth formal curve branches with distinct tangents; the scope is seven-row coefficient geometry, not a Keller trajectory | **CONFIRMED** | `Phi` a square in `k[[s,t]]`; coincident tangents; a hidden `r8`, Taylor, all-`(9,12)`, maximum-twelve, counterexample, or JC2 promotion in a charged artifact |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md` | `37ce842eece0e79f0768bdfd492be70905bb83ba62af93965b4c4a2a3d6f03a3` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `dc4793a1499ab44d8f6d43573857416f2f2023b14acf13458c7ad8cd96d02872` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `7da9534f69022d31027cdd2cbe51f49bd2b54457bf8e41696201644aa138fa73` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `a55cfc7fe46f43287f34750b287a6dfb66f9454b8eb77b02f41e681e00b32210` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `a637c70707920ac4b7b1481b7b15c2a3503e11bad0f848c113be32a8c02b38d8` | `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `d4b54c5a3e93ee9cc696017b9e87b6e0deb7b29253239e1df5f1e87fac063a31` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `0047d3482a26a10daacb032aa08e6da888552274c09f1d85083cdf5ae40d9ebb` | prompt only |

Pinned and named dependencies recomputed, not used as mathematical evidence beyond the licensed inputs named above:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-912-order3-nu-parity-normal-q8-erratum-20260824.md` | `7f1ed3c7874c743b35ba4f519acdc2555f65c93c467ccb2e894d8d0b7ade1cc2` |
| `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.py` | `51168609a477905b25cb551ddd40931d1a6d752d7a1569bdc1b9a394cf8dcd23` |
| `cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.json` | `5d2e160a0cd92e70f4a45220e19f8e4102125b3895ee990d44082fdbfda50732` |
| `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` | `f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d` |
| `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md` | `903a973ac4975dfdeea77d143ebaa33cdc504d0f75d31dfe5327dad2d9be8528` |
| `cases/max12_912_order3_nu_parity_genus5_20260824/replay.py` | `c965bb660cf2f0f55c7ebbed3126b22bfb5d67e178565426aa94ce56f6ce1d9a` |
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` |

Negative-control hashes (quarantined; not consumed):

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md` | `9616396705d071efac3cf52332c5007a4a045989940bcc8743a545e87f763a1c` |
| `xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md` | `fc0b0216784bdcec8f9b0955c5a6c71d57870ae2265ed927f306d19d31a79c30` |
| `xmodel/max12-912-order3-nu-q12-formal-branch-20260824.md` | `fd4db3e2125a11c05dac3c9613b8f4305942150d0e92a3200259e595c2afce62` |
| `cases/max12_912_order3_nu_q12_formal_branch_20260824/MANIFEST.sha256` | `3ced488452275f29a4645efb098c87a987e54eb3df85b9f5646da8da8bdbe099` |
| `cases/max12_912_order3_nu_q12_formal_branch_20260824/FREEZE.txt` | `aa17408d0f860158fdd55577315299f9d9298599f8c7d37c72cb306fbb29b83c` |

The four SHA-256 pins inside `replay.py` match the genus-five replay, fibre-compiler, `Q8` erratum replay, and `Q8` erratum report hashes above. `shasum -a 256 -c cases/max12_912_order3_nu_q8_formal_branch_20260824/MANIFEST.sha256` exits `0`. `python3 cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.py | diff -u cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.json -` exits `0`. The replay reconstructs the eight tails, uses `Rat((1,3))` for `1+3v`, recomputes `(2.2)`, and gcd-certifies the two named minors. It does not construct `Phi` and does not run the implicit-function theorem. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present. The replay source contains no `Q12` polynomial, no `Rat.constant(Fraction(1,3))`, and no path pin of a quarantined `Q12` artifact.

---

## Claim 1 — eight source tails; seven imposed rows

**CONFIRMED.**

Work in characteristic not `2` or `3`. The involution `f(z) |-> -f(-z)` acts on coefficients by `a_i |-> (-1)^{i+1} a_i`. Even coefficients are anti-invariant, so the fixed locus in the depressed degree-nine chart is `a0=a2=a4=a6=0`. Approximate-cubic coordinates with `q=0` give the same locus, and `d(a0,a2,a4,a6)/d(x0,x2,x4,q)` at parity is triangular of determinant `3≠0`. Rank-drop loci in `a`-coordinates and in `(x,q)` coincide.

Independent reconstruction of the pinned compiler produces eight tails with supports

```text
r1:25, r2:36, r3:42, r4:55, r5:63, r6:84, r7:94, r8:121
```

and the eight SHA-256 digests displayed in `replay.json`. Every monomial of `r_ell` has odd total degree in `(a0,a2,a4,a6)` exactly when `ell` is odd. Direct restriction to parity gives `r1=r3=r5=r7=0` as elements of `Q[p,x1,x3,x5]`, and the first normal derivatives of the even tails vanish on the locus.

The fibre equations in `(1.1)` are the seven rows `r1=r2=r3=r4=r5=r7=0`, `r6=nu`. The Jacobian used below is of those seven rows in the eight coefficients `(a0,a2,a4,a6,p,x1,x3,x5)`. The tail `r8` is reconstructed and character-checked, then excluded from the Jacobian. No charged artifact imposes `r8=0` or `9 r8'=j/u`.

The fibre is already `k=mu=0`. Odd `k`-derivatives vanish on parity, so `k` is not a fifth normal coordinate inside this slice. Non-blocking: the replay does not include a `k`-column, and none is needed.

---

## Claim 2 — corrected `1+3v` chart; no `Q12` descendant

**CONFIRMED.**

On `p*x5*A≠0` the reviewed genus-five chart is

```text
v=A/(p x5),
x3=p x5 (v+2),
x1=x5 p^2 (v+1)+x5^2 (1+3v)/(9v),
x5=-36 p^2 v^2 (3v^2+3v+1)/(3v^2-2).
```

The producer replay implements `genus.Rat((Fraction(1), Fraction(3)))`, the polynomial `1+3v`. It does not implement `genus.Rat.constant(Fraction(1,3))`. These agree only at the point `v=-2/9`, which is not an identity.

Independent evaluation at twenty-four rational `v` with `p=1` and by exact rational-function arithmetic gives `r2=r4=0` on the polynomial-numerator chart and recovers

```text
r6=-2304 p^9 v^6 (3v^2+3v+1)^3 A5(v)/(3v^2-2)^4.
```

On the constant-`1/3` slice, `r2` and `r4` are nonzero at all twenty-four samples, and Gaussian elimination recovers the quarantined `Q12` determinant identity. That slice is the negative control. It is not an input.

The frozen replay pins the `Q8` erratum report/replay, the genus-five replay, and the compiler. It does not pin the quarantined `Q12` report, the `Q12` checkpoint replay, or the `Q12` formal-branch case. Payload field `quarantined_q12_branch_consumed` is `false`, matching the source.

The `Q12` formal-branch package is the same IFT template on the wrong chart, with a SHA-256 pin of the refuted checkpoint. That is why it is quarantined. Parallelism of the template is not consumption of a `Q12` theorem.

---

## Claim 3 — both rank-three minors; localization factors

**CONFIRMED.**

At parity the seven-row Jacobian is block diagonal:

```text
J_N = d(r1,r3,r5,r7)/d(a0,a2,a4,a6)     (4 x 4),
J_I = d(r2,r4,r6)/d(p,x1,x3,x5)         (3 x 4).
```

Cross blocks vanish: odd tails are identically zero on the even locus, and even tails are invariant. Independently, every even-column derivative of every odd parity tail is the zero polynomial, and every normal derivative of every even tail vanishes on parity. The row `r8` is not in `J_I`.

Gaussian elimination over `Q` of `J_N` at twenty-four rational chart points with `p=1`, on the genuine `1+3v` substitutions, recovers the erratum identity

```text
det(J_N)=p^{20}*226492416*v^{16}*(3v^2+3v+1)^8*Q8(v)
         /(3v^2-2)^{10},

226492416=2^{23}*3^3,

Q8(v)=-999 v^8-1539 v^7+1782 v^6+6498 v^5
      +7320 v^4+4428 v^3+1548 v^2+296 v+24.
```

The scalar, exponents, denominator, and octic match `(2.2)`. At the numerical control `p=v=1` one has `x5=-252`, `x3=-756`, `x1=27720`, and `det(J_N)=25275425185572323328`. Weighted homogeneity of weights `wt(r1,r3,r5,r7)=(13,15,17,19)` and `wt(a0,a2,a4,a6)=(9,7,5,3)` accounts for the factor `p^{20}` after evaluating at `p=1`. On the constant-`1/3` slice the same Gaussian path recovers the quarantined `Q12` identity and not `(2.2)`.

`Q8` has no rational root (complete rational-root scan against `±` factors of `24` over factors of `999`). Vanishing of `det(J_N)` on the retained chart is therefore an algebraic condition. Euclidean gcds give

```text
gcd(Q8, v)=gcd(Q8, 3v^2+3v+1)=gcd(Q8, 3v^2-2)=1.
```

The prefactors `p`, `226492416`, `v^{16}`, `A2^8`, and `D^{10}` of `(2.2)` are units at every `Q8` root of the generic chart. Thus `det(J_N)=0` there, so rank `J_N ≤ 3`.

The named normal minor is rows `r3,r5,r7` against columns `a2,a4,a6`. The named invariant minor is rows `r2,r4,r6` against columns `x1,x3,x5`. Both are evaluated as rational functions of `v` by the explicit `3 x 3` expansion (not a permutation loop), then reduced by `gcd(numerator, denominator)`. Independently of reduction:

```text
gcd(num(normal minor), Q8)=gcd(den(normal minor), Q8)=1,
gcd(num(invariant minor), Q8)=gcd(den(invariant minor), Q8)=1.
```

Reduced degrees are `36/18` for the normal minor and `29/14` for the invariant minor. Hidden chart denominators therefore do not introduce a `Q8` pole. At `p≠0` the weights restore unit powers of `p` (`p^{18}` for the normal `3 x 3`, `p^{15}` for the invariant `3 x 3`).

Stronger independent control, not required by the producer: all sixteen `3 x 3` minors of `J_N` are units at every `Q8` root, and all four `3 x 3` minors of `J_I` are units there. Rank is exactly three in each block at every algebraic `Q8` point of the chart. The displayed coordinate choice is not a minor that vanishes at some roots.

Localization factors needed to call the minors units at a loaded `Q8` point:

```text
p ≠ 0,           from p^9 R6(v)=nu with R6(v)≠0,
v ≠ 0,           Q8(0)=24,
A2(v) ≠ 0,       gcd(Q8,A2)=1,
D(v) ≠ 0,        gcd(Q8,D)=1,
A5(v) ≠ 0,       gcd(Q8,A5)=1  (also the load),
226492416 ≠ 0,   characteristic not 2 or 3,
both named 3 x 3 numerators and denominators.
```

All hold. The full Jacobian therefore has rank six, the parity fixed fibre is a smooth curve, and the full tangent space has dimension two.

---

## Claim 4 — squarefreeness, `R6'`, loaded points

**CONFIRMED.**

Independent monic Euclidean algorithm over `Q`:

```text
gcd(Q8, Q8')=1,     Q8(0)=24 ≠ 0,
gcd(Q8, A2)=1,      gcd(Q8, D)=1,      gcd(Q8, A5)=1,
gcd(Q8, Q12)=1.
```

`Q8` is squarefree of degree `8` and coprime to every chart factor of `(2.2)` and to the quarantined dodecic. No rational root.

Write `R6(v)=-2304 v^6 A2^3 A5 / D^4`, already reconfirmed as an identity of rational functions on the genuine chart. The numerator of `dR6/dv`, after removing the invertible factor `D^3` and the irrelevant scalar, is `N' D - 4 N D'` with `N=v^6 A2^3 A5`. Independently, the unreduced quotient-rule numerator `N' D^4 - N (D^4)'` equals that polynomial times `D^3`. Both have gcd `1` against `Q8`. Thus

```text
gcd(Q8, num(R6'))=1.
```

Because `gcd(Q8, v A2 D A5)=1`, a root `v0` of `Q8` in `C` has `R6(v0)∈ C^*`. For any `nu∈ C^*` the equation `p^9=nu/R6(v0)` has solutions in `C`. These are algebraic points of the coefficient scheme, not actual Keller trajectories: the genus-five theorem already emptied every actual trajectory on the whole parity locus, including `Q8=0`. The producer does not treat them as actual base solutions.

Kummer typing is vacuous for these constant points. Ninth roots of nonzero constants exist over the algebraic closure of the constant field. No obstruction.

---

## Claim 5 — equivariant elimination; residual odd equation

**CONFIRMED.**

The named unit minors license a simultaneous formal implicit-function theorem in characteristic zero:

- solve `a2,a4,a6` from `r3,r5,r7` as odd functions of `(a0,p)`;
- solve `x1,x3,x5` from `r2,r4,r6` as even functions of `(a0,p)`.

Uniqueness plus equivariance of the involution `n |-> -n`, `b |-> b` force those solutions to have the stated parities. Remaining coordinates may be taken as `t=a0` (anti-invariant) and an invariant `s` étale-equivalent to `p`. (Claim 7 identifies `s` with `v` up to a unit.) No residual even equation remains: all three even rows were used.

The remaining odd equation `F(s,t)` satisfies `F(s,-t)=-F(s,t)` in `k[[s,t]]` with `char k ≠ 2`. Writing `F=sum a_{ij} s^i t^j`, oddness kills even `j`, so

```text
F(s,t)=t Phi(s, t^2)
```

as formal series. This is the representation of an odd series, not an extra existence theorem. The implicit-function uniqueness is used only to guarantee that the remainder, after substituting the unique equivariant solutions, is odd in `t`.

The coordinate choice is proved, not assumed: both named minors are units at every algebraic `Q8` root (Claim 3), and every other `3 x 3` of either block is a unit there as well. One could retain any leftover invariant column of `J_I` and any leftover anti-invariant column of `J_N`. The producer’s choice `(s,t) ~ (p, a0)` is one such pair.

---

## Claim 6 — Schur complement `Phi(s,0)=unit*det(J_N)`

**CONFIRMED.**

Partition `J_N` at the remaining odd row `r1` and remaining odd column `a0`, with `D` the named `3 x 3` on rows `r3,r5,r7` and columns `a2,a4,a6`. On `t=0` the remaining linearized odd condition is the Schur complement `det(J_N)/det(D)`. The series `Phi(s,0)` is exactly that coefficient of `t` in `F(s,t)`. Claim 3 makes `det(D)` a unit at every loaded `Q8` point, so

```text
Phi(s,0)=unit(s)*det(J_N)(s)
```

in the local ring of the fixed curve. No extra localization is required.

---

## Claim 7 — `p` as a function of `v`; `dPhi/ds ≠ 0`

**CONFIRMED.**

On the reversible chart the load is `p^9 R6(v)=nu`. At a root `v0` of `Q8` one has `R6(v0)≠0` (Claim 4), so `p=(nu/R6(v))^{1/9}` is a formal unit in `C[[v-v0]]` after choosing a ninth root. That is the producer’s sentence that the loaded equation solves `p` as a formal function of `v`. Its `p`-derivative `9 p^8 R6` is a unit at the point.

The remaining invariant coordinate after Claim 5 is `p`. The unit minor `d(r2,r4,r6)/d(x1,x3,x5)` says that, at fixed `p`, there is a unique `(x1,x3,x5)` solving the even equations, hence a unique `v` (the chart `v |-> (x1,x3,x5)` at fixed `p` is an immersion on `p*x5*A≠0` with `D≠0`). The loaded curve is therefore a graph `v=v(p)` in `C[[p-p0]]`. Equivalently `gcd(Q8,num(R6'))=1`, independently certified, makes `dv/dp` a unit. Thus `p` and `v` are étale coordinates on the fixed curve, and either may be used as `s`.

Along that curve

```text
det(J_N)=p^{20}*226492416*v^{16}*A2^8*Q8(v)/D^{10}.
```

Every prefactor is a unit at the point (Claim 3). Squarefreeness of `Q8` makes the zero of `det(J_N)` simple in `v`. Transporting by the étale change `v=v(p)` keeps it simple in `p`. Combined with Claim 6,

```text
dPhi/ds(0,0)=unit*d(det(J_N))/ds(0,0) ≠ 0.
```

The `t=0` restriction already vanishes, so the displayed derivative is the only remaining obstruction to the second implicit-function step. That obstruction is absent.

Non-blocking compression in §3: the sentence “`Q8` is squarefree with all factors in `(2.2)` units, hence `dPhi/ds≠0`” does not re-cite the `R6'` line of `(2.4)`. The missing citation is not a missing hypothesis. The unit invariant minor already forces the graph `v=v(p)`, and `(2.4)` independently records `gcd(Q8,num(R6'))=1`. Either certificate licenses the coordinate change. The `Q12` ancestor called `R6'` redundant given the minor; on the genuine chart both hold, and the minor is the structural reason `s` is a regular parameter.

---

## Claim 8 — reducedness, smoothness, distinct tangents, scope

**CONFIRMED.**

The second implicit-function theorem applies to `Phi(s,u)=0` at `(0,0)` with `u=t^2` and `dPhi/ds(0,0)≠0`, producing a unique series `s=psi(u)=psi(t^2)`. Weierstrass preparation in `k[[s,t]]` writes

```text
t Phi(s,t^2)=t*(s-psi(t^2))*unit(s,t).
```

The unit is a unit, so the zero set is exactly the two branches

```text
parity:      t=0,
non-parity:  s=psi(t^2).
```

Neither factor is a square. Each is a graph, hence formally smooth. Tangents at the origin: the first is the `s`-axis `(ds,0)`; the second is parametrized by `t |-> (psi(t^2), t)` with derivative `(0,1)`, the `t`-axis. Distinct.

The cubic jet of `Phi` is not required. Simple motion of the normal eigenvalue along the fixed curve is the whole local calculation.

Scope is observed in the report, registration, README, FREEZE block, and replay payload: seven-row coefficient-fibre geometry; not an algebraic or rational Keller trajectory; no terminal `r8`; no Taylor, simplicity, or coprimality; no disjoint-component analysis; no all-`(9,12)`, maximum-twelve, counterexample, or JC2 conclusion. The genus-five emptiness of actual parity trajectories is not misused as a base solution.

---

## Attacks that do not land

- **Hidden denominators.** Both named minors, after reduction, have denominators coprime to `Q8`. Chart factors `v`, `A2`, `D` are coprime to `Q8`. Evaluating at `p=1` and restoring `p`-weights is legitimate because `p≠0` at loaded points.
- **Confusion of the seven-row fibre with `r8`.** The eighth tail is reconstructed and typed, then excluded from the Jacobian and from `(1.1)`. No charged artifact imposes it.
- **Unproved equivariant coordinate choice.** The named minors are units at every algebraic `Q8` root; so is every other `3 x 3` of either block. Remaining coordinates `(p,a0)` exist. The involution plus uniqueness give `t Phi(s,t^2)` in characteristic not `2`.
- **A minor that vanishes at some algebraic `Q8` root.** Independent gcd of every `3 x 3` of `J_N` and of `J_I` against `Q8` is `1` in both numerator and denominator.
- **Implicit carryover from the refuted `Q12` package.** The replay pins the `Q8` erratum, the genus-five replay, and the compiler. It does not pin a `Q12` path, does not substitute `1/3`, and does not assert the `Q12` determinant identity. The IFT template is standard mathematics recomputed on the genuine residual; it is not a `Q12` theorem.
- **Passing replay as the proof.** The replay is internally consistent regression of the computational hypotheses. The IFT, Schur complement, and branch geometry were re-derived from those hypotheses, not read off `replay.json`.

---

## Non-blocking remarks

- The `Q8` erratum is not yet different-model reviewed. Identity `(2.2)` is independently Gaussian-confirmed here at twenty-four samples and matches the reviewer identity `(R.1)` of the `Q12` refutation. That is enough to use the octic as a residual, not enough to treat the erratum text as a reviewed theorem beyond `(2.2)` and the gcd ledger reconfirmed above.
- The fibre compiler has no completed different-model review. Odd-tail derivatives used here are those of the pinned Faber engine, as in the genus-five and `Q12`-refutation reviews.
- Characteristic not `2` or `3` is the ambient involution / Faber inverse-root setting.
- The extra gcd `gcd(Q8,num(R6'))=1` is a genuine control that `v` is étale against `p`. It is implied by the unit invariant minor plus chart reversibility, and it is independently true.
- All sixteen normal `3 x 3` minors being units is stronger than the producer states. It is recorded as independent evidence, not as a frozen extra theorem.

---

## What this does not license

This review does not license: an algebraic or rational Keller trajectory through a `Q8` contact; pullback of `r8` or of `9 r8'=j/u`; Kummer descent; Taylor, simplicity, or coprimality reconstruction; emptiness or existence of components disjoint from parity; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2. It also does not license transferring any conclusion of the quarantined `Q12` formal-branch package.

---

**Verdict.** `CONFIRMED`

Smallest failing identity or hypothesis: none.
