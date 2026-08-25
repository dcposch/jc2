# Hostile review: AS D7 divided-Frobenius erratum and corrected Q11/Q10 censuses

**Reviewer: hostile different-model session (Claude), 2026-08-25.  All
producer bytes treated as immutable; nothing edited except this file.**

## 0. Session constraints and evidence basis

This review session had no shell: no Bash, no local execution, no hash
recomputation.  Every SHA-256 statement below is therefore a *textual*
cross-consistency check between frozen files, not an independent digest
computation, and the frozen AWS outputs are trusted as transported bytes
under their manifests.  The verify scripts
(`verify_frozen_result.sh`, `verify_frozen_results.sh`), which locally
re-hash the remote trees and byte-compare a re-run of the lightweight
aggregate, were read line-by-line but not executed here.  All mathematics
below was re-derived by hand from the frozen sources, independently of the
producer's replay.

Read in full: the three charged reports; every file of
`cases/as_fonly_d7_next_top_carry_frobenius_erratum_20260825/` including the
remote tree; registrations, compilers, aggregators, launchers, manifests,
freezes, aggregate outputs, launch/deployment metadata, check logs, and
representative shard outputs (00, 26) of
`cases/as_fonly_d7_vertical_next_top_corrected_shards_20260825/` and
`cases/as_fonly_d7_vertical_next_top10_corrected_shards_20260825/`; and the
pinned predecessors
`generate_degree10_gate.py`, `generate_corrected.py`,
`audit_full_e1_degree7.py`, `audit_full_c5_source.py`,
`compile_full_c5_gate.py`, `audit_next_cartier_source.py`,
`compile_next_cartier.py`, `compile_next_top_carry.py`, the old shard
compiler and its frozen aggregate/shard outputs and freeze.

Charged hashes: all nine appear verbatim and mutually consistently across
the freezes and reports (erratum report `1129f2c9…` cited identically in
five places; erratum result manifest `a9bc1277…`; erratum freeze
`e2339110…` cited by the Q11 result freeze; Q11 report `4d9cebda…`,
result manifest `a9a73b2d…`, freeze `7f06a1b9…` cited by both Q10 freezes;
Q10 report `b636b00a…`, result manifest `7ee3ae60…`).  The Q10 freeze hash
`e73b854b…` is terminal (nothing downstream cites it yet) and could not be
recomputed in this session.

## 1. Full integer determinant filtration (re-derived)

With `P=x-x^3+3U+9C+27W`, `Q=y+3V+9D+27Z`, `A=U_x-x^2`, direct expansion of
`P_xQ_y-P_yQ_x-1` gives, term by term,

```text
3(A+V_y) + 9(AV_y-U_yV_x + C_x+D_y)
 + 27(AD_y+C_xV_y-U_yD_x-C_yV_x + W_x+Z_y)
 + 81({C,D} + AZ_y+W_xV_y-U_yZ_x-W_yV_x)
 + 243(C_xZ_y+W_xD_y-C_yZ_x-W_yD_x) + 729{W,Z},
```

confirming the erratum's (3)-(4) exactly, including the sign and placement
of every one of `L,K,M,N,T,S`.  The gate chain is L≡0, then
`E=L/3+K+C_x+D_y≡0`, then `F=E1+M+W_x+Z_y≡0` (mod 3, coefficientwise), and
the fourth residual is `F1+N+T+3S+9{W,Z}`, so the next residual mod 3 is
exactly `F1+N+T` — (5)-(6) confirmed.  Both divided carries are exactly as
claimed: `M`'s single-Frobenius part `MF={UF,D}+{C,VF}` is identically
divisible by 3 (every term carries a `UF`/`VF` derivative), so it vanishes
in `F mod 3` and reappears as `MF/3` in `F1`; `K`'s double-Frobenius part
`Kdouble={UF,VF}` is identically divisible by 9, enters `E1` as
`Kdouble/3`, vanishes in `F mod 3`, and reappears as `Kdouble/9` in `F1`.

