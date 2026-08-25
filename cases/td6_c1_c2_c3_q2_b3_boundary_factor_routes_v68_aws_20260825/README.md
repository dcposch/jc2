# TD6 fixed-A3 q2 B3 chart-boundary route certificate (V68)

Status: **producer-exact routing of the V66 factors `t=0`, `w=0`, and
`t=2` into three already frozen direct-source strata; hostile review
pending.**

On `D(U0)`, use the normalized coordinates

```text
x = C0/U0^2,  y = V0^2/U0^3,  w = V0/U0,
t = y/(x+5),
b(x,y) = 4x^2-4xy+24x+y^2-20y+20.
```

V68 proves the exact line-pencil factorization

```text
b(x,t(x+5)) = (x+5)((t-2)^2 x + 5t^2-20t+4).
```

Consequently:

- `t=0` gives `4(x+1)(x+5)=0`;
- `w=0` on `D(U0)` gives `V0=0`;
- `t=2` gives `-16(x+5)=0` and hence the `x=-5,y=0` branch.

The raw-center identity

```text
B3|_(V0=0) = 4 U0^2 (C0+U0^2)(C0+5U0^2)
```

then routes all three chart-boundary factors into

```text
U0=0,
V0=0, C0=-U0^2,
V0=0, C0=-5U0^2.
```

The archive hash-pins the frozen direct-source certificates for all three
targets.  Their exact markers include original-row replay, a degree-zero
compatibility gcd and denominator one on `U0=0`; an original-row unit
compatibility certificate on `C0=-U0^2`; and genuine-P12/staged-N13 residual
`-k/50` on `C0=-5U0^2`.  The two rational-line certificates include direct
q-prime and P12-without-N13 negative controls.  V68 additionally checks
wrong-coefficient, missing-branch, and source-marker omissions.

This package proves a route lemma and verifies its source dependencies; it
does not replace their producer/review status.  It does not cover the finite
factors `2t-1` or `t^2-4t+2`, and does not itself prove a whole-B3, whole-A3,
TD6, SP-2, landing, or JC2 statement.

## AWS custody

The same source archive ran on Box02 and r6d with 1 GiB/120-second caps.
Both executions returned rc 0 and byte-identical stdout SHA
`c84447f961863fcd0c80a82ed3ec28d0e6efcfe0f89fa7de4f9bc1d5c90ffdce`.

- archive SHA: `876751020cb4f4465b0314a3bd2d79c2a6afee5008feda17290a946e94f6126a`;
- source manifest SHA: `c41520929a4edfb9923973890f3b8977fbb3d63a7671ae20fecbc489dc6b66a2`;
- route producer SHA: `4b528bad9e8d13994343d7ab747a855c41e93f3a975d35c993fac6f8bc8b061c`.

Run `python3 verify.py` for a lightweight custody/member/scope check.
