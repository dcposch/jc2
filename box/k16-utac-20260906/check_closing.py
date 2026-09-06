#!/usr/bin/env python3
"""Emit a direct, compact presentation of the closing ideal; no ray inputs.

After computing P only through 2N, the residual rows 2N+1..4N generate
the same ideal as Phi_2N+1..Phi_4N by the unit triangular recursion.
"""
from pathlib import Path
import argparse

a = argparse.ArgumentParser()
a.add_argument('N', type=int)
a.add_argument('--prime', type=int, default=1000003)
a.add_argument('--max-exponent', type=int, default=45)
a.add_argument('--order', choices=['dp', 'wp'], default='wp')
args = a.parse_args()
n = args.N
weights = [2, 1, 3] + list(range(2, n+1))
order = 'dp' if args.order == 'dp' else 'wp('+','.join(map(str,weights))+')'
out = Path(__file__).parent / f'check_closing_N{n}_p{args.prime}_{args.order}.sing'
src = f'''// Independently emitted from frozen UF formula. N={n}; coefficient field GF({args.prime}).
int N={n};
ring R={args.prime},(x,u,B,w2,l(2..N)),dp;
proc xc(poly f,int k){{matrix m=coef(f,x);int i;
 for(i=1;i<=ncols(m);i++){{if(deg(m[1,i])==k){{return(m[2,i]);}}}} return(poly(0));}}
poly eta=(u-3*l(2))/4;
poly L=-1; int j;
for(j=2;j<=N;j++){{L=L+l(j)*x^j;}}
poly G=3*L*(L+1)/2-B*x;
poly RF=3*L^2*(L*(L+2)-4*B*x)/16-eta*x^2*(L/2+B*x);
poly P=-1/4-B*x+eta*x^2+w2*x^3;
poly Ex,Pk; int k; list Phi;
for(k=4;k<=2*N;k++){{Ex=x*diff(P^2,x)-3*P^2+G*P-RF;
 Pk=2*xc(Ex,k)/(k-3); Phi[k]=Pk; P=P+Pk*x^k;}}
poly c4=2*(eta^2)-6*B*w2-2*eta*l(2)-3*(l(2)^2)/4;
print("CTRL_PHI4="+string(Phi[4]==c4));
print("CTRL_PHI5="+string(Phi[5]==30*B^2*w2-10*B*eta^2+10*B*eta*l(2)+3*B*l(2)^2+4*eta*w2-eta*l(3)-3*l(2)*w2/2-3*l(2)*l(3)/4));
Ex=x*diff(P^2,x)-3*P^2+G*P-RF;
int bad=0; for(k=0;k<=2*N;k++){{if(xc(Ex,k)!=0){{bad++;}}}}
print("CTRL_LOW_ROWS_BAD="+string(bad));
ideal Icl;
for(k=2*N+1;k<=4*N;k++){{Icl[k-2*N]=xc(Ex,k);}}
ring S={args.prime},(u,B,w2,l(2..N)),{order};
map ph=R,0,u,B,w2,l(2..N); ideal Icl=ph(Icl);
poly eta=(u-3*l(2))/4;
option(redSB);
print("START_GB N="+string(N)+" field="+string(char(basering)));
ideal Gi=std(Icl);
print("GB_SIZE="+string(size(Gi))+" DIM="+string(dim(Gi)));
proc mine(ideal gg,poly f,string nm,int bound){{int e;poly nf=1;
 for(e=1;e<=bound;e++){{nf=reduce(nf*f,gg);if(nf==0){{print("MIN_EXP "+nm+"="+string(e));return(e);}}}}
 print("NO_POWER_UP_TO "+nm+"="+string(bound));return(0);}}
int z1=mine(Gi,u,"u",{args.max_exponent});
int z2=mine(Gi,l(2),"l2",{args.max_exponent});
int z3=mine(Gi,eta,"eta",{args.max_exponent});
int z4=mine(Gi,B*eta,"Beta",{args.max_exponent});
int z5=mine(Gi,B,"B",{args.max_exponent});
int z6=mine(Gi,w2,"w2",{args.max_exponent});
print("DONE_CLOSING_CHECK");quit;
'''
out.write_text(src)
print(out)
