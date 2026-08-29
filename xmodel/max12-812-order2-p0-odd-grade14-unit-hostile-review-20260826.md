# Hostile review: the `p=0` odd sheet has a raw grade-14 unit

Date: 2026-08-26

Verdict: **CONFIRMED.**  In the complete normalized terminal source, the
fifth raw tail row at absolute `sigma`-grade fourteen is exactly

```text
E_(5,14) = -(21/320)*b^5*w^2.                       (0.1)
```

This identity is formed before the grade-13 equations, the predecessor
equation `F`, or any radical are used.  Since the chart is `D(b*w)`, (0.1)
is a unit.  Equivalently, on the original quadratic sheet

```text
w=e1/b^2,       k0=(12/5)w^2,

E_(5,14)=-(7/256)*k0*b^5,                            (0.2)
```

which is a unit on `D(b*k0)`.  Thus the normalized odd component over

```text
V(rs) intersect D(cs*k0),       b=cs,
```

does not prolong through terminal grade fourteen.  This does **not** treat
the other `p=0` cusp on `D(rs)`.  Here `rs` is the leading face coordinate,
not the live correction `rs1`.

## 1. Frozen inputs and custody

The source inputs inspected in full were:

| artifact | SHA-256 |
|---|---|
| terminal/Taylor/Gate-A design | `68ccd9f24318473039ce56e969915663df6bf538c5fcf72a98055f605daab4a0` |
| complete terminal compiler | `2d8507bcdab953f94a19bc6f794fe8233f466c74afcbab4f21497aab4280951a` |
| canonical tails file | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical JSON digest of all tails | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| coefficient-infinity source audit | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| grade-13 triangular theorem | `1ff6433a3122b60c6ac872cefe9b23db34918bc63467c70a67f7ffcc2e6e86d9` |
| grade-14 reducer | `55a73c7aa4ae555b46ac0abf8e824930db04954972e8aa859f3d56c101889f71` |
| grade-14 source freeze | `b018dc4e7a7cefa38cd019ed786921c93f293a03136eb647dfaf5100d23b0710` |

The original exact-Q terminal DAG has archive hash
`94e9b039d8390a41add35aa94a7db0f705bb9448638003be9a99f476f5b83f45`.
Its row manifest identifies `(ell,grade)=(5,14)` with equal source and full
root `270200`, expression SHA-256
`da69527730e513efa4027e670f8322b83941368877c6c7e841bcf5220cfe1030`.
The equality of the two roots is an exact target-absence sentinel, not a
numerical comparison.

The grade-14 producer ran as

```text
max12_812_order2_p0_odd_g14_exact_q_20260826T102720Z_Box03
```

and ended with `validator=PASS_G14_EXACT_NAVIGATION`.  Its key hashes are:

| output | SHA-256 |
|---|---|
| `grade14_reduced_exact.json` | `6e6b3f3a5b6a3f4fee4e48cff3bcfffc5e08ef788d2397e1c20b76e561fb5d09` |
| generated Singular source | `e192753935785c7f61954728276dcea466decd87ae8677086901fef3ed7d5eb8` |
| result JSON | `7a4bc318db0d75fa4f5950adea142f7403eef96784da02be7224658a50a3d147` |
| Python stdout | `2623bdc13c9427c483d98b883080a2422fdcd2b6198432070a4e668295d6a1ff` |
| Singular stdout | `05407d45ca64cf45dc9755fe6d47b80efdde5ac4e6903bc3c08d44871157b2a9` |
| validation | `8c36acf2bfb9314b544305e405b3616f0860645cf2c61a8399f974fa45ba4099` |

## 2. Grade, source orientation, and targets

The compiler indexes a series coefficient by its literal exponent of
`sigma`; there is no hidden division by two in `source_rows[(ell,d)]`.
From the frozen primitive source,

