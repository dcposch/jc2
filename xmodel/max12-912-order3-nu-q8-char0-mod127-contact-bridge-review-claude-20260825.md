# Hostile review — selected-Q8 characteristic-zero/mod-127 full-contact bridge

| Field | Value |
|---|---|
| Report under review | `xmodel/max12-912-order3-nu-q8-char0-mod127-contact-bridge-20260825.md` (`39ae6229…`) |
| Case under review | `cases/max12_912_order3_nu_q8_char0_mod127_contact_bridge_aws_20260825/` (MANIFEST `d7abdade…`, FREEZE `e9744c64…`, tag `q8_char0_mod127_contact_bridge_r6d_v2`) |
| Pinned dependencies audited | quotient compiler `22b0cdc4…`, local series `5e3e3d86…`, full-contact source `08a3d227…`, frozen full-contact result `804f9fbb…`; transitively `order3_fibre.py` `a4fdac5d…`, descent replay `5dcb0a67…`, jet replay `5536f16a…` |
| Reviewed context read in full | gap audit (char0-specialization-scheme-gap), no-merger erratum (repaired lemma), global-quotient gate + its CONFIRMED review, formal branch + its CONFIRMED review, normalization jet CONFIRMED review, galois primitivity + infinity passport + their joint CONFIRMED review, sparse-contact component lemma, p127 factorization, p127 full-contact endpoint |
| Overall verdict | **CONFIRMED** at the registered arithmetic-local scope (no false identity; two one-line presentational precisions and one custody note, all non-blocking; execution disclosure in section 1) |
| Reviewer / model | Claude (Fable 5, Anthropic); different model family from the producer |
| Constraint compliance | no producer, case, manifest, or ledger byte edited; only this file written into the repo; one verification script staged at `/tmp/q8_char0_mod127_contact_bridge_review_checks_20260825.sh` for a future shell-bearing session |

## 1. Execution disclosure (mandatory)

This review session has no shell (no Bash/Monitor). I could not recompute any
SHA-256, rerun `producer.py`/`independent_replay.py`, or recompute the exact
`8 x 8` determinant, the six characteristic-zero row residuals, or the
`Q8bar`-squarefreeness/quintic-irreducibility gcds. The verdict rests on
three legs: (i) complete source reading of every charged byte and every
pinned dependency on the live import chain; (ii) hand re-derivation of every
hand-checkable identity, inventoried in section 11 (this includes one full
row reduced coefficient-by-coefficient, one full coordinate reduced
coefficient-by-coefficient, two full contact-formula identities multiplied
out mod 127, a support census of all twelve row blocks, the multiplicative
norm lattice, and the determinant's nonvanishing at all three rational
contacts); and (iii) the frozen fail-closed attestations (`rc=0` with
fatal-raise structure verified by reading, plus the hash lattice of section
2). The frozen-trusted computational residue is inventoried in section 11.
Residual byte checks for a shelled session are staged in `/tmp` and listed
in section 13.

## 2. Consumed bytes and hash lattice (audit by reading)

- Report `39ae6229…` = MANIFEST line 1 = review-prompt pin.
- MANIFEST `d7abdade…` = FREEZE.md display = prompt pin. FREEZE hash
  `e9744c64…` appears only in the prompt (newest artifact; nothing in-repo
  pins it yet — unverifiable by reading, disclosed).
- Report section 5 pins = MANIFEST lines 3–5, 9–10 = remote `source.sha256`
  and `output.sha256` line-for-line (`producer.py 8360bed8…`,
  `independent_replay.py fc58a2d4…`, `run_remote.sh 3d9afa57…`,
  `producer.json a07c9523…`, `replay.json 40aebed2…`). Remote bytes = local
  bytes.
- The three rc files share one digest `9a271f2a…` — consistent with each
  containing exactly `0`; all three read `0`.
- Producer PINS cross-attested in-repo: compiler `22b0cdc4…` appears
  identically in the probe MANIFEST, the full-contact MANIFEST, and frozen
  `result.json:compiler_sha256` (four sites); `5e3e3d86…` in the probe
  MANIFEST; `08a3d227…` and `804f9fbb…` in the full-contact MANIFEST.
