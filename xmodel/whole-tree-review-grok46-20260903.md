# Hostile review: WHOLE-MAJOR-TREE NECESSITY

Lane: whole-tree-review-grok46, 2026-09-03.
Charged: Sol `moh-program-review-sol56-20260903.md` §3.1, §3.3, §5.1 and
`box/mohprog-drivers-20260903/`.
Task: source-first re-transcription; independent whole-tree recursion;
row-for-row survivor diff; answers (a)–(g); typed promotion.

No ledger edit, no `jc2-lean`, no `ideation-20260903T1015Z-*` file, no other
running-lane report. No exit-price assertion, so no `charge_basis` line.

---

## 0. Frozen-input gate and method

All ten frozen SHA-256 values matched. Stop-on-mismatch was not triggered.

```text
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  moh-program-review-sol56-20260903.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  branch-orbits-v2-grok46-20260903.md
c61bb15528b25587578ac10101cb18267e83150fa6ea541e250f606e648d5418  branch-orbits-v2-review-gpt55-20260903.md
982c75da179e263e109d0bf6ba0e8b13e591225c80d0111d24ba32b61be67896  n6-family-review-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553  candidate_eval.py
c2a27632d54576abbca54b9f268a7fa5d2b144497a1e364c93102450a066baf9  tree-independent.py
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  candidate-results.json
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  moh1983_jram340_configurations_of_roots.pdf
```

Journal page \(N\) is PDF page \(N-139\). Propositions were read from
`pdftoppm -r 300` renderings **before** charged §3 was opened.
`tree-independent.py` was not opened until an independent recursion had
run. That first recursion (no top-chart danger flag) produced 20 or 348
survivors according to whether every zero factor at \(D_1\) was killed.
After the source chart of Lemma 5.3 + Prop. 5.6 was encoded, the same
code path produced 60/58/55/23/20 and matched both charged drivers
row-for-row. The 60 is therefore not an accidental copy of the charged
count: it is the unique arithmetic that couples Prop. 5.3's universal
extension to Prop. 5.6's still-centred zero leaf.

PATH-ARITH(1–13) means the finite space of the frozen enumerator, not
existence of a Jacobian pair. Counts below are of arithmetic skeletons.

---

## 0.1 Executive finding

The local extension obligation is **PROVED-IN-SOURCE**. Proposition 5.3
applies to **any** factor \(\pi-C_r\) whose multiplicity lies in the
window; the p.200 Theorem (4) is a universal conditional over the
covering subdiscs \(E_i\). “Every above-threshold sibling extends” is
Moh's statement at p.200(4) and a consequence of the Prop. 5.3 proof
(the proof uses only the multiplicity, not a privileged choice). It is
not an over-reading of an existential lemma.

The finite DP `C_FULL_TREE` is **DERIVED**: it is a correct arithmetic
model of that obligation plus the p.201 orbit action, the Lemma 5.3
top-chart translation, and Prop. 5.6 on a still-dangerous zero leaf. It
is not a theorem Moh states, and it is not a sufficiency theorem for
\((f,g)\). Measured on PATH-ARITH at \(n\le 100\), \(K_{\min}=2\):

| screen | rows | \((n,m)\) classes | printed killed | \((75,50)\) residue |
|---|---:|---:|---:|---|
| PATH-ARITH(1–13) | 658 | 63 | 0 | 9 rows, several \(M_2\) |
| `C_FULL_TREE` | **60** | **12** | 0 | \(\{M_2=55,\,V_2\in\{2,3\}\}\) |
| + ODE (3.7) | **58** | 12 | 0 | same |
| + passport (3.8) | **55** | 11 | 0 | same |
| + edgewise recenter | 23 | 7 | 0 | same |
| + recenter + ODE | **20** | 7 | 0 | same |

Three independent implementations agree on all six counts row-for-row:
this lane's recursion, frozen `tree-independent.py --zero-only`, and
`full_tree_partition.py` as imported by `candidate_eval.py`. Moh's six
printed rows survive every screen. The screen does **not** close
`OPEN[MOH-PROGRAM]`: 49 excess rows remain after the strongest
source-derived package (passport).

On the campaign space the emptiness claims are MEASURED for the derived
screen, not source-proved emptiness of pairs: \(D=105\) and \(D=117\)
have **no** `C_FULL_TREE` survivor. Sol's \(L=8a+5\) ray (\(a=0..3\))
and the four geometric \(A_2=6\) members of \(n=9(7t+6)\) (\(t=0..3\))
all die by the same forced major-zero sibling at \(j=2\).

---

## 1. Independent transcriptions (from 300-dpi page images)

Notation. \(n=\deg_y g\), \(m=-\,M_1=\deg_y T_1^\psi\), \(d_r=\gcd\{n,M_1,\ldots,M_{r-1}\}\),
\(V_{s+1}=d_{s+1}\), \(M_s=n-2\) the last effective pair. Def. 4.1 p.164:
\(D(a,b,p,q)=a\,p\,q'-b\,q\,p'\).

### Proposition 4.6 (pp.170–171)

**Hypothesis.** For some \(r,\lambda,v\) and a \(\pi\)-root
\(\sigma=\sum a_j t^j+\pi t^\delta\) of \(g(y)\):
(1) \(\deg_y g=n>1\);
(2) \(\operatorname{ord} g(\sigma)=n\lambda<0\), \(\operatorname{ord} T_i^\psi(\sigma)=(-\mu_i)\lambda\) for \(i=1,\ldots,r\);
(3) \(\lambda=(-1+\delta)/(n-m_r)<(-1+\delta)/(n-m_i)\) for \(i=1,\ldots,r-1\);
(4) \(\deg g_\sigma(\pi)=v(n/d_r)\);
(5) \(\deg T_{r,\sigma}^\psi(\pi)=v(-\mu_r/d_r)=v((-\mu_r+M_r-n)/d_r)+v((n-M_r)/d_r)\).

