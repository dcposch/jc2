# Research lane: PI1-S4 — the last bit of rank four

You are the campaign's flagship proof lane. Everything left of the
rank-four (M) programme rides one question (integration §2):

> **(PI1-S4)** Let `D ⊂ C²` be an irreducible polynomial curve
> (normalization `A¹`, ONE place at infinity) whose every affine
> singularity is a double point of two smooth branches (tangency
> allowed, type `A_{2k-1}`, k>=1). Can `π₁(C² − D)` surject onto
> `S_4` sending every meridian of `D` to a transposition, with the two
> local meridians at each double point mapping to DISJOINT
> transpositions?

NO closes B0 at N=4 unconditionally, promotes `A_F=B` at rank four,
and completes the promoted (M) programme in both monodromy classes.
YES must come with an explicit candidate curve and representation —
that would be structured progress toward the counterexample side.
Fail closed: a typed OPEN naming the exact missing input is a good
outcome; unconditional partial results are valuable.

charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
charged_input=xmodel/b0-proof-hostile-review-sol56-20260831.md
charged_input=xmodel/b0-pi1-acquisition-grok46-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
8ffc0a06edcf2be3908b1486da57e7d4a024973e679f9d25577cc281ef005320  {{LANE_INPUTS}}/b0-proof-hostile-review-sol56-20260831.md
cd503e487e3b5277519e4d0668de2d6ca69b0f4002405bfb406cce17df6e3b82  {{LANE_INPUTS}}/b0-pi1-acquisition-grok46-20260831.md
```

Additional constraints you may consume (promoted, integration §1.5):
in the campaign application `D = D_1` also satisfies: it carries a
degree-4 `S_4`-cover datum coming from a Keller map with a SECOND
polynomial curve `D_0` disjoint from `Sing D_1`, the cover is etale
over `C² − D_1` with meridian cycle type `(2,1,1)`, and over generic
`p ∈ D_1` there are exactly `a=2` affine points... careful: over `D_1`
the count is `a_{D_1}=2` with one boundary point of `e=2`. Use these
only if helpful — the clean question above suffices.

Attack routes, in order of expected decisiveness:

1. **Global braid relation at infinity.** `D` is a polynomial curve:
   one place at infinity. For such curves the braid monodromy at
   infinity is constrained (the product of all local braids equals the
   full twist `Δ²_d` at infinity for a degree-`d` curve — write the
   affine version precisely). At each `A_{2k-1}` double point the
   local braid is `σ^{2k}`; smooth branch points contribute nothing;
   the place at infinity absorbs the rest. Determine what the product
   relation forces on a transposition-valued representation with
   disjoint images at every double point: disjoint transpositions
   commute, so every local braid image is TRIVIAL — hence the image
   of the full twist must be trivial; compute the image of the full
   twist / infinity braid under the representation directly (it is a
   specific central-ish element; for a degree-d curve with one place
   at infinity the local knot at infinity is an iterated torus knot —
   its braid word is explicit from the Puiseux pair data, and
   Abhyankar–Moh rigidly constrains those pairs for polynomial
   curves). This is the route the acquisition typed as "where the
   answer lives".
2. **Nori's inequality after resolving infinity** (acquisition ledger:
   nori_ens1983.pdf, Thm 3.27 and its local refinements): compute the
   self-intersection of the strict transform of `D̄` after resolving
   ONLY the place at infinity, in terms of `d` and the Abhyankar–Moh
   semigroup; determine for which semigroups `C̄² > 2·(number of
   double points)` holds — the promoted fibre data bound the double
   points via the (M')/Euler identities (under H2+H3 machinery on
   `D_1` inside the residual configuration: `ν = s` since all double
   points, and the aggregate identity pins `s` — derive the exact
   count). If the inequality holds for every admissible semigroup,
   Nori gives abelianness and NO follows.
3. **Orevkov negativity at infinity** (Math. USSR Sb. 65 (1990);
   acquire the actual PDF — the acquisition lane found the author
   site 504'd; try Math-Net.Ru, library genesis mirrors are NOT
   permitted, use official sources only; if unobtainable, type the
   statement as unverified and do not consume it).
4. **Direct ZvK.** If 1-3 all leave a gap, run Zariski–van Kampen on a
   generic vertical pencil for a general member of the class: generators
   = meridians in one fibre; relations from double points (re-derive
   the `A_{2k-1}` local relations YOURSELF — the acquisition's claim
   that disjoint transpositions satisfy them is a flagged inference,
   verify or refute it first, k=1 and k=2 explicitly) and from the
   place at infinity. Determine whether `S_4`-surjectivity with the
   prescribed local images is consistent.

Route order matters: route 1's triviality-of-local-images observation
composes with any constraint on the infinity braid image — if the
infinity image must be a nontrivial element of the subgroup generated
by the meridian images, NO follows immediately; make that precise
first. Pin every literature statement (page, theorem number, PDF
hash). Deliverable: theorem NO (with proof), structured YES candidate,
or typed OPEN with the exact missing local/global input and all
unconditional partials proved.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1-s4-decision-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Include a `charge_basis` declaration only if you assert a genuinely new
exit price with a direct mathematical-source citation; otherwise omit.
