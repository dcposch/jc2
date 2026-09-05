# Census coverage at all degrees: audit through n = 200

**Verdict: COVERAGE THEOREM for normalized minimal-counterexample data.** Neither bounded-search clause is imposed by the frozen enumerator; `Kmin=16` has an independent all-degree justification. The operative conditions are necessary with the centre argument given below. **1,420 is before Xu; the original conjunction has 1,377 rows. Coverage leaks: 0.** This is containment, not realization or elimination.

Work over an algebraically closed characteristic-zero field. A non-coordinate Keller pair minimal in total-degree sum, put into the promoted First-Separation setup and the normalizations below, has every resulting major-tower row at `n<=200` in `census(n,Kmin=16,full=True)` and surviving the original operative conjunction. All necessities are independent of 100 and 200. Arbitrary larger `Kmin`, optional UNI/H2 filters, and unnormalized or descended presentations are outside this statement.

**Custody.** Before substantive inspection, an `awk -F=` join of the receipt's `charged_input_<i>_basename` and `_sha256` fields under `lane_inputs_dir` produced [input-manifest.sha256](../box/census-coverage-20260905/input-manifest.sha256). `sha256sum -c`: **7/7 OK**. Charged reads used `/tmp/jc2-lane.94eJYj/inputs`. No ledger, `jc2-lean`, or `ideation-*` file was edited.

Moh citations are **printed pages**, PDF ordinal = printed minus 139. The decisive renders were visually read: [p. 200](../box/census-coverage-20260905/root-moh-61.png), [p. 201](../box/census-coverage-20260905/root-moh-62.png). Supporting pages for every proposition below were also rendered; images control over incomplete OCR. Primary PDFs: [Moh](../refs/moh1983_jram340_configurations_of_roots.pdf), [Xu](../refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf); Xu uses its own page numbers.

The operative code is auxiliary to the charged inputs: five implementations were snapshotted and hashed in [op-aux-inputs.sha256](../box/census-coverage-20260905/op-aux-inputs.sha256). Replay imports those snapshots and the charged core. GGV is declared separately below. Prior reports located claims and code; promotion labels were not used as proofs.

**The two printed lists differ.** P.200 **Theorem (1)–(7)** assumes degree equals y-degree and characteristic data, then constructs major towers, classifies successors, bounds their number, and requires a major successor. Its proof cites Props. 5.4 and 6.1. After the proof Moh introduces the application below degree 100: “We shall search for the sequences of integers.” Search (1) explicitly has `n<=100`. Immediately before search (6), p. 201 says, “A simple computation shows that s<=5.” These are the precise lines forbidding promotion of the entire search list as one all-degree theorem.

**A** = all-degree necessity/definition with the stated setup; **B** = bounded-search clause; **C** = change of representative by a stated group element. Mixed items are split. A Galois symmetry proving necessity is A, not a choice of representative.

