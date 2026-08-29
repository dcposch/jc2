# Coordinator ledger patch request

No top-level canonical ledger was edited by this packet author.

After a fresh independent hostile review of this v4 seal, the coordinator
should mark the v3 packet as superseded for launch and cite the final v4
implementation-report and source-seal hashes.  Historical v1, v2, and v3
hashes should remain in provenance rather than be silently replaced.

The ledger must preserve the claim boundary: v4 emits finite
support-specialized raw-J rows and contains no solver; a successful run
confirms the preregistered 29/155 inventory rather than measuring one.
The packet status is `V4_REPAIRED_LAUNCH_NOT_AUTHORIZED`; no AWS launch is
authorized by this packet, and any future launch additionally requires the
coordinator's explicit GO after a hostile PASS plus a fresh immutable host
registration.