That the predecessor really imposes all three gates was checked against the
frozen chain: L-rows at degrees 2–4 (`generate_degree10_gate.py` base
rows; `L mod 3` has degree ≤ 4 in the charged normal form, and I verified
by hand that `L` is *formally* divisible by 3 there, e.g. the `x^3`
coefficient is `8t+t=9t`); E-rows at degrees 6 (`k6` pivots), 5
(`accepted5` with the Frobenius `L5`), 4 (`accepted4`, whose (2,2)
coefficient is asserted identically zero), plus the divergence-absorbable
remainder; F-rows at degrees 9–8 (`Rfull=Mfull+KFdiv`), 7
(`audit_full_e1_degree7.py` proves the full degree-7 `E1` is exactly
`Ksingle/3`, and `full_c5` adds the C5/D5 cross `M5`), and the (2,2)
Cartier row `F22`, with the frozen next-Cartier freeze certifying that
every compatible point admits a cap-seven next digit (so the divergence
absorbs the rest of `F`).  Degrees 5–9 of `F` are beyond `W_x+Z_y`'s reach
only at 7–9, and exactly those are imposed.  The chain is complete; `F1`
exists on every visible state.

## 2. The divided terms, their coefficients, and completeness at 12/11/10

Hand recomputation over Z with `UF=fua·y^6+fa·x^3y^3+fb·x^6`,
`VF=fc·y^6+fd·x^3y^3+fvb·x^6`:

- `UF_x/3 = fa·x^2y^3+2fb·x^5`, `UF_y/3 = 2fua·y^5+fa·x^3y^2`,
  `VF_x/3 = fd·x^2y^3+2fvb·x^5`, `VF_y/3 = 2fc·y^5+fd·x^3y^2` — these match
  `UFx3/UFy3/VFx3/VFy3` in the corrected Q11 compiler, `ufx3/…` in the
  frozen predecessor `generate_corrected.py`, and the erratum replay, with
  identical orientation (`bracket(l,r)=l_x r_y − l_y r_x` throughout, both
  divided terms entering with plus signs, same as `N`).
- `{UF,VF}/9 mod 3` recomputed by hand:
  `(2fa·fc−2fua·fd)x^2y^8+(4fb·fc−4fua·fvb)x^5y^5+(2fb·fd−2fa·fvb)x^8y^2 ≡
  (2fa·fc+fua·fd)x^2y^8+(fb·fc+2fua·fvb)x^5y^5+(2fb·fd+fa·fvb)x^8y^2` —
  identical to erratum (8), to `expected_kdouble` in the replay, and to the
  Q10 compiler's `Kdoubleq` assert.
- Controls recomputed: `UF=x^6, D7=y^7` gives `42/3=14≡2` at `x^5y^6`
  (total degree 11); `UF=x^6, VF=y^6` gives `(6·6)/9=4≡1` at `x^5y^5`
  (total degree 10).  Both nonzero, exactly as frozen.
- Bidegree support: `MF7/3` occupies all 12 degree-11 bidegrees (shape 12
  ✓); `MF6/3` occupies exactly the 8 bidegrees with x-exponent in
  {0,1,3,4,6,7,9,10} (shape 8 ✓), i.e. it misses exactly (2,8),(5,5),(8,2).

Exhaustive sweep for any further divided Frobenius term at degrees 12, 11,
10: `T mod 3` has degree ≤ 9 (`A mod 3` and `V0` derivatives have degree
≤ 3; `W,Z` capped at 7); `M0` ≤ 9; `W_x+Z_y` ≤ 6; `K_singleF/3` ≤ 8;
`L/3` ≤ 5; carries from the pointwise gate divisions are confined to
degrees ≤ 9 because at degree ≥ 10 every integer coefficient of `E` and
`F` is *identically* divisible (Kdouble by 9, MF by 3) — no canonical
representative enters.  Hence at degree 12 the row is exactly
`N12={C7,D7}`; at 11 exactly `Q11=(1)`; at 10 exactly `Q10=(2)`.  No
further term exists.  The vertical normal form has no degree-3 or degree-5
first-digit Frobenius layer (`u3_0,u3_3,v3_0,v3_3` absent, `u5,v5` zeroed),
and even generically such layers could reach only degree ≤ 8 here.

