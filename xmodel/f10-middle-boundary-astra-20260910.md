# Middle denominator boundary: GAP, integer issue isolated

First action 2026-09-10 06:22:48 UTC; cap 06:32:48, reserve 06:30:48. Three current-pinned inputs only; exact WHOLE/reuse scope is recorded separately. Manual mathematics, zero scientific execution.

**Verdict:** neither uniform integer nonvanishing nor an actual integer boundary pair is proved. ROOT's suggested numerator is verified. A uniform real-root control shows why a sign exclusion on the real cone cannot finish the task.

Put d=h-r-1, m=3r+1, x=d/m, y=r/m. From accepted P0, substituting sigma=4-x, A=-3-x and pi=4-2x-y²+xy gives

    B2=11+6x+x²+y²-xy,
    B3=-50-35x-10x²-x³-10y²-2xy²+10xy+2x²y,
    72P0=5x³-27x²+63x-9
          +36y²+108xy²-36xy-108x²y.

Thus N=72m³P0 is exactly

    5d³-27(m+4r)d²+(63m²-36rm+108r²)d
       -9m(m²-4r²),

or, after m=3r+1,

    5d³-(189r+27)d²+(567r²+342r+63)d
       -(135r³+207r²+81r+9).

The factored constant is -9(3r+1)(r+1)(5r+1), checking its sign and coefficients independently.

For fixed r>=2, N is strictly increasing on real 0<=d<=r: its second derivative 30d-378r-54 is negative there, while

    N_d(r)=204r²+288r+63>0.

Also N(0)<0 and

    N(r-1)=8(31r³-12r²-60r-13)>0.

The latter positivity follows from r²(31r-12)>=4(31r-12), leaving 64r-61>0. For every r>=3,

    N(1)=-135r³+360r²+72r+32<0:

it is bounded above by -45r²+72r+32, negative at 3 and decreasing thereafter. Hence precisely one real boundary d_r lies strictly between 1 and r-1 for every r>=3. This is a changed-domain control, not an integer counterexample or an allowed leading point. For r=2 the only integer d=1 gives N=536, so P0=67/3087, consistent with the accepted gate.

The exact unresolved assertion is d_r not an integer for every integer r>=3. No sampled residue table, rational-point classification, descent or integral-point theorem establishes it here. The real-cone control rules out a uniform positivity argument but does not refute integer nonvanishing. Consequently the P0=0 branch stays retained, and no global W elimination is licensed by this task.

No new OPEN ID. Remaining quantity: one possible integer zero per r, uniformly unbounded r. Cheapest decisive next mathematical check is a uniform integral-point obstruction for this single cubic, or one actual integer pair; neither was obtained. This compact GAP is not offered as a review-worthy unit theorem. Full leading equations, guards, forcing and source/JC2 questions remain untouched. Own-only targets were absent; own WHOLE/OPEN/collision check precedes the marker. No follow-on or execution authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2632`.
- Body SHA-256:
  `c8f15a3145abc44e8c88636b132de9f47abe9845c3bf925ba720557a59ae8b91`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
