# Fable 5 hostile review charge: cutoff-six square-tail field obstruction

You are Fable 5 acting as a hostile, different-model mathematical reviewer in
the plane Jacobian-conjecture campaign.  Work inside
`/Users/dc/code/math/jc2`.  This is an exact certificate review, not a prose
summary.  You have shell access and must actually execute independent
standard-library exact-rational checks.

## Frozen charge and output contract

Review exactly this producer report:

`xmodel/ggv-upper-endpoint-tail6-field-obstruction-r0-sol-ultra-20260828.md`

Required SHA256:

`c62acd1be938b14e10e76c28c6bc45cabf874ed8ef4385d617746fdf104c3101`

Frozen case:

`cases/ggv_8_28_upper_endpoint_tail6_desk_20260828/`

Required pins:

```text
812dc5b7d337dc8a6bb68b5419c4ce0556c2e0ed29e1eb4213d5a79ece3a8269  UNIT_CERTIFICATE.json
86a0c851cea30bb397d4e80bb9cda8a6f50559d5cbc7de649a431960ecd10113  analyze_tail6.py
c038fd929d8c11cf8465dd72edb5fc4cca430140d11199f3c6fbd2f968e1b389  TAIL6/TAIL_DEFORMATION_SYSTEM.json
```

Also run `sha256sum -c SOURCE.sha256` from the frozen case and report every
result.  If any pin fails, stop substantive review, write a `GAP` report, and
identify the mismatch.

Your sole durable output is exactly:

`xmodel/ggv-upper-endpoint-tail6-field-obstruction-crossreview-fable5-20260828.md`

Do not edit any canonical file (`AUDIT.md`, `APPROACHES.md`, `PROGRESS.md`,
`notes.md`, `COORDINATION.md`, or any case/source artifact).  Do not enter,
read, list, search, build, status, or modify `jc2-lean`.  Put any independent
scratch checker under `/tmp`, delete it when finished, and transcribe enough
code/formulas plus exact command outputs into the report for the review to be
auditable.  Do not use Singular, AWS, network access, or meaningful local
compute; this is a desk-scale Python `fractions.Fraction` audit.

At the end, run `sha256sum` on your output report and print to stdout exactly
one final marker of the form

```text
WROTE <path> SHA256 <64-hex> VERDICT <CONFIRMED|GAP|REFUTED>
```

## Independence rule

You may read the producer report, compiler, JSON evidence, and source, and you
must eventually run the producer's documented `--check` replay.  But that
replay alone is not evidence.  Before relying on its conclusion, write and
run an independent implementation under `/tmp` which does **not** import or
execute `analyze_tail6.py`.  Parse the frozen source JSON directly, implement
your own exact polynomial arithmetic and tracked Gaussian/RREF elimination,
and recompute the charged atoms below.  Explicitly say which evidence was
independently reconstructed and which was only custody/replay checked.

## Charged atoms (all mandatory)

Classify each atom `CONFIRMED`, `GAP`, or `REFUTED`, with exact intermediate
formulas and literal outputs.  `CONFIRMED` requires all atoms to pass.

1. **Pins and source geometry.**  Verify every hash above and the full source
   manifest.  From the frozen source—not from copied report prose—recompute
   the cutoff-six census: 220 retained variables, 260 prefix equations through
   `D11`, rank 98, nullity 122, and 253 remaining `D12..D22` equations, or
   explain any discrepancy.

2. **Endpoint sign and carrier identities.**  Independently reconstruct the
   constant endpoint polynomial and establish literally
   `D22[X^0]-1 = -1-p32*p110`.  Trace the nullspace-coordinate labels back to
   the source and check `p32=G15[X^1]`, `p110=F7[X^0]`.  Check the sign rather
   than accepting the serialized certificate.  State why a field endpoint
   forces both carriers nonzero without normalizing either one.

