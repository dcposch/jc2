# D43 common-integral emitter: bounded preflight and reducer-free source lane

**Date:** 2026-08-28  
**Producer:** GPT-5.6  
**Scope:** residue-A, `a00pp`, B-frozen no-log `W1*W2 != 0` chart  
**Status:** **COEFFICIENT/SPECIALIZATION PREFLIGHT IMPLEMENTED; COMMON 34+184 EMISSION STILL OPEN**

## Executive verdict

There are two different goals which the current discussion had conflated.

1. A **source-defined characteristic-zero or `Z_p` point** does not logically
   require an integral lift of the 509-element D23 reduced Groebner basis.
   In principle it is enough to emit, in one explicit exact source ambient,

   ```text
   34 source-derived parked rows + 184 pristine D43 source rows,
   ```

   prove their source/reconstruction identities, and pass a Hensel/formal-
   smoothness argument for that source ambient.  This is a sound reducer-free
   bypass in principle.

2. Proving that this source model is **the same presentation as the banked
   34+184 modular NF model** does require the missing 509
   reducer-to-parked identities and the integral source-to-NF identities.
   Those traces are comparison certificates, not prerequisites for defining
   a valid source scheme.

The advertised direct `218`-row/`184`-coordinate bypass is not complete
today.  The pristine source Jacobian is `184 x 190`, while the assembled
banked system is `218 x 184`; the only current comparison drops the two
`uW` columns and invokes the modular identity `raw=NF+Q*parked`.  Therefore
an exact coordinate descent/reconstruction certificate is additionally
load-bearing.  The committed 34 parked rows are
prime-specific RREF/NF outputs, and no committed artifact gives exact common
source identities and solve-back certificates for their three D23
compatibility rows and five D25 Schur residuals.  Also, one successful
`p^2` correction is not by itself an infinite Hensel lift.

This preflight adds a small fail-closed implementation:

- `cases/d43_common_integral_emitter.py` — exact 432-basis radical
  arithmetic, literal `R_ext -> a00pp` collapse, primitive/simple-root and
  denominator gates, and separate source/equivalence certification seals;
- `cases/test_d43_common_integral_emitter.py` — six light tests, including
  both registered primes and the banked `p^2` Hensel frame.

It emits no mathematical row and cannot seal an incomplete bundle.

## 1. Exact coefficient order

### 1.1 Integral generator choice

Writing only `2h^2=3` over `Z` does not give a monic power reduction for
`h`.  The genuinely integral generator should therefore be

```text
H = 2h,     H^2 = 6.
```

Define

\[
\begin{aligned}
\mathcal O_0={}&\mathbf Z[r,z,A_1,A_2,H]/(
 r^2-3,\ \Phi_{42}(z),\\
&A_1^3-(3+r),\ A_2^3-(3-r),\ H^2-6),
\end{aligned}
\]

where the primitive order-42 relation is the literal cyclotomic polynomial

\[
\Phi_{42}(z)=z^{12}+z^{11}-z^9-z^8+z^6-z^4-z^3+z+1.
\]

The sequential monic basis of `O_0` has exponent bounds

```text
z: 0..11, r: 0..1, A1: 0..2, A2: 0..2, H: 0..1
```

and rank `12*2*3*3*2 = 432` over `Z`.

The convenient source arithmetic uses `h=H/2`.  Its working algebra is

\[
\mathcal O_{\rm work}=\mathcal O_0[1/30],
\]

because the current exact Newton construction explicitly divides by
`j=1,...,6`, while `h^2=3/2` introduces `2`.  For the common simple-root
Hensel locus it is safe to work over

\[
\mathcal O_{\rm et}=\mathcal O_0[1/210].
\]

Here `5` is algorithmic (Newton division); `2,3,7` cover the radical and
cyclotomic bad primes.  This is only the base coefficient localization.
Every later pivot/RREF normalization must still record its exact algebraic
denominator and prove that denominator a unit at both registered
specializations.  It is not licensed to assume that every derived
denominator divides 210.

### 1.2 Relation to the committed exact source engine

The exact gold lane already has the right raw representation:

