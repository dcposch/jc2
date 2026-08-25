# Preregistration — reduced rational cokernel at the common-cubic witness

Consume the frozen exact `299 x 149` Jacobian/residual payload at the one
normalized common-cubic mod-`3^11` witness.  Compute an exact primitive basis
of its 153-dimensional rational left kernel and pair it with the literal
residual.  Independently re-evaluate the source equations under the three
certified rational right-kernel directions: target translations of `P` and
`Q`, and the degree-compatible shear `Q -> Q+tP`.

The purpose is to type the Lyapunov--Schmidt object correctly.  If all three
right-kernel directions are exact gauges, then their raw rational-cokernel
map is constant and the rational kernel disappears after quotient.  The
non-gauge singular successor is instead the mod-3 tangent kernel modulo these
gauges, paired with the mod-3 cokernel.  Report both dimensions exactly.

Do not call the raw left-kernel pairing a full Kuranishi map: transverse
image-coordinate elimination and nonlinear left-cokernel compatibility are
still required.  No lifting or nonexistence inference is licensed.
