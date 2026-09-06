#!/usr/bin/env python3
"""Exact small-polynomial controls for normalized actual degrees two and three.
The polynomials are the row numerators emitted in finite_m3_Q_d1_b1_rows.out.
"""
import json
from pathlib import Path
import sympy as s
z=s.symbols('z')
f=1986398181*z**2-16122815232*z-3806398081024
g=48281373*z**2-392411136*z-49433741312
out={'m3_plus_row5_after_removing_nonzero_h_factor':str(f),'m3_plus_row6':str(g),'resultant':str(s.resultant(f,g,z)),'gcd':str(s.gcd(f,g)),'m3_minus_inconsistent_cross_products':[775*59,1375*34],'all_pass':s.gcd(f,g)==1 and 775*59!=1375*34}
p=Path(__file__).resolve().parent/'finite_low_resultant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
