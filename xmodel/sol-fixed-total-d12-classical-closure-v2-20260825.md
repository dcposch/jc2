# Provisional routing correction: every fixed-total-D12 envelope is classically counterexample-closed

Date: 2026-08-25  
Status: **PRIMARY-SOURCE CHECKED; HOSTILE SCOPE REVIEW RUNNING**

## Result

Every characteristic-zero coefficient family satisfying
`deg_total(P),deg_total(Q) <= 12` is classically counterexample-closed.  In
particular, neither the broad fixed-D12 B9/B8 envelopes nor their stricter
actual-total-degree `(9,12)` and `(8,12)` subfamilies are live JC2
counterexample strata.

Guccione--Guccione--Valqui work over a characteristic-zero field and define a
counterexample to be a Jacobian pair which is not an automorphism.  Their
paper *On the shape of possible counterexamples to the Jacobian Conjecture*,
arXiv:1401.1784v3, states and proves the Heitmann bound

```text
gcd(deg_total P,deg_total Q) >= 16
```

for every counterexample.  See the abstract and Introduction, pp. 1--2:
<https://arxiv.org/abs/1401.1784> and
<https://arxiv.org/pdf/1401.1784>.

If both total degrees are at most `12`, their gcd is at most `12`, contradicting
the necessary lower bound `16` for a counterexample.  For the strict degree
pairs the gcds are `3` and `4`.  Therefore every characteristic-zero Keller
pair anywhere in a fixed-D12 envelope is an automorphism.  Moh's much stronger
maximum-degree bound would also close these families, but is not needed for
this correction.

The field scope causes no gap for a `Q_3` point or a point over a finite
extension.  The GGV paper begins over an arbitrary characteristic-zero
field.  Equivalently, one may base-extend to an algebraic closure; a
polynomial inverse, if it exists after base extension, is unique and descends.

## Exact campaign scopes

The corrected B9 interface first lands in the finite broad cell

```text
deg_y(P,Q)=(9,12),  deg_total P<=11, deg_total Q<=12.
```

Although its actual total degrees need not be `(9,12)`, this entire broad cell
is closed: both actual total degrees are at most `12`, so their gcd is less
than `16`.  The later normalized common-cubic family and the binary-cubic band
compilers deliberately impose the stricter box

```text
deg_total(P,Q)=(9,12),  P9=a K^3, Q12=b K^4.
```

Those strict computations are source-honest, but they are not a remaining
JC2 frontier.  The analogous strict B8 quartic box has actual total degrees
`(8,12)` and is classically closed for the same reason.  The only potentially
live B9/B8 transfer retains the partial-`y` bounds while dropping every finite
total-degree (equivalently, coefficient-`x`-degree) cap.  The GGV observation
does not close those unbounded-total partial-`y` `(9,12)` or `(8,12)` residue
classes.

## Consequence for the Artin--Schreier residue towers

There is a stronger conditional consequence for a complete fixed-support
AS-residue tower inside any fixed total-degree cap at most `12`.  Fix one
finite set of coefficient slots and impose every
coefficient of the determinant equation at every precision.  If this same
complete scheme is nonempty modulo `3^n` for arbitrarily large `n`, its
closed solution subsets in the compact coefficient ball `Z_3^N` are nested
and nonempty.  Compactness (equivalently finite branching plus Koenig's
lemma) gives one exact `Z_3` Keller map.

For the B9 AS component, the reviewed moving-residue-ball argument gives
distinct colliding `Z_3` points after the licensed integral source transport.
Adding those points and a unit separation variable gives a finite-type
collision scheme over `Z`; a `Q_3` point makes its generic fibre nonempty,
and base change gives a complex nonautomorphic Keller map in the same fixed
degree box.  The Heitmann/GGV bound forbids that outcome.  Consequently every
complete fixed-D12 B9/B8 AS scheme with the licensed collision transport must
become empty at some finite depth.

This is an existence-of-a-finite-death-depth theorem, not an effective bound
on that depth.  It does not say that one selected parent is the last parent,
that unrelated solutions at different depths form a thread without the
fixed nested scheme, or that any current finite solver result is UNSAT.

## Allocation correction

1. Stop new expensive solver and Groebner expansion whose sole client is any
   fixed-total-D12 B9/B8 envelope, including the broad and strict boxes.
2. Preserve completed fixed-D12 work as controls for the exact
   Kuranishi/Bockstein compiler, finite-death mechanisms, and the new
   Poisson/fractional-power recurrence.
3. Transfer those mechanisms to the genuinely live broad partial-`y` cells,
   where coefficient `x`-degrees and total degrees are unbounded.  Any
   transfer must re-prove the relevant weighted/rational centralizer lemma;
   the squarefree binary-cubic lemma cannot simply be relabeled.
4. Keep TD6 and the global landing/cofinality fronts active.  They are not
   affected by this strict-box correction.

## Refusal scope

This routing correction reuses a classical theorem to close the campaign's
entire fixed-total-D12 counterexample-search envelope; it is not a new proof
of that classical maximum-12 consequence.  It does not exclude unbounded-total
partial-`y` `(9,12)` or `(8,12)`, bound the finite death precision, validate an
incomplete finite family, construct a counterexample, or resolve JC2.  It
corrects which current computations are live clients of those goals.
