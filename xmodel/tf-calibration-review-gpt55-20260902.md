# Hostile review: TIME-FUNCTION CALIBRATION D = 48

Reviewer: gpt-5.5. Date: 2026-09-02. Lane: hostile review of
`xmodel/time-function-calibration-d48-opus5-20260902.md`.

## 0. Custody and method

Frozen inputs in `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.0qqcjz/inputs`
were hashed with `shasum -a 256` before use. All six matched the charge:

```text
db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a  time-function-calibration-d48-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  d1-subtree-review-grok46-20260902.md
437c5b45facf61e8e24d5399da50d131310b360f8184667a25c7388c6941c09e  bottom_star.py
a84e7e92b7a17c85fb96ce3fc784bdc15952583cf4ce892a2ded2838ad7bf3dc  kernel_L.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  moh_skeleton_N.py
```

Also checked: workspace `box/moh_skeleton_N.py` and
`box/tfcal-drivers-20260902/moh_skeleton_N.py` have the same SHA-256
`3022020435...`; `d1floor.py` is `cf0780cc...`; `general.py` is
`e7d7d2e...`.

Moh page images read directly: `refs/moh1983_jram340_configurations_of_roots.pdf`,
journal p.200 and p.201 rendered at 300 dpi with `pdftoppm` (PDF pages 61 and
62). I used `box/depth-drivers-20260902/moh.txt` only as a locator/OCR aid, not
as the source of the damaged formulas.

Reruns, summarized:

```text
kernel_L.py                  PASS; generic nullity 3; candidates -1,0,1,2,3,4
tfcal.py                     PASS; 37 checks, 0 failures
star_explicit.py             PASS; explicit (2,3), V=1,2 witnesses
d48final.py                  PASS; D=48 funnel and six Moh rows
sweep.py 48 48 6 16          PASS; D=48 1301/50 -> 33/12 -> 0/0
sweep.py 105 105 6 16        PASS; D=105 5037/264 -> 148/38 -> 8/8 -> 3
sweep.py 48 120 6 16         PASS; totals reproduced
bottom_star.py               interrupted in V=3 after V=1,V=2 output; see item 6
```

No ledger edit. No `jc2-lean`. No exit-price assertion; no `charge_basis` line.

## 1. Executive verdicts

