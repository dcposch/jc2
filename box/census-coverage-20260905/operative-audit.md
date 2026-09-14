# Operative screen audit (subtask notes)

The operative tree screen has an all-degree necessity derivation from the printed sources, conditional on the FS-normalized minimal Keller setting. No additional degree/depth cap occurs inside it. The number **1,420 is before Xu**, not after conjunction with Xu. Mechanically replayed, original `XU` excludes 43 rows/29 groups and leaves **1,377** rows; the later stronger principal floor excludes 48/33 and leaves **1,372** rows. These are numerical candidate counts, never realization claims.

## Custody and artifacts

Frozen charged core: `/tmp/jc2-lane.94eJYj/inputs/moh_skeleton_full.py`, loaded explicitly into `sys.modules` under the two imported names. Auxiliary sources were copied into this directory as `op-{scope_enum,opus5_probe,full_tree_partition,xu_screen,split_window}.snapshot.py`; all five hashes in `op-aux-inputs.sha256` mechanically checked OK. No pre-existing implementation was edited. `op-ft-xu-count.py` uses these snapshots and the frozen charged core; its 36-second replay is `op-ft-xu-count.{json,log}`. The JSON contains every operative row, each Xu bound, and the complete set-comparison result. An exploratory weaker-gate count was stopped after its n=180 checkpoint: it is not a complete n≤200 count and is not used in the verdict.

Rendered/visually inspected from frozen PDFs: Moh printed pp.170,179,180,188,189,190,194,205 and Xu pp.4,5,7,8,10,11,12. Images are `op-moh-pNNN.png` and `op-xu-pN.png`; also rendered Moh182/200. Moh PDF page = printed−139. Searchable companions `op-moh-layout.txt`, `op-xu-layout.txt` were generated from the frozen PDFs.

## Actual entry points and source necessity

`op-scope_enum.snapshot.py:27–35` calls `Tree(n,m,Ms, gate=False,ode=True,capacity=False,passport=False)`, sets `recenter=True`, checks `d_s>V_s>d_s/2`, and embeds the prescribed `V_{s-1},...,V_2` path. `op-full_tree_partition.snapshot.py:401–402` is the independent `C_FULL_TREE_POLYNOMIAL_ODE` implementation; `op-xu_screen.snapshot.py:184ff` uses its evaluator.

At level j set `P=V_{j+1}d_j/d_{j+1}`, `Q=V_{j+1}(n−M_j)/d_{j+1}`, `h=d_j/(n−M_j)=P/Q`, `L=lcm den(δ_{j+1}),...,den(δ_s)`, and `A=den(Lδ_j)`.

| Actual code condition | Printed basis and scope | Necessity status |
|---|---|---|
| `d_s>V_s>d_s/2` (`opus5:212`) | Two distinct top factors in FS; Moh p.194 setup; major threshold Def.5.1(2), p.179. Strict upper bound says other top multiplicity `u_s>0`; strict lower says `v_s>u_s`. | A, in the normalized minimal setting. |
| Branch-specific radii, exact `Fraction` products (`63–81`) | Def.5.1(3), p.179; extension formula Prop.5.3 p.180. | A, no n≤100 use. |
| Integer P,Q assertions and selected V>h (`77–80,122`) | Def.5.1(1),(2),(4), p.179; Prop.4.6(1),(2), p.170. | A; P,Q are degrees, and denominator divisibility follows from the gcd chain. |
| A from L; `b=P mod A,...,P`; `P=b+A Σv` (`72–75,137,145`) | Printed item(8) p.201 Puiseux cyclic action. Over old field `k((t^(1/L)))`, adjoin `t^(1/(LA))`; generator fixes old coefficients and multiplies π by a primitive A-th root. Nonzero root orbits have A members of equal multiplicity; zero has multiplicity b. | A consequence of the root action. A=1 is included, with arbitrary b. |
| Coin multiplicities are positive; capacity `(Q−[b>0])//A` (`146–154`) | Prop.4.6(3),(4), p.170: q is squarefree, every p-root is a q-root. Thus `[b>0]+A·#orbits≤Q`. | A. The FT implementation uses weaker `Q//A` at lines265/300; harmless for coverage. Both implementations' complete survivor sets agree at n≤200. |
| Require at least one major root (`192–193`) | Moh Theorem p.200(7), before the bounded-search paragraph; equivalently Prop.A.3(4), p.205, applied with deg p=P,deg q=Q. | A. |
| Recursively admit every major sibling; force selected path to embed (`140–174`) | Prop.5.3 p.180 applies to every factor with multiplicity>h; Theorem p.200(4),(7). | A. Minor factors stop in this abstraction; deeper constraints on them are omitted, enlarging the model. |
| Reject every p-root multiplicity v with P−Qv=0 (`138–139,149–150`) | Prop.4.6 pp.170–171 derives the local ODE; Prop.A.3 p.205 rewrites it as `Q q p'=(P q'−c)p`, c≠0. At a p-root a of multiplicity v, q is simple, so `(P−Qv)q'(a)=c`. | A; applies to fixed zero root only if b>0, as code checks. |
| Bottom `(12) or (13)` on every major leaf (`83–92,131–134`) | Moh p.201(12),(13), derived from r=1 constant Jacobian ODE, Prop.4.6 p.170; root-conjugacy and coprimality argument on p.188. | A, no bounded degree needed. |
| `danger` survives zero root or removable integer radius≤0; reject danger at bottom (`125–133`) | Prop.5.6 p.188 requires the actual bottom π-root to be `πt^δ1`. It does not by itself identify tower labels with the full centre. The Galois/minimal-packet derivation below supplies that hypothesis. Affine removal is printed p.190. | A after the derivation, plus C affine normalization; not a naked reading of labels. |
| `capacity=False`, `passport=False` | Code branches at119 and194 are disabled. | Neither `A|(Q−1)` nor weighted passport test is operative. No extra unproved constraint is hidden in these branches. |

