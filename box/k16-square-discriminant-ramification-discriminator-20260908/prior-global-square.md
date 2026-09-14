# K16 global-square discriminator: reversible equation, no Pell termination gain

2026-09-06; desk `model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

**NO-GAIN.** The proposed nested-square identity is exactly the original
boundary equation. Its apparent Pell right side has full degree, and its
natural square-branch switch leaves the marked rational category. No
all-degree obstruction or degree-lowering transformation results. Stop
this candidate here; the `b=0, B*eta!=0` product target remains OPEN.

## 1. Search and close prior work

Searched final `.md` reports selected by sibling `.run.v2` receipts with
`final_status=DONE`; no logs, prompts, raw bodies, or live reports were
searched. Terms: exact-square, Pell, Davenport, Darboux, nested square,
and completing the square. The K16 exact-square title concerns an ideal
nilpotence exponent, not this polynomial-square construction. Broader
terminal-report hits concern different curve/dessin problems; no exact
K16 nested formula or Pell termination argument was found in this scope.

The close antecedents were read fully before this conclusion:

| report in `xmodel/` | immutable full SHA-256 |
|---|---|
| `k16-universal-series-fable5-20260905.md` | `5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb` |
| `k16-tacnode-fable5-20260905.md` | `ab1c4ca249f85f3978108fe9e26f391695805e443fdb51a6be135635b2a0fa31` |

Series §4 already treats polynomiality of a branch of the quartic in L
as an equivalent termination problem, not an additional equation.
Tacnode §3 proves failure of a second-branch polynomial involution on
`b!=0`; its §5 expressly makes no boundary claim on `b=0`. That theorem
is NOT specialized across its excluded denominator here. The elementary
branch calculation below is specific to the present normalized boundary.

Normalization and the exact target are consumed from the previously read,
reviewed `k16-boundary-product-astra-20260906.md`, SHA
`1c4a1100cc774932f23da27e11bf828a6fa10d5e256ce1528694d356d9031d9c`,
and its gate, SHA
`d40a0aefde728d22f0b4e38aaef908dd2c59408b3e0fee1631ca17b35d5e1130`.
No result from the provisional square-ramification note is consumed.

## 2. Exact polynomial hypothesis map

Work over an algebraically closed characteristic-zero field k. Normalize
`B=eta=1` with the leading coefficient of A allowed to move. To avoid the
earlier use of U for `x^3 A^2`, call that expression H in this note:

```text
H=x^3 A^2, D=(3/4)x^2 A^2,
E=2xWW'-W^2+((3/2)H-1)W-(3/16)H^2+(3/4)H+x,
V=2W+1, U=2xD/3-V=H/2-V.

K=3U^2-2V^2-1-4x-2x(V-1)V'.
K=-4E,             U+V=H/2.                             (ID)
```

This is an identity in the differential polynomial ring, not just on
solutions. A coefficient-by-coefficient check with `z=W'` independent:

| monomial | coefficient in E | coefficient in K |
|---|---:|---:|
| xWz | 2 | -8 |
| W^2 | -1 | 4 |
| HW | 3/2 | -6 |
| W | -1 | 4 |
| H^2 | -3/16 | 3/4 |
| H | 3/4 | -3 |
| x | 1 | -4 |

There are no other monomials after expansion. Conversely, polynomials
`A,U,V` satisfying `K=0` and `U+V=x^3 A^2/2` give the polynomial
`W=(V-1)/2`, and (ID) recovers E=0. No division by A, a coefficient of
A, or a polynomial in x enters this equivalence. The sign of A is kept.

For every integer `m>=4`, write `q=2m-1`, `3d^2=m`,
`p=1/[4(2d+1)]`, and `lambda=lc A!=0`. The full target becomes

```text
deg A=m-2, deg V=q, lc V=2p*lambda^2,
V(0)=-1, V'(0)=2,
U+V=(1/2)x^3 A^2, K=0.
```

Then `U(0)=1`, `U'(0)=-2`; `deg U=q` and
`lc U=(1/2-2p)lambda^2`, since `p!=1/4` for m>=4.
These are transported hypotheses/consequences, not extra restrictions.
Both roots d are retained, including both rational factors when
`m=3s^2`. No `lambda=1` or fixed original leader is imposed.

## 3. Why the global Pell/degree lever does not materialize

The proposed norm equation is

```text
3U^2-2V^2 = T_V := 1+4x+2x(V-1)V'.                     (P)
```

For a degree-q polynomial V with leader v!=0, `deg T_V=2q` and its
leader is `2q v^2!=0`. Thus (P) is not a small-remainder polynomial
approximation: the derivative term has exactly the full square degree.
At infinity it gives only `3(lc U)^2=2(q+1)v^2`. Since
`lc U/v=1/(4p)-1=2d`, this is exactly `3d^2=m`, already imposed.

Even subtracting that leading balance yields only

```text
3U^2-2(q+1)V^2
 = 1+4x-2xV'+2V(xV'-qV),       degree at most 2q-1.
```

The `2V(xV'-qV)` term retains the unknown lower coefficients and the
usual degree `2q-1` of a product of degrees q and q-1. No strict extra
degree drop has been proved. No Davenport bound is invoked without a
small-remainder hypothesis or with a different meaning of remainder.

Nor is the left side a source of nonconstant polynomial Pell units:
over k, `3a^2-2b^2=1` factors as
`(sqrt(3)a-sqrt(2)b)(sqrt(3)a+sqrt(2)b)=1` in k[x]. Each factor is a
unit, hence constant, so a,b are constant. The coefficient is constant,
not a nonsquare polynomial defining the usual nontrivial Pell cover;
and `T_V` itself changes with the unknown V. This does not rule out
other transformations, but supplies no Pell-powered degree descent.

The origin marking also diagnoses the most obvious branch switch
exactly. Holding V fixed and replacing U by -U preserves (P), but a
new A would have to satisfy

```text
A_tilde^2 = 2(V-U)/x^3 = 4V/x^3-A^2.                   (SW)
```

Because `V(0)=-1` and A is polynomial, the right side has a pole of
order exactly 3 at zero, with leading term `-4/x^3`. A rational square
has even valuation at every place. Thus **no rational A_tilde exists**.
The switch cannot act on the marked polynomial category, let alone
lower m. This is a negative control against using the other square
root as a second polynomial solution; it is not nonexistence of the
original A. Equivalently, for fixed V at most one U-sign can lift to
a rational A, up to A's own sign.

Both the origin and infinity information have therefore been used,
without producing a contradiction: the origin prevents the candidate
descent, while infinity returns the known leading equation. A new
global termination theorem would still have to forbid simultaneous
polynomiality of the two linked squares. Merely requiring those
squares to terminate is the original equation under (ID).

## 4. Terminal custody

This is the short stopped-candidate note requested, not a replacement
ideation lane. All identities above have explicit expansions or
one-place/degree proofs; no numerical sampling, finite-m solve, CAS,
external theorem, or computational certificate is used. There are no
owned jobs, PGIDs, or continuing writers after transactional sealing.
No AWS, live peer body, shared ledger, or `jc2-lean` was accessed.
Only this report and its required publication metadata were created.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6767`.
- Body SHA-256:
  `352fee7c64bbf8340e39223a903acd60f400d28f297841c85c727983ae85b7c5`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
