# Hostile review — `(8,12)` order-four quotient toric genus/RH gate

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order4-quotient-toric-genus-rh-theorem-20260826.md` |
| Target SHA-256 | `7f107c5e422177aac4387bd42e23e4c833592106406a36a01fe89a4ccd555e41` |
| Charged parent (V2 client) | `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md` |
| V2-client SHA-256 | `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621` |
| Charged parent (V2 delta review) | `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-v2-20260825.md` |
| V2-review SHA-256 | `252bbd07d29084952453b45546cff7e0d8ddda7a72576311d1f982ee01a66200` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim. The plane, birationality, irreducibility, and nondegeneracy gates of §1 remain uncertified; they are hypotheses, not outputs |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. The V2 review header token is not evidence. Charged parents were opened to recompute hashes and to read the definition of `C_4`, the weights `(3.1)`, and the deck/residual action as *statements*; no live AWS output, modular plane relation, or existing `CONFIRMED`/`REPAIR` string is an input to a genus, ramification, or elimination identity |
| Method | source reading and hand derivation only; SHA-256 of the target and of both named Section 0 artifacts; no CAS, solver, substantive exact Python, Sage, Singular, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named target and both charged parents uncommitted) |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `7f107c5e422177aac4387bd42e23e4c833592106406a36a01fe89a4ccd555e41`, matching the launch pin. Independently recomputed SHA-256 of the V2 client is `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621`, matching Section 0. Independently recomputed SHA-256 of the V2 delta review is `252bbd07d29084952453b45546cff7e0d8ddda7a72576311d1f982ee01a66200`, matching Section 0. The target status banner, the phrase “hostile-confirmed”, the V2 overall token, and every charged `CONFIRMED`/`REPAIR` string were not used as evidence. No live AWS endpoint and no modular plane polynomial were opened. No file other than this review was written.

---

## Verdict

The note is a correct conditional producer theorem. Independently: the four exact-plane hypotheses of §1 are the right strength for birationality, geometric irreducibility, a faithful residual `mu_16`, and passage from the affine `(s,t)` chart to the unique smooth complete models; the identifications `K^{mu_16}=L(q,v)` and `K^{mu_4}=L(q,y)` follow from the primitive character of `w=s/t` together with the explicit inverses in `(2.3)` and the lattice indices `16` and `4`, without an invariant-ring claim; the two quotients are distinct; all three Newton polygons, Euclidean areas, lattice perimeters, and interior-point counts recompute, and nondegeneracy of `P` transports under both monomial substitutions; both boundary tables list every zero and pole of the coordinate functions, including infinity, with the correct splitting numbers and inertia orders; the ramification totals are `24`, `40`, and `136`; all three Riemann–Hurwitz identities and the tower identity `40+4*24=136` hold; a source would give a nonconstant morphism `P^1_x\to Ytilde` (already `P^1_x\to Xtilde`) by properness and nonconstancy of `r_7^4` / `r_7^{16}`, which is impossible for `g=37` or `g=7`. The attacks by omitted boundary places, non-split unramified places, a kernel in the group action, a weighted-versus-ordinary mismatch, reducibility of `P(q,y^4)`, and substitution of affine genus all fail. No elimination of the leaf is claimed until the §1 gates are certified, and nothing in the note produces Taylor polynomiality or a Keller pair.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-quotient-toric-genus-rh-theorem-20260826.md` | `7f107c5e422177aac4387bd42e23e4c833592106406a36a01fe89a4ccd555e41` | target (matches required pin) |
| `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md` | `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621` | charged V2 coefficient client; matches target §0 |
| `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-v2-20260825.md` | `252bbd07d29084952453b45546cff7e0d8ddda7a72576311d1f982ee01a66200` | charged V2 delta review; matches target §0; unused as a verdict |

Both parent hashes match the strings printed in the target's Section 0. The V2 client is consumed only for the definition of the saturated chart `(0.3)`, the weighted action `(3.1)`, the residual `mu_16` and order-four deck as *statements*, the weight `19` of `r_7`, the nonvanishing `8\,dR_7/dx=j/u`, and the coefficient-infinity firewall. Its compiler contract and unrun geometry gate are not inputs. The V2 review is hashed and unused as a theorem.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field containing `mu_16`. Let `C_4` be an irreducible one-dimensional component of the saturated fibre

