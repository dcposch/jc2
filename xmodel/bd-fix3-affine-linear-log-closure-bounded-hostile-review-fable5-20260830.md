# Bounded hostile review: affine-linear cubic block closure (Fable 5)

Reviewer: Fable 5 (hostile, different-model)  
Date: 2026-08-30 UTC  
Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`  
Charged claim: no proper cubic intermediate block of a hypothetical Keller
map has affine-linear Miranda coefficients in any fixed global trace-zero
basis.

Custody: all four frozen input SHA-256 hashes reverified at this basis;
producer body reverified (16015 bytes,
`0a82cca5...f1902b`). Binding inputs used as promoted, not re-audited:
structure sandwich `ba69b33f...`, Galois/nonmonogenicity `f9720718...`,
log-Kodaira theorem `ff25ba27...`. Desk review; only light sympy identity
checks, no Singular/heavy CAS, no `jc2-lean` contact. Producer sections 4
(almost-surjectivity), 5 (explicit control), 6 (general cubic corollaries)
are outside this bounded scope and were not audited.

Throughout: `A=C[u,v]` with `(u,v)=(f,g)` the Keller pair, `B=B_K` the
integral closure of `A` in the cubic intermediate field `K`, `d2=3`,
sandwich `A^2 --g1--> Y=Spec B --g2--> A^2` (binding). "Affine-linear"
means total degree `<=1` in `(u,v)`; the hypothesis is that SOME global
trace-zero `A`-basis of the trace-zero module realizes it.

## Item 1. Miranda table and `det(t,t^2)=Phi(r,s)` — CONFIRMED

Hypotheses actually needed: char 0 (2,3 invertible for trace splitting and
the table); `B` finite flat of rank 3 over `A` — this is where normality
enters: `B` normal makes `Y` CM, and miracle flatness over the regular base
gives finite flat (binding structure item 2); `A=C[u,v]` so Quillen–Suslin
makes `E=ker(tr)` free of rank 2; a chosen basis `(z,w)` of `E`. No
Gorenstein hypothesis is needed for the table.

Derivation, independently redone. `B=A(+)E` since `tr(1)=3` is a unit. For
any basis, write `z^2=alpha+az+bw`, `zw=beta+ez+fw`, `w^2=gamma+cz+dw`.
Trace-zero of `z,w` forces, from the diagonal of the multiplication
matrices, `f=-a` and `e=-d`. The constants are then forced: the
`A`-component of `x` is `tr(x)/3` and `tr(x)` is the trace of the
multiplication matrix, giving `3alpha=tr(M_z^2)=2alpha+2(a^2-bd)`, so
`alpha=2(a^2-bd)`; symmetrically `gamma=2(d^2-ac)`; and
`3beta=tr(M_zM_w)=2beta+(bc-ad)`, so `beta=-(ad-bc)`. I verified
associativity of the resulting table by hand ((zz)w=z(zw) both give
constant `-a^2d-abc+2bd^2`, z-coeff `bc-ad`, w-coeff `a^2-bd`). The table
is exactly the producer's.

For `t=rz+sw`, the trace-zero part of `t^2` is
`(ar^2-2drs+cs^2, br^2-2ars+ds^2)`, and
`det(t,t^2)=r(br^2-2ars+ds^2)-s(ar^2-2drs+cs^2)=Phi(r,s)` with
`Phi=bX^3-3aX^2Y+3dXY^2-cY^3` (symbolically reverified). Lemma 2.1:
`B=A[t]` iff `(1,t,t^2)` is a basis of the free rank-3 module iff the
transition determinant is in `A^*=C^*`; subtracting the `A`-part of `t`
changes nothing, and a 3-element generating set of a free rank-3 module is
automatically a basis. Hence `B` monogenic over `A` iff `Phi(r,s) in C^*`
for some `r,s in A` — a unit of `C[u,v]`, i.e. a nonzero scalar. Binding
nonmonogenicity (Galois integration section 1 item 5) therefore forces
`Phi(r,s) not-in C^*` for all `r,s in A`. The coefficients `(a,b,c,d)`
are basis-dependent; the affine-linear hypothesis is quantified over an
existential basis choice and stays so in the promoted statement.

## Item 2. Common-zero uniqueness repair — CONFIRM_WITH_CORRECTIONS

The producer's phrase "integrality makes the common zero unique" is not a
proof; the prompt's normality argument is correct and I confirm it.

The common zero locus of four affine-linear functions is an affine
subspace: empty, a point, a line, or `A^2`. All of `A^2` means
`a=b=c=d=0`, `Phi=0`, and every fibre algebra is `C[z,w]/(z,w)^2`, not a
domain — impossible since `K` is a field. Suppose the locus contains a
line `L`. Localize at its generic point: `O=O_{A^2,eta_L}` is a DVR with
residue field `kappa=C(L)`, and `B_eta=B(x)O` is a normal (localization
of the integrally closed `B_K`) semilocal Dedekind ring, finite flat of
rank 3 over `O`. Its special fibre is computed from the table: along `L`
all of `a,b,c,d` vanish, and the six structure constants lie in the square
of the ideal of `L`, so

```text
B_eta/mB_eta = kappa[z,w]/(z,w)^2:
radical N=(z,w), dim_kappa N=2, N^2=0, local.
```

Locality forces a single maximal prime `q` over `m`, so `ef=3` with
`(e,f)=(3,1)` or `(1,3)`. If `(1,3)` the fibre is a cubic field extension
of `kappa` with radical zero — contradiction with `dim N=2`. If `(3,1)`
(rank-three totally ramified), the fibre is `B_q/(t^3)` for a uniformizer
`t` of the DVR `B_q`, whose radical `(t)` has `(t)^2=(t^2)!=0` mod
`(t^3)` — contradiction with `N^2=0`. So no line exists; a nonempty common
zero locus is one point. Translating it to the origin replaces `(f,g)` by
`(f-u_0,g-v_0)`, which preserves `C[f,g]`, Keller, and affine-linearity,
and makes `a,b,c,d` linear, i.e. `Phi=uP1+vP2`, `P0=0`.

## Item 3. Isolated common zero: the `O(-3)` bridge — CONFIRM_WITH_CORRECTIONS

The producer identified the incidence parametrization with `Spec B`
without argument. The missing bridge is proved as follows, on `B` itself.

**Grading.** With `deg u=deg v=deg z=deg w=1`, linear `a,b,c,d` make every
table relation homogeneous of degree 2, so `B` is a graded domain with
`B_0=C`, generated in degree 1 by `u,v,z,w` (independent: `1,z,w` is a
free basis and `u,v in A`). Freeness gives the exact Hilbert function
`Hilb_B(n)=(n+1)+2n=3n+1`.

**Twisted-cubic Proj.** `X=Proj B` is an integral projective curve. Since
`B` is a 2-dimensional domain, `H^0_{B+}(B)=0`, so `B` injects into
`Gamma_*(O_X)`, which is a finite `B`-module; the cokernel has finite
length, so `chi(O_X(n))=3n+1`: degree 3, `p_a=0`. Nondegenerate in
`P^3=P(B_1^v)` because a vanishing linear form would be a zero divisor in
the domain `B`. An integral nondegenerate degree-3 curve in `P^3` is the
rational normal cubic, so `X=P^1` with `O_X(1)=O_{P^1}(3)`. Then
`Gamma_*=(+)_n H^0(P^1,O(3n))` has Hilbert function `3n+1` in every
degree, equal to `Hilb_B`, so the injection is an equality:

```text
B = (+)_{n>=0} H^0(P^1,O(3n)),
```

the cone over the twisted cubic. Its resolution is the affinization
`Tot O_{P^1}(-3) -> Y`, proper birational, contracting exactly the zero
section (the unique complete curve, since `O(-3)` is negative) to the
vertex `V(B_+)`, which maps to `(0,0) in A^2` because `u,v in B_+`.

**Literal map.** `gcd(P1,P2)=1` must be proved, and the producer's field
argument is repaired thus: if `q=[r_0:s_0] in P^1(C)` satisfies
`P1(q)=P2(q)=0` then `Phi(r_0,s_0)=0` identically on `A^2`, so
`t_0=r_0z+s_0w` has `det(t_0,t_0^2)=0`; since `t_0` has constant nonzero
`E`-coordinates, `t_0^2 in C(u,v)+C(u,v)t_0`, so `[C(u,v)(t_0):C(u,v)]<=2`
divides 3, forcing `t_0 in C(u,v) cap B = A`; but `0!=t_0 in E` and
`A cap E=0`, contradiction. (The same argument, verbatim, rules out a
common zero of `P0,P1,P2` in item 4.) Also `P1,P2!=0`: if `P1=0` then
`gcd` fails at any root of `P2` by the same mechanism. With basepoint-free
`(P1,P2)`, the incidence surface `{uP1+vP2=0} subset A^2 x P^1` is the
kernel of `O^2 --(P1,P2)--> O(3)`, a line bundle of determinant `O(-3)`,
hence `= Tot O(-3)`, and the never-vanishing kernel section `(-P2,P1)`
trivializes it: the literal map `(u,v)=tau*(-P2,P1)` is exactly this
trivialization, and its composite to `A^2` contracts `tau=0` to the
origin. This matches the cone model; but note the exclusion below does not
need the literal identification, only the intrinsic cone structure.

**Exclusion.** From the grading: units of the graded domain are
homogeneous of degree 0, so `O(Y)^*=C^*`; and `Cl(Y)=Cl(P^1)/Z<O(3)>=Z/3`
(the section ring is by construction projectively normal). Binding
structure item 4 gives `R` nonempty of pure codimension one and
`g1(A^2) subset Y\R=U`. Localization for normal `Y`:

```text
C^* -> O(U)^* -> (+)_i Z[R_i] --cl--> Cl(Y)=Z/3.
```

The class map from a nonzero free group to a finite group has nonzero
kernel, and that kernel is the image of `O(U)^*/C^*`; so `U` has a
nonconstant unit `phi`. Then `g1^*phi` is a nowhere-zero polynomial, hence
a scalar `c`; dominance makes `O(U)->C[x,y]` injective, so `phi=c`,
contradiction. The common-zero case is dead. CONFIRMED with the bridge
supplied; the producer's `Cl(Y)=Z/3`, `O(Y)^*=C^*` statements are correct.

## Item 4. No common coefficient zero: incidence torsor — CONFIRM_WITH_CORRECTIONS

Now `(a,b,c,d)` have no common zero, equivalently `Phi_{(u,v)}` is never
the zero form. Write `Phi=P0+uP1+vP2`.

**Field forbids a common `Pi` zero.** Proved above (quadratic-element
argument); the producer's one-line version is replaced by it.

**`S_X=empty`.** If `q=[r_0:s_0]` has `P1(q)=P2(q)=0!=P0(q)`, then
`Phi(r_0,s_0)=P0(r_0,s_0) in C^*` with constant `r_0,s_0 in A`, so Lemma
2.1 makes `B` monogenic, contradicting the binding nonmonogenicity. So
`S_X=empty`, and with the previous paragraph `(P1,P2)` is basepoint-free;
this also covers `P1=0` or `P2=0` (a root of the other cubic would lie in
`S_X` or be a common zero of all three; and `P1=P2=0` makes `Phi=P0`
represent a nonzero scalar at some `C`-point, again monogenic). Hence
`rho=[P1:P2]:P^1->P^1` is a morphism of degree exactly 3 (nonconstant:
proportional `P1,P2` have common roots), and the homogeneous Wronskian
`W=P1P2'-P2P1'` is nonzero, since `W=0` in char 0 forces linear
dependence, already excluded.

**Gorenstein/incidence bridge, proved.** `I_Phi={Phi=0} subset A^2xP^1`
is smooth (the `u,v` partials are `P1,P2`, basepoint-free), and
`pi:I_Phi->A^2` is finite (proper with finite fibres: no fibre cubic
vanishes) and flat (CM over regular, fibres length 3). The bridge
`Spec B ~= I_Phi` over `A^2` does not need Gorenstein duality; it follows
from the presentation. First, the Miranda table is a presentation:
`A[z,w]/(three table relations)` is spanned by `1,z,w` and surjects onto
the free rank-3 `B`, hence is `B`. Second, `Gamma(I_Phi)` contains the
elements glued from the two charts

```text
omega=(b*lam | 3a-3d*mu+c*mu^2),  theta=(b*lam^2-3a*lam+3d | c*mu),
```

(`lam=X/Y`, `mu=Y/X`; regularity across charts checked by division in
`A[lam]/(phi)`), and direct reduction modulo `phi=b*lam^3-3a*lam^2+3d*lam-c`
gives (symbolically reverified)

```text
omega^2=3a*omega+b*theta-3bd,  omega*theta=bc,
theta^2=c*omega+3d*theta-3ac,
```

whose trace-zero shift `(omega-a, theta-d)` satisfies exactly the Miranda
table of `(a,b,c,d)`. So there is an `A`-algebra map
`B -> C:=pi_*O_{I_Phi}` sending `(1,z,w)` to `(1,omega-a,theta-d)`. `C` is
free of rank 3 (pushforward of the Koszul sequence of the divisor:
`C=A(+)R^1pi_*O(-3)`, rank `1+2`). The map is an isomorphism iff the image
triple is a fibrewise basis; finite flatness lets one check on each fibre
`C(x)kappa(p)=H^0` of the length-3 zero scheme of `Phi_p`. If `b(p)!=0`
the fibre lies in the `lam`-chart and `(1, b*lam, b*lam^2-...)` is
triangular with unit leading coefficients; symmetrically if `c(p)!=0`. If
`b(p)=c(p)=0`, then `Phi_p=-3XY(aX-dY)` with `(a,d)(p)!=(0,0)`; for
`a,d!=0` the value matrix at the three distinct points has determinant
`9ad!=0`; for `a=0` (resp. `d=0`) the fibre ring is
`kappa[lam]/(lam) x kappa[mu]/(mu^2)` and the value/jet matrix has
determinant `+-9d^2` (resp. symmetric), nonzero. So `Spec B ~= I_Phi`
over `A^2` in every coefficient degeneration. 

**Torsor invariants.** `q:Y->P^1` has fibres
`{uP1(q)+vP2(q)=-P0(q)}`, affine lines: `Y` is a torsor under
`ker(O^2->O(3))=O(-3)`, Zariski-locally `A^1xA^1`. Units restrict to
constants on fibres, hence come from `P^1`: `O(Y)^*=C^*`. For an affine
bundle, `q^*:Pic(P^1)->Pic(Y)=Cl(Y)` is an isomorphism: `Cl(Y)=Z`,
generated by `q^*O(1)`. CONFIRMED.

## Item 5. Reducible ramification — CONFIRMED

If `R=R_1 cup ... cup R_k`, `k>=2` (pure codim 1, binding), localization
gives `C^* -> O(U)^* -> Z^k --cl--> Cl(Y)=Z`. Any map `Z^k->Z` with
`k>=2` has nonzero kernel by rank alone — no individual class needs to be
proved nonzero, so the argument does not consume the class-lattice
injection. A nonzero kernel element lifts to a nonconstant unit on `U`;
`g1(A^2) subset U` (binding) pulls it back to a nowhere-zero polynomial,
a scalar, and dominance-injectivity of `O(U)->C[x,y]` makes the unit
itself scalar: contradiction. So `R` is irreducible. CONFIRMED.

## Item 6. Irreducible support: `F=dF=0` — CONFIRM_WITH_CORRECTIONS

In char 0, `g2=pi` finite flat is étale at `y=(u,v,q)` iff the fibre
cubic is reduced at `q`; so the non-étale set is
`{Phi=0, d_{P^1}Phi=0}`. In the `lam`-chart, for fixed `lam`, the two
equations are affine-linear in `(u,v)` with matrix
`[[p1,p2],[p1',p2']](lam)`, determinant the inhomogeneous Wronskian
`w(lam)`, whose zero set (both charts) is exactly `Crit(rho)`, including
directions ramified over `rho=infinity`.

Off `Crit(rho)`: unique solution — one graph point, genuinely non-étale
(double root there), so the graph over `P^1\Crit(rho)` is nonempty and
contained in `R`. Its closure in `Y` is an irreducible curve; `R`
irreducible of pure dimension 1 forces `R = ` that closure. At
`s in Crit(rho)` the matrix has rank exactly 1 (rank 0 would need
`P1(s)=P2(s)=0`, excluded by basepoint-freeness), so the solution set is
empty or an entire affine line — the whole fibre `q^{-1}(s)`, since the
fibre is itself the solution line of the first equation. A whole vertical
fibre inside `R` would force the irreducible `R` to equal it,
contradicting that `R` dominates `P^1`. Hence the system is inconsistent
at every critical direction: `R` has no point over `Crit(rho)`, and since
`R` is closed in `Y`, the graph is already closed. Cramer's rule gives a
morphism `P^1\Crit(rho) -> Y` splitting `q|_R`; a section of a separated
morphism is a closed immersion, and its image is `R` set-theoretically, so
the reduced scheme satisfies

```text
R ~= P^1 \ Crit(rho).
```

Purity enters through the binding pure-codimension-one statement (which
forbids `R` from being a point set and underwrites the case split); the
fixed-sheet/transposition input is NOT load-bearing for the closure — it
feeds only the producer's divisor-multiplicity and `Pic`-generator
decorations (`omega_Y=q^*O(1)`, `Cl(U)=0`, `chi_c`), which the bounded
chain never uses and which I did not audit.

**Riemann–Hurwitz.** `deg rho=3` gives ramification degree
`Sum_q (e_q-1) = 2*3-2 = 4` with each `e_q-1<=2`; one critical direction
could carry at most 2, so `#Crit(rho)>=2`. CONFIRMED.

