# Hostile review of the Sol ordered-`T-a1` `rho=0` cascade closure (V42)

Date: 2026-08-27
Reviewer: Opus5 (different model from the Sol producer)

Verdicts:

| object | verdict |
|---|---|
| A2 identity `Tg16_6-(3/32)rs1*Tg13_2=(21/1024)a1^2*rs1^2` | **CONFIRMED** |
| A1 ordinary branch certificate `a1^8` | **CONFIRMED** |
| branch coverage from `Tg14_3` | **CONFIRMED** |
| combined raw-field-point theorem | **CONFIRMED (scope sharpened)** |

No mathematical defect was found in any of the four. Five non-mathematical
defects are recorded in section 8; one of them (the mutation control) is
inert rather than wrong, and I supply a replacement control that passes and
is strictly stronger. The exact scoped result **is eligible for `AUDIT.md`
promotion**, subject to the textual corrections in section 8.

## 0. What was reviewed and how

Artifacts, all four hashes re-verified locally before anything else:

```text
5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f
  xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-sol-20260827.md
f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459
  cases/.../replay_a1_cascade_closure_v42.py
01b8edd2b699d7c4b65452ea6eba47a98bf25c1cd5a18022a035e2346c973566
  cases/.../RESULT.json
9de72b9261e12896f3c352f313b0788091616fc64c9ec9754c53eba196ed3ca5
  cases/.../FREEZE.sha256
```

The producer replay does run and reproduces `RESULT.json` field for field
(0.6 s). Per the review brief that was **not** accepted as review. Everything
below was rebuilt from the frozen bytes with three implementations that do
not share code with the producer:

1. my own strict tokenizer for the `.poly` corpus (no `ast`), plus my own
   sparse `Fraction` Laurent arithmetic;
2. an ordinary univariate **division algorithm** for the lift, instead of the
   producer's `divided_difference` construction;
3. **Singular** for a final independent-engine check of the three headline
   identities and for the necessity tests of section 7. All Singular runs are
   desk-scale: the longest is 0.035 s wall.

No AWS launch, no web access, no `jc2-lean` access, no canonical-ledger edit.
The only file I wrote inside the repository is this report.

## 1. Source custody (verified)

The replay pins `solve_graded_ladder_v37.py`
(`ba034c8c…845b`) and four consumed reports; all five hashes match. I then
audited whether V37's own custody is complete rather than trusting it:

* parser `census_j2_typed_v23.py` pinned (`14f2de22…4501`);
* `V23/output_r1/RESULT.json` pinned (`ce4d0adb…4641`); each grade 10--15 row
  file checked against `charts.a1_ordered.output_sha256` inside it;
* the four grade 16--19 `compiled/result.json` files pinned by constants in
  V37; each row file checked against `coefficient_sha256` inside them.

That chain is closed. I re-walked all of it **without importing V37** and
re-hashed all **70/70** row files: no mismatch.

Three further custody facts that the producer does not state and that a
hostile reader should want:

* **Correct file family.** The grade 16--18 directories also contain
  `Tg1x_y_at_point_q.poly` / `_at_old_point_q.poly` restrictions. V37 resolves
  `Path(result["coefficient_paths"][name]).name`, which lands on the full
  `Tg1x_y_q.poly`. The sparse/at-point files are **not** used. This matters:
  using them would silently scope the whole result to the V34 six-coordinate
  support.
* **Chart consistency.** For grades 10--15 the ordered-`a1` chart is produced
  by V23 as `specialize(row, {rs,cs,c0,c1,a0}, {})`. I re-derived all 42 of
  those outputs from the pinned V9/V20/V22 source rows with my own parser:
  **42/42 exact**. For grades 16--19 the AWS exports are already in that
  chart; I verified directly that **no** row among the 70 contains any of
  `rs, cs, c0, c1, a0`. So all ten grades genuinely live on one chart.
* **Independent census.** After `rho=0`:

```text
grade      10   11   12   13   14   15   16   17   18   19
rows        0    1    4    5    6    7    7    7    7    7     (51 nonzero)
terms       0    1    9   28   75  187  424  867 1647 2929
```

  65 variables, every row sigma-homogeneous of its grade, every `rho`
  exponent even before specialization. This reproduces V37's hard-coded
  `ROW_COUNTS` / `TERM_COUNTS` from the bytes rather than from V37.

Finally I cross-validated my tokenizer against the producer's `ast` parser on
all 70 files: identical polynomials, 6651 stored terms. Both parsers are
therefore mutually corroborated.

## 2. The inherited deductions, re-derived and typed

I did not consume the prior cascade on trust. Every displayed identity was
recomputed from the frozen rows. All pass:

```text
Tg11_1                                    = (3/8)*a1*e0
Tg12_2|e0=0                               = (3/32)*e1*(e1-4*a1*ell1)
Tg12_1|e0=0                               = (3/8)*a1*ee0 + (3/8)*aa0*e1
Tg12_1|e0=0,e1=4a1*ell1                   = (3/8)*a1*(ee0+4*aa0*ell1)
Tg13_4|e0=0,e1=4a1*ell1,ee0=-4aa0*ell1    = -(3/2)*a1^2*ell1^3
Tg14_4|e0=e1=ee0=0                        = (3/32)*a1^2*ell1*rs1
Tg14_3|base + (1/2)*ell1*Tg13_1|base      = (3/8)*a1^2*cs1*ell1 - (3/16)*a1*aa0*rs1
Tg13_2|B = -(3/8)*a1*ee1*ell1     Tg13_1|B = (3/8)*a1*ec3
Tg15_4|B = (3/32)*a1^2*ell1*rs2   Tg14_2|B = -(3/8)*a1*ell1*ez3
Tg14_1|B = (3/8)*a1*(ec4-a1*cs2)
Tg15_3|B = (3/8)*a1^2*cs2*ell1 - (1/16)*a1^3
Tg16_5|B = (27/2)*cs2^3*ell1^4
Tg15_4|A2 = (3/32)*a1*rs1*(a1*ell2-ee1)
```

One step of the cascade is **not** asserted by the pinned V41 replay: on the
first factor branch `e1=0`, the vanishing of `ee0` is needed but V41 only
checks `Tg12_1` on the branch `e1=4a1*ell1`. I closed that hole: the third
line above gives `Tg12_1|e0=e1=0 = (3/8)*a1*ee0`, so `ee0=0` on `D(a1)`
immediately. The cascade is complete; this is a gap in the earlier *replay
script*, not in the earlier *argument*.

Typing of the inherited deductions, which the producer's ledger gets right
but states loosely:

| deduction | type |
|---|---|
| `e0=0` | ideal-strength: `a1*e0 in I` gives `e0 in (I:a1)`; no radical needed |
| `e1=0`, `ee0=0` | **radical/field-point**: case split on the exact factorization of `Tg12_2` |
| `ell1=0` | **radical/field-point**, and the discarded branch localizes further at `ell1` |
| `aa0*rs1=0` | ideal-strength *given* `ell1=0`, hence radical overall |

Localizations actually used: `D(a1)` throughout; `D(ell1)` only inside the
branch that is being contradicted; `D(rs1)` only to define A2. That matches
the producer's ledger exactly. No hidden division was found.

## 3. Branch coverage — CONFIRMED

```text
Tg14_3|e0=e1=ee0=ell1=0  =  -(3/16)*a1*aa0*rs1     (exactly one surviving term)
```

Verified in my implementation and again in Singular (residual `0`). This is
hand-checkable: of the 37 terms of the chart file `Tg14_3.poly`, `rho=0`
kills the `rho^2`/`rho^4` terms and each remaining term other than
`(-3/16)*a1*aa0*rs1` carries a visible factor of `e0`, `e1`, `ee0` or `ell1`.

On `D(a1)` over any field, `a1*aa0*rs1=0` gives `aa0=0` or `rs1=0`, i.e.
the cover `V(rs1) ∪ V(aa0)`. This is a field-point/radical step (a product
vanishing in a domain), correctly labelled as such by the producer. Needs
`char != 2,3`.

