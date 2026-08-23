**VERDICT: YES — all 67 nested rows are DEAD-AT-TIER; the outer-merge gap of last round is closed. SOUND-WITH-ERRATA on the writeup (the sign lemma is false as stated; I1 is a tautology; the free-ν_A “exactly two” list is an undercount).**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: the round-9 OUTER-MERGE repair of the 24 rows reopened in `xmodel/grok-td11-block2-review.md` (21 `(B,B)` windowed-out + 3 BB2 `M=1` hidden alternatives). Documents: `TOWER-TD11.md` §§16–17 as revised; `NF-M.md` §5 round-9 addendum; `cases/nfm_check.py` blocks H3b + I.
Honest question: are all 67 nested rows now DEAD at tier with no gap of the kind found last round (outer merge unanalyzed; sibling-schema disjunction)?
Method: line-read of the round-9 claim against `(2.8)–(2.11)` at `sol-normalform.md:316-365`, Lemma CAP-DEN at `TOWER-TD11.md:241-254`, the 145-row expander in `cases/tower_td11.py`, and the filed 11-C packet `L3a1b1n2 + 2 L4a1b2n3`. Independent exact `Fraction` replay of the A-nonzero pin, of `μ_in=1 ⇒ w_in=2`, of the both-nonzero menu **without** the A=Q restriction, of the `g | 4` family refusal out to `ν=399`, of the `μ_in=1` equal-handshake menu, of the inner-zero closed form, of the A-zero menu at census `ν_A=2` and the free-`ν_A` superset, and of the named pair `(3,5)@5/2`, `(5,7)@7/2`. The 67-row / 24-row decorations were re-expanded from the 145-layer, not taken from `ROWS67`. Gate: `python3 cases/nfm_check.py` exit 0, **23/23**. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: erratum — the both-nonzero sign lemma is false. I1 is a tautology (`or True`). A≠Q schemas exist. All of them sit at or below `1/2` and die by the completed-object clash the repair already invokes.

- File: `NF-M.md:206-208`; `cases/nfm_check.py:696-703,610-618`
- Claim: with `X = κ̄ − 2` and `ε = 0`, (2.9) forces `A = Q` exactly (`A > Q` gives `ν < 1`; `A < Q` flips the sign), so the family `κ̄ = 2νQ + 2`, `Q = μ_in + 1`, is the complete both-nonzero pinned menu.
- How checked.

  I1’s predicate is

  ```
  all((k_*(mu_in+2) - (k_-2)*(mu_in+2)) > (k_-2)/2 or True
      for mu_in in (1,2,4) for k_ in range(3,30))
  and all(Fr(2*nu*Q+2, 1).denominator == 1 ...)
  ```

  `or True` makes the first conjunct identically true. The second says an integer written over `1` has denominator `1`. This is the same non-gate class as the round-8 B2/H4/DG5, except this time the sentence it is supposed to underwrite is **false**.

  Exact closed form from (2.9) + `X = κ̄ − 2`, `ε = 0`:

  ```
  κ̄ = 2(1 + νQ) / [1 − ν(A − Q)],     denominator > 0  ⇒  A ≤ Q.
  ```

  `A > Q` does give `ν < 1` (that half is right). `A < Q` does **not** flip the sign whenever `κ̄ < 2Q/(Q−A)`. Because the A-edge has `μ = 1`, NE is forbidden (`m_j < min μ = 1`), so `A = μ_in + 1` and `Q = 2 + x`. Scanning the closed form over `μ_in ∈ {1,2,4}`, `x ≤ 16`, `ν ≤ 80` produces seven A≠Q schemas, all legal under R2.2 + MP6:

  | `μ_in` | `x` | `ν` | `(A,Q)` | `κ̄` | `(d_p,d_q)` | `M` | gap at `i=2` |
  |---:|---:|---:|---|---:|---|---:|---|
  | 1 | 1 | 3 | (2,3) | 5 | (6,10) | 2 | `5/12` |
  | 2 | 2 | 2 | (3,4) | 6 | (6,9) | 3 | `1/2` |
  | 2 | 2 | 5 | (3,4) | 7 | (15,21) | 3 | `7/30` |
  | 4 | 4 | 4 | (5,6) | 10 | (20,25) | 5 | `1/4` |
  | 4 | 4 | 9 | (5,6) | 11 | (45,55) | 5 | `11/90` |
  | 4 | 5 | 2 | (5,7) | 6 | (10,15) | 5 | `3/10` |
  | 4 | 6 | 3 | (5,8) | 5 | (15,25) | 5 | `1/6` |

  As `x` grows, `gap → 1/(Aν) ≤ 1/4`. No further A≠Q object enters the window. The `(6,9)` at gap exactly `1/2` sits strictly below every 11-C `gap(X) > 1/2` and falls to the completed-object clash, as I2 already says for that pair.

  So: the family `κ̄ = 2νQ + 2` is **not** the complete both-nonzero menu. It is the `A = Q` slice. The missing slice is entirely `≤ 1/2` and dies by a clause the repair already uses. This is not last round’s gap (an unanalyzed live arrival). It is a false lemma whose surviving objects are already covered.

