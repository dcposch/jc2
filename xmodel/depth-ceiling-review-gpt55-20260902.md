# Hostile Review: DEPTH-CEILING

Lane: `DEPTH-CEILING-REVIEW`. Date: 2026-09-02. Reviewer: GPT-5.5.

Scope: hostile review of the charged producer report
`depth-ceiling-opus5-20260902.md`, against the local primary texts only
(`refs/moh1983_jram340_configurations_of_roots.pdf` and
`refs/guccione_valqui2017_ja471_shape_counterexamples.pdf`) plus the frozen
charged inputs. I did not inspect `jc2-lean`. I did not edit canonical ledgers.

## Custody

Frozen inputs: all five supplied SHA-256 hashes matched before review.

Read artifacts:

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
b6a369146240dbd36107907ebfb63ab2fc602abb524151d6ab31d39e5bc10722  /tmp/jc2-depth-review/moh1983.txt
449d8028da79c7f2ae9eff9161553fcc35f75a48989f169c5d9ef54edf88773f  /tmp/jc2-depth-review/ggv2017.txt
bda331bad29e46fd154b1de93931bdb2e2e383a0f4fcb377b37210ce432cd7cb  /tmp/jc2-depth-review/moh_p179_def51.png
9ada08891ff4820d5a6cd7fb9993ae75a9381e42e7b4f86eabccd613e933a9f5  /tmp/jc2-depth-review/moh_p180_prop53.png
100ae1c0115149aa22bd5ae0d5c80355c7c71a5364a30982cb53bdac53ec7b51  /tmp/jc2-depth-review/moh_p202_table.png
3db762b9f36da9df1c2144f9ea05d381da442577a54c13a0b92e0b53d3dad668  /tmp/jc2-depth-review/moh_p202_table_360.png
d831e2806868b6735c2bc8ecf337add3ec1a738ac47d656437997f96be3f4941  /tmp/jc2-depth-review/moh_p202_n75_delta_crop.png
3f02018b6c2f4478c92f898e55ba7835d934ace4414ae7156849d4bdf951268f  /tmp/jc2-depth-review/moh_p207_appendixII.png
2b8e80e1d63c1aa7e13fb8c40b28f969456b1950d3b898544d5050b26de7afc3  box/depth-drivers-20260902/depth/mohrec.py
8f02f149ba44520c496703c263d19db108225e6bfc7730ddb22cceb9ba6e9a4e  box/depth-drivers-20260902/depth/places.py
008e46fab801b4f56ac8ecf5a37148d790723fcfe2dac43ecbb4d485e0baa740  box/depth-drivers-20260902/depth/census2.py
beb705eb359175dfa05d462b8c3c0b026d5aba3c2fe92aa316175bd8ea2698b3  box/depth-drivers-20260902/depth/dmin.py
b372c33c7e7203d7b3ca0dec250bd342b243fb5ce3801af33da4bacb15f7d7bc  box/depth-drivers-20260902/depth/res.py
```

Line tags below: `CH` = frozen charged report
`/private/.../inputs/depth-ceiling-opus5-20260902.md`; `MOH` =
`/tmp/jc2-depth-review/moh1983.txt`; `GGV` =
`/tmp/jc2-depth-review/ggv2017.txt`.

## Executive Verdict

The lane has real content, but not all of the charged theorem block survives.
`NU-TWO`, the Moh-side logarithmic depth bound, the place ledger, the contact
deficiency identity, the `(64,48)` correction, and the `D_min >= 105` arithmetic
are promotable after wording repairs. Two charged assertions must not be
promoted as written:

1. The explanation of Moh's `s <= 5` has the wrong displayed lower bound. The
   bound `n >= 4*2^(s-2)` alone gives `s <= 6` at `n <= 100`; Moh's conclusion
   uses the additional proper-gcd fact `K < n`, indeed `n/K >= 2`.
2. The claimed exact reproduction of Moh's delta columns fails on the legible
   bracketed `n=75` entry. Moh's table prints `delta_1 = 1/2 [1/3]`; the
   recovered Definition 5.1(3) formula gives `1/2 [2/3]`. This is a one-entry
   bounded open, or a Moh table typo, but it is not exact reproduction.

## A. DEPTH-LOG

Verdict: **CONFIRMED with repairs** for the Moh-side bound
`3 <= s <= log_2 K`. **GAP/REFUTED as written** for the blanket "attained"
claim and for the charged explanation of Moh's `s <= 5`.

Charged lines: `CH:326-348`, `CH:535-536`, `CH:716-718`.

Source lines:

```text
MOH:105-110   T_i determine and are determined by the characteristic sequence.
MOH:562-566   tree data along one root determine the full symmetric tree; these are {M_i,d_i}.
MOH:591-614   Lemma 2.1: Jacobian condition; exponents terminate at n-1.
MOH:2509-2512 Prop 5.5: s=2 gives invertibility or simultaneous degree reduction.
MOH:3226-3228 after Cor. 6.1, smallest-degree search must assume d_s > 3.
MOH:3255-3278 Moh's degree <=100 search: f=T_1, m=-M_1<n<=100, d_r=gcd(n,M_1,...,M_{r-1}), d_s>=4, conclusion 3<=s<=5.
GGV:1518-1586 standard pair has a unique type II.b starting corner.
GGV:2115-2135 Theorem 7.6: regular corners and Omega(d_i) bounds.
GGV:2270-2285 Cor. 7.9: gcd(a,b)>2; prime/2-prime exclusion for B.
```

Moh side proof:

In Moh's normalization, `d_1=n` and
`d_{r}=gcd(n,M_1,...,M_{r-1})`; in particular
`d_2=gcd(n,M_1)=gcd(n,m)=K` because `M_1=-m` (`MOH:3257-3273`). For effective
characteristic pairs the gcd chain is strict. A strict divisor of an integer is
at most half of it, so

```text
d_2 >= 2^(s-2) d_s.
```

Corollary 6.1 plus the no-reduction/minimal-degree search gives `d_s>=4`
(`MOH:3226-3228`, `MOH:3275-3278`). Therefore

```text
K=d_2 >= 4*2^(s-2)=2^s, hence s <= log_2 K.
```

The lower bound `s>=3` is exactly Moh Prop. 5.5 in the no-reduction case:
`s=2` forces invertibility or a simultaneous degree reduction (`MOH:2509-2512`),
contrary to the degree-minimal noninvertible hypothesis.

Hypotheses repaired:

```text
Keller pair, noninvertible, degree-minimal under polynomial automorphisms;
after a linear GEN gauge, deg f=deg_y f=m, deg g=deg_y g=n, m<n, f=T_1;
s counts Moh's effective characteristic pairs of the target-side
characteristic sequence, not places of a generic pencil member.
No one-place hypothesis is used. In fact the minimal noninvertible case is
forced into the two-point-at-infinity alternative by Moh Prop. 5.4/Lem. 5.3.
```

Moh's `s <= 5`:

The producer says this is `n >= 4*2^(s-2)` at `n <=100`. That arithmetic is
insufficient: for `s=6` it gives only `n>=64`. The missing line is that
`K=d_2` is a proper divisor of `n`; since `m<n` and `K=gcd(m,n)`, `n/K>=2`.
Thus

```text
n >= 2K >= 2^(s+1).
```

At `n<=100`, `s=6` would force `n>=128`, so Moh's `s<=5` follows. Under the
later degree-minimal leading-form split one even has `n/K>=3`, but Moh's
printed step needs only `n/K>=2`.

GGV side:

The charged proof needs one indexing repair. The weak Theorem 7.6(7) clause
`Omega(d_j)>=j-1` bounds `k`, not `k+1`. For a standard pair the starting
corner is type II.b (`GGV:1521-1522`, `GGV:1580-1586`), so Theorem 7.6(8)
applies and gives `Omega(d_i)>=i` for `i>0` (`GGV:2134-2135`). For the last
corner this gives `d_k>=2^k`. Since `d_k | gcd(a,b)`, `a<b`, and in the
standard degree-minimal gauge `a+b=K`, one has `d_k < K/2`; hence
`2^(k+1)<K`, i.e. `k+1 < log_2 K`. This confirms the advertised
`k+1 <= log_2 K` as a real inequality, with a strict margin.

Attainment:

`census2.py` confirms sharpness for Moh numerical skeletons in the coarse
enumeration:

```text
n=64 max s=4=max floor(log2 K)
n=96 max s=5=max floor(log2 K)
n=192 max s=6=max floor(log2 K)
n=384 max s=7=max floor(log2 K)
```

That is not a source theorem and not an actual-counterexample witness. On the
GGV side the repaired proof is strict (`k+1 < log_2 K`), so exact real
attainment is not even the right statement. Repair: promote "Moh-side bound is
sharp on the numerical skeleton census"; do not promote "the bound is
attained" for actual maps or for GGV corners.

Promotion recommendation: **PROMOTE DEPTH-LOG after repairs**; **DEMOTE
attainment to MEASURED-SKELETON only**.

## B. PLACE-LEDGER

Verdict: **CONFIRMED** as an identity over places at infinity. The theorem is
not a depth bound. The advertised 16/16 HN rerun is only **partially rerun here**
because one row timed out at 300s; the mandatory four-row recomputation
passed.

Charged lines: `CH:177-223`, `CH:466-502`, `CH:623-634`.

Proof:

Let `C` be a generic affine member `aP+bQ+c=0`, projectively closed in degree
`D=max(deg P,deg Q)`, and let `gamma` run through its places over `L_infty`.
Then `sum_gamma nu_gamma=D` by intersection with `L_infty`. The function
`P|_C` has degree equal to the geometric degree `N` of the map, because a
generic value of `P` on the generic target line cuts a generic fiber of `F`;
therefore the pole divisor of `P|_C` has degree `N`, i.e.
`sum_gamma m_gamma=N`.

Finally

```text
T := sum_gamma (nu_gamma-1),   r_inf(C)=#places = D-T.
```

Proper places are exactly those with `m_gamma>0`; non-proper places have
`m_gamma=0`. Hence `D-T=kappa+S n`, the place form of DEG-SPLIT.

Reconciliation:

This is exactly SAT-WEIGHT with the boundary component multiplicity `c_C`
expanded into `c_C` individual places:

```text
SAT-WEIGHT: D=sum_C nu_C c_C, N=sum_C m_C c_C, D-T=sum_C c_C.
PLACE-LEDGER: same identities after replacing each component C by its c_C places.
```

Thus this `T` is `T_ext` from integration #12/#14, not a new classical-only
quantity. HALF-CAP is also consistent: for one dicritical and `D>N`, it gives a
floor `D <= 2(T+kappa)`, not an upper bound on `T`. PLACE-LEDGER therefore
locates the mass but does not cap it.

Four rerun rows from `places.py`:

```text
map                    D  r_inf  T=D-r_inf  nu-list       N
(x, y+x^4)             4      1          3  [4]           1
(x, xy^2)              3      3          0  [1,1,1]       2
psi_2 o (x,xy^2)       6      3          3  [1,1,4]       2
(x^3, y^2)             3      1          2  [3]           6
```

The default 16-row run produced 15 OK rows and one timeout:

```text
psi_4 o (x,xy^2)  EXC TimeoutExpired
failures: 1
```

Rerunning that row with a 300s subprocess timeout still timed out. This is not
a counterexample to the identity; it is a reproducibility limit in this review.
Repair the measured claim to "15/16 rerun here at <=300s; four required rows
confirmed; producer's separate long-budget row not independently confirmed in
this pass."

Promotion recommendation: **PROMOTE PLACE-LEDGER**; **do not promote the
unqualified 16/16 rerun claim from this review alone**.

## C. CONTACT-DEFICIENCY

Verdict: **CONFIRMED with gauge stated**. Also confirmed: Moh/GGV do not form
this quadratic pairing sum as a constraint. The successor is `OPEN[N-ON-THE-
TREE]`, not another depth-count lane.

Charged lines: `CH:362-430`, `CH:565-578`, `CH:713-714`.

The identity:

Assume `f-c_1` and `g-c_2` are monic in `y` and have `y`-degree equal to total
degree in the chosen GEN gauge. Over `C((t))`, `t=x^-1`, write

```text
f-c_1 = prod_j (y-phi_j),   g-c_2 = prod_i (y-tau_i).
```

Then

```text
Res_y(f-c_1,g-c_2)=prod_{i,j}(phi_j-tau_i).
```

For generic `(c_1,c_2)` the affine intersection is a generic fiber of `F`;
therefore its degree in `x` is the geometric degree `N`. Since
`deg_x R = -ord_t R(x=t^-1)`,

```text
N = - sum_{i,j} ord_t(tau_i-phi_j).
```

If the common leading form is `H=L_1^u L_2^v`, with
`l(f)=alpha H^d`, `l(g)=beta H^e`, then there are `du,dv` roots of `f-c_1`
and `eu,ev` roots of `g-c_2` on the two slopes. Different-slope pairs have
`ord_t=-1`; there are `du*ev+dv*eu=2deuv` of them. Hence

```text
N = 2deuv - sum_same_slope ord_t(tau_i-phi_j).
```

Three requested recomputations:

```text
automorphism, GEN gauge:
  f=x+y, g=y+(x+y)^3.
  J=1, Res_y(f-7/3,g+5/2)=x-947/54, deg_x=1=N.
  Thus -sum ord=1.

