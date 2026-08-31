# Hostile review: wild one-cusp valuation and completion structure

Date: 2026-08-31 UTC
Reviewer: Grok 4.6 (independent different-model adversarial referee)
Charged packet (frozen copy): `block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md`
Producer: Sol 5.6 Ultra, lane `wild_valuation_structure`
Packet frozen lane basis named in the file: `1d97e7b76b9e53d849588cd678f47468bedd5de0`

No charged file was edited. No canonical ledger was edited. `jc2-lean` was not inspected. No CAS was used. Arithmetic is desk-level. No exit price is asserted.

## 0. Disposition

The packet is a conditional valuation/completion lemma for the exact ring
`R=C[A,U,Z]/(U^2-A-A^2 Z)` carrying a quartic Keller pair, not a mixed/mixed
horn exclusion. At that stated scope every charged identity survives the
attacks below. The Poisson parent was promoted on 2026-08-31; labels
`PROVISIONAL` on its consumed conclusions may be relabelled. Inverse-Kummer
identities remain provisional inputs.

```text
completion R^_P = C[Z][[u]], orders, bracket (1.3)     CONFIRMED
associated-graded (1.4)--(1.6); unimodular (1.9); (1.10) CONFIRMED
cusp-companion rectification (1.11); infinite-jet wildness CONFIRMED
generic boundary (1.12)--(1.15); independent NLF witness CONFIRMED
flow divisor (2.1), iterates (2.4)/(2.6), RH (2.5)     CONFIRMED
necessary tuples §3.1, table, closures (3.6)           CONFIRMED
inverse-Kummer collision is not a place of (2.1); (3.10) CONFIRMED
maximum-safe list and OPEN typing                      CONFIRMED
declared scope (horn remains open)                     CONFIRMED
```

Hardest failed attack: vanishing of `prod_(i=0)^(j-1)(k-2i)` in (1.15).
For `k<0` every factor is negative, so the product never vanishes in
characteristic zero; regular and residue-field corrections to the principal
part `s^(-1) partial_s` drop strictly less than 2 and cannot cancel the
leader. Next hardest: a general `{f=a_f}` forced through `sing(Y)` or tangent
to `B`. Isolated singularities of the normal surface `Y` and the polar
`V(b,b_g)` are finite, hence avoidable.

## 1. Custody

Frozen SHA-256 values were reproduced before mathematical reading.

```text
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5
  .../block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
cd27b7f6687103fae0fc4e5fe19772e0f8e62939d73a655ebf04e57905ddba05
  .../block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190
  .../block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  .../block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
```

