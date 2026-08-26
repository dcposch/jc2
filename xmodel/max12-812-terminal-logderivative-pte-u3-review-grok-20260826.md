# Hostile review — terminal logarithmic-derivative moments and complete `U=3`

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-terminal-logderivative-pte-u3-classification-20260826.md` |
| Target SHA-256 | `8e1535aac96785ecf72df6ed22cdd239031d89d82e84fbe0d2078ce6b786c5dc` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. The charged extremal-abc review is same-model and is not used as a PASS/CONFIRMED certificate; the Wronskian formula `W=kappa A B/(rad(A)rad(B))`, equal monic degrees, `deg P=U`, `1<=alpha_i<=m`, `beta_j>=1`, `deg(A-B)=D-U+1` with `G` squarefree, the radicand product, the gcd exactness test, and the charged converse are taken as the *statements* of the charged theorem, then the logarithmic derivative, every residue, the moment identities, the converse, the `U=3` normal forms, and both exact lists are re-derived below from those statements alone |
| Method | source reading and hand derivation only; SHA-256 of the target and the two named parents; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named producer artifact uncommitted) |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `8e1535aac96785ecf72df6ed22cdd239031d89d82e84fbe0d2078ce6b786c5dc`, matching the launch pin. Both charged sources match the hashes printed in the target's Charged theorem section. Producer verdict language, the target's own status line, the coordinator summary, and any prior PASS/CONFIRMED token were not used as evidence. No file other than this review was written.

---

## Verdict

The charged corollary is correct as a terminal logarithmic-derivative / weighted-moment reformulation of the already licensed extremal-abc theorem, together with a complete affine classification at `U=3`. Independently: dividing `W=kappa A B/P` by `A B` yields `T'/T=kappa/P=sum_i n_i/(x-c_i)` with the displayed sign convention and no leftover principal part; the expansion at infinity of both sides forces the power sums through degree `U-2` to vanish and identifies `kappa` as the degree-`U-1` moment; the residue of `kappa/P` at a simple root of the monic squarefree `P` is `kappa/P'(c_i)`, hence `P'(c_i)=kappa/n_i`; the converse recovers equal monic degrees from the `k=0` moment, a nonzero constant numerator from the remaining moments plus uniqueness of partial fractions, exact degree `deg(A-B)=D-U+1` from the leading term of `T-1` at infinity, and squarefreeness of `A-B` from `T'!=0` on `{T=1}` finite; no omitted noncollision, nonzero-moment, scalar, degree, or separability hypothesis breaks a numbered claim. For `U=3` the only moment equations are `sum n_i=0` and `sum n_i c_i=0`; after affine normalization each sign type has a unique support, with pole locations `b/(a+b)` and `-b/c`, and permutations within each sign class account for every duplicate. The exact order-two census is three affine classes and the exact order-four census is ten; every displayed `D`, every radicand multiplicity including exponent-zero uncharged zeros, and every gcd exclusion re-derives. What is finite at fixed `U` is the set of signed integer profiles and a square algebraic presentation of the support after affine gauge; reducedness and a finite set of geometric points are proved only for `U=3`, and are not claimed as a geometric census for general `U`. Passing these identities does not solve another Faber tail, produce Taylor polynomiality, a Keller pair, a whole leaf, `(8,12)`, a bound on all `U`, or JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-terminal-logderivative-pte-u3-classification-20260826.md` | `8e1535aac96785ecf72df6ed22cdd239031d89d82e84fbe0d2078ce6b786c5dc` | target (matches required pin) |
| `xmodel/max12-812-nontrivial-terminal-extremal-abc-classification-20260826.md` | `149691f1784ffccea9473a63efaec4a7d0eea56f9c1e1ba267610b104022920e` | charged extremal-abc theorem: `W=kappa A B/(rad(A)rad(B))`, equal monic degrees, `U>=2`, `deg G=D-U+1`, `G` squarefree, radicand product, gcd exactness, charged converse |
| `xmodel/max12-812-nontrivial-terminal-extremal-abc-review-grok-20260826.md` | `b9cf307094a3128ae459714d6a84e49d4f004308d97b5d5b8298afb1e300b149` | same-model audit of the charged theorem (read; unused as a verdict) |

Both parent hashes match the target's Charged theorem block. The charged theorem is consumed only for the rewritten triple `T=A/B`, `G=A-B`, `W=kappa A B/(rad(A)rad(B))` with `A,B` coprime monic of common degree `D`, `P=rad(A)rad(B)` of degree `U=r+s`, multiplicities `1<=alpha_i<=m` and `beta_j>=1`, `deg G=D-U+1` with `G` squarefree (constants allowed), the radicand formula, exact order `m` iff `gcd(m,all alpha_i, all beta_j)=1`, the degree box `U-1<=D<=m(U-1)`, and the charged converse reconstructing only the terminal equation. Its passport language, Riemann--Hurwitz saturation, and enumerator `(7.1)` are not inputs to any new identity below, except that the degree box is reused as the reason there are finitely many integer profiles. No scope-firewall sentence of either parent is an input.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field after the already licensed finite constant extension. Let `m in {2,4}` be the exact Kummer order, and let `A,B` be as in the charged extremal-abc theorem: coprime monic of common degree `D>=1`, `U>=2`, `T=A/B`, `G=A-B`, `P=rad(A)rad(B)` monic of degree `U`, and `W=kappa A B/P` with `kappa!=0`. Write `c_1,...,c_U` for the distinct roots of `P` and

