**VERDICT: SOUND-WITH-ERRATA — 159/159 TOWER-DEAD and the conditional emptiness claim hold inside the audited perimeter; the six named fail-closed classes are the right residual direction but are not a complete account of what the enumeration silently assumes (undeclared merge-schema finiteness), stamp “re-derives” are partly theatrical, and the td-7 regression is a shared CAP-DEN identity check rather than a full stamping-engine replay.**

Reviewer: Grok 4.5 (hostile referee). Date: 2026-08-14.
Targets: `cases/td11_census.py`; CONDITIONAL EMPTINESS certificate text emitted there and the matching CLOSED-AT-TIER / residual inventory in `TOWER-TD11.md` (status banner + §17; stale OPEN language still present elsewhere in that file).
Claim under review: every configuration of the audited td-11 class-B/C layer (159 instrument-backed rows quotienting a ~2e8 raw route space, each row covering its full chain/word/arrival extension class) is TOWER-DEAD, with emptiness CONDITIONAL on six named fail-closed classes (beyond-core, cap-free grammar, refile, current-state arrivals, post-merge strata, ν=1 provenance).
Method: ran `python3 cases/td11_census.py` (exit 0, **6/6**, 159 dead, 6 FC, 17/17 td-7) and `python3 cases/tower_td11.py` (exit 0, **66/66**). Independent recount of the decorated-skeleton layer; adversarial extension-class covering replay on 5 rows; independent re-derivation of 10 stamps across all five instruments; expansion of menu/outer search bounds; cross-read of `NF-M.md` §5, `TOWER-TD11.md` §§13/17, and the prior 67-row review chain. No other repo file modified. No git.

---

## Machine gates (this session)

| command | result |
|---|---|
| `python3 cases/td11_census.py` | exit 0; **6/6**; 159 rows; stamps 81/11/31/15/21; 6 FC named; 17/17 td-7 |
| `python3 cases/tower_td11.py` | exit 0; **66/66** |

Skeleton recount independent of the stamp path: 11-A 6 + 11-B 8 + 11-C (16+40+40+49)=145 → **159**. Stamp multiset matches C2 exactly. `RAW_ESTIMATE = 743·785·347 = 202 389 485 ≈ 2.0e8` matches the sizing banner (narrative floor, not a covering proof — see Finding 3).

---

## Findings (worst first)

### 1. Severity: residual (load-bearing) — the six fail-closed classes are incomplete as a completeness inventory; merge-schema enumeration bounds are a silent seventh assumption

