# TB-GERM hostile review: different-model gate

## 0. Custody and verdict

Verdict: **PROMOTE-WITH-REPAIRS**.

The theorem proof in TB sec. 3 survives hostile review. The two polynomial
identities check exactly by SymPy, the unit divisions used in L1-L3 are
accounted for under (1.3), the Weierstrass count gives
`beta_1 = 8 + 3*kappa`, and the parity claim `kappa` odd follows from the
unibranch multiplicity-2 type.

Two repairs are required before integration:

1. TB sec. 5 overstates independence. Against PRE's own dependency list, TUBE-2
   and TB-GERM share more load-bearing input than SK-5: at least the frozen
   `(8,6)` one-place infinity data and `beta_1` conversion, and the full
   representation kill also shares the constant-stratum disposal. The
   "two independent chains" language in TB sec. 5 and sec. 7 should be downgraded to
   "same gate, independently re-derived after shared row/setup inputs".
2. The sign around TB (3.3) must be stated sharply. SymPy confirms the exact
   identity is
   `27*alpha_3^2*qt = 4*sigma^2*h^3 - P^2`, not
   `P^2 - 4*sigma^2*h^3`. The latter is only valid after absorbing `-1` into
   the unspecified analytic unit in (3.4). TB line 204 says "up to sign", but
   the promotion summary must not drop that qualifier.

Frozen input hashes were verified before reading:

```text
4f464f9c7321501cf0adaacc6ad573212911d41e4589ccf47e834be709b59d6c  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kR4vX7/inputs/tb-g2-finish-opus5-20260901.md
7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kR4vX7/inputs/row-86-prebuild-opus5-20260901.md
```

Below `TB` is the frozen `tb-g2-finish-opus5-20260901.md`, and `PRE` is the
frozen `row-86-prebuild-opus5-20260901.md`. I used no external literature and
made no ledger or charged-input edit.

## 1. Section 3.1 algebra

Checked by direct SymPy expansion in
`ZZ[rho,sigma,alpha_0,alpha_1,alpha_2,alpha_3]`; this is not an eyeball check.
For

```text
a = rho + sigma*alpha_0,  b = sigma*alpha_1,
c = sigma*alpha_2,        d = sigma*alpha_3,
disc = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2,
```

SymPy gives

```text
D = -27*alpha_0^2*alpha_3^2
    +18*alpha_0*alpha_1*alpha_2*alpha_3
    -4*alpha_0*alpha_2^3
    -4*alpha_1^3*alpha_3
    +alpha_1^2*alpha_2^2

t = dD/dalpha_0
  = -54*alpha_0*alpha_3^2
    +18*alpha_1*alpha_2*alpha_3
    -4*alpha_2^3.
```

The residual for TB (3.1), displayed at TB:172-174,

```text
disc(Phi) - sigma^2*(-27*rho^2*alpha_3^2 + rho*sigma*t + sigma^2*D)
```

is the zero polynomial. All coefficients match.

The residual for TB (3.2), displayed at TB:179-181,

```text
t^2 + 108*alpha_3^2*D - 16*(alpha_2^2 - 3*alpha_1*alpha_3)^3
```

is also the zero polynomial. The coefficient-level cancellation is:

```text
t^2:
  +2916 a0^2 a3^4
  -1944 a0 a1 a2 a3^3
  +432  a0 a2^3 a3^2
  +324  a1^2 a2^2 a3^2
  -144  a1 a2^4 a3
  +16   a2^6

108*a3^2*D:
  -2916 a0^2 a3^4
  +1944 a0 a1 a2 a3^3
  -432  a0 a2^3 a3^2
  -432  a1^3 a3^3
  +108  a1^2 a2^2 a3^2

16*h^3:
  -432  a1^3 a3^3
  +432  a1^2 a2^2 a3^2
  -144  a1 a2^4 a3
  +16   a2^6.
```

The `alpha_0` terms cancel exactly, and the remaining coefficients equal
`16*h^3`.

