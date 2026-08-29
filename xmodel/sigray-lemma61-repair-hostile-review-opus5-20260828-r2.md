# Hostile review — Sigray Lemma 6.1 repaired tower proof, R2

Reviewer: Opus 5, different model from the Sol Ultra producer and from the
R1 same-model reviewer.  Date: 2026-08-28 UTC.

## Terminal verdict

**REPAIR.**  Lemma 6.1 is a **true theorem**, and every load-bearing
inference in the R2 proof — the `rho`-monotonicity gate, the fixed-pair
edge law, `r_j>=1`, the Proposition 4.4 transport, the axis orientation, and
the residual degree contradiction — is **CONFIRMED** by independent
re-derivation from the primary source.  I found **no false step and no
counterexample**.  Two *documentary* typing riders are missing and must be
inserted verbatim (Section 9); both are true, both are one line, and neither
changes any conclusion or rolls back any consumer.

## 1. Custody

```text
2fdbbee9ec04db1f3ff1220eeda4ffb84c1c1580948d76a0015119a85602bc5e  xmodel/sigray-lemma61-repair-sol-ultra-20260828-r2.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
651231a80274de4d684076c4b238be38b98e3a4ad704e750a06fa23c43ef6e5f  R1 producer
b279732cdf8a513f2d74688234619fcca6c643b33b428f51c287f64b87bdc28a  R1 same-model review
ca63eb5e75a1d67ac02c2f643aff82b14af3d94a35e26d78e6de523604348e18  no-first-constant-corner review (Sol Ultra)
```

Charged hash recomputed and matched before reading.  The R1 review's verdict
was **not credited**; I re-derived its `rho` gate from scratch.  Primary pages
re-read from the PDF: 8--9, 10--23, 29--36.  No AWS, no web, no CAS.

## 2. The printed defect is real (independent recomputation)

In the `(xi,eta)` chart write `f_F^+=xi^d p(eta)`, `g_F^+=xi^e q(eta)`.  Then

```text
J(f_F^+,g_F^+) = xi^(d+e-1) * ( d*p*q' - e*p'*q ).            (A)
```

With `deg p=1` and `deg q=0` the printed proof's terminal state gives
bracket `-e*p'*q`, which vanishes exactly when `e=d_(g,F)=0`.  The printed
p.34 inference "`deg(p_(g,F_j))=0` ... therefore `J!=0`" is therefore invalid
in isolation.  The producer's diagnosis is exact.  (A) is also the cleanest
proof of the two auxiliary facts used below: `e=0` forces `q'=0`, i.e. a
constant corner; and `e<0` forces `q^d p^(-e)` constant, impossible because
`deg p_F>=1` on `T_a^+`.

## 3. Item 1 — `m_F>0` + corner theorem `=>` `rho(F)>0`   CONFIRMED

`m_F>0` means the Proposition 4.2 recursion did *not* stop at `j=0`, i.e.
`J(f_F^+,h_(0,F)^+)=J(f_F^+,g_F^+)=0`.  Proposition 4.1 (p.18) is a strict
dichotomy under condition (7): `J=xi^(-u)` iff `d_F+d_(g,F)=1-u`, and `J=0`
iff `d_F+d_(g,F)>1-u`.  Hence `rho(F)=d_F+d_(g,F)+u-1>0`.  Condition (7) at
`b=0` is exactly "`g_F^+` is not a nonzero scalar", supplied on all of
`T_a^+` by the reviewed no-first-constant-corner theorem; I confirmed from
`ca63eb5e` that that theorem carries a genuinely different-model
(Sol Ultra) `CONFIRMED AND STRENGTHENED` verdict, so the R2 dependency label
"independently reviewed" is accurate.  Corrected Proposition 4.2's terminal
clause with `mu_F=0` is the converse direction and is used correctly.

## 4. Item 2 — common `K`, `T_a^+` typing, edge law   CONFIRMED

*Fixed-pair typing.* Statement 3.9's hypothesis is "`kappa` suitable **and**
has the property of Proposition 3.1", i.e. `kappa` is a multiple of every
`x`-pole order of the curve `h=0` — an `h`-dependent **divisibility**
condition.  Both `f-a` and `g` are squarefree (a repeated factor would divide
`J(f,g)`), so a single `K` works: take `K = lcm(` suitable `kappa`, all pole
orders on `R_(f-a)` and on `R_g`, denominator of `u` `)`.  Existence is
immediate; the producer's operative requirement is right, its gloss is not
(Section 9, Patch 1).  Only `f-a` and `g` are ever fed to Statement 3.9 —
**no derived tower polynomial**, so the campaign's known auxiliary-`h`
`kappa` hazard is genuinely dormant here.  CONFIRMED.

*Ancestors stay in `T_a^+`.* Statement 3.10(i) makes `u |-> d_(f-a,I_P(u))`
monotone decreasing, so `d_(f-a,F_j) >= d_(f-a,F) > 0` for `j<=Ku`.
CONFIRMED.  This uses the unstated `f <-> f-a` inertness (Section 9,
Patch 2).

