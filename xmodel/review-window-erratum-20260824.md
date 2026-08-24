# Erratum — self-reported review windows

Date: 2026-08-24  
Status: **FROZEN METADATA CORRECTION / NO MATHEMATICAL CHANGE**

Three Grok review reports self-reported approximate UTC windows that disagree
with the timestamps written automatically by `ops/lane.sh`.  The runner
timestamps are authoritative.  The review reports and run records remain
byte-frozen; this note corrects only their human-written metadata.

| review | frozen report SHA-256 | frozen run SHA-256 | report says | authoritative runner window |
|---|---|---|---|---|
| `d73-strict-or-equality-review-grok-20260824` | `3c0df2009432646bc6b93fa36f4c688b24af9e8df22629755303e89fde0fac3a` | `da21d939239de2ebba773ed8447b9f8627e41de977d7c0b0197d01f6ebf9eaa5` | `08:35:00--09:15:00Z` | `08:50:00--09:00:40Z` |
| `as109-carry-erratum-review-grok-20260824` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | `9dc8cf6f753bade0fe27ca8c4abfa8085e0b12dd2b23f7b9f3a2d9e8d1f0f57c` | `08:55:54--09:18:00Z` | `08:51:04--08:59:39Z` |
| `dual-pencil-review-grok-20260824` | `57e6d4a14d90abc1411fe9e20d328745084f4123355be728ad54bf112a7ad0f5` | `0dc9c0c7d2ca8d5d541c247bbed07a6706972348a1e9d99def0cfad26695c369` | `08:35:00--09:05:00Z` | `08:54:01--09:02:00Z` |

All three runner records have exit code zero, `final_status=DONE`, and the
report hashes displayed above.  No input hash, computation, source audit,
verdict, or scope statement is affected.
