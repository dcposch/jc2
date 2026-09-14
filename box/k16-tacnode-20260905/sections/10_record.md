## 10. Computation record (`box/k16-tacnode-20260905/`), collision scan, completion

```text
manifest.sha256, input-verification-final.log      custody (awk manifest; sha256sum -c 4/4 OK at start and at sealing)
tacnode_involution.py -> _K6/_K10.{json,log}        Props. 2.1-2.4, Theorem 5.1 pieces, pivot chain, closed forms (generic jets; ALL_PASS)
disc4_check.py/.json                               [x⁴]Disc(F_0) with generic P_4 = -16T_2/(9b²)
t2_family.sing/.out                                t = 2, d = -1 family: C irreducible, L̃ series, D = (15/2)L²x³, ∞-branch with lc -1/y
custody_tacnode.py -> _t3.*, _t4.* (exact Q(d)); _t{3,4,5}_p31991_d*.* (modular, incl. Hensel replay; t = 5: Hensel loop stopped at seal (19 min), NOT claimed; its D/T_2/membership lines are complete)
hensel_debug{,2,3}_t3_p31991.sing                  diagnosis of the rejected jet-truncation draft
sections/, finalize.sh, hash_artifacts.sh, artifacts.sha256, collision_scan{,.filtered}.txt
```

All CAS local, `--cpus=1`, <= 5 Singular processes; one shell lost to a self-matching `pkill -f` (no artefact affected); the exact
t = 5 std over Q(d) was not attempted (unfinished after 32 min in the charged lane): t = 5 is modular only.

Collision scan (`ops/open_collision.py --root .`, filtered of this lane's files): `OPEN[K16-UF-CONTACT-ORDER-BOUND]`:
hits 17(sssssss) (the charged source lane's delta: KNOWN, the source of the tacnode OPEN) and 17(ooooooo)/(ppppppp)
(lexical noise). `OPEN[K16-UF-DEGENERATE-TACNODE]`: 17(sssssss) (source). Retained OPENs:
17(ccccccc), 17(jjjjjjj) (charged sources), 17(zzzzzz)/(eeeeeee)/(hhhhhhh) (Moh/census: noise), the K16 deltas 17(xx)-(vvvvvv)
for `OPEN[K16-UNIFORM-POINT]` (KNOWN), and lines of the same-round `ideation-20260905T1200Z-astra.md` (uncharged, not read).
Nothing closes any OPEN.
