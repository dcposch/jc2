# Hostile review: C1 denominator hole and ARITH-SPREAD repair

You are Grok 4.6 acting as a different-model adversarial algebraic-geometry
referee.  Work in `/Users/dc/code/math/jc2`.

## Charged objects

Read and hash:

- `xmodel/ideation-20260829T0002Z-fable5.md`, expected SHA-256
  `db51f06128d884dd80361d866c8042c1d80afff02d616f38d3334ecec7d875e9`;
- `xmodel/d43-conceptual-breakthrough-primary-research-grok46-20260828.md`,
  expected SHA-256
  `99fb7d7c21f8c0a7754f9b33354a3963520cdcb01e22df9e7ce786b74f425588`;
- `xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md`, whose
  report-body seal is
  `877e451f33b24b7714c712404401f11b35b6621e80400e791c4b54cfbe5078fd`.

Do not read any still-unfinished `ideation-20260829T0002Z-*` peer report.

## Questions to decide from first principles

1. Does Fable's constant-system counterexample
   `F={105337*105673}` genuinely refute the original two-frame C1
   non-unit-ideal inference?  Locate the exact denominator-clearing error.
2. State and prove the strongest correct finite-prime replacement.  Track an
   emptiness certificate over `K0`, clearing denominators into the finite
   étale order `A=Z[1/42][...]`, localization denominators, maximal ideals
   over the registered primes, and the numerator of the absolute norm.
   Determine the exact divisibility/exponent statement; do not accept the
   informal `about 10^(5k)` claim without hypotheses.
3. Prove or refute each ARITH-SPREAD limit implication for a fixed finite-type
   `A`-scheme `X`:
   - nonempty geometric fibers at closed points over infinitely many distinct
     rational primes imply nonempty geometric generic fiber;
   - geometrically empty/unit fibers at closed points over infinitely many
     distinct rational primes imply empty generic fiber;
   - if the generic fiber is nonempty, what exactly holds for all but finitely
     many closed points/rational primes?
   Use the constructible image theorem carefully.  Distinguish a proper ideal
   over the residue field, a geometric point over its algebraic closure, and
   an `F_p`-rational point.
4. Audit whether one frame/maximal ideal per rational prime suffices, and how
   complete splitting/Galois torsors affect—or do not affect—the theorem.
5. Audit the proposed D43 client.  A cross-prime census is meaningful only if
   every fiber is a reduction of one frozen integral system.  Decide which
   existing row/emitter objects establish that and which remain provisional
   or unsealed.  In particular, test Fable's claim that v3 is unnecessary for
   the per-prime census itself.
6. State the exact evidential meaning of one `UNIT`, finitely many `PROPER`,
   infinitely many of either, and a uniform point-count/character-sum theorem.
   A "signal" must never be worded as a characteristic-zero conclusion.
7. Attempt countermodels for every implication and record why each succeeds
   or fails.  Check non-flat families, vertical components, residue-degree
   greater than one, localized denominators, and constructible images that
   omit finitely many points.

## Output

Write only

`xmodel/d43-arith-spread-hostile-review-grok46-20260829.md`.

Give per-claim verdicts `CONFIRMED`, `REPAIR`, or `REFUTED`; a clean theorem
statement suitable for `AUDIT.md`; an explicit correction to the original C1
claim; the minimum sound experimental client; and exact promotion/scope
limits.  End with a self-hash delimiter and body SHA-256.

No AWS, web, heavy CAS, canonical-ledger edits, commits, pushes, or access of
any kind to `jc2-lean`.
