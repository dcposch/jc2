# K00 V20R2 valuation three: coordinator integration of the reviewed closure

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `55067d08c111f473945700ded838a7798b8b3fb2`  
Lifecycle: `PROMOTED EXACT FINITE-JET EXCLUSION / DRIFTED PREFLIGHT QUARANTINED`

## Binding verdict

Promote the exact valuation-three exclusion below. Over every
characteristic-zero field, the normalized V20R2 source

```text
C6=1,
k10[0]=kappa!=0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0]!=0,
d=Lambda^3 x+Lambda^4 y+Lambda^5 z+...,
x!=0
```

has no compatible jet satisfying all seven literal rows through grade 12.
Consequently no same-source `K[[Lambda]]` formal section has exact valuation
three.

This promotion does not consume the source packet's declared preflight
digest: those declared bytes are not the committed bytes. The mathematical
fan is instead bound by two independent hostile reconstructions, and the
grade-12 endpoint by a separate producer/replay plus hostile reconstruction.
The custody failure is preserved in the evidence record rather than repaired
by changing a sealed producer.

## Evidence and custody supersession

The Sol source/threat packet is
`xmodel/k00-r3-source-threat-packet-sol56-20260829.md`, full SHA-256
`6940e1ea3e9b39aa525cc9b55e05488ca6b754e06517ddc627a2c8e8f1948dc4`,
body SHA-256
`c2fffead93bdebdf017d6536fe6640cbf6ec93ed8a13a0477d90ed42c0efbdcd`.
Its mathematical grade-6--11 fan is retained, but its Section 8 replay pin
`bac4b688...` is not: the current committed file has SHA-256
`a6eec6464c85f9f14a80759f07445516005b2e4abcea6e3e478e661028353b94`.
The original transcript and runtime are therefore quarantined as evidence.

Opus 5 independently reconstructs the complete source fan in
`xmodel/k00-r3-source-threat-packet-hostile-review-opus5-20260829.md`,
full SHA-256
`6cad7b8008a7be1868cda003ce8896f8e6232a04ac343deb51a6eb47ba04a525`,
body SHA-256
`c567c05ea41f3f8858efe5b235cab19ffc847915cd096482d2a97faf2f1ac057`.
It confirms the packet mathematics and independently discovers the same
grade-12 closure later produced by Sol.

The independent endpoint producer is
`xmodel/k00-r3-erfan-grade12-certificate-sol56-20260829.md`, full SHA-256
`e84f295144713011f3a27548c273ac4bccca0f34b7dfa14bb21a58b0e8638bb4`,
body SHA-256
`0dca07ecf7538acd065fedbc60bd3f417400b86fa3ddf29f049a4dcf30a06c1e`.
Its literal replay
`xmodel/k00-r3-erfan-grade12-replay-sol56-20260829.py` has SHA-256
`02fb368a054c781e8846e07a2948a5bdbe9e879abebc4e9b8e34be008f4e2053`
and passes ordinarily and under `python3 -O`.

Fable 5 independently rebuilds all 569 tails, the whole charged fan, and all
three endpoint cells in
`xmodel/k00-r3-erfan-grade12-hostile-review-fable5-20260829.md`, full
SHA-256
`c9711e2e98d2d6a4c15443d8aa06b7f32639e2a67e6f70704ef387e045b82a46`,
body SHA-256
`611ff99b2404d5f640b1fb1acf87755991a38bef7abf194ea70bf2d4c6d8c98f`.
Its 79-check exact suite confirms every mathematical claim and supplies
independent mutation probes. Its `PASS_WITH_REPAIRS` verdict identifies the
same upstream digest mismatch and no mathematical gap.

For the contracted-calendar statement, promotion explicitly binds
`cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/K_VECTOR.txt`
at SHA-256
`940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a`;
it is not inferred from the source packet's two principal pins.

## Exact exclusion tree

Write

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4,
ell(s,t)=(2s,t/8,s,t,s,2t).
```

Grade 6 has reduced zero set `A(x)=B(x)=0`. The leading `DQ(x)`
rank-two and both rank-one branches die at grade 9, so every survivor has
`x=ell(s,t)`, `(s,t)!=(0,0)`.

For the next coefficient, rank two dies at grade 11. On isotropic source
rays the correct direct argument is
`D=t(u-8*epsilon*i*v)^2`; the two displayed syzygies alone degenerate
there. Both next-rank-one branches die at grade 12 by the exact jet-blind row
`G12_6=epsilon*i*v_y^3/32`.

On next rank zero, grade 10 forces `z` onto the same cone. The complete
grade-11 linear block uses the shifted coordinates

```text
U=u_z+(5/6)kappa*s,
V=v_z-(5/6)kappa*t,
```

not the rank of `DQ(z)`. Effective rank zero dies at grade 11. Effective
rank one is confined to the two source rays and then, for each sign, the
grade-12 localized unit identity is

```text
12288*C1-6144*j*C3 = 800*t^6*kappa^2*qV^2,  j in {+i,-i}.
```

Effective rank two dies because the
two cleared binary quadratics have resultant

```text
-(5^8/(2^76*3^4))*kappa^8*(s^2+64*t^2)^12;
```

on either isotropic source ray their common square root forces
`U^2+64V^2=0`, contradicting the rank-two open. Thus the three residual
cells `R3-00-ER1(+)`, `R3-00-ER1(-)`, and `R3-00-ER2` are all empty
at grade 12.

Every branch is exhausted. Grades 13--19 are unreachable after the certified
empty prefix; they are not silently computed or declared identically zero.

## Repairs folded into promotion

1. The stale `bac4b688...` preflight and its claimed observed transcript
   are not promotion evidence. The present `a6eec646...` bytes are retained
   only as a separately reviewed advisory replay; the independent
   reconstructions carry the theorem.
2. The 122-column and grade-through-12 censuses are justified by structural
   degree/arrival arguments, not the producer preflight's hard-coded counts.
3. Say “six nonzero leading quadrics” because `Q6=0`. On the
   `u^2=192v^2` kill, the quotient values are
   `(1/8)v^3` and `-(1/64)v^3`, after
   `b=-2r(1+4a)` over `r^2=192`; `a,b` range over that extension.
4. The grade-11 residual list was a correct stopping-point handoff, not a
   false existence claim. It is now superseded by the independently produced
   and reviewed grade-12 closure.
5. The Fable report's process note that the Opus review had not completed was
   true at its observation cutoff and is now stale. Both sealed reviews are
   consumed here.

## Scope

This is reduced, field-valued finite-jet emptiness and its immediate
same-source formal-section consequence on one normalized support. It is not
scheme-theoretic. It gives no source-wide closure theorem: ramified DVR
pullbacks with `Lambda=u(t)t^e`, `e>1`, are a separate atlas. It proves no
other load/support face, actual map, counterexample, or JC2 conclusion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6300`.
- Body SHA-256:
  `d1ff817cb29ca4b29ce2e1093a0a3cd206318b19a76d7a0fc70203bedde766ae`.
- Frozen basis: `55067d08c111f473945700ded838a7798b8b3fb2`.
