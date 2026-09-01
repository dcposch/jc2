# Hostile review: row normal-form exhaustiveness

## 0. Integrity, scope, and verdict

The stop check passed. Before reading the inputs I obtained, in the charged order,

```text
30eb230dca026da6d59cbc7dd733cdb4ca63af443d5069ee83f7713b83a357f3
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc
a88890bdf50e9b864379eb62603d08c11f67f981d589360b75a58ae0d60e5896
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb
```

These exactly match the manifest for `EXHAUST`, `CI5`, `CLOS`, and `SWEEP`. I did not inspect
`jc2-lean`, edit an input or canonical ledger, or run a CAS. The only output is this report.
No new exit price is asserted, so FALLACY-v2 requires no `charge_basis` line.

I independently re-fetched Galindo--Monserrat, arXiv:0910.2613v2, from
`https://arxiv.org/pdf/0910.2613v2`: 241372 bytes, SHA-256
`637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9`. Crossref identifies the
published source as C. Galindo and F. Monserrat, *The Abhyankar--Moh Theorem for plane valuations
at infinity*, Journal of Algebra **374** (2013), 181--194,
`https://doi.org/10.1016/j.jalgebra.2012.11.001`.

**Verdict: REPAIR / SPLIT, not promotion as written.** The conditional algebraic assertion

```text
Delta=(6,4,3) or (8,4,6,3)  ==>  target-equivalent to some D_{b,c}, c!=0
```

is correct after two short repairs supplied below. The producer's Step 8 itself has a genuine
local-algebra gap, and its handling of GM Remark 2.1 does not by itself pin the row gauge. More
decisively for the requested headline, the frozen closure and coordinator inputs expressly leave
ROW-SWEEP/campaign-row identification provisional (`CLOS:31,155-159,196`; `CI5:55-60,96-98`).
Thus this charge cannot promote either “all campaign rows” or “exactly six msolve types” merely by
proving the conditional normal-form lemma. The six entries remain exact *AM-numerical candidate
types*, with attainment still OPEN.

## 1. Quantifiers, gauge, and target-automorphism licence

There are two different statements, and `EXHAUST:93-119` proves only the second unless a suppressed
gauge choice is made explicit.

1. For an original campaign curve `D_0`, the cage must supply an automorphism `U` and a
   normalization `nu` of `D=U(D_0)` for which `(deg P,deg Q,Delta)` has one of the displayed row
   values.
2. For a pair already presented in that gauge, EXHAUST supplies `T` with `T(D)=D_{b,c}`.

The full quantifier is therefore `for all D_0, there exist U,nu,T,a,b,c`, and the target map used
downstream is `W=T o U`. Renaming `U(D_0)` as `D` is harmless only if stated. The source-affine
map quantified at `EXHAUST:98-99` is otherwise dangling: equality of images does not mention it.
The precise parametrized conclusion should be `T o nu o a = (r^2,q)` (with the inverse convention
for `a` adjusted as necessary), or the unused source quantifier should be deleted.

The gauge issue is repairable without invoking an unspecified coordinate change. If
`nu=(P,Q)` is birational and `deg P=d>n=deg Q`, its degree-`d` homogenization maps the sole point
of `P^1-A^1` to `[1:0:0]`; hence the image has one place at infinity. A generic affine line pulls
back with degree `d`, so the projective image has degree `d`. Moreover
`[C(t):C(P)]=d` and `C(P,Q)=C(t)`, whence the irreducible implicit equation has `y`-degree `d`.
Its total degree is also `d`, so its `y^d` coefficient is constant and it can be made monic.
Thus the *original row coordinates* already satisfy GM Definition 2.3, with
`q_0=x`, `q_1=y`, values `(delta_0,delta_1)=(d,n)`, and characteristic zero. This is the missing
reason that the approximate-root delta sequence and its invariants are carried in the cage gauge.

