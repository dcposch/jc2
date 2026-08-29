# GGV upper endpoint: exact field-valued tail-7 obstruction

Date: 2026-08-28 UTC  
Author: Sol Ultra (`/root/reduced_endpoint_seed`)  
Status: producer report; requires different-model hostile review before promotion

## Result

There is no characteristic-zero field-valued solution of the frozen raw
branch-P endpoint equations on the square-tail specialization in which every
raw parameter of weight below 7 is zero.  This is an exact negative result for
the **entire tail-7 endpoint stratum**, not merely for the earlier normalization
`p87=1,p32=-1` or its two rational subbranches.

No literal raw endpoint point is banked.  This task therefore produced a
minimal exact obstruction rather than the requested positive seed.  It does
not exclude the tail-6 stratum, the unrestricted branch-P endpoint family, or
any other endpoint branch.

## Exact proof

Let the frozen tail-7 linear-nullspace coordinates be `p0,...,p87`.  Replaying
the triangular eliminations over `Q`, while explicitly withholding `p32` and
`p87` from the pivot columns, gives the literal endpoint equation

```
-1 - p32*p87 = 0.                                      (E)
```

Thus every endpoint point over a field has `p87 != 0`.  At row 21, one exact
left-cokernel compatibility is

```
-(3/4)*p86*p87^2 = 0.                                  (C21)
```

In characteristic zero, (E) and (C21) force `p86=0`.

Independently, constant-coefficient elimination of the 11 same-row parameters
`p33,...,p43` from the 26 row-14 equations has rank 10, leaves the single free
mode `p43`, and gives 16 nonzero compatibility equations.  Every monomial in
these compatibilities has degree exactly 2, and their support is exactly
`p78,...,p87`.  They are therefore homogeneous quadrics in the ten displayed
F7 coordinates.

For a putative endpoint field point, divide those ten coordinates by the
nonzero scalar `p87`.  Homogeneity makes this a valid dehomogenization of the
necessary row-14 subsystem; no symmetry of the full residual system is being
asserted.  With `p87=1` and the already forced `p86=0`, the 16 equations reduce
to quadrics in `p78,...,p85`.  Their ordered canonical term bytes have SHA256

```
30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257
```

and are byte-identical to the previously frozen 8-variable shared block.  The
audited AWS exact-Q calculation on that block literally returned
`BASIS_SIZE=1`, `UNIT=1`, and `J[1]=1`.

There is also now a compact Nullstellensatz certificate independent of that
status line.  `liftstd` returned a constant basis element `36036` and 16
cofactors.  After division by `36036`, the separately frozen script, which does
not call a standard-basis routine, expands and verifies

```
1 = h1*f1 + ... + h16*f16.
```

Only `h1,...,h4,h13,...,h16` are nonzero, each of degree at most 2.  Its literal
output is `DIRECT_REPLAY_LHS=1` and `DIRECT_REPLAY_OK=1`.

This contradiction proves the result.

## Scaling firewall

The earlier affine normalization must not be described as WLOG for the full
tail-7 residual.  A diagonal-grading check on all 198 reduced constraints gave
4018 monomial-weight relations of rank 86 and nullity 2; the only free gradings
are the silent coordinates `p46` and `p77`, while `p32` and `p87` have weight
zero.  Thus there is no licensed global diagonal torus action normalizing
`p87`.

The proof above needs no such action.  It normalizes only the homogeneous
row-14 necessary subsystem after (E) proves `p87` nonzero.  This distinction is
essential to the promoted scope.

## Reproducible custody

Primary source lineage:

- authoritative raw system:
  `ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`
- reviewed tail compiler `tail_deformation.py`:
  `a411d66158b01e3baf611067e29b223d88370bf01e7c8d84e09e87e72023f626`
- frozen tail-7 deformation JSON:
  `7edd5ccd471e9eb3e27f0f163b0b337e0fb5057126ec69869f988093defba7aa`
- projective compiler:
  `f107f9994fd710dbe7036b57bca08021067692976c31371e07f85493bff74d7f`
- independent projective verifier:
  `7762f8d84796674215c915908de003db435efa77a5daf8b9eb984ad4b37f44e9`
- projective case manifest:
  `29ffa224682d8f424b1ff5f33fc8c1227e8805f1b67cec0610b74fcc14599955`

Frozen proof objects under
`cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828/`:

- homogeneous row-14 system:
  `5ba0f08eeaf9023d45e64563c82269c57202ac0596208a06145d1bccd793afdf`
- symbolic localization certificate:
  `291fff50be2573ce1e6a04f5fadecbb95b728506dce522c4f1a465905e9bc831`
- localized 8-variable block wrapper:
  `ea41511595d4cf906a06778ebdf80c69ba8f24f92b693e366a3fd9d8ac1cefa1`