| Item | Verdict | Line evidence | Repair / promotion |
|---|---|---:|---|
| Omission by `moh_skeleton_N.py`, `d1floor.py`, `general.py` | CONFIRMED for (8)-(11), also (12)-(13). The enumerator implements the numerical skeleton and Def. 5.1(2) windows, not Moh's root-of-unity filters. | `moh_skeleton_N.py:146-170,207-211,277-323`; `d1floor.py:39-52,195-245,264-361`; `general.py:10-40` | Promote the omission. Repair wording: the code encodes necessary numerical consequences of search (1)-(7), not the actual Jacobian/minimality test in printed (3). |
| Moh p.201 reading | GAP in the charged notation. The scan does not print the report's symbols verbatim. It prints denominator increment `A_{r-1}`, quotient `Delta_{r-1}`, and remainder in (9); then `V_{r-1} <= Delta_{r-1}` in (10). | p.201 scan; OCR locator `moh.txt:3286-3299`; `mohcond.py:2-9,22-32` | Rename the denominator increment `A_j`. State reconstructed (10) as algebraically equivalent to Moh's nonzero branch after eliminating the quotient, not as a verbatim transcription. Not promotable until census-rebase finishes. |
| `(10)_1` | CONFIRMED as a necessary bottom-star congruence and as a corollary of Moh's printed final alternatives (12)-(13). GAP if advertised as "Moh prints exactly this". | p.201 scan; `mohcond.py:72-81`; `d48final.py:11-22` | Promote `a_1=eV_2 == 0 or 1 mod A_1` as a proved necessary condition. Repair: call it `(10)_1 corollary`; record that p.201 prints the stronger paired divisibilities (12)/(13). |
| Reconstructed `(10)` for `j>=2` | GAP / NOT PROMOTABLE. It is plausible and calibrated, but it drops Moh's printed alpha-zero alternative (11). | p.201 scan; charged report `time-function...:409-423`; `mohcond.py:28-33` | Keep as `RECONSTRUCTED[nonzero-branch]`. Do not promote counts depending on it as exact Moh census counts until census-rebase lands. |
| TF-0 | CONFIRMED. `d Q P' - e Q' P = gamma != 0` forces simple roots for both `P=p_g` and `Q=p_f`, and `gcd(P,Q)=1`. | charged `time-function...:189-207`; `tfcal.py:114-124` | Promote. This repairs D1-SUBTREE's "intra-f clustering is free": invisible to `N` is true; free is false at the leading bottom star. |
| TF-DESSIN passport | CONFIRMED. The passport and Riemann-Hurwitz genus-zero check are correct. | charged `time-function...:212-220`; `star_explicit.py:17-25` | Promote the passport. |
| TF-DESSIN existence for every `(d,e,V)` | GAP. The cubic map construction proves the `(d,e)=(2,3)` case after contracting degree-2 vertices; it is not a construction for arbitrary `d,e`. | charged `time-function...:222-226`; `star_explicit.py:26-29` | Promote only `(2,3), V=1,2` explicit witnesses and the `(2,3)` cubic-tree construction in principle. Add `OPEN[DESSIN-GENERAL]`. |
| "cubic plane map" description | CONFIRMED only for `(d,e)=(2,3)`. | charged `time-function...:222-226` | Repair: say "for `(d,e)=(2,3)`, after contracting the degree-2 color." |
| TF-NOTAME | GAP as a global theorem; CONFIRMED for the V=1 bottom form tested. | charged `time-function...:326-336`; `tfcal.py:146-157` | Promote only with exact scope: tame-silent subspace, `V=1` machine check, and `nu != 1-delta_1`. General `V` proof remains open. |
| TF-EXH | CONFIRMED conditional on TF-NOTAME and exhaustion. | charged `time-function...:354-360`; `tfcal.py:159-169` | Promote the identity and conditional corollary, not an unconditional census filter. |
| D=48 selected skeleton | CONFIRMED killed by `(10)_1`; also killed by reconstructed level-2 (10). | direct rerun; `d48final.py:24-57` | Repair: do not imply `(10)_1` is the unique death cause once reconstructed (10) is imposed. |
| D<=120 rebased counts | CONFIRMED as counts for `(10)` nonzero-branch reconstruction plus `(10)_1` plus knapsack. | live `sweep.py 48 120 6 16`; saved `sweep48-120.log:1-30` | Promote as measured under the reconstructed filter, with the reconstruction caveat. |
| D=105 survivors | CONFIRMED. The three charged groups are exactly the knapsack-alive groups after reconstructed `(10)+(10)_1`. They also survive `(10)_1` alone. | live `sweep.py 105 105`; `survivors.log:39-42` | Promote. |
| Six Moh rows | CONFIRMED for `(10)_1`, reconstructed `(10)`, and printed bottom alternatives (12)/(13). Two reconstructed `(10)` rows are equality: `(64,48)` and `(99,66)`. | `mohcond.py` rerun; `d48final.py:11-22` | Promote only after saying reconstructed `(10)` is not verbatim and is not final census law. |

## 2. What Moh p.201 actually prints

The p.201 scan is readable enough for the disputed symbols.

Moh's condition (8): for the increment of the denominator of `delta_{r-1}`
with respect to `delta_s,...,delta_r`, let `L` be the l.c.m. of the reduced
denominators of `delta_s,...,delta_r`; then `A_{r-1}` is the reduced
denominator of `L delta_{r-1}`.

Moh's division (9) is:

```text
V_r (d_{r-1}/d_r) = Delta_{r-1} A_{r-1} + box_{r-1}.
```

Thus Moh's `Delta_{r-1}` is the quotient, not the denominator increment. The
charged report uses `Delta_j` for Moh's `A_j`; that notation must be repaired.

Moh's printed nonzero-factor condition (10) is:

```text
V_{r-1} <= Delta_{r-1}
```

where `Delta_{r-1}` is the quotient above, for a corresponding factor
`pi - alpha`, `alpha != 0`. Eliminating the quotient gives the charged
inequality

```text
A_j V_j <= V_{j+1} d_j/d_{j+1}
```

for the nonzero branch, because all terms are integral and
`V_j <= floor((V_{j+1}d_j/d_{j+1})/A_j)` iff `A_j V_j <= V_{j+1}d_j/d_{j+1}`.
So the reconstruction is plausible, but it is not what Moh prints verbatim and
it omits (11).

