# Hostile review: EXACT-N-RIGIDITY and STAR-REALISABILITY

Reviewer: GPT-5.5/Codex hostile review. Date: 2026-09-02.

Scope: review only the new claims in `EXACT-N-RIGIDITY` and
`STAR-REALISABILITY`. I did not re-review integration #17. I used #17 only as
reviewed input for JAC-FIBRE, FRONTIER-EXACT, D1-PIN, D1-STAR, RADIUS-ORDER,
and PIN-NOT-CEILING.

Input custody: the six frozen inputs in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.EfPwqb/inputs`
were checked first with `shasum -a 256 -c`; all returned `OK`. No ledger edits
and no `jc2-lean`.

Verdict summary:

| Item | Verdict | Promotion recommendation |
|---:|---|---|
| 1 | CONFIRMED | Promote Phi monotonicity, Phi-DICT, Phi(delta_1)=1, and the D1-STAR sandwich, with the repairs below. |
| 2 | CONFIRMED | Promote "not an artefact", with scope: Prop. 5.3 gives the geometric predecessor radius for `r>=2`; use `r=2` for `delta_1`. |
| 3 | MIXED: CONFIRMED core, REFUTED subclaim | Promote `A_bot` warning and the two-sided/integrality window. Do not promote "`L` never exceeds 3.32 to `D<=190`"; the local D<=190 table refutes it. |
| 4 | CONFIRMED | Promote the D<=140 and D<=190 SINGLE counts; type MIXED cap hits as OPEN. |
| 5 | CONFIRMED | Promote NO-RESIDUE with wording repair: calculus is for any Puiseux series `h`; the `1/g_y` conclusion is for simple branches of fibres of `g`. |
| 6 | CONFIRMED | Close forced-repeated-root STAR obstruction. Promote squarefree bottom partition `(1^(e V_2))`, not global Keller realisability. |
| 7 | CONFIRMED | Promote the D=105 STAR row under its stated campaign order; repair notation by separating per-root `c=1/10` from packet `q=3/10`. |

## Sources Used

Charged reports:

- `exact-n-rigidity-opus5-20260902.md`: Phi and EXACT-N claims at lines
  51-57, 73-86, 125-137, 265-317, 344-399, 403-440, 488-545.
- `star-realisability-sol56-20260902.md`: squarefree and STAR claims at lines
  210-266, 327-346, 385-428, 434-514, 552-584.

Reviewed baseline consumed, not re-reviewed:

- `integration17-coordinator-fable51-20260902.md`: JAC-FIBRE and
  FRONTIER-EXACT at lines 14-21; D1-PIN and RADIUS-ORDER at lines 22-35;
  promoted list at lines 109-116.
- `d1-subtree-review-grok46-20260902.md`: JAC-FIBRE reproof at lines 61-85;
  FRONTIER-EXACT at lines 91-101; D1-PIN at lines 109-161; D1-STAR at
  lines 167-192; final promoted/retracted/open block at lines 380-459.

Implementation and logs:

- `box/exactn-drivers-20260902/exactn.py`: Phi/floor formulas at lines 38-54;
  group data at 104-112; SINGLE/MIXED at 115-157; run counters at 159-205.
- `box/exactn-drivers-20260902/exactn140.log`: completed D<=140 run at
  lines 43-90, including D=105 at line 65 and totals at 82-90.
- `box/exactn-drivers-20260902/exactn-single200.log`: D<=190 row table at
  lines 80-102; summed locally to the quoted D<=190 totals.
- `box/exactn-drivers-20260902/noresidue.py`: calculus statement and cases at
  lines 3-14, 22-27, 29-57.
- `box/exactn-drivers-20260902/noresidue.log`: controls at lines 1-18.
- `box/exactn-drivers-20260902/treestar.py`: root-free contact resultant
  method at lines 3-12 and checks at 44-89.
- `box/exactn-drivers-20260902/treestar.log`: Keller witness rows at lines
  16-27.
- `xmodel/exact-packet-filter-gpt55-20260902.md`: packet semantics at lines
  32-40, D=105 exact variants at lines 73-85, and scope at 146-150.
- `box/star-realisability-drivers-20260902/star_realisability.py`: `q`,
  bidegree, operator scaling, STAR result, scan/table, and D=105 printer at
  lines 112-209 and 239-389.
- `xmodel/star-realisability-sol56-20260902.log`: completed STAR run at lines
  3719-3784.

Moh page images/text:

- Rendered page images read from `refs/moh1983_jram340_configurations_of_roots.pdf`:
  `/tmp/jc2-moh-pages/p170.png`, `p171.png`, `p180.png`, `p184.png`, `p207.png`.
- OCR line references in `box/depth-drivers-20260902/moh_raw.txt`: Prop. 4.6
  statement at lines 1122-1144; Prop. 5.3 geometric predecessor radius at
  lines 1462-1473; p.184 invocation of A.5 at lines 1564-1577; Prop. A.5
  location at lines 2377-2381. The OCR misreads the product dot in A.5 as a
  dash; the p.207 page image clearly says `p(pi) . q(pi)` has only simple roots.

## Item 1: Phi Lemma And Sandwich

Verdict: CONFIRMED.

Claim reviewed: define

```text
Phi(delta) = delta - lambda_f(delta) - lambda_g(delta)
```

along the path of a `g`-root. Its slope is `1-a-b`, so it is non-increasing;
JAC-FIBRE gives `Phi(delta^0)>=1` at a `g`-frontier; RADIUS-ORDER at `r=1`
with `M_1=-m` gives `Phi(delta_1)=1`; therefore `Phi` is constant on
`[delta_1,delta^0]` and `a+b=1`.

Reproof. Fix a branch/root `rho` of `g-c_2`. For a radius `delta`, let `a` be
the number of active `g` roots in the ball containing `rho` and `b` the number
of active `f` roots in that same ball. On an interval with no parting event,
`lambda_g' = a` and `lambda_f' = b`, by the definition
`lambda_h=sum min(delta, contact)`. Hence

```text
Phi' = 1 - a - b <= 0
```

because the tracked `g` root gives `a>=1` and `b>=0`. Continuity of the `min`
functions handles the breakpoints. This proves monotonicity. This is also what
the driver computes: `Phi` is implemented incrementally in `exactn.py:38-41`,
and the closed tower expression is separately computed in `exactn.py:43-45`.

At the `g`-frontier `delta^0`, `lambda_g(delta^0)=0`. Reviewed
FRONTIER-EXACT says that on a proper branch
`lambda_f(delta^0)=delta^0-1`; see integration #17 lines 18-21 and the
hostile reproof in `d1-subtree-review...:91-101`. Therefore

```text
Phi(delta^0) = delta^0 - (delta^0-1) - 0 = 1
```

on every proper frontier. In the non-proper case reviewed JAC-FIBRE gives
`delta^0>1` and zero contribution (`integration17...:14-21`,
`d1-subtree-review...:77-81`), so if `lambda_f(delta^0)=0`,
`Phi(delta^0)=delta^0>1`. Thus the correct statement is stronger and cleaner:
proper frontier means equality; arbitrary frontier gives `>=1`.

For `delta_1`, reviewed RADIUS-ORDER gives

```text
lambda_g(delta_r) = - n(1-delta_r)/(n-M_r)
```

under `M_s=n-2` (`d1-subtree-review...:125-135`). Def. 5.1(1) gives
`lambda_f=(m/n)lambda_g` along the tower (`d1-subtree-review...:160-161`).
Hence

```text
Phi(delta_r)
 = delta_r + (n+m)(1-delta_r)/(n-M_r).
