# Produce a sealed exact K0 field certificate (R1)

You are Opus 5, continuing as the primary producer of the theorem in your
report.  Turn it into a small, independently reviewable certificate packet.
Do not merely restate the proof.  Encode the decisive identities and mutation
guards so a different engine can replay them exactly.

Do not access `jc2-lean`.  Do not run AWS or any local CAS.  Bounded stdlib
Python source checks are allowed.  Write only inside a fresh
`cases/d43_k0_field_certificate_r1_20260828/` plus one producer report in
`xmodel/`; do not edit the theorem report or top-level campaign ledgers.

## Charged theorem

`xmodel/d43-k0-splitting-primary-research-opus5-20260828.md`, SHA-256
`6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430`.

## Certificate requirements

Create two genuinely independent exact checkers:

1. a corrected PARI/GP script suitable for the AWS r6b PARI 2.15.4 host;
2. a stdlib-Python checker that does not call PARI and uses explicit integer,
   finite-field, and canonical quotient-algebra arithmetic.

Both must verify, with named fail-closed gates and hostile mutations:

- the literal source `Phi42` pin and rank-432 monic-basis theorem;
- the explicit two-way generation proving
  `B = Q(zeta42,r3,h) = Q(zeta168)` of degree 48;
- Kummer independence of `[3+r3]` and `[3-r3]`, preferably with two
  independent cubic-character primes (including 673) so no unexecuted
  degree-432 irreducibility claim is needed;
- hence `K0` is one field of degree 432, with idempotents only 0 and 1,
  Galois/nonabelian status, and the exact ramification set `{2,3,7}`;
- both registered frames, complete splitting/count 432, and the registered
  `p^2` Hensel replay;
- conditional on the literal displayed E polynomial, the explicit
  `q0 = u*(1+i)*(r3-1)/2` identities, direct substitution into E, four
  distinct `K0`-rational fourth-root branches, and both pointbank regressions.

Correct any syntactic/type issues in the report's illustrative GP recipe.
The theorem path must not depend on PARI `nffactor`, an absolute primitive
polynomial, or the modular pointbanks; those are corroboration only.  Directly
mutate each load-bearing identity (source polynomial, base generation,
character rank, frame, q0 coefficient/direct E substitution) and require the
mutation suite to fail for the intended reason.  Include a false mutation
that legitimately survives, as in the report, to guard against a vacuous
"all mutations fail" harness.

Provide an AWS-only, one-core, zero-swap, short-timeout runner with exact
host/instance/tag and source-hash gates, bounded memory/file output, immutable
artifacts, exact manifest/census/hash replay, and one final atomic terminal.
The terminal must distinguish the unconditional K0 theorem from the
E-conditional theorem.  No product decomposition or component list should be
emitted except the literal single factor `K0` and idempotents `[0,1]`.

Seal a deterministic source archive and write a hostile review request.
Status must remain `R1_SOURCE_READY_AWS_NOT_AUTHORIZED`; a different-model
source PASS and coordinator GO are required before execution.

Write the producer report only to:

`xmodel/d43-k0-field-certificate-r1-opus5-20260828.md`

End with exact hashes, bounded tests actually run, recipes not run, and the
claim firewall: coefficient-field theorem plus E-conditional ratio theorem,
not a D43 row/point/template/Keller/JC2 result.
