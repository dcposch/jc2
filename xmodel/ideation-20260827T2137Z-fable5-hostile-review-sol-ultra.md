# Hostile independent review — Fable5 coherent compression and lower transfer

Date: 2026-08-27  
Reviewer: Sol Ultra  
Charged report: `xmodel/ideation-20260827T2137Z-fable5.md`

## 0. Custody and headline verdict

I verified the charged artifact before reading it:

```text
edd383ad33838268cc7e700f2aa913dab73eb6744a60133a131a69eb7ef476bb
```

The two mandatory post-seal review inputs are:

```text
0e09faeb69480b7594864199fbd061291af490cf8e514d1795784fbf00ad9bee
  xmodel/ideation-20260827T2137Z-postseal-truth-delta.md
0ccdc259358267fc805c2af477bc6b0f48620dbd2e76c016cdb85caee1ba3cba
  xmodel/ideation-20260827T2137Z-opus5-hostile-review-sol-ultra.md
```

**Headline verdict: CONFIRM the gauge identity and its localized receiver
periodicity; REPAIR the proposed algebraic sector assembly; REFUTE the Krull
argument as a finite-bound argument, the asserted rational-pairing route as
proved, the lower `29 versus 36` inference, and the claim that the lower
characteristic tower stops at raw row 40.**

The central distinction is the one established in the reviewed Opus torsor
audit: four periodic finite-dimensional receiver spaces are not a finite list
of row maps. Fable proposes a potentially useful way to package the repeated
row maps, but does not construct the package or an effective order. The exact
lower conjugacy also has a resonance omitted by Fable: for target
`Etilde=-tau^17`, the relevant algebraic series is `P^(-3)`, and its `n=3`
coefficient (raw row label 20) is multiplied by zero rather than furnishing a
two-dimensional gate.

| Charged item | Verdict | Narrow repair |
|---|---|---|
| `T_m(HY)=H T_(m+4)(Y)` and cokernel direction | **CONFIRMED** | It gives `coker T_(m+4) -> coker T_m`, `[f] -> [Hf]`. It is an isomorphism only after `H` is a unit. |
| “One module, not an unbounded list” | **REPAIR** | One periodic list of localized receivers; still infinitely many nonlinear row maps and non-periodic frozen windows. |
| Coherent/algebraic sector section | **GAP/REPAIR** | Algebraicity is plausible and can be constructed from the already-known `Q=P^2` by four-section extraction. R7R2 regular holonomicity and the `q2` sample do not perform that construction. |
| `q2`/square-root evidence | **INSUFFICIENT** | The coincidence holds at `q2`; the exact `q3` mismatch has coefficient ratios `1, 3/4, 11/16`, so it is not a sector formula. |
| Krull gives finite determination | **REFUTED AS ARGUED** | Krull separation gives no uniform prefix order. Noetherian stabilization of the coefficient ideal can give non-effective existence after the coefficient ring and section are actually defined. |
| Rational residue pairings and effective `N0` | **NOT ESTABLISHED** | Algebraic sections pair algebraically, not automatically rationally; Galois trace can annihilate a nonzero section. An explicit norm/coordinate construction and degree bound are missing. |
| Novelty of the explicit gauge formula | **NEW-TO-BASELINE, NOT UNIQUE** | I found no earlier explicit operator display, but Opus independently sealed the same gauge identity in this round. Earlier work already stated gauge-equivalent representatives and warned that polynomial windows change. |
| Lower-face transfer | **KNOWN SELF-REPEAT / NEW CLAIMS REFUTED** | Fable's own 18:08 report already connected the upper transfer to `4Kg'-3K'g`. The current full-row schedule and finite-tower conclusion are wrong. |
| Lower `29` conditions | **REFUTED** | In rows 18--40 the corrected F-side receiver budget is 27 after removing resonant row 20, and it is only a finite prefix of an infinite transformed tower. |
| `29` versus 36 predicts LF40 proper/unit | **REFUTED** | Receiver dimensions are generator ceilings, not independent equations; the gates are F-side, whereas the 36 counted slots are G-side and not free after the earlier rows. |
| Prefix-unit principle | **CONFIRMED** | A replayed unit of a literal subset lifts to the full ideal. Proper subsets are silent. |
| Prefix ladder as designed | **REPAIR** | Put all 18 affine `D22` generators in rung one, never stop after proper subset outputs, and replay a unit against the authoritative 513-generator manifest. The held 466-generator object already generates the full ideal. |
| `C74-PLACE -> EXIT-RPMC(C)` route | **DELETE** | Post-seal source review refutes the physical-other-chart reading and shows `EXIT-RPMC(C)` is the old `RPMC(C)` under its exit premise. |

