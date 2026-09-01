# Systems lane: POINT-POSTCHECK — extraction + repaired postcheck bundle

You are a systems/preparation lane. The (8,6,11) and (8,6,9)
characteristic ideals are validated NONEMPTY (proper Groebner bases;
generator systems symbolically cross-checked between encodings).
Realization now needs: (a) closed-point extraction from each
variety (rational or algebraic points; the ideals live in
QQ[B,C,D,E,F,G,b,gam,d,e,f,u] with the Rabinowitsch u), and (b) the
nodal postcheck (reduced I_DP of length delta_aff, immersive,
distinct tangents, no triple fibre, gcd-cover exclusion) run on the
extracted points.

Produce the complete job bundle (fenced files + SHA-256 manifest),
applying EVERY dialect lesson from this campaign's suite runs —
list them explicitly in a preamble and check your code against
each: (1) no M2 reserved names (pi, gamma, I as locals...); (2) no
tower-ring numgens assumptions — use flattened rings built ONCE
before any symbol use, or explicit `use`; (3) coefficient extraction
via the SOURCE ring's variable, never a rebound global; (4) diff(var,
poly) argument order; (5) `first degree` for ring-element degrees;
(6) no underscore-subscript identifiers; (7) msolve GROEBNER-mode
output conventions ([1 = unit ideal = EMPTY; proper basis =
NONEMPTY) — the interpreter must read basis data, not solver
conventions; msolve solve mode (-P?) conventions verified against
fetched docs for the point extraction. Deliverables: extraction
scripts (msolve solve-mode where 0-dim; otherwise an M2/sage
rational-slice script with a certified fallback), the REWRITTEN
idp_postcheck (self-test on the (6,4,3) witness + (t^8,t^6)
rejection), a driver with caps and a summary table, and exact
verdict rules (REALIZED / NON-REALIZABLE / UNDECIDED per point and
per type). No execution here.
charged_input=xmodel/nodal-realization-86-96-grok46-20260831.md
charged_input=xmodel/msolve-prep-realization-grok46-20260831.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08  {{LANE_INPUTS}}/nodal-realization-86-96-grok46-20260831.md
64e451b44a421ca8efbd9d5fd553fd43cc2fb7afe6415ab760aab9ac47c27ef4  {{LANE_INPUTS}}/msolve-prep-realization-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Desk-scale only; no CAS. Do not edit canonical ledgers or inspect
`jc2-lean`. Four hours hard budget.

Write one report and no other file:

```text
xmodel/point-postcheck-bundle-grok46-20260901.md
```

Skeleton first WITHOUT the BODY-END marker; bounded per-section
writes; seal only at completion. Under 7,000 words. No charge_basis.
