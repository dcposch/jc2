# Hostile review: degree-at-least-three adjoint-defect gate

Reviewer: Opus 5 (different-model hostile review)
Date: 2026-08-30 UTC
Target: `xmodel/bd-a2-d3plus-pg-defect-sol56-20260830.md` (PROVISIONAL PRODUCER)

## 0. Custody and overall verdict

All six charged files hash exactly as charged. The producer's internal seal is
self-consistent: body through the unique standalone `<!-- BODY-END -->` is
`10372` bytes with SHA-256
`01daaf7e8e786a3e759c8e1147249476a78376da6c21e68b07d5173ed0978051`, matching
both the seal block and the artifact JSON. **No correctness is inferred from
this**; every claim below was reconstructed from scratch.

No CAS, no Singular, no web search, no AWS. `jc2-lean` not touched. No sibling
ideation/q6/other-model material read. No inputs, Git state, or canonical
artifacts modified.

Overall: **CONFIRM_WITH_CORRECTIONS.** The mathematical core is correct and
stronger than I expected; I found no false theorem. The corrections are (i) a
wrong general Newton criterion in the negative control (right answer, wrong
rule), (ii) a missing surjectivity proof for `q` at `d=3`, (iii) a
duality-versus-isomorphism conflation in the pointwise step, (iv) an
unnecessary right-exactness in the five-term sequence, and (v) an unnecessary
appeal to Castelnuovo. Two free corroborations are supplied in §11.

Itemized verdicts:

```text
1  ambient cohomology / adjunction / factor two   CONFIRMED
2  unirational -> rational, H^1=H^2=0             CONFIRM_WITH_CORRECTIONS
3  Leray bridge (0.1)                             CONFIRM_WITH_CORRECTIONS
4  GR trace inclusion, J_GR, Q_GR                 CONFIRMED
5  cohomology of GR sequence, (0.2), (3.3)        CONFIRM_WITH_CORRECTIONS
6  d=3 adjunction, omega_X=q^*O(1)                CONFIRM_WITH_CORRECTIONS
7  length/image argument, Z_GR ~= T               CONFIRMED
8  exhaustive length-two alternatives             CONFIRMED
9  x^3+y^4+z^5 negative control                   CONFIRM_WITH_CORRECTIONS
10 smooth d>=3 special case (Sec. 5)              CONFIRMED
11 proposed successor D3-ADJOINT-HORIZONTALITY    ACCEPTED_WITH_FIREWALLS
```

## 1. Ambient cohomology and adjunction — CONFIRMED

`W=P2 x P1` is smooth, so any hypersurface is automatically Cartier and
(1.1) is the ideal sequence of an effective Cartier divisor. This needs no
flatness, no Cohen--Macaulay hypothesis, and no smoothness of `X`. `X` is CM
and Gorenstein as a *consequence* (hypersurface in a smooth variety), not as
an assumption; `omega_X` invertible follows. Normal + surface gives
`Sing(X)` finite by Serre `R1+S2` (`S2` automatic).

Kunneth for `O(a) box O(b)`:

```text
H^0(P2,O(-d))=0 (d>=1),  H^1(P2,O(n))=0 (all n),
h^2(P2,O(-d))=h^0(P2,O(d-3))=(d-1)(d-2)/2   [Serre, omega_P2=O(-3)],
H^0(P1,O(-3))=0,  h^1(P1,O(-3))=h^0(P1,O(1))=2.
```

So the only nonvanishing Kunneth term is `(i,j)=(2,1)` and
`h^3(W,O_W(-d,-3))=2*(d-1)(d-2)/2=N_d`. **The factor of two is exactly
`h^1(P1,O(-3))=3-1=2`.** I checked its provenance: for class `dA+eB` one gets
`N_{d,e}=(e-1)(d-1)(d-2)/2`, so the `2` is `e-1` with `e=3`, i.e. it is the
`P1`-degree of the class, not a doubling of the plane-curve genus. (Both
readings coincide at `e=3` because `e-1=2`; see the corroboration in §11.)

`H^i(W,O_W)=0` for `i>0` including `i=3` (needs `H^2(P2,O)=0`). The long
exact sequence of (1.1) then gives (1.3) verbatim: `H^1(X,O_X)=0` (squeezed
between two zeros) and `H^2(X,O_X) ~= H^3(W,O_W(-d,-3))`, so `h^2(O_X)=N_d`.

