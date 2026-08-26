# AWS registration

- failed pre-compute tag:
  `max12_912_order3_d1_double_root_control2_rees_source_identity_20260826T012542Z_r6d`
- host: r6d, `100.26.198.153` (Amazon EC2)
- job:
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_rees_source_identity_20260826T012542Z_r6d`
- worker PID `199110` was observed blocked behind `WAITING_GO`; after GO it
  failed closed at `SOURCE_HASH_FAILURE` because `PREREGISTRATION.md` had not
  been transferred.  No compiler or Singular process ran.
- live replacement tag:
  `max12_912_order3_d1_double_root_control2_rees_source_identity_20260826T012642Z_r6d`
- replacement job:
  `/home/ubuntu/jobs/max12_912_order3_d1_double_root_control2_rees_source_identity_20260826T012642Z_r6d`
- replacement worker PID: `199408`, observed blocked behind `WAITING_GO`
- compiler cap: 2 GiB virtual, 120 seconds, nice 10
- Singular cap: 4 GiB virtual, 300 seconds, nice 10

No GO sentinel existed in the replacement job when its registration was
written.  Its complete frozen source closure verified before GO.