**Conclusion, \(r\ge 2\).**
(1) \(\sigma\) is a distribution detector for \(g,T_1^\psi,\ldots,T_{r-1}^\psi\).
The leading coefficients of \(g(\sigma),T_1^\psi(\sigma),\ldots,T_{r-1}^\psi(\sigma)\)
are powers of a common polynomial \(p(\pi)\) of degree \(v\).
(2) \(T_{r,\sigma}^\psi(\pi)=p(\pi)^{(-\mu_r+M_r-n)/d_r}\cdot q(\pi)\) with
\(\deg q=v((n-M_r)/d_r)\).
(3) \(q\) has all distinct roots.
(4) all roots of \(p\) are roots of \(q\).
(5) \(p\) is not a power of \(q\).

If \(r=1\), \(D(n,-M_1,g_\sigma,T_{1,\sigma}^\psi)=\) nonzero constant.
The proof reduces the Jacobian ODE to
\(D\bigl(v(-\mu_r/d_r),p,T_{r,\sigma}^\psi\bigr)=C^*p^{(\cdots)+1}\),
then cites Appendix I Props. A.3 and A.4.

At disc \(D_j\) this is charged (3.1):
\(P_j=V_{j+1}d_j/d_{j+1}\), \(Q_j=V_{j+1}(n-M_j)/d_{j+1}\).

### Definition 5.1 (p.179)

A tower \(D_s\supseteq D_{s-1}\supseteq\cdots\supseteq D_r\) of major discs,
with integers \(\{V_i:i=r+1,\ldots,s+1\}\), satisfies:
(1) in \(D_i\), \(g\) has precisely \((n/d_{i+1})V_{i+1}\) roots, and
\(T_j^\psi\) has \((-\mu_j/d_{i+1})V_{i+1}\) roots for \(j=1,\ldots,i\);
(2) \(V_{i+1}d_i/d_{i+1}\ge V_i>d_i/(n-M_i)\) for \(i=r+1,\ldots,s\), and
\(V_{s+1}=d_{s+1}\);
(3) logarithmic radius \(\delta_i\) as the displayed product over
\(V_j,\,j=i+1,\ldots,s\) (depends on the **whole** \(V\)-path above \(i\),
not on \(V_i\));
(4) the unique general point in \(D_i\) satisfies Prop. 4.6 with
\(v=V_{i+1}(d_i/d_{i+1})\).

Immediately after the definition Moh writes the existential gloss of
Prop. 5.2: “any subdisc can be used as \(D_{s-1}\) if it contains more
than the average number of roots. The existence of such a subdisc is
ensured by Proposition 4.6.”

### Proposition 5.2 (p.176)

\(g\) monic, \(n>1\), \(M_s\) the largest \(M_i<n-1\), \(s\ge 2\).
Let \(\sigma\) be the unique \(\pi\)-root of \(g\prod_{i=1}^s T_i^\psi\)
in the \(\delta_s\)-disc \(D_s\), and let \(\pi-c_s\) be **a** factor of
\(p(\pi)\) (cf. Prop. 4.6) with multiplicity \(V_s>d_s/(n-M_s)\).
Then \(\delta_{s-1}\) is the displayed formula, and Prop. 4.6 holds at
\(D_{s-1}\) with \(v=V_s(d_{s-1}/d_s)\). Special case of Prop. 5.3.

### Lemma 5.2 (pp.177–179) — **not** a \(q\)-capacity lemma

Numerical lemma used in the proof of Prop. 5.3. For numbers
\(L\le M_r<\cdots<M_s<n-1\) and \(V_i(n-M_i)>d_i\), it defines a
monotone \(\delta(L)\) and \(\lambda(L)\), and proves
\(\bigl((n-L)/d_r\bigr)\lambda^*=-1+\delta^*<0\).
**This is not** \(A_j\mid Q_j-1\). Charged (3.4) mislabels it.

### Proposition 5.3 (pp.180–183) — exact hypothesis

> Suppose that \(g(x,y)\) is monic in \(y\) with \(y\)-degree \(n>1\) and
> for \(r\ge 2\) a tower of major discs \(D_s\supseteq\cdots\supseteq D_r\)
> is constructed. Let \(\pi-C_r\) be a factor of \(p(\pi)\) as in the
> conclusions of Proposition 4.6 with multiplicity \(V_r\) satisfying
> \[
> \deg p(\pi)=V_{r+1}\Bigl(\frac{d_r}{d_{r+1}}\Bigr)\ge V_r>\frac{d_r}{n-M_r}.
> \]

Then \(\delta_{r-1}\) is the Def. 5.1(3) formula at \(i=r-1\), and
\(D_s\supseteq\cdots\supseteq D_r\supseteq D_{r-1}\) is a tower of major
discs. The proof verifies Def. 5.1(1)(3)(4) at the new disc by comparing
orders to Prop. 4.4 / 4.6; the only datum of the chosen factor that
enters is its multiplicity \(V_r\) (and that it is a root of \(p\)).
Nothing in the proof distinguishes one above-threshold factor from
another. Q.E.D. p.183.

### Proposition 5.4 (p.183)

If a tower \(D_s\supseteq\cdots\supseteq D_1\) is constructed, the
smallest disc containing **all** roots of \(g(y)T_1^\psi(y)\) is \(D_i\)
with
\[
i=\max\bigl\{r:\tfrac{V_{r+1}d_r}{d_{r+1}}>V_r\bigr\}.
\]
If \(\delta_i>-1\), then either \(k[x,y]=k[T_1^\psi,g]=k[f,g]\), or there
exists an automorphism of \(k[x,y]\) reducing the degrees of
\(T_1^\psi(f,g)\), \(g\), and \(f\) simultaneously.

The proof translates **at that globally selected disc**: for \(i>1\),
the unique \(\pi\)-root in \(D_i\) has the form \(h(x)+\pi t^{\delta_i}\),
and \(y\mapsto y-h(x)\) centres it. This is not an edgewise rule.

### Proposition 5.6 (pp.188–189)

If \(s\ge 2\) and a tower \(D_s\supseteq\cdots\supseteq D_1\) has been
constructed, and the unique \(\pi\)-root in \(D_1\) is of the form
\(\sigma_1=\pi t^{\delta_1}\), then either the rings already agree or a
polynomial automorphism simultaneously reduces the degrees of \(f\), \(g\),
and \(T_1^\psi(f,g)\). Both outcomes contradict the p.200 search premise
(degrees not simultaneously reducible, \(J=1\)).

p.201 last sentence: “the situation indicated by equation (11) cannot
always happen as established by Proposition 5.6.”

