# TD6 V87R1 exact V87-to-V86 q2-specialization repair

Date: 2026-08-26

Status at freeze: producer preregistration; no result claimed.

## Review defect being repaired

The independent V87 hostile review found no error in the represented all-q
identity, but returned `REPAIR` because V87 did not explicitly compare its
q2-only specialization against the promoted, hostile-reviewed V86 outputs.
Shared source code and matching term counts are not a comparison.

## Exact acceptance gate

Rebuild live V87 P12, all 38 FIRST maps, `h_F`, and the augmentation quotient
`h_2` over the untruncated all-q ring. Then set every q coordinate except q2
to zero and require:

1. all 39 source digests, under the documented V86 exact serializer, equal
   the frozen V86 full-beta source digests;
2. the cleared V87 `h_F` table is byte-identical to frozen V86
   `TOTAL_F_Q2_HF_CLEARED.tsv`;
3. the cleared V87 `h_2` table is byte-identical to frozen V86
   `TOTAL_F_Q2_HBETA_CLEARED.tsv`;
4. localized h digests equal the V86 exact-result pins;
5. all live V87 source/h digests also reproduce the frozen V87 inventories;
6. one common clearing is exactly `U*H`, introduces no F/q inverse, and
   makes every emitted h coefficient polynomial;
7. two AWS clients emit byte-identical mathematical evidence.

The comparator consumes the frozen V86 corrected hostile review and
promotion record. Any mismatch is a closed failure and controls V87 prose.

## Scope

A pass repairs only the V87-to-V86 specialization custody gap. It does not
add a new source chart, a unit-q theorem, or any whole fixed-A3, TD6, SP-2,
or JC2 claim.
