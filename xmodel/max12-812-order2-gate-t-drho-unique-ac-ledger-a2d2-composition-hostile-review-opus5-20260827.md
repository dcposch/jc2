# Hostile review: Gate-T `D(rho*k)` unique-`AC` ledger and the `(2,4,>=3)` contact composition

Date: 2026-08-27

Reviewer: Opus5, adversarial, independent derivation.

Artifacts under review, all three hashes recomputed locally and **matching**:

```text
1d086a79b0d4e7a6a9905391dc13acf4571d766292c58c7b2f25b1c673141457
  xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-sol-20260827.md
0c124179041b1a3cc115e24d1e5bce4f7ca9edcbc0e3224c302dd20d85b8867e
  xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-replay-20260827.py
d62b3f22bcad7de1bacecfa13c455f90bd654b578dd23cc5d2439054993f76f3
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-hostile-review-opus5-20260827.md
```

The upstream correction consumed here is the erratum-controlled one, not the
withdrawn original sentence: `delta_D1` annihilates `J1+J2`, so the stage-zero
root pairs `(rs,cs)`, `(c0,c1)`, `(a0,a1)` are all zero on any such contact and
must never be substituted for the deeper shifted pairs.

## 0. Verdict summary

| Item | Verdict |
|---|---|
| Exact strict unique-`AC` ledger, `s_min`, `G`, `T`, lifecycle, well-orders | **CONFIRMED** (two required presentation edits) |
| Rings, `p0=-2*rho^2`, localizations, saturations, direction of the induced map | **GAP** (mathematics right, logical assembly and ring-naming incomplete) |
| Shifted finite-jet map through grade 18 and its completeness | **CONFIRMED** (verified exhaustively, verbatim) |
| Grade-18 actual-total custody (V33) | **GAP** (honest description, insufficient evidence; closed here by reconstruction) |
| `B22` endpoint composition and the residue `(3/2)*rho^2*cv^2` | **CONFIRMED**, and independently strengthened |
| Desk-replay evidentiary adequacy | **GAP** (the central equalities are not replayed at all) |
| Strategic scope and firewalls | **CONFIRMED** (one uncovered sub-case must be named) |

The theorem (0.1) is **true**. Every equation I tested held, and I could not
break it. What needs work is (i) how §4 assembles the logic, (ii) what the
grade-18 pin actually witnesses, and (iii) how little of the report's own
mathematics its replay touches. I also found that the exclusion is
substantially *cheaper* than the report claims: it needs neither the Hensel
root series, nor the moving connection, nor the deck involution, nor the
localizations at `k`, `au`, `J`, and it can be certified without any
allocation case split. That is a strengthening, not a refutation.

## 1. What I did, and what the producer replay does not do

I re-ran the producer replay: it prints
`PASS-DRHO-UNIQUE-AC-LEDGER-A2D2-COMPOSITION-DESK-REPLAY` in 0.03 s and all
31 of its pinned digests match on disk. All five §1 history digests match on
disk as well.

Then I read the machinery line by line and rebuilt both sides myself, with my
own polynomial and truncated-series arithmetic over `Fraction`, importing no
campaign module (the single exception is the frozen support miner's pure
`enumerate_primitives`, used only as a cross-check against my own
re-derivation of the same inventory):

1. `prolong_boundary_g18_v33.py` (V33), `prolong_boundary_g16_v28.py` (V28),
   `export_allrows_g13_g14_v20.py` (V20), `replay_row5_grade14.py` (the base
   series primitives), `census_j2_typed_v23.py` (the parser and
   `sigma_weight`), `compile_local_row.py` (the `B22` block),
   `compile_r1_d1_ac.py` (`source_coefficients`), and
   `compile_square_load_ladder.py` (`tail_text`, `NAMES`, `WEIGHTS`);
2. rebuilt the general-`rho` actual-total source and all seven rows to grade
   18 from the 569-tail JSON, and reproduced the **frozen general-`rho`
   grade-15 rows** and the **frozen `rho=0` face rows at grades 16, 17 and
   18**;
3. rebuilt the `B22` branch from `compile_local_row.block(2,2)`'s literal
   source arguments and checked
   `delta_22([sigma^g]Phi_l^tot)=[sigma^g]Phi_l^B22` at **every** grade
   `0..18` for all seven rows, with nineteen mutation controls;
4. re-derived the four polar primitives from the four-summand binomial
   structure, independently of the miner;
5. recomputed `lambda(sigma)`, both allocations, `Psi`, and the terminal
   residue exactly, in `Q(lam)[...]` with `lam` inverted;
6. produced a case-free syzygy certificate for the same exclusion in pure
   actual-total coordinates.

The consolidated verifier is

```text
eaf86e57a02f0fa8dce20b0e1ac81acdd168a8d5aec477a1d380d47269dbeaee
```

(142 s measured, desk scale, pure Python). Its full output is reproduced in the
relevant sections and the source is Appendix A. No AWS, no CAS, no web sweep,
no ledger edit, no `jc2-lean` access; only this file was written.

## 2. Attack 1 — the exact unique-`AC` ledger

### 2.1 The criterion, `s_min`, `G`, `T` and the eighteen baselines all hold

The report's criterion (2.1) is not merely asserted here; I checked it against
its actual definition. Strict unique-`AC` means `AC` is the **strict** minimum
of the five unit-load lower-hull weights
`AC=a+c, C2=2c, R3=3r, RC=1+r+c, A2=4+2a`. Over the whole box
`1<=a<=24, 3<=c<=39, 2<=r<=39` (25 704 points):

```text
   (d in {1,2,3}, s>=0, a+3s>d)  ==  (a+c < min(2c,3r,1+r+c,4+2a))     0 disagreements
```

So (2.1) **is** strict `AC`-minimality, not a convenient restatement.

From the same search, `s_min` and the closed forms reproduce exactly:

```text
   d=2: s_min=1 for a in {1,2};    s_min=0 for a>=3
   d=3: s_min=1 for a in {1,2,3};  s_min=0 for a>=4
   d=1: s_min=0 for every a>=2  (a=1 has c=2<3 and is out of the fan)
   G = 10+2a+d = 10+a+c ;  T = G+d = 10+2a+2d  (= the miner's target_grade)
```

and the eighteen `(a,d,r_floor)` baselines of (2.4) reproduce verbatim in
order. The eleven/one/two/one/one/two/infinite lifecycle partition is a
faithful transcription of the frozen `d=2,3` audit
(`cdd23058…`, whose table carries the *same* promotion and review digests),
extended by one correct update: the `(8,3,8)` target-shadow review
(`02cbae00…`) is `CONFIRMED`, and the only `a=8,d=3` promotion on disk is
`max12-812-order2-square-d1-a8d3-moving-connection-rankjump-route-promotion-20260826.md`,
whose own status line reads **"PROMOTED ROUTE FALSIFICATION ONLY"**. So the
report's "`CONFIRMED`, but no narrow promotion" is exactly right, and its
refusal to call the union promoted is correct.

I also confirmed the `d=1` route: the union promotion `85533441…` composes the
`a=2..5`, `a=6,7`, `a=8`, `a=9`, `a>=10` promotions named in its own custody
block, and the `a>=10` ceiling promotion covers `a>=10, c>=a+1, r>=a`, i.e.
all of `d=1,2,3`.

### 2.2 Both well-orders do select `(2,4,3)` — but "first missing contact" is false

Over the whole fan (`d=1,2,3`, `a<=60`), with lexicographic
`K_val=(a,c,r_floor)` and `K_grade=(G,a,c,r_floor)`:

```text
   K_val   : first cell strictly after (2,3,2) is (2,4,3), G=16, T=18 ; then (2,5,3), G=17, T=20
   K_grade : first cell strictly after (2,3,2) is (2,4,3), G=16, T=18 ; then (2,5,3), G=17, T=20
```

confirming (3.2) and the §7 successor. The `K_grade` tie at `G=17` between
`(2,5,3)` and `(3,4,3)` breaks toward `(2,5,3)`, agreeing with `K_val`.

Now the honest part and the dishonest part. In **both** orders exactly two
cells precede `(2,3,2)`:

```text
   (a,c,r_floor)=(1,3,2)  d=2  G=14  T=16
   (a,c,r_floor)=(1,4,2)  d=3  G=15  T=18
```

and by the report's own §2 ("the only banked total contact was `(2,3,2)`")
and §7.1, both are still untransported. §0's status line is correctly
qualified ("AFTER `(2,3,>=2)`") and §3's body names both cells. But:

- **§1 line 80** says the novelty is "the finite-jet total/D1 composition for
  **the first missing contact** (0.1)". That is **false**. `(1,3,2)` is
  missing and strictly earlier in both registered orders.
- **§3's heading (line 162)**, "The minimal uncovered contact", is false for
  the same reason.

This is not cosmetic. `(1,3,2)` has terminal grade `T=16`, so it needs *less*
custody than the contact actually chosen, and the `a=1,d=2` `B22` block has
the same shape as `B22` (`primitive_count=6, maxpole=2`, no `RA2` family).
`(1,4,2)` has `T=18` — the same grade — but it is the `E` negative-control
block with `maxpole=3` and a second dangerous `RA2` family, so it genuinely
is a harder import. A reader budgeting from §1 would not learn either fact.

### 2.3 A live notational trap: `(1,3,2)` means two different cells

§2 declares the ledger tuple to be `(a,d,r_floor)`; §3 switches to
`(a,c,r_floor)`. Both conventions are labelled, but the *same literal triple*
`(1,3,2)` occurs in both and denotes different cells:

```text
   in (2.4) and the lifecycle table   (1,3,2) = a=1, d=3, c=4   (the E / pole-three cell)
   in §3                              (1,3,2) = a=1, c=3, d=2   (the low-a6 cell)
```

The lifecycle table's row "`(1,3,2)` | promoted exceptional pole-three
endpoint" is correct in *its* convention and wrong in §3's. This is exactly
the `k`/`k0`/`k10` class of naming trap this campaign has hit before, and it
should be removed before promotion.

**Verdict, ledger: CONFIRMED.** The arithmetic, the `s_min` table, `G`, `T`,
the eighteen baselines, the lifecycle routing and both well-order selections
are exactly right and independently reproduced. Two edits are required
(§2.2, §2.3).

## 3. Attack 2 — rings, maps, opens and saturations

### 3.1 What checks out

`p0 -> -2*rho^2` is what V33 literally builds
(`p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))`),
with `p[j] = 2*ell_j` for `j>=1`; `c = shift(Cs,2)`;
`r = (p^2 + shift(Rs,2))/4`; `n3=shift(Az,3)`, `n2=shift(Ac,3)`,
`n1=shift((p*Az+Ez)/2,3)`, `n0=shift((p*Ac+Ec)/2,3)`; loads at
`sigma^4, sigma^12, sigma^20`. `I^tot_18` is the literal seven-row ideal
through grade 18 and `S_tot={(rho*k*J)^n}` is a multiplicative set. All
correct.

