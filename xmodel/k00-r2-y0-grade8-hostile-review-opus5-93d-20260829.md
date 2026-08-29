# Hostile review — nearest K00 `r=2` reseed (grade-8 `y=0` kill and grade-7 preflight)

**Reviewer:** Opus 5, independent (different-model) hostile review
**Date:** 2026-08-29
**Frozen basis:** `93db679d3160c957b0610297afccc1f2fad53125`
**Target:** `xmodel/k00-higher-valuation-contraction-and-r2-preflight-sol56-93d-20260829.md`, Sections 7–8 and item 5 of Section 1 only
**Excluded from scope:** the separate \(r\ge7\) exclusion theorem (Sections 3–4, under Grok review), Section 5's raw odd-row check, Section 6's valuation-one closure, `jc2-lean`, Lean, convergence, algebraization

## 0. Verdict

| item | claim | verdict |
|---|---|---|
| 1 | grade 4–8 equations, shifts, target absence, row indexing | `PASS_WITH_INDEXING_REPAIRS` |
| 2 | translated \(w\), the two \(A,B\) identities, load cancellations, final cubics, omitted free coefficient | `PASS` — every displayed constant reproduced exactly |
| 3 | no common zero on \(D(\kappa)\cap(D(s)\cup D(t))\) | `PASS` |
| 4 | necessity of \(y\ne0\) for an old-plane \(r=2\) survivor | `TRUE_BUT_SUPERSEDED` — strictly weaker than the producer's own grade-8 computation delivers |
| 5 | proposed grade-7 preflight (Section 8) | `FAIL_AS_SPECIFIED` — rank/kernel description is taken at the wrong locus; the packet has **zero** exclusion power |

Overall: **Section 7 stands as an exact finite-jet exclusion. Section 8 must not be
run as designed.** Two new exclusions derived during this review are typed
`REVIEW_DERIVED_UNREVIEWED` in §6 and must not be promoted on this document alone.

## 1. Custody and independence of the reconstruction

All three producer seals verify byte-exactly against the frozen tree:

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/K_VECTOR.txt
cade1704d973750e455829a3c3783d1c8444a4bb6e2b14e37e8277c83393819c  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/CONTRACTED_TARGET.txt
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

The producer's own body seal also verifies: 14379 bytes,
`efec8e4e94315afee74dc47f2658fccd9be1d99c078dadbc61f3f88b25235cf3`.

**Custody nit.** The producer's seal recipe says "every byte through the unique
`BODY-END` line". That string occurs **twice** in the file (the marker, and the
recipe sentence quoting it). The seal is still reproducible because the marker
is the first occurrence, but the word "unique" is wrong and a naive
`rfind`-based verifier reproduces a different body. Recommend "first
occurrence".

No producer scratch was used. The seven honest rows were rebuilt from
`tails.json` alone, reproducing the row/load split of
`reconstruct_tails` and `tail_dag_rows` in the frozen compiler:
569 tail terms; each monomial \(m\) over \((C_0,\dots,C_6,k_{10},k_6,k_2)\)
satisfies \(\sum m_j w_j=12+\ell\) with \(w=(8,7,6,5,4,3,2\mid 2,6,10)\); loads
occur at most linearly; the substitution is
\(C_0=(1+d_0)/256,\;C_1=d_1,\;C_2=(1+d_2)/16,\;C_3=d_3,\;C_4=(3+d_4)/8,\;C_5=d_5,\;C_6=1\).
Every number below is exact rational arithmetic in pure Python (no CAS, no
Gröbner, no floating point); the full audit runs in under 0.25 s per script.

Neither \(\kappa=k_{10,0}\) nor \(J_0\) nor any \(d_{i,r}\) was normalized to 1
anywhere in this review. The load support was held fixed at
\(k_{6,0}=k_{2,0}=0\), \(k_{10,0}=\kappa\ne0\).

## 2. Item 1 — the grade 4–8 equations, shifts, targets, row indexing

### 2.1 Shifts and target absence (confirmed)

Reproduced from the frozen compiler and re-derived: \(k_{10}\mapsto\Lambda^2k_{10}\),
\(k_6\mapsto\Lambda^6k_6\), \(k_2\mapsto\Lambda^{10}k_2\); targets are *added* with
sign \(-1\) at \(\Lambda^{14}\mu_2\) (row 2), \(\Lambda^{16}\mu_4\) (row 4),
\(\Lambda^{18}\mu_6\) (row 6), \(\Lambda^{19}J_{\det}/4\) (row 7). With the frozen
boundary \(\mu_{2,0}=\mu_{4,0}=\mu_{6,0}=0\) the earliest target grade is 15.
**No target is present at any grade \(\le 8\).** Confirmed.

