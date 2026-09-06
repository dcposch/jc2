**Descent of packets: an orbit transport theorem, and an unverified R063 identification**

The full packet partition is **not carried bijectively to the child's infinity
partition**. There is, however, an explicit transport rule for its major orbits.
For an actual licensed descent in the reduced source setting it gives
`I'_M = u_s I_M`, hence **`I'_M = I_M` when `u_s=1`**. This statement compares
mapped roots; it does not identify independently enumerated necessary configurations.
New child minor packets and a different number of discs are compatible with it.

The named-row verdict is **OPEN**. The frozen replay's literal R063 descriptor
and the charged own-data instrument cannot describe a parent with `I_M=19`.
The child arithmetic gives `71/4`, but the reconstructed source possibilities
give `1035/59` and fail final Galois compatibility. Neither “corrected to 19”
nor “R063 DEAD” is certified. The missing input is the correct frozen R063 row
with its complete pattern; no unfrozen roster was substituted.

**Custody and source convention.** I joined the receipt's numbered basename and
SHA-256 fields with `awk`, then ran `sha256sum -c`: **8/8 OK**. The manifest is
`box/descent-partition-20260906/charged-inputs.sha256`. Mathematical inputs were
the frozen copies in `/tmp/jc2-lane.X8q4dc/inputs`; no fleet, ledger edit,
`jc2-lean`, or `ideation-*` input was used.

Here **M** means Moh and **X** Xu, with printed page numbers. Layout extracts are [moh.txt](/home/ubuntu/jc2/box/descent-partition-20260906/moh.txt)
and [xu.txt](/home/ubuntu/jc2/box/descent-partition-20260906/xu.txt). I also inspected
the images of M pp.171, 188, 197–198, where the text layer loses formulas.
The exact arithmetic and descriptor audit are [check.py](/home/ubuntu/jc2/box/descent-partition-20260906/check.py)
and [checks.json](/home/ubuntu/jc2/box/descent-partition-20260906/checks.json).

**The ring map and the printing conflict.** Use Xu's smaller member `f=T_1^ψ`,
larger member `g`, and degrees `m<n`. This is Moh's reduced convention on p.200;
if starting with an unreduced first member, first declare the triangular target
change `(f,g) -> (T_1^ψ(f,g),g)`. It preserves the target function field but does
not justify identifying two pre-existing fibre partitions. Primes below label
the child, never derivatives.

Write `u=u_s`, `v=v_s`, `d=d_s`, `ell=v-u-1`, `H=ell+1=v-u`, and retain Moh's
normalization of the major direction to `y=0`, with minor direction `y=bx+e`,
`b!=0` (M pp.194–195, equations (8)–(10)). Absorb the printed finite truncation
and its harmless sign choices into `c(gamma)`. The ordered generator map is

```
Phi*: k[x,y] -> k[gamma,gamma^(-1),pi]
y |-> gamma^(-u),
x |-> (gamma^(-u)-e-c(gamma)-gamma^v*pi)/b.
F = Phi*(f), G = Phi*(g) in k[gamma,pi], by Prop. 6.3(1),
deg_pi F = m' = um/d, deg_pi G = n' = un/d, by (2).
```

Thus `x_pi=-gamma^v/b`, `y_gamma=-u gamma^(-u-1)`, and
`J_(gamma,pi)(x,y)=-u gamma^(v-u-1)/b`. For Moh's output order `(G,F)`, whose
source determinant is normalized to 1 on p.198, this is also `J(G,F)`.
Swapping to `(F,G)` changes only its nonzero constant sign.

M p.197(3) prints the **positive monomial** `-(u/b) gamma^(v-u-1)`.
The p.198 determinant instead prints reciprocal powers, inconsistent with the
substitution immediately above it. The reciprocal in the charge repeats that
conflict. Taken literally for `ell>0`, it cannot be the Jacobian of two members
of `k[gamma,pi]` at all. The substitution and p.197 determine the correction;
it is not a choice of convention. All computations here use `C gamma^ell`.
See [M, Prop. 6.3 text vicinity](/home/ubuntu/jc2/box/descent-partition-20260906/moh.txt:3063).

With `gamma` fixed, `pi -> infinity`
is `x -> infinity` over `k(y)`, after `k(y) -> k(gamma)`. That is precisely the
charged child-top reduction for the p.150 **eta-characteristic datum**. For Xu's
child packets, however, the base tends to infinity: set `T=gamma^(-1)` and
solve `F(T^(-1),pi)=xi` in Puiseux series in **T**. Then `y=T^u -> 0`.
The printed `pi_i=(tau_i-c)/gamma^v` initially describes the principal cluster
over `gamma=0`, where `y=infinity`, not Xu's child infinity partition.
Characteristic conjugates over g and roots of `f-xi` over the base are distinct.