### p.200 Theorem (exact (4), (5), (7))

After constructing a tower down to \(D_r\), the roots of
\(\prod_{i=1}^r g\,T_i^\psi\) in \(D_r\) are covered by a disjoint union
of subdiscs \(\bigcup E_j\) (Def. 1.1). Then:

> **(4)** if the number of roots of \(g(y)\) in \(E_i\) is
> \(> n/(n-M_r)\), then the tower can be extended to
> \(D_s\supseteq\cdots\supseteq D_r\supseteq E_i\);
>
> **(5)** if that number is \(\le n/(n-M_r)\), then \(E_i\) is a minor
> disc (and a distribution-detector statement);
>
> **(6)** the number of subdiscs is bounded by \((n-M_r)V_{r+1}/d_{r+1}\)
> (that is \(Q_r\));
>
> **(7)** there must be at least one \(E_i\) satisfying (4).

Proof: “Propositions 5.4 and 6.1.”

### p.201 orbit action (9)–(13)

\(A_{r-1}\) is the reduced denominator of \(L\delta_{r-1}\), \(L=\operatorname{lcm}\)
of reduced denominators of \(\delta_s,\ldots,\delta_r\). Division:
\(V_r(d_{r-1}/d_r)=\triangle_{r-1}A_{r-1}+\square_{r-1}\).
Galois \(\bar t\mapsto\omega\bar t\), \(\omega\) an \(A_{r-1}\)-th root of unity.
Then (10) \(V_{r-1}\le\triangle_{r-1}\) if the factor is \(\pi-a\), \(a\ne 0\);
(11) \(V_{r-1}=j A_{r-1}+\square_{r-1}\) if the factor is \(\pi\).
At \(r=2\): (12) or (13) as printed, matching p.188
\(A\mid n^*V_2\) and \(A\nmid m^*V_2\), or the swap, together with
\(A\mid(n^*+m^*)V_2-1\) “from the very definition of \(A\)”.

### Proposition A.3 (p.205)

Let \(m=\deg p\), \(n=\deg q\). Suppose \(D(m,n,p,q)=c\,p\) with
\(c\ne 0\in k\). Then: (1) every root of \(p\) is a root of \(q\);
(2) \(q\) has no multiple root; (3) \(p\) is not a power of \(q\);
(4) at least one root of \(p\) has multiplicity \(>m/n\).

**The right-hand side is \(cp\), not \(c\).** Quoted from the image.

### Lemma 5.3 (pp.185–186)

The smallest disc containing all roots of \(g T_1^\psi\) has logarithmic
radius \(-1\) iff \(M_s=n-2\) and the highest homogeneous form of \(g\)
has two roots, one of multiplicity \((n/d_s)v_s\) with \(d_s>v_s>d_s/2\).

---

## 2. Answer (a). The universal quantifier

**Exact hypothesis of Prop. 5.3.** “Let \(\pi-C_r\) be a factor of
\(p(\pi)\) as in the conclusions of Proposition 4.6 with multiplicity
\(V_r\) satisfying \(\deg p=V_{r+1}(d_r/d_{r+1})\ge V_r>d_r/(n-M_r)\).”

This is a **universal conditional**: *any* factor whose multiplicity
lies in the window. It is not “there exists a chosen factor.” Prop. 5.2's
gloss on p.179 is existential (“any subdisc *can* be used … existence is
ensured”), which is the language of constructing one tower. Prop. 5.3
is the general step, and its proof never uses uniqueness of the factor.

**p.200 Theorem (4) quantifier.** The covering is a disjoint union of
**all** subdiscs \(E_j\). Clause (4) is “if the number of roots of \(g\)
in \(E_i\) is \(>n/(n-M_r)\), then the tower extends to \(E_i\).” There
is no “for some \(i\)” inside (4). The companion (7) is the existential
“at least one.” So (4) is **for every \(i\)** in the covering that meets
the count. The count \(>n/(n-M_r)\) is the same threshold as
\(u>d_r/(n-M_r)\) after Prop. 4.6(1) (number of \(g\)-roots in the
subdisc is \((n/d_r)\) times the \(p\)-multiplicity, up to the local \(v\)).

**Verdict.** “Every above-threshold sibling extends” is

- Moh's statement at p.200(4), and
- a consequence of the Prop. 5.3 proof (uniform in the choice),

not an over-reading of Prop. 5.2. What *is* derived, not quoted, is the
assembly of these local extensions into a finite DP over all Galois
orbit partitions with a top-chart danger flag. Type that assembly
DERIVED. Type the local obligation PROVED-IN-SOURCE.

The charged §5.1 sentence “this applies to *every* such factor, not just
to the factor chosen for the displayed \(V\)-path” is correct.

---

## 3. Answer (b). Partition (3.3) and capacity (3.4)

### Orbit sizes are \(A_j\)

p.201: \(\bar t\mapsto\omega\bar t\) with \(\omega^{A_{r-1}}=1\) acts on
the local \(\pi\) of the \(D_{r-1}\) chart by \(\pi\mapsto\zeta\pi\).
Nonzero roots therefore come in orbits of size exactly \(A_j\). That is
the content of charged “delta 17(j)”: **yes**, nonzero-orbit cardinality
is \(A_j\). Fixed locus: \(\pi=\zeta\pi\Rightarrow\pi(\zeta-1)=0\Rightarrow\pi=0\)
only. **At most one fixed root.**

### \(b\equiv P_j\pmod{A_j}\)

Write \(p(\pi)=\pi^b\prod_\ell(\pi^{A}-c_\ell)^{u_\ell}\) with \(c_\ell\ne 0\).
Then \(P=b+A\sum u_\ell\), so \(b\equiv P\pmod A\). This is exactly (9)
plus (11): \(\square\equiv P\pmod A\) is the canonical remainder, and
(11) allows \(b=\square+jA\). Forced: **yes**, any actual factorisation
compatible with the Galois action has \(b\equiv P\pmod A\). The minimal
nonnegative representative is \(P\bmod A\in\{0,1,\ldots,A-1\}\). If that
remainder is positive then a zero root of \(p\) **must** exist.

### Is \(A_j\mid Q_j-1\) Lemma 5.2's content?

