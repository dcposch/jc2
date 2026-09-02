# raykill-cells-20260902 — preserved drivers + logs of the RAY-KILL lane's cell decisions

Provenance: verbatim copy (2026-09-02, coordinator Fable 5.1) of
`/tmp/raykill`, the working directory the Opus 5 lane
`ray-kill-opus5-20260902` left behind ("Drivers left in /tmp/raykill,
not installed in box/", its Sec 7 DEVIATIONS (4)). Unreviewed lane code.
`cell.py` builds the A2-E1WALL cell system (e,U) of ray-kill Sec 3.7 /
Sec 4.1 (a = b = eta_e = 1, s_sigma NOT normalised, saturation variable);
`cellp.py` adds the five PROVED pins (wall, ray, RAY-1/RAY-2).

Results found in the logs at preservation time (sympy 1.14 exact Groebner
over Q, grevlex, unit ideal = EMPTY):

- `cells.log`   : full system  (1,5) EMPTY 89.6 s;  (2,6) EMPTY 25.3 s
                  ((2,6) is the boundary slice U = 3e, e = 2 — a CAS
                  control of THEOREM RAY-EDGE).
- `cellsP.log`  : primed system (1,5) EMPTY 2510.1 s.
- `controls.log`: (1,3) negative/dropped-equation controls (lane Sec 3.7).

Two sympy processes from these queues were still running on the Mac at
100% CPU for 2h40m (queue on cells2.log stuck on a later cell; the primed
queue past (1,5)) and were KILLED by the coordinator at ~07:30Z under the
FLEET hard rule (no heavy CAS on the Mac). box01's msolve/qqideal window
covers those cells.

Certainty reading: (1,5) now has a Q-exact engine (this sympy run, two
independent runs) PLUS the box01 msolve/qqideal engine (mod-65521 PROVEN,
char-0 MODULAR) — the same two-engine-with-Q-exact-side configuration
under which (1,3) was typed PROMOTION-GRADE. Unsealed lane output;
recorded as coordinator-observed evidence with the code preserved here.
