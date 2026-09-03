# OPEN[CENTRE-SUPPORT] — zero-factor centres, Prop. 5.6, and 204 → 55

Lane: `centre-support-grok46-20260903`, 2026-09-03.
Charge: `whole-tree-review-opus5-20260903.md` §7.3–§7.4, §10 (the hypothesis
on which the Prop. 5.6 zero-chain kill rests: 288 of `C_FULL_TREE`'s 598
kills; raw emptiness of \(D=60,81,105\)).
No ledger edit, no `jc2-lean`, no `ideation-20260903T1200Z-*`, no other
running-lane report. No exit-price assertion, so no `charge_basis` line.
Drivers: `box/centresupport-drivers-20260903/`.
Source: `refs/moh1983_jram340_configurations_of_roots.pdf`, journal page
\(N\) = PDF page \(N-139\), `pdftoppm -r 300`, pp.145–147, 168–172, 176–185,
188–190, 201.

---

## 0. Frozen-input gate

All eight charged SHA-256 values matched. Stop-on-mismatch was not triggered.

```text
27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096  whole-tree-review-opus5-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  whole-tree-review-grok46-20260903.md
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  moh-program-review-sol56-20260903.md
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  opus5_probe.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  full_tree_partition.py
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  bottomode.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

PATH-ARITH(1–13) is the frozen enumerator's finite space (658 rows at
\(n\le 100\)), not existence of a Jacobian pair.

---

## 1. Executive finding

**The Prop. 5.6 zero-chain kill is justified.** On a still-centred zero
child, \(\sigma_1=\pi t^{\delta_1}\) holds: the parent-level p.201 Galois
already used for (10)/(11), uniqueness of the zero root of \(p\), and
Lemma 1.1 (two centres at distance \(e\) cannot sit in one disc of
logarithmic radius \(>e\)). This is Moh's p.184 argument (“a noninteger
exponent produces different roots”) applied to the unique Galois-fixed
root \(\pi=0\).

The charged \(D_1\) tests — (i) \(\deg g_\sigma=n^*V_2\), (ii) the \(r=1\)
ODE, (iii) increment Galois of order \(A_1\) on \(\pi\) — **do not cut**
the free coefficient. The killing Galois is the *parent* ramification
(\(A_2=5\) on the cheapest row), not \(A_1=2\).

With the lemma, ungated `C_FULL_TREE` is the correct screen: **204 → 55
is restored** at \(n\le 100\) (21 → 11 classes), measured on frozen
`opus5_probe.py`.

Residual, not needed for Prop. 5.6: on a *nonzero* parent factor
(\(C_2\neq 0\)) a twist \(a=\lambda C_2^2\) is Galois-legal as a
polynomial configuration. No Keller witness; no \(D_1\) obstruction.
Typed `OPEN[NONZERO-PARENT-TWIST]`.

---

## 2. What the source writes

### 2.1 Def. 1.3 — PROVED-IN-SOURCE

p.146, Def. 1.3: \(\sigma=\sum_{j<\delta}a_j t^j+\pi t^\delta\in k[\pi]\langle\langle t\rangle\rangle\)
with \(a_j\in k\). p.147: this is “a general point in the disc with radius
\(2^{-\delta}\) centered at \(\sum_{j<\delta}a_j t^j\).” The sum runs over
**all** exponents below \(\delta\), not the tower radii. The charged
display
`centre(D_{j-1})=centre(D_j)+C_j t^{δ_j}+Σ_{δ_j<e<δ_{j-1}} a_e t^e`
is the only reading compatible with Def. 1.3 and Def. 1.1(7). p.201(8)
confines support, per window, to \((1/L_i)\mathbb{Z}\) with
\(L_i=\mathrm{lcm}(\mathrm{den}\,\delta_s,\ldots,\mathrm{den}\,\delta_{i+1})\).
That is a lattice, not a vanishing theorem.

### 2.2 Prop. 5.3 does not vanish the window — PROVED-IN-SOURCE (negative)

p.180: \(\tau=\sum a_j t^j+c_r t^{\delta_r}\in D_r\), and \(\delta_{r-1}\)
is the min of \(\mathrm{ord}(\tau_i-\tau_j)\) among roots strictly closer
to \(\tau\) than \(\delta_r\). The sum is the unrestricted Def. 1.3 centre
of \(D_r\). The proof (pp.180–183) is a numerical squeeze via Lemma 5.2
plus a Prop. 4.4/4.6 contradiction if the actual radius sat strictly
between \(\delta_r\) and \(\delta(M_{r-1})\). Shared intermediate terms
are invisible to pairwise orders, so they are compatible with the formula
for \(\delta_{r-1}\). Lemma 5.2 is purely numerical. Def. 5.1(4) again
writes \(\sigma_i=\sum\alpha_j t^j+\pi t^{\delta_i}\) unrestricted.

### 2.3 The one vanishing Moh proves — PROVED-IN-SOURCE, narrow

p.184, Prop. 5.4, the case \(\delta_i>-1\) and
\(V_{j+1}d_j/d_{j+1}=V_j\) for all higher \(j\) (so \(p\) has a unique
root at every coarser level):

> Since a noninteger exponent \(j\) in the above expression will produce
> different roots for \(g(y)\,T_1^\psi(y)\) as shown in the previous case,
> then all exponents must be integers.

The previous case is \(t^{1/\ell}\to\omega t^{1/\ell}\). This is **only**
the one-point-at-infinity case, not a search condition on a splitting tower.

### 2.4 Prop. 5.6 and the \(s=2\) deduction — PROVED-IN-SOURCE

p.188, hypothesis italicised by Moh: if \(\sigma_1=\pi t^{\delta_1}\), then
either \(k[x,y]=k[T_1^\psi,g]=k[f,g]\) or a degree-reducing automorphism
exists. p.190, \(s=2\), \(\delta_2=-1\), \(0<\delta_1<1\):

> \(\sigma_1=at^{-1}+b+\pi t^{\delta_1}\). And an automorphism
> \(x\to x\), \(y\to y-ax-b\) will change \(\sigma_1\) to \(\pi t^{\delta_1}\).

At \(s=2\), \(L_1=1\), so the only lattice points in \([-1,\delta_1)\) are
\(\{-1,0\}\), both removed. That closes Prop. 5.5. It does not close
\(s\ge 3\).

### 2.5 p.201(11) is an aside — PROVED-IN-SOURCE as text, GAPPED as a rule before this lane

p.201 last sentence: “the situation indicated by the equation (11) can not
always happen as established by Proposition 5.6.” Equation (11) is the
zero-factor continuation \(V_{r-1}=j A_{r-1}+\square_{r-1}\). Prop. 5.6
forbids an all-(11) chain **only under** \(\sigma_1=\pi t^{\delta_1}\).
Moh does not prove that vanishing for \(s\ge 3\). That was
OPEN[CENTRE-SUPPORT].

---

## 3. Cheapest test: \((75,50; M=55,73; V=3,4)\)

### 3.1 Tower data — MEASURED from Def. 5.1 / p.201

```text
n=75, m=50, M=(-50,55,73), V=(V2=3, V3=4, V4=1)
d=(75,25,5,1), n*=3, m*=2, s=3
delta = (-1, 1/5, 1/2)
L2=1, A2=5, L1=5, A1=2
D2: P=20, Q=16, P mod A2=0, threshold 5/4
(10)=True, (11)=False   selected V2=3 is a nonzero orbit
(12)=False, (13)=True   A1=2 | m*V2=6 and A1 | n*V2-1=8
```

Def. 5.1(1) at \(D_1\): \(g\) has \((n/d_2)V_2=9\) roots, \(T_1^\psi\) has
\((m/d_2)V_2=6\). So \(\deg g_\sigma=n^*V_2=9\),
\(\deg T^\psi_{1,\sigma}=m^*V_2=6\). Prop. 4.6 at \(r=1\):

\[
D(n,-M_1,g_\sigma,T^\psi_{1,\sigma})=25(3g_\sigma T'-2T g_\sigma')
=\text{nonzero constant}.
\]

After p.190, the level-2 centre is the coefficient of \(t^{1/5}\): \(C_2\neq 0\)
on the selected (10)-path, \(C_2=0\) on a still-centred zero child. The only
point of \((1/L_1)\mathbb{Z}\) in \((\delta_2,\delta_1)=(1/5,1/2)\) that is
neither a radius nor an integer is \(\{2/5\}\). (The window
\((-1,1/5)\) has \(L_2=1\), lattice \(\mathbb{Z}\), only \(\{0\}\), already
removed.) Generic bottom general point:

\[
\sigma_1=C_2 t^{1/5}+a_{2/5}\,t^{2/5}+\pi t^{1/2}.
\]

### 3.2 Tests (i), (ii), (iii) at \(D_1\) — MEASURED: they do not cut \(a_{2/5}\)

**(i) Degree.** Prop. 1.2: \(g_\sigma(\pi)=c\prod(\pi-\alpha_j)\) over roots
with \(\mathrm{ord}(\sigma-\tau_j)=\delta_1\). If \(a_{2/5}\) is *shared*,
it cancels in every \(D_1\) factor and is strictly higher than the leading
difference to \(D_2\)-siblings (\(\mathrm{ord}=(C_2-C')t^{1/5}\), since
\(1/5<2/5\)) and to the 15 roots outside \(D_2\) (order \(-1\)). The
nine-factor product is \(\prod(\pi-\alpha_j)\), independent of \(a_{2/5}\)
and of \(C_2\); degree stays 9. If \(a_{2/5}\) is an *unshared probe* from
a true centre with \(a=0\), then \(\mathrm{ord}(a t^{2/5})=2/5<\delta_1\),
the probe leaves \(D_1\), and the \(\delta_2\)-face contribution drops
\(\mathrm{ord}\,g(\sigma)\) from \(-3/10\) to \(-6/5\) and \(\deg_\pi\) from
9 to 0. That kills an unshared probe, not a centre coefficient.

**(ii) ODE.** \(3g T'-2T g'\) is a differential polynomial in the star
coefficients of \(g_\sigma,T_\sigma\) (degrees 9 and 6). It does not contain
\(a_{2/5}\). The variety \(\mathrm{D}=\kappa\neq 0\) is a cylinder along
\(a_{2/5}\). Leading cancellation \(3\cdot 6=2\cdot 9\) is identical.

**(iii) Increment Galois of order \(A_1=2\).** p.201: \(\bar t^{10}=t\),
\(\bar t\mapsto -\bar t\). Then \(t^{2/5}=\bar t^4\mapsto t^{2/5}\). This
action **fixes** the whole \((1/5)\mathbb{Z}\) lattice. p.188 still forces
\(\pi\mid g_\sigma\) because \(2\nmid 9\); that is a star condition, not
\(a_{2/5}=0\).

### 3.3 Parent Galois of order \(A_2=5\) — DERIVED, and this is the kill

p.201 at \(r=3\): \(L=1\), \(A_2=5\), \(\bar t^5=t\), \(\bar t\mapsto\omega\bar t\),
\(\omega^5=1\). This is \(\mathrm{Gal}(k((t^{1/5}))/k((t)))\), the same
action that yields (10)/(11) at \(V_2\). On \(t^{2/5}=\bar t^2\): multiplier
\(\omega^2\neq 1\) (cyclotomic: \(\omega^2=\exp(4\pi i/5)\)).

**Zero-factor child (\(C_2=0\)).** Centre \(a t^{2/5}\). Resultant of
\(y-a W^2 u^2\) against \(W^5-1\) is \(y^5-a^5 u^{10}\) over \(\mathbb{Q}\)
(0.01 s). For \(a\neq 0\) this is **five** distinct centres
\(a\omega^{2k}t^{2/5}\), pairwise at logarithmic distance \(2/5<\delta_1=1/2\).
By Lemma 1.1 they cannot lie in one disc of radius \(1/2\). They would be
five children of \(D_2\), all with \(t^{1/5}\)-coefficient \(0\), contradicting
uniqueness of the zero root of \(p\) (one root at \(0\), multiplicity
\(b\in\{5,10,15,20\}\)). Equivalently the tree would display an extra radius
\(2/5\) between \(1/5\) and \(1/2\). Hence \(a_{2/5}=0\). At \(a=0\) the
orbit collapses to \(y^5\): one centre.

**Nonzero parent (\(C_2\neq 0\)), selected path of this printed row.**
Twisting \(a=\lambda C_2^2\) sends the five images to the five sibling discs
already present as the (10)-orbit of \(C_2\). The resultant of
\(y-CWu-\lambda C^2 W^2 u^2\) against \(W^5-1\) lies in
\(\mathbb{Q}[C,\lambda,y,u]\), monic of degree 5 in \(y\); at \(\lambda=0\)
it is \(y^5-C^5 u^5\). Galois + polynomiality of the centre configuration
do not force \(\lambda=0\). No Jacobian pair with \(\lambda\neq 0\) was
constructed. Typed `OPEN[NONZERO-PARENT-TWIST]`.

### 3.4 Verdict on item (1)

```text
D1 tests (i)(ii)(iii)      do not cut a_{2/5}         MEASURED
parent Galois A2=5
  on a zero-factor child   a_{2/5} FORCED ZERO        DERIVED
  on a (10)-child          a=λ C2^2 Galois-legal      MEASURED as a
                                                      configuration;
                                                      UNDECIDED as a
                                                      Keller coefficient