- Report timing/RSS claims equal the stderr `time -v` blocks exactly
  (7.48 s / 26,652 KiB producer; 9.42 s / 25,612 KiB replay; both
  `Exit status: 0`); both stderr streams contain only timing lines,
  satisfying the README acceptance term.
- Row fingerprints: report `Q 6088819a…` = payload `source_rows_Q_sha256`;
  report `F127 4a085f47…` = payload `source_rows_F127_sha256` = the
  replay's independently recomputed `source_rows_F127_sha256`.

Every hash relation checkable by reading is consistent; none conflicts.

## 3. Charge 1 — six sparse rows, denominators, reduction identity, redundant rows

**Denominators.** `canonical_row_q` calls `fraction_mod_checked` on every
scalar of all six rows and raises on any denominator divisible by 127; the
replay's `canonical_row_mod` re-raises independently on the payload entries;
`rc=0` twice. Hand check: all ten `e1` scalars have denominators in
`{3,9,27}`, and I reduced all ten by hand — `4/9→71`, `4/3→86`, `−4/27→61`,
`−8/9→112`, `−4/9→56` — matching the payload's `F127` block entry-for-entry.

**Support census.** By exact line arithmetic on the pretty-printed payload
(13n+1 lines per exact block, 12n+1 per reduced block), the six rows have
exactly 10, 16, 20, 29, 35, 57 entries for `e1,e2,e3,e4,e5,e7` in **both**
the `Q` and `F127` blocks — equal to the reviewed gate's frozen table
(10/20/35/57/16/29; 167 imposed monomials) and to the sparse-contact
lemma's sizes. Q-and-F127 support equality also shows no scalar collapsed
mod 127: the reduction is support-preserving here.

**Reduction to the full-contact source.** The frozen endpoint compiles its
rows from the same pinned compiler bytes (`22b0cdc4…`, enforced inside
`load_compiler`) and reduces the same `Fraction` scalars with the same
`fraction_mod` map at evaluation time, so coefficientwise reduction identity
is forced by byte identity plus determinism; the producer additionally
checks the two pinned entry points emit identical exact rows (fatal on
mismatch), and the replay recomputes the reduced rows and their fingerprint
from the payload's exact entries. The endpoint never materializes reduced
row bytes, so "byte-identical" is discharged at the strongest available
tier: same pinned source bytes, same deterministic map, fresh-rerun dict
equality against the frozen result.

**Redundant rows.** The manifest rows are exactly `v*x5-x3+2*x5` and
`inv*x5*(x3-2*x5)-1` (payload list, replay-enforced; identical strings in
the endpoint's `source_chart` and the gap audit's display). By hand: the
`inv` row makes `x5` and `x3-2*x5` units on `Y`; then `v=(x3-2*x5)/x5` and
`inv=(x5*(x3-2*x5))^(-1)` are graphs, and eliminating `(v,inv)` is a
coordinate-ring isomorphism onto the seven-variable localization at
`x5*(x3-2*x5)`. They impose nothing beyond the localization. Verified as
advertised.

## 4. Charge 2 — localization order

The producer's localizer is `x5*(x3-2*x5)` (code line 213), `w` is not a
factor, the payload flags `localizer_does_not_invert_w: true`, and the
replay fails closed on both the flag and the row list. Note the contrast
with the compiler's own Singular helper (`inv*w*x5*(x3-2*x5)-1`) and the
reviewed gate's punctured presentation (3.1): those invert `w`; the bridge
deliberately does not.

**Generic `w!=0` open = reviewed punctured quotient.** `Y ⊗ Q` localized
additionally at `w` inverts the multiplicative set generated by
`w*x5*(x3-2*x5)` — exactly the gate's (3.1) localization of the same
byte-identical six rows — and eliminating the graph pair `(v,inv)` (the
gate adjoined the inverse of `w*x5*(x3-2*x5)` instead; both present the
same open subscheme of the six-row `Q`-scheme) recovers the reviewed
punctured quotient. That object is CONFIRMED at review tier.