```text
p = 2*ell2*sigma^2+2*ell3*sigma^3+...,
c = b*sigma^2+cs1*sigma^3+...,
r = (p^2+sigma^2*(rs1*sigma+...))/4,
f = K^2+sigma^2*N.
```

Consequently the initial orders of the seven nonleading coefficients of
`f`, listed as `(a0,...,a6)`, are

```text
(6,5,4,4,3,2,2),                                    (2.1)
```

and the already shifted load orders are

```text
ord(k10-load)=4,       ord(k6-load)=12,
ord(k2-load)=20.                                      (2.2)
```

These shifts are exactly `Lambda^2,Lambda^6,Lambda^10` with
`Lambda=sigma^2`.  Thus the producer's label “grade 14” means
`[sigma^14]`, as required by the terminal design.

The tail orientation is also correct.  The charged convention is

```text
H_F(w)-g(z(w)) = sum_(ell>=1) r_ell*w^(-ell).         (2.3)
```

The canonical builder therefore stores
`r_ell=-[w^(-ell)]g(z(w))`; the terminal compiler consumes that stored
tail without another sign change.  A focused inverse-root reconstruction
in Section 3 independently recovers the decisive fifth-tail coefficients
with this sign.

There is no fifth-row target: the exact target vector is

```text
(0,mu2,0,mu4,0,mu6,J/4).
```

Accordingly row five is a source equation at every grade.  Even a
hypothetical nonzero fifth target would first be shifted to grade
`2*(12+5)=34`, not grade fourteen.  Hence neither a target nor a target
orientation can alter (0.1).

## 3. Independent coefficient reconstruction

### 3.1 Complete normalized-source replay

An independent sparse exact collector was written without importing the
terminal DAG implementation:

```text
cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/
  replay_row5_grade14.py
```

Its SHA-256 is
`2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258`,
and its freeze has SHA-256
`9a4f6014f8df125fcfaabad9f659991648e910f53f004a98d1065dd9b969b092`.
It reconstructs `p,c,r,N,f` directly from the design, consumes all 89
canonical fifth-tail monomials, and proves over `Q` that:

```text
[sigma^d]r5=0                 for d<14,
[sigma^14]r5=-(21/320)b^5w^2.
```

Exactly 42 tail monomials have a nonzero individual contribution at grade
fourteen.  Expanding the necessary first three source jets produces 249
raw coefficient monomials; exact collection cancels every correction-
dependent term and leaves the single monomial in (0.1).

Two independent AWS machines replayed the exact-Q identity before their
modular controls.  The controls give coefficient `700` modulo `32003` and
`20680` modulo `65521`, both nonzero.

| lane | result SHA-256 | stdout SHA-256 | validation SHA-256 |
|---|---|---|---|
| Box03 | `7ddb31adb16de20e3e73b419fd21747f7e7d6b9900ec48ce06827bdbc7f8604e` | `e38b718af198f955a95f8b72e1806d54a533f3f90e33ff1fe306546f05116a43` | `25aeed0d70a2b4f9f8739063019c1b45641f21972659cbfc6272c6a8b88dd2af` |
| r6d | `c6becf1776d900aaeca7ff92cc1de632ed464d4290d9ba7b11bf712ad225382b` | `3f418aab7b0c7918ee0e81e6412b79ca75e93ceb817f29f696d81c294d2b3f20` | `25aeed0d70a2b4f9f8739063019c1b45641f21972659cbfc6272c6a8b88dd2af` |

This replay independently reconstructs the normalized source arithmetic
but deliberately reuses the frozen canonical tails.  It is not presented
as an independent regeneration of all Faber tails.

### 3.2 Focused Faber and sign check

The part of the Faber source that can produce the surviving monomial can
be regenerated by hand-sized inverse-root algebra.  Specialize to

```text
f=z^8+A*z^5+B*z^2+C*z,
g=F12(f)+K*F10(f).
```

