# Final review: marked-curve full-lift obstruction

Reviewer: configured Sol5.6 independent lens; actual hosted identity and cost unmeasured.
Date: 2026-10-25 UTC
Basis: `db01d6034600ce8e85ed706db2d4e8fa4359f4fe`
Verdict: **CONFIRM_EXACT_PUBLIC_PACKAGE**
Lifecycle: MANUAL / independent delta review; this review does not itself promote or edit ledgers.

## Scope

I approve the sealed public proof and the proposed three-ledger delta only for
the following conditional theorem: for the literal
`S=C[X,Y,W,T]/(X^2-Y^5-WT^7)`, weights `(5,2,3,1)`, there is no degree-`e>1`
full homogeneous algebra lift with `T` mapped to `T^e` and the specified
injective Poisson central map. The adopted `lambda_1>=N`, divisorial
attachment/projectivity results, and their named dependencies remain explicit
inputs. This is not an all-target exclusion, infinitely singular reduction,
properness theorem, or JC2 proof.

## Producer and unchanged core

The producer is sealed and VERIFIED at the public basis. Its full SHA-256 is
`504310c1d583a8c330538ce37852856cc49ffb293ead2244dff89df249b67d1a`,
body SHA-256 is
`271c229fae88a7e42c3e057824cedc3f0eb0659b0767c0b86ba5d790c04922d3`,
and manifest SHA-256 is
`8badb5711fc499170a39173554f8f6dacf41123e39a6b0d88452f585011dc534`.
The six-section public core (producer lines 32–121) is mechanically
byte-identical to `markedcurve1436-astra.md` lines 5–94. I therefore retain my
independent `PASS_CONDITIONAL` mathematical review without silently changing
its hypotheses or conclusions.

## New bracket and appendix delta

The displayed bracket is consistent with the weighted relation and the
previously reviewed reduction. In the appendix, `T` is prime because `S/(T)`
is the domain `A0`; injectivity of the central map makes `U mod T` nonzero, so
`T` does not divide `U`. Bracketing the full relation with `V` and using
primality gives `T^(7e)|{U,V}`. Since `{U,V}` and `T^(7e)` have the same
weight, their quotient is a scalar `c`. Cancellation gives
`{V,H}=-2cU`; reduction modulo `T`, the central Poisson identity, and
`U0!=0` force `c=1`. Thus specialization at `T=1` is a polynomial
Jacobian-one pair. Finally, injectivity of the degree-`e` associated-graded
map prevents cancellation of every nonzero initial form, giving
`delta(F*f)=e delta(f)`. The appendix uses the full relation, not a truncated
or localized lift, and introduces no classification premise.

## Ledger delta

I read the complete 45-line preview and 29-line mutation plan. The current
SHA-256 values of `AUDIT.md`, `PROGRESS.md`, and `APPROACHES.md` equal the
three declared old hashes. The two replacement anchors occur exactly once;
the append is literal. Applying each proposed edit in memory reproduces the
declared new hashes `a539fdd69454bc2ea3b281ffc45a7282dc5646400e17c089104197edb7107266`,
`cf048c100b8173f311c4c3fceddac0a8d60880efba7143a98741bfa57b16e3b3`,
and `29254ba7f315ae3638a97fbdb73e5c9400b568bddc3a0bf020975a9c6cf89ab4`.
The prose states the exact conditional theorem, links the sealed producer and
this planned review filename, distinguishes the static example from an actual
attachment, and explicitly leaves other targets, the infinitely singular
branch, general finite-normalization gap, properness, and JC2 open. No ledger
edit was made by this reviewer.

## Limitations and custody

This is a final artifact/appendix/ledger delta review, not a foundation
re-audit or novelty certificate. The public proof was read whole (172 lines),
as were its manifest, the ledger preview, and ledger plan. My own freshly
hashed MARKEDVERIFY proof/source and governor coverage was reused unchanged.
Frozen STATE299 matched HQ launch exactly before structural review; all 42
fixed pins and all 11 archives passed before reliance. No history or web
query, new source, new science, paid or child lane, Git/shared-ledger edit,
protected access, cloud/auth action, promotion, or successor occurred.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — this review raises no `OPEN[...]` entries.

Corpus basis: `db01d6034600ce8e85ed706db2d4e8fa4359f4fe` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4113`.
- Body SHA-256:
  `3d0ed92523494a5ac82a81e5642996c08fe1aef4da08813ff28ea3def08c2476`.
- Frozen basis: `db01d6034600ce8e85ed706db2d4e8fa4359f4fe`.
