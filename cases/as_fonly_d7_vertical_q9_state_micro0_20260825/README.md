# AWS-only Q9 shard-zero accelerator

Run on the same host as the active macro partition, passing its exact result
directory:

```sh
nohup setsid ./launch_micro0.sh UNIQUE_TAG /exact/macro/result/dir > launch.log 2>&1 < /dev/null &
```

The 81 microshards each have one CPU, an 8 GiB VM cap, and a 12-hour
timeout.  They rerun only structural bases `0..80`; the canonical 27-way
job remains active for an exact count/histogram consistency check.
