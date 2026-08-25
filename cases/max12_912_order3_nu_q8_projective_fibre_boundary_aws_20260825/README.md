# Selected-Q8 projective fixed-fibre boundary probe

This AWS-only secondary probe tests whether the **global-family** standard
projective homogenization has any point at infinity over `w=25`.  It uses the
same eliminated localized six-row source as the live generic-length races,
with internal affine coordinates

```text
(u,c,d2,d4,x1,x5,v),   x3=(v+2)x5,   u=inv*x5,
u*x5*v=1.
```

The six rows and localizer are homogenized only in the seven internal
coordinates, with `w` retained as the affine base coordinate.  Seven standard
projective charts are tested independently at `w=25,t=0`.

If every raw homogenized chart is empty, then the true saturated projective
closure also has empty boundary over `w=25`.  Combined with the separately
frozen affine fibre length `190`, properness and upper semicontinuity bound the
generic localized length by `190`.  If any raw chart is nonempty, no negative
mathematical conclusion follows: the point may be an artefact removed by
`t`-saturation, and a separate saturated successor is required.

Every substantive run is remote.  A lane is evidence only when its generator
and Singular endpoint are fail-closed and its input/source hashes are pinned.