```text
(r_1,r_2,r_3,r_4-1,r_5,r_6):r_7^infinity,     r_7\neq 0
```

in `L[a_0,\ldots,a_6]`, and write `s=a_5`, `t=a_6`. Assume the four gates of the target's §1: the normalization `Ctilde` of a complete closure of `C_4` has function field `K=L(s,t)`; the unique irreducible relation of `s,t` is the Laurent equality `F(s,t)=P(s^2/t^3,t^8)=0`; `P(q,v)` is irreducible of Newton polygon

```text
Delta_X=conv{(0,0),(0,2),(1,3),(8,3)};
```

and `P` is nondegenerate with respect to every face of `Delta_X`, including the two-dimensional face.

The residual action `a_i\mapsto\lambda^{8-i}a_i` of `mu_16` restricts to `lambda(s,t)=(\lambda^3 s,\lambda^2 t)`. It is faithful on `K`. Putting `w=s/t`, `q=s^2/t^3`, `y=t^2`, `v=t^8`, one has the field equalities

```text
K^{mu_16}=L(q,v),          [K:L(q,v)]=16,
K^{mu_4}=L(q,y),           y^4=v,     [K:L(q,y)]=4,
```

with `mu_4\subset mu_16` the unique subgroup of order four (the source deck). The smooth complete quotients `Xtilde=Ctilde/mu_16` and `Ytilde=Ctilde/mu_4` are the normalizations of the ordinary projective closures of the irreducible plane curves `P(q,v)=0` and `P(q,y^4)=0` respectively, and are not the affine chart `r_4=1`.

Nondegeneracy of `P` transports to `P(q,y^4)` and to `F`, and the toric genus theorem plus Pick's theorem give the geometric genera of the smooth complete models

```text
g(Xtilde)=7,     g(Ytilde)=37,     g(Ctilde)=165.
```

The four edges of `Delta_X` are all the zeros and poles of `q` and `v` on `Xtilde`. The Kummer covers `y^4=v`, `w^4=q^2 y`, and `w^{16}=q^8 v` have total ramification `24`, `40`, and `136` respectively, and Riemann–Hurwitz reproduces the three genera, including infinity. The tower identity `40+4\cdot 24=136` holds.

An order-four source in this leaf would give an equivariant map from its Kummer curve to `Ctilde`, hence a morphism `P^1_x\to Ytilde` which is nonconstant because `r_7^4` is deck-invariant and a constant multiple of a nonconstant function of `x`, and already a nonconstant morphism `P^1_x\to Xtilde` because `r_7^{16}` is residual-invariant. Either map is impossible. Thus if the §1 gates pass, the entire `mu_4\neq 0` coefficient leaf is empty of sources, for every `U`. Until those gates are certified over characteristic zero, no elimination is claimed, and nothing here is a Taylor realization or a Keller pair.

---

## Attack A — exact plane gate: strength for every conclusion

**CONFIRMED.** The four items of §1 are independent, and none of the later identities can be obtained by dropping one of them.

Item 1 is a birationality hypothesis, not a consequence of a plane elimination ideal. If the projection `C_4\to A^2_{(s,t)}` had degree greater than one onto its image, one would have `K\supsetneq L(s,t)`, the lattice-index bounds on `[K:L(q,v)]` would become upper bounds only, and genera of the `(s,t)`-plane model would not be genera of `Ctilde`. The target states this limitation in the last sentence of §1. With item 1 in force, every rational function on `C_4`, including `a_0,\ldots,a_4` and `r_7`, lies in `L(s,t)`, so every place of the unique smooth complete model is a place of the `(s,t)`-curve: there are no extra poles created by the embedding in `A^7`.

