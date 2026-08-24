# Artin--Schreier all-Witt/Tate control

- **Producer/session:** OpenAI Codex, Bacon provisional W descendant
- **Date:** `2026-08-24T03:07:57Z`
- **Basis commit:** `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`
- **Status:** **PROVISIONAL** — the upstream `AS3-MIN-W2 / W2-SURVIVOR`
  remains under independent Claude review
- **Method:** closed-form exact identities only; no Witt search, enumeration,
  solver, network call, or shared-ledger edit

## Verdict

The `p=3` survivor has an explicit compatible polynomial lift over every
finite Witt ring, provided support is allowed to grow.  The same construction
works for every odd prime `p`.  Its coefficientwise inverse limit is not a
polynomial map: it is the rational, restricted-analytic map

\[
 (x,y)\longmapsto
 \left(x-x^p,\frac{y}{1-px^{p-1}}\right)
 \quad\text{over }\mathbf Z_p.
\]

Thus the control defeats any argument that passes from an **unbounded-support**
compatible all-Witt tower to a characteristic-zero **polynomial** merely by
taking the inverse limit.  It does not touch a fixed-support or uniformly
bounded-degree theorem, and it is not a plane Jacobian-conjecture
counterexample.

This report is the one explicitly provisional descendant permitted while the
upstream `W2-SURVIVOR` is reviewed.  The algebra below is standalone, but its
campaign lineage and any promotion remain conditional on that review.

## 1. Closed-form tower

Let `p` be an odd prime and identify

\[
 R_n=W_n(\mathbf F_p)=\mathbf Z/p^n\mathbf Z.
\]

Put

\[
 z=p x^{p-1},\qquad
 S_n(x)=\sum_{j=0}^{n-1}z^j
       =\sum_{j=0}^{n-1}p^j x^{j(p-1)},
\]

and define the polynomial map over `R_n`

\[
 F_n=(P_n,Q_n)
 =\left(x-x^p,\ yS_n(x)\right).                 \tag{1.1}
\]

The coefficient `-1` is the Teichmuller lift of `-1 in F_p` for odd `p`, so
the first coordinate is itself compatible at every level.  At `n=1`, (1.1)
is exactly the Artin--Schreier special fibre `(x-x^p,y)`.

### Determinant

Since `P_n` is independent of `y`,

\[
 \begin{aligned}
 [P_n,Q_n]
 &=\frac{\partial P_n}{\partial x}
   \frac{\partial Q_n}{\partial y}
   -\frac{\partial P_n}{\partial y}
    \frac{\partial Q_n}{\partial x}\\
 &=(1-px^{p-1})S_n(x)\\
 &=(1-z)(1+z+\cdots+z^{n-1})\\
 &=1-z^n
  =1-p^n x^{n(p-1)}.                            \tag{1.2}
 \end{aligned}
\]

Equation (1.2) is an identity over `Z[x]`, not a sampled congruence.  Hence

\[
 [P_n,Q_n]=1\quad\text{in }R_n[x,y]              \tag{1.3}
\]

for every `n>=1`.

### Reduction compatibility

The standard truncation `R_{n+1} -> R_n` gives

\[
 S_{n+1}-S_n=p^n x^{n(p-1)}=0\quad\text{in }R_n[x].
\]

Therefore

\[
 F_{n+1}\bmod p^n=F_n.                           \tag{1.4}
\]

More generally, the same equality holds from any later level to any earlier
one.  This is a single compatible tower, not merely one independently chosen
solution at each `n`.

### Fixed marked collision

The constant sections

\[
 r_0=(0,0),\qquad r_1=(1,0)
\]

are distinct over every `R_n`, and

\[
 F_n(r_0)=F_n(r_1)=(0,0)                         \tag{1.5}
\]

holds exactly: `0-0^p=0`, `1-1^p=0`, and `Q_n` has a factor `y`.
Thus the points, target, determinant, and maps are all compatible through the
tower; no moving-point choice is being hidden.

There is also an exact finite-level algebra description.  If `U=P_n` and
`V=Q_n`, then `S_n` is a unit with inverse `1-px^{p-1}` in `R_n[x]`, and

