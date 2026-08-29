# Hostile review — H17/q7/a3 arcwise Gate-A composition

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-arcwise-gate-a-composition-theorem-20260826.md` |
| Target SHA-256 | `266d85ca49aae4b893e0514a3ab1bf271c688ce54295ae20f414675a8c401bc3` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim; `q=7`, `ord(a)=3`, and `ord(R_i,S_i)>=14` are named Newton-cell data, not first-block consequences; Section 5 remains conditional on the companion all-orders IFT, which was not reviewed |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation of the Gate-A composition. Different model family from the producer. No producer status line, no charged `CONFIRMED`/`PASS`/`UNIT`/`ENDPOINT` token, and no validator string is evidence |
| Method | SHA-256 of the target and every charged pin; hand and rational polynomial expansion of both directions of (3.1)--(3.2) and of monic square division; independent Euclidean/UFD derivation of `N0=m z(z^2+p)` on `D(p*m)`; independent binomial, load, and target grade arithmetic under `Lambda=sigma^3`; independent cancellation of the weight-42/45 load clusters against (1.4); explicit ramified section of `Lambda=tau^3 varrho` with unit inverse of the odd-coefficient twist. Characteristic 65521 was not used. The companion all-orders normalized IFT was not opened as an algebra source |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target and of every charged input named in the review prompt match those pins. Producer verdict language, the target's own status line, and both charged reviews' `CONFIRMED` tokens were not used as characteristic-zero evidence. The first-block lemma was consumed only after its numbered identities were re-expanded. The one-parameter reduction was consumed for the displayed row identity `(0.1)` and the unit automorphism, not for a fibre-equality slogan. Sequential grade-51 review was consumed only as the finite receiver `(5.1)`, not as an all-orders lift. No file other than this review was written. Charged artifacts, shared ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On a complete characteristic-zero DVR, after the ramification `Lambda=sigma^3`, a literal delayed-load source arc in the named cell

```text
H=17,  q=min(ord U, ord V)=7,  ord(a)=3,
Q0=z^2(z^2+p),  p a unit,  K10 a unit,
ord(R0,R1,S0,S1)>=14
```

has first unloaded quadratic polar part exactly `(3/8) sigma^{34} [N0^2/Q0]_-`. Delayed loads and `mu2` start at grade 42, `mu4` at 48, the cubic at 51, `mu6` at 54, and `J/4` at 57. No omitted binomial, moving jet, load, or target occupies grade 34. The charged first-block equivalences therefore force `Q0|N0^2`, and unique factorization on the coprime squarefree type `A0=z`, `D0=z^2+p` forces `N0=m z(z^2+p)` with `m` a unit. The maps (3.1) and (3.2) are inverse regular maps on `D(M)`, sending that closed point to `(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0)`. After the delayed-load weights and the capital graph (1.4), substitution into the complete ordinary-Faber tails is the same source substitution as the frozen H17 producer: every effective lowercase slot is `sigma^{42}` times its capital coordinate, and the weight-42/45 load clusters cancel identically. The leading projective split lands on `D(X_0)` or `D(Y_0)` according as `U_7` or `V_7` is a unit. The finite ramification `sigma=s^4`, `tau=varrho=s^3` is an explicit section of `Lambda=tau^3 varrho` with `R=1+s^3` a unit, so the one-parameter arc lifts to the strict two-parameter source by the polynomial row identity and the unit inverse, not by special-fibre equality alone. Conditional on the companion all-orders IFT, the inverse of these two-sided maps produces a literal source-row formal arc on this one named Newton cell.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| Gate-A theorem (target) | `266d85ca49aae4b893e0514a3ab1bf271c688ce54295ae20f414675a8c401bc3` | immutable composition (matches required pin) |
| first-block theorem | `56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23` | charged elementary input (matches required pin) |
| first-block hostile review V2 | `85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff` | charged review bytes; verdict prose unused |
| one-parameter Rees reduction | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | cited row identity `(0.1)` and unit twist; not a fibre-equality license |
| one-parameter reduction review | `1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de` | charged review bytes; verdict prose unused |
| sequential grade-51 review | `465f53cd423d94645f0b99f4e96d18853bb469b96dc2f85590dc7fe912d158ec` | charged finite receiver; not an all-orders IFT |

All six files are presently untracked. `HEAD` at review time is `418e413593120d19e15e6546eb50c985f4b1f038`. The first-block promotion and one-parameter promotion named in the target were not charged by the review prompt and were not used as algebra. The companion all-orders normalized Kummer-lift theorem was not hashed and not reviewed.

---

## Strongest exact theorem that survives

Let `R` be a complete characteristic-zero DVR with uniformizer `sigma`. On the delayed-load ray

```text
Lambda=sigma^3,
k10=Lambda^{12} K10,  k6=Lambda^8 K6,  k2=Lambda^4 K2,
```

with `K10` a unit, after exact monic square division `C=Q^2+Delta` over `R[1/2]`, restrict to the named cell (1.3)--(1.4). Then:

1. The first negative ordinary block is isolated at grade 34 and is equivalent to `Q0|N0^2`. On `D(p*m)` one has `N0=m z(z^2+p)` with `m` a unit.
2. The seven-tuple `(a,E,U,R0,M,V,W0)` of (3.1)--(3.2) is a polynomial coordinate isomorphism with `(q2,q1,q0,n3,n2,n1,n0)` on `D(M)`. Multiplied by `sigma^{17}` in the normal, this is the unsplit affine-Faber chart of the frozen H17 graph. The leading-order split of `(U,V)` lands in one of the two projective charts `D(X_0)`, `D(Y_0)` of the confirmed grade-48 predecessor.
3. Substituting (3.2) and the capital load graph (1.4) into the complete ordinary-Faber tails, with every lowercase load slot equal to `Lambda^{14}` times the corresponding capital coordinate and with targets at (4.1), yields the identical seven source-row series as the frozen normalized H17 graph, coefficient for coefficient in `(Q,N,K,mu,J)`.
4. After the finite ramification `sigma=s^4` and the section `tau=varrho=s^3`, the same arc satisfies the strict two-parameter source rows, because those rows are the polynomial pullback of the one-parameter rows along `Lambda=tau^3 varrho` and the odd-coefficient twist is inverted by the unit `R=1+s^3`.

Conditional on confirmation of the companion all-orders normalized IFT, the inverse of (1)--(3) produces a literal formal coefficient arc satisfying all seven delayed-load source rows on this cell, with `J` a unit in the fraction field if the free determinant target is chosen with unit constant term. The statement is one named Newton cell. It is not a fan atlas, a global total-Rees theorem, a Taylor realization, order-two closure, `(8,12)` closure, maximum twelve, or JC2.

---

## Attack 1 — exact powers on `Lambda=sigma^3`; grade 34 is isolated

**CONFIRMED.** No omitted correction occupies the first negative block.

The one-parameter source, re-read from the charged reduction rather than from Gate-A prose, is

```text
Phi_ell = r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^{10} k2)
          - Lambda^{12+ell} delta_ell,
