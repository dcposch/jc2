# TD6 q2-beta rational-line dependency/custody erratum

## Verdict

**NONMUTATING DEPENDENCY AND SCOPE REPAIR.**  The frozen rational-line
producer bytes are unchanged.  Hostile review
`xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-review-grok-20260825.md`,
SHA-256
`2e76f499895c34f0532f09b44e865ffdfb9acad6ebf896ce1d0fc55477830555`,
returned `CONFIRMED_WITH_REPAIRS`.

The freeze-time claim that the three lines' `U=0` endpoint was supplied by
the old V33/V69 whole-`U=0` theorem is withdrawn.  V33/V69 only proved
`U=0,D(C)` and therefore missed the common origin of these lines.  The sole
endpoint authority used here is now the independently rebuilt and
hostile-reviewed V70 origin theorem at `C=V=U=0`.

## Corrected dependency graph

Inside the fixed source-typed normalized A3 q2-beta section, with

```text
q_beta = t + beta t^2 + t^25,
q_beta' = 1 + 2 beta t + 25 t^24,
```

the frozen D(U) calculations and corrected endpoints are:

1. `V=0, C=-U^2`: V46 gives a direct first-J original-row unit
   incompatibility on `D(U)`, independent of N13.  V70 gives the origin
   endpoint.  Their union source-closes this whole affine line for every
   beta.
2. `V=0, C=3U^2`: V45 gives an exact genuine-P12/original-first-row
   identity on `D(U)` and algebraic glue to an abstract
   `N13=(k/25)beta`, with residual `-k/50`.  V70 gives the origin endpoint.
   The old staged-N13 localization erratum remains in force: this is not a
   composed staged-N13 original-source lift on `D(U)`.
3. `V=0, C=-5U^2`: the same V45 algebraic status holds on `D(U)`, and V70
   gives the origin endpoint.  It likewise remains a staged-N13
   original-source-DAG debt.

Thus V70 repairs endpoint custody only.  It does not retroactively turn the
two V45 abstract-N13 identities into original-source certificates.

## Exact B3 consequence

On `V=0`, the raw B3 equation has the two non-origin branches

```text
C=-U^2  and  C=-5U^2
```

on `D(U)`.  The reviewed V68 route calculation sends the `t=0` chart debt
to exactly these lines, while its `w=0` and `t=2` finite endpoints route to
the origin as recorded there.  Consequently:

- `C=-U^2,D(U)` is source-closed by V46, and its endpoint is source-closed
  by V70;
- `C=-5U^2,D(U)` is the precise remaining staged-N13 source-DAG debt for
  this B3 boundary route;
- `C=3U^2,D(U)` is not a B3 branch (`B3=128 U^6` there) and is retained only
  as a separately scoped rational-line algebraic result.

No whole-B3 original-source theorem may consume the `C=-5U^2` line until a
V65/V67-style replay carries its actual N13 current row through previous and
first original rows, retains direct `q_beta'`, records every denominator,
and passes an omission/wrong-row control plus hostile review.

## Superseded wording and strict firewall

This erratum supersedes only the rational-lines report/README dependency on
V33/V69 as a whole-`U=0`, denominator-one endpoint theorem.  It replaces
that endpoint pin with reviewed V70.  It does not mutate or withdraw the
three D(U) calculations, and it does not relax the frozen N13-localization
erratum on `C=3U^2` or `C=-5U^2`.

No whole `H=0`, whole `B3=0`, whole A3, other TD6-modulus, TD6, SP-2,
landing, counterexample, or JC2 conclusion follows.

