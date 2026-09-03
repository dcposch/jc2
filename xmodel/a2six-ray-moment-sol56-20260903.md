# The \(A_2=6\) ray: fixed \(N=6\), the first global moment-page boundary, and the non-proper Schur interface

Date: 2026-09-03  
Lane: `a2six-ray-moment-sol56-20260903`  
Status: **PROVED-HERE arithmetic and conditional linear algebra; UNREVIEWED witness geometry; full geometric interpolation OPEN**

## Executive verdict

The replacement ray is correct as an unbounded ray of the implemented numerical census.  For every integer \(t\geq 0\), put

\[
 P=7t+6,
 \qquad (n,m)= (9P,6P),
 \qquad M=(-6P,4P,9P-2),
 \qquad (V_2,V_3)=(1,6t+5).
\]

Then

\[
 (\delta _3,\delta _2,\delta _1)=(-1,1/6,7/12),\qquad
 (A_2,A_1)=(6,2),\qquad q=1/2,
\]

and the unique \(s=3\) packing problem admits copies of a six-disc nonzero
orbit.  Two copies have \(k=12\) and \(N=6\) for every \(t\).  The exact
census rows at \(D=n=54,117,180,243\) were re-emitted, and the \(D=117\)
member is exactly the live row in `branch-orbits-v2`.

The arithmetic admits the proper packets and fixes aggregate root counts, but
does not prove attainment or determine the non-proper tree, action, support, or
sharing required by `globalinterp.py`.  The frozen driver refuses the bare
\(D=54\) skeleton:

```text
ERROR: decorated input must contain n=54 branches, got 0
```

Two conditional direct-moment **value** projections were emitted instead.
Their exact ranks show a growing proper-bottom value-column defect and a
witness value-column repair.  The exact bottom functional
\(Y^{K-1-3k}\prod_{\rm bot}(Y-\tau_i)\) begins at \(t=1\), but evaluates
generically nonzero on non-proper columns.  Hence the defect is stable only on
the bottom restriction.  The decisive interface is

\[
 S_t^{\rm geom}:\operatorname{gr}U_{\rm np}\longrightarrow
 \operatorname{coker}(\operatorname{gr}J_{{\rm bot},t}),
\]

The witness declares two numerically admissible six-disc orbits with identical
lower data.  Under a covariant full-series completion, their rigid-star
branches split into length-six and length-twelve orbits, giving four constants
before global equations.  The requested \(C_A,C_B\) impose two extra
equalities.  Full rank, weights, and constants remain conditional.

No geometric realization, full `POLY`, full `NO-RESIDUE`, or cofinal
obstruction is claimed.  No exit-price assertion is made.

## 0. Custody, method, and claim types

All eight frozen inputs passed the required SHA-256 gate byte-for-byte before
use; no mismatch occurred.  In particular, the executed `globalinterp.py` was
the charged `49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588`.

`PROVED-HERE` denotes exact algebra or rerun code; `REVIEWED INPUT` denotes a
charged promoted result; `UNREVIEWED/WITNESS-ONLY` denotes an added experimental
completion; and `OPEN` denotes a missing theorem or datum.  Section 11 bounds
and gives the cheapest test for every OPEN.

The implementation is at `moh_skeleton_full.py:69-145`; the moment equations
and input contract are at `global-interpolation-sol56-20260902.md:161-199`
and `global-interpolation-sol56-20260902.md:459-570`.  The review confirms that even the tuple plus \((k,\text{orbit
partition})\) is insufficient at
`global-interpolation-review-grok46-20260903.md:207-229`.

The D=105 report was read only after `.run.v2` reached `final_status=DONE`.
Prohibited ideation was not read; no ledger or `jc2-lean` action occurred.

## 1. Symbolic verification of the ray

### 1.1 Core skeleton and gcd chain

Fix \(t\in\mathbf Z_{\geq0}\) and \(P=7t+6\).  The proposed data are

\[
 n=9P,\quad m=6P,\quad
 M_1=-6P,\quad M_2=4P,\quad M_3=9P-2,
\]

with \(s=3\), \(V_2=1\), and \(V_3=6t+5\).  The order is strict:

\[
 M_2-M_1=10P>0,\quad
 M_3-M_2=5P-2>0,\quad n-M_3=2.
\]

Also \(m<n\), \(M_1=-m\), and \(m\nmid n\), because \(n/m=3/2\).
The gcd chain implemented at `moh_skeleton_full.py:76-82` is

\[
 d_2=\gcd(9P,6P)=3P,
 \qquad d_3=\gcd(3P,4P)=P,
\]

and

\[
 d_4=\gcd(P,9P-2)=\gcd(P,2).
\]

Since \(P\equiv t\pmod2\), \(d_4=2\) for even \(t\) and \(d_4=1\) for
odd \(t\).  Moreover \(d_s=P\geq6\), so the implemented numerical version of
(6) holds.

The two windows in (7), using the exact strict/non-strict predicate in
`moh_skeleton_full.py:91-95`, reduce to

\[
 \frac P2 < 6t+5\leq P,
 \qquad
 \frac35 <1\leq 3(6t+5).
\]

Their four positive margins are respectively

\[
 \frac{5t+4}{2},\qquad t+1,qquad \frac25,qquad 18t+14.
\]

Thus every implemented window holds for every \(t\geq0\).

Scope: printed (1) has the search cap \(n\leq100\), so only \(t=0\) lies under
it; the uncapped ray concerns the implementation.  Geometric (3)/(4) are not
scalar predicates.  See `n6-family-review-grok46-20260903.md:59-66`.

### 1.2 Radii and increment denominators

Using the exact product in `Skel._delta` (`moh_skeleton_full.py:84-89`) gives

\[
 \delta_3=1-\frac{n-M_3}{n-M_3-1}=1-2=-1.
\]

The remaining factors are

