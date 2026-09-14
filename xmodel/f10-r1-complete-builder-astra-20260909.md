# F10 r=1 complete ideal builder: unexecuted implementation packet

Status: **INTERNAL-UNREVIEWED / PREPARATION ONLY.** The exact sparse builder and
independent full-condition checker have been written and statically inspected.
Neither has been imported, compiled, run or tested. No ideal rows, candidate
point, unit certificate, runtime or solver result have been emitted. No compute
or launch authority is created by this report.

Actual start: 2026-09-09 12:05:12 UTC. Fixed terminal cap: 12:23 UTC, with the
parent's earlier-of-actual-plus-18-minute rule retained. Provenance basis:
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

## 1. Inputs and retained theorem scope

The new whole Euler producer `a5ab487c…` and terminal different-model gate
`77d59f7b…` were hash-checked before WHOLE reads. Root reports promotion 16r.
The three accepted 16q whole inputs are reused at their pinned exact interfaces,
not re-proved; the own terminal classical-admissibility report and static
frontier audit are likewise reused at their stated scope. Full paths, hashes,
and WHOLE-versus-excerpt scopes are in `input-pins.json` and `READ-SCOPE.md`.
All ten current input hashes were rechecked at 12:14:59 UTC. No live body,
unpublished peer proof, protected project, or new external theorem is consumed.

The imported theorem gives field-point equivalence between this L1 presentation
and the complete compact source contract, and equivalence of the exact unit
questions. It does not supply a point or unit certificate. A proper L1 would
give an algebraic-closure point and hence an ordinary constant-Jacobian
counterendpoint of actual degrees 112/196; the compressed degrees 4/7 are not
those source degrees. This preparation does not claim a nonreduced-base graph
isomorphism, rational-point necessity, classical openness, or global exclusion.

## 2. Literal builder specification

Owned directory: `box/f10-r1-complete-builder-20260909/`.

`builder.py` uses a rational sparse dictionary with twelve parameter exponents
and one S exponent. Fixed variable order is

`u, ell, d0, d1, v0, v1, v2, k1, k2, k3, k4, omega`.

Set d=d0+d1*S, v=v0+v1*S+v2*S², k=k1*S+k2*S²+k3*S³+k4*S⁴,
f=S*d-u, h=1-u*d+S*v. The coefficient array of A is (k,h,f,S), and B5=S².
For j=4,3,2,1,0 it constructs the WHOLE forcing

Qj=delta_(j+2)−(j+1)f'B_(j+1)+2fB'_(j+1)
−(j+2)h'B_(j+2)+hB'_(j+2)−(j+3)k'B_(j+3),

then divides each S^i coefficient by the fixed rational j−3i. Nonzero forcing
at either resonant slot is an exception, not discarded. The free B3/S and
B0/1 coefficients are fixed to beta=gamma=0; k0=0 is explicit. No parameter
pivot or localization by u occurs.

Delta is 1+u*t−ell*t*Pi−t*Pi² with Pi=t−u*t²+S*t³. The builder's descending
delta array follows the accepted printed coefficients. Its two remaining
polynomials are

E1=2k'B2+h'B1−hB1'−2fB0'−u,

E0=k'B1−hB0'−1.

Every S coefficient of E1 in degrees 0–8 and E0 in degrees 0–9 is retained,
including zeros, followed by omega*a*b−1, where a=k4 and b=[S⁷]B0. Thus the
accepted ambient presentation has twenty ordered slots. Actual nonzero row
counts, term counts and realized degrees are not known until execution.

The export includes all A_j, B_j, whole forcings, both resonant zero slots,
every coefficient slot within their envelopes, all full-Jacobian slot mappings,
all ten inverse-pole slots, both residuals, the guard, and exact restoration
metadata. Coefficients are reduced numerator/positive-denominator STRINGS;
exponent vectors are small nonnegative integers. Direct Python JSON writes use
exclusive files; no float or JavaScript numeric round-trip is used.

## 3. Independent checker and what PASS would mean

