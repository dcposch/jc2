# Hostile review: QCS `A^2`-filling comparison + degree-six labelled PALF obstruction

**Reviewer:** Opus 5, independent hostile mathematical review
**Date:** 2026-08-29
**Repository basis (resolved):** `0375694aa21fd8db3b465ef2098ca539106a1582`
**Lifecycle:** hostile review only. No promotion of QCS, of any map, or of JC2.

## 0. Custody

All six pins in the review request were recomputed byte-exactly and match.

```text
report 1  xmodel/qcs-a2-filling-comparison-sol56-20260829.md
  full 888028226fa340990893909e34865c8d84f65d46d4377b87968fe0c95a3a6b67   MATCH
  body 9012 bytes  9c41323249ac54ddf0f13bd34631ce52225ce16adf1119333f0d0d50a322ec60  MATCH
report 2  xmodel/qcs-degree6-labelled-palf-obstruction-sol56-20260829.md
  full 56c1d9e45e01a32e748136d8a7084a3c8cf868dc70b120cf16efa6716a283ff3   MATCH
  body 9434 bytes  181e5bdd06b053d790f7d8e08391927aec363d986f8a5ef04809ad2468ff1b9f  MATCH
identity  xmodel/pcb-generic-collision-surplus-coordinator-integration-sol56-20260829.md
  full cee4e1f8079b5a20ee6fca3c7fa58dda1d8c90aeb235cd411d5fc485b9eb7936   MATCH
  body 7094 bytes  85c279638f2d13203f5a6e22af23785c4981c4d5f286c81127bfd91c66e37b56  MATCH
```

Both reviewed reports declare frozen basis `31777ce90994a106aade85064c0d868e32863f94`.
That commit is the immediate parent of the resolved basis (drift = 1 commit,
`0375694a` "Promote valuation four and retype generic PCB"). Basis drift is
benign for this lane: no promoted QCS identity changed between the two commits.

Producer of record, consulted as source for the control (unpinned by report 1,
pinned by the coordinator): `xmodel/pcb-generic-collision-surplus-sol56-20260829.md`,
full `412091929a68e8539148d00c24ee71e1d0c45185571b48be55be19d3efe0813f`.

`jc2-lean` was not entered, listed, searched, stat'ed, built, or inspected. No
Singular and no heavy work was run. Everything below is desk-scale exact
topology/algebra plus finite permutation arithmetic reproduced independently.

## 1. What I recomputed independently

Rather than voting, I rebuilt every load-bearing object from the promoted
identity package and from first principles:

* the one-variable ramification identity and the auxiliary Milnor space;
* the Riemann--Hurwitz balance for `g` restricted to a fibre, from which I
  re-derived the promoted `d - chi_gen = sum_i d_i b_i` and the promoted margin
  `Xi = d - s - sum_i b_i` **independently** (this is a real cross-check: the
  promoted margin is exactly RH for the fibre-restricted `g`-cover);
* the degree-six passport permutations (product, cycle types, group order,
  transitivity, coalescence) by explicit computation;
* the `A_4` germ: Milnor number, branch count, compact Milnor-fibre genus,
  moving divisor points, the relative exact sequence, and the affine jump;
* the five-stabilization PALF page and its unimodular handle matrix;
* the embedding obstruction, by intersection-form rank rather than by genus
  monotonicity;
* a **new closed-form genus budget** for the promoted zero-excess germ family,
  and two explicit **repaired controls** that defeat report 2's obstruction at
  the same total degree.

## 2. Verdict table