Prop 5.6 on this row's
  still-centred zero
  siblings                 hypothesis restored         DERIVED
mechanism                  parent Galois (p.201/p.184
                           uniqueness), not the ODE,
                           not the D1 degree count,
                           not A1=2. Uniform on every
                           still-centred zero child.
```

The 288 ungated kills are kills of still-centred **zero** children. For
those, \(C_2=0\) and \(a_{2/5}\) is forced zero. The gap that `C_FULL_TREE`
rests on **closes**.

---

## 4. Item (2): \((64,48)\) and the empty-free control \((99,66)\)

**\((64,48; V_2=V_3=3)\).** \(\delta=(-1,1/4,9/16)\), \(A_2=4\),
free \(\{1/2\}\), selected path is (10). Parent Galois \(\bar t^4=t\),
\(t^{1/2}=\bar t^2\mapsto\pm\bar t^2\), orbit size 2. Resultant
\((y^2-a^2 u^4)^2\). Two centres at distance \(1/2<9/16=\delta_1\), same
contradiction on a zero child. \(A_1=4\) increment fixes \(t^{1/2}\).
ODE/degree at \(D_1\) again a cylinder. Same verdict, same mechanism.

**\((99,66; V_2=V_3=8)\).** \(\delta=(-1,1/3,4/9)\), free in
\((\delta_2,\delta_1)=\emptyset\) (next \((1/3)\mathbb{Z}\)-point after
\(1/3\) is \(2/3>4/9\)). After p.190, \(\sigma_1=C_2 t^{1/3}+\pi t^{4/9}\).
On a still-centred zero child, \(C_2=0\) and there is no lattice room for
an extra term, so \(\sigma_1=\pi t^{4/9}\) with **no extra hypothesis**.
Prop. 5.6 applies unconditionally. Control holds.

**Printed six, window-correct free sets** (158 empty / 500 nonempty among
658 selected chains) — MEASURED, agrees with the charge:

```text
(64,48; 3,3)   δ=(-1,1/4,9/16)    free={1/2}
(75,50; 2,4)   δ=(-1,1/5,2/3)     free={2/5,3/5}
(75,50; 3,4)   δ=(-1,1/5,1/2)     free={2/5}
(84,56; 2,3)   δ=(-1,2/7,16/21)   free={3/7,4/7,5/7}
(84,56; 5,3)   δ=(-1,1/4,7/12)    free={1/2}
(99,66; 8,8)   δ=(-1,1/3,4/9)     free=∅
```

All six selected paths are (10), not (11). Prop. 5.6 never applies to the
*selected* printed path; it applies to the still-centred zero *siblings*
that p.200(4) obliges the whole-tree recursion to extend.

---

## 5. The lemma that closes OPEN[CENTRE-SUPPORT] for Prop. 5.6

**Lemma (Zero-factor centre support).**
Let \(f,g\in k[x,y]\) satisfy the Jacobian condition with \(\deg=\deg_y\),
and let \(D_s\supseteq\cdots\supseteq D_r\) be a tower of major discs
satisfying Def. 5.1, \(r\ge 2\). Suppose the chart at \(D_r\) is centred
at 0 and \(\pi\) is a factor of the Prop. 4.6 polynomial \(p(\pi)\). Let
\(L,A_{r-1}\) be as in p.201(8) at this \(r\), and let \(\omega\) be a
primitive \(A_{r-1}\)-th root of unity acting by \(\bar t\mapsto\omega\bar t\),
\((\bar t)^{L A_{r-1}}=t\). Let \(D_{r-1}\) be the unique child corresponding
to this zero factor, of logarithmic radius \(\delta_{r-1}\). Then every
coefficient of the centre of \(D_{r-1}\) at an exponent
\(e\in(\delta_r,\delta_{r-1})\) which is moved by this action vanishes.

In particular, after the p.190 removals of the integer exponents \(-1\) and
\(0\), iterating down a still-centred chain yields \(\sigma_1=\pi t^{\delta_1}\).
Prop. 5.6 therefore applies to every all-(11) major path that reaches \(D_1\).

**Hypotheses, all source:** Def. 1.3 (\(a_e\in k\)); p.201(8) (the
automorphism); uniqueness of the root \(\pi=0\) of \(p\); Lemma 1.1; p.184's
Galois production of distinct roots from a moved exponent; p.190 for the
integers. No Jacobian identity beyond the existence of \(p\) is used.

**Proof.** A term \(a t^e\) with \(a\in k^\times\) is sent to
\(a\,\omega^{L A_{r-1}e}t^e\). If the multiplier is nontrivial, the orbit
consists of more than one distinct centre, pairwise at logarithmic distance
\(e\). By Lemma 1.1 they cannot lie in one disc of radius \(\delta_{r-1}>e\).
They would be distinct children of \(D_r\) with the same \(t^{\delta_r}\)-coefficient
\(0\), contradicting uniqueness of the zero root of \(p\). Hence \(a=0\).
For the standard parent ramification \(L=1\), \(\bar t^A=t\), the fixed
exponents are the integers, already removed by p.190. On a still-centred
chain every parent is a zero factor, so every window is killed, and
\(\sigma_1=\pi t^{\delta_1}\).

**Type.** DERIVED from the cited source statements. Not a quoted lemma of
Moh. The p.184 case is the specialisation “\(p\) has a unique root”; the
zero-factor specialisation is the one Prop. 5.6 needs, and p.201 already
installs the Galois action that moves the free exponents.

**What the lemma does not say.** It does not force twisting coefficients on
a (10)-child (\(C_r\neq 0\)): those Galois images are the existing nonzero
siblings. That is `OPEN[NONZERO-PARENT-TWIST]` and is not an input to
Prop. 5.6.

---

## 6. Screens at \(n\le 100\), lemma accepted

Frozen `opus5_probe.py` (SHA `4402bf52…5d11ad9`), 658 PATH-ARITH rows,
6/6 printed kept in every line. Desk, 4.5 s one core.

| screen | rows | classes | excess | Prop. 5.6 |
|---|---:|---:|---:|---|
| PARTITION (danger off) | 348 | 52 | 342 | none |
| PARTITION + ODE | 347 | 52 | 341 | none |
| PARTITION + ODE + passport | 330 | 52 | 324 | none |
| GATED (empty-free only) | 216 | 21 | 210 | gated |
| GATED + ODE | 215 | 21 | 209 | gated |
| GATED + ODE + passport | **204** | **21** | 198 | gated |
| UNGATED (`C_FULL_TREE`) | 60 | 12 | 54 | lemma |
| UNGATED + ODE | 58 | 12 | 52 | lemma |
| UNGATED + ODE + passport | **55** | **11** | 49 | lemma |

**204 → 55 is restored.** 21 → 11 classes. Matches the charged
`C_FULL_TREE` / `C_FULL_TREE_PASSPORT` counts the second gate already
replayed (60 / 58 / 55). The 288 of 598 kills the gate flagged as gapped
are the still-centred zero children to which the lemma applies.

Raw-row emptiness of \(D=60,81,105\) is therefore restored. The ray
verdicts (\(A_2=6\), \(L=8a+5\)) and the pinned-\(N\) emptiness of
\(D=105,117\) were already gap-free and are untouched.
`OPEN[MOH-PROGRAM-ARTIFACT]` residual after the restored screen: 49 excess
rows / 5 excess classes at \(n\le 100\) under UNGATED+ODE+passport
(re-based from the gated 198 / 17 back to the charged 49 / 5).

---

## 7. Typed block

```text
(1) CHEAPEST TEST (75,50; 3,4)
    Def 5.1(1) degrees 9 and 6                 MEASURED
    σ1 = C2 t^{1/5} + a t^{2/5} + π t^{1/2}
      after p.190; C2 is the D2-centre         PROVED-IN-SOURCE (shape)
    (i) deg g_σ = 9 does not cut a             MEASURED (Prop 1.2)
    (ii) r=1 ODE does not cut a                MEASURED (cylinder)
    (iii) A1=2 does not cut a                  MEASURED (fixes (1/5)Z)
    parent Galois A2=5, C2=0: a FORCED ZERO    DERIVED (p.201+Lem 1.1)
    parent Galois A2=5, C2≠0: a=λ C2^2 legal   MEASURED as configuration
    VERDICT for Prop 5.6: FORCED ZERO,         mechanism = parent Galois,
      uniform on still-centred zero children.  not ODE, not D1 degree, not A1.