**Correct contact closure.** The marked contacts have `w=0`: the producer
evaluates at `bases=[0,c,d2,d4,x1,x3,x5]` and the frozen section is a
`w=0` section. Inverting `w` would therefore delete every marked contact —
the gap audit's "main trap", avoided. Inverting `x5*(x3-2*x5)` removes
nothing near the contacts because both factors are units there (frozen
records; my hand norm lattice, section 11), and — decisively — localizing
at a function that is a unit at a point does not change the local ring at
that point, so the closure geometry `Y` presents at each contact is that of
the plain six-row scheme. The `R[[w]]` completion (charge 6) then makes
`w` a nonzerodivisor in a complete local domain, so the punctured locus is
dense in each contact germ and the contacts lie in the closure of the
reviewed punctured branch. This is the correct — and the smallest correct —
contact closure.

## 5. Charge 3 — monic normalization, finite étale, splitting DVR

**Monic normalization.** The pinned jet replay sets
`MODULUS = (−1/999)·Q8` with `Q8` the display octic of the reviewed
erratum/primitivity lineage (leading `−999`, integer vector equal to the
negation of `full_contact.py`'s `Q8_Z`). Hand: `999=27·37 ≡ 110 (mod 127)`
is a unit; every monic denominator `{333,27,111,37}` is a 127-unit; the
producer's serialized exact monic coefficients equal `Q8_Z/999`
coefficient-for-coefficient (all nine reduced by hand); and the monic
reduction equals `Q8bar=[106,122,106,126,72,61,60,29,1]` by two independent
hand routes (from the exact rationals via `333^{-1}=82` etc., and from
`Q8_Z mod 127` scaled by `110^{-1}=112`). The producer's fatal
`modulus_reduction == F.Q8` check passed at `rc=0`.

**Finite étale.** Monic degree eight makes `Z_(127)[v]/(Q8m)` free of rank
eight; étaleness at 127 is equivalent to `Q8bar` squarefree, which is
machine-attested twice (producer and endpoint, `gcd(Q8bar,Q8bar')=[1]`) and
independently implied by the frozen factorization artifact:
`Q8bar=(v+60)(v−58)(v−26)·(irreducible quintic)`. I hand-verified that 58,
26, and 67(=−60) are actual roots of `Q8bar` (all three sums ≡ 0 mod 127)
and are pairwise distinct; distinctness of the remaining five and their
disjointness from the linears follow from the quintic's (machine-attested)
irreducibility. Characteristic-zero separability follows from the reviewed
irreducibility of `Q8` over `Q` (Rabin at 7).

**Splitting DVR.** Two sound readings, both licensed by the lineage. The
complete reading — which harmonizes every sentence of the report — takes
`R = W(F_{127^5})`, the unramified quintic extension of the complete
`Z_127`: finite, unramified, Henselian; `Q8bar` splits into eight simple
roots over `F_{127^5}` (residue pattern `1+1+1+5`), and Hensel lifts each
to a unique integral root of the monic `Q8m` with the eight reductions
pairwise distinct. The algebraic reading localizes the integral closure of
`Z_(127)` in the splitting field of `Q8` at a prime over 127: unramified
because the discriminant is a 127-unit; the eight roots are integral
(monic) hence in `R`; root differences are units by squarefree reduction,
so `R[v]/(Q8m) ≅ R^8` by CRT. Either way the advertised eight integral
characteristic-zero roots with distinct reductions exist. The report's
"Hensel" wording presumes the Henselian/complete reading over the literal
non-Henselian `Z_(127)`; the gap audit's parenthetical "(and, if desired, a
further strict henselian/complete DVR base change)" already licenses it —
one-line precision, non-blocking (section 12).

## 6. Charge 4 — contact formulas, `3 x 3` solve, units, residuals, reduction, no wrong slice

**Formulas.** The producer's `x5=−36v²(3v²+3v+1)/(3v²−2)`, `x3=x5(v+2)`,
`x1=x5(v+1)+x5²(3v+1)/(9v)` are byte-identical to the pinned reviewed
`local_series.py` (lines 288–292) and to the frozen endpoint's correct
branch (`correct_x1_factor: "3*v+1 over 9*v"`).

