# Preregistration: diagnostic-free exact-Q fused rerun

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

The frozen V2 fused source asks Singular for `dim(I)` before `I` is a
standard basis, which emits the benign line `// ** I is no standard basis`.
This successor changes no ideal, saturation, stratum, engine, order, or
normal-form check.  It replaces only that unused display line by

```text
source_dim_not_computed=1
```

and strengthens the runner to reject `no standard basis` and every `// **`
diagnostic.  Run selected-open and boundary-incidence exact-Q programs on
both Box02 `std/dp` and Box03 `slimgb/dp`.  Agreement of diagnostic-free
mirrors is the acceptance endpoint.  The original V2 lanes remain timing and
mathematical controls, not final software acceptance endpoints.

All semantic firewalls in `SEMANTIC_ERRATUM.md` remain binding.  In
particular `Bsrc` denotes the w-horizontal boundary incidence, not a union of
source components generically contained in the boundary.
