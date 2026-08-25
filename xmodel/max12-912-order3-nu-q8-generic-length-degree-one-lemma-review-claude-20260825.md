# Hostile review: generic length 190 implies degree one and all Q8 contacts

Date: 2026-08-25  
Reviewer: Claude (independent hostile algebraic-geometry and computational-algebra
referee; no producer role)  
Prompt executed:
`xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-review-grok-20260825-prompt.md`,
under the claude wrapper
(`...-review-claude-20260825-prompt.md`), which directs the output to this
file.  No producer file, case, manifest, or ledger was edited; the grok output
path was not written.  
Status: **REVIEW COMPLETE**

## Verdict summary

**CONFIRMED_WITH_REPAIRS** (token repeated alone on the final line).

The theorem under review is the conditional implication: *assume* the exact
generic endpoint

```text
dim(A)=0,  length_K(A)=vdim=190,  source_fail=0        (1)
```

over `K=F_127(w)` for the displayed localized seven-variable ideal, and
*consume* the three frozen inputs (H geometrically integral and monic of
`v`-degree 190; a reviewed `H`-image source component over `kbar`; the unit
full relative `8x8` Jacobian at the eight corrected-Q8 contacts).  Then the
localized source over `Fbar_127` has a unique `w`-dominant component, of cycle
multiplicity one, birational onto `H`, containing all eight contacts.

I attacked every load-bearing step per the prompt's eight items and found **no
mathematical error and no counterexample**.  The seven-variable and
eight-variable presentations are isomorphic over `k[w]` by explicit two-sided
maps (not a one-way substitution); the length accounting over `kbar(w)` is
exact with no hidden separability, embedded-point, or multiplicity assumption;
the contact-branch argument is a correct etale/IFT argument in which `w` is
genuinely the uniformizer; and local-to-global passage of the contact branch
into the generic fibre is forced by regularity plus `w`-dominance.  The
conclusion stated is the exact strongest one available, and the firewall is
complete.

Repairs are required only at the provenance/wording tier: the lemma calls all
three consumed inputs "already reviewed/frozen", but the repository contains
no hostile review of the candidate-plane-integrality producer or of the
full-contact-Jacobian certificate, and both of those producer files carry
explicit "review required" status lines.  The pending endpoint (1) is a
declared missing computational premise, exactly as the lemma states — it is
not a flaw in the conditional mathematics.  I did not treat (1) as true
anywhere in this review.

## Files read (read-only)

Required by the prompt, in full:

- `xmodel/max12-912-order3-nu-q8-generic-length-degree-one-lemma-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-component-reviewed-successor-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md`
- `cases/max12_912_order3_nu_q8_generic_vertical_length_aws_20260825/generate.py`
- `cases/max12_912_order3_nu_q8_generic_vertical_length_orders_aws_20260825/generate_variant.py`

Supplementary interface verification (read-only):

- `xmodel/max12-912-order3-nu-q8-sparse-contact-component-lemma-20260825.md`
  (chart definition consumed by the reviewed successor)
- `xmodel/max12-912-order3-nu-q8-sparse-contact-component-review-claude-20260825.md`
  (the review the successor incorporates; its scope statements are load-bearing
  for Finding R1 below)