`B_22 = D_22/H_root` with

```text
H_root=(p+2*lam^2, 2*lam*rho1+ell1, rho1^2+2*lam*rho2+ell2)
```

is exactly the `sigma^0, sigma^1, sigma^2` coefficient set of
`lambda(sigma)^2+P(sigma)/2` for `lambda=lam+rho1*sigma+rho2*sigma^2`,
`P=p+2*ell1*sigma+2*ell2*sigma^2` — I recomputed all three. The frozen
compiler's `RootIdeal` is those generators for grades `1..rootmax=2` plus
`ilam*lam-1`, so the report's `lam`-localized description is faithful. The
factors `lam,k0,au,cv` have the meanings claimed; the closed `R` tail is real:
neither `b0` nor `b1` is inverted anywhere, and neither occurs in the
certificate.

The staged Rees saturations `K^rho_(m,f)` with `f in {rs,cs,c0,c1}` at stage
one and `f in {a0,a1}` at stage two are exactly the list (4.6) of the Kummer
report; the claim that (4.7) is a *downstream contact* saturation and not a
statement about those charts or the terminal receiver is correct and important.

### 3.2 Three real defects

1. **A dangling cross-reference.** (4.7) says "adjoin `au,cv` and one of the
   allocation ideals in **(5.2)**". There is no equation (5.2) in the
   document; §5 has only (5.1). The allocation ideals are (6.2). A reader
   cannot assemble (4.7) as written.

2. **The ambient ring of (4.7) is never named.** `I^tot_18` lives in
   `U_18^rho`; `H_root` is written in `D_22`'s variables `p, lam, rho1, rho2`;
   `Alloc_epsilon` relates `A0, C0` to `au, cv`. The only consistent reading
   is `U_18^rho[au,cv,lam,rho1,rho2]` with `p := -2*rho^2`, so that
   `p+2*lam^2` becomes `2*(lam^2-rho^2)`. The report never says this, and the
   reader is instead pointed at `delta_22^+ : U_18^rho -> B_22[1/(...)]`,
   which is a different ring.

3. **The displayed ring map runs the wrong way for the conclusion, and the
   report does not say what fixes it.** `delta_22^+` induces
   `Spec(B_22[1/(lam*k0*au*cv)]) -> Spec(U_18^rho)`. Emptiness of the source
   of a scheme map says nothing about the target — this is precisely the
   erratum's own item 5 ("it yields only the forward implication … no
   converse"). §4 and §6 as written therefore look like they infer endpoint
   emptiness from a reversed ring map.

   The report is nevertheless **not** guilty of that inference: §5's sentence
   "every arbitrary total DVR arc satisfying (0.1) factors through (4.3) at
   the finite row level: discarded later jets cannot enter grades 16–18" is
   the arcwise statement, and it is correct. I verified something sharper
   which makes the point unmistakable and which the report should simply
   state:

   > On the contact (0.1) the actual-total row coefficients at grades 16, 17
   > and 18 involve **exactly** the eighteen jets
   > `rho, ell1, ell2, aaa1, az3, az4, aaa0, ac3, ac4, ez4, ez5, ez6, ec4, ec5, ec6, cs3, rs3, k`,
   > and `delta_22` restricted to those eighteen is a **bijective renaming**
   > with nonzero rational scalars. Hence the total and `B22` grade-16..18
   > coefficient ideals are carried onto one another by a ring
   > **isomorphism**, and emptiness transfers in both directions.

   That is one sentence, it is verified below, and it removes the direction
   worry entirely. Without it §4 is a genuine hole.

4. **Minor, but worth fixing:** §6 concludes "Hence each saturated ideal
   `E_22^epsilon` in (4.7) is the unit ideal, proving (0.1)." Strictly,
   (4.7) is the unit ideal *on the open where `au*cv != 0`*; the points with
   `au=0` or `cv=0` are killed by the degree argument in the preceding
   paragraph, not by (4.7). The two halves must be assembled explicitly.

**Verdict, ring/map/saturation: GAP.** No mathematical error; the ring naming,
the (5.2) reference, and the direction argument are incomplete as written.
The repair is the boxed sentence above plus two cross-reference fixes.

## 4. Attack 3 — the shifted finite-jet map through grade 18

### 4.1 Independent derivation of the map

`compile_r1_d1_ac.source_coefficients(pp,az,ac,cz,cc,rz,rc)` sets
`kc = sigma^2*rz`, `kr = pp^2/4 + sigma^2*rc`, `n3=sigma^3*az`,
`n2=sigma^3*ac`, `n1=sigma^3*(pp*az/2+cz)`, `n0=sigma^3*(pp*ac/2+cc)`, and
then the *same seven formulas* V33 uses. So the two branches differ only in
their seven input series, and the dictionary is forced:

```text
   Cs  <-> rz ,      Rs <-> 4*rc ,      Az <-> az ,  Ac <-> ac ,
   Ez  <-> 2*cz ,    Ec <-> 2*cc .
```

`compile_local_row.block(2,2)` feeds `rz=sigma^3*b1`, `rc=sigma^3*b0`,
`az=sigma^2*(a1+sigma*a1_1+sigma^2*a1_2)`, `ac` likewise,
`cz=sigma^4*(c1+sigma*c1_1+sigma^2*c1_2)`, `cc` likewise, and constant loads
`k0,k60,k20`. Substituting gives exactly (4.3):

```text
   cs3 -> b1 ,  rs3 -> 4*b0 ;
   aaa1 -> a1D , az3 -> a1D_1 , az4 -> a1D_2 ;   aaa0 -> a0D , ac3 -> a0D_1 , ac4 -> a0D_2 ;
   ez4 -> 2*c1D , ez5 -> 2*c1D_1 , ez6 -> 2*c1D_2 ;  ec4 -> 2*c0D , ec5 -> 2*c0D_1 , ec6 -> 2*c0D_2 ;
   k -> k0 , k6 -> k60 , k2 -> k20 ,  rho -> lam , ell1,ell2 retained.
```

and (4.5) verbatim: `c_total=sigma^5*b1`, `r_total=P^2/4+sigma^5*b0`,
`n3=sigma^5*A_z`, `n2=sigma^5*A_c`, `Ez/2=sigma^4*C_z`, `Ec/2=sigma^4*C_c`.
The factors `2` and `4` are the ones `source_coefficients`'s own docstring
inserts. **Every index and factor in (4.3) is correct.**

### 4.2 The row identity, at every grade

Building both branches from the frozen 569 tails:

```text
   delta_22 carries all 7 total F-series and all 3 load series onto the B22 ones     PASS
   delta_22([sigma^g]Phi_l^tot) = [sigma^g]Phi_l^B22  for l=1..7 and every g=0..18   PASS
```

### 4.3 Completeness — proved, not asserted

The report's §5 says discarded jets "cannot enter grades 16–18" and offers the
`B22` inventory (5.1) as the reason. That is an inventory sentinel, not a
proof. I proved it directly. Imposing only the contact conditions
(`a1=aa1=a0=aa0=0`, `c1=e1=ee1=ez3=c0=e0=ee0=ec3=0`,
`cs=cs1=cs2=rs=rs1=rs2=0`) and leaving *every* later jet symbolic
(`ell3..ell18`, `cs4..`, `rs4..`, `az5..`, `ac5..`, `ez7..`, `ec7..`,
`k1, k2c, k10_3.., k6, k6_1.., k2`):

```text
   all seven rows vanish identically at every grade 0..15                  PASS
   variables occurring at grades 16,17,18:
      aaa0 aaa1 ac3 ac4 az3 az4 cs3 ec4 ec5 ec6 ell1 ell2 ez4 ez5 ez6 k rho rs3
   this set is EXACTLY the 18 jets of (4.3) — no more, no fewer            PASS
```

So no later jet, no lower source jet and no connection jet can contribute, and
conversely the map retains nothing superfluous. The producer's kill list (4.4)
is *incomplete as a specification* — it never names `k1, k2c, k10_i, k6_i` —
but the omission is covered by its own clause "later jets that cannot enter
through grade 18", which is now verified rather than assumed.

### 4.4 The shifted pairs are the deeper ones, and the stage-zero pairs are dead

(6.1) is right. With `A0(z)=aaa1*z+aaa0`, `C0(z)=(ez4*z+ec4)/2`,
`R0(z)=cs3*z+rs3/4`, the root values at `z=+/-rho` are exactly the report's
`A0plus/minus`, `C0plus/minus`, `R0plus/minus`. The stage-zero pairs
`(rs,cs)`, `(c0,c1)`, `(a0,a1)` are, by the definition of this contact,
identically zero — they are six of the eighteen jets the contact kills. The
report's explicit warning at (6.1) is therefore not decorative: substituting
them would produce the trivial map the upstream review refuted. **The
correction is consumed correctly.** (Index bookkeeping also matches the
erratum's "shifted again for later contacts": `(2,3,>=2)` used
`rs2/cs2, ec3/ez3, aaa0/aaa1`; this contact uses `rs3/cs3, ec4/ez4`, with the
`A` pair unchanged because `ord(A)=2` in both.)

### 4.5 Which clauses are load-bearing (the analogue of the upstream §4.6 table)

```text
   clause of (4.3)                 detectable at g16   g17                 g18
   rs3 -> b0  (drop factor 4)             NONE          NONE               rows 1,2,3,5,7
   ez4 -> c1  (drop factor 2)         rows 1,2,3,5,7  rows 1,2,3,5,7       rows 1,2,3,4,5,7
   ell1 -> 0  (moving term)               NONE        rows 2,3,5,7         rows 2,3,5,7
   ell2 -> 0                              NONE          NONE               rows 2,3,5,7
   k -> 0                                 NONE          NONE               rows 1,2,3,5,7
   cs3 -> 0  /  rs3 -> 0                  NONE          NONE               rows 1,2,3,5,7
   az3 <-> ac3  (transposition)           NONE        rows 1,2,3,5,7       rows 1,2,3,5,7
   k6 -> 0                                NONE          NONE               NONE
   k2 -> 0                                NONE          NONE               NONE
```

Two honest consequences the report should state: the `k6 -> k60` and
`k2 -> k20` clauses of (4.3) are **vacuous at this contact** (neither load
reaches grade 18 in any row), exactly as the four targets were vacuous at
grade 15 upstream; and unlike the previous contact, the factor `4` and the
moving term `2*sigma*ell1` *are* testable here.

**Verdict, finite-jet completeness: CONFIRMED.** Verbatim correct, and the
completeness claim is now proved exhaustively rather than inferred from an
inventory.

## 5. Attack 4 — grade-18 custody (V33)

### 5.1 What V33 actually does

Reading `prolong_boundary_g18_v33.py`: it loads V20's base module (pinned),
sets `base.MAX_DEGREE = 18` — which is honoured, because every series
primitive in `replay_row5_grade14.py` reads the module-level `MAX_DEGREE` at
call time — builds the general-`rho` source series, builds
`totals = {row: v28.build_row(...)}` for all seven rows, and only then defines
`killed = parser.J1 | frozenset({"a0","rho"})`. It bridges 56 upstream
objects (42 V23 `a1_ordered` charts, plus V28's grade 16 and V30's grade 17,
each hash-checked) and serializes only `face[row] = specialize(totals[row][18], killed)`.

