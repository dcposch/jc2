# V43G3 tracked generic `Q(t)` multiplier successor

Date: 2026-08-27

V43G2 returned the exact `dp` basis `(1)` for the full generic ordered-`a1`
decision after the exact `Tg19_2`/`ez9` pivot.  V43G3 is a separately frozen
producer whose sole task is to turn that decision into a replayed Bezout
identity.

The compiler must independently regenerate all 59 literal rows from the
pinned V43 source, repeat the complete 70/59/66/65/eight-rho-only/sole-`ez9`
census, and check the exact pivot term

`Tg19_2 : (3/8)t*a1*ez9`.

It must then construct the same 58 dehomogenized rows in the same
64-variable `Q(t)` ring and byte-compare the ring declaration and every ideal
entry to the frozen V43G2 decision script.  Any discrepancy is fatal.  The
pivot row is retained in the source map with multiplier zero; eliminating it
is the checked linear quotient isomorphism, not a row omission.

On the exact same 58-row `dp` ideal, Singular runs `liftstd(J,T)`, checks
`matrix(J)*T=matrix(G)`, lifts `1` through `G`, forms `C=T*H`, and checks
`matrix(J)*C=[1]` exactly in `Q(t)`.  All 58 multipliers, the basis, the
transformation matrix, and the final coefficient matrix are saved.

Only a terminal PASS with both matrix replays is evidence.  Timeout, OOM,
signal, missing output, source drift, a nonunit result inconsistent with
V43G2, or any `FAIL_` marker is no verdict.  This run does not itself
rehomogenize or clear denominators; those are successor validators over the
saved exact multipliers.

Pinned V43G2 artifacts:

- case result `60b76bd4d3a8106a1e670073ae1f84218e1d62ae21187d79d75abf0bbcc48028`;
- case freeze `bbb8b2d637be3458c0e67cfabbe3fa594ea521cb6a1151a5a242f937abf4c04d`;
- compiler result `fac99098b36f5875b53c8d66439f34ca59b47e7f25a58f97dba1cb8cddd3806c`;
- generated decision script `7e3149d9ff89274e31c1068a51903dd9e2e716168141bd6286fa6b47d56328b3`;
- V43G2 compiler source `4ce93300474ec1a86cb9a435fbb3d780b3e121a946796a07f1cd0f8a73bd0a99`;
- V43G2 preregistration `2545d70dd88700318c45a6a1a337f63b28379cef2f8760dd3481ba2d7bb2f6c8`.

The first run uses one spare r6a core with a 384-GiB virtual-memory cap and a
two-hour wall cap.  The AWS source manifest is frozen before launch.  V43G1
and all existing jobs remain untouched.
