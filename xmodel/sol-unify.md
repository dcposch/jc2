# Rooftop mass versus carrier denominator: the two `nu` bounds do not unify

**Date:** 2026-08-23  
**Scope:** `xmodel/sol-rooftop.md`, `xmodel/sol-bdelay.md`, `TDBOUND.md`,
`SHEET6-DEPTH.md`, the residue-A template and tetrahedral quotient, and the
banked D21--D25 records.  
**Tier convention:** **EXACT** means proved from the displayed identities or
from the promoted H1 sheet calculus. A family called **FORMAL** satisfies
those arithmetic/tree identities but is not asserted to come from a
polynomial Keller pair. Every new Keller assertion is labelled
**CONJECTURE**.

## 0. Verdict

\[
 \boxed{\textbf{INDEPENDENT AT THE BANKED STRUCTURAL TIER}.}
\]

The repeated symbol is a notation collision.

* In the rooftop formula, `P` runs over **pole vertices** (the leaves of the
  pole subtree), and \(\nu_P\) is the local decoration of that one tree
  vertex. It is not an index over every point of the branch.
* In the depth formula, \(\nu_1,\ldots,\nu_s\) are the successive gcd-drop
  indices at **all characteristic vertices on one pole branch**. Their full
  product is the branch Puiseux denominator.

For the banked residue-A branch the full factorization is

\[
 \kappa(P_i)=42=7\cdot3\cdot2,
 \qquad \nu_{P_i}=2.                                  \tag{0.1}
\]

Thus the rooftop sees only the final factor `2`; it does not see `7` or the
intermediate `3`. The tetrahedral passport has ramification indices
`3,2,2,3`, but these belong to the degree-four quotient after common-carrier
cancellation. The factor `7` in (0.1) is already an exact counterexample to
identifying passport ramification with all carrier characteristic factors.

Neither proposed bound implies the other from the stated identities:

1. `KJN(C)` bounds `td`, hence the pole-leaf mass, but does not bound the
   number or product of internal characteristic gcd drops on a fixed leaf.
   The residue-A `w=2` calculus admits arbitrarily many `l=0` factors while
   keeping `td=6`, the entry masses, and the merged child fixed.
2. A bound on every \(\kappa_i\) does not bound the rooftop weights
   \(a_Pb_P\). An explicit formal two-pole entry family has
   \(\kappa_i=6\) for both poles and rooftop energy tending through the
   positive odd integers.

There is no known polynomial-origin Keller realization of either formal
family. Consequently these models prove independence of the **banked
constraints**, not a set-theoretic non-implication between conjectures on a
hypothetical class of noninvertible Keller maps. Such a set-theoretic
implication would itself be a new Keller theorem.

On the one fully fixed residue-A inventory, `KJN(1)` is already the exact
identity `td=6`; it does not follow from UCD and supplies no UCD bound. This
tautology is not a partial unification of G2 and G5.

## 1. The exact dictionary

### Lemma 1.1 -- Puiseux gcd dictionary (**EXACT**)

Let a primitive pole Puiseux series have minimal denominator \(\kappa_i\).
Write its characteristic numerator sequence as
\(\gamma_1,\ldots,\gamma_s\), and put

\[
 e_0=\kappa_i,
 \qquad e_j=\gcd(e_{j-1},\gamma_j),
 \qquad \nu_j=\frac{e_{j-1}}{e_j}.                   \tag{1.1}
\]

Then

\[
 \prod_{j=1}^{s}\nu_j
 =\frac{e_0}{e_s}
 =\kappa_i.                                         \tag{1.2}
\]

For a partial characteristic segment \(S\),

\[
 \prod_{j\in S}\nu_j\mid\kappa_i,
 \qquad
 \prod_{j\in S}\nu_j\leq\kappa_i.                \tag{1.3}
\]

**Proof.** The first equality telescopes. Minimality of the complete
Puiseux denominator gives \(e_s=1\). A partial product is a quotient of two
members of the divisibility chain
\(e_s\mid e_{s-1}\mid\cdots\mid e_0\). \(\square\)

In the Eggers--Wall tree, the characteristic vertex \(F_j\) at that gcd
drop carries

\[
 \nu_{F_j}=\nu_j,
 \qquad
 \kappa(F_j)=\nu_{F_j}\kappa(F_j^\circ)             \tag{1.4}
\]

when \(F_j^\circ\) is the next characteristic vertex toward the root.
Hence the full root-to-leaf product of the vertex indices is
\(\kappa(P_i)\).

