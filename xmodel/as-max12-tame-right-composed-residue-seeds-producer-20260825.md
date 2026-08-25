# AS max-12 tame right-composed residue seeds

Status: **PRODUCER-EXACT / PROVISIONAL PENDING DIFFERENT-MODEL REVIEW**

## Result

Over `F_3`, the Artin--Schreier map

`A(s,t)=(s-s^3,t)`

has determinant one and three-to-one fibres.  Two integral tame source
automorphisms move this seed to the two degree pairs at the live maximum-12
frontiers while retaining unit leading `y` coefficients.

For

`u=x+y^3`, `v=y+u^4`,

put

`G9=(u-u^3,v)`.

Then `deg_y(G9)=(9,12)`, its total-degree pair is `(9,12)`, and its leading
`y` coefficients are `(-1,1)`.

For

`u=x+y^4`, `v=y+u^2`,

first form `(u-u^3,v)` and then apply the determinant-one target operation
`(P,Q) -> (Q,-P)`.  The result

`G8=(v,-(u-u^3))`

has `deg_y(G8)=(8,12)`, total-degree pair `(8,12)`, and leading `y`
coefficients `(1,1)`.

The terminology matters: these maps are tame **right-compositions** `A∘B`,
or source-coordinate transforms.  They are not group conjugates
`B^{-1}∘A∘B`.

## Exact checks

For both choices `B=(u,v)`, the displayed integral inverse is

`y=t-s^k`, `x=s-(t-s^k)^m`,

and exact composition in both directions is the identity.  Also
`det J(B)=1`.  Before the target swap/sign, exact calculation over `Z` gives

`det J(A∘B)=1-3u^2`.

Consequently both reductions have literal polynomial determinant one over
`F_3`.  Since `a-a^3=0` for every `a in F_3` and `B` is bijective, each
reduced map has exactly three image points, each with a fibre of size three.
The replay enumerates all nine points and verifies that exact census rather
than inferring it only from the formula.

## AWS custody

The authoritative source hashes are:

- `PREREGISTRATION.md`: `d7196367ba917d692a965eb6d5eab44bdecb8157ca43712a08a873d9e07b574a`;
- `README.md`: `f0ed37894c2208828b3068245041b29c34be09a72bedbe903563467fde7fd086`;
- `verify_seeds.py`: `3bca7ac19da1eeda9c5999f578a3717121fe970afebb12b801db6cb5ea784947`.

Box02 (`ip-172-30-0-186`) and r6d (`ip-172-30-0-45`) independently ran
Python 3.12.3 / SymPy 1.13.3 under
`/home/ubuntu/jobs/as_frontier_tame_right_composed_seeds_20260825T1612Z_v4`.
Both returned rc zero, empty stderr, and byte-identical stdout SHA256
`1653dd2c98046bcb188ea6a5cf07bb77237dc241f9fa19d722e2d34ae0d3ca38`.

The earlier `T1600Z` attempts stopped at an absent-SymPy environment before
the replay ran.  No mathematical claim rests on those environment failures;
the clean `v4` runs above are the frozen evidence.

## Meaning and firewall

These seeds remove one narrow software/strategy obstacle: the ordinary
untransformed AS presentation has `3`-divisible high-`y` coefficients in
several monic-normalization interfaces, whereas these two residue
presentations already have unit leading `y` faces at degrees `(9,12)` and
`(8,12)`.

They do **not** prove that either seed lies in the normalized Q8 or TD6
source-typed chart; denominators and source reconstruction at `p=3` remain
open.  They also prove no lift modulo nine, no compatible all-depth branch,
no characteristic-zero Keller map, no counterexample, no maximum-12
theorem, and no resolution of JC2.  The next direct gate is the complete
degree-at-most-12 determinant-one lifting scheme above each seed, starting
with its full first-digit affine system and retaining every determinant row.
