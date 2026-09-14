#!/usr/bin/env python3
"""Prepare strongest mean-free chart in isolated artifact custody."""
from pathlib import Path
import meanfree_stage as M
D=Path(__file__).resolve().parent/'selected'/'meanfree_stage8_slimgb'
D.mkdir(parents=True,exist_ok=True)
M.OUT=D
M.main(8)
