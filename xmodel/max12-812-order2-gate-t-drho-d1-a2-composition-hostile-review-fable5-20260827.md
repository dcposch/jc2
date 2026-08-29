# Hostile review: Gate-T `D(rho)` / D1 `a=2` contact composition (Fable5, different model)

Date: 2026-08-27

Reviewer: Fable5, adversarial, independent derivation.  No campaign module
was imported; every polynomial identity below was recomputed with my own
exact-`Fraction` arithmetic from the frozen inputs.

Producer under review:

```text
db0ecebf37cf8283c27e36ed8f0ba10ae9bcf1887d1854affe73cf61c8f367cd
  xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-sol-20260827.md
33514275318db4ce7ba01adae1f1260f416d3b47734cc4bc10b0217acbed51cd
  xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-replay-20260827.py
```

Both hashes recomputed locally and **match**.  Consumed upstream correction:

```text
d62b3f22bcad7de1bacecfa13c455f90bd654b578dd23cc5d2439054993f76f3
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-hostile-review-opus5-20260827.md
614ddcdb17ae233cd2babea5b45f329f57a7e28e13c7bc0616e78c6bc1731571
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-erratum-sol-20260827.md
```

Both rehash and match.  All twelve files pinned by the producer replay were
independently rehashed on disk and match.

## 0. Verdict summary

| Charged item | Verdict |
|---|---|
| 1. Rings, `p0=-2*rho^2`, localizer `D(p*k)=D(rho*k)`, shifted root pairs (2.6)/(2.7) | **CONFIRMED** |
| 2. V28 grade-16 custody: universal path vs `rho=0` serialized face | **CONFIRMED, and strengthened to a byte-level reproduction** |
| 3. Finite-jet factorization `CF-D1-A2` and two-grade completeness | **CONFIRMED, and strengthened: grades 0–14 vanish identically on the contact locus** |
| 4. Composition with the reviewed D1 `a=2` endpoint; both decks; moving root; residue `(3/2)*rho^2*cv^2` | **CONFIRMED** |
| 5. Replay adequacy and source/presentation custody | **GAP (custody-honest but under-verifying; erratum-directed pins missing; §8 overstates)** |
| 6. Strategic scope, coverage firewalls, no-go countermodel | **CONFIRMED** |

