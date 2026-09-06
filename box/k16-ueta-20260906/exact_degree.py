import argparse
import pathlib

ap = argparse.ArgumentParser()
ap.add_argument('m', type=int)
ap.add_argument('--branch', type=int)
ap.add_argument('--boundary', action='store_true')
ap.add_argument('--slim', action='store_true')
a = ap.parse_args()
m = a.m
vs = [f'l{j}' for j in range(2, m)]
variables = ','.join(vs + ['b'])
weights = ','.join(map(str, list(range(m-2, 0, -1)) + [m]))
coeff = '(0,d)' if a.branch is None else '0'
dinit = f'minpoly=3*d^2-{m};' if a.branch is None else f'number d={a.branch};'
L = '-b+' + '+'.join([f'l{j}*x^{j}' for j in range(2, m)] + [f'x^{m}'])
s = f'''ring big={coeff},(x,{variables},B,eta),dp;
{dinit}
proc cx(poly ff,int jj) {{ return(subst(ff/(x^jj),x,0)); }}
proc uf(poly PP,poly LL,poly BB,poly ee) {{return(2*x*PP*diff(PP,x)-3*PP^2+(3/2*LL*(LL+b)-BB*x)*PP-3/16*LL^2*(LL*(LL+2*b)-4*BB*x)+ee*x^2*(b*LL/2+BB*x));}}
int m={m}; poly L={L}; number p=1/(4*(2*d+1));
poly P=p*x^(2*m); poly f; poly v; number Aj; int j;
for(j=2*m-1;j>=2;j--) {{
 Aj=2*(2*m+j-3)*p+3/2;
 if(Aj==0){{ERROR("ZERO_HIGH_PIVOT");}}
 f=uf(P,L,0,0); v=-cx(f,2*m+j)/Aj; P=P+v*x^j;
}}
poly etam=cx(P,2); P=P-B*x-(1/4)*b^2;
f=uf(P,L,B,etam); poly brow=cx(f,2*m+1);
number bp=-((4*m-3)*p+3/4);
poly bcheck=subst(brow,B,1)-subst(brow,B,0)-bp;
if(bcheck!=0){{ERROR("BAD_B_PIVOT");}}
poly Bm=-subst(brow,B,0)/bp; P=subst(P,B,Bm);
f=uf(P,L,Bm,etam);
int check=1;
for(j=0;j<=3;j++){{if(cx(f,j)!=0){{check=0;}}}}
for(j=2*m+1;j<=4*m;j++){{if(cx(f,j)!=0){{check=0;}}}}
print("ALL_UNUSED_ROWS_ZERO="+string(check));
if(check==0){{quit;}}
ideal K;
for(j=4;j<=2*m;j++){{K=K,cx(f,j);}}
K=simplify(K,2);
print("ROW_COUNT="+string(size(K)));
ring small={coeff},({variables}),wp({weights});
{dinit}
ideal K=imap(big,K); poly em=imap(big,etam); poly bm=imap(big,Bm);
'''
if a.boundary:
    s += 'K=subst(K,b,0);\n'
s += 'option(redSB);\nprint("STD_START");\n'
s += ('ideal G=slimgb(K);' if a.slim else 'ideal G=std(K);') + '\n'
s += 'print("STD_DONE");print("BASIS_SIZE="+string(size(G)));print("DIM="+string(dim(G)));\n'
s += 'int e;for(e=1;e<=20;e++){if(reduce(b^e,G)==0){print("B_POWER="+string(e));break;}}\n'
s += 'for(e=1;e<=12;e++){if(reduce((bm*em)^e,G)==0){print("BETA_POWER="+string(e));break;}}\n'
s += 'print("ETA_ZERO="+string(reduce(em,G)==0));quit;\n'
name = f'exact_m{m}' + ('' if a.branch is None else f'_d{a.branch}') + ('_boundary' if a.boundary else '') + ('_slim' if a.slim else '')
p = pathlib.Path(__file__).parent / (name + '.sing')
p.write_text(s)
print(p)
