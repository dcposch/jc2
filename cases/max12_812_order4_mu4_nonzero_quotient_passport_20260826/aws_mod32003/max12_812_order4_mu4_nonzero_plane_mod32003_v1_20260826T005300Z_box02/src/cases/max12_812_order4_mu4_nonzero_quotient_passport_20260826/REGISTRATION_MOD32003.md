# AWS registration: corrected-V2 mod-32003 plane/torus witness

Date: 2026-08-26

Status: preregistered; screening/certificate-support only.

- tag:
  `max12_812_order4_mu4_nonzero_plane_mod32003_v1_20260826T005300Z_box02`;
- host: Box02, `i-010201a5da47795c4`, public IP `34.203.207.55`, expected
  hostname `ip-172-30-0-186`;
- same-named directory under `/home/ubuntu/jobs/`;
- compiler SHA-256:
  `97372842cdc61579767e8f7b3083a1af4ab1ff80d861da526f3618ef65fa97af`;
- runner SHA-256:
  `f149c7643720d5364490cf931993e4b41f5917c6391a994b3a18e15de1a2d1c4`;
- corrected V2 source-input SHA-256:
  `5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47`;
- timeout `3600 s`, cap `67108864 KiB`, characteristic `32003`.

The client redoes both source-presentation checks and the `r_7` saturation
from corrected V2 source, computes and factors the plane elimination, and
tests absence of singularities in the coefficient torus.  It does not by
itself prove characteristic-zero elimination, birationality, or
nondegeneracy of every boundary face.  If the eventual exact-Q plane
polynomial reduces to this relation and the face tests also pass, a unit
torus-singularity ideal modulo `32003` is an exact witness that the
corresponding characteristic-zero discriminant is nonzero.  Otherwise the
endpoint is screening-only or **NO VERDICT**.
