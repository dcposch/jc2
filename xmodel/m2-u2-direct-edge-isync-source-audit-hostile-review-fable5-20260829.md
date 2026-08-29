# Hostile delta review — direct nested-U2 i-sync/source certificate (Fable 5)

Date: 2026-08-29  
Reviewer: Fable 5, adversarial delta review of Fable P1 (prior direct-nested-U2
review repair)  
Target: `xmodel/m2-u2-direct-edge-isync-source-audit-sol56-20260829.md`  
Target full SHA-256:
`59fd30425df7bf4e9138c56b2d4ba4247d0c35f2ddeb409bc09b5cb6c7c45a0f` (verified)  
Target body SHA-256:
`6c24091eecb78fe82b664794421fb8e1685c60394d807ed21d2866d16b38f0f2` (verified;
convention reproduced: all bytes through the final content line's newline,
excluding the blank line and `---` separator; 11827 of 11966 bytes)

## Verdict

**PASS_WITH_REPAIR.**

The certificate's central delta claim is CONFIRMED on the reopened printed
pages: Proposition 9.3's printed proof derives `n in N*` and equation (d)
with no `i`-normalization, so for an actual direct inner-U2-to-outer-U2 edge
the integer anchor `n_e = nu_H*kbar_O - kbar_H in N*` is printed-tier
independent of the full-degree identity, and my prior P1 sentence ("`n_e`'s
integrality rides on the i-normalization") was too strong at printed-lemma
tier. The full-degree chain (3.17) -> (DEG) -> (IS) is literal and carries no
chain/leaf/M=1 premise. The perimeter (actual adjacent vertices only; no
stage-R row promotion) is correctly drawn and implementation-verified at
schema scope.

One repair is required (T1): the certificate silently omits the standing
domain hypothesis `O, H in V_a ∩ T_a^searrow` carried by every printed
statement it chains except Statement 3.17. The hypothesis is dischargeable at
promoted tier (MP0), so the certified conclusion survives unchanged, but a
source audit whose whole value is "the literal printed chain" must print the
literal printed hypotheses. Two precision notes (N1, N2) and one sharpening
of the missing-lemma statement (N3) are attached.

## 0. Provenance and custody re-verification

- Target full and body SHA-256: reproduced exactly (above).
- All eight custody hashes in target Section 1 reproduced byte-exactly:
  prior P1 review full `5cf66cd0...0142d7` / body `0fcd5675...12ec3d5`;
  reviewed R1 target `99bbe233...92912b`; `refs/sigray_full.pdf`
  `9bf9f032...1623ae`; `ladder/BOOK-OFFAXIS.md` `7679db8a...667f77`;
  `ladder/SHEET6-DEPTH.md` `ad9ced6c...71036d`; lex-primary producer
  `9c20947b...667613` and its review `e156f94c...440740`;
  `cases/book_offaxis.py` `c22e3a1f...042ebc`.
- Printed pages reopened from `refs/sigray_full.pdf` (printed page =
  physical page, confirmed on every page used): pp. 13-14 (Not 3.9-3.13,
  St 3.7-3.8, Not 3.12, Prop 3.1), pp. 17-18 (St 3.15-3.18, Prop 3.2),
  p. 28 text layer (Not 6.1, St 6.1-6.2), pp. 39-40 (Not 8.1, St 8.1,
  Prop 8.1 + proof), p. 42 (St 8.4 + proof, St 8.5), pp. 50-51 (Prop 9.2,
  Prop 9.3 + proof, St 9.6). Equation-bearing pages were read as rendered
  images, not `pdftotext -layout`, so the stacked-fraction inversion trap
  does not apply; the Prop 9.3(c),(d) fractions were read off the print
  with `nu_G` in the denominator of the whole sum.

## 1. Charge 1 — O/H orientation: CONFIRMED

Reopened literally:

- Prop 3.2 (printed p. 18): for `F in V_a \ {(0,x),(0,y)}` and `G := F°`,
  the notation `F := G + c` is defined. Child on the left.
- St 3.17 (printed p. 18): "Set F, G in V_a. Assume F = G + c"; (i)
  `deg(p_F) = mult(p_G, c)`. Child on the left; outer vertex is `G`.
- Prop 9.3 (printed p. 50): "Let F, G in V_a ∩ T_a^searrow such that
  G = F + c". Child is `G`; outer vertex is `F`. Letters opposite to
  St 3.17, exactly as the target's Section 2 table states.
- BOOK R2.1 (`ladder/BOOK-OFFAXIS.md` §7): merge `G` with arriving edges
  `H_e -> G`, `mu_e = mult(p_G^red, c_e)`. Outer vertex is `G`.
- St 8.4 (printed p. 42, used but not tabled by the target): "Set
  F, G in V_a ∩ T_a^searrow. Assume G = F + c"; conclusion
  `mult(p, c) | M_G` in Prop 8.1's notations at the parent `F`. Child is
  `G` — same orientation as Prop 9.3; the target's use (`mu_e | M_H`,
  divisor constraint on the arriving child's `M`) is the correct reading.

The target's dictionary (audit `O`/`H` = R2.1 `G`/`H_e` = 9.3 `F`/`G` =
3.17 `G`/`F`) is exact. The warning that the letter `G` flips roles between
R2.1/3.17 and 9.3 is real and was necessary. In (d)/(NE) the divisor `nu`
is the arriving child's (`nu_G` in 9.3 = `nu_H` in audit notation) —
verified on print; consistent with the prior review's W1 form
`kbar_out = (kbar_in + n)/nu_in`.