- File: `cases/td11_census.py:181–277,458–476`; `NF-M.md:191–240,257–272`
- Claim: emptiness is conditional on exactly six named KEEP-AS-POSSIBLY-LIVE classes (FC1–FC6), and nothing the census assumes outside those classes is left undeclared.
- How checked.

  FC1–FC6 as written:

  | id | class | citation in census |
  |---|---|---|
  | FC1 | beyond-core charged strata (deg > 94; incl. NF-P-OB1) | TOWER-TD11 §13.0 |
  | FC2 | cap-free grammar slice (`k > 6` / `lex > 40`) | TOWER-TD11 §12(iii) |
  | FC3 | Q+E5/E5F refile layer | scope §1.1 UNKNOWN |
  | FC4 | current-state arrivals beyond entry-state decorations | TOWER-TD11 §10(b) |
  | FC5 | merged-chart post-merge P0 strata | NF-M riders |
  | FC6 | ν=1 case-I handshake provenance beyond enumerated menus | NF-P-OB2 |

  Those six match the standing residual inventory (beyond-core, cap-free, refile, current-state, post-merge, ν=1). They are the right *direction* for Rule 6. They are **not** a complete list of silent assumptions inside the dead-stamping path.

  **Undeclared seventh class — finite NF-M / outer schema search bounds.**

  | enumerator | hard bounds in census | what depends on completeness |
  |---|---|---|
  | `menu_AB` | `nu_e ∈ {3}` only; `A=1`, `eps=2`; `x ≤ 11` | 28 UNREALIZABLE AB `M=3` rows + 12 AB SELF-REFUSED |
  | `menu_BB` | `k ≤ 5`; `x ≤ 12`; `ν ≤ 120` | BB UNREAL / SELF / OUTER |
  | cylinder | `ν ≤ 99` | 3 BB2 split SELF-REFUSED |
  | `outer_all_dead` | `x ≤ 16`; `ν ≤ 80`; equal-menu `ν ≤ 200` | all 21 OUTER-DEAD + discrete alts on the 3 split rows |

  FC2 is about **pole-chain** px2 grammar (`k≤6`, `lex≤40`). It does **not** license finiteness of the **merge-schema** Diophantine searches. A live schema past those loops would flip UNREALIZABLE / SELF / OUTER without landing in any named FC.

  Stress (this review):

  - `menu_BB` modestly expanded (`k≤8`, `x≤20`, `ν≤200`): **0 extra** schemas at `μ∈{1,2}`.
  - `outer_all_dead` expanded (`x≤40`, `ν≤250`) and free-`A_` scan: **0 live** in-window unrefused hits for `μ_in∈{1,2,4}`.
  - Equal-menu cylinder refused for sampled `ν` past 200.
  - Freeing `menu_AB`’s `(A,eps)` **does** produce `MG=3` Diophantine solutions (e.g. `κ̄=7`, `(d_p,d_q)=(15,21)`). Those violate the banked AB handshake form (`A=1`, `eps=2`, census `ν_e=3` — `NF-M.md:252-255`). Under that normal form, AB `M=3` stays unrealizable. The census **hardcodes** the form; it does not re-derive why free `(A,eps)` is illegal.

  Related NF-M riders also not folded into FC1–FC6 as first-class census conditions:

  - A-zero index floor `P_inner ≥ 4` / smuggling path (`NF-M.md:235-240`);
  - NF-M-OB1 positive-dimensional components retained, not quotiented (`NF-M.md:266-269`);
  - symbolic/parametric scale parameters (`NF-M.md:261-265`).

  FC5 (“post-merge P0 strata”) is the closest bucket; it does not name schema-loop completeness or the `P_inner` floor.

- Gate theater: C4 only checks `len(FC)==6`. It does not test that the list is complete, that citations resolve, or that no dead stamp depends on an unnamed assumption.

- Effect on the claim: the **159-row death table** still stands relative to banked NF-M menus. The certificate’s “conditional on **six** named classes” **understates conditionality**. Anything the enumeration silently assumes and does not name is a seventh class it must declare — here, at minimum, **merge-schema enumeration finiteness / handshake normal-form completeness**.

---

### 2. Severity: residual — stamp “re-derives” are real for CAP-DEN / den-criterion / outer closed form, theatrical for SPINE and for CLASH menu maxima