The `P` in the user's Sigray/rooftop formula has a different range. More
literally, Sigray writes `F`:

\[
 \operatorname{td}
 =\sum_{F\in T_{a,\mathrm{pole}}}
   \frac{\alpha\beta a_Fb_F}{\nu_F},
 \qquad
 \mathcal E_{\rm MR}
 =\sum_{F\in T_{a,\mathrm{pole}}}\frac{a_Fb_F}{\nu_F}. \tag{1.5}
\]

Here \(F\) is a pole-tree **leaf**. Proposition 5.6 may aggregate several
actual punctures above one such tree vertex into its mass \(\Lambda(F)\),
but it still contributes only the one local decoration \(\nu_F\) to
(1.5). There is one pole vertex on a chosen pole path. Intermediate
characteristic vertices are not additional summands in (1.5), and a vertex
on a shared trunk can belong to several root-to-leaf products without
becoming several mass summands.

Consequently, on the residue-A branch -- where DS1 identifies every
segment vertex with a characteristic vertex of that same pole series --
the precise relationship is

\[
 \boxed{
 \nu_{P_i}\mid\kappa_i,
 \qquad
 \kappa_i
 =\nu_{P_i}
  \prod_{\substack{F<P_i\\F\ \mathrm{characteristic}}}\!\nu_F.} \tag{1.6}
\]

It is **not**
\(\kappa_i=\prod_{P\text{ lying on the branch}}\nu_P\): the latter
product has the single factor \(\nu_{P_i}\).

### Residue A

The exact template ladder is

| vertex | \(\kappa(F)\) | \(\nu_F\) | \(\bar\kappa_F\) |
|---|---:|---:|---:|
| root \(R=(0,y)\) | `1` | `1` | `1` |
| suffix \(F_s\) | `7` | `7` | `5` |
| merge \(G_m\) | `21` | `3` | `5` |
| pole \(P_i\) | `42` | `2` | `5` |

Thus

\[
 1\xrightarrow{\times7}7
  \xrightarrow{\times3}21
  \xrightarrow{\times2}42.                          \tag{1.7}
\]

At either pole the entry normalization is

\[
 (\rho,\nu,\bar\kappa)=(1,2,5),
 \qquad w=\frac{5-1}{2}=2.                           \tag{1.8}
\]

There are two pole leaves and, for both,
\((a_P,b_P,\nu_P)=(1,1,2)\). Therefore

\[
 \mathcal E_{\rm MR}
 =\frac12+\frac12=1,
 \qquad
 \operatorname{td}=2\cdot3\cdot1=6,
 \qquad
 \deg\Psi=6\cdot6=36.                              \tag{1.9}
\]

This is `KJN(1)` at equality. It uses only the pole inventory, not the
hidden factors `7` and `3`.

### The passport is a quotient invariant, not a carrier denominator

For

\[
 \beta(u)=
 \frac{u(u-2/3)^3}{(u^2-u+1/6)^2},                  \tag{1.10}
\]

the exact fibers are

| target | source multiplicities | passport part |
|---|---|---|
| `0` | \(u=2/3\) triple, \(u=0\) simple | `(3,1)` |
| `infinity` | the two roots of \(u^2-u+1/6\), both double | `(2,2)` |
| `1` | \(u=\infty\) triple, \(u=3/4\) simple | `(3,1)` |

The Riemann--Hurwitz defect is

\[
 (3-1)+(2-1)+(2-1)+(3-1)=6=2\cdot4-2.              \tag{1.11}
\]

These are all ramification points of the degree-four residual cover. They
do not enumerate the characteristic vertices of a pole branch. In
particular, the characteristic factor `7` in (1.7) occurs in the very same
banked genome, while `7` occurs nowhere in the passport.

The double index `2` at each quotient pole and the leaf index
\(\nu_{P_i}=2\) therefore agree numerically in the banked model, but they
are not the same definition: the former is the valuation of \(\beta\) at a
pole of the residual rational map; the latter is a gcd drop in the original
pole Puiseux series. No banked theorem identifies the two constructions in
families.

The exact cancellation mechanism also shows why no converse dictionary is
possible. If a common carrier `C` enters the two residual factors with
weights `3` and `4`, then

\[
 \frac{(C^4h_1)^3}{(C^3f)^4}
 =\frac{C^{12}h_1^3}{C^{12}f^4}
 =\frac{h_1^3}{f^4}.                                \tag{1.12}
\]

