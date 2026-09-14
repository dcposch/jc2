# Monomial-Jacobian Euler interface: first coordinate arrow refuted

2026-09-06; desk `model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

**Verdict: the proposed direct port is invalid, with exact controls.**
The task premise that `t=1/gamma` constantizes `J=c gamma^2` has the
Jacobian factor reversed. Correct constantization is Puiseux, and the
ordinary Euler conclusion already fails for an explicit polynomial
receiver with Jacobian `-2 gamma^2`. This refutes those specific arrows,
not every possible support theorem for monomial Jacobians. No receiver
or source exclusion follows; stop this composition pass here.

## 1. Licensed client and frozen read scope

Read the complete terminal `xmodel/row2515-order-gate-sol56-20260903.md`,
SHA-256 `f1766b7c59c03387447fa0b599d79ef05935a0a5c373ff17c8e4020592bd67fb`.
It accepts the descent from the `(125,75;M2=105)` skeleton with
`u_s=1,v_s=4` to polynomial receivers in `K[gamma,pi]` with

```text
(n',m';M2',V2';k)=(25,15;21,2;2),
[P,Q]_(gamma,pi)=c gamma^2, c!=0,
```

up to the explicitly declared ordering/sign of the two components.
Its failed sparse chart is NOT a necessary full coefficient space:
`OPEN[FULL-ORDER-BASIS]` remains, independently of the present argument.

Read the source/license discussion through §§1–4.1 of terminal
`xmodel/topface-license-sol56-20260903.md`, SHA-256
`53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae`.
It records Moh Proposition 6.3's actual polynomial ring and exponent
`gamma^(v_s-u_s-1)`, and Proposition 6.4's license when u_s=1. Thus the
positive exponent here is not a notation choice for `gamma^-2`.
No unproved prefix basis, fixed root partition, or inverse-minor rule
is added to that client.

Re-read GGV1 Theorem 2.6's complete proof and Lemma 2.2, in the primary
`box/census-coverage-20260905/core-ggv-layout.txt`, SHA-256
`e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1`.
Its ordinary polynomial clause requires P,Q in `K[x,y]` and an ordinary
constant nonzero Jacobian. The general clause supplies E only in
`L^(l)=K[x^(1/l),x^(-1/l),y]`. Those are different hypotheses/rings.
The full endpoint conventions and notes [4]–[5] were already read in
the preceding task; no live D108/D125 review is consumed here.

History check used only final `.md` reports with sibling DONE receipts,
searching Euler with Laurent/monomial/gamma and Theorem 2.6. The K16
Laurent/Euler hits concern their coefficient spine, not a proof of this
constantization or a polynomial-E port for the present receivers.
The row gate itself retains missing monomial-J Laurent anchors. No
novelty claim is made for the elementary chain rule or counter-control.

## 2. The first arrow fails by the ordinary chain rule

Use throughout `[f,g]_(x,y)=f_x g_y-f_y g_x`. If
`[P,Q]_(gamma,pi)=c gamma^k` and

```text
P_hat(t,pi)=P(t^-1,pi), Q_hat(t,pi)=Q(t^-1,pi),
```

then

```text
[P_hat,Q_hat]_(t,pi)
 = (d(t^-1)/dt) c(t^-1)^k
 = -c t^(-k-2).                                        (INV)
