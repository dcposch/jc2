# Hostile review: quartic one-cusp function-pair reduction

## Custody

Charged hashes reproduced before reading:

```text
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
70c1e16270564af7138cdc9f4b4ef396a17b398698694330ee5146ec8a273f5d
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md.artifact.json
7d40e7ee6d5970c51d62f73bafaf11670cb32c06bd51859876ab526f0fdf8bab
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
  refs/chau1999_apm71_full.pdf
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

Producer manifest reproduced:

```json
{"artifact":{"body_bytes":21468,"body_sha256":"ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d","file_bytes":21801,"frozen_basis":"06a4110854d7ad38525daccfa7895943259a3812","full_sha256":"0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f","name":"block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md","published_mode":"0444"},"custody":{"closed_utc":"2026-08-30T22:37:37Z","finalized_utc":"2026-08-30T22:37:41Z","lease_id":"b6700119e3bdb144606273f2e7ae5144","opened_utc":"2026-08-30T22:25:55Z","owner":"rank4_cycle1_function_pair","source_bytes":21468,"source_sha256":"ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d"},"schema":"jc2.artifact-finalize/v1"}
```

Producer seal reproduced:

```text
Body definition: every byte through the unique standalone <!-- BODY-END --> line,
including its terminating newline; this seal is outside the body.
Body bytes: 21468.
Body SHA-256: ca809efbfbf2e613e74254d27a2b37fc4cef44610569a03cf7aa69da11b9b78d.
Frozen basis: 06a4110854d7ad38525daccfa7895943259a3812.
```

Custody verdict: all charged bytes matched. No `CUSTODY_FAIL`.

Primary-source checks used narrowly:

```text
Miyanishi, Lectures on Geometry and Topology of Polynomials,
arXiv:1504.07179, Lemma 2.5.2, checked at
https://arxiv.org/pdf/1504.07179.

Chau, Non-zero constant Jacobian polynomial maps of C2,
Ann. Polon. Math. 71 (1999), charged file refs/chau1999_apm71_full.pdf,
Theorem 4.4 and Remark 4.9.

