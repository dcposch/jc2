# exactn-drivers-20260902

Driver directory of lane `exact-n-rigidity-opus5-20260902` (flagship EXACT-N;
successor of `OPEN[D1-SUBTREE]` and `OPEN[UPPER-TO-FLOOR]`).

* `dictionary.py` / `.log` — STEP 1 (LEMMA DICT, LEMMA SHIFT, THEOREM DICT-N).
  Newton-polygon reading of `{ord_t h(tau_i)}` for `h = f, g_y, [f,g]`; 9 Keller
  rows, the charged out-of-gauge row, 7 non-Keller NEGATIVE rows, the sum
  identity, the shifted-tree formula, a non-singleton frontier ball. 64 checks.
* `treestar.py` / `.log` — THEOREM D1-STAR on four explicit Keller pairs, the
  joint `f*g` tree read root-free from `Res_y(g(x,y), h(x,y+w))`. 28 checks.
* `noresidue.py` / `.log` — COROLLARY NO-RESIDUE, with a negative control. 4 checks.
* `exactn.py` — `Phi` controls (CONTROL P1–P4) + the two-sided/arithmetic filter.
  Imports the reviewed `box/moh_skeleton_N.py` unedited. FAIL-CLOSED.
  - `exactn140.log`   full run, FLOOR/CEILING/SINGLE/MIXED, `D <= 140`, 345 s.
  - `exactn-single200.log`  SINGLE only, reaches `D = 190` (stalls at `D = 192`).
  - `exactn100.log`, `exactn130.log`, `exactn200.log`, `exactn-mohsharp2.log` —
    superseded partial runs from earlier (slower) revisions; kept for custody.

Unreviewed lane code.  Reproduce:
    python3 box/exactn-drivers-20260902/dictionary.py
    python3 box/exactn-drivers-20260902/treestar.py
    python3 box/exactn-drivers-20260902/noresidue.py
    python3 box/exactn-drivers-20260902/exactn.py --control-nmax 100 --nmax 140 --exact
