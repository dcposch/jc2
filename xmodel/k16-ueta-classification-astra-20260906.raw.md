**K16 whole-polynomial classification lane: the infinity balance is consistent at every degree; uniform restricted classifications and the exact remaining obstruction**

Lane `k16-ueta-classification-astra-20260906`. Frozen basis `800137c8a8f58b741abaca4cdead3b36ed7c3f30`. Date 2026-09-06. Notes and exact local drivers: `box/k16-ueta-20260906/`.

**VERDICT: OPEN for U_eta and for the stronger classification. (BOUNDARY) is also OPEN. No whole-ray theorem (T) is promoted.** The requested leading-coefficient contradiction does not occur: both leading roots are consistent for every actual degree, on every coefficient-field factor. The proved degree alternatives and restricted uniform classifications below do not reduce arbitrary L to finitely many cases. Finite exact computations are used only in their stated scopes.

Here **actual degree means `m=deg L`**, as in UTAC §8. The cubic family has `deg P=6` and `deg L=3`; it must not be counted as an actual-degree-six counterexample. The intended stronger assertion is that, after normalizing b=1, every solution is on `C_B` or `C_3`, and hence there is no solution with `deg L>=4`.

**1. Frozen custody and source conventions.**

Before reading charged mathematics, the receipt `xmodel/k16-ueta-classification-astra-20260906.run.v2` was parsed mechanically with `awk -F=`. Entries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` were paired into a manifest and piped to `sha256sum -c`. All seven returned OK. The retained manifest is `box/k16-ueta-20260906/manifest.sha256`; no hash was retyped for verification.

All source references mean verified copies in `/tmp/jc2-lane.fImwPK/inputs/`:

| short name | frozen basename |
|---|---|
| UTAC | `k16-utac-astra-20260906.md` |
| Closing | `k16-t2-closing-opus5-20260906.md` |
| Series | `k16-universal-series-fable5-20260905.md` |
| Tacnode | `k16-tacnode-fable5-20260905.md` |
| Xempty | `k16-xempty-astra-20260905.md` |
| Radical | `k16-radical-steps-grok46-20260906.md` |
| FALLACY | `FALLACY-v2.md` |

The receipt was read only. No ledger, `jc2-lean`, `ideation-*` input, fleet, external source, or mutable certificate was used. Computations reconstruct coefficients from (UF); upstream theorems are consumed only as stated in these frozen reports.

**2. The entire equation, jets, and legitimate normalizations.**

Work over an algebraically closed field k of characteristic zero for point statements; ideal statements descend factorwise to the indicated characteristic-zero coefficient field. Put `theta=x d/dx`. The complete universal equation is

```text
F(P,L) := (theta-3)(P^2) + ((3/2)L(L+b)-B*x)P
          -(3/16)L^2*(L(L+2b)-4B*x)
          +eta*x^2*(b*L/2+B*x) = 0.                         (UF)

