# Coordinator integration: unit-`S` relative orders four and five

Date: 2026-08-28 UTC.  Status: **PROMOTED WITH REVIEW REPAIRS**.

## Frozen evidence

- order-four producer: `874bcd98b21c19546db67e6dc4599aebd800259687c45ecc0780ab282119e92d`;
- order-four checker: `a4e6f18b718fb99495aaf048a4b104109ef20b320b89e2016c50dfb63a608e40`;
- order-five producer: `aa88f1904ac14f05cbac193dac12ef054ba3928306811a253abb840656fc7138`;
- order-five checker: `f683bd2a33e93ad2ecd3ca38155388b65d1f536b8ae33fad3c1eff4412112bc4`;
- different-model Opus5 hostile review:
  `5df1d312df6d44ca88abd3b67f296daebd5afdeda5b7b4b3f6c5230741407226`.

The coordinator replayed both stored checkers after the review; both returned
their exact PASS markers.  The Opus review independently rebuilt the
calculation with full jets, all modes through `m=14`, and the previously
implicit `f5` and `c10` terms.

## Integrated theorem

On the reviewed active-`c2`, exact-`D=0`, lambda-nonzero unit-`S` branch, at
each simple root of squarefree `A`, the two D12 lifts give

```text
epsilon^-4 F
 = L^4 + epsilon*L^3*J1 + epsilon^2*L*H2
       + epsilon^3*C3 + epsilon^4*D4 + epsilon^5*E5 + ... .
```

The complete relative-order-four characteristic is regular.  At relative
order five the sole possible polar part is

```text
L^-1*H2*(3*C3/4 + 5*c2*tau^2*H2/32 - 3*J1*H2/16).
```

Its face residue is a nonzero local unit times

```text
J*(20*c2*J + 3*N),
```

which is precisely the numerator already forced divisible by `A` in the
reviewed residual D12 row.  Therefore relative order five is regular and
adds no cut.  The newborn `c10` term is `c10*tau^10*L`, and the omitted fifth
coefficient contributes `(3/2)*L^2*f5`; both are manifestly regular.  If
`S(alpha)=0`, `L` is a nonzero constant and there is no face pole, so the
conclusion is not weakened there.

## Mandatory repair riders

The producer reports remain frozen; the following review findings supersede
their overstatements.

1. The order-four checker's `raw_f2` is a surrogate that omits genuine low
   tau terms, and its jets are truncated.  Its advertised broken-first-lift
   mutation is decorative.  Opus's independent full-jet reconstruction,
   rather than that checker alone, supplies the missing coverage.
2. The order-five checker omits explicit `c10` and `f5` coverage, and its
   final product assertion is tautological as coded.  Opus independently
   forms the product from the computed `H2` and bracket and checks the exact
   `8192` load.
3. The order-four sentence that regularity forces `L|K,L|B` needs active
   `c2`; this is a standing branch hypothesis, not an unconditional fact.
4. The result inherits the q1-free D9 reduced prefix, D8/D10 lifts,
   exact-`D=0`, and the reviewed-with-repair R11/R12/R12r chain.  It is local
   face regularity, not raw-window compatibility or an endpoint theorem.

## Campaign decision

Stop blind unit-`S` face-pole expansion at order five.  Orders four and five
show that later face residues can merely restate prior determinant rows; an
order-six computation has low discriminatory value without a structural
invariance claim.  The licensed successors are:

1. prove or refute a finite-mode recurrence / row-ideal invariance theorem;
2. impose the complete raw receiver windows and quadratic endpoint on this
   branch; or
3. return to the rank/Fitting decomposition of the lambda-zero receiver.

No raw pair, endpoint exclusion, Keller theorem, counterexample, or JC2
conclusion follows.