Item 2 is the translation of the relation into the monomial coordinates of `(1.1)`. Equality as Laurent polynomials, up to a monomial, is the correct statement of a Newton polygon. Item 3 supplies irreducibility of `P` in `L[q,v]` and the exact convex hull `(1.3)`. A two-dimensional Newton polygon together with nondegeneracy implies geometric irreducibility over an algebraic closure, so “irreducible” over the already enlarged constant field is enough: the torus hypersurface cannot split into Galois conjugates without collapsing `Delta_X` to a segment. Item 4 is exactly Khovanskii nondegeneracy (smoothness in `(C^*)^2` from the two-dimensional face; distinct `C^*`-roots of each edge polynomial from the one-dimensional faces; vertices automatic). Without the two-dimensional face, the interior-point count would be only an upper bound on geometric genus.

The residual action `(2.1)` is the restriction of the V2-client formula `a_i\mapsto\lambda^{8-i}a_i` to `i=5,6`. Faithfulness on `K` is not an extra geometric axiom: `w\mapsto\lambda w` is a primitive character of `mu_16`, and the only element of `mu_16` with a positive-dimensional fixed locus in the `(s,t)`-plane that could contain the curve is `\lambda=-1`, which fixes `s=0`. If `s\equiv 0` then `q\equiv 0` and `P(0,v)\equiv 0`, so `q` divides `P`, contradicting irreducibility together with the vertex `(0,0)`. Cube roots of unity do not lie in `mu_16`, so there is no analogous kernel along `t=0`. The group therefore injects into `Aut(K)`, hence into `Aut(Ctilde)`. Pointwise stabilizers may be nontrivial; that is ramification, computed in §§4–5.

Finite automorphisms of a smooth complete curve in characteristic zero extend from the function field, and the quotient by a finite group is again a smooth complete curve. Thus `Xtilde` and `Ytilde` in `(2.5)` are well-defined as soon as items 1–4 hold, and they are the unique smooth complete curves with the invariant fields of `(2.4)`. The ordinary projective closures of `P(q,v)=0` and `P(q,y^4)=0` are complete models of those same fields (Attack D below), so their normalizations are `Xtilde` and `Ytilde`. This includes every zero of `t`, every pole of `q` or `y`, and every point at infinity. It is not the genus of the affine `r_4=1` slice.

---

## Attack B — invariant fields, `w,q,y,v`, degrees, two quotients

**CONFIRMED.** Directly from `(1.1)` and `(2.2)`:

```text
w^{16}=(s/t)^{16}=s^{16}/t^{16},
q^8 v=(s^2/t^3)^8 t^8=s^{16}/t^{16},
t=w^2/q=(s^2/t^2)\cdot(t^3/s^2)=t,
s=w^3/q=(s^3/t^3)\cdot(t^3/s^2)=s,
y^4=(t^2)^4=t^8=v,
w^4=(s/t)^4=s^4/t^4=q^2 y.
```

So `(2.3)` and the Kummer equation `(5.1)` are identities of rational functions, valid on the function field (the apparent division by `q` is not a restriction of the field equality). The function `q` is not identically zero: `P(0,v)` is the left-edge polynomial, nonzero as a polynomial because `(0,0)` is a vertex and, by nondegeneracy, has two distinct roots in `C^*` rather than vanishing identically. Likewise `t\not\equiv 0` because `P(q,0)` is the constant term.

The exponent lattice generated by `(2,-3)` and `(0,8)` is the image of the matrix with columns those vectors, determinant `16`. The character `(a,b)\mapsto 3a+2b\bmod 16` is surjective (`gcd(3,2,16)=1`), so the lattice of `mu_16`-invariant monomials has the same index `16` and coincides with `\langle(2,-3),(0,8)\rangle`. The lattice generated by `(2,-3)` and `(0,2)` has determinant `4`, and `(a,b)\mapsto 3a+2b\bmod 4` is likewise surjective, giving index `4`. These are statements about Laurent monomials, not about generation of the invariant polynomial ring; the target correctly refuses an invariant-ring claim.

