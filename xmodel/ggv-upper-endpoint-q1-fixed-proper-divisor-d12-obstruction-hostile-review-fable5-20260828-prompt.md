# Assignment: hostile review of the fixed proper-divisor D12 obstruction

You are Fable 5, serving as an independent hostile mathematical reviewer in
the plane Jacobian-conjecture campaign.  Work inside
`/Users/dc/code/math/jc2`.

Write the final report, and only the final report, to

`xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-hostile-review-fable5-20260828.md`

You may additionally write one independent exact checker to

`xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-hostile-review-fable5-20260828-check.py`.

Use `/tmp` for all other scratch.  Do not edit any canonical campaign file,
case packet, adapter, log, or prior report.  Never enter, list, search, read,
build, status, or modify the nested user-owned `jc2-lean` tree.  Do not use
AWS, network access, Singular, Sage, SymPy, or another CAS.  Exact
standard-library Python and read-only shell commands are allowed.  Preserve
the dirty worktree.

## Charged artifacts

Verify these live hashes before using the artifacts:

```text
9903780f612f07c8afd6bd6d6318d4a086ae59c59e6a7e554609f2de1a1eb258  xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-sol-ultra-20260828.md
5f64ee850a3adc310b6a54cbcbe083e31c0ac877e777eacfec4c9983e368628e  xmodel/ggv-upper-endpoint-q1-post-d9-d11-proper-divisor-survivor-sol-ultra-20260828.md
24381cd505e9d507083c49f18c4eb45a3f55bee87446c2d0aa11a33b6fa203fb  cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/verify_q1_d12_obstruction.py
b2e0e3b9ed6ffb20328a044ae4172d0290597e5cbf088b62928ef480c24b4561  cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/RESULT.json
02070d01044cdfe4c9f511d798abbd08e74d20bf28f4a98fd60d5c716cd6adb3  cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/TARGET.json
11524630f770a96436583a6c70eaa92775d0565c1117397e4647bece9b57bb4c  cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/SOURCE.sha256
17af235557aeeaa981b33ee0c18555c6bed0e19e1aba76d0eeefdf0bd8ce919e  cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/EVIDENCE.sha256
```

The producer claims that one exact q1-compatible proper-divisor prefix
survives D10 and D11 with `A` not dividing `W`, but has no legal D12
extension.  It gives two certificates: a characteristic polar remainder and
a direct 28-row/16-column affine-dual obstruction.

## Mandatory independent checks

Do not treat replay of the producer checker as proof.  Independently rebuild
the relevant objects from the frozen predecessor/raw source and adjudicate:

1. Reconstruct the exact frozen `F0..F11`, `G0..G11`, q1 data, windows, and
   D0--D11 status.  Confirm that the predecessor really is a legal raw point,
   that `C=X-1`, `B=A/C`, and `A` does not divide `W`.
2. Independently derive the weight-12 characteristic recurrence.  Check the
   coefficient and sign of every predecessor term, the legal `F12` term, and
   the born `c12` mode.  Determine whether either can affect the polar class.
3. Recompute the numerator reduction and gcd data.  Verify or refute
   `g12_polar=Nred/(12 C^3 B^2)`, `gcd(Nred,A)=1`, `Nred(1)=-12`, and the
   serialized Bezout identity showing `Nred` is a unit modulo `B`.
4. Check the claim root by root: does the frozen prefix have an unavoidable
   pole at every individual `B`-root, independently of its separate
   `C`-root pole?  State carefully what is proved over rational/complex
   field points and what is not proved scheme-theoretically.
5. Reconstruct the literal raw D12 affine equation from the determinant
   operator and authoritative raw slot inventory.  Verify that the legal new
   slots are exactly three `F12` columns (`X^2,X^3,X^4`) and thirteen `G12`
   columns (`X^0..X^12`), with no omitted bound mode or window slot.
6. Independently compute the 28-by-16 matrix, its rank, augmented rank, and
   the proposed dual functional
   `20[X^0]+10[X^4]+4[X^8]+[X^12]`.  Check that it kills every legal new
   column and evaluates the base to exactly `11009739/16384`.
7. Run hostile mutations: wrong determinant sign/coefficient, one omitted
   legal slot, an illicit extra slot, and a changed dual coefficient.  The
   independent checker should detect each load-bearing mutation.
8. Explain exactly how this evidence bears on the proposed single-root
   transport/two-scale local model.  Do not generalize from this one fixture
   to all proper-divisor strata unless you supply a proof.

Return one of `PASS`, `REPAIR`, or `REFUTE`, distinguishing mathematical
errors from documentation/custody issues.  Give the strongest promotable
statement with hypotheses and scope firewalls.  Record every file read,
every command/check run, checker hash, and final report hash command.  No JC2,
branch-P-wide, scheme-unit, or universal transport conclusion is licensed by
a fixture-level result.
