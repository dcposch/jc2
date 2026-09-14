# Common4/Q centered bad-coefficient typing

Status: **TYPED PROSPECTIVE LOCALIZATION ONLY; NO SOLVE, POINT, PROPERNESS, OR UNIT CLAIM.** 2026-09-08.

## 1. Frozen source and normalized ring

The frozen pins were checked before typing. The observed SHA-256 values of `baseline.py`, `exporter.py`, and `lift-contract.md` are respectively
`ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53`,
`9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703`, and
`433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad`.
They match the retained header/manifest pins. The header is the rational `common_4` client over `Q`, with zero-based indices and global degree reverse lexicographic order in displayed variable order.

Let `a_(i,j)=[g^i p_old^j]A(g,p_old)`. Before the economical normalization, centering has the sign

`p_old=p+mu`, equivalently `p=p_old-mu`.

Thus it is the plus sign in `A(g,p+mu)` that defines the requested coefficient. For the accepted normalization, put

`A_bar(g,p_old)=mu^-15 A_raw(mu*g,mu*p_old)`,
`B_bar(g,p_old)=mu^-25 B_raw(mu*g,mu*p_old)`

with `tau=mu`. Then `mu_bar=1` and

`a_bar_(8,k)=mu^(k-7) a_raw_(8,k)`.

The simultaneously transported baseline variables are

`c=c_raw*mu^-36`, `lambda2=lambda2_raw*mu^-3`, and
`lambda3=lambda3_raw*mu^-2`.

If the old inverse of `c_raw` is denoted by `z_raw`, the retained inverse variable is correspondingly `z=z_raw*mu^36`, so its unchanged row is `z*c-1`. These are bookkeeping equalities for the accepted nonzero dilation, not a new parameterization: the 371-variable baseline contains no `mu` variable and no second gauge.

The original baseline ring is

`R=Q[98 free A coefficient names, 269 free B coefficient names, c, z, lambda2, lambda3]`.

The displayed order gives IDs `0..97` to the free A coefficients, `98..366` to the free B coefficients, `367` to `c`, `368` to the existing `z`, `369` to `lambda2`, and `370` to `lambda3`. All fixed coefficient-map records remain records rather than ring variables.

## 2. Exact coefficient projection and fixed substitutions

In the unnormalized notation the proposed coefficient is exactly

`h_raw=[g^8 p^4]A_raw(g,p+mu)`

`     =a_raw_(8,4)+5*mu*a_raw_(8,5)+15*mu^2*a_raw_(8,6)+35*mu^3*a_raw_(8,7)`.

Only `k=4,5,6,7` can contribute: `k<4` cannot supply `p^4`, while total degree at most 15 gives `8+k<=15`, hence `k<=7`. Under the accepted dilation,

`h=mu^-3*h_raw=[g^8 p^4]A_bar(g,p+1)`.

The common4/Q coefficient map fixes the total-degree-15 face to `H^3`, with
`H=p^2(p^3+g^3)`, fixes the inner A face at `g`-degree 9 to
`g^9(p-1)^6`, and fixes `A_g0_p0=0`. The four contributing map entries are:

| `k` | actual source label | total-degree check | inner-face check | source-map value |
|---:|---|---|---|---|
| 4 | `A_g8_p4` | `8+4=12<15` | `8<9` | free variable, ID 95 |
| 5 | `A_g8_p5` | `8+5=13<15` | `8<9` | free variable, ID 96 |
| 6 | `A_g8_p6` | `8+6=14<15` | `8<9` | free variable, ID 97 |
| 7 | `A_g8_p7` | `8+7=15` | `8<9` | fixed outer-face value `0`, rational wire `[[0,1],[0,1]]`; no variable ID |

The last zero follows without expanding `H^3`: every `g` exponent in a term selected from its three factors is a multiple of 3, whereas 8 is not. There is no competing inner assignment at `g`-degree 8. The other three entries are neither on the outer face, on the inner face, nor at the fixed origin. Ascending lexicographic exponent order leaves 91 free A entries before `g`-degree 8; its free entries `p^0` through `p^6` therefore have IDs `91..97`, which gives the displayed IDs.

Consequently the exact polynomial in the existing normalized ring is

`h=A_g8_p4+5*A_g8_p5+15*A_g8_p6`.

Equivalently, its unsimplified `mu=1` projection is

`A_g8_p4+5*A_g8_p5+15*A_g8_p6+35*A_g8_p7`,

