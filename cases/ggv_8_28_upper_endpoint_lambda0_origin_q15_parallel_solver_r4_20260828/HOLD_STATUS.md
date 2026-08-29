# r4 nearby-order portfolio — hold status

Date: 2026-08-28

Status: `HELD_UNEXECUTED`

The proposed three-job nearby block/order portfolio was stopped before any
remote source staging or solver execution.  Only the already emitted exact
input bytes and their frozen provenance were copied into this local case.

The three campaign instances were briefly resized from `r6i.16xlarge` to
`r6i.4xlarge`, started, and audited read-only.  Each audit found Amazon EC2
Linux, 16 vCPU, approximately 128 GiB available RAM, zero configured swap, no
conflicting process, and Singular 4.3.2 with executable SHA-256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
The parent hold arrived before source packaging or transfer.  At
2026-08-28T12:11:51Z all three instances were stopped:

```text
r6a  i-02cb2b4a379ffcc64  r6i.4xlarge  stopped
r6b  i-0f089e64c378f5da3  r6i.4xlarge  stopped
r6c  i-040b7a1c2ed72d4cc  r6i.4xlarge  stopped
```

No AWS job namespace, command, source archive, or solver byte was staged or
executed.  No mathematical result or marker was produced.  The local `.sing`
files are retained only as immutable inputs for possible later round
synthesis; they must not be run without a new preregistration and explicit
release of this hold.

