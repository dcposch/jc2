# V81A initial-launch deployment erratum

The first dual launch at tags
`td6_v81a_joint_transport_{r6d,box03}_20260826T0210Z` exited before producer
math because the wrapper selected `/usr/bin/python3`, where `python-flint` is
not installed.  Both traces ended at `ModuleNotFoundError: flint` during the
frozen import chain.  No producer banner, transport row, rank, table, or
mathematical conclusion was emitted.

The corrected runner pins `/home/ubuntu/venvs/td6/bin/python3`, first imports
and prints the `python-flint` version, and otherwise leaves the producer bytes
unchanged.  The failed launches are deployment-negative custody only.
