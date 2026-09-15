# Hostile review: disjoint branch divisors and translated Keller fiber products

Reviewer: swarmHQ Sol (gpt-5.6-sol). Reviewed frozen commit
`4e5fc9305f329568de5383f310bc37ccd555cd49`, report
`xmodel/disjoint-branch-translates-swarmHQ-root-20260915T093700Z.md` (full SHA-256
`ec07f8e07830fe297cb79033abe0a37476aa9fa833526a653ad709e775d2b87e`).
Evidence: MANUAL, with standard-theorem/PRIMARY-RELATIVE limitations below.
Lifecycle recommendation: independent FIRST for the algebraic theorem at its stated
conditional import scope; the Chau source premise remains PRIMARY-RELATIVE here.
This is not a JC2 proof or a source-proof audit.

## Verdict claim by claim

1. **CONFIRMED (BOOK/standard-theorem-relative).** If the reduced branch divisors
   of the two finite Galois normalizations have no common component, then `X_t` is
   nonempty, smooth, and irreducible. I independently reconstructed the valuation,
   field, and actual-ring arguments below; none uses model agreement.
2. **CONFIRMED conditional on the cited Chau theorem; source attachment GAP in this
   lane.** Given that a nonsingular plane polynomial map cannot have an `A^1`
   component in its nonproper-value set, the exceptional translations are contained
   in a set of size at most `r(r-1)+1`. The primary body was not independently
   available/read in this no-source lane, so I do not upgrade the quotation or its
   hypotheses beyond PRIMARY-RELATIVE. Local history (`notes.md:22448`) records a
   prior complete-body read of arXiv:0710.5212, but that record is comparison
   evidence, not my own primary verification.
3. **CONFIRMED (BOOK/standard-theorem-relative).** If `D` is empty, then `F` is an
   automorphism. The conclusion uses triviality of connected finite etale covers of
   complex affine space plus Zariski Main/Hartogs extension. The report correctly
   draws no conclusion about `X_0` when `D` is nonempty.

## Independent hostile reconstruction

Write `A=C[z1,z2]`. The two actual source rings are polynomial rings equipped with
different `A`-maps: `z |-> F(p)` and `z |-> F(q)+t`. Constant nonzero Jacobian makes
both maps etale, hence flat; their generic rings are the finite separable fields
`L` and `L_t`. The sign is correct: ramification of the second cover occurs where
`z-t` lies in `D`, namely on `D+t`.

Put the two Galois closures in one algebraic closure and set `E=M intersect M_t`.
At every height-one prime of `A`, disjoint branch support makes at least one of the
two Galois extensions unramified at every prolongation. Since `E` is a subextension
of both, it is unramified there. The intersection of finite Galois extensions is
Galois. Purity then makes the finite normalization in `E` etale over all `A^2`;
connectedness of that normalization and topological simple connectedness of
`C^2` force degree one. Thus `E=K`, the Galois closures are linearly disjoint, and
so are their subfields. Consequently `L tensor_K L_t` is a field.

This generic statement really attaches to the source. The coordinate ring
`C_t=C[p] tensor_A C[q]` is flat over the domain `A`, so it injects into its generic
localization, the field above. Hence `C_t` is a domain: there is no torsion-supported
vertical component. Smoothness follows because the fiber product is etale over a
smooth source. Nonemptiness can also be checked without finiteness: each dominant
etale map has image containing a dense open, and two translated dense opens meet.

For the finite bound, `D` lies in `A_F`: over the complement the original cover is
finite etale and its Galois normalization remains etale. Since both are curves, each
irreducible `D_i` is a component of `A_F`. Conditional on the cited no-`A^1`
theorem, each `D_i` has trivial translation stabilizer: a curve invariant under a
nonzero vector contains the Zariski closure of every integer orbit, an affine line,
and irreducibility/dimension makes it that line. Each ordered pair `(i,j)` therefore
contributes at most one translation; all `r` self-pairs contribute only zero. This
is exactly `r(r-1)+1`, including `r=1`, and is only a containing set.

When `D` is empty the same purity argument gives `M=K`, hence `L=K`. A birational
etale quasi-finite map is an open immersion by Zariski Main. A missing divisor would
pull a defining polynomial back to a nonconstant unit, impossible on `A^2`; across
a codimension-two complement the inverse coordinates extend on the normal target.

## Negative controls and excluded conclusions

- Dropping characteristic zero fails exactly as reported: `(x,y)|->(x^p-x,y)` has
  Jacobian `-1`, empty branch divisor, and translated fiber products split into `p`
  affine planes. This tests the finite-etale/simple-connectedness import.
- Using `L intersect L_t=K` without Galois closures would not imply linear
  disjointness; the proof correctly works in `M,M_t`.
- Allowing a translation-invariant branch component destroys finiteness: an affine
  line has a one-dimensional translation stabilizer. The no-line premise is thus
  load-bearing, not cosmetic.
- Common intersection points of `D` and `D+t` do not matter; purity is controlled by
  height-one/common-component ramification.
- At `t=0`, if the generic degree exceeds one, the diagonal is clopen and the
  off-diagonal locus is nonempty. Therefore generic irreducibility, the finite
  exceptional containment, and this review do not prove zero-fiber connectedness,
  properness, an `A^2` generic fiber, or JC2. No characteristic-positive or uniform
  bound on `r` is obtained.

## Evidence and lifecycle

Manual review ran September 15, 2026 from 09:46:21 UTC. Before reading the report I
verified its artifact against expected basis
`18acf7b12245b8eaf2f419a031ea01e7d16f18c1` and manifest SHA-256
`317b90414968f665b7fea8264d9f50c9af3b4dade03a9376dc78da7cd4477a40`;
report and manifest were mode `0444`. Whole-read pre/post report hashes were the
unchanged expected full hash above. No network, CAS, exact-science Python, worker,
paid tool, or descendant was used. Python was used only for the trusted artifact
lifecycle. Standard purity, finite-etale-cover, Zariski Main, and Hartogs facts were
not independently source-audited and remain BOOK-relative. The Chau import remains
PRIMARY-RELATIVE for the reason stated above.

For priority comparison only, ROOT separately reported that Streeter (2021),
Lemma 2.8, uses the same common-subextension ramification mechanism for finite
covers of `P^1` with disjoint branch loci. I did not retrieve that source, it is
not an input to this proof, and it supports retaining `Novelty UNKNOWN` rather than
claiming a new general mechanism. The present plane application, actual-source
flat injection, and finite translation count were compared on their own merits.

## COLLISIONS

status: EMPTY

- NONE -- trusted `ops/open_collision.py` found no explicit `OPEN[...]` entry.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6867`.
- Body SHA-256:
  `265c29781135dffa2bb128ae1c30274a4b8a80d3df3fb605b479af02fb236e58`.
- Frozen basis: `4e5fc9305f329568de5383f310bc37ccd555cd49`.
