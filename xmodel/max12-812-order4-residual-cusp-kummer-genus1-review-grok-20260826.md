# Hostile review — `(8,12)` order-four residual cusp and deck-genus gate

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md` |
| Target SHA-256 | `cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none that breaks a numbered genus, divisor, or Riemann–Hurwitz claim |
| Smallest missing hypothesis | the source projection/nonconstancy gate of §0 and §5, which the target correctly refuses to treat as proved |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. No prior `CONFIRMED`/`REPAIR` string, and no sentence of the target, is an input to a hull, face, order, or genus identity |
| Method | SHA-256 of the target and of every Section 5 artifact; reading of those stdouts, their Singular scripts, and the freeze/metadata under `cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/`; independent exact `fractions.Fraction` arithmetic for Newton data, face identities, left transverse, weighted discriminant, and the local Newton polygon after the correct cubic tangent; no Singular/`hnoether.lib` replay |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named target uncommitted) |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756`, matching the launch pin. Independently recomputed SHA-256 of every Section 5 artifact matches the printed string. Frozen inputs named in `FREEZE_MULTIPRIME_V2.sha256`, `FREEZE_TOP_LOCAL_V3.sha256`, `FREEZE_TOP_DELTA_V4.sha256`, `FREEZE_TOP_HN_V5.sha256`, and `FREEZE_BOUNDARY_Q_V2.sha256` rehash. All thirty-two prime-stdout hashes recorded in the candidate JSON rehash. The prior nondegenerate toric note’s genera `7/37/165` were opened only as a control whose hypothesis is visibly false here; they are not promoted. No file other than this review was written.

---

## Verdict

Unconditionally, on the reconstructed residual plane `P(q,v)=0`: the Newton polygon, area `23/2`, boundary length `11`, and seven interior lattice points recompute; `P` is irreducible over `Q` and, by Ostrowski, geometrically irreducible; exact membership of the cleared substitution in the `r_7`-saturated source is a containment, not a dominance or elimination equality; length four plus Hessian unit on the torus singular scheme yields four reduced ordinary nodes over the algebraic closure; every toric boundary point is accounted for; the top point `q=-4/27` is one `(2,7)` branch of local delta three with `ord(v)=-6`, not two branches of order `-3`; `g(X)=7-4-3=0` and `div_X(v)=8P_0-P_{ul}-P_A-6P_B` are complete; `y^4=v` is a geometrically irreducible cyclic degree-four cover of Riemann–Hurwitz genus `1`.

Conditionally, the `mu_4\neq 0` source leaf is empty only if every relevant component maps nonconstantly to this `Y`. That projection gate is open. Nonconstancy of `rho=r_7^4` does not force it. The note does not promote a source elimination, and does not promote the failed-hypothesis genera `7/37/165`.

The displayed cubic tangent `w=(1/52488)Q^3` in §2.3 and `(2.4)` is the coefficient of `l_B^3=(27Q)^3`, equivalently `(3/8)Q^3` in the coordinate `Q=q+4/27` that the prose names. This is a wrong leading constant in a displayed expansion. It does not change `ord(v)=-6`, delta three, the divisor, or `g(Y)=1`.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-residual-cusp-kummer-genus1-gate-20260826.md` | `cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756` | target (matches required pin) |
| `.../run/candidate.json` | `706505e02f57e6991170e230738d6a8b96b5ac82ed2ec3fa83b1ba8ff498508d` | reconstructed candidate JSON |
| `.../run/exact_candidate.stdout` | `9b0e08c2d826286364f07f6a6fba9560e23ca8ea4fcba15cbbcf373152badbe3` | membership / Q-irreducibility / four-node stdout |
| `.../aws_toplocal_v3/...stdout` | `b7aa07121bc761acd8dd0a3342bb8f5321da8e38c4068859edb23e0b8d0094ff` | face identities, discriminant, left transverse |
| `.../aws_topdelta_v4_retry1/...stdout` | `4791594d69326fc6725e72bd15b6900988cc04f18fa7aaf050fa306c63c33a0a` | local delta |
| `.../aws_tophn_v5/...stdout` | `59c2c35f2288f6c983925dba4a855a28e49eadc9d9db5ef84aa78b6bed2a971d` | Hamburger–Noether |