(delta_1,...,delta_7)=(0, mu2, 0, mu4, 0, mu6, J/4).
```

The delayed graph (1.1) puts every effective lower-load slot at `Lambda^{14}`:

```text
Lambda^2  * Lambda^{12} K10 = Lambda^{14} K10,
Lambda^6  * Lambda^8  K6    = Lambda^{14} K6,
Lambda^{10}* Lambda^4  K2    = Lambda^{14} K2.
```

With `Lambda=sigma^3` this is sigma grade 42. Affine-linearity of `r_ell` in the three lower loads puts quadratic load monomials at `Lambda^{28}=sigma^{84}`, far after the first block. Target grades from the same source:

| datum | source power | sigma grade |
|---|---:|---:|
| delayed loads `(K10,K6,K2)` | `Lambda^{14}` | 42 |
| `mu2` in row 2 | `Lambda^{14}` | 42 |
| `mu4` in row 4 | `Lambda^{16}` | 48 |
| cubic `Delta^3/Q^3` | `sigma^{51}` | 51 |
| `mu6` in row 6 | `Lambda^{18}` | 54 |
| `J/4` in row 7 | `Lambda^{19}` | 57 |

Odd targets are identically zero.

At fixed `z`, with `C=Q^2+Delta` and `ord(Delta)=17`, the binomial series in characteristic zero is

```text
(Q^2+Delta)^{3/2}
  = Q^3 + (3/2) Q Delta + (3/8) Delta^2/Q - (1/16) Delta^3/Q^3 + ....