Starting with the unique `z(w)=w+O(w^-1)` satisfying `f(z(w))=w^8`, and
using (2.3), direct expansion gives exactly

```text
r5 = -(21/4096) A^5 K
     +(5/128)   A^3 B K
     -(5/64)    A B^2 K
     -(3/32)    A C^2.                              (3.1)
```

This independently fixes both the fifth-tail index and its sign.  In the
normalized source, after setting the irrelevant corrections to zero,

```text
A=2*b*sigma^2,
B=b^2*sigma^4,
C=(b^2*w/2)*sigma^6,
K=(12*w^2/5)*sigma^4.                               (3.2)
```

The four terms of (3.1) contribute at grade fourteen as follows:

| term | coefficient of `b^5*w^2*sigma^14` |
|---|---:|
| `-(21/4096)A^5K` | `-63/160` |
| `+(5/128)A^3BK` | `+3/4` |
| `-(5/64)AB^2K` | `-3/8` |
| `-(3/32)AC^2` | `-3/64` |

Their sum is `-21/320`.  The complete replay in Section 3.1 supplies the
separate fact that every term involving the other live corrections
cancels, rather than merely vanishing in this specialization.

## 4. Raw-ideal audit

The grade-14 reducer reconstructs the complete source first and only then
solves the four grade-13 pivots.  Its raw grade-14 term counts are

```text
(33,26,16,6,1,0,0),
```

so row five already has one term before reduction.  Its reduced count is
again one.  In particular:

- no grade-13 pivot is used to create (0.1);
- the predecessor equation `F=0` is not used;
- no radical, saturation, or denominator clearing is used;
- no late correction or load was set to zero before source formation; and
- the source/full DAG roots agree because row five has no target.

The relevant raw localized coefficient ring is a `Q`-algebra containing
`b^(-1)` and `w^(-1)`.  Therefore

```text
(-320/21)*b^(-5)*w^(-2) * E_(5,14) = 1.             (4.1)
```

Thus adjoining all earlier equations, including `F` and the grade-13
rows, cannot restore a solution.  The conclusion is an actual raw unit on
the normalized chart, not a statement inferred from a radical or from a
factor of a reduced numerator.

“Raw” here is relative to the normalized successor sheet.  The reviewed
grade-eleven/twelve support normalization has already introduced
`e0=a0=ell1=0`, `e1=b^2*w`, and the later jets as independent correction
variables.  The review does not claim that the original unreduced
grade-eleven/twelve scheme has unit ideal.  This distinction creates no
field-valued formal-arc loophole: such an arc lies on the reduced support,
and all of its later correction coefficients remain live in this source.

The normalization itself loses no point of the named open sheet.  From

```text
12*e1^2-5*k0*b^4=0,       b*k0 != 0,
```

one has `w=e1/b^2 != 0` and `k0=(12/5)w^2`; conversely these formulas
recover the original sheet.  Formula (0.2) also displays the unit directly
in its original open coordinates.

## 5. Gate A and exact scope

Gate A controls an attempted passage from the local infinity sheet to
global rational functions and then to finite-branch Taylor germs.  The
design explicitly states that Gate A is not needed to continue the same
complete terminal-infinity source.  Equation (0.1) is such a direct
terminal row.  No finite Taylor symbol, global coefficient function, deck
identification, or unproved overlap is used here.

Accordingly the local terminal unit eliminates this particular normalized
sheet before Gate A could matter.  It does not prove Gate A, and the typed
Taylor emitters remain only typed artifacts; they are simply unnecessary
for excluding this sheet.

The confirmed conclusion is limited to the `p=0` odd collision component
on `V(rs) intersect D(cs*k0)` in the `(8,12)`, order-two, `[6,2]` terminal
client.  It does not cover the `D(rs)` cusp, positive-order-load faces,
fractional slopes outside this chart, omitted infinity supports, or any
other terminal profile.  It does not by itself close all order two, all
`(8,12)`, maximum twelve, or JC2.
