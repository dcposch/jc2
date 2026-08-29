# Review request: D43 exact sparse row producer

Please review before any AWS launch or fanout.

1. Verify the source support map, especially the ten `x*` to shallow-tail
   names, and confirm that the two modular certificates have exactly this
   support with alpha and beta zero.
2. Verify the source-first pin semantics: all complement variables are
   substituted before jet multiplication, while the fixed B-orbit constants
   remain present.
3. Compare `selected_source_rows` componentwise with
   `directionb_strike.jrows`; check the `+42` sign and placement.
4. Review the canonical semantic encoding down to normalized `Fraction`
   pairs in every `K3` coefficient.
5. Verify that band 20 is compared exactly, not modulo a prime, with the
   support-specialized D21 source bank.
6. Attack the sentinel, PIN42, pure-y, alpha/beta, W/E5, checkpoint-hash,
   atomic-write, resource, registration, duplicate-target, and missing-cover
   gates.
7. Confirm that the recorded G0p2 checkpoint cannot enter the dormant
   full-checkpoint lane and that a fresh manifest is required after GB21
   exists.

Maximum promotion after a successful pilot: **exact support-specialized
band-20 source emission with D21 equality**.  No point-existence or JC2 claim
is licensed.