**No Q12/wrong-`x1` slice.** The producer never constructs the quarantined
factor. The frozen endpoint constructs the wrong slice `x5²/(27v)`
explicitly and **proves it fails**: `old_wrong_x1_residuals` are all
nonzero in the frozen result (e.g. `e1=[17,26,98,109,40,67,111,64]`), with
a fatal assert had they vanished. The pin set contains no Q12-era artifact.

**Hand-verified contact identities mod 127.** (i) `v·x5` multiplied out and
reduced by hand equals `[23,73,91,54,24,95,46,123]`, which is exactly the
frozen `x3−2x5` record — verifying the `v`-relation at the section; adding
`2·x5` reproduces the frozen `x3=[25,82,94,42,15,10,35,101]` exactly.
(ii) `x5·D` multiplied out by hand equals `[0,0,91,19,19] = −36v²·A2`,
verifying the `x5` formula at the section. (iii) The full exact→mod-127
reduction of all eight `x5` coefficients (`25^{-1}=61`, `100^{-1}=47`)
reproduces `[1,68,65,121,59,21,58,116]` — simultaneously checking the
producer's reduction arithmetic and the frozen section value.

**`3 x 3` normal solve.** Rows 3,5,7 at `w=0` are affine-linear in
`(c,d2,d4)` with a fatal nonlinearity check (consistent with the `e1`
block structure: the sole `c·d4²` monomial carries `w`). The normal
determinant record `[33,52,125,109,75,23,39,99]`, norm 24, required-unit,
is byte-equal between producer and frozen endpoint; uniqueness of the
solution forces the producer's Gaussian `J.solve` and the endpoint's
Cramer solve to agree, and the `(c,d2,d4)` reductions match the frozen
section byte-for-byte.

**Residuals.** All six divided rows, the `v` row, and the localizer row
vanish exactly in `Q[v]/(Q8)` — fail-closed raises with a correct
`NF.__bool__` zero test (read and verified; a wrong truthiness would have
raised on the residual check and broken `rc=0`). The `v` and `inv` rows
vanish by construction (`x3−2x5=v·x5` identically; `pinverse` raises on a
non-coprime input). Mirrored mod 127 by the frozen endpoint's independent
`F127` implementation.

**Unit lattice (hand).** `norm(v)=Q8bar(0)=106`; `norm(9v)=9⁸·106=33`;
`norm(x5)=36⁸·norm(v)²·norm(A2)/norm(D)=30·60·77·19^{-1}=29`;
`norm(x3−2x5)=norm(v)·norm(x5)=26`; `norm(localizer)=29·26=119` — all five
equal the frozen records, a five-way multiplicative consistency check of
the recorded unit values. `gcd(Q8bar,D)=1` and `gcd(Q8bar,A2)=1` verified
by hand (reduce `Q8bar` mod the quadratic: `110v+4` resp. `30v+15`, and
check the induced root is not a root of the quadratic).

**Coordinatewise reduction.** All eight coordinate vectors in the payload's
`contact_coordinates_F127` are byte-equal to the frozen
`contact_coordinates_low_to_high` (compared value-by-value); the replay
re-derives them independently from the exact rationals (own `reduce_exact`)
and against a **fresh** rerun of the frozen endpoint with `fresh == frozen`
dict equality — any drift anywhere in the chain fails closed.

## 7. Charge 5 — the full relative `8 x 8` determinant

**Presentation identity.** Producer and endpoint build the same matrix:
rows `(e1,e3,e5,e7,e2,e4, localizer-row, v-row)`, columns
`(c,d2,d4,x1,x3,x5,inv,v)` — verified line-by-line in both sources; both
frozen `columns` lists agree. Hand-checked partials: localizer row
`(0,0,0,0, inv·x5, inv·(x3−4x5), x5(x3−2x5), 0)`; `v` row
`(0,0,0,0, −1, v+2, 0, x5)`; the six source rows have zero `inv`/`v`
columns because the rows do not involve them. No row/column/sign mismatch
is possible at the comparison: the equality is value-level on identical
orderings.