| Printed search item | Clause-by-clause classification and source |
|---|---|
| Preface: `f=T_1^psi` | **C.** Prop. 2.2 and p. 185 give `T_1^psi=f+H(g)`. Use the target automorphism `(U,V)->(U+H(V),V)`. The generated algebra and Keller condition are preserved. |
| **(1)** `m=-M_1<n<=100` | `m=-M_1`: **A**, characteristic convention after the preceding C, p. 150 and p. 185. `m<n`: **C**, orient the target coordinates and cancel equal leading degrees if needed. `n<=100`: **B**, the explicitly bounded application. |
| **(2)** `m` does not divide `n`; `M_s=n-2` | Nondivisibility is **A for a minimal representative after C**: if `n=km`, the top Jacobian identity gives `g_n=c f_m^k`; `(U,V)->(U,V-cU^k)` reduces degree. `M_s=n-2` is **A**, Prop. 5.4, Lemma 5.3, and the promoted First-Separation reduction, pp. 183–186/194. |
| **(3)** `J=1`; no simultaneous degree reduction | `J=1`: **C**, constant source/target scalings. No simultaneous reduction: **A**, minimum total-degree sum; it excludes the automorphism alternative in Prop. 5.4 p. 183. It is not an integer test on skeletons. |
| **(4)** effective characteristic data “less than n-2” | **Literal wording defective**, not silently promoted. It includes `n` and `M_s`, while (2) has `M_s=n-2`. Safe **A replacement**: p. 200 Theorem(3), “largest one <=n-2,” with the p. 150 characteristic definition and p. 174 effective truncation excluding terminal `n-1`. This replacement proves the code's endpoint convention directly. |
| **(5)** `d_r=gcd(n,M_1,...,M_{r-1})` | **A**, the definition on p. 150. Each new characteristic exponent is the first outside the preceding divisibility lattice, so the gcd strictly drops. |
| **(6)** `3<=s<=5`, `d_s>=4` | `s>=3`: **A**, Prop. 5.5 pp. 186–188, excluding the two-effective-pair case; `s=1` is already incompatible with the FS endpoint. `d_s>=4`: **A**, Cor. 6.1 pp. 199–200 and p. 200's explicit smallest-degree conclusion. `s<=5`: **B**. |
| **(7)** `V_{r+1}d_r/d_{r+1} >= V_r > d_r/(n-M_r)` | **A**, Def. 5.1(2) p. 179 and Prop. 5.3 pp. 180–182; also p. 190's multiplicity-versus-degree display and Theorem(4),(7) p. 200. The right inequality selects a major successor. |
| **(8)** radii; `L`; denominator increment `A_{r-1}` | **A**, Def. 5.1(3) p. 179 and the definitions on p. 201. `L` is the LCM of upper reduced denominators; `A` is the reduced denominator of `L delta_{r-1}`. |
| **(9)** `V_r d_{r-1}/d_r = TRI A + SQ` | **A**, Euclidean division of the integer degree, `0<=SQ<A`. No degree/height hypothesis. |
| **(10)** `V_{r-1}<=TRI` for nonzero selected root | **A**, p. 201's explicit Puiseux action `tbar->omega tbar`, where `tbar^(LA)=t`, over the old field `k((t^(1/L)))`. A nonzero coefficient has an orbit of size A. |
| **(11)** `V_{r-1}=jA+SQ` for selected zero root | **A**, the same action: all nonzero roots contribute multiples of A, so zero multiplicity is the total degree modulo A. Positivity gives `j>=0`. |
| **(12)** `A_1 \| (n/d_2)V_2` and `A_1 \| (m/d_2)V_2-1` | **A as one alternative**, terminal Prop. 4.6, Prop. A.5, and the proof of Prop. 5.5 pp. 187–188, explicitly cited on p. 201. Valid at the bottom of an arbitrary tower. |
| **(13)** the exchanged pair of divisibilities | **A as the other alternative**, the same terminal argument. Both alternatives must be retained after fixing `m<n`; a coordinate swap does not license discarding one. |

The C operations can coexist: a generic linear source map makes both leading y-coefficients nonzero; output scalings make both polynomials monic. If the resulting Jacobian is c, precompose by `(x,y)->(x/c,y)`, preserving monicity and degrees and making `J=1`. Target swaps and triangular cancellations preserve the generated algebra. Centre normalization uses `(x,y)->(x,y-a x-b)` (inverse signs when substituting). No fractional Puiseux translation is treated as a polynomial automorphism.

Two all-degree implications deserve explicit proofs. Put `P=V_r d_{r-1}/d_r`. At level `r-1`, the increment subgroup fixes the previous centre and multiplies the new coefficient by a primitive A-th root of unity. Thus a nonzero root of multiplicity `v` uses `Av<=P` degrees; a zero root has multiplicity `v congruent P mod A`. These are exactly (10)/(11). The field statement is essential: the increment action fixes the **old 1/L lattice**, not just integer exponents.

At terminal `D_1`, Def. 5.1(4) invokes Prop. 4.6's constant differential equation for `g_sigma,f_sigma`, of degrees `N=(n/d_2)V_2`, `H=(m/d_2)V_2`. Prop. A.5 and the constant ODE give simple roots, no common root, and no common derivative root, as used on p. 187. Under the increment action each polynomial has exponents congruent to its degree modulo A. For `A>1`, neither residue can be nonzero simultaneously (common zero root), and both cannot be zero (common zero derivative). The remaining nonzero residue is 1 by simplicity. Hence `(N,H) mod A` is `(0,1)` or `(1,0)`. For `A=1` the tests are vacuous. This extends the **terminal argument**, not the special `s=2` reduction, to every height.

