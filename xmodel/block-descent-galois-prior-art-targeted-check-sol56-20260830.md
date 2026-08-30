# Targeted prior-art check: `BD-GAL` versus the classical Galois case

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **TARGETED SEARCH NOTE / NEGATIVE SEARCH IS NOT NOVELTY EVIDENCE**

## 1. Question and scope

Opus's hostile review of `BD-GAL` observed that the unavailable `d1=1`
specialization resembles the classical Galois case of the Jacobian
conjecture. This note checks only:

1. whether the full-extension theorem is classical; and
2. whether a quickly discoverable source already states the new proper-
   intermediate conclusion.

This was a narrow source lookup, not the scheduled broad JC2 web sweep.

## 2. Classical full-extension theorem confirmed

The standard bibliographic source is:

```text
L. Andrew Campbell,
"A Condition for a Polynomial Map to be Invertible",
Mathematische Annalen 205 (1973), 243--248,
DOI 10.1007/BF01349234.
```

EuDML indexes the paper under that title, author, journal, year, and subject.
The Encyclopedia of Mathematics' Jacobian-conjecture entry explicitly states
that a Keller map is invertible when the full function-field extension
`C(F) subset C(X)` is Galois, attributing the result to Campbell. Later
standard attributions also name Razar and Wright for algebraic/general-field
treatments:

```text
Michael Razar, "Polynomial maps with constant Jacobian",
Israel Journal of Mathematics 32 (1979), 97--106,
DOI 10.1007/BF02764906.

David Wright, "On the Jacobian conjecture",
Illinois Journal of Mathematics 25 (1981), 423--440,
DOI 10.1215/IJM/1256047158.
```

Thus `BD-GAL` must not be advertised as new in the `d1=1` full-extension
case. The campaign's promoted block-sandwich premise is in any event stated
for a proper intermediate field, `d1,d2>=2`, so it does not use that
specialization.

## 3. Proper-intermediate search result

Targeted exact-phrase and concept searches covered combinations of

```text
Jacobian conjecture / Keller map,
proper intermediate field / intermediate subfield,
Galois subextension,
normalization / block system / imprimitive monodromy.
```

No indexed primary paper or survey located in this pass states the exact
proper-intermediate theorem:

```text
C(f,g) proper-subfield K proper-subfield C(x,y)
and K/C(f,g) Galois  ==> contradiction.
```

One commutative-algebra proceedings source discusses intermediate rings
invariant under the Keller derivations and proves such a ring etale over the
base. That is a different hypothesis: an arbitrary normalized block field is
not assumed derivation-invariant, and the source snippet does not give the
missed-ramification/fixed-sheet argument.

Recent public campaign repositories found by the same targeted queries invoke
the classical full Galois case and discuss block actions or affine-completion
programs, but the indexed pages did not expose the proper-intermediate
no-Galois theorem.

This is a **search outcome, not proof of novelty**. Before publication, run a
full citation review of Campbell, Razar, Wright, later Galois-case literature,
and work on imprimitive Keller monodromy. Internal mathematical promotion of
`BD-GAL` does not depend on a novelty claim.

## 4. URLs used

```text
https://doi.org/10.1007/BF01349234
https://eudml.org/subject/MSC/13B25
https://encyclopediaofmath.org/wiki/Jacobian_conjecture
https://doi.org/10.1007/BF02764906
https://doi.org/10.1215/IJM/1256047158
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3428`.
- Body SHA-256:
  `ad93944dfad298c09b93d6f566b3d35b2f359a0ec5b312d39d6436484f91f12d`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
