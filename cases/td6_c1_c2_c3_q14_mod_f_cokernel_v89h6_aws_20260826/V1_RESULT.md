# TD6 V89H5V1 q14-plus-high unimodular inverse result

Date: 2026-08-26

Producer verdict: **exact inverse gate PASS; strict q-zero-remainder gate FAILS
closed on Box02 and r6d (both rc 1).**

## Exact retained family

The clients set `q2,...,q13=0`, keep q15 absent under the reviewed target
shear, and retain independent untruncated `q14,q16,...,q24`.  Both rebuild
literal V87 transport, all 38 packed raw FIRST maps, and genuine raw P12 from
the frozen source package.  Their q-zero source digests match V85.

## Unimodular inverse theorem

The full retained-q FIRST support graph has 368 edges and one cyclic SCC,

```text
S = {0,1,2,3,4,5,6,13}.
```

All q support inside its 8 by 8 block is `q14`.  Division-free subset DP
gives determinant exactly `1`; the emitted adjugate is a two-sided inverse.
SCC condensation then gives an explicit finite polynomial two-sided inverse
of the full 38 by 38 FIRST pivot block.  It has 3,168 nonzero coordinate
rows, introduces no denominator, and replays exactly in the 38 original
FIRST sources.  This portion is byte-identical on both AWS hosts.

## Exact obstruction to the preregistered collapse route

Reducing literal P12 through that inverse replays in the original FIRST
sources and leaves 18 records rather than only the frozen q-zero unit:

- one q-zero record;
- seventeen positive records, all with q monomial `(14,)`;
- no `q16,...,q24` record and no cross-q record.

The complete 18-record remainder has SHA256

```text
eb939448f5636a3084ca129aa3a5cdf44709ac3a8ca28be77a14c2e5fdea7c14.
```

The client emits the obstruction and then hits its preregistered strict
assertion `remainder == q-zero unit`, so both hosts terminate with rc 1.
No denominator-cleared total-F composition is attempted or claimed.

This failure does **not** show that `(P12,FIRST,F)` is nonunit: it only
rejects the specific q-zero-remainder shortcut for this normalized inverse.
The V89H5V2 client separately tests whether all seventeen positive records are
coefficientwise in `(F)` on the registered open.

## Scope firewall

The exact inverse theorem is restricted to the displayed residue block.
It does not cover `q2,...,q13` unit charts.  The remainder result does not
exclude alternate combinations of FIRST, and neither result is a total-Rees
theorem, a source point, whole fixed A3, TD6, SP-2, or JC2 result.

## Custody

- source archive:
  `ff286114688c4cab111d7d09cb2fd4bc17beaee213d9ebf802d9cf876aa59651`;
- source manifest:
  `ce109eb196664ac83708ba2e66ea7da6799800a56878820fdfb3980dd2550d17`;
- client:
  `a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b`;
- byte-identical stdout:
  `9261d8f5d1caa174e709eba75ff9f7072822a15beb260b164639fd5a8d1bbdbf`;
- SCC determinant:
  `eab9d41987bfb0b6073bfef09c7b389dfccd7848e4c0bbaac151ac51b5e7caf5`;
- SCC adjugate inverse:
  `93ea22558c824f0ab7884082b2e07defca53baadc9209f12470c2760b0d69ff7`;
- full FIRST inverse:
  `059a6f3cbab5c6b026d1c692d046c96b36b7d5cd65ec0ac2251202c6e4d13860`;
- P12 remainder:
  `eb939448f5636a3084ca129aa3a5cdf44709ac3a8ca28be77a14c2e5fdea7c14`.
