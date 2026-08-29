# Preregistration: complete colon-witness serialization V14R1

Date: 2026-08-27

Status: **FROZEN CUSTODY REPAIR; NO PROMOTED LOCAL RESULT AT REGISTRATION.**

V14's exact-Q process found a six-generator colon and a unit witness, and
checked its `6 x 6` lift matrix in memory.  The endpoint is not promotable:
Singular serialized only the first row of that matrix.  V14R1 changes no
ring, row, order, quotient, syzygy, witness-selection, or decision rule.  It
regenerates the byte-pinned V14 input and adds only proof serialization:

1. save each of all 36 entries `L[i,j]` in its own file;
2. save the chosen `h` and its six multipliers `u1,...,u6` separately;
3. recheck in the producer that `h*r7=sum_i ui*ri` and `h(0)!=0`;
4. construct a fresh replay script from the saved polynomial bytes and rerun
   the identity in a second Singular process.

The exact-Q lane is primary evidence and `p=65521` is control only.  Any
missing entry, wrong matrix dimension, nonunit `h`, sign error, diagnostic,
or failed fresh replay rejects the run.  A positive endpoint would prove only
that the unloaded `r7` lies in `(r1,...,r6)` in the local ring at the
normalized K00 coefficient point.  It would not prove mixed Lambda/load/
target reachability, closure-first incidence, Taylor realization, order two,
maximum twelve, or JC2.

