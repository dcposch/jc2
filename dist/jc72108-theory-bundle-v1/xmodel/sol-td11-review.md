VERDICT: BROKEN — TD11-CLASH does not prove the advertised all-configuration death: OB-6 runs the td-7 budget-5 closure while claiming td-11 budget-9 coverage, OB-8 does not audit the 129/145 decorated 11-C skeletons that are nested, and the NF-D corollary includes the same two-word deep families that its §12 perimeter excludes.

# Hostile review of TD11-CLASH

This is a break of the theorem/certificate, not an exhibited tower survivor. The local packet arithmetic, the four advertised near misses, and the direct 11-A `5/8` kill all replay. What fails is the universal perimeter needed to pass from those local facts to every synchronized td-11 class-B/C configuration and to arbitrary NF-D depth.

## Findings, ranked

### 1. CRITICAL — the claimed budget-9 global-window audit actually runs at budget 5

`TOWER-TD11.md:226-248,353-363,379-380` says block 10 closes every td-11 opponent state under the gross budget-9 discipline. But `cases/tower_td11.py:408-420` calls

```python
px5.close_with_cells(*seed)
```

without a budget. The imported td-7 engine defaults to `budget=5` at `cases/scratch_offaxis_pricing/px5.py:63-74`. The printed counts `21 + 347 + 69` are therefore budget-5 counts. This directly contradicts both the theorem document and the original scope, which says td-11 has gross budget 9 and that no present engine certifies the required multistep closure (`xmodel/sol-td11-13-scope.md:46-51,142-154`).

Exact replay on the 11-A opponent seed `(w,M)=(3,2)` gives:

```text
budget       5    6    7    8    9
states      21   56  130  330  743
```

Thus block 10 omits 722 states on this seed alone. The first omitted states occur at price 6, including `(2/13,13)`, `(2/11,11)`, and `(3/4,8)`.

The advertised ratio maximum is also false at budget 9. A reachable admissible path is

```text
(3,2)
  -- st96 l2e0k2S2x0nu5(20,16), lambda=4 --> (3/2,4)
  -- st96 l4e0k2S4x0nu5(40,16), lambda=2 --> (3/4,8),
```

followed at total price 7 by

```text
st96 l8e0k1S1x2nu2(18,9),   dq*l/dp = 9*8/18 = 4,
```

not the claimed `R*=5/2<4`. This particular object is not itself a window escape: its preceding full degree is already `400`, so its gap is `4/400=1/100`. It nevertheless falsifies the proof's stated maximum and leaves the global `<1/2` conclusion in need of a new budget-9, degree-aware proof.

Even an explicit `budget=9` rerun would remain exploratory, not complete: `px2.py:82-88` retains the td-7 hard loops `k<7` and `ell_ex<41`, which the proved normal-form discussion expressly forbids in a production compiler (`xmodel/sol-normalform.md:230-233,732-734`).

### 2. CRITICAL — OB-8 does not discharge nested 11-C composition

The required entry/hierarchy quantifier has six labelled hierarchy packets: one for 11-A, one for 11-B, and four for 11-C. For 11-C, with leaves `A(M=1), B1(M=2), B2(M=2)`, the corrected diagnostic is:

| hierarchy | decorated rows | rows with a mixed node |
|---|---:|---:|
| direct `G(A,B1,B2)` | 16 | 0 |
| nested `G(G(A,B1),B2)` | 40 | 8 |
| nested `G(G(A,B2),B1)` | 40 | 8 |
| nested `G(G(B1,B2),A)` | 49 | 18 |
| **total** | **145** | **34** |

So 129/145 decorated skeletons are nested. These totals reproduce `xmodel/sol-td11-13-scope.md:21-44`. The checked-in old expansion returns only `103/25`, because it conflates an inner child's emitted `M_child` with the independently chosen parent-edge `mu | M_child`; that known defect is documented at `BOOK-OFFAXIS-REVIEW.md:239-246`.

A concrete printed-tier skeleton omitted by that conflation is

```text
Gout(Gin(B1,B2), A)

Gin:   mu(B1)=2 | 2,  mu(B2)=2 | 2,  M_in=4 | (2+2)
Gout:  mu(inner)=2 | M_in=4,  mu(A)=1 | 1,  M_out=3 | (2+1).
```

Taking both merges interior satisfies `M>=2`; the inner node is mixed. This is a legal divisor/subadditivity skeleton, not a claim that its still-unchecked Q+E5F/ODE completion exists. Under Rule 6, that distinction means OPEN, never TOWER-DEAD.

