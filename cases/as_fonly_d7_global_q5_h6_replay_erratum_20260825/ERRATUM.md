# Global Q5/H6 replay V1 source omission and V2 repair

The frozen V1 replay
`cases/as_fonly_d7_global_q5_h6_20260825/replay_global_q5_h6.py`
replaced the parent source block beginning at the first `S_H7,J7` carry and
ending immediately before the result dictionary.  That interval also
contained the parent definitions of the integer polynomials `P` and `Q`.
The replacement subsequently referenced `P,Q` when constructing
`P5=P+81H6`, `Q5=Q+81J6`, so every attempted replay stopped fail-closed with

```text
NameError: name 'P' is not defined.
```

This is a replay-source omission.  It does not change the separately frozen
formula compiler, emitted SMT, pointwise 69-by-14 certificates, or any solver
endpoint.  It does mean that no SAT endpoint may be consumed through V1.

V2 pins the exact V1 bytes and inserts the omitted, already frozen parent
definitions

```text
P = (x-x^3) + 3U + 9C + 27W + 81H7,
Q = y       + 3V + 9D + 27Z + 81J7
```

immediately before `P5,Q5`.  All remaining V1 source transformations and
assertions are unchanged.  The two known-model omission controls must pass
V2 on AWS before any global SAT model is consumed.