## 4. The A2 identity — CONFIRMED

After the inherited substitutions `e0=e1=ee0=ell1=aa0=0` the frozen rows
collapse to two terms each:

```text
Tg13_2 = rs1*( -(3/32)*a1^2 + (5/1024)*k*rs1^2 )
Tg16_6 = (3/256)*a1^2*rs1^2 + (15/32768)*k*rs1^4
```

and

```text
Tg16_6 - (3/32)*rs1*Tg13_2 = (21/1024)*a1^2*rs1^2.
```

Confirmed coefficientwise in my implementation and independently in Singular
(`A2_RESIDUAL=0`). The `k*rs1^4` terms cancel because
`(3/32)*(5/1024) = 15/32768`; the surviving scalar is
`3/256 + 9/1024 = 21/1024`.

Notes a hostile reader should check and which hold:

* The identity is **division-free**. Only the *conclusion* needs
  `D(a1*rs1)`, which is exactly the A2 branch definition (`rs1 != 0` by the
  branch, `a1 != 0` by the chart). Producer's ledger correct.
* It is *not* independent of the prior review's A2 relation: substituting
  `k*rs1^2=(96/5)a1^2` into `Tg16_6` gives the same `21/1024`. The new
  content is that the two-row combination avoids needing `5` to be a unit.
* Characteristic. The identity is over `Q`; the kill needs `21/1024` to be a
  unit, i.e. `char not in {2,3,7}`. The producer restricts to `char 0`, which
  is safe but not sharp.
* The producer's claim that the prior review simply had not looked at
  `Tg16_6` is factually right: the pinned V41 replay touches only
  `Tg11_1, Tg12_1, Tg12_2, Tg13_1, Tg13_2, Tg13_4, Tg14_1, Tg14_2, Tg14_3,
  Tg14_4, Tg15_3, Tg15_4, Tg16_5`.

## 5. The A1 ordinary branch certificate — CONFIRMED

Under `e0=e1=ee0=ell1=rs1=0` the two elimination rows are

```text
p13 = (3/8)*a1*ec3 - (3/8)*a1^2*cs1 + (3/8)*aa0*ee1          (3 terms)
p14 = -(3/32)*a1^2*rs2 + (3/8)*aa0*ec3 - (3/4)*a1*aa0*cs1
      - (3/8)*a1*ee1*ell2 + (3/32)*ee1^2                     (5 terms)
```

`deg_ec3 p13 = 1` with leading coefficient `(3/8)a1`, and after eliminating
`ec3` the row `p14` has `deg_rs2 = 1` with leading coefficient
`-(3/32)a1^2`. Both are units exactly on `D(a1)`, so the eliminations are
forced, not chosen:

```text
p13 = (3/8)*a1*(ec3 - ec3v)
p14 = -(3/32)*a1^2*(rs2 - rs2v) + (3/8)*aa0*(ec3 - ec3v)
```

with `ec3v`, `rs2v` the producer's values, both free of `ec3` and `rs2`, both
sigma-homogeneous of the correct weights (8 and 4). Verified.

The reduced rows have term counts `15:7, 17:9, 18:10, 19:24`, matching the
banked census, and depend on exactly five variables `a1, aa0, cs1, ee1,
ell2` — `k` drops out because `rs1=0`. No sparse coordinate restriction was
imposed; I confirmed the reduced rows are the *full* A1-specialized rows
(term counts before reduction: `15:8, 17:16, 18:16, 19:28`).

The compact Laurent identity `sum H_g*Fbar_g = 1` verifies, and every `H_g`
is sigma-homogeneous of weight exactly `-g` (checkable by hand: with
`a1=5, aa0=6, cs1=3, ee1=7, ell2=2` each of the eight `H15` monomials has
weight `-15`, etc.). So it is not an inhomogeneous normalization artifact.

**Independent lift.** Rather than replay the producer's divided differences I
divided `D = sum H_g*P_g^{raw} - 1` by `ec3 - ec3v` and then by `rs2 - rs2v`
with the ordinary division algorithm, obtaining `q3, q2` with zero remainder,
and set

