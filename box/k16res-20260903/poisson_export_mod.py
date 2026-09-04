#!/usr/bin/env python3
"""Emit a modular job exporting the multiplication matrix of R_s|_{b4=1} on B = A[q]/(R_r|_{b4=1}, r != s), and compute its det mod p in numpy."""
import sys
sys.path.insert(0,'.')
import emit_jobs as E
def job(t,p,root,s,tag):
    L,vs,ws=E.header("W",t,"mod",p,root); L+=E.PROCS.splitlines(); E.load_R(t,L)
    L+=["ideal RR1=subst(RR,b4,1);"]
    vsa=E.qvars(t)
    L+=[f"ring WA={p},({','.join(vsa)}),dp; number yy={root}; option(redSB);",
        f"ideal RA=imap(W,RR1); int tt={t}; int r; int c=0; ideal SA;",
        f"for (r=1;r<=tt-1;r++){{ if (r!={s}) {{ c++; SA[c]=RA[r]; }} }}",
        "int tm=timer; ideal GA=std(SA); print(\"B dim=\"+string(dim(GA))+\" vdim=\"+string(vdim(GA))+\" time=\"+string(timer-tm));",
        "ideal KA=kbase(GA); int nb=size(KA); int i; int j; ideal Img;",
        f"for (i=1;i<=nb;i++){{ Img[i]=reduce(RA[{s}]*KA[i],GA); }}",
        "matrix MA=coeffs(Img,KA); string sline;",
        f'write(":w {E.HERE}/{tag}_matrix.txt", "NB="+string(nb));',
        f'for (i=1;i<=nb;i++){{ sline=""; for (j=1;j<=nb;j++){{ sline=sline+string(MA[i,j])+","; }} write(":a {E.HERE}/{tag}_matrix.txt", sline); }}',
        'print("EXPORT_DONE"); quit;']
    return "\n".join(L)+"\n"
if __name__=="__main__":
    t,p,root,s=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
    tag=f"t{t}_poisson_s{s}_mod_p{p}_r{root}"
    open(tag+".sing","w").write(job(t,p,root,s,tag)); print(tag)