```

At `r=1`, `M_1=-m`, so `n-M_1=n+m` and

```text
Phi(delta_1) = delta_1 + (1-delta_1) = 1.
```

This is exactly the formula stated in the charged report at
`exact-n-rigidity...:280-286` and checked in `exactn.py:57-88`. The saved
D<=140 log shows all P1/P2 controls passed, including all 242,099 V-skeletons
at `n<=100` (`exactn140.log:28-40`).

The sandwich now follows without another inequality. Since
`delta^0>delta_1` for the bottom-major proper branch (reviewed D1-PIN/D1-STAR
input; `d1-subtree-review...:188-190`), monotonicity gives
`Phi(delta^0)<=Phi(delta_1)=1`, while Phi-DICT gives `Phi(delta^0)>=1`.
Therefore `Phi` is identically 1 on the interval. On every open subinterval,
`Phi'=0`, hence `a+b=1`. Because `a>=1`, the `g` branch is alone in the joint
`f*g` tree above `delta_1`, with no `f` root in the ball. That is exactly the
star conclusion in `exact-n-rigidity...:293-317`.

Repair: state `Phi(delta^0)=1` at proper frontiers and `>1` only for
non-proper frontiers; define `a,b` as active counts on open intervals between
parting radii. Do not say the floor is "attained" globally; only the per-disc
density is pinned.

