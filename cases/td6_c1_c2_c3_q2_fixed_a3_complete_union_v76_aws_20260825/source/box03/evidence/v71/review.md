# Hostile bounded review: TD6 V71 fixed-A3 q2-beta whole-`H=0` composition

Referee: independent algebraic-logic and custody pass of the frozen V71
composition claim only.  Operations used: full read of the charged V71
surfaces; full read of every producer and hostile-review report listed in
`DEPENDENCIES.sha256`; independent SHA-256 of every DEPENDENCIES, MANIFEST,
and FREEZE path; execution of the packaged `verify.py` as a standard-library
hash / verdict-marker / Boolean-cover / Bezout script; hand expansion of the
printed P3/QH Bezout polynomial; inspection of frozen leaf stdout for
`q_beta`, `q_beta'`, center, and denominator-factor banners.  No producer
execution, no CAS, solver, Lean, or other substantive computation.  Stored
PASS strings are not authority.

Claim surfaces:
`xmodel/td6-c1-c2-c3-q2-h-complete-cover-v71-20260825.md`,
`cases/td6_c1_c2_c3_q2_h_complete_cover_v71_20260825/`.

Consumed leaves, with the hostile-review scopes V71 actually uses:

```text
V64   H=0, D(U V P3 QH)     CONFIRMED
V62D  V=H=0, D(U)           CONFIRMED
V65   H=P3=0, D(U)
      H=QH=0, D(U)          CONFIRMED
V70   whole raw U=0         CONFIRMED
```

---

## Charge 1 — Immutability, verdicts, leaf scopes

**Result: holds.**  Every DEPENDENCIES, MANIFEST, and FREEZE path
recomputes.  Each of the four hostile reviews ends with a lone line
`CONFIRMED` after `rstrip()`, and the confirmed leaf is the exact open
V71 consumes.  No unreviewed leaf sits in the union.

Independent SHA-256 of the V71 freeze:

| object | SHA-256 | matches |
|---|---|---|
| `README.md` | `50cd2729962f63f51e4ea42ddc793c5fadcedd27a6db46f524f1716cd512035c` | MANIFEST |
| `DEPENDENCIES.sha256` | `fd4ef22e04c9730387b9f69c44b07940bab220a2376d29001e8487e8effeb809` | MANIFEST |
| `verify.py` | `d3b3437ef0d524b63b562db521a3c983f82684ad7e7402878f2febd96ab799b4` | MANIFEST |
| `MANIFEST.sha256` | `ca23e4813e609d899716c2648920e867c3713b9103227b085ec7ecbb76b4b94b` | FREEZE |
| xmodel V71 report | `7b51c5f00a3ea9cccc485589e014e84ec61f52ba992e79590ccbf23460db3f25` | FREEZE |

All twelve DEPENDENCIES targets recompute, including the four leaf
`FREEZE.sha256` files.  Cross-check against those leaf freezes: each
pins the same producer report V71 names.

```text
V64 xmodel  096a3f67… = V64 FREEZE pin = V71 DEPENDENCIES pin
V62D xmodel 52736b96… = V62D FREEZE pin = V71 DEPENDENCIES pin
V65 xmodel  936f5470… = V65 FREEZE pin = V71 DEPENDENCIES pin
V70 xmodel  9013ec37… = V70 FREEZE pin = V71 DEPENDENCIES pin
```

Review tails, last non-empty line only:

```text
…v64-review-grok-20260825.md   CONFIRMED
…v62d-review-grok-20260825.md  CONFIRMED
…v65-review-grok-20260825.md   CONFIRMED
…v70-review-grok-20260825.md   CONFIRMED
```

Licensed scopes versus consumption:

- V64 review, exact licensed scope: `H=0, D(U*V*P3*QH)` inside the
  fixed source-typed A3 q2-beta section, with the printed `P3` and
  `QH`.  Not the four factor strata.  V71 uses precisely that open.
- V62D review: emptiness on `V=H=0, D(U)`.  Explicitly not `U=0`.
  V71 uses precisely that edge.
- V65 review: `H=P3=0, D(U)` and `H=QH=0, D(U)`.  Explicitly not
  whole curves, not `U=0`, not `V=0`, not generic `H`.  V71 uses
  precisely those two opens.
