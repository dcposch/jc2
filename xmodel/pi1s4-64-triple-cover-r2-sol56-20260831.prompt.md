# Research lane: TRIPLE-COVER — the resolvent cubic kill of the (6,4) row

You are a bounded primary research lane on
OPEN[PI1S4-(6,4)-TRIPLE-COVER] (charged FIXED-TUPLE report §9): the
resolvent `S_4 -> S_3` (kernel V) turns a hypothetical
`φ: π₁(C²−D) ↠ S_4` (meridians to transpositions, disjoint at the
three nodes) into a simply-branched connected triple cover of `C²`
branched over `D`, in which the two disjoint node transpositions map
to the SAME S_3 transposition. Over `C²` every finite flat cover
trivializes projectively: the cover is a global cubic
`z³ + a(x,y) z + b(x,y)` with discriminant `−(4a³ + 27b²) = c·f`
(f the sextic defining D, c a constant), forcing `deg a <= 2`,
`deg b <= 3`, and on the degree-6 leading forms `4a₂³ + 27b₃² = c·(y-form)⁶`-type
identities (the charged report displays `4a_2^3 + 27b_3^2 = c y^6`
in its normalization).

Task, fail closed: (1) re-derive the reduction (why is the triple
cover free/global-cubic over C²? — trivial Picard + the
simply-branched structure; why is the branch divisor exactly D with
multiplicity one and the discriminant identity as displayed; what
does S_3-connectivity force); (2) solve the leading-form identity
`4a₂³ + 27b₃² = c·L⁶` (L linear) over C: classify all `(a₂, b₃)` —
this is a binary-form Diophantine identity (essentially the syzygy
of the cubic discriminant); determine whether solutions force
degeneracy (e.g. a₂, b₃ proportional to powers of L, making the
cover's discriminant a perfect power at infinity — then compare
with the REQUIRED infinity type of the row: Δ=(6,4,3), β₁=15,
δ_∞=7 — derive the discriminant curve's Puiseux data at infinity
from `z³+az+b` with a,b polynomial and check compatibility);
(3) the affine constraints: f has exactly three nodes; the
discriminant of a cubic has cusps where a=b=0 generically — a
NODAL discriminant is special: derive the condition (the
discriminant curve of `z³+az+b` has a node iff ... work it out:
nodes of disc correspond to parameters where two distinct
simple-ramification sheets collide — a=0,b=0 gives a cusp;
transverse a,b vanishing patterns give which singularity?);
(4) verdict: row KILLED (the identity system is inconsistent),
SURVIVES (exhibit the consistent (a,b) family — a MAJOR structured
step toward a counterexample: the cubic cover would be one explicit
polynomial identity away from a Keller-adjacent object; report its
full data), or OPEN at a named step.

Quantification discipline: this route, if it kills, kills EVERY
curve of the row carrying the S_4 representation (the reduction
uses only φ and D's numerics), independent of the fold structure.
charged_input=xmodel/pi1s4-64-fixed-tuple-opus5-20260831.md
charged_input=xmodel/row-sweep-sol56-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch (r2 note: the
r1 lane mis-listed the inputs directory and aborted; the receipts show
all three frozen copies present — list the directory carefully before
concluding a file is absent):

```text
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  {{LANE_INPUTS}}/pi1s4-64-fixed-tuple-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  {{LANE_INPUTS}}/row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 5 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-triple-cover-r2-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