\[
\begin{aligned}
V_3(n-M_3)-d_3&=5t+4,\\
V_3(n-M_2)-d_3&=6P(5t+4),\\
V_2(n-M_2)-d_2&=2P,\\
V_2(n-M_1)-d_2&=12P.
\end{aligned}
\]

They give defining quotients \(5/6\) and \(5/12\), hence

\[
 \delta_1=7/12.
\]

For the increment denominators in (8),

\[
 A_2=\operatorname{den}(\delta_2)=6,
\]

while \(L_1=\operatorname{lcm}(\operatorname{den}\delta_3,
\operatorname{den}\delta_2)=6\), and therefore

\[
 A_1=\operatorname{den}(L_1\delta_1)
     =\operatorname{den}(7/2)=2.
\]

This is the increment-denominator definition at
`moh_skeleton_full.py:98-107`, not the absolute denominator of \(\delta_1\).

### 1.3 Conditions (9)--(13), \(q\), and \(u\)

At \(j=2\), condition (9) has

\[
 Q=V_3\frac{d_2}{d_3}=3(6t+5)=18t+15
   =6(3t+2)+3.
\]

Thus \((\triangle_2,\square_2)=(3t+2,3)\).  Since \(V_2=1\), (10) holds
and \(1\not\equiv3\pmod6\) makes (11) fail: the ray is **(10)-only**.

At the bottom,

\[
 (n/d_2,m/d_2,V_2,A_1)=(3,2,1,2).
\]

The congruences implemented in `cond1213` show (12) false and (13) true:
\(3\not\equiv0\pmod2\), while \(2\equiv0\pmod2\) and
\(3-1\equiv0\pmod2\).

Finally,

\[
 q=(1-\delta_1)\frac{de}{d+e}
   =\frac5{12}\frac{2\cdot3}{5}=\frac12,
\]

where \((d,e)=(m/d_2,n/d_2)=(2,3)\), and

\[
 u=V_3d_2/d_3=18t+15.
\]

These are exact symbolic identities.  A SymPy check and the native `Skel`
predicates agree for the four emitted members.

### 1.4 Orbit packets and fixed \(N\)

The reviewed nonzero-orbit law says that a (10) split has disc-orbit size
exactly \(A_2\), not merely a divisor of it
(`branch-orbits-v2-grok46-20260903.md:192-225`).  Since \(s=3\), the flat
packing at the unique \(D_2\) is exact, not a relaxation
(`branch-orbits-v2-grok46-20260903.md:247-265` and its review at
`branch-orbits-v2-review-gpt55-20260903.md:498-503`).  One packet therefore
has

\[
 |O|=6,\qquad w=|O|V_2=6,
 \qquad N_{\rm pkt}=|O|V_2q=3.
\]

Because

\[
 u=18t+15=6(3t+2)+3,
\]

the number \(r\) of such packets may range from \(1\) to \(3t+2\).  Thus

\[
 k=6r,\qquad N=3r,
\]

and the exact orbit-admissible set is

\[
 N_{\rm orb}=\{3,6,9,\ldots,3(3t+2)\}.
\]

Taking \(r=2\) yields \(k=12,N=6\) for every \(t\geq0\).  This proves the
fixed-\(N\) numerical claim.  It does not prove attainment by a polynomial
Jacobian pair.

## 2. Census emission at \(t=0,1,2,3\)

The hash-checking `verify_ray.py` ran the frozen
`census(D,Kmin=16,full=True)` slice; `ray-verification.json` saves the result.
Each target occurred exactly once.

| \(t\) | \(D=n\) | exact emitted \((n,m,M,V)\) | \(d_4\) | \(u\) | all assignments / target hits |
|---:|---:|---|---:|---:|---:|
| 0 | 54 | `(54,36,(-36,24,52),{2:1,3:5})` | 2 | 15 | 2 / 1 |
| 1 | 117 | `(117,78,(-78,52,115),{2:1,3:11})` | 1 | 33 | 7 / 1 |
| 2 | 180 | `(180,120,(-120,80,178),{2:1,3:17})` | 2 | 51 | 4687 / 1 |
| 3 | 243 | `(243,162,(-162,108,241),{2:1,3:23})` | 1 | 69 | 281 / 1 |

For every row, `windows_ok()` and `full_ok()` returned true,
`cond1011=(True,True,False)`, and
`cond1213=(True,False,True)`.  The native census generator is at
`moh_skeleton_full.py:154-170`.

The \(t=1\) output is exactly the live `branch-orbits-v2` row

```text
m=78 M=[52,115] Vs=11 u=33 |O|=6 (10)-only A2=6
```

at `branch-orbits-v2-grok46-20260903.md:372-380`.  That table displays
\(N_{\rm orb}=\{6,9,12,15\}\) because its reporting window begins at
\(N=6\); the unrestricted packet set here additionally contains \(N=3\).
This is an identification of the full numerical row, not an analogy based on
the common value \(A_2=6\).

## 3. The proper \(k=12\) decoration and the non-proper count

### 3.1 The tree data actually forced

Set

\[
 K=d_2=3P=21t+18,
 \qquad e=n/K=3,
 \qquad d=m/K=2,
\]

and

\[
 v=K-u=3t+3.
\]

In any realization, the reviewed top theorem supplies one major \(D_2\) and
one top-minor child.  The major \(D_2\) contains \(eu\) roots, not merely \(u\)
literal roots (`branch-orbits-v2-review-gpt55-20260903.md:90-104`).  Each
selected bottom disc has \(eV_2=3\) roots.  Consequently the two six-disc
packets contain \(ek=36\) proper roots.

The requested `NONPROPER-COUNT`

\[
 e\left(K-\sum_BV_2(B)\right)=e(K-12)=n-36
\]

is only an aggregate.  Conditional on placing the selected stars in the
distinguished \(D_2\), with no additional bottom-major packet, it splits
between two locations:

