# THETA-reopen Hostile Review (GPT-5.5)

## 0. Hash Gate

CONFIRMED. I created this report skeleton before the hash gate, as
requested. I then verified all four frozen read-only inputs under
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.sbAHnD/inputs`.
The computed SHA-256 digests match the supplied values exactly:

- `4009c3abdc16e972aec121206664a21adc81ff8467dfe8d5a0f561e90f3a86d5`
  `theta-reopen-explicit-pullback-sol56-20260831.md`
- `2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5`
  `block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md`
- `7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474`
  `block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md`
- `69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9`
  `block-descent-a1-mprime-coordinator-integration-fable5-20260831.md`

Method note: this review used the frozen packet copies only, plus direct
polynomial differentiation. I did not fetch external literature, run a CAS, edit
charged inputs, edit canonical ledgers, or inspect `jc2-lean`. Citations below
use the frozen basenames and line numbers.

## 1. Constraint System (1.1)-(1.4)

CONFIRMED. The normal form is forced by the quotient
`U^2=A+A^2Z`: every class is uniquely `P(A,Z)+UQ(A,Z)`, matching the
structure packet's normal-form line (`structure:145-149`) and the THETA
packet's setup (`theta:43-50`).

The charged normalization is `{f,g}=kappa`, with the standard orientation
`J(h,k)=h_x k_y-h_y k_x`. Under the source chart
`A=x^2`, `U=x+x^3y`, `Z=2y+x^2y^2`, the three generator brackets are exactly
`2A^2`, `4U`, and `2+4AZ`; these are also the brackets recorded in
`theta:51-55`. The sign is consistent with the local Hamiltonian convention
`X_f=kappa partial_q`, `X_g=-kappa partial_p` at an etale companion point
(`structure:198-220`).

For arbitrary `F,G` in the ambient variables,

```text
{F,G}=2A^2(F_A G_U-F_U G_A)
     +4U(F_A G_Z-F_Z G_A)
     +c(F_U G_Z-F_Z G_U),        c=2(1+2AZ).
```

Putting `f=P+UQ`, `g=R_0+US_0`, and reducing `U^2` to
`H=A(1+AZ)`, the even part is exactly

```text
2A^2(P_A S_0-Q(R_0)_A)
+4H(P_A(S_0)_Z+Q_A(R_0)_Z-P_Z(S_0)_A-Q_Z(R_0)_A)
+c(Q(R_0)_Z-P_ZS_0),
```

and the odd coefficient is exactly

```text
2A^2(Q_A S_0-Q(S_0)_A)
+4(P_A(R_0)_Z-P_Z(R_0)_A+H(Q_A(S_0)_Z-Q_Z(S_0)_A))
+c(Q(S_0)_Z-Q_ZS_0).
```

So (1.3E)/(1.3O) and the coefficient system `E=kappa`, `O=0`
(`theta:65-86`) are the correct polynomial identities in
`C[A,Z]`. The first-jet equation
`2(q_1 r'-p's_1)=kappa` follows by taking the constant `A` coefficient of
`E` (`theta:105-115`). I see no normalization or even/odd split error.

## 2. Obstruction A-Degree-Zero (3.1)-(3.2)

CONFIRMED. If `P,Q,R_0,S_0` are all in `C[Z]`, every `A`-derivative term in
`E` vanishes and

```text
E=2(1+2AZ)(Q(R_0)'-P'S_0).
```

Let `B(Z)=Q(R_0)'-P'S_0`. The `A^0` coefficient of `E=kappa` gives
`2B=kappa`, hence `B=kappa/2`. The `A^1` coefficient is then
`4ZB=2kappa Z`, which is not the zero polynomial because `kappa != 0`.
This reproduces (3.1)-(3.2) (`theta:327-344`). The obstruction is independent
of the residue degrees, but only excludes the displayed ruling-degree-zero
class.

## 3. Obstruction A-Linear Minimal Jet (3.3)-(3.11)

CONFIRMED within its stated scope. Write `K=kappa` and use the ansatz

```text
P=Z^2+AC,  Q=-K/2+AD,  R_0=Z^3-Z+AE,  S_0=-3KZ/4+AL.
```

For `[A^0]O`, the first large summand has no contribution, the second gives
`4(C(3Z^2-1)-2ZE)`, and the last gives
`2(-K/2)(-3K/4)=3K^2/4`. With `c_*=3K^2/16`, `O=0` is therefore

```text
2ZE-(3Z^2-1)C=c_*,
```

which is (3.4). Since `gcd(2Z,3Z^2-1)=1`, all solutions are exactly

```text
C=c_*+2Z sigma,
E=(3c_*/2)Z+(3Z^2-1)sigma.
```

For `[A^1]E`, direct collection before substitution gives

```text
-3KC +(3KZ/2)C' -KE' +6D(3Z^2-1)-12ZL+2KZ=0.
```

Substituting the preceding parametrization reduces the first three terms to
`K sigma'-9KZ sigma-(9/2)Kc_*`, giving exactly (3.5). For `[A^1]O`, direct
collection gives

