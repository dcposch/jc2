# Hostile review — prime-ray `3p` one-edge family

Date: 2026-08-26

| Field | Value |
|---|---|
| Producer under review | `xmodel/prime-ray-3p-one-edge-family-sol-20260826.md` |
| Producer SHA-256 | `6533dd9f2767b5f1930f1cf2ef11baceaeb60480e832fb8197c621c515c68665` |
| Overall verdict | **REPAIRABLE** |
| Arithmetic theorem scope | **CONFIRMED after one local wording repair:** for every prime `p>=7`, `p=3 mod 4`, the fixed `(3,-1)` starting edge has exactly `(3p-13)/4` one-edge final chains, of which exactly `(p-3)/2` carry one `MN` family |
| Scope/firewall | **CONFIRMED:** this is arithmetic in the necessary-chain interface for a globally minimal standard pair, not a theorem about arbitrary total-gcd `3p` Keller pairs or nonminimal prime shears |
| Blocking defects | (i) `gamma=3` is a generated admissible corner but is not final, so generated admissibility and finality do not literally coincide; (ii) the Section 8 terminal-system “equivalence” and one-solution falsifier are false for the repository's covering-only emitted systems |
| Heavy computation / AWS / Lean | none / none / not accessed |

The two defects do not change the parametric family, either count, the
Dirichlet obstruction, or the minimal/nonminimal firewall.  They do change
two literal claims and therefore prevent an unqualified `CONFIRMED` verdict.

## 1. Custody and independent control

All producer and cited hashes match the charged bytes:

```text
6533dd9f2767b5f1930f1cf2ef11baceaeb60480e832fb8197c621c515c68665  xmodel/prime-ray-3p-one-edge-family-sol-20260826.md
729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e  lib/families.py
1394871719df5a9ae7726268c1ad760af3bc89e7f8e707af550e6155e9114d88  lib/FAMILIES.md
f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371  ladder/REDUCTION.md
6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe  xmodel/as109-partial-y-history-stop-20260824.md
f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd  xmodel/as109-partial-y-history-review-grok-20260824.md
```

A read-only invocation of the exact port recovered the displayed `p=7,11,19`
controls.  A second loop checked every prime `p=3 mod 4` through `199` and
found, for each one,

```text
generated gamma = 3,...,v;
final gamma     = 4,...,v;
MN-viable gamma = 4,...,v with 3 not dividing gamma;
number final    = v-3;
number viable   = (p-3)/2.
```

The replay was a regression control only; the formulas below were rederived.

## 2. Starting corner and edge — CONFIRMED

Put `p=4u-1` and `v=3u-1`.  Then

```text
u=(p+1)/4,                 v=(3p-1)/4,
A0=(3u,3v),                A0'=(1,0),
v11(A0)=3(u+v)=3p,
gcd(3u,3v)=3*gcd(u,3u-1)=3.
```

For `mu=2`, the edge form is `(2u,2v)`, and

```text
(2u,2v)-(1,1)=(2u-1,6u-3)=(2u-1)(1,3).
```

The port's `dir_of` convention therefore gives `(rho,sigma)=(3,-1)`.
Algorithm 2 uses

```text
(a',b')=(3u-i,3v-3i).
```

At `i=v`, this is `(1,0)`.  The loop endpoint is legal because
`b/rho=(3v)/3=v`, and `(1,0)` is present in `PLLC`.  Thus the claimed
starting edge is genuinely emitted by the local Algorithm-2 port.  The
conditions `a<b` and `a+b=3p` also hold.

## 3. Generated versus final corners — REPAIRABLE wording, conclusions confirmed

For the edge above,

```text
l1=lcm(3,1)=3,             gap=3,
gmax=min(3v/3,3v-1)=v.
```

The simple-edge equality is `2v-1=3`, which fails because `v>=5`.  The
candidate loop therefore visits every integer `1<=gamma<=v`, and its corner
formula is exactly

```text
a_gamma=9u+(gamma-3v)=gamma+3,
A_gamma=Corner(gamma+3,3,gamma).
```

This confirms the Laurent-lattice point: the geometric first coordinate is
`(gamma+3)/3`; it need not be integral.  No congruence `gamma=0 mod 3` is
required.

The producer's statement that generated-corner admissibility and finality
“coincide here” is, however, false at exactly `gamma=3`.  The actual
`get_generated_corners` test is

```text
a_gamma-3*gamma < 0
and
(3*gamma-a_gamma > gamma or gcd(a_gamma,gamma)>1).
```

Consequently:

- `gamma=1` fails the sign condition;
- `gamma=2` fails the second condition;
- `gamma=3` passes through `gcd(6,3)=3`, although
  `3*gamma-a_gamma=gamma` and hence it is not final;