Moh's printed alpha-zero condition (11) is visible as:

```text
V_{r-1} = j A_{r-1} + box_{r-1}
```

with the exact range/role of `j` not recovered here. This is enough to keep the
level-`j>=2` reconstruction non-promotable.

Finally, p.201 prints separate final `r=2` alternatives:

```text
(12)  A_1 | (n/d_2) V_2,      A_1 | (m/d_2) V_2 - 1,
or
(13)  A_1 | (m/d_2) V_2,      A_1 | (n/d_2) V_2 - 1.
```

These imply the charged bottom congruence

```text
a_1 = (n/d_2)V_2 = eV_2 == 0 or 1 mod A_1.
```

On the enumerated `D<=120` census, the converse also held: 902,893 assignments,
zero differences between `star_congruence(S)` and the printed (12)/(13) test.

## 3. Omission audit, function by function

`box/moh_skeleton_N.py` is the campaign enumerator. It does not import
`mohcond`, does not define denominator increments `A_j`, and has no
root-of-unity orbit/divisibility test.

Function map:

```text
controls_pairing()        lines 103-142   CONTACT-DEFICIENCY/FRONTIER controls; no Moh (8)-(13).
Skel.__init__()           lines 146-164   M_1=-m, M_s from input, d-chain, V_{s+1}, a_i,b_i,u,v.
Skel._delta()             lines 165-170   Def. 5.1(3) radii.
lam_g/closed/radius       lines 172-195   Lemma 5.2/order identities.
N_upper/N_upper_closed    lines 197-205   derived ceiling U.
windows_ok()              lines 207-211   Def. 5.1(2) / search window (7).
top_of_window/U_robust    lines 213-233   branch-robust maximum over window data; no Moh (8)-(13).
MOH_SURVIVORS             lines 235-242   calibration rows only.
census()                  lines 277-323   enumerates n,m,M,V satisfying numerical skeleton/window constraints.
controls_census()         lines 325-342   calibrates counts and row inclusion.
controls_rejection()      lines 350-392   leading-form and small-K rejection controls; no root-of-unity filters.
run_filter/fast_filter    lines 397-536   U-bound filters only.
main()                    lines 538-556   runs controls and filters; no Moh (8)-(13).
```

Detailed condition map for `census()`:

```text
search (1):  m=-M_1<n      encoded by K loop and dd in 2..e-1, lines 288-300.
search (2):  m does not divide n, M_s=n-2
             m does not divide n follows from gcd(dd,e)=1 and dd>=2, lines 297-299;
             M_s=n-2 is appended/assigned, lines 293 and 300.
search (3):  Jacobian condition and no simultaneous degree reduction
             not tested as an equation; only necessary campaign consequences are used.
search (4):  characteristic data below n-2
             encoded as increasing M chain and gcd constraints, lines 292-308.
search (5):  d_r=gcd(n,M_1,...,M_{r-1})
             encoded by the divisor chain and gcd filter, lines 292-307.
search (6):  3<=s<=5, d_s>=4
             d_s>=4 by divisor_chains floor=4, lines 270-275;
             s>=3 by requiring a nonempty chain; s<=5 is not explicit, but holds on D<=120 by size.
search (7):  V-window
             encoded exactly as lo< V_i <= hi, lines 312-320; plus V_s<d_s, line 319.
search (8):  denominator increment A_j
             omitted.
search (9):  division by A_j into quotient/remainder
             omitted.
search (10): nonzero-factor bound
             omitted.
search (11): alpha-zero alternative
             omitted.
search (12),(13): final r=2 bottom divisibility alternatives
             omitted.
```

`box/tfcal-drivers-20260902/d1floor.py` imports `Skel,census` at line 29 and
then derives `q`, floor/ceiling, and integrality/knapsack filters. It has no
`Delta`, no denominator-increment function, no root-of-unity action, and no
(8)-(13) gate. Relevant lines: `qval/qprod` at 39-49, `floor_r/ceil_r` at
51-52, two-sided floor/ceiling filter at 195-245, `(UNI)` integrality at
264-315, and hypothesis-free knapsack at 317-361.