The target-automorphism licence needed for the no-`S_4` conclusion is elementary and narrower
than `EXHAUST` §2.3. Any `W in Aut(A^2)` restricts to an isomorphism of complements, so no
campaign invariant has to survive the change of gauge. The broader claim that the transformed
curve is again a campaign branch curve is cited only indirectly to an uncharged D1-DEGREE review
(`EXHAUST:187-207`); among the four frozen inputs, `CI5:83-85` merely records that result as an
auxiliary promoted item. It is therefore not independently source-auditable here and, fortunately,
is not load-bearing (`EXHAUST:267-270`).

There is also a small determinant ambiguity. A polynomial automorphism has Jacobian in `C*`, but
that alone does not make a licence literally restricted to determinant one cover arbitrary
scalings (`EXHAUST:197-198`). If “Keller” means nonzero constant Jacobian, there is no issue. If
the campaign normalizes the determinant to one, precompose the source by a linear automorphism of
determinant `(det W)^{-1}`; the target branch locus remains `W(D_0)`. Subject to that clarification,
the Aut licence is sound.

## 2. Inventory typing and primary-source audit

GM Definition 2.2 defines
`S_{C,infinity}={-nu_{C,p}(h): h in O_C(C-{p})}`. The published Theorem 2.1 says, under its
characteristic hypothesis, that **there exists** a finite positive sequence `Delta` which generates
this semigroup and satisfies the three gcd/semigroup/strict-inequality axioms. It does not assert
uniqueness or attach an arbitrary legal sequence to arbitrary coordinates. Remark 2.1 says the
approximate-root hypotheses may be reached after a change of variables to an isomorphic `C'`, that
`S_{C',infinity}=S_{C,infinity}`, and that `delta_0=deg C'`. Theorem 2.1 and Remark 2.1 are on
internal page 4, not page 3 as recorded at `EXHAUST:53-55,570-572`; Definition 2.2 is on page 2.

Consequently `EXHAUST:488-489` does not adequately handle the caveat: semigroup invariance alone
does not preserve the first entries `(d,n)`. The fixed-gauge argument in §1 above repairs it. Once
the row `Delta` is certified as that approximate-root sequence, the strong published conclusion is
`S_D=<Delta>`, not merely `Delta subset S_D`.

The consumed links type as follows.

| Link | Exact use and audit result |
|---|---|
| GM Theorem 2.1 | Supplies `S_D=<Delta>` in the repaired row gauge. **CONFIRMED with gauge repair**. Over `C` the characteristic condition is automatic. |
| ROW-SWEEP | Supplies the row census and the assertion that the only un-killed `(6,4)` and `(8,4)` labels are `(6,4,3)` and `(8,4,6,3)`. Its elementary delta-sequence enumerations check, but its campaign pin remains **PROVISIONAL** in `CLOS:31,155-159,196` and `CI5:55-60,96-98`. `EXHAUST:522-524` incorrectly calls this promoted. |
| ROW-NF / FOLD | The old implication from the row label to a fold was provisional (`EXHAUST:156-170`). Sections 4--5 reprove it, so neither may be consumed as a black box. |
| D1-DEGREE / Aut licence | The exact prior review is not among the four frozen files. The topological corollary needs only the direct complement isomorphism, proved in §3; broader campaign invariance is redundant. |
| ROW-84 | `CLOS:35-53` independently proves, for monic `(8,4)`, `Delta=(8,4,6,3)` iff `deg(P-Q^2)=6`. The forward implication needed here is also obtained from the degree basis in §5. **CONFIRMED**, with the producer's “third proof of the equivalence” overclaim corrected there. |
| promoted ROW-KILL | `CI5:32-53` forbids the meridional transposition quotient for every displayed `D_{b,c}` and `D'_{b,c}`, `c!=0`. This is consumed at exactly that explicit-family scope, not re-proved. |
| birationality | Load-bearing, not decorative: it gives `Frac A_D=C(t)` and normalization `C[t]`, makes pole value equal polynomial degree, makes the projective degree the maximum parameter degree, and excludes `c=0`. `EXHAUST:493` lists only two of these roles. |

