# Hostile review: degree-three Hodge divisor and genus-one four-row gate

Date: 2026-08-30  
Reviewer: GPT-5.5, independent hostile reconstruction  
Receipt status: `ABSENT`

## 0. Charge and overall verdict

All five charged SHA-256 values match the files byte for byte:

```text
087953ec71175d8e470cd2aa89dd7928ef0ab88223009c619e2d95dc39287637
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md
e571684152a54d9921cc38bdcb9f8833a6f875bda659cf6ebeb8877871246a87
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md.artifact.json
ef7b8f5ea7c9f44af7b01f69e3a0f7d15852c804074d41cf1a6aa9f1f204ef1a
  xmodel/bd-a2-d3plus-pg-defect-coordinator-integration-sol56-20260830.md
80c8fd45679f56ac64966f0041fe9dce8b112fdbcfd6db66c7c25195cc42c6e8
  xmodel/bd-a2-d3plus-pg-defect-hostile-review-opus5-20260830.md
4eb8fc8ba526441c609448602a122601330ed99db9264d91261ea4cfb810a113
  xmodel/bd-a2-d3plus-pg-defect-sol56-20260830.md
```

No correctness is inferred from those hashes, seals, manifests, or earlier
reviews. I reconstructed the surface, lattice, local-DVR, and invariant
arguments independently.

Overall verdict: **CONFIRM_WITH_CORRECTIONS**. The Hodge divisor, four rows,
and Picard lower bounds survive. I found no fifth row and no counterexample to
the conditional theorem. Three proof repairs matter, and one sharpening
materially reduces the successor locus:

1. Flat connected genus-one fibrations are not automatically
   cohomologically flat in the presence of multiple fibres. Here local
   freeness is rescued by characteristic-zero tameness.
2. The support-transfer statement is about support on the base; contraction
   can lose internal discrepancy data even though it cannot erase a whole
   defect fibre.
3. The blowup lower bound needs an induction that includes satellite and
   intersection centres.
4. Hodge colength `k` gives ternary-cubic level **exactly** `k`, not merely the
   displayed lower valuations. Thus a level-two point also satisfies
   `v(c4)<12` or `v(c6)<18`, and a level-one point satisfies `v(c4)<8` or
   `v(c6)<12`.

Itemized disposition:

| item | disposition |
|---:|---|
| 1 | `CONFIRM_WITH_CORRECTIONS` |
| 2 | `CONFIRMED` |
| 3 | `CONFIRMED` |
| 4 | `CONFIRMED` |
| 5 | `CONFIRM_WITH_CORRECTIONS` |
| 6 | `CONFIRM_WITH_CORRECTIONS` |
| 7 | `CONFIRMED` |
| 8 | `CONFIRM_WITH_CORRECTIONS` |
| 9 | `CONFIRM_WITH_CORRECTIONS` |
| 10 | `CONFIRMED` |
| 11 | `CONFIRMED` |
| 12 | `CONFIRM_WITH_CORRECTIONS` |

## 1. Flatness, connectedness, Hodge lines, and duality

**Disposition: `CONFIRM_WITH_CORRECTIONS`.**

Let `B=P1`. For each `t in B`, restriction of the defining equation to
`P2 x {t}` is a ternary cubic. It cannot vanish identically: otherwise the
integral surface `X` would contain the same-dimensional irreducible surface
`P2 x {t}` and hence equal it, contrary to `[X]=3A+3B`. Every fibre is
therefore a nonempty pure one-dimensional plane Cartier divisor. Since `X` is
Cohen--Macaulay (indeed a hypersurface) and `B` is regular of dimension one,
`q:X->B` is flat. Equivalently, a uniformizer of `B` is a nonzero element of
the domain `O_X`, hence a nonzerodivisor, and torsion-free modules over a DVR
are flat. Nonreduced and multiple plane cubics cause no exception.

For every scheme fibre `C`, including a triple line,

```text
0 -> O_P2(-3) -> O_P2 -> O_C -> 0
```

gives `H^0(C,O_C)=C` and `h^1(C,O_C)=1`. Thus the fibres are connected and
have no extra global nilpotents. Pushing the global hypersurface sequence

```text
0 -> O_P2xB(-3,-3) -> O_P2xB -> O_X -> 0
```

