# Adversarial review: SHEET6-DIRECTIONB.md §6.T + §6.V (window-build verdict)

You are Grok 4.6, acting as a hostile referee for the JC2 campaign in
/Users/dc/code/math/jc72108 (full read access, you may run python3).

## The claim under review
§6.V of SHEET6-DIRECTIONB.md concludes: the 83-var forced-nonzero-tail
window does NOT kill residue-A ("NOT EMPTY-BY-KILL"): the linearization
relaxation is consistent (rank 57 of 77, -42 in the column span), while
the differential at the zero-tail point is inconsistent (rank 29) and
all closed-form strata die. Survivor locus V = 47 band conditions +
slot-20 condition; 32 residual low-data-dependent obstruction rows.

## Your job: try to BREAK it, in both directions
(a) FALSE-SURVIVAL hazard (our history: one survival claim was retracted
    when a review found the object was wrong). Check: is the relaxation
    in (1) genuinely an OVER-approximation of the true solution set
    (every var-monomial independent — is the monomial list complete,
    including the degree-3 low monomials feeding eta^0)? Were any rows
    of the true window dropped before ranking? Is the -42 normalization
    (the E5-corrected factor, SHEET6-TEMPLATE.md line ~239 erratum)
    used consistently between gate and verdict phases?
(b) FALSE-KILL-SHARPNESS hazard: the doc claims the differential (2) is
    inconsistent uniformly in the 7 dead-stretch values. Check the
    uniformity argument (7 free, incl. all-zero) — sampled or exact?
(c) Reproduce: cd cases && python3 directionb_window.py gate (16/16,
    ~3s), bands (~11s), verdict (7/7, ~89s). Report any mismatch.
(d) Semantics: does "no linear-algebra kill" in (1) actually imply no
    FUNCTIONAL kill of the kind that proved the zero-tail theorem, or
    only no kill by THIS row set at depth 21? Is the §6.V wording
    honest about that distinction?
(e) The 47 band conditions: spot-check 3 of them against a direct jet
    computation (the engine has the machinery; pick band 8 or 12).

## Deliverable
Write /Users/dc/code/math/jc72108/xmodel/grok-directionb-review.md:
VERDICT line first (SOUND / SOUND-WITH-ERRATA / BROKEN + one sentence),
then findings ranked by severity, each with file:line + how you checked.
Do not modify any other repo file. No git.
