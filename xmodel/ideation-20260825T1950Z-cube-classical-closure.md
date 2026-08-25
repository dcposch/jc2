# Classical-closure mini-round: where the fractional-power recurrence can still live

Date: 2026-08-25  
Owner: cube trajectory  
Status: **BLIND WHOLE-PORTFOLIO DELTA; FRONTIER-ADMISSION PROPOSAL**

## Independence and trigger

I reread all 46 numbered rows of `APPROACHES.md` and the current gaps in
`PROGRESS.md`.  I did not read any sibling submission for this mini-round.
The trigger is the primary-source routing correction that every fixed
total-degree-12 characteristic-zero Keller envelope is already
counterexample-closed by the Heitmann degree-gcd bound.  Therefore the exact
squarefree `(9,12)` Poisson recurrence through rows 18--12 is a method theorem,
not a live maximum-12 counterexample frontier.

## Main conclusion

The fractional-power recurrence has one credible unbounded-total client:
**a source-valid Newton-corner chart whose common approximate-root core is
closed in the rational function field**.  It does *not* transfer directly to
the broad partial-`y` chart.

For partial `y`-degrees `(9,12)`, the top coefficient identity has the form

```text
P_[y=9] = a h(x)^3 y^9,       Q_[y=12] = b h(x)^4 y^12,
```

so the apparent core is `K=h(x)y^3`.  In the pure `y` filtration this is
composite and its rational Poisson centralizer is generally larger than
`k(K)`.  Extra centralizer terms occur at every relevant level, invalidating
the four-resonance descent proved for the squarefree binary cubic.  Calling
this the same order-one chart would hide the load-bearing hypothesis.

There is, however, a concrete live subfamily.  If the top-`y` vertex is an
actual outer Newton corner and `d=deg_x h`, the refined corner initial core is,
up to a scalar,

```text
K_0 = x^d y^3.
```

When `gcd(d,3)=1`, `K_0-T` is geometrically irreducible and the Laurent/rational
centralizer is `k(K_0)`.  This is exactly the hypothesis needed by the
fractional-power descent.  When `3|d`, the core is a proper power and the
centralizer gate correctly fails.  The `(8,12)` analogue has core `x^d y^4`
and the same admission test is `gcd(d,4)=1`.  These statements apply only when
the named vertex dominates every lower-`y` term for one licensed weight;
partial-`y` bounds alone do not ensure that.

More generally, the right condition is not merely “noncomposite-looking.”
For the exact associated-graded core `K`, one must prove that `K-T` is
geometrically integral, equivalently that `k(K)` is relatively algebraically
closed in `k(x,y)`.  Then

```text
ker({K,-}: k(x,y) -> k(x,y)) = k(K),
```

and the recurrence becomes an associated-graded Hamiltonian-centralizer
argument.  This is the genuine connection between avenues 1/3 (Newton
corners/strip rows) and avenue 29 (Hamiltonian derivations); it is stronger
and more source-honest than importing the strict squarefree formulas verbatim.

## Cheapest decisive frontier-admission gate

Before any large CAS continuation, choose the smallest live unbounded-total
partial-`y` source cell and freeze these inputs:

1. the denominator-free original determinant rows and allowed support;
2. one explicit positive weight for which the proposed `(9,12)` or `(8,12)`
   top vertex is genuinely outer and all lower terms are strictly below it;
3. the resulting common core `K` and the exact source/localizer units;
4. a proof or exact certificate that `K-T` is geometrically integral;
5. the first two associated-graded bracket rows, both directly and through the
   proposed fractional-power formula.

The smallest useful test is the monomial-corner chart with
`gcd(deg_x h,3)=1` for B9, followed by the analogous odd-degree B8 chart.  A
tiny AWS exact replay may check the original rows after the chart is admitted,
but no heavy job should launch before items 1--4 are recorded.

**Pass condition.**  The original-row replay agrees with the recurrence, the
completed root exists in the declared filtered localization, and the only
rational centralizer terms are the expected powers of that root.

**Immediate stop conditions.**  Stop the transfer if any of the following
occurs: the proposed corner is not outer; `K-T` factors geometrically; a
centralizer generator outside `k(K)` appears; the root requires an unlicensed
denominator or loses the original source/localizer; or the direct determinant
row disagrees with the recurrence.  A composite-core failure is a theorem
about that chart, not a reason to add more Groebner bands.

If the gate passes, the next bounded experiment is only three descending
bands.  Success means a strict reduction in source variables or a new exact
divisibility allocation; unchanged dimension for three bands is the stop rule.
Only then should a general row generator be built.

## Ranked bets after the 46-row scan

1. **Newton-corner/FT2 admission (avenues 1, 3, 29).**  This is the strongest
   new method connection.  It can compress a named unbounded-total GGV corner
   or top-`y` outer-corner family without asserting a total-degree ceiling.
2. **Existing source-horizontal maximum-12 boundary work (avenues 2, 4, 31).**
   The Q8 selected leaf is already excluded, but the full coefficient-infinity
   and nonselected boundary cover remains live.  FT2 may help only after one
   of those boundary valuations supplies the admitted core; projected/Q8 data
   alone are insufficient.
3. **TD6 source-DAG valuation as an independent control (avenues 2--4).**  Test
   its actual associated-graded core against the centralizer criterion.  A
   composite or nonclosed core is a useful negative control; do not force the
   cubic recurrence onto a differently typed topological-degree chart.
4. **Support-growing Artin--Schreier tower (avenues 19--21).**  This remains
   unbounded-total, but characteristic three makes the `1/3` binomial
   recurrence nonintegral and Frobenius enlarges the special-fibre
   centralizer.  Its current value is finite-death/Kuranishi mechanism and
   conductor growth, not a direct FT2 client.  A tame-prime integral chart
   would be required before reranking it.
5. **Formal-germ acceleration (avenue 4).**  Once a source chart passes the
   centralizer gate, the recurrence can replace repeated coefficient
   Groebner elimination inside a D-series window.  It does not supply the
   missing algebraization, gluing, or cofinality theorem.

The scan gives no positive rank change to the collision ideal/SAT census
(32, 36, 37), passport/group-only routes (25, 26), or the closed/exotic
clusters (5--18, 22--24, 27--30, 33--46).  Root-allocation conditions such as
`K|CW` may later feed monodromy bookkeeping, but presently they are local
divisor choices, not a global block-system theorem.

## Allocation and global-wall impact

Stop all new expensive work whose sole client is a fixed-total-D12 B8/B9 or
strict `(9,12)` binary-cubic family.  Preserve those artifacts as compiler,
finite-death, and recurrence controls.  A reasonable next allocation is

```text
general max12/Q8 source boundary      35%
TD6 source-complete cover             25%
AS support-growing/unbounded tower    20%
Newton-corner/FT2 admission           15%
global landing/cofinality reserve      5%
```

This moves capacity away from classically closed fixed-cap search without
abandoning the exact mechanisms learned there.  Even a successful FT2 corner
gate closes only a named Newton/source family.  The campaign-wide wall remains
a source-complete landing/cofinality theorem showing that every hypothetical
counterexample enters one of the admitted families; the recurrence does not
create that theorem.

## Firewall

This memo proposes a frontier-admission test.  It does not transfer the
squarefree theorem to all partial-`y` maps, close an unbounded-total family,
validate a p-adic lift, alter the reviewed selected-Q8 exclusion, exclude TD6,
or prove JC2.  No new heavy computation was run locally or remotely for this
memo.
