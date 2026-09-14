# Nine idle fleet workers terminated; persistent data retained

Completed 2026-09-10 13:44:13 UTC under DC's explicit retirement instruction.
The nine exact instance/volume pairs are in PLAN.md. AWS independently reports
all nine instances TERMINATED, all nine retained 100 GiB EBS volumes AVAILABLE
with no attachments, and no nonterminal instance carrying jc2fleet=1.
The coordinator and separately owned formalization infrastructure were not
part of these queries or operations. Model research/review lanes were not
stopped. No campaign scientific computation was running on these workers.

Five running workers were checked by current EC2 DMI identity, boot ID,
non-kernel process inventory, mounts/block devices, and system/user timers at
13:40:22 UTC. Their inventories showed service daemons and the inspection
session only; no scientific jobs or campaign timers. The other four workers
were already stopped. Original process outputs are retained beside this file.

All nine root mappings initially had DeleteOnTermination=true. Each was set
false and independently re-read with its exact instance/volume binding before
the explicit nine-ID termination call. No term-all or volume-delete call was
used. This preserves sole-source vol-0eb6450d18ffa89f1 independently of its
now-retired instance; the prior instance-retention hold is superseded by DC's
new instruction, but the data-preservation obligation remains.

The x2idn worker i-025410e620b1d65c9 also held instance-store RAID /dev/md0 at
/home/ubuntu/t2t3-full: 780825513 apparent bytes, 726 files, 59 directories,
8 symlinks. Before termination, all 793 entries were archived with numeric
ownership, sparse-file support, ACLs and xattrs onto its EBS root volume.
GNU tar --compare succeeded against the entire source; the archive was made
root-owned0444 and synced before the AWS termination call.

Recovery location on retained vol-0be96430c433dfbe2:

    /var/lib/jc2-retired-instance-store-20260910T1340/instance-store.tar

Archive: 782284800 bytes; SHA-256
4c20fb5e99e605dfb3df1facd6cfa987d7e75feb521241e3231bcf8374400625.
Copy/compare/sync completed13:41:55.481155375. The original ephemeral storage
is lost with termination, but its archived data is recoverable from this EBS
volume. No archive extraction or mathematical payload inspection was needed.

Evidence pins:

- pretermination-aws.json: 401057e58d3cfa1b31a6fca22a3f8de9d63659277746ae846003d10e738cf6f6
- instance-store-copy.txt: 75b8521ed13322286c470b4e75f3d95eef4fe4b3641b47a6608532d7554c6b5b
- terminate-response.json: 7a0dea098e54dbbd1928b1740a93c87476431103001c3633b48ef8bf1209953e
- final-instances.json: 9f55dfcbeac4a7a3f223254066a930bf0a86bac962408c496491cdd1f5c22e3a
- retained-volumes.json: 22c6a0b30ae86ce0b594f21067034cdac963b3668a8f7b3765fce99ab50a9868
- remaining-fleet.json: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570

No idle instances are retained for possible future work. Any next scientific
batch needs a newly allocated worker and a fresh physical/native registration;
none may attempt to restart one of these retired instance IDs. Retained disks
remain recoverable storage, not active compute or a new scientific result.
