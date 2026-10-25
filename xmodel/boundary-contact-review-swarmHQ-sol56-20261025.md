# Independent review of the boundary-contact constraints

Reviewer: swarmHQ Sol5.6, configured independent review role. Date: October 25, 2026 (UTC).
Basis: `2ead4a746396b8a5ec0cb5793c3ef66658bae2b6`.
Evidence tier: MANUAL / INDEPENDENT REVIEW / CONDITIONAL.
Reviewed public claim: [boundary-contact constraints](boundary-contact-constraints-swarmHQ-root-astra-20261025.md).
The review below is byte-identical to lines 5–90 of the independent terminal review
(full SHA256 `c1a76f414b208000e7746e16c0fc4705413b04001b7b452017496fa40be7e1cf`).
Its producer filename denotes the exact source whose scientific sections are copied in the public proof; this is an export of that review, not a new review of the public formatting.

## Verdict

**PASS_CONDITIONAL.** No fatal implication was found in the two necessary
constraints, the two-centre support consequence, or the stated local-cover
gap in `boundaryperiod1545-astra.md`. The result remains conditional on the
adopted actual divisorial attachment/projectivity package and named standard
Serre, covering, and rational-fibre tools. It supplies a sufficient
commutation condition, not an available computation, exclusion of all escape,
stabilization, or JC2 proof.

## Hostile audit

1. **Candidate A.** If an integral `D!=B` meets `B` set-theoretically only at
a smooth point `p`, it avoids the unique surface singularity `q`; hence its
Weil divisor is Cartier along its support and trivial off it. With
`Pic(Y)=Z[L]`, effectiveness and ampleness give `D~lL`, `l>0`, and restriction
`D|B=l[p]`. For the ordinary cuspidal rational curve, the normalization unit
sequence gives additive, torsion-free `Pic0(B)`, while smooth points
parametrize `Pic1(B)`. Therefore `O_B(lp)=L_B^l=O_B(lp0)` forces `p=p0`.
This fixes the boundary point only; it does not impose one place, genus,
tangency, or smoothness on arbitrary `D`.

2. **Existence and actual fixation.** For large `m`, Serre vanishing lifts the
section of `L_B^m` with divisor `m[p0]`, and global generation of
`I_B tensor L^m` supplies a kernel section with nonzero normal coefficient.
A scalar perturbation retains the boundary restriction but makes the divisor
smooth and reduced at `p0`; it also avoids `q` and contains no `B`. Every
global component meets ample `B`, hence passes through `p0`; the single smooth
local branch then forces one global component of multiplicity one. Thus the
curve is integral with one normalization point at infinity, without Bertini
or an `A1` assertion.

Properness of `k` extends its normalization lift. If both polynomial image
coordinates extended over the complete normalization they would be constant,
contradicting quasi-finiteness, so its image has a boundary point. The unique
source infinity and `h^{-1}(B)_red=C` make that point `sigma(p0)`, with no
other boundary point. Since `sigma` is an automorphism of `B`, it preserves
the cusp and smooth locus; Candidate A gives `sigma(p0)=p0`, while the unique
cusp is also fixed. No formal algebraization is used.

3. **Candidate B.** The retained AMPLE calculation gives
`C.Z=-Z^2=(e-1)/(ne)`, hence `C.(nZ)=(e-1)/e<1`. Because `nB` is Cartier,
`nZ=k*(nB)-nC` is an effective integral exceptional Weil divisor. Every
exceptional prime has positive integral coefficient: a local equation of
`nB` vanishes at its boundary centre. Q-ampleness makes each exceptional
curve meet `C`, and `k_C` makes the set intersection a singleton. If `C` were
Cartier there, its trivialization away from its support would make it Cartier
on a neighborhood of the entire exceptional curve. Restriction would be a
line bundle with a nonzero section having a zero, so `C.E` would be a positive
integer. All other terms are strictly positive by Q-ampleness; one Cartier
contact would already make `C.(nZ)>=1`, contradiction. Thus every exceptional
contact is non-Cartier. No ambient smoothness or uniform local-index bound is
assumed.

4. **Exceptional curves and centres.** Resolution, rationality, Leray, and
coherent dimension at most one give `H1` zero for each reduced exceptional
component. Normalization genus plus defect length makes it intrinsically
`P1`, including in singular ambient `W`; removing its unique `C` contact gives
`A1`. Finite `h` maps it to a complete curve with exactly one boundary point
and one normalization place there. Candidate A makes a smooth such point
`p0`; otherwise it is the cusp `q`. Since `sigma` fixes both, every
`k`-exceptional centre lies over `{p0,q}`. This is support only and gives no
bound, common resolution, or iterate stabilization.

5. **Actual affine branches and fixed sheets.** Near `p0`, the finite fibre is
the single point `a`. Remove the full inverse of `B` and every reduced affine
image germ; the normal source-germ complement is one connected degree-`e`
cover. Unique boundary ramification and residue degree one make the
`B`-meridian an `e`-cycle `tau`. For each irreducible affine image equation
`f=0`, dominance makes `f(P,Q)` nonconstant; its zero locus has a curve, and
quasi-finiteness makes a component dominate the image. Its closure is finite
over the complete image. Normalizations cover every place over `p0`, and the
unique `h`-fibre puts all corresponding source points at `a`. Each selected
branch is generically in actual `U`, where the ambient map is etale, so its
meridian fixes a sheet in this same local cover. Different meridians may fix
different sheets; no compatible global labeling is asserted.

6. **Exact remaining gap.** If every affine branch meridian commuted with
`tau`, the cyclic centralizer of an `e`-cycle would make any such fixed-point
element trivial. Filling those trivial-inertia branches leaves the connected
cyclic cover ramified only along smooth `B`; uniqueness of normal finite
extension gives the standard cyclic model and makes `C` Cartier at `a`,
contradicting Candidate B. Therefore actual `p0`-centred escape requires a
nontrivial branch inertia not commuting with `tau`. The report correctly does
not derive commutation from period/intersection classes. Multiple, singular,
or tangent noncommuting configurations and cusp-centred escape remain open.

## Publication custody

ROOT checked exact equality of the exported scientific blocks and retained the original producer and review artifacts.
The following collision output was generated by ROOT from the terminal review and the frozen public corpus; it is not attributed to the reviewer's execution.
EMPTY means that no explicitly raised OPEN entry required a collision comparison, not that the argument is novel.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `2ead4a746396b8a5ec0cb5793c3ef66658bae2b6` (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6749`.
- Body SHA-256:
  `99adb4eb34236942e8374181f4cb9b615be9ea083787e386d8d40e3a2821e82c`.
- Frozen basis: `2ead4a746396b8a5ec0cb5793c3ef66658bae2b6`.
