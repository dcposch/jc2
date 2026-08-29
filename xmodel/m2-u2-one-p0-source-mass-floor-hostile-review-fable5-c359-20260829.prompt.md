You are Fable 5 acting as an independent hostile mathematical referee in the
Plane Jacobian Conjecture campaign. Work only in /Users/dc/code/math/jc2.
Never enter, enumerate, search, read, build, status, modify, or control any
jc2-lean path. Use local files only; no web, AWS, CAS, or heavy computation.

This is a custody-sensitive review on the exact Git basis

  c3598b92598c1596e6c6331f4c877619b432a115

Review from first principles:

  xmodel/m2-u2-one-p0-source-mass-floor-r1-sol56-20260829.md

The producer has full-file SHA-256
`28f9918e18eae42580584afbd98a36418ac98ecabf078c829e20484159baeb3c`.
Its claimed body is the first 8611 bytes, ending after the newline of
`*End of sealed report body.*` and excluding the following blank newline and
final separator. The claimed body SHA-256 is
`42993a409e5ed4d2f4c4bb253e05e6ebf1b0e2f22dbd2eaf80bf71aa076d7f71`.
Recompute the full hash, exact body length, and body hash before reliance.
Explicitly assess whether this body convention is adequately defined.

## Frozen five-source manifest

These are the five mathematical sources pinned by the producer. Verify every
full-file SHA-256 before reading and again immediately before verdict. If any
differs at either check, write `INPUT_MUTATED / INCONCLUSIVE` and make no
promotion. Freeze and cite the actual line ranges you use; do not rely on the
producer's paraphrases.

```text
93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
40104334b5e21d6495f9857a6c13a2877ad0e31a67529c5f23243e7170cfaaaa  ladder/BOOK-OFFAXIS.md
9034a987330f55c00e06689e35d6aac397da74fc129c3685437a155afe2f805d  ladder/SHEET6-TDUNIFORM.md
19fcd0133c72eba01dc4a554638111760a8813231a3b983a752d7d7528f58f82  xmodel/m2-u2-one-p0-semilinear-family-record-r1-sol56-20260829.md
4dde1c471b04d88db466293bc197c78529bc16743cc7ccde176e594bceb622dc  xmodel/m2-u2-one-p0-semilinear-family-record-r1-correction-sol56-20260829.md
```

Do not use any prior review or campaign verdict as a proof oracle. The only
mathematical charge basis is the exact five files above. You may use bounded
integer/rational desk arithmetic solely as a bug finder.

## Required hostile review

Attack every producer checklist item in Section 5 and every implication used
by ASM, NM, and U2F.

1. Reconstruct MP0/MP1 orientation exactly. Edges are `F -> F^o`, the root
   `(0,y)` is below, poles are leaves above, and arrivals at a merge `G` are
   vertices `H=G+c` above it. Define precisely the component `U_H`, descendant
   pole leaves, and in-degree `r(G)`. Decide whether every actual labelled U2
   arrival is an MP0-tree edge to which Statement 8.4 applies.

2. Prove or refute: a finite incoming component with one pole leaf contains no
   MP0 merge. Then separately prove or refute the stronger statement actually
   needed by the producer: every child on its pole-to-H path lies outside
   `V_{2,a}`. Do not conflate `r(G)=1` / Notation-9.2 regularity with
   `G notin V_{2,a}`. Charge `SHEET6-MULTIPOLE.md` MP0/MP1 and D1/D2 directly.

3. Read Statement 8.5 exactly as recorded at `BOOK-OFFAXIS.md:100-132`:
   `F in T_a^downarrow cap V_a`, `G=F^o`, **`G notin V_{2,a}`** implies
   `M_G | M_F`. Compare this with the same file's dirty regular `V_{2,a}`
   chain vertices at `:276-309` and the retracted td-7 M-descent at
   `:370-389`. Determine whether “merge-free” alone composes Statement 8.5 to
   `M_H | M_P=b_P`, or whether a V2 escape is an unpriced break. The producer
   may use `mu | M_H` from Statement 8.4 only at its exact orientation.