For (6), `n>=3d_2>=12*2^(s-2)`: hence `n<=100` gives `s<=5`, whereas `n<=200` permits `s=6`. The other clauses use minimality. [printed-audit.md](../box/census-coverage-20260905/printed-audit.md) completes the implicit `d_s=3` argument on p. 200: an explicit translation and Prop. 6.3 decrease both **total degrees**, and the birational inverse proves the image pair remains non-coordinate. No descended pi-degree is mistaken for total degree.

**Every implemented core restriction.** Line numbers here refer to the charged frozen `moh_skeleton_full.py`, not a later workspace edit. Write `K=gcd(n,m)`, `e=n/K`, `d=m/K`; this scalar d is distinct from the indexed `d_i`.

| Code condition / lines | Printed correspondence | Class and audit result |
|---|---|---|
| `K>=Kmin`, default 16; 154,158 | None in Moh's list | **A with auxiliary GGV Cor. 6.6** for 16; a larger user-supplied cutoff needs a separate theorem. |
| `K<=n//3`, `n%K==0`, `e>=3`; 158–161 | (1),(2),(5) | **A after C.** Reduced ratios satisfy `2<=d<e`. The explicit `e<3` rejection repeats the outer bound. |
| Nonempty strict divisor chains, every member >=4; 147–152,162–165 | (4) replacement,(5),(6) | **A.** Exactly `K>d_3>...>d_s>=4`, so `s>=3`. The recursion has **no length cap**. |
| `d_{s+1}=gcd(d_s,n-2)`; 163 | (2),(5) | **A.** Since `d_s\|n`, this equals `gcd(d_s,2)`: 1 for odd `d_s`, 2 for even. Neither parity is excluded. |
| `2<=d<e`, `gcd(d,e)==1`, `m=Kd`; 167–169 | (1),(2),(5) | **A after C.** `d=1` would mean `m\|n`; the gcd enforces exactly K, not a divisor chosen below it. |
| `M_1=-m`, `M_s=n-2`; 170 | (1),(2) | **A in normalized FS setup.** |
| `M_{i-1}<M_i<n-2`, exact gcd `gcd(d_i,M_i)=d_{i+1}`; 171–177 | (4) replacement,(5) | **A.** Every integer in the interval is visited, including negative values. The terminal `prev<n-2` guard is redundant. |
| `V_{s+1}=d_{s+1}`; 79,182 | Def. 5.1(2) | **A for the parent tower.** This is not automatically a convention for a descended child's truncated tower. |
| `floor(d_i/(n-M_i))+1 <= V_i <= V_{i+1}d_i/d_{i+1}`; 189–191 | (7) | **A.** Exact Fraction arithmetic implements the strict lower endpoint; the upper division is exact. `max(w0,1)` adds nothing. |
| `V_s<d_s`; 198 | Lemma 5.3 pp. 185–186; p. 194 FS | **A**, the two distinct top factors. Together with (7), `d_s/2<V_s<d_s`. It is stronger than (7)'s non-strict upper bound for a valid reason. |
| Product R, rational radii, LCM, reduced A; 184,193–194,200,202–204,210 | (8), Def. 5.1(3) | **A definitions.** Denominators stay positive because `V_i(n-M_i)>d_i` and `M_{i-1}<M_i`. No floating-point or denominator-size cutoff. |
| `w<=TRI or (w-SQ)%A==0`; 195–196 | (9),(10),(11) | **A.** Both root-location branches retained, at every `i=s-1,...,2`. |
| Full conjunction (12) **or** full conjunction (13); 205–208 | (12),(13) | **A.** Correct bottom index; the LCM includes `delta_2`. |
| `with_V=False`; 180–181 | No theorem filter | A diagnostic projection bypassing V tests. The coverage statement uses `with_V=True`. |
| `windows_ok`, `A`, `div9`, `cond1011`, `cond1213`, `full_ok`; 91–135 | Same tests | Re-evaluation, not additional hidden pruning. `full=True` in the generator performs the corresponding tests during recursion. |
| `any10()`; 137–140 | Remark after (13), Prop. 5.6 | **Not called** by `census` or `full_ok`. Its absence is missed numerical pruning, not a leak. Numerical permission for (10) is not an actual nonzero coefficient. |
| No upper n bound; no upper s bound | B clauses of (1),(6) | **Both B clauses absent.** `n<=200` is supplied by the audit driver as the theorem's explicit finite domain. |