```text
n_i =  alpha_i     if c_i is a zero of A,
n_i = -beta_i      if c_i is a zero of B.
```

Then the `n_i` are nonzero integers, the positive ones are at most `m`, and

```text
T'/T = kappa/P = sum_i n_i/(x-c_i),
sum_i n_i c_i^k = 0                 for 0<=k<=U-2,
kappa = sum_i n_i c_i^(U-1) != 0,
P'(c_i) = kappa/n_i                 for every i.
```

Conversely, `U>=2` distinct points `c_i` in an algebraic closure and nonzero signed integer weights `n_i` satisfying the displayed power-sum vanishing, with every positive weight at most `m`, determine coprime monic polynomials

```text
A = product_(n_i>0) (x-c_i)^{n_i},
B = product_(n_i<0) (x-c_i)^{-n_i}
```

of a common degree `D>=U-1`, a map `T=A/B` with the same logarithmic derivative, `deg(A-B)=D-U+1`, and `A-B` squarefree (a nonzero constant allowed). This recovers the charged triple, and if additionally `gcd(m, all n_i)=1` the charged radicand formula produces an exact order-`m` terminal solution. The converse reconstructs only the terminal differential equation.

For `U=3`, every such signed multiplicity profile has one and only one support up to affine source change `x |-> p x+q` with `p!=0` and permutations among equal-sign points. The two sign types have unique normal forms

```text
T_(a,b)(x) = x^a (x-1)^b / (x - b/(a+b))^{a+b},
             1<=a,b<=m, gcd(m,a,b)=1 for exactness,
S_(b,c)(x) = x^{b+c} / ((x-1)^b (x + b/c)^c),
             1<=b,c, b+c<=m, gcd(m,b,c)=1 for exactness,
```

the unordered pair determining the affine class in each type. The exact order-two affine classes are the three rows `(1,1|-2)`, `(1,2|-3)`, `(2|-1,-1)`. The exact order-four affine classes are the ten rows `(1,1|-2)`, `(1,2|-3)`, `(1,3|-4)`, `(1,4|-5)`, `(2,3|-5)`, `(3,3|-6)`, `(3,4|-7)`, `(2|-1,-1)`, `(3|-1,-2)`, `(4|-1,-3)`. Their radicand profiles, including every exponent-zero uncharged zero of `T`, are the displayed ones.

At each fixed `U>=2` there are finitely many signed integer profiles, because `U-1<=D<=m(U-1)` together with `r+s=U` and `1<=alpha_i<=m`. After affine gauge, each profile presents as `U-2` support coordinates subject to the `U-2` moment equations of degrees `1` through `U-2`. That is a finite list of profiles and a square algebraic solution scheme. It is not a theorem that the scheme is reduced, nor that it is zero-dimensional, nor that the set of geometric points is finite, except in the case `U=3` where uniqueness of support is proved above.

This is only the terminal differential equation. It does not produce another Faber tail, Taylor polynomiality, a Keller pair, a whole Kummer leaf, `(8,12)`, a bound on all `U`, or JC2.

---

## Attack 1 — `T'/T=kappa/P`, residues, moments, `kappa`, and `P'(c_i)`

**CONFIRMED.** Every sign and the infinity convention survive.

Work over an algebraic closure of a characteristic-zero field, as licensed. The charged theorem supplies coprime monic `A,B` of equal degree, `P=rad(A)rad(B)` monic of degree `U=r+s` with distinct finite roots `c_1,...,c_U`, and

```text
W = A'B - A B' = kappa A B / P,       kappa != 0.
```

The radical is the monic squarefree kernel, so `P` is monic and separable. Characteristic zero is used throughout: integers `n_i` remain nonzero in `L`, derivatives drop order by exactly one, and `U-1!=0`.

**Logarithmic derivative.** In characteristic zero, `T=A/B` differentiates as `T'=W/B^2`. Therefore

```text
T'/T = (W/B^2) * (B/A) = W/(A B) = kappa/P.
```

There is no sign ambiguity in this line: the charged Wronskian is `A'B-AB'`, and `T'=W/B^2` is the quotient rule. The competing formula `T'/T=A'/A-B'/B` is the same identity rewritten. If `A=prod_i (x-a_i)^{alpha_i}` and `B=prod_j (x-b_j)^{beta_j}` in monic coordinates, logarithmic differentiation in characteristic zero gives

```text
A'/A = sum_i alpha_i/(x-a_i),       B'/B = sum_j beta_j/(x-b_j),
```

hence

```text
A'/A - B'/B = sum_i alpha_i/(x-a_i) - sum_j beta_j/(x-b_j).
```

