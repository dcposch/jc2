VERDICT: BROKEN — even after adding Grok's seventh merge-schema-finiteness class, the compiler deletes a valid, in-bound 11-C normal-form chart by applying `M_G | sum(mu_e)` outside its proved `epsilon=0=k` scope; therefore 159 is not a complete quotient and CONDITIONAL EMPTINESS is not earned as stated.

# Sol hostile review of the td-11 census compiler

This is a coverage failure, not an exhibited live Keller route. The omitted object below is an exact local merge chart at the same printed/pre-refile tier as the census rows. A later outer completion may still die. That does not repair a compiler which declares the chart impossible before performing that analysis.

## Reproduction

| command | result |
|---|---|
| `python3 cases/td11_census.py` | exit 0; 6/6; 159/159 stamped; 6 FC printed; td-7 17/17 |
| `python3 cases/tower_td11.py` | exit 0; 66/66 |
| `python3 cases/nfp_check.py` | exit 0; 10/10 |
| `python3 cases/nfm_check.py` | exit 0; 25/25 |

The first result reproduces the requested 159. It does not test coverage: C5 is only `len(ROWS) == 159` plus absence of the literal stamp `LIVE` (`cases/td11_census.py:478-490`). An object deleted before `ROWS` is built cannot falsify it. The checked source still prints six FCs (`cases/td11_census.py:458-476`); throughout this review I also grant Grok's proposed seventh class, finite merge-schema/outer-menu completeness, and test the stronger seven-class formulation requested here.

## Findings, ranked

### 1. CRITICAL — an eighth perimeter class is missing: conditional-subadditivity authority

The exact normal form requires the merge record to carry an authority bit for the divisibility law:

> `M_G | sum(mu_e)` is proved only in its valid scope, `epsilon=0=k`, and must not become a blanket mixed-merge filter.

That restriction is explicit at `xmodel/sol-normalform.md:111-120` and `BOOK-OFFAXIS.md:317-331`. R2.2(D) says

```text
M_G = gcd(d_p,d_q),
M_G | sum(mu_e)  iff  epsilon=0 and k=0.
```

The compiler nevertheless uses it unconditionally:

```text
expand():         for MG in divs(sum(mus))       # line 121
skeleton_rows():  for MG in divs(sum(mus))       # line 140
menu_BB():        if ... or (2*mu) % MG: reject  # line 232
```

`cases/nfm_check.py:333-349` repeats the same blanket rejection in its schema helper. This is not merely a missing proof of a loop bound. It is use of a proved conditional theorem where its antecedent is false.

#### Concrete omitted 11-C record

Use the inner `G(B1,B2)` node of entry 11-C, with both B leaves still at their filed entry states:

| field | exact value |
|---|---|
| arrivals | `(mu,w,M,P)=(2,3/2,2,4)` twice |
| equal index | `i_G=P/mu=2` |
| zero/non-chain data | `epsilon=0`, one NE orbit `k=1` with `m_1=1`, `ell_ex=0` |
| orbit order | `nu_G=13` |
| shape sums | `A=2+2+1=5`, `Q=2+1=3` |
| equal-handshake data | `C_shape=mu*Q-A=1`, `E=mu+nu*C_shape=15` |
| emitted cell | `(d_p,d_q)=(65,40)`, `M_G=gcd(65,40)=5` |
| frame | `kbar_G=8`, `X_G=13`, `P_G=i_G*d_p=130` |

Every applicable local check passes:

```text
X_G/kbar_G = 13/8 = 65/40 = d_p/d_q
2*d_q = 80 > 65                         incoming searrow, twice
1*d_q = 40 < 65                         strict NE orbit
d_p != d_q, 2*d_q                       root-multiplicity guard
gcd(M_G,nu_G) = gcd(5,13) = 1
```

The handshake is also exact: `2(8-3/2)=13`. The NE charge is 5, within the td-11 budget 9. The cell is inside the compiler's own hard bounds (`k<=5`, `x<=12`, `nu<=120`). Its only rejected condition is `5 !| 4`; that condition is unavailable because `k=1`.