Paths are under `cases/max12_812_order4_mu4_nonzero_quotient_passport_20260826/`. Reconstruction stdout independently records `RECONSTRUCTION_STABLE_16_24_32=1`, `SUPPORT_SIZE=18`, and the same candidate hash. The monomial substitution `(q,v)=(a_5^2/a_6^3,a_6^8)` pulls the residual support onto the JSON `(a_5,a_6)` support identically (18 terms). `SINGULAR_INPUT.sha256` of the V3/V4/V5 jobs equals the freeze hash of the corresponding `.sing` file.

---

## Strongest exact theorem that survives

**Unconditional (reconstructed plane).** Let `P\in Q[q,v]` be the displayed residual polynomial of Section 1 of the target (the unique polynomial with the charged 18-term support, leading torus monomial `q v^3`, and constant term `8503056/121`). Let `X` be the normalization of the closure of `P=0` in the toric surface of its Newton polygon. Then `P` is geometrically irreducible, that closure lies in the smooth locus of the (possibly singular) toric surface, and

```text
g(X)=0,
div_X(v)=8 P_0 - P_ul - P_A - 6 P_B.
```

The Kummer curve `Y: y^4=v` is geometrically irreducible of degree four over `X`, and its complete normalization has `g(Y)=1`.

**Conditional (source).** If every relevant irreducible component of the corrected, `r_7`-saturated coefficient fibre, in the chart `a_6\neq 0`, maps nonconstantly to this `Y` by `q=a_5^2/a_6^3`, `y=a_6^2`, then there is no exact-order-four `mu_4\neq 0` source: the source deck quotient is `P^1_x`, properness extends the rational map across poles, and a genus-one complete curve admits no nonconstant morphism from `P^1`. Exact membership of the cleared substitution in the saturated source ideal is already known and is not this hypothesis. Nonconstancy of `rho=r_7^4` is not this hypothesis.

Nothing here is a Taylor realization or a Keller pair. The genera `7/37/165` of the nondegenerate control are not conclusions of this plane.

---

## Attack 1 — Newton hull, area, boundary, seven interior points

**CONFIRMED.** The 18-term support of the charged residual polynomial is

```text
(0,0),(0,1),(0,2),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),
(3,2),(3,3),(4,2),(4,3),(5,2),(5,3),(6,3),(7,3),(8,3).
```

All four vertex coefficients are nonzero: `(0,0)` is `8503056/121`, `(0,2)` is `5184`, `(1,3)` is `1`, `(8,3)` is `-3587901148629/1982464`. No other support point lies on the four extreme edges (the lower edge `3x=8y` contains only `(0,0)` and `(8,3)`; the upper-left edge `y=x+2` contains only `(0,2)` and `(1,3)`). The convex hull is therefore exactly

```text
Delta=conv{(0,0),(0,2),(1,3),(8,3)}.
```

Shoelace on the clockwise circuit `(0,0)\to(0,2)\to(1,3)\to(8,3)\to(0,0)` gives signed area `-23/2`. Lattice lengths `gcd(0,2)=2`, `gcd(1,1)=1`, `gcd(7,0)=7`, `gcd(8,3)=1`, so `B=11`. Pick: `I=23/2-11/2+1=7`. Direct enumeration of strict interior lattice points:

```text
(1,1),(1,2),(2,1),(2,2),(3,2),(4,2),(5,2).
```

Seven points, matching Pick. The toric arithmetic genus of the closure is these seven interior points. This count is not the geometric genus; faces are not squarefree, so the nondegenerate identification `g=I` is false.

---

## Attack 2 — irreducibility and what membership does not prove

**CONFIRMED, with the membership limitation exactly as the target states it.**

Charged exact stdout:

```text
EXACT_CANDIDATE_MEMBER=1
EXACT_PLANE_FACTOR_COUNT=1
EXACT_RESIDUAL_FACTOR_COUNT=1
EXACT_SOURCE_SAT_DIM=1
```

The verifier reduces the displayed plane polynomial `FCAND\in Q[a_5,a_6]` against `modStd` of the `r_7`-saturation of the corrected tail ideal, and factorizes both `FCAND` and `P` over `Q`. Containment of the image of the `a_6\neq 0` locus in `V(P)` follows. Dimension one of the saturated source does not prevent a component from contracting to a point of `V(P)`. Factorization over `Q` is not, by itself, geometric irreducibility.

Geometric irreducibility is nevertheless forced by the Newton polytope, independently of the factorizer. The four primitive edge directions `(0,1)`, `(1,1)`, `(1,0)`, `(-8,-3)` are pairwise non-parallel, so `Delta` is not a segment plus a polygon (that construction always produces a parallel pair). Enumerating lattice length-splits of the four edges shows that the only ways to write the edge loop as a sum of two closed lattice loops give a point plus `Delta`. Area `23/2` has prime numerator, so `Delta` is not an `n`-fold dilate of a smaller lattice polytope. Ostrowski: a polynomial whose Newton polytope is Minkowski-indecomposable is irreducible over the algebraic closure, up to units; `deg_v P=3` independently forbids a proper power. Thus `P` is geometrically irreducible. The same holds for `FCAND`, whose polytope is the image of `Delta` under `(i,j)\mapsto(2i,-3i+8j)`.

What membership does **not** prove: elimination equality in `Q[q,v]` or `Q[q,y]`; birationality of `C_4` onto `V(P)`; dominance; that `(q,y)` is nonconstant on every component; that `L(C_4)=L(q,v)(w)`. The target states this in §1 and again in §5. The failed combined token `EXACT_NODE_BOUNDARY_CERTIFICATE=FAIL` is the correct refusal of the nondegenerate package (the verifier demanded `vdim=3` and squarefree faces; the plane has `vdim=4` and both left and top faces non-squarefree).

---

## Attack 3 — length four plus Hessian unit, four ordinary torus nodes

**CONFIRMED over the algebraic closure.**

The verifier saturates the Jacobian ideal `(P,\partial_q P,\partial_v P)` by `q v`, then prints `dim=0`, `vdim=4`, and that the affine Hessian `P_{qq}P_{vv}-P_{qv}^2` generates the unit ideal on that Artinian ring. Charged stdout matches the script. In characteristic zero, a geometric point of a plane curve at which the gradient vanishes and the `2\times 2` Hessian is nonzero is an `A_1` node (nondegenerate quadratic form; Morse lemma). An `A_1` has Tjurina number one, so the Jacobian scheme is reduced of length one at each such point. Hessian a unit in the coordinate ring means Hessian is nonzero in every residue field, hence at every geometric point. Length `4` over `Q` of a reduced zero-dimensional scheme is four geometric points over `Qbar` (possibly in conjugate residue extensions). They lie in the torus because of the saturation by `q v`. They are therefore four reduced ordinary torus nodes over the algebraic closure, not one fat point of length four, not an `A_{k\ge 2}`, and not a boundary singularity.

The length is four, not three: the verifier’s bundled `PASS` path required `vdim==3` and squarefree faces, and correctly printed `FAIL`. The target uses the printed `4` and does not revive that bundle.

---

## Attack 4 — every toric boundary point

**CONFIRMED. No missing corner, no missing open-edge place.**

Clockwise traversal, inward primitive normals (interior to the right):

| edge | primitive inward | lattice length | `ord(q)` | `ord(v)` |
|---|---|---:|---:|---:|
| `[(0,0),(0,2)]` | `(1,0)` | `2` | `1` | `0` |
| `[(0,2),(1,3)]` | `(1,-1)` | `1` | `1` | `-1` |
| `[(1,3),(8,3)]` | `(0,-1)` | `7` | `0` | `-1` |
| `[(8,3),(0,0)]` | `(-3,8)` | `1` | `-3` | `8` |

