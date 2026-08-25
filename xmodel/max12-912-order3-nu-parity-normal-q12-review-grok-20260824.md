# Hostile different-model review — maximum-12 parity-normal `Q12` checkpoint

| Field | Value |
|---|---|
| Claim under review | Frozen producer: on the reviewed `nu!=0`, `k=mu=0` generic parity chart, the four anti-invariant rows have invertible `4 x 4` normal Jacobian away from a squarefree residual `Q12(v)=0`. Displayed identity `(3.1)` after the genus-five substitutions for `x3,x1,x5`. First-order only: no trapping at `Q12`, no non-parity exclusion, no maximum-twelve theorem |
| Overall verdict | **REFUTED** |
| Smallest failing identity | `(3.1)` on the substitutions displayed in §3. With `p=1`, `v=1` on the genuine `r2=r4=0` chart one has `det(J_N)=25275425185572323328`, while the right-hand side of `(3.1)` equals `169664962152837939200/243` |
| Smallest missing hypothesis | none; the identity is false rather than incomplete. The replay implements a different `x1` from the one written in the report, and that other slice is not the loaded fibre |
| Evidence tier | independent involution typing of all eight rows from the pinned Faber tails; Gaussian elimination over `Q` of the `4 x 4` (not the producer `4!` Leibniz expansion); 24 exact chart samples distinguishing the displayed `x1` from the replay `x1`; exact `Q(v)` reconstruction of `det(J_N)` on the genuine `r2=r4=0` chart; Euclidean gcd ledger for both `Q12` and the true residual octic; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | none named by the launch prompt |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | `2026-08-24T20:55:07Z` – `2026-08-24T21:12:00Z` |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, pinned compiler, reviewed parity theorem/review, and the named Faber input reread in full before any verdict:

- `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md`
- `cases/max12_912_order3_nu_parity_normal_q12_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` and `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md`
- `cases/max12_912_order3_nu_parity_genus5_20260824/replay.py` (pinned by SHA-256)
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (pinned parent compiler; no completed fibre review exists in-tree)
- `xmodel/max12-partial-y-shared-faber-probe-20260824.md` and `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` (named Faber input of the compiler; consumed only as the engine producing the eight tails)

No producer, case, canonical, ladder, coordination, prompt, log, run, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Do not accept `GENERIC NORMAL RANK IS FOUR; Q12 IS THE RETAINED RANK BOUNDARY`.**

The involution, the `4 x 4` as the complete first-order normal block, and the displayed reversible substitutions for `x3,x1,x5` survive. The exact identity `(3.1)` does not. The report writes the reviewed genus-five `x1`, then claims that substituting those formulae into `(2.1)` produces `Q12`. The frozen replay substitutes a different rational function of `v` for `x1`, on which `r2` and `r4` do not vanish. Identity `(3.1)` is true on that off-fibre slice and false on the loaded chart the report names.

On the genuine `r2=r4=0` chart the independent reconstruction is

```text
det(J_N) = p^20 * 226492416 * v^16 * (3v^2+3v+1)^8 * Q8(v)
           / (3v^2-2)^10,                                 (R.1)

226492416 = 2^23 * 3^3,

Q8(v) = -999*v^8 - 1539*v^7 + 1782*v^6 + 6498*v^5
        + 7320*v^4 + 4428*v^3 + 1548*v^2 + 296*v + 24.   (R.2)
```

`Q8` is squarefree and coprime to `v`, `3v^2+3v+1`, `3v^2-2`, `A5`, and the producer’s `Q12`. Consequently:

- at a root of `Q12` with chart denominators nonzero, `J_N` is invertible;
- at a root of `Q8` with chart denominators nonzero, `J_N` drops rank, and `p^9 R6(v)=nu` still supplies loaded algebraic points.

The residual first-order rank boundary on the retained chart is `Q8=0`, not `Q12=0`. `(R.1)` is a reviewer identity used to exhibit the failure; it is not a frozen replacement theorem.

**Do not promote this to:** invertibility away from `Q12`; trapping at `Q8` or at `Q12`; emptiness of a non-parity component; all `(9,12)`; maximum twelve; a counterexample; or JC2.

