# Hostile primary-source audit — Pinchuk quasi-polynomial reduction

**Overall verdict: `LOCAL IDENTITIES CONFIRMED / THEOREM 3.4 SKETCHED WITH
TERMINATION GAP / NOT A GLOBAL JC2 REDUCTION`.**

S. I. Pinchuk, *Quasi-polynomial mappings with constant Jacobian*, Izv.
Math. 85:3 (2021), 506–517 (Russian original Izv. RAN Ser. Mat. 85:3
(2021), 178–190), DOI `10.1070/IM9017`, does **not** prove JC2, does **not**
produce a polynomial Keller normal form, and does **not** transport a
hypothetical plane Keller pair into the campaign's Sigray books. Theorem 4.1
is an elementary identity, confirmed below under stated leading-coefficient
hypotheses, and it is the only load-bearing Pinchuk arrow that touches the
maximum-12 spectral bound of 16. Theorem 3.4 is a source-side reduction to a
*q*-polynomial whose leading weighted Jacobian is claimed constant; the six
local cases of Lemma 3.6 are algebraically checkable, but the sentence that
“the rest … is similar” supplies an incomplete well-founded measure and does
not prove that the only terminal state is a nonzero constant leading
Jacobian.

This is a validity audit of the 2021 quasi-polynomial paper. It is not a
priority claim, not a JC2 resolution, and not about the 1994 real Pinchuk
maps (Avenue 24).

Basis at review: `7832fb73ac887041968f9cec2dc6cba7aa0d0bcf`. Packet
inspected: `xmodel/ideation-20260824T1820Z-packet.md`. No ideation
submission or synthesis from round `20260824T1820Z` was read.

## Sources actually read

Primary:

- Landing page `https://www.mathnet.ru/eng/im9017` (abstract, MSC 14R15 /
  13R20, bibliography of 15 items).
- Complete Russian HTML full text
  `https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=im&paperid=9017&option_lang=rus`
  (MathNet “полный текст в HTML”; original language of the paper). All
  numbered definitions, lemmas, theorems, displayed formulae (1.1)–(4.3),
  the six cases of Lemma 3.6, and the remainder paragraph of Theorem 3.4
  were read from this text, not from snippets.
- Requested English PDF
  `https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=9017&what=fullteng`
  302s to `/links/.../im9017_eng.pdf` (declared 466 kB). A browser-UA fetch
  returned a valid `%PDF-1.5` header but stalled at 46074 bytes / ~455 kB
  with no `startxref`/`%%EOF`. The English translation uses the same theorem
  numbers as the Russian original. Citations below use English page range
  506–517 together with the Russian HTML theorem labels, which match.

Load-bearing imports, read in full or in the theorems actually used:

- F. Pakovich, A. K. Zvonkin, *Minimum degree of the difference of two
  polynomials over \(\mathbb{Q}\), and weighted plane trees*, arXiv:1306.4141
  (Selecta Math. (N.S.) 20:4 (2014), 1003–1065). PDF SHA not recorded;
  theorems 3.1, 3.3, 4.1, 5.4 and Definitions 1.1, 5.2 were read from the
  arXiv PDF (54 pages).
- C. Valqui, J. A. Guccione, J. J. Guccione, *On the shape of possible
  counterexamples to the Jacobian conjecture*, J. Algebra 471 (2017), 13–74,
  arXiv:1401.1784. Abstract and the Newton-polygon/shape claims used for
  Theorem 1.3 provenance. Secondary navigation only for Moh, Heitmann,
  Abhyankar, Makar-Limanov, Formanek, Joseph, Dixmier.

Independent algebra (scratch, outside the bank): `/tmp/pinchuk-venv` sympy
checks of (2.2), Theorem 4.1, the Stothers pair (3.2), the displayed (3.3),
the spectral \(W\)-norm, and \(J(f,W)\).

## Per-claim verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Definitions and fidelity of the three equivalences | `CONFIRMED as written / OVERREADING REFUTED` |
| 2 | Imported polynomial normal form, Theorem 1.3 | `GAP (cited, not proved here); scope is standard Newton-shape, not a new engine` |
| 3 | Theorem 3.4 reduction to reduced *q*-form | `GAP at the published scope; six local cases CONFIRMED as inequalities; remainder measure incomplete` |
| 4 | Theorem 4.1 three-way identity | `CONFIRMED` under matched leading coefficients; unrestricted statement has a smallest countermodel |
| 5 | “Complete classification” citation of Pakovich–Zvonkin 2014 | `OVERREAD`; unitrees classified, not all complex equality pairs |
| 6 | Maximum-12 elimination identity and abc bound 16 | `CONFIRMED` as algebra and as the numerical bound; source supplies no \(\mathbb{C}(x)\) rigidity |
| 7 | Campaign impact | Local identity usable on the \((9,12)\) \(k=0\) spectral face; Theorem 3.4 is not a global JC2 reduction; quarantine Avenue 24 |

---

## 1. Definitions and fidelity

**Verdict: `CONFIRMED as written / OVERREADING REFUTED`.**

Notation in the paper: \(\phi\sim\psi\) means \(\phi=c\psi\) for some
\(c\in\mathbb{C}^*\). A plane polynomial map \(F=(f,g)\) is Keller when
\(J(f,g)\sim 1\).

### Polynomial equivalence (Definition 1.1)

Elementary polynomial automorphisms are

```text
(x,y) |-> (x, y + a x^m),     (x,y) |-> (x + b y^n, y),
```

\(a,b\in\mathbb{C}\), \(m,n\in\mathbb{N}\). Two polynomial maps are
equivalent when one is obtained from the other by composing on the **source**
with a finite product of these (and, implicitly, linear changes used in
§1). Jung–van der Kulk is invoked only as the known generation of
\(\mathrm{Aut}(\mathbb{C}^2)\), not proved.

Preserved in both directions along this relation:

- polynomiality;
- \(J\sim 1\) (each elementary has Jacobian 1);
- polynomial invertibility and noninvertibility;
- recovery of a polynomial inverse: if \(G=F\circ\Phi\) with \(\Phi\) a
  polynomial automorphism, then \(G^{-1}=\Phi^{-1}\circ F^{-1}\).