### 2.2 Degree census of the rebuilt rows

Writing \(\Phi_\ell=U_\ell(d)+\Lambda^2k_{10}L^{10}_\ell(d)+\Lambda^6k_6L^{6}_\ell(d)+\Lambda^{10}k_2L^{2}_\ell(d)-\Lambda^{12+\ell}\delta_\ell\):

| row | \(U_\ell\) homogeneous degrees (term counts) | \(\min\deg L^{10}\) | \(\min\deg L^{6}\) | \(\min\deg L^{2}\) |
|---|---|---|---|---|
| 1 | 2:8, 3:7, 4:1 | 2 | 1 | 1 |
| 2 | 2:11, 3:9, 4:3 | 2 | 1 | 1 |
| 3 | 2:9, 3:13, 4:4, 5:1 | 2 | 1 | 1 |
| 4 | 2:12, 3:15, 4:8, 5:1 | 2 | 2 | 1 |
| 5 | 2:8, 3:19, 4:10, 5:3 | 2 | 1 | 1 |
| **6** | **3:21**, 4:16, 5:4, 6:1 | 2 | 2 | 1 |
| 7 | 2:6, 3:23, 4:19, 5:8, 6:1 | 2 | 1 | 1 |

Degrees 0 and 1 are absent from every \(U_\ell\) and from every \(L^{10}_\ell\)
(they cancel after the affine substitution; this is *not* visible term-by-term
in `tails.json` and is the reason a linear-term mutation is invisible to the
quadratic sector — see the control in §8). These are the facts that license
"grade 4 is \(Q(\ell)=0\)" and "the \(\kappa\)-load first enters at grade 6".

### 2.3 Row-6 / row-7 indexing — **material repair**

`Q_6 \equiv 0`: row 6 has **no quadratic part at all**. Consequently, on the
whole old-plane \(r=2\) lane,

* row 6 is identically zero at every grade \(0\le g\le 9\) in the \(y=0\) branch;
* row 6 is identically zero at grades \(\le7\) in the general branch, and its
  grade-8 coefficient vanishes identically on the grade-6 locus.

So the repeated phrase "the seven equations \(Q_i(y)=0\)" / "the seven
affine-linear grade-7 equations" over-counts: **row 6 is vacuous throughout the
region this analysis inhabits.** Stronger still, the seven quadrics
\(Q_1,\dots,Q_7\) span a space of dimension only **4** — the producer's three
"left-kernel covectors" are exact linear syzygies of the \(Q_i\) themselves,
reproduced here independently and byte-for-byte:

\[
\tfrac3{128}Q_1+\tfrac18Q_3+Q_5=0,\qquad Q_6=0,\qquad
\tfrac1{512}Q_1+\tfrac1{128}Q_3+Q_7=0 .
\]

Row 7 is correctly identified as the \(J_{\det}\) row (target \(-\Lambda^{19}J_0/4\));
it plays no role before grade 19 and none of the \(r=2\) conclusions touch it.

Independent corroboration outside the reviewed scope: the Section-5 odd
\(K_6\)-linear sector \((\tfrac34,-\tfrac3{32},-\tfrac3{512},-\tfrac3{4096})\mathscr L\)
on rows 1,3,5,7 with \(\mathscr L=d_1-\tfrac14d_3+\tfrac1{16}d_5\) reproduces exactly,
and rows 4 and 6 carry no \(K_6\)-linear term at all. Reported for information
only; the \(r\ge7\) theorem remains Grok's.

### 2.4 Grades 4–8 on the plane

With \(d=\Lambda^2\ell(s,t)+\Lambda^3y+\Lambda^4z+\Lambda^5v+\Lambda^6u+\cdots\),
\(\ell(s,t)=(2s,t/8,s,t,s,2t)\), and \(k_{10}=\kappa+\kappa_1\Lambda+\cdots\), the
\(\Lambda\)-coefficients of all seven rows are **identically zero at grades 4 and 5**
with \(y,z,v,u,\kappa_j\) all free. This is the exact statement that
\(Q_i(\ell)=0\) *and* \(DQ_i(\ell)\equiv0\) (the plane lies in the singular locus of
every \(Q_i\)), and it also forces \(c_{3,i}(\ell)=0\) and \(M_{4,i}(\ell)=0\).
Grade 6 is then **exactly** \(Q_i(y)=0\), with no \(z\), \(\kappa\), \(v\) or \(u\)
dependence — verified as a polynomial identity, matching the producer.

