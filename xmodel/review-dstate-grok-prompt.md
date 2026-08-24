# Hostile review assignment: round-two `D-STATE-GATE`

Work in `/Users/dc/code/math/jc2`.  You are the independent different-model
reviewer.  Review the producer claim in
`xmodel/round2-dstate-gate-20260824.md` and every artifact under
`cases/round2_dstate_gate/`.  Read the relevant banked sources pinned by
`provenance.json`; do not trust prose, stored booleans, or producer code where
an independent derivation is possible.

Your only repository write is `xmodel/review-dstate-grok.md`.  Do not edit any
ledger, case artifact, prompt, run file, or other path.  Scratch work belongs
outside the repository.  Do not use the network and do not launch a solver or
any remote/AWS job.

Audit, at minimum:

1. preregistration chronology, frozen verdict precedence, provenance hashes,
   manifest integrity, and exact replay commands;
2. the corrected 30-input/30-output pure-`y` state, six-band starts, `H_29`,
   first-occurrence layers 26/32/38, coefficientwise projection squares, and
   the claimed Ore-affine identity `M38 - 2*M32 + M26 = 0` at both primes;
3. whether the two source-derivative implementations are genuinely
   independent enough, and independently recompute a representative
   coefficient or matrix relation rather than accepting stored hashes;
4. independently derive the full-source coefficient formula
   `[t^42]E_full = [t^42]E_y + 42*S_M*G_M*(3*alpha1-2*beta1)*p(eta)^4*p'(eta)`
   and verify that both partials are nonzero in characteristic zero and at the
   registered primes;
5. inspect the actual current source constructor/state labels and decide
   whether `alpha1,beta1` are typed as held, derived with a chain rule, or
   independent source coordinates.  Attack the possibility that the claimed
   absence is only a search or naming failure;
6. scope discipline: no band-28 solve, D43, all-depth stationarity,
   Ore/Spencer/Fitting, germ, characteristic-zero, or JC2 inference.

Use one headline verdict: `CONFIRMED`, `CONFIRMED WITH GAPS`, `INCONCLUSIVE`,
or `REFUTED`.  Separate the positive pure-`y` statement from the negative
typing stop.  If confirmed, state exactly what can enter `AUDIT.md`; if not,
give the smallest failing identity/path and blast radius.  Record commands,
independent calculations, artifact hashes, caveats, and an adversarial attack
log.  End only after the report is complete.
