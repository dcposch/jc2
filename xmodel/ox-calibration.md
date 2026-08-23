# Ox calibration — independent D25 verdict

## Scope and exclusions
- Read only `xmodel/sol-ideas-0821.md` items 1–2 for the claim.
- Did **not** read `SHEET6-DIRECTIONB.md §9.S2`, `cases/d25_certificate_replay.json`, or any replay output.
- Derived parsing, row selection, coefficient extraction, and controls from the sibling `.ms` inputs.
- Code: `cases/ox_calibration.py`.

## Verdict: REFUTED
The claimed pivot certificate is not supported by the raw parked-fiber systems at either prime. The raw equations contradict the certificate before its claimed triangular reduction can produce 16 branches.

## Raw-system findings
| Prime | Equations | Variables | Terminal source rows | Distinct terminal constants | Localized dimension |
|---|---:|---:|---:|---:|---:|
| 105337 | 34 | 28 | 18–23 zero-based | 6 | −1 (empty) |
| 105673 | 34 | 28 | 18–23 zero-based | 6 | −1 (empty) |

### Claimed terminal matrix
My parser independently reproduces the claimed coefficient matrices exactly:

```text
p=105337
81190 11537  71983
21068 40041 102675
91127 14342 11531
102882 73079 60568
86415 37898 45675
29262 89263 75336

p=105673
62322 85289 102850
97729 25028   7845
65138 63462  50448
57279 19175  12220
20272 17266  48552
37031 29570  71293
```

But the raw rows are not six trinomials in `(U,V,1)` after substitution of the emitted Laurent relations. They are large multivariate polynomials containing additional base terms. Their `U`, `V`, and constant coefficients match the displayed matrix, but those coefficients alone do not form a closed subsystem.

## Root contradiction
The raw structural/Laurent rows force:

```text
x70 + 52700*x72 = 0      p=105337
x70 + 9676*x72  = 0      p=105673
```

Together with the other emitted compatibility rows, the full localized raw ideal has dimension `-1`. Thus the raw chart is already empty.

A negative control replacing the six inconsistent terminal constants by one common constant still yields an empty localized system. This confirms that the first obstruction is not merely the six distinct constants; it comes from the interaction of the structural Laurent rows with the rest of the raw ideal.

## Lift-pivot check
The five residual rows are not compatible with the claimed rank-two affine block. My direct extraction gives a zero `2×2` minor in columns `(x33,x38)`:

| Prime | Derived minor | Unit? |
|---|---:|---|
| 105337 | 0 | no |
| 105673 | 0 | no |

So the claimed exact solution of `x33,x38` followed by four free lifts is not available from the raw residual rows without an unstated reduction whose validity is not exhibited by the `.ms` systems.

## Negative controls
1. **Aligned terminal constants:** replaced all six terminal constants by the first one. The localized subsystem remains empty, showing that inconsistency is deeper than unequal terminal values.
2. **Direct minor extraction:** tested the claimed `(x33,x38)` minor directly from the residual affine forms; it is zero, so it cannot be a Laurent unit.
3. **Full raw saturation:** saturated by `W1*W2*uW1*uW2*x70*x71*x72*x73*x47*x52*x53*x54*x55*x57*x58*x59*x60*x62*x63*x65*x66`; the full raw system remains empty.

## Counts derived from this run
- Raw parked variables: **28**
- Raw parked equations: **34**
- Residual rows: **5**
- Terminal candidate rows: **6**
- Distinct extracted terminal constants: **6 / 6**
- Localized raw dimensions: **−1, −1**
- Aligned-control dimensions: **−1, −1**
- Verified disjoint affine components: **0**
- Verified carrier dimension: **not applicable**, because the claimed base quotient was not reached.

## Conclusion
Items 1–2 are refuted as certificates for the emitted `.ms` systems. Although the note’s displayed matrices can be recovered from selected coefficients, the required closed terminal reduction, unit lift pivots, dimension 10 base quotient, 16 branches, and downstream dimension/count claims do not follow from the raw inputs used here.
