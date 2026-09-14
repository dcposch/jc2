# Characteristic-degree instrument: resumed computation and sealed closeout

**Disposition: Theorems A/B remain established; the finite augmented-chart decision is COMPUTE-BOUND OPEN for both (99,66) branches and D=108 delta=3.** No production computation completed a verified unit or a verified proper augmented ideal. In particular, this report establishes neither the first non-truncation split-branch kill nor a nondegenerate necessary-chart survivor. The exact resource outcomes, acceptance checks, and worker termination appear in §8 and §10.

The attained characteristic degrees are **55** for (99,66) and **63** for (108,72). Their whole leading rows lie at normalized depths **143** and **153**. The full characteristic block excludes every identically-zero-Jacobian point once the actual D2 source faces are imposed. These mathematical conclusions survive the interrupted first run; they do not turn an unfinished Gröbner computation into a decision.

**1. Frozen custody, adoption, and disk discipline.** This resume uses receipt `xmodel/char-degree-instrument-astra-r2-20260905.run.v2`, frozen basis `fbeb47f6c0b1bdb0699b2e204f414e2271fddff9`, start 2026-09-05 23:12:44 UTC. Before reading the charged inputs, I mechanically paired the receipt's numbered `_sha256` and `_basename` fields with `awk`, built the manifest, and ran `sha256sum -c` against `/tmp/jc2-lane.01qCZg/inputs`. All six files passed. The manifest and replay transcript are [inputs.sha256](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/inputs.sha256) and [hash-check.txt](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/hash-check.txt). The charged first report hashes `f8821a7515f41879dad49455701ffc75b7e0980ae27cf9b6422e46e8c1d44e1a`; its unsealed and pending closeout is superseded here.

`fleet.sh ips` identified exactly the requested owned instance: **i-02703754668abed88**, IP **172.30.0.40**, Owner **char-degree-20260905**, type r7i.8xlarge. Adoption reached it at 23:13:08 UTC; live Singular processes and schedule parents were present. The local root had 1.2 GiB free, and the worker had about 22 GiB free. No worker tree or large CAS output was copied back. New evidence consists of small receipts/scripts under `box/char-degree-20260905/resume-r2/`, plus the explicitly requested final report. Large emitted scripts were hashed in place. No local write exceeding 10 MB was made. No ledger, `jc2-lean`, or `ideation-*` file was edited.

The 150-minute watch limit was September 6 01:42:55 UTC, within the 180-minute ceiling at02:12:44 UTC. Existing stages finished naturally under their individual limits, with status polls every ten minutes. A five-second `/proc` monitor additionally preserved observed memory high-water values without changing CAS commands.

Sections2–6 reuse the charged statements/proofs and inherited source custody. Fresh exact-Q controls rechecked degree arithmetic, actual equality-face ranks, the depressed identity, support cutoffs, and monic-remainder equivalence. All four JSON outputs exactly equal their inherited outputs. [fresh-math-controls.json](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/fresh-math-controls.json) binds script hashes, output-path redirection, rc, wall, and output hashes.

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

The canonical implementation takes the monic approximate root of the target resultant before composition. The runs instead retain every permitted target monomial existentially; this is a necessary enlargement. Such a member is a family representative, not an independently certified canonical `T_i`.

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

All five lower target coefficients remain. Four are recovered with rational monic pivots from high y-coefficients, retaining every unselected row. The positive-degree rows leave `e0` free; only the canonical resultant construction determines it.

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

After eliminating the four high h-coefficients, Q is constant in h, including an identically canceled h-linear term. Thus the upper-bound-only system retains Delta, but exact attainment forces `lambda=0`, contradicting `Z lambda-1`. This is **PROVED-HERE: UNIT ON DELTA**, not a unit of the unrestricted chart. The fresh source-arithmetic control retains all four Delta parameters.

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

**7. Coverage, rings, and acceptance rules applied in this resume.** Production rings are over Q, with ordered coefficient/graph variables and Singular order `dp`. They contain no physical `t,z` after coefficient extraction. Custody records bind the actual ring declaration, ordered-generator count/hash, and explicit source/input maps; complete generator lists remain in worker metadata.

All five target scalars remain; `e0` is free. Source graphs use rational pivots only. Added graph variables have monic acyclic definitions, whose elimination gives an isomorphic quotient. Every original residual row is transported. Radical front consequences preserve the algebraic set, rather than being asserted as linear ideal identities.

The beta=1 convention spends the residual simultaneous dilation once:

\[
F_\alpha=\alpha^{-n}F(\alpha x,\alpha y),\qquad
G_\alpha=\alpha^{-m}G(\alpha x,\alpha y).
\]

It acts by `K(t,z) -> K(t/alpha,z)`. Beta has scaling weight 4/5, while the characteristic leader has weight 143/153 and remains free and nonzero. Neither separation nor the Jacobian scalar is additionally normalized. Choosing a root conjugate by itself would not justify beta=1.

For both 99 branches, the audited diagonal translation permits `jet0=0`; the retained separation and remaining minor coordinates are transported, and the full chart is recovered with the free translation parameter. The characteristic family and whole homogeneous target are covariant under that action. The source localizers are the nonzero branch-separation variable (`rho` on delta2, `c` on delta5/2), expressed in each declared ring, together with `Z55*leader55-1`. The complete actual row strings are retained in the custody JSON.

D108 needs two separate chart labels. **The inherited mean-zero chart is a restricted chart with an unresolved universal-coverage justification.** Its even quadratic face cannot be centered without transporting the physical source arc. A unit confined there would exclude that restriction only. The repaired chart retains `minor_mean=mu` and has h3 face `-((pi-mu)^2-c)`, F/G target powers 12/8, and `c != 0`. Every quadratic `-pi^2+L*pi+N` is represented by `mu=L/2`, `c=N+L^2/4`; no additional gauge is spent. This is the chart needed for a full D108 branch-exclusion claim. Its localizers are the separation inverse times `c` minus one and `Z63*leader63-1`.

The algebraic D108 translation used in the ordinary circuit runs changes polynomial presentation while retaining the original minor equations. It is not an unsupported source slice. A later retained theorem additionally permits `jet0=0` **on the repaired free-mean chart**: under translation by q,

\[
j_0'=j_0-q,\quad u'=u,\quad v'=v-qu,\quad
\mu'=\mu+q^2u-2qv,\quad c'=c.
\]

Taking `q=j0` keeps the full mean and has an explicit inverse. The source prefixes, actual coefficient maps, and characteristic rows are transported; the full chart is the slice times a free affine coordinate. This licenses the separately labeled optimized free-mean/jet0 stage-8 attempt, while leaving the inherited mean-zero caveat intact. The proof and control are [d108-meanfree-translation-theorem.md](/home/ubuntu/jc2/box/char-degree-20260905/d108-meanfree-translation-theorem.md) and its adjacent exact-Q control receipt.

The derived-face audit uses the actual offset-zero D1 moment matrices from §6, not a floor interpreted as equality. The stronger front cuts are: 99 stage0 `D<=29,C<=60`, stages1–8 `D<=30,C<=62`; D108 stage0 `D<=32,C<=66`, stages1–8 `D<=33,C<=68`. The next possible band is retained with its scalar tau, including tau=0. No stronger cutoff, inversion of tau, or vanishing leader is inferred. The cubic, quartic, stage-specific and input-map proofs are hash-bound in the audit artifacts.

Set `H=h-b/6`, `v=B2+a/3+b^2/18`, `U=8V/3`, with V,p,q as in charged §7. If `Rraw=v^2-UH` and R retains its y-degrees below k, then modulo **all** high-y remainder rows,

\[
Q=(3R/4+p)H^2-vUH/8+vR-9U^2/64+pv+q.
\]

The difference from the unshortened Q is `(Rraw-R)*(3H^2/4+v)`; monicity recovers the high-remainder rows with pivot3/4. Exact product cutoffs cannot lose a tested coefficient because t exponents are nonnegative. The 64 controls include empty R and the `pH^2` boundary. Circuit normalizer `6k-2` puts its targets at **141/151**, the same physical rows as **143/153** in normalizer `6k`.

The leading-target check requested as **17(rrrrrrrrr)/(nnnnnnnnn)** was applied substantively to both kinds of leading rows. Those literal labels do not occur in the frozen reports, so no source location for them is invented. At a source leading pole tag the equation is **coefficient minus the complete forced target**; strictly lower tags retain zero targets:

| Source branch | F local power and target | G local power and target |
|---|---|---|
| 99 delta2 | 81; `(zeta^2*(zeta+3rho))^9` | 54; `(zeta^2*(zeta+3rho))^6` |
| 99 delta5/2 | 189; `(pi*(pi^2-c))^9` | 126; `(pi*(pi^2-c))^6` |
| D108 inherited mean zero | 96; `(pi^2-c)^12` | 64; `(pi^2-c)^8` |
| D108 repaired free mean | 96; `((pi-mu)^2-c)^12` | 64; `((pi-mu)^2-c)^8` |

