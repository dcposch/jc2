#!/usr/bin/env python3
from pathlib import Path
import meanfree_stage_v2 as M
D=Path(__file__).resolve().parent/'selected'/'meanfree_jet0_stage8_slimgb'
D.mkdir(parents=True,exist_ok=True)
M.OUT=D
M.main(8,False)