- `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py`
  (lines 1-141: `compile_quotient` contract — names order, imposed rows,
  Fraction scalars — against which `generate.py`'s `substitute()` was audited)
- Directory listings of `xmodel/` and the self-contained count case, plus
  targeted greps of `xmodel/*review*.md`, to establish which producers have
  review files (none exist for the plane-integrality or full-contact files).

## Execution disclosure

This review session has no shell.  I did not recompute any SHA-256, did not
run Singular, and executed no replay or producer script.  Computational facts
inside the frozen producer files (factor degrees, residual zeros, gcd/norm
units, the pinned hashes themselves) are consumed as frozen attestations;
hash cross-references were checked by eye only.  Every verdict below rests on
hand algebra over the displayed presentations plus those attestations.  The
pending endpoint (1) is treated strictly as an assumption.

---

## Item-by-item audit

### 1. Seven-variable generic ideal = eight-variable full-contact source — VERIFIED (two-sided isomorphism over `k[w]`)

Three presentations are in play.  Write `k=F_127` and suppress the six divided
rows `e1,e3,e5,e7,e2,e4` (variables `w,c,d2,d4,x1,x3,x5` only; they involve
neither `inv`, `v`, nor `u`):

- `S` (chart of the sparse/component chain):
  `k[w,c,d2,d4,x1,x3,x5][t]/(rows, t*x5*(x3-2*x5)-1)`, with chart function
  `v=(x3-2*x5)/x5`;
- `X8` (full-contact presentation):
  `k[w,c,d2,d4,x1,x3,x5,inv,v]/(rows, f1, f2)` with
  `f1 = v*x5-x3+2*x5`, `f2 = inv*x5*(x3-2*x5)-1`;
- `X7` (generic producer): `k[w,u,c,d2,d4,x1,x5,v]/(rows', eloc)` where
  `rows'` = rows after `x3 -> (v+2)*x5` and `eloc = u*x5*v-1`.

**`X7 ≅ X8`.**  Define `phi: X8 -> X7` on coordinates by `x3 |-> (v+2)*x5`,
`inv |-> u^2*v`, all else fixed; and `psi: X7 -> X8` by `u |-> inv*x5`, all
else fixed.  Well-definedness: `phi(f1)=0` identically;
`phi(f2) = u^2*v*x5*(v*x5) - 1 = (u*x5*v)^2-1 = (eloc)(u*x5*v+1) ≡ 0`;
`psi(rows') = rows mod f1`; `psi(eloc) = inv*x5^2*v - 1 ≡ 0` because `f1`
turns `x3-2*x5` into `v*x5`, so `f2` reads `inv*x5^2*v = 1`.  Composites:
`u |-> inv*x5 |-> u^2*v*x5 = u*(u*x5*v) = u`;
`inv |-> u^2*v |-> inv^2*x5^2*v = inv*(inv*x5^2*v) = inv`;
`x3 |-> (v+2)*x5 = x3` by `f1`.  Both composites are the identity, so this is
an isomorphism of `k[w]`-algebras — no `w` appears in any substitution and no
denominator is used.  It therefore identifies integral models, every local
ring (in particular at the `w=0` contacts), and the generic fibres.  This
answers the prompt's "isomorphism rather than one-way substitution" demand.

**`S ≅ X8`.**  Send `t |-> inv`; conversely `inv |-> t`,
`v |-> t*(x3-2*x5)^2` (on `S`, `x5^{-1} = t*(x3-2*x5)`, so this is the chart
ratio).  Checks: `f1 |-> (x3-2*x5)*(t*x5*(x3-2*x5)-1) = 0`; `f2 |->` the
localizer of `S`; and in `X8`,
`inv*(x3-2*x5)^2 = inv*(x3-2*x5)*(v*x5) = v*(inv*x5*(x3-2*x5)) = v`, so both
composites are identities.  Hence the chart of the reviewed component theorem
(`x5*(x3-2*x5) != 0`, i.e. `x5 != 0` and `v != 0`) **is** the open set of the
generic presentation: on `X7`, `eloc` makes each of `u, x5, v` a unit
(`x5^{-1}=u*v`, `v^{-1}=u*x5`, `u^{-1}=x5*v`); on `X8`, `f2` makes
`inv, x5, x3-2*x5` units and `f1` makes `v` a unit.  The lemma's sentence "on
this open set `x5` and `v` are units" is correct and complete: localizing at
`x5*v`, at `x5^2*v`, or at `x5*(x3-2*x5)` gives the same multiplicative
saturation, hence the same open subscheme.

**Producer code audit.**  `generate.py` substitutes
`x3^e = ((v+2)*x5)^e = sum_k C(e,k)*2^(e-k) * v^k * x5^e` — the code's
exponent tuple `(0, ec, ed2, ed4, ex1, ex3+ex5, kv)` and coefficient
`comb(ex3,kv)*2^(ex3-kv)` implement exactly this, with the `w`-degree routed
into the parameter coefficient (ring `(127,w)`), matching the tuple order of
the hash-pinned compiler's `names=["w","c","d2","d4","x1","x3","x5"]`
(verified against `compile_quotient`).  Fail-closed elements verified by
reading: compiler SHA pin `22b0cd...` (the same pin the sparse/breadth chain
carries, tying (1)'s ideal to the six rows of the component theorem),
`imposed=(1,3,5,7,2,4)` and `names` tripwires, `mod_scalar` raising on
`p | denominator`, `vdim` printed only when `dim==0`.  The variant adapter
hash-pins the base generator and only permutes variable order / term order /
algorithm, none of which can change `dim` or `vdim`.  Two hygiene defects
(both harmless to the conditional mathematics) are recorded as R4:
`input_term_counts=9,20,33,57,14,29,2` is printed but never measured, and the
adapter's fourth textual patch has no occurrence-count anchor.

### 2. Base change to `kbar(w)` and the support prime — VERIFIED

`dim_K(A)=190` gives `dim_Kbar(A ⊗_K Kbar)=190` for **any** field extension;
nothing more is claimed by (2).  Note `Kbar := kbar(w)` is *not* an algebraic
closure of `K` and the argument never needs it to be (Finding R3 asks for a
half-line saying so).

`E = Kbar[v]/(H)` is a field of degree exactly 190: `H` is irreducible in
`kbar[w,v]` (consumed input 1), monic in `v`, and `kbar[w]` is a UFD, so by
Gauss any factorization over `kbar(w)` descends to monic factors in
`kbar[w][v]` — hence `H` stays irreducible over `kbar(w)`.

The reviewed component `C` (consumed input 2) has cycle-theoretic plane image
`H`; since `C` is an irreducible curve and its image closure is the curve
`V(H)`, the map `C -> V(H)` is dominant, hence generically finite.  `V(H)`
surjects onto `A^1_w` (`H` monic in `v`: every fibre is nonempty), so `C` is
`w`-dominant and its generic point `eta_C` lies over the generic point of
`A^1_w`.  The generic fibre of the localized source is exactly
`Spec(A ⊗_K Kbar)`:

```text
O(X7 ⊗_k kbar) ⊗_{kbar[w]} kbar(w) = O(X7) ⊗_{k[w]} kbar(w)
                                   = (O(X7) ⊗_{k[w]} k(w)) ⊗_{k(w)} kbar(w)
                                   = A ⊗_K Kbar,
```

so `eta_C` **is** a support prime of the exact generic algebra, with residue
field `L = kbar(C)`, and `E` embeds `Kbar`-linearly into `L` by `w |-> w`,
`v |-> v` (in the `X7` coordinates the plane map is literally `(w,v)`).  The
chart identity needed for input 2 to apply to *this* algebra is Item 1.  Since
`C` is an integral curve, its generic-fibre trace is the single point
`Spec kbar(C)` (every closed point of `C` has residue field `kbar`, hence lies
over a closed point of `A^1_w`), so one component supplies exactly one support
prime.

### 3. The formula `m*[L:Kbar] = m*d*190` — VERIFIED

For any finite-dimensional `Kbar`-algebra `B`: `B` is Artinian, splits as a
product of local factors `B_P`, and every composition factor of `B_P` as a
`B_P`-module is `kappa(P)`; hence

```text
dim_Kbar(B) = sum_P  l(B_P) * [kappa(P):Kbar],
```

exactly, with no reducedness, separability, or excellence input.  Attacks and
outcomes:

- *Scheme multiplicity vs cycle multiplicity*: `m := l((A⊗Kbar)_P)` and
  `(A⊗Kbar)_P = O_{X7_kbar, eta_Z}` (a localization of a localization; the
  order is immaterial), so `m` is simultaneously the generic-fibre local
  length and the coefficient of `Z` in the fundamental cycle of the localized
  source.  `m=1` is therefore genuinely "cycle multiplicity one" and gives
  generic reducedness along `Z`.
- *Embedded points*: in the zero-dimensional algebra `A⊗Kbar` every prime is
  maximal, and any `w`-dominant embedded prime of the localized source would
  itself appear as a support point of the generic fibre, charged by the same
  ledger (and annihilated by the exact total, Item 5).  Embedded primes
  supported over special `w`-values never meet the generic fibre and are
  irrelevant to the statement.
- *Nonreduced Artin factors*: absorbed by `m`.
- *Inseparability*: `d=[L:E]` is the full field degree; `[L:Kbar]=190*d`
  holds by multiplicativity regardless of separability.  In dimension zero
  the Hilbert-Samuel multiplicity equals the length, so no alternative
  reading of "multiplicity" changes (3).
- *Residue field vs cycle degree*: correctly separated as `d` vs `m`; the
  pushforward degree onto `H` is `m*d`, forced to `1*1`.

The forcing step is exact integer arithmetic: `m*d*190 <= 190` with
`m,d >= 1` gives `m=d=1` and leaves total length `0` for every other support
point; each additional point would contribute at least `[kappa:Kbar] >= 1`.

### 4. Geometric integrality of `H` — LOGIC VERIFIED; PROVENANCE TIER MISLABELED (R1)

I re-derived both arguments of the integrality producer by hand:

- *Arithmetic irreducibility*: `H` monic in `v` over the integrally closed
  `F_127[w]` forces monic factors in `F_127[w][v]` (Gauss); monicity preserves
  `v`-degrees under `w=25` and `w=47`; the proper nonzero subset sums of
  `{2,188}` and `{1,3,186}` are `{2,188}` and `{1,3,4,186,187,189}`, which are
  disjoint.  Correct, given the frozen factor degrees.
- *Geometric integrality*: the Galois orbit of a geometric component of an
  `F_127`-irreducible curve is transitive; the Galois-fixed point `(71,50)`
  would lie on every conjugate component (or on a repeated component), making
  `grad H` vanish there; `H_v(71,50)=104 != 0` refutes both splitting and a
  repeated factor.  Correct, given the frozen point and derivative values.

*Frobenius/constant-field attack*: over `kbar`, conjugate source components
mapping to conjugates of `H` all map to `H` itself (`H` has `F_127`
coefficients), so each contributes at least `190` to (2); several components
contributing "less than 190 each" is impossible because every `H`-dominant
component's residue field contains the full degree-190 field `E`.  A
component mapping onto a proper geometric factor of `H` cannot exist because
no such factor exists.  The lemma's one-line orbit remark is sound.

**However**: the integrality producer file's own status line reads
"hostile different-model review required"; no review file for it exists in
`xmodel/` (checked this session by directory listing and grep); and the
review-cleared sparse-contact review explicitly recorded the `H` facts as
"a dependency, not verified by this review".  The lemma's framing of this
input as "already reviewed" is therefore wrong.  See R1.  This review has now
hand-audited the producer's *mathematics*; its *computations* remain
unreplayed by any reviewer.

### 5. Uniqueness: multiplicity one, degree one, no other `w`-dominant component — VERIFIED

Given (1)+(2), the single point `P=eta_C` already consumes
`m*d*190 = 190`, so `Spec(A ⊗ Kbar) = {P}`, `(A⊗Kbar)_P = kappa(P) = E`;
equivalently the strongest scheme-theoretic form holds:

```text
A ⊗_K Kbar ≅ E = kbar(w)[v]/(H)   as Kbar-algebras,
```

i.e. the geometric generic localized source is the one reduced point with
residue field exactly the function field of `H`.  Distinct components have
distinct generic points, and every `w`-dominant component (of any dimension —
a `>= 2`-dimensional one would force `dim(A) >= 1`, contradicting (1))
places its generic point in `Spec(A⊗Kbar)`; hence exactly one `w`-dominant
geometric component exists in the chart, with multiplicity one and
source-to-`H` degree one.  Geometric uniqueness is the stronger statement:
`Spec(A⊗Kbar) -> Spec(A)` is surjective, so `Spec(A)` is also a single point
and uniqueness over `F_127(w)` follows a fortiori; no appeal to descent is
needed anywhere.  The lemma claims exactly this list and nothing stronger.

### 6. Contact local rings `kbar[[w]]` — VERIFIED (with a hand determinant-structure check)

Ambient count: 9 coordinates including `w`; 8 equations (six rows + `f1` +
`f2`); the certificate attests all 8 vanish at the corrected section over
`A = F_127[v]/(Q8bar)` (squarefree, so 8 distinct geometric contacts) and
that the full relative `8x8` Jacobian in `(c,d2,d4,x1,x3,x5,inv,v)` has
determinant with `gcd(det,Q8bar)=1` and norm `88 != 0`, i.e. a unit at every
conjugate contact.  By the Jacobian criterion this makes `X8 -> A^1_w` etale
at each `q_i` (valid in any characteristic; no separability caveat at a
rational point), so

```text
Ohat_{X8_kbar, q_i} ≅ kbar[[w]]    as kbar[[w]]-algebras,
```

which is precisely (4): the maximal ideal is generated by `w`, so `w` itself —
not a ramified parameter — is the uniformizer, and the residue field is
`kbar`.  By Item 1's `k[w]`-isomorphism this is a statement about the same
localized source whose generic algebra is `A`; the localizer is among the
eight equations, and the certificate's unit ledger
(`v, 9*v, 3v^2-2, 3v^2+3v+1, x5, x3-2x5, x5*(x3-2x5)`, normal `3x3`
determinant — all with gcd 1 against `Q8bar`) licenses every denominator in
the section and places all eight contacts inside the chart.

Structural cross-check done by hand: the six rows have zero `inv`- and
`v`-derivatives, `f2` has zero `v`-derivative, `f1` has zero `inv`-derivative;
Laplace expansion along the `inv` column and then the `v` column gives

```text
det J_8x8 = ± x5 * [x5*(x3-2*x5)] * det J_6x6(rows; c,d2,d4,x1,x3,x5),
```

so on the chart the `8x8` unit is exactly equivalent to the `6x6` unit used
at charged fixed-fibre points in the reviewed successor — the two Jacobian
certificates in this chain are mutually consistent, and the `8x8` form is the
right one for the full presentation including the localizer.  The negative
control (corrupting `(3v+1)/(9v)` to `1/(27v)` makes all six residuals
nonzero) shows the residual check is not vacuous.  Tier caveat: this
certificate is producer-exact and unreviewed (R1); its internal logic is
sound as audited here, its arithmetic consumed as frozen.

### 7. Survival of the contact branch in the generic localized fibre — VERIFIED

Fix a contact `q_i`.  Completion `kbar[[w]]` is regular, so
`O_{X7_kbar, q_i}` is a regular (hence domain) local ring of dimension one.
Consequences, each closing one attack from the prompt:

- *Unique branch / local-to-global passage*: a regular local ring has one
  minimal prime, so exactly one irreducible component `W` of the localized
  source passes through `q_i`, reduced there; there is no analytic-vs-Zariski
  branch mismatch because the local ring itself is a domain.
- *Vertical component*: `O -> Ohat` is injective (Krull), and `w != 0` in
  `kbar[[w]]`, so `w` does not vanish identically on `W`; a nonconstant
  regular function on an irreducible curve makes `W -> A^1_w` dominant.  `W`
  is not vertical.
- *Removed denominators*: `q_i` satisfies the localizer (unit ledger above),
  and `W` is a component of the already-localized scheme, so no removed
  denominator can delete it; "components contained in a removed denominator"
  cannot occur inside the chart by construction.
- *Higher-dimensional special component through `q_i`*: impossible, since
  every component through `q_i` induces a chain in the dimension-one local
  ring.
- *Passage to the generic fibre*: `W` `w`-dominant puts `eta_W` in
  `Spec(A ⊗ Kbar) = {P}` (Item 5), so `eta_W = P` and
  `W = closure(P) = Z`.  Hence `q_i ∈ Z` for every `i`, and `Z` is even
  smooth at each contact.

Vertical or boundary components *away* from the contacts are genuinely not
classified by this argument; the lemma says so explicitly, which is the
correct scope.

### 8. Exact strongest conclusion and firewall — VERIFIED

The lemma's conclusion (unique `w`-dominant geometric component; cycle
multiplicity one; degree one onto `H` as equality of function fields; all
eight corrected-Q8 contacts on it) is exactly equivalent to
`A ⊗_K Kbar ≅ E` plus the eight containments, which is the strongest
statement the premises support.  "Degree one" is correctly cashed out as
birationality / function-field equality: the internal coordinates become
rational functions in `kbar(H)`, with **no** claim of regularity at the
projective boundary — and the firewall paragraph explicitly withholds
projective-boundary regularity, characteristic-zero no-merger, integral
specialization of the characteristic-zero branches, identity with the
primitive-grouping/infinity components, both Taylor families, the terminal
differential row, rational trajectories, maximum-12, and JC2.  Checked item
by item against the prompt's required firewall list: complete.  The
characteristic-127-only caveat is present.

Useful corollary for the race operators (not a defect): an *accepted*
endpoint with `vdim < 190` would contradict consumed inputs 1–2 (they force
length at least 190), i.e. it would signal an upstream defect or chart
mismatch, not a smaller theorem; an accepted `vdim > 190` would leave this
lemma silent (its conclusion genuinely needs equality).  The gate's insistence
on exactly `190` is the mathematically correct trigger.

---

## Findings and exact repairs (ranked)

**R1 [required — provenance wording in the lemma].**  Where: Section 1,
"Consume these already reviewed/frozen inputs", and the sentence "The
conclusion below is conditional only on (1)...".  Facts established this
session: input 2's producer (the reviewed successor) is review-cleared; input
1's producer (`p127-candidate-plane-integrality`) and input 3's producer
(`p127-full-contact-jacobian-aws`) both carry "review required" status lines,
no review file for either exists in `xmodel/`, and the cleared
sparse-contact review states in terms that the `H` facts were "a dependency,
not verified by this review" and that the full-contact certificate was "not
used in the count".  Labeling these two inputs "already reviewed" is false.
Exact replacement wording:

> Consume these frozen inputs: (1) `H(w,v)` is geometrically irreducible,
> monic of `v`-degree 190, over `k` — producer-exact certificate, hostile
> review pending; (2) over `kbar`, at least one irreducible component of the
> same localized source has plane image `H=0` — review-cleared; (3) at each
> of the eight corrected-Q8 contacts at `w=0`, the full eight-equation source
> presentation and localizer vanish and the relative `8x8` Jacobian is a unit
> — producer-exact certificate, hostile review pending.

and

> The conclusion below is conditional on (1) and on the truth of the three
> frozen inputs at their stated certification tiers; among *pending
> computational endpoints* it is conditional only on (1).

This repair changes no mathematics — the implication audited here assumes the
inputs true, as the prompt directs — but a provenance-gated ledger must not
carry a false review-status assertion.  Mitigation recorded: this review has
now hand-verified the internal mathematical logic of both unreviewed
producers (Items 4 and 6); their computations remain unreplayed.

**R2 [recommended — one sentence, Section 3].**  Replace

> That branch is `w`-dominant; because the localizer is a unit at `q_i`, its
> generic point survives in `A tensor_K Kbar`.

with

> That branch lies in the localized chart because the localizer is a unit at
> `q_i`, and it is `w`-dominant; hence its generic point lies in the generic
> fibre `Spec(A tensor_K Kbar)`.

Survival needs both facts; as written the causal clause is attached to the
wrong one.  (The mathematics around it is correct.)

**R3 [recommended — notation half-lines, Sections 1–2].**  State that
`Kbar` denotes `kbar(w)`, which is not an algebraic closure of `K` and is
nowhere required to be; and that `length_K(A)` means `dim_K(A)` (= Singular
`vdim`), the quantity the decomposition `sum m_P [L_P:Kbar]` computes.

**R4 [recommended — pending-lane hygiene; premise side only].**
(a) `generate.py` prints `input_term_counts=9,20,33,57,14,29,2` without
measuring it; either assert the counts in the generator or exclude the line
from any acceptance matching.  (The drop from the sparse supports
`10,20,35,57,16,29` is consistent with monomial merges under
`x3 -> (v+2)x5`, but nothing checks this.)  (b) The acceptance gate should
add a no-conflicting-endpoint clause: if any completed race lane reports
`dimension` or `vdim` different from (1), fail closed pending adjudication —
all six lanes are pure-Singular executions, term-order/algorithm diversity is
not implementation independence, and a single accepted endpoint is the trust
boundary as worded.  (c) `generate_variant.py`'s fourth textual replacement
(the `term_order` print augmentation) lacks the occurrence-count anchor the
other three patches have; harmless while the base hash pin holds; note only.

No finding rises above wording/hygiene.  There is no mathematical repair.

## Missing computational premise vs flaw in the conditional mathematics

- **Missing premise**: exactly (1).  No generic-length lane has completed; six
  AWS pure-Singular races are pending; the lemma's Sections 1 and 5 say this
  plainly, and its acceptance gate correctly rejects timeouts, partial bases,
  and fixed-fibre lengths.  Nothing in this review treats (1) as true, and
  the lemma supplies no unconditional component claim.
- **Flaw in the conditional mathematics**: none found.  Refutation attempts
  and their outcomes: one-way substitution (closed: explicit two-sided
  `k[w]`-isomorphisms, Item 1); chart mismatch with the component theorem
  (closed: `S ≅ X8 ≅ X7`, Item 1); inseparable source-to-`H` degree (closed:
  full field degree used, Item 3); nonreduced/embedded generic structure
  (closed: exact Artinian length decomposition, Items 3, 5); constant-field
  or Frobenius splitting (closed: geometric integrality of `H` plus the
  `>= 2*190` count, Item 4); a second `w`-dominant component or a
  higher-dimensional dominant component (closed: exact total 190 and
  `dim(A)=0`, Item 5); ramified uniformizer or wrong completed ring at a
  contact (closed: etale over `A^1_w`, Item 6); contact branch vertical,
  boundary-trapped, or lost between local and global (closed: regularity plus
  `w`-dominance, Item 7); overreach in the conclusion (closed: firewall
  complete, Item 8).  Accordingly there is no counterexample to exhibit: the
  smallest candidate degeneracies (a length-`>=2` Artin factor at `P`, a
  degree-2 `L/E`, a conjugate pair of components, a vertical branch through a
  contact) are each directly annihilated by the exact count `190 = 190`.

## Custody notes (citation level; hashes not recomputed)

- `generate.py` pins `quotient_compiler.py` at `22b0cd...` — the same
  compiler hash the sparse mixed-volume supports and breadth lanes pin
  (per the cleared sparse review), so the pending endpoint's six rows are
  provably the component theorem's six rows.
- `generate_variant.py` pins `generate.py` at `e688ff...` and refuses on
  anchor-count drift for three of its four patches (R4c).
- The successor cites the sparse review at SHA `ebd002...` with verdict
  "CONFIRMED WITH REPAIRS"; that file exists and its repair list matches what
  the successor incorporates.
- Hand arithmetic re-verified where consumed: `80*8+64=704>658`;
  `75*8+64=664>658`; `80*8=640<658`; `2+188=190`; `1+3+186=190`;
  `{2,188} ∩ {1,3,4,186,187,189} = {}`; `9=3^2`, `27=3^3`, `36`, `2`, `104`,
  `88` all nonzero mod 127.

## Conclusion

Conditional on the exact generic endpoint (1) and on the truth of its three
frozen inputs, the lemma's chain — base-change length preservation, the
degree-190 field `E`, the exact Artinian ledger forcing `m=d=1` and an empty
remainder, the etale contact local rings, and the forced passage of each
contact branch into the unique generic component — is correct at every step,
and its stated conclusion is the exact strongest one available with the
firewall fully intact.  The required repairs are provenance and wording only
(R1 foremost: two of the three consumed inputs are not "already reviewed");
the pending endpoint is a missing computational premise by design, not a
defect.  With R1 applied (and R2–R3 recommended), the conditional lemma
stands.

CONFIRMED_WITH_REPAIRS