N2 (nit): the target's Section 2 cites "Proposition 3.2 and Statement 3.17,
printed pp. 17-18"; both are on printed p. 18 (p. 17 carries St 3.15/3.16).
Harmless; no formula is affected.

## 2. Charge 2 — the literal full-degree chain: CONFIRMED, with unstated
## standing hypothesis (repair T1)

Every link reopened:

1. `p_F` is the full pattern. Not 3.10 (p. 13) defines
   `h_F^+(xi,eta) = xi^{j/kappa} p_j(eta)` (largest nonvanishing index) and
   `p_{h,F} := p_j`; Not 3.13 (p. 16 region) sets `p_F := p_{f,F}`. So
   St 3.17(i)'s polynomials are the full leading eta-polynomials; the
   target's `^full` annotation is faithful.
2. St 3.17(i) hypotheses are exactly `F, G in V_a`, `F = G + c`, `c in C`.
   No chain-only, leaf-only, or `M=1` premise as printed; the statement
   applies verbatim when the child is itself an inner merge. Substitution
   `F = H`, `G = O` gives `deg(p_H^full) = mult(p_O^full, c)`.
3. Prop 8.1 (pp. 39-40): `i := deg(p_F)/M*_F in N*`; (i) gives
   `(xi^delta p(eta))^i = ⊖ f_F^+(xi,eta)` and the proof line
   `deg(p) = deg(p_F)/i = M*_F`. Matching eta-parts against
   `f_F^+ = xi^{d_F} p_F(eta)` (Not 3.10/3.13) forces
   `p_F^full = ⊖ (p^red)^i` as polynomials, hence
   `mult(p_O^full, c) = i_O * mult(p_O^red, c)` for every `c` (a fortiori
   the nonzero U2 direction). With BOOK R2's printed definition
   `mu_e = mult(p_O^red, c_e)`: **(DEG)** `deg(p_H^full) = i_O*mu_e`.
   Confirmed.
4. Applying Prop 8.1(i) at `H`: `deg(p_H^full) = i_H*dp_H`, so **(IS)**
   `i_H*dp_H = i_O*mu_e`. For an actual edge this is an identity between
   already-defined quantities (one full degree computed two ways), exactly
   as the target says. Confirmed.
5. Divisibility side: St 8.4 (p. 42) gives `mu_e | M_H` (verbatim, no
   `M=1` hypothesis); Prop 8.1(v) gives `M_H = gcd(dp_H, dq_H)`, so
   `mu_e | dp_H` and the target's solvability/lcm remark is correct
   arithmetic. The target's honesty framing (numerical solvability is not
   index assignment; census tuples acquire no indices) is correct and
   important.
