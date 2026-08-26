# Loaded order-four lemniscatic target V2: fail-closed record

Date: 2026-08-26

Status: **NO VERDICT.  V2 is an immutable failed control.**

The registered Box03 lane
`max12_812_order4_lemniscatic_param_v2_20260826T023000Z_box03` completed all
direct polynomial checks and printed its final PASS token.  Immediately
afterward Singular 4.3.2 diagnosed the terminal statement `exit(0)` as
undefined.  The shell return code was nevertheless zero.  Because the
registration rejects any engine error, the lane is not promoted.

The exact arithmetic preceding that terminal typo is useful only as a
control.  Retrieved outputs are frozen under `aws_v2_failed/`; principal
hashes are:

```text
stdout  ddfdf831edb378f5bdcabffd2a65aa688d3a7897aebf7326ae58f1541099904d
stderr  e4ad89b40bd5892c65275319e681285c05a20281eacc58180dd1db0b3dc44f7b
meta    172892a61afee6e18f31ad8b966a352659b7a85745c8da0d5a9830d34ca04cb7
archive 6de1f9ce33ba2f12cc5ae695e30a3cba398c0708e789704525b4f7a8bb7927c4
```

V3 has exactly two terminal-line deltas: its completion-token version is
changed from V2 to V3, and it uses `quit;`.  All arithmetic statements are
byte-identical, including the fail-closed nonzero exits on failed identities.