### 2.5 The two linear forms are not ad hoc

\(A=16w_1-4w_3+w_5\) and \(B=w_0-4w_2+2w_4\) are exactly the \(K_6\)-linear
sector of the rows: \(L^{6,\mathrm{lin}}_1=\tfrac3{64}A\) and
\(L^{6,\mathrm{lin}}_2=\tfrac3{1024}B\). Moreover every quadric lies in the ideal
they generate, \(Q_i=A\alpha_i+B\beta_i\) with explicit linear \(\alpha_i,\beta_i\)
(e.g. \(Q_1=A(-\tfrac3{2048}d_0+\tfrac9{1024}d_2-\tfrac3{512}d_4)+B(\tfrac3{128}d_1-\tfrac3{1024}d_3)\),
\(\alpha_4=\beta_4=\alpha_6=\beta_6=0\) up to the displayed forms). This is the
structural reason for both displayed identities and for
"\(A=B=0\Rightarrow\) every \(Q_i(w)=0\)".

## 3. Item 2 — translation, identities, loads, cubics, omitted coefficients

### 3.1 The \(y=0\) grade-8 system

With \(y=0\), grades 4,5,6,7 of all seven rows vanish **identically** in
\(z,v,u,\kappa,\kappa_1,\dots,k_6,k_2\). Grade 8 is the first live grade, and its
variable set is exactly

\[
\{\kappa,\;s,\;t,\;z_0,\dots,z_5\}.
\]

**Omitted-free-coefficient search: negative.** Provably absent at grade 8:
\(d_{*,5}\) (killed by \(y=0\) in \(DQ(y)[v]\)), \(d_{*,6}\) (killed by
\(DQ(\ell)\equiv0\)), \(\kappa_1\) (multiplies \(DM_4(\ell)[y]=0\)),
\(\kappa_2\) (multiplies \(M_4(\ell)=0\)), \(\kappa_{\ge3}\) (grade
\(\ge6+j\)), all of \(k_6\) (earliest \(\Lambda^9\), since \(k_{6,0}=0\) and
\(\min\deg L^6\ge1\)), all of \(k_2\) (earliest \(\Lambda^{11}\)), all targets
(earliest \(\Lambda^{15}\)). Nothing can cancel the two cubics.

### 3.2 The translation and the identities (all exact)

With \(a(s,t)=(s^2,st/8,16t^2,0,0,0)\) and \(w=z-a\):

\[
E_i=Q_i(w)+\kappa\,\mathcal L_i,\qquad \deg_\kappa E_i\le1 \text{ exactly},
\]

confirmed row by row (the \(K_0^0\) part of \(E_i(w)\) is *literally* \(Q_i(w)\);
\(a\) absorbs the cubic and quartic pieces exactly). Then

\[
Q_1(w)+8Q_3(w)=\tfrac3{2048}AB,\qquad
Q_4(w)=\tfrac3{524288}\left(B^2-64A^2\right),
\]

both residual-zero. The loads are

\[
\mathcal L_1=\tfrac5{2048}\bigl(sA+tB\bigr)+\tfrac5{4096}t(3s^2-64t^2),\qquad
\mathcal L_2=-\tfrac5{512}tA+\tfrac5{32768}sB+\tfrac5{65536}s(s^2-192t^2),
\]

with the **exact proportionalities**

\[
\mathcal L_3=-\tfrac18\mathcal L_1,\quad
\mathcal L_5=-\tfrac1{128}\mathcal L_1,\quad
\mathcal L_7=-\tfrac1{1024}\mathcal L_1,\quad
\mathcal L_4=\mathcal L_6=0 .
\]

So \(\mathcal L_1+8\mathcal L_3=0\) and \(\mathcal L_4=0\) are correct, but they are
special cases of a stronger fact the producer does not state: **there are only two
independent loads**, \(\mathcal L_1\) and \(\mathcal L_2\). Hence \(E_1+8E_3=E_4=0\)
gives \(AB=0\) and \(B^2=64A^2\), so \(A=B=0\) in characteristic zero, and the
six nontrivial grade-8 equations collapse to precisely
\(\kappa\mathcal L_1=\kappa\mathcal L_2=0\), i.e.