The OB-8 gate at `cases/tower_td11.py:449-461` checks one leaf maximum, a small gcd identity, and a literal `True`. It does not enumerate even the direct 16 rows, much less the 129 nested rows or their emitted frames. Its cap-intersection argument is conditional on the relevant vertices remaining simultaneously alive. No restriction-of-ladder or global-first-death lemma establishes that condition through an inner merge; the source scope identifies precisely this local-to-global step as conjectural (`xmodel/sol-td11-13-scope.md:177-200,235-250`).

The document ultimately admits the break: nested pre-clash inner states are outside the theorem and must remain OPEN (`TOWER-TD11.md:374-382`). Therefore §7.6 cannot simultaneously be called an OB-8 discharge, and the theorem cannot certify every td-11 class-B/C row.

### 3. CRITICAL — the NF-D corollary does not close the equalized `mu=(1,M)` deep branches

The theorem explicitly names every co-scaled `Pi=5^k` family and arbitrary depth at `TOWER-TD11.md:287-303`, then claims entry-wise NF-D closure at `:321-324`. Its own perimeter excludes multi-word deep-zone coexistence at `:374-382`.

Those are the same objects at sufficiently large depth. NF-D says the live td-11 branch pads both pole chains in step with `Pi_1=Pi_2`, and specifically gives `Pi=5^k` on both poles (`NF-D.md:183-193,216-227`). Only finitely many letters can remain above `theta*` (`NF-Z.md:124-162`), so sufficiently deep repeated-5 stacks have sub-`theta*` tails on both chains. NF-Z defines that exact situation as multi-word deep coexistence and explains the missing cross-branch aliveness/nested-exponent gcd coupling (`NF-Z.md:407-440`). Equality of the two total products does not prove that coupling.

The gate contains no cross-branch deep-zone check: OB4 tests quotient equality/factorability, X3 tests a local Case-A divisor, and the theorem aggregate merely combines those booleans. `cases/nfd_check.py` still correctly prints `D(11-A)=D(11-B)=D(11-C)=OPEN` for the infinite equalized family.

Therefore the local full-lattice X refusal may close a single-word/per-spine projection, and may cover shallow co-scaled pairs before both tails enter the deep zone. It does not prove the actual unbounded two-stack family that made NF-D OPEN. Repair requires either a new cross-branch decoupling lemma and gate for the diagonal family, or deletion/qualification of the `Pi=5^k`, all-depth, and NF-D-corollary claims.

### 4. HIGH — realization and current-state `mu` classes are asserted, not exhausted

The original scope requires, per hierarchy and orientation, all current-state `M_U` classes, independent `mu | M_U`, arrival provenance, E5F offsets, shared budget, terminal, and a real clash carrier (`xmodel/sol-td11-13-scope.md:60-124,202-256`). It records the completed td-11 Q+E5/E5F refile as **UNKNOWN** (`:21-24`). TD11 nevertheless calls OB-10 discharged. The entire OB-10 gate is literal `True` at `cases/tower_td11.py:463-469`, as is the future-census implication at `:481-488`.

Two exact stress objects show what is missing.

First, the earlier `M_U=4` perimeter class is real already on 11-A:

```text
(w,M,P)=(3,2,4)
  -- st96 l2e0k2S2x0nu5(20,16), lambda=4 --> (3/2,4,40).
```

On the strict branch a legal neutral `nu=5` gives `P_1=2*5=10`. Choosing `(mu_1,mu_2)=(1,4)` gives

```text
P_1/mu_1 = 10 = 40/4 = P_2/mu_2.
```

This synchronized current-state branch is absent from OB4's entry-level `(1,1)`/`(1,M_entry)` characterization. Its competing gap is `2/5 < 3/5=gap(X)`, and the abstract cap argument appears to kill it; the point is that the claimed all-`mu` characterization/gate never tested it.

Second, there is a complete budget-feasible synchronized/E5F route candidate omitted by the budget-5 cell map:

```text
(3,2,P=4)
  -- (21,15), l=2, lambda=4 --> (4/3,3,P=42)
  -- (85,35), l=3, lambda=2 --> (2/5,5,P=1190).
```

Choose `mu_2=5`. The strict-side neutral stack `Pi=7*17=119` gives

```text
1190/5 = 238 = (2*119)/1.
```

