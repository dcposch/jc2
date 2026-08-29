# HENS-CT multivariate Ore bridge R1 — preregistration

Frozen UTC date: 2026-08-28

## Narrow charge

This successor addresses only the frozen software boundary in
`cases/ggv_hens_ct_rank_one_control_r0_20260828`.  The pinned stack constructs
the generic associated commutative polynomial ring successfully and then
unconditionally replaces it by `MPolynomialRing_libsingular`.  PassageMath
10.8.10 rejects that replacement when its coefficient ring is itself a
multivariate polynomial ring.

The only exact-arithmetic adapter authorized here is:

```diff
-            except ImportError:
+            except (ImportError, NotImplementedError):
```

in `OreAlgebra_generic.associated_commutative_algebra`.  Thus an unavailable
or incompatible optional libSingular implementation retains the generic Sage
polynomial ring which the method constructed immediately beforehand.  No line
of `ideal.py`, composition, Groebner reduction, uncoupling, creative
telescoping, Ore arithmetic, or the frozen HENS-CT input is changed.

The already reviewed installation-only amendment disabling optional analytic
extensions is retained byte-for-byte.  Both patches and both patched source
files must be hashed.

## Mandatory upstream gate

Before the rank-one control is touched, reproduce the algebraic-integral
example shipped in `ore_algebra.ideal.ct`:

```text
f=(x-y)t^3+t-x^2*y-x^2,
q=t*y,
I=Ann(u*v), composed by u=t,
integrate in y.
```

Success requires all of:

1. the original explicit libSingular constructor still raises the frozen
   `NotImplementedError` (live mutation);
2. the patched Ore algebra uses the generic polynomial-ring fallback;
3. `ct(Dy, certificates=True)` emits nonzero `L` and `C`;
4. `L` agrees up to a nonzero scalar with the operator printed by the shipped
   doctest;
5. exact Ore reduction gives `(L-Dy*C) mod J = 0`; and
6. an independent action in the algebraic field gives
   `L(t*y)-d_y(C(t*y))=0`, using the implicit derivative of `t`.

Only an archived `UPSTREAM_PASS` satisfying all six conditions opens the
rank-one stage.  Any backend exception, empty/zero operator, reducer mismatch,
timeout, or resource stop closes the run without charging the control.

## Frozen rank-one control

If and only if the upstream gate passes, run the exact R0 charge

```text
h=1+X^-3+X^-7,
y^8=1+s*h*y,
Q=X^2*y^2,
E=Q(s,X)[y]/(y^8-1-s*h*y).
```

Success requires nonzero `L in Q(s)<Ds>` and nonzero certificate operator
`C`, exact Ore reduction of `L-DX*C` modulo the composition ideal, serialized
`B=C(Q)`, and the independent direct field identity

```text
L(Q)-d_X(B)=0 in E,
y_s=h*y/(8*y^7-s*h),
y_X=s*h'*y/(8*y^7-s*h).
```

The four-section semi-invariance condition is checked exactly on every
coefficient of `L`.  The R0 iteration limit remains 96.  A candidate is
serialized before each reducer; candidate output is never called a real
certificate unless both exact reductions pass.

## Host and process custody

- Authorized host: AWS r6c, instance `i-040b7a1c2ed72d4cc`, type
  `r6i.16xlarge`.
- Require Linux, Amazon EC2 DMI, the exact instance id, a nonempty job tag
  equal to the fresh namespace basename, at least 450 GiB available memory,
  at least 20 GiB free disk, and `SwapTotal=SwapFree=0`.
- Refuse a competing CAS, compiler, pip, or campaign Python process and any
  process already using at least 2 GiB RSS.
- Fresh namespace only: `/home/ubuntu/jobs/ggv_hens_ct_backend_r1_*/`.
- One registered `setsid` process group.  The worker does not spawn a child
  until the parent records PID=PGID=session, immutable start time, namespace,
  and source hash.  All descendants stay in that session and PGID.
- Guard memory, disk, swap, and descendant census every ten seconds.  Use
  `timeout --foreground`, TERM then bounded KILL only on the validated PGID,
  and require an empty final group census.
- Address-space cap 400 GiB, file-size cap 8 GiB, install cap 1800 seconds,
  full exact pipeline cap 14400 seconds, and outer cap 16320 seconds.

The source payload is made read-only before registration.  The patched tool
source is made read-only before mathematics.  Source, patches, tool freeze,
candidate/final outputs, terminal marker, resource record, registry,
telemetry, and final no-orphan census are SHA-256 manifested.

## Terminal semantics and firewall

`PASS` means a genuine rank-one telescoper/certificate passed both reducers.
`UPSTREAM_PASS` alone means only that the backend adapter reproduced the
upstream proof-of-method example.  `FAIL_*`, `TIMEOUT_*`, and `RESOURCE_STOP`
are software/operational outcomes, not mathematical verdicts.

Even `PASS` proves only that this adapter instantiates exact algebraic creative
telescoping on the frozen rank-one control, which already fails scalar row 23.
It proves no nonlinear nonvacuity, family-uniform cutoff, raw determinant
claim, polynomial descent, branch P/Q result, survivor exclusion, GGV family,
landing statement, Keller theorem, or JC2.
