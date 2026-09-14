# Broad external JC2 sweep — 2026-09-06T09:12Z (renewal of 2026-09-03T10:10Z)

Status: **PARTIAL.** No external characteristic-zero plane-JC resolution,
proof, or counterexample. Renewed in full on arXiv, watched repositories,
broad GitHub, Zenodo, Palomar, MathOverflow/MathSE, Mathstodon and
Wikipedia. **X/Twitter, Bluesky and Zulip `#Palomar` were NOT covered**
(access failures below); their clocks are not reset. Undated broad discovery
surfaced two previously unlisted primaries, both bounded and neither a plane
result, and one watched actor withdrew and re-proved an internal HC4 step.

## Search boundary

Window: `2026-09-03T10:17Z` → `2026-09-06T09:23Z` (~71 h). Previous charged
sweep: frozen `websweep-20260903T1010Z-grok46.md`, SHA-256
`fab2edcfc3f81b10a3001fbed85db4fd8b262baedb460a1e6410341b5acc7a81`; the
manifest of all three charged inputs was verified mechanically before use.
Undated broad-discovery probes were **not** window-limited and are marked so.
Snippets located pages; every claim is quoted from an opened primary, and
examined-at timestamps are fetch UTC. All 57 fetched artifacts are hashed in
`box/websweep-20260906T0912Z/{source-index.tsv,receipts-sha256.txt}`, with
compact extracts under `extracts/`.

## 1. arXiv — structurally complete negative