For the known cell `(dp,dq,nu_G,M_G)=(18,27,13,9)@mu_0=5`, `kbar_G=6`, `X=4`, and arrival frame `(nu_U,kbar_U)=(17,7)`, E5F gives

```text
n = 17*6 - 13*7 = 11 >= 1.
```

Also `gcd(6,13)=1`, `18` does not divide `27`, the direct terminal has `w=4/9`, `psi=1`, and `lambda=6<=9`; the charged gaps are `5/14` and `1/34`. At budget 5 the `(2/5,5)` cell map contains only `{(7,5)}`; at budget 6 it adds `{(2,5),(17,5),(22,5),(27,5)}`. This route may still die under a repaired CAP-DEN/window proof, but it is an explicit E5F-admissible configuration the 46 checks do not exercise.

The proposed dichotomy “a selected pair is realized and killed, or unrealized and dead” also does not replace the missing route-level carrier theorem: rejection of one proposed arrival does not reject a state until every legal pad/reroute has been checked (`xmodel/sol-td11-13-scope.md:97-110,208-219,244-247`).

### 5. MEDIUM — the divisor-closure/cap-shrink proof mishandles cap `c=1`

`TOWER-TD11.md:171-172,201-205` assumes `den(alpha_1) | c`, while its cap tables include `c=1` at `:193-197,307-311`. Since every entry has half-integral `alpha_1`, the premise is false for `c=1`.

The gate repeats the mismatch. OB7a creates an integer alpha lattice when `c=1` (`cases/tower_td11.py:305-319`), and OB7b tests `alpha=a/c` (`:324-346`). It therefore never tests the actual half-integral register class after a cap shrinks to 1. This is exactly the least-tested direct OB-8 edge: divisor closure of the cap values is not by itself closure of the register classes when a larger cap was legal earlier.

This is repairable and does not produce an escape. If the cap is 1 from the start, every prefix has `k=1`, so `alpha=N+1/2`. For neutral X,

```text
alpha - 1 + (nu+1)/(2nu) = N + 1/(2nu),
```

whose denominator is `2nu>1`; 11-B's resonant `X=5/4` gives denominator 4. A cross-check of every quarter-lattice register from an earlier cap 4 against later caps 2/1, and every sixth-lattice register from cap 6 against later caps 2/1, found zero escapes. The theorem needs this separate dynamic-cap lemma; its present gate and “divisor-closed” sentence do not supply it.

### 6. LOW — the resonance gate uses the wrong `M'` formula, though the 11-A kill survives

`cases/tower_td11.py:101-106` checks the changing resonance with

```text
M' = gcd(l,nu+1) = gcd(l,3).
```

For the clean changing cell the correct law is `M'=gcd(l,dq)=gcd(l,5)`, as the imported engine itself uses at `cases/scratch_offaxis_pricing/px2.py:55-60`. This is numerically harmless here: `l | 2`, so both `l=1,2` give `gcd(l,5)=1`.

A4 is also a finite sample, not its advertised all-route proof: `cases/tower_td11.py:130-140` tests letters below 16 and stack depth at most 2. The symbolic valuation argument is valid, so this is test-strength errata rather than an escape.

## Realization classes the theorem's quantifier must cover

| dimension | required classes |
|---|---|
| entry/topology | 11-A binary; 11-B binary; 11-C direct ternary plus the three labelled nested orders above |
| merge placement | root and interior/trunk completions; every zero-slot orientation; class-B, class-C, MP6, and all-`mu>=2` mixed nodes |
| chain history | empty; arbitrary `nu>=2` neutral words; state-changing clean resonances; fixed dirty/charged cells; pure-(b) parameters; charged self-returns and multiplicity partitions; neutral padding before and after charged vertices |
| current-state arrivals | every `mu | current M`, not merely entry `M`; emitted `M_G | sum mu_e`; at nested nodes an independent parent `mu | M_child`; entry, direct-cell, neutral, padded, and rerouted arrival provenance |
| synchronization/realization | H8 pass and fail at every node; all E5F-admissible direct/pad/reroute witnesses; E5-refuted witnesses removed only after their whole reroute family is exhausted |
| budget/completion | one shared price ledger through all branches and merges up to 9; direct terminals, inter-merge chains, trunks, and every terminal `psi` |
| tower order | every charged predecessor stratum, sibling/inner/merge/trunk gap, dynamic simultaneously-alive cap, non-killing prefix register, and global first-death order |
| neutral depth | single-word zones and, if the theorem claims all `Pi=5^k`, the cross-branch multi-word deep zone; `nu=1` and other NF-P schemas must remain explicitly outside until proved |

