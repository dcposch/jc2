# Hostile review (Opus 5): corrected q=6 affine-ADE threat map v2

Date: 2026-08-30 UTC
Reviewer: Opus 5, different-model hostile review
Charged basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`
Receipt status: `ABSENT` (no exit-price assertion; no `charge_basis` line)

## 0. Custody

All ten charged SHA-256 values reproduce byte-exactly. Derived checks:

```text
v2 body 14628 bytes 03590225ea52239df4d485b4b7aaac015af4d4e8975aba299b637663f6ce2f34  MATCH manifest
local audit body     941d4e27b95bee2483b98fa62c4e1b9c9b94e7dff7aa200848ab03977461522d  MATCH v2 §2
```

Note, not a defect: v2 §2 cites `a5bf78c8...` as "binding normal-F5
carrier/effectivity integration". That digest resolves to
`bd-a2-normal-f5-decorated-carrier-effectivity-reduction-coordinator-integration-sol56-20260830.md`
(verified present at that hash), **not** to the quadratic-incidence
integration `17f41e70...` in my charge list, which v2 never cites. The
citation is accurate; the quadratic-incidence file is context only.

No `jc2-lean` access, no D3 report, no sibling external-model prompt/log/
receipt, no heavy CAS, no web. No charged file, artifact, or Git state edited.

---

## 1. Global marked-surface formulas — `CONFIRMED`

Reconstructed independently on `Bl_9 F_2` with `S0^2=-2, S0.F=1, F^2=0,
P_i^2=-1`. For `C=aS0+(2a+eps)F-sum x_iP_i` and a test class
`alpha S0+beta F` one gets `(alpha S0+beta F).C = alpha*eps + beta*a`
(the `-2a alpha` and `+2a alpha` cancel — this is the factor of two the
`2a` coefficient is designed to absorb). Hence:

* `A = 2S0+5F-sum_i P_i` gives `A.C = 5a+2eps-sum_i x_i = d`.  **(1.1) ✓**
* `T = S0+3F-sum_(I)P_i` gives `T.C = 3a+eps-sum_(I)x_i = t`.  **(1.1) ✓**
* `F.C = a`. This is the divisor v2 §4 uses, and it is the correct source of
  `a>=0`: `F` is nef with `F^2=0`, so `pi^*F.C_j>=0` for every effective
  `C_j`, with equality iff `C_j` is fibre-contained. **The v2 correction is
  right and v1's `a_j>0` was genuinely unjustified.**
* Adjunction. With `K=-2S0-4F+sum P_i`,
  `C^2+K.C = 2a^2+2a*eps-sum x_i^2 - 4a - 2eps + sum x_i`, and
  `a-d = -4a-2eps+sum x_i` identically. So the code's
  `num = 2a^2+2a*eps-sum x^2+a-d`, `delta = 1+num//2` is exactly `p_a(C)`,
  and `delta>=0` plus the parity filter are the correct necessary
  conditions. **✓** Signs and every factor of two check out.
* Totals. Matching `S0`- and `F`-coefficients of `C_tot=4S0+9F-sum c_iP_i`:
  `sum w_j a_j = 4` and `2*4 + sum w_j eps_j = 9`, i.e. `sum w_j eps_j = 1`.
  **(1.2) ✓, factor of two correct.** `sum w_j t_j = 1` is `T.C_tot = 1`,
  and the code's `validate_marking` verifies `13 - sum_I c_i = 1` for both
  `BASE_C` and `TAU0_C`. With one `Z=S0+2F-sum_(5 pts)P` subtracted,
  `A0=3` and `eps` total is unchanged at 1; `total_after_carrier` enforces
  the matching drop `14 -> 9`. **✓**
* `weighted_unit_contacts` is complete: `sum w_j eps_j=1` with `w in {1,2}`
  and `eps_j>=0` has *only* unit-vector solutions at weight-one indices. **✓**
* `x_L` is structurally forced to zero (`c[L]=0`, `L` in no coordinate
  block). Consistent, not an omission. **✓**

## 2. The `a>=0` correction and the `a=0` classification — `CONFIRMED` for the stated claim; `GAP` on its hypothesis