Thus the marked quotient can remain literally equal to (1.10) while the
cancelled carrier changes. Passport rigidity controls the right side of
(1.12); it controls no characteristic denominator of `C`.

### What D21--D25 adds (**EXACT, modular and chart-local**)

The compatible records

\[
 X_{25}\longrightarrow X_{23}\longrightarrow X_{21} \tag{1.13}
\]

retain the same leading marked quotient (1.10) at both registered primes,
but the source remains positive-dimensional:

* Row 21 and Row 23 vanish; Row 22 and Row 24 are active.
* The Row-22 ten-tail matrix has rank `4`, hence a six-dimensional deep-tail
  kernel before projection.
* On each of the `36` radical fibers,
  \(\dim X_{21}=13\) and
  \(\dim\operatorname{im}(X_{23}\to X_{21})=11\).
* On every D25 radical fiber there are `16` cells, each
  \(\mathbb A^{14}\), with `10` free projected-base coordinates and `4`
  free lift coordinates. Across the `36` radical fibers this is `576`
  cells at each prime.

This proves that the fixed leading passport forgets carrier/tower
directions through D25. It does **not** compute a new characteristic
exponent or \(\kappa_i\), and D-cutoff is not sheet depth. Hence (1.13) is
an exact finite-window obstruction to the proposed identification, not by
itself an infinite \(\kappa_i\)-family.

## 2. `KJN(C)` does not give UCD from the banked constraints

### Lemma 2.1 -- the complete exact consequence of `KJN(C)`

For fixed \((\alpha,\beta)\), `KJN(C)` implies

\[
 \operatorname{td}\leq C\alpha\beta.                \tag{2.1}
\]

Since every pole mass is at least \(\beta\), the number `m` of pole leaves
satisfies

\[
 m\leq\frac{\operatorname{td}}{\beta}
   \leq C\alpha.                                     \tag{2.2}
\]

Both inequalities are **EXACT consequences** of the banked identities.
They bound pole leaves, not internal characteristic vertices.

**Proof.** Use
\(\deg\Psi=\alpha\beta\operatorname{td}\) in `KJN(C)`, then sum
\(\Lambda(P)\geq\beta\) over the pole leaves. \(\square\)

No displayed identity bounds the number of gcd drops on one of these
`m` leaves.

### Lemma 2.2 -- residue-A constant-mass/unbounded-denominator model
(**EXACT at H1 arithmetic tier; FORMAL as to polynomial origin**)

Starting from (1.8), an `l=0` child with arbitrary
\(q\geq2\) has

