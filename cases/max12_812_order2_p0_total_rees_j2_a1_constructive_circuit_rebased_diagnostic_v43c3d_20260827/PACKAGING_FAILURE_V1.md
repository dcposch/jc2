# V43C3D v1 packaging failure

The first frozen diagnostic wrapper/source bundle used an AWS lane tag beginning
in `...rebased_v43c3d_`.  The wrapper accepted that tag, but the independently
pinned V43C3 producer correctly required `...rebased_v43c3_`, so it failed
closed in `require_aws` before proof construction (rc 1, 0.10 seconds, maximum
RSS 32,336 KiB).  This has no mathematical verdict.

The additive v2 launcher uses a tag beginning
`...rebased_v43c3_diagnostic_v43c3d_`, which is accepted by both the original
V43C3 prefix guard and the stricter v2 diagnostic sentinel.  No mathematical
derivation or V43C3 producer byte is changed.