There is an exact coefficient witness. Set `z=eta^13` and

```text
F_B(z) = z^2 - 3z + 9/5,
N(z)   = z - 9/5,
p      = F_B(z)^2 N(z),
q      = eta F_B(z) N(z).
```

Applying the exact Lemma-M2 reduction implemented by `cases/nfm_check.py` gives

```text
F_reduced(z) = -1053/5,
C_ODE = F_reduced/d_q = -1053/200 != 0,
L3 residual = 0.
```

The remaining collision guards are nonzero:

```text
disc(F_B)=9/5,
F_B(9/5)=-9/25.
```

Thus the two B orbits are distinct, the NE orbit is distinct from them, and this is a coefficient-realized local NF object rather than a formal Diophantine row.

It extends to a complete configuration at the compiler's own decorated-skeleton tier. Let the inner emitted edge arrive at the outer root with `mu_inner=1` (legal because `1|M_inner=5`), take the filed A arrival `mu_A=1`, and choose exterior root `M_root=1`. The resulting record is

```text
hierarchy       G(G(B1,B2),A)
inner rec       (kinds=(2,2), mus=(2,2), M_inner=5) + the exact chart above
root mus        (1,1)
root M/interior (1,False)
```

That is exactly the structural level represented by the 129 nested census rows; no census row contains a completed outer ODE/refile either. Requiring more completion only for this witness would move the entire advertised nested table into FC3.

The census cannot emit it. At the inner node `sum(mu_e)=4`, so lines 121/140 offer only `M_G in {1,2,4}`. `M_G=5` disappears before NF-M, window, outer, or coefficient analysis. The emitted inner gap is `kbar_G/P_G=8/130=4/65`, so it is not independently killed by the in-window refusal used for the retained inner cells.

#### It is outside all seven stated fail-closed classes

| class | why this record is not in it |
|---|---|
| FC1 beyond-core | FC1 is expressly `deg > 94 px2 states`: states first reached beyond the P0/Dijkstra exact core (`TOWER-TD11.md:272-301,539-552`). This record reaches the inner merge directly from degree-4 entry states; its large `P_G` is a merge emission, not a beyond-core px2 predecessor. `TOWER-TD11.md:663-669` also treats merge closure as separate from beyond-core closure. Broadening FC1 to every degree appearing anywhere would be a new, materially larger condition. |
| FC2 cap-free grammar | `k=1`, `ell_ex=0`, `nu=13`, price 5; all enumerator caps are respected. |
| FC3 refile | The omission occurs at the printed node-cell tier, before Q+E5/E5F realization, exactly where the 159 rows themselves live. |
| FC4 current-state arrivals | Both children of the omitted merge are unchanged filed B entry states. Its later merge-emission arrival is the same nested mechanism already counted in all 129 nested rows; calling that FC4 would exclude the compiler's own nested table. |
| FC5 post-merge P0 | This is the merge cell, before any post-merge P0 step. |
| FC6 `nu=1` provenance | `nu_G=13`. |
| FC7 finite merge schemas / outer bounds | The schema is inside every loop bound and obeys the equal-handshake normal form. It is rejected by an invalid theorem application, not by running past a finite menu. |

Calling every omitted merge cell “schema finiteness” would make FC7 an unbounded catch-all rather than Grok's stated finite-loop/handshake-completeness rider. The honest additional condition would be an eighth class: all merges for which subadditivity authority is absent, i.e. at least `epsilon!=0 or k!=0`. Better is to fix the compiler and re-enumerate them; the answer will no longer be 159.

The scope document already warned against the promotion that occurred here: 159 is “neither mathematical lower nor upper” and post-jump `M` can add rows (`xmodel/sol-td11-13-scope.md:39-44`).

### 2. HIGH — the 159-row key is not the advertised normal-form quotient

The exact NF record at `xmodel/sol-normalform.md:74-120` and compiler interface at `:610-698` is deliberately fat. The census key is not.