So the report's §5 characterisation is **accurate on every point**: V33 does
construct the unspecialized general-`rho` rows through grade 18 before its
unrelated `rho=0` ordered-`a1` face, only the face rows are serialized, and the
report explicitly declines to call those bytes general-`rho` rows. There is no
relabeling anywhere. Custody is also *better closed* than in the upstream
case: the seven `Tg18_*_q.poly` digests are not in the report, but they are in
`aws_q/compiled/result.json`, which **is** pinned, and I confirmed all seven
(and all seven `_at_point_` files) match on disk.

### 5.2 What it does not certify — quantified

The face kills `rho, a0, c0, c1, cs, rs`. Of the eighteen live jets, it kills
exactly one: `rho`. That sounds mild, and it is not:

```text
   contact rows at grade 18: 77 terms in total
                             28 rho-free  (a rho=0 face can see these)
                             49 invisible (64%)
   the terminal residue is (3/2)*rho^2*cv^2 : rho-exponent 2 -> entirely invisible
```

`rho` enters the whole construction only through `p[0]=-2*rho^2`, so the face
is precisely the `p[0]=0` slice. **The frozen V33 bytes are blind to every
term that carries the exclusion.** V33's contribution is therefore *code-path*
custody (a hash-pinned source file that provably builds the right object),
plus *slice* custody at grades 16–18. It is not row custody for the statement
being proved. The report's own phrase — "V33 supplies current custody that the
actual total producer follows that construction through grade 18" — is
defensible but should say "code-path and `rho=0`-slice custody".

### 5.3 What I reconstructed instead

I closed the gap by content, on both sides of the missing anchor:

```text
   all seven frozen GENERAL-rho grade-15 rows (V22 r1) reproduce exactly     PASS
      (133, 224, 355, 140, 585, 200, 759 terms; every term rho-even, max rho exponent 8)
   all seven frozen rho=0 face rows at grade 16 (V28) reproduce exactly      PASS
   all seven frozen rho=0 face rows at grade 17 (V30) reproduce exactly      PASS
   all seven frozen rho=0 face rows at grade 18 (V33) reproduce exactly      PASS
      (153, 244, 327, 174, 358, 140, 251 terms — matching the replay's expected counts)
```

One code path, one source-series definition: it matches frozen **general-`rho`**
bytes at grade 15 and frozen **face** bytes at grades 16, 17 and 18. I also
found and verified a structural invariant that is worth banking on its own and
that neither the report nor the replay uses:

> **Isobaric grading.** Give weights `rho:1, ell_j:2, cs_j:3, rs_j:4,
> (a1,aa1,aaa1,az_j):5, (a0,aa0,aaa0,ac_j):6, (c1,e1,ee1,ez_j):7,
> (c0,e0,ee0,ec_j):8, k10-jets:2, k6-jets:6, k2:10`. Then every actual-total
> row `Phi_l` is **homogeneous of degree exactly `12+l`** — the tail weight.

I verified this for all seven rows through grade 18 and, independently, for
all 21 frozen face polynomials. It is a cheap, byte-level fail-closed test
that any future exporter should carry.

This is derived-here evidence and must be labelled as such. It is not a
substitute for a frozen general-`rho` grade-18 export, and I searched: none
exists (V22 stops at `NEW_GRADE=15`; V28/V30/V33 are all `rho=0` faces).

**Verdict, grade-18 custody: GAP.** The producer's *description* is honest and
precise; the *evidence* it points at cannot see the load-bearing content. This
review closes the gap by independent reconstruction, at derived-here strength.
The report's own §7 stop rule (`ACT-TOT-G20` for the next contact) should be
applied retroactively as `ACT-TOT-G18-GENERAL-RHO` and named as an open
custody item rather than treated as discharged.

## 6. Attack 5 — the `B22` endpoint

### 6.1 Inventory, primitives, root, allocations, functional, residue

I re-derived the polar inventory from the four-summand binomial structure
(`alpha in {3/2,5/4,3/4,1/4}`, four atoms, `pole = denominator - 4*alpha`)
without using the miner, then cross-checked against the miner's own pure
function:

```text
   grade 16  coeff 3/4    pole 1   AC
   grade 18  coeff 5/32   pole 1   k*A^2
   grade 18  coeff 5/8    pole 1   k*R*C
   grade 18  coeff 3/8    pole 2   C^2
   primitive_count = 4, maxpole = 2, one dangerous family, pad=1 sentinel stable
```

exactly the report's (5.1) and (6.4), and exactly the frozen
`source_inventory.json` block. Then:

```text
   (6.3) lambda0=eps*rho, lambda1=-ell1/(2 lambda0), lambda2=-(ell2+lambda1^2)/(2 lambda0)
         solve lambda(sigma)^2+P(sigma)/2 = 0 through sigma^2                       PASS
         (rho1 = -(1/2)*ell1/lam ; rho2 = -(1/2)*ell2/lam - (1/8)*ell1^2/lam^3)
   (6.2) both allocations multiply to au*cv*L, L=z^2-rho^2                          PASS
   (6.5)/(6.6) Psi = Phi4 + eps*lambda(sigma)*(Phi3+(P/4)*Phi1):
         [sigma^16]Psi = [sigma^17]Psi = 0 and [sigma^18]Psi = (3/2)*rho^2*cv^2
         for BOTH orientations                                                      PASS
```

`Psi` is not vacuous: replacing `P/4` by `P/2` or by `0` destroys the grade-17
vanishing. Rows 1, 3, 4 are target-free through 18 (rows 1 and 3 have zero
target identically; row 4's target starts at `sigma^32`) — in fact all seven
rows are, since the earliest target is `sigma^28`.

### 6.2 The residue is a unit on a strictly larger open than claimed

```text
   variables occurring in [sigma^18]Psi :  cv, lam   only
```

The residue is independent of `au`, of `k0` (I checked directly: setting
`k0:=0` leaves it unchanged), of `b0, b1` and of every deeper `A`/`C` jet. So
(6.6) is a unit on `D(rho*cv)`, hence certainly on the report's
`D(rho*k*J*au*cv)`; the report's "the reviewed compiler needs only
`lam,cv,k0`" over-counts by one factor (the frozen compiler's `Unit` ideal
carries a superfluous `ik0*k0-1`). `D(rho*k)` in the headline is inherited
from the standing unit-`k10` gate, not required by the endpoint.

### 6.3 The one gap in §6's prose

"Since `L` is squarefree on `D(rho)` and the exact leading `A0,C0` are nonzero
**linear** polynomials, the exhaustive allocations are (6.2)." Linearity is a
*consequence*, not a hypothesis, and the report asserts it. The missing
sentence:

> `ord(A)=2` and `ord(C)=4` give `A0 != 0` and `C0 != 0`, both of degree `<=1`
> in `z`. From `L | A0*C0` with `deg L = 2` we get `A0*C0 != 0`, so
> `deg(A0*C0) = 2` and both factors have degree exactly 1; `L` squarefree on
> `D(rho)` then forces the two opposite allocations, with `au != 0`, `cv != 0`.

I checked the degenerate branches: `aaa1=0, aaa0!=0` forces `C0=0`
(contradiction), and a same-root allocation is already killed at grade 16 —
under `A0=au(z-rho), C0=cv(z-rho)` one gets `[sigma^16]Phi1 = -(3/2)*au*cv*rho`,
nonzero on `D(rho)`. So (6.2) really is exhaustive.

### 6.4 The endpoint is much cheaper than the report makes it look

Two findings, both strengthenings.

**(a) A single raw row suffices.** On this contact, row 4 is *identically zero*
at grades 16 and 17 and has just two terms at grade 18:

```text
   [sigma^18]Phi4 = (3/32)*(ec4^2 + rho^2*ez4^2)  =  (3/16)*(C0(rho)^2 + C0(-rho)^2)
```

Under either allocation this is `(3/4)*rho^2*cv^2`, already a unit. The
`lambda`-part of `Psi` contributes an equal amount, which is the whole origin
of the `(3/2)` in (6.6): `Psi`'s residue is exactly twice row 4's. The moving
root series, `rho1`, `rho2`, `H_root`'s second and third generators, `ell1`,
`ell2` and the deck involution do **no work** at this contact.

**(b) No case split is needed at all.** Write

```text
   g1 = [sigma^16]Phi1 = (3/8)*(aaa0*ez4 + aaa1*ec4)
   g2 = [sigma^16]Phi2 = (3/8)*(aaa0*ec4 + rho^2*aaa1*ez4)
   g4 = [sigma^18]Phi4 = (3/32)*(ec4^2 + rho^2*ez4^2)
   D  = rho^2*ez4^2 - ec4^2
```

Then, verified exactly:

```text
   ez4*g2 - ec4*g1        =  (3/8)*aaa1*D
   ec4*g2 - rho^2*ez4*g1  = -(3/8)*aaa0*D
   (32/3)*g4 + D = 2*rho^2*ez4^2 ,   (32/3)*g4 - D = 2*ec4^2
```

so `aaa1*rho^2*ez4^2, aaa1*ec4^2, aaa0*rho^2*ez4^2, aaa0*ec4^2` all lie in
`(g1,g2,g4)`. On any point with `rho != 0` and `(aaa0,aaa1) != (0,0)` this
forces `ez4 = ec4 = 0`, i.e. `ord(C) > 4`, contradicting `ord(C)=4`. No
allocation split, no Hensel root, no deck, and nothing inverted except `rho`.
(The exclusion is still set-theoretic/arcwise — the step from
`aaa1*ez4^2 = 0` to `ez4 = 0` is a point statement — which is exactly the
caveat the report already makes.)

`g1, g2` are `(3/4)` times the two coefficients of `A0*C0 mod L`, so the
report's reading of the grade-16 primitive is precisely right; and the fact
that rows 3, 5, 7 at grade 16 are `-(p/4), -(p^2/32), -(p^3/128)` times row 1
while rows 4, 6 vanish is the same deflation the upstream review found at
grade 15, unreported here.

**Verdict, `B22` endpoint composition: CONFIRMED**, with the §6.3 sentence
added, and with the §6.4 simplification available as a much shorter and
strictly more robust certificate.

## 7. Attack 6 — evidentiary value of the desk replay

The replay is materially better than the upstream one on custody. It does real
work in three places:

- `custody_check` hashes 31 files, all matching, including the V33 producer,
  its `FREEZE.sha256`, both result JSONs, the `B22` compiler, its `FREEZE` and
  `EVIDENCE` manifests, the frozen `source_inventory.json`, and the frozen run
  transcript;
