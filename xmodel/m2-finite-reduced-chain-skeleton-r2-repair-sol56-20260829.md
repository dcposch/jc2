# Finite reduced P0 chain skeleton R2 repair

Date: 2026-08-29 UTC. Producer: Sol Ultra integration lane. Lifecycle:
`SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`.

R1 theorem report `239393d7...`/body `8587625b...` passed two independent
reviews:

- Fable5 `3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f`
  / body `28fc400c6879a288f3f09a85668d3cd8e56ea88e518dfcdaaa41f26692651320`,
  verdict `PASS_WITH_NARROWING`;
- Grok 4.6
  `bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912`
  / body `c95fbe402dd4d9791290e914f7fbb9d12632400ae898ec2d9cc873db990f86a1`,
  verdict `PASS_AT_STATED_CHAIN_SCOPE`.

The R1 packet is frozen unchanged. R2 copies its mathematics and makes only
two review-requested implementation/test repairs.

## R2 changes

1. `first_predecessor` is now a true minimum-cost witness tree. R1 used
   `setdefault` on the first Dijkstra push, so `(2/9,9)` and `(1/2,1)` could
   retain a more expensive witness while their state-table `lambda_min` was
   correct. R2 tracks tentative best distances and replaces the predecessor
   on every strict improvement. A new gate checks all 151/151 non-root
   predecessor records against finalized costs in the secondary run and all
   68/68 in the charged run.
2. A second charged regression at `(w,M,B)=(2,4,4)` closes the original
   test suite's `lex` blind spot. It records exactly 152 states, 658 expanded
   edges, maximum reduced numerator 8, maximum `M=25`, `max_k=4`,
   `max_lex=2`, derived-lex maximum 99, and state-table hash
   `255f1fe24efce6921703a80155646f5a78f949f678c96043d47c0beec6ddfd7d`.
   A semantic `lex<=0` cap can no longer pass the golden suite.

The original `(3/2,2,B=5)` theorem payload remains 69 states, 295 edges,
maximum numerator 3, maximum `M=25`, and state-table hash
`c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad`.
Only the predecessor portion of its JSON changes.

## Review-derived theorem sharpenings retained

Fable independently derived the resolvent identity

```text
E * (l*a*(1+k+lex) - kbar*d*C) = l*a*T,
```

which proves `E | l*num(w)*T` directly from the integral transport and makes
the cap-free divisor enumeration self-contained relative to P0. Fable also
proved the pure-epsilon phantom-absorption lemma: the exact residue-zero
class always realizes `M'=E`, and every illegal legacy divisor child is a
zero-cost neutral drop from that legal state. This explains why the legacy
and exact reduced maps agree although 41 reachable menus contain legacy
phantom edges. R2 keeps the exact congruence data; it does not copy the
legacy over-emission.

## Replay and hashes

```text
b6f363407af9ea16f83bb5c0b7ff5c659e0e69b372ef2ace47d1f53b8b768afb  finite_chain_skeleton_r2.py
99670c469b66e7639f3046169ca3a7f8bbcda24890b19fe2018674adc23f7e19  test_finite_chain_skeleton_r2.py
f269eaeb33cd5bc5bacdcc6feab803025c4294c720401606ff67dc73c3d2ee5e  README.md
f064e0930dc11d05c7276fa0420418ecf1efc62eed9a9b10a69bc626b88fa558  td7_caseiii_special_nu_r1.py
f4cfa83df42cd38975482160848bc35146f8c26a5c66a7f5b5190638201ab7a8  test_td7_caseiii_special_nu_r1.py
13fc996f56747a8e4b314da42007a15d89604860e3c89ba984fa35d18ee01df4  charged R2 JSON
5eecfc4c7d8478ab78c6a5db0dbb8611e008da452bedf41a8cae5183cf2797d7  secondary R2 JSON
```

`test_finite_chain_skeleton_r2.py` passes 46 checks under ordinary and
optimized Python. The unchanged td-7 special-consumer suite passes 17 checks
in both modes. No heavy computation or CAS ran.

## Scope

R2 does not broaden the reviewed theorem. It covers reduced P0 chain states
only. Last-vertex indices, full cell degrees, merge families, generic-AP
consumer uniformity, landing, realizability, a cofinal degree ceiling, and
JC2 remain outside. No AWS action is associated with this packet.

---
Report-body SHA-256 (bytes before the separator line above): `995f310e19c20e373280c5328805f2261249150c9d0cb45d813107fa9c3f90c4`