6. The target's claim that SHEET6-DEPTH §1 records the same two-source
   chain but with an `M=1` rider is accurate: that sheet derives
   `deg(p_child^full) = i_parent*mu_e` generally and only then specializes
   `mu_e = 1` on `M=1` ancestry. The target's derivation is genuinely
   scope-free of that rider.

**T1 (the repair).** The target asserts domain membership only for
St 3.17 ("Both U2 merge vertices are in the displayed domain" — true for
`V_a`). But the other three chained statements carry a standing hypothesis
the target never prints: Prop 8.1 requires `F in T_a^searrow`, and St 8.4
and Prop 9.3 require `F, G in V_a ∩ T_a^searrow`, where (Not 6.1, printed
§6) `T_a^searrow = {F in T_a^+ : d_F < (1-pi(F))*deg(p_F)}` (St 6.1:
dichotomy with `T_a^nearrow`). Discharge exists at promoted tier and is
`M`-free: MP0 (SHEET6-MULTIPOLE, review-confirmed) is the equality
`T_a^searrow ∩ V_a \ {(0,x),(0,y)} = U \ {(0,y)}` for the configuration
tree `U`; its D1 proof anchors to the printed Prop 8.4 proof line (p. 45,
"From Propositions 6.7 and 6.8 ... F_0,...,F_n in T_a^searrow", from any
pole; poles themselves by Prop 5.3(iv)-(v) + St 3.16). Hence every actual
adjacent pair `O, H` in a configuration satisfies the hypothesis. Repair:
add one sentence stating the standing hypothesis and its MP0/p. 45
discharge. Note this also strengthens the target's own Section 6: an
abstract stage-R row lacks the `T_a^searrow ∩ V_a` typing datum as well,
so instantiating Prop 9.3 on a census row is blocked for typing reasons
too, not only for missing degrees/`i`.

## 3. Charge 3 — Prop 9.3 states `n_e in N*` independently: CONFIRMED
## (this is the delta's core, and it stands)

Reopened print, p. 50: after the four-case classification — case (I) being
literally "`F in V_{2,a} \ V_{1,a}`", a condition on the OUTER vertex,
matching the U2 outer merge under the review-confirmed regime — the
proposition states: "In particular, via Proposition 8.1, in the cases (I)
and (II), there exists `n in N*` such that: (a) `u = v - n/kappa_G`; (b)
`deg(p)/deg(q) = (D_G + n deg(p_G))/(i(kappa_G(1-v)+n))`; (c)
`D_F = (D_G + n deg(p_G))/nu_G`; (d)
`kappa_F(1-pi(F)) = ((1-pi(G))kappa_G + n)/nu_G`."

Reopened proof, p. 51: "Property (a) is a consequence of the definition of
`V_a`." — `n := kappa_G(v-u) in N*` with no `i` and no full degree. Then
(c) from (a) + St 3.17(ii) + `kappa_F = kappa_G/nu_G`, and (d) from (a) +
`kappa_F = kappa_G/nu_G` alone; both displayed derivations re-checked by
hand. The statement's "via Proposition 8.1" preamble is exercised only by
(b), whose very notation (`deg(p)`, `deg(q)`, `i`) is Prop 8.1's.

Consequences, all confirmed:

- Writing `kbar_V = kappa_V(1-pi(V))`, (d) is verbatim
  **(NE)** `kbar_O = (kbar_H + n_e)/nu_H`, and `n_e in N*` is part of the
  proposition's conclusion for any actual adjacent pair in its domain. No
  `i`-normalization and no full degree enter. At `nu_H = 1` (U2 inner
  arrival, Not 3.4, review-confirmed): `n_e = kbar_O - kbar_H in N*`.
