# Proposed p523 place metadata — ROOT manual calculation

INTERNAL MANUAL CANDIDATE, UNREVIEWED. This is a proposed input for future
independent reconstruction, not registration, an execution payload, a source
baseline, or a fully admissible place. No mathematical subprocess was used.
Publication lease began2026-09-11 03:24:17UTC. Planned reserve03:30/HARD03:33
was inherited across compaction and is recorded now without resetting it.

## Proposed values

All arrays below are ascending powers of V, constant first. Mathematical
integers are decimal strings. The proposed place fields are:

- p="523", degree="1", phi=["0","1"].
- P7_mod_p=["0","17","249","53","102","191","291","1"].

The producer and checker must each reconstruct the monic septic from the
literal formulas, compare every coefficient, independently check the prime
and factor, and perform all scalar, denominator and column checks. These
handwritten values are not a substitute for any of those checks. No source
registration or execution is authorized by this report.

## Manual coefficient derivation

At tau=3/10="471" mod523, the literal leading expressions give:

- dL=["310","410","12"].
- K=["208","207","346","206"].
- gamma=["171","62","384","487"].
- B=-140*tau*(1+tau-6V)=["50","252"].
- L=-245*120*144*tau="287", L_inverse="441".

Using S7=2K^2+B*K*dL+245*gamma*dL^2, the padded eight-coefficient
summands, their sum, and normalization are:

- 2K^2=["233","157","148","255","491","69","146","0"].
- B*K*dL=["228","272","9","266","315","388","51","0"].
- 245*gamma*dL^2=["62","266","178","46","226","491","163","287"].
- S7=["0","172","335","44","509","425","360","287"].
- L_inverse*S7=["0","17","249","53","102","191","291","1"].

Intermediate manual multiplication checks:

- K*dL=["151","395","70","50","225","380"].
- dL^2=["391","22","335","426","144"].
- gamma*dL^2=["440","285","116","124","18","414","212","46"].

The zero constant agrees with the earlier factored expression
S7(0)=dL(0)^2*(2+tau)*(3+tau)*(48+5tau-27tau^2), whose last factor at3/10
is9*523/100. The leading coefficient287 agrees with L; 287*441 is1 modulo523.
The displayed monic vector has P7'(0)="17", so this manual calculation also
finds the proposed linear root simple. This extra check remains UNREVIEWED;
it is not needed to replace any source acceptance condition.

## Scope and remaining checks

The previous manual precheck found fixed D0/D1/D2 denominators and five
scalar residues nonzero: dL="310", W="151", t5="9", H7_5="428", H7_6="95".
ROOT's earlier H7_5="137" scratch was erroneous and corrected in notes03:17;
it was never used in source code, execution or qualified metadata.

Ten tests remain UNKNOWN: det1 through det6, critical_c, pivot8, pivot9,
pivot10. No fully admissible place follows from the five checked scalars or
from a simple root. A vanished remaining inverse means BAD PLACE for this
circuit, not a source result or a characteristic-zero scalar vanishing.
Although F=V/W reduces to zero, it is not explicitly inverted. Do not erase
generic terms or alter generic support because of that residue.

This is a proposed finite leading-field place, not a source point, reopened
highest-axis/REG experiment, rank calculation, family exclusion, or JC2
proof/counterexample. The source and runtime implementations remain subject
to their own completion and independent review gates.

## Read scope and custody

Exactly three scientific inputs were used, with same-ROOT previously complete
WHOLE-read/current-pin reuse, not a claim of three new fresh-WHOLE reads:

- box/f10-source-cone-direct-circuit-astra-20260911/OPERATIONS.md:
  3be532afc6e784842694cf02d4399573228362abb47ae36130ef97c4274faa59.
- box/f10-direct-rows-wire-root-20260911/ROOT-ADOPTED-WIRE-PINS.md:
  2b2770fe494098812a52c6829a4bd97803f44bb0474863b8008a69f3725956fd.
- xmodel/f10-r3-vzero-place-astra-20260911.md:
  3f70c36d66bb9cc8fdbbb53a8546fcf1dc4547897374cc50a3b55658d7b1bbcb.

All three were hash-checked before the lease and again03:30UTC after
compaction; the third was also freshly read WHOLE at that point. No live
author source was read. Own final-body WHOLE and current postpins precede
the unique completion marker, close, finalize and expected-manifest VERIFY.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d. No shared theorem promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4328`.
- Body SHA-256:
  `2b13630d035b24b8bd8ac95003dd9c3ac8096d3865c02bc544064143600dac63`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
