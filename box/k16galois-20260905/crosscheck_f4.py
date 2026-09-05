#!/usr/bin/env python3
"""If the exact point polynomial f_4 (minpoly_exactchart_t4_exact_q2_0.txt, over (0,yy) with minpoly H_4) exists,
reduce it modulo each prime ideal used in the t=4 sweep and compare with the modular minimal polynomial m̄
(minpoly_pattern_t4_mod_p{p}_b{b}_q2_0.txt).  Prints EQUAL/DIFFER per prime ideal."""
import pathlib, re, subprocess, glob
f4 = pathlib.Path('minpoly_exactchart_t4_exact_q2_0.txt')
if not f4.exists(): print("no exact f_4 yet"); raise SystemExit
fx = f4.read_text().strip()
q=9; H=f"{12*q*q}*yy^2-{12*q*5}*yy+{5*14}"
def roots(p): return sorted(r for r in range(p) if (12*q*q*r*r-12*q*5*r+5*14)%p==0)
out=[]
for m in sorted(glob.glob('minpoly_pattern_t4_mod_p*_b*_q2_0.txt')):
    mm=re.search(r"p(\d+)_b(\d)",m); p=int(mm.group(1)); b=int(mm.group(2)); r=roots(p)[b]
    mod=pathlib.Path(m).read_text().strip()
    script=f"""ring E=(0,yy),(q2_0),dp; minpoly={H}; poly f={fx};
ring M=({p}),(q2_0),dp; number yy={r}; poly fbar=imap(E,f); poly mbar={mod};
fbar=fbar/leadcoef(fbar); mbar=mbar/leadcoef(mbar);
if (fbar-mbar==0) {{ print("EQUAL p={p} b={b}"); }} else {{ print("DIFFER p={p} b={b}"); }}
quit;"""
    r_=subprocess.run(['Singular','-q'],input=script,capture_output=True,text=True,timeout=600)
    out.append((r_.stdout.strip(), r_.stderr.strip()[:100]))
    print(out[-1][0], out[-1][1])