Adjunction: `omega_W=O_W(-3,-2)`, hence
`omega_X=(omega_W(X))|_X=O_X((d-3)A+B)`, which is (1.4). Serre duality on the
projective CM scheme `X` with dualizing sheaf `omega_X` gives
`h^0(omega_X)=h^2(O_X)=N_d`; no smoothness needed. Independent check: the
restriction sequence `0->O_W(-3,-2)->O_W(d-3,1)->omega_X->0` has
`H^0=H^1=0` for `O_W(-3,-2)`, so

```text
H^0(X,omega_X) ~= H^0(P2,O(d-3)) tensor H^0(P1,O(1)),   dim = N_d.   (R1)
```

(R1) is a free strengthening the producer does not state: the canonical
system is the *complete Segre system* of the ambient class, not merely
`N_d`-dimensional. Consistency at `d=2`: `N_2=0`, matching the charged
quadratic integration's `H^2(X,O_X)=0`. Consistency at `d=3`: `N_3=2`.

## 2. Passage through the resolution — CONFIRM_WITH_CORRECTIONS

The conclusion is true. Two repairs.

**(2a) No compactification step is needed, and it should not be invoked.**
Dominant rational maps of integral `C`-varieties correspond contravariantly to
`C`-embeddings of function fields. `A2 --> X` dominant gives
`C(X) -> C(x,y)`; `r` birational gives `C(Y)=C(X)`; and
`C(x,y)=C(A2)=C(P2)`. So `C(Y) -> C(P2)` is an embedding of fields of the
same transcendence degree `2`, hence `C(P2)/C(Y)` is algebraic and finitely
generated, hence finite. That *is* a dominant generically finite rational map
`P2 --> Y`, with no compactification argument. Composability is automatic in
the function-field formulation; the producer's phrasing invites the reader to
verify a composite of rational maps, which is the fragile route.

**(2b) Castelnuovo is not needed and should be removed from the load path.**
The producer only uses `H^1(O_Y)=H^2(O_Y)=0`. Resolve indeterminacy
`P2 <- Z -> Y` with `Z` smooth projective and `f:Z->Y` generically finite.
In characteristic zero `df` is generically an isomorphism, so
`f^*Omega^1_Y -> Omega^1_Z` and `f^*(omega_Y)^{m} -> omega_Z^{m}` are
injective maps of torsion-free sheaves, giving injections
`H^0(Y,Omega^1_Y) -> H^0(Z,Omega^1_Z)` and
`H^0(Y,mK_Y) -> H^0(Z,mK_Z)`. Birational invariance identifies the right sides
with `H^0(P2,Omega^1)=0` and `H^0(P2,mK)=0`. Hence `q(Y)=p_g(Y)=0`, and Hodge
theory on the smooth projective `Y` gives `h^1(O_Y)=q=0`, `h^2(O_Y)=p_g=0`.
This is exactly (2.1) with no Lüroth/Castelnuovo input. It is also the method
already used in the charged rational-forest integration §1, so the producer's
heavier route is a regression, not an upgrade.

Castelnuovo's criterion (Beauville, *Complex Algebraic Surfaces*, 2nd ed.,
Thm. V.1, with the standard char-0 corollary that a unirational surface is
rational) does apply and does give rationality of `Y`; but rationality is a
strictly stronger conclusion than the argument consumes, so it must not be a
dependency. **Repair: replace "Thus `Y` is unirational and, in characteristic
zero, rational" by the forms argument, and demote "`Y` is rational" in the
theorem statement to a remark.**

**(2c) Recorded hypothesis.** `Y` must be smooth *projective* for Hodge theory
and Serre duality. Hironaka supplies a projective resolution of the projective
surface `X`. The producer writes only "let `r:Y->X` be a resolution"; add
"projective".

## 3. Leray bridge — CONFIRM_WITH_CORRECTIONS

`r_*O_Y=O_X` by Zariski's main theorem (`X` normal, `r` proper birational).
Fibres of `r` have dimension `<=1`, so `R^2r_*O_Y=0`; `R^1r_*O_Y` is coherent
with support in `Sing(X)`. I verified the support claim in the *stronger* form
the producer needs but does not state: even if `r` is not an isomorphism over
`X_sm`, it is a composite of blowups there, and smooth points are rational
singularities, so `R^1r_*O_Y` and (below) `J_GR` are still trivial off
`Sing(X)`. Finite support kills `H^p` for `p>0`, so `H^0` is the finite total
length.

