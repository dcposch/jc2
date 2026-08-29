You are the hostile different-model reviewer for one narrow AS109 theorem.
Work in `/Users/dc/code/math/jc2`.  Write exactly one file:

`xmodel/as109-n6-low-witt-common-core-cartier-hostile-review-grok-20260827.md`

Do not edit any other file.  Do not use or inspect `jc2-lean`.  No web is needed.  No heavy local computation; the registered
Python replay is desk scale.

Charged producer:

`xmodel/as109-n6-low-witt-common-core-cartier-producer-sol-20260827.md`

Required SHA-256:

`c79dfbf550962c1fcbae974b6fe1ab1867489ceb8a93906ad4b7739a49522526`

Read the producer in full, then read every history artifact and frozen case
file it names.  Recompute all hashes and rerun the frozen replay.  Independently
derive, without trusting producer PASS strings:

1. the exact packed determinant identity for
   `P=x-x^109+109A`, `Q=y+109B`;
2. every coefficient row of the first-Witt divergence equation, especially
   `a5'+6b6=0` when `deg_y B=6`;
3. the exact image/cokernel of `d/dx` on `F_109[x]`;
4. the passage from primitive common-core data
   `q6=beta*h^(6/d)` and `v109(beta)=1` to the Cartier condition on
   `(bar h)^b`, including possible degree drop modulo 109;
5. the claimed leading-degree exclusions `Hbar!=108` for `d=6` and
   `Hbar!=54` for `d=3` modulo 109;
6. the extra `p_m` valuation/gcd implication and whether UFD really forces
   `bar h` to be a 109th power up to scalar;
7. every positive and negative control; and
8. novelty/scope relative to the stopped top-two-band calculation, support
   gate/carry erratum, wild-symplectic, polar-conductor, and prior Cartier
   work.

Actively seek the smallest missing hypothesis or counterexample.  In
particular attack integrality of alpha/beta, reduction of a primitive h,
content normalization, cancellation in `(bar h)^b`, the distinction between
`deg h` and `deg bar h`, and whether the low row actually supplies a new
constraint rather than a known tautology.  Do not infer existence or
nonexistence of a lift.

Write one self-contained Markdown review to the exact output path above,
with a headline verdict from `CONFIRMED`, `CONFIRMED_WITH_REPAIR`, `GAP`, or
`REFUTED`; a numbered claim table; independent derivation; replay/hashes;
novelty adjudication; licensed conclusion; and explicit scope firewall.
After the file is complete, print only its path and SHA-256 to stdout.  Do not
write any other file.

