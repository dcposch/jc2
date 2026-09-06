# HOSTILE GATE: six shifted child sums after fixed-list closure — Sol 5.6 — 2026-09-06

```text
VERDICT: R025, R026, R027, R028, R057, R058 all SURVIVE.

The proposed R063-template kill does not replay.  The frozen shifted-46 DATA
replay computed each listed fraction by terminating the unselected D'_3 major
packet too early.  Proposition 5.3 instead carries that packet to the prescribed
D'_2.  The complete child partitions include integral sums:

R025 17 (also 22)     R026 17       R027 17 (also 22)
R028 22               R057 18       R058 18.

These values exactly match the exact-contact parent certificates under the
u_s=1 major-orbit map.  The parent certificates remain necessary numerical/face
configurations, not polynomial-pair witnesses, but they are not shown to be
R063-style coarse-lattice artifacts.  The artifact here is the truncated child
sum and the replay's false empty-closure result.
```

No new exit-price assertion is made, so no `charge_basis=` line applies.

## 0. Custody, scope, and the frozen-source conflict

Before mathematical use I paired the numbered
`charged_input_<i>_sha256=`/`_basename=` fields of
`xmodel/six-rows-child-sum-sol56-20260906.run.v2` with `awk`, wrote the resulting
manifest in `/tmp`, and ran `sha256sum -c`. All **10/10** frozen copies in
`/tmp/jc2-lane.EWXUl5/inputs` returned `OK`. The exact-rational driver repeats
the digest check. Mathematical inputs were those frozen copies. No fleet,
ledger edit, `jc2-lean`, or `ideation-*` input was used.