## 1. Exact gauge identity: what it proves and what it does not

Put

```text
T_m(Y)=4H Y' + (m-12)H'Y.
```

Direct expansion gives

```text
T_m(HY)
 = 4H(H'Y+HY')+(m-12)H'HY
 = H(4HY'+(m-8)H'Y)
 = H T_(m+4)(Y).
```

Therefore multiplication by `H` induces, in the stated direction,

```text
coker(T_(m+4)) -> coker(T_m),       [f] |-> [Hf].
```

On `K[X,H^-1]`, multiplication by `H` is invertible and
`T_(m+4)(H^-1Y)=H^-1T_m(Y)`, so this is an isomorphism. This exactly matches
the gauge relation for `nabla_(m+4)` and `nabla_m`, and composes with the
reviewed Opus torsor theorem: one four-character target direct sum is the
cohomology of the geometric Kummer torsor.

It does not follow that the polynomial cokernels or the D3 polygon-window
cokernels are isomorphic. The inverse uses `H^-1`. A minimal exact example is
`H=X` over `K[X]`:

```text
T_12(X^k)=4k X^k,       coker_K[X](T_12)=K.[1],
T_16(X^k)=4(k+1)X^k,   coker_K[X](T_16)=0.
```

After localizing at `X`, the missing `X^-1` mode restores the one-dimensional
row-16 cokernel and multiplication by `X` carries it to `[1]`. Thus the
localized statement is exact and the polynomial statement is false in
general.

The campaign already has a fixture-level version of the same warning. In the
reviewed 18:08 gate audit, integer-shifted representatives of the branch-P
row-22 class gave different polynomial/pole-window codimensions, including a
vacuous presentation versus the seven-dimensional polynomial `M(Y)`
presentation. For a frozen window there is an additional problem:
multiplication by degree-eight `H` need not even carry the later row's source
and target windows into the earlier row's windows. That inclusion must be
checked row by row from the polygon.

The promotable conclusion is therefore:

> Rows in one residue class have gauge-isomorphic localized de Rham receiver
> spaces. Their polynomial presentations, allowable pole orders, polygon
> windows, and nonlinear maps from the frozen coefficient scheme need not be
> periodic.

This agrees with, rather than strengthens beyond, the reviewed torsor audit.
The torsor theorem gives a per-period target-space budget; it gives no row
independence, realized codimension, collapse order, or finite decision bound.

There is also a branch-P component qualifier. For `H=A^2`, the full
degree-four torsor is disconnected, while R7R1 selects one quadratic field
component. Four-character bookkeeping is valid after geometric base change
on the full torsor, but the selected field does not literally carry all four
deck automorphisms. Fable's “sector characters cycle” must retain this
qualifier.

## 2. The proposed algebraic sector section

### 2.1 The `q2` sample does not construct it

R7R1 already supplies the correct algebraic generating function:

```text
P^8=F(X,sP),       Q=P^2=sum_(n>=0) q_n s^n.
```

The equality

```text
[t^2] (1/2)sqrt(F)=F2/(4H)-F1^2/(16H^3)=q2
```

is correct. It is an accidental low-order agreement in the original `t`
coordinate, not a construction of any of the four `s`-sector series. The
already-derived exact next coefficient is

```text
q3 = p^5 [ F3/(4H^2)
            - 3 F1 F2/(32H^4)
            + 11 F1^3/(512H^6) ].
```

Meanwhile

```text
p [t^3](1/2)sqrt(F)
 = p [ F3/(4H) - F1F2/(8H^3) + F1^3/(32H^5) ].
```

After using `p^4=H`, the three termwise ratios are