`box/tfcal-drivers-20260902/general.py` is only the hypothesis-free knapsack:
it imports `Skel,census,qval` at lines 5-8 and searches sums
`N=sum V_2 q` at lines 10-40. It also has no (8)-(13) gate.

Verdict: confirmed. Repair by adding a separate `A_j`-named Moh-condition
layer; keep the reconstructed nonzero branch typed until (11) is recovered.

## 4. `(10)_1`: proof and normalization

Use `A_1` for the reduced denominator of `L_1 delta_1`, where
`L_1=lcm(den(delta_s),...,den(delta_2))`. This is exactly Moh's denominator
increment specialized to the bottom.

Why `L_1` appears: after the levels `s,...,2` have been fixed, the center
`sigma_1` has exponents in `k((x^{-1/L_1}))`. Adding the term
`pi x^{-delta_1}` requires adjoining `T=x^{-1/(L_1 A_1)}`. If
`L_1 delta_1=a/A_1` in lowest terms, then `x^{-delta_1}=T^a`, and the Galois
generator `T -> zeta T` multiplies `pi` by `zeta^a`, a primitive `A_1`-st root.
The primitivity is because `gcd(a,A_1)=1`.

The automorphism fixes `sigma_1`, preserves the bottom disc, and permutes the
`a_1=eV_2` leading `pi`-coefficients of `p_g`. By TF-0 they are distinct. All
nonzero orbits have size `A_1`; the fixed orbit has size 1 if present. Hence

```text
a_1=eV_2 == 0 or 1 mod A_1.
```

The "at most one root is 0" statement does not depend on an arbitrary centering
of the picture. In the natural Moh chart `pi=(y-sigma_1)x^{delta_1}`, the fixed
point of the multiplicative action is `pi=0`. If one translates the coordinate,
the action becomes an affine rotation with one fixed point. Since the roots are
simple, the fixed point can still occur at most once. The orbit count is
coordinate-invariant; only the label "0" uses the `sigma_1`-centered chart.

Moh's final bottom alternatives (12)/(13) imply this congruence. Type `(10)_1`
as a corollary/necessary condition, not the verbatim p.201 print.

## 5. TF-0

Let `P=p_g`, `Q=p_f`, with `deg P=eV`, `deg Q=dV`, and

```text
d Q P' - e Q' P = gamma != 0.
```

If `r` is a double root of `P`, then `P(r)=P'(r)=0`, so the left side at `r`
is 0, contradiction. The same argument handles a double root of `Q`. If `r` is
a common root of `P` and `Q`, both terms vanish at `r`, contradiction. Thus
both polynomials have simple roots and are coprime.

This confirms the correction to D1-SUBTREE: `Q=p_f` also has simple roots.
"Intra-f clustering below delta_1 is free" is false for the leading bottom
coefficient; "invisible to pinned N" remains true.

Machine evidence: `tfcal.py:114-124` plants a double root in `P`, a double root
in `Q`, and a common root; all force the differential expression to vanish at
the planted point. `tfcal.py` rerun: 37 checks, 0 failures.

## 6. TF-DESSIN

Passport: confirmed. Put

```text
phi = Q^e / P^d.
```

Then

```text
phi'/phi = e Q'/Q - d P'/P = -gamma/(P Q).
```

So all finite critical points lie over 0 or infinity: the `dV` roots of `Q`
have index `e`, and the `eV` roots of `P` have index `d`. Since `P` and `Q`
are monic with equal total degree in `Q^e` and `P^d`, `phi(infinity)=1`. The
ODE forces cancellation at infinity so that the point at infinity has index
`(d+e)V-1` over 1, and the finite roots of `Q^e-P^d` are simple. The degree
there is

```text
deV - ((d+e)V - 1) = deV - (d+e)V + 1.
```

Riemann-Hurwitz:

```text
over infinity: eV(d-1)
over 0:        dV(e-1)
over 1:        (d+e)V-2
total:         2deV-2
```

so the passport is genus 0.

Existence: only partially confirmed. For `(d,e)=(2,3)`, the charged cubic
plane-map description is correct after contracting the degree-2 color. The
ordinary map has `2V` cubic vertices, `3V` edges, `V+1` monogonal faces and
one face of degree `5V-1`; deleting the `V+1` loops leaves a tree with `2V`
vertices, `V+1` leaves, and `V-1` trivalent vertices. Such a plane tree exists
for every `V>=1`, so Riemann existence gives the desired Belyi map in the D=48
case `(d,e)=(2,3)`.