### *q*-polynomials (Definition 2.1)

\(f=\sum_l a_l(x)\,y^l\) is a *q*-polynomial when each coefficient \(a_l\)
is a finite sum of monomials \(a_{kl}x^k\) with **rational** (possibly
negative) exponents \(k\). The paper treats these as holomorphic on the
slit half-plane \(\{x>0\}\times\mathbb{C}\), with \(x^k\) the positive real
branch. Weighted leading forms, Newton polygons in \(\mathbb{Q}\times\mathbb{N}_0\),
and \(J\) are defined on that domain.

### *q*-equivalence (Definition 3.1)

A *q*-elementary automorphism is

```text
(x,y) |-> (x, y + c x^μ),    c ∈ C,  μ ∈ Q.
```

\(F\) and \(G\) are *q*-equivalent when \(G=F\circ\Phi_1\circ\cdots\circ\Phi_s\)
with each \(\Phi_i\) *q*-elementary.

Preserved:

- \(J\sim 1\);
- the *q*-polynomial class;
- invertibility as holomorphic maps of the slit half-plane (each \(\Phi_i\)
  is invertible there, inverse \((x,y)\mapsto(x,y-c x^\mu)\)).

Not preserved:

- polynomiality, as soon as some \(\mu\notin\mathbb{N}\cup\{0\}\);
- existence of a polynomial inverse;
- the ambient ring \(\mathbb{C}[x,y]\).

### “A polynomial map is equivalent to a *q*-map” (Definition 3.2)

There exists a polynomial map \(H\) that is polynomially equivalent to \(F\)
and *q*-equivalent to \(G\). So \(G=F\circ\Phi_{\mathrm{poly}}\circ\Phi_{q}\).
The output \(G\) is in general only a *q*-polynomial. Constant Jacobian is
preserved. Polynomiality of \(G\) is not. Noninvertibility of \(F\) as a
polynomial map does imply that \(G\) is not bijective as a holomorphic map
of the slit plane, because the \(\Phi\)'s are bijective there; in particular
\(G\) has no polynomial inverse.

### Reduced form (Definition 3.3)

A *q*-map \(F=(f,g)\) is in reduced form if there are weights
\(w=(-1/m,1)\) with \(m>1\) such that \(J(f_w,g_w)\sim 1\).

### Smallest countermodel to the overreading

Overreading: “*q*-equivalence preserves polynomial invertibility, or an
inverse of the reduced *q*-map yields a polynomial inverse of the original
Keller pair.”

Countermodel: \(F=(x,y)\) (polynomial automorphism) and
\(\Phi=(x,\,y+x^{-1})\). Then \(G=F\circ\Phi=(x,\,y+x^{-1})\) is
*q*-equivalent to \(F\), has Jacobian 1, and is invertible on \(\{x>0\}\)
with inverse \((x,\,y-x^{-1})\), which is not polynomial. The same \(\Phi\)
may be applied to a hypothetical noninvertible Keller polynomial \(F\);
source composition with \(\Phi\) never manufactures a polynomial inverse.

Theorem 3.4’s last sentence, “invertibility of \(G\) implies invertibility of
\(F\)”, is correct as a statement about maps of the slit plane (the
\(\Phi_i\) are invertible). It does **not** recover a polynomial inverse of
\(F\) from a *q*-inverse of \(G\), unless every \(\mu\) used is a
nonnegative integer.

---

## 2. Imported polynomial normal form (Theorem 1.3)

**Verdict: `GAP` as a theorem proved in this paper; the cited package covers
an arbitrary hypothetical noninvertible plane Keller map after polynomial
elementary changes, at the standard Newton-shape granularity, not as a new
reduction engine.**

Theorem 1.3 (English pp. 507–508 / Russian HTML §1) states: if
\(G:\mathbb{C}^2\to\mathbb{C}^2\) is polynomial with \(J(G)\sim 1\) and \(G\)
is **not** invertible, then \(G\) is polynomially equivalent to some
\(F=(f,g)\) with

- (a) \(\deg f\) and \(\deg g\) do not divide one another;
- (b) \(N(f)\) and \(N(g)\) are homothetic,
  \(N(f)=(\deg f/\deg g)\,N(g)\);
- (c) if \(w_1>0\) and \(w_2>0\), then \(f_w\) is degenerate: \(N(f)\) has
  **no side in the open first quadrant**, and lies in a rectangle
  \(0\le k\le K\), \(0\le l\le L\) with \((K,L)\in N(f)\) and \(K\ge L\).

What is proved in the paper: nothing. The paragraph before Theorem 1.3
assigns the statement to the literature, especially Abhyankar [1] and
[2]–[8] (Bass–Connell–Wright, van den Essen, Formanek, Valqui–Guccione–
Guccione, Makar-Limanov’s two MPIM preprints, Moh). Proposition 1.2 (the
classification of \(w\)-homogeneous solutions of \(J(u,v)\sim u^\alpha\) for
\(w_1>0\), \(w_2>0\)) is likewise stated with the proof omitted.

What the cited shape literature actually gives, at the level needed here:

- Valqui–Guccione–Guccione, J. Algebra 471 (2017), 13–74 (arXiv:1401.1784):
  Newton polygons of a hypothetical counterexample, after passing to a
  standard minimal pair, have no interior first-quadrant sides, are
  homothetic, and the degree-gcd is at least 16. This is the modern
  packaging of Abhyankar’s expansion geometry plus Heitmann.
- Moh, J. Reine Angew. Math. 340 (1983), 140–212: configuration of roots
  and degree constraints.
- Makar-Limanov MPIM 2013-53 / 2014-30: Newton polygon / polytope of a
  Jacobian mate.

Does this cover an arbitrary hypothetical noninvertible plane Keller map
after legitimate **polynomial** changes? Yes, at that granularity: any such
map is polynomially equivalent to one whose Newton polygons satisfy (a)–(c).
The campaign’s GGV corner calculus (Avenue 1) is a finer descendant of the
same package; Pinchuk 1.3 is not finer than GGV, and it is not a substitute
for `G2-PSC`.