The ambient 2-cones at `(0,0)` and `(8,3)` are not regular (`|det|=8` and `3`). The curve misses both fixed points because the vertex coefficients are nonzero, so it lies in the smooth locus of the toric surface (open 1-strata and the dense torus). No extra delta is hiding at a corner.

**Left edge.** Independently, `P(0,v)=(1296/121)(22v-81)^2`. One point `v=81/22\neq 0`. The `v`-derivative vanishes there, as required of a tangency. The transverse coefficient is `\partial_q P(0,81/22)=123466498884/14641\neq 0`, matching the charged V3 token, so the curve is smooth and tangent to `{q=0}` with intersection multiplicity two. On the normalization `ord(q)=2`, `ord(v)=0`. Delta zero. The left face is not squarefree (`EXACT_LEFT_FACE_SQUAREFREE=0`); that is a tangency, not a node.

**Upper-left primitive edge.** Two-term face `5184 v^2 + q v^3`. Lattice length one, one simple torus root. Smooth branch with `(ord(q),ord(v))=(1,-1)`, approaching `(q,v)=(0,\infty)` in ordinary affine coordinates, not an omitted corner.

**Top edge.** Independently exact:

```text
H(q)=(-1/1982464)(9261q-484)(27q+4)^6,
L_2(q)=(81/30976)(120771q^2+189396q+30976)(27q+4)^3.
```

Remainders zero, scales matching V3. The simple root `q_A=484/9261` is not a root of `L_2` (`L_2(q_A)=11577755326021632/678223072849\neq 0`) and is not `-4/27`. One smooth branch, `ord(v)=-1`. This is `P_A`. The residual quadratic `Q_2` has nonzero discriminant `20906834832` and `Q_2(-4/27)=5568\neq 0`, so the order of `L_2` at `q_B` is exactly three.

**Lower primitive edge.** Binomial face on lattice length one: one simple boundary point, `(ord(q),ord(v))=(-3,8)`. Unique zero of `v`. This is `P_0`.

---

## Attack 5 — HN at `q=-4/27`: one `(2,7)` branch, delta three, slope, `ord(v)=-6`

**CONFIRMED for branch count, type, delta, and `ord(v)=-6`. The printed coefficient `1/52488` of `Q^3` is a chart mix.**

Multiplicities independently: `mult(H,q_B)=6`, `mult(L_2,q_B)=3`, `L_1(q_B)=-46235367/121\neq 0`, `l_A(q_B)=-1856\neq 0`. In the chart `w=1/v`, `Q=q+4/27`, the weight-`6` initial form (weight `wt(Q)=1`, `wt(w)=3`) is the quadratic

```text
A_{\mathrm{raw}} Q^6 + B_{\mathrm{raw}} Q^3 w + C w^2
```

with `C=-46235367/121` and discriminant zero. The V3 numbers `A=-29/209088`, `B=7047/484`, `C=-46235367/121` are the coefficients after dividing out `l_B=27Q` powers, i.e. of `A\,l_B^6+B\,l_B^3 w+C w^2`. They satisfy `B^2-4AC=0` and `-B/(2C)=1/52488`, matching the charged tokens. The actual tangent in the `Q`-chart is

```text
w = (1/52488)\,l_B^3 + \cdots = (3/8)\,Q^3 + \cdots.
```

After the correct translation `w\mapsto w+(3/8)Q^3`, the weight-`6` mixed and `Q^6` terms cancel, leaving `C w_{\mathrm{des}}^2`, and the next Newton face is the primitive segment `[(0,2),(7,0)]` with no lattice points of `2i+7j<14`. That is one branch of type `y^2=c x^7`, characteristic exponents and semigroup `\langle 2,7\rangle`, conductor `6`, gaps `{1,3,5}`, local delta `3`. Charged V4/V5 tokens `TOP_QB_DELTA=3`, `TOP_QB_ISOLATED=1`, `TOP_QB_BRANCHES=1`, `TOP_QB_BETA=2,7`, `TOP_QB_SEMIGROUP=2,7`, `TOP_QB_CONDUCTOR=6` agree. The HN translation in V5 by `(1/52488)Q^3` does not cancel that tangent, but `w\mapsto w+c Q^3` is an automorphism of the plane, so the printed invariants are still those of the same germ.