The charged text does not provide a general construction for arbitrary coprime
`(d,e)`. "Cubic plane map" is wrong outside `(2,3)`: the bipartite vertices
have degrees `e` and `d`. Therefore:

```text
TF-DESSIN[passport]        CONFIRMED.
TF-DESSIN[(2,3) existence] CONFIRMED in principle; explicit V=1,2 witnesses checked.
TF-DESSIN[all d,e,V]       GAP.
```

Driver note: `bottom_star.py` is not a reliable complete enumerator beyond
V=1. The full run printed:

```text
V=1: one admissible branch, simple(P), simple(Q), resultant nonzero.
V=2: only a gamma=0 branch, then V=3 Groebner solve did not finish before interruption.
```

But `star_explicit.py` directly checks the charged V=2 witness:

```text
P=pi^6+3*pi^3+3/2, Q=pi^4+2*pi, dQP'-eQ'P=-9,
simple(P)=True, simple(Q)=True, coprime=True,
deg(Q^3-P^2)=3.
```

Repair: keep `bottom_star.py` as exploratory; cite `star_explicit.py` or a real
dessin construction for V>=2.

## 7. TF-NOTAME and TF-EXH

The order operator in the charged report is consistent with `kernel_L.py` and
`tfcal.py`:

```text
L_tilde(F,G) = (d-nut) F P' - e F' P + d Q G' - (e-nut) Q' G.
```

`kernel_L.py` rerun with `P=pi^3+3pi`, `Q=pi^2+2`, `(d,e)=(2,3)`:

```text
generic nullity = 3 on deg F<=3, deg G<=4;
rank-drop candidates from one maximal minor: -1,0,1,2,3,4.
```

`tfcal.py` evaluates the same V=1 bottom form at sample `nut` values and finds
generic nullity 3; on the no-tame subspace

```text
Gamma_nu=P(g0+g1 pi), Phi_nu=Q(f0+f1 pi)
```

it solves only the zero vector generically, while at `nut=d+e=5` (equivalently
`nu=1-delta_1`) it finds the residual family `g_i=(e/d)f_i`.

Thus TF-NOTAME is confirmed only at this checked scope:

```text
V=1 bottom form, tame-silent subspace, nu != 1-delta_1.
```

The charged coefficient proof suggests all V, but the supplied drivers do not
establish it. Promote only the V=1 scope until a determinant/free-module proof
for arbitrary simple `P,Q` is added.

TF-EXH is a clean conditional identity. If the bottom-major discs exhaust the
level-2 factor, so

```text
p_2 = product_i (pi-C_i)^{V_i}
```

and TF-NOTAME gives

```text
sum_{j != i} V_j/(C_i-C_j) = 0
```

at every bottom disc, then multiplying the `i`-th equation by `V_i C_i` and
summing gives

```text
sum_i V_i C_i sum_{j != i} V_j/(C_i-C_j)
  = sum_{i<j} V_i V_j.
```

The left side is 0 by the equations. The right side is positive for two or more
nonempty discs. Therefore exhaustion plus TF-NOTAME implies at most one
bottom-major disc.

Exact hypotheses:

```text
1. characteristic zero / algebraically closed coefficient field;
2. distinct bottom-disc centers C_i;
3. positive integer weights V_i;
4. no outer factor w, i.e. the bottom-major discs exhaust p_2;
5. the no-tame conclusion h'(C_i)=0 has already been justified at that order.
```

This is not a skeleton-only census filter without hypothesis 5.

## 8. Numerical reruns and spot checks

### 8.1 D=48

The selected row:

```text
n=48, m=32, M=(-32,-12,46), V_2=1, V_3=3
d-chain [48,16,4,2], (d,e)=(2,3), u=12, v=4
delta_s..delta_1 = -1, 7/22, 3/8
q=(1-delta_1)de/(d+e)=3/4
a_1=eV_2=3, b_1=dV_2=2
A_1=4, a_1 mod A_1=3, so (10)_1 FAIL
A_2=22, A_2 V_2=22 > V_3 d_2/d_3=12, so reconstructed (10) also FAIL
```

