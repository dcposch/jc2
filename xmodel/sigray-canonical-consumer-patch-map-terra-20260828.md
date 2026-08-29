# Surgical patch map: Sigray Section 7--9 consumers after the root-scope audit

Date: 2026-08-28  
Producer: GPT-5.6-terra / Codex, read-only consumer audit  
Scope: the eleven named `ladder/SHEET6-*` consumers and statically affected
`cases/*.py` files.  `jc2-lean` was neither entered, listed, searched, read,
built, modified, status-checked, nor controlled.  No consumer or engine file
was edited.

Line numbers and quotations below refer to this exact source snapshot:

```text
555363fd...  ladder/SHEET6-AF3.md
01cfd9b7...  ladder/SHEET6-TDU-REVIEW.md
086a4759...  ladder/SHEET6-CAMPAIGN.md
6c045f36...  ladder/SHEET6-A3L1-REVIEW.md
cf84555a...  ladder/SHEET6-A2P-REVIEW.md
a0d71267...  ladder/SHEET6-H3.md
aaaf1dba...  ladder/SHEET6-HIII-REVIEW.md
89d6303c...  ladder/SHEET6-REVIEW.md
78215e1f...  ladder/SHEET6-MULTIPOLE.md
2cc7c194...  ladder/SHEET6-2POLE.md
04247d66...  ladder/SHEET6-MP-REVIEW.md
41208832...  cases/sheet6_campaign.py
8bd0a55a...  cases/h3_check.py
1b899999...  cases/hiii_compose.py
a235f37f...  cases/twopole_check.py
2642c0ab...  cases/monodromy_td.py
```

## 0. Controlling facts and present review status

Three corrections must not be conflated.

1. **Corrected Proposition 8.4 is nonroot only.**  It proves `M_F != 1`
   for a singleton-pole counterexample only when
   `F in T_a^& cap (V_a \ {(0,y)})`.  The printed root clause is an open
   proof gap: for `F=(0,y)` the descent has `n=0` and `H=F_{-1}` is
   undefined.  Pole vertices are nonroot, so every pinned pole-entry
   `M=1` kill remains valid.
2. **Statements 8.4 and 8.5 survive.**  Statement 8.4 is valid even on a
   root edge.  The reviewed cyclic semi-invariance repair proves Statement
   8.5, including its congruence conclusion.  Thus at a case-IV terminal
   one may retain `M_(0,y) | M_G`; one may not delete the divisor `1` by
   invoking Proposition 8.4.  Statement 8.2 is valid only at nonroot
   vertices; a root use must be replaced by a direct reduced-ODE/top-degree
   calculation.
3. **The Section 7 repair is not yet promoted.**  The resolution-free
   quotient proposal at SHA `71aba565...` failed its Terra gate at SHA-file
   `xmodel/sigray-section7-resolution-free-coordinator-hostile-review-terra-20260828.md`:
   it must track the induced quotient isomorphism `tau_(i,a)` and prove
   transport of the repaired jump/max `kappa`.  Consequently the literal
   per-puncture `delta_a`, printed equation (22), literal nested `Y(F_i)`,
   and printed proof of Statement 9.4 may not be cited as established.
   Once the minimal `tau`/`kappa` repair clears a different-model gate, the
   correct replacements are the cluster identity `(22-cl)` and disjoint
   first-separation exit sets.  Until then every global `Sigma lambda`
   conclusion below is conditional.  The reviewed Section 9 conclusion is
   correspondingly a **conditional** repaired theorem: `td >= 6`, not an
   exclusion at `td=6`.

The clean vocabulary to use everywhere is:

```text
NR-M1: corrected Proposition 8.4 kills M=1 at a certified nonroot down vertex.
ROOT-M: at (0,y), Statement 8.5 gives divisibility only; M=1 is allowed.
EXIT: lambda charges are assigned to disjoint first-separation exit sets.
22-cl: cluster excess delta_a^cl replaces the literal per-puncture delta_a.
```

