# HORN-FLAGSHIP — case (B3) attacked with the merged cusp toolset

Lane: `HORN-FLAGSHIP`. Date: 2026-09-02. Agent: Opus 5.
Desk derivation + exact symbolic leading-coefficient algebra (sympy 1.14,
integer/rational only). No Groebner, no AWS, no literature fetched. Four
drivers in `/tmp/hornflag`, not installed in `box/`.

## 0. Custody, hashes, method

The four charged frozen copies were hashed with `shasum -a 256` **before any
was read**; all four match the charge exactly:

```text
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  homcover-transfer-opus5-20260902.md
fadc17c809e72d64a493fc1fb16a739d441474b401f191081303de3b003d7d62  homcover-transfer-review-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
```

Below: **HT** = HOMCOVER-TRANSFER, **HR** = its gpt-5.5 hostile review,
**MI** = MPRIME-ALLN-H2, **C32** = CELL-32-TERMINATION. No charged file was
edited; no repository file was modified.

Everything in §4 was computed from C32's own displays with a monomial
(leading-coefficient) calculus, and **the whole apparatus reproduces C32 §5.1
exactly at `e=0`** — four independent identities, all difference `0` (§4.2).
That control is what licenses the general-`e` extension.

No `charge_basis` line: this report asserts no new exit price.

## 1. Verdict, up front

```text
(1) (B3) PRESENTATION.  The charge's "torus-knot group + k commuting-square
    relators" is FALSE as a presentation of G = pi_1(C^2 \ A_F) and is
    replaced by a correct ZvK statement (Sec 2.1).  Of the three cusp theorems:
      CUSP-PARITY    SURVIVES VERBATIM, in a strictly stronger all-degree form
                     (THEOREM B3-DEGREE): sgn rho(h) = eps^{deg h} for EVERY h.
      ORBIFOLD-CAGE  SURVIVES as a LOCAL, orbit-summed cage at each cusp
                     (THEOREM B3-CAGE), with a new geometric reading of r_c.
      CENTRAL-RANK   REFUTED globally (G has no centre in (B3)); survives
                     per-orbit inside the cusp's own local group.
    Two new laws are needed and proved: THEOREM B3-PUSHOFF and THEOREM
    B3-COMPONENT.
(2) THE CAGE ON (B3).  At N = 4 the cage is RIGID but NOT EMPTY.  It pins
    rho(G) = S_4, forces the cusp Puiseux pair to satisfy
    (2|p and 3|q) or (3|p and 2|q), and determines E = F^{-1}(A_F) completely:
    j = 1 with geometric genus k_odd - 1 when some double point has ODD
    contact, j = 2 with both components rational when all contacts are even.
    No EMPTY window in N is obtained.  Reported as found.
(3) THE A2 3x3 DETERMINANT AT e >= 1.  COMPUTED.  Chambers I (g>2e) and III
    (g<2e) TERMINATE OUTRIGHT.  Chamber II (g=2e) has
        det = 36 n (c + 2e)(c + 2e + 1),   c := G_{2e}/(b eta_e^2),
    and every branch of it closes EXCEPT the single wall c = -(2e+1).  That
    wall is exactly C32's Wall B.  Combining with C32's T5 (which sends the
    r'=0 section to the same wall):
      THEOREM HORN-A2.  On the live section with e >= 1, EVERY surviving pair
      has g = 2e and G_{2e} = -b(1+2e)eta_e^2, i.e. deg E1 <= 2e-1.
    The horn's live section does NOT close; it collapses to one explicit wall,
    with the three top coefficients pinned on a one-dimensional ray.
(4) COMPOSITION.  Nothing here closes (B3) at any N.  The H2 branch is not
    closed.  Sec 5 gives the per-window ledger and names what would compose.
```

## 2. Task (1): the (B3) group, and which cusp theorems survive

### 2.1 The presentation, derived — and the charge's claim corrected

Scope first. MI's `(B3)` says `A_F` has **a cusp** — MI §6 defines "cusp" in
the wide sense, *any unibranch singular germ*. The charge says
*quasi-homogeneous* cusp. That is a strictly narrower hypothesis: in case (A)
Lin-Zaidenberg supplies `{x^p=y^q}` and quasi-homogeneity is free, but in (B3)
`A_F` is not homeomorphic to `C` and Lin-Zaidenberg does **not** apply. I
work in the charge's scope and flag every use:

```text
SCOPE[B3-QH].  The cusp p_0 is assumed quasi-homogeneous, of type {x^p = y^q},
gcd(p,q)=1, p,q >= 2.  NOT banked from MI; charged assumption.  For a general
unibranch germ the local group is an iterated-torus-knot group and Sec 2.4
generalises through its JSJ/Seifert pieces; that generalisation is NOT done here.
```

Now the presentation. Let `n = deg_y bar A_F` for a generic projection
`pr:(x,y) |-> x`. Zariski-van Kampen gives `G = <x_1,...,x_n | R>` with `R`
collected over the discriminant points:

* **ordinary vertical tangency** (`v` of them): `x_i = x_j`;
* **double point of two smooth branches with contact `t`** (`A_{2t-1}`; local
  braid `sigma^{2t}`): `(x_i x_j)^t = (x_j x_i)^t`. For `t = 1` this **is** the
  commuting square `[x_i,x_j] = 1`; for `t >= 2` it is not;
* **the quasi-homogeneous cusp** (local braid `(sigma_1...sigma_{p-1})^q` on the
  `p` strands through it): the `(p,q)` torus-braid relations.

So the charge's sentence is right about *which* relators the double points
contribute — commuting squares, exactly when the double points are genuine
nodes — and wrong about the global shape:

