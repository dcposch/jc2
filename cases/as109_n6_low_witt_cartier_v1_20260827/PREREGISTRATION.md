# AS109 residual `n=6` low-Witt Cartier gate V1

Date frozen: 2026-08-27 11:20Z  
Producer: Sol  
Compute class: desk-scale exact/std-lib replay only; no Singular and no AWS
needed

## Charged question

For an exact integral lift

```text
P=x-x^109+109 A,       Q=y+109 B,       det J(P,Q)=1,
```

couple the first-Witt divergence equation to the already-promoted residual
`deg_y(Q)=6` common core

```text
p_m=alpha h^(m/d),     q_6=beta h^(6/d),
d=gcd(m,6) in {3,6}.
```

Test whether the coefficient of `y^5`, which is outside the stopped top-two
band cascade, gives a genuine branch-local Cartier condition on `q_6` when
`v_109(beta)=1`.

## Preregistered statements

The producer may report `PASS-LOW-WITT-CARTIER` only if it proves and the
replay checks the following exact statements.

1. The packed determinant identity over `Z[x,y]` is

   ```text
   det J(P,Q)-1
    =109*(A_x+B_y-x^108)
     +109^2*((A_x-x^108)B_y-A_y B_x).
   ```

2. Modulo 109, for `A=sum a_i(x)y^i`, `B=sum b_j(x)y^j`,

   ```text
   a_i' + (i+1)b_(i+1) = delta_(i,0)x^108.
   ```

   Hence `a_5'+6b_6=0`.

3. If `v_109(beta)=1`, so that

   ```text
   b_6 mod 109=(beta/109 mod 109)*(bar h)^b,
   b=6/d in {1,2},
   ```

   then `(bar h)^b` lies in `im(d/dx:F_109[x]->F_109[x])`.  Equivalently,
   every coefficient at exponent `109*k-1` vanishes.

4. If `Hbar=deg(bar h)` and the leading coefficient survives, this implies

   ```text
   b*Hbar != 108 mod 109.
   ```

   Thus the `d=6` branch excludes `Hbar=108 mod 109`, and the `d=3`
   branch excludes `Hbar=54 mod 109`.

5. For `i>=6`, the same first-Witt equation gives `a_i'=0`.  On the
   additional branch `v_109(alpha)=1` and `gcd(m/d,109)=1`, unique
   factorization implies `bar h in F_109[x^109]` up to a scalar.  This is a
   positive compatibility control: then `(bar h)^b` is automatically in the
   derivative image.

## Required controls

- exact packed determinant expansion on deterministic sparse integer inputs;
- `h=x^108`, `b=1` must hit a Cartier obstruction;
- `h=x^54`, `b=2` must hit the same obstruction;
- `h=1+x^109`, for `b=1,2`, must be in the derivative image and admit an
  explicit `a_5` satisfying the first-Witt row;
- the common-core Wronskian must vanish exactly in representative `d=3` and
  `d=6` profiles.

## Scope and stop

This gate concerns only the valuation-one content branch of `q_6`, and the
extra top-`P` statement only the separately stated valuation/gcd branch.  It
does not assert that either branch is forced, does not inspect the first
nonzero digit when `v_109(beta)>1`, does not run W2/W3, does not enumerate a
degree rectangle, and does not prove existence or nonexistence of an AS109
polynomial lift.

If the low row is a history duplicate *as coupled to the residual common
core*, or if any control fails, report `FAIL_`/`DUPLICATE` and stop without a
canonical promotion.

