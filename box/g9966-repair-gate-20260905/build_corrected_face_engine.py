#!/usr/bin/env python3
"""Generate a local diagnostic engine; originals are read-only."""
import ast
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

here=Path(__file__).resolve().parent
source=here.parent/'g9966-d2-precise-20260905/band_engine.py'
original=source.read_text()
text=original
text=text.replace('RECEIPT = HERE / "receipt.run.v2"', 'RECEIPT = ROOT / "box/g9966-d2-precise-20260905/receipt.run.v2"')
text=text.replace('FROZEN = HERE / "frozen"', 'FROZEN = ROOT / "box/g9966-d2-precise-20260905/frozen"')
old_doc=ast.get_docstring(ast.parse(text),clean=False)
new_doc='''Diagnostic (99,66) repair allowing the two h3 equality-face coefficients.

The source h3 strict-floor restriction is replaced by weight >=32, with
the t4*z5 coefficient fixed to -8/3 by the h2 face and t8*z2 initially free.
The old strict-support basis is retained and these two pure face terms added.
Both branch minor leaders are re-solved exactly with jet0 and Hc_11_0 free.
This diagnostic does not establish necessity of every imported chart block.
In particular the delta2 double-root coordinate remains at zeta=0.
No original input is modified; provenance and exact diff accompany this file.
'''
text=text.replace(old_doc,new_doc,1)
tree=ast.parse(text)
fn=next(node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='h3_branch_map')
maps=json.loads((here/'face-minor-probe.json').read_text())
replacement=['def h3_branch_map(branch: str) -> tuple[dict[sp.Symbol, sp.Expr], list[sp.Symbol], dict]:',
             '    """Exact minor-leader solution after correcting the h3 D2 equality face."""']
for i,branch in enumerate(('delta2','delta52')):
    result=maps[branch]
    replacement += [f'    {"if" if i==0 else "elif"} branch == {branch!r}:',f'        encoded = {result["mapping"]!r}',
      f'        free_names = {result["free_h_coefficients"] + (["jet0","rho","u"] if branch=="delta2" else ["jet0","u","v","c"])!r}',
      f'        localizer = {"rho" if branch=="delta2" else "c"!r}']
replacement += ['    else:', '        raise ValueError(branch)',
 '    substitutions = {symbol(name):sp.sympify(rhs) for name,rhs in encoded.items()}',
 '    free = list(map(symbol,free_names))',
 '    centre = {"parameters":free_names,"localization":localizer+"!=0",',
 '              "minor_constant":"free","Hc_11_0":"free",',
 '              "h3_face":"pi^8-(8/3)*pi^5+E82*pi^2",',
 '              "E82":"solved in terms of retained Hc_8_3 and other free coefficients",',
 '              "scope":"diagnostic corrected h3 equality face, no full necessity assertion"}',
 '    return substitutions,free,centre']
lines=text.splitlines(keepends=True)
text=''.join(lines[:fn.lineno-1])+'\n'.join(replacement)+'\n'+''.join(lines[fn.end_lineno:])
needle='    assert len(variables) == 21\n    return {key: sp.expand(value) for key, value in out.items()}, variables'
assert text.count(needle)==1
text=text.replace(needle,'''    assert len(variables) == 21
    out[(4,5)] = out.get((4,5),0) - sp.Rational(8,3)
    out[(8,2)] = out.get((8,2),0) + symbol("E82")
    variables.append(symbol("E82"))
    assert len(variables) == 22
    return {key: sp.expand(value) for key, value in out.items()}, variables''')
text=text.replace('expected=105 if branch=="delta2" else 103','expected=106 if branch=="delta2" else 105')
text=text.replace('"ODE_compatibility":"Hc_11_0=0 retained"','"Hc_11_0":"free; no ODE compatibility imposed"')
text=text.replace('"delta52_Hc_11_0_retained":localized==symbol("c")','"Hc_11_0_free":True')
text=text.replace('"delta52_Hc_11_0":"fixed_zero_retained"','"delta52_Hc_11_0":"free"')
text=text.replace('"new_free_dimensions":1','"h3_equality_face_correction":True,\n            "new_free_dimensions_over_pristine":2 if branch=="delta2" else 3')
output=here/'corrected_face_engine.py'
output.write_text(text)
(here/'corrected_face_engine.patch').write_text(''.join(difflib.unified_diff(original.splitlines(keepends=True),text.splitlines(keepends=True),fromfile=str(source),tofile=str(output))))
compile(text,str(output),'exec')
spec=importlib.util.spec_from_file_location('corrected_face_control',output)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
controls={}
for branch in ('delta2','delta52'):
    k2,free,meta=m.build_major_h2(branch,8)
    controls[branch]={'k2_slots':len(k2),'inner_free':len(free),'minor_control':meta['h3_control'],'h3_free':meta['h3_free']}
record={
 'status':'PASS','source_sha256':hashlib.sha256(original.encode()).hexdigest(),
 'corrected_engine_sha256':hashlib.sha256(text.encode()).hexdigest(),
 'controls':controls,'custody':m.verify_inputs(),'pristine_pin':m.charged_driver_control(),
 'scope':'DIAGNOSTIC corrected equality-face chart; delta2 at-level double-root shift not yet freed.'}
(here/'corrected-face-controls.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
