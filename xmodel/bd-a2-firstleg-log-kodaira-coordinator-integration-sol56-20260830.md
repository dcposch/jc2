# Coordinator integration: exact log-Kodaira obstruction for an `A^2` first leg

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **BINDING INTEGRATION / DIFFERENT-MODEL-CONFIRMED EXACT THEOREM**

## 0. Evidence and disposition

This integration binds

```text
cc836852f92ee0a30dab9bfef3cb37b6f818ea2bb76d125ad95c8eecab44248f
  xmodel/bd-a2-firstleg-log-kodaira-obstruction-producer-sol56-20260830.md
662dd4f416c723cf18d4084831357be915e7e3c5bc6640ed63387915a0434194
  xmodel/bd-a2-firstleg-log-kodaira-obstruction-hostile-review-opus5-20260830.md
```

The Opus verdict is `CONFIRM_WITH_CORRECTIONS`.  It reconstructed the ruled
completion, local collision calculation, every exceptional valuation, and
logarithmic monotonicity, and supplied a second discrepancy computation.  It
also sharpened the lower bound to the exact logarithmic plurigenus.  The
corrections below fill one local-normal-form step, display the interior-fibre
order, identify the normality used for the section, and remove a cosmetic
sign claim.  None changes the theorem.

## 1. Exact theorem

Let `qbar:P->P^1` be a `P^1`-bundle with section `D_infinity`, and put
`Y=P minus D_infinity`.  Let `R subset Y` be closed and suppose

```text
q|R:R -> P^1 minus S
```

is an isomorphism for a finite set `S`.  Let `D_0` be the closure of `R` in
`P`; it is a section, and its support meets `D_infinity` precisely over `S`.
Put

```text
U=Y minus R=P minus (D_0 union D_infinity).
```

Then, for every integer `n>=1`,

```text
bar-P_n(U) = n*(#S-2)+1       if #S>=2,
             0                if #S<=1.
```

Consequently

```text
bar-kappa(U) = -infinity      if #S<=1,
               0              if #S=2,
               1              if #S>=3.
```

The answer is independent of all contact multiplicities between the two
sections.  In particular `bar-kappa(U)>=0` exactly when `#S>=2`, and then no
dominant morphism `A^2_C->U` exists.

## 2. Binding proof mechanism and repairs

The closure `D_0->P^1` is proper, quasi-finite, and birational.  Normality of
the target makes the finite birational morphism an isomorphism; this, rather
than smoothness by itself, is the operative section argument.

Because `D_0` and `D_infinity` have the same fibre degree, choose a rational
function `phi` with

```text
div(phi)=D_infinity-D_0+qbar^*E.
```

For `#S>=2`, choose nonzero
`eta in H^0(P^1,Omega^1(log S))` and set

```text
omega=qbar^*eta wedge dlog(phi).
```

Near a collision write `D_infinity:{w=0}`, `D_0:{w=a(t)}` with
`ord_t(a)=m_s>=1`.  After multiplying by a base rational function one may
take `phi=w/(w-a(t))`: the quotient of the two functions has zero divisor on
the local `P^1`-bundle, hence restricts to a regular invertible function on
each complete fibre and therefore comes from the base.  If
`eta=h(t)dt/t`, then

```text
omega=-h(t)*(a(t)/t) * dt wedge dw / (w*(w-a(t))).
```

Its order along the interior fibre is explicitly

```text
ord_(F_s)(omega)=m_s-1+ord_s(h)>=0.
```

After the `k`-th collision blowup its exceptional exponent is exactly
`m_s-k-1`; the last exceptional carries a simple logarithmic pole and the
earlier exceptionals carry no worse pole.  Thus `omega` is a nonzero section
of the resolved log-canonical bundle.

The exact dimension follows from the discrepancy identity

```text
K_(P_tilde)+D_tilde
 = rho^*(K_P+D_0+D_infinity)
   - sum_(s in S) sum_(i=1..m_s) (i-1)E_(s,i).
```

Base sections of degree `n*(sum_s m_s-2)` must vanish to order
`n*(m_s-1)` at each `s`; the residual degree is `n*(#S-2)`, giving the
displayed formula.  This also proves sharpness: one collision of any positive
contact order still has log Kodaira dimension `-infinity`.

Finally, logarithmic pluricanonical forms pull back injectively along a
dominant generically finite morphism of smooth complex quasi-projective
varieties, even when the morphism is nonproper.  Hence

```text
bar-kappa(A^2)=-infinity >= bar-kappa(U)
```

would contradict `#S>=2`.  Since a dominant morphism between surfaces is
generically finite, no stronger finiteness or étaleness hypothesis is needed.

## 3. Scope and application gate

This theorem is unconditional at the displayed two-section type.  It does
not use a cubic cover, a block quotient, étaleness of a first leg, class
groups, units, Euler characteristic, or strong Zariski Main.

Its affine-linear cubic application remains conditional here on the separate
`AL3-REDUCE` review.  That producer identifies a residual affine-line torsor
whose deleted ramification graph has collision set `S=Crit(rho)` with
`#S>=2`.  If that reduction is promoted, the theorem above immediately
excludes the residual first leg and hence closes the affine-linear Miranda
cubic subfamily.  This integration alone proves nothing about nonlinear
cubic coefficients, primitive monodromy, existence of a block, a
counterexample, or JC2.

The natural successor is a multisection or higher-coefficient-degree version
of the logarithmic calculation, with resolution discrepancies retained.  A
cover-side finite algebra is not enough: the contradiction is specifically
the impossibility of a dominant `A^2` first leg into the log-nonnegative
complement.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5251`.
- Body SHA-256:
  `10fb58eb6845d21a3620e20a30bbd128cb5671f8119e258b7ea60aca1e829b2f`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
