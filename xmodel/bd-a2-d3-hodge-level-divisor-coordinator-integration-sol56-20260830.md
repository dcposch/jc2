# Binding integration: degree-three Hodge divisor and four-row gate

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `32e7338e066753da7bd3e0da93cc750174b293ac`  
Disposition: **PROMOTE WITH REVIEW REPAIRS AND EXACT-LEVEL SHARPENING**

## 0. Binding verdict

Promote the degree-three Hodge-divisor theorem and its exhaustive four-row
classification.  Let `X subset P2 x P1` be an integral normal class-`(3,3)`
hypersurface over `C`, assume the binding dominant-rational-`A2` and adjoint
theorem, and let `r:Y->X` be the minimal projective resolution.  Then the GR
trace induces

```text
O_P1(1) --s--> O_P1(3),
div(s)=T=q(Z_GR),                    length(T)=2.       (0.1)
```

After relative minimalization `h:Y->S`, the rational genus-one fibration
`g:S->P1` has exactly one of two forms:

```text
m=1: no multiple fibre and a section;
m=3: one triple fibre and no section.                  (0.2)
```

Writing `D=h_*(K_Y-r^*K_X)<=0`, exactly four rows occur:

| type | base defect `T` | pushed discrepancy `D` | exact local CFS levels | minimum blowups | `rho(Y)` |
|---|---|---|---|---:|---:|
| section | `t1+t2`, `t1!=t2` | `-F_t1-F_t2` | `(1,1)` | 2 | `>=12` |
| section | `2t` | `-2F_t` | `2` | 2 | `>=12` |
| triple fibre `F_0=3P_0` | `t0+t1`, `t1!=t0` | `-P_0-F_t1` | `(1,1)` | 2 | `>=12` |
| triple fibre `F_0=3P_0` | `2t0` | `-4P_0` | `2` | 4 | `>=14` |

There is no fifth row.  In the triple-fibre rows the central plane cubic is a
triple line.  The local CFS level equals the local Hodge/GR length exactly;
it is not the coefficient `b_t` in `D_t=-b_tP_t`.

The different-model hostile review returns `CONFIRM_WITH_CORRECTIONS`.  It
finds no counterexample and preserves every row and Picard bound.  Its main
new leverage is exactness of the CFS level, which adds a finite principal-open
upper disjunction to the invariant computation.

## 1. Frozen evidence and custody

```text
087953ec71175d8e470cd2aa89dd7928ef0ab88223009c619e2d95dc39287637
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md
e571684152a54d9921cc38bdcb9f8833a6f875bda659cf6ebeb8877871246a87
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md.artifact.json

9115b2886303568c7671a375913f5eae28858391ce4cdbf3d1c43232c328fa94
  xmodel/bd-a2-d3-hodge-level-divisor-hostile-review-gpt55-20260830.md
  body 8b46aac7130d093fee885255d2d1dd35e10d54028600f43dea0a18f2ee0ffb82
9ab5cd2633b46614cd086f1f4c1b657082903e437b36814b377128f31dfdb9a0
  xmodel/bd-a2-d3-hodge-level-divisor-hostile-review-gpt55-20260830.run.v2

ef7b8f5ea7c9f44af7b01f69e3a0f7d15852c804074d41cf1a6aa9f1f204ef1a
  xmodel/bd-a2-d3plus-pg-defect-coordinator-integration-sol56-20260830.md
```

Root reproduced the schema-v2 receipt, prompt, Codex adapter, launcher,
Seatbelt profile, validator, appendix, composed model prompt, report, log,
and all five charged mathematical hashes before reading the review.  The
report body was stamped against basis
`7dd85a6598c56fa043dd397382de1c93d846fa39` and verified.
`charge_basis_status=ABSENT` is correct because the reviewer asserted no new
exit price.

## 2. Hodge divisor on the coefficient base

Every coefficient-base fibre of `q:X->P1` is a nonzero plane cubic Cartier
divisor, including a possible triple line.  The hypersurface is
Cohen--Macaulay and the base is a regular curve, so `q` is flat.  The fibre
sequence gives `h0(O_C)=h1(O_C)=1` even for nonreduced cubics; globally,