**Structure (hand).** The `(inv,v)` columns vanish on the six source rows,
so Laplace on the last two columns gives, with positive sign,
`det(full) = det(S₆ₓ₆) · x5² · (x3−2x5)` — the full determinant is a unit
iff the six-row source Jacobian determinant is, and
`norm(det) = norm(det S)·29²·26 = norm(det S)·22`, consistent with the
frozen `88 = 4·22`.

**Value.** The reduction `[101,42,36,116,8,110,107,14]` is byte-equal in
three places produced by three distinct implementations: the producer's
`NF`-field Gaussian elimination with sign tracking, the endpoint's `F127`
permutation expansion (8! terms — the source of the ~8 s runtimes), and
the replay's independent rational re-reduction of the eight exact
coefficients. `gcd` one with `Q8bar` and norm 88 are machine-attested; by
hand I evaluated the reduced determinant at all three rational contacts:
`det̄(58)=27`, `det̄(26)=104`, `det̄(67)=61`, all nonzero — the unit claim
is hand-verified at the three `F_127`-rational contacts and rests on the
frozen gcd/norm only for the five quintic-conjugate contacts.

## 8. Charge 6 — arithmetic formal implicit-function conclusion

**Why `R[[w]]`, precisely.** Write `Y_R = Spec R[w,y]/(f₁,…,f₈)` with `y`
the eight internal coordinates and `R` the (complete reading) splitting
DVR. The 127-integral contact section `a ∈ R⁸` satisfies `f(0,a)=0` (six
residuals plus two graph rows, section 6), and `J=∂f/∂y(0,a)` has
determinant a unit of `R` at each root: its reduction is the frozen unit
(gcd one with `Q8bar` ⇒ nonvanishing at every `v̄ᵢ`). Formal IFT in the
`w`-adic topology then solves a unique `y(w) ∈ R[[w]]⁸` with `y(0)=a` —
each series coefficient is obtained by inverting the same unit matrix `J`
against polynomial data in `R`, so the coefficients lie in `R` itself, no
completion of `R` being needed for the series. The completion of `Y_R`
along the section ideal `(w, y−a)` is `R[[w]]` (the map
`(w,y−a) ↦ (w,f)` is a formal automorphism because `J` is invertible), and
with `R` complete this is the completed local ring at the marked closed
point. Fibrewise: `R[[w]]/(127) = k[[w]]` literally; and the completed
local rings of the two **fibre schemes** at the marked points are `K[[w]]`
and `k[[w]]` by the same IFT over the respective fields (`det ≠ 0` in `K`
since its reduction is nonzero; `det̄` a unit over any residue extension
since gcd is geometric). One precision (non-blocking, section 12): the
report's apposition "with generic and special fibres `K[[w]]` and
`k[[w]]`" must be read as the gap audit writes it — fibre **completions** —
not as `R[[w]]⊗_R K`, which is the strictly smaller bounded-denominator
subring of `K[[w]]`. Every consuming statement (erratum items 5/6) uses
the fibre-completion or `R`-section form, both true as proven.

**Why the selected branch is the generic branch.** Over the field
`E=Q[v]/(Q8)` (a field by reviewed irreducibility) the six divided rows
with `w` a parameter have a **unique** formal solution with the given
constant terms: each degree is solved by the same unit `6 x 6` constant
matrix `S` (the pinned `local_series` recursion is exactly this Newton
scheme, and its degree-`d` finite-difference matrix equals `S` for every
`d`); `det S ≠ 0` follows from the hand factorization
`det(full)=det(S)·x5²(x3−2x5)` with the left side and both cofactors
units. The constant terms of the reviewed branch and the producer's
contact coincide because both solve the same unit `3 x 3` normal system at
`w=0`. The `R[[w]]` solution base-changed to `K` solves the same system
with the same constant term, so uniqueness identifies it with the reviewed
selected branch. Hence the generic branch of the arithmetic completion
**is** the reviewed characteristic-zero selected branch, and the reviewed
`E[[w]]` object of the CONFIRMED gate review is its `E`-form.