```text
1, 3/4, 11/16.
```

Fable records only the first two as a negative control. The third confirms
the same failure. More importantly, a failed square-root guess is not
evidence that “each sector has its own” unspecified closed form.

### 2.2 A plausible exact repair exists, but is absent from the report

After adjoining `mu_4`, let `zeta` be a primitive fourth root and extract the
ordinary four-sections of the known algebraic `Q`:

```text
Q_a(X,s)=(1/4) sum_(ell=0)^3 zeta^(-a ell) Q(X,zeta^ell s)
          =sum_(k>=0) q_(a+4k)(X) s^(a+4k).
```

Mapping every later receiver to the first receiver in its sector uses the
confirmed cokernel direction and produces coefficients
`H^k q_(a+4k)`. Thus the candidate fixed-receiver series is

```text
Gamma_a(X,z)=sum_(k>=0) H^k q_(a+4k)(X) z^k.
```

Equivalently, it is obtained from `s^(-a)Q_a(X,s)` after the algebraic
substitution `s^4=Hz`. This shows why an algebraic sector package should be
available after a finite base change. It also shows that R7R2's separate
regular-holonomicity theorem for `P,W` is not the missing construction: the
algebraicity needed here already comes from `Q=P^2`, and one must still:

1. fix the exact character/clearing convention;
2. map every coefficient into one localized de Rham quotient;
3. define the relative quotient over the coefficient stratum;
4. prove compatibility with specializations and with the chosen field
   component; and
5. reconcile that localized section with the frozen polynomial windows.

None of these five steps is carried out in the charged report. In particular,
“a section `gamma_j(s)` of the coherent module `M_j`” is introduced without a
base ring, a module presentation, a formula such as `Gamma_a`, or a map from
the R7 coefficients.

Algebraicity of `P,W` and regular holonomicity of their cyclic surface
`D`-modules do not by themselves imply that the desired relative de Rham
module is locally free on the stated prefix-survivor scheme. An integral base
does not make an arbitrary coherent module torsion-free. Generic freeness can
supply a smaller open locus; every discarded discriminant/torsion locus then
requires a separate finite stratification.

The card's proposed FAIL interpretation is also wrong. Failure of Fable's
particular assembly would not discover “transcendental tower content”:
`Q=P^2` is already algebraic. It would diagnose a bad sector projection,
clearing convention, or relative-cohomology construction.

## 3. Krull separation is not an effective determinacy theorem

The charged argument says that if every coefficient vanishes then
`gamma_j` belongs to `intersection_N s^N M_j`, which is zero by Krull, and
concludes that finitely many rows decide all rows. The first implication is
formal equality of power series; Krull is not needed. The conclusion does
not follow from the intersection statement.

The elementary countermodel is

```text
M=K[[s]],       gamma_N=s^N.
```

The module is torsion-free over an integral complete local ring, every
`gamma_N` is algebraic, and `intersection_r s^rM=0`. Nevertheless the first
nonzero coefficient can occur at an arbitrarily large `N`. Krull separation
does not make the descending chain `s^rM` stabilize and supplies no uniform
order.

For one fixed section, nonzeroness has some finite order. For a family, the
correct non-effective argument is different. Once all class coordinates
`a_0,a_1,...` are proved to be regular elements of a specified Noetherian
coordinate ring `A`, the ascending coefficient ideals

```text
I_N=(a_0,...,a_N) subset A
```

stabilize. Then some finite prefix cuts the same scheme as all coefficients.
This is the Noetherian observation already recorded in the reviewed 18:08
gate audit. It gives neither a computable `N0` nor a uniform bound across
unproduced strata. Localization at the discriminant proves a statement only
on that open locus; it cannot be followed by the word “then integrality” to
recover the omitted closed locus.

### 3.1 The proposed rational-pairing repair is not proved

Even after constructing `Gamma_a`, pairing an algebraic section with an
algebraic dual section normally gives an algebraic function of `s`, not a
rational one. Regular holonomicity implies finite differential equations; it
does not imply rational solutions. The scalar example

```text
c(s)=sqrt(1+s)
```

