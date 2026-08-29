# Type-(2,3) weight-at-atypical surrogate: coordinator integration

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: `PROMOTED EXACT LOCAL-ANALYTIC CONTROL / NO ACTUAL-MAP CLAIM`

## Binding verdict

Promote the exact local-analytic control below, with the review's tube,
wording, attribution, and forced-branch repairs folded in.  Its purpose is a
dependency test: pointwise analytic geometry at one boundary interface does
not by itself force positive profile excess.  It is not a polynomial or
rational pair, its comparison profile is not an actual Section-7 quotient
weight, and it proves or refutes nothing about actual polynomial Keller maps,
PCB, QCS, or JC2.

## Evidence

The Sol producer is
`xmodel/weight-at-atypical-local-countermodel-sol56-20260829.md`, full
SHA-256
`84afec54eb1f915ccb474a60ff72b1145ae4ffa7997a329fa8076dcbf59ea479`,
body SHA-256
`80b6fd58a0a141ec1a395c064c92bd2f7e206aa9eec9af15aea285aa69c6e350`.

Fable 5 independently reconstructed all displayed identities in
`xmodel/weight-at-atypical-analytic-surrogate-hostile-review-fable5-20260829.md`,
full SHA-256
`28e22f20da290adbceff2edd508b75ef498ed6723d1e93616b5ebf3fad8f2104`,
body SHA-256
`cf1ba18a699de9f9107b86ec8fe253e867f762a52e6c8f821832683efd460011`.
All eight attack items are `CONFIRMED`; the verdict is `PASS_WITH_REPAIRS`
at the declared surrogate tier.

## Maximum exact control

In the boundary chart

```text
x=t*s^3,       y=s^-1,
R=sqrt(1+3s^2/2),       A=(2/3)(R-1),
f=t^2+A,       g=t^3+tR,
```

take the branch `R(0)=1` on `|s|<sqrt(2/3)`.  Then exactly

```text
dx^dy=s ds^dt=df^dg.
```

On the boundary `s=0`, the residual map is

```text
(P,Q)=(z^2,z^3+z),       Q^2=P(P+1)^2.
```

It has normalized degree ratio `2:3` and one transverse node at `(-1,0)`,
with distinct source parameters `z=+i,-i`; equal target values do not merge
the source clusters.  The point `(s,t)=(0,0)` is a Morse point of `f`, the
central fibre has two normalized branches and local Milnor number one, and
the local `g`-degrees there are `1+1`.  At every `z!=0`, including `z=+-i`,
the singleton local `g`-degree is two.  Thus the formal comparison data

```text
(u,kappa^-,kappa^+)=(3,1,1),       b^+=2
```

support the constant analytic profile `w_an=2`, so
`I_an=integral_A1 w_an dchi_c=2=b^+`: the profile excess is zero despite the
Morse cycle, quotient collision, nonlinear `Q`, and `2:3` residual type.

Proper-tube conservation, asserted but undisplayed by the producer, holds
exactly.  On `f=a`, put

```text
h_a=a+(R+2)/3,
g=t*h_a,
Phi_a=(a-A)h_a^2.
```

Then

```text
Phi_a'=-s*h_a,
Phi_a(0)=a(a+1)^2,
Phi_a''(0)=-(a+1).
```

The proper local `g`-tube degree is therefore constantly two.  For `a!=0`
the two index-two punctures lie over the distinct moving values
`+-sqrt(a)(a+1)`; at `a=0` they specialize to the two node branches of
degrees `1+1`.

The nonrational square root is not an arbitrary defect of the construction.
Within the ansatz

```text
f=t^2+a(s),       g=t^3+t*r(s),
```

the Jacobian identity forces

```text
r(s)^2=r(0)^2+3s^2/2.
```

The residual `(z^2,z^3+z)` forces `r(0)=1`, hence
`r^2=1+3s^2/2`, which is not a square in `C(s)`.  Thus single-valued
rational/polynomial origin is exactly the hypothesis this natural
pointwise control cannot satisfy.

## Repaired inference and successor

The safe inference is restricted to analytic germs at one boundary
interface: exact local Jacobian-one geometry, the cluster/local-degree rule,
proper-tube conservation, a boundary collision, one local Milnor cycle and
its monodromy, and residual type `2:3` are jointly insufficient to force even
one unit of analytic-profile excess.  A valid actual-map proof must consume
single-valued rational/polynomial origin or a simultaneous multi-component/
global identity.  This does not quantify over arguments using those missing
hypotheses.

The cheapest positive successor is the polynomial-origin collision gate
`STRICT-COLLIDE-POLY` recorded in the QCS integration: prove or falsify
strict excess at a quotient collision using actual source-compatible
polynomial-origin data.  Constructing another analytic surrogate does not
advance that gate.

The phrase “Chau-compatible” in the producer is treated only as informal
motivation; the promoted content is the exact normalized `2:3` residual
ratio and carries no external attribution.

## Scope

This is an exact holomorphic/algebraic-over-`C(x,y)` boundary surrogate,
neither a polynomial nor rational affine pair.  It supplies no actual
Eggers--Wall realization, quotient-line bijection, `d-N` pushforward,
globally atypical value, map, counterexample, or JC2 conclusion.  Formal
comparison data are not a map, and local zero excess is not an attained
global configuration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4825`.
- Body SHA-256:
  `24675cfe3a07aa9cd05a46fc4842b32f0b86ddf1d322ac9731dfe19bed3eb8ad`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
