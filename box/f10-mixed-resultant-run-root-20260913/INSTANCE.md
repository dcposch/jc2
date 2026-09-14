# Bound instance — one mixed-resultant observation

ROOT allocated i-0a749d64ef2ef62c1 at2026-09-13T07:55:20Z, r7i.xlarge,
private172.30.0.245/public54.89.148.20, personal/us-east-1. Root EBS
vol-01631036b2d7929fe is100GiB gp3 with DeleteOnTermination=false observed
by direct API. Exact instance RUNNING after allocation. No IAM profile.

HQ user-manager timer jc2-retire-mixres20260913a.timer armed within60seconds,
ActiveState=active, NextElapseUSecRealtime=September13 08:24:00UTC.
Service ExecStart is /usr/local/bin/aws --profile personal --region us-east-1
ec2 terminate-instances --instance-ids i-0a749d64ef2ef62c1. No wildcard target.
Original latest admission08:06/retirement08:24 unchanged. ROOT collector.

Frozen registration88b20be63c264e684ee5818fd87fa93f2e586fdac4f7bde23270cd00b04ea10d;
preflight21e2bb41e332af8fc24394f5c17cc5278b035dc4eb6af6970a4804fa92c57882.
The final preflight excludes its own separately pinned main script from the
system-library inventory; no other source change. No local syntax/import/test.
Binding this job.json does not mutate the disabled producer template.
Actual host-key, worker qualification, job outcome and retirement evidence are
recorded as observed, not inferred from this registration.