4. Conditional on `mu | b_P`, independently check both pole cases
   `nu_P | alpha` and `nu_P | beta` using the exact TDUNIFORM R1-R4 formulas.
   Then derive the strongest pole-mass lower bound that survives if
   `M_H | b_P` is not available. Use MP5 carefully: for a unique-leaf branch
   with arrival multiplicity 3, does a `b_P=1` pole necessarily arrive with
   multiplicity 1, forcing `b_P>=2`? Distinguish the general ASM claim from
   this corrected family's special `mu=3` data.

5. Prove or refute disjointness in NM: the `r` incoming subtrees of the inner
   merge and the `R-1` other incoming subtrees of the outer merge must have
   pairwise disjoint pole-leaf sets in the exact rooted-tree orientation.
   Check whether an intervening P0 vertex, an adjacent merge edge, a shared
   suffix, or nested merges changes that statement. Never sum a leaf twice.

6. Read both family artifacts completely. After applying the correction
   `inner_u2.dq: 4 -> 3`, identify exactly what remains fixed:
   inner arity and both arrival multiplicities; outer arity and arrival
   multiplicities, including the unused/symmetric sibling; the roles of
   `l=3`, `h=3`, `r=2`, `R=2`; and what source landing remains unproved.
   Decide whether the producer underuses or overstates any fixed multiplicity.

7. Try hard to construct an actual typed counterexample with `td<=14` to ASM
   or U2F. At minimum test the source-interface skeleton suggested by the
   pinned formulas: global type `(alpha,beta)=(2,3)`, three pole leaves with
   `(a,b,nu)=(1,2,3)`, so each has `Lambda=4`, `M_P=2`, total `td=12`; two
   nested binary merges; each relevant arrival has `mu=3`, `M_H=3`; and a
   regular `V_{2,a}` escape between each pole and arrival so Statement 8.5 is
   inapplicable. Check every charged-source hypothesis, MP1 merge count,
   Statement 8.4, N1/pole arithmetic, weights/full indices, and family labels.
   If this is only an abstract typed ledger rather than realized actual
   vertices, say exactly which realization/transport datum is missing. Do not
   call it an actual counterexample unless every demanded field is supplied.

8. Independently minimize the safe numerical consequence. If ASM fails, test
   candidates such as the purely topological `td>=3*beta` and the stronger
   corrected-family bound obtainable from `mu=3`, MP5, and `b_P>=2`, e.g.
   `td>=3*max(beta,2*alpha)`. Prove any replacement before stating it, find its
   minimum over coprime `2<=alpha<beta`, and say exactly which panels it
   excludes. Do not retain `td>=15` by plausibility.

9. Audit the producer's compiler recommendation. State whether ASM can be
   attached to every merge arrival, only to arrivals with a certified
   edgewise Statement-8.5 chain / direct `M_H|b_P` certificate, or not at all.
   Give the weakest primary verdict among `PASS`, `PASS_WITH_REPAIR`, `FAIL`,
   and `INCONCLUSIVE`, and the maximum safe promotion. A missing load-bearing
   theorem is not a wording repair.

## Output and custody contract

Include:

- Fable 5/model/invocation disclosure and exact Git basis;
- target full-file and body-seal recomputation;
- a complete pre/post table for all five frozen sources;
- exact line citations for every charged source passage;
- itemized verdicts for all nine attacks above;
- a fully typed `td<=14` counterexample attempt and an honest actual-vs-formal
  classification;
- the strongest replacement lemma actually proved, or an exact statement of
  why no replacement is justified;
- maximum safe promotion and explicit exclusions.

Do not include a `charge_basis=` line; this is not an exit-charge report. Do
not edit the producer, any source, canonical file, code, prompt, log, run
record, `pilot-local.log`, or any file except the exact report below. Do not
commit or push. Write the report exactly to:

  xmodel/m2-u2-one-p0-source-mass-floor-hostile-review-fable5-c359-20260829.md

Seal the report by defining its body as all bytes before the literal
`## Seal` heading and recording the exact body byte count and SHA-256.