sheared representative of (x, x y^3):
  f=x+y, g=(x+y)y^3.
  Res_y(f-7/3,g+5/2) has degree 3, so -sum ord=3=N.
  The raw unsheared (x,xy^m) is not in the monic-root hypothesis for f.

non-Keller two-slope example:
  H=(y-x)(y-2x), f=H^2+y, g=H^3+x.
  J is nonconstant. Res_y(f-7/3,g+5/2) is squarefree of degree 6, so N=6.
  Here d=2,e=3,u=v=1, so 2deuv=12 and the same-slope contact sum is 6.
```

Assessment of Moh/GGV blindness:

Moh's Definition 5.1 counts roots of `g` and `T_j` in one tower of major discs
(`MOH:2115-2137`), and Proposition 5.3 advances that tower using one chosen
factor and multiplicity (`MOH:2155-2177`). His theorem separates major and
minor discs qualitatively (`MOH:3236-3253`) and his search list is in
`(n,M_i,d_i,V_i,delta_i)` (`MOH:3255-3320`). GGV's constraints are on regular
corners, divisibilities, and Newton polygon data (`GGV:1518-1785`,
`GGV:2115-2285`). In the inspected lines, neither source forms
`deg_x Res_y`, the proper/non-proper split, or the double sum over all
`g`-roots and `f`-roots.

This does not mean `N` is absent from the objects: the identity above expresses
`N` on Moh's root tree in principle. It means the published recursion does not
evaluate the global pairing. The missing bounded datum is the minor-disc
distribution needed to sum all first separations, not the count of major depth
levels.

Promotion recommendation: **PROMOTE CONTACT-DEFICIENCY with monic GEN
hypothesis**; **PROMOTE OPEN[N-ON-THE-TREE]**:

```text
BOUNDED QUANTITY: the integer
N = -sum_{i=1..n} sum_{j=1..m} ord_t(tau_i-phi_j), 1 <= N <= mn,
computed from Moh major-tower data plus minor-disc distribution.
```

## D. MOH-SHARP-2

Verdict: **CONFIRMED after source-legitimacy repair**. The arithmetic list is
correct. The phrase "GGV Cor. 7.9 at K" is not a direct citation; it is a
replay of GGV's proof with degree-minimality replacing B-minimality at the one
place GGV uses minimality of `B`.

Charged lines: `CH:582-612`.

Source lines:

```text
MOH:169-178   Moh states the <=100 computation in the introduction.
MOH:3226-3278 d_s>=4 and 3<=s in the no-reduction search.
MOH:3596-3603 Appendix II states the special cases and computational wall.
GGV:693-705   B and minimal pair are defined as gcd-minimal over counterexamples.
GGV:796-879   Prop. 4.7 constructs an (m,n)-pair and proves v_1,1 preservation using minimality.
GGV:1432-1462 Prop. 5.20 / Cor. 5.21 standardize while preserving v_1,1 and en_1,0.
GGV:1761-1769 Cor. 6.6 proves B>=16.
GGV:2270-2285 Cor. 7.9 proves gcd(a,b)>2 and B != p,2p.
```

Legitimacy repair:

GGV define `B` as the minimum gcd among all counterexamples (`GGV:693-699`).
Corollary 7.9 states the prime/2-prime exclusion for `B`, not for every
arbitrary counterexample degree gcd (`GGV:2270-2272`). However, the proof can
be replayed for a degree-minimal counterexample:

1. Proposition 4.7 first constructs a subrectangular `(m,n)` shape with
   `en_{1,0}(P)=st_{1,1}(P)` (`GGV:816-823`).
2. In the preservation step, GGV use minimality of `B` at `GGV:873-877` to rule
   out a transformation that would lower the common `v_1,1` factor. If the
   pair is degree-minimal, the same alternative lowers both total degrees, so
   it is also impossible.
3. Proposition 5.20 then standardizes and preserves `v_1,1` and `en_{1,0}`
   (`GGV:1432-1437`).
4. Corollary 7.9's first half applies to every standard `(m,n)`-pair:
   `gcd(a,b)>2` (`GGV:2270-2278`). In this repaired standard gauge,
   `(a,b)=(1/m)en_{1,0}(P)=(1/m)st_{1,1}(P)` and `a+b=K`. Therefore
   `gcd(a,b)|K`; if `K=p` or `2p`, the same `a<b` argument at
   `GGV:2283-2285` excludes it.

Thus (F4) is legitimate, but only with this proof replay written out.

Finite arithmetic rerun:

Conditions used:

```text
(F1) D=K*e, e>=3, and some d with 2<=d<e, gcd(d,e)=1.
(F2) K>=16.
(F3) K has a proper divisor c>=4, namely d_s.
(F4) K is neither p nor 2p.
(F5) D>=101.
```

`dmin.py` output:

```text
admissible D in [101,120] = [105,108,112,117,120]
D=105  K in [21,35]
D=108  K in [18,27,36]
D=112  K in [16,28]
D=117  K in [39]
D=120  K in [20,24,30,40]
admissible D in [101,200]: 30 of 100.
```

Moh survivor control:

```text
(64,48) K=16, e=4,d=3 passes F2-F4.
(84,56) K=28, e=3,d=2 passes F2-F4.
(75,50) K=25, e=3,d=2 passes F2-F4.
(99,66) K=33, e=3,d=2 passes F2-F4.
```

Promotion recommendation: **PROMOTE MOH-SHARP-2 with proof-replay repair**.

## E. NU-TWO

Verdict: **CONFIRMED with scope repair**.

Charged lines: `CH:126-153`, `CH:656-657`.

Source lines:

```text
MOH:1588-1597 Prop. 4.5: if M_r=n-2, top forms are powers of a common form with at most two distinct linear factors, and the two multiplicities are different.
MOH:2317-2330 Prop. 5.4: if the smallest-disc radius is > -1, then invertible or simultaneous degree reduction.
MOH:2453-2457 Lem. 5.3: smallest-disc radius -1 iff M_s=n-2 and the highest form of g has two roots.
```

For a degree-minimal noninvertible Keller pair in any GEN gauge
(`deg=deg_y`, monic in `y`), the reduction alternative in Prop. 5.4 is
forbidden. Hence the smallest disc must have logarithmic radius `-1`. Lemma
5.3 then gives `M_s=n-2` and two roots of the top form of `g`. Proposition 4.5
upgrades this to a common top form with at most two linear factors and different
multiplicities. Combining "two roots" with "at most two" gives exactly two.

Repair:

Say "gauge-free among GEN gauges." Do not state this for a coordinate system
where `deg_y` is not the total degree. The conclusion `E_0` is free also uses
the separately promoted FIRST-FORK result from integration #14; Moh supplies
the two-root leading form, not the polar-tree valency theorem by itself.

Promotion recommendation: **PROMOTE NU-TWO in GEN scope**; **close
OPEN[NU2-RIGIDITY] positive in that scope**.

## F. Moh Survivor Correction

Verdict: **CONFIRMED as an internal repair to Moh/MKS**. Moh's Appendix II
sentence really prints `(64,68)`, but Moh's own Section 6 table and reduced
Appendix II row force `(64,48)`.

Charged lines: `CH:640-651`.

Source lines and page checks:

```text
MOH:3331-3338  Section 6 table first row: n=64, m=-M_1=48, M_2=52, M_3=62, M_4=63.
MOH:3596-3598  Appendix II sentence prints degrees (64,68), (84,56), (75,50), (99,66).
MOH:3604-3626  Appendix II transforms first three cases to (16,12), (21,14), (15,10).
```

The page image `moh_p207_appendixII.png` confirms the appendix sentence is
printed as `(64,68)`, not merely an OCR hallucination. The page image
`moh_p202_table.png` confirms the Section 6 table first row is `(n,m)=(64,48)`.
The reduced row `(16,12)` is exactly `(64,48)/4`, while `(64,68)/4` is not
integral in the second coordinate and is incompatible with the displayed
reduction. Therefore the repair is forced: treat `(64,68)` as Moh's printed
typo and use `(64,48)`.

Consequences confirmed:

```text
gcd(64,48)=16, gcd(84,56)=28, gcd(75,50)=25, gcd(99,66)=33.
All four have K>=16. None is killed by GGV Cor. 6.6.
```

Promotion recommendation: **PROMOTE correction `(64,68)` -> `(64,48)`**, with
the caveat that this corrects a printed inconsistency in Moh, not just OCR.

## G. Definition 5.1(3), Delta Columns, and "25 Values"

Verdict: **SPLIT**.

* Definition 5.1(3) formula: **CONFIRMED** from the rendered page image and
  OCR line range.
* Delta-column "reproduced exactly": **REFUTED/GAP** because of the legible
  bracketed `n=75` entry.
* Moh's "25 possible values for M_2" at `(75,50)`: **CONFIRMED**.

Charged lines: `CH:257-309`, `CH:444-464`, `CH:513-517`.

Source lines:

```text
MOH:2115-2137  Definition 5.1, OCR-damaged but formula confirmed on page 179 image.
MOH:2155-2177  Proposition 5.3, page 180 image confirms the next-disc formula.
MOH:3331-3345  Section 6 table of M_i, V_i, delta_i.
MOH:3348-3350  Moh says (75,50) has 25 possible M_2 values and 2 possible V_3 values.
```

The recovered formula from page 179 is:

```text
delta_i = 1 -
 (n-M_i) prod_{j=i+1..s} [ V_j (n-M_j) - d_j ]
 -------------------------------------------------
 (n-M_s-1) prod_{j=i+1..s} [ V_j (n-M_{j-1}) - d_j ].
