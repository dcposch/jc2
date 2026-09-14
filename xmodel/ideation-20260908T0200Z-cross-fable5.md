# 0200Z adversarial cross — Fable 5.1 lane

2026-09-08. Model start 02:41:33 UTC; hard stop 02:56 UTC. Inputs: whole
`cross-poststate.md` and the four collected blind reports (coordinator, astra,
fable5, sol56) in `/tmp/jc2-lane.kRN787/inputs`, plus the frozen packet and
snapshots as lookup context only. Tiers unchanged: 15h ACCEPTED; nonodd theorem
PROVISIONAL (15i coalesced, still not a cross premise); golden and common
controls root-checked; minimal receiver ACCEPTED. No promotion from agreement.
No charge_basis. Skeleton; sections are appended below as completed.

## 1. Merged fingerprints, origins and disagreements preserved

**Golden eight-parameter object (Astra Card 2 = Fable blind Card 1, independent).**
Both blind reports wrote the same polynomial family. Astra's `(u,v,w,lambda,tau,alpha,beta,gamma)`
is Fable's `(R3 two slots, R1, lambda, f, alpha, beta, gamma)`:

    R = H + u g p² + v p³ + w p,   F = lambda D + tau p,   mu = 5 lambda²/9,
    A = R³ + alpha R + F,
    B = R⁵ + beta R³ + gamma R + (5R²/3 + beta − 5alpha/9) F + mu L,
    [A,B] = [R,T] + [F, mu L],   T = (3R²+alpha) mu L − delta F − (5/3) R F²,
    delta = gamma − beta alpha + 5alpha²/9.

Agreement is not evidence. The two origins differ in status: Fable derived it as the
`j=12` first-contact stratum of the odd golden chain (necessary, conditional on the
transported steps below); Astra states it as a literal sufficient ansatz with no
classification claim. Both are right at their scope. Astra counts ten parameters because
the two inverse-lift parameters are retained; Fable's eight is the bracket-only count.
A solution of the bracket rows is a receiver point only after every polynomiality row,
every negative Laurent row after the accepted inverse, both conjugates and the guards
hold. Nobody has such a point.

**Thickened-branch shortcut (coordinator Card A, Astra dual-number control, Fable
OPEN[GOLDEN-RAMIFIED-INITIAL]).** Three independent negatives agree that the reduced
3/5 consumer cannot be copied onto the repeated branch. This is agreement on a failure,
verified in §3; it carries no positive content.

**Uniform source/Euler (Astra Card 1 binomial family, coordinator Card C, Sol's bottleneck
statement).** All three want a parameterised theorem. None supplies a second receiver
attachment; the only instance attached is the retired `r=2,s=3`.

**common_4 (coordinator Card B, Sol Card 2 C4-FILTER, Fable not carded).** Coordinator
and Sol want a bounded test; Fable called the weight-trim question KNOWN Newton-polygon
work. This disagreement stands; see §2(d).

**46-ID dispositions.** Consensus: raise 29; lower 4 and 36 (coordinator lowers 36 only).
Contested: 1 (coordinator, Astra raise; Fable, Sol unchanged), 3 (Astra, Fable raise),
38 (Astra, Sol raise), 18 reopen and 33 lower (Astra only). No cross resolution; all
theorem-level ranks remain unchanged and these are task-level moves.

**Systems.** Coordinator NO_NEW_MACHINERY, Astra NO_CHANGE, Fable advisory checker lint,
Sol sealed-launch attestation. Selection in §4.

## 2. Attacks on the strongest mechanisms and hidden hypotheses

**(a) Source first-contact transported to golden.** The chain that Fable's blind report
said "holds verbatim" has these hidden hypotheses, now made explicit.

- Oddness. The accepted minimal receiver report never states parity for golden; the
  golden control's `F_a` merely happens to be odd. Fable's survivor table (even `j` only,
  `j<=12`) is therefore an ODD-GOLDEN deduction. Nonodd golden keeps `j<=12` from
  `deg U = 12−j >= 0` but adds odd strata, e.g. `j=11: F_11 = c D p`, `j=9: U in <gp²,p³>`,
  and needs the nonodd A-reference and all five scalar kernels of the provisional 15i
  theorem, which is not a cross premise. The two scopes must be tracked separately.
- Centralizer `K[H]`. The Newton-slope argument (valuations `(0,0,0,−5)`, slope `5/3`)
  gives geometric integrality of the generic fibre and is field-pattern independent.
  This step is sound for golden. The kernel removal needs `deg T = 35−2j` not a multiple
  of 5 except `j=10`; same as 15h.