The current theorem machine-checks only local entry packets/windows, a budget-5 state projection of the three opponent seeds, a static cap/register superset (with the `c=1` defect), and the direct 11-A valuation kill. It does not cover the complete table above.

## Confirmed subclaims

### The scope's 11-A hard object is exactly the object killed here

The scope and TD11 use the same tuple:

```text
Delta=3, n=2, nu=2, (w,M,P)=(3,2,4), dq=5,
P'=4*(2l)/l=8, gap=5/8, w'=2.
```

The window condition is exactly

```text
5/8 > (nu_X+1)/(2nu_X)  iff  nu_X>4,
```

so the legal cases are odd `nu_X>=5` (`xmodel/sol-td11-13-scope.md:337-355`; `TOWER-TD11.md:270-282`). For both legal `l=1,2`, the correct law gives `M'=gcd(l,5)=1`, hence downstream `mu=1`. The strict branch has `P_1=2C` with `C` odd and `v_2(P_1)=1`; the resonance branch has `P_2=8AB` and `v_2(P_2)>=3` (`xmodel/sol-normalform.md:506-590`). H8 raw equality is impossible. Thus the original 5/8 intruder really dies. A preceding genuine neutral pad moves its gap below `1/2`; a `nu=1` degree-preserving insertion keeps the literal value but not the H8 escape and remains outside the present NF-P perimeter.

### OB-1's type-(2,5) packet replays

For pole type `(alpha,beta)=(2,5)`, P1 gives `(k_0,l_0)=(2,5)` and `g_top=(2+5)/2=7/2`; Z1 gives

```text
alpha_1 = l_0 + 1 - g_top = 5 + 1 - 7/2 = 5/2.
```

The full pole degrees are `(2,6)`. The regression `(2,3) -> (k_0,l_0,g_top,alpha_1)=(2,3,5/2,3/2)` agrees with the promoted td-7 packet. The arithmetic is correct, although block 6 mostly asserts the formula and hard-coded entry data rather than replaying a new polynomial-collapse certificate.

### The four advertised near misses all replay

1. 11-B `nu_X=3`, cap 6: `2nu_X=6 | 6`, but `nu_X=3` is illegal because `3 | nu_X`.
2. 11-B `nu_X=2` and 4, cap 6: the actual denominator sets are `{4,12}` and `{8,24}` respectively, never divisors of 6.
3. 11-A cap 4 admits arithmetic `k=4` prefix rows, but a full correct register sweep still found no X escape.
4. 11-A `nu_X=3` has `gap(X)=2/3>5/8`, and CAP-DEN kills it (`3` does not divide `16`).

These are genuine load-bearing edges. The ledger is incomplete, however: it does not list the budget-9 closure failure, nested cap history, cap-1 register class, or multi-word deep-zone coupling above.

## Gate replay

```text
python3 cases/tower_td11.py  -> exit 0, ALL 46 checks PASS
python3 cases/nfd_check.py   -> exit 0, ALL 22 checks PASS
```

The green 46 count is not a theorem certificate. Besides the wrong budget, B1 is the tautology `5/4 == 5/4`, while OB7e, OB8b, OB10, and the census implication pass literal `True` (`cases/tower_td11.py:152-158,364-367,457-469,481-488`). The aggregate row checks only `okX`, `okLat`, and the budget-5 ratio summary (`:471-480`). The NF-D gate is internally consistent and, importantly, continues to report the equalized td-11 depth as OPEN.

## Minimum repair before promotion

1. Replace the td-7 state projection with a cap-free, provenance-preserving shared-budget-9 closure; retain full degrees, paths, current `M`, arrivals, E5F witnesses, and budget inventory. Remove the hard `k/ell_ex` loops.
2. Build the corrected 145-row 11-C hierarchy layer, transport full frames through every inner edge, and prove either a global-ladder restriction theorem or every nested first-death order. Static “third pole only shrinks the cap” is insufficient.
3. Prove cross-branch deep decoupling for the equalized `Pi=5^k` family, or leave the NF-D corollary and all-depth claim OPEN.
4. Add per-route current-state `mu`, H8, E5F/reroute, terminal, cap-history, and census-parity assertions; replace the literal-`True` obligation rows.
5. Repair the `c=1` register case and the resonance `M'=gcd(l,5)` check explicitly.
