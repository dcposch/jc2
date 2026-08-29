# Different-model hostile review — nearest K00 r=2 reseed

You are Opus 5, an independent hostile reviewer in the Plane Jacobian
Conjecture campaign. Frozen git basis:
`93db679d3160c957b0610297afccc1f2fad53125`.

Review only the new `r=2` claims in
`xmodel/k00-higher-valuation-contraction-and-r2-preflight-sol56-93d-20260829.md`.
The separate `r>=7` theorem is under Grok review and need not be duplicated.

The producer claims that for

```text
d=Lambda^2 ell(s,t)+Lambda^3 y+Lambda^4 z+...,
ell=(2s,t/8,s,t,s,2t),  (s,t)!=(0,0),  k10[0]=kappa!=0,
```

the even sublane `y=0` is impossible by grade 8. With
`a=(s^2,st/8,16t^2,0,0,0)`, `w=z-a`,
`A=16w1-4w3+w5`, `B=w0-4w2+2w4`, it claims exact row combinations force
`A=B=0`, then leave

```text
E1=(5 kappa/4096)t(3s^2-64t^2),
E2=(5 kappa/65536)s(s^2-192t^2),
```

with no zero on `D(kappa) intersect (D(s) union D(t))`.

Independently reconstruct from the frozen V20R2 tails/source, not producer
scratch:

1. all grade 4..8 equations needed for the `r=2,y=0` conclusion, including
   shifts, target absence/presence, and the correct row-6/row-7 indexing;
2. the translated `w`, the two identities in `A,B`, load cancellations,
   and the final two cubics; find any omitted free coefficient that could
   cancel them;
3. the no-common-zero argument on the actual source open;
4. the claimed necessary consequence `y!=0` for any old-plane r=2 survivor;
5. the proposed grade-7 nonzero-y preflight: verify its equations,
   `Q(y)=0` plane, left/right kernels, and whether only rank-drop/Fitting
   strata remain. State the smallest honest next exact packet and whether it
   should be desk algebra or AWS-only CAS.

Distinguish a finite compatible jet from a formal arc and a polynomial map.
Do not normalize `kappa`, `J0`, or a leading coordinate to 1 without a
licensed action. Do not switch load support.

No web, AWS, heavy local CAS, commit, push, canonical edits, or external
messages. Never read, list, stat, grep, build, modify, or touch `jc2-lean`.
Write only `xmodel/k00-r2-y0-grade8-hostile-review-opus5-93d-20260829.md`
plus `/tmp` scratch. End with an exact body seal and basis. Omit
`charge_basis=` unless a new exit price is truly asserted. Fail closed.