**127 versus `t²=w`.** Adjoining `t` with `t²=w` embeds `R[[w]] ⊂ R[[t]]`:
a degree-two extension ramified only in the branch-parameter direction,
recovering the reviewed non-parity branch in pre-quotient coefficient
space (`a₀=t·unit`, odd coordinates odd in `t`). The coefficient DVR `R`
is untouched: 127 remains the uniformizer, `R[[t]]/(127)=k[[t]]`, and the
arithmetic extension `R/Z_(127)` stays unramified. The report's
distinction is exactly right; no 127-ramification is smuggled in.

## 9. Charge 7 — source-scheme identity for primitivity and infinity

The consumers' objects, from their reviewed texts: the primitivity theorem
groups the eight contacts by geometric irreducible components of the
`Q`-defined six-row divided quotient scheme, with uniqueness of the
component through each contact supplied by the gate review's `Ô ≅ E[[w]]`;
the infinity theorem's `C_Q8` is that same unique component; the
sparse-contact lemma's mod-127 source is "the six-row divided
approximate-cubic source … chart `x5*(x3−2*x5) ≠ 0`, `v=(x3−2*x5)/x5`";
the full-contact endpoint declares the identical chart and its scope says
"independent of plane `H_v`".

Verified from the pinned rows and graph/localizer presentation, never from
`H`: (1) `Y ⊗ Q` after eliminating `(v,inv)` is the gate's six-row
characteristic-zero quotient localized at `x5(x3−2x5)` — byte-identical
rows via the four-way-attested compiler pin, and the localization does not
change local rings or the set of components **through the contacts**
(units there; a component through a contact cannot lie in the removed
locus). (2) Its `w≠0` open is the reviewed reversible punctured parity
quotient (gate section 2, reviewed), and the scheme-theoretic closure in
`Y ⊗ Q` restores the eight `w=0` contacts (charge-6 density plus the
integral section: the closure of the characteristic-zero contact point —
the generic point of the section `Spec R → Y_R` — contains the mod-127
point). (3) `Y ⊗ F_127` is presentation-identical to the sparse lemma's
and the endpoint's full localized source — same rows, same localizer, `v`
as graph variable versus defined function on the same open. (4) Component
labels in primitivity/infinity/no-merger therefore all denote geometric
irreducible components of base changes of this one displayed `Z_(127)`
scheme — the plane projection `H(w,v)` enters nowhere in this package.
This discharges the gap audit's item-7 manifest at exactly its four
required points.

## 10. Charge 8 — scope