```text
q_*O_X=O,                 R^1q_*O_X=O(-3),
q_*omega_(X/P1)=O(3).                                      (2.1)
```

The resolution fibration `f=q r` is also flat and connected.  Characteristic
zero is load-bearing here: multiple fibres are tame, so the usual wild-fibre
torsion in `R^1f_*O_Y` is absent.  Rationality gives `chi(O_Y)=1`, hence

```text
R^1f_*O_Y=O(-1),          f_*omega_(Y/P1)=O(1).            (2.2)
```

Start from

```text
0 -> r_*omega_Y -> omega_X -> Q_GR -> 0
```

and tensor by `q^*O(2)`.  With
`Q_rel=Q_GR tensor q^*O(2)`, projection formula and (2.1)--(2.2) give the
nonzero map (0.1).  Its cokernel and `q_*Q_rel` both have length two, so they
are equal without assuming the next higher direct image vanishes.  Since
`Q_rel` is faithful over the GR scheme, annihilators identify

```text
div(s)=q(Z_GR)=T
```

scheme-theoretically for the given projection.  Thus `T` is either two
distinct reduced points or one colength-two DVR subscheme; two physical
defect points over one base value are not a third alternative.

## 3. Discrepancy, minimalization, and the four rows

For `Delta=K_Y-r^*K_X`, adjunction with arithmetic genus gives

```text
Delta.E_i=2p_a(E_i)-2-E_i^2 >=0
```

on every minimal exceptional component.  The connected negative-definite
intersection matrix has entrywise negative inverse, so `Delta<=0`; a
connected Gorenstein block has zero discrepancy exactly when it is Du Val.

Contract vertical `(-1)`-curves to the relatively minimal rational
genus-one surface `S`.  With compatible divisor representatives,

```text
D=h_*Delta<=0,             K_S=F+D.                       (3.1)
```

The tame canonical bundle formula is

```text
K_S ~ -F + sum_i(m_i-1)P_i,
F_i=m_iP_i,                deg fundamental line=1.        (3.2)
```

Since `rho(S)=10`, a horizontal `(-1)`-curve exists.  Intersecting (3.2)
with it shows that two multiple fibres are impossible.  With none, its degree
is one and it is a section.  With one fibre of multiplicity `m`, every
multisection degree is divisible by `m`; a general plane-line horizontal
divisor has degree three.  Hence `m|3`, giving exactly (0.2).

For every fibre component `Theta`, `D.Theta=0`.  The connected fibre
intersection matrix has integral kernel generated by the primitive fibre
cycle, so a nonzero local part is

```text
D_t=-b_tP_t,             b_t>0.                           (3.3)
```

Support equality is on the **base**:

```text
Supp_P1(D)=Supp(T).                                        (3.4)
```

Contraction can discard internal discrepancy components inside a supported
fibre; (3.4) says it cannot erase the whole defect fibre.  The two global
intersection equations are

```text
m=1: sum_t b_t=2;
m=3: b_0+3 sum_(t!=t0)b_t=4.                             (3.5)
```

Combining (3.4)--(3.5) with the exact length-two base scheme yields precisely
the table in Section 0.  In particular a defect entirely away from the triple
fibre cannot sum to four, and no `b_t` is identified with local geometric
genus or GR length.

## 4. Picard bounds

For each blowup in the inverse of `h`,

```text
D_new=pi^*D_old+E,
coeff_E(D_new)=1+ord_p(D_old).                            (4.1)
```

Proper surjectivity ensures that every `Y_t->X_t` has a component mapping
onto the one-dimensional plane fibre; that component is not
`r`-exceptional and has discrepancy coefficient zero.  Starting from
`D_t=-bP_t`, every inherited component has coefficient at most `-b`, so a
zero carrier must be born in the blowup chain.

The satellite-safe induction is: before the first zero, if `M_j` is the
largest fibre coefficient after `j` blowups, then

```text
M_j<=-b+j.
```

