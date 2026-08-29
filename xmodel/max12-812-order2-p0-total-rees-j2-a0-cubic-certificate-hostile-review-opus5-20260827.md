# Hostile review: candidate direct `T-a0` cubic certificate

Reviewer: Opus 5 (independent hostile review)

Date: 2026-08-27

## Verdict

**CONFIRMED** for the displayed polynomial identity, its literal-source
provenance, its `T-a0` chart typing, and the resulting emptiness theorem for
the whole registered first `J2` chart.

Two separate findings, both about the *evidence package* rather than the
identity:

- **V24's own lift is not a certificate and must not be promoted as one.**
  Its cofactors are localized at `rho` (cleared denominator
  `rho^6*(3*qa1^2*rho^2+1)`, whose `rho`-constant term is `0`), which fails
  V24's own preregistered normalization rule.  The displayed identity is a
  strictly stronger, genuinely denominator-free object that V24 did not
  return.
- **The V24 `a1_ordered` lane is vacuous at `rho=0`** (denominators are pure
  powers of `rho`, no `1+rho*W` factor).  It supplies no evidence toward the
  ordered second `J2` stratum.

While auditing, I also independently verified a **strictly stronger**
identity that removes the unit factor entirely (`A0-CERT-P`, §8): `a0^3`
itself lies in the ideal of 13 chart rows.  That upgrades the conclusion from
"empty `rho=0` fibre" to "**the whole `T-a0` chart is the zero ring**".  The
six-row identity under review is the human-checkable face of it.

Nothing here closes `V(J1+J2)`, the ordered `a1` stratum, the `k`-localizer
residuals, coverage, deck/square, Gate T, order two, maximum twelve, or JC2.

## 0. Method and what I did *not* trust

I did not use V24's PASS banner, its lift, its compiler, its `std`/`reduce`
output, the producer's reasoning, or the displayed identity as given.  I
wrote an independent restricted-AST parser and dict-of-monomials exact-`Q`
engine (no CAS), reparsed the literal hash-pinned bytes, and reproduced the
chart substitution from the *full unspecialized* source rows.  A second,
structurally different code path (direct modular evaluation, no monomial
dictionaries) supplied the finite-field replays.

Scripts are staged at `/tmp/opus5_ta0/` (`poly.py`
`26340f0f684056799825377a592ba08bf140aa1999f42a600304cf8ec04d3b25`,
`liftback.py` `8f192c797d13c8fcc50ee478af561fcce9a0d8130a0860ee21c0c344f5898dd0`,
`mutate.py` `4cfe6a33cbe83a45595b9154b649d1a6bfd421bc148bf75ad020161deace0e6e`,
`explicit_cert.py` `300356bdfe780825ebed6e960af923ca59490fe54cd43b74d5a94c9395f7535d`,
`ff_replay.py` `798bdda838f7c8a34da2565c789d6cf0aa095b303a602f0c1a9966b4dec38971`,
`v24_audit.py` `b4c84e6dcd01697885afd635318989b07ea7065a01547c57ffafcb9e4f4b643d`,
`FINAL.py` `0da0fed8c7698b0cf1ff62fcf520a7bd7cb5954be495ce159ac935234a2f3310`).
No AWS mutation, no heavy local CAS, no web.

## 1. Exact-`Q` residual and finite-field replay  (brief item 1)

With `q=qa1` and the six hash-verified `output_r1/a0_chart` rows, the
coefficientwise residual of

```text
a0^3*(1+3*q^2*rho^2)
 - (6*ell1*cs1-8*rho^2*cs2)*Tg11_1 + 2*rs2*Tg11_2 + 6*rho^2*cs1*Tg12_1
 + 2*rs1*Tg12_2 + 4*cs1*Tg12_3 + 16*Tg15_6
```

is **literally `0`** — zero monomials, exact `Fraction` arithmetic.

Independent modular replay (separate evaluator, exact modular inverses):
200 uniformly random points each at `p = 32003, 65521, 1000003, 2147483647`;
**0 mismatches** in all 800.

