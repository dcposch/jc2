# `(8,12)` order-two square `r=1` / `d=1` V12: source-support erratum

Date: 2026-08-26

Status: **NONMUTATING ERRATUM.  V12 THEOREM 2 IS QUARANTINED OUTSIDE ITS
BASELINE CONTACT.  V12 THEOREM 1 REQUIRES A SOFTWARE REPLAY.  NO SQUARE OR
ORDER-TWO VERDICT.**

## 0. Immutable inputs

```text
fe7a5c8a528b059c22118cc0256c180a9b455d8ba04637b5dc3ae2d3dbf95ae3
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/RESULT.md
31abd6c8bb76709a2bc8de526e70baf775f32bc34d68940c97d82ee8ddfd3186
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/QUARANTINE.md
cb1b07bb679c1149bc2671c2ed88417352c0708787f8362756ed3ffb12d3a88a
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/compile_v12_recurrence_products.py
decc00a91c952354902da2eeeeac6eb9c7fdc06748bf5f96957f45617e07743a
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/FREEZE.sha256
f06671486459aeb34a797e64ea4f8572cd01728218bb526d419ed6d326eda72a
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/RESULTS.sha256
509c9edf1c613fa4ff997d3da4acbfeccd7e0895fd76e2f471fad37d90ec15aa
  xmodel/max12-812-order2-square-r1-d1-v12-hostile-review-grok-20260826.md
e43bc4b2a454e84964d4a2e99479d521841304e1b55c0d47a652ad920a649c0f
  cases/max12_812_order2_square_positive_load_fan_z3_20260826/RESULT.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
```

Nothing above is mutated by this note.

## 1. The two independent defects

### 1.1 `r=1`: standard-basis and validator defect

Both V12 `r=1` stdout files contain twice

```text
// ** R1_rad is no standard basis
```

The program forms `R1_rad=radical(R1_I)` and then calls `reduce` with that
unstandardized ideal.  The validator rejects `=FAIL` and a leading `?`, but
not `// **`.  Therefore the printed support marker is not a valid
Groebner-membership certificate and the sentence in V12 `RESULT.md` saying
that no Singular diagnostic remains is false.

This is a software/certificate defect, not evidence against the underlying
grade-thirteen identity.  The exact remainder is

```text
(b1*z+b0)^3 mod (z^2+p/2)
 = b1*(3*b0^2-(p/2)*b1^2)*z
   +b0*(b0^2-(3*p/2)*b1^2).
```

On `D(p)` its zero set is `b0=b1=0`: if either coefficient is zero the
other equation kills the other coefficient; if both are nonzero, the two
displayed factors would give simultaneously
`b0^2=(p/6)b1^2` and `b0^2=(3p/2)b1^2`, a contradiction in characteristic
zero (and in the registered good characteristic).  A repair must either
standardize the radical before every reduction or certify this elementary
case split directly, and its validator must reject every `// **` diagnostic.

### 1.2 symbolic `d=1`: incomplete shifted source support

The V12 D1 source compiler extracts only absolute sigma grades 15 and 16
after

```text
A=sigma^2*theta*(A0+sigma*A1),
C=sigma^3*theta*(C0+sigma*C1),
R=sigma^2*theta*eta*R0.
```

It then substitutes `theta=sigma^n`, `eta=sigma^s` and claims every

```text
a=2+n,   c=a+1,   r=a+s,   n,s>=0.                 (1.1)
```

That substitution shifts the eight displayed `k10`/unloaded monomials, but
it cannot turn an unextracted higher absolute source coefficient into a
certified row.  The complete frozen source also contains

```text
sigma^12*k6*f^(3/4) + sigma^20*k2*f^(1/4)
```

and the four nonzero target charges at absolute grades `28,32,36,38`.
These terms enter the shifted window for finite values of `n`.

## 2. Exact missing-support calculation

Write

```text
f=K^2+sigma^5*D,
K=L^2+sigma^2*R,
D=L*A+C,
L=z^2+p/2.
```

The first nonpolynomial pieces of the two omitted load summands are obtained
directly from the binomial series:

```text
sigma^12*k6*f^(3/4)
 = polynomial
 +(3/8)*sigma^16*k6*R^2/L
 +(3/4)*sigma^17*k6*C/L
 -(1/16)*sigma^18*k6*R^3/L^3
 -(3/8)*sigma^19*k6*(A*R/L^2+C*R/L^3)
 -(3/32)*sigma^22*k6*(A^2/L^3+2*A*C/L^4+C^2/L^5)
 + later terms,                                             (2.1)

sigma^20*k2*f^(1/4)
 = polynomial
 +(1/2)*sigma^22*k2*R/L
 -(1/8)*sigma^24*k2*R^2/L^3
 +(1/4)*sigma^25*k2*(A/L^2+C/L^3)
 -(3/32)*sigma^30*k2*(A^2/L^5+2*A*C/L^6+C^2/L^7)
 + later terms.                                             (2.2)
```

Here `k6,k2` denote their leading series coefficients; a positive load
valuation adds that valuation to every corresponding order.  Formulae
(2.1)--(2.2) are support identities only.  They do not assert that the
listed truncation is a complete global fan.

For (1.1), with unit leading `k6`, the omitted `k6*C/L` term has absolute
order

```text
17+c=20+n,
```