Finite enumeration of partitions loses no multiplicity type: enumerate each possible zero multiplicity b, then every nondecreasing multiset of positive orbit multiplicities summing to (P−b)/A with the finite slot bound. The actual polynomial p supplies one of these possibilities. Galois-conjugate children have the same numerical data; requiring one feasible arithmetic child template per orbit is necessary. The recursion has exactly the input skeleton's number of levels; there is no independent s≤5 check.

## Why the centre condition is justified, and its exact group

The older `recenter-gate-opus5` objection was correct about a missing implication in a one-line explanation: labels alone do not literally list every Puiseux coefficient. Nevertheless, the implication needed by the actual `danger` implementation follows from printed Prop.5.3 p.180.

Normalize the top major direction by `(x,y)↦(x,y−ax)`. Starting in a still-centred zero packet, the full Puiseux Galois group over k((t)) preserves the packet, since all previously fixed labels are zero (or integer centre coefficients fixed by the group). If a first noninteger centre term `c t^e`, c≠0, occurred strictly before the next declared major radius δ, choose a common Puiseux denominator N and a generator `t^(1/N)↦ζ_N t^(1/N)` moving that term. It takes a root of the same polynomial product to another root in the same zero packet. Their first separation is e<δ. This contradicts the definition of δ in Prop.5.3 p.180 as the **minimum** contact of all roots of `g∏_{i≤r}T_i` in that packet. Thus no such intervening noninteger centre term exists. Iterate down the zero path. Multiplicity b need not be one; the packet is fixed because its root value is zero.

The full/ancestor action matters: the current increment action over k((t^(1/L))) fixes old fractional exponents and alone is insufficient. The argument above uses the full group only while `danger` remains true. After any nonzero noninteger label, code clears `danger` permanently and does not apply this centre claim to its descendants.

Def.5.1's positive product gives δ_i<1; p.189 (also Lemma6.1 p.194) gives intermediate δ_i≥0 in the FS setting. Top δ_s=−1. Therefore the only integral centre terms below δ_1 are `a t^(−1)+b`, and the group element printed on p.190 is exactly `(x,y)↦(x,y−ax−b)`, determinant1. It preserves degrees and makes the bottom centre zero. Prop.5.6 then gives either an automorphism pair or simultaneous degree reduction, both excluded for a minimal counterexample. No nonintegral translation is used. Thus the weaker `gate=True` test that allows arbitrary free old-lattice coefficients overcounts possible zero packets; its additional numerical survivors are not established coverage leaks.

## Xu scalar screen and strict split screen are different

Xu's original `XU` here is **Corollary5.3 p.8**, `IM≥Im`, obtained from Theorem4.7(ii) p.5 and Theorem5.1 p.7. It is not Corollary7.5. Source hypotheses are a characteristic-zero Jacobian pair, monic in y, generic ξ for `f_ξ=f−ξ`; the principal contribution uses the two-point leading form. The source-to-code degree map is `deg_y f=m`, `deg_y g=n`, `v_s=V_s`, `u_s=d_s−V_s`. The normalized minimal data meet these hypotheses. Generic ξ does not change negative-order major leading data.

