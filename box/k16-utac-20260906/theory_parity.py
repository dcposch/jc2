import argparse,pathlib,subprocess,time,json
ap=argparse.ArgumentParser();ap.add_argument('m',type=int);ap.add_argument('--root',type=int);ap.add_argument('--prime',type=int,default=1000003);ap.add_argument('--timeout',type=int,default=180);a=ap.parse_args();m=a.m;pr=a.prime
val=(m*pow(3,-1,pr))%pr
if a.root is not None: root=a.root%pr; assert(root*root-val)%pr==0
else:
 root=pow(val,(pr+1)//4,pr);root=root if root*root%pr==val else None
field=f'({pr},d)' if root is None else str(pr)
alg=f'minpoly=d2-{m}/3;' if root is None else ''
d='d' if root is None else str(root)
vs=[f'l{j}' for j in range(2,m,2)]+['b'];weights=[m-j for j in range(2,m,2)]+[m]
L='-b+'+'+'.join(f'l{j}*x{j}' for j in range(2,m,2))+f'+x{m}'
base=pathlib.Path('box/k16-utac-20260906')/f'theory_parity_m{m}_p{pr}_d{d}'
script=f'''ring r={field},(x,{','.join(vs)}),(dp(1),wp({','.join(map(str,weights))}));
{alg}
proc cf(poly f,int k) {{ matrix c=coeffs(f,x); if(nrows(c)<k+1){{return(0);}} return(c[k+1,1]); }}
poly L={L};
poly G=3/2*L*(L+b);
poly R0=3/16*L^3*(L+2*b);
number dd={d}; number pp=1/(4*(2*dd+1));
poly P=pp*x{2*m};
poly F;
number pivot;
int j;
for(j={4*m-2};j>={2*m};j=j-2) {{ F=x*diff(P^2,x)-3*P^2+G*P-R0; pivot=2*pp*(j-3)+3/2; P=P-cf(F,j)/pivot*x^(j-{2*m}); }}
poly eta=cf(P,2);
poly R=R0-eta*x2*b*L/2;
F=x*diff(P^2,x)-3*P^2+G*P-R;
ideal J=cf(P,0)+b2/4;
for(j=0;j<={4*m};j++){{ if(cf(F,j)!=0){{J[size(J)+1]=cf(F,j);}} }}
print("BUILT");print(size(J));
ring S={field},({','.join(vs)}),wp({','.join(map(str,weights))});
{alg}
ideal J=imap(r,J);poly eta=imap(r,eta);option(redSB);
ideal H=std(J);
print("GB_DONE");print(size(H));print(dim(H));print(vdim(H));
poly z=1;int e;for(e=1;e<=100;e++){{z=reduce(z*eta,H);if(z==0){{print("ETA_EXP");print(e);break;}}}}
z=1;for(e=1;e<=100;e++){{z=reduce(z*b,H);if(z==0){{print("B_EXP");print(e);break;}}}}
print("DONE");quit;
'''
base.with_suffix('.sing').write_text(script)
t=time.time()
with base.with_suffix('.out').open('w') as f:
 try:
  p=subprocess.run(['Singular','-q',str(base.with_suffix('.sing'))],stdout=f,stderr=subprocess.STDOUT,timeout=a.timeout)
  status='complete';code=p.returncode
 except subprocess.TimeoutExpired:status='timeout';code=None
result={'m':m,'field':field,'d':d,'status':status,'returncode':code,'elapsed':time.time()-t,'output':base.with_suffix('.out').read_text()}
base.with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