**The local rule, including the count.** Translate the child's formal root
coordinate by its common centre, writing

```
h(T)=T^v (T^u-e-c(T^(-1))),
w=pi-h(T)=-b T^v x=-b T^v/t,      t=x^(-1), y=T^u.
```

This changes the Puiseux centre. Consider a parent packet with common centre
`y=a t^epsilon+...`, `a!=0`, `epsilon>0`, and radius `delta>epsilon`.
Let an entire conjugacy orbit contain `N` such discs, with `rho_f` roots in each.
Here N is the actual centre orbit size; inserting denominators from earlier
zero coefficients does not increase it. In particular `epsilon N` is an integer.
Then its image has

```
number of child discs       N' = epsilon N,
roots in each child disc    rho'_f = rho_f,
radius                     delta' = v-u + (u/epsilon)(delta-1),
orders                     lambda'_f = (u/epsilon)lambda_f,
                           lambda'_g = (u/epsilon)lambda_g.
```

The `u`-cover may split an image into several Galois orbits; their total
number of discs remains `epsilon N`.

Take `s=t^(1/N)` for the parent centre. Its projection
to the y-axis has first exponent `k=epsilon N`. Inversion gives k inverse
centres over the Puiseux closure: extract a k-th root of the leading unit to
invert `s^k U(s)`. Minimality of N makes the inverse centres distinct.
Replacing `y` by `T^u` changes grouping, not this count. This proves the
positive-epsilon inversion directly; M Lemma 6.2, pp.196–197, states the
equal-pole-order case used at the principal chart. At `epsilon=p/q`, one
q-orbit therefore produces p inverse coefficients.
The charged instrument's `inverse_top` implements exactly this count, including
its explicit statement that multiplication by u is absent from the root count
([frozen instrument](/tmp/jc2-lane.X8q4dc/inputs/descend_own.py:76)).

For contacts, `dy/dx` has t-order `epsilon+1`. Changing y by order delta at
fixed x changes inverse x by order `delta-epsilon-1`. Since `ord_T t=u/epsilon`
and `w=-b T^v x`, its w-contact is
`v+(u/epsilon)(delta-epsilon-1)`, the asserted radius. Substitution in an
unchanged polynomial value multiplies its order by `u/epsilon`. The strict
inequality `delta>epsilon` makes this a transverse invertible change at the
disc: leading root multiplicities, squarefreeness, and separation of the f/g
leading roots are preserved. This last hypothesis is essential.

The printed input for the orders is M Prop.4.6, p.170, and its p.171 Remark:
`lambda_f=m(delta-H)/(n-M_i)`, with the appropriate generation's data. X Lemma
4.1 has right side `-J(t^(-1),alpha)t^(-2)`. For `J=C x^ell` it has order
`-ell-2`; the nonzero final determinant gives

```
delta = H + lambda_f + lambda_g,
final major: delta < H;       zero-order minor: delta > H.
```

See [X Lemmas 4.1–4.4](/home/ubuntu/jc2/box/descent-partition-20260906/xu.txt:190)
and [M p.171 Remark](/home/ubuntu/jc2/box/descent-partition-20260906/moh.txt:1711).
Substitution of the local rule gives
`delta'=H+(u/epsilon)(lambda_f+lambda_g)` for a parent final major.
Thus the shift is checked against the actual changed radii and orders.

**What happens to the other packets.** The same transverse rule applies to a
nonprincipal minor packet whose first nonzero centre precedes its final split.
Its two orders remain zero, and `delta'>H`. Two other cases require separate maps.

At the principal direction `y~b/t`, inversion preserves projection order one.
If its parent contact is delta, its image over the **finite** child base point
`gamma=0` has radius `u delta-v`, the same number of roots, and gamma-orders
multiplied by u. The nominal principal endpoint `delta=v/u` therefore maps to
radius zero. It does not become a child infinity packet. The polynomiality and
monicity assertions on pp.197–198 are proved in this finite chart.

A parent zero-centred minor packet can have its **first nonzero term at the
final radius itself**, `epsilon=delta>1`. Then the transverse formula cannot
be applied with the old per-disc root count. In centred coordinates its leading
fibre polynomial changes by Newton inversion, schematically
`f_sigma(a w^epsilon)-xi`; the transformed radius is `v-u/epsilon` and the
root count must be read from that polynomial. For the unsplit single zero
packet in R050 this gives `rho'_f=epsilon rho_f=4`, not 2. In general the joint
leading polynomials and their orbit data, not just the three numbers
`(rho_f,lambda_f,delta)`, are needed to perform this endpoint operation.