- `cases/r1_experiment.py:19-45` represents `Q(sqrt(3))` coefficients as
  exact pairs of `Fraction`s;
- `cases/r1_experiment.py:86-180` represents the radical ring by keys
  `(z,A1,A2,W1,HW1,W2,HW2,EB)` and reduces by the literal `Phi_42`;
- `cases/r1_experiment.py:543-600` performs the exact suborbit Newton build;
- `cases/build_tails43.py:30-35,42-104` is the resume-safe exact D43 gold
  compiler using that ring.

The exact output `cases/directionb_tails_D43.pkl` and its `ckpt43/`
checkpoints are not present in the current tree.  Only the specialized
`p=105337` rebuild is present.  No exact D43 build was attempted locally in
this bounded preflight.

At `a00pp`, collapse the committed raw ring only by the literal identities

```text
HW1 = h*W1,   HW2 = h*W2,   EB exponent = 0.
```

The `W_i` and `uW_i` remain polynomial/chart coordinates, not coefficient
denominators.  Their inverse laws must remain explicit rows
`W_i*uW_i-1`; a future emitter must not hide `1/W_i` inside a coefficient.
The new adapter rejects a surviving `EB` exponent or a negative Laurent
exponent instead of guessing a chart convention.

This ring is intentionally `a00pp`-scoped.  A simultaneous 36-fiber family
ring needs independent `h1,h2` selectors (or an equivalent etale product),
not the single `h` used here.

## 2. What the current scripts actually specialize

### 2.1 `build_tails_modp.py`

The modular D43 builder does not retain radical coefficients.

| operation | exact source location | consequence |
|---|---|---|
| choose the promoted radical frame | `cases/build_tails_modp.py:143-145` via `valuation_e.radical_env`, whose source is `r1_fullcore.radical_point` | all `z` powers are immediately finite-field scalars |
| choose `A1,A2,h1,h2` | `cases/build_tails_modp.py:422-425` via `d25_eplus.fiber_env`; the atlas laws are checked at `cases/d25_eplus.py:135-152` | selector data are prime/fiber values, not symbolic roots |
| fold `A_i,h_i` | `cases/build_tails_modp.py:185-203` | the bank loses their exponent provenance |
| fold `z` twists | `cases/build_tails_modp.py:206-218,239-255` | the bank loses `Phi_42`-basis coefficients |
| Newton division | `cases/build_tails_modp.py:258-278` | `j^{-1}` is taken directly in `F_p` |
| frozen B constant | `cases/build_tails_modp.py:296-307` | `3/2` is folded as `3*2^{-1}` |
| output | `cases/build_tails_modp.py:475-487` | payload records only numeric `A1,A2,h1,h2` and explicitly says the radicals were folded |

The local statement `pt,r3,h32 = ...` is slightly misleading for source
recovery: `r3` and `h32` are not retained by this engine; `z` is used via
the precomputed power table, while `A_i,h_i` come from the atlas `env`.

### 2.2 `d25_reduce.py`

The D25 reducer starts one step earlier but still specializes before
reduction.

- `cases/d25_reduce.py:199-242` reads exact D25 bank coefficients as
  `(c0,c1)` `Fraction` pairs and radkeys.  It asserts `z` and `EB` exponents
  are zero, then maps each rational denominator to its inverse modulo `p`.
- `cases/d25_reduce.py:270-283` multiplies by the atlas values of
  `A1,A2,HW1/W1,HW2/W2` and only then calls the modular NF engine.
- `cases/d25_reduce.py:334-357` derives the selected `r3` from the `a00pp`
  `A1` value and checks the cube/square laws on all fibers.
- `cases/d25_reduce.py:114-150` parses and demands exactly 509 monic
  reducers.

The existing fraction conversion at `d25_reduce.py:234-238` and
`d25_assemble.py:328-335,374-378` has no explicit `denominator % p != 0`
assert before exponentiating.  The new preflight makes this an explicit hard
gate.

## 3. Exact specialization acceptance tests

The registered `a00pp` maps are:

| `p` | `zeta42` | `r3` | `A1` | `A2` | `h` | `H=2h` |
|---:|---:|---:|---:|---:|---:|---:|
| 105337 | 2779 | 795 | 50630 | 10114 | 50267 | 100534 |
| 105673 | 13862 | 14686 | 38664 | 46664 | 35053 | 70106 |