- Suggestion: drop “forces `A = Q` exactly”. Write the closed form, record the seven A≠Q schemas as below-window, and replace I1 with a gate that actually enumerates `A ≠ Q` (the closed form is three lines).

### 2. Severity: erratum — “exactly two” above-window free-`ν_A` candidates is an undercount. I2b is cited and does not exist. The two named objects are real and census-unrealizable; so are the extras.

- File: `NF-M.md:218-221`; `cases/nfm_check.py:638-640,715-724`
- Claim: the free-`ν_A` superset names exactly two above-window candidates, `κ̄=30,(3,5)` at `5/2` and `κ̄=35,(5,7)` at `7/2`, both needing `ν_A ∈ {5,6}`.
- How checked.

  The two named objects exist and the arithmetic is exact.

  | object | `X/κ̄ = d_p/d_q` | pin | `i` used | gap | `ν_A` |
  |---|---|---|---:|---|---:|
  | `κ̄=30,(3,5)` | `(30 − 2ν_A)/30 = 3/5` | `ν_A = 6` | 4 (`μ_in=1` A-zero floor) | `30/(4·3) = 5/2` | **6** |
  | `κ̄=35,(5,7)` | `(35 − 2ν_A)/35 = 5/7` | `ν_A = 5` | 2 (`μ_in=2` A-zero floor) | `35/(2·5) = 7/2` | **5** |

  At the census value `ν_A = 2` the same degree pairs drop **into** the window and refuse: `(3,5)` becomes `κ̄=10` at gap `5/6`; `(5,7)` becomes `κ̄=14` at gap `7/5`. Both `refused_gap` at `k | 2`.

  They are not the only above-window free-`ν_A` schemas at the document’s own `i_min`. Independent A-zero scan (`ν_A ≤ 20`, `κ̄ ≤ 80`, same NE/`x` bounds) produces many more with `gap ≥ 5/2` at conservative `i`, among them `ν_A=4` `κ̄=28,(5,7)` at `14/5`, `ν_A=6` `κ̄=42,(5,7)` at `21/5`, `ν_A=12` `κ̄=40,(4,10)` at `5/2`. There is also one free-`ν_A` **in-window live** object, `ν_A=15`, `κ̄=48,(6,16)`, gap `2` (because `r = α + 1` has `den | 2` on the cap lattice). Every one of these needs `ν_A ≠ 2`.

  `outer_schemas` hard-codes `for nu_A in (2,)`. The comment “the free-`ν_A` superset is scanned in I2b” points at a gate that was never written. I2’s `above == []` is true only of the census-pinned slice, which is the slice that kills the 24 rows.

- Suggestion: either write I2b as a real free-`ν_A` enumerator and list every above-window / in-window-live object with its `ν_A`, or replace “exactly two” by “in particular the two border objects `(3,5)@5/2` and `(5,7)@7/2`”. Do not claim a complete named-object census that the gate does not compute.

### 3. Severity: residual — `P_inner ≥ 4` is the A-zero `i_min` floor and is not proved. The dangerous direction is a smaller `i`.