- `construction_path_check` **reads the pinned V33 bytes** and requires eight
  literal source snippets (`base.MAX_DEGREE = 18`, the `-2*rho^2` constant,
  the moving `ell` loop, the `c`/`r`/`n3` shifts, the seven-row build, and the
  face definition), and enforces
  `index(seven_rows) < index(face_after_totals)`. That is genuine evidence for
  the "general-`rho` before the face" claim;
- it also checks V33's status string and the seven grade-18 term counts
  against the pinned `compiled/result.json`, the `B22` inventory block against
  the pinned `source_inventory.json`, and eight markers against the pinned
  frozen stdout.

What it does **not** do:

1. **`finite_jet_map_check` verifies nothing.** `mapping` and `vanished` are
   hardcoded dictionaries never compared to any file or to any computation.
   Worse, its one apparent assertion is a tautology:

   ```python
   exponents = {"total_c_from_D1_R": 2 + 3, ...}
   if exponents != {"total_c_from_D1_R": 5, ...}: raise AssertionError(exponents)
   ```

   `2+3` against `5`. The central mathematical content of the report — the map
   (4.3)/(4.4) and the row identity (4.6) — is not touched by a single line of
   the replay.

2. **The endpoint equality (6.6) is never computed.** `hensel_and_deck_check`
   checks the Hensel relations and the allocation product at two numeric
   points (real, but elementary), then writes
   `residue = Fraction(3,2)*lam*lam*cv*cv` — the answer, typed in — and only
   asserts it is nonzero. It reads no row, forms no `Psi`, and would pass
   identically if the true residue were `0` or `(7/5)*rho^4*au^2`.

3. **The four polar primitives (6.4) are not enumerated**, only their count is
   cross-checked against the frozen inventory.

4. **`coverage_ledger_check` is self-contained.** `route()` is a hardcoded
   table compared to nothing on disk; `endpoint()`'s closed forms and
   `least_s()`'s search do genuinely cross-check each other, which is worth
   something, but no lifecycle claim is checked against a lifecycle artifact.

5. The frozen transcript marker `B22_LOCAL_COEFFICIENT=3/2*lam^2*cv^2` that
   the replay greps for is a **producer-authored literal** in the generated
   `.sing` file, not an engine-computed value. The data-bearing markers are
   `B22_BOTH_ORIENTATIONS=1` (a computed `int`, which does contain the residue
   equality) and `B22_ENDPOINT=...` behind a `quit`-guard. The replay treats
   all eight markers alike.

Everything in items 1–3 is supplied by this review's verifier
(`29b6d851…`), which computes both branches from the frozen tails, checks
(4.6) at every grade with nineteen mutation controls, re-derives (6.4), and
recomputes (6.6) symbolically for both orientations.

**Verdict, replay adequacy: GAP.** Real custody and a real V33 construction-path
check; zero coverage of (4.3), (4.4), (4.6), (6.4) and (6.6). The tautology in
`finite_jet_map_check` should be removed or replaced with the row comparison.

## 8. Attack 7 — scope firewalls

I checked each firewall against the artifacts rather than against the report.

- **One contact exclusion, not the unique-`AC` fan.** §7.1 states this
  correctly, and my §2.2 finding *strengthens* the fence: two strictly earlier
  cells remain untransported, and the report must not be read as an induction
  base for a sweep.
- **Not the generic-square cover.** Correct; strict unique-`AC` is one part,
  and §7's list of untouched cells (`C2, R3, RC, A2`, equality intersections,
  `RA2=A2=R3`, exact-square zero-normal receiver, positive-order loads,
  `V(k)`, staged terminal receiver) is accurate.
- **Not a Rees/terminal-receiver theorem.** §4's last paragraph explicitly
  says (4.7) is a downstream contact saturation and not a statement about the
  six `K^rho_(m,f)` charts or the terminal receiver. Correct, and consistent
  with the erratum's item 5.
- **Ramified fibre.** §8 is right: (4.3), (6.1) and (6.2) use the inverse root
  transform only on `D(rho)`; the residue is `(3/2)*rho^2*cv^2`, which is the
  first thing to die at `rho=0`; the four `J1` charts, two `J2` charts and the
  separate terminal receiver over `rho=0` are untouched.
- **`G2-PSC` / `G2-BD`.** §8's definitions match `ladder/REDUCTION.md` §7.1
  verbatim, including the "no established implication in either direction"
  disjointness. The added sentence "a reviewed local endpoint cannot be used
  backward as a source-to-landing theorem" is correct and worth keeping.
- **Gate T, order two, maximum twelve, `(8,12)`, JC2.** None follows; §10's
  denial list is complete and I found no sentence in the report that leaks
  past it.

**One sub-case must be named.** The theorem is `ord(R)>=3`. The remaining
sub-case of the *same* `(ord A, ord C) = (2,4)` contact is `ord(R)=2`, where

```text
   AC=6, C2=8, R3=6, RC=7, A2=8
```

so `AC` **ties** `R3`: it is an `AC=R3` equality face, outside the strict cell
by construction (the frozen `d=2,3` audit already calls `(a,d)=(2,2), s=0` an
equality face). §7 does say "every equality intersection … remain separate",
but a reader can easily take (0.1) for "the `ord(A)=2, ord(C)=4` contact is
closed". It is not; `ord(R)=2` is open and belongs to a different fan cell.

**Verdict, strategic scope: CONFIRMED**, with the `ord(R)=2` sub-case named
explicitly.

## 9. Strongest exact surviving theorem, and the smallest repair

The theorem is not too strong. It survives verbatim, and I can state it in a
sharper and cheaper form.

> **`KGT-DRHO-UAC-A2D2` (verified).** Let `k` be a field of characteristic
> zero and `V` a normalized DVR with uniformizer `sigma`. In the Kummer total
> source `p0 = -2*rho^2`, after the reviewed generic-square first-normal,
> half-weight and exact reduced `M=0` gates with unit leading `k10`, there is
> no total-source arc with
>
> ```text
> ord(A)=2 ,  ord(C)=4 ,  ord(R)>=3 ,  rho != 0 .
> ```
>
> Proof data (all derived here from the frozen 569 tails, and equal under the
> bijective renaming (4.3) to the frozen `B22` block): on this contact all
> seven rows vanish identically at grades `0..15`, and
>
> ```text
> [sigma^16]Phi1 = (3/8)*(aaa0*ez4 + aaa1*ec4)
> [sigma^16]Phi2 = (3/8)*(aaa0*ec4 + rho^2*aaa1*ez4)
> [sigma^16]Phi4 = [sigma^17]Phi4 = 0
> [sigma^18]Phi4 = (3/32)*(ec4^2 + rho^2*ez4^2)
> ```
>
> With `A0=aaa1*z+aaa0`, `C0=(ez4*z+ec4)/2`, `L=z^2-rho^2`, the two grade-16
> coefficients are `(3/4)` times the coefficients of `A0*C0 mod L`, and
> `[sigma^18]Phi4 = (3/16)*(C0(rho)^2+C0(-rho)^2)`. The three explicit
> syzygies of §6.4(b) put `aaa1*rho^2*ez4^2`, `aaa1*ec4^2`,
> `aaa0*rho^2*ez4^2`, `aaa0*ec4^2` in the ideal, so `rho != 0` and
> `ord(A)=2` force `ord(C)>4`. Equivalently, via the two allocations
> `A0=au(z∓rho), C0=cv(z±rho)`, the residue is `(3/4)*rho^2*cv^2` from row 4
> alone, or `(3/2)*rho^2*cv^2` from the report's `Psi`.
>
> The exclusion is arcwise/set-theoretic. It needs `rho != 0` and nothing
> else inverted: not `k`, not `J`, not `au`, not `cv`, not `b0`, not `b1`.
> It does **not** cover `ord(R)=2` (an `AC=R3` equality face), any other
> `(a,c)` cell, any Rees chart, the terminal receiver, or `rho=0`.

The smallest repair to the producer document is six edits; none changes a
computation.

1. **§1 (line 80) and the §3 heading (line 162):** replace "the first missing
   contact" / "The minimal uncovered contact" with "the first missing contact
   at or after `(2,3,>=2)`", and add one sentence: "The two strictly earlier
   untransported cells are `(a,c,r)=(1,3,2)` (`T=16`, low-`a6` block shape)
   and `(1,4,2)` (`T=18`, the `E` pole-three block); the first is not harder
   than this one and is deferred for scheduling reasons only."
2. **§2/§3:** use one tuple convention throughout, or annotate every triple.
   As written `(1,3,2)` denotes two different cells in the same document.
3. **§4 (4.7):** fix the dangling "(5.2)" to "(6.2)", and name the ambient
   ring: `U_18^rho[au,cv,lam,rho1,rho2]` with `p := -2*rho^2`.
4. **§4/§5:** insert the direction sentence — "On (0.1) the grade-16..18 row
   coefficients involve exactly the eighteen jets of (4.3), and `delta_22`
   restricted to those is a bijective scalar renaming; emptiness therefore
   transfers in both directions, and no reversed ring map is used."
5. **§6:** insert the degree sentence of §6.3 above before (6.2), and assemble
   the two halves ((4.7) unit on `au*cv != 0`, plus the degree argument off
   it) explicitly.
6. **§5 and §9:** relabel V33's contribution as code-path plus `rho=0`-slice
   custody, record that 49 of the 77 live grade-18 terms — including the whole
   residue — are invisible to the frozen bytes, and add
   `ACT-TOT-G18-GENERAL-RHO` alongside `ACT-TOT-G20` as an open custody item.
   Optionally state the deflation (rows 4 and 6 are zero at grade 16; rows 3,
   5, 7 are `p`-multiples of row 1 there) and that the `k6`/`k2` clauses of
   (4.3) are vacuous here.

With these six edits I would not object to the document.

## 10. `AUDIT.md` promotion eligibility

**Eligible, as one narrow filing, after repairs 1–6:**

- the exact strict unique-`AC` ledger with its equivalence to strict
  `AC`-minimality of the five hull weights, `s_min`, `G=10+a+c`, `T=G+d`, the
  eighteen baselines, the lifecycle routing, and the `(8,3,8)`
  reviewed-but-unpromoted status;
- the shifted finite-jet map (4.3)/(4.4) with the **verified** completeness
  statement (grades 16–18 involve exactly eighteen jets) and the row identity
  (4.6) at every grade `0..18`;
- the exclusion `ord(A)=2, ord(C)=4, ord(R)>=3` on `D(rho*k)` in the form
  boxed in §9, preferably with the single-row/syzygy certificate as the
  primary proof and `Psi` as a corroborating second route;
- the isobaric grading of §5.3, as a reusable fail-closed exporter test.

No existing `AUDIT.md` entry covers any of it. I searched `unique-AC`,
`Kummer`, `D(rho)`, `contact ladder`, `d23`, `actual-total`; the nearest entry
is the Kummer base-change/erratum entry, which explicitly says "The later
shifted-root contact compositions remain provisional until reviewed
independently" — this review is that review, for this one contact.