**(3a) Correction.** The displayed sequence terminates
`-> H^2(Y,O_Y) -> 0`. The standard five-term exact sequence is
`0 -> E_2^{1,0} -> H^1 -> E_2^{0,1} -> E_2^{2,0} -> H^2` and asserts nothing
about surjectivity onto `H^2`. Delete the `-> 0`. Nothing is lost: exactness
at `E_2^{2,0}=H^2(X,O_X)` is genuine (`E_3^{2,0}=E_inf^{2,0}` injects into
`H^2(Y,O_Y)`), and `H^2(Y,O_Y)=0` already forces surjectivity of
`H^0(R^1r_*O_Y) -> H^2(X,O_X)`. With `H^1(X,O_X)=H^1(Y,O_Y)=0` the map is also
injective, so (2.2) and hence (0.1) hold:

```text
sum_(p in Sing X) p_g(X,p) = h^2(O_X) = N_d >= 2   for d >= 3.
```

**(3b) Canonicity and resolution-independence: CONFIRMED.** For a proper
birational `h:Y''->Y` of smooth surfaces, `h_*O=O` and `R^1h_*O_{Y''}=0`, so
`R^1r''_*O_{Y''}=R^1r_*O_Y`; dominating any two resolutions by a third gives
independence. The Leray edge map is canonical once `r` is fixed, and the
module is `r`-independent, so the isomorphism (2.2) is canonical.

**(3c)** "Every `d>=3` normal survivor is singular and has at least one
nonrational singularity" is correct (`N_d>0`), as is "Gorenstein rational
surface singularity = Du Val" (Artin, *Amer. J. Math.* 88 (1966); standard
form e.g. Reid, *Chapters on Algebraic Surfaces*, Thm. 4.20). This is precisely
where any import of the charged **quadratic** conclusions would be fatal:
at `d=2`, `N_2=0` and every singularity *is* Du Val and `r` *is* crepant. The
producer correctly imports none of that. I confirm the firewall holds: no
`d=2` conic/Du Val/`D9`/crepancy statement is used anywhere in the `d>=3`
argument, and each is *false* at `d>=3`.

## 4. Grauert--Riemenschneider trace inclusion — CONFIRMED

**Direction.** `r_*omega_Y -> omega_X` is the degree-`0` cohomology of the
Grothendieck duality trace `Rr_*omega_Y[2] -> omega_X[2]`. It is injective
because `r_*omega_Y` is torsion-free and the map is an isomorphism on the dense
open where `r` is an isomorphism, so its kernel is torsion. The inclusion is
into `omega_X`, i.e. **adjoint (pole-free) forms sit inside the dualizing
sheaf** — the producer's direction is right. Concretely, writing
`Delta := K_Y - r^*K_X` (an integral `r`-exceptional divisor, integral because
`X` is Gorenstein), the projection formula gives the explicit description

```text
J_GR = r_*O_Y(K_Y - r^*K_X)  subset  O_X,
r_*omega_Y = J_GR tensor omega_X.                                   (R2)
```

`J_GR subset O_X` because a rational function `f` with
`div(f)+Delta >= 0` is regular off a finite set, hence regular by normality.
This makes uniqueness of `J_GR` in (3.1) immediate (`omega_X` invertible), and
shows `J_GR=O_X` off `Sing(X)`, so `O_X/J_GR` has finite length and
`Q_GR = O_{Z_GR} tensor omega_X` is exact (tensoring by an invertible sheaf).
`Z_GR` is *zero-dimensional*: **CONFIRMED**. `Z_GR = empty` iff `Delta >= 0`
iff `X` is canonical iff all singularities are Du Val, which is excluded here.

**Non-saturation.** `J_GR` need not be integrally closed, radical, or a power
of the maximal ideal; the argument uses only finite colength, so this is
harmless. But it is a firewall: `Z_GR` is **not** the reduced singular set and
**not** a multiplier/adjoint ideal of any divisor pair. Sanity witness: for the
cone over a plane cubic, `Delta=-E`, `J_GR=m`, colength `1=p_g`.

**GR hypotheses.** Grauert--Riemenschneider (*Invent. Math.* 11 (1970),
Satz 2.3) requires `Y` smooth, `r` proper, `r` generically finite/semi-small.
All hold; `X` need be neither normal nor Gorenstein for GR itself. Hence
`R^i r_*omega_Y=0` for `i>0` (also directly `R^2=0` by fibre dimension), the
Leray spectral sequence degenerates, and
`H^i(X,r_*omega_Y)=H^i(Y,omega_Y)` for all `i`. Serre duality on `Y`:
`H^0(Y,omega_Y)=H^2(O_Y)^v=0`, `H^1(Y,omega_Y)=H^1(O_Y)^v=0`. **CONFIRMED.**