```text
4(CE'-C'E) -(9/2)KD -KL' +(3/2)KZD' +(3/2)K^2Z=0,
```

equivalently (3.6). For the highest odd coefficient, the actual coefficient is
`8Z(DL'-D'L)`, so in the domain `C[Z]` it is equivalent to (3.7). These checks
verify (3.4)-(3.8) term by term (`theta:348-376`).

The degree contradiction also checks. If `D != 0`, then (3.7) gives
`L=lambda D` in `C(Z)`, hence in `C[Z]`, with constant `lambda`. Let
`m=deg D` and leading coefficient `d`. In (3.5), the `D` term has leading
degree `m+2` with coefficient `18d`; no term except `-9KZ sigma` can cancel it.
Thus `deg sigma=m+1` and `lc(sigma)=2d/K`, which is (3.9). Then in (3.6),
using `C=c_*+2Zsigma` and `E=(3c_*/2)Z+(3Z^2-1)sigma`, the leading term of
`C'E-CE'` is

```text
6s^2(n+1)Z^(2n+2)-6s^2(n+2)Z^(2n+2)
=-6s^2 Z^(2n+2),
```

where `s=lc(sigma)` and `n=m+1`. This is the claimed
`-6lc(sigma)^2 Z^(2m+4)`. The right side of (3.6) has degree at most
`max(m,1)`, so cancellation is impossible.

If `D=0`, equation (3.5) becomes
`Ksigma'-9KZsigma-12ZL+2KZ-(9/2)Kc_*=0`. When `sigma` is zero or constant,
every term except the nonzero constant `-(9/2)Kc_*` is divisible by `Z`. When
`n=deg sigma>=1`, the same equation forces `deg L=n`; otherwise either
`-9KZsigma` or `-12ZL` has an uncancelled top degree. Equation (3.6) then has
left leading term `-6lc(sigma)^2Z^(2n+2)`, while its right side has degree at
most `max(n-1,1)`. This is again impossible.

The cases `D != 0` and `D=0`, with `sigma` zero/constant/nonconstant in the
second branch, exhaust all polynomial choices under `A`-degree `<=1` and the
fixed minimal jet `p=Z^2`, `r=Z^3-Z`, `T_0=0`. The packet's disclaimers are
correct: this does not cover another point of the minimal residue family,
nonzero `T_0`, or any `A`-degree `>=2` (`theta:405-410`).

## 4. Degree-8 Composition Claim (3.12)-(3.14)

CONFIRMED as strength evidence, not as an obstruction. With
`J(h,k)=h_x k_y-h_y k_x`, the displayed substitution (`theta:414-428`;
`structure:96-98`) gives

```text
J(x^2,x+x^3y)=(2x)(x^3)-0=2x^4=2A^2,
```

```text
J(x^2,2y+x^2y^2)=(2x)(2+2x^2y)=4x(1+x^2y)=4U,
```

and

```text
J(x+x^3y,2y+x^2y^2)
=(1+3x^2y)(2+2x^2y)-x^3(2xy^2)
=2+8x^2y+4x^4y^2=2+4AZ.
```

So the source chart pulls the bracket on `R` to the standard plane Jacobian.
If a landed admissible pair satisfies `{f,g}=kappa`, then its composed pair
`F=iota(f)`, `G=iota(g)` satisfies `J(F,G)=kappa`.

The cited `[C(x,y):K]=2` is also directly visible. Let
`K=C(A,U,Z)` inside `C(x,y)`. Since `A=x^2`, `C(x,y)=K(x)` because
`y=(U/x-1)/A`. Thus the degree is at most two. It is not one: the field
automorphism

```text
x |-> -x,        y |-> -y-2/x^2
```

fixes `A`, `U`, and `Z` but moves `x`, so `x notin K`. Hence
`[C(x,y):K]=2`. If the charged rank-four condition
`[K:C(f,g)]=4` is part of admissibility (`theta:132-140`), finite-extension
multiplicativity gives

```text
[C(x,y):C(F,G)]=[C(x,y):K][K:C(f,g)]=2*4=8.
```

