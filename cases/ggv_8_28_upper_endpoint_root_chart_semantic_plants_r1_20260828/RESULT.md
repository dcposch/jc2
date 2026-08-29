# Result: PASS on the literal TRIPLE03 root open

## Strict verdict

`TRIPLE03_ROOT_D_DELTA_ENDPOINT_DEAD_WITH_SEMANTIC_PLANTS`

On the frozen literal TRIPLE03 branch `q1=c8=q2=0`, the exact right-kernel
parametrization on the root chart `D(Delta)` has all 21 coefficients of

`E = x14*x72 + x1*x97`

equal to zero after reduction by the pinned branch standard basis. This statement
is only about that open chart.

## Mandatory semantic controls

The retrospective replay passed every fail-closed plant in the same reducer:

- first bordered residual normal form: `0`;
- bordered residual plus `Delta`: nonzero and exactly `NF(Delta)`;
- first diagonal endpoint coefficient: `0`;
- endpoint coefficient plus one: `1`, hence nonzero;
- affine replay `NF(e+1)-NF(e)-1`: `0`.

The actual certificate also replayed 95 rational-unit pivots, 66 complete bordered
`(r+1)` identities, and 636 full 106-row kernel identities with zero failures.
The Singular transcript was diagnostic-free and the worker returned zero.

## Byte agreement with the original bank

- original chart: `0141cffd951fde163341dfa1d835194fce6168f49a91abc3c7171e7342e166d9`;
- regenerated chart delta: `9e07a399764ace2008ad89af5c865326b0cdb65ceab1bcc83f5edcc63463144b`;
- regenerated endpoint coefficients: `a20a6af9de8f45a9b0486827cbc503111c554d6484fae3a59f150b0fbe8b7c28`;
- regenerated bordered identities: `ba2576ce6b4cd9b0344e3a0e1f1246f188d1a7182fb66a4eda186c1dd45ad5cd`.

These are byte-identical to the hashes preregistered from the frozen original
archive. The patched chart, which only adds the semantic-control block, has SHA
`6ef6ffe875d0cead46292a488bb59f979341f11a57d6e68afc5af619f84d67ee`.

## Scope firewall

This PASS does not by itself cover `V(Delta)`. It makes no scheme-theoretic,
nilpotence, radical, other-component, whole-branch, or ambient endpoint claim.
The separately banked closed-complement result is combined only under the precise
assumptions in `UNION_THEOREM.md`.