whereas `AC/L` and `C^2/L^2` occur at `15+2n` and `16+2n`.
Consequently it ties the `C^2` target already at `n=4` (`a=6`), ties the
first `AC` face at `n=5` (`a=7`), and precedes that face for `n>=6`
(`a>=8`).  This is a concrete failure of V12's unbounded symbolic-support
claim.

The first further thresholds, allowing `r=a+s`, are:

| contribution | absolute order | at/before `C^2` grade `12+2a` when |
|---|---:|---:|
| `k6*C/L` | `18+a+ord(k6)` | `a>=6+ord(k6)` |
| `k2*R/L` | `22+a+s+ord(k2)` | `a>=10+s+ord(k2)` |
| `k2*A/L^2` | `25+a+ord(k2)` | `a>=13+ord(k2)` |
| `k2*C/L^3` | `26+a+ord(k2)` | `a>=14+ord(k2)` |
| `mu2` target | `28+ord(mu2)` | `a>=8+ceil(ord(mu2)/2)` |
| `mu4` target | `32+ord(mu4)` | `a>=10+ceil(ord(mu4)/2)` |
| `mu6` target | `36+ord(mu6)` | `a>=12+ceil(ord(mu6)/2)` |
| `J/4` target | `38` | `a>=13` |

The ceiling entries are only order comparisons.  A sparse target row is
not a Laurent-polynomiality term and must be retained in the exact
seven-row cokernel; it cannot be absorbed into the local simple-pole block.

## 3. Exact counterexamples to the old finite fan's source completeness

Measure orders relative to absolute grade ten and use the seven enumerated
forms

```text
AC,C2,RA2,A3,kR3,kRC,kA2.
```

The old text calls these "eight" forms, but the enumerator has seven names
and `1016=(2^7-1)*8` candidate active-set/boundary pairs.

1. Set `(a,c,r,q10,q6)=(8,9,8,1,0)`.  The seven old values are

   ```text
   17,18,26,29,25,19,21,
   ```

   so the old fan reports `AC` as the unique minimum.  The omitted
   `k6*C/L` value is `7+q6+c=16`, strictly smaller.

2. Set `k6=0` and `(a,c,r,q10,q2)=(15,16,15,1,0)`.  The old minimum is
   `AC=31`, while the omitted `k2*R/L` value is `12+q2+r=27`.

3. Set `k6=k2=0` and `(a,c,r,q10)=(10,11,10,1)`.  The old minimum is
   `AC=21`, while a unit `mu2` target occurs at relative order 18.  Its row
   may force `mu2=0`, but omitting it is not a complete source fan.

Thus the amended fan result is usable only as navigation inside its seven
registered forms.

## 4. Correct surviving scopes

- The V12 D1 bytes source-type the baseline contact
  `a=2,c=3,r>=2` through its two decisive grades 15 and 16.  No omitted
  lower load or target can occur there.  This baseline statement must be
  reviewed as a lifecycle root separate from `r=1`; it does not inherit the
  unbounded theorem.
- The V12 `r=1` source extraction at grade 13 is independent of all omitted
  lower loads and targets, whose first possible absolute negative grade is
  at least 16.  Its mathematical support calculation survives, but promotion
  awaits the standard-basis/validator replay in Section 1.1.
- No `n>0` D1 contact is promoted by V12.

## 5. Corrected exact-source sharding contract

The successor must use the frozen seven rows themselves, not an extrapolated
eight-term Laurent expression.

1. Split the repaired `r=1` lifecycle from the D1 lifecycle.
2. For D1, reconstruct all four charged source summands
   `f^(3/2), sigma^4*k10*f^(5/4), sigma^12*k6*f^(3/4),
   sigma^20*k2*f^(1/4)` and all four target rows.  Emit the exact moving
   lower-unitriangular row transform at every grade consumed.
3. Give `k6(sigma),k2(sigma),mu2(sigma),mu4(sigma),mu6(sigma)` independent
   finite jets; retain `J` as a unit.  Do not infer their valuation from
   `ord(k10)`.
4. First shard by the threshold bands

   ```text
   a=2..5;  a=6;  a=7;  a=8..9;  a=10..12;
   a=13;    a=14; a>=15,
   ```

   and within each band by the first nonzero lower-load/target valuation.
   The bands are design aids, not proof cells; exact source support may
   refine them.
5. In root-oriented shards, put every denominator-`L` contribution into one
   truncated simple-pole block.  Keep `k2*A/L^2`, `k2*C/L^3`, higher
   corrections, and sparse targets outside that block until exact pole and
   row-cokernel identities are proved.
6. Include a source-support manifest listing every monomial through the
   requested terminal grade, with a negative control that deletes
   `k6*C/L` and must fail at `(a,c,r,q10,q6)=(8,9,8,1,0)`.
7. Exact Q is the proof endpoint; at least one good prime is a software
   control.  Every compiler and engine run is AWS-only and fail closed.

The first economical corrected producer is the finite baseline band
`a=2..5`, followed by the `a=6,7` `k6` transition.  It must not wait for a
global high-contact fan.

## 6. Firewall

This erratum retracts only the unbounded source-coverage inference and the
unclean `r=1` software certificate.  It neither refutes the displayed local
residue argument nor proves any successor band empty.  It does not close the
square branch, order two, `(8,12)`, maximum twelve, or JC2.