Containment `L(q,v)\subseteq K^{mu_16}` is immediate from the weights. The reverse containment and the exact degree follow from Galois theory plus `(2.3)`: `K=L(s,t)=L(q,w)` and `w^{16}=q^8 v\in L(q,v)`, so `[K:L(q,v)]\le 16`; the action of `mu_16` on `K` is faithful of order `16`, so `[K:K^{mu_16}]=16`; therefore `L(q,v)=K^{mu_16}` and `T^{16}-q^8 v` is the minimal polynomial of `w`. The same argument with `mu_4` and `w^4=q^2 y` gives `L(q,y)=K^{mu_4}` and `[K:L(q,y)]=4`. In particular `[L(q,y):L(q,v)]=4` with `y^4=v`, so the two quotients are not the same object: `Ytilde\to Xtilde` is the residual cyclic cover of degree four. The affine `r_4=1` slice is `C_4` itself, of field `K`, not `Ytilde`.

---

## Attack C — three Newton polygons, Pick, interior genera, nondegeneracy transport

**CONFIRMED.** Shoelace, counterclockwise.

`Delta_X`: vertices `(0,0)\to(0,2)\to(1,3)\to(8,3)\to(0,0)`. Area `|0\cdot 2+0\cdot 3+1\cdot 3+8\cdot 0- (0\cdot 0+2\cdot 1+3\cdot 8+3\cdot 0)|/2=|3-26|/2=23/2`. Lattice lengths `gcd(0,2)=2`, `gcd(1,1)=1`, `gcd(7,0)=7`, `gcd(8,3)=1`, perimeter `B=11`. Pick: interior lattice points `I=23/2-11/2+1=7`. Direct count of strict interior points: `(1,1),(1,2),(2,1),(2,2),(3,2),(4,2),(5,2)`, seven points.

`Delta_Y`, the image of `Delta_X` under `(i,j)\mapsto(i,4j)`: vertices `(0,0),(0,8),(1,12),(8,12)`. Area `|0\cdot 8+0\cdot 12+1\cdot 12+8\cdot 0-(0\cdot 0+8\cdot 1+12\cdot 8+12\cdot 0)|/2=|12-104|/2=46`. Lattice lengths `8,1,7,4`, perimeter `B=20`. Pick: `I=46-10+1=37`. Direct count: ten interior points at `x=1`, then `8+7+5+4+2+1` at `x=2,\ldots,7`, total `37`.

`Delta_C`, the image of `Delta_X` under `(i,j)\mapsto(2i,-3i+8j)`: vertices `(0,0),(0,16),(2,21),(16,0)`. The linear map has determinant `16`, so area `16\cdot 23/2=184`, matching shoelace `|0- (16\cdot 2+21\cdot 16)|/2=184`. Lattice lengths `16, gcd(2,5)=1, gcd(14,21)=7, 16`, perimeter `B=40`. Pick: `I=184-20+1=165`.

Under nondegeneracy, the geometric genus of the smooth complete model of a Laurent plane curve is the number of interior lattice points. That is `(3.1)`, `(3.2)`, `(3.3)`. Equation `(3.3)` is correctly labelled a consistency check: the source obstruction is at least `Ytilde`, and already `Xtilde`.

Nondegeneracy transports under both substitutions, so the Newton counts on `Delta_Y` and `Delta_C` are not an extra hypothesis.

The map `(q,y)\mapsto(q,y^4)` is a degree-`4` étale covering `(C^*)^2\to(C^*)^2` in characteristic zero (`4y^3\neq 0`). Smoothness of `P=0` in the torus therefore pulls back to smoothness of `Q(q,y):=P(q,y^4)=0` in the torus, which is two-dimensional nondegeneracy of `Q`. Each one-dimensional face of `Delta_Y` is the image of a face of `Delta_X`. On the left, upper-left, and top edges the face polynomials of `Q` are `P_{\mathrm{face}}(y^4)` or the same univariate polynomial in `q`; simple `C^*`-roots remain simple because the extra factor of the derivative is a unit on `C^*`. On the lower edge, `Delta_X` has lattice length `1`, so `P` is binomial `A+B q^8 v^3`; after substitution the face polynomial of `Q` is `A+B z^4` in the primitive edge coordinate `z=q^2 y^3`. This has four distinct simple `C^*`-roots, matching lattice length `4`, even though the intermediate lattice points `(2,3),(4,6),(6,9)` are absent from the support of `Q`. Vertices remain monomials. Thus `Q` is nondegenerate with respect to every face of `Delta_Y`.

