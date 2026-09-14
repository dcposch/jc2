# Independent audit of the implemented D108 free-mean adapter

Audited adapter: `d108/meanfree_stage.py`, SHA-256
`6a35b6d19b1a0103bef46249d1f04860bbce44b6f47a5bbc6506e2c68e4df512`.
The implementation agrees with the approved full-quadratic repair.
Existing frozen engine files and previously hash-bound proof files were
not modified by this audit.

The adapter keeps the same h3 coefficient box and the same strict minor
arc, with jet0 free. It changes only incidence row(8,1) by -2mu and
row(8,0) by +mu^2. The former -c and +pi^2 target subtractions remain.
This correctly imposes the actual h3 face `-((pi-mu)^2-c)`. The new
mu is omitted from the initial h3 elimination-variable set, retained in
the output coefficient ring, and never appears as a solved pivot.

The target-table replacement emits every coefficient of
`((pi-mu)^2-c)^12` for F and its eighth power for G. No mean term or
odd pi coefficient is omitted. Setting mu=0 recovers every original
raw incidence row and both complete original target polynomials.
The scheduled pole powers through12 do not reach the F/G leading
powers96/64, but defining the correct complete targets prevents a
latent error when those depths are eventually reached.

The in-memory gauge metadata is copied before marking the mean free.
This is metadata of a supplementary chart, not an edit of the source
or campaign ledgers. No arc translation or extra coordinate pin is
performed. The source c localizer remains `Zc*c-1`, and the actual
stage0/1 circuit files retain both it and `Z63*leader63-1`.

## Source maps and preprocessing

The adapter calls the full source builder with jet0 free, normalized
coordinates, and the proved strong-front mode. Its stages0 and1 retain
611 and577 named coordinates respectively, including mu and all five
scalar target coefficients. Their input hashes match the saved map
receipts. Mu occurs43 times in each h expression, is absent from the
pivot-variable list, and every recorded pivot leader is a nonzero
rational. Their source residual lists happen to be empty after exact
graph elimination; no residual was deleted by the adapter.

The source floors, h2 major face and moment equations, and outer boxes
are unchanged. The strong-front proofs use precisely those data, the
fixed H0, and the characteristic identities; they do not assume a zero
minor mean. Stage0 consequently retains D<=32,C<=66, and stage1 uses
D<=33,C<=68. The same stage-positive proof applies through stage8.
No additional gauge is hidden in those radical consequences.

## Covariance of the existing beta normalization

Under simultaneous dilation with restored source monicity,
`P_alpha(x,y)=alpha^(-deg P)P(alpha x,alpha y)`, the minor arc coefficients
transform as

    jet0 -> alpha^-1 jet0,  u -> alpha^-2 u,
    v -> alpha^-3 v,        mu -> alpha^-4 mu,
    c -> alpha^-8 c.

Indeed the entire quadratic obeys

    alpha^-8*((alpha^4*pi-mu)^2-c)
      = (pi-alpha^-4*mu)^2-alpha^-8*c.

Thus its prescribed pi leader is preserved, the free mean stays free,
and c remains nonzero. Beta still transforms by alpha^-5, allowing the
single already-audited beta normalization. No value of mu, c, or the
characteristic leader is normalized in addition. The characteristic
leader retains its earlier transformation alpha^-153.

All claims above were checked in
`d108-meanfree-adapter-audit.py/.json`, which passes over exact Q and
binds the actual stage0/1 inputs. These are implementation and covariance
controls; they are not a completed characteristic-chart computation.