is algebraic and regular holonomic but not rational. Galois symmetrization is
not automatically detecting: the trace of this nonzero section to `K(s)` is
zero. A norm is rational and detects a nonzero field element, but is nonlinear
and requires the finite extension, all embeddings, denominators, and degree
bounds to be explicit.

There are further missing pairing details. On an affine curve the natural
perfect duality involves the dual connection and compact supports/boundary
conditions; a “Galois-symmetrized basis of algebraic sections of the dual
module” is not produced. A trace of a basis need not remain a basis. A
resultant can provide a degree bound only after an explicit algebraic equation
and a denominator nonvanishing at the expansion point are pinned.

Thus no effective `N0` is established. The cheapest valid successor is not
another `q2` comparison. It is:

1. write the exact `Gamma_a` for one frozen branch-P stratum;
2. verify its coefficients through at least `q3` and one full sector return;
3. reduce it into an explicit fixed de Rham basis;
4. derive an annihilating recurrence or algebraic equations for every class
   coordinate;
5. prove the recurrence leading coefficient is a unit at `s=0`; and
6. print the resulting numerical prefix bound and replay every row through
   it.

Until that is done, Card 1 is a worthwhile research program, not a tower-
capacity theorem or a converter from endpoint verdicts to family verdicts.

## 4. Exact lower conjugacy, offset, and resonance

The lower transfer must be rederived from its target exponent; copying the
upper `P^2` tower is invalid. Use the same confirmed R7 change of variables

```text
F=P^8,       G=P^12 W,       s=tau/P.
```

The algebraic conjugacy is

```text
Etilde=8P^21 J(s,W),       J(s,W)=-s_tau W_xi|s.
```

For the lower Keller target `Etilde=-tau^17=-s^17P^17`, this gives

```text
W_xi|s=(s^17/8) P^-4(P+sP_s)
       =(s^17/8)(Q-(s/3)Q_s),       Q=P^-3.
```

Writing `Q=sum_(n>=0) q_n s^n` yields the exact coefficient law

```text
w_(n+17)' = (3-n) q_n / 24.                 (L)
```

This calculation fixes all three points left open in Fable's Card 2:

1. **Licensing.** For `n != 3`, exactness of `q_n dxi` is a necessary
   F-side gate. At `n=3`, equation (L) is only `w_20'=0`; it gives no
   exactness condition on `q_3`. Raw row label 20 is resonant, not a
   two-dimensional gate.
2. **Character/row label.** `q_n` has character `n-3`, congruent modulo four
   to `m=n+17`. Thus the receiver dimension schedule
   `1+[4|m]` is correct for the nonresonant rows.
3. **Operator offset.** The direct representative is

   ```text
   4Kc'+(n-3)K'c = T_(m-8)(c),       m=n+17,
   ```

   not `T_m(c)`. The two are related only by the gauge

   ```text
   T_(m-8)(K^2Y)=K^2T_m(Y).
   ```

   That multiplication/division by `K^2` is precisely where polynomial
   windows can change.

At `n=0`, the direct connection is `nabla_-3`; after the campaign's scaling
it is the reviewed endpoint ODE

```text
4Kg'-3K'g=4K.
```

For `K=xi(xi-rho)^7`, its residues `-3/4,-21/4` are both nonintegral and its
localized `H^1` dimension is indeed one. This anchor is consistent. It does
not validate the copied all-row schedule or a polynomial-window map.

### 4.1 Raw row 40 is not the end of the transformed tower

`F` and `G` have finite raw `tau` support, so the determinant coefficient
system `Dtilde_0,...,Dtilde_40` is a complete finite polynomial system. That
does not make `Q=P^-3` a polynomial in `s`. The formal inverse
`tau=sP(X,tau)` generally gives infinitely many nonzero coefficients, exactly
as bounded upper raw support failed to truncate `P^2` in the reviewed R7
audit. Because `Etilde=-tau^17` is an exact identity, equation (L) holds for
every `n>=0`, including transformed labels above 40.

Thus two different statements must remain separate:

- LF40 itself is a finite full `(F,G)` ideal because the raw determinant has
  no coefficients above 40;
- eliminating `G` through the characteristic change produces an infinite
  algebraic F-side gate sequence, with one resonance at label 20.

