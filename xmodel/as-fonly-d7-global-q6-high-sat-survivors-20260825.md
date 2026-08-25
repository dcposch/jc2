# AS F-only `D=7`: two global Q6/high filtered-state survivors

**Status: PRODUCER EXACT; TWO DIRECT-REPLAYED SAT WITNESSES;
PROVISIONAL PENDING DIFFERENT-MODEL SOURCE/COMPILER REVIEW.**

This gate globally revisits three structural bases whose first displayed
Q9/Q8/Q7 representatives had stopped at the next source row.  It keeps all
raw predecessor, Q9, Q8, and Q7 digits symbolic, reimposes the final degree-8
source row after Q7 restoration, adjoins the sixteen homogeneous degree-7
digits `(H7,J7)`, imposes all seven Q6 rows, and imposes the sixty-three
divided-carry rows `R12,...,R7`.

The exact row inventory is

```text
predecessor 20; corrected top 5,12,11;
Q9 23; Q8 22; Q7 19; final G8 9; Q6 7; R12..R7 63.
```

## Result

On Box02, pinned Boolector 1.5.118 returned:

| base | endpoint | wall / max RSS | exact evidence |
|---|---|---:|---|
| 303 (`0102020`) | UNSAT, solver evidence only | 8m10s / 1.70 GiB | formula `65153b165ebf41d0c0eab16968ecb1533b7c09f2e32d84e5c79bb403bae3b081`, stdout `f40349218f0606ab0a5c7973a9cc14be26b56faae0e1a54dd5d9c00416671d10`; no proof certificate |
| 513 (`0201000`) | SAT, literal replay PASS | 9m11s / 1.46 GiB | formula `2156231ae243cf9b697f4da62e3bc3be046372809013e211aceb8b2578aae7d2`, model `8b04ed1edf90836afa9f4712bd317e810c8407f9e2edeee6257bf979e3a7c9ab`, replay JSON `afc1b4f08f75e1e8800621f76cf0872f17f0171b3ab519fff05f74ec6edf35df` |
| 519 (`0201020`) | SAT, literal replay PASS | 11m16s / 1.72 GiB | formula `37632719978aee58b0296f9e61f4d601fa5f8316eb8a7158f6e5a7b632ec14db`, model `a71c04ae2118cadca501944a9a007d44470d2c7bfa0126f15ef0306fcaf50660`, replay JSON `3d9380f868c5f5a0dc59a46dbb64fc1c7437e544ec5e5f2ec71e178248487830` |

For each SAT model, an independent replay reconstructs the nested integer
source expressions, checks every displayed row, and checks that recursive and
literal integer division by `243` agree coefficientwise in degrees 12 through
7.  Both replays end with

```text
final G8 = 0;
Q6 = 0;
R12 = R11 = R10 = R9 = R8 = R7 = 0;
PASS-AS-GLOBAL-Q6-HIGH-DIRECT-REPLAY.
```

The complete accepted digits are:

```text
base 513 predecessor =
[0,2,0,1,0,0,0,0,0,2,0,0,1,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,1]
base 513 Q9 =
[2,0,1,0,1,2,2,1,0,1,0,2,0,2,0,1,0,0,0,2,0,1,0,2,0,0,0,1,0,2,0,1]
base 513 Q8 =
[1,0,2,2,0,1,0,2,0,1,1,0,1,2,2,0,0,0,0,0,2,1,2,2,2,0,0,1,2,1,2,1]
base 513 Q7 =
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,2]
base 513 Q6/H7,J7 =
[2,0,1,0,1,0,1,1,1,0,2,1,0,1,2,2]

base 519 predecessor =
[0,2,0,1,0,2,0,0,0,2,0,0,1,0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,1]
base 519 Q9 =
[0,0,1,0,1,2,2,1,0,0,2,2,0,2,1,1,0,0,0,2,1,1,0,1,0,0,0,1,2,2,0,0]
base 519 Q8 =
[1,0,0,2,1,0,0,2,2,1,0,2,2,2,2,2,2,2,0,0,2,2,0,0,0,0,0,1,0,0,1,2]
base 519 Q7 =
[0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,2]
base 519 Q6/H7,J7 =
[2,0,1,2,1,0,2,1,1,0,2,2,2,1,2,1]
```

## Custody and exact scope

The source compiler/replay live in
`cases/as_fonly_d7_global_q6_high_20260825/`.  Its frozen source closure SHA is
`ced77bd91a6fbe6bb6543c9a29bcf9a3918071f6cfe33ffa7413340a3d8d74fb`.
The compressed exact three-base custody archive has SHA
`5f4c03d545b709e5bfb6cd9820ca66129d75d3f974535d227e3747e0e22e30e4`.

This is a theorem about two accepted **filtered source states**, subject to
source/compiler review.  It is not yet a complete polynomial map modulo 81,
not a chronological digit lift, not a whole-base classification, and not an
all-depth `3`-adic lift.  The earlier attempt to interpret these filtered
states as direct `+81` map digits failed an exact determinant assertion and is
quarantined.  No characteristic-zero, bounded-support, counterexample, or JC2
claim follows.

The next typed gate is to reimpose every earlier source row after the next
restoration, compute the first genuinely unencoded divided layer, and extract
the full Jacobian/cokernel and smooth-Hensel minor at both witnesses.  The base
303 UNSAT response remains diagnostic until a checked CNF/DRAT certificate is
available.