```text
H13 = -(8/3)*a1^-1*q3 - (32/3)*aa0*a1^-3*q2,      H14 = (32/3)*a1^-2*q2,
```

which is what the two displayed factorizations of `p13`, `p14` force. The
resulting six direct multipliers are **hash-identical** to the banked
`direct_multiplier_sha256` for all of `13,14,15,17,18,19`, as are the four
`reduced_sha256`, the `branch_cover` hash and the `a2.combination` hash — all
recomputed from my own objects. Term counts `17, 8, 8, 3, 1, 1` reproduce.

**Denominator clearing.** Minimal `a1` exponents are
`13:-8, 14:-8, 15:-8, 17:-6, 18:-5, 19:-5`, so `N = 8` is right and tight
(three multipliers attain it). After multiplying by `a1^8` no negative
exponent survives, and

```text
a1^8 = H13'*Tg13_1|A1 + H14'*Tg14_2|A1 + H15'*Tg15_3|A1
       + H17'*Tg17_5|A1 + H18'*Tg18_6|A1 + H19'*Tg19_7|A1
```

holds coefficientwise. Singular confirms independently: `CERT_RESIDUAL=0`.

**Two hostile checks that pass.**

* *Only `a1` is inverted.* I audited every monomial of every uncleared
  multiplier: `a1` is the **only** variable ever carrying a negative
  exponent. There is no hidden division by `aa0`, `ee1`, `cs1` or `ell2`.
  The ledger line is accurate.
* *Integrality.* The lcm of the denominators of the six cleared multipliers
  is **1** — they are integer polynomials — and the A1 rows have denominators
  dividing `2^8`. So the certificate is valid over `Z[1/2]`, i.e. in **every
  characteristic except 2**, not merely over `Q`. This is a strengthening the
  producer does not claim.

## 6. Are the six multipliers really applied to raw rows? — yes

This was checked at four levels, because a dual-as-primal or
quotient-substitution error is exactly the failure mode this certificate
shape invites:

1. In the producer's code the final sums use
   `direct_rows = {13: p13, 14: p14, **raw_diagonal}`, where `raw_diagonal`
   is the frozen row with only the five branch variables zeroed — **no**
   elimination substitution, no dual functional, no quotient representative.
2. My independent rebuild of `p13, p14, raw_diagonal` from the frozen bytes
   reproduces the identity.
3. Singular re-verifies it from serialized raw rows in a separate engine.
4. **Scope probe.** Applying the *same* cleared multipliers to the
   **unspecialized** rows gives

```text
sum H_g' * Tg_g  -  a1^8   =   a 968-term polynomial,
every term of which is divisible by one of e0, e1, ee0, ell1, rs1.
```

   So the certified statement is precisely
   `a1^8 in (six rows) + (e0,e1,ee0,ell1,rs1)`, and demonstrably **not**
   `a1^8 in I_raw`. This is the cleanest available refutation of the main
   tempting overread, and it is a positive computation rather than a caveat.

## 7. The mutation control is inert; here is a real one

The banked control mutates one coefficient of `Tg19_7` and checks the fixed
certificate breaks. It cannot fail:

```text
h19 = 384*a1^-5*aa0        (a single monomial)
delta = 1*a1*aa0*cs1^2*ell2 (a single monomial)
residual = h19*delta = 384*a1^-4*aa0^2*cs1^2*ell2   (always 1 nonzero term)
```

Because `direct_sum` is already `1` and `h19` is a nonzero monomial, the
residual is `h19*delta != 0` for *any* single-coefficient perturbation of any
row with a monomial multiplier. The control carries zero information. It is
not wrong, it is empty.

**Replacement control (mine, and it passes).** Drop-one necessity, computed
by exact `std` over `Q` on the localized reduced core
`(Fbar_15, Fbar_17, Fbar_18, Fbar_19, a1*t-1)`:

```text
all four rows      : unit ideal   (= 1)          <- certificate exists
drop Tg15_3        : NOT the unit ideal
drop Tg17_5        : NOT the unit ideal
drop Tg18_6        : NOT the unit ideal
drop Tg19_7        : NOT the unit ideal
```

Every one of the four diagonal rows is genuinely load-bearing. For the
grade-19 row I also extracted an **explicit witness**, which settles the V39
question constructively rather than by dual nonmembership. Let
`K = Q[t]/(96*t^5+1)`, a degree-5 field over `Q` (`x^5+1/96` is irreducible
since `-1/96` is not a fifth power in `Q` and `Q` has no primitive fifth root
of unity). Set

```text
a1 = 1,  aa0 = t,  ee1 = -2*t^2,  cs1 = -4*t^3,  ell2 = 0,
ec3 = -2*t^3,  rs2 = 28*t^4,  e0=e1=ee0=ell1=rs1=0,  all else 0.
```

Then, evaluated on the frozen rows,

```text
Tg13_1 = Tg14_2 = Tg15_3 = Tg17_5 = Tg18_6 = 0,      Tg19_7 = -(1/4)*t^4 != 0.
```

So the five-row subsystem has a `K`-point on `D(a1)` inside the A1 branch:
the A1 branch really does survive to grade 19 and `Tg19_7` really is what
kills it. (The drop-19 locus is one-dimensional at `a1=1`, so this is not an
isolated accident.)

## 8. Defects, all non-mathematical

**D1 — inert mutation control.** As above. *Correction:* replace with the
drop-one `std` census plus the explicit `K`-witness of section 7; both are
desk-scale (0.02 s) and both are decisive.

**D2 — attribution error in section 1.** The producer writes that the prior
review's "statement that A2 survives the grade-16 prefix is not [correct]"
and that the present result "supersedes that narrow conclusion". The prior
review contains no such statement — the word "survive" does not occur in it.
What it says is that its result "is not: … closure of either A1 or A2", which
is a correct scope disclaimer about its own conclusion and remains true.
*Correction:* "`Tg16_6` was outside the earlier review's selected A2 checks;
the earlier scope statement is unaffected."

**D3 — two unrelated 24-term `Tg19_7` objects.** Section 3 gives
`Fbar_19 = Tg19_7 (24 terms)`; section 4 then invokes "V39's 24-term
`Tg19_7` compatibility residual". These are different polynomials. V39's
`R19` is `Tg19_7` reduced modulo the *other raw rows at weight 19* and
contains `rs1`, `e1`, `k`, `ell3` (e.g. `+(15/1024)*aa0*cs1*k*rs1^2`), none of
which can appear in the A1 core, whose variables are only
`a1, aa0, cs1, ee1, ell2`. The hashes differ. The producer never asserts they
are equal, but the juxtaposition invites the misreading. *Correction:* state
explicitly that the coincidence of term counts is accidental.

**D4 — the firewall list under-states the chart.** The banked `firewalls`
name only `rho=0` and "raw frozen source rows". The ordered-`a1` chart is
itself the coordinate specialization `rs=cs=c0=c1=a0=0` applied to the source
rows. That belongs in the firewall list by name, since "ordered-`a1`" encodes
it only by convention. *Correction:* add
`"the ordered-a1 chart sets rs=cs=c0=c1=a0=0"`.

**D5 — custody hardening.** The replay banks only `named_row_count: 70` and
`v37_sha256`; the 70 individual row digests live only inside V37 and the
containers it pins. The chain is closed today, but a successor should bank
the 70 digests in its own `RESULT.json` so the corpus is pinned at the leaf.
(Contrast the V37 erratum's absolute-path problem: this case's
`FREEZE.sha256` is correctly repo-relative and checks clean.)

**D6 — descriptive imprecision, no logical weight.** Section 3 calls
`Fbar_15/17/18/19` "the successive diagonal components of the rank-five
compatibility block identified by the exact symbol report". The symbol report
identifies a rank-five block `Tg{g}_3..Tg{g}_7` at *each* grade `g=14..19`;
the producer's selection is the diagonal `(g, g-12)` across grades, with
`(16,4)` skipped. Fine as a selection rule, but it is not an object the
symbol report names. The certificate does not depend on this.