- every `gamma>=4` is generated and final because
  `3*gamma-(gamma+3)>gamma` is equivalent to `gamma>3`.

The clean repair is therefore:

```text
candidate parameters: 1<=gamma<=v;
generated corners:    3<=gamma<=v;
final corners:        4<=gamma<=v.
```

The one-edge complete chains are still exactly `gamma=4,...,v`, so their
count remains

```text
v-3=(3p-13)/4.
```

For a length-one chain, `is_admissible` returns true before any pairwise
divisibility conditions, exactly as claimed.

## 4. `MN(A_gamma)` and its count — CONFIRMED

At a final corner,

```text
b*l-a=3*gamma-(gamma+3)=2*gamma-3.
```

For `gamma>=4`, the loop inequality `k*gamma<2*gamma-3` admits `k=1`
and excludes every `k>=2`.  Then `e=gcd(1,2*gamma-3)=1`, and the remaining
condition is

```text
gcd(gamma,2*gamma-3)=gcd(gamma,3)=1.
```

Every viable `gamma` therefore contributes exactly one family, with

```text
d1=gamma-3,                d2=gamma.
```

Among `4,...,v`, the number not divisible by three is

```text
(v-3)-(floor(v/3)-1)=v-2-floor(v/3).
```

A prime greater than three and congruent to `3 mod 4` is `7` or `11 mod 12`.
Substitution in both residue classes gives exactly `(p-3)/2`.  The controls
are consequently exact:

```text
p=7:  v=5,  final 4,5,              viable 4,5;
p=11: v=8,  final 4,5,6,7,8,        viable 4,5,7,8;
p=19: v=14, final 4,...,14,          viable 4,5,7,8,10,11,13,14.
```

## 5. Uniformity obstructions — CONFIRMED at the stated narrow scope

The linear growth of the two counts rules out a fixed finite list of literal
`(p,gamma)` chain or family instances.  It does not rule out a finite list of
parametric templates; the producer states this limitation correctly.

For Algorithm 6, the first-edge integer is

```text
Delta0=gcd(3v,(3v-0)/3)=gcd(3v,v)=v=(3p-1)/4.
```

The port's `num_factors` is `Omega` with multiplicity.  Let `Q` be a product
of any finite collection of primes other than `2,3`, and let `r` be the
inverse of `3 modulo 4Q`.  Since `gcd(r,4Q)=1`, Dirichlet supplies infinitely
many primes `p=r mod 4Q`.  Reduction modulo four gives `p=3 mod 4`, while

```text
4Q divides 3p-1, hence Q divides (3p-1)/4=Delta0.
```

Taking `Q` with arbitrarily many distinct factors proves unbounded
`Omega(Delta0)`.  For the stated divisibility shortcut, choose a factor
`q` outside the support of the proposed fixed positive integer `C(3)` and
then choose a Dirichlet prime `p>q`; `q` divides `Delta0` but divides neither
`C(3)` nor `p^e`.  Thus `Delta0 | C(3)*p^e` fails for every fixed `C(3),e`.

This only defeats that published ceiling as a source of a uniform bound.  It
does not prove that realized chain lengths are unbounded; the producer's
nonclaim is exact.

## 6. Generic source shear and the GGV scope firewall — CONFIRMED

The generic-coordinate sharpening can be derived directly from the charged
source-shear identity.  If the seed total degrees are `dP,dQ` and
`D=gcd(dP,dQ)`, a generic linear source coordinate makes the actual
`y`-degrees equal `dP,dQ`.  Their top `y` coefficients are then nonzero
constants, so the source-shear notation has `H=0` and `d=D`.  Formula (1.3)
of the reviewed AS109 source gives, for `L` above the fixed coefficient bound,

```text
deg sigma_L(P)=dP*L,       deg sigma_L(Q)=dQ*L,
gcd=D*L.
```

Taking any sufficiently large prime `L=p` proves the stated `D*p` ray.  All
maps remain in the same source-automorphism orbit.

That last fact is exactly why GGV5 cannot simply be applied to the sheared
pair.  The sheared pair has gcd `Dp`, while its orbit contains the seed of
gcd `D<Dp`; it is not globally gcd-minimal.  `ladder/REDUCTION.md` charges
GGV5 Theorem 2.20/Algorithm 8 only to the globally minimal standard pair
selected by GGV1.  Standardization may undo the prime-producing shear.
Therefore the producer correctly refuses to infer an arbitrary-`3p` theorem,
the `(6,9)` partial-`y` closure, or a finite prime-ray reduction.

One harmless precision: the arbitrary-standard-pair `2p` audit uses not only
`a+b=G` and `gcd(a,b)>2`, but also positivity and `a<b`.  This only reinforces
the firewall; no complete-chain transport to arbitrary standard pairs was
reviewed.

