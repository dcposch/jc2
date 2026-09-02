# STAR-REALISABILITY — the bottom operator forces the simple partition

Lane: `STAR-REALISABILITY`  
Date: 2026-09-02  
Scope: degree-minimal, noninvertible Keller candidates in Moh's gauge; exact
arithmetic; `(UNI)` only where explicitly stated.  
Result: `OPEN[STAR-REALISABILITY/FORCED-REPEAT]` is closed with **zero kills**.

## 0. Headline

**[PROVED-HERE/UNREVIEWED]** The premise inherited from integration #17 needs a
source-level correction. Moh's Proposition 4.6 does not *print* the words “simple
roots” in its `r=1` clause, but its printed equation

\[
 D\!\left(n,-M_1,g_{\sigma_1}(\pi),T^\psi_{1,\sigma_1}(\pi)\right)=c,
 \qquad c\in k^*,
\]

already forces the product of the two displayed polynomials to be squarefree.
Moh explicitly draws that conclusion in the all-roots subcase on p.184 by
invoking Proposition A.5 on p.207. Consequently, if the campaign shorthand is
\(p_1(\pi):=g_{\sigma_1}(\pi)\), then every Keller realization of every numerical
skeleton has

\[
 \operatorname{part}(p_1)=(1^{eV_2}).
\]

No choice of \((M_2,\ldots,M_s,V_2,\ldots,V_s,u,v,d_j,\delta_j)\) forces a
repeated bottom root. The operator forces the opposite. This closes the bounded
partition question; no extra datum is needed to determine the bottom
multiplicity partition.

**[MEASURED]** After the current `(UNI)` filter—some integral
\(N=kV_2q\ge6\), \(kV_2\le u\)—9,553 of the 902,893 enumerated assignments at
\(D\le120\) reach the STAR test. All 9,553 pass and none is killed. At the five
MOH-SHARP-2 degrees, 6,328 assignments reach the test and all pass. No supported
degree is emptied.

**[PROVED-HERE/UNREVIEWED]** “Pass” here has deliberately narrow meaning:
*not killed by a forced repeated bottom root*. It does not exhibit a global
Keller pair and does not certify full coefficient-level realizability of a Moh
skeleton.

## 1. Custody, source, and computation envelope

