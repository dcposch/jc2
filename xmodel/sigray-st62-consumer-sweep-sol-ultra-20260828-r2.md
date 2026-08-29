# Statement 6.2 consumer sweep — r2 dependency correction

Date: 2026-08-28 UTC.  Status: **SUPERSEDES the dependency conclusion of
`d64b043c...`**.  The exact source-defect diagnosis and consumer census in r1
remain valid; this addendum corrects which later propositions supply the
missing next-vertex domain.

## Correction

The r1 sweep and several promoted reviews conflated two source operations:

- `G*_(kappa)c`, the point one grid step above `G` (Notation 3.8); and
- `H=G+c`, the next actual vertex in direction `c` (Proposition 3.2).

Proposition 6.7 proves positivity only for the first object.  It does not by
itself prove `H in T_a^+`, which is what Statement 6.2 and regularity require.
The missing bridge uses **both repaired Proposition 6.7 and repaired
Proposition 6.8**, as derived in
`xmodel/sigray-prop67-prop68-source-audit-sol-ultra-20260828.md`
(`c3d6ff92...`, pending different-model review at this filing).

Let `G in V_a cap T_a^down`, let `F=G+c` be a down child, and let `c*` be an
alternative root with
`m*=mult(p_G,c*) >= mult(p_G,c)`.  The raw, valid calculation from Statement
6.2 gives

```text
d_G < (1-pi(G))*m*.
```

For the realizable microstep `E=G*_(kappa)c*`, exact Statement 3.9 for the
fixed fibre polynomial gives

```text
d_E=d_G-m*/kappa,
deg p_E=m*,
pi(E)=pi(G)+1/kappa.
```

Hence `E in T_a^down`; Proposition 6.7 supplies the needed positivity.  If
`m*=1`, Lemma 6.1 and the repaired pole-threshold argument make `E` a pole
vertex.  If `m*>1`, repaired Proposition 6.8 constructs a pole above `E` on
the same branch while keeping every grid ancestor down.  The first actual
vertex `H` in that direction is therefore down, in particular positive.

## Corrected consumer verdict

There is still **no identified mathematical rollback**, but that conclusion
is conditional on the complete repairs of **both** Propositions 6.7 and 6.8,
not on Proposition 6.7 alone.  This applies to every regularity consumer:

- `SHEET6-AF2.md`;
- `SHEET6-A2P-REVIEW.md`;
- `SHEET6-III.md`;
- `SHEET6-MULTIPOLE.md`;
- the Statements 9.6--9.11 template in `SHEET6-CAMPAIGN.md`.

The source audit finds both propositions repairable with unchanged
conclusions.  Its Proposition 6.7 repairs are a cyclic-residual
semi-invariance lemma and replacement of an illegal exact Statement 3.9 use
on `h_F` by Statement 3.11.  Proposition 6.8 needs
`d_(F_n)<=d_F-n/kappa`, not the false printed `d_(F_n)<=u-n/kappa`, plus an
explicit final-branch argument.  Until a different-model review seals that
packet, the consumer verdict is **PROVISIONALLY SAFE UNDER REPAIR**, not
unconditionally banked.