**Smallest valid successor.** Recompute the normal determinant on the displayed genus-five `x1` (the polynomial `1+3v`, not the constant `1/3`), freeze the octic residual, and only then ask the first-order invertibility statement away from that residual. Do not open a generic coefficient rectangle or AWS.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, traps a formal arc in parity, empties a non-parity component, or closes maximum twelve. Producer replay output was not used as evidence of `(3.1)`. The involution restrictions, the `4 x 4` Jacobian, both `x1` substitutions, the two determinant identities, and the gcd ledgers were re-derived over `Q`. The reviewed genus-five theorem is consumed only for the chart `p*x5*A!=0`, the reversible solves `(3.2)`–`(3.4)` of that theorem, the identity `r6=p^9 R6(v)`, and the element-versus-place exclusions of `v`, `A2`, and `D`. The fibre compiler is not a reviewed theorem; tails used as a computational engine are those of the pinned Faber construction. The already-excluded parity *trajectory* is not treated as an actual base solution: the linearization is of the coefficient scheme.

---

## Scope (not enlarged)

Exact first-order normal rank of the loaded coefficient fibre along the parity fixed locus, on the reviewed generic chart. Formal-arc trapping, neighborhood emptiness, exclusion of a disjoint non-parity component, all `(9,12)`, maximum twelve, a counterexample, and JC2 remain out of scope. The present refutation stays inside that scope: it is the displayed determinant identity and the named residual that fail.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The involution `f(z) |-> -f(-z)` fixes `a0=a2=a4=a6=0`. With `k=0`, odd rows `r1,r3,r5,r7` are anti-invariant and vanish on the fixed locus; even rows `r2,r4,r6,r8` are invariant | **CONFIRMED** | a nonvanishing odd tail on parity; an even tail with a nonzero normal derivative there; a fifth even coefficient (e.g. a free `a8` or anti-invariant `k`) needed inside the `k=0` fibre |
| 2 | The displayed `4 x 4` is the complete first-order normal block. The load `r6=nu` and the eliminated even rows `r2=r4=0` contribute no hidden first-order normal conditions | **CONFIRMED** | a nonzero `d r6 / d(a0,a2,a4,a6)` on parity; a first-order odd-row contribution from `k` inside the fibre; linear dependence of the four odd rows identically |
| 3 | On `p*x5*A!=0`, the substitutions `x3=p x5 (v+2)`, `x1=x5 p^2 (v+1)+x5^2 (3v+1)/(9v)`, `x5=-36 p^2 v^2 (3v^2+3v+1)/(3v^2-2)` are reversible in the function field and cut out `r2=r4=0` | **CONFIRMED** | a different `x1` solving `r2=0`; `r2` or `r4` nonzero after those substitutions; a missed extra component of `r2=r4=0` on the chart |
| 4 | Exact substitution of those formulae into `(2.1)` yields `(3.1)` with the displayed scalar, exponents, denominator, and degree-12 polynomial `Q12` | **REFUTED** | `(3.1)` holding at even one genuine chart point (it fails at `p=1,v=1`); the replay’s `x1` coinciding with `(3v+1)/(9v)` |
| 5 | `Q12` is squarefree and coprime to `v`, `A2`, `D`, `A5`, and is the only remaining normal-rank boundary on the retained chart; the non-`Q12` factors of `(3.1)` are already excluded as elements | **REFUTED** as a rank-boundary claim. The Euclidean facts about the polynomial `Q12` itself hold and do not rescue the claim | `Q12` dividing the genuine numerator; a common root of `Q8` and `Q12`; a chart factor of `(R.1)` meeting the loaded fibre as an element |
| 6 | Over the algebraic closure, `p^9 R6(v)=nu != 0` supplies loaded coefficient points above roots of `Q12`, with constant-field/Kummer typing respected | **CONFIRMED** as algebra and **REFUTED** as a rank-boundary existence statement. Those points exist and are ordinary rank-four points of the fibre. The points at which rank actually drops lie over `Q8=0`, and the same `R6` argument supplies loaded points there | `gcd(Q12,A5)≠1`; `R6` identically zero; a character obstruction that would empty constant `p` in `C` |
| 7 | Invertibility licenses only first-order absence of a normal tangent at a parity coefficient point, not formal trapping, neighborhood emptiness, exclusion of a disjoint component, or a maximum-twelve theorem | **CONFIRMED** as scope of the prose, **REFUTED** as attached to `Q12`. The negative list is observed. The invertibility region is the complement of `Q8=0`, not of `Q12=0` | a hidden trapping, emptiness, non-parity, all-`(9,12)`, maximum-twelve, counterexample, or JC2 promotion in a charged artifact |

