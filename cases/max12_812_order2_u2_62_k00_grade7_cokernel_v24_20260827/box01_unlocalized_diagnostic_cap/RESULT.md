# V24 hostile-review unlocalized diagnostic: resource cap

Date: 2026-08-27

The additive Box01 diagnostic computed a standard basis of the frozen
mod-65521 prior ideal without the Rabinowitsch localization.  It reached the
registered 3600-second timeout with exit status 124 and no algebraic result
marker.  Maximum RSS was 7,472,536 KiB; the timing record reports zero swaps.

Outcome:

```text
RESOURCE_CAP_NO_VERDICT
```

This gives no answer to whether the unlocalized modular prior ideal is empty
or whether its geometric support lies in `k10_0*W=0`.  It changes neither the
reviewed exact conditional V24 theorem nor the localized modular-unit result,
and it has no characteristic-zero, stratum, jet, arc, closure, or JC2 scope.

Frozen harvested bytes:

```text
6ea4bb09fb1dd8abfbe29143528b1d80589dcbc4d253594b45e426feed0e6228  unlocalized_probe.sing
13e3271c6c2c9a751f30a3a380b1c70b0fcb0b97dddd093e0e41452dfe2edeed  unlocalized.stdout
6102887f5893bbf9db5bac694a7ec02d09d154bb690c8d57215a67145d8958c0  unlocalized.stderr
```