For TB (3.3), with
`P = 27*rho*alpha_3^2 - sigma*t/2` and
`qt = -27*rho^2*alpha_3^2 + rho*sigma*t + sigma^2*D`, SymPy confirms

```text
27*alpha_3^2*qt - (4*sigma^2*h^3 - P^2) = 0,
27*alpha_3^2*qt - (P^2 - 4*sigma^2*h^3) != 0.
```

Thus TB (3.3) itself is correct, and TB (3.4) is correct as a unit-equivalence.
The exact equality in the charge summary, if promoted without "up to sign",
would be wrong.

## 2. Section 3.2 lemmas

The local ring is `R = C{y,sigma}`. After TB (1.3), displayed at TB:116-118,
`alpha_3(0,0) != 0`, `D(0,0) != 0`, `gamma = 0`, `m = 4`, and the discriminant
factor is `disc(Phi) = U*sigma^2*f` with `U` a unit. Cancelling `sigma^2` is
legitimate in the domain `R`; no localization at `sigma` is being used. Passing
from (3.3) to (3.4) divides only by the unit `27*alpha_3^2*U` and possibly by
`-1`.

L1, TB:213-216, is valid. If `h(0,0) != 0`, then `h^3` has an analytic square
root up to a unit, and

```text
P^2 - 4*sigma^2*h^3 = (P - 2*sigma*k)(P + 2*sigma*k).
```

Both factors have zero constant term because `P(0,0) = 0` and `sigma(0,0)=0`.
So `f`, which is unit-equivalent to the product by (3.4), is reducible unless
the factors are associated; in the associated case it is a unit times a square.
Both alternatives contradict the reduced irreducible `A_{beta_1-1}` germ in
TB (2.3). This also justifies the extra sentence that `h` cannot be a unit
times a square, although that extra sentence is not needed later.

L2, TB:218-228, proves smoothness rather than assuming it. Since `h(0,0)=0`,
the term `4*sigma^2*h^3` has multiplicity at least `5`. The degree-2 part of
`unit*f` is a nonzero scalar multiple of `sigma^2`, so `(lin P)^2` is a
nonzero scalar multiple of `sigma^2`. In the chosen normal form
`rho = rho(y)` and `ord_y rho = 4`, hence `rho` contributes no linear term and

```text
lin P = -(t(0,0)/2)*sigma.
```

Therefore `t(0,0) != 0` and `partial P / partial sigma (0,0) != 0`. The
coordinate change `(y,sigma) -> (y,P)` is justified by the analytic inverse
function theorem. On `S = {P=0}` the equation

```text
sigma = 54*rho*alpha_3^2/t
```

divides by the unit `t` and uses `alpha_3` as a unit, giving
`ord_y(sigma|_S) = 4`. No division by `sigma` occurs.

L3, TB:230-232, also survives. In coordinates `(y,P)`, if `h|_S` vanished
identically then `h` would be divisible by `P`. Then
`4*sigma^2*h^3` would be divisible by `P^3`, so

```text
P^2 - 4*sigma^2*h^3 = P^2 * unit,
```

contradicting reducedness of `f`. Hence `kappa = ord_y(h|_S)` is finite.
Since L1 gives `h(0,0)=0`, the finite order is at least `1`. This answers the
specific hostile concern: the order used in TB (3.6) is well-defined and not
silently infinite.

## 3. Section 3.3 Weierstrass count

The count in TB:253-275 is correct after the L2 coordinate change. In
`C{y,P}` write

```text
G = P^2 - W,      W = 4*sigma^2*h^3,
f = unit*G.
```

At `y=0`, `sigma(0,P)` has `P`-order `1` because `partial P / partial sigma`
is a unit, and `h(0,P)` has `P`-order at least `1` because `h(0,0)=0`.
Thus `ord_P W(0,P) >= 5`, so `G(0,P)` has exact `P`-order `2`. Weierstrass
preparation applies with degree two:

```text
G = u(y,P) * (P^2 + p(y)P + q(y)).
```

For a degree-two Weierstrass polynomial, completing the square gives analytic
type `A_{nu-1}` with

```text
nu = ord_y(p^2 - 4q),
```

