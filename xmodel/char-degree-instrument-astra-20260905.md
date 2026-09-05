The characteristic-degree instrument is a valid necessary condition and excludes the cone vertex. For the two clients its attained degrees are **55** and **63**, respectively. The leading rows occur at normalized depths **143** and **153**. They can be adjoined to stage 0 as full coefficient equations, but they are not consequences of the old shallow truncations. The finite computation status will be recorded below after the owned worker has finished and been terminated.

This report distinguishes four assertions: printed necessity for realized data; an exact exclusion theorem on the degenerate locus; an implementation of the augmented necessary chart; and a decision about that chart. The first three do not substitute for the fourth. No campaign ledger, `jc2-lean`, or `ideation-*` file was edited. No exit-price assertion is made.

**1. Custody and scope.** Before reading the charged material, I mechanically built a SHA-256 manifest from the receipt's paired `charged_input_<i>_basename` and `_sha256` fields with `awk`, then ran `sha256sum -c` against `/tmp/jc2-lane.Q25z05/inputs`. All seven files passed. The manifest and transcript are [inputs.sha256](/home/ubuntu/jc2/box/char-degree-20260905/inputs.sha256) and [hash-check.txt](/home/ubuntu/jc2/box/char-degree-20260905/hash-check.txt). The receipt basis is `47c51904e6147923be45b799072444f87a147cb7`; the recorded start is 2026-09-05 20:44:20 UTC. All new drivers, copies, controls, and run receipts are under `box/char-degree-20260905/`.

The mathematical source is Moh's 1983 article. “Keller Lemma 2.1” here means Moh's lemma about the Keller hypothesis. I read the frozen PDF, its fresh text extraction, and images where the formulas did not extract reliably. Citations below use printed page numbers. The full source audit, including the relevant image names and extraction locations, is [source-audit.md](/home/ubuntu/jc2/box/char-degree-20260905/source-audit.md). Existing corrected-engine files were consumed through retained snapshots and declared maps; an equation is not identified merely because its coordinate has the same name.

The charged reports establish inclusion of the truncated pure-power locus in the old necessary chart. They do not supply an exhaustion theorem saying that every old-chart point belongs to that locus. Accordingly, “the only survivors found” is not used as “the only possible survivors.” The new obstruction requires a fresh decision on the whole augmented ideal.

**2. Printed attainment theorem.** Use Moh's order `(f,g)=(G,F)`, with `deg_y F=n`, `deg_y G=m`, and characteristic indices `M_i`. Printed p150 defines

\[
d_1=n,\quad d_{i+1}=\gcd(n,M_1,\ldots,M_i),\quad
n_i=d_i/d_{i+1},\quad q_1=M_1,\quad q_i=M_i-M_{i-1},
\]
\[
\Lambda_i=\sum_{j\le i}q_jd_j,\qquad \mu_i=\Lambda_i/d_i,
\qquad D_i=-\mu_i.
\]

I write `Lambda_i` for this numerical invariant and reserve `lambda_i` for a free leading coefficient. The auxiliary roots `h2,h3` have different degrees and are not characteristic polynomials.

Under the Keller hypothesis, Lemma 2.1, printed p151, proves `e=n−1` and `deg_x f_e(x)=1`. Its proof makes every earlier series coefficient `f_j(x)`, `j<e`, constant. Proposition 2.1, p152, says that taking the monic approximate root commutes with the coefficient specialization `psi:x→0`. This specialization acts on coefficients of a polynomial in **formal target variables**; it does not set the physical source coordinate to zero after composition.

Proposition 2.2(1), p152, states the exact equality

\[
\deg_y T_i^\psi(G(x,y),F(x,y))=-\mu_i=D_i
\]

when `M_i≤e`. Part (2) says the leader is a unit when `M_i<e`. The end of the proof on p154 explicitly uses “monic” to mean a unit leader, not a leader already set equal to 1. Since the coefficient ring is `k[x]`, that unit is a nonzero scalar. Part (3) treats `M_i=e` differently: the leader is a nonzero scalar times `f_e(x)` and has x-degree one. The definition on p174 removes a terminal `M_h=n−1` from the effective list. Thus every effective index `i≤s` is in the scalar-unit case.

