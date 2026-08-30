# Clean-room audit: transfer of the `A1`-ruling theorem to a proper block surface

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`u_rows_full_family`)  
Frozen basis: `f02aba6913ec6f9ecd1f3ae103475cde05f3ee29`  
Disposition: **CONFIRM WITH MATERIAL HYPOTHESIS/PROOF REPAIRS; QUALITATIVE TRANSFER ONLY**

## 0. Verdict

Opus's qualitative `RULE-ON-Y` conclusion is correct, but not for the reason
given.  Write `R` for the **source non-etale locus** of `g2`; this is the
object called `R` in the promoted block theorem.  Then

```text
U := Y minus R
```

is in fact a smooth rational affine complex surface, is dominated by the
actual first leg `A2 -> U`, has only constant units, and has logarithmic
Kodaira dimension `-infinity`.  Consequently the exact charged
Miyanishi--Sugie theorem applies and gives an `A1`-fibration

```text
rho: U -> C,                    C=A1 or P1,
```

and the charged Gurjar--Miyanishi fibre statement gives that every reduced
fibre is a disjoint union of affine lines.

Three repairs are load-bearing.

1. An open subset of an affine surface is not automatically affine.  The
   missing argument is Nagata's dimension-two theorem: the complement of an
   effective Weil divisor on a normal excellent affine surface is affine.
   It applies because `R` is nonempty and pure of codimension one.
2. Miyanishi--Sugie consumes **smooth affine** plus negative log Kodaira
   dimension, not merely `normal affine dominated by A2`.  Smoothness is
   nevertheless automatic here because `R` is the full non-etale locus and
   the target of `g2` is smooth; equivalently the promoted block theorem
   gives `Sing(Y) subset R`.
3. `branch(g2)` is ambiguous.  The displayed open is well typed only when
   `B` means the source ramification/non-etale support `R`.  If `B` means the
   target discriminant curve, `Y minus B` is meaningless.  The principal
   open `Y minus g2^{-1}(B)` is smooth affine but need not contain the whole
   first-leg image, because an unramified sheet may lie over a discriminant
   value.

Thus `RULE-ON-Y` genuinely crosses the quadratic-presentation firewall at a
qualitative level for the proper-block sector.  It does not transfer the
quadratic Euler/Picard cap, does not bound an adapted completion, and says
nothing about a primitive counterexample having no proper intermediate
field.

## 1. Exact charged inputs

The audit charges these immutable reports literally:

```text
0345e4973092fb621a64bde13b0cba71adeabd640e0baaba4ec215ff8c8cd3a5
  xmodel/ideation-20260830T1015Z-opus5.md

ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
  body 85db7afd1e8b9f1039bbf977b78a6ea1f64cef9b6fb9323f2233281cf1be6e9f

f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md
  body a8aa57dc9f1208491b4512321a4bdd2d83e6ce496707299e25a8179916fdf261

f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
  body f3668b3ec1c7fd5caefe8b0421548327fc990426b6a04f37083ef7b907475ca1
```

The first block integration promotes, for a hypothetical noninvertible Keller
map and a proper intermediate field,

```text
A2 --g1, etale quasi-finite dominant--> Y
   --g2, finite flat surjective--> A2,
```

where `Y` is an integral normal affine surface, `R=NonEt(g2)` is nonempty
and pure of codimension one, and

```text
g1(A2) subset Y_sm minus R,             Sing(Y) subset R.
```

The second block integration additionally proves that missed boundary
component classes inject into `Cl(Y)` and that the different is nonprincipal.
Those facts do not obstruct affineness of `Y minus R`: on a normal excellent
affine surface a non-Cartier and nonprincipal effective Weil divisor can
still have affine complement.

The ruling integration is presentation-specific only in its construction of
the quadratic open and its Euler number.  Its source audit records the
general surface theorem in the exact form used below.

## 2. Reconstruction of every hypothesis on `U=Y minus R`

### 2.1 Excellence and the divisor to be deleted

`Y` is finite over `A2_C`, hence is a finite-type complex affine scheme and
therefore excellent.  It is a normal integral surface.  Since `R` is a pure
codimension-one reduced closed subset, its irreducible components define the
effective Weil divisor

```text
R_red = sum_i R_i,
```

whose support is exactly the set deleted in defining `U`.

### 2.2 Affineness: the omitted theorem

