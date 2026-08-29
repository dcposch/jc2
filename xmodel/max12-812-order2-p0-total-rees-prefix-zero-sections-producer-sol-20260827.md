# Producer — three exact horizontal zero sections of the exported total prefix

Date: 2026-08-27

Status: **EXACT SOURCE-PREFIX RESULT, AWAITING DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen object and replay

The preregistered replay consumes exactly the 21 exact-Q V9 literal
actual-total rows

```text
Tg10_1,...,Tg10_7, Tg11_1,...,Tg11_7, Tg12_1,...,Tg12_7
```

and the exact-Q V17 literal actual-total row `Tg14_5`.  It parses their
frozen polynomial bytes through a restricted Python AST evaluator, evaluates
over `Q[rho]` with exact `Fraction` coefficients, and uses no external CAS.

```text
preregistration SHA-256 1c4661ac689443184478333755ace8d1ad28b06449dc65ba66d612df3325a815
replay SHA-256          9eb848f034bb7513e50790e9eb896866454cd439a11ac67fba541bb14c657bc0
```

The replay prints the SHA-256 of every one of the 22 inputs.  In particular,
the independently rederived rows used by the recent cubic certificates are

```text
Tg10_2 50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6
Tg10_4 6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d
```

and the V17 row is

```text
Tg14_5 91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7
```

`python3 -m py_compile` passes.  The replay's exact terminal output includes

```text
CS0_ZERO_ROWS=22
A00_ZERO_ROWS=22
A10_ZERO_ROWS=22
WITNESS_TG12_2=0
WITNESS_TG14_5=-21/320
NEGATIVE_CONTROL_TG12_2=(-5/128)*rho^0
PREFIX_ZERO_SECTIONS=PASS
```

The witness control is the independently promoted point
`cs=e1=1,k=12/5,rho=0`; the negative control is
`cs=k=1,e1=rho=0`.  Thus the evaluator detects both the reviewed
`-21/320` row and a deliberate nonzero prefix residual.

## Exact zero sections

All unmentioned source variables are zero.  In each assignment `rho` remains
an indeterminate, not a sampled value:

```text
CS0: cs=1, k=0;
A00: a0=1, rs=cs=c0=c1=0;
A10: a1=1, rs=cs=c0=c1=0.
```

Every one of the 22 frozen source rows evaluates to the zero polynomial in
`Q[rho]` on every assignment.

For `CS0`, the standard `T-cs` chart relations are compatible with

```text
qrs=qc0=qc1=0,  u=1,
rs=cs*qrs, c0=cs*qc0, c1=cs*qc1, 1-u*cs=0.
```

Thus `CS0` is an exact horizontal section of the currently exported
unlocalized `T-cs,k=0` prefix.  It proves that no combination of these 22
rows and the stated chart relations can make that special fibre empty or
make `rho` nilpotent.

For `A00` and `A10`, after base change to `A/J1` the standard `a0` chart
relation `a1=a0*qa1` is compatible with `(a0,qa1)=(1,0)`, while the ordered
`a1` chart is compatible with `(a0,a1)=(0,1)`.  Hence the exported source
prefix alone cannot remove either proposed second-stage direction.  This is
not a claim that every still-uncompiled stage-two equation or unexported
source row vanishes.

## Consequences

1. **Do not launch a `k=0` emptiness or rho-torsion computation using only
   the V9 grade-10--12 rows and V17 row 5 at grade 14.**  It has an exact
   horizontal point for every `rho`.
2. **Do not expect the same prefix to delete either `J2` chart.**  Both pure
   exceptional directions survive it horizontally.
3. The cheapest next proof-side action is a source/coverage audit of the
   common localizer: older custody calls the family post-`M=0`,
   unit-`k10`, with `k=k10`.  If that is the registered scope, `k=0` is a
   sibling load-timing family and must be routed rather than killed inside
   this chart.  If it is not, a genuinely new source row or selection
   equation is required before another emptiness attempt.
4. The second-stage successor must first export the source rows that can see
   pure `a0/a1`, or prove a routing/receiver theorem.  Merely changing the
   Rees chart cannot make the three horizontal source-prefix sections
   disappear.

## Firewall

Only 22 frozen rows are tested: all rows through grade 12 and row 5 at grade
14.  The result says nothing about the other grade-13/14 rows, higher source
grades, the full source ideal, source-family coverage, a formal arc, a
Keller pair, Gate T, all order two, maximum twelve, or JC2.  It neither
weakens the promoted `T-rs`, `T-c0`, ordered `T-c1`, nor localized `T-cs`
theorems, all of which retain their stated localizers and scopes.