All remarks below are non-blocking unless marked otherwise. Claim 4 is blocking. Claims 5–7 fail in so far as they inherit `(3.1)`.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md` | `9616396705d071efac3cf52332c5007a4a045989940bcc8743a545e87f763a1c` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `b34b184264ed91ff78f35295932aa617f4089ac6929b74d3164f65f1abfb1deb` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `c4ddd427b86027b8ab90345eccb2da76a1edfdf2d8488f0d6f3e2ac1b362e5b3` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `bff291fcf01fcb9cfc33e70161be4df59cc0a98315c174ac083cbb3ba8049658` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `2172c53974553ded8cf3d06764e0609ae1a9b590171e3b928a14422120f90ab9` | `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `2af02f169f4c65e7bfd3627d8f05934b0bdbdc35df1c1b9a0577f765b0a6b70e` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `a2d342a0d70911263a72172ba3ee02f21e33951ca9d2f4753f8de39d1dca54d0` | prompt only |

Pinned and named dependencies recomputed, not used as mathematical evidence beyond the licensed inputs named above:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` | `f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d` |
| `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md` | `903a973ac4975dfdeea77d143ebaa33cdc504d0f75d31dfe5327dad2d9be8528` |
| `cases/max12_912_order3_nu_parity_genus5_20260824/replay.py` | `c965bb660cf2f0f55c7ebbed3126b22bfb5d67e178565426aa94ce56f6ce1d9a` |
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` |

The two SHA-256 pins inside `replay.py` match the genus-five replay and fibre-compiler hashes above. `shasum -a 256 -c cases/max12_912_order3_nu_parity_normal_q12_20260824/MANIFEST.sha256` exits `0`. `python3 cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.py | diff -u cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.json -` exits `0`. The replay is internally consistent and proves a rational-function identity on the `x1` it actually substitutes. That `x1` is not the displayed chart. Passing replay is therefore regression of a false substitution, not evidence of `(3.1)`.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present.

---

## Claim 1 — involution, fixed locus, eight-row typing

**CONFIRMED.**

Work in characteristic not `2`. The involution `f(z) |-> -f(-z)` acts on coefficients by `a_i |-> (-1)^{i+1} a_i`. Even coefficients are anti-invariant, so the fixed locus in the depressed degree-nine chart is

```text
a0=a2=a4=a6=0.
```

(The leading term `z^9` is invariant; depression already sets `a8=0`.) Approximate-cubic coordinates with `q=0` give the same locus: `a0=x0`, `a2=x2`, `a4=x4`, `a6=3q` at `q=0`, and

```text
d(a0,a2,a4,a6)/d(x0,x2,x4,q) |_{parity}
```

is triangular of determinant `3≠0`. Characteristic not `3` is ambient Faber. The `4 x 4` in `a`-coordinates is therefore étale-equivalent to the `4 x 4` in `(x0,x2,x4,q)`; rank-drop loci coincide.

On this locus with `k=0` one has `f` odd, unique monic `w=z+O(z^{-1})` odd, and `F_12` even, so `g=F_12` even. Odd tails vanish identically as polynomials in the invariant coefficients. Direct restriction of the pinned tails confirms `r1=r3=r5=r7=0` as elements of `Q[p,x1,x3,x5]`. Independently, the odd-row derivatives in the odd (tangent) columns also vanish on the locus, as required for functions identically zero on `{a_even=0}`.

Even tails are invariant. An invariant function is even in the anti-invariant coordinates, so its first normal derivatives vanish on the fixed locus. Direct restriction of `d r_{2,4,6,8} / d(a0,a2,a4,a6)` to parity yields the zero `4`-tuple for each even row.

The fibre is `k=mu=0`. The `k`-derivatives of the odd rows vanish on parity; the even rows have nonzero `k`-derivatives. Thus `k` behaves as an invariant (tangent) parameter, not as a fifth normal coordinate inside the fibre already cut by `k=0`. The replay.json string `fixed_locus: a0=a2=a4=a6=k=0` mixes the involution locus with the fibre equation `k=0`. Non-blocking: the matrix `(2.1)` does not include a `k`-column, and none is needed.

---