## Item 2: Phi(delta_1)=1 Is Not A Definition Artefact

Verdict: CONFIRMED.

Moh Prop. 5.3 is geometric: for `r>=2`, after a chosen factor of the
Prop. 4.6 polynomial, it defines `delta_{r-1}` as the logarithmic radius of the
minimal disc containing the roots with contact above `delta_r`; see
`moh_raw.txt:1462-1473`, checked against the p.180 page image. Taking `r=2`
is the relevant use for `delta_1`. The Def. 5.1(3) radius formula is then a
proved recursion, not a bare normalisation. The charged report's statement at
`exact-n-rigidity...:344-353` is accurate with this `r=2` wording.

Independent Keller controls are also real but should be typed correctly.
`treestar.py` computes the joint contact tree from
`Res_y(g(x,y), h(x,y+w))`, so no Moh recursion is used
(`treestar.py:3-12`, `44-89`). In the four Keller pairs,
`Phi(delta_1)=1`, FRONTIER-N reproduces `N=1`, and D1 is a star; see
`treestar.log:3-14`, `16-27`, `29-40`, and `42-53`. These examples have
`nu=1`, so they are geometry controls, not NU-TWO counterexample candidates.

Repair: phrase the Moh point as "Prop. 5.3 gives `delta_{r-1}` geometrically
for `r>=2`; in particular `delta_1` is obtained when the current level is
`r=2`." Keep the explicit Keller pairs as controls outside the counterexample
census.

## Item 3: A_bot, Window, And The Floor L

Verdict: CONFIRMED for the structural claims; REFUTED for the numeric phrase
"`L` never exceeds 3.32 to `D<=190`."

EXACT-N itself is the formula

```text
N = sum_B a_1(B) * d(1-delta_1(B))/(d+e)
```

over bottom-major discs, with other roots contributing zero by
DETECTOR-NULL/MINOR-FRONTIER. The charged report states it at
`exact-n-rigidity...:403-417`. The implementation matches:
`contrib(S)=d(1-delta_1)/(d+e)` at `exactn.py:52-54`,
`floor_L(S)=a_1*contrib(S)` at `exactn.py:47-50`, and group options store
`(a_1,L,U,c)` at `exactn.py:104-112`.

The two-sided window follows:

```text
L = a_1 c = e V_2 d(1-delta_1)/(d+e) <= N <= u e c = U,
L/U = V_2/u.
```

`U` is reviewed N-CEILING; `L` is the new lower bound. The identity
`U*a_1 = L*u*e` is checked in `exactn.py:90-96`, and the saved log shows
the P3/P4 checks pass (`exactn140.log:34-40`).

`A_bot` is not a skeleton function. The charged witness

```text
f = x + y^5,
g = y + (x+y^5)^3
```

has `J=1`, `deg_y(f,g)=(5,15)`, and

```text
Res_y(f-7/3, g+5/2) = (459165024*x - 373007043793157)/459165024,
deg_x Res = 1.
```

