# LANDING-LEDGER — primary research: the total typed landing obligation as a fail-closed compiler

Date: 2026-08-29 (UTC). Lane: Fable 5, equal-standing whole-campaign researcher.
Charge: design the smallest sound compiler/audit that turns the campaign's
amorphous full-configuration landing gap (REDUCTION CRITICAL 4-6) into a
typed, fail-closed ledger. This document is the design, the first packet
specification, and the verdict. It is not an implementation.

Inputs read in full, and only these: `ladder/REDUCTION.md`,
`ladder/SHEET6-DEPTH.md`, `ladder/SHEET6-MULTIPOLE.md`,
`ladder/BOOK-OFFAXIS.md`, `xmodel/ideation-20260829T0002Z-fable5.md` Card B,
`xmodel/ideation-20260829T0002Z-sol56.md` Card 1. Direct citations inside
those files are used at statement level only, to identify the promoted source
of each transition rule. No other ideation submission, no `jc2-lean` access,
no web/AWS/heavy CAS, no canonical edit. The only local computation was exact
rational spot-arithmetic reproducing formulas printed in the four ladder
files; every number below that came from it is re-derivable by hand.

Notation is ASCII: `kbar` = kappa-bar = kappa*(1-pi) (Not 9.1), `nu`, `mu`,
`rho`, `w = (kbar-rho)/nu`, `dp`/`dq` = reduced pattern degrees,
`Del = dq-dp` at merges and `(n-1)nu+1` at chain steps, `lam` = lambda,
`psi` = the St 9.4 terminal charge. Unqualified `kappa` occurs only inside
intrinsic terminal records `(h,chart,kappa,F)` and is a different quantity
(cover/Puiseux order); the ledger never conflates the two.

---

## 0. Verdict in one paragraph

**CONTINUE.** The typed schema below is minimal-sufficient: every field is
either consumed by a promoted move hypothesis or by a recorded downstream
kill, and the deleted fields (`w`, `M`, `rho`, `Lambda`, `X`, `psi`, `dp/dq`)
are proved derivable inside the promoted perimeter. The rule table covers
every currently promoted move with a negative control each. The three-way
classifier is total by construction because candidates are generated from a
grammar whose own completeness certificate (R1.0 / St 3.18 / Prop 9.3 case
list / MP6-R2.2 shape laws) is part of the packet; caps can only emit
`UNCOVERED`, never a rejection. The hand-run of the two-pole `td=6` sector
through the first post-jump boundary discharges everything except exactly
one family — the interior-merge `nu_G=1` eta-factor cells at odd `l>=5`,
which the promoted record excludes only by a machine cap (`l<=4`) — and it
finds that every cell of that family satisfies `dp | dq`, the exact
dead-pattern of the promoted td-7 zero-chain law, giving a concrete
candidate closing lemma. The right representation is parametric family
records with a symbolic frontier at `UNCOVERED` classes; pure enumeration is
impossible (three independent unbounded directions) and a pure symbolic
frontier would waste the promoted closure theorems. The first packet is the
`td=6, m=2` compiler with acceptance tests A1-A5. No output of this program
touches `G2-PSC`, `G2-BD`, `RPMC(C)`, or the cofinal degree ceiling.

---

## 1. The object, stated as an interface

Fix once per packet: topological degree `td`, global type `(alpha,beta)`
(Lemma 2.1; `2<=alpha<beta`, coprime), pole count `m>=2`, an entry
assignment `E` with per-pole identities, and a fibre token `a`. The ledger's
target theorem, per packet, is:

> **(LL-Soundness+Totality).** Let `CFG` be the set of full configurations
> of a normalized counterexample with these header data (the T6 objects of
> REDUCTION, inside the trust perimeter of Section 3 below). The compiler
> emits a finite set `FAM` of typed family records and a classification.
> (1) *Totality:* every configuration in `CFG` maps to a unique leaf path
> through `FAM` in which every step is `COVERED` or ends `TERMINAL`, or the
> path reaches an `UNCOVERED` family record; no configuration is unmapped
> and no transition is silently skipped. (2) *Soundness:* every `COVERED`
> certificate is valid over its cited trust set; every `DEAD` verdict kills
> all configurations through that family; `ALIVE` families are conservative
> supersets (realizability untracked). (3) *Provenance:* the map preserves
> entry identities, per-edge `(mu, case, zero-dir)` data, the unused-branch
> registry, and the lam-ledger; distinct entry contexts map to distinct
> records. (4) *Fail-closed:* the candidate generator's grammar-completeness
> certificate is part of the packet; any grammar residue is emitted
> `UNCOVERED` with its exact missing hypothesis.