The signed weights `(1.1)` are exactly these residues: `+alpha` at a zero of `A`, `-beta` at a zero of `B`. This is `(1.2)`. The opposite convention `sum n_i/(c_i-x)` would flip every residue and then flip `kappa`; the target uses the standard meromorphic form whose residue at a point is the order of `T` there. Coprimality of `A` and `B` makes the two supports disjoint, so there is no cancellation of residues and no point with `n_i=0`.

**Partial fractions of `kappa/P`.** `P` is monic of degree `U` with distinct roots, so

```text
kappa/P(x) = sum_i [kappa / P'(c_i)] * 1/(x-c_i).
```

The residue formula `Res_{c_i}(1/P)=1/P'(c_i)` uses simplicity of the roots and no extra sign: locally `P(x)=(x-c_i) Q_i(x)` with `Q_i(c_i)=P'(c_i)!=0`. Identifying with `(1.2)` gives `n_i=kappa/P'(c_i)`, which is `(1.5)`. Equivalently `n_i P'(c_i)` is independent of `i` and equal to `kappa`. If some `P'(c_i)` vanished, `P` would not be separable, contradicting distinct `c_i`.

**Expansion at infinity.** The correct local coordinate at infinity is `x^{-1}`, not the expansion at `0`. For each finite `c_i`,

```text
1/(x-c_i) = x^{-1} (1 - c_i x^{-1})^{-1} = sum_{k>=0} c_i^k x^{-k-1},
```

as a formal Laurent series in `x^{-1}`, valid whether or not `c_i=0`. (The competing expansion `1/(x-c_i)= -c_i^{-1} sum (x/c_i)^k` is the expansion at the origin and is undefined at `c_i=0`; it is the wrong chart.) Therefore

```text
sum_i n_i/(x-c_i) = sum_{k>=0} (sum_i n_i c_i^k) x^{-k-1}.
```

On the other side `P` is monic of degree `U`, so `P(x)=x^U (1+O(x^{-1}))` and

```text
kappa/P = kappa x^{-U} (1+O(x^{-1})) = kappa x^{-U} + O(x^{-U-1}).
```

The coefficient of `x^{-U}` on the right is exactly `kappa`: lower terms of `P` contribute only from `x^{-U-1}` onward. Comparing coefficients of `x^{-1},...,x^{-(U-1)}` on the left against zero on the right yields

```text
sum_i n_i c_i^k = 0       for 0 <= k <= U-2.
```

The coefficient of `x^{-U}` yields `kappa=sum_i n_i c_i^{U-1}`. This is nonzero because `kappa!=0` is charged. This is `(1.3)`--`(1.4)`.

**Residue at infinity, as a sign check.** The sum of residues of `(T'/T)\,dx` on `P^1` vanishes. The finite residues are the `n_i`, already summing to zero by the `k=0` moment, so the residue at infinity is zero. In the local coordinate `z=1/x` one has `dx=-z^{-2} dz` and `T'/T=kappa x^{-U}+O(x^{-U-1})`, hence `(T'/T)\,dx = -kappa z^{U-2}\,dz + higher`. For `U>=2` there is no `dz/z` term, confirming residue zero rather than a hidden `log x` in `log T`. The `k=0` vanishing is exactly the statement that `T` has neither a zero nor a pole at infinity, which the charged equal-degree normalization already encodes as `T(infinity)=1`.

**What would have flipped this attack.** A Wronskian of opposite sign; taking residues of `1/prod(c_i-x)` rather than `1/prod(x-c_i)`; expanding at `0` instead of `infinity`; taking `P` non-monic so that the leading coefficient of `kappa/P` is not `kappa`; or characteristic dividing some `n_i` so that a residue of `A'/A` vanished.

---

## Attack 2 — converse: equal degrees, constant numerator, `deg G=D-U+1`, squarefreeness

**CONFIRMED.** The stated hypotheses suffice. No omitted noncollision, nonzero-moment, scalar, degree, or separability hypothesis breaks a numbered claim.

Take `U>=2` distinct points `c_i` and nonzero signed integer weights `n_i` satisfying `(1.3)`, with every positive weight at most `m`. Define `A,B` by `(1.6)`. Characteristic zero is standing.

**Noncollision and both signs.** Distinctness of the `c_i` is a stated hypothesis, so `A` and `B` have disjoint supports and are coprime, and `P:=prod(x-c_i)` is monic separable of degree `U`. The `k=0` equation `sum n_i=0` together with nonzero integer weights forces both signs to appear: a one-sided tuple of nonzero integers cannot sum to zero. Empty products therefore do not occur, and `D:=sum_{n_i>0} n_i = sum_{n_i<0} (-n_i)` is an integer at least `1`.

**Equal monic degrees.** Formula `(1.6)` makes `A` and `B` monic by construction. The `k=0` moment says the total positive weight equals the total negative weight, so `deg A=deg B=D`. This is the first sentence of the converse proof.

**Constant numerator, and `kappa!=0` without a separate hypothesis.** Write

```text
sum_i n_i/(x-c_i) = N(x)/P(x),       N(x)=sum_i n_i prod_{j!=i}(x-c_j).
```