## 5. Cohomology of the GR sequence — CONFIRM_WITH_CORRECTIONS

Full long exact sequence, no endpoint skipped:

```text
0 -> H^0(r_*omega_Y)=0 -> H^0(omega_X) -> H^0(Q_GR)
  -> H^1(r_*omega_Y)=0 -> H^1(omega_X) -> H^1(Q_GR)=0 -> ...
```

`H^1(Q_GR)=0` because `Q_GR` is zero-dimensional. Hence
`H^0(X,omega_X) ~= H^0(Q_GR)`: **(0.2) CONFIRMED**, together with the
by-product `H^1(omega_X)=0`. Since `omega_X` is invertible,
`length(Q_GR)=length(O_{Z_GR})=length(Z_GR)`, so
`length(Z_GR)=h^0(omega_X)=N_d`: **(3.3) CONFIRMED**.

**(5a) Correction: the pointwise statement is a duality, not an
isomorphism.** I reconstructed it rather than accepting "local duality
identifies this length point by point". Grothendieck duality for `r`, with
`omega_X^.=omega_X[2]` (`X` CM of dimension `2`), `R^{>0}r_*omega_Y=0`, and
`r_*O_Y=O_X`, applied to the triangle
`O_X -> Rr_*O_Y -> (R^1r_*O_Y)[-1] ->`, and using
`Ext^i_X(F,omega_X)=0` for `i!=2` with `Ext^2_X(F,omega_X)=F^D` for `F` of
finite length, yields the canonical exact sequence

```text
0 -> r_*omega_Y -> omega_X -> (R^1 r_*O_Y)^D -> 0,
i.e.  Q_GR ~= (R^1 r_*O_Y)^D   (Matlis dual).                      (R3)
```

So the correct statements are: (i) lengths agree **pointwise**, not merely in
total (`length M^D = length M`), which is *stronger* than the fallback the
prompt allowed; (ii) `Ann(Q_GR)=Ann(R^1r_*O_Y)`, so the two define the *same*
closed subscheme; but (iii) `Q_GR` and `R^1r_*O_Y` are **not** isomorphic
`O_X`-modules in general. Any successor that reads off minimal generators,
socle, or a filtration must fix one side. At `d=3` the distinction is
immaterial: every length-`2` module over an artinian local `C`-algebra is
self-dual. At `d>=4` it is not. **Repair: replace line 207's sentence by
(R3) plus "hence equal lengths and equal annihilators pointwise".**

(R3) also re-derives `length(Z_GR)=sum_p p_g(X,p)=N_d` independently of
(0.2), which is a genuine cross-check: two routes agree.

## 6. Degree three, `omega_X=q^*O(1)` — CONFIRM_WITH_CORRECTIONS

`d=3` in (1.4) gives `omega_X=O_X(B)=q^*O_{P1}(1)` and, by (R1),
`H^0(omega_X)=H^0(P2,O(0)) tensor H^0(P1,O(1))=q^*H^0(P1,O(1))`, dimension
`2`. So the canonical system *is* exactly the pullback of `|O_{P1}(1)|`:
**CONFIRMED**, and via (R1) this is a one-line consequence rather than the
producer's dimension-count-plus-injectivity argument.

**(6a) Missing step — surjectivity of `q` and exclusion of a vertical
component.** The producer asserts "pullback is injective" without proof, and
never rules out a vertical case. Supply: for `t in P1`, `q^{-1}(t)=X cap
(P2 x {t})` is the zero scheme on `P2 x {t} ~= P2` of the restriction of the
defining section of `O_W(d,3)`, i.e. of a section of `O_{P2}(d)`. It is empty
only if that section vanishes identically, i.e. `P2 x {t} subset X`; since `X`
is integral of dimension `2` this forces `X=P2 x {t}`, of class `B`, which
contradicts `[X]=dA+3B` with `d>=3`. Hence **every fibre of `q` is a nonempty
plane curve of degree `d`, `q` is surjective, and no vertical hypersurface
component occurs.** Only then is `q^*: H^0(P1,O(1)) -> H^0(X,q^*O(1))`
injective (`X` integral). Note also that plane curves are connected, so `q`
has connected fibres and `q_*O_X=O_{P1}` (Stein factor is a normal rational
curve dominated by `P1`). This last point is not used by the producer but is
needed by the successor.