All four matched. The unique body of the charged valuation packet through its
first standalone body-end marker (including that marker's terminating newline)
is the whole file: 24686 bytes, SHA-256
`2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5`.

Parent non-local-finiteness, hyperbolic generic fibres, and the degree-four
étale fibre ledger are consumed as promoted. Function-pair collision,
immersive normalisation of `C_0`, and the `(2,1,1)+(3,1)+(2,2)` census are
consumed as reviewed. Inverse-Kummer sheet equations remain provisional
interface, not a conclusion of this review.

## 2. Completion isomorphism, orders, and bracket (1.3)

**Verdict: CONFIRMED.**

Let `q=U^2-A-A^2 Z` and `P=(A,U)`. In the `(A,U)`-adic completion of
`C[A,U,Z]` one has `R/P=C[Z]` and `q_A=-1-2AZ`, which evaluates to `-1` along
`P` and is a unit in `C[Z][[A,U]]`. The formal implicit-function theorem
supplies a unique zero-constant-term solution `A=a(u,Z)` of `A+Z A^2=U^2`.

The quadratic formula yields two roots. The root with the minus sign before
the square root is `-1/Z+O(U^2)`, not in the completion. The retained root is

```text
a(u,Z)=(sqrt(1+4 Z u^2)-1)/(2Z)
      = 2 u^2 / (1 + sqrt(1+4 Z u^2)).
```

The second expression is visibly regular at `Z=0`. Expanding
`sqrt(1+x)=1+(1/2)x-(1/8)x^2+(1/16)x^3-(5/128)x^4+...` with `x=4 Z u^2`
reproduces the displayed jet

```text
a = u^2 - Z u^4 + 2 Z^2 u^6 - 5 Z^3 u^8 + ...
```

so `a in (u^2)` and `(a,u)=(u)`. Therefore `R^_P=C[Z][[u]]` with
`U |-> u`, and the generic-point completion is the DVR `C(Z)[[u]]`. Closed
points `p_(z0)=(A,U,Z-z0)` give `C[[u,w]]`, `w=Z-z0`. Orders
`ord_P(U)=1`, `ord_P(A)=2`, `ord_P(Z)=0` are the orders of `u`, `a`, and `Z`
in that DVR.

The cyclic chart `A=x^2`, `U=x+x^3 y`, `Z=2y+x^2 y^2` is not used: it only
corroborates the same orders along `x=0`. Direct substitution confirms it
satisfies `q=0`.

Poisson parent brackets give `{U,Z}=2+4 A Z`. Substituting the series
produces `{u,Z}=B` with `B=2+4 Z a=2 sqrt(1+4 Z u^2)`, a unit of
`C[Z][[u]]` because `B=2+O(u^2)`. For coordinates with `{u,Z}=B`,

```text
{F,G}=B(F_u G_Z - F_Z G_u),
X_H=B(H_u partial_Z - H_Z partial_u),
```

which is (1.3). Both Hamiltonian fields therefore extend to derivations of
the completion and may drop the `u`-adic filtration by one (`partial_u`
drops by one; `B` and `partial_Z` do not).

## 3. Associated-graded identities, unimodular relation, symbols

**Verdict: CONFIRMED.**

Write `F=h(Z) u^m + O(u^(m+1))`, `G=k(Z) u^n + O(u^(n+1))`, and `B=2+O(u^2)`.
Then

```text
F_u G_Z - F_Z G_u = (m h k' - n h' k) u^(m+n-1) + O(u^(m+n)),
```

so multiplying by `B` yields the floor (1.4) and the initial form (1.5)

```text
in_(m+n-1){F,G} = 2(m h k' - n h' k) u^(m+n-1).
```

(The prime is `d/dZ`, as the packet states.) If `m=n=0` the displayed
`u^(-1)` coefficient is identically zero, so the floor need not be attained;
that is why (1.4) is only a floor. Iterating `{H,-}` gives (1.6) as a floor,
with equality only while successive initials survive.

Every element of `R` has unique shape `H=P_H(A,Z)+U Q_H(A,Z)` because `R` is
free of rank two over `C[A,Z]`. The promoted parent theorem `X_H` locally
finite iff `H in C[A]` rewrites as (1.8). There is no universal eigenweight:
`H=Z` has order zero and `H=U^N` has order `N`. Non-local-finiteness alone
cannot upgrade (1.4) to an attained growth law.

For the charged pair, `{f,g}=kappa` is order zero. The order-zero coefficient
computed from linear jets is exactly (1.9):

```text
2(f_1 g_0' - f_0' g_1)=kappa.
```

Hence `(f_0',g_0')` never vanish simultaneously, so `Z |-> (f_0(Z),g_0(Z))`
is an immersion `Phi=A1 -> C_0`. The reviewed function-pair theorem supplies
distinct `z,z'` on `Phi` with the same image, and identifies the map with the
immersive normalisation of `C_0`. A constant coordinate would place `C_0` in
a line, contradicting Chau singularity of the asymptotic image. An affine
(degree-one) coordinate would be injective on `A1` and would separate
`z,z'`. Thus `deg f_0, deg g_0 >= 2`. (The unibranch-cusp alternative is
already excluded by immersivity of the parametrisation; the collision is
multibranch.)

Generically along `Phi` both Hamiltonians have order zero, and the degree
`-1` symbols are (1.10). Attack: `partial_u` is not locally nilpotent on
`C[Z][[u]]`. The claim is about the associated-graded ring `C[Z][u]`, where
`-2 f_0'(Z) partial_u` is locally nilpotent. No nonzero formal eigenvalue
appears. The cited invariant-ring control (étale first jet along `Phi`,
arbitrary polynomial restrictions) is consistent and is not used as a
premise of (1.9)--(1.10).

The three completions of §1 of the packet (`Phi` inside `S`, ramification
boundary `R_bd=Y-S`, deleted cyclic lines `L_j`) are correctly refused
identifications. Interface check against the function-pair coordinator
(lines 82--105, 114--144) and cyclic source (140--180, 205--242) matches.

## 4. Cusp-companion rectification (1.11)

**Verdict: CONFIRMED.**

The target cusp `c` is not a point of `S`. The unique interior companion
`u_c in T=pi^(-1)(B) cap S` is supplied by the cyclic packet (lines 427--439),
which leaves `u_c in Phi` versus not open. Since `pi|_S` is étale, `p=f-f(u_c)`
and `q=g-g(u_c)` are regular parameters, so `O^_(S,u_c)=C[[p,q]]`. Then
`X_f(p)=0`, `X_f(q)=kappa`, hence `X_f=kappa partial_q`, and likewise
`X_g=-kappa partial_p`. This is (1.11).

Attack: translations are locally finite on polynomials, so a finite-jet
eigenvalue or the Newton polygon of the pulled-back polynomial cusp germ
`b(f(u_c)+p,g(u_c)+q)=0` cannot detect global non-local-finiteness. That germ
is a polynomial in `(p,q)` and has a finite `partial_q`-orbit; it cannot be
the witness. The actual obstruction is infinite-jet: a derivation of the
finitely generated algebra `R` is locally finite iff the orbits of `A,U,Z`
are finite-dimensional, iff each generator, as an element of `C[[p,q]]`,
satisfies a nonzero constant-coefficient ODE `P(kappa partial_q)=0`, iff it
is a finite exponential polynomial
`sum_lambda sum_(j<m_lambda) a_(lambda,j)(p) q^j exp(lambda q/kappa)`.
Global wildness is the negation for at least one generator. Reading "no
local invariant" as "no finite-jet local invariant of the cusp germ" makes
the claim exact; the infinite jet is local in the formal-neighbourhood sense
but is not a finite-jet invariant.

The cubic algebra with discriminant `s^3-w^2` in the Kummer packet
(546--575) is a compatibility control for fibre lengths, not an equation of
the charged length-three completion. Leaving that completion `OPEN` is
correct, not a hole.

## 5. Generic boundary (1.12)--(1.15)

**Verdict: CONFIRMED.**  The redundant second non-local-finiteness proof
holds. The leading-coefficient product and the linear-independence step
survive.

At the generic point of irreducible `B` the fibre is `(2,1,1)` (branch
topology 100--104; companion threat-map 213--227, 263--303). After completed
strict henselisation of the DVR, tame ramification of index two in
characteristic zero is the chart (1.12): `K[[b]]->K[[s]]`, `b |-> s^2`, up
to units absorbed into the uniformiser. The cited lines display the divisor
form `div_Y(pi^* b_i)=2 R_i + S_i` and the different `sum R_i`; the DVR
chart is the standard consequence, not an extra computation.

`B` is not a coordinate line (it carries a cusp). If `b_g` vanished
identically as a polynomial, `B` would be a vertical line. If `b` divided
`b_g`, degrees would drop. Hence `b_g` (and likewise `b_f`) is a unit at the
generic point of `B`. Hamiltonian identities `X_f(b)=kappa b_g` and
`X_g(b)=-kappa b_f` therefore have valuation zero. With `v(s)=1` and
`X_f(s^2)=2 s X_f(s)` of valuation zero, the principal part is (1.13): a
degree `-2` symbol `c s^(-1) partial_s` with `c=(kappa overline(b_g))/2` in
`K^*`. Then `v(D^j s)=1-2j` for all `j>=1`, which is (1.14).

Existence of `h in O(S)` with `v(h)=k<0`. The valuation `v` is the DVR of
the function field at the generic point `eta` of a component of `R_bd=Y-S`.
Its unique centre on the separated scheme `Y` is `eta`. If `v>=0` on all of
the affine ring `O(S)`, the prime `{x in O(S): v(x)>0}` would be a centre
on `S`. Because `S` is open in `Y`, that centre would also be a centre on
`Y`, distinct from `eta`, contradicting uniqueness of centres. Thus some
`h` has `k<0`. (`Y` is the finite normalisation of `A^2` in `k(S)`, hence
separated and normal; singularities are isolated and unused here.)

Leading coefficient of `D^j h`. In `K((s))` write `h=alpha s^k + O(s^(k+1))`
with `alpha in K^*`. The principal part `D_prin=c s^(-1) partial_s` sends
`s^k` to `c k s^(k-2)`. Inductively

```text
D_prin^j h = alpha c^j (prod_(i=0)^(j-1) (k-2i)) s^(k-2j) + higher.
```

A holomorphic correction is `a(s) partial_s` with `a(0)` finite, hence drops
valuation by at most 1. A residue-field derivation of `K` applied to the
leading coefficient produces a term of valuation `k`, strictly greater than
`k-2`. Any insertion of a non-principal summand therefore cannot cancel the
principal-part leader.

The product `prod_(i=0)^(j-1)(k-2i)` vanishes iff `k=2i` for some
`0<=i<=j-1`, iff `k` is even and `0<=k<=2(j-1)`. This is impossible for
`k<0`. Characteristic zero is used (no vanishing of the integer `k` itself
as a coefficient). Thus `v(D^j h)=k-2j` exactly, which is (1.15).

Linear independence. The valuations `k, k-2, k-4, ...` are strictly
decreasing, hence distinct. A `C`-linear relation among the iterates would
have a unique most polar term. Local finiteness of `X_f` on `R` would make
the orbit of `h` finite-dimensional. Contradiction. The same for `X_g`.

Independence of the automorphism/LND theorem is real: the argument uses the
constant Jacobian (so `X_f(b)=kappa b_g`), the reviewed `(2,1,1)` tame
boundary, affinity of `S`, and separatedness of `Y`. It does not use the
Dubouloz--Palka automorphism formula. The slogan "from the reviewed boundary
packet alone" is slightly tighter than the ingredients: the constant
Jacobian is used, and is displayed in the same section. That is a wording
tightening, not a gap in the proof. Blast radius zero.

FALLACY-v2 floor/attainment: (1.14) and (1.15) are equalities with displayed
leaders, not floors. Pole identities are applied at the generic point of a
boundary divisor, after the vertex class (tame index two) is checked.

## 6. Flow divisor, iterates, Riemann--Hurwitz

**Verdict: CONFIRMED.**

Consume the promoted statement: for general `a_f` the map `g: C_f=V(f-a_f)->A1`
is surjective étale of degree four. Let `Cbar_f` be its smooth projective
completion, genus `gamma_f`, punctures `Sigma=Sigma_infty sqcup Sigma_fin`.

At a finite deleted place choose a uniformiser with `g-g(p)=z^e` exactly in
the completion (extract an `e`-th root of the unit in characteristic zero).
Then `D(g)=kappa` forces `D=(kappa/e) z^(1-e) partial_z` exactly in that
coordinate, not merely to leading order. At infinity, `g=z^(-e)` likewise
gives `D=-(kappa/e) z^(e+1) partial_z`. There are no zeros or poles on
`C_f` because `g` is étale there (`e=1` and `D(z)` is a unit). This is
(2.1) with attainment at every place: zeros of multiplicity `e_p+1` over
infinity, poles of multiplicity `e_p-1` at finite deleted points.

The iterate formulae (2.4) follow by induction on the exact local fields
just obtained. The finite product `prod_(i=1)^(j-1)(1-i e)` vanishes iff
`e=1/i` for some positive integer `i`, hence iff `e=1` at `i=1`. At a
finite ramified point `e>=2` it never vanishes, so
`ord_p(D^j z)=1-j e` exactly. The infinity product `prod(1+i e)` never
vanishes.

Riemann--Hurwitz for a degree-four map `Cbar_f -> P1`, all ramification in
`Sigma`:

```text
2 gamma_f - 2 = -8 + sum_all (e_p-1),
sum_infty e_p = 4,     sum_infty (e_p-1)=4-r_infty,
sum_fin (e_p-1)=2 gamma_f + 2 + r_infty.
```

Degree of zeros of `D` is `sum_infty (e_p+1)=4+r_infty`. Degree of poles is
the finite sum just displayed. Difference `2-2 gamma_f` matches `deg K`.
This is (2.5). The finite ramification sum is at least 2, so a finite
ramified point exists.

For (2.6): Riemann--Roch gives, for large `M`, a nonconstant section of
`O(M p)`, hence `h in O(C_f)` with its only pole at that finite ramified
`p`. (Functions with a single pole at `p` are holomorphic at the other
punctures, hence lie in `O(C_f)`.) In the exact coordinate of (2.2),

```text
D(h)=(kappa/e) z^(1-e) * (-M alpha z^(-M-1)+...)
```

has order `-M-e`, and the new leading coefficient is a nonzero multiple of
`-M`. Subsequent factors are `-(M+i e) != 0`. Thus
`ord_p(D^j h)=-M-j e` for all `j`. Attack: iterates may acquire poles at
other finite punctures because `D` itself has poles there. That is true and
harmless: `O(C_f)` permits poles at all of `Sigma`, and linear independence
only needs strictly decreasing order at `p`. Local finiteness on `R` would
descend to `R/(f-a_f)` because `X_f(f)=0` stabilises the ideal. This is a
second global non-local-finiteness witness, from the degree-four fibre
rather than from the automorphism classification.

FALLACY-v2: a valuation floor is not treated as attainment; (2.1), (2.4),
and (2.6) carry uniformiser witnesses. Flags, places, and cover series are
not identified.

## 7. Necessary tuples, table, and closures (§3.1)

**Verdict: CONFIRMED.**  The genericity choice can avoid a fibre through a
singular point of `Y` and can avoid tangency to `B`.

Reviewed census: generic `B` fibre `(2,1,1)`, cusp `(3,1)`, omitted node
`(2,2)`, `e(T)=-3`, `B` irreducible, normalisation `beta_B: A1 -> B`
(topology 100--104, 213--227; companion 205--256). One place at infinity of
`B` is the content of topology (2.1): finite points of a source `P1` map
into the affine curve, so the affine normalisation is `A1`. Then
`f o beta_B` is a polynomial, and `d_f` is its degree (equivalently the pole
order at that unique infinite place).

Bad values of `a_f` are finite in number:
- `f`-coordinates of `c`, `n`, and any other singular points of `B`;
- critical values of the polynomial `f o beta_B`;
- `f`-coordinates of `sing(Y)`, a finite set because `Y` is a normal
  surface (finite normalisation of `A^2`), hence has isolated singularities;
- values at which `{f=a}` is tangent to `B`, i.e. points of `V(b,b_g)`.
  This scheme is finite unless `b_g` vanishes on `B`, already excluded.

A Zariski-general vertical line therefore meets `B` only at ordinary
`(2,1,1)` points, transversely, and misses `sing(Y)`. At each such point the
completed base change is `C[[b,t]]->C[[s,t]]`, `b |-> s^2`. Transversality
makes `g-g(p)` a unit times `b`, hence a unit times `s^2`, so the curve
normalisation has local index two. The only finite deleted points of
`gbar: Cbar_f -> P1` are those ramified points of `Y` (companions remain in
`S`, hence in `C_f`). Distinct ordinary points of `B` give distinct ramified
points. Thus `e_p=2` for every `p in Sigma_fin` and `s_fin=d_f`, which is
(3.1).

Substitute into (2.5): `sum_fin (e_p-1)=s_fin=d_f=2 gamma_f + 2 + r_f`,
which is (3.2). Pole orders of `g` over infinity are the parts of a
partition `lambda_f` of 4 of length `r_f`. The four rows are exactly the
positive partitions of 4:

| `r_f` | `lambda_f` | `d_f` |
|---:|---|---:|
| 1 | `(4)` | `2 gamma_f + 3` |
| 2 | `(3,1)` or `(2,2)` | `2 gamma_f + 4` |
| 3 | `(2,1,1)` | `2 gamma_f + 5` |
| 4 | `(1,1,1,1)` | `2 gamma_f + 6` |

No length-zero row: `sum_infty e_p=4` forces `r_f>=1`. Necessity, not
attainment, as stated. Then `d_f>=3` and `d_f-r_f-2=2 gamma_f in 2 Z_(>=0)`.
Euler of the affine fibre:
`e(C_f)=(2-2 gamma_f)-(d_f+r_f)=-4 gamma_f-2 r_f<0`, matching the promoted
hyperbolic-fibre statement. Interchanging coordinates gives (3.5). No
relation between the two genera or partitions is claimed.

Closures (3.6) are exactly the numerical failures of (3.2)--(3.5). They do
not exclude any tuple that passes the table. Orientation checks: `d_h=3`
forces `(gamma_h,r_h,lambda_h)=(0,1,(4))`; `d_h=4` forces genus zero,
`r_h=2`, and `(3,1)` or `(2,2)`. The packet's `PROVISIONAL` tag on the table
was pending the parent's different-model review; that review has confirmed
the degree-four étale generic fibre, so the tag may be dropped. The
derivation of the table from (2.1) plus `(2,1,1)` plus transversality does
not use the automorphism classification.

## 8. Inverse-Kummer collision (§3.2)

**Verdict: CONFIRMED** that the collision is not a place of (2.1) and does
not change any `e_p`; **CONFIRMED** the valuation identity (3.10) as desk
algebra from (3.9). Sheet equations (3.8)--(3.9) remain consumed
provisional interface.

The model identification `(mu, r_pp)=(2,2)` is the promoted Poisson ring.
Minimal-degree comparison in the reviewed function-pair packet gives
`mu=d1=2`, which is (3.7). Inverse-Kummer identities (3.8) and the local
difference `J_t=u^2-v^2` are quoted from the still-provisional successor;
this review does not promote them.

Granting (3.9), let `w` be a rank-one valuation centred at the collision
with `w(u)=alpha>0`, `w(v)=beta>0`. If `alpha<beta` then `w(u^2)<w(v^2)` so
`w(J_t)=2 alpha=2 min(alpha,beta)`; symmetrically if `beta<alpha`. If
`alpha=beta` then `w(u^2-v^2)>=2 alpha`, with equality unless the initial
squares agree. This is (3.10). In the transverse stratum `(u,v)` are regular
parameters and the Newton segment is `conv{(2,0),(0,2)}`; the tangent
stratum keeps (3.10) but does not determine the Newton polygon in a chosen
regular system. Off `B`, `Disc(P_t)` of the monogenic order has even
valuation at least `2 w(J_t)`, with equality if no other sheet difference
vanishes; the discriminant of the finite-étale normalisation remains a unit.
That is order-index, matching Kummer (4.7) and (4.8)--(4.9).

The collision is never a place of (2.1). Reviewed alternatives (cyclic
328--342; Kummer 249--289) are exactly (3.11): `L0` off `B`, or `L1` an
ordinary `(2,1,1)` point of `B`, never the cusp or node. In `L0` both
preimages are interior étale points of `S`. In `L1` they are the two
interior companions; the ramified boundary point is a third, distinct
point. Generic `{f=a_f}` moreover misses the collision value. So `J_t`
records failure of a primitive element to separate étale sheets, not a new
deleted point and not a change of any `e_p`.

Euler ledger (3.12) is the coordinator identity (0.1) at `mu=2`:
`e(D_B)=-6-N` and the orbit sum `N+3`. Bounds `N>=epsilon_c` and, in `L1`,
`N>=2+epsilon_c` follow because the collision is distinct from `c`.
Equations (2.1) and (3.12) count different curves; no term transfers.

## 9. Maximum-safe conclusions and OPEN typing

**Verdict: CONFIRMED.** No proved-labelled line hides an unproved
statement. No charged wording closes the horn.

1. Completion, (1.3), (1.5), (1.9), and local nilpotence of (1.10) are
   proved on the ring. Relabel the model identification from `PROVISIONAL`
   to consumed-promoted. Degree `-1` symbols still do not detect wildness.
2. Formal translations at `u_c` are proved. The length-three ramified
   completion is correctly `OPEN`.
3. Degree `-2` generic-boundary symbols and (1.15) are proved. This is an
   independent non-local-finiteness witness, not using the automorphism
   formula. Relabel "PROVISIONAL globally wild" to wild.
4. (2.1) and (2.4) are exact. Closures (3.6) are the only numerical kills.
   The four-row table remains unexcluded. Relabel the table from
   `PROVISIONAL` to consumed-promoted.
5. Survival of `u^2-v^2=0` as monogenic index is correctly still
   `PROVISIONAL`, because it consumes the inverse-Kummer successor (AUDIT
   still lists that successor as provisional). No Orevkov--Chau term, second
   ruling, or independent Kummer class is inferred.

OPEN list (cusp Newton polygon, special-boundary leading terms, transport
from monogenic index to a dicritical jump, incidence `u_c in Phi` or not,
collision `L0`/`L1`, tangency versus transversality of immersed collision
branches, uncontrolled integer `kappa_B`) is not under-typed. No
`PROVISIONAL` label on an unproved premise is used inside a line the packet
marks as exact, except the inverse-Kummer block which is labelled
throughout.

The cheapest discriminator `Theta_h=d_h-r_h-2` is correctly described as
uncomputed: the packet does not supply an SNC pole expansion. Asking for
one is the right successor, not a CAS elimination.

## 10. Weakest exact hypotheses, correction, next test

**Hypotheses actually used.** Characteristic zero, algebraically closed.
The hypersurface ring `R` above, with the Poisson structure of the promoted
parent (or any `C^*` multiple). A pair `f,g in R` with `{f,g}=kappa in C^*`
and `[Frac(R):C(f,g)]=4`. Finite normalisation `Y->A2` with
`S=Y-R_bd=Spec R`, `pi|_S` étale, image cofinite, and reviewed boundary
census: irreducible `B`, generic fibre `(2,1,1)`, unique cusp `(3,1)`,
unique omitted node `(2,2)`, normalisation of `B` equal to `A1`. Reviewed
function-pair collision: immersive polynomial normalisation `Phi -> C_0`
with a multibranch self-identification off `{c,n}`. For (1.15):
separatedness of `Y` and nonemptiness of `R_bd`. For §3.1: Zariski-general
coordinate fibres, now available from the promoted parent. For (3.8)--(3.10)
as geometric statements about `Disc(P_t)`: the inverse-Kummer successor,
still provisional.

**Correction and blast radius.** No correction to a charged identity. Two
label changes after the parent promotion: drop `PROVISIONAL` on
non-local-finiteness of `X_f,X_g`, on hyperbolicity of generic fibres, and
on the table (3.1)--(3.6). Optional wording tightening of "boundary packet
alone" in (1.15): name the constant Jacobian among the ingredients. Blast
radius zero. Inverse-Kummer remains provisional; conclusion 5 must not be
read as promoted.

**Best next falsification test.** Compute `(d_h, r_h)` for either charged
coordinate from one genuine SNC compactification of a generic fibre (pole
order of `h o beta_B` at the unique infinite place of `B`, and the number of
poles of the mate on that fibre). Form `Theta_h=d_h-r_h-2`. If `Theta_h` is
negative or odd, then either (3.2) is false or the horn is closed by (3.6).
If `Theta_h` is nonnegative even, the test specialises to the corresponding
partition row of the table and does not yet kill. Desk-level negative
control already available without a compactification: the identity (1.9)
fails if a coordinate restriction `f_0` is affine, so any explicit model of
the pair whose restriction to `Phi` is degree one in `Z` would refute the
function-pair collision rather than this valuation lemma.

<!-- BODY-END -->