`N` is a polynomial of degree at most `U-1`, with leading coefficient `sum n_i`. The `k=0` moment already drops that leading coefficient, so `deg N<=U-2`. The remaining equations of `(1.3)` say that the expansion of `N/P` at infinity has vanishing coefficients of `x^{-1}` through `x^{-(U-1)}`, hence begins at `x^{-U}`. A ratio of a polynomial of degree at most `U-1` by a monic polynomial of degree `U` has expansion beginning at `x^{-U}` if and only if `N` is constant. That constant is the coefficient of `x^{-U}`, which is `sum_i n_i c_i^{U-1}`. Call it `kappa`. If this constant vanished then `N equiv 0`, so `sum n_i/(x-c_i)=0` as a rational function, hence every residue `n_i=0` by uniqueness of partial fractions, contradicting nonzero weights. Equivalently: vanishing of all `U` moments of degrees `0` through `U-1` is a Vandermonde system in the `U` distinct nodes `c_i`, hence forces `n=0`. Thus `(1.4)` is a conclusion from `(1.3)` plus distinct nodes plus not-all-zero weights, not a missing hypothesis. This proves `(1.2)` in the converse direction.

**Exact degree of `G`.** Equal monic degrees give `T(infinity)=1`. From Attack 1, `T'/T=kappa x^{-U}+O(x^{-U-1})`. There is no `x^{-1}` term, so the formal logarithm at infinity has no `log x` and is fixed by `log T(infinity)=0`:

```text
log T = integral (kappa x^{-U}+O(x^{-U-1})) dx
      = -kappa/(U-1) x^{-(U-1)} + O(x^{-U}),
```

using `U>=2` so that `U-1!=0` in characteristic zero. Then `T=exp(log T)=1+log T+O((log T)^2)`. The square `(log T)^2` has valuation `2(U-1)` at infinity, and `2(U-1)>=U` for `U>=2`, with equality only at `U=2`. In all cases the square (and higher) contributes only to the error `O(x^{-U})`, never to the leading term of `T-1`. Thus

```text
T-1 = -kappa/(U-1) x^{-(U-1)} + O(x^{-U}),
```

with leading coefficient `-kappa/(U-1)!=0`. Now `G=A-B=B(T-1)` is a polynomial of degree at most `D`, and the displayed expansion gives valuation exactly `-(D-(U-1))` at infinity. Hence `deg G=D-U+1` exactly. In particular this degree is a nonnegative integer: if `D<U-1` the expansion of the polynomial `G` would vanish at infinity, forcing `G equiv 0`, hence `T equiv 1`, hence `kappa=0`, a contradiction. So `D>=U-1` is a conclusion, not a missing degree hypothesis, and the constant-`G` edge `D=U-1` is included.

**Squarefreeness of `G`.** Let `c` be a finite root of `G`. Then `A(c)=B(c)`. This common value cannot be `0`, or `c` would be a common root of the coprime polynomials `A,B`. Thus `T(c)=1`, and `c` is not among the `c_i`, so `P(c)!=0`. Formula `(1.2)` gives `T'(c)=T(c)*kappa/P(c)=kappa/P(c)!=0`. A multiple root of `G` would be a multiple root of `T-1=G/B` (since `B(c)!=0`), hence a zero of `T'`. Contradiction. Every finite root of `G` is therefore simple. If `G` has no finite root then `deg G=0`, `G` is a nonzero constant, and squarefreeness holds by the charged convention already licensed for `D=U-1`. This is `(1.7)`.

**Recovery of the charged triple.** The identity `W=A B T'/T` together with `(1.2)` rewrites as `W=kappa A B/P`. The multiplicities of `A` are the positive `n_i`, at most `m` by hypothesis; the multiplicities of `B` are the absolute values of the negative `n_i`, at least `1` because the weights are nonzero integers. Combined with `(1.7)` this is the charged `(0.5)` plus `(0.6)`. The charged converse then produces a polynomial radicand of degree `m U` solving the terminal identity, and the gcd condition `(0.2)` of the target (which is `(0.11)` of the charged theorem) makes the Kummer order exact. The last sentence of Theorem 1 correctly restricts this reconstruction to the terminal differential equation.

**Hypotheses checked for omission.**

- *Noncollision.* Distinct `c_i` is stated. Without it `P` would drop degree and `(1.5)` would divide by zero.
- *Nonzero weights.* Stated. Without it a point with `n_i=0` would be an uncharged interpolation node not present in `A` or `B`, and `deg P` would not equal `U`.
- *Nonzero moment `kappa`.* Not listed as a converse hypothesis; derived from Vandermonde / uniqueness of partial fractions, as above. Listing it would be redundant, omitting it is not a gap.
- *Scalar.* `A,B` are constructed monic, `T(infinity)=1`, and `kappa` is the constant numerator. No further scalar is required to recover `W=kappa A B/P`. Matching the charged constant `C=(m j/8)^m` remains the harmless normalization already present in the charged converse.
- *Degree.* Equal degrees are derived from `k=0`; `D>=U-1` is derived from `(1.9)` plus polynomiality of `G`; `deg G=D-U+1` is derived from the leading term of `T-1`. None of these is a missing input.
- *Separability of `G`.* Proved, not assumed. Separability of `A` or `B` is not required: multiple roots are the data `n_i`.
- *Positive weights at most `m`.* Not needed for `(1.2)` or `(1.7)` alone, but needed for polynomiality of the charged radicand and for the last sentence of Theorem 1. Including it in the converse statement matches the charged universe (`alpha_i<=m`) and is not an extra restriction on terminal maps. Negative weights are correctly left unbounded except through `D<=m(U-1)`.
- *At least one weight of each sign.* Follows from `sum n_i=0` and nonzero integers, as above.