\[
 R_n[x,y]\cong
 R_n[U,V,X]/(X^p-X+U),\qquad
 x=X,\quad y=V(1-pX^{p-1}).                       \tag{1.6}
\]

Hence every finite-level map is finite locally free of rank `p` and etale:
the derivative `pX^{p-1}-1` is a unit.  This is a rank statement over the
non-domain `R_n`, not an illicit generic-degree calculation there; its special
fibre has the already reviewed generic degree `p`.

## 2. The `p=3` crosswalk

For `p=3`,

\[
 P_n=x-x^3,\qquad
 Q_n=y\sum_{j=0}^{n-1}3^j x^{2j}.                \tag{2.1}
\]

At `n=2`,

\[
 (P_2,Q_2)=(x-x^3,\ y+3x^2y)\pmod 9.            \tag{2.2}
\]

Because `-1=8 mod 9`, this is precisely the producer's displayed map

\[
 (x+8x^3,\ y+3x^2y)\pmod9.
\]

With the fixed integral representative `x-x^3`, (1.2) reads
`[P_2,Q_2]=1-9x^4`; the producer used the congruent representative
`x+8x^3` and printed `1+27x^2+72x^4`.  These integer representatives differ,
but their maps and determinants agree modulo `9`.  Thus the all-level formula
crosswalks to the provisional `W2-SURVIVOR` without importing its obstruction
solver.

## 3. Exact support and degree growth

Every coefficient `p^j` with `0<=j<n` is nonzero in `R_n`.  Consequently

\[
 \operatorname{supp}(Q_n)
 =\{(j(p-1),1):0\le j<n\},                       \tag{3.1}
\]

so `Q_n` has exactly `n` monomials,

\[
 \deg_x Q_n=(n-1)(p-1),\qquad
 \deg Q_n=(n-1)(p-1)+1.                          \tag{3.2}
\]

The full map has

\[
 \deg F_n=\max\{p,(n-1)(p-1)+1\};               \tag{3.3}
\]

this equals `p` for `n=1,2` and then grows linearly.  The coefficient of the
`j`th new monomial has exact `p`-adic valuation `j`.  Thus the support union is
infinite even though every finite-level representative is a polynomial.

This growth is the load-bearing feature of the control.  It does not inhabit
any fixed finite support or uniform degree cap.

## 4. Inverse limit: restricted analytic and rational, not polynomial

The inverse limit of the coefficient rings with polynomial representatives is
the `p`-adic completion

\[
 \varprojlim_n R_n[x,y]\cong\mathbf Z_p\langle x,y\rangle,
\]

the ring of restricted power series: for each `p`-adic precision only finitely
many coefficients are nonzero.  Here

\[
 S_\infty(x)=\sum_{j\ge0}p^j x^{j(p-1)}
\]

is restricted because its coefficient valuations tend to infinity.  Since
`px^{p-1}` has Gauss norm at most `p^{-1}` on the closed unit disc,

\[
 S_\infty(x)=\frac{1}{1-px^{p-1}}
 \quad\text{in }\mathbf Z_p\langle x\rangle.      \tag{4.1}
\]

The compatible tower therefore converges coefficientwise to

\[
 F_\infty=
 \left(x-x^p,\frac{y}{1-px^{p-1}}\right)
 \in\mathbf Z_p\langle x,y\rangle^2.             \tag{4.2}
\]

It is simultaneously a rational map over `Q_p` and a restricted-analytic map
on the closed unit bidisc.  Its denominator is congruent to one modulo `p`, so
it is a unit everywhere on `Z_p`; there is no hidden pole at either marked
point.  Taking the convergent geometric series, or differentiating the rational
expression directly, gives

\[
 [F_\infty]=1                                    \tag{4.3}
\]

exactly, and the collision `(0,0),(1,0)->(0,0)` persists over `Z_p`.

The analogue of (1.6) shows that (4.2) is finite etale of rank `p` as an
endomorphism of the closed `p`-adic unit bidisc.  This is a statement in the
restricted-analytic category; the same rational expression is not an
everywhere-defined algebraic endomorphism of affine two-space.

