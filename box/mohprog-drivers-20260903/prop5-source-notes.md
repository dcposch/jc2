# Moh source notes: Definition 5.1, Propositions 5.3--5.6, and the characteristic-sequence check

Scope: source-only hostile read for the `prop5_source` lane. I did not read any
charged Markdown report, any `jc2-lean` material, any `ideation-20260903T*`
file, or another lane's in-progress report. I read the 300-dpi images
`/tmp/moh-pages-sol56/moh-40.png` through `moh-50.png` (journal pp.179--189)
in full. I also read source images for journal pp.146--147, 150--159, 170--176,
200--203, and Appendix I pp.205--207 where needed to resolve the algebra used
on pp.179--189. The frozen PDF hash was checked directly:

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51
```

No OCR/pdftotext formula was trusted; the formulas below were read from the
page images. Page/paragraph locators identify the printed journal page and the
beginning of the relevant paragraph or the displayed equation number.

## 1. Index dictionary that matters

Moh's convention is shifted relative to the usual "gcd through the current
characteristic exponent" convention:

\[
d_1=n,\qquad d_{j+1}=\gcd(n,M_1,\ldots,M_j).
\]

This is printed at p.150, paragraph beginning "Recall", first display. Thus
the search-page statement `d_r=g.c.d.{n,M_1,...,M_{r-1}}` on p.201(5) is the
same convention, not a typo.

For a full tower ending in `D_1`, the numerical sequence is
`V_2,...,V_{s+1}`, with `V_{s+1}=d_{s+1}`. At level `D_k`, Proposition 4.6
supplies polynomials which I denote `p_k,q_k`; from p.182, last two displays,

\[
 P_k:=\deg p_k=V_{k+1}\frac{d_k}{d_{k+1}},\qquad
 Q_k:=\deg q_k=V_{k+1}\frac{n-M_k}{d_{k+1}}.
\]

For `k>=2`, choosing a factor `pi-c_k` of `p_k` of multiplicity `V_k`
extends `D_k` to `D_{k-1}`. This is Proposition 5.3's construction (p.180,
statement, the two displays defining `tau` and `delta_{r-1}`), with `k=r`.

## 2. Definition 5.1, transcribed in operative form

Source: p.179, lower half, Definition 5.1, clauses (1)--(4).

A tower `D_s superset ... superset D_r` comes with integers
`V_i (i=r+1,...,s+1)` and satisfies:

1. In `D_i`, `g(y)` has exactly
   \( (n/d_{i+1})V_{i+1}\) roots, and `T_j^psi(y)` has exactly
   \( (-\mu_j/d_{i+1})V_{i+1}\) roots for `j=1,...,i`.
2. For `i=r+1,...,s`,
   \[
   V_{i+1}\frac{d_i}{d_{i+1}}\ge V_i>
   \frac{d_i}{n-M_i},\qquad V_{s+1}=d_{s+1}.
   \]
3. `D_i` has logarithmic radius
   \[
   \delta_i=1-
   \frac{(n-M_i)\prod_{j=i+1}^{s}[V_j(n-M_j)-d_j]}
        {(n-M_s-1)\prod_{j=i+1}^{s}[V_j(n-M_{j-1})-d_j]}
   \quad(i=r,...,s).
   \]
4. If `sigma_i` is the unique general point of `D_i`, the hypotheses of
   Proposition 4.6 hold with `sigma=sigma_i`, `delta=delta_i`, and
   \(v=V_{i+1}d_i/d_{i+1}\).

The displayed root counts in clause (1) are equality statements for every
level, not merely lower bounds. Their integrality is automatic from the gcd
chain and the actual tower, but a numerical emulator should still assert it.

## 3. Proposition 5.3: exact statement and proof payload

### 3.1 Statement

Source: p.180, top through the paragraph ending "tower of major discs."

Assume `r>=2` and a tower `D_s superset ... superset D_r` is constructed.
Let `pi-C_r` be a factor of the common polynomial `p(pi)` furnished by
Proposition 4.6, with multiplicity `V_r`, satisfying

\[
\deg p=V_{r+1}\frac{d_r}{d_{r+1}}\ge V_r>
\frac{d_r}{n-M_r}.
\]

Write

\[
\tau=\sum a_jt^j+c_rt^{\delta_r}\in D_r
\]

and let `delta_{r-1}` be the minimum order of a difference between roots of
`g prod_{i=1}^r T_i^psi` which lie strictly closer to `tau` than `delta_r`.
Equivalently it is the radius of the minimal disc `D_{r-1}` containing those
roots. Then

\[
\delta_{r-1}=1-
\frac{(n-M_{r-1})\prod_{j=r}^{s}[V_j(n-M_j)-d_j]}
     {(n-M_s-1)\prod_{j=r}^{s}[V_j(n-M_{j-1})-d_j]},
\]

and adjoining `D_{r-1}` gives another tower of major discs.

### 3.2 Proof map

* p.180, first proof paragraph: Definition 5.1(2) is called "automatic";
  Moh defines the auxiliary rational function `delta(L)` and first claims
  `delta_{r-1} >= delta(M_{r-1})`.
* pp.180--182, from "Let us assume the contrary" through "Our claim has thus
  been established": assuming an intermediate radius produces a unique
  pi-root `sigma*`; Lemma 5.2 supplies the order identities; the hypotheses of
  Proposition 4.4 are verified; its non-splitting conclusion contradicts the
  definition of `delta_{r-1}`.
* p.182, paragraph beginning "Let delta** denote": set
  `delta**=delta(M_{r-1})`, take the unique pi-root `sigma**`, and apply
  Proposition 4.6 with
  \[
  v=V_r\frac{d_{r-1}}{d_r},\qquad r-1\text{ in place of }r.
  \]
  The bottom two displays on p.182 state
  \[
  \deg q=V_r\frac{n-M_{r-1}}{d_r}>1,
  \qquad
  \deg p=V_r\frac{d_{r-1}}{d_r}.
  \]
* p.183, first paragraph: `q` has distinct roots. Therefore at least two
  roots of `T_{r-1}^psi` in the `delta**`-disc are separated at exactly that
  radius; hence `delta_{r-1}=delta(M_{r-1})=delta**`. This supplies clauses
  (1), (3), and (4) of Definition 5.1 for the extended tower.

### 3.3 What the `p,q` multiplicity theorem actually says

Proposition 4.6 (p.170, conclusions (1)--(5)) and Appendix I Proposition A.3
(p.205, statement and proof) give, at each new level:

* `q_k` is squarefree;
* every root of `p_k` is a root of `q_k`;
* `p_k` is not a power of `q_k`;
* at least one root of `p_k` has multiplicity strictly larger than
  \(P_k/Q_k=d_k/(n-M_k)\).

Proposition 5.3 chooses such a large-multiplicity factor and calls its
multiplicity `V_k`. Appendix I does **not** say that every root is large, that
the large root is unique, or that its multiplicity divides either degree.
Promoting any of those statements would be a source error.

The proof of A.3 is useful for seeing the exact strength. Its differential
equation is rewritten (p.205, first proof display) as

\[
Qq(\pi)p'(\pi)=(Pq'(\pi)-c)p(\pi),\qquad c\ne0.
\]

Root-valuation comparison gives roots(`p`) subset roots(`q`) and squarefree
`q`; a degree-count contradiction gives only the existence of one root of
multiplicity `>P/Q`.

### 3.4 Full factor partitions versus the orbit conditions

Let `A_k` be the relative denominator increment of `delta_k` and write

\[
P_k=\Delta_kA_k+\square_k,
\qquad 0\le\square_k<A_k.
\]

The relative conjugation used by Moh on p.201 makes nonzero coefficient roots
occur in full `A_k`-orbits with constant multiplicity, while zero is fixed.
Precisely, Moh chooses `\bar t` with
`\bar t^{L A_k}=t` and uses the automorphism
\(\bar t\mapsto\omega\bar t\) of
\(k\langle\langle\bar t\rangle\rangle\) over
\(k\langle\langle\bar t^{A_k}\rangle\rangle\), where
\(\omega^{A_k}=1\). Thus the fixed field is the `A_k`-power subfield
(equivalently \(k\langle\langle t^{1/L}\rangle\rangle\)), not a
`t^{1/A_k}` field.
Consequently an actually selected factor has exactly the two necessary
possibilities Moh prints:

* `c_k != 0`: the orbit contributes `A_k V_k` to `P_k`, so
  `V_k <= Delta_k` (p.201(10));
* `c_k = 0`: its multiplicity is congruent to `P_k` modulo `A_k`, so
  `V_k=jA_k+square_k` (p.201(11)).

The same conjugation and squarefreeness of `q_k` suggest the further check
`Q_k == 0 or 1 (mod A_k)`. In fact the stronger congruence

\[
\boxed{A_k\mid Q_k-1}
\]

is source-derivable, but it is automatic from the already-computed radii and
adds no elimination. To see this without an orbit heuristic, specialize Lemma
5.2 (pp.177--179) at its parameter `L_0=M_k`. Put

\[
R=d_{k+1}\delta_s+
\sum_{i=k+2}^sV_i\frac{d_{k+1}}{d_i}
(\delta_{i-1}-\delta_i)-V_{k+1}\delta_{k+1}.
\]

Every denominator in `R` divides the old lcm `L`, and Lemma 5.2 says

\[
\frac{n-M_k}{d_{k+1}}(R+V_{k+1}\delta_k)=-1+\delta_k.
\]

Thus `(Q_k-1)L delta_k` is an integer. Since `A_k` is the reduced denominator
of `L delta_k`, `A_k | Q_k-1`.

For `A_k>1`, the complete bare orbit factorization can therefore be
written
\[
p_k(\pi)=\pi^{u_0}\prod_{\ell=1}^{h}
 (\pi^{A_k}-c_\ell)^{u_\ell},\qquad
u_0+A_k\sum_{\ell=1}^{h}u_\ell=P_k,
\]
\[
q_k(\pi)=\pi\prod_{\ell=1}^{g}(\pi^{A_k}-b_\ell),\qquad
Q_k=1+A_kg,
\]
with the `b_\ell` distinct and every `c_\ell` among them. A selected
nonzero factor has `V_k=u_\ell`; a selected zero factor has
`V_k=u_0`. Thus squarefreeness consumes exactly one root of `q_k`
for every *distinct* root of `p_k`, not `u_\ell` or
`u_\ell-1` roots. In the original leading polynomial
`p_k^{ell_k}q_k`, its multiplicity is `ell_k u_\ell+1`.

Once this automatic congruence is imposed, the bare factor-partition data add
no further bound on a selected `V_k` beyond (7), (10)/(11):

* on a nonzero branch, allocate `A_k V_k` to the selected orbit and put the
  residual `P_k-A_kV_k` at zero;
* on a zero branch, allocate `V_k` at zero and the residual, divided by
  `A_k`, to one nonzero orbit.

When `A_k>1`, `q_k` has a zero root and enough nonzero orbit slots because
`Q_k=1 mod A_k`; for `A_k=1` there is no nontrivial orbit constraint. The
only possible accidental equality `p_k=q_k^e` would
force `V_k=P_k/Q_k`, excluded by the strict lower inequality. This is only a
combinatorial realization of the A.3 conclusions, not a proof that arbitrary
such data solve the differential equation.

### 3.5 Proposition A.4 does not print another integer filter

Appendix I Proposition A.4 (p.206) starts with

\[
D(P,N,p,q^*)=c p^{\ell+1},\quad c\ne0,\quad \ell\ge0,
\]

and proves recursively that `q*=p^ell q` and

\[
D(P,N-\ell P,p,q)=c p.
\]

In Proposition 4.6 this is exactly the step which produces the squarefree
`q_k` governed by A.3. It determines the full multiplicity in `q*` over a
root of `p` as `ell*mult_p+1`, but gives no second restriction on the chosen
`V_k`. The exponent displayed on p.170(2),

\[
\ell=\frac{-\mu_k+M_k-n}{d_k},
\]

is a nonnegative integer for the actual data. In fact its integrality and
positivity are automatic from the characteristic-data recurrence in the
search regime, rather than a new filter. Write `E_k=ell_k`,
`n_{k-1}=d_{k-1}/d_k`. At the first applicable level,

\[
E_2=n^*m^*-n^*-m^*,\qquad n^*=n/d_2,\quad m^*=m/d_2,
\]

which is positive when `n^*,m^*>1` are coprime. From
`R_k=-mu_k=n_{k-1}R_{k-1}-M_k+M_{k-1}` one obtains

\[
E_k=n_{k-1}^2E_{k-1}
 +(n_{k-1}-1)\frac{n-M_{k-1}}{d_k}.
\]

Here `d_k` divides both `n` and `M_{k-1}`, so the second term is a
positive integer whenever the gcd descends. A.4 is a reduction theorem, not
a numerical classification of which `p,q` solve A.3.

There is nevertheless an exact coefficient/position constraint in the A.3
differential equation which a bare multiplicity partition forgets. Let the
distinct roots of the squarefree `q` be `a_1,...,a_Q`, and put
`u_i=mult_{a_i}(p)`, allowing `u_i=0` at the extra roots of `q`. Then

\[
\sum_{i=1}^Q u_i=P,\qquad
w_i:=P-Qu_i\ne0,\qquad
w_iq'(a_i)=c \quad(1\le i\le Q).
\]

These equations follow by comparing the local leading coefficient at each
`a_i`. Conversely, given squarefree `q` and `p` with these equations,
the polynomial `D(P,Q,p,q)/p-c`, of degree at most `Q-2`, vanishes at all
`Q` roots of `q`, so the full A.3 equation holds. Equivalently,

\[
\sum_i w_i\prod_{j\ne i}(\pi-a_j)=c,
\]

or, after making `q` monic,

\[
\sum_iw_i a_i^h=0\quad(0\le h\le Q-2),\qquad
\sum_iw_i a_i^{Q-1}=c.
\]

The `h=0` equation is automatic from `sum u_i=P`, but the remaining
moment equations couple all root positions and all multiplicities.
Propositions A.3 and A.4 do **not** assert that every numerical multiplicity
partition admits such distinct `a_i`. Thus an exact `ODE-realizability`
test is a genuine remaining candidate, but no degree-only version is
PROVED-IN-SOURCE here.

Two parts of this exact system *do* give source-proved finite combinatorics
beyond a single selected factor:

1. Every sibling factor must satisfy
   \[
   \boxed{P_k-Q_ku\ne0}.
   \]
   This follows immediately from
   \((P_k-Q_ku)q_k'(a)=c\ne0\). It is stronger than “`p_k` is
   not a power of `q_k`”: the latter excludes all multiplicities being
   equal to `P_k/Q_k`, while the local equation excludes even one such
   root. The displayed branch multiplicity `V_k` already obeys it because
   (7) says `V_k>P_k/Q_k`, but the residual degree must admit an orbit
   partition all of whose unselected multiplicities avoid the average.
2. Proposition 5.3 is stated for any factor of multiplicity
   `u>P_k/Q_k`. Each such factor therefore creates a legitimate major
   child, not merely the one factor retained in a printed `V`-chain.
   Proposition 5.6 applies to every complete tower obtained this way.
   Consequently a full implementation must quantify universally over all
   high-multiplicity siblings of an existentially chosen orbit partition.

This **FULL-FACTOR-TREE** requirement is source-backed; it is not present in
the one-dimensional list of selected `V_k`'s. A finite driver reports
that the bare full tree sends the 658 rows at `n<=100` to 60
`V`-assignments / 40 groups / 12 degree classes, and at `(75,50)`
keeps only `(M_2,V_2)=(55,2),(55,3)`. Adding the local
`P_k-Q_ku\ne0` requirement recursively gives 58 assignments / 38 groups
/ 12 classes; it changes none of the nine `(75,50)` selected-path rows
by itself. Thus this explains the requested `(75,50)` discriminator but
still leaves 52 rows beyond Moh's six.

The orbit symmetry gives a smaller exact form of the remaining position
problem. Write `A=A_k`, `b=u_0`, `z=pi^A`,
`S=(Q-1)/A`, and pad the list of nonzero `q`-orbits to exactly
`S` entries by setting `u_l=0` at a `q`-only orbit. Define
\[
W_0=\frac{P-Qb}{A},\qquad W_l=P-Qu_l.
\]
Then `W_0+sum_l W_l=0`, and for distinct nonzero orbit parameters
`z_l` the moment equations reduce to
\[
\sum_{l=1}^{S}W_lz_l^h=0\qquad(1\le h\le S-1).
\]
This is still a coefficient-existence problem, not a condition printed by
Moh.

One useful necessary inequality follows elementarily. The rational function
\[
\Phi(\pi)=\frac{q(\pi)^P}{p(\pi)^Q}
 =\Psi(z)=Cz^{W_0}\prod_l(z-z_l)^{W_l}
\]
satisfies, by the A.3 equation,
\[
\Phi'(\pi)=c\,q(\pi)^{P-1}p(\pi)^{-Q}.
\]
Thus `\Phi-\Phi(infinity)` has order `Q-1` at infinity, and
`\Psi-\Psi(infinity)` has order `S`. If
`h=gcd(|W_0|,|W_1|,...)` and `d_+=sum_{W_i>0}W_i`, the primitive
rational map obtained by dividing all exponents by `h` has degree
`d_+/h`. Its local degree at infinity cannot exceed its global degree,
so
\[
\boxed{\frac{d_+}{h}\ge S}.
\]
This is rigorously DERIVED-FROM-SOURCE plus elementary rational-map degree,
but it is not a theorem stated or proved by Moh. It should not be labelled
PROVED-IN-SOURCE.

## 4. Proposition 5.4 and Lemma 5.3: a strict top inequality

Proposition 5.4 (p.183, middle, statement) identifies the smallest disc
containing all roots of `g(y)T_1^psi(y)` as

\[
D_i,\qquad i=\max\{r:V_{r+1}d_r/d_{r+1}>V_r\}.
\]

If `delta_i>-1`, either the coordinate rings already agree or a polynomial
automorphism reduces the degrees simultaneously. The proof is on pp.183--185:
the `i=1` case uses Appendix I A.5 and conjugation to force `M_1=-1`; for
`i>1`, a nonzero root of the common `p(pi)` makes the center exponents
integral, after which the weighted leading form has a factor
`a^l x-y^l` and an elementary automorphism lowers the degrees.

The quantifier on `i` is essential. It is
\[
i=\max\{r:V_{r+1}d_r/d_{r+1}>V_r\},
\]
so `D_i` is the globally smallest disc containing all roots of
`gT_1^psi`. The p.184 argument that every earlier center exponent is
integral uses this global root count; only then does Moh write the center as
`h(x)` and apply `y->y-h(x)`. The tempting edge-state rule “zero
center preserves a pure danger; a nonzero center preserves it exactly when
its delta is integral” is therefore **INFERRED/OPEN**, not an exact
consequence of Proposition 5.4 on an arbitrary sibling path. A finite
experiment with that rule reduces the source-backed 58 rows to 20 (six
printed plus fourteen), but it must not be promoted without proving that the
global-smallest-disc hypothesis persists.

Lemma 5.3 (p.185, lower half; proof p.186) says the smallest-disc radius is
`-1` iff `M_s=n-2` and the highest homogeneous form has two roots, one with
multiplicity `(n/d_s)v_s`, where

\[
d_s>v_s>d_s/2.
\]

The proof explicitly derives `d_s>V_s>d_s/2` (p.186, displays following
"It follows from Proposition 5.4 and 5.3") and then identifies the root
multiplicity as `V_s`. Therefore lowercase `v_s` in Lemma 5.3 is the tower's
capital `V_s`, and the strict top bound

\[
\boxed{V_s<d_s}
\]

is PROVED-IN-SOURCE. This is a genuine strengthening of the weak upper sign
printed in the generic p.201(7), although it may be redundant with other
specialized assumptions in an implementation.

## 5. Proposition 5.5 and the bottom (`r=2`) alternatives

### 5.1 Statement and setup

Proposition 5.5 (p.186, lower third) says that if there are only two effective
characteristic pairs (`s=2`), then the coordinate rings already agree or a
polynomial automorphism simultaneously reduces the relevant degrees.

The proof assumes the contrary. Proposition 5.4 forces (p.187, first display)

\[
M_2=n-2,\qquad \delta_2=-1,
\]

and Proposition 5.3 gives

\[
d_2>V_2>d_2/2.
\]

Writing

\[
n=d_2n^*,\quad -M_1=d_2m^*,\quad U_2=d_2-V_2<V_2,
\]

p.187 gives, in reduced form,

\[
\delta_1=
\frac{(n^*+m^*)U_2-1}{(n^*+m^*)V_2-1}=\frac BA,
\qquad 0<\delta_1<1,\quad A>1.
\]

### 5.2 Independent derivation of the denominator identity

For `s=2` it is immediate from the preceding reduced fraction that

\[
\boxed{A\mid (n^*+m^*)V_2-1}.
\]

The general tower version, with `A_1` the reduced denominator of `L delta_1`,
comes directly from Lemma 5.2 and is worth recording because it does not rely
on the displayed special fraction. Put `b=(n-M_1)/d_2=n^*+m^*` and

\[
R=d_2\delta_s+
\sum_{i=3}^sV_i\frac{d_2}{d_i}(\delta_{i-1}-\delta_i)
-V_2\delta_2.
\]

All denominators of `R` divide `L`. Lemma 5.2 with its parameter equal to
`M_1` gives

\[
b(R+V_2\delta_1)=-1+\delta_1,
\]

so

\[
(bV_2-1)(L\delta_1)=-L-b(LR)\in\mathbb Z.
\]

Reduction of `L delta_1` therefore proves
`A_1 | (n^*+m^*)V_2-1`.

### 5.3 Why (12)/(13) are exactly the source's bottom residue condition

At p.187, bottom paragraph, the leading polynomials satisfy

\[
D(n,-M_1,g_\sigma(\pi),T^\psi_{1,\sigma}(\pi))=c\ne0.
\]

Appendix I A.5 and the differential identity give both

\[
(g_\sigma,T^\psi_{1,\sigma})=1,
\qquad (g'_\sigma,(T^\psi_{1,\sigma})')=1.
\]

The relative `A_1` conjugation has the following alternatives (p.188, first
three paragraphs): if `A_1` does not divide a degree, zero is a root of that
polynomial; if it does divide the degree, the polynomial lies in
`k[pi^{A_1}]` and zero is a root of its derivative. Coprimality excludes
"neither degree divisible" and derivative-coprimality excludes "both
divisible". Combining the one-divisible/one-not-divisible dichotomy with the
denominator identity yields precisely

\[
A_1\mid n^*V_2,\qquad A_1\mid m^*V_2-1,
\]

or

\[
A_1\mid m^*V_2,\qquad A_1\mid n^*V_2-1.
\]

These are p.201(12)/(13). They already imply `gcd(A_1,V_2)=1`. The simple-root
and derivative-coprime information contributes no further degree-only residue
condition: the residues of the two degrees are exactly `{0,1}` modulo `A_1`,
and their nonzero root orbits can be chosen disjoint.

### 5.4 The rest of p.188 is special to `s=2`, not an omitted universal clause

Moh treats the first alternative by setting (p.188, middle)

\[
n^*V_2=AD,\qquad m^*V_2-1=AE.
\]

Then `gcd(A,V_2)=1`, hence `V_2|D`. If `1-delta_1=(n^*+m^*)C/A`, the two
equalities

\[
(n^*+m^*)V_2-1=A(D+E),\qquad V_2-U_2=C(D+E)
\]

give

\[
V_2>V_2-U_2=C(D+E)\ge D\ge V_2,
\]

a contradiction. The other bottom alternative is verbatim symmetric.

The factorization through `U_2=d_2-V_2` and the true-fraction assertion use
`s=2`, `M_2=n-2`, `delta_2=-1`. For `s>=3`, higher-level product factors occur
in `delta_1`; p.188 supplies no analogous positive equality and no second
general clause after (12)/(13). Verdict: **no omitted universal `r=2`
numerical clause was found in Proposition 5.5**. Importing the final
`V_2>...>=V_2` contradiction into a longer tower would be invalid.

## 6. Proposition 5.6: exact content and the branch datum

### 6.1 Statement and proof

Proposition 5.6 is stated at p.188, bottom. For `s>=2`, if the unique pi-root
in `D_1` is

\[
\sigma_1=\pi t^{\delta_1},
\]

then the coordinate rings already agree or a polynomial automorphism lowers
the degrees simultaneously.

The proof occupies p.189:

1. Proposition 5.4 and Lemma 5.3 reduce to
   `delta_s=-1`, `M_s=n-2`, and `d_s>V_s`.
2. The displayed formula for `delta_{s-1}`, together with
   \[
   V_s(n-M_{s-1})>V_s(n-M_s)>d_s,
   \quad d_s>V_s,
   \quad d_s\mid n-M_{s-1},
   \]
   yields `delta_1>=delta_{s-1}>=0`.
3. Because `g` and `T_1^psi` have no common polynomial factor, after adding a
   constant if needed, `g` has a term `x^l`, `l>=1`. For the pure pi-root this
   gives `ord g(sigma_1)=n lambda<=-l`.
4. Equality of orders in Proposition 4.1 gives
   \[
   n\lambda+(-M_1)\lambda-1=-2+\delta_1\ge-2.
   \]
   Hence `l=1`, `n lambda<=-1`, and the final display gives
   `delta_1<=(-M_1)lambda<0`, contradiction.

Thus the proposition's exact theorem is geometric: a nonreducible pair cannot
have a bottom general point with no lower center terms.

### 6.2 Safe numerical projection

At each actual extension `D_k -> D_{k-1}`, `k=2,...,s-1`, retain a typed bit

```text
Z_k : selected factor is pi       (c_k=0)
N_k : selected factor is pi-a     (c_k!=0).
```

The source implications are one-way:

```text
N_k => V_k <= Delta_k                         (10)
Z_k => V_k == j*A_k + square_k for some j    (11)
```

After the standard top normalization, all `Z_k` give the pure `sigma_1`
excluded by Proposition 5.6. This is exactly the meaning of Moh's sentence at
p.201, last paragraph: "the situation indicated by equation (11) can not
always happen." Therefore a necessary branch-level condition is

\[
\bigvee_{k=2}^{s-1}N_k.
\]

After forgetting the branch bits, the fail-closed row filter is only

\[
\boxed{\exists k\in\{2,\ldots,s-1\}:V_k\le\Delta_k.}
\]

In words: reject a numeric row only if every level forces the zero-factor
branch because (10) is impossible. A value satisfying the congruence in (11)
does not prove that the actual factor is zero; it may also satisfy (10).
Accordingly, the slogan `NOT-ALL-(11)` is exact only when it refers to typed
factor choices, not to congruence membership alone.

The last extension `D_2 -> D_1` is the `k=2` bit and must be included. It is
controlled by `(A_2,V_2)`. For `s=3` it is the sole branch bit. There is **no
new factor-choice bit at `A_1`**: `A_1` governs the bottom leading-polynomial
conjugation and alternatives (12)/(13), not another tower extension.

## 7. Characteristic sequence and the exact semigroup equation

This was read because a proposed filter on `{n,M_i}` can easily use the wrong
generators.

### 7.1 Correct conversion

Moh p.150, last three displays, defines

\[
n_0=1,\quad n_j=\frac{d_j}{d_{j+1}},\quad
q_1=M_1,\quad q_j=M_j-M_{j-1},
\]

\[
\lambda_j=\sum_{i=1}^j q_i d_i,\qquad
\mu_j=\frac{\lambda_j}{d_j},\qquad
\theta_j=\mu_j-M_j.
\]

Equivalently,

\[
\mu_1=M_1=-m,qquad
\mu_j=n_{j-1}\mu_{j-1}+M_j-M_{j-1}.
\]

The positive degree generators are

\[
R_j:=-\mu_j
=-\frac{M_1n+\sum_{i=2}^j(M_i-M_{i-1})d_i}{d_j}.
\]

Moh p.154, paragraph beginning "In the tradition of Pythagoras", proves
`deg_y T_j^psi=-mu_j` and

\[
\gcd(n,\mu_1,\ldots,\mu_j)
=\gcd(n,M_1,\ldots,M_j)=d_{j+1}.
\]

Thus a semigroup test on the literal set `{n,M_1,...,M_s}` is the wrong map;
the source's approximate-root degrees are `{n,R_1,...,R_s}`. In particular,
an implementation should at least assert `R_j` is a positive integer for
every effective `j`.

### 7.2 Proposition 3.1, exact bounded membership condition

Proposition 3.1 is stated on p.157 and proved through p.159. Its canonical
expansion is

\[
T_{r+1}(f,g)=T_r(f,g)^{n_r}+\sum_{j,\alpha}c_{j,\alpha}g^jT_\alpha,
\]

where `alpha=(alpha_1,...,alpha_r)`, `0<=alpha_i<n_i` for `i<r`, and initially
`alpha_r>=0`; Proposition 3.1 sharpens this to `alpha_r<n_r` for nonzero
terms. For every effective `r` (`M_r<e`; Lemma 2.1 makes `e=n-1` in the
Jacobian case), comparison of y-degrees gives (p.158(10)--(11))

\[
-\mu_{r+1}=(-\mu_r)n_r-q_{r+1}<(-\mu_r)n_r
\]

and

\[
\deg_y(g^jT_\alpha)=jn+\sum_{i=1}^r(-\mu_i)\alpha_i.
\]

There is a unique term attaining degree `(-mu_r)n_r`, and p.159(13) states
that its indices solve

\[
\boxed{
jn+\sum_{i=1}^{r-1}R_i\alpha_i=n_rR_r,
\quad j\ge0,\quad 0\le\alpha_i<n_i,\quad \alpha_r=0.}
\]

This is the exact source theorem behind the approximate-root semigroup
condition

\[
n_rR_r\in\langle n,R_1,\ldots,R_{r-1}\rangle.
\]

It is PROVED-IN-SOURCE, with the bounded digits and uniqueness stronger than
unbounded knapsack membership. It should be tested for every `r=1,...,s`,
using `d_{s+1}=gcd(d_s,M_s)` at the last step. The `r=1` equation reduces to
`n_1m=(m/d_2)n` and is automatic.

This predicate is not merely a guessed conductor condition. Moh's warning on
p.151 (paragraph beginning "We shall call the reader's attention") gives the
example of degree data 6 and 8 for which `M_2=13` cannot occur. With the
orientation `n=8,m=6`, the source conversion gives `R_1=6`, `R_2=5`,
`n_1=4`, `n_2=2`; equation (13) would require

\[
8j+6\alpha_1=10,\qquad0\le\alpha_1<4,
\]

which has no solution. Thus gcd descent and ordering alone do not imply the
bounded semigroup equation in general.

For the specialized search regime it is arithmetically redundant on the
audited finite census. An independent driver check found the correctly
indexed equation true on all 658 p.201(1)--(13) rows at `n<=100`, on all
54 rows remaining after the bare full-tree partition, all 17 remaining after
the polynomial filter, all 14 remaining after the ODE/passport filter, and
all 23,720 baseline rows at `48<=D<=200`. Direct hand checks on the
`(75,50)` families with `M_2=5,10,40,55,60` and `M_3=73`
likewise all pass. Alternative index shifts kill printed rows and are
fail-closed wrong. Thus Proposition 3.1 is a genuine source theorem and is
not implied by bare gcd/order in general, but it is **not** the missing
Moh-program discriminator on these bounded sets.

### 7.3 What p.201(4) and the bound `s<=5` mean

The search list's condition (4), p.201 top, says verbatim that
`{n,M_1,...,M_s}` **“is the part of characteristic data of
`(f,g)` which are less than `n-2`.”** This wording is slightly
inexact because p.200(2) has already set `M_s=n-2`; operationally it
means the initial characteristic-data segment through `n-2`. It is not
merely the inequalities
`M_1<...<M_s`. Therefore Proposition 3.1 is logically entailed by the
semantic wording of printed condition (4), even though Moh does not expand
it there into equation (13). It is a plausible arithmetic test for a program
implementing “characteristic data.”

The “simple computation” giving `s<=5` on p.201 is only a chain-length
bound. Moh lists on p.155(1)
\[
d_{j+1}=\gcd(n,\mu_1,\ldots,\mu_j)<d_j.
\]
Hence every `n_j=d_j/d_{j+1}>=2`. With `d_s>=4` and `n<=100`,
\[
n=d_1\ge 2^{s-1}d_s\ge2^{s+1};
\]
`s>=6` would imply `n>=128`. No extra realizability test is hidden in
that sentence.

Besides strict gcd descent and Proposition 3.1, the source gives
`R_j=-mu_j=deg_y T_j^psi>0` (Proposition 2.2, pp.152--154) and
`R_{j+1}<n_jR_j` (p.158(10)). The latter is algebraically just
`M_{j+1}>M_j`; the characteristic-data recovery formula at p.154 is
tautological after converting between `M` and `mu`. No further
standard approximate-root inequality appears on pp.150--159.

### 7.4 No source conductor filter beyond Proposition 3.1 was found

Pages 155--156 give the mixed-radix `f`-degree expansion and Lemma 3.1's
unique expansion over `k[x]`; pp.157--159 turn it into the bounded membership
above. These pages do not state a conductor equality, symmetry of a numerical
semigroup, or a condition that the literal `M_i` generate the value semigroup.
The one-place statement on p.150 does not by itself license such an extra
integer filter. A stronger conductor test therefore remains OPEN unless a
separate Abhyankar--Moh theorem is quoted with its hypotheses and the ring/
valuation map checked.

## 8. Candidate/verdict table for implementation

| Candidate | Exact predicate | Source status | Expected relation to printed list |
|---|---|---|---|
| Top strictness | `V_s<d_s` | PROVED-IN-SOURCE, pp.185--186 | Strengthens weak upper sign in generic (7); test it. |
| Bare `p` factor partition | selected nonzero: `V_k<=Delta_k`; selected zero: `V_k=P_k mod A_k` | PROVED-IN-SOURCE, p.201 plus Props.4.6/A.3 | No extra *direct selected-factor* bound beyond (7),(10)/(11). |
| No-average sibling | every factor multiplicity `u` has `P_k-Q_ku!=0` | PROVED-IN-SOURCE-DERIVED from the A.3 ODE | Indirectly restricts residual partitions; 60 to 58 rows after full tree. |
| Full factor tree | recurse down every sibling with `u>P_k/Q_k`; no all-zero complete branch | PROVED-IN-SOURCE, Props.5.3 and 5.6 | 658 to 60 rows; exactly isolates the two requested `(75,50)` rows, but leaves 54 excess. |
| Squarefree `q` orbit | `A_k | Q_k-1` | PROVED-IN-SOURCE-DERIVED from Lemma 5.2 | Automatic from radii; consistency assertion, not an elimination. |
| Bottom residue | (12) or (13) | PROVED-IN-SOURCE, pp.187--188, p.201 | Complete degree-only content of A.5/conjugation. |
| Extra p.188 inequality | reuse `V_2>...>=V_2` for `s>=3` | REFUTED AS UNIFORM | The argument is special to `s=2`; do not implement generally. |
| Prop.5.6 | typed branches with at least one nonzero; projected filter `exists k=2..s-1: V_k<=Delta_k` | PROVED-IN-SOURCE with p.201 gloss | Include the `k=2`/`A_2,V_2` step; no `A_1` branch bit. |
| Integral recenter state | propagate “pure danger” through integral nonzero centers | INFERRED/OPEN | Prop.5.4 proves this only at the globally smallest `gT_1`-disc; 58 to 20 rows experimentally. |
| Positive approximate-root degrees | `R_j=-mu_j` is a positive integer | PROVED-IN-SOURCE, pp.150,154 | Test; may be automatic in the search range. |
| Bounded semigroup | equation p.159(13) for each effective `r` | PROVED-IN-SOURCE | Automatic on 658/658 at `n<=100` and 23,720/23,720 baseline rows at `48<=D<=200`; not the discriminator. |
| Stronger conductor/generator claim on `{n,M_i}` | unspecified | OPEN | Wrong generator map as stated; no such theorem appears on the audited pages. |
| Full ODE solvability | existence of distinct `a_i` satisfying the displayed weighted moment system | OPEN | A.3 gives necessary root facts, not a numerical classification or sufficiency theorem. |
| Primitive passport bound | `d_+/gcd(|W_i|)>=(Q-1)/A` | DERIVED-FROM-SOURCE, not Moh-stated | Elementary necessary condition from the exact ODE rational map; not a located Moh program rule. |

Bottom line for items (i)--(iii):

* (i) The source's full factor multiplicity structure supplies the selected
  high-root inequality and the zero/nonzero orbit alternatives. There is no
  further *direct* bound on selected `V_k`, but the exact ODE forbids every
  sibling multiplicity `u=P_k/Q_k`, and every high sibling must itself be
  extended. The resulting FULL-FACTOR-TREE is a real restriction beyond the
  printed one-chain conditions.
* (ii) Proposition 5.5 gives exactly (12)/(13) at the bottom. Its remaining
  contradiction is `s=2`-specific, so it is not a missing second general
  clause.
* (iii) Proposition 5.6 is a geometric pure-root prohibition. Its safe
  numerical shadow is existential nonzero branch / not-all-forced-zero, with
  the final `k=2` selection included. Arithmetic satisfaction of (11) is not
  itself a branch identity, and (12)/(13) do not supply an `A_1` branch bit.
