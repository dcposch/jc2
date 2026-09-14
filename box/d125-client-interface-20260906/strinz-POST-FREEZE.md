# Post-freeze research frontier — 30 August 2026

> **Status.** This is a research communication note, not part of the
> `0.1.0-preview` theorem or evidence bundle. It summarizes post-freeze work
> through internal checkpoint `8b5fac46`. The exact supporting artifacts remain
> in the research repository and have not been curated into this public tree.
> No degree-`(75,125)` exclusion, counterexample, properness theorem, or
> actual-pair occupancy claim is made.

This update supersedes the allocation advice in the 25 August note while
preserving its exact historical claims. Its purpose is to expose reusable
formulas and precise open interfaces to researchers working on Family F2,
approximate-root recurrences, nonproperness, or formal plane-Jacobian
reductions.

## 1. The actual source bracket has a periodic band normal form

The literal degree-`(75,125)` source bracket now reproduces the OMEGA
common-power staircase through the first resonance:

| depth | forced Q band | source meaning |
|---:|---|---|
| 1 | `q24` | K1 |
| 2 | `q23` | K2 and `rbar | p14^2` |
| 3 | `q22` | complete K3 carrier divisibility |
| 4 | `q21` | complete K4 root-jet locus |
| 5 | `q20` | one-dimensional resonance, kernel `span(rbar^4)` |

Thus the OMEGA formulas are not merely parallel model calculations: through
these depths they solve literal source-bracket rows. At depth five the
invariant object is the quotient class

```text
[q20] mod span(rbar^4),
```

not a canonically normalized shear coordinate.

## 2. K5 is classified and globally occupiable as a legal truncation

On the landed K3+K4 locus, polynomiality of the global rational `q20` formula
is equivalent to literal band-31 solvability. At a double carrier root, write

```text
A = ord(p14),  B = ord(p13),  C = ord(p12).
```

The K5 survivor types include the robust `A>=4,B>=2` channel, one tuned
`A=5,B=1,C=0` channel, and the deeper `A>=6,B=1,C>=1` channel. Composing these
local conditions with the legal degree windows gives 22 occupied rows out of
a 24-row source-truncation table; the two nonzero-`p14` double/double rows fail
by the exact divisor-degree inequality `6+6>11`.

These are explicit finite truncation witnesses. They do not establish that a
complete standardized F2 pair realizes any row.

## 3. The next source bands sharply prune the K5 table

The complete `q18` Laurent remainder on the `k=1` families is controlled at
its first relevant tiers by two monomials. On the tuned
`(m,k,ell)=(2,1,0)` family it has the guarded nonzero coefficient

```text
25*c5*lamQ*q1^3 / (486*lamP^4*r2^7)
```

at order `-6`. Since `q18` is a polynomial source band, that local family is
eliminated at K7, independently of `P10`. Every global K5 row containing this
root type is therefore dead.

For the restored `m>=3,k=1,ell>=1` family, the first remainder order is

```text
min(m-8, ell-6).
```

The single-term and tied leading coefficients are explicit. The remaining
global question is a finite Hermite/degree-budget recompile, not another
generic K7 march.

## 4. One robust q19 component survives with an exact normal form

On the simplest occupied `S0,kE=2,(d1,s1)` component, the full band-30 image
problem collapses to

```text
Psi(p12(1)) = 0,
p12'(1) = 0,
Psi(p12 mod S0) = 0,

Psi(x) = -40*x^2 + (560/27)*x - 1000/729.
```

The depth-six operator is injective, so `q19` is unique. Its complete cokernel
proves that the first-resonance coordinate, the OMEGA shear, `p9`, `p10`, and
`p11` are image-inert on this component. The row itself forces the legal top
coefficient of `q19`.

The quadratic has discriminant class `[6]`. It has no point over the rational
descent field used by the exact checker, but over the theorem-facing complex
ambient field it yields four seven-dimensional affine components and an
explicit polynomial `q19`. Consequently this result parks a componentwise q19
sweep: it is a structural normal form and a positive truncation result, not an
exclusion.

## 5. Row 40, Row 42, and the reduced-model boundary

The RSTEP stage audit distinguishes two exact objects:

- Row 42 is the bracket tower of the pre-`T` stage-1 object.
- Row 40 is the bracket tower of the post-`T` stage-3 object, because the
  monomial transformation contributes the required Jacobian factor.

A complete corrected reduced Row-40 tower would homogenize to a Keller pair of
degrees `(15,25)` and is excluded by classical low-degree results. This closes
the reduced model, not the actual `(75,125)` source: the known monomial
adapters either miss the degree scale or introduce Laurent terms. The missing
source-to-reduced adapter is therefore explicit and remains open.

The source-positive finite Row-40 model is dominant through `L=41` and first
non-dominant at `L=42`, with 145 essential rows and rank 133 at fixed gamma.
Rank deficiency does not decide whether its distinguished zero lies in the
image. A full nonlinear export is currently cost-walled; the useful successor
is a directional/tangent-cokernel computation at the `L<=41` contraction
witness.

## Interfaces that may be useful to other projects

- **Literal source recurrence.** The depth-dependent first-order operators,
  their five-periodic resonances, and their finite Hermite cokernels may be
  comparable with approximate-root or Faber-normal-form recurrences.
- **Roy van Rijn's F2 work.** Both programmes see universal `3/5` cancellation
  polynomials, but no theorem identifies the carrier coordinates or occupancy
  hypotheses. A typed native-coordinate map remains the useful bridge.
- **El Hilany–Tsigaridas.** The relevant F2 edge is pertinent and its toric
  coordinate is literally `w=x*y^5`. Local constant-multiplicity conclusions
  remain stratum-specific; the source-band results above refine which strata
  are actually available.
- **Formal low-degree work.** The `dcposch/jc2-lean` project attacks much lower
  partial degrees with a different source decomposition. Its fail-closed
  source/local/global theorem interfaces are an architectural model, not a
  theorem imported here.
- **Collision geometry.** A bridge still requires a global finite
  normalization, moved-sheet data, and a trace/conductor map. Local carrier
  jets alone do not provide those objects.

## Current bounded questions

1. Recompile the complete K5 occupancy table through the exact q18/K7 pole
   conditions, including simultaneous Hermite feasibility and zero-band
   rescues.
2. Resolve only the next Laurent tier on the two surviving tied `d2` patterns.
3. Decide the corrected `L=42` distinguished zero fibre by a constrained
   tangent/cokernel or first weighted Schur obstruction.
4. Construct `DICRITICAL-EXTENSION` before importing target-degree constraints.

Further q19 component sweeps, q15, K8 marching, broad Gröbner calculations,
and degree-pair claims are not licensed by the present evidence.

## Public-release boundary

The frozen preview remains the citable, replayable package. This note does not
change `THEOREMS.md`, the frozen proof artifacts, checksums, release metadata,
or the `0.1.0-preview` claim ledger. A future `0.2` or addendum should import
post-freeze mathematics only after its exact artifacts, hostile controls,
dependency custody, and release checks are curated together.
