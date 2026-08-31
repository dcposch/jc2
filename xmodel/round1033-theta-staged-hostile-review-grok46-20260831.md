# Hostile review: THETA-STAGED (Sol) — is `OPEN[THETA-STAGE0-MARKED-SNC]` right?

Date: 2026-08-31
Reviewer: Grok 4.6, different-model expert referee
Charge: fail-closed Stage-0 verdict of the frozen THETA-STAGED report
against the two promoted one-cusp packets and the synthesis launch note.
No other file, ledger, or `jc2-lean` inspection. No CAS.

## Verdict

**OPEN CONFIRMED.** The charged pullback is not explicit in the two
packets; no admissible marked SNC representative is present; no unique
horizontal source vertex is typed. A wrong OPEN would have been a
finite derivation of `P_f,Q_f,P_g,Q_g`, of an equation of `B`, or of a
complete divisorial pole ledger. No such derivation exists.

The reopen list is **sufficient for Stage 2** and **amended on
necessity**: minimality and uniqueness of a lift of `q_infty` are
protocol-level, not required to evaluate `Theta_h` from (0.3). The
missing ring map is independently fatal, so the amendment does not
reopen the lane from frozen data.

Transformation law (0.4) is proved; `d_h` as in (0.3) is model-free.
The reading of (1.12)--(1.14) as generic-point-only matches the
structure packet. Chart (0.2) is source-side and cannot be reused as
`(f,g)`.

---

## 0. Custody

Frozen copies hashed on this host before reading; all four match the
charge:

```text
1cf8f9d75e17efd2fc5d43861d721a1eb3b3c0d468e93c75d571f875576012fb  round1033-theta-staged-sol56-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  ideation-20260831T1033Z-synthesis.md
```

Line cites below are to these copies, abbreviated `report`,
`structure`, `connectedness`, `synthesis`. Parent packets named by
`structure` (Poisson, function-pair, Kummer, cyclic) were not opened.
No canonical ledger was read or edited.

Notation. `R=C[A,U,Z]/(U^2-A-A^2Z)`, `S=Spec R`, `K=Frac(R)`,
`pi=(f,g):S->A2` with `{f,g}=kappa in C^*`, `Phi=V(A,U)`, `B` the
charged singular irreducible target branch, `beta_B:A1->B` its
normalization. `h` is one of `f,g` and `k` the other.

---

## 1. Hunt: does frozen data pin `(f,g)` or a marked SNC model?

**No.** Every candidate that could have refuted the OPEN was checked.

### 1.1 Explicit images in `R`

The unique normal form of an element of `R` is `H=P_H(A,Z)+U Q_H(A,Z)`
(`structure:145-149`). That is a normal-form statement, not a value of
`(f,g)`. The jets along `Phi`,

```text
f=f_0(Z)+f_1(Z)u+O(u^2),     g=g_0(Z)+g_1(Z)u+O(u^2),
```

are names (`structure:164-180`). The unimodular identity
`2(f_1 g_0'-f_0' g_1)=kappa` and the constraints `deg f_0,deg g_0>=2`
(neither coordinate affine, immersive normalization `Phi->C_0` with a
double point) restrict jets; they do not name four polynomials.
PROVISIONAL non-local-finiteness (`structure:150-162`) only excludes
`H in C[A]`.

The connectedness packet never displays `f` or `g`. The line `f=P(t)`
(`connectedness:205`) is the inner hypothesis of a contradiction
(`delta_f>1` forces a polynomial subring, then `P'(t)` is a unit, then
`deg P=1`). The conclusion is `C(f)` algebraically closed in `K`, not
an identification of `f` with a named element.

No tuple `P_f,Q_f,P_g,Q_g` occurs as a value in either packet.

### 1.2 Equation of `B` and `beta_B`

`structure:250` is definitional: “Let `b(f,g)` be a reduced irreducible
equation of `B`.” No polynomial `b` is written. The census
(`structure:387-396`) supplies fibre types `(2,1,1)` / `(3,1)` /
`(2,2)`, irreducibility, and `beta_B:A1->B`, still without an equation
or a parametrization. Inverse-Kummer data (`structure:473-557`) name
`c_0,E,r_E,kappa_B` without polynomials. The cyclic replacement
`H_cyc=pi o f_2` and `D_B=V(b o H_cyc)` (`structure:559-573`) compose
the missing `pi` with the chart; they do not supply `b`.

