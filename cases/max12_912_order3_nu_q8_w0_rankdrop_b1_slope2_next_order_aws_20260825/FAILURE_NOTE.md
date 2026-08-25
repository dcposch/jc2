# Launch negative controls

The first Box02 and Box03 launch tags (`..._v1`) failed closed before source
generation because the rsynced runner lacked an executable bit and the
launcher invoked it directly.  Their immutable `launcher.stderr` files say
`Permission denied`; no `input.sing`, `runner.rc`, or mathematical output was
created.  They are custody/software negative controls only.

The accepted `..._v2` tags invoke the same pinned runner explicitly through
`bash`; both regenerated the source and completed rc zero.
