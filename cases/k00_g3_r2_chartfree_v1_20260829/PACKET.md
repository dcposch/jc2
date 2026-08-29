# Sealed packet note: `K00-G3-R2-CHARTFREE/v1`

Date: 2026-08-29

Lifecycle: **PRODUCER PASS / EXACT SAME-CODE-FAMILY REPLAY PASS /
INDEPENDENT REVIEW OUTSTANDING / PROVISIONAL ONLY**.

## Endpoint

On campaign basis commit
`92ebe92ad5986a47f01af9ed901260595dfed869`, the packet rebuilds the seven
literal grade-three rows and verifies exactly

```text
P3(x,u) = C(x)u + c3(x),
C(x) = A(x)[:,1..6].
```

For

```text
H = B + I3(A) + I3([C|c3]),
```

it emits exact two-stage coefficient matrices proving `q_j^4 in H` for all
351 nonzero literal `2 x 2` minors `q_j` of `A`.  All 441 literal minor
labels, including the 90 zero labels, are preserved.  All 1,225 literal
`I3(A)` and 1,225 literal `I3([C|c3])` positions are likewise preserved in
the source-label manifest and in the 2,457-column raw ideal.  For each of
those two `I3` families the exact census is `ncols=1,225`, `zero=412`, and
`nonzero/size=813`.

The checked matrix identities are

```text
matrix(Hraw) * TH = matrix(GH),  shape(TH) = 2457 x 20
matrix(GH)   * CQ = matrix(Q4),  shape(CQ) =   20 x 351.
```

The standard basis has 20 entries and dimension two.  The unresolved-minor
profile at powers `1,2,3,4` is `291,60,36,0`.  Therefore
`I2(A) subset sqrt(H)`, which excludes every rank-exactly-two leading point
from lifting through literal grade three.  This is the chart-free
mathematical successor to the capped selected full-`P6` chart.  The
historical chart remains `RESOURCE_CAP_NO_VERDICT` as an engine outcome.

## Custody

- source freeze:
  `1a7ad8c9cbe92f5bc68613ca6758eb2ef150819d0af5a96b613574fb3f9c25df`;
- output manifest:
  `d446e8f2c875309219333fce3346f25e345a8b4566e2319cbaaa9755399ee1e3`;
- `RESULT.json`:
  `8c64644ba06107696ac753cd85ce3b44b45bf803e21a3c6979d14591a711fdaf`;
- source labels:
  `daa4a3b7deee43d4d36de13a7811ae693af3751684e5c87531bd525ac467c9a4`;
- standard basis:
  `286133422a89c5d6881bce3b20a8a946bc31a58a642d16e0b28167e1ce42b78a`;
- raw-to-basis transform:
  `739c73d90ce9cf6248e2c76e8c5341ac5b5739ebf5cfacc9c61575c53e25fdc4`;
- all-`q^4` coefficient matrix:
  `919a3b02ee9149e318f6f0cf8c39b42425dc5aa699e5bf80a93b54f78de08c42`;
- producer Singular source:
  `a315f7c8eec43a909b4a7007bc21c30358a3fa82cbf7f8566bcd754074f7daf1`;
- replay Singular source:
  `feffc9f49cd4d2bc54838561aeb79febe26830545cd6d09778701d6cf26be945`.

The output contains 68,089,702 bytes.  The 21,869,823-byte `CQ` artifact is
the full explicit rational-polynomial certificate matrix, so the
fresh-reduction fallback was not used.

## Tests and controls

The canonical ordinary build returned

```text
PASS_K00_G3_R2_CHARTFREE_OBSTRUCTED_PRODUCER_EXPLICIT_CERTIFICATES
```

in 16.25 seconds with maximum resident set size 795,574,272 bytes and zero
swaps.  The standalone validator returned

```text
PASS_K00_G3_R2_CHARTFREE_VALIDATOR_EXACT_REPLAY_SAME_CODE_FAMILY
```

in 7.11 seconds with maximum resident set size 302,710,784 bytes and zero
swaps.  Both Singular stderr artifacts are empty, and diagnostics are
fail-closed.

A fresh `python3 -B -O` build in a separate directory returned the same
producer status.  `diff -qr` against the canonical ordinary output was empty,
and both output manifests had SHA-256 `d446e8f2...e1e3`.  No AWS resource was
used or needed.

Mutation controls pass for a `C` entry, a `c3` entry, one nonzero raw-to-basis
coefficient, one nonzero basis-to-`q^4` coefficient, and one `q^4` target.
The forced-unit ideal becomes unit and the known-proper ideal `(d0_1)` stays
proper.

## Firewall and review target

This packet is not independent of its discovery computation: producer and
replay share the generated construction.  A different model should rederive
the grade-three split from the frozen literal rows, audit the row/column label
order, and replay or independently verify the fourth-power certificates
before promotion.

The endpoint excludes only rank exactly two at grade three.  It does not
decide rank at most one, rank five/`MAX5CLASS`, later lifting on other strata,
source reachability, a counterexample, or JC2.  No canonical campaign file was
edited, and this packet was not committed by its producer.

## Seal

- Body length: `4137` bytes (all bytes before this heading).
- Body SHA-256:
  `a2487f5440500a70822dffebab8f9875fc26a98c422c816aa440809824c4b3b7`.