`OPEN[CENSUS-EXHAUSTIVITY]` (`connectedness:447-450`) further blocks
recovering `B` as “the” ramified boundary image of `Y->A2`. Even given
that, a census of fibre types is not an equation.

### 1.3 Divisorial pole ledger

What is present is not a ledger for poles of `f` and `g` on a
compactification of `S`:

- interior: `ord_P(U)=1`, `ord_P(A)=2`, `ord_P(Z)=0` on `Phi`
  (`structure:90-93`), a divisor inside `S`;
- generic ramification: (1.12)--(1.15) at the generic point of `B`,
  where `f` and `g` remain finite (they are the finite morphism's
  coordinates on `Y`);
- fibre formula (2.1) on `Cbar_h`, in unknown `e_p,Sigma_infty,Sigma_fin`;
- (3.1)--(3.5): `s_fin=d_h` with `d_h` unknown; four necessary rows;
- `Theta_h=d_h-r_h-2` named as cheapest discriminator, with the packet
  stating it does not supply either number (`structure:596-609`).

The structure packet's own conclusion (`structure:638-642`) types the
SNC boundary/pole model **OPEN**. The connectedness packet
(`connectedness:428-430`) repeats that nothing supplies a length-three
cusp-boundary completion or an existence theorem for any table row.

### 1.4 Finite typed derivation?

Jacobian `{f,g}=kappa`, étaleness of `pi|_S`, degree four, and the
census do not determine a unique pair in `R`. Target automorphisms of
Jacobian `1` act. Uniqueness-up-to-automorphism, even if it held,
would not be a desk-finite construction of images. The PROVISIONAL
model identification is explicitly sourced to an uncharged Poisson
parent (`structure:15-21,30-36`) and is not available here.

No missed pinning datum was found. The OPEN is not refuted.

---

## 2. Transformation law (0.4) and model-freeness of `d_h`

The definitions in (0.3) match the packets:

```text
d_h = -ord_(q_infty)(h o beta_B) = deg(h o beta_B),
r_h = #{p in Cbar_h : ord_p(k)<0},
Theta_h = d_h-r_h-2.
```

(`structure:596-606,602-603`; `connectedness:291-296,318-329`.) Here
`h` is used as the target affine coordinate of which `f` or `g` is the
pullback; that is the only typing under which `h o beta_B` is a map
`A1->A1`.

`d_h` is independent of any compactification `X` of `S`. The curve `B`
lives in the target `A2`. Its normalization is affine (`beta_B:A1->B`),
so the unique smooth projective model of that normalization is `P1`
with a single point `q_infty` at infinity. Automorphisms of `A1` are
affine and preserve polynomial degree. The function `h o beta_B` is
regular on `A1`, hence a polynomial, and
`deg= -ord_(q_infty)`. No surface divisor is used. This is model-free
by construction.

`r_h` is likewise independent of `X`. The general fibre `C_h=V(h-a)`
is a curve in `S`; a boundary modification `X'->X` identical on `S`
does not change `C_h` or `k|_C_h`. The smooth projective model of a
function field of one variable in characteristic zero is unique up to
unique isomorphism, and `r_h` is the cardinality of the polar support
of `k` on that model (not the polar degree, which is `4`).

Hence if `X'->X` is any birational map of compactifications that is
the identity on `S`,

```text
d_h(X')=d_h(X),    r_h(X')=r_h(X),    Theta_h(X')=Theta_h(X).
```

The report's wording that “normalization leaves the two function
fields unchanged” is slightly loose (the modification, not a further
normalization, is the identity on `S`), but the content is correct:
`C(B)` and `C(C_h)` are unchanged, and so are their unique smooth
projective models. No pole identity is consumed. (0.4) is proved.

Caveat, not a defect of (0.4): equality of this `d_h` with the finite
puncture count `s_fin` is the separate claim (3.1), which uses
transversality, avoidance of `n`, and `S=Y-R_bd`, and which sits
behind `OPEN[CENSUS-EXHAUSTIVITY]` if extra non-coordinate ramified
boundary images exist. That identification is not needed for
model-freeness of (0.3) itself.

---

