# Audit/addendum: valuation-five v2 grade-19 closure and custody

Date: 2026-08-29  
Reviewer: Sol 5.6 Ultra  
Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`  
Reviewed report: `xmodel/k00-r5-jetfan-v2-repair-opus5-20260829.md`  
Reviewed report full SHA-256: `91dcf1731590ca2bdae53804c911c01b2a4ba1ebfc58aa6e182f402c84292d84`  
Reviewed report body SHA-256: `a13c02edb9e79161cb6f43c4ec05e670e65ad94c6ae83ef1447d58018b68ff21`  
Verdict: **GRADE-19 MATHEMATICS CONFIRMED; CUSTODY WORDING CORRECTED BELOW**

## Audit procedure

I read the full sealed report and its complete embedded replay.  The seal
verifies on the displayed frozen basis.  The unique embedded Python block has
SHA-256

```text
e7c6cab141c31f2732481bd8a19eeea91ac19786e8bfce81e5e4691e97f9d83a
```

as claimed.  I ran that source in ordinary and optimized Python, intercepting
only its optional `/tmp/K00-R5-R0-RESIDUAL-v2.txt` write in memory.  Both runs
returned `K00_R5_V2_REPLAY=PASS`; both produced the same 207498 canonical
bytes and residual SHA-256
`02b4cb9f90dfb72eca05608386578de57b6d4db93ef94c1ed60cb807e95f9e6e`.
All five mutations fired.

I then inspected the exact intermediate series rather than relying only on
the replay's final marker.  No CAS, web service, AWS resource, git operation,
canonical file, or `jc2-lean` path was used.

## 1. Grade-19 ideal membership is correct

On the rank-zero substitution

```text
d[5]=ell(s,t)=(2s,t/8,s,t,s,2t),
```

the independent intermediate checks gave

```text
D10(d): first nonzero grade 17; grades 15 and 16 are exactly zero,
D6(d) : first nonzero grade 12; grades 10 and 11 are exactly zero,
D2(d) : first nonzero grade 11.
```

More precisely, with `A6=A(d[6])` and `B6=B(d[6])`, the replayed sparse
polynomials satisfy

```text
[L^12]D6 = -(3/512) A6 B6,

[L^17]D10 = -(295/262144)s A6 B6
             -(295/524288)t(B6^2-64A6^2).
```

Thus the exact contracted load coefficient is

```text
E19 := [L^19](p10 D10+p6 D6)
     = -[(295/48)k10_0 s+32k6_1]
         ([L^12]Phi_3+(1/8)[L^12]Phi_1)
       -(295/3)k10_0 t [L^12]Phi_4.                 (1)
```

This identity was checked as equality of full sparse polynomials, with all
source coefficients still symbolic.  It is membership in the grade-12 ideal,
not merely membership in its radical.

The contracted seven-row relation has the correctly signed terminal term:

```text
H19 := [L^19](h Phi_7-sum_{i=1}^6 u_i Phi_i)
     = E19-5 Jdet_0.                                (2)
```

The other contracted sectors cannot reach grade 19.  On this cell the exact
order of `p2 D2` is 22; the report's earlier lower bound `>=21` is conservative
and its later exact order 22 is correct.  The even-target products start at
orders at least 20, 22, and 24.  The factor `5` in (2) is exactly
`h(0)/4=20/4`, including the row-7 target sign `-Jdet_0/4`.

Combining (1) and (2) gives the displayed certificate

```text
5 Jdet_0
 = -[(295/48)k10_0 s+32k6_1]
       ([L^12]Phi_3+(1/8)[L^12]Phi_1)
   -(295/3)k10_0 t [L^12]Phi_4
   -H19.