L(0)=-b, L_1=0;
P(0)=-b^2/4, P_1=-B, P_2=eta.                              (UJ)
```

Equivalently, with

```text
H=2theta(P)-3P-B*x+(3/2)L(L+b),
R=(3/16)L^2*(L(L+2b)-4B*x)-eta*x^2*(b*L/2+B*x),
```

the equation is `P H=R`. These are polynomial identities; no series is substituted for either entire polynomial. The prime in `d/dx` denotes differentiation. P_j denotes a coefficient, not a derivative.

On b nonzero the substitution

```text
(L,P,B,eta,b) -> (L/b,P/b^2,B/b^2,eta/b^2,1)
```

divides F by b^4 and preserves every marked jet. For nonconstant L with leading coefficient A, choose alpha with `alpha^m A=1`; the substitution x -> alpha*x sends

```text
l_j -> alpha^j l_j, B -> alpha B,
eta -> alpha^2 eta, P_j -> alpha^j P_j, b -> b.
```

The Euler derivation commutes with this substitution. It gives a monic L over the algebraic closure, on every nonzero-leading-coefficient stratum. Neither substitution applies to a vanished denominator; constant L and b=0 are treated separately. These are the maps of UTAC §§2,4, derived directly from (UF).

At b=1 the two known solution families are

```text
C_B: L=-1,       P=-1/4-B*x,       eta=0;
C_3: L=-1+A*x^3, P=-L^2/4,        B=eta=0.
```

Direct substitution verifies both, including their common constant point. In general b they become `L=-b,P=-b^2/4-Bx` and `L=-b+A x^3,P=-L^2/4`. Their existence does not prove exhaustion.

**3. Every leading-degree case at infinity.**

Assume b nonzero and normalize b=1. Neither P nor L is zero because of its constant jet. Write `a=deg L`, `c=deg P`, `A=lc L`, and `C=lc P`. The complete list of potentially contributing degrees in F is

```text
2c, 2a+c, a+c, c+1, 4a, 3a, 2a+1, a+2, 3.
```

A vanished B or eta deletes terms from this list, never creates a new leader. Equal degrees among lower terms can cancel freely; the argument uses a unique leader only in the cases where it is strictly above all the others.

| case | complete degree conclusion |
|---|---|
| L=0 or P=0 | impossible from the nonzero constant jets |
| a=0, c>=2 | L=-1; `(theta-3)P^2` has the unique highest degree 2c, coefficient `(2c-3)C^2!=0`; all other degrees are at most c+1 or 3; impossible |
| a=0, c=1 | jets give `P=-1/4-Bx`, B nonzero, eta=0; this is C_B |
| a=0, c=0 | jets give B=eta=0 and P=-1/4; the common constant point |
| a=1 | excluded by L_1=0 |
| a>=2, c<2a | degree 4a is unique, with coefficient `-3A^4/16`; impossible, including c=0,1 |
| a>=2, c>2a | degree 2c is unique, with coefficient `(2c-3)C^2`; impossible |
| a>=2, c=2a | all three degree-4a terms must be added; they yield (UT) below and do cancel |

For the last case set `p=C/A^2`. Its leading equation is

```text
(4a-3)p^2+(3/2)p-3/16=0.                                  (UT)
```

Its discriminant is `3a`, nonzero; its two distinct, nonzero solutions are

```text
p=1/(4(2d+1)),                  3d^2=a.
```

The denominator cannot vanish for an integer a>=2. Thus the full top equation is consistent at **every** a>=2. In particular, setting p=-1/4 would force a=3, but there is no license to set p=-1/4 for an arbitrary solution: the constant jet is a value at zero, not the leading ratio at infinity. At a>=4 neither leading root equals -1/4, which is consistent with a hypothetical non-proportional solution.

There is no omitted cancellation of H's leading term. With A=1 it is

```text
lc H=(4m-3)p+3/2=3(2d+1)/4 != 0,
```

so `deg H=2m`. This covers both signs. Xempty §7.1, lines 670–687, already records the consistency of (UT); Series §3, lines 128–141, explains that the logarithmic residue computation returns precisely the same equation. Repeating it does not supply a second independent constraint.

**4. Every coefficient-field factor and every polynomial-range pivot.**

For each m>=2, `Q[d]/(3d^2-m)` is a quadratic field unless `m=3s^2` for an integer s>=1. In that case it is the product of the two rational fields d=s and d=-s, treated separately. In the irreducible case both embeddings into the algebraic closure are covered by an exact computation over the whole quadratic field. No convenient modular split root substitutes for either treatment.

For monic `L=-b+l2*x^2+...+l_(m-1)*x^(m-1)+x^m`, start with `P=p*x^(2m)`. The coefficient of the next P_j in row `x^(2m+j)` is

```text
A_j=2(2m+j-3)p+3/2
   =(2m+j+6d)/(2(2d+1)).
