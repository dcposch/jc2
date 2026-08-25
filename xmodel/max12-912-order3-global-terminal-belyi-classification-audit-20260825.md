# Whole-order-three terminal Belyi classification — scope-promotion audit

Date: 2026-08-25  
Status: **EXACT TEXTUAL COMPOSITION; HOSTILE REVIEW REQUIRED BEFORE PROMOTION**

## Result

Let an actual characteristic-zero `(9,12)` partial-`y` Keller trajectory lie
on the nontrivial order-three Kummer branch.  Write

```text
K=C(x),       L=K(u),       u^3=h in C[x],
sigma(u)=zeta*u,            h not a cube in C(x),
3 | deg(h),                 j in C^*.
```

The reviewed universal Faber theorem and order-three covariance give

```text
9*r8'=j/u,                  sigma(r8)=zeta^2*r8.
```

Then

```text
T:=r8^3 in C(x)
```

is nonconstant and satisfies the exact identity

```text
h=(j^3/27)*T^2/(T')^3.                              (1.1)
```

Consequently every actual order-three trajectory—not only a selected-Q8
trajectory—has the terminal Belyi classification already proved for the
selected branch:

1. writing `T=A/B` in lowest terms and `W=A'B-AB'`,

   ```text
   h=(j^3/27)*A^2*B^4/W^3;                          (1.2)
   ```

2. polynomiality of `h` is equivalent to every finite zero of `W` lying in
   `supp(A*B)` and every `A`-root having multiplicity at most three;
3. the universal hypotheses `3|deg(h)` and `h` noncube eliminate both
   unequal-degree strata;
4. hence `deg(A)=deg(B)=D`, and after scaling
   `lambda=T(infinity)` to one, `T:P1->P1` is a three-value Belyi map with

   ```text
   over 0:         (alpha_1,...,alpha_r), alpha_i<=3,
   over infinity:  (beta_1,...,beta_s),
   over 1:         (e,1^(D-e)),
   r+s=e+1,        deg(h)=3(e+1),
   ```

   and these entries saturate Riemann--Hurwitz `2D-2`.

This is a necessary classification.  The cyclic `D=1,2` rows remain exact
noncube terminal positive controls, so the theorem by itself excludes no
trajectory.

## Direct universal derivation

The covariance has no selected-Q8 input.  The order-three Faber tail has
geometric weight `wt(r_l)=12+l`, hence `r8` has character `20=2 mod 3` and
can be written `r8=u^2 R`, `R in K`.  Therefore `T=r8^3=u^6 R^3=h^2 R^3`
lies in `K`.

The terminal row gives

```text
T'=3*r8^2*r8'=(j/3)*r8^2/u=(j/3)*h*R^2.
```

Since `T^2=h^4 R^6` and `(T')^3=(j^3/27)h^3 R^6`, equation (1.1) follows.
The same calculation shows `T'` is nonzero: `r8` cannot be the zero function
because `9r8'=j/u!=0`.  Thus the zero-solution defect found in the selected
terminal report is automatically absent, without a Q8 contact or a
`nu!=0` load.

Equivalently, `S=r8^9=T^3 in K` satisfies

```text
h^3*(S')^9=j^9*S^8,
```

but the direct cube `T=r8^3` is stronger and avoids re-proving the divisor
cube from the ninth-power equation.

## Parent and duplicate audit

The composition consumes only:

| Parent | SHA-256 | Licensed role |
|---|---|---|
| maximum-12 Kummer preflight | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | `h in C[x]`, exact order-three class, `3|deg h`, noncube |
| preflight `CONFIRMED` review | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` | source/Kummer audit |
| universal Faber theorem | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` | terminal row and tail covariance |
| Faber `CONFIRMED` review | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` | independent formal-Laurent verification |
| selected terminal classification | `5d8806db54eb2056dd7aafe6fb7dc342c68be1bef7cba06b96beeeaa765273fc` | divisor, infinity, and passport argument |
| terminal `CONFIRMED` review | `713e41def64d0fc313d254cae5d660e412f5ba9b69bd4d7c0e6c212a4688c52b` | independent audit of every classification step |
| terminal nondegeneracy erratum | `0221a683fc88daeb162d84096e94200989dd3853d3f319455bf13f4e1dd93b1f` | excludes the formal zero solution |

Repository search found no prior whole-order-three promotion.  The only
duplicate is the selected-Q8 terminal classification itself.  Its proof
after the terminal identity uses no Q8 coordinate, no `k=mu=0`, no `nu`, and
no selected component; those hypotheses were merely the historical route to
the identity.  Here the universal Faber terminal row supplies that identity
before any load or coefficient-component choice.

The constant in (1.1) is fixed by `j`, rather than the rescaled
`nu^10` constant in the selected report.  This changes no divisor,
polynomiality, infinity, or passport conclusion.

## What is genuinely new and what remains charged

This is the first nonduplicate consequence of the FT2/Faber audit: it
globalizes a **terminal necessary classification** from one selected Q8
component to the entire nontrivial order-three `(9,12)` cell.  It does not
add a high row or classify a coefficient fibre.

For each balanced passport, an actual trajectory must still:

1. realize the complete lower fibre
   `r1=r2=r4=r5=r7=0`, `r3=mu`, `r6=nu` with its Faber constant `k`;
2. satisfy the original terminal row, not only the Belyi consequence;
3. reconstruct all coefficient functions and both Taylor polynomiality
   families at the true center;
4. retain every finite/projective boundary and coprimality condition.

Thus the next honest gate is a passport-versus-Taylor realization test on
the full order-three lower fibre, split by `(k,mu,nu)`.  The selected-Q8
positive-genus theorem handles one component only; this universal terminal
classification supplies a common target for the remaining components.

## Firewall

No claim is made for the order-one `(9,12)` leaf, either `(8,12)` Kummer
leaf, a formal coefficient point not lying on an actual trajectory, or a
map over a field of positive characteristic.  This report proves no passport
is realized, no passport is impossible, no Taylor family is polynomial, no
trajectory exists or is excluded, no maximum-12 theorem, no counterexample,
and no JC2 result.  No computation was run for this composition.
