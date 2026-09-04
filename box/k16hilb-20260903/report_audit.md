# Independent audit of the unsealed report

Audit target: `xmodel/k16-hilbert-regseq-sol56-20260903.md` as read before
sealing.  Compared against `source_audit.md`, `symbolic_audit.md`,
`froberg_audit.md`, `computation_audit.md`, and the currently present output
artifacts.  No Singular job was started.

## Corrections required before sealing

1. **Pure powers and the Froberg identity are not equivalent.**  Lines
   352--356 call an indexed construction of one pure-power leader for every
   variable "equivalently" a proof of weighted-Froberg maximal rank.  The
   pure powers prove only `dim=0`; many zero-dimensional ideals have a
   different Hilbert function.  Froberg maximal rank is strictly stronger
   (although it would imply finite length and hence pure-power containment).
   Replace "or equivalently" by, for example, "or, more strongly, by".

2. **The requested `t=3..8` status needs explicit OPEN/timeout rows.**  The
   full-cone table stops at `t=7`, while both subset tables stop at `t=6`.
   Unless the currently running jobs finish cleanly, add explicit `t=8`
   full-cone `OPEN/timeout` and `t=7,8` literal-subset/tail `timeout` rows or a
   nearby failure table.  This distinguishes "not reported" from "not run"
   and makes the residual statement exact.

3. **The `t=8` Hilbert-target artifact must be explicitly excluded.**
   `t8_mod_p1009_b0_requested_target.out` has a clean exit and completion
   marker but used the unverified Froberg numerator as a target; it returned
   a one-element basis, `DIM=7`, and is circular/noncertifying.  The four
   mechanical acceptance conditions at lines 472--476 are therefore only
   necessary, not sufficient.  State that a Hilbert-target run is accepted
   only when its target numerator was independently certified (and ideally
   verify reduction of all input generators), and list this conjectural
   target run as excluded.

4. **The claimed `t=7` TSV validation is not yet present.**  The clean new
   output `t7_mod_p1009_b0_full.out` does support `dim=0`, length `43133`,
   5,830 printed minimal generators, and pure exponents
   `(16,11,9,8,8,8,7)`.  However, there is currently no
   `t7_mod_p1009_b0_full_initial_ideal.tsv`, and
   `initial_ideal_validation.md` explicitly says no `t=7` artifact was read.
   Thus lines 270--273 and 476--478 overstate the independent list/antichain
   check.  Generate and validate the TSV, or qualify the `t=7` entry as
   printed by Singular but not independently parsed.

5. **Synchronize the audit artifacts with the new `t=7` result.**
   `computation_audit.md` still labels the `p=1009`, root-400 run incomplete
   and treats `H7` as legacy-only; `froberg_audit.md` likewise describes the
   `t=7` comparison as a legacy replay.  The new output is clean
   (`JOB_DONE`, empty stderr, resource `exit=0`, wall 1199.14 s), and its
   decoded JSON is byte-identical to `legacy_t7_hilbert.json`.  Update those
   memos or note their audit cutoff so the final evidence bundle does not
   contradict Section 3.

## Wording/precision fixes

6. **Not every generated job performs the stated grading check.**  Lines
   79--81 are true of `emit_hilbert_job.py` jobs, which run `homog` and `deg`
   checks before `std`.  The preexpanded wrappers emitted by
   `emit_preexpanded_cone_job.py` do not run those checks; their validation is
   structural text preservation only.  Narrow the sentence to the
   recurrence-generated accepted jobs, or add equivalent checks to the
   wrapper before accepting a result.

7. **Clarify the coefficient field for lengths.**  Lines 31--34 say "all
   lengths" are equivalently dimensions over `A_t` and contrast them with
   dimensions over `Q`, but the `t=5,6,7` lengths are over `F_1009`, where a
   `Q`-dimension is meaningless.  Suggested wording: each length is over the
   run's coefficient field; for an exact nonsplit `A_t`, the geometric-fibre
   and `A_t` lengths agree and the underlying `Q`-dimension doubles; modular
   lengths remain special-fibre lengths.

8. **Make the leader equality's scope explicit.**  Lines 337--350 follow a
   uniform conditional statement, but the unqualified "In fact" can be read
   as uniform.  State explicitly: at fixed `t=3..7` the charged unit checks
   give the equality; uniformly it is conditional on every
   `mu_(t,k)` being a unit.  The conclusion that the coprime-original-leader
   route fails is valid either in the fixed range or under that uniform
   hypothesis.

