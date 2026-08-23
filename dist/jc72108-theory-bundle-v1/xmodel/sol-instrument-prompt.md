# THE INSTRUMENT DECISION: what kills the residual-32 system?

You are GPT 5.6 Sol, repo /Users/dc/code/math/jc72108 (full access).
Joint decision point with Fable. Read SHEET6-DIRECTIONB.md §7.S (the
full screen campaign record — ~300 lane-hours, everything TIMEOUT
except chamber a3 double-EMPTY) and the §6.V/§7/§8 theory state.

The question: what is the next instrument for deciding the residue-A
nolog system (84 vars, 85 eqs, over E = the Q(sqrt3)-flattened ring,
mod-p variants banked)? Give your ranked recommendation with honest
cost/probability estimates. The option space (add your own):

A. BIGGER IRON: u-6tb1.112xlarge / u-12tb1.112xlarge (4-12 TB RAM,
   ~$40-90/h). Would 3-6x memory change the F4 outcome, or is the
   growth super-exponential and 12 TB buys one more degree step?
   Estimate from the observed growth profile (R2 mains were at
   ~500G/lane at 48h and climbing).
B. DIFFERENT GB ENGINE: FGb (Faugere's, via Maple), magma (license?),
   OpenF4, Singular slimgb, macaulay2 with different strategies —
   any with fundamentally better memory behavior on this shape?
C. SMARTER ELIMINATION: msolve -e with a DESIGNED elimination block
   (the 42 highs first was one choice; the band-triangular structure
   of the 47 conditions suggests eliminating band-by-band — 7 stages
   of small eliminations instead of one big GB). Feasible?
D. CHAMBER MAP v3: real per-chamber fences sized by a Macaulay-proxy
   pilot, on the big-iron box, prioritizing the 6 open chambers.
E. MODULAR + LIFTING: many more primes at SHORTER caps to find ONE
   lucky prime (GB runtime varies by prime), then CRT/lift evidence.
   Or trace-lifting strategies.
F. THEORY-FIRST PIVOT: park the system as compute-hard with named
   revisit conditions; redirect to rows 21+ (D25 probe), the Q2
   intersection (l12 3-chart), or algebraization (the germ is only
   meaningful if it algebraizes — maybe prove it CANNOT, killing
   residue-A without ever solving the system).
G. HYBRID: minimal big-iron burst (one u-6tb spot instance, 24h, the
   single most decisive lane) + theory-first in parallel.

Constraints: $5000/mo credit envelope (bulk available); the system is
THE decisive object for on-axis td=6; a wrong "park" call costs weeks.
My (Fable's) prior leans G (one decisive big-iron burst on the main
p105337 lane + F's algebraization lane in parallel) but I want your
independent ranking BEFORE seeing mine in detail. Deliverable:
xmodel/sol-instrument.md — ranked plan, cost table, kill criteria per
option, and your single concrete "do this today" pick. No repo
modifications except your output file. No git.