One statement in the erratum deserved special hostility and survives with a
proof: "these are exactly the three derivative-cokernel bidegrees missing
from the pure `N10` derivative row."  Since
`{F,G}=∂_x(F·G_y)−∂_y(F·G_x)`, every bracket is a divergence, and a
divergence's coefficient at a bidegree `(a,b)` with `a≡b≡2 (mod 3)` is
`(a+1)w+(b+1)z≡0`; so `{C7,D5}+{C6,D6}+{C5,D7}` vanishes identically at
(2,8),(5,5),(8,2) (I confirmed the (2,8) cancellation of `{C7,D5}`
monomial-by-monomial), `MF6/3` also misses them, and `{UF,VF}/9` lives
*only* there.  The three degree-10 Cartier rows of the corrected residual
are therefore pure first-digit Frobenius quadrics — a genuinely new source
term that no pure-bracket runner could ever have seen.

## 3. Preservation/quarantine boundary

- The corrected compilers consume the old shard only as a pinned
  *definition prefix* (split before `shard_count`, SHA `64bbd0e1…` pinned
  in-code and in both source closures) and re-enumerate `N12` from scratch;
  the aggregates fail closed on `N12=629115` and `visible=1085103`.  The
  only old-shard *datum* that survives is the N12 row/count, exactly as
  licensed.
- Old `602343` and `439108047=729·602343` (arithmetic checked) remain
  wrong-source diagnostics: the old aggregate is untouched, its freeze
  still records them, and no corrected file consumes them.  Quantified
  delta from the frozen histograms: the corrected row moves exactly four
  bases from fibre 81 to 0 and the unique giant base from 531441 to
  190269; `4·81+(531441−190269)=341496=602343−260847` reconciles exactly.
  At shard 26 the corrected Q11 stream SHA equals the old N11 stream SHA
  (identical survivor sets there); at shard 00 only the giant base moved.
- No earlier full-C5 or first-Cartier count depended on the retracted
  bound.  The retracted claim was about `F1=F/3` (fourth residual); the
  predecessor gates live in `L`, `E`, `F` mod 3, whose visible degree
  really is ≤ 9, and their divided single-Frobenius content at degrees
  ≤ 9 (`L5`, `KFdiv`, `E1_7=Ksingle/3`) was already constructed over Z in
  the frozen predecessors — `audit_full_e1_degree7.py` proves the entire
  degree-7 `E1` equals `Ksingle/3` formally.  The bound was load-bearing
  only in the two quarantined top-carry interpretations (old degree-11
  census; stopped pure degree-10 runner).

## 4. Compilers against the frozen predecessor system

- Exec-prefix chain: Q10 shard → corrected Q11 shard (SHA `349ea509…`
  pinned in-code, in both runner manifests, closures, and freezes) → old
  shard (`64bbd0e1…`) → `compile_next_top_carry.py` (`1fc18eeb…`) →
  runpy of `compile_next_cartier.py` → `compile_full_c5_gate.py` →
  `generate_corrected.py` → `generate_degree10_gate.py`.  Every link's
  expected SHA in code equals the closure manifests; the remote
  `source_closure_check.log` shows `OK` for all files on both runs, and
  the Q10 run additionally replayed the erratum source before launch,
  reproducing output SHA `51473096…` byte-identically
  (`source_erratum_replay.out` equals the erratum's frozen `replay.out`
  line-for-line), with `verified_utc` preceding `launch_utc` in
  `deployment.meta`.
