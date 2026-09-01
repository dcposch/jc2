# Systems lane: CHARP-PREFILTER — modular evidence for the two timeout types

You are a systems/preparation lane. Types (8,6,7) [C] and (8,6,3)
[D] timed out at 3h in char 0 and are rerunning at 12h caps; a
char-p prefilter gives fast independent evidence and can decide
EMPTY outright (an ideal empty mod several large primes AND in a
degeneration-compatible way is strong evidence; an ideal NONEMPTY
mod p with a smooth point lifts by Hensel under conditions you must
type precisely — a modular point does NOT prove char-0 nonemptiness
without a lifting argument; type the exact logical value of each
outcome, no overclaim). Deliverables: msolve jobs for I_C, I_D mod
three large primes (2^31-ish, msolve -p syntax verified against
fetched docs), the interpreter (GROEBNER-mode conventions — basis
[1] = EMPTY mod p), a driver, verdict rules with the honest
typing (EMPTY mod p for a single prime does NOT imply char-0
EMPTY — but char-0 NONEMPTY implies NONEMPTY mod almost all p, so
EMPTY mod 3 independent primes is contrapositive evidence typed as
STRONG-EVIDENCE-EMPTY, never a verdict), and SHA-256 manifest.
Dialect checklist pass mandatory. Also include (separate section) a
one-file fix spec for the braid job's argument-dispatch bug (read
its driver.log/meta on the box is not possible from this lane —
spec the diagnostic steps for the coordinator instead).
charged_input=xmodel/msolve-prep-realization-grok46-20260831.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
64e451b44a421ca8efbd9d5fd553fd43cc2fb7afe6415ab760aab9ac47c27ef4  {{LANE_INPUTS}}/msolve-prep-realization-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Desk-scale exact reasoning only; fetch/hash literature as needed; no
CAS. Do not edit canonical ledgers, any charged file, or inspect
`jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/charp-prefilter-grok46-20260901.md
```

Skeleton first WITHOUT the BODY-END marker; bounded per-section
writes (under 1,500 words each); seal only at completion; if budget
runs short, type the rest OPEN then seal. Under 5,000 words. No
charge_basis.
