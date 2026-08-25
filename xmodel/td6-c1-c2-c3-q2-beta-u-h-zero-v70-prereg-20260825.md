# Preregistration: TD6 q2-beta raw `C=U=0` rebuild (V70)

Timestamp: `2026-08-25T16:28:50Z`.

This run answers only the raw exceptional-stratum debt exposed by the hostile
V33 review: rebuild the fixed normalized A3 q2-beta source after imposing
`C=U=0`, retaining `V` and polynomial `beta`.  It must not specialize the
V33 `U=0,D(C)` echelon.  It must start from the original transport rows,
retain direct `q_beta'=1+2 beta t+25 t^24`, and replay every incompatibility
against original source rows.

The byte-pinned producer archive is the V69 canonical-serializer source
archive, SHA-256
`9e89808cca9d24ec5182466b40e53d612317a4f03c70053a9c490e957ab51f38`;
its outer source manifest has SHA-256
`fe39baefa6bcec511646397b5060ee8a4d555d17c2310b40b0035ff5931900ac`.
The executed command on each AWS host will be

```sh
PYTHONHASHSEED=0 /usr/bin/time -v timeout --signal=TERM --kill-after=120s 8h \
  /home/ubuntu/venvs/td6/bin/python \
  jc2/cases/td6_c1_c2_c3_q2_n13_raw_canonical_v69_20260825/replay.py \
  --stratum=u-h-zero
```

Two independent AWS executions from the same archive are required.  Each
run is capped at 12 GiB.  Promotion requires rc zero, byte-identical canonical
mathematical stdout or an exact adjudication of any difference, exact source
manifest checks, original-row ancestry, all transport/stage denominator
factors, and an omission/wrong-source control.  If the certificate remains
localized at `V`, the raw origin `C=V=U=0` remains a separate mandatory leaf;
no whole-`U=0` or whole-`H=0` composition is licensed before that leaf closes.

The reviewed surviving input theorem is only `U=0,D(C)` in the fixed A3
q2-beta section.  No outcome here may imply whole A3, another TD6 modulus,
TD6, SP-2, landing, or JC2.
