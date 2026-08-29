# Registration: D1 high-contact translated `C^2` block and target shadow

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS EXACT-SOURCE FALSIFICATION CLIENT.**

## Question

For the D1 contacts

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,  ord_sigma(R)>=a,
```

the first unloaded `C^2/L^2` block occurs at absolute grade

```text
G(a)=12+2*a.
```

At `a=9`, rows 3 and 4 supplied the decisive pair

```text
c1*c0,  2*c0^2-p*c1^2.
```

Test whether that pair remains an actual source constraint after all earlier
load and target jets are retained for `a>=10`.  This is a navigation client,
not an emptiness theorem.

## Hand invariant and preregistered expectation

The tagged literal-Faber contribution of `C^2/L^2` should translate
homogeneously with `a`; after extraction at `G(a)` its seven rows should be

```text
0,
(3/8)c1^2,
(3/4)c1*c0,
(3/16)(2*c0^2-p*c1^2),
-(3/16)p*c1*c0,
0,
-(3/128)p^2*c1*c0.
```

But the complete target source contains independent series

```text
-sigma^28*mu2(sigma)  in row 2,
-sigma^32*mu4(sigma)  in row 4.
```

For every integer `a>=10`, the grade-`G(a)` row uses the fresh jets

```text
mu2_[2*a-16],  mu4_[2*a-20],
```

which occur in no earlier grade.  The preregistered expectation is therefore:

1. the *tagged* nonlinear block is translation invariant;
2. the fresh `mu2` jet shadows `(3/8)c1^2` and the fresh `mu4` jet shadows
   `(3/16)(2*c0^2-p*c1^2)` by exact affine-linear equations;
3. only the mixed `c1*c0` component is target-unshadowed at this grade;
4. consequently the two-generator `a=9` obstruction does **not** translate
   unchanged to `a>=10`.

The symbolic reason for the unbounded range is exact: increasing `a` by `s`
multiplies the tagged `C^2` source by `sigma^(2*s)`, while replacing the fresh
target indices by indices larger by `2*s`.  Threshold representatives
`a=10,11,12,13,14,15` are nevertheless replayed from all seven frozen source
rows to catch the known `mu4`, `mu6`, `J`, `k2*R`, `k2*A`, and `k2*C` timing
walls.

## Acceptance tests

For each `a=10,...,15`, on exact Q and independently on `F_65521`:

1. rebuild all seven literal source rows with independent jets for moving
   `p`, `A,C,R`, `k10,k6,k2`, `mu2,mu4,mu6`, and the sparse `J/4` target;
2. recursively extract every grade from 28 through `G(a)` and verify exact
   quotient identities;
3. independently isolate the homogeneous `C^2` contribution and verify all
   seven displayed rows coefficient by coefficient;
4. verify the fresh `mu2` and `mu4` variables occur with coefficient `-1`
   only in rows 2 and 4 at `G(a)`, occur nowhere earlier, and give exact
   polynomial sections solving those two equations;
5. verify the grade-`G(a)` row 3 has no target dependence;
6. include an exact-contact witness for the tagged targeted block with
   `c1=0,c0=1`, proving that target shadowing is not merely a radical claim;
7. require rc 0, no Singular diagnostics, and zero swap.

Run exact Q on Box03 and `F_65521` on r6d.  The client must fail closed off
AWS and under any ancestry/hash mismatch.

## Firewall

A PASS disproves only the proposed unchanged two-equation induction.  It does
not prove that a high-contact source solution exists: other same-grade loads,
the `J` wall, later pole blocks, terminal rows, and Taylor pullbacks may still
eliminate each threshold band.  It gives no result for `p=0`, `k0=0`, other
D1 cells, the whole square component, order two, `(8,12)`, maximum twelve, or
JC2.

