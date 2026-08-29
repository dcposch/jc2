# Local replay termination record

Date: 2026-08-27

The desk-scale construction attempt using producer SHA-256
`3487c75251172eb3215963a04005ff1b7a6c45cfaee441c3c1a4cd95f39f4773`
was terminated deliberately when its sparse exact expansion reached the
campaign's local-memory boundary.

- local PID: `98259`
- elapsed wall time: `108.47 s`
- user/system time: `107.16 s` / `1.23 s`
- maximum RSS reported by `/usr/bin/time -l`: `4,222,730,240` bytes
- swaps: `0`
- output root: `/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/tmp.2NzljvpEKA/out`
- certificate/result files: none
- disposition: no mathematical verdict; relaunch on AWS only

The process received `SIGTERM` before the workstation crossed into swap.
