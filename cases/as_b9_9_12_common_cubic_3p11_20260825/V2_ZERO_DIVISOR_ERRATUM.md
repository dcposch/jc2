# V2 zero-divisor erratum and quarantine

The V2 emitter source is preserved at SHA-256
`ab85df4824042f9919e535ad9b2d9c4213deb1aa2ed953ae6fa6aed4c66a7556`.
Its helper

```text
bv(value) = (_ bv(value mod 177147) 64)
```

was incorrectly used for the modulus itself.  Consequently every generated
`bvurem` divisor `bv(MODULUS)` became the 64-bit zero constant, and the
coefficient bounds `bvult h_i bv(MODULUS)` became `h_i < 0`.  The emitted
SMT SHA-256
`182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604`
therefore bit-blasts to the trivial empty-clause DIMACS
`p cnf 0 1`, SHA-256
`69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394`.

The V2 Boolector/Z3 `UNSAT` outputs and their trivial DRAT verification are
**invalid-formula negative controls only**.  They say nothing about the
mathematical common-cubic locus.  No frozen parent calculation is affected.

V3 uses a distinct raw-width constructor for the positive modulus/divisor,
audits every remaining residue constructor call, emits the patched source as
a hashed custody artifact, and must be reviewed independently before any
mathematical use.