- V70 review: three-piece constructible cover of whole raw `U=0`.
  V71 uses `U=0`, hence in particular `H=U=0`.  That is a subset of
  a confirmed theorem, not a broadening.

`verify.py` printed

```text
TD6-A3-Q2-H-COMPLETE-COVER-V71 CUSTODY PASS
exact_scope=whole H=0 inside fixed source-typed A3 q2-beta
whole_A3_or_TD6_or_SP2=false
```

It is a custody and set-cover audit.  It does not import any producer
and does not divide a polynomial.  Its PASS string is not a theorem.

**Defects.**  None load-bearing.  Frozen V65/V70 *producer* reports
still say “hostile review pending”; those bytes are immutable and
historically accurate at freeze time.  V71’s authority is the later
`CONFIRMED` reviews, which it pins.

**Survival.**  Hash-closed freeze.  Four `CONFIRMED` reviews at the
exact leaves consumed.

---

## Charge 2 — Exhaustive Boolean cover of `H=0`

**Result: holds as a set-theoretic identity in affine `(C,V,U)`.**
There is no missing intersection, no reversed `D(...)`, and no
specialization of a fraction-field certificate onto a denominator
zero.

Write `H = C - 3U^2`.  The README union is

```text
V(H)
 = [V(H) ∩ D(U V P3 QH)]
   ∪ [V(H,V) ∩ D(U)]
   ∪ [V(H,P3) ∩ D(U)]
   ∪ [V(H,QH) ∩ D(U)]
   ∪ V(H,U).
```

`D(U V P3 QH)` is the standard principal open `{UVP3QH ≠ 0}`, i.e.
`D(U) ∩ D(V) ∩ D(P3) ∩ D(QH)`, matching V64’s `D(U*V*P3*QH)`.  It is
not a union of those opens.

Take a point of `V(H)`.

- If `U=0`, then `H=C`, so the point is in `V(C,U) ⊂ V(U)`.  Reviewed
  V70 empties all of `V(U)`, hence empties `V(H,U)`.
- If `U ≠ 0` and `V=0`, V62D applies on `V=H=0, D(U)`.
- If `U ≠ 0` and `P3=0`, V65 applies on `H=P3=0, D(U)`.
- If `U ≠ 0` and `QH=0`, V65 applies on `H=QH=0, D(U)`.
- If `U,V,P3,QH` are all nonzero, V64 applies on `H=0, D(U V P3 QH)`.

Those five predicates cover every 4-tuple of vanishing/nonvanishing
for `(U,V,P3,QH)`.  The packaged Boolean audit is the same split:
`not u`, `u and not v`, `u and not p3`, `u and not qh`,
`u and v and p3 and qh`.  Overlap is allowed (`any(leaves)`).

No leaf is used off its localization.

- V64 inverts the coefficient-leaf radical `{U,V,P3,QH}`.  Specializing
  it to `U=0`, `V=0`, `P3=0`, or `QH=0` would be an illegal
  fraction-field reduction.  V71 does not do that: those zeros are
  rebuilt as V70, V62D, and V65.
- V62D inverts `{U}` only.  It is not used at `U=0`.
- V65 inverts `{U}` only, in the curve field.  It is not used at
  `U=0`.
- V70 `u-h-zero` inverts `{V}` and does not specialize to the origin;
  the origin is a separate V70 leaf.  V71 consumes the reviewed
  three-piece union, not a single chart.

On `D(U)`, `V=0` forces `P3 = 128 U^6 ≠ 0` and `QH = -64 U^6 ≠ 0`.
So the V62D edge does not meet either V65 curve on `D(U)`.  That is
a consistency remark, not a missing piece: even if it did meet, both
leaves would still apply.

The cover is set-theoretic emptiness of solutions on the affine
surface `H=0`.  It is not a single identity in one function field.
The five certificates live in five different coefficient fields of
the same source section; that is the licensed representation of a
constructible cover, not a field mismatch.

**Defects.**  None.  xmodel’s “V70 `U=0`” is stronger than the
`H=U=0` piece strictly required; README’s “hence in particular
`H=U=0`” is the accurate consumption.

**Survival.**  Every affine point of `H=0` in this section lies on a
reviewed leaf used only on its stated open.

---

## Charge 3 — Same section, q-prime, original-row strength, curve parameter

