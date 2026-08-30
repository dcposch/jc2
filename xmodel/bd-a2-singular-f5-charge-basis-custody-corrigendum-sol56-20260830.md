# Custody corrigendum: `charge_basis=ABSENT` was correct for the singular-F5 polar review

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `eb6c6aee8bcdbac667a2fbd2c03231c8edc38939`  
Disposition: **OPERATIONAL CORRECTION; NO MATHEMATICAL CLAIM CHANGES**

## Correction

Section 0 of the sealed binding integration

```text
xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-coordinator-integration-sol56-20260830.md
```

incorrectly describes the review receipt's
`charge_basis_status=ABSENT` as an operational prompt-format defect and says
future prompts should use the validator marker. Those two statements are
superseded.

The status was correct. The singular-F5 review made no new exit-price
assertion. The machine marker is not a generic declaration of hash-pinned
review inputs and must not be added merely to avoid an `ABSENT` receipt.

## Literal policy and implementation

The frozen sources are:

```text
a89658bc2bf01c4cbbc601f3b9db60e46168d37f00367fdc87ef2e94b19a125e  ops/validate_charge_basis.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
7385ef9ec753d7173f9b109a9ba739b073671049a7b0b638ac4b0f52d26a7b9a  COORDINATION.md
```

`FALLACY-v2.md` says to add exactly one `charge_basis={...}` line *for an
exit claim*, and then narrows this further: declare only a new exit-price
assertion; consuming a promoted price needs no line. `COORDINATION.md` says
reports *may* declare such a line, invalid declarations quarantine the lane,
and absence is recorded as `ABSENT` without being interpreted as a
mathematical pass. The validator implements exactly that contract: if it
finds no line beginning `charge_basis=`, it prints `charge_basis=ABSENT` and
returns success.

The charged review prompt, receipt, and superseded integration are:

```text
7b0254f8fe9429854349cedcc17e929e2ff55dc68031eac352ebd8b287064e7c  xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-hostile-review-gpt55-20260830.prompt.md
11f14900e244108b0f5676da1bdc732469d0005d86cdb43ef8c7edfebe25d1fb  xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-hostile-review-gpt55-20260830.run.v2
fdf8f476acc86e2c07fbc472771ee49358d02c87d2667f15e6b762800eed7bc6  xmodel/bd-a2-singular-f5-local-polar-and-a6-a7-elimination-coordinator-integration-sol56-20260830.md
```

The prompt requests a geometric/local-algebra hostile review and no new
per-ray or first-separation exit price. Therefore omission of the marker and
the receipt status `ABSENT` are semantically correct. Hash custody is recorded
by the prompt/run hash fields and root's independent reproduction, not by
`charge_basis`.

## Forward rule

Before launching an external lane, classify whether the requested report is
authorized to assert a *new exit price* in the sense of `FALLACY-v2.md`.

- If yes, require exactly one valid machine line for each newly asserted
  basis, with its exact delta, branch, distinct flag count, and mathematical
  citation.
- If no, omit the line and expect `charge_basis_status=ABSENT`.
- Never synthesize a placeholder marker for geometry, ordinary input hashes,
  or consumption of an already promoted exit price.

No launcher, validator, prompt, receipt, review verdict, or promoted
singular-F5 mathematical conclusion changes. This is a correction to the
interpretation of one receipt field and to future prompt-writing guidance.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3395`.
- Body SHA-256:
  `c95ee81b0e1ba4b2a63cf170a612ae1a4f405f1c95757770aa128db5c7933ae4`.
- Frozen basis: `eb6c6aee8bcdbac667a2fbd2c03231c8edc38939`.