The two infinity deltas are correct, and genuinely have two desk-scale derivations. The clusters in
`SWEEP:119-125,275-285` give

```text
(2^7,1,1):                 delta_infinity = 7,
(4^2,2^6,1^2):  2*binom(4,2)+6*binom(2,2) = 18.
```

Independently, GM gives `S_D=<3,4>` in both cases, whose gaps are `{1,2,5}`. The normalization
colength is therefore `delta_aff=3`; the rational degree-6 and degree-8 genus formulas give
`delta_infinity=10-3=7` and `21-3=18`. No flag, physical place, or cover series is identified in
this calculation. The second route also shows that both cluster values are **unnecessary** for the
normal-form theorem: use GM equality and the gap count directly.

## 3. Transport of the \(S_4\) representation

This part is correct. Let `W in Aut(A^2)` carry the original curve `D_0` to `D_{b,c}`; in the
fully quantified version `W=T o U`. It restricts to a biholomorphism

```text
W : A^2-D_0  ->  A^2-D_{b,c}
```

and hence gives an isomorphism `W_*` on fundamental groups with the corresponding base points.
Given the allegedly forbidden representation

```text
rho_0 : pi_1(A^2-D_0) ->> S_4,
```

the transported representation is, in the correct direction,

```text
rho_{b,c} = rho_0 o (W_*)^{-1} : pi_1(A^2-D_{b,c}) ->> S_4.
```

It remains onto because both factors are onto/isomorphisms. At a smooth point of the curve, the
derivative of a holomorphic automorphism is complex-linear and invertible on the normal line. It
therefore sends a positively oriented small transverse disc to a positively oriented transverse
disc. After the usual base-path adjustment, `W_*` sends the curve-meridian conjugacy class onto
the curve-meridian conjugacy class. Thus `rho_{b,c}` sends every meridian to a transposition.
Conjugating for a base-point change is harmless because transpositions form a conjugacy class in
`S_4`. This contradicts ROW-KILL at its promoted explicit-family scope (`CI5:32-53`).

No projective closure, infinity meridian, braid basis, pencil, degree, `beta_1`, or `M_infinity`
is transported. In particular, the FALLACY-v2 target/arrival-index and flag/place/series hazards do
not enter. The same calculation with `W^{-1}` proves equivalence, not merely one implication.

## 4. The fold-forcing argument in row \((6,4)\)

Let `A=C[P,Q]`, `deg(P,Q)=(6,4)`, and `v=deg_t`. Birationality gives
`Frac A=C(t)`. Since `t` is integral over `C[Q]`, `C[t]` is the finite normalization of `A`.
For `F_mA=A cap C[t]_{<=m}`, the leading-coefficient map shows

```text
dim(F_mA/F_{m-1}A) = 1 if m is in S_D, and 0 otherwise.
```

The leaves are one-dimensional because the ambient graded piece of `C[t]` is. Hence
`dim C[t]/A = #(N-S_D)`, rigorously justifying (4.1). With `3 in S_D`, `4=deg Q in S_D`, and
`delta_aff=3`, one has `<3,4> subset S_D`; its three gaps are `{1,2,5}`, so any strict enlargement
would have fewer than three gaps. Therefore `S_D=<3,4>`. (Using the full GM conclusion gives this
equality directly and then gives `delta_aff=3`; either route is valid.)

Choose `R in A` of degree 3 and put `B=C[R,Q]`. Then

```text
<3,4> subset v(B) subset v(A)=<3,4>.
```