The `A_i,h` values match `a00pp` in
`cases/d23_atlas_p{105337,105673}.json`; the `z,r3` values are the literal
`r1_fullcore.radical_point` selectors.  Every accepted specialization must
pass all of the following, not merely witness vanishing.

1. `Phi42(z)=0`, `z^42=1`, and `z^6,z^14,z^21 != 1`.
2. `r^2=3`, `A1^3=3+r`, `A2^3=3-r`, `2h^2=3`.
3. `Phi42'(z), 2r, 3A1^2, 3A2^2, 4h` are units.
4. Every recorded rational and algebraic denominator is a unit.
5. The selected roots equal the registered branch values, not merely some
   roots of the same equations.

The exact verifier returns:

| `p` | `z^6` | `z^14` | `z^21` | `Phi42'(z)` | `2r` | `3A1^2` | `3A2^2` | `4h` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 105337 | 16077 | 15094 | 105336 | 72846 | 1590 | 63015 | 32307 | 95731 |
| 105673 | 103751 | 92504 | 105672 | 32731 | 29372 | 58241 | 93174 | 34539 |

All defining-equation residues are zero and every displayed derivative is a
unit.  The banked `p^2` frame from
`cases/d43_char0_lift_p105337.json` is also accepted:

```text
modulus = 105337^2 = 11095883569
z = 8852313585
r = 11012141449
A1 = 786496672
A2 = 8038065910
h = 6003627245
```

In particular, the stored `z` satisfies the stronger literal
`Phi42(z)=0 mod p^2`, has exact order 42, and reduces to `2779 mod p`.
The banked artifact itself recorded only `z^42-1`; primitivity and the
cyclotomic relation are now separately checked.

### 3.1 Full emitted-row acceptance at both primes

A future source emission is accepted only if, at **each** prime:

- the common variable registry and monomial order specialize without drift;
- every one of the 34 exact rows, after its recorded source normalization
  unit, reparses dictionary-exactly as
  `cases/d25fam_p<P>_a00pp.ms`;
- every one of the 184 pristine exact rows specializes dictionary-exactly to
  a freshly rebuilt raw source bank (the current shipped rebuild exists only
  at 105337);
- the three D23 and five D25 solve-back identities specialize and replay;
- all source/pivot denominators remain nonzero;
- only after these gates may witness vanishing be used as a consistency
  check.

For the optional presentation-equivalence tier, additionally:

- 509 exact reducer candidates specialize, with unit leading coefficients,
  to the exact monic dictionaries in each shipped GB;
- all 509 reducer-to-parked membership identities replay;
- all 184 source-to-reducer NF identities replay and match the recovered
  checkpoint dictionaries.

### 3.2 Fiber-label warning

The atlas defines its cube-root twist as the *smaller integer* primitive cube
root in each finite field.  Under the registered `z` maps:

```text
p=105337: smaller omega = z^14 = 15094
p=105673: smaller omega = z^28 = 13168 (where z^14 = 92504)
```

Thus atlas labels away from `a00pp` are prime-relative.  A common
characteristic-zero 36-fiber emitter must use a fixed cyclotomic character
and record the induced per-prime relabeling.  It may not identify the same
`aijuv` text label across primes by silently using `z^14` at both.

## 4. Provenance of the 34 parked rows and 509 reducers

### 4.1 The 34 parked rows

They are not 34 independent pristine D43 equations.  Their exact modular
construction is:

| parked indices | block | immediate source |
|---:|---|---|
| 1--26 | D21 fiber core | `d25_assemble.py:1356-1367` loads 26 prime/fiber `.ms` rows |
| 27--29 | D23 compatibility `g1,g2,g3` | atlas `g_rows`; loaded at `d25_assemble.py:707-714` and assembled at `1207-1212` |
| 30--34 | five D25 Schur residuals | constructed at `d25_assemble.py:914-939` and appended at `1213-1217` |

