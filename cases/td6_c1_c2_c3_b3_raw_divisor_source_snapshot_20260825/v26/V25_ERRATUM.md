# V25 erratum to V23

V23 failed before source construction in both pivot orders because the shared
`b3tq`/`b3half` setup unconditionally asserted `t^2-4t+2=0`.  That relation is
licensed only for `b3tq`; the `b3half` branch licenses the rational value
`t=1/2` instead.

V25 changes only that branch guard and the bundle/runner names.  It asserts
`t^2-4t+2=0` for `b3tq` and `t=1/2` for `b3half`.  No matrix, source equation,
pivot policy, compatibility target, or certificate code is changed.  V23's
empty stdout and exact assertion failure remain a typed negative control.
