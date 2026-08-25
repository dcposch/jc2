# AS F-only `D=7`: complete Q9-fibre exclusion at the first predecessor

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL
SOURCE/COMPILER REVIEW.**

## Exact scoped theorem

Fix the first Q9-compatible corrected-Q10 predecessor emitted by the frozen
vertical source-state gate.  In predecessor coordinates

```text
(Pp,Qq,Rr,Tt,s,w,h,
 fua,fa,fb,fc,fd,fvb,
 d7_1,d7_4,d7_7,d6_1,d6_4,
 c5_0,c5_1,c5_2,c5_3,c5_4,c5_5,
 d5_0,d5_1,d5_2,d5_3,d5_4,d5_5),
```

it is the point `c5_5=2` with every other coordinate zero.

There is no assignment over `F3` to all 19 Q9-kernel coordinates, all 32
raw Q8 digits, and all 18 raw Q7 restoration digits satisfying

```text
23 explicit Q9 source rows,
22 explicit Q8 source rows,
19 explicit Q7 source rows,
46 terminal coefficient rows in total degrees 9,10,11,12.       (1)
```

The Q9 source matrix has rank 13 in 32 restored coefficients, so its exact
origin-plus-kernel parametrization has dimension 19.  All 19 coordinates
are symbolic in this formula.  Consequently (1) excludes the complete Q9
affine fibre over this predecessor, not merely the previously frozen
13-trit Q8-compatible subchart.  The 23 Q9 rows are imposed again on the
symbolic coefficients as a self-audit.  The Q8 and Q7 variables are raw;
there is no fixed-matrix, RREF-section, zero-section, or representative
extrapolation premise.

## Circuit and checked certificate

The producer hash-pins the reviewed raw-Q7 circuit and changes exactly two
typed pieces: the Q9 variable count from 13 to 19 and the chart header from
the six-equation Kuranishi locus to the full 19-dimensional kernel.  Exact
replacement counts are asserted before execution.  Every downstream source
row, divided-carry gate, and terminal row is inherited byte-for-byte.

The source-pinned circuit uses 32-bit residues modulo 729 and reduces after
every gate.  Its maximum unreduced product is
`728^2=529984<2^20`, and it contains 35 exact division constraints.  A clean
one-millisecond Z3 smoke run emitted the formula and returned `unknown`; the
SMT2 payload is 870,585 bytes with SHA-256

```text
0061e1ccd62c849d54db9258247413d8fe80bf8cdf696ef987ea904fae89fd5d.
```

Boolector 1.5.118 returned `unsat` in 11.27 seconds with 97,336 KiB maximum
RSS.  Pinned `z3-solver` 4.16.0 then applied
`simplify -> bit-blast -> tseitin-cnf`, producing

```text
6,184,696 variables
29,430,517 clauses
CNF SHA-256 a25c7ed0f48766548fc518f9de2b4c7d4e51e413c085dc30f68d6668f1928369.
```

CaDiCaL 1.7.3 emitted the textual DRAT trace with SHA-256
`b8dbb0649833f5c545190e6b56e0efb4c9721385f08a553fdfd92d25ff956eda`.
Independent `drat-trim`, commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, binary SHA-256
`92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a`,
reports

```text
s VERIFIED
67,643 / 29,430,517 clauses in core
883 / 3,634,962 lemmas in core
6,570,804 resolution steps
0 RAT lemmas in core.                              (2)
```

## Controls and provenance

The terminal-omission positive control from the embedded 13-trit subchart
is also a literal point of this 19-dimensional fibre.  Boolector finds it
SAT, and independent integer replay verifies all 23 Q9, 22 Q8, and 19 Q7
source rows, recursive/literal `/243` agreement, and exactly one nonzero
terminal coefficient.  Its model and replay JSON hashes are

```text
6cd687baf9835ab7814af17c6d4825dec5a7e0e9ab96e2f3e2508e3c54d01e5f
877641bb3bd1d39af275be5cea057048cd3be8e1f8b880f6776e34303290c866.
```

The first emitter launch accidentally inherited a two-hour Z3 timeout and
was TERM-stopped after the SMT2 bytes were written.  It is retained only as
a deployment negative control.  The clean one-millisecond emitter exited
zero and produced byte-identical SMT2 before any solver evidence was
consumed.

All substantive work ran on Box02 under
`/home/ubuntu/jobs/as_first_predecessor_full_q9_rawq7_20260825T0712Z`.
The 225 MB custody archive contains source closures, both emitter records,
the embedded SAT/direct-source control, formula, CNF, DRAT, proof-check
output, Z3 wheel, and checker source/binary.  Its remote path is
`/home/ubuntu/jobs/as_first_predecessor_full_q9_rawq7_custody_20260825T072254Z.tar.zst`
and its SHA-256 is
`601076db6aa5f27e74315657baf7c5a87c2ad64982011612064ee26c1c3f5649`.

## Coverage ledger and refusal scope

This result kills exactly one of the 11,881 Q9-compatible corrected-Q10
predecessor states in the aligned vertical chain, albeit with its entire Q9,
Q8, and Q7 fibre at this gate.  The other 11,880 predecessor states across
the surviving structural bases remain open.  The separate `a` and `g`
endpoint families from the degree-ten gate, the fat/nonreduced incidence at
their intersections, and other associated-top branches are also outside
scope.

The highest-information successor is one symbolic predecessor formula over
the frozen vertical predecessor equations and all Q9/Q8/Q7 variables.  A
single SAT model would give a direct-source survivor; a checked UNSAT proof
would kill the whole aligned vertical predecessor locus without 11,880
independent certificates.  There is no all-depth/no-lift, characteristic
zero, counterexample, or Jacobian-conjecture inference here.