**(6b) Minor.** The adjunction isomorphism `omega_X ~= q^*O_{P1}(1)` is
canonical only up to the scalar implicit in the choice of defining equation.
Harmless: only vanishing loci are used.

Composing (0.2) with (6a): `H^0(P1,O(1)) -> H^0(Z_GR,q^*O(1)|_{Z_GR})` is an
isomorphism of `2`-dimensional spaces. **CONFIRMED.**

## 7. The length/image argument — CONFIRMED

Each of the three sub-claims the prompt isolates holds, with the following
literal justifications (the producer states them correctly but compresses).

**(7a) A nonzero `s in H^0(P1,O(1))` vanishing on `T` pulls back to zero on
`Z_GR`.** `Z_GR` is artinian, so `q|_{Z}` is finite and the scheme-theoretic
image is `O_T=O_{P1}/ker(O_{P1} -> (q|_Z)_*O_Z)`. Twisting by `O(1)`, the
evaluation map factors as
`H^0(O(1)) -> H^0(O_T tensor O(1)) -> H^0((q|_Z)_*O_Z tensor O(1))` with the
second arrow injective. So `q^*s|_{Z_GR}=0` **iff** `s|_T=0`. This is an
equivalence, which is more than the producer needs but removes the only place
where a one-directional implication could hide a gap.

**(7b) `length(T)<=length(Z_GR)`.** `O_T` injects into `(q|_Z)_*O_Z`; over
`C` with closed points, length `= dim_C`, so
`dim_C O_T <= dim_C O_Z = 2`. Finiteness of `q|_Z` is what makes this true; it
would fail for a general morphism.

**(7c) `length(T)<=1` is impossible.** `Z_GR != empty` (length `2`), so
`T != empty` and `length(T)=1`, i.e. `T={t}` reduced. Then
`h^0(O(1) tensor I_t)=h^0(O_{P1})=1 != 0`, so a nonzero `s` vanishing on `T`
exists; by (7a) `q^*s` kills `Z_GR`, contradicting injectivity in (0.2).
Hence `length(T)=2=length(Z_GR)`.

**(7d) Equality forces an isomorphism of schemes.** `O_T -> (q|_Z)_*O_Z` is an
injection of `C`-algebras of equal finite dimension `2`, hence bijective. Both
`Z_GR` and `T` are affine, and a morphism of affine schemes inducing an
isomorphism on coordinate rings is an isomorphism. So **`q|_{Z_GR}` is a
closed immersion and `Z_GR ~= T subset P1`: (0.3) CONFIRMED.**

**Scope caveat I add.** Abstractly, *every* length-`2` `C`-scheme embeds in
`P1`, so (0.3) carries no information about the isomorphism class of `Z_GR`.
The entire content is the *immersivity of `q` on `Z_GR`*: the base projection
separates the adjoint defect. The producer's prose ("must move
scheme-theoretically in the coefficient-base direction") states this
correctly, but the theorem should be phrased as "`q|_{Z_GR}` is a closed
immersion" rather than "`Z_GR ~= T`", to prevent a downstream reader from
mistaking (0.3) for a structural statement about `Z_GR`.

## 8. Exhaustiveness of the length-two alternatives — CONFIRMED

An artinian `C`-scheme of length `2` with all residue fields `C` is either two
reduced points or `Spec C[e]/(e^2)` at one point (an artinian local `C`-algebra
of length `2` is `C[e]/(e^2)`). Since `Z_GR=V(J_GR) subset X`, the local ring
is `O_{X,p}/J_{GR,p}`, so the two cases in the producer's list are exhaustive
and mutually exclusive. Under (0.3):

* case (a): two distinct points `p_1 != p_2` of `Sing(X)`, each with local
  `p_g=1` by (R3), and `q(p_1) != q(p_2)`;
* case (b): one point `p` with local `p_g=2`, and the base parameter acts
  nontrivially in the precise sense
  `q^#(m_{q(p)}) not-subset J_{GR,p}`, equivalently
  `O_{P1,q(p)} -> O_{X,p}/J_{GR,p}` is surjective, equivalently `T` is the
  double point of `P1` at `q(p)`.

Both excluded configurations are exactly as the producer states. By (R3) and
self-duality at length `2`, the same dichotomy is visible on `R^1r_*O_Y`;
in particular "the base parameter acts nontrivially" is duality-invariant here
(Matlis duality is an exact contravariant equivalence, so multiplication by
`q^#(t-t_0)` has the same rank on both sides). This is a *coincidence of
length two* and must not be generalized to `d>=4`.