The per-fiber emission itself is literal at
`cases/d25_assemble.py:1265-1283`.  `cases/d25_perfiber.py:204-250`
independently reparses 34 rows, proves the first 29 reduce to zero through
the D23 GB, and identifies the last five as the D25 residuals.  The canonical
ledger records the same `26+3+5=34` shape at
`ladder/SHEET6-DIRECTIONB.md:1954-1963,2030-2040`.

Current `a00pp` parked hashes are:

```text
p105337 ef6db7e9ad36666537475fabf8238887de0c7e6d8f02c9381eaa7c810cbe4fe2
p105673 43b81c4ea5f77a5d0d32f433a23e867e9ef4c7228f5d6e7624f43561aa976175
```

These are certified modular files, not two reductions of a committed common
34-row source file.

### 4.2 The 509 D23 reducers

The 509 elements are an output basis, not the original parked source.

1. `cases/directionb_det23_p105337.rows.txt:1-8` states that the 400-row
   determinantal input is 397 rows of the D21 radical-point fiber GB plus
   `g1,g2,g3`.
2. `cases/directionb_det23_p105337.ms:1-8` begins that 400-row modular input.
3. msolve reduced it to the 509-element monic grevlex basis recorded at
   `cases/directionb_det23_gb_p105337.out.txt:1-10`; the second prime has the
   identical 509-element support skeleton.
4. The canonical provenance and 509 verdict are
   `ladder/SHEET6-DIRECTIONB.md:1448-1483`.

Current GB hashes are:

```text
p105337 3ba965d8d57439fce5e6febd6a3f7a3ab3bcad74337768eec18681bf0e2a2acc
p105673 cda3a0d61c6ab8973f3d6f4ec6b45abba0007514789323445200a948738e72de
```

`d25_reduce.py:114-150` and `d43_reduce_modp.py:136-149` consume these
prime-specific bases.  The D43 checkpoint producer saves only NF rows
(`d43_reduce_modp.py:186-190`), not quotient traces.  This is exactly the
gap restated by `xmodel/sol-d43int.md:37-50,125-129` and mechanically
enforced by `cases/d43_integral_gate.py:66-84,118-133`.

## 5. Dependency map

```text
r1_experiment.py exact K3/R_ext
        |
        +--> build_tails43.py exact gold source ----X output absent locally
        |
r1_fullcore.radical_point --> valuation_e.radical_env --+
                                                        |
d23_atlas + d25_eplus.fiber_env ------------------------+
                                                        v
                                               build_tails_modp.py
                                                        |
                                                        v
                                              prime-folded D43 raw bank
                                                        |
509 modular D23 GB --------------------------------------+--> d43_reduce_modp
                                                               |
                                                               v
                                                     184 modular NF rows

exact D25 bank (not shipped here)
        |
        +--> d25_reduce.py + 509 modular GB --> modular NF/trace checkpoints
        |
        +--> d25_assemble.py
                 ^       ^
                 |       +-- atlas g1,g2,g3
                 +---------- 26 modular D21 fiber-core rows
                              |
                              v
                      34 modular parked rows
```

The desired reducer-free source branch cuts above both modular GB arrows,
but it must first choose and certify a common ambient:

```text
exact low-order source + exact solve DAG --> common 26+3+5 --+
exact D43 source (184 rows / 190 coords) ---------------------+--> explicit
exact coordinate descent/reconstruction ---------------------+    source model
```

The existing banked `218/184` object is not literally this source model.
`cases/d43_char0_lift.py:349-383` constructs the pristine `184 x 190`
Jacobian (180 tail directions, eight fixed directions, and `alpha,beta`; see
also `:787-794`).  In contrast, `cases/d43_full_family.py:343-360` assembles
34 parked plus 184 graph-NF rows on 156 external and 28 parked variables.
The current comparison at `cases/d43_char0_lift.py:491-530` identifies only
182 assembled columns with source labels, assigns no source column to
`uW1,uW2`, and relies explicitly on `raw=NF+Q*parked` over `F_p`.  Thus it is
a modular row-space comparison, not an integral coordinate descent.

## 6. Reducer-free bypass: exact logical boundary

### 6.1 What is sufficient for source-defined existence

The bypass is sound if all of these are supplied:

1. one exact coefficient order and one explicitly declared source ambient;
2. an exact coordinate descent/reconstruction map relating the 190 pristine
   source coordinates to every coordinate used by the parked equations; if
   the target is the banked 184-coordinate chart, this must explain the two
   `uW` coordinates and the eight source directions not selected by the
   current 182-column modular map;
3. 34 exact parked constraints proven source-derived after that map;
4. 184 exact pristine D43 source rows in the declared ambient;
5. a common mod-`p` point and a first correction for the entire declared
   source system (only in a certified 184-coordinate descent may this be
   called the banked all-218 correction);
6. a genuine lifting theorem: for example, a unit Jacobian minor for a
   locally generating subsystem plus exact localized-generation identities
   for the remaining rows.

The existing rank-131 minor and the existing `p^2` correction concern
different incomplete presentations.  Because 218 equations have many
dependencies, rank 131 alone is not a square-system Hensel certificate.
One must either prove the remaining 87 rows lie in the localized ideal of a
smooth 131-row subsystem, or provide an equivalent formal-smoothness/lifting
argument.  A single first correction does not establish a `Z_p` point.

### 6.2 What the 509 traces add

Reducer-to-parked traces are required to prove

```text
source parked ideal = ideal generated by the 509 banked reducers
```

and integral source-to-NF traces are required to identify the 184 source
rows with the recovered graph rows modulo that ideal.  These statements let
one transport the banked Jacobian/local calculations to the source model.
They are not logically required if smoothness and lifting are recomputed
directly on the common source equations.

Accordingly, the new certification shell has two independent seals:

- `seal_source`: 34 parked + 184 pristine, with exact coordinate descent,
  source, and solve-back gates;
- `seal_presentation_equivalence`: the source seal plus 509 reducer
  identities and 184 source-to-NF identities.

### 6.3 Exact provenance gates for the derived three D23 rows

The current `g1,g2,g3` are mod-`p` RREF outputs after modular NF, so their
support agreement across two primes is not an exact source derivation.  A
reducer-free common derivation must bank:

1. the exact pristine Row-22 block and its exact relation to the chosen 26
   D21 core rows;
2. the exact Row-22 factorization `A22=C10*diag(carriers)`;
3. an explicit unit rank-4 minor of `C10` and exact six-row left kernel;
4. the 22-pivot and deep-tail reconstruction DAG, equation by equation,
   with every chart unit and denominator listed;
5. the exact affine four-column level-44 matrix, an explicit unit rank-2
   minor, and a complete exact left-kernel basis;
6. literal identities showing each common `g_s` is the resulting
   compatibility row after the DAG;
7. reverse solve formulas proving, on the stated chart,

   ```text
   g1=g2=g3=0  iff  the six Row-22 compatibility equations are solvable.
   ```

For source existence, these may be direct substitution/pseudo-division
identities through the 26-row triangular chart; they need not pass through a
509-element GB.  If exact three-row compression proves awkward, retaining
the original Row-22 equations and reconstruction variables gives a valid
larger raw source presentation, but it is no longer the advertised
34+184/184-coordinate model and its Hensel calculation must be redone in its
explicit larger ambient.

### 6.4 Exact provenance gates for the five D25 rows

The existing phase-B calculation reads exact radkeys but converts `C24` to
`F_p` before row reduction (`cases/d25_assemble.py:471-537`).  A common
derivation must instead bank:

1. the exact nine Row-24 cells and the 90-entry frontier census;
2. the literal factorization
   `A24=C24*diag(A1W1,A1^2,A2W2,A2^2,A1HW1,A1^2,A2HW2,A2^2,A1^2,A2^2)`,
   including row monomial normalizers;
3. exact rank `4` of `C24`, with a named `4x4` determinant that is a unit at
   both registered maps;
4. an exact five-row `L24` spanning the full left kernel, with
   `L24*C24=0` literally over the common ring;
5. the exact previously certified D21/Row-22 reconstruction DAG, applied
   only to `L24*b24`;
6. five literal residual identities and reverse frontier solve formulas,
   proving

   ```text
   R1=...=R5=0  iff  the nine Row-24 equations admit the ten frontier variables
   ```

   on the named unit chart;