## 3. Reading of (1.12)--(1.14) as generic-point-only

The report's reading is **correct**, and is the structure packet's own.

`structure:243-279` states the surface fibre partition `(2,1,1)` at
the **generic point** of `B`, after completed strict henselization,
with `K` a separable closure of the function field of `B`:

```text
K[[b]] -> K[[s]],     b |-> s^2.                         (1.12)
```

The identities (1.13)--(1.14) are for this generic quadratic
ramification valuation `v` of the surface field. The packet then says
expressly (`structure:297-298`) that the generic statement does not
determine the special two-dimensional cusp completion and does not
identify `R_bd`, `Phi`, or a deleted `L_j`.

Three distinct objects:

1. `v` of (1.12)--(1.14): a divisorial valuation of `K=C(S)` along the
   unique ramified factor over the generic point of `B`. Along that
   divisor the target coordinates `f,g` are finite (`Y->A2` is finite).
2. `q_infty` in (0.3): a place of the **curve** field `C(B)`, the unique
   infinity of `beta_B`. The order `ord_(q_infty)(h o beta_B)` is the
   degree of a coordinate of the affine embedding `B subset A2`.
3. Places counted by `r_h`: points of `Cbar_h` over `k=infinity`.

Transporting (1.12) to a unique source vertex at infinity identifies a
generic surface valuation with a special place of `C(B)` and with a
component of `X-S` over the line at infinity. That is the missing
geometric assertion. It would also be a pole/interior mix: the
ramified factor of (1.12) meets general `h`-fibres in the **finite**
deleted set `Sigma_fin`, whereas `Theta_h` is built from infinity of
`B` and from `Sigma_infty`.

The unique ramified factor is horizontal for the `h`-fibration in the
weak sense that `B` is not a coordinate line, so the factor dominates
the `h`-base. That does not type a unique **infinity** vertex, does
not force `r_h=1`, and is not a pole ledger for `h`. The report is
right not to invoke (1.12)--(1.14) for Stage 0.

---

## 4. Reopen list: necessity and sufficiency for Stage 2

The report asks for five items (`report:154-157`):

1. explicit checked images for `f,g` in (0.1), or an equivalent
   complete divisorial pole ledger;
2. an equation and normalized parametrization for `B`;
3. one marked SNC compactification resolving them;
4. a marking-compatible minimality rule;
5. a proof identifying all source primes over `q_infty`.

### 4.1 Sufficiency

Yes: with (1)--(5), Stage 2 as launched (`synthesis:75-76`) can run —
one marked SNC model, a divisor table, and the single numerical
subtraction `Theta_h=d_h-r_h-2`. Stage 1's puncture/parity prefilter
is then also defined.

### 4.2 Necessity, item by item

| Item | Necessary to evaluate `Theta_h` via (0.3)? | Necessary for the launched unique-vertex Stage 0? |
|---|---|---|
| 1. `(f,g)` or pole ledger | **Yes.** Without images or a complete pole ledger, neither `h o beta_B` nor poles of `k` on `Cbar_h` can be computed. | Yes |
| 2. `b` and `beta_B` | **Yes, fail-closed.** `d_h` is defined from `h o beta_B`. With `OPEN[CENSUS-EXHAUSTIVITY]`, `B` is not known to be the unique non-coordinate ramified image, so it is not recoverable from (1)+(3) by a typed step. | Yes |
| 3. marked SNC model | **Not for (0.3) itself.** `d_h` is a curve degree on `B`; `r_h` is a polar count on the unique smooth model of `C_h`, constructible in principle from `R/(h-a)` once (1) is known. **Yes for Stage 2's surface divisor table.** | Yes |
| 4. minimality rule | **No.** (0.4), proved in the same report, says every boundary modification identical on `S` yields the same `Theta_h`. | Only if a unique contracted representative of a horizontal divisor is still demanded |
| 5. lifts of `q_infty` | **No for the number `Theta_h`.** (0.3) reads `d_h` on `B`, not on a source prime over `q_infty`. A complete list of lifts is needed for a surface table; **uniqueness** is not. Identifying `q_infty` with a unique source component would pre-select the `r_h=1` row (`report:129-135`). | Uniqueness only if that gate is kept |

### 4.3 Amendment

