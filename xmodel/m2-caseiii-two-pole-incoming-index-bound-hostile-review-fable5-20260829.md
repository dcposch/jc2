# Hostile review: two-pole case-III "incoming-index" bound (sol56)

Reviewer: Fable 5 (different-model hostile review). Date: 2026-08-29 UTC.
Target: `xmodel/m2-caseiii-two-pole-incoming-index-bound-sol56-20260829.md`
(full SHA-256 `406e78d2…f46` verified; body `8a16cad9…b43` verified) and
packet `cases/m2_caseiii_two_pole_nuh_bound_r1_20260829/` (all three file
hashes and the charged-JSON hash `12a3f6b7…037` verified; ordinary and
`-O` tests both pass with exactly 130,095 checks, ~0.5 s each; no CAS ran).
Sources consulted in full: `ladder/BOOK-OFFAXIS.md` (§§6–11a),
`ladder/SHEET6-DEPTH.md` (§5c–5d), `ladder/SHEET6-MULTIPOLE.md` (MP2),
`cases/book_offaxis.py` (`solve_arr`, `cell_check`, `NUCAP`),
`xmodel/sol-h5a.md`, `xmodel/grok-h5a-review.md`, and
`xmodel/m2-budget-quotient-primary-research-opus5-20260829.md` (for the
charged notation adjudication only). Independent scripts and four staged
mutations were run from `/tmp/tpb_review/` (bounded exact-rational Python
only); the packet and producer report were not modified.

## VERDICT: `REPAIR_REQUIRED`

The merge-degree arithmetic is correct, new, and sharp exactly as claimed —
I verified every step by hand and by an independent 6,346,105-cell sweep on
a box strictly larger than the packet's, with zero violations. But the
theorem's headline object is wrong at the promoted tier: its case-III
handshake `X = mu0*(kbar - h*w0)` with `h = nu_H` is the printed
Prop 9.3(g),(h) reading, which the promoted H5a resolution
(`xmodel/sol-h5a.md` Props 1–2, hostile-reviewed SOUND in
`xmodel/grok-h5a-review.md`, promoted in `BOOK-OFFAXIS.md` §11-PRE/§11a)
proves incoherent unless `nu_U = nu_G` (open CONJECTURE `U_7C`), and which
§11a explicitly brands "the mixed reading that corresponds to neither
Notation 3.5 value". Under the promoted Q+E5 pin the identical algebra
bounds the merge-local `nu_G` (times `w_U`), and the incoming `nu_H` is
**free** — the report's central "notation correction" against Opus5 is
therefore pointed in the wrong direction, and the claim that this theorem
licenses removing `NUCAP=500` is not supported by the literal sheet laws as
promoted today. The report nowhere mentions H5a, E5, or `U_7C`, although
the fork is stated verbatim in the very report it corrects (Opus5 §10c) and
in its own principal source file (BOOK-OFFAXIS §11a). PASS is denied on
that ground; REJECT is withheld because the difficult-regime lemma survives
the pin change intact (the `kbar` bound is reading-independent) and yields
a genuine promoted-tier theorem after a mechanical restatement.

---

## Findings, severity order

### F1 — BLOCKER. The bounded quantity is pinned by a superseded handshake; at the promoted tier the incoming index is not bounded, and is not the handshake variable at all

The theorem conditions on "the literal case-II/case-III handshakes … in
`ladder/BOOK-OFFAXIS.md` R2.1–R2.2". R2.1's case-III line
`X_G = mu0*(kbar_G - nu_e*w_e)` descends (via `SHEET6-DEPTH.md` §5c,
"equations (e)–(h)") from printed Proposition 9.3(g),(h). The promoted
record now says, of exactly that transport:

* `sol-h5a.md` Prop 1 (grok-review Finding 1, SOUND): the kappa-decoration
  at a doubly realized (case-III) vertex is forced to the Q/jump value;
  the P/coarse value contradicts printed St 3.8.