- File: `cases/nfm_check.py:593-594,668`
- A-zero uses `i ≥ max(2, ⌈4/μ_in⌉)`, the 4 being the B-seed `P = 4`. Smaller `i` makes a larger gap. At `i = 1` the census-pinned `(3,5)` (`ν_A=2`, `μ_in=1`, `κ̄=10`) would sit at `10/3 > 5/2` and leave the clash window.
- That `i = 1` would require `P_inner / μ_in = 1`, hence `P_inner = 1` on a merge of two `P = 4` B-poles. Every inner BB schema has local `d_p ≥ 9` (cylinder `4ν+1`, discrete `10` or `11`). No P-shrink mechanism is on the page. Not a demonstrated escape; the floor is the one place an above-window census-pinned object could be smuggled in if the emission `P` were smaller than the seed.

### 4. Severity: residual — H3 still prints the pre-repair stamps. H3b and I4 are the honest layer.

- File: `cases/nfm_check.py:558-567`
- H3 still demands `21 DEAD-WINDOWED` and `15 DEAD-SELFREF` and still says “CAP-DEN-refused” in the check string. That is the round-8 classifier last review rejected. H3b restates the 43/24 split; I4 restamps the 24. A reader who stops at H3 sees the old death certificates. `TOWER-TD11.md:323-336` (§7.6) still writes “the 129 nested rows are OPEN” against §17’s CLOSED-AT-TIER. Stale, not load-bearing once I4 is the cited stamp.

### 5. Severity: clear — (i) any A-nonzero orientation pins `X_out = κ̄ − 2` parametrically, independent of `w_in`. This is the load-bearing new step and it holds.

- File: `NF-M.md:203-206`; (2.8) at `sol-normalform.md:316-321`; A-packet `[1@2;2]`
- Nonzero handshake: `X = μ_e(κ̄ − w_e)`. The A-edge is `μ = 1`, `w = 2`, so `X_out = κ̄_out − 2`. The inner emission `w_in` does not appear. The *values* `(κ̄, X)` may still depend on `w_in` through the second affine row; (2.9) consumes only the **ratio** `X/κ̄ = (κ̄−2)/κ̄`, so every subsequent discrete/family constraint is parametric in `w_in`. If `μ_in ≠ 1` the second row has a different slope and pins a specific `κ̄ = (μ_in w_in − 2)/(μ_in − 1)`; that value is never needed, because every schema compatible with the ratio dies.
- This is exactly the step last review said was missing. It is now present and it is correct.

### 6. Severity: clear — (iii) `μ_in = 1` both-nonzero forces `w_in = 2` or contradiction, and the equal-handshake menu then dies.

- File: `NF-M.md:208-211`; `nfm_check.py:619-637`
- Two `μ = 1` rows: `X = κ̄ − 2` and `X = κ̄ − w_in`. Parallel, distinct unless `w_in = 2`. Contradiction if `w_in ≠ 2` (both-nonzero impossible). Equality if `w_in = 2` (unpinned; (2.10), not (2.9)).
- Equal-handshake menu, `ε = 0`, `A = 2`, `Q = 2 + x`:
  - `C = 0` (`x = 0`): cylinder `κ̄ = 4ν + 2`, `(2ν, 1+2ν)`, gap `1 + 1/(2ν) ∈ (1, 5/4]`. Algebraically refused: `r = a/c + 1/(2ν)`, lattice to `ν = 300` plus the same divisor argument as I3. Independently: `ν = 2..199`, zero escapes.
  - `C ≠ 0`: `E = 1 + νx` divides `aμA = 4`. One discrete schema, `ν=3,x=1`, `κ̄=5`, `(6,10)`, gap `5/12 < 1/2`. This is the “one discrete `(6,10)` below-window” of `NF-M.md:211`.
- For `μ_in = 1` the A=Q “pinned family” `κ̄ = 4ν+2` is the same cylinder (double-counted, both refused). No live `μ_in=1` both-nonzero object.

### 7. Severity: clear — (ii) the A=Q family `κ̄ = 2νQ + 2` refuses algebraically via `g | 4`. The `μ_in=1` cylinder likewise.