(2) (64,48; 3,3) free {1/2}: same mechanism    DERIVED / MEASURED
    (orbit size 2 under A2=4).
    (99,66) free ∅: Prop 5.6 applies to        MEASURED
    zero children with no extra hypothesis.

(3) SOURCE: intermediate coefficients
    Def 1.3 / Def 5.1(4) / Prop 5.3: sum       PROVED-IN-SOURCE
      unrestricted; Prop 5.3 does not vanish
      the window (δ_r, δ_{r-1}).
    Lemma 5.2: numerical, no coefficients.     PROVED-IN-SOURCE
    p.184: integers forced only if p has a     PROVED-IN-SOURCE (narrow)
      unique root at every coarser level.
    p.190: s=2, y ↦ y-ax-b.                    PROVED-IN-SOURCE
    p.201 l.52: aside citing Prop 5.6;         PROVED-IN-SOURCE as text;
      hypothesis σ1=π t^{δ1} unverified in       the hypothesis is now
      source for s≥3.                            supplied by the lemma.

(4) LEMMA[ZERO-FACTOR-CENTRE]                  DERIVED
    => ungated C_FULL_TREE justified.
    n≤100 screens (frozen opus5_probe):        MEASURED
      gated+ODE+passport   204 / 21
      ungated+ODE+passport  55 / 11
    204 → 55 RESTORED.  D=60,81,105 empty
    at raw-row level again.  Rays and pinned-N
    of D=105,117 untouched (already gap-free).