**No.** Lemma 5.2 is the \(\delta(L)\) numerical lemma. The capacity
statement is **DERIVED** from: \(q\) squarefree (Prop. 4.6(3)), p-roots
\(\subset\) q-roots (Prop. 4.6(4)), and the same Galois action. Then
\[
q(\pi)=\pi^\varepsilon\prod_{k=1}^{S}(\pi^A-d_k),\qquad\varepsilon\in\{0,1\},
\]
so \(Q=\varepsilon+A S\) and \(Q\bmod A\in\{0,1\}\). If \(b\ge 1\) then
\(0\) is a \(p\)-root hence a \(q\)-root, so \(\varepsilon=1\) and
\(A\mid Q-1\). If \(b=0\), \(\varepsilon\) may be \(0\) or \(1\).

p.188 gives \(A_1\mid(n^*+m^*)V_2-1\) from the definition of \(A_1\) as
reduced denominator of \(\delta_1\), which is a **different** identity
(and holds on all 658 PATH-ARITH rows). Charged (3.4) as a selected-path
filter is automatic: every one of the 658 rows has \(A_j\mid Q_j-1\) at
every printed level. It kills nothing by itself. Type: DERIVED Galois
capacity; OVER-READING as a Lemma 5.2 citation.

### Several fixed \(q\)-roots?

**No.** Unique Galois-fixed point. Squarefreeness does not create extra
fixed points. The zero-root count of \(q\) is \(0\) or \(1\).

### Unused slots

