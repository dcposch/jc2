# Preregistration: small-`a` unique-`AC` `d=2,3` support miner

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS EXACT SUPPORT/LOCAL-POLE CENSUS.  NO
EMPTINESS ENDPOINT.**

## Question

After the high-contact source ceiling removes `a>=10`, the strict unit-load
unique-`AC` residue has eighteen `(a,d)` baselines, `1<=a<=9` and
`d in {2,3}`, with the exact minimum `s=r-a`

```text
s_min(a,2)=1 for a<=2, else 0;
s_min(a,3)=1 for a<=3, else 0.
```

Mechanically expand all four binomial source summands through

```text
G_C2=10+2*a+2*d
```

and decide which primitive families can have local pole order at least two
at the `A0` root after the first `AC/L` root allocation.  This is a support
census for the next source client, not a source/Faber bridge or an emptiness
theorem.

## Preregistered invariant

For a primitive `P/L^q` containing `e_A` copies of `A`, let `g` be its first
absolute grade and `h=G_C2-g`.  At correction depth `h`, losing one allocated
`A0` root factor costs at least one sigma order.  Its worst possible local
pole order at the `A0` root is therefore

```text
q - max(e_A-h,0).
```

The expected census is:

- every baseline contains the target `C^2/L^2`, coefficient `3/8`, as a
  local double pole;
- exactly one baseline has another possible local double pole:

  ```text
  (a,d,s)=(1,3,1), i.e. (a,c,r)=(1,4,2),
  ```

  where `R*A^2/L^2`, coefficient `-3/8`, begins two grades before the target
  and can lose both `A0` factors;
- the other seventeen baselines have no second primitive with local pole
  order at least two through the target.

The compiler must independently enumerate atom multiplicities from grade
cost bounds.  It may not import a handwritten eleven-family list or impose
an arbitrary binomial-degree cutoff.

## Acceptance

1. Symbolically reconstruct the strict-cell inequalities and require exactly
   the eighteen baselines and the displayed `s_min` table.
2. For each baseline independently expand the unloaded, `k10`, `k6`, and
   `k2` binomial summands, combine cancellations over `Q`, and retain every
   polar primitive of first grade at most `G_C2`.
3. Derive all atom-count bounds from positive effective grade costs.  Repeat
   the census with one extra count in every direction as a cutoff sentinel.
4. Compute correction depth and worst local pole order for every retained
   primitive.  Require target `C^2` on all eighteen blocks, exactly seventeen
   safe blocks, and the unique `RA2` negative control above.
5. Record a canonical characteristic-independent JSON inventory.  Run exact
   rational arithmetic on Box03 and a separate `F_65521` coefficient control
   on r6d.  Exact Q is the support endpoint.
6. Fail closed off AWS, on any hash mismatch, duplicate output, timeout,
   nonzero rc, rejected diagnostic, missing/nonunique marker, or nonzero swap.

## Firewall

A PASS certifies only the primitive support and worst local-pole census.  It
does not prove the literal seven-row source bridge, truncated divisibility,
root allocation, cancellation impossibility, emptiness of any cell, the
high-contact corollary, a fan cover, D1, the square component, order two,
maximum twelve, or JC2.