**Not eligible:** §1's "first missing contact" and §3's heading as written;
any reading of §5 as frozen general-`rho` grade-18 row custody; anything
suggesting `ord(A)=2, ord(C)=4` is closed (the `ord(R)=2` equality face is
open); the `d=2,3` union promotion, which remains lifecycle-blocked on an
`(8,3,8)` narrow promotion that does not exist.

**Explicitly not promotable in any form from this artifact:** a strict
unique-`AC` total cover, a generic-square cover, any Rees chart or terminal
receiver statement, any ramified-fibre statement, `G2-PSC`, `G2-BD`, Gate T,
order two, maximum twelve, `(8,12)`, or JC2.

## 11. Execution record

Desk scale only. No AWS launch, no heavy local CAS, no web sweep, no
canonical-ledger edit, no access of any kind to `jc2-lean`. Only this file was
written; no other campaign artifact was touched, read-modified, or
status-inspected.

```text
producer report      1d086a79…   hash verified
producer replay      0c124179…   hash verified, re-run, PASS in 0.03 s
upstream review      d62b3f22…   hash verified
31 replay pins                   all verified on disk
5 history pins                   all verified on disk
7 Tg18_*_q.poly + 7 _at_point    verified against the pinned compiled/result.json
reviewer verifier    eaf86e57a02f0fa8dce20b0e1ac81acdd168a8d5aec477a1d380d47269dbeaee
                                 pure-Python exact Fraction arithmetic, all checks PASS
```

Files read for the reconstruction (all hash-pinned upstream):
`prolong_boundary_g18_v33.py`, `prolong_boundary_g16_v28.py`,
`export_allrows_g13_g14_v20.py`, `replay_row5_grade14.py`,
`census_j2_typed_v23.py`, `compile_local_row.py`, `compile_r1_d1_ac.py`,
`compile_square_load_ladder.py`, `mine_support.py`, `tails.json`, and the
frozen `Tg15_*`, `Tg16_*`, `Tg17_*`, `Tg18_*` exports.

## Appendix A — reviewer verifier

Written to `/tmp` and run from there; imports no campaign module except the
frozen miner's pure `enumerate_primitives`, used only as a cross-check.
SHA-256 `eaf86e57a02f0fa8dce20b0e1ac81acdd168a8d5aec477a1d380d47269dbeaee`.