No additional parity/gcd test occurs. `Skel.u` (82) is the **major capacity** `V_s K/d_s`, not `u_s=d_s-V_s`; it is computed, not tested. Existing arithmetic implies `delta_s=-1`, increasing radii `<1`, and Lemma 6.1's `delta_{s-1}>=0` (p. 194).

The rest of the file adds no hidden core filter. Lines 217–416 are tables/controls with test-specific ranges. `groups_of` preserves rows. `uni_hits` assumes one orbit and tests integral `N=kV_2q`, `kV_2<=u`, `N>=6`, optionally `N<=16`. `mixed_hit` uses H2's `[6,16]`, positive rational summands and total capacity; `CAP=60000` flags undecided groups, retained by `hm or c`. `do_mixed=False` substitutes UNI. CLI degrees 48–120 and the listing set are run/report parameters. **UNI and H2 are outside this coverage theorem**; their rerun output is not an unconditional census.

**Kmin.** Auxiliary [GGV](../refs/guccione_valqui2017_ja471_shape_counterexamples.pdf), SHA-256 `8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60`, defines B on manuscript/PDF p. 2 as minimum degree-gcd over **all counterexamples**; Cor. 6.6 p. 34 gives `B>=16` (proof p. 35). All three pages were rendered. Thus every counterexample has `K>=16`; no claim that minimum degree-sum minimizes gcd is needed. With only charged sources, use `Kmin=2`: all added rows also fail the justified operative tree through 200.

| Exhaustive run, `1<=n<=200`, `full=True` | Rows | Groups `(n,m,M,V_s)` |
|---|---:|---:|
| Default `Kmin=16` | 23,720 | 14,016 |
| Relax only `Kmin` to 2 | 24,063 | 14,356 |
| Added numerical rows/groups | 343 | 340 |
| Added realized minimal-counterexample possibilities | **0** | **0** |

The 343 added rows have `{K=8:48,10:68,12:134,14:33,15:60}`, all `s=3`, and violate GGV. At `n<=100`, counts are 592 versus 658. Every row is retained in [core-rows-kmin2.jsonl](../box/census-coverage-20260905/core-rows-kmin2.jsonl); none is asserted realized.

There are **1,833 height-six rows**, all at n=192. One is `(192,128)`, `M_2,...,M_6=(-96,-80,-72,-36,190)`, `V_2,...,V_6=(1,24,12,6,3)`, with `(d_2,...,d_6)=(64,32,16,8,4)`. An added `s<=5` cap would remove these rows; **the charged code has none**.

All 24,063 rows pass independent `Skel` window/full tests, integral-capacity and bottom-identity checks; no duplicates. `any10` fails on 4,749 default rows and 277 extras but is not imposed. Whole-tree extension, sibling bottom tests, centre obstruction and ODE nondegeneracy are further A pruning. The core does not enforce algebraic realizability or reconstruct Moh's unpublished program; his six p. 202 rows are controls, not a completeness proof.

Loop coverage is constructive. A normalized realized row's K and reduced ratio occur in the outer loops, its strict gcd chain in `divisor_chains`, and its increasing M-values in `Mrec`. From the top down, each actual multiplicity lies in its integer V-window and obeys the strict top bound. Inductively R and LCM equal Def. 5.1's product and upper denominator LCM. The necessary orbit and terminal disjunctions retain it, so the row is yielded. No step uses `n<=100` or `s<=5`.

**Operative tree.** `scope_enum.operative` calls `opus5_probe.Tree` with `gate=False,ode=True,recenter=True,capacity=False,passport=False`. Xu uses an independent `full_tree_partition`. Replay on **all 24,063 rows** found identical survivor sets, not merely equal totals.

At an internal level j, the branch-specific quantities are

`P=V_{j+1}d_j/d_{j+1}`, `Q=V_{j+1}(n-M_j)/d_{j+1}`, `lo=P/Q=d_j/(n-M_j)`.

These are `deg p`, `deg q`, and the major threshold in Prop. 4.6 p. 170 / Prop. 5.3 p. 182.