## Claim 2 — completeness of the `4 x 4`; no hidden normal conditions from `r6=nu` or even rows

**CONFIRMED.**

A first-order deformation off parity is `a_even = ε n + O(ε^2)` with invariant coordinates `a_odd = a_odd_0 + ε t + O(ε^2)`. Odd rows vanish identically on the fixed locus, so `d r_odd / d a_odd = 0` there, and the first-order odd conditions are exactly `J_N n = 0`. Even rows are invariant, so `d r_even / d a_even = 0` on the locus; their first-order conditions constrain only `t`. In particular `r6=nu` is an even constraint and contributes no first-order normal equation. The same holds for `r2=r4=0` and for `r8`. Those even equations determine the chart in `(p,v)` (Claim 3) and the load `p^9 R6(v)=nu`; they do not enlarge the normal block.

The four odd rows are not identically dependent: on the genuine chart `det(J_N)` is the nonzero rational function `(R.1)`. Characteristic not `2` or `3` is used for the involution and for the unit `3` in the `a`-versus-`(x,q)` comparison.

---

## Claim 3 — reversible generic-chart substitutions

**CONFIRMED** as written in the report and in the reviewed genus-five theorem. **Not** what the frozen replay substitutes.

On `p*x5*A≠0` set `v=A/(p x5)`, so `x3=p x5 (v+2)`. The coefficient of `x1` in `r2` is `(4/9)A≠0`, hence

```text
x1 = x5 p^2 (v+1) + x5^2 (3v+1)/(9v)
```

is the unique solution of `r2=0` in the function field. The denominator `9v` is nonzero as an element because `v=0` is `A=0`, already excluded by the genus-five theorem. Substituting into `r4=0` recovers

```text
(3v^2-2) x5 + 36 p^2 v^2 (3v^2+3v+1) = 0,
```

and `Res(3v^2-2, 3v^2+3v+1)=27≠0`. As elements of the function field, `D=3v^2-2` cannot vanish on the chart and `A2=3v^2+3v+1` cannot vanish without forcing the already-excluded `x5=0`. The solve

```text
x5 = -36 p^2 v^2 A2(v) / D(v)
```

is therefore reversible in `K`. Independent evaluation of the even tails at these substitutions, at twenty-four rational `v` with `p=1` and by exact rational-function arithmetic, gives `r2=r4=0` identically and recovers the reviewed `R6(v)`.

The frozen replay does not implement this `x1`. It implements

```text
x1_replay = x5 p^2 (v+1) + x5^2 (1/3) / (9v) = x5 p^2 (v+1) + x5^2 / (27 v).
```

The genus-five replay writes `Rat((Fraction(1), Fraction(3)))`, i.e. the polynomial `1+3v`. The present replay writes `genus.Rat.constant(Fraction(1, 3))`, i.e. the constant `1/3`. These agree only at the point `3v+1=1/3`, i.e. `v=-2/9`, which is not an identity. At all twenty-four sample values, `r2` and `r4` vanish for the displayed `x1` and do not vanish for `x1_replay`. The displayed chart is the loaded fibre; the replay slice is not.

---

## Claim 4 — exact determinant `(3.1)` and `Q12`

**REFUTED.**

`det(J_N)` depends on `x1`. At the off-chart test point `p=1`, `x3=5`, `x5=7`, Gaussian elimination over `Q` gives two different values at `x1=2` and `x1=11`. Restriction to a wrong `x1` is therefore not harmless.

On the replay slice `x1_replay`, Gaussian elimination and the exact rational-function determinant both recover `(3.1)` identically, including the scalar `-8388608/243 = -2^{23}/3^5`, the powers `v^{14}`, `A2^7`, `D^{10}`, and the displayed `Q12`. That is why the frozen replay passes. It is an identity off the fibre.

On the displayed `r2=r4=0` substitutions, `(3.1)` fails at every one of the twenty-four sample values. Smallest concrete counterexample, `p=1`, `v=1` (so `A2=7`, `D=1`, chart denominators units):

```text
x5 = -252,    x3 = -756,    x1 = 27720,
det(J_N) = 25275425185572323328,
(3.1)    = 169664962152837939200 / 243.
```

The two rationals are not equal. The same point has `r2=r4=0` and `R6(1)≠0`.