\[
 (\rho',\nu',\bar\kappa';n_e,n_{\rm pat})
 =(2,q,2q+2;4q-1,1).                                \tag{2.3}
\]

From any state \((2,q,2q+2)\), an `l=0` child with arbitrary
\(q'\geq2\) has

\[
 (\rho',\nu',\bar\kappa';n_e,n_{\rm pat})
 =(2,q',2q'+2;2(qq'-1),1).                          \tag{2.4}
\]

All entries are positive integers and

\[
 w'=\frac{(2q'+2)-2}{q'}=2.                         \tag{2.5}
\]

**Proof.** Substitute `dp=q`, `dq=q+1` and then
`dp=q'`, `dq=q'+1` in the exact case-(II) step equations of
`SHEET6-DEPTH.md`. \(\square\)

Choose \(q=q'=2\) repeatedly and insert `r` such vertices between a pole
entry and the banked downstream residue-A tree. The full characteristic
product is then

\[
 \kappa_i(r)=42\cdot2^r.                             \tag{2.6}
\]

The handshake depends only on `w`, so the terminal jump cell remains

\[
 (r_{\rm merge},\nu_{\rm cell},l,M)=(2,3,1,2),
 \qquad
 (\bar\kappa,D/i,\rho)=(5,3,1/2).                   \tag{2.7}
\]

The two pole entries remain
\((a_P,b_P,\nu_P)=(1,1,2)\). Hence, for every `r`,

\[
 \mathcal E_{\rm MR}=1,
 \qquad \operatorname{td}=6,
 \qquad \deg\Psi=36,                               \tag{2.8}
\]

while (2.6) is unbounded. Thus even sharp `KJN(1)` does not imply UCD in
the residue-A sheet arithmetic.

This countermodel remains valid even under the artificial extra condition
that every newly inserted factor lie in the passport set `{2,3}`: repeated
`2` already makes (2.6) unbounded. The failure is therefore not merely
absence of a per-factor bound; `td` does not bound the number of internal
factors.

The exact `w=2` law does not force \(q\in\{2,3\}\): (2.3)--(2.4) allow
every integer \(q\geq2\). The fixed `A_4` passport cannot repair this,
because it is formed only after (1.12) cancels the common carrier.

To promote `KJN(C) => UCD` from this tier to polynomial-origin Keller
pairs would require a genuinely new statement:

> **CONJECTURE K2C (Keller degree-to-carrier theorem).** The pure-boundary
> Jacobian identity, together with polynomial origin, bounds the number and
> product of the internal characteristic indices on each pole leaf in terms
> of the rooftop pole-mass data.

`KJN(C)`, the `w` law, the passport, and D21--D25 do not prove K2C.

## 3. UCD does not give `KJN(C)`

### Lemma 3.1 -- bounded-denominator/unbounded-mass model
(**EXACT entry arithmetic; FORMAL as to polynomial origin**)

Fix \((\alpha,\beta)=(2,3)\). For each odd positive integer `b`, take two
formal pole entries with

\[
 a_P=1,
 \qquad b_P=b,
 \qquad \nu_P=2,
 \qquad \kappa_P=6,
 \qquad \bar\kappa_P=5,
 \qquad \pi(P)=\frac16.                             \tag{3.1}
\]

The entry divisibility is exact:

\[
 2\mid\alpha,
 \qquad 2\mid b\beta-1=3b-1                       \tag{3.2}
\]

because `b` is odd. The denominator `6=3*2` is compatible with endpoint
index \(\nu_P=2\), and
\(6(1-1/6)=5\). Thus UCD holds uniformly with `K=6` in this formal
family. But

\[
 \mathcal E_{\rm MR}
 =2\frac{b}{2}=b,
 \qquad
 \operatorname{td}=6b,
 \qquad
 \deg\Psi=36b.                                     \tag{3.3}
\]

Therefore no fixed `C` in `KJN(C)` follows from UCD and the entry
identities. \(\square\)

The obstruction is the rooftop numerator \(a_Pb_P\). A denominator ceiling
controls neither `b_P` nor, in general, the number of pole leaves.

### Strict residue-A qualification

If “residue-A constraints” means the **entire banked entry inventory** --
two poles, \((a_P,b_P,\nu_P)=(1,1,2)\), and type `(2,3)` -- then (1.9)
already proves `KJN(1)`. In that zero-dimensional entry sector,

\[
 \mathrm{UCD}\Longrightarrow\mathrm{KJN}(1)         \tag{3.4}
\]

is logically true only because the consequent is true without the
antecedent. It cannot close global G5: reaching this fixed inventory has
already specialized to `td=6`.

If “residue-A constraints” means only the fixed tetrahedral passport, then
(1.12) shows that the passport does not control the common carrier or its
weights, and Lemma 3.1 remains the relevant obstruction at the structural
tier.

## 4. Disposition

| question | answer |
|---|---|
| Are rooftop \(\nu_P\) and depth \(\nu_j\) the same? | Only at the pole leaf: \(\nu_P\) is one member of the branch sequence. The full product is over characteristic vertices, not pole places. |
| Does the passport determine \(\kappa_i\)? | No. The banked branch has factor `7`, absent from the passport; common carriers cancel exactly. |
| Does `KJN(C)` imply UCD from the stated constraints? | No. Lemma 2.2 keeps `td=6` and sends \(\kappa_i=42\cdot2^r\) to infinity at formal H1 tier. A polynomial-origin implication is **CONJECTURE K2C**. |
| Does UCD imply `KJN(C)`? | No in general; Lemma 3.1 keeps \(\kappa_i=6\) and sends the energy through all positive odd integers. |
| What happens on the one fixed residue-A inventory? | `KJN(1)` is already exact; UCD remains independent and open. |

Accordingly there is no honest single Keller-specific inequality presently
retiring both G2 and G5. UCD bounds the **multiplicative internal carrier
axis**; KJN bounds the **additive pole-mass axis**. A single statement that
bounded both would be a new stronger conjecture, not a reformulation of
either wall.

\[
 \boxed{
 \textbf{No unification: }\quad
 \bigl(\max_i\kappa_i\bigr)
 \ \text{and}\ 
 \sum_P\frac{a_Pb_P}{\nu_P}
 \text{ are independent coordinates in the banked model.}}
\]
