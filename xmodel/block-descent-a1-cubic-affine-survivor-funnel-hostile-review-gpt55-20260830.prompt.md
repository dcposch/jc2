# Hostile review: proper-cubic affine-survivor funnel

You are GPT-5.5 acting as a fresh hostile reviewer for the plane Jacobian-
conjecture campaign. Work in `/Users/dc/code/math/jc2`. Reconstruct every
claim independently and seek explicit counterexamples, especially to the
companion-section and smooth-branch arguments. Do not modify charged inputs,
Git state, canonical ledgers, or unrelated files. Do not read any sibling
external-model prompt, log, report, or receipt. Do not inspect, list, search,
stat, build, modify, or control `jc2-lean`.

Hash-check and audit only these charged repository files:

```text
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
a38d1ba420fa8388fbf453051bd9d570edbfe99f0a1ff240f1f297d1e6718fcd
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md.artifact.json
aa198a357ce3c7dd3df6c97019f76553f27c76e5f4b7928ed3e52104de3f3915
  ops/block_descent_a1_cubic_affine_survivor_replay.py
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db
  refs/jc86.pdf
```

You may independently fetch Miyanishi's primary arXiv source
`1504.07179` into a temporary directory only; its expected PDF SHA-256 is
`ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4`.
Do not treat later summaries as a substitute for the cited primary lemmas.

Audit these load-bearing points:

1. Verify the general (not specially typed) Miyanishi results used to obtain
   at most one multiple fibre, `Pic(U)=Z/m<[F]>`, and rational acyclicity.
   Check that restricting `rho o g1` to a general source line supplies the
   required transverse `A1`, without assuming that `g1` respects the ruling.
2. Reconstruct the no-multiple-fibre step. Decide whether irreducible reduced
   `A1` fibres plus no multiplicities really make `rho` a smooth `A1`-bundle,
   then whether it is trivial over `A1`. Check the exact scope of Orevkov
   Theorem 1.1 before using it on the resulting degree-three Keller self-map.
3. Audit the localization argument showing `U minus g1(A2)` has no divisorial
   component. Keep that target statement distinct from the false assertion
   that the Zariski-Main finite completion has no redundant boundary divisor.
   Check Miyanishi Lemma 2.5.2 as the advertised countercontrol.
4. Prove or refute the Kummer step `g1^*t=cP^m`, irreducibility of
   `X^m-t/c` over `C(U)`, and `m|d1`. Check normality, divisor coefficients,
   the exact order of `[F]`, roots of unity, and possible composite-`m`
   exceptions. Confirm separately that etaleness of `pi:U->A2` gives
   `K_U~0`. Do not silently place arbitrary `U` in Miyanishi's additional
   typed `(d,n,r)` class.
5. Starting only from finite-flat rank three and `S0=empty`, audit
   `T=U times_(A2) B -> B`. Is it genuinely surjective, radicial and etale
   at singular/reducible points of reduced `B`, hence an isomorphism even
   though `U->A2` is not finite? Check the componentwise Cartier/principal
   statement and every scheme-versus-set distinction.
6. Check that `W=U minus T -> A2 minus B` is connected finite etale of degree
   three with `S3` monodromy, and that each affine local complement group
   fixes a companion sheet. Actively seek a normal integral cubic control
   falsifying any overstatement.
7. Reconstruct the smooth-branch contradiction: Chau normalization,
   Abhyankar--Moh rectification, `pi1(Gm times A1)=Z`, and incompatibility of
   connected cubic monodromy with transposition inertia. Decide exactly what
   remains for singular or reducible contractible one-place forests; do not
   promote the tempting unproved claim that local companions share one
   global label.
8. Rerun the replay under ordinary, `-O`, and `-OO`, reproduce its payload and
   mutation behavior, and state which geometry and cited theorems it does
   not verify.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem and cheapest useful successor. This review makes
no exit-price assertion: emit no `charge_basis={...}` line; receipt status
`ABSENT` is expected. Do not run heavy local CAS.

Write exactly one repository file:

```text
xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
