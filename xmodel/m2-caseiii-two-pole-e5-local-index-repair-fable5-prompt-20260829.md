# Fable 5 primary repair — two-pole case III under promoted Q+E5

You found the blocking notation error in Sol's R1. Now act as the primary
repairer, not as reviewer. Work from `/Users/dc/code/math/jc2` and write:

`xmodel/m2-caseiii-two-pole-e5-local-index-repair-fable5-20260829.md`

Create a fresh packet only at:

`cases/m2_caseiii_two_pole_e5_local_index_r2_20260829/`

R1 must remain byte-untouched. Read the R1 report/packet and your full hostile
review, then re-found the result strictly on the promoted Q+E5/H5a reading in
`xmodel/sol-h5a.md`, `xmodel/grok-h5a-review.md`,
`ladder/BOOK-OFFAXIS.md` §§6--11a, `ladder/SHEET6-DEPTH.md` §§5c--5d,
`ladder/SHEET6-MULTIPOLE.md`, `cases/td7_census_e5.py`, and the relevant
`cases/book_offaxis.py` solver branch.

Required mathematical output:

1. State and prove the reading-independent two-pole difficult-regime lemma
   `dq/D <= 2*delta+3` and
   `kbar <= mu*w*(2*delta+3)`, including every scope hypothesis.
2. Under Q+E5 derive the exact elimination
   `mu0*nu_G*w_U = delta*kbar + mu*w` and the sharp corresponding bounds on
   merge-local `nu_G` in all multiplicity regimes. Explicitly prove that no
   incoming `nu_U`/`nu_H` bound follows or is required.
3. Recompute all 17 promoted cells, the old td-7 discriminator slice, and
   exact equality/sharpness cases. State that equality in the ratio bound has
   `D=M=1` and is MP2-dead; determine the best useful M>=2 refinement if one
   is honestly provable.
4. Plant multi-nonzero/inner-arrival counterfixtures showing exactly why the
   two-pole theorem cannot be widened.
5. Give a precise source-level migration plan from the legacy capped
   `nu_H` enumeration to a Q+E5 merge-local solve in the
   `td7_census_e5.py` style. Do not modify the canonical engine in this task.

The packet must use exact arithmetic, have ordinary and `python3 -O` tests,
new hostile mutations, sealed JSON output, and a claim firewall. Correct the
R1 adjudication of Opus in both directions and regenerate every certificate
field rather than patching prose. Final status is source-ready for
different-model hostile review; it authorizes no canonical engine change or
AWS action.

Hard boundaries: no web, AWS, commit, push, canonical edits, heavy CAS, or
local long/high-memory process. Never access/list/search/build/status or
control `jc2-lean`; never run global `git status` or workspace-wide searches.
Modify only the named report and fresh R2 packet; use `/tmp` for scratch.