**Theorem A — effective characteristic attainment.** Over a characteristic-zero field, every realized datum satisfying Moh's monic Keller setup has, at each effective index, a specialized constant-coefficient target polynomial whose composition has actual y-degree `D_i` and nonzero scalar leader. Therefore its coefficient equations, exact upper-degree equations, scalar-leader equations, and a leader localizer are necessary equations on any coefficient chart intended to contain every such realization.

This proves attainment from printed statements, rather than turning a degree upper bound into equality. It applies uniformly to the effective indices. It does not confer a Keller hypothesis on an arbitrary chart point or on an incomplete child prefix.

There are two precise coordinate implementations. One is canonical: form

\[
\mathcal R(U,V)=\operatorname{Res}_y(F(0,y)-V,\ U-G(0,y)),
\]

monic of U-degree n; take its monic `d_i`-th approximate root in U and compose `(U,V)=(G,F)`. The finite approximate-root recursion divides only by nonzero integers, so its coefficients are polynomial functions over Q of the source coefficients. Proposition 2.1 supplies the specialization bridge. The second implementation existentially retains every target monomial allowed by Proposition 3.1. It can enlarge the canonical locus and is consequently safe for a necessary-chart exclusion. Without the canonical identities, its member must be called a family representative, not an independently certified canonical `T_i`.

The numerical calculations, independently recomputed in [source-audit-controls.json](/home/ubuntu/jc2/box/char-degree-20260905/source-audit-controls.json), are:

| Client | M sequence | d sequence | Lambda sequence | Effective characteristic degrees |
|---|---|---|---|---|
| `(99,66)` | `−66,77,97` | `99,33,11,1` | `−6534,−1815,−1595` | `66,55,145` |
| D=108 | `−72,81,106` | `108,36,9,1` | `−7776,−2268,−2043` | `72,63,227` |

Hence the requested ratios are `99:66:55=9:6:5` and `108:72:63=12:8:7`. In both clients all three displayed indices are effective. The auxiliary degree pairs are `(33,11)` and `(36,9)`.

**3. The complete T2 family and polynomial rows.** Proposition 3.1, printed p157, gives the recursive target expansion, its weight inequality, and its unique term of equality weight, which omits the latest characteristic polynomial. Its specialization remark is on p159. Here `n_1=3` and `T1^psi=G+constant`. Enumerating the permitted monomials of weight at most `3m=2n`, with G-exponent below 3, gives exactly `1,G,G²,F,FG,F²`. The unique equality term is `F²`; cancellation of the monic highest term forces its coefficient to be −1. Absorbing the constant shift of T1 gives the full necessary family

\[
Q=G^3-F^2+aG^2+bFG+cF+dG+e_0.\tag{1}
\]

All five lower target coefficients remain. Four are recovered triangularly from high y-coefficients: start with `Q0=G³−F²`, set `b=−[x⁰y^(n+m)]Q0`, add `bFG`, then successively choose `a,c,d` to cancel the constant-x coefficients at y-heights `2m,n,m`. The leaders used are 1. Every unselected coefficient remains an equation, including positive-x coefficients at those heights. The heights are `165,132,99,66` and `180,144,108,72`.

The assertion that the degree rows determine **all five** scalars needs a correction: `e0` changes only the constant coefficient and is free in this necessary enlargement. The canonical resultant construction determines it; the upper-degree and attained-positive-degree rows do not. Retaining it avoids silently deleting a permitted target term.

Write `q_pq=[x^p y^q]Q` and let `L=2n=3m`. Each coefficient is a polynomial over Q in the F/G chart coordinates and `a,b,c,d,e0`. Proposition 2.2 licenses the finite rows

\[
q_{pq}=0\ (q>D_2),\quad q_{p,D_2}=0\ (p>0),\quad
q_{0,D_2}-\lambda=0,\quad Z\lambda-1=0.\tag{2}
\]

