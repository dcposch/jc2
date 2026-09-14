# K16 b=0 product boundary: marked rational pole rigidity and a quadratic norm model

2026-09-06. Desk lane `boundary-product-astra-desk`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

**Verdict: NEW UNIFORM LEMMAS; THE PRODUCT TARGET REMAINS OPEN.** A rational relaxation has an exact, globally controlled defect: under the constant marking, `A=c/x+A0(x)`, `W` is polynomial, and `eta-W'(0)=3c^2/4`. The prescribed linear marking kills the only possible pole. There is a genuine rational negative control when that marking is omitted. A second lemma replaces the earlier quartic intersection parameter by a quadratic norm model and retains its entire differential linkage. Neither lemma proves nonexistence, classifies all UF solutions, or promotes the K16 whole-ray theorem.

## 1. Frozen inputs and exact target

The following completed, sealed reports were read only. Their full SHA-256 values agree with their terminal `.run.v2` receipts (`final_status=DONE`, `report_state=BODY_SEALED_AFTER_DIVERT`). The first report was read completely; only the directly relevant sections of the other reports were consumed.

| source | full report SHA-256 | scope used |
|---|---|---|
| `xmodel/k16-ueta-classification-astra-20260906.md` | `f04c483c94f9c1320e4d630cfd52422ca3730ad396d0d653c3d3ef2a2c49e8ac` | full; especially §§5,7 |
| `xmodel/k16-xempty-astra-20260905.md` | `1f06694fb58d53c4a4b3c54dad88722cd31a5ccc894679ac52b0620b91e2623f` | UF map and §§7.1–7.3 |
| `xmodel/k16-f3abel-astra-20260905.md` | `0d2b27fed00a27a1f21d0997adce38252405506839d74f674327f2ff994b22b4` | boundary normalization, §§6–7 |
| `xmodel/k16-universal-series-fable5-20260905.md` | `5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb` | §3 residue limitation and beginning of §4 |

Work at geometric points over an algebraically closed characteristic-zero field k. Write

```text
U=x^3 A^2,
E=2x W W' - W^2 + ((3/2)U-B)W
  -(3/16)U^2 +(3/4)B U +B eta x.
```

The target is absence of `E=0` with `W(0)=-B`, `W'(0)=eta`, `B eta!=0`, and, for every integer `m>=4`,

```text
q=2m-1, 3d^2=m, p=1/(4(2d+1)),
y=(d+m)/(2q), deg A=m-2, lc A=1/y,
deg W=q, lc W=p/y^2.
```

Both factors/embeddings of `3d^2=m` remain present. Statements below are point statements, not assertions about unlocalized nonreduced ideals.

## 2. Normalization is licensed, but the individual leaders must move

For nonzero `r,s,h` with `h^2=s r^3`, put

```text
Wtilde(x)=s W(rx), Atilde(x)=h A(rx),
Btilde=sB, etatilde=sr eta.
```

Directly, `Etilde(x)=s^2 E(rx)`. Taking `s=1/B`, `r=B/eta`, and either square root `h` normalizes `Btilde=etatilde=1`. The Euler derivation commutes with the variable scaling. Degrees and the ratio `lc W/(lc A)^2=p` are preserved, since `q=2(m-2)+3`.

The individual leading constants are **not** preserved. If `lambda=lc Atilde`, then

```text
lambda^2 y^2 = B^(2m-2)/eta^(2m-1),
lc Wtilde = p lambda^2.
```

Thus the normalized problem has arbitrary `lambda!=0`, not `lambda=1/y`. Conversely, given a normalized pair with this ratio, choose `eta0!=0` with `eta0^q=1/(lambda^2 y^2)`, set `B0=1`, and invert the above scaling; choose the sign of its square root so the reconstructed A has leader `1/y`. Then W has leader `p/y^2`. Consequently the geometric existence problems are equivalent, separately for each m and d. Adjoining roots is legitimate over k; over a coefficient ring this is a finite cover on the stated unit locus, not an undeclared ring automorphism.

## 3. New global lemma: the marked rational category already is polynomial

