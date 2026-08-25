# Affine-only shard of the selected-Q8 sparse mixed volume

This independent AWS shard imports the pinned full mixed-volume producer and
computes only the origin-augmented seven-dimensional mixed volume.  It exists
to put the coordinate-boundary-safe number on the critical path while the
full raw/affine/control replay continues elsewhere.  The full replay, not
this shard alone, supplies the standard-polytope controls.