There can also be roots with `x -> x_0` finite when `y=T^u -> 0`. They form a
child packet at radius v about h(T), with leading polynomial
`f(-w/b,0)-xi` after the radius-v rescaling. Its count is
`r_0=deg_x f(x,0)`, with zero count if this polynomial is constant. For generic
target values it is squarefree and has zero g-order on all its roots. These are
new **minor** roots of the infinity partition, supplied by a finite parent line.
They have no parent packet at `x=infinity`. R009 has `r_0=2`; R050 has `r_0=0`.

Bare triples therefore do not determine the entire child partition. One also
needs centres, conjugacy, endpoint leading polynomials, and the finite-line
remainder. The latter supplies no major term: at finite x, polynomial g has no pole.

**The theorem and its quantifiers.** On the reduced source locus of the charged
instrument, every actual final major has an earlier first nonzero centre with
`0<epsilon<delta`. A nonzero finite limiting y-value would map an x-pole to a
finite nonzero gamma-value, contradicting monicity in pi. A final major with
the whole preceding centre zero is excluded by Moh Prop.5.6, pp.188–190, in
the reduced setting. This is why `descend_own` explicitly excludes the all-zero
bottom route; it is not an extra denominator invented for this report.

Apply the transverse rule to all the remaining major orbits. Their contributions
obey the exact identity

```
-N' rho'_f lambda'_g
  = -(epsilon N) rho_f (u/epsilon)lambda_g
  = u (-N rho_f lambda_g).
```

Every child root with a pole of G has `x -> infinity`, since G is the pullback
of a polynomial g. It therefore comes from one of these parent major orbits;
parent minor roots have order zero and cannot supply a pole after reparametrizing.
This proves **major-orbit transport**, with no missing major packets:

```
I'_M = u I_M.                         In particular u=1 gives I'_M=I_M.
```

There is also a global proof for generic intersection numbers which needs no
child analogue of Xu's minor inequality. On `gamma!=0`, Phi identifies the
child chart with the cover of `y!=0` obtained by adjoining `gamma^u=y^(-1)`.
Its function-field degree is u: `y^(-1)` is not a nontrivial power in `k(x,y)`.
For a generic target `(xi,eta)`, no parent intersection lies on `y=0`, and no
child intersection lies on `gamma=0`. The latter follows because `G(0,pi)` is
monic and has finitely many roots, whose F-values cannot equal generic xi.
Hence the u-sheeted chart cover multiplies the intersection length by u.
Monicity in the root variable makes each length the degree of the corresponding
resultant. This extends the field-degree argument in X Cor.4.8 without applying
that corollary's Keller hypothesis to the child.

For clarity about a fixed exceptional fibre, the chart argument has the boundary
formula `I(F-xi,G)=u(I(f-xi,g)-B)`, where B is the parent intersection length
on `y=0`; the child boundary length at `gamma=0` is zero for generic xi.
For generic g-translation B=0. Generic translation does not change any negative
g-order, hence does not change either major sum. A claimed unshifted child norm
must include any positive-order roots if an exceptional fixed fibre is retained;
the p.171 shift alone cannot discard them. The controls below have zero-order
minor packets and no such correction. No cover division is hidden in Xu's degree.

This compares a **pair and its image**, or jointly compatible root data.
Independently enumerated necessary configurations need not be images of one
another. A child test can cut an outer set of parent data even though every
realized pair satisfies transport. Such an exclusion would not refute this
theorem; nor does the theorem license replacing an unverified child's computed
value by its parent's. This is FALLACY-v2's configuration/pair distinction.

**R009: all counts and orders under the map.** The charged gate pins the source
pattern, with degrees `(192,128)`, `M=(-128,148,190)`, `V=(2,3)`, and first
nonzero radius `epsilon=5/16`. Here `(u,v,H)=(1,3,2)` and child degrees are
`(48,32)`, with `M'=(-32,37)`. The following are actual packet counts in the
necessary pattern, not counts divided by a Puiseux cover.

| Parent packet | Parent count × rho_f; delta | Child count × rho_f; delta | Child (lambda_f,lambda_g) |
|---|---|---|---|
| Final majors | `16 × 4; 19/24` | `5 × 4; 4/3` | `(-4/15,-2/5)` |
| Nonprincipal minors | `16 × 2; 21/16` | `5 × 2; 3` | `(0,0)` |
| Principal minor | `1 × 32; 3` | finite `gamma=0`, radius `0` | zero orders at the endpoint |
| Finite parent line | no parent infinity packet | `1 × 2; 3` | `(0,0)` |

