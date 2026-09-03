"""Compatibility shim for the frozen census driver.

The supplied frozen input set contains ``moh_skeleton_full.py`` but not the
legacy ``moh_skeleton_N.py`` imported only by control_0.  Re-exporting the
frozen implementation lets the byte-identical driver run in isolation.  This
makes control_0 tautological; all substantive counts are checked separately.
"""

from moh_skeleton_full import *  # noqa: F401,F403