* `sol-h5a.md` Prop 2 (grok-review Finding 3, SOUND): under Q, printed
  St 3.17(ii) + Prop 9.3(e) force the E5 transport
  `kbar_F = (nu_F*kbar_G + n)/nu_G`; printed (g),(h) agree with E5 **iff**
  `nu_F = nu_G`, which is open CONJECTURE `U_7C` ("a dead hope at the
  proved tier" as a theorem). Printed (g),(h) amount to `kappa_F = kappa_G`
  — "neither presentation-value".
* `BOOK-OFFAXIS.md` §11a (promoted, census hostile-replayed): the px5:244
  pin `kbar = (mu0*nu_U*w_U - 2)/(mu0 - 1)` — the same formula
  `cases/book_offaxis.py:solve_arr:339` implements and this theorem
  generalizes — is "the mixed reading that corresponds to neither
  Notation 3.5 value"; the promoted pin is (I4)
  `kbar = (mu0*nu_G*w_U - 2)/(mu0 - 1)` "with `nu_U` free (any legal
  vertex)". The promoted 17-cell book records **infinite** legal arrival
  menus (`neutral nu ≡ -1 (mod mu0)` congruence classes) — the incoming
  index is unbounded and harmlessly so.
* `grok-h5a-review.md` Finding 5 computes all three readings on a recorded
  edge (`mu0=5, kbar=6, nu_G=13, nu_U=7, w_U=2/5`): campaign E5 `X=4`;
  "mixed handshake" `X=16` — the value this theorem's equations produce;
  printed-(h) literal `n=39`. Mutually incompatible; the campaign lives on
  E5.