## 1. `ladder/SHEET6-AF3.md`

### Lines 135--139: actual false root restriction

Current:

> `M_(0,y)` divides `M_G`, and Prop 8.4 ... forbids 1, forcing
> `M_(0,y)=3` ... resp. `in {2,4}`.

Replace by:

> By repaired Statement 8.5, `M_(0,y) | M_G`.  Corrected Proposition
> 8.4 has no root clause, so the allowed divisors are `{1,3}` in classes
> 1 and 3, and `{1,2,4}` in classes 2 and 4.  This is satisfiable and adds
> only divisibility constraints on the root data.

At line 170 replace “Prop 8.4/8.5 at the terminal” by “Statement 8.5 at the
terminal; corrected Proposition 8.4 is unavailable at the root.”

**Effect:** proof repair only.  The four survivor classes do not disappear;
their compatibility statement becomes strictly stronger.  All pole-entry
kills in lines 23, 50, 62--72, 105--111, and 181--183 are unchanged because
a pole vertex is nonroot.

### Lines 205--212: Section 7 dependency

Current text correctly diagnoses nested literal `Y(F)` but leaves the
branch-at-`F` reading as standing H2.  Replace its disposition by:

> Replace literal `Y(F_i)` along a characteristic path by the disjoint
> first-separation sets `E_i`; apply repaired Corollary 7.1 once to their
> union and the separate x-side `psi` cluster.  This repairs Statement
> 9.4 after `(22-cl)` is promoted.  The dependency is presently
> provisional pending the `tau_(i,a)` and `kappa` transport gate.

**Effect:** the local entry pin and four-class list are unchanged.  Any
claim that their displayed budgets are theorem-grade is conditional until
Section 7 closes.

## 2. `ladder/SHEET6-TDU-REVIEW.md`

### Lines 189--193: actual false root restriction

Current:

> St 8.5 + Prop 8.4 at `(0,y)` force `M_(0,y)=3` -- satisfiable.

Replace by:

> Repaired Statement 8.5 gives only `M_(0,y) | 3`, hence
> `M_(0,y) in {1,3}`.  Corrected Proposition 8.4 imposes no root
> restriction.  Both values are compatible, so the zero-charge terminal
> remains unexcluded.

**Effect:** no change to the two `td=9`, `Sigma lambda=0` survivor classes;
the negative result is stronger.  The prime-`td` theorem TDU is completely
unchanged because its `b=1` kills occur at pole entries.  TDU-c and all
claims using (25) should be labelled conditional on the repaired Section 7
budget; TDU itself needs no H2/Section 7 input, as lines 220--223 already
observe.

## 3. `ladder/SHEET6-CAMPAIGN.md`

### Lines 20--21 and 43--44: root scope plus global budget

Replace the two blanket summaries by:

> The local case-IV calculation gives `lambda_root=0` in the working exit
> allocation.  Its global ledger uses `(22-cl)` and is conditional until
> the Section 7 quotient/weight transport closes.

and

> With disjoint first-separation exit sets, repaired Statement 9.4 gives
> `Sigma lambda <= td-2` (conditional on `(22-cl)`).  Corrected Proposition
> 8.4 kills `M_F=1` at every **nonroot** down vertex of a singleton-pole
> characteristic sequence.  It gives no root kill.

The current phrase “any M=1 outcome kills the chain” must not remain.

### Lines 52--63: overbroad Statement 8.2/IIa sentence

Current line 60 says `k>0 => l=0 (St 8.2)` without scope.  Replace it by the
reviewed Section 9 wording:

> In the `mu=2` IIa branches actually solved below, nonroot regularity and
> Statement 8.2 force `l=0`.  In general the reduced `q` has a simple
> factor at each root of `p`; `k>0` supplies positive exit charge, not a
> universal `l=0` theorem.  Statement 8.2 is not used at `(0,y)`.

