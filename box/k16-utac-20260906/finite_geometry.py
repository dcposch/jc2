#!/usr/bin/env python3
"""Closing-only polynomial solution strata. No ray data or certificates read.
Generate Singular scripts from UF; compact transcripts and JSON only.
"""
import argparse, json, pathlib, subprocess, time
ROOT=pathlib.Path(__file__).resolve().parent

def script(n, field='0', branch=None, homogeneous=True):
    alg=branch is None
    fld=f'({field},d)' if alg else field
    extension=f'minpoly=3*d^2-{n};' if alg else ''
    p='1/(4*(2*d+1))' if alg else f'number(1)/(4*(2*({branch})+1))'
    lv=[f'l({i})' for i in range(2,n)]
    rv=['x']+lv+['B']+(['b'] if homogeneous else [])
    sv=lv+(['b'] if homogeneous else [])
    if not sv: sv=['dummy']
    weights=list(range(n-2,0,-1))+([n] if homogeneous else [])
    order='wp('+','.join(map(str,weights))+')' if homogeneous else 'dp'
    mp=['0']+lv+['0']+(['b'] if homogeneous else [])
    b='b' if homogeneous else '1'
    end='''
proc mine(ideal H,poly f){int e;for(e=1;e<=30;e++){if(reduce(f^e,H)==0){return(e);}}return(0);}
print("MIN_B_POWER="+string(mine(GJ,b)));
''' if homogeneous else 'GJ;'
    return f'''// Generated independently from frozen UF, normalized actual leading coefficient l_N=1.
int N={n};
ring R={fld},({','.join(rv)}),dp;
{extension}
proc xc(poly f,int k){{matrix mm=coef(f,x);int ii;for(ii=1;ii<=ncols(mm);ii++){{if(deg(mm[1,ii])==k){{return(mm[2,ii]);}}}}return(poly(0));}}
poly L=-{b}+x^N;int j;
''' + ''.join(f'L=L+l({i})*x^{i};\n' for i in range(2,n))+f'''
number p={p};
poly G=3*L*(L+{b})/2-B*x;
poly RF0=3*(L^2)*(L*(L+2*{b})-4*B*x)/16;
poly P=p*x^(2*N);poly residual;poly pj;number pivot;
for(j=2*N-1;j>=2;j--){{
 residual=x*diff(P^2,x)-3*(P^2)+G*P-RF0;
 pivot=2*(2*N+j-3)*p+number(3)/2;
 if(pivot==0){{print("ERROR_ZERO_PIVOT");quit;}}
 pj=-xc(residual,2*N+j)/pivot;P=P+pj*x^j;
}}
poly eta=xc(P,2);
P=P-B*x-number(1)*({b}^2)/4;
poly RF=RF0-eta*x^2*({b}*L/2+B*x);
residual=x*diff(P^2,x)-3*(P^2)+G*P-RF;
poly Brow=xc(residual,2*N+1);
poly Bd=diff(Brow,B);
number Bpivot=-((4*N-3)*p+number(3)/4);
print("B_PIVOT_CHECK="+string(Bd==Bpivot));
poly Bsol=-subst(Brow,B,0)/Bpivot;
P=subst(P,B,Bsol);eta=subst(eta,B,Bsol);
G=subst(G,B,Bsol);RF=subst(RF,B,Bsol);
residual=x*diff(P^2,x)-3*(P^2)+G*P-RF;
int highok=1;int lowok=1;
for(j=2*N+1;j<=4*N;j++){{if(xc(residual,j)!=0){{highok=0;}}}}
for(j=0;j<=3;j++){{if(xc(residual,j)!=0){{lowok=0;}}}}
print("HIGH_ROWS_ZERO="+string(highok));print("LOW_ROWS_ZERO="+string(lowok));
ideal J;for(j=4;j<=2*N;j++){{J[j-3]=xc(residual,j);}}
''' + ('''print("CUBIC_B_ON_L2_ZERO="+string(subst(Bsol,l(2),0)));
print("CUBIC_ETA_ON_L2_ZERO="+string(subst(eta,l(2),0)));
print("CUBIC_P_FAMILY_CHECK="+string(subst(P+(L^2)/4,l(2),0)==0));
''' if n==3 and branch==-1 else '') + f'''
ring S={fld},({','.join(sv)}),{order};{extension}
map phi=R,{','.join(mp)};
ideal J=phi(J);
print("N="+string(N)+" J_SIZE="+string(size(J)));
option(redSB);ideal GJ=std(J);
print("GB_SIZE="+string(size(GJ)));print("DIM="+string(dim(GJ)));
{end}
print("DONE");quit;
'''

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,required=True)
    ap.add_argument('--field',default='0');ap.add_argument('--branch',type=int)
    ap.add_argument('--normalized-b',action='store_true');ap.add_argument('--timeout',type=int,default=600)
    a=ap.parse_args(); label=f'finite_m{a.n}_'+('Q' if a.field=='0' else f'F{a.field}')+(f'_d{a.branch}' if a.branch is not None else '')+('_b1' if a.normalized_b else '_hom')
    path=ROOT/(label+'.sing');path.write_text(script(a.n,a.field,a.branch,not a.normalized_b))
    started=time.monotonic()
    try:
        proc=subprocess.run(['Singular','-q',str(path)],capture_output=True,text=True,timeout=a.timeout)
        out=proc.stdout+proc.stderr;status='PASS' if proc.returncode==0 and 'DONE' in out and '?' not in out and 'ERROR' not in out and all(z in out for z in ['B_PIVOT_CHECK=1','HIGH_ROWS_ZERO=1','LOW_ROWS_ZERO=1']) else 'FAIL'
    except subprocess.TimeoutExpired as e:
        out=(e.stdout or b'').decode() if isinstance(e.stdout,bytes) else (e.stdout or '')
        status='TIMEOUT'
    elapsed=time.monotonic()-started;(ROOT/(label+'.out')).write_text(out)
    data={'N':a.n,'field':a.field,'branch':a.branch,'homogeneous_b':not a.normalized_b,'status':status,'seconds':round(elapsed,3),'output':out,'script':str(path.relative_to(ROOT))}
    (ROOT/(label+'.json')).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
if __name__=='__main__':main()
