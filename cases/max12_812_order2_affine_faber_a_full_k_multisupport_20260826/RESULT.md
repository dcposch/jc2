# Result: full affine-Faber `K` multigraded support

Date: 2026-08-26

Status: **DUAL-AWS SUPPORT ENUMERATION PASS; NAVIGATION ONLY.**

The frozen compiler reconstructed all seven complete ordinary-Faber tails
in the exact moving-discriminant coordinates and formed the unweighted
polynomial

```text
K=E*H3+H5.
```

Both exact Q and the F65521 software control emitted exactly **371** nonzero
monomials.  Their ordered exponent-vector sequences agree byte-for-byte;
the common sequence has SHA-256

```text
a21e5dbbbfe7e937aa0eb2cb873047852b902b6a959f8df8f19a2b18f88dab6a.
```

All preregistered type controls passed:

```text
dK/dmu6 = 0,
dK/dJ   = 0,
dK/dmu4 = B = 4*a,
dK/dmu2 = -B*E/4 + 5*B^3/16,
[lambda^3]K on the central kernel/complement/load-zero slice
          = -E*M^3/16.
```

Both validators printed `PASS_A_FULL_K_MULTISUPPORT`.  Exact Q used 11 MiB
maximum resident memory, the finite-field control used 10.5 MiB, and neither
swapped.

AWS custody:

```text
Box03 exact Q:
  max12_812_order2_affine_faber_a_full_k_multisupport_20260826T162000Z_q
r6d F65521:
  max12_812_order2_affine_faber_a_full_k_multisupport_20260826T162000Z_p65521
```

This result is the complete raw support table for the named normalized
polynomial.  It is not a predecessor-ideal reduction, coefficient
stratification, Newton fan, source/Rees overlap, valuation-coverage theorem,
order-two result, maximum-twelve result, or JC2 result.  Equality faces must
still be reduced against the complete predecessor rows, and every cone must
retain the literal source/load/target map.