Clause (4) is what makes the fail-closure honest rather than rhetorical:
totality is inherited from a *theorem* (the shape grammar), not from the
enumerator's loop bounds. This is the exact repair demanded by REDUCTION
CRITICAL 4 items 2-5 and by the sol56 bottleneck-1 wording ("emit `OPEN`
rather than silently omit an unknown transition").

---

## 2. Minimal typed state schema

### 2.1 Stored objects

**S-HDR (configuration header, immutable).**

| field | type | consumed by |
|---|---|---|
| `td` | int `>=6` | budget RHS (St 9.4), mass identity (T7); `td>=6` is a header invariant (Section 9 assembly), not a rule |
| `type=(alpha,beta)` | coprime ints | MP4/D4 entry pin, prime/beta-minimal forcing (global type) |
| `fibre` | opaque token | provenance; T7 holds at every fibre; no aggregation across fibres |
| `poles[i]` | `{id, a_i, b_i, nu_i, branch_token, deck_orbit_token, chart}` | R0; `branch/deck/chart` are opaque provenance for terminal-place identification (intrinsic L3-L5 layer); never consumed by transition rules |
| `hierarchy` | merge tree, `Sum(r-1)=m-1` (MP1) | R4/R7 event skeleton |
| `arrangement` | per merge: which arriving edge (if any) is the 0-direction | derives the Prop 9.3 case tag; E5-pinned solve |
| `H5a_reading` | pinned `Q-value` | every case-III rule application carries this flag (BOOK-OFFAXIS 11a: the two readings give different books) |

Header invariants (wellformedness, checked once): `Sum_i Lambda_i = td` with
`Lambda_i = a_i b_i alpha beta / nu_i` (Prop 5.6 (19) + SOL-PROP58/Chau
every-fibre repair); `Lambda_i >= beta >= 3`; the T7 `nu`-menu
(`nu|alpha & nu|b*beta-1` or `nu|beta & nu|b*alpha-1`); MP4 forcing `b=1`
at beta-minimal or prime `Lambda`.

**S-VTX (vertex frame, the mutable state).**

| field | type | notes |
|---|---|---|
| `zone` | `PRE_MERGE(i) \| INTER_MERGE(node) \| TRUNK \| ROOT` | position relative to `G*`; MP2 fires on nonroot `TRUNK`, MP3 exempts ancestors |
| `nu` | int `>=1` | vertex order; `nu>=2 => V_1` (Not 3.4) |
| `shape` | see grammar below | primary combinatorial datum |
| `kbar` | rational `>0` | the transported quantity; invariant: `kbar` integral when `nu>=2` (DS1(c)); rational legal at `nu=1` case-I vertices (BOOK-OFFAXIS P3) |
| `w_cert` | `W-CLOSED-FORM(DS3/DS4) \| W-PRICED(P0,budget) \| W-SYMBOLIC` | certification status of the derived `w`; load-bearing: R7's root kill fires only on the first two |

Shape grammar (this *is* the candidate generator; completeness certificates
R1.0 + St 3.18 + semi-invariance, review-confirmed in BOOK-OFFAXIS Sec. 6):

    SHAPE_CHAIN(l, n, eps_p, [m_j], lex, eps_q)
      p = T eta^eps_p (eta^nu - c^nu)^l Prod_j (eta^nu - d_j^nu)^m_j
      q = T eta^eps_q (simple orbits: chain + k noncchain + lex extras)
      dp = eps_p + nu(l + Sum m_j);  dq = (1 + k + lex)nu + eps_q
      eps_q = 1 forced at nu>=2 (R1.0 eta||q); free in {0,1} at nu=1.
    SHAPE_MERGE(nu, eps_p, [mu_e], [m_j], l, eps_q)
      dp = eps_p + nu(Sum mu_e + Sum m_j);  dq = (r0 + k + l)nu + eps_q
      (r0 = distinct nonzero arriving orbits; on-axis some-mu=1: k=0 forced,
       families IIa/ZCH/I of MP6(d)).

The explicit `eps_q` slot at `nu=1` is a deliberate schema addition: it is
what makes the eta-factor family *representable*, and the hand-run (Section
5) shows it is exactly where the current promoted record has its cap.

**S-EDGE (per edge, parent above child).**

| field | type | notes |
|---|---|---|
| `parent`, `child` | frame refs | full frames retained; no aggregation |
| `mu_e` | int `>=1` | arrival multiplicity; invariant `mu_e \| M(parent)` (St 8.4); down merge-free segments `M(child) \| M(parent)` when child not in `V_2` (St 8.5) |
| `zero_dir` | bool | from `arrangement` |
| `sym_constraints` | list | retained-not-checked admissibility (`n_e in N*`, `n_e = -kbar_e (mod nu_e)`, i-sync). Policy (stage-R, kept): never used to kill; recorded so the superset semantics are explicit in the record rather than implicit in an engine |

The Prop 9.3 **case tag is derived**, not stored:
`case = II` (non-0 edge at a `V_1` vertex), `III` (0-edge at a `V_1`
vertex), `I` (`V_2\V_1` vertex, including every genuine root merge), `IV`
(root endpoint outside `V_1 u V_2`; trunk terminal only). `V`-membership is
derived from `(nu, merge?, root?)`.

**S-LEDGER (per configuration, append-only).**

- `lam_ledger`: list of `(vertex_id, lam_lower_bound, pricing_rule)`.
  Lower-bound semantics is part of the type (BOOK-OFFAXIS Sec. 10 honesty
  riders): kills fire only when `Sum lam > td - 1 - psi`; equality routes
  carry a `FRAGILE` flag (any new printed unit kills them).
- `unused_registry`: list of `(vertex_id, orbit_spec, fate)` with
  `fate in { NO_TREE_VERTEX(St 3.18), NE_PRICED(lam, St 7.3 + AF2),
  DECK_CONJUGATE(one continuation per orbit), UNKNOWN }`. `UNKNOWN`
  forces the enclosing family `UNCOVERED`. This registry is the "unused
  branches" obligation of REDUCTION CRITICAL 4 item 4 made first-class.
- `cert_chain`: per rule application, `(rule_id, tier, sources)` with
  `tier in {printed-P1..P4, H1, promoted(hash)}`. A trust-perimeter change
  invalidates exactly the records citing the changed source — this is why
  theorem-source is a stored field and not documentation.

### 2.2 Derivability proofs (deleted fields)

| field | derivation | source |
|---|---|---|
| `M` | `= gcd(dp,dq)` at every vertex; at entry `gcd(b*alpha,b*beta) = b` | Prop 8.1(v) as used in MULTIPOLE D6(d), R2.2(D); MP4 |
| `rho` | `= a/b` at entry; `= kbar/dq` at every post-entry frame | entry: St 5.2(i). Post-entry: DS2/R1.2/R1.4 give `kbar = rho*dq` on all chain transports; at merges `rho = X/dp` with the Prop 9.3(b) consistency `X/kbar = dp/dq` — the defining equation of the merge solve, hence safe to bake in |
| `w` | `= (kbar-rho)/nu` | definition (DEPTH Sec. 1) |
| `X` | `= rho*dp = kbar*dp/dq` | same |
| `Lambda_i` | `= a_i b_i alpha beta / nu_i` | Prop 5.6 (19) |
| `psi` | `= ceil(1/(1-w_G)) - 1 = ceil(M/j)-1`, `j = M(1-w) in N*` | P1/H3-psi, Prop 9.3(k),(m) |
| `dp,dq` | from `shape` | grammar above |
| budget remaining | `td - 1 - psi - Sum lam` | St 9.4 (25) |

Deleting `w` and `M` while keeping `kbar` and `shape` is the correct
minimality direction: `kbar` is the transported primary (the only field the
chain rules actually advance), and the shape is the only field the merge
solve actually constrains. Everything the downstream kills quote (`w`
alphabets, `M`-divisibility, `X>0`, `psi`) is a view.

### 2.3 Added fields, with load-bearing justification

1. `arrangement`/`zero_dir` — without it the case tag (hence the handshake
   *form*: `X = mu(kbar - w)` vs `X = mu_0(kbar - nu_e w)`) is not derivable;
   the DEPTH Sec. 5c correction exists precisely because an engine modeled a
   case-III edge with case-II equations.
2. `w_cert` — the mixed-root window kill ("any independently certified
   `w>=1` branch kills a root meet", BOOK-OFFAXIS header 2026-08-28) is
   unsound without a certification status: post-jump `w` values are only
   budget-priced, and inner-merge arrivals are `W-SYMBOLIC` until trunk
   transport is composed.
3. `eps_q` at `nu=1` — representability of the eta-factor family (Section 5).
4. `sym_constraints` — makes the conservative-superset semantics a typed
   property of the record instead of engine folklore.
5. `H5a_reading` pin — every case-III solve is conditional on the promoted
   Q-value reading; BOOK-OFFAXIS 11a records that the two coherent readings
   produce different books (17 vs 2 cells at td=7).
6. `cert_chain` tiers — REDUCTION's referee checklist requires the frozen
   status snapshot to be citable per record.

---

## 3. Rule table (every currently promoted move)

Every rule lists: preconditions (exact), transform, preserved provenance,
source, and one negative control that a correct implementation must reject
(mutation tests A4). All rules preserve S-HDR verbatim, never merge two
configurations, and append to S-LEDGER monotonically.

**R0 ENTRY** (per pole `i`).
- Pre: header invariants; entry `(a,b,nu)` in the T7 menu.
- Out: frame `(zone=PRE_MERGE(i), nu=nu_i, shape=entry, kbar=a(alpha+beta))`;
  derived `M=b`, `rho=a/b`, `w0=a(b(alpha+beta)-1)/(b nu)`;
  `w_cert=W-CLOSED-FORM`.
- Provenance: pole id + branch/deck/chart tokens attach here and are carried
  by every descendant record.
- Source: St 5.2(i), Not 8.1, Prop 5.1(i)+Not 5.1-5.2 (repaired sided
  thresholds), corrected Prop 4.2 with `h_0=g` (constant-shift erratum
  packet, incl. the no-first-constant-corner layer on `T_a^+`), St 2.1;
  T7 = Props 5.3/5.5-5.7 audited + SOL-PROP58 + Chau 4.4.
- Negative control: entry with prime `Lambda` and `b>=2` must be rejected
  (MP4/D4); `Sum Lambda != td` must be rejected.

**R1 CHAIN-NEUTRAL** (clean step, `n=1`).
- Pre: non-merge child, `SHAPE_CHAIN(l,1,0,[],0,1)`, `l | M(parent)`
  (St 8.4); non-0 edge; `nu_child >= 2` free parameter.
- Transform: `kbar_child = w_G*(nu_child+1)` i.e. `w` fixed (`Del=1`);
  `lam += 0`; `M_child = gcd(l*nu, nu+1)`.
- Provenance: appends the `nu-1` conjugate orbit roots to
  `unused_registry` as `DECK_CONJUGATE` (St 3.18 one continuation per
  orbit).
- Source: DS1 (printed tier: St 3.16 iff, Not 3.4/3.5, Def 3.1, Prop 3.1,
  St 3.17(i)) + DS2 at `n=1` [H1]; off-axis: R1.1/R1.2 (`l` cancels).
  The chain-membership frame (`MP0`: characteristic sequences, leaves =
  poles) consumes repaired Props 6.7/6.8 (microstep -> next vertex,
  same-branch pole; `d_(F_n) <= d_F - n/kappa` descent) and St 6.2 with its
  restored `H in V_a cap T_a^+` hypothesis.
- Negative control: a `nu_child=1` chain child must be rejected as a `V_a`
  vertex (St 3.16 iff — the recorded twopole_check over-generation).

**R2 CHAIN-RESONANT** (clean step, `n>=2`).
- Pre: as R1 plus `Del := (n-1)nu+1` divides `num(w_G)`; off-axis
  additionally `den(w_G) | dq` (both from `kbar_child in Z` at `nu>=2`).
- Transform: `w -> w*n/Del` (contraction `<= 2/3`); `kbar_child =
  w_G*dq/Del`; `M_child = gcd(l, n*nu+1)`.
- Source: DS3 [H1]; off-axis R1.2.
- Negative control: from `w=3/2`, the candidate `(n,nu)=(2,2)` (`Del=3 | 3`)
  must be rejected because `den(w)=2` does not divide `dq=5` — the exact
  BOOK-OFFAXIS Sec. 8 Step 2 filter.

**R3 CHAIN-DIRTY** (priced step; `l>=2` only).
- Pre: `l>=2`, `l | M(parent)`; shape with `eps_p`/non-chain orbits obeying
  the strict NE laws `eps_p*dq < dp`, `m_j*dq < dp`; own-edge searrow
  `E := l*dq - dp > 0`; `kbar_child = l*w_G*dq/E in Z` at `nu>=2`.
- Transform: `w -> l*w_G(dq-1)/(nu E)`; `lam += Sum_j max(1,
  ceil(X/m_j - kbar)) + [eps_p>=1]*max(1, ceil((X/eps_p - kbar)/nu))` (AF2
  rule); every non-chain orbit appended `NE_PRICED`; `M` can jump
  (`V_2`-escape: St 8.5 inapplicable).
- Source: R1.0/R1.3/R1.4 (review-confirmed) + P0 (corrected St 9.3 (24)
  with E6 sign fix, St 6.1/6.2, Prop 6.7, St 7.1/7.3, Not 9.3); St 8.4.
  Finiteness certificate per `(w,l)`: `E <= l*num(w)*T` (P0(i)); the
  pure-(b) family is `nu`-free with a single `w`-image (P0(ii)).
- Negative control: a dirty step at `mu=1` must be rejected (R1.3); a step
  with `l` not dividing the *current* `M`-state must be rejected — the exact
  `l|b`-conflation that produced the refuted `W_off` alphabet (Sec. 10 P4,
  the L2 cell autopsy).

**R4 MERGE** (interior; `r>=2` arriving edges).
- Pre: per-edge frames with `mu_e | M_e`; handshake system
  `X_G = mu_e(kbar_G - w_e)` for non-0 case-I/II edges,
  `X_G = mu_0(kbar_G - nu_e w_e)` for the case-III 0-edge (E5 pin: the
  `kbar` equation uses `nu_G`, not the arrival vertex; `H5a_reading=Q`);
  shape solve `X/kbar = dp/dq` over the merge grammar; searrow law
  `mu_e*dq > dp` per arriving edge; `m_j*dq < dp` for non-chain orbits
  (`k>0 => dq<dp`, R2.2(S)); `dq = 1 (mod nu)`, `gcd(M_G,nu)=1` (R1.0);
  root-mult law `dp != mu*dq` (R2.2(R)). On-axis (some `mu_e=1`): `k=0`
  forced (D6(a) via repaired 6.7/6.8), families IIa/ZCH/I with the MP6(d)
  gcd menus; `l=0` forces `M=1` or is impossible (MP7). Subadditivity
  `M_G | Sum mu_e` may be *used* only when `eps_p=0` and `k=0` (R2.2(D)).
- Transform: emit child frame `(kbar_G, shape)`; `M_G = gcd(dp,dq)`;
  `lam +=` P2 prices (NE orbits, free 0-root; arriving edges and q-extras
  price 0); `unused_registry +=` the `l` q-extras as `NO_TREE_VERTEX`;
  child typing: `M_G=1` -> new M=1 segment entry with
  `w_child = w*(r+l)/(l*nu+1)` (DS4 5b; `=r*w` at `l=0`); `M_G>=2` ->
  suffix segment with `w_child = (kbar_G - X_G/dp)/nu_G`.
- Mixed residue (fail-closed): for all-`mu_e>=2` merges the emitted-`M_G`
  menu with `k>0` or `eps_p>0` has **no completeness theorem**
  (BOOK-OFFAXIS Sec. 3: explicitly OPEN); the generator emits that residue
  class as `UNCOVERED(complete mixed-merge emission menu)` — never as an
  enumerated list.
- Source: MP6/MP7 (P1-P4 tier), R2.1/R2.2 (review-confirmed), E5
  (promoted, H5a-Q conditional), DEPTH Sec. 5a-5c handshakes.
- Negative controls: (a) equal-`mu` join with unequal certified `w` must be
  rejected (R2.1(i)); (b) all-`mu=1` `l=0` emitting `M>=2` must be rejected
  (MP7); (c) a `k>0` shape with `dq>dp` must be rejected (R2.2(S)); (d) a
  case-III edge solved with case-II equations must be caught (the DEPTH
  Sec. 5c engine correction, preserved as a permanent mutation test).

**R6 TRUNK-M1-KILL** (corrected Prop 8.4 = MP2/MP3).
- Pre: nonroot vertex, `zone=TRUNK` (i.e. `F <= G*`), `G* != (0,y)`,
  derived `M=1`.
- Out: configuration `DEAD`; certificate = D3 chain (Prop 8.3 under the P1
  regularity reading, St 8.1, Cor 6.1 + Prop 6.3, Thm 6.1, unique-
  predecessor D2).
- Provenance: kill recorded with the full path; no other configuration
  affected.
- Source: MULTIPOLE MP2/MP3 with the 2026-08-28 root-scope supersession.
- Negative control: a root `(0,y)` state with `M=1` must **not** be killed
  (St 8.5 permits root `M=1`; the historical root-before-`M=1` ordering bug
  is the permanent regression test).

**R7 ROOT-MEET** (genuine merge at `(0,y)`; case I).
- Pre: contact-zero meet, `(0,y) in V_2\V_1`; per actual searrow parent
  edge `X_R = mu_e(1-w_e) = A/B`, hence `w_e = 1 - A/(mu_e B) in (0,1)` —
  no `mu_e=1` hypothesis (mixed-root window); all-`mu=1` `r`-way meet:
  `(dp,dq)=(r,r+l)`, `l>=1`, `w_e = l/(r+l)`.
- Kill: any arriving edge whose `w_e >= 1` with
  `w_cert in {W-CLOSED-FORM, W-PRICED-complete}` -> `DEAD`. A `W-SYMBOLIC`
  arrival never kills; it leaves the family `ALIVE`-conservative or, if the
  transport to certify it is itself missing, `UNCOVERED`.
- Source: Prop 9.3 case I (c),(d) + Prop 8.1(i) + St 3.17 + St 9.2
  (`K_F=1`) [H1]; DEPTH Sec. 5d; mixed-root window (hostile-confirmed).
- Negative controls: case-IV equations applied to a genuine merge must be
  rejected (the historical false label); `l=0` at the root must be rejected
  (`0 = T p` impossible, D9); the legal local cell `r=2, l=1, w=1/3` with
  `M_root=1` must **not** be rejected (root `M=1` is legal).

**R8 TRUNK-TERMINAL** (case IV; last searrow vertex above `(0,y)`).
- Pre: `w_G < 1` (case-IV `d_F/deg p_G = 1 - w_G > 0`); `M_G >= 2` (MP2);
  `j := M_G(1-w_G) in N*` (Prop 9.3(m) i-normalized).
- Out: `TERMINAL(record)` with `psi = ceil(1/(1-w_G)) - 1 = ceil(M/j)-1`;
  immediately triggers R9. The terminal record carries the link slot for
  intrinsic identification `(h,chart,kappa,F)` — an opaque pointer, not a
  computation performed here.
- Source: P1/H3-psi (chart transport via Lemma 2.1(i)/St 3.12/St 3.17(i)),
  Prop 9.3(i)-(m), St 9.2.
- Negative control: a terminal with `w>=1` or `j not in N*` must be
  rejected.

**R9 BUDGET** (configuration-level).
- Pre: a completed route with terminal `psi`.
- Check: `Sum lam <= td - 1 - psi` over pairwise-distinct searrow vertices,
  shared suffix counted once (MFE attachment theorem; actual-weight
  Cor 7.1). Violation -> `DEAD`. Equality -> `ALIVE+FRAGILE`.
- Source: St 9.4 (25)/(26); MP8 at inequality scope only — the literal
  (22), `(22-cl)`, equality/no-refinement rhetoric stay quarantined and no
  rule may cite them.
- Negative control: a shared suffix priced once per pole path must be
  rejected (double count); on an equality route, a planted extra printed
  unit must flip the verdict to `DEAD` (slack accounting test).

**Source-tier crosswalk (Card B move list).** Prop 5.1 sidedness and the
no-constant-corner theorem enter through R0's entry typing; Props 6.7/6.8
and St 6.2(+H) enter through R1/R4's chain-membership and `k=0` manufacture;
Prop 8.4 (nonroot) is R6; St 8.5 is the S-EDGE divisibility invariant; the
mixed-root window is R7; MFE + Cor 7.1 are R9; Section 9 `td>=6` is a header
invariant. Single-pole moves (TDU/Prop 8.4 at `s=1`) are a separate sector
compiler with the same schema and are out of packet 1's scope by design.

---

## 4. The total three-way classifier

For every state `s`, the generator produces the complete candidate family
`Cand(s)` from the shape grammar (Section 2.1) plus the event skeleton
(hierarchy/arrangement). Then:

    classify(s, c) =
      COVERED(R, cert)        c is admitted by rule R with a discharge of
                              every precondition (cert = the instantiated
                              derivation, tiered), or c is refuted by rule R
                              (cert = the kill derivation). Both are
                              "covered": described-and-decided.
      TERMINAL(record)        s has no outgoing transition and R7/R8 emit a
                              complete terminal record.
      UNCOVERED(h)            otherwise; h = the exact missing hypothesis,
                              as a named statement with its smallest
                              blocking instance and the list of blocked
                              consumers.

Hard prohibitions, each of which is a checkable property of the output:

1. **No silent skip:** `Cand(s)` partitions into the three classes; the
   partition is emitted, not summarized.
2. **No default:** there is no "else" branch; an unmatched candidate is
   `UNCOVERED` by construction.
3. **No cap exhaustion as decision:** a cap (engine bound, sweep window,
   depth limit) may only produce `UNCOVERED`, never a rejection. This
   single rule converts MULTIPOLE Sec. 4's flagged caps into ledger rows
   (Section 5 shows the concrete case).
4. **No aggregation across entry contexts:** records are keyed by the full
   S-HDR + path provenance; identical cells from different contexts are
   different records (the BOOK-ENUM "any-context survival wins" pattern is
   banned; REDUCTION MEDIUM 2).
5. **Kills are downstream of coverage:** `ALIVE`/`DEAD` is a separate
   dimension from `COVERED`/`UNCOVERED`; an `ALIVE` family is a conservative
   superset and says nothing about realizability.

---

## 5. Hand-run: two-pole `td=6` through the first post-jump boundary

### 5.1 Header and entry (R0)

`td=6`, `m=2` forces `Lambda=(3,3)`, `beta=3`, `alpha=2`, type `(2,3)`.
`Lambda=3` is beta-minimal and prime, so `b=1` forced (MP4); the T7
`nu`-menu (`nu | 2` and `nu | 2`) with `Lambda = 6a/nu = 3` forces
`(a,b,nu)=(1,1,2)` at both poles. **The entry menu has exactly one member;
the off-axis sector is empty at `td=6` (BOOK-OFFAXIS Sec. 4), so this
header is the whole sector.** Entry frames: `kbar=5`, derived
`(M,rho,w0)=(1,1,2)`, `w_cert=W-CLOSED-FORM`. Header invariants pass
(`3+3=6`; `Lambda>=3`).

### 5.2 Pre-merge chains (R1/R2)

`W(2)={2}`: no `Del>=3` divides 2, so R2 never fires; every step is R1 with
`nu_j>=2` free and depth unbounded. Classification: `COVERED(R1)` as a
**parametric family** (depth `*`, `nu_j` free), with the DS3/DS4 closure
certificate (`gen=0`, `d0<=2`) attached; reachable frames are exactly
`{(w,nu,kbar)=(2,nu,2nu+2)}`. Finiteness of *states* is not asserted —
depth is bounded only by the pole's characteristic-exponent count, which
`(m,td)` does not control (DS1 R1). Both chains arrive at the single merge
(MP1) with `mu=(1,1)` (MP5), `lam=0`.

### 5.3 The merge event (R4/R7): candidate partition

Arrangements: interior meet with no 0-edge, interior with either chain at
the 0-direction, or root meet.

| candidate class | classification | certificate / missing hypothesis |
|---|---|---|
| Root meet, any `l` | `COVERED(R7): DEAD` | case-I law needs `w_e<1`; both arrivals carry certified `w=2` (`W-CLOSED-FORM`); promoted analytic closure (MULTIPOLE 2026-08-28 header; DEPTH 5d) |
| Interior, 0-edge arrangements (ZCH) | `COVERED(R4): REJECTED` | case-III handshake demands `w_other = nu_e * w_0chain`, `nu_e>=2`; sole value 2 cannot satisfy `2 = nu*2` (DEPTH 5c; machine check 7, 403 solves, none joinable) |
| Interior IIa, `l` odd, `nu>=3` odd | `COVERED(R4): ADMITTED` exactly one cell | integrality `kbar = 2*dq/Del in Z` (DS1(c), `nu_G>=2 => V_1`) pins `(r,nu,l)=(2,3,1)`: `(dp,dq)=(6,10)`, `kbar=5`, `X=3`, `M=2`, child `Q=(6,12,3,2,5)` at `i=2`, `w_trunk=3/2`. Checked: `(2,5,1)`, `(2,3,3)`, `(2,7,1)`, `(2,5,3)` all fail integrality |
| Interior IIa, `l` even or `nu` even | `COVERED(R4): REJECTED` | `M = gcd(2, l*nu+1) = 1` -> MP2 kill downstream; MP9 |
| Interior `nu_G=1`, plain `q` (`eps_q=0`) | `COVERED(R4): REJECTED` | `l` even: exact log-obstruction, all `l`, td-uniform; `l` odd: `M=gcd(2,2+l)=1` -> MP2 (D9) |
| **Interior `nu_G=1`, `eps_q=1` (eta-factor), `l` odd `>=5`** | **`UNCOVERED`** | see 5.4 |
| Interior `nu_G=1`, `eps_q=1`, `l in {1,3}` | `COVERED: REJECTED (machine)` | l1_ode_check families B/B-eta, `l<=4` — an instance-level exact check, valid as a kill for those two cells only |
| Interior `nu_G=1`, `eps_q=1`, `l` even | `COVERED(R4): REJECTED` | `M = gcd(2, 3+l) = 1` -> MP2 |
| Mixed all-`mu>=2` candidates | not generated | `mu_e \| M = 1` forces `mu=(1,1)` (St 8.4 + MP5); the mixed `UNCOVERED` residue class of R4 is unreachable in this header |

### 5.4 The `UNCOVERED` family, made exact

Shape: `SHAPE_MERGE(nu=1, eps_p=0, mu=(1,1), m=[], l, eps_q=1)`, `l` odd
`>=5`; `(dp,dq)=(2,3+l)`. The handshake `X = kbar-2` with `X/kbar = dp/dq`
gives `kbar = 2(3+l)/(1+l)`, `X = 4/(1+l) > 0`, `M = gcd(2,3+l) = 2`
(`l` odd), `kbar in Q\Z` legal at `nu=1` (case I). Every promoted filter
passes: searrow (`dq>dp`), `gcd(M,nu)=1`, N1/L6 trivial at `nu=1`, no
lam price (the eta root is a q-extra; q-extras price 0). Instances:
`l=5: (2,8), kbar=8/3, w_trunk=7/3`; `l=7: (2,10), kbar=5/2, w_trunk=9/4`.
The promoted record excludes this family only by the flagged engine cap
`l<=4` (MULTIPOLE Sec. 4 "Engine caps"; DEPTH Sec. 6 "nu=1 cells only
`l in {1,2,4}` in that historical diagnostic"). Under classifier
prohibition 3 this is exactly an `UNCOVERED` row:

> `UNCOVERED(h)` with `h` = "uncapped exclusion of the interior all-`mu=1`
> `r=2` merge cells with `nu_G=1`, eta-factor `q` (`eps_q=1`), `l` odd
> `>=5` at `w=2`" — smallest instance `(dp,dq)=(2,8)`; blocked consumers:
> the exactness of the td=6 jump menu (DEPTH Sec. 6), MP9's survivor list,
> and every downstream td=6 residue argument that quotes "the menu is
> exactly IIa(2,3,1)".

**Candidate closing lemma (new observation, recorded for the named-lemma
queue).** Every cell of the family has `dp = 2 | dq = 3+l` (`l` odd). The
promoted td-7 generalized zero-chain law (BOOK-OFFAXIS Sec. 11, dual-
verified) proves T1-death exactly when `dp | dq` for its 0-chain cell class.
The family here is the `eps_q`-variant (0-root in `q`, not `p`), so the law
does not literally apply — but its mechanism (the reduced Prop 8.1(iv)
equation admits no admissible solution with nonzero RHS when `dp | dq`) is
the obvious candidate, and the `l<=4` machine kills are consistent with it.
A one-page extension of that law to `eps_q=1` would close this family
uniformly and restore "menu = exactly IIa(2,3,1)" as a theorem instead of a
capped record.

### 5.5 First post-jump boundary (the `M=2` suffix from `Q=(6,12,3,2,5)`)

Trunk state `(w,M) = (3/2, 2)`, `w_cert=W-PRICED(P0)`. The complete
one-step candidate partition (P0 menu is state-local, so the td-7
computation of the same state transfers; td enters only through the budget
RHS):

| step | classification | result |
|---|---|---|
| neutral thick `l=2, n=1`, `nu` odd | `COVERED(R1)`, parametric | `w=3/2` fixed; `M=2` iff `nu` odd (else `M=1` -> R6) |
| thin `l=1` any | `COVERED(R1): self-killing` | `M=gcd(nu,n*nu+1)=1` -> R6 `DEAD` |
| clean resonant | `COVERED(R2): REJECTED` | `Del=3` forces `(n,nu)=(2,2)`; `den(w)=2` does not divide `dq=5` |
| dirty (A) `(21,15), nu=7` | `COVERED(R3)`, `lam>=2` | `-> (w,M)=(2/3,3)` |
| dirty (C) `(20,16), nu=5` | `COVERED(R3)`, `lam>=2` | `-> (3/4,4)` |
| dirty eps `(7,5), nu=2` | `COVERED(R3+R6): DEAD` | `-> M=1` on the trunk, `lam>=3` moot |
| pure-(b) doubling | `COVERED(R3+R6): DEAD` | `-> (3,1)`, `M=1` |

Terminal arithmetic (R8/R9): from `(2/3,3)`: `j=1`, `psi=2`, budget
`6-1-2=3 >= Sum lam = 2` -> `ALIVE` (slack 1; at most one further priced
unit, e.g. an `l=3` step, before a `psi<=2` terminal — the packet
enumerates this finite residue). From `(3/4,4)`: `j=1`, `psi=3`, budget
`2 = Sum lam` -> `ALIVE+FRAGILE` (equality; any new printed unit kills).
Direct termination from `w=3/2` is `COVERED(R8): REJECTED` (`w>=1`).

### 5.6 What the hand-run establishes

Discharged with certificates: the root meet (DEAD), all ZCH arrangements,
all IIa cells but one, the plain `nu=1` layer, the mixed sector
(unreachable), the entire first post-jump step menu, and the terminal/budget
arithmetic of both surviving routes. Remaining symbolic: the parametric
depth/`nu` directions (by design — never enumerated); the suffix residue
below the boundary (finite, `<= 2` further priced units, compiler's job).
Remaining `UNCOVERED`: exactly one family (5.4). **Finiteness is asserted
only at the family-record level and only because three specific promoted
certificates exist for this header** (`W(2)={2}` closure; P0 budget-
boundedness with budget `<=4`; the single-merge hierarchy). The entry
menu's finiteness by itself proves nothing — the state space is infinite in
three independent directions (depth, per-step `nu`, and `kbar` at
equal-`mu` equal-`w` joins, which is a free parameter pre-integrality), and
at `td>=8` the budget argument is already known not to close panels
(BOOK-OFFAXIS P5). The expectation of ideation Card B ("the promoted
closures should leave exactly the interior residue plus known-open tags")
is confirmed, with the known-open tag now typed to one exact family plus a
candidate closing lemma.

---

## 6. Representation decision and the first packet

### 6.1 Decision

**Parametric family records, with a symbolic transition frontier exactly at
the `UNCOVERED` classes; enumeration only of derived finite quotients under
an attached closure certificate.** Grounds: (i) pure state enumeration is
impossible — unbounded depth (DS1 R1), unbounded `nu` at every neutral
step, free `kbar` at equal-`mu` equal-`w` joins; (ii) a pure symbolic
frontier discards the promoted finite quotients (DS3/DS4 `w`-closure, Sec.
5b cell determination, P0 pricing) that make sectors decidable at all;
(iii) the hybrid is exactly what the hand-run produced: finitely many
family records, each carrying either a closure certificate or an
`UNCOVERED` marker.

### 6.2 First packet: `LL-1 = (td=6, m=2)` sector compiler

Deliverable: one artifact (suggested `cases/landing_ledger_td6.py` +
JSONL output), compiling Section 5 mechanically. Record format per family:
`{header_key, path_provenance, family_spec(params+constraints),
classification, cert_chain, lam_ledger, unused_registry, verdict}`.
Exact integer/Fraction arithmetic only; every rule application cites its
rule id and tier; output includes the complete candidate partition per
event (prohibition 1).

Acceptance tests (all mandatory, exit nonzero on any failure):

- **A1 (record parity).** Reproduces: root meet `DEAD(R7)`; ZCH rejected
  (case-III solve, 0 joinable); admitted interior menu exactly
  `{IIa(2,3,1) -> Q(6,12,3,2,5)}`; plain `nu=1` rejected with the two named
  certificates; cross-checks against the promoted records (26 phase-4
  shapes at `w=2`; the 351/351 depth-invariance as a family-level
  assertion).
- **A2 (fail-closed).** The `UNCOVERED` list is nonempty and contains the
  `eps_q=1, l odd >=5` family with its named missing hypothesis and
  smallest instance `(2,8)`; every `UNCOVERED` row carries `h`, instance,
  and blocked consumers. Any additional `UNCOVERED` rows are findings to
  report, not failures.
- **A3 (post-jump boundary).** First-step partition from `(3/2,2)` exactly
  as the table in 5.5, including both `DEAD`-by-R6 rows; terminal
  arithmetic `j=1`, `psi in {2,3}`; verdicts `ALIVE(slack 1)` and
  `ALIVE+FRAGILE(equality)`; the finite sub-boundary residue enumerated to
  exhaustion of the budget.
- **A4 (mutation battery).** Each rule's negative control implemented as a
  planted mutation that must be caught: root-`M=1` kill (historical bug);
  `l>=1` omission at root cells; case-IV at a genuine merge; case-II model
  of a ZCH edge; equal-`mu` unequal-`w` join; `l`-vs-`M`-state conflation;
  shared-suffix double count; equality-route extra-unit flip; and a planted
  cap presented as a rejection, which must surface as `UNCOVERED`.
- **A5 (provenance).** Swapping pole ids or entry contexts produces
  distinct records; no record aggregates two contexts; `lam_ledger` and
  `unused_registry` are append-only; every record's `cert_chain` resolves
  to the frozen trust snapshot.

Cost: desk-scale (the whole sector is hand-run above); no AWS.
Second packet (only after LL-1 passes review): `td=7, m=2` including the
off-axis entry — the first header where `W-PRICED` certification, dirty
steps, case-III/E5, and the 11a conditional books all fire; its A1 baseline
is the 17-cell (Q-reading) census with the H5a flag carried explicitly.

### 6.3 Relation to the round's cards

This design is the execution spec for Fable5 Card B, and it supplies the
input sol56 Card 1 declares as a dependency: an `UNCOVERED` family record
*is* a registered grammar scope with a completeness statement attached —
exactly what `M2-RANK-OR-LASSO` needs before any ranking/lasso search is
meaningful. The ledger neither performs nor presupposes that search.

---

## 7. Interface separations (nothing crosses these)

1. **`G2-PSC`.** The ledger consumes the T7 entry menu as an input with its
   own trust tag; pole/branch/deck/chart fields are opaque tokens. A
   complete ledger at every `td` would still say nothing about transporting
   a GGV packet into Sigray decorations, and no ledger certificate may be
   cited in a `G2-PSC` argument or vice versa. The pure-Sigray backbone
   bypasses `G2-PSC`; the ledger is architecture-neutral on that choice.
2. **`G2-BD`.** The `lam` budget is the St 9.4 charge ledger, not a
   delay/carrier bound. `ALIVE`, `TERMINAL`, and even a complete sector
   book imply nothing about bounded delay after residue-A; conversely no
   `G2-BD` estimate may prune a ledger family.
3. **`RPMC(C)` / cofinal ceiling.** Every packet is fixed-`(td,type)`. The
   ledger asserts no uniformity in `td`, consumes no type menu, and its
   sector completeness must never be summed into an "all `td`" claim; the
   `DIR/PC/RPMC => KJN` chain and the type-menu obligation live entirely
   outside and may not be cited by any rule.
4. **Realizability firewall.** `ALIVE` families are conservative supersets
   (`P`-realizability untracked, exactly as the promoted engines); a
   nonempty `ALIVE` book is not evidence of a counterexample, and an empty
   one at a fixed header is not a `td`-exclusion unless every sector
   (single-pole composite included) is separately closed.
5. **Trust perimeter.** Every certificate resolves to the frozen Sigray
   trust set plus named promoted repairs; a perimeter change invalidates
   the records citing it and nothing else — the ledger is designed to be
   re-run, not re-argued.

---

## 8. Verdict and handoffs

**CONTINUE.** The instrument works at design tier: the schema needed no
field beyond the declared additions to express everything the hand-run met;
the classifier's cap-to-`UNCOVERED` rule converted a flagged engine cap
into the sector's single open family; and the run produced a new, checkable
mathematical observation (`dp | dq` across the whole `eps_q` family,
matching the td-7 zero-chain dead-pattern) that a prose audit had not
surfaced. Recommended sequence: (1) build LL-1 against A1-A5; (2) send the
`eps_q` zero-chain-law extension to the named-lemma queue (one page,
instance-checkable, closes the only `UNCOVERED` row of the sector);
(3) only then LL-2 at `td=7`, where the off-axis machinery and the H5a
conditionality enter. Stop condition inherited from Card B: one bounded
pass per packet; if a packet's `UNCOVERED` list exceeds a few dozen
families without structural compression, freeze and report its shape — that
outcome is the measurement, not a failure.

---
Report-body self-hash (sha256 of every byte above this line): 83fe23123f35275e551ef8d1704da1181dea9c346a4915cd0e15c6db82998700