Intersection multiplicity of the curve with the top divisor `{w=0}` at `q_B` is `6` (the factor `(27q+4)^6`). One branch, therefore `ord(w)=6` and `ord(v)=-6` on the unique point of `X` above `P_B`. Two smooth branches of pole order three would require a nonzero discriminant and would be incompatible with delta three on a single germ. That split is false.

The sentences in §2.3 and `(2.4)` that write `w=(1/52488)Q^3+\cdots` and `w=(1/52488)\tau^6+O(\tau^7)` with `Q=q+4/27` and `Q=\tau^2\cdot(\mathrm{unit})` use the `l_B`-normalized coefficient in the `Q`-chart. Replace `Q^3` by `l_B^3`, or replace `1/52488` by `3/8`. The order `ord(v)=-6` does not change.

---

## Attack 6 — genus subtraction `7-4-3=0` and completeness of `div(v)`

**CONFIRMED. No missing place in the divisor.**

Arithmetic genus of the toric closure is `I=7`. Singularities of that closure: four ordinary torus nodes (`delta=1` each) and one top `(2,7)` cusp (`delta=3`). The left tangency, the two primitive-edge points, and the simple top root are smooth. The curve misses the ambient fixed points. Hence

```text
g(X)=7-4\cdot 1-3=0.
```

The function `v` is a unit at the left tangency (`v=81/22`) and at every torus node. Its zeros and poles on `X` are exactly the places of Attacks 4–5:

```text
div_X(v)=8 P_0 - P_ul - P_A - 6 P_B.
```

Zero degree `8`, pole degree `1+1+6=8`. No other boundary divisor, and no interior zero or pole (`v` is a torus coordinate). Completeness of the principal divisor is this degree match together with the exhaustive edge list.

---

## Attack 7 — exact-order-four Kummer, local table, `g(Y)=1`

**CONFIRMED. The false nondegenerate genus `37` is not used.**

Valuations `-1` at `P_ul` and at `P_A` are odd, so `v` is not a square in the geometric function field, hence not a proper power of exponent dividing `4`. The cover `y^4=v` is geometrically irreducible of degree four. A place of valuation `n` contributes `4-\gcd(4,n)` to the ramification divisor, with `\gcd(4,n)` geometric points above it, each of inertia `4/\gcd(4,n)`. Independently:

| place | `ord(v)` | `gcd` | points | inertia | contribution |
|---|---:|---:|---:|---:|---:|
| `P_0` | `8` | `4` | `4` | `1` | `0` |
| `P_ul` | `-1` | `1` | `1` | `4` | `3` |
| `P_A` | `-1` | `1` | `1` | `4` | `3` |
| `P_B` | `-6` | `2` | `2` | `2` | `2` |

Total `R=8`. Riemann–Hurwitz, using `g(X)=0` and this `R` only:

```text
2g(Y)-2=4(2\cdot 0-2)+8=-8+8=0, \qquad g(Y)=1.
```

Every zero and pole of `v` is in the table. The left tangency and the four nodes have `ord(v)=0` and contribute nothing. The false split of `P_B` into two places of order `-3` would have produced two contributions of `3`, total `R=12`, and `g(Y)=3`; that calculation is excluded by Attack 5. The nondegenerate top edge (seven simple places of order `-1`) is likewise excluded by the factor `(27q+4)^6`.

---

## Attack 8 — source firewall; weakest sufficient nonconstancy

**CONFIRMED. The target’s refusal is the right one.**

The reconstructed `Y` is a complete geometrically irreducible curve of genus one. A nonconstant morphism `P^1\to Y` is impossible. The source deck quotient is `P^1_x`; properness extends any rational map. Therefore the **weakest exact statement that excludes the leaf** is:

```text
on every relevant component of the corrected r_7-saturated fibre,
the map to the (q,y)-plane is nonconstant.
```

Exact membership already lands that map on `V(P(q,y^4))`. Geometric irreducibility of `Y` then makes a one-dimensional image dominate `Y`. One does not need birationality onto `Y`, equality of elimination ideals, or any statement about `rho`.

Nonconstancy of `rho=r_7^4` does **not** force this. A component may be vertical over a point of `Y` with `rho` still varying. In that case the map `P^1_x\to Y` is constant and genus one is no obstruction. Algebraicity of `rho` over `Q(q,y)` on every relevant component would convert `rho`-nonconstancy into `(q,y)`-nonconstancy; that algebraicity is not proved. The target correctly declines to treat the known nonconstancy of the terminal map as a map to this `Y`.

The successor list in §5 is strictly stronger than the weakest sufficient gate (it also asks that the contraction equal `P(q,y^4)` and that `rho` not vary in a fibre). The extra strength is harmless as a next job; it is not necessary for exclusion once one-dimensionality of `(q,y)` is known.

---

## Attack 9 — `a_6=0`, saturation, components, completion

**CONFIRMED: none of these evades the stated conditional theorem; all of them can evade an unconditional source elimination, which is not claimed.**

- **`a_6=0`.** The formulae `(0.4)` are for the chart `a_6\neq 0`. Substituting `a_6=0` into `FCAND` leaves a degree-`16` equation in `a_5` plus a nonzero constant, so the plane curve itself does not contain the line `a_6=0`. A source component on which `a_6\equiv 0` with other coordinates still moving would map to a point of the `(q,y)`-plane (or leave `q` undefined) and would fall outside the conditional hypothesis. Saturating by `a_6` can drop such a component; that is successor item 1, not a hole in the plane theorem.
- **`r_7` saturation.** The charged membership is in the saturated ideal. Components supported on `r_7=0` are a different leaf.
- **Several components.** Dimension one of the saturated source allows several curve components. The genus obstruction applies only to those whose `(q,y)` image is one-dimensional. A constant component must be treated separately, as §5 says.
- **Completion.** The genera and the ramification table are on the complete normalization of the toric closure, including every pole of `v`. Affine arithmetic genus is not used. Completing `Y` does not create a nonconstant map from `P^1` that the affine curve lacked.

No evasion of `g(Y)=1` on the reconstructed plane, and no evasion of the *conditional* source emptiness, is available from these. An unconditional emptiness claim would be evaded by any of them; the target does not make that claim.

---

## Control: the nondegenerate toric theorem

The predecessor note’s gates included Khovanskii nondegeneracy of every face of `Delta`. That hypothesis fails: `EXACT_LEFT_FACE_SQUAREFREE=0`, `EXACT_TOP_FACE_SQUAREFREE=0`, and the torus singular scheme is nonempty of length four. Its geometric genera `g(X)=7`, `g(Y)=37`, `g(C)=165` are therefore not theorems about this plane. They remain a consistent control on the *nondegenerate* polygon of the same hull: if the faces had been squarefree and the torus smooth, Pick would have given those numbers, and the top edge would have been seven simple places of `ord(v)=-1`. The present degeneracy subtracts exactly `4+3=7` from the virtual genus of `X`, collapsing it to zero, and replaces the nondegenerate Kummer ramification by the table of Attack 7. Using `37` here would be a false substitution; the target does not make it.

---

## Reported constant

In §2.3 and `(2.4)`, the repeated tangent is written as `w=(1/52488)Q^3+\cdots` with `Q=q+4/27`. Independently, `1/52488=-B/(2C)` is the coefficient of `l_B^3=(27Q)^3`, and the coefficient of `Q^3` is `3/8`. Read `(2.4)` as `w=(1/52488)l_B^3+O(\tau^7)=(3/8)Q^3+O(\tau^7)` with `Q=\tau^2\cdot(\mathrm{unit})`. No numbered genus, divisor, or Riemann–Hurwitz identity uses the leading coefficient.

---

VERDICT: CONFIRMED
