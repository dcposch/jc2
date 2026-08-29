# Unit-root transport: the fixed endpoint cascade is root-local

Date: 2026-08-28  
Author: Sol Ultra discriminator desk  
Status: **EXACT PRODUCER / AWAITING HOSTILE REVIEW**

## Verdict

Fable's proposed single-root transport mechanism is correct, subject to the
same reviewed reduced branch-P prefix, complete characteristic schedule, and
fixed characteristic cascade used by the endpoint packet.

Let `alpha` be a simple root of the squarefree polynomial `A`, and assume

```text
nu=V0 is a unit at alpha, i.e. V0(alpha) != 0.
```

Then the complete fixed-`F1=A^2` characteristic cascade transports to the
local DVR at `alpha`.  It gives

```text
ord_alpha(g22) >= -2
```

apart from the optional homogeneous kernel `c22*A^-5`, whose endpoint image
is identically zero.  Since the raw `G22` receiver is absent, the original
endpoint row is

```text
D22_raw = -L22(g22),
L22(R)  = -40*A^3*A'*R - 8*A^4*R'.
```

The simple-root condition makes `A` a uniformizer and `A'` a unit.  Therefore
`L22` sends every term of order at least `-2` into the maximal ideal at
`alpha`.  Thus

```text
D22_raw in (X-alpha),
```

which contradicts the endpoint target `D22=1` at this single root.

Consequently, every full endpoint stratum containing even one root of `A` at
which `V0` is nonzero is field-empty.  In divisor notation
`C=gcd(A,V0)`, this kills every `C != A` stratum at the endpoint.  It does not
touch the deep stratum `C=A`.

This conclusion is independent of q1 and does not use the provisional D9
repair.  It is not a JC2 result: the raw-normal-form landing, branch coverage,
and global degree-ceiling problems remain.

## 1. Exact `epsilon^2` Newton model

Work after extending the characteristic-zero ground field to contain the
simple root `alpha`.  Put

```text
X=alpha+epsilon,
A=epsilon*a(epsilon),       a(0)=A'(alpha) != 0,
t=epsilon^2*s,
H(epsilon,s)=epsilon^-4 F(alpha+epsilon,epsilon^2*s).
```

For the reviewed reduced prefix

```text
F0=A^4,
F1=A^2*V0,
F2=(V0^2+A^2*Z)/4,
F3=(V0*Z+A*T)/8,
```

direct substitution gives the exact identity

```text
Q = a(epsilon)^2 + V0(alpha+epsilon)*s/2,

H = Q^2
  + epsilon^2*(a^2*Z*s^2/4 + V0*Z*s^3/8)
  + epsilon^3*a*T*s^3/8
  + sum_(i>=4) epsilon^(2i-4)*F_i*s^i.                 (1)
```

In particular,

```text
H(0,s)=(A'(alpha)^2+V0(alpha)*s/2)^2.                 (2)
```

Thus Opus's `epsilon^2` leading square is exact.  It explains why a
`V0`-unit root can survive much deeper than a `V0`-zero root: the leading
Newton polynomial is already a square, rather than a genuine quartic whose
square defect is visible at D7--D9.

For any exponent `beta`, coefficient comparison after `t=epsilon^2*s`
gives

```text
(F^beta)_k
 = epsilon^(4*beta-2*k) [s^k] H(epsilon,s)^beta.       (3)
```

Hence the mode born at even weight `m`, with
`beta_m=(12-m)/8`, contributes to `g_n` at order at least

```text
6 + 3m/2 - 2n.                                        (4)
```

At the load-bearing mode rows, the leading coefficients from (2) are
nonzero and the exact orders are

| mode/row | coefficient in `H(0,s)^beta` at `a(0)=V0(alpha)=1` | order |
|---|---:|---:|
| `c6` at `g8` | `3/32` | `-1` |
| `c10` at `g11` | `1/4` | `-1` |
| `c14` at `g14` | `1` | `-1` |
| `c16` at `g16` | `1` | `-2` |
| `c18` at `g18` | `1` | `-3` |
| `c20` at `g20` | `1` | `-4` |

