# Coordinator integration: Galois block obstruction and no two-block system

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **BINDING INTEGRATION / DIFFERENT-MODEL-CONFIRMED BLOCK THEOREM**

## 0. Evidence and disposition

This integration binds the conservative intersection of

```text
766a843a25eaf560840f15afa8971dd39246fc8b15290491d18e7f4a4c6bb7f7
  xmodel/block-descent-d2-galois-obstruction-producer-sol56-20260830.md
e324c104d06ad9e987cfe304ee001e52a58d91eaba941b80c78555a058056df9
  xmodel/block-descent-d2-galois-obstruction-hostile-review-opus5-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The Opus verdict is `CONFIRM_WITH_CORRECTIONS`.  It independently rebuilt
the missed-principal-divisor lemma, fixed-sheet theorem, Galois-uniformity
contradiction, rank-two trace-zero proof, and group-theoretic translation.
No mathematical gap was found in `BD-GAL` or `BD-D2`.  This file incorporates
the review's shorter proof, residue-degree accounting, and terminology
repairs rather than preserving the producer's avoidable ambiguities.

## 1. Binding theorem

Let `F=(f,g):A^2_C->A^2_C` be a hypothetical non-invertible Keller map and
let

```text
C(f,g) proper-subfield K proper-subfield C(x,y),
d1=[C(x,y):K]>=2,             d2=[K:C(f,g)]>=2.
```

For the promoted factorization

```text
A^2 --g1, etale quasi-finite--> Y=Spec(B_K)
    --g2, finite flat--> A^2,
```

write `R` for the non-etale locus of `g2`.  Then:

1. **Missed principal divisors.**  No nonzero nonunit `b in B_K` has
   `V_Y(b) subset Y minus g1(A^2)`.  Indeed, its pullback would be a
   nowhere-zero polynomial on `A^2`, hence a scalar unit, and the literal
   inclusion `B_K subset C[x,y]` makes `b` the same scalar.
2. **Fixed sheet over every prime divisor.**  For every irreducible
   `p in C[f,g]`, at least one component of `g2^{-1}(V(p))` dominates
   `V(p)` and is generically unramified.  The shortest proof applies item 1
   directly to `b=p`: if all components were inside `R`, the whole principal
   divisor would be missed.  If the primes above `(p)` have ramification and
   residue degrees `(e_i,f_i)`, geometric inertia fixes exactly
   `sum_(e_i=1) f_i` sheets, and this sum is at least one.
3. **No proper Galois quotient.**  The extension `K/C(f,g)` is not Galois.
   Otherwise transitivity of the Galois group on primes over a height-one
   prime makes every `e_i` equal.  A component of the nonempty branch support
   supplies an `e_i>1`, while item 2 supplies an `e_i=1`, a contradiction.
   Normality, not smoothness of `Y`, is enough for the height-one DVR
   argument; characteristic zero supplies separable residue extensions and
   tame divisorial ramification.
4. **No two-block system.**  In particular `d2!=2`, because every quadratic
   extension in characteristic zero is Galois.  In monodromy notation
   `H subset J subset G`, this says `[G:J]!=2` and `J` is not normal in `G`.
   It says nothing about the block size `[J:H]`; in particular it does not
   exclude `d1=2`.
5. **Structural corollaries.**  `B_K` is nonfactorial and nonmonogenic over
   `C[f,g]`.  The rank-two direct proof writes a hypothetical degree-two
   algebra globally as `A[w]/(w^2-h)`; its ramification set is the nonempty
   principal divisor `V_Y(w)`, contradicting item 1.  This second proof is
   independent of the Galois-uniformity argument, but shares the same source-
   unit mechanism and is not advertised as logically independent of item 1.

“Branch” and “discriminant” agree here only at the level of support.  No
divisor multiplicities are identified.  A fixed sheet of `g2` is a fixed
block of the full map; it is not necessarily a single source sheet.

## 2. Independently checked strengthenings

The reviewer derived the following two claims.  The coordinator checked
their proofs directly against the promoted sandwich; they are included with
their exact global scope.

**Class-lattice injection.**  Let `Z=Y minus g1(A^2)`.  The free abelian
group on the codimension-one components of `Z` injects into `Cl(Y)`.  If a
divisor supported in `Z` were `div(b)`, then both `b` and `b^{-1}` would be
regular on `g1(A^2)`.  Their pullbacks would be mutually inverse polynomials
on `A^2`, hence scalars; the function-field inclusion then makes `b` scalar.
Thus every ramification-component class has infinite order and `Cl(Y)` is
infinite whenever `R` is nonempty.

**Nonprincipal different.**  The relative dual

```text
omega_(B_K/A)=Hom_A(B_K,A)
```

is not a free `B_K`-module, equivalently the different is not principal.
If a generator existed, its effective divisor would be
`sum_T(e_T-1)T`, supported exactly on the nonempty codimension-one
ramification locus in characteristic zero.  It would give a nonempty
principal closed set inside `R`, contradicting item 1.  Consequently there
is no global complete-intersection presentation of this finite algebra over
`A`.  This statement does **not** assert that the finite morphism is nowhere
locally complete intersection: an invertible but nonfree dualizing module is
not excluded by the argument.

## 3. Prior-art boundary

A targeted source check confirms that the full-extension Galois case is
classical, beginning with Campbell (1973), with later Razar/Wright results.
The check found no indexed statement of the exact proper-intermediate theorem,
but a negative targeted search is not novelty evidence.  The mathematical
claim here is internal and reviewed; no external novelty claim is made.

The source record is:

```text
b75c56add2dcd846654e627ab10bde1a0bea62b857db004f64b77da46e41b741
  xmodel/block-descent-galois-prior-art-targeted-check-sol56-20260830.md
```

## 4. Exact boundary and successor

Promoted:

```text
proper Galois block quotient: impossible;
two-block quotient d2=2:       impossible;
every divisorial inertia:      at least one fixed block;
ramification class lattice:    injects into Cl(Y);
different / relative dual:     nonprincipal / nonfree.
```

Not proved: `d1!=2`; exclusion of any non-Galois `d2>=3`; primitive
monodromy; parity of the total degree; smoothness of `Y`; properness or
surjectivity of `g1`; existence of a block; a counterexample; or JC2.

The next block discriminator is cubic and must use the `A^2` first leg, not
only cover-side finite algebra.  The affine-linear Miranda subfamily and its
logarithmic first-leg obstruction are separate review-gated packets at this
seal; they are not promoted by this integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6637`.
- Body SHA-256:
  `f3668b3ec1c7fd5caefe8b0421548327fc990426b6a04f37083ef7b907475ca1`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