```

`mohrec.py` reproduces the following printed entries:

```text
n=64: delta_2=1/4, delta_1=9/16.
n=84, M_2=64,V_2=2: delta_2=2/7, delta_1=16/21.
n=84, M_2=72,V_2=5: delta_2=1/4, delta_1=7/12.
n=99: delta_2=1/3, delta_1=4/9.
n=75, V_2=3: delta_2=1/5, delta_1=1/2.
```

But the high-resolution crop of Moh's `n=75` row shows:

```text
V_2 = 3 [2],   delta_2 = 1/5,   delta_1 = 1/2 [1/3].
```

For the bracketed `V_2=2` alternative, the recovered formula gives:

```text
n=75, m=50, M=[-50,55,73], d=[75,25,5,1], V=[2,4,1]
delta_3=-1, delta_2=1/5, delta_1=2/3.
```

So the charged "exact reproduction" statement is false as written. Either
Moh's bracketed `1/3` is a printed table error, or the recovered formula is
being applied to the wrong bracketed alternative. Because Definition 5.1(3)'s
page image agrees with the driver formula and the formula matches every other
checked entry, the likely repair is "Moh table typo at `n=75`, bracketed
`delta_1`." Hostile standard: do not promote exact reproduction until that
single entry is adjudicated.

The "25 possible values" statement is confirmed independently. At `(n,m)=(75,50)`,
`K=25` and the next divisor is `d_3=5`. The multiples of `5` in `[-50,74)` are
exactly 25; imposing the genuine drop condition `gcd(25,M_2)=5` leaves 20. This
matches the driver and explains the difference between Moh's loose count and
the stricter skeleton count.

Promotion recommendation: **PROMOTE recovered Definition 5.1(3)** and
**PROMOTE the 25-value calibration**; **DO NOT PROMOTE exact delta-column
reproduction**.

```text
OPEN[DELTA75-BRACKET]
BOUNDED QUANTITY: one rational table entry, the bracketed delta_1 for
(n,m,M_2,M_3,V_3,V_2)=(75,50,55,73,4,2). Moh table prints 1/3; recovered
Definition 5.1(3) gives 2/3.
```

## Typed Verdict Block

```text
LANE        DEPTH-CEILING hostile review
SCOPE       Keller, noninvertible, degree-minimal where stated; GEN gauge
            means monic in y with deg=deg_y. PLACE-LEDGER is general for
            dominant maps. CONTACT-DEFICIENCY requires the monic GEN resultant
            hypothesis. No case (A), A2, reducible-branch, or Z(G)=1 change.

