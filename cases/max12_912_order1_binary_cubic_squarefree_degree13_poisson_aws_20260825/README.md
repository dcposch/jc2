# Squarefree degree-13 Poisson collapse gate

Dual AWS exact replay verifies both the denominator-cleared rational
degree-13 original row and the direct polynomial original row after
`C=K*L`, `W=K*M`.  The pole numerator is factored exactly.  At reduced
geometric points the preceding `K|C*W` allocation plus this polynomiality
condition forces `K|C` and `K|W`; this is a squarefree rootwise argument, not
a nonreduced ideal identity.  Predicted dimensions are `21+5=26`.

Accepted tags:

- `max12_912_order1_squarefree_degree13_poisson_v2_r6d_20260825T1937Z`;
- `max12_912_order1_squarefree_degree13_poisson_v2_box02_20260825T1938Z`.

Both return rc0 with byte-identical verifier stdout and peak RSS
12,736/12,524 KiB.  The first r6d attempt used Singular's reserved `ZZ`
identifier and was rejected by the diagnostic gate; it is remote routing
custody only.  Run `python3 replay.py`.
