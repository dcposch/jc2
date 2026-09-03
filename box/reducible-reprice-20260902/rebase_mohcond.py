#!/usr/bin/env python3
"""REBASE of the N_min sweep onto the census filtered by Moh's own search conditions,
   per box/tfcal-drivers-20260902/mohcond.py (sibling lane time-function-calibration-d48).
     STAR      star_congruence: a_1 = e V_2 == 0 or 1 (mod Delta_1).  Fully proved there.
     MOHALL    moh_all = (10) for j = 2..s-1 AND star_congruence.  (10) is an OCR
               reconstruction with the alpha = 0 branch (11) missing, so its kills are
               a CEILING.
   Kill percentages are recomputed over the reduced base, so they are comparable only
   within a column."""
import sys, os, time
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE,'..','tfcal-drivers-20260902'))
sys.path.insert(0, os.path.join(HERE,'..'))
sys.path.insert(0, os.path.join(HERE,'..','d1sub-drivers-20260902'))
from moh_skeleton_N import Skel, census
from mohcond import star_congruence, moh_all
from d1floor import qval, achievable

WIN=[(2,None),(4,None),(6,None),(4,16),(6,16)]
def run(nmax=120, nmin=48, gate=None, label=""):
    tot={w:dict(a=0,k=0,g=0,kg=0) for w in WIN}; rows={}
    for n in range(nmin,nmax+1):
        na=0; kill={w:0 for w in WIN}; grp={}
        for (m,Ms,V) in census(n):
            S=Skel(n,m,list(Ms),V)
            if not S.windows_ok(): continue
            if gate is not None and not gate(S): continue
            na+=1; allv=achievable(S); key=(m,Ms,S.V[S.s])
            g=grp.setdefault(key,{w:False for w in WIN})
            for (lo,hi) in WIN:
                if [x for x in allv if x>=lo and (hi is None or x<=hi)]: g[(lo,hi)]=True
                else: kill[(lo,hi)]+=1
        if not na: continue
        rows[n]=(na,len(grp),{w:sum(1 for k in grp if not grp[k][w]) for w in WIN})
        for w in WIN:
            tot[w]['a']+=na; tot[w]['k']+=kill[w]; tot[w]['g']+=len(grp); tot[w]['kg']+=rows[n][2][w]
    print("\n== %s : D in [%d,%d] ==" % (label,nmin,nmax))
    print("   %-11s %9s %9s %8s %8s %8s %8s" % ("window","assign","kill","%","groups","grpkill","%"))
    for (lo,hi) in WIN:
        T=tot[(lo,hi)]; lab="N>=%d"%lo+("" if hi is None else " <=%d"%hi)
        print("   %-11s %9d %9d %7.2f%% %8d %8d %7.2f%%" %
              (lab,T['a'],T['k'],100.0*T['k']/max(1,T['a']),T['g'],T['kg'],
               100.0*T['kg']/max(1,T['g'])))
    dead={w:[n for n in rows if rows[n][2][w]==rows[n][1]] for w in WIN}
    print("   degrees with EVERY surviving group killed:")
    for (lo,hi) in WIN:
        lab="N>=%d"%lo+("" if hi is None else " <=%d"%hi)
        print("     %-11s %s" % (lab, dead[(lo,hi)] if dead[(lo,hi)] else "NONE"))
    print("   per-degree (MOH-SHARP-2 degrees) groups / N>=6 kills:",
          ", ".join("%d: %d/%d" % (n, rows[n][1], rows[n][2][(6,None)])
                    for n in (105,108,112,117,120) if n in rows))
    return rows

if __name__=="__main__":
    t0=time.time()
    run(120,48,star_congruence,"STAR-CONGRUENCE gate (fully proved)")
    run(120,48,moh_all,"MOH_ALL gate (10)+star  [kills are a CEILING]")
    print("\nwall %.1f s" % (time.time()-t0))