- Divisibility. `H | F_j²` gives only `D | F_j` (golden control (1)); `F_j = D U`,
  `w(U) <= 0`. Correct, but the `j=10` and `j=12` strata survive, so the chain proves
  nothing for golden without a new consumer.
- Consumer. Fable's thickened injection into `K̄(p) × K̄(p)[ε]/(ε²)` is a true linear
  injectivity lemma. It does NOT license the 3/5 rigidity on the ε-component: the
  dual-number pair commutes there (§3), and the UFD step `f⁵ = g³ ⇒ f` a cube of a monic
  linear fails in a nonreduced coefficient ring. Fable's blind wording "licenses
  global-initial bookkeeping" was an overstatement; the lemma is bookkeeping only.
  OPEN[GOLDEN-RAMIFIED-INITIAL] stays typed OPEN, and root's ramified 6/10 control shows
  that in the sheet coordinate `w` with `z ~ w²` the initial degrees double to 6/10 and
  coprimality is lost, so no copy of the 3/5 lemma exists there either. A golden
  consumer needs a source-specific obstruction, e.g. an `ε²`-level or second-order source
  identity distinguishing `F_12 = lambda D` from the commuting fixture. None is derived.

**Corrections to Fable's own blind report.** (1) "One explicit bracket evaluation ...
sub-second ... either way binding" is wrong on two counts: a bracket evaluation yields a
polynomial system in eight unknowns plus `c` over `Q(rho)`; deciding whether `lambda=0`
is forced is an elimination with `lambda` inverted, not an evaluation, and its runtime is
unmeasured. The outcome set is `lambda` forced zero / a `c!=0` solution / INCONCLUSIVE.
(2) A `lambda!=0` solution is not a golden receiver point until the full row set holds.
(3) The survivor table is odd-golden only. (4) The degree-14 top cancellation
`H[H,L] = 2D[H,D] = 2p⁴L³M⁴([p,L]/(pL) − [L,M]/(LM))` was rechecked by hand here via the
log-derivative expansion with exponent vectors `H=(2,1,2)`, `D=(1,1,1)` over `(p,L,M)`;
it requires exactly `mu = 5lambda²/9`, which both reports use. (5) The classification
"every step holds verbatim" was desk work, not a gated theorem; it stays PROVISIONAL desk.

**(b) Astra's binomial-top family.** Checked interfaces: `as−br=1` gives `gcd(r,s)=1`
and `w(H)=1`; the `p^r`-recovery needs `b>2` (a monomial `g^i p^l`, `l<r`, has weight
`>= b−br > 2−br`), stated correctly; `2j ≡ 0 mod e` only at `j=e,2e`, giving `H⁵,H³`
kernels as claimed. Hidden hypotheses: oddness (used to kill scalar constants), the
squarefree branch product (`g^s+p^s` squarefree, fine), and the classical UFD step in
`K̄(p)[Z]`, valid there because the ring is reduced. Verdict: a plausible library lemma
with no second attachment. Not a cross premise; do not gate it before a receiver with a
binomial top exists, and golden is not binomial.

**(c) Coordinator Card C.** Same status as (b): abstraction is cheap, attachment absent.
Retaining `gcd(m,n)` and the scalar kernels is the right checklist; nothing more here.

**(d) Sol's C4-FILTER.** No literal LP is supplied, so nothing can be closed. The
inequalities 15h consumes are not raw-support inequalities: finiteness of the reference
division needs a unit leading coefficient and a replacement that lowers g-degree without
raising degree or weight; the kernel removal uses exact scalar orders (`ord alpha >= 10`,
`ord delta >= 20`) that come from identity (5), not from support; `K[H]` needs geometric
integrality of the common_4 generic fibre; injection needs squarefree `V0` and the
weight-to-g-degree lemma. A feasible `L(i,j)=ai+bj` supplies none of these; an infeasible
one closes only single-linear-filtration encodings. The commuting fixture `R³,R⁵`
satisfies every support inequality and fails only at the bracket, so the LP cannot
separate it from a source. Coordinator Card B (weight trim from the full Jacobian) is the
correctly posed question; Fable's blind "KNOWN" label stands in the sense that the
interface report already shows faces alone cannot trim, but the full-Jacobian
implication is untested and a bounded desk test is legitimate.

## 3. Cheapest decisive test executed, and the proposed one