| normal-form information | census representation |
|---|---|
| context `chi`: entry, labelled hierarchy, current node/edge, branch mask, zero-slot orientation | entry and hierarchy only |
| budget ledger `L`: charge atoms, exact/lower-bound authority, multiplicity partition, inventory, slack | absent |
| frame `(w,M,nu,kbar,rho,P,i,d_p,d_q,X)` at every state | root `M` only |
| complete cell `C`: Prop. 9.3 case, `l,epsilon,k,m_j,ell_ex`, factors, price authority | absent |
| cost-coupled arrival `A` and exact scale `S` | absent |
| tower history `Theta`, caps, prefix deltas and H8 scale constraints | absent |
| merge children/cases, zero mode, subadditivity authority, E5 offsets, emitted frame | inner `(kinds,mus,M)` used transiently, then discarded |
| coefficient history `Omega` and open obligations | absent |

The emitted five-field key is only

```text
(entry, hierarchy, root_mus, M_root, interior)
```

(`cases/td11_census.py:295-310,333`). A recount gives:

```text
159 generated list elements
 88 distinct five-field keys
133 distinct emitted seven-tuples
 15 five-field keys carrying conflicting stamp types
```

Hidden `recs` explain why superficially equal rows can receive different stamps, but those records are omitted from the output key. A consumer cannot map a fat NF record to a unique public row or recover which hidden decoration justified the death. This is not a merely cosmetic deduplication problem: the missing `epsilon,k,M_G` authority field is exactly how Finding 1 passed through the perimeter.

The canonical output requested by the scope includes node cells, chain paths, arrivals/E5 data, exact ODE certificate, lambda ledger, terminal reason, and raw/dedup keys (`xmodel/sol-td11-13-scope.md:119-124`). The current tuples do not implement that interface.

### 3. HIGH — entry 11-B replay succeeds only at the entry-state tier; FC4 is load-bearing

The base packet is entry type `(2,5)` with poles

```text
A: [1@3;2]       (w,M,P)=(3,1,2)
B: [3@4/3;6]     (w,M,P)=(4/3,3,6)
(k_0,l_0)=(2,5), alpha_1=5/2, pole top=7/2, caps={1,2,3,6}.
```

This agrees with `TOWER-TD11.md:91-102,193-205` and the compiler seeds.

#### All eight skeleton rows

| root arrivals | allowed root `M_G` decorations | count | stamp |
|---|---|---:|---|
| `(mu_A,mu_B)=(1,1)` | `M=1` exterior; `M=2` interior/exterior | 3 | SPINE-DEAD-H8 |
| `(mu_A,mu_B)=(1,3)` | `M=1` exterior; `M=2` interior/exterior; `M=4` interior/exterior | 5 | CLASH-DEAD |

That is exactly 3+5=8. It also explains why the withdrawn NF-D raw-P equalization is not consumed:

* On `(1,1)`, H8 requires `2 Pi_A = 6 Pi_B`, hence `Pi_A=3 Pi_B`. Legal neutral products on both entry branches are 3-free, so the `v_3` mismatch is stable at the entry-state tier.
* On `(1,3)`, H8 becomes `2 Pi_A = (6/3) Pi_B`, hence `Pi_A=Pi_B`. The empty word and `5^r` families realize equality. The census correctly sends this sibling to CLASH rather than pretending the raw degrees disagree.

#### Full CLASH extension-class covering

For the five co-scaled rows:

1. Neutral X has `g_X=(nu+1)/(2nu)` with `nu>=2` and `3 !| nu`, hence `1/2 < g_X <= 3/4`. The only resonant X is `5/4`; every padded copy is at most `5/8`. The opponent menu has maximum `5/22<1/2`. Thus the relevant prefix is empty on both the neutral and resonant branches.
2. Case A starts at `alpha_1=5/2`. For neutral X the forced denominator is `2nu`. It divides neither cap 2 nor 6: the apparent `nu=3`, cap-6 escape is illegal because `3|nu`; `nu=2` gives denominator 4. The resonant `5/4` branch likewise has denominator 4.
3. Case B is excluded by the strict gap ordering together with the promoted no-skip descent law.
4. Case C quantifies over the full alpha lattice, so it is menu-independent. CAP-DEN first forces `nu|c^2`; after the 3-free domain removes 3 and 9, the residual `nu in {2,4}` cases have denominators in `{4,8,12,24}`, none dividing caps 1,2,3,6. Resonant-X denominators are `{4,12}`. The NF-Z dagger completion explicitly adds the previously missed cap 3 and finds no escape (`TOWER-TD11.md:597-646`; `cases/tower_td11.py:847-869`).
5. The hostile quarter-register near-miss needs cap 4. Entry 11-B never has cap 4.

So I found no new entry-11-B extension outside FC1-FC7. The banked mathematical covering for the entry-state rows is sound. The compiler's own “re-derive” remains thinner: `opp_menu_max=5/22` is a constant, `ok` on SPINE is unused, and the CAP-DEN sweep samples a finite `nu` range while the infinite closure lives in the cited theorem.

FC4 is essential. The exact-core B step

```text
st96 l3 e1 k2 S4 x0 nu3: (w,M,P)=(4/3,3,6) -> (3/2,2,44), lambda=4
```

combined with A neutral `u=11`, `P_A=22`, yields current arrivals `(mu_A,mu_B)=(1,2)` and exact synchronization `22=44/2`. That arrival tuple is absent from all eight rows. It is not a new certificate break because it is precisely FC4. It does prove that “each row covers its full arrival extension class” is false unless FC4 is applied before quotienting.

### 4. MEDIUM — prior Sol perimeter findings map to the named classes, but not in the simplistic way advertised

#### The `(95,1)` grammar family

The abstract clean step

```text
(w,M)=(95,1) -> D95n48nu2,  R=97/2>47
```

is the counterexample which withdrew the universal `R<=47` grammar law (`TOWER-TD11.md:278-301`; `xmodel/sol-td11-rereview.md:22-41`). It was never shown reachable from a td-11 entry.

For the conditional certificate, the answer is **yes, with that qualification**: any td-11 realization first reached above the degree-94 exact core is FC1; if it additionally requires `k>6` or lexicographic depth beyond 40, FC2 also applies. The naked abstract grammar row is not itself a td-11 configuration. FC1 therefore fail-closes the reachable threat; it does not rehabilitate the false global grammar lemma.

#### NF-P riders

The phrase “`nu=1` provenance” does not cover NF-P as a whole:

| NF-P residue | actual owner |
|---|---|
| NF-P-OB1, reflexive/transitive state-changing reachable-numerator closure (`NF-P.md:105-110`) | FC1 beyond-core |
| NF-P-OB2, case-I `nu=1` affine-handshake provenance (`NF-P.md:111-115`) | FC6 |
| pure-(b), equal-handshake cylinders, enumerated `nu=1` modes, x-tail/resonance menus | claimed closed by the banked NF-P core (`NF-P.md:56-101`), not a fail-closed class |

Thus FC1+FC6 cover NF-P's two named open obligations. FC6 alone does not cover “the NF-P riders,” and the certificate should not say that it does. A pure dirty-chain `nu=1` issue is in current-state/chain provenance, not automatically NF-P-OB2.

The promotion ledger is desynchronized but not absent: `AUDIT.md:756-783` still reads as if the NF-P slice were open, while `notes.md:480,498,502` records the quotient lemmas, nested closure, and specifically “NF-P banked; compiler top of queue.” I therefore do not count NF-P as an unpromoted instrument; I count the stale ledger split as an audit erratum.

### 5. MEDIUM — no row relies on the known withdrawn arithmetic, but one global citation is impermissibly broad

I hunted the five stamp families against the promotion/retraction trail.

No load-bearing row death reuses the known withdrawn result:

* 11-B SPINE uses the correct `(mu_A,mu_B)=(1,1)` comparison `2/1` versus `6/1`; the equalized `(1,3)` sibling is routed to CLASH.
* OUTER uses the corrected closed form including the `A<Q` cases (`cases/td11_census.py:251-276`); the round-8 DEAD-WINDOWED/sign shortcut is not the live reason. The 129 nested deaths are promoted in `AUDIT.md:773-782` and the later ledger.
* The td-7 regression uses the current 17 cells, not the stale six-cell layer.

The citation offender is the global preamble at `cases/td11_census.py:13-19`, which lists “NF-D mechanisms” among banked theorems quotienting the **full chain/word extensions**. Read literally, that cites a retracted instrument. `NF-D.md:3-23,216-227` says every td-11 depth value remains OPEN and withdraws the old empty synchronized-depth enumeration. Only narrower pieces such as M-drop D5 and co-scaling windows survive. `TOWER-TD11.md:45-51` states this correctly, and the later full-word kill is the entry-specific DIE horn at `TOWER-TD11.md:597-646`.

Required correction: replace the broad `NF-D mechanisms` citation with the exact surviving lemma ids (for example D5 where used) and cite the td-11 DIE horn for full-word closure. I found a bad global provenance claim, not a 159th-row counterexample independently made live by a withdrawn theorem.

Three additional audit-theater findings agree with Grok:

* `stamp_two_pole()` computes `ok` and never consumes it (`cases/td11_census.py:291-297`); SPINE is stamped unconditionally.
* NF-P gate summary checks F1/F2 end in theatrical predicates such as `... and True` and `9 == 11-1-1` (`cases/nfp_check.py:304-320`). The underlying D1/D2 arithmetic is real; those summary lines are not the proof.
* td-7 computes `kbar`, `X`, N1 and P3, but its death uses the same shared CAP-DEN/window predicate for all 17 cells (`cases/td11_census.py:401-416`). It is a useful identity regression, not replay through the full td-11 stamping engine.

The three BB2 composite rows are also better labelled `SPLIT` (cylinder self-refused, discrete alternatives outer-dead) than simply `SELF-REFUSED`; their deaths are recoverable, but the current stamp obscures the actual instruments.

## Final assessment

**CONDITIONAL EMPTINESS is not earned as stated, even with Grok's seventh class added.** What is earned is narrower:

* the program deterministically constructs 159 list elements and assigns all of them a death label;
* the entry-state 11-B eight-row covering survives full replay, conditional on FC4 and the existing exact-core/bounds perimeter; and
* the corrected NF-M/OUTER arithmetic and td-7 shared primitives pass their regression gates.

What is not earned is the universal set statement. The omitted 11-C chart is finite, in-bound, entry-state, `nu=13`, pre-P0, coefficient-realized, and outside FC1-FC7. It is deleted solely because the compiler discards the normal form's `subadditivity_authority` field and applies a conditional theorem unconditionally. One such object is enough to break the certificate, whether or not its eventual global completion dies.

Minimum repair:

1. Remove blanket `M_G|sum(mu)` filtering from `expand`, `skeleton_rows`, `menu_BB`, and the NF-M checker. Derive `M_G=gcd(d_p,d_q)` from each exact cell and require divisibility only when its authority predicate proves `epsilon=0=k`.
2. Re-enumerate the 11-C inner and outer cells. Do not retain “159” as an expected theorem count.
3. Emit the fat record, including current arrivals, node cells, coefficient certificates, budget ledger and `subadditivity_authority`; make deduplication and stamp selection functions of that record.
4. Turn FC1-FC7 into executable predicates and test an exhaustive disjoint-or-explicitly-overlapping cover. If maintainers prefer to fail-close all non-authorized-subadditivity merges, declare an eighth class explicitly; that would be a weaker new conditional theorem.
5. Narrow NF-D citations, distinguish composite SPLIT stamps, and make the gates consume the arithmetic booleans and promotion ids they claim to audit.

Until then the honest status is: **159 frozen diagnostic occurrences locally stamped; seven-class conditional emptiness OPEN.**