### The replay is demonstrably discriminating

Every mutation below produced a **nonzero** residual:

| mutation class | outcome |
|---|---|
| each of the 7 coefficients `+1`, `-1`, and sign-flipped (21 cases) | all nonzero (2–19 residual terms) |
| each of the 7 terms deleted (7 cases) | all nonzero |
| `1+3q^2rho^2` → `1+2q^2rho^2`, `1-3q^2rho^2`, `1`, `1+3q^2rho^4`, `1+3q^3rho^2` | all nonzero |
| `a0^3` → `a0^2` | nonzero |
| each cited row replaced by a sibling of the same grade (6 cases) | all nonzero (4–63 terms) |
| `cs1`↔`cs2` swap, `rs1`↔`rs2` swap, `rho^2` dropped from `G[Tg12_1]`, `rho^2`→`rho^4` in `G[Tg11_1]` | all nonzero |

In `F_65521`, each `+1` coefficient mutation is detected at **50/50** random
points, so the finite-field lane alone would have caught any of them.

## 2. Provenance, divided rows, rational-function cofactors  (item 2)

Custody, all recomputed here:

```text
V23R1 output_r1/RESULT.json  ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641
   == the pin in V24 FREEZE.sha256                                    OK
42/42 upstream source .poly files rehash to their recorded input_sha256  OK
84/84 chart-polynomial files rehash to their recorded output_sha256      OK
84/84 term counts reproduced by my independent parser                    OK
3/3 V23R1 input_manifest hashes (V9 COEFFICIENTS, V20 RESULT, V22 RESULT) OK
V24 aws_q_a0 / aws_q_a1 EVIDENCE.sha256: 18/18 and 18/18 entries verified OK
V24 compile_result.json input_sha256: 42/42 equal the V23R1 a0_chart bytes OK
```

Row-by-row source provenance of the six cited rows:

```text
Tg11_1 g11  src 11f6bd635957677cb8a0b29cedc847369d68d6b695e844efdf32f683078db469  V9  aws_q_v9/compiled/Tg11_1.poly
Tg11_2 g11  src fa9c5c109541478fc56a0a4c9564a80cbdd9aeaa2bd8a1c2eabfa5076afb1093  V9
Tg12_1 g12  src 799ccff5e54711c53da6498ac01f8ac3fae2290600fd19664238cb49ed8d6e54  V9
Tg12_2 g12  src b66a3e858c41d22b4ce3f4592cdee28664e5ba677f138860f840565625b073e6  V9
Tg12_3 g12  src b0d090f9000f6e74bd214a0c443450114994c3fd61a0a577453f8c69acc42f87  V9
Tg15_6 g15  src 786c6bb976305614cc0945b2ebf0d78600fb9a96aefa1553248ff8f473b5c51e  V22R1 aws_q_r1/compiled/Tg15_6_q.poly
```

**No divided row.**  The `Tg` rows are honest `sigma`-graded coefficients of
the emitter rows: in the frozen shard the extraction is
`Tg=subst(TQ,sigma,0); TRem=TQ-Tg; TQ=TRem/sigma`, guarded by
`if (sigma*TQ-TRem!=0) { extraction=0; }`.  That is exact division of the
ambient `sigma`-expansion, not division of a source row by a source variable
(contrast the promoted `T-rs`, whose relation list *does* contain four
divided raw rows).  Every row is independently `sigma`-homogeneous of its
grade and `rho`-even: I recomputed both for all 42 full source rows, **0
violations**.

**No rational-function cofactor remains and no unlisted row is used.**  I
constructed the *complete explicit lift in the unspecialized presentation
ring* — this is the decisive check:

```text
a0^3*(1+3*qa1^2*rho^2)
  =  (6*cs1*ell1 - 8*cs2*rho^2) * Tg11_1
   + (-2*rs2)                   * Tg11_2
   + (-6*cs1*rho^2)             * Tg12_1
   + (-2*rs1)                   * Tg12_2
   + (-4*cs1)                   * Tg12_3
   + (-16)                      * Tg15_6
   + H  * (a1 - a0*qa1)
   + rs*L_rs + cs*L_cs + c0*L_c0 + c1*L_c1
```

