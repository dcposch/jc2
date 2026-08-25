# AS F-only `D=7`: next-top-carry divided-Frobenius erratum

**Status: PRODUCER EXACT SOURCE CORRECTION; AWS REPLAY PASS; HOSTILE REVIEW
PENDING.  THE OLD DEGREE-11 CENSUS AND DEGREE-10 RUNNER ARE QUARANTINED.**

## Headline

The next top-carry filtration previously treated degrees 12 and 11 as the
pure quadratic current-digit bracket `N={C,D}` and asserted that the
quotient residual had degree at most nine.  That assertion is false.  The
degree-six Frobenius first digit has derivatives divisible by three, so it
vanishes in one reduction but reappears after the following division.

The degree-12 equation is unchanged and its exact survivor count remains
valid.  The full degree-11 equation is

```text
Q11 = {C7,D6}+{C6,D7}
      + ({UF,D7}+{C7,VF})/3                        mod 3,            (1)
```

not the first line alone.  At degree ten one must also include

```text
Q10 = {C7,D5}+{C6,D6}+{C5,D7}
      + ({UF,D6}+{C6,VF})/3
      + {UF,VF}/9                                  mod 3.            (2)
```

Thus the old 602,343 degree-11 count is a wrong-source diagnostic, not a
finite-lift census, and the just-launched degree-ten successor was stopped.

## 1. Full integer determinant filtration

Write over the integers

```text
P=x-x^3+3U+9C+27W,
Q=y+3V+9D+27Z,
A=U_x-x^2.
```

Direct expansion, before any reduction, gives

```text
det J(P,Q)-1
 = 3 L
 + 9 (K+C_x+D_y)
 + 27 (M+W_x+Z_y)
 + 81 (N+T)
 + 243 S
 + 729 {W,Z},                                      (3)
```

where

```text
L=A+V_y,
K=A V_y-U_y V_x,
M=A D_y+C_x V_y-U_y D_x-C_y V_x,
N={C,D},
T=A Z_y+W_x V_y-U_y Z_x-W_y V_x,
S=C_x Z_y+W_x D_y-C_y Z_x-W_y D_x.                (4)
```

On the accepted predecessor, put

```text
E=L/3+K+C_x+D_y=3E1,
F=E1+M+W_x+Z_y=3F1.                               (5)
```

Then the next residual modulo three is exactly

```text
F1+N+T.                                            (6)
```

Split `U=U0+UF,V=V0+VF`, with `U0,V0` of degree at most four and
`UF,VF` the homogeneous degree-six Frobenius forms.  The `U0,V0` part of
`M` has degree at most nine, but the single-Frobenius part

```text
MF={UF,D}+{C,VF}                                   (7)
```

has degree eleven.  Its coefficients are divisible by three and therefore
vanish in `F mod 3`; precisely because (5) then divides by three, `MF/3`
appears in `F1`.  Its degree-11 and degree-10 pieces are the added terms in
(1) and (2).

Likewise, the double-Frobenius part `Kdouble={UF,VF}` has degree ten and is
divisible by nine.  It enters `E1` as `Kdouble/3`, still vanishes in
`F mod 3`, and reappears in `F1` as `Kdouble/9`.  The first-/next-digit term
`T mod 3` still has degree at most nine: Frobenius derivatives in its higher
part vanish there.  Hence degree 12 remains purely `N12={C7,D7}`.

## 2. Exact nonzero source terms

With

```text
UF=fua*y^6+fa*x^3*y^3+fb*x^6,
VF=fc*y^6+fd*x^3*y^3+fvb*x^6,
```

the AWS replay derives

```text
{UF,VF}/9 mod 3
 = (2 fa fc+fua fd) x^2 y^8
 + (fb fc+2 fua fvb) x^5 y^5
 + (2 fb fd+fa fvb) x^8 y^2.                      (8)
```

These are exactly the three derivative-cokernel bidegrees missing from the
pure `N10` derivative row.  The generic corrected-row hashes are

```text
Q11: 33f254938a7a8188abd5420408b166b1185d0f0b77d88e29487f6bcdace9ceac
Q10: 4092fbef5741755de22c4a41fe55aa4373fa9d8e4d5f9e723402bd81bd82d16c. (9)
```

Two minimal controls prove that the omitted summands are actually nonzero:

```text
UF=x^6, D7=y^7  => [({UF,D7})/3] = 2 x^5 y^6,
UF=x^6, VF=y^6 => [{UF,VF}/9]    =   x^5 y^5.       (10)
```

The first control has total degree 11 and the second total degree 10.  They
are universal source controls, not claimed predecessor points.

## 3. Preservation and quarantine table

| Artifact/claim | Disposition |
|---|---|
| Frozen full-C5 predecessor and first following Cartier gate | Unaffected |
| Binary Wronskian classification of `N12=0` | Correct and unaffected |
| Pure-`N` radial identities for `N12,N11,N10` | Algebraically correct, but only as the explicitly stated pure-`N` summand |
| Six current degree-six Frobenius spectators are absent from degree 11 | Still correct; the corrected added term uses `C7,D7`, not those spectators |
| Sharded `N12` count `629,115` and its per-base histogram | Correct source row; retained provisionally pending monolithic agreement/review |
| Sharded old-`N11` count `602,343` / `439,108,047` | Quarantined wrong-source diagnostic; not a lift count |
| `F/3` has maximum degree nine | Retracted |
| Old monolithic degree-11 runner | Quarantine its degree-11 interpretation; degree-12 output remains usable |
| Preregistered pure degree-ten runner | Source-incomplete and stopped before output; do not run |

Frozen erroneous bytes and remote outputs are preserved as provenance; they
are not mutated.  This report supersedes their full-gate interpretation.

## 4. AWS replay and scope

The exact-integer replay ran on Box02 under tag
`as_d7_top_frob_erratum_20260825T003321Z` at
`2026-08-25T00:34:13Z`, return code zero.  The source archive and output
hashes are

```text
source archive:
  105a7e0d3fb10514afb0b38eabf78b2642346154a5a0068becbee0e97ba7e478
source FREEZE:
  d9be1ceff015d35ea434e8c1250f917ae56f071d1402b0d6b23a2d07b1a919c2
replay.out:
  5147309670dc3e0d7caaadc93ddf2a08c1c1b97e57cbf182bae6d40fbed123fd
replay.err: empty.                                         (11)
```

The next licensed task is to attach (1) to the exact predecessor census and
only then form (2).  No corrected count is claimed here.  There is no lower
row, recurrence, all-depth, characteristic-zero, no-lift, counterexample,
or JC2 conclusion.