3. **Rows 12 and 13 field-radical cover.**  Independently eliminate each
   row's same-row constant slots from literal frozen equations.  For row 12,
   display the same-row slot count/rank, compatibility count/rank, and verify
   equality of its compatibility row space with the eight coefficients of
   `A^2 mod H`, where `C=X^4-1`, `H=C^2`; justify over a characteristic-zero
   field that this implies `A=C*B`, `deg B<=6`.  For row 13 after this
   substitution, display its slot count/rank and compatibility count/rank;
   verify that the compatibility space is exactly the eight coefficients of
   `B*(4*C*F7-B) mod H` plus the stated scalar `E`.  Recompute the implication
   `B=C*V`, `deg V<=2`, then expand the scalar to exactly
   `V0*(V0-4*p110)/4`.  Prove that the two branches `V0=0` and
   `V0=4*p110` cover all characteristic-zero field points.  Audit carefully
   that these are radical/set-theoretic implications, not scheme identities.

4. **Rows 14/15 elimination.**  On each branch, independently reproduce the
   row-14 and row-15 progressive substitutions from the literal source rows.
   Withhold `p32` from the row-15 pivot set.  Report same-row pivot lists or an
   equally exact identification, the numbers of compatibilities, their ranks,
   cumulative rank after duplicate removal, retained variables/generators and
   maximum degree.  Check that no hidden division by `p110`, `p32`, or another
   parameter occurs.

5. **Both sparse `p110^2` witnesses and literal-row provenance.**  Independently
   expand, term by term, both claimed identities (zero-based indices):

   ```text
   V0=0:
   p110^2 = (1/12)r14[1] + (1/9)r14[13]
             -(2/9)(r15[3]+r15[7]+r15[11]+r15[15]).

   V0=4*p110:
   p110^2 = -r14[9] -(37/9)r14[13]
             +(16/9)r15[3] +(32/9)r15[7]
             +(256/45)r15[11] +(512/63)r15[15].
   ```

   For every selected compatibility, reconstruct it as a rational combination
   of the substituted literal source rows at the correct progressive stage,
   and compare its exact hash/provenance with `UNIT_CERTIFICATE.json`.
   Explicitly distinguish row-15 provenance after row-14 substitutions from
   provenance in the unmodified raw row.  A mere JSON-schema validation or a
   call to the producer compiler is insufficient.

6. **Final unit identity.**  Independently multiply and collect terms in
   `1=(1-p32*p110)(1+p32*p110)+p32^2(p110^2)`.  Confirm that the two inputs are
   actual generators/consequences of each branch target and that no
   localization division is used.  Then run the producer's documented
   `python3 .../analyze_tail6.py --check --output ...` replay and quote its
   decisive marker.

7. **Live mutation.**  In the independent checker, perturb at least one
   nonzero coefficient in one sparse `p110^2` witness (or one contributing
   literal source row) while leaving the target unchanged.  Demonstrate that
   the check fails and print the exact nonzero residual polynomial, not merely
   `False`.  Restore nothing in the frozen case because mutations must be
   in-memory or under `/tmp` only.

8. **Firewall audit.**  State the narrowest valid theorem.  Separately audit:
   (a) characteristic assumptions and any bad-prime issue; (b) field-valued
   emptiness versus a lifted scheme-level unit certificate; (c) fixed
   branch-P square baseline/cutoff-six versus the full branch-P family; and
   (d) absence of any Keller-pair, counterexample, or JC2 conclusion.  Check
   that neither `D23` nor a `G22` slot was silently imposed.

## Required report structure

The report must contain:

1. review identity/date and an overall verdict;
2. a compact atom-by-atom verdict table;
3. exact hash/manifest command output;
4. independent checker method and enough implementation detail to rule out
   circular reuse;
5. all demanded exact formulas, ranks, pivots/provenance, witness expansions,
   final identity expansion, mutation residual, and producer replay marker;
6. the precise promotable theorem and scope firewalls;
7. a final line exactly `FINAL VERDICT: CONFIRMED`, `FINAL VERDICT: GAP`, or
   `FINAL VERDICT: REFUTED`.

Be hostile: search for sign errors, progressive-substitution errors,
cumulative-span artifacts, illicit normalizations/localizations, missed
field branches, characteristic leakage, and overclaim.  If something fails,
do not repair it silently: classify it and explain the narrowest surviving
statement.