```

For j>=2 it is nonzero for every m>=2: a zero would imply `(2m+j)^2=12m`, whereas `(2m+2)^2>12m`. More strongly, for m>=4 this pivot is nonzero for **every j>=0**, since `4m^2>12m`. On a split factor m=3s^2, s>=2, the possible negative-sign resonance is `j=-6s(s-1)<0`, outside the polynomial coefficient range; the positive-sign resonance is also negative. For m=3,d=-1 only j=0 is resonant. That constant coefficient is prescribed by the jet and the remaining equation is retained, never divided out. The m=2 factors and m=3,d=1 have no polynomial-range resonance.

Rows `2m+j`, j=2m-1 down to 2, determine P_j by scalar divisions. Their eta forcing has degree at most m+2<=2m. All B forcing has degree at most 2m+1, including the B contribution through P_1. Thus these high coefficients are independent of B and eta. Set `eta_m=P_2`, prescribe `P_1=-B,P_0=-b^2/4`, and use row 2m+1. Its B pivot is

```text
-((4m-3)p+3/4)=-3d/2 != 0.
```

It determines a polynomial B_m. The remaining ideal is exactly

```text
k_m[l2,...,l_(m-1),b],
K_m=([x^4]F,...,[x^(2m)]F), after this reconstruction,
weights(l2,...,l_(m-1),b)=(m-2,...,1,m).
```

All coefficients above 2m have been killed, all rows 0–3 are identically zero with the jets, and F has degree at most 4m. Therefore vanishing of this finite list is equivalent to the **entire polynomial identity** F=0, not merely to a truncated approximation. Scalar divisions preserve the equivalence over coefficient algebras with nilpotents as well. This recovers exactly UTAC §§4,8's K_m and eta_m.

The weights assign `wt B_m=2m-1`, `wt eta_m=2m-2`, and `wt [x^k]F=4m-k`. They prove homogeneity, but leave m-1 variables and 2m-3 residual equations with m unbounded. Counting equations, or having nonzero high pivots, proves no height theorem and no bound on m. Task (B) would finish the unrestricted classification only after a further theorem reduced these surviving families to a fixed finite list. No such theorem follows here.

The complete actual-degree-two and -three classification is consumed from UTAC §4, lines 148–183: m=2 gives a unit ideal at b=1; m=3,d=1 gives a unit ideal; m=3,d=-1 has reduced locus l2=0 and reconstructs exactly C_3. Its explicit nonzero resultant on d=1 and two incompatible values of l2^3 on d=-1 retain all low-degree alternatives. Thus no low actual degree or exceptional constant pivot remains hidden in U_eta.

**5. Uniform consequences that use the whole polynomial.**

**5.1 Uniqueness and support.** For fixed L,b and a fixed leading root p, there is at most one marked tuple `(P,B,eta)` of polynomial solutions, for every m>=2. This proof and (SUPPORT) also hold at b=0. To prove this, compare two tuples and put `D=P-Q`. If `k=deg D>=2`, then k<2m and the unique top contribution in their difference has degree 2m+k and coefficient `A_k*lc D`. Parameter differences contribute only through degree 2m+1 (eta differences through m+2). Since A_k is a unit, this is impossible. Hence D has degree at most one. The constant jets agree, so `D=-deltaB*x` and `deltaeta=0`. Row 2m+1 is `-(3d/2)deltaB=0`, giving D=0 and equality of the tuples.

Let g be the gcd of the nonconstant exponents actually occurring in L. For a gth root of unity zeta, `L(zeta*x)=L(x)`, and the transformed tuple is

```text
(P(zeta*x), zeta*B, zeta^2*eta).
```

It has the same leading root because g divides m. Uniqueness forces invariance. Consequently

```text
g>=2 => B=0 and P in k[x^g];
g>=3 => eta=0.                                             (SUPPORT)
```

This proves U_eta uniformly on g>=3. A remaining U_eta counterexample has g=1 or 2; if B is nonzero, necessarily g=1. The statement includes arbitrary multiplicities and every coefficient-field factor.

**5.2 One nonconstant monomial.** Suppose `L=-b+A*x^m`, bA nonzero, m>=3. Normalize b=A=1 and put z=x^m. By (SUPPORT), B=eta=0 and

```text
P=p*z^2+q*z-1/4.
```

The five coefficients of the whole residual, in descending order, are

```text
z^4: (4m-3)p^2+(3/2)p-3/16,
z^3: 6(m-1)pq-(3/2)p+(3/2)q+3/8,
z^2: -m*p+(2m-3)q^2+(3/2)p-(3/2)q-3/8,
z^1: (3-m)q/2,
z^0: 0.
```

The first two rows give `p=1/(4(2d+1))` and `q=-1/(2(3d+2))`, where `m=3d^2`. The latter is nonzero and its denominator cannot vanish at integer m>=3. The z row forces m=3. The z^2 row excludes d=1; d=-1 gives p=-1/4,q=1/2 and every coefficient vanishes. Thus the entire one-monomial L family is classified uniformly as C_3. No lower coefficient was suppressed after this shape was assumed.

**5.3 A structured case that really reduces to exact computations.** For b nonzero there is no solution with `L=-b+A*x^j+C*x^(2j)`, C nonzero, integer j>=2. Normalize b=C=1 and put z=x^j. For j>=3, (SUPPORT) forces B=eta=0 and `P in k[z]`, of degree four. For j=2 the complete actual-degree-four exclusion in §6 applies, including eta nonzero. A=0 is the one-monomial case already excluded.

For integer j>=4, row z forces `[z]P=0`, so write

```text
L=-1+A*z+z^2, P=-1/4+v*z^2+w*z^3+h*z^4.
```

Here theta is `j*z*d/dz`. Rows 2,3,4 determine v,w,h by scalar divisions; their pivots are `-(2j-3)/2`, `-(3j-3)/2`, and `-(4j-3)/2`. Together with the row-one pivot, the only exceptional integer j>=2 is j=3. For example `v=-3A^2/(4(2j-3))`. Define Q5,Q6,Q7 by substituting this unique reconstruction in rows 5,6,7, dividing the odd rows by A (already nonzero), setting U=A^2, and taking primitive integer numerators. Only constant content is removed. The exact driver `structure-quadratic.py` constructs these polynomials in Q[j,U] directly from UF and verifies

```text
resultant_U(Q5,Q6)=-D*C1, resultant_U(Q5,Q7)=D*C2,
D=j^8*(j-1)^2*(2j-3)^6*(4j-3)^2,
C1=6272j^5-12670j^4+243j^3+7505j^2+1409j-3267,
C2=1792j^5-890j^4-8547j^3+15481j^2-11687j+3267,
resultant_j(C1,C2)=669531824097600026204667144843558912 != 0.
```

All denominators are products of the listed pivot factors. D is nonzero for integer j>=2. A common solution of the three rows would force C1=C2=0, contradicting their nonzero resultant. This necessary resultant condition remains valid when a coefficient in U vanishes; no U-leading coefficient is divided out.

At j=3 retain `q=[z]P`. Rows 2,3,4 still reconstruct v,w,h with nonzero scalar pivots. The primitive numerators of rows 5 through 8 generate an ideal in `Q[A,q]`, generator order `(A,q)`, order `dp`. The emitted `structure-quadratic.sing` computes its standard basis `(1)`; an independent exact rational calculation agrees. The same replay checks the cubic family's full residual is zero. Thus all integers j>=2 are covered by two polynomial resultant identities and **one justified exceptional computation**, not by a finite sample of j. The explicit scalar formulas, row numerators and compact `EXACT_Q_ALL_PASS` output are in the notes. This proves a restricted uniform exclusion, not a cutoff for arbitrary L.

**6. Exact computations and their scope.**

The local driver `exact_degree.py` emits (UF) directly in a large polynomial ring with variables `(x,l2,...,l_(m-1),b,B,eta)` and characteristic-zero coefficient field `(0,d)`, `minpoly=3*d^2-m`. It performs the scalar reconstruction above, checks the B coefficient against `-3d/2`, and checks every discarded low and high coefficient is zero. Only then does `imap` transfer the x-free residual generators and reconstructed B_m,eta_m into

```text
(Q(d), (l2,...,l_(m-1),b), wp(m-2,...,1,m)).
```

The source expressions contain only the declared small variables after elimination; equality is checked by coefficient identities, not by similarity of names. `std(K_m)` is computed exactly and the displayed b power is reduced to zero against that basis. No `sat()` wrapper, modular prime, rational reconstruction, or unchecked cofactor recovery is used.

| actual m | coefficient field | unused rows all zero | reduced basis size | exact conclusion |
|---|---|---|---:|---|
| 4 | Q(d), 3d^2=4 | yes | 17 | dimension 0; b^4 in K_4 |
| 5 | Q(d), 3d^2=5 | yes | 60 | dimension 0; b^5 in K_5 |
| 6 | Q(d), d^2=2 | yes | not obtained | 1800-second cap; no degree-six exclusion |

The m=6 basis attempt exited at its 1800-second cap (exit 124). No result is inferred from it. The m=4,5 results independently reproduce UTAC's exact exclusions. The monomial solution on b=0 with all small variables zero is an exact nonunit control for every K_m. The explicit C_B and C_3 families are positive solution controls on their legitimate degree strata.

An initial run failed its B-pivot and unused-row checks because Singular parsed `b^2/4` with an incorrect exponent. It was stopped; `exact_m6-rejected.out` retains the failure. The repaired emitter uses `(1/4)*b^2`. Only repaired runs with successful coefficient checks support the table.

Closing §4, lines 201–205, labels its finite data MEASURED-MODULAR; those data are not used as characteristic-zero evidence. Radical §§4–6 explicitly show why finite small-power patterns do not supply the desired uniform statement. UTAC §6 proves that closing nilpotence exponents can grow without new reduced components. None of these facts turns the present finite table into an all-m classification.

**7. The b=0 stratum: a proved complementary classification and the missing boundary theorem.**

First there is a complete whole-polynomial result on **b=B=0**. If L=0, (UF) gives `(theta-3)P^2=0`, hence P=0 in characteristic zero. Otherwise let m=deg L>=2. Top balance still gives `deg P=2m`, and

```text
P*(2xP'-3P+(3/2)L^2)=(3/16)L^4.                           (Z)
```

Suppose P has a nonzero root alpha of multiplicity r. Then L has multiplicity s>=1 there. In the differential factor the possible lowest orders are r-1 and 2s. Every possibility is as follows:

| comparison | forced order of the product | contradiction |
|---|---|---|
| r-1<2s | 2r-1 | cannot equal the even number 4s |
| r-1>2s | r+2s | equality to 4s would give r=2s, inconsistent with this inequality |
| r-1=2s | at least r+2s=4s+1 | too large, including any cancellation of the two leaders |

Thus P has no nonzero root, so `P=c*x^(2m)`. After division by x^(4m), (Z) is a constant quadratic equation for the rational function `L^2/x^(2m)`. That rational function must be constant. Consequently the complete list of nonzero solutions on b=B=0 is

```text
L=A*x^m, P=p*A^2*x^(2m), A!=0,
(4m-3)p^2+(3/2)p-3/16=0.
```

In particular eta=P_2=0. These unbounded-degree solutions are outside the desired B*eta-nonzero boundary and illustrate why it would be wrong to exclude the entire b=0 stratum by leading balance.

The terminal ideal is explicitly

```text
C=x^(t-1)+c1*x^(t-2)+...+c_(t-1), L=x^2*C/y-b,
J_t=([x^4]F,...,[x^(2t+2)]F) in k[c1,...,c_(t-1),b],
```

after scalar reconstruction of P with leading coefficient omega. These rows are Xempty's `E_2,...,E_(2t)`, since its Abel residual multiplied by x^2 equals UF (Xempty lines 90–108, 632–644).

For the actual missing boundary take b=0 and B*eta nonzero. Write `L=x^2 A`, `P=xW`. Dividing the complete UF identity by x^2 gives exactly

```text
(theta-1)(W^2)+((3/2)x^3 A^2-B)W
  =(3/16)x^6 A^4-(3/4)B*x^3 A^2-B*eta*x.                 (B-UF)
```

For m=t+1, the terminal conditions, on each factor `3d^2=m`, are

```text
q=2m-1, y=(d+m)/(2q), omega=1/(4y^2(2d+1)),
deg A=m-2, lc A=1/y;
deg W=2m-1, lc W=omega;
W(0)=-B, W'(0)=eta, B*eta!=0.                             (B-JL)
```

The missing theorem is precisely that **no polynomial A,W satisfying (B-UF) and (B-JL) exists, for every m>=4 and every field factor**. By Xempty's scalar-unit reconstruction and its reversible map, this is equivalent to

```text
B*eta in sqrt(J_t+(b)) for every t>=3 and factor.             (BOUNDARY)
```

The t=2 boundary is covered separately by Xempty lines 430–444. Xempty §7.3, lines 848–877, proves `ord_0 P=1`, `ord_0 H=2`, removes their product's x^3 factor, and constructs an exact finite-algebra isomorphism. It does not prove this exclusion. Its lines 879–909 explicitly leave open the requirement that the complementary factors satisfy the differential linkage. Their degrees `2m-1,2m-2`, with total `4m-3`, are consistent for every m. The other boundary involving the slice determinant Delta is not an interchangeable name for b=0.

The local-root argument for (Z) also has an exact limit: for B*eta nonzero, reducing R modulo L gives `-B*eta*x^3`. Hence P and L have no common nonzero root; their gcd is x up to a scalar at b=0. Nonzero P roots now occur off L=0, where simple roots are compatible with UF. The parity contradiction used in (Z) is unavailable. By (SUPPORT), any such boundary solution also has gcd 1 among the exponents in L. These restrictions do not exclude it. Tacnode lines 205–207 expressly make no b=0 radical claim.

**8. Exact residual and the conditional whole-ray dependency chain.**

What survives the entire-polynomial analysis is the following typed statement, with all coefficients defined by §4:

```text
OPEN[K16-UETA-WHOLE-POLYNOMIAL]:
For every actual m>=4 and every field factor k_m of Q[d]/(3d^2-m),
V(K_m) has no geometric point with b*eta_m != 0.

Equivalently: eta_m in sqrt(K_m:b^infinity).
Sufficient stronger assertion: b in sqrt(K_m), for every such m and factor.
```

Degrees four and five are discharged exactly above. For the remaining unbounded degrees the weak target needs only support gcd 1 or 2, and only gcd 1 if B_m is nonzero. The stronger target additionally has to exclude eta_m=0 solutions outside C_3 and C_B. The structured-family theorems do not cover arbitrary L. Neither a choice of u chart nor a free P-coefficient list has been concealed: `u=4eta+3bl2`, and eta nonzero does not imply u nonzero. This entire-polynomial formulation includes that missed locus without resolving it.

For completeness, the precise conditional promotion chain is recorded below. Every source label refers to the frozen files in §1.

| implication | frozen source and necessary qualification |
|---|---|
| U_eta gives `B eta in sqrt(J_t:b^infinity)` | UTAC §9, lines 326–330; specialization uses Xempty lines 90–108 and 632–644's reversible coefficient map `L=x^2 C/y-b`, `P=xW-b^2/4`; only b nonzero is covered |
| this plus (BOUNDARY) gives `B eta in sqrt(J_t)` | UTAC §9, lines 332–342; radical decomposition into the b-nonzero and b-zero loci |
| the latter target transports to the positive terminal ideal | Xempty §8, lines 913–924: triangular row-image theorem and high elimination, explicitly `gy F(x)+3x(D0(x+b4)-D0(b4))=0` |
| `B eta in sqrt(J_t)` gives `tau in sqrt(I_+)` | Xempty lines 926–941: `R_boundary=y eta/3`, `tau=-(gy/3)B eta mod I_+`; gy/3 is a unit factorwise by lines 61–65 and 934 |
| `tau in sqrt(I_+)` gives `(I_+,T_(t,0))=S_t` | Xempty lines 942 and 949–956, charged (8.1): `T_(t,0)=yg+tau` has a finite geometric-series inverse |
| unit ideal gives empty terminal normalized receiver chart | Xempty lines 943–946 |
| empty receiver chart gives no solution of the original K16 ray system, hence (T) at t | Xempty lines 943–946, consuming its frozen constant spine, normalizer and second affine spine; repeated in UTAC §9 |

The boundary combination requires no uniform nilpotence exponent. Indeed if `b^k r^u in J_t`, `r=B eta`, and `r^v=j+bh` with j in J_t, then `r^(u+kv)=r^u(j+bh)^k in J_t`. This is also an elementary proof of the needed direction of the radical decomposition. A proof after inverting b alone cannot replace its second hypothesis: in Q[b,eta], the ideal (b) becomes the unit ideal on that open set although eta is not in its unlocalized radical.

The final arrows are consumed frozen theorems, not independently reconstructed upstream proofs. Consuming Xempty lines 958–985's finite whole-index range through t=7 gives its residual t>=8; without consuming its stated t=6,7 results the remaining frontier is t>=6. No finite-index equality here extends either range uniformly. Since U_eta and (BOUNDARY) remain unproved, the chain has no new whole-ray antecedent, and **no THEOREM (T) for the whole ray is asserted**.

**9. Completion and fallacy audit.**

All lane computations have ended. Retained artifacts total under 100 KB; the lane stayed within its time and disk limits.

Actual degree, coefficient-field factors, vanished leaders, radical versus ideal membership, and finite versus uniform scope remain explicit. Tacnode Theorem 3.1 supplies no polynomial conjugate branch. No top coefficient is identified with a constant jet, and no unproved cutoff, height count, or modular signal is promoted.

No new exit-price assertion is made, so no charge_basis line applies. The proved uniform claims have the restricted scopes in §§3–5 and §7. The unrestricted classification, U_eta, and the displayed (B-UF) exclusion remain **OPEN**.

<!-- BODY-END -->

Seal: the body is every byte through the marker and its terminating newline.
Body bytes: `23812`.
Body SHA-256: `f04c483c94f9c1320e4d630cfd52422ca3730ad396d0d653c3d3ef2a2c49e8ac`.
