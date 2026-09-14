# Frozen core census audit (auxiliary lane notes)

Source: `/tmp/jc2-lane.94eJYj/inputs/moh_skeleton_full.py`, SHA-256 `d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2`. All line references below address this frozen copy. No existing files modified.

## Results

`census(n, Kmin=16, full=True)` for **1 <= n <= 200** produces **23,720 numerical V-assignment rows, 14,016 global groups** `(n,m,M_2..M_s,V_s)`. With only Kmin relaxed to 2: **24,063 rows, 14,356 groups**. Hence 343 additional rows, 340 additional groups. The smallest K that can have a strict divisor chain ending at least 4 is 8; Kmin = 1, 2, 4 or 8 yield identical outputs. There is no s<=5 filter. Baseline depth distribution is s=3: 1,677; s=4: 10,464; s=5: 9,746; s=6: **1,833**. Every s=6 row is at n=192.

The extra rows are **not coverage leaks** once GGV Corollary 6.6 is admitted: all have K<16, forbidden for every realized counterexample, not merely a specially minimized one. No claim that any extra numerical row is realized is made. The 343 rows are grouped by K as follows: K=8:48; K=10:68; K=12:134; K=14:33; K=15:60. The n<=100 baseline count is 592 and the Kmin-relaxation adds 66 rows (658 total); this numerical surplus relative to Moh's table has no bearing on coverage.

The first Kmin-relaxation row is n=36,m=24,K=12,s=3, `(M_2,M_3)=(16,34)`, `(V_2,V_3)=(1,3)`, global major exponent u=9. It passes all implemented Moh (1)–(13) tests but violates the additional all-degree GGV K>=16 theorem. The first s=6 baseline witness is n=192,m=128,K=64, `(M_2,...,M_6)=(-96,-80,-72,-36,190)`, `(V_2,...,V_6)=(1,24,12,6,3)`, u=48. It witnesses implementation of s=6; it is only a numerical row.

The row postcheck found zero duplicate rows, zero failures of `windows_ok`, zero failures of independently reevaluated `full_ok`, zero nonintegral u, zero failures of K/2<u<K, zero failures of `A_1 | ((e+d)V_2-1)` across all 24,063 rows. `any10` is absent on 4,749 baseline rows and 277 Kmin-relaxation rows; that function is **not called** by census/full_ok.

## Exact core condition map

| Frozen code | Condition actually imposed | Printed correspondence and class |
|---|---|---|
| 154,158 | K>=Kmin, default16 | No Moh search item. **A (auxiliary GGV Cor6.6)** at default16. User-chosen larger Kmin is a domain restriction, not automatically proved. |
| 158–161 | K divides n; e=n/K>=3; K<=floor(n/3) | Search (1),(2),(5), **A after C orientation/minimality**. This is exactly compatible with 2<=d<e and gcd(d,e)=1. The e<3 guard duplicates the outer upper limit. |
| 147–152,162,164 | Nonempty strict divisor chain K>d_3>...>d_s>=4, each divides previous; s>=3 | Search (4),(5),(6). **A**: characteristic-gcd definitions, Prop5.5 s>=3, Cor6.1 d_s>=4. No upper bound on chain length. |
| 163 | d_1=n,d_2=K, d_{s+1}=gcd(d_s,n−2) | Search (5) and M_s=n−2 in (2), **A**. In particular d_{s+1}=gcd(d_s,2), automatically 1 if d_s odd and 2 if even. No parity case is excluded. |
| 167–169 | m=Kd, integer2<=d<e, gcd(d,e)=1 | Search (1),(2),(5), **A after C**. `d=1` means m divides n and is removed by minimality; d<e chooses m<n by target swap. The gcd is exact since K=gcd(m,n). |
| 170 | M_1=−m, M_s=n−2 | Search (1),(2), characteristic-data convention and promoted First-Separation/normalization hypotheses. **A in the normalized setup**. |
| 171–177 | Every intermediate M_i integer, M_{i−1}<M_i<n−2; gcd(d_i,M_i)=d_{i+1} | Search (4),(5), **A**, characteristic data. The terminal prev<n−2 duplicates the half-open range if s>=3. No positivity bound on M_i. |
| 180–181 | `with_V=False` bypasses all V/radius tests | Diagnostic projection, not the operative enumeration; cannot be called the full screened census. |
| 182 | V_{s+1}=d_{s+1} | Def5.1 initial characteristic normalization; **A**. |
| 189–191 | integer V_i> d_i/(n−M_i), V_i<=V_{i+1}d_i/d_{i+1}; V_i>=1 | Search (7), Def5.1(2), **A**. Since the lower bound is positive, max(w0,1) is redundant. Integer division in hiQ is exact because d_{i+1}|d_i. |
| 198 | V_s<d_s | **A**, two distinct top roots and Lem5.3 / Sect6 p194 setup (not an n<=100 or s<=5 consequence). Combined with (7), d_s/2<V_s<d_s. |
| 184,193–194,200,202–204,210 | Def5.1 rational radii; LCM and reduced denominator A_j | Search (8), **A definitions**. Fractions preserve exactness. Denominator in R update is strictly positive from V_i(n−M_i)>d_i and M_{i−1}<M_i. |
| 195–196 | Q=TRI A+SQ, retain V_i<=TRI **or** V_i≡SQ modA | Search (9)–(11), **A**, from the printed cover automorphism tbar↦omega tbar, not a bounded-search approximation. Applied at i=s−1,...,2. No branch selection imposed. |
| 205–208 | (A1|eV2 and A1|dV2−1) OR (A1|dV2 and A1|eV2−1) | Search (12),(13), **A**, Prop5.5 proof. Both complete conjunctive alternatives retained. |
| 71–82,84–140 | Object recomputations `windows_ok`, A/L, div9, cond1011, cond1213, full_ok | Same formulas as recursion; they are diagnostics/postconditions rather than extra hidden filters. `u=V_s K/d_s` is computed, not additionally filtered; integrality follows from d_s|K. |
| 137–140 | `any10`: at least one level admits numerical (10) | Exposed helper only. **Not imposed** by census, full_ok, groups_of or count_only. The source comment describes the Prop5.6 remark; do not silently turn that into a census filter. |
| 154 versus215 | No n upper limit or s upper limit in census | Search (1)'s n<=100 and (6)'s s<=5 are **B and absent**. `n` is a function argument; the campaign's n<=200 is an openly declared finite coverage range. |