**[MEASURED]** Before reading any charged input, all seven frozen SHA-256 values
matched the charge:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  d1-subtree-review-grok46-20260902.md
ad1bf4467319f98a29e50de16915ced5f5c4177f7ffe28657332aba00ad18245  ideation-20260902T1608Z-synthesis.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  moh_skeleton_N.py
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
e2b4d616a6ccbd771f1eb8c1b9e37ffaf50a46e278a529c1e05c5de948fda313  runall.py
```

**[MEASURED]** The source is
[Moh 1983](/Users/dc/code/math/jc2/refs/moh1983_jram340_configurations_of_roots.pdf),
SHA-256
`6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51`.
I used OCR only to locate material and read the page images for journal pp.150–151,
164–165, 167–171, 173–176, 179–184, 190–194, and 207. Journal page \(P\) is
PDF page \(P-139\).

**[MEASURED]** The final driver run was sequential: 28.98 s real, 27.86 s user,
0.23 s system, maximum RSS 77,725,696 bytes (about 74.1 MiB). There was no
multiprocessing, no network work, no saturation or Gröbner calculation, no
canonical-ledger edit, and no inspection of `jc2-lean`.

## 2. What Moh's data determine

### 2.1 The eta expansion does not supply a free bottom partition

**[PROVED-HERE/UNREVIEWED]** Moh p.150 works over \(k[x]((\eta))\) with

\[
 g(x,y)=\eta^{-n},\qquad
 f(x,y)=\eta^{-m}+\sum_{j>-m} f_j(x)\eta^j,
\]

and defines

\[
 d_1=n,\qquad d_{j+1}=\gcd(n,M_1,\ldots,M_j),\qquad
 M_j=\min\{i:f_i(x)\ne0,\ d_j\nmid i\}.
\]

The leading term gives \(M_1=\mu_1=-m\); Moh states this explicitly on p.184.
Lemma 2.1 on p.151 says the Keller condition is equivalent to

\[
 \operatorname{ord}_\eta\!\left(
   \sum f_i(x)\eta^i-\sum f_i(0)\eta^i
 \right)=n-1,
 \qquad \deg_x f_{n-1}(x)=1.
\]

Its proof rewrites this as \(f_i'(x)=0\) for \(i<n-1\) and
\(f'_{n-1}(x)\in k^*\). Its stated tree consequence is \(M_i\le n-1\).
This is the \(\eta=g^{-1/n}\)-adic characteristic expansion, not a list of
\(t=x^{-1}\)-adic residue roots inside \(D_1\). It neither chooses a bottom
partition nor forces a repeat. The bottom partition is instead decided by the
`r=1` operator below.

### 2.2 Definition 4.1 and Propositions 4.1, 4.2, and 4.4

**[PROVED-HERE/UNREVIEWED]** For a \(\pi\)-root
\(\sigma=\sum a_jt^j+\pi t^\delta\), Proposition 4.1 on p.164 takes the leading
coefficients \(h_\sigma(\pi)\), \(g_\sigma(\pi)\) and extracts from the Jacobian
identity the coefficient

\[
 \lambda_hh_\sigma g_\sigma'-\lambda_gg_\sigma h_\sigma'.
\]

Definition 4.1 names the corresponding operator

\[
 D(a,b,P,Q):=aP(\pi)Q'(\pi)-bQ(\pi)P'(\pi).
\]

The introductory paragraph on p.164 also fixes the tree interpretation: if a
leading polynomial has distinct residue roots with multiplicities
\(\ell_1,\ldots,\ell_t\), then the current disc splits into proper subdiscs
containing exactly those numbers of roots. Thus the root-multiplicity partition
of \(g_{\sigma_1}\) is exactly the branching partition of the `g`-roots below
\(D_1\).

**[PROVED-HERE/UNREVIEWED]** Proposition 4.2 on p.165 propagates a distribution
detector when the order inequality is strict. Its conclusion is a common-power
relation among leading coefficients; it does not assign a new bottom residue
partition. Proposition 4.4 on pp.168–169 is the nonsplitting alternative: under
its seven hypotheses the relevant leading coefficients are powers of one common
linear polynomial. These are higher-level detector/nonsplitting statements. They
do not override the nonzero constant in the terminal `r=1` equation.

### 2.3 Proposition 4.6 has two different outputs

**[PROVED-HERE/UNREVIEWED]** Proposition 4.6 on pp.170–171 must be split by
`r`.

For \(r\ge2\), it produces Moh's literal common polynomial \(p_r(\pi)\) of
degree \(\nu\). In the notation of the proposition,

\[
 g_\sigma=C_0p_r^{n/d_r},\qquad
 T^\psi_{r,\sigma}
   =p_r^{(-\mu_r+M_r-n)/d_r}q_r,
\]

where

\[
 \deg q_r=\nu\frac{n-M_r}{d_r},
\]

\(q_r\) has distinct roots, every root of \(p_r\) is a root of \(q_r\), and
\(p_r\) is not a power of \(q_r\). The major recursion chooses a factor
\(\pi-C_r\) of \(p_r\) with multiplicity \(V_r\).

For \(r=1\), Proposition 4.6 does **not** introduce that common \(p_r\).
Instead it concludes

\[
 D\!\left(n,-M_1,g_\sigma,T^\psi_{1,\sigma}\right)=c\in k^*.
\]

The proof on p.171 records
\(T_1^\psi=f+\text{a polynomial in }g\), hence
\((T_1^\psi)_f=1\); this is the source of the nonzero right-hand side.

**[PROVED-HERE/UNREVIEWED]** Therefore “Moh's \(p(\pi)\) at
\(\sigma_1\)” is campaign shorthand and is potentially misleading. In the rest
of this report

\[
 P_1:=p_1:=g_{\sigma_1},\qquad Q_1:=T^\psi_{1,\sigma_1}.
\]

The literal common \(p_r\) should be reserved for \(r\ge2\).

### 2.4 Definition 5.1 brings the numerical skeleton to D1

**[PROVED-HERE/UNREVIEWED]** Definition 5.1 on p.179 gives, in \(D_i\),

\[
 \#\{g\text{-roots}\}=\frac{n}{d_{i+1}}V_{i+1},\qquad
 \#\{T_j^\psi\text{-roots}\}=\frac{-\mu_j}{d_{i+1}}V_{i+1},
\]

the windows

\[
 \frac{d_i}{n-M_i}<V_i\le
 V_{i+1}\frac{d_i}{d_{i+1}},
\]

the product formula for \(\delta_i\), and the instruction that the hypotheses of
Proposition 4.6 hold at the general point \(\sigma_i\) with
\(\nu=V_{i+1}d_i/d_{i+1}\). Proposition 5.3, applied with \(r=2\), extends the
tower to \(D_1\); the last sentence of its proof on p.183 says criteria (1), (3),
and (4) hold for the extended tower.

Put

\[
 K=d_2=\gcd(n,m),\qquad n=Ke,qquad m=Kd.
\]

At \(i=1\), \(d_1=n\), \(M_1=\mu_1=-m\), and
\(\nu_1=V_2d_1/d_2=eV_2\). Proposition 4.6(4),(5), equivalently Definition
5.1(1), now gives exact local degrees

\[
 A:=\deg P_1=a_1=eV_2,
 \qquad
 B:=\deg Q_1=b_1=dV_2.
\]

This also isolates a common confusion: \(V_2\) is the marked multiplicity of the
chosen root of the **level-2** common polynomial \(p_2\). It selects \(D_1\),
which contains \(eV_2\) roots of \(g\). It is not the multiplicity of any root of
the new bottom polynomial \(P_1\).

### 2.5 The bottom partition theorem

**[PROVED-HERE/UNREVIEWED]** Substitute \(M_1=-m\) in the terminal equation:

\[
 nP_1Q_1'-mQ_1P_1'=c,\qquad c\ne0. \tag{BOT}
\]

If \(\alpha\) were a repeated root of \(P_1\), then
\(P_1(\alpha)=P_1'(\alpha)=0\), so the left side of `(BOT)` would vanish at
\(\alpha\), contradicting \(c\ne0\). The identical argument applies to a
repeated root of \(Q_1\). A common root of \(P_1,Q_1\) also makes the left side
zero. Hence \(P_1Q_1\) is squarefree.

The degree rescaling makes Moh's Appendix-I statement apply verbatim:

\[
 (n,m)=\frac{K}{V_2}(A,B),\qquad
 D(A,B,P_1,Q_1)=\frac{V_2}{K}D(n,m,P_1,Q_1)\in k^*.
\]

Proposition A.5 on p.207 says exactly that if the weights equal the two
polynomial degrees and the `D`-value is a nonzero constant, then the product has
only simple roots. In the all-roots subcase treated there (where \(V_2=K\)), Moh
p.184 applies A.5 to this `r=1` equation and explicitly concludes that
\(g_\sigma(\pi)\) has all distinct roots. The displayed rescaling supplies the
same A.5 hypotheses for general \(V_2\le K\).

Therefore, over Moh's algebraically closed characteristic-zero field,

\[
 \boxed{\operatorname{part}(P_1)=(1,\ldots,1)=(1^{eV_2}).}
\]

Only \(e=n/K\) and \(V_2\) determine the length. The remaining skeleton data
determine admissibility, disc radii, higher-level branching, and packet capacity,
but cannot change a bottom part from 1 to a larger integer. There is no
bottom-partition datum left to enumerate.

**[PROVED-HERE/UNREVIEWED]** This corrects, rather than contradicts, D1-STAR:
D1-STAR's simple bottom star agrees with Moh's operator. The reviewed claim
“Prop. 4.6 at `r=1` does not already force simple roots” is tenable only in the
narrow bibliographic sense that the proposition does not spell out the elementary
consequence in its conclusion list. As a mathematical implication it is false,
and Moh's own p.184 removes the ambiguity.

### 2.6 What remains free at r >= 2, and why it is not bottom data

**[PROVED-HERE/UNREVIEWED]** For contrast, at a genuine \(r\ge2\) common
polynomial set

\[
 A_r=\nu_r=V_{r+1}\frac{d_r}{d_{r+1}},\qquad
 B_r=\deg q_r=A_r\frac{n-M_r}{d_r}.
\]

Writing the distinct roots of \(q_r\) as \(\beta_1,\ldots,\beta_{B_r}\), the
unrecorded discrete datum is the weak multiplicity vector

\[
 w_j=\operatorname{ord}_{\beta_j}p_r\ge0,qquad
 \sum_{j=1}^{B_r}w_j=A_r.
\]

The skeleton marks one coordinate \(w_j=V_r\), with
\(V_r>d_r/(n-M_r)=A_r/B_r\), but does not store all other coordinates or the
root positions. Its positive coordinates form a partition of \(A_r\), with at
most \(\min(A_r,B_r)\) parts. Once the marked coordinate is fixed, the number of
labeled weak vectors is bounded by
\(\binom{A_r-V_r+B_r-2}{B_r-2}\) for \(B_r\ge2\) (and by 1 in the one-coordinate
case); the printed conditions “support inside \(q_r\)” and “not a power of
\(q_r\)” reduce this finite set further. This is the extra datum relevant to
levels \(r\ge2\). Transporting it to \(r=1\) is the category error that created
the apparent STAR open.

**[PROVED-HERE/UNREVIEWED]** Proposition 6.1 on pp.190–193 is expressly an
\(r\ge2\) minor-disc result, with
\(1\le V_r\le d_r/(n-M_r)\). Lemma 6.1 on p.194 states only that
\(\delta_{s-1}\ge0\) when \(\delta_s=-1\). Neither supplies or changes a bottom
partition. The coefficient uncertainty discussed on p.194 occurs when
\(\operatorname{ord}g(\sigma)=0\); Proposition 4.6 assumes
\(\operatorname{ord}g(\sigma)=n\lambda<0\). It is not an exception to `(BOT)`.

## 3. Implementation

**[PROVED-HERE/UNREVIEWED]** The bounded standalone driver is
[star_realisability.py](/Users/dc/code/math/jc2/box/star-realisability-drivers-20260902/star_realisability.py),
SHA-256
`8e20c580e1f77a852b9e3119ac39af2ac0ae55eb65086469740044a0ac757811`.
It imports the unchanged `Skel` and `census` framework from
[moh_skeleton_N.py](/Users/dc/code/math/jc2/box/moh_skeleton_N.py). No canonical
file was changed.

The driver does the following, in order:

1. **[PROVED-HERE/UNREVIEWED]** Lines 44–92 verify all seven frozen hashes and
   the unchanged workspace core before importing or enumerating. A simulated bad
   expected hash stopped before the census.
2. **[PROVED-HERE/UNREVIEWED]** Lines 112–154 compute
   \(q=(1-\delta_1)de/(d+e)\) with `Fraction` and implement the current `(UNI)`
   filter. If \(q=p/r\) is reduced, integrality of \(kV_2q\) is equivalent to
   \(r/\gcd(r,V_2)\mid k\), with \(1\le k\le\lfloor u/V_2\rfloor\). There is no
   obsolete \(N\le16\) cap: the charged frontier here is \(N\ge6\).
3. **[PROVED-HERE/UNREVIEWED]** Lines 157–182 check
   \((A,B)=(eV_2,dV_2)=(a_1,b_1)\) and the exact operator scale
   \((n,m)=(K/V_2)(A,B)\).
4. **[PROVED-HERE/UNREVIEWED]** Lines 193–209 implement the forced partition
   \((1^A)\). It returns `PASS` for the repeated-root obstruction; it does not
   assert coefficient-level realization.
5. **[PROVED-HERE/UNREVIEWED]** Lines 239–266 count every complete V-assignment
   emitted by `census(D, with_V=True)` that has at least one `(UNI)` witness with
   integral \(N\ge6\). Lines 330–389 print the two requested tables and the full
   selected \(D=105\) row.

**[MEASURED]** An independent exhaustive comparison of the optimized `(UNI)`
period calculation against the frozen `d1floor.achievable(S, Nlo=6)` loop covered
all 902,893 assignments at \(D\le120\): zero mismatches and 9,553 assignments
reached the STAR test.

## 4. Controls

**[PROVED-HERE/UNREVIEWED]** The required positive control passes. For
\((f,g)=(y,x+y^k)\), take at the bottom

\[
 P_1(\pi)=1+\pi^k,qquad Q_1(\pi)=\pi.
\]

Then

\[
 D(k,1,P_1,Q_1)=k,
\]

and \(P_1\) has \(k\) distinct roots. The driver checks this exactly for
\(2\le k\le12\). These automorphisms have \(s=1\), so they are a direct operator
control rather than members of the \(s\ge3\), \(K\ge16\) counterexample census.

**[PROVED-HERE/UNREVIEWED]** The negative lemma control constructs polynomials
with a repeated root at \(\pi=0\) and verifies that the `D`-operator also vanishes
there, for 35 degree pairs. It then checks the bottom-degree/operator scaling on
a census row. This tests the failure mode in the direction actually used by the
proof.

**[MEASURED]** The non-Keller two-tower rows were not made acceptance controls.
They need not satisfy a Keller-only nonzero-constant operator identity, exactly as
the charge permits.

## 5. Census results

### 5.1 MOH-SHARP-2 degrees

**[MEASURED]** “Enumerated” is the complete V-assignment population before the
current integrality frontier. “Tested” means it has at least one `(UNI)` packet
with integral \(N\ge6\). The STAR kill is then applied to every tested assignment.

| D | enumerated V-assignments | tested | forced-repeat killed | surviving | STAR emptied? |
|---:|---:|---:|---:|---:|:---:|
| 105 | 5,037 | 63 | 0 | 63 | no |
| 108 | 85,205 | 1,184 | 0 | 1,184 | no |
| 112 | 47,655 | 593 | 0 | 593 | no |
| 117 | 1,686 | 22 | 0 | 22 | no |
| 120 | 516,309 | 4,466 | 0 | 4,466 | no |
| **total** | **655,892** | **6,328** | **0** | **6,328** | **none** |

### 5.2 Complete D <= 120 census

**[MEASURED]** The table lists every degree at most 120 for which `census`
emits at least one numerical skeleton. Degrees omitted from the table have an
empty upstream census domain; they are not degrees emptied by STAR.

| D | enumerated | tested (UNI, integral N>=6) | killed | surviving | emptied? |
|---:|---:|---:|---:|---:|:---:|
| 48 | 1,301 | 26 | 0 | 26 | no |
| 54 | 514 | 10 | 0 | 10 | no |
| 60 | 3,623 | 72 | 0 | 72 | no |
| 63 | 438 | 7 | 0 | 7 | no |
| 64 | 2,417 | 57 | 0 | 57 | no |
| 66 | 390 | 3 | 0 | 3 | no |
| 72 | 15,694 | 302 | 0 | 302 | no |
| 75 | 682 | 12 | 0 | 12 | no |
| 78 | 558 | 9 | 0 | 9 | no |
| 80 | 16,074 | 241 | 0 | 241 | no |
| 81 | 764 | 14 | 0 | 14 | no |
| 84 | 10,748 | 152 | 0 | 152 | no |
| 88 | 550 | 9 | 0 | 9 | no |
| 90 | 30,107 | 368 | 0 | 368 | no |
| 96 | 130,186 | 1,610 | 0 | 1,610 | no |
| 99 | 1,180 | 25 | 0 | 25 | no |
| 100 | 26,873 | 247 | 0 | 247 | no |
| 102 | 984 | 14 | 0 | 14 | no |
| 104 | 786 | 15 | 0 | 15 | no |
| 105 | 5,037 | 63 | 0 | 63 | no |
| 108 | 85,205 | 1,184 | 0 | 1,184 | no |
| 110 | 1,890 | 14 | 0 | 14 | no |
| 112 | 47,655 | 593 | 0 | 593 | no |
| 114 | 1,242 | 18 | 0 | 18 | no |
| 117 | 1,686 | 22 | 0 | 22 | no |
| 120 | 516,309 | 4,466 | 0 | 4,466 | no |
| **total** | **902,893** | **9,553** | **0** | **9,553** | **none** |

**[MEASURED]** Every degree supported after `(UNI)` integrality has at least one
STAR survivor. Thus STAR empties no degree, both on the five-degree slice and in
the complete \(D\le120\) run.

## 6. Smallest selected assignment at D = 105

**[MEASURED]** The word “smallest” needs an order. For campaign continuity I use
the executable order already used by `box/tfe-drivers-20260902/pick105.py`,

\[
 (s,N_{\min},e,m,(M_2,\ldots,M_s),(V_2,\ldots,V_s)),
\]

rather than that file's stale prose comment. Other lexicographic orders choose a
different row, so the order is part of this measurement.

The selected assignment is:

```text
n = D = 105,  m = 70,  s = 3
K = gcd(n,m) = 35,  (d,e) = (2,3),  (u,v) = (20,15)
(M_1,M_2,M_3) = (-70,-63,103),  with M_3 = n-2
(d_1,d_2,d_3,d_4) = (105,35,7,1)
(V_2,V_3,V_4) = (1,4,1)          [V_4=d_4]
(delta_1,delta_2,delta_3) = (3/4,71/95,-1)
(a_1,a_2,a_3) = (3,60,105)       [g-root counts]
(b_1,b_2,b_3) = (2,40,70)        [T_1/f-root counts]
lambda_g(delta_i) = (-3/20,-3/19,-105)
lambda_f(delta_i) = (-1/10,-2/19,-70)
```

**[PROVED-HERE/UNREVIEWED]** Its Def.5.1 windows are

\[
 \frac{35}{105-(-63)}=\frac5{24}<V_2=1
 \le V_3\frac{35}{7}=20,
\]

and

\[
 \frac7{105-103}=\frac72<V_3=4
 \le V_4\frac71=7.
\]

**[MEASURED]** Its exact weight is

\[
 q=(1-\delta_1)\frac{de}{d+e}
   =\frac14\frac65=\frac3{10}.
\]

The selected `(UNI)` V-packet consists of \(k=20\) equal bottom discs, each with
\(V_2(B)=1\):

\[
 (V_2(B))_B=(1^{20}),\qquad
 \sum_BV_2(B)=20=u,
\]

and

\[
 N=kV_2q=20\cdot1\cdot\frac3{10}=6.
\]

This is its only `(UNI)` integer at or above the current frontier.

**[PROVED-HERE/UNREVIEWED]** At the bottom,

\[
 (\deg P_1,\deg Q_1)=(eV_2,dV_2)=(3,2),
\]

and

\[
 D(105,70,P_1,Q_1)=35D(3,2,P_1,Q_1)\in k^*.
\]

Hence its requested bottom partition is

\[
 \boxed{(1^3)=(1,1,1).}
\]

## 7. Fallacy-v2 and scope audit

**[PROVED-HERE/UNREVIEWED]** Flag/place/series are not identified. This report
uses only Moh's \(t\)-adic general point \(\sigma_1\), its residue variable
\(\pi\), and the separate \(\eta\)-adic expansion where explicitly named. It
makes no claim about campaign places or cover series.

**[PROVED-HERE/UNREVIEWED]** There is no exit-price assertion, so no
`charge_basis` line is declared. There is no floor/attainment inference in the
STAR proof: `(BOT)` is an exact polynomial identity with nonzero constant right
side. No pole identity, saturation, remainder computation, or variable-name ring
identification is used.

**[PROVED-HERE/UNREVIEWED]** The objects are kept distinct:
\(V_2\) is a marked multiplicity in \(p_2\); \(P_1=g_{\sigma_1}\) is the bottom
leading polynomial; \(P_1'\) is its actual \(\pi\)-derivative. The argument does
not manufacture an \(M_0\) or extend a major tower below level 1.

**[PROVED-HERE/UNREVIEWED]** `(UNI)` remains a global hypothesis about equal
lower-V data across bottom discs. The zero STAR-kill theorem itself is
branch-local and does not use `(UNI)`; `(UNI)` is used only to select the finite
population requested for measurement.

**[PROVED-HERE/UNREVIEWED]** No new `OPEN` is raised. The bounded open named in
the charge—the partition of an integer \(eV_2\)—is answered by the unique
partition \((1^{eV_2})\) compatible with the bottom Keller operator. General
coefficient-level or global Keller realizability is outside this forced-repeat
test and is not claimed.

## 8. Typed verdict

```text
LANE        STAR-REALISABILITY / forced repeated bottom root
SCOPE       Degree-minimal noninvertible Keller candidates in Moh's gauge.
            (UNI) is used only for the requested N-integrality population.

