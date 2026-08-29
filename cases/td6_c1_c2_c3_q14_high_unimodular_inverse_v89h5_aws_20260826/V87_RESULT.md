# TD6 V87TFAQ literal total-`(F,all licensed q)` raw-source result

Date: 2026-08-26

Producer verdict: **PASS on Box02 and r6d.** Independent hostile review is
not yet incorporated.

## Exact result

Put

```text
F  = C*U - V^2 + U^3,
H  = C - 3*U^2,
B3 = 4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4
     + V^4 - 20*V^2*U^3 + 20*U^6,
q(t) = t + sum_{e in E} q_e*t^e + t^25,
E = {2,...,14,16,...,24}.
```

On the normalized three-center source chart, with all 132 transport-free
section coordinates retained, the rebuilt genuine raw P12 and 38 packed raw
FIRST maps satisfy the exact identity

```text
U^12*H^3*B3
  = a_P*P12(C,V,U,q)
    + sum_i a_i*FIRST_i(C,V,U,q)
    + F*h_F + sum_{e in E} q_e*h_e
```

in `Q[C,V,U,q_e:e in E]_{U*H*B3}`. The `a_P,a_i` are the frozen
V82QST3 multipliers. The q coefficient ring was sparse, multivariate, and
untruncated, and any q-dependent inverse was a closed failure.

The expanded source and residual both have exact total q-degree one. Thus no
cross-q monomial occurs in this particular family. The implementation did not
assume this: it decomposed the positive-q residual by an exact ordered
augmentation-ideal partition, assigning every nonconstant q monomial to one
of its factors. That same check would therefore have handled cross-q terms.

The common denominator of all sources, multipliers, products, `h_F`, and the
22 `h_e` is exactly

```text
C*U - 3*U^3 = U*H.
```

No `F` or q factor is inverted, and no denominator outside the registered
`U,H,B3` set occurs. Multiplication once by `U*H` makes all 312,604 audited
`E3` coefficients polynomial; the cleared identity has 5,626,872 scalar
coordinates and replays exactly.

## Source custody and fail-closed gates

Each of the 22 q variables enters in two literal places:

- its transport RHS at `('g','X',0,e)`;
- its direct raw-receiver derivative term `e*q_e*t^(e-1)` in `q'`.

The client required exactly one registered transport source path for each q
variable. For every variable, separately omitting its transport path and its
direct-`q'` path changed the raw FIRST family: all 44 path-omission fixtures
passed. The normalized target-shear coordinate `q15` remains explicitly fixed
at zero; no unproved tangent-gauge removal is used.

At all q variables zero, the genuine 2,893-term P12 and every one of the 38
FIRST maps reproduce the frozen V85 source inventory exactly. Setting also
`F=0` replays the frozen V82QST3 special identity, and the complete
parameter-label set is exactly `0..131`. No staged CURRENT, PREVIOUS, or POLE
row is consumed; only literal degree-12 extraction from the frozen raw CURRENT
compiler is used.

The residual has 3,553 section monomials. Its q-zero part divides
coefficientwise by `F` in 50,346 scalar coordinates and reproduces the frozen
V85 `h_F` digest. The augmentation partition accounts for 46,378 nonconstant
q coefficients. Omitting P12 or the first active FIRST row breaks replay.

## DVR consequence

On `D(U*H*B3)`, the left side is a unit. Therefore there is no DVR arc in
this retained literal source family on which all P12/FIRST equations vanish
and `F` together with all 22 licensed q coordinates have positive valuation.
Indeed every coefficient of `h_F,h_e` lies in the registered localization,
so the right side would have positive valuation while the left side remains
a unit.

This is the exact producer-tier meaning of
`positive_F_and_all_licensed_q_arcs_on_this_slice_excluded`.

## Certificate hashes

- source archive:
  `e80b1cba7b4a1749c7f12ecd7b6a8d9418e73b6b01d8f82081dbb76f113669d3`;
- V87 client:
  `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463`;
- V86 parent client:
  `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c`;
- V85 parent client:
  `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e`;
- total raw P12:
  `1ff8beed73f24dd63ca5692510223e48b7a18ce65d6000241a0620d1dee6ea87`;
- localized `h_F`:
  `5f429f959e71b89a39c8c4317765f71c627550c2754db7ffd7a5f6f9043f4ab9`;
- total/q-zero source inventory:
  `079447d97638f18b7807cdd84b1178f9969d3f93727c7ab40588079586160a68`;
- `h_F,h_e` inventory:
  `85d0c375c3a042f3b80567106adf4c0e5115f7774e18dfd298aad3faecbbb32b`;
- 44-fixture omission inventory:
  `ad23c19b145f6d839192a94b06e47db4cf233365b18aebd8ba59674452415918`;
- exact-result record:
  `5b27705017fce762b8622f32978dfbd6d13bcb75c1ffe2b85e156c003f94f570`;
- byte-identical mathematical stdout on both hosts:
  `7b741c3159e7b39fcafb1851013a2cf3445ca57c3f46dc65ee09b947649557b5`.

## AWS custody

Both lanes returned `rc=0` with the distinct
`TD6-V87TFAQ-LITERAL-TOTAL-F-ALLQ-RAW-P12-SOURCE PASS` banner. The four
mathematical output files and stdout are byte-identical across hosts.

- Box02: 19:26.61 elapsed, 3,762,460 KiB maximum RSS, zero swap;
- r6d: 19:27.93 elapsed, 3,762,384 KiB maximum RSS, zero swap.

## Scope firewall

This totalizes `F` together with exactly the 22 literal normalized q jets
`q2..q14,q16..q24` on one source slice. It does not totalize `q15`, cover a
unit q coordinate, or cover dead stretch, correction, orbit/pole, centering,
deck/torsion, other boundary moduli, or a total-Rees chart. It proves no whole
fixed-A3, TD6, SP-2, or JC2 statement.
