# Symbolic K00 quadratic-normal replay V6

Date: 2026-08-27

Status: **EXACT SOURCE REPLAY PASS; LOCAL SIMPLIFICATION ONLY.**

The preregistered exact-rational AWS replay reconstructed the unloaded part
of all seven frozen ordinary tails after the K00 transverse substitution,
with `C6` retained as an indeterminate.  Every constant and linear-normal
coefficient is zero.  For the exact quadratic-normal pieces it verified

```text
Q5 = -(3*C6^2/128)*Q1-(C6/8)*Q3,
Q6 = 0,
Q7 = -(C6^3/512)*Q1-(C6^2/128)*Q3.
```

```text
lane=max12_812_order2_u2_62_k00_normal_quadratic_v6_q_20260827T083026Z_box01
engine_rc=0
validator=PASS_REPLAY_ONLY
elapsed=0:00.04
max_rss_kib=18608
swaps=0
quadratic_term_counts=8,11,9,12,8,0,6
quadratic_rows_sha256=d74f19a1f083274f49c61cb112c855fb9889d92dc7f61cff1e03906f8e93d62c
```

Therefore rows 5--7 provide no new pure quadratic-normal equation modulo
odd rows 1 and 3 at K00.  A smaller next compiler may omit those redundant
quadratics and begin at the first higher normal/`Lambda` coefficient.

This does not show that any higher coefficient vanishes, does not decide
the K00 closure incidence, does not construct a strict arc or Taylor
realization, and has no JC2 consequence.
