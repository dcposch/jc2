# Research lane: connectedness of the general coordinate fibres

You are a bounded primary research lane. A producer-side pre-review found
that the wild-valuation packet's Riemann--Hurwitz accounting (2.5), the
tuple identity (3.2), the four-row partition table, and the closures (3.6)
all silently assume the general coordinate fibre `C_f = V(f - a_f)` in
`S = Spec R`, `R = C[A,U,Z]/(U^2-A-A^2Z)`, is connected (equivalently
geometrically irreducible). Your job is to prove or refute that
connectedness in the charged scope, then restate the repaired identities.
Do not edit canonical ledgers, any charged file, or inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-hostile-review-grok46-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`; verify these
SHA-256 hashes first and stop on mismatch:

```text
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
8abde87c3e9320ae1b75e90d4c4c26e4a7a16dc685398bf446b5b33b230f9787  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
d5fa676a7c364bb8cbc470a2a912be995456ba98cea7a9d4943044844f73b97a  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-hostile-review-grok46-20260831.md
```

The charged hypotheses are those of the valuation packet: `f,g in R` with
`{f,g} = kappa in C^*`, `[Frac(R):C(f,g)] = 4`, the promoted Poisson
parent (both flows non-locally-finite, hyperbolic generic coordinate
fibres), and the reviewed boundary census (finite normalization `Y -> A2`,
`S = Y - R_bd`, etale `pi|_S`, cofinite image, irreducible `B` with
generic fibre `(2,1,1)`, unique `(3,1)` cusp, unique omitted `(2,2)`
node).

Task, in order:

1. Prove or refute: the general fibre `C_f` is geometrically irreducible.
   The pre-review sketches the intended proof (its §5): a nontrivial
   relative algebraic closure of `C(f)` in `Frac(R)` would force
   ramification over a finite value of `f`; etaleness on `S` pushes that
   ramified sheet into the boundary; finiteness of `Y -> A2` would then
   create a boundary divisor mapping onto a vertical line, contradicting
   the sole irreducible nonvertical boundary image `B`. Make every step of
   this exact — in particular why the relative closure ramifies at all
   (Stein factorization / the primitivity of `f`), why a vertical
   boundary image is actually excluded by the charged census, and what
   happens at the finitely many bad values of `a_f`. If a step genuinely
   needs an unavailable input, type it `OPEN` precisely.
2. Do the same for `g` (by symmetry, but state what breaks if anything).
3. Restate the repaired versions of (2.5), (3.2), the four-row table, and
   (3.6) — under your connectedness theorem if proved, or in the honest
   multi-component form (with `delta_h` components and total genus `G_h`)
   if refuted or `OPEN`. Include the pre-review's missing consistency
   clause: a supplied `gamma_h` must satisfy `gamma_h=(d_h-r_h-2)/2`.
4. Adopt the pre-review's two other corrections in your statement of the
   packet's surviving content: the narrowed cusp-companion claim (the
   unmarked formal conjugacy class cannot detect wildness; marked
   generator expansions can), and the provenance note on (2.6).

Computation rules: desk-scale exact algebra only. Never run Singular,
msolve, any CAS, or any computation of uncertain duration or memory on
this machine. Six hours is your hard budget; bank partial exact lemmas
rather than overrunning.

Write one report and no other file:

```text
xmodel/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your first
action and append each completed section as you finish it. Keep it under
roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Include a `charge_basis` declaration only if you assert a genuinely new
exit price with a direct mathematical-source citation; otherwise omit it
entirely.