Fable's sentence “rows beyond 40 vanish identically, so no infinite-tower
issue” repeats the bounded-support error already refuted for the upper face.

### 4.2 Correct finite-prefix arithmetic and why it predicts nothing

For multiplicities `(1,7)`, `r=2` and

```text
h_m=dim H^1(U,nabla_m)=1+[4|m].
```

If one temporarily truncates to labels `18,...,40`, summing all receiver
dimensions gives Fable's `23+6=29`. But label 20 is unlicensed and has
`h_20=2`. The corrected nonresonant prefix budget is therefore

```text
sum_(18<=m<=40, m!=20) h_m = 29-2 = 27.
```

Including the inhomogeneous endpoint label 17 adds one, giving 28 through
label 40. Neither number is a total-tower count because labels 41 and above
remain licensed.

Even `27` is only the number of coordinates available in the localized
receivers. It is an upper bound on the number of scalar F-side gate
generators, not their height or independence. The same nonlinear `F`
coefficients occur in every row. Restricting primitives to the frozen
polynomial windows can add obstructions and destroys the gauge periodicity.

The comparison with `36=8+28` is category-invalid:

- the 36 slots are `G_17,...,G_24` slots;
- the `q_n` are F-side conditions obtained after formal `G` elimination;
- row 17 and all previous rows already consume/couple those G handles;
- labels 25 and above have no new raw G block and are nonlinear conditions on
  accumulated variables; and
- the actual localized LF40 ideal has 409 variables and 741 equations, with
  740 determinant generators, not a 36-variable linear incidence problem.

Consequently `29<36` (or corrected `27<36`) gives no lower bound on LF40's
solution dimension and no proper-versus-unit prediction. A row-by-row linear
ledger can still be a useful compiler checksum for the new-block maps at
labels 18--24, provided it uses `P^-3`, omits label 20's F-gate, and compares
literal polygon windows. It cannot validate the terminal ideal or turn a
rank discrepancy automatically into a new coupled connection.

## 5. Novelty audit

The novelty labels need three repairs.

1. A targeted search found no pre-round display of
   `T_m(HY)=HT_(m+4)(Y)`. It is a clean new explicit formula relative to the
   sealed baseline. Opus independently sealed the equivalent gauge identity
   in the same 21:37 round, and the reviewed torsor audit confirmed it. It is
   therefore not a unique Fable contribution.
2. The broader algebraic-recursion route predates this report. The reviewed
   R7 audit already proposed an eventual finite algorithm from the algebraic
   equation, Hermite reduction, and a certified recurrence in the finite
   de Rham quotient. The reviewed 18:08 gate audit already used Noetherianity
   to say that some finite subset suffices, without a bound. Fable's new part
   is the proposed one-section implementation and effective degree target,
   not the existence of a finite-type research route.
3. The lower transfer is not new. Fable's own
   `ideation-20260827T1808Z-fable5.md`, section 3b, explicitly says that the
   lower `Dtilde_17` transfer reduces to `4Kg'-3K'g` and calls the upper and
   lower endpoints two instances of one transfer principle. The current
   novelty search excluded the individual 18:08 reports and therefore missed
   its own predecessor. The `r=2` arithmetic and proposed LF40 ledger are new
   additions, but the former is mislicensed and the latter remains a design.

Relative to Opus, Fable's genuinely distinctive contribution is the attempt
to package the infinitely many maps into an algebraic fixed-receiver section
and seek an effective recurrence/zero-recognition bound. Opus supplied the
topological four-receiver capacity theorem and correctly left finite
determination open. Fable names a plausible next object beyond that theorem,
but supplies no theorem about it. This is significant ideation value, not
promotion evidence.

## 6. Prefix-unit ladder: exact logical scope and custody repair

The monotonicity principle is exact. If literal generator sets satisfy
`S subset T`, then

```text
1 in (S)  =>  1 in (T).
```

A cofactor certificate against `S` can be zero-padded to a certificate
against `T`. Properness goes in no useful direction: `(S)` proper says
nothing about `(T)`.

