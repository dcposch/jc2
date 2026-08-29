# Independent theorem hunt: uniform local obstruction behind the upper tail ladder

Act as Grok 4.6, an independent mathematical researcher.  Work in
`/Users/dc/code/math/jc2` on the fixed branch-P upper endpoint fixture for
the plane Jacobian-conjecture campaign.

## Distinct charge

Find a structural theorem that replaces one-cutoff-at-a-time elimination.
The reviewed fixed square-tail endpoint strata at cutoffs 7 and 6 are empty;
the frozen cutoff-5 packet now claims a complete characteristic-zero
field-point exclusion pending different-model review.  Cutoff 4 restores
all raw slots of weight >=4, cutoff 3 additionally restores the ten `tt_*`
coordinates, and cutoff 2 additionally restores the seven `z_*` coordinates
and is exactly the complete fixed 303-variable/513-generator fixture.

Seek the common `A`-adic/rootwise mechanism explaining the observed radical
cascades and, ideally, an induction or finite local classification that
handles cutoffs 4, 3, and 2 simultaneously.

## Exact setting

Use `A=X^4-1`, `H=A^2`, `F0=H^2`, `G0=H^3`, `F1=H`, `c2=0`, and

```text
D_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j').
```

The full reviewed early cascade is

```text
F2=(1+H Z)/4,      deg Z<=6,
F3=(Z+A T)/8,      deg T<=9,
```

with arbitrary later raw F windows and the triangular characteristic
description of G.  The charged endpoint is `D0=...=D21=0, D22=1`, with no
`D23` and no `G22` slot.  The authoritative raw source is
`cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json`,
SHA-256 `ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.

Relevant sources include the reviewed upper-cascade producer/review, the
tail-7/6 reports and reviews, the frozen cutoff-5 producer packet and its
analytic handoff, `CHARACTERISTIC_CROSSCHECK.md`, and the reviewed M-cokernel
and D5N local-naturality reports.  Treat cutoff 5 as provisional until its
current Fable review closes; rederive claims you use.

Explore especially:

* formal `F` square-root / `G` characteristic expansion and its A-adic pole
  orders;
* the four simple roots of A, tagged CRT jets, and whether the endpoint's
  required `g22=(X^5/5-X+c)/(8A^5)` principal parts conflict with earlier
  polynomial-window descent;
* an invariant/core recurrence generalizing the tail-6 and tail-5 branch
  identities;
* how restoring `T mod A` and then `Z` changes the obstruction, with an
  exhaustive factor/gcd stratification rather than unjustified division;
* a proof that some earlier row forces `A|T`, or a precise counterexample to
  that hope;
* a small exact local-jet resultant or linear functional that could be
  compiled independently and reviewed.

Do not normalize endpoint carriers without a complete cover.  Distinguish
field radicals from scheme identities, local values from the global
H-multiple, and projections from actual raw points.  A timeout, modular
point, proper ideal, or partial basis is non-evidence.  Use only light exact
scratch computations; no heavy local CAS and no AWS launch.  Do not enter,
list, search, read, build, status, or modify `jc2-lean`.  Do not edit any
canonical ledger or existing case packet.

## Output

Write exactly one report:

`xmodel/ggv-upper-endpoint-uniform-tail-local-obstruction-grok46-20260828.md`

Use `/tmp` for scratch.  Lead with `EXACT THEOREM`, `EXECUTABLE REDUCTION`,
or `NO ADVANCE`.  Include explicit identities/proofs or a minimal exact
compiler specification, branch coverage, mutation tests, and a ranked next
action.  Make no JC2 or full-family claim beyond what is actually proved.
