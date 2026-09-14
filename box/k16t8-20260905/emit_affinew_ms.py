#!/usr/bin/env python3
"""Emit an msolve .ms export of the AFFINE half of Prop 7.1 at t=8:
   V(I2 + (W_1..W_7) + (b4-1))  in ring P = F_32003[b4,q2_0..q7_0], wp 1..7.
Reuses the charged prefix verbatim (cut at the evalpoint terminator); no polynomial is retyped.
Ring map declared: P -> msolve vars (q2,...,q7); b4 |-> 1 by subst, so b4 does not occur in the output.
"""
from pathlib import Path
HERE = Path(__file__).resolve().parent
TPL = HERE / "affinew_t8_mod_p32003_b0.sing"
MARK = "  return(wnz);\n}"
txt = TPL.read_text()
i = txt.find(MARK)
if i < 0:
    raise SystemExit("evalpoint terminator not found")
prefix = txt[: i + len(MARK)] + "\n"
lines = prefix.splitlines()
lines[0] = 'print("K16T8 affinewms_t8_mod_p32003_b0");'
prefix = "\n".join(lines) + "\n"

t = 8
outfile = str(HERE / "msolve_t8_affinew_p32003_b0.ms")
vs = ",".join(f"q{j}" for j in range(2, t))
L = [
    'print("AFFINEWMS export of I2+(W)+(b4-1) for msolve");',
    'print("AFFINEWMS ring="+string(basering));',
    "ideal Sys=subst(I2+Ws,b4,1);",
    'print("AFFINEWMS ngens="+string(size(Sys))+" (expect 28 = 21 minors + 7 W_r)");',
    # image check: b4 must be gone from every generator
    "int i; int b4seen=0;",
    "for (i=1;i<=size(Sys);i++) { if (deg(Sys[i],intvec(1,0,0,0,0,0,0))>0) { b4seen=1; } }",
    'print("AFFINEWMS B4_ELIMINATED="+string(b4seen==0));',
    # sanity: none of the 28 generators became 0 or a nonzero constant
    "int nz=0; int uni=0;",
    "for (i=1;i<=size(Sys);i++) { if (Sys[i]==0) { nz=nz+1; } if (Sys[i]!=0 && deg(Sys[i])==0) { uni=uni+1; } }",
    'print("AFFINEWMS ZERO_GENS="+string(nz)+" CONSTANT_GENS="+string(uni));',
    f'string vs="{vs}";',
    f'string fn="{outfile}";',
    'write(":w "+fn, vs);',
    'write(":a "+fn, string(char(basering)));',
    "string s;",
    "for (i=1;i<=size(Sys);i++) {",
    "  s=string(Sys[i]);",
]
for j in range(2, t):
    L.append(f'  while (find(s,"q{j}_0")>0) {{ s=s[1,find(s,"q{j}_0")-1]+"q{j}"+s[find(s,"q{j}_0")+{len(f"q{j}_0")},size(s)]; }}')
L += [
    '  if (i<size(Sys)) { s=s+","; }',
    '  write(":a "+fn, s);',
    "}",
    'print("AFFINEWMS_EXPORT_DONE ngens="+string(size(Sys)));',
    'print("JOB_DONE");',
    "quit;",
]
p = HERE / "affinewms_t8_mod_p32003_b0.sing"
p.write_text(prefix + "\n".join(L) + "\n")
print(p, "bytes", p.stat().st_size)