i-normalizing E5 (with `deg p_U = i_G*mu0`, `w_U := (kbar_U - rho_U)/nu_U`)
gives `X_G = mu0*(kbar_G - nu_G*w_U)`: the incoming `nu_U` cancels into
`w_U`, and the elimination against the case-II partner reads
`mu0*nu_G*w_U = delta*kbar + mu*w`. I verified this identity exactly on
all 17 promoted §11a cells (script `e5_check.py`; e.g.
`(98,147,73,49)@25`: `25*73*(2/25) = 146 = 24*6 + 2`). So at the promoted
tier the theorem's elimination bounds `nu_G` given `w_U` — the
merge-local index — and there is **no** incoming-index bound, because the
incoming index no longer appears in the handshake. The headline sentence
("the incoming zero-edge index `h=nu_H` … has an explicit finite bound…
closes the mathematical reason for the old `NUCAP=500` fallback"), the
README's "must not be confused with the merge-local pattern index `nu_G`",
and the sealed certificate's `notation_correction` field all assert the
superseded side of a documented fork without naming the fork. The report's
conditionality sentence cites R2.1–R2.2 but not H5a/E5/`U_7C`; that
omission is material, because the packet's own repo proves the condition
it silently adopts to be false-unless-`U_7C`.

### F2 — MAJOR. The charged Opus adjudication is wrong in both directions

The report claims Opus5's Theorem 2.4/4 "correctly bounds … `nu_G`" and
errs only in later identifying it with `nu_H`. Neither half survives:

1. Opus's §10c states the H5a fork explicitly — "under the promoted
   E5/Q-value reading (I4) uses `nu_G`, so `nu_U` is genuinely free…
   I do not adjudicate H5a" — so Opus did not simply confuse two symbols;
   Sol's report resolves the fork silently, on the non-promoted side,
   while presenting the resolution as a notation repair.
2. Opus's clause-4 inequality `nu <= mu0*num(w_0)` is **not correct for
   `nu_G` either**. Its (4a) route applies the case-II transport
   `kbar = mu_e*w_e*dq/E_e` to the 0-edge, which matches neither recorded
   case-III reading. Under E5 the route collapses (`kbar =
   mu0*(nu_G*w_U)*dq/E_0`, and `E_0 = nu_G*|T|` makes `nu_G` cancel), and
   the face-value inequality is refuted by the promoted book itself:
   **16 of 17 §11a cells violate `nu_G <= mu0*num(w_U)`** (script output;
   e.g. `(15,25,12,5)@3`: `12 > 3`; `(21,35,17,7)@4`: `17 > 4`;
   `(98,147,73,49)@25`: `73 > 50`). Under the printed reading the
   derivable form is `nu_G <= mu0*num(nu_e*w_e)` — conditional on `nu_e`,
   not "unconditional". Opus's §7(a) restatement as an arriving-`nu_e`
   bound is likewise refuted on the promoted cells, where the mixed pin's
   required incoming index equals `nu_G` identically (my script confirms
   `h_mixed = nu_G` on all 17 — i.e. imposing the mixed pin on E5 cells
   is precisely CONJECTURE `U_7C`), e.g. `7 > 2 = 2*num(1/2)` on
   `(9,15,7,3)@2`.
3. The correct promoted-tier replacement is the one this packet's own
   algebra yields after the pin swap: `mu0*nu_G*w_U = delta*kbar + mu*w`
   with the reading-independent `kbar <= mu*w*(2*delta+3)` (F4), hence
   `nu_G <= mu*w*(delta*(2*delta+3)+1)/(mu0*w_U)` per arriving state —
   verified to hold on all 17 promoted cells.

So the "missing incoming-index bound" the report supplies is missing
because, at the promoted tier, it does not exist and is not needed; and
the `nu_G` bound the report concedes to Opus is one Opus does not soundly
possess. Both reports need the same repair: the E5 pin plus this packet's
gap lemma.

### F3 — MAJOR. The engine consequence is overdrawn even within the packet's own model

`NUCAP=500` caps the `nuH` loop in `solve_arr`'s no-pin branch
(`book_offaxis.py:334-336`), which fires whenever `zero` is a pole leaf,
all `non0` edges share `(mu,w)` with `mu >= 2 < mu0` — **regardless of
`len(non0)` and `inner_mus`**. The theorem covers only the two-pole case
(`len(non0) == 1`, no inner edges): its `kbar` bound genuinely fails
otherwise. Certified countercells (script `indep_gap.py`, all of (S),
(NE), (R) checked): two equal-`mu` nonzero arrivals + 0-edge,
`nu = delta+1`, `k=1`, `m = mu-1`, `lex = 0` give
`dq/D = 3*delta+4 > 2*delta+3` — e.g. `mu=2, mu0=3`: cell `(13,7)`,
`D=1`, ratio `7 > 5`; `mu=5, mu0=11`: `(109,22)`, ratio `22 > 15`.
`cell_check` models `r0 = len(mus_non0)` arriving orbits, so such cells
are reachable by the engine's own solver: replacing `NUCAP` wholesale in
this branch would be unsound *even under the mixed pin*. The report's
consequence paragraph does say "two-pole", but the Result section's
"closes the mathematical reason for the old `NUCAP=500` fallback in the
`mu0>mu>=2` branch of `solve_arr`" is broader than what is licensed. The
deeper point stands via F1: the loop being capped is itself an artifact of
the superseded pin — the E5-correct rebuild (`cases/td7_census_e5.py`
pattern) has no `nu_H` loop at all, so the honest fate of `NUCAP` is
removal-by-rebuild, not replacement-by-cap.

### F4 — CONFIRMED. Within its stated conditional model, every step of the mathematics checks out; the `kbar` half is reading-independent and survives promotion

Charge-1/2 reconstruction, all verified by hand and by the independent
sweep (`mu <= 7, delta <= 8, nu <= 40, k <= 4, lex <= 6`, all multiplicity
tuples; 6,346,105 `D>0` cells; zero violations):

* Pattern: for a genuine case-III merge, `nu_G >= 2` is automatic (a
  `nu_G = 1` merge is V_{2,a}\V_{1,a}, case I — R2 §7 preamble, DEPTH
  §5c), so R1.0's `eta || q` applies and
  `dp = mu0 + nu_G*(mu + Sm)`, `dq = 1 + nu_G*(1 + k + lex)` is exactly
  R2.2 with `r0 = 1`, `eps = mu0` (the 0-arrival multiplicity *is* the
  0-root multiplicity, by definition of `mu_e = mult(p_red, c_e)`).
  Q-extras simple in `nu`-orbits; the `+1` is the simple `eta` factor.
* `m_j*dq < dp < mu*dq` is licensed by R2.2(S) (strict NE for non-chain
  orbits, strict searrow for the arriving `mu`-edge; equality separately
  excluded by (R)), hence `m_j <= mu-1`; at `mu = 1`, `k = 0` is forced —
  matching §8 Step 3's independent "`k > 0` needs `dq < dp` = FALSE here".
* `D = nu*A - delta` (`A = mu*s - Sm`), `A >= k + mu*lex >= s`, `s >= 1`
  (else `D = -delta < 0`): exact.
* Gap lemma `dq/D <= 2*delta+3`: both cases verified; the boundary is
  exact (`x = ns = delta+1` gives equality in
  `(1+2x)/(x-delta) <= 2*delta+3`). Equality holds iff `n = delta+1`,
  `s = 1`, `A = 1` — i.e. `k=1, m=mu-1, lex=0` (`mu>=2`) or `k=0, lex=1`
  (`mu=1`) — and forces `D = 1`. Attained for **every** delta in the
  sweep (7 equality cells per delta in my box), not just delta=1.
* `kbar = mu*w*dq/D`: from the case-II handshake `X = mu*(kbar-w)` plus
  Prop 9.3(b) consistency. **Case II is untouched by H5a** (grok-h5a
  Finding 3: the correct denominator "is already `nu_G` by printed (c)"),
  so `kbar <= mu*w*(2*delta+3)` is a sound promoted-tier bound at every
  two-pole case-III merge under either pin. This is the salvageable core.
  It holds on all 17 promoted cells (`kbar ∈ {5,6,7} <= 2*(2*mu0+1)`).
* Elimination `mu0*h*w0 = delta*kbar + mu*w`: exact algebra — but the
  left-hand side is `mu0*(kbar_U - rho_U)` only under the mixed pin (F1);
  under E5 it is `mu0*nu_G*w_U`.
* Regimes 1–2 (`mu0<mu`: `h < mu*w/(mu0*w0)` from `kbar>0`; `mu0=mu`:
  `h*w0 = w`): exact, and identical to `solve_arr`'s already-proved
  branches (`:321-324`, `:316-319`), which do not need the pattern and so
  hold with extra same-`(mu,w)` and inner edges too. Regime 3 does not.
  No zero denominators (`D >= 1`, `mu0*w0 > 0`, case-2 denominator
  `ns - delta >= 1`); no hidden integrality (`kbar in Z` is never used);
  no literal countercell exists in scope — my sweep found none.

### F5 — Charge 4: the charged discriminator is arithmetically exact and its kill is reading-stable, but it replays a retracted section and its ray-language is mixed-pin-only

Against the td-7 record: the charged `(mu,w)=(1,2)`, `(mu0,w0)=(2,3/2)`
computation reproduces BOOK-OFFAXIS §8 Step 3 ("chain 2 at 0, mu0=2",
`kbar = 3*nu_H - 2`, `A ∈ {7,10}`, cell `(5,7)`, `M=1`, MP2-dead) exactly;
§8's own Diophantine window `A-4 | 6 => A <= 10` independently corroborates
`kbar <= 10 = mu*w*(2*delta+3)`. The `(dp,dq,kbar,X,h) = (5,7,7,5,3)`
cell and `M=gcd(5,7)=1` check; uniqueness of the `h=3` pattern is exact
(`n*(5*lex-2) = 9` forces `(n,lex) = (3,1)`); MP2 as cited
(SHEET6-MULTIPOLE MP2: interior trunk `M != 1`) kills it. Two caveats:

* §8 is a **retracted** section, and its Step-2 premise (chain-2 frozen at
  `3/2`) was refuted by the triple review and replaced by the §10 P0
  priced closure; the charged case is legitimate only as the
  `w_U = 3/2` entry-state **slice** of class C, not as "the" td-7 ray.
  The genuinely promoted td-7 source is §11a (E5), whose `mu0=2` row
  `(9,15,7,3)@2` lives on the different slice `w_U = 1/2` and is
  untouched (and unkilled) by this packet — no contradiction, but also no
  recovery of a promoted result.
* Reading-stability, verified by recomputation: under the promoted E5 pin
  the same slice gives `3*nu_G = kbar + 2 <= 12`, so `nu_G ∈ {2,3,4}`:
  `nu_G=2` → `(4,8)`, `kbar=4`, T1-dead; `nu_G=3` → the same `(5,7)`,
  `M=1`, MP2-dead; `nu_G=4` → `dq = 60/8` non-integral. The slice dies
  under both pins — but "h odd and h>=3", "odd ray leaves only h=3", and
  "every odd `h>=5` … excluded before a cell solve" are statements about
  `nu_U` and are meaningless under the promoted pin (`nu_U` free).

### F6 — Charge 5: tests are real and the constant is genuinely attained, but only on MP2-dead cells; the 130,095 checks exercise the lemma, not the scope

* Both test modes pass with 130,095 checks; all five published hashes
  reproduce (report full+body, three packet files, charged JSON).
* The gap-lemma test recomputes `dp, dq, D` inline (independent of the
  module) — a genuine theorem-level check over its box. The
  handshake-grid and elimination checks are largely self-referential:
  `h` is defined as `(kbar - X/mu0)/w0` with `X = kbar*dp/dq`, which makes
  `mu0*h*w0 == delta*kbar + mu*w` an identity by construction, and
  `pattern_certificate` `require`s the universal bound before the test
  re-asserts it. Violations would still surface (as ValueError), so the
  circularity is a transparency defect, not a soundness hole.
* Nothing in the packet can test *which* case-III handshake is the law —
  exactly where it fails (F1). The scope conditions (case-III vs case-I,
  two-pole vs `r0>=2`, leaf vs inner 0-slot) are untested; the helper
  accepts out-of-scope inputs (F7).
* Sharpness: `2*delta+3` **is** attained, for every delta (not only the
  delta=1 fixture). But every equality cell has `D = 1`, and
  `M | D` forces `M = 1`: **every sharpness witness is MP2-dead as an
  interior merge**. Restricted to `M >= 2` cells (`D >= M >= 2`),
  `dq/D <= 2 + (2*delta+1)/2`, and the empirical maxima in my box are far
  smaller (3, 3, 3, 5, 3, 4, 7, 8 for delta = 1..8). A repaired packet
  should state that the constant is sharp only at the pattern+handshake
  tier and is never realized by an MP2-surviving cell.
* Mutations (staged on copies in `/tmp/tpb_review/mut{A..D}`, packet
  untouched), all detected: gap-test constant `2d+2` →
  `CHECK_FAILED:gap-bound-4`; source `kbar_bound` `2d+2` →
  `CHECK_FAILED:high-kbar-bound`; sharpness fixture `nu 2→3` →
  `CHECK_FAILED:sharp-ratio`; source ratio-require `2d+2` →
  `ValueError: universal dq/D bound failed`. The fixture and constant are
  load-bearing in the tests.
* Nit: per-delta sharpness is asserted only globally (`equality is not
  None`), not per delta.

### F7 — Nits

1. `pattern_certificate` does not enforce the NE law `m_j*dq < dp` or the
   0-edge searrow `mu0*dq > dp`; it accepts NE-illegal tuples (harmless
   for the sup — any NE violation forces `D >= dq`, ratio `<= 1`, proven
   and swept — but the helper will emit an `h` certificate for a
   non-cell). It also accepts `nu = 1`, which is case-I territory where
   the `dq = 1 + nu*(1+s)` q-shape is unlicensed (harmless superset).
2. "Every nonchain p-root is strictly northeast: `m_j*dq < dp < mu*dq`" —
   the second inequality is the arriving edge's searrow law, not
   NE-ness; conflated phrasing.
3. The sealed certificate JSON embeds the inverted `notation_correction`
   prose; a repair must regenerate the certificate, not just the report.

---

## Charge-by-charge summary

1. **Pattern reconstruction**: licensed as claimed for genuine two-pole
   case-III cells (`nu_G >= 2` automatic; zero-root convention
   `eps = mu0` definitional; q-extras and handshake census correct);
   `m_j <= mu-1` licensed; `nu_G = 1` is out of case-III scope and its
   inclusion in the certificates is a harmless superset (F4, F7).
2. **Three regimes**: every step of the difficult regime is exact; no
   countercell in scope (6.35M-cell independent sweep); the only failures
   are *out* of scope (`r0 >= 2`, inner edges — F3). No zero denominators
   or hidden integrality (F4).
3. **`nu_G` vs `nu_H`**: at the promoted tier the theorem does **not**
   bound the incoming `nu_H` (which is free under E5) — it bounds
   `nu_G*w_U`; Opus's provisional `nu <= mu0*num(w0)` binds **neither**
   soundly (16/17 promoted cells violate it as a `nu_G` bound; the
   arriving-`nu_e` form fails likewise). The report's correction is
   inverted; the sound object is the E5 restatement in F2.3 (F1, F2).
4. **Charged conclusion**: reproduced exactly against §8 Step 3 and the
   engine formulas; `h<=4`/odd/`(5,7,7,5)`/`M=1` all check; kill is
   reading-stable, but the source replayed is retracted and the promoted
   §11a `@2` cell lives on a different, untouched slice (F5).
5. **Tests/mutations**: 130,095 both modes; hashes reproduce; gap test is
   theorem-level, handshake tests partly tautological; scope untestable;
   `2*delta+3` genuinely attained for every delta but only on `D=1`,
   `M=1` (MP2-dead) cells; all four staged mutations detected (F6).
6. **Safe engine consequence**: below.

## Exact safe engine consequence

Under this verdict, none — `NUCAP=500` and the OPEN fallback stay. For the
record:

* A repaired, E5-founded packet licenses: (i) `kbar <= mu*w*(2*delta+3)`
  at every two-pole case-III merge (promoted tier, reading-free), and
  (ii) the pin `mu0*nu_G*w_U = delta*kbar + mu*w`, bounding the
  merge-local `nu_G <= mu*w*(delta*(2*delta+3)+1)/(mu0*w_U)` per arriving
  state. The engine consequence is a rebuild of the case-III solve in the
  `td7_census_e5.py` style (no `nu_H` loop exists), with two-pole
  finiteness at fixed budget coming from the finite priced `(w_U, M_U)`
  closure times the per-state cell menu — not from any incoming-index cap.
* If the campaign instead explicitly retains the mixed pin as an
  engine-model convention (equivalently, works inside `U_7C`), the theorem
  licenses replacing `ncap = NUCAP` and OPEN-on-exhaust by
  `ncap = floor(mu*w*(delta*(2*delta+3)+1)/(mu0*w0))` and
  DEAD-on-exhaust **only** on `solve_arr` rows with `zero` a pole leaf,
  `len(non0) == 1`, `inner_mus == []`, `inner0_mu is None`,
  `mu0 > mu >= 2`, with a mixed-pin/`U_7C` conditionality tag on every
  resulting verdict. Rows with two or more same-`(mu,w)` nonzero edges or
  any inner arrival must keep the cap and OPEN fallback (certified
  countercells, F3).
* In no reading does anything here certify the legacy `cell_check`
  grammar, equal nonzero joins (`kbar` stays affine/unbounded there),
  multipole or inner-merge trees, full landing, any topological-degree
  ceiling, realizability, or JC2. The report's own firewall on these
  points is accurate.

## Repair path

R1. Re-found the theorem on the promoted Q+E5 pin: identical gap lemma,
`kbar` bound unchanged, elimination restated as
`mu0*nu_G*w_U = delta*kbar + mu*w`; regimes 1–2 become `nu_G < mu*w/(mu0*w0)`
and `nu_G = w/w0`. (All three restatements verified here on the promoted
17-cell book.) Alternatively, state the present theorem as explicitly
conditional on `U_7C`/printed-(g),(h) and withdraw the cap-removal claim.
R2. Rewrite the Opus adjudication per F2 (both directions), citing Opus
§10c's fork paragraph. R3. Regenerate the certificate JSON (F7.3). R4.
Scope the engine consequence per F3, or convert it to the E5 rebuild. R5.
Add the M=1 sharpness caveat (F6) and the NE/searrow requires (F7.1).

## Verification log

Hashes: `shasum -a 256` on the report (matches `406e78d2…`), body bytes
before the final `---` (matches `8a16cad9…`), the three packet files
(match `fdefd729…`, `3b3dd42e…`, `d9860253…`), and the regenerated charged
JSON (matches `12a3f6b7…`). Runs: `python3 test_caseiii_two_pole_bound_r1.py`
and `python3 -O …` (both `PASS checks=130095`). Independent scripts (staged
under `/tmp/tpb_review/`, not committed): `indep_gap.py` (6,346,105-cell
sweep; per-delta maxima/equality census; `M>=2` restriction; `r0=2`
countercell certification), `e5_check.py` (17-cell promoted-book
verification of the E5 identity, reading-free `kbar` bound, transplanted
`nu_G` bound, 16/17 Opus-clause-4 violations, charged-slice E5 replay),
and mutations `mutA–mutD` (all detected). No `jc2-lean` access, no
workspace-wide git commands, no network, no CAS, no canonical edits.

To verify this review's integrity: `shasum -a 256
xmodel/m2-caseiii-two-pole-incoming-index-bound-hostile-review-fable5-20260829.md`
gives the full-report hash; the body hash below covers all bytes strictly
before the final `---` separator line (recompute with
`python3 -c "import hashlib,sys; b=open(sys.argv[1],'rb').read();
print(hashlib.sha256(b[:b.rfind(b'---\n')]).hexdigest())" <file>`).

---
Review-body SHA-256 (bytes before the separator line above): `9cbb1a7cccb23ddf0db2d380932aecb7bdef140954727d4e46af34a25aefd681`