Stages0–8 do not reach those source leading powers, but their emitter convention was audited; the old coefficient-equals-zero defect cannot be counted as a unit. Independently, the new characteristic block subtracts every coefficient of `lambda*z^40*(1+z)^15` or `lambda*z^49*(1+z)^14`. That means 16/15 binomial target subtractions, with the correct sign and exact positions, plus the leader inverse row. The complete characteristic block is adjoined at every stage. Passing the source pole check alone would not check this new block.

Before reading any unit or properness, acceptance requires unchanged script and input hashes, exact Q and declared ring order, complete row counts, `ALL_ROWS_PARSED`, the completed solver-result delimiters appropriate to that driver, rc0, no parser/CAS errors, exactly parsed result fields, and the completed localization control vector `[0,1]`. Both separation and leader localizers were also tested independently in the actual declared rings. No `sat()` list wrapper is interpreted as an ideal; these presentations use explicit inverse equations. Unit additionally requires independent exact-Q replay and all coverage, gauge, derived-face, and target checks. Properness of a complete validated ideal invokes §6, with the stage and chart explicitly stated.

The inherited toy v2 control metadata used an older emitter hash. This resume regenerated and replayed positive and wrong-target controls with the actual current v1/v2 emitters and the selected `slimgb` presentation. These fresh toys use `k=2`, target degree3, and return the expected proper/unit pair with rc0, clean parsing, and controls `[0,1]`. A separate inherited degree55, leader `-1/4` control deliberately fails the actual D2 source faces. **These are backend controls, not source-chart survivors.** The fresh controls, strict parser checks, per-stage target checks, and source-map custody are linked in §8.

The production backends place their inline controls after the expensive Gröbner call. Bounded attempts therefore do not contain a completed inline-control/result block. External control success is useful construction evidence, but cannot supply the missing production completion. Such runs remain OPEN even when every source and characteristic row has parsed successfully.

**8. Reissued finite schedule and decision table.** All36 main circuit attempts reached complete emission and `ALL_ROWS_PARSED`. None reached a complete accepted result/control block. Each cell is **status+rc; recorded elapsed seconds; RSS GiB**: T=COMPUTE-BOUND OPEN, M=MEMORY-BOUND OPEN. Both clients' times include emitter/build overhead; build times are separately retained. A dash means RSS was not captured. An inequality is the observed `/proc` VmHWM through the last sample, rounded downward, hence only a lower bound on final peak RSS. The 16 GiB address-space caps are not substituted for RSS.

| Stage | 99 delta2 | 99 delta5/2 | D108 mean-zero restriction | D108 repaired free mean |
|---:|---|---|---|---|
| 0 | T1; 601.6; — | T1; 601.2; — | M14; 587.8; — | T1; 600.8; — |
| 1 | T1; 601.5; — | T1; 601.1; — | M14; 605.4; — | T1; 600.8; — |
| 2 | T1; 601.4; — | T1; 601.1; — | M14; 843.7; — | T1; 600.8; — |
| 3 | T1; 601.4; — | T1; 601.1; — | M14; 844.1; — | T1; 600.7; — |
| 4 | T1; 601.3; — | T1; 601.0; — | M14; 848.4; — | T1; 600.7; — |
| 5 | T1; 601.4; — | T1; 601.1; — | T1; 900.8; — | T1; 600.7; — |
| 6 | T1; 601.3; ≥11.16 | T1; 601.1; ≥11.09 | T1; 900.8; ≥15.01 | T1; 600.7; ≥10.06 |
| 7 | T1; 601.3; ≥11.16 | T1; 601.0; ≥11.12 | T1; 900.7; ≥14.87 | T1; 600.6; ≥10.17 |
| 8 | T1; 601.3; ≥11.21 | T1; 601.1; ≥11.11 | T1; 1800.9; — | T1; 600.6; ≥10.18 |

Every stage's script, input, emitter, source-map, ordered-ring and output SHA-256 is bound in [99 custody](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/audit-99.json) and [D108 custody](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/audit-d108-custody.json). These retain exact row counts, localizer strings, ring order and target checks. Ring/block sizes are: 99 delta2: 2537–2912 generators, 1280–1389 characteristic Q rows; 99 delta5/2: 2535–2910 generators, 1280–1389 characteristic Q rows; 108 mean zero: 2495–2906 generators, 1144–1256 characteristic Q rows; 108 free mean: 2520–2931 generators, 1144–1256 characteristic Q rows. A zero residual-source-row count after graph elimination does not mean original source conditions were dropped; their images and rational pivots are separately audited.

