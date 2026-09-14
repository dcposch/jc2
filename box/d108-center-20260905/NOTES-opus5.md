# d108-center-opus5-20260905 — lane notes

Report: `xmodel/d108-center-opus5-20260905.md` (sealed, body 21665 B,
sha256 9c3b3615d8d18e9a694dd172db778c0a76bf7dd99589f10108515bd36276a2d3).

## Result in one paragraph

The centre half of the commissioned repair succeeds: Moh p.201 (8) gives
`L_2 = lcm{den delta_3} = 1`, so the D2 generic point of the D=108 row admits
exactly one Def 5.1(4) centre coordinate, an integer-`t` term that is a constant
in `y`; the group element is `y -> y + a_1`; that translation is already spent
pinning the minor jet constant to zero, so the repair pays it and frees `jet0`.
With `jet0` free the stage-0 incidence ideal is still the unit ideal (exact-Q
cofactor identity, `CHECK = 1`, specialising at `jet0 = 0` to the identity
`17(ddddd)` published).  But the floor's SLOPE is wrong: the frozen engine uses
`z = pi*s^6` (weight `4r+6q`, face 42) where Def 5.1(3) `delta_2 = 1/4` forces
`z = pi*s^5` (weight `4r+5q`, face `35 = ord_s K3(sigma_D2)`).  On the corrected
chart the twelve nonzero rows are twelve `Q*` pivots on twelve distinct `h3`
coordinates, the residual is empty, and there is an explicit rational point
respecting `c != 0` and `D_2`-minimality.  VERDICT: REFUTED at stage 0.

## Reusable audit recipe for any D_i weight floor

1. `delta_i` from `moh_skeleton_full.Skel(...)._delta` (Def 5.1(3)).
2. `z = w-1 = t*y-1`  =>  z-radius `= 1 + delta_i`; uniformiser denominator
   `den(1+delta_i)`; the generic point is `z = ... + pi * s^{(1+delta_i)*den}`.
3. Cross-check with the exact order
   `ord_s K_j(sigma_{D_i}) = den * (deg K_j + V_{i+1}*delta_i + (deg K_j - V_{i+1})*delta_s)`
   (Def 5.1(1) supplies `V_{i+1}` as the root count of `K_j` inside `D_i`).
   This must equal the face weight.
4. Centre exponents live in `(1/L_i)Z`, `L_i = lcm{den delta_s..den delta_{i+1}}`
   (Moh p.201 (8), implemented as `Skel.L`).  At `i = s-1`, `L = 1`, so the only
   centre coordinate is the `y`-constant.
5. Name the group element for every pin.  The gauge group here is
   `(x,y) -> (x, lambda*y + mu*x + s_0)` (degree `<= d = -delta_s`); `lambda` is
   spent by `z = w-1`, `mu` by the second face root at `w = 0`, `s_0` by the
   minor series lacking its `t^1` term in `w`.

## Status of the sibling row

`(99,66)` = `Skel(99,66,[77,97],{2:8,3:8})`, `delta = (4/9, 1/3, -1)`.  Its
engine passes steps 1-3 exactly (`3r+4q`, face 32, D1 `t=e^9, z=e^12+Pi*e^13`).
Its centre defect is the same single coordinate; on `delta=5/2` the constant
translation is spent TWICE (minor pin plus `"b0":"fixed_zero"` = `Hc_11_0`).

## Artifacts

See `work/`.  `frozen-inputs.opus5.sha256` / `.opus5.check.log` are this lane's
custody; the unprefixed `frozen-inputs.*` files are the partial Astra run's and
were left untouched.  Astra's `replay/` was read but not consumed; where it
overlaps we agree, except that its `minimal_t8z` witness has `jet1 = jet2 = 0`
and so violates `D_2`-minimality — `work/witness-minimal.json` does not.
