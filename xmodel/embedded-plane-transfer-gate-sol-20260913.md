# Embedded-plane transfer — different-model FIRST

Sol, September 13, 2026. MANUAL / DIFFERENT-MODEL FIRST. Scope is exactly the frozen producer's fiber bound and embedded-source/full-output-factorization obstruction. The accepted complex plane Keller mapping-degree-at-most-three theorem is consumed without reproof. No claim about arbitrary output projections, noninjective parametrizations, the ambient symplectic proof, or JC2 is made.

## Verdicts

- **All-fiber cubic bound: CONFIRMED.** This includes `r=0`, `x=0`, repeated roots, and the displayed sharp fiber.
- **Embedded-source factorization implication: CONFIRMED.** Injectivity of `j` is exactly what transfers the ambient fiber bound to `h`; injectivity of `i` is unnecessary.
- **Canonical `{R=r,D=d}` fiber description and restricted map: CONFIRMED.** It obstructs this literal canonical slicing mechanism, not arbitrary projections.
- **Long four-dimensional attachment: CONFIRMED CONDITIONAL ON THE CITED EXPLICIT SOURCE DATA.** The polynomial source-coordinate inverse and equation (54) factorization were checked at the targeted primary-text tier. The paper's symplectic calculation was not audited and is not needed for the conditional fiber-count transfer.

## Independent cubic calculation

Put `w=1+xy`, `a=2-3xy-x^2 b`, and, on `x!=0`, `v=w/x`. Direct expansion gives

```
R=xa,
S=x^-1(2+4w-3aw^2),
T=(aw^3-w^2-w)/(2x^2).
```

For a target `(r,t,s)`, substitute `a=r/x`, `w=xv`:

```
s=2/x+4v-3rv^2,
2t=rv^3-v^2-v/x.
```

Eliminating `1/x` yields

```
p(v)=rv^3-2v^2+sv+4t=0,
p'(v)=3rv^2-4v+s=2/x.
```

Thus an actual `x!=0` preimage determines a root with `p'(v)!=0`, and conversely such a root reconstructs uniquely
`x=2/p'(v)`, `y=v-1/x`, and `b=(2-3xy-r/x)/x^2`. There are at most three such points if `r!=0`; if `r=0`, the fixed `-2v^2` term makes `p` genuinely quadratic, so there are at most two. For `x=0`, necessarily `r=0`; the original formulas give uniquely `y=s`, `b=-2t-4s^2`. Hence the total is always at most three. A repeated root has `p'=0` and corresponds to no finite `x!=0` point, so multiplicity cannot hide a component.

For `(r,t,s)=(0,1/8,0)`, `p=-2v^2+1/2`. Its roots reconstruct `(-1,3/2,13/2)` and `(1,-3/2,13/2)`; the `x=0` branch is `(0,0,-1/4)`. This confirms sharpness and all three substitutions.

## Transfer and canonical-fiber attacks

If `Phi j=i h`, then for fixed `z`, distinct points of `h^-1(z)` have distinct `j`-images, all in `Phi^-1(i(z))`. Therefore every fiber of `h` has cardinality at most three. A plane Keller map is dominant and generically finite; its generic fibers are reduced in characteristic zero, so its field degree is at most three. The accepted low-sheet theorem then gives automorphy. Mere projection of `Phi j` supplies no such injection into a full ambient fiber, and noninjective `j` destroys the count; the producer correctly excludes both.

In polynomial source coordinates `(x,y,b,D)`, fixing `(R,D)=(r,d)` leaves `x(2-3xy-x^2b)=r`. If `r!=0`, `x` is a unit and solving for `b` gives `G_m x A1`. If `r=0`, the ideals `(x)` and `(2-3xy-x^2b)` are comaximal because
`1=(2-3xy-x^2b)/2+x(3y+xb)/2`; hence the fiber is the disjoint union of the `x=0` copy of `A2` and another `G_m x A1`. Any map from `A2` to `G_m x A1` has constant first coordinate because the only units of `C[u,v]` are constants, so it is not dominant. On `x=0`, `(T,S)=(-(b+4y^2)/2,y)` has inverse `y=S`, `b=-2T-4S^2`. The claimed direct obstruction is therefore correct.

## Primary source attachment and scope

Primary HTML read: Long, arXiv:2608.23777v1, retrieved 2026-09-13, title/date/TOC; equations (12)-(13); Section 4 equations (21)-(26) and the inverse proof passages; Section 6 equation (54) and its immediate explanation. The source sets `Q=y+x b/3`, `A=1-3xQ`, `C=(1+3xQ)/2`, `M=b+9Q^2` and solves

```
M=3x^2 p+2Az,  D0=Cp-3Q^2z.
```

The coefficient determinant is `-9x^2Q^2-2AC=-1`, giving exactly
`p=3Q^2M+2AD0`, `z=CM-3x^2D0`; substitution recovers `q=Q`, `b=M-9Q^2`, and `D0`. The later `D=D0+H(x,y,b)` is triangular. This manually confirms the polynomial source-coordinate inverse. Equation (54) states literally `Phi_pt=sigma o (G x id) o Psi`, with `sigma` swapping the final two outputs. Consequently the four-dimensional fiber bound follows from this cited polynomial factorization, while remaining conditional on those explicit source formulas rather than on an independent whole-paper/symplectic audit.

No blocker was found. The correct stopping decision is the producer's narrow one: this embedded-source/full-output-factorization route is closed, while arbitrary projections and noninjective sources remain outside the claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4686`.
- Body SHA-256:
  `e4bf760b226a49819b0b487f21fa6144167f1db1b4a6dd50476dc90edcd7fce7`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