\[
 \underbrace{e(u-12)}_{\text{residual roots inside the major }D_2}
 \quad+\quad
 \underbrace{e(K-u)}_{\text{roots in the top-minor child}}.
\]

| \(t\) | \(D\) | major \(D_2\) roots \(eu\) | selected proper | residual in \(D_2\) | top minor | aggregate non-proper |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 54 | 45 | 36 | 9 | 9 | 18 |
| 1 | 117 | 99 | 36 | 63 | 18 | 81 |
| 2 | 180 | 153 | 36 | 117 | 27 | 144 |
| 3 | 243 | 207 | 36 | 171 | 36 | 207 |

Either count may split into several discs.  Calling their sum one “minor disc”
would conflate place and count.  The residual location shares the major
\(D_2\) ancestor with the selected packet; the top-minor location does not,
changing denominators, constants, and the Schur map.

### 3.2 Conditional two-packet witness with identical lower data

Let \(\xi=x^{-1}\), \(z=\xi^{1/12}\), and \(\zeta=\zeta_{12}\).  Here \(z\)
is the minimal displayed-radius uniformizer of the proper packet, not
necessarily a common uniformizer after non-proper completion; the integer
family parameter remains \(t\).  After subtracting outer terms in the major-
\(D_2\) bottom chart, a leading template for the two disc packets
\(O=A,B\) is

\[
 \widehat\tau_{O,j,\epsilon}
 =a_O\zeta^{2j}z^2
  +\epsilon\zeta^{7j}z^7+\text{higher terms},
 \quad j\in\mathbf Z/6,
 \quad \epsilon\in\{0,+1,-1\},
\]

with \(a_Aa_B\neq0\) and \(a_A^6\neq a_B^6\).  This template realizes the displayed contacts
\(\delta_2=1/6\) and \(\delta_1=7/12\), conditional on the omitted outer
series.  Each of the two six-disc orbits has the same lower data:

```text
V2=1; delta1=7/12; A1=2; bottom case=(13);
three roots per disc; p_g=pi^3-pi; p_f=pi^2-2/3.
```

If every higher term is completed covariantly, \(z\mapsto\zeta z\) sends
\(j\mapsto j+1\); after six steps the centre returns while the \(z^7\) term
changes sign.  The displayed branches then split into two orbits per packet:

- \(\epsilon=0\): one orbit of length six;
- \(\epsilon=\pm1\): one orbit of length twelve.

For the two disc packets, Galois descent therefore supplies four primitive
proper integration constants

\[
 C_A^{(0)},\ C_A^{(\pm)},\ C_B^{(0)},\ C_B^{(\pm)}.
\]

This is the direct application of “one constant per Galois orbit of branches,”
not per geometric disc orbit; see
`global-interpolation-review-grok46-20260903.md:132-150`.  Distinct orbits are
not identified by symmetry.

The user-requested two-constant specialization is still a useful conditional
model, but it must state the additional equations

\[
 C_A^{(0)}=C_A^{(\pm)}=:C_A,
 \qquad
 C_B^{(0)}=C_B^{(\pm)}=:C_B.
\]

At the descent stage \(C_A\) and \(C_B\) remain unrelated; global equations
may later relate them.  These are arbitrary specialization constraints, not
star consequences.  Non-proper constants remain undetermined until their
Galois partition is supplied.

### 3.3 Rigid star, support, and sharing

The promoted bottom star is

\[
 p_g(\pi)=\pi^3-\pi,
 \qquad
 p_f(\pi)=\pi^2-\frac23.
\]

Direct differentiation proves

\[
2p_f p_g'-3p_g p_f'=\frac43.
\]

Writing this bracket as \(\kappa=4/3\), the fixed normalization gives the
Jacobian constant \(c_J=\kappa q/(de)=1/9\); this is distinct from the packet
contribution \(N_{\rm pkt}=3\).

The parity support is exact: \(p_g\) is odd and \(p_f\) is even, compatible
with \(A_1=2\).  At the three roots \(\pi=0,\pm1\), the exact trace weights
give

