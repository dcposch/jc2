# Hostile different-model review — `(9,12)` DZ20 stabilizer/valuation exclusion

You are the fresh hostile different-model reviewer.  Work in
`/Users/dc/code/math/jc2` at committed ancestor basis
`1144839652c6a4750b9b0cd43e21d80cc9a755eb`.  The producer artifacts are
newer frozen working-tree bytes.  Read in full:

- `xmodel/max12-912-order3-dz20-stabilizer-valuation-20260824.md`;
- every file in
  `cases/max12_912_order3_dz20_stabilizer_valuation_20260824/`;
- the named preflight, Faber, order-three fibre, and their completed reviews;
- `xmodel/pinchuk-quasipolynomial-reduction-source-audit-grok-20260824.md`
  only as a scope warning: Pakovich--Zvonkin unitrees are not a complete list
  of all equality pairs, and the producer must not need that overread.

Frozen hashes:

```text
producer report  4a5ec8b08aab7a9ba5d7c22593efeb67621fea720128dd7051972f52cc9191e5
registration     801295a8f622fe711527613c942166c9f1e768b24aeea2485b85de92bc66e476
README           7d0faaf0ec6427e1585e54ed807f62d96288603b68d1c2618325c234f099be28
replay.py        da97811fe6292c7de7caabbbb8a9159e00b3dfd9b551155607d904b35dfa6173
replay.json      bc11592d197be05d5360f0294b2f111e8382558d071291af4810856a8d75dca6
MANIFEST         78719e904cac78806752b4d8b895b9a319e9422d5803aff468075607bcdd3695
FREEZE           f1ee7e72a0e7a097141a95fbb888103b3456619316c4bf903e668f666b40082a
```

Verify the manifest and replay, but treat them only as regression.  Rebuild
the proof independently and attack every load-bearing arrow:

1. **Spectral input and coprimality.**  Re-derive the exact Faber specialization
   at `k=mu=nu=0`, why terminal nonzero `r8` gives exactly
   `deg_z(g^3-f^4)=16`, and why a constant nonzero differential Jacobian makes
   `gcd(f,g)=1`.  Flag if the registered claim is conditional on more than it
   says.
2. **Passport.**  Starting from degrees `9,12`, coprimality, and degree 16,
   prove or refute that `B=3g_z f-4g f_z` is a nonzero `z`-constant; check
   simple roots, the unique index-20 point, all sixteen finite points over
   one, and the full Riemann--Hurwitz ledger.  Search for repeated-root or
   cancellation counterexamples.
3. **Isotriviality without the classification overread.**  Prove directly
   from finite transitive permutation triples / three-point covers that over
   `C(x)` the pair lies in one of finitely many constant source-PGL2 orbits.
   Do not use a purported Pakovich--Zvonkin classification of all pairs.
   Check descent over the function field, twists, and whether factorization
   of `beta` really recovers `(f,g)` up to the claimed common scaling.
4. **Affine normalization and stabilizer.**  Verify that the unique index-20
   point fixes infinity, depression kills translation, and the full ambiguity
   is a cyclic scaling group of order `e|gcd(36,20)`, hence `e=1,2,4`.
   Challenge wild/nonfaithful actions, fixed generic points, scalar changes of
   `f,g`, and extra target roots of unity.
5. **Descent parameter.**  Independently prove `eta=lambda^e in L`.  Audit the
   coefficient-exponent gcd argument in every support shape, including
   symmetric templates and possibly vanishing nonleading coefficients.
   Derive Kummer covariance and
   `sigma(eta)=zeta^(-e)eta`, not merely up to an uncontrolled constant.
6. **Exact table.**  Recompute
   `(e,N,a,S)=(1,20,2,14),(2,10,1,4),(4,5,2,4)` and
   `R=C h^(-S)v^(-N)` from the leading coefficient of `W` and
   `r8=u^2R`.  Check all signs, powers, eigenspaces, and constants.
7. **Finite valuations.**  Rebuild both the noncancelled and cancelled local
   balances of `9hR'+6h'R=j`.  Verify `m=3 mod N`, why `m=3` is impossible,
   why no cancelled branch survives, and why `v` has no divisor where `h` is
   regular.  Try explicit Laurent series through the first post-cancellation
   term rather than trusting order slogans.
8. **Infinity and conclusion.**  Check the sum-of-orders sign, leading power
   and coefficient at infinity, `D>3s`, the forced `s=1`, and the final use of
   `3|D` plus algebraically closed constants to make `h` a cube.  Test all
   three stabilizers and the terminal positive control independently.
9. **Scope.**  Decide the smallest failing identity or missing hypothesis.
   Do not promote the result to common-factor strata, nonzero loads, the
   order-one core, all `(9,12)`, maximum twelve, a counterexample, or JC2.

Use exact hand derivations and an independent scratch script if useful.  Do
not edit producer, case, canonical, ladder, coordination, prompt, log, run,
or erratum files.  Do not launch AWS.  Write exactly one report:

`xmodel/max12-912-order3-dz20-stabilizer-valuation-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim, checked
hashes, exact independent evidence, promotion language, and quarantine
language.