Applying the same filtered-leaf count to `B subset A` gives
`dim F_mB=dim F_mA` for every `m`, hence `B=A`. This is the needed justification: equality of
semigroups works here because the degree valuation has one-dimensional leaves, not as a general
unqualified subring principle. Every element of `<3,4>` is uniquely `3i+4j` with `i>=0` and
`0<=j<=2`; leading-term reduction proves that the `R^i Q^j` are a basis. Up to degree 6 the basis
is `1,R,Q,R^2`, so

```text
P = alpha R^2 + beta Q + gamma R + epsilon,   alpha!=0.
```

Completing the square and applying the displayed triangular automorphism at `EXHAUST:331-339`
puts the parametrization in the fold form `(Rtilde^2,Q)`. This proves the former FOLD statement.
After an affine source change and target scalings/translations it becomes

```text
r=t^3+bt+c,    q=t^4+q_3 t^3+q_2 t^2+q_1 t.
```

If substitution is written `t=u+mu`, the sign at `EXHAUST:342` should be
`mu=-a_2/(3a_3)`, not plus; this is only a convention-level repair. Crucially, the ring equalities
already proved give

```text
C[r,q] = C[r^2,q],
```

so there is a polynomial `H` with `r=H(r^2,q)`.

The divided-difference computation (4.5) is correct. For `e=t+s!=0`, eliminating `ts` from
`r(t)+r(s)=0` gives

```text
N(e)=-e^4-2q_3e^3+(2b-3q_2)e^2+(q_3b+4c-3q_1)e+2cq_3,
```

and `N(e)=0` gives `q(t)=q(s)` as well. The producer's treatment of the degenerate roots is not
valid: `EXHAUST:388-393` assumes `q` is a local coordinate, while `:394-397` asserts multiplicity
one without proof and falsely in general (for example `r=t^3-3t+2`, `q=t^4-4t` have order two at
`t=1`). The following replacement closes the gap.

In coordinates `(u,y)=(r,q)`, the unfolded curve lies in

```text
f(u,y)=u-H(u^2,y)=0.
```

At every point `(0,y_0)` on it, `f_u=1`. Thus this is a unique smooth graph `u=h(y)`; the
one-dimensional reduced germ of the unfolded curve contained in it equals that graph. It has one
normalization preimage and `q-y_0` is a uniformizer. Now a nonzero root of `N` is impossible:
if `t!=s` and `r(t)=-r(s)!=0`, evaluating `H` gives both `r(t)=r(s)` and
`r(t)=-r(s)`; if both are zero, two normalization preimages contradict the unique smooth graph;
if `t=s`, then `r(t)=0` and `Dq=q'(t)=0`, contradicting that `q-y_0` is a uniformizer.

Over `C`, a quartic with no nonzero root and leading term `-e^4` equals `-e^4`. Coefficient
comparison therefore forces exactly

```text
q_3=0,    q_2=2b/3,    q_1=4c/3.
```

Finally, if `c=0`, `r` is odd and both `r^2` and the forced `q` are polynomials in `t^2`; their
function field is contained in the proper subfield `C(t^2)`, contradicting birationality. Hence
`c!=0`. Birationality enters the normalization/filtration argument and this last exclusion;
characteristic zero enters division by 2 and 3 and algebraic closure enters the root argument.

## 5. Row \((8,4)\) and direct landing on \(D_{b,c}\)

For a curve already certified to have `Delta=(8,4,6,3)`, the same filtration argument gives
`S_D=<3,4>`, `delta_aff=3`, a degree-three `R`, and
`A_D=C[R,Q]` with basis `R^iQ^j`, `0<=j<=2`. The degree-at-most-eight part is

```text
1, R, Q, R^2, RQ, Q^2       (degrees 0,3,4,6,7,8).
```

Consequently the expansion (5.1) is exhaustive and `c_02!=0`. In the fixed GM approximate-root
gauge, `delta_2` is the minimum degree of `P-phi(Q)`. Terms of `phi` of degree at least three have
degree at least 12 and cannot minimize. Choosing the quadratic, linear, and constant coefficients
to cancel the three pure-`Q` basis terms leaves degree 7 if `c_11!=0`, degree 6 precisely if
`c_11=0,c_20!=0`, and at most 4 if both vanish. Since `delta_2=6`,