The tree check reports, per `g` root, two other `g` roots at contact `11/15`,
twelve at `-1/5`, and one `f` root at `11/15`; it gives
`delta_1=11/15`, `a_1=3`, `b_1=1`, `delta^0=14/15`, `N=1`
(`treestar.log:16-27`). Thus the equivalence relation `contact >= 11/15`
partitions the 15 `g` roots into five conjugate D1 discs of size 3. Because all
15 roots lie in bottom-major discs, `A_bot=15`, not the single-disc `a_1=3`.
This is a valid witness that the number of bottom discs is not determined by
one skeleton row. Repair: the witness is `nu=1`, outside NU-TWO, so it refutes
the general "A_bot is a skeleton function" principle, not any NU-TWO-specific
orbit theorem.

The numerical overclaim: `exact-n-rigidity...:81-84` says the floor "never
fires (max L = 3.32 to D<=190)" and line 528 states `63/19=3.32` for D<=140.
The D<=140 half is supported: `exactn140.log:43-90` has `maxL=63/19` through
D=140 and no floor kills. The D<=190 extension is not supported by the local
row table. In `exactn-single200.log:80-102`, after D=140 the `maxL` column
contains `108/25`, `135/28`, `224/59`, `165/31`, and `288/67`; the maximum
through D=190 is `165/31 = 5.32258...` at D=176. A local row-sum confirmed:

```text
D<=190 rows: groups=76282, kU=1288, kSINGLE=49623, maxL=165/31.
```

No floor kill follows, since `165/31 < 16`, but the claimed "3.32 to D<=190"
is false. Promote "floor never fires to D<=190" if desired; do not promote the
3.32 maximum beyond D<=140.

## Item 4: MIXED/SINGLE Counts And D=105 Reconciliation

Verdict: CONFIRMED, with cap typing.

Fresh rerun performed in this review:

```text
python3 box/exactn-drivers-20260902/exactn.py --control-nmax 100 --nmax 100 --exact
```

It completed in 52.1s with all Phi controls passing and returned:

```text
D<=100 groups=3975
floor kills=0
ceiling U<6 kills=274
SINGLE kills=2499
MIXED kills=1121
MIXED cap hits=847
degrees emptied=NONE
```

This agrees with the D<=100 prefix of the completed D<=140 saved log
(`exactn140.log:43-62`) when summed.

The D<=140 measurement is supported by the completed saved run:

```text
groups=18064
floor kills=0
ceiling U<6 kills=697 = 3.9%
MIXED kills=5275 = 29.2%, cap hits=4750 typed UNDECIDED
SINGLE kills=11992 = 66.4%
degrees emptied=NONE
```

See `exactn140.log:82-90`, with the D=105 row at line 65. The code counts
branch-robust groups and treats capped MIXED searches as undecided rather than
killed (`exactn.py:183-188`, `199-205`). This is the correct conservative
direction.

The D<=190 SINGLE total is supported by summing `exactn-single200.log:46-102`:

```text
groups=76282
ceiling U<6 kills=1288
SINGLE kills=49623 = 65.0%
degrees emptied=NONE
```

The saved log has no footer, so this is a mechanical row-table sum, not a
printed total. No row has `kSINGLE=#groups`.

D=105 reconciliation against `exact-packet-filter-gpt55-20260902.md`:

- `exactn.py --only 105 --exact` under the campaign window `[6,16]` gives
  `264` groups, `kMIXED=159`, and `cap hits 0`. This matches
  `exactn140.log:65` and the fresh focused run.
- GPT-5.5 exact-packet-filter has two variants. Its `N integer >=6` variant
  gives `125` hits and `139` no-hits at D=105 (`exact-packet-filter...:73-77`).
  Its restricted `N integer in [6,16]` variant gives `105` hits and `159`
  no-hits (`exact-packet-filter...:82-85`).

Thus the exact equality is:

```text
EXACT-N-MIXED D=105 count 159/264
  = exact-packet no-hit count for N in [6,16]
  = 264 - 105.
```

The apparent `125` discrepancy is the wider `N>=6` variant:

```text
125 - 105 = 20
```