- Therefore my prior P1 sentence — that `n_e`'s integrality "rides on the
  i-normalization `deg(p_{H_e}) = i_G*mu_e`" — is refuted at printed tier
  by the printed proof. The target's correction is right. What survives of
  P1 is its policy half, which the target keeps: stage-R rows cannot
  instantiate 9.3 at all (no configuration, no typing, no degrees), so
  BOOK-OFFAXIS §10 rider (ii) ("`n_e in N*` and i-sync are never used to
  kill") correctly remains in force for census consumers.
- Companion X handshake rebuilt independently: divide (c) by `i_O`; with
  (DEG) `deg(p_H^full) = i_O*mu_e` and `rho_H = D_H/deg(p_H^full)`,
  `X_O := D_O/i_O = mu_e(rho_H + n_e)/nu_H`; eliminating `n_e` by (NE)
  gives `X_O = mu_e(kbar_O - w_H)` with `w_H = (kbar_H - rho_H)/nu_H`.
  Exact match with BOOK R2.1's printed transcription. The handshake — and
  only the handshake — consumes the degree identity, as the target says.

N1 (precision note, not repair-grade): because the printed preamble
attaches "via Proposition 8.1" to the whole block (a)-(d), a hostile
re-reader could contest the word "independently". The target's sentences
are literally true as written (the proposition itself states
`n_e in N*`; consumers may cite conclusions of proved propositions), but
the bulletproof citation is the proof line "Property (a) is a consequence
of the definition of `V_a`" plus the (d) derivation, which confine the
8.1-dependence to (b). Recommend adding that one proof-line citation.

The residual bridge inventory for an actual direct edge is therefore:
`V_a ∩ T_a^searrow` typing (T1; MP0-discharged), case-(I) classification
(printed case condition on the outer vertex; review-confirmed U2 regime),
and `nu_H = 1` (Not 3.4; review-confirmed). No unproved normalization
bridge remains. For an abstract census row nothing is discharged — the
target's perimeter, now with typing as an additional blocker.

## 4. Charge 4 — direct merge-to-merge grammar: CONFIRMED (permission,
## not realization)

Prop 3.2 (p. 18) defines `F = G + c` for every `F in V_a` except the two
roots, with `G = F°` — adjacency is the predecessor map, unclassified.
St 3.18 (p. 18) ties children to roots of `p_F`; St 3.16 (p. 17) is an
iff: merge (more than one child direction) exactly when `p_F` has more
than one root. No printed clause found (search of §§3, 6, 8, 9 plus the
campaign's DS1, which constrains only segment vertices `j >= 1` and
permits empty segments) mandates an intervening chain vertex between two
merges. The census grammar (`hierarchies`) also represents nested
`('G', ..., ('G', ...))` directly. So a direct inner-merge child is
grammatically permitted, and the target's explicit refusal to convert
permission into existence ("'Direct' remains a hypothesis of the nested
theorem, not an existence conclusion of this audit") is the correct
boundary — realization of a specified U2 pair would need landing/gluing
facts nobody has printed.

## 5. Charge 5 — perimeter and implementation at schema scope: CONFIRMED

The certificate discharges P1 only for actual adjacent vertices and
refuses the contracted stage-R "inner" tuple mapping. Inspected
`cases/book_offaxis.py` (hash above) at exactly the named schema scope:

- `hierarchies` (l. 88): nested tuples, nodes `('leaf', i)` /
  `('G', children)` only. Confirmed.
- `merge_cells` (l. 115): docstring "Conditional (hierarchy,
  mu-assignment, emitted-M) skeletons ... Returns conditional skeleton
  dicts only"; an inner `('G', ...)` child passes upward exactly one
  integer (its emitted `M` option) plus class tags. Confirmed.
- `expand2` (l. 360): `struct = ('leaf', i, mu) | ('G', children_structs,
  M_G)` — no full degree, no `i`, no terminal `nu`, no terminal `kbar`,
  no segment-length tag. Confirmed (and hence no `T_a^searrow` typing
  either — T1's strengthening).
- `stage_rp_census` (l. 683): returns `{'DEAD': 0, 'ALIVE': 0, 'OPEN': n}`
  for every row; docstring states the census "does not quotient
  last-vertex nu/kbar, full pattern degree, or partner-dependent
  mixed/full-cell families". Confirmed.

Book citations confirmed: BOOK-OFFAXIS §3 "2691 conditional merge
skeletons ... diagnostic skeletons"; §9 inner-merge arrivals "keep known
mu_e ... but unknown w_e — never used to kill" and the child-`w` formula
"composed down inter-merge segments" (so a contracted hierarchy edge can
indeed stand for an inner merge followed by a nonempty P0 segment, whose
actual outer arrival vertex is the segment endpoint — the target's
substitution hazard is real); §10 P5 non-quotient list and honesty rider
(ii); the 0 DEAD / 0 ALIVE / 2691 OPEN recount is unchanged by this
certificate. All as the target states.

## 6. Charge 6 — promotability and the smallest remaining lemma

**Promotable: YES, at actual direct-edge scope, with T1 attached.** The
direct nested-U2 finiteness theorem (as repaired by the R1 review: W1 rule
display, W2 naming) may now consume `n_e in N*` and the full R2.1
handshake on its explicitly hypothesized actual direct inner-U2-to-outer-U2
edges, at printed-lemma tier, subject to: (i) the T1 typing sentence
(MP0 discharge), (ii) R4 (`alive != existent` — no existence claim), and
(iii) the stage-R consumption bar (rider (ii)) staying in force verbatim
for any census-tier consumer. The prior P1 rider's *justification* should
be restated: not "integrality rides on i-normalization" (refuted) but
"census rows cannot instantiate Prop 9.3 at all (no configuration, no
`V_a ∩ T_a^searrow` typing, no full degrees/`i`, possible hidden positive
inter-merge segment)".

**Smallest remaining census coverage lemma:** the target's Section 7
row-to-edge refinement/coverage lemma is correctly identified and
correctly the smallest gap; no new local i-sync lemma is missing for the
zero-length class. Sharpening N3: the refinement must transport not only
the reduced patterns and enough full-degree data to verify
`deg(p_H^full) = i_O*mu_e`, but also the `V_a ∩ T_a^searrow` typing and
the last-vertex `(nu, kbar)` frame of each class representative — these
are exactly the data §10 P5 declares un-quotiented, and without them the
zero-length class cannot even state (NE)/(IS). Positive-length classes
route to a separately proved P0-terminal composition, as the target says.

## 7. Repair list

- **T1 (required):** print the standing hypothesis
  `O, H in V_a ∩ T_a^searrow` for Prop 8.1 / St 8.4 / Prop 9.3, with its
  discharge for actual configurations (MP0; printed anchor Prop 8.4 proof
  p. 45 via Props 6.7/6.8, poles by Prop 5.3(iv)-(v) + St 3.16), and add
  the typing datum to Section 6's list of what census rows lack.
- **N1 (recommended):** cite the p. 51 proof lines ("Property (a) is a
  consequence of the definition of `V_a`"; (d) from (a) +
  `kappa_F = kappa_G/nu_G`) when claiming independence from
  `i`-normalization, since the printed statement's preamble says "via
  Proposition 8.1" for the whole (a)-(d) block.
- **N2 (nit):** Prop 3.2 and St 3.17 are both on printed p. 18.
- **N3 (recommended):** sharpen the Section 7 lemma to transport typing
  and last-vertex `(nu, kbar)` frame data (see §6 above).

None of these alters the certified conclusion; hence PASS_WITH_REPAIR,
not REPAIR_REQUIRED.

## 8. Execution disclosure

Shell used only for SHA-256 hashing, byte-slice seal verification,
`pdftotext` text-layer greps, and file reads within
`/Users/dc/code/math/jc2`. Equation-bearing PDF pages were read as
rendered images (stacked-fraction safe). No web, AWS, heavy computation,
canonical edit, source/prompt/adapter edit, commit, or push. `jc2-lean`
not entered; no `ideation-20260829T0820Z-*` file read.

---

Report-body SHA-256 (all bytes before the separator line above):
`e25e06aa2e87e330ddefc9273cced89454c3b07a647efc50a65c11aa81869b38`.