## 7. Section 8 terminal-system semantics — REPAIRABLE, but materially so

The conjectural globally-minimal exclusion `3P-E31` is a legitimate target.
The claimed equivalence with a terminal Laurent-system disjunction is not.
The repository's reduction systems are conservative coverings: true pair
worlds inject into emitted-system solutions, but supports are
over-approximated and no converse is established.  This is stated explicitly
in `jc72108/REDUCE4-CUT-REVIEW.md`, Front 3, and is consistent with
`ladder/REDUCTION.md`'s warning that the special Laurent output is not itself
a Keller pair.

Thus:

- emptiness of every correctly covering terminal system would suffice to
  exclude realization of the corresponding chain;
- a proof that every system solution induces a licensed polynomial degree
  reduction would also suffice;
- nonemptiness of an emitted system does **not** construct a globally minimal
  standard Keller pair and does not falsify `3P-E31`;
- even an exact nonzero Laurent/polynomial solution can be a spurious point of
  the over-approximating system, and a solution might itself lie on a
  degree-reducible branch.

Accordingly, replace “equivalently” by “a sufficient algebraic route is,” and
replace the proposed falsifier by:

> A nonempty exact system falsifies a proposed unit-row/emptiness certificate,
> not the Keller-pair exclusion.  Falsifying `3P-E31` itself requires a
> globally minimal standard Keller counterexample realizing the registered
> chain, or a separately proved converse from the system witness to such a
> pair.

The suggested `p=7,11` regrading remains a useful search for a uniform
functional, provided success is interpreted one-way and interpolation is not
promoted as a theorem.

## 8. Exact disposition

| Claim | Verdict |
|---|---|
| `u,v,A0`, scale `3p`, coordinate gcd `3` | **CONFIRMED** |
| `mu=2` gives direction `(3,-1)` and endpoint `(1,0)` | **CONFIRMED** |
| Laurent denominator `l=3`; no `gamma mod 3` integrality requirement | **CONFIRMED** |
| Candidate loop `1<=gamma<=v` | **CONFIRMED** |
| Generated admissibility equals finality | **REPAIRABLE:** exception `gamma=3` |
| Final range `4<=gamma<=v` and count `(3p-13)/4` | **CONFIRMED** |
| MN condition `gcd(gamma,3)=1`, one family, count `(p-3)/2` | **CONFIRMED** |
| `p=7,11,19` controls | **CONFIRMED** |
| Unbounded `Omega((3p-1)/4)` by CRT/Dirichlet | **CONFIRMED** |
| Failure of fixed `C(3)*p^e` divisibility shortcut | **CONFIRMED** |
| No conclusion about realized chain lengths | **CONFIRMED limitation** |
| Generic source shear produces gcd `D*p` for all sufficiently large primes | **CONFIRMED** |
| GGV5 global-minimum / nonminimal-shear firewall | **CONFIRMED** |
| Terminal-system equivalence and one-solution falsifier | **REPAIRABLE:** false converse; retain only the sufficient emptiness/reduction direction |

## Final verdict

**REPAIRABLE.**  Bank the exact `3p` one-edge arithmetic, both counts, the
factor obstruction, and the scope firewall after correcting the unique
`gamma=3` generated/nonfinal exception.  Do not bank the Section 8 system
“equivalence” or claim that one nonzero terminal-system solution falsifies a
Keller-pair exclusion.  No result here proves or disproves JC2.

## Re-review disposition — 2026-08-26

Charged repaired producer SHA-256:

```text
8217cc3f354a5d079f110380c8303370ff2c773846cd3738bd6fb8d381d11cc1
```

**Verdict on the repaired artifact: CONFIRMED at the original narrow scope.**

The `gamma=3` seam is now exact.  Section 3 distinguishes the candidate loop
`1<=gamma<=v` from the returned generated corners `3<=gamma<=v` and the final
corners `4<=gamma<=v`.  It records the exceptional admission
`gcd(6,3)=3`, states that this corner is not final, and leaves the final-chain
and `MN` counts unchanged.

The terminal-system seam is also now exact.  Section 8 states only the valid
one-way implication: emptiness of all correctly covering systems, or a
licensed degree reduction for every system solution, suffices for `3P-E31`.
It expressly denies a converse, says that a nonempty covering system defeats
only the proposed emptiness certificate, and requires either an actual
globally minimal standard Keller counterexample or an independently proved
converse to falsify `3P-E31`.  Section 9 repeats the no-converse nonclaim.

No new mathematical or scope issue was introduced by these repairs.  The
earlier `REPAIRABLE` disposition remains the audit history of SHA
`6533dd9f...`; this appended disposition supersedes it only for repaired SHA
`8217cc3f...`.  All other confirmations and limitations in this review remain
unchanged.
