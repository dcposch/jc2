# Post-verdict playbook for open_8_28_c2_v6.p65521

## If GB = [1]  (subcase (2) empty mod 65521)
1. Confirm at p=1048573, p=2147483629, strict variant  — already queued in lane 2.
2. Run the characteristic-zero-header core
   (`systems/open_8_28_c2_v6.q.ms`, queued lane 2).  An msolve `-g` `[1]`
   alone is only `FIRST-PRIME-EMPTY (NOT Q-EMPTY)`.  Upgrade it by extracting
   an exact rational certificate via Singular `lift(I,1)` and checking that
   identity independently with FLINT; only that verified identity is `[1]`
   over Q.
3. Subcase (1): `open_8_28_c1_v6` (73-var core, queued). BOTH subcases empty over Q
   + (yet-to-be-done) verification of the Cascade3 reduction over Q, audit of
   Generator A against Prop 4.3, and G0 string-identity regressions
   => the (8,28) family is discarded => degree bound becomes 125.
4. Then: write up (methods + certificates + code), contact GGV.

## If GB != [1]  (solutions exist mod p)
1. Extract solutions: msolve -P 2 (rational parametrization / RUR) on the core.
2. Exact side-condition checks: corner nonvanishing (incl. strict-mode origin
   corners), reconstruct eliminated b's via the Cascade3 substitution log,
   verify [P,Q] = x^2 by direct bracket arithmetic mod p.
3. Repeat at the other two primes; compare solution counts/degrees.
4. If solutions persist across primes: attempt Hensel lift / char-0 RUR
   -> a candidate leading-tower for a (108,72) counterexample. Handle with
   care and immediately.