At a centre on one or several negative components the new coefficient is at
most `1+M_(j-1)`; intersection and infinitely-near centres cannot accelerate
the birth of zero.  Thus at least `b` blowups are required over that fibre,
and counts over distinct fibres add.  Since `rho(S)=10`, the four Picard
bounds are exactly those displayed in Section 0 for the minimal resolution.

## 5. Exact local Hodge level and invariant gate

At every complex DVR, Liu--Lorenzini--Raynaud Theorem 3.1 identifies the
resolved-torsor Hodge lattice with the minimal Jacobian/Neron differential
lattice, including the locally insoluble triple fibre.  The 2018 corrigendum
does not alter that theorem.  With compatible generators, if the local order
of `s` is `k`, Fisher's differential weights give

```text
c4_plane=s^4 c4_min,
c6_plane=s^6 c6_min,
Disc_plane=s^12 Disc_min.                                (5.1)
```

Cremona--Fisher--Stoll Lemma 3.2 applies without a solubility hypothesis and
shows that the CFS level of the given ternary cubic is **exactly** `k`.
Therefore

```text
k=1: v(c4)>=4, v(c6)>=6, v(Disc)>=12,
     and [v(c4)<8 or v(c6)<12];

k=2: v(c4)>=8, v(c6)>=12, v(Disc)>=24,
     and [v(c4)<12 or v(c6)<18].                         (5.2)
```

The discriminant lower bound follows from
`c4^3-c6^2=1728 Disc` once the `c4,c6` bounds are imposed; it is a control,
not a third generator.  The upper disjunction in (5.2) must be implemented as
a finite principal-open cover, not as another equality.

For `m=3`, all fibre multiplicities remain divisible by three under pullback.
The plane fibre has total degree three, so it is necessarily `3L`.  After
constant normalization and `t0=0`, the exact global coefficient family is

```text
F=x^3+tG1+t^2G2+t^3G3.                                  (5.3)
```

This is finite-dimensional, not a finite set of orbits.  Normality and
generic smoothness are open conditions and must remain literal localizations.
Saturation computes a closure and may reintroduce bad boundary points; every
survivor must be checked on the declared open and actually minimized.

## 6. Controls, scope, and interface composition

The reviewed diagonal cubics separate discriminant order from total-space
normality and fibre multiplicity.  The generalized-Hesse control has

```text
(v(c4),v(c6),v(Disc))=(4,6,24)
```

but exact level one, not two; its minimal Jacobian has discriminant order 12.
Thus discriminant order 24 alone is never a level-two certificate.

The theorem-interface composition finds one immediate exact client: the
separately frozen first-jet packet
`bd-a2-d3-triple-line-first-jet-invariant-gate-sol56-20260830.md` reduces the
triple-line normal chart to two repeated-root first-jet forms.  That packet is
still provisional under a live Fable review, so none of its eliminations is
promoted here.  The new upper disjunction (5.2) should be added to its
successor computation as soon as review closes.

This integration promotes a conditional degree-three surface theorem, not a
surface-existence theorem.  It does not classify all exceptional
discrepancies or Kodaira fibres, prove normal/global compatibility of an
invariant solution, supply the dominant `A2` map, produce a polynomial map,
or prove or disprove JC2.

## 7. Cheapest decisive successor

Start with the strongest row `m=3,T=2t0`.  In the exact coefficient ring of
(5.3), impose

```text
t^8 divides c4,          t^12 divides c6,
and [t^12 does not divide c4 or t^18 does not divide c6],
```

on the normal and generic-smooth open.  Use `Disc/t^24` as a control.  Apply
the CFS minimisation state machine to every survivor; finite-jet
nonemptiness is not a level or existence certificate.  Then run the other
three globally normalized rows, keeping the two support points distinct when
required.  Review remains nonblocking, and any Gröbner or saturation shard
that ceases to be desk-scale runs on AWS.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11008`.
- Body SHA-256:
  `032a0a7eeeafc42cc53da1216a038740a9f3c797806adc68cc82d94a23f20ed6`.
- Frozen basis: `32e7338e066753da7bd3e0da93cc750174b293ac`.
