# Hostile different-model review — TD6 moduli-uniform third-band gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/td6-moduli-uniform-third-band-20260824.md`
- every file under `cases/td6_moduli_uniform_third_band_20260824/`
- the producer and confirmed review for the parent TD6 moduli-uniformity gate
- the earlier first-band, pointwise next-row, and paired-third-band gates and
  their landed reviews

Frozen child hashes:

- report: `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b`
- replay: `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8`
- freeze: `0685b4412f6cb65f8b6556ede01d63c2652a508d08dc76ba57cf53b351254da9`
- canonical stdout: `c5c3417f3ba32574a778126de4cbc2bab5ee1f4528a17d3f86b106b68cbbd2ea`

Independently rerun the replay and attack exactly:

1. Verify all inherited source typing and the exact specialization: rectangles,
   `p=t^15`, `q=t+t^25`, center `(1,1,1)`, zero dead stretch, reduced F1
   boundary pattern, source relation, and pole normalization. List every
   modulus still fixed rather than quantified.
2. Rebuild enough of the parent transport to confirm ranks `3508/3602`,
   `36/94`, the 58-dimensional affine family on
   `Q=-2*S^2+2*S+5*D-3=0`, and consistency/rank two of the inherited pole
   row. Check for imported-hash, coordinate-order, or denominator errors.
3. Independently derive `f_(2,1)=0`, `f_(3,0)=H^3`, and
   `[s^0*t^0]J-1=3*(1-S+D)^3-1`. Substitute the moduli curve and recompute
   the sextic `F(S)` exactly; make sure no free affine parameter can enter.
4. Verify Rabin irreducibility modulo 31, squarefreeness, and every source-open
   saturation gcd. Confirm that the sextic leaves exactly six licensed
   complex `S` values rather than introducing or losing a boundary branch.
5. Audit the degree-18 residue field. Recompute
   `N(alpha)=3^28/5^96`; check that its 3-adic valuation proves
   `A^3-alpha` irreducible over `K=Q[S]/(F)`, and that `1,A,A^2` is therefore
   a valid basis at all six roots.
6. Independently compile or verify all 40 coefficients of `[s^0]J-1`, the 35
   nonzero rows, homogeneous rank `25/58`, and the exact left-null
   certificate. Multiply the certificate into the unreduced matrix and
   recompute the degree-four residual, especially its nonzero
   `(136875/29)A` coefficient.
7. Check that the nonzero residue excludes every one of the 18
   pole-normalized conjugates and that the quadratic pole band is genuinely
   unused. Look for field-special rank jumps, conjugate-specific vanishing,
   or a mismatch between affine and homogeneous systems.
8. Enforce scope. The admissible conclusion is emptiness of this one fixed
   normalized reduced-boundary family at the centered band. It does not kill
   SP-2, any terminal class, the broader boundary/dead-stretch moduli, or JC2.
   Identify the smallest valid deformation successor.

Use an independent derivation or second exact engine wherever practical. Try
hard to find a source-typing, field, rank, or left-syzygy error. Do not edit
producer/canonical files, broaden the computation, or launch AWS.

Write exactly one report file:

`xmodel/td6-moduli-uniform-third-band-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent replay, exact scope, and promotion advice.