9. **Distinguish run from accepted evidence at `t=3` modulo 1009.**  Lines
   96--99 correctly say both roots were run through `t=6`, but both `t=3`
   modular transcripts contain a parser error after the useful records.
   If the sentence is intended as an evidence claim, say that the clean exact
   `t=3` run is accepted and the two modular runs are diagnostic/tainted.

## Core claims independently confirmed

- The residual ring has exactly `t` variables, so no proper homogeneous
  `t+2`-tuple can be a regular sequence.  The actual stated-band degrees and
  the zero-of-order-two CI contradiction are correct.
- The corrected tail formula
  `L_t = t/(t+1) * binomial(3t+1,t)` and the reported values through `t=6`
  agree with the clean outputs.  Properness plus Cohen--Macaulayness is a
  valid independent characteristic-zero argument; it does not promote the
  modular length by flatness.
- The full Hilbert coefficient vectors and lengths through the clean new
  `t=7` run match the weighted-Froberg positive prefix.  The `t=8` value
  `215702` remains a candidate unless an actual full calculation completes.
- The prompt-order pure powers reported through `t=7`, the two exact `t=2`
  controls, the distinction from the old variable order and from the coarse
  sub-chart degeneration, and the fixed-range characteristic-zero `(V0)`
  verdict are correct.
- The modular/characteristic-zero warning and the final `PARTIAL` verdict are
  correctly conservative.

## Addendum: when a Hilbert-guided seed alone certifies dimension zero

Let `R=K[x_1,...,x_n]` over a field with the declared global term order, let
`I` be the actual input ideal in that same ring, and let `Gseed` be the output
of a Hilbert-guided call.  The following fallback is valid **without** knowing
that `Gseed` is a standard basis, provided one separately knows the minimal
software invariant

```text
every g in Gseed belongs to I.                              (A)
```

Indeed, put `M=<LM(g): g in Gseed>`.  Assumption (A) gives the exact
containment

```text
M subset in(I)=<LM(f): f in I>.
```

If `x_i^(a_i) in M` for every variable, then only the finitely many monomials
with all exponents below `(a_1,...,a_n)` can survive modulo `M`.  Hence
`R/M` is finite-dimensional.  Since `M subset in(I)`, `R/in(I)` is a quotient
of `R/M` and is also finite-dimensional.  Finally the initial-ideal theorem
gives `dim(R/I)=dim(R/in(I))=0` (and, in the homogeneous weighted setting,
equality of their graded Hilbert functions).  Notice that this proof needs
only `Gseed subset I`; it does not need `<Gseed>=I`.

The caveat is load-bearing for an **arbitrary conjectural** `H`.  Singular's
documented contract requires the optional Hilbert vector to be the first
Hilbert series (including its final non-series bookkeeping entry).  With a
wrong or malformed vector, its promise that `std(I,H,W)` returns a standard
basis is unavailable.  It is reasonable from Buchberger algorithm semantics
to expect every partial output to remain an `R`-linear combination of the
input generators, but that invariant must be treated as an explicit
implementation assumption unless it is backed by source-level documentation
or, preferably, exact transformation certificates `Gseed=U*I`.  Merely
re-standardizing `<I,Gseed>` does not repair missing (A): if a seed polynomial
lay outside `I`, the union ideal could be strictly larger and its dimension
zero would say nothing about `dim(R/I)`.

For the proposed computational check, let

```text
M0=minbase(lead(Gseed));  GM=std(M0).
```

Here `M0` is a monomial ideal (and `minbase` must preserve the ideal generated
by those leading monomials).  Under (A), either exact check

```text
dim(GM)=0,
```

or explicit reductions `reduce(x_i^(a_i),GM)==0` for every `i` is sufficient;
the latter exhibit the pure-power certificate directly.  Using both is
redundant but an excellent consistency check.  Prefer `dim(GM)` to trusting
`dim(M0)` when Singular warns that the unmarked object is “no standard basis,”
even though any monomial generating set is mathematically a Groebner basis.

This fallback certifies only fixed-fibre zero-dimensionality.  It does **not**
certify that `Gseed` is a standard basis, that `M=in(I)`, the conjectural
Hilbert series or its length, or the minimal generators/pure-power minima of
the full initial ideal.  At most it supplies the upper bound
`length(R/I)<=length(R/M)<=product_i a_i`.  A modular instance can then feed
the charged properness lemma for the characteristic-zero **dimension** only;
it still does not promote the modular length.