```python
#!/usr/bin/env python3
"""Opus5 hostile independent verifier: Gate-T D(rho*k) unique-AC (2,4,>=3) composition.

Desk scale, exact Fraction arithmetic.  Imports no campaign module except the frozen
support miner's pure enumerate_primitives, used only as a cross-check.  Runtime 142 s.
"""
from fractions import Fraction
import json, re
from pathlib import Path

ROOT = Path("/Users/dc/code/math/jc2")
TAILS = ROOT/"cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"

# ---------- polynomials: dict monomial->Fraction, monomial = sorted tuple of (name,exp)
def pconst(c):
    c = Fraction(c); return {(): c} if c else {}
def pvar(n): return {((n,1),): Fraction(1)}
def padd(*ps):
    o = {}
    for p in ps:
        for m,c in p.items():
            v = o.get(m, Fraction(0)) + c
            if v: o[m] = v
            elif m in o: del o[m]
    return o
def pscale(s,p):
    s = Fraction(s)
    return {} if not s else {m: c*s for m,c in p.items()}
def pmul(a,b):
    if not a or not b: return {}
    o = {}
    for ma,ca in a.items():
        for mb,cb in b.items():
            d = dict(ma)
            for n,e in mb: d[n] = d.get(n,0)+e
            m = tuple(sorted(d.items()))
            v = o.get(m, Fraction(0)) + ca*cb
            if v: o[m] = v
            elif m in o: del o[m]
    return o

# ---------- series over sigma, truncated at N-1
class Ctx:
    def __init__(self, maxdeg): self.N = maxdeg+1
    def szero(self): return [{} for _ in range(self.N)]
    def sadd(self,*ss): return [padd(*[s[i] for s in ss]) for i in range(self.N)]
    def sscale(self,c,s): return [pscale(c,x) for x in s]
    def smul(self,a,b):
        o = self.szero()
        for i in range(self.N):
            if not a[i]: continue
            for j in range(self.N-i):
                if b[j]: o[i+j] = padd(o[i+j], pmul(a[i],b[j]))
        return o
    def sshift(self,s,k):
        if k == 0: return list(s)
        o = self.szero()
        for i in range(self.N-k): o[i+k] = s[i]
        return o
    def spow(self,s,e):
        o = self.szero(); o[0] = pconst(1); b = s
        while e:
            if e&1: o = self.smul(o,b)
            e >>= 1
            if e: b = self.smul(b,b)
        return o
    def named(self, names):
        """names: list, entry None/'' means the jet is zero on this contact."""
        s = self.szero()
        for i,n in enumerate(names):
            if i < self.N and n: s[i] = pvar(n)
        return s
    def sig(self,k,poly):
        s = self.szero()
        if k < self.N: s[k] = poly
        return s

WEIGHTS = [8-i for i in range(7)] + [2,6,10]

def build_row(ctx, entries, row, coefficients, loads):
    total = ctx.szero()
    for raw_monomial, raw_coefficient in entries:
        m = [int(v) for v in raw_monomial]
        assert len(m) == 10 and sum(a*b for a,b in zip(m,WEIGHTS)) == 12+row, (row,m)
        assert all(e in (0,1) for e in m[7:]) and sum(m[7:]) <= 1
        term = ctx.szero(); term[0] = pconst(1)
        for i,e in enumerate(m[:7]):
            if e: term = ctx.smul(term, ctx.spow(coefficients[i], e))
        for i,e in enumerate(m[7:], start=7):
            if e: term = ctx.smul(term, loads[i])
        total = ctx.sadd(total, ctx.sscale(Fraction(str(raw_coefficient)), term))
    return total

def assemble(ctx, p, c, r, az, ac, ez, ec):
    """The seven F-coefficients, literally as in V33 build_source_series /
    compile_r1_d1_ac.source_coefficients (identical formulas)."""
    n3 = ctx.sshift(az,3); n2 = ctx.sshift(ac,3)
    n1 = ctx.sshift(ctx.sscale(Fraction(1,2), ctx.sadd(ctx.smul(p,az), ez)), 3)
    n0 = ctx.sshift(ctx.sscale(Fraction(1,2), ctx.sadd(ctx.smul(p,ac), ec)), 3)
    return {
        6: ctx.sscale(2,p),
        5: ctx.sscale(2,c),
        4: ctx.sadd(ctx.smul(p,p), ctx.sscale(2,r)),
        3: ctx.sadd(ctx.sscale(2, ctx.smul(p,c)), ctx.sshift(n3,2)),
        2: ctx.sadd(ctx.smul(c,c), ctx.sscale(2, ctx.smul(p,r)), ctx.sshift(n2,2)),
        1: ctx.sadd(ctx.sscale(2, ctx.smul(c,r)), ctx.sshift(n1,2)),
        0: ctx.sadd(ctx.smul(r,r), ctx.sshift(n0,2)),
    }

def total_source(ctx, zero=frozenset(), rho="rho"):
    """V33 general-rho actual-total source, with the named jets forced to zero."""
    def nm(n): return None if n in zero else n
    N = ctx.N
    p = ctx.szero()
    if rho: p[0] = pscale(-2, pmul(pvar(rho), pvar(rho)))
    for d in range(1, N):
        nd = nm(f"ell{d}")
        if nd: p[d] = pscale(2, pvar(nd))
    c = ctx.sshift(ctx.named([nm(x) for x in ["cs"]+[f"cs{i}" for i in range(1,N)]]), 2)
    r0 = ctx.named([nm(x) for x in ["rs"]+[f"rs{i}" for i in range(1,N)]])
    r = ctx.sscale(Fraction(1,4), ctx.sadd(ctx.smul(p,p), ctx.sshift(r0,2)))
    az = ctx.named([nm(x) for x in ["a1","aa1","aaa1"]+[f"az{i}" for i in range(3,N)]])
    ac = ctx.named([nm(x) for x in ["a0","aa0","aaa0"]+[f"ac{i}" for i in range(3,N)]])
    ez = ctx.named([nm(x) for x in ["c1","e1","ee1"]+[f"ez{i}" for i in range(3,N)]])
    ec = ctx.named([nm(x) for x in ["c0","e0","ee0"]+[f"ec{i}" for i in range(3,N)]])
    coefficients = assemble(ctx, p, c, r, az, ac, ez, ec)
    k10 = ctx.named([nm(x) for x in ["k","k1","k2c"]+[f"k10_{i}" for i in range(3,N)]])
    k6  = ctx.named([nm(x) for x in ["k6"]+[f"k6_{i}" for i in range(1,N)]])
    k2  = ctx.named([nm("k2")])
    loads = {7: ctx.sshift(k10,4), 8: ctx.sshift(k6,12), 9: ctx.sshift(k2,20)}
    return coefficients, loads, dict(p=p,c=c,r=r,az=az,ac=ac,ez=ez,ec=ec,k10=k10,k6=k6,k2=k2)

def b22_source(ctx, a=2, d=2, r_floor=3, amax=2, cmax=2, rmax=0, pmax=2,
               k0max=0, k6max=0, k2max=0):
    """compile_local_row.block(a,d) source arguments, fed through source_coefficients."""
    def jetseries(stem, mx):
        s = ctx.szero()
        for j in range(mx+1):
            if j < ctx.N: s[j] = pvar(stem if j == 0 else f"{stem}_{j}")
        return s
    pp = ctx.szero(); pp[0] = pvar("p")
    for j in range(1, pmax+1):
        if j < ctx.N: pp[j] = pscale(2, pvar(f"ell{j}"))
    az = ctx.sshift(jetseries("a1", amax), a)
    ac = ctx.sshift(jetseries("a0", amax), a)
    cz = ctx.sshift(jetseries("c1", cmax), a+d)
    cc = ctx.sshift(jetseries("c0", cmax), a+d)
    rz = ctx.sshift(jetseries("b1", rmax), r_floor)
    rc = ctx.sshift(jetseries("b0", rmax), r_floor)
    kc = ctx.sshift(rz, 2)                                            # total 'c'
    kr = ctx.sadd(ctx.sscale(Fraction(1,4), ctx.smul(pp,pp)), ctx.sshift(rc,2))  # total 'r'
    coefficients = assemble(ctx, pp, kc, kr, az, ac, ctx.sscale(2,cz), ctx.sscale(2,cc))
    loads = {7: ctx.sshift(jetseries("k0",k0max),4),
             8: ctx.sshift(jetseries("k60",k6max),12),
             9: ctx.sshift(jetseries("k20",k2max),20)}
    return coefficients, loads, dict(pp=pp,kc=kc,kr=kr,az=az,ac=ac,cz=cz,cc=cc)

TERM = re.compile(r'^\((-?\d+(?:/\d+)?)\)\*(.*)$')
def parse_frozen(path):
    txt = Path(path).read_text().strip()
    o = {}
    if txt == "0": return o
    for part in txt.split('+'):
        part = part.strip()
        if not part: continue
        mm = TERM.match(part); assert mm, part
        co = Fraction(mm.group(1)); dd = {}
        for f in mm.group(2).split('*'):
            if '^' in f:
                n,e = f.split('^'); dd[n] = dd.get(n,0)+int(e)
            else: dd[f] = dd.get(f,0)+1
        k = tuple(sorted(dd.items())); o[k] = o.get(k,Fraction(0))+co
    return {k:v for k,v in o.items() if v}

def load_tails(): return json.loads(TAILS.read_text())
def varnames(poly): return sorted({n for m in poly for n,_ in m})

# ============================================================ Laurent helpers (lam invertible)
def lmul(a,b):
    if not a or not b: return {}
    o={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            d=dict(ma)
            for n,e in mb:
                d[n]=d.get(n,0)+e
                if d[n]==0: del d[n]
            m=tuple(sorted(d.items())); v=o.get(m,Fraction(0))+ca*cb
            if v: o[m]=v
            elif m in o: del o[m]
    return o
def lpow(p,e):
    o=pconst(1)
    for _ in range(e): o=lmul(o,p)
    return o
def lsmul(ctx,a,b):
    o=ctx.szero()
    for i in range(ctx.N):
        if not a[i]: continue
        for j in range(ctx.N-i):
            if b[j]: o[i+j]=padd(o[i+j],lmul(a[i],b[j]))
    return o
def subst(poly,tab):
    out={}
    for mono,co in poly.items():
        t=pconst(co)
        for n,e in mono:
            t=lmul(t,lpow(tab.get(n,pvar(n)),e))
            if not t: break
        out=padd(out,t)
    return out
def txt(p):
    if not p: return "0"
    return " + ".join("(%s)*%s"%(c,"*".join(n if e==1 else "%s^%d"%(n,e) for n,e in m) or "1")
                      for m,c in sorted(p.items()))

MAX=18; ctx=Ctx(MAX); tails=load_tails()
CONTACT=frozenset({"cs","cs1","cs2","rs","rs1","rs2","a1","aa1","a0","aa0",
                   "c1","e1","ee1","ez3","c0","e0","ee0","ec3"})
RETAINED={"rho","ell1","ell2","aaa1","az3","az4","aaa0","ac3","ac4",
          "ez4","ez5","ez6","ec4","ec5","ec6","cs3","rs3","k"}
OK=True
def note(flag,label):
    global OK
    OK &= bool(flag)
    print("   [%s] %s" % ("PASS" if flag else "FAIL", label))

# ================================================================= A. LEDGER
print("A. STRICT UNIQUE-AC LEDGER, s_min, G, T, WELL-ORDERS")
def strict_AC(a,c,r): return a+c < min(2*c,3*r,1+r+c,4+2*a)
bad=[(a,c,r) for a in range(1,25) for c in range(3,40) for r in range(2,40)
     if ((c-a) in (1,2,3) and r-a>=0 and a+3*(r-a)>c-a) != strict_AC(a,c,r)]
note(not bad, "criterion 'd in {1,2,3}, s>=0, a+3s>d' == strict AC-minimality of the 5 hull weights")
def s_min(a,d):
    s=0
    while not (a+s>=2 and a+3*s>d): s+=1
    return s
ledger=[(a,d,a+s_min(a,d)) for a in range(1,10) for d in (2,3)]
prod=[(1,2,2),(1,3,2),(2,2,3),(2,3,3),(3,2,3),(3,3,4),(4,2,4),(4,3,4),(5,2,5),(5,3,5),
      (6,2,6),(6,3,6),(7,2,7),(7,3,7),(8,2,8),(8,3,8),(9,2,9),(9,3,9)]
note(ledger==prod, "producer (2.4): 18 baselines (a,d,r_floor) reproduce exactly")
note(all(10+2*a+d == 10+a+(a+d) for a in range(1,10) for d in (2,3)), "G = 10+2a+d = 10+a+c")
note(all(s_min(a,1)==0 for a in range(2,40)), "d=1 cell has s_min=0 for every a>=2 (a=1 has c=2<3)")
cells=[{"a":a,"c":a+d,"d":d,"r":a+s_min(a,d),"G":10+a+(a+d),"T":10+a+(a+d)+d}
       for a in range(1,61) for d in (1,2,3) if a+d>=3]
Kval=lambda x:(x["a"],x["c"],x["r"]); Kgr=lambda x:(x["G"],x["a"],x["c"],x["r"])
base=next(x for x in cells if Kval(x)==(2,3,2))
for nm,key in (("K_val",Kval),("K_grade",Kgr)):
    nxt=min((x for x in cells if key(x)>key(base)),key=key)
    nxt2=min((x for x in cells if key(x)>key(nxt)),key=key)
    note((nxt["a"],nxt["c"],nxt["r"],nxt["G"],nxt["T"])==(2,4,3,16,18),
         "%s: first cell strictly after (2,3,2) is (2,4,3), G=16, T=18"%nm)
    note((nxt2["a"],nxt2["c"],nxt2["r"],nxt2["G"],nxt2["T"])==(2,5,3,17,20),
         "%s: the cell after that is (2,5,3), G=17, T=20"%nm)
    pre=sorted((x for x in cells if key(x)<key(base)),key=key)
    print("        cells PRECEDING (2,3,2) in %s (all still untransported): %s"
          % (nm, [(x["a"],x["c"],x["r"],"G=%d"%x["G"],"T=%d"%x["T"]) for x in pre]))
print("        (a,c)=(2,4) with r=2:  AC=6 C2=8 R3=6 RC=7 A2=8  -> AC ties R3, equality face, NOT covered")

# ================================================ B. CONTACT ROWS AND JET COMPLETENESS
print("\nB. ACTUAL-TOTAL CONTACT ROWS ord(A)=2, ord(C)=4, ord(R)>=3  (general rho)")
tc,tl,TS = total_source(ctx, zero=CONTACT)
trows={l:build_row(ctx,tails[str(l)],l,tc,tl) for l in range(1,8)}
note(not [(l,g) for l in range(1,8) for g in range(16) if trows[l][g]],
     "all seven rows vanish identically at every grade 0..15 (first AC grade G=16)")
used=set()
for g in (16,17,18):
    for l in range(1,8): used |= set(varnames(trows[l][g]))
note(used==RETAINED, "grades 16,17,18 involve EXACTLY the 18 jets of producer (4.3); no more, no fewer")
print("        variables at g16/g17/g18:", " ".join(sorted(used)))
for l in range(1,8):
    print("        row %d term counts: %s"%(l," ".join("g%d=%d"%(g,len(trows[l][g])) for g in (16,17,18))))

# ============================================== C. THE SHIFTED FINITE-JET MAP delta_22
print("\nC. THE SHIFTED FINITE-JET MAP (4.3)/(4.4) AND ROW IDENTITY (4.6)")
bc,bl,BS = b22_source(ctx)
brows={l:build_row(ctx,tails[str(l)],l,bc,bl) for l in range(1,8)}
DELTA={"rho":pvar("lam"),"ell1":pvar("ell1"),"ell2":pvar("ell2"),
 "aaa1":pvar("a1"),"az3":pvar("a1_1"),"az4":pvar("a1_2"),
 "aaa0":pvar("a0"),"ac3":pvar("a0_1"),"ac4":pvar("a0_2"),
 "ez4":pscale(2,pvar("c1")),"ez5":pscale(2,pvar("c1_1")),"ez6":pscale(2,pvar("c1_2")),
 "ec4":pscale(2,pvar("c0")),"ec5":pscale(2,pvar("c0_1")),"ec6":pscale(2,pvar("c0_2")),
 "cs3":pvar("b1"),"rs3":pscale(4,pvar("b0")),
 "k":pvar("k0"),"k6":pvar("k60"),"k2":pvar("k20")}
PSUB=pscale(-2,lmul(pvar("lam"),pvar("lam")))
def killp(poly): return subst(poly,{"p":PSUB})
def mk(tbl):
    def d(poly):
        out={}
        for mono,co in poly.items():
            t=pconst(co); dead=False
            for n,e in mono:
                im=tbl.get(n)
                if im is None: dead=True; break
                t=lmul(t,lpow(im,e))
                if not t: dead=True; break
            if not dead: out=padd(out,t)
        return out
    return d
d22=mk(DELTA)
note(all(all(d22(tc[i][g])==killp(bc[i][g]) for g in range(MAX+1)) for i in range(7))
     and all(all(d22(tl[i][g])==killp(bl[i][g]) for g in range(MAX+1)) for i in (7,8,9)),
     "delta_22 carries all 7 total F-series and all 3 load series onto the B22 ones")
note(all(all(d22(trows[l][g])==killp(brows[l][g]) for g in range(MAX+1)) for l in range(1,8)),
     "delta_22([sigma^g]Phi_l^tot) = [sigma^g]Phi_l^B22 for every l=1..7 and every g=0..18")
inv = len({str(v) for v in DELTA.values()})==len(DELTA)
note(inv, "delta_22 restricted to the 18 live jets is a bijective scalar renaming (so emptiness transfers BOTH ways)")
print("        mutation controls -- which clauses of (4.3) are load-bearing at g<=18:")
def probe(label,mut):
    t=dict(DELTA); mut(t); dd=mk(t)
    hit={g:[l for l in range(1,8) if dd(trows[l][g])!=killp(brows[l][g])] for g in (16,17,18)}
    print("          %-30s g16:%-14s g17:%-14s g18:%s"%(label,hit[16] or "NONE",hit[17] or "NONE",hit[18] or "NONE"))
probe("rs3 -> b0 (drop factor 4)",  lambda t: t.__setitem__("rs3",pvar("b0")))
probe("ez4 -> c1 (drop factor 2)",  lambda t: t.__setitem__("ez4",pvar("c1")))
probe("ell1 -> 0 (moving term)",    lambda t: t.pop("ell1"))
probe("ell2 -> 0",                  lambda t: t.pop("ell2"))
probe("k -> 0",                     lambda t: t.pop("k"))
probe("k6 -> 0",                    lambda t: t.pop("k6"))
probe("k2 -> 0",                    lambda t: t.pop("k2"))
probe("cs3 -> 0 / rs3 -> 0",        lambda t: (t.pop("cs3"),t.pop("rs3")))
probe("swap az3 <-> ac3",           lambda t: (t.__setitem__("az3",pvar("a0_1")),t.__setitem__("ac3",pvar("a1_1"))))

# ================================================== D. CUSTODY
print("\nD. FROZEN CUSTODY")
D15=ROOT/"cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled"
g15ctx=Ctx(15); gc,gl,_=total_source(g15ctx)
g15={r:build_row(g15ctx,tails[str(r)],r,gc,gl) for r in range(1,8)}
m15=all(g15[r][15]==parse_frozen(D15/("Tg15_%d_q.poly"%r)) for r in range(1,8))
note(m15,"all seven frozen GENERAL-rho grade-15 rows (V22 r1) reproduce exactly")
note(all(e%2==0 for r in range(1,8) for mo in parse_frozen(D15/("Tg15_%d_q.poly"%r)) for n,e in mo if n=="rho"),
     "every frozen grade-15 term is rho-even")
FACE=frozenset({"rs","cs","c0","c1","a0"})
fc,fl,_=total_source(ctx,zero=FACE,rho=None)
frows={r:build_row(ctx,tails[str(r)],r,fc,fl) for r in range(1,8)}
dirs={16:"max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827",
      17:"max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827",
      18:"max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827"}
for g,dn in dirs.items():
    ok=all(frows[r][g]==parse_frozen(ROOT/"cases"/dn/("aws_q/compiled/Tg%d_%d_q.poly"%(g,r))) for r in range(1,8))
    note(ok,"all seven frozen rho=0 ordered-a1 FACE rows at grade %d reproduce exactly"%g)
tot=sum(len(trows[r][18]) for r in range(1,8))
vis=sum(1 for r in range(1,8) for m in trows[r][18] if "rho" not in dict(m))
print("        contact rows at g18: %d terms, %d rho-free (a rho=0 face can see these), %d invisible"%(tot,vis,tot-vis))
print("        the terminal residue has rho-exponent 2 -> lies entirely in the invisible part")
def deg(n):
    if n=="rho": return 1
    if n.startswith("ell"): return 2
    if n in ("k","k1","k2c") or n.startswith("k10_"): return 2
    if n=="k6" or n.startswith("k6_"): return 6
    if n=="k2": return 10
    if n[:2]=="cs": return 3
    if n[:2]=="rs": return 4
    if n in ("a1","aa1","aaa1") or n.startswith("az"): return 5
    if n in ("a0","aa0","aaa0") or n.startswith("ac"): return 6
    if n in ("c1","e1","ee1") or n.startswith("ez"): return 7
    if n in ("c0","e0","ee0") or n.startswith("ec"): return 8
    raise KeyError(n)
hom=all({sum(deg(n)*e for n,e in m) for g in range(MAX+1) for m in trows[r][g]} in ({12+r},set())
        for r in range(1,8))
note(hom,"every actual-total row is isobaric of degree 12+l for wt(rho,ell,cs,rs,az,ac,ez,ec)=(1,2,3,4,5,6,7,8)")

# ======================================= E. PRIMITIVE INVENTORY (5.1)/(6.4)
print("\nE. B22 POLAR PRIMITIVE INVENTORY")
from itertools import product as iproduct
import math, importlib.util
ATOMS=((2,2,1,0,0,2),(4,4,2,0,0,1),(5,3,0,1,0,1),(5,4,0,0,1,1))
SUMM=(("unloaded",None,Fraction(3,2),0),("k10","k10",Fraction(5,4),4),
      ("k6","k6",Fraction(3,4),12),("k2","k2",Fraction(1,4),20))
def binom(al,n):
    x=Fraction(1)
    for i in range(n): x*=al-i
    return x/math.factorial(n)
def mine(a,d,r,target,pad=0):
    b={"R":r,"A":a,"C":a+d}; agg={}
    for nm,load,al,fx in SUMM:
        if target-fx<0: continue
        costs=[f+b["R"]*R+b["A"]*A+b["C"]*C for f,_,R,A,C,_ in ATOMS]
        for cnt in iproduct(*(range((target-fx)//c+pad+1) for c in costs)):
            n=sum(cnt)
            if not n: continue
            fixed=fx; den=0; e={"R":0,"A":0,"C":0}; sc=1
            for q,(f,dd,R,A,C,s) in zip(cnt,ATOMS):
                fixed+=q*f; den+=q*dd; sc*=s**q
                e["R"]+=q*R; e["A"]+=q*A; e["C"]+=q*C
            gr=fixed+sum(b[k]*e[k] for k in e)
            if gr>target: continue
            po=den-int(4*al)
            if po<=0: continue
            mu=math.factorial(n)
            for q in cnt: mu//=math.factorial(q)
            agg[(nm,load,fixed,e["R"],e["A"],e["C"],po)]=agg.get((nm,load,fixed,e["R"],e["A"],e["C"],po),Fraction(0))+binom(al,n)*mu*sc
    out=[]
    for (nm,load,fixed,R,A,C,po),co in agg.items():
        if not co: continue
        gr=fixed+b["R"]*R+b["A"]*A+b["C"]*C
        out.append((gr,co,po,R,A,C,nm))
    return sorted(out)
prim=mine(2,2,3,18)
for gr,co,po,R,A,C,nm in prim:
    print("        grade %2d coeff %-6s pole %d  %s%s"%(gr,co,po,("k*" if nm=="k10" else ""),
          "".join(s*e for s,e in (("R",R),("A",A),("C",C))) or "1"))
note({(gr,co,po) for gr,co,po,_,_,_,_ in prim}=={(16,Fraction(3,4),1),(18,Fraction(5,32),1),
      (18,Fraction(5,8),1),(18,Fraction(3,8),2)}, "producer (6.4): exactly the four listed primitives")
note(len(prim)==4 and max(p[2] for p in prim)==2 and mine(2,2,3,18,pad=1)==prim,
     "(5.1): primitive_count=4, maxpole=2, atom-cutoff sentinel stable under pad=1")
try:
    M=ROOT/"cases/max12_812_order2_square_owner_d1_unique_ac_d23_small_a_support_miner_20260826/mine_support.py"
    sp=importlib.util.spec_from_file_location("m",M); mo=importlib.util.module_from_spec(sp); sp.loader.exec_module(mo)
    th=mo.enumerate_primitives({"a":2,"d":2,"c":4,"s_min":1,"r":3,"first_ac_grade":16,"target_grade":18})
    note({(int(x["first_grade"]),Fraction(x["coefficient"]),int(x["pole"])) for x in th}
         =={(gr,co,po) for gr,co,po,_,_,_,_ in prim}, "agrees with the frozen miner's own enumerate_primitives")
except Exception as exc:
    print("   [SKIP] miner cross-check:",exc)

# ================================================== F. ENDPOINT
print("\nF. B22 ENDPOINT: HENSEL ROOT, ALLOCATIONS, TERMINAL FUNCTIONAL, RESIDUE")
LAM=pvar("lam"); ILAM={(("lam",-1),):Fraction(1)}
P0=pscale(-2,lmul(LAM,LAM))
r1=pscale(Fraction(-1,2),lmul(pvar("ell1"),ILAM))
r2=pscale(Fraction(-1,2),lmul(padd(pvar("ell2"),lmul(r1,r1)),ILAM))
lam_s=ctx.szero(); lam_s[0]=LAM; lam_s[1]=r1; lam_s[2]=r2
P_s=ctx.szero(); P_s[0]=P0; P_s[1]=pscale(2,pvar("ell1")); P_s[2]=pscale(2,pvar("ell2"))
chk=ctx.sadd(lsmul(ctx,lam_s,lam_s),ctx.sscale(Fraction(1,2),P_s))
note(not any(chk[g] for g in range(3)),
     "(6.3): lambda0=eps*rho, lambda1=-ell1/(2 lambda0), lambda2=-(ell2+lambda1^2)/(2 lambda0) solve lambda^2+P/2=0 to sigma^2")
want=pscale(Fraction(3,2),lmul(lmul(LAM,LAM),lmul(pvar("cv"),pvar("cv"))))
for eps,lab in ((1,"Alloc_+ / eps=+1"),(-1,"Alloc_- / eps=-1")):
    tab={"p":P0,"a1":pvar("au"),"a0":pscale(-eps,lmul(pvar("au"),LAM)),
         "c1":pvar("cv"),"c0":pscale(eps,lmul(pvar("cv"),LAM))}
    R={l:[subst(brows[l][g],tab) for g in range(MAX+1)] for l in (1,3,4)}
    Psi=ctx.sadd(R[4],lsmul(ctx,ctx.sscale(eps,lam_s),
          ctx.sadd(R[3],ctx.sscale(Fraction(1,4),lsmul(ctx,P_s,R[1])))))
    note((not Psi[16]) and (not Psi[17]) and Psi[18]==want,
         "(6.6) %s: [s^16]Psi=[s^17]Psi=0 and [s^18]Psi=(3/2)*rho^2*cv^2"%lab)
    note(sorted({n for m in Psi[18] for n,_ in m})==["cv","lam"],
         "        %s: the residue involves only cv and lam (not au, k0, b0, b1 or the deeper jets)"%lab)
    note(subst(brows[4][18],tab)==pscale(Fraction(3,4),lmul(lmul(LAM,LAM),lmul(pvar("cv"),pvar("cv")))),
         "        %s: the SINGLE raw row Phi4 already gives (3/4)*rho^2*cv^2 at grade 18"%lab)
tabsame={"p":P0,"a1":pvar("au"),"a0":pscale(-1,lmul(pvar("au"),LAM)),
         "c1":pvar("cv"),"c0":pscale(-1,lmul(pvar("cv"),LAM))}
note(subst(brows[1][16],tabsame)!={}, "a same-root allocation is already killed at grade 16 on D(rho)")
note(not any(brows[6][g] for g in range(MAX+1)) and [g for g in range(MAX+1) if brows[4][g]]==[18],
     "deflation: row 6 vanishes identically through 18; row 4 is nonzero only at grade 18")

# ================================ G. THE SAME EXCLUSION, DIRECTLY IN TOTAL COORDINATES
print("\nG. CASE-FREE CERTIFICATE IN ACTUAL-TOTAL COORDINATES (reviewer's simplification)")
print("        [sigma^16]Phi1 =", txt(trows[1][16]))
print("        [sigma^16]Phi2 =", txt(trows[2][16]))
print("        [sigma^16]Phi4 = %s ,  [sigma^17]Phi4 = %s"%(txt(trows[4][16]),txt(trows[4][17])))
print("        [sigma^18]Phi4 =", txt(trows[4][18]))
A1,A0,E,F,RH=(pvar(x) for x in ("aaa1","aaa0","ez4","ec4","rho")); R2=pmul(RH,RH)
g1=pscale(Fraction(3,8),padd(pmul(A0,E),pmul(A1,F)))
g2=pscale(Fraction(3,8),padd(pmul(A0,F),pmul(R2,pmul(A1,E))))
g4=pscale(Fraction(3,32),padd(pmul(F,F),pmul(R2,pmul(E,E))))
note(trows[1][16]==g1 and trows[2][16]==g2 and trows[4][18]==g4 and not trows[4][16] and not trows[4][17],
     "the three live coefficients are exactly g1,g2 (grade 16) and g4 (grade 18)")
Cp=pscale(Fraction(1,2),padd(F,pmul(RH,E))); Cm=pscale(Fraction(1,2),padd(F,pscale(-1,pmul(RH,E))))
note(g1==pscale(Fraction(3,4),pscale(Fraction(1,2),padd(pmul(A1,F),pmul(A0,E))))
     and g2==pscale(Fraction(3,4),pscale(Fraction(1,2),padd(pmul(A0,F),pmul(R2,pmul(A1,E))))),
     "g1,g2 are (3/4) x the two coefficients of A0*C0 mod L, A0=aaa1*z+aaa0, C0=(ez4*z+ec4)/2, L=z^2-rho^2")
note(g4==pscale(Fraction(3,16),padd(pmul(Cp,Cp),pmul(Cm,Cm))), "g4 = (3/16)*(C0(rho)^2 + C0(-rho)^2)")
D=padd(pmul(R2,pmul(E,E)),pscale(-1,pmul(F,F)))
note(padd(pmul(E,g2),pscale(-1,pmul(F,g1)))==pscale(Fraction(3,8),pmul(A1,D)),
     "syzygy  ez4*g2 - ec4*g1 = (3/8)*aaa1*(rho^2 ez4^2 - ec4^2)")
note(padd(pmul(F,g2),pscale(-1,pmul(R2,pmul(E,g1))))==pscale(Fraction(-3,8),pmul(A0,D)),
     "syzygy  ec4*g2 - rho^2 ez4*g1 = -(3/8)*aaa0*(rho^2 ez4^2 - ec4^2)")
note(padd(pscale(Fraction(32,3),g4),D)==pscale(2,pmul(R2,pmul(E,E))) and
     padd(pscale(Fraction(32,3),g4),pscale(-1,D))==pscale(2,pmul(F,F)),
     "(32/3)g4 +/- D = 2 rho^2 ez4^2 and 2 ec4^2")
print("        => aaa1*rho^2*ez4^2, aaa1*ec4^2, aaa0*rho^2*ez4^2, aaa0*ec4^2 all lie in (g1,g2,g4).")
print("        => on rho!=0 with (aaa0,aaa1)!=(0,0):  ez4=ec4=0, i.e. ord(C)>4.  Contradiction.")
print("        No allocation case split, no Hensel root, no deck involution, no k, au, J or cv inverted.")

print("\n%s" % ("OPUS5-A2D2-HOSTILE-VERIFY-COMPLETE  ALL-CHECKS-PASS" if OK
                else "OPUS5-A2D2-HOSTILE-VERIFY-COMPLETE  *** SOME CHECK FAILED ***"))
```