- File: `cases/td11_census.py:152–177,282–314,401–416`
- Claim: “each [stamp] re-derives its killing arithmetic, then cites.”
- How checked — 10 stamps across all five instruments:

  | # | instrument | row (representative) | independent re-derive | verdict |
  |---:|---|---|---|---|
  | 1 | SPINE-DEAD-H8 | 11-A `(1,1)` `M=1` | entry `P/μ`: `2/1` vs `4/1` → `v_2`: 1≠2 | **arith OK; code theater** |
  | 2 | SPINE-DEAD-H8 | 11-B `(1,1)` `M=1` | `2/1` vs `6/1` → `v_3`: 0≠1 | **arith OK; code theater** |
  | 3 | SPINE-DEAD-H8 | 11-C nested inner AB `μ_B=1` | `inner_h8_dead`: kinds `[1,2]` with B-edge `μ=1` | **OK (predicate)** |
  | 4 | CLASH-DEAD | 11-A co-scaled | `7/16 < 1/2`; `capden_x_refusal({1,2,4}, odd ν)`; `lemma_11A_RES` | **CAP-DEN OK; menu max hardcoded; lemma thin** |
  | 5 | CLASH-DEAD | 11-C direct `(1,2,2)` | `2/5 < 1/2`; CAP-DEN on `{1,2}` | **OK as port of TD11-CLASH** |
  | 6 | UNREALIZABLE | AB `M=3` | `AB_MENU` MGs = `{1}` only | **OK under frozen AB form** |
  | 7 | UNREALIZABLE | BB1 `M=1` | `BB1_MENU` MGs = `{2}` only | **OK under `menu_BB(1)`** |
  | 8 | SELF-REFUSED | AB `M=1` | sole schema `κ̄=7,(5,7)`, gap `7/10`, `refused_gap` True | **OK (real den-criterion)** |
  | 9 | SELF-REFUSED | BB2 `M=1` split | cylinder `g=(6ν+3)/(2(4ν+1))` refused ν=2..99; discrete `(7,11)` below-window + `outer_all_dead(1)` | **OK; note slightly over-says “in-window” for the discrete** |
  | 10 | OUTER-DEAD | BB2 `M=4` | sole schema gap `1/10 ≤ 1/2`; `outer_all_dead(μ_in)` True | **OK** |

  **SPINE theater (rows 1–2).** `stamp_two_pole` computes

  ```text
  ok = (vL != vR + (0 if muB == M else 0))
  ```

  under the branch `muB < M`, so the ternary always adds 0, and **`ok` is never read** — the stamp is unconditional. The printed note `v_p: vL != vR` happens to match the correct entry-state `P/μ` comparison for these seeds. That is not “re-derived then cited”; it is a hardcoded dead stamp with a decorative boolean.

  **CLASH menu maxima are constants**, not menus: `opp_menu_max ∈ {7/16, 5/22, 2/5}` are frozen from the one-step tables. The live CAP-DEN scan is real (`refused_gap` over the full register lattice). The empty-prefix half is a citation of tower/scope menus, not a re-derivation inside the census.

  **`lemma_11A_RES` is a witness, not a proof.** It checks `gcd(l,5)=1` for `l|2`, that `8AB` is divisible by 8 on a six-point sample `(A,B)`, and that `2·3·5 ≢ 0 (mod 4)`. The real content — `v_2(8AB)≥3` for all prefixes because of the factor 8, and `v_2(2·Pi)=1` for odd stacks — is only sketched. Gate A4 in `tower_td11.py` is the actual load-bearing check; the census lemma is a pocket summary.

  **SELF / OUTER / CAP-DEN path is genuine.** `refused_gap`, cylinder sweep, and the both-nonzero closed form `κ̄ = 2(1+νQ)/(1−ν(A−Q))` are real arithmetic. Expanded outer bounds found no escape (Finding 1).

---

### 3. Severity: residual — the quotient covers the raw space only as an instrument-uniformity claim; five adversarial rows replay cleanly inside the perimeter, and that is where a census lies if it lies

- File: `cases/td11_census.py:1–19,93–146,282–386`; scope diagnostic `xmodel/sol-td11-13-scope.md:22-37`
- Claim: 159 instrument-backed rows quotient a ~2e8 raw route space; each row’s stamp covers its full chain/word/arrival extension class within the audited perimeter.
- How checked.

  **Layer identity.** Corrected `expand` (`μ_e | M_child` independent) reproduces the scope diagnostic on the nose: 6+8+145=159. Old-defect conflation is not used. Hierarchies are the full labelled set (1 binary + 4 ternary). This is the right skeleton for the printed-tier census.

  **What a row encodes / does not encode.**

  | in the row key | not in the row key |
  |---|---|
  | entry, hierarchy, root `μ`, `M_root`, interior, inner `(kinds,μ,M)` | concrete chain words, arrival vertices, `ν`, multi-word `Pi`, degree, `λ`, current-state `P` |

  Covering is therefore **not** by enumerating extensions. It is by arguing each instrument is constant on the extension class. That is the only honest reading of the sizing banner (`RAW_ESTIMATE` is a product of three different seeds’ chain counts — a floor narrative, not a bijection).

  **Five adversarial covering replays.**

  | adv | row | instrument | covers extension class? |
  |---|---|---|---|
  | 1 | 11-A co-scaled CLASH `(1,2), M=3, exterior` | CLASH-DEAD | **Yes inside perimeter.** Empty prefix + CAP-DEN + 11A-RES are route-shape-uniform provided no chain inserts a gap above `7/16` into `(g_X, 5/2)`. That proviso is exactly FC1+FC2+FC3. Current-state `μ` is FC4. |
  | 2 | 11-B SPINE `μ_B=1` | SPINE-DEAD-H8 | **Yes at entry-state.** Pure `v_3` mismatch on `P/μ`; independent of chain words. Current-state `P` changes are FC4. |
  | 3 | 11-C nested BB2 `M=1` SELF-REFUSED | SELF-REFUSED + outer on discretes | **Yes on realizing schemas.** Kill is on `(κ̄,d_p,d_q)` / cylinder family, not the pre-merge word. Completeness of `menu_BB(2)` is the silent hypothesis (Finding 1). |
  | 4 | 11-C nested AB `M=3` UNREALIZABLE | UNREALIZABLE | **Yes under AB handshake normal form** (`ν_e=3`, `A=1`, `eps=2`). Not by free Diophantine search (Finding 1). |
  | 5 | 11-C nested BB2 `M=4` OUTER-DEAD | OUTER-DEAD | **Yes.** Inner schemas windowed out; outer parametric in `w_in` (round-9 load-bearing step). Expanded bounds still empty. |

  **Where a census would lie.** The lie surface is not the 159 count. It is (a) a non-uniform instrument (stamp depends on a chain feature not quotiented into the row), or (b) an incomplete menu that misses a realizing schema. (a) is handled for SPINE/CLASH by FC1–FC4. (b) is the undeclared class in Finding 1. Within the banked instruments and the six named FCs plus schema-finiteness, the five adversarial rows do **not** expose a covering hole.

  Interior flag: many keys appear as `(interior=True/False)` pairs with the **same** stamp when the instrument ignores interior; when decorations differ (different inner records sharing a printed root key fragment), stamps differ for real reasons (H8 vs AB menu). No interior-only escape found.

