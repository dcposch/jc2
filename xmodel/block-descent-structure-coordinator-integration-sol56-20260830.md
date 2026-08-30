# Coordinator integration: intermediate block descent becomes an étale sandwich

Coordinator: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: **BINDING PROMOTION / CONDITIONAL STRUCTURE THEOREM / FORMER PRIMITIVITY ROUTE STOPPED**

## 0. Custody and disposition

The reviewed proposal is Opus cross-pollination section 5.3:

```text
6e48015c296c9677237daee2a21a20195d5fc346e163dbcbaa68b74e46bab296
  xmodel/ideation-20260829T2254Z-crosspoll-opus5.md
  body 53234 / 647bca6600e31816c1f7ac14f2b061d7be574cf653d7102ac063375627d0346b
```

Fable 5 independently audited the local algebra, purity/discriminant
argument, finite-étale endgame, controls, and minimal-degree consequence,
returning `CONFIRM_WITH_CORRECTIONS`:

```text
bc88ca78c303553555dee3e94f16cbef6e81ea187cd201b73e6d700ccc821992
  hostile review, 38440 bytes through BODY-END
213da698fcc910dbc119573e8d4d6a09ebcd839ba39f1acc9d2b1fa9ba794a66
  lane log
ecbf087ea4d9b86b2a3ae11007eebbf2b0928b8a96c3d21cf2ed3443cf428ad2
  prompt
fa91382a3103312a70ae48ee6f55daf710a916971400e230c385cbaac5701f85
  run receipt
```

The review finds that the proposed codimension-one condition is not a new
hypothesis to prove: for every nontrivial block it is false. The surviving
result is the conservative block-structure theorem below. This integration
repairs the review's special-fibre cardinality argument before promotion and
withholds only its citation-dependent polynomial-parametrization decoration.

## 1. Promoted theorem

Let `F=(f,g): A^2_C -> A^2_C` be a non-invertible Keller map. Let

```text
C(f,g) proper-subfield K proper-subfield C(x,y),
d1=[C(x,y):K] >= 2,       d2=[K:C(f,g)] >= 2,
```

and let `B_K` be the integral closure of `C[f,g]` in `K`. Put
`Y=Spec(B_K)`. The inclusions factor `F` as

```text
A^2 --g1--> Y --g2--> A^2.
```

Then the following hold, without a minimal-topological-degree assumption.

1. `B_K` is contained in `C[x,y]` and is module-finite over `C[f,g]`.
   Thus `Y` is an integral normal affine surface with function field `K`.
2. `g2` is finite, flat, and surjective of generic degree `d2`. Its
   trace-discriminant ideal is nonzero (and principal on `A^2`).
3. `g1` is dominant and quasi-finite of generic degree `d1`; in fact it is
   étale everywhere and hence open. It is not finite, proper, or surjective.
4. If `R` is the non-étale locus of `g2`, then `R` is nonempty and has pure
   codimension one. Moreover

   ```text
   g1(A^2) subset Y_sm minus R,       Sing(Y) subset R.
   ```

   Hence `g1` misses every point of every branch divisor. In particular its
   image never contains every codimension-one point of `Y`.
5. With `A(h)` denoting the nonproperness set of a complex polynomial map,

   ```text
   Y minus g1(A^2) subset A(g1),
   A(F)=g2(A(g1)),
   g2(R)=V(Disc(g2)) subset A(F).
   ```

6. For every closed point `z` of the discriminant curve,

   ```text
   #F^{-1}(z) <= (d2-1)*d1 = deg(F)-d1.
   ```

   For every closed `z` outside `A(F)`, the fibre has exactly `deg(F)`
   points.
7. `Y` is not isomorphic to `A^2`.

This is conditional structure on a hypothetical counterexample and a proper
intermediate field. It proves neither that such a field exists nor that a
counterexample exists.

## 2. Load-bearing arguments

The containment `B_K subset C[x,y]` follows because an element of `B_K` is
integral over `C[f,g]`, hence over `C[x,y]`, and lies in `C(x,y)`, while
`C[x,y]` is integrally closed. Finiteness of the normalization in the finite
separable field extension gives the finite map `g2`. Normal surfaces are
Cohen--Macaulay, so miracle flatness over the regular target makes `g2`
finite flat; integrality makes it surjective.

