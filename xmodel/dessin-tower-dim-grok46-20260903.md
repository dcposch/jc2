# DESSIN-TOWER expected dimension — admissible covers of Moh's major-disc tree

Lane: Grok 4.6. Charge `OPEN[DT-DIM]`, round `20260903T1015Z`, Card II of
the charged Grok ideation. Desk only. Canonical ledgers not edited.
`jc2-lean` not inspected. No other `ideation-20260903T1015Z-*` file than
the two charged was opened. No running-lane report was opened.

## 0. Custody and hashes

Frozen inputs, SHA-256 verified byte-exact before any read:

```text
7b56aad2c1fb067481852eedecc89ba5598cd26eeb2cf3358c3b8c2f16438015  ideation-20260903T1015Z-grok46.md
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  ideation-20260903T1015Z-opus5.md
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  time-function-endgame-review-sol56-20260902.md
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  bottomode.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

Moh pages used as images (paper page \(N\) = PDF page \(N-139\)): Prop 4.6
at 170–171, Def 5.1 at 179, the split degrees at 182, A.3 at 205, Appendix
II opening at 207. `FALLACY-v2` in force. No new exit-price assertion, so
no `charge_basis` line.

## Direct answer

The object is a genus-0 admissible cover of the dual graph of Moh major
discs, with a STAR-ABC (Davenport–Stothers) Belyi map at every bottom
vertex and a Prop 4.6 leading-form pair at every internal vertex. After
the internal ODE is reduced by Moh A.4 to A.3, that pair is also a
three-point cover (PROVED-HERE, §2). Every vertex therefore contributes
\(r_v-3=0\). The residual moduli are the positions of the \(k\) bottom
nodes on the stable core of the tree.

**Primary formula (Reading A, 3-point internals):**

\[
\operatorname{expdim}_A(S,k)=\max(k-2,\,0).
\]

It is \(\ge 0\) on Moh's six printed rows at every UNI integer-\(N\)
packet (HARD gate passed). It does **not** separate the 652 excess
(1)–(13) rows from the six. On the D = 105 trio it is strictly positive
(\(10\) through \(22\) at \(N\ge 6\)). On the 840 UNI \(N\ge 6\)
V-assignments in \(48\le D\le 120\) (670 groups, matching the charged
census-rebase count): **821 positive, 19 zero, 0 negative.** Mean
\(\operatorname{expdim}_A\) grows with \(D\) (8.39 on [48,80], 11.21 on
[81,100], 13.62 on [101,120]).

Trichotomy: combinatorics of this Hurwitz count **cannot finish JC2**.
The types with \(\operatorname{expdim}_A=0\) are 19 rigid isolated CE
candidates (listed in §6.4); the rest are a positive-dimensional family
growing in \(D\). The all-degree proof, if it exists, is Q3(a)
(irregularity of the pencil Gauss–Manin), not \(\operatorname{expdim}<0\).

The Opus Card 3 count \(k-(n-m)\) is **not** a special case of
\(\operatorname{expdim}_A\). It subtracts interpolant-polynomiality
relations that are not Hurwitz data. It is negative on all six and on
both charged controls, so it is the wrong dimension (Opus outcome (iii),
confirmed). \(V_2=1\) skeletons are the **large-\(k\)** end of the UNI
window (because \(q\) is a proper fraction and \(N=kV_2 q\ge 6\) forces
\(k\ge 7\)); they have \(\operatorname{expdim}_A\ge 5\), not a kill.

---

## 1. The object

### 1.1 Skeleton and packet

A Moh skeleton is \(S=(n,m,M_2,\dots,M_s,V_2,\dots,V_s)\) in the sense of
`box/moh_skeleton_full.py` (Def 5.1 + printed (1)–(13)). Write
\(K=\gcd(m,n)\), \((d,e)=(m/K,n/K)\), \(d_1=n\), \(d_{i+1}=\gcd(d_i,M_i)\),
\(M_1=-m\), \(M_s=n-2\), \(V_{s+1}=d_{s+1}\). The UNI packet is an integer
\(k\ge 1\) with \(k V_2\le u:=V_s K/d_s\) and
\(N=k V_2 q\in\mathbb{Z}\), \(q=(1-\delta_1)\,de/(d+e)\). The integer
\(k\) is the number of bottom-major discs in one Galois orbit.

### 1.2 Dual graph \(\Gamma(S,k)\)

Vertices: one per major disc of a UNI realisation of \(S\) with \(k\)
bottoms. Edges: inclusions \(D_{j+1}\supset D_j\).

Def 5.1(1) (paper 179): \(D_j\) contains \(a_j=n V_{j+1}/d_{j+1}\) roots
of \(g\). In particular \(D_s\) contains all \(n\) roots of
\(g\prod T_i^\psi\), so \(n_s=1\). The number of major children of \(D_s\)
of the given \(V_s\)-type that can fill \(D_s\) is \(d_s/V_s\) when this
is an integer, else 1 (one major plus minors). **Measured:** this filling
number is \(1\) on all 840 UNI \(N\ge 6\) V-assignments in \(48\le D\le 120\),
and on all six printed rows. The UNI tree is therefore a **bamboo of
internal discs** \(D_s\supset\cdots\supset D_2\) (one disc per level
\(j\ge 2\)) with a **star of \(k\) bottoms** attached to \(D_2\).
Component count before stabilisation: \(c=k+(s-1)\).

### 1.3 The cover, marked points, prescribed vs moduli

Let \(C\) be a nodal curve of arithmetic genus 0 with dual graph
\(\Gamma(S,k)\). A **dessin tower** of type \((S,k)\) is a finite
admissible cover \(\varphi\colon X\to C\) (Harris–Mumford: nodes to nodes,
matching ramification, no ramification in the smooth locus except at
marked branch points) with the following restrictions.

**Bottom vertex** (disc \(D_1\)). STAR-ABC, promoted
(TFE opus5 Thm STAR-ABC; review sol56 §5 CAN-promote). The pair
\((p_f,p_g)\) of leading forms, \(\deg p_g=eV_2\), \(\deg p_f=dV_2\),
satisfies \(d\,p_f p_g'-e\,p_g p_f'=\kappa\in\mathbb{C}^\times\),
equivalently \(R=p_f^e/p_g^d\colon\mathbb{P}^1\to\mathbb{P}^1\) is Belyi
of degree \(deV_2\) with passport

\[
\bigl[e^{dV_2}\bigr],\quad\bigl[d^{eV_2}\bigr],\quad
\bigl[(d+e)V_2-1,\,1^\gamma\bigr],
\qquad\gamma=V_2(de-d-e)+1.
\]

Existence for every \((d,e,V_2)\) remains `OPEN[STAR-ALLV]`; it is not
used as a skeleton kill (STAR-REALISABILITY: zero kills on the decided
range). The source of \(R\) is the \(\pi\)-line of \(D_1\). One of the
three branch values lives at \(\pi=\infty\), which is the node toward
the parent.

**Internal vertex** (disc \(D_j\), \(j\ge 2\)). Def 5.1(4): Prop 4.6
holds at the general point \(\sigma_j\) with
\(v=V_{j+1}(d_j/d_{j+1})\). Prop 4.6 (paper 170–171), \(r\ge 2\):
leading coefficients of \(g(\sigma),T_1^\psi(\sigma),\dots,T_{r-1}^\psi(\sigma)\)
are powers of a common polynomial \(p(\pi)\) of degree \(v\); 
\(T_{r,\sigma}^\psi=p^\alpha\cdot q\) with \(q\) squarefree of degree
\(v(n-M_r)/d_r\), every root of \(p\) a root of \(q\), and \(p\) not a
power of \(q\). At the split from \(D_r\) to \(D_{r-1}\) (paper 182):

\[
\deg p=V_r\frac{d_{r-1}}{d_r},\qquad
\deg q=V_r\frac{n-M_{r-1}}{d_r}>1.
\]

The printed text does **not** name a ramification profile of a map
\(\mathbb{P}^1\to\mathbb{P}^1\) at an internal vertex. Two readings are
in §2.

**Prescribed by \(S\):** the graph type (bamboo-star of depth \(s\) with
\(k\) leaves, once \(k\) is given), the numerical windows \(V_i,M_i,d_i\),
the STAR-ABC passport, and the Prop 4.6 degrees \((\deg p,\deg q)\) at
each internal split. Radii \(\delta_i\) (Def 5.1(3)) pin the gluing
*scales*.

**Moduli, named as charged:**

1. **Branch constants \(a_O\) per orbit.** The \(k\) centres of the
   bottoms, as roots of the director polynomial \(\Psi\) on \(D_2\).
   UNI = one Galois orbit, so one such \(k\)-set. After \(\mathrm{PGL}_2\)
   of the core, \(k-3\) essential cross-ratios, plus the outer mark of
   §3, net \(\max(k-2,0)\).
2. **DS moduli \(\gamma\) per bottom star.** The symbol \(\gamma\) in
   STAR-ABC is the passport integer \(V_2(de-d-e)+1\), the number of
   simple points in the third profile. It is **not** a dimension. The
   expected dimension of one STAR-ABC pair, after affine source
   normalisation and scaling, is \(\mu_{\mathrm{DS}}=0\): STAR-ABC
   itself counts \(b_1-2=dV_2-2\) truncation equations in \(b_1-2\)
   essential parameters of monic \(Q\) (TFE opus5 §4.2). For
   \((d,e,V_2)=(2,3,1)\) this is \(0\) equations in \(0\) parameters,
   unique pair, field of moduli \(\mathbb{Q}\) (review sol56 §5; the
   explicit star \(p_g=\pi^3-\pi\), \(p_f=\pi^2-2/3\)). The charge's
   phrase “DS moduli \(\gamma\)” is a label collision; we keep \(\gamma\)
   as passport data and \(\mu_{\mathrm{DS}}=0\).
3. **Outer coefficients shared at junctions.** Puiseux coefficients of
   the common truncation \(w(t)\) on \(D_j\) with exponents in
   \((\delta_{j+1},\delta_j)\). Characteristic exponents are prescribed
   by \(S\). Non-characteristic coefficients are Tschirnhausen-killable
   (Appendix II). Two readings of the leftover count: **O1** = 0
   (nothing beyond \(S\)); **O2** = \(s-2\) (one intermediate
   characteristic coefficient per extra level). Neither is a full
   Zariski-moduli computation of the equisingular stratum;
   SOURCE-UNVERIFIED as an exact count from the printed text.

**Automorphisms.** \(\mathrm{PGL}_2\) of each component is already
subtracted as the \(-3\) in \(r_v-3\). Residual \(\mathrm{Aut}(\mathbb{A}^2)\)
that preserve the skeleton type is absorbed into Moh's gauge for the
census objects; for the two controls it is checked separately (§5).
Finite deck groups do not change expected dimension.

**Node conditions.** Ramification-index matching at a node is a discrete
constraint on which passports glue (0-dimensional). Analytic gluing of
local parameters is part of the definition of an admissible cover, not
an extra equation. The radii \(\delta_i\) pin scales, so there is no
smoothing modulus on the stratum (smoothing would leave the dual graph).

---

## 2. Internal passport: two readings

Prop 4.6 plus A.4 (paper 206) reduce the internal ODE to A.3 (paper 205):

\[
D(m,Q,p,q):=m\,p\,q'-Q\,q\,p'=c\,p,\qquad c\neq 0,
\]

with \(m=\deg p\), \(Q=\deg q\), \(q\) squarefree, every root of \(p\) a
root of \(q\), \(p\) not a power of \(q\), and at least one root of \(p\)
of multiplicity \(>m/Q\).

### Reading A (Belyi / 3-point). Licensed by the ODE, used as primary

Put \(R=q^m/p^Q\). Then

\[
\frac{R'}{R}=m\frac{q'}{q}-Q\frac{p'}{p}=\frac{D(m,Q,p,q)}{pq}=\frac{c}{q},
\]

so \(R'=c R/q\). Every finite critical point of \(R\) lies among the
roots of \(q\). The values of \(R\) there are \(0\) or \(\infty\). At
source-infinity, \(R(\infty)=\rho:=(\mathrm{lc}\,q)^m/(\mathrm{lc}\,p)^Q\),
and the local degree is \(Q-1\) whenever the leading terms of \(q^m-\rho p^Q\)
cancel (the A.3 degree count, parallel to STAR-ABC). For \(Q>2\) this is
genuine ramification over \(\rho\). Thus \(R\) is branched over **at most
three points** \(\{0,\infty,\rho\}\). Paper 182 requires \(Q>1\); the
boundary \(Q=2\) is a 2-point (cyclic) degeneration, still expected
dimension 0 after Aut.

**The internal vertex is a 3-point cover, \(r_v=3\), contribution \(0\).**
This is the DS-type condition at every level that the Grok ideation
named, now with a map. It is **not** the STAR-ABC passport: the profiles
depend on the multiplicity vector of \(p\) along the roots of \(q\).

That multiplicity vector is a partition of \(\deg p=V_r d_{r-1}/d_r\),
one part of which is \(V_{r-1}\) for the chosen major child, the others
either major-window parts or minor parts \(\le d_{r-1}/(n-M_{r-1})\)
(Prop 6.1). The printed Prop 4.6 does not choose the partition.
SOURCE-UNVERIFIED as a unique numerical passport. Two sub-readings of
the partition (not needed for dimension, both give \(r=3\)):

- **A1 (UNI major-orbit).** \(p=c\prod_{i=1}^{n_{\mathrm{child}}}(\pi-a_i)^{V_{r-1}}\)
  with \(n_{\mathrm{child}}=k\) at \(D_2\). Extra roots of \(q\) are
  minor-disc centres.
- **A2 (Card I full partition).** Any (10)∨(11)-admissible partition of
  \(\deg p\) with Galois orbits of size \(A_{r-1}\). Finite list.

### Reading B (polynomial-\(q\), pre-ODE). The other natural reading

The printed conclusions (2)–(5) of Prop 4.6 specify a squarefree
polynomial \(q\) of degree \(Q=V_r(n-M_{r-1})/d_r>1\) containing the
roots of \(p\). They do not mention a Belyi map. If one takes
\(q\colon\mathbb{P}^1\to\mathbb{P}^1\) itself as the cover of the
component, a generic squarefree polynomial of degree \(Q\) has \(r=Q\)
branch values (\(\infty\) plus \(Q-1\) finite critical values) and
contribution \(Q-3\). The A.3 ODE is then *additional* structure, not
part of the passport. This reading **overcounts** if Reading A is right
(the ODE rigidifies \(Q-3\) down to 0). It is recorded as
\(\operatorname{expdim}_B\) in §4 and evaluated; it never goes negative
on the charged sets.

---

## 3. Derivation of \(\operatorname{expdim}(S,k)\)

**Step 1.** Each bottom component is a 3-point cover: \(r=3\),
contribution \(0\). \(\mu_{\mathrm{DS}}=0\) after source Aut, so a
Galois orbit of identical stars adds no DS moduli. (For \((2,3,1)\):
one orbit, field of moduli \(\mathbb{Q}\).)

**Step 2 (Reading A).** Each internal component is a 3-point cover:
\(r=3\), contribution \(0\).

**Step 3.** The bamboo \(D_s\supset\cdots\supset D_3\) consists of
components with two special points (parent node + one child). These are
unstable and contract in the Deligne–Mumford compactification. After
contraction one has a single core component, the \(\pi\)-line of \(D_2\),
with

- \(k\) marked points (the bottom nodes, the roots of \(\Psi\)),
- \(1\) marked point (the outer direction, formerly the parent node,
  the place at infinity of the original \(x\)-chart).

So \(n_{\mathrm{marked}}=k+1\). For \(k\ge 2\) this is stable,
\(\dim\overline{\mathcal{M}}_{0,k+1}=(k+1)-3=k-2\). For \(k=1\) the
core itself is unstable (\(n=2\)); the whole tree contracts to the
unique bottom \(\mathbb{P}^1\) with its three STAR-ABC points, dimension
\(0\). For \(k=0\) there is no tower.

**Step 4.** Node matching is discrete (Step 0-dimensional). Outer
coefficients: O1 adds 0; O2 adds \(s-2\). Primary uses O1 (characteristic
data already in \(S\); Appendix II's 7–17 variables appear only after
Prop 6.3 reduction of *polynomial* pairs, which is Card III, not this
Hurwitz count).

**Step 5.** Therefore

\[
\operatorname{expdim}_A(S,k)=\max(k-2,\,0).
\]

The arguments \((d,e,V_*,s)\) enter the *domain*: the admissible \(k\)
are those with \(k V_2\le u(S)\) and \(k V_2 q(S)\in\mathbb{Z}\). They
enter the passport (STAR-ABC \(\gamma\), Prop 4.6 degrees) and the
existence GAP `OPEN[STAR-ALLV]`. They do not enter the integer
\(\operatorname{expdim}_A\) except through \(k\). Under Reading B they
also enter through \(Q_j(S)\).

A variant with top-filling \(r=d_s/V_s>1\) and equal UNI split of the
\(k\) bottoms among \(r\) mids was implemented; it coincides with
\(\operatorname{expdim}_A\) on the whole charged slice because \(r=1\)
identically there.

---

## 4. Closed formulae (primary and comparators)

| tag | formula | status |
|---|---|---|
| **E0 = \(\operatorname{expdim}_A\)** | \(\max(k-2,0)\) | **PRIMARY.** Reading A, O1. |
| E1 | \(\max(k-2,0)+(s-2)\) | O2 outer. Same sign pattern as E0 on \(s=3\); strictly positive on all UNI \(N\ge 6\) in the slice (no zeros). |
| E2 = \(\operatorname{expdim}_B\) | \(\max(k-2,0)+\sum_{j=2}^s\max(Q_j-3,0)\) | Reading B, no ODE. Always \(\gg 0\) on charged sets. |
| E3 | \(k-(n-m)\) | Opus Card 3. **Not** a special case of E0. Fails HARD gate and both controls. |
| E4 | \(\max(k-2,0)-(n-m)\) | E0 minus polynomiality. Same failure. |
| E5 | \(\gamma-3\) | Treats the passport integer as \(r-3\). Not licensed. Negative on \((2,3,V_2=1)\). |

---

## 5. Controls

**Automorphism \((y,\,x+y^\ell)\), \(\ell=5,7,8\).** Outside the
(1)–(13) search (\(d=1\)). One bottom disc, \(k=1\), a cyclic (2-point)
cover of the unique component. \(\operatorname{expdim}_A=0\ge 0\),
matching a rigid map after affine normalisation. E3 \(=1-(\ell-1)=2-\ell<0\):
the Opus count kills a genuine automorphism, so it is wrong.

**Composition \((x+y^5,\,y+(x+y^5)^3)\).** Five bottom discs, \(\nu=1\),
outside NU-TWO. \(n=15\), \(m=5\), \(k=5\).
\(\operatorname{expdim}_A=\max(5-2,0)=3\ge 0\). The elementary
composition \((x+p(y),\,y+q(x+p(y)))\) with \(\deg p=5\), \(\deg q=3\),
after monic+Tschirnhausen, has a handful of lower-term parameters (order
4+2); expected dimension 3 is the right order. E3 \(=5-10=-5<0\) again
kills a genuine automorphism.

Both controls pass E0 and fail E3/E4. That is the HARD-gate analogue on
maps that exist.

---

## 6. Evaluation

Enumerator: `box/moh_skeleton_full.py`, hash matching the frozen copy.
Moh's own space at \(n\le 100\) uses \(K_{\min}=2\); the D-slice uses
\(K_{\min}=16\) as in integration #17. UNI packets as in `uni_hits`
(\(N=k V_2 q\in\mathbb{Z}\), \(k V_2\le u\)). Wall-clock 2.9 s one core,
stdlib plus the enumerator; peak memory python. No AWS. No ledger write.

### 6.1 Moh's six (p.202) — HARD gate

All six have \(s=3\), filling number 1, Reading A tree = 1 core + \(k\)
bottoms.

| row | \((d,e)\) | \(V_2\) | \(u\) | \(q\) | \(\gamma\) | UNI \((k,N)\) | E0 | E3 |
|---|---|---|---|---|---|---|---|---|
| (64,48) | (3,4) | 3 | 12 | 3/4 | 16 | (4, 9) | **2** | −12 |
| (84,56) \(M_2=64\) | (2,3) | 2 | 21 | 2/7 | 3 | (7, 4) | **5** | −21 |
| (84,56) \(M_2=72\) | (2,3) | 5 | 21 | 1/2 | 6 | (2, 5), (4, 10) | **0**, **2** | −26, −24 |
| (75,50) \(V_2=3\) | (2,3) | 3 | 20 | 3/5 | 4 | (5, 9) | **3** | −20 |
| (75,50) \(V_2=2\) | (2,3) | 2 | 20 | 2/5 | 3 | (5, 4), (10, 8) | **3**, **8** | −20, −15 |
| (99,66) | (2,3) | 8 | 24 | 2/3 | 9 | (3, 16) | **1** | −30 |

E0 \(\ge 0\) at every UNI integer-\(N\) packet, including the \(N=4\)
row that integration #17 kills by the frontier \(N\ge 6\) and Appendix II
kills by computation. HARD gate **passed**. E2 is 23–51 (Reading B,
overcount). E3 is negative on all six: if that were \(\operatorname{expdim}\),
the formula would be wrong (Appendix II is a computation on 7–17
variables after Prop 6.3, not a dimension obstruction).

### 6.2 The 652 excess (1)–(13) rows at \(n\le 100\)

CONTROL 4 reproduced: 658 rows, 6 printed, 652 excess. Among the 652:

- 297 have **no** UNI integer \(N\ge 1\) (no packet; \(\operatorname{expdim}(S,k)\)
  is not evaluated).
- 355 have at least one UNI integer \(N\ge 1\): E0 min-over-\(k\) is
  **0 on 59, positive on 296, never negative**.
- Restricting to \(N\ge 6\): 321 excess packets; E0 at saturating \(k\)
  is 0 on 8, positive on 313.

E3 is negative on all 355 (and on all six). **E0 \(<0\) does not
separate 652 from 6.** PROGRAM is not this combinatorics. (297
integrality failures are the D1-PIN filter, already measured, not a
Hurwitz dimension.)

### 6.3 D = 105 trio, charged \(k\)-windows

(1)–(13) at \(D=105\), \(K_{\min}=16\): 15 V-assignments, 7 with UNI
\(N\ge 6\). The Opus trio (all \(V_2=1\), \((d,e)=(2,3)\)):

| \(M_2\) | \(V_3\) | \(A_1\) | \(q\) | \(u\) | charged \(k\) | E0 at those \(k\) | E3 |
|---|---|---|---|---|---|---|---|
| 28 | 5 | 2 | 1/2 | 25 | \(\{12,14,\dots,24\}\) | 10, 12, …, 22 | −23 … −11 |
| 28 | 6 | 2 | 9/13 | 30 | 13 (and 26) | 11 (and 24) | −22 (−9) |
| 40 | 4 | 2 | 9/17 | 28 | 17 | 15 | −18 |

All **positive** under E0, all **negative** under E3. The two extra
(2,3,\(V_2=1\)) UNI \(N\ge 6\) rows at this degree have \(A_1=1\) and
\(k=25\), E0 = 23. A seventh UNI \(N\ge 6\) row is \((d,e)=(4,5)\),
\(k=13\), E0 = 11; one more is \(V_2=4\), \(k=7\), E0 = 5. Nothing in
the D = 105 UNI window is Hurwitz-rigid.

### 6.4 Slice \(48\le D\le 120\), UNI \(N\ge 6\), \(K_{\min}=16\)

Measured: 1692 V-assignments, 1189 groups (matches census-rebase);
**840 V-assignments / 670 groups** alive at UNI \(N\ge 6\) (matches the
charged Grok count). Filling number \(d_s/V_s=1\) on all 840. Signs at
saturating \(k\):

| formula | neg | zero | pos |
|---|---|---|---|
| E0 primary | **0** | **19** | **821** |
| E1 (O2) | 0 | 0 | 840 |
| E2 (Reading B) | 0 | 0 | 840 |
| E3 Opus | 840 | 0 | 0 |
| E5 \(\gamma-3\) | 240 | 177 | 423 |

E0 value distribution (saturating \(k\)): \(0^{19},1^{16},2^{21},\dots\),
max 33. Saturating \(k\) ranges from 1 to 35; the mode is \(k=13\)
(121 assignments). \(V_2=1\) occupies 485 of 840 and has
\(k_{\mathrm{sat}}\in[7,35]\), hence E0 \(\in[5,33]\) — the *large*
end, not the rigid end.

**Growth with \(D\):** mean E0 at saturating \(k\) is 8.39 on [48,80]
(\(n=85\)), 11.21 on [81,100] (\(n=224\)), 13.62 on [101,120]
(\(n=531\)). Max E0 is 19, 26, 33 on those bands. No degree empties.
The quantity is unbounded as a function of \(D\) on this window
(bounded for each fixed \(D\) by \(\lfloor u/V_2\rfloor-2\le K-2\le n/3-2\)).

**Rigid isolated CE candidates** (\(\operatorname{expdim}_A=0\) at
saturating \(N\ge 6\) \(k\), i.e. \(k_{\mathrm{sat}}\in\{1,2\}\)): 19
V-assignments, none of them \(V_2=1\). They are large-\(V_2\) packets
with \(q\) close to 1, so a single disc already makes \(N\ge 6\).

```text
D=60  m=40  M=(-10,45,58)     V2=11 (2,3) s=4  k=1  N=10
D=80  m=60  M=(68,78)         V2=7  (3,4) s=3  k=1,2  N=7,14
D=84  m=63  M=(49,82)         V2=7  (3,4) s=3  k=1,2  N=7,14
D=96  m=72  M=(-8,20,94)      V2=7  (3,4) s=4  k=1,2  N=8,16
D=96  m=72  M=(-8,76,94)      V2=7  (3,4) s=4  k=1,2  N=8,16
D=96  m=72  M=(56,92,94)      V2=7  (3,4) s=4  k=1,2  N=7,14
D=96  m=72  M=(80,84,94)      V2=7  (3,4) s=4  k=1,2  N=7,14
D=100 m=75  M=(85,98)         V2=7  (3,4) s=3  k=2    N=7
D=108 m=72  M=(60,80,106)     V2=20 (2,3) s=4  k=1    N=16
D=108 m=72  M=(60,100,106)    V2=20 (2,3) s=4  k=1    N=16
D=108 m=72  M=(90,106)        V2=17 (2,3) s=3  k=1    N=17
D=108 m=72  M=(90,99,106)     V2=17 (2,3) s=4  k=1    N=17
D=120 m=72  M=(12,44,118)     V2=8  (3,5) s=4  k=1,2  N=10,20
D=120 m=72  M=(12,76,118)     V2=8  (3,5) s=4  k=1,2  N=10,20
D=120 m=90  M=(-10,25,118)    V2=7  (3,4) s=4  k=2    N=8
D=120 m=90  M=(-10,95,118)    V2=7  (3,4) s=4  k=2    N=8
D=120 m=90  M=(100,105,118)   V2=7  (3,4) s=4  k=2    N=7
D=120 m=80  M=(88,118)        V2=17 (2,3) s=3  k=1,2  N=17,34
D=120 m=80  M=(100,110,118)   V2=17 (2,3) s=4  k=1,2  N=17,34
```

These 19 are the only rigid isolated CE candidates the Hurwitz count
produces in the slice. They remain subject to Appendix II-style
polynomial algebra (Card III) and to Q3(a). They are not a proof.

---

## 7. Comparison

### 7.1 (2,3,\(V_2=1\)) rigidity and Opus Card 3

The DS pair of type \((2,3,1)\) is unique up to normalisation, field of
moduli \(\mathbb{Q}\). A UNI realisation is therefore \(k\) identical
stars, glued by \(k\) centres. That is exactly Step 1 plus the
\(a_O\)-count of Step 3: \(\operatorname{expdim}_A=\max(k-2,0)\). The
Opus count “\(k\) gluing constants against \(n-m\) polynomiality
relations” **adds** the interpolant-degree-killing block of Card III,
which is not a Hurwitz datum.

Is \(k<n-m\) for every \(V_2=1\) group? On the D = 105 trio, yes
(\(k\le 26\), \(n-m=35\)). On the slice, E3 is negative on all 840 UNI
\(N\ge 6\) assignments, \(V_2=1\) included. **That does not kill
\(V_2=1\) skeletons.** Reasons, typed:

1. The composition control has \(k=5<n-m=10\) and **exists**. The
   relations are not independent of the automorphism group, and outer
   coefficients supply unknowns (Opus Card 3, outcome (iii), stop
   condition: do not guess the outer count). Subtracting \(n-m\) fails
   both charged controls and the six.
2. Under the Hurwitz count the same \(V_2=1\) rows have *large* \(k\)
   (the UNI window \(N=k q\ge 6\) with \(q<1\) forces \(k\ge 7\)), hence
   \(\operatorname{expdim}_A\ge 5\). They are moduli, not rigid.
3. HARD gate: E3 \(<0\) on all six, but Appendix II is a further
   computation, not a dimension obstruction.

So \(k-(n-m)\) is not a special case of \(\operatorname{expdim}_A\).
MAJOR-MULT is not proved by this counting. `OPEN[MAJOR-MULT]` is
untouched (the page-179 question whether a major disc may have \(V=1\)
is not a dimension question).

### 7.2 ORTHO-DEFECT as infinitesimal shadow

ORTHO-DEFECT (promoted, integration #17 context): \(2de N=\sum_\nu(e m_\nu-d m'_\nu)^2\),
with \(N=O(1)\). This is a quadratic form on the deviation of infinitely-near
multiplicities from the ray \((m_\nu:m'_\nu)=(d:e)\). Exact proportionality
is Moh A.1 (\(D=0\), \(p\) and \(q\) powers of a common linear factor),
which Prop 4.6(5) and STAR-ABC both forbid. The defect \(N=O(1)\) says
the tower is an *infinitesimal* Davenport–Stothers configuration: Galois
conjugates of almost-proportional Belyi maps, glued through the Puiseux
tree. That is the tangent-space form of the same object whose global
form is the dessin tower.

It is **not** equal to \(\operatorname{expdim}_A\). The identity prices
\(N\), a polar mass already pinned; \(\operatorname{expdim}_A\) prices
the Hurwitz moduli of the covers. A positive-dimensional Hurwitz space
is compatible with a bounded defect (the defect is constant on a
component, or jumps at resonances). Negative Hurwitz dimension would
have been the global emptiness statement; it does not occur. No
promotion of “ORTHO-DEFECT \(\Rightarrow\) \(\operatorname{expdim}<0\)”
is claimed. SOURCE of the identity: the charged Grok §8 cross-connection,
not re-derived here.

---

## 8. Trichotomy, the theorem needed, bounded quantity

Card II outcomes, applied:

1. **Wrong on the six.** No. E0 \(\ge 0\). Formula retained.
2. **Separates 658 \(\to\) 6.** No. E0 is nonnegative on both printed
   and excess (when a UNI packet exists). PROGRAM is not this
   combinatorics. Stop hunting PROGRAM as a Hurwitz-dimension predicate.
3. **Uniformly negative at \(N\ge 6\).** No. 0 of 840.
4. **Nonnegative infinitely often, growing in \(D\).** Yes. Proof of JC2
   cannot be this count. The all-degree route is Q3(a) (Picard–Fuchs
   irregularity of \(dx/g_y\) on \(g=c_2\)), as the Grok ideation
   already named when combinatorics fails.

**Theorem that would have been a proof candidate, stated to record the
gap:**

> **(not claimed).** For every (1)–(13)-admissible skeleton \(S\) and
> every UNI packet \(k\) with \(N=k V_2 q\in\mathbb{Z}\), \(N\ge 6\),
> one has \(\operatorname{expdim}(S,k)<0\).

The primary formula refutes this as stated. A variant that subtracts
\(n-m\) independent interpolant relations would make it true on the
slice, and is false on the six and on both controls. There is no safe
replacement that both passes the HARD gate and is negative at \(N\ge 6\).
Typed OPEN, not filled by cap.

**Rigid isolated CE candidates:** the 19 rows of §6.4, plus, at \(n\le 100\)
without the \(N\ge 6\) floor, the additional excess zeros of §6.2 (59
min-over-\(k\), 8 of them still zero at \(N\ge 6\)). Moh's six are **not**
in this list at \(N\ge 6\) (their E0 is 1 through 8). Appendix II kills
the six by polynomial algebra after Prop 6.3, which is the correct
operation on a nonnegative Hurwitz space.

**Positive, growing with \(D\):** the 821 assignments of §6.4, including
the entire \(V_2=1\) block (485) and the D = 105 trio. This is the CE
list the Hurwitz count produces. A Newton lift on one of these, after
PROGRAM (which this count does not supply), is the CE-side attack
(Q3(e)); a germ is `REPRESENTATIVE`, not a map.

**Bounded quantity of `OPEN[DT-DIM]`.** The integer
\(\operatorname{expdim}_A(S,k)=\max(k-2,0)\) at every (1)–(13)+UNI
\(N\ge 6\) skeleton, together with the sign distribution
(0 / 19 / 821) on \(48\le D\le 120\) and the growth of the mean with
\(D\). The OPEN is **answered as a formula and a table**, not closed as
a proof of JC2. Residual GAPs that this lane does not fill:
`OPEN[STAR-ALLV]` (existence of the bottom dessin for all \((d,e,V)\));
the unique internal multiplicity partition (Card I);
`OPEN[MOH-PROGRAM]` (658 \(\to\) 6 is not this count);
`OPEN[PF-IRREG]` (the Q3(a) quantity).

Reading B does not change the trichotomy: \(\operatorname{expdim}_B>0\)
everywhere on the charged sets, still growing in \(D\), still not a proof.

---

## 9. Desk CAS and pages

Python 3 stdlib on `box/moh_skeleton_full.py` (hash equal to the frozen
copy). One core, 2.9 s wall-clock for the full evaluation (n \(\le\) 100
excess 0.56 s; slice 2.2 s). Peak memory: python process, \(\ll\) 4 GB.
Moh PDF pages 170–171, 179, 182, 205, 207 read as images via the
existing 180 dpi renders and `pdftoppm`. No `jc2-lean`. No other
20260903T1015Z ideation. No running-lane report. No canonical ledger
edit. No `charge_basis`.

Controls: E0 = 0 on \((y,x+y^\ell)\) and E0 = 3 on the five-disc
composition, both \(\ge 0\) with the expected free parameters. E3/E4
fail those controls and the six; they are recorded only as a comparison.

---

## Disposition

| item | status |
|---|---|
| \(\operatorname{expdim}_A(S,k)=\max(k-2,0)\) | PROVED-HERE as the Hurwitz count of Reading A, with the internal 3-point step PROVED-HERE from A.3 |
| Internal Prop 4.6 numerical passport | SOURCE-UNVERIFIED (partition); two readings A/B, dimension uses only \(r=3\) vs \(r=Q\) |
| HARD gate on the six | PASS for E0; FAIL for E3/E4 |
| 652-separation | NO |
| D = 105 trio | E0 \(\in\{10,\ldots,22\}\), not a kill |
| Slice 48–120 UNI \(N\ge 6\) | 0 neg / 19 zero / 821 pos, mean growing in \(D\) |
| Opus \(k<n-m\) as a special case | NO; wrongly kills automorphisms and the six |
| ORTHO-DEFECT = infinitesimal shadow | interface, not an identity with \(\operatorname{expdim}\) |
| Proof of JC2 by \(\operatorname{expdim}<0\) | refuted for this formula; theorem needed is stated and fails; Q3(a) remains |
| `OPEN[DT-DIM]` | answered as a bounded integer-valued function plus tables; not a JC2 proof |

<!-- BODY-END -->
