# Task: toric-circuit closure of the monomial relaxation (your avenue #2)

You are GPT 5.6 Sol, primary research, repo /Users/dc/code/math/jc72108
(full access, python3 allowed). This executes YOUR avenue #2 from
xmodel/sol-avenues2.md against the now-final window state.

## State (read first)
- SHEET6-DIRECTIONB.md §6.V (PROMOTED), §7 (level-42 no-log pins,
  PROVED: tf1_42=tf2_42=tg1_42=tg2_42=tg01_42=tg02_42=0), §8 (depth-23:
  still no linear kill; pinned D21 relaxation = 76 rows x 4351 monomial
  cols, rank 56, CONSISTENT; plain D21 = 77 x 5106 rank 57; D23 pinned
  86 x 8623 rank 66).
- Engine: cases/directionb_window.py (relax/esolve/band machinery,
  state-parameterized via DIRECTIONB_STATE env; D21 state
  /tmp/directionb_tails_D21.pkl, banked copy directionb_tails_D21.pkl
  in repo root; D23 at /tmp/directionb_tails_D23.pkl).
- The relaxation treats every var-monomial as an INDEPENDENT column.
  Its consistency is why no linear kill exists. Your avenue: restore
  the multiplicative structure via toric circuits — binomial relations
  m1*m4 = m2*m3 between monomial columns coming from additive relations
  between exponent vectors — and test whether the CLOSED system is
  exactly inconsistent.

## The task
1. Design the circuit closure concretely for the PINNED D21 window
   (76 x 4351, the smallest decisive object): which circuits, how many,
   what closure tier (degree-2 circuits among occurring monomials?
   circuits within each row's support? the full lattice?). Be explicit
   about why your chosen tier is sound (every true solution satisfies
   the added binomials) and about what inconsistency would prove
   (EMPTY forced-tail locus at window tier — state the exact semantics).
2. PILOT: implement and run the cheapest sound tier exactly (exact
   arithmetic over E or QQ; the window engine's esolve/relax functions
   are reusable; python3, sympy available; keep memory < 8 GB). If the
   full tier is too big, run a principled sub-tier and report what it
   does/doesn't decide.
3. If linear-algebra-with-binomials is still consistent: report the
   rank growth and whether iterating closure tiers converges to the
   true variety (and at what cost), i.e. is this a viable kill route
   or a dead end? Kill criterion per your own avenues doc.

## Deliverable
xmodel/sol-toric.md: 5-line executive summary (VERDICT: KILL /
NO-KILL-AT-TIER-N / DEAD-END + why), design, pilot results with exact
numbers, reproduction commands. Write your pilot script to
cases/directionb_toric.py. Do NOT modify any other repo file. No git.
Honesty over optimism; a clean dead-end verdict is valuable.