> **CORRECTION.** `G` is **not** `G_{p,q}` with `k` relators adjoined. `G` has
> `n` generators, `n` being the degree of the projected curve, which is
> unbounded in `p,q,k`; the cusp's relators involve only `p` of them; and the
> tangency relations `x_i = x_j` are part of the data. What is canonical is
> the **homomorphism** `iota : Loc_{p_0} = G_{p,q} -> G` induced by inclusion,
> which is in general neither injective nor surjective. HT §2.2 (THEOREM
> NO-PUSHFORWARD, CONFIRMED by HR §1) is exactly the statement that this
> `iota` may destroy information, so nothing may be transported across it
> by analogy.

The consequence is methodological and it is the reason the rest of this section
works: **every (B3) theorem below is either global-and-abelian (§2.2) or
strictly local at a singular point (§2.3-§2.5), and none crosses `iota` in the
forbidden direction.** Locally, `rho ∘ iota` is a genuine `S_N`-representation
of `G_{p,q}` and everything HT proved about such representations applies.

### 2.2 CUSP-PARITY survives, in a stronger form

> **THEOREM B3-DEGREE.** Let `A_F` be irreducible (H2), `G = pi_1(C^2\A_F)`,
> `rho : G -> S_N` the ACS-1 monodromy, `m` a meridian. By LEMMA F1
> (HT §2.1, proved there) `G^{ab} = Z<m>`; write `deg : G -> Z` for the
> abelianisation. Then for **every** `h ∈ G`
> ```text
>       sgn rho(h) = eps^{deg h} ,      eps = sgn rho(m) = (-1)^{W - sum_l s_l}.
> ```
> *Proof.* `sgn ∘ rho : G -> {+-1}` is a homomorphism to an abelian group, so it
> factors through `G^{ab} = Z<m>` and is determined by its value on `m`; that
> value is `(-1)^{N - #cycles}` for the cycle type `1^a prod_l mu_l^{s_l}`
> of MI `[P3]` + 7.B, i.e. `(-1)^{W - sum_l s_l}`. ∎

This is HT's CUSP-PARITY with the case-(A) hypothesis deleted. It contains
HT's two identities as the special cases `h = alpha` (`deg = q`) and
`h = beta` (`deg = p`) once `iota` is applied, and it applies to elements HT
had no name for. Two uses below:

* `deg z = pq` for the central `z = alpha^p` of a `(p,q)` cusp, so
  `sgn rho(z) = eps^{pq}`;
* at a double point with contact `t`, the two branch meridians have `deg = 1`
  and their product has `deg = 2`, so `rho(g_1 g_2)` is always even.

### 2.3 CENTRAL-RANK: refuted globally, survives locally

HT's CENTRAL-RANK (`rank H^{ab} = r+1`, hence `r = j-1`) is a theorem about a
**central** extension `1 -> Z_H -> H -> Delta -> 1`, and the centre is
`Z(G_{p,q})`. In (B3) `G` is not `G_{p,q}` and has no such centre: `A_F` is not
a cone, `C^2 \ A_F` does not retract to a Seifert-fibred `S^3`-complement, and
there is no candidate `Z`. So:

```text
CENTRAL-RANK, global form:  REFUTED for (B3) (hypothesis absent, not merely
                            unverified).  It must not be quoted at (B3).
```

What survives is the **per-orbit** statement inside the cusp's own local group,
and it acquires a geometric meaning that case (A) did not display:

> **LEMMA B3-LOC.** Let `p_0` be the cusp, `Loc_{p_0} ≅ G_{p,q}`, and let
> `O` be an orbit of `rho(Loc_{p_0})` on the `N` sheets, `H_O` the point
> stabiliser in `G_{p,q}`, `Delta_O := H_O Z/Z <= Z/p * Z/q` of index `M_O`
> with Kurosh free rank `r_O`. Then `rank H_O^{ab} = r_O + 1`, and
> ```text
>   r_O + 1 = rank H_1(U_O),   U_O := the connected component of
>             F^{-1}(B_{p_0} \ A_F) indexed by O.
> ```
> Moreover **if `O` is one of the `a_{p_0}` affine orbits** (`|O| = 1`, `F` a
> local biholomorphism there), `U_O = B_y \ E` for the corresponding
> `y ∈ F^{-1}(p_0)`, so
> ```text
>   r_O + 1 = # local branches of E at y  = # local branches of A_F at p_0 = 1,
> ```
> hence `r_O = 0` at every affine orbit over a unibranch point.
>
> *Proof.* The first sentence is HT CENTRAL-RANK applied to `H_O <= G_{p,q}`
> (its proof uses only `H_2(Delta_O) = 0` and `Z_H ≅ Z`, both intact). For the
> second: orbits of `rho(Loc_{p_0})` correspond to connected components of
> `F^{-1}(B_{p_0}\A_F)`, and `H_O^{ab} = H_1(U_O)`. For the third: a Keller map
> is étale, so `F` is a local biholomorphism at every `y`, `(E,y) ≅ (A_F,p_0)`
> analytically, and `H_1(B_y \ E) = Z^{#branches}` (link of a plane germ with
> `r` branches is an `r`-component link). ∎

The last clause is the (B3) replacement for `j`: in case (A) `r = j-1` reads
off the **global** component count; in (B3) the same algebra reads off a
**local branch count**, which is pinned by MI's profile data.

### 2.4 THEOREM B3-CAGE — ORBIFOLD-CAGE, orbit-summed