- State reconstruction: the state is 7 structural (`Pp,Qq,Rr,Tt,s,w,h`,
  3^7=2187 bases), 6 Frobenius (`fua,fa,fb,fc,fd,fvb` — exactly the
  variables of `UFx3/…`, so the divided terms bind to the enumerated
  values), and 17 unknowns (`d7_1,d7_4,d7_7,d6_1,d6_4`, all of `c5_*`,
  `d5_*`).  `rref_source`/`affine_solutions` were checked by hand: pivots
  only in the unknown block, compatibility on the zero-A rows, back-
  substitution sign correct; the per-base count `3^(6+17−c)` matches the
  literal enumeration that the frozen predecessors dual-checked per base.
  All three runs reproduce `visible=1,085,103`, matching the frozen
  next-Cartier count (20×17 gate, F22 = `c5_3+d5_2+2h^2`).
- Coefficients: twelve Q11 rows (`len(Q11)==12` asserted; MF7/3 alone
  covers all 12 bidegrees) and eleven Q10 rows (`len(Q10)==11` asserted
  with an explicit homogeneity assert; N10+MF6/3 cover 8, `{UF,VF}/9` the
  3 Cartier bidegrees).  `Q10`'s `Kdoubleq` as an F3 product of the
  already-divided derivatives equals `{UF,VF}/9 mod 3` because the
  integer divisions are exact termwise.
- Spectator omission: the base arithmetic (`generate_degree10_gate.py`)
  normalizes mod 3 in every operation and drops derivative exponents
  ≡ 0 (mod 3), so the six current-digit directions
  `c6_0,c6_3,c6_6,d6_0,d6_3,d6_6` can only enter via the `sub6` pivot
  solutions, which I verified are spectator-free (the spectator columns of
  the degree-5 rows carry coefficients 6,3,3,6 ≡ 0).  The compilers assert
  spectator-freeness of N12/N11/Q11/Q10 rows, the full-C5 gate asserts the
  whole system's support lies in state∪spectator-free names, and
  `eval_expr` raises `KeyError` on any name outside the assignment — a
  fail-loud guarantee that every passing run evaluated rows supported
  exactly on the stored state.  Hence the spectators are constrained by
  nothing tested and the completion factor is exactly `3^6=729`
  (all `729·count` products checked by hand).
- Canonical-carry / state-sufficiency search: at degrees 12–10 the divided
  coefficients are identically divisible integer forms, so their mod-3
  values depend only on the state mod 3; the `W,Z`-dependent and
  representative-dependent carries in `F1` and `T` are confined to degrees
  ≤ 9.  No hidden canonical-carry assumption is present at the tested
  degrees — and the packages correctly refuse degree nine, where exactly
  such carry provenance and a state-sufficiency proof would be required.

## 5. Partition, aggregation, certificates, metadata

- Partition: `start=2187·i/27=81i`, contiguous, disjoint, covering;
  aggregates assert `start==previous_stop`, final stop `3^7`, per-shard
  index/count, PASS tails, and (Q10) all three predecessor controls.
  Failure of any shard breaks the PASS tail or `overall_rc`, and the
  launcher then skips or fails the aggregate (rc 125) — fail-closed.
- Totals re-derived from frozen data (not from PASS): every aggregate
  histogram hand-sums to its total — N12: `Σ fibre·mult = 629,115` over
  2,187 bases; Q11: `260,847`; Q10: `33,225`; `2187−2028=159` Q10-live
  bases; shard-level spot checks (00: 599,427/256,203/30,969; 26:
  438/60/27) reproduce their own histograms and the `·729` lines.
- Cross-run agreement: shard-for-shard, the Q10 run's N12 and Q11 stream
  SHA-256 digests equal the Q11 run's (checked at shards 00 and 26), and
  the Q10 aggregate re-derives 1085103/629115/260847 independently of the
  Q11 run's files.  As charged, this is parallel agreement within one
  implementation lineage plus the separate erratum replay for the
  universal forms; the only fully independent engine here is this review's
  hand algebra, which confirms the forms.
- Certificates: aggregate outputs list all 27 leaf SHAs (each equal to the
  transported shard-output SHA in the remote manifests — checked
  entry-by-entry for both runs), and the Merkle roots `7a281804…` (Q11)
  and `def726e4…` (Q10) match reports and freezes.  The Merkle
  construction (leaf = H("leaf"‖index‖payload-SHA), odd-node duplication)
  was read and is deterministic; roots not recomputed here (no shell).
