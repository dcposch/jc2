# URGENT audit lane: ENCODING-FAITHFULNESS — are the six characteristic ideals faithful?

You are a high-priority audit lane. ALL SIX realization verdicts
(the two (9,6) KILLED, the two (8,6) NONEMPTY, the two pending) hang
on whether the generated characteristic ideals faithfully encode
their delta-sequence types. New COMPUTED EVIDENCE of a possible
unfaithfulness: generic sliced points of BOTH type86_A (target:
one-place Delta=(8,6,11), delta_inf=10, delta_aff=11) and type86_B
(target: (8,6,9), delta_inf=11, delta_aff=10) yield honestly NODAL
curves with REDUCED ordered double-point schemes of degree exactly
30 — i.e. delta_aff = 15, hence delta_inf = 6 — the WRONG split for
both types, and 15 = delta consistent instead with a TWO-place
infinity (gcd(8,6)=2: the one-place condition is exactly what the
h-conditions were meant to force). A concrete witness point (11
number-field coefficients, quadratic field) is charged.

charged_input=xmodel/type86A-sliced-witness-pt0.m2.txt
charged_input=xmodel/msolve-prep-realization-grok46-20260831.md
charged_input=xmodel/nodal-realization-86-96-grok46-20260831.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
475ca486f3e2eed4a71e842dbe4f16ad9db43efd46c19a9318c22490e0d1010e  {{LANE_INPUTS}}/type86A-sliced-witness-pt0.m2.txt
64e451b44a421ca8efbd9d5fd553fd43cc2fb7afe6415ab760aab9ac47c27ef4  {{LANE_INPUTS}}/msolve-prep-realization-grok46-20260831.md
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08  {{LANE_INPUTS}}/nodal-realization-86-96-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Tasks, fail closed: (1) re-derive from first principles (AG-S /
Abhyankar-Moh, the campaign's promoted cluster identities) the exact
dictionary between the h-coefficients of the Tschirnhausen chart
(as defined in the msolve-prep §2 shared chart) and the
delta-sequence / one-place / beta_1 data: WHICH h-vanishings +
which open condition force one place with Delta=(8,6,beta_1)?
Verify or refute the six generated ideals' encodings against the
dictionary — indexing errors (h_k off by one level), missing
one-place conditions, and wrong open conditions are the suspects;
(2) DESK-CHECK THE WITNESS: from the charged point's 11 explicit
coefficients build p(t), q(t) and compute the infinity structure by
hand/Puiseux (mult-2 leading behavior: is it one place or two? what
beta_1?); its delta_aff = 15 is machine-computed (reduced, 15
nodes) — verify the genus split for whatever infinity structure you
find; (3) verdict per ideal: FAITHFUL / UNFAITHFUL (with the exact
correction) — and re-type all six suite verdicts accordingly: which
of KILLED/(9,6), NONEMPTY/(8,6) survive, which must be recomputed
with corrected ideals (spec the corrections precisely for a rerun).
Note: the (9,6) kills were EMPTY verdicts — an unfaithful ideal that
is EMPTY kills only its (possibly wrong) encoding; type carefully
what EMPTY proves under each faithfulness outcome.
<function hdr at 0x1029e3320>
Desk-scale exact reasoning; no CAS. No ledger edits; no jc2-lean.
Five hours hard budget.

Write one report and no other file:

```text
xmodel/encoding-faithfulness-audit-sol56-20260901.md
```

Skeleton first WITHOUT the BODY-END marker; bounded per-section
writes; seal only at completion; budget-short => OPEN then seal.
Under 6,000 words. No charge_basis.
