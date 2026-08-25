# TD6 V77: q3 gamma dual adjoint on the generic three-center chart

Date: 2026-08-25  
Status: **PRODUCER-EXACT / DUAL-HOST PASS / FIRST-ORDER DIAGNOSTIC ONLY**

## Object and scope

The replay keeps the fixed source-typed three-center section

```
y=s^-1,
x=C*s+V*s^2+U*s^3+t*s^4,
p=t^15,
q_gamma=t+gamma*t^3+t^25,
```

with zero q2 coefficient, zero dead stretch, and the frozen F1/pole data.  It
works over `E(C,V,U)[gamma]/(gamma^2)` on

```
D(U*(C-3U^2)*B3).
```

Here `B3` is the previously frozen center divisor, not gamma.  The q3 source
term is the exact original transport key `('g','X',0,3)`, and the direct
Jacobian derivative `3*gamma*t^2` in q-prime is retained.

This is not a q3-family or neighborhood theorem.  The gamma=0 fixed-A3 base
is already the unit ideal (the V76 dependency), so its square-zero thickening
is formally empty.  The content of V77 is the exact source support,
varying-echelon/lambda-prime, genuine-P12, and denominator audit needed for a
nontruncated simultaneous-modulus successor.

## Exact result

Both AWS runs returned rc 0 and agree exactly after removing only the two
host-specific `aws_hostname` and `aws_run_tag` lines.  The normalized stdout
SHA-256 is

```
52273c663073270c777c21d0da018f671b3e3e74cb892dc3e70b94749743f76c
```

Load-bearing endpoints:

* transport rank `3470/3602`, with one gamma-bearing affine RHS pivot and
  gamma-independent transport matrix;
* first rank `38/132`; the selected first minor has nonzero gamma derivative
  (`c0730f...`), so a full q3 pencil may not treat the q2 pivots as polynomial
  units;
* the genuine 2,893-term P12 compiler has four gamma-derivative monomials
  (SHA `70d253...`);
* after exact varying first-echelon reduction, the base remainder is
  `-k/50`, while the gamma derivative is a three-term affine polynomial
  (SHA `3dd07b...`), not a scalar;
* 28 original first rows support the source identity; 14 have nonzero
  lambda-prime support; the base and gamma multiplier projections have
  1,489 and 1,149 terms respectively;
* exact differentiation gives 3,386 terms in each of `lambda0*bprime` and
  `lambdaprime*b0`; omitting lambda-prime fails the identity;
* all exact leaf/termwise denominator radicals are among `U`,
  `C-3U^2`, and `B3`; the termwise dual audit covers 77,512 slots.

The three-term gamma remainder is the decisive scheduling signal: q3 does
not preserve the q2 first-stage scalar remainder, so a later staged
compatibility or source-level telescoping syzygy is genuinely required.

## Custody

The first pair of launches used system Python and failed before mathematics
with `ModuleNotFoundError: flint`; they are retained under
`deployment_negative/` as deployment-only controls.  The corrected pair used
`/home/ubuntu/venvs/td6`, a 12-GiB address-space cap, and a four-hour timeout.

| item | SHA-256 |
|---|---|
| source archive | `333e25718c3e492497822b64c9b6e732cc6f26853bf2196a296ebc9db10a2293` |
| source manifest bytes | `83eff5e28413162cb4f89379e4994a55462bf2520afaf564ffc7136991e259de` |
| V77 replay source | `5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22` |
| Box02 stdout | `c046639746e5916c0ff6226695d39aa11a0ed004838c5e8ffa544b6ebe226328` |
| Box03 stdout | `0b0b953295c02325fd8ee9617cacc7b36ca2fd93b941c73c64bff2c1d100ea2b` |
| normalized stdout | `52273c663073270c777c21d0da018f671b3e3e74cb892dc3e70b94749743f76c` |
| Box02 stderr/time | `042831bb4bc7f5756bd859f428f153a0c432d718018addfd99e27025fcc2637e` |
| Box03 stderr/time | `7dcf34513dbf828b0aea7233e66d37173b82d720f3f9c0d590bbdb099f9c81e0` |

Box02: `ip-172-30-0-186`, run
`/home/ubuntu/runs/td6_v77b_q3_gamma_dual_box02_20260825T2227Z`, maximum RSS
550,536 KiB.  Box03: `ip-172-30-0-249`, run
`/home/ubuntu/runs/td6_v77b_q3_gamma_dual_box03_20260825T2227Z`, corrected
mirror with the same mathematical body.

## Firewall

V77 does not prove a finite gamma neighborhood empty, does not kill the full
gamma family, does not cover the remaining higher-q or dead-stretch moduli,
does not kill TD6 or SP-2, and does not resolve JC2.