ITEM A      DEPTH-LOG
STATUS      CONFIRMED with repairs; attainment GAP/DEMOTED.
LINES       CH:326-348; MOH:105-110,562-566,2509-2512,3226-3278;
            GGV:1518-1586,2115-2135.
REPAIR      Moh-side: d_2=K and strict divisor chain give K>=2^s.
            Moh s<=5 at n<=100 additionally uses n/K>=2, not only
            n>=4*2^(s-2). GGV side uses Theorem 7.6(8), not only 7.6(7).
PROMOTION   Promote bound; demote "attained" to Moh numerical skeleton evidence.

ITEM B      PLACE-LEDGER
STATUS      CONFIRMED; 16/16 rerun not confirmed here.
LINES       CH:177-223,466-502; SM input:261-278; I14:48-56.
REPAIR      Identify T with T_ext/SAT-WEIGHT component expansion. HALF-CAP is
            a floor. Four mandatory rows rerun; one optional 16-row battery
            row timed out at 300s.
PROMOTION   Promote theorem, not the unqualified measured 16/16 claim.

ITEM C      CONTACT-DEFICIENCY
STATUS      CONFIRMED with monic GEN hypothesis.
LINES       CH:362-430,565-578; MOH:2115-2177,3236-3320; GGV:1518-2285.
REPAIR      Raw (x,xy^m) must be sheared to a monic f-root gauge before using
            the root product. Moh/GGV do not form the global pairing sum.