```

Here `H19` is itself an explicit polynomial combination of the coefficient
equations through grade 19.  Therefore `5*Jdet_0` lies in the defining ideal
after the rank-zero substitution.  Over a `Q`-algebra with `Jdet_0` inverted,
the localized ideal is the unit ideal.  The report's scheme-theoretic
rank-zero emptiness claim is valid and uses neither reducedness nor an
algebraic-closure argument.

## 2. Grade calendar and source projection are correct

The literal calendar follows directly from valuation five and the fixed
boundary constants:

| sector | first grade |
|---|---:|
| unloaded quadratic | 10 |
| K10 quadratic; K6 linear | 12 |
| unloaded cubic; first `mu2` target | 15 |
| K2 linear | 16 |
| K10 cubic; K6 quadratic; first `mu4` target | 17 |
| first `mu6` and `Jdet` targets | 19 |

The generic dependency ranges through grade 19 are exactly

```text
d[5..14], k10[0..7], k6[1..8], k2[1..4],
mu2[1..5], mu4[1..3], mu6[1], Jdet[0].
```

After the rank-zero substitution, the literal minimal projection is exactly

```text
s,t; d_i[6..13]; k10[0..6]; k6[1..7]; k2[1..4];
mu2[1..5]; mu4[1..3]; mu6[1]; Jdet[0],
```

giving 78 live coordinates.  The 58-coordinate free affine factor is

```text
d_i[14..19], k10[7..17], k6[8..13], k2[5..9].
```

In particular, `k10[6]` and `k6[7]` really occur in the literal grade-19
rows; `k10[7]`, `k6[8]`, and `d_i[14]` do not.  The former coefficients lie
in `(A6,B6)` but need not lie in the quadratic grade-12 ideal.  This distinction
does not enter the terminal certificate (1), which is an exact ideal identity.

The counts `169` labelled columns, `164` after five boundary zeros, and `140`
after the 24 valuation-five zeros are consistent.  In the report's
`169=24+6+48+36+55` bookkeeping, the last `55` intentionally includes the
five boundary-fixed load/target columns; it is not a claim that all 55 are
free.

## 3. Custody wording defect and clean correction

The embedded replay's `PINS` dictionary contains exactly ten paths:

```text
tails.json,
compile_contracted_source_v20r2.py,
serialized_replay_prelude_Q.sing,
LOCAL_UNIT_WITNESS_R1.txt,
UNIT_MULTIPLIER_1.txt,...,UNIT_MULTIPLIER_6.txt.
```

Accordingly `SOURCE_PINS_VERIFIED=10` is accurate.  However, Section 1 first
says that the charter names "four" artifacts while displaying five, and then
says "All five verified byte-exact."  Of those displayed five, only the tails
and compiler occur in `PINS`.  These three contextual files do **not**:

```text
xmodel/k00-r5-jetfan-provisional-sol56-20260829.md
xmodel/k00-r5-jetfan-replay-sol56-20260829.py
xmodel/k00-r5-jetfan-internal-hostile-audit-sol56-20260829.md
```

I independently checked them during this audit.  Their current hashes equal
the three hashes printed in the report (`82e6512d...`, `eb8513b6...`, and
`fee02eb0...`), so there is no observed byte drift.  Nevertheless, the
embedded replay neither verifies nor binds them.  They also do not appear in
the canonical residual's `PIN` lines, so its published byte count and digest
do not commit to those contextual documents.

The clean correction is **wording only**.  Do not add the three contextual
documents to `PINS`, because the proof deliberately does not consume them and
doing so would unnecessarily change the residual serialization.  Section 1
should be read as:

> The embedded replay verifies ten mathematical source artifacts: the tails,
> compiler, prelude, unit witness, and six multipliers.  The rejected producer,
> rejected replay, and binding audit are contextual readings, not replay pins;
> their recorded hashes were not checked by the embedded replay.

Section 11's statement that no "existing artifact" was read is also literally
false and conflicts with Sections 0--1.  Its intended, accurate replacement is:

> No canonical ledger or `jc2-lean` path was accessed and no existing
> repository artifact was modified.  Only the explicitly named mathematical
> inputs and contextual reports were read.

Finally, the embedded source docstring says "four mutation controls" although
the code and report correctly implement five.  This is a harmless count typo.

## Verdict

The custody overstatement and two minor wording/count errors do not feed any
algebraic computation.  The ten actual mathematical pins verify, the source
calendar and residual projection close, and the exact grade-19 identity proves
`5*Jdet_0` ideal membership.  The valuation-five v2 repair's mathematical
conclusion survives this audit unchanged.  This addendum should accompany the
sealed report so its custody claims are interpreted precisely.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7616`.
- Body SHA-256:
  `ad1da4e3970ce2f1d4256fea08007aa751c2b1a918a96ced11e4634be1450c23`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