The leading relation `y^16=c t^5` becomes a degree-5 equation for w with
leading order `-1/5`. More fully, the inverse-top count is
`16-5(2+1)=1` for the zero **reduced** multiplicity. Thus the child's top
pattern is `pi (pi^5-a)^2 (pi^5-b)`, up to nonzero coefficient normalizations.
Its f-root count is `2+20+10=32`.

The final major sum is `5*4*(2/5)=8`. Its shifted radius expression is
`(48/80)*5*4*(2-4/3)=8`. The minor zero packet is genuinely supplied by
`deg_x f(x,0)=2`; calling it the image of the principal packet would assign
32 roots to a 2-root object. Parent and child have respectively 33 and 11
final packets in this description, while both major sums equal 8.

**R050: the zero minor endpoint changes its count.** Here the source has
degrees `(196,56)`, `M=(-56,184,194)`, `V=(4,3)`, first nonzero radius `1/4`,
and pattern `pi (pi^4-a)^4 (pi^4-b)`. The child has degrees `(49,14)`,
`M'=(-14,46)`, and the same `(u,v,H)=(1,3,2)`.

| Parent packet | Parent count × rho_f; delta | Child count × rho_f; delta | Child (lambda_f,lambda_g) |
|---|---|---|---|
| Final majors | `4 × 8; 19/28` | `1 × 8; 5/7` | `(-2/7,-1)` |
| Nonzero minor orbit | `4 × 2; 2` | `1 × 2; 6` | `(0,0)` |
| Zero minor endpoint | `1 × 2; 2` | `1 × 4; 5/2` | `(0,0)` |
| Principal minor | `1 × 14; 3` | finite `gamma=0`, radius `0` | zero orders at the endpoint |

The inverse-top zero reduced multiplicity is `7-1(4+1)=2`, giving
`pi^2(pi-a)^4(pi-b)`. Translating the leading coefficient variable gives the
replay's multiset `(4,2,1)`; this changes which root is distinguished as zero.
The zero minor endpoint has first nonzero exponent 2, so Newton inversion
doubles its f-degree. There are no remaining finite-line roots: `8+2+4=14`.
The sum is `1*8*1=8`, also `(49/63)*8*(2-5/7)=8`. Parent and child packet
counts are 10 and 3. Equal intersection numbers have not produced a bijection.

**R063: what can actually be recomputed from the frozen description.** The
replay supplies `(n',m')=(42,28)`, effective `s'=3`, `ell=1`, `V'=(3,7)`, and
`p'_2=pi^5(pi^A-c)^3`. It supplies neither the M-vector nor the source row.
Those assertions are nonetheless restrictive enough for a consistency audit.

Since `d'_2=gcd(42,28)=14`, the degree equation is
`7*14/d'_3=5+3A`. A characteristic divisor `d'_3` is a proper divisor of 14
greater than 1. The only solution is `d'_3=7`, `A=3`, `P'_2=14`.
The claimed `V'_3=7` equals `d'_3`; all p'_3 multiplicity is therefore in its
selected factor. The own map has a zero centre above level 2. Applying the
charged H-scaled Def.5.1 formula gives

```
delta'_2 = -2/(41-M'_2),
M'_2 = 35, delta'_2=-1/3,
M'_3 in {36,37,38,39,40}.
```

The last list exhausts the effective possibilities; 41 would be the dropped
`n'-1` tail. The true zero-centre stabilizer is 1. The child order at D'_2 is
`lambda'_f=28(-1/3-2)/(42-35)=-28/3`. The exact shifted unsplit calculus gives:

| Child leaf forced by the literal pattern | Count × rho_f | Final delta | lambda_f | lambda_g | Total major term |
|---|---|---:|---:|---:|---:|
| Selected nonzero orbit, multiplicity 3 | `3 × 6` | `7/6` | `-1/3` | `-1/2` | `9` |
| Zero sibling, multiplicity 5 | `1 × 10` | `13/24` | `-7/12` | `-7/8` | `35/4` |

Thus **71/4 is correct for that literal numerical child pattern**, with ell
included. The zero child sibling is not a
valid final Galois packet: its actual radius denominator is 24 and the two
leading degrees are 10 and 15, neither 0 nor 1 modulo 24. That is a failed
necessary completion, not a witnessed descendant partition.

