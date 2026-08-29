# Hostile review: `WEIGHT-AT-ATYPICAL` type-(2,3) analytic Keller surrogate

Reviewer: Fable 5 (independent adversarial review; different model from producer)  
Date: 2026-08-29 UTC  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Reviewed producer: `xmodel/weight-at-atypical-local-countermodel-sol56-20260829.md` (Sol 5.6)  
Lifecycle of this report: `HOSTILE REVIEW / SINGLE DELIVERABLE / NO LEDGER EDITS`

## 0. Verdict

**PASS_WITH_REPAIRS at the declared surrogate tier.** All eight mandated
attack items return `CONFIRMED`. Every displayed identity in the producer
body is exactly correct; I re-derived each one independently by hand and
replayed all of them in exact symbolic algebra. No mathematical error was
found. The required repairs (Section 4) are one display gap — the
proper-tube-conservation ingredient is asserted in the producer's Section 0
list but never demonstrated in the model; I verify it here with an exact
closed-form identity, so the gap is display-only, not content — plus two
scope-wording tightenings and one unverifiable external attribution. The
producer's own surrogate boundary is honest and repeatedly stated: this is
an analytic Keller surrogate, not a polynomial map; a local Milnor cycle is
not a certified global atypical value; the height-three data are a
comparison profile, not an actual Eggers--Wall realization. Nothing in this
review promotes any statement about actual polynomial Keller maps,
`WEIGHT-AT-ATYPICAL`, `PCB-EXCESS`, PCB, or JC2.

| item | subject | verdict |
|---|---|---|
| 1 | chart, `dx^dy=s ds^dt=df^dg`, branch, domain, original variables | CONFIRMED |
| 2 | residual `(t^2,t^3+t)`, ratio 2:3, self-intersection at `t=+-i` | CONFIRMED |
| 3 | Hessian, central fibre, two branches, Milnor number one, no global claim | CONFIRMED |
| 4 | fibre expansion and local `g`-degree two for every `t_0!=0`, incl. `+-i` | CONFIRMED |
| 5 | branch degrees `1+1` at `t_0=0`; `w_an=2`, `I_an=2` | CONFIRMED |
| 6 | `u=3, kappa^-=kappa^+=1, b^+=2` typed as comparison profile only | CONFIRMED |
| 7 | scope: pointwise-analytic dependency barrier only; overclaim scan | CONFIRMED (two sentences flagged, R2/R3) |
| 8 | unique value beyond older equality controls; max safe statement | CONFIRMED (positioning corrected; see 2.8 and Section 6) |

## 1. Custody and method

- Full-file SHA-256 recomputed:
  `84afec54eb1f915ccb474a60ff72b1145ae4ffa7997a329fa8076dcbf59ea479` —
  matches the assignment pin.
