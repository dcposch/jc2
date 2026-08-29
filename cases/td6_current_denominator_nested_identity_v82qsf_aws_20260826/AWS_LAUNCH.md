# V82QSF dual-AWS launch

- source archive SHA-256:
  `ef0c0969e5fd1a8260ed8c1ed1f652fa958eb9c47e6e1317a0ef0d5d4191a2a0`
- Box03 run:
  `/home/ubuntu/runs/td6_v82qsf_nested_box03_20260826T083035Z`, PID `186724`
- r6d run:
  `/home/ubuntu/runs/td6_v82qsf_nested_r6d_20260826T083035Z`, PID `251961`
- caps: 1 GiB and 600 seconds per host

Both Amazon EC2 lanes passed `rc=0`.  Their stdout streams differ only in the
registered run tag; after removing that one provenance line the common SHA-256
is `d5f931fbe55a645bcffe43670ba615755380558b96f00b387802fd55fc21623f`.
Peak RSS was 30,440 KiB on Box03 and 29,520 KiB on r6d.