`checker.py` imports no producer mathematics. It has a separate sparse
implementation with both S and t coordinates, parses canonical exact wires,
rebuilds A from the parameter definitions, and differentiates the complete
serialized pair to form A_S B_t−A_t B_S. It independently constructs the
FACTORED Delta, rather than using the producer's delta array or recurrence.

It checks all t⁷ through t² coefficients vanish, and that the complete t¹ and
t⁰ polynomials equal every saved residual row. Saved forcing data are checked
by subtracting each diagonal contribution from this independently computed
full determinant. Envelopes, all zero-slot maps, gauges and tops are checked.

Independently of the module quotient formulas it substitutes
S=p*z³−z²+u*z, t=z^−1. Terms S^i*t^k with i>=k cannot have negative z powers;
only i<k are expanded, hence at most the fourth power of this small trinomial.
It collects ALL three A and seven B negative coefficient slots and rejects any
unmapped pole. This is a low inverse check, never a degree112/196 source-power
expansion. The u=0 mode performs literal specialization and the same checks.

Guard restoration is checked against the actual computed leading coefficients:
A_original=A/a, B_original=B/b, c_original=1/(ab), eta_original=ab. Guard
omega*ab−1 supplies both inverses; the cleared monic identities are a/a and b/b.
It does not falsely impose k4=1 or b=1. A successful checker verifies the
presentation artifact, NOT that its residual polynomials vanish at any point.

## 4. Designed controls, not passed controls

`VALIDATION-PLAN.md` specifies seven ordinary-Python modes: full, u-zero,
dropped-constant, u-zero-dropped-constant, upper-coefficient, guard and
leading-top. The constant attack removes the actual −1 monomial from E0 AND
its S0 row; a deliberately weakened upper-only mathematical verifier is
required to accept it before the complete checker rejects it. The same attack
is required at u=0. The upper attack changes d0*S²/2 in B4 to 3*d0*S²/2 in both
storage locations while preserving B5; guard and false-a=1 attacks modify
actual payloads too. No mutation has run; no pass count is claimed. There is no
`assert`-based evidence and no optimized-mode evidence. A separate large-integer
precision attack remains pending, not silently credited to string encoding.

## 5. Execution gate and pending obligations

Both entrypoints call the metadata-only `execution_gate.py` before mathematical
imports or construction. The supplied authority template is disabled. Root must
independently register the exact AWS instance/hostname/job/admissibility pin,
executable/dependency/input hashes, full parent CAPRUN argv and child argv,
caps, cwd and exclusive outputs. The parent check is element-for-element on
the raw NUL-split argv; merely containing a runner pathname cannot pass.
`ops/run_capped.py` is unchanged. No allocation, shell worker, solver, or new
supervisor is implemented. Local host discovery or a matching path alone does
not create authority.

Static inspection is the ONLY implementation evidence here. Syntax/import
checks, launch rejection/dummy lifecycle controls, exact emission, independent
full and changed-object checks, serialization precision, and measured
rows/terms/degrees/time/CPU/RSS all remain pending on a separately registered
capped worker. The actual checker can report counts/degrees; CAPRUN supplies
lifecycle/resource telemetry. These source files are not a license to solve,
choose a prime, compute a basis, allocate a machine or expand the source.

## 6. Publication and collisions

New source/text edits use apply_patch only. The report is published by the
existing begin/close/finalize/verify transaction. Current input and owned-file
hashes are recorded in custody; the final report/manifest are pinned after
publication. All authored code/text receives a WHOLE static read before the
body marker. No mathematical subprocess of any size ran, including syntax
compile, imported builder, checker, numerical toy, or frontier execution.

OPEN(S) RAISED: None. Runtime validation is explicitly pending engineering work,
not a new mathematical open-problem identifier.

COLLISIONS: EMPTY — own-artifact check only; no corpus scan. The new packet does
not modify the accepted 16q/16r proofs, prior code or shared ledgers. No
follow-on task, claim promotion or external launch is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8133`.
- Body SHA-256:
  `f0e0c4f94df5de5bbdff086f4c3d78f01daa5085eb8f24e2139b0734edbd67c9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