The held upper object must be described more precisely than “top rung below
full.” The authoritative affine raw ideal has 303 variables and 513 literal
generators. The held object retains 466 of those original generators,
including every `D7,...,D22` generator and all 18 affine `D22` target
coefficients. Exact cofactor replay expresses the other 47 raw generators in
the retained ideal. Hence the held 466-generator ideal is algebraically
**equal** to the 513-generator ideal, not merely a proper prefix of it.

Custody pins are:

```text
8e25502c5f8e7b7397d1799f0502fc3088fd0cb8d3425b832b31aa3cd902b611
  held 466-original-generator system
afd9565d128417924cb74c46a306bf8d72136a51e2e4f13f695d859eea9837fa
  held Singular input
324f4293a8fae7baab2632f89d1274dc1b880a8708f34c2348e46a7f4fe915b7
  current hardened full source manifest
```

Fable's sample rungs “through D14” and “through D18” omit the only affine
target unless all 18 `D22` generators are added separately. Such homogeneous
prefixes contain the origin and are guaranteed proper, so they cannot return
UNIT. The proposed stop after two proper rungs would then abandon the ladder
before its first informative affine rung. Post-seal custody has already made
the correct repairs:

- include all 18 `D22` target generators from rung one;
- use nested literal subsets of the pinned 466 original generators;
- treat every proper subset output as silent and never stop merely because
  two subsets are proper;
- for UNIT, retain tracked exact-Q cofactors and replay/zero-pad them against
  the authoritative 513-generator raw manifest; and
- for PROPER, retain the campaign's required complete 303-coordinate rational
  raw witness/replay.

These are logical corrections only. This review does not recommend launching
another lane, and took no AWS action.

## 7. Post-seal G2 and finite-end corrections

The post-seal delta invalidates the report's top proof route and Card 3's
placement dependency. Corollary 7.4 is same-edge native content, VGG minimal
re-selection is chart-rigid, old `C74-PLACE` splits into separate L1--L5
obligations, and `EXIT-RPMC(C)` is equivalent to existing `RPMC(C)` once its
own exit clause is assumed. Delete the claimed
`C74-PLACE -> EXIT-RPMC(C)` physical-other-chart corridor. Do not relabel it
as a repair.

The finite-end identity itself is confirmed:

```text
sum_S e_S = td+b1-1.
```

Its one-sided use survives only with typed marked data. A partial sum can
refute a forest if every included term is proved to be a distinct marked end
with the correct multiplicity and the right-hand invariants belong to that
same generic fibre. Without a leaf/place injection, duplicates can manufacture
a false excess. Passing certifies nothing.

The passport claim is too strong as written. Pole degrees and local `e_S`
data do not automatically specify how cycles are grouped over branch values,
and ordinary passports lose the marking on `e=1` fixed ends. Braid orbits are
on branch values, not sheet blocks. The reviewed marked-component refinement
prunes the clean residue-A census `169 -> 48` and kills none of the 48. Thus a
marked partial-budget validator remains useful after a place dictionary; a
full branch-cycle CSP does not yet follow from the decorations claimed in
Fable's card.

## 8. Narrowest promotable results

### 8.1 Gauge-receiver lemma

> For `T_m(Y)=4HY'+(m-12)H'Y`, multiplication by `H` induces
> `coker T_(m+4) -> coker T_m`, `[f] -> [Hf]`. It is an isomorphism over
> `K[X,H^-1]`. No polynomial-window isomorphism follows without explicit
> degree/pole-window checks.

### 8.2 Lower characteristic licensing lemma

> Under the confirmed R7 change `F=P^8`, `G=P^12W`, `s=tau/P`, the exact
> lower target `Etilde=-tau^17` gives, for
> `P^-3=sum q_n s^n`,
> `w_(n+17)'=(3-n)q_n/24`. Hence every `q_n dxi` with `n!=3` is a necessary
> exactness class, while `n=3` is resonant and supplies no F-side class. The
> direct row-`m=n+17` operator is `T_(m-8)`; conversion to `T_m` multiplies
> the primitive by `K^2` and is only gauge-equivalent after localization.
> Finite raw determinant support through 40 does not truncate this transformed
> series.

### 8.3 Prefix-unit lemma at the held object