The code uses two independent extremal bounds over every admitted whole-tree completion: `IM_max≥IM(actual)` and `Im_min≤Im(actual)`. It rejects only if `IM_max<Im_min`. Optimizing different completions for the two bounds is weaker than optimizing one common tree, so it cannot introduce a false exclusion.

* Major leaf bound (`xu_screen:222–232`): root mass `N=mV_2/d_2` times `n/(n+m)(1−δ_1)` from Theorem5.1 p.7 and Moh Prop.4.6. This is a safe upper bound; any further major final separation at δ≥δ_1 only decreases the contribution. No attainment conclusion is needed.
* Minor packet floor (`209–216`): `δ_floor=δ_j+h(1−δ_j)/v`, then `max(δ_floor−1,0)` per packet, multiplied by orbit cardinality A. Moh Prop.6.1 begins p.190 and Xu Cor.4.5 p.5 identify these roots as minor. A direct derivation from Xu Lemma4.1 p.4 and the proof of Theorem4.7 is: for a minor final root, `δ_final=−Σ_{β≠α}ord(α−β)`. For a packet of N roots and fixed negative outside-contact sum S_out, every inside contact is at most δ_final; hence `δ_final≥S_out−(N−1)δ_final`, i.e. δ_final≥S_out/N. The displayed code formula is this S_out/N in Moh's radius/root-count coordinates. Every packet contributes at least one final minor root, so it supplies a lower bound, never an equality assertion.
* Principal floor (`192–201`): original code uses `v_s−1` when u_s=1 and **zero** when u_s>1. For the principal packet, N=u_s m/d_s and S_out=v_s m/d_s, so the same distance argument gives `v_s/u_s−1` for every u_s≥1. Thus original zero floor is safe missed pruning. The stronger policy is separately counted, not silently substituted.
* Add the single global constant1 in `Im=1+Σ(δ−1)`; code `row_bound:432–449` does so. It never inserts one per minor packet. Minor terms are floors and major terms bounds; no floor is treated as attained.

Corollary7.5, visually inspected on Xu pp.11–12, assumes the §7.3 setting (p.10), u_s>1, and the full split polynomial `p=∏_{i=1}^{u_s}(π−c_i)` with all c_i distinct. It excludes exactly the strict side `ρ<(v_s+1)/(u_s+1)`. Equality and partial partitions are not excluded by this corollary.

Actual direct implementation `op-split_window.snapshot.py:344–355` tests `part==(1,)*u and rho<cutoff`. Its public caller validates `s>2`, `M_s=n−2`, the gcd chain, `v>u≥2` at185–218; `genuine_partitions` (line93) keeps only ≥2 blocks. `screen_view:398–401` records Xu as an independent certificate, while G and L determine its chart status; it does not apply Xu to all partitions or replace `<` by `≤`. The direct helper alone has no u>1 guard; its actual public call path supplies it. All-degree theorem claims should use that validated path, not the bare helper on malformed arguments.

`op-xu75-controls.json` mechanically checks u=3,v=8: full `[1,1,1]` atρ=2 is excluded; full split atρ=9/4 (equality) andρ=5/2 are retained; partial `[2,1]` atρ=2 and nonsplit `[3]` atρ=2 are not excluded. All five controls passed.

## Exact replay table

| Screen | 16≤n≤100 | 16≤n≤200 |
|---|---:|---:|
| Frozen core, Kmin2, full=True | 658 | 24,063 |
| Opus5 polynomial/ODE tree | 20 | 1,420 |
| FT polynomial/ODE tree | 20 | 1,420 |
| Symmetric set difference, Opus5 vs FT | 0 | 0 |
| Original Xu kills | 3 | 43 |
| Original conjunction survivors | 17 | 1,377 |
| Stronger principal-floor Xu kills | 3 | 48 |
| Stronger conjunction survivors | 17 | 1,372 |

At n≤200 the base operative rows form686 groups, original Xu completely kills29 groups, stronger floor33 groups. The code's names `1420 operative` and the task's phrase `C_FULL_TREE_POLYNOMIAL_ODE ∧ XU (1420)` must not be identified. A coverage statement may retain the larger 1420 set (safe weaker pruning), or describe the actual conjunction with its correct1377/1372 cardinality.

<!-- BODY-END -->