PROVED-HERE/UNREVIEWED
            Moh's literal common p_r(pi) belongs to r>=2.  At r=1 put
            P_1=g_{sigma_1}, Q_1=T^psi_{1,sigma_1}.  Prop 4.6 gives
            D(n,m,P_1,Q_1)=c!=0.  Since deg(P_1,Q_1)=(eV_2,dV_2),
            this rescales to the degree-weighted operator of Prop A.5.
            P_1 Q_1 is squarefree, so part(P_1)=(1^{eV_2}).

CORRECTION  “Prop 4.6 r=1 does not force simple roots” is false as a
            mathematical implication.  Moh p.184 explicitly invokes A.5 and
            says g_sigma has all distinct roots.  It was only true as a remark
            that Prop 4.6 does not print those words in its conclusion list.

MEASURED    MOH-SHARP-2: 655892 enumerated, 6328 tested after (UNI),
            integral N>=6; 0 killed, 6328 surviving; no degree emptied.
            Complete D<=120: 902893 enumerated, 9553 tested; 0 killed,
            9553 surviving; no supported degree emptied.

CONTROL     (y,x+y^k), k=2..12: P_1=1+pi^k, Q_1=pi,
            D(k,1,P_1,Q_1)=k and P_1 has k simple roots: PASS.
            Repeated-root vanishing and exact operator scaling: PASS.

D=105      Campaign-order first row: n=105,m=70,M=(-70,-63,103),
            d_i=(105,35,7,1),V=(1,4,1),(d,e)=(2,3),(u,v)=(20,15),
            q=3/10, packet (V_2(B))=(1^20), N=6,
            bottom partition (1^3).

DECISION    OPEN[STAR-REALISABILITY/FORCED-REPEAT] CLOSED: zero skeletons
            are killed by this obstruction.  PASS does not assert existence
            of a Keller realization.

COMPUTE     Python 3, exact Fraction/Sympy controls, one sequential process;
            28.98 s wall, about 74.1 MiB max RSS.  No canonical-ledger edit;
            jc2-lean not inspected.
```

<!-- BODY-END -->
