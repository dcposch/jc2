# AWS launch metadata: generic-square high-contact `A` prolongation

Date: 2026-08-26

The corrected source archive shipped to both hosts was
`/tmp/jc2_square_aprol_source_v2_20260826T075500Z.tar.gz`, SHA-256
`05f044c74c05c45855e2a1b16e553a1e4cb241942e3973aa233d5905367da343`.
Each lane verified the complete preregistered `FREEZE.sha256` before
compilation.  The archive name is transport metadata; the recorded
`start_utc` fields below are authoritative.

| role | host | public IP | remote job | field | tag / PID | caps |
|---|---|---|---|---|---|---|
| exact producer | Box03 / `ip-172-30-0-249` | `98.80.65.144` | `/home/ubuntu/jobs/max12_812_order2_square_aprol_v2_q_20260826T075600Z_box03` | `Q` | `max12_812_order2_square_aprol_v2_q_20260826T075600Z_box03` / `182232` | 32 GiB VM; 600 s compile; 7200 s engine |
| software control | r6d / `ip-172-30-0-45` | `100.26.198.153` | `/home/ubuntu/jobs/max12_812_order2_square_aprol_v2_p65521_20260826T075600Z_r6d` | `F_65521` | `max12_812_order2_square_aprol_v2_p65521_20260826T075600Z_r6d` / `247689` | 32 GiB VM; 600 s compile; 7200 s engine |

Both corrected lanes started at `2026-08-26T07:54:20Z`.  Box03 ended at
`07:54:31Z`; r6d ended at `07:54:26Z`.  Both recorded Singular return code
zero, a passing fail-closed validator, and zero swap.

## Quarantined first attempt

The immediately preceding source had two defects: its grade-fourteen
control substituted `e_i=-(5*k0/24)*a_i`, missing the factor two caused by
`C=(e1*z+e0)/2`, and it attempted the unsupported Singular syntax
`quit(81)`.  Both validators correctly rejected it because
`SQUARE_APROL_GRADE14_CANCELLATION=1` was absent.  Its later printed radical
and endpoint are not accepted evidence.

| host | remote job | field | tag / PID | validator |
|---|---|---|---|---|
| Box03 | `/home/ubuntu/jobs/max12_812_order2_square_aprol_q_20260826T074700Z_box03` | `Q` | `max12_812_order2_square_aprol_q_20260826T074700Z_box03` / `181833` | `FAIL_MISSING_OR_NONUNIQUE:SQUARE_APROL_GRADE14_CANCELLATION=1` |
| r6d | `/home/ubuntu/jobs/max12_812_order2_square_aprol_p65521_20260826T074700Z_r6d` | `F_65521` | `max12_812_order2_square_aprol_p65521_20260826T074700Z_r6d` / `247410` | same rejection |

The two complete failed streams are retained under `quarantine_v1_*` only
as negative custody.  They are not used in the result.