groups have a mixed packet only outside the campaign window, i.e. with
integer `N>16` (the D=105 union there reaches 17 through 30). Those groups are
alive for the lower-frontier-only question and dead for the bounded campaign
window `[6,16]`. Both computations are MIXED packet computations over lower
V-profile branch types; they ask different target sets. A focused run with
`Nhi=30` in the older exactn driver hit its 20,000-state cap twice, so the
full Fraction exact-packet row is the cleaner widened comparator.

Repair: every count must name its target set: `N>=6` or `N in [6,16]`, and
whether it counts hits or no-hits.

## Item 5: Corollary NO-RESIDUE

Verdict: CONFIRMED, with wording repair.

The calculus statement is correct even with fractional exponents. Let
`t=x^{-1}` and let

```text
h(t) = sum_a c_a t^a,       a in (1/l) Z
```

be any Puiseux series without logarithms. Then

```text
d/dx h = -t^2 d/dt h = - sum_a a c_a t^(a+1).
```

The coefficient of `x^{-1}=t^1` would require `a+1=1`, hence `a=0`, and its
coefficient is `-0*c_0=0`. Fractional exponents introduce no exception: there
is still only one exponent with `a+1=1`. This is exactly the argument in
`noresidue.py:3-14` and `exact-n-rigidity...:125-130`.

For a simple branch `tau` of a fibre `g=c_2`, implicit differentiation gives

```text
g_x + g_y tau' = 0
d/dx f(x,tau) = (f_x g_y - f_y g_x)/g_y = J/g_y(x,tau).
```

For a Keller pair `J in C^*`, the calculus vanishing for
`h=f(x,tau(x))` implies

```text
[x^-1] 1/g_y(x,tau) = 0
```

on every simple branch of every fibre of `g`. The "simple" qualification means
`g_y(x,tau)` is not identically zero on the branch; for generic fibres of a
monic polynomial this is the relevant case.

The negative control is correctly computed. For

```text
g = y^2 - x^2 - x
```

on the branches `y=+-sqrt(x^2+x-c_2)`,

```text
1/g_y = 1/(2y)
      = +- (1/(2x)) * (1 + x^-1 - c_2 x^-2)^(-1/2),
```

so `[x^-1]1/g_y = +-1/2`. Also `ord_t g_y=-1`, hence
`delta^0=-ord_t g_y=1`, the leading-order case forbidden by LEMMA DICT.
The local driver reports `[1/2,-1/2]` for `g=y^2-x^2-x` and for the shifted
variant (`noresidue.log:5-10`), and zero for coordinate controls
(`noresidue.log:2-4`, `14-16`). The row `y^2-x^3-x^2` is correctly typed
vacuous for this test (`noresidue.log:11-13`): the reported zero is not a kill,
because the relevant lattice behaviour makes `t^1` absent in that leading
case.

What NO-RESIDUE adds beyond Moh's search conditions: Moh's numerical search
conditions encode leading orders, radii, degree chains, and leading
polynomial constraints. NO-RESIDUE is a coefficient-level residue condition on
`g` alone after a branch of a fibre is chosen. Its leading-order consequence is
the already visible `delta^0 != 1` obstruction: if `1/g_y` has leading term
`t^1`, the coefficient is nonzero and Keller is impossible. Beyond that,
when `t^1` is a subleading term, the condition depends on Puiseux coefficients
of `g`, not merely on `(n,m,M,V)` or the list of radii.

Therefore NO-RESIDUE is not a skeleton condition at any numerical order in the
current Moh skeleton sense. If one augments the data by enough Puiseux
coefficients, it becomes a finite jet/residue equation for that coefficient,
but that is coefficient data, not the skeleton. It is automatic on the `f`
side and a genuine necessary condition on candidate `g`; it is not a
standalone sufficiency statement and was not run as a census kill here.

Repair: replace "for any Puiseux `tau`" by "for any Puiseux series `h`, the
derivative has zero `x^-1` coefficient; applying this to
`h=f(x,tau(x))` on a simple branch of `g=c_2` gives the condition on
`1/g_y`."

## Item 6: Prop. 4.6 -> A.5 Squarefree Bottom

Verdict: CONFIRMED, with scope repair.