> **THEOREM B3-CAGE.** At a quasi-homogeneous cusp `p_0` of type `(p,q)`, put
> `A := rho(alpha)`, `B := rho(beta)` (images of the two `G_{p,q}` generators
> under `rho ∘ iota`), `c_A := #cycles(A)`, `c_B := #cycles(B)` on the `N`
> sheets. Let the orbits of `<A,B>` be `O_1,...,O_T`, `kappa_i` the order of
> `rho(z)|_{O_i}` and `M_i = |O_i|/kappa_i`, `M_tot := sum_i M_i`. Then
> ```text
>   (B3-1)   c_A + c_B  =  M_tot + T - R_tot ,     R_tot := sum_i r_{O_i} ;
>   (B3-2)   T = # F^{-1}(p_0) ∪ {infinity pieces} = # parts of the fibre
>            partition over p_0, with part sizes |O_i| ;
>   (B3-3)   r_{O_i} = 0 for each of the a_{p_0} affine orbits (LEMMA B3-LOC),
>            so  c_A + c_B <= M_tot + T,  with the defect carried entirely by
>            the pieces at infinity ;
>   (B3-4)   the nontrivial cone orders {p/m > 1} ∪ {q/l > 1} attached to one
>            orbit are pairwise coprime, and coprime to that orbit's kappa_i.
> ```
> *Proof.* `rho(z)` is central in `<A,B>`, hence semiregular on each orbit, so
> `O_i` splits into `M_i` blocks and `Z/p * Z/q` acts on the block set `𝔅`,
> `|𝔅| = M_tot`, giving a degree-`M_tot` (possibly disconnected) orbifold cover
> of `D^2(p,q)`. Multiplicativity of `chi^{orb}`,
> `sum_c (2-2g_c-c_c) - S - S' = -M_tot` with `S,S'` the numbers of preimages of
> the two cone points, plus `S = c_A`, `S' = c_B` (HT (C-4), whose proof is
> per-orbit and needs no transitivity), plus `2g_c + c_c = r_{O_c}+1`, give
> (B3-1). (B3-2) is the orbit/component correspondence; (B3-3) is LEMMA B3-LOC;
> (B3-4) is HT (C-2)-(C-3) applied orbitwise. ∎

