# AWS launch metadata

Preregistered 2026-08-26T08:29:00Z after live host audit.  Both hosts had
zero swap; Box03 had 487 GiB available at load 6.33 and r6d had 355 GiB
available at load 6.38.  The r6d host retained an unrelated capped Singular
lane; this client is independently capped at 32 GiB.

| field | host | tag | remote job directory | cap / compiler / engine | state |
|---|---|---|---|---|---|
| `Q` | Box03 | `max12_812_order2_square_lowcontact_c1c2_q_20260826T082900Z_box03` | `/home/ubuntu/jobs/max12_812_order2_square_lowcontact_c1c2_q_20260826T082900Z_box03` | 32 GiB / 600 s / 7200 s | launched, PID `186429` |
| `F_65521` | r6d | `max12_812_order2_square_lowcontact_c1c2_p65521_20260826T082900Z_r6d` | `/home/ubuntu/jobs/max12_812_order2_square_lowcontact_c1c2_p65521_20260826T082900Z_r6d` | 32 GiB / 600 s / 7200 s | launched, PID `251709` |

The source freeze is `a35b0784e083db86b1f658620acfa650839a3318e67b7c1b372ca69398048567`.
Every nonzero exit, timeout, missing unique sentinel, Singular diagnostic, or
source-hash mismatch is no verdict.