## 9. Overreads tested

| tempting overread | status |
|---|---|
| `a1^8` (or any `a1^N`) is certified in the unsplit raw ideal | **false**; the same multipliers leave a 968-term residual lying in `(e0,e1,ee0,ell1,rs1)`. Independently, V37 banks `a1^4 not in I_19` at weight 20, complete for rows through 19 |
| conversely, the theorem says nothing at all about `I_19` | **also false, and worth registering.** If `V(I_19) ∩ D(a1) = ∅` over `Qbar`, the Nullstellensatz gives `a1^N in I_19 ⊗ Qbar` for some `N`, hence `a1^N in I_19` over `Q` by `Q`-linearity of membership. Combined with V37, `N >= 5`. This is **non-effective**: no bound and no certificate follows from anything here, because `e1=ee0=ell1=0` are only radical steps. It should be recorded as a consequence, never as a certificate |
| the reduced 4-row core is the banked content | no; the reduced rows are intermediates, the banked identity is on the raw A1-specialized rows |
| `Tg19_7` could be dropped or replaced by a quotient/dual representative | refuted constructively in section 7 |
| something follows for general `rho` | only this: the `rho=0` slice of the general-`rho` family has no `D(a1)` point on this chart. Nothing about `rho != 0`; the morphism is not proper, so fibre emptiness does not propagate |
| something follows for the saturated Rees chart, the honest total chart, bounded degree, Gate T, or JC2 | **no**, in every case, without the registered comparison/base-change certificate. The producer's firewall is correct |
| "over `Q`" means only `Q`-rational points | the argument is stronger: it excludes points over *every* field of characteristic not in `{2,3,7}` — in particular over `Qbar`, which is what the brief asks for. The whole frozen system is defined over `Z[1/2]` (row denominators are `2`-powers, lcm `2^15`) |

## 10. Exact scope of the confirmed statement

Let `S` be the frozen ordered-`a1` corpus: the exported source rows of grades
10--19, specialized by `rs=cs=c0=c1=a0=0` and then by `rho=0`, i.e. the 51
nonzero rows whose 70 file digests are pinned above.

**Confirmed.** For every field `K` with `char K not in {2,3,7}`, the system
`S = 0` has no `K`-point with `a1 != 0`. In particular there is no such point
over an algebraically closed field of characteristic zero.

**Confirmed, ideal-strength, at branch scope.**

```text
a1^8  in  ( Tg13_1, Tg14_2, Tg15_3, Tg17_5, Tg18_6, Tg19_7 )
          + ( e0, e1, ee0, ell1, rs1 )
```

as ordinary polynomial ideals, with explicit integer multipliers, valid over
`Z[1/2]`.

**Not established anywhere:** an unsplit `a1^N in I_19` certificate; any
statement at `rho != 0`; any saturated-Rees, base-change, honest-chart,
bounded-degree, Gate-T or JC2 consequence; identification of `I_19`, its
primary structure or its multiplicities.

## 11. Promotion

**Eligible for `AUDIT.md` promotion at the exact scope of section 10.** The
mathematics is confirmed by two independent engines and an independent lift
method, the custody chain is closed at the leaf files, the localization
ledger is accurate, and the certificate is integral. Promotion should carry
the corrections D2--D4 in the text, the replacement control D1 (or an
explicit note that the banked mutation control is inert), and the section-10
scope wording verbatim rather than the headline phrase "over `Q`", which
understates the field reach while inviting a `Q`-rational misreading.

## Disclosure

I read the producer report, the four pinned inputs, the V37 loader and its
erratum and preregistration, the V23 parser, and the frozen row corpus. I ran
my own `Fraction` replay, my own tokenizer, an ordinary division-algorithm
lift, and four short Singular scripts (longest 0.035 s wall) for
cross-engine confirmation and for the drop-one necessity census. Scratch work
lived in `/tmp`. No AWS job, no network, no `jc2-lean` access, no canonical
ledger edit; this report is the only repository file I created or modified.