**Typing firewall (I sharpen the producer's own disclaimer).**
`Supp(Z_GR) subset Sing(X)` may be **strict**: Du Val points of `X` carry
`J_GR=O_X` and are invisible to `Z_GR`. So `Z_GR` is not a census of singular
points. Its points are not branches, not places, not sheets, not ramification
primes, not exceptional components, not points of the `pi`-discriminant, and
not normalization points. The partition (2.3) is of local cohomological
lengths only. The producer says this; I confirm it and add that "two length-one
defects" in case (a) could each sit at a singular point with an arbitrarily
complicated resolution graph — length `1` bounds `p_g`, not the graph.

## 9. Negative control `x^3+y^4+z^5=0` — CONFIRM_WITH_CORRECTIONS

**The control's conclusion is CORRECT; its stated criterion is wrong.**

**(9a) The criterion.** The producer writes "the two positive triples *below*
the Newton face" with strict inequalities. The correct Merle--Teissier /
Khovanskii count (Merle--Teissier, *Conditions d'adjonction (d'après Du Val)*,
LNM 777, 1980; Newton-nondegenerate case) is over lattice points of
`Z^3_{>0}` that are **not in the interior** of the Newton polyhedron, i.e.

```text
p_g = # { (i,j,k) in Z^3_{>0} : i/a + j/b + k/c <= 1 }   (weak).
```

The strict rule is **REFUTED** as a general criterion by
`x^3+y^3+z^3`, the cone over a smooth plane cubic: the strict count is `0`,
but `p_g=1` (for the cone over a smooth plane curve of degree `n`,
`p_g = sum_{m=0}^{n-3} binom(m+2,2)`; `n=3` gives `1`, `n=4` gives `4`, and the
weak count reproduces both). Weak-rule controls: `A_1`, `A_{n-1}`, `E_8`
(`x^2+y^3+z^5`) all return `0`, as required.

**(9b) The instance survives verbatim.** For `(a,b,c)=(3,4,5)` the condition
`i/3+j/4+k/5 <= 1` is `20i+15j+12k <= 60`. Solutions with `i,j,k>=1`:
`(1,1,1) -> 47`, `(1,1,2) -> 59`. Everything else exceeds `60`
(`(1,1,3)->71`, `(1,2,1)->62`, `(2,1,1)->67`). And `20i+15j+12k=60` has **no**
solution with `i,j,k>=1`, so no lattice point lies on the boundary and the
strict and weak counts coincide here. Hence `p_g=2`. The producer's two
displayed inequalities are individually true.

**(9c) Independent second computation.** Brieskorn's signature count for
`x^a+y^b+z^c` (Brieskorn, *Invent. Math.* 2 (1966)) with Durfee's
`mu_+ = 2 p_g` (*Math. Ann.* 232 (1978)): with `x=20i+15j+12k`,
`1<=i<=2, 1<=j<=3, 1<=k<=4` (so `mu=24=(3-1)(4-1)(5-1)`), the `24` values are
`47,59,71,83,62,74,86,98,77,89,101,113,67,79,91,103,82,94,106,118,97,109,121,133`.
Those with `x/60 mod 2 in (0,1)` are `47,59` (in `(0,60)`) and `121,133` (in
`(120,180)`), so `mu_+=4` and `p_g=2`. Two independent methods agree.

**(9d) Rational tree.** `gcd(3,4)=gcd(4,5)=gcd(3,5)=1`, so the link is the
Brieskorn integral homology sphere `Sigma(3,4,5)`, Seifert-fibred over the base
orbifold `S^2(3,4,5)`. By Orlik--Wagreich / Pinkham the good resolution of a
weighted-homogeneous normal surface singularity is star-shaped with central
curve of genus equal to the base genus (`=0` here) and three arms that are
chains of rational curves from continued fractions. Hence the good-resolution
dual graph **is a tree of rational curves**. `E_8` (`x^2+y^3+z^5`,
`Sigma(2,3,5)`) is the same shape with `p_g=0`, confirming that graph shape
alone does not decide `p_g`.

**Verdict:** the control is valid and does exactly what the producer claims —
it falsifies "reduced rational-forest topology `=>` rational singularity", and
therefore correctly blocks appending "therefore the rational forest is
impossible" to the theorem. **Repair: change `<` to `<=` and "below the Newton
face" to "not interior to the Newton polyhedron", and add the parenthetical
that for `(3,4,5)` no boundary lattice point exists so the count is
unchanged.** Do not delete the control.