The second coordinate is not in `Z_p[x,y]`: every coefficient `p^j` is
nonzero in the characteristic-zero domain `Z_p`, so (4.1) has infinitely many
nonzero monomials.  Equivalently, the nonconstant denominator
`1-px^{p-1}` is not a unit of the polynomial ring.  The inverse limit is
therefore not a characteristic-zero polynomial map.

## 5. What the control refutes—and what it does not

The exact identities prove the following limited negative statements.

1. **No universal later unrestricted Witt obstruction for this control.**  An
   explicit compatible lift exists at every finite `W_n(F_p)` once new support
   is allowed.  The upstream `W_2` survival is not forced to die at `W_3` or
   another finite level in the unrestricted-support problem.
2. **`W_2` survival is not an algebraization certificate.**  The `p=3` lift is
   merely the first truncation of a tower whose natural limit is nonpolynomial.
3. **Unbounded-support all-Witt compatibility does not make its inverse limit
   polynomial.**  The actual inverse limit lands in the restricted Tate
   algebra and resums rationally; coefficient compatibility alone does not put
   it in `Z_p[x,y]`.

The third statement concerns the given tower and the formal inverse-limit
passage.  It does **not** prove that the special fibre has no different,
bounded-support characteristic-zero polynomial lift.  Ruling out—or
constructing—such an alternative would be a much stronger problem.

In particular, this control does not refute:

- a theorem assuming one fixed finite support or a uniform degree bound;
- a separately proved algebraization or finite-generation lemma;
- a claim about existence of some other polynomial lift rather than the
  coefficientwise limit of this tower;
- any obstruction on the prior characteristic-two Mondello stratum;
- the plane Jacobian conjecture over `Q_p`, `Q`, `C`, or any characteristic-zero
  field.

The map (4.2) is a noninjective characteristic-zero **rational/restricted-
analytic** unit-Jacobian map, not a polynomial map.  Calling it a JC2
counterexample would change the category and be false.

## 6. Prior-art and repository deduplication

The ingredients already in the repository are narrower:

- `xmodel/sol-pcurvature.md:136-149` records the special-fibre family
  `(x-x^p,y)` as a degree-`p` finite-etale nonautomorphism control.
- `xmodel/review-round1-proof-gates-claude.md:302-306` independently confirms
  the Artin--Schreier generic-degree/separability warning.
- `xmodel/round2-witt-oddprime-20260824.md:8-61` records only the `p=3`,
  `n=2` lift and collision, and explicitly says that its artifact supplies no
  all-level tower at lines 149-163.

A repository-wide exact-pattern search for the denominator
`1-p x^(p-1)`, the coefficient pattern `p^k x^{k(p-1)}`, and an all-level
`Q_n` returned no prior occurrence.  Broader searches for Artin--Schreier,
Witt inverse limits, and Tate/restricted-analytic language found the preceding
special-fibre and `W_2` records, but not (1.1)--(4.2).  Accordingly the
closed-form compatible tower and its rational/Tate limit are new to the
repository; the underlying special fibre and first lift are not.

Frozen upstream artifacts used for the crosswalk:

| Artifact | SHA-256 |
|---|---|
| `cases/round2_witt_oddprime/PREREGISTRATION.md` | `af9917fe117c84a92ab9738c1d258d636354cec63cdc81e5e5bd1cbe4f6269e3` |
| `xmodel/round2-witt-oddprime-20260824.md` | `09b901f2a27f825a627da2ad0835d1875212716693769d505ab465b04bae6ff1` |
| `cases/round2_witt_oddprime/results.json` | `bb02c36fcd8356529b1d188fa61760bbfd6194fafcd050740752a795abd5201c` |
| `cases/round2_witt_oddprime/replay.json` | `2285ade3f46eb9fb22cffb1af0c950776e8c1f9ee89e94a92e8a4495571d5341` |
| `xmodel/review-witt-oddprime-claude-prompt.md` | `55fde648bfee42e436b5880c09a78c40b7b6c92b18d3e0f8d01dd6ce53aa2f39` |

No promotion is licensed until the upstream review returns.  Regardless of
that lifecycle result, equations (1.1)--(4.3) remain elementary identities;
their honest use is as an algebraization/support-growth negative control.