**Proof reproduced.** If `a_j=0` then `d_j = 2eps_j - sum x_ji`. If
`eps_j=0` then `d_j<=0`; so `d_j>0` forces `eps_j>=1`, and `sum_k w_k eps_k=1`
with nonnegative terms forces `w_j=1, eps_j=1`, whence `d_j = 2-sum x_ji <= 2`.
**(1.3) `CONFIRMED`.**

**Complete list.** With `a=0, eps=1`: `C=F-sum x_iP_i`, `d=2-sum x_i`,
`t=1-sum_(I)x_i`.
`d=2` forces `sum x=0`, i.e. `C=F`, `t=1`.
`d=1` forces one `x_i=1`; `i in O` gives `t=1`, `i in I` gives `t=0`;
`i=L` is excluded by `c_L=0`. Both have `num=-2`, `delta=p_a=0`.
**(1.4) `CONFIRMED` and complete — no omitted `O`/`I` or infinitely-near
label.** For positive-rank allocations the `x`-support is further tied by
root-chain differences, but the *label set* is not truncated: for rank-zero
allocations `group_vectors` ranges over all of `I` and `O` with singleton
blocks, so every infinitely-near label is reachable.

**Coefficient-two owners.** A weight-two prime cannot own the unit `eps`, so
`a=0` gives it `d<=0`. **`CONFIRMED`.** This is why `U3` (degrees 4+4), the
odd `Delta=0` block (4+4) and both doubled blocks (weight-2 leg) gain nothing.
I verified this *numerically and independently* (§8): restricted to
`min(a)=0`, my from-scratch enumerator produces **0** admissible metadata in
`U3`, `U3+Z`, `odd`, `odd+Z`, `doubled`, `doubled+Z` — the six cells of (3.1)
— and nonzero metadata in exactly the eight cells v2 lists.

**Reducibility hidden by "physical prime".** Charged local audit §6 supplies
the missing licence: a single global irreducible prime carrying two distinct
local branches would attach one vertex to two resolved leaves and create a
cycle, so the forest forces distinct branches onto distinct global primes;
a doubled Cartier coefficient creates no second vertex. The one-prime-per-
branch ansatz is therefore justified, not assumed. **`CONFIRMED`.**

**`GAP` — degree-zero components (the one real omission I found).**
(1.3) is stated and used under the hypothesis `d_j>0`, which v2 never
justifies, and (1.1) lists nonnegativity for `a,eps,t,x` but **not** for `d`.
The polarization `A=2S0+5F-sum P_i` is nef but **not ample**:
`A.(F-P_i-P_j)=0`, and `F-P_i-P_j` is effective whenever two marked centres
lie on one fibre. Such a component is vertical (`a=0`), has `p_a=0`, may
carry the unit `eps`, and consumes part of the `c` budget — yet it is
outside the enumeration, because `analyze_cell` fixes `k` primes with
`sum w_j d_j = 8` from the local census, which counts only germs *at* the
F5 cluster. v1's blanket `a_j>0` excluded this case trivially; v2, having
opened the `a=0` domain, now owes it. This is a scope gate, not a refutation:
it does not produce a survivor, but it means the classification in §1 is
complete only **within** the fixed-degree-multiset ansatz.

## 3. Local vs global verticality — `CONFIRMED`

The local model `f=h+uv` (audit §2.3, `a=c=0,b=1`, `p=h_z`) establishes
exactly one thing: the polar can have a **Cartier factor of coefficient two**
on the reduced vertical prime `{v=z=0}` of local `A`-degree one. It licenses
the weight vector `(1,1,2)` in `B3_tau0_doubled_residual` and `(1,2)` in the
nonzero-modulus doubled block. v2 §1 correctly refuses to promote it to a
global `B.C=0` class, and (1.3) independently forbids that promotion.

