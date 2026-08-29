# Coordinator ledger patch request

No top-level canonical ledger was edited by this packet author.

After a fresh independent hostile review of this v3 seal, the coordinator
should mark the v2 packet as superseded for launch and cite the final v3
implementation-report and source-seal hashes.  Historical v1 and v2 hashes
should remain in provenance rather than be silently replaced.

The ledger must preserve the claim boundary: v3 emits finite
support-specialized raw-J rows and contains no solver.  The packet status
is `V3_REPAIRED_LAUNCH_NOT_AUTHORIZED`; no AWS launch is authorized by this
packet, and any future launch additionally requires the coordinator's
explicit GO after a hostile PASS.