```

The coefficient of `X^3` in `(1+X)^{3/2}` is independently `(3/2)(1/2)(-1/2)/6=-1/16`. `Q^3` and `(3/2) Q Delta` are polynomials in `z`. Write `Delta=sigma^{17} N` with `N0=N mod sigma !=0` by the declared normal order. Then:

- `(3/8) Delta^2/Q` has exact grade 34, polar part `(3/8) N0^2/Q0`;
- `-(1/16) Delta^3/Q^3` has grade 51;
- every later binomial term has grade at least 68.

Moving jets: `Q=Q0+sigma Q'` and `N=N0+sigma N'` produce

```text
Delta^2/Q = sigma^{34} N0^2/Q0 * (1 + O(sigma)),
```

so every correction to (2.2) has grade at least 35. Loads and `mu2` cannot meet grade 34 because `42>34`. The cubic cannot meet grade 34 because `51>34`. Later targets are later still. The H15 routing table already records that loads can tie or precede the quadratic block only for `H>=21`; here `2*17=34<42`.

Laurent-to-ordinary connection. The first possible negative `z`-principal part of `C^{3/2}` is the grade-34 polar part of `(3/8) Delta^2/Q`. Polynomial summands contribute nothing to `h_j` for `j>=1`. The charged first-block lemma supplies a lower-unitriangular diagonal-one map from `(h1,...,h4)` to the first four ordinary rows. A complete initial ordinary block of length four at grade 34 therefore vanishes if and only if `h1=h2=h3=h4=0` at that grade. Moving connection coefficients multiply already-vanishing earlier negative `z`-coefficients, of which there are none, or else raise the grade. The connection cannot tie grade 34.

The coefficient `3/8` is a unit in `Q`. On an equicharacteristic-zero DVR, and on any mixed-characteristic DVR of residue characteristic not `2` or `3`, it preserves grade 34. The target already localizes at `2`. Residue characteristic three would collapse the displayed binomial and is outside the charged characteristic-zero composition; it is not a missing hypothesis inside that neighbourhood.

---

## Attack 2 — ordinary-first-four bridge forces `N0=m z(z^2+p)` on `D(p*m)`

**CONFIRMED.** The implication is exact on the written factor type; `p` a unit and `m` a unit cannot be dropped.

The charged first-block statement, re-expanded rather than taken from review prose: Euclidean division `N^2=A Q+R` with `deg R<=3` and the reciprocal

```text
1/Q = z^{-4}(1 - q2 z^{-2} - q1 z^{-3} + O(z^{-4}))
```

give the triangular identities

```text
h1=r3,  h2=r2,  h3=r1-q2 r3,  h4=r0-q2 r2-q1 r3
```

with diagonal one over `Z[q2,q1]`. Thus `h1=h2=h3=h4=0` if and only if `R=0` if and only if `Q|N^2`, and then every later negative coefficient vanishes as well. Four rows are sharp: remainder `R=1` gives `h1=h2=h3=0` and `h4=1`.

Over the UFD `k[z]`, `Q|N^2` if and only if `Q_half|N` with `Q_half=prod_f f^{ceil(e_f/2)}`. Under the hypotheses

```text
Q=A^2 D,  deg A=1,  deg D=2,  gcd(A,D)=1,  D squarefree,
```

one has `Q_half=A D` of degree three. A degree-three divisor of a polynomial of degree at most three is a scalar multiple, uniquely `N=M A D`.

Apply this on the residue field of the DVR to `Q0=z^2(z^2+p)` with `p` a unit and `deg N0<=3` (because `deg Delta<=3`). Set `A0=z` and `D0=z^2+p`. Then:

- `gcd(A0,D0)=1` because `D0(0)=p!=0`;
- `D0` is squarefree because its discriminant is `-4p!=0` after inverting `2`;
- `deg N0<=3=deg(A0 D0)`.

The first-block criterion therefore yields `N0=m z(z^2+p)` for a unique scalar `m` in the residue field. The definition `ord(Delta)=17` forces `N0!=0`, hence `n3 mod sigma=m` is a unit of the DVR. This is (2.4). Independently, with `m=5`, `p=7`,

```text
N0^2 = 25 z^6 + 350 z^4 + 1225 z^2,
Q0 (25 z^2 + 175) = N0^2,     remainder 0.
```

Hypotheses that cannot be dropped:

- squarefreeness of `D0`: if `D0=B^2` then `Q0=A0^2 B^2` requires only `A0 B|N0`. Explicit control: `Q=(z^2-1)^2`, `N=z^2-1` satisfies `Q|N^2`, while `A D=(z-1)(z+1)^2` does not divide `N`. This is the `p=0` / double-double / Pell collision, already firewalled in Section 6.
- degree: if `deg N0>3` the scalar conclusion fails. Square division forbids this.
- `m!=0`: if `m=0` then `N0=0`, contradicting the declared order 17. Route: raise `H`.

If `Q0` is squarefree then `Q_half` has degree four, so `N0=0`, contradicting (1.3). If `Q0` is a square, or `D0` collides with `A0`, the type is not the coprime squarefree repeated-`A` cell. The implication (2.3) `=>` (2.4) is therefore exact on `D(p*m)`, and is a kernel statement, not an analogy with the affine-Faber normal.

---

## Attack 3 — both directions and every sign of (3.1)--(3.2); q=7 kernel versus order-14 complements

**CONFIRMED.** The unsplit seven-tuple is a two-sided polynomial isomorphism on `D(M)`. The exact values `q=7`, `ord(a)=3`, `ord(R_i,S_i)>=14` are named cell data. They are not forced by the first block. The theorem does not claim they are.

Monic square division is itself a polynomial isomorphism over `R[1/2]`. Expanding `Q=z^4+q2 z^2+q1 z+q0` gives

```text
Q^2 = z^8 + 2 q2 z^6 + 2 q1 z^5 + (2 q0 + q2^2) z^4
        + 2 q2 q1 z^3 + (2 q2 q0 + q1^2) z^2 + 2 q1 q0 z + q0^2,
