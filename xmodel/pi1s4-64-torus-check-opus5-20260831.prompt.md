# Research lane: TORUS-CHECK — the torus-type test and the affine bridge

You are the flagship lane on the lit-sweep's decisive lead. The (6,4)
row sextic has simple singularities `3A_1 + A_14` (three affine nodes
+ the (2,15) infinity germ). The fetched literature (charged registry
§2) gives: (R10) a projective generic non-cyclic triple plane
branched at a degree-6 simple-singularity sextic exists iff the
sextic is TORUS TYPE; (R12/Oka Lemma 3, the Tokunaga criterion) torus
type is checkable: C is torus type iff there is a conic C_2 with
C_2 ∩ C ⊂ Sing(C) and I(C, C_2; P) = 2·rho(P,5) at each such point;
the TAME list excludes [A_14, 3A_1]; the sole non-tame loophole is
the identity A^3 - B^2 = F with deg A <= 2, deg B <= 3, which the
charged TRIPLE-COVER-CLOSE §4-6 already kills under row geometry.

charged_input=xmodel/lit-targeted-endgame-grok46-20260831.md
charged_input=xmodel/pi1s4-64-zvk-u6-opus5-20260831.md
charged_input=xmodel/pi1s4-64-triple-cover-close-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a130acb580933543a6909753e665c56295bd4ab052469caa8c84e041766c2467  {{LANE_INPUTS}}/lit-targeted-endgame-grok46-20260831.md
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  {{LANE_INPUTS}}/pi1s4-64-zvk-u6-opus5-20260831.md
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  {{LANE_INPUTS}}/pi1s4-64-triple-cover-close-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Tasks, fail closed:

1. **Run the torus-type check on the explicit family.** ROW-NF
   (PROVISIONAL, reviewed CONFIRMED) gives the family in closed form:
   x = r(t)^2, y = q(t), r = t^3+bt+c, q = t^4+(2b/3)t^2+(4c/3)t.
   Derive the implicit sextic F_j (resultant, by hand at the level of
   structure — or consume the ZVK-U6 report's derivation), and decide
   torus type: EITHER via the non-tame loophole closure (the charged
   cancellation kill: verify it covers exactly the A^3-B^2 = c·F
   identity needed here, all scaling conventions matched — if yes,
   the row sextic is NOT torus type, for every j), OR via Oka's
   criterion directly (a conic through the three nodes and the A_14
   point with the prescribed intersection numbers — count conditions:
   a conic has 5 parameters; passing through 3 nodes = 3 conditions;
   I = 2·rho at A_14 = how many? — decide existence).
2. **Conclude projectively.** If NOT torus type: by R10 no projective
   generic triple plane is branched at F_j — state exactly what dies
   (the S_3 resolvent cover EXTENDED to P^2 with branch only F_j).
3. **The affine bridge — the new work.** The campaign's φ lives on
   C^2 - D; its S_3 resolvent triple cover is affine. The projective
   statement leaves two escapes: (a) the projective extension is
   branched ALSO along the line at infinity; (b) the extension is
   not "generic" in R10's sense. Analyze both: the promoted
   72-tuple theorem constrains the infinity behavior (the cable
   braid image under any admissible tuple — compute the image of
   the infinity boundary/meridian of L_infty under the S_3 resolvent
   of the (O4)-shape tuples: is the L_infty meridian image trivial
   (then the cover does NOT branch at infinity and (a) closes) or a
   3-cycle/transposition (then type the branched-at-infinity
   projective object and check R10/CM25/Sh12 against branch degree
   6+1 or 6+2... the registry's R8/R9 constrain branch degree 6;
   fetch what exists for degree 7/8 or derive the cubic-surface
   projection analysis directly)? This is the exact gap between the
   literature theorems and the affine question — closing it kills
   the (6,4) row by pure algebra + sourced classification, with no
   braid computation. A typed OPEN naming the exact missing
   classification is a good outcome.
4. Assemble: row KILLED (theorem + full dependency chain), or the
   exact residual with the branched-at-infinity object typed.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-torus-check-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