**Pole/defect lemma.** Suppose `A,W in k(x)` satisfy `E=0`, `B!=0`, and W is regular at zero with `W(0)=-B`. Then

```text
W in k[x],   A=c/x+A0(x),  A0 in k[x],
eta-W'(0)=(3/4)c^2.                                      (PD)
```

In particular the exact marking `W'(0)=eta` forces `c=0`; every such rational solution is polynomial. This holds uniformly in all degrees and does not require `eta!=0`. The latter is required for §2's normalization and for the campaign target.

Proof at a nonzero finite point alpha: if A has a pole of order a>=1, U has pole order 2a. If W has a pole of order w>=1, the possible largest pole orders of E are

```text
2w+1 from 2xWW',  2a+w from UW,  4a from U^2.
```

The first leader is nonzero because alpha and w are nonzero. If `w>=2a`, it is uniquely largest. If `w<=2a-1`, the U^2 term is uniquely largest. If W is regular, U^2 is again uniquely largest. All cases contradict E=0. If instead A is regular and W has a pole, the derivative term is uniquely largest. Therefore neither function has a pole away from zero. Since W was assumed regular there, W is polynomial.

At zero, if A has pole order a>=2, U has pole order `2a-3>0`; W is regular, so U^2 is the unique highest pole. Hence A has at most a simple pole. Put `A=c/x+O(1)`, `W=-B+w1 x+O(x^2)`. The entire coefficient of x in E is

```text
B*(eta-w1-(3/4)c^2).
```

This proves (PD), including `c=0`. There is no appeal to generic roots, squarefreeness, degree balance at infinity, or a formal solution being globally rational.

**Whole-equation negative controls.** Take `cB!=0` and either root

```text
p0^2+(3/2)p0-3/16=0,   p0=(-3 +/- 2sqrt(3))/4,
A=c/x, W=p0 c^2 x-B, eta=(p0+3/4)c^2.
```

Here `eta=+/-sqrt(3)c^2/2!=0`, and direct substitution gives E identically zero. Yet `W'(0)=eta-3c^2/4`, not eta. Thus `B eta!=0` and the constant marking alone do not imply polynomial A; the exact linear marking is essential. This is not a counterexample to the target: its jet is wrong and its degrees are outside the target. If instead `B=0`, take the same A,W and set `eta=p0 c^2`; then both markings hold but A still has a pole. This checks the necessity of the lemma's `B!=0` hypothesis.

The lemma eliminates finite-pole escapes in any proposed rational descent or rational integrability argument. It does **not** exclude a globally pole-free pair: that is exactly the remaining polynomial problem.

## 4. A new quadratic finite-algebra model on B=eta=1

Normalize as in §2 and set

```text
Z=xA,
R=(3/16)x Z^4-(3/4)Z^2-1,
J=2W'-(W+1)/x+(3/2)Z^2.
```

The constant marking makes J polynomial, and `E=x(WJ-R)`. On a solution `WJ=R`, `J(0)=1`, `deg W=q`, `deg J=q-1`, and `deg R=2q-1`. Define

```text
f(t)=3t(t-1),
D(t)=(3/4)Z(f(t))^2,       D(1-t)=D(t),
Q(t)=(t-1)D(t)-1
    =(27/4)t^2(t-1)^3 A(3t(t-1))^2-1.
```

There are exact identities

```text
Q(t)Q(1-t)=-R(f(t)),
f(x Z(x)^2/4)-x=xR(x),
f(t) Z(f(t))^2/4-t=tQ(t).                                (QN)
```

They give mutually inverse finite k-algebra maps, including all multiplicities,

```text
k[x]/(R)  <-->  k[t]/(Q),
t=x Z(x)^2/4,          x=3t(t-1).                         (QA)
```

Indeed R(0)=-1 and R modulo Z equals -1, so x, Z and hence t are units in the first quotient. The first norm identity gives R(f)=0 in the second; the last identity gives the t-composition. For the reverse direction, the middle identity gives `f(t)=x`; then the last identity and the unit t imply `Q(t)=0`. Here `Q(0)=Q(1)=-1` and `deg Q=2q-1=4m-3`.

