# AWS launch metadata

Preregistered 2026-08-26T09:04:01Z.  The immediate live audit found zero
swap on both hosts.  Box03 had 481 GiB available at load 14.11; r6d had
348 GiB available at load 13.26.  Existing lanes remain independently
capped.  These four identity clients are capped at 16 GiB each.

| field | host | tag | configuration | cap / compiler / engine | state |
|---|---|---|---|---|---|
| `Q` | Box03 | `max12_812_order2_square_third_sharp_generic_q_20260826T090401Z_box03` | `generic` | 16 GiB / 600 s / 3600 s | preregistered |
| `Q` | Box03 | `max12_812_order2_square_third_sharp_p0moving_q_20260826T090401Z_box03` | `p0moving` | 16 GiB / 600 s / 3600 s | preregistered |
| `F_65521` | r6d | `max12_812_order2_square_third_sharp_generic_p65521_20260826T090401Z_r6d` | `generic` | 16 GiB / 600 s / 3600 s | preregistered |
| `F_65521` | r6d | `max12_812_order2_square_third_sharp_p0moving_p65521_20260826T090401Z_r6d` | `p0moving` | 16 GiB / 600 s / 3600 s | preregistered |

Source freeze SHA is
`f6999a1f9ef2a07bcb921fbf8482b5b00d8daeceb7a41c6a9fca2030203cabe4`.
Every source mismatch, timeout, nonzero exit, missing unique sentinel, or
Singular diagnostic is no verdict.