```text
c_11=0,   c_20!=0.
```

Completing the square in `R` and applying

```text
(x,y) |-> (c_20^{-1}(x-c_02 y^2-c_01 y-epsilon'), y)
```

therefore lands directly on `(Rtilde^2,Q)`. The normalization and repaired coefficient argument
of §4 use only degrees `(3,4)`, the ring equality, and birationality, so they yield exactly
`D_{b,c}`, `c!=0`. No octic infinity-meridian or degree-eight cover theorem is used.

Two wording repairs are required. First, `EXHAUST:445-448` is not a third proof of the *full*
ROW-84 equivalence: it assumed the four-entry `Delta` at `:420-425`. It proves the forward
implication needed here; the iff is independently established at `CLOS:35-53`. Second, the
displayed shear is `Phi_{c_02}(x,y)=(x-c_02y^2,y)`, whereas `EXHAUST:105` promises the fixed
`Phi=Phi_1`. The promise is true after writing

```text
Phi_{c_02}=Phi_{c_02-1} o Phi
```

and absorbing `Phi_{c_02-1}` into the remaining left factor. Equivalently, once `T(D)=D_{b,c}`,
`Phi^{-1}T(D)=D'_{b,c}`. Thus the `(8,4)` forward theorem lands directly on `D_{b,c}` and the
fixed-`Phi` family identification is also exact.

## 6. Audit of the three recorded repairs

- **C1 -- CONFIRMED.** The genus-three numerical semigroups containing `<4,6>` are exactly
  `<3,4>` (gaps `1,2,5`), `<4,5,6,7>` (gaps `1,2,3`), and `<2,7>` (gaps `1,3,5`). Thus the prior
  uniqueness sentence is false. The present theorem may conclude `<3,4>` only because it also
  knows `3 in S_D` (or directly because GM gives `S_D=<Delta>`).

- **C2 -- DEFECTIVE AS WRITTEN, CLOSED BY §4'S REPLACEMENT.** The producer correctly notices that
  “no nonzero minus pair” is not itself the row hypothesis and that zero-zero and diagonal cases
  require treatment. Its actual treatment assumes an unproved local coordinate and makes a false
  multiplicity-one assertion. The identity `r=H(r^2,q)` and the smooth implicit graph
  `u-H(u^2,y)=0` handle all three cases without Puiseux assumptions. With that substitution, the
  advertised forward bridge from `delta_aff=3`/ring equality to (4.6) is proved.

- **C3 -- CONFIRMED.** Once (4.6) holds, `c=0` makes both target coordinates even in `t`; the
  induced function field lies in `C(t^2)` and the map is not birational. This is exactly where
  `c!=0` enters. It is not a consequence of the semigroup or a resultant-count floor.

These are repairs of algebra and typing, not new exit-price assertions.

## 7. Corollary dependency list

The five-item list at `EXHAUST:484-495` is neither minimal for its displayed conditional corollary
nor complete for the broader campaign/exact-six conclusion.

For the conditional statement about curves *already carrying* one of the two specified delta
sequences, a minimal dependency list is:

1. GM generation in the fixed gauge, plus the standard birational-normalization and
   one-dimensional degree-filtration facts;
2. the elementary fold/normal-form proof of §§4--5, including the repaired implicit-graph step and
   the birational exclusion `c=0`;
3. the promoted explicit-family ROW-KILL at `c!=0`;
4. the elementary ambient-automorphism transport of §3.

