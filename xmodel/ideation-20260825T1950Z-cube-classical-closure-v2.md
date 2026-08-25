# Classical-closure mini-round V2: the genuine unbounded-total approximate-root client

Date: 2026-08-25  
Owner: cube trajectory  
Status: **BLIND WHOLE-PORTFOLIO DELTA; CORRECTED FRONTIER-ADMISSION PROPOSAL**

This is the canonical successor to
`ideation-20260825T1950Z-cube-classical-closure.md` (SHA-256
`744216b5e0027428490aeb4521b172ce3666cb0a9c3c6e36d5ba50dd50102618`).
The parent incorrectly called `h(x)y^3` composite in general.  It is composite
when `h` is a cube (including constant `h` after scalar extension), but it can
be a closed polynomial when `h` is not a cube.  The full-portfolio ranking and
fixed-D12 routing correction survive; the admission gate is broadened and
made exact below.  Do not use the parent's blanket composite-core sentence.

## Independence and trigger

I reread all 46 numbered rows of `APPROACHES.md` and the current gaps in
`PROGRESS.md`, without reading any sibling mini-round submission.  The trigger
is the primary-source correction that every fixed-total-degree-12
characteristic-zero Keller envelope is already counterexample-closed by the
Heitmann degree-gcd bound.  The exact strict `(9,12)` squarefree Poisson
recurrence is therefore a method theorem, not a live counterexample frontier.

## Correct transfer criterion

For unbounded-total partial `y`-degrees `(9,12)`, the top determinant row gives

```text
P_[y=9] = a h(x)^3 y^9,       Q_[y=12] = b h(x)^4 y^12,
```

and the common approximate-root core is `K=h(x)y^3`.  Over a characteristic
zero algebraic closure, the generic fibre

```text
h(x)y^3 = T
```

is geometrically integral precisely when `h` is not a cube in the rational
function field (equivalently, the divisor multiplicities of `h`, together
with `3`, have gcd one).  In that case `k(K)` is relatively algebraically
closed in `k(x,y)` and

```text
ker({K,-}: k(x,y) -> k(x,y)) = k(K).
```

This is the rational-centralizer hypothesis used by the fractional-power
descent.  If `h=g^3`, then `K=(gy)^3`, the centralizer contains `gy`, and the
four-resonance squarefree argument does not transfer.  In particular, the
fixed-total-D12 normalization that makes `h` constant lies in the bad
composite-core case even though its separate binary-total-homogeneous core
was squarefree.

The `(8,12)` analogue has `K=h(x)y^4`.  Its geometric-integrality test is that
`K` is not a proper power: no common divisor greater than one may divide `4`
and every divisor multiplicity of `h`.  Thus square and fourth-power `h`
strata require an enlarged-centralizer treatment, while a primitive stratum
is a legitimate approximate-root client.

A refined Newton corner remains a useful sufficient subcase.  If the
top-`y` vertex is genuinely outer and `d=deg_x h`, its vertex core is
`x^d y^3`, which is closed when `gcd(d,3)=1`; for B8 the corresponding test is
`gcd(d,4)=1`.  Failure of this monomial test does not prove the full
`h(x)y^3` core nonclosed, because lower terms of `h` can destroy the proper
power.  This is why the exact `K-T` test, not degree congruence alone, is the
canonical gate.

The conceptual bridge is now precise: avenues 1/3 provide a source-valid
Newton/partial-`y` filtration and avenues 29/4 provide the associated-graded
Hamiltonian centralizer and triangular formal descent.  The recurrence may
compress a named unbounded-total source family only after all four pieces are
typed together.

## Cheapest source-honest decisive gate

Before any large computation, freeze one smallest live partial-`y` source
cell with:

1. its denominator-free original determinant rows and exact allowed support;
2. the declared `y` or Newton filtration and proof that the bracket is
   homogeneous at the used rows;
3. the common core `K` produced by the top row, with every source/localizer
   unit recorded;
4. an exact factorization/irreducibility certificate for `K-T` over the
   relevant geometric function field;
5. direct original-row and fractional-power forms of the first two lower
   rows.

The cheapest first split is the B9 partial-`y` `h`-stratification:

- **primitive stratum:** `h` is not a cube; test three descending bands;
- **power stratum:** `h=g^3`; record the extra centralizer generator `gy` and
  stop FT2 unless a separate relative-centralizer normal form is specified.

The B8 square/fourth-power split is the next control.  An outer monomial corner
with primitive exponent vector is a convenient small witness, but not a
substitute for checking the actual source core.

**Pass condition.**  `K-T` is geometrically integral, the completed root exists
in the declared filtered localization, the original rows agree with the
recurrence, and no rational centralizer generator outside `k(K)` appears.

**Immediate stop conditions.**  Stop on a nonhomogeneous/unlicensed
filtration, geometrically reducible `K-T`, an extra centralizer generator, an
unlicensed denominator, loss of the original source/localizer, or disagreement
with a direct determinant row.  If three admitted bands do not strictly lower
the source dimension or impose a new exact divisibility allocation, do not
build a full-row generator.

## Whole-portfolio rank and allocation

1. **Partial-`y`/Newton FT2 admission (avenues 1, 3, 29)** is the strongest new
   method connection.  The primitive `h` stratum is a genuinely
   unbounded-total client.
2. **General max12/Q8 source-horizontal boundary (2, 4, 31)** remains the
   leading concrete proof lane.  FT2 may enter only through an actual boundary
   valuation and denominator-cleared source core; the reviewed selected-Q8
   exclusion itself needs no reopening.
3. **TD6 source-DAG valuations (2--4)** are the best independent control for
   whether the centralizer criterion survives a differently typed boundary
   model.
4. **Support-growing Artin--Schreier towers (19--21)** remain unbounded-total,
   but characteristic three makes `1/3` nonintegral and Frobenius enlarges
   special-fibre centralizers.  They remain finite-death/conductor experiments,
   not direct FT2 clients without a tame-prime or generic-fibre interface.
5. **Formal-germ windows (4)** can use an admitted recurrence as an elimination
   accelerator, but retain their algebraization/gluing/cofinality debts.

No positive rank change follows for collision/SAT censuses (32, 36, 37),
passport/group-only routes (25, 26), or the closed/exotic clusters (5--18,
22--24, 27--30, 33--46).  Local root-allocation conditions are not yet global
monodromy blocks.

Recommended allocation remains:

```text
general max12/Q8 source boundary      35%
TD6 source-complete cover             25%
AS support-growing/unbounded tower    20%
partial-y/Newton FT2 admission        15%
global landing/cofinality reserve      5%
```

Stop expensive work whose only client is a fixed-total-D12 B8/B9 box, while
retaining its artifacts as compiler and recurrence controls.  A successful
FT2 gate closes at most one named source family.  The campaign-wide wall is
still a source-complete landing/cofinality theorem.

## Firewall

This is a corrected frontier-admission proposal.  It does not prove the
primitive partial-`y` stratum empty, solve the power stratum, validate a
p-adic lift, alter the selected-Q8 theorem, close TD6, establish cofinality, or
prove JC2.  No heavy computation was run for this memo.