Orevkov, On three-sheeted polynomial mappings of C2,
Math. USSR-Izv. 29 (1987), Lemma 4.2, checked from the Math-Net
English PDF linked at https://www.mathnet.ru/eng/im1571.
```

## Executive Verdict

The function-pair report is mostly correct, but only as a conditional
normalization-and-budget theorem. The cyclic Miyanishi replacement, the
coordinate-power form, the construction of the noninvertible Keller map
`H=pi o f_mu`, the minimal-degree consequence `mu=d1`, the exact nonproper
set `B union C0`, the Orevkov-Chau budget inequality, and the Euler/orbit
ledger all survive hostile reconstruction, provided the auxiliary hypotheses
listed below are kept explicit.

No exclusion of the one-cusp horn follows. The last possible contradiction
is still a missing theorem coupling the quartic algebra, `K_U=0`, or the
saturated two-component infinity link to the new immersed self-collision of
`C0`. In the charged material that coupling is not present.

## 1. Pseudo-plane Hypotheses and Miyanishi Lemma 2.5.2

Status: CONFIRMED, with hypotheses made explicit.

The charged pseudo-plane input supplies:

```text
U smooth, rational, affine;
bar-kappa(U)=-infinity;
rho:U->A1 an A1-fibration;
every reduced ruling fibre is one A1;
rho^{-1}(a)=mu*Phi, Phi ~= A1, mu>=2;
Pic(U)=Z/mu<[Phi]>;
H_i(U;Q)=0 for i>0;
K_U~0;
mu|d1.
```

Miyanishi Lemma 2.5.2 applies to a `Q`-homology plane with log Kodaira
dimension `-infinity`, an `A1`-fibration over `A1`, and a unique multiple
fibre `dF` with `F ~= A1`, `d>=2`. The lemma constructs the degree-`d`
cyclic base cover of the ruling, totally ramified over the multiple value
and over infinity, normalizes the fibre product, obtains a finite etale
Galois cover of the original surface, and says that deleting `d-1` of the
`d` affine-line components over `F` leaves an open surface isomorphic to
`A2` which still maps surjectively and etale to the original surface.

Applying this with `d=mu`, `F=Phi`, gives a morphism

```text
f_mu:A2->U
```

which is surjective, etale, and generically of degree `mu`. It is not a
finite cover after deletion; it is a Galois affine pseudo-covering in the
source's sense, while the finite Galois object is the normalized cyclic
cover before deleting the `mu-1` lines.

The coordinate claim also survives, but it uses one extra trivial-bundle
step. Let `x` be a coordinate on the cyclic base cover. After choosing the
base coordinate so that `rho(Phi)=a`, the base map is

```text
x |-> a+lambda*x^mu, lambda in C*.
```

The retained open has fibres equal to the ordinary pulled-back ruling
fibres away from `x=0` and to the retained line over `x=0`. Since all
reduced ruling fibres in the charged row are one affine line, this induced
map `A2->A1_x` has all scheme fibres reduced affine lines. Equidimensionality
over the smooth curve gives flatness; the fibres are smooth, hence this is a
smooth `A1`-bundle. Over `A1`, the line-bundle and additive torsor classes
vanish, so the bundle is trivial. Therefore `x` is a genuine polynomial
coordinate on the retained `A2`, and

```text
rho o f_mu = a+lambda*x^mu.
```

Required hypotheses: `U` smooth and normal; `U` a `Q`-homology plane in
Miyanishi's sense; log Kodaira dimension `-infinity`; base exactly `A1`;
unique multiple fibre `mu*Phi` with `Phi ~= A1`; and, for the coordinate
upgrade, the charged fact that every reduced ruling fibre is a single `A1`.

## 2. The Polynomial Keller Map `H`

Status: CONFIRMED, with wording corrections.

Set `H=pi o f_mu`. Since `A2` is affine, this is a polynomial pair. The
factor `f_mu` is etale but not finite. The factor `pi` is etale on its
displayed domain `U`, but `pi:U->A2` is not finite and its image is only
`A2-{n}`. These corrections matter; they do not damage the argument.

The composition is etale everywhere on `A2`, so its Jacobian determinant is
a polynomial with no zero in `A2(C)`. Over the algebraically closed field
`C`, a nonconstant polynomial has a zero on its hypersurface; equivalently,
the only units of `C[x,y]` are `C*`. Thus the Jacobian is a nonzero constant.

The geometric degree is the tower degree:

```text
deg_geo(H) = deg_geo(pi|U)*deg_geo(f_mu) = 4*mu.
```

This is computed at a general target point avoiding the asymptotic curves.
The image is exactly

```text
H(A2)=pi(f_mu(A2))=pi(U)=A2-{n},
```

because `f_mu` is surjective and the charged companion file gives
`pi(U)=A2-{n}`. Therefore `H` is a noninvertible plane Keller map of
geometric degree `4mu`.

## 3. Minimal-Counterexample Consequence

Status: CONFIRMED.

For the original block, the total geometric degree is `4d1`. The cyclic
replacement gives another noninvertible Keller map of degree `4mu`. If the
original counterexample was chosen with minimal geometric degree among all
plane Keller counterexamples, the replacement cannot have smaller degree:

```text
4mu >= 4d1, hence mu>=d1.
```

The pseudo-plane package also gives `mu|d1`; write `d1=k*mu`. Then
`mu>=d1` forces `k=1`, so

```text
mu=d1.
```

The direction of the inequality in the producer is correct. The statement
is not an identity for arbitrary nonminimal factorizations.

The `d1=1` corollary is also scoped correctly: inside this exact
unique-multiple-fibre pseudo-plane row, `mu|d1` and `mu>=2` rule out
`d1=1`. This does not exclude rank-four configurations outside the charged
row, nor any primitive/no-proper-block horn.

## 4. Finite Completion and Nonproper Values

Status: CONFIRMED, with one dependency stated.

Let `Utilde->U` be the finite cyclic cover before deletion, and let `Ubar`
be the normalization of `Y` in `C(Utilde)`. Since `Y` is excellent normal
affine and the extension is finite, `Ubar->Y` is finite. Over `U` it is the
finite etale cover `Utilde->U`. The retained source `A2` is

```text
Utilde minus (L_1 union ... union L_{mu-1}).
```

Thus the boundary of the retained `A2` in `Ubar` is exactly

```text
preimage of R=Y-U, together with L_1,...,L_{mu-1}.
```

Composing the finite maps `Ubar->Y->A2` gives a finite completion of `H`.
The boundary over `R` maps into `B`. Each deleted line maps to

```text
C0=pi(Phi).
```

There is no hidden boundary divisor: any point outside the retained `A2`
lies either over `R` or on one of the deleted lines. Conversely, a general
point of each boundary image is nonproper for `H`, because sequences in
`A2` can approach the deleted boundary in the finite completion. Hence the
nonproper-value set is set-theoretically

```text
A(H)=B union C0.
```

At this stage `C0` may coincide with an irreducible component of a reducible
`B`; the producer correctly postpones excluding that possibility.

The claim `n notin C0` is confirmed. The retained line `L_0` lies in the
source `A2`, `H(A2)=A2-{n}`, and `C0=H(L_0)`. Therefore `C0` misses `n`.
Since `n in B`, once Section 5 below proves `B` irreducible, `C0!=B`.

The closedness of `C0` is also valid: a nonconstant polynomial map
`A1->A2` is finite onto its image because `C[t]` is finite over `C[p(t)]`
for a nonconstant coordinate polynomial `p(t)`, hence finite over the
intermediate image ring.

## 5. Orevkov-Chau Infinity Budget

Status: CONFIRMED. This is the load-bearing part, and it survives after the
following reconstruction.

Orevkov's Lemma 4.2, in the regularized topological completion, has the
form

```text
sum_l [ mu_l + sum_{x in l-{infinity}}(mu_x-mu_l) ] = deg_geo(H)-1,
```

where `l` runs over the nonconstant boundary components, `mu_l` is the
generic local multiplicity along `l`, and each correction is nonnegative.
Chau's Remark 4.9 restates this as formula (4.9), and formula (4.10)
rewrites the same budget in the Newton-Puiseux language. The producer's
finite normalization is not literally Orevkov's final regular extension,
but resolving it only subdivides or refines the same boundary branches; it
cannot remove a nonconstant boundary contribution. Thus lower bounds may be
checked on the finite normalization and then charged to the regular
extension.

A boundary component with generic transverse multiplicity `m` and degree
`s` over the normalization of its image contributes at least `m*s`.
Indeed, the Orevkov bracket includes the generic `m`, and ramification of
the polynomial map `A1->A1` of degree `s` contributes total finite
ramification `s-1`, weighted by `m`. This justifies replacing generic
missing rank by an Orevkov lower bound, not merely by a target-fibre
cardinality.

For each irreducible component `B_i`, the generic partition of the quartic
second leg is `(2,1,1)`. The two unramified sheets are in `U`; the length-two
ramified sheet is on `R`. After the cyclic cover, the valuation identity over
the generic DVR of `R_i`,

```text
sum e_j f_j = mu,
```

multiplied by the rank-two local factor of `pi`, gives total boundary
generic multiplicity `2mu` over `B_i`. Hence the boundary over the `r`
components of `B` contributes at least

```text
2mu*r.
```

At the unique `(3,1)` cusp value, the ramified local length is three rather
than two. The cusp is unibranch on the target branch, so this is a genuine
local-degree jump at the same normalization branch, not a second
normalization preimage. After the cyclic cover the jump contributes at
least

```text
mu.
```

The `(2,2)` node is budget-free in this formula. The node has two
normalization preimages, each carrying the generic rank-two packet. Their
image self-identification changes the target fibre picture but does not
increase local multiplicity along either boundary parameter. This is exactly
the distinction between singular image and critical parametrization.

The deleted lines contribute separately. Each `L_j`, `j=1,...,mu-1`, is a
boundary component of the retained source and maps nonconstantly to `C0`.
The ambient map is etale along `L_j`, so the transverse local multiplicity
is one. Its Orevkov bracket is therefore at least one. This remains true
even if, before irreducibility is proved, `C0` coincides with a component of
`B`: Orevkov sums boundary components, not distinct image curves, so there
is no cancellation or overlap discount.

Thus

```text
4mu-1 = deg_geo(H)-1
      >= (2mu*r + mu) + (mu-1)
      = 2mu*r + 2mu - 1.