```

with no `z^7` term. Equating `C=Q^2+Delta` and inverting is

```text
q2=C6/2,  q1=C5/2,  q0=(C4-q2^2)/2,
Delta3=C3-2 q2 q1,  Delta2=C2-q1^2-2 q2 q0,
Delta1=C1-2 q1 q0,  Delta0=C0-q0^2.
```

Both composites were recomputed on independent integer tuples and are the identity. The inverse is the polynomial expansion of `Q^2+Delta`. There is no blowup or Rees torsion in this map.

Now the affine-Faber seven-tuple. Let `A=z-a` and `D=A^2+4 a A+E`. Expanding in `z` over `Q[a,E,U,R0,M,V,W0]`:

```text
A^2 D = z^4 + (E-6 a^2) z^2 + 2a(4a^2-E) z + a^2(E-3 a^2),
A D   = z^3 + a z^2 + (E-5 a^2) z - a(E-3 a^2).
```

The `z^3` coefficient of `A^2 D` cancels, so `Q` remains depressed. Adding `U A+R0` and `M(A D)+V A+M U/2+W0` produces exactly (3.2):

```text
q2=E-6 a^2,
q1=2a(4a^2-E)+U,
q0=a^2(E-3 a^2)+R0-a U,
n3=M,
n2=a M,
n1=(E-5 a^2)M+V,
n0=-a(E-3 a^2)M-a V+M U/2+W0.
```

These are polynomial identities. Every sign was checked by expanding `(z-a)^k` and collecting coefficients, and by a rational probe `(a,E,U,R0,M,V,W0)=(2,5,7,11,13,17,19)`: both directions return the same seven-tuple. On `D(M)` they invert regularly by (3.1). Substituting (3.2) into (3.1) is the identity on `(a,E,U,R0,M,V,W0)`. Substituting (3.1) into (3.2) and clearing the denominator `M` is the identity on `(q2,q1,q0,n3,n2,n1,n0)`. No root of the moving quartic is adjoined. The coordinate `a=n2/M` is regular on `D(n3)`.

Closed point. From (1.3) and (2.4),

```text
Q0=z^4+p z^2,     N0=m z^3 + m p z,
```

so `(q2,q1,q0,n3,n2,n1,n0)=(p,0,0,m,0,m p,0)`. Then (3.1) returns

```text
M=m,  a=0,  E=p,  U=0,  R0=0,  V=m p-p m=0,  W0=0.
```

This is (3.3). Independently, `Q0=A^2 D` and `N0=M A D` at `A=z`, `D=z^2+p`, `M=m` is the same point. Hence every DVR arc through that point has `q=min(ord U, ord V)>0` and `ord(a)>=1`, with `q=infinity` allowed. That much is forced.

What is not forced. First-block divisibility never sees the higher jets of `n2`, `U`, or `V`. The exact orders

```text
ord(a)=3,  min(ord U, ord V)=7,  ord(R0,R1,S0,S1)>=14
```

are the named Newton cell (1.3). They match the internal H17 equality wall `v(a)=17-2q`, `v(R_i)=v(S_i)=2q` of the normalized graph, but that wall is graph data, not a residue-field consequence of `H=17`. The theorem already says that (1.3)--(1.4) name a single closed cell and does not assert that every literal source arc enters it. Complements appearing before order `2q=14` are a different cell (the linear pivot of the valuative complement form); they are not a hole in this cell.

Split versus unsplit. The frozen H17 producer uses

```text
qc = 2a(4a^2-E)+X+R1,
n1 = lambda((E-5a^2)M+Y+S1),
n0 = lambda(-a(E-3a^2)M-a Y+(M X)/2+S0-a S1).
```

The unsplit formulae (3.2) use a single pair `(U,V)` and a remainder `W0`. These agree on `(Q,N)` under the linear identifications

```text
U=X+R1,   V=Y+S1,   S0=W0+(M/2) R1.
```

The extra pairing `(M/2) R1` in unsplit `n0` is therefore not a failed sign: it is absorbed by the producer complement coordinate `S0`. The unique two-sided map is the unsplit seven-tuple (3.1)--(3.2). A canonical section of the split is `R1=S1=0`, `X=U`, `Y=V`, `S0=W0`. On that section, `D(X_0)` (resp. `D(Y_0)`) is exactly `D(U_7)` (resp. `D(V_7)`). The cell hypothesis `min(ord U, ord V)=7` with at least one leading kernel coefficient nonzero puts the arc on one of the two confirmed grade-48 projective charts. Independent high jets of `X` overlapping `R1` are a non-unique presentation of the same `(Q,N)`, already admitted by the valuative composition; existence of some splitting is all Gate-A uses. The inverse, from any split-graph point to `(Q,N)` to `C`, is unique. There is no root extension, Rees torsion, or illicit inversion on `D(M)`.

---

## Attack 4 — load graph, target timings, lowercase versus capital, coefficientwise rows

**CONFIRMED.** There is no lowercase/capital load error and no effective-target scaling error. The capital graph (1.4) times `Lambda^{14}` is the frozen producer substitution.

The ordinary-Faber tails are polynomials in the ten slots `(B0,...,B6,k10,k6,k2)`. The source `Phi_ell` feeds those slots the already-weighted combinations `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^{10} k2`. Combined with (1.1) every such slot is `Lambda^{14}` times the capital coordinate. Under `Lambda=sigma^3` this is `sigma^{42}` times (1.4):

```text
k10_slot = sigma^{42} kappa,
k6_slot  = sigma^{42} ((15/32) kappa E^2 + sigma^6 d6),
k2_slot  = sigma^{42} ((15/256) kappa E^4 + sigma^6 d2),
mu2_eff  = sigma^{42} (-(5/4096) kappa E^6 + sigma^6 dm),
mu4_eff  = sigma^{48} d4,
mu6_eff  = sigma^{54} nu6,
(J/4)_eff= sigma^{57} (J/4).
```

This is byte-for-byte the frozen H17 substitution `LK10=s^{42}*KK`, `LK6=s^{42}*((15/32)*KK*EE^2+s^6*d6)`, `LK2=s^{42}*((15/256)*KK*EE^4+s^6*d2)`, `MU2=s^{42}*(-(5/4096)*KK*EE^6+s^6*dm)`, `MU4=s^{48}*d4`, together with (3.2) multiplied by `lambda=s^{17}`. The target's (1.4) writes capital coordinates without the overall `sigma^{42}`; the factor is supplied by (1.1) plus `Phi_ell`, and is recorded as the effective timings (4.1). Substituting (1.4) into unweighted tails without that factor would be a genuine scaling error. That is not the substitution used.

Independently recomputed weight-42/45 load clusters on the capital leading graph `d2=d6=dm=0`, with `K2=(15/256) kappa E^4`, `K6=(15/32) kappa E^2`, `K10=kappa`, `mu2=-(5/4096) kappa E^6`:

```text
C2_load(42)-mu2 = kappa E^6 (
    -15/2048 + 45/4096 - 5/1024 + 5/4096
) = kappa E^6 (-30+45-20+5)/4096 = 0,

