# Hostile composition review: unit-load D1 strict unique-`AC`, `d=2,3`

You are an independent hostile mathematical reviewer.  Work read-only in
`/Users/dc/code/math/jc2`.  Review the frozen coverage audit

```text
cdd2305804073e771b26d00a22030486a3d8347c6d70c41f4d6a7a7b6482e1c7
  xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-audit-20260826.md
```

and write only

```text
xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-hostile-review-grok-20260826.md
```

Return one top-level verdict: `CONFIRMED`, `CONFIRMED_CONDITIONAL`,
`REFUTED`, or `INCONCLUSIVE`.  A conditional verdict is expressly allowed
because the frozen `a=8,d=3` producer's distinct hostile review may still be
live.  State that exact lifecycle condition rather than silently importing a
provisional result.

## Charged authorities

Recompute these SHA-256 values and all nested manifests/review verdicts:

```text
8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da
  xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-promotion-20260826.md
2ff74f6914a3316104d7a406ca6d6d4ede2cf8332221dfcccd7461f9d925176e
  xmodel/max12-812-order2-square-d1-e-a1d3-opposite-root-pole3-promotion-20260826.md
b5c38f1b2e2e5ec6f2ac32fb350f11686dac5cb45eabe8cf1ea67d20726bd362
  xmodel/max12-812-order2-square-d1-a7-loadtie-dual-functional-promotion-20260826.md
9cc6870289ec0697e438c3999616194d3955e3bc875cd69cad855fd16d28c3b9
  xmodel/max12-812-order2-square-d1-a8-d2-loadfirst-dual-promotion-20260826.md
4c9b9e441d666b91d8255af8aca3978eeccd8263775b33184a1e3334f0fd51b2
  cases/max12_812_order2_square_owner_d1_a8d3_targetshadow_chamber_split_20260826/PRODUCER_FREEZE.sha256
551ca2f6f8aaf75fd67019d055e43ae862150de62d51cb0bd8755d4d0085a19a
  xmodel/max12-812-order2-square-d1-a9-d23-j38-r3-tail-promotion-20260826.md
470ea478c9463d62d39a428962fd9dd5845f4bf882388f84594c82a211634fb8
  xmodel/max12-812-order2-square-d1-age10-cge-a1-source-ceiling-corollary-promotion-20260826.md
```

Also inspect, if present, the distinct cell review

```text
xmodel/max12-812-order2-square-d1-a8d3-targetshadow-chamber-hostile-review-grok-20260826.md
```

and its `.run` custody.  If it is absent or not final, do not decide that
lifecycle condition yourself unless you fully and independently review the
same producer; return `CONFIRMED_CONDITIONAL` if everything else holds.

## Mandatory mathematical checks

1. Recompute the strict unit-load fan from

   ```text
   AC=a+c, C2=2c, R3=3r, RC=1+r+c, A2=4+2a
   ```

   under `a>=1,c>=3,r>=2`, with `d=c-a in {2,3}` and `s=r-a` integral.
   Prove that strict unique `AC` is exactly `s>=0` and `a+3s>d`, with
   `1<=d<=3`.  Keep equality faces out.
2. Independently derive the minimum `s`/`r` table:

   ```text
   d=2: s_min=1 for a=1,2; s_min=0 for a>=3;
   d=3: s_min=1 for a=1,2,3; s_min=0 for a>=4.
   ```

   Confirm that `1<=a<=9` gives exactly 18 disjoint baseline closed
   `R`-tails, with no omitted integral point and no extra equality point.
3. Match every one of those 18 baselines literally to a promoted theorem or
   to the frozen provisional `a=8,d=3` producer.  Verify exact `A,C` versus
   closed `R` language, and that the eleven-block theorem excludes E and
   a=7..9 exactly as claimed.  The navigation-only support miner is not an
   authority and must not be imported.
4. Verify that each finite theorem covers all larger `R` order without
   inverting a leading `R` coefficient.  Audit the exceptional E client, the
   a=7 timing tie, the separate a=8 d=2 and d=3 chambers, and both a=9 tails;
   prohibit extrapolation across them.
5. Verify that the promoted closed source ceiling literally contains all
   `a>=10,c>=a+1,r>=a`, hence every strict d=2,3 tail at high a, including
   arbitrary larger C/R order.  Check that its `CONFIRMED_CONDITIONAL`
   review condition was discharged by the promoted parent.
6. Reconcile localizations.  Finite theorems live on `D(p*k0)` or
   `D(p*k0*J)`; the tail is on `D(J)` after its registered gates.  Decide
   whether the common composition may safely be stated only on
   `D(p*k0*J)` and then conventionally named `D(p*k0)` for Keller sources
   because `J` is a unit.  Do not erase an upstream hypothesis.
7. Determine the strongest common theorem type.  Some inputs are
   scheme-theoretic unit ideals and others rootwise/arcwise exclusions;
   decide whether the union supports arcwise/set-theoretic emptiness but not
   a uniform scheme-structure assertion.
8. Audit qring safety and every relevant producer/review firewall.  State
   the exact first residual D1 cells after this composition: equality faces,
   other primary/tied faces, positive-order leading load, and excluded
   localizations, rather than claiming all D1.

## Firewall

This review may at most license a later composition promotion for the
normalized integral unit-load strict unique-`AC`, `d=2,3` cell on the common
open.  It says nothing about equality faces, primary `C2/R3/RC/A2`, positive
leading load order, `p=0`, `k0=0`, `J=0`, zero/infinity or terminal landing,
the full square component, order two, maximum twelve, or JC2.  If the audit
fails, identify the smallest missing or overlapping `(a,d,s)` cell and the
narrow surviving union.