| # | Claim (source) | Verdict |
|---|---|---|
| C1 | `K = sum_i b_i(deg P_i - 1) = dim V_aux`, exact auxiliary count (R1 §1) | **CONFIRMED** |
| C2 | `mu_fin(P_i) = d_i - 1 = sum_a (d_i - q_i(a))` (R1 §1) | **CONFIRMED** |
| C3 | After morsification `K` is a weighted positive half-twist length (R1 §1) | **CONFIRMED WITH RIDER** (needs `b_i in Z_{>0}`; true here) |
| C4 | `K` carries **no** automatic page-`H_1` / vanishing-one-cycle reading (R1 §1) | **CONFIRMED** (and independently forced by C13) |
| C5 | Surjective `∂_P`, `Ψ` of the stated types ⟹ `K >= delta + s - 1` (R1 §2) | **CONFIRMED** (pure rank-nullity, conditional on connected `F`) |
| C6 | `delta = 1 - chi_gen = b_1(F)` (R1 §2) | **CONFIRMED** for connected `F`; **GAP** in the stated `c>1` remark |
| C7 | "First surjectivity says the graph is connected" (R1 §2) | **CONFIRMED** only if `∂_P` *is* a simplicial edge boundary; **not needed** for C5 |
| C8 | Neither map is constructed in current sources (R1 §2) | **CONFIRMED AT SPOT-CHECK SCOPE**; **GAP** as a repository-wide non-existence claim (unpinned citations) |
| C9 | Collision endpoints are "two endpoints among actual pole places" (R1 §2) | **REFUTED** — in the promoted germ family they are *finite-value* ends |
| C10 | Five positive stabilizations give a `D^4` PALF with page `Sigma_{1,4}` (R1 §3) | **CONFIRMED** |
| C11 | Five stabilization cycles are a `Z`-basis of `H_1(Sigma_{1,4})` (R1 §3) | **CONFIRMED** (lower-triangular, unit diagonal) |
| C12 | Therefore filling + positivity + counts cannot force the extra `s-1` (R1 §3) | **CONFIRMED BUT NARROW** — kills a hypothesis nobody can have (see C13) |
| C13 | `D^4 ≅ A^2`-type filling framing (R1 §3, §4) | **REFUTED AS A CATEGORY** — for a Keller pair `f` is a submersion, so the interior-Lefschetz category is empty |
| C14 | `A_4`, `mu=4`, one branch, `g(M_a)=2`, two moving divisor points (R2 §2) | **CONFIRMED** |
| C15 | Affine local jump `5 = 4 + 1` (interior + end merger) (R2 §2, (2.1)) | **CONFIRMED**, and generalizes to `jump = mu + q_gen - 1` |
| C16 | The five units are `H_1(M_a, M_a ∩ D)`, not five interior PL cycles (R2 §2) | **CONFIRMED** (dim `= 4 + 1 = 5`) |
| C17 | Passport: `G=1`, four ends, `b_1(F_Hur)=5`, special `G_m ⊔ A^1` (R2 §1) | **CONFIRMED** (group is `A_6`, order 360, transitive; product `=1` right-to-left) |
| C18 | `Sigma_{2,1}` cannot embed in the genus-1 fibre / in `Sigma_{1,4}` (R2 §3) | **CONFIRMED** (cleanest proof: symplectic rank 4 > 2) |
| C19 | `(2.1)` and `(3.1)` are the same Euler value with different homological degree (R2 §3) | **CONFIRMED** |
| C20 | A `D^4` PALF handle matrix must be unimodular (R2 §3) | **CONFIRMED** as a necessary condition |
| C21 | An unlabelled five-tuple search is a guaranteed false positive (R2 §4) | **CONFIRMED** (already anticipated by R1 §4's last paragraph) |
| C22 | R2 supersedes R1 §4's proposed labelled search | **CONFIRMED**, under a hypothesis R2 adds and flags |
| C23 | "The obstruction is a mismatch between *this* germ and *this* passport" (R2 verdict, §5) | **UNDERCLAIM / GAP** — the passport genus is *forced*; the obstruction is germ-intrinsic |
| C24 | "This result invalidates neither QCS nor the degree-six dependency control" (R2 consequence) | **REFUTED for the second clause** — the control is invalidated *as a joint witness* |
| C25 | "For the exact equality germ no successor packet is needed; genus `2>1` returns NO" (R2 §5) | **CONFIRMED for that germ**; **REFUTED as a lane closure** — repaired controls exist at the same `d` |

## 3. Item 1 — what `K` exactly is

`K` is exactly what report 1 says, and I reproduce the derivation.

For `P` of degree `d` over `C`, `deg P' = d-1`, so
`mu_fin(P) = sum_{z in A^1} ord_z(P') = d-1`. At a point `z` of multiplicity
`m_z` in its own fibre, `ord_z(P - P(z)) = m_z` and `ord_z(P') = m_z - 1`, so
grouping by value gives `sum_a (d - q(a)) = sum_z (m_z - 1) = d-1`. Both
displayed forms in R1 §1 are therefore exact identities, not estimates. C2 CONFIRMED.

The local Milnor fibre of a one-variable `P` at a critical point `z` is `m_z`
points; its reduced homology is `H~_0` of dimension `m_z - 1 = ord_z(P')`.
Hence `dim V_aux = sum_i b_i (d_i - 1) = K`. C1 CONFIRMED, **as a
vanishing-zero-cycle dimension**, exactly as typed.

For the braid statement: a morsified degree-`d` polynomial has `d-1` simple
branch points and a positive factorization of length `d-1` in `B_d` (product =
the degree-`d` monodromy at infinity, which has `sigma`-length `d-1`). Taking
`b_i` **independently perturbed disjoint copies** of `P_i` makes the weighted
count an actual positive factorization of length `b_i(d_i-1)` for a
disconnected cover of `A^1_a` of degree `b_i d_i`. So C3 is CONFIRMED, with the
rider that this reading needs `b_i` to be a positive **integer**. It is:
the producer defines `b_i = kappa_i^+(u_i - 1)` (producer line 18, "the generic
high baseline", line 121) with `kappa` a multiplicity and `u_i >= 2`. If a
future package ever admits rational `b_i`, C1 survives as a dimension count but
C3 dies. Record the rider; do not carry the braid reading without it.

C4 CONFIRMED. The `P_i` live on quotient lines `U_i ≅ A^1_z`, not on `F`, and
the `B_i` are coefficient multiplicities. Nothing in the package produces a map
from `V_aux` to `H_1(F)`. This is reinforced from an unexpected direction in
§5 below: for an actual Keller pair `f` is a **submersion**, so `f` has no
interior critical points at all and there are no page vanishing one-cycles for
`K` to be. The absence of a page interpretation is not a gap in the sources;
it is structural.

## 4. Item 2 — the boundary complex `(2.1)`

**The implication is valid.** `H~_0(P;Q)` for `s` discrete pole places has
dimension `s-1`; surjectivity of `∂_P` gives `rank = s-1`; rank-nullity gives
`dim ker = K - (s-1)`; surjectivity of `Ψ` gives `dim ker >= b_1(F;Q)`. With
`F` connected, Suzuki's `delta = 1 - chi_gen` equals `b_1(F)`, so
`K >= delta + s - 1`. C5 CONFIRMED.

I checked that this target is *exactly* generic PCB and not a lookalike.
Using the promoted package, `chi_gen = 2-2G-s-n` and `delta = 2G+s+n-1`, so
`delta + s - 1 = 2G+2s+n-2` and

```text
Xi = K - (delta + s - 1) = d - s - sum_i b_i,
```

which is the promoted margin verbatim (integration lines 102--111; producer
(QCS'), line 44). So `(2.1)` would prove precisely `Xi >= 0`. Good typing.

**Independent cross-check of the promoted identity.** For a Keller pair,
`Jac(f,g)=1` forces `df` and `dg` independent everywhere, hence `g|_{F_a}` is
étale on the affine fibre. Riemann--Hurwitz for `g: F̄_a -> P^1` of degree `d`
then reads `2G-2 = -2d + (d-s) + (W-n)` where `W` is the sum of local
`g`-degrees at the `n` finite-value ends. Eliminating `G` gives
`chi_gen = d - W`, i.e. exactly the producer's `(2.2)` `d - chi_gen = sum_i d_i b_i`
with `W = sum_i d_i b_i`. The promoted collision package is therefore RH for
the fibre-restricted `g`-cover. This is a genuinely independent confirmation of
the identity tier and it is what makes the sharpenings in §6 possible.

**Conventions.** `H~_0` reduced, `H_1` absolute, coefficients `Q`: all stated,
all consistent, dimensions add correctly. C6 CONFIRMED for connected `F`.

**GAP (C6, disconnected remark).** R1 §2's `c`-component paragraph is
incomplete. If `F` has `c` components, `b_1(F) = c - chi_gen = delta + c - 1`,
so the rank-nullity conclusion becomes `K >= (s-1) + delta + (c-1)`, which is
*stronger*, not a repair. The report's `(s-c) + (c-1) = s-1` decomposition of
the vertex part is correct but decorative; it does not carry the target. Repair:
delete the paragraph or state the `b_1 = delta + c - 1` correction, and cite the
integration's primitivity rider for the actual-pair case.

**C7.** Surjectivity onto `H~_0` of the vertex set is equivalent to
connectedness *only when* `∂_P` is the simplicial boundary of a graph with
edge space `V_aux`. R1 posits that structure without building it. The rank-nullity
argument does not need it, so this is a presentational hazard, not a hole.
Repair: state `(2.1)` purely as two linear surjections; drop "connected".

**C9 — a live REFUTATION, not a gap.** R1 §2 says "every weighted quotient
critical event needs two endpoints among actual pole places." The one worked
member of the promoted zero-excess family says otherwise. In
`f = t^2 + s^5/5, g = t` on `D = {s=0}`, the two moving points `t = ±sqrt(a)`
that collide are points where `g` is **finite**; they are finite-value end
places, not poles. Report 2 §1 states this correctly for its own purposes but
does not carry it back as a refutation of R1 §2's vertex type. So the
boundary-tree route as literally written has the wrong vertex set: the natural
candidate for `∂_P` is *zero* on the only collision event the campaign has
computed. Repair: re-type the vertex set as the `s+n` places at infinity, or as
`M_a ∩ D` (the relative pair that report 2 §2 correctly identifies), and then
re-derive; note that with vertices `= s+n` places the rank-nullity target
becomes `K >= (s+n-1) + b_1(F)`, which the degree-six control violates even
harder (`5 >= 3+5` false), and which my repaired control in §7 also violates
(`10 >= 4+10` false). Either vertex choice therefore remains unconstructible by
counting alone; the route is untyped, exactly as R1 concludes, but for a
*different and stronger* reason than R1 gives.

**C8.** I spot-checked the corpus for any existing construction of a
pole-incidence boundary or a suspension: the only `xmodel` files matching
`pole.incidence|incidence (graph|boundary)|suspension` are one ideation file,
this review's own prompt, report 1 itself, and an unrelated `td6` review; all
`boundary (tree|graph)` hits are ideation files, i.e. unpromoted brainstorm.
So the negative claim is supported at spot-check scope. **GAP:** R1 §2 makes a
repository-wide non-existence claim on *unpinned prose citations*
("the Section 7 collision formula", "the resolution-free repair", "the monodromy
reports", "the Hamiltonian--Kummer audit", "Earlier common-resolution direction
claims"). The producer pins the resolution-free construction (`aec8bd7e...`,
producer line 124); report 1 pins nothing. Repair: enumerate the searched
artifact set with SHA-256 pins, or retype the sentence as
"no construction was found in the searched set", which is all that is licensed.

## 5. Item 3 — the five-stabilization control

**C10 CONFIRMED.** Start from the trivial PALF on `D^4` with page `D^2`. A
positive stabilization attaches a page 1-handle plus a Lefschetz 2-handle along
a curve crossing that 1-handle geometrically once; the pair cancels, so the
total space stays `D^4`. On pages: a 1-handle with both feet on one boundary
component gives `Sigma_{g,b} -> Sigma_{g,b+1}`; with feet on two different
boundary components it gives `Sigma_{g,b} -> Sigma_{g+1,b-1}` (both drop `chi`
by 1). Four of the first kind then one of the second gives
`Sigma_{0,1} -> Sigma_{0,5} -> Sigma_{1,4}`; `chi = 1-5 = -4 = 2-2-4`;
`b_1 = 2(1)+4-1 = 5`. The genus-increasing move is available because
`Sigma_{0,5}` has five boundary components. All arithmetic in R1 §3 is exact.

**C11 CONFIRMED.** In the handle basis `h_1..h_5`, the `k`-th stabilization
curve has coefficient `±1` on `h_k` (it crosses the new handle once), arbitrary
integers on `h_1..h_{k-1}`, and `0` on later handles. The matrix is
lower-triangular with unit diagonal, hence unimodular over `Z`; the five classes
are a `Z`-basis and the thimble-to-page map is injective.

**C12 CONFIRMED, with a sharp scope statement.** What the control proves,
exactly and only, is: *there is no theorem of the form* "[positive Lefschetz
filling with total space `D^4`] + [page with `b_1 = delta`] + [`s` boundary
components marked] `⟹` #cycles `>= delta + s - 1`", because `(5,5,2)` is a
witness against it (`5 >= 5+1` is false). What it does **not** prove: nothing
about polynomials, nothing about `f` or `g`, nothing about the Jacobian, and
nothing about whether `∂_P` or `Ψ` can be constructed from *algebraic* input.
Its `s = 2` is a bare label with no structure attached.

**C13 — the load-bearing hazard R1 misses.** For a Keller pair, `Jac(f,g) = 1`
forces `df != 0` everywhere, so `f: A^2 -> A^1` is a **submersion**: it has no
critical points, all fibres are smooth, and there are **no interior Lefschetz
vanishing cycles at all**. Every unit of `delta` lives at infinity. So the PALF
category — whose entire content is interior Lefschetz singularities — has empty
interior content for the actual object. Two consequences:

1. R1 §3's control refutes a hypothesis that no correct proof could have used,
   because the hypothesis silently identifies `K` with a count of page vanishing
   cycles, which R1 §1 itself declares untyped. The no-go is internally valid but
   evidentially thin; its function is to foreclose a tempting slogan, not to
   constrain any live route.
2. "`D^4 ≅ A^2`-type filling" is a double abuse: `D^4` is compact with boundary
   `S^3` and `A^2 = C^2` is open, *and* the filling category is the wrong one.
   Report 2 §3's last paragraph gets this half-right ("A boundary degeneration or
   relative handle is required, and ordinary PALF data do not specify it"); R1
   never says it. Repair: replace "`A^2`-filling" everywhere by "positive
   Lefschetz filling", and add the submersion remark, which is one line and kills
   the whole PALF lane cleanly rather than by control.

## 6. Items 4 and 5 — the local germ and the passport

### 6.1 Local germ: every number CONFIRMED

`f = t^2 + s^5/5`, `g = t`, `D = {s=0}`, `df ∧ dg = s^4 ds ∧ dt`.

* Jacobian ideal `(2t, s^4)`, `mu = dim C{s,t}/(t,s^4) = 4`. Type `A_4`
  (`A_k = x^2 + y^{k+1}`, `k=4`). ✔
* `gcd(2,5) = 1`, so one branch, `r = 1`. ✔
* `chi(M_a) = 1 - mu = -3`; `r = 1` boundary circle; `-3 = 2-2g-1` gives
  `g(M_a) = 2`, equivalently `mu = 2g + r - 1`. ✔
* Independent check without Milnor theory: `M_a` is the double cover of the
  `s`-disk branched at the five roots of `a - s^5/5`, so `chi = 2 - 5 = -3` and,
  since 5 is odd, the boundary is connected: `Sigma_{2,1}`. ✔
* `M_a ∩ D = {(0, ±sqrt a)}`, two points, inside the Milnor ball for `|a| << eps`. ✔
* `chi(M_a \ D) = -5`, `b_1 = 6` (`= 2g + #ends - 1 = 4+3-1`). ✔
* Central fibre `t^2 = -s^5/5` is unibranch; normalization is a disk; minus its
  one point over `D` it is a punctured disk, `chi = 0`, `b_1 = 1`. ✔
* Jump `0 - (-5) = 5`. ✔

C14, C15 CONFIRMED. **Generalization I verified and recommend recording:** the
split is not "mu + (2-1)" by accident. In general, for a boundary germ whose
extended generic fibre meets `D` in `q_gen` points near the collision and whose
special fibre has Milnor number `mu` and `r` branches,

```text
local affine jump = [chi(normalized special) - chi(M_a)] + [q_gen - r]
                  = (mu + r - 1) + (q_gen - r)
                  = mu + q_gen - 1.
```

For the germ family `f = s^b/b + phi(t)` at a critical point of multiplicity `m`
this equals `(b-1)(m-1) + m - 1 = b(m-1)`, which is exactly the collision
capacity `b(d_1 - q(a))` contribution. Report 2's `(2.1)` is the `r=1, q_gen=2`
case. **Narrowing:** report 2's phrasing "`mu` interior + one end merger"
matches the `r = 1` case only; for `r > 1` the interior term is `mu + r - 1` and
the end term is `q_gen - r`. No error in report 2 (it only treats `r=1`), but the
sentence must not be transported.

C16 CONFIRMED: `H_1(M_a) -> H_1(M_a,{p_±}) -> H~_0({p_±}) -> H~_0(M_a) = 0`
gives `dim H_1(M_a, M_a ∩ D) = 4 + 1 = 5`. This is the correct home of the five
units and it is a **relative** group. Note this is the same relative pair that
§4/C9 says the boundary complex should have used.

### 6.2 Passport: every number CONFIRMED, by explicit computation

With `sigma_+ = (1 2 3 4 5)`, `sigma_- = (0 1 2 4 3)`, `sigma_inf = (0 3 1 5 2)`
on `{0..5}`:

```text
cycle types (5,1),(5,1),(5,1)
sigma_+ sigma_- sigma_inf = id     under right-to-left composition (TRUE)
                                   under left-to-right composition (FALSE)
sigma_+ sigma_- = sigma_inf^{-1},  type (5,1)
|<sigma_+, sigma_-, sigma_inf>| = 360, transitive  =>  the group IS A_6
R = 4+4+4 = 12,  2G-2 = -12+12 = 0,  G = 1
```

R1 §4's "transitive `A_6` action" is therefore correct (I checked the order, not
just evenness; a transitive degree-6 subgroup of `A_6` containing a 5-cycle could
have been `A_5`, and is not). **Minor hazard:** the composition-order convention
is load-bearing and unstated in both reports; only right-to-left works.

Ends: `sigma_inf` has 2 cycles ⟹ `s = 2` poles of `g`-order 5 and 1; each finite
branch value has one ramified (5-cycle) point removed ⟹ `n = 2`. So
`F_Hur = Sigma_{1,4}`, `b_1 = 2+4-1 = 5`, `chi_gen = -4`, `delta = 5`. Coalescing
the two finite branch values gives limit monodromy `sigma_+sigma_- = sigma_inf^{-1}`,
components = orbits of `<sigma_inf>` of sizes 5 and 1, both rational; removing
the finite 5-cycle point and the poles gives `G_m ⊔ A^1`, `chi = 1`, jump `5`. ✔
`(b_0,b_1): (1,5) -> (2,1)`, `Δb_0 - Δb_1 = 1-(-4) = 5`. ✔ C17, C19 CONFIRMED.

The matching is tighter than the producer claims: the germ gives local
`g`-degree 5 at each of the two moving points (`t - t_0 ~ c s^5`), which is
exactly the ramification index of the passport's 5-cycles, and the two moving
points' `g`-values `±sqrt a` are exactly the two finite branch values that
coalesce. The control is genuinely matched — which is what makes its
inconsistency interesting.

### 6.3 The embedding obstruction: CONFIRMED, with a cleaner proof

Report 2 argues by genus monotonicity. That works (the boundary circle of an
embedded `Sigma_{2,1}` separates, so `genus(X) = 2 + genus(complement) >= 2`),
but the robust proof is by intersection form. `H_1(Sigma_{2,1};Z) = Z^4` carries
the standard symplectic form, `det = 1`, nondegenerate; equivalently the `A_4`
vanishing chain has intersection matrix `tridiag(0;±1)` with `det = 1`. Algebraic
intersection numbers of closed loops are preserved by any embedding of surfaces.
For `Sigma_{1,4}` the pairing on `H_1` has radical of dimension `b-1 = 3` and
nondegenerate rank `2g = 2`. A rank-4 nondegenerate subspace cannot map into a
form of rank 2. Hence `Sigma_{2,1}` embeds in neither `Sigma_{1,4}` nor a closed
genus-1 surface, and the argument survives puncturing `M_a` at its two divisor
points. C18 CONFIRMED. C20 CONFIRMED: total space a homology ball forces the
`5x5` thimble-to-handle matrix to be injective and surjective over `Z`.

### 6.4 C23 — report 2 UNDERCLAIMS its own obstruction

Report 2 presents the contradiction as a clash between *this germ* and *this
passport*, and §5 offers "try an alternative germ". That framing is wrong in a
way that matters: **the passport genus is not a free choice.** From the RH
balance of §4 applied to the control's own data (`d = 1 + I_1 = 6`, `n = d_1 = 2`,
`W = d_1 b = 10`, `g` étale on the affine part):

```text
2G = 2 - chi_gen - s - n = (d_1 - 1)(b - 1) - s = (2-1)(5-1) - s = 4 - s.
```

With `s >= 1` (a nonconstant `g` on a compact fibre must have a pole), `G <= 1`,
and integrality forces `s in {2,4}`, `G in {1,0}`. So `G = 1` at `s = 2` is the
*unique* consistent passport genus for this germ, and **no** alternative
passport can rescue it. A second, purely surface-theoretic derivation of the same
equation: `F_gen ⊃ M_a \ D = Sigma_{2,3}` with `chi = -5`, the complement is
`Sigma_{G-2,1}` minus `s` points with `chi = 5-2G-s`, and
`chi_gen = -4` forces `2G + s = 4` again.

Conclusion: the incompatibility is **germ-intrinsic and passport-independent**.
The germ `f = t^2 + s^5/5, g = t` admits no single-quotient-line global model
with connected generic fibre at all. Report 2's obstruction is stronger than
report 2 says; the "alternative germ" advice in §5 is aimed at the wrong knob.

### 6.5 C24 — report 2 also OVERCLAIMS, in its nonclaims

Report 2's closing line, "This result invalidates neither QCS nor the degree-six
dependency control," is not consistent with its own §3. The control's *purpose*
(producer §4.2, §5) was to show that curve topology, transitive monodromy,
Suzuki defect, and exact local Jacobian-one equality **jointly** fail to force
strictness. If the germ and the passport cannot coexist, there is no single
object satisfying the constraints jointly, so the joint claim loses its witness.
The control survives only as two separate one-constraint-at-a-time controls:
(a) an exact zero-excess Jacobian-one germ, which kills pointwise local
strictness; (b) an abstract Hurwitz cover with `Xi = -1`, which kills pure
numerical forcing. The coordinator integration had already narrowed the language
("the two objects are not glued... they prove only that strictness is absent from
the recorded numerical/topological content"), and that narrowing is the correct
one; report 2 upgrades "not glued" to "cannot be glued" and should say so in its
consequence section. Repair: replace the sentence with "this invalidates the
control as a **joint** witness while leaving each single-constraint control
intact."

## 7. Item 6 — supersession, and what weaker realization survives

**C22 CONFIRMED, conditionally.** R1 §4's item 2 says "the quotient braid
`P = z^2` with coefficient rank five", which under R1 §1's own typing is a
*formal* datum (five coefficient copies of one half-twist), not the germ.
Report 2 correctly flags that it is adding the stronger reading ("if the label
`P=z^2, b=w=5` means the exact zero-excess boundary collision"). Under the strong
reading the test is obstructed (§6.3--6.4). Under the weak reading the test is
not obstructed but is **vacuous**, by R2 §4 — and R1 §4 had already said so
itself ("The unlabelled stabilization construction in Section 3 already realizes
the counts with determinant one"). So the proposed test is dead under both
readings, and report 2 covers both. Minor fairness point: R1 never called §3 a
labelled realization; R2's corrective sentence is aimed at a claim R1 did not make.

**C25 REFUTED as a lane closure — this is the main hostile finding.**
Report 2 §5 says "For the exact equality germ no such packet is needed: the genus
`2>1` obstruction already returns NO." True for that germ. But the campaign must
not read this as closing the dependency-barrier lane, because a genus-consistent
replacement exists **at the same total degree, the same baseline, the same pole
count, and the same margin**.

**GENUS-BUDGET (new, exact).** For the promoted zero-excess family
`f = s^b/b + phi(t)`, `g = t`, `b = u-1`, one quotient line, `d_1 = deg phi`,
connected generic fibre, `g` étale on the affine part:

```text
2G       = (d_1 - 1)(b - 1) - s                       (independent of the shape of phi)
Xi       = d - s - b = (1+b) - s - b = 1 - s          (so Xi < 0  <=>  s >= 2)
at a critical point of phi of multiplicity m:
   germ  = Brieskorn (b, m),  mu = (b-1)(m-1),  r = gcd(b,m),
   2 g_loc = (b-1)(m-1) - gcd(b,m) + 1
necessary global condition  G >= max_m g_loc :
   (b-1)(d_1 - m) + gcd(b, m) >= s + 1   for every critical multiplicity m.
```

For `phi` a pure power (`m = d_1`, one critical point) this reads
`gcd(b, d_1) >= s+1`. The recorded control is `(b,d_1,s) = (5,2,2)`:
`gcd(5,2) = 1 < 3`, failing by exactly one unit of genus (`G = 1`, `g_loc = 2`).
That is report 2's obstruction, in closed form, and it shows the failure is
arithmetic, not accidental. It also shows `d_1 = 2` is doomed in general:
`gcd(b,2) <= 2` forces `s <= 1`, hence `Xi = 1-s >= 0`.

**But the binding case is only the pure power.** For `phi` with several critical
points the term `(b-1)(d_1-m) >= b-1` makes the condition easy. Concretely:

> **Repaired degree-six control.** Keep `u = 6`, `b = 5`, `s = 2`; replace
> `phi = t^2` by any degree-3 `phi` with two simple critical points, e.g.
> `phi(t) = t^2(t-1)`. Then

```text
d = 1 + b = 6,     d_1 = 3,     n = 3,     W = d_1 b = 15,
chi_gen = d - W = -9,           2G = (3-1)(5-1) - 2 = 6,  G = 3,
delta = 1 - chi_gen = 10 = 2G+s+n-1,        K = b(d_1-1) = 10,
Xi  = d - s - b = -1 = K - (delta + s - 1).
Two atypical values (the two critical values of phi); at each:
   germ = Brieskorn (5,2) = A_4, mu = 4, r = 1, g_loc = 2  <=  G = 3   OK
   local jump = mu + q_gen - 1 = 4 + 2 - 1 = 5;  total 5+5 = 10 = delta  OK
   collided cluster weight w = 5 = b  (zero excess, by the promoted family)  OK
RH check: 2G-2 = -2(6) + 3*(5-1) + (6-2) = 4.                              OK
```

and the passport exists. I verified an explicit transitive Hurwitz datum by
computation:

```text
tau_1 = tau_2 = (1 2 3 4 5),  tau_3 = (0 1 2 5 4),  tau_inf = (0 4 1 5 3)   in S_6
all of type (5,1);  tau_1 tau_2 tau_3 tau_inf = id;  transitive;  group = A_6 (360)
R = 4+4+4+4 = 16,  2G-2 = -12+16 = 4,  G = 3,  s = #cycles(tau_inf) = 2
poles of g-order 5 and 1  (same pole structure as the recorded control)
```

A second, independent repaired control with a *pure power* `phi` also exists,
saturating the genus budget exactly: `(b, d_1, s) = (6, 3, 2)` (`u = 7`,
`f = s^6/6 + t^3`), giving `d = 7`, `n = 3`, `W = 18`, `chi_gen = -11`, `G = 4`,
`delta = K = 12`, `Xi = -1`, `mu = 10`, `r = 3`, `g_loc = 4 = G`,
`gcd(6,3) = 3 = s+1`; witness `sigma_1 = sigma_2 = (0 1 2 3 4 5)`,
`sigma_3 = (1 2 3 4 5 6)` in `S_7`, all type `(6,1)`, product of type `(5,2)`,
transitive, `R = 20`, `G = 4`. Here the local monodromy is weighted-homogeneous,
`h(s,t) = (zeta_6 s, zeta_3 t)`, which fixes each of the three branches
`t = c zeta_3^j s^2` individually, so the three complementary disks are
individually preserved and the two poles can sit in two of them — the obvious
equivariance objection does not bite.

So: **a weaker common realization remains meaningful, and it is not a PALF.**
The surviving object is report 2 §5's packet, re-posed on genus-consistent
parameters and with the PALF language dropped (C13). Items 2--5 of that packet
are the right shape; item 5 ("integral handle matrix plus the boundary
3-manifold check for the claimed `D^4` filling") should be struck as
category-inappropriate and replaced by "a proper map to a disk with the stated
boundary divisor and nowhere-vanishing `df ∧ dg`".

## 8. Item 7 — FALLACY-v2 hazard sweep

* **Flag / place / series.** Handled correctly in R2 §1 and §3 ("the two moving
  points... are finite-end places") and in R1 §2's closing sentence. **But**
  R1 §2's own construction violates it: "two endpoints among actual pole places"
  identifies a quotient flag with a physical pole, and the only computed germ
  says the endpoints are finite-value places. See C9. R1 §3's "mark any two of
  the four boundary components as poles" is a bare label with no `g`-structure;
  R1 and R2 §4 both say so. No Puiseux-series substitution occurs anywhere.
* **Boundary vs interior.** The central real distinction of this pair, and R2
  §2 gets it right. Hazard retained: R2's "`H~_0` term" language can be misread
  as a drop in `b_0` of the *fibre*; locally `Δb_0 = 0` and `b_1` drops by the
  full 5 (`6 -> 1`), whereas globally the passport has `Δb_0 = +1`, `Δb_1 = -4`.
  R2 §3 (3.1) states the difference correctly; the §2 wording should point at
  the relative group `H_1(M_a, M_a ∩ D)`, which is the object that actually
  has dimension 5, and not at `b_0`.
* **Relative vs absolute.** R2 identifies the correct relative pair. R1's
  `V_aux` is never declared relative or absolute; given C16 it should be
  relative, and then C9's vertex-set repair follows.
* **Filling vs polynomial.** Two failures, both in R1: `D^4 != A^2`, and — the
  serious one — a Keller `f` is a submersion, so the interior-Lefschetz category
  is empty and no PALF models it. See C13.
* **Floor vs attainment.** Both reports keep `K >= delta+s-1` as a floor and
  never assert equality; `Xi = 0` would be the sharp case and is not claimed.
  Clean.
* **Carrier / attainment, per-ray charge, pole/interior identities, `sat()`
  wrapping, raw remainder degree, merge-free / M-descent, target/arrival index.**
  Not engaged by either report. No exit set is typed, no ray is charged, no pole
  identity is applied, no ideal is saturated, no normal form is taken, Statement
  8.5 is not invoked, and no `nu` index appears. Nothing to flag.
* **Variable / ring map.** The composition-order convention for the passport
  permutations is load-bearing and unstated (only right-to-left gives product
  `= 1`). The `A_6` claim needed an order computation, not a parity argument.
  Both now pinned above.
* **Prime label / derivative.** `P_i'` in R1 §1 is genuine differentiation
  (`ord_z(P_i')`), unambiguous. `sigma_+`/`sigma_-` are labels for the two
  finite branch values, not signs of anything. Clean.
* **Actual-map scope.** Neither report constructs a Keller pair, a polynomial
  model, a common surface germ, or a map. Both say so. My repaired controls in
  §7 are also **not** Keller pairs and **not** glued families: every member of
  the promoted `u`-family carries a boundary pole of `f` of order `b` and is not
  polynomial on `A^2`. Nothing here is promotable.
* **Custody.** R1 cites campaign artifacts by prose name with no hashes; R2 and
  the coordinator use pins. See C8.

## 9. Maximum exact theorem safe to retain

Retain the following, and nothing stronger.

**T1 (auxiliary tier).** With `b_i in Z_{>0}`,
`K = sum_i b_i(deg P_i - 1) = sum_i b_i mu_fin(P_i) = dim V_aux`, where `V_aux`
is the `b_i`-weighted sum of reduced `H_0` of the local Milnor fibres of the
`P_i`. After independently morsifying `b_i` disjoint copies of each `P_i`, `K`
is the length of a positive half-twist factorization for the disconnected
auxiliary cover of `A^1_a`. No page-`H_1` reading is licensed, and for a Keller
pair none can exist, since `f` is a submersion.

**T2 (conditional linear algebra).** If `F` is connected and there exist
surjections `∂: V_aux ->> H~_0(V;Q)` and `Psi: ker ∂ ->> H_1(F;Q)` with `V` a
set of `s` places, then `K >= delta + s - 1`, i.e. `Xi >= 0`. No such pair is
constructed; with `V` = pole places the only computed collision event maps to
zero, and with `V` = all `s+n` places at infinity the conclusion is
contradicted by the controls. Untyped, not proved, not disproved.

**T3 (topological no-go).** There is a PALF on `D^4` with page `Sigma_{1,4}` and
five positive vanishing cycles whose classes form a `Z`-basis of
`H_1(Sigma_{1,4};Z)`. Hence no theorem of the form
"[positive Lefschetz filling by `D^4`] + [page `b_1 = delta`] + [`s` marked
boundary components] `⟹` #cycles `>= delta + s - 1`". This constrains slogans
only; it constrains no live algebraic route.

**T4 (local, exact).** For `f = t^2 + s^5/5`, `g = t`, `D = {s=0}`: `A_4`,
`mu = 4`, one branch, `M_a ≅ Sigma_{2,1}`, `M_a ∩ D` two points,
`chi(M_a \ D) = -5`, central normalized punctured disk `chi = 0`, local affine
jump `= mu + q_gen - 1 = 5 = b(d_1 - q(0))`, and the five units are
`H_1(M_a, M_a ∩ D)`, of dimension `4 + 1`, **not** five interior
Picard--Lefschetz cycles. General form: `jump = (mu + r - 1) + (q_gen - r) = mu + q_gen - 1`.

**T5 (passport, exact).** `(5,1)^3` on six letters with right-to-left product
`= 1` generates `A_6` transitively; `R = 12`, `G = 1`, four labelled ends,
`F_Hur = Sigma_{1,4}`, `b_1 = 5`, `chi_gen = -4`, `delta = 5`; coalescence gives
`G_m ⊔ A^1`, `chi = 1`, jump `5`, `(1,5) -> (2,1)`.

**T6 (obstruction, strengthened).** `Sigma_{2,1}` embeds in no genus-`<=1`
surface (symplectic rank 4 > 2). Moreover, for a connected generic fibre with a
single quotient line and `g` étale on the affine part,
`2G = (d_1-1)(b-1) - s`, so the germ of T4 forces `G <= 1 < 2 = g(M_a)` for
every `s >= 1`. The germ therefore has **no** single-quotient-line global model,
independently of any passport.

**T7 (GENUS-BUDGET, new necessary condition).** For the promoted zero-excess
family `f = s^b/b + phi(t)`, `g = t`, one quotient line: `Xi = 1 - s`, and for
every critical multiplicity `m` of `phi`,
`(b-1)(d_1-m) + gcd(b,m) >= s+1` is necessary. For pure-power `phi` this is
`gcd(b,d_1) >= s+1`, which the recorded control fails (`gcd(5,2)=1 < 3`) and
which forces `Xi >= 0` whenever `d_1 = 2`. This is a genuinely new constraint,
absent from every reviewed artifact, and it is **not** a step toward QCS: it is
a filter on controls.

**T8 (repaired controls, arithmetic + Hurwitz tier only).** `(b,d_1,s) = (5,3,2)`
with two simple critical values gives `d = 6`, `n = 3`, `G = 3`,
`K = delta = 10`, `Xi = -1`, `g_loc = 2 <= 3`, and the transitive `A_6` datum
`(1 2 3 4 5),(1 2 3 4 5),(0 1 2 5 4),(0 4 1 5 3)`. `(b,d_1,s) = (6,3,2)` gives
`d = 7`, `G = 4 = g_loc`, `K = delta = 12`, `Xi = -1`, with the `S_7` datum
`(0 1 2 3 4 5),(0 1 2 3 4 5),(1 2 3 4 5 6)`. Both pass every desk-scale test
that kills the recorded control. Neither is glued, neither is polynomial,
neither is a Keller pair, and neither is promotable.

## 10. Cheapest next discriminator

**GLUE-OR-KILL at `(b, d_1, s) = (5, 3, 2)`.** This is the minimal perturbation
of the recorded control — same `d = 6`, same baseline `b = 5`, same `s = 2`,
same pole orders `(5,1)`, same `Xi = -1` — with only `phi = t^2` replaced by a
degree-3 `phi` with two simple critical points. Decide:

1. **(cheap, desk)** Does a smooth quasi-projective surface `S` with boundary
   divisor `D`, a proper-over-a-disk fibration `f`, and a function `g` with
   `df ∧ dg` nowhere zero realize the germ `s^5/5 + phi(t)` at `D` *and* the
   genus-3 degree-6 `g`-cover? Sub-checks: (a) the two `A_4` Milnor fibres embed
   at the two atypical values (they do, `2 <= 3`); (b) the special-fibre
   ramification profile at each atypical value is `(5,1)` over the surviving
   root and `(5)` over the collided one, and `chi_a = -4` independently of the
   pole count (I verified this last identity: the check is `s`- and
   `c`-independent, so it cannot discriminate — use (a) and the monodromy
   equivariance instead).
2. **(cheap, desk)** Monodromy equivariance: the local geometric monodromy of
   `A_4` must be compatible with the global `A_6` monodromy of the `g`-cover and
   with the fixed pole set. For the `(6,3,2)` variant I already checked that the
   weighted-homogeneous monodromy `(zeta_6 s, zeta_3 t)` fixes each branch, so
   the obvious equivariance objection does not fire; run the same check for
   `(5,3,2)`.

If (1)+(2) pass, the joint-consistency barrier has a genus-consistent witness
and report 2's obstruction is confined to the recorded representative. If either
fails, the failure mode is a **second** necessary condition beyond GENUS-BUDGET,
and that would be the first genuinely new positive lever in this lane — at which
point it, not `STRICT-COLLIDE-POLY`, becomes the cheapest route to `Xi >= 0`.

Do **not** run any mapping-class or Kirby enumeration: report 2 §4 is right that
it is a guaranteed false positive, and C13 shows the category is empty for a
submersive `f`.

## 11. Ruling: sharpen or overclaim?

**Both, in different places, and the net effect is that the dependency barrier
is currently weaker than either report states.**

* Report 1 **sharpens the typing**: `K` is pinned exactly at the auxiliary
  quotient tier, the target `K >= delta+s-1` is verified to be exactly the
  promoted `Xi >= 0`, and the two missing maps are named precisely. Its `A^2`/PALF
  framing is a category error (C13) and its pole-endpoint sentence is refuted
  (C9), but its conclusion — the route is untyped, not proved, not disproved —
  survives both repairs and is if anything better supported after them.
* Report 2 **removes a piece of the barrier** rather than sharpening it. The
  degree-six control was the campaign's only *joint* witness that the reviewed
  constraint set fails to force strictness; report 2 shows the germ and the
  passport cannot coexist, so that joint witness is gone. Its own nonclaim
  sentence ("invalidates neither ... the degree-six dependency control") is an
  accidental **overclaim of the surviving barrier** (C24). In the opposite
  direction it **underclaims its own obstruction** (C23): the passport genus is
  forced by the germ, so the incompatibility is germ-intrinsic and no alternative
  passport helps.
* Taken together with §7: report 2's obstruction is real, exact, and correctly
  kills the recorded control, but it does **not** close the lane. Two repaired
  controls at the same degree pass the genus budget and have explicit transitive
  Hurwitz data. So the honest current state is: the joint-consistency barrier is
  **unwitnessed but not refuted**, and the coordinator's existing narrowing
  ("the two objects are not glued"; "bridge refuted" superseded) remains the
  correct lifecycle language — now upgradeable to "cannot be glued *for the
  recorded representative*", with the recorded representative replaceable.

## 12. Nonclaims

This review promotes nothing. It does not prove or refute QCS or PCB, does not
construct a Keller pair or a counterexample, does not construct a common surface
germ, does not build `∂_P` or `Psi`, and draws no JC2 conclusion. The repaired
controls in §7 and §9 T8 are arithmetic-plus-Hurwitz objects only: they are not
polynomial on `A^2`, not Keller pairs, and not glued families; they are offered
solely as the cheapest falsifier of a lane closure. No exit set is typed, no ray
is charged, no book budget is consumed, and no exit price is asserted. GENUS-BUDGET
(T7) is a necessary condition on controls, not a lower bound on `Xi`. No `jc2-lean`
object was inspected, and no canonical ledger or existing artifact was modified.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `40810`.
- Body SHA-256:
  `61a9e817aa7926deb6a7f07464787e0b3c4b8c7d641ce8874a31faaab7b90364`.
- Frozen basis: `0375694aa21fd8db3b465ef2098ca539106a1582`.