7. specialization at both primes to the parked rows, with any RREF row
   scalars recorded explicitly rather than hidden by monic normalization.

These seven gates replace the 509 reducers for the source-existence lane.

## 7. Smallest safe implementation slices

### Slice 0 — completed here

- exact 432-basis arithmetic with `Phi_42`, not `z^42-1`;
- true integral-generator documentation `H=2h`;
- literal adapter from committed `R_ext` terms to `a00pp` coefficients;
- denominator, primitivity, branch, and simple-root checks at both primes and
  the banked `p^2` frame;
- source/equivalence seals which fail closed, including a mandatory exact
  190-to-parked coordinate descent/reconstruction gate.

Light verification:

```text
python3 -m unittest -v cases/test_d43_common_integral_emitter.py
Ran 6 tests in 0.007s -- OK
```

Artifact hashes:

```text
cases/d43_common_integral_emitter.py
  5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d
cases/test_d43_common_integral_emitter.py
  9896fb1061f5cdd085c50d81b0fa418f3ba43ad84d0f1604f79994906a952199
selftest JSON (ephemeral /tmp output)
  ce555eaff22e576b3d8fd23c1fcab2037e7588057304b7e859c77240c66b635d
```

### Slice 1 — fastest next mathematical implementation

Build the coordinate bridge and common low-order 34 rows first, without a
509 lift:

1. write the exact source-coordinate registry and the parked-coordinate
   substitution/reconstruction map; prove every relation, including the
   `W*uW-1` chart equations, and account for all 190 source directions rather
   than copying the current modular zero columns;
2. specialize that bridge at both primes and verify the current 182-column
   identifications, while treating `uW1,uW2` by the exact inverse relation;
3. obtain the exact D25 source bank in a controlled compute environment;
4. replace `phaseB/phaseC` finite-field RREF by exact
   `RadicalCoefficient` linear algebra with denominator ledgers;
5. replay the 26-row source triangular DAG directly;
6. emit and specialize the exact `3+5` rows at both primes;
7. require dictionary-exact parked-row matches after recorded unit scalings.

This slice is small linear algebra on low-order source data; it is the best
first discriminator.  Failure of a common unit minor or cross-prime row
specialization stops the bypass before any D43-scale build.

### Slice 2 — common pristine D43 rows

Run the existing exact `build_tails43.py` gold lane outside the local bounded
preflight, then stream its radkeys through the literal `a00pp` adapter.  Gate
`EB=0`, all 190 source-coordinate labels, all 184 row labels, the exact
coordinate descent/reconstruction certificate, denominator ledger, and
specialization at both primes.  Do not rebuild the quotient ring from
least-residue modular coefficients.

### Slice 3 — source Hensel test

Combine exact `34+184` in the explicitly certified source ambient, evaluate
the registered point, solve its entire first correction, and establish
localized generation/formal smoothness there.  Only this slice can promote
a `Z_p`/char-0 point.  Do not reuse the banked `218/184` Jacobian until the
exact coordinate descent is proven.

### Optional Slice 4 — banked-presentation equivalence

Lift or recompute the 509 basis with exact membership traces and connect the
184 source rows to the banked NFs.  This permits reuse of the current modular
NF geometry but is not on the critical path for direct source existence.

## 8. Firewalls and conclusion

- No `jc2-lean` path was entered, listed, searched, read, built, modified,
  status-queried, or controlled.
- No AWS job and no heavy local computation was run.
- No canonical ledger was edited.
- No existing source/artifact was modified; only the two new fail-closed
  files and this new xmodel report were added.
- No common 34-row source emission, 509 integral basis, all-218 `p^2` replay,
  smoothness certificate, `Z_p` point, or characteristic-zero point is
  claimed.

The clean decision is:

\[
\boxed{\text{Pursue the exact coordinate bridge plus reducer-free 34+184 lane first.}}
\]

The 509 lift is a valuable equivalence certificate and a route to reuse
banked NF calculations, but it should not block the faster direct-source
existence test.

## Seal note

The immutable SHA-256 of this report is printed in the producer handoff after
the final byte-level audit; it is intentionally not self-embedded.