**What would have flipped this attack.** Omitting distinctness so that two opposite-sign weights collide and cancel; a converse that allowed `kappa=0` as a genuine extra solution rather than the zero-weight tuple; a proof of `deg G=D-U+1` that used `D>=U-1` as an unstated input rather than a conclusion; a multiple root of `G` compatible with `T'!=0`; or characteristic dividing `U-1` so that the integral of `x^{-U}` became a logarithm.

---

## Attack 3 — complete `U=3` classification up to affine source change

**CONFIRMED.** Both normal forms, uniqueness, both pole locations, and the accounting of duplicates by same-sign permutations survive.

For `U=3` the system `(1.3)` is two equations, `sum n_i=0` and `sum n_i c_i=0`. The degree-two moment is `kappa`, required nonzero. The affine group `x |-> p x + q` with `p!=0` is the correct source automorphism: it is the stabilizer of infinity in `PGL(2)`, and infinity is distinguished by the charged normalization `T(infinity)=1` (all zeros and poles of `T` are finite). A Möbius sending a finite support point to infinity would break equal degrees and is not licensed.

Because both signs appear and there are three nonzero weights, the only combinatorial types are two positives and one negative, or one positive and two negatives.

**Two zeros and one pole.** Write the weights as `(a,b,-(a+b))` with `a,b` positive integers at most `m`. Send the two zeros to `0` and `1` by an affine map (translate one to `0`, then scale the other to `1`; the two points are distinct). Let the pole be `t`. The `k=1` moment reads

```text
a*0 + b*1 + (-a-b) t = 0,       t = b/(a+b).
```

Collision with `0` is `b=0`; collision with `1` is `a=0`. Both are forbidden. In characteristic zero the three points `0,1,b/(a+b)` are therefore distinct, with no extra noncollision hypothesis. The degree-two moment is

```text
kappa = b - (a+b) (b/(a+b))^2 = a b/(a+b) != 0,
```

so the configuration is nondegenerate. This is `(2.1)`. Swapping the two zeros is the affine map `x |-> 1-x`, which sends `t=b/(a+b)` to `1-t=a/(a+b)` and swaps `(a,b)`. Thus the unordered pair `{a,b}` determines the affine class, and the ordered pair with `a!=b` is counted once. If `a=b` then `t=1/2` and `x |-> 1-x` is an extra symmetry of the same labelled profile, not a second class. Exactness is `gcd(m,a,b,a+b)=gcd(m,a,b)=1`, as stated.

**One zero and two poles.** Write the weights as `(b+c,-b,-c)` with `b,c` positive integers and `b+c<=m` (the unique positive weight is an `alpha`, hence at most `m`). Send the zero to `0` and one pole to `1`. Let the second pole be `t`. The `k=1` moment reads

```text
(b+c)*0 + (-b)*1 + (-c) t = 0,       t = -b/c.
```

Collision with `0` is `b=0`; collision with `1` is `b+c=0`. Both are forbidden in characteristic zero, so `0,1,-b/c` are distinct. The degree-two moment is

```text
kappa = -b - c (b/c)^2 = -b(b+c)/c != 0.
```

The denominator factor `x-t=x+b/c` produces `(2.2)`. Swapping the two poles is the scaling that sends `-b/c` to `1` and `1` to `-c/b`, exchanging `{b,c}`. The unordered pair `{b,c}` determines the affine class. Exactness is `gcd(m,b+c,b,c)=gcd(m,b,c)=1`, as stated.

The alternative affine chart that sends the two poles to `0,1` places the zero at `c/(b+c)`. That chart is affine-equivalent to `(2.2)`: the map `x |-> -c/(b+c) x + c/(b+c)` sends `{0,1,-b/c}` to `{c/(b+c), 0, 1}`. It is a second presentation of the same class, not a third sign type. Likewise `1/T_(a,b)` is a one-zero two-pole rational function, but substituting `S=1/T` into the charged identity produces `d (S')^m = C S^{m+1}`, a different equation. Source affine transformations do not swap zeros of `T` with poles of `T`. The two sign types are disjoint.

**Exhaustiveness and uniqueness.** After the `k=0` constraint on weights, the only remaining moment is linear in the three points. The affine group has two parameters, so each ordered weight triple has a unique support modulo affine transformations, provided the three points remain distinct and `kappa!=0`, both of which hold in characteristic zero for every positive integer solution of the sign-type bounds. Permutations among equal-sign points are the only residual labelling automorphisms, and they are already quotiented by using unordered pairs. No other sign pattern exists for three nonzero integers summing to zero. No degenerate (colliding or vanishing-`kappa`) case enters the list.

