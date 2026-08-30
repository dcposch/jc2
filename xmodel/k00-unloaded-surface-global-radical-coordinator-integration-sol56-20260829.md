# Binding integration: unloaded K00 global radical

Coordinator: Sol 5.6 Ultra  
Date: 2026-08-29 UTC  
Frozen integration basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: **BINDING PROMOTION / EXACT GLOBAL RADICAL / MIXED-SOURCE FIREWALL**

## 0. Charged evidence and disposition

```text
96d88f49fd8e2dab1b05d18ac7912d7c1e3374fc474dcfafce29a08558edb62b
  xmodel/k00-unloaded-surface-global-radical-sol56-20260829.md
6f300d9890bb624e7c1023763271e409cc106c3f68e94436809b0ca18cf5a178
  xmodel/k00-unloaded-surface-global-radical-hostile-review-fable5-20260829.md
8f307a03fadc8d610fda151f671d815ae8bc3dd7ceee233593743018e65b81f4
  aws_r6b_global_power_v4/CUSTODY.sha256
a14e3f84ff95adbb6e799aaa663fd16f2152fbcac0e439547c6aba4ef8354f4e
  replay_global_power.sing
```

Fable's different-model verdict is `CONFIRM_WITH_CORRECTIONS`. It
independently parses the original seven rows, proves both ideal containments
without using the producer's standard basis of `I`, expands all 28 serialized
multipliers, reconstructs the V3 serialization defect and V4 repair, attacks
the identities with five mutations, and confirms every functor-of-points
scope boundary. The two corrections below are binding. The exact radical
theorem is promoted.

## 1. Promoted theorem

In `Q[d0,...,d5]`, let `I=(r1,...,r7)` be the seven frozen unloaded K00 rows
and put

```text
f0=d0-2*d4-d4^2,
f1=8*d1-(1+d4)*d3,
f2=d2-d4-16*d3^2,
f5=d5-2*d3,
J=(f0,f1,f2,f5).
```

Then

```text
sqrt(I)=J.                                           (1.1)
```

Moreover `J` is prime of height four and

```text
Q[d0,...,d5]/J ~= Q[d3,d4].                         (1.2)
```

The reduced unloaded zero set is therefore exactly the smooth graph

```text
D(S,T)=(2*S+S^2,(1+S)*T/8,S+16*T^2,T,S,2*T),        (1.3)
```

with `S=d4,T=d3` uniquely.

The proof is portable in the original seven-row presentation. For each
`a in {0,1,2,5}`, the frozen certificate gives seven explicit multipliers
with

```text
f_a^5=sum_(j=1)^7 c_(a,j)*r_j.                      (1.4)
```

All 28 multiplier files and all four identities pass the fresh direct replay
and Fable's independent exact-Python reconstruction. Conversely, substituting
(1.3) kills all seven rows. The kernel of that substitution is exactly `J`,
and its quotient is the polynomial ring `Q[d3,d4]`, proving primality and the
other containment.

## 2. Sharp generator exponent

For every displayed generator `f_a`, power five is the first power lying in
`I`:

```text
f_a^k notin I  for 1<=k<=4,
f_a^5 in I.                                          (2.1)
```

The producer carried sufficiency by (1.4) and labelled minimality as an
in-memory screen. Fable upgrades minimality independently: since the seven
rows have order at least two at the origin while each `f_a` has nonzero
linear part, power one fails; exact degree-two-through-four coefficient
systems prove `f_a^4 notin I+m^5`, hence `f_a^4 notin I`, for all four `a`.
If a smaller positive power lay in `I`, multiplication would put the fourth
power in `I`, a contradiction.

This is generatorwise sharpness. It is not an assertion that every mixed
monomial of `J` has the same first power or that `I` has a stated integral
closure.

## 3. Binding corrections

1. The producer's phrase that the fresh replay uses “no standard-basis or
   lifting computation” is narrowed. The replay uses no standard basis of
   `I` and no lift/`liftstd` for the promotion-bearing identities; it does use
   tiny `std(J)` and `std(BAD)` preflight computations. Fable's independent
   containment proof is substitution-based and Groebner-free.
2. The shipped certificate mutation `c0_1 -> c0_1+1` is valid but weak: its
   residual is exactly `r1`. Promotion also charges Fable's independently
   successful interior-coefficient, source-row, wrong-exponent, and
   cross-wired-certificate mutations.

No mathematical conclusion changes.

## 4. Exact consequence and firewall

For any characteristic-zero field, reduced Q-algebra, or formal-series
domain, an **unloaded** point satisfying all seven rows lies uniquely on the
graph (1.3). Reducedness is necessary, not cosmetic: over
`Q[d0,...,d5]/(d0,...,d5)^2`, every unloaded row vanishes while the nonzero
linear parts of the `f_a` survive.

The literal loaded source has the form

```text
R(d)+K10*A10(d)+K6*A6(d)+K2*A2(d)-targets=0.
```

It does not set `I=0`. Therefore (1.1) does not put a loaded trajectory on
the graph, does not permit termwise recentering, and does not remove
nonreduced normal cones. Any consumer must first prove that the unloaded block
vanishes in a reduced target at the exact coefficient or associated-graded
stage being used.

In particular, the separate exact normal-coordinate claim `I subset J^2`,
the proposed `J^17 subset I` corollary, Rees-valuation sharpenings, ramified
calendars, and mixed-source inductions keep their own lifecycle states; none
is promoted merely by this integration.

## 5. Nonclaims

This theorem identifies one unloaded affine scheme's reduced support. It
does not prove equality of schemes, a loaded solution, ramified-source
coverage, closure incidence, all-order lifting, source reachability,
algebraization, a polynomial map, a counterexample, or JC2. Formal data are
not maps, and reduced support is not attainment.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5312`.
- Body SHA-256:
  `d5294dab7f1a8c6c6c311fed667920f7e45385ea621299cebed362595f494d64`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