```

Since `r>=1`, the inequality forces

```text
r=1.
```

For `r=1` the lower bound equals the entire budget, so every inequality used
above is saturated. There is no spare contribution from a hidden dicritical,
from an extra critical point on a boundary parametrization, or from another
component of `B`.

## 6. Consequences of Saturation and Chau's Theorem

Status: CONFIRMED, with the singular-image correction emphasized.

Saturation of the deleted-line contribution implies that each deleted line
contributes exactly one. Since the ambient map is etale along the line, the
only way to have contribution one is:

```text
degree(L_j -> normalization(C0)) = 1,
no finite ramification correction.
```

The normalization of `C0` is `A1`: it is dominated finitely by `A1`, and it
cannot be a punctured affine line because a nonconstant unit would pull back
to a nonconstant unit of `C[t]`. Therefore each deleted line maps
degree-one to the normalization of `C0`. By deck symmetry the retained line
`L_0` has the same image parametrization. Since `pi o f_tilde` is etale
along these lines, the normalization parametrization is immersive.

Now `r=1` and `n notin C0` give `C0!=B`; hence `C0` is a genuine second
component of the nonproper-value set of `H`.

Chau's Theorem 4.4 applies to this noninvertible constant-Jacobian
polynomial map after a harmless generic coordinate choice making the
polynomials monic in `y`. Its assertion (E3) says that every asymptotic
curve `C_[phi]` has a singularity. Applied to the component `C0`, this
forces `C0` to be singular.

Because the normalization map of `C0` is immersive, the singularity cannot
be a cusp or any other unibranch singularity caused by a critical
parametrization. It must be a multibranch self-identification. Transporting
through `L_0 ~= Phi` gives

```text
there exist p!=p' in Phi with pi(p)=pi(p').
```

The collision value is not `n`, since `n` is not in `pi(U)`. It is not the
unique cusp value `c`, because the charged companion census gives exactly
one companion point of `U` over `c`. Thus the collision is either away from
`B`, or at an ordinary point of `B` where the two unramified companions both
lie on `Phi`. The charged data do not choose between these cases.

This is a new same-ruling-fibre self-collision theorem. It is not a new bad
fibre of `rho`, not a critical point of the parametrization, and not an
exclusion.

## 7. Euler Identity and Cyclic-Orbit Deficit

Status: CONFIRMED, downstream of `C0!=B`.

Let

```text
T=U times_{A2} B,        A=T intersect Phi,        N=#A,
D=V(b o H)=f_mu^{-1}(T).
```

The finiteness of `A` uses the result `C0!=B`. Without it, `Phi` could lie
inside `T`; after irreducibility and `C0!=B`, `Phi` is not a component of
`T`, so `A` is finite.

The full cyclic pullback `Ttilde=f_tilde^{-1}(T)` is finite etale of degree
`mu` over `T`, hence

```text
e(Ttilde)=mu*e(T)=-3mu.
```

The retained source `D` is obtained by deleting the intersections of
`Ttilde` with `L_1,...,L_{mu-1}`. Each deleted line meets `Ttilde` in a copy
of `A`; these are finite sets of cardinality `N`. Deleting finite points
lowers Euler characteristic by their cardinality, so the sign is correct:

```text
e(D)=-3mu-(mu-1)N,
D intersect {x=0}=A.
```

The map `x:D->A1` is quasi-finite. If a component of `D` were vertical, the
corresponding ruling fibre in `U` would be contained in `T`; its polynomial
image under `pi` would be a closed irreducible curve dense in the now
irreducible `B`, hence all of `B`, forcing it to contain `n`, impossible
because `pi(U)=A2-{n}`.

Let `nu` be the generic cardinality of an `x`-fibre on `D`. A finite
Zariski-Main completion over `A1` is torsion-free, hence flat over the
smooth base; its fibres have length `nu`, and deleting boundary points can
only lower the number of source points. Therefore each special fibre has
cardinality at most `nu`. Constructible Euler integration gives

```text
e(D)=nu - sum_s (nu-#D_s).
```

At `x=0`, the defect is `nu-N`. Away from zero, the cyclic deck action sends
`x` to `zeta*x`, acts freely on nonzero `x`-values, and preserves `D`; hence
nonzero exceptional values occur in free orbits of size `mu` with constant
defect on each orbit. If `Delta` is the sum over one representative from
each nonzero orbit, then

```text
-3mu-(mu-1)N = nu-(nu-N)-mu*Delta,
Delta=N+3.
```

This proves the producer's orbit-deficit formula. It also proves that the
tempting congruence `mu|e(D)` is false in general; the correct congruence is

```text
e(D)=N mod mu.
```

The cusp dichotomy is correct. If the unique cusp companion point of `T`
does not lie on `Phi`, its cyclic preimage gives `mu` cusp points in one
nonzero deck orbit. If it lies on `Phi`, one cusp point remains at `x=0`
and the other `mu-1` copies lie on deleted lines. The node contributes no
point of `D`, because `n` is omitted by `pi(U)`.

I attempted an independent SymPy check of the displayed polynomial control,
but SymPy is not installed in this environment. The necessary small control
is nevertheless elementary and is reconstructed in the next section.

## 8. All-`mu` Polynomial Firewall

Status: CONFIRMED as a firewall only.

For

```text
G(t)=(t-1)^3(t-2)(t-3)(t-4)(t-5),
Q(t,y)=y^2-G(t),
q_mu(x,y)=Q(x^mu,y),
```

the curve `Q=0` has a single cusp at `(t,y)=(1,0)`. Indeed
`G` has a triple root at `1`, and the other roots are simple. Locally at
`t=1`, after multiplying by a unit, the equation is `y^2=(t-1)^3`, an
ordinary cusp. At the simple roots, `G'(t)!=0`, so the curve is smooth.

The normalization is

```text
z^2=(t-1)(t-2)(t-3)(t-4)(t-5),        z=y/(t-1).
```

This is the affine part of an odd-degree genus-two hyperelliptic curve with
one point at infinity removed. The cusp normalization is point-bijective, so

```text
e(Q=0)=2-2*2-1=-3.
```

At `t=0`, `G(0)=-120`, so `Q=0` has two points; thus `N=2` in the model.
For `q_mu=0`, the singular points occur exactly over `x^mu=1`, giving `mu`
ordinary cusps. Projection to `x` has generic cardinality two. The deficient
fibres occur exactly when

```text
x^mu in {1,2,3,4,5},
```

so there are `5mu` deficient fibres, each with one point instead of two.
Therefore

```text
e(q_mu=0)=2-5mu=-3mu-(mu-1)*2,
sum_nonzero_orbit_reps(2-#fibre)=5=N+3.
```

Every ambient fibre of `x:A2->A1` remains a reduced irreducible affine line.
Thus the Euler/orbit ledger, one cusp orbit, no source node, and all cyclic
power features do not force a second bad ruling fibre.

This control does not realize a Keller map, the quartic finite-flat algebra,
the omitted `(2,2)` target value, the companion counts, `Pic(U)=Z/mu`,
`K_U=0`, or the two-component nonproper set. Its blast radius is exactly the
producer's stated one: it blocks only arguments that use the polynomial
fibre ledger alone.

## 9. Search for a Decisive Successor

Status: GAP/OPEN.

No decisive contradiction follows from the charged files.

The quartic algebra might eventually force the `C0` self-collision to occur
on `B`, or force a critical jump in the boundary map, or force an additional
bad ruling fibre. But none of these implications is proved in the charged
material. The saturated Orevkov-Chau budget actually says that any such
extra event must be justified by a new theorem; it cannot be inserted as a
free geometric expectation.

`K_U=0` also gives no immediate contradiction. In the charged setup
`f_mu^*K_U=K_A2~0`, and `T` is principal on `U`. Adjunction is compatible
with the Euler calculation. There is no remaining canonical-class term that
forces a congruence on `N` or a new local-degree correction.

The two-component link at infinity is the best remaining target, but the
needed statement is absent. The smallest exact missing lemma is one of the
following:

```text
1. a quartic-algebra lemma forcing the immersed self-collision of C0 to lie
   on B, with a resulting divisor-intersection contradiction;
2. an infinity-link lemma showing that B union C0 must create an additional
   Orevkov local-degree jump despite saturation;
3. a ruling-coupling lemma showing that the self-collision on Phi forces a
   second reducible or multiple fibre of rho;
4. an exact computation of N=#(T intersect Phi) incompatible with
   Delta=N+3 and the companion packet.
```

Until one of these is proved, the successor is `OPEN`.

## 10. Maximum-Safe Theorem, Corrections, and Blast Radius

Status: CONFIRMED theorem with restricted blast radius.

Maximum-safe promotion:

```text
Every strict-block survivor in the charged connected rank-four one-cusp
row canonically produces a noninvertible plane Keller map

    H=pi o f_mu:A2->A2

of geometric degree 4mu, with image A2-{n} and with a coordinate x satisfying

    rho o f_mu = a+lambda*x^mu.

If the original survivor is minimal among all plane Keller counterexamples,
then mu=d1. The nonproper-value set of H is exactly B union C0, where
C0=pi(Phi). The Orevkov-Chau degree-at-infinity budget forces B
irreducible and is saturated. Hence C0 is a distinct second asymptotic
component, normalized immersively by the retained line, and Chau's theorem
forces C0 to have a multibranch self-identification. Equivalently, there
exist p!=p' in Phi with pi(p)=pi(p'), away from the omitted node n and away
from the unique cusp value c. For D=V(b o H), the exact identities are

    e(D)=-3mu-(mu-1)N,
    D intersect {x=0}=A=T intersect Phi,
    sum_nonzero_orbit_reps(nu-#D_x)=N+3.
```

Required corrections:

```text
1. f_mu is etale, surjective, and generically degree mu, but not finite
   after deleting mu-1 lines.
2. pi is etale on U, but pi:U->A2 is not finite and not surjective onto A2.
3. The selected A2 in Miyanishi's construction need not be stable under
   the full deck action; the Galois statement belongs to the finite cyclic
   cover/function-field level.
4. The coordinate x requires the smooth trivial A1-bundle argument over A1.
5. The Orevkov budget must be read on a regular extension; the finite
   normalization only supplies lower-bound packets after resolution.
6. Chau supplies singularity of the asymptotic image curve, not criticality
   of its normalization map.
7. Section 5's finite number N depends on the earlier proof C0!=B.
8. The polynomial firewall is not a Keller or quartic-algebra model.
```

Do not promote:

```text
exclusion of R4-CYCLE-1;
exclusion of the whole one-cusp horn;
existence of a proper block;
existence of a counterexample;
JC2;
mu|3;
N=0;
C0 intersect B nonempty;
a forced second bad ruling fibre;
a critical parametrization of C0;
finiteness of f_mu or pi|U;
any arbitrary rank-four d1=1 exclusion outside this exact pseudo-plane row.
```

Cheapest next attack: compute the saturated two-component infinity relation
for `B union C0` together with the quartic companion algebra. The target is
not another Euler congruence, but a theorem forcing the `C0` self-collision
to land on `B` or forcing a positive local-degree jump that would break the
already saturated Orevkov-Chau budget.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23773`.
- Body SHA-256:
  `9e41fdf54b2a6db8908c50830c0b97fe70d7d5a83a71ff994c95baeb16cc0240`.
- Frozen basis: `7ff3257e9a5f944580cef9c7961296b6ca1db50c`.
