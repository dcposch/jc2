# Generic-square high-contact `A` prolongation

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS, INCLUDING EXACT `Q`; INDEPENDENT EXACT ROW
CERTIFICATE PASS.  ONE HIGH-CONTACT CONE ONLY; NO NORMAL-FAN,
SQUARE-BRANCH, OR ORDER-TWO VERDICT.**

## 1. Producer endpoints

The corrected client reconstructs all seven complete frozen loaded source
rows under

```text
Lambda=sigma^2,
M=sigma^3*(A0+sigma*A1),
R=sigma^2*(B0+sigma*B1),
C=sigma^4*(E0+sigma*E1),
k10=k0+sigma*k1.
```

Here `A_i,E_i` are linear in `z`, `B_i` have degree below four, and the
compiler uses the ordinary-coordinate conventions recorded in the design.
It extracts source grades fourteen and fifteen without dropping any row or
later coefficient, checks the forbidden-load firewall, and saturates the
combined source ideal only by `p*k0`.

This frozen client keeps the square parameter `p` constant in `sigma`.  It
retains every tangent coefficient displayed above, but it does not contain a
`p1` tangent.  Thus the producer endpoint below is, by itself, a fixed-`p`
high-contact statement.

| field | host | tag | time | peak RSS | validator |
|---|---|---|---:|---:|---|
| `Q` | Box03 | `max12_812_order2_square_aprol_v2_q_20260826T075600Z_box03` | 10.97 s | 38,180 KiB | `PASS_SQUARE_A_PROLONGATION` |
| `F_65521` | r6d | `max12_812_order2_square_aprol_v2_p65521_20260826T075600Z_r6d` | 6.48 s | 36,372 KiB | `PASS_SQUARE_A_PROLONGATION` |

Both engine return codes are zero and both runs used zero swap.  Exact-Q
stdout SHA-256 is
`f24167e2d9544d0937851ae14831ee476cd22116c0f9cdcf75d3ac31ff634d1e`;
the good-prime stdout SHA-256 is
`274942a72cbfb03dfac712238c6072784f314a27c51158af8c0aa7fa5473d556`.
The good-prime run is a software control, not the characteristic-zero proof.

## 2. Exact source result

Every source row is exactly divisible by `sigma^14`; the grade-fourteen and
grade-fifteen quotient identities both pass.  Neither grade depends on
`k6,k2,mu2,mu4,mu6,J`.  The grade-fourteen cancellation family

```text
B0=0,                 E0=-(5*k0/24)*A0
```

is verified in ordinary coordinates using
`e_i=-(5*k0/12)*a_i`, because `C=(e1*z+e0)/2`.  This confirms that grade
fourteen alone does not kill `A0`.

After adjoining both complete grades and localizing on `D(p*k0)`, the exact
characteristic-zero radical is

```text
(a1,
 a0,
 aa1*e0+aa0*e1,
 p*aa1*e1-2*aa0*e0,
 p*aa0*e1^2+2*aa0*e0^2).
```

In particular both coefficients of the leading linear polynomial
`A0=a1*z+a0` lie in the radical, while `1` does not.  Thus every
characteristic-zero point of this localized high-contact source scheme has
`A0=0`.  The residual tangent relations displayed above are recorded but
are not promoted beyond this cone.

## 3. Independent source-to-receiver certificate

The distinct package
`cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/` gives a
second construction, with `RESULT.md` SHA-256
`eba4640a9c7da51e4297e7e0b3c236f73f2eb2f70770de0634e1d0fea652d13f`.
Its exact-Q Box03 and `F_65521` r6d lanes both pass.  Rather than recomputing
the producer radical, it verifies coefficientwise for all seven rows that
the source grades are the lower-unitriangular Faber transform of

```text
h14 = [ (3/4) A0 E0/L
       -(3/8) B0 A0^2/L^2
       +(5/32) k0 A0^2/L ]_-,

h15 = [ (3/4)(A0 E1+A1 E0)/L
       -(3/8)(B1 A0^2+2 B0 A0 A1)/L^2
       +(5/32)(k1 A0^2+2 k0 A0 A1)/L
       -(1/16) A0^3/L^3 ]_-,
```

where `L=z^2+p/2`.  Clearing `16 L^3` in `h15` and reducing modulo `L`
gives exactly `-A0^3`.  Vanishing of the seven negative Laurent
coefficients forces `L^3` to divide the cleared numerator; hence
`L | A0^3`.  On `D(p)`, `L` is squarefree of degree two and
`deg(A0)<=1`, so `A0=0`.  This hand separator is independent of all
grade-fourteen root allocations and agrees with the producer radical.

## 4. Failed-attempt quarantine

The first two-host attempt failed its own validator because a control
substitution missed the coefficient factor two and because `quit(81)` is
not valid Singular syntax.  The corrected source was refrozen and rerun on
both hosts.  Complete first-attempt streams are preserved under
`quarantine_v1_box03/` and `quarantine_v1_r6d/`; no first-attempt endpoint
is evidence.  See `AWS_LAUNCH_METADATA.md`.

## 5. Scope firewall and next gap

This result eliminates the surviving leading `A` direction only in

```text
ord_sigma(R)>=2,       ord_sigma(C)>=4
```

on `D(p*k0)` after the reviewed square half-weight ray.  It does not prove
that this cone exhausts the generic-square normalized Newton/Rees fan.
Lower valuations of `R` or `C`, root-allocation faces such as `L | M*S`,
the moving-`p` tangent, the degenerate `p=0` intersection, later
terminal/Taylor receivers, the whole square branch, all order two,
`(8,12)`, maximum twelve, and JC2 remain open in this package.  Hand
differentiation with `L(sigma)=L+sigma*ell` predicts the additional cleared
grade-fifteen numerator

```text
-12*ell*L*A0*E0 + 12*ell*B0*A0^2
 -(5/2)*ell*k0*L*A0^2.
```

Modulo `L`, its only survivor is `12*ell*B0*A0^2`; the grade-fourteen
equation already predicts `L | B0*A0^2`.  This strongly suggests the
`-A0^3 mod L` separator persists, but that extension is not promoted until
an exact moving-`p` source replay confirms the bridge.  The immediate
mathematical tasks are that addendum and the finite correction-aware fan
cover of the lower-valuation cones.