and here `nu` must equal the known `beta_1` of TB (2.3).

The no-cancellation part checks. Write `W = w(y) + P*V(y,P)`, with
`W_1(y) = V(y,0)`. Evaluating at `P=0` gives

```text
-w = u(y,0) q,
ord_y q = ord_y w.
```

Since `ord_y(sigma|_S)=4` and `kappa = ord_y(h|_S)`,

```text
ord_y w = 2*4 + 3*kappa = 8 + 3*kappa.
```

Differentiating at `P=0`,

```text
-W_1 = u_P(y,0)q + u(y,0)p,
ord_y p >= min(ord_y W_1, ord_y q).
```

The derivative

```text
W_P = 8*sigma*sigma_P*h^3 + 12*sigma^2*h^2*h_P
```

has, along `P=0`,

```text
ord_y W_1 >= min(4 + 3*kappa, 8 + 2*kappa).
```

Therefore

```text
ord_y(p^2) >= min(8 + 6*kappa, 16 + 4*kappa, 16 + 6*kappa)
             > 8 + 3*kappa
```

for every `kappa >= 1`. Hence `p^2` cannot cancel `4q`, and

```text
beta_1 = nu = ord_y(4q) = 8 + 3*kappa.
```

The parity statement is not an extra geometric assumption. The local type is a
unibranch multiplicity-2 `A_{beta_1-1}` germ, so `gcd(2,beta_1)=1` and
`beta_1` is odd. Since `8` is even, `3*kappa = beta_1 - 8` is odd, and
`kappa` is odd.

## 4. Section 5 independence audit

TB sec. 5 claims the TB-GERM gate reproduces PRE's TUBE-2 gate with only SK-5
shared. The equality

```text
E = 14 - beta_1 = 14 - (8 + 3*kappa) = 3*(2 - kappa)
```

in TB (5.1), TB:364-366, is arithmetically correct. The independence claim
around it is not.

PRE's TUBE-2 kill chain is explicitly listed at PRE:435-443. Its load-bearing
inputs include:

```text
family-3 g=2 cabling and rho_inf = C_2(delta_4^3).iota,
e(iota) = 2*delta_aff - 29 = 14 - beta_1,
constant-stratum death,
SK-5 plus the A_4 word equation for non-constant block products,
TUBE-2 fixedness,
B_2 stabilizer = 3Z.
```

TB-GERM, by TB:236-245 and TB:277-285, uses:

```text
family-3 g=2 mixed-cover setup,
SK-5 to make L_infty the total branch component,
THEOREM TB and TB-2 to force (m,gamma) = (4,0),
the local A_{beta_1-1} infinity germ and contact 8,
the new identities (3.2)-(3.4), L1-L3, and the Weierstrass count.
```

The overlap is therefore not only SK-5. At minimum both chains share the
frozen row model:

```text
(d,n) = (8,6), g=2, one place at P_inf,
beta_1 = 32 - c, delta_aff = 21 - (beta_1-1)/2,
(Dbar . L_infty)_{P_inf} = 8, germ A_{beta_1-1}.
```

This is not cosmetic. In TUBE-2, `beta_1` is used to compute the exponent
`E = 14 - beta_1` in PRE (4.3) and PRE sec. 5, especially PRE:245-250 and
PRE:283-296. In TB-GERM, the same `beta_1` is the known type value matched
against the Weierstrass discriminant order at TB:273-275. If the row census or
`beta_1` conversion were wrong, both congruence gates could fail together.

For a full representation-level kill, there is another shared input. TB (3.6)
is stated under the non-constant block-product hypothesis, TB:236-240. To turn
the non-integrality of `kappa` into "row dead", the constant stratum must also
be disposed of. PRE lists that as SK-2 / SHAPE-KILL sec. 4.3 at PRE:439. TUBE-2
uses the same disposal. TB's sec. 7 verdict table should cite it explicitly or
state that the TB-GERM corollary is only a non-constant-stratum kill.

Conclusion for sec. 5: the theorem is still useful and the equality (5.1) is
confirmed, but the "two independent chains" and "only SK-5 shared" promotion
language is too strong. The safe replacement is:

```text
TB-GERM gives the same congruence as TUBE-2 by a different local calculation,
after shared row/setup inputs and SK-5. This corroborates the gate but is not
a second independent chain in the strict dependency sense.
```

## 5. Section 4 local witnesses

I checked TB (4.1)-(4.3) directly for the two cases used by the verdict table.
For

```text
Phi_k = ((y^4 + sigma)/27) X^3 - (sigma*y^k/3) X^2Y + sigma Y^3
```

the coefficients are

```text
rho = y^4/27, alpha_0 = 1/27, alpha_1 = -y^k/3,
alpha_2 = 0,  alpha_3 = 1.
```

SymPy gives, for `k=5`,

```text
disc(Phi_5)
  = sigma^2*(4*sigma^2*y^15 - sigma^2 - 2*sigma*y^4 - y^8)/27
  = -(sigma^2/27)*((sigma + y^4)^2 - 4*sigma^2*y^15),
D = (4*y^15 - 1)/27,
h = y^5,
P = sigma + y^4,
disc_sigma((sigma + y^4)^2 - 4*sigma^2*y^15) = 16*y^23.
```

For `k=7`,

```text
disc(Phi_7)
  = sigma^2*(4*sigma^2*y^21 - sigma^2 - 2*sigma*y^4 - y^8)/27
  = -(sigma^2/27)*((sigma + y^4)^2 - 4*sigma^2*y^21),
D = (4*y^21 - 1)/27,
h = y^7,
P = sigma + y^4,
disc_sigma((sigma + y^4)^2 - 4*sigma^2*y^21) = 16*y^29.
```

This verifies TB (4.2), TB:312-313, and the claimed germ types. The second
factor is a quadratic in `sigma` with unit leading coefficient. Its
discriminant has order `8 + 3k`; when `k` is odd, that order is odd, so the
quadratic is analytically a unibranch `A_{8+3k-1} = A_{7+3k}` germ. Thus:

```text
k = 5: 8 + 3k = 23, germ A_22.
k = 7: 8 + 3k = 29, germ A_28.
```

The other local readings also match TB:315-320 and TB:333-336:

```text
m = ord_y(rho) = 4,
gamma = ord_y(alpha_3(y,0)) = 0,
t(0,0) = -54*(1/27) = -2,
D(0,0) = -1/27,
S = {P=0} = {sigma = -y^4},
ord_y(sigma|_S) = 4,
ord_y(h|_S) = k,
F(y,0) = y^8,
partial F / partial sigma |_{sigma=0} = 2*y^4.
```

So the `A_22` and `A_28` witnesses with `m=4` are real local Miranda data in
the sense claimed. They prove local admissibility only. They do not realize a
global octic, and TB sec. 4 correctly avoids that carrier/attainment fallacy.

## 6. Sections 6-7 consequences

The `L_infty` constraints in TB sec. 6 are consistent with the earlier data, with
one caveat about wording rather than mathematics.

The first constraint, TB:394-398, is the intersection of the residual branch
with the line at infinity:

```text
Dbar irreducible degree 8, one place at P_inf,
(Dbar . L_infty)_{P_inf} = 8.
```

This is the same contact used in TB (1.1), not a separate count of three or
four physical crossings. The report keeps that distinction, which is compliant
with the FALLACY-v2 flag/place guardrail.

The second and third constraints, TB (6.1)-(6.2), follow from TB's line-bundle
bookkeeping once `k_0 = 5` and `m = 4` are accepted:

```text
3*deg Q = -k_0 - m = -9,  deg Q = -3,
deg N = -2,               deg N - 2*deg Q = 4 = m,
div(rho) = 4*P_inf on L_infty.
```

No extra row kill is hidden there. The divisor statement depends on TB step
(C)'s support assertion, quoted in TB:411-415: zeros of `rho` away from
`S_pi cap T_0` would force discriminant multiplicity at least `4` along
`T_pi - S_pi`, contradicting the total-branch multiplicity `2`.