with **all cofactors polynomial over `Q`**: `H` 31 terms, `L_rs` 72,
`L_cs` 70, `L_c0` 11, `L_c1` 11.  Reassembly verified exactly (residual
zero).  My serialization of `(H,L_rs,L_cs,L_c0,L_c1)` hashes to
`4808bc26ae61459ee49d9c5c8b056a1235c08e8c11a977b989b19adb95f227a9`;
the two small ones are

```text
L_c0 = (9/4)a0*cs1*ell2*qa1 + 3*a0*cs2*ell1*qa1 - 3*a0*cs3*qa1*rho^2
     - (3/4)a0*rs3 - (3/4)a0^2*qa1^2 + (5/8)c0*k1 - (3/4)c1*cs3
     + (15/4)cs1^2*k*rho^2 - (3/4)cs2*e1 + (5/4)e0*k + (15/64)k*rs1^2
L_c1 = (9/4)a0*cs1*ell2 + 3*a0*cs2*ell1 - 3*a0*cs3*rho^2
     - (3/4)a0*qa1*rho^2*rs3 - (9/4)a0^2*qa1 - (5/8)c1*ell1*k
     + (5/8)c1*k1*rho^2 - (3/16)c1*rs3 + (15/8)cs1*k*rho^2*rs1
     - (3/4)cs2*e0 + (5/4)e1*k*rho^2
```

The whole certificate is `sigma`-homogeneous of weight 15: cofactor weights
are `4,4,4,3,3,3,0` against row grades `11,11,11,12,12,12,15`, and both
`a0^3` and `a0^3*qa1^2*rho^2` have weight 15 (`qa1`, `rho` are weight 0).

**What the certificate actually says.**  `-16*Tg15_6` already contributes
`a0^3(1+3*qa1^2*rho^2)` — that is exactly the reviewed pure-exceptional
vector of row 6 (`-1/16*a0^3`, `-3/16*a0^3*qa1^2*rho^2`).  The mathematical
content is that the **17 nuisance terms of `Tg15_6` lie in the ideal of the
five grade-11/12 rows** with weight `<= 4` cofactors.  The certificate is
therefore genuinely a grade-15 phenomenon: it could not exist before the
promoted V22R1 export, and it is what destroys the previously reviewed
`a0=1, J1=0` horizontal `Q[rho]` zero-section of the grade-`<=14` prefix.

## 3. Chart substitution and typing  (item 3)

I re-implemented `J1=(rs,cs,c0,c1)=0`, `a1=a0*qa1` independently and
regenerated **all 84** V23R1 chart files from the 42 full source rows: every
one matches (both `a0_chart` and `a1_ordered`).  `rs,cs,c0,c1` are literal
distinct ring variables in the frozen V8 ring declaration, disjoint from the
jets `cs1,cs2,cs3,rs1,rs2,rs3`, so killing exactly those four names is
reduction modulo `J1`, not an accidental prefix match.

The lift-back is the real typing check: forming the combination on the
**full** rows with only `a1 -> a0*qa1` leaves a 164-term residual, and
**every one of its monomials is divisible by one of `rs,cs,c0,c1`** (0
exceptions).  That is what licences the explicit `L_e` cofactors above.

Typing against the promoted staged calculus:

```text
A' = A/J1                       base of the second stage ("two J2 charts on V(J1)")
C  = A'[qa1]/((a0*qa1-a1):a0^inf)   exact chart presentation (2.3) of the obligation table
f_i = a0, N = 3                 exceptional power, absorbed free by the saturation
s   = 1                         NO genuine localizer, hence NO residual V(s)
W   = 3*qa1^2*rho               rho cofactor
z_e = rs, cs, c0, c1            base equations of the stage
```

