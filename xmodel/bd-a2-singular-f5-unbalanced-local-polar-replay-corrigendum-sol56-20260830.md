# Corrigendum: optimization-safe replay for the unbalanced singular-F5 polar table

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra sublane `/root/u_rows_full_family`  
Frozen basis: `2ad7ee8c773fb987200ad2abaa39cf6353f92fc1`  
Lifecycle: **REPLAY-EVIDENCE CORRIGENDUM / NO MATHEMATICAL CLAIM CHANGE**

## 0. Exact correction

This packet corrects only the optimized-mode replay claim in Section 6 of

```text
xmodel/bd-a2-singular-f5-unbalanced-local-polar-sol56-20260830.md
full SHA-256 6a7dc7bec108d867fe9215a85fdc09c2d2790db73d36c4123e96f7419f9511f3
body SHA-256 590d3ae673f01711627a5adddec9ce174e345617b7aba5402c82db05487ecc53
```

The original replay

```text
ops/f5_unbalanced_polar_replay.py
SHA-256 ee488fbb19c243815f85254d8c2d3a06ba77991b1cf8e92d70e57b4b0317ac82
```

implemented every check with Python `assert`.  Its ordinary run genuinely
checked the arithmetic, but `python3 -O` and `python3 -OO` removed those
checks.  The original report's statement that optimized runs "pass
identically" was therefore vacuous as evidence in those two modes.  The
sealed original is intentionally unchanged.

No analytic calculation, branch partition, exceptional vector, or theorem
statement is corrected.  This is an evidence-engine defect only.

## 1. Optimization-safe v2 replay

The replacement is

```text
ops/f5_unbalanced_polar_replay_v2.py
SHA-256 034414413db07d8a39c2b36b26eb3eb5ce0f0fe4e865cacf16d0671a0b13cfed
```

Every invariant now calls an explicit `require` function that raises
`ReplayFailure`; no verification has semantic dependence on `assert`,
`__debug__`, or a docstring.  The v2 replay checks:

1. `C_A3(2,2,1)=(2,1,0)`;
2. `C_D5(2,4,5,3,3)=(0,1,0,1,1)`;
3. `C_D6(2,4,5,6,3,3)=(0,1,0,1,0,0)`;
4. the nonzero `U3` cusp and smooth-branch controls over an exact rational
   sign grid;
5. the separated `D5` roots, nonzero cubic lift, and nonzero `delta^2`;
6. the forced nonzero `D6` coefficient when `delta=0`;
7. both named D cells occur and every partition sums to eight.

The positive commands all exit zero and print the same three rows:

```text
python3 ops/f5_unbalanced_polar_replay_v2.py
python3 -O ops/f5_unbalanced_polar_replay_v2.py
python3 -OO ops/f5_unbalanced_polar_replay_v2.py

U3/A3: partition=4+4 m=(2, 2, 1) n=(2, 1, 0)
U5/D5: partition=2+3+3 m=(2, 4, 5, 3, 3) n=(0, 1, 0, 1, 1)
U6/D6: partition=3+5 m=(2, 4, 5, 6, 3, 3) n=(0, 1, 0, 1, 0, 0)
```

## 2. Deliberate-mutation negative control

The option `--deliberate-mutation` replaces the correct D5 contact vector by
the wrong vector `(1,0,0,0,2)` while retaining the certified exceptional
coefficient vector.  The explicit Cartan check must then raise
`ReplayFailure("D5 Cartan/contact mismatch")`.

Each of the following commands was run independently and exited nonzero:

```text
python3 ops/f5_unbalanced_polar_replay_v2.py --deliberate-mutation
python3 -O ops/f5_unbalanced_polar_replay_v2.py --deliberate-mutation
python3 -OO ops/f5_unbalanced_polar_replay_v2.py --deliberate-mutation
```

Thus both successful evidence and rejection of a deliberate corruption are
live in ordinary, optimized, and double-optimized modes.

## 3. Binding scope

Replace only Section 6's references to the old replay and its optimized-mode
evidence with Sections 1--2 above.  The old script remains immutable as
historical evidence for its ordinary run, but is superseded by v2 for all
future replay citations.

This corrigendum neither strengthens nor weakens the local theorem.  The
replay remains arithmetic corroboration, not evidence for analytic or global
realization, a finite first-leg algebra, a polynomial map, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3626`.
- Body SHA-256:
  `3284a77e0a10434d5816053558fcdd7786d2fd7ae034173b58c10a801409029a`.
- Frozen basis: `2ad7ee8c773fb987200ad2abaa39cf6353f92fc1`.
