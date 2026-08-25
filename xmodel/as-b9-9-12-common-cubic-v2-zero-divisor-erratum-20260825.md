# Erratum: normalized B9 common-cubic V2 encoded a zero divisor

Status: **RETRACTION OF V2 SOLVER EVIDENCE; PARENT FAMILY UNAFFECTED**

The normalized common-cubic V2 formula at SHA-256
`182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604`
does not encode arithmetic modulo `177147`.  Its residue constructor reduced
the modulus constant itself, so all 407 generated remainder divisors were
zero and every `h_i < 177147` bound became `h_i < 0`.

This is witnessed exactly by deterministic Z3 4.16 bit-blasting: the whole
formula simplifies to `p cnf 0 1` with SHA-256
`69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394`.
The instantaneous V2 Boolector/Z3 `UNSAT`, CaDiCaL result, and trivial DRAT
verification are quarantined deployment/encoding negatives, not
mathematical evidence.

The complete normalized mod-`3^11` family at result SHA-256
`984dbcf57ce181c5f07308f80950b38a9c78174cd9c802c868b46ce337e90539`
is unaffected: only the later common-cubic SMT emitter was wrong.  V3 has a
separate source, formula hash, raw-modulus constructor, and exhaustive
constructor-call audit.  No common-cubic SAT/UNSAT statement is licensed
until that corrected formula and its source are independently checked.