- Metadata: launch/deployment metas match the reports' tags, host, UTC
  windows, and archive SHAs (`ad285e6e…`, `7d8811ea…`); every `.err` and
  `launch.log` carries the canonical empty-file SHA `e3b0c442…` and the
  ones read are empty; rc files read show rc 0; `shard_00.time` shows
  2:13.68 / 20,804 kB, matching the Q11 report's "longest shard" and
  "~21 MB" claims; runner-manifest and source-closure check logs show all
  `OK`.  Remote manifests cover every file in both trees, including the
  check logs and the Q10 pre-launch erratum replay.

## 6. Scope audit

The three packages claim, and their artifacts support, exactly: the
corrected source rows (1)-(2) with nonzero controls; survival counts
`629,115`, `260,847`, `33,225` through source-corrected degrees 12, 11, 10
of the next residual on the frozen 1,085,103-state predecessor; and
`24,221,025=729·33,225` (and `190,157,463=729·260,847`) as pure
current-digit Frobenius spectator completions.  Survival is nested
(N12 ⊇ Q11 ⊇ Q10 filters, verified in the shard control flow).  Degree
nine (quotient residual plus first-/next-digit cross, with its open carry
provenance and state-sufficiency gate), lower rows, later Cartier tests,
recurrence, all-depth lifting, characteristic-zero algebraization,
counterexamples, and JC2 are all explicitly left open in the reports,
preregistrations, and freezes; nothing read overreaches that scope.

## Promotable sentences

**Erratum.** Over the integers the determinant filtration of the AS F-only
`D=7` vertical branch gives, on the accepted full-C5/first-Cartier
predecessor, the next residual `F1+N+T mod 3`, whose degree-12 row is
unchanged `N12={C7,D7}` and whose full degree-11 and degree-10 rows are
`Q11={C7,D6}+{C6,D7}+({UF,D7}+{C7,VF})/3` and
`Q10={C7,D5}+{C6,D6}+{C5,D7}+({UF,D6}+{C6,VF})/3+{UF,VF}/9`, with nonzero
universal controls `2x^5y^6` and `x^5y^5`, so the old pure-bracket
degree-11 census `602343/439108047` and the stopped pure degree-10 runner
are wrong-source diagnostics while the `N12` row and count `629115` are
unaffected.

**Corrected Q11.** On the frozen 1,085,103 visible predecessor states,
exactly 629,115 satisfy `N12={C7,D7}=0` and exactly 260,847 of those also
satisfy the source-corrected
`Q11={C7,D6}+{C6,D7}+({UF,D7}+{C7,VF})/3=0`, giving exactly
`729·260847=190,157,463` current-digit degree-six Frobenius spectator
completions; this count supersedes the quarantined 602,343 and licenses
only survival through corrected degrees 12 and 11.

**Corrected Q10.** Of the 260,847 corrected-Q11 survivors, exactly 33,225
also satisfy the source-corrected
`Q10={C7,D5}+{C6,D6}+{C5,D7}+({UF,D6}+{C6,VF})/3+{UF,VF}/9=0`, spread over
159 of the 2,187 structural bases, giving exactly `729·33225=24,221,025`
spectator completions; the row is a strong shrink, not a finite
obstruction, and degree nine and below remain open.

## Smallest gap

No false row, count, source assumption, or custody defect was found.  The
smallest genuine custody gaps, all disclosed or inherent: (i) the three
censuses share one implementation lineage (the erratum replay and this
review's hand algebra are the only independent checks of the row forms,
and only the review is independent of the producer); (ii) this session
could not recompute any SHA-256 or run the frozen verify scripts, so byte
custody rests on the internally consistent hash lattice; (iii) the `N12=
629115` control still awaits the separately promised monolithic
stream-hash agreement; (iv) the Q10 result-freeze hash `e73b854b…` is
terminal and uncorroborated by any downstream file yet.  None of these
touches the mathematics or the stated counts.

CONFIRMED
