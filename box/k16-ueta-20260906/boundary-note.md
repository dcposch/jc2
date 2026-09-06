# Boundary and dependency audit (frozen-source subtask)

All source line numbers below refer to verified frozen copies in
`/tmp/jc2-lane.fImwPK/inputs/`. No mutable mathematical input was used.

## Conclusion

Xempty §7.3 does **not** prove the uniform assertion

`B eta ∈ sqrt(J_t+(b))` for every terminal index and every field factor.

It proves a correct change of finite algebras on that stratum, including the
marked triple-point removal, and explicitly leaves exclusion of the required
differential factor open. This is a concrete missing polynomial assertion,
not an omitted normalization.

## Exact source scope

* Xempty lines 90–108 define scalar-unit reconstruction and
  `S=k[c1,...,c_(t-1),b]`, `J_t=(E_2,...,E_(2t))`.
* Xempty lines 53–65 specify field factors of `3d²=t+1` and prove the
  normalizer scalars are units factorwise.
* Xempty lines 600–644 give the full, scheme-theoretically reversible map
  `L=x²C/y-b`, `P=xW-b²/4`, including both jets and leading coefficients.
* Xempty lines 848–877 handle `b=0, B eta !=0`: `Rbar=R/x³`,
  `Pbar=P/x`, `Hbar=Hdiff/x²`, with nonzero constant `Rbar(0)=-B eta`,
  and an exact isomorphism `k[x]/(Rbar) ≅ k[v]/(Q/g)`.
* Xempty lines 879–909 state why this does not establish emptiness: total
  length `4N-3` and factor lengths `2N-1,2N-2` remain consistent for every
  N, and the missing assertion is exclusion of a factor satisfying the
  linked differential formula and initial jets.
* UTAC lines 324–361 explicitly retain (BOUNDARY) as a separate unproved
  hypothesis. Its §9 does not cite a completed boundary theorem.

The other “boundary” in Xempty §§3 and 6 is the slice determinant locus
`Delta=0` (equivalently the homogeneous H locus after normalization), not
an interchangeable name for `b=0`. In particular a proof for that chart at
finitely many indices cannot supply the uniform b-zero statement.

## Polynomial form of the exact remaining boundary problem

Fix `m=t+1>=4`, one field factor `k` of `Q[d]/(3d²-m)`, and pass to an
algebraic closure for the point statement. Set `q=2m-1` and consume the
Xempty constants

```
y=(d+m)/(2q),
omega=1/(4y²(2d+1)).
```

At b=0 write `L=x²A`, `P=xW`. Then the full UF equation, divided by x²,
is exactly

```
(theta-1)(W²) + ((3/2)x³A²-B)W
  = (3/16)x⁶A⁴ -(3/4)Bx³A² -B eta x,       theta=x d/dx.       (B-UF)
```

Its marked and terminal constraints are

```
deg A=m-2,  lc A=1/y,
deg W=2m-1, lc W=omega,
W(0)=-B,   W'(0)=eta.
```

The exact missing theorem is: **there is no polynomial pair A,W satisfying
(B-UF) and these constraints with B eta nonzero, for any such m and either
factor.** This is equivalent to (BOUNDARY), because the frozen reconstruction
has only scalar-unit pivots and the change from C,W to L,P is reversible,
including at b=0. Conversely, every hypothetical boundary point produces
this full polynomial pair; there is no formal-series substitution here.

The triple-point orders follow directly from the jets: P has order one,
`Hdiff=2theta(P)-3P-Bx+(3/2)L²` has coefficient eta at x² and has order two,
and hence R has order three. Explicitly

```
Pbar=W,
Hbar=(2theta(W)-W-B)/x+(3/2)x²A²,
Rbar=(3/16)x⁵A⁴-(3/4)Bx²A²-B eta.
```

The first quotient in Hbar is polynomial since W(0)=-B. All three formulas
retain every coefficient. The boundary finite-algebra transform from the
source is

```
f(v)=4Bv²+(16B eta/3)v⁴,
g(v)=4Bv+(16B eta/3)v³,
Q/g=v²g(v) A(f(v))-1.
```

It is coprime to g and nonzero at v=0, so the inverse maps
`v=x/L(x)`, `x=f(v)` apply on the finite quotients stated above. This imposes
no contradiction on the unbounded degree m. It is not legitimate to erase
the differential definition of Hbar and count arbitrary factors instead.

Nor can a proof at b!=0 be extended by mere specialization. The b-zero
locus may contain components supported entirely in b=0. To use such an
extension one would need an additional theorem (for example an appropriate
dominance/deformation theorem), which none of these frozen inputs supplies.

A useful non-exclusion control: at b=B=eta=0 and every integer m>=2, choose
any nonzero a and either root p of

```
(4m-3)p²+(3/2)p-3/16=0.
```

Then `L=a x^m`, `P=p a² x^(2m)` solves UF with the marked jets. These are
outside B eta!=0, but show that b-zero degree balance itself must preserve
solutions of unbounded degree. They are not boundary-target counterexamples.

## Conditional dependency chain, with frozen source at every arrow

Write `r=B eta` and `I_+=(T_(t,1),...,T_(t,2t-1))`.