**Ruled completion.** The torsor under `O(-3)` is classified by
`H^1(P^1,O(-3))` and embeds as the complement of a section `D_infinity`
in the `P^1`-bundle `P=P(V)`, `0->O(-3)->V->O->0`. `R` is closed in `Y`
and maps isomorphically to `P^1\S`, `S=Crit(rho)`. The binding log
theorem itself proves the closure `D_0` of `R` in `P` is a section
(proper quasi-finite birational onto normal `P^1`) meeting `D_infinity`
exactly over `S`; since `R` has no interior point over `S`, the closure
escapes to `D_infinity` there with some contact `m_s>=1`, and the theorem
is contact-independent. Hypothesis match verified, not assumed.

## Item 7. Log theorem + sandwich match — CONFIRMED

Binding theorem `ff25ba27` hypotheses: `P^1`-bundle `P` with section
`D_infinity`, `Y=P\D_infinity` (item 6), `R subset Y` closed with
`q|_R:R->P^1\S` an isomorphism (item 6), `#S>=2` (Riemann–Hurwitz).
Conclusion: `bar-kappa(U)>=0` and **no dominant morphism `A^2->U`**,
`U=Y\R`; only dominance is needed, no properness or étaleness. Binding
sandwich: `g1:A^2->Y` is dominant with `g1(A^2) subset Y_sm\R subset U`;
an image dense in `Y` and contained in the open `U` is dense in `U`, so
`g1:A^2->U` is dominant. Contradiction. The irreducible residual is dead,
completing the case tree: common zero on a line (item 2), at a point
(item 3), `S_X!=empty` (item 4), reducible `R` (item 5), irreducible `R`
(items 6–7) — every case terminates in a contradiction.

