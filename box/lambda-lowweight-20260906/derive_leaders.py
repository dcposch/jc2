#!/usr/bin/env python3
"""Exact-Q canonical h-adic T2 leader lifts; inputs are metadata and frozen roster."""
import json,pathlib,subprocess,time,sys,gzip,hashlib
OUT=pathlib.Path('box/lambda-lowweight-20260906')
cases=[]
for p in pathlib.Path('box/gi-only-20260905/classes').glob('*/class.json'):
 d=json.loads(p.read_text()); K=d['K'];n=d['e']*K;m=d['q']*K; M2=d['M_prime'][0]
 cases.append(dict(id=d['class_id'],K=K,e=d['e'],q=d['q'],n=n,m=m,M2=M2,unknowns=d['unknowns_without_T'],ell=d['ell']))
cases.sort(key=lambda d:d['unknowns'])
for line in pathlib.Path('/tmp/jc2-lane.IZAvbL/inputs/roster.jsonl').read_text().splitlines()[:4]:
 d=json.loads(line);r=d['receiver_chart'];o=d['own_child'];cases.append(dict(id=d['row_id'],K=r['K'],e=r['e'],q=r['q'],n=o['n_prime'],m=o['m_prime'],M2=o['M_prime'][1],unknowns=r['unknowns_without_T'],ell=o['ell']))
proc=r'''
proc ha(poly f,int L,int J,int a)
{
 matrix R[1][L+1];
 int ii,jj;
 matrix C=coef(f,hh);
 for(ii=1;ii<=ncols(C);ii++)
 { jj=deg(C[1,ii],WH)+1; R[1,jj]=R[1,jj]+C[2,ii]; }
 list dv;
 for(ii=1;ii<=L+1;ii++)
 {
  if(R[1,ii]!=0)
  {
   dv=division(R[1,ii],ideal(h));
   if(dv[3][1,1]!=1){ print("DIVISION_ERROR"); quit; }
   if(ii>=J+1){R[1,ii]=dv[2][1];}else{R[1,ii]=0;}
   if(ii<L+1){R[1,ii+1]=R[1,ii+1]+dv[1][1,1];}
   else {if(dv[1][1,1]!=0){print("CARRY_ERROR");quit;}}
  }
 }
 matrix CY;poly keep;
 CY=coef(R[1,J+1],y);keep=0;
 for(ii=1;ii<=ncols(CY);ii++){if(deg(CY[1,ii],WY)>=a){keep=keep+CY[1,ii]*CY[2,ii];}}
 R[1,J+1]=keep;
 return(R);
}
proc yc(poly f,int a)
{
 matrix C=coef(f,y);int i;
 for(i=1;i<=ncols(C);i++) {if(deg(C[1,i],WY)==a){return(C[2,i]);}}
 return(poly(0));
}
'''
allres=json.loads((OUT/'leaders.json').read_text()) if (OUT/'leaders.json').exists() else []
for d in cases:
 if len(sys.argv)>1 and d['id'] not in sys.argv[1:]:continue
 K,e,q=d['K'],d['e'],d['q'];L=e*q*K;D=(e-1)*d['m']-d['M2'];W=L-D;J,a=divmod(D,K)
 names=[f'h_0_{a}' for a in range(K-1,-1,-1)]
 blocks={}
 for z,maxi,start in [('A',e,1),('B',q,2)]:
  for i in range(start,maxi+1):
   vals=list(range(K-1,-1,-1))
   if i==maxi:vals.remove(0)
   vn=[f'{z}{i}_0_{a}' for a in vals];names+=vn
   blocks[f'{z}{i}']='+'.join(f'{v}*y^{a}' for v,a in zip(vn,vals))
 lines=[f'ring R=0,(y,hh,{",".join(names)}),(lp(1),dp({len(names)+1}));','option(redSB);',f'intvec WY=1,{",".join("0" for _ in range(len(names)+1))};',f'intvec WH=0,1,{",".join("0" for _ in names)};',f'poly h=y^{K}+'+'+'.join(f'h_0_{a}*y^{a}' for a in range(K-1,-1,-1))+';']
 for bn,expr in blocks.items():lines.append(f'poly {bn}={expr};')
 lines += [f'poly P=hh^{e}+'+'+'.join(f'A{i}*hh^{e-i}' for i in range(1,e+1))+';',f'poly Q=hh^{q}+'+'+'.join(f'B{i}*hh^{q-i}' for i in range(2,q+1))+';',proc,f'matrix H=ha(Q^{e}-P^{q},{e*q},{J},{a});','matrix F;poly gam;int jj;']
 mon=[]
 for aa in range(q):
  for bb in range(e):
   rr=aa*e+bb*q
   if D<rr*K<L:mon.append((rr,aa,bb))
 assert len({r for r,_,_ in mon})==len(mon)
 for rr,aa,bb in sorted(mon,reverse=True):
  lines += [f'gam=-yc(H[1,{rr+1}],0);',f'F=ha(P^{aa}*Q^{bb},{e*q},{J},{a});',f'for(jj=1;jj<={e*q+1};jj++){{H[1,jj]=H[1,jj]+gam*F[1,jj];}}',f'if(yc(H[1,{rr+1}],0)!=0){{print("PIVOT_ERROR");quit;}}']
 lines += [f'poly lam=yc(H[1,{J+1}],{a});',f'write(":w {OUT}/{d["id"]}.lambda.txt",string(lam));',f'print("DONE {d["id"]} "+string(size(lam)));','quit;']
 script=OUT/(d['id']+'.derive.sing');script.write_text('\n'.join(lines)+'\n')
 t=time.monotonic();pr=subprocess.run(['prlimit','--as=17179869184','--','Singular','-q',str(script)],capture_output=True,text=True,timeout=600)
 fn=OUT/(d['id']+'.lambda.txt')
 print(d['id'],pr.returncode,round(time.monotonic()-t,2),pr.stdout[-1000:],pr.stderr[-1000:],flush=True)
 assert pr.returncode==0 and 'DONE '+d['id'] in pr.stdout and 'ERROR' not in pr.stdout and '?' not in pr.stdout
 d.update(L=L,D2=D,W=W,J=J,a=a,family_pivots=sorted(mon,reverse=True),lambda_path=str(fn),lambda_terms=int(pr.stdout.strip().split()[-1]),lambda_bytes=fn.stat().st_size)
 raw=fn.read_bytes(); compressed=fn.with_suffix(fn.suffix+'.gz'); compressed.write_bytes(gzip.compress(raw,mtime=0))
 d.update(lambda_path=str(compressed),lambda_sha256=hashlib.sha256(raw).hexdigest(),lambda_compressed_sha256=hashlib.sha256(compressed.read_bytes()).hexdigest(),lambda_compressed_bytes=compressed.stat().st_size)
 fn.unlink()
 allres=[v for v in allres if v['id']!=d['id']]+[d]
 (OUT/'leaders.json').write_text(json.dumps(allres,indent=2)+'\n')