This is a degree-two parameter map, unlike Xempty §7.3's degree-four map in v. It uses the extra b=0 biquadratic structure; it does not lower the quotient length or the actual m.

**The ramification exception is explicit.** The only finite ramification point of f is `t=1/2`, with `x=-3/4`. If R vanishes there, then `Z(-3/4)^2=-8/3` and, independent of Z',

```text
R'(-3/4)=4/3,     Q'(1/2)=-2.
```

Thus this root is simple in R and must belong to exactly one of W,J. If it belongs to W, its slope satisfies `3W'(-3/4)^2-4W'(-3/4)-2=0`, which is consistent over k. No division by `2t-1` may silently delete this case.

## 5. The exact remaining differential norm filter

Under (QA), W selects a divisor M of Q of degree q; write `Q=MN`, `deg N=q-1`, and `a=M(0)M(1)!=0`. Let `sigma M(t)=M(1-t)`, and likewise for N. Keeping the root multiplicities gives

```text
W(f(t))=-M(t)sigma M(t)/a,
J(f(t))=a N(t)sigma N(t).                                 (NF)
```

Away from `t=1/2`, Q and sigma Q have disjoint roots, since their difference is `(2t-1)D` and D is a unit at a Q root. At the fixed point both have a simple root as just checked; if W contains that x root, W(f) has exactly the required double root. This proves the norm factorization without assuming an unramified or squarefree quotient. The constants follow from Q(0)=Q(1)=-1 and W(0)=-1.

Define `V=M'(t)sigma M(t)-M(t)M'(1-t)`. Substituting (NF) into the definition of J and clearing denominators gives precisely

```text
3a^2 t(t-1)(2t-1) N sigma N
 = -2t(t-1)V +(2t-1)(M sigma M-a)
   +6a t(t-1)(2t-1)D.                                    (DF)
```

This is an entire polynomial identity; zero, one, the fixed point, and repeated factors have not been discarded. Conversely (DF), (NF), and the displayed Q structure recover the differential formula for J: canceling a nonzero polynomial is valid for an identity over k. Its value at x=0 then supplies `W'(0)=J(0)=1`. The leading ratio from §2 must still be imposed.

The global obstruction is now typed exactly: **no factor M of the prescribed degree, norm leader, and Q shape should satisfy (DF), for all m>=4.** This remains open. Norm factorization is automatic once a divisor is selected; (DF) is not automatic. For example, for `A=x^(m-2)` the polynomial R has at least two distinct nonzero roots (its next-to-leading coefficient is zero and its constant term is -1). Degree-q choices of its root multiset can be swapped at two different roots, changing `W'(0)=sum 1/rho` for W normalized by W(0)=-1. Therefore some choices fail even this marked derivative, while all have the norm factorization and the same complementary degrees. This is a control against declaring the norm/divisor count sufficient, not a target-shaped counterexample or a finite-degree solve.

The prior logarithmic-residue argument only returns the top balance; it was not reused as an obstruction. The new pole lemma is global but does not forbid pole-free solutions. The new norm model keeps rather than resolves the missing differential linkage. No whole-ray exclusion, uniform radical membership, or JC2 conclusion follows here.

## 6. Exact checks and custody

Run `python3 box/k16-boundary-product-20260906/check.py`. Its SHA-256 is
`159431da68c3f73a860bada1e62b377bb75a116ffc1cf84ad16a3c5aef3d47f5`.
It prints eleven PASS markers and `ALL_EXACT_IDENTITY_CHECKS_PASS`: scaling, the rational controls, the origin coefficient, the quadratic norm and inverse maps, the full residual relation, ramification, and the cleared differential filter. These are exact symbolic identities over rational function fields, not sampled numerical or finite-m solution evidence. The valuation arguments above supply the degree-uniform proofs.

No AWS work, heavy CAS, live report/log body, shared-ledger edit, or `jc2-lean` access was used. New files are confined to this transactional report and its owned small checker directory. Source hashes were rechecked before publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11029`.
- Body SHA-256:
  `dd497637ccab6a87bb379633d81eb3e1a5bc3a1180d3cfef1a5e1ee3d77fbc6c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