No tau-zero or doubled block is globally misclassified. Verified numerically:
in `B3_tau0_doubled_residual` (degrees `(4,2,1)`, weights `(1,1,2)`) the only
`a=0`-eligible leg is branch 1 — weight one, degree two — exactly as v2 §1
asserts ("gain candidates only through their separate coefficient-one
degree-two prime"). The weight-two leg contributes zero `a=0` metadata.

## 4. Local analytic census — `CONFIRMED` (conditional on the audit's own review gate)

Rebuilt from the charged audit and cross-checked against the engine's `jobs`
table. Every stratum maps to a registered cell with `sum w_j d_j = 8`:

```text
U3/A3           m=(2,2,1) n=2e1+e2        4+4          (1,1)
B3 tau!=0 D!=0  m=(2,1)   n=3e1           4+2+2        (1,1,1)   pair zero
B3 tau!=0 D=0   ord d even  -> 4+2+2 (1,1,1) tangent:1,2   [lambda=k]
                ord d odd   -> 4+4   (1,1)   pair zero
                d=0         -> 4+2·2 (1,2)   pair zero
B3 tau=0        m=(2,2)   n=(2,2)  c=(0,2,0,2,...)
                D0!=0       -> 4+2+1+1 (1,1,1,1) pair zero
                D0=0 even   -> 4+2+1+1 (1,1,1,1) tangent:2,3
                D0=0 odd    -> 4+2+2   (1,1,1)   pair zero
                D0=0 d_R=0  -> 4+2+2·1 (1,1,2)   pair zero
```

Nine strata, ten `tau!=0` jobs (five ± `Z`) and four `tau=0` jobs (no `Z`,
per audit §0.4 — subtracting a carrier from `(0,2,0,2^6)` would need a
negative centre multiplicity). **14 jobs; the registration is exhaustive.**
I found no missing analytic stratum: the Weierstrass trichotomies in (2.9)
and (2.16) are exhaustive over `C[[r]]` (even order ⟹ analytic square root;
odd order ⟹ nonsquare, ramified; zero ⟹ literal square), and the residual
site polynomial (2.14) is checked never to collide with the node.

Local pair rule: the engine's `tangent:i,j` accepts **any** `lambda>=1`, not
`lambda=k`. Audit §6 licenses only `C_i.C_j = lambda_ij` exactly, so the
engine's condition is a strict **relaxation** — the safe direction for an
elimination. **No wrong local pair rule found.**

## 5. Affine-root domain, caps, orientations, carriers — `CONFIRMED_WITH_CORRECTIONS`

* Euler rank cap. `expected_cap = 8 - local_rank - k - (1 if Z)` is enforced
  by `require` for all 14 jobs; I recomputed each and all match.
* `component_patterns` derives `-base <= delta_i <= rank*base` from
  `C_A m >= 0` (nonincreasing `delta`) plus residual effectivity — a proved
  bound, not an arbitrary cutoff. `allocation_orbits` canonicalises by
  ordered coordinate chains and guards duplicates by serialization.
* Root orientation is carried by chain order; `component_contacts` enforces
  `z_contact >= 0`, at most one positive `Z` edge and at most one positive
  strict edge per component; `total_after_carrier` enforces the exact
  `14 -> 9` drop. `carrier_representatives` quotients by allocation
  automorphisms. Chronological `O` filter is applied only as a *diagnostic
  partition* of the minima, never as a domain restriction. **✓**
* **CORRECTION / load-bearing finding.** v2 §4 says "the result is
  independent of the conceptual lower bounds and of unresolved same-owner
  carrier triples". That is true and I verified it. But the result is **not**
  independent of the root/block machinery. I ran a relaxed superset that
  keeps every shifted total `c` reached by the allocation walk and drops
  `connected_coordinate_blocks`, `branch_differences` and the owner map
  entirely:

```text
relaxed pair matches, all 14 affine cells: 11
  B3_tau_ne0_Delta_ne0                4
  B3_tau_ne0_Delta0_doubled           2
  B3_tau_ne0_Delta0_doubled_plus_Z    1
  B3_tau0_odd_residual                4
```

  So `branch_differences`/`connected_coordinate_blocks` are genuinely
  load-bearing for the *overall* zero. They are unchanged from v1, so this is
  an inherited dependency, not a v2 regression — but v2's §4 sentence should
  not be read as "the enumeration needs nothing but the exact join."
  **Decisively for v2: every one of the 11 has `min(a)>=1`, i.e. all lie in
  the old positive-only domain. The newly admitted `a=0` slice has zero pair
  matches even in the relaxed superset (§8).**

## 6. Candidate generator and coordinate-block solver — `CONFIRMED`

* `branch_candidates` splits `sum_i x_i = 5a+2eps-d` into `sum_I x_i` and
  `sum_O x_i` using `t`; rejects negative partial sums; bounds `x<=c//w`
  per branch; applies the parity and `delta>=0` filters. Matches §1. **✓**
* Divisibility by Cartier weight is enforced twice — in `owner_options`
  (`residual % weight`) and again inside `branch_differences` via `require`.
  Bounds are `c // weight`, and the join's residual reconstruction rejects
  `remaining % weight != 0`. **✓** No unweighted/weighted confusion found.
* Strict total. The join imposes `sum_j w_j x_j = c` exactly, reconstructing
  the last branch from the residual rather than taking a Cartesian product.
  I re-derived the same counts with a naive full Cartesian product (§8):
  identical. **✓**
* Pair conditions are applied to **reduced** classes with the correct
  `2a_ja_k + a_j eps_k + a_k eps_j - <x_j,x_k>`, and are checked
  incrementally *and* at the terminal branch. `lambda_counts` records the
  tangency value. **✓**
* Ordering. `pair_condition_matches_before_carrier` is incremented **before**
  `carrier_forest_profile` is called. The zero is therefore genuinely
  pre-carrier; the unlabelled-cycle and `FOREST_UNRESOLVED_*` retentions
  never bind. **✓ Confirmed by reading and by the counters.**
* Latent fail-closed edge, probed and clear: `aggregate_cross_lower_bound`
  contains `require(a_left>0 and a_right>0)`, reachable only after a meta is
  branch-feasible. Under the nonnegative domain a zero block sum would abort
  the whole run. I instrumented it: **0 such events** across all 28 rows. It
  never fires and never silently truncates.

## 7. Replay programs — `CONFIRMED`

Read both in full (1042 + 217 lines).

```text
v2 pins v1 by SHA before import                                         ✓
only mutation to the engine: module-global weighted_positive_compositions ✓
ordinary / -O / -OO : byte-identical, 37859 bytes,
  27ca7c500f411843c34c1aad60d51261b6e66e9ba712eddf48aa67893add8f3e      ✓ (= §7)
corrected raw   33d8841e0609857220f80fc3d46e8a33ccfc655ef19bfb42b465ee802ae13216 ✓
positive control 293f2aee078dbcb0448c57ce4720646503719e2596a9454e709736baa041d602 ✓
  (= standalone `python3 ops/q6_f5_affine_ade_threat_replay.py | shasum`)
AST assert nodes: v1 = 0, v2 = 0                                        ✓
--mutate-drop-vertical  rc=1 "FAIL:vertical a=0 domain was not exercised"
--mutate-contact        rc=1 "FAIL:q6 baseline multiplicity sum must be fourteen"
  both, in ordinary, -O and -OO                                         ✓
```

False-comparison attacks, all negative:

* **`lru_cache` state.** The only caches are `permutations_i()` (constant)
  and `branch_candidates`, keyed on `(c, allocation_serial, differences, a,
  degree, eps, t)` — none of which depends on the composition generator, and
  the body never calls it. The cache is a pure memo.
* **Two `main()` calls on one module.** I ran three configurations:
  (A) shared module, corrected-then-positive (v2's own order);
  (B) shared module, **reversed** order; (C) two **fresh** module objects,
  one per generator. All three give identical raw SHAs for both domains.
  No cross-run contamination.
* **Monkeypatching.** `analyze_cell` resolves `weighted_positive_compositions`
  as a module global at call time, so the substitution really reaches the
  engine — confirmed by the `--mutate-drop-vertical` old-pass/new-fail
  behaviour and by the nonzero deltas.
* **JSON canonicalisation.** Both runs use `sort_keys=True,
  separators=(",",":")`; the delta is computed on parsed integers, not on
  text. `vertical_class_control` runs before either `main()` and only
  populates a pure memo.
* **Optimisation flags.** All control flow uses `require()` raising
  `RuntimeError`, never `assert`; `-O`/`-OO` are inert (verified by
  byte-identical output and identical mutation diagnostics).
* **Import side effects.** `exec_module` runs only definitions; `main()` is
  guarded by `__name__ == "__main__"`.

Timing on this desk: 3.5 s, standard library only. No AWS, no CAS.

## 8. Independent verification of every delta — `CONFIRMED` (v2's claim is provable in a stronger form)

Driver written from scratch (no import of the v2 wrapper), fresh modules,
reversed order. **All 28 rows of §3 reproduce exactly**, including every
`v1 -> v2` count and every added-candidate figure:

```text
affine added metas   16,28,16,28,7,7,2,7                  = 111  ✓ (§3)
rank-zero added      4,2,4,2,7,7,4,1                      =  31  ✓ (§3)
total added metas 142, added join metas 142, added candidates 3317 ✓ (0.2)
pair_condition_matches_before_carrier = 0 in all 28 rows        ✓
survivor payload 830 bytes ab2fc3c6c5d47160fa947542dd5d33e375c9221a43df05c10cd99cfb6926b46d ✓
six inventory digests of §5                                     ✓ all six
both full tables of §5 (orbits / feasible allocations / join metas /
  candidates / matches / survivors, affine and control)         ✓ every cell
```

**Conceptually independent enumerator (no charged code at all).** For the 14
rank-zero controls I enumerated directly from the divisor identities:
`a` over all nonnegative weighted compositions, `eps`/`t` over weight-one
unit vectors, `x` over the full box `0<=x_i<=c_i//w_j` split by the `I`/`O`
sums, adjunction parity and `p_a>=0`, then a **naive Cartesian product**
checking `sum_j w_j x_j = c` and the pair rule. Result:

```text
join metas   6,2,15,3,15,3,6,2,1,1,8,8,13,2   identical to v2 baseline_controls
candidates   972,72,1623,134,1623,134,972,72,141,21,664,664,827,112  identical
pair matches 0 in all 14                       a=0 metas 31 (= §3 total)
```

**Relaxed superset over the affine cells, restricted to the newly admitted
slice `min(a)=0`:** keeping every shifted `c` but discarding all root/block/
owner/carrier structure, the `a=0` slice yields
`68,34,68,34,0,0,0,0,53,53,32,14` admissible metadata rows (a superset of the
16/28/16/28/7/7/2/7 the engine admits) and **zero pair-condition matches in
every cell**. So the v2 correction is safe for a reason stronger than v2
claims: the `a=0` domain is eliminated by the class identities, adjunction and
the weighted equality alone, independently of the affine-root machinery,
the energy bounds, and the carrier filter. It also independently reproduces
(1.3): the six cells of (3.1) admit **no** `a=0` metadata even in the
relaxed domain.

## 9. Energy and block-separation inequalities — `CONFIRMED`, and none is load-bearing

* (4.1) uses `x^2>=x` only; it is valid verbatim for `a>=0`. **✓**
* (4.2) is `2a_Ga_H + a_G eps_H + a_H eps_G - sum(c^2-c)/2`, correct for the
  weighted block/complement pair; its internal positivity `require` never
  fires (§6). **✓**
* Every entry of the §4 chronology-filtered minima table and of (4.3)
  reproduces exactly from the run
  (`minimum_chronology_branch_feasible_energy` /
  `minimum_chronology_feasible_aggregate_cross_bound`).
  Note the doubled `Delta=0` row: raw minimum is `0`, chronology-filtered is
  `1`; the report's `1` is the chronology-filtered value, correctly labelled.
* `energy_pruning_applied = false` in **all 28 rows**. **No inequality prunes
  any executable metadata row; none is load-bearing after the exact join.**
  The report says exactly this, and it is true.
* The `0` in the `tau=0` doubled row is honest and correctly not repaired.
  The offered replacement kill is sound: in that cell the only `a=0`-eligible
  leg is the weight-one degree-two prime, `a=0, eps=1, d=2` forces `sum x=0`,
  i.e. `C=F`, and `F.C_0 = a_0 >= 1` for the degree-four companion, breaking
  `pair_mode="zero"`. The generalisation ("kills every newly added degree-two
  vertical branch with a distinct-site degree-four companion") is correct for
  the same reason.
* **Minor correction.** §4's closing sentence says degree-one vertical
  candidates "remain covered by (4.1)--(4.2) and the exact join". Since
  (4.1)--(4.2) prune nothing, only the exact join covers them. §4's own next
  paragraph states this correctly; the two sentences are in tension. Read:
  *covered by the exact join alone*. My §8 relaxed check independently
  confirms those degree-one candidates die.

## 10. Verdicts

| object | verdict |
|---|---|
| Local analytic census (`U3/A3`, full `B3/A2` modulus, tau=0 residual, doubled strata, pair rules) | `CONFIRMED`, conditional on the charged audit's own outstanding review gate |
| Corrected global vertical classification (`a>=0`, (1.3), (1.4), local-vs-global separation) | `CONFIRMED` as stated; `GAP` on the unjustified hypothesis `d_j>0` (item 2) |
| Finite enumeration software (v1 engine + v2 wrapper, deltas, controls, mutations) | `CONFIRMED` |
| Conditional maximum theorem | `CONFIRM_WITH_CORRECTIONS` |

**v1 is correctly superseded.** Its `a_j>0` restriction was unjustified;
`a_j=F.C_j>=0` is the right constraint and v1's exact output is faithfully
reproduced by v2's positive-only control.

### Maximum-safe theorem

> Fix the quadratic-F5 frame and the charged binding Euler/`A1`-ruling,
> rational-forest, and normal-F5 carrier/effectivity inputs. Assume the
> charged q=6 local contact audit, so that the strict polar decomposition at
> the F5 cluster is one of the nine registered `(degree, Cartier weight, pair
> rule)` strata of total weighted `A`-degree eight, with strict total
> `(0,1,1,2,2,2,2,2,2)` for `U3` and `B3, tau!=0` (optionally minus one
> contracted carrier) and `(0,2,0,2,2,2,2,2,2)` for `B3, tau=0` (no carrier).
> **Assume in addition that the marked class `4S0+9F-sum c_iP_i` has no
> component of `A`-degree zero**, so that its reduced strict primes are
> exactly those registered germs. Then, admitting every reduced strict prime
> with `B`-degree `a_j = F.C_j >= 0` — including the three global vertical
> classes `F`, `F-P_o`, `F-P_i` — the necessary-lattice enumeration over all
> affine-ADE root allocations within the Euler rank caps, together with the
> rank-zero controls, contains **no configuration satisfying the local pair
> conditions**, in all 28 rows, **before** any carrier-forest or
> unlabelled-cycle filtering. Hence neither `U3/A3` nor any `B3/A2` modulus
> admits a necessary global boundary configuration in the q=6 frame.

Scope gates preserved in full: this is a **necessary-lattice** statement. It
does not prove that the quadratic frame occurs, that any lattice row is
effective, anything about a nonquadratic incidence, the existence of a
polynomial map, or JC2. `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`; no
attainment is claimed anywhere here.

### Exact corrections required before integration

1. **Add the `d_j>0` scope gate.** State explicitly that `A=2S0+5F-sum P_i`
   is nef but not ample, that `A.(F-P_i-P_j)=0`, and that the enumeration
   assumes no `A`-degree-zero component. Either discharge it or carry it as a
   named hypothesis. (Item 2 `GAP`.)
2. **Weaken the §4 independence sentence.** The zero is independent of the
   energy bounds and of the carrier/unlabelled-cycle filter — verified — but
   **not** of `connected_coordinate_blocks`/`branch_differences`, which
   remove 11 positive-`a` pair matches present in the relaxed superset.
   Those 11 are entirely in v1's domain, so v2's own delta is unaffected.
3. **Fix the §4 closing attribution:** degree-one vertical candidates are
   covered by the exact join alone, since `energy_pruning_applied=false`
   in all 28 rows.
4. Optional strengthening, now provable: the `a=0` slice dies under the class
   identities, adjunction and the weighted equality alone (§8), with no
   affine-root, energy, or carrier input. Recording this makes the v2
   correction robust to any future revision of the root machinery.

### Dependencies

Charged local contact audit (its own different-model review still open);
the binding Euler/`A1`-ruling, rational-forest, and normal-F5
carrier/effectivity integrations; `sum w_j d_j = 8`; the forest one-branch-
per-prime licence (audit §6).

### Cheapest decisive successor

Discharge correction 1. Concretely: on the completed incidence, decide
whether the polar `p=f_z` can have a component of class `F-P_i-P_j` (or any
`A`-degree-zero class) for some pair of marked centres of the charged
nine-blowup — equivalently, whether two of the nine centres are fibre-
collinear in the chronology. This is a small explicit chart computation on
the already-charged local model, needs no CAS and no new enumeration, and it
is the only remaining door through which the `a>=0` correction could still
be incomplete. If it closes, the conditional q=6 closure is integrable as
stated above with hypothesis 1 removed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23422`.
- Body SHA-256:
  `c968ed6f60b3cd65868050a49180a5f5bbc37ae2241042e9aa6870290f75c90f`.
- Frozen basis: `aeb4b256daf459b16548d87225d8c1dc34a87904`.
