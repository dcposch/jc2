VERDICT: STILL-BROKEN

The round-3 restatement honestly accepts most of the prior review: the budget-5 erratum and ratio-4 counterexample are recorded, nested 11-C is no longer claimed, the formal NF-D corollary is restricted to single-word-deep configurations, and the census is called a template rather than a certificate.  The remaining break is narrower but load-bearing: B9d's budget-9 cutoff uses a false universal bound on the `px2` grammar, so OB-6 and hence the theorem at its advertised `px2-MENU-SLICE` tier are not proved.  This is a certificate break, not an exhibited tower survivor.

## Findings, ranked

### 1. CRITICAL — the degree-aware budget-9 cutoff rests on a false `R <= 47` grammar law

The accepted parts replay exactly.

* `TOWER-TD11.md:236-244` correctly says the old `21+347+69` audit was budget 5, retires `R* < p`, and records the reachable ratio-4 path.  Direct engine replay gives costs `4,2,1` on

  ```text
  (3,2) --(20,16),l=2--> (3/2,4)
        --(40,16),l=4--> (3/4,8)
        --(18,9),l=8-->  (4/9,9),
  ```

  so the last row is present by total price 7.  Its preceding full degree is `4*(20/2)*(40/4)=400`, its ratio is `9*8/18=4`, and its gap is `4/400=1/100`.  Ledger row 8 (`TOWER-TD11.md:433`) is accurate.
* `TOWER-TD11.md:257-270,470-477` candidly says the two large full closures were not run and limits the claim to the inherited `px2` menu slice.

The replacement cutoff is not valid, however.  `cases/tower_td11.py:657-661,727-735` says **every** `px2`-grammar step has ratio at most

```text
47 = 1 + k_max + lex_max,
```

then `b9_audit` stops expanding every state of full degree greater than 94 (`:696-705`).  The `k <= 6`, `lex <= 40` caps govern the dirty branch at `cases/scratch_offaxis_pricing/px2.py:77-125`; they do not govern the separate clean-resonance branch at `px2.py:45-60`.  For a clean row,

```text
R = (n*nu+1)/nu = n + 1/nu,
```

and `n` is controlled by `num(w)`, not by `k` or `lex`.  A concrete engine grammar row is

```text
(w,M)=(95,1) -> clean D95n48nu2,
R = 97/2 > 47.
```

This is a counterexample to the asserted grammar law, not a claim that `(95,1)` is reachable from a td-11 seed.  That distinction does not rescue the proof: menus are cached only after the `deg > 94` early exit, and `rb` quantifies only over that low-degree cache (`tower_td11.py:704-720`).  Thus B9d checks the reported `12/10/8` cores and assumes, rather than proves, safety of every descendant.  No reachable-state invariant relating `num(w)`, clean `R`, and full degree is stated or cited.  My complete budget-9 state closure for `(3,2)` had maximum clean ratio `7/2`, but that empirical fact neither proves the cutoff law nor covers the two expressly unclosed seeds.

The theorem aggregate has a related wiring defect: `tower_td11.py:755-764` conjuncts the old budget-5 `AUD` ratio condition and never conjuncts the B9 result.  B9d remains a separate script-wide check, so a Boolean failure there would still make the process exit nonzero, but the advertised aggregate row does not replay its own budget-9 premise.

Perimeter clause (iv) cannot silently supply the missing proof.  B9d and §7.5 claim all steps in the `px2` grammar, while §9 invokes that audit and also treats named clean resonances.  If the intended tier excludes every other resonance-bearing descendant, the audit and theorem must say so and prune that branch; they cannot use the false all-grammar bound.

### 2. MEDIUM — the corrected 145/34 layer and direct verdicts are genuine, but the current-state wording is broader than SK3

The OB-8 repair itself passes.

* The corrected independent-parent-edge expansion at `tower_td11.py:531-604` gives

  ```text
  direct                 16 / 0 mixed
  G(G(A,B1),B2)          40 / 8
  G(G(A,B2),B1)          40 / 8
  G(G(B1,B2),A)          49 / 18
  total                 145 / 34.
  ```

  The old conflated rule independently regresses to `103/25`.
* The classifier tests hierarchy first (`tower_td11.py:605-619`): every non-direct row is unconditionally `OPEN`.  It therefore never stamps any of the 129 nested rows dead.
* The 16 direct rows replay as 13 `SPINE-DEAD` and 3 `CLASH-DEAD`.  Incoming root `mu` patterns `(1,1,1)`, `(1,1,2)`, and `(1,2,1)` contribute `3+5+5` decorations; a `mu=1` B-edge forces `Pi_A=2 Pi_B`, impossible because both products are odd.  Pattern `(1,2,2)` contributes three root decorations and is the inhabited co-scaled CAP-DEN case.  Thus the direct verdicts are substantive, not a count-only assertion.

