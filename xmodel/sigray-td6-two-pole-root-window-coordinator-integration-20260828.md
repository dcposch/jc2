# Two-pole `td=6` root-window closure — coordinator integration — 2026-08-28

## Disposition

**GREEN at the exact scope below.**  The conclusion is not obtained by
applying the interior-meet lemma `L1a` at `(0,y)`.  It is the composition of
the already promoted entry/tree statements `MP1`, `MP4`, and `MP5` (whose
proof `D5` is used only at nonroot pre-merge vertices), the exact row-1 depth
alphabet, and the independently reviewed mixed-multiplicity root-edge
theorem.

The Sol cross-review returned `PROMOTE`.  The Grok hostile review returned
`REPAIR`, correctly rejecting the shorthand “`L1a(b)` at the root” and
identifying the repaired composition below.  The coordinator then checked
that `D5` explicitly assumes `K=H°` is still pre-merge and handles the final
arrival separately with Statement 8.4.  Thus the hostile objection repairs
the citation chain but does not leave a mathematical gap in this scope.

## The theorem (`ROOT-W2`)

In the two-pole `td=6` sector, the two pole chains cannot have a genuine
contact-zero meet at `(0,y)`.

Equivalently, if `m=2`, `td=6`, and the two pole chains meet, their unique
merge is not the root.  This is a root-sector theorem only; it does not
exclude the surviving interior residue-A merge.

## Proof trace

1. The `td=6,m=2` entry pin forces type `(alpha,beta)=(2,3)`,
   `Lambda_1=Lambda_2=3`, and row 1 of table (23) at each pole.  Hence both
   pole entries have `M=1` and initial depth invariant `w_0=2` (`MP4`).
2. `MP1` gives `sum_G(r(G)-1)=m-1=1`.  Therefore there is exactly one
   two-way merge.  If the meet is `(0,y)`, every vertex above it is nonroot
   and strictly pre-merge.
3. Apply `MP5/D5` down each chain.  At every step its lower vertex `K` is
   still nonroot and pre-merge, exactly the stated domain of `D5`; no root
   form of Proposition 8.4 or the interior-meet clause `L1a(c)` is used.
   Each chain remains an `M=1`, single-simple-orbit segment through its last
   nonroot parent.  The reviewed DEPTH recursion gives the exact alphabet
   `W(2)={2}`.  This also covers a zero-length segment, where the pole itself
   is the root parent.  At the arrival, Statement 8.4 gives
   `mu_e | M_{H_e}=1`, hence `mu_e=1`; an actual mixed-multiplicity parent
   therefore does not arise in this sector.
4. Let `H_e` be either actual parent arriving at the root.  The
   mixed-multiplicity root-edge theorem applies edgewise and gives

       X_root = mu_e(1-w_e) = A/B > 0,

   so every actual root parent must satisfy `0<w_e<1`, independently of
   `mu_e`.
5. The same parent has `w_e=2` by step 3.  Contradiction.

The edgewise mixed-root theorem is stronger than is needed here: MP5 already
forces both actual arrivals to be simple.  Its value in this proof is the
case-I inequality `0<w<1`, not an extrapolation of the all-simple degree
formula to a hypothetical all-`mu>=2` root.

## Scope firewall

The theorem does **not** establish any of the following:

- exclusion of the interior residue
  `Q=(6,12,3,2,5)` or its four terminal classes;
- root/SF1 landing completeness or exclusion of a one-pole root signature;
- any `m>=3`, `td!=6`, off-axis, or post-jump `M>=2` sector without its own
  exact incoming alphabet;
- the formulas `A=sum(mu)`, `B=r+l`, `k=0`, or `B>A` for an
  all-`mu>=2` root;
- a polynomial Keller map, a counterexample, or a proof of JC2.

The general reusable rule is only this: a genuine root edge requires
`0<w<1`; an independently certified incoming alphabet contained in
`[1,infinity)` kills that edge.

## Evidence and custody

- mixed-root integration:
  `aaa4d179992c51210eb70a30127c8c32d0856bf11b9b044802bec1746cbcacb0`;
- frozen cross packet:
  `9cc1d824e35abbd9f367f59cc94bfde2f6c93f37a099ee48238211b6bbbec8e9`;
- Sol cross-review:
  `a64a58afca4748cc80e3f5a31d6ec4f72762f3ae7b3926effaf8cc0844424b55`;
- Grok hostile cross-review:
  `13db3c55d308814f90f8e62352e1c3df1cdc5ef42bf24c496b08fcd85d445eb2`.

The canonical dependency passages checked were `SHEET6-MULTIPOLE.md` MP1,
MP4, MP5 and D5; `SHEET6-DEPTH.md` DS2--DS3 and the root-edge correction;
and the historical scope warning in `SHEET6-L1.md`.  No CAS or AWS result is
a premise.  `jc2-lean` was not entered, listed, searched, read, built,
modified, status-checked, or controlled.
