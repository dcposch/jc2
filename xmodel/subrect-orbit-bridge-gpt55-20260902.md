# SUBRECT-ORBIT-BRIDGE -- degree-minimal pairs and the subrectangular gauge

Lane: `SUBRECT-ORBIT-BRIDGE`. Date: 2026-09-02. Agent: GPT-5.5.
Scope: frozen inputs only, local `refs/`, desk algebra; no web, no canonical
ledger edit, no `jc2-lean`. No exit-price assertion is made, so there is no
`charge_basis` line.

## 0. Custody

The charged frozen inputs were hashed before reading. All matched:

```text
7b0ffec769314ce91a0831f7b2a88f5d5c8c97c08bfa56bd1e9bb8dbfb5c23f0  minimal-keller-shape-opus5-20260902.md
b1e09351164c134ec8aa74a7b905678e70021155b23add5bec9994e9f1268ac1  minimal-keller-shape-review-gpt55-20260902.md
bf1d428c7ddc03ab002410174b995cdd01e8a3c76c52475b03faf959b33da2ca  integration14-coordinator-fable51-20260902.md
```

Primary local reference:

```text
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
```

Auxiliary checked reports for controls:

```text
64a4ebd6246d095bf75d7fab50f20e815f3f0ba729c5713071eda95dbdcd22e7  xmodel/polar-chain-n4-grok46-20260902.md
4ad3e2211a7008359781ab2f17955c67c1c22458fbb0c5bbb3adffd9850024e8  xmodel/b3-census-deg5-deg6-sol56-20260902.md
```

Citation shorthand: `GGV` is Jorge A. Guccione, Juan J. Guccione, and
Christian Valqui, "On the shape of possible counterexamples to the Jacobian
Conjecture", J. Algebra 471 (2017), local PDF above, arXiv:1401.1784v3.

## 1. Verdict

`OPEN[SUBRECT-ORBIT-BRIDGE]` is closed **YES**, under the campaign meaning that
`F_min` is minimal for `D=max(deg P,deg Q)` inside its full `Aut(C^2) x
Aut(C^2)` orbit. Every such degree-minimal counterexample admits the GGV
standard subrectangular gauge preserving both coordinate degrees. In fact, the
GGV source automorphism that supplies the subrectangular shape must be affine
linear; otherwise its inverse would prove that the original pair was not
degree-minimal.

Consequently the bounded quantity is decided:

```text
nu(F_min) = 2.
```

So neither `nu=1` nor `nu>=3` can occur at an `Aut x Aut` degree-minimal
counterexample representative. Integration #14's `E_0`-free conclusion and the
vacuity of CH2 are unconditional at every geometric degree `N`, after reading
the result in this degree-minimal scope.

Important separation: the short argument "linear change plus (LF)" is **not**
valid by itself for arbitrary `H` with at least two distinct roots. A linear
change preserves the number of reduced roots of a binary form in `P^1`. It can
send two chosen roots to `x=0` and `y=0`, but it cannot turn three or more
roots into `x^u y^v`. The bridge is closed only after adding the
GGV/Makar-Limanov subrectangularization and replacing GGV's global-`B`
minimality step by orbit degree-minimality.

## 2. GGV's Theorem, Precisely

GGV Section 4 defines

```text
B = infinity, if JC is true;
B = min gcd(v_11(P),v_11(Q)), if JC is false,
    where (P,Q) runs over all counterexamples.
```

A **minimal pair** in GGV means a counterexample with
`gcd(v_11(P),v_11(Q))=B`. This is global minimality over all counterexamples,
not minimality inside one `Aut x Aut` orbit.

GGV Definition 4.3: for coprime `m,n>1`, an `(m,n)`-pair is a Jacobian pair
`(P,Q)` in `L(l)` such that

```text
v_11(P)/v_11(Q) = v_10(P)/v_10(Q) = m/n,
v_(1,-1)(en_10(P)) < 0.
```

It is **standard** if `P,Q in L` and `v_(1,-1)(st_10(P))<0`.

The subrectangular input appears in the proof of Proposition 4.7: for any
counterexample, van den Essen Cor. 10.2.21, following Makar-Limanov, gives a
source automorphism `phi` and integers `1<=a<=b` with

```text
(a,b) in Supp(phi(P)) subset { (i,j): 0<=i<=a, 0<=j<=b }.
```

GGV then uses Theorem 2.6(4) to get `a<b`, proves the aligned support relation
for `Q`, and obtains an `(m,n)`-pair. Proposition 4.7, as printed, assumes
`(P,Q)` is a GGV-minimal pair and concludes that some source automorphism
produces an `(m,n)`-pair while preserving both `v_11(P)` and `v_11(Q)`, with
successor directions between `(-1,1)` and `(-1,0)`.

Proposition 5.20 then standardizes an `(m,n)`-pair in `L` by an automorphism
preserving `v_11(P)`, `v_11(Q)`, and `en_10(P)`. Corollary 5.21 is the exact
GGV theorem used by Integration #14: if JC is false, there exists a Jacobian
pair `(P,Q)` and coprime `m,n>1` such that `(P,Q)` is a standard `(m,n)`-pair in
`L`, is GGV-minimal, satisfies `st_11(P)=en_10(P)`, and has the successor
inequalities.