It does **not** cover the map after the *q*-elementary changes of §3: those
exit \(\mathbb{C}[x,y]\). Theorem 1.3 is a polynomial-category input to
Theorem 3.4, not a conclusion about the reduced *q*-form.

Proposition 1.2 is used later to justify that, for **polynomial** maps, a
positive-weight leading Jacobian \(J(f_w,g_w)\sim 1\) forces invertibility.
That arrow is not proved in the paper. Smallest overreading: treating 1.2/1.3
as internally established lemmas of Pinchuk 2021.

---

## 3. Theorem 3.4

**Verdict: `GAP` at the strongest exact scope the paper claims
(“any noninvertible plane Keller polynomial map is equivalent, in the sense
of Definitions 3.1–3.2, to a *q*-map in reduced form”). Local inequalities
in Lemma 3.6 cases 1–6: `CONFIRMED`. Production of \(J(f_w,g_w)\sim 1\) by
the remainder walk: `GAP`. No countermodel refuting the statement was
found; the proof as printed is not well-founded.**

### Statement

Any noninvertible polynomial \(F=(f,g):\mathbb{C}^2\to\mathbb{C}^2\) with
\(J(f,g)\sim 1\) is equivalent (Definition 3.2) to a *q*-polynomial map
\(G\) in reduced form (Definition 3.3). Invertibility of \(G\) implies
invertibility of \(F\).

The proof is entirely in Russian HTML §3 (English ~pp. 512–514). It uses
*q*-elementaries (3.1) only, and claims the Newton polygon of \(f\) can be
cut until some adjacent side with weights \(w=(-1/m,1)\), \(m>1\), has
\(J(f_w,g_w)\sim 1\).

### Input from earlier lemmas

- Lemma 2.2: for \(w\)-homogeneous *q*-forms \(u=x^k y^l p(t)\),
  \(v=x^r y^s q(t)\), \(t=x^m y^n\),

  ```text
  J(u,v) = [(ks-lr)pq + (ms-nr) t p'q - (lm-kn) t p q']
           * x^{k+r-1} y^{l+s-1}.
  ```

  Independently confirmed (sympy, several \((k,r,m)\)).
- Lemma 2.3: if that Jacobian vanishes then \(f^{\deg g}\sim g^{\deg f}\)
  and both leading forms are powers of one *q*-polynomial \(u\).
- Proposition 2.4: existence of some \(v\) with \(J(u,v)\sim u^\alpha\),
  \(\alpha>0\), by a \(\delta\)-descent
  \(\delta(a,b)=\mathrm{wt}(ab)-\mathrm{wt}(xy)-\mathrm{wt}(J(a,b))\).
  On a fixed weight lattice \((1/N)\mathbb{Z}\) with finite Newton support,
  \(\delta\) takes finitely many nonnegative values, so the descent
  terminates. Over unstructured \(\mathbb{Q}\) it would not; the paper does
  not say this, but finite support saves it.
- Lemmas 2.5–2.8: reduction to Abhyankar’s equation \(J(u,v)\sim u\)
  (i.e. \(\alpha=1\), \(r=s=1\)) when \(ks-lr\neq 0\) and \(ml-nk>0\), plus
  root-multiplicity lower bounds. The degree identities

  ```text
  (i)  k-l + deg p - l deg q = 0          (m=1,n=0)  =>  deg p > l deg q
  (ii) k-l+(m-1)deg p - (ml-k)deg q = 0   (m>1,n=1) =>  deg p > (ml-k)/(m-1)
  ```

  are confirmed. Combined with “every root of \(p\) is a root of \(q\)”
  (valuation of (2.7) at a root of \(p\) not a root of \(q\) is
  \(\mu-1<\mu\)), some single root of \(p\) has multiplicity strictly above
  the displayed threshold. Confirmed.

### Lemma 3.5

\(N(f)\cap\{k<l\}\neq\varnothing\). Proof: otherwise the same holds for
\(N(g)\), and the “extreme” terms would make \(J\) nonconstant. This is
one sentence. It uses noninvertibility (an invertible leading form
supported on \(k\ge l\) can have \(J\sim 1\), e.g. \((x,y)\)). After
Theorem 1.3(c) has already killed first-quadrant sides, the extreme terms
cannot be a linear automorphism. The lemma is plausible in that setting and
is not independently proved. `GAP` as a stand-alone lemma; not used as a
refutation.

### Lemma 3.6: \(K>L\), six cases

Start from Theorem 1.3(c): \(N(f)\) in a rectangle with top-right vertex
\((K,L)\), \(K\ge L\). Let \(S_1=[(K_1,L_1),(K,L)]\) be the side adjacent to
\((K,L)\) “from the left / below”. Lemma 3.5 forces the supporting weight
to satisfy \(w_1\le 0\), \(w_2=1\). Write \(f_w\sim u^\mu\),
\(u=x^k y^l p(t)\).

**Case 1.** \(L_1=L\), \(w_1=0\), so \(S_1\) is horizontal,
\(0<K_1<K\), \(t=x\). Then \(k>0\), so Lemmas 2.7, 2.5 and 2.6(i) give a
root of \(p\) of multiplicity \(>l\), hence \(\deg p>l\). If one had
\(K=L\), then \(\deg p=l-k<l\) (using \(k>0\)), contradiction. Thus
\(K>L\). The paper’s wording “\(K>K_1>L\)” is slightly too strong:
\(K_1>L\) can fail when the horizontal side crosses the diagonal. The
lemma only needs \(K>L\). No transformation. Confirmed as \(K>L\).

**Case 2.** \(L_1=L\), \(K_1=0\), \(p\) has at least two distinct roots.
Translate \(x\mapsto x+x_0\) for a root \(x_0\) of \(p\). Polynomial. The
case reduces. Confirmed.

**Case 3.** \(L_1=L\), \(K_1=0\), \(p\sim(x-x_0)^d\). Translate
\(x\mapsto x+x_0\). A new left side \(S_0\) appears, and the adjacent side
at \((K,L)\) now has \(K_1<K\), \(L_1<L\). Polynomial. Confirmed as a
polygon change.