The upstream refutation is consumed correctly: nowhere does the producer
treat the vanished stage-zero `J1+J2` coordinates as leading D1 forms.  The
composition is carried entirely by the shifted pairs (2.7), exactly as the
erratum demanded ("any downstream contact import must exhibit and check its
shifted finite-jet map explicitly").  The mathematics of sections 2, 4, 5,
6, 7 of the producer is, as far as I can check it — and I checked all of it
by independent reconstruction — **true and correctly firewalled**.  The one
defect is evidentiary: the desk replay verifies transcriptions and hashes,
not rows, and it ignores the Opus5 erratum's custody directive.  My own
verifier closes that gap for this review.

## 1. What I did

Independent verifier `c9998a67618430a3dbcf47451c907a646761707e2ac37682c30d415b7a040be0`
(Appendix A, 102 s, pure-Python `Fraction`, run from the repository root),
plus the V28 face checker
`cff4ea54471465d11d05f08b4b35a5d28f072ed136214b81e88abaacb630011e`
(Appendix B).  Everything below was recomputed from four frozen inputs only:
the 569-tail `tails.json` (`d72f774c…`, canonical digest `6eed03d4…`
reproduced), the seven frozen `Tg15_*_q.poly` bytes, the frozen `D1AC`
compiler `compile_r1_d1_ac.py` (`e024a13d…`), and the frozen
`compile_cge3_universal.py` (`352ad4f2…`) for `transform_series`.

1. rebuilt all seven **general-`rho`** actual-total rows through grade 16
   from (3.1) and the tails; matched all 2396 frozen grade-15 terms exactly;
2. rebuilt the V28 `rho=0` ordered-`a1` grade-16 face and matched all seven
   frozen `aws_q` `.poly` files term-for-term (467 terms), plus both AWS
   evidence freezes after the standard `/source/` path remap;
3. specialized the total rows to the contact locus of (0.1) and computed the
   exact variable support at every grade `0..16`;
4. rebuilt the charged `D1AC` rows from the frozen compiler's literal
   `d1_section` arguments and checked the renaming (4.2) at **all** grades
   `0..16` (119 identities);
5. expanded `universal_hshift` independently, extracted the analytic
   `h_{15,j}, h_{16,j}`, verified the lower-unitriangular moving row
   identity at both grades, both denominator recurrences, both deck
   allocations, and the terminal residue **identically in every free jet**;
6. re-ran the producer replay (PASS, 12/12 pins) and re-derived the
   localizer identity and the coverage countermodel by hand.

No AWS launch, no CAS, no web access, no ledger edit, no `jc2-lean` access
of any kind.  Only this file was written.

## 2. Attack 1 — rings, localizer, shifted root pairs

### 2.1 Rings and ideals

`U_16^rho = U_16 ⊗_{k[p0]} k[rho]`, `p0 ↦ -2*rho^2` (2.1) is the Kummer
base change whose global finite faithful flatness was independently
confirmed in the Opus5 review; I re-checked the normal-form argument
(division by the monic `rho^2+p0/2` gives the free rank-two basis `{1,rho}`)
and accept it.  `I^tot_16` names the rows at all grades `<=16`; V28's
`MAX_DEGREE=16` build carries every jet a grade-16 coefficient can touch
(`ell16, cs14, rs14, az11, ac11, ez11, ec11, k10_12, k6_4`), so the ring is
large enough.  The staged ideals (2.5) match the frozen chart registry.

### 2.2 Localizer identity (2.4) — derived, not assumed

On the D1 side the promoted endpoint localizes at `S = {(p*k10)^n}`.  Under
`p ↦ -2*rho^2` the localizer becomes `-2*rho^2*k`.  In characteristic zero
`-2` is a unit, and inverting `rho^2*k` is equivalent to inverting `rho*k`:

```text
rho * (rho*k) = rho^2*k        => rho invertible in (rho^2*k)^{-1}-ring,
(rho^2*k) * k = (rho*k)^2      => rho^2*k invertible in (rho*k)^{-1}-ring.
```

Hence the two multiplicative sets generate the same localization and
`D(p*k) = D(rho*k)` as registered opens.  **CONFIRMED.**  No other
inversion is smuggled in: the grade-16 numerator `N16` is a polynomial
evaluated at a root, not a division (checked in §5.4); `theta`, `eta`,
`b0`, `b1`, `ell1`, `L` are never inverted.

One presentational defect: §0 declares "`k` a characteristic-zero field"
and two sentences later uses `k` for the leading unit-`k10` coefficient in
`D(rho*k)`.  This is exactly the documented `k`/`k0`/`k10` naming drift.
Unambiguous from context, but it should be repaired (§7, R4).

### 2.3 Shifted pairs (2.7) are the correct transport

From the frozen `D1AC` arguments and the renaming (4.2), the D1 stage-zero
coefficients correspond to the total shifted jets as

```text
a1^D = aaa1,   a0^D = aaa0,
c1^D = ez3/2,  c0^D = ec3/2,
eta*b1 = cs2,  eta*b0 = rs2/4        (theta = 1).
```

Substituting into the D1 pair forms `a0^D ± rho*a1^D`, `(c0^D ± rho*c1^D)`,
`(b0 ± rho*b1)` gives exactly (2.7): `A0± = aaa0 ± rho*aaa1`,
`C0± = (ec3 ± rho*ez3)/2`, `R0± = rs2/4 ± rho*cs2` — the same three
matrices as (2.6), with determinants `-rho/2, -rho/2, -2rho` (rechecked by
hand), applied one contact level deeper.  The producer's §5 allocation in
total names (`aaa0+rho*aaa1=0`, `ec3-rho*ez3=0` on the plus deck) is the
verbatim image of the compiler's `or15` substitution
(`a0=-au*lam, c0=+cv*lam`): with `a0^D=-au*rho, a1^D=au` one gets
`A0plus = 0`, and with `c0^D=cv*rho, c1^D=cv` one gets `C0minus = 0`.
**Exact.**

### 2.4 The refuted stage-zero composition is genuinely not used

I checked every step of the producer's derivation for a hidden use of the
withdrawn §6 sentence of the old bridge.  The stage-zero coordinates
`rs,cs,c0,c1,a0,a1` appear only (i) inside `J1,J2` (2.5), (ii) in the
context display (2.6) with the explicit warning that they vanish on this
contact, and (iii) among the fourteen contact vanishings.  The leading D1
forms are everywhere the shifted pairs.  The ring map direction is the
sound contravariant one: the contact locus of the total scheme is
identified with the D1 jet scheme by the renaming, so D1 emptiness pulls
back to total-contact emptiness.  The refuted direction (stage-zero root
matrices supplying D1 orientations) never occurs.

**Verdict, ring/map: CONFIRMED.**

## 3. Attack 2 — V28 grade-16 custody

I read `prolong_boundary_g16_v28.py` (`6c76dc54…`, matches its own
`FREEZE.sha256` row) line by line.  Findings:

1. `build_source_series` constructs, with **general `rho`**
   (`p[0] = -2*rho*rho`) and `MAX_DEGREE=16`, exactly the series (3.1):
   moving `p`-jets `2*ell_i` through `i=16`, `c = sigma^2*Cseries`,
   `r = (p^2+sigma^2*Rseries)/4`, the four `sigma^3`-shifted correction
   series with the `(p*Az+Ez)/2` and `(p*Ac+Ec)/2` couplings, the seven
   `F_i` of (2.2), and loads `sigma^4*k10, sigma^12*k6, sigma^20*k2` with
   the frozen jet names (`k, k1, k2c, k10_3.., k6, k6_1.., k2`).
2. All seven `totals[row]` through grade 16 exist **before** the face
   specialization `killed = J1 ∪ {a0, rho}` (V23's
   `J1 = {rs,cs,c0,c1}`) is applied.  Only the face is serialized.
3. The pinned `aws_q/RESULT.json` (`c9f89344…`) status
   `PASS-A1-BOUNDARY-PROLONG-G16-V28` and face term counts
   `63,86,98,45,77,22,33` are the wrapper's record of that exact-Q run.

I then **reproduced the seven face polynomials byte-for-byte**: my own
general-`rho` grade-16 rows, specialized by the same kill set, equal the
frozen `aws_q/compiled/Tg16_*_q.poly` contents term-for-term, and both AWS
evidence freezes (29 rows each, `aws_q` and `aws_p65521`) rehash after
remapping the recorded AWS-absolute paths at `/source/cases/…`.  So the
producer's sentence "its exact-Q execution freezes the grade-16
construction path and the seven face outputs" is literally true, and its
scope discipline is exactly right: the serialized rows are `rho=0`
ordered-`a1` face rows and are nowhere relabeled as general-`rho` rows.

The general-`rho` grade-16 rows used by the theorem remain **derived-here
objects** on my side too, but they are now anchored three independent ways:
(i) the same series construction reproduces all 2396 frozen grade-15 terms;
(ii) it reproduces all 467 frozen V28 face terms at grade 16; (iii) the
image under the contact renaming reproduces the frozen `D1AC` compiler's
grade-16 rows, which were engine-certified on dual AWS lanes in the
finite-band case.  The producer's judgment that a dedicated general-`rho`
grade-16 serialization "would improve documentary custody but is not an
additional mathematical hypothesis" is correct: the grade-16 coefficients
are polynomial consequences of the pinned emitter, insensitive to any
truncation choice.  I still endorse freezing one (it remains the single
most valuable forward export, as the Opus5 review already said).

**Verdict, grade-16 custody: CONFIRMED (byte-level).**

## 4. Attack 3 — finite-jet factorization `CF-D1-A2`

This is the load-bearing new mathematics, and I verified it by direct
computation rather than by the support table.

### 4.1 The contact locus and the fourteen vanishings

Contact (0.1) in the total presentation is precisely

```text
Az, Ac == 0 mod sigma^2   =>  a1=aa1=a0=aa0=0,
Ez, Ec == 0 mod sigma^3   =>  c1=e1=ee1=c0=e0=ee0=0,
Cser, Rser == 0 mod sigma^2 => cs=cs1=rs=rs1=0,
```

with exactness `(aaa1,aaa0) != (0,0)` and `(ez3,ec3) != (0,0)`, and
`ord(R)>=2` free.  These fourteen vanishings contain every generator of
`J1+J2`, so the contact locus sits inside the terminal-receiver stratum —
consistent with the Opus5 finding that the induced map lands there and on
no blowup chart.

### 4.2 Independent support computation (the decisive check)

I specialized my independently rebuilt total rows at the fourteen
vanishings and computed exact supports:

- **grades 0–14: all seven rows vanish identically.**  The producer's lemma
  claims only that the fourteen window rows factor; in fact the entire row
  system through grade 16 collapses onto the two-grade window.  A contact
  arc satisfies the grade `<=14` equations automatically, so no discarded
  low-grade condition is being hidden.  This is a free strengthening the
  producer may state.
- **grade 15** (2,2,2,0,2,0,2 terms): support
  `{aaa0,aaa1,ez3,ec3}` plus `rho` — the `AC/L` family only.
- **grade 16** (8,10,11,2,11,0,11 terms): support contained in
  `{aaa0,aaa1,az3,ac3,ez3,ez4,ec3,ec4,cs2,rs2,k,ell1,rho}`.
  Row 4 is the pure `C^2` slot (`{ez3,ec3,rho}`); row 6 is identically
  zero; `ell1` occurs in rows 2,3,5,7 only, matching the Opus5 mutation
  table for the moving term.

Therefore **no discarded jet contributes** inside the window.  Explicitly
checked absent at grades 15–16 on the contact locus: `ell2..ell16`,
`cs3..cs14`, `rs3..rs14`, `az4..az11`, `ac4..ac11`, `ez5..ez11`,
`ec5..ec11`, `k1`, `k2c`, `k10_3..k10_12`, `k6, k6_1..k6_4`, `k2`, and all
four targets.  The `k10`-jet naming trap flagged by Opus5 (`k2c` looks like
a `k2` jet) is therefore immaterial to this window, though (4.2) should
still name `k1, k2c ↦ 0` explicitly (§7, R3).

This confirms the producer's family bookkeeping (4.3)–(4.4) as the correct
*explanation*: with `a=2` the only in-window polar families are `AC/L` at
15 and `C^2/L^2`, `k10*R*C/L`, `k10*R^3/L` at 16; the successor families
sit at `>=18` (`RA^2/L^2` and `k10*A^2/L` at 18, `k10*R^2A/L^2` at 19,
`k6*C/L` at 20, `A^3/L^3` at 21, `k2*R/L` at 24, targets at 28/32/36/38).
I re-derived each entry grade from the eight-term `universal_hshift`
generating function and the fan weights; they agree with the replay's
`orders` table and with the confirmed grok support table.  My raw-row
support computation is independent of, and stronger than, that table.

### 4.3 The substitution identity

Renaming the contact rows by (4.2) (with `theta` retained as bookkeeping)
and substituting `p = -2*rho^2` into my independently rebuilt `D1AC` rows
gives **equality at every grade `0..16`, all seven rows** — 119 exact
identities.  In particular the induced window rows are exactly
`I^D1_(15,16)`, and the grade-15 image has the known two-binomial
structure: rows `(g1, g2, -(p/4)g1, 0, -(p^2/32)g1, 0, -(p^3/128)g1)` with
`g1 = (3/4)theta^2(a0^D c1^D + a1^D c0^D)`,
`g2 = (3/8)theta^2(2 a0^D c0^D - p a1^D c1^D)`.

The renaming is injective on monomials (the `eta`-degree records the
`cs2/rs2` degree and the `b`-exponents recover it), so no information is
lost or aliased; `theta=1` is a legitimate normalization because the
identity holds with `theta` present and the induced arc point has
`theta=1`, a unit.

**Verdict, finite-jet completeness: CONFIRMED, with the grade `0..14`
identical-vanishing strengthening.  Lemma `CF-D1-A2` is proved.**

## 5. Attack 4 — composition with the reviewed D1 `a=2` endpoint

### 5.1 Endpoint statement match

The promoted statement (`973f7953…`, confirmed by grok `e03de4e1…`)
excludes, on `D(p*k10)` after the reviewed first-normal/half-weight/`M=0`
gates, arcs with `ord(A)=a, ord(C)=a+1, ord(R)>=a`, `a in {2..5}`, via the
two-allocation dichotomy and next-grade residue `(3/2)*lambda^2*cv^2`.
The producer consumes exactly the `a=2` member, with `D(p*k10)` pulled
back to `D(rho*k)` by §2.2, the same gates as hypotheses, and the same
residue.  Note `RESULT.md` states the gates as first-normal + half-weight
and the promotion adds `M=0`; the producer assumes all three, which only
weakens its claim — the safe direction.  The gates enter the composition
only through the registered presentation (3.1) itself (unit-`k10`
normalized post-gate form); no gate predicate is needed inside the
two-grade algebra, which my rederivation confirms uses nothing but the
fourteen window rows, exact contact, and `rho` a unit.

### 5.2 Exclusion re-derived end to end

From my independently built objects:

1. `transform_series` diagonal: `T0(i,i) = 1` for all `i` — the moving row
   basis is lower-**uni**triangular, hence invertible over any coefficient
   ring, no localization needed for this step.
2. Row identities (14 checks): `g15_i = Σ_j T0_ij(p) h15_j` and
   `g16_i = Σ_j T0_ij h16_j + Σ_j T1_ij(ell1,p) h15_j`, with
   `T1 = 2*ell1*dT0/dp`.  So raw window rows vanish iff all fourteen
   analytic `h` vanish.
3. Recurrences: `h15_{k+2} + (p/2) h15_k = 0` (k=1..5) and
   `h16_{k+4} + p h16_{k+2} + (p^2/4) h16_k = 0` (k=1..3): the grade-15
   polar content is `N15/L` with `N15 = h15_1 z + h15_2`, the grade-16
   content is `N16/L^2` with
   `N16 = h16_1 z^3 + h16_2 z^2 + (h16_3+p h16_1) z + (h16_4+p h16_2)`,
   both against the **static** `L = z^2+p/2 = z^2-rho^2`; the moving-root
   corrections are already peeled off into the `T1` connection and the
   `sigma`-linear parts of the `Inv` expansions.
4. `h15_1 = g1` and `h15_2 = g2` exactly, so `N15 = 0` is `L | A0*C0`.
   With `L` squarefree on `D(rho)` and exact contact: if `a1^D = 0` then
   `g1=0` forces `c1^D=0` and `g2=0` then forces `c0^D=0`, contradicting
   exact `ord(C)=3`; symmetrically for `c1^D=0`.  Hence `a1^D=au != 0`,
   `c1^D=cv != 0`, and precisely the two opposite-root allocations (5.2)
   survive, exchanged by `rho ↦ -rho`.
5. On **both** allocations, `N15` vanishes identically, and

   ```text
   N16(z = allocated A0 root) = (3/2)*rho^2*cv^2*theta^2
   ```

   **identically in every free jet** — `aa0^D, aa1^D, cc0^D, cc1^D, b0,
   b1, eta, ell1, k0` all cancel, both decks.  This is the machine form of
   "every competing in-window term is a simple pole and acquires a factor
   `L` in the `L^2` numerator": the `ell1`-independence disposes of the
   moving Hensel root, the `eta`/`b`-independence covers both `ord(R)=2`
   (unit `eta`) and `ord(R)>2` (`eta=0`) with one identity, and the
   `k0`-independence shows the load enters the window only through terms
   that die at the root.
6. Assembly: a post-gate arc on `D(rho*k)` with contact (0.1) satisfies
   the grade `<=14` rows automatically (§4.2), and its grade-15/16 rows
   are the D1 values (§4.3).  `g15=0` forces `h15=0` (unitriangularity),
   which with exactness forces an allocation with `au, cv != 0`;
   `g16=0` then forces `h16=0`, hence `N16 ≡ 0`, hence
   `0 = N16(root) = (3/2)*rho^2*cv^2`, which is nonzero since `rho` is a
   unit on the registered open, `cv != 0`, and the characteristic is zero.
   Contradiction.  **The exclusion (0.1) holds.**

Every localization used is accounted for: `rho` (registered open), `p`
(equals `-2*rho^2`, unit there), `k` (registered chart unit; not needed in
the residue itself), `au, cv` (nonzero by exact contact plus grade 15),
`theta=1`.  Nothing else is inverted.

### 5.3 Deck orientations

The plus and minus decks are both present, are exchanged by
`rho ↦ -rho = tau`, evaluate at `z=+rho` and `z=-rho` respectively, and
give the **same** residue value — verified symbolically, matching the
frozen compiler's `D1AC_resplus`/`D1AC_resminus` gates and the finite-band
`evalpos`/`evalneg` rings.  No orientation is dropped and none is
double-counted: the two decks are the two solutions of the grade-15
dichotomy, not independent hypotheses.

**Verdict, D1 endpoint composition: CONFIRMED.**

## 6. Attack 5 — replay adequacy, custody, coverage firewalls

### 6.1 What the replay actually proves

I re-ran it: `PASS-GATE-T-DRHO-D1-A2-COMPOSITION-DESK-REPLAY`, 12/12 pins
match.  Reading its four check functions:

- `custody_check`: real (12 SHA-256 pins).
- `construction_path_check`: substring sentinels on V28 and the `D1AC`
  compiler plus the pinned `RESULT.json` status/counts.  Real but
  transcription-level; it proves the frozen files contain the quoted
  lines, not that the report's mathematics matches them.
- `support_window_check`: arithmetic on a **hardcoded** copy of the order
  table.  It verifies the producer transcribed its own table consistently;
  it touches no frozen row.
- `deck_allocation_check`: three numeric samples of `A0*C0 = au*cv*L` and
  of the residue **formula**.  It does not derive the residue from any
  row or from the frozen compiler.
- `coverage_negative_control`: correct, matches my hand check.

So the replay is honest custody plus self-consistency, in the same genre
the Opus5 review criticized on the bridge replay.  Two specific defects:

1. **The erratum's custody directive is ignored.**  Erratum §3: "Future
   replays should pin the R1 wrapper and all seven `.poly` bytes."  This
   replay pins neither, nor `tails.json`, nor `compile_cge3_universal.py`
   (the `transform_series` source), except transitively through a pinned
   but never-executed KRB replay file.  For the record, the missing pins
   are:

   ```text
   d9f23a279b39b45ca27717a00493a6e928d1042007bc2c3c183eb2d239882768  export_allrows_g15_v22r1.py
   4d237049cdd6fbaf05a14dcda0710fdb1660058241b0b3a72e1c0c473e7a40ba  Tg15_1_q.poly
   5a438032b3d558131246d3022006b68cc424f4c09bfcef0215e8ce8ea76e0e69  Tg15_2_q.poly
   53d513df5003c5b0e60a50aff59779d9c921374e8878dea8e7ba9f3152d294d4  Tg15_3_q.poly
   2cf0b1d34df224ba0df2b60bdd7b8144fd733d35133edd851c91d27a9b830748  Tg15_4_q.poly
   26e2f4ef586955dddd1d694343f1bf29f28f050e4da61f386b2e11fb44a08f08  Tg15_5_q.poly
   786c6bb976305614cc0945b2ebf0d78600fb9a96aefa1553248ff8f473b5c51e  Tg15_6_q.poly
   1b3eb2ae0963ee0044a209d91f8dc3ca9ef4d11c3dd47633d799219449bfcddd  Tg15_7_q.poly
   d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  tails.json
   352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23  compile_cge3_universal.py
   ```

   (all under their recorded case paths; the seven `.poly` rows are in
   `cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/`).
2. **Producer §8 overstates the replay**: "It checks … the complete
   two-grade support window, both root allocations, (5.3) …" — each of
   these is checked only as a transcription or numeric sample.  The
   mathematical verification lives in the frozen `D1AC`/finite-band AWS
   certifications, the Opus5 reconstruction, and now Appendix A here.

The composition does not fall on this: everything the replay fails to
verify, I verified independently, and the analytic side was already
engine-certified over exact Q in the frozen finite-band run.  But as
stated, replay adequacy is a **GAP** with a small repair (§7, R1–R2).

### 6.2 Coverage firewalls

The §6 no-go is correct and its countermodel is sound: `q(u-1) = -1` makes
the client the unit ideal while `(rho,u)=(1,1)` remains in
`V(I) ∩ D(rho)`, with everything `tau`-equivariant.  So client emptiness
plus finite-jet fidelity, without valuative coverage, proves nothing about
the source — the composition's own §6 says so and its two-requirement
interface (fidelity + coverage) is the right one.  The whole-cover outcome
**INCOMPLETE** is honestly recorded in the replay payload.

Placement in the fan is also right: `(a,c,r)=(2,3,>=2)` is the `a=2`
member of the parametric unique-`AC` `d=1` family of the pinned lower-hull
reduction (`c9ecfe40…`), with `RC` joining at `s=0` and `R^3` joining only
at `(2,3,2)` — matching the licensed in-window terms exactly.  The
remaining cells listed in §6 (rest of the unique-`AC` fan, the `C2`, `R3`,
`RC`, `A2` primary cells, equality faces, the exact-square zero-normal
receiver, positive-order `k10`, `k=0`) are genuinely outside this theorem.
Sections 7 and 9 correctly deny any `rho=0`, six-chart, `G2-PSC`, `G2-BD`,
Gate-T, order-two, maximum-twelve, or JC2 consequence; the ramified fibre
argument (all three root determinants vanish at `rho=0`) stands.

**Verdict, strategic scope: CONFIRMED.  Replay adequacy: GAP.**

## 7. Smallest repair

No mathematical content changes.

- **R1 (replay custody):** add the ten pins listed in §6.1 to the replay's
  `PINS` table, discharging the erratum directive.
- **R2 (§8 phrasing):** replace "It checks the frozen Kummer bridge, …,
  the complete two-grade support window, both root allocations, (5.3), and
  the coverage negative control" with "It pins the frozen inputs and
  re-checks transcriptions of the support window, allocation, residue, and
  countermodel; row-level verification is carried by the frozen dual-AWS
  `D1AC`/finite-band certifications and the independent reviews."
- **R3 ((4.2) completeness):** state `k1, k2c, k10_i (i>=3), k6_i (i>=1),
  k2_i (i>=1) -> 0` explicitly, to close the standing `k2c` naming trap.
- **R4 (§0 naming):** rename the base field or write `D(rho*k10lead)` so
  the field `k` and the load coefficient `k` stop colliding.
- **Optional strengthening:** record that on the contact locus the total
  rows vanish identically at all grades `0..14` (§4.2), so the two-grade
  window is the *complete* row content of `I^tot_16` on this contact.

## 8. Strongest exact surviving statement

The composition is **not** too strong; (0.1) survives verbatim, and with
the §4.2 strengthening it can be stated sharply:

> **Theorem (confirmed).**  Work in the registered post-gate total source
> (3.1) over a characteristic-zero field, on the open `D(rho*k)` (equal to
> the pullback of the promoted D1 chart `D(p*k10)` under `p=-2*rho^2`).
> Let a normalized DVR arc have square-correction contact
> `ord(A)=2, ord(C)=3, ord(R)>=2` — equivalently the fourteen vanishings
> of §4.1 with `(aaa1,aaa0) != 0 != (ez3,ec3)`.  Then its total rows vanish
> identically at grades `0..14`, its grade-15/16 rows are exactly the
> charged `D1AC` rows under the shifted-pair renaming (4.2), and the pair
> (grade-15 allocation dichotomy, grade-16 residue
> `(3/2)*rho^2*cv^2 != 0`) is contradictory on both decks.  **No such arc
> exists.**  This is one arcwise contact exclusion after the reviewed
> generic-square gates; it is not a `D(rho)` cover, not a ramified-fibre
> result, and not a Gate-T, `G2-PSC`, `G2-BD`, order-two, maximum-twelve,
> or JC2 verdict.

## 9. `AUDIT.md` promotion eligibility

**Eligible, as one narrow filing, after repairs R1–R2** (R3–R4 cosmetic):
the `D(rho*k)` `a=2` contact exclusion of §8, together with Lemma
`CF-D1-A2` (including the grade `0..14` identical vanishing), the
localizer identity `D(p*k)=D(rho*k)`, the byte-level V28 custody scope of
§3, and the §6 fidelity-plus-coverage interface with its countermodel.
This is the first shifted-root contact composition to survive the review
demanded by the standing `AUDIT.md` Kummer entry ("the later shifted-root
contact compositions remain provisional until reviewed independently");
no existing entry covers it.  It is independently reconstructed on both
sides here and desk-replayable via Appendix A.

**Not eligible in any form:** any reading as a `D(rho)` cover, a ramified
(`rho=0`) result, a whole deck/square statement, a Gate-T, `G2-PSC`,
`G2-BD`, order-two, maximum-twelve, or JC2 claim — the producer claims
none of these, and the countermodel in its §6 is the standing reason such
an upgrade would be false.  The producer replay should not be cited as
row-level verification (§6.1).

## 10. Execution record

```text
producer report       db0ecebf…  hash verified
producer replay       33514275…  hash verified, re-run, PASS, 12/12 pins independently rehashed
upstream review       d62b3f22…  hash verified
upstream erratum      614ddcdb…  hash verified
KRB producer          1b583d5a…  hash verified
V28 script/freeze     6c76dc54… / 8e54871f…  verified; both AWS evidence freezes rehash (29+29 rows, /source/ remap)
frozen Tg15 rows      7 files, digests in §6.1, all reproduced term-for-term
frozen V28 Tg16 face  7 files, reproduced term-for-term (467 terms)
reviewer verifier     c9998a67618430a3dbcf47451c907a646761707e2ac37682c30d415b7a040be0   102 s
face checker          cff4ea54471465d11d05f08b4b35a5d28f072ed136214b81e88abaacb630011e   ~9 s
```

Desk-scale only.  No AWS launch, no CAS, no web sweep, no canonical-ledger
edit, no `jc2-lean` access.  Only this file was written.

## Appendix A — reviewer verifier

Run from the repository root (`python3 /tmp/fable5_kgt_drho_d1_a2_verify.py`
with `ROOT` set accordingly); imports no campaign module.

```python
#!/usr/bin/env python3
"""Fable5 hostile independent verifier: KGT-DRHO-D1-A2 composition.

Independent implementation (no campaign module imported).  Checks:
  A. frozen custody of every mathematical input actually used;
  B. seven actual-total rows rebuilt from the 569-tail JSON, grade-15
     rows compared against the frozen Tg15_*_q.poly bytes;
  C. V28 grade-16 rho=0 ordered-a1 face reproduced (term counts + bytes
     custody via RESULT.json counts);
  D. contact-locus specialization (0.1): grades 0..14 must vanish, and
     the grade-15/16 supports must lie inside the (4.2) source jets --
     the decisive later-jet-independence check of Lemma CF-D1-A2;
  E. renamed contact rows equal the frozen D1AC-compiler rows at every
     grade 0..16 (with p -> -2*rho^2), i.e. the finite-jet factorization;
  F. analytic side: universal_hshift h-extraction, unitriangular moving
     row identity at grades 15/16, both denominator recurrences;
  G. both deck allocations kill N15; N16 at the allocated A0 root equals
     (3/2)*rho^2*cv^2*theta^2 identically in all free jets, both decks.
"""
from __future__ import annotations

import json
import math
import re
import sys
import time
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

ROOT = Path("/Users/dc/code/math/jc2")
N = 17  # sigma-grades 0..16

T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


# ---------------- sparse polynomials ----------------
def P0():
    return {}


def Pc(c):
    c = Fraction(c)
    return {(): c} if c else {}


def Pv(name, exp=1):
    return {((name, exp),): Fraction(1)}


def Padd(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            v = out.get(m, Fraction(0)) + c
            if v:
                out[m] = v
            elif m in out:
                del out[m]
    return out


def Pscale(s, p):
    s = Fraction(s)
    if not s:
        return {}
    return {m: c * s for m, c in p.items()}


def Pmul(a, b):
    out = {}
    for ma, ca in a.items():
        da = dict(ma)
        for mb, cb in b.items():
            d = dict(da)
            for nm, e in mb:
                d[nm] = d.get(nm, 0) + e
            key = tuple(sorted(d.items()))
            v = out.get(key, Fraction(0)) + ca * cb
            if v:
                out[key] = v
            elif key in out:
                del out[key]
    return out


def Ppow(p, e):
    out = Pc(1)
    b = p
    while e:
        if e & 1:
            out = Pmul(out, b)
        e >>= 1
        if e:
            b = Pmul(b, b)
    return out


def Psub(p, table):
    """Substitute: name -> Poly for names in table, others kept."""
    out = {}
    for m, c in p.items():
        term = Pc(c)
        for nm, e in m:
            base = table.get(nm)
            term = Pmul(term, Ppow(base, e) if base is not None else Pv(nm, e))
            if not term:
                break
        out = Padd(out, term)
    return out


def support(p):
    return {nm for m in p for nm, _ in m}


# ---------------- truncated sigma-series ----------------
def SZ():
    return [P0() for _ in range(N)]


def Sadd(*ss):
    return [Padd(*[s[i] for s in ss]) for i in range(N)]


def Sscale(c, s):
    return [Pscale(c, x) for x in s]


def Smul(a, b):
    out = SZ()
    for i in range(N):
        if not a[i]:
            continue
        for j in range(N - i):
            if b[j]:
                out[i + j] = Padd(out[i + j], Pmul(a[i], b[j]))
    return out


def Sshift(s, k):
    return ([P0()] * k + s[: N - k]) if k else list(s)


def Spow(s, e):
    out = SZ()
    out[0] = Pc(1)
    b = s
    while e:
        if e & 1:
            out = Smul(out, b)
        e >>= 1
        if e:
            b = Smul(b, b)
    return out


def Snamed(names):
    s = SZ()
    for i, nm in enumerate(names):
        if i < N:
            s[i] = Pv(nm)
    return s


def Ssig(k, poly):
    s = SZ()
    if k < N:
        s[k] = poly
    return s


# ---------------- custody ----------------
def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


PINS = {
    "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json":
        "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py":
        "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    "cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py":
        "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23",
    "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/prolong_boundary_g16_v28.py":
        "6c76dc541d27b436a289f1decccd6e90c1424b3a586685e128331c8490b06480",
    "xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md":
        "1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a",
}
for rel, expected in PINS.items():
    actual = digest(ROOT / rel)
    assert actual == expected, ("custody", rel, actual)
log("A. custody: all direct mathematical inputs rehash")

TAILS = json.loads((ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json").read_text())
canonical = json.dumps(TAILS, sort_keys=True, separators=(",", ":"))
assert sha256(canonical.encode()).hexdigest() == "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
counts = [len(TAILS[str(r)]) for r in range(1, 8)]
assert counts == [36, 54, 58, 81, 89, 120, 131] and sum(counts) == 569
log("   tails.json canonical digest + 569 census ok")

# ---------------- total source series (independent of V28/V22 code) ----------------
p_tot = SZ()
p_tot[0] = Pscale(-2, Pmul(Pv("rho"), Pv("rho")))
for d in range(1, 17):
    p_tot[d] = Pscale(2, Pv(f"ell{d}"))
c_tot = Sshift(Snamed(["cs"] + [f"cs{i}" for i in range(1, 15)]), 2)
r_tot = Sscale(Fraction(1, 4), Sadd(Smul(p_tot, p_tot), Sshift(Snamed(["rs"] + [f"rs{i}" for i in range(1, 15)]), 2)))
az_tot = Snamed(["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 12)])
ac_tot = Snamed(["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 12)])
ez_tot = Snamed(["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 12)])
ec_tot = Snamed(["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 12)])
n3 = Sshift(az_tot, 3)
n2 = Sshift(ac_tot, 3)
n1 = Sshift(Sscale(Fraction(1, 2), Sadd(Smul(p_tot, az_tot), ez_tot)), 3)
n0 = Sshift(Sscale(Fraction(1, 2), Sadd(Smul(p_tot, ac_tot), ec_tot)), 3)
FT = {
    6: Sscale(2, p_tot),
    5: Sscale(2, c_tot),
    4: Sadd(Smul(p_tot, p_tot), Sscale(2, r_tot)),
    3: Sadd(Sscale(2, Smul(p_tot, c_tot)), Sshift(n3, 2)),
    2: Sadd(Smul(c_tot, c_tot), Sscale(2, Smul(p_tot, r_tot)), Sshift(n2, 2)),
    1: Sadd(Sscale(2, Smul(c_tot, r_tot)), Sshift(n1, 2)),
    0: Sadd(Smul(r_tot, r_tot), Sshift(n0, 2)),
}
LT = {
    7: Sshift(Snamed(["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 13)]), 4),
    8: Sshift(Snamed(["k6", "k6_1", "k6_2", "k6_3", "k6_4"]), 12),
    9: Sshift(Snamed(["k2"]), 20),
}
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]


def build_row(entries, row, F, L):
    tot = SZ()
    for raw_m, raw_c in entries:
        m = [int(v) for v in raw_m]
        assert len(m) == 10 and sum(a * b for a, b in zip(m, WEIGHTS)) == 12 + row
        coeff = Fraction(str(raw_c))
        assert coeff
        term = SZ()
        term[0] = Pc(1)
        for i, e in enumerate(m[:7]):
            if e:
                term = Smul(term, Spow(F[i], e))
        for i, e in enumerate(m[7:], start=7):
            assert e in (0, 1)
            if e:
                term = Smul(term, L[i])
        tot = Sadd(tot, Sscale(coeff, term))
    return tot


log("B. building seven actual-total rows through grade 16 (general rho) ...")
TOT = {}
for row in range(1, 8):
    TOT[row] = build_row(TAILS[str(row)], row, FT, LT)
    log(f"   row {row}: g15 {len(TOT[row][15]):>4} terms, g16 {len(TOT[row][16]):>4} terms")

# frozen grade-15 bytes
TERM_RE = re.compile(r"^\((-?\d+(?:/\d+)?)\)\*(.*)$")


def parse_poly(path: Path):
    out = {}
    for part in path.read_text().strip().split("+"):
        part = part.strip()
        if not part:
            continue
        mm = TERM_RE.match(part)
        assert mm, (path, part[:60])
        co = Fraction(mm.group(1))
        d = {}
        for f in mm.group(2).split("*"):
            if "^" in f:
                nm, e = f.split("^")
                d[nm] = d.get(nm, 0) + int(e)
            else:
                d[f] = d.get(f, 0) + 1
        key = tuple(sorted(d.items()))
        out[key] = out.get(key, Fraction(0)) + co
    return {k: v for k, v in out.items() if v}


FROZEN15 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled"
ok15 = True
for row in range(1, 8):
    fr = parse_poly(FROZEN15 / f"Tg15_{row}_q.poly")
    same = fr == TOT[row][15]
    ok15 &= same
    odd = sum(1 for mo in fr for nm, e in mo if nm == "rho" and e % 2)
    log(f"   frozen Tg15_{row}: {len(fr):>4} terms, match={same}, odd-rho terms={odd}")
assert ok15, "frozen grade-15 mismatch"
log("   all seven frozen grade-15 rows reproduced exactly")

# V28 rho=0 ordered-a1 face at grade 16
KILL_V28 = {"rs", "cs", "c0", "c1", "a0", "rho"}
face_counts = {}
for row in range(1, 8):
    face = {m: c for m, c in TOT[row][16].items() if not any(nm in KILL_V28 for nm, _ in m)}
    face_counts[f"Tg16_{row}"] = len(face)
V28_EXPECTED = {"Tg16_1": 63, "Tg16_2": 86, "Tg16_3": 98, "Tg16_4": 45, "Tg16_5": 77, "Tg16_6": 22, "Tg16_7": 33}
assert face_counts == V28_EXPECTED, ("V28 face counts", face_counts)
log(f"C. V28 rho=0 ordered-a1 grade-16 face term counts reproduced: {face_counts}")

# ---------------- D. contact-locus specialization ----------------
CONTACT_ZERO = {"a1", "aa1", "a0", "aa0", "c1", "e1", "ee1", "c0", "e0", "ee0", "cs", "cs1", "rs", "rs1"}
MAPPED = {"rho", "ell1", "cs2", "rs2", "aaa1", "aaa0", "az3", "ac3", "ez3", "ez4", "ec3", "ec4", "k", "k6", "k2"}
ctab = {nm: P0() for nm in CONTACT_ZERO}
CON = {}
low_ok = True
sup_ok = True
for row in range(1, 8):
    CON[row] = [Psub(TOT[row][g], ctab) for g in range(N)]
    low = [g for g in range(15) if CON[row][g]]
    if low:
        low_ok = False
        log(f"   !! row {row}: contact rows nonzero below grade 15 at {low}")
    s15 = support(CON[row][15])
    s16 = support(CON[row][16])
    extra = (s15 | s16) - MAPPED
    if extra:
        sup_ok = False
        log(f"   !! row {row}: unmapped jets in window: {sorted(extra)}")
    log(f"D. row {row}: contact g15 {len(CON[row][15]):>3} terms sup={sorted(s15)}")
    log(f"          contact g16 {len(CON[row][16]):>3} terms sup={sorted(s16)}")
assert low_ok, "contact rows must vanish identically below grade 15"
assert sup_ok, "a discarded jet contributes inside the two-grade window"
log("   grades 0..14 vanish on the contact locus; grade-15/16 support inside the (4.2) jet set")

# ---------------- E. D1AC branch from the frozen compiler's literal arguments ----------------
th = Pv("theta")
et = Pv("eta")
pp = SZ()
pp[0] = Pv("p")
pp[1] = Pscale(2, Pv("ell1"))
azd = Sadd(Ssig(2, Pmul(th, Pv("a1"))), Ssig(3, Pmul(th, Pv("aa1"))))
acd = Sadd(Ssig(2, Pmul(th, Pv("a0"))), Ssig(3, Pmul(th, Pv("aa0"))))
czd = Sadd(Ssig(3, Pmul(th, Pv("c1"))), Ssig(4, Pmul(th, Pv("cc1"))))
ccd = Sadd(Ssig(3, Pmul(th, Pv("c0"))), Ssig(4, Pmul(th, Pv("cc0"))))
rzd = Ssig(2, Pmul(Pmul(th, et), Pv("b1")))
rcd = Ssig(2, Pmul(Pmul(th, et), Pv("b0")))
# source_coefficients: kc = sigma^2*rz ; kr = pp^2/4 + sigma^2*rc
kc = Sshift(rzd, 2)
kr = Sadd(Sscale(Fraction(1, 4), Smul(pp, pp)), Sshift(rcd, 2))
n3d = Sshift(azd, 3)
n2d = Sshift(acd, 3)
n1d = Sshift(Sadd(Sscale(Fraction(1, 2), Smul(pp, azd)), czd), 3)
n0d = Sshift(Sadd(Sscale(Fraction(1, 2), Smul(pp, acd)), ccd), 3)
FD = {
    6: Sscale(2, pp),
    5: Sscale(2, kc),
    4: Sadd(Smul(pp, pp), Sscale(2, kr)),
    3: Sadd(Sscale(2, Smul(pp, kc)), Sshift(n3d, 2)),
    2: Sadd(Smul(kc, kc), Sscale(2, Smul(pp, kr)), Sshift(n2d, 2)),
    1: Sadd(Sscale(2, Smul(kc, kr)), Sshift(n1d, 2)),
    0: Sadd(Smul(kr, kr), Sshift(n0d, 2)),
}
LD = {7: Ssig(4, Pv("k0")), 8: Ssig(12, Pv("k6")), 9: Ssig(20, Pv("k2load"))}
log("E. building seven charged D1AC rows ...")
D1 = {row: build_row(TAILS[str(row)], row, FD, LD) for row in range(1, 8)}
for row in range(1, 8):
    low = [g for g in range(15) if D1[row][g]]
    assert not low, ("D1 divisibility", row, low)
log("   SOURCE_DIVISIBLE reproduced: all D1AC rows vanish below grade 15")
log("   D1 g15 term counts: " + str([len(D1[r][15]) for r in range(1, 8)]))
log("   D1 g16 term counts: " + str([len(D1[r][16]) for r in range(1, 8)]))

# renaming (4.2) with theta retained; compare against D1 rows with p -> -2 rho^2
RENAME = {
    "cs2": Pmul(Pmul(th, et), Pv("b1")),
    "rs2": Pscale(4, Pmul(Pmul(th, et), Pv("b0"))),
    "aaa1": Pmul(th, Pv("a1")), "az3": Pmul(th, Pv("aa1")),
    "aaa0": Pmul(th, Pv("a0")), "ac3": Pmul(th, Pv("aa0")),
    "ez3": Pscale(2, Pmul(th, Pv("c1"))), "ez4": Pscale(2, Pmul(th, Pv("cc1"))),
    "ec3": Pscale(2, Pmul(th, Pv("c0"))), "ec4": Pscale(2, Pmul(th, Pv("cc0"))),
    "k": Pv("k0"), "k6": Pv("k6"), "k2": Pv("k2load"),
}
PSUB = {"p": Pscale(-2, Pmul(Pv("rho"), Pv("rho")))}
fun_ok = True
for row in range(1, 8):
    for g in range(N):
        left = Psub(CON[row][g], RENAME)
        right = Psub(D1[row][g], PSUB)
        if left != right:
            fun_ok = False
            log(f"   !! functoriality fails row {row} grade {g}")
assert fun_ok
log("   renamed contact rows == D1AC rows with p=-2*rho^2 at EVERY grade 0..16 (7x17 identities)")

# g15 structure: N15-shape binomials
g1_expect = Pscale(Fraction(3, 4), Pmul(Ppow(th, 2), Padd(Pmul(Pv("a0"), Pv("c1")), Pmul(Pv("a1"), Pv("c0")))))
g2_expect = Pscale(Fraction(3, 8), Pmul(Ppow(th, 2), Padd(Pscale(2, Pmul(Pv("a0"), Pv("c0"))), Pscale(-1, Pmul(Pv("p"), Pmul(Pv("a1"), Pv("c1")))))))
assert D1[1][15] == g1_expect
assert D1[2][15] == g2_expect
for row, (s, d, j) in {3: (-1, 4, 1), 5: (-1, 32, 2), 7: (-1, 128, 3)}.items():
    assert D1[row][15] == Pmul(Pscale(Fraction(s, d), Ppow(Pv("p"), j)), g1_expect), row
assert not D1[4][15] and not D1[6][15]
log("   grade-15 ideal structure: rows = (g1, g2, -(p/4)g1, 0, -(p^2/32)g1, 0, -(p^3/128)g1)")

# ---------------- F. analytic side ----------------
def inv_series(power):
    # (1 + sp t^2)^(-power) truncated through t^8, sp = p/2 + sigma*ell1
    sp = Padd(Pscale(Fraction(1, 2), Pv("p")), Pmul(Pv("sigma"), Pv("ell1")))
    out = P0()
    for n in range(5):
        c = Fraction((-1) ** n * math.comb(n + power - 1, power - 1))
        out = Padd(out, Pscale(c, Pmul(Ppow(sp, n), Pv("t", 2 * n) if n else Pc(1))))
    return out


tP = Pv("t")
sg = Pv("sigma")
A_an = Pmul(Pmul(Ppow(sg, 2), th), Padd(Padd(Pv("a1"), Pmul(Pv("a0"), tP)), Pmul(sg, Padd(Pv("aa1"), Pmul(Pv("aa0"), tP)))))
C_an = Pmul(Pmul(Ppow(sg, 3), th), Padd(Padd(Pv("c1"), Pmul(Pv("c0"), tP)), Pmul(sg, Padd(Pv("cc1"), Pmul(Pv("cc0"), tP)))))
B_an = Pmul(Pmul(Ppow(sg, 2), Pmul(th, et)), Padd(Pv("b1"), Pmul(Pv("b0"), tP)))
k_an = Pv("k0")
I1, I2, I3 = inv_series(1), inv_series(2), inv_series(3)
H = Padd(
    Pscale(Fraction(3, 4), Pmul(Pmul(Pmul(Ppow(sg, 10), tP), Pmul(A_an, C_an)), I1)),
    Pscale(Fraction(3, 8), Pmul(Pmul(Pmul(Ppow(sg, 10), Ppow(tP, 3)), Ppow(C_an, 2)), I2)),
    Pscale(Fraction(-3, 8), Pmul(Pmul(Pmul(Ppow(sg, 12), Ppow(tP, 2)), Pmul(B_an, Ppow(A_an, 2))), I2)),
    Pscale(Fraction(-1, 16), Pmul(Pmul(Pmul(Ppow(sg, 15), Ppow(tP, 4)), Ppow(A_an, 3)), I3)),
    Pscale(Fraction(5, 16), Pmul(Pmul(Pmul(Ppow(sg, 10), k_an), Ppow(B_an, 3)), I1)),
    Pscale(Fraction(5, 8), Pmul(Pmul(Pmul(Pmul(Ppow(sg, 11), tP), k_an), Pmul(B_an, C_an)), I1)),
    Pscale(Fraction(-5, 32), Pmul(Pmul(Pmul(Pmul(Ppow(sg, 13), Ppow(tP, 2)), k_an), Pmul(Ppow(B_an, 2), A_an)), I2)),
    Pscale(Fraction(5, 32), Pmul(Pmul(Pmul(Pmul(Ppow(sg, 14), tP), k_an), Ppow(A_an, 2)), I1)),
)
# h[g][j] = [sigma^g t^(j+1)] H
h = {15: {}, 16: {}}
lowH = set()
for m, c in H.items():
    d = dict(m)
    gs = d.pop("sigma", 0)
    ts = d.pop("t", 0)
    if gs < 15:
        lowH.add((gs, ts))
    if gs in (15, 16) and 2 <= ts <= 8:
        key = tuple(sorted(d.items()))
        row = ts - 1
        tgt = h[gs].setdefault(row, {})
        tgt[key] = tgt.get(key, Fraction(0)) + c
assert not lowH, ("Hshift not divisible by sigma^15", sorted(lowH)[:5])
for g in (15, 16):
    for j in range(1, 8):
        h[g].setdefault(j, {})
        h[g][j] = {k: v for k, v in h[g][j].items() if v}
log("F. universal_hshift expanded; divisible by sigma^15; h[15][*], h[16][*] extracted")


def transform(i, j):
    delta = i - j
    if delta < 0 or delta % 2:
        return P0(), P0()
    n = delta // 2
    coeff = Fraction(1)
    for idx in range(n):
        coeff *= Fraction(j, 2) + idx
    coeff /= math.factorial(n)
    coeff /= 2 ** n
    t0 = Pscale(coeff, Ppow(Pv("p"), n) if n else Pc(1))
    t1 = Pscale(2 * n * coeff, Pmul(Pv("ell1"), Ppow(Pv("p"), n - 1) if n > 1 else Pc(1))) if n else P0()
    return t0, t1


for i in range(1, 8):
    t0ii, _ = transform(i, i)
    assert t0ii == Pc(1), ("diagonal not unit", i)
log("   moving transform is lower-unitriangular (diagonal T0 = 1 for all i)")

row_ok = True
for i in range(1, 8):
    pred15 = P0()
    pred16 = P0()
    for j in range(1, i + 1):
        t0, t1 = transform(i, j)
        pred15 = Padd(pred15, Pmul(t0, h[15][j]))
        pred16 = Padd(pred16, Pmul(t0, h[16][j]), Pmul(t1, h[15][j]))
    if D1[i][15] != pred15:
        row_ok = False
        log(f"   !! grade-15 row identity fails i={i}")
    if D1[i][16] != pred16:
        row_ok = False
        log(f"   !! grade-16 row identity fails i={i}")
assert row_ok
log("   raw D1AC rows == unitriangular transform of analytic h at grades 15 and 16 (14 identities)")

half_p = Pscale(Fraction(1, 2), Pv("p"))
for kdx in range(1, 6):
    assert Padd(h[15][kdx + 2], Pmul(half_p, h[15][kdx])) == P0(), ("rec15", kdx)
for kdx in range(1, 4):
    assert Padd(h[16][kdx + 4], Pmul(Pv("p"), h[16][kdx + 2]), Pmul(Ppow(half_p, 2), h[16][kdx])) == P0(), ("rec16", kdx)
log("   denominator recurrences: h15 simple pole (L), h16 double pole (L^2)")

# ---------------- G. allocations and the terminal residue ----------------
z = Pv("z")
N15 = Padd(Pmul(h[15][1], z), h[15][2])
N16 = Padd(
    Pmul(h[16][1], Ppow(z, 3)),
    Pmul(h[16][2], Ppow(z, 2)),
    Pmul(Padd(h[16][3], Pmul(Pv("p"), h[16][1])), z),
    Padd(h[16][4], Pmul(Pv("p"), h[16][2])),
)
rho = Pv("rho")
au = Pv("au")
cv = Pv("cv")
minus2rho2 = Pscale(-2, Pmul(rho, rho))
ALLOC = {
    "plus": {"p": minus2rho2, "a1": au, "a0": Pscale(-1, Pmul(au, rho)), "c1": cv, "c0": Pmul(cv, rho)},
    "minus": {"p": minus2rho2, "a1": au, "a0": Pmul(au, rho), "c1": cv, "c0": Pscale(-1, Pmul(cv, rho))},
}
target = Pscale(Fraction(3, 2), Pmul(Pmul(Ppow(rho, 2), Ppow(cv, 2)), Ppow(th, 2)))
for deck, table in ALLOC.items():
    n15a = Psub(N15, table)
    assert n15a == P0(), (deck, "N15 not killed")
    n16a = Psub(N16, table)
    at_root = Psub(n16a, {"z": rho if deck == "plus" else Pscale(-1, rho)})
    assert at_root == target, (deck, "residue mismatch")
    free = support(at_root) - {"rho", "cv", "theta"}
    assert not free
log("G. both deck allocations kill N15; N16 at the allocated A0 root")
log("   == (3/2)*rho^2*cv^2*theta^2 identically (no aa*, cc*, b*, eta, ell1, k0 dependence), both decks")

# grade-15 exclusion dichotomy, by hand-check encoded:
#   h15_1 = (3/4) th^2 (a0 c1 + a1 c0), h15_2 = (3/8) th^2 (2 a0 c0 - p a1 c1)
assert h[15][1] == g1_expect and h[15][2] == g2_expect
log("   h15_1, h15_2 equal the two grade-15 binomials: N15=0 <=> L | A0*C0")

log("PASS-FABLE5-KGT-DRHO-D1-A2-INDEPENDENT-VERIFY")
```

Observed output (verbatim key lines):

```text
all seven frozen grade-15 rows reproduced exactly     (133/224/355/140/585/200/759 terms)
V28 rho=0 ordered-a1 grade-16 face term counts reproduced: 63/86/98/45/77/22/33
grades 0..14 vanish on the contact locus; grade-15/16 support inside the (4.2) jet set
contact g15 supports: {aaa0,aaa1,ez3,ec3(,rho)}; g16 supports subset of
  {aaa0,aaa1,az3,ac3,cs2,rs2,ez3,ez4,ec3,ec4,k,ell1,rho}; row 6 == 0
renamed contact rows == D1AC rows with p=-2*rho^2 at EVERY grade 0..16 (7x17 identities)
grade-15 ideal structure: rows = (g1, g2, -(p/4)g1, 0, -(p^2/32)g1, 0, -(p^3/128)g1)
moving transform is lower-unitriangular (diagonal T0 = 1 for all i)
raw D1AC rows == unitriangular transform of analytic h at grades 15 and 16 (14 identities)
denominator recurrences: h15 simple pole (L), h16 double pole (L^2)
both deck allocations kill N15; N16 at the allocated A0 root
  == (3/2)*rho^2*cv^2*theta^2 identically (no aa*, cc*, b*, eta, ell1, k0 dependence), both decks
h15_1, h15_2 equal the two grade-15 binomials: N15=0 <=> L | A0*C0
PASS-FABLE5-KGT-DRHO-D1-A2-INDEPENDENT-VERIFY
```

## Appendix B — V28 face byte check

Checker `cff4ea54…` rebuilds the seven grade-16 rows with the kill set
`{rs,cs,c0,c1,a0,rho}` applied at source level (equivalent by
specialization commuting with the polynomial build), parses the frozen
`aws_q/compiled/Tg16_*_q.poly` files, and compares exact term
dictionaries.  Observed: all seven match (`63/86/98/45/77/22/33` terms,
`V28-FACE-BYTES-MATCH`), and both `EVIDENCE.sha256` freezes (29 rows per
lane) rehash after remapping the recorded AWS-absolute paths at
`/source/cases/…`.
