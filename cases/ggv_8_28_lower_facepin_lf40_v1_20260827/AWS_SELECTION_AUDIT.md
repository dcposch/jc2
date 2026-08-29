# LF40 AWS selection audit

At `2026-08-27T18:47:34Z`, AWS reported instance
`i-0f089e64c378f5da3` as running at `34.204.74.226`, type `r6i.16xlarge`,
availability zone `us-east-1a`.  The SSH audit at
`2026-08-27T18:47:45Z` identified hostname `ip-172-30-0-106`, Linux
6.17.0-1019-aws, and DMI vendor `Amazon EC2`.

The audited node had 532,329,025,536 bytes total RAM and 527,184,838,656 bytes
available, no configured swap, 190 GiB free on the 193 GiB root filesystem,
and Singular 4.3.2 at `/usr/bin/Singular`.  `pgrep` showed no Singular,
msolve, or Python campaign process; the only listed shell was the audit
command itself.  The newest pre-existing job directory was timestamped
`2026-08-27T13:45:48Z`.  Those historical output directories are retained
unchanged.

`r6a` was deliberately not selected: the parallel K00 lane owner reserved it
for the requested BASE3 R2 replay.  LF40 therefore registers a unique new tag
on idle `r6b`, after verifying that both its source and output target paths are
absent.

