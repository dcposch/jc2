# Fixed-A deep-q1 full-tail preregistration

Date: 2026-08-28

This packet preregisters two literal fixed slices and one strictly smaller
reviewed subbranch before any uncertain computation.  The fixed polynomial is
`A=X^4-1`; the two full slices are separately `lambda=0` and `lambda=1`, with
`R0=lambda*A`, `S=3*lambda*A'`, `V0=A*S`, and the reviewed D9 consequence
`T=A*U`.  No equivalence between nonzero lambda values is claimed.  In
particular, the tempting constant translation/shear is not a raw-window gauge:
it creates forbidden `F9[X^0]` and `G13[X^0]` slots.

## Charged full raw systems

The direct compiler retains `c2`, every legal raw `F4,...,F14` and
`G4,...,G21` coefficient, and the complete raw representation of all later
characteristic modes.  It imposes

```text
D0=...=D21=0, D22=1, D23=...=D35=0.
```

There is no `G22` slot.  The compiler expands the authoritative recurrence

```text
D_n=sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j').
```

The q1 restriction is therefore consumed with its actual D23 tail license,
not inferred from D0,...,D22.  The supported terminal row is compiled
literally; any D35 cancellation must replay from the frozen coefficients.

## Exact de Rham screen

The smaller compiler independently constructs

```text
q_n = 2/(n+2) [t^n] F^((n+2)/8),  1 <= n <= 13,
```

and compiles exactness on both quadratic components of `p^4=A^2`.  Writing a
coefficient as `p^r*N/A^k`, its rational primitive is represented by the
complete bounded polynomial ansatz for

```text
A P' + (r/2-d) A' P,
```

where `d` is the primitive denominator exponent.  The two twists differ by a
nonzero whole-character scalar and give the same coefficient ideal.  All even
gates remain in the compiled system as guards; only an exact replay may remove
them as automatically exact.

For each full lambda slice this q-system is a necessary screen.  `1` in its
exact-Q ideal is an emptiness certificate for the fixed slice, but a proper
q-ideal is not a raw endpoint survivor until intersected with the direct raw
system.

The third system is labelled
`lambda_0_c2_nonzero_exact_D0_reduced_qgates`.  It consumes only the reviewed
proper subbranch `c2!=0`, exact defect `D=0`, the D11/D12 lifts, and q3 after
`A|U`, giving `U=0`.  Its frozen forms are

```text
F1=F3=0,
F2=-A^3 Q/8,
F4=A^2 Q^2/256,
F5=A^2 r/256,
F6=A e1/2048,
F7=A f.
```

Here `deg Q<=2`, `deg r<=3`, `deg e1<=6`, and `deg f<=5`; `F8,...,F13`
retain their authoritative raw windows.  A unit certificate here kills only
this proper subbranch, never the full lambda=0 slice.

## Desk validation frozen before launch

The all-row recurrence independently reproduced the low formulas

```text
G1 = 3 A^5 S/2,
G2 = 3 A^4 S^2/4 + 3 A^4 Z/8 + c2 A^5,
G3 = A^3 S^3/8 + 3 A^3 S Z/8 + 3 A^4 U/16
     + 5 c2 A^4 S/4.
```

The de Rham compiler independently reproduced `q1`, `q2`, and `q3`; on
lambda=0 these are `0`, `Z/16`, and `p U/32`.  Before consuming the proposed
hand anchors it independently expanded the reduced recurrence and then matched

```text
q5 = p^3 r/1024,
q7 = p^3 (f/4 - Qr/65536),
q9 = p^3 (F9/4 - 3Qf/256 - 3Q^2r/8388608),
q8 = A (F8/4 - Qe1/2^18 - Q^4/2^23).
```

The local standard-library desk commands completed in under one second.
Their stdout hashes are:

```text
dd3bb2b1e975f527ceb57b46a6f493745fd800798c8dbc8afd06c93d6fcc86dc  q-gate desk stdout
62c975599324e854213509e23f2adc4935b375645bb17f59c3c9b1a27812e3cd  raw desk stdout
```

## Frozen executable sources

```text
82284effbd507693cb8deb00e33b108d0f62d3d3861ce487e75d2e3f98b8fbea  compile_fixed_q1_raw.py
b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201  compile_q_gates.py
47d644bf803dfc2c3e65b57110aca8e4ae32a878794b9def6787adf21f4128b6  reduce_q_gates.py
```

Pinned mathematical/code dependencies are recorded in `SOURCE.sha256` and are
rechecked inside the compilers.  The scope ledger was observed at
`b40b355237ab563f7618be43f584ccbe9ef07e8bebc13253544eb1048dc503c9`
for `APPROACHES.md`; it is provenance, not mutable runtime input.

## AWS execution and classification

Use audited idle Amazon EC2 only, in a fresh job directory and process group.
Initial CPU affinity is one core; swap must be exactly zero before and
throughout.  Record DMI, instance identity, load, memory/disk gates, immutable
source hashes, PID/PGID/SID/starttime, a process-group registry, stdout,
stderr, `/usr/bin/time -v`, and terminal markers.  Apply explicit inner and
outer timeouts and verify zero remaining group members at exit.

Order:

1. replay source hashes and both desk checks;
2. compile the three q-gate systems and the two literal full raw systems;
3. run exact sequential affine reduction with exact-Q and primes
   `65521,65519,65497`; abort on rank disagreement;
4. run bounded modular Groebner discriminators on the reduced q ideals;
5. run tracked exact-Q Groebner only for a promising modular unit or a small
   reduced ideal; a unit verdict requires an internally replayed exact-Q
   cofactor certificate;
6. use the 300-variable raw Groebner only if the exact q screens do not decide
   and the compiled direct tail is demonstrably within the registered cap.

Verdicts:

- `EXACT-Q-UNIT`: field-empty at exactly the system's recorded scope, only
  after coefficient replay;
- `EXACT-SURVIVOR`: an explicit assignment must replay every charged equation;
- `MODULAR-UNIT/NONUNIT`: discriminator only;
- timeout/resource cap: `NO-VERDICT`;
- source drift, nonzero swap, host/job conflict, rank disagreement, formula
  mismatch, or reducer replay disagreement: stop without mathematical verdict.

No HENS namespace, `jc2-lean`, top-level canonical file, family landing,
Keller theorem, or JC2 conclusion is in scope.
