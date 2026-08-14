# Task: coefficient-gluing DESIGN for the six td-7 survivor cells

You are GPT 5.6 Sol, primary research, repo /Users/dc/code/math/jc72108
(full read access). Your sixcells analysis (xmodel/sol-sixcells.md,
dual-certified with xmodel/grok-sixcells-review.md) established that the
six td-7 cells survive the local T1 + transport + budget-equality tiers,
and estimated a "reusable honest coefficient-gluing emitter" at 3-5 days.
DC has green-lit the build. YOU write the DESIGN DOC now; a separate
implementation agent will build the emitter from your spec, so precision
and completeness matter more than prose.

## What the design must contain (xmodel/sol-gluing-design.md)
1. THE EQUATIONS: for a route through a cell, the full coefficient-gluing
   system — local Prop. 8.1(iv) data at each vertex, the transport maps
   between consecutive vertices (cite the exact handshake statements:
   SHEET6-DEPTH w-invariant, BOOK-OFFAXIS R2.1/R2.2, case-IV P1 laws),
   and the compatibility conditions that close the loop at the terminal.
   Every variable named, every equation numbered, ground field stated
   (Q(A)? extensions per cell?).
2. INSTANTIATION RECIPE: how to specialize the template to each of the
   six cells x their routes (the 53 routes; note which of the 35
   budget-equality routes share systems after dedup). Expected system
   sizes (vars/eqs) per cell — be honest about the big one
   (39,65,32,13)@7.
3. FALSIFIABLE PILOT: fully instantiate the SMALLEST system — cell
   (9,15,7,3)@2, its direct completion route — by hand in the doc:
   explicit polynomial equations ready for msolve emission (obeying
   AUDIT.md emission rules: expanded monomials, saturation of forced-
   nonzero scales, satisfiability guards, pattern-positive anchor
   candidates). If you can already SOLVE it exactly (sympy-level size),
   do so and state the verdict — a kill here would be the first
   next-tier scalp.
4. SOUNDNESS ARGUMENT: why emptiness of the gluing system kills the
   route (and what nonemptiness does/doesn't mean); which promoted
   results it consumes; wrong-object hazards an implementer must guard
   (chart conventions, level offsets, the M-fold t-ambiguity from
   BOOK-OFFAXIS (c2)).
5. BUILD PLAN for the implementation agent: module layout mirroring
   existing engines (cases/book_offaxis.py style), gate tests (regression
   against the six certified local solutions + the 56 law-dead cells as
   negative controls), fleet emission targets (ops/FLEET.md — solver jobs
   go to Box02/box01, never local).

Label anything unproven **CONJECTURE**. No repo modifications except your
output file. No git. Depth over breadth; the pilot instantiation (3) is
the most valuable single item.
