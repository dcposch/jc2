# Coordinator correction: pair-square surface conductor retyping

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **PROVISIONAL SAME-MODEL HOSTILE CORRECTION / DIFFERENT-MODEL REVIEW STILL REQUIRED**

## 0. Charged report and verdict

This note records an internal hostile audit of

```text
c4adef363801dfaebd444c0953ffdaf76c31623051833a9f4b195797812b64a2
  xmodel/pair-square-surface-conductor-retyping-sol56-20260830.md
```

whose sealed body is 18,318 bytes with SHA-256
`cbe0b53c1af0ee738bdfb6475abdb09fb49d203e3706514a812a2863fa5a52f2`.
The internal verdict is `CONFIRM_WITH_CORRECTIONS`.  Because both producer
and audit use the Sol model family, this note does not promote new surface
claims.  The curve-level N2/N3 results were already different-model reviewed
and bound separately in
`pair-square-qcs-coordinator-integration-sol56-20260830.md`.

## 1. Exact mathematics that survives

The following are correct at their displayed types.

1. **N2.**  For pole cycles `C_j` of lengths `e_j`, a support vector obeys

   ```text
   [1_S] in im(sigma-1)
     iff |S intersect C_j|=|S|*e_j/d for every j.
   ```

2. **N3.**  Using all finite branch monodromies of the connected curve cover,
   the external direct-sum inertia map surjects onto the pole-moving space and
   has kernel dimension `2G-2+2s`.
3. The normalization `Ybar` of the fixed ordered compactification
   `P^1_f times P^1_g` in `C(x,y)`, the off-diagonal closure `W`, its swap,
   its normalization, and its conductor square are canonical.
4. Once finite local sheet sets `S_P` over physical places are supplied, the
   abstract augmentation sequence

   ```text
   0 -> direct_sum_P Qtilde[S_P]
     -> Qtilde[disjoint_union_P S_P]
     -> Qtilde[{P}] -> 0
   ```

   is exact with ranks `w-r`, `w-1`, and `r-1` in the corresponding terms.
5. For any already-constructed finite event graph with pole marks, the
   relative-cohomology connecting map is injective exactly across the marked
   components described by the graph long exact sequence; if all `s` marks
   lie in one connected component, its source has rank `s-1` and the target
   rank is `s-1+b_1`.

Items 4 and 5 are abstract linear algebra/topology.  They do not construct
the local sheet system, conductor stalk, event graph, factor-swap descent,
dimension identification, or marked connectivity theorem.

## 2. Binding corrections to the provisional surface proposal

The diagonal marking must be defined scheme-theoretically: take the
scheme-theoretic intersection of `W` with the diagonal in the full fibre
square and its scheme-theoretic inverse image on `W^nu`, or explicitly state
that only reduced support is retained.  The diagonal is a whole component of
the full fibre square, not automatically a Cartier divisor there.

The tuple

```text
(W^nu, conductor square, diagonal-contact marking)
```

is a canonical **candidate** datum, not a proved minimal datum.  The Kummer
example shows that forgetting conductor/contact loses visible gluing data; it
does not prove that no invariant of the abstract normalization could ever
recover the needed information.

Likewise, the local augmentation is canonical only after the physical local
sheet sets and their specialization are constructed.  It is a candidate for
realization by a conductor stalk, not yet that stalk or a boundary matrix.
The event graph and its map remain entirely conditional; fixed points of the
factor swap may require equivariant or stacky treatment.

## 3. Kummer control retyped

For `F_b(a,x)=(a,x^b)`, the affine residual components
`x_1=zeta*x_2` meet the diagonal at `x=0`; this is an affine ramification
line, not a physical boundary place.  The unique physical pole place is
`x=infinity`, where the projective residual closure also meets the diagonal.
Those contacts must not be conflated.

Moreover, this finite map has empty Section-4 missing set `R`, so its
canonical `U=T-pi(R)` is all of `T`; choosing `A^1 times G_m` instead is a
different non-Keller étale-locus control.  It has no Section-7 finite-value
boundary quotient line.  Therefore `w(a)=b` is only a persistent local-sheet
analogue, not the campaign's proved `w_i` datum.

The safe conclusion is narrower and still useful:

> An isotrivial persistent pair event must contribute zero to any
> special-minus-generic excess.  Hence raw normalized-component, conductor,
> or cell ranks cannot themselves be the desired excess.

This does not establish that relative vanishing cohomology is the unique
correct construction.

## 4. Next exact gate

On one actual Section-7 quotient curve, pull the precisely marked conductor
datum to a strict-henselian disc at one exceptional point.  Construct an
equivariant reduced-sheet augmentation complex and its generic-to-special
cone.  The stop tests are:

```text
generic rank                         = b_i-1;
special cohomology concentrated H^0  = w_i(z)-b_i;
root-braid and factor-swap descent    = proved;
admissible-blowup invariance          = proved;
isotrivial Kummer vanishing           = zero, with 0 and infinity distinct.
```

Only after this stalk gate should the campaign attempt a global event graph,
marked connectivity, or an identification with the excess module.  No QCS,
PCB, selector, actual polynomial map, counterexample, or JC2 statement is
proved here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5398`.
- Body SHA-256:
  `6126735f68f198b7ef05dbba796adda795e5ba14637d07cd402d439356603031`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