Nagata's theorem for normal excellent two-dimensional domains says that the
complement of every effective Weil divisor in the affine spectrum is affine.
Applying it to `R_red` proves that `U` is affine.  This is strictly stronger
than the principal-open argument and is essential here: the promoted
class-lattice theorem rules out any nonempty principal divisor supported in
the missed locus.

The targeted source check used Holger Brenner, *The affine class group of a
normal scheme*, arXiv:`math/0209298`, Introduction (the normal excellent
dimension-two case, attributed there to Nagata), together with its
Definition 1.1 and Lemma 1.2/Remark 1.6 conventions for complements of
effective Weil divisors:

```text
https://arxiv.org/abs/math/0209298
```

No factorial, locally factorial, Cartier, principal, or Gorenstein hypothesis
is required.  Conversely, the bare implication "open in affine implies
affine" remains false and must not appear in the proof.

### 2.3 Smoothness and the role of singular points

By definition `g2` is etale at every point of `U`.  Since its target `A2` is
smooth, `U` is smooth.  This also follows from the promoted inclusion
`Sing(Y) subset R`.

The theorem does **not** say that `Y` is smooth.  Singular points can remain
outside `g1(A2)`; indeed every singular point is necessarily outside that
image.  What is proved is that none remains after the full source non-etale
locus is deleted.  Deleting only selected divisorial branch components would
not license this conclusion.

### 2.4 The actual dominant first leg

Because `g1(A2)` is disjoint from `R`, the morphism factors uniquely through
the open immersion `U -> Y`.  Its image is dense in `Y`, hence dense in the
dense open `U`; therefore

```text
g1:A2 -> U
```

is an actual dominant, generically finite morphism.  It remains etale and
quasi-finite.

There is also a useful independent repair if one refuses Nagata's theorem.
Let `V=g1(A2)` with its open-subscheme structure.  Openness of `g1` makes
`V` open in `Y`, and `A2 -> V` is surjective etale and quasi-compact, hence
fpqc.  Affineness descends fpqc, so `V` is smooth affine.  Thus the ruling
theorem applies at least to the actual first-leg image.  Nagata is what
upgrades this smaller, image-dependent statement to the canonical open
`U=Y minus R`.

### 2.5 Rationality, units, and logarithmic Kodaira dimension

Dominance makes pullback injective on regular functions.  Hence every unit
on `U` pulls back to a unit of `C[x,y]`, and

```text
O(U)^* = C^*.
```

The same dominant generically finite map makes a smooth projective model of
`U` unirational.  Over `C`, the surface Castelnuovo theorem makes it rational.
Finally, logarithmic pluricanonical pullback along `A2 -> U` gives

```text
bar-kappa(U) <= bar-kappa(A2) = -infinity,
```

so `bar-kappa(U)=-infinity`.  This is the same charged argument used in the
quadratic ruling integration; no compactification of `Y` has been assumed.

## 3. Exact surface theorem and maximum safe conclusion

The charged hostile review states the Miyanishi--Sugie theorem at the needed
scope: over an algebraically closed field of characteristic zero, a
**smooth affine surface** has logarithmic Kodaira dimension `-infinity` if
and only if it is `A1`-ruled, and in dimension two the cylinder projection
extends on the surface itself to a surjective `A1`-fibration over a smooth
curve.  There is no finite base change.

Applying it gives

```text
rho:U -> C,                   general fibre A1.
```

Since `U` is rational, Luroth makes `C` rational.  Pullback embeds
`O(C)^*` into `O(U)^*=C^*`; a smooth rational affine curve with at least two
punctures has a nonconstant unit.  Therefore the exact base dichotomy is

```text
C=A1 or C=P1.
```

The complete-base branch is real at this level and cannot be discarded.
The charged Gurjar--Miyanishi lemma then gives, for every fibre, that its
reduced support is a disjoint union of curves isomorphic to `A1`.  Fibre
multiplicities are not controlled by that statement.

The resulting maximum safe theorem is:

> **Proper-block ruling theorem.**  For every proper intermediate field of a
> hypothetical noninvertible complex Keller map, let `Y,g1,g2` be the
> promoted block factorization and let `R=NonEt(g2)` in the source.  Then
> `U=Y minus R` is a smooth rational affine surface with
> `O(U)^*=C^*` and `bar-kappa(U)=-infinity`, dominated by the actual etale
> quasi-finite first leg `A2 -> U`.  It admits a surjective `A1`-fibration
> over exactly `A1` or `P1`, with no finite base change; every reduced fibre
> is a disjoint union of affine lines.