### Lines 72--81 and 89--91: historical G2/H2 wording

Replace “and no M=1” by “and no certified **nonroot** M=1; the printed
terminal leaves root `M` uncontrolled.”  The reason the printed dichotomy
fails is now cleaner: neither a root `M=1` nor a root `M!=1` conclusion is
licensed.  H2 should be stated as

```text
NR-M1 kills + first-separation EXIT charges + no-applicable-case,
conditional on repaired (22-cl).
```

### Lines 174--180 and line 231: engine/census statement

Current:

> kills: child `M_F=1` ...

Replace by:

> kills: a child `M_F=1` only after the child is certified nonroot.  A
> child with root signature `(nu,kappa-bar)=(1,1)` is a terminal candidate
> and is recorded before any M-filter.

Until the root-aware rerun is complete, replace “Current terminal-class
endpoint: eight classes” by “Current **nonroot/IV** ledger: eight classes;
root-signature `M=1` candidates were under-enumerated and are pending the
root-aware rerun.”

**Effect:** the mathematical `td<=5` exclusion survives through the reviewed
row-4 repair and nonroot pole-entry kills.  The old phase-1 and composed
root/SF1 census is invalid as an exhaustive census and may broaden.  No
existing nonroot survivor is removed by this correction.

## 4. `ladder/SHEET6-A3L1-REVIEW.md`

### Lines 112--115 and 295--299: “nitpick” is a proof gap

Current text calls the root use of Proposition 8.4 a nitpick/cosmetic issue.
Replace both occurrences by:

> AF3's root `M!=1` sentence is a genuine proof gap, not a hedge-word
> issue: corrected Proposition 8.4 excludes `(0,y)`.  Repaired Statement
> 8.5 retains only `M_(0,y)|M_G`.  This defect has no weight in the entry
> pin or four-class verdict.

### Lines 151--165: replace the incomplete grade argument

The current argument incorrectly tries to delete a homogeneous grade-zero
summand merely because a grade-one inhomogeneous summand exists.  Replace
the proof paragraph by a citation/summary of the reviewed cyclic
semi-invariance repair (`xmodel/sigray-cyclic-semi-invariance-repair-sol-ultra-20260828.md`,
final Terra gate): at a nonmerge/nonroot down vertex the stabilizer action
makes every residual a single effective character; unique nonzero
root-orbit plus direct positivity of `G` and the reduced ODE force the
terminal residual to have character one, hence `q=eta r(eta^nu)` and
`gcd(nu,deg q)=1`.

**Effect:** proof repair only; the L1a menus and all enumerated cells are
unchanged.

### Lines 281--286: Section 7 disposition

Replace “branch-at-F reading is forced ... confirmed” by the actual repair
status: first-separation exit sets are the correct replacement, and their
global use is conditional on the repaired `(22-cl)` gate.  Local AF2
per-orbit lower bounds remain valid; only summation/ownership changes.

## 5. `ladder/SHEET6-A2P-REVIEW.md`

### Lines 23--25 and 159--185: shared budget is not printed-confirmed

Current:

> CONFIRMED (Cor 7.1 is one global Euler-characteristic budget ...)

and lines 164--168 cite printed equation (22) plus printed `delta_a>=0`.
Replace by:

> **CONDITIONAL PASS.**  The shared-union form is the right repaired
> conclusion: assign each cv cluster to its first-separation exit, apply
> repaired Corollary 7.1 once to the disjoint union, and count the shared
> suffix once.  The literal `Y(F_i)` and printed per-puncture equation (22)
> do not prove it.  Promotion awaits the `tau_(i,a)`/`kappa` transport
> repair for `(22-cl)`.

Lines 100--118 are a local charge argument and need only replace “member of
`Y(F)`” by “member of the exit set owned at `F`”; its lower bound is
unchanged.

### Lines 193--213: Proposition 8.4 audit scope

