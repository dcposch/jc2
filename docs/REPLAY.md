# Reproducible mathematical computation

These requirements concern the evidence, independently of a swarm's cloud provider
or model launcher. Commands below run from the campaign repository root.

## Before computation

State actual total degrees separately from partial-y and weighted degrees. Explicitly
record whether coefficient-x or total degree is bounded. Compare the exact scope
with the accepted closed cases in [APPROACHES.md](../APPROACHES.md) and
[AUDIT.md](../AUDIT.md), and verify applicable primary-source hypotheses.

`python3 ops/frontier_gate.py --help` describes the implemented classical filters.
A refusal blocks a counterexample search in that closed scope. A method control needs
a named live client and a bounded purpose. An inconclusive verdict means only that
the implemented tests do not decide the scope; it is not proof of openness against
other theorems. For realization jobs at N >= 6, use `box/preflight.py` on the manifest
before launching; its encoding-faithfulness checks must pass.

Run heavy or uncertain-duration computation on a separate worker with explicit limits.
Your operator chooses the provider, budget, launcher, and permitted machines.

## Artifact contract

Include exact engine versions, commands, input hashes, seeds, all primes, execution
environment, UTC times, expected outputs, and meaningful negative controls. Use
logical worker identifiers when private infrastructure details are irrelevant.

Store replay instructions in the artifact README. Use repository-relative paths in
`SHA256SUMS` and check them from the repository root:

```sh
sha256sum -c box/<artifact>/SHA256SUMS
```

A frozen report and manifest are integrity evidence, not mathematical verification.
Do not modify a report under review. Finish and freeze new bytes, then request a delta
review if the charged claim or computation changes.

## Exactness checks

- Preserve exact integers and rationals as integers or decimal strings across tool
  boundaries. JavaScript binary floating-point JSON numbers can silently round them.
  Check the retained mathematical values as well as their hashes.
- For a characteristic-p, Witt, or p-adic successor digit, exhibit the exact integer
  numerator, prove divisibility on the charged predecessor scheme, and form the
  integer quotient before reducing modulo p. Reconstruct the rows independently.
  A mod-p bracket alone does not verify a divided carry.
- A `python -O` or `-OO` claim requires active checks in those modes. Inspect the
  verification paths for stripped assertions and run a deliberate failing mutation
  under every claimed mode. Ordinary-only scripts may use assertions with that scope
  stated explicitly; identical successful output does not validate optimized checks.
- msolve 0.10.1 characteristic-zero `-g` can emit a first-prime unit basis before
  rational reconstruction. A characteristic-zero header and `[1]` are not an exact
  rational certificate. See the ledger's engine caveats.
- Preserve every localization, saturation, quotient, specialization, and source map.
  A modular point, truncated survivor, or growing formal family is not automatically
  a characteristic-zero point of the complete source.
- Apply [FALLACY-v2.md](../FALLACY-v2.md). A report asserting a new exit price carries
  the exact `charge_basis={...}` declaration it specifies. Other reports omit it;
  an absent declaration is not a mathematical pass.

## Optional authoring tools

`ops/artifact_finalize.py` offers a no-overwrite local publication transaction:
`begin -> close -> finalize -> verify`. See its `--help` and module documentation.
`ops/open_collision.py` searches banked research, including the archived journal;
its candidates require mathematical interpretation. `ops/seal.py` checks integrity.
None replaces independent hostile review, and outside swarms may use different
orchestration as long as their submitted evidence meets the contract.