This independently reproduces the fixed cascade's mode-pole schedule.
The checker derives the entries with exact generalized binomial
coefficients; no floating point or CAS is used.

## 2. The coefficientwise normalization

The decisive observation is simpler than expanding every `epsilon` rung.
In the local DVR let `nu=V0`, a unit, and define

```text
Fbar_i = nu^-i F_i,
gbar_n = nu^-n g_n,
cbar_m = nu^-m c_m.                                    (5)
```

Equivalently, only at the level of the characteristic series,
`Fbar(t)=F(t/nu)` and `Gbar(t)=G(t/nu)`.  Then

```text
Fbar_0=A^4,
Fbar_1=A^2,
Fbar_2=(1+A^2*Zbar)/4,
Fbar_3=(Zbar+A*Tbar)/8,

Zbar=Z/nu^2,       Tbar=T/nu^3.                        (6)
```

So (6) is exactly the reviewed fixed prefix in the local coefficient ring.

The normalization also intertwines the complete characteristic recurrence.
For `y=F^beta`,

```text
n*A^4*y_n
 = sum_i (((beta+1)i-n) F_i y_(n-i)).                  (7)
```

Every summand of (7) is multiplied by
`nu^-i nu^-(n-i)=nu^-n`.  For the mode at `m`, the extra factor
`cbar_m=nu^-m c_m` times the coefficient at `n-m` again gives exactly
`nu^-n`.  Therefore

```text
gbar_n=nu^-n g_n                                       (8)
```

for the full nine-mode schedule, not merely for the principal branch.
Because `nu` is a unit, `gbar_n` is regular at `alpha` if and only if `g_n`
is regular there.

There is one important firewall: (5) is **not** asserted to be a symmetry of
the raw determinant equation or of the global `X`-degree windows.  The
coefficients `cbar_m` are local functions, not global scalar modes.  That
does not matter here.  The reviewed fixed cascade from D7 through D21 uses
only algebraic fractional-power recurrence, regularity of `G_n`, and
`A`-adic divisibility.  It never differentiates `cbar_m`.  When a scalar
mode must be killed, `c_m=0` or `cbar_m` is a local unit, so the same unique
lowest-pole argument applies.  The positive modes such as `c16` are simply
carried as local coefficients in the same relations.

## 3. Why no global quotient object is needed

The apparent obstruction in the SRT proposal was that the reviewed proof
names global polynomial quotients (`R,Q,T,Y,M,N,O,P,S,U`).  In the proof,
however, each name is introduced only after a numerator is shown divisible
by the relevant power of `A`.  In the DVR these are ordinary local
quotients.  No value at a second root is used.

The local ladder is therefore the same one:

1. D7--D15 alternately complete a square, force the square defect into
   `(A)`, then force its quotient into `(A)`; the unique polar modes
   `c6,c10,c14` are killed at their reviewed rows.
2. D16 and D17 introduce local quotients `M,N` through the centered quadratic
   relation and its successor.  No square-root sheet is selected.
3. D18--D21 introduce `O,P,S,U`; `c18` and `c20` are units if nonzero and
   are killed by their strictly deepest poles.  Their linked successor
   cancellations are irrelevant after the preceding regularity row.
   The literal raw windows at these rows have dimensions `5,3,2,1` and
   consist of polynomial `G18,G19,G20,G21` coefficients.  Hence they supply
   exactly the local regularity used here; their special global degrees and
   rank labels are not otherwise invoked.
4. After D21 the complete auxiliary characteristic coefficient has no term
   below `A^-2`:

   ```text
   gbar_22 = qbar + Wbar/A^2.                           (9)
   ```

Multiplying (9) by the unit `nu^22` returns to the original characteristic
coefficient and preserves its order:

```text
g22=nu^22*gbar_22,       ord_alpha(g22)>=-2.            (10)
```

This localizes precisely the reviewed characteristic part of the fixed
theorem.  It does not import the fixed packet's special low-`X` equations,
literal root labels, or 513-row rank census; those are additional global
constraints and are not needed for (10).

## 4. Endpoint calculation in the original coordinates