## Verdict and promotion

Itemized: 1 CONFIRMED; 2 CONFIRM_WITH_CORRECTIONS; 3
CONFIRM_WITH_CORRECTIONS; 4 CONFIRM_WITH_CORRECTIONS; 5 CONFIRMED; 6
CONFIRM_WITH_CORRECTIONS; 7 CONFIRMED.

**Overall: CONFIRM_WITH_CORRECTIONS.** All corrections are repairs of
proofs (uniqueness via DVR radicals; cone bridge via Hilbert `3n+1` and
twisted-cubic Proj; incidence bridge via presentation plus fibrewise
determinants including all coefficient degenerations; field/gcd via the
quadratic-element argument; critical-direction inconsistency via the
whole-fibre dichotomy); no producer conclusion in the load-bearing chain
was refuted.

Maximum exact theorem safe to promote:

> **Theorem AL3-CLOSED (basis-dependent affine-linear scope).** Assume the
> binding sandwich (`ba69b33f`), the binding nonmonogenicity
> (`f9720718`, section 1 item 5), and the binding log-Kodaira theorem
> (`ff25ba27`). Let `F=(f,g)` be a hypothetical non-invertible Keller map
> with an intermediate field `C(f,g) < K < C(x,y)`, `[K:C(f,g)]=3`, and
> `B_K` the integral closure of `A=C[f,g]` in `K`. If there exists a
> global trace-zero `A`-basis of the trace-zero module of `B_K` in which
> all four Miranda coefficients `a,b,c,d` are affine-linear in `(f,g)`,
> then contradiction. Equivalently: no proper cubic intermediate block of
> a Keller map has affine-linear Miranda coefficients in any fixed global
> trace-zero basis.

The affine-linear hypothesis is a property of a basis choice, quantified
existentially; nothing is asserted for bases in which the coefficients are
not affine-linear, and no invariance statement is promoted. Nonclaims:
nothing about nonlinear or higher-degree cubic Miranda coefficients,
primitivity, `d1`, existence of any block or intermediate field, any
counterexample, or JC2. The producer's sections 4–6 (almost-surjectivity
analysis, explicit `G_m`-ramified control, general cubic corollaries)
remain outside this verdict.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17843`.
- Body SHA-256:
  `9d131643ed51c13468e2fb2414f33923c481c919de78002da1e991479b244c76`.
- Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`.
