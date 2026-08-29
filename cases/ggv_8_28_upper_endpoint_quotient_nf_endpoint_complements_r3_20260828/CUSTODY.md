# R3 custody

- preregistration SHA:
  `781edcad4a5a524337a4717dca8344ef736af56177495ef1a51ee2d09c0c7fb0`;
- source manifest SHA:
  `ad043d20f6ea11040905658d40e5c0f07ec74efd1a3e8403316de61233b22d7d`;
- source archive SHA:
  `ad22770a90e2b807ba969e21b750d69ddbc28b859690c3f3b7e98899cc733367`;
- hostile/positive preflight archive SHA:
  `08efb73a5490c94a48af8eeab606303d986e463401e79941c14afdeb6c5929d0`.

All six terminal archives and remote checksum sidecars are stored under
`custody/terminals`. Every supervisor recorded swap-violation flag zero and worker
return code zero; the nonzero stage/component return codes are preserved inside
the relevant archives. None of these archives was mutated during reclassification.