- `liftstd` certificate source:
  `3258a17ac3402c2db9f53423445a179846c78699ff22deec243b49e561841bca`
- direct identity replay source:
  `255aa3ac1db1594a84faa5fd178482ab6b002f0df9d18c2531dd85bdb51efbdc`
- frozen direct-replay stdout:
  `24250ce63900adca4899bf4c4d6e7b045e47e34c3c54d6efabec5b4d49addabf`
- frozen full cofactor stdout:
  `cd946a2f1906a23978f8be97c766235e2a061030086ed4ab3ae7fa084ef7de1c`

The exact 8-variable source remains
`cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/BRANCHES/shared_block.json`,
SHA256
`3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab`.
Its exact-Q Singular source is
`458dce839bce84004be992e146603f05dbce4a1716c5717a4c7ac130e2e1707c`.

Audited AWS evidence is under
`cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/AWS_R6D_SHARED_BLOCK_20260828T010806Z/`.
The evidence-manifest SHA256 is
`559c028e258c344179b65f7e45f517e1265be9ff3e433a6791ee88ac5b998ccc`;
the literal engine stdout SHA256 is
`85d3aad67e459f6f7d8e84556ccfc462cf15eff6ed37ab51a21cda2559eb64c0`.
The AWS engine was `/usr/bin/Singular` SHA256
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
It used one core, an 8 GiB cap, a 1,800 s cap, and zero swap; it finished in
0.07 s at 10,328 KiB maximum RSS.

Local certificate replay used arm64-Darwin Singular 4.4.1 (44105), binary
SHA256
`d31b5138a4ed6fdc1be66d77df99758772fa36d1c7173b10065b7dbdb17089ca`.
Both the `liftstd` construction and direct identity expansion terminated in
0.00 s with about 5 MB maximum RSS and zero swap.

Replay from the projective case directory:

```
sha256sum -c SOURCE.sha256
python3 -B verify_projective_r14.py
/opt/homebrew/bin/Singular -q R14/r14_nullstellensatz_replay_q.sing
```

Expected terminal markers are `status: PASS`, `DIRECT_REPLAY_LHS=1`, and
`DIRECT_REPLAY_OK=1`.

## Corroborative normalized branch descent

Before the projective promotion, the normalized 41-variable residual exposed
four sparse equations in `a=p68,b=p60,c=p54`:

```
4+6b-8a+(32/9)a^2 = 0
3/2+6c-(3/4)b+4ab-3a+(4/3)a^2 = 0
c(-3/4+4a)+b(-9/8+(3/2)a) = 0
c(-9/8+(3/2)a) = 0.
```

Their exact characteristic-zero solutions are only `(3/4,0,0)` and
`(3/2,0,0)`.  Indeed the last equation splits at `a=3/4`; direct substitution
forces `b=c=0` there, while off that branch the last two force `c=b=0`, and the
first then factors as `(32/9)(a-3/4)(a-3/2)`.

After substitution and exact linear cleanup, each branch had 143 equations in
31 operative variables.  Pivot parameters were `[43,44,45,49,75]` on the
`a=3/4` branch and `[43,45,49,53,75]` on the `a=3/2` branch.  Frozen branch
JSON hashes are respectively
`a887e6197293f0b0229ed27f06e40149912d2c4fb7a0f9de1a2c8d69ddec6e4d`
and
`b1bb657096e6e7936f86ab76adadf39a62f85d57c14b592f450689d09f4051a4`.
Both contain the same unit 8-variable block.  These branches are now
corroborative only; the generalized proof does not depend on their exhaustivity
inside a globally normalized full residual.

## History and next rung

The bank/history check found no exact raw witness satisfying literal
`D0=...=D21=0,D22=1`.  The previously reviewed tail-11 and tail-10 sections
specialize row 22 to an exact unit.  Fresh exact desk compilation showed the
same literal `-1` endpoint obstruction for tail 9 and tail 8.  Tail 7 was the
first endpoint-capable square-tail rung; the argument above now eliminates it
over characteristic-zero fields.

Stop rule: retire tail 7 after hostile review confirms the source lineage,
symbolic row-21 relation, homogeneous dehomogenization, byte match, and direct
identity.  Continue only at the separate tail-6 rung, beginning with its
triangular structure and smallest mandatory localized compatibility block.
Do not launch the full tail-6 residual before those reductions are exhausted.

## Claim firewall

This report establishes no raw endpoint point and no counterexample.  It makes
no claim about the unrestricted branch-P endpoint, other GGV branches, scheme
emptiness/nonreduced points, or JC2.  It may be promoted only as a
characteristic-zero **field-valued tail-7 specialization obstruction**.

