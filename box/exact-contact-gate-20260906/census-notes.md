# Independent flat census replay (census worker)

Frozen inputs used: charged exact-contact report and charged roster; source extracts Moh/Xu from parent. No producer driver was available or read. All arithmetic uses Python `fractions.Fraction`. Run `python3 box/exact-contact-gate-20260906/census_replay.py`; this writes two compact JSON files.

## Enumeration actually reproducing the report

For levels `i=s-1,...,2` use

- `P_i=V_(i+1)*d_i/d_(i+1)` and `Q_i=P_i*(n-M_i)/d_i`;
- `lo_i=P_i/Q_i=d_i/(n-M_i)`;
- `L_i=lcm(den(delta_(i+1)),...,den(delta_s))`, `A_i=den(L_i*delta_i)`;
- `p_i=pi^z product(pi^A_i-c_j)^r_j`, where `z+A_i sum(r_j)=P_i`;
- `[z>0]+A_i #j<=Q_i`, no positive multiplicity equals `lo_i`, and `V_i` is a multiplicity;
- distinguish choosing the zero factor from choosing a nonzero orbit of multiplicity `V_i`. Repeated nonzero factors with the same multiplicity are symmetric, so each multiplicity has only one selection option;
- when `A_i=1`, record every root in the ordinary singleton list (`z=0`), removing redundant representations under translation. Keeping a special zero root here gives 2,021 rather than 1,080 labeled objects.

Take the Cartesian product of the level choices. This is the producer's coarse Moh lattice convention; it need not be the smaller *actual centre stabilizer* lattice when a selected higher coefficient vanishes. The difference is very large for R063 and R066: they contribute 509 and 230 of the 1,080 coarse enumerations. The purpose of this replay is to identify and test the claimed arithmetic count, not to silently replace its enumeration with a stronger one.

At a pattern root of multiplicity `r`, use `rho=m*r/d_i`, `a=m*(1-delta_i)/(n-M_i)`, and `kappa=rho*(1-delta_i)-a`. A minor packet contributes `-kappa/rho` to the unsplit minor sum. A major packet provisionally terminated at the next final disc contributes `n*rho*kappa/((n+m)*rho-m)`. The selected orbit follows the selected lower tower. The principal minor baseline is `V_s/u_s` (the constant 1 plus its unsplit contribution). Final selected discs contribute `n/(n+m)*rho*(1-delta_1)`.

Both variants tested give the same numerical outputs on these 66 rows: (a) follow only the selected Galois orbit and terminate every other major packet immediately; (b) copy the chosen continuation into every major packet with the selected multiplicity. This agreement is a finite-dataset observation, not a theorem identifying equal multiplicity and Galois conjugacy.

## Exact mechanically reproduced count

| Category | Count |
|---|---:|
| Enumerated labeled tower configurations | 1,080 |
| Nonintegral flat major sum | 995 |
| Flat major sum below unsplit minor sum | 77 |
| Both preceding defects | 71 |
| Nonintegral, but flat major sum >= unsplit minor sum | 924 |
| Integral, but flat major sum below unsplit minor sum | 6 |
| Flat major sum >= unsplit minor sum | 1,003 |
| Pass both flat comparisons | 79 |
| Rows with a flat survivor | 59 |

Thus 924 is correct arithmetic; it is 924 of the **1,003** flat configurations passing the minor inequality, out of 1,080 overall. The sentence saying “924 of 1,080 configurations that Cor 5.3 alone retains” has the wrong denominator qualification.

Type totals under the report's T1/T2/T3 definition:

| Type | Total | Nonintegral | Below minor sum | Integrality only | Flat survivors |
|---|---:|---:|---:|---:|---:|
| T1 | 52 | 1 | 5 | 0 | 47 |
| T2 | 29 | 11 | 2 | 10 | 17 |
| T3 | 999 | 983 | 70 | 914 | 15 |

T1's one nonintegral configuration is R007: `z=5`, two nonzero orbits of multiplicity 2, zero-selected `V_2=5`, `I_M=5/2`, minor sum 4. It already fails the inequality. T2's repeated factors need not be a single Galois orbit: the `(75,50)` control has two distinct nonzero orbits, each internally conjugate.

## What the count does and does not prove

Exactly **19** of the 1,080 configurations have an off-tower major sibling born at level 3 or higher. All 19 lie among the 924 integrality-only failures. Their raw major value assumes immediate termination and is not justified by the selected tower alone. Distribution:

| Rows | Number |
|---|---:|
| R022 | 1 |
| R025, R026, R027, R028 | 3, 4, 2, 2 |
| R047, R048 | 4, 1 |
| R057, R058 | 1, 1 |

Hence 905 of the claimed 924 arithmetic exclusions have only final-level off-tower siblings; the remaining 19 require the actual sibling closure. The root/closure worker is auditing that printed closure separately. It would be invalid to promote the raw 924 count as exclusions of all possible completions merely because the immediate-termination rational numbers were faithfully reproduced.

The report's “14 patterns” for the six target rows does not match the same reconstruction that exactly reproduces all four census totals: the six have **13** coarse configurations, distributed **3,4,2,2,1,1**. This is an ordinary counting correction, not a mathematical kill.

