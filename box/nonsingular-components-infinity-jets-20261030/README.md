# Nonsingular components and infinity jets

**PROVISIONAL / MANUAL; independent PASS. JC2 remains unresolved.**

The [reviewed report](../../xmodel/nonsingular-components-and-infinity-jets-swarmHQ-root-sol56-20261030.md) gives an all-n proof with a fixed
nonsingular P, globally nonsingular Q_n, and arbitrarily high Jacobian precision
at one fixed infinity valuation. There is no exact polynomial mate for P.
The full graded rings are smooth and symplectic; the filtered target is not
Poisson closed. Every displayed pair has nonconstant Jacobian.

The [author candidate](CANDIDATE.md) and [independent review](../../xmodel/nonsingular-hamiltonian-jet-review-sol56-20261030T2300Z.md)
are preserved exactly. The candidate's UNREVIEWED label is historical.
[SCIENTIFIC-INPUTS.json](SCIENTIFIC-INPUTS.json) records hashes and proof provenance.

From this directory, with Python and SymPy installed:

```sh
python3 -B check.py
sha256sum -c SHA256SUMS
```

[check-result.json](check-result.json) records exactly n=0,1,2 plus ten identities.
These are sanity checks, not a substitute for the all-n proof. The portable
script differs from the author script only in its output destination.
Checksums establish byte identity, not mathematical correctness. Novelty is
unassessed; no fixed-degree, full filtered, or global Keller exclusion follows.
