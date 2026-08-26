# Pre-solve custody

The registered Box03 AWS compiler returned rc zero, empty stderr, pinned the
base compiler/B hashes, and emitted its unique PASS.  Before `GO_SOLVE`,
Box03 verified the 136-line / 5125-byte global-`dp` input:

```text
4e531f9c3b618f4a9af4991572aa969c7375cd404dcbc62551d8c236b419c562  la20_dp_cone.sing
```

The displayed tail of the frozen source includes the complete term-iteration
and strict-weight checks.  No local compiler or CAS execution was performed.

