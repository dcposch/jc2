# Hostile review: K00 ramified `(e,m)` calendar and finite-transition-type gate

Date: 2026-08-30 UTC
Reviewer: Opus 5 (different model from the Sol 5.6 Ultra producer)
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c` (verified `git rev-parse HEAD`)
Targets:
`xmodel/k00-ramified-em-calendar-finite-type-gate-sol56-20260830.md`
`xmodel/k00-ramified-em-calendar-meta-replay-sol56-20260830.py`

## 0. Verdict

**CONFIRM_WITH_CORRECTIONS.**

Every exact mathematical assertion in the artifact that I could reduce to the
frozen source is correct, and I reproduced the charged certificate **byte for
byte from an independent code path** (my own JSON parser, my own sparse
`Q[d0..d5]` arithmetic, my own graph substitution, my own Pareto routine):
3812 bytes / `afb3979a091647fb1c2567c06295400358bf84d65387cc6447faabb92231f501`.
The 569-tail census, the raw degree stencil (1.1)/(1.2), the whole §3
bidegree antichain table, the exact-graph surface table, the six tie
equations (4.1), the five congruences (4.2), the band thresholds, and the
`(2,9)`/`(4,18)` countercontrol all hold.

Ten corrections follow. None refutes a displayed equation. Two are material
to how the artifact may be consumed: the verdict string invites a reading the
artifact does not support (C1), and the priority ranking in §8 is wrong by its
own metric (C8). The rest are scope, labelling, and retention-list repairs.

Nothing here promotes `e=2,m=2`, `e=3,m=2`, or any new cell.

## 1. Custody, seal, determinism, replay (mandate 1)

All independently recomputed.

- `git rev-parse HEAD` = `0d7544ebd5cb12def6bac892646010301098be3c`. I did not
  inspect, list, stat, or run any command against `jc2-lean`, and ran no
  unscoped parent `git status`.
- Report full file: `9a94cd3b…5c65` — matches the mandate.
- Replay full file: `7accef57…4a7f` — matches.
- Body seal: the body-end marker line occurs **exactly once** in the report
  and is standalone (preceded by a newline). Bytes through it inclusive =
  `20154`; SHA-256 `5b57d03dbb11de8b2e837339e2e89091b994d02ddd9a665800a6e5c922b9e731`.
  Both match the seal block. The seal block itself lies outside the body.
- All eleven pinned sources rehashed by me: `d72f774c…`, `2ac7653c…`,
  `2c918d5b…`, `7c73616d…`, `6c719521…`, `fa5a4ef6…`, `efd2f4fe…`,
  `4710349b…`, `3a4565b8…`, `7cbc45a1…`, `669a3496…`. All exact. Custody is
  checked **before** `load_engine()`, so importing the engine (whose own
  custody gate sits inside `main()` and is skipped on import) does not leave
  the tails or compiler unpinned. That is the right order.
- `python3 -B` and `python3 -B -O`: exit 0, byte-identical stdout, ~0.2 s.
  The stdout is byte-identical to the block transcribed in §9 of the report
  (`diff` empty). Neither the replay nor the imported engine contains a single
  bare `assert` (0 occurrences in each; all checks route through `fail()`
  raising `AssertionError` explicitly), so `-O` strips nothing and the
  identical `-O` output is honest rather than vacuous.
- The replay writes no files and imports only `fractions`, `hashlib`,
  `importlib`, `json`, `pathlib`.

**Certificate.** The digest self-check compares against a constant embedded in
the same file, so on its own it proves only internal consistency. Its
evidentiary value is that I rebuilt the payload from data I computed myself
and got the same 3812 bytes and the same digest. That is the check that
matters, and it passes.

**C2 — the mutation banner overstates.** `MUTATIONS=CUSTODY,SURFACE_16_TO_15,
RATIO_SCALE,CHARGED_SUCCESSOR_TEXT` advertises four controls; exactly one is a
live negative control.

- `SURFACE_16_TO_15` is genuine. I confirmed it fires: with the graph's `16`
  changed to `15`, the `N=0` restriction of the unloaded rows is nonzero in
  **6 of 7** rows.
- `RATIO_SCALE` is not a control. It is
  `if 2*2+3*9 != 31 or 6*2+1+2*9 != 31: fail(...)` — a comparison of integer
  literals that cannot fail under any mutation of the source, the engine, or
  the graph.
- `CUSTODY` is a fail-closed hash gate, not a mutation.
- `CHARGED_SUCCESSOR_TEXT` is a provenance pin (useful — it pins *which*
  sentence is being cited inside an already hash-pinned file), not a mutation.

This is the same class of banner erratum the `e2m1` integration already
recorded as its F1 correction. For calibration, the `e2m1` replay carries six
controls (`SURFACE_16_TO_15`, `OMIT_A10_CUBIC`, `DELTA_64_TO_63`,
`RANK1_SIGN`, `ZERO_ROW_REACTIVATION`, plus custody).

**Reviewer-owned mutation battery (adds coverage the replay lacks).** I
perturbed each of the five live graph constants and counted rows whose `N=0`
restriction becomes nonzero:

```text
d0=2S+S^2 : 2 -> 3, 1, 2.001   ->  1/7 rows fire
d1 const  : 1 -> 2, 0, 1.001   ->  5/7
d1 scale  : 1/8 -> 9/8, -7/8, 0.126 -> 5/7
d2 square : 16 -> 17, 15, 16.001 -> 6/7
d5 scale  : 2 -> 3, 1, 2.001   ->  7/7
```

Every constant is detected, so the exact-graph identity is rigid in all of
them; but the weakest (`2S`) is caught by a single row, so a producer choosing
that constant for its one control would have had a much thinner margin than
the `16 -> 15` choice actually made.

**C3 — the certificate does not cover §4.** `surface_resonance_walls` is
charged as a dict of **strings** (`"h6=m-4e"`, …). No computation in the
replay derives or checks (4.1), (4.2), the band table, or the chamber
endpoints. I verified all of them by hand (§6 below) and they are correct, but
the charged certificate supplies no machine evidence for the entire ratio /
congruence half of the artifact. Consumers should treat §4 as desk-verified,
not replay-verified.

## 2. Source census and raw stencil (mandate 2)

Reconstructed independently. I wrote my own parser and my own sparse
`Q[d0..d5]` arithmetic; I did not call `module.reconstruct_rows()`.

- Per-row tail counts `36,54,58,81,89,120,131`, total **569**. ✓
- Every monomial has 10 slots, all weights `sum(a*b)` against
  `(8,7,6,5,4,3,2,2,6,10)` equal `12+ell`, and the maximum number of
  simultaneous load flags is **1**, so `A10`, `A6`, `A2` are well defined. ✓
- Coordinate map `C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8,
  C5=d5, C6=1` is verified against the frozen compiler at
  `compile_contracted_source_v20r2.py:890`; the weight vector against `:61`;
  the load shifts `k10:2, k6:6, k2:10` and target shifts
  `mu2:14 (row 2), mu4:16 (row 4), mu6:18 (row 6), Jdet:19 with factor 1/4,
  target_sign=-1` against `:398-430` and `:876-883`. The §1 row display is
  **faithful**.
- The five zero-constant boundary columns are exactly `k6[0], k2[0], mu2[0],
  mu4[0], mu6[0]` (`:337-342`), while `k10[0]` and `Jdet[0]` are FREE. This is
  precisely what licenses `h6,h2,hmu2,hmu4,hmu6 in Z_{>=1} ∪ {∞}` and
  `h10=hJ=0` on the charged ray. §1's typing is faithful.
- Exact degree minima and maxima, reproduced:

```text
R   min 2,2,2,2,2,3,2   max 4,4,5,5,5,6,6
A10 min 2,2,2,2,2,2,2   max 3,4,4,4,5,5,5
A6  min 1,1,1,2,1,2,1   max 2,2,3,3,3,4,4
A2  min 1,1,1,1,1,1,1   max 1,1,1,2,2,2,3
```

Identical to (1.1) and (1.2). ✓

**Possible arrival vs surviving term.** §2's table is correctly typed
throughout ("Every entry is a possible source arrival, not an assertion that
its leading coefficient survives earlier equations"). I confirmed the
distinction is not decorative: in `e=2,m=2` with `n=3`, (3.1) permits K10 at
`2e+min(2n,m+n,3m) = 4+min(6,5,6) = G9`, and the cell's literal extraction
finds the G9 K10 coefficients **zero** — first actual arrival G10. So (3.1) is
a strict floor on that branch, exactly as advertised.

**Four independent instantiations of §2.** The raw table is corroborated by
four artifacts that do not share the meta replay's code path:

```text
e2m1 prose  : K6 G14+, K2 G22+, targets G29,G33,G37,G38   vs 13+h6, 21+h2, 28+h,32+h,36+h, 38   ✓
e2m2 banner : K10 G8 raw / G10 surface; K6 G15; K2 G23; G29,G33,G37,G38    ✓
e3m2 banner : K10 nominal G10, first actual G12; K6 G21/G23; K2 G33; G43,G49,G55,G57  ✓
Fable e2m2  : surface degrees [3,3,3,none,3,4,3], Jdet first possible G38  ✓
```

All match `2e+2m`, `2e+3m`, `6e+h6+m`, `6e+h6+2m`, `10e+h2+m`, `14e+hmu2`,
`16e+hmu4`, `18e+hmu6`, `19e` exactly.

**C10 (minor).** §2's table carries `+h6,+h2,+hmu` for the five late sectors
but silently drops `+h10` and `+hJ` for K10 and Jdet. That is the charged-ray
specialization declared one paragraph earlier and is not an error, but the
table is not the general-`h10` table its §1 preamble prepares.

## 3. Substitution, normal coordinates, antichains (mandate 3)

**The coordinate change is a genuine global automorphism.** With
`(S,T,n0,n1,n2,n5) = (d4, d3, f0, f1/8, f2, f5)` and `f0,f1,f2,f5` the four
generators of `J` exactly as in the promoted sandwich artifact, the map is
polynomial with polynomial inverse `d = D(S,T)+N`, and the four `J`-generators
evaluate to `(n0, 8n1, n2, n5)`. So `v(J) = v(N)` up to the unit 8, and the
substitution is valid for every `d` — the *substitution* carries no hypothesis.

**Antichains reproduced exactly.** Independent recomputation gives, row by row,
the §3 table verbatim:

```text
R    G,row4:(0,2)                    row6:(0,3),(1,2)
A10  G:(0,2),(1,1),(3,0)   row4:(0,2),(2,1)   row6:(0,2),(2,1),(4,0)
A6   G:(0,1),(2,0)         row4:(0,2),(1,1)   row6:(0,2),(2,1),(3,0)
A2   1,3,5,7:(0,1),(1,0)   row2:(1,0)   row4:(0,1)   row6:(0,1),(2,0)
```

No omitted monomial, no missing row exception. Pareto-minimality is the right
reduction: for positive `(m,n)` the minimum of `a*m+b*n` over the support
equals the minimum over the minimal elements.

**Cancellation vs absence — checked explicitly, and it favours the report.**
Every exact-graph zero arises by large cancellation, not structural absence:

```text
N=0 pre-collection term count -> collected
R    [26,39,46,65,75,80,114]  -> [0,0,0,0,0,0,0]
A10  [13,21,26,39,46,65,76]   -> [2,3,3,0,5,4,6]
A6   [5,8,9,9,15,19,26]       -> [1,2,2,0,3,3,4]
A2   [1,1,2,4,5,8,9]          -> [1,1,1,0,2,2,3]
```

Row 7 of `R` collapses 114 terms to nothing; row 4 of `A10` collapses 39. This
is *not* the FALLACY-v2 hazard, because these are polynomial identities in
`Q[S,T]` valid for all `S,T`, hence coefficient-independent and unbreakable by
any branch. The report's wording ("identically zero") is the correct type. The
series-level hazard — distinct monomials of the *same* bidegree cancelling once
actual series are substituted — is separately and correctly flagged in §2/§3.

**Corollaries I verified that strengthen the artifact.**

- Every `R_l` has minimal normal degree exactly 2 (row 6 attains it only at
  `(1,2)`). So `I ⊆ J^2` and `I ⊄ J^3` — the promoted sandwich's lower
  sharpness, rederived here CAS-free.
- The degree-2 part of `A10_l` vanishes on the tangent plane for **all seven
  rows**. §2's remark ("the K10 quadratic at `2e+2m` vanishes on the leading
  tangent surface in all four charged cells") is true for a stronger reason:
  it vanishes universally on the plane, independently of the cell.
- Degree-3 of `A10` on the plane is nonzero exactly on rows `G`, zero on rows
  4 and 6 — matching surface degrees `3,3,3,∞,3,4,3`. Degree-1 of `A6` on the
  plane is zero on every row (surface degree 2 on `G`), degree-1 of `A2` is
  nonzero exactly on rows `G`. All four consistency checks pass.

## 4. Exact-graph table and (3.1)/(3.2) (mandate 4)

Reproduced exactly:

```text
K10 surface degrees  3,3,3,INF,3,4,3   ->  2e+3m (G), zero (row 4), 2e+4m (row 6)
K6                   2,2,2,INF,2,3,2   ->  6e+h6+2m, zero, 6e+h6+3m
K2                   1,1,1,INF,1,2,1   ->  10e+h2+m, zero, 10e+h2+2m
R                    identically zero on every row
```

matching the banner `SURFACE_MINIMA=K10:333_INF_343;K6:222_INF_232;K2:111_INF_121`.
(3.1) `2e+min(2n,m+n,3m)` and (3.2) `2e+min(2n,2m+n,4m)` follow from the `G`
and row-6 `A10` antichains and are correct. The `n`-dependence claim ("`(e,m)`
does not determine even the possible centered arrival without the extra state
`n`") is right and is independently validated by `e=3,m=2`: (3.1) gives
`6+min(2n,2+n,6) = 12` for every `n>=4`, and the cell's replay banner reports
exactly `K10_NOMINAL_G10_BUT_EXACT_G10_G11_ZERO;FIRST_ACTUAL_G12`.

**C5 — §3 inherits §4's conditional, and the gap is measurable.** §4 says
plainly "conditional on having reached the exact graph". §3 says only "after
absorbing tangent components", and §0 says "After exact graph recentering it
has a still sharper finite bidegree table" with no flag at all. The
*antichain table* is unconditional; the *arrival formulas* (3.1)/(3.2) and the
exact-graph surface table require `ord(S,T)=m`, i.e. that the branch is
tangential to the graph at leading order. That is a real restriction:

- The seven degree-2 initials of `R` (six nonzero; **row 6's is identically
  zero**) cut out an affine cone of dimension **4**. The tangent plane is a
  2-dimensional subcone. Grade `2m` alone does not force tangentiality.
- Explicit exact witnesses with `d3=d4=0` (so `ord(S,T)>m` while `ord(d)=m`):
  the 2-plane `{d0=4d2, d5=-16d1}` and the line `{d0=0, d1=-d5/16, d2=0}`.
  I checked `(4,1,1,0,0,-16)`, `(4,0,1,0,0,0)` and `(0,-1,0,0,0,16)`: all
  seven degree-2 initials vanish. On `(4,0,1,0,0,0)` even six of the seven
  degree-3 parts vanish (only row 6 survives, at `-1/65536`).

So §3's calendar does not cover the tangentially degenerate leading
directions; they are eliminated only by the separately promoted set-theoretic
leading-plane result, which the `e3m1` replay imports under the banner
`G0_G3=IMPORTED_PROMOTED_SET_THEORETIC_LEADING_PLANE`. §3 should carry the
same conditional sentence §4 carries.

**Also verified:** the seven quadratic initials span a rank-**4** subspace of
the 10-dimensional space of quadrics in `(n0,n1,n2,n5)`. §5.4's caveat "the
seven quadrics do not generate the full `J`-initial ideal" is therefore
correct and in fact understated — there are only four independent ones.

## 5. Ratio walls, ties, congruences, endpoints, countercontrol (mandate 5)

All desk-verified.

- (2.1) `2e+2m=3m ⟺ m=2e`. ✓ The `m<2e` / `m=2e` / `m>2e` trichotomy is
  correct, as is the warning that the reviewed leading-plane passage does not
  import for `m>2e`.
- (2.2) `2e+2m=q*m` for `q=3,4,5,6` gives `m/e = 2,1,2/3,1/2`. ✓ Correctly
  demoted to "bookkeeping walls only".
- (4.1): all six equations check against the exact-graph table —
  `h6=m-4e`, `h2=2m-8e`, `hmu2=3m-12e`, `hmu4=3m-14e`, `hmu6=3m-16e`,
  `3m=17e`. Note these compare each sector's first arrival **anywhere in the
  7-row system** against K10's first main-row surface grade; since `mu4` and
  `mu6` live only on rows 4 and 6, that is a cross-row comparison, and it is
  the right one for a global calendar. ✓
- Band thresholds: `h6,h2,hmu2 >= 1` all require `r>4`; `hmu4>=1` requires
  `3m>=14e+1`, i.e. `r>14/3`; `hmu6>=1` requires `r>16/3`; Jdet ties at
  `r=17/3` and precedes for `r>17/3`. ✓ The endpoint remark is correct: at
  `r=4, 14/3, 16/3` the right side of (4.1) is exactly 0, and since every `h`
  must be `>=1`, the sector is strictly later. ✓
- (4.2): `h2=2(m-4e)` is even ✓; `hmu2=3(m-4e)` is divisible by 3 ✓;
  `hmu4 ≡ -14e ≡ e (mod 3)` ✓; `hmu6 ≡ -16e ≡ 2e (mod 3)` ✓; and
  `3m=17e ⟺ 3|e, (e,m)=q*(3,17)` ✓.
- (4.3) and the `(e,m,d)=(2,9,1)` example: `d=m-4e=1`, and
  `nu10=31`, `6e+h6+2m=31`, `10e+h2+m=31`, `14e+hmu2=31` with `(1,2,3)`. ✓
  Minimality is right: `d>=1` and `e>=2` force `m>=4e+1>=9`.
- (4.4): `(2,9)` gives `31 = 31` (tie); `(4,18)` gives `62` vs `61` (K6
  first). ✓ Both arithmetics check.

**The countercontrol is sound, and the report states its own limitation.**
The `(2,9)`/`(4,18)` pair only separates the two chambers because `h6` is held
at 1 in both. The report says so immediately ("Dividing by the gcd forgets the
additive boundary order. Scaling `h6` as well would still reach only the
coefficient-sparse base-change subfunctor"). That is the honest reading:
`(4,18,h6=1)` is a genuine member of the family that is **not** in the image of
the `q=2` base change from `(2,9)` (whose image has `h6` even), so the calendar
does not factor through `m/e`. Confirmed.

**Infinity is handled correctly.** `h=∞` means the zero series, hence "never
arrives", hence strictly later than any finite grade; the band table's phrase
"by choosing a finite positive order" is the right scoping, and Jdet — whose
order is *fixed* at 0 on the charged ray, not chosen — is correctly kept out of
that phrase.

## 6. The no-go statements (mandate 6)

Separating the two claim strengths is the single most important thing a
consumer must do with this artifact.

**What is actually established (all confirmed):**

1. *Uniformizer change.* A DVR automorphism preserves the valuation, hence
   preserves `e` and `m`. ✓ And the normalization `Λ=u·τ^e → σ^e` is available
   over an algebraically closed characteristic-zero residue field because every
   unit power series is an `e`-th power there. ✓
2. *Residual deck group.* Automorphisms fixing `τ^e` satisfy
   `(φ(τ)/τ)^e = 1`, and the `e`-th roots of unity in `K((τ))` are the
   constants `μ_e`, so `φ(τ)=ζτ` exactly. ✓ The proof in §1 is correct.
3. *Ramified base change.* `τ=σ^q` has image supported in degrees divisible by
   `q`, so it is not surjective onto the `(qe,qm)` cell; and descent needs
   coefficientwise membership in `K[[τ^q]]`, which gcd divisibility of two
   leading orders does not give. ✓ Unconditional and correct.
4. *The finite-jet obstruction.* The `e=2,m=2` odd G8 survivor component forces
   `N3≠0` and `N5≠0`, hence is disjoint from the `τ^2`-pullback locus. I
   verified this against the Fable review §8, which proves it on the whole
   constructible component (`B(N5)-εi8A(N5) = -128tq` with `t≠0`, `q≠0`), not
   merely at the fixture. ✓ The report's typing is correct and matches the
   mandate's closing constraint: these are finite G8 **jets**, they die at G9,
   and no arc, attainment, or source-completeness claim is attached.
5. *Graph recentering.* Correct: recentering absorbs only the tangent-plane
   part of the newest normal coefficient; the state after recentering includes
   "at least" `(e,m,n, retained jets, load-order vector)`. The "at least" is
   the honest quantifier.
6. *The sandwich.* (5.1) `2n <= v(I(d)) <= 5n` is a verbatim citation of the
   promoted artifact's own (1.4), correctly typed ("for any centered valuation
   for which the displayed ideal values are finite"). The derived window
   `ceil(L/5) <= n < L/2` and the observation that its width grows with `L` are
   correct. I independently confirmed the exactness claim behind it: since `R`
   has **no** monomial of normal degree `<2`, the only bidegree that can reach
   grade `2n` is `(0,2)`, so `v(r_l)=2n` exactly when the quadratic initial is
   nonzero at the leading normal coefficient. ✓

**C1 — the verdict string is ambiguous in the dangerous direction.** The
headline block reads

```text
NO_FINITE_TRANSITION_QUOTIENT_THEOREM
```

and the charged certificate field reads

```text
"verdict": "FINITE_EXACT_CALENDAR_DATA_NO_FINITE_TRANSITION_QUOTIENT_PROVED"
```

Both parse either as *"no finite transition quotient was proved"* (true, and
what the prose says) or as *"it was proved that no finite transition quotient
exists"* (false, and unsupported by anything in the artifact). The prose is
careful — §0's operative sentence is "none of the available operations
identifies the full jet-transition functors", and the lifecycle line is "NO
FINITE TRANSITION QUOTIENT **PROVED**". But the certificate string is what
downstream consumers will read, and it is hash-charged. It should be
`NO_FINITE_TRANSITION_QUOTIENT_ESTABLISHED_BY_THESE_OPERATIONS` or similar.

What §5/§6 actually refute is narrower and should be stated as such: a
transition recurrence keyed on **cone-and-rank alone** is false, and a
calendar keyed on **the ratio `m/e` alone** is false. Neither is a candidate
anyone would have defended. The artifact contains no lower bound on the number
of transition types and no argument that the enlarged state
`(e,m,n,jets,load orders)` cannot be finitely stratified.

**C6 (wording).** §5.4's "If the seven quadratic initials do not vanish at the
leading normal coefficient, then `v(I)=2n`" is unsatisfiable as literally
written, because row 6's quadratic initial is identically zero (verified
above). The intended and correct hypothesis is "if **at least one** of the
quadratic initials is nonzero"; since `v(I)` is a minimum, one suffices.

**C7 (wording).** §5.2's "Quotienting by the deck group retains only invariant
series" conflates the quotient with the fixed locus. Taking `μ_e`-invariants
selects `K[[τ^e]]`; forming the quotient set does not. The conclusion — that
the deck action supplies no descent in `e` — is unaffected and correct.

## 7. The same-state/different-successor controls (mandate 7)

Reconstructed against the four cell artifacts. Grades and successors check out;
the *labelling* does not.

| control | cells | `m` | `n` | cone grade | successors | state really common? |
|---|---|---|---|---|---|---|
| §6 row 1 | e2m1 / e3m1 | 1 / **1** | 3 / 3 | G6 / G6 | all ranks die G7 / only rank 2 dies G7 | **yes** (only `e` differs) |
| §6 row 2 | e3m1 / e2m2 | **1 / 2** | 4 / 4 | G8 / G8 | all ranks die G9 / G9 tangent, closure G10 | **no** — `m` differs |
| §6 row 3 | e2m2 / e3m2 | 2 / **2** | 4 / 4 | G8 / G8 | K10 collision kills G10 / K10 G10-G11 cancels, rank 0 → n=5, rank 1 to G12 | **yes** (only `e` differs) |

Source pins I verified: e3m1 "At first normal order three, rank two dies at G7
… Rank zero recenters" and "At first normal order four, rank two dies at G9;
rank one has terminal `-ε·5i·k10[0]·t^3/16`; rank zero reduces to the two
incompatible surface cubics" (all three at G9 = `2e+3m`); e2m1 "The two
complete rank fans exhaust ranks 2, 1, and 0. Their terminal G7 identities use
`k10[0] != 0` exactly twice"; e2m2 `G8_N4=ALL_G9_TANGENT_RANKS_DEAD_G10`;
e3m2 `G8_N4=RANK2_DEAD_G10;RANK1_G10_SURVIVOR_DEAD_RAW_G12;RANK0_TO_N5`. All
present and all matching the table.

**C4 — the charged pins select the wrong two controls, and mislabel one.**

- The certificate's `same_cone_different_successor` and the banner
  `SAME_STATE_DIFFERENT_SUCCESSOR=N4_G8_E3M1_vs_E2M2;N4_G8_E2M2_vs_E3M2`
  carry only **two** entries where §6 displays three, and the omitted one
  (row 1, e2m1 vs e3m1) is the cleanest: same `m=1`, same `n=3`, same cone
  grade G6, only `e` differs.
- The pair that *is* pinned first, `E3M1 … vs E2M2`, is the one whose states
  are **not** the same: `m=1` against `m=2`. §6's consequence column is honest
  ("identical cone **grade**, different immediate successor"), but the
  left-hand header "common reduced state" and the banner token
  `SAME_STATE_DIFFERENT_SUCCESSOR` are both wrong for that pair.
- Two of the three controls therefore reduce to "the transition depends on
  `e`", which is unsurprising given that the load shift is literally `2e`. The
  controls do refute a cone/rank-only recurrence; they do not bear on any
  richer candidate.
- Control 3, the only one that fixes `(m,n)` and varies `e` at the harder
  grade, rests on `e=3,m=2`, which was **provisional at seal**. §6 does not
  flag which of its rows depend on unreviewed data.

## 8. Lifecycle audit (mandate 8)

§7's table is **accurate as sealed**, and I re-verified its executable claim:
all four cell replays run clean in ordinary Python —
`e2m1-g7-rankfan` (`…REPLAY=PASS`), `e3m1-g0-g9-complete-rankfan` (PASS),
`e2m2-g0-g10-complete-rankfan` (PASS), `e3m2-g0-g12-complete-rankfan` (PASS),
all exit 0.

State of the ledger as I observe it now, which post-dates the seal:

- `e=2,m=1` and `e=3,m=1`: binding coordinator integrations, **PROMOTED**.
  Matches §7.
- `e=2,m=2`: Fable review `4710349b…` returns **CONFIRMED** ("Every displayed
  equation, every rank chart, every terminal…"). Matches §7.
- `e=3,m=2`: the Grok attempt failed pre-research on an exhausted paid balance
  (HTTP 402; the log contains no mathematical output and none was consumed),
  and a substituted Fable review returned **CONFIRMED**. That review is dated
  after the meta gate's file, so §7's "DIFFERENT-MODEL REVIEW ACTIVE AT SEAL"
  was correct when written.
- A later binding coordinator integration now binds both `m=2` cells.

**I promote nothing on the strength of this review**, and in particular I do
not treat the meta gate's agreement with either `m=2` producer as evidence:
it is same-model synthesis, and the independent evidence is the two Fable
reviews, not this artifact. §7's own sentence — "No provisional cell is
promoted by agreement with this same-model synthesis" — is respected by the
artifact and by me.

§7's "Not covered" list (items 1–5) and the closing typing sentence ("Point-set
emptiness of a finite prefix excludes a formal arc only inside the same exact
cell. It supplies no map-to-cell or source-exhaustion theorem") are correct and
correctly scoped.

## 9. Priority claim (mandate 9)

**(8.2) `(4,1)` at G11 is CONFIRMED as the cheapest untouched unit-ray cell.**
Enumerating `2e+3m <= 11` with `e>=2, m>=1` gives exactly
`(2,1)=7, (3,1)=9, (2,2)=10, (4,1)=11` — the first three are done, so `(4,1)`
is the unique untouched cell at or below G11. Its absence claim also checks:
K6 `>= 6e+h6+m = 26`, K2 `>= 42`, `mu2 >= 57`, `mu4 >= 65`, `mu6 >= 73`,
Jdet `= 76`. All six match §8 exactly. The comparison with `(3,2)` (K10 at
G12) is correct, and `(4,1)`'s four mandatory controls are well posed.

**(8.1) `e=2,m=2,h10=1` reopening at G11 is CONFIRMED as stated but is not the
cheapest.** The G11 grade is right (`2e+h10+3m = 4+1+6`), and the claim that
G10 becomes vacuous is genuinely supported, not assumed: at rank zero the
`k10[0]`-free rows (5.5)/(5.6) still force `A(N5)=B(N5)=0` and the K10 load
cancels from (5.6), after which the Fable review's "**every one of the seven**
G10 rows equals `k10[0]·W_r(s,t)`" makes G10 identically satisfied on the face.
So the shared G10 step costs nothing on the whole `h10>=1` face.

**C8 — four ranking defects in §8.**

(a) *Cheaper omitted boundary faces.* By §8's own metric — first surface K10
grade on the `k10[0]=0` child — the `e=2,m=1` child reopens at
`2e+h10+3m = 4+1+3 = **G8**`, and the `e=3,m=1` child at `6+1+3 = **G10**`.
Both are cheaper than (8.1)'s G11, and both are one-grade marginal extensions
of **promoted** rather than merely reviewed work. The `e2m1` child is cheaper
still in width: its integration records that the terminal G7 identities "use
`k10[0] != 0` exactly twice", so at most two branches survive onto that face.
§8 names neither child.

(b) *An omitted tie in the follow-on ranking.* "After the boundary G11 child
and `(4,1)`, the ranked discriminators are `(2,3)` at G13 …" — but `(5,1)`
also has `2e+3m = 13`. The list is complete only under the different criterion
"next new transverse order `m`", which is not the metric §8 declares.

(c) *The residue is an infinite face family.* `h10 ∈ {1,2,3,…,∞}` each give a
distinct calendar (`K10` surface at `10+h10`). §8 names `h10=1` and correctly
flags `h10=∞` as separate and undecided, but silently omits `2 <= h10 < ∞`.
Solving the `h10=1` child does not close the `k10[0]=0` residue.

(d) *`(2,3)` is mis-motivated.* §8 lists it as "the next new transverse order".
Per the Fable review §12 it is more than that: every `e2m2` kill above G6
consumed the open `(s,t) != (0,0)`, so — given the leading-plane passage —
`(2,3)` is the **completion residue** of the `m=2` result, not merely a new
frontier. Its priority should reflect face completeness, not novelty.

**C9 — the G11 retention sketch is incomplete.** §8 says the G11 extraction
"has the same surface cubics multiplied by `k10[1]` together with a fresh
quadratic block". Two coefficients are missing from that list.

- The `A10` grade-6 block is not the cubic alone. In `e2m2` at `n=4` the
  bidegrees `(1,1)` and `(3,0)` **tie**, because `m+n = 2+4 = 6 = 3m`; the
  cell's own (5.2) records the block as `L_r = DM4_r(ell)[w] + W_r(s,t)`. So at
  `4+1+6` the retained object is `k10[1]·L_r`, i.e. the mixed
  surface×normal term `DM4_r(ell)[w]` **and** the cubic. The same tie is
  already visible in the promoted `e2m1` erratum, whose replay banner reads
  `K10_G7_ERRATUM=DM4(ell)[u]+A10_CUBIC(ell)=DM4(ell)[u-mu/2]` (there
  `m+n = 1+2 = 3 = 3m`). The Fable review's §12 sketch ("the same `W_r` cubics
  reappear multiplied by `k10[1]`") has the same omission; a literal G11
  producer that retains only `W_r` will be wrong.
- `k10[1]` is not the only load coefficient that can reach G11. Solving
  `4 + j_k + (Σ surface indices) + (Σ normal indices) = 11` over the `A10`
  antichain admits `(1,1)` with surface index 2 and normal index 3 and
  `j_k = 2`. So on any chart still carrying a normal coefficient at order 3,
  **`k10[2]` reaches G11**. Whether that chart survives to G11 is the
  producer's question; the retention list must include it a priori.

The rest of the §8 retention discipline — "retain every surface and normal
coefficient capable of reaching G11, including all nonzero deck characters",
"use the G10 cone only after literal equality with the frozen source", "stop at
the first complete reduced rank fan" — is correct and is the right standard.

**(6.1) is correctly typed.** `G_terminal = 2e+3m` holds on all four cells
(`7,9,10,12`), and the artifact says outright that this is verified on four
cells only and "is not evidence for a coefficient-blind proof of the same
formula at all `(e,m)`". That is the right floor/attainment discipline. Note
the charged text pins carry the terminal grade for `e3m1` (G9), `e2m2` (G10)
and `e3m2` (G12) but not for `e2m1` (G7).

## 10. Itemized verdict (mandate 10)

| # | item | verdict |
|---|---|---|
| 1 | hashes, seal, body bytes, 11 source pins, ordinary/`-O` determinism, transcript match | CONFIRMED |
| 1b | certificate 3812 B / `afb3979a…` rebuilt from an independent code path | CONFIRMED |
| 1c | "MUTATIONS" banner: only 1 of 4 is a live control; `RATIO_SCALE` is a literal tautology | CORRECTION (C2) |
| 1d | §4 walls/congruences charged as strings only, no machine check | CORRECTION (C3) |
| 2 | 569 census; (1.1) minima; (1.2) maxima; load linearity; compiler fidelity of §1 | CONFIRMED |
| 2b | §2 raw table, incl. four independent instantiations; arrival-vs-survival typing | CONFIRMED |
| 2c | §2 table drops `+h10`, `+hJ` without restating the charged-ray specialization | CORRECTION (C10, minor) |
| 3 | `d=D(S,T)+N`, normal coordinates, all twelve Pareto antichains, no omitted row | CONFIRMED |
| 3b | exact-graph zeros are cancellation identities in `Q[S,T]` — coefficient-independent, correctly typed | CONFIRMED |
| 4 | exact-graph surface table; (3.1); (3.2); `n`-dependence | CONFIRMED |
| 4b | §3/§0 omit the tangentiality conditional §4 states; grade-`2m` locus is a **dim-4** cone vs the dim-2 plane, with exact non-tangential witnesses | CORRECTION (C5) |
| 5 | (2.1), (2.2), (4.1)×6, (4.2)×5, band thresholds, zero endpoints, (4.3), `(2,9)`, (4.4) | CONFIRMED |
| 5b | treatment of `h=∞` and of Jdet's fixed order | CONFIRMED |
| 6 | uniformizer, deck group `μ_e`, base-change sparsity, jet obstruction, recentering, sandwich | CONFIRMED |
| 6b | verdict string readable as "no finite quotient exists" — not established | CORRECTION (C1, material) |
| 6c | "seven quadratic initials do not vanish" unsatisfiable (row 6 ≡ 0); "quotienting" vs invariants | CORRECTION (C6, C7) |
| 7 | grades/successors of all three controls against the four cells | CONFIRMED |
| 7b | pinned pair has `m=1` vs `m=2`; banner token `SAME_STATE…` wrong; cleanest control unpinned | CORRECTION (C4) |
| 8 | lifecycle table as sealed; all four cell replays PASS in ordinary Python | CONFIRMED |
| 9 | `(4,1)` at G11 is the unique cheapest untouched unit-ray cell; its six absence grades | CONFIRMED |
| 9b | `(8.1)` G11 reopening and vacuous G10 on the `h10>=1` face | CONFIRMED |
| 9c | `e2m1,h10=1` (G8) and `e3m1,h10=1` (G10) are cheaper and unnamed; `(5,1)` ties `(2,3)`; `2<=h10<∞` omitted; `(2,3)` mis-motivated | CORRECTION (C8) |
| 9d | G11 retention omits `DM4_r(ell)[w]` and `k10[2]` | CORRECTION (C9) |
| 10 | "no finite transition quotient can exist" | **NOT ESTABLISHED** — see C1 |

### Maximum exact statement safe to promote

On the frozen V20R2 generic-K00 source (tails `d72f774c…`, compiler
`2ac7653c…`), with `Λ=τ^e` (`e>=2`), `ord_τ(d)=m>=1`, `C6=1`, `ord_τ(k10)=h10`,
`ord_τ(Jdet)=hJ`, and `h6,h2,hmu2,hmu4,hmu6 ∈ Z_{>=1} ∪ {∞}`:

1. the seven rows are exactly
   `Φ_l = R_l(d) + Λ^2 k10 A10_l(d) + Λ^6 k6 A6_l(d) + Λ^10 k2 A2_l(d) − targets_l`
   with `targets` `(mu2, mu4, mu6, Jdet/4)` at `Λ^14, Λ^16, Λ^18, Λ^19` on rows
   `2,4,6,7`;
2. the exact `d`-degree minima and maxima are (1.1) and (1.2), and the §2 raw
   table of **first possible arrivals** follows verbatim;
3. in the global polynomial coordinates `(S,T,n0,n1,n2,n5)=(d4,d3,f0,f1/8,f2,f5)`
   the Pareto-minimal bidegree antichains are exactly the §3 table; in
   particular every `R_l` lies in `J^2` and none in `J^3`, and rows 4 of
   `A10`, `A6`, `A2` vanish identically on the exact graph;
4. consequently the exact-graph surface degrees are `K10 (3,3,3,∞,3,4,3)`,
   `K6 (2,2,2,∞,2,3,2)`, `K2 (1,1,1,∞,1,2,1)`, and **on a branch already
   tangential to the graph** with `ord(S,T)=m`, `ord(N)=n>m`, the main-row and
   row-6 K10 floors are (3.1) and (3.2);
5. the six tie equations (4.1), the congruences (4.2) including
   `Jdet ⟺ (e,m)=q·(3,17)`, the band thresholds `r>4, 14/3, 16/3, 17/3` with
   strict exclusion at `r=4, 14/3, 16/3`, the simultaneous-tie form (4.3), and
   the `(2,9)` vs `(4,18)` same-ratio countercontrol at fixed `h6=1`, are exact.

Every grade in 2, 4, 5 is a **possible-arrival floor**, never an attainment
claim; item 4 carries the tangentiality hypothesis of C5. Nothing above
supplies a cell, map, arc, source point, attainment, or source-completeness
statement, and nothing above bounds the number of transition types in either
direction.

Explicitly **not** promotable: any reading of
`NO_FINITE_TRANSITION_QUOTIENT_*` as an impossibility result. What is
established is that a recurrence keyed on cone-and-rank alone, and a calendar
keyed on `m/e` alone, are false, and that uniformizer change, ramified base
change, gcd reduction, the deck action, graph recentering, and the `J^5 ⊆ I ⊆ J^2`
sandwich individually fail to produce one.

### Cheapest decisive successor

**`(e,m)=(4,1)`, first complete reduced rank fan through G11**, as §8 ranks it.
It is the unique untouched unit-ray cell at or below G11; it is the only cheap
place where `G_terminal = 2e+3m` gets a fourth-`e` test; and the `(3,2)`
G10/G11 cancellation gives it a ready same-`(m,n)`/different-shift control. Its
retention list must include every surface and normal coefficient able to reach
G11, all nonzero deck characters, and — by C9's argument applied at `m=1` — the
mixed `(1,1)` block wherever `m+n = 3m`, i.e. at `n=2`.

Two cheaper items exist but are not decisive for the `(e,m)` atlas, and should
be scheduled as cleanup rather than as the successor:

- `e=2,m=1,h10>=1`, reopening at **G8** — cheapest of all by §8's own metric,
  a one-grade extension of promoted work, and narrow (at most the two branches
  whose G7 terminals consumed `k10[0]`);
- `e=3,m=1,h10>=1`, reopening at **G10**.

Both, together with `2<=h10<∞` and `h10=∞`, are required before any
`k10[0]=0` residue can be called closed.

I ran: hashing, both replay modes, my own reconstruction of the source and the
substitution, a 15-point graph-constant mutation battery, one `sympy` Gröbner
basis on six quadrics in six variables (about one second), and all four cell
replays. I ran no Singular and no heavy CAS, did not touch `jc2-lean`, did not
run an unscoped parent `git status`, and edited no canonical file, script,
dependency, or producer. I did not re-derive the interior rank-fan charts of
the four cells from scratch; for those I relied on the cell producers and the
two Fable reviews, and I say so rather than implying independent coverage.

<!-- BODY-END -->
