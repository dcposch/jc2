# M2 finite reduced chain skeleton R1

This desk-scale instrument encodes the finite reduced-state lemma suggested
by the 2026-08-29 peer ideation round.  Conditional on the exact P0 formulas
in `ladder/BOOK-OFFAXIS.md`, it computes the complete set of reduced chain
states `(w,M)` reachable from one fixed state within one fixed numerical
lambda budget without any global search cap.

The key difference from `cases/book_offaxis.py` is that `k`, `lex`, the
numerator of `w`, and `M` are never truncated by constants.  Each one-step
loop bound is derived from

```text
C = l(k+lex)-Sm >= 1,
T = Sm+l-eps(1+k+lex) >= 1,
E = (l-eps)+nu*C,
E | l*num(w)*T,
nu >= 2,
```

and from the remaining lambda budget.  The free-`nu` pure-epsilon family is
quotiented by exact congruence classes of `nu+1`, not sampled.

The script covers P0 chain transitions only.  It does not enumerate merge
cells, prove generic-AP uniformity, build a full landing book, establish
realizability, bound topological degree, or imply JC2.

Run the charged `td=7` post-jump start with:

```sh
python3 cases/m2_finite_reduced_chain_skeleton_r1_20260829/finite_chain_skeleton_r1.py \
  --w 3/2 --M 2 --budget 5 --output /tmp/m2-skeleton.json
```

The resulting JSON records every reduced state, minimum lambda cost, derived
loop-bound maxima, one predecessor, and a hash of the canonical state table.

The charged run completes in under a second with 69 reduced states, maximum
`M=25`, maximum reduced `w` numerator 3, and state-table SHA-256
`c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad`.
It exactly matches the current legacy capped engine's reduced state/cost map;
the prose count “70” in P5 is stale relative to that engine, which returns 69.
Both ordinary and optimized test runs pass 35 fail-closed checks.

`td7_caseiii_special_nu_r1.py` supplies the first downstream-consumer
quotient.  Against the frozen `td=7` chain-1 partner, the neutral odd-`nu_H`
ray at `(w,M)=(3/2,2)` has exactly one case-III ZCH special value:
`nu_H=3`, producing `(dp,dq,M_G)=(5,7,1)` and hence an MP2 kill.  Every odd
`nu_H>=5` is uniformly empty.  The proof reduces the merge equation to
`nu_G*((3nu_H-4)l-2)=3nu_H`; it uses inequalities and divisibility, not an
enumeration cap.