Moh Prop. 4.6 itself separates the cases. On p.170, the distinct-root list is
under `r>=2`; the `r=1` clause says only that `g_sigma(pi)` and
`T^psi_{1,sigma}(pi)` satisfy

```text
D(n, -M_1, g_sigma(pi), T^psi_{1,sigma}(pi)) = nonzero constant.
```

This is visible on the p.170 image and in `moh_raw.txt:1122-1144`. The proof
on p.171 derives the `r=1` operator after noting
`T_1^psi=f+polynomial in g`; see the p.171 image.

Prop. A.5 on p.207 says: if `m=deg p(pi)`, `n=deg q(pi)`, and
`D(m,n,p,q)=c` with `c!=0`, then `p(pi).q(pi)` has only simple roots. The OCR
line `moh_raw.txt:2380` misreads the product dot as a dash; the page image
`/tmp/jc2-moh-pages/p207.png` clearly has the product dot.

For the bottom disc, put

```text
P_1 = g_{sigma_1}(pi),
Q_1 = T^psi_{1,sigma_1}(pi).
```

With `K=gcd(n,m)`, `n=K e`, `m=K d`, and bottom multiplicity `V_2`, the local
degrees are

```text
deg P_1 = e V_2,       deg Q_1 = d V_2.
```

This is the arithmetic isolated in `star-realisability...:210-222` and checked
in code by `bottom_bidegrees` and `operator_scale`
(`star_realisability.py:157-182`). Since

```text
(n,m) = (K/V_2) * (deg P_1, deg Q_1),
```

the Prop. 4.6 operator rescales to

```text
D(deg P_1, deg Q_1, P_1, Q_1)
  = (V_2/K) D(n,m,P_1,Q_1) in k^*.
```

Prop. A.5 applies, so `P_1 Q_1` is squarefree. In particular `P_1` itself is
squarefree, and the bottom partition is forced to

```text
(1^(e V_2)).
```

This also follows by the elementary repeated-root argument in the Sol report:
if `alpha` is a repeated root of `P_1`, then both `P_1(alpha)` and
`P_1'(alpha)` vanish, making
`n P_1 Q_1' - m Q_1 P_1'` vanish at `alpha`, contrary to the nonzero constant
(`star-realisability...:231-241`).

Moh's own p.184 use is narrower but confirms the inference. In Prop. 5.4's
`i=1` all-roots subcase, he applies Prop. 4.6, then explicitly invokes A.5 and
concludes `g_sigma(pi)` has distinct roots; see `moh_raw.txt:1564-1577` and
the p.184 page image. The general `V_2<=K` bottom-disc statement is not printed
there as a separate theorem; it is the rescaling above. That rescaling is
valid exactly because the bottom degrees match the coefficient weights up to
the same positive factor.

The measurement follows almost tautologically from the theorem but is still
implemented fail-closed. `star_test` checks the scale and returns
`PASS[MOH-PROP-4.6+A.5-FORCED-SIMPLE]` with partition `(1,)*degree`
(`star_realisability.py:193-209`). The scan counts only rows with a `(UNI)`
integer `N>=6` witness (`star_realisability.py:239-266`), and the saved run
prints:

```text
MOH-SHARP-2: enumerated=655892, tested=6328, killed=0, surviving=6328.
D<=120:     enumerated=902893, tested=9553, killed=0, surviving=9553.
```

See `star-realisability-sol56-20260902.log:3719-3784`, with totals at
`3731-3732` and `3763-3764`. I also ran the scan functions directly in this
review because the script's `main()` hard-codes an expired producer temp input
path; the direct run reproduced the same totals and the D=105 row.

Repair: say "Prop. 4.6 at `r=1`, combined with Prop. A.5 after degree
rescaling, forces simple bottom roots." Do not say Prop. 4.6's printed
`r=1` conclusion list itself contains the simple-root assertion. Promote the
closure of forced-repeated-root STAR only; do not promote any claim that all
tested numerical skeletons are globally realised by Keller pairs.

## Item 7: D=105 STAR Row

Verdict: CONFIRMED, with notation repair and order caveat.

The row in `star-realisability...:446-493` is:

```text
n=105, m=70, M=(-70,-63,103), V=(1,4,1),
K=35, (d,e)=(2,3), (u,v)=(20,15).
```

Direct recomputation with `Skel(105,70,[-63,103],{2:1,3:4})` gives:

```text
d_i=(105,35,7,1)
delta=(3/4, 71/95, -1)
lambda_g=(-3/20, -3/19, -105)
a=(3,60,105)
b=(2,40,70)
u=20, v=15
windows_ok=True
```

The Def. 5.1 windows printed in the Sol report are correct:

```text
35/(105-(-63)) = 5/24 < V_2=1 <= V_3*35/7 = 20,
7/(105-103) = 7/2 < V_3=4 <= V_4*7 = 7.
```

There are two compatible weights in circulation:

```text
per-root c = d(1-delta_1)/(d+e) = 2*(1/4)/5 = 1/10,
per-V_2-unit q = e*c = (1-delta_1) d e/(d+e) = (1/4)*(6/5) = 3/10.
```

Sol's `q=3/10` is the per-`V_2` packet weight used by
`star_realisability.py:112-114`, not the per-root `contrib` used by
`exactn.py:52-54`. With `k=20` equal bottom discs and `V_2(B)=1`,

```text
N = k V_2 q = 20 * 1 * 3/10 = 6.
```

The bottom bidegree is `(deg P_1,deg Q_1)=(eV_2,dV_2)=(3,2)`, and the operator
scales as

```text
D(105,70,P_1,Q_1) = 35 D(3,2,P_1,Q_1).
```

The bottom partition is therefore `(1^3)`, as printed at
`star-realisability...:498-514` and in the saved run
`star-realisability-sol56-20260902.log:3767-3784`.

Order caveat: this is the smallest D=105 row for the STAR report's stated
campaign order `(s,N_min,e,m,M_2..M_s,V_2..V_s)`
(`star-realisability...:434-444`). It is not the same as the exact-packet
filter's lexicographic order on `(m,M_tuple,V_s)`, which selects
`(105,42,(-14,103),5)` with `N=10`
(`exact-packet-filter...:106-128`). Both statements are consistent once the
order is named.

## OPENs And Bounded Residue

No new exit-price assertion is made; no `charge_basis` line is applicable.

`OPEN[BRANCH-PROFILE]` remains from EXACT-N: whether all major branches in an
actual pair share one lower-V profile. Bounded quantity per branch-robust group:
the number/partition of bottom-major branch classes with
`sum_B V_2(B)<=u`, equivalently the integer `A_bot/a_1` in `[1,u/V_2]` in the
single-profile case. See `exact-n-rigidity...:617-628`.

`OPEN[MIXED-CAP-D<=140]`: 4,750 D<=140 groups are capped in the MIXED
knapsack and are typed UNDECIDED, never killed (`exactn140.log:82-90`).

`OPEN[MIXED-141-190]`: MIXED was not completed in the D=141..190 slice in the
local artifacts. The bounded group count for that slice is
`76,282 - 18,064 = 58,218` branch-robust groups, using the D<=190 row-sum and
the completed D<=140 total.

`OPEN[NO-RESIDUE-CENSUS]` is not promoted as a numerical skeleton test. The
condition is a coefficient/jet equation on `g`; it should be applied only after
a coefficient model or Puiseux jet is present.

`OPEN[GLOBAL-REALISABILITY]` is outside STAR-REALISABILITY: the squarefree
bottom result says a forced repeated bottom root kills no tested assignments;
it does not assert a Keller pair realises any numerical skeleton.

## Typed Verdict Block

