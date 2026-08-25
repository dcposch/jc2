# TD6 source-dilation contraction: exact negative control

Date: 2026-08-25  
Status: **HAND/SOURCE AUDIT / EXACT WEIGHT OBSTRUCTION / NO TD6 KILL**

## Verdict

The proposed dilation of the local source parameter `t` does not define a
contracting `G_m` action from the full normalized TD6 source to the empty V76
slice.  It is stopped by the boundary normalization before any elimination.

Write

```
p(t)=t^15,
q(t)=t + sum(q_e*t^e) + t^25.
```

Under `t -> b*t` and independent target scalings
`f -> alpha*f`, `g -> delta*g`, restoring `p_15=q_1=1` forces

```
alpha=b^-15, delta=b^-1.
```

The other normalized endpoint is then `q_25=b^24`.  Preserving it forces
`b^24=1`, leaving only `mu_24`.  If determinant-one target scaling is also
required, `alpha*delta=1` forces `b^16=1`, leaving at most `mu_8`.  There is
no one-dimensional stabilizer of the V76 boundary section.

Keeping only q1 monic gives formal weights `e-1` to the higher q jets, but
also sends the load-bearing q25 endpoint to zero.  The limit drops the
degree/pole type and is outside TD6/V76.  Keeping q25 monic gives q1 weight
`-24`, so it diverges.  The required target scalars have negative b-powers
and do not extend regularly to `b=0`.

## Landed-chart obstruction

Before normalization the x chart is

```
y=s^-1,
x=c1*s+c2*s^2+c3*s^3+j*t*s^4,
j != 0.
```

Raw t-dilation sends the transverse coefficient `j` toward zero, leaving
the principal open `D(j)` where the Jacobian compiler and V76 live.
Compensating with the determinant-one source scaling
`(x,y)->(a*x,a^-1*y)` and `s'=a*s` gives

```
x'=c1*s' + a^-1*c2*s'^2 + a^-2*c3*s'^3
   + a^-3*t*s'^4.
```

Thus fixing the t coefficient assigns opposite weights to the higher-q and
generic center data; reversing the action only reverses both sets.  Generic
orbits escape to center infinity rather than to a finite V76 point.

The frozen pole normalization `L^8*A^3=9`, with `L*A != 0`, supplies the
same guard: homogeneity requires `8*w_L+3*w_A=0`, so a nontrivial action has
a negative pole weight.  The V76 `U/H/B3` charts cover finite center space,
not `j=0`, `q25=0`, center infinity, or pole infinity.

## Logical scope

At most the dilation defines a Rees degeneration to an initial-form scheme
on a larger boundary.  Properness/flatness and same-landed-chart hypotheses
are absent, so emptiness of V76 says nothing about that special fibre.
Solutions may escape through the loci just listed.

This is a negative control on one shortcut, not an obstruction to TD6
solutions and not a theorem about SP-2 or JC2.