**Executed (owned box, stdlib, capped 30 s / 25 CPU / 512 MiB, `python3 -I -B`, normal
and `-O` byte-identical stdout).** Free-symbol 3/5 identities only.

    P = Z³ + ε p² Z,  Q = Z⁵ + (5/3) ε p² Z³:   [P,Q] = 0 mod ε²,
    untruncated [P,Q] = −(20/3) ε² p³ Z³,        P⁵ = Q³ mod ε²,
    (Z + ε a)³ = Z³ + 3ε a Z²  (a Z² term, never a Z term), so P is no cube;
    mutation 5/3 → 4/3 does not commute;
    (Z² + p)³, (Z² + p)⁵ commute exactly;  the reduced pair Z³+p²Z, Z⁵+(5/3)p²Z³ does not.

Outcome: the shortcut "apply the reduced 3/5 consumer to the nilpotent component or to
the ramified 6/10 chart" is refuted by explicit commuting pairs. Stop scope: this closes
only that shortcut. It says nothing about golden emptiness, the `j=12` stratum, or any
source point.

**Hand-checked low jet (not machine-verified).** Linear parts: `[p]A = alpha w + tau`,
`[g]A = 0`, `[g]B = mu`, `[p]B = gamma w + (beta − 5alpha/9) tau + mu`, hence
`J0 = −mu(alpha w + tau)` and `tau = −alpha w` whenever `lambda != 0`. Astra's degree-2
rows were not rechecked.

**Proposed, not executed.** The `j=12` decision: expand `[A,B] − c g²` (degree `<= 14`
after the top cancellation), retain every coefficient row, both conjugates, and decide
the ideal with `lambda` inverted. This is an eight-unknown elimination over `Q(rho)`
of unmeasured cost; it needs root authorisation and a recorded wall cap. Outcomes:
`lambda` forced zero retires the stratum; a `c!=0` solution is a candidate needing the
full row set; timeout is INCONCLUSIVE. Expected gain is the first exact answer on whether
the golden client has a nonzero-Jacobian first contact at degree 3.

## 4. Systems: one upgrade selected

Evidence verified in frozen inputs: PROGRESS records two Fable checkers exceeding
generator-only scope and a full-pair control run despite a contrary flag; the 0156
harvest records reviewer C1 building sparse 15/25 toy pairs under a no-A15/B25 header
and an unrecorded inner timeout group. These are three recorded recurrences with a root
correction cost each. Sol's attestation addresses an ordering ambiguity that root
resolved manually this round with no recorded failure, and it adds a new artifact and
gate. The coordinator's own launcher-declaration lapse is addressed by neither.

Selection: Fable's advisory static scope lint, and NO_CHANGE otherwise. Smallest test:
run it on the three charged 15h checkers and the retained C1 block; it must flag C1 and
pass the three; one false positive on an accepted checker discards it. It is advisory,
never edits a checker, and fits NO_NEW_MACHINERY. Defer the attestation.

## 5. Recommendations

- Proof: CONTINUE the nonodd review as owned; do not fold 15i into golden. Golden:
  CONTINUE only the odd-golden desk chain to the explicit `j=10`/`j=12` strata plus the
  nonodd stratum list; STOP any consumer that copies the 3/5 lemma onto nilpotent or
  ramified charts. common_4: coordinator Card B as one desk test with the `R³,R⁵`
  fixture as mandatory negative control; C4-FILTER only after a literal LP exists.
- Disproof: the `j=12` stratum decision under root authorisation and a cap; no builder,
  no AWS, no solver rerun.
- Uniform/Euler: NO cross premise; library-lemma status until a binomial-top receiver
  is named.
- Systems: the lint's smallest test only.

## 6. Custody

Inputs hashed in `box/ideation-20260908T0200Z-cross-fable5/input-hashes.txt` (poststate,
four blind reports, packet, manifest, golden control, 15h proof, three harvests,
PROGRESS). Control `thickened_controls.py` SHA-256
`ab362387ae6ecc64dd1e360ca2c9c680f5af6c1e15dcff9f8a823de2583790f4`; stdout (normal and
`-O` identical) `647faefd1b42986361bf55233731eef3eebf7428ce80e0d2222bfdb9cb91955b`;
empty stderr. No snapshot byte, shared or protected path was written. No CAS, AWS,
source objects, H/R powers, peer live reports or new agents were used. JC2 unresolved;
no promotion, no charge_basis.

<!-- BODY-END -->