Indices range over the ambient degree bound `p+q≤L`. These equations express an actual scalar leader. The last row makes it a unit in the localized coordinate ring. In particular, the leading row is **coefficient minus target**, never the coefficient alone. A derived coefficient that happens to vanish yields a genuine contradiction with the localizer only after all necessary maps and target subtractions have been respected.

Proposition 2.2 alone proves y-degree. A separate printed argument permits the stronger total-degree block used in the runs. Proposition 4.5, p169, for `M_r=n−2`, gives a common highest homogeneous form for F and the earlier characteristic polynomials `i<r`. Its proof on p172 explicitly considers the roots of the specialized `T_i^psi` for every `i≤r`. The minimum root-order argument rules out order below −1 in the existing coordinates. A polynomial of y-degree D with scalar leader and all roots of order at least −1 has coefficient bounds `deg_x[y^(D-j)]≤j`, hence total degree D. No new generic shear is involved. For the present `r=3`, this licenses total degrees 55/63 for T2 and also 145/227 for T3.

The already placed F tops are `y²⁷(y−x)⁷²` and `y²⁴(y−x)⁸⁴`. The common-form conclusion therefore forces

\[
Q_{55}=\lambda y^{15}(y-x)^{40},\qquad
Q_{63}=\lambda y^{14}(y-x)^{49}.\tag{3}
\]

These whole homogeneous targets, with free nonzero lambda, are subtracted. They are printed-source consequences, not guesses from a support picture. Two representatives of (1) of degree below m differ by at most a constant, since the other four target differences have distinct degrees `5k,4k,3k,2k>D2`; thus the existential family retains this necessary top condition. Section 4's normalization of the Jacobian to 1 causes no additional gauge expenditure here: allowing a nonzero Jacobian scalar multiplies the source identities by a nonzero constant and leaves their root-order comparisons intact.

**4. Where the rows live.** Set `t=1/x`, `z=ty−1`, and `K_P=t^(deg-bound P)P(1/t,(1+z)/t)`. For (99,66), the complete target expression is

\[
K_Q=K_G^3-K_F^2+b t^{33}K_FK_G+a t^{66}K_G^2
 +c t^{99}K_F+d t^{132}K_G+e_0t^{198}.
\]

D108 replaces the scale 33 by 36. A physical monomial `x^p y^q` in Q occurs at t-depth `L−p−q`. Thus the leading homogeneous target occurs at depth `L−D2`, and the complete equations say every earlier coefficient polynomial vanishes, followed by subtraction of the entire target polynomial at that depth.

| Quantity | `(99,66)` | D=108 |
|---|---:|---:|
| Ambient Q bound L | 198 | 216 |
| T2 leader depth `L−D2` | **143** | **153** |
| Degree-zero Jacobian depth `n+m−2` | 163 | 178 |
| Intrinsic recursive defect `n1 D1−D2` | 143 | 153 |
| Next recursive defect `n2 D2−D3` | 20 | 25 |

At the whole-target band, the raw D2 location weights `3r+4q` and `4r+5q` range over **589–649** and **857–927**. The leader corners `t^143 z^55` and `t^153 z^63` have weights649 and927. These location weights use different ambient normalizers from the Jacobian; they are neither stage numbers nor automatically valuations of the complete Q. The intrinsic recursive defect is `q_(i+1)=n_iD_i−D_(i+1)`.

Some high-degree cancellation rows are early, and they yield useful elimination. The nonzero attainment row itself is deep. Renaming the characteristic residual as a new low-degree object does not prove those deep cancellations. Adjoining the full block at every finite stage is legitimate, but it accesses coefficients omitted by the old truncation theorem. It is therefore a non-truncation instrument, not a uniform small-depth instrument.

One consequence explains the limited role of the old shallow Jacobian rows. The chain rule gives

\[
J(F,Q)=(3G^2+2aG+bF+d)J(F,G).
\]

The first factor has actual degree `2m=4k`. With total degree `Q≤D2`, a nonzero Jacobian has degree at most `D2−k−2`, namely **20** or **25**. Hence all Jacobian bands tested at stages 0–8 already vanish on the strengthened characteristic locus. This does not force the remaining low-degree Jacobian to be constant.