The map `(s,t)\mapsto(s^2/t^3,t^8)` is a degree-`16` étale covering of tori: the Jacobian determinant is `16 s t^4\neq 0` on `(C^*)^2`. Two-dimensional nondegeneracy of `F` follows. On the four edges of `Delta_C` the face polynomials are `P_{\mathrm{left}}(t^8)` (sixteen simple roots), a binomial (upper-left), the same degree-`7` univariate in `q=s^2 t^{-3}` as on the top of `Delta_X` (the primitive generator of that edge of `Delta_C` is exactly `q`), and `A+B s^{16}` on the bottom (sixteen simple roots). So `F` is nondegenerate with respect to `Delta_C`.

Independently of transport, Riemann–Hurwitz in Attacks E–F computes `g(Ytilde)` and `g(Ctilde)` from `g(Xtilde)=7` and the Kummer valuations of `v` and `q^2 y`. Those valuations use only the edge table of `Delta_X`. Agreement with the Newton counts is therefore a genuine check, not a circular reuse of the same area.

---

## Attack D — omitted places, non-split places, kernel, weighted/ordinary mismatch, reducibility of `P(q,y^4)`, affine genus

**CONFIRMED; every listed breaking attempt fails.**

**Omitted boundary points.** Outward normals of `Delta_X` (clockwise rotate of each counterclockwise edge) reproduce the first table exactly:

| edge | outward primitive | places | `ord(q)` | `ord(v)` |
|---|---|---:|---:|---:|
| `[(0,0),(0,2)]` | `(1,0)` | `2` | `1` | `0` |
| `[(0,2),(1,3)]` | `(1,-1)` | `1` | `1` | `-1` |
| `[(1,3),(8,3)]` | `(0,-1)` | `7` | `0` | `-1` |
| `[(8,3),(0,0)]` | `(-3,8)` | `1` | `-3` | `8` |

Zero and pole degrees: `deg(q)_0=2\cdot 1+1\cdot 1=3=deg(q)_\infty`, `deg(v)_0=8`, `deg(v)_\infty=1+7=8`. There is no place with both `ord(q)>0` and `ord(v)>0` (the origin: `P(0,0)\neq 0` by the vertex `(0,0)`), and no place with both orders negative (no northeast edge). Those eleven places are therefore all the zeros and poles of `q` and `v`. The ordinary line at infinity of `P(q,v)=0` consists of the two points cut out by the unique degree-`11` monomial `q^8 v^3`; their preimages on the normalization are among the Newton places already listed (top plus upper-left over `[0:1:0]`, lower-diagonal over `[1:0:0]`). The two left places are affine. The four edges of `Delta_C` similarly produce `16+1+7+16=40` places, matching `B(Delta_C)` and the lifted counts from the second table. Nothing at `t=0` or at infinity is missing from Riemann–Hurwitz.

**Non-split unramified places.** The genera are geometric. Over an algebraically closed residue field of characteristic zero, a unit is an `N`-th power and Hensel lifts every simple residual root. For `y^4=v` at `ord(v)=0` one has `gcd(4,0)=4` unramified places (the two left `X`-places give the eight left `Y`-places). For `w^4=q^2 y` at `ord=-4` one has `gcd(4,4)=4` unramified places (the four lower-diagonal `Y`-places). There is no residual-extension loophole in the geometric count.

**Kernel of the group action.** Attack A: the action on `K` is faithful. Stabilizers of closed points are the inertia groups of §§4–5, not a kernel of `mu_16\to Aut(Ctilde)`. Explicitly: at the sixteen points of the lower edge of `Delta_C` one has `t=0`, `s\neq 0`, and `\lambda^3=1` in `mu_16` forces `\lambda=1`, matching `e(C/X)=1` there; at the sixteen points of the left edge one has `s=0`, `t\neq 0`, and `\lambda=-1` fixes the point, matching `e(C/X)=2`.

