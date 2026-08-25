# AWS-only Q7-kernel high-carry census

`compile_shard.py` evaluates one disjoint subset of the `3^9` Q7 kernel.
`aggregate.py` checks coverage, hashes the ordered stream, classifies the
high-row zero locus, and validates a quadratic presentation when one exists.
All substantive execution is remote.
