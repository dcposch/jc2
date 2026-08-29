# Hostile review assignment: affine-Faber `A`-face formal `J` arc

Work in `/Users/dc/code/math/jc2`.  Review exactly

```text
cases/max12_812_order2_affine_faber_a_ift_lift_20260826/RESULT.md
```

whose required SHA-256 is

```text
62e0f17d0679f21a00b1e96d36d68399ee93e22f698f8ed96ef01405c1053046
```

The charged evidence manifest is

```text
cases/max12_812_order2_affine_faber_a_ift_lift_20260826/EVIDENCE.sha256
```

with required SHA-256

```text
1afbeb633080bf6f3d4cf4ec41cd24bcf50821ff5dc843053f047f3f90d07b92
```

Write the unique report to

```text
xmodel/max12-812-order2-affine-faber-a-ift-hostile-review-grok-20260826.md
```

Do not edit any other file and do not touch `jc2-lean`.  This is a hostile
mathematical audit, not a trust pass.  Do not use producer status lines,
PASS tokens, the printed point, or the printed determinant as evidence.
You may inspect charged exact source, but independently rederive the
mathematics by hand and do not invoke Singular, Sage, SymPy, msolve, Lean,
or another CAS.

Audit at least:

1. Starting from the frozen ordinary Faber definition, reconstruct the
   specialized octic coefficients for
   `D=1,p=0,r=-1,k10=1,beta=15/8,gamma=15/16`,
   `c=t,n3=t^3 v,n2=0,n1=t^3 u,n0=t^2 e0`.  Check that this is the
   `5D+2s=0` face and that no Laurent/Faber convention was exchanged.
2. Prove that `R1,R3,R5,R7` are exactly divisible by `t^3`.  Recompute the
   three divided rows and `4R7/t^3` at
   `(t,u,v,e0)=(0,0,-1/20,0)`.  Attack the signs and factor `4` in
   `J=4R7`.
3. Independently compute the full Jacobian of the three divided zero rows in
   `(u,v,e0)` and its determinant.  Decide whether the characteristic-zero
   formal implicit-function theorem really produces unique series
   `u(t),v(t),e0(t)` and preserves a generically nonzero `J`.
4. Recompute the next even divided jet.  Check
   `u_2=13/800`, `v_2=0`, `e0_2=-21/640` and the zero next coefficient of
   `4R7/t^3`.
5. Audit evidence integrity: rehash every named file, require empty compiler
   stderr, exact-Q as producer, F65521 only as software control, and no
   diagnostics hidden behind exit code zero.
6. Attack scope.  `t` is an exceptional/contact uniformizer, not
   automatically the source `Lambda`.  The result must remain normalized
   ordinary-Faber only until a literal two-sided total-Rees chart map,
   moving-center/torsion/omission audit, and general contact/ramification
   treatment are proved.  Terminal `[6,2]`, both Taylor families, order two,
   and JC2 are out of scope.

Report exactly one overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.
State the smallest failing identity or missing hypothesis, the strongest
exact theorem that survives, and a precise normalized-only firewall.  End
with exactly one standalone verdict token.