The recorded `delta_infinity` values (producer item 2) are corroboration, not a dependency, if the
full GM equality is used: `S_D=<3,4>` already gives `delta_aff=3`. Conversely, if one deliberately
uses only `Delta subset S_D`, the infinity values are needed; the proof must choose one route.
The D1 campaign-invariance licence (item 4) is unnecessary for nonexistence on the original
complement. Birationality is not a freestanding cited theorem but is a hypothesis with all the
roles listed in §2. Theorem FOLD, ROW-NF, nodality, `Phi` transport, M-INF, and FIXED-TUPLE are
indeed not used in this conditional lemma.

To infer the headline “every campaign residual curve in rows `(6,4)/(8,4)`,” one must additionally
have: the D1 cage and its initial gauge automorphism; a complete, promoted ROW-SWEEP pin saying
that the only survivors in those rows have precisely these delta sequences; and the preceding
M-INF eliminations of the other row labels. Those are absent from the five-item list. Worse, their
status is contradicted inside the frozen record: `CLOS:31,155-159,196` says ROW-SWEEP remains
provisional, `CI5:55-60,96-98` repeats that campaign-row exhaustiveness is not promoted, while
`EXHAUST:522-524` calls the census promoted. This review validates the relevant elementary
delta-sequence enumeration, but the charged set does not contain the D1/M-INF primary proofs
needed to re-gate the entire sweep. A status label cannot be upgraded by implication.

The six entries at `EXHAUST:535-540` do exactly match the unresolved numerical ledger in
`SWEEP:372-377,447-458,469-471`: four `(8,6)` and two `(9,6)` AM types. But `SWEEP:27-32,
356-362,433-438,476-487` expressly withholds nodal attainment. Therefore the safe conclusion is:

```text
conditional on a separately promoted full cage/sweep, the unresolved ledger consists of
exactly six AM-numerical candidate types, each still OPEN for realization/exclusion and S4 routing.
```

It is not “six realized residual curves,” and the phrase “exactly six msolve types” is licensed
only if “type” means these unresolved numerical decision cases and the coordinator's stated exact
two-engine msolve rule is also retained (`CI5:73-76,99-100`).

Two non-load-bearing overclaims should also be deleted. The two killed rows form corresponding
families/unions of Aut-classes, not “one geometric class” (`EXHAUST:530-531`): different moduli
even have different affine singularity types (`CLOS:145-153`). And the successor claim that
exactly two of the six types have a generator below `n` (`EXHAUST:551-558`) is false:
`<4,6,9>` for `Delta=(9,6,4)` also has `4<6`. Neither error affects the conditional exhaustiveness
proof, but neither belongs in a promoted report.

## 8. Promotion recommendation

**REFUSE promotion of the charged report and its full-campaign corollary as written.** This is not
a counterexample to the normal-form theorem. It is a split verdict:

- **PROMOTE-AS-CORRECTED** the fixed-gauge conditional theorem for curves certified to have
  `Delta=(6,4,3)` or `(8,4,6,3)`. Before promotion, insert the GM fixed-gauge argument, replace
  Step 8 by the `u-H(u^2,y)` implicit-graph proof, correct the source-translation sign/convention,
  trim the “third iff proof” wording, and display the fixed-`Phi` factorization. After those exact
  repairs, the fold, `c!=0`, direct octic landing, and meridional `S_4` transport are rigorous; no
  algebraic obligation in EXHAUST itself remains OPEN.
- **DO NOT PROMOTE** “every campaign `(6,4)/(8,4)` residual is covered” on this frozen basis.
  State it conditionally until the D1 cage/ROW-SWEEP campaign pin is separately promoted. Correct
  the dependency list and the conflicting status sentence.
- **DO NOT PROMOTE** an unqualified “N=4 residual is exactly six msolve types.” Conditional on the
  full promoted sweep it is exactly six *unresolved AM-numerical candidate types*; existence and
  the noncoprime `S_4` route remain OPEN. Remove the false “one geometric class” and successor
  observations.

Accordingly, the requested upgrade to full campaign scope fails this gate, while its central
desk-scale algebra is salvageable by the explicit proof replacements above.

<!-- BODY-END -->