A polynomial automorphism would have function-field degree one, so such a
landed pair would compose to a noninvertible Keller map of geometric degree
eight. This is safe routing input: it explains the strength of a successful
higher-`A` construction, but it does not disprove that construction.

## 5. Terminology Fork in Section 6

CONFIRMED. The structure packet says the provisional dynamical theorem is
about Hamiltonian derivations: nonconstant `X_H` is non-locally-finite exactly
when `H notin C[A]`, equivalently `Q_H != 0` or `partial_Z P_H != 0`
(`structure:151-162`). It also gives an independent boundary-valuation route
to non-local-finiteness (`structure:281-295`).

That is different from the morphism property of `pi|_S`. The connectedness
packet uses `pi|_S` as etale (`connectedness:73-83`), hence locally
quasi-finite; the finite map is the separate normalization map
`Y -> A2`. The THETA packet's section 6 distinction is therefore correct:
read "locally finite" literally only for the derivations, and "locally
quasi-finite" for `pi` (`theta:547-557`).

## 6. Strategic Soundness and Successor Lane

CONFIRMED, with the all-degrees induction left OPEN. The report is right that
finite exhaustion cannot be promoted from the frozen packets: there is no cap
on `deg_A P,Q,R_0,S_0` or on the off-`A=0` `Z` degrees (`theta:124-128`), and
the final scope statement keeps all `A`-degree `>=2` strata open
(`theta:559-569`).

The leading-term mechanism in (3.10) is a plausible pattern, but not yet an
induction. A promotable induction would have to say something like:

```text
For the fixed minimal residue point p=Z^2, r=Z^3-Z and T_0=0,
no finite A-degree polynomial lift solves E=kappa, O=0. More precisely,
after expanding P,Q,R_0,S_0 in A and eliminating all lower-order coefficient
conditions, some surviving Wronskian/Bezout leading term in Z has degree
strictly above every term available on the opposite side.
```

For the full horn it would have to be stronger still, covering every point of
the seven-parameter minimal residue family and every nonzero `T_0`.

The naive induction already breaks at `A`-degree two. Write
`P=Z^2+AC_1+A^2C_2+...` and similarly for `Q,R_0,S_0`. The equation (3.4)
still constrains `C_1,E_1`, and the displayed (3.5) for `[A^1]E` remains the
same. But `[A^1]O` no longer gives (3.6); it gains the free second-order term

```text
2(C_2(3Z^2-1)-2ZE_2)
```

on the right after division by four and rearrangement. This term can have
arbitrary `Z` degree and has exactly the kind of Bezout shape that can absorb
the Wronskian leading term used in (3.10). Also, `[A^3]O` is no longer just
`DL'-D'L=0`; second-order coefficients contribute. Thus the first-order proof
does not bootstrap without a new elimination invariant or normal-form
complement controlling those higher compensators.

Successor lane scope: start with the full `A`-adic coefficient hierarchy for
the fixed minimal jet, analyze the `A^2` compensator operator explicitly, and
only then attempt an induction on maximal `A` degree. Treat any all-family or
nonzero-`T_0` claim as a separate strengthening.

## 7. Verdict

1. CONFIRMED: the constraint system (1.1)-(1.4) has the correct bracket
   normalization and even/odd normal form.
2. CONFIRMED: `OBSTRUCTION[A-DEGREE-ZERO]` follows from the forced `A^0` and
   `A^1` coefficients.
3. CONFIRMED: `OBSTRUCTION[A-LINEAR-MINIMAL-JET]` is exhaustive for
   `A`-degree `<=1`, `p=Z^2`, `r=Z^3-Z`, `T_0=0`; all leading-term and
   `D=0` branches check. Its stated exclusions do not extend beyond that
   scope.
4. CONFIRMED: the degree-8 composition claim is algebraically sound for a
   landed admissible pair with `[K:C(f,g)]=4`, and is correctly typed as
   strength evidence rather than an obstruction.
5. CONFIRMED: the locally finite / locally quasi-finite terminology fork is
   necessary and matches the structure packet.
6. CONFIRMED: the no-cap strategic warning is sound. A possible all-degree
   induction requires new work; the first obstruction to the naive induction
   appears already at `A`-degree two.

The two obstructions are promotable only as bounded exclusions:
`A`-degree zero universally, and `A`-degree `<=1` at the simplest minimal jet
with `T_0=0`. The degree-8 reframe is safe to adopt as routing input: a
successful admissible pullback would be counterexample-level data, but the
current report still leaves the higher-`A`, other-family, and nonzero-`T_0`
construction problem OPEN.

No exit price is asserted.

<!-- BODY-END -->