**Weighted-projective versus ordinary plane closures.** The coordinates `q,v` are residual invariants (`q` of weight `0`, `v` of weight `16`), but `P` is not quasi-homogeneous: total degrees of the vertices are `0,2,4,11`. There is no weighted projective line or plane in which `P` is homogeneous of a single degree, so the ordinary projective closure in `P^2` is the correct naive complete model. Its arithmetic genus is `45`, not `7`; the excess is singularities of that model. The unique smooth complete curve with function field `L(q,v)/(P)` is simultaneously the normalization of that ordinary closure and the (already smooth, by nondegeneracy) compactification in the toric surface of `Delta_X`. The same holds for `P(q,y^4)` in coordinates `(q,y)`, whose vertex degrees `0,8,13,20` are likewise not weighted-homogeneous. No identity in §§3–5 uses an arithmetic genus or a weighted degree.

**Reducibility after `v=y^4`.** Let `Q(q,y)=P(q,y^4)`. If `Q=R^d` with `d>1` then `Delta_Y=d\cdot Delta(R)`, so the vertex `(1,12)` would be `d` times a lattice point, hence `d\mid 1`. So `Q` is not a proper power. By Attack B, `L(q,v)(y)` is a degree-`4` field, so `T^4-v` is irreducible over `L(q,v)` and `Q` is irreducible in `L(q)[y]`. Gauss's lemma then gives irreducibility in `L[q,y]`. A disconnected union would make the Newton genus of the product polygon disagree with the Riemann–Hurwitz genus of the connected Galois cover `Ytilde`; they agree at `37`. Thus `Ytilde` is the normalization of the ordinary projective closure of the irreducible plane curve `Q=0`.

**Affine genus.** The numbers `7`, `37`, `165` are geometric genera of smooth complete models, equivalently interior lattice points, equivalently Riemann–Hurwitz on complete curves. The target states that the affine `r_4=1` slice is not a source obstruction, and does not use it.

---

## Attack E — valuations, inertia, ramification totals `24`, `40`, `136`, three RH identities

**CONFIRMED.** For a cyclic Kummer cover `T^N=f` in characteristic zero, a geometric place with `ord(f)=n` has `gcd(N,n)` points above it, each of ramification index `N/gcd(N,n)`, and contributes `N-gcd(N,n)` to the different degree. (The case `n=0` is the completely split unramified fibre, `gcd(N,0)=N`.)

**`Ytilde\to Xtilde`:** `y^4=v`.

| `X`-edge | `#` on `X` | `n=ord(v)` | `gcd(4,n)` | `e` | `#` on `Y` | contribution |
|---|---:|---:|---:|---:|---:|---:|
| left | `2` | `0` | `4` | `1` | `8` | `0` |
| upper-left | `1` | `-1` | `1` | `4` | `1` | `3` |
| top | `7` | `-1` | `1` | `4` | `7` | `21` |
| lower diagonal | `1` | `8` | `4` | `1` | `4` | `0` |

Total `R_{Y/X}=24`, which is `(4.1)`. Riemann–Hurwitz:

```text
2g(Y)-2=4(2\cdot 7-2)+24=4\cdot 12+24=72,     g(Y)=37.
```

**`Ctilde\to Ytilde`:** `w^4=q^2 y`. Pulled-back orders: `ord_Y=e_{Y/X}\cdot ord_X` for functions of `X`, and `4\,ord_Y(y)=ord_Y(v)`. This reproduces the second table, including `ord(q^2 y)\in\{2,7,-1,-4\}`.

| `Y`-row | `#` on `Y` | `ord(q^2 y)` | `gcd(4,\cdot)` | `e` | inertia | contribution |
|---|---:|---:|---:|---:|---|---:|
| left | `8` | `2` | `2` | `2` | order `2` | `8\cdot 2=16` |
| upper-left | `1` | `7` | `1` | `4` | order `4` | `3` |
| top | `7` | `-1` | `1` | `4` | order `4` | `21` |
| lower diagonal | `4` | `-4` | `4` | `1` | trivial | `0` |

