# First independent hostile review of INITIAL0955

- Task: `infinity-jet-graded-obstruction-review-sol56-20261030T1300Z`
- Configured model: `gpt-5.6-sol`; hosted identity: `UNVERIFIED`
- Startup UTC: `2026-10-30T13:08:05Z`
- Review completed UTC: `2026-10-30T13:16:04Z`
- Verdict: **GAP**

## Disposition

The all-`n` Jacobian calculation, the primitive source and target infinity valuations,
the two raw discrepancies, `e=1`, `f=2`, the fixed-precision obstruction, and both
full associated-graded ring descriptions check. The bracket signs and degree shift
also check. One material ambiguity prevents `PASS_SCOPED`: the phrase “Its induced
bracket” at `initial-qualified-handoff.md:57` does not distinguish restriction of the
ambient bracket after grading from an associated-graded bracket induced from `A_n`.
The latter reading is false for every `n>=2`.

## First faulty claim and cheapest correction

Write `h_n(z)=Q_n` and `J_n=1-(-z)^n`. Since `P,z` are algebraically independent,
`A_n=C[P,h_n(z)]` and `A_n intersect C[z]=C[h_n(z)]`. If `J_n` belonged to `A_n`,
then it would belong to `C[h_n]`. Both have `z`-degree `n`, so this would force
`J_n=a h_n+b`. For `n>=2`, matching the nonzero `z^n` term forces `a!=0`, while
the resulting nonzero `z` term cannot match `J_n`. Hence `{P,Q_n}=J_n` is not in
`A_n`; `A_n` is not a Poisson subalgebra before grading. For `n=1` only,
`J_1=1+2Q_1` and closure does hold.

The cheapest correction is to replace the disputed sentence by:

> The ambient degree-`+1` bracket on `gr_v C[x,y]` restricts after grading to
> `gr_v A_n=C[p,q]`, where `{p,q}=1`. For `n>=2`, this is not the associated
> graded of a Poisson bracket on `A_n`, because `A_n` is not Poisson-closed.

No ring equality needs changing. The correction is load-bearing because exact
filtered Poisson closure is automatic for a Keller pair and is absent here.

## Independent checks

1. With `z=xy^3-1` and `P=xy`, direct differentiation gives
   `{P,z}=2xy^3=2(1+z)`. Since
   `h_n'(z)=(1/2) sum_{j=0}^{n-1}(-z)^j`,
   `{P,Q_n}=(1+z) sum_{j=0}^{n-1}(-z)^j=1-(-z)^n` for every `n>=1`.

2. Put `u=y`, `t=z/y`. Then `x=(1+ut)/u^3`, `z=ut`, and `C(x,y)=C(u,t)`.
   The `u`-adic valuation is primitive (`v(u)=1`) and is at infinity because
   `v(x)=-3`. Directly,
   `dx wedge dy=-u^(-2) du wedge dt`, so the source raw discrepancy is `-1`.

3. Use full target-field generators `a=Q_n`, `b=P Q_n^2`; their inverse is
   `P=b/a^2`, `Q_n=a`. They are algebraically independent and
   `dP wedge dQ_n=-a^(-2) da wedge db`. On the source,
   `a=u(t/2+O(u))` and `b=t^2/4+O(u)`. Thus the target valuation is primitive
   and at infinity (`v(a)=1`, `v(P)=-2`), its raw discrepancy is `-1`, its value
   group has index `e=1`, and its residue field is `C(t^2/4)` inside `C(t)`,
   of degree `f=2`. The leading normal coefficient `t/2` equals
   `d(t^2/4)/dt`, with no sign mismatch in the volume identity.

