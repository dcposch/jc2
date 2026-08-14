# Task: the priced inter-merge normal form (td-11/13 refile, step 1)

You are GPT 5.6 Sol, primary research, repo /Users/dc/code/math/jc72108
(full access, python3). Your own scope doc (xmodel/sol-td11-13-scope.md)
named THE top risk of the td-11/13 refile: "failure to prove a finite,
completeness-preserving normal form for priced inter-merge states."
Solve or precisely reduce that problem now, BEFORE the census compiler
is built, so the compiler consumes a proved normal form instead of an
ad-hoc state space.

## Inputs
- Your scope doc section 1 (the state-space analysis: multi-orbit /
  mixed / nested merges with current-state multiplicities and
  vertex-level E5F).
- The td-7 precedent: BOOK-OFFAXIS sections 6-10 (R1/R2 chain calculus,
  the lambda-budget P0/P1), td7_census_e5.py (the E5 pin discipline),
  TOWER-UNIFORM.md lemma kernel (L-A, M=1 absorption, N1, N4, E5F port
  as proved — your scope's own list).
- The depth-closure invariant (SHEET6-DEPTH.md: w=(kappa-rho)/nu
  conserved by l=0 steps; BOOK(m,td) finite, d0 <= 2 gen + 2) — the
  finiteness mechanism that worked at the book level.

## The problem, precisely
A priced inter-merge state must record enough to (a) price onward steps
(lambda-budget), (b) apply E5F at each vertex, (c) decide merge legality
(mu-divisibility, subadditivity), (d) support the tower-tier clash
arithmetic downstream. Naively this state space is infinite (chain
lengths, multiplicity vectors, characteristic data). Find the normal
form: a finite set of state invariants such that two states with equal
invariants have identical futures (completeness preservation), with a
PROOF, or an explicit reduction to a minimal set of unproven lemmas.

## Deliverable
xmodel/sol-normalform.md: 5-line exec summary (SOLVED / REDUCED-TO-N-
LEMMAS / OBSTRUCTED + the invariant list), the normal form definition,
the completeness proof or lemma list, a worked example on td-11 entry
11-A (your intruder entry — does the normal form tame its 5/8 intruder
family?), and the compiler interface spec (what the census engine
stores per state). Label unproven steps CONJECTURE. No repo
modifications except your output file. No git.
