# Gate T: reviewed unique-`AC` A2D2 additive repair

Date: 2026-08-27

Status: **ALL SIX OPUS5 PRESENTATION/CUSTODY REPAIRS APPLIED ADDITIVELY;
THE ONE-CONTACT THEOREM IS REVIEW-CONFIRMED AND ELIGIBLE FOR NARROW
PROMOTION.**

Immutable producer and hostile review:

```text
1d086a79b0d4e7a6a9905391dc13acf4571d766292c58c7b2f25b1c673141457
  xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-sol-20260827.md
23007a2bb15e866f87a05bdff9f7a0ea0f1b05588d721d4b03bd377f0b89ce12
  xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-hostile-review-opus5-20260827.md
```

Neither is rewritten.  This note is the authoritative repair layer.

## Six repairs

1. The contact is the first missing contact **at or after** the already
   transported `(a,c,r_floor)=(2,3,2)` base.  It is not the globally first
   missing contact.  The two strictly earlier untransported cells are
   `(1,3,2)` (`G=14,T=16`) and `E=(1,4,2)` (`G=15,T=18`).
2. Every unlabelled triple in this repair uses the convention
   `(a,c,r_floor)`.  A tuple involving `d=c-a` or `s=r-a` is explicitly
   labelled `(a,d,s)`.
3. The saturation calculation is in
   `U_18^rho[au,cv,lam,rho1,rho2]` with `p:=-2*rho^2`.  The allocation
   reference is the producer's (6.2), not its dangling (5.2).
4. On this contact, the grade-16--18 coefficients involve exactly the
   eighteen reviewed jets.  The restricted map `delta_22` is a bijective
   scalar renaming, with factors `2` and `4`; emptiness therefore transfers
   from the D1 row system to the total contact without reversing a ring map.
5. The allocation-open saturation is the unit ideal only where
   `au*cv != 0`.  Off that open, the degree argument from the first `AC`
   remainder equations forces one leading linear factor to vanish, contrary
   to exact `ord(A)=2` or exact `ord(C)=4`.  The two cases together, not the
   saturation alone, exclude the contact.
6. V33 supplied a general-`rho` construction path and frozen `rho=0` slice,
   not frozen general-`rho` grade-18 bytes; 49 of 77 live grade-18 terms were
   invisible on that slice.  The later additive `ACT-TOT-G20` custody lemma
   now supplies the stronger general-`rho` construction custody through
   grade 20 on exact-Q and `F_65521` lanes with a coefficientwise cross-lane
   check:

   ```text
   c8a14e4fc4c627263e75f963838293dbe88ee46d17c770b7be16eb76799418cf  Q
   4b4b49b52e29a69c4bae6d88e7bc456dc96db7b299a67652d74287b2696df9e2  F_65521
   6b3f87e68cd30fe9cb35934bad4fa8cebd1ad0181d5212aa7165ee728f6567bb  cross
   ```

   Thus `ACT-TOT-G18-GENERAL-RHO` is discharged by the stronger G20 custody
   result; no V33 face byte is relabelled.

## Primary reviewed proof

The Opus5 review independently reconstructed the total rows and found the
cheaper direct-coordinate certificate.  Put

```text
A0=aaa1*z+aaa0,
C0=(ez4*z+ec4)/2,
L=z^2-rho^2.
```

On this contact all seven rows vanish in grades `0..15`, and the three
needed coefficients are exactly

```text
g1=[sigma^16]Phi1=(3/8)*(aaa0*ez4+aaa1*ec4),
g2=[sigma^16]Phi2=(3/8)*(aaa0*ec4+rho^2*aaa1*ez4),
g4=[sigma^18]Phi4=(3/32)*(ec4^2+rho^2*ez4^2).
```

The four exact syzygies in the additive uniform three-row replay put

```text
aaa1*rho^2*ez4^2, aaa1*ec4^2,
aaa0*rho^2*ez4^2, aaa0*ec4^2
```

in `(g1,g2,g4)`.  On `D(rho)` and the exact-`A` open
`D(aaa0) union D(aaa1)`, the radical therefore contains `ez4,ec4`,
contradicting exact `ord(C)=4`.  This is the primary proof.  It requires no
root allocation or extra localization; the reviewed B22 moving-root residue
is a corroborating second proof.

## Reviewed theorem and scope

In the post-gate Kummer total source over a characteristic-zero field, after
the reviewed generic-square first-normal, half-weight, and exact reduced
`M=0` gates, there is no normalized DVR arc with

```text
ord(A)=2, ord(C)=4, ord(R)>=3, rho != 0.
```

The conclusion is arcwise/set-theoretic.  The original registered
unit-`k10` chart stated it on `D(rho*k10lead)`; the direct certificate only
uses `rho != 0`.  It does not cover the `ord(R)=2` equality face, either
earlier cell `(1,3,2)` or `E`, any other contact, `rho=0`, a positive-order
load, a Rees chart or terminal receiver, the generic-square fan, either
global `G2` obligation, Gate T, order two, maximum twelve, JC2, or a
counterexample.

The additive replay pins the producer/review, G20 Q/P/cross custody, and the
uniform syzygy interface, then reruns the ledger and syzygy controls.  It
must emit `PASS-KGT-DRHO-UAC-A2D2-REVIEW-REPAIR-V2`.

