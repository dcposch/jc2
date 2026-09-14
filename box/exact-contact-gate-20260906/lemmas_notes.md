# Independent Lemmas A/B audit

Frozen mathematical inputs only. Root mechanically verified 7/7 hashes before delegation.
Images of Moh pp.150,179,180,200 were inspected from temporary rasterizations in
`/tmp/jc2-lemmas-scratch/`; equations missing in OCR below were read from those images.
The authoritative source is the frozen PDF; line references identify the retained extracts.

## A: the claimed primitivity is refuted as a printed numerical necessity

The report asserts that at every split the multiplicities
`r_j=rho_j/(m/d)` of the reduced pattern have gcd 1, because otherwise `d` was
not the reduction divisor. This confuses a global characteristic divisor with
the maximal power of one local leading polynomial.

Moh p.170 Prop.4.6(1) specifies a common polynomial `p` of degree `v`; (2)
specifies the complementary polynomial `q`; (3) says `q` has distinct roots;
(4) every root of `p` is a root of `q`; (5) says **p is not a power of q**.
There is no statement that `p` is not itself a proper power.
See `moh.txt:1632-1644`.

The decisive printed countercontrol is Xu section 6.1(i), PDF p.8,
`xu.txt:406-416`, for `n=75,m=50,M2=55,M3=73,V3=4,V2=2`:

```
f_sigma2 = a ((pi^5-c1)(pi^5-c2))^4,
g_sigma2 = b ((pi^5-c1)(pi^5-c2))^6.
d2 = gcd(75,-50) = 25;  m/d2 = 2;  n/d2 = 3.
p2 = ((pi^5-c1)(pi^5-c2))^2.
```

There are ten distinct roots, each with reduced multiplicity 2. Their gcd is 2,
not 1. Xu explicitly computes `IM=8, Im=4` and retains this possibility. The
producer itself uses this same case as a positive control. Replacing `p2` by
its square root would require a putative `d'=25/2`, not an allowed integer
global characteristic divisor. Thus the stated rationale for Lemma A fails
even at the level of the elementary exponents in its positive control.

An explicit local polynomial witness supplied by root and independently
expanded/gcd-checked in `lemmas_audit.py` makes this stronger than relying
on an unexcluded hypothetical pair. Set

```
h = pi^10-5*pi^5+5,
s = pi^6-3*pi,
p = h^2,                    deg p = 20,
q = h*s,                    deg q = 16.
5*h*s' - 3*h'*s = -75,
20*p*q' - 16*p'*q = -300*p.
```

The last line is the reduced local ODE `D(P,Q,p,q)=c*p` appearing after
Moh's Prop.A.4 (`moh.txt:3536-3544`) for this row's `P=20,Q=16`.
Both h and q are squarefree, `gcd(h,s)=1`, all roots of p are roots of q,
and p is not a power of q (already impossible from their degrees).
Nevertheless every root of p has multiplicity 2. Moreover
`h=(pi^5-(5+sqrt(5))/2)(pi^5-(5-sqrt(5))/2)` realizes precisely the two
nonzero A=5 orbits in Xu's first pattern.

This is a counterexample to the proposed filter in the printed necessary
configuration calculus; it is **not** a polynomial counterexample to the
Jacobian conjecture. The global data do not supply a theorem excluding the
local proper power. Verdict for Lemma A as stated: **REFUTED**.

## B: exact lattice statement, its proof, and its proper scope

Moh p.150 is a different series construction from the physical Puiseux discs
at `x=t^-1`. It sets

```
eta = g(x,y)^(-1/n) = y^-1 + alpha2(x)y^-2 + ...,
f(x,y) = eta^-m + sum_{a>-m} f_a(x) eta^a.
d1 = n,
d_{i+1} = gcd(n,M1,...,Mi),
Mi = min{a : f_a(x) != 0, d_i does not divide a}.
```

See `moh.txt:533-547,562-572`; the displayed equations require the page image
because they are absent from layout OCR. The `M_i` are the characteristic
indices of the conjugate defining-equation roots under `eta -> omega eta`,
with x fixed. They are not arbitrary physical t-contact exponents.

Two precise consequences are immediate:

1. If `f_a(x)!=0` and `a<M_i`, then `d_i|a` (otherwise the minimum defining
   `M_i` was not minimal).
2. For every pair of characteristic indices `j<i`, `d_i|M_j` by the gcd
   definition, equivalently `n-M_j == n (mod d_i)`.

In Moh's major tower `Ds superset ... superset D1`, an ancestor `Di` of `Dj`
has `i>j`; therefore statement 2 really does give the divisor condition for
**every ancestor**, not just the immediate parent, when all indices are in
the same global characteristic list.