`d48final.py` rerun:

```text
V-assignments: census 1301, Def. 5.1(2) windows 1301, Moh (10) 33, +(10)_1 0
groups: 50 -> (10) 12 -> (10)_1 0
```

`sweep.py 48 48 6 16` reproduced:

```text
D=48: V-skel 1301, groups 50, g:(10)=12, g:+(10)_1=0, g:+knap=0,
      V:(10)=33, V:+(10)_1=0.
```

Verdict: dead at order 0 by `(10)_1`; if reconstructed (10) is accepted, it is
also dead at level 2.

### 8.2 D<=120

Live rerun of `sweep.py 48 120 6 16` reproduced the charged totals:

```text
TOTAL: V-skel 902893 ; groups 10637 -> (10) 1012 -> (10)_1 287 -> knapsack-alive 233
V-assignments: 902893 -> (10) 3760 -> (10)_1 329
degrees emptied under reconstructed (10)+(10)_1: 48, 66, 78
```

Typed carefully: this is exact for the implemented reconstruction, not yet an
exact measurement of Moh (8)-(13), because (11) is not recovered.

### 8.3 `(10)_1` alone

The charged `[48,90]` figures match `sweep1.log:3-16`:

```text
D in [48,90]: V-assignments 83860 -> 11150, so 86.70% killed.
D in [48,90]: groups 2080 -> 1792, so 13.85% killed.
knapsack-alive after (10)_1 alone: 916 groups.
```

My live `sweep1.py` attempt reproduced rows through D=88, then was stopped
while spending time in the D=90 knapsack. I therefore treat the `[48,90]`
percentage as log-confirmed, not freshly completed in this lane.

### 8.4 D=105 survivors

Live `sweep.py 105 105 6 16`:

```text
D=105: V-skel 5037, groups 264, g:(10)=38, g:+(10)_1=8, g:+knap=3,
       V:(10)=148, V:+(10)_1=8.
```

`survivors.py` rerun prints exactly three knapsack-alive groups:

```text
m=70, M=(28,103), V_s=5, u=25, (d,e)=(2,3), a_1 in [3],
  N in [6,7,8,9,10,11,12]
m=70, M=(28,103), V_s=6, u=30, (d,e)=(2,3), a_1 in [3],
  N in [9]
m=70, M=(40,103), V_s=4, u=28, (d,e)=(2,3), a_1 in [3],
  N in [9]
```

They also survive `(10)_1` alone. Direct check:

```text
star-only D=105 groups: 203
(70,(28,103),5): 2 star assignments, 1 also reconstructed-(10), star-only hits 6..16
(70,(28,103),6): 2 star assignments, 1 also reconstructed-(10), star-only hit 9
(70,(40,103),4): 2 star assignments, 1 also reconstructed-(10), star-only hit 9
```

### 8.5 D=105 random `(10)_1` hand audit

Seed `20260902`, 20 random assignments from `census(105)`. The check is
`a_1 mod A_1 in {0,1}`.

```text
#  m   M          V_2..V_s      L_1 A_1 a_1 residue verdict
1  70  (-55,103)  [20,4]        127  11   60   5      FAIL
2  70  (98,103)   [7,5]           4  17   21   4      FAIL
3  70  (30,103)   [10,3]         44  49   30   30     FAIL
4  42  (-7,103)   [6,6]          19  41   30   30     FAIL
5  70  (49,103)   [26,6]         47 129   78   78     FAIL
6  63  (-35,103)  [6,5]          33  47   30   30     FAIL
7  70  (28,103)   [2,5]          18   9    6   6      FAIL
8  70  (20,103)   [5,4]          67   4   15   3      FAIL
9  42  (-7,103)   [3,4]          63   4   15   3      FAIL
10 70  (-56,103)  [8,5]          38  39   24   24     FAIL
11 70  (-28,103)  [9,4]          75  22   27   5      FAIL
12 70  (-49,103)  [12,5]        109  59   36   36     FAIL
13 70  (-49,103)  [8,4]          87  13   24   11     FAIL
14 70  (-20,103)  [22,4]         33 109   66   66     FAIL
15 70  (42,103)   [16,4]         35  79   48   48     FAIL
16 84  (-14,103)  [10,5]         28  89   50   50     FAIL
17 70  (-42,103)  [14,6]         25  69   42   42     FAIL
18 70  (63,103)   [26,6]          7 129   78   78     FAIL
19 84  (-70,103)  [10,6]        149  89   50   50     FAIL
20 70  (14,103)   [30,6]         77 149   90   90     FAIL
```