## 10. Section 5 smooth special case — CONFIRMED

If `X` is smooth then `Y=X`, `R^1r_*O_Y=0`, and (0.1) reads `0=N_d>=2`:
impossible. So no *smooth* normal class-`(d,3)` hypersurface with `d>=3`
receives a dominant rational map from `A2`. This is consistent with, and
independent of, the charged rational-forest §3 and the charged
one-attachment review's scope line, neither of which is imported.

## 11. Two free corroborations (my inference, not the producer's)

**(11a) The factor of two, geometrically.** By §6a the general `q`-fibre is a
plane curve of degree `d`, of arithmetic genus `(d-1)(d-2)/2 = N_d/2`. So
`h^2(O_X) = 2 * (genus of the general q-fibre)`. This is an independent
corroboration of the factor of two demanded by item 1, and it also shows the
`3` in `dA+3B` enters twice in different ways: as `e-1=2` in the Kunneth term
and as `deg(pi)=3` on the plane side. For general `dA+eB` the two readings
diverge (`N_{d,e}=(e-1)(d-1)(d-2)/2`), so the coincidence is specific to
`e=3`.

**(11b) A numerical constraint the producer misses.** Since `Delta=K_Y-r^*K_X`
is `r`-exceptional, `Delta . r^*D = 0` for every `D`, hence
`K_Y . r^*K_X = K_X^2` and `Delta^2 = K_Y^2 - K_X^2`. On `X`,
`K_X^2 = ((d-3)A+B)^2 . (dA+3B) = (d-3)(5d-9)`, which is `0` at `d=3`.
`Delta != 0` because `Z_GR != empty`, and the exceptional intersection form is
negative definite (Mumford, *Publ. IHES* 9 (1961)), so `Delta^2 < 0`. With
`K_Y^2 = 10 - rho(Y)` for a rational `Y`:

```text
d=3:  rho(Y) = 10 - Delta^2 >= 11.
```

Moreover, by §6a and adjunction on `Y`, the strict transform of a general
`q`-fibre has self-intersection `0` and `K_Y`-degree `0`, so **`Y` carries a
genus-one fibration over `P1` with connected fibres**: `Y` is a blown-up
rational elliptic surface with `rho>=11`. The successor should use this; it is
a much sharper handle than "`Y` is rational".

## 12. Successor `D3-ADJOINT-HORIZONTALITY` — ACCEPTED_WITH_FIREWALLS

The proposed successor is well-typed and desk-scale. Four firewalls.

1. Step 1 computes the base-parameter action on `omega_X/r_*omega_Y`, which by
   (R3) is the correct (non-dual) side. Do not transport it to `R^1r_*O_Y`
   without dualizing; the accidental self-duality at length `2` does not
   extend to `d>=4`.
2. Step 3's "finite-flat cubic different/discriminant" lives on
   `pi:X->P2` (generically finite of degree `3`, `R_pi ~ dA+B`, hence `3A+B`
   at `d=3`; the charged quadratic value `2A+B` is the `d=2` instance of the
   same formula and must be recomputed, not imported). (0.3) is a statement
   about `q:X->P1`. Conflating the two projections is the principal typing
   hazard in this successor.
3. Step 4's phrase "prove that every licensed defect is vertical" is
   underspecified. To contradict (0.3) one must refute **both** branches:
   (a) `#q(Supp Z_GR) >= 2` in the two-point case, and
   (b) `q^#(m_{q(p)}) not-subset J_{GR,p}` in the one-point case. Refuting only
   one branch closes nothing.
4. `pi` need not be finite (`X` may contain fibres `{x} x P1`); `q` is
   surjective with connected fibres (§6a) and that is the only projection
   property proved here.

## 13. Maximum safe theorem