**5. The cone vertex fails attainment.** Let h be monic of y-degree k and let

\[
F=h^3+B h+C,\qquad G=h^2+D h+E,
\]

with four scalar parameters. Every constant-coefficient target polynomial in F,G lies in `k[h]`. A nonconstant polynomial of h-degree l has actual y-degree `kl`; zero and constants are handled separately. Neither 55 is divisible by 33 nor 63 by 36. Thus the exact attainment locus misses the whole four-constant Delta family, and every truncated Delta slice misses the augmented chart.

For (1), the high h-coefficients give explicitly

\[
b=-3D,\quad a=2B-3E,\quad c=-BD+2C-D^3+3DE,
\]
\[
d=B^2+BD^2-4BE+3CD+3E^2.
\]

After these substitutions Q is constant in h: its h-linear coefficient cancels identically. Thus the upper-bound-only system retains Delta, whereas its attained-degree row makes `lambda=0`; together with `Z lambda−1` it gives −1. The symbolic identity and all four parameters are retained in the source controls. This is **PROVED-HERE: UNIT ON DELTA**, not a unit of the unrestricted chart.

A necessary caution is that the raw coefficient `[y^55]Q` need not vanish before the upper rows. For `h=y^33+y^22`, `h²` has y^55 coefficient 2 while its actual degree is 66. The obstruction is exact attainment after higher coefficients vanish, not a claim that every intermediate monomial is absent from every power of h.

**6. A stronger nondegeneracy theorem using the existing faces.** The complete source chart and its offset-zero outer D1 equations imply actual D2 faces

\[
F_{D2}=(\pi^3-1)^{24},\quad G_{D2}=(\pi^3-1)^{16}
\]

for (99,66), and `(pi⁴−1)²¹`, `(pi⁴−1)¹⁴` for D108. This needs checking for the outer remainders: a floor alone would allow them to change an equality face. On each outer equality band, write the face as `S(pi³)` or `S(pi⁴)`. The offset-zero D1 vanishing order at pi=1 exceeds `deg S`, so the whole equality face is zero. Exact Q matrix ranks for the four blocks are `11,11,8,11` and `9,9,7,9`, all full column ranks. [nondegeneracy-controls.json](/home/ubuntu/jc2/box/char-degree-20260905/nondegeneracy-controls.json) enumerates the actual sites and matrices. Thus these faces are already consequences at stage 0 and remain so through stage 8.

**Theorem B.** In either full coefficient chart, those actual source faces and an attained constant-target degree 55/63 exclude **every** point with `J(F,G)≡0`.