All 20 fail by the displayed residue; D=105 has only 310/5037 assignments
passing `(10)_1` alone and 8 after reconstructed `(10)`.

## 9. Six Moh rows

`d48final.py` and `mohcond.py` both rerun cleanly.

```text
row                         delta_1  L_1 A_1 a_1  a_1 mod A_1  (10)_1
(64,48)                     9/16      4   4  12       0          PASS
(84,56) M2=64,V2=2          16/21     7   3   6       0          PASS
(84,56) M2=72,V2=5          7/12      4   3  15       0          PASS
(75,50) V2=3                1/2       5   2   9       1          PASS
(75,50) V2=2                2/3       5   3   6       0          PASS
(99,66)                     4/9       3   3  24       0          PASS
```

Reconstructed `(10)` at `j=2`:

```text
(64,48):             A_2=4, V_2=3,  A_2 V_2=12, top=12  equality
(84,56) M2=64,V2=2:  A_2=7, V_2=2,  A_2 V_2=14, top=21  strict
(84,56) M2=72,V2=5:  A_2=4, V_2=5,  A_2 V_2=20, top=21  strict
(75,50) V2=3:        A_2=5, V_2=3,  A_2 V_2=15, top=20  strict
(75,50) V2=2:        A_2=5, V_2=2,  A_2 V_2=10, top=20  strict
(99,66):             A_2=3, V_2=8,  A_2 V_2=24, top=24  equality
```

Printed bottom alternatives (12)/(13) also pass all six:

```text
row                         A_1  eV_2 dV_2
(64,48)                      4    12    9
(84,56) M2=64,V2=2           3     6    4
(84,56) M2=72,V2=5           3    15   10
(75,50) V2=3                 2     9    6
(75,50) V2=2                 3     6    4
(99,66)                      3    24   16
```

Calibration against Moh's table is real; it does not upgrade reconstructed
`j>=2` into a source transcription.

## 10. Promotions, repairs, opens

Promote:

```text
OMISSION        The campaign enumerators omit Moh (8)-(11), and in fact (12)-(13).
TF-0            Bottom ODE forces simple roots for P and Q and gcd(P,Q)=1.
(10)_1          Necessary bottom congruence a_1=eV_2 == 0 or 1 mod A_1.
D=48            Selected skeleton dies at order 0; D=48 empties under reconstructed (10)+(10)_1.
D<=120 counts   Promote as measured under reconstructed nonzero-branch (10)+(10)_1.
D=105           Three survivors confirmed; all also survive (10)_1 alone.
TF-EXH          Conditional identity/exhaustion corollary, with hypotheses stated.
```

Do not promote yet:

```text
RECONSTRUCTED (10) j>=2     Not promotable until census-rebase recovers (11) and the page text.
TF-DESSIN all (d,e,V)       Passport yes; all-parameter existence needs a general dessin/permutation construction.
TF-NOTAME all V             V=1 checked; all-V proof not supplied by the drivers.
bottom_star.py V>=2 solve   The script missed the explicit V=2 witness and hung in V=3.
```

Refuted/retired wording:

```text
"Moh prints (10)_1"                      No. Moh prints (12)/(13); (10)_1 is a corollary.
"Delta_j is Moh's denominator increment" No. On p.201 Moh's denominator increment is A_j; Delta_j is the quotient.
"intra-f clustering below delta_1 free"   False for the leading bottom pi-coefficients by TF-0.
"cubic map for every (d,e,V)"             False wording; cubic only for (2,3) after contraction.
```

Bounded OPEN:

```text
OPEN[MOH-11-EXACT]
  Recover (11) and final (12)/(13) verbatim.  Bounded over D<=120 by 3760
  V-assignments / 1012 groups after reconstructed nonzero-branch (10).

OPEN[DESSIN-GENERAL]
  Supply a transitive permutation triple or planar bipartite map for arbitrary
  coprime d,e,V.  Bounded here by the finite (d,e,V_2) set in the 287 D<=120
  groups after reconstructed (10)+(10)_1.

OPEN[TF-NOTAME-GENERAL]
  Prove no-tame injectivity for arbitrary simple P,Q with dQP'-eQ'P=gamma, or
  type it V=1 only.  Bounded algebra: four coefficients f0,f1,g0,g1.

OPEN[BOTTOM-STAR-SOLVER]
  Replace `bottom_star.py`'s generic `sympy.solve` with a dessin/ansatz witness
  checker or a bounded Groebner strategy. Current failure: V=2 solver output
  contradicts `star_explicit.py`, and V=3 did not finish.
```

## 11. Typed verdict block

```text
LANE        TF-CALIBRATION-REVIEW-GPT55-20260902
SCOPE       Hostile review of the D=48 time-function calibration, Moh p.201
            (300 dpi), frozen charged inputs, desk-scale Python/Sympy reruns.

CONFIRMED   Omission: `moh_skeleton_N.py`, `d1floor.py`, and `general.py`
            implement the skeleton/window/integrality machinery, not Moh
            (8)-(11) or final (12)-(13).

CONFIRMED   (10)_1 as a necessary bottom-star congruence:
            A_1=den(L_1 delta_1), L_1=lcm den(delta_s..delta_2),
            a_1=eV_2 == 0 or 1 mod A_1.  The automorphism has order A_1 and
            acts by a primitive multiplier on pi.  "Zero root at most once" is
            invariant; the label zero is the sigma_1-centered chart.

GAP         (10)_1 as verbatim Moh text.  Moh p.201 prints bottom alternatives
            (12)/(13), which imply it; D<=120 measurement shows equivalence
            on 902893 assignments, but the report should call it a corollary.

GAP         Reconstructed (10) for j>=2 is the nonzero-factor branch after
            eliminating Moh's quotient in (9).  It omits (11).  NOT PROMOTABLE
            until census-rebase lands.

CONFIRMED   TF-0: d Q P' - e Q' P = gamma != 0 forces P and Q simple and
            coprime.  This refutes "intra-f clustering below delta_1 is free"
            for leading bottom coefficients.

CONFIRMED   TF-DESSIN passport and genus-zero Riemann-Hurwitz count.
GAP         TF-DESSIN existence for all (d,e,V).  Cubic plane-map construction
            is correct only for (d,e)=(2,3) after contracting degree-2 vertices.
            Explicit (2,3), V=1,2 witnesses pass.

GAP         TF-NOTAME as all-V theorem.  Confirmed by driver only for the V=1
            bottom form and no-tame subspace, with exception nu=1-delta_1.

CONFIRMED   TF-EXH conditionally: under TF-NOTAME and exhaustion of p_2, the
            identity sum_i V_i C_i cond_i = sum_{i<j} V_i V_j implies at most
            one bottom-major disc.

MEASURED    D=48 selected row (48,32), M=(-32,-12,46), V=(1,3), delta=(-1,7/22,3/8),
            a_1=3, q=3/4: (10)_1 fails with A_1=4; reconstructed (10) also
            fails with A_2 V_2=22>12.  D=48 funnel 1301/50 -> 33/12 -> 0/0.

MEASURED    D<=120 combined reconstruction:
            V-assignments 902893 -> 3760 -> 329;
            groups 10637 -> 1012 -> 287 -> 233 knapsack-alive;
            degrees emptied under the reconstruction: 48,66,78.

MEASURED    D=105: 264 groups -> 38 -> 8 -> 3 knapsack-alive:
            (m=70,M=(28,103),V_s=5), (m=70,M=(28,103),V_s=6),
            (m=70,M=(40,103),V_s=4).  All three also survive (10)_1 alone.

MEASURED    Six Moh rows pass (10)_1, printed bottom alternatives (12)/(13),
            and reconstructed (10).  Equality in reconstructed (10) occurs for
            (64,48) and (99,66).

NOT CLAIMED Moh exact rebased census; sufficiency of (10)_1; realisability of
            any surviving skeleton; all-parameter dessin existence; all-V
            TF-NOTAME; any new exit price.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `29032`.
- Body SHA-256:
  `e85f4ce310b16af4b0a1325c12a448965c7c5119cffb2878242de84a316b75a8`.
- Frozen basis: `d2c3632dcc5f0094ba4541024414ef005bd64294`.