Exact reconstruction of the genuine determinant, by Gaussian elimination of the `4 x 4` over `Q(v)` after the displayed substitutions, followed by peeling the chart factors, yields `(R.1)`–`(R.2)`. Five further exact samples (`v=1,2,-1,1/2,5`) match `(R.1)` and mismatch `(3.1)`. The determinant is weighted-homogeneous of weight `40` for `wt(z)=1`, as required by `wt(r1,r3,r5,r7)=(13,15,17,19)` and `wt(a0,a2,a4,a6)=(9,7,5,3)`; setting `p=1` extracts the `p^{20}` factor.

`Q12` does not divide the genuine numerator. The residual on the loaded chart is the octic `Q8`, not the dodecic `Q12`.

---

## Claim 5 — squarefreeness, gcds, and exclusion of non-`Q12` factors

**REFUTED** as the statement that `Q12=0` is the only remaining normal-rank boundary on the retained chart. The Euclidean facts about the polynomial `Q12` itself are true and non-rescuing.

Independent monic Euclidean algorithm over `Q`:

```text
gcd(Q12, Q12') = 1,     Q12(0) = 480 ≠ 0,
gcd(Q12, A2) = 1,       gcd(Q12, D) = 1,       gcd(Q12, A5) = 1,
gcd(A2, D) = 1.
```

So `Q12` is squarefree and coprime to the listed chart polynomials. Those are facts about a polynomial that is not a factor of `det(J_N)` on the fibre.

On the genuine chart the vanishing locus of `det(J_N)` is cut by `v`, `A2`, `D`, and `Q8`. The first three are already excluded as *elements* by the reviewed genus-five theorem, by the same argument the producer gives: `v=0` is `A=0`; `A2=0` forces `x5=0`; `D=0` makes the `r4` identity impossible on `p v ≠ 0`. Places at which they vanish remain places, not extra coefficient branches. That exclusion is not an improper saturation; it simply does not touch `Q12`, and it leaves `Q8=0` as the residual.

Independently:

```text
gcd(Q8, Q8') = 1,       Q8(0) = 24 ≠ 0,
gcd(Q8, A2) = 1,        gcd(Q8, D) = 1,        gcd(Q8, A5) = 1,
gcd(Q8, Q12) = 1.
```

`Q8` is squarefree of degree `8`, coprime to every chart factor and to `Q12`. No rational root. The producer’s claim that non-`Q12` factors of `(3.1)` are the only ones to exclude is false because `(3.1)` is the wrong function: the factor that remains on the fibre is `Q8`, which is coprime to `Q12`.

---

## Claim 6 — loaded algebraic points; `r6=nu`; constant field / Kummer

**CONFIRMED** that `p^9 R6(v)=nu` supplies coefficient points over roots of `Q12`, and **REFUTED** that those points are the rank-drop locus.

The reviewed identity `R6(v)=-2304 v^6 A2^3 A5 / D^4` was reconfirmed on the genuine chart. Because `gcd(Q12, v A2 D A5)=1`, a root of `Q12` in `C` has `R6(v)∈ C^*`. For any `nu∈ C^*` the equation `p^9=nu/R6(v)` has solutions in `C`. These are algebraic points of the coefficient scheme, not actual Keller trajectories: the genus-five theorem already emptied every actual trajectory on the whole parity locus, including both `Q12=0` and `Q8=0`. The producer does not treat them as actual base solutions; that distinction is observed.

Kummer typing is vacuous for these constant points. Character two of `p` and the cube calculation `p^9∈ K` belong to actual trajectories, which do not exist on parity. Over the algebraic closure of the constant field, ninth roots of nonzero constants exist. No obstruction.

Those `Q12` points are nevertheless ordinary rank-four points of the loaded fibre, because `gcd(Q8,Q12)=1`. The same `R6` argument, using `gcd(Q8,A5)=1`, supplies loaded algebraic points above roots of `Q8`, and *those* are the points at which `J_N` drops rank. The sentence “`(3.3)` is not made empty by `r6=nu≠0`” is true of a locus that is not a rank boundary and false as a description of the residual.

---

## Claim 7 — geometric conclusion licensed by invertibility

**CONFIRMED** that the charged prose does not claim formal trapping, neighborhood emptiness, exclusion of a disjoint non-parity component, or a maximum-twelve theorem. **REFUTED** that invertibility holds away from `Q12=0`.