---

### 4. Severity: residual — conditionality wording is mostly honest; the certificate still overclaims in three places

- File: `cases/td11_census.py:478–490`; `TOWER-TD11.md:1-41,524-537,671-693`; `cases/tower_td11.py` SK3 / block 15
- Claim: CONDITIONAL EMPTINESS over the audited class; six FC remain KEEP-AS-POSSIBLY-LIVE; not an unconditional empty-panel certificate.

  **What is honest.**

  - The census certificate text explicitly refuses unconditional emptiness.
  - ZERO live / ZERO deferred on the 159-row table is true as a stamp fact (C3).
  - Residual work named (beyond-core, cap-free, refile) matches the campaign.
  - §17 CLOSED-AT-TIER for the 129 nested rows (62 H8 + 67 NF-M) matches the census multiset (nested contribution to 81/11/31/15/21).

  **Overclaims / integrity breaks.**

  1. **“Full synchronized chain/word/arrival extensions”** reads like extensions were enumerated. They were not. The true claim is instrument-uniformity on extension classes under the exact-core discipline (Finding 3). Wording should say that.

  2. **“Conditional on six named classes”** is false as a completeness statement (Finding 1). At least schema-enumeration finiteness must be named, or folded into an explicit FC.

  3. **Document / gate lag vs the certificate.**

     | locus | still says | census / §17 says |
     |---|---|---|
     | `TOWER-TD11.md` lines 10–11, 26–28 | nested OPEN; NF-P slice OPEN | nested CLOSED-AT-TIER; NF-P STAMPED (§17) |
     | §13 perimeter (i) | 129 nested OPEN, never certified | census stamps all 129 dead-at-tier |
     | `tower_td11.py` SK3 | nested stamped OPEN, **never** TOWER-DEAD | census stamps them with named instruments |
     | formal “CONDITIONAL EMPTINESS CERTIFICATE” block | **only** in `td11_census.py` printout | not a dedicated TOWER-TD11 section |

  The gate that still forbids nested TOWER-DEAD (SK3) and the compiler that stamps them dead are both green (66/66 and 6/6). That is a **campaign-integrity** defect: two exit-0 artifacts disagree on the nested tier. A reader of TOWER-TD11’s front matter alone would not know the census certificate exists.

  C5 is also thin: it checks `len(ROWS)==159` and no stamp string `'LIVE'`. It does not check that FC classes are excluded from the certified class, nor that every stamp’s instrument is the one claimed in C2’s breakdown beyond the Counter equality.

---

### 5. Severity: residual — td-7 regression is genuine arithmetic on the promoted 17-cell book, not a stub, and not “the same stamping engine”