Where GGV uses global `B`: in Proposition 4.7, after putting
`(Pbar,Qbar)=(phi(P),phi(Q))`, GGV sets `psi=phi^{-1}`. If `psi` is nonlinear,
Jung-van der Kulk gives either `deg psi(x) | deg psi(y)` or conversely; in the
first case, writing `l_11(psi(x))=R` and `l_11(psi(y))=lambda R^k`, GGV computes
that the original pair has

```text
v_11(P) = m v_11(R) (abar + k bbar),
v_11(Q) = n v_11(R) (abar + k bbar),
```

where the subrectangular pair has

```text
v_11(Pbar) = m (abar + bbar),
v_11(Qbar) = n (abar + bbar).
```

GGV uses the fact that the original gcd is the global minimum `B` to force
equality and hence `k=1`, `v_11(R)=1`, contradicting nonlinearity. GGV also uses
its minimal-pair Remark 4.2 to exclude degree divisibility and get `m,n>1`.

## 3. Replacement by Orbit Degree-Minimality

Let `(P,Q)=F_min` be a counterexample minimizing `D=max(deg P,deg Q)` in its
`Aut x Aut` orbit. Apply the same Makar-Limanov/vdE source automorphism `phi`
used in GGV Proposition 4.7, before any appeal to global `B`.

If `psi=phi^{-1}` is nonlinear, the displayed GGV computation gives

```text
deg P  > deg phi(P),     deg Q > deg phi(Q).
```

Indeed `v_11(R)>=1` and either `k>1` or `v_11(R)>1`; since `abar,bbar>0`,
`v_11(R)(abar+k bbar) > abar+bbar`. Therefore

```text
max(deg phi(P), deg phi(Q)) < max(deg P, deg Q),
```

contradicting the defining minimality of `F_min`. Thus `psi`, and hence `phi`,
is affine linear. Affine linear source changes preserve total degree of each
coordinate, so the subrectangular gauge preserves both degrees.

The exclusion `m,n>1` also does not need global `B` in this orbit-minimal
setting. If one of `m,n` is `1`, or if the two degrees are equal, the elementary
target cancellation from `(LF)` lowers `D`; this is the usual `(MIN)` step and
contradicts `Aut x Aut` degree-minimality.

Proposition 5.20's standardization is degree-preserving already: in the relevant
case it keeps the `(1,1)` leading forms and is given by `x -> x`, `y -> y+lambda`.
Thus every orbit degree-minimal counterexample has a degree-preserving standard
subrectangular GGV gauge.

## 4. Top Form and Root Count

In the subrectangular gauge, `(a,b) in Supp(P)` and every support point of `P`
lies in the rectangle `0<=i<=a`, `0<=j<=b`. The only point of that rectangle
with total degree `a+b` is `(a,b)`. Hence

```text
l_11(P) = c x^a y^b.
```

For a Jacobian counterexample, `(LF)` gives

```text
l_11(P) = alpha H^d,     l_11(Q) = beta H^e,
gcd(d,e)=1,              deg H = gcd(deg P,deg Q).
```

Therefore `H=c' x^u y^v` with `u=a/d`, `v=b/d`. Since GGV has `a,b>0`,
we get `u,v>=1`, and the reduced root set of `H` is exactly `{x=0,y=0}`.
Thus `nu=2` in the subrectangular gauge.

Because Section 3 showed that the gauge from `F_min` is affine linear, the
number of distinct roots is preserved from `F_min` to the gauge. Hence
`nu(F_min)=2`, not merely "some equivalent gauge has `nu=2`".

This also answers the proposed alternatives:

```text
nu = 1: impossible at F_min.
nu = 2: forced.
nu >= 3: impossible at F_min.
```

The reason `nu>=3` is impossible is not `(LF)` alone. It is that GGV supplies a
subrectangular form and degree-minimality forces the supplying automorphism to
be affine; an affine map cannot change three reduced roots into two.

For `nu=1`, the classical one-root reduction can be stated in the form needed
here. If the common binary form `H` is a power of one linear form for a
Jacobian counterexample, apply the Makar-Limanov/vdE subrectangularization used
by GGV Proposition 4.7. Its image has two reduced top roots. Since an affine
source map preserves the reduced root count on `P^1`, that subrectangularizing
automorphism cannot be affine. The GGV inverse-degree computation quoted in
Section 2 then shows that the subrectangularizing map strictly lowers both
coordinate degrees. Decompose it by Jung-van der Kulk into affine and
elementary factors; affine factors preserve degree, so at least one elementary
factor in the word strictly lowers `D`. This proves the requested one-root
descent. The target-side special case where one degree divides the other is
GGV Remark 4.2 / note 12.

## 5. Consequences for Integration #14

Integration #14 should now be read as unconditional for every `Aut x Aut`
degree-minimal counterexample representative:

```text
nu(F_min)=2,
deg_{T_+}(E_0)=2,
E_0 is a free vertex of the polar tree.
```

So CH2's hypothesis "`Psi=0` and `E_0` a leaf" is vacuous at every geometric
degree `N` in degree-minimal gauge. The conditional cap remains true but has no
degree-minimal instance.

For completeness, if `nu=1` had survived, FIRST-FORK would make `E_0` a leaf.
Then E0-LEAF-CAP gives, with no Keller-specific input beyond the later Moh
floor,

```text
Psi=0 and E_0 leaf  =>  D <= N + 1 - 2 g_L <= N+1.
```

Moh gives `D_min>=101`; with the GGV divisor sharpening used in Integration
#14, `D_min>=102`. Thus CH2 in any gauge would force

```text
N >= 100   using Moh 101,
N >= 101   using the sharpened D_min>=102.
```

This is a conditional bound only, not an empty-cell claim.

If `nu>=3` had survived, FIRST-FORK would put a fork at `E_0`, and since
`m_{E_0}=D`,

```text
Psi >= D (nu-2) >= D.
```

With `D_min>=102`, this would give fork mass at least `102` in the
degree-minimal counterexample range. That would not kill a cell by itself; it
would retype the problem as a large anticanonical-defect/fork-mass problem.
The bridge eliminates this branch at `E_0`, leaving only deeper forks.

## 6. Controls

Desk controls were limited to leading forms and root counts.

```text
(x, y+x^k), k=2,3,4:  Jac=1, top form x^k, nu=1.
(x, xy):              top form xy, nu=2.  Not Keller, but first-fork shape control.
(x, x^2 y^2):         top form x^2 y^2, nu=2.  Not Keller, same control.
(x, x y (x-y)):       top form x y (x-y), nu=3.  Not Keller; shows linear maps
                      cannot monomialize a three-root top form.
(x,xy) after (x,y)->(x,y+x^2): top form x^3, nu=1.
```

These match the charged controls: nonlinear elementary source composition
manufactures `nu=1` while raising degree; `(x,xy)`-type maps display `nu=2`.
They are not counterexample evidence.

The `(LF)` normal-form control is algebraic. Since `[P,Q]` is constant, the top
homogeneous bracket vanishes. Binary homogeneous forms with zero bracket have
the same reduced linear factors and proportional multiplicity vectors. Hence
`l(P)=alpha H^d`, `l(Q)=beta H^e`, `gcd(d,e)=1`. At degree-minimality, `d,e>=2`
and unequal, otherwise a target elementary map or target linear combination
lowers `D`.

The `N=4` `(B3)` control remains as Integration #14 states from
`polar-chain-n4-grok46-20260902`: `Psi=0` and `E_0` leaf are jointly impossible
there (`7 >= 2n+kappa >= 9`), the polar tree forks, and the six DO graphs are
killed by transfer-determinant identities, not by CH2. The present bridge does
not reopen that computation; it says the `E_0` fork/leaf alternatives are not
available at degree-minimal infinity. Any fork in the `N=4` `(B3)` analysis is
therefore a deeper fork.

## 7. Typed Output

```text
ANSWER
  YES: every Aut x Aut D-degree-minimal counterexample representative admits
  the degree-preserving GGV standard subrectangular gauge.

BOUNDED QUANTITY
  nu(F_min), the number of distinct roots of the top form of the max-degree
  coordinate, is exactly 2.

PROMOTE
  Integration #14's E_0-free conclusion and CH2 vacuity at every N, in the
  degree-minimal scope.

REPAIR
  Do not say "linear change plus LF monomializes any H with at least two roots."
  Say: GGV/ML gives a subrectangular source gauge; orbit D-minimality forces
  that gauge to be affine degree-preserving; therefore the original H already
  had two reduced roots.

GLOBAL-B USAGE
  GGV used global minimality of B to force degree preservation in Proposition
  4.7. In this bridge, the same contradiction is supplied by orbit
  degree-minimality. GGV's B-minimality remains the hypothesis for Corollary
  5.21 as printed and for the later global lower-bound theorem B>=16.

NO NEW OPEN
  OPEN[SUBRECT-ORBIT-BRIDGE] is closed in this scope. No replacement OPEN is
  needed for nu at F_min. Existing deeper-fork and satellite-mass OPENs remain.
```

## 8. FALLACY-v2 Audit

Flag/place/series are separated: `nu` is the reduced root count of the top
binary form on source `L_infty`; it is not the satellite `nu_C` and not a
Puiseux denominator. Carrier/attainment is separated: the non-Keller controls
are shape controls only. Floor/attainment is separated: Moh and `D_min>=102`
are floors, and the conditional CH2 cap is not promoted as an actual kill.
Pole/interior identities are consumed only through Integration #14 and the
`N=4` control. No `sat()`, raw-remainder, variable-map, prime-label, or
merge-free/M-descent argument is used. Case (A), A2, and `Z(G)=1` are untouched.

<!-- BODY-END -->
