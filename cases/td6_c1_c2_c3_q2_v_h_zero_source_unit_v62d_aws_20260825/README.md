# TD6 fixed-A3 q2 `V=H=0` source-unit certificate (V62D)

Status: **producer-exact original-row unit certificate on
`V=H=0,D(U)`; independently duplicated on Box02 and r6d.**

The fixed source-typed center is `(c1,c2,c3)=(C,V,U)`,

```text
H = C - 3 U^2,
q_beta(t) = t + beta t^2 + t^25.
```

After exact transport, the first stage has rank `38/132`.  The
previous/pole stage has rank `37/94`; its two nonzero dependencies are
`('X-1',11)` and `('X-1',13)`.  V62D combines their exact Bezout weights,
returns to their raw previous equations, divides the combined raw polynomial
once by the original first pivots, and obtains the exact remainder `1`.
Replaying the resulting 13 first-row and 12 previous-row multipliers against
the arbitrary-degree original rows reproduces `1` exactly.

This representation does not use the current stage, N13, or P12.  Removing
one used first-row edge or one used previous-row edge destroys the unit
identity.  Both the source-coefficient denominator ledger and the complete
first/previous pivot-coefficient ledger have radical support exactly `{U}`.
Consequently the certified scope is the raw rational edge
`V=H=0,D(U)` for arbitrary `beta`.  The `U=0` edge remains a separate direct
source theorem and is not composed here.

No whole-H, whole-fixed-A3, TD6, SP-2, landing, or JC2 conclusion is made.

## Exact AWS custody

The same source archive was replayed independently under 12 GiB caps.

### Box02 (`34.203.207.55`)

- path: `/home/ubuntu/runs/td6_v62d_v_h_zero_box02_20260825T1400Z`;
- UTC: `2026-08-25T13:54:31Z`--`2026-08-25T14:17:23Z`;
- exit code: `0`;
- maximum RSS: `556892` KiB;
- stdout SHA256:
  `50a143c637b0344b2ea8dc7d4f67ae85c4afe497b6d3fecb59a1d94665980a76`.

### r6d (`100.26.198.153`)

- path: `/home/ubuntu/runs/td6_v62d_v_h_zero_r6d_20260825T141255Z`;
- UTC: `2026-08-25T14:13:25Z`--`2026-08-25T14:30:00Z`;
- exit code: `0`;
- maximum RSS: `555196` KiB;
- stdout SHA256:
  `db4e566e4dfb51d6bffe66fc271fb3e19d9b7b4c5c5b1d7657d1789a305dd1bf`.

The stdout files differ only in the three absolute artifact-path markers.
Their exact proof artifacts agree byte-for-byte:

- original-row unit certificate:
  `6d672e839c84b518909ea70161761f929d249fa4251fa5852bde9f896c1572a1`;
- source denominator ledger:
  `02d29ba2f0112a5f2d83b1973d86e4350ae04203df1496a9f598c599c8d8426a`;
- pivot denominator ledger:
  `bacdf7a6869cb50f118c4a77fa646815963f9782be5bf0f387dc676361f8b034`.

The portable archive SHA256 is
`6d568ff6e77dc764c2ddae6b5be1c6b8baa75e47e364ac15f83d6e4aaaa52e42`.
Its complete 111-entry `SOURCE.sha256` has SHA256
`bed1c3b9b705189702cdc9177340955ddafb813ecd8449032960da5da959e91e`;
Box02's frozen `source-check.txt` verifies all 111 entries.

Run the lightweight custody, duplicate-agreement, marker, and scope check:

```bash
python3 verify.py
```