---

## Attack 4 — independent census of exact order two and exact order four

**CONFIRMED.** The claimed totals `3` and `10` are exact. Every `D`, every radicand multiplicity including exponent-zero uncharged zeros, and every gcd exclusion re-derives. There is no wrong row.

The charged radicand, up to its nonzero scalar, is

```text
d = c prod_{n_i>0} (x-c_i)^{m-n_i} prod_{n_i<0} (x-c_i)^{m-n_i},
```

i.e. exponent `m-alpha` at a zero of `T` and exponent `m+beta` at a pole of `T`. The profile records the positive exponents. An exponent zero occurs precisely when `alpha=m`, which is an uncharged zero of `T` of order `m`, and is written as such rather than as a part `0`. Poles have exponent `m+beta>=m+1>0` and are never uncharged. The degree is `m U`, hence `6` for `m=2` and `12` for `m=4` at `U=3`. Exactness is `gcd(m, all parts of A and of B)=1`. The degree box is `2<=D<=2 m`.

**Order two, two zeros / one pole.** Unordered pairs `{a,b}` with `1<=a,b<=2`:

| `{a,b}` | weights | `gcd(2,a,b)` | keep? | `D` | radicand exponents |
|---|---|---:|---|---:|---|
| `{1,1}` | `(1,1\|-2)` | `1` | yes | `2` | `2-1=1`, `2-1=1`, `2+2=4` so `[4,1,1]` |
| `{1,2}` | `(1,2\|-3)` | `1` | yes | `3` | `2-1=1`, `2-2=0`, `2+3=5` so `[5,1]` plus one uncharged double zero |
| `{2,2}` | `(2,2\|-4)` | `2` | no | `4` | trivial Kummer class |

Two exact rows, matching the target, including the omitted gcd-two vertex `D=m(U-1)=4`.

**Order two, one zero / two poles.** Unordered pairs `{b,c}` with `b+c<=2`: the only candidate is `{1,1}`, weights `(2\|-1,-1)`, `gcd(2,1,1)=1`, `D=2`. Radicand exponents `2-2=0`, `2+1=3`, `2+1=3`, hence `[3,3]` plus one uncharged double zero. The pair `{1,2}` has sum `3>2` and is excluded by `alpha<=m`, not by gcd. Total exact order-two classes: `2+1=3`.

**Order four, two zeros / one pole.** Unordered pairs `{a,b}` with `1<=a,b<=4`:

| `{a,b}` | weights | `gcd(4,a,b)` | keep? | `D` | radicand |
|---|---|---:|---|---:|---|
| `{1,1}` | `(1,1\|-2)` | `1` | yes | `2` | `[6,3,3]` |
| `{1,2}` | `(1,2\|-3)` | `1` | yes | `3` | `[7,3,2]` |
| `{1,3}` | `(1,3\|-4)` | `1` | yes | `4` | `[8,3,1]` |
| `{1,4}` | `(1,4\|-5)` | `1` | yes | `5` | `[9,3]` plus one uncharged fourth-order zero |
| `{2,2}` | `(2,2\|-4)` | `2` | no | `4` | order two, not four |
| `{2,3}` | `(2,3\|-5)` | `1` | yes | `5` | `[9,2,1]` |
| `{2,4}` | `(2,4\|-6)` | `2` | no | `6` | order two, not four |
| `{3,3}` | `(3,3\|-6)` | `1` | yes | `6` | `[10,1,1]` |
| `{3,4}` | `(3,4\|-7)` | `1` | yes | `7` | `[11,1]` plus one uncharged fourth-order zero |
| `{4,4}` | `(4,4\|-8)` | `4` | no | `8` | order one; the vertex `D=m(U-1)` |

Seven exact rows. Exponents independently: `m-a`, `m-b`, `m+(a+b)`, summing to `12` in every kept row. Uncharged zeros occur exactly on `{1,4}` and `{3,4}`, where one part equals `m=4`.

**Order four, one zero / two poles.** Unordered pairs `{b,c}` with `b+c<=4`:

| `{b,c}` | weights | `gcd(4,b,c)` | keep? | `D` | radicand |
|---|---|---:|---|---:|---|
| `{1,1}` | `(2\|-1,-1)` | `1` | yes | `2` | `[5,5,2]` |
| `{1,2}` | `(3\|-1,-2)` | `1` | yes | `3` | `[6,5,1]` |
| `{1,3}` | `(4\|-1,-3)` | `1` | yes | `4` | `[7,5]` plus one uncharged fourth-order zero |
| `{2,2}` | `(4\|-2,-2)` | `2` | no | `4` | order two, not four |

Pairs with sum `>=5` violate `alpha<=m`. Three exact rows. Note that `(2\|-1,-1)` at `m=4` has `alpha=2<4`, so the exponent `4-2=2` is a genuine part of `d` and is *not* an uncharged zero; the target correctly writes `[5,5,2]` with no uncharged annotation. Total exact order-four classes: `7+3=10`.

