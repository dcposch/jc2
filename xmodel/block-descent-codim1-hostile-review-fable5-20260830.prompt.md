# Hostile proof review — intermediate block descent via codimension-one image

Identity: Fable 5, different-model hostile reviewer. Work in
`/Users/dc/code/math/jc2` on frozen basis
`0f7ee003be45ee40d51d4048897cdacf63821172` plus the sealed reports below.

Read and hash-verify:

```text
72aa958a0e69606886e035fecca8c85790ec2bb3ebc20c065938879fcdddd297
  xmodel/ideation-20260829T2254Z-sol56-alt.md
  body 28201 / 0477ab88d170343f70b1f353e88d7f112bc35308631228cdf85302c472b83fd5

6e48015c296c9677237daee2a21a20195d5fc346e163dbcbaa68b74e46bab296
  xmodel/ideation-20260829T2254Z-crosspoll-opus5.md
  body 53234 / 647bca6600e31816c1f7ac14f2b061d7be574cf653d7102ac063375627d0346b

e1ce01691b8ba4366a2249c3653830e0219f6f611ae5b782b34eb2da183a5971
  xmodel/ideation-20260829T2254Z-crosspoll-fable5.md
  body 42096 / 0c2adb5a883121d2151fdd92f2ce7182f0cc7b84b3e15961b2d6bd2bc92da599

a6cc7385b6a2fbb0c92db05a3052dfe14b083d04d3e049e7006923f7f3b293ca
  xmodel/sol-lateral3.md
```

The narrow new claim to attack is Opus cross-pollination §5.3. Given a
hypothetical polynomial Keller counterexample `F=(f,g)` and a proper
intermediate field `C(f,g) subset K subset C(x,y)`, put `B_K` equal to the
integral closure of `C[f,g]` in `K`, `Y=Spec(B_K)`, and factor

```text
A2 --g1--> Y --g2--> A2,   F=g2 o g1.
```

Independently prove or refute every step:

1. `B_K subset C[x,y]`, module-finiteness over `C[f,g]`, normality of `Y`,
   and the exact dominance/quasi-finiteness status of `g1`. Do not assume
   `g1` finite, proper, surjective, or etale at singular image points.
2. At every smooth codimension-one point of `Y` lying in `g1(A2)`, determine
   whether `dF` invertible forces `g2` etale there. State all characteristic
   and separability hypotheses.
3. Audit the purity step: if `g1(A2)` contains every codimension-one point of
   `Y`, does finite `g2:Y->A2` become etale everywhere? Name the exact purity
   theorem and verify its hypotheses despite possible singularities of `Y`.
   Then check whether connected finite-etale `Y->A2_C` must be an isomorphism.
4. Decide the strongest contrapositive for a nontrivial block: must `g1`
   miss a divisor of `Y`? If so, prove or refute that its finite image under
   `g2` lies in the Jelonek nonproperness set `A(F)`. Keep a missed divisor,
   a branch divisor, a nonproperness component, and a missing value distinct.
5. Compare this criterion with the older `Y ~= A2` recognition target. Is it
   genuinely weaker than properness/JC2, a tautological restatement of
   nonproperness, or a useful bridge to Avenue 7/26/31? Identify the cheapest
   next theorem or countermodel. Test at least one finite non-Keller
   factorization and one open-immersion/quasi-finite control.
6. Audit the minimal-topological-degree factor argument separately. Do not
   infer that a minimal counterexample has primitive monodromy unless the
   codimension-one hypothesis is actually proved.

Return `CONFIRM`, `CONFIRM_WITH_CORRECTIONS`, `REFUTE`, or `OPEN` item by
item, the maximum exact theorem safe for promotion, and one prove/falsify/
bypass launch with stop conditions. This is desk commutative algebra only;
no heavy CAS is expected.

Write exactly
`xmodel/block-descent-codim1-hostile-review-fable5-20260830.md` plus scratch
under `/tmp`. No web, AWS, canonical edits, commit, push, or any
inspection/list/search/stat/build/modification/control of `jc2-lean`. End in
one standalone `<!-- BODY-END -->`; do not add a seal. No exit price is
asserted, so omit `charge_basis`. Fail closed.