Total `R_{C/Y}=40`, which is `(5.2)`. Riemann–Hurwitz:

```text
2g(C)-2=4(2\cdot 37-2)+40=4\cdot 72+40=328,     g(C)=165.
```

**`Ctilde\to Xtilde`:** `w^{16}=q^8 v`. The four rows of the first table give `ord(q^8 v)\in\{8,7,-1,-16\}`.

```text
R_{C/X}=2(16-\gcd(16,8))+1(16-\gcd(16,7))+7(16-\gcd(16,1))+1(16-\gcd(16,16))
       =2\cdot 8+15+7\cdot 15+0
       =16+15+105=136.
```

Riemann–Hurwitz: `16(2\cdot 7-2)+136=192+136=328`, again `g(C)=165`. Tower: `R_{C/X}=R_{C/Y}+4 R_{Y/X}=40+96=136`. Every contribution is accounted for, including the unramified lower-diagonal fibre of `C/X` (sixteen points, inertia trivial) and infinity.

The Jacobian of `(s,t)\mapsto(q,y)` on `(C^*)^2` has determinant `4 s t^{-2}\neq 0`, so there is no extra ramification in the torus to omit from the tables.

---

## Attack F — source map, nonconstancy, firewall against live plane data and Keller existence

**CONFIRMED.** An exact-order-four source in the V2 leaf has coefficients satisfying `(0.2)` of the charged client, hence (after a constant weighted scaling `lambda^{16}mu_4=1`) lands on `C_4`. The order-four deck acts by `a_i\mapsto\zeta^{-i}a_i`. For `\zeta\in mu_4` this is the restriction of `(2.1)`, because `\zeta^{8-i}=\zeta^{-i}`. The unique subgroup of order four in cyclic `mu_16` is this deck. The source Kummer curve therefore maps `mu_4`-equivariantly into `Ctilde`, and the quotient morphism is a rational map from the source base `P^1_x` to `Ytilde`. The target `Ytilde` is proper, the source is a smooth curve, and a rational map from a smooth curve to a proper curve extends across every point, including every pole of the affine coordinates `q,y`.

The function `r_7` has weight `19`. It is not `mu_4`-invariant (`19\equiv 3\bmod 4`), but `r_7^4` is (`76\equiv 0\bmod 4`). By item 1 it lies in `K`, hence descends to `Ytilde`. On the source, `8\,dR_7/dx=j/u\neq 0`, so `R_7` is a nonconstant function of `x`; the scaling constant `lambda` is constant, so `r_7` is a constant multiple of `R_7`, and `r_7^4` remains nonconstant. A fourth-power of a nonconstant function of a curve of characteristic zero is nonconstant (the only rational solutions of `T^4=c` are constants). Therefore the extended morphism `P^1_x\to Ytilde` is nonconstant. Riemann–Hurwitz on a degree-`d\ge 1` cover `P^1\to Ytilde` would read `-2=d\cdot 72+R` with `R\ge 0`, which is impossible. Equivalently, the image would be a rational subfield of `L(x)`, hence `g(Ytilde)=0` by Lüroth, contradicting `(3.2)`.

The same argument with `r_7^{16}` (weight `19\cdot 16`, residual-invariant) gives a nonconstant morphism `P^1_x\to Xtilde`, contradicting `(3.1)`. The coefficient fibre `(0.3)` does not involve the infinity multiplicity `U`, so the obstruction, if the gates pass, empties the whole `mu_4\neq 0` leaf and not merely the `U=2` passports. A constant map is not available as a loophole: it would force `r_7` constant, contrary to the terminal differential.