C6_load(42) = kappa E^8 (
    15/32768 - 15/16384 + 15/32768
) = 0,

C1_load(45) = kappa a E^5 (-15/256 + 45/256 - 30/256) = 0,
```

and the same three-term cancellation for the `C3`, `C5`, `C7` triples against `(15/256, 15/32, 1)`. Because the identities are polynomial in the full series `E` and `kappa`, they kill every positive-excess jet of those clusters. After subtracting `mu2` from row 2 and `mu4` from row 4, no load or target reaches below grade 48. That is the content of "the polynomial weight-42/45 load identities cancel precisely the predecessor terms below weight 48."

Normal coefficients in (3.2), multiplied by `sigma^{17}`, are the producer `N3=s^{17} MM`, ..., with `E-5a^2=(E-3a^2)-2a^2` the producer `DD-2 AA^2` form of `n1`. No Laurent row replaces an ordinary row. Row 7's target is `Lambda^{19}(J/4)` with a uniform minus in `Phi_7=r_7-Lambda^{19}(J/4)`, matching the charged V2 ending `-tau^{57} rho^{19}((j/4)(1+tau))`. The overall sign of `J/4` is not a scaling of the grade.

Thus, on the named cell, the complete source rows in `(Q,N,loads,targets)` are the complete normalized graph rows. This is the missing arcwise Gate-A identity. It is a coefficient isomorphism on one DVR, not a monolithic Rees algebra and not an atlas of neighboring valuation cells.

---

## Attack 5 — strict two-parameter lift; flatness versus the explicit ramified section

**CONFIRMED** as an explicit ramified lift. Flat base change licenses equality of saturated central fibres, not by itself this arc. The target's actual argument uses the polynomial row identity and the unit inverse, which do license the lift.

The charged one-parameter reduction states two distinct facts.

- Row identity: after localizing at `R=1+tau` and setting `C_i=R^{i mod 2} B_i`, `J=R j`, `Lambda=tau^3 varrho`, every two-parameter generator is the pullback of

  ```text
  Phi_ell = r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^{10} k2)
            - Lambda^{12+ell} delta_ell.
  ```

  This is an identity of polynomials, independently rechecked on the four even/terminal target exponents `tau^{42} rho^{14} mu2`, `tau^{48} rho^{16} mu4`, `tau^{54} rho^{18} mu6`, `tau^{57} rho^{19}(j/4)(1+tau)`.

- Flatness: `Q[Lambda] -> Q[tau,varrho,R^{-1}]` is torsion-free over a PID, hence flat, and saturated special fibres over `Lambda=0` and `(tau,varrho)=(0,0)` coincide.

Flatness of the toric map does not construct a section, does not ramify a uniformizer, and does not produce a formal arc from a one-parameter solution. Equality of central fibres is a statement about the reduced boundary scheme, not about a curve of positive order in `Lambda`.

The lift that the target actually writes is not that fibre statement. It is the explicit section

```text
sigma=s^4,     tau=s^3,     varrho=s^3.
```

Then `tau^3 varrho=s^{9} s^{3}=s^{12}=(s^4)^3=sigma^3` as monomials. Both `tau` and `varrho` have positive order. `R=1+s^3` has constant term 1, hence is a unit in `Q[[s]]`. The inverse `B_even=C_even`, `B_odd=C_odd/R`, `j=J/R` is therefore regular along the arc. If `Phi_ell(C(sigma), Lambda=sigma^3, k, J)=0` in `Q[[sigma]]`, the pullback along `sigma=s^4` remains zero, and the row identity gives `Psi_ell(B(s), tau(s), varrho(s), k, j)=0` in `Q[[s]]`. Loads are not twisted. This is existence after finite ramification, not uniqueness of the splitting `v(Lambda)=3 v(tau)+v(varrho)`, which the target correctly declines to classify.

Membership in the required opens, along this arc:

- `R=1+s^3` is a unit, so the localization at `R` does not meet the arc. The inverse twist is defined.
- If the free determinant series is chosen with unit constant term, then `J` is a unit in `Q[[sigma]]` and `j=J/R` is a unit in `Q[[s]]`. Effective occurrence remains `sigma^{57} J/4`.
- `Lambda=s^{12}`, `tau=s^3`, `varrho=s^3` are nonzero in the fraction field, so the generic point of the arc lies in `D(Lambda J)=D(tau varrho j)`. Saturation by those elements does not delete a formal arc along which they are nonzerodivisors.
- At `s=0` one has `R=1`, hence `B_i ≡ C_i` and `j ≡ J`. The special fibre of `C` is `Q0^2=z^4 (z^2+p)^2`, which has nonzero coefficients, so the arc is not in the coefficient-irrelevant locus.
- `K10=kappa` is a unit by (1.1) and (1.4); at the receiver (5.1) the constant `kappa(0)=8 m^3/(5 a3^3 p^5)` is a unit on `D(a3 p m)`, so the IFT does not drive `K10` off `D(K10)`.

The odd-coefficient twist changes the octic presentation. It is not claimed, and is not true, that the two-parameter octic `B` remains in the same H17 square-normal Newton cell in the `s`-adic. The claim is that `B(s)` satisfies the two-parameter source rows. That is what the row identity gives.

The epithet "literal flat pullback" in the target's Section 4.1 is therefore slightly loose as a citation of the reduction's fibre theorem, and accurate as a citation of the reduction's row identity (4.2). The numbered lift claim does not depend on the loose epithet.

---

## Attack 6 — strongest exact result and scope

**CONFIRMED.** The target's Section 6 matches the algebra.

Covered, and only this:

```text
H=17, q=7, ord(a)=3,
D(p*m*K10),
the load graph (1.4),
the two projective opens D(X_0) and D(Y_0).
```

Not covered, and correctly firewalled:

- a different factor type, `p=0`, `m=0`, `K10=0`, unit kernel, unequal kernel order outside the registered split, another center order, another load slope, or the rest of the source fan;
- a global total-Rees/Cech atlas, pairwise chart overlaps, commutation of saturation with specialization, or classification of other positive-rational splittings of `v(Lambda)=3 v(tau)+v(varrho)`;
- the invariant rational coefficient functions at the two finite branches, terminal-to-global algebraization, or either finite Taylor polynomiality pullback;
- a Keller map or counterexample, order two, `(8,12)`, maximum twelve, or JC2.

Section 5's unique all-orders lift of the receiver

```text
5 kappa(0) a3^3 p^5 - 8 m^3 = 0
```

is explicitly conditional on the companion complete-local IFT. That companion was not reviewed here. The finite identity (5.1) itself is the charged sequential grade-51 residual `H51=-2 m^3 p^2+(5/4) kk0 a3^3 p^7`, which on `D(p)` is the same equation; it is a finite prolongation, not the IFT. The Jacobian display `45 x m^2 a3^4 p^{16}/2^{19}` is likewise a companion claim and is not re-proved. Gate-A's contribution is the two-sided coefficient identification that turns a normalized-graph solution into a literal source-row arc, and conversely. That identification does not by itself produce polynomiality.

The result is therefore one named Newton cell of delayed-load affine-Faber type, with a ramified lift to the strict two-parameter source. It is not a fan atlas, a global total-Rees theorem, a Taylor realization, an order-two closure, a max12 result, or a JC2 result.

---

## What was not used as evidence

The target's status line, both charged `CONFIRMED` tokens, the sequential grade-51 `PASS`/`ENDPOINT` strings, the first-block promotion, the one-parameter promotion, AWS validator tokens, and characteristic 65521. The companion all-orders theorem was not read as algebra. No producer case file was edited. No Singular, Sage, msolve, or Lean run was required: the identities are polynomial division, unique factorization, binomial coefficients, and a unit automorphism after one ramification.

CONFIRMED