If one hypothesizes a genuinely new nonzero eta-support exponent a below
Mi, fixing the old characteristic divisor requires `d_i|a`. This is the
correct conditional form of the report's assertion. It does not establish
that a free effective parameter obtained by solving
`M=n-W` from an arbitrary sibling split is such a nonzero eta-support index.
That bridge is absent from the proof. Nor does the congruence make such an
inserted tower compatible with the frozen complete characteristic list.

Verdict: **CONFIRMED-WITH-FIX** for the conditional support/global-chain
divisibility. It cannot be used as the claimed license for a free-W closure.
The stronger correct closure is the following printed result.

## Same-list tower continuation removes the artificial depth parameter

Moh p.179 Def.5.1(4) uses the *fixed* associated characteristic data for
every tower and declares the conditions of Prop.4.6 at each `Di`, with
`v=V_{i+1} d_i/d_{i+1}`. The paragraph immediately following the definition
explicitly says **any** above-average subdisc of `Ds` can be used as `Ds-1`
(`moh.txt:2137-2148`).

More generally, p.180 Prop.5.3 takes *any* factor `pi-c_r` of `p_r` with
multiplicity

```
deg(p_r) >= V_r > d_r/(n-M_r),
```

and says the continuation is a major disc `D_{r-1}` whose radius is

```
delta_{r-1} = 1 -
 (n-M_{r-1}) product_{j=r}^s [V_j(n-M_j)-d_j]
 / ((n-M_s-1) product_{j=r}^s [V_j(n-M_{j-1})-d_j]).
```

Then `Ds superset ... superset Dr superset D_{r-1}` is again a tower of major
discs. See `moh.txt:2157-2179`; the formula is read from the page image.
The proof at pp.180-183 does not merely select one possible next radius:
it rules out an earlier one using a hypothetical
`M_r > L* > M_{r-1}` and Prop.4.4 (`moh.txt:2182-2214`), then establishes
equality (`moh.txt:2280-2317`). Thus there are no arbitrary intervening major splits with a new
W parameter in this fixed-list tower calculus.

The summary theorem p.200(4) repeats that **every** subdisc `Ei` containing
more than `n/(n-M_r)` g-roots extends the tower (`moh.txt:3231-3247`).
The statement applies uniformly to parallel and unequal-multiplicity major
siblings, using different V selections but the same global M,d sequence.
The index decreases at each major step; a complete length-s chain has at
most s-1 such steps. In particular a major sibling formed at level 2 goes
next to D1. For r=1, Prop.4.6 gives
`D(n,-M1,g_sigma,T1_sigma)=nonzero constant` (`moh.txt:1646-1648`).
A repeated root of either leading polynomial, or a common root of the two,
would make both terms of the determinant zero there. Hence both patterns
are squarefree and disjoint; D1 is final in Xu's sense when its f-degree
exceeds one. There is no further major continuation below it. A depth cap
on an unconstrained extra-M search is not the mathematical completion
criterion.

## Twenty reproducibly random rows

`lemmas_audit.py` reads only the frozen roster. The sample method is
`random.Random(20260906).sample(rows,20)`, sorted by row id only for output.
Results in `lemmas_audit.json`:

```
R001 R003 R004 R007 R008 R010 R013 R017 R020 R033
R038 R039 R040 R046 R048 R050 R058 R059 R060 R063
20/20 gcd recurrences pass; 88/88 ancestor/deeper pairs pass.
```

Each record checks `d_i=gcd(n,M_1,...,M_{i-1})` and all `j<i` pairs,
including non-immediate ancestors, for both `d_i|M_j` and
`n-M_j == n (mod d_i)`. Negative controls check `d_i` **does not divide**
the same-index characteristic exponent `M_i`; every check passes.
The script and JSON explicitly distinguish this necessary chain test from
the unsupported free-W-to-support bridge. It is a mechanical corroboration
of the roster's lattice consistency, not evidence that sampled configurations
are realized polynomial pairs.

## Ell shift and the separate invariance question

Xu Lemma4.1 is genuinely valid for an arbitrary polynomial Jacobian:
`gy(alpha) d_t f(alpha)-fy(alpha) d_t g(alpha)=-J(t^-1,alpha)t^-2`
(`xu.txt:192-203`). Consequently J=c*x^ell gives RHS `-c*t^(-ell-2)`.
At a final major root where the leading determinant is nonzero, comparing
orders in the proof of Lemma4.4 gives
`lambda_f+lambda_g+1+ell=delta`; the corresponding minor argument gives
`delta>1+ell` when both leading orders are zero
(`xu.txt:227-241`).