PROMOTION   Promote identity and OPEN[N-ON-THE-TREE].

ITEM D      MOH-SHARP-2
STATUS      CONFIRMED after proof-replay repair.
LINES       CH:582-612; MOH:169-178,3226-3278,3596-3603;
            GGV:693-705,796-879,1432-1462,1761-1769,2270-2285.
REPAIR      Cor. 7.9 excludes p and 2p for B directly. For degree-minimal K,
            replay Prop. 4.7's preservation argument with degree-minimality.
            Arithmetic list [101,120] = {105,108,112,117,120}.
PROMOTION   Promote D_min>=105.

ITEM E      NU-TWO
STATUS      CONFIRMED in GEN gauges.
LINES       CH:126-153; MOH:1588-1597,2317-2330,2453-2457.
REPAIR      "Gauge-free" means any gauge with deg=deg_y. E0-free additionally
            consumes FIRST-FORK from integration #14.
PROMOTION   Promote; close OPEN[NU2-RIGIDITY] positive in GEN scope.

ITEM F      Moh survivor correction
STATUS      CONFIRMED as internal correction.
LINES       CH:640-651; MOH:3331-3345,3596-3598,3604-3626.
REPAIR      Moh's appendix prints (64,68), but the Section 6 table and reduced
            row force (64,48). All four survivors have K>=16; none is killed
            by GGV Cor. 6.6.