\[
E_1=\frac{5\kappa}{4096}\,t\,(3s^2-64t^2),\qquad
E_2=\frac{5\kappa}{65536}\,s\,(s^2-192t^2).
\]

Both constants reproduce **exactly**. Section 7 is arithmetically clean.

*Notational nit:* the producer reuses the symbol \(E_1\) for both the full row
and its restriction to \(A=B=0\); harmless here, but it should be renamed in any
promoted text.

## 4. Item 3 — the no-common-zero argument

Correct as written. On \(D(\kappa)\cap(D(s)\cup D(t))\): if \(t=0\) then
\(E_2=0\Rightarrow s^3=0\Rightarrow s=0\), excluded. If \(t\ne0\) then \(E_1=0\)
gives \(3s^2=64t^2\), so \(s\ne0\), and \(E_2=0\) gives \(s^2=192t^2\); combining,
\(576t^2=64t^2\), i.e. \(512t^2=0\), so \(t=0\) — contradiction. The two cubics
have no common zero with \((s,t)\ne(0,0)\), over any field of characteristic zero
(and the argument needs no \(J_0\) hypothesis). The source open is stated
correctly: \(D(s)\cup D(t)\), not the affine origin.

## 5. Item 5 — the proposed grade-7 preflight: `FAIL_AS_SPECIFIED`

The grade-7 equations themselves are right. Verified as polynomial identities:
the grade-7 coefficient is affine-linear in \(z\) with matrix \(DQ(y)\); \(d_{*,5}\)
does not appear; \(\kappa_1\) does not appear; the three listed left-kernel
covectors contract the right-hand side to **zero identically** (a genuine, not
automatic, check — it passes).

The preflight *design* is nevertheless wrong, in a way that makes it useless.

### 5.1 The rank statement is taken at the wrong locus

Measured directly:

| locus of \(y\) | \(\operatorname{rank}DQ(y)\) | right kernel |
|---|---|---|
| generic in ambient \(\mathbb A^6\) | 4 | 2, and constant in \(y\) |
| generic on \(V(A,B)\) | **2** | **4**, \(=\{\xi:A(\xi)=B(\xi)=0\}\) |
| on the old plane \(y=\ell(s',t')\) | **0** | **6** |

Grade 6 forces \(y\in V(A,B)\) (the producer states this correctly). So the
"fixed two-dimensional right kernel" and "three generic cokernel conditions"
describe the *ambient* matrix, not the matrix on the locus the preflight
actually inhabits. On the whole relevant locus the rank has already dropped from
4 to \(\le2\). The sentence "it does not settle the strata on which \(DQ(y)\)
drops rank" mis-frames the problem: the rank-drop stratum **is** the entire
region.

There are therefore \(7-2=5\) cokernel conditions, not 3. The two the producer
omits are \(e_4\) (row 4 alone, since \(\alpha_4=\beta_4=0\)) and
\(\mathrm{row}_1+8\,\mathrm{row}_3\) — the latter being exactly the combination
the grade-8 argument leans on, and *not* a syzygy of the \(Q_i\)
(\(Q_1+8Q_3=\tfrac3{2048}AB\ne0\); it merely vanishes on \(V(A,B)\)).

### 5.2 The preflight has zero exclusion power — it is answerable by hand

Put \(u=y_2-y_4\), \(v=y_3-8y_1\), \(\zeta_A=A(z)\), \(\zeta_B=B(z)\). On
\(V(A,B)\) the \(\kappa\)-load drops out entirely
(\(\kappa\,DM_4(\ell)[y]=\tfrac{5\kappa}{2048}(sA(y)+tB(y))=0\) for row 1, and
analogously for the others), and the seven grade-7 equations reduce **exactly** to

\[
\alpha_i\zeta_A+\beta_i\zeta_B+r_i=0,\qquad
\begin{cases}
\text{rows }1,3,5,7: & c_i\,(u,-v),\quad c=(\tfrac3{1024},-\tfrac3{8192},-\tfrac3{131072},-\tfrac3{1048576})\\
\text{row }2: & (\tfrac3{256}v,\ \tfrac3{16384}u)\\
\text{rows }4,6: & (0,0),\quad r_4=r_6=0 .
\end{cases}
\]