- File: `NF-M.md:206-208`; `nfm_check.py:726-745`
- `A = Q`, `ε = 0`: `d_p = νQ`, `i ≥ 2`, gap `= (2νQ+2)/(2·νQ) = 1 + 1/(νQ) ∈ (1, 5/4] ⊂ (1/2, 5/2)`.
- Death residue `r = α + 1/(νQ)` with `α = a/c`, `c | 2`. At `α = 1/2`: `r = (νQ+2)/(2νQ)`, and `gcd(νQ+2, 2νQ) = gcd(νQ+2, 4) | 4`. So `den = 2νQ/g` with `g | 4`. The would-be escape `den | 2` forces `νQ | g | 4`; together with `νQ ≥ 4` this is `νQ = 4` and `g = 4`. But `g = gcd(6,4) = 2 ≠ 4`. No escape. Lattice check `Q ∈ {2,3,5}`, `ν ≤ 399`, every residue of `{1,2}`: zero escapes. Cylinder `r = a/c + 1/(2ν)`: the same, zero escapes to `ν = 199`.
- I3 is a real gate (unlike I1). The algebraic claim is earned.

### 8. Severity: clear — (iv) the census pin is the filed entry packet, not a decoration of the 67 rows, and it does uniquely select the `ν_e=3` AB schema.

- File: `NF-M.md:211-212`; `BOOK-OFFAXIS.md:80-81`; `sol-td11-13-scope.md:294-296`; 145-layer in `tower_td11.py:533-589`
- 11-C is `L3a1b1n2 + 2 L4a1b2n3`. The letter dictionary is `(Λ, a, b, ν)`: `L3a1b1n2 = (3,1,1,2)` is the A-pole, `L4a1b2n3 = (4,1,2,3)` is each B-pole. BOOK-OFFAXIS’s td-7 type-`(2,3)` packet is the same pair, `(a,b,ν) = (1,1,2) ⊕ (1,2,3)`, `w_0 = (2, 3/2)`. So `ν_A = 2` and `ν_B = 3` are the filed pole characteristics.
- The 67-row layer stores `(μ, M, interior)` only. It does not carry `ν`. The pin cannot be “read off a row”; it is the leaf identity of those rows. Neutral padding on A before the outer merge would change `ν_e` (odd letters are legal at `w=2`); that is a current-state arrival, and the standing rider already excludes it. The `ν_A=15` live object of finding 2 is exactly such a current-state, not one of the 67.
- AB inner, B-zero: `κ̄ = 3ν_e − 2`, `X = 3ν_e − 4`. Census `ν_e = ν_B = 3` gives `κ̄=7`, `(5,7)`, `M=1`, gap `7/10` — the in-window schema the 12 AB rows already self-refuse. The sibling `ν_e=4` schema (`κ̄=10,(4,5)`, gap `5/4`) is not the B-pole. Uniquely selected, as claimed. Dead either way, as the prior review already granted.

### 9. Severity: clear — the 3 BB2 `M=1` rows are split and both branches die. The 24-row decorations match the expander.

- File: `NF-M.md:215-218`; `nfm_check.py:441-461,747-772`; expander `tower_td11.py:899-970`
- BB2 menu `M=1`: the cylinder family (in-window for every `ν ≥ 2`, H2-refused at `k | i_G = 2`) **and** two discrete schemas `(ν,ε,m_j,κ̄,d_p,d_q) = (2,1,(1,),7,11,7)` and `(3,2,(1,),7,11,7)`, both gap `7/(2·11) = 7/22 < 1/2`. Last review: stamping the *row* dead because the cylinder self-refuses is a disjunction error. The discrete alternatives are now sent through the outer merge.
- Those 3 rows have inner `M_G = 1`, so `μ_in | 1` forces `μ_in = 1`. I4’s `('BB2-M1-disc', 1, 1) × 3` matches. At `μ_in=1` the outer menu is the cylinder `κ̄=4ν+2` (refused) plus the discrete `(6,10)` (below-window) plus A-zero / inner-zero (finding 5–8). Both branches dead.
- Re-expansion of the 27 live `G(G(B1,B2),A)` rows:

  | inner `(μ, M_G)` | `n` | `μ_in` values | stamp |
  |---|---:|---|---|
  | `(1,1), 1` | 3 | `{1}` | UNREAL (no BB1 `M=1` schema) — already earned |
  | `(1,1), 2` | 6 | `{1,2}` ×3 | DEAD-OUTER |
  | `(2,2), 1` | 3 | `{1}` | SPLIT (cylinder self-refused / discrete outer-dead) |
  | `(2,2), 2` | 6 | `{1,2}` ×3 | DEAD-OUTER |
  | `(2,2), 4` | 9 | `{1,2,4}` ×3 | DEAD-OUTER |

  I4’s `ROWS24` is exactly the 6+6+9+3. No live BB decoration has a `μ_in` outside `{1,2,4}`.