> Let `W=P2 x P1`, `A=pr_1^*O(1)`, `B=pr_2^*O(1)`, and let `X subset W` be an
> integral normal hypersurface with `[X]=dA+3B`, `d>=3`, over `C`, admitting a
> dominant rational map from `A2`. Let `r:Y->X` be any resolution with `Y`
> smooth projective, `q:X->P1` the second projection, `N_d=(d-1)(d-2)`.
>
> 1. `X` is Cohen--Macaulay and Gorenstein, `omega_X=O_X((d-3)A+B)`,
>    `H^1(O_X)=0`, `h^2(O_X)=h^0(omega_X)=N_d`, and
>    `H^0(omega_X)=H^0(P2,O(d-3)) tensor H^0(P1,O(1))`.
> 2. `q(Y)=p_g(Y)=0`, hence `H^1(O_Y)=H^2(O_Y)=0`. (`Y` is in fact rational,
>    by Castelnuovo; that stronger fact is not used.)
> 3. `sum_{p in Sing X} p_g(X,p) = N_d >= 2`, canonically and independently of
>    `r`. In particular `X` is singular and at least one singularity is not
>    Du Val.
> 4. `J_GR := r_*O_Y(K_Y-r^*K_X) subset O_X` is an `r`-independent ideal of
>    finite colength with `r_*omega_Y=J_GR tensor omega_X`,
>    `Z_GR:=V(J_GR) subset Sing(X)`,
>    `Q_GR := omega_X/r_*omega_Y ~= O_{Z_GR} tensor omega_X ~= (R^1r_*O_Y)^D`,
>    `length(Z_GR)=N_d`, and
>    `H^0(X,omega_X) -> H^0(Z_GR,omega_X|_{Z_GR})` is an isomorphism; i.e.
>    `Z_GR` is an exact interpolation scheme for the complete system
>    `|(d-3)A+B|`.
> 5. `q` is surjective with connected fibres, the general fibre being a plane
>    curve of degree `d` and genus `N_d/2`.
> 6. If `d=3`: `omega_X=q^*O_{P1}(1)`, `h^0=2`, and `q|_{Z_GR}` is a **closed
>    immersion** onto a length-two subscheme `T subset P1`. Consequently
>    exactly one of: (a) two singular points with local `p_g=1` in distinct
>    `q`-fibres; (b) one singular point `p` with local `p_g=2` and
>    `q^#(m_{q(p)}) not-subset J_{GR,p}`. Also `rho(Y)>=11` and `Y` carries a
>    genus-one fibration over `P1`.

**Exact dependencies.** Kunneth + Serre duality on `P2 x P1`; adjunction for a
Cartier divisor in a smooth variety; Zariski's main theorem; Grauert--
Riemenschneider (Satz 2.3); Grothendieck/local duality on a `2`-dimensional CM
scheme; injectivity of pullback of `1`-forms and pluricanonical forms under a
generically finite dominant map in characteristic zero; Hodge symmetry on a
smooth projective surface; Hironaka. Castelnuovo is cited but not load-bearing
after the §2b repair. Artin's Gorenstein-rational `=` Du Val is used only for
the remark in §3c.

**Firewalls / what this does not supply.** No block, no finite presentation, no
basis invariance, no occurrence or effectivity certificate, no polynomial map,
no counterexample, no JC2 statement, and **no exclusion at `d=3`**: (0.3) is a
discriminator, not a contradiction. No `d=2` conclusion (smooth conic bundle,
Du Val, crepancy, `D9(-1)`, `R_pi=2A+B`, `rho=11` at `d=2`) is used or valid
here; `N_d>0` makes the Du Val and crepancy statements *false* for `d>=3`.
Nonnormal, nonreduced, reducible, projective-basepoint, fibre-degree-drop and
vertical-component strata are untouched. `Supp(Z_GR)` may be a proper subset of
`Sing(X)`. The `x^3+y^4+z^5` control is topological only and is not asserted to
occur on any class-`(3,3)` incidence surface. The rational-forest gate and this
gate are independent: neither implies the other, and §9 shows the forest gate
cannot see `Z_GR`.

**Required edits before promotion.** (i) §9 strict `->` weak Newton
inequality; (ii) §4/§6 insert the surjectivity-of-`q` argument of §6a;
(iii) §3 line 207 replace by (R3); (iv) §2 delete the `-> 0` from the
five-term sequence; (v) §2 replace the Castelnuovo route by the forms
argument and add "projective" to the resolution; (vi) §4 restate (0.3) as
"`q|_{Z_GR}` is a closed immersion". With these six edits I would return
CONFIRMED.

Receipt status `ABSENT`, as expected: this review makes no exit-price
assertion, so no charge-basis declaration line is emitted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `28949`.
- Body SHA-256:
  `5e1173c7aab69668bc9b320467753fee0642d353766b78e3a750f3afb9b0ae21`.
- Frozen basis: `f02aba6913ec6f9ecd1f3ae103475cde05f3ee29`.
