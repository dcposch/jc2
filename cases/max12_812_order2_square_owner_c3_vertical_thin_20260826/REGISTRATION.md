# Registration: generic-square vertical `c=3, r>=2` thin source replay

Date: 2026-08-26

## Question

On the generic unit-load chart `D(p*k0)`, after the reviewed `c=1,2`
gates and the reviewed `c>=4,r>=2` high-contact gate, verify the exact
complete-source bridge and the two-grade divisibility separator for the sole
remaining vertical family `a=0,c=3,r>=2`.

## Frozen design and acceptance

The client pins the final hand lemma SHA
`dd4005a92440e8241807bbe3bea4f9305de06c2d08fd0e095dc5dddba4bc7707`.
It regenerates all seven exact source/Faber rows through absolute grades
13--15, checks the lower-unitriangular Laurent bridge, and independently
checks the common-numerator identities for the displayed `H13,H14,H15`.

Over the etale root chart it must verify both deck orientations and:

1. `L | A0*E3` gives the opposite-root allocation;
2. `L^2*H14 mod L = -(3/8) B2*A0^2`;
3. for `r=2`, the complementary-root coefficient is a nonzero unit times
   `B2(root)`, hence forces the complementary factor of `B2`;
4. after that factor is imposed, `L^3*H15 mod v = -(1/16)A0^3`;
5. the same grade-15 identity is independent of `B3`, covering every
   symbolic `r>=3` without sampling;
6. omitted-connection and wrong-cubic-coefficient negative controls fire.

No radical or broad coefficient ideal is allowed.  Exact Q is the producer;
`F_65521` is a software control.  A failed shard is no mathematical verdict.

## Scope firewall

PASS eliminates only vertical `a=0,c=3,r>=2` finite-order faces on
`D(p*k0)`, conditional on the already reviewed first-normal setup.  It does
not eliminate `r=1`, horizontal `a>0`, `p=0`, `k0=0`, ramified slopes,
zero/infinity sections, the whole square stratum, order two, maximum twelve,
or JC2.

## AWS registration

Dual independent runs: exact Q on Box03 and `F_65521` on r6d.  Each is capped
at 24 GiB virtual memory, 600 seconds compilation, and 3600 seconds engine
time.  All substantive algebra runs on AWS only.
