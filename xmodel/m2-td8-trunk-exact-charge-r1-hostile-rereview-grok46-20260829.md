# Independent hostile rereview: td=8 trunk exit-set charge

Reviewer: Grok 4.6, different-model adversarial pass. Date: 2026-08-29 UTC.
Target only: `xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md`.
No other live reviewer of this target was opened. No web, AWS, CAS, heavy
local computation, canonical edit, source-packet edit, prompt edit, adapter
edit, target edit, commit, push, or any access to `jc2-lean`.

## 0. Verdict

**`PASS_WITH_REPAIR`.**

Theorem `TD8-TRUNK-EXIT-GE3` is true on the reviewed affine equal-join
family. The old per-ray trunk value `2` is a correct selected-ray
calculation and is not a first-exit-set calculation. Every cv flag in the
multiplicity-`2i` extra direction has actual weight at least `2`, and the
exit set cannot consist of a single weight-`2` flag: the unsplit case forces
a denominator jump and total weight at least `3`; every genuine split
produces at least two distinct flags and total weight at least `4`. The
displayed `tau=8`, `2i -> i` profile is of the second kind.

The global budget `2+2+3+1=8 > td-1=7` then kills the entire affine family
for every `t>=0`. This is an arity/additivity obstruction, not a new
coefficient computation.

The repairs below are citation and consumer-conformity, not a hole in the
inequality. No countermodel restoring trunk exit charge `2` on this family
was found. The first-exit quotient/orbit caveat does not supply one.

## 1. Custody and reconstruction perimeter

Target hashes recomputed on this host before any mathematical use:

```text
full  3c2c9a7ed79cc6d05ec3ba7098c1dc89cabb3547791d777c4bf8971d1ae28e39  MATCH
body  688dbf41e3e3b6c777ec7267c8114569c4507261eb6dea9003dc6236c330494c  MATCH
      (all bytes before the target's separator line `---\nReport-body SHA-256`)
```

Pinned dependencies, full SHA-256 recomputed on this host, all match the
target's §1 list:

```text
910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4
  xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-fable5-20260829.md
e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61
  xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-hostile-review-opus5-20260829.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508
  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370
  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad
  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

The first-exit caveat charged below is the already-written different-model
review of the multipole partition, used only as the stated attack, not as
a dependency of the theorem:

```text
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
  (producer; opened only to locate the caveat)
