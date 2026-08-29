# Hostile review — actual-total `T-c0`/`T-c1` rho-unit certificates (Fable 5, 20260827)

Round: post-`20260826T2350Z` producer follow-up
Reviewer: Fable 5, different-model adversarial algebra review
Date: 2026-08-27

Verdict: **REPAIRABLE.**

- The upstream literal-source provenance dependency — the one obligation the
  producer's status line leaves open — is **DISCHARGED here for rows 2 and 4**:
  I rederived `Tg10_2` and `Tg10_4` (and, as corroboration, both rows' full
  grade-10/11/12 total and frozen coefficient files, twelve `.poly` files in
  all) from the literal actual-total V0R1 source emitter and the charged
  `tails.json`, with a from-scratch evaluator that imports no campaign
  compiler.  Every file matches the hash-pinned V9 export exactly (§3).
- Identities (1)–(3) are **EXACT** as printed, every coefficient and sign
  (§4).
- These are **honest direct total-family rho-unit certificates, not
  specialized analogies** (§7) — with one asymmetry the producer's summary
  paragraph obscures:
  - `T-c0` is stronger than claimed: a **full-chart, ordering-free,
    localizer-free** certificate (§5).  But its stated mechanism — "Since
    `c0` is inverted on this chart" — is **false as written**: `c0` is the
    exceptional equation of `D_+(c0)`, not a unit of the chart ring.  The
    correct mechanism is free `c0`-power absorption by the kernel=saturation
    presentation; the exact repaired certificate is supplied and verified.
  - `T-c1` is a **`c1`-localized** certificate.  Localizing at `c1` — the
    exceptional coordinate of its own chart — is legal but costs a residual
    closed stratum `V(c1) ∩ (ordered c1-stratum)` that **no other chart or
    stratum picks up** and that the note's debt list does not name (§6).
    This is a new mandatory ledger entry, not a retraction.
- One wording defect: "The coefficient `k` is not used by the identities" is
  false for (3), which contains `k` in two cofactor terms; the true statement
  is that **no localization at `k` is required** (§8).

Per instruction, nothing here touches `T-cs`, the `a0/a1` second stage, the
terminal receiver, `k=0` strata, the generic deck/square bridge, order two,
maximum twelve, or JC2.

## 1. Charged inputs, all rehashed this session

```text
6a29aac9506fba6ffd7f12a35efedb7501fb149d8f5d7c949740e8b1c2876da6  xmodel/max12-812-order2-p0-total-rees-t-c0-c1-rho-unit-producer-sol-20260827.md
db160c13351bab3a238582601e9a4f444ff98319524722176afb4ef047c54b00  xmodel/ideation-20260826T2350Z-rho-unit-hostile-review-fable5.md
50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4  xmodel/max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md
86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e  .../aws_q_v9/COEFFICIENTS.json
50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6  .../aws_q_v9/compiled/Tg10_2.poly
6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d  .../aws_q_v9/compiled/Tg10_4.poly
```

(`...` = `cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826`.)
All three producer-quoted hashes match the on-disk artifacts.  The two `.poly`
files read verbatim as displayed in the producer note.

Boundary: no web, no AWS mutation, no `jc2-lean`.  Local tool use: `shasum`,
file reads, and one light exact-arithmetic Python script (sparse polynomials
over `Q`, `Fraction` coefficients, sigma-truncation at 13; sha256
`5fdd854b3bb5ddd442d65a475d0468e24853b0569a39a6613514f5cb6cd513a5`, staged at
`/tmp/rho_unit_rederive_fable5.py`, session-local, not committed).  No
Groebner bases, no Singular, nothing heavier than truncated series products —
exactly the discriminator the producer note itself proposes.

## 2. Provenance chain to the V0R1 emitter — every pin verified

The V9 export chain imports frozen predecessors by hash.  I rehashed every
link down to the leaves:

```text
V9 wrapper pins V8   41484e92ac2c3433562b8f120c922cb8d2bff5bff736c4b5664989c692dc85fa  VERIFIED
V8 pins V7           c678d293c2c26462c3ca5cc3776644b181176a2cf657b0beb6b65754c7dcd2d0  VERIFIED
V7 pins V6           9937fcfc61dff1d39029e6653b2be73ab3f835c2bc8bc81405876e54ef10b6bf  VERIFIED
V6 pins stream V2    5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112  VERIFIED
stream pins V0R1     3aa6bbbbe539607461c5f27b400aeedd335a4d18e01e40d730f5537da4f45938  VERIFIED
  (= cases/..._t_rs0_discovery_20260826/compile_t_rs0_discovery.py, the
   literal actual-total emitter; also pinned by the discovery FREEZE.sha256)
V0R1 pins base       77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc  VERIFIED
  (= compile_square_load_ladder.py, whose tail_text/term_text define the
   row-formula semantics)
V0R1 pins tails.json d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  VERIFIED
  canonical form     6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8  VERIFIED
  569 total entries; row 2: 54 entries, row 4: 81 entries                        VERIFIED
```

Run-side corroboration (not load-bearing for the mathematics, since §3
recomputes everything, but checked): the generated `t_rs0_row2_q.sing` and
`t_rs0_row4_q.sing` hash-match the manifest's `row_records.input_sha256`
(`6cd1fcd9...`, `1c6d2f29...`); the row stdouts hash-match
`stdout_sha256` (`5f22f638...`, `2c21a291...`) and print the **conditional**
PASS banner `T_RS0_ROW_SHARD_ENDPOINT=PASS_NAVIGATION_ONLY` after a real
fail-closed gate on computed sentinel ints
(`prefixMap*deck*extraction*coefficientMap*explicitNF`), all `=1`; the
validator verdict is `PASS_T_RS0_EXACT_COEFFICIENT_EXPORT_V9`;
`EVIDENCE.sha256` (65 entries) pins the manifest and both rows at the quoted
hashes; `KeepT10_2.poly` is byte-identical to `Tg10_2.poly`.  The
`F_65521` control-lane hashes equal the producer's quoted
`dc775709...`/`491dec9e...`/`75330c39...`, and I checked the mod-65521
encoding by hand: `1024 ≡ 15/64`, `−24570 ≡ 3/8`, `−21819 ≡ 5/1024`,
`26618 ≡ 3/32 (mod 65521)` — the control lane is arithmetically consistent
with the Q display on every coefficient of both rows.

## 3. Independent source-only rederivation  [EXACT — the charged discriminator]

I reimplemented, from scratch and without importing any campaign module:

- the **literal total source** of the V0R1 emitter's `source_block`:
  `T_p = -2*rho^2 + Σ_{i=1..12} 2*sigma^i*ell_i` (the corrected moving
  source; the wrong literal `p=-2*rho^2` is *not* what is emitted),
  `T_c = sigma^2*(cs + sigma*cs1 + ... + sigma^10*cs10)`,
  `T_r = (T_p^2 + sigma^2*(rs + ... + sigma^10*rs10))/4`,
  the four normal series `T_n3..T_n0` (with `T_n1, T_n0` carrying the
  `(T_p*a-series + e-series)/2` structure), the seven generators
  `T_F6=2T_p`, `T_F5=2T_c`, `T_F4=T_p^2+2T_r`, `T_F3=2T_pT_c+sigma^2T_n3`,
  `T_F2=T_c^2+2T_pT_r+sigma^2T_n2`, `T_F1=2T_cT_r+sigma^2T_n1`,
  `T_F0=T_r^2+sigma^2T_n0`, and loads `T_K10` (9 jets), `T_K6`, `T_K2`;
- the **frozen owner side** (`F_` prefix: `rho` absent, 3-jet truncations);
- the **row-formula semantics** of the base `term_text`/`tail_text`:
  term = coeff · Π `F_i^{m[i]}` · (single load) · `Lambda^{Σ load-weights}`
  with `Lambda -> sigma^2`, load exponents guarded to `{0,1}` with at most
  one load per monomial, and the per-monomial weight census
  `Σ m·(8-i | 2,6,10) = 12 + row` (I re-enforced all three guards over rows
  2 and 4; all entries pass); row targets `-sigma^{2(12+row)}*mu_row` vanish
  identically mod `sigma^13`;