- Body SHA-256 recomputed on every byte through the producer's unique
  standalone BODY-END marker line including its terminating newline (8993 bytes,
  matching the seal's own byte count):
  `80b6fd58a0a141ec1a395c064c92bd2f7e206aa9eec9af15aea285aa69c6e350`,
  byte-identical (programmatic string comparison, not eyeball) to the
  producer seal's stated digest and to the assignment pin. The `BODY-END`
  marker occurs once standalone; its only other textual occurrence is
  inline inside the seal's body-definition sentence, so the seal's
  "unique standalone" clause holds.
- References consulted for definitions and scope only (not as oracles):
  `xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md`
  (the `K,n,e,kappa^-,m,kappa^+,b^+` formalism, Lemmas 3.1/3.2, (4.1)) and
  `xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md`
  (PASS on the amended repair; its Section 2 contains the older admitted
  chart and the moving-`Q`-value refutation of the multiplicity lemma).
  For item 8 positioning I also read the sibling
  `xmodel/pcb-generic-collision-surplus-sol56-20260829.md` (degree-six
  zero-excess controls, `QCS`/`QCS'` retyping) and the ideation-round
  statement of the bridge
  (`xmodel/ideation-20260829T1808Z-fable5.md`, "an atypical value carries
  at least one unit of Section-7 weight on some `U_i`").
- Execution disclosure: this session had a shell. All checks were
  desk-scale exact algebra: hand derivations replayed in sympy 1.14 in a
  scratch venv outside the repository. No Singular, no AWS, no web, no
  writes other than this file, `jc2-lean` untouched.
- The producer is treated adversarially throughout: every equation below
  was derived before comparing with the producer's display.

## 2. Item-by-item findings

### 2.1 Chart and exact Jacobian identity — CONFIRMED

With `x=t s^3`, `y=s^(-1)`: `x_s y_t - x_t y_s = 0 - s^3(-s^(-2)) = s`, so
`dx^dy = s ds^dt` exactly. With `R=sqrt(1+3s^2/2)`, `A=(2/3)(R-1)`,
`f=t^2+A`, `g=t^3+tR`: `R'=3s/(2R)`, `A'=s/R`, and

```text
f_s g_t - f_t g_s = (s/R)(3t^2+R) - 2t(3st/(2R)) = sR/R = s,
```

replayed symbolically to `s` on the nose. So (1.2) is exact wherever `R` is
defined: `dx^dy = s ds^dt = df^dg`.

Branch and domain: the zeros of `1+3s^2/2` are `s=+-i sqrt(2/3)`. On
`|s|<sqrt(2/3)` the value `1+3s^2/2` lies in the open disc of radius 1
about 1, hence in the right half-plane, so the principal square root with
`R(0)=+1` is holomorphic there; any `rho<sqrt(2/3)` as chosen by the
producer is strictly safe (the natural maximal disc is `|s|<sqrt(2/3)`
itself — a cosmetic strengthening only). The domain is a fixed `s`-disc
times all of `A1_t`, i.e. genuinely uniform in `t`: `f,g` are polynomial in
`t` with coefficients holomorphic on the disc. The branch normalization
`R(0)=+1` is load-bearing (it gives `A(0)=0`, hence `f(0,0)=0` and the
residual `+t` term in `g`); the producer uses it consistently.

Original variables: `s^2=y^(-2)` gives `R=sqrt(1+3/(2y^2))`,
`f=x^2y^6+(2/3)(R-1)`, `g=x^3y^9+xy^3R`, valid on `|y|>1/rho` with the same
branch (`|3/(2y^2)|<1` there, so the principal branch matches). `R` is
algebraic of degree 2 over `C(y)` and not rational: `R^2=(2y^2+3)/(2y^2)`
and `2y^2+3` is squarefree of degree 2, not a square in `C(y)`; if `f` were
rational then `R=(3/2)(f-x^2y^6)+1` would be rational. So "algebraic and
analytic near this boundary component, but not a polynomial pair (nor a
rational pair)" is exactly right. The coordinate change itself is the one
admitted in the Terra hostile review (its Section 2 uses the identical
`s=y^(-1), t=xy^3` chart), so "already admitted by the hostile-reviewed
Section-7 proper-tube control" is accurate for the chart; the pair `(f,g)`
is new, and the producer correctly says the differential identity (1.2),
not the chart, is the evidence.

### 2.2 Residual map, ratio, self-intersection — CONFIRMED

At `s=0`: `R=1`, `A=0`, so `(f,g)(0,t)=(t^2,t^3+t)`, i.e. `(P,Q)=(z^2,z^3+z)`
with `deg P:deg Q = 2:3` as claimed. Self-intersections: `P(t_1)=P(t_2)`,
`t_1!=t_2` forces `t_2=-t_1`; then `Q(t_1)=Q(-t_1)` forces `t_1(t_1^2+1)=0`,
so `{t_1,t_2}={i,-i}` (the symbolic solve returns exactly the diagonal, the
zero pair, and `(i,-i)`, `(-i,i)`). Image point `(P,Q)=(-1,0)`. The image
curve is exactly `Q^2=P(P+1)^2` (replayed to 0), the nodal cubic with an
ordinary node at `(-1,0)`: tangent vectors `phi'(i)=(2i,-2)`,
`phi'(-i)=(-2i,-2)` have determinant `-8i != 0`, so the two local branches
are transverse and the parametrization `t -> (t^2,t^3+t)` is an
immersion (`phi'` never vanishes) and injective away from `{+-i}`; it is
the normalization of the nodal cubic. "Finite self-intersection ... does
not merge the two source parameters" is exactly correct: `t=i` and `t=-i`
remain two distinct points of the source parameter line, two distinct
singleton direction clusters (the deck orbit is trivial, `m=1`), whose
values happen to collide in the target. That is the correct Section-7
typing: clusters and weights live on the source quotient line, and only the
pushforward adds masses over a common target point (here the pushforward
mass over `(-1,0)` would be `2+2=4`; the producer claims nothing about it,
correctly).

### 2.3 Morse point, central fibre, Milnor number — CONFIRMED

`f_s=s/R`, `f_t=2t` vanish at `(0,0)` and nowhere else in the chart with
`s!=0` — so the affine Keller identity is uncontradicted, and the
producer's remark that the pulled-back area form itself carries the factor
`s` on the removed boundary is the right explanation. At the origin,
`f_ss=1, f_st=0, f_tt=2` (replayed): `Hess=diag(1,2)`, nondegenerate, and
`f(0,0)=0`. A nondegenerate critical point with critical value 0 gives an
ordinary node on the central fibre and local Milnor number one; the nearby
fibre is the Milnor smoothing with one vanishing cycle. The explicit fibre
equation checks exactly: on the branch, `f=0` iff `R=1-(3/2)t^2`, and
squaring gives `s^2=(2/3)(R^2-1)=-2t^2+(3/2)t^4=-2t^2(1-3t^2/4)`, the
producer's (2.1); near the origin the resquaring is reversible because both
`R` and `1-(3/2)t^2` are near `+1`, which is the producer's stated branch
caveat. Two normalized branches `s=+-i sqrt(2) t(1-(3/8)t^2+...)` with
distinct tangents. No global polynomial atypicality is claimed anywhere:
Section 2 closes with the explicit disclaimer, and Section 0 lists the
non-claims. CONFIRMED.

### 2.4 Every `t_0!=0`: local `g`-degree two, including `t_0=+-i` — CONFIRMED

Independent derivation. Fix `t_0!=0`, `a=t_0^2`. On `f=a`, solve
`t=t_0 sqrt(1-A(s)/t_0^2)` (germ with `t(0)=t_0`; well defined since
`A(0)=0`). With `A(s)=s^2/2-(3/16)s^4+O(s^6)` (replayed),

```text
t-t_0 = -s^2/(4t_0)+O(s^4),
R     = 1+(3/4)s^2+O(s^4),
g-(t_0^3+t_0) = (3t_0^2+1)(t-t_0)+(3/4)t_0 s^2+O(s^4)
              = s^2[-(3t_0^2+1)/(4t_0)+(3/4)t_0]+O(s^4)
              = -s^2/(4t_0)+O(s^4),
```

all three lines replayed symbolically and equal to the producer's (3.2).
The leading coefficient `-1/(4t_0)` is nonzero for **every** finite
`t_0!=0`, in particular at `t_0=+-i` where it is `+-i/4`. Since the fibre
is a smooth graph over `s` near the puncture, `s` is a uniformizer and the
local `g`-degree is exactly two, for every direction, including the two
value-colliding directions. At `t_0=+-i` the two punctures sit at
`t`-distance 2 apart, have disjoint tubes, and share the value pair
`(a,b)=(-1,0)`; they are two distinct singleton clusters of degree two each
— consistent with 2.2 and with the Section-7 source-side cluster
definition (clusters are indexed by the coefficient direction, not by the
value pair). I also checked the two source-line ramification loci that a
careless reader might conflate: at `z=+-i/sqrt(3)` (where `Q'=3z^2+1=0`)
and at `z=+-i` (value collision) nothing happens to the fibre-side
`g`-degree — `w_an` measures `ord_s` of `g` on the fibre branch, not
`ord_z` of `Q` on the parameter line, and the producer never conflates
them. CONFIRMED, and cross-checked against the exact tube identity in
Section 3 below (which reproduces `g(puncture)=+-sqrt(a)(a+1)=Q(+-sqrt(a))`
and the same leading term).

### 2.5 `t_0=0`: branch degrees `1+1`, `w_an=2`, `I_an=2` — CONFIRMED

On the central fibre `R=1-(3/2)t^2` exactly, so

```text
g = t^3+tR = t^3+t-(3/2)t^3 = t-(1/2)t^3
```

**exactly** (not merely to leading order; replayed). Each of the two
normalized branches of (2.1) is parametrized by `t` (since
`s=+-i sqrt(2) t(1-(3/4)t^2)^(1/2)` is analytic in `t` and the branch is
smooth), so `t` is a uniformizer and `g` has a simple zero: local degree
one on each branch. The two branches share the single coefficient
direction `z=0` (both have `t->0` at the puncture `(s,t)=(0,0)`, and the
full fibre `t=+-sqrt(-A(s))` has no other boundary point), so they form one
analytic direction cluster of weight `1+1=2=b^+`, the producer's (3.4).
Fibres are bounded in `t` over the `s`-disc (`|t|^2<=|a|+|A|_max`), so
there are no other ends at `s=0` for any fibre: for `a!=0` the punctures
are exactly `t=+-sqrt(a)`, each a singleton of weight 2 by 2.4. Hence
`w_an(z)=2` for all `z in A1`, constant, trivially constructible, and

```text
I_an = integral_(A1) w_an dchi_c = 2*chi_c(A1) = 2 = kappa^+(u-1) = b^+,
```

so `I_an-b^+=0`, the producer's (3.5)-(3.6). This is exactly the equality
case of the reviewed repair's (4.1) with `S={0}` (`P'(z)=2z`), i.e.
`b^+(1-#S)+w(0)=0+2=2`: the surrogate saturates the PASSed inequality and
therefore contradicts nothing that was promoted — it only blocks a
*strict* strengthening from these local inputs. CONFIRMED.

### 2.6 Height-three data typed as comparison profile — CONFIRMED

Reading the chart through the repair file's Section 2: the Puiseux
presentation at this boundary flag has integer exponents (`K=1`), height
`u=3` (`x ~ z y^(-3)+...`; on fibre `a`, the branch at direction `t_0` is
`x=t_0y^(-3)-y^(-5)/(4t_0)+...`), an empty strict prefix below height 3, so
`e=gcd(K,{})=K=1`, `kappa^-=K/e=1`, `m=e/gcd(e,n)=1` with `n=Ku=3`
("coefficient quotient is unramified"), `kappa^+=K/gcd(e,n)=1`, and
`b^+=kappa^+(u-1)=2`. These match (3.1) and are the same values the Terra
review assigned to the identically shaped older chart. The typing
discipline is correct and explicit: the producer calls them "formal
comparison data," names the profile `w_an` "deliberate[ly]," and states
that without polynomial-origin Eggers--Wall/tree realization no actual
Section-7 pushforward weight is asserted. What is genuinely realized at
branch level is the local Puiseux shape (including the correct
zero-coefficient behaviour at the collision direction: on the central
fibre the branches have first nonzero coefficient at height 4, exactly the
`z=0`/zero-coefficient case of the reviewed formalism, with no `kappa`
jump since `m=1`). What is not realized — packet-level EW tree, source-
complete quotient bijection, `d-N` pushforward — is exactly what the
producer disclaims. CONFIRMED: comparison profile, not an actual
Eggers--Wall realization, and the body says so.

### 2.7 Scope and overclaim scan — CONFIRMED with two flags

What the report proves, exactly: there exists an analytic local boundary
interface carrying all of the listed pointwise ingredients — exact
Jacobian-one boundary chart, the same cluster/local-degree rule, proper-
tube conservation (verified in Section 3 below), a boundary collision, one
local Milnor cycle with its Picard--Lefschetz monodromy, and the
normalized 2:3 residual type — on which the analytic-profile analogue of
`EXCESS-1` fails (`w_an=b^+` pointwise and `I_an-b^+=0`). Therefore no
proof of the bridge can be assembled solely from steps that remain valid
for analytic germs at a single boundary flag; any valid proof must consume
actual-map provenance or a global/multi-component identity. That is a
standard dependency-faithful countermodel, the same genre the Terra review
already used, and the producer's Sections 0, 2, 3, 4, 5 state the
non-claims correctly and repeatedly (not a polynomial pair, no quotient
bijection, no `d-N` pushforward, no refutation of `WEIGHT-AT-ATYPICAL` /
`PCB-EXCESS` / PCB / JC2, no certified global atypical value). The
Section 4 not-ruled-out list is complete and honest (global Euler package,
polynomial-origin rationality, simultaneous all-component behaviour,
algebraic compactification identity, new signed invariant), and the
Section 5 ledger keeps every actual-map statement `open`. The producer
also satisfies the ideation-round firewall (no flag/place/series
identification anywhere).

Flags (both wording, neither verdict-changing):

- **F1 (Section 0):** "any proof must use something beyond the listed
  pointwise analytic data" — as written this slightly outruns the
  construction, which blocks only arguments whose steps are valid for
  analytic germs **at a single boundary interface**; Section 4 itself
  correctly lists "simultaneous behaviour at every boundary component" as
  not ruled out. Align Section 0 with Section 4 (repair R2).
- **F2 (Section 5):** "it shows exactly which pointwise argument is
  insufficient" — plural: Section 4 rules out three mechanisms (Morse
  geometry alone, Milnor-cycle injection, profile-level budget transfer)
  (repair R3).

One further sentence was attacked and survives: the Section 0 ingredient
list includes "proper-tube conservation used in Section 7," which the body
never demonstrates in the model. If conservation had failed in the
surrogate, the list would overclaim and this item would be `GAP`. It holds
(Section 3), so the sentence is true but undisplayed: repair R1.

### 2.8 Unique value and maximum safe statement — CONFIRMED (positioning corrected)

The relevant older zero-excess Jacobian-one controls are (i) the Terra
review Section 2 chart (`u=3`, `f=t^2+s^2/2`, `g=t`, residual
`(z^2,z)`, node collision `1+1=2=b^+`) and (ii) the sibling QCS degree-six
chart (`u=6`, `f=t^2+s^5/5`, `g=t`, residual `(z^2,z)`, unibranch cusp
collision of weight `5=b`, whole-line profile `I-b=0`). Correction to the
framing in this assignment and implicitly in the producer's pitch: being
*globally in `t`* is **not** new — both older controls are also defined
for all `t`, and are even polynomial in `(s,t)`. What is genuinely unique
here:

1. **First control with residual `Q`-degree > 1**, giving the normalized
   type `2:3` on the whole parameter line — the U1-relevant ratio — with a
   genuinely nonlinear `g`-side (moving `Q`-ramification at
   `z=+-i/sqrt(3)`, checked inert in 2.4).
2. **First control with a finite target-curve self-intersection**
   (`t=+-i` over `(-1,0)`): two source clusters with equal value pairs and
   unmerged source parameters, exercising the source-quotient/target-
   pushforward distinction inside a countermodel for the first time.
3. **First control framed at minimal degeneracy**: a nondegenerate
   (Morse, `mu=1`) boundary point — the older QCS cusp has `mu=4` but was
   never framed against the Milnor-cycle mechanism; here the Milnor-cycle
   injection and Morse-implies-excess mechanisms are named and refuted at
   the mildest possible singularity, which is the sharpest direction for a
   negative control.
4. The price of 1-3 is the square-root branch: unlike both older
   controls, this pair is non-polynomial even in the chart variables, and
   Section 3 below proves the price is unavoidable in the natural ansatz —
   which converts a cosmetic weakness into a named discriminator for the
   successor gate.

The whole-line constant profile with `I_an-b^+=0` is shared with QCS 4.1
and is not by itself new. The maximum exact statement safe to retain is
given in Section 6. CONFIRMED that the example adds unique value (points
1-3, plus the forced-branch lemma), with the "globally-in-`t`" claim
demoted as above.

## 3. Additional adversarial checks (new exact content)

### 3.1 Proper-tube conservation holds exactly (closes the R1 gap)

On any fibre `f=a`: `t^2=a-A(s)` and `g=t(t^2+R)=t(a-A+R)`. Since
`A=(2/3)(R-1)` gives `-A+R=(R+2)/3` (replayed to 0),

```text
g = t*h_a(s),        h_a(s) = a+(R(s)+2)/3,   h_a(0)=a+1,
```

and `h_a` is nonvanishing on a small disc for `a` near 0. So
`(s,t)->(s,g)` is an `s`-preserving isomorphism of the fibre germ onto
`{g^2=Phi_a(s)}` with `Phi_a=(a-A)h_a^2`, and — the key exact identity,
replayed symbolically —

```text
Phi_a'(s) = -s*h_a(s),      Phi_a(0)=a(a+1)^2,      Phi_a''(0)=-(a+1).
```

Consequences, all exact:

- For every small `a`, generic `b` near 0 has `Phi_a(s)=b^2` with exactly
  two roots `s` in the tube, each carrying one point with `g=+b`: the
  proper `g`-tube degree is **2, constant in `a`** — conservation holds,
  with `a=0` giving the two node branches of degree `1+1`.
- For `a!=0`, the only critical points of `g` on the fibre in the tube are
  at `s=0` (since `Phi_a'=-sh_a` and, at the `s`-projection branch points
  `Phi_a(s_0)=0`, `s_0!=0` makes `g` a uniformizer): the two punctures,
  each of index 2 over the **distinct moving values**
  `+-sqrt(a)(a+1)=Q(+-sqrt(a))` — reproducing (3.2)'s leading term
  `-s^2/(4t_0)` from `Phi_a` independently.
- The deleted multiplicity-strengthened Lemma 3.2 fails here exactly as in
  the Terra chart: `mult_0(P-P(0))*b^+=4>2=w_an(0)`; the amended one-point
  bound holds with equality, `2>=2`.

So the Section 0 ingredient "proper-tube conservation" is genuinely
instantiated; the producer must display this (repair R1).

### 3.2 The square-root branch is forced: the surrogate boundary is structural

In the ansatz `f=t^2+a(s)`, `g=t^3+t*r(s)`, the identity
`f_s g_t-f_t g_s=s` decomposes by `t`-degree into `3a'(s)=2r'(s)` (the
`t^2` coefficient) and `a'(s)r(s)=s` (the constant), hence
`(2/3)r r'=s`, i.e. `(r^2)'=3s` and

```text
r(s)^2 = r(0)^2+(3/2)s^2      (dsolve replay: r=+-sqrt(C+6s^2)/2).
```

Prescribing the residual `(z^2,z^3+z)` forces `r(0)=1`, so
`r^2=1+3s^2/2`: the producer's `R`, uniquely, and `1+3s^2/2` is squarefree
of degree 2, so `r` is not in `C(s)`. Prescribing rationality instead
forces `r(0)^2` such that `r(0)^2+(3/2)s^2` is a square in `C(s)`, i.e.
`r(0)=0`, which destroys the `+t` term (residual `(z^2,z^3)`, no node) and
makes `a(s)` linear, destroying the Morse point. Within this ansatz there
is **no** rational/polynomial Keller chart with this residual: the
analytic surrogate is not lazily non-polynomial; the single-valued
rational origin of the boundary data is provably the exact constraint the
countermodel violates. This names the discriminator for the Section 5
successor gate.

### 3.3 Consistency with the promoted perimeter

The surrogate contradicts no promoted statement: it saturates repaired
Lemma 3.1 (generic equality), amended Lemma 3.2 (`>=` with equality), and
the repair's (4.1) (equality case), and it instantiates the moving-value
phenomenon that justified deleting the multiplicity factor. The bridge it
targets is the one stated in the ideation round ("an atypical value
carries at least one unit of Section-7 weight on some `U_i`"), read at the
excess typing that the sibling QCS file established as the correct one;
the producer's inline paraphrase is fair.

## 4. Required repairs

- **R1 (required, content display).** Add the exact tube-conservation
  computation of Section 3.1 (`g=t*h_a(s)`, `Phi_a=(a-A)h_a^2`,
  `Phi_a'=-s*h_a`, constant tube degree 2, two index-2 points over
  `+-sqrt(a)(a+1)`). Without it, the Section 0 claim that "proper-tube
  conservation used in Section 7" is among the instantiated ingredients is
  asserted but not demonstrated; with it, the ingredient list is fully
  displayed. Verified true here, so display-only.
- **R2 (required, wording).** Section 0: scope "any proof must use
  something beyond the listed pointwise analytic data" to "...beyond the
  listed pointwise analytic data at a single boundary interface," aligning
  with the Section 4 not-ruled-out list.
- **R3 (minor, wording).** Section 5: "which pointwise argument is
  insufficient" -> "which pointwise arguments are insufficient" (three
  mechanisms are refuted in Section 4).
- **R4 (minor, typing).** "Chau-compatible degree ratio" is an external
  attribution not verifiable at this desk (no web access; no pinned
  internal source found). Either pin an internal file fixing the
  U1-normalized `2:3` type or mark the attribution informal.
- **R5 (optional, strengthening).** Add the forced-branch lemma of
  Section 3.2 (`r^2=r(0)^2+(3/2)s^2`; residual `(z^2,z^3+z)` forces
  `r^2=1+3s^2/2`, irrational), upgrading the surrogate boundary from a
  disclaimer to a theorem and naming the successor discriminator.

## 5. Cheapest useful successor

A short sealed addendum (desk-only, no CAS beyond replayable exact
algebra, any model): apply R1-R4 and fold in R5. Deliverable: the same
countermodel with the tube-conservation identity and the forced-branch
lemma displayed, and the Section 5 gate restated as: *prove
`WEIGHT-AT-ATYPICAL` (or the correctly retyped `QCS`/`QCS'` quotient-
collision surplus of the sibling file, which is the form the campaign
should actually target) by essential use of single-valued
rational/polynomial origin of the boundary data — the exact hypothesis
this countermodel provably cannot satisfy (`r^2=1+3s^2/2` is not in
`C(s)`) — or of a simultaneous multi-component/global filling identity.*
That is the cheapest step that converts this negative control into a
positive constraint on the prove lane. The expensive successor (an actual
polynomial-origin strictness theorem at a quotient collision) is correctly
left open and should not be attempted as a repair of this file.

## 6. Maximum exact statement safe to retain

> There is a holomorphic pair `f=t^2+(2/3)(R-1)`, `g=t^3+tR`,
> `R=sqrt(1+3s^2/2)`, on `A1_t x {|s|<sqrt(2/3)}` — algebraic of degree 2
> over `C(x,y)` under `x=ts^3, y=s^(-1)`, neither polynomial nor rational
> on the affine plane — with `df^dg=dx^dy=s ds^dt` exactly; residual
> boundary map `(P,Q)=(z^2,z^3+z)` of normalized type `2:3` on the whole
> parameter line, whose value curve `Q^2=P(P+1)^2` has one ordinary node
> at `(-1,0)` with unmerged source parameters `z=+-i`; a boundary Morse
> point of `f` at the origin (Milnor number one) whose central fibre is a
> node with `g`-branch degrees `1+1`; every direction `z!=0` (including
> `z=+-i`) a singleton cluster of local `g`-degree two; constant analytic
> profile `w_an=2=b^+=kappa^+(u-1)` for the formal comparison data
> `(u,kappa^-,kappa^+)=(3,1,1)`; profile integral `I_an=2=b^+`; and
> conserved proper `g`-tube degree 2 at the collision, with the two nearby
> index-2 points lying over the distinct moving values `+-sqrt(a)(a+1)`.
> Consequently no proof of `WEIGHT-AT-ATYPICAL` can consist solely of
> steps valid for analytic germs at a single boundary flag — exact local
> Jacobian-one geometry, the cluster/local-degree rule, proper-tube
> conservation, a boundary collision, a local Milnor cycle with its
> monodromy, and the `2:3` residual type are jointly insufficient for even
> one unit of profile excess; any valid proof must essentially consume
> single-valued rational/polynomial origin of the boundary data (provably
> violated here: in the ansatz `f=t^2+a(s)`, `g=t^3+t r(s)`, Jacobian one
> forces `r^2=r(0)^2+3s^2/2`, and the residual `(z^2,z^3+z)` forces
> `r^2=1+3s^2/2`, not rational) or a global/multi-component identity.
> Nothing is decided about actual polynomial Keller maps, actual
> Eggers--Wall packets, actual atypical values, `WEIGHT-AT-ATYPICAL`,
> `PCB-EXCESS`, PCB, or JC2.

## 7. FALLACY-v2 conformance

Checked against the guardrail: no cv-flag/place/series identification is
made by producer or review (the producer's branch/cluster/parameter
separation is explicit and verified); no exit-set charge is asserted or
consumed, so no `charge_basis` line is declared; floors and attainment are
kept distinct (the surrogate saturates the promoted `>=` statements with
equality and claims no strictness anywhere); no cap-or-analogy fill is
used — the one undisplayed ingredient was closed by exact computation, not
assumption. Verdict unchanged: **PASS_WITH_REPAIRS** at the declared
exact-local-analytic-surrogate tier, with repairs R1-R4 required before
any consumer cites the Section 0 ingredient list verbatim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26796`.
- Body SHA-256:
  `cf1ba18a699de9f9107b86ec8fe253e867f762a52e6c8f821832683efd460011`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