PROMOTION   Promote correction with "printed typo" caveat.

ITEM G      Definition 5.1(3), deltas, 25 values
STATUS      SPLIT: formula CONFIRMED; exact delta reproduction REFUTED/GAP;
            25-value calibration CONFIRMED.
LINES       CH:257-309,444-464,513-517; MOH:2115-2137,2155-2177,3331-3350.
REPAIR      Do not claim exact reproduction while n=75 bracketed delta_1 is
            unresolved: Moh prints 1/3, recovered formula gives 2/3.
PROMOTION   Promote formula and 25-value count; keep OPEN[DELTA75-BRACKET].

OPENS       OPEN[N-ON-THE-TREE]: bounded integer N in [1,mn] from complete
            major/minor root-pair distribution.
            OPEN[DELTA75-BRACKET]: one rational delta table entry.
            TEST-GAP[PLACE-16TH-RERUN]: HN row psi_4 o (x,xy^2) timed out
            at 300s in this review; not a mathematical open.

FALLACY-v2  No new exit-price assertion, so no charge_basis line. The review
            separates flag/place/series depth, does not infer attainment from
            a floor, treats representative skeleton evidence as non-actual,
            and leaves the one delta mismatch open instead of filling by cap
            or analogy.
```

## Final Recommendation

Promote the lane only in repaired form:

```text
PROMOTE:
  NU-TWO (GEN gauge), DEPTH-LOG bound, PLACE-LEDGER, CONTACT-DEFICIENCY,
  MOH-SHARP-2 D_min>=105, Moh survivor correction, Definition 5.1(3) formula,
  and the 25-value calibration.

DO NOT PROMOTE AS WRITTEN:
  exact delta-column reproduction;
  "bound is attained" outside Moh skeleton-census wording;
  the displayed explanation n>=4*2^(s-2) => s<=5.

SUCCESSOR:
  N-ON-THE-TREE. The bounded object is the double contact sum over all
  f/g root pairs, requiring the minor-disc distribution absent from Moh/GGV's
  published constraints.
```

<!-- BODY-END -->
