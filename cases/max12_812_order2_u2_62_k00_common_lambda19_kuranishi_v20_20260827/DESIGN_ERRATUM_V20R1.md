# V20R1 design erratum: use the contracted universal cokernel

Date: 2026-08-27

Status: **TYPE CORRECTION FROZEN BEFORE IMPLEMENTATION OR ALGEBRA.**

This erratum changes no frozen row, source jet, weight, local relation, or
V17/V18 theorem.  It corrects the variance of the universal first-order
object in Section 4 of `PREREGISTRATION.md`.

## 1. Why the displayed vector quotient is not the discriminator

Write

```text
M = (R_h)^7 / (I*(R_h)^7 + image(Gamma)_h).
```

For a load coordinate `X`, coordinate projection sends `I*(R_h)^7` into
`I` and sends `image(Gamma)` onto the generators of `E_X`.  It therefore
induces a surjection

```text
pi_X : M -> (R_h)/(I+E_X)_h.
```

Consequently every V18 axis covector pulls back along `pi_X`; setting its
other six components to zero is already an extension.  Any finite sum of
the three pullbacks is also an extension.  Thus an `EXTENDS` versus
`DOES_NOT_EXTEND` computation for the vector quotient is tautological and
cannot be the mixed reachability discriminator.  The sentence in Section 4
claiming that the three axis covectors need not extend is withdrawn.

This does not make the V18 covectors composable with the honest jet source.
The missing operation is contraction by the simultaneous parameter vector,
and that contraction does not descend from `M` to a fixed scalar quotient.

## 2. Correct universal object

Introduce independent parameters

```text
p=(p10,p6,p2,p_mu2,p_mu4,p_mu6,p_J)
```

over

```text
B=(R_h)[p10,p6,p2,p_mu2,p_mu4,p_mu6,p_J].
```

For `s in S6`, define

```text
Gamma_p(s) = <p,Gamma(s)>
            = p10*sum_i s_i*a_i^k10
              +p6*sum_i s_i*a_i^k6
              +p2*sum_i s_i*a_i^k2
              -p_mu2*s2-p_mu4*s4-p_mu6*s6.
```

The representation-invariant universal scalar target and cokernel are

```text
D_p = <p,K(w)>
    = p10*D_k10+p6*D_k6+p2*D_k2
      +p_mu2*u2+p_mu4*u4+p_mu6*u6-p_J*h/4,

Q_p = B / ( I*B + (Gamma_p(s) : s in S6) ).             (2.1)
```

Changing the chosen unloaded relation by a six-row syzygy changes `D_p` by
one of the displayed generators, so `[D_p] in Q_p` is representation
independent.  Polynomial generators are locally complete after clearing a
unit denominator, exactly as in V16R1/V17.

The honest mixed specialization is

```text
p10   = Lambda^2*k10,
p6    = Lambda^6*k6,
p2    = Lambda^10*k2,
p_mu2 = Lambda^14*mu2,
p_mu4 = Lambda^16*mu4,
p_mu6 = Lambda^18*mu6,
p_J   = Lambda^19*Jdet.
```

Under this substitution, `D_p` is exactly the residual `Rmix` in (3.1).
The V20 compiler must therefore form the contracted generators
`Gamma_p(s)` before truncating and stratifying in `Lambda`; it must not test
extension of axis covectors in the uncontracted vector quotient.

## 3. Implementation consequence and controls

The literal seven-row 140-equation presentation remains ground truth.  The
optimized presentation is now:

```text
Phi1=...=Phi6=0,    D_p=0 modulo (I, Gamma_p(S6)),
```

after the honest specialization above, with lower compatible jets retained.
At every prefix the compiler must serialize the parameter-dependent
contracted columns, not seven independent coordinate blocks.

Mandatory controls are:

1. replay `h*r7=sum u_i*r_i` and all 66 six-row syzygies;
2. replay `D_p` and `Gamma_p(s)` before and after the honest specialization;
3. replay the 87 seven-row cross relations after contraction;
4. mutate one weight or one target sign and require failure; and
5. compare every optimized prefix bidirectionally with the literal seven-row
   coefficient equations.

V18 duals remain navigation controls on the three coordinate
specializations of (2.1).  Their pullbacks to the vector module are automatic
and carry no mixed-source verdict.  A mixed obstruction or compatible jet
still requires a complete exact constructible-stratum cover through
`Lambda^19`.

## 4. Scope

This is a type correction only.  It neither proves nor disproves mixed jet
reachability, excludes an arc, decides K00 closure incidence, nor bears a
direct order-two, maximum-twelve, or JC2 conclusion.