Yes, correctly allowed. Extra \(q\)-roots with \(p\)-multiplicity \(0\)
are unused slots: either the unused zero (\(\varepsilon=1,\,b=0\)) or
extra nonzero \(A\)-orbits. Distinct \(p\)-roots
\(=(1\text{ if }b\ge 1\text{ else }0)+A\cdot(\#\text{orbits})\le Q\).
p.200(6) is the same bound (number of subdiscs \(\le Q\)).

---

## 4. Answer (c). The recursion, state, and worked examples

### Child data when a sibling of multiplicity \(u\) becomes the next major disc

\(n\), \(m\), \(\{M_i\}\), \(\{d_i\}\) are **global** characteristic data
of \((f,g)\). They do not change per branch. The child's \(V_j\) **is**
\(u\). At the child disc \(D_j\) (already constructed as a major disc
with this multiplicity), Prop. 4.6 produces a new \(p,q\) of degrees
\[
P' = u\cdot\frac{d_{j-1}}{d_j},\qquad
Q' = u\cdot\frac{n-M_{j-1}}{d_j}.
\]
So the child's next \(Q\) **is** determined by \(u\) together with the
global \((n,M_{j-1},d_j)\). Charged DP that stores only
\(({\rm level},u)\) can recompute \(P',Q'\) if it still has the globals.

### Radii and \(A\) are not functions of \(({\rm level},u)\) alone

Def. 5.1(3): \(\delta_i\) is a product over \(V_{i+1},\ldots,V_s\).
p.201(8): \(A_j\) uses \(\delta_j\) and \(\operatorname{lcm}(\operatorname{den}\delta_s,\ldots,\operatorname{den}\delta_{j+1})\).
A sibling at level \(j\) with a **different** \(V_j=u\) changes
\(\delta_{j-1}\) and \(A_{j-1}\) of everything below it. State
\(({\rm level},{\rm multiplicity})\) **forgets the branch's \(\delta\)-sequence
and \(A\)-sequence** unless the higher \(V\)-tuple is part of the state.
Both working implementations store that tuple (`high` in
`tree-independent.py`; `path` in `full_tree_partition.py`). At \(s=3\)
the higher tuple is just \(V_3\), so the forgetfulness is invisible;
at \(s\ge 4\) it is not. Type: DERIVED implementation constraint, forced
by Def. 5.1(3).

### How Prop. 5.6 enters the DP (the 60, not 348 or 20)

Lemma 5.3: at \(D_s\), \(p\) has two roots, selected \(V_s\) major,
complement minor. Translating the \(\pi\)-chart so the selected root is
at \(0\) is the same coordinate change Prop. 5.3 writes as
\(\tau=\sum\alpha_j t^j+c_r t^{\delta_r}\). After that translation the
selected tower **begins as a zero factor**. A boolean `danger` records
that the chart is still centred at \(0\):

- zero label keeps `danger`;
- nonzero label clears it, **unless** the exploratory edgewise-recenter
  rule (integral \(\delta\)) is on;
- at \(j=2\), every major child must obey (12)/(13); if `danger` is
  still true, Prop. 5.6 kills that leaf.

A first recursion that killed **every** zero factor at \(D_1\), ignoring
whether `danger` had already been cleared by a nonzero ancestor, produced
20 rows (Moh's six kept). A recursion that never applied Prop. 5.6
produced 348. The source-faithful coupling is the `danger` flag: a zero
sibling of a still-centred parent is a Prop. 5.6 leaf; a zero sibling
after a nonzero break is a different local origin and is not
\(\sigma_1=\pi t^{\delta_1}\) in the global chart. That coupling is
exactly 60 rows. Type: DERIVED from Prop. 5.6 + the Lemma 5.3 chart,
not a quoted DP.

If \(P\bmod A>d_j/(n-M_j)\) at \(j=2\) with parent `danger` still true
(always, at \(s=3\), coming off the top chart), every partition contains
a major zero sibling which dies. That is the uniform kill of the
\(D=105\), \(D=117\), \(L=8a+5\), and geometric \(A_2=6\) rays below.

### Worked example: Moh \((n,m)=(75,50)\), printed row

\(n=75\), \(m=50\), \(M=(-50,55,73)\), \(V_3=4\), \(V_2=3\) (or \(2\)).
\(d=(75,25,5,1)\). Windows: \(2.5<4\le 5\) and \(1.25<V_2\le 20\).
\(\delta_3=-1\), \(\delta_2=1/5\). For \(V_2=3\), \(\delta_1=1/2\);
for \(V_2=2\), \(\delta_1=2/3\) (p.202 prints \([1/3]\), unattained).
\(A_2=\operatorname{den}(\delta_2)=5\). At \(j=2\):
\(P=V_3 d_2/d_3=20\), \(Q=V_3(n-M_2)/d_3=16\), threshold \(h=5/4\).
\(P\bmod A=0\): **no forced zero**. Capacity \(16\equiv 1\pmod 5\).

Selected \(V_2=3\not\equiv 0\pmod 5\), so a nonzero orbit. Partitions
containing \(3\):
- \(b=0\), orbits \(\{3,1\}\): only \(u=3\) is major (\(1\le 5/4\)).
- \(b=5\), orbits \(\{3\}\): both \(3\) and the zero \(b=5\) are major.

The second partition's zero sibling, with parent `danger` still true,
is a Prop. 5.6 leaf: reject that partition. The first partition has no
major zero. The selected child \(V_2=3\) has \(A_1=2\) and satisfies
(13): \(A_1\mid m^*V_2=6\) and \(A_1\mid n^*V_2-1=8\). Survives.

Selected \(V_2=2\): valid partitions \(\{2,2\}\) and \(\{2,1,1\}\) with
\(b=0\); partitions with major \(b\in\{5,10\}\) die as above. The
selected (13)-style check holds with \(A_1=3\). Survives.

All other PATH-ARITH rows at \((75,50)\) have \(P\bmod A_2>h\)
(\(M_2\in\{5,10,40,60\}\)). Forced major zero sibling at \(j=2\) dies.
Residue exactly \(\{M_2=55,\,V_2\in\{2,3\}\}\).

### Worked example: Moh \((64,48)\)

\(d=(64,16,4,2)\), \(V_3=3\), \(V_2=3\), \(\delta_2=1/4\), \(\delta_1=9/16\),
\(A_2=4\), \(P=12\), \(Q=9\), \(h=4/3\), \(P\bmod 4=0\). Selected \(V_2=3\le\triangle=3\)
(10). Partition \(b=0\), one orbit \(u=3\). Capacity \(9\equiv 1\pmod 4\).
No major sibling. (12) holds at \(A_1=4\). Survives.

### Excess row killed by the tree, sibling named

Take PATH-ARITH \((75,50,M_2=40,V_3=4,V_2=1)\), which passes (1)–(13)
including (12)/(13). Here \(A_2=9\), \(P=20\), \(Q=28\), \(h=5/7\),
\(P\bmod 9=2>5/7\): **forced major zero of multiplicity \(2\)**.
Selected \(V_2=1\) is a nonzero orbit (embeds, `danger` would clear
along the selected path, and (12)/(13) holds for \(V_2=1\)). Every
admissible partition still contains the zero factor \(b=2\). That
sibling, evaluated in the still-centred top chart, is a Prop. 5.6 leaf
at \(D_1\). The skeleton dies. The killing sibling is the **forced
zero factor of multiplicity \(b=P\bmod A_2=2\)**, not the selected
\(V_2=1\).

The same pattern kills every \(D=105\) and \(D=117\) campaign row
(§8 below).

---

## 5. Answer (d). The ODE step (3.7)

Prop. A.3: \(D(m,n,p,q)=c\,p\) with \(c\ne 0\). **RHS is \(cp\), not \(c\).**
Def. 4.1: \(D(m,n,p,q)=m p q'-n q p'\).

Let \(a\) be a simple \(q\)-root, \(u=\operatorname{mult}_a p\ge 1\),
\(p=(\pi-a)^u p_a\), \(q=(\pi-a)q_a\), \(p_a(a)\ne 0\), \(q_a(a)\ne 0\).
Substitute:
\[
D=(\pi-a)^u\bigl[(m-nu)p_a q_a+(\pi-a)(\cdots)\bigr]=c(\pi-a)^u p_a.
\]
Cancel \((\pi-a)^u\) (uses \(u\ge 1\)) and set \(\pi=a\):
\[
(m-nu)q_a(a)=c.
\]
With charged names \(P=m\), \(Q=n\): \((P-Qu)q_a(a)=c\). Since \(c\ne 0\),
\(P-Qu\ne 0\).

**Hypotheses used:** \(q\) simple at \(a\) (Prop. 4.6(3): \(q\) squarefree,
every \(q\)-root is simple); \(u\ge 1\) (so \(a\) is a \(p\)-root; Prop. 4.6(4)
puts every \(p\)-root among the \(q\)-roots). Both hold at **every**
\(p\)-root, not only major ones.

**Exact, not the strict window restated.** The major window is
\(u>P/Q\). The ODE is \(u\ne P/Q\). For a major root the window already
gives \(P-Qu\ne 0\). The new content is that a **minor** sibling of
multiplicity exactly \(P/Q\) (when that is an integer) is forbidden.
Measured: 60 → 58. The two ODE kills at \(n\le 100\) are

```text
(84, 56, M=(70,77,82), V_2=5, V_3=10, V_4=5)
(96, 72, M=(84,88,94), V_2=3, V_3=9, V_4=3)
```

Type: PROVED-IN-SOURCE as a local identity; DERIVED as a filter on every
combinatorial part of every partition (Moh never writes “scan minor
siblings for \(u=P/Q\)”).

---

## 6. Answer (e). The passport (3.8)

**Not in Moh.** Typed EXTERNAL.

Construction, from the orbit picture and Prop. A.3. On \(z=\pi^A\),
\[
p=\pi^b\prod_\ell(z-c_\ell)^{u_\ell},\qquad
q=\pi\prod_k(z-d_k)
\]
when \(\varepsilon=1\) (forced if \(b\ge 1\); charged passport assumes
\(Q\equiv 1\pmod A\)). Then \(S=(Q-1)/A\) is the number of nonzero
\(q\)-orbits. The cyclic quotient of \(\varphi=p^Q/q^P\) has weights
\[
W_0=\frac{P-Qb}{A},\qquad W_\ell=P-Qu_\ell,
\]
and unused \(q\)-orbits contribute weight \(P\). ODE-degeneracy is
\(W=0\). Let \(g=\gcd(|W_i|)\) and \(d_+=\sum_{W_i>0}W_i\). The reduced
map has degree \(d_+/g\) and at least \(S\) distinguished \(0/\infty\)
slots coming from the \(q\)-orbits. The inequality
\[
\frac{d_+}{g}\ge S
\]
is a degree/passport obstruction of Davenport–Zannier / cyclic-Belyi
type: a primitive rational function cannot have more \(0/\infty\) slots
than its degree. It is **not** a theorem Moh states, and it is not a
formal consequence of Prop. A.3 alone (A.3 does not mention \(A\) or
\(S\)).

It is a correct *shape* of a necessary condition for the cyclic quotient
of \(p^Q/q^P\). Whether this exact packaging is the sharp passport of
the geometric map, or a slightly over-strong combinatorial proxy, is
OPEN as a geometric theorem; as an arithmetic filter it is well-defined
and fail-closed. Measured: 58 → 55. Extra kills:

```text
(84, 56, M=(42,77,82), V_2=1, V_3=12, V_4=6)
(96, 64, M=(48,88,94), V_2=1, V_3=12, V_4=7)
(100, 40, M=(70,95,98), V_2=8, V_3=4, V_4=4)
```

Moh's six survive. Combined with edgewise recenter it leaves the same
20-row set as ODE+recenter (charged §3.1). Type: EXTERNAL. Do not
promote as PROVED-IN-SOURCE. Do not promote as Moh's lost program.

---

## 7. Answer (f). The recentring rule

**What Prop. 5.4 proves.** After a full tower \(D_s\supseteq\cdots\supseteq D_1\)
exists, there is a **unique** index
\(i=\max\{r:V_{r+1}d_r/d_{r+1}>V_r\}\) such that \(D_i\) is the smallest
disc containing all roots of \(g T_1^\psi\). If \(\delta_i>-1\), a
polynomial automorphism of \(k[x,y]\) (or already \(k[x,y]=k[f,g]\))
reduces degrees. The proof (pp.183–185) translates only at that disc:
\(\sigma=h(x)+\pi t^{\delta_i}\), then \(y\mapsto y-h(x)\). For \(i=1\)
it uses the \(r=1\) ODE instead.

**Does the edgewise extrapolation change a quantifier?** **Yes.** The
exploratory rule treats every sibling with integral \(\delta\) (in Moh's
range \(\delta\in(-1,1)\), this is \(\delta=0\)) as still dangerous after
a nonzero label, as if Prop. 5.4's translation were available at that
sibling. That replaces “the globally selected disc \(D_i\)” by “every
integral-radius sibling.” Charged §3.3 states this correctly and types
it OPEN. Measured: 60 → 23 without ODE, 58 → 20 with ODE, 55 → 20 with
passport. Moh's six survive, so it is fail-closed as a probe, not as a
source theorem.

p.190's \(y\mapsto y-ax-b\) reducing \(\sigma_1=at^{-1}+b+\pi t^{\delta_1}\)
to \(\pi t^{-\delta_1}\) is the \(s=2\), \(\delta_2=-1\) special case
used to deduce Prop. 5.5 from Prop. 5.6. It does not license arbitrary
siblings.

Type: OVER-READING if promoted as Prop. 5.4; OPEN[`FULL-TREE-RECENTER`]
as a new axiom. Charged typing of this point is correct.

---

## 8. Answer (g). Independent replay, \(D=105\), \(D=117\), the two rays

### Replay

| source | TREE | ODE | PASSPORT | POLY | POLY+ODE |
|---|---:|---:|---:|---:|---:|
| this lane | 60 | 58 | 55 | 23 | 20 |
| `tree-independent.py` | 60 (`--zero-only`) | (tied to `--passport`) | 55 | 23 (default recenter) | — |
| `full_tree_partition.py` | 60 | 58 | 55 | 23 | 20 |
| `candidate-results.json` | 60/12 | 58/12 | 55/11 | 23/7 | 20/7 |

Row-keys of `C_FULL_TREE`: this lane \(=\) `tree-independent.py --zero-only`
\(=\) `FT.full_tree_ok`, disagree \(=0/658\). Frozen
`candidate-results.json` SHA
`01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2`
records the same 60/58/55/23/20 and the \((75,50)\) residue
\(\{M_2=55,\,V_2\in\{2,3\}\}\). `C_ZERO_PATH` (canonical \(b=P\bmod A\)
followed while major) is 153/15, matching the json.

The 12 `C_FULL_TREE` classes:
\((64,48)\), \((72,48)\), \((75,50)\), \((80,32)\), \((84,56)\),
\((90,60)\), \((96,64)\), \((96,72)\), \((96,80)\), \((99,66)\),
\((100,40)\), \((100,80)\). Forty groups. All six printed rows sit in
the first, third, fifth, and tenth classes.

Charged “recentring → 20” is the **POLY+ODE** (or POLY+PASSPORT) count.
Bare POLY is 23. Report both.

`candidate_eval.py` was not re-executed over \(48\le D\le 200\) (79s in
the frozen json). The \(n\le 100\) half was re-executed via its imported
`full_tree_partition.py`. Campaign \(D\le 200\) group counts 1516 (tree)
and 1261 (passport) are accepted as frozen MEASURED, matching charged
§4.5; this lane independently confirmed the emptiness of \(D=105\) and
\(D=117\) under the same predicates.

### \(D=105\) (the “trio” and the rest)

Campaign \(K_{\min}=16\): 15 PATH-ARITH rows, 4 values of \(m\in\{42,63,70,84\}\),
14 groups. Bounded-\(N\in[6,16]\) slice: 3 groups (charged “trio”).
**Every one dies under bare `C_FULL_TREE`.** Uniform mechanism: at
\(j=2\), \(P\bmod A_2>h=d_2/(n-M_2)\), so a major zero sibling is
forced; parent `danger` is still true from the Lemma 5.3 top chart;
Prop. 5.6 kills that sibling. Selected \(V_2\) often itself embeds and
even satisfies (12)/(13); the **sibling** kills the row.

Named examples:

| \(m\) | \(M_2\) | \(V_2,V_3\) | \(A_2\) | \(P\) | \(b_{\min}\) | \(h\) | killing sibling |
|---:|---:|---|---:|---:|---:|---|---|
| 42 | 49 | 2, 5 | 13 | 15 | 2 | \(3/8\) | zero \(b=2\) (selected *is* this zero; `danger` stays) |
| 63 | 28 | 5, 6 | 13 | 18 | 5 | \(3/11\) | zero \(b=5\) |
| 70 | 28 | 1, 5 | 18 | 25 | 7 | \(5/11\) | zero \(b=7\) (this is Sol \(L=5\)) |
| 70 | 10 | 1, 4 | 25 | 28 | 3 | \(7/19\) | zero \(b=3\) |
| 84 | 28 | 1, 6 | 13 | 18 | 5 | \(3/11\) | zero \(b=5\) (selected is nonzero \(V_2=1\)) |

The \(L=5\) member is the \(a=0\) Sol ray. Verdict: **KILL / C_FULL_TREE**,
typed DERIVED application of Prop. 5.6 to a forced major zero sibling.

### \(D=117\)

Seven PATH-ARITH rows, all \(m=78\), all `C_FULL_TREE` empty. Same
mechanism. The geometric \(A_2=6\) member is
\(M_2=52\), \(V_3=11\), \(V_2=1\): \(P=33\), \(b_{\min}=3>h=3/5\),
killing sibling zero \(b=3\) (selected is nonzero). Other rows:
\(b_{\min}\in\{3,11,2,8,5,3\}\), all major except the last printed
\(V_2=17\) row, which still carries a major zero \(b=17\) as the
selected (11)-factor and dies as a Prop. 5.6 leaf. Verdict: **KILL**.

### \(A_2=6\) ray \(n=9(7t+6)\), \(t=0..3\)

Geometric members (the \((2,3)\)-type packets with \(A_2=6\), \(V_2=1\),
\(V_3=6t+5\), \(h=3/5\), \(b_{\min}=3>3/5\)):

| \(t\) | \(n\) | \((m,M_2,V_3,V_2)\) | TREE |
|---:|---:|---|---|
| 0 | 54 | \((36,24,5,1)\) | KILL, zero \(b=3\) |
| 1 | 117 | \((78,52,11,1)\) | KILL, zero \(b=3\) |
| 2 | 180 | \((120,80,17,1)\) | KILL, zero \(b=3\) |
| 3 | 243 | \((162,108,23,1)\) | KILL, zero \(b=3\) |

**The sourced tree kills the ray.** (At \(n=180\) there exist *other*
\(A_2=6\) skeletons, not members of this geometric family, of which 9
survive `C_FULL_TREE`. Those are not the ray the question named.)

### Sol's \(L=8a+5\) ray, \(a=0..3\)

Skeleton: \(n=21L\), \(m=14L\), \(M_2=7(3L+1)/4\), \(M_3=n-2\),
\(V_2=1\), \(V_3=5\). All four pass PATH-ARITH(1–13). All four have
\(P\bmod A_2>h\):

| \(a\) | \(L\) | \(n\) | \(A_2\) | \(P\) | \(b_{\min}\) | \(h\) | TREE |
|---:|---:|---:|---:|---:|---:|---|---|
| 0 | 5 | 105 | 18 | 25 | 7 | \(5/11\) | KILL |
| 1 | 13 | 273 | 48 | 65 | 17 | \(13/29\) | KILL |
| 2 | 21 | 441 | 78 | 105 | 27 | \(21/47\) | KILL |
| 3 | 29 | 609 | 108 | 145 | 37 | \(29/65\) | KILL |

**The sourced tree kills the ray**, already at \(a=0\) (which is a
\(D=105\) campaign row). Pattern in \(a\): \(b_{\min}=10a+7\),
\(h=(8a+5)/(16a+11)\), always \(b_{\min}>h\). This is a uniform
DERIVED kill, not four coincidences. It does **not** by itself give a
source-proved emptiness of Jacobian pairs along the ray: it empties the
PATH-ARITH model after the derived screen.

---

## 9. Typed block

```text
COMPONENT                         TYPE
--------------------------------  ------------------------------------------
Prop.5.3 local extension of ANY   PROVED-IN-SOURCE
  above-threshold factor
p.200 Thm (4) for every E_i       PROVED-IN-SOURCE
  meeting the count
"every sibling extends" as        PROVED-IN-SOURCE (quoted at p.200(4);
  Moh's statement                   also a consequence of the 5.3 proof)
C_FULL_TREE finite DP             DERIVED (orbit fill + Lemma 5.3 top
  (danger, knapsack, (12)/(13))     chart + Prop.5.6 on a still-centred
                                    zero leaf). Not a Moh theorem.
                                    Not sufficiency for (f,g).
C_ZERO_PATH (forced b=P mod A)    DERIVED projection of Prop.5.6;
                                    PROVED-IN-SOURCE as the typed
                                    all-zero leaf, not as "reject (11)"
(3.3) P = b + A Σ u_ℓ, b ≡ P mod A  DERIVED from p.201 Galois + (9)(11)
nonzero orbit size = A_j          DERIVED from p.201 (yes)
A_j | Q_j-1 as Lemma 5.2          OVER-READING (wrong lemma). Content
                                    is DERIVED Galois capacity; automatic
                                    on all 658 PATH-ARITH rows
several fixed q-roots             OVER-READING. Unique fixed point 0.
unused q-slots allowed            DERIVED, yes (p.200(6) bound)
child Q determined by u           DERIVED, yes (next-level Prop.4.6)
δ, A recomputed per branch        PROVED-IN-SOURCE Def.5.1(3), p.201(8)
DP state (level, multiplicity)    OVER-READING if claimed sufficient
  sufficient                        for s≥4; both working codes store
                                    the higher V-tuple
(3.7) (P-Qu) q_a(a)=c, P-Qu ≠ 0   PROVED-IN-SOURCE local identity
                                    (A.3 RHS = cp, not c). DERIVED as
                                    a scan of minor siblings. Exact,
                                    not the strict window.
(3.8) d_{+}/g ≥ S                 EXTERNAL (cyclic quotient of p^Q/q^P;
                                    Davenport–Zannier type). Necessary
                                    in shape; packaging not in Moh.
Prop.5.4 polynomial translation   PROVED-IN-SOURCE at the globally
                                    selected D_i only
edgewise recenter at every        OVER-READING / OPEN[FULL-TREE-RECENTER]
  integral-δ sibling                (changes a quantifier)
C_FULL_TREE 658→60, keeps six,    MEASURED, three-way row-for-row
  (75,50) residue {55}×{2,3}        agreement
ODE 60→58, passport 58→55,        MEASURED
  POLY 60→23, POLY+ODE 58→20
D=105, D=117 empty under TREE     MEASURED for PATH-ARITH after the
                                    derived screen. Not a source-proved
                                    emptiness of pairs.
A2=6 ray t=0..3 geometric members KILL / DERIVED (forced b=3)
L=8a+5 ray a=0..3                 KILL / DERIVED (forced b=10a+7)
OPEN[MOH-PROGRAM] closed?         NO. Residual 49 excess rows after
                                    C_FULL_TREE_PASSPORT.
```

---

## 10. Promotion recommendation

**Promote, with the type repairs above:**

1. The local whole-major-tree obligation (Prop. 5.3 + p.200(4)): every
   above-threshold factor extends. Campaign may treat this as a
   source-backed necessary condition on any claimed characteristic
   tower, not as a sufficiency theorem.
2. The finite screen `C_FULL_TREE` as a **named derived necessary
   filter** on PATH-ARITH, fail-closed on Moh's six, uniform in \(D\),
   already the exact \((75,50)\) discriminator. Frontier movement:
   \(D=105\) and \(D=117\) become empty *after this filter*; the
   baseline “\(D=105\) has three bounded-\(N\) groups” is baseline-only.
3. ODE (3.7) as a local A.3 identity, applied to every \(p\)-root
   including minor siblings. Two extra kills at \(n\le 100\), both
   fail-closed.
4. The Lemma 5.2 correction: do not cite it for \(A\mid Q-1\).

**Do not promote:**

- `C_FULL_TREE` as PROVED-IN-SOURCE in the same breath as Prop. 5.3.
  The DP (top-zero danger, generic fill) is DERIVED.
- `C_FULL_TREE` or `C_FULL_TREE_PASSPORT` as Moh's lost CDC program,
  or as a discriminator of the p.202 table (49 excess remain).
- (3.8) as a Moh theorem. Keep EXTERNAL.
- Edgewise recenter as Prop. 5.4. Keep OPEN.
- Emptiness of Jacobian pairs at \(D=105\), \(D=117\), or along the
  two rays. Those are PATH-ARITH emptiness after a derived screen.
- DP state \(({\rm level},u)\) as sufficient without the higher
  \(V\)-tuple.

The campaign may move its frontier onto `C_FULL_TREE` as a **necessary
PATH-ARITH filter**, and onto `C_FULL_TREE_ODE` as a cheap exact
sharpening. It should **not** move the frontier onto passport or
recenter without keeping their types. It should **not** declare
`OPEN[MOH-PROGRAM]` closed.

---

## 11. OPENs, bounded quantity, cheapest test

### `OPEN[MOH-PROGRAM-ARTIFACT]` (pre-existing; not closed)

Residual after the strongest source-derived screen
(`C_FULL_TREE_PASSPORT`): **49 excess rows / 7 new \((n,m)\) classes**
at \(n\le 100\), occupying
\((72,48)\), \((80,32)\), \((84,56)\) (also printed), \((90,60)\),
\((96,64)\), \((96,72)\), \((96,80)\), \((100,80)\).
Cheapest test: none at desk scale. Closing requires the CDC listing or
an independent period reconstruction of Moh's output. Do not fill by
cap or analogy.

### `OPEN[FULL-TREE-RECENTER]` (charged; confirmed)

Quantifier change in Prop. 5.4. Bounded effect at \(n\le 100\): 55 → 20
rows (passport on), 35 extra kills, Moh's six kept. Cheapest test
already done: the Prop. 5.4 proof uses the unique \(\pi\)-root in the
globally selected \(D_i\) (pp.183–185) and does not mention siblings.
To *close* as a theorem one would need a source sentence applying the
translation at every major disc with integral \(\delta\), or a geometric
argument that the automorphism of \(k[x,y]\) at \(D_i\) induces the
same centring on every sibling chart. Neither is on the page. Desk
status: remains OPEN. Do not promote.

### `OPEN[PASSPORT-SHARPNESS]` (new; bounded)

Whether \(d_+/g\ge S\) with the charged weights is the geometric
passport of the cyclic quotient, or a combinatorial over-packaging.
Bounded effect: 3 rows at \(n\le 100\) (listed in §6). Cheapest test:
search small \((P,Q,A)\) for polynomials \(p,q\) satisfying
\(D(P,Q,p,q)=cp\), Galois symmetry of order \(A\), squarefree \(q\),
p-roots \(\subset\) q-roots, and a partition violating (3.8). If a
witness exists, (3.8) is over-strong and those 3 kills are retracted.
If none exists up to a declared bound (say \(P\le 40\), \(A\le 12\)),
the inequality stays EXTERNAL-necessary in that range. Desk: one-core
enumeration of A.3 solutions, well under 20 min / 4 GB.

### `OPEN[SIBLING-COEFFICIENTS]` (charged residual; confirmed)

The tree constrains multiplicities and radii, not the simultaneous
existence of polynomials \(p_j,q_j\) at every sibling with a common
coefficient field and matching leading terms. Cheapest test: for one
excess `C_FULL_TREE` survivor (e.g. a \((90,60)\) row), try to realise
the sibling \(p,q\) over \(k[\pi]\) with the A.3 ODE at two adjacent
nodes. Failure is not a source theorem; success does not close
`OPEN[MOH-PROGRAM]`.

No `charge_basis` line: this report asserts no new exit price.

---

## 12. Controls and honesty box

- SHA-256 gate: 10/10 match.
- Image-first transcription: yes, before charged §3.
- First recursion ran before `tree-independent.py` was read. First
  counts were 20 (over-kill zeros at \(D_1\)) and 348 (no Prop. 5.6).
  The 60 required the Lemma 5.3 top-chart `danger` flag, which is
  source-justified and independently implemented.
- Three-way row-for-row agreement on 60/58/55/23/20: this lane,
  `tree-independent.py`, `full_tree_partition.py`.
- Moh's six kept on every screen here. Fail-closed.
- PATH-ARITH vs pairs: never identified.
- `FALLACY-v2`: no cv-flag/place/series identification; no
  floor-as-attainment; no `sat()`; no exit-price.

Desk: all \(n\le 100\) screens \(<3\)s one core; \(D=105,117\) and both
rays \(<10\)s; peak RAM well under 4 GB.

<!-- BODY-END -->
