# Exact replay: GGHV (5.9) and Proposition 5.4

Status: **PRODUCER-CHECKED, EXACT, finite classical-proof instrument only**. No full source-map/reduction-chain validation, new JC2 proof, open-frontier claim, or ideal solve is asserted. All calculations below are characteristic-zero rational polynomial identities; the eliminant certificate itself has integer coefficients.

Primary source read directly: Guccione–Guccione–Horruitiner–Valqui, *Increasing the degree of a possible counterexample to the Jacobian Conjecture from 100 to 108*, [arXiv:2204.14178v1](https://arxiv.org/pdf/2204.14178v1), Section 5, printed pp. 14–20. Printed pp. 17–18 were additionally inspected as rendered PDF pages, not solely extracted text.

Pinned local PDF: `box/ideation-20260906T1210Z/ggvh-2204.14178v1.pdf`, SHA256 `ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd`; text SHA256 `f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368`. No live blind submission or live gate was read.

## Typed verdicts

| Target | Producer verdict | Exact evidence / boundary |
|---|---|---|
| Nine displayed coefficient equations on p. 18 | CONFIRMED | Independent Laurent multiplication agrees coefficient by coefficient, assuming the stated monic cubic with zero x² coefficient. |
| Displayed consequence (5.9) | CONFIRMED | Explicit identity in the ideal of the original nine equations; no parameter division or saturation. |
| Proposition 5.4 scalar f1 | CONFIRMED | Both the displayed differential equation and its pre-cancellation identity hold exactly; polynomial uniqueness proved below. |
| g quartic and f=y(y+1)g separability | CONFIRMED | A two-term polynomial Bezout identity, nonzero endpoint values, and exact degrees. |
| Printed substitution x→x−D2 removes the x² term | REFUTED LITERALLY; LOCALLY REPAIRABLE | The coefficient becomes −2D2. The required substitution is x→x−D2/3. This nearby typo is separate from the two confirmed target identities. |
| Entire Section 5 / Theorem 2.1 applicability chain | NOT AUDITED HERE | Upstream normal forms, polygon reductions, valuation transports, and all other proof steps remain outside this bounded instrument. |

## Finite elimination with no saturation

Use the exact abbreviations

`a=d1, b=d0, c=d−1, u=d−2, v=d−3, w=d−4, z=d−5, t=d−6, k=d−7, l=d−8, m=d−10, T=C3^23 F−4`.

Work first in the polynomial ring `Q[a,b,c,u,v,w,z,t,k,l,m,T]`. Let e1,…,e6 be the coefficients of `Dtilde²` at x powers −1,−2,−3,−4,−5,−7, respectively. Let e7,e8,e9 be the coefficients of `Dtilde³` at −1,−2,−4, with T added to e9. Here

`Dtilde=x³+a x+b+c x^−1+u x^−2+v x^−3+w x^−4+z x^−5+t x^−6+k x^−7+l x^−8+m x^−10+...`.

The omitted d−9 cannot reach a selected square coefficient; for the −4 cube coefficient it would need the absent x² term. Terms below x^−10 cannot reach any selected coefficient. Thus this finite multiplication is exact, not a tail approximation. Since `Dtilde=x³(1+O(x^−2))`, `Dtilde^−1=x^−3+O(x^−5)` has no coefficients at −1,−2,−4; the lambda term does not contribute to these three Q equations. The stated remainder of x^−1 order at least five also contributes nothing.

The certificate records the nine displayed polynomials literally and compares them against independently generated square/cube convolutions. The first six equations successively give

```text
w = −bc−au
z = −c²/2−bu−av
t = −cu−bv−aw
k = −u²/2−cv−bw−az
l = −uv−cw−bz−at
m = −vw−uz−ct−bk−al.
```

Each pivot coefficient is exactly 2. These are polynomial substitutions over Q; no c, C3, F−4, or other parameter is assumed nonzero. After these substitutions, e7,e8,e9 become `(3/2)A, (3/2)B, R/2`, where

```text
A = a c²+2cv+u²
B = −b c²+2uv
R = 2T−6auv−6bcv−3bu²−3c²u.
```

Two immediate identities are

`R+3aB+3bA=2T−3c²u`, and `uA−cB=u³+a c²u+b c³`.

Set `V=4T²+6T c²u+9c⁴u²+9a c⁶`. Applying the difference-of-cubes identity gives the explicit multiplication certificate

```text
8T³+18a c⁶T+27b c⁹
 = (27c⁶u+3bV) A + (3aV−27c⁷) B + V R.
```

This is exactly (5.9), since `T³=C3^69 F−4³`. The code also lifts the identity through the six constant pivots and emits all nine multipliers Mi satisfying

`8T³+18a c⁶T+27b c⁹ = M1 e1+...+M9 e9`

as a literal identity in the **original** polynomial ring. Their term counts are `[14,9,7,5,5,4,5,5,4]`, totaling **58**. All final Mi have integer coefficients. The checker verifies the fully multiplied identity without a Groebner basis. Therefore the asserted consequence belongs to the original ideal, not only its radical or a saturation, and even the boundary c=0 is retained. The only rational divisions in deriving the certificate were fixed scalar divisions by 2 and 3; the final integer identity needs none.

This establishes the necessary consequence used in the paper. It does **not** assert that (5.9) generates the complete elimination ideal, that its vanishing reconstructs all nine variables scheme-theoretically, or that this small system equals any full Keller/source ideal. In the published application T is a polynomial because Proposition 5.4 gives `T=C3^21 f`; the ideal identity itself treats T as an independent indeterminate and needs no such substitution.

## Scalar f1, uniqueness, and squarefreeness

With `C3=y^8(y+1)`, define

```text
g = −(35−42y+54y²−81y³+243y⁴)/910,
f1 = y⁹(y+1)² g,
f = f1/C3 = y(y+1)g.
```

Exact differentiation confirms both

`6y(y+1) f1′−10(9y+8) f1 = y⁹(y+1)²`

and the pre-cancellation identity

`6C3 f1′−10C3′ f1=C3²`.

The latter verification avoids relying on division by y or y+1 at their zeroes. The polynomial solution is unique: if a nonzero polynomial r solved the homogeneous first equation and its lowest y exponent were the nonnegative integer n, its lowest coefficient would be multiplied by `6n−80`, which cannot vanish in characteristic zero. The difference of two polynomial solutions therefore vanishes.

More strongly, the quartic itself satisfies the tiny exact identity

`(−24y−26)g+(6y²+6y)g′=1`.

This is at once the reduced scalar differential equation and a Bezout certificate for `gcd(g,g′)=1`. Evaluating it at y=0 and y=−1 gives `g(0)=−1/26` and `g(−1)=−1/2`. Thus neither y nor y+1 divides g; all four roots of g in an algebraic closure are simple. Consequently f has degree six, with one simple factor y, one simple factor y+1, and four further simple roots. As an extra exact check, `disc(g)=43046721/210999880000`, which is nonzero. These conclusions extend from Q to every characteristic-zero field; no numerical root test is used.

The formula has `deg(f1)=15`, not six. It is f, not f1, that Proposition 5.4 asserts is separable of degree six; f1 deliberately has y multiplicity nine and y+1 multiplicity two.

## Nearby normalization typo

The viewed p. 18 literally prescribes `phi(x)=x−D2` immediately before declaring `Dtilde=x³+d1 x+d0+...`. Since the preceding D is monic with quadratic coefficient D2, direct expansion gives

`[x²]((x−D2)³+D2(x−D2)²)=−2D2`,

whereas replacing D2 by D2/3 in the shift makes that coefficient zero. Thus the printed shift does not justify d2=0 as written. The corrected translation is an automorphism over the same characteristic-zero polynomial coefficient ring, preserves the leading cubic coefficient, and makes the desired normalization. Terms of x^−1 order at least five remain beyond the selected coefficients under this corrected translation. This local repair is explicit; its interaction with every later valuation bound and every earlier reduction is left to the independent full-chain review.

## Replay and genuine negative controls

Artifacts: `box/ggvh99-eliminant-replay-20260906/`.

`certificate.json` is 4,593 bytes, SHA256 `a50d7f535f9d29c4909df28fd25a3c91d1103bcc70ef34bde46138338a2b3c16`. It contains all nine equations, six pivot ideal identities, the three reduced equations, the short identity, nine original-generator multipliers, and the f1/g/f/Bezout polynomials.

`replay.py` SHA256 `859cbc65eb162d3fc3cda1cfe63151c2829f112cad554baa7a61d9bcfa71aae8`; `preflight.py` SHA256 `11011a79e14611bb917721cb026d271095f4c81c24483c7767139ad55f5c0dbf`. Only standard Python plus the existing SymPy 1.12 installation was used. No packages were installed.

Read-only replay from the repository root:

```sh
python3 box/ggvh99-eliminant-replay-20260906/replay.py --verify box/ggvh99-eliminant-replay-20260906/certificate.json
```

Five damaged packets were fed into the actual checker: deleting `2d−10` from the sixth equation, reversing the sign of the eliminant's 18 coefficient, perturbing an ideal multiplier, changing the f1 denominator from 910 to 911, and reversing one quartic Bezout coefficient. All were rejected for the corresponding exact polynomial-identity failure. These are not hash-only mutations or modular controls.

Generation/check completed in 1.3054 s internally, peak 55,644 KiB; independent read-only recheck completed in 1.0889 s, peak 55,148 KiB. The preflight and both exact runs were separately capped at 60 s and 512 MiB aggregate RSS and all ended normally. The preflight used small exact resultants only to expose the structure; no Groebner or full-system solve occurred. No AWS action, large source expansion, live-report read, shared-ledger mutation, or jc2-lean edit occurred.

`custody.json` hashes all owned completed artifacts and both pinned primary files, records terminal PGIDs/caps, and declares no live arithmetic writers. The source bytes are untouched. After transactionally sealing this report, the producer yields; all task outputs are immutable and ready for root's independent replay. This instrument corroborates two bounded classical calculations; it does not substitute for the separate applicability/full-proof gate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9977`.
- Body SHA-256:
  `d28b4e0afcccb9d4e3a606f60da6fd971889a8527642d3a677901d5e80f955c8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