This is a \(7\times2\) system with determinant \(\tfrac3{16384}(u^2+64v^2)\), and all
five cokernel conditions vanish identically. Its solution is **universal**:

\[
\boxed{\;\zeta_A=A(z)=2st,\qquad \zeta_B=B(z)=s^2-64t^2\;}
\]

which is precisely \(A(a(s,t))\) and \(B(a(s,t))\) — the translation vector of
Section 7 is the grade-7 solution. Substituting it returns residual 0 in **all
seven rows for every \(y\in V(A,B)\)**, including the rank-drop strata.

**Conclusion:** the grade-7 preflight is unconditionally non-empty. Running it
as specified — Fitting/minor stratification, six charts \(D(y_j)\), charts
\(D(\kappa J_0)\cap D(s)\) and \(D(\kappa J_0)\cap D(t)\) — cannot exclude anything.
The \(\kappa\) and \(J_0\) chart splits are inert at this grade
(\(J_0\) first appears at \(\Lambda^{19}\)).

**Explicit witness (finite compatible 7-jet, exact).**
\(s=3,\;t=1,\;\kappa=5\) (not normalized), \(y=(0,1,2,-1,4,-20)\)
(\(A(y)=B(y)=0\), \(y\ne0\), \(u=-2\), \(v=-9\)),
\(z=(-53,3,2,2,3,-34)\) (\(A(z)=6=2st\), \(B(z)=-55=s^2-64t^2\)),
\(d_{*,5},d_{*,6},\kappa_1,\kappa_2,k_{6,1}\) arbitrary. All seven rows vanish at
every grade \(\le7\). Perturbing \(A(z)\) by 1 breaks grade 7 in rows 1,2,3,5,7
(and not row 4); perturbing \(y\) off \(V(A,B)\) breaks grade 6.

## 6. New exclusions derived during this review

Typed `REVIEW_DERIVED_UNREVIEWED`. These are finite-jet exclusions on the
old-plane \(r=2\) lane. They need their own hostile review before promotion.

### 6.1 The rank-2 stratum dies at grade 8

On \(u^2+64v^2\ne0\), grade 7 forces \(z=a(s,t)+w\) with \(A(w)=B(w)=0\) uniquely.
Then \(w\), \(d_{*,6}\) and \(\kappa_1\) drop out of grade 8 entirely, row 6
vanishes identically, and \(d_{*,5}\) enters only through \(A(v),B(v)\) with the
same \((\alpha,\beta)\) structure. Two grade-8 equations are therefore free of
\(d_{*,5}\), of \(w\) and of \(\kappa\):

\[
\text{row}_3/c_3-\text{row}_1/c_1=4\,\mathcal D,\qquad
\text{row}_4=-\tfrac3{32768}\,\mathcal F,
\]
\[
\mathcal D:=t\,u^2-64t\,v^2-2s\,uv,\qquad
\mathcal F:=s\,u^2-64s\,v^2+128t\,uv .
\]

The exact eliminations
\[
s\mathcal D-t\mathcal F=-2uv\,(s^2+64t^2),\qquad
s\mathcal F+64t\mathcal D=(u^2-64v^2)(s^2+64t^2)
\]
give, for \((s,t)\ne(0,0)\): either \(s^2+64t^2\ne0\), whence \(uv=0\) and
\(u^2=64v^2\), forcing \(u=v=0\); or \(s^2+64t^2=0\), whence \(u=\pm8iv\) and
\(u^2+64v^2=0\). Both contradict \(u^2+64v^2\ne0\).
**The rank-2 stratum is empty at grade 8.** (Brute-force integer scan
\(|s|,|t|,|u|,|v|\le6\): zero hits.)

### 6.2 The producer's grade-8 kill covers the whole rank-0 stratum, not just \(y=0\)

For \(y=\ell(s',t')\) anywhere on the old plane, the grade-8 coefficients of all
seven rows are **byte-identical** to the \(y=0\) grade-8 system: \((s',t')\)
does not appear at grade 8 at all (it first re-enters at grade 9). Reason:
\(DQ(\ell)\equiv0\), \(M_4(\ell)\equiv0\) and \(c_3(\ell)\equiv0\) on the plane, so
every polarization with all arguments in the plane vanishes. Hence Section 7's
computation kills \(y=\ell(s',t')\) for **all** \((s',t')\), not merely \((0,0)\).

### 6.3 Consequence for item 4