### 10. Severity: clear — below-window outer schemas now have a genuine completed-object clash. CAP-DEN applies because X is a child of *this* merge.

- File: `NF-M.md:213-215`; `TOWER-TD11.md:241-254`; last review finding 7
- Last review: an inner vertex `< 1/2` is a live arrival at the unanalyzed outer merge; citing TD11-CLASH (direct hierarchies only) for `G(G(B1,B2),A)` was smuggling OB-8 back in.
- After the outer merge is actually run: if `gap(G_out) ≤ 1/2`, then `G_out` is not first. X is a leaf of `G_out` (the A-pole), `gap(X) ∈ (1/2, 2/3]`, so X dies first on the completed 3-pole. The X-family criterion (`ν | c²`, caps `{1,2}`, half-integral register) is the one that belongs to this vertex class. Additional live vertices only shrink the cap. The inner `(B,B)` chart does not touch the X-side register. This is the composition lemma last review said the round was written to supply.
- In-window `G_out` is a different vertex class and is killed by the general den-criterion at `k | 2` (I2/I3), not by Lemma CAP-DEN. The round-9 attribution (finding 8 of the last review) is kept. Independently: every census-pinned in-window outer schema refused; the A=Q family and the `μ_in=1` cylinder refuse algebraically.

---

## Replay of the four load-bearing claims

| # | claim | earned? |
|---|---|---|
| (i) | A-nonzero pins `X_out = κ̄ − 2` independently of `w_in` | **yes** (finding 5) |
| (ii) | both-nonzero forces `A = Q`, family `κ̄ = 2νQ+2`, refused via `g \| 4` | family + `g \| 4` **yes**; “forces `A = Q`” **no** (finding 1) |
| (iii) | `μ_in=1` forces `w_in=2` or contradiction | **yes** (finding 6) |
| (iv) | zero-slots census-pinned `ν_A=2` from `L3a1b1n2`, uniquely selecting `ν_e=3` AB | **yes**, against the filed packet, not the 67-row decorations (finding 8) |

Named objects `(3,5)@5/2` and `(5,7)@7/2`: genuinely census-unrealizable (`ν_A ∈ {5,6}`). Not the complete free-`ν_A` above-window set (finding 2).

---

## The 67

| stamp | n | last review | this review |
|---|---:|---|---|
| DEAD-UNREALIZABLE | 31 | earned (menus complete) | still earned |
| AB DEAD-SELF-REFUSED | 12 | earned (general den-criterion, `k \| i_G=2`, X alive) | still earned; `ν_e=3` is the B-pole |
| BB2 `M=1` SPLIT | 3 | **not earned** (cylinder refused; discrete `7/22` unanalyzed) | **earned** (finding 9) |
| DEAD-OUTER | 21 | **not earned** (outer merge unanalyzed) | **earned** (findings 5–8, 10) |
| LIVE / DEFERRED | 0 / 0 | 24 reopened | **0 / 0** |

`67 = 31 + 12 + 3 + 21`. The 43 that were already solid stay solid. The 24 that were not are now dead at `G_out`, parametrically in the unknown inner emission, with the discrete BB2 alternatives split off and killed by the same outer menu.

Riders unchanged and correctly scoped: `ν=1` modes (NF-P), post-merge P0 strata, current-state arrivals (the `ν_A=15` gap-`2` object lives there, not in the 67).

---

## What would reopen this

1. An A≠Q both-nonzero schema with gap `> 1/2` that the den-criterion does not refuse. The closed form says no.
2. A census-pinned (`ν_A=2`) A-zero or inner-zero schema that is in-window and not refused, or that reaches `≥ 5/2` at a legal `i`. None found at the stated `i_min`.
3. A proof that `P_inner` can be `1`. That would put census `(3,5)` above the pole top (finding 3).
4. Promoting a current-state A-arrival (`ν_e` odd, ≠ 2) into the 67 without re-running A-zero. The rider forbids the promotion.

None of these is exhibited. Last round’s gap — death certificates issued for an outer merge that had not been run, and a disjunction that hid two discrete schemas — is not present.

Machine gate: `nfm_check.py` 23/23, exit 0. I1 does not constrain the sign lemma; the independent enumerator does. No git commit.
