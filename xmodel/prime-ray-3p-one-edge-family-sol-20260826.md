# Prime-ray `3p` one-edge family: exact arithmetic audit

Date: 2026-08-26

Status: **HOSTILE-REVIEW-REPAIRED HAND-DERIVED GGV5-INTERFACE OBSTRUCTION
WITH READ-ONLY SCRIPT CONTROLS; NOT A KELLER-PAIR OR PRIME-RAY THEOREM.**

This note isolates a parametric family inside the GGV5 admissible-chain
arithmetic.  It corrects two tempting but false navigation claims:

1. fixed seed multiplier `g` does not give a uniformly bounded number of
   literal admissible chains as the prime `p` grows; and
2. the factor-count integer controlling Algorithm 6 cannot in general be
   bounded by the prime factors of `g*p`.

The result applies only to the necessary-chain interface for a **globally
minimal standard pair**.  A pair obtained by applying a high triangular
source shear to a seed counterexample is nonminimal by construction, so this
note cannot be applied to that pair.  That firewall is load-bearing.

## Review erratum and disposition

Independent hostile review:

```text
xmodel/prime-ray-3p-one-edge-family-hostile-review-sol-20260826.md
  0f1a2977b723c75e0e039868e47c074835c9cdcddb715075af40ea0751c9ba12
```

Verdict: **REPAIRABLE; all arithmetic conclusions confirmed after two local
scope corrections.**  This version incorporates both:

1. `gamma=3` is generated and admissible through the gcd clause, but is not
   final; the final range and both counts are unchanged; and
2. the emitted terminal systems are conservative coverings, not equivalent
   moduli problems.  Their emptiness is a sufficient exclusion route, while
   their nonemptiness does not produce or falsify a Keller-pair theorem.

No other reviewed arithmetic, control, factor obstruction, or scope
firewall is changed.

## 1. Sources, notation, and evidence tiers

The local exact-integer port is:

```text
lib/families.py       SHA-256 729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e
lib/FAMILIES.md       SHA-256 1394871719df5a9ae7726268c1ad760af3bc89e7f8e707af550e6155e9114d88
ladder/REDUCTION.md   SHA-256 f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371
```

`Corner(a,l,b)` denotes the geometric point `(a/l,b)`.  In particular, a
corner with `l=3` lies in `(1/3) Z x Z`; its first geometric coordinate need
not be integral.  This resolves the apparent integrality issue in
`((gamma+3)/3,gamma)`.

Evidence tiers used below:

- **DIRECT HAND DERIVATION:** all displayed formulas, inequalities, gcds,
  counts, and the Dirichlet/CRT factor obstruction;
- **READ-ONLY SCRIPT CONTROL:** the instances `p=7,11,19`, using the frozen
  local port without editing it;
- **LITERATURE INTERFACE ASSUMPTION:** that GGV5 Theorem 2.20 and Algorithms
  2--9 have exactly the globally-minimal-standard-pair scope recorded in
  `ladder/REDUCTION.md`, and that the local port faithfully represents those
  algorithms.  This note does not independently reprove that theorem.

The separate source-shear theorem and review remain:

```text
xmodel/as109-partial-y-history-stop-20260824.md
  6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe
xmodel/as109-partial-y-history-review-grok-20260824.md
  f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd
```

They are cited only to explain the nonminimal-shear firewall in Section 7.

## 2. The starting corner and edge

Let `p >= 7` be prime with

```text
p == 3 mod 4.
```

Write

```text
u = (p+1)/4,                 v = 3u-1 = (3p-1)/4.
```

Define the integral starting corner and lower endpoint

```text
A0 = Corner(3u,1,3v),        A0' = Corner(1,1,0).
```

Then

```text
v_(1,1)(A0) = 3u+3v = 3p,
gcd(3u,3v) = 3 gcd(u,3u-1) = 3,
3v = 3((3u)-1).
```

Thus this is the `p`-free first-corner branch: the total corner scale is
`3p`, but the coordinate gcd is only `3`.

In `get_starting_edges`, choose `mu=2`.  The edge-form endpoint is

```text
enF = (2u,2v),
enF-(1,1) = (2u-1,6u-3) = (2u-1)(1,3),
```

so its primitive normal direction is

```text
(rho,sigma) = (3,-1).
```

Algorithm 2 uses

```text
A0' = A0 - i*(-sigma,rho).
```

At `i=v`, this is exactly

```text
(3u-v,3v-3v) = (1,0).
```

The loop permits this value because `i <= b/rho = v`.  This proves the
displayed starting edge inside the local GGV5 arithmetic.

## 3. Every generated final corner

For this edge,