OPEN[NONZERO-PARENT-TWIST]                     OPEN (bounded)
    Can λ≠0 occur on a (10)-child of a
    Jacobian pair?  Cheap tests do not forbid
    it; no Keller witness.  Not an input to
    Prop 5.6.  Bound: the 348 partition-only
    rows at n≤100 with a (10)-edge at D2.
    Cheapest test: one (75,50; V=3,4) pair,
    or the star system of bottomode.py with
    the twisted centre substituted into the
    next order of LOCAL-KELLER.

ARTIFACTS  box/centresupport-drivers-20260903/
           centre_support_test.py  (40/40 checks)
           rerun_screens.py        (204→55)
No ledger edit. No jc2-lean.
```

---

## 8. FALLACY-v2

No cv-flag / place / series identification. No per-ray exit charge. No
`REPRESENTATIVE`/`FULL_ACTUAL_EXIT` claim. No pole identity. Floor/attainment:
the 55 is a PATH-ARITH residue, not an attainment of 55 Jacobian pairs.
`sat()` unused. Variable map for the resultants: ring
\(\mathbb{Q}[C,\lambda,y,u]\) and \(\mathbb{Q}[a,y,u]\), generator order as
written, image check = the resultant against \(W^A-1\) lies in that ring
(coefficients in \(\mathbb{Q}\), no cyclotomic leftover). Prime marks unused.
No Statement 8.5. No target/arrival index.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19828`.
- Body SHA-256:
  `c6acd87403180ca492cae9479c0dc2ec54f359aaa46aa453e28a4ce40fefdc00`.
- Frozen inputs (SHA-256): as in §0 (eight charged hashes, all matched).