Date-ordered API at `2026-09-06T09:14:45Z`: `all:"Jacobian conjecture"`
**total 219, unchanged**. Re-sorted by `lastUpdatedDate` at `09:14:58Z`,
the newest update of any of the 219 is Liu
[2608.19112v2](https://arxiv.org/abs/2608.19112v2) at
`2026-09-02T02:45:38Z`, **before** the window; the newest *submission*
remains van Dobben de Bruyn
[2608.27341v1](https://arxiv.org/abs/2608.27341) (`2026-08-27T16:41:51Z`).
**Zero in-window new submissions and zero in-window revisions.**

Phrase totals at `09:15:11Z`, with the newest update in each: `"plane
Jacobian conjecture"` **10** (2204.14178, 2022); `"Keller map"` **25**
(2608.12543v2, `08-31`); `"Jacobian pair"` **9** (`08-12`);
`"Abhyankar-Moh"` **19** (`07-17`); `"Hessian conjecture"` **4**;
`"polynomial automorphism"` **161**; `"Jacobian conjecture dimension two"`
and `"Moh Jacobian"` **0**. **Every newest is `≤ 2026-09-02`.**

**The apparent index gap is the arXiv announcement schedule, not a fetch
failure.** `arxiv.org/list/math.AG/new` at `09:15:29Z` reads "Showing new
listings for **Friday, 4 September 2026**", 46 entries; the API index stops
consistently at `2026-09-03T17:32Z`/`17:54Z` across math.AG/AC/CV. arXiv
announces Sun–Thu, the last deadline was Thu `09-03` 18:00Z, and today is
Sunday `09-06` 09:23Z, before the Sunday 20:00 ET announcement. The interval
Thu 18:00Z → now therefore holds **zero announced arXiv papers by
construction**; anything submitted in it appears Monday `09-07` and is the
first item the next sweep must claim.

Friday 4 September listings, full keyword scan (`09:15:29Z`): math.AG 46
entries, math.AC 19, math.CV 26; 6 keyword hits, **all non-JC**. Fifteen
watched authors probed at `09:21:58Z`–`09:22:15Z` (Orevkov, Valqui,
Guccione, Pissolato, Shaska, Migus, Jelonek, Xavier, Gao, Meng, Charbonnel,
Kowalczyk, van Dobben de Bruyn, Horruitiner, van den Essen): **no in-window
JC record for any**; newest relevant are Shaska 2609.00672 (`09-01`) and
Migus 2607.21572v3 (`08-27`).

## 2. Undated broad discovery — two primaries the last sweep missed

Both predate the window and came from unrestricted phrase/registry search,
not from watching a known actor.

### 2a. arXiv:2608.14217v1 — a claimed proof of the *quartic* HC4

Opened abs `2026-09-06T09:22:57Z` / `09:23:13Z`. Zixiang Ni, *The Quartic
Hessian Conjecture in Dimension Four*,
[arXiv:2608.14217v1](https://arxiv.org/abs/2608.14217), **v1 only**,
submitted `2026-08-14T11:48:06Z`, 10 KB, math.AG + cs.AR.
Quote: "It is known in dimensions at most three, false in dimensions at
least five, and open in dimension four. **We prove its four-variable
quartic case.**" Per the abstract, three exhaustive cone types reduce to
`f = P(x1,x2,x3) + x4·Q(x1,x2,x3) + a·x4²`, `deg Q ≤ 2`; `a ≠ 0` descends
from three-dimensional HC by a Schur complement, `a = 0` by an
isotropic-cone rank analysis. **The abstract does not mention the Jacobian
conjecture** (zero occurrences on the abs page).

Scope: the **quartic case only**, not HC4, so it does not deliver the
`HC4 ⇒ JC2` antecedent even if correct. I read the abstract only; **I did
not open or check the PDF**, and a 10 KB v1 with no journal and an anomalous
cs.AR cross-list is unverified.

Concrete finding: **neither public HC4 actor cites it.** `grep
'2608.14217'` returns 0 in Roy's `STATUS.md`/`README.md` (`09:23:34Z`) and 0
in ipitchford's `README.md`, whose first-unproved list still names "the
quartic Hessian conjecture in dimension four" as its target (line 18).

### 2b. Zenodo 10.5281/zenodo.22168498 — a planar necessary condition

Opened record `2026-09-06T09:19:29Z`. Casey Atwell, *A Relative
Jacobian-Rank Filtration for Keller Maps*,
[doi:10.5281/zenodo.22168498](https://doi.org/10.5281/zenodo.22168498),
created `2026-08-30T03:53:22Z` — one day before the previous window opened,
so a genuine gap rather than a new delta. Quote: "We introduce the
relative Jacobian rank `rho_rel(F)`, the minimum over complex basepoints of
the generic rank of `JF(x)−JF(a)`. For complex Keller maps we prove that
`rho_rel(F) ≤ 1` implies polynomial automorphy. Consequently **every
hypothetical nonautomorphic planar Keller map has `rho_rel = 2`**. … The
paper does not claim `rho_rel(F) ≤ 2` implies automorphism."

Assessment, not the deposit's framing: in the plane `JF` is `2×2`, so
`rho_rel ∈ {0,1,2}` always and `rho_rel = 0` is the affine case. The planar
corollary therefore excludes only the rank-`≤1` stratum, and its conclusion
is the generic and only remaining value — a correctly scoped bounded result,
**weak as a planar filter**. Abstract read from the record; **full text not
opened**.

## 3. Watched repositories

Heads compared at `2026-09-06T09:16:43Z` (GitHub REST).

**Seven of the eight heads are byte-identical to the previous sweep** — no
new commit on SuperMindAI `8b376296bb8f` (`08-05`), wstrinz/72-108
`d5fb30e7` (`08-23`), wstrinz/75-125 `16ae8b263cb8` (`08-30`),
collision-geometry `0f1f2c8c` (`08-25`; its `updated_at
2026-09-03T16:57:01Z` is metadata, not a push), ipitchford `530dc13e`
(`08-31`), AEjonanonymous `e4eee150` (`08-28`), SNAPKITTYWEST `319c0e1f`
(`08-15`). The single mover is **royvanrijn/jacobian-research**,
`fb056eaa153f` → `7471645748ae07b8d942f6957e314378ca8aed1f`
(`2026-09-05T20:23:34Z`), 42 commits / 300 files ahead, type
`ACTIONABLE_HC4_ONLY`.

**Strinz.** Both mains frozen; branches enumerated `09:20:42Z`:
`codex/palomar72-composed` still `3c2ac84866179f77ae8114fe0293800b6eca77da`,
and a second branch `codex/palomar-f37` exists but points at main's
`d5fb30e7`, i.e. **no new content**. `q18` and the missing
source-to-reduced adapter remain the first unproved arrows; **no new public
exact artifacts**. `NO_ACTIONABLE_DELTA`.

**Roy van Rijn — a withdrawn inference, then a claimed repair.** Compare
`fb056eaa…7471645748` (`09:16:5xZ`): 42 commits, 234 added / 62 modified /
4 renamed. The commit stream is K3, elliptic-curve rank and prime-gap work;
**zero new `plane-jc/` paths**. But two **new** HC4 files were added
(237 lines each), opened `09:17:22Z`:

- `HC4_MOTION_FRAME_TRANSPORT_AUDIT.md`. Quote: "The final regular Jordan
  block in the HC4 master reduction **was closed using an unjustified
  differential equation.** … The normalized motion determinant is `pq/a²`,
  not `pq`. Consequently the claimed deduction `d(pq)=0` in the
  affine-plane bridge, §4 **does not follow**." The audit "temporarily made
  … **HC4MR1** and the equivalence **HC4MR2** partial"; "the original
  constant-motion inference remains withdrawn". Its further claim that
  "`PHC4 ⇒ JC2` is not affected by this gap" is the repo's own assertion,
  unverified here.
- `HC4_NEGATIVE_MOTION_POLYNOMIAL_OBSTRUCTION.md`, Theorem **HC4MRA2**,
  excluding the surviving `p=q=−a≠0` branch by global polynomiality of
  `N=S⁻¹T`. Explicit scope: "**It does not prove unrestricted HC4 or
  JC2.** … no independent end-to-end or complete formal verification is
  claimed."

`STATUS.md` (1.7 MB, 1345 rows): 24 occurrences of "prove JC(2)", **all
inside negative scope clauses**, and a regex for
`(establishes|proves|resolves|settles|closes) … JC(2)` returns **zero**
matches. `NO_ACTIONABLE_DELTA` for JC2; `ACTIONABLE` at HC4 scope only.

## 4. Broad GitHub discovery — search beyond the watchlist

Repository search `q=jacobian conjecture&sort=updated` at `09:18:24Z`:
**61 repos**, only two pushed in-window — `dcposch/jc2-lean`
(`2026-09-05T09:28:23Z`, the campaign's own repo, **excluded by lane scope,
not inspected**) and one external:

**`fsantibanezleal/CAOS_RESEARCH`** (new actor, `09:18:43Z`), described as
an "Experiment-history repository … First program: the Jacobian conjecture
after the 2026 counterexample". Pushed `2026-09-05T13:54:22Z`, 3256 tree
entries including `manuscripts/jacobian-conjecture/`. **But** its six
in-window commits are Huneke–Wiegand torsion merges, the log for that path
shows the JC manuscripts untouched since **`2026-08-01T13:46:09Z`**, its own
`data/derived/research/jacobian.json` records `"now": "false for N >= 3;
**N = 2 open**"`, and its in-window Zenodo deposit
[22342976](https://doi.org/10.5281/zenodo.22342976) is that Huneke–Wiegand
paper, **not JC**. `NO_ACTIONABLE_DELTA`; watchlisted.

Repos created since `2026-08-25` matching JC: **total 1**, Arthur742Ramos
(`08-27`, already known, a Lean formalization of the *three*-dimensional
counterexample). **No new claimant appeared in the window.**

## 5. Zenodo, Palomar, MathOverflow, Mathstodon, Wikipedia

**Zenodo** (`09:19:09Z`): `"Jacobian conjecture"` total **125** (was 123);
**one in-window deposit, 22342976, not JC**; the only other newer record is
22216400 (ipitchford, `08-31`, the standing ACTIONABLE). The secondary
query `"plane Jacobian" OR "Keller map"` (total **39**) surfaced 22168498
(§2b) plus out-of-scope 22111578 and 22040381 (**WITHDRAWN**).

**Palomar** (`09:19:xxZ`): `recent.json` schema v2, **188** entries (was
170), **20** in-window, newest `PALOMAR-2026-09-06-000002`
(`2026-09-06T05:02:14Z`, Nikodym). Its sole in-window keyword hit,
`PALOMAR-2026-09-04-000001` "Even-order **Grünschloß–Keller** permutation
nets", is a quasi-Monte-Carlo net, **not a Keller map**; no `14R15`, no
plane-exclusion title. The four campaign entries are still `registered`, and
PalomarArchive (100 repos, `09:21:11Z`) holds exactly **3** JC-named forks,
**all pre-window**.

**MathOverflow / MathSE** (`09:19:55Z`–`09:20:08Z`): advanced search
`fromdate=1788430620` returns `items: []` on **both** sites. Watched thread
[MO 513413](https://mathoverflow.net/questions/513413): score 49, **views
8831 → 8869**, 4 answers, `last_activity` still `2026-08-19T07:37:34Z`.

**Watchlist change — `ratto3423` (user 595783) is active again.**
`last_access_date` moved from `2026-08-23T07:06:39Z` (frozen across the two
previous sweeps) to **`2026-09-05T13:09:41Z`**. Their post list still holds
**exactly one** item, a/513493, `last_edit 2026-07-23T08:44:31Z`, score 14,
ending "Write-up in preparation"; it claims `max(deg P, deg Q) ≥ 125` with
everything below 125 reduced to `(72,108)`. **Browsing resumed; the
artifact is still ABSENT.**

**Mathstodon** (`09:20:25Z`): `#jacobianconjecture` newest still
`2026-08-16T09:31:14Z` — **no in-window post**; `#jacobian` `08-07`;
`#keller` `08-30`. `#leanprover`: 7 in-window posts, **none JC**. Tao
(`109378244433513115`): 19 in-window statuses (AI-and-research, a
Navier–Stokes rumor clarification, bounded-gaps timeline) — **no JC
mention**.

**Wikipedia** (`09:20:42Z`): last edited `2026-08-28T14:47:56Z` by IlkkaP
("remove duplicate reference to Borisov 2020"), **pre-window and
unchanged**; no change to the "two dimensions remains open" text.

## 6. Coordinator spot-checks — confirmed, not substituted for coverage

- **AEjonanonymous Lean file.** Fetched `09:22:32Z`, 4662 bytes, SHA-256
  prefix `1d63ecf607525069f7d2d0b15ad2a197`, head `e4eee1505c7f`
  (`2026-08-28`). Final theorem verbatim: `theorem
  jacobian_conjecture_2d_established … (hc : c ≠ 0) (h_jac :
  IsConstantJacobian P Q c) : coeff (0 : Fin 2 →₀ ℕ) (jacobian P Q) ≠ (0 :
  k)`. **Confirmed:** it concludes only that the Jacobian's constant
  coefficient is nonzero — a restatement of the hypothesis, with **no
  invertibility, surjectivity or bijectivity** in the statement.
- **arXiv:1605.09430.** Abs opened `09:22:57Z`; Guccione–Guccione–Valqui,
  lower side of the Newton polygon, submission history `[v1] Mon, 30 May
  2016 21:58:33 UTC`. **Confirmed** a 2016 preprint — a newer publication
  listing is not a new all-degree exclusion.

## 7. Proof or counterexample claims

**No in-window primary claims a characteristic-zero plane proof or
counterexample**, and no claimant repository was created in the window. The
standing `SNAPKITTYWEST/jacobian-formal` ("SOLVED via Jordan Algebras") head
is unchanged since `2026-08-15T20:35:17Z`; `UNSOUND_SCOPE` if revived.

### ACTIONABLE

1. **arXiv:2608.14217v1 (Ni) — quartic HC4 claimed proved, uncited by both
   HC4 actors.** Examined `2026-09-06T09:22:57Z`/`09:23:13Z`. Exact claim:
   the four-variable **quartic** case of the Hessian conjecture, under the
   4-d homogeneous Hesse theorem and the known 3-d HC; **not** HC4, **not**
   JC2, JC unmentioned.
   *Smallest decisive check:* read the `a=0` branch and confirm its
   rank-zero reduction really lands on two-dimensional HC without assuming
   HC4 — one desk read of a 10 KB PDF, no CAS.
   *Affected interface:* the **APPROACHES Hessian/HC4 row** and standing
   ACTIONABLE #1 (ipitchford), whose stated target this claims to settle;
   **orthogonal to integration #17** and to (99,66) / D108 / K16.
   *Follow-up:* record `2608.14217` on the HC4 row as a
   claimed-but-unverified antecedent; do **not** divert #17 slots.
   `ACTIONABLE_LITERATURE`.

2. **Zenodo 22168498 (Atwell) — `rho_rel = 2` necessary for a planar
   counterexample.** Examined `2026-09-06T09:19:29Z`. Hypotheses: complex
   Keller map, `rho_rel` = min over basepoints of the generic rank of
   `JF(x)−JF(a)`; claim used, `rho_rel ≤ 1 ⇒ polynomial automorphy`.
   *Smallest decisive check:* on one surviving configuration, decide whether
   `JF(x)−JF(a)` can have generic rank `≤1`. **Expected answer: vacuous** —
   in the plane the only alternatives are the affine case and rank 1, so the
   filter is very likely met by all 64 configurations. Do the cheap check,
   then close it. *Affected interface:* the necessary-configuration
   enumeration (24,063 → 90 → 64 at `n ≤ 200`), as a candidate extra
   necessary condition. `ACTIONABLE_LOW`; **do not launch a solve from it.**

3. **Roy `HC4MRA1`/`HC4MRA2` — a public HC4 inference withdrawn and
   re-proved.** Examined `2026-09-06T09:17:22Z`, head
   `7471645748ae07b8d942f6957e314378ca8aed1f`. Changes **actor status and
   artifacts**, not JC2 correctness. *Smallest decisive check:* grep campaign
   notes for any use of the `d(pq)=0` step or affine-plane bridge §4 and
   re-derive it — the repo now says that step **does not follow**.
   `ACTIONABLE_DEPENDENCY_CHECK`.

### NOT (one line each)

- arXiv 219-corpus: zero in-window submissions **and** zero revisions; 15
  watched authors probed, no in-window JC record for any.
- Zenodo 22342976 Huneke–Wiegand; 22111578 cube-tiling Keller; 22040381
  **WITHDRAWN**.
- CAOS_RESEARCH: JC manuscripts frozen since `08-01`, `N = 2 open`.
- Palomar 20 new entries: no `14R15`, its one "Keller" is a QMC net;
  PalomarArchive 3 JC-named forks, all pre-window.
- MO/MSE `items: []`; MO 513413 unchanged since `08-19`; ratto3423
  reactivated but **still one post, still no write-up**.
- Mathstodon JC tags / Tao: no in-window JC mathematics; Wikipedia last
  edited `2026-08-28`, pre-window.
- SuperMind / both Strinz mains / collision-geometry / ipitchford /
  AEjonanonymous / SNAPKITTYWEST: heads frozen.
- `dcposch/jc2-lean` pushed in-window: **campaign-owned, excluded by lane
  scope, not inspected.**

Absence of a hit is **weak evidence**, not evidence of absence; each
negative is bounded by the query and instant recorded beside it.

## Coverage limits — PARTIAL, do not reset these clocks

Concrete holes, verified rather than assumed:

1. **X/Twitter: NOT COVERED — regression.** `x.com/search?q="Jacobian
   conjecture"&f=live` (`09:20:56Z`) returned HTTP 200 / 293 KB containing
   **0 occurrences of "jacobian"** and 2 JS-shell markers; `nitter.net`
   served an 11.5 KB placeholder. The previous sweep read X content at
   `2026-09-03T10:14Z`; this one could not. **The watched `@octonion`
   account and all X traffic since `2026-09-03T10:17Z` are unexamined.**
2. **Bluesky: NOT COVERED.** `public.api.bsky.app` `searchPosts`
   (`09:21:28Z`) returned **HTTP 403 Forbidden**.
3. **Zulip `#Palomar`: NOT COVERED.** Not attempted this sweep; the
   previous one recorded `{"code":"UNAUTHORIZED"}`. Carried forward
   unresolved — the registry JSON remains the only Palomar substitute.
4. **GitHub code search** needs authentication; only repository-level
   search ran, so a JC result committed inside an unrelated repo is missed.
   arXiv `id_list` was intermittently rate-limited, worked around via
   `arxiv.org/abs/` HTML with no listing skipped.
5. **Nothing was executed or replayed**: not Ni's argument, not Atwell's
   theorem, not `HC4MRA2`, not ipitchford's certificates, not Roy's
   `MATH_STATUS.json`. Ni and Atwell were read at **abstract level only**,
   neither PDF opened — located claims, not verified ones.
6. Per lane scope: no jc2-lean inspection, no live lane reports, no shared
   ledger edits, no fleet; no posts, messages, issues, PRs, registrations or
   account connections. Read-only throughout.

## Overall status

At cutoff `2026-09-06T09:23Z`, characteristic-zero JC2 remains **externally
open** and the campaign baseline is untouched by everything found: 24,063 →
90 → 64 necessary configurations at `n ≤ 200`, 44 `u_s=1` and 20 split;
(99,66), D108 and uniform K16 still open. Nothing external bears on the
running full-ideal reverse gate, which is not a public result. The two new
primaries are bounded and non-planar in effect; the one repository delta is
an HC4 self-correction that explicitly disclaims both HC4 and JC2.

Next backstop `2026-09-07T09:23Z`; the **Monday `09-07` arXiv announcement
is the first mandatory item**, carrying every submission from Thu `09-03`
18:00Z onward. Sweep immediately on a public char-0 plane theorem,
counterexample, or a Strinz exact-artifact drop. **X, Bluesky and Zulip must
be re-attempted from `2026-09-03T10:17Z`, not from this cutoff.**

```text
typed:
  sweep_completeness=PARTIAL
  uncovered_channels=x-twitter|bluesky|zulip-palomar
  uncovered_since=2026-09-03T10:17Z
  plane_jc_status=EXTERNALLY_OPEN
  arxiv_in_window_new=0 ; arxiv_in_window_revisions=0
  arxiv_frontier=2026-09-03T18:00Z_announcement_schedule_not_a_hole
  actionable=3
  actionable_1=arxiv:2608.14217v1/ni-quartic-hc4 ; type=ACTIONABLE_LITERATURE ; scope=quartic-HC4_not_HC4_not_JC2
  actionable_2=zenodo:22168498/atwell-relative-jacobian-rank ; type=ACTIONABLE_LOW ; scope=planar-necessary-condition_likely-vacuous
  actionable_3=royvanrijn:7471645748ae/HC4MRA1-MRA2 ; type=ACTIONABLE_DEPENDENCY_CHECK ; scope=withdrawn-d(pq)=0-step
  dag=APPROACHES.Hessian-HC4 ; not integration-#17
  ipitchford_target_claimed_proved_uncited=true
  strinz_q18=OPEN ; strinz_source_to_reduced_adapter=OPEN
  roy_window=NO_ACTIONABLE_DELTA_for_JC2 ; roy_jc2_assertions=0
  supermind=STATIC ; collision_geometry=STATIC ; ipitchford=STATIC
  new_actors=fsantibanezleal/CAOS_RESEARCH|casey-atwell|zixiang-ni
  caos_research=NO_ACTIONABLE_DELTA
  palomar_jc_new=0 ; palomar_entries=188
  ratto3423=REACTIVATED_2026-09-05T13:09Z ; ratto3423_writeup=ABSENT
  spotchecks_confirmed=aejon-lean-no-invertibility|1605.09430-is-2016
  campaign_baseline_effect=NONE
```

<!-- BODY-END -->