along the second projection, using the elementary cohomology of `O_P2(-3)`,
gives directly `q_*O_X=O_B` and `R^1q_*O_X=O_B(-3)`; no reduced-fibre
assumption is hidden in this base-change step. For `f=q r`, the same DVR
argument proves flatness. Normality and proper birationality give
`r_*O_Y=O_X`, hence

```text
f_*O_Y=q_*r_*O_Y=O_B,
```

so the fibres of `f` are connected.

Adjunction gives `omega_X=q^*O(1)`, and therefore

```text
omega_(X/B)=q^*O(3),             q_*omega_(X/B)=O(3).       (1.1)
```

The delicate point is `R^1f_*O_Y`. Flatness plus connectedness alone does
not exclude torsion for an arbitrary genus-one fibration. Contracting vertical
`(-1)`-curves does not change `Rf_*O`; on the relatively minimal model the
standard decomposition is a rank-one line bundle plus torsion supported at
wild fibres. In characteristic zero every multiple fibre is tame, so the
torsion is zero. This is stated for fibrations without a section in Seiler,
Theorem 1.1, [*Global moduli for polarized elliptic surfaces*](https://www.numdam.org/item/CM_1987__62_2_187_0.pdf),
pp. 189--190. Thus `R^1f_*O_Y` is locally free of rank one.

The dominant rational map from `A2` yields a generically finite rational map
`P2 --> Y` by the function-field inclusion. Over `C`, the smooth projective
unirational surface `Y` is rational (the original rationality route is
Castelnuovo, [*Sulle superficie di genere zero*](https://media.accademiaxl.it/memorie/S3-VX-1896/Castelnuovo82-123.pdf)).
Only `chi(O_Y)=1` is needed here. If `R^1f_*O_Y=O(a)`, Leray gives

```text
1=chi(O_Y)=chi(O_B)-chi(O(a))=-a,
```

so it is `O(-1)`. Relative duality for the proper flat Gorenstein curve
fibration then gives

```text
f_*omega_(Y/B)=(R^1f_*O_Y)^vee=O(1).                    (1.2)
```

The duality input is Grothendieck's coherent-duality theorem,
[*Theoremes de dualite pour les faisceaux algebriques coherents*](https://www.numdam.org/article/SB_1956-1958__4__169_0.pdf),
Exposé 149; the displayed formula is its relative-dimension-one,
`F=O_Y` specialization.

Multiple fibres therefore create neither torsion nor a base-change failure in
this characteristic, but the tame-fibre theorem is an essential dependency.

## 2. The pushed GR sequence and its scheme-theoretic divisor

**Disposition: `CONFIRMED`.**

Start from the binding trace sequence

```text
0 -> r_*omega_Y -> omega_X -> Q_GR -> 0.
```

Tensoring by the invertible `q^*O(2)` is exact. Projection formula gives

```text
Q_rel = Q_GR tensor q^*O(2),
r_*omega_Y tensor q^*O(2)=r_*omega_(Y/B),
omega_X tensor q^*O(2)=omega_(X/B).
```

The pushed long exact sequence really begins

```text
0 -> O(1) --s--> O(3) -> q_*Q_rel
  -> R^1q_*(r_*omega_(Y/B)).                              (2.1)
```

The first map is generically an isomorphism and therefore a nonzero injection
of line bundles. It is multiplication by a section `s in H^0(B,O(2))`; its
cokernel `C` has length two. The finite sheaf `q_*Q_rel` also has length two:
over `C` its length is its vector-space dimension, unchanged by the finite
pushforward or a line-bundle twist. Exactness injects `C` into `q_*Q_rel`, so
equality of lengths makes that injection an isomorphism. No vanishing of the
following `R^1q_*` term is assumed.

Locally, `Ann(C)=(s)`. Also

```text
Q_rel=O_ZGR tensor omega_X tensor q^*O(2)
```

is an invertible and hence faithful `O_ZGR`-module. Consequently

```text
Ann_B(q_*Q_rel)=ker(O_B -> q_*O_ZGR),
```

the ideal of the scheme-theoretic image for the **given** projection. Hence

```text
div(s)=q(Z_GR)=T                                             (2.2)
```

scheme-theoretically. The binding closed-immersion theorem further identifies
`Z_GR` with `T`. Twisting preserves both finite length and annihilator because
it is locally tensoring by a free rank-one module. The underlying vanishing
input is Grauert--Riemenschneider, Satz 2.3,
[*Verschwindungssätze für analytische Kohomologiegruppen auf komplexen Räumen*](https://www.math.uni-hamburg.de/home/riemenschneider/OR1970c.pdf).

## 3. Anti-effectivity and the Du Val criterion

**Disposition: `CONFIRMED`.**

Write `Delta=sum a_i E_i`. It is an integral exceptional divisor because
`K_X` is Cartier. For each exceptional prime,

```text
Delta.E_i=K_Y.E_i=2p_a(E_i)-2-E_i^2.                      (3.1)
```

The exceptional intersection form is negative definite; this is Mumford's
primary result in [*The topology of normal singularities of an algebraic
surface*](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1961a--TopSingSurface-NumDam.pdf),
p. 6. A minimal resolution has no exceptional rational `(-1)`-curve, since
contracting one leaves a smooth surface and a shorter resolution. Thus the
right side of (3.1) is nonnegative: it is nonnegative for a rational component
because `E_i^2<=-2`, and positive when `p_a(E_i)>=1`.

On a connected block, the intersection matrix `M` is negative definite, has
nonnegative off-diagonal entries, and is irreducible. Hence `-M` is an
irreducible nonsingular `M`-matrix; `M^{-1}` is entrywise strictly negative.
Solving

```text
M (a_i) = (Delta.E_i) >= 0
```

gives `a_i<=0`, strictly on the entire block if the intersection vector is
nonzero. Therefore `Delta<=0`.

If `Delta` vanishes on a block, (3.1) forces every component to be a rational
`(-2)`-curve; equivalently the resolution is crepant. Conversely a Du Val
resolution is crepant. For a connected Gorenstein normal surface singularity,

```text
Delta_block=0  iff  the singularity is Du Val.             (3.2)
```

The primary rational-singularity source is Artin,
[*On isolated rational singularities of surfaces*](https://doi.org/10.2307/2373050).
Minimality and Gorensteinness are essential in (3.2).

## 4. Relative minimalization and the full canonical formula

**Disposition: `CONFIRMED`.**

Successively contract vertical `(-1)`-curves to

```text
h:Y->S,             g:S->B,             f=g h.
```

The process terminates; `S` remains smooth, projective, rational, and
`g` is a relatively minimal genus-one fibration. Since `Delta` is vertical and
anti-effective,

```text
D=h_*Delta <= 0
```

is vertical. Choose canonical and fibre divisors compatibly with
`K_X=q^*O(1)`. Pushing `K_Y=f^*(t)+Delta` through `h` gives the actual divisor
identity

```text
K_S=F_t+D.                                                 (4.1)
```

Without those compatible representatives, (4.1) is an equality of divisor
classes. The relative formula is

```text
Delta=h^*D+K_(Y/S),                                       (4.2)
```

where `K_(Y/S)` is effective and `h`-exceptional.

Write every multiple fibre as `F_i=m_i P_i`, where `P_i` is the primitive
integral fibre cycle; it need not be reduced. Characteristic-zero tameness gives
the complete formula

```text
omega_S = g^*(omega_B tensor L)
          tensor O_S(sum_i (m_i-1)P_i),
deg L=chi(O_S)=1.                                         (4.3)
```

There is no wild coefficient and no torsion-length correction. Thus

```text
K_S ~ -F + sum_i (m_i-1)P_i,
K_S == (-1+sum_i(1-1/m_i))F.                              (4.4)
```

Primary sources are Kodaira, [*On compact analytic surfaces II*](https://doi.org/10.2307/1970131),
Section 12, and Seiler, Theorem 1.1, cited above. The tame/wild algebraic
framework also appears in Bombieri--Mumford,
[*Enriques' Classification of Surfaces in Characteristic p, III*](https://doi.org/10.1007/BF01390138),
Theorem 2.

## 5. At most one multiple fibre; index one or three

**Disposition: `CONFIRM_WITH_CORRECTIONS`.**

Formula (4.4) gives `K_S^2=0`; rationality then gives `rho(S)=10`. Hence `S`
is not a minimal rational surface and contains a `(-1)`-curve `C`. Relative
minimality makes `C` horizontal, and adjunction gives `K_S.C=-1`. Put
`n=F.C>0`. Intersecting (4.4) with `C` gives

```text
-1=(-1+sum_i(1-1/m_i)) n.                                (5.1)
```

The coefficient is negative. Two multiple fibres contribute at least
`1/2+1/2=1`, so there is at most one.

With no multiple fibre, (5.1) gives `n=1`; the rational curve `C` maps with
degree one to `P1` and is a section. With one multiple fibre `F_0=mP_0`,
(5.1) gives `n=m`. More generally every horizontal divisor `H` has

```text
F.H=m(P_0.H),
```

so every multisection degree is divisible by `m`, excluding a section for
`m>1`.

The missing construction in the producer is short: choose a general plane
line, intersect it with `X`, pull its horizontal strict transform to `Y`, and
push it to `S`. It is an effective horizontal divisor of total generic degree
three. Therefore `m|3`. The only possibilities are exactly

```text
m=1: no multiple fibre and a section;
m=3: one triple fibre and no section.                      (5.2)
```

Here `m=1` means the no-multiple case, not a “multiple fibre of multiplicity
one.”

## 6. Support transfer

**Disposition: `CONFIRM_WITH_CORRECTIONS`.**

For every fibre component `Theta`, both the base-pullback part of (4.3) and
every primitive fibre cycle have intersection zero with `Theta`; hence
`K_S.Theta=0`. From (4.1), `F.Theta=0`, so

```text
D.Theta=0.                                                 (6.1)
```

Here is the required kernel calculation rather than an appeal to a fibre
label. Let `M=(Theta_i.Theta_j)` and let `a=(a_i)` be the positive
multiplicity vector of the scheme fibre. Then `Ma=0`, the off-diagonal entries
of `M` are nonnegative, and the component graph is connected. For
`x_i=a_i y_i`, symmetry gives

```text
x^T M x=-sum_(i<j) M_ij a_i a_j (y_i-y_j)^2.
```

Thus `M` is negative semidefinite and its rational kernel is exactly `Q a`.
Its integral kernel is generated by the primitive fibre cycle `P_t`. Thus

```text
D_t=-b_t P_t,        b_t in Z_(>0)                        (6.2)
```

when the local part is nonzero.

“Support” here must mean support **on the base**. Both implications hold:

- If `t` is not in `Supp(T)`, then `Q_GR` and, by binding Matlis duality,
  `R^1r_*O_Y` vanish at all points over `t`. Those singularities are rational;
  Gorenstein rational surface singularities are Du Val, so every discrepancy
  block over `t` vanishes and `D_t=0`.
- If `D_t=0`, (4.2) restricts over `t` to
  `Delta_t=(K_(Y/S))_t`. The right side is effective, whereas `Delta_t` is
  anti-effective. Both vanish, so the GR ideal is the unit ideal over `t` and
  `t` is not in `Supp(T)`.

Consequently

```text
Supp_B(D)=Supp(T).                                         (6.3)
```

Contraction may still discard internal discrepancy components inside a
supported fibre. Equation (6.3) says only that it cannot discard the entire
base support.

## 7. Global equations and exhaustion of rows

**Disposition: `CONFIRMED`.**

In the no-multiple case, (4.1) and (4.3) give `D~-2F`. Intersecting with the
horizontal `(-1)`-curve, for which `F.C=1`, yields

```text
sum_t b_t=2.                                               (7.1)
```

In the triple case, `K_S~-P_0`, `F~3P_0`, and hence `D~-4P_0`. Now
`P_0.C=1` and `F.C=3`, so

```text
b_0+3 sum_(t!=t0) b_t=4.                                  (7.2)
```

This intersection derivation avoids cancelling divisor classes. Combine
(7.1)--(7.2) with (6.3) and the binding length-two closed subscheme `T`:

- support of size two forces local lengths `1+1`;
- support of size one is the unique colength-two DVR quotient `(u^2)`;
- a defect only away from the triple fibre would require a multiple of three
  to equal four;
- two physical defect points over one base point are excluded by the binding
  closed immersion.

There is no fifth row and no embedded-point alternative on the smooth base.
At no point is `b_t` identified with local geometric genus. The row
`b_0=4` with local GR length two is the explicit counterexample to such an
identification. Extra Du Val points remain invisible.

## 8. Blowup recurrence, carriers, and Picard bounds

**Disposition: `CONFIRM_WITH_CORRECTIONS`.**

Factor the inverse of `h` into point blowups and put `D_0=D`. At the `j`-th
blowup,

```text
D_j=pi_j^*D_(j-1)+E_j,
coeff_(E_j)(D_j)=1+ord_(p_j)(D_(j-1)).                    (8.1)
```

A coefficient born positive remains positive on its strict transform, so the
final inequality `Delta<=0` forces every centre order to be at most `-1`.

Proper surjectivity survives base change, hence `Y_t->X_t` is onto. Since
`X_t` is a pure one-dimensional plane cubic, some component of `Y_t` maps
onto a curve. It is not `r`-exceptional and therefore has discrepancy
coefficient zero. If `D_t=-bP_t`, every component inherited from `S_t`
starts with coefficient `-b a_i<=-b` and retains it. The zero-coefficient
carrier must therefore be created by the blowup chain.

The producer's informal induction needs this satellite-safe form. Before the
first zero coefficient, let `M_j` be the largest coefficient among fibre
components after `j` blowups over `t`. Then `M_0<=-b`. At a centre lying on
components with negative coefficients `c_i<=M_(j-1)` and local
multiplicities `mu_i>=1`,

```text
ord_p(D_(j-1))=sum mu_i c_i <= M_(j-1).
```

Thus the new coefficient is at most `1+M_(j-1)`, while old coefficients do
not change, and inductively `M_j<=-b+j`. No zero coefficient can occur before
the `b`-th blowup. Intersection and infinitely-near centres only delay it.
Counts over distinct fibres add.

Since `rho(S)=10` and each blowup raises Picard rank by one, the lower bounds
for the **minimal resolution** are `12,12,12,14` in the four rows below.
Arbitrary later blowups are irrelevant.

## 9. The no-section Hodge bridge

**Disposition: `CONFIRM_WITH_CORRECTIONS`.**

Liu--Lorenzini--Raynaud Theorem 3.1 actually says the following. Over a DVR
with algebraically closed residue field, for a proper flat regular curve with
`f_*O=O`, the canonical generically isomorphic map

```text
H^1(model,O) -> Lie(Neron(Jac))                            (9.1)
```

has kernel and cokernel of equal finite length. See the authors' PDF,
[*Néron models, Lie algebras, and reduction of curves of genus one*](https://www.math.u-bordeaux.fr/~qliu/articles/LLR.pdf),
Theorem 3.1, pp. 456 and 475--481. Smoothness of the Néron model makes its
Lie algebra free of rank one. The source is free of rank one here by the
characteristic-zero tame-fibre argument in Item 1, not merely by properness,
flatness, and connectedness. Its kernel is therefore zero; equal lengths make
the cokernel zero. Thus (9.1) is an isomorphism, including at a locally
insoluble triple fibre.

Dualizing identifies the resolved-torsor Hodge lattice with the Néron
invariant-differential lattice of the minimal Jacobian. Blowups preserve
`H^1(O)` and `R^1f_*O` because `pi_*O=O` and `R^1pi_*O=0`; relative duality
preserves the corresponding Hodge line. Passing to a strict henselization or
completion is faithfully flat, so an isomorphism and the finite colength
descend. In the present complex DVR the residue field is already algebraically
closed, so strict henselization is not needed merely to invoke the theorem.

The 2018 [corrigendum](https://arxiv.org/abs/1804.11158) corrects LLR Theorem
4.3 and the later Brauer/Shafarevich--Tate formula. It does not alter Theorem
3.1 or this Hodge bridge.

## 10. Fisher/CFS normalization, orientation, and exact local level

**Disposition: `CONFIRMED`.**

Choose compatible local generators so that the minimal/resolved generator
`alpha` maps to `s beta`, where `beta` is the plane-model residue
differential. Hence `beta=s^{-1}alpha`. Fisher's Lemma 2.2 says that replacing
`omega` by `lambda^{-1}omega` multiplies the geometric invariants by
`lambda^4` and `lambda^6`; Proposition 5.19 and Proposition 5.23 identify
these geometric invariants with the normalized model invariants. See
Fisher, [*The invariants of a genus one curve*](https://www.dpmms.cam.ac.uk/~taf1000/papers/g1inv.pdf),
pp. 3--4 and 21--24. Therefore the orientation is

```text
c4_plane   = s^4  c4_min,
c6_plane   = s^6  c6_min,
Disc_plane = s^12 Disc_min.                              (10.1)
```

Changing compatible generators only introduces the corresponding units; the
valuation and divisor statements are canonical. The plane Hodge line is
`O(3)`, the minimal one is `O(1)`, and `s` is in `O(2)`. Thus the discriminant
degrees are exactly

```text
36 = 24 + 12.                                             (10.2)
```

Cremona--Fisher--Stoll Lemma 3.2 applies to every nonsingular degree-three
model, without a solubility hypothesis:

```text
v(Disc_plane)=v(Disc_Jac,min)+12 ell,
ell=min(floor(v(c4)/4),floor(v(c6)/6))                    (10.3)
```

in residue characteristic different from two and three. See
[*Minimisation and reduction of 2-, 3- and 4-coverings of elliptic curves*](https://www.dpmms.cam.ac.uk/~taf1000/papers/minred-234.pdf),
Lemma 3.2, pp. 8--9. It therefore includes the locally insoluble triple-fibre
case.

If the local length of `T` is `k`, (10.1) makes `ell=k` **exactly**. The safe
valuation statement is consequently

```text
k=1: v(c4)>=4, v(c6)>=6, v(Disc)>=12,
     and [v(c4)<8 or v(c6)<12];
k=2: v(c4)>=8, v(c6)>=12, v(Disc)>=24,
     and [v(c4)<12 or v(c6)<18].                          (10.4)
```

Also `v(Disc_plane)-v(Disc_min)=12k` exactly. The producer's `4/6/12` and
`8/12/24` lower bounds are confirmed. Exactness supplies the additional upper
disjunction and makes the proposed threat locus smaller. Actual minimization
is useful to classify survivors; it is not needed to recover `ell` from
`c4,c6` in this characteristic.

## 11. Diagonal and generalized-Hesse controls

**Disposition: `CONFIRMED`.**

For

```text
F=x^3+A y^3+B z^3+C xyz,
```

the CFS/Fisher normalization obtained from CFS equation (2.4) is

```text
c4   = C(C^3-216AB),
c6   = -C^6-540ABC^3+5832A^2B^2,
Disc = -AB(C^3+27AB)^3.                                  (11.1)
```

Nonzero scalar constants are units over `C` and do not affect the following
orders.

1. For `x^3+t(y^3+z^3)`, (11.1) gives discriminant order eight. The total
   surface has exactly three singular points on the central line. At each,
   the local equation is analytically `uv+x^3`, hence type `A2`; the surface
   is normal. Resolution introduces fibre multiplicities `1,2` in addition
   to the strict line of multiplicity three, so the fibre gcd is one: this is
   not a triple fibre after resolution.
2. For `x^3+t y^3+t^2 z^3`, (11.1) gives discriminant order twelve. There is
   one isolated hypersurface singularity. In the chart `z=1`, completing the
   square with `T=t+y^3/2` gives
   `x^3+T^2-y^6/4`, the simple-elliptic singularity of type `tilde E8`.
   Hence the total surface is normal. Its ternary-cubic level is one.
3. For

   ```text
   A=t+3t^3,  B=t^2,  C=-3t-3t^3,
   ```

   one has

   ```text
   C^3+27AB=-27t^7(3+t^2).
   ```

   Formula (11.1) gives precisely

   ```text
   (v(c4),v(c6),v(Disc))=(4,6,24).                        (11.2)
   ```

   The central total-space singularity is unique and isolated, so the
   hypersurface is normal. Equation (10.3) gives level one, with minimal
   Jacobian discriminant order twelve and `c4_min` a unit; the Jacobian has
   type `I_12`. The model is a critical, strictly-henselian-insoluble ternary
   cubic of period three. LLR Theorem 6.6 then identifies the minimal regular
   torsor fibre as type `3I_12` (LLR, pp. 496--498). This is the safe exact
   resolution-fibre type. The Hesse surface singularity must not be called
   simple elliptic without a separate explicit resolution.

Thus discriminant order 24 alone does not imply level two. The Hesse control
has order 24 but level one, exactly as intended.

## 12. Triple line, finite jets, and saturation semantics

**Disposition: `CONFIRM_WITH_CORRECTIONS`.**

In the `m=3` case, `g^*(t_0)=3P_0`. Pullback through every blowup preserves
divisibility of all fibre-component coefficients by three. Since `r` is an
isomorphism at the generic point of every component of the normal surface
fibre, the multiplicity of each plane component equals that of its strict
transform. A pure plane cubic of total degree three whose component
multiplicities are all divisible by three can only be

```text
X_(t0)=3L.                                                  (12.1)
```

After a constant plane change and a projective base coordinate with `t_0=0`,
the global `O_P1(3)` coefficient bound gives the exact polynomial jet

```text
F=x^3+tG_1+t^2G_2+t^3G_3.                                (12.2)
```

This makes the calculation finite-dimensional and gives finitely many
coefficient equations. It does **not** give finitely many candidate models:
the stabilizer of the line and the jet parameter spaces are positive
dimensional. “Finite orbitwise calculation” must mean finite-type algebraic
elimination after finitely many central cubic strata, not enumeration of a
finite set.

The saturation instruction needs an exact ring and open locus. For the
triple-line chart take

```text
R=C[coefficients of G_1,G_2,G_3]
```

or an explicitly declared quotient/slice of it. Let `I_2` be generated by the
coefficients below `t^8` in `c4` and below `t^12` in `c6`. Exact level two is
the additional open union from (10.4): one of the coefficients of `t^8`,
`t^9`, `t^10`, or `t^11` in `c4` is nonzero, or one of the coefficients of
`t^12`, ..., `t^17` in `c6` is nonzero. It must be handled on the
corresponding finite principal-open cover, not inserted among the generators
of `I_2`. The coefficients below `t^24` in `Disc` are redundant in
characteristic zero by
`c4^3-c6^2=1728 Disc`, but are useful as a positive control.

Generic smoothness is the open condition that the discriminant is not the
zero polynomial. Normality of the universal total hypersurface is also an
open condition here; computationally it must be obtained from the universal
Jacobian incidence/height or an equivalent conductor/Fitting test. Work on a
finite principal-open cover of

```text
U=U_(generic-smooth) intersect U_normal.
```

If a closed bad locus has ideal `J_bad`, then `I:J_bad^infinity` describes the
closure of `V(I)\V(J_bad)`; it can reintroduce bad boundary points. Therefore
one must retain the localization/open condition when interpreting output and
run both controls: a known normal generic-smooth model must survive, and a
known nonnormal or generically singular model must be removed.

A nonempty necessary locus is only a list of local/global coefficient
candidates. It is not a normal surface until normality is checked, not a
surface dominated by `A2` until that separate hypothesis is supplied, and not
a polynomial map or a counterexample.

## 13. Corrected four rows

The complete safe table is:

| type | base defect `T` | pushed discrepancy `D` | local GR lengths | exact local levels | minimum `h`-blowups | `rho(Y)` | section |
|---|---|---|---|---|---:|---:|---|
| no multiple | `t1+t2`, `t1!=t2` | `-F_t1-F_t2` | `(1,1)` | `(1,1)` | 2 | `>=12` | yes |
| no multiple | `2t` | `-2F_t` | `2` | `2` | 2 | `>=12` | yes |
| `F_0=3P_0` | `t0+t1`, `t1!=t0` | `-P_0-F_t1` | `(1,1)` | `(1,1)` | 2 | `>=12` | no |
| `F_0=3P_0` | `2t0` | `-4P_0` | `2` | `2` | 4 | `>=14` | no |

The levels in the table are CFS levels of the given integral plane cubic at
the indicated base points. They are not the integers `b_t`; in the last row
the numbers are `2` and `4`, respectively.

## 14. Maximum-safe theorem

Assume the binding degree-three adjoint theorem for an integral normal
class-`(3,3)` hypersurface `X subset P2 x P1` over `C`, dominated rationally
by `A2`, and let `r:Y->X` be its minimal projective resolution. Then:

1. `q` and `f=q r` are flat connected genus-one fibrations;
   `q_*omega_(X/P1)=O(3)` and `f_*omega_(Y/P1)=O(1)`.
2. The GR trace induces

   ```text
   0 -> O(1) --s--> O(3) -> q_*Q_rel -> 0,
   Q_rel=Q_GR tensor q^*O(2),
   div(s)=q(Z_GR)=T,
   length(T)=2.
   ```

3. `Delta=K_Y-r^*K_X<=0`; a connected block is zero exactly when the
   corresponding Gorenstein singularity is Du Val.
4. Relative minimalization gives a rational surface `S`, a vertical
   `D=h_*Delta<=0`, and `K_S=F+D`. There is either no multiple fibre and a
   section, or one triple fibre and no section.
5. Base supports agree, and the four rows in Section 13 are exhaustive. The
   Picard bounds for the minimal resolution are `12,12,12,14`.
6. At a point of local GR length `k`, the given ternary cubic has CFS level
   exactly `k`, satisfies (10.1), and obeys the sharpened bounds (10.4). In the
   triple-fibre case its central plane fibre is a triple line.

This theorem classifies only the relatively minimal multiplicity, the
length-two base defect scheme, the pushed discrepancy, local Hodge levels,
and Picard lower bounds. It does not classify `Delta`, Kodaira types at every
fibre, all singularities of `X`, or the existence of a compatible global
surface, dominant map, polynomial map, or Jacobian-conjecture counterexample.

## 15. Exact dependencies: quoted theorems versus deductions

Quoted primary inputs:

- the binding adjoint/GR-defect theorem supplied in the charge;
- Grothendieck's coherent relative duality in Exposé 149;
- Grauert--Riemenschneider Satz 2.3 for higher direct-image vanishing;
- Mumford's negative definiteness of the exceptional intersection form;
- Artin's characterization of rational/Gorenstein surface singularities and
  rational double points;
- Kodaira Section 12 and Seiler Theorem 1.1 for the canonical bundle formula,
  primitive multiple-fibre coefficients, and tame/wild torsion;
- Liu--Lorenzini--Raynaud Theorems 3.1 and 6.6 for the Lie/Hodge comparison
  and torsor fibre type;
- Fisher Lemma 2.2 and Propositions 5.19/5.23 for invariant-differential
  weights and normalization;
- Cremona--Fisher--Stoll Theorem 2.8 and Lemma 3.2 for model invariants and
  level, including insoluble models.

Deductions in this review, not quotations from those sources, are: flatness
from equidimensional plane fibres; the length comparison in (2.1); the
annihilator proof of (2.2); anti-effectivity from the inverse matrix; the
horizontal `(-1)`-curve inequality; `m|3`; support transfer via (4.2); the two
global integer equations; exhaustion of the four rows; the satellite-safe
blowup induction; the orientation (10.1) after choosing generators; the
sharpened upper disjunction in (10.4); the three local control calculations;
and the triple-line argument.

## 16. Cheapest decisive successor

The cheapest first decision is the strongest, smallest row: `m=3`, `T=2t0`.
Fix `t0=0` and `L=(x=0)`, use the finite ring in Item 12, and compute the
level-exact ideal

```text
t^8 | c4,        t^12 | c6,
and [t^12 does not divide c4 or t^18 does not divide c6]
```

on the declared normal and generic-smooth open locus. Use `Disc/t^24` as a
control, not as a substitute for the simultaneous conditions. If that open
locus is empty, the fourth row is eliminated. If nonempty, run exact local
resolution/minimization and retain only genuine normal models; nonemptiness
alone proves no global existence.

Then perform the analogous **global bidegree-`(3,3)`**, row-normalized jobs:
put two-support points at `0,infinity`, or the double point at `0`, and impose
the exact level-one or level-two conditions at every required point. The
global coefficient ring, rather than an unconstrained formal jet, is what can
test compatibility with degree three. All four rows must be addressed before
claiming an exclusion. Even a surviving global normal hypersurface still
does not supply the separate dominant-`A2` hypothesis or a polynomial map.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30970`.
- Body SHA-256:
  `8b46aac7130d093fee885255d2d1dd35e10d54028600f43dea0a18f2ee0ffb82`.
- Frozen basis: `7dd85a6598c56fa043dd397382de1c93d846fa39`.
