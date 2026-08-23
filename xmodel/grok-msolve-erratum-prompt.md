You are Grok, adversarial verifier. Repo: /Users/dc/code/math/jc2. A soundness
ERRATUM has been proposed (uncommitted edit at the top of AUDIT.md — read it
via `git diff AUDIT.md`) claiming: msolve 0.10.1 `-g` on characteristic-0 input
can return the reduced GB of the FIRST machine prime only — in particular, in
the unit-ideal case it can return [1] after the first modular computation,
before CRT/rational reconstruction, while still printing a char-0 header. If
true, the campaign's archived char-0 `[1]` outputs for the cCa2/cCa6 strata of
(72,108) subcase (2) are modular evidence only (chartG is unaffected: its
system contains the literal generator -1). Your job: CONFIRM or REFUTE the
claimed msolve behavior, by source + experiment. Write xmodel/grok-msolve-erratum.md.

EVIDENCE SO FAR (outgoing coordinator's quick probe, on box01
ubuntu@54.175.21.169, key ~/.ssh/claude-cli.pem — msolve source at
/home/ubuntu/msolve; LOCAL msolve is banned, run everything on box01):
 - toy char-0 run: "Initial prime = 1093866353".
 - planted trap (1093866353*x-1, y-1): msolve CHANGED its initial prime
   (1110619847), used 5 primes, 0 bad, returned the CORRECT proper GB. So
   there is at least coefficient-level bad-prime avoidance, and the naive
   short-circuit did NOT reproduce.

WHAT TO DO:
 1. SOURCE: read msolve's multi-modular driver (src/msolve/, the -g/groebner
    path): find (a) the prime-selection filter (what exactly is excluded —
    leading coefficients only? content? all coefficients?); (b) the
    unit-ideal / [1] handling: is there an early-return when a modular GB is
    [1]? does it verify with a second prime / lift the cofactor? (c) whether
    the printed "#field characteristic: 0" header reflects the computation
    performed.
 2. EXPERIMENT: design a probe where the FIRST SELECTED prime is bad but no
    input coefficient reveals it (badness hidden in a determinant/resultant,
    e.g. an ideal proper over Q whose reduced Q-GB has the initial prime in a
    denominator while inputs have small coefficients — you know the initial
    prime is input-dependent, so first extract the selection rule from source,
    then construct accordingly). Run it on box01. Does msolve return a wrong
    [1]?
 3. FORENSICS: inspect the archived campaign outputs
    /Users/dc/code/math/jc2/jc72108/runs/open_8_28_c2_cCa2.q.out and (if
    present) the cCa6 char-0 output + any verbose logs: do they show #primes
    used, CRT/reconstruction evidence, or anything distinguishing a first-prime
    exit from a completed multi-modular run?
VERDICT: CONFIRMED (the erratum stands: archived char-0 [1] = first-prime
evidence) / REFUTED (msolve's char-0 [1] is a certified-over-Q result, or at
least multi-prime-verified — state exactly what it certifies) / PARTIAL (state
precisely which scenario is dangerous). Note: even if REFUTED, finitely many
modular [1]s without a rational cofactor certificate are still not a Q-membership
certificate — distinguish "msolve bug" from "evidence-tier philosophy". Terse,
technical, show the source lines and the probe.