The verdict table in TB sec. 7 follows from TB-GERM and LOC:

```text
Delta       beta_1   kappa=(beta_1-8)/3   TB-GERM result
(8,6,11)   21       13/3                  killed, non-integral
(8,6,9)    23       5                     passes, LOC k=5 gives A_22
(8,6,7)    25       17/3                  killed, non-integral
(8,6,3)    29       7                     passes, LOC k=7 gives A_28
```

The TUBE-2 column also follows from PRE (4.3):

```text
E = 14 - beta_1:
21 -> -7  killed,
23 -> -9  passes,
25 -> -11 killed,
29 -> -15 passes.
```

Thus the two gates select the same two survivors. The label
`KILLED (two independent chains)` in TB:444 and TB:446 requires the sec. 5 repair
above; the killed/pass entries themselves are arithmetically right.

For TB sec. 7.2, `(8,6,3)` has `kappa = 7`, and the LOC witness realizes the
`A_28` germ with `m=4`. Therefore TB-GERM gives no local TB kill and cannot be
used as a local backstop to the Moh route. That part is confirmed.

The sentence "has no TB backstop" should not be promoted in a broader sense.
TB sec. 7.1(2) and sec. 7.2 themselves leave a global triple-plane successor: a normal
non-cyclic triple plane with weighted branch degree `10`, one non-Gorenstein
point over the infinity crossing, and affine `A_1` points. If "TB backstop"
means that global successor, the claim is too broad. Safe wording:

```text
TB-GERM supplies no further local obstruction at P_inf for (8,6,3);
any remaining triple-cover obstruction would have to be global.
```

## 7. Repairs and fallacy audit

Required repairs for promotion:

1. **TB sec. 5 independence language.** Replace "Beyond SK-5, nothing" and the
   table phrase "two independent chains" with a dependency-qualified statement.
   The two gates share SK-5, the `(8,6)` row census, the one-place infinity
   model, and the `beta_1` values; the full representation-level kill also
   shares the constant-stratum disposal. This downgrades corroboration, not the
   theorem.
2. **TB (3.3) sign discipline.** Keep the exact identity
   `27*alpha_3^2*qt = 4*sigma^2*h^3 - P^2`. Use
   `f = unit*(P^2 - 4*sigma^2*h^3)` only after explicitly absorbing `-1` into
   the unit. Do not state `27*alpha_3^2*U*f = P^2 - 4*sigma^2*h^3` as an exact
   equality.
3. **Representation-level corollary scope.** Because TB-GERM assumes the
   non-constant block-product stratum, any "dead at representation level" line
   should cite the promoted constant-stratum kill, or else state the result as
   a non-constant-stratum kill.
4. **TB sec. 7.2 backstop wording.** Replace broad "no TB backstop" language with
   "no further local TB-GERM obstruction at `P_inf`; remaining triple-cover
   obstructions, if any, are global."

FALLACY-v2 guardrail:

```text
flag/place/series: passed; contact 8, A_{beta_1-1}, and kappa are distinct.
floor/attainment: passed; kappa equality comes from Weierstrass, not a floor.
carrier/attainment: passed for LOC; local witness is not a global octic.
variable/ring map: passed; computations are in declared local rings.
prime label/derivative: passed; eta' is a label, dD/dalpha_0 is a derivative.
sat/raw remainder: not in play.
exit price: none asserted; no charge_basis line is included.
```

Final promoted content after repairs:

```text
TB-GERM: for the non-constant mixed-cover stratum at (8,6), g=2,
beta_1 = 8 + 3*kappa with finite odd kappa >= 1. Therefore
beta_1 == 2 mod 3 is necessary. The local witnesses show A_22 and
A_28 are admissible for m=4, so the local TB-GERM gate kills only
beta_1=21 and beta_1=25 among the four row types.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16487`.
- Body SHA-256:
  `7b8f854f64c77d409c78bf9a70d090edfcc0001ec60410e1e3deea71ebdd32a4`.
- Frozen basis: `45e4c7bc5ae54713799f84d7b7faea5de6e18afd`.