Return to the original raw determinant coordinates; this avoids any false
claim that (5) preserves the determinant row.  The universal same-row
identity with absent raw `G22` is

```text
D22_raw=-L22(g22),
L22(R)=-40*A^3*A'*R-8*A^4*R'.                          (11)
```

If a Laurent term has `A`-order `k>=-2`, each summand in (11) has order at
least `k+3>=1`; differentiation can lower order by at most one.  Thus (10)
implies `D22_raw` vanishes at `alpha`.

The optional homogeneous term is harmless by an exact cancellation:

```text
L22(c22*A^-5)
 = -40*c22*A^-2*A' + 40*c22*A^-2*A' = 0.              (12)
```

Equations (10)--(12) contradict the unit target `D22=1` at one root.  This
proves the unit-root transport theorem.

Two live mutations guard the new bridge.  Replacing the mode scaling
`cbar_m=nu^-m*c_m` by `nu^(-(m-1))*c_m` fails all 99 causal mode/weight
checks through weight 22: the total factor becomes `nu^(-(n-1))`, not
`nu^-n`.  Replacing the `-40` in `L22` by `-39` leaves residual scalar `1`
on `c22*A^-5`, destroying the optional-kernel cancellation.

## 5. Independent mixed-root check

The known proper-divisor prefix with

```text
A=X^4-1, C=X-1, B=1+X+X^2+X^3
```

dies at D12.  The new checker independently re-evaluates the serialized
Bezout certificate and obtains

```text
gcd(B,V0)=gcd(B,Nred)=gcd(B,B')=1,
g12_polar=Nred/(12*C^3*B^2).
```

Thus every one of the three `B`-roots is a simple `V0`-unit root with an
exact order-two pole, independently of the `C`-root.  At the rational root
`alpha=-1`,

```text
A'(alpha)=-4,  V0(alpha)=8,  C(alpha)=-2,
H(0,s)=(16+4s)^2,
Nred(alpha)=-3969/4096 != 0.
```

So the concrete D12 death is an honest early instance of the theorem's local
mechanism, not evidence for a hidden global coupling.

## 6. Scope and consequences

The exact source theorem for the imported cascade is the recursively pinned
packet

```text
cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/
  verify_uniform_d18_d22.py
    sha256 49d1acaf1a8b066e9de15005e97ce948b8b33bd38315a1e77dcdf945c9b9761d
  RESULT.json
    sha256 f46d7afd8b4e1e7cb5c60b029f8660dc2f1bf0e8770724808a3451c8c4e9e684
```

with the different-model 289/289 hostile review
`a294cdf70f0496b360855b1b88e6f362e752e0bda33498902eb6fba7785e23a5`.
That final checker recursively pins the complete reviewed prefix through
D17; the present checker pins these bytes and does not silently substitute a
summary theorem.

Promotable after hostile review:

- the exact `epsilon^2` model (1)--(4);
- coefficientwise local normalization (5)--(8);
- localization of the reviewed characteristic cascade and the endpoint
  contradiction at a single `V0`-unit root;
- hence endpoint emptiness of every `C != A` stratum under the named branch-P
  hypotheses, without q1 and without the D9 repair.

Not claimed:

- any statement about the deep `A|V0` stratum;
- preservation of raw global windows under (5);
- a new raw-normal-form compiler or a landing/coverage theorem;
- scheme-theoretic emptiness, a Keller-pair theorem, or JC2.

The next mathematical target is therefore sharply reduced: analyze the deep
`A|V0` branch directly.  For q1 this is the active one-parameter component
`V0=3*lambda*A*A'`, with `c2,c6` retained.  The proper-divisor `W` fanout is
no longer needed for full endpoint exclusion, although D9/D12 remain useful
early-row information.

## Replay

```bash
cd cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828
python3 -B verify_unit_root_transport.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

The checker uses only the Python standard library and exact `Fraction`
arithmetic.  It verifies all pinned inputs, three nontrivial exact Newton
identities, recurrence and mode scaling through weight 22, the forced-mode
valuation table, the endpoint order/kernel calculation, and the mixed-root
D12 Bezout certificate.
