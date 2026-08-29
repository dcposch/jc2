# Cutoff-four square tail: independent two-branch exclusion

Date: 2026-08-28  
Author: Sol Ultra, independent characteristic-mode lane  
Status: `PROVISIONAL EXACT PASS; HOSTILE REVIEW REQUIRED`

## Verdict

Direct recompilation from the pinned branch-P determinant source excludes
all characteristic-zero field points of the fixed cutoff-four upper-endpoint
square-tail specialization.  The calculation uses no CAS.  It extends the
higher-cutoff square/divisibility cascade from `D8` through `D15`, then ends
with an exact `D18` branch split and a `D20` obstruction.

The literal census is

```text
286 retained raw variables;
138 prefix equations D0,...,D7;
rank 76, nullity 210;
375 retained equations D8,...,D22.
```

The endpoint is exactly

```text
1+p32*p171-p86*p91=0.
```

## Uniform cascade and first correction

With `C=X^4-1`, `H=C^2`, exact compatibility witnesses give

```text
F4=H*V,
F5=V/2+H*R,
F6=R/2+H*U,
F7=U/2+H*Q.
```

Each equality is a characteristic-zero field-radical parameterization.  In
particular, the previously suspected `D11` gap disappears when the `D8-D10`
substitutions are applied in their licensed order: `D11` contains every
coefficient of `W^2 mod C`.

Let

```text
x=V0, v=R0, r=U0, b=p171,
s=p196-3*x/4, h=p152-s*x.
```

The post-`D15` scalar core is

```text
E13=h*v-3*b*v/4+3*b*r/2-3*r^2/8,
E14=h*r+3*b^2/4-3*b*r/2+3*r^2/16-3*x*v^2/8,
E15=h*b-3*b^2/4-v^3/8-3*x*v^2/16-3*x*v*r/4.
```

Thus the core is the cutoff-five core shifted by one tail mode, with the
first genuine correction carried by `x`.  The endpoint carrier reconstructs
as

```text
p86=b*s+3*v*r/4+3*v^2/16.
```

After the exact additive-gauge slice `p161=F8[X^0]=0`, neither `D16` nor
`D17` adds a scalar-core equation.  `D18` adds exactly

```text
v*(b*v+r^2)=0,
```

which is the cutoff-five `K17` invariant transported by
`(V0,R0,b) -> (v,r,b)` and shifted one determinant row.

## Closed branch

For `v=0`, the `x` corrections vanish.  The core identity

```text
3*b^3=2*b*E13+4*b*E14-4*r*E15 modulo v
```

and the monic carrier relation lift through the endpoint to a division-free
six-generator unit.  Exact independent decoding of the emitted JSON gives
the literal polynomial `1`.

## Open branch

For `v!=0`, put `tau=r/v`.  Exact desk elimination gives

```text
x=(tau^2/2)*(12*tau^2+6*tau+1),
v=-(3/4)*tau^2*P3,
P3=1+10*tau+40*tau^2+64*tau^3.
```

The serialized `D20` witness, with 10 nonzero compatibility cofactors and
14 combined literal source rows after the licensed substitutions, gives

```text
tau^9*P3^3=0.
```

Since `v!=0` forces `tau*P3!=0`, this is impossible.  Equivalently,

```text
P3=(4*tau+1)*(16*tau^2+6*tau+1),
```

and both displayed root loci lie on the excluded `v=0` boundary.  No
endpoint, `D21`, or `D22` row is used in this open branch.

## Firewalls

- The result is for characteristic-zero field points after named radical
  steps, not for the upstream nonreduced scheme.
- `tau` is introduced only on `v!=0`; the boundary-root mutation confirms
  this hypothesis is indispensable.
- The `p161` slice is licensed by an exact additive determinant symmetry and
  does not normalize `p32,p171,p86`, or `p91`.
- The closed branch uses the endpoint; the open branch does not.
- This is a cutoff-four specialization result, not a full branch-P or JC2
  theorem.

The replay and immutable certificates live in

```text
cases/ggv_8_28_upper_endpoint_tail4_desk_20260828/
```
