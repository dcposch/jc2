# TD6 V77 q3 gamma dual adjoint — exact AWS producer report

Date: 2026-08-25  
Status: **PRODUCER-EXACT / DUAL-HOST PASS / DIAGNOSTIC, NOT FAMILY COVERAGE**

## Verdict

On the generic three-center open `D(U*(C-3U^2)*B3)`, with q2 fixed to zero,
the q3 boundary jet

\[
q_\gamma(t)=t+\gamma t^3+t^{25}
\]

has been propagated exactly through the constant transport echelon and the
varying first Jacobian stage over dual numbers.  The calculation retains the
transport RHS source key, the direct term `3 gamma t^2` in q-prime, every
varying pivot multiplier, the genuine 2,893-term P12, and an original-row
source replay.

The selected first pivot product varies nontrivially with gamma.  The raw
P12 gamma derivative has four monomials.  After exact varying first-stage
reduction its gamma remainder has three affine monomials, rather than being
a scalar.  Thus q3 genuinely changes the first-stage operator and the
reviewed q2 scalar identity cannot simply be copied to a higher-q family.

The dual remainder remains a unit because its base value is the already
reviewed `-k/50`.  This emptiness is automatic for a square-zero deformation
of an empty base; it is not a q3 neighborhood or full-family kill.

## Exact endpoints

| gate | result |
|---|---|
| transport | rank `3470/3602`; one gamma-bearing RHS pivot; matrix derivative zero |
| first Jacobian | rank `38/132`; original-row dual replay exact |
| first minor | nonzero gamma derivative, SHA `c0730fa1...` |
| genuine P12 | base 2,893 terms; gamma 4 terms, SHA `70d253cd...` |
| reduced remainder | base `-k/50`; gamma 3 affine terms, SHA `3dd07bb5...` |
| multipliers | 28 source rows; 14 lambda-prime rows; 1,489 base and 1,149 gamma support terms |
| derivative replay | `lambda0*bprime` and `lambdaprime*b0` each 3,386 terms; omission control detects lambda-prime removal |
| denominator audit | 77,512 termwise slots; radical contained in `U*(C-3U^2)*B3` |

All mathematical stdout agrees across Box02 and Box03 after deleting only
the two host/run-tag lines.  The normalized body SHA-256 is
`52273c663073270c777c21d0da018f671b3e3e74cb892dc3e70b94749743f76c`.

## Custody

Case:
`cases/td6_c1_c2_c3_q3_gamma_dual_adjoint_v77_aws_20260825/`

| artifact | SHA-256 |
|---|---|
| source archive | `333e25718c3e492497822b64c9b6e732cc6f26853bf2196a296ebc9db10a2293` |
| V77 replay | `5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22` |
| Box02 stdout | `c046639746e5916c0ff6226695d39aa11a0ed004838c5e8ffa544b6ebe226328` |
| Box03 stdout | `0b0b953295c02325fd8ee9617cacc7b36ca2fd93b941c73c64bff2c1d100ea2b` |
| normalized body | `52273c663073270c777c21d0da018f671b3e3e74cb892dc3e70b94749743f76c` |

The initial system-Python pair failed before mathematics because `flint` was
absent.  Those rc-1 logs are retained as deployment-negative custody.  The
proof-bearing reruns used `/home/ubuntu/venvs/td6`, a 12-GiB cap, and a
four-hour timeout; both returned rc 0.

Lightweight verification:

```sh
python3 cases/td6_c1_c2_c3_q3_gamma_dual_adjoint_v77_aws_20260825/verify.py
```

## Next exact gate

Do not continue coefficient by coefficient.  Run one exponent-keyed
vector-AD pass for every licensed higher-q coefficient
`q2..q14,q16..q24`, through transport, first, previous/pole, and current,
and compute the joint tangent/conormal kernel and image.  Then either derive
a denominator-free source-level telescoping syzygy or construct a
rank-stratified fraction-free/Fitting atlas.  The nonzero first-minor gamma
variation forbids treating the q2 pivot echelon as globally unit over the
full higher-q polynomial ring.

## Scope firewall

This report proves no finite gamma neighborhood theorem, no all-gamma
theorem, no coverage of higher q/dead-stretch/p-boundary/F1/pole moduli, no
whole-TD6 or SP-2 kill, and no result on JC2.