with the final labeled coefficient substituted by its prescribed zero. No unsupported coefficient, fixed zero, total-degree slot, or inner-face slot has been discarded.

For the complete source map, not merely this projection, the retained factored assignments are `A_top=H^3`, `B_top=H^5`, `A_inner=g^9(p_old-1)^6`, `B_inner=g^15(p_old-1)^10`, and both target constants zero. They account for 17 fixed A entries and 27 fixed B entries, including every zero on those faces and the two zero constants. The face intersections are the original consistent assignments. Nothing here expands the degree-15/25 faces or the degree-6/10 inner powers.

## 3. Structural and ideal-theoretic status

`h` is **not structurally zero** in `R`: `A_g8_p4`, `A_g8_p5`, and `A_g8_p6` are three distinct polynomial generators, so their Q-linear combination with coefficients `1,5,15` is a nonzero element of the ambient polynomial ring.

Its licensed status is nevertheless only an **uneliminated coefficient polynomial**. No supplied accepted/source identity identifies `h` with zero, with an existing row, or with a proved redundant generator. In particular, the common-centering source names the still-missing arrow: vanishing of the remaining forbidden centered coefficients as a consequence of all Jacobian equations. It does not prove that arrow for this coefficient. The lift contract supplies the original 105 polynomiality equations but supplies no separate identity making this centered coefficient vanish.

Therefore this typing establishes neither `h` nonzero on `V(I_full)` nor `h` outside `I_full` or `sqrt(I_full)`. The three free-slot declarations prove only ambient structural nonzeroness; failure to have a membership proof would not prove nonmembership.

## 4. Licensed prospective localization

The local schema licenses the coefficient function: it supplies the exact coefficient labels/map and the mathematical source supplies the polynomial translation. That translation is used only to define `h`. It does not replace any source equation and does not transport the lift to centered coordinates.

Let `I_full` be the retained complete 816-row ideal in `R`. Append one fresh variable `z_h`, distinct from the existing `z`, after `lambda3`; its proposed zero-based ID is 371. In

`R_h=R[z_h]`

the exact prospective ideal is

`I_h=I_full*R_h + <z_h*h-1>`

`   =I_full*R_h + <z_h*(A_g8_p4+5*A_g8_p5+15*A_g8_p6)-1>`.

The appended row label is exactly `GUARD/h`. Thus the proposal has **372 variables and 817 indexed rows**. The row in IDs is

`x_371*x_95+5*x_371*x_96+15*x_371*x_97-1`.

All original data are retained literally:

- all 371 original variable names in their displayed order, followed only by `z_h`;
- all 411 A/B coefficient-map entries and all 44 fixed-assignment rows, including every fixed face and zero map;
- all 660 rows `J/I/J` for `0<=I<=23`, `0<=J`, `I+J<=38`, with `J/2/0` imposing the original sign convention `J(A,B)-c*g^2` and `J=A_g*B_p-A_p*B_g`;
- all 105 rows `LIFT/A/t/e` and `LIFT/B/t/e` for the original inverse map
  `g=v^-1, p_old=v^4*u-lambda2*v^2-lambda3*v-v^-1`;
- the six fixed-unit vertex guards and the existing scalar row `GUARD/c`, with no origin guard and no guard on either unrestricted lambda.

The count is `44+660+105+6+1+1=817`, where only the last summand is new. This is localization by `h`, not the equation `h=1`: no specialization, gauge, row deletion, graph compression, coefficient-field change, or centered-lift replacement is part of the proposal.

## 5. Acceptance and stop map

If, in a later authorized computation, this **complete** characteristic-zero ideal `I_h` were proved proper, the weak Nullstellensatz would provide a point over an algebraic closure of Q; a Q-rational point is unnecessary. The retained `z*c-1`, all 660 Jacobian rows, all 105 polynomiality rows, monic/fixed faces, and the accepted lift contract would then reconstruct a polynomial Keller pair of exact degrees 75 and 125, hence the accepted sufficient-contract counterexample.

If instead `I_h` were proved to be the unit ideal, that result would exclude only the full-source stratum `h!=0`. It would not remove `I_full`, prove the other forbidden coefficients vanish, or establish a whole-weight transfer. Neither properness nor the unit outcome is computed or claimed here.

A receiver-only or mod-p point does not meet this acceptance map. The earlier commuting face control with Jacobian zero also fails the retained nonzero-scalar source contract and cannot serve as a countercontrol for this localization. No construction, source expansion, solver, remote action, or later decision is performed here. **STOP / IDLE.**

<!-- BODY-END -->