```text
l1   = lcm(rho,1) = 3,
gap  = rho/gcd(rho,1) = 3,
gmax = min((3v-0)/3,3v-1) = v.
```

For `p>=7`, `v>=5`; the edge is not simple because the Algorithm-3 simple
equality would require `2v-1=3`.  Hence the generated parameter runs through
every integer

```text
1 <= gamma <= v.
```

The numerator of the generated corner is

```text
a_gamma
  = 3*(3u) + (gamma-3v)*(-sigma)*(3/rho)
  = 9u + gamma - 3v
  = gamma+3.
```

Therefore

```text
A_gamma = Corner(gamma+3,3,gamma)
        = ((gamma+3)/3,gamma) geometrically.                 (3.1)
```

There is no requirement `gamma == 0 mod 3`: the denominator `l=3` is part
of the Laurent-corner datum.

The generated-corner test is

```text
(gamma+3)-3*gamma < 0
and
(3*gamma-(gamma+3) > gamma or gcd(gamma+3,gamma)>1).        (3.2)
```

Consequently:

```text
gamma=1  fails the sign condition;
gamma=2  fails the second condition;
gamma=3  is generated through gcd(6,3)=3, but is not final;
gamma>=4 is generated and final because
         3*gamma-(gamma+3)>gamma <=> gamma>3.
```

Thus the generated corners are exactly `3<=gamma<=v`, whereas every integer

```text
4 <= gamma <= v = (3p-1)/4                                (3.3)
```

gives an admissible one-edge complete chain.  Their literal count is

```text
v-3 = (3p-13)/4.                                           (3.4)
```

Length-one chains pass `is_admissible` automatically because its pairwise
conditions begin only when there are at least two edges.

## 4. Exact `MN(A_gamma)` viability lattice

A complete chain contributes a GGV degree family only when the final corner
has a nonempty `MN(A_gamma)` set.  For (3.1), Algorithm 9 has

```text
b*l-a = 3*gamma-(gamma+3) = 2*gamma-3.
```

The loop condition

```text
k*gamma < 2*gamma-3
```

allows exactly `k=1` for `gamma>=4`.  Then `e=1`, and the remaining
coprimality condition is

```text
gcd(gamma,2*gamma-3) = gcd(gamma,3) = 1.                    (4.1)
```

Thus the exact one-edge parameter lattice carrying an `MN` family is

```text
p prime, p>=7, p == 3 mod 4;
4 <= gamma <= (3p-1)/4;
gamma != 0 mod 3.                                          (4.2)
```

There is one `k=1` family for each such `gamma`.  Its step sizes, if needed,
are

```text
d1 = gamma-3,             d2 = gamma,
```

with the initial coprime `(m,n)` obtained from the Bezout pair used by
Algorithm 9.

For a prime `p>=7` with `p==3 mod 4`, necessarily `p==7` or `11 mod 12`.
Counting the integers in (4.2) gives

```text
v-2-floor(v/3) = (p-3)/2.                                  (4.3)
```

This is the corrected viable-family count.  Formula (3.4) counts all
admissible final chains; formula (4.3) counts only those carrying a GGV
`MN` family.

## 5. Read-only controls

The exact local port was queried without modification.  It returns:

| `p` | `3p` | `A0` | all final `gamma` | `MN`-viable `gamma` |
|---:|---:|---|---|---|
| 7 | 21 | `(6,15)` | `4,5` | `4,5` |
| 11 | 33 | `(9,24)` | `4,5,6,7,8` | `4,5,7,8` |
| 19 | 57 | `(15,42)` | `4,5,6,7,8,9,10,11,12,13,14` | `4,5,7,8,10,11,13,14` |

The counts are respectively `(2,2)`, `(5,4)`, and `(11,8)`, matching
(3.4) and (4.3).  The controls check the implementation path; they are not
evidence that any polynomial Keller pair realizes a chain.

## 6. Two uniformity obstructions

### 6.1 No uniformly finite literal menu

The number of admissible one-edge chains already grows as `(3p-13)/4`, and
the number carrying an `MN` family grows as `(p-3)/2`.  Therefore no menu of
a fixed finite number of **literal chain/family instances**, independent of
`p`, can cover this one edge.

This does not rule out a finite number of **parametric templates**.  Indeed,
(4.2) itself is one such two-parameter template.  The exact successor must
seek a uniform identity or monovariant in `(p,gamma)`, not enumerate prime
values or final corners one at a time.

### 6.2 The Algorithm-6 factor bound is not uniform

For the first edge, the integer in the Algorithm-6 length bound is

```text
Delta0 = gcd(b0,(b0-b0')/rho)
       = gcd(3v,v)
       = v
       = (3p-1)/4.                                         (6.1)
```