The non-obvious strengthening is completion rigidity. At a closed point
`x`, with `y=g1(x)` and `z=F(x)`, étaleness of `F` identifies the completed
local rings at `z` and `x`. Quasi-finiteness of `g1` makes the completed
local ring at `x` finite over that at `y`. Excellence and normality make the
completed local ring at `y` a two-dimensional normal domain. The intervening
map has height-zero kernel and is surjective because its composite is the
completion isomorphism; it is therefore itself an isomorphism. Flatness and
unramifiedness descend, so both `g1` at `x` and `g2` at `y` are étale. Since
the schemes are Jacobson, this holds everywhere on the image. Thus the image
of `g1` is open and disjoint from `R` and from `Sing(Y)`.

If `R` were empty, the connected finite cover `g2` would be finite étale over
`A^2_C`, hence trivial, contradicting `d2>=2`. Purity (equivalently here the
finite-flat discriminant support together with branch purity) makes the
nonempty branch locus divisorial. This proves that the codimension-one image
antecedent fails rather than remaining an open bridge.

Finite `g2` is proper, which gives the composition identity
`A(F)=g2(A(g1))`. Openness and density of `g1(A^2)`, plus compactness of
bounded subsets of `A^2(C)`, give `Y minus g1(A^2) subset A(g1)`. Since all
of `R` is missed, its discriminant image lies in `A(F)`.

The fibre deficit needs one normalization lemma that was implicit in the
review. Let `Z` be the normalization of `Y` in `C(x,y)`; strong Zariski Main
embeds `A^2` openly in `Z`. For a closed `y in Y`, localize at `y` and let
`q_1,...,q_r` be the points of `Z` above it. Their residue fields are `C`.
Chinese remaindering supplies an integral element `b` with pairwise distinct
residues at the `q_i`. Its minimal polynomial over `K` has degree at most
`d1` and coefficients in the normal local ring: integrality makes those
coefficients integral, and normality brings them back into the ring. Modulo
the maximal ideal this polynomial has the `r` distinct chosen residues as
roots, so `r<=d1`. Thus every `g1` fibre has at most `d1` points. A finite-
flat `g2` fibre has at most `d2` distinct points, and over its discriminant at
least one lies in `R` and contributes no `g1` preimage. This proves the
displayed `deg(F)-d1` bound. Outside `A(F)`, properness over a small
neighborhood makes the étale map `F` a covering of its generic degree,
giving equality.

Finally, if `Y` were abstractly `A^2`, the factorization could be conjugated
to polynomial self-maps `F=G2 o G1` of `A^2`. The chain rule makes both
Jacobian determinants nonzero constants (the image of `G1` is dense), so
the finite map `G2` would be a connected finite étale cover of degree
`d2>=2` of `A^2_C`, again impossible.

## 3. Binding corrections and withheld claims

1. The launch condition "`g1(A^2)` contains every codimension-one point" is
   refuted for every nontrivial block: the whole nonempty branch divisor is
   missed. It must not remain listed as an attainable proof obligation.
2. The alternative recognition target `Y isomorphic to A^2` is also
   impossible for every nontrivial block. It is a reductio, not a descent
   theorem waiting to be proved.
3. Consequently this route gives no implication from minimal topological
   degree to primitive monodromy. Primitivity remains open. The honest
   successor is to rule out the forced étale sandwiches directly, beginning
   provisionally with block index `d2=2` (`BD-D2`).
4. The review's estimate `#F^{-1}(z) <= deg(F)-d1` is promoted only with the
   CRT/minimal-polynomial normalization lemma supplied in section 2. It does
   not require flatness of the degree-`d1` normalization and makes no
   attainment claim beyond the displayed upper bound.
5. The stronger wording that discriminant components are polynomially
   parametrized components of `A(F)` is citation-dependent and unnecessary
   for the structural result. Only the proved inclusion
   `g2(R)=V(Disc(g2)) subset A(F)` is promoted here.

## 4. Scope and next discriminator

The theorem constrains only a block that already exists. It does not supply
an intermediate field, prove primitive monodromy, select a bounded
topological degree, control all components of `A(F)`, decide smoothness of
`Y`, or prove JC2. The proposed next discriminator `BD-D2` is not promoted:
it asks whether a degree-two finite-flat branched cover in this sandwich can
be ruled out using the topology of the complement and the geometry at
infinity. It requires its own producer and hostile review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8285`.
- Body SHA-256:
  `85db7afd1e8b9f1039bbf977b78a6ea1f64cef9b6fb9323f2233281cf1be6e9f`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
