# Opus 5 hostile review — Sol U2 fixed-terminal finiteness repair

Producer: Sol 5.6. Work independently from `/Users/dc/code/math/jc2` and write
exactly:

`xmodel/m2-u2-terminal-finiteness-r1-repair-hostile-review-opus5-20260829.md`

Read the complete target
`xmodel/m2-u2-terminal-finiteness-r1-repair-sol56-20260829.md`
(full SHA-256
`3989703ae243705166843dfe5183bbc83cba44d9284071e49deca19cd935933e`,
body `aa6f8685d56c8c7582082717bf802649fa5966282ae76c4666c2c0b6fc9f1bf0`),
Grok's U2 primary only as needed to identify the claimed input, both hostile
reviews of the finite P0-chain theorem, and the exact P0/P1 clauses in current
`ladder/BOOK-OFFAXIS.md`. Do not read Fable's active review of Grok U2 or any
other post-target result. Treat every claim as an allegation.

Audit the theorem at its exact conditional scope:

1. Re-derive the backward laws (R), (E), and (D), including the complete
   four-family partition of P0. Check that no zero-cost, weight-changing
   family is omitted and that every free local parameter is either `n`, `s`,
   or a finite reduced residue record.
2. Attack the uniform `Mhat` bound. Verify `M'|T`, the coprimality with local
   `nu`, `T>=1`, all multiplicity inequalities, and the count of positive-cost
   steps. Seek a dirty or pure-epsilon family that can make `M` grow faster
   than claimed at fixed budget.
3. Attack the compact weight bounds. Check `2C>=s`, the expansion bounds,
   the lower bound on every intermediate weight, the uniform resonance-depth
   bound, and the uniform bound on every weight-changing `nu`. Pay special
   attention to `k=0`, q-extras-only resonance and to `eps>0` with q-extras.
4. Prove or refute Lemma 3.1. Its induction must cover simultaneous unbounded
   integer variables, fixed variables that make an intermediate limiting
   value equal to `w`, and all endpoint/sign cases. Search explicitly for an
   infinite Diophantine family contradicting the lemma.
5. Verify that every fixed path really multiplies into the claimed product
   with fixed positive rational coefficients. Check whether changing `M`,
   residue classes, `l`, partitions, or local legality can create infinitely
   many path types despite bounded depth.
6. Determine whether quotienting neutral/pure-epsilon free `nu` is legal for
   the stated P0/P1 terminal theorem, and state exactly which later consumers
   would invalidate that quotient if the conclusion were widened.
7. Build clean-room symbolic/algebraic checks and small exhaustive searches
   in `/tmp`, including hostile toy parameters designed to focus infinitely
   many `L` to one target. Do not mistake bounded search for proof.

Return `PASS_AT_CONDITIONAL_P0P1_SCOPE`, `PASS_WITH_REPAIR`,
`REPAIR_REQUIRED`, or `FAIL`. Preserve any valid narrower lemma, give a
clause-level scorecard, exact counterexample or repair where applicable,
full/body hashes, commands/counts, and the maximum safe consequence. Even a
pass validates only the implication “reviewed U2 transport + reviewed P0/P1
grammar => finitely many terminal-reaching L at fixed entry/budget.” It does
not validate Grok's U2 ODE, gluing, landing, realization, a panel exclusion,
a td ceiling, or JC2. No AWS is authorized.

Hard boundaries: no web, AWS, commit, push, canonical edits, heavy CAS, or
local long/high-memory process. Never access/list/search/build/status or
control `jc2-lean`; never run global `git status` or workspace-wide searches.
Modify only the requested review report; use `/tmp` for scratch.