- File: `cases/td11_census.py:32–34,389–416,492–505`
- Claim: “the promoted 17-cell book is replayed through the **same stamping engine** (kbar/X/N1/P3 identities + the A/B/C CAP-DEN refusal at cap `k|2`) and must come out 17/17 TOWER-DEAD.”
- How checked.

  - `TD7_CELLS` matches the promoted Q+E5 book of 17 cells exactly (cross-check against the filed list from the E5 census review).
  - For every cell: `κ̄ = 2 d_q/(d_q−d_p)` integral; `X = κ̄−2`; `N1 = gcd(κ̄, ν_G)`; `P3 = (d_q−1) ≡ 0 (mod ν_G)`; first cell `(9,15)` gives `κ̄=5`, `X=3` as asserted.
  - Kill predicate: `capden_x_refusal((1,2), odd ν≥3)` and `2/5 < 1/2` — the **same** `capden_x_refusal` / window constants used on 11-C CLASH rows.
  - All 17 return TOWER-DEAD.

  **What “same engine” is not.**

  | shared with td-11 path | not shared |
  |---|---|
  | `capden_x_refusal`, `refused_gap` | skeleton expand, `μ`-decoration, H8 `v_p`, menus, outer-merge, UNREAL/SELF/OUTER |
  | hardcoded 17 tuples | any pricing / E5 / route enumeration |
  | global kill (identical `okA∧okW` for every cell) | cell-specific death analysis |

  `μ_0`, `M_G`, and `P3` are computed (or carried) but **do not enter the kill**. The regression proves: (i) the 17-book identities still type-check, (ii) the shared CAP-DEN primitive still fires on caps `{1,2}`. It does **not** prove the decorated-skeleton stamping path is sound by replaying td-7 configurations through it. Docstring overclaim; implementation is a real identity+CAP-DEN check, not a stub and not a full engine regression.

---

## Attack checklist (requested)

| # | attack | result |
|---:|---|---|
| 1 | Quotient / extension-class covering (5 adversarial rows) | **Holds inside perimeter** for all five; covering is instrument-uniformity, not extension enumeration; lie surface = incomplete menus (→ Finding 1) or non-uniform instruments (carved to FC1–FC4 for SPINE/CLASH) |
| 2 | Stamps re-derive arithmetic (10 across 5 types) | **CAP-DEN / SELF / OUTER genuine**; SPINE boolean dead; CLASH menu maxima hardcoded; `lemma_11A_RES` thin |
| 3 | Six fail-closed classes complete? | **No** — merge-schema enumeration finiteness (and several NF-M riders) are silent; FC1–FC6 are the right residual *direction* |
| 4 | Conditionality wording overclaim? | **Yes, three places**: “full extensions” wording; “exactly six” completeness; TOWER-TD11 / SK3 lag vs census |
| 5 | td-7 regression genuine (same engine, not stub)? | **Genuine identities + shared CAP-DEN; not the full stamping engine; not a stub** |

---

## Bottom line

The census compiler does what a quotienting emptiness compiler should do at this campaign stage: freeze the corrected 159-row decorated-skeleton layer, stamp every row with a named banked instrument, refuse unconditional emptiness, and keep six residual classes open under Rule 6. Gates green: **159/159 dead, 6/6 census checks, 66/66 tower checks**. The five adversarial covering replays do not produce a live extension inside the audited perimeter.

What keeps this from a clean SOUND:

1. **Declare the seventh class** (or prove it): finite merge-schema / outer-menu bounds and the AB handshake normal form are load-bearing and currently silent.
2. **Make re-derives real**: read the SPINE `ok`; derive or gate-import menu maxima; replace pocket `lemma_11A_RES` with the tower A4 content or a real `v_2` sweep.
3. **Reconcile artifacts**: SK3 / §13 perimeter (i) / front-matter OPEN residue must not contradict the census certificate and §17 CLOSED-AT-TIER; put the CONDITIONAL EMPTINESS block in `TOWER-TD11.md` or stop claiming it lives there.
4. **Downgrade the td-7 blurb** to “shared CAP-DEN + book identities,” or actually run the 17 cells through a skeleton-shaped path.

Until (1) and (3) are fixed, the right public sentence is:

> Every one of the 159 audited decorated skeletons is TOWER-DEAD by a named instrument, **conditional on** the six named fail-closed classes **and** on the completeness of the banked NF-M / outer schema enumerations (finite bounds + AB handshake form) that the census ports but does not re-prove.

That is earned. “Conditional on six named classes” alone is not.