`num_factors(Delta0)` is `Omega(Delta0)`, with multiplicity.  It is
unbounded along these primes.  More strongly, let `Q` be a product of any
prescribed finite set of primes different from `2,3`.  Dirichlet's theorem
gives primes

```text
p == inverse(3) mod 4Q.
```

Then automatically `p==3 mod 4` and

```text
Q | (3p-1)/4 = Delta0.
```

Choosing `Q` with arbitrarily many distinct prime factors makes
`Omega(Delta0)` arbitrarily large.  Choosing one prime factor of `Q` outside
the support of a proposed fixed `C` also disproves any universal claim

```text
Delta0 | C(3)*p^e
```

with fixed `C(3)` and fixed `e`.

This does **not** prove that realized chain lengths are unbounded.  The
chains constructed above have one edge.  It proves only that the published
factor-count ceiling and a proposed `C(g)*p^e` divisibility shortcut cannot
supply a `p`-uniform chain bound.

## 7. Minimal-pair / nonminimal-shear firewall

The reviewed source-shear theorem says that, after a generic linear source
choice, a hypothetical counterexample of total-degree gcd `D` produces by
`y -> y+x^p` a source-equivalent counterexample of gcd `D*p` for every
sufficiently large prime `p`.

That statement does not license GGV5 on the sheared pair:

- GGV5 Theorem 2.20 and Algorithm 8 are consumed in
  `ladder/REDUCTION.md` only for a **globally minimal standard pair**.
- The sheared pair has the original seed pair in its source-automorphism
  orbit and hence is deliberately nonminimal.
- Standardizing or degree-reducing it may simply undo the shear and erase
  `p`.

Only the first-corner facts `a+b=G` and `gcd(a,b)>2` have been reviewed in
the broader arbitrary-standard-pair argument used for the `2p` theorem.
The complete-chain enumeration above cannot be projected to that scope.

Therefore this note does not prove a theorem about arbitrary gcd `3p`
pairs, does not close the partial-`y` `(6,9)` frontier, and does not turn the
prime-ray equivalence into a finite reduction.

## 8. Best falsifiable next lemma

The smallest source-typed mathematical target exposed by the audit is:

> **`3P-E31` (conjectural uniform one-edge exclusion).** For every prime
> `p>=7` with `p==3 mod 4` and every `gamma` satisfying (4.2), no globally
> minimal standard Keller counterexample realizes the GGV5 chain
> `A0 -> (1,0)`, direction `(3,-1)`, with final corner `A_gamma`.

A sufficient algebraic route to `3P-E31` is to prove every correctly covering
terminal Laurent system empty, or to prove that every one of its solutions
supplies a licensed polynomial degree reduction contradicting global
minimality.  No converse from an emitted-system solution to a Keller pair is
currently available.

Why this is the cheapest material lemma:

1. the direction, lower endpoint, denominator, and final-corner formula are
   fixed;
2. all prime dependence is explicit in `A0`, and all residual dependence is
   the single integer `gamma`;
3. the repository already contains bounded navigation controls at starting
   corners `(6,15)` and `(9,24)`; and
4. a uniform row functional or valid Moh-type degree reduction would prove an
   infinite-family exclusion.  A nonempty covering system would instead
   falsify only that proposed emptiness certificate.

The cheapest experiment is not another prime census.  Regrade the frozen
`p=7` and `p=11` terminal systems by `(p,gamma)`, retain raw Laurent supports,
and ask whether a common bracket-row functional has a coefficient that is a
unit throughout (4.2).  A proposed functional must then be derived
symbolically over `Q[p,gamma]` with the congruence/divisibility side
conditions; interpolation alone is navigation.  Nonemptiness of an emitted
system is not a falsifier of `3P-E31`: falsification requires a globally
minimal standard Keller counterexample realizing the chain, or an
independently proved converse transporting a system witness to such a pair.

Even a proof of `3P-E31` remains a globally-minimal-`3p` result.  A separate
arbitrary-standard-pair transport or direct degree-gcd argument would still
be required before using it on the nonminimal prime shears emitted from an
arbitrary seed.  That is the exact global obstruction, not bookkeeping.

## 9. Explicit nonclaims

- No counterexample, Keller pair, or Laurent realization is constructed.
- No total-degree-gcd `3p` exclusion is proved.
- No statement about every arbitrary standard pair is proved.
- No converse from a covering-system solution to a Keller pair is asserted.
- No bound on realized chain length is proved.
- No finite parametric-template theorem is disproved.
- No source-to-Sigray, source-to-`A(F)`, landing, topological-degree ceiling,
  or JC2 conclusion is made.
- No heavy computation, AWS job, or `jc2-lean` access was used.
