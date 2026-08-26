# Text-only hostile review — control-2 Rees monomial certificate

Act as a hostile tropical/commutative-algebra referee.  Text only: do not run
Python, Singular, Sage, msolve, Lean, Gfan, or substantive symbolic
computation on the local Mac.  Read frozen sources and already-emitted AWS
artifacts; lightweight hashes are allowed.  State that no local substantive
computation was run.

Audit

```text
cases/max12_912_order3_d1_double_root_control2_rees_certificate_20260826/
```

especially these frozen identities:

```text
48c7a6f9144b6b83fb57b2c80decb48208a7d3ff8fe880c77abb10631a09ef5d  FREEZE.sha256
abb769de9d9cf7fd1af43f96d32fcc148f79ba51844b1995e539baab7b84ebee  RESULT.md
d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088  aws_r6d/singular.stdout
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

Also read the complete v2 source package and its r6d B artifacts.  Charge:

1. Verify that `base_B.sing` is exactly the frozen expanded Rees-v2 source,
   and that `compile_certificate.py` changes only the embedded AWS tag and
   inserts basis/certificate printing plus a source-identical saturation
   cross-check.  Check anchor counts and hashes.
2. Verify the construction order: exact `s!=0` contraction of the full finite
   ideal; then `s=0`; then standard basis `GH`.  Decide whether `GH[34]=la^20`
   is genuinely in the full minimum-weight initial ideal, including all
   polynomial/S-polynomial consequences, rather than an artifact of merely
   taking initial forms of generators.
3. Search for dehomogenization, minimum/maximum-weight reversal, block-order,
   elimination, or hidden localization errors that could create `la^20`
   spuriously.  Explain why adding `s=0` after contracting, rather than before,
   matters.
4. Independently interpret `GH[35]=s`, `sat_with_exp=1`, direct reduction of
   `TORUS^1`, and inverse-variable torus localization.  Are these mutually
   consistent exact checks?  Is `la^20` alone already the canonical monomial
   obstruction because `la` is required nonzero?
5. Explain why every submitted generator initial can vanish at the displayed
   residue while the full initial ideal contains `la^20`: identify this as a
   tropical-prevariety versus tropical-variety/S-polynomial distinction.
6. State exact promotion scope.  The result may exclude only frozen
   `a=1,h=q2=k=nu=0,mu=2/3`, weight
   `(4,1,1,22,22,30,30,30)`, with all eight displayed coordinates nonzero.
   It must not exclude moving-axis or later `q2` directions, other
   supports/weights/residues/loads, the whole correction ray/fan, D1, or JC2.
7. Audit AWS custody: source hashes, rc zero, empty compiler/CAS stderr,
   separated time telemetry, exact PASS/no FAIL, and the v1 software-control
   firewall.

Encoding A is independent and may remain live.  Do not infer its endpoint.
Write exactly one report and make no other repository edits:

`xmodel/max12-912-order3-d1-double-root-control2-rees-certificate-review-grok-20260826.md`

End with one token on its own line:
`REES_CERT_CONFIRMED`, `REES_CERT_REPAIRED`, or `REES_CERT_REJECTED`.