Checked byte-level in report sections 1 and 6, FREEZE's strict exclusions,
the README, the producer payload's `scope` and `conclusion` strings, and
the replay's `scope` string: the package claims **no** mod-127 degree one,
**no** all-eight component grouping (explicitly: "It does not prove that
the eight mod-127 points lie on one global component"), **no**
characteristic-zero no-merger without that separate grouping input (the
report's section 6 is doubly conditional — on the separate seeded/generic
route **and** on the repaired no-merger lemma, which itself remains
review-charged and is consumed here only as a checklist target, not as a
theorem), **no** Taylor/trajectory realization, **no** maximum twelve, and
**no** JC2. The positive claims are exactly the proven ones: integrality,
coordinatewise reduction, source identity, unit determinant, `R[[w]]`,
closure containment, and special-fibre unibranch regularity at the
contacts ("one regular local branch in every dimension" is the correct
local-to-global consequence of `Ô_{Y_k,q_i} ≅ k[[w]]`: the local ring
injects into a domain, so exactly one component of any dimension passes
through each contact). The failed V1 launch is disclosed as a negative
custody control, absent from the manifest, and not consumed.

## 11. Hand-verification inventory and frozen-trusted residue

Hand-verified in this session (all mod-127 arithmetic done twice where
sums were involved): `Q8bar` from both the exact monic rationals and
`Q8_Z·112`; monic = `Q8_Z/999` at all nine coefficients;
`Q8bar(58)=Q8bar(26)=Q8bar(67)=0`; supports 10/16/20/29/35/57 in all
twelve row blocks by line census; all ten `e1` scalar reductions; all
eight `x5` coordinate reductions; the full products `v·x5 = x3−2x5` and
`x5·D = −36v²A2`; `x3 = v·x5+2·x5` against the frozen section; the
inverse table `37^{-1}=103, 27^{-1}=80, 111^{-1}=119, 333^{-1}=82,
25^{-1}=61, 100^{-1}=47, 9^{-1}=113, 3^{-1}=85, 19^{-1}=107, 110^{-1}=112`;
the norm lattice `106/33/29/26/119`; `gcd(Q8bar,D)=gcd(Q8bar,A2)=1`;
`det̄(58)=27, det̄(26)=104, det̄(67)=61`; the block-triangular determinant
factorization and both graph-row partial-derivative rows; the
`12n+1`/`13n+1` payload line arithmetic; the rc-file digest coincidence;
timing/RSS equality with the report.

Frozen-trusted residue (machine-attested only, disclosed): every SHA-256;
the six exact characteristic-zero residual vanishings and the exact values
of `c,d2,d4,x1,inv` beyond their reduction spot-checks; `Q8bar`
squarefreeness gcd and the quintic's irreducibility; the exact `6 x 6` and
`8 x 8` determinant values; `gcd(det̄,Q8bar)=1` beyond the three rational
roots; norms 88, 24, 19, 77 (the last two participate in the hand-derived
consistency `norm(x5)=29`); the two-entry-point row dict equality; the
replay's fresh-versus-frozen full-contact dict equality.

## 12. Non-blocking notes (none blocks the registered scope)

1. **Fibre phrasing.** Report section 1's "with generic and special fibres
   `K[[w]]` and `k[[w]]`" should say fibre *completions* (as the gap audit
   does); `R[[w]]⊗_R K ⊊ K[[w]]`. All operative statements are already in
   the correct form.
2. **Hensel over `Z_(127)`.** Section 3's "Hensel gives eight … roots"
   presumes the Henselian/complete splitting DVR; state the complete
   reading (`W(F_{127^5})`) or the splitting-field integral-closure
   construction in one line. Under the complete reading, "finite unramified
   splitting DVR" and the section-1 completion statement are both literal.
3. **Custody.** `shared_faber_probe.py` (`69f9e12c…`) is hash-pinned only
   inside `order3_fibre.py`'s `main()`, not on the library import path the
   producer and replay actually execute (`load_shared()` is pin-free). The
   effective guard is real but dynamic: any row-affecting drift breaks the
   replay's fresh-versus-frozen dict equality and the support census. A
   successor should add the static pin to `quotient_compiler.load_parent`.
4. **"Two independent entry points"** (report section 2) are two pinned
   import paths of the *same* compiler bytes — a consistency control, not
   implementation diversity. Genuine diversity exists where it matters, at
   the reduction/determinant layer (three implementations, section 7).
5. FREEZE hash `e9744c64…` is prompt-only for now (newest artifact).

## 13. Residual byte checks for a shell-bearing session

Staged at `/tmp/q8_char0_mod127_contact_bridge_review_checks_20260825.sh`:
`shasum -a 256 -c` on the bridge MANIFEST; the MANIFEST/FREEZE/report
hashes against the prompt pins; the four producer PINS; the
`shared_faber_probe.py` library pin (note 3). The two replays
(`producer.py | diff producer.json`; `independent_replay.py … | diff
replay.json`) are substantive and belong on an allowed remote worker per
the standing AWS-only policy. A failure of any of these would reopen this
review; every relation checkable by reading is already consistent.

## 14. Smallest failing identity or missing hypothesis

None found. The two candidates closest to the line are the fibre-completion
phrasing and the Henselian reading of the splitting DVR (notes 1–2); both
are one-line precisions whose corrected forms are already the ones every
consumer uses, so neither invalidates a consumed statement. The bridge
discharges the gap audit's item-6 certificate (integral contact plus
arithmetic implicit-function unit) and item-7 manifest (exact row/localizer
/base-change identity) at the boundary-local tier, exactly as registered:
the global degree-one/all-contact grouping gate, the no-merger lemma's own
review, Taylor realization, maximum twelve, and JC2 all remain open and are
all correctly declared open.

CONFIRMED