The producer's item 4 ("\(y\ne0\) is necessary") is true but strictly weaker than
their own arithmetic yields. The honest necessary condition on the old-plane
\(r=2\) lane is

\[
Q(y)=0\ \ (\Leftrightarrow A(y)=B(y)=0)\quad\text{and}\quad u^2+64v^2=0\ \text{with}\ (u,v)\ne(0,0),
\]

with \(u=y_2-y_4\), \(v=y_3-8y_1\). Over \(\mathbb Q\) (or \(\mathbb R\), or any field
in which \(-1\) is not a square) this is **empty**, so:

> **Over a rational source base the entire old-plane \(r=2\) lane is excluded at
> grade 8** — a nonzero \(\Lambda^3\) correction does not save it.

Over \(\overline{\mathbb Q}\) (any field containing \(i\)) exactly one stratum
survives grade 8 unexamined: the rank-1 stratum \(u=\pm8iv\), \(v\ne0\).

## 7. Smallest honest next exact packet

Not the Section-8 preflight. The smallest honest packet is:

**Packet N-R (rank-1 stratum, grade 8).** Fix the reduced grade-6 locus
\(A(y)=B(y)=0\); work in \(\mathbb Q[s,t,y_1,\dots,y_4]/(u^2+64v^2)\) localized at
\(v\) (equivalently over \(\mathbb Q(i)\) with \(u=8\varepsilon i v\), \(\varepsilon=\pm1\)).
There the grade-7 matrix has rank 1, so
\((A(z),B(z))=(2st,\;s^2-64t^2)+\lambda(v,u)\) with one free \(\lambda\). Impose the
six nontrivial grade-8 rows in the unknowns \((\lambda,\;w\ \text{with}\ A(w)=B(w)=0,\;d_{*,5},\;\kappa)\)
and test \(D(\kappa)\cap(D(s)\cup D(t))\).

* Size: six rows, \(\le\) 80 terms each, quadratic; two of the six are
  \(d_{*,5}\)-free and \(\kappa\)-free, as in §6.1.
* **Desk algebra, not AWS-only CAS.** The entire present audit — rebuild of all
  seven rows from `tails.json`, symbolic \(\Lambda\)-expansion to grade 9,
  ideal membership, syzygies, ranks, eliminations, witnesses and controls —
  ran in exact rationals in pure Python in well under one second per step.
  Nothing here justifies a Gröbner decomposition or a registered AWS lane.
  A CAS lane becomes appropriate only if the packet returns non-empty and the
  jet has to be pushed coefficientwise toward \(\Lambda^{19}\).
* If N-R is empty, the old-plane \(r=2\) lane is closed over \(\overline{\mathbb Q}\)
  at grade 8 and the producer's Section 7 + §6.1 + §6.2 + N-R together form the
  full statement. If N-R is non-empty, it yields only a compatible 8-jet over a
  field containing \(i\), which then has to be extended to \(\Lambda^{19}\).

**Out of scope but worth flagging.** None of this touches the non-plane \(r=2\)
lane \(d=\Lambda^2x+\cdots\) with \(x\) in another component of the quadratic cone
\(Q(x)=0\). The producer says so correctly in the last paragraph of Section 8;
that scope statement must survive into any promoted text.

## 8. Controls run

* **Positive.** Explicit exact 7-jet witness (§5.2) — all seven rows vanish at
  grades \(\le7\).
* **Negative (grade 7).** \(A(z)\to A(z)+1\): grade 7 becomes nonzero in rows
  1,2,3,5,7 and stays zero in rows 4,6 — matching \(\alpha_4=\beta_4=r_4=0\).
* **Negative (grade 6).** \(y\) moved off \(V(A,B)\): grade 6 becomes nonzero.
* **Invariance.** The free part \(w\) of \(z\) provably does not move the grade-8
  coefficients on the rank-2 stratum; confirmed numerically at three independent
  random \(w\).
* **Search.** 400 random draws of \((d_{*,5},k_{10,1..4},d_{*,6})\) on the rank-2
  stratum: no grade-8-compatible jet, as §6.1 predicts.
* **Mutation (fail-closed check on the pipeline).** Perturbing a `tails.json`
  coefficient that feeds the quadratic sector of row 4 by \(1/64\) breaks
  \(Q(\ell)=0\) and the \(Q_4\) identity; perturbing row 2's \(k_{10}\)-load
  quadratic sector breaks \(M_4(\ell)=0\). A first attempt that perturbed a
  degree-1 monomial changed nothing — recorded because it is an easy way to run
  a **vacuous** mutation control on this artifact: only monomials with
  \(m_1+m_3+m_5\le2\) reach the quadratic sector.