At `T = 1` this is HT's `s+s' = M+2-j` verbatim. The generalisation is exactly
what (B3) needs, because the cusp's local monodromy in (B3) is never
transitive: some sheets survive affinely and some are lost at infinity.

### 2.5 THEOREM B3-PUSHOFF and THEOREM B3-COMPONENT

`(B3)` needs one object case (A) never had: the covering of the curve itself.
Let `A_F°` be the smooth locus of `A_F` pulled back to the normalisation
`A_F~ ≅ A^1` (MI Lemma A), i.e. `A^1` minus one puncture per branch at each
singular point. `F` étale makes

```text
(2.5.1)   E° := F^{-1}(A_F°)  -->  A_F°     an a-sheeted covering,
```

`a = a_p` at every smooth `p` (MI control 2). Its monodromy is not `rho`, but
it is computed by `rho`:

> **THEOREM B3-PUSHOFF.** For a loop `gamma` in `A_F°` let `gamma~` be its
> push-off into `C^2 \ A_F`. Then `rho(gamma~)` centralises `rho(m_gamma)` and
> acts on `Fix rho(m_gamma)` — the `a` sheets — as the monodromy of (2.5.1).
> At the puncture attached to a branch `b` at a singular point `P`,
> ```text
>   gamma~  =  z_b · prod_{b' != b} g_{b'}^{(b · b')_P}     in  pi_1(B_P \ A_F),
> ```
> `z_b = 1` for a **smooth** branch `b`. In particular:
> * at a double point of two smooth branches with contact `t`,
>   `gamma~ = g_{other}^t`;
> * at a unibranch point, `rho(gamma~)` lies in the centre of
>   `rho(Loc_P)`.
>
> *Proof.* The first sentence is the standard identification of the fibre of
> (2.5.1) over `p` with `Fix rho(m_p)`. For a smooth branch `b`, `gamma` bounds
> a disc **inside** `b`; pushing that disc off normally gives a disc meeting
> `A_F` exactly in the other branches, with multiplicity `(b·b')_P` each, and
> `lk(gamma~, b) = 0`; so `gamma~` is the stated product. For a unibranch
> singular branch, `rho(gamma~)` commutes with the images of all local
> meridians, which generate `rho(Loc_P)`. ∎

> **THEOREM B3-COMPONENT.** `j := #`components of `E` equals the number of
> orbits of the groupoid generated by (i) the monodromy of (2.5.1) on the `a`
> sheets and (ii) for each `y ∈ E` lying over a singular point `P`, the
> identification of the `r_P` branch-sheets at `y`.
>
> *Proof.* `E = E° ∪ (E ∩ F^{-1}(Sing A_F))`. Removing a point from an
> irreducible curve keeps it connected, so components of `E` and of `E°` agree
> except for the merges induced by the points `y`, at which `E` has `r_P`
> branches (`F` étale), one per branch of `A_F` at `P`. ∎

`j` is exactly `rank H^{ab}` (LEMMA F1), i.e. the quantity that carried the
whole case-(A) argument. B3-COMPONENT computes it without any centre.

## 3. Task (2): the cage on the (B3) profile

### 3.1 `N = 4`: the representation is pinned

N4-PIN (MI §8.1) gives `a=2`, `W=2`, one dicritical `(1,2)`, generic meridian
cycle type `(2,1,1)`, fibre partition `(3,1)` at the cusp `p_0` with
`a_{p_0}=1`, and `(2,2)` at each double point with `a_q = 0`. Then:

> **PROPOSITION 3.1.** `rho(G) = S_4`; `rho(Loc_{p_0}) ≅ S_3` acting on the
> 3-element orbit and fixing the sheet `y_0` over the cusp; at each double
> point `rho(g_1), rho(g_2)` are **disjoint** transpositions.
>
> *Proof.* `A_F` irreducible makes all meridians conjugate, so `rho(G)` is
> generated by the transpositions conjugate to `rho(m)`; a transitive subgroup
> of `S_4` generated by transpositions is `S_4`. At `p_0` the orbits are
> `(3,1)`, so every element of `rho(Loc_{p_0})` preserves both, so the
> generating transpositions lie inside the 3-set; transitive there, hence
> `S_3`. At a double point the two generators are commuting transpositions;
> equal ones give orbits `(2,1,1)`, disjoint ones give `(2,2)`. For contact
> `t >= 2` the alternative "sharing a letter" forces `3|t` and orbits `(3,1)`;
> `(2,2)` excludes it. ∎

`|rho(G)| = 24 > 4`, so MI COR 7.2 (non-regularity) is **satisfied, not
violated**: it kills nothing at `N = 4` in (B3).

> **PROPOSITION 3.2 (the cusp type at `N = 4`).** The Puiseux pair of the (B3)
> cusp satisfies
> ```text
>        (2 | p  and  3 | q)      or      (3 | p  and  2 | q).
> ```
> *Proof.* `rho(z)` is central in `rho(Loc_{p_0}) = S_3`, which has trivial
> centre, so `rho(z) = e`; hence `ord(A) | p`, `ord(B) | q`, coprime, with
> `<A,B> = S_3`. Two elements of coprime orders generating `S_3` must have
> orders `2` and `3` (neither can be trivial, `S_3` being non-cyclic). ∎
>
> *Independent parity check.* `deg z = pq` and `rho(z)=e` is even, so
> THEOREM B3-DEGREE gives `eps^{pq} = +1` with `eps = (-1)^{W - sum s_l} =
> (-1)^{2-1} = -1`, i.e. **`pq` even** — the weaker half of Prop 3.2, obtained
> from the parity law alone. The two routes agree.

This kills, for instance, `(p,q) = (2,5), (3,5), (4,5), (5,6), (5,7)` and
every pair with `3 ∤ pq`; it admits `(2,3)`, `(3,4)`, `(2,9)`, `(4,3)`,
`(8,3)`, `(2,15)`, `(4,9)`, ... It is a **necessary numerical gate**, in the
Path-1 discipline sense: no realisation of any admitted pair is claimed.

**B3-CAGE, checked on the admitted cell.** With `A` a transposition and `B` a
3-cycle in `S_{\{1,2,3\}}`: `c_A = 3`, `c_B = 2`, `kappa_i = 1`, `M_tot = 4`,
`T = 2`. (B3-1) gives `R_tot = 4 + 2 - 5 = 1`, and (B3-3) gives `r = 0` at the
affine orbit `{y_0}`, so the size-3 orbit at infinity has `r = 1`, i.e.
`H_1(U) = Z^2`. Independent orbifold count: the degree-3 cover of `D^2(p,q)`
with `A`-cycles `(2,1)` and `B`-cycle `(3)` has
`chi^{orb} = chi(Sigma) - 3 + 3/p + 3/q = 3(1/p+1/q-1)`, so `chi(Sigma) = 0`,
`Sigma` = annulus, `r = 2g+c-1 = 1`. **Agrees.**

### 3.2 `N = 4`: `E` is determined completely

Apply B3-PUSHOFF at each puncture of `A_F~ = A^1`. The punctures are `P_0`
(one, over the unibranch cusp) and `P_i^{+-}` (two per double point `q_i`,
contact `t_i`), plus the one place at infinity (MI Lemma A). `a = 2`, so the
monodromy of (2.5.1) is a homomorphism `pi_1(A_F°) = F_{2k+1} -> Z/2`, i.e. a
sign `eps_P ∈ {0,1}` per puncture.

```text
 at P_0 :          rho(gamma~) ∈ Z(rho(Loc_{p_0})) = Z(S_3) = 1   ==>  eps = 0.
                   [second, independent proof: a_{p_0}=1 and F etale give one
                    degree-1 piece at y_0 plus one more degree-1 piece, so the
                    two sheets do not exchange.]
 at P_i^{+-} :     rho(gamma~) = rho(g_other)^{t_i} = (34)^{t_i} on
                   Fix rho(g_self) = {3,4}      ==>  eps = t_i mod 2.
 at infinity :     eps_infty = sum of the others  =  0   (2k_odd is even),
```

writing `k_odd := #{i : t_i odd}` (every genuine node has `t_i = 1`). Hence
the branch locus of the degree-2 cover `bar E -> P^1` is exactly the `2k_odd`
punctures `P_i^{+-}` with `t_i` odd, and Riemann-Hurwitz gives:

> **THEOREM B3-N4.** At `N = 4` under `H2` in case (B3):
> ```text
>   k_odd >= 1 :  j = 1.  E is IRREDUCIBLE, of geometric genus k_odd - 1,
>                 with 3 + 4k - 2 k_odd places at infinity, exactly one
>                 singular point y_0 (analytically ≅ the cusp of A_F), smooth
>                 elsewhere;  H^{ab} = Z.
>   k_odd  = 0 :  j = 2.  E = E_1 ⊔ E_2, both RATIONAL, one carrying y_0,
>                 with n_1 + n_2 = 3 + 4k places at infinity;  H^{ab} = Z^2.
> ```
> *Control.* `chi_c(E) = sum_i (2 - 2g_i - n_i)` equals `1 - 4k` in both
> branches, reproducing N4-PIN's `chi_c(F^{-1}(A_F)) = 1 - 4k` exactly. That
> number was derived in MI from Theorem (E); here it comes out of the covering
> combinatorics, which is an independent route.

Note `j = 1 <= a = 2`: MI's `j <= a` holds, and in the node case it is strict.

### 3.3 What is **not** killed — reported as found

`j = 1` is the case-(A) death sentence (MI CUSP-KILL). **It is not one here.**
CUSP-KILL's mechanism is: `j=1` ⟹ `E` homeomorphic to `C` ⟹ Lin-Zaidenberg ⟹
`H ≅ G_{p,q}` ⟹ `M = 1` ⟹ `H ◁ G` ⟹ Galois ⟹ Campbell. In (B3) with
`k_odd >= 1`, `E` has genus `k_odd-1` and `3+4k-2k_odd >= 5` places at
infinity, while `A_F` has genus `0` and one place: `E` is **not** homeomorphic
to `A_F`, the first implication fails, and nothing downstream runs. I looked
for a replacement and found none:

* `H^{ab} = Z = G^{ab}`, and the inclusion `H^{ab} -> G^{ab}` is an
  isomorphism (some conjugate of `m` fixes sheet 1, so `H` surjects onto
  `G^{ab}`); transfer then only reproduces `x |-> 4x`. No contradiction.
* `chi(C^2\E) = 4k = 4 · chi(C^2\A_F)`: the degree-4 identity, vacuous.
* The `delta`-budget `delta(p,q) + sum_i t_i + delta_infty = (n-1)(n-2)/2`
  with `n = deg bar A_F` is a budget, not a bound, because
  `OPEN[DEG-AF-VS-N]` (MI §9) is open.

```text
VERDICT (2) at N = 4:  case (B3) is NOT EMPTY under the merged cage.  What the
cage delivers is an exact survivor characterisation: Prop 3.1, Prop 3.2 and
THEOREM B3-N4.  No EMPTY window in N is claimed, and none was found.
```

### 3.4 General `N`

At general `N` the same three theorems apply verbatim, with `a`, `W`, the
`mu_l`, and the fibre partitions taken from MI `(L)`, `(K)`, `[P3]`, 7.B. The
usable all-degree gate is:

```text
 (G1)  sgn rho(h) = eps^{deg h} for every h ∈ G,   eps = (-1)^{W - sum_l s_l}
       (THEOREM B3-DEGREE).  At a (p,q) cusp:  eps^{pq} = sgn rho(z).
 (G2)  c_A + c_B = M_tot + T - R_tot  at each cusp, with R = 0 on all a_{p_0}
       affine orbits, hence  c_A + c_B <= M_tot + T  (THEOREM B3-CAGE).
 (G3)  T = #parts of the fibre partition over the cusp, part sizes = |O_i|,
       a_{p_0} = #parts of size 1, and  N - a_{p_0} = r_{p_0} W + K_{p_0}.
 (G4)  j = orbit count of the (2.5.1)-monodromy glued by the branch merges
       (THEOREM B3-COMPONENT), with puncture data from B3-PUSHOFF.
```

Two honest limits. First, (G2) is an inequality at general `N` because
`r_{O}` at an infinity orbit is a local invariant this pass does not pin (in
the `N=4` cell it came out of the equation, not out of a theorem). Second,
`(B3)` at general `N` may carry several cusps and several multibranch points;
MI's `N=4` sharpness ("exactly one singular-branch point") is explicitly a
small-degree phenomenon and I do not extend it. Consequently **no EMPTY window
in `N` follows from (G1)-(G4) at this pass**, and I do not manufacture one.

## 4. Task (3): the A2 `3x3` determinant at `e >= 1`

### 4.1 Set-up and the monomial calculus

C32 §6 states the successor exactly: form the general-`e` analogues of
`(E3top)`, `(E1top)`, `(K1top)` and test the `3x3` determinant chamber by
chamber. I do that, with one methodological change that makes it a finite desk
computation: **leading coefficients are extracted by monomial substitution**

```text
   eta = A Z^e ,  s = S Z^sigma ,  q = Q Z^m ,  r = R Z^n ,  G = C Z^g ,
```

which computes the coefficient of the top power of every expression built from
`Z`, these five, and `d/dZ` — exactly the Euler-eigenvalue rule C32 uses by
hand. Every place where a leader could vanish is branched explicitly (§4.3,
§4.4); no nominal degree is reported as exact.

The three equations are C32's own displays, consumed at their typing
(PROVED-HERE/UNREVIEWED there):

```text
 EQ3 :  eta Z^2 Xi - (3a/b) (Z eta^2 G^2)'      = 0     [C32 T2, sec.3]
 EQ1 :  6 D1 r' - 4q'E1 + 2qE1' + 4C1 s' - 2C1's + 2 kappa Z = 0   [C32 (1.1)]
 EQ2 :  E2eq|_{G=0} + Delta_2                   = 0     [C32 sec.6 displays]
 EQ4 :  2(sC1 - qE1)r' + kappa E1 + q s s' - q' s^2 = 0  [C32 (2.2), from O0+E0]
```

with `C1 = d[psi s + Phi/(2b)]`, `Phi = sG/eta` (C32 T1), `d = 3a/(2b)`.

### 4.2 Controls

All four `e=0` specialisations were rebuilt independently from C32 §5.1 and
subtracted:

```text
   Xi  - 4I                     |_{e=0}   =  0
   EQ1 - 2*E1d                  |_{e=0}   =  0
   EQ2 -   E2d                  |_{e=0}   =  0
   EQ3 - 2A*(2Z^2 I - t(ZG^2)') |_{e=0}   =  0
```

Four identities, four zeros. In particular C32's §6 displays of `E2eq|_{G=0}`
and `Delta_2` are **verified** against its §5.1 `E2d`, not merely quoted.

### 4.3 The `u`-grading and the three chambers

Every family in all four equations has exponent `u + (per-equation offset)`,
with

```text
 u_r = n+e ,  u_q = m ,  u_s = 2sigma-e ,  u_eta = 3e-1 ,  u_G = e+g-1 ,
 u_T = 2g-e-1 ,        U := max(u_r,u_q,u_s) over the present families.
```

`u_eta - u_T = 2(2e-g)` and `u_G - u_T = 2e-g`, so `g` against `2e` is the
whole chamber trichotomy, as C32 §6 says. `EQ1` and `EQ2` each carry a
`eta`-type and a `G`-type copy of each of `r,q,s`, at offsets differing by
`g-2e`; so the `eta`-type dominates in Chamber III, the `G`-type in Chamber I,
and in Chamber II they coincide and **add**, with weight

```text
        c := G_{2e} / (b eta_e^2)      (Wall A is c = -(2/3)(1+3e),
                                        Wall B is c = -(1+2e)).
```

`EQ2`'s own `G`-family carries the factor `(2e-g)` and therefore **vanishes
identically in Chamber II** — checked, and the reason the Chamber II rows are
clean. In the simultaneous-top regime `u_r = u_q = u_s = U` one has
`m = U`, `n = U-e`, `2sigma = U+e`, and with `x := a eta_e^3 r_n n`,
`y := b eta_e^2 q_m`, `w := a eta_e s_sigma^2 / b` the three rows are

```text
 EQ3 :  [ 12 ,  8(e-m) ,  -6(e-sigma) ]
 EQ1 :  [ 6(3e+1) ,  4(2e+1)(e-m) ,  -3(e+1)(e-sigma) ]  (+ c * [9, 2(g-2m), (3/2)(e-g+sigma)])
 EQ2 :  [ 6(4e+3) ,  2(8e^2-4em+6e-6m+1) ,  -3(2e^2+2e-3sigma) ]
                                            (+ c * [12, 4(g-m), (3/2)(2e-2g+1)])
```

and the determinants are

```text
  Chamber III (g < 2e) :  det =  72 e n (2e+1)
  Chamber I   (g > 2e) :  det =  36 (U + g - 3e)
  Chamber II  (g = 2e) :  det =  36 n (c + 2e)(c + 2e + 1)
```

By C32 T5 the whole `r'=0` section is already reduced to a Chamber II wall, so
`r' != 0`, `n >= 1`, and `e >= 1` throughout.

**Chamber III is EMPTY.** `det = 72en(2e+1) != 0`. The three pair-minors from
row `EQ3` are `-48e(e-U)`, `36e(e-U)`, `12e(e-U)^2`, all nonzero; the three
`EQ3` entries `12, 8(e-U), -3(e-U)` are nonzero, so singles die too. If
`U < 3e-1` the top of `EQ3` is the lone `eta`-family `12abA^6e^2(2e-1) != 0`:
contradiction. The residue `U = 3e-1` cannot be reached by the `s`-family
(`2sigma = 4e-1` is odd — C32's parity separation, re-derived), and the
remaining `{r,q}` system has `2x2` determinant `12(20e^3-4e^2+5e+1) != 0`,
forcing `x=y=0` against the nonzero `eta`-family. Singles at `U=3e-1` die on
`6(3e+1)` resp. `4(2e+1)(1-2e)`.

**Chamber I is EMPTY.** In the regime `U >= 2g-e` one has
`U+g-3e >= 3g-4e > 0` since `g >= 2e+1`; all pair-minors are nonzero by the
same margin. `U < u_T` leaves the lone target family
`-3aA^2C^2(2e+2g+1)/b != 0`: contradiction. At `U = u_T` the `s`-family is
again excluded by parity (`2sigma = 2g-1`), and the `{r,q}` determinant is
`12(3g-e-1) != 0`, killing it against the nonzero target.

### 4.4 Chamber II: the walls, and what survives

Off the two walls the determinant is nonzero and Chamber II is empty. On them:

* **`c = -2e`.** Rows `EQ3` and `EQ1` become **proportional** (`EQ1 = (1/2)EQ3`
  as rows), the system has rank 2, and its solution ray is
  `(x,y,w) = (-nw/4, 0, w)` — i.e. `y = 0`, i.e. `q_m = 0`, contradicting the
  hypothesis that the `q`-family is at the top. `EQ4` on that ray gives
  `-3nw^2/4 = 0` as well. The `{r,s}` pair (the one configuration whose minors
  all vanish here) is killed by `EQ4`, whose top is then
  `(3/2)(c+2e+2)xw = 3xw = 0`. All leaders are alive at this wall: at
  `c=-2e` the leaders of `E1, D1, C1` equal `b eta_e^2`, `a eta_e^3`,
  `d eta_e s_sigma` — the `G` term exactly neutralises the Euler weight of
  `eta` in all three at once. **EMPTY.**
* **`c = -(2e+1)` — C32's Wall B.** Here `E1`'s leader vanishes
  (`deg E1 <= 2e-1`), so the `E1`-carrying families of `EQ1` and `EQ4` drop one
  degree; `EQ2` and `EQ3` are unaffected (they are written in
  `eta,q,r,s,G,Phi` only). The valid rows are
  `EQ3 = [12,-8n,3n]`, `EQ1 = [-3,0,3n/4]`, `EQ2 = [6, 2-4e-8n, 3e+9n/2-3/2]`,
  of rank 2, with ray
  ```text
        (x, y, w)  =  (n/4, 3/4, 1) * w ,
  ```
  on which `EQ2` is satisfied identically and `EQ4`'s surviving top
  `(3/2)xw - (n/2)yw = 0` is satisfied identically. **SURVIVES.**
* `U = 3e-1` in Chamber II: `EQ4`'s top is `-2(2e+1+c)xy`, forcing Wall B; and
  at Wall B `EQ1`'s row is `[-3, 0]`, giving `x=0`, contradiction. The
  `q`-only and `r`-only sub-branches die on `4(1-2e)(c+2e+1)` /
  `-10(2e-1)` and on `3(6e+2+3c)` / `10`. **EMPTY.**
* `U < 3e-1` in Chamber II: the three coincident `EQ3` families must cancel,
  `P(c) := 4e^2(2e-1) + 4ce(2e-1) - c^2(6e+1) = 0`. `EQ1, EQ2` then give a
  one-dimensional ray and `EQ4` a quadratic on it; eliminating `c` between
  that quadratic and `P` gives
  ```text
   Res_c = -576 n^2 (32e^3+32e^2+6e+1) * F(e,n),   F quadratic in n,
   leading coeff  A(e) = 1024 e^6 (2e-1)(16e^2-8e-1)(18e^3+24e^2+6e+1) > 0,
   disc_n(F) = (2^6 e^3 K(e))^2 * [ 2e(2e-1) ],  K having no integer root.
  ```
  `2e(2e-1)` is **never** a perfect square for `e >= 1`: `gcd(2e,2e-1)=1`
  would force both factors square, `2e = s^2` gives `e = 2u^2` and then
  `2e-1 = (2u-1)(2u+1)` needs two coprime squares differing by `2`, impossible.
  So `disc_n(F)` is never a perfect square, `F` has no rational root in `n`,
  `Res_c != 0` at every cell, and `P(c)=0` is incompatible with the ray.
  The pair and single sub-branches, and the ray-solvability denominator, were
  tested the same way (`Res_c` against `P`, no common cell for `e <= 199`).
  **EMPTY** (the `F != 0` step is proved, not measured; the pair sweep is
  measured over `e <= 199`).

Collecting, and adding C32 T5 (which sends `r'=0` to the very same wall):

> **THEOREM HORN-A2.** On the live section (`G != 0`, `s != 0`, `a b kappa != 0`,
> `eta != 0`) with `e = deg eta >= 1`, every surviving pair satisfies
> ```text
>       g = 2e     and     G_{2e} = -b (1 + 2e) eta_e^2 ,
> ```
> equivalently `deg E1 <= 2e - 1`. Off that wall the section is EMPTY. On it,
> in the simultaneous-top regime `U >= 3e`, the three top coefficients are
> pinned to the ray
> ```text
>    r_n = s_sigma^2 / (4 b eta_e^2) ,   q_m = 3a s_sigma^2 / (4 b^2 eta_e) ,
>    with   m = U ,  n = U - e ,  2 sigma = U + e ,  U >= 3e .
> ```

That is a genuinely stronger outcome than the charge's fallback: not "an
infinite determinant-zero wall" in a free parameter, but **one wall, named by
an equation already in the record, on which the leading data is rigid**.

```text
TYPING.  The horn's live section does NOT close.  OPEN[A2-CELL-32] survives,
narrowed to  OPEN[A2-CELL-32-E1WALL] :  g = 2e, deg E1 <= 2e-1, r' != 0,
U >= 3e, leaders on the ray above.  Chambers I and III, and every Chamber II
branch off the E1-wall, are EMPTY.  The next lever is the pair (O0, O1),
which this pass did not consume (only their consequence (2.2) was used).
```

## 5. Task (4): composition, per degree window

`(1)`-`(2)` and `(3)` are **different instruments on different objects**: the
first two constrain the ACS-1 monodromy of a (B3) profile; the third
constrains an explicit pullback normal form at one cell of the horn's
`A`-degree-2 census. They do not compose into a kill, and I do not claim one.

```text
 N <= 3   EMPTY.                                          [MI]
 N = 4    (0) EMPTY  [SMOOTH-KILL].  (A) EMPTY  [HT CUSP-A-EMPTY, HR CONFIRMED].
          (B1) EMPTY [NODAL-ALL-N].  (B2) EMPTY [MI sec.6].
          (B3) SURVIVES.  Newly pinned here: rho(G) = S_4 (Prop 3.1);
               (2|p,3|q) or (3|p,2|q) (Prop 3.2);  E irreducible of genus
               k_odd-1 with one cusp, or two rational components when every
               double point has even contact (THEOREM B3-N4).
               NOT EMPTY.  This is the whole N=4 H2 residual.
 5..7     (A) EMPTY [HT: proved N<=6, measured N=7].  (B2) beta>=2.  (B3) open.
 N = 8    (A) NONEMPTY, HT's 192-cell group-theoretic residual (not realised).
 8..10    (A) as above.  (B2) beta >= 2.  (B3) open, cage (G1)-(G4) only.
 11..16   (A).  (B2) beta >= 1.  (B3) open.
 N >= 17  the above, plus (B1) with data solving MI (5.4).
```

**What would compose.** Three named items, in order of cheapness:

1. `OPEN[DEG-AF-VS-N]` (MI §9). A bound `deg bar A_F <= f(N)` turns the
   `delta`-budget `delta(p,q) + sum_i t_i + delta_infty = (n-1)(n-2)/2` into a
   bound on `k` and on the Puiseux pair, and Prop 3.2 then leaves a finite
   list at `N = 4`. This is the single highest-value successor for (B3).
2. A `(B3)` analogue of CUSP-KILL for `j = 1`. THEOREM B3-N4 hands it the exact
   object to work on: an irreducible affine `E` of genus `k_odd-1` with one
   quasi-homogeneous cusp and `3+4k-2k_odd` places at infinity, index 4 and
   non-normal in `G`. Case (A)'s route through Lin-Zaidenberg is unavailable;
   a route through the ends is not.
3. `(O0, O1)` on the A2 `E1`-wall. THEOREM HORN-A2 reduces
   `OBSTRUCTION[A-DEGREE-TWO]` to one wall with rigid leaders; two unconsumed
   equations remain, and the `y : w = 3 : 4` pin is exactly the kind of datum
   a subleading pass can contradict.

Not composed, and not claimed: any kill of `(9,6,2)`; any all-degree closure;
existence of `F`; any statement about MPRIME case (A) at `N >= 8`; any
promotion of the `N=8` survivors to geometry.

## 6. FALLACY-v2 audit

* **Flag/place/series.** Four groups kept apart throughout: `Loc_{p_0}`,
  `Loc_{q_i}`, `G = pi_1(C^2\A_F)`, `G_{p,q}`. The identification HT makes in
  case (A) (`G ≅ G_{p,q}`) is **not** made here; §2.1 records that it is false
  in (B3) and §2.3 refutes the global CENTRAL-RANK rather than transporting it.
  `iota : Loc_{p_0} -> G` is never crossed in the direction NO-PUSHFORWARD
  forbids.
* **Carrier/attainment.** Prop 3.1, Prop 3.2, THEOREM B3-N4 are `REPRESENTATIVE`
  necessary conditions on a hypothetical counterexample; none asserts that any
  admitted `(p,q)` or any `k` is realised by a Keller map. The A2 residual ray
  is a pin on leaders, not a witness.
* **Floor/attainment.** `c_A + c_B <= M_tot + T` is stated as an inequality
  because `r` at the infinity orbits is not pinned in general; the `N=4`
  equality `R_tot = 1` is derived, then independently confirmed by an orbifold
  Euler characteristic count.
* **Per-ray / exit-set.** No exit price asserted; no `charge_basis` line.
* **Raw remainder degree / vanished leaders.** Every chamber branch on a
  vanishing leader is explicit: Wall A, Wall B, `c = -2e`, `c = -(2e+2)`,
  `c = -(6e+2)/3`, `sigma = e`, `m = e`, `n = 0`, and the two parity
  exclusions `2sigma = 4e-1`, `2sigma = 2g-1`. At Wall B the invalidity of the
  `E1`-carrying expansions is stated and the rows recomputed, not reused.
* **Prime label/derivative.** In §2-§3 primes are labels (`P_i^{+-}`,
  `s'` never appears); in §4 every prime is `d/dZ`, per C32's convention. The
  two never mix: §4 uses no `+-` labels.
* **Variable/ring map.** The monomial substitution is declared in §4.1 with its
  generator order and coefficient field, and validated by four independent
  `e=0` identities before use.
* **`sat()` / pole / interior.** Not in play; no ideal, no Groebner, no pole.
* **Not filled by cap or analogy.** Where the charge's presentation claim is
  wrong I say so and derive the replacement; where quasi-homogeneity is assumed
  rather than banked I type `SCOPE[B3-QH]`; where no EMPTY window exists I say
  none was found rather than manufacturing one; where the A2 wall survives I
  type it rather than declaring closure.

## 7. Typed verdict block

```text
LANE              HORN-FLAGSHIP
SCOPE             Keller, noninvertible, H2, case (B3); cusp quasi-homogeneous
                  (SCOPE[B3-QH], charged assumption, not banked from MI).

PROVED HERE       B3-DEGREE     sgn rho(h) = eps^{deg h} for every h ∈ G.
                                (CUSP-PARITY, hypothesis-free form.)
                  B3-LOC        r_O + 1 = rank H_1(U_O); = #branches of E at y
                                for affine orbits, hence 0 over a unibranch pt.
                  B3-CAGE       c_A + c_B = M_tot + T - R_tot at each cusp.
                                (ORBIFOLD-CAGE, orbit-summed.)
                  B3-PUSHOFF    gamma~ = z_b * prod g_{b'}^{(b.b')}; central at
                                a unibranch branch, g_other^t at a double point.
                  B3-COMPONENT  j from the (2.5.1)-monodromy plus branch merges.
                  Prop 3.1      rho(G) = S_4, rho(Loc_cusp) ≅ S_3 at N = 4.
                  Prop 3.2      (2|p,3|q) or (3|p,2|q) at N = 4.
                  B3-N4         E irreducible, genus k_odd-1, one cusp,
                                3+4k-2k_odd ends;  or j=2 with both components
                                rational when every contact is even.
                  HORN-A2       live section, e>=1  ==>  g=2e and
                                G_{2e} = -b(1+2e)eta_e^2 (deg E1 <= 2e-1);
                                Chambers I and III EMPTY; leaders on a ray.
                  All PROVED-HERE, UNREVIEWED.

REFUTED HERE      the charged (B3) presentation "G_{p,q} + k commuting squares".
                  CENTRAL-RANK in its GLOBAL form at (B3) (no centre exists).

CONSUMED          HT: LEMMA F1, NO-PUSHFORWARD, CENTRAL-RANK, ORBIFOLD-CAGE
                  (C-2)/(C-4), CUSP-A-EMPTY  -- at their typing (HR CONFIRMED).
                  MI: Lemma A, (L), (K), [P3], 7.B, THEOREM PROFILE, N4-PIN,
                  COR 7.2, SMOOTH-KILL, NODAL-ALL-N  -- PROVED-HERE/UNREVIEWED.
                  C32: T1, T2 (Xi), (1.1), sec.6 E2eq/Delta_2 displays, (2.2),
                  T5  -- verified at e=0 here before use.

MEASURED          four e=0 identities, all differences exactly 0.
                  chamber determinants and all pair/single minors, symbolic.
                  Chamber II U<3e-1: Res_c cofactor has no integer root
                  (PROVED via the 2e(2e-1) non-square lemma); pair sweep
                  e <= 199 zero hits; resultant scan e <= 400 zero hits.

NOT CLAIMED       any EMPTY window in N for (B3);  any kill of (9,6,2)/(9,6,4);
                  closure of OPEN[A2-CELL-32];  closure of the H2 branch;
                  realisability of any admitted (p,q) or k;  anything about
                  MPRIME case (A) at N >= 8;  a general-unibranch version of
                  Sec 2.4.

OPENS RAISED      OPEN[A2-CELL-32-E1WALL]   g=2e, deg E1 <= 2e-1, U >= 3e,
                                            leaders on the stated ray.
                  OPEN[B3-J1-KILL]          a (B3) analogue of CUSP-KILL for
                                            the irreducible E of B3-N4.
                  OPEN[B3-INFINITY-RANK]    pin r_O at the infinity orbits, to
                                            turn (G2) from <= into =.
                  OPEN[B3-QH]               is the (B3) cusp quasi-homogeneous?
                                            Assumed by charge, not banked.
                  (MI's OPEN[DEG-AF-VS-N] is re-flagged as the highest-value
                   successor for (B3); it is MI's, not raised here.)

DEVIATIONS        (1) Sec 2 replaces the charge's presentation claim rather than
                      deriving it; the claim is false and the correction is the
                      deliverable.  This is the main judgement call here.
                  (2) Task (3) exceeded its charge: the charge anticipated an
                      infinite wall and permitted stopping; two of three
                      chambers instead terminate, and the residual is one named
                      wall.  EQ4 = C32 (2.2) was used, which C32 sec.6 did not
                      list among the three rows.
                  (3) Drivers left in /tmp/hornflag, not installed in box/.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `38766`.
- Body SHA-256:
  `52ede8771f325249ca05491db374d88a52ea8a59ecd4935b4790e9307134bf73`.
- Frozen basis: `9d491006c412f47260b5ac25c3b65656ceec390b`.
