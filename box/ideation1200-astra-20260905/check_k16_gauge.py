from pathlib import Path
import re, subprocess, time
import sympy as S
out=Path(__file__).resolve().parent
c,b,s,z=S.symbols('c1 b s z')
for sign in [-1,1]:
 src=Path(f'/home/ubuntu/jc2/box/k16f3abel-20260905/controls_t2_d{sign}_raw.sing').read_text()
 def expr(name): return S.sympify(re.search(r'poly '+name+r'=(.*);',src).group(1).replace('^','**'),locals={'c1':c,'b':b})
 B=expr('Bsol'); eta=expr('eta')
 rows=[S.sympify(q.replace('^','**'),locals={'c1':c,'b':b}) for q in re.search(r'ideal rows=(.*);',src).group(1).split(',')]
 M=B.subs(b,0); N=S.diff(B,b); rho=eta.subs(b,0); sigma=S.diff(eta,b)
 Delta=S.factor(N-sigma); A=S.factor(rho-M); H=S.factor(N*rho-M*sigma)
 v=B/eta; cn=c/v; bn=b/v**3
 print('T2_D',sign,'AFFINE',S.diff(B,b,2)==0 and S.diff(eta,b,2)==0)
 print('DELTA',Delta,'A',A,'H',H)
 print('SCALE_B',S.expand(B.subs({c:s*c,b:s**3*b},simultaneous=True)-s**5*B)==0)
 print('SCALE_ETA',S.expand(eta.subs({c:s*c,b:s**3*b},simultaneous=True)-s**4*eta)==0)
 print('SLICE_GAUGE',S.cancel(B.subs({c:cn,b:bn},simultaneous=True)-eta.subs({c:cn,b:bn},simultaneous=True))==0)
 print('B_ELIM',S.cancel(B.subs(b,A/Delta)-H/Delta)==0,'ETA_ELIM',S.cancel(eta.subs(b,A/Delta)-H/Delta)==0)
 def fmt(p):
  terms=[]
  for exps,coeff in S.Poly(p,c,b,z).terms():
   terms.append('('+str(coeff)+')'+''.join('*'+str(v)+('^'+str(e) if e>1 else '') for v,e in zip([c,b,z],exps) if e))
  return '+'.join(terms) or '0'
 base='ring r=0,(c1,b,z),dp;\n'+'ideal E='+','.join(fmt(e) for e in rows)+';\npoly B='+fmt(B)+';\npoly eta='+fmt(eta)+';\npoly D='+fmt(Delta)+';\npoly A='+fmt(A)+';\n'
 base+='ideal trueSlice=E, B-eta,1-z*B; ideal G=std(trueSlice); print("TRUE_SLICE_UNIT "+string(reduce(1,G)==0));\n'
 base+='ideal bareSlice=B-eta,1-z*B; ideal GC=std(bareSlice); print("BARE_SLICE_NONUNIT "+string(reduce(1,GC)!=0));\n'
 base+='ideal boundary=E,D,A,1-z*B; ideal GB=std(boundary); print("BOUNDARY_UNIT "+string(reduce(1,GB)==0));\n'
 base+='poly HH='+fmt(H)+';\n'
 # b-eliminated numerator equations cleared by actual b degree, not fixed fictitious degree.
 nr=[S.cancel(Delta**S.degree(e,b)*e.subs(b,A/Delta)).expand() for e in rows]
 assert all(S.denom(e)==1 for e in nr)
 base+='ideal main='+','.join(fmt(e) for e in nr)+',1-z*D*HH; ideal GM=std(main); print("ELIM_MAIN_UNIT "+string(reduce(1,GM)==0));\nquit;\n'
 file=out/f't2_d{sign}_gauge.sing';file.write_text(base)
 r=subprocess.run(['timeout','--foreground','20s','Singular','-q',str(file)],capture_output=True,text=True)
 print('CAS_EXIT',r.returncode);print(r.stdout.strip()); print(r.stderr.strip())
 assert r.returncode==0 and 'error' not in r.stdout.lower() and r.stdout.count(' 1')==4
 # Exact nonempty decoupled-control witness c1=1, b=A(1)/Delta(1).
 bv=S.cancel(A.subs(c,1)/Delta.subs(c,1)); kv=S.cancel(B.subs({c:1,b:bv}));print('BARE_WITNESS',{'c1':1,'b':str(bv),'B=eta':str(kv),'z':str(1/kv)})
for t in [8,9,10,11]:
 w=8*t+2; h=[0]*(w+1);h[0]=1
 for wt in list(range(1,t))+[t+1]:
  for i in range(wt,w+1): h[i]+=h[i-wt]
 print('MACAULAY',t,w,h[w],sum(h[w-(4*t+1-k)] for k in range(1,2*t)))