4. For the source grading, `v(u)=v(z)=1` and `z/u=t` is residue-transcendental.
   Every source polynomial becomes a finite Laurent polynomial in `u,z`, so every
   initial form lies in `C[U,U^(-1),Z]`. Conversely, `U`, `U^(-1)`, and `Z` are
   the initials of `y`, `xy^2`, and `xy^3-1`. This proves the full equality
   `gr_v C[x,y]=C[U,U^(-1),Z]`, including arbitrary cancellations. It is a smooth,
   normal, finitely generated Laurent-polynomial ring.

5. The source bracket satisfies `{U,Z}=-U^3`. It has valuation-degree shift `+1`
   and is nondegenerate because `U` is a unit. Its inverse form is
   `-U^(-3)dU wedge dZ`, which becomes `-U^(-2)dU wedge dt` under `Z=Ut`.

6. For `A_n`, `p=in(P)=U^(-2)` and `q=in(Q_n)=Z/2`. The initial monomials of
   `P^a Q_n^b` are `2^(-b)U^(-2a)Z^b`; distinct pairs `(a,b)` give distinct
   Laurent monomials. Even among equal-valuation terms, no cancellation can create
   an outside generator. Hence the full ring equality `gr_v A_n=C[p,q]` holds.
   The ambient graded bracket restricts to it and gives `{p,q}=1`. Its residue
   coordinate is `pq^2=(Z/U)^2/4` and `q` is a primitive normal element.

7. The formal limit `(1/2)log(1+z)` has formal Jacobian one but is not a polynomial
   component. It is only a `z=0` formal series and supplies no global polynomial map.

## Keller-source hypotheses absent from the controls

The full Jacobian is nonconstant and has zeros, so these maps are not étale and do
not preserve the affine volume form exactly. Both components also fail the necessary
Keller nonsingularity condition: `grad(P)=(y,x)` vanishes at `(0,0)`, while
`grad(Q_n)=h_n'(z)(y^3,3xy^2)` vanishes along `y=0`. For `n>=2`, the source-target
inclusion is not Poisson-closed before grading. Thus the controls lack exact global
Jacobian, component submersivity, and full filtered Poisson/volume compatibility.
No properness, integrality, or other hypothesis not forced by the Keller condition
is inserted into this review.

## Exact obstruction scope

For every fixed `M`, taking `n>=M` gives `J_n congruent 1 mod u^M` while retaining
the same raw discrepancies, `e=1`, `f=2`, full graded rings, and ambient leading
bracket. Degree grows with `n`. This excludes only a uniform no-fold criterion whose
complete input is that fixed infinity-Jacobian precision and those stated local or
graded data, with degree unbounded.

It does **not** exclude use of the exact global Jacobian, full filtered compatibility,
component nonsingularity, additional global input, or a degree-dependent certificate
using all coefficients of the particular pair. It does not universalize to every
associated-graded or finite test. The unrelated diagonal-projector result is outside
this review, as required by `root-qualifications.md:9-13`.

## Reading and execution audit

- Preflight verified all 16 packet members and both scientific seals before body use.
- `MANIFEST.json`: 243/243 LF.
- Nine governors: 1340/1340 LF (`23+112+162+259+517+22+102+107+36`).
- `STATE.md`: 150/150 LF under its separate 150-LF allowance.
- `ADMISSION.json`: 44/44 LF; `initial-qualified-handoff.md`: 72/72 LF;
  `root-qualifications.md`: 24/24 LF.
- `APPROACHES-EXCERPT.md`: 4/4 LF, exactly original `APPROACHES.md:33-36` only.
- Exact non-STATE displayed total: 1727 LF, including the manifest; repeated LF: 0.
- No reader STOP, omitted required range, or budget overrun. No links were followed;
  imported foundations of other reports were not reviewed. No CAS, web, source/history
  or repository query, secondary agent/model, protected-tree access, or extra output.
  Deviations: none.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6540`.
- Body SHA-256:
  `2454484f05cec2fa4d97aa78fe9e928bd08174f5c87f745cb80e9b57870484c1`.
- Frozen basis: `397632cbdf8eaaac8c6f22db1c69921adc85f9e4`.
