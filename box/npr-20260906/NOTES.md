# NPR bounded check notes (2026-09-06, grok46)

Lane `npr-dichotomy-grok46-20260906`. Report: `xmodel/npr-dichotomy-grok46-20260906.md`.
No ledger edit, no jc2-lean, no other ideation-* input, no fleet.

## Custody

Receipt `xmodel/npr-dichotomy-grok46-20260906.run.v2` basis `cf45b6b4f80196d8bc2236c603ffc62cb0eddaa7`.
Manifest built with awk from numbered `charged_input_<i>_sha256=` / `_basename=` plus `lane_inputs_dir`; `sha256sum -c` OK on 3/3:

```
a7ee66808eb8688a568d9da98ec5840e9bb55fe0c76af21e6ac9852fb5cad89f  ideation-20260906T0000Z-opus5.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  roster.jsonl
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

Frozen copies: `/tmp/jc2-lane.us8BN8/inputs/`. Independent `sha256sum` of those three files matched the receipt.

## Files here

- `census.tsv` — 66 rows: n,m,gcd,n1,m1,semigroup,genus, child n1,m1, parent=child.
- `newton-check.txt` — (3,2) support weights; dual-cone scan; exclusivity example; general-triangle Q3 scan over roster pairs.

## Mechanical totals (from roster.jsonl `source.{n,m}` and `own_child.{n_prime,m_prime}`)

- gcd(n1,m1)=1: 66/66
- genus (n1-1)(m1-1)/2 >= 1: 66/66
- parent (n1,m1)=child: 66/66
- (n1,m1)=(3,2) Weierstrass: 40/66
- genus histogram: 1:40, 2:2, 3:11, 4:4, 6:3, 9:3, 12:2, 27:1 (matches the charged ideation)
- pair histogram: (3,2):40, (4,3):9, (5,3):4, (7,4):3, (5,2):2, (5,4):2, (7,2):2, (7,5):2, (7,3):1, (10,7):1

Root free space at wake ~2.7G, at notes write ~1.7G. This directory is << 2 MB.