**Case 4.** \(0<L_1<L\). Lemma 3.5 gives \(K_1<L_1\), so \(k<l\), and
\(u=x^k y^l p(x^m y)\) with \(m>1\). Lemmas 2.8 and 2.6(ii) produce a root
\(t_0\) of multiplicity \(d>(ml-k)/(m-1)\). The *q*-shear
\((x,y)\mapsto(x,\,y+t_0 x^{-m})\) sends the leading form to a component
whose most negative \(x\)-exponent term is a constant times
\(x^{k+m(d-l)} y^d\). The inequality

```text
k + m(d-l) - d = (k - ml) + d(m-1) > (k-ml) + (ml-k) = 0
```

is an identity given 2.6(ii). So the new vertex has first coordinate
strictly larger than the second. The paper writes “hence \(K>L\)”,
identifying this new local vertex of the transformed leading form with the
global bounding-box corner of \(N(f)\). After a negative-power shear the
whole Newton polygon is rewritten in \(\mathbb{Q}\times\mathbb{N}_0\). The
inequality for the transformed leading vertex is confirmed; the
identification with the original \((K,L)\) is a sketch. The map is no
longer polynomial. Confirmed as a *q*-statement, not as a polynomial
Newton-polygon statement.

**Case 5.** \(L_1=0\) and \(p\) has at least two distinct roots. One shear
makes \(L_1>0\), then Case 4. Confirmed as a reduction.

**Case 6.** \(L_1=0\) and \(p\sim(t-t_0)^d\). The shear produces a new
left side \(S_0\), and \((K,L)\) becomes the right endpoint of a new side
with \(t=x^{m_1} y\), \(1<m_1<m\). The paper takes \(m-m_1\) as a
termination measure, and argues: if all exponents of the current
*q*-polynomial lie in \((1/N)\mathbb{Z}\), then \(m\in(1/N)\mathbb{Z}\),
the shear does not enlarge the denominator, and \(m-m_1\ge 1/N\). After
finitely many Case-6 steps one falls into Case 4 or 5. This is the only
explicit well-founded measure in Lemma 3.6. Confirmed on a fixed
denominator \(N\).

Smallest attempted countermodels:

- Horizontal side with \(K=L\): killed by the degree contradiction in Case 1,
  not a countermodel.
- Square-free \(p\) of large degree in Case 4: 2.6(ii) still produces some
  root with \(d>(ml-k)/(m-1)\), because \(\deg p/\deg q\) strictly exceeds
  that threshold. Not a countermodel.
- Denominator growth under Case 6: the paper’s lattice argument blocks it
  if one starts from a polynomial (\(N=1\)) or from a *q*-polynomial of
  already finite denominator. Not a countermodel.

### The remainder: “the rest of the proof of Theorem 3.4 is similar”

Quoted from the Russian HTML immediately after Lemma 3.6 (English ~p. 514):

> Consider the side \(S_1=[(K_1,L_1),(K,L)]\) adjacent to \((K,L)\) as the
> left-lower side of that vertex, with \(K_1<K\), \(L_1\le L\). Repeat
> cases 1–6 of Lemma 3.6 if needed until \(K_1>L_1\). Let \(w\) be the
> weights of the next side \(S_2=[(K_2,L_2),(K_1,L_1)]\). By Lemma 3.5,
> \(-1<w_1<0\), \(w_2=1\). If \(J(f_w,g_w)\sim 1\), we are done. If
> \(J(f_w,g_w)=0\), continue in this way along sides
> \(S_n=[(K_n,L_n),(K_{n-1},L_{n-1})]\), \(n=2,3,\dots\), with
> \(K_n>L_n\) and \(L_n<L_{n-1}\). This cannot continue indefinitely,
> because every \(L_n\) is a nonnegative integer. The process of cutting
> corners stops only when \(J(f_w,g_w)\sim 1\) for some \(n\). Theorem 3.4
> is proved.

Three gaps, in strengthening order.

1. **The measure does not include Case 6.** The walk claims \(L_n\) is a
   strictly decreasing sequence of nonnegative integers. Case 6 decreases
   \(m\), not \(L\), and after the shear the vertex \((K,L)\) moves onto a
   new side whose \(L\)-coordinate need not drop. Nested Case-6 steps
   inside the walk are not given a combined measure
   \((L_n,\,m-m_1,\,N)\).
2. **“Stops only when \(J_w\sim 1\)” is an assertion, not an exclusion of
   other terminals.** Possible other terminals: \(L_n=0\) with no remaining
   side of the stated shape; collapse of \(\{k<l\}\) (Lemma 3.5 after
   *q*-changes is not re-proved); the map becoming invertible as a
   *q*-map, which the paper would count as a win for \(F\) but does not
   analyse. The Jacobian-weight heuristic (a constant \(J\sim 1\) must
   appear as some face Jacobian) is never written down, and after
   *q*-shears the face decomposition of \(J\) changes.
3. **Adjacent-side preservation is not tracked.** Each shear rewrites the
   whole polygon. The paper never proves that the “next” side \(S_n\) of
   the transformed polygon is the transform of the old next side, nor that
   a side already known to have \(J_w\sim 1\) survives subsequent cuts on
   other sides.

A remark after the proof notes that a reduced *q*-map may be further
changed by \((x,y)\mapsto(x^\mu, x^{1-\mu} y)\) to a form depending only on
\(x\), and that composing on the left with a polynomial Keller map
decreases \(m\). That remark is not part of the proof of 3.4, and the
descent on \(m\) under left composition is not shown to reach \(m\le 1\).

The displayed example (3.2)–(3.3),

```text
p = 6 + 6 t^3 + t^6,    q = 4 t + t^4,
u = x^{-3} p(t),        v = x^4 y q(t),    t = x^6 y,
claimed J(u,v) = -72,
```

is **false as written**. Direct computation:

```text
J(u, x^4 y q(t)) = 3 x^6 y (-x^{54} y^9 - 10 x^{36} y^6 - 30 x^{18} y^3 - 48)
                 not in C*.
```

The same pair with Theorem 4.1’s second component \(v=x^{-2} q(t)\) does
give \(J=-72\), and \(2p'q-3pq'=-72\), \(\deg(p^2-q^3)=3\), which is the
classical Stothers minimizer of Davenport’s bound. So (3.3) is a
mis-copied second component, not a countermodel to Theorem 4.1.

**Strongest exact scope that is confirmed:** after polynomial elementary
changes putting a noninvertible Keller pair into the Newton-shape of
Theorem 1.3, a finite sequence of *q*-elementaries can be attempted along
the six local cutting moves, and each individual move does what the paper
says to the *leading form of the current side*. **Not confirmed:** that
the process is well-founded through the remainder walk, that it must
terminate with some \(J(f_w,g_w)\in\mathbb{C}^*\), or that the output is
a *q*-map whose invertibility (in any category) recovers a polynomial
inverse of the input.

This is not a global JC2 reduction.

---

## 4. Theorem 4.1

**Verdict: `CONFIRMED` for coprime positive \(k,r\), polynomials of exact
degrees \(kd,rd\) whose leading coefficients satisfy
\(\mathrm{lc}(p)^r=\mathrm{lc}(q)^k\), and \(m=k+r+1\). Both directions
among (1),(2),(3) hold. The unrestricted statement (no leading-coefficient
matching) is false. Over \(\mathbb{C}(x)\) with degree in a separate
variable \(z\), the *degree* identity survives; the *Jacobian* identity
does not, unless \(p,q\) are independent of \(x\) or the substitution
\(z=x^m y\) is restored.**

### Independent derivation

Let \(k,r,d\in\mathbb{N}\), \(\gcd(k,r)=1\), \(\deg p=kd\), \(\deg q=rd\),
and write \(W:=r p' q-k p q'\), \(R:=\deg(p^r-q^k)\),
\(A:=p^r\), \(B:=q^k\). Naive degrees: \(\deg A=\deg B=krd\).

