# AWS execution custody — confirmed TD6 two-center hostile review

The different-model hostile review
`xmodel/td6-c1-c3-two-center-cover-review-claude-20260825.md` is **CONFIRMED**
(SHA-256
`56c4ece1224c723f8bbe107f0c9af6776dc0affcb03923a394628838923bde19`).
Its staged independent probe was executed on AWS Box03 and exited `0`.

The frozen final probe has SHA-256
`af2b91640ff61d73c6c39146e448ddd1428fa83c2274c0d78f8032f0716a507b`;
stdout has SHA-256
`5dbd50253f6fdbe27cc9ce4e9b1c15f890e36a7f39fd2640185b7ce198c459df`;
`/usr/bin/time -v` stderr has SHA-256
`d2c1ae07280153137c7f4d7fb950ceaad9f1e1b5a617d3309c0256c45d0d3ec2`.
The stdout contains 108 explicit PASS assertions, four INFO lines, and the
final `PROBE PASSED` verdict; its total line count is 114.  Runtime was 0.10 s
with maximum RSS 19,040 KiB.

The probe closes the review’s execution-side residual condition: it
recomputed the frozen hashes, extracted and source-verified V4--V7, pinned
the producers and archived parents, and independently recomputed the charged
polynomial, resultant, field-unit, irreducibility, norm, and residual checks.
An initial harness-only failure selected a macOS AppleDouble top-level entry;
the final frozen probe explicitly selects the extracted payload directory.

Portable evidence and custody metadata are frozen separately at
`cases/td6_c1_c3_two_center_cover_review_aws_20260825/`.  This supplement does
not mutate the original producer package and does not enlarge the theorem:
only the frozen source-typed section `(c1,c2,c3)=(C,1,U)` is killed at the
first-band/P12 gate.  No full centering family, neighborhood, SP-2, maximum-
degree, or JC2 conclusion follows.