The omitted list in the target — two-zero `(2,2)`, `(2,4)`, `(4,4)` and one-zero `(2,2)` — is exactly the gcd-four filter, and the order-two omitted profile is exactly `(2,2\|-4)`. No row is missing, no row is extra, no `D` is off by one, no radicand part is transposed, and no exponent-zero uncharged zero is either dropped or wrongly inserted (in particular the charged zero of order `2` on the order-four row `(2\|-1,-1)` is kept as the part `2`). The thirteen affine classes named in the computational paragraph are `3+10`.

**Smallest wrong row.** None.

---

## Attack 5 — what is finite at fixed `U`

**CONFIRMED**, with the finiteness claim read as a finite list of profiles plus a square algebraic presentation, not as a geometric census.

The computational paragraph asserts that for fixed `U`, `(1.3)` is a finite exact system after affine normalization, because there are finitely many signed integer profiles (`U-1<=D<=m(U-1)`) and each profile has `U-2` support variables and `U-2` moment equations.

**Profiles are finite.** This is exact. A profile is a tuple of `U` nonzero integers, `r` of them positive and at most `m`, `s=U-r` of them negative, summing to zero, with common absolute sum `D` in the charged box `U-1<=D<=m(U-1)`. There are finitely many such tuples, and the gcd filter is a further finite cut. The degree box is a statement of the charged theorem, consumed here only as a bound on `D`.

**The algebraic presentation is square after affine gauge.** The identities `(1.3)` are affine-invariant: translation leaves every moment of degree `>=1` unchanged because `sum n_i=0`, and scaling multiplies the degree-`k` moment by `p^k`, so vanishing is preserved. One may therefore fix two affine gauges (for instance send one marked point to `0` and another to `1`, or kill the barycentre and a scale). This leaves `U-2` support coordinates. The `k=0` moment constrains only weights and is already imposed on the profile. The remaining moments `k=1,...,U-2` are `U-2` polynomial equations. That count is correct as a presentation, not as a dimension computation.

**What is not proved, and is not claimed as a geometric theorem.** Square-ness of a presentation does not imply that the scheme is a finite set of reduced points. The `U-2` equations may be dependent, may cut a positive-dimensional locus, or may be non-reduced. The target does not assert reducedness, does not assert zero-dimensionality, and does not assert a finite set of geometric points for general `U`. The sentence “finite exact system” is immediately glossed by the two facts above (finite profiles, square presentation), and the next sentence calls the result a smaller frontend for enumerating terminal clients than unrestricted coefficients of `A,B`. That comparison is about the shape of the input, not about a completed census.

For `U=3` the scheme *is* a finite set of reduced points: Attack 3 gives a unique support per profile, with `kappa!=0` and no collision. That is a separate theorem, and is the only place a geometric finiteness statement is used.

Reading “finite exact system” as “finitely many geometric solutions at every `U`” would be an overclaim, and is not the claim the paragraph makes once the colon-expansion is included. No numbered theorem is broken. The corrected strongest statement, already given above, is the one that names profiles and a square algebraic solution scheme as the finite objects, and isolates geometric uniqueness at `U=3`.

---

## Attack 6 — firewall

**CONFIRMED**, with one non-blocking campaign sentence named below.

Every numbered conclusion stays inside the terminal differential equation. Theorem 1 states that its converse reconstructs only that equation. The `U=3` list is a list of terminal maps, i.e. of solutions of `T'/T=kappa/P` with the charged multiplicity bounds and the gcd test. The radicand profiles are the charged formula `(0.10)` evaluated on those maps; they are not a verification of any lower tail.

The computational paragraph's last sentence, “For `U=3`, no CAS is needed; the thirteen displayed clients can be compiled directly into the remaining six Faber tails and both Taylor boundary gates,” names surfaces outside the firewall as a destination for the list. It does not assert that any listed map satisfies another Faber tail, admits Taylor polynomialization, produces a Keller pair, or survives a boundary gate. The immediately following Scope firewall paragraph refuses exactly those promotions, together with closing a Kummer leaf, closing `(8,12)`, bounding all `U`, and JC2. The refusal matches the required boundary. The campaign sentence is not a numbered failure.

