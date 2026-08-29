# G2: intrinsic exact-pair Newton--Puiseux closes L3/L5 at the coverage layer

**Date:** 2026-08-28  
**Lane:** Sol Ultra, exact desk theorem  
**Status:** provisional pending different-model hostile review  
**Computation:** none; no CAS and no AWS

## 0. Verdict

The campaign's current `L3/L5 open` label conflates two different source
architectures.

- For the **hybrid GGV/VGG-to-Sigray transport**, `H-TRUNC` remains open:
  nothing yet proves that the selected VGG translation subsequence is the
  strict truncation of an actual fibre branch.
- For the preferred **intrinsic exact-pair two-chart constructor**, L3 and
  L5 are consequences of ordinary all-root Newton--Puiseux plus
  normalization.  Sigray's Proposition 3.1 already states the load-bearing
  multiplicity count for every prefix.  The Kummer action on a common
  denominator has orbit size equal to the reduced branch denominator, and
  its orbits are exactly the boundary places.

Thus, after independent review, the intrinsic coverage layer may be recorded
as

```text
L3 exact-fibre strict truncation                         available
L4 both-chart boundary-place coverage                   available
L5 leaf / deck-orbit / normalized-place bijection       available
```

This does **not** supply the repaired Sigray decorations at every ancestor,
landing, `RPMC(C)`, a cofinal degree ceiling, or JC2.

## 1. Source and exact theorem

Let `K` be algebraically closed of characteristic zero, let

```text
h(x,y)=f(x,y)-a in K[x,y]
```

be squarefree, and let `C` be the reduced affine curve `h=0`.  Write
`Cbar^nu` for the disjoint union of the normalizations of the projective
closures of its irreducible components.  In the `x=infinity, y=finite`
chart put

```text
B_x={S in Cbar^nu-C : ord_S(x)<0 and ord_S(y)>=0},
u=1/x,
e_S=ord_S(u)=-ord_S(x)>0.
```

Choose a positive integer `kappa` divisible by every `e_S`.  After the base
change `u=t^kappa`, let `L_x(kappa)` be the set of complete Puiseux leaves

```text
y=phi(t) in K[[t]]
```

of the `x`-chart factor of `h(t^-kappa,y)`.  The group `mu_kappa` acts by
`phi(t) -> phi(zeta*t)`.

> **Theorem EPL (exact-pair leaf theorem).**
>
> 1. At every finite Puiseux prefix, the multiplicity of a residual root is
>    exactly the number of complete leaves extending that prefix.  Hence an
>    all-root Newton--Puiseux construction neither skips nor invents a branch,
>    and its cumulative translation is the strict truncation of every leaf
>    below the current exponent.
> 2. The natural descent map induces a bijection
>
>    ```text
>    L_x(kappa)/mu_kappa  <-->  B_x.
>    ```
>
> 3. If a leaf lies over `S`, its least Puiseux denominator is `e_S`, its
>    `mu_kappa` orbit has size `e_S`, and its stabilizer has size
>    `kappa/e_S`.

The identical statement holds after interchanging `x` and `y`.

For a normalized Keller pair, `df` is nowhere zero because
`df wedge dg` is a nonzero constant.  Therefore every fibre `f=a` is smooth
and in particular squarefree.  The normalized rectangle/NE-corner condition
gives the already reviewed dichotomy that every boundary place is in exactly
one of the two finite-transverse-coordinate charts.  Applying Theorem EPL in
both charts gives L3--L5 for the intrinsic exact-pair constructor.

## 2. Proof

### 2.1 Local normalization and the reduced denominator

For `S in B_x`, smoothness of the normalization gives

```text
Ohat_(Cbar^nu,S) = K[[z]].
```

Since `ord_S(u)=e_S`, initially `u=z^e_S*v(z)` with `v(0)!=0`.  In
characteristic zero the unit `v` has an `e_S`-th root in `K[[z]]`; replacing
`z` by `z*v(z)^(1/e_S)` gives

```text
u=z^e_S.
```

The local branch is therefore represented by

```text
y=sum_(n>=0) b_n u^(n/e_S).
```

The denominator is reduced.  Indeed, on each nonvertical irreducible plane
component `K(C)=K(x)(y)`.  The completed local factor over `K((u))` has
residue degree one and ramification degree `e_S`, hence degree `e_S`; its
displayed root `y` generates that factor.  If all nonzero exponents had a
common denominator `d<e_S`, the root would lie in `K((u^(1/d)))`, forcing
the local factor degree to be at most `d`, a contradiction.  A vertical
component cannot occur in `B_x`; it belongs to the other chart and has the
same argument after swapping coordinates.

### 2.2 Common denominator and Kummer orbit

Embed the branch in the common base change by `u=t^kappa`.  Its leaves have
the form

```text
phi(t)=sum_n b_n t^(n*kappa/e_S).
```

