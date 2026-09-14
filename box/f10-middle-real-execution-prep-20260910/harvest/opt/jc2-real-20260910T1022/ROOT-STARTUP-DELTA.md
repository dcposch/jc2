# ROOT startup delta — 2026-09-10 09:56 UTC

This narrow supplement does not reset the original runtime implementation
cap (10:02:13 UTC) or publication reserve (09:59:13 UTC), and authorizes no
execution. The frozen ROOT-CARD.md remains unchanged at SHA256
43643a6ee8546be56592237d62ac4b1a0ce16d47980c2ba895355f27ba015c4b.

Add `-S` to the full registered Python startup flags: scientific/probe
children use `-E -s -S -B`, with the trusted immutable script directory still
available for the accepted sibling authority import; sibling-free dispatcher
and CAPRUN use `-I -S -B`. Exact real CLI wrong-job preflights must exercise
these same flags. No accepted scientific source change is requested.

Rationale: Python's official command-line reference states that `-I` implies
`-E`, `-P`, and `-s`, but not `-S`; `-S` suppresses automatic site import and
its path changes. `-B` prevents writing bytecode but does not establish that
existing bytecode is unreadable. ROOT's separately prepared native manifest
must therefore also account for installed standard-library bytecode and any
standard-library ZIP path, not claim that source-only hashes close startup.
Reference: https://docs.python.org/3.12/using/cmdline.html

These are future entry-contract requirements, not a tested runtime claim.
Hash and read this whole supplement before relying on it; pin it in custody.
If the original cap precludes a complete implementation, report that gap
within the original cap, without adding time or executing anything.
