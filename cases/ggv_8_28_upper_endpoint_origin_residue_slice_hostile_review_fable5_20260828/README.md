# Hostile review: origin-residue fixed-slice exclusion (Fable 5, 2026-08-28)

Independent hostile audit of the frozen fixed-slice theorem

- `xmodel/ggv-upper-endpoint-origin-residue-slice-sol-ultra-20260828.md`
  (SHA256 `7202f703...`), producer checker `de371953...`, and the exact
  arbitrary-Q negative control `c940ba04...`.

Verdict: **PASS**. On the strict slice `A=X^4-1, lambda=0, exact D=0,
Q=e=F8=r=0` (characteristic zero), every literal q7/q9/q11/q13 solution
making the complete characteristic coefficient G15 polynomial has
`D22[X0]=0`, contradicting the raw endpoint target `+1`; the slice is
empty. `c2!=0` is verified to be harmless scope narrowing (not
load-bearing). The exact `Q=X` mutation was independently replayed:
legal q7..q15 primitives, legal G11/G15 windows, polynomial G15, origin
pairing `2^50/375` scaling to exactly `+1` — so the identity does not
promote to arbitrary Q. No promotion to another A, another branch, the
full endpoint, Keller, or JC2.

Fresh standalone checker (standard library only, exact rationals; does not
import or trust the producer checker):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-origin-residue-slice-hostile-review-fable5-20260828-check.py
```

Expected final marker: `PASS_HOSTILE_ORIGIN_RESIDUE_SLICE_FABLE5`
(captured in `checker_output.txt`).

Contents: `RESULT.json` (verdict), `SOURCE.sha256` (frozen inputs,
repo-root-relative), `EVIDENCE.sha256` (produced artifacts),
`checker_output.txt` (replay transcript).

Full findings: `xmodel/ggv-upper-endpoint-origin-residue-slice-hostile-review-fable5-20260828.md`.