| Operative condition | Necessary justification; class |
|---|---|
| Integral nonnegative zero multiplicity `b`, `b congruent P mod A`, `0<=b<=P`; nonzero-orbit multiplicities form a multiset with `P=b+A sum(v)` | **A**, full orbit bookkeeping from p. 201's action. Enumerating all b and nondecreasing multisets loses no unordered partition. No multiplicity/partition search cap. |
| At most `floor((Q-1[b>0])/A)` nonzero orbits in Opus5 | **A**, Prop. 4.6(3),(4): q is squarefree and contains every p-root. Each nonzero orbit uses A distinct q-roots, zero uses one if present. The other implementation uses the weaker `floor(Q/A)`, harmless for containment. |
| Require at least one factor `v>lo` | **A**, Theorem(7) p. 200, or Prop. A.3(4) p. 205. |
| Recurse on **every** factor above lo, including an unselected zero sibling | **A**, Theorem(4) p. 200 and Prop. 5.3. Each actual major child extends. Testing only the recorded path would miss pruning. |
| The recorded `V_j` path must embed in one such tree | **A**, the realized tree itself supplies an embedding. Other siblings are existentially completed, with no invented equality among different branches. |
| Every bottom major child satisfies (12) or (13) | **A**, the terminal proof above applies separately to every child. |
| Reject positive root multiplicity v with `P=Qv` | **A**, the local ODE from Prop. 4.6/Prop. A.3. From `P p q' - Q p' q = c p`, at a p-root a of multiplicity v, squarefreeness gives `(P-Qv)q'(a)=c!=0`. Applies to zero and nonzero roots alike. |
| Reject a still-centred, removable all-zero chain reaching bottom | **A after the explicit C affine removal**, Prop. 5.6 pp. 188–190 plus the full-Galois centre argument below. The Boolean `danger` becomes permanently false after a non-removable nonzero coefficient. |

Zero **labels** alone do not specify the centre. After top-slope removal, a still-zero packet is invariant under full Puiseux Galois over `k((t))`. A first nonzero nonintegral centre term `a t^e` before the next radius would have a conjugate in the same packet first separated at e. Prop. 5.3 p. 180 defines the child as the **minimal disc containing the entire packet** of g/approximate-root roots; its radius would be e, a contradiction. This excludes intervening old-lattice terms which the current increment action alone fixes.

Induct down that path. Lemma 6.1/Def. 5.1 give lower radii in `[0,1)`, so integral centre terms are only the constant and top slope. P.190's `(x,y)->(x,y-a x-b)` removes them. Radius-zero nonzero coefficients are removable; positive fractional ones are not and permanently clear `danger`. Thus a surviving dangerous path has terminal point `pi t^delta_1`; Prop. 5.6 contradicts minimality/noncoordinateness. Zero-factor multiplicity is irrelevant. Nothing is inferred below a nonzero fractional ancestor.

The full ancestor action repairs the L>1 proof gap without a cap. Optional `capacity`/`passport` are disabled: neither the stronger `A | Q-1` test nor passport conditions enter 1,420. No child-top, U-NEGATIVE, descended-degree or Appendix-II-shape filter enters it.

**Xu has two distinct screens.** The census-wide `XuBounder` uses **Cor. 5.3 p. 8**, `IM>=Im`, from Theorems 4.7 and 5.1 (pp. 5,7). The input is the normalized pair, monic in y with constant nonzero Jacobian, and generic `f_xi=f-xi`; this does not change negative-order major data. It optimizes bounds over tree completions:

`IM_max >= Im_min = 1 + principal_minor_floor + other_minor_floor`.

For a bottom major packet of f-mass `v*m/d_2`, the code's contribution to the upper bound is

`(v*m/d_2) * n/(m+n) * (1-delta_1)`.

Xu Theorem 5.1 sums over final major roots. Further refinements have radius at least `delta_1`; distributing fixed root mass among them cannot increase this expression. It is an upper bound, not attainment. A-orbits contribute A distinct conjugate packets.

For an internal minor packet of multiplicity v, the code uses the first possible zero-order radius

`rho_0 = delta_j + [d_j/(n-M_j)]*(1-delta_j)/v`

and floor `max(0,rho_0-1)` per packet, times A for a nonzero orbit. Moh Prop. 6.1 pp. 190–194 applies while g-order is negative. Initial packet mass gives the maximal order slope as radius increases; splitting reduces mass and can only postpone zero order. Xu Cor. 4.5 p. 5 identifies these as minor roots; Lemma 4.4(ii) puts their final orders above 1. Each disjoint packet has a final minor descendant. Theorem 4.7/Cor. 5.3 license the floor, not exact final split data.

