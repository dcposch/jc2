# Registration: exact global strict-Rees saturation

Status: preregistered, AWS-only, no verdict yet.

Input is the exact `strict_rees.sing` emitted by the registered compiler
lane.  The runner fails closed unless it is on Linux/Amazon EC2 with a
nonempty registered lane tag.  It records the Singular version and exact
input hash, applies a 256-GiB virtual-memory cap and 14,400-second inner
timeout, and executes through `ops/aws_exact_lane.sh`.

The computation performs sequential saturation by `tau` and `rho`, takes
the boundary, then saturates by the full coefficient irrelevant ideal.  A
unit result is fail-closed evidence against a strict algebraic boundary arc
for this fixed source.  A nonunit result is only boundary accessibility.
Neither outcome checks the two finite Taylor families, rational-section
descent, closes the order-two client, or proves anything about JC2.