There is no additional gcd/parity test in the core. In particular d_s odd/even is handled only by `gcd(d_s,n−2)`, and there is no explicit “K is composite” filter: the nonempty divisor chain ending >=4 forces that property where appropriate. No implicit n<=100-specific chain bound exists.

## GGV source justification for Kmin

The legacy upstream `box/moh_skeleton_N.py:284` attributes `K>=16` to GGV Cor6.6; the frozen file's `control_4` lines313ff explicitly distinguishes the “no GGV K>=16” comparison domain. Checked auxiliary source (not one of the seven charged frozen inputs): `refs/guccione_valqui2017_ja471_shape_counterexamples.pdf`, SHA-256 **8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60**. It is an author manuscript with its own printed page numbers. PDF p2 defines B as the minimum of gcd(degP,degQ) over **all counterexamples**; Cor6.6 on p34 states B>=16; the proof is on p35, using Prop6.5 and Cor5.21. Therefore every realized counterexample has K>=B>=16. This does not assume that the campaign's minimum degree or minimum degree-sum counterexample minimizes gcd. Rendered and visually inspected `core-ggv-p2.png`, `core-ggv-p34.png`, `core-ggv-p35.png`.

## Exhaustiveness argument for these core loops

Given any datum already satisfying the normalized all-degree conditions, take K=gcd(n,m), e=n/K, d=m/K. GGV puts K>=16; 2<=d<e puts e>=3 and hence K<=floor(n/3), so the outer loops visit its K and d. Its strict characteristic-gcd sequence is one of the recursively generated nonempty chains, with no artificial depth cap. Its increasing integer M values are visited by every Mrec interval and exact gcd gate. Descend from i=s: its actual integer V_i belongs to the inclusive upper/strict lower candidate interval, its top multiplicity is <d_s, and each necessary printed disjunction keeps its branch. The running R and LCM equal Def5.1's products/LCMs by induction; hence the intermediate and bottom denominator gates calculate the printed A values. The row is yielded. This is the algorithmic portion of a coverage theorem; the root report must separately establish that the operative full-tree/ODE/Xu filters are necessary on the realized data being quantified.

## Rest of frozen file: no hidden core filters

Lines217–416 are a published-row table and controls. They run only through `run_controls`; they do not change census output. Some controls use restricted n intervals (48..90,48..75,4..100 etc.) to compare algorithms; those intervals are not global conditions. `control_4` only prints the excess over Moh's final table and does not assert equality to it. No theorem may be inferred from reproducing that finite table.

`groups_of` groups rows by `(m,Ms,V_s)` and appends `(V_2,q,u)`, with default Kmin16/fullTrue. It does not delete any row. `q=(1−delta1)de/(d+e)` is computed only.

The integration rerun functions have additional **conditional** outputs, separate from the all-degree row census:

* `uni_hits`: tests N=k V2 q, integer k>=1, k V2<=u, integral N>=Nlo, optional N<=Nhi. The docstring expressly assumes UNI (one Galois orbit). This is not a universally necessary test absent that hypothesis.
* `mixed_hit`: tests sums of candidate `(v,q)` with total v<=floor(u), Nlo<=integer sum(vq)<=Nhi. The default Nlo=6/Nhi=16 is the campaign H2 window, not Moh (1)–(13). It drops candidate/partial sums above Nhi under positivity; values are positive here because Def5.1 makes 1−delta1 a product of positive quantities. CAP=60000 is a memory truncation per layer, marked capped. `rerun` retains every capped group (`hm or c`), hence caps weaken deletion rather than exclude a possible group. `do_mixed=False` substitutes UNI for the mixed test and remains a separate conditional computation.
* `rerun` defaults degrees48..120; `listing` restricts only which survivors are printed in detail. `count_only` counts unfiltered groups; CLI defaults48..120 describe the chosen run window. The current task's n<=200 is provided by the audit driver.
* The controls describe an inferred Moh delta1 typo at n75. They are diagnostics; that special-row logic is not imposed on arbitrary census rows.

Reproducible artifacts: `core-count.py`, `core-count-summary.json`, `core-count.log`, full row file `core-rows-kmin2.jsonl`, `core-audit-rows.py`, `core-audit-rows.json`. Count driver imports only the frozen file and calls its census; it never modifies that source. No files outside the authorized lane output directory were written.