Now invert the descriptor using the charged own-data rule. `ell=1,u=1` forces
`v=3,d_s=4`, hence parent degrees `(168,112)`, with
`M=(-112,140,4M'_3,166)`, `d_3=28`, `V_2=3`, `V_4=3`.
At parent level 3, `P_3=21` and `delta_3` is respectively
`5/17,2/7,3/11,1/4,1/5`. A first nonzero selected root of multiplicity 7
cannot fit its denominator orbit: even the smallest denominator is 4 and
`4*7>21`. On the zero route the printed/instrument inversion count is

```
V'_3 = 7-delta_3(21-V_3).
```

Consequently `V'_3=7` forces **`V_3=21` in every case**. The entire level-3
factor is zero. Def.5.1 then gives `delta_2=3/10`, `P_2=42`, `A_2=10`, and
threshold `d_2/(n-M_2)=2`. With a selected multiplicity 3 there are only two
degree possibilities: zero 12 with orbit `(3)`, or zero 2 with orbits `(3,1)`.
The latter is forbidden equality at the threshold. The only pattern is
`p_2=pi^12(pi^10-c)^3`.

This inferred parent's complete forced major arithmetic is

| Inferred source leaf | Count × rho_f | Final delta | lambda_f | lambda_g | Total term |
|---|---|---:|---:|---:|---:|
| Selected nonzero orbit | `10 × 6` | `3/4` | `-1/10` | `-3/20` | `9` |
| Zero sibling | `1 × 24` | `24/59` | `-14/59` | `-21/59` | `504/59` |

Therefore `I_M=9+504/59=1035/59`, **not 19**. There is no unexamined major
level below this sibling: it is born at level 2, and M Prop.5.3 sends it to
level 1. It also fails its denominator-59 finality condition, with f/g counts
24 and 36. The selected orbit, which is a legitimate transverse calculation,
does transport its contribution 9 exactly. The mismatching zero arrays are
already invalid as final root configurations.

These are outer first-support possibilities only. Every one fails whole-source
completion, so none supplies the replay's asserted `NONEMPTY` own route.

All five descriptor-compatible source possibilities contradict 19. At least one
degree/ell/V/pattern/source-value identification is wrong or incomplete. The
frozen description does not identify which one. I requested the omitted R063
row while continuing; none was available when this report was sealed.

**Promotion and affected rows.** Promote the declared map, the corrected
Jacobian monomial, the strict-sector packet rule, and major-orbit transport
`I'_M=u_s I_M` on actual reduced licensed images. Promote the R009/R050 checks
with their different packet counts. Do not promote a full packet bijection,
equality without the factor u on a ramified descent, or equality of independently
filtered configuration sets.

Do **not** promote a new R063 kill or a corrected child partition with value 19.
The minimal missing data are its verified parent `(n,m,M,V)`, complete parent
pattern with actual centre stabilizers, and the correlated own-child route and
full child pattern. These resolve the exhibited numerical inconsistency; no
polynomial witness is required merely to test a necessary exclusion afterward.
The exact fixed-fibre norm also requires the boundary/positive-order accounting
stated above, not an unproved extension of Xu's minor inequality.

All actual `u_s=1` images among the replay's 46 rows obey transport. The reported
differences on **R001, R002, R003, R010, R013, R019, R020** compare different
minor filters (R001) or uncorrelated extra child configurations (the other six).
They need a joint-image audit. **R025–R028, R057, R058** retain the charged
gate's sibling-completion correction: the replay's “neither integer” used the
rejected flat parent sums. No additional row is excluded or residual count changed.

**Verification and FALLACY-v2.** Run `python3 box/descent-partition-20260906/check.py`.
It loads only four pure helper definitions by AST from the verified frozen
`descend_own.py`; it does not import the uncharged `own_v_routes` dependency or
claim to run its full route engine. Exact Fraction checks verify both named
controls, their root totals, radius and order transformations, the factor-u
control at u=2, and all five possibilities in the literal R063 audit. Negative
controls retaining parent disc counts give `128/5` on R009 and 32 on R050,
exposing why an ell shift without a count transformation proves nothing.

Roots, discs, conjugacy orbits, characteristic conjugates, and affine places
are separately typed throughout. Unsplitting at an endpoint is checked in the
pinned controls; bare minor floors are not called attained partitions on other
rows. Every variable/field map used in the theorem is explicit. There is no
new exit-price assertion, so no `charge_basis` declaration applies. The result
on the requested complete formal-row decision is
`OPEN[R063-FROZEN-DESCRIPTOR-INCONSISTENCY]`, with the major transport theorem
proved on its stated image domain.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21598`.
- Body SHA-256:
  `39d748370d7b8e52c3d4b4f62cb29de4bb1612aef52fdba867b77c7f65e0ed80`.
- Frozen basis: `5cd6acd5c1de9379ec42e1e682c6fc90fffaa9d8`.