**Result: holds.**  All four leaves are the same source-typed
normalized A3 section `(c1,c2,c3)=(C,V,U)` with
`q_beta = t + beta t^2 + t^{25}`, polynomial `beta`, and (where the
stage is reached) direct `q_beta' = 1 + 2 beta t + 25 t^{24}`.  Each
proves an original-row unit or incompatibility with monic gcd 1 /
residue-field unit, for every beta, on its open.  The V65 curve
parameter `T = V^2/U^3` is not identified with raw `U`.

Center typing, from the reviews and frozen stdout:

| leaf | center | ring of the certificate |
|---|---|---|
| V64 | `C=3U^2` over `Q(V,U)` | post-transport fraction field, invert `U V P3 QH` |
| V62D | `V=0`, `C=3U^2` over `Q(U)` | `E(Q(U))[beta]`, invert `U` |
| V65 | `(3 U^2, V, U)` in the P3 or QH curve field | `Q(U)[Z,V]/(Z^2-aZ-b, V^2-Z U^3)`, invert `U` |
| V70 `u-h-zero` | `C=U=0` over `Q(V)` | `E(V)[beta]`, invert `V` |
| V70 origin | `C=V=U=0` | constant field, denominator 1 |

Dual’s polynomial `H = C - 3 U^2` is the same object in every leaf.
Printed `P3` and `QH` match V71, V64, and V65 byte-for-byte:

```text
P3 = V^4 - 32 V^2 U^3 + 128 U^6
QH = V^4 +  8 V^2 U^3 -  64 U^6
```

V64 stdout factor set is exactly those two quartics together with
`U` and `V`.  No third polynomial is silently renamed.

Direct q-prime / polynomial beta:

- V64 frozen stdout: `q_beta=t+beta*t^2+t^25` and
  `q_beta_prime=1+2*beta*t+25*t^24`; all three stage banners
  `*_all_pivots_beta_independent=true`.  Residual `-k/50` with `k`
  a frozen residue-field unit (`k_coordinate_denominator_factor_set=[]`).
- V62D review Charge 1: `configure_qd(direct_qprime=True)` installs
  `Q_PRIME = {0:1, 1: BetaPoly([0,2]), 24:25}`.  `--omit-direct-qprime`
  is absent.  `solve_stage` aborts on `lead.degree != 0`.  The
  serialized unit targets `{(): 1}` after monic gcd 1.
- V65 theorem argv is `--component=p3` or `--component=qh` only.
  Stdout `direct_qprime_retained=true`, `weighted_scaling_used=false`.
  The omit stream is a separate rc-one negative control and is not
  theorem evidence.  Residual again `-k/50`.
- V70 theorem argv is `--stratum=u-h-zero` or `--stratum=origin`.
  Stdout `direct_qprime_retained=true`.  Origin never reaches
  `configure_qd` because transport already returns; that is correct,
  not a dropped `q'`.  Both residuals are beta-degree 0 with monic
  gcd 1.

Curve parameter versus raw `U`.  V65 executes

```text
T = V^2 / U^3 = Y_CURVE = Z
```

in the coefficient field `Q(U)[Z,V]/(…)`.  `RatU` inverts ambient
`U`; the unused weighted modes `b3tq` / `b3half` are excluded by
`COMPONENT in {p3,qh}`.  `QH_V_zero_forces_U_zero=true` is the
statement that `Z=0` is not a root of either T-quadratic, so `V=0`
is not on either curve in `D(U)`.  V71’s Bezout writes the same
`T=V^2/U^3` and never substitutes `T` for `U`.  Certificate chart
`U^{13}` is a power of ambient `U`, not of `T`.

Strength for the union: a residue-field unit (`-k/50` or `1`) or a
beta-degree-0 incompatibility with gcd 1 is emptiness for every
polynomial beta on that open.  There is no beta-root leftover to
carry across the cover.

**Defects.**  None load-bearing.  V62D stdout does not reprint a
`q_beta=` banner; the review’s live `configure_qd` inspect and the
shared dual pin `cf3f3f02…` are the typing evidence.

**Survival.**  One section, one family, original-row obstructions
strong enough to union.

---

## Charge 4 — P3/QH Bezout optional

**Result: the identity is correct in `Q[T]` and is not used as a
cover step.**