Only `a0` is exceptional: `a1 = a0*qa1` is not an independent exceptional
coordinate, `qa1` is a free chart coordinate, and this is the *least-index*
chart, so no ordering equations are needed.  The certificate is unordered
and unlocalized.

## 4. `1+rho*W` and hidden localization  (item 4)

`1 + 3*qa1^2*rho^2 = 1 + rho*W` with `W = 3*qa1^2*rho`, a polynomial —
verified symbolically.  I checked each place a localization could hide:

- **cofactors** — all polynomial (explicit, above); no denominators anywhere;
- **`qa1`** — a new chart variable from the Rees presentation, never inverted;
- **`rho`** — appears only with nonnegative powers; the *certificate* never
  divides by it (V24's lift does; see §6);
- **`J1`** — passing to `A/J1` is the staged geometry, a closed condition;
- **`a0`** — appears only as the exceptional power `a0^3`, absorbed by the
  `(:a0^inf)` saturation, never inverted;
- **`k`, `cs`, `rs`** — no localizer at all here (`s=1`).

Note the `rho=0` face is *not* the certificate.  At `rho=0` the identity
degenerates to a clean five-row statement (`Tg12_1` and the `cs2` term drop
out):

```text
a0^3 = 6*ell1*cs1*Tg11_1 - 2*rs2*Tg11_2 - 2*rs1*Tg12_2 - 4*cs1*Tg12_3 - 16*Tg15_6   (all rows at rho=0)
```

verified exactly.  But per the promoted converse correction
(`f^N*s^m in J+(rho)` does *not* imply the multiplicative form), that face
alone would only give `a0` nilpotent modulo `rho`, **not** emptiness.  The
multiplicative `(1+rho*W)` form is essential and is what the candidate
supplies.

## 5. Does exceptional saturation close the chart?  (item 5)

**Yes, at the chart level, and with no residual stratum.**  Mapping the
explicit certificate into `C`: the six `Tg` rows die (they lie in the source
relation ideal), `a1-a0*qa1` dies, `rs,cs,c0,c1` die.  Hence

```text
a0^3 * (1 + rho*W) = 0   in C.
```

`C = A'[qa1]/((a0*qa1-a1):a0^inf)` is `a0`-torsion-free (if `a0*f = 0` then
`a0^{N+1} f in P`, so `f in (P:a0^inf)`, so `f = 0`).  Therefore
`1 + rho*W = 0` in `C`, so `1 = rho*(-W) in rho*C`, so `C/rho*C = 0`:

> the `rho=0` fibre of the **whole registered `T-a0` chart** is empty, with
> exceptional power `a0^3`, genuine localizer `s=1`, rho cofactor
> `W=3*qa1^2*rho`, and base equations `rs,cs,c0,c1`.

Using only 6 of the source rows makes the hypothesis *weaker* and the
conclusion *stronger*, so the finite-prefix scope is not a defect in this
direction.  The genuine residual dependencies are:

1. **Row provenance.** That `Tg11_1,Tg11_2,Tg12_1,Tg12_2,Tg12_3` and
   `Tg15_6` really are coefficients of vanishing emitter rows of the
   registered source.  This rests on the promoted V9/V20/V22R1 exports and
   still carries the campaign's recorded upstream total-emitter row
   provenance debt.  My work is exact *given* the bytes.
2. **`C`'s presentation.** `(2.3)` of the obligation table and the
   torsion-freeness slot of the promoted rho-unit calculus.

### Precisely what remains before any Gate-T / order-two claim

- **the ordered `a1` stratum of `J2` is open** — and V24 gives nothing there
  (§6);
- **the terminal receiver `V(J1+J2)` is open**;
- the four `J1` strata are closed only on the named unit-`k10` family and
  only on `D(k)` (`T-rs` localizer `35k`, `T-cs` `k^164`); the global
  off-family load-timing fan is open;
- generic deck/square comparison; terminal zero receiver; an effective bound
  on the decisive source grade; coverage;
- then order two, maximum twelve, JC2.

The certificate closes exactly **one of the six nodes** of the staged tree,
and it is the first `J2` node.

## 6. V24 audit  (item 6)

**Custody.** Two lanes, one per chart, different hosts
(`ip-172-30-0-186` / `ip-172-30-0-249`), same source archive
`bd0616d6c32f993aa1c994d8c3b7b81e2c065de4cd0ff8b8f50ee5c654ada40d`,
`compiler_rc=engine_rc=validator_rc=0`, all `EVIDENCE.sha256` entries
verified, `freeze_check` all OK.  The compiler does re-pin the V23R1
`RESULT.json` and parser hash and re-hash all 42 per-chart polynomials
before emitting.  Engine wall time was 0.02 s against a 14400 s cap — the
computation is trivially small, which is consistent but also means the
four-hour cap and the memory cap were never exercised.  **The two lanes are
one computation run twice, not two independent derivations.**

**The generated ideal is faithful.**  All 31 `P_Tg*` definitions in
`screen.sing` parse to exactly the hash-verified V23R1 `a0_chart` bytes; the
11 omitted rows are precisely the 11 that are literally zero on the chart.

**`degBound` warnings.**  `degBound=15` plus `option(redSB)` produced three
`// ** G is no standard basis` diagnostics.  Consequences:

- a **membership** conclusion from `reduce(f,G)==0` stays sound (`G` is a
  subset of the ideal), and the script additionally replays the lift with
  `if (replay!=0) { FAIL_LIFT_REPLAY }`.  I independently replayed both
  `LIFT.txt` files at 60 random points in `F_2147483647`: **0 mismatches**.
  V24's PASS is honest;
- a **nonmembership** conclusion would *not* be sound.  The `else` branch
  of this script is therefore unusable as written, and the negative control
  is unsound in principle.

**The negative control is structurally vacuous.**  `negative_control=a0^2`
has weighted degree 10 while every generator is homogeneous of weighted
degree 11–15, so `reduce(a0^2,G)==a0^2` holds for pure degree reasons and
can never fail.  Preregistered control 3 ("the exceptional square of weight
10 must remain unchanged") is therefore not a test.  The positive control
`reduce(P_Tg11_1,G)==0` is near-tautological (`P_Tg11_1` is generator #1),
and `V24_CONTROLS=1` is an unconditional `print`, not a computed flag.
`PASS_J2_RF_SCREEN_V24` is printed in **both** branches, so the banner means
"the screen ran", not "membership".

**The returned lift is `rho`-localized — this is the substantive defect.**
The ring is `ring R=(0,qa1,rho),(...)`, i.e. coefficient field
`Q(qa1,rho)`: **`rho` is inverted**.  (The design forced this: the compiler
rejects nonpositive `wp` weights, and `rho`, `qa1` both have sigma-weight
0.)  The `a0` lane's `LIFT.txt` has denominators
`{3*qa1^2*rho^2+1, rho^4*(3*qa1^2*rho^2+1), rho^6*(3*qa1^2*rho^2+1)}`, LCM
`rho^6*(3*qa1^2*rho^2+1)`.  Cleared, and verified exactly by me:

```text
rho^6*(1+3*qa1^2*rho^2)*a0^3
  = (224*ell1*cs1 - 128*rho^2*cs2)*Tg11_7 - 2*rho^6*rs2*Tg11_2
    - 10*rho^8*cs1*Tg12_1 - 2*rho^6*rs1*Tg12_2 + 32*rho^2*cs1*Tg12_7
    - 16*rho^6*Tg15_6.
```

Its cleared denominator has `rho`-constant term `0`, so it **fails V24's own
preregistered normalization rule** and cannot be normalized to `1+rho*W`.
V24 also used different rows (`Tg11_7`, `Tg12_7` instead of `Tg11_1`,
`Tg12_3`).  The displayed candidate is *not* a rewriting of V24's lift (the
`ell1*cs1` coefficients are 14 vs 6 after substituting
`Tg11_7 = (rho^6/16)*Tg11_1`); the producer did additional work.

**The `a1_ordered` lane is vacuous.**  Its lift has only pure `rho`-power
denominators (up to `rho^12`) and *no* `1+rho*W` factor; cleared it says
`3*rho^12*a1^3 in I`, which is empty content at `rho=0`, and it needs 12
rows rather than 6.  Both lanes' `outcome:"RATIONAL_FUNCTION_MEMBERSHIP"`
must be read as "some `rho`-power multiple lies in the ideal" and nothing
more.

**Does the discovery path create a logical dependency?**  **No.**  The
displayed identity is a finite polynomial identity over `Q` in hash-pinned
literal bytes; I verified it, its unspecialized lift, its typing, and its
homogeneity without using V24 at all.  Once verified, V24 is heuristics.
But the converse matters: **V24 must not be cited as the certificate**, and
the promotion's evidence must be the identity and the explicit lift, not
`LIFT.txt`.

## 7. Repairs

1. **Promote the displayed identity, not V24.**  Record the explicit
   unspecialized lift `(G_m, H, L_rs, L_cs, L_c0, L_c1)` as the frozen
   artifact.  Cite V24 only as discovery.
2. **Restate the V24 outcome field.**  Change both lanes' `outcome` to
   something like `RHO_POWER_MEMBERSHIP_ONLY`, and add an explicit erratum
   that the `a0` lift fails the case's own denominator rule and the `a1`
   lift is vacuous at `rho=0`.
3. **Replace the vacuous negative control.**  Any weight-10 target is
   unreducible by construction.  A sound, cheap replacement that is also the
   right test: exhibit a *point* with `rho=0`, `a0!=0` on which all
   grade-`<=14` rows vanish — the already-promoted `a0=1, J1=0` horizontal
   `Q[rho]` zero-section does exactly this, and it proves (no Groebner
   needed) that `a0^3` is **not** in the grade-`<=14` ideal.  That makes
   "grade 15 is necessary" a theorem instead of an impression.
4. **Fix the ring design if the Groebner path is ever reused.**  Keep `rho`
   and `qa1` as ring variables and use an order admitting weight-0 variables
   (e.g. `(a(w),dp)` or a `(wp(...),dp)` block) instead of pushing them into
   the coefficient field; and drop `degBound` before any nonmembership claim.
5. **Make `V24_CONTROLS` a computed flag** and print distinct terminal
   banners for the membership and nonmembership branches.
6. **Carry the row-provenance debt forward explicitly** in the promotion
   text: the theorem is conditional on the six rows being genuine vanishing
   emitter coefficients.

## 8. Strongest theorem safe to promote

### 8a. The reviewed six-row certificate

> **`T-a0` `rho=0` fibre emptiness (unordered, unlocalized).**
> Let `R` be the frozen source presentation ring, let
> `Tg11_1, Tg11_2, Tg12_1, Tg12_2, Tg12_3, Tg15_6` be the six literal
> exact-`Q` rows with the SHA-256 values listed in §2, and let
> `A = R/Q` be any quotient in which those six rows vanish.  Put
> `J1=(rs,cs,c0,c1)`, `A'=A/J1`, `J2=(a0,a1)`, and let
> `C = A'[qa1]/((a0*qa1-a1):a0^inf)` be the exact first standard Rees chart
> of `Proj Rees_{A'}(J2)`.  Then the polynomial identity
>
> ```text
> a0^3*(1+3*qa1^2*rho^2)
>   = (6*ell1*cs1-8*rho^2*cs2)*Tg11_1 - 2*rs2*Tg11_2 - 6*rho^2*cs1*Tg12_1
>     - 2*rs1*Tg12_2 - 4*cs1*Tg12_3 - 16*Tg15_6
>     + H*(a1-a0*qa1) + rs*L_rs + cs*L_cs + c0*L_c0 + c1*L_c1
> ```
>
> holds in `R[qa1]` with all cofactors polynomial over `Q`.  Consequently
> `C/rho*C = 0`: the `rho=0` fibre of the whole registered `T-a0` chart is
> **empty**, with exceptional power `a0^3`, genuine localizer `s=1`, and
> `rho` cofactor `W=3*qa1^2*rho`.  By the promoted staged rho-unit calculus,
> no DVR arc with `ord(rho)>0` and `J2*R' != 0` lifts into this chart.

Corollary worth recording separately (it is what makes grade 15 the active
ingredient): modulo the ideal generated by the five grade-11/12 rows above,
`Tg15_6 = -(1/16)*a0^3*(1+3*qa1^2*rho^2)` on the `a0` chart.

### 8b. `A0-CERT-P`: the same chart is empty outright — independently verified here

Fable5's `T-a0` design note
(`xmodel/max12-812-order2-p0-total-rees-j2-grade15-certificate-design-fable5-20260827.md`,
§2b, otherwise **unreviewed**) states a unit-free 13-row, 32-entry table for
`a0^3` itself.  It was outside my assigned candidate, but it bears directly
on "the strongest theorem safe to promote", so I verified §2b — and only
§2b — to the same standard as §§1–5:

```text
exact-Q residual on the hash-pinned chart rows                      0 terms
cofactor sigma-weight ledger: each cofactor homogeneous of 15-grade  13/13 OK
lift-back to the FULL unspecialized rows (only a1 -> a0*qa1):
   429 residual terms, monomials outside (rs,cs,c0,c1)               0
   explicit certificate reassembles exactly                          yes
   H 77 terms; L_rs 189, L_cs 180, L_c0 30, L_c1 30 (all polynomial)
mutations: each of the 13 cofactors +1, and each dropped (26 cases)  all nonzero
finite-field replay: 200 random points at p=65521 and p=2^31-1       0 mismatches
```

Rows used and their `output_sha256` prefixes (all rehashed by me against
`RESULT.json ce4d0adb…`): `Tg11_1 ddfff315`, `Tg11_2 70cf6c47`,
`Tg12_1 8c827abf`, `Tg12_2 b28d2dea`, `Tg12_3 9106a962`, `Tg13_1 125cfe9d`,
`Tg13_3 0672ce27`, `Tg14_1 1a7e3346`, `Tg14_3 86187535`, `Tg15_1 c1919647`,
`Tg15_3 dd5138e0`, `Tg15_5 a272b7c8`, `Tg15_6 c3bb2b11` (V9 / V20 / V22R1).

> **`T-a0` chart emptiness (unconditional).**  With `R, A, A', C` as in §8a
> but with `A = R/Q` any quotient killing the **thirteen** rows above,
>
> ```text
> a0^3 = sum_{13 rows} G_m*Tg_m + H*(a1-a0*qa1) + rs*L_rs + cs*L_cs + c0*L_c0 + c1*L_c1
> ```
>
> holds in `R[qa1]` with all cofactors polynomial over `Q`.  Hence
> `a0^3 in (a0*qa1-a1)*A'[qa1]`, so `1 in ((a0*qa1-a1):a0^inf)` and
> **`C = 0`**: the whole registered `T-a0` chart is the zero ring, not merely
> its `rho=0` fibre.  Exceptional power `a0^3`, localizer `s=1`, unit factor
> `1` (`W=0`).

This is the certificate that should be promoted; §8a is then the
human-checkable six-row face of the same fact (and remains independently
useful, since it needs only three grade-15-adjacent rows and one grade-15
row).  Two cautions: the surrounding design note is unreviewed and I checked
only its §2b identity — in particular I did **not** check its `T-a1`
refutation claims; and the saturation step needs the promoted exact chart
presentation `(2.3)`, so §8b inherits the same two dependencies listed in §5.

## 9. Scope firewall

Of the Fable5 design note I verified §2b's identity only; its `T-a1`
refutations, minimality claims, and AWS decision identity are untouched here.
This review promotes no `a1`-stratum result, no terminal-receiver result, no
radical or saturation computation, no source rows beyond the six cited, no
claim about `k=0` or the off-family fan, and no Gate-T, order-two,
maximum-twelve, or JC2 verdict.  It does not certify V24 as a certificate
producer.