```text
LANE        EXACT-N-RIGIDITY / STAR-REALISABILITY hostile review
SCOPE       New claims above integration #17 only.  #17 not re-reviewed.

CONFIRMED   (1) Phi monotonicity and sandwich.
            Proof: Phi' = 1-a-b<=0; JAC-FIBRE/FRONTIER-EXACT gives
            Phi(delta^0)=1 at proper frontiers and >1 at non-proper
            frontiers; RADIUS-ORDER with M_1=-m gives Phi(delta_1)=1.
            Therefore Phi is constant on [delta_1,delta^0] and D1 is a
            joint f*g star.
            Repair: proper frontier is equality, not merely >=1.

CONFIRMED   (2) Phi(delta_1)=1 is not a Def.5.1(3) artefact.
            Prop.5.3 gives the predecessor radius geometrically for r>=2;
            set r=2 for delta_1.  Four Keller controls verify the identity
            from the joint tree, outside NU-TWO scope.

CONFIRMED   (3a) A_bot is not a single skeleton function.
            Witness (x+y^5, y+(x+y^5)^3): resultant degree N=1;
            D1 contact classes are five conjugate discs of size a_1=3,
            so A_bot=15.  Scope: nu=1 control, not NU-TWO theorem.

CONFIRMED   (3b) EXACT-N window and integrality.
            N=sum_B a_1(B)c(B), c=d(1-delta_1)/(d+e);
            L=a_1 c<=N<=u e c=U; L/U=V_2/u.  Integrality is on the
            total packet, not on one branch unless SINGLE/(UNI) is assumed.

REFUTED     (3c) "max L=3.32 to D<=190".
            Correct: maxL=63/19 through D<=140; local D<=190 row table has
            maxL=165/31 at D=176.  No floor kill still follows since
            165/31<16.

CONFIRMED   (4) Counts.
            Fresh D<=100 run: groups 3975, U<6 kills 274, SINGLE 2499,
            MIXED 1121 with 847 cap hits, no emptied degree.
            D<=140 saved run: groups 18064, U<6 697, MIXED 5275 with
            4750 caps, SINGLE 11992, no emptied degree.
            D<=190 SINGLE row-sum: groups 76282, U<6 1288, SINGLE 49623,
            no emptied degree.
            D=105 reconciliation: exactn MIXED 159/264 is the no-hit count
            for N in [6,16] = 264-105.  GPT-5.5's 125 hits use the wider
            N>=6 variant; the difference is 20 groups with hits only above
            16.

CONFIRMED   (5) NO-RESIDUE.
            For any Puiseux h=sum c_a t^a, d/dx h=-sum a c_a t^(a+1),
            so [t^1] is zero even with fractional exponents.  For Keller
            pairs this forces [x^-1] 1/g_y(x,tau)=0 on every simple branch
            of every fibre of g.  Negative control y^2-x^2-x gives +-1/2
            and delta^0=1.  Not a numerical skeleton condition; it is a
            coefficient-level condition on g.

CONFIRMED   (6) Prop.4.6 r=1 plus A.5 forces squarefree bottom.
            Prop.4.6 prints only the nonzero operator at r=1.  After
            degree rescaling, Prop.A.5 applies and P_1 Q_1 is squarefree;
            part(P_1)=(1^(eV_2)).  Moh p.184 explicitly does this in the
            all-roots subcase.  STAR forced-repeat kills 0/9553 at D<=120.
            Promotion excludes global Keller realisability.

CONFIRMED   (7) D=105 row.
            Under STAR's campaign order:
            n=105,m=70,M=(-70,-63,103),V=(1,4,1),(d,e)=(2,3),(u,v)=(20,15),
            q=(1-delta_1)de/(d+e)=3/10, packet (1^20), N=6,
            bottom partition (1^3).
            Repair: per-root c=1/10; q=3/10 is per V_2 unit.

PROMOTE     Items 1,2,3a,3b,4,5,6,7 with repairs.
DO NOT      Promote item 3c's "3.32 to D<=190" numerical bound.
OPEN        BRANCH-PROFILE bounded by sum V_2<=u; MIXED-CAP-D<=140 has
            4750 groups; MIXED-141-190 has at most 58218 groups;
            NO-RESIDUE-CENSUS awaits coefficient/Puiseux-jet data;
            GLOBAL-REALISABILITY outside this lane.

FALLACY     No flag/place/series identification.  No floor/attainment
            upgrade.  A_bot witness is a nu=1 control.  No sat/remainder
            or variable-name ring-map claim.  No exit-price assertion.
```

<!-- BODY-END -->