No sentence claims that a listed map is a Keller pair, that the `U=3` list closes either nontrivial leaf, that `U` is bounded, or that JC2 is decided.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `T'/T=kappa/P=sum n_i/(x-c_i)`; residues of `kappa/P` are `n_i`; power sums through degree `U-2` vanish; `kappa=sum n_i c_i^{U-1}`; `P'(c_i)=kappa/n_i` | **CONFIRMED** | opposite Wronskian sign; expansion at `0` rather than `infinity`; non-monic `P`; a multiple root of `P`; `char` dividing some `n_i` |
| 2 | Converse: `k=0` forces equal monic degrees; remaining moments force a nonzero constant numerator; `deg(A-B)=D-U+1`; `A-B` squarefree; charged hypotheses recovered; no missing noncollision / nonzero-moment / scalar / degree / separability input | **CONFIRMED** | colliding opposite-sign weights; `N equiv 0` accepted as an extra solution; `D>=U-1` used as an unstated hypothesis rather than a conclusion; a multiple root of `G` with `T'!=0`; `char` dividing `U-1` |
| 3 | `U=3`: unique affine support per profile; normal forms `(2.1)` and `(2.2)`; poles at `b/(a+b)` and `-b/c`; unordered pairs; same-sign permutations account for duplicates; both types nondegenerate in char `0` | **CONFIRMED** | a third sign type; `t=b/(a+b)` colliding with `{0,1}`; `1/T_(a,b)` wrongly identified with `S_(*,*)`; counting ordered pairs `{a,b}` and `{b,a}` as two classes |
| 4 | Exact order two: three affine classes; exact order four: ten; every `D`; every radicand part including exponent-zero uncharged zeros; gcd omissions `(2,2\|-4)` at `m=2` and `(2,2),(2,4),(4,4)` two-zero plus `(2,2)` one-zero at `m=4` | **CONFIRMED** | a missed pair with `alpha<=m` and gcd `1`; `[5,5,2]` wrongly annotated as uncharged; `(2\|-1,-1)` at `m=2` omitting the uncharged double zero; `D` off by one; profile parts not summing to `m U` |
| 5 | Fixed `U`: finitely many integer profiles and a square algebraic presentation after affine gauge; no reducedness or geometric-finiteness theorem for `U>3`; geometric uniqueness only at `U=3` | **CONFIRMED** | a hidden claim that the scheme is zero-dimensional for every `U`; an infinite family of integer profiles inside the degree box |
| 6 | Terminal differential equation only; no other Faber tail, Taylor polynomiality, Keller pair, whole leaf, `(8,12)`, bound on all `U`, or JC2 | **CONFIRMED** | a hidden promotion in Theorem 1, Theorem 2, the explicit lists, or the firewall paragraph |

---

## Remarks (non-blocking)

1. The inequality `D>=U-1` in the converse is a corollary of the leading term of `T-1` together with polynomiality of `G`, not an extra input. The written proof jumps from `(1.9)` to `deg G=D-U+1`; that language already treats the degree as a nonnegative integer and silently includes the constant-`G` edge. Correct, but the constant case is less explicit here than in the charged parent.
2. Nonvanishing of `kappa` in the converse is likewise a corollary (Vandermonde / uniqueness of partial fractions) and is correctly not listed as a hypothesis.
3. The bound “positive weights at most `m`” is superfluous for `(1.2)` and `(1.7)` and necessary for the charged radicand. Including it in the converse statement matches the charged universe of terminal maps.
4. “Finite exact system” can be overread as a zero-dimensional geometric census. The colon-expansion in the same sentence prevents that reading from being a numbered claim. The strongest statement recorded above makes the distinction explicit.
5. The computational sentence that names the six remaining Faber tails and both Taylor boundary gates is campaign language, cancelled by the following refusal paragraph, in the same sense as the charged parent's “bridge to the live coefficient/Taylor clients.”
6. Characteristic zero is essential and present: residues equal the integer orders, `U-1!=0` in the integral, `a,b,a+b` and `b,c,b+c` remain nonzero so the `U=3` supports do not collide, and Vandermonde is invertible.
7. The name “weighted Prouhet--Tarry--Escott” is descriptive of the vanishing of the first `U-1` power sums of a signed atomic measure. It is not used as an external existence theorem.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms a terminal logarithmic-derivative reformulation of the charged extremal-abc theorem, together with a complete affine classification of exact order-two and order-four solutions at `U=3`. It does **not**:

- solve `r_1'=...=r_6'=0` or determine the algebraic fibres of those constants;
- produce the remaining Faber coefficient functions, a rational or polynomial trajectory, either original Taylor-boundary family, a strict Rees boundary, or a Keller pair;
- prove reducedness or geometric finiteness of the moment scheme for `U>3`, bound `U`, realize an arbitrary passport, or lift a passport to the lower Faber fibre;
- close the order-four client, the order-two client, the cell `(8,12)`, maximum twelve, or JC2.

The target's own Scope firewall paragraph matches this boundary. No creep was found in any numbered claim.

---

## Terminal boundary (accepted, not enlarged)

```text
T'/T=kappa/P=sum_n_i/(x-c_i)=PROVED
moments_through_degree_U-2_vanish=PROVED
kappa=sum_n_i c_i^(U-1)=PROVED
P'(c_i)=kappa/n_i=PROVED
converse_equal_monic_degrees_constant_numerator=PROVED
deg(A-B)=D-U+1_and_G_squarefree=PROVED
U=3_two_normal_forms_unique_affine_support=PROVED
pole_locations_b/(a+b)_and_-b/c=PROVED
exact_order_two_three_classes=PROVED
exact_order_four_ten_classes=PROVED
radicand_profiles_including_uncharged_zeros=PROVED
fixed_U_finite_profiles_and_square_scheme=PROVED
fixed_U_geometric_finiteness_for_U>3=NOT_CLAIMED
other_six_tails=NOT_SOLVED
Taylor_polynomiality=NOT_CLAIMED
U_bounded=NOT_CLAIMED
any_Kummer_leaf_closed=false
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```