*Edge law.* Statement 3.9(iii) applied twice with `kappa=K`, `c=c_j`:

```text
rho(F_(j+1))-rho(F_j) = (-r_j/K) + (-t_j/K) + 1/K = (1-r_j-t_j)/K.
```

Sign and direction CONFIRMED: `rho` decreases as the parameter *increases*,
so **ancestors have the larger `rho`**, which is the direction the argument
needs.  Independent global check by telescoping:
`rho(F_0)-rho(F) = (k_f-d_F)+(k_g-d_(g,F))-u`, consistent.

## 5. Item 3 — `r_j>=1`, including endpoint and zero-root cases   CONFIRMED

Statement 3.18's first clause ("if `F*c` exists then `c` is a root of `p_F`")
is hypothesised for `kappa*pi(F) in N`, **not** `N^*`, so it applies at the
axis `j=0` where `K*pi(F_0)=0`.  I did not have to trust it: Proposition
3.1(**) gives `mult(p_(f-a,F_j),c_j) = #{`Puiseux series of `f-a=0` with
prefix `c_0..c_j}`, and `P` itself realizes that prefix, so `r_j>=1`
unconditionally.  The **zero-root case** `c_j=0` (forced whenever
`kappa_P<K`, so most `j`) is covered identically — `0` is then a genuine root
of `p_(f-a,F_j)`; the converse clause of Statement 3.18 is never used.  With
`t_j>=0` trivially, `1-r_j-t_j<=0`, so `rho(F_j)>=rho(F)>0` for every
`0<=j<=Ku`.

Every ancestor tower is then nonempty: `rho(F_j)>0` + condition (7) +
Proposition 4.1 give `J(f_(F_j)^+,g_(F_j)^+)=0`, hence `m_(F_j)>=1`.  The
first relation is **ordinary** (`k,l in N^*`): `l=0` would make `g_F^+`
scalar (excluded by the corner theorem) and `l>=1` with `k*d_(g,F)=l*d_F>0`
forces `d_(g,F)>0`, so no `(1,0,c)` constant corner can occur at index zero.
CONFIRMED.  Endpoint check: `F_0` is `(0,y)` or `(0,x)`, with
`d_(f,(0,y))=deg_x f=k_f>0`, so `F_0 in T_a^+` and
`rho(F_0)=k_f+k_g-1>=1>0` directly.

## 6. Item 4 — Proposition 4.4 transport   CONFIRMED

Proposition 4.4 is applied at `F=F_(j+1)` with `F'=F_j` (Notation 3.8 with
`kappa=K`), hypothesis (i) `F in T_a^+`, and `K*pi(F_(j+1))=j+1 in N^*`.
Both relations required by its hypotheses exist by Section 5.  The auxiliary
polynomial is the **fixed** `h=g` at every edge — no tower member `h_j` is
ever transported, so the "In particular" comparability clause and its
`l_j>=1` division hazard are not invoked.  Its proof's denominators
`kappa*d_(h,F)`, `kappa*d_(h,F')-mult(q,c)` and `kappa*d_(F')-mult(p,c)` are
all nonzero here, because `d_(g,F_j)>0` (Section 5) and
`kappa*d_(F')-mult(p,c)=kappa*d_F>0` by Statement 3.9(iii).  No unlicensed
auxiliary-`h` denominator.  CONFIRMED.

## 7. Item 5 — axis orientation   CONFIRMED, and a trap cleared

This is the one place where the R2 could have been fatally wrong, and it is
**not**.  `pdftotext -layout` renders stacked fractions with the numerator
subscript collapsed onto the denominator line, which inverts them: read that
way, Notation 2.4 appears to say `alpha/beta=k_g/k_f`, giving the reciprocal
`(k,l)=(beta,alpha)`.  I resolved it with per-glyph bounding boxes
(`pdftotext -bbox`, printed p.9, Notation 2.4(i)): numerator base `k` at
`y=[621.59,628.67]` with subscript `f` at `y=[624.38,629.69]`; denominator
base `k` at `y=[631.99,639.07]` with subscript `g` at `y=[634.37,639.68]`.
So

```text
alpha/beta = k_f/k_g   (so alpha<beta, since k_f<k_g by Lemma 2.1(iii)).
```

Same method on p.8 confirms Lemma 2.1(iv) is `k_g/k_f not in N^*`
(numerator subscript `g` above denominator subscript `f`), which is the
non-vacuous reading and directly yields `alpha!=1` in Statement 2.1.