The original principal floor is `v_s-1` for `u_s=1` (Moh Prop. 6.4 pp. 198–199), **zero for `u_s>1`**. Minimum minor and maximum major bounds may use different completions: this is permissive, since actual values lie between them. Only `IM_max<Im_min` rejects. The code adds the global 1 once and uses exact rationals. The stronger-floor replay is a separate diagnostic.

The **direct Corollary 7.5** helper is in the snapshotted `box/lib/split_window.py`, lines 344–355. Its actual path goes through `skeleton_view` (183–219), which checks the FS endpoint, characteristic gcd data, `s>2`, and `v_s>u_s>=2`; `genuine_partitions` returns partitions with at least two parts. These are principal-minor face partitions. The helper excludes only

`partition == (1,)*u_s and rho < (v_s+1)/(u_s+1)`.

Xu pp. 11–12 require principal minor roots, `u_s>1`, the full distinct split, and the **strict** cutoff. Partial partitions and equality remain. For `(u_s,v_s)=(3,8)`, rho=2 excludes `(1,1,1)` but not `(2,1)`; for `(2,5)`, rho=2 equals the cutoff and remains. [xu75-controls.json](../box/census-coverage-20260905/xu75-controls.json) checks these boundaries and caller scope. The bare helper lacks input validation (notably u=1); the audited call path supplies it.

The split caller records Cor. 7.5 as an independent certificate; G/L tests determine chart status. Killing a chart does not kill its parent row, which may split differently or reach descent. This audit adds no indiscriminate Cor. 7.5 rejection of `u_s>1` rows.

| Mechanical screen, `n<=200` | Surviving rows | Interpretation |
|---|---:|---|
| Core, Kmin=2 | 24,063 | All stripped-list numerical candidates |
| Core, Kmin=16 | 23,720 | Additional all-degree GGV pruning |
| `C_FULL_TREE_POLYNOMIAL_ODE` | **1,420** | Same result for both Kmin choices; 686 groups |
| That screen AND original Xu Cor. 5.3 bound | **1,377** | 43 rows removed; 29 whole groups removed |

At `n<=100`: 658 core, 20 operative, 17 after original Xu. Replay took about 36 seconds with **zero tree-set mismatches**. [op-ft-xu-count.json](../box/census-coverage-20260905/op-ft-xu-count.json) contains every operative row and both bounds. Calling 1,420 the conjunction is a population-label error; the larger set remains safe.

**Containment follows:** the normalized realized datum is visited by the core loops; its actual factor tree satisfies the operative necessities; its Xu data lie between the computed bounds. Hence the original conjunction retains it whenever normalized `n<=200`.

Literal item(4) has a safe printed replacement; no implemented restriction remains undecidable. Neither B clause leaks. The 343 low-K extras and 1,833 height-six rows are numerical diagnostics. **No enumerator repair is required.** Correct the description to “all-degree consequences with explicit normalizations and GGV,” not “(1)–(13) verbatim,” and distinguish 1,420 before Xu from 1,377 after it. Higher Kmin, a height-five cap, or unconditional UNI/H2 would need a new audit.

**FALLACY-v2.** Search normalization and theorem are separated at the cited printed lines. Every normalization names its group element; the Galois proof separates labels, old lattice and physical packet. Floors never imply attainment, rows never imply realization, and the parent top convention is not transferred to children. No new exit-price assertion is made; no charge-basis declaration applies.

Replay from the repository root:

```text
sha256sum -c box/census-coverage-20260905/input-manifest.sha256
sha256sum -c box/census-coverage-20260905/op-aux-inputs.sha256
python3 box/census-coverage-20260905/core-count.py
python3 box/census-coverage-20260905/core-audit-rows.py
python3 box/census-coverage-20260905/op-ft-xu-count.py
python3 box/census-coverage-20260905/xu75-controls.py
```

Renders, logs, rows, snapshots and three detailed audits (`printed-audit.md`, `core-audit.md`, `operative-audit.md`) remain in the output directory. The seal uses the receipt's frozen basis. No ledger promotion is performed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23979`.
- Body SHA-256:
  `5b2be87d646f8f71b680a79209548d7e6a637b0477ae2f1a034879927fd0ca7c`.
- Frozen basis: `0b4b95e91fc1f1782c1949d3092c649296b71c8e`.