> A tracked exact unit certificate for any literal subset of the 466 retained
> original generators, replayed and zero-padded to the authoritative raw
> manifest, proves the 513-generator affine ideal is unit. A proper subset
> result proves nothing about the full ideal. The replayed 47 omission
> identities make the held 466 ideal equal to the full 513 ideal.

No coherent-compression theorem, effective `N0`, lower finite-capacity
theorem, LF40 proper/unit prediction, physical-other-chart corridor, or full
passport theorem is promotable from the charged report.

## 9. Precise errata and cheapest discriminators

| Location | Required erratum | Cheapest decisive next test |
|---|---|---|
| §3.1.1 | Replace “row cokernels are one module” by localized receiver periodicity; retain polynomial/window warning. | For one branch-P sector, print the actual source/target windows at `m,m+4` and test the `H` maps. |
| §3.1.2 | Delete the square-root assembly inference and use `Q=P^2` four-section extraction. | Construct `Gamma_a`; match `q0..q7`, including exact `q3`. |
| §3.1.3 | Delete the Krull-to-`N0` implication and unproved rational-pairing claim. | Produce explicit coordinate equations or a recurrence with leading coefficient a unit at zero and a numerical order bound. |
| Card 1 FAIL semantics | Failure of the proposed package is not transcendence. | Compare the failed step directly with the algebraic equation for `Q`. |
| §3.3/Card 2 | Replace copied `P^2` schedule by `P^-3`, omit resonant label 20, record operator offset `m-8`, and retain labels above 40. | Derive labels 17--24 symbolically and compare the literal raw new-block maps; no terminal prediction. |
| Card 2 arithmetic | Replace 29 by 27 only as the nonresonant 18--40 receiver prefix; delete comparison with 36 and all proper/unit language. | Compute realized Jacobian ranks on an already-known exact point only as non-decisive telemetry. |
| §6 | Add all 18 affine targets to every rung; delete the “two proper” stop; call 466 full-ideal-equivalent. | If the existing lanes cap, replay the first all-affine literal subset against manifest `324f4293...`; no homogeneous rung. |
| §§2,3.2,5,Card 3 | Delete `C74-PLACE -> EXIT-RPMC(C)` and require a marked place dictionary before the partial validator. | On one complete exact-pair forest, verify injective leaf-to-marked-end IDs and the confirmed finite-end equality. |

## 10. Evidence and scope firewall

Checks performed for this review:

1. Verified the charged SHA-256 and hashed both mandatory post-seal inputs.
2. Read all three charged/mandatory reports in full.
3. Hand-expanded `T_m(HY)` and checked the induced cokernel direction and
   localized inverse; checked the polynomial counterexample `H=X`.
4. Re-derived the exact `q3` formula comparison and all three ratios.
5. Re-derived the lower R7 conjugacy from `Etilde=-tau^17`, including
   `Q=P^-3`, coefficient `(3-n)/24`, resonance `n=3`, character congruence,
   and operator offset `T_(m-8)`.
6. Recounted the lower prefix budget: `29-h_20=27`.
7. Read the reviewed R7/R7R2 source audits, the prior gate/window review, the
   NU17 lower-face review, the LF40 family/compiler custody, and the held
   prefix-quotient preregistration/verifier at their relevant sections.
8. Verified the current hardened full source-manifest hash and checked the
   literal counts `303/513/466/47/18` from the independent quotient verifier.
9. Ran targeted novelty searches for the gauge identity, finite
   determination, residue pairing, lower transfer, and prefix monotonicity.
   The prior Fable 18:08 lower-transfer statement and the prior R7
   algebraic-recurrence proposal are charged against novelty.

I did not run a CAS, heavy local computation, or AWS action. I did not enter,
list, search, read, build, or modify `jc2-lean`. I did not edit a canonical
ledger or any file other than this report. All statements about LF40 beyond
the displayed conjugacy are logical audits of existing reviewed artifacts,
not a solver result. No finding here is a Keller-pair existence/exclusion,
family landing, counterexample, or JC2 result.

Report path:
`xmodel/ideation-20260827T2137Z-fable5-hostile-review-sol-ultra.md`