The note does not assert that the live characteristic-zero plane/nondegeneracy computation has passed §1. Status, §0, and the first paragraph of §6 state the opposite. A modular plane relation is not an input. If any gate fails, the Newton genera are withdrawn and the alternative sieve `deg(\rho:Ytilde\to P^1)\mid D` is named only as a necessary terminal check; the parenthetical `D=1` and `D=3` for `U=2` is a pointer to a separate classification and is not used as evidence of `(3.1)`–`(5.3)` or of the conditional obstruction. Passing that sieve is explicitly not Taylor polynomiality and not a Keller pair. The coefficient-infinity firewall of the V2 client is preserved: a point of `C_4` is not a source.

---

## Scope firewall

Accepted, not enlarged:

- conditional genera, ramification, and Riemann–Hurwitz for the smooth complete residual and deck quotients of one irreducible one-dimensional component, granted the four exact gates of §1;
- faithfulness of residual `mu_16` on that component, and the invariant-field identifications `(2.4)`;
- a source-nonexistence implication *if* those gates pass, for every `U`, via a nonconstant map from `P^1_x`;
- the statement that affine `r_4=1` genus, a modular relation, and an unrun AWS endpoint are not obstructions.

Refused:

- any claim that the §1 gates have been certified;
- emptiness of `C_4` as a scheme, or a dimension statement;
- a Taylor realization at a finite branch point;
- terminal-power/Belyi constraints as outputs of this note;
- a Keller pair;
- order-four closure of the `(8,12)` cell;
- JC2;
- the V2 overall token, and the target's status language, as certificates of a plane polynomial.

The last paragraph of §6, naming `D=1` and `D=3` for `U=2`, is a fallback pointer, not a theorem of this note.

---

## Findings, classified

**Fatal.** None. Every numbered identity in `(1.1)`–`(1.3)`, `(2.1)`–`(2.5)`, `(3.1)`–`(3.3)`, `(4.1)`, `(5.1)`–`(5.3)` recomputes by hand. No omitted place, kernel, reducible pullback, weighted/ordinary mismatch, or affine-genus substitution breaks a conclusion. The §1 hypotheses are explicit and are the ones the conclusions use.

**Repairable.** None that blocks a numbered claim. Two sentences could be added without changing the mathematics: that nondegeneracy of `P` implies nondegeneracy of `P(q,y^4)` and of `F` by étale pullback of tori together with the edge-polynomial check `A+Bz^k`; and that `P(q,y^4)` is irreducible, which already follows from Attack D. The “entire leaf” sentence of §6 is correctly conditional on the gates, which include uniqueness of the plane relation; a parenthetical that every one-dimensional component must be gated would only restate §0.

**Cosmetic.**

1. The toric genus theorem is used without a name. The identity `g=I(Delta)` under the stated nondegeneracy is the standard Khovanskii count and is independently reproduced by Riemann–Hurwitz.
2. In `(5.2)` and `(5.3)` the zero contributions of the unramified lower-diagonal fibres are present in the general formula and omitted from the displayed sum. The totals `40` and `136` are unaffected.
3. Section 0 calls the fibre “hostile-confirmed”. That is provenance language for the V2 freeze; this review does not inherit it.
4. The `D=1,3` clause in §6 cites a separate passport classification. It is unused here.

**Fatal freeze / hash failures.** None. The three named SHA-256 strings recompute.

---

## Smallest failing identity

None. The identities

```text
[K:L(q,v)]=16,     [K:L(q,y)]=4,     y^4=v,     w^{16}=q^8 v,     w^4=q^2 y,
area(Delta_X)=23/2,   B(Delta_X)=11,   g(Xtilde)=7,
area(Delta_Y)=46,     B(Delta_Y)=20,   g(Ytilde)=37,
area(Delta_C)=184,    B(Delta_C)=40,   g(Ctilde)=165,
R_{Y/X}=24,   R_{C/Y}=40,   R_{C/X}=136,   40+4\cdot 24=136,
2\cdot 37-2=4\cdot 12+24,   2\cdot 165-2=4\cdot 72+40=16\cdot 12+136
```

all hold under the §1 gates. The smallest missing hypothesis that would break a numbered claim is one of those four gates themselves; they are stated, not omitted. Live plane/nondegeneracy certification is outside the note.

CONFIRMED
