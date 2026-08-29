# Hostile review request: exact K00 syzygy-origin projection V16R1

Act as an adversarial algebraic-geometry and computer-algebra reviewer.  Do
not trust the producer's prose, stored ranks, branch label, validator, or
hash claims.  Work read-only except for the single review output named
below.  Do not edit any canonical ledger and do not touch `jc2-lean`.

Review the exact-Q claim in:

```text
cases/max12_812_order2_u2_62_k00_syzygy_constant_projection_v16r1_20260827/
```

The claimed narrow theorem is: for the unloaded `C6=1` K00 rows in
`R=Q[d0,...,d5]`, the full polynomial syzygy module of
`(r1,...,r7)` has origin-evaluation rank one and every evaluated syzygy has
coordinates 2, 4, and 6 zero.  Since a syzygy with unit seventh component
exists, every local representation `r7=sum(q_i r_i)` has
`q2(0)=q4(0)=q6(0)=0`.

Required hostile checks:

1. Verify the frozen source hashes and portable evidence manifest from the
   actual bytes.  Notice that the producer-origin
   `run/PRODUCER_ARTIFACTS.sha256` contains absolute AWS paths; treat it as
   provenance only and use the portable top-level `EVIDENCE.sha256` for a
   local custody check.
2. Explain why original V16 is nonpromotable: it incorrectly made the
   `NO_COORD6_FREEDOM` outcome a process failure.  Confirm V16R1 genuinely
   accepts both preregistered branches and used new tags/source bytes.
3. Independently reconstruct the seven exact rows from the frozen replay
   prelude.  Parse the frozen 87-generator module, replay all 87 identities
   `sum_i S[j][i] r_i=0`, and confirm it is the serialized output of the
   full `syz(r1,...,r7)` computation used by V14R1, not a hand-picked subset.
4. Independently parse all 609 exact origin constants.  Recompute the 7x87
   rank over Q, the `(6,7)` projection rank, and whether rows 2, 4, and 6
   vanish identically.  Do not accept the integers in `RESULT.json` or the
   producer validator as evidence.
5. Independently replay the seven serialized base-syzygy component bytes in
   a fresh exact-Q process.  Require a literal-zero polynomial residual and
   independently evaluate its seventh component at the origin.  Check the
   claimed origin vector `(-200,0,-960,0,-5120,0,-40960)`.
6. Adjudicate the localization-completeness step carefully: any syzygy over
   `R_m` clears by a common denominator `s` with `s(0)!=0` to a polynomial
   syzygy, and evaluation is multiplied by the nonzero scalar `s(0)`.
   Confirm whether this really lets the complete polynomial evaluation span
   control all local representation freedom.  Track the sign when passing
   from a syzygy with unit seventh coordinate to
   `r7=sum(q_i r_i)`.
7. Treat `p=65521` only as a software control.  Check it did not silently
   substitute for exact Q.
8. Search for omitted denominators, a wrong distinction between
   `syz(r1,...,r7)` and `syz(r1,...,r6)`, incomplete module generation,
   unsafe normalization, characteristic leakage, or a way a local syzygy
   could evade the polynomial-span argument.
9. Enforce the firewall.  Even a PASS proves only unloaded order-zero local
   constants at normalized `C6=1`.  It does not prove a first-order load
   obstruction, a representation-invariant deformation cokernel result,
   honest `Lambda<=19` reachability, closure incidence, order two, maximum
   twelve, or JC2.

Return `PASS`, `FAIL`, or `NOT AUDITABLE`, list exact independent checks and
any repairs, and state the strongest theorem justified by the bytes.  Write
the completed review only to:

```text
xmodel/max12-812-order2-k00-syzygy-projection-v16r1-hostile-review-REVIEWER-20260827.md
```

