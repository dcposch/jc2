# Custody quarantine: Grok hostile review attempt A

**Date:** 2026-08-29  
**Classification:** **`TRANSIENT_INPUT_MUTATION_NO_PROMOTION`**

## Record

Attempt A ran under tag
`m2-two-pole-full-actual-first-separation-hostile-review-grok46-76c-20260829`
from `2026-08-29T11:27:34Z` to `2026-08-29T11:40:02Z` and exited 0.
Its sealed mathematical verdict was `PASS_WITH_REPAIR`.

Artifacts:

```text
c40f193df565e1dc47ebf8f52e0781806b3aa8e58a552bfc93a9cbb6f479f430  report
  sealed body 36313 bytes:
  8c27398008093ee85dfff39e610829b6ef6e5461af624aeb304f46af1e074e44
7bbd499234f1d953d9b5b0acdde7ba767b9e1b93580485cc398c45ab9bfb55ac  prompt
69c81e9aace5d0a9d216a78a202558dfc6465f82868e17cbc11b7e1d074b6beb  log
4f03d5856b9a69926d4f732015acb6fe9179c6ecf48154d8d78cf5f97343c0e0  run.v2
```

During the live interval, the coordinator reported that charged input
`ladder/BOOK-OFFAXIS.md` was briefly appended and then immediately restored
byte-for-byte.  Its charged/current SHA-256 is
`1ae50f7925de2d63a718b48ab892c78a3313e4a505b8faf7385853d591c58840`,
and attempt A itself observed that hash both before and after.  Nevertheless,
an ABA mutation is not detectable from endpoint hashes and it cannot be
proved that the reviewer never observed the transient bytes.

Therefore attempt A is diagnostic evidence only.  Its mathematical findings,
charge declarations, checker result, and apparent custody **must not be used
for promotion**.  A fresh stable-basis attempt B must independently repeat the
hostile review without reading or citing attempt A or this note.

No canonical, ladder, case, guardrail, or operations file is changed by this
record.  It records a custody failure; it does not adjudicate theorem truth.

<!-- END-SEALED-BODY::m2-two-pole-full-actual-first-separation-hostile-review-grok46-76c-20260829-attempt-a-custody-quarantine -->

## Seal (outside the sealed body)

- Sealed-body bytes: `1845`
- Sealed-body SHA-256:
  `5efb3795b967d2817aab3f38d72de6a078ae09c8293b66aa166ab7cf0b4d738c`