```

For k=2 this is `-c t^-4`, NOT `-c`. Its pole cannot be ignored by
describing the pair as Laurent. Inversion constantizes exponent k=-2,
which is not the charged receiver. Therefore Theorem 2.6 cannot be
applied to the inverted pair by the claimed constant-J hypothesis.

For k>=0, the correct algebraic constantization instead is

```text
t=gamma^(k+1),
P_bar=P(t^(1/(k+1)),pi), Q_bar=Q(t^(1/(k+1)),pi),
[P_bar,Q_bar]_(t,pi)=c/(k+1).                           (PU)
```

This is an identity in the ramified extension, with derivation
`d/dt=(1/((k+1)gamma^k))*d/dgamma`. The functions lie in
`K[t^(1/(k+1)),pi]`, generally NOT in `K[t,pi]`. They may be embedded
in GGV1's `L^(k+1)`; that licenses the Laurent theorem, not its
ordinary polynomial clause. For a direction satisfying that theorem's
positivity hypotheses, it provides E in `L^(k+1)`. Its pullback lies
in `K[gamma,gamma^-1,pi]` and obeys

```text
[E_pull,P]_(gamma,pi)=(k+1)gamma^k ell(P),
```

with the corresponding transported leading form. For original weight
`(rho,sigma)`, the transformed direction is proportional to
`((k+1)rho,sigma)`, and the pulled Euler weight is
`(k+1)rho+sigma`, not `rho+sigma`. The exceptional endpoint `(1,1)`
likewise pulls back to `(k+1,1)`.

Negative gamma powers are not excluded by the theorem; multiplying E
by a power to clear them is not harmless, since
`[gamma^N E,P]=gamma^N[E,P]+N gamma^(N-1)E P_pi`.
Even positive fractional exponents in t invalidate the old
integer-polynomial support enumeration. No polynomiality assertion
for the corrected Euler element is proved in this pass.

## 3. Same-ring counter-control to ordinary polynomial Euler import

In exactly the receiver ring `K[gamma,pi]`, set

```text
P=gamma*pi, Q=gamma^2.
[P,Q]=-2 gamma^2.
```

At ordinary weight `(1,1)`, ell(P)=P, of positive weight 2.
There is NO polynomial E with `[E,P]=P`. Indeed, term by term,

```text
[gamma^i pi^j, gamma*pi]=(i-j)gamma^i pi^j.             (DIAG)
```

The coefficient of `gamma*pi` in `[E,P]` is therefore always zero,
while in P it is one. The same proof excludes E even in the original
Laurent ring `K[gamma,gamma^-1,pi]`. In particular, no degree-2
polynomial Euler element of the kind used for D108 exists. Importing
GGV1's endpoint prohibition would also wrongly forbid this actual
receiver's endpoint `(1,1)`.

The corrected ring map is nonvacuous and consistent on this control:

```text
P_bar=t^(1/3)pi, Q_bar=t^(2/3), [P_bar,Q_bar]=-2/3,
E_bar=(3/2)t*pi, [E_bar,P_bar]=P_bar.
```

Its pullback is `(3/2)gamma^3*pi`, whose bracket with P is
`3gamma^2 P`, not P. Dividing this Euler element by 3 yields a
twisted relation `[E_twisted,P]=gamma^2 P`, precisely retaining
the extra Jacobian factor and higher Euler weight.

This receiver is NOT asserted to have degrees 25/15, the Moh root
data, or a lift to the charged source. It refutes the unrestricted
step `polynomial monomial-J pair -> ordinary polynomial Euler element`.
It does not refute a future theorem using additional genuine client
hypotheses. The first proposed coordinate arrow is REFUTED; a suitably
restricted corrected support theorem remains GAP, not a blanket no-go.

## 4. Tiny controls and terminal scope

`box/monomial-jacobian-euler-20260906/check.py` implements exact
two-variable Laurent/Puiseux differentiation using only Fractions and
finite dictionaries. It checks the receiver bracket, inversion and
rejection of its false constant value, corrected Puiseux bracket,
Euler identity, pulled/twisted Euler factors, and diagonal control.
The proof of (DIAG) is termwise for all exponents; finite checker
instances are only arithmetic controls, not a completeness argument.
Explicit exceptions, not assertions, enforce checks under `python -O`.
The script has 25-second CPU and 512-MiB address-space caps.
Its SHA-256 is
`54414d0231504b7ca90c03620b0c9d99833cc4e0373de393dcc6b09c66a85738`.
Normal and optimized runs each returned nine PASS markers and
`ALL_EXACT_CONTROLS_PASS`; both processes exited normally.

No AWS, CAS package, solver, external literature sweep, live peer body,
shared ledger, or `jc2-lean` access. No monomial-J receiver or source
exclusion is claimed. All owned work is terminal before publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7259`.
- Body SHA-256:
  `4d417700ce5b8fdaa144ba0f1db86b03f8c6ca95c933eff3a89655cc94395cdf`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