Reducedness says `gcd(e_S,{n:b_n!=0})=1`.  For `zeta in mu_kappa`, the leaf
is fixed precisely when

```text
zeta^(n*kappa/e_S)=1 for every n with b_n!=0.
```

The reduced gcd condition makes this stabilizer the subgroup of order
`kappa/e_S`; orbit--stabilizer gives orbit size `e_S`.

The base-changed normalization is the normalization of `Cbar^nu` after
`u=t^kappa`.  Its points above a fixed `S` are exactly the `e_S` conjugate
embeddings just displayed, and `mu_kappa` acts transitively on them.  Points
above different `S` cannot meet under this action because the quotient map
descends to `Cbar^nu`.  Therefore Kummer orbits of complete leaves are in
bijection with the original normalized boundary places.

### 2.3 All-root prefixes are actual strict truncations

At a common grid exponent `n/kappa`, write the current prefix as

```text
sum_(j<n) c_j x^(-j/kappa)
```

and make Sigray's substitution

```text
eta_n=x^(n/kappa)*(y-sum_(j<n)c_j*x^(-j/kappa)).
```

Sigray Proposition 3.1 says that the degree of the leading residual
polynomial is the number of Puiseux series with the shorter prefix, and the
multiplicity of a root `c_n` is the number of series with the extended
prefix through `c_n`.  Its proof identifies those series with points on the
smooth compactification of the base-changed curve.  Sigray Statement 3.9(i)
then records the same equality recursively as

```text
mult(p_(h,F),c)=deg(p_(h,F*c)).
```

Consequently retaining **every** residual root with its multiplicity retains
every complete leaf exactly once as a presentation.  The accumulated sum is
literally the strict truncation of each retained leaf.  Zero coefficients
create no hidden terms: they are grid positions with residual root zero and
are included in the prefix equality.  Once distinct leaves separate, Hensel
lifting supplies their unique algebraic continuations; the finite leaf may
store that exact factor rather than an infinite coefficient list.

This proves the exact-pair form of L3.  Section 2.2 proves the quotient/no-
duplication form of L5.

## 3. Primary-source custody

The pinned source is

```text
refs/sigray_full.pdf
SHA-256 9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
```

Relevant printed locations:

- Statement 3.1 and Definitions 3.1--3.3, PDF pp. 10--11: two Puiseux forms,
  characteristics, contacts, and the two Eggers--Wall components;
- Notations 3.7--3.10, PDF pp. 12--13: a common suitable `kappa`, strict
  truncation, and the residual polynomial;
- Proposition 3.1 and proof, PDF pp. 13--14: exact degree/multiplicity counts
  and the bijection with points on the smooth compactification after the
  `t^kappa` base change;
- Statement 3.9, PDF pp. 14--15: recursive multiplicity/degree transport.

The orbit--stabilizer and reduced-denominator argument in Section 2.2 is
spelled out here because Proposition 3.1 counts base-changed presentations
but does not itself state the quotient formula.

## 4. What this closes, and what it does not

### 4.1 Closed after review: intrinsic exact-pair coverage layer

The source object contains the exact polynomial `h=f-a`.  Running the
all-root algorithm in both physical charts and quotienting complete leaves by
the common Kummer action gives:

```text
exact branch truncations                         L3
all normalized boundary places in both charts   L4
one leaf orbit per place, with e/stabilizer      L5
```

Substituting the exact second component `g` in a leaf field gives its
pole/finite tag and is invariant under presentation conjugacy.

### 4.2 Still open: decoration and global proof

The theorem does not prove that the later Sigray labels consumed by the books
are all sound.  In particular it does not repair the Proposition 4.2
constant-leading-part existence gap or automatically provide the corrected
`lambda_F,M_F,Q(F)` and complete approximate-root tower degrees at every
ancestor.  It also proves no landing theorem, bounded delay, `RPMC(C)`, type
bound, cofinal total-degree ceiling, Keller contradiction, or JC2 result.

### 4.3 Hybrid firewall

Nothing here identifies a VGG/GGV selected translation chain with these
intrinsic prefixes.  A hybrid client must still prove `H-TRUNC`, the common
`P/Q` face-root identification, and source-to-place coverage.  The theorem
removes L3/L5 only from the **pure exact-pair** route; it does not revive
`C74-PLACE`, transpose coverage, or VGG minimal re-selection.

## 5. Review charge

An independent review should attack, in order:

1. whether the least Puiseux denominator must equal `e_S` when `y` is the
   plane primitive element;
2. the stabilizer size `kappa/e_S` and absence of cross-place collisions;
3. whether Sigray Proposition 3.1 counts base-changed presentations or
   original places, and whether the quotient above corrects that distinction;
4. vertical components and reducible squarefree fibres;
5. the exact boundary between the intrinsic theorem and the still-open
   hybrid `H-TRUNC` assertion.

No repository file other than this report was modified by this lane.  The
user-owned `jc2-lean` tree was not entered, read, searched, built, statused,
or modified.
