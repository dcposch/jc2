# Hostile audit custody — B9 normalized common cubic at `3^11`

This is a distinct, AWS-only hostile audit of
`cases/as_b9_9_12_common_cubic_3p11_20260825/`.  It does not modify or
replace the V2 producer, its quarantine, or V3.

The audit has two conclusions:

1. V2's `UNSAT` is an invalid-formula verdict.  Its residue constructor was
   used for the modulus itself, so the emitted formula contains
   `bvurem(..., 0)` and `h_i < 0`.
2. The intended finite gate is **SAT**.  An independent integer
   staged/Kuranishi reconstruction, which never reads the producer SMT,
   emits a literal mod-`177147` witness.  A second small verifier replays the
   displayed B9 parent modulo `243`, degree bounds `(9,12)`, determinant one,
   both leading units, and all 23 normalized common-cubic top rows.

Key hashes are:

- independent compiler: `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8`;
- independent result: `fad73f36b609363f0ee8cde84f9ffd89233913ec9e036b00441ee11de5e8307f`;
- literal witness: `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`;
- independent verifier: `eba7d223b88fd61da246fd766a3c5f4f73163e9b0261263d64406779671d6689`;
- verifier result: `2008726f5791b86b3c4f6e5b296cbbf4cdfa91766290c1d32aeec81e4a52c67a`.

This proves one finite-depth SAT point over one fixed B9 mod-243 parent.  It
does not prove an all-depth tower, an inverse limit, a scheme dimension, a
characteristic-zero map, a counterexample, a maximum-twelve theorem, or JC2.

All substantive computation ran on AWS Box02.  The Mac was used only for
text inspection, hashing, SSH orchestration, and custody import.