On `D(U)`, `P3/U^6 = T^2 - 32 T + 128` and
`QH/U^6 = T^2 + 8 T - 64`.  Hand expansion:

```text
(5T-136)(T^2+8T-64)  = 5T^3 - 96 T^2 - 1408 T + 8704
(5T+64)(T^2-32T+128) = 5T^3 - 96 T^2 - 1408 T + 8192
difference           = 512
```

so `((5T-136) QH_norm - (5T+64) P3_norm)/512 = 1`.  This matches V65
stdout `QH_P3_bezout=((5*T-136)*QH-(5*T+64)*P3)/512=1` and the
`verify.py` coefficient check (low-to-high, difference `[512,0,0,0]`).

Disjointness on `D(U)` follows: the two T-quadratics generate `1`.
V71 states that this is a consistency check, not needed for
exhaustiveness.  That is accurate.  The Boolean cover treats
`P3=0` and `QH=0` as independently covered V65 leaves.  If a
common zero existed, both unit identities would still apply; the
union does not drop the intersection on a disjointness hypothesis.

**Survival.**  Bezout holds and is logically optional.

---

## Charge 5 — V33/V69 whole-`U` defect is repaired before consumption

**Result: holds.**  V71 does not consume the withdrawn V33/V69
whole-divisor sentence.  It consumes reviewed V70.

The erratum
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-scope-erratum-20260825.md`
(pinned inside the V70 freeze as `df746976…`) withdraws “the entire
raw `U=0` center divisor is empty”.  Surviving V33/V69 algebra is
only `U=0 ∩ D(C)`, transport chart `C^2`, complete parent chart
`C^3`.  At `C=0` those pivots vanish and the old echelon cannot be
specialized.  The same erratum quarantines every all-beta composition
that used V33/V69 as whole `U=0`, including the asserted whole-`H=0`
union.

V70 rebuilds `C=U=0` over `Q(V)` (complete chart `V^3`) and the
origin (complete chart `1`) as original-row certificates, not as
`C=0` specializations of V33.  Event fingerprint: V33 numerators
`-C` at columns `193/1289`; V70 `u-h-zero` numerators `-V` at
columns `194/1290`.  The V70 review CONFIRMED the three-piece cover

```text
V(U) = [V(U) ∩ D(C)] ∪ [V(C,U) ∩ D(V)] ∪ V(C,V,U)
```

with V33 taken in its repaired scope `U=0 ∩ D(C)`.  For V71’s
`H=0` union, `H=U=0` is exactly `C=U=0`, so only V70’s own two
pieces are strictly required; citing whole reviewed `U=0` is
stronger and still valid.

V71 therefore restores the `U=0` leaf of whole `H=0` *after* the
repair gate the erratum demanded.  It does not quietly revive the
quarantined V33/V69 sentence.

**Survival.**  The V33/V69 scope defect is not in the consumed
`U=0` leaf.

---

## Charge 6 — Exact conclusion and firewall

**Result: the written conclusion is the largest statement the
union can bear, and it is not any of the refused claims.**

What survives: in the fixed source-typed normalized A3 section
`(c1,c2,c3)=(C,V,U)` with `q_beta = t + beta t^2 + t^{25}`, the
normalized compatibility system has no solution at any point of
the raw divisor `H = C - 3 U^2 = 0`, for every polynomial beta.

What is refused, in both xmodel and README, and correctly:

- `H ≠ 0` (the complementary A3 open is uncharged);
- whole A3;
- any other center / boundary / dead-stretch / F1 / pole modulus;
- TD6;
- SP-2;
- landing;
- JC2.

`verify.py` reprints `whole_A3_or_TD6_or_SP2=false`.  Each leaf
already printed the corresponding denials on its own open
(`whole_raw_stratum_killed=false`, `whole_V_H_zero_edge_empty=false`,
`component_all_beta_killed=false`, `full_A3_beta_family_killed=false`).
V71’s new content is only the Boolean union of those reviewed
opens.  It performs no new elimination.

xmodel’s phrase “normalized TD6 compatibility system” names the
compatibility system of this TD6 A3 q2-beta section, not a TD6
theorem.  The firewall sentence immediately blocks the broader
reading.

**Survival.**  Whole `H=0` in this fixed A3 q2-beta section, for
every beta, and nothing stronger.

---

## Attempted flips that did not kill the composition

| attack | outcome |
|---|---|
| Unreviewed leaf | Four reviews end `CONFIRMED` at the consumed opens.  V33 is an internal piece of reviewed V70, and is not even required for `H=U=0`. |
| Hash drift | All DEPENDENCIES / MANIFEST / FREEZE paths recompute; leaf FREEZE pins match the producer reports V71 names. |
| Reversed `D(U V P3 QH)` | V64 Boolean is `u and v and p3 and qh`, the intersection of principal opens, matching the denominator radical. |
| Specialize V64 to a factor zero | Not done.  Factor zeros are V62D / V65 / V70 rebuilds. |
| Specialize V33 through `C=0` | Not done.  V70 rebuilds `C=U=0` and the origin. |
| Identify `T` with raw `U` | V65 field is `Q(U)[Z,V]/(…)`, `T=Z=V^2/U^3`; unused weighted modes excluded; V71 Bezout keeps that `T`. |
| Missing `P3=QH=0` intersection | Empty on `D(U)` by Bezout; covered independently even if not. |
| Missing `V=P3=0` on `D(U)` | Empty: `P3(V=0)=128 U^6`.  V62D would still cover `V=0`. |
| Field / extension mismatch | Five coefficient fields of one source section; the claim is a set-theoretic union, not one fraction-field identity. |
| Dropped direct `q'` | Frozen theorem streams retain it; origin dies in transport before `configure_qd`.  Omit streams are controls. |
| Beta-root leftover | Every leaf residual is degree 0 with monic gcd 1, or the residue-field unit `-k/50`. |
| H / P3 / QH definition mismatch | Same three polynomials on V71, V64, V65, V62D dual, and V70 dual. |
| Cover relies on disjointness | Boolean `any(leaves)`; xmodel and README say disjointness is optional. |
| Quiet whole-A3 / TD6 / SP-2 / landing / JC2 | Explicitly denied. |
| Consume quarantined V33/V69 whole-`U` | Consumes V70 `CONFIRMED` instead. |
| `endswith("CONFIRMED")` matching `CONFIRMED_WITH_REPAIRS` | False: that token ends in `REPAIRS`.  All four files end in a lone `CONFIRMED`. |