Observed output (all `[PASS]`):

```text
A. STRICT UNIQUE-AC LEDGER, s_min, G, T, WELL-ORDERS
   [PASS] criterion 'd in {1,2,3}, s>=0, a+3s>d' == strict AC-minimality of the 5 hull weights
   [PASS] producer (2.4): 18 baselines (a,d,r_floor) reproduce exactly
   [PASS] G = 10+2a+d = 10+a+c
   [PASS] d=1 cell has s_min=0 for every a>=2 (a=1 has c=2<3)
   [PASS] K_val: first cell strictly after (2,3,2) is (2,4,3), G=16, T=18
   [PASS] K_val: the cell after that is (2,5,3), G=17, T=20
        cells PRECEDING (2,3,2) in K_val (all still untransported): [(1, 3, 2, 'G=14', 'T=16'), (1, 4, 2, 'G=15', 'T=18')]
   [PASS] K_grade: first cell strictly after (2,3,2) is (2,4,3), G=16, T=18
   [PASS] K_grade: the cell after that is (2,5,3), G=17, T=20
        cells PRECEDING (2,3,2) in K_grade (all still untransported): [(1, 3, 2, 'G=14', 'T=16'), (1, 4, 2, 'G=15', 'T=18')]
        (a,c)=(2,4) with r=2:  AC=6 C2=8 R3=6 RC=7 A2=8  -> AC ties R3, equality face, NOT covered

B. ACTUAL-TOTAL CONTACT ROWS ord(A)=2, ord(C)=4, ord(R)>=3  (general rho)
   [PASS] all seven rows vanish identically at every grade 0..15 (first AC grade G=16)
   [PASS] grades 16,17,18 involve EXACTLY the 18 jets of producer (4.3); no more, no fewer
        variables at g16/g17/g18: aaa0 aaa1 ac3 ac4 az3 az4 cs3 ec4 ec5 ec6 ell1 ell2 ez4 ez5 ez6 k rho rs3
        row 1 term counts: g16=2 g17=4 g18=9
        row 2 term counts: g16=2 g17=5 g18=14
        row 3 term counts: g16=2 g17=6 g18=16
        row 4 term counts: g16=0 g17=0 g18=2
        row 5 term counts: g16=2 g17=6 g18=18
        row 6 term counts: g16=0 g17=0 g18=0
        row 7 term counts: g16=2 g17=6 g18=18

C. THE SHIFTED FINITE-JET MAP (4.3)/(4.4) AND ROW IDENTITY (4.6)
   [PASS] delta_22 carries all 7 total F-series and all 3 load series onto the B22 ones
   [PASS] delta_22([sigma^g]Phi_l^tot) = [sigma^g]Phi_l^B22 for every l=1..7 and every g=0..18
   [PASS] delta_22 restricted to the 18 live jets is a bijective scalar renaming (so emptiness transfers BOTH ways)
        mutation controls -- which clauses of (4.3) are load-bearing at g<=18:
          rs3 -> b0 (drop factor 4)      g16:NONE           g17:NONE           g18:[1, 2, 3, 5, 7]
          ez4 -> c1 (drop factor 2)      g16:[1, 2, 3, 5, 7] g17:[1, 2, 3, 5, 7] g18:[1, 2, 3, 4, 5, 7]
          ell1 -> 0 (moving term)        g16:NONE           g17:[2, 3, 5, 7]   g18:[2, 3, 5, 7]
          ell2 -> 0                      g16:NONE           g17:NONE           g18:[2, 3, 5, 7]
          k -> 0                         g16:NONE           g17:NONE           g18:[1, 2, 3, 5, 7]
          k6 -> 0                        g16:NONE           g17:NONE           g18:NONE
          k2 -> 0                        g16:NONE           g17:NONE           g18:NONE
          cs3 -> 0 / rs3 -> 0            g16:NONE           g17:NONE           g18:[1, 2, 3, 5, 7]
          swap az3 <-> ac3               g16:NONE           g17:[1, 2, 3, 5, 7] g18:[1, 2, 3, 5, 7]

D. FROZEN CUSTODY
   [PASS] all seven frozen GENERAL-rho grade-15 rows (V22 r1) reproduce exactly
   [PASS] every frozen grade-15 term is rho-even
   [PASS] all seven frozen rho=0 ordered-a1 FACE rows at grade 16 reproduce exactly
   [PASS] all seven frozen rho=0 ordered-a1 FACE rows at grade 17 reproduce exactly
   [PASS] all seven frozen rho=0 ordered-a1 FACE rows at grade 18 reproduce exactly
        contact rows at g18: 77 terms, 28 rho-free (a rho=0 face can see these), 49 invisible
        the terminal residue has rho-exponent 2 -> lies entirely in the invisible part
   [PASS] every actual-total row is isobaric of degree 12+l for wt(rho,ell,cs,rs,az,ac,ez,ec)=(1,2,3,4,5,6,7,8)

E. B22 POLAR PRIMITIVE INVENTORY
        grade 16 coeff 3/4    pole 1  AC
        grade 18 coeff 5/32   pole 1  k*AA
        grade 18 coeff 3/8    pole 2  CC
        grade 18 coeff 5/8    pole 1  k*RC
   [PASS] producer (6.4): exactly the four listed primitives
   [PASS] (5.1): primitive_count=4, maxpole=2, atom-cutoff sentinel stable under pad=1
   [PASS] agrees with the frozen miner's own enumerate_primitives

F. B22 ENDPOINT: HENSEL ROOT, ALLOCATIONS, TERMINAL FUNCTIONAL, RESIDUE
   [PASS] (6.3): lambda0=eps*rho, lambda1=-ell1/(2 lambda0), lambda2=-(ell2+lambda1^2)/(2 lambda0) solve lambda^2+P/2=0 to sigma^2
   [PASS] (6.6) Alloc_+ / eps=+1: [s^16]Psi=[s^17]Psi=0 and [s^18]Psi=(3/2)*rho^2*cv^2
   [PASS]         Alloc_+ / eps=+1: the residue involves only cv and lam (not au, k0, b0, b1 or the deeper jets)
   [PASS]         Alloc_+ / eps=+1: the SINGLE raw row Phi4 already gives (3/4)*rho^2*cv^2 at grade 18
   [PASS] (6.6) Alloc_- / eps=-1: [s^16]Psi=[s^17]Psi=0 and [s^18]Psi=(3/2)*rho^2*cv^2
   [PASS]         Alloc_- / eps=-1: the residue involves only cv and lam (not au, k0, b0, b1 or the deeper jets)
   [PASS]         Alloc_- / eps=-1: the SINGLE raw row Phi4 already gives (3/4)*rho^2*cv^2 at grade 18
   [PASS] a same-root allocation is already killed at grade 16 on D(rho)
   [PASS] deflation: row 6 vanishes identically through 18; row 4 is nonzero only at grade 18

G. CASE-FREE CERTIFICATE IN ACTUAL-TOTAL COORDINATES (reviewer's simplification)
        [sigma^16]Phi1 = (3/8)*aaa0*ez4 + (3/8)*aaa1*ec4
        [sigma^16]Phi2 = (3/8)*aaa0*ec4 + (3/8)*aaa1*ez4*rho^2
        [sigma^16]Phi4 = 0 ,  [sigma^17]Phi4 = 0
        [sigma^18]Phi4 = (3/32)*ec4^2 + (3/32)*ez4^2*rho^2
   [PASS] the three live coefficients are exactly g1,g2 (grade 16) and g4 (grade 18)
   [PASS] g1,g2 are (3/4) x the two coefficients of A0*C0 mod L, A0=aaa1*z+aaa0, C0=(ez4*z+ec4)/2, L=z^2-rho^2
   [PASS] g4 = (3/16)*(C0(rho)^2 + C0(-rho)^2)
   [PASS] syzygy  ez4*g2 - ec4*g1 = (3/8)*aaa1*(rho^2 ez4^2 - ec4^2)
   [PASS] syzygy  ec4*g2 - rho^2 ez4*g1 = -(3/8)*aaa0*(rho^2 ez4^2 - ec4^2)
   [PASS] (32/3)g4 +/- D = 2 rho^2 ez4^2 and 2 ec4^2
        => aaa1*rho^2*ez4^2, aaa1*ec4^2, aaa0*rho^2*ez4^2, aaa0*ec4^2 all lie in (g1,g2,g4).
        => on rho!=0 with (aaa0,aaa1)!=(0,0):  ez4=ec4=0, i.e. ord(C)>4.  Contradiction.
        No allocation case split, no Hensel root, no deck involution, no k, au, J or cv inverted.

OPUS5-A2D2-HOSTILE-VERIFY-COMPLETE  ALL-CHECKS-PASS
```