## 9. Jet / arc / map discipline

Everything above concerns **finite compatible jets**: coefficient tuples
satisfying \(\Phi_i\equiv0\pmod{\Lambda^{g+1}}\) for the stated \(g\), with the
frozen source boundary and unit conditions. The §5.2 witness is a compatible
**7**-jet and nothing more; §6.1–6.2 are **8**-jet exclusions on named strata.
An exclusion of \(g\)-jets excludes formal arcs of the same source type
(an arc truncates to a jet); the converse fails, and no statement here produces a
formal arc, a convergent arc, an algebraization, or a polynomial Keller map. The
producer's Section 9 states this correctly and should be retained verbatim.

## 10. Findings ledger

| # | finding | severity |
|---|---|---|
| F1 | Section 7's identities, loads, cubics and constants all reproduce exactly from the frozen tails | confirmation |
| F2 | \(Q_6\equiv0\); row 6 vacuous throughout; "seven equations" is six, and the quadrics span only dimension 4 | indexing repair |
| F3 | only two independent loads (\(\mathcal L_3,\mathcal L_5,\mathcal L_7\) are fixed multiples of \(\mathcal L_1\); \(\mathcal L_4=\mathcal L_6=0\)) | strengthening |
| F4 | \(A,B\) are the \(K_6\)-linear sector of rows 1 and 2; \(Q_i\in(A,B)\) with explicit cofactors | structural |
| F5 | omitted-free-coefficient search at grade 8, \(y=0\): negative | confirmation |
| F6 | Section 8's rank/kernel statement is taken at the ambient generic \(y\), not on \(V(A,B)\) where rank is 2 and the right kernel is 4 | material error |
| F7 | two cokernel conditions omitted (\(e_4\) and \(\mathrm{row}_1+8\,\mathrm{row}_3\)); both nevertheless vanish | material omission |
| F8 | grade 7 is unconditionally solvable with \(A(z)=2st\), \(B(z)=s^2-64t^2\); \(\kappa\) drops out; the proposed packet has no exclusion power | `FAIL_AS_SPECIFIED` |
| F9 | rank-2 stratum dies at grade 8 | new, `REVIEW_DERIVED_UNREVIEWED` |
| F10 | Section 7's own computation kills every \(y\) on the old plane, not only \(y=0\) | new, `REVIEW_DERIVED_UNREVIEWED` |
| F11 | over \(\mathbb Q\) the whole old-plane \(r=2\) lane is excluded at grade 8; over \(\overline{\mathbb Q}\) only \(u=\pm8iv,\ v\ne0\) survives | new, `REVIEW_DERIVED_UNREVIEWED` |
| F12 | producer seal recipe says "unique `BODY-END`" but the string occurs twice | custody nit |

No exit price is asserted anywhere in this review, so no `charge_basis` line is
emitted. No canonical file was edited, no commit or push was made, no external
message was sent, no web or AWS access occurred, and no heavy CAS was invoked.

**Execution-gap disclosure re `jc2-lean`.** No file inside `jc2-lean` was opened,
read, built or modified, and its pre-existing dirty submodule-pointer state is
unchanged. But the prohibition was not honoured cleanly: (i) one repo-wide
`grep -rl` for a custody hash traversed `jc2-lean` before its output was filtered;
(ii) a `find ... -path ./jc2-lean -prune` and a post-write
`git status --porcelain` pathspec each stat the path. Recorded rather than
glossed, per campaign discipline on disclosing execution gaps.

<!-- BODY-END -->

## Seal

- Body definition: every byte up to and including the terminating newline of the
  single `BODY-END` HTML-comment line above; that line occurs exactly once in
  this file, and this seal section lies outside the body.
- Body bytes: `23496`.
- Body SHA-256:
  `4a60e84331eaf363990b4438956493274c359ec4f504a028a0544ba7bca7e677`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
- Reviewed artifact: `xmodel/k00-higher-valuation-contraction-and-r2-preflight-sol56-93d-20260829.md`,
  body 14379 bytes, body SHA-256
  `efec8e4e94315afee74dc47f2658fccd9be1d99c078dadbc61f3f88b25235cf3` (verified).