Change the verdict to “CONFIRMED for nonroot starting vertices.”  In the
inventory, prefix item (1) with `F != (0,y)`/`n>=1`; explicitly say the
printed root clause has `H=F_{-1}` undefined.  The singleton-regularity and
merge-forbidding analysis is otherwise unchanged.

**Effect:** merge legality and the interior two-pole exhibit are unchanged.
The shared budget and all numerical books using it are conditional on
Section 7, and any root census is additionally pending the root-aware engine
rerun.

## 6. `ladder/SHEET6-H3.md`

### Lines 33--64: proof anatomy scope

Change “assume some `M_F=1`” to “assume `M_F=1` at a nonroot starting
vertex.”  Add after the anatomy: “For `F=(0,y)`, `n=0` and the proof does
not start.”  The observation that the Bezout computation for `M>=2` is
absorbed by case-IV condition (m) remains useful, but it is not a root
extension of Proposition 8.4.

### Lines 143--153 and 181--204: `psi` theorem dependency

Replace the claim that the printed Corollary 7.1 directly proves the budget
by the first-separation/cluster repair, and label H3q conditional until
`(22-cl)` clears review.  The chart transport, definition
`psi=ceil(R)-1`, and pointwise arithmetic are unchanged.

### Lines 214--221 and 292--299: remove a nonexistent root constraint

Replace “Prop 8.4 at the root -- all satisfiable” and
“`M_(0,y)!=1` (Prop 8.4) satisfiable” by:

> Corrected Proposition 8.4 imposes no condition at the root.  Repaired
> Statement 8.5 supplies only divisibility from the last nonroot vertex;
> root `M=1` is allowed.  Hence this compatibility check is automatic.

At the trust-perimeter paragraph (lines 371--374), add the repaired Section
7 cluster identity and first-separation exit lemma as explicit dependencies.

**Effect:** the negative result “blanket H3 is false” is strengthened.  The
`psi` kill arithmetic is unchanged, but its global budget status is
conditional rather than “printed-statement solid.”

## 7. `ladder/SHEET6-HIII-REVIEW.md`

### Lines 38--43: global budget proof

The membership facts from the Proposition 8.4 descent are usable only for
nonroot sequence vertices, and the printed `Y` proof double-counts.  Replace
the paragraph by the disjoint first-separation exit-set argument and mark it
conditional on `(22-cl)`.

### Lines 81--89: root compatibility

Replace “root M free ... so Prop 8.4 satisfiable” and the purported
`M>=2` Bezout run by:

> Root `M` is not constrained by corrected Proposition 8.4.  Statement
> 8.5 divisibility and case-IV (m) are the only relevant constraints.

### Lines 230--259 and 310--317: SF1 census is not exhaustive

The reported `28 -> 2 -> 1` scan discarded `M=1` before recognizing a
root signature, both in the common engine and in the scan itself.  Replace
“CONFIRMED REAL ... 28 -> 2 -> 1” and “sanctioned SF1 = 0” by:

> The existence of case-I root termination is confirmed, but the numerical
> SF1 census is a lower bound pending a root-aware rerun.  The prior engine
> retained only root-signature children with `M>=2`; root-signature `M=1`
> children were wrongly killed by Proposition 8.4.

At lines 286--312 replace “H3q (proved from printed statements)” by
“H3q conditional on the repaired Section 7 budget.”

**Effect:** the old exhaustive SF1 counts and the composed “td=6 sanctioned
residual 0” engine verdict are invalid as exhaustive enumerations.  They can
only broaden on rerun.  The independently reviewed `td<=5` theorem is not
invalidated.

## 8. `ladder/SHEET6-REVIEW.md`

This is a historical review and should retain its dated verdict, but it
needs a correction box rather than silent rewriting.

### Lines 64--70

Current:

> Prop 8.4 itself (if it applies to `(0,y)` at all) forces `M != 1` ...
> No element has `M=1`.

Replace by:

> The terminal statement permits “some `M in N`.”  Corrected Proposition
> 8.4 does not apply at `(0,y)`, so it proves neither `M=1` nor `M!=1`.
> Therefore the dichotomy asserted in Statement 9.12 is not derived; a
> terminal with root `M>=2` remains permitted by the listed Q-data.

### Lines 154--164

Qualify “`k>0 => l=0` via Statement 8.2” to the solved nonroot `mu=2`
branches.  Do not state it as a general IIa theorem or a root theorem.

**Effect:** historical conclusion G2 (“printed proof incomplete”) remains,
on a cleaner ground.  No modern census should be sourced from this file.

## 9. `ladder/SHEET6-MULTIPOLE.md`

### Lines 18--20, 44, 46, and 84: exact MP2/MP3 scope

At line 20 replace “on the shared suffix at and below ... `M_F!=1` there”
by “at every **nonroot** vertex of the shared suffix at and below `G*`.”

Replace MP2 by:

> **MP2 (restored nonroot kill).** If `G* != (0,y)`, then `M_F != 1`
> for every `F in U \ {(0,y)}` with `F <= G*` (the nonroot trunk and
> `G*` itself).

Replace MP3 by:

> Among nonroot vertices, the vertices escaping MP2 are exactly
> `{F in U:F>G*}`.  Separately, `(0,y)` is outside corrected Proposition
> 8.4 and has no `M!=1` constraint.

In D3 (line 84), begin “Take a **nonroot** `F<=G*`” and end “conversely all
nonroot `F<=G*` are killed.”

**Effect:** MP2/MP3 need a theorem-statement repair, but every interior-meet
application (including `M_G*=1` contradictions) is unchanged.  Root `M=1`
is newly admitted; the root-meet residual was already meant to remain open.

### Lines 32, 61, 99, 115, 128, 136--137, and 169: MP8 demotion

Replace literal `Y(F)`/equation (22) by first-separation EXIT sets and
`(22-cl)`.  Until Section 7 closes, change MP8 from theorem to conditional
lemma.  In particular, the strong sentence “no refinement or re-partition
... can charge” and Theorem O's use of “Combined with MP8” are not presently
promotable.  The local facts `lambda_F=0` for a specifically identified exit
set and the exact jump-cell ODE witness remain valid.

**Effect:** MP8 and the global “maximal printed-tier” budget claim are
demoted pending Section 7; MP0--MP7 local structure and the explicit
resonant witness survive.

### Line 96: root use of Statement 8.2