Orientation, three independent confirmations:
(a) at `(0,y)`, `eta=y` so `d_(h,(0,y))=deg_x h` and
`d_f/d_g=k_f/k_g=alpha/beta`; at `(0,x)`, `l_f/l_g`, equal by Lemma 2.1(ii).
Taking orders in `(g^+)^k=s(f^+)^l` gives `k/l=d_f/d_g=alpha/beta`, and
coprimality gives `(k,l)=(alpha,beta)`.
(b) Proposition 4.5's proof: `(l/k)(k_f,l_f) in N_h`, i.e.
`(k_g,l_g)=(l/k)(k_f,l_f)`, so `l/k=k_g/k_f=beta/alpha`. Same answer, and it
also confirms both charts give the same primitive pair.
(c) The source's own p.34 text, verified by bbox: `(g_(F_n)^+)^(k_f) =
(f_(F_n)^+)^(k_g)`, i.e. `(k,l) ∝ (k_f,k_g) ∝ (alpha,beta)`.

**R2's display (4) is correct.**  My first-pass layout reading said otherwise;
the coordinate evidence overrules it.

## 8. Items 6 and 7 — residual contradiction, terminal clause, consumers

*Residual degrees.* From `(g_F^+)^alpha=s(f_F^+)^beta`, separating `xi` and
`eta` parts gives `p_(g,F)^alpha = s*p_F^beta` (R2 (5)) and
`alpha*d_(g,F)=beta*d_F`.  With `deg p_F=1`: `alpha*deg p_(g,F)=beta`, so
`alpha | beta`, so `alpha=1` by coprimality, contradicting Statement 2.1.
CONFIRMED — and cross-checked against the source's own equation (21),
`deg(p_(F_n)) = (k_f/k_g) deg(p_(g,F_n))`, which is the identical relation.
Note this simultaneously kills `deg p_(g,F)=0` (it would force `beta=0`),
which is precisely the printed hole.  CONFIRMED.

*Terminal clause.* `m_F=0` gives `mu_F=0` and `J(f_F^+,g_F^+)=C*xi^(-u)`.
The constant-leading-part repair is used correctly and only where it is
needed: `C in C^*` rather than the printed bare `xi^(-u)` (the chain rule
gives `J(f,g)/x^u`, so `C=J(f,g)`), and the `(1,0,c)` constant-corner branch
of corrected Proposition 4.2 is excluded at index zero by the corner theorem,
not assumed away.  CONFIRMED.

*Consumers.* Proposition 6.8's proof (p.35) uses Lemma 6.1 exactly once, in
the contrapositive: `deg(p_(F_n))=1 => m_(F_n)=0 => F_(P)^* in T_(a,pole)`,
contradicting minimality via Proposition 5.3(iv),(v).  That rider is now
**discharged**.  It was not, however, Proposition 6.8's *only* prerequisite:
it still rests on repaired Proposition 6.7 (four-part repair), corrected
Statements 3.9/3.11, Proposition 5.3(iv)/(v)/(vii), and the corner theorem.
The correct statement is that Lemma 6.1 was the only outstanding **review**
rider, and that this proof adds **no new** exposure, because Proposition 6.7
already depends on the same corner theorem.  The microstep-to-next-vertex
bridge (Statement 6.2 raw inequality -> Proposition 6.7 positivity ->
`mult(p_G,c)>=2` -> repaired Proposition 6.8 -> Statement 6.2 iff) is
therefore sound as far as Lemma 6.1 is concerned.  R2's closing note that
Statement 6.2's printed "in particular" clause omits `H in V_a cap T_a^+` is
independently confirmed from p.29.  One custody caveat: I am also Opus 5, so
this review adds no cross-model independence for the corner theorem itself —
that independence comes from `ca63eb5e`, not from me.

## 9. The smallest exact patch (both documentary)

**Patch 1 (K typing).**  In the paragraph beginning "Write `F=I_P(u)`",
replace

> Choose one `K` suitable for this chart, with `Ku in N`, large enough that
> Statement 3.9 applies to the two fixed polynomials `f-a` and `g`.

by

> Choose one `K in N^*` that is simultaneously suitable for this chart, a
> multiple of the denominator of `u`, and a multiple of every `x`-pole
> (resp. `y`-pole) order of the curves `f-a=0` and `g=0`, so that Statement
> 3.9 holds for both fixed polynomials; such a `K` exists as the lcm of
> finitely many integers.  Statement 3.9's hypothesis is a divisibility, not
> a size, condition.

**Patch 2 (`f` vs `f-a`).**  After equation (2), insert:

> On `T_a^+` the leading index is positive, so `f_(F_j)^F` and
> `(f-a)_(F_j)^F` have the same leading term: `d_(F_j)=d_(f-a,F_j)` and
> `p_(F_j)=p_(f-a,F_j)`.  This identification is what lets `rho` be written
> with `f-a` while Proposition 4.1, Statement 3.18 and the definition of
> `T_a^+` are stated with `f`.

## 10. Scope

This review establishes Lemma 6.1 and its Proposition 6.8 consumer only.  It
proves no landing, cofinality, degree ceiling, Statement 6.2 domain closure,
or Jacobian-conjecture conclusion, and audits nothing in Sections 7--9.
