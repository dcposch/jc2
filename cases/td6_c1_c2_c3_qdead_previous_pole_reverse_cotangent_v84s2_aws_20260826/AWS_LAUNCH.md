# V84S2 dual-AWS launch

Source archive SHA-256:
`822a646fc0ce8d1a847f6cffe34989bd572faaae481f2b7629a2481de8092950`.
Source closure manifest SHA-256:
`ace59b2832f9c1b6c6bc01a033ac6f6538554774931c3fd2cce357dc93b8bf87`.

- Box03 tag: `td6_v84s2_reverse_box03_20260826T071503Z`
- Box03 run: `/home/ubuntu/runs/td6_v84s2_reverse_box03_20260826T071503Z`
- Box03 wrapper PID: `177220`
- r6d tag: `td6_v84s2_reverse_r6d_20260826T071503Z`
- r6d run: `/home/ubuntu/runs/td6_v84s2_reverse_r6d_20260826T071503Z`
- r6d wrapper PID: `243440`

Both lanes passed the matched reverse-row/max-pivot/ascending-parameterization
toy controls and entered the exact source replay.  Each is capped at 8 GiB
virtual memory with a six-hour timeout.  No result is interpreted until both
terminate successfully and their exact tables agree.
