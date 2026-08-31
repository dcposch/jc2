# Degree-eight invariant-cell reconnaissance result

Status: **NO CAS RESULT; PACKET CORRECTED AND FULL SEARCH RETIRED**.

The initial three actual lanes and one target-3 control all failed closed in
the generator before Singular started. The packet had counted `57` raw
nonconstant monomial coefficients as if they were `57` distinct coefficient
polynomials. Four coefficient polynomials repeat, so the actual ideal has
`53` unique generators. The target-3 mutation similarly has `58` raw
coefficients and `54` unique generators. Two later count-only diagnostics
independently exposed `53` and `54`. No lane produced a Gröbner basis or any
mathematical emptiness/nonemptiness result.

The corrected R2 generator freezes both raw and unique counts. It replays
identically under normal Python, `-O`, and `-OO`, and is covered by the
campaign test suite. The source and launch pins are recorded in
`AWS_REGISTRATION_R2.md`.

## Why the full run is retired

Every pair in this packet has total pullback degree at most eight. If its
Jacobian is the nonzero constant `2`, rescaling one coordinate gives a plane
Keller pair of the same degree. Moh's degree-at-most-100 theorem therefore
makes it a polynomial automorphism. But the horn packet requires geometric
degree `4*mu=8` at `mu=2`, whereas an automorphism has geometric degree one.
Thus this bounded cell cannot contain the required horn, independently of a
Gröbner computation.

Primary source anchors:

- T. T. Moh, *On the Jacobian conjecture and the configurations of roots*,
  J. Reine Angew. Math. 340 (1983), 140--212,
  <https://doi.org/10.1515/crll.1983.340.140>.
- Moh's author page states the degree-at-most-100 result explicitly:
  <https://www.math.purdue.edu/~ttm/jacobian.html>.

The corrected packet remains available only for reproducibility or for a
future, explicitly registered structural-identity question. It is not an
active counterexample search.

## Retrieved evidence custody

Each `EVIDENCE.sha256` below rehashes every non-supervisor payload and run
file in its directory. All six supervisor logs are empty (SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).

```text
fe26de237343998856ce4bd55a3f23b0ed91bba1dd6374a9e3f66be4cde70278  aws_r6a_quartic_inv_mu2_d8_p32003_actual_slimgb_20260831T0550Z_r6a/EVIDENCE.sha256
d8e139dacd0b9f1f9b9f1c53ec3a7b152f0f069603624b485723b4e023aa7587  aws_r6b_quartic_inv_mu2_d8_p65521_actual_std_20260831T0550Z_r6b/EVIDENCE.sha256
697aef81ef9454eba3e2831a0ad9cb1abe1791833bfceaf2d5e69e19e2a49a4b  aws_r6c_quartic_inv_mu2_d8_p104729_actual_slimgb_20260831T0550Z_r6c/EVIDENCE.sha256
22c9676b0c808bf9fada5c9638c032bad068fcc08813867a3d04dc1fbb86f67b  aws_r6d_quartic_inv_mu2_d8_p32003_target3_std_20260831T0550Z_r6d/EVIDENCE.sha256
eedb4f615cfc731d5c9c93892d0d53225561dc97ef897ed121dfe015e0c5e269  aws_r6d_quartic_inv_mu2_d8_p32003_actual_count_r1_20260831T0600Z_r6d/EVIDENCE.sha256
6c89de8e20b344cbec9d7b380297d7bd2225bb3fdfb291b96bf9413bdf3bf287  aws_r6d_quartic_inv_mu2_d8_p32003_target3_count_r1_20260831T0600Z_r6d/EVIDENCE.sha256
```

Interpretation is deliberately negative: these receipts prove that the
runner refused a mismatched packet and that the diagnostics recorded the
deduplicated counts. They do not prove the ideal empty.
