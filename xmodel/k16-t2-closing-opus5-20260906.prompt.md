# K16 UNIFORM test lane (two finite checks at t = 3, 4 that decide two uniform conjectures): the K16 ray's uniform statement (R) is equivalent (tacnode report) to the vanishing of the 4-jet quadratic T₂ = 3b²w₃ + 18B·w₂ − 10η² on every terminal datum, and the universal-series report gives the degree-N closing conditions Φ_{2N+1..4N}. CONJECTURE 1 (closing in (T₂)): the degree-N closing lies in the ideal (T₂) — check at t = 3, 4 from the frozen exact bases (box/k16xempty-20260905/controls_t{3,4}_raw.sing, identity map on (c_i, b), minpoly 3d² − N): eliminate to the 4-jet and compare with (T₂) (non-vacuous against the socle degrees 14/21); test l_{N+1} ≡ 0 mod T₂ in free jets; a nonzero remainder refutes it (type OPEN[K16-CLOSING-NOT-IN-T2]). CONJECTURE 2 (attainment leader): on the K16 terminal datum (a 3:2-type pair with 16-approximate root h, F = h³ + …, G = h² + …), Theorem A of the char-degree report (charged) gives a t-uniform NECESSARY condition never used on the ray: the second characteristic polynomial T₂^{char} of Prop 3.1 attains its degree D₂ with a unit leader λ. Compute λ in the ray's jets (b, B, η, l_j, w_j) at t = 3, 4 (and 5 if cheap) from the same frozen bases and test: is λ a unit multiple of the obstruction — does λ vanish on the terminal cone exactly where Bη does, and is the 4-jet quadratic T₂ (a factor of) the leading attainment row? If YES at t = 3, 4: state precisely what remains for a uniform proof (the identification for all t is then a symbolic identity in the universal recursion — attempt it symbolically in N); if NO: record the exact discrepancy. Either way ADD the attainment rows to I_{t,+} at t = 3..6 and report whether they cut the terminal cone to {Bη = 0} (a finite computation per t). FALLACY-v2 (a finite-t identity is not a theorem; state the universal-recursion identity needed). DISK DISCIPLINE: the host has ~3 GB free — write only the report and JSON ≤ 1 MB; no artifact trees, no CAS dumps; check `df -h /` before any write > 10 MB. ≤ 180 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/k16-t2-closing-20260906/.
Report: xmodel/k16-t2-closing-opus5-20260906.md
Seal (<!-- BODY-END -->); 10-25KB; 180 min.
charged_input=xmodel/k16-tacnode-fable5-20260905.md
charged_input=xmodel/k16-universal-series-fable5-20260905.md
charged_input=xmodel/char-degree-instrument-astra-r2-20260905.md
charged_input=xmodel/k16-xempty-astra-20260905.md
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k16-t2-closing-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
ab1c4ca249f85f3978108fe9e26f391695805e443fdb51a6be135635b2a0fa31  {{LANE_INPUTS}}/k16-tacnode-fable5-20260905.md
5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb  {{LANE_INPUTS}}/k16-universal-series-fable5-20260905.md
d9b95ce9c4588104c9f306d987f91957988611b80d2025a05f14c40568e33b45  {{LANE_INPUTS}}/char-degree-instrument-astra-r2-20260905.md
1f06694fb58d53c4a4b3c54dad88722cd31a5ccc894679ac52b0620b91e2623f  {{LANE_INPUTS}}/k16-xempty-astra-20260905.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
