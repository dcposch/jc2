# V85TF1 deployment erratum

Date: 2026-08-26

The mathematical preregistration did not change.  Three diagnostic launch
generations are excluded from theorem evidence.

1. The first Box02 q2 / Box03 q10 pair used archive
   `b5fdfa580e4bd85510d292cf799d46b1505544d92e8661740d4c1c27a31b2993`.
   Both workers were deliberately terminated before certificate ingestion
   after static inspection found that the exact polynomial parser did not
   remove spaces emitted around subtraction.  No PASS or mathematical
   verdict was produced.
2. The second pair used archive
   `7b2e84c27ad5999efd79773cfd2ef1d1fc77ae8c6cce68d0cf058b03ac83f427`.
   Both returned `rc=1` after the generic raw P12 build.  The imported q-jet
   compiler state had not been restored before the independent `F=0`
   transport rebuild, so base transport received an `EJet` object where its
   exact coefficient field was required.  The traceback ended in a Python
   `TypeError`; it did not reach base-change comparison or any mathematical
   assertion.
3. The r6d q2/q10 optimization pair used archive
   `467bd2f096381dcd4a7aed8583f8009e5d59695972002c62e3f49cd163281f7a`.
   Those workers inherited the same state-restoration defect and were
   deliberately terminated once the second-pair traceback identified it.
   No PASS or mathematical verdict was produced.

The repair snapshots the original `qd` base compiler objects at import and
restores every object changed by `configure_qd_jet` before and after each raw
source build.  Only runs using the later archive pinned by the final result
may be consumed as producer evidence.