1. `U_eta => r ∈ sqrt(J_t:b^infinity)` by specialization of the universal
   polynomial jets to terminal reconstruction: UTAC lines 326–330;
   reversibility and the declared coefficient map are Xempty 632–644 and
   its scalar-pivot reconstruction 90–108.
2. Together with (BOUNDARY), this gives `r ∈ sqrt(J_t)` using
   `sqrt(J_t)=sqrt(J_t:b^infinity) ∩ sqrt(J_t+(b))`: UTAC 332–342.
   An elementary certificate combination verifies the implication: if
   `b^k r^u ∈ J_t` and `r^v=j+bh`, j∈J_t, then
   `r^(u+kv)=r^u(j+bh)^k ∈ J_t`. No uniform exponent is required.
3. Row-image transport takes the positive coefficient ideal to I_+ after
   the specified triangular change and high elimination: Xempty 913–924,
   with literal row identity `gy F(x)+3x(D0(x+b4)-D0(b4))=0`.
4. The target maps by `tau=-(gy/3)r mod I_+`, hence
   `r ∈ sqrt(J_t) => tau ∈ sqrt(I_+)`: Xempty 926–941. The scalar gy/3 is
   a unit by Xempty 61–65 and 934; the recorded boundary identity is
   `R_boundary=U_h'(b4)+b3 C_h(b4)=y eta/3` at 930.
5. `tau ∈ sqrt(I_+) <=> (I_+,T_(t,0))=S_t`, with
   `T_(t,0)=yg+tau`: Xempty 942, 949–956. The forward implication is the
   finite geometric-series inverse; the converse is weighted cone scaling.
   One must never put the literal constant row in `sqrt(I_+)`.
6. The unit ideal gives empty terminal normalized receiver chart, then no
   solution of the original K16 ray system, then theorem (T) at that t:
   Xempty 943–946, consuming its explicitly banked constant spine,
   normalizer, and second affine spine. UTAC 352–359 repeats this chain.

The frozen corpus supplies this last transport as a charged theorem; its
upstream proofs are not independently re-established in these seven input
files. There is no need to invent an attainment map or to consume an
uncharged ledger entry. This chain proves a whole-ray theorem only when its
two uniform hypotheses are proved at every required t and factor.

No new exit-price assertion is made, so no charge_basis line is appropriate.

## Additional whole-polynomial theorem on b=B=0

This stratum admits a complete classification by valuations, without any
truncation. Suppose L is nonzero, of actual degree m>=2. Degree balance
forces deg P=2m, and the equation is

```
P H=(3/16)L^4,   H=2xP'-3P+(3/2)L².
```

If alpha!=0 is a root of P of multiplicity s>=1, then it is a root of L
of multiplicity h>=1. At alpha the derivative term has order s-1 and the
L² term has order 2h. There are three exhaustive cases:

* If s-1<2h, then ord H=s-1, so 2s-1=4h, impossible by parity.
* If s-1>2h, then ord H=2h, so s+2h=4h and s=2h, contradicting the case.
* If s-1=2h, cancellation can only raise ord H. Then s=2h+1 and
  ord(PH)>=4h+1, contradicting ord L^4=4h.

Thus P has no nonzero root. Over the algebraic closure it is c*x^(2m)
with c!=0. Substitution and division by x^(4m) give a constant quadratic
for the rational function Z=L²/x^(2m):

```
(3/16) Z² -(3/2)c Z -(4m-3)c²=0.
```

Since k(x) is a field and k is algebraically closed, the quadratic splits
into constant factors, so Z is constant. Hence L=a*x^m and P=p*a²*x^(2m),
where a!=0 and p satisfies `(4m-3)p²+(3/2)p-3/16=0`. Conversely direct
substitution verifies every such pair. Its jets force eta=0. If L=0,
then `(theta-3)P²=0` forces P=0 by coefficient comparison, since no
integer exponent 2j equals 3. This proves the complete b=B=0 statement
and verifies all of the unbounded-degree controls above. It does not
exclude the separate B eta!=0 stratum.

On the actual remaining locus b=0, B eta!=0, reduction of Rfree modulo L
is `-B eta x³`. Therefore P and L have no common nonzero root, and their
monic gcd is exactly x. The valuation parity theorem above consequently
has no nonzero common root to which it can apply. The even quartic is

```
Q_P(x,Y)=(3/16)(Y²-L²)(Y²-S),  S=8P+4Bx-L².
```

Here `[x]S=-4B`, so S has a simple marked zero and is not a square in k(x).
The companion ±sqrt(S) branches are genuinely nonpolynomial; ±L are the
two polynomial roots supplied by the b=0 symmetry. Treating all four roots
as polynomial would be an error. This factorization is compatible with
arbitrary actual m and does not prove (BOUNDARY).

The frozen tacnode report also states the boundary scope explicitly at
lines 205–207: on b=0 its eta radical assertion is equivalent, via
`18B w_2-6eta² ∈ J_t+(b)`, to `B w_2 ∈ sqrt(J_t+(b))`, and **no claim is
made on b=0**. Thus neither its tacnode theorem nor the radical-step
finite-index certificates conceal a uniform proof of the boundary.