```

and its hostile review `xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md`.

Printed source re-read on-page from `refs/sigray_full.pdf` (printed page =
PDF page): Definitions 3.1--3.4 and Statements 3.3, 3.9--3.18, Proposition
3.1 (pp. 10--18); Notation 6.1, Statements 6.1--6.2, Theorem 6.1 (pp. 28--32);
Notation 7.1, Statements 7.1--7.3, Propositions 7.3--7.5, Corollary 7.1
(pp. 34--39); Notation 9.1, Statements 9.3--9.4 (pp. 48--49). Desk
arithmetic only: the two gaps, the integrality implication `3q/2 in N* =>
q` even, and `2+2+3+1=8`. Reconstruction is from those printed clauses and
the hash-pinned reviews of the listed packets, not from agreement with the
target.

## 2. Charge ledger

| # | Charge | Finding |
|---|---|---|
| 1 | St 7.3 existence/uniqueness on every ray of the `2i` extra direction; tree non-remerging after a split | **CONFIRMED**, citation repair |
| 2 | Corrected St 9.3 on every descendant flag (cyclic-orbit, quotient, same-fibre, full-multiplicity); each weight `>= ceil(3/2)=2` | **CONFIRMED** |
| 3 | First-separation ownership/additivity; C7.1* fallback; first-exit quotient/orbit caveat | **CONFIRMED**; caveat discharged; writeup must say so |
| 4 | Single-flag case: uniqueness `=> N=2i` until cv, `tau_0=17/2`; `q` integral; `3q/2` integral `=> q>=2` even, total `>=3` | **CONFIRMED** |
| 5 | Multi-flag case and the old `tau=8`, `2i->i` profile: cost `>=4`, or a legitimate share/discard | **CONFIRMED** cost `>=4`; no legitimate share/discard |
| 6 | Pairwise distinctness of two A-exits, selected trunk flags, and the x-side unit; ceiling `td-1=7`; `2+2+3+1=8` kills every `t` | **CONFIRMED** |
| 7 | Theorem truth vs terminology/consumer repairs vs any broader td8 / ceiling / source / JC2 claim | **SEPARATED** as required |

Headline classification of the target: **`PASS_WITH_REPAIR`**.

## 3. Charge 1 — existence, uniqueness, non-remerging

**Existence.** Statement 7.3: if `I_P(u) in T_a^%`, some later `I_P(v)` is
in `T_{a,cv}`. Notation 6.1 partitions `T_a^+` into `T_a^%` and `T_a^&`.
Statement 6.2: the child `F+c` is down iff `d_F < (1-pi(F)) mult(p_F,c)`,
equivalently (Prop. 6.1 excludes equality) the extra child is up iff
`D_F/mult(p_F,c_*) > kbar_F`. Frozen trunk data give `D_F=17i`,
`mult=2i`, `kbar_F=7`, so `17/2 > 7`. The extra child `G=F*c_*` is
therefore in `T_a^%`. Every series in `B_*` passes through `G` (Prop. 3.1
and St 3.9(i)), so St 7.3 supplies a cv flag on that ray.

After `pi>1`, the down test is empty on `T_a^+`: `(1-pi)deg(p)<0` while
`d>0`, so `T_a^& cap T_a^+ cap {pi>1}=empty`. The extra direction cannot
later spawn a pole once it has crossed `pi=1`.

**Uniqueness per ray.** Statement 3.13: on each ray there is a unique `u`
with `d_{I_P(u)}=0`. Notation 7.1 puts `T_{a,cv}` inside `T_a^0`. Hence at
most one cv flag per ray. The target's phrase "uniqueness of the zero of
`d_{I_P(u)}`" is exactly St 3.13 and must be cited.

**Non-remerging.** Definition 3.3: `(P,u)~(P*,u*)` iff `u=u*` and
`u <= O(P,P*)`. If two series split at contact `v=O(P,P*)`, then for every
`w>v` the flags `I_P(w)` and `I_{P*}(w)` are distinct. A later
identification would require some `w>v` with `w <= O`, hence `O>=w>v`,
contradicting the definition of `O`. This is the tree law of `T_a` itself,
not an ambient lemma about the multipole down-vertex set `U`. The target's
slogan "divergent directions never remerge" is true, but it is Def. 3.3
and must be cited as such (R1).

Cyclic conjugates are already one geometric direction: St 3.16 writes
`p_F(eta)=eta^l p̃(eta^{nu})`, and St 3.18 supplies a unique `nu`-th
rotation for which `F*c` exists. The extra reduced factor
`(eta^{17}-B)^2` is one orbit, one child.

## 4. Charge 2 — corrected Statement 9.3 on every descendant

Corrected Statement 9.3, `c_* != 0` (Section 9 audit (4.1); printed (24)
has the wrong sign):

```text
w_H := kappa_H(pi(H)-1)  >=  D_F/mult(p_F,c_*) - kbar_F.
```

Right-hand side at the trunk: `17i/(2i)-7=3/2`. The printed proof uses
one Puiseux ray through the up-child `G=F+c_*` together with
`kappa_H >= kappa_F` and St 3.11. Any later split of that ray only
decreases `N`, so the height needed to drive `d` to `0` is at least
`D_F/mult`; the inequality on a descendant is the same, and is strict if
`N` actually drops.

Typing, independently:

- **Cyclic-orbit.** One extra orbit, one `c_*` up to St 3.18. Conjugates
  are not extra summands.
- **Quotient.** `T_a` is already the contact quotient of Def. 3.3. Distinct
  later contacts give distinct points of `T_a`.
- **Same-fibre.** All flags live on the prescribed fibre `f=a`. C7.1*
  is every-fibre and applies to that fibre.
- **Full-multiplicity.** The right-hand side is computed at `F` with
  `mult(p_F,c_*)=2i`, the full extra-direction count. A later local
  multiplicity `i` does not weaken the inequality at `F`.

Integrality: `w_H in N*`. Independently, Prop. 7.3's geometric perturbation
produces a simple nearby place `Q` with `Lambda(Q)=kappa(pi-1)`, and
`Lambda` is a positive integer by the printed formula (18). Statement 3.14
preserves `eta`, hence `kappa` and `pi`, so this is `w_H` for every cv
flag, not only the simple ones. This is the pinned exact-lambda
integrality upgrade, re-derived here from the printed proof, not taken on
trust. Combined with the gap `3/2`, every distinct descendant flag has
`w_H >= 2 = ceil(3/2)`.

## 5. Charge 3 — ownership, additivity, caveat, fallback

**Ownership.** Let `C` be the y-side characteristic path of either pole,
which contains the trunk `F`. The extra child `G=F*c_*` is not the
characteristic continuation (that continuation is the reduced
multiplicity-three orbit). Every flag of a series in `B_*` has first
separation from `C` at `F`. Later splits of `B_*` remain in the component
of `T_a \ C` attached along `G`. Def. 3.3 forbids re-entry. Those flags
are exactly the first-separation set `E_F(c_*)` in the Section 9 repair
(4.2). None may be discarded because both subgroups started at the same
reduced root orbit.

**Additivity.** C7.1* (pinned Section 7 repair, Terra PASS on the amended
hash) applies to any pairwise-distinct subset of `T_{a,cv}` on a
prescribed fibre. Summing `w_H` over the set `E_F(c_*)` is therefore
legal once distinctness is Def. 3.3. Literal nested `Y(F)` is not used.

**Fallback, stronger and cleaner.** Even if the local-charge name
`lambda_F^exit` were withdrawn, C7.1* still counts the same flags
directly. The route kill in the target's §4 is already this fallback: it
selects distinct cv flags and applies C7.1*, not a nested `Y(F)` sum.
The local-charge language is optional packaging.

**First-exit quotient/orbit caveat, confronted.** The global first-exit
review's blocker is the jump from MP0's finite tree of **down-vertex pole
paths** `U` to the orbit object that contains selected cv flags. Its
abstract countermodel identifies two later cv representatives `H_1,H_2`,
coming from two local directions at a vertex of `U`, as one quotient flag
`H`, so a local price `2` collapses to one C7.1* term. That blocker is
real for MFE. It is not a blocker here.

This argument never uses `U` or MFE. It works in `T_a` as defined by
Def. 3.3. The selected flags are a finite explicit set: the A-exit
witnesses, the trunk-exit witnesses, and the x-side witness. Distinctness
is Def. 3.3 plus Statement 3.3 (two components).

If, contrary to Def. 3.3, two later trunk flags were identified as one
`H`, the situation would move from Case A (`r>=2`) to Case B (`r=1`).
Case B still yields total weight at least `3` (Charge 4). The caveat
therefore cannot restore trunk exit charge `2`. Moreover Def. 3.3 forbids
the identification unless the series agree through `pi(H)`, which is
precisely Case B and not a split. The abstract MFE countermodel is not
realized by the Eggers--Wall object on which this theorem lives.

The target listed the ownership question as a review risk and did not
write this discharge. That is the writeup repair (R2), not a mathematical
gap.

## 6. Charge 4 — single-flag case

Assume `E_F(c_*)={H}`. Then every `P in B_*` has `H(P)=H`, so
`pi(H) <= O(P,P')` for all pairs, by Def. 3.3. There is no split strictly
below `pi(H)`. Proposition 3.1(*) / St 3.9(i) therefore give
`N(tau)=2i` on `(0,tau_0]`.

Area identity, from St 3.10: `omega` is continuous of slope `-N`,
`omega(pi(F))=d_F`, `omega(u_0)=0` by St 3.13. Rescaling
`tau=kappa_F(u-pi(F))` yields `D_F = integral_0^{tau_0} N(tau) d tau`.
Hence `17i = 2i tau_0`, so `tau_0=17/2`.

The exact identity `w_H = q(tau_0 - kbar_F)` is algebra:
`tau_0 - kbar_F = kappa_F(pi(H)-1)`, and `q:=kappa_H/kappa_F`. Thus
`w_H = 3q/2`.

`q in N*` from Notation 3.5: `kappa_F = kappa_P / e_j` on the interval
after the last characteristic exponent `<= pi(F)`. Along a ray, `e_j`
is nonincreasing, so the ratio of two such values is a positive integer.
This is the pinned exact-lambda Theorem A.4, re-derived from the printed
notation. For `c_* != 0`, St 9.3 also gives `kappa_H >= kappa_F`, hence
`q>=1`.

`(INT)` forces `3q/2 in N*`. With `q in N*` this makes `q` even, hence
`q>=2` and `w_H>=3`. The integer rounding `ceil(3/2)=2` is impossible
in the unsplit case: the mechanism that produces an integer from `3/2`
is a denominator jump, which raises the charge to at least `3`.

## 7. Charge 5 — multi-flag case and the old `tau=8` profile

If `r:=|E_F(c_*)|>=2`, Charge 2 gives `sum w_H >= 2r >= 4`.

The pinned exact-lambda Theorem C exhibits one formal profile realizing
per-ray `Delta=2`: `N=2i` on `(0,8]` and `N=i` on `(8,9]`, with
`kappa_H=kappa_F` and `tau_0=9`. That profile is a split of `B_*` into
two groups of size `i` at `tau=8`.

At `tau=8`, remaining `kappa d = 17i-16i=i`, and
`1-pi(F') = kbar_F/kappa_F - 8/kappa_F = -1/kappa_F < 0`, so `pi(F')>1`.
Both children of the split are therefore up (Charge 1). The continuing
group reaches `d=0` at `tau_0=9` with `q=1`, hence weight `2`. The
departing group is still subject to St 9.3 at the original `F`, so its
own `tau_0` is at least `17/2`; it cannot die at `tau=8`. It produces a
second cv flag of weight at least `2`. The two flags are distinct:
their contact is `tau=8`, while each cv height is at least `17/2 > 8`
(Def. 3.3). Total at least `4`. The displayed per-ray value `2` occurs
twice; it is not a total charge of `2`.

**Share.** Distinct subgroups share a cv flag only if they agree through
`pi(H)`, which by Def. 3.3 means they did not split. That is Case B, not
a discount of Case A.

**Discard.** A subgroup fails to produce a cv flag only if its child is
down, hence poleward. After `pi>1` there is no down child in `T_a^+`.
A third pole would also leave the reviewed two-pole family. Cyclic
conjugacy does not discard a flag: conjugates are one direction (St 3.18)
and, if they remain one flag with a ramification jump, that is Case B
with `q>=2` and charge at least `3`, not a two-flag configuration with a
missing summand.

There is no legitimate way for distinct subgroups to share or discard a
cv flag so as to restore total `2`.

## 8. Charge 6 — global route budget

Frozen A-copy data, independently reproduced from the pinned transport /
exact-lambda chain: `D=14`, extra multiplicity `2`, `kbar=5`, gap
`14/2-5=2`. Choose one cv flag on each A-exit; each has weight at least
`2` by corrected 9.3 plus `(INT)`. The merge has only two chain-arrival
orbits, both down; St 3.18 supplies no extra `c_*`, so merge exit mass is
identically `0`. Choose every flag in `E_F(c_*)`; total at least `3` by
the theorem. The x-side: Theorem 6.1 is `l_f < k_f`, so Statement 9.4's
proof gives an x-component cv flag of integral weight at least `psi=1`.

Pairwise distinctness:

- x-side vs all y-side flags: Statement 3.3, two components of `T_a`.
- A1 vs A2: extra directions leave at distinct vertices `H_1 != H_2`
  (the two rigid `(21,15)` cells). Their rays split already at the merge.
- Either A-exit vs trunk exit: first separation at `H_e` versus at the
  trunk. After the trunk, the characteristic child is the multiplicity-three
  down continuation toward the merge; the extra child is up. Def. 3.3
  keeps those subtrees disjoint.

C7.1* on this distinct set: total actual weight at least `2+2+3+1=8`.
For `td=8` the same theorem says every distinct-cv subset has total
weight at most `td-1=7`. Contradiction. Equivalently, after reserving
the x-side unit, the y-side ceiling is `6`, and `2+2+3=7` already
exceeds it. All displayed ratios are independent of `t`; `i=28(4+3t)>0`
for every integer `t>=0`. The kill is uniform.

## 9. Charge 7 — theorem, terminology, broader claims

**Theorem truth.** On every member of the reviewed affine equal-join
family, the trunk extra-direction exit set has total actual weight at
least `3`. Consequently that formal route is excluded at the
actual-weight budget tier, for every `t>=0`.

**Terminology.** The name `lambda_F^exit` is the Section 9 difference-set
(4.2), not printed Notation 9.3. The target uses it correctly as a set
of first-separation flags. The budget theorem that consumers must cite
is C7.1* applied to an explicitly distinct finite set. That is already
how the target's §4 is written.

**Consumer repair, not a defect of this theorem.** The pinned exact-lambda
Theorem F asserts survival iff three *per-ray* charges equal `2`. That
consumer step is false for this family: the per-ray trunk criterion
`Delta=2 iff kappa_H=kappa_F` and `tau_0=9` remains valid as a selected-ray
statement (exact-lambda Theorem C, independently re-derived), but as a
budget statement it undercounts the exit set. The displayed `tau=8`
split costs at least `4` in C7.1*. The survival criterion must be
withdrawn and replaced by `ROUTE_KILLED_BY_TRUNK_ARITY`.

**Not proved, and correctly not claimed by the target:** any other `td=8`
route family; a degree ceiling; source landing or realization by a
polynomial pair; a counterexample; JC2; attainment of the bound `3`;
repair of every remaining consumer of literal nested `Y(F)`.

The ratio `B=(4/3)A` is used only to name the extra orbit. The load-bearing
input is reduced multiplicity `2` together with `D_F=17i` and `kbar_F=7`,
which are in the pinned transport/exact-lambda chain. The ratio is not
load-bearing for the arity theorem.

## 10. Precise countermodel test

Sought: a configuration, compatible with the printed tree and the
reviewed D2 combinatorics, in which the trunk extra-direction contributes
total C7.1* weight `2`.

| candidate | why it fails |
|---|---|
| Unsplit extra group, `q=1` | `3/2 not in N*`; forbidden by `(INT)` |
| Unsplit extra group, `q>=2` | Charge `>=3` (Case B) |
| `tau=8` half-drop, count only the continuing ray | Second up-child exists and is a distinct cv flag; total `>=4` |
| Identify the two later flags after cyclic quotient | Either Def. 3.3 forbids it, or it is Case B and total `>=3` |
| Send one subgroup to a new pole | Impossible after `pi>1` on `T_a^+`; also a third pole, not this family |
| Share one cv flag across a split | Requires agreement through `pi(H)`, hence no split |
| Collapse an A-exit into the trunk exit | Distinct first-separation vertices; Def. 3.3 |

No candidate survives. There is no precise countermodel to
`TD8-TRUNK-EXIT-GE3` on this family.

## 11. Required repairs before consumer citation

R1. Cite Definition 3.3 for non-remerging and for distinctness of split
flags; cite Statement 3.13 for uniqueness; cite Statement 6.2 for the
up-test `D_F/mult > kbar_F`; cite Notation 3.5 for `q in N*`; cite
Statement 3.3 for the x-side.

R2. Write the Charge 3 discharge of the first-exit quotient/orbit caveat
in the producer text: the argument lives in `T_a`, not in MP0's `U`;
the abstract identification, if forced, collapses Case A into Case B
and still yields `>=3`.

R3. In every consumer of exact-lambda Theorem F, withdraw "survives iff
three per-ray charges equal `2`" for this family, and replace the trunk
budget summand by the exit-set lower bound `3` (or `4` for the displayed
split profile). Do not treat that consumer repair as a gap in the
present theorem.

No mathematical lemma is missing at the printed-source plus pinned-review
perimeter.

## 12. Maximum safe consequence

```text
ROUTE_KILLED_BY_TRUNK_ARITY
```

for the reviewed affine equal-join `td=8` family, uniformly in every
integer `t>=0`. The exact-lambda per-ray knife-edge is withdrawn for
this family. Nothing else is licensed: not a global `td=8` exclusion,
not a degree ceiling, not source landing, not a polynomial pair, not a
counterexample, not JC2, and not a GREEN promotion of any other route
engine.

---
Report-body SHA-256 (all bytes before the separator line above):
`fdb2a6e6d17b08e521ce0a27d1703e4890586268f7afb684db95d4164897c0ae`.