This theorem uses no quadratic trace-zero frame, incidence surface, `F5`
boundary type, or fixed coefficient presentation.

## 4. Smooth-locus and terminology controls

Using only a smooth locus does not generally repair an affineness gap.  The
normal quadric cone

```text
Y0=Spec C[x,y,z]/(z^2-xy) -> A2_(x,y)
```

is finite flat of rank two and has one singular point `o`.  Its smooth locus
`Y0 minus {o}` is not affine: normal Hartogs gives the same global function
ring as `Y0`, so if the punctured surface were affine its canonical spectrum
would put the omitted point back.  On the other hand the full non-etale locus
of this particular finite map is `V(z)`, and its complement `D(z)` is smooth
affine.  This cleanly separates "take the smooth locus" from "delete the full
ramification divisor".  It is only a local-logic control: its principal
ramification violates the promoted missed-principal-divisor obstruction and
it is not a block sandwich.

Likewise, if `D=V(Disc(g2))` denotes the **target** branch curve, then

```text
g2^{-1}(A2 minus D)
```

is a principal affine open and is finite etale over `A2 minus D`.  It can be
strictly smaller than `Y minus R`: over a target branch value, some source
sheets may be unramified.  The block theorem says `g1` avoids `R`, not that it
avoids all of `g2^{-1}(D)`.  This target open therefore cannot silently
replace `U`.

## 5. Firewall, numerical non-transfer, and controls

The qualitative ruling really is presentation-independent within the
proper-block horn, so it crosses the quadratic-presentation firewall in that
precise sense.  It does **not** transfer any of

```text
e(U)=12-r-c,       r+c<=11,       the P1 sharpening,
the D9 lattice,    a bounded adapted completion,   the F5 carrier table.
```

The constant `12` and all displayed ranks come from the charged quadratic
completion.  An independent compactification and boundary/Picard calculation
for `Y` would be needed before the ruling becomes a numerical exclusion.

The complete-base control in the charged ruling packet remains decisive:
`F_n minus S` for a smooth ample section is a smooth rational affine surface
with constant units, a dense etale `A2`, and an `A1`-fibration over `P1`.
Thus none of the transferred qualitative hypotheses excludes the `P1` base.

There is no honest cheap "consistent full sandwich" control.  If one
exhibited `Y,g1,g2` with the promoted proper-block degrees `d1,d2>=2` and
`g1(A2) cap R=empty`, then

```text
F=g2 o g1:A2 -> A2
```

would be etale everywhere and would have generic degree `d1*d2>1`; it would
itself be a noninvertible Keller map and hence a counterexample to JC2.
Opus's proposed falsification control must therefore be priced as solving the
counterexample problem, not as an ordinary abstract model.  The quadric-cone
and Hirzebruch controls above test individual logical steps without claiming
a full sandwich.

## 6. Exact repairs to the Opus card

Replace the card's hypothesis sentence and cheapest discriminator by:

```text
B := R=NonEt_Y(g2) (source support).
R is a nonempty pure Weil divisor; Sing(Y) subset R.
Nagata => U=Y minus R is affine; etaleness => U smooth.
The actual g1 factors dominantly through U.
Units, rationality, and bar-kappa=-infinity follow from this map.
Miyanishi--Sugie then yields the A1-fibration.
```

Do not say that the external theorem consumes only "normal affine dominated
by A2".  Do not propose restriction to the smooth locus if normality fails;
normality is promoted, `U` is already smooth, and a smooth locus need not be
affine.  Do not call a full sandwich an inexpensive consistency control.

With these changes the disposition is `PROVE/REPAIR`, not `REFUTE`.  The
qualitative theorem is exact and useful as a new Avenue 26/30 instrument;
its next honest discriminator is a completion/boundary invariant for the
canonical `U`, or a block-specific restriction on the two possible ruling
bases.  No selector, primitive-monodromy theorem, counterexample, or JC2
conclusion follows here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13234`.
- Body SHA-256:
  `b0252d377b6ae898dabe9ee95401113cab637f2b1d58e1fb8415469fc29199e6`.
- Frozen basis: `f02aba6913ec6f9ecd1f3ae103475cde05f3ee29`.
