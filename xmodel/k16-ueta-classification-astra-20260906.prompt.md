# PROOF LANE (≤ 180 min) — the K16 whole-ray obstruction is now ONE precise statement (frozen k16-utac report §8): U_η: for every actual degree m ≥ 4 and every coefficient-field factor of Q[d]/(3d²−m), there is NO zero of the reconstructed polynomial-solution ideal K_m of the universal ODE (UF) with b·η_m ≠ 0; the sufficient stronger form: the ONLY nonconstant polynomial solutions of (UF) with b ≠ 0 and actual degree ≥ 4 are the two proved families C₃ = {L = −1 + a·x³, P = −L²/4} and C_B = {L = −1, P = −1/4 − B·x} (i.e. none of actual degree ≥ 4 at all). The truncated-series route has two identified gaps (η ≠ 0 ⇏ u ≠ 0; free growing P-list). TASK: PROVE the classification by a route that sees the WHOLE polynomial, not a truncation: (A) Newton-polygon / degree-balance of (UF) at x = ∞: write (UF) with θ = x d/dx, compare leading terms of L, P of actual degrees (a,c) with b ≠ 0 and show the degree balance forces the two families (this is the classical way polynomial solutions of an algebraic ODE are classified — the leading-coefficient equation at ∞ must be consistent); handle every case of the leading exponents including cancellations and the coefficient-field factors of 3d² − m; (B) if (A) leaves cases, use the Euler-derivation/weight structure to reduce them to finitely many exact computations and DO them (exact-Q, Singular/msolve local — no fleet); (C) the (BOUNDARY) implication at b = 0: from Xempty §7.3's separate b = 0 treatment, show B·η ∈ √J_t on the b = 0 stratum too (or state exactly what is missing); (D) if U_η is proved with (BOUNDARY), state THEOREM (T) for the WHOLE K16 ray with the full dependency chain (§9) and mark every link with its frozen source; if not, give the exact residual statement. Output must be a proof text with the (UF) equation written out explicitly and every degree case listed — FALLACY-v2 (a finite-index equality is not a uniform statement; a modular result is a signal). DISK: report ≤ 1 MB; host writes ≤ 2 MB; no fleet; no ledger edits; no jc2-lean; no ideation-* input. Notes to box/k16-ueta-20260906/.
Report: xmodel/k16-ueta-classification-astra-20260906.md
Seal (<!-- BODY-END -->); 12-24KB; 180 min.
charged_input=xmodel/k16-utac-astra-20260906.md
charged_input=xmodel/k16-t2-closing-opus5-20260906.md
charged_input=xmodel/k16-universal-series-fable5-20260905.md
charged_input=xmodel/k16-tacnode-fable5-20260905.md
charged_input=xmodel/k16-xempty-astra-20260905.md
charged_input=xmodel/k16-radical-steps-grok46-20260906.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k16-ueta-classification-astra-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
a37f89f6c0583df4d5fe6eb8f125f5cb54f880205eca32a5204ac9992ed16e81  {{LANE_INPUTS}}/k16-utac-astra-20260906.md
2294486a92148654ff13930dcc3a8732684cb8e48097a37387247527a90d249d  {{LANE_INPUTS}}/k16-t2-closing-opus5-20260906.md
5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb  {{LANE_INPUTS}}/k16-universal-series-fable5-20260905.md
ab1c4ca249f85f3978108fe9e26f391695805e443fdb51a6be135635b2a0fa31  {{LANE_INPUTS}}/k16-tacnode-fable5-20260905.md
1f06694fb58d53c4a4b3c54dad88722cd31a5ccc894679ac52b0620b91e2623f  {{LANE_INPUTS}}/k16-xempty-astra-20260905.md
ebd1dfd57a7b17c0bad7414a222a14ca35d7f5f2a83bfd456f8f380f3289c528  {{LANE_INPUTS}}/k16-radical-steps-grok46-20260906.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
