# TD6 V86TFQ2 literal total-`(F,q2)` raw-source result

Date: 2026-08-26

Producer verdict: **PASS on Box03 and r6d.**  Independent hostile review is
not yet incorporated.

## Exact result

Put

```text
F  = C*U - V^2 + U^3,
H  = C - 3*U^2,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6,
q_beta(t) = t + beta*t^2 + t^25.
```

On the normalized three-center source chart, with all 132 transport-free
section coordinates retained, the rebuilt genuine raw P12 and 38 packed raw
FIRST maps satisfy the exact identity

```text
U^12*H^3*B3
  = a_P*P12(C,V,U,beta)
    + sum_i a_i*FIRST_i(C,V,U,beta)
    + F*h_F + beta*h_beta
```

in `Q[C,V,U,beta]_{U*H*B3}`.  The `a_P,a_i` are the frozen V82QST3
multipliers.  The coefficient ring in `beta` was a sparse, untruncated
polynomial ring, not a tangent or fixed-degree quotient.

The expanded total source and its residual both have exact beta degree one.
Consequently `h_beta` is beta-independent.  The common denominator of all
sources, multipliers, products, `h_F`, and `h_beta` is exactly

```text
C*U - 3*U^3 = U*H.
```

No `F` or `beta` factor is inverted, and no denominator outside the
registered `U,H,B3` set occurs.  Multiplication once by `U*H` produces the
emitted polynomial certificate tables.

## Source custody and fail-closed gates

The client rebuilds the literal beta source in both places where it enters:

- the transport RHS at `('g','X',0,2)`;
- the raw receiver through `q_beta'=1+2*beta*t+25*t^24`.

Removing either path changes the raw FIRST family.  At `beta=0`, the genuine
2,893-term P12 and every one of the 38 FIRST maps match the frozen V85 source
inventory exactly.  Setting also `F=0` replays the frozen V82QST3 identity,
and the complete parameter-label set is exactly `0..131`.  No staged CURRENT,
PREVIOUS, or POLE row is consumed.

The residual has 3,338 parameter monomials.  Its beta-zero part divides
coefficientwise by `F` in 50,346 scalar coordinates and reproduces the frozen
V85 quotient hash.  Its positive-beta part shifts exactly by one beta power
in 3,330 coefficients.  The final clearing audit checks 65,005 exact `E3`
coefficients and 1,170,090 polynomial scalar coordinates.  Omitting P12 or
the first active FIRST row breaks replay.

## Arc consequence

On `D(U*H*B3)`, the left side is a unit.  Therefore there is no DVR arc in
this retained literal source family on which all P12/FIRST equations vanish
and both `F` and `beta` have positive valuation.  This is the exact
producer-tier meaning of `positive_F_and_beta_arcs_on_this_slice_excluded`.

## Certificate hashes

- authoritative V3 source archive:
  `a7e3681db04b927458be08106bcf9756ce50ea56ff176c80e4b146b4eaf0d508`;
- V86 client:
  `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c`;
- total raw P12:
  `ca69df8acbad9e4ed61b1d0346c659f0f8ada5275fe693a3e25b8452bb968a7f`;
- localized `h_F`:
  `d42fd41927eaa8b89feb97ca5e78f23b21f267e07bbcc6cb1f0a8cf8ae9d6359`;
- localized `h_beta`:
  `ff283ad8cd4b8ba277459c168c5dbc74473cea7714be1473232681e7eaf928d8`;
- cleared 2,797-term `h_F` table:
  `89ecec18cea6547fe465fc4f6088f7f94ec9b6d717eefb33386f5b3fab6d49e0`;
- cleared 3,330-term `h_beta` table:
  `590f88a20183a4d4363a4e14397084cae347838331abc6df536f60129f2f0384`;
- total/beta-zero source inventory:
  `450c478c6e8d9e3bbdeef4470dc2c3fdfa999f74713e27cc500861f8e1938597`;
- exact-result record:
  `50c91f3253a564e52d356ac6ea1e9216ab96e84abe95c7898ea96ec1d481f236`;
- byte-identical mathematical stdout on both hosts:
  `48799b2b3e20553198ca9fd0e8820551145fc27c7aa1a71f685d133aaff928e3`.

## AWS custody

Both lanes returned `rc=0` with the distinct
`TD6-V86TFQ2-LITERAL-TOTAL-F-Q2-RAW-P12-SOURCE PASS` banner.  The four
mathematical output files and stdout are byte-identical across hosts.

- Box03: 17:23.45 elapsed, 1,046,304 KiB maximum RSS, zero swap;
- r6d: 17:17.87 elapsed, 1,045,420 KiB maximum RSS, zero swap.

The V1 harness failure and the non-authoritative, latency-heavy V2 replay are
quarantined by `DEPLOYMENT_ERRATUM.md` and do not contribute to this verdict.

## Scope firewall

This totalizes only the literal `q2=beta` coefficient together with `F` on
one normalized source slice.  It does not totalize the other q jets, dead
stretch, correction, orbit/pole, centering, deck/torsion, or boundary
moduli; cover unit-beta fibres; supply a full total-Rees chart; or prove a
whole fixed A3, TD6, SP-2, or JC2 statement.