For completeness, the common-polynomial fact used in the proof is Lemmas 4–5, p5, of Arzhantsev–Petravchuk, [Closed and Irreducible Polynomials in Several Variables](https://arxiv.org/pdf/math/0608157): in characteristic zero, zero Jacobian in two variables implies `F=f(H),G=g(H)` for a polynomial H. This supplementary primary PDF is retained with SHA-256 `70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28`.

Here is the argument, independent of any solver. Let `k0=deg_y H`. Since `deg F=deg_y F`, also `deg H=k0`. The attained characteristic degree gives `k0 | gcd(n,m,D2)`, which is 11 or 9. Unique factorization of the two F top forms forces `deg f=9,k0=11` in the first case and `deg f=12,k0=9` in the second. Evaluate on the actual D2 covers `(t,z)=(s³,pi s⁴)` and `(s⁴,pi s⁵)`. The physical F valuations are −9 and −12. Hence H has negative valuation, so the highest power in f(H) strictly dominates all lower powers. The F face must be a ninth or twelfth power. Its actual root multiplicities are 24 or 21, neither divisible by 9 or 12. This contradiction proves the theorem. The full proof and source custody are [nondegeneracy-theorem.md](/home/ubuntu/jc2/box/char-degree-20260905/nondegeneracy-theorem.md).

Consequently, a verified proper **complete augmented ideal** over Q would, by extension of scalars and the weak Nullstellensatz, prove existence of a point over Qbar with `J` not identically zero. It would be an existential nondegenerate **necessary-chart survivor**, even if no coordinates were extracted. It would not be a Keller pair: its Jacobian may have degree up to 20/25. A timeout, a memory failure, or a partial coefficient construction proves no properness and supplies no such survivor.

**7. Gauge accounting and exact implementation.** The new drivers retain the full source coefficient map, its rational graph eliminations, every residual finite row, all five target scalars, and leader and separation inverse variables. No variable coefficient is inverted in graph elimination; only nonzero rational pivots are used. Unused free coordinates are recorded, and active-ring variants explicitly inject their ordered generators back into the full ring before interpreting a result. Their source h/D images and generator images are checked. All source target faces and the new characteristic target use coefficient-minus-target rows.

The beta=1 slice is justified by the residual simultaneous dilation

\[
F_\alpha=\alpha^{-n}F(\alpha x,\alpha y),\qquad
G_\alpha=\alpha^{-m}G(\alpha x,\alpha y).
\]

It preserves the placed directions and restored monicity and acts by `K(t,z)→K(t/alpha,z)`. Beta transforms as `beta alpha^−4` or `beta alpha^−5`, so over the algebraic closure it can be normalized once. Merely choosing a conjugate would not normalize beta; this repairs that explanation in the frozen D108 description. The new leader transforms as `lambda alpha^−143` or `lambda alpha^−153` and stays free. No simultaneous normalization of that leader, the minor separation, or the Jacobian scalar is made. [gauge-and-roster-audit.md](/home/ubuntu/jc2/box/char-degree-20260905/gauge-and-roster-audit.md) records the action.

For 99, the frozen full diagonal-translation proof supplies the `jet0=0` slice with its retained `minor_a2` or `v` coordinate. The total-degree/whole-top characteristic ideal is covariant under that translation with all target scalars and lambda fixed, so selected optimized runs use this existing slice. Every actual coefficient image and residual was transported; no other coordinate was pinned.

D108 requires care. Its three strict jets and the even at-level face do **not** support the same slice argument. An exact point of all frozen h3 stage-0 incidence rows, with `jet0=u=v=1,c=2`, translates to a forbidden pi-linear coefficient −2. The missing at-level mean would transform as `j3′=j3+q²u−2qv`; it is not a hidden coordinate of the frozen engine. Therefore no D108 jet0 pin was used. The negative control is [d108-translation-audit.json](/home/ubuntu/jc2/box/char-degree-20260905/d108-translation-audit.json).

A further audit found a coverage gap in the frozen zero-mean face itself: centering the generic polynomial without transporting the source arc does not justify that restriction. The supplementary corrected chart therefore retains a free `minor_mean=mu` and uses `−[(pi−mu)²−c]` for the h3 face, with `c≠0`; the F/G leading targets use `[(pi−mu)²−c]^12` and its eighth power. Every quadratic `−pi²+L pi+N` is represented polynomially by `mu=L/2`, `c=N+L²/4`. The leader −1 follows from the fixed top; distinct roots give `c≠0`. This uses no additional gauge. At mu=0 it recovers the frozen equations. The original requested runs and the supplementary mean-free stages0–8 are distinguished in the results. [d108-mean-coverage-audit.md](/home/ubuntu/jc2/box/char-degree-20260905/d108-mean-coverage-audit.md) proves the repair and records an exact negative control against the unsupported centering.

The D108 optimization instead changes only the polynomial coordinates used to compute the characteristic equations. For a bound N,

\[
T_q(t^r z^j)=t^r z^j(1+qt)^{N-r-j},\qquad T_q^{-1}=T_{-q}.
\]

It keeps the old minor variables and equations, uses `q=jet0`, transforms h in the characteristic expression, and reparametrizes the outer D/C spaces by their invertible coefficient maps. D2 floors and the complete finite D1 moment prefixes are stable in both directions; outer terms are inactive in the old stage-0–8 pole equations after the proved early reductions. The explicit inverse maps, generator round trips, h round trip, and vanishing transformed t¹ band were checked. This is an algebraic change of ring coordinates, not a claim of a translated source-chart slice. [d108-algebra-translation-audit.md](/home/ubuntu/jc2/box/char-degree-20260905/d108-algebra-translation-audit.md) gives the proof.

The first characteristic cancellations themselves provide useful reductions. With
`F=h³+A2 h+A3`, `G=h²+B1 h+B2`, all outer y-degrees below k, the high-degree equations force

\[
B1=-b/3,\qquad A2=(3B2+a)/2.
\]

Set

\[
H=h-b/6,\quad v=B2+a/3+b^2/18,
\quad V=A3-bB2/4+ab/12+b^3/54-c/2,
\]
\[
A=a+b^2/4,\quad p=d+bc/2-A^2/3,
\quad q=e_0+c^2/4-A(d+bc/2)/3+2A^3/27.
\]

Direct expansion gives

\[
Q=-2VH^3+(3v^2/4+p)H^2-3vVH+v^3-V^2+pv+q.
\]

Since `deg_y Q<2k`, monic division forces `V=3 quo_y(v²,H)/8`. Combining this with the actual source floors proves normalized B2 bands `r≤27` and A3 bands `r≤56` vanish for 99; the D108 cutoffs are 30 and 62. The proof uses the actual offset-zero equality maps, not coordinate names. D108's next band is allowed: `D31=tau z³¹(1+z)⁴`, `C63=3tau²z³⁴/8`; it is not arbitrarily set to zero. [front-band-lemma.md](/home/ubuntu/jc2/box/char-degree-20260905/front-band-lemma.md) and its exact controls prove these statements. When square divisibility yields a zero coordinate, the addition is explicitly recorded as a radical consequence preserving the algebraic set, not falsely called a linear ideal identity. Every original row is transported afterward. Further coefficient comparisons give `H0² | D_r³`; the low H-adic digit gives `H0³ | D_r⁴` where its band precedes the leader. These improve the stage0 cutoffs to **99 D≤29,C≤60; D108 D≤32,C≤66**. At positive stages the actual D1 weight190/277 matrices have full column rank11/9, giving **99 D≤30,C≤62; D108 D≤33,C≤68**. The next coefficient images are nonzero, so no stronger cutoff is inferred. The cubic, quartic, and stage-specific proof/control files are retained under the driver directory.

Two equivalent arithmetic backends were implemented. The first performs four exact monic divisions and tests `Q=E H+L`, with the upper H² digit zero, `deg E≤D2−k`, its whole leading face subtracted, and `deg L≤D2−1`. The second avoids expanding those quotient substitutions. Put `U=8V/3`, retain every high-y coefficient of `Rraw=v²−UH` as an equation, and let R be its part of y-degree below k. Modulo those equations,

\[
Q=(3R/4+p)H^2-vUH/8+vR-9U^2/64+pv+q.\tag{4}
\]

All coefficients above the required total degree and the whole leading target in (4) are imposed. In normalized form U is `(8/3)Vn/t`, checked as an exact monomial division. With ambient bound `6k−2`, the whole target occurs at t-depth 141 or 151. These shifted numbers represent the same physical conditions as 143/153 in the original normalization. No quotient remainder is replaced by a support cap. The final coefficient-graph backend gives fresh variables to intermediate coefficients, retaining every monic defining equation, every high-remainder equation, and every required Q coefficient. Its acyclic graph projects isomorphically to the preceding ideal. Product bounds retain exactly the t-coefficients that can reach a tested row; all factors have nonnegative t-exponents. Independent elimination and 64 exact-Q support controls verify this, including empty remainders and the pH² boundary. It emits a complete explicit ideal without expanded quotient or product substitutions.

Independent symbolic controls verify (4), the shifts, localization, ring maps, and target subtraction. A positive control deliberately outside the actual D2 chart uses a degree-11 homogeneous s and `h=s³−s²+s−1`, `v=s²`, `U=s+1`, `p=−5/8`. It has actual characteristic degree55 and leader−1/4. The correct target gives a proper ideal; replacing the leader target by1 gives a unit. This control proves the emitter does not kill attainment indiscriminately. It is not counted as a survivor of either source branch. A Singular rational-expression parser failure found during development was corrected using rational-prefix serialization; those failed startup outputs are quarantined and never counted as mathematical results.

**8. Finite schedule and decision status.** COMPUTATION-CLOSEOUT-PENDING. The required schedule consists of stages 0–8 on each 99 branch and D108 delta3, over exact Q. Every primary result must be tied to its script and input hashes, include the full characteristic block, and pass parser and positive/negative controls before being read as unit or properness. A unit additionally requires independent replay, the gauge and derived-face audit, and the leading-target subtraction check. Resource-bound attempts remain typed OPEN. The completed table, selected optimized attempts, custody manifest, and owned-worker termination receipt will replace this paragraph before sealing.

**9. Uniformity, and why this is not a cheap replacement for Keller.** Theorem A supplies exact attained-degree and scalar-unit rows for every effective characteristic index of every realized datum in Moh's setup. For a realized two-point parent, Proposition 4.3, p166, forces an index `M_s=n−2`: otherwise the top would have one linear factor. The p172 argument then supplies actual total degrees for every effective characteristic polynomial in those same coordinates. Earlier homogeneous faces are powers of the common form; the last face has its own source formula and cannot be copied from the earlier indices.

There is no uniform small-depth bound. The recursive defect is `M_(i+1)−M_i`, which can be large. Moreover, imposing the full compatible sequence essentially restores the Keller obstruction on these unequal two-point tops. Here is a direct algebraic explanation. Suppose the scalar target recursion has the Proposition-3.1 weight restriction and its equality term omits the latest characteristic factor, and every composed `H_i=T_i(G,F)` has actual total degree D_i. Induction gives

\[
\deg((\partial_U T_i)(G,F))=D_i+M_i.
\]

The derivative of `T_i^n_i` has degree `n_iD_i+M_i`. Every lower term has smaller derivative degree; an equality-weight term differentiates only an earlier factor, whose M-index is smaller. Thus there is no cancellation of that nonzero derivative leader. The chain rule at the last effective index gives, if J is nonzero,

\[
\deg J\le n-M_s-2=0.
\]

The zero case is also excluded uniformly for unequal two-point tops. A common polynomial generator would have degree dividing `gcd(n,D1,…,Ds)=gcd(n,M1,…,Ms)`, which divides2. Degree1 yields one top linear factor; degree2 with exactly two top factors yields equal multiplicities. Both contradict the given unequal top multiplicities. Therefore the **full compatible all-effective-degree chart forces a nonzero constant Jacobian**. This theorem, with its hypotheses and proof, is [full-characteristic-keller-theorem.md](/home/ubuntu/jc2/box/char-degree-20260905/full-characteristic-keller-theorem.md). It is not applied to the present T2-only runs as if T3 had been imposed.

The supplementary residual roster was independently copied and mechanically checked against its own receipt. Its hash is `c1c3b86fa7a19c0ff059aaac8da6fd5b1809911603c34cbe0414c7148efe2e8b`. Filtering `source.u_s≥2` gives **20 parents and 36 typed ES leaves**, with every `leaf_count` equal to its actual array length. This differs by two from the prose count38 in the task/prior report. No missing leaf was invented and no ledger was edited. [instrument-manifest.json](/home/ubuntu/jc2/box/char-degree-20260905/family-c/instrument-manifest.json) recomputes each parent's degrees and recursive defects; the latter range from7 to320. R012 is the D108 delta3 parent; R015 contains the two 99 branches.

These records are necessary tower configurations, not polynomial pairs, and their children are marked prefix-only. Uniform necessity belongs to a realized **parent coefficient lift**. Applying it to a typed ES leaf requires that lift and the actual transport of the rows. The labels alone supply neither a child Keller hypothesis nor attainment of omitted characteristic polynomials. Thus the instrument is uniformly available at the parent level, excludes the identified degeneracy in the clients proved above, and does not automatically produce 36—or38—leaf kills.

FINAL-CLOSEOUT-PENDING.