Keep (1) and (2) as the numerical reopen gate. Keep (3) for Stage 2's
divisor table (not for Stage 1's prefilter). Demote (4) to optional
presentation. Replace (5) by: a complete list of source primes over
`q_infty` **without** a uniqueness requirement, unless the successor
reimposes unique-vertex as a geometric object rather than as a number.

A list of several lifts would still leave the launched “unique
horizontal vertex” clause unsatisfied. That is a reason to drop the
clause for the numerical invariant, not a reason to treat uniqueness
as supplied by “identifying all”.

The amendment does not change the present verdict: item (1) is absent.

---

## 5. Chart `iota` (0.2): source-side, not the charged pullback

The report's claim is **correct**.

```text
iota: R -> C[x,y],
      A |-> x^2,
      U |-> x+x^3y,
      Z |-> 2y+x^2 y^2.                                  (0.2)
```

Direction: a `C`-algebra map `R->C[x,y]`, geometrically
`A2_(x,y)->S`. The charged pullback is the opposite map
`pi^#: C[xi,eta]->R`, geometrically `S->A2`. Matching names `x,y`
with `xi,eta` is a variable/ring-map fallacy (`report:63-65`).

Image check, desk expansion:

```text
(x+x^3 y)^2 - x^2 - x^4(2y+x^2 y^2)
  = x^2 + 2 x^4 y + x^6 y^2 - x^2 - 2 x^4 y - x^6 y^2 = 0.
```

So `iota` kills `q` and is well-defined on `R`. It is the retained
cyclic-source chart (`structure:96-98`), as the report says.

Moreover `x` is not even in `K`. From `A=x^2` one has `[C(x,y):K]=2`
on this chart, so `x` is not a rational function on `S`. The charged
coordinates live in `R subset K`. Hence no section of `iota` can
supply `f` or `g`. The composition `iota o pi^#` would be the cyclic
map `H_cyc`, which the packet names and does not display
(`structure:559-564`).

`A` is the ruling coordinate `t` (`structure:483-484`), not a licensed
stand-in for `h in {f,g}`.

---

## 6. Guardrail audit and residual remarks

- **Variable/ring map.** (0.1) and (0.2) differ in direction, rings,
  and variables. Image of (0.2) was rechecked. Names were not matched.
- **Flag/place/series.** `q_infty` (place of `C(B)`), a horizontal
  prime of `X-S`, a point of `Cbar_h`, interior `Phi`, and the generic
  ramified factor of (1.12) remain distinct. The report does not fuse
  them.
- **Pole/interior.** (1.12)--(1.14) are not used as pole identities
  for `h`. Along that factor `f,g` are finite.
- **Floor/attainment.** The four-row table is necessary-only in both
  packets. No row is promoted to attainment. `Theta_h` is not
  evaluated.
- **Prime label/derivative.** The packets define `'` as `d/dZ` on
  residue series (`structure:132-133`). The report does not treat it
  as a divisor mark.
- **Protocol vs mathematics.** `synthesis:70-73` requires a unique
  horizontal vertex at Stage 0 or else `OPEN`. That gate is stricter
  than (0.3)+(0.4). The report obeyed the gate. Independently, the
  missing images already force `OPEN`.
- **Orevkov remainder.** Correctly not identified with `Theta_h`
  (`structure:539-557`; `synthesis:78-80`).
- Stages 1 and 2 were rightly not entered.

No literature fetch was required: uniqueness of smooth projective
models of curves and the identification `deg= -ord_infty` on `A1`
are standard.

---

## 7. Disposition

```text
OPEN CONFIRMED
OPEN[THETA-STAGE0-MARKED-SNC]
```

The fail-closed Stage-0 stop is right in both directions. Nothing in
the two packets pins the pullback or a marked SNC representative, so
the OPEN does not waste a computable composite. The reopen list is
sufficient for Stage 2; it is slightly too strong on minimality and on
uniqueness of lifts of `q_infty`, which (0.4) and (0.3) make
unnecessary for the number `Theta_h`. The successor lane should keep
items (1)--(2) as the numerical gate, keep (3) for a surface table,
and treat (4)--(5) as optional presentation except if it reimposes a
geometric unique-vertex requirement.

The one-cusp horn is neither killed nor pinned.

<!-- BODY-END -->