The minor sum is explicitly recorded as `Im_unsplit`. A minor packet can split before its nominal zero radius, raising the minor sum. Particularly when `u_s>1`, `delta=V_s/u_s` is an unsplit principal-minor order, not an unconditional exact ledger for the realized pair. Reproduction of the raw arithmetic should not promote such an unsplit order as attained.

## R009 and R050 positive and negative arithmetic controls

R009 has two coarse patterns. `(z=0,parts=(1,2))` gives exactly `(I_M,Im_unsplit)=(8,8)`. `(z=16,parts=(2))` gives `(1592/79,3)` with sibling `(rho,kappa,W0,L)=(32,20,44,1)` at the zero root. The `L=1` here is the actual coefficient stabilizer before the zero continuation; using the coarser old lattice `L=16` also gives final increment 79, so this discrepancy does not change that final Galois obstruction.

R050 has `(z=1,parts=(1,4))` giving `(8,8)` and `(z=5,parts=(4))` giving `(123/11,3)` with sibling `(rho,kappa,W0,L)=(10,4,12,1)`. The same coarse-versus-actual lattice distinction is harmless for its final denominator 11.

No polynomial witness, root coefficient realization, or new exit-price assertion is claimed here. Closure can strengthen these provisional outputs only through the separately checked print.

## Follow-up independent closure audit

I read and reran `closure_fixed.py`, then wrote `closure_audit.py` without importing that driver. The audit checks every emitted node's radius, order, P/Q degrees, threshold, factor mass, child state, actual lattice update, final root counts/residues, final major term, Cartesian sum, and row survivor set. **1,294 exact equalities pass across all nine target rows.** It also verifies there is no target pattern with an unresolved choice between a zero factor and a nonzero factor of the designated multiplicity. The driver generally chooses the first matching factor, which would require additional route handling on other rows; that issue does not occur on these targets.

The actual stabilizer update is `L -> L` on a zero factor and `L -> lcm(L,den(delta))` on a nonzero factor. Thus R028's zero-selected level-3 factor retains `L=1`, while its six nonzero siblings acquire `L=6`; their next radii are respectively `1/5` and `1/3`. The specified R028 route is preserved: `V_3=4` chooses the zero factor, and `V_2=3` chooses a nonzero orbit below it. No node count, W range, partition length, or orbit-number cap appears in this fixed-index recursion. Every major continuation decrements the printed global index from i to i−1, ending at i=1.

### Manual R028 counter-completion to the claimed conditional kill

For `(n,m)=(180,120)`, use `M=(-120,132,150,178)`, `d=(180,60,12,6,2)` and `V=(3,4,5)`.

1. At level 3, `rho=100`, `kappa=80`, `W=30` give `delta=1/6`, `|lambda_f|=10/3`, `P=10`, `Q=25`, `A=6`, threshold `2/5`. The pattern is `pi^4(pi^6-c)`. Its zero child is `(rho,kappa,L)=(40,30,1)`; the six ordinary children are `(10,5,6)`.
2. The zero child at level 2 has `W=48`, `delta=1/5`, `|lambda_f|=2`, `P=20`, `Q=16`, `A=5`, threshold `5/4`. Choose `(pi^5-a)(pi^5-b)^3`. Its five minor packets have `rho=2`, `delta=6/5`. Its five major packets have `rho=6`, `kappa=14/5`, final `delta=1/2`, and individual `J=9/5`. This branch contributes major sum 9 and minor sum 1.
3. Each ordinary child at level 2 has `W=48`, `delta=1/3`, `|lambda_f|=5/3`, `P=5`, `Q=4`, `A=1`, threshold `5/4`. Choose multiplicities `(2,3)`. The two final major packets are `(rho,kappa,delta,J)=(4,1,13/18,2/3)` and `(6,7/3,7/12,3/2)`. Each of the six conjugate copies contributes `13/6`, for total 13, with no minor contribution.

Final residues are `(rho_f,rho_g)=(6,9)` modulo 2 on the selected arm, `(4,6)` modulo 3 and `(6,9)` modulo 2 on the ordinary arms. They pass the squarefree/coprime residue condition. All three reduced multiplicity sets `{4,1}`, `{1,3}`, `{2,3}` have gcd 1, so this completion satisfies the report's Lemma A restriction. Its only level-2 exponent is the existing global `M_2=132`, divisible by the common ancestor divisors 12 and 6; final `M_1=-120` is divisible by 60,12,6. Thus it satisfies Lemma B when applied to actual ancestors. It inserts no new exponent.

The principal minor baseline is 5, giving **`I_M=9+13=22`, `Im_unsplit=5+1=6`**. The **same** coarse row configuration had flat value **`111/4`**: immediate termination of each `rho=10,kappa=5` sibling contributed `25/8`, so `9+6*(25/8)=111/4`. Its nonintegrality disappears when the printed intermediate level is respected.

This is a counter-completion within two remaining major levels and within the stated numeric A/B restrictions. It refutes the reported conditional numerical row kill; it is not a polynomial-pair witness or proof that all coefficient equations admit a solution. The independent closure output has necessary numeric survivors on every one of the six claimed kills, unique `(8,8)` on R009/R050, and none on R001. Therefore the six claimed removals cannot promote residual 59.