The correct first-order dictionary: invertibility of `J_N` at a loaded parity *coefficient* point means there is no first-order normal tangent to the loaded fibre there. It does not trap a formal arc (order `≥2` may leave), does not empty an analytic neighborhood, does not speak to a component disjoint from parity, and does not bound degrees. The report, registration, README, FREEZE scope block, and replay payload all stay inside that negative list. No numbered promotion to JC2 or to maximum twelve is present.

What fails is the invertibility region. Away from `Q8=0` and the already separated `p`, `x5`, `A` element-boundaries, `J_N` is invertible and a formal coefficient-scheme component meeting parity there cannot acquire a first-order normal tangent. Away from `Q12=0` this is false: every `Q8`-root with chart denominators nonzero is a counterexample to the producer’s invertibility statement, and every `Q12`-root with chart denominators nonzero is a point the producer would have excluded as rank-deficient while `J_N` is actually invertible.

Scheme-versus-point language in §4 (“scheme-theoretically normal-unramified along the parity fixed locus at first order”) is the right type of statement for a unit determinant on a chart. Attached to the vanishing of `Q12` it is the wrong closed set. The base locus of the linearization is the coefficient scheme cut by `r2=r4=0`, `r6=nu`, not an actual Keller trajectory; the producer does not confuse those, and the genus-five emptiness of actual trajectories is not misused as a base solution.

---

## Attacks that land

- **Wrong `x1` in the replay.** Report and genus-five theorem use `(3v+1)/(9v)`. Replay uses `(1/3)/(9v)`. `det` depends on `x1`. `(3.1)` is the determinant on the latter slice, where `r2` and `r4` are nonzero.
- **`Q12` is not a factor of the genuine determinant.** Independent gcd of the genuine numerator against `Q12` is `1`. Invertibility at `Q12=0` and rank drop at `Q8=0` are simultaneous counterexamples to the named residual.
- **Passing replay is not a proof of the report.** The replay asserts exact rational-function equality after its own substitution. That equality holds and is irrelevant to §3 as written.

## Attacks that do not land

- **Hidden first-order condition from `r6=nu`.** Even row; normal derivatives vanish on parity. Confirmed by direct restriction.
- **`a`-coordinates versus `(x0,x2,x4,q)`.** Jacobian factor `3` is a unit. Rank loci coincide.
- **`k` as a fifth normal direction.** Odd `k`-derivatives vanish on parity; the fibre is already `k=0`. No extra column in `(2.1)`.
- **Improper saturation of `v`, `A2`, `D`.** Those vanish only as places, not as elements, on the retained chart, by the reviewed genus-five theorem. The same exclusions apply to `(R.1)`. They do not create `Q12`.
- **Misuse of the excluded parity trajectory as an actual base solution.** Not present. The linearization is of algebraic coefficient points. The genus-five theorem is used only as chart data and as element-exclusions.
- **Scope inflation to trapping, non-parity emptiness, maximum twelve, or JC2.** Absent from every charged artifact.

---

## Non-blocking remarks

- The Euclidean ledger for `Q12` in the replay is a correct ledger for that polynomial. It does not identify the rank boundary.
- Weighted homogeneity of `det(J_N)` and the extraction `p=1` then restore `p^{20}` are correct on both slices.
- The fibre compiler has no completed different-model review. Odd-tail derivatives used here are those of the pinned Faber engine. The refutation of `(3.1)` is a substitution failure on that matrix and does not depend on rebuilding `z(w)` from scratch.
- Characteristic not `2` or `3` is the ambient Faber inverse-root / binomial `F_j` setting, as in the genus-five review.
- `(R.1)`–`(R.2)` are reviewer identities. They are not frozen, not replay-pinned, and not promoted.

---

## What this does not license

This review does not license: invertibility away from `Q12`; a trapping claim at `Q8` or at `Q12`; emptiness of a non-parity component; any generic loaded component; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2. It also does not freeze `(R.1)` as a successor theorem.

---

**Verdict.** `REFUTED`

Smallest failing identity: `(3.1)` after the displayed substitutions `x3=p x5 (v+2)`, `x1=x5 p^2 (v+1)+x5^2 (3v+1)/(9v)`, `x5=-36 p^2 v^2 (3v^2+3v+1)/(3v^2-2)`. Counterexample `p=1`, `v=1`: `det(J_N)=25275425185572323328` against right-hand side `169664962152837939200/243`.
