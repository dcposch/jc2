import sys, io, contextlib
sys.path.insert(0, "box")
import moh_skeleton_N as M
# operative test with the campaign's N_min = 6 (N<=5 closed 2026-09-02T01:10Z)
M.fast_filter(400, nmin_geom=(6, 6))