None of these flips.

---

## Leftover nits (not load-bearing)

1. Frozen V65/V70 producer reports still say “hostile review pending”.
   Historical at those freezes; V71 pins the later reviews.
2. `verify.py` `endswith("CONFIRMED")` would also accept a file
   ending `NOT CONFIRMED`.  The four actual tails are a lone
   `CONFIRMED` line.  The script does not recursively replay leaf
   FREEZE contents; it hashes the FREEZE files themselves.
3. V64 xmodel producer never prints the words `q_beta`; the case
   README and frozen stdout do.  V62D stdout has no `q_beta=`
   banner.
4. xmodel “unit-certified” is slightly loose for V70’s
   incompatibilities; README’s “unit/incompatibility” is exact.
5. xmodel cites whole `U=0` rather than the strictly necessary
   `H=U=0`.  Logically valid, slightly broader than the H-cover
   needs.
6. V65 README still carries “hostile review pending” as frozen
   status.

None of these reverses the licensed identity or requires a
theorem-scope erratum.

---

## Survival statement

The frozen V71 package is a hash-closed, review-gated Boolean
composition, not new elimination.  In the fixed source-typed
normalized A3 q2-beta section `(c1,c2,c3)=(C,V,U)`,

```text
V(H) = V64(H ∩ D(U V P3 QH))
     ∪ V62D(H ∩ V=0 ∩ D(U))
     ∪ V65(H ∩ P3=0 ∩ D(U))
     ∪ V65(H ∩ QH=0 ∩ D(U))
     ∪ V70(U=0).
```

Each summand is a `CONFIRMED` original-row emptiness theorem on
exactly that open, with polynomial beta and retained direct
`q_beta'` as required.  The P3/QH Bezout is correct and unused by
the cover.  The withdrawn V33/V69 whole-`U=0` sentence is not
consumed; reviewed V70 is.  The conclusion is emptiness of the
normalized compatibility system on all of `H=0` in this section,
for every beta.  It is not `H≠0`, whole A3, another modulus, TD6,
SP-2, landing, or JC2.

No theorem-scope repair is required.  The nits above are custody
and expository only.

CONFIRMED
