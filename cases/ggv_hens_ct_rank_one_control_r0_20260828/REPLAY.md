# Replay map

## Standard-library controls (safe locally)

```sh
python3 replay_rank_one_controls.py
```

Success is `PASS_RANK_ONE_CONTROLS`.  This checks the reviewed closed form and
primitive step-eight recurrence, the `+22` fixed receiver, all index maps, and
the four required wrong-gauge/wrong-sector mutations.  It does **not** claim
an algebraic telescoper.

## Frozen tool-interface failure (AWS evidence environment)

The installed environment used by the terminal run was

```text
/home/ubuntu/jobs/ggv_hens_ct_rank_one_r0_20260828T010100Z_v2/venv
```

On that host, from this directory, replay with

```sh
/home/ubuntu/jobs/ggv_hens_ct_rank_one_r0_20260828T010100Z_v2/venv/bin/python \
  smoke_ore_interface.py
```

The observed terminal exception is

```text
NotImplementedError: polynomials over Multivariate Polynomial Ring in
ss, xx, yy over Integer Ring are not supported in Singular
```

It occurs while materializing the generators of the outer differential Ore
algebra, before construction of the charged algebraic field, composition
annihilator, telescoper, or certificate.

## Full emitter

`run_ore_ct.py` is the frozen intended route.  A successful compatible
backend must emit nonzero `L`, nonzero `C`, and exact Ore membership of
`L-Dxx*C`; that output must then receive an independent direct replay in
`E=Q(s,X)[y]/(y^8-1-s(1+X^-3+X^-7)y)`.  No such output exists in this lane.
