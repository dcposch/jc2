# Max12 `(9,12)` Q8 global-quotient AWS custody supplement

Date: 2026-08-25  
Status: **exact custody supplement to an already-CONFIRMED gate; no new theorem**

## 1. Result and scope

The completed AWS lane

```text
q8_global_quotient_evidence_20260825T000746Z
```

has been harvested byte-for-byte from r6d host `ip-172-30-0-45`.  Both its
frozen replay and its independently staged hostile probe exited `0` with
their stated PASS endpoints.  The parent manifest check lists every frozen
file as `OK`.

This supplement adds execution custody only.  It does not alter or enlarge
the already-CONFIRMED scope of
`max12-912-order3-nu-q8-global-quotient-gate-20260824`: the selected formal
branch has its exact quotient and reviewed local dimension statement, while
whole-scheme irreducibility, a global plane equation, projective closure,
rational trajectories, all `(9,12)`, maximum twelve, and JC2 remain open.

## 2. Frozen replay lane

The exact pinned source was

```text
cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/replay.py
SHA-256 f0f52954bed71b65b9219fd497f7ea2bbe6652144c463ca06f03391b87957fdd
```

It ran from `2026-08-25T00:07:46Z` through `00:11:56Z`, exited `0`, used a
maximum resident set of `139812 KiB`, and produced

```text
stdout SHA-256 d05eeb86d8c11b6463f25b18bff1a59b736a924bd3fcf619aaf23404f4e764a5
stderr SHA-256 facd8228633649bd642075b2c1a1244c26a9af744192d11ec00e1726fabc0ee1
```

The stdout is byte-identical to the frozen parent `replay.json`.  The stderr
contains only `/usr/bin/time -v` accounting and records exit status zero;
its supervisor stderr is empty.

## 3. Independent hostile probe lane

The harvested independent source is `q8gq_probe.py`, SHA-256

```text
9238fb05bf950953888f71513c4d7e580e6dd2b48455f2294d024941472bc2c3.
```

It ran from `2026-08-25T00:07:46Z` through `00:08:56Z`, exited `0`, used a
maximum resident set of `27080 KiB`, and produced

```text
stdout SHA-256 6e6acff244b6f7b11cc164b2738b79cb64357cffa141956e798ec925943fcf18
stderr SHA-256 c1ca408fe329e8370c0c46bbbc4d41a664978abf3355aa997587015ce2abc164
```

The stdout independently records:

- transitive dependency-pin import PASS;
- exact quotient identity for all eight rows at three independent rational
  points;
- weight homogeneity and the `n,q` weight-zero typing;
- exact report-table and `167`-versus-`230` monomial checks;
- fail-closed Hensel invertibility and six-row residual vanishing through
  `w^5`;
- output-unit, terminal-jet, payload-digest, and Pade-falsifier checks;
- exact rank `25/25` over `Q` for the full tested `(n,q)` box; and
- a third-prime rank PASS for all `48` tested `Z` boxes.

Its stderr likewise contains only `/usr/bin/time -v` accounting with exit
status zero; its supervisor stderr is empty.

## 4. Custody checks

The AWS launch metadata pins the replay and hostile-probe source hashes and
the `128 GiB` virtual-memory guard.  `manifest.stdout` is preserved exactly
and reports every parent manifest entry `OK`; `manifest.stderr` is empty.

Lightweight local custody checks are:

```sh
cmp \
  cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/replay.json \
  cases/max12_912_order3_nu_q8_global_quotient_aws_custody_20260825/aws/frozen_replay.stdout
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_global_quotient_aws_custody_20260825/MANIFEST.sha256
```