Leading terms of \(W\): the degree-\(d(k+r)-1\) parts of \(r p' q\) and
\(k p q'\) are \(rkd\,\mathrm{lc}(p)\mathrm{lc}(q)\,t^{d(k+r)-1}\) and
cancel. So \(\deg W\le d(k+r)-2\) always.

Let \(\delta(a/b)=\deg a-\deg b\). If \(\delta(f)\neq 0\) then
\(\delta(f')=\delta(f)-1\). Also
\((p^r-q^k)/q^k = p^r/q^k-1\), so the two functions have the same
derivative.

If \(\mathrm{lc}(p)^r=\mathrm{lc}(q)^k\), then \(R<krd\),
\(\delta((p^r-q^k)/q^k)=R-krd\neq 0\) (unless \(p^r=q^k\)), and

```text
δ((p^r/q^k)') = (r-1)deg p + (k-1)deg q + deg W - 2k deg q
              = -kd - rd + deg W.
```

The other expression is \(R-krd-1\). Equating them:

```text
R - krd - 1 = -kd - rd + deg W
R = d(kr - k - r) + 1 + deg W.                 (*)
```

Hence \(R\ge d(kr-k-r)+1\), with equality iff \(\deg W=0\) and \(W\neq 0\),
i.e. \(W\in\mathbb{C}^*\). This is (1)\(\Leftrightarrow\)(2), provided
\(p^r\not\equiv c\,q^k\). If \(W=0\) then \((\log p^r)'=(\log q^k)'\), so
\(p^r=c q^k\); after matching leading coefficients one gets \(R=-\infty\).

For (1)\(\Leftrightarrow\)(3), apply Lemma 2.2 to
\(u=x^{-k}p(x^m y)\), \(v=x^{-r}q(x^m y)\): here \(l=s=0\), \(n=1\),
so

```text
J(u,v) = [r t p'q - k t p q'] x^{-k-r-1} y^{-1}
       = W(t) · x^{m-k-r-1}.
```

With \(m=k+r+1\) one has \(J(u,v)=W(x^m y)\). Thus \(J(u,v)\in\mathbb{C}^*\)
if and only if \(W\in\mathbb{C}^*\). Sign: the paper’s \(rp'q-kpq'\) is the
correct one; the opposite sign would send \(J\) to \(-W\).

Coprimeness of \(k,r\) is not used in \((*)\). It is the standard Mason–
Stothers setup (if \(\gcd(k,r)=g>1\) then \(p^r-q^k\) factors as a
difference of \(g\)-th powers). Coprimeness of \(p\) and \(q\) is not in
the theorem statement; if they share a factor then \(W\) may vanish or drop
degree, and the equality case of Mason–Stothers is excluded anyway.

### Smallest countermodel to the unrestricted statement

Take \(p=2t^4+1\), \(q=t^3+1\), \(k=4\), \(r=3\), \(d=1\). Then
\(\mathrm{lc}(p)^3=8\neq 1=\mathrm{lc}(q)^4\), \(\deg(p^3-q^4)=12=krd\),
and \(\deg W=3\neq 0\). Identity \((*)\) fails, (2) fails, and the
associated \(J(u,v)\) is not constant. Scaling to match leading
coefficients restores the setup.

Generic *monic* pair of degrees \(4,3\): \(\deg(p^3-q^4)=11=6+5\), matching
\((*)\) with bound \(6\) and \(\deg W=5\). Equality (2) is rare.

### Stothers pair of the paper (3.2)

```text
p = 6+6t^3+t^6,   q = 4t+t^4,   k=3, r=2, d=2.
2p'q - 3p q' = -72 ∈ C*,
deg(p^2-q^3) = 3 = 2(6-3-2)+1,
J(x^{-3} p(x^6 y), x^{-2} q(x^6 y)) = -72.
```

All three sides of Theorem 4.1 hold. This is the pair the paper intended
next to (3.2); see the (3.3) correction in §3.

### Over \(\mathbb{C}(x)\), degree in a separate \(z\)

The identity \((*)\) is about \(\deg_z\) and \(d/dz\). It holds over any
characteristic-zero coefficient field, including \(\mathbb{C}(x)\), as soon
as \(\deg_z p=kd\), \(\deg_z q=rd\) and
\(\mathrm{lc}_z(p)^r=\mathrm{lc}_z(q)^k\) in \(\mathbb{C}(x)^*\). Check:
\(p=z^2+x\), \(q=z^3+xz\), \(k=2\), \(r=3\), \(d=1\) gives
\(\deg_z(p^3-q^2)=4=2+\deg_z W\), bound \(2\).

Specialization / discriminant exceptions, all of which can drop or raise
\(\deg_z\):

- a pole or zero of \(\mathrm{lc}_z(p)\) or \(\mathrm{lc}_z(q)\) at a
  special \(x_0\) (degrees in \(z\) drop);
- a special \(x_0\) at which the matched-leading-coefficient identity
  fails after clearing denominators;
- vanishing of the leading coefficient of \(W\) as an element of
  \(\mathbb{C}(x)[z]\), so \(\deg_z W\) jumps down and \(R\) may drop;
- a common factor of \(p\) and \(q\) in \(\mathbb{C}(x)[z]\) after
  specialization (discriminant locus of the pair);
- characteristic-\(p\) reduction, excluded by the paper’s
  characteristic-zero setting.

The Jacobian identity is **not** the \(z\)-Wronskian. If \(p,q\in\mathbb{C}(x)[z]\)
depend on \(x\) and \(z\) is independent of \(x\), then
\(J_{x,z}(x^{-k}p,\,x^{-r}q)\) acquires extra \(p_x,q_x\) terms and is not
equal to \(W\). Restoring \(z=x^m y\) recovers Theorem 4.1. For the
maximum-12 client, \(f,g\in\mathbb{C}[x][z]\) and the object of interest
is \(\deg_z(g^3-f^4)\), i.e. the *degree* side of Theorem 4.1 over
\(\mathbb{C}(x)\), not the associated *q*-map.

---

## 5. Classification citation (Pakovich–Zvonkin 2014)

**Verdict: `OVERREAD`.** The paper’s sentence (English ~p. 516 / Russian
HTML §4) that Pakovich–Zvonkin obtained a “complete classification of the
polynomials \(p,q\) minimizing \(\deg(p^r-q^k)\)” is strictly stronger than
what [15] proves.

Pakovich–Zvonkin, arXiv:1306.4141, as actually stated:

- A Davenport–Zannier triple is a coprime pair \(P,Q\in\mathbb{C}[x]\) of
  equal degree \(n\) with prescribed root-multiplicity partitions
  \(\alpha,\beta\vdash n\) such that \(\deg(P-Q)\) attains the Riemann–
  Hurwitz lower bound \((n+1)-(p+q)\) (Definition 1.1).
- Weighted bicolored plane trees are in correspondence with complex
  DZ-triples of a given passport (dessins / Belyi). Existence of a tree
  \(\Leftrightarrow\) existence of a complex equality pair with that
  passport (Theorem 3.1 / 3.3): a tree exists iff
  \(p+q\le n/d+1\), \(d=\gcd(\alpha,\beta)\). This is Zannier 1995 recast
  in dessin language, and it classifies *existence over \(\mathbb{C}\)*,
  not a list of polynomials.
- A *unitree* is a weighted tree unique for its passport (Definition 5.2).
  Uniqueness of the tree is a *sufficient* condition for the corresponding
  DZ-triple to be defined over \(\mathbb{Q}\). It is not necessary
  (Section 6 produces further rational examples by Galois invariants).
- The main theorem of the paper, Theorem 5.4, is a complete classification
  of **unitrees**: ten infinite series \(A\)–\(J\) and ten sporadic trees
  \(K\)–\(T\), up to colour swap and multiplying all weights by \(d>1\).
- Computation of the actual polynomials is postponed: “This paper deals
  only with the combinatorial aspect… The computation of the corresponding
  DZ-triples is postponed to a separate publication.” (p. 4 of the arXiv
  text).

So the licensed objects are:

| Object | Licensed by Pakovich–Zvonkin 2014? |
|---|---|
| All complex equality pairs of a given passport | Existence, via trees; not an enumerated list of polynomials |
| Weighted plane-tree correspondence | Yes, the dictionary of the paper |
| Unitrees | Yes: complete combinatorial classification, Theorem 5.4 |
| Rational-coefficient examples | Those coming from unitrees (existence over \(\mathbb{Q}\)), plus further examples in §6; explicit polynomials not computed here |

### Exponent pair \((4,3)\), \(d=3\)

Here \(p\) has degree \(kd=12\), \(q\) has degree \(rd=9\),
\(P=p^3\) and \(Q=q^4\) both have degree \(n=36\). If \(p\) and \(q\) are
square-free, the passport is twelve black vertices of degree 3 and nine
white vertices of degree 4. Then \(d=\gcd(3,4)=1\), \(p+q=21\le 37=n+1\),
so a tree exists and the bound \(\deg(P-Q)\ge 16\) is attained over
\(\mathbb{C}\). That is exactly Pinchuk’s bound
\(d(kr-k-r)+1=3(12-4-3)+1=16\).

This passport is **not** a unitree. The unitree series of Theorem 5.4 are
stars, periodic chains, brushes, and a handful of small-diameter sporadics;
none is “twelve vertices of degree 3 and nine of degree 4”. Consequently
2014 licenses:

- existence over \(\mathbb{C}\) of minimizing pairs with this multiplicity
  pattern;
- **no** uniqueness over \(\mathbb{Q}\);
- **no** finite list of explicit polynomials;
- **no** finite enumeration that can be dropped onto a coefficient
  trajectory in \(\mathbb{C}(x)\).

A finite combinatorial enumeration of weighted trees with this passport is
in principle possible (trees on 21 vertices, 20 edges, total weight 36).
That is a dessin census, not a classification of \(\mathbb{C}(x)\)-pairs,
and it is not carried out in [15].

---

## 6. Maximum-12 client

**Verdict: `CONFIRMED` as algebra and as the numerical bound; the cited
source supplies a combinatorial parameterization of *complex* equality
pairs, not rigidity of a \(\mathbb{C}(x)\) coefficient trajectory.**

### The elimination identity

Let \(W=g^3-f^4-3kf^2 g-k^3 f^2\). Let \(\tau\) satisfy \(\tau^3=f\). Then

```text
Norm_{t^3=f}(g - f t - k t^2)
  = Resultant_t(t^3-f, g-f t-k t^2)
  = g^3 - f^4 - 3 k f^2 g - k^3 f^2
  = W.
```

Confirmed (sympy: both the resultant and \(\det(gI-f M_t-k M_t^2)\) equal
\(W\) on the nose, no sign error). At \(k=0\) this is the elementary
identity \(g^3-f^4=\prod_{i=0}^2(g-f\,\omega^i\rho)\), \(\rho^3=f\).

For the Jacobian, if \(k\) is independent of the two Jacobian variables
then \(W=W(f,g)\) and

```text
J(f,W) = W_g J(f,g) = 3(g^2 - k f^2) J(f,g).
```

Confirmed on generic bilinear \(f,g\) with constant \(k\). If \(k=k(x)\)
then an extra term \(W_k J(f,k)\) appears:

```text
W_k = -3 f^2 g - 3 k^2 f^2,    J(f,k) = -k' f_y,
```

and the displayed identity fails wherever \(k'\neq 0\) and \(f_y\neq 0\).
On the campaign’s Faber face, \(k\) is a function of \(x\) only. The
identity as printed is therefore the \(k\)-constant (or \(k_y=0\) and
Jacobian taken in \((z,\cdot)\) with \(x\) parametric, ignoring
\(J(f,k)\)) form. For the \(k=\mu=\nu=0\) locus the extra term is zero
anyway.

### The bound 16

Exponents \((k,r)=(4,3)\), \(d=3\): \(\deg g=12=4\cdot 3\),
\(\deg f=9=3\cdot 3\), \(W_0:=g^3-f^4\). Theorem 4.1 / Mason–Stothers /
Zannier give

```text
deg_z(g^3 - f^4)  ≥  d(kr-k-r)+1 = 3(12-4-3)+1 = 16,
```

for coprime \(f,g\) of those exact \(z\)-degrees with matched leading
coefficients (monic is enough). Equality iff \(3 g_z f-4 g f_z\in\mathbb{C}(x)^*\).

Generic monic pair of degrees \((9,12)\) does **not** attain 16: the
\(z^{35}\) coefficient of \(g^3-f^4\) is \(3B-4A\) for subleading
coefficients \(A,B\), and even after that cancellation the generic degree
is 35, 34, … down to the bound. Attaining 16 is the equality case.

On \(k=\mu=\nu=0\), a *coprime* monic pair of \(z\)-degrees \((9,12)\) with
\(\deg_z W=16\) therefore does exactly attain the polynomial-abc bound for
exponents \((4,3)\). That is tautological given the bound, and it is
correct. The common-cubic locus \(f=K^3\), \(g=K^4\) is *not* coprime and
has \(W\equiv 0\); it is not this client.

Whether the campaign’s Faber conditions \(r_1=r_2=r_4=r_5=r_7=0\),
\(r_3=\mu=0\), \(r_6=\nu=0\) *force* \(\deg_z W=16\) (rather than 17
through 35) is a statement about that fibre, not about Pinchuk. The packet
attributes the possible degrees 21, 18, 16 to \(r_3,r_6,r_8\). This audit
does not re-derive the Faber expansion; it only confirms that *if* those
conditions put the pair on the equality locus, the number 16 is the
Davenport–Zannier number for \((4,3)\), \(d=3\).

### What the cited source supplies

Pakovich–Zvonkin: a weighted-tree parameterization of complex equality
pairs of a prescribed *passport*, plus a complete list of unitrees. For
the square-free passport \((3^{12}\mid 4^{9})\) this is existence over
\(\mathbb{C}\), not a finite rigid list, and not a constraint on
coefficient functions of \(x\). Pinchuk Theorem 4.1: the ODE
\(3 g_z f-4 g f_z\in\mathbb{C}(x)^*\) equivalent to \(\deg_z=16\). Neither
source rigidifies a trajectory in \(\mathbb{C}(x)\).

### Cheapest honest next test

On the already-compiled \((9,12)\) order-three fibre with \(k=\mu=\nu=0\),
impose the *z*-Wronskian condition

```text
3 f g_z - 4 g f_z  ∈  C(x)*
```

(equivalently: all \(z\)-coefficients of \(g^3-f^4\) of degree \(>16\)
vanish) and decide whether the remaining coefficient ODE / algebraic
system is empty, finite, or still a positive-dimensional family after
affine/scaling. Do **not** import a unitree list. Do **not** treat a dessin
census of passport \((3^{12}\mid 4^{9})\) as a \(\mathbb{C}(x)\)
classification. Stop if the Wronskian condition is independent of the
Keller+Faber equations and leaves a positive-dimensional family: then the
abc bound is attained or not according to a further differential condition,
not a finite list.

---

## 7. Campaign impact

### Valid local identities, not a global JC2 reduction

Usable, and only these:

- Theorem 4.1 (1)\(\Leftrightarrow\)(2) over \(\mathbb{C}(x)\) in the fibre
  variable, giving the number 16 for exponents \((4,3)\), \(d=3\).
- The algebraic identity \(W=\mathrm{Norm}_{t^3=f}(g-ft-kt^2)\) and, for
  constant \(k\), \(J(f,W)=3(g^2-kf^2)J(f,g)\).
- The dictionary “equality in Davenport–Zannier \(\Leftrightarrow\)
  \(W_{\mathrm{Wronskian}}\in\mathbb{C}^*\)”, which names the cheapest
  extra equation on the \(k=\mu=\nu=0\) face.

Not usable as a theorem input:

- Theorem 3.4 as a global reduction of an arbitrary plane Keller pair to a
  polynomial problem, to a GGV corner, or to a Sigray book.
- “*q*-invertible \(\Rightarrow\) polynomial inverse”.
- “Pakovich–Zvonkin supplies a finite rigid list for \((4,3)\), \(d=3\)”.
- Any identification of this paper with the 1994 real Pinchuk maps.

Theorem 3.4, even if the termination gap were closed, would produce a
*q*-polynomial with a distinguished negative-weight side of constant
Jacobian. That object is not an input to `G2-PSC` (packet/sheet
compatibility of a GGV corner with a Sigray pole tree), not an input to
`G2-BD`, and not a polynomial pair the GGV farm can enumerate. The
*q*-elementary \((x,\,y+c x^\mu)\) with \(\mu\notin\mathbb{N}\cup\{0\}\) is
exactly the kind of source change that *destroys* polynomiality and
therefore cannot land in the books.

A remark in §1 that Theorem 3.4 can be used to construct possible
counterexamples in the Weyl algebra \(A_1\) (citing Joseph [10, Thm 4.2
and Prop. 5.5] and Dixmier [9]) is a pointer to Avenues 13–14, not a
construction, and not a plane-polynomial CE.

### Avenue map (promotion / quarantine language)

Copy-ready.

**Promote, as a local identity only, not as a theorem landing a Keller
pair:**

> Pinchuk 2021 Theorem 4.1, for coprime positive \(k,r\) and polynomials
> of degrees \(kd,rd\) with matched leading coefficients, the three
> conditions \(rp'q-kpq'\in\mathbb{C}^*\),
> \(\deg(p^r-q^k)=d(kr-k-r)+1\), and
> \(J(x^{-k}p(x^{k+r+1}y),\,x^{-r}q(x^{k+r+1}y))\in\mathbb{C}^*\) are
> equivalent. The degree identity remains valid for \(\deg_z\) over
> \(\mathbb{C}(x)\). For exponents \((4,3)\) and \(d=3\) the number is 16.
> This is the polynomial-abc bound on the maximum-12 face
> \(k=\mu=\nu=0\), coprime monic \(z\)-degrees \((9,12)\). It is not a
> classification of that face.

Map: Avenue 1 (Newton / GGV) as *related geometry, not a replacement*;
Avenue 25 (dessins / Hurwitz) as the correct home of the Pakovich–Zvonkin
dictionary; the maximum-12 \((9,12)\) order-three fibre as the only live
client.

**Quarantine:**

> S. I. Pinchuk, *Quasi-polynomial mappings with constant Jacobian*, Izv.
> Math. 85:3 (2021), is a different paper and a different topic from the
> 1994 real Pinchuk counterexamples to the strong real Jacobian
> conjecture. Avenue 24 is unchanged. Do not deform a real Pinchuk map,
> and do not cite 2021 as evidence about real nonvanishing Jacobian.
>
> Theorem 3.4 is **not** licensed as a global JC2 reduction, **not**
> licensed as `G2-PSC` transport, and **not** licensed as a polynomial
> normal form. Its remainder walk is a sketch (`GAP`). Source changes
> include rational negative powers and leave \(\mathbb{C}[x,y]\).
>
> The sentence that Pakovich–Zvonkin 2014 gives a “complete
> classification” of minimizing pairs is an overread of a classification
> of *unitrees*. For passport \((3^{12}\mid 4^{9})\) the 2014 paper
> licenses existence over \(\mathbb{C}\), not a finite \(\mathbb{Q}\)-list
> and not a \(\mathbb{C}(x)\)-rigid trajectory.

**Unchanged avenues.** All 46 numbered rows except the local identity use
just named. In particular Avenue 5 (JvdK elementaries) already contains
the polynomial half of Definitions 1.1 / 3.1; the *q*-half is new as a
citation and is not a proof tool. Avenue 2 (Sigray ladder) does not gain a
source theorem.

### Exact promotion sentence for the evidence bank

> SOURCE-AUDITED 2026-08-24, Pinchuk Izv. Math. 85:3 (2021): Theorem 4.1
> CONFIRMED as an identity under matched leading coefficients; the
> maximum-12 number 16 is that identity at \((k,r,d)=(4,3,3)\). Theorem
> 3.4 GAP as a complete reduction; not a polynomial Keller form; not
> JC2. Pakovich–Zvonkin 2014 OVERREAD as a complete classification of
> minimizing pairs. Not Avenue 24. No JC2 inference.

---

## Bounded successor

One test, then stop.

On the existing \((9,12)\) order-three fibre at \(k=\mu=\nu=0\), add the
single extra condition \(\deg_z(g^3-f^4)=16\) (equivalently
\(3fg_z-4gf_z\in\mathbb{C}(x)^*\)) and decide emptiness / finiteness /
positive dimension after affine and scaling. Interpreter:

- empty: the coprime \(k=0\) face does not attain the abc bound, so the
  packet’s “exactly 16” claim is false on this fibre (the pair is either
  non-coprime or has \(\deg_z W>16\), both of which are separate cases);
- finite (after scaling): a genuine finite list, which then has to be
  matched to Taylor boundaries — this is the only way the 2021 paper
  helps the fibre;
- positive-dimensional: Pakovich–Zvonkin trees parameterize the generic
  fibre of the Wronskian condition over \(\mathbb{C}\), and one still has
  to impose Keller+Faber, so there is no shortcut.

Do not close Theorem 3.4 as a campaign engine. A documentation-only
reconstruction of one Newton-polygon walk through Cases 4 then 6, tracking
\((K,L,m,N)\), would test the remainder measure; it would still not land a
Keller pair in the books.

---

## What this audit does not claim

- Novelty or priority of quasi-polynomial reductions, Newton cutting, or
  Davenport–Zannier.
- A proof or disproof of JC2.
- That Theorem 3.4 is false: no countermodel to the statement was
  produced; the proof is incomplete as printed.
- That a maximum-12 Keller pair exists or does not.
- Any change to canonical, packet, producer, reviewer, prompt, run, log,
  or case files.

Scratch used: `/tmp/pinchuk-audit-20260824`, `/tmp/pinchuk-venv`. Not in
the bank.
