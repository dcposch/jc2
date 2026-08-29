# V43C3D v2 packaging failure

The additive v2 tag bridge passed both AWS prefix guards and reached the final
diagnostic interception in 1.38 seconds.  It then failed closed because V43C3
had already created the output directory and the v1 interceptor redundantly
requested `mkdir(..., exist_ok=False)`.  The failure occurred before a
diagnostic file was written and has no mathematical verdict.

V3 retains both frozen predecessors and adds only an output-directory
idempotence shim: the first exact creation is unchanged, while the second call
is accepted only if it names the same already-existing registered output
directory.  No proof construction, guard, root, or polynomial operation is
changed.