Selected stage8 alternatives also remained OPEN. The 99 delta2 `slimgb` run ended rc1 at1200.467s; the delta5/2 active-front run ended rc1 at1801.169s; the delta5/2 remainder run failed for memory at1215.298s. Their peak RSS was not captured. D108 `meanfree_jet0_stage8_slimgb`: rc1, 1200.517s, observed HWM ≥15.4 GiB, OPEN; `meanfree_stage8_slimgb`: rc1, 1200.417s, not captured, OPEN. No selected run supplies a branch kill or proper ideal.

The final historical inventory is [status-catalog-final.json](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/status-catalog-final.json). It includes the older normalized/active/construction attempts and quarantined startup failures. Stale `RUNNING`, `EXPANDING_FULL_CHARACTERISTIC`, or `EMITTED_NOT_DECIDED` metadata is reconciled against the final process inventory; it proves no solver completion. Some legacy `CAS_ERROR_OPEN` records are memory failures during construction, not parser failures. No control result or administrative `CLOSED` receipt is promoted to a production verdict.

Fresh emitter and all-production-ring inverse controls pass. The independent [final strict reader](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/strict-acceptance-production-final.json) binds39 actual production outputs: **34 time-bound,5 memory-bound, zero complete clean unit/proper candidates**. Its controls reject incomplete markers, wrong control vectors, and a real malformed Singular script that exits rc0. Production inline controls never completed after the bounded Gröbner calls, so acceptance stops at OPEN.

**Per-client verdict:** (99,66) delta2 — **compute-bound OPEN**; (99,66) delta5/2 — **compute-bound OPEN**; D108 delta3 — **compute-bound OPEN**, including the coverage-repaired free-mean chart. No independent unit replay or coordinate extraction was triggered because no production unit or proper candidate existed. If a complete validated ideal had been proper, the charged typing would be **PROPER — EXACT-Q-PROPER-AUGMENTED-IDEAL: an existential nondegenerate necessary-chart survivor over Qbar**, even without extracted coordinates. That event did not occur here.

**9. Uniform scope retained from the charged report.** Theorem A applies at every effective index of a realized parent, without a uniform shallow-depth bound. These T2-only runs do not impose the next characteristic degrees145/227. The supplementary roster's checked20 parents and36 typed ES leaves remain necessary configurations with prefix-only children; no omitted leaf is invented. Labels alone supply neither a child Keller hypothesis nor the coefficient lift transporting attainment rows.

The stronger theorem forcing a nonzero constant Jacobian requires the full compatible sequence of effective characteristic polynomials and its target-recursion restrictions. It cannot be applied to the present computations as though T3 had been imposed. Here a validated proper point could still have nonconstant Jacobian of degree at most20/25.

FALLACY-v2 was checked before classification. Attainment has its theorem; actual faces have their source-map audit; leader subtraction, zero cases, declared rings and rational graph maps are explicit. Normalizer depth is distinguished from stage number. No new exit-price assertion is made, so no `charge_basis=` line applies. The finite branch decision remains typed OPEN.

**10. Worker termination, final custody, and seal.** The23:33:08 UTC poll found no remaining solver/schedule jobs. All final output hashes were harvested before termination. After rechecking the instance ID, IP and Owner, I executed `bash ops/fleet/fleet.sh term i-02703754668abed88` at23:34:31 UTC. It returned rc0 and `shutting-down`; AWS confirmed **terminated** at23:35:11 UTC, before this report was sealed. [termination.json](/home/ubuntu/jc2/box/char-degree-20260905/resume-r2/termination.json) and the adjacent `termination-state.json` record both observations.

Large scripts/outputs stayed on the worker; only their hashes and small custody records were retained locally. The final evidence manifest, `box/char-degree-20260905/resume-r2/evidence.sha256`, has SHA-256 **77a38f0bd31d41cab35f4b164419973094b342a83ae7e621a2ccdb545afbbcc9** and binds62 retained artifacts. Its entries were mechanically checked before sealing. The final finite outcome is OPEN; Theorems A/B and the exclusion of every zero-Jacobian point on the attained actual-face chart remain established.

<!-- BODY-END -->