Replace “top-cancellation of (iv) (St 8.2's proof computation)” by a direct
top-degree comparison in the reduced identity (iv) at `u=0`.  Do not cite
Statement 8.2 at the root.  The formula `k_f=(r+l)l_f` is unchanged if that
direct comparison is included.

### Lines 65 and 102: wrong td=6 root-meet ground

Replace “empty at td=6 by reach (2POLE phase 3)” with the corrected ground
already isolated in MP-REVIEW section 2c: Proposition 9.3(d) at child
`(nu,kappa-bar)=(1,1)` forces `kappa-bar_parent<nu_parent` on both parents;
the corrected M=1/zero-charge reach census has no such td=6 parent.  State
that the old phase-3 menu omitted `l>=1` and is not evidence.

**Effect:** td=6 root-meet conclusion unchanged after a corrected AWS rerun;
the proof/enumerator must change.  General `td` root meets remain open.

## 10. `ladder/SHEET6-2POLE.md`

### Lines 20 and 278--286: root-merge proof/enumerator

Replace the headline by:

> Root merges at `td=6` are excluded only by the `kappa-bar<nu` reach
> obstruction after the root menu is augmented by `l>=1`; the old phase-3
> two-ground argument and l-free enumerator are invalid for this family.

Replace phase 3's two listed structural grounds by the corrected
Proposition 9.3(d) parent test.  The `mu=(1,1), l=1` root pattern is locally
ODE-solvable and must be enumerated before applying the reach filter.

### Lines 75--83: shared suffix scope

Replace “on the shared suffix and at `G_m`” by “at every **nonroot** shared
suffix vertex and at a nonroot `G_m`.”  Add: “The root itself is never
killed by corrected Proposition 8.4.”  The pre-merge statement remains
unchanged.

### Lines 120--132 and 390--394: global budget

Replace printed equation (22)/literal Y-disjointness by conditional
`(22-cl)` plus first-separation exits.  Keep “shared suffix counted once” as
the repaired conclusion, not as a theorem of the printed text.

### Lines 134--150: eliminate the stale entry menu

Section 2c currently says both `M_i in {1,2}` are live, while section 2d
correctly pins each row-1 pole to `M_i=gcd(2,3)=1`.  Fold 2d into 2c and
delete the live-`M=2` prose.  This is independent of Proposition 8.4; the
pin is a definition-level equality.  Keep the observation that an entry
`M=1` is not killed in the multipole pre-merge region.

### Lines 21 and 323--335: stale book count

The headline says “3 merge classes / 9 IV classes” although the status and
later promoted record say residue A plus two boundary classes.  Mark the
3+9 list explicitly historical or remove it.  This is pre-existing
bookkeeping, not a new mathematical change.

**Effect:** the interior residue-A witness remains.  The old root phase and
the legacy 3+9 census are invalid as current evidence.  The td=6 root-meet
exclusion is expected to survive the corrected reach rerun; the shared
budget remains conditional on Section 7.

## 11. `ladder/SHEET6-MP-REVIEW.md`

### Lines 40, 52, 128--129, and 284--285: nonroot MP2

Replace “MP0--MP8 stand as printed” by “MP0--MP7 stand after the nonroot
MP2/MP3 scope correction; MP8 is conditional on the Section 7 repair.”
Qualify D3 and the suffix kill as nonroot.  At lines 128--129 say the two
pre-merge segments are the **nonroot** escape set and that the root is a
separate no-constraint endpoint.

### Lines 57, 116--117, 173--181, and 210--215: Section 7

The review currently confirms literal equation (22) “as an equality.”
Reverse that disposition: the literal per-puncture equality is
invalid/unproved; only `(22-cl)` may support MP8 after the outstanding
quotient/weight transport repair.  St 9.4's shared budget is conditional on
first-separation exits and `(22-cl)`.

### Lines 131--152 and 299--304

These lines already correctly identify the missing `l`-family and the
`kappa-bar<nu` replacement ground.  Preserve them and make 2POLE/MULTIPOLE
conform to them; do not weaken this correction.

**Effect:** MP8's theorem-grade status changes to conditional.  The review's
root-menu correction and explicit interior witness remain valid.

## 12. Static engine patch map

### Minimal root-aware rule

Do not infer rootness from `M`.  Introduce one central predicate and one
central disposition function, imported by every enumerator:

```python
def has_root_signature(node):
    return LF(node.nu) == (0, 1) and LF(node.kap) == (0, 1)

def dispose_m1(node, *, certified_nonroot=False):
    if node.M != 1:
        return "KEEP"
    if certified_nonroot:
        return "KILL_NR_M1"
    if has_root_signature(node):
        return "TERMINAL_ROOT_M1"
    return "KILL_NR_M1"  # only when the transition construction certifies nonroot
```

In practice the last branch should require an explicit `certified_nonroot`
assertion rather than infer it from a missing root signature; the Q-signature
is necessary for rootness but the safest engine API makes geometric scope
explicit.  Order is mandatory:

```text
budget test -> root-terminal recognition -> nonroot M=1 kill -> enqueue.
```

Pole-entry filters pass `certified_nonroot=True`.  A root terminal is
recorded and not enqueued as an ordinary continuation.

### `cases/sheet6_campaign.py`

- Lines 14--19 and 359--361: qualify all M1 kills as nonroot.
- Lines 330 and 334: the abstract `KILL_M1` shortcuts occur before a child
  exists, so they cannot distinguish a root.  Remove the blanket shortcuts.
  Enumerate the `mu=1` single-orbit/root possibility and the `mu=2` case-I
  possibility; retain immediate M1 shortcuts only for branches whose grammar
  forces `nu_F>=2` (IIb and III), hence nonroot.
- Lines 374 and 384: route constructed children through the central
  disposition; add a `root_hits` collection to `bash`.
- Lines 749--755: make the same change in `tdu_bash`.
- Lines 469--487 (`cong_survivors`) are safe because that routine explicitly
  enumerates `nu_F>=2`; update the comment to say why.  Line 600 and all
  pinned singleton-pole entry deaths are safe because poles are nonroot.

**Invalidated output:** every `bash`, `bash5`, `bash6`, `tduniform`, and
downstream composed count that claimed exhaustive root/SF1 coverage.  The
nonroot transition graph and pole-entry counts are unchanged.

### `cases/h3_check.py`

- Lines 87--93: recognize and record a root-signature child before applying
  M1.
- Lines 151--161: the SF1 scanner presently filters `ch.M==1` before its
  `(nu,kappa)=(1,1)` test.  Reverse the order and report M as part of the
  dedup key.
- It also inherits the abstract shortcuts from `sheet6_campaign.step`, so a
  local edit alone is insufficient.

**Invalidated output:** the published 28 root-lookalikes and all deductions
from that number.  The IV `(j)--(m)` arithmetic is unchanged.

### `cases/hiii_compose.py`

- Lines 77--80 in `e5_iii_outcomes` are safe: the loop starts at
  `nu_F=2`, so these are certified nonroot M1 kills.  Clarify the comment.
- Lines 224--232: recognize a root signature before the `child.M==1` filter
  and record `TERMINAL_ROOT_M1`.  It inherits upstream abstract shortcuts.
- Pole-entry deaths at lines 301--326 are safe.

**Invalidated output:** the composed SF1 `28 -> 2 -> 1` census and the
exhaustive “single-pole td6 residual 0” engine label.  Existing nonroot IV
classes and entry deaths are unchanged; the new run may only add root
candidates.

### `cases/twopole_check.py`

- Lines 195--235: `suffix_bash` must accept an explicit `certified_nonroot`
  flag.  Its initial and descendant M1 kills are valid only on an interior
  suffix.  Recognize root-signature descendants first.
- Lines 238--273: the root menu is l-free (`dq=k+2`) and omits the family
  exposed by MP-REVIEW.  Add `l>=1`, in particular the all-`mu=1` root
  pattern `dp=2`, `dq=2+l`, before the parent `kappa<nu` reach test.
- Lines 348--375: `l1_stage` kills `ch.M==1` before distinguishing root
  from interior, and then labels every `nu=1` cell ODE-dead.  Split by root
  signature first.  The nonroot L1b ODE death remains; at the root, even
  `l` is log-obstructed while odd `l` (including the exact locally solvable
  `l=1` cell) must reach the parent filter.

**Invalidated output:** phase 3's “0 root merges” as produced by the old
menu, and any phase-4 count treating all `nu=1` merge cells as nonroot.
The interior residue-A result is unchanged.  The corrected td6 root result
must be regenerated; MP-REVIEW predicts zero via parent `kappa<nu`, not via
the old menu.

### `cases/monodromy_td.py`

Line 515's singleton-pole `b=1` entry filter is safe: it acts only on pole
vertices.  Change the docstring to “corrected nonroot Proposition 8.4 at a
singleton pole entry”; no logic or census changes.

No other Python `Prop 8.4`/`M==1` consumer was found under `cases/` by the
static search recorded in this audit.

## 13. Safe smoke tests before any full rerun

These are small unit tests, safe locally; the full enumerations remain AWS
work.

1. `Node(...,nu=1,M=1,kap=1,...)` with no nonroot certificate returns
   `TERMINAL_ROOT_M1`, never `KILL_NR_M1`.
2. The same M1 node with a certified nonroot transition returns
   `KILL_NR_M1`.
3. A pinned singleton pole with `M=1` is killed even if some numeric fields
   resemble an axis signature; pole metadata is the nonroot certificate.
4. In every BFS, insert a synthetic root-signature M1 child and assert it
   enters `root_hits` before the M-filter.  Assert an ordinary nonroot M1
   child is still pruned.
5. Exercise the formerly shortcut `mu=2` case-I path and assert a root
   candidate can be emitted.  IIb/III M1 paths with `nu_F>=2` must remain
   pruned.
6. `twopole_check.root_merges` must enumerate `(mu_1,mu_2,l)=(1,1,1)` with
   `(dp,dq)=(2,3)` before reach filtering.  A unit fixture with parent
   `kappa<nu` should reach the filter; a td6 row-1 fixture should fail the
   parent-reach condition, not a searrow/l-free assertion.
7. Static assertion: no `child.M == 1: continue` remains outside the central
   disposition helper; explicit `MF<2` sites must carry a `nu_F>=2` or
   certified-nonroot assertion.

After these pass, run the corrected single-pole/SF1 and two-pole root jobs on
AWS.  Compare old vs new output in three disjoint columns: `nonroot` (must be
byte-identical), `old root M>=2` (must be reproduced), and `new root M=1`
(the only permitted broadening).

## 14. Verdict-impact ledger

| prior result | disposition after this audit |
|---|---|
| Pinned `M=1` pole-entry kills, including prime-td TDU and rows 1/5/7/10 | **UNCHANGED**; poles are nonroot. |
| Corrected Section 9 theorem `td>=6` | **CONDITIONAL BUT NOT ROOT-INVALIDATED**; its M1 kills are nonroot pole/transition kills, but its budget awaits Section 7. |
| AF3 four terminal classes | **UNCHANGED / BROADENED ROOT M-MENU**; allow divisor 1. |
| TDU `td=9` zero-charge negative | **UNCHANGED / STRONGER**; allow root M=1. |
| H3 blanket-root-kill refutation | **UNCHANGED / STRONGER**. |
| H3q psi budgets and every shared `Sigma lambda` book | **DEMOTED TO CONDITIONAL** pending `(22-cl)`. |
| HIII/SF1 numerical censuses | **INVALID AS EXHAUSTIVE; MAY BROADEN** after root-aware rerun. |
| MP2/MP3 | **PROOF-SCOPE REPAIR**: nonroot suffix only; interior consequences unchanged. |
| MP8/global “no budget can charge” theorem | **DEMOTED TO CONDITIONAL** pending Section 7. |
| Two-pole interior residue-A witness | **UNCHANGED**. |
| Two-pole phase-3 “0 root merges” old computation | **INVALID EVIDENCE; RERUN REQUIRED** with l-family.  Expected conclusion unchanged via `kappa<nu`. |
| `td=6` exclusion | **STILL NOT PROVED**; no correction here closes rows 8/9 or the two-pole sector. |

## 15. Recommended patch order

1. Repair and re-review Section 7 (`tau_(i,a)`, EW2 orbit bridge, corrected
   `kappa` transport).  Do not promote any global budget before it passes.
2. Centralize root/nonroot M1 disposition in the engines; run the seven
   local smoke tests.
3. Correct the two-pole root menu and rerun root/SF1 jobs on AWS.
4. Patch the canonical prose in this order: CAMPAIGN, MULTIPOLE, 2POLE,
   AF3/TDU/H3/HIII, then the historical reviews with explicit correction
   boxes.  This avoids duplicating obsolete H2 language.
5. Publish one new checksumed census separating nonroot, root-M>=2, and
   root-M=1 outcomes; only then restate an exhaustive terminal ledger.