This fully answers the prior nested-composition objection: `TOWER-TD11.md:292-305` says 129 OPEN and explicitly says OB-8 is not fully discharged.  One scope sentence remains too broad on its face.  SK3 fixes the static leaf vector `BS3={1,2,2}`; it does not enumerate post-jump current-`M` decorations.  Section 10 correctly sends decorations outside the audited class to OPEN (`TOWER-TD11.md:418-420`), whereas the theorem says “all `mu`-assignments ... including current-state classes” (`:339-342`).  That phrase must be read through §10(b), or narrowed; SK3 is not evidence for the broader reading.

### 3. MEDIUM — the formal §9 corollary now matches the prior perimeter objection, but stale all-depth claims remain

The controlling corollary at `TOWER-TD11.md:374-389` makes the requested restriction exactly: it covers only configurations whose below-`theta*` deep zone is single-word, identifies sufficiently large co-scaled `Pi_1=Pi_2=5^k` tails as two-word coexistence, and leaves that slice **OPEN**.  Perimeter clause (ii) repeats the exclusion at `:466-477`.  `cases/nfd_check.py` also continues to report `D(11-A)=D(11-B)=D(11-C)=OPEN` for the equalized family.  This repairs the §12-perimeter objection at the formal theorem/corollary location.

The restatement is not textually clean yet.  Section 5 still says every neutral word, every depth, and the `Pi=5^k` family close (`TOWER-TD11.md:113-123`), and gate row X3 still says the td-11 depth question “closes entry-wise WITHOUT a depth cap” (`cases/tower_td11.py:222-229`).  Those statements are the withdrawn claim and contradict §9.  The formal §9 restriction should control, but “no residual overclaim” is not yet true.

### 4. CONFIRMED — ledger row 5 is a real escape shape and is excluded only entry-pairwise

The arithmetic is exact.  Starting from `alpha_1=3/2`, an allowed abstract cap-4 prefix update with `(k,l)=(4,3)` gives

```text
alpha' = 3/2 + 3*(4-1)/4 = 15/4 == 3/4 (mod 1).
```

Against `nu=2`, `gap(X)=3/4`, hence

```text
r = 3/4 - 1 + 3/4 = 1/2,
den(r)=2 | 2.
```

So it is a genuine Case-C escape shape.  It is not an entry escape: 11-A and 11-C have the `w=2` X-domain and forbid even `nu`; 11-B permits `nu=2` but has cap history `{1,2,6}`, never 4, so it has no quarter-register history.  `tower_td11.py:374-410` and ledger row 5 at `TOWER-TD11.md:430` correctly encode the lesson that dynamic-cap sweeps must remain entry-paired.

### 5. LOW — §10 is an honest fail-closed template, but not an implemented perimeter classifier

As prose, §10 is honest about what remains.  It says the td-11 Q+E5/E5F census does not exist and that it is not an emptiness certificate (`TOWER-TD11.md:391-397`).  Its three conjuncts require entry mapping, membership in the audited hierarchy/decoration class, and the corrected perimeter; every failure becomes OPEN (`:399-412`).  Together with §12's list of nested rows, multi-word depth, the capped engine horizon, `nu=1`/resonance material, and the unknown Q+E5/E5F refile (`:466-477`), this is a fair description of the work still required for a td-11 panel closure.

The sentence that the gate “implements exactly this classifier” (`:414-415`) is too strong.  SK3's row is only `(mus, mixed-count, M_root, interior)` and checks the hierarchy/direct-`mu` split.  It has no fields for deep-zone multiplicity, menu horizon, budget, resonance, mapping, or refile status.  Conjunct (c) is therefore a required future compiler precondition, not something the current 57-row gate enforces.  This does not make the template dishonest; it prevents treating it as an executable panel certificate.

## Gate replay and final disposition

```text
python3 cases/tower_td11.py  -> exit 0, ALL 57 CHECKS PASS
python3 cases/nfd_check.py   -> exit 0, ALL 22 CHECKS PASS
```

The green count confirms the corrected arithmetic, 145-row classifier, direct verdicts, and ledger row 5.  It does not validate the high-degree cutoff because B9d tests its false bound only on the low-degree cache.

Answers to the requested checks: (1) the erratum, retirement, and row 8 are correct, but the replacement budget-9 audit and “no residual overclaim” are not; (2) yes, all 129 nested rows remain OPEN and all 16 direct verdicts replay; (3) the formal §9 restriction matches the prior objection exactly, though §5/X3 remain stale; (4) yes, row 5 is real and correctly entry-paired; (5) the census template plus perimeter is an honest fail-closed account of what remains, but TD11-CLASH is **not sound at its stated tier** until the clean-resonance hole in B9d is repaired (or expressly removed from the tier) and the scope contradictions are reconciled.
