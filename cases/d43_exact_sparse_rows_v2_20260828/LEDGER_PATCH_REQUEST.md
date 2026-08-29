# Coordinator ledger patch request

No top-level canonical ledger was edited by this packet author.

After hostile PASS, the coordinator should mark the v1 direct-exact packet as
superseded for launch and cite the final v2 implementation-report and source
seal hashes.  Historical v1 hashes should remain in provenance rather than be
silently replaced.  The ledger must preserve the claim boundary: v2 emits
finite raw-J rows and contains no solver.