- **sigma-adic extraction**: grade-`g` coefficient of the truncated row.

Results, for both rows 2 and 4:

1. **Total grades 0–9 vanish identically** — the total rows have sigma-order
   exactly 10, matching the run's `T_RS0_GRADE_g_NONZERO` flags.  This is a
   nontrivial global cancellation across (54 resp. 81) tail monomials and is
   reproduced independently here.
2. **Deck**: both total rows are even in `rho`.  **Specialization map**: the
   `rho=0` image of every total grade 0–12 equals the frozen-side grade.
3. **All twelve exported files match exactly**: `Tg10_2`, `Tg11_2`, `Tg12_2`,
   `Fg10_2`, `Fg11_2`, `Fg12_2`, `Tg10_4`, `Tg11_4`, `Tg12_4`, `Fg10_4`,
   `Fg11_4`, `Fg12_4` — polynomial-equality against my parse of each `.poly`
   file, exact rational coefficients.  Term counts 5 and 2 at grade 10 agree
   with the (here non-pathological) telemetry.

**Independently derived rows** (my evaluator's output, canonically sorted):

```text
Tg10_2 = 3/8*a0*c0 + 3/8*rho^2*a1*c1 + 3/32*c1^2
       + 15/64*rho^2*cs^2*rs*k + 5/1024*rs^3*k
Tg10_4 = 3/32*c0^2 + 3/32*rho^2*c1^2
```

identical to the V9 display and to the hash-pinned files.  **The exports'
upstream literal-source provenance dependency is discharged for these two
rows.**  (The four `T-rs` rows charged by the earlier promotion are *not*
re-extracted here and remain on their own firewall.)

Note on independence: the AWS path computes these rows through the V8
incremental normal-form schedule; my path evaluates the V0R1 legacy formula
directly.  Exact agreement of all twelve files also settles, for these two
rows, the semantic equivalence of the two pipelines.

## 4. Identities (1)–(3) — every coefficient and sign  [EXACT]

Expanded against my independently derived rows (not the display):

- **(1)** `3*c0^2 = 32*Tg10_4 - 3*rho^2*c1^2` — exact.
- **(3)** `3*c1^2 = 32*Tg10_2 - 12*rho^2*a1*c1 - (15/2)*rho^2*cs^2*rs*k
  - (5/32)*rs^3*k - 12*a0*c0` — exact.
- **(2)** is (3) modulo `(rs,cs,c0)`: exact, with the explicit cofactor form

  ```text
  32*Tg10_2 - 3*c1^2 - 12*rho^2*a1*c1
    = (15/2)*rho^2*cs^2*k * rs + (5/32)*k * rs^3 + 12*a0 * c0,
  ```

  every remainder term carrying an explicit `rs`- or `c0`-cofactor.  Hence
  `3*c1^2 in (Tg10_2, rho, rs, cs, c0)` exactly as claimed.

The ordered `J1` substitutions are the correct bilinears for each chart
(`rs=c0*qrs, cs=c0*qcs, c1=c0*qc1` on `D_+(c0)`; analogously over `c1`), and
the ordered complements match the obligation table's chart order
(`rs`, `cs`, `c0`, `c1`); both the ratio and base-function stratum readings
are licensed by the promoted covering analysis.

## 5. `T-c0`: full-chart certificate; producer's mechanism mistyped  [EXACT]

**Defect.**  "Since `c0` is inverted on this chart" is false.  On `D_+(c0)`
the chart ring is `C = A[J1/c0] ⊂ A_{c0}`; `c0` is the exceptional equation
(`J1*C = (c0)C`) and is *not* a unit of `C`.  This is precisely the
exceptional-coordinate/unit conflation the `20260826T2350Z` review's §5
exists to refuse.  The producer's "equivalently" display
`(32/(3*c0^2))*Tg10_4 = 1 + rho^2*qc1^2` is an identity of `C[1/c0]` only.

**Repair — and an upgrade.**  The following polynomial identity is exact (I
verified it by expansion, with `qc1` a fresh variable):

```text
3*c0^2*(1 + rho^2*qc1^2)
  = 32*Tg10_4 - 3*rho^2*(c1 + c0*qc1)*(c1 - c0*qc1).           (1')
```

This is a corrected-lemma certificate `(*_s)` with `f_i = c0`, `N = 2`,
`s = 3` (invertible — effectively `s = 1`), `U = 1 + rho^2*qc1^2`, relation
list = `{Tg10_4}` plus the single bilinear `c1 - c0*qc1`, and `E = ∅`: **no
ordered stratum and no localizer at all**.  By kernel = saturation
(obligation (2.3)) and free absorption of exceptional powers, `(1')` gives
`1 + rho^2*qc1^2 = 0` in the honest chart ring, hence `1 in rho*C`:

**`rho` is a unit on the entire `T-c0` chart of the total family; its
`rho = 0` fibre is empty — including the exceptional locus, with no ordering
hypothesis and no `D(k)` restriction.**  The producer's invocation of the
ordered complement `qrs = qcs = 0` is unnecessary for this chart (identity
(1) involves neither `rs` nor `cs`), and the conclusion survives the false
"inverted" step under the repaired mechanism.  Stronger scope than claimed.

## 6. `T-c1`: honest, but localized — new residual obligation  [EXACT]

On the ordered stratum (`rs = cs = c0 = 0` or the ratio form), my derived row
gives the exact factorization

```text
32*Tg10_2  ≡  3*c1*(c1 + 4*rho^2*a1)      (mod (rs,cs,c0) + bilinears),
```

verified by expansion.  One free `c1`-saturation step puts
`c1 + 4*rho^2*a1` in the honest stratum ideal, i.e. `c1 = -4*rho^2*a1` in the
honest ordered stratum ring.  Consequences:

- **Localized (the producer's claim): correct.**  Inverting `c1`,
  `(32/(3*c1^2))*Tg10_2 = 1 + 4*rho^2*(a1/c1)` holds in the localization,
  `a1/c1` being an honest element there (it is *not* a `J1` ratio variable,
  exactly as the note says), and the localized ordered `rho = 0` fibre is
  empty.
- **Unlocalized: NOT empty as proved.**  Without inverting `c1`, the ordered
  stratum's `rho = 0` fibre is only shown to lie in `V(c1)`.  On `D_+(c1)`,
  `V(c1)` is the exceptional divisor of that chart, and a point of the
  ordered stratum with `c1 = 0` has all of `rs, cs, c0, c1` and all three
  ratio coordinates vanishing — the `rs`, `cs`, `c0` sections all vanish
  there, so **no other chart or earlier stratum covers it**.  DVR arcs with
  `J1*R' != 0` and `ord(c1)` minimal-positive among the four generators route
  their lifted closed point exactly there.
- The residual

  ```text
  V(c1) ∩ (ordered c1-stratum) ∩ (rho = 0)      [stage one, on-chart]
  ```

  is therefore a **new mandatory closed obligation**.  It is *not* named by
  the note's debt line "closed localizer strata such as `k=0`", which lists
  only source-side localizers; `c1` is the exceptional coordinate of its own
  chart, a different and previously unledgered residual type.  (Candidate
  closure route: a second certificate on that residual from the remaining
  grade-10/11/12 rows — `Tg11_4 = 3/16*c0*e0 + 3/16*rho^2*c1*e1
  - 3/32*c1^2*ell1` and its siblings engage the `e`-jets there — but that is
  a new bounded search, not this note's content.)

The summary sentence "(1)–(3) are direct total-family rho-unit certificates
for the ordered `T-c0` and `T-c1` charts" must be repaired to: full-chart
certificate for `T-c0`; **`c1`-localized** certificate for `T-c1` with the
residual above entered in the localizer/stratum ledger.

## 7. Honest direct total-family certificates, not specialized analogies

Determination as charged: **direct and total, not analogies.**

- The rows are the actual grade-10 coefficients of the actual-total V0R1
  moving source (all twelve `ell` jets and `rho` present in the emitter),
  independently recomputed here; they are not lifts-by-analogy of the frozen
  endpoints.  The `rho`-terms `(3/8)*rho^2*a1*c1`, `(15/64)*rho^2*cs^2*rs*k`,
  `(3/32)*rho^2*c1^2` are genuine total-family content with no frozen
  counterpart.
- The frozen `(3/32)c0^2`-type elementary units of the obligation table §4
  are recovered as the literal `rho = 0` shadows (`Fg10_4 = (3/32)*c0^2`;
  `Fg10_2 = (3/8)*a0*c0 + (3/32)*c1^2 + (5/1024)*rs^3*k`), i.e. the
  implication runs total ⟹ specialized, as an emptiness certificate must.
- **Later-row stability: confirmed.**  (1'), (2), (3) are ideal-membership
  identities; they persist verbatim in every further quotient obtained by
  adjoining later source equations, and the finite-prefix side conditions
  (common bivariate emitter, overcomplete jet ceiling, restricted names) are
  those of the charged V0R1 design.
- The certificates consume no `D(k)` hypothesis (see §8), so they hold on
  the full registered family and a fortiori on its `D(k)` stratum; the
  note's decision not to *enlarge* the registered scope is sound.

## 8. Nits (wording only, no mathematical content at stake)

1. "The coefficient `k` is not used by the identities" — false for (3),
   whose remainder carries `(15/2)*rho^2*cs^2*rs*k` and `(5/32)*rs^3*k`.
   True statement: identity (1) is `k`-free, and neither certificate
   requires localizing at `k`.
2. "Since `c0` is inverted on this chart" — see §5; replace by the
   saturation mechanism.
3. The producer's manifest telemetry is trustworthy here (counts 5 and 2 are
   true term counts; the known sign-count overcount does not trigger on
   these positive-leading rows), but the hash-bound `.poly` files remain the
   authority, as used throughout.

## 9. Obligation ledger

**Discharged this session:**

1. Literal-source provenance of `Tg10_2` and `Tg10_4` (the producer's sole
   flagged dependency): rederived from the frozen V0R1 emitter + charged
   tails; exact match, including grades 11–12 and the frozen side.
2. Exact expansion of (1), (2), (3); the `(*_s)`-typed full-chart repair
   `(1')` for `T-c0`; the stratum factorization behind `T-c1`.

**Repairs required before promotion (this note's producer):**

1. Restate the `T-c0` mechanism via saturation (`(1')`), deleting the
   "`c0` is inverted" step; scope may be *widened* to the full chart.
2. Retype `T-c1` as `c1`-localized; add the residual
   `V(c1) ∩ ordered c1-stratum` to the localizer/stratum ledger.
3. Fix the `k`-usage sentence (§8.1).

**Retained (unchanged, per the standing ledger):** the `T-cs`
control/certificate; the `T-c1` residual just named; second-stage `a0,a1`
charts over `V(J1)`; the terminal `V(J1+J2)` receiver; source-side localizer
strata (`k`-naming still to be pinned); provenance of the four `T-rs`
promotion rows (not re-extracted here); the seven `A` shards; the generic
deck/square `D(rho)` bridge; every broader claim.

## 10. Nonclaims and firewall

- Nothing here proves any chart empty beyond: (i) the full `T-c0` chart of
  the registered total family (conditional now only on the frozen artifacts
  reviewed and rehashed here, the covering/saturation lemmas of the charged
  `20260826T2350Z` review, and the standing scope of the registered source
  design), and (ii) the `c1`-localized ordered `T-c1` stratum, with its
  named residual outstanding.
- No `T-cs`, `a0/a1`, terminal-receiver, `k=0`, deck/square, order-two,
  maximum-twelve, or JC2 inference of any kind.
- The AWS attestations were corroborated but are not load-bearing: every
  mathematical statement above rests on the session rederivation plus hand
  algebra.
- This file is my only repository edit.