\[
 \sum_{p_g(\pi)=0}\frac{p_f(\pi)}{p_g'(\pi)}=1,
\quad
 \sum_{p_g(\pi)=0}\frac{\pi p_f(\pi)}{p_g'(\pi)}=0,
\quad
 \sum_{p_g(\pi)=0}\frac{\pi^2p_f(\pi)}{p_g'(\pi)}=\frac13.
\]

These identities explain a first internal cancellation, but they do not supply
the omitted post-star tail.

In \(z\)-orders the forced radii are \(-12,2,7\).  Therefore

\[
 J(D_1,D_2)=5,
 \qquad J(D_2,D_3)=14,
 \qquad J(D_1,D_3)=19.
\]

The sharing rules forced by the tree are:

- the three branches in one \(D_1\) share its centre through \(z^6\) and
  first separate at the rigid \(z^7\) star;
- six conjugate \(D_1\)'s in a packet are Galois-related, while packets
  \(A\) and \(B\) are not Galois-identified (global equations may relate them);
- all descendants inside the major \(D_2\), including its residual
  non-proper roots, share the \(D_2\)-ancestor outer factors;
- roots in the top-minor child share only the \(D_3\) ancestor with the
  major block.

The complete tame exponent support is **OPEN**.  In particular, the skeleton
does not say whether coefficients at \(z^3,z^4,z^5,z^6\) vanish, nor which
post-\(z^7\) coefficients occur or are shared.  Assigning all omitted
coefficients to zero is a specialization, not a consequence of the Moh tuple.
This is why the manifest labels its extra non-proper contacts
`WITNESS-ONLY / UNREVIEWED`.

### 3.4 Partial-orbit refusal

`globalinterp.py` uses `verified:true` as a caller assertion and checks only
that the named representative occurs among the members
(`globalinterp.py:691-714`).  It does not reconstruct the permutation or prove
closure.  The custody wrapper therefore validates an explicit generator on
each disc orbit.  It checks that the members and images are the same six-element
set and that the generator is one six-cycle.

Deleting one member from a packet gives exit code 2 and

```text
REFUSED[PARTIAL-ORBIT]: every (10) disc orbit must contain exactly A2=6 members
```

The executed control tests five of six discs.  Under the conditional covariant
branch action, six of the twelve \(\epsilon=\pm1\) branches would likewise be
nonclosed, but that branch-level refusal was not executed.

## 4. The first moment page and the stock-emitter boundary

### 4.1 Exact global equations

To avoid collision with the characteristic exponents \(M_i\), write the
global moments as

\[
 \mathcal M_r=\sum_{i=1}^{n}\frac{H_i\tau_i^r}{D_i},
 \qquad
 D_i=\prod_{j\neq i}(\tau_i-\tau_j).
\]

The exact degree conditions are

\[
 \mathcal M_0=\cdots=\mathcal M_{n-m-2}=0,
 \qquad
 \mathcal M_{n-m-1}=1.
\]

Here \(n-m=K=3P=21t+18\).  Thus the homogeneous page has

\[
 R_{\rm hom}=K-1=21t+17
\]

rows, namely \(17,38,59,80\), and the separate monic row makes
\(18,39,60,81\) affine equations.  The distinction is essential: there are
\(K-1\) coefficients to kill and one normalization, not \(K\) homogeneous
kill equations (`global-interpolation-sol56-20260902.md:161-190`).

The direct value matrix is

\[
 A^{\rm val}_{r,i}=\tau_i^r/D_i.
\]

It is not the actual parameter Jacobian \(J\), which also differentiates root,
denominator, integration, and sharing data.

### 4.2 First raw bottom orders

For a proper branch, let \(\widehat\tau_i\) be its major-\(D_2\)-centered
coordinate.  The displayed bottom-chart valuations are

\[
 \operatorname{ord}_\xi H_i=-\frac16,
 \qquad \operatorname{ord}_\xi\widehat\tau_i=\frac16,
 \qquad \operatorname{ord}_\xi D_i=-\frac56.
\]

Consequently the raw leading order of the centered proper-block summand is

\[
 12\left(-\frac16+\frac r6+\frac56\right)=2r+8
\]

in \(z\).  A global common translation gives a triangular row-equivalent
moment system, but the \(D_2\) centering is not shared by the top-minor block.
Thus this is proper-block metadata, not an emitted global page.  Complete-orbit tracing can leave a nonzero
coefficient at that raw order only when

\[
 2r+8\equiv0\pmod{12},\qquad\text{i.e.}\quad r\equiv2\pmod6.
\]

The character-eligible rows at the displayed raw orders are therefore:

| \(t\) | \(D\) | row range | rows potentially nonzero at raw order \(2r+8\) |
|---:|---:|---:|---|
| 0 | 54 | \(0\le r\le16\) | 2, 8, 14 |
| 1 | 117 | \(0\le r\le37\) | 2, 8, 14, 20, 26, 32 |
| 2 | 180 | \(0\le r\le58\) | 2, 8, 14, 20, 26, 32, 38, 44, 50, 56 |
| 3 | 243 | \(0\le r\le79\) | 2, 8, 14, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74 |

For every other row, the displayed leading character cancels.  Its first
nonzero integer-order coefficient depends on precisely the tame support and
sharing that the charge omits.  Eligible contributions may also cancel between
the two packets.  This is not a completed first-nonzero page for all DEG rows.

The \(z^5\) bottom-to-\(D_2\) and \(z^{14}\) \(D_2\)-to-\(D_3\) labels are
junction provenance.  They do not determine coefficient matrices at those
orders without the outer unit series.  Treating a junction label as an
equation order would conflate a place with a series coefficient.

### 4.3 Why the frozen full lift was not fabricated

The minimal exact input to the frozen driver consists of a rooted tree on all
\(n\) labelled leaves, the cyclic action, every truncated \(\tau_i(z)\), all
sharing declarations, and a sufficient precision guard
(`global-interpolation-sol56-20260902.md:500-532`).  The canonical manifest in
this lane proves custody only for the proper packet and explicitly marks the
non-proper completion absent.  Passing the bare \(t=0\) fixture to the frozen
driver exits 2 with the 54-branch error quoted above.

There is also a desk-scale reason not to brute-force an invented full quadratic
lift.  At only the relative \(z^5\) bottom/\(D_2\) window, the frozen
`moh_total_degree` construction has the following lower bounds on branch-power
variables alone:

| \(t\) | \(D\) | branch-power-variable lower bound |
|---:|---:|---:|
| 0 | 54 | 417,645 |
| 1 | 117 | 4,305,807 |
| 2 | 180 | 15,744,465 |
| 3 | 243 | 38,816,019 |

These bounds omit denominator inverses, derivative products, integration/time
variables, polynomial coefficients, equations, and SymPy expression overhead.
The full lift was therefore stopped before allocation.  The scalable direct
projection described next stayed below 65 MB.

### 4.4 Unknown-count convention

The charged (4.13)/(4.16) discrepancy is repaired by one convention:

```text
Z_page includes the leading/star variables;
U_page = h_constants + |Z_page|;
u0 is not added again.
```

The rank tables below count only columns of the displayed parity projection;
they exclude integration constants and list their custody separately.  There
is no exact total global unknown count until the non-proper branch-orbit
partition and sharing data determine \(h\) and \(|Z_{\rm page}|\).  Reporting
one from \((n,m,M,V,\delta,u,v,k)\) would repeat the double-count and the
bare-tuple fallacy.

## 5. Conditional associated-graded projections and exact ranks

### 5.1 What the two emitted matrices mean

The companion driver is `box/a2six-drivers-20260903/a2six_moment_driver.py`.
It hash-checks the frozen driver, validates the two proper six-cycles, emits the
page metadata above, and defines two rational leading matrices.

In the **raw-leaf** model, each of the \(k\) rigid stars contributes three
confluent columns.  At distinct rational witness centres \(x_j\),

\[
 C_{r,(j,\ell)}={r\choose\ell}x_j^{r-\ell},
 \qquad \ell=0,1,2.
\]

Residual and top witness leaves are appended as ordinary Vandermonde columns.
In the **rigid-star macro** model, each normalized slot contributes one
ordinary Vandermonde column.  These bracket two possible maps from geometric
deformation coordinates to primitive values.  Neither is asserted to be the
unprovided actual map.

For the displayed rational matrices the ranks are exact over \(\mathbf Q\):
a maximal ordinary or confluent Vandermonde minor is a nonzero product of
pairwise centre differences and the nonzero factorials \(1!,2!\).  Independent
elimination modulo the three good primes \(1009,1013,1019\) gave the same rank
in every case.  No rational reconstruction is needed because the determinant
argument already proves the characteristic-zero value.

### 5.2 \(k=12\), homogeneous page

Each entry below is `columns / rank / left cokernel`.  The `D2` raw columns are
the 36 proper leaves plus all residual leaves inside the major \(D_2\); `full`
also includes the top-minor leaves.

| \(t\) | \(D\) | equations | raw proper | raw through \(D_2\) | raw full |
|---:|---:|---:|---:|---:|---:|
| 0 | 54 | 17 | 36 / 17 / 0 | 45 / 17 / 0 | 54 / 17 / 0 |
| 1 | 117 | 38 | 36 / 36 / 2 | 99 / 38 / 0 | 117 / 38 / 0 |
| 2 | 180 | 59 | 36 / 36 / 23 | 153 / 59 / 0 | 180 / 59 / 0 |
| 3 | 243 | 80 | 36 / 36 / 44 | 207 / 80 / 0 | 243 / 80 / 0 |

The raw value-rank increments from the residual \(D_2\) block are
\(0,2,23,44\); the top block adds no further rank because the witness has
already reached full row rank.

For the macro projection:

| \(t\) | \(D\) | equations | macro proper | macro through \(D_2\) | macro full |
|---:|---:|---:|---:|---:|---:|
| 0 | 54 | 17 | 12 / 12 / 5 | 15 / 15 / 2 | 18 / 17 / 0 |
| 1 | 117 | 38 | 12 / 12 / 26 | 33 / 33 / 5 | 39 / 38 / 0 |
| 2 | 180 | 59 | 12 / 12 / 47 | 51 / 51 / 8 | 60 / 59 / 0 |
| 3 | 243 | 80 | 12 / 12 / 68 | 69 / 69 / 11 | 81 / 80 / 0 |

Here the residual \(D_2\) value-rank increments are
\(3,21,39,57=18t+3\), and the top increments are
\(2,5,8,11=3t+2\).  The proper macro cokernel is
exactly

\[
 (K-1)-12=21t+5.
\]

The residual value columns reduce it; the top value columns fill the remainder.

### 5.3 \(k=12\), separate monic row

Adding \(\mathcal M_{K-1}=1\) gives \(K\) affine equations.  The table reports
the Jacobian/tangent rank of the same displayed witness models; consistency
also requires pairing the left kernel with the affine target, addressed in
Section 7.

| \(t\) | \(D\) | equations | raw proper rank/coker | raw \(D_2\) increment | macro proper rank/coker | macro \(D_2\) increment | macro top increment |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 54 | 18 | 18 / 0 | 0 | 12 / 6 | 3 | 3 |
| 1 | 117 | 39 | 36 / 3 | 3 | 12 / 27 | 21 | 6 |
| 2 | 180 | 60 | 36 / 24 | 24 | 12 / 48 | 39 | 9 |
| 3 | 243 | 81 | 36 / 45 | 45 | 12 / 69 | 57 | 12 |

The raw \(D_2\) witness fills the affine value-row cokernel.  In the macro
model the value rank through \(D_2\) is \(u=15,33,51,69\), leaving

\[
 K-u=v=3t+3
\]

dimensions, exactly supplied by the top-minor macro block.

### 5.4 Interpretation

Exactly for these value matrices, the proper defect grows linearly and witness
value columns fill it.  It is not family-intrinsic because the actual
tail-to-value map is missing.  The geometric parameter-Jacobian rank after
`NO-RESIDUE` and `POLY` remains OPEN.

## 6. The \(k=6,N=3\) single-orbit control

The orbit law numerically permits one six-disc packet, hence \(k=6,N=3\).
It lies below the \(N\geq6\) frontier and is a negative-control packet/value
model, not a partial orbit or realized geometry.  It counts 18 proper roots.
The residual count inside the
major \(D_2\) is now \(54t+27\), the top count remains \(9t+9\), and total
non-proper count is \(63t+36\).

On the homogeneous value page:

| \(t\) | \(D\) | equations | raw proper columns/rank/coker | macro proper columns/rank/coker |
|---:|---:|---:|---:|---:|
| 0 | 54 | 17 | 18 / 17 / 0 | 6 / 6 / 11 |
| 1 | 117 | 38 | 18 / 18 / 20 | 6 / 6 / 32 |
| 2 | 180 | 59 | 18 / 18 / 41 | 6 / 6 / 53 |
| 3 | 243 | 80 | 18 / 18 / 62 | 6 / 6 / 74 |

With monicity, the raw proper value cokernels are \(0,21,42,63\), while the macro
cokernels are \(12,33,54,75\).  In the same rational witness, the raw residual
value columns again fill all rows.  The macro residual columns leave
\(3t+2\) homogeneous or \(3t+3\) affine dimensions; top value columns fill
them.

Halving the proper packet enlarges the value-column deficit, while freely added
non-proper value columns fill it.  This cautions against treating a blind
bottom count as a global obstruction.

## 7. Stable bottom-value left kernels and the geometric Schur criterion

### 7.1 Exact polynomial description

Consider the affine bottom value matrix with rows \(r=0,\ldots,K-1\) and
\(p=3k\) proper columns.  For a coefficient vector
\(\lambda=(\lambda_0,\ldots,\lambda_{K-1})\), set

\[
 L_\lambda(Y)=\sum_{r=0}^{K-1}\lambda_rY^r.
\]

Then for a bottom column \(i\),

\[
 (\lambda^TA^{\rm val}_{\rm bot})_i
 =\frac{L_\lambda(\tau_i)}{D_i}.
\]

It follows exactly that the affine left kernel is represented by

\[
 L_\lambda(Y)=G_{\rm bot}(Y)Q(Y),
 \qquad \deg Q\leq K-p-1,
\]

whenever \(K>p\).  Its dimension is \(K-p\).  On the homogeneous page the
degree bound drops by one, giving dimension \(K-p-1\).  Choosing

\[
 Q(Y)=Y^{K-p-1}
\]

gives the distinguished monic functional

\[
 \Lambda_{t,k}(Y)=Y^{K-1-p}G_{\rm bot}(Y).
\]

It obeys

\[
 \lambda^TA^{\rm val}_{\rm bot}=0,
 \qquad \lambda^Tb_{\rm monic}=1,
\]

because its \(Y^{K-1}\) coefficient is one.  This certifies inconsistency only
when the bottom \(H_i\)-values are treated as the displayed independent
columns; it is not yet a certificate for the true tame-parameter system.

For \(k=12\), the exponent and cokernel dimensions are

\[
 K-1-p=21t-19,
 \quad
 \dim\operatorname{coker}_{\rm aff}=\max(0,21t-18),
 \quad
 \dim\operatorname{coker}_{\rm hom}=\max(0,21t-19).
\]

For \(k=6\), they are

\[
 K-1-p=21t-1,
 \quad
 \dim\operatorname{coker}_{\rm aff}=21t,
 \quad
 \dim\operatorname{coker}_{\rm hom}=\max(0,21t-1).
\]

At \(t=0\) the distinguished exponent is negative in both models and the raw
proper matrix already has full row rank.  The stable formula begins at
\(t=1\).

### 7.2 Weighted initial form on the proper packets

Let \(w_{D_2}\) be the outer centre, set
\(\widehat Y=Y-w_{D_2}\), and define
\(\widehat G_{\rm bot}=\prod_i(\widehat Y-\widehat\tau_i)\).  Translation
acts triangularly on moment rows, so the centered left kernel transports back
to the original bottom value matrix.  Give \(z\) weight 1 and
\(\widehat Y\) weight 2.  Then

\[
 \operatorname{in}_{(1,2)}\widehat G_{\rm bot}(\widehat Y)
 =\left(\widehat Y^6-a_A^6z^{12}\right)^3
  \left(\widehat Y^6-a_B^6z^{12}\right)^3.
\]

For \(t\geq1\), its weighted initial polynomial has the closed form

\[
 \operatorname{in}_{(1,2)}\widehat\Lambda_{t,12}(\widehat Y)
 =\widehat Y^{21t-19}
  \left(\widehat Y^6-a_A^6z^{12}\right)^3
  \left(\widehat Y^6-a_B^6z^{12}\right)^3.
\]

For the one-packet control, remove the \(B\)-factor and replace the exponent
by \(21t-1\).  This is the stable bottom left-kernel pattern visible cofinally.
It is **PROVED-HERE for the bottom value block**, conditional only on the
displayed proper leading template.

### 7.3 Why it is not yet a cofinal obstruction

For any non-proper column \(\eta\), the same functional gives

\[
 (\lambda^TA^{\rm val}_{\rm np})_\eta
 =\frac{\Lambda_{t,k}(\eta)}{D_\eta}.
\]

On the open set where \(\eta\) is not a bottom root and all leading denominator
units are nonzero, its leading coefficient is

\[
 \frac{\operatorname{lc}(\eta)^{K-1-p}
       \prod_{i\in\mathrm{bottom}}\operatorname{lc}(\eta-\tau_i)}
      {\operatorname{lc}(D_\eta)},
\]

which is generically nonzero.  In witness completion A, its valuation on a
residual \(D_2\) leaf is explicitly

\[
 (K-1-p)\rho_{\rm res}+\frac p6+\frac32,
 \qquad
 \rho_{\rm res}=\frac16+\frac1{6(r_{\rm res}-1)},
\]

and on a top-minor leaf it is \(15t+12\) for \(k=12\).  These finite values
are compatible with the witness value-column fill, not an attainable tame
direction.

A legal decoration must first put shared/global directions in a base/bottom
block and reserve \(U_{\rm np}\) for genuinely new non-proper-relative
directions.  Only then are the actual blocks \(J_{\rm bot},J_{\rm np}\) and
the geometric interface defined:

\[
 S_t^{\rm geom}:\operatorname{gr}U_{\rm np}\to
 \operatorname{coker}(\operatorname{gr}J_{{\rm bot},t}).
\]

A genuine cofinal obstruction would require, for every legal completion, a
nonzero normalized \(\lambda_t\) such that

\[
 \lambda_tJ_{{\rm bot},t}=0,
 \qquad
 \lambda_tJ_{{\rm np},t}=0,
 \qquad
 \operatorname{in}(\lambda_tb_{\rm monic})\neq0.
\]

Equivalently, a dual class must annihilate \(\operatorname{im}S_t^{\rm geom}\)
while detecting the target.  The displayed \(\Lambda\) is only a candidate:
an independent non-proper \(H_\eta\)-value column pairs nontrivially with it,
but that column need not be an attainable parameter direction.

The counterexample lane needs a **legal**, Galois-closed non-proper completion,
with the required support, sharing, `NO-RESIDUE`, and `POLY`, for which the
Schur image hits the monic target class.  Conversely, the obstruction lane
must prove universal Schur-annihilation over every such completion.  This is
`OPEN[NONPROPER-SCHUR]`; bottom rank excess alone is not the valuated-MDS
theorem.

## 8. Conditional tropical bases

### 8.1 Exact tree formula

For the raw scaled-GRS value matrix and a row-sized column set \(S\), let
\(T\) be its complement and let \(C(X)\) denote the sum of pairwise contacts
inside \(X\).  The Vandermonde numerator and full derivative denominators give

\[
 \operatorname{val}\det A_S=-C(\text{all leaves})+C(T).
\]

Thus a minimum-weight basis is found by minimizing \(C(T)\).  The driver does
this exactly by a finite complement dynamic program, balancing occupancies
among the three-root proper discs.

The calculation still needs a complete contact tree.  Two formal ultrametric
witnesses satisfying the numerical strict-frontier inequality were used to
expose dependence on omitted non-proper data.
Let \(r_{\rm res}\) be the residual root count inside \(D_2\).

- Completion A puts those roots in one cluster of contact
  \(1/6+1/[6(r_{\rm res}-1)]\).  Its derivative valuation is \(-3/2\).
- Completion B changes only that contact to
  \(1/6+3/[6(r_{\rm res}-1)]\).  Its derivative valuation is \(-7/6\), still
  strictly below the non-proper frontier \(-1\).
- Both put the top-minor witness cluster at internal contact 2.

These are **WITNESS-ONLY** choices.  They are not asserted to satisfy the full
Keller, support, or polynomiality conditions.

### 8.2 \(k=12\) minima

Basis compositions are ordered as
`(proper, residual-inside-D2, top-minor)`.

| \(t\) | \(D\) | completion A weight | A composition | completion B weight | B composition |
|---:|---:|---:|---:|---:|---:|
| 0 | 54 | \(467/12\) | (17,0,0) | \(621/16\) | (15,2,0) |
| 1 | 117 | \(20263/124\) | (24,14,0) | \(19745/124\) | (24,14,0) |
| 2 | 180 | \(84337/232\) | (24,35,0) | \(82027/232\) | (24,35,0) |
| 3 | 243 | \(10832/17\) | (24,56,0) | \(10566/17\) | (24,56,0) |

Every weight changes.  At \(t=0\), even the minimizing composition changes.
No listed minimum uses a top-minor column, but that is a feature of these two
chosen trees, not a conclusion forced by the ray.

### 8.3 \(k=6\) minima

| \(t\) | \(D\) | completion A weight | A composition | completion B weight | B composition |
|---:|---:|---:|---:|---:|---:|
| 0 | 54 | \(1111/26\) | (12,5,0) | \(1071/26\) | (12,5,0) |
| 1 | 117 | \(5419/32\) | (12,26,0) | \(5185/32\) | (12,26,0) |
| 2 | 180 | \(99029/268\) | (12,47,0) | \(95551/268\) | (12,47,0) |
| 3 | 243 | \(120919/188\) | (12,68,0) | \(117417/188\) | (12,68,0) |

Again every weight changes, although the displayed compositions remain the
same.  Labels within them are interchangeable subject to the balanced
per-disc profiles recorded in JSON.  This demonstrates model-dependence, not a
geometric counterexample.

## 9. Guarded comparison with the completed \(D=105\) lane

The D=105 `.run.v2` now has `final_status=DONE`.  Its sealed report does **not**
contain a global moment-rank computation, so no such number is imported here.
The safe comparison is local and structural.

For Sol's group-A member,

\[
 (n,m,K,u)=(105,70,35,25),
 \qquad A_2=18,
 \qquad q=1/2,
\]

Its gate parameters are \(\mu=1/12\), \(E=7/36\), and \(E/\mu=7/3\);
the corresponding values here are \(1/12,5/12,5\)
(`d105-rank-gate-sol56-20260903.md:168-174`).

Its orbit-admissible packet has \(k=18,N=9\).  Its optional distinguished-
\(D_2\) bookkeeping places 54 selected roots and splits the 51-root complement
as 21 residual plus 30 outside; this is not attained geometry.  The blind
local count \(2k=36\) versus 35 DEG slots gives
\(-1\), hence “not overdetermined”; the completed report explicitly types this
as a counting bound, not a rank (`d105-rank-gate-sol56-20260903.md:501-522`).

Its restricted one-disc `LOCAL-KELLER` operator is \(5\times7\), exact rank 5,
kernel dimension 2, and row cokernel 0 (`ibid.:447-499`).  Substituting this ray's
\(\mu=1/12\) and \(E=5/12\) into the same formula gives the same local
rank/nullity but a different second kernel direction.  This cannot be compared
numerically with the global conditional ranks in Section 5:
the D=105 lane emitted no full \(Q_*\), global unknown count, global equation
count, rank, cokernel, or saturation because its 51-root non-proper decoration
is missing (`d105-rank-gate-sol56-20260903.md:527-566,667-685`).

For orientation, \(D=54\) has 17 homogeneous rows and counts 36+18 roots;
D=105 has 34 and counts 54+51.  Their minimal displayed-lattice
\(D_1\)-\(D_2\) gap indices are 5 and 7 in their respective uniformizers,
not common global orders.  Both lanes stop at the non-proper interface.

## 10. Controls, resources, and reproducibility

The frozen `globalinterp.py controls` suite passed 40 checks with zero
failures.  The lane companion selftest passed 49 checks.  A fresh timed rerun
used one core, 15.28 seconds wall time, and 64,584 KB maximum resident memory.
This is well below the 30-minute/6-GB desk bound.

The required same-page controls behaved as follows:

- \((f,g)=(y,x+y^3)\) and \((y,x+y^5)\) pass the exact quotient/Lagrange
  recovery, homogeneous moments, monic moment, polynomiality, and no-log
  exponent-class checks in the frozen suite.
- For \(g=y^2-x^2-x\), the two branch coefficients of \(1/g_y\) at
  \(\xi=x^{-1}\) order 1 are \(+1/2\) and \(-1/2\).  It therefore fails
  `NO-RESIDUE` at exactly the required order.
- The rigid star passes the bracket and the three trace identities in
  Section 3.
- A five-of-six disc packet is refused before equation emission, with exit
  code 2.
- The bare \(D=54\) stock input is refused for having 0 rather than 54
  decorated branches, also with exit code 2.

Reproduction and the artifact map are in the driver-directory README; its
`SHA256SUMS` check passed completely.

## 11. Bounded OPEN register and cheapest tests

| OPEN | bounded missing quantity | cheapest decisive test |
|---|---|---|
| `OPEN[GEOMETRIC-REALIZATION]` | First member has \(D=54\), hence 54 candidate root series. | Construct a full candidate satisfying promoted local/tree constraints; then test global compatibility by `NO-RESIDUE`, DEG, and `POLY`. |
| `OPEN[NONPROPER-TREE]` | Under the selected-packet bookkeeping, 18 leaves count as 9 residual plus 9 top-minor; either may split further. | Supply both location trees separately and verify every first-separation pair. |
| `OPEN[TAME-SUPPORT]` | Before the rigid \(z^7\) split, four exponents are undecided on 36 proper branches: at most 144 raw proper slots before sharing. | Determine their character support and ancestor equalities at \(D=54\); rerun the eligible rows and the \(z^5\) junction. |
| `OPEN[TWO-CONSTANT-SPECIALIZATION]` | Four proper branch-orbit constants versus the requested two; exactly two extra equalities are missing. | Derive or reject \(C_O^{(0)}=C_O^{(\pm)}\) for one packet from the integrated local-star evaluation; conjugacy then handles its six discs, and repeat for the second packet. |
| `OPEN[FULL-GLOBALINTERP]` | At \(D=54\), the frozen quadratic lift already has a lower bound of 417,645 branch-power variables at relative \(z^5\), before other auxiliaries. | Once a full decoration exists, first emit only the linear initial/direct moment map over the three good primes; invoke the full quadratic lift only if that page survives and a sparse representation is available. |
| `OPEN[NONPROPER-SCHUR]` | The first nontrivial raw affine value cokernel is at \(t=1\): \(39\times36\), with 81 non-proper leaves counted 63+18. | On a legal \(D=117\) completion, compute the actual \(J_{\rm bot},J_{\rm np},S_1^{\rm geom}\) and target class over three primes, then certify over \(\mathbf Q\). |
| `OPEN[COFINAL-VALUATED-MDS]` | The bottom cokernel dimensions are the closed linear functions in Section 7, but four values do not control all legal non-proper completions. | Prove universal Schur-annihilation symbolically in \(t\), or exhibit one legal completion with target-hitting Schur image.  A fifth synthetic witness is not decisive. |
| `OPEN[ACTUAL-NO-RESIDUE/POLY]` | At \(D=54\), at most 54 raw residue coefficients occur before orbit descent; the exact orbit count is unknown because the non-proper action is unknown. | With completed common \(w=\xi^{1/R}\), check `[w^R]D_i^{-1}=0` orbitwise, integrate, then test forbidden supports of the surviving \(m+1=37\) coefficients. |
| `OPEN[D105-GLOBAL-COMPARISON]` | The completed D=105 gate still lacks placements/support for 51 roots (21+30). | Supply that decoration and compute its own global initial matrix; compare only matrices with the same coordinate and page conventions. |

These bounds are counts of finite objects, not claims of attainment or
complexity guarantees.

## 12. FALLACY-v2 audit and final typed result

- **Objects and attainment:** in a conditional realization \(D_j\) label
  tree-disc vertices and \(\tau_i\) are series; disc/branch orbits stay
  distinct.  Packing proves admissibility, not a
  realized carrier; `NONPROPER-COUNT` is a count; scale figures are bounds.
- **Algebra:** no pole theorem fills missing branches, no saturation or raw
  normal-form claim is made, and `POLY` remains OPEN.
- **Maps and labels:** \(z=\xi^{1/12}\), matrix rows, and columns are declared;
  \(p_g'=d p_g/d\pi\); 1009, 1013, 1019 label characteristics.  Moment rows,
  junction labels, and branch indices are not interchanged.
- **Unused hazards:** no exit price, merge-free inference, or \(M\)-descent is
  asserted.

```text
PROVED-HERE
  Ray identities and census rows; D=117 identity; star algebra and conditional
  root-count split; custody refusal; rational-matrix ranks; bottom
  kernel formula; conditional tree-DP weights; controls.

REVIEWED INPUT CONSUMED
  Nonzero orbit size; exact s=3 packing; unique major D2 and eu count;
  one constant per branch orbit; rigid star; global moment framework.

UNREVIEWED / WITNESS-ONLY
  Non-proper contact/support/sharing; rational value-projection witnesses,
  not the geometric parameter map; two-constant specialization with
  underived extra equalities.

OPEN
  Realization; non-proper tree/support; intrinsic first pages and counts;
  NO-RESIDUE/POLY; Schur image; cofinal obstruction; global D=105 comparison.

BOTTOM-LANE CONCLUSION
  The proper value-column defect grows and has a stable functional; witness
  value columns fill it, but no actual-parameter cofinal invariant is proved.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `39565`.
- Body SHA-256:
  `5faeb691779351cd8aa554e968ea07f5664e49a71b3f9a3f8e0cc439577769d0`.
- Frozen basis: `86733612c63ff5d39ce1f2b14fb4c5e94d2f5b1f`.
