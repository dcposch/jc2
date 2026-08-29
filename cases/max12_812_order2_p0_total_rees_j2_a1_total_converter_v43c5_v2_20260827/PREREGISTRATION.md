# V43C5 V2 preregistration: corrected literal-row census and total `a1^628`

## Frozen question

In the ordinary polynomial ring `S = Q[t,X19_total]`, with the exact map
`t |-> rho^2`, replay the V43C5 converter from the reviewed V43C4 special
certificate and reviewed V43G4 generic certificate.  The only change from
V43C5 V1 is a fail-closed correction of the literal source census:

- the frozen source has 70 named row slots (`Tg10_1` through `Tg19_7`);
- exactly 59 of those literal total rows are nonzero; and
- exactly 11 named slots are the zero polynomial.

V1 incorrectly required the 70-entry named-slot hash map to have length 59.
Its AWS run therefore stopped before building a converter certificate.  V1
remains immutable and is evidence only of a pre-certificate software failure.

## Additive census contract

V2 must reconstruct the pinned V43 source and independently require:

1. the complete expected 70-name alphabet and a 70-entry hash map;
2. 59 unique nonzero row records and 11 complementary zero-row names;
3. the canonical hash of every nonzero literal row agrees with its named-slot
   hash;
4. every complementary slot has the canonical hash of the zero polynomial;
5. all 66 positive variables, the 65-variable rho-zero alphabet, and the sole
   general-only variable `ez9` agree with the frozen source; and
6. the serialized proof records the full hash map, its nonzero and zero
   submaps, and the exact zero-row-name list.

The serialized replay must reject both deletion of one zero-row name and
corruption of one zero-row hash.  These controls are additive to every V1
algebraic mutation; they do not change the converter identity.

## Registered identity and verdict

All V1 algebra remains unchanged.  If

`a1^104 = sum C_j R_j(0)`

and

`t^6*a1^4 = sum (G_i/5) R_i(t)`,

put `H=-sum C_j (R_j(t)-R_j(0))/t`, `x=a1^104`, `y=tH`, and
`Phi=sum_(k=0)^5 x^(5-k)y^k`.  The registered multiplier circuit must replay

`a1^4*((x-y)*Phi+y^6) = a1^628`.

Only
`PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5-V2`
with a complete frozen proof/result is a provisional positive verdict.  Run
on AWS only, one core, at most 8 GiB virtual memory and twenty minutes.  The
same scope/firewalls as V1 apply; in particular this proves only membership in
the literal total raw ordered-a1 grade-through-19 ideal and says nothing about
terminal-receiver reachability without a separate chain map.
