# Hostile review assignment: `P4P1-SOURCE-HONESTY`

Work in `/Users/dc/code/math/jc2`.  Independently audit
`xmodel/round2-p4p1-honesty-20260824.md` and all artifacts in
`cases/round2_p4p1_honesty/`.  This closes a correctness/scope issue raised by
the earlier D43 source/NF review, so do not accept the producer's reassuring
interpretation without checking the actual compiler path.

Your only repository write is `xmodel/review-p4p1-honesty-grok.md`.  Scratch
work belongs outside the repository.  Do not edit ledgers, frozen artifacts,
prompts, or run files; do not use the network, AWS, or a heavy solver.

Audit at least:

1. preregistration chronology, taxonomy, provenance/manifest hashes, and
   byte-replay;
2. independently derive the integer source identity
   `Delta[t^42]E=42*S_M*G_M*(3*alpha-2*beta)*p(eta)^4*p'(eta)` and its ten
   coefficients;
3. inspect and execute the actual `rung_kernel` assembler on empty and real
   checkpoint input, proving or refuting exact subtraction of checkpoint from
   final rows;
4. verify both checkpoint banks really omit the sidecar names and check every
   coefficient's exact normal form through each registered 509-element `I23`
   basis.  Attack ordering/ring-extension mistakes and the claim that constant
   coefficients cannot reduce;
5. independently check the origin `(alpha,beta)=(0,0)`, off-origin `(1,0)`,
   and the asserted zero line `3 alpha-2 beta=0` at both primes;
6. decide whether any prior modular origin/D43 claim used a nonzero sidecar
   value, and whether there is actual wrong mathematics or only an overbroad
   source-provenance slogan;
7. enforce scope: no integral emitter, general D43 nonemptiness, depth,
   compatible tail, germ, characteristic-zero, or JC2 inference.

Use one verdict: `CONFIRMED`, `CONFIRMED WITH GAPS`, `INCONCLUSIVE`, or
`REFUTED`.  If confirmed, state exact clean replacement wording and what may
enter `AUDIT.md`; if not, identify the smallest failing identity and blast
radius. Record commands, hashes, independent calculations, caveats, and an
adversarial attack log.