The objects audited here have the roster's semantic type
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`. “SURVIVES” means that an
integral necessary child partition exists; it does not exhibit a Keller pair or
settle global coefficient compatibility.

One charged-input conflict must be explicit. `t3-residue-closure...:101-147`
calls the six source sibling searches dead, whereas the later hostile
exact-contact gate gives fixed-list completions, an explicit R028 counterexample
to the empty search, and local ODE controls (`exact-contact-gate...:245-317`).
The task treats those exact-contact parent completions as the comparison data.
I use the T3 report only for its general current-level lattice statement
`rho_f in (m/d_i)Z` and its `r-1` bound (`t3-residue-closure...:23-34`), after
separating a mandatory fixed-characteristic transition from an optional inserted
split. Reading that bound as freezing the (D'_3) unit through (D'_2) would
contradict printed Proposition 5.3; on that reading the inputs would support only
typed `OPEN`, never the requested kill.

## 1. Declared map and the integer invariant

Use Xu's orientation: the reduced smaller source member is
(P=T_1^\psi(f,g)), of (Y)-degree (m), and the larger member is (Q=g), of
degree (n). If the input pair is not already reduced, the triangular target
change to ((T_1^\psi(f,g),g)) is declared first. It does not identify two
independently enumerated partitions.

For all six rows (u=u_s=1, v=v_s=5), and
(ell=v-u-1=3). With (b\ne0), the ordered source-to-child map is

\[
 \Phi^*:k[x,y]\longrightarrow k[\gamma,\gamma^{-1},\pi],\qquad
 y\longmapsto\gamma^{-1},\qquad
 x\longmapsto {\gamma^{-1}-e-c(\gamma)-\gamma^5\pi\over b}.
\]

Put (X=\gamma, Y=\pi),
(P'=\Phi^*(P)=\bar T_1^\psi(\sigma)), and
(Q'=\Phi^*(Q)=\bar g(\sigma)). A prime is a child-generation label;
(P'_Y,Q'_Y) denote derivatives. Direct differentiation of this declared map,
not a match of variable names, gives (J_{X,Y}(P',Q')=c_0X^3), with
(c_0\in k^*). This is the positive monomial convention justified in
`descent-partition-theorem...:29-60`.

**Prop. 6.3/6.4.** Since (u_s=1), Moh Proposition 6.4 supplies the radius
hypothesis for Proposition 6.3. Thus, under the hypothesis that a parent pair
realizes one of these rows, (P',Q'\in k[X,Y]) are monic in (Y), with

\[
 (n',m')=(30,20)\quad\hbox{on R025--R028},\qquad
 (n',m')=(32,24)\quad\hbox{on R057--R058}.
\]

**Xu Theorem 5.1 shifted by \(\ell\).** Set \(H=1+\ell=4\). Xu Lemma 4.1, applied to
(J=c_0X^\ell), shifts the final-major identity to

\[
 I'_M=I(P'_\xi,Q')={n'\over n'+m'}
 \sum_{\sigma\in\mathcal P'_M}\rho_{P'}(\sigma)(H-\delta_\sigma),
 \qquad P'_\xi=P'-\xi .                                      \tag{1}
\]

Minor roots have (Q')-order zero and contribute nothing to (1). This is the
root-product equality only after the actual final-major partition is complete;
`r063-ell-gate...:231-260` derives the shift from Xu's printed Theorem 5.1.

**Xu §2.** Because the two child members are honest (Y)-monic polynomials and
their generic resultant is nonzero,

\[
 I(P'_\xi,Q')=\deg_X\operatorname{Res}_Y(P'_\xi,Q')
 =-\operatorname{ord}_t\prod_{P'_\xi(\alpha)=0}Q'(\alpha)
 \in\mathbb Z_{\ge0},\qquad X=t^{-1}.                         \tag{2}
\]

There is no cover-degree division in (2); see Xu printed §2, PDF p.1, and
`exact-contact-gate...:35-67`. A fractional *truncated* sum does not contradict
(2).

## 2. `descend_own`: every first-support alternative

The frozen loop `descend_own.py:151-181` has exactly two coefficient cases at
each source level: zero and nonzero first support. Its congruence and orbit-size
tests give the following complete route table. `0?` is
\(P-V_i\equiv0\pmod{\operatorname{den}\delta_i}\); `nz?` is
\(\operatorname{den}(\delta_i)V_i\le P\), with \(\delta_i>0\).

| Rows | source step(s), from top down | exhaustive result | retained child vector |
|---|---|---|---|
| R025, R027 | (i=3:(\delta,P,V)=(1/6,10,1)): `0?` no, `nz?` yes | first nonzero at 3 | R025 ((2,1)); R027 ((3,1)) |
| R026 | (i=3:(1/6,10,4)): zero yes, nonzero no, giving incoming (1); (i=2:(1/5,20,2)): zero no, nonzero yes | first nonzero at 2 | ((2,1)) |
| R028 | same zero step at (i=3); (i=2:(1/5,20,3)): zero no, nonzero yes | first nonzero at 2 | ((3,1)) |
| R057 | (i=3:(1/7,10,1)): zero no, nonzero yes | first nonzero at 3 | ((3,1)) |
| R058 | (i=3:(1/7,10,3)): zero yes, nonzero no, giving incoming (1); (i=2:(1/4,12,3)): zero no, nonzero yes | first nonzero at 2 | ((3,1)) |

For example R026's zero tests are (10-4=6\equiv0\pmod6) and
(20-2=18\not\equiv0\pmod5); its nonzero tests are (24>10) and
(10\le20). R058 analogously uses (10-3=7\equiv0\pmod7), then
(12-3=9\not\equiv0\pmod4). The charged roster records `NONEMPTY` for each
whole-source route and the shifted-46 report records one vector on all 46
licensed rows (`child-xu-shifted-46...:28-47`). Hence none of the six has an
unexhausted set-valued own alternative.

The resulting child data are

| Rows | (M') | (d') | (V') | (delta') | licenses |
|---|---|---|---|---|---|
| R025, R026 | ((-20,22,25)) | ((30,10,2,1)) | ((2,1)) | ((7/3,0,-1)) | `DETERMINED_PROP6.4`, `DETERMINED_COMPLETE_US1` |
| R027, R028 | ((-20,22,25)) | ((30,10,2,1)) | ((3,1)) | ((3/2,0,-1)) | same |
| R057, R058 | ((-24,26,29)) | ((32,8,2,1)) | ((3,1)) | ((9/4,1,-2)) | same |

The local (ell)-condition used by the R063 gate also passes. For R025--R028,
at (D'_3), (-1<-5/8,-1/10), and at (D'_2),
(-1/2<-2/25). For R057/R058 the corresponding comparisons are
(-2<-1,-3/28) and (-1/2<-3/56). These are the shifted condition-(3)
checks needed for the local Proposition 4.4/5.3 argument; no blanket generalized
cover theorem is assumed (`r063-ell-gate...:264-288`).

## 3. Printed factor rules and the forced leaf arithmetic

**Prop. 4.6.** At (D'_i), the common leading polynomial has degree

\[
 P_i=V'_{i+1}{d'_i\over d'_{i+1}},\qquad
 Q_i=V'_{i+1}{n'-M'_i\over d'_{i+1}}.                         \tag{3}
\]

The companion (q_i) is squarefree, contains every distinct root of (p_i),
and the equality multiplicity (P_i/Q_i) is forbidden by the nonzero
differential equation. **Definition 5.1(4)** makes every general point in the
fixed tower satisfy Proposition 4.6. Moh prints these statements on pp.170--171
and p.179; the fixed-list consequence is summarized at
`exact-contact-gate...:163-178`.

For a reduced multiplicity (r) at (D'_i), put

\[
 \rho_P={m'\over d'_i}r,\quad \rho_Q={n'\over d'_i}r,\quad
 a=-{m'(\delta'_i-H)\over n'-M'_i},\quad
 \kappa=\rho_P(H-\delta'_i)-a.                               \tag{4}
\]

If (r(n'-M'_i)>d'_i), the packet is major and its forced direct-final data are

\[
 \delta_f=H-{(n'+m')\kappa\over(n'+m')\rho_P-m'},\qquad
 J_f={n'\rho_P\kappa\over(n'+m')\rho_P-m'}.                  \tag{5}
\]

If the inequality is reversed, it is minor and reaches zero order at
(delta_f=\delta'_i+a/\rho_P>H). Actual centre stabilizers are used. Here
(delta'_3\in\{-1,-2\}) and (delta'_2\in\{0,1\}), so every zero and
nonzero lane has (L'=1) through (D'_2); consequently
(A'=\operatorname{den}(L'\delta_f)=\operatorname{den}\delta_f).

### 3.1 The (30/20) child: R025--R028

At (D'_3), (3) gives ((P_3,Q_3,A_3)=(2,5,1)). Containing
(V'_3=1) forces the unique multiplicity pattern ((1,1)). Each factor carries
((\rho_P,\rho_Q)=(10,15)), so the two factors exhaust ((20,30)). Both are
major because (1>2/5). The top face itself has the exact witness
(p=z^2-1, q=z(z^2-1)(2z^2-3)), with (D(2,5,p,q)=6p).

This is the point missed by the frozen replay: Proposition 5.3 carries **both**
above-average factors to the prescribed (D'_2). The unselected one is not a
final (D'_3) packet. At (D'_2), each 10-root packet has
((P_2,Q_2,A_2)=(5,4,1)) and current unit (m'/d'_2=2), hence reduced total
(r=5). Its at-level parting is within the (r-1=4) bound.

All partitions of 5 into at most four parts are

\[
 (5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1).                 \tag{6}
\]

Equations (4)--(5), the actual (L'=1), and the final residue test give:

| (r) | class | ((\rho_P,\rho_Q)) | (delta_f) | (A'), residues | (J_f) | result |
|---:|---|---|---:|---|---:|---|
| 1 | minor | (2,3) | 5 | (1;(0,0)) | 0 | final; split-depth bound 0 |
| 2 | major | (4,6) | (7/3) | (3;(1,0)) | 4 | final pass |
| 3 | major | (6,9) | (3/2) | (2;(0,1)) | 9 | final pass |
| 4 | major | (8,12) | (21/19) | (19;(8,12)) | (264/19) | fail |
| 5 | major | (10,15) | (7/8) | (8;(2,7)) | (75/4) | fail |

Thus (6) leaves exactly four complete branch types:

| code | reduced pattern | (P')-root packets (major; minor) | (Q')-root packets | subtree (I'_M) | minor-floor increment |
|---|---|---|---|---:|---:|
| A | (3,2) | (6,4; none) | (9,6) | 13 | 0 |
| B | (3,1,1) | (6; 2,2) | (9; 3,3) | 9 | 2 |
| C | (2,2,1) | (4,4; 2) | (6,6; 3) | 8 | 1 |
| D | (2,1,1,1) | (4; 2,2,2) | (6; 3,3,3) | 4 | 3 |

Each row of this table exhausts 10 roots of (P') and 15 of (Q'). The
patterns are genuine Proposition-4.6 faces, not integer partitions alone. For
(D(P,Q,p,q)=Ppq'-Qp'q), exact witnesses include

\[
\begin{array}{c|c|c}
 A&p=z^2(z-1)^3&q=z(z-1)(25z^2-35z+7),\ D=21p;\\
 B&p=z^3(z^2-5z+15)&q=z(z^2-5z+15)(z+1),\ D=-105p;\\
 D&p=z^2(z^3-1)&q=z(z^3-1),\ D=3p.
\end{array}
\]

For C, over (k\supset\mathbb Q(\sqrt5)), take
(a=(1+\sqrt5)/2, c=(5-\sqrt5)/10),
(p=z^2(z-1)^2(z-a)), and (q=z(z-1)(z-a)(z-c)); then
(D(5,4,p,q)=(3\sqrt5/5)p). Every displayed (q) is squarefree and contains
the distinct roots of (p). The driver verifies all four identities exactly.

The selected branch is A, C, or D when (V'_2=2); C has two marked choices of
the multiplicity-2 coefficient, explaining four flat records but only three
unmarked patterns. It is A or B when (V'_2=3). The other (D'_3) branch may
be any of A--D. The complete finite exhaustion is therefore:

| selected branch | sibling A | sibling B | sibling C | sibling D |
|---|---:|---:|---:|---:|
| A | 26 | 22 | 21 | 17 |
| C | 21 | 17 | 16 | 12 |
| D | 17 | 13 | 12 | \(8^*\) |
| B | 22 | 18 | 17 | 13 |

Rows A/C/D apply to R025/R026; rows A/B apply to R027/R028. The C row is
duplicated when the marked selected coefficient is retained. Every displayed
complete sum is integral. The sole star, D+D, has shifted minor floor
(I'_m=4+6=10), so (8<10) rejects that otherwise complete face; it is not
needed by any survivor. All other entries pass (I'_M\ge I'_m).

There is no omitted root packet: two complete branch rows give exactly
(2(10,15)=(20,30)). A multiplicity-1 minor has reduced (r=1), hence depth
bound zero; at zero order the repeated-leading-root alternative would also be
a (Q')-leading root and contradict the minor condition, so the endpoint is
final (`exact-contact-gate...:219-236`). Every multiplicity-2 or -3 major goes by Proposition 5.3 directly
to (D'_1), where Proposition 4.6's constant determinant makes the leading
polynomials squarefree and disjoint. Multiplicities 4 and 5 also go directly to
(D'_1), but fail the actual final residues shown above. No free (W)-level can
repair them.

### 3.2 The (32/24) child: R057 and R058

At (D'_3), ((P_3,Q_3,A_3)=(2,3,1)), and again the unique pattern is
((1,1)). Both factors are major because (1>2/3), each carries
((12,16)), and both are forced to (D'_2). Here
(p=z^2-1, q=z(z^2-1)) gives (D(2,3,p,q)=-2p). At (D'_2),
((P_2,Q_2,A_2)=(4,3,1)), current unit (m'/d'_2=3), and the reduced total
(r=4) has bound 3. The complete list is
((4),(3,1),(2,2),(2,1,1)); ((1,1,1,1)) has four distinct roots and exceeds
(Q_2=3).

| (r) | class | ((\rho_P,\rho_Q)) | (delta_f) | (A'), residues | (J_f) | result |
|---:|---|---|---:|---|---:|---|
| 1 | minor | (3,4) | 5 | (1;(0,0)) | 0 | final; depth 0 |
| 2 | major | (6,8) | (38/13) | (13;(6,8)) | (48/13) | fail |
| 3 | major | (9,12) | (9/4) | (4;(1,0)) | 9 | final pass |
| 4 | major | (12,16) | (52/27) | (27;(12,16)) | (128/9) | fail |

Consequently the sole complete branch type is

\[
 E=(3,1):\quad (\rho_P,\rho_Q)=(9,12)\text{ major at }9/4,
 \ (3,4)\text{ minor at }5,\quad I'_M(E)=9.
\]

It has the exact face
(p=z^3(z-4),q=z(z-4)(z+1)), with
(D(4,3,p,q)=20p). Both top branches are E, so the unique complete root-count
partition exhausts ((24,32)), has

\[
 I'_M=9+9=18,\qquad I'_m=4+1+1=6,
\]

and admits no further split for either multiplicity-1 minor. The two majors go
directly to final (D'_1).

## 4. Why every frozen flat value is nonintegral

The replay values are reproduced exactly, but they are negative controls for
premature finality. In the (30/20) child, treating the unselected top factor as
immediately final applies (5) at (D'_3) and gives

\[
 (\rho_P,\rho_Q,\delta_f,A',J_f)=(10,15,7/8,8,75/4).
\]

Adding this invalid upper packet to selected-branch subtotals gives

\[
 13+75/4=127/4,\quad8+75/4=107/4,\quad4+75/4=91/4,
 \quad9+75/4=111/4.
\]

These are exactly R025--R028 at `child-xu-shifted-46...:76-79`. For the
(32/24) child, the same premature calculation at (D'_3) gives
((12,16,52/27,27,128/9)); adding the selected E subtotal 9 yields
(209/9), exactly R057/R058 at lines 96--97.

The replay says its closure uses a bounded DATA search (`child-xu-shifted-46...:
35-41`) and expressly says that its counts are not kills (lines 109--120,
157--175). Its `cl: empty` entries cannot override the printed fixed-list move.
Replacing the truncated (75/4) by A/B/C/D gives the integral matrix above;
replacing (128/9) by E gives 18.

The depth bound is not a rescue for the truncation. The factor at (D'_3) first
makes the mandatory Proposition-5.3 transition to the fixed (D'_2). At that
current level its root count is 10 with unit 2, hence (r=5), or 12 with unit
3, hence (r=4). The displayed single at-level parting respects bounds 4 and 3.
Afterward, fixed (D'_1) finality or the (r=1) minor bound ends every branch.
Using the old (D'_3) units 10 or 12 at (D'_2) would conflate strict-below
continuation with at-level parting and directly contradict Proposition 5.3.

## 5. Parent transport and the six row verdicts

For an actual parent major orbit with actual centre exponent (epsilon), orbit
size (N), per-disc (P)-root count (ho), and final radius (delta>epsilon),
the declared map gives (`descent-partition-theorem...:71-116`)

\[
 N'=\epsilon N,\quad \rho'=\rho,\quad
 \delta'=4+{\delta-1\over\epsilon},\quad
 (\lambda'_P,\lambda'_Q)={1\over\epsilon}(\lambda_P,\lambda_Q). \tag{7}
\]

Therefore each mapped major contribution is preserved and, on all mapped roots,
(I'_M=u_sI_M=I_M) (`descent-partition-theorem...:167-219`). This is not a
bijection of full partitions: parent minors can regroup and new child minors can
fill the inverse degree count.

The exact-contact parent leaves map numerically as follows.

| source orbit | ((\epsilon,N)) | parent major ((\rho,\delta)) | child ((N',\rho,\delta')) | child term |
|---|---|---|---|---:|
| 180/120 small, (r=2) | ((1/6,6)) | ((4,13/18)) | ((1,4,7/3)) | 4 |
| 180/120 small, (r=3) | ((1/6,6)) | ((6,7/12)) | ((1,6,3/2)) | 9 |
| 180/120 large, (r=2) | ((1/5,5)) | ((4,2/3)) | ((1,4,7/3)) | 4 |
| 180/120 large, (r=3) | ((1/5,5)) | ((6,1/2)) | ((1,6,3/2)) | 9 |
| 192/144 small, (r=3) | ((1/7,7)) | ((9,3/4)) | ((1,9,9/4)) | 9 |
| 192/144 large, (r=3) | ((1/4,4)) | ((9,9/16)) | ((1,9,9/4)) | 9 |

The source ((1,1,2)) large face maps, with the inverse zero group, to child D;
the source ((1,3)) large face maps to child B. The seven small R057/R058 arms
and the four-fold large orbit each map to E. Degree-completing child minors have
zero major charge, exactly as the transport theorem permits.

| row | exhaustive own selection | explicit complete child partition | forced complete (I'_M) | parent certificate | verdict / artifact answer |
|---|---|---|---:|---:|---|
| R025 | first support 3; selected A at (r=2) | A + D | 17 | 17 | **SURVIVES**; not coarse. A+B also gives 22. |
| R026 | first support 2; selected D at (r=2) | D + A | 17 | 17 | **SURVIVES**; not coarse. |
| R027 | first support 3; selected A at (r=3) | A + D | 17 | 17 | **SURVIVES**; not coarse. A+B also gives 22. |
| R028 | first support 2; selected B at (r=3) | B + A | 22 | 22 | **SURVIVES**; this is the exact-contact gate's explicit correction of flat (111/4). |
| R057 | first support 3; selected small E | E + E | 18 | 18 | **SURVIVES**; not coarse. |
| R058 | first support 2; selected large E | E + E | 18 | 18 | **SURVIVES**; not coarse. |

Thus the parents' printed-complete configurations are consistent with the
*correct* child closure, not with the replay's claim that the child has none.
They used actual zero-centre stabilizers, the fixed characteristic list, and
explicit local ODE faces (`exact-contact-gate...:247-317`). Global coefficient
compatibility remains open, so they are not realizing pairs; but no R063-style
coarse-lattice defect is evidenced on these six.

## 6. Finite logic and FALLACY-v2 audit

The universal R063 implication fails at the partition step:

1. Assume a pair realizes one of the six parent rows. Propositions 6.4 and 6.3
   produce the polynomial monic child in the declared ring.
2. The zero/nonzero cases give the singleton own vector printed in §2.
3. Proposition 4.6 and Definition 5.1(4) force top pattern ((1,1)); both top
   packets are major and Proposition 5.3 sends both to (D'_2).
4. Equations (6) and the four-part list for (32/24) exhaust every at-level
   multiplicity pattern. Actual (L'), final residues, ODE witnesses, fixed
   (D'_1) finality, and the (r-1) bound leave A--D or the unique E.
5. Counts exhaust both child degrees. The complete sums are the integer matrix
   in §3.1 and 18 in §3.2; the exact-contact mapped witnesses are among them.
6. Hence (2) supplies no contradiction. Each row **SURVIVES** this gate.

`REPRESENTATIVE` was never promoted to a pair. The frozen flat values were
recomputed but not called resultant degrees. The shifted minor expression was
used only as a floor (it removes D+D); it was not called attained without the
displayed final-minor packets. Actual (L'=1) and (A') were computed per lane.
The source flag, physical coefficient disc, and cover orbit were kept distinct.
The mandatory fixed-list arrival index (D'_2) was not replaced by a legacy
free-(W) search state. No pole identity was used on a minor packet. Every ring
map, member orientation, and prime/derivative convention is declared above.

Exact arithmetic and all discrete alternatives are in
`box/six-rows-child-20260906/audit.json`. Re-run with
`python3 box/six-rows-child-20260906/audit.py --output box/six-rows-child-20260906/audit.json`.
The driver asserts the ten digests, frozen flat controls, ODE identities, root
totals, integral completions, parent-matched witnesses, and verdict count
`SURVIVES=6, DEAD=0, UNDECIDED=0`. Report plus JSON are below 2 MB.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20254`.
- Body SHA-256:
  `1b78971de01d037edbdb35325999e86af3be6d9c9744beeb3c6599ff063bb6d7`.
- Frozen basis: `b5a478eb93b8f92f04be20b28e2e0cb06ccfef8a`.
