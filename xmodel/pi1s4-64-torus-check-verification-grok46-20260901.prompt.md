# Verification lane: TORUS-CHECK — computation and countermodel arm

Second arm of the paired review; independent of the gate;
computations and countermodels only.

charged_input=xmodel/pi1s4-64-torus-check-opus5-20260831.md
charged_input=xmodel/pi1s4-64-zvk-u6-opus5-20260831.md
charged_input=xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe  {{LANE_INPUTS}}/pi1s4-64-torus-check-opus5-20260831.md
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  {{LANE_INPUTS}}/pi1s4-64-zvk-u6-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  {{LANE_INPUTS}}/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Targets: (1) re-derive the implicit sextic F_j for TWO explicit
(b,c) values (e.g. (0,1) and (1,1)) by resultant BY HAND (structured
elimination — the resultant of x - r(t)^2 and y - q(t); exploit the
r,q relations from ROW-NF), verify degree 6, the three nodes, and
the A_14 infinity germ on each; (2) test Theorem NO-TORUS
numerically-exactly on both: attempt A^3 - B^2 = c F with
indeterminate coefficients (deg A<=2, deg B<=3: a finite linear-
plus-quadratic system — set it up and refute solvability by exact
elimination at the two parameter points); (3) verify the conic-
criterion count (§2): conics through the three nodes with the
prescribed A_14 intersection — recount the linear conditions;
(4) INF-TRIVIAL's feeds: recompute the discriminant census of the
x-projection for (b,c)=(0,1) (the 11 values, the three simultaneous
tangencies over x=0) directly from dF/dy resultants; verify the
three x=0 half-twists are disjoint transpositions in the fibre
ordering; (5) the Riemann-Hurwitz fibre-line identity in §5.5
(2g-2 = 4(-2)+6+(4-c(Pi))): check both candidate values (2,1) and
(4,0) for consistency with d=2g_L+c(Pi)+2 at d=6 AND with the
promoted degree-4 cover Euler data (chi_c(Y)=3) — which survives
all three constraints?; (6) sanity: apply the whole ROW-KILL chain
shape to the KNOWN-good (4,2) case (where the promoted S_3 collapse
exists): does the machinery reproduce the promoted result without
contradiction? Verdict per target: HOLDS / BROKEN / UNTESTABLE.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1s4-64-torus-check-verification-grok46-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
