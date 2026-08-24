# Erratum v2 — additional self-reported review windows

Date: 2026-08-24  
Status: **FROZEN CUMULATIVE METADATA CORRECTION**

This successor preserves the byte-frozen three-row correction in
`xmodel/review-window-erratum-20260824.md`.  The additional Grok reports below
self-reported approximate UTC windows that disagree with the timestamps
written automatically by `ops/lane.sh`.  Runner timestamps are authoritative;
the review reports and run records remain byte-frozen.  No mathematical
verdict changes.

| review | frozen report SHA-256 | frozen run SHA-256 | report says | authoritative runner window |
|---|---|---|---|---|
| `as109-natural-nogo-review-grok-20260824` | `3b0d369c678a518614be0218c434eec97c43af0747aa8a26906256e12d2b13d5` | `ff5a4981131fd196c5a512dc58dd8dd5baf20c9a0ea46161486d80bfb7498a16` | `09:34:00--09:52:00Z` | `09:29:14--09:38:12Z` |
| `as109-quadratic-review-grok-20260824` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | `becc731e30c590ca66d32cd3a42cec9b619d12d4fff4477e56a9e81cdc158f37` | `09:42:00--09:52:00Z` | `09:39:02--09:51:15Z` |
| `secant-idempotent-review-grok-20260824` | `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9` | `142f8010cf8987621fee98e6ff0e655a6970fbfb129e6b8c2cbd362dafdfd44b` | `09:20:00--09:50:00Z` | `09:34:18--09:51:07Z` |
| `td6-global-compatibility-review-grok-20260824` | `f3e468f415fdd7bd1aa85962090d34a55bf6ff15d469c28373347cf1c7cc42ac` | `9df9af99a471dc6757a2d0870bef2e70985da446426483ccf35e016e8e6f0ca5` | `09:20:00--09:50:00Z` | `09:39:02--09:52:25Z` |
| `secant-projective-review-grok-20260824` | `99b7649365a3fbae34932c2bacc03ad141507f74a6ca55d2945bc427e0404957` | `e51ba6d63ac7203e37664f04ea01561ca068a6f524c9edbbba21cc25269aaaf7` | `09:48:00--10:00:00Z` | `09:44:03--09:55:17Z` |
| `secant-as109-review-grok-20260824` | `16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029` | `406889d4243ba468b7ebb65a58aea3dc136f1b4bbfc51582b605955cdede5a8e` | `09:57:00--10:20:00Z` | `09:56:42--10:11:06Z` |
| `as109-cubic-review-grok-20260824` | `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef` | `bc5ee8746d6b60507f4cfcb53d160954c7b4f51450d40cea91def043afa77f96` | `10:00:00--10:07:00Z` | `09:59:12--10:10:25Z` |
| `td6-two-chart-first-band-review-grok-20260824` | `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` | `78bd4770e40b20a19ed2b9c88b46a44e6e4ef5e4f3c3567e1b6ffac940f58e76` | `10:19:14--10:35:00Z` | `10:19:14--10:33:47Z` |
| `as109-quartic-review-grok-20260824` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | `9d9c3eeb2c85db721a4d05a4b51dee68baa70f49f4c3fd17bf6b5330d6799d7c` | `10:22:00--10:32:37Z` | `10:24:25--10:36:32Z` |
| `quintic-y-review-grok-20260824` | `ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e` | `bce9da37c72661ef592eb87ea0f9bef7e5d0957414a5513d8d328f23d7727960` | `10:38:00--10:50:00Z` | `10:33:46--10:51:13Z` |
| `td6-two-chart-next-row-review-grok-20260824` | `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` | `ad9b40353a6d5ca25b4652c3ca6ca2c2fe9c44fe875dd2a71727962016f5962b` | `10:35:18--10:42:00Z` | `10:33:46--10:44:53Z` |
| `as109-degree-cross-review-grok-20260824` | `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6` | `fdd2292bff4f2eb1519377cb9200410a728d53a1f7427a1e17027280a024ccb7` | `10:48:00--11:05:00Z` | `10:43:26--10:59:52Z` |
| `as109-sextic-preflight-review-grok-20260824` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | `5a71d75485f9ad152f01fd18233d03964fcf9689249110b387bb1a51d1d38241` | `10:53:00--11:07:35Z` | `10:44:09--11:11:23Z` |
| `as109-ainfinity-review-grok-20260824` | `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76` | `c3f1ca8d8d86f7847043743933b648733e7c523b3e4b004d19cdfeb5ba308939` | `11:07:00--11:20:00Z` | `11:00:12--11:18:27Z` |
| `td6-moduli-uniformity-review-grok-20260824` | `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` | `e46f7e2b71c8ce7a475911902082759cd8b22a0e86af169eb02405ea3b9caa40` | `10:48:00--11:16:25Z` | `11:00:12--11:19:35Z` |
| `as109-sextic-survivor-review-grok-20260824` | `4f2c8b6cd1a165ed73dedb0a3fc92256199927961a6c5126afc6689408106c59` | `aab7fe60da5cffbbaf51982f9036c6ed94b3d5f262196e16494f0747f9214ee9` | `11:00:00--11:18:29Z` | `11:03:20--11:21:43Z` |
| `td6-paired-third-band-review-grok-20260824` | `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` | `082b8cbc6e1115f1e6c17976fd16e4995d28dc88cd9422417b629b90ab9f8936` | `11:15:02--11:33:00Z` | `11:15:02--11:35:41Z` |
| `as109-sextic-46-closure-review-grok-20260824` | `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c` | `6cf5adaeb6e4da6fc654e4ed6d3c460872eb9458f558a821c464809f1dcb432b` | `11:33:00--11:49:04Z` | `11:33:32--11:52:44Z` |
| `as109-sextic-56-exclusion-review-grok-20260824` | `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70` | `758f2ddd617e71fdd868ba25bb7c397a627bdca5fc1cffec7ee044c789f28b8b` | `11:41:00--11:47:00Z` | `11:33:32--11:49:56Z` |
| `moskowicz-prime-degree-review-grok-20260824` | `a32082a89077b17bb9f9df4d2b518d8e7ad6de4e126a35cf0d49b446bb0d5a06` | `36c46f84e1f9978edd7861afb333f6ce175fa1d4450f7eeaaf273144d66b5c34` | `11:28:00--11:50:00Z` | `11:33:32--11:44:38Z` |
| `as109-xy-membership-review-grok-20260824` | `04c4d3dc8342141c4b1cb615e232a00053a056825fddbe55dd3ba5c2b44b8ac0` | `23e1e02ff77b703e13572c44a272b807f096d852013adb1834ac954a4160a5fd` | `11:48:17--12:05:00Z` | `11:48:17--11:59:15Z` |
| `td6-moduli-uniform-third-band-review-grok-20260824` | `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef` | `4adabbb17c53c4e370a7f8213f32e2042ab26297f30ac4567538725ff92497a1` | `11:48:17--12:12:00Z` | `11:48:17--12:11:05Z` |
| `as109-bounded-y6-chain-review-grok-20260824` | `81669337bf038ae2bb2d81c20bec7ef92a97eaeaa03f906d0a20c33bf20a9115` | `e87997c9fbcfedcfbe0d77170d04b3683b5dc9a4711cc13a0c9acd9b20e89b88` | `11:50:00--12:02:07Z` | `11:54:47--12:05:02Z` |
| `as109-partial-y-history-review-grok-20260824` | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` | `8f492d348d73b3710bcb7d72de6c09ffd5c278d84d63cc693447bef4af81a6b3` | `12:05:00--12:27:42Z` | `12:15:36--12:31:30Z` |
| `as109-wild-symplectic-conductor-review-grok-20260824` | `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | `93efcce92f0c7139f2d0954f63f0d5833160c62e38bc1f4e2d0a996c0e0f43cc` | `12:32:00--12:50:00Z` | `12:31:14--12:49:03Z` |
| `td6-boundary-q2-deformation-review-grok-20260824` | `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c` | `f7cf11d05fcfca5d92bdab763634ca5131f323a25974b322e512794fb0c8c4d2` | `12:58:15--13:16:11Z` | `12:53:23--13:19:11Z` |

All 26 additional runner records have exit code zero,
`final_status=DONE`, and matching embedded report hashes.  The frozen v1 and
this successor jointly cover 29 reports.  No input hash, computation, source
audit, verdict, or scope statement is affected.
