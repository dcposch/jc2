# Registration: independent generic-square high-contact A-prolongation row certificate

Date: 2026-08-26

This owner-v2 lane is an independent coefficientwise row-identity control
for the root-owned A-prolongation producer.  Its scope is the
correction-aware high-contact cone on `D(p*k0)` after the
reviewed square half-weight ray,

```text
Lambda=sigma^2,
M=sigma^3*(A0+sigma*A1+...),
R=sigma^2*(B0+sigma*B1+...),
C=sigma^4*(E0+sigma*E1+...).
```

The client reconstructs all seven frozen loaded source rows, extracts exact
sigma grades fourteen and fifteen, and checks both grades coefficientwise
against their Laurent receivers through the lower-unitriangular transform
from `w^2=z^2+p/2`.  It also checks the characteristic-zero hand separator
that the grade-fifteen cleared numerator is `-A0^3` modulo `L=z^2+p/2`.

Run exact `Q` on Box03 and an independent `F_65521` control on r6d.  Each
lane uses `ops/aws_exact_lane.sh`, a 16 GiB virtual-memory cap, a 10-minute
compiler cap, and a one-hour engine cap.  Each records tag, host, remote job
directory, PID, UTC start, engine version, input hash, stdout/stderr,
resource report, exit code, and fail-closed validation.

Required endpoint:

```text
SQUARE_APROLONG_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE
```

This is one high-contact cone, not normalized-fan exhaustiveness.  It does
not cover smaller valuations of `R` or `C`, `p=0`, the terminal/Taylor
receivers, the entire square branch, or all order two.