Moh p.171 Remark explicitly extends Prop.4.6 to `J=x^ell` after replacing
condition (3) by `lambda=(-1-ell+delta)/(n-M_r)` with its accompanying
strict inequality (`moh.txt:1711-1718`, formula visually verified by root).
Thus the **local ell sensitivity is confirmed**. For complete final-major
packets satisfying these shifted source hypotheses, the same norm calculation
gives the shifted weighted expression; that inference must keep its hypotheses.

However, a changed coordinate formula is not proof of *failure of descent
invariance*. A transformation can change the parameter, packet cardinality,
and contact orders while preserving the quantity or test. The producer itself
finds `IM'=IM=8` on both targeted rows and explicitly labels numerical
invariance open. Its final inference, that the shift *hence* proves
non-invariance, is therefore unsupported. A commuting comparison between the
parent and child root configurations, or a counterexample to it, remains to
be supplied. The full Xu minor inequality is only printed for a constant
Jacobian (`xu.txt:261,352,396`), which the producer correctly acknowledges.

Recommended item-f verdict: **CONFIRMED-WITH-FIX** if phrased as ell-sensitive
local formulas and **OPEN** descent invariance; **REFUTED** for the asserted
logical implication that ell sensitivity alone establishes non-invariance.

No new exit-price assertion is made in these notes.

## Margin-zero rigidity: precise proof and limit of the conclusion

This section independently checks the strictness needed to turn a minor floor
into an attained contact pattern on R009/R050. Start with a Moh minor packet
of rho f-roots, generic-disc order `lambda_f=-a<0` at radius delta0. While
the packet remains unsplit the product formula gives

```
lambda_f(delta) = -a + rho*(delta-delta0),
delta_star = delta0 + a/rho > 1.
```

Every root in this packet remains a minor root by Xu Cor.4.5
(`xu.txt:244-251`). If it first genuinely splits at `delta_s<delta_star`
into k>=2 nonempty packets with multiplicities rho_j and sum rho_j=rho,
write `b=a-rho*(delta_s-delta0)>0`. The nominal zero orders of the children
are `delta_j=delta_s+b/rho_j`; all exceed 1 since
`delta_j>=delta_s+b/rho=delta_star>1`. Relative to leaving the parent
unsplit, the change in the sum of nominal minor contributions is

```
Delta = sum_j(delta_j-1) - (delta_star-1)
      = (k-1)*(delta_s-1) + b*(sum_j 1/rho_j - 1/rho).
```

If delta_s>=1, both terms are nonnegative and the second is positive.
If delta_s<1, use `b>rho*(1-delta_s)` and Cauchy
`rho*sum_j(1/rho_j)>=k^2` to obtain

```
Delta > (1-delta_s)*(rho*sum_j 1/rho_j-k)
      >= (1-delta_s)*k*(k-1) > 0.
```

Thus every genuine earlier split strictly increases the eventual minor sum;
the same argument iterates on each child. For the two target rows, the
admissible multiplicities are multiples of `m/gcd(n,m)=2`, so the unsplit
terminal packets have f-degree at least 2 as required by Xu's definition
of a final pi-root. The proof is being applied to admissible minor packets,
not to artificial singleton leaves omitted by that definition.

The nominal zero radius is attained if there is no earlier genuine split.
At this radius both leading orders are zero. If the f_xi leading pattern
had a repeated root, Xu Lemma2.1(ii) (`xu.txt:64-73`) would give
`f_sigma^n/g_sigma^m in K*`. Hence its roots would also be roots of
g_sigma, and an actual f_xi root continuing from such a root would have
`ord g(alpha)>0`. This contradicts Cor.4.5, which says every root in this
Moh minor packet has `ord g(alpha)=0`. Therefore the zero-order f_xi
pattern is squarefree; the same minor property also excludes a shared
f_xi/g leading root. This proves finality there, with exact order
delta_star, and excludes an unaccounted delay past it. The use of generic
f_xi is part of Xu Lemma2.1's stated hypotheses.

A unary step, where all roots acquire the same next centre coefficient,
is not a split and changes neither the packet cardinality nor the product
valuation intercept. At a generic point of any correctly centred disc
below the first internal separation, each of the rho factors has order
delta; factors outside the packet have their previously fixed contacts.
The displayed affine valuation formula therefore survives all such centre
changes. Arbitrary unary descriptions cannot move delta_star.

Once the finite major closure has left a unique major contact pattern with
`IM=8` and the unsplit minor floor is `Im=8`, these strict inequalities
exclude every earlier genuine minor split. The major contribution remains
fixed and minor descendants cannot become major by Cor.4.5. Therefore the
**necessary contact orders and multiplicities** are pinned to the unsplit
pattern. This conclusion does not assert unique polynomial coefficients,
unique Puiseux centres, or existence of a realized polynomial pair. Local
coefficient moduli and global compatibility equations remain outside this
contact/multiplicity assertion.
