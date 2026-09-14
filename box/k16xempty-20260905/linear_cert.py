#!/usr/bin/env python3
import ast,json,math,sys,time
from pathlib import Path
from fractions import Fraction as Q
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'linear_python'))
import flint
flint.ctx.threads=1
T=int(sys.argv[1]); e2=3*(T+1); weights=list(range(1,T))+[T+1]; tw=8*T+2
start=time.monotonic()
def say(s): print(f'{time.monotonic()-start:.3f} {s}',flush=True)
def scalar(node):
 if isinstance(node,ast.Constant):return Q(node.value)
 if isinstance(node,ast.UnaryOp):return -scalar(node.operand) if isinstance(node.op,ast.USub) else scalar(node.operand)
 if isinstance(node,ast.BinOp):
  a,b=scalar(node.left),scalar(node.right)
  if isinstance(node.op,ast.Add): return a+b
  if isinstance(node.op,ast.Sub): return a-b
  if isinstance(node.op,ast.Mult): return a*b
  if isinstance(node.op,ast.Div): return a/b
 raise ValueError(ast.dump(node))
def ev(node):
 if isinstance(node,ast.Name): assert node.id=='d';return Q(0),Q(1,3)
 if isinstance(node,ast.Constant):return Q(node.value),Q(0)
 if isinstance(node,ast.UnaryOp):
  a,b=ev(node.operand);return (-a,-b) if isinstance(node.op,ast.USub) else (a,b)
 if isinstance(node,ast.BinOp):
  a,b=ev(node.left);c,d=ev(node.right)
  if isinstance(node.op,ast.Add): return a+c,b+d
  if isinstance(node.op,ast.Sub): return a-c,b-d
  if isinstance(node.op,ast.Mult): return a*c+e2*b*d,a*d+b*c
  if isinstance(node.op,ast.Div):
   norm=c*c-e2*d*d;return (a*c-e2*b*d)/norm,(b*c-a*d)/norm
 raise ValueError(ast.dump(node))
raw={};label=None
for line in (root/f'linear_t{T}_terms.txt').read_text().splitlines():
 if '|' not in line:label=line;raw[label]={};continue
 ss,ee=line.split('|');ee=tuple(map(int,ee.split(',')));raw[label][ee]=ev(ast.parse(ss,mode='eval').body)
scales={}; polys={}
for label,poly in raw.items():
 scale=math.lcm(*(v.denominator for ab in poly.values() for v in ab)); scales[label]=Q(scale)
 ints={ee:(int(a*scale),int(b*scale)) for ee,(a,b) in poly.items()};gg=math.gcd(*(v for ab in ints.values() for v in ab))
 if gg>1:
  # keep rational normalization factor permitted
  ints={ee:(a//gg,b//gg) for ee,(a,b) in ints.items()}; scales[label]=Q(scale,gg)
 polys[label]=ints
say('PARSED '+str({k:len(v) for k,v in raw.items()}))
def mons(w,ii=0):
 if ii==len(weights)-1:
  if w%weights[ii]==0:yield (w//weights[ii],)
  return
 for ex in range(w//weights[ii]+1):
  for tail in mons(w-ex*weights[ii],ii+1):yield (ex,)+tail
monlist=list(mons(tw));lookup={m:i for i,m in enumerate(monlist)};n=len(monlist)
cols=[]
for k in range(2*T,1,-1):
 for mon in mons(tw-(4*T+2-k)):cols.append((k,mon))
say(f'MACAULAY {n}x{len(cols)}')
prime=32003
while True:
 eroot=next((rr for rr in range(prime) if (rr*rr-e2)%prime==0),None)
 if eroot is not None: break
 prime+=2
 while not flint.fmpz(prime).is_prime():prime+=2
mat=flint.nmod_mat(n,len(cols),prime)
for j,(k,mon) in enumerate(cols):
 for ee,(aa,bb) in polys[f'ROW {k}'].items():
  i=lookup[tuple(x+y for x,y in zip(mon,ee))];mat[i,j]=(aa+eroot*bb)%prime
say(f'MODULAR_MATRIX p={prime} eroot={eroot}')
rr,rank=mat.rref(); piv=[]
for i in range(rank):
 for j in range((piv[-1]+1) if piv else 0,len(cols)):
  if rr[i,j]:piv.append(j);break
say(f'MODULAR_RANK {rank}')
if rank!=n:raise RuntimeError(f'Need row subset rank {rank} vs n {n}')
if '--rank-only' in sys.argv:
 import hashlib
 mm=flint.nmod_mat(n,n,prime)
 for i in range(n):
  for j,col in enumerate(piv):mm[i,j]=mat[i,col]
 det=int(mm.det())
 assert det!=0
 bad=[(label,str(v.denominator)) for label,poly in raw.items() for ab in poly.values() for v in ab if v.denominator%prime==0]
 assert not bad
 meta={'t':T,'target_weight':tw,'coefficient_field':'Q(d),3*d^2=t+1','integral_generator':'e=3*d, e^2=3*(t+1)','prime':prime,'e_image':eroot,'d_image':(eroot*pow(3,-1,prime))%prime,'matrix_shape':[n,len(cols)],'rank':rank,'minor_determinant_mod_prime':det,'row_monomials':monlist,'selected_columns':[{'source_row':cols[j][0],'multiplier_exponents':cols[j][1],'full_column_index':j,'exact_row_scale':str(scales[f"ROW {cols[j][0]}"])} for j in piv],'all_raw_coefficient_denominators_are_prime_units':True,'hashes':{str(pth.name):hashlib.sha256(pth.read_bytes()).hexdigest() for pth in [root/f'controls_t{T}_raw.sing',root/f'linear_t{T}_terms.txt',Path(__file__)]}}
 (root/f'linear_t{T}_rank_certificate.json').write_text(json.dumps(meta,indent=2)+'\n')
 say(f'EXACT_RANK_MINOR_SAVED detmod={det} raw_denominators_prime_units=True')
 sys.exit(0)
A=flint.fmpz_mat(2*n,2*n)
for j,col in enumerate(piv):
 k,mon=cols[col]
 for ee,(aa,bb) in polys[f'ROW {k}'].items():
  i=lookup[tuple(x+y for x,y in zip(mon,ee))]
  A[i,j]=aa;A[i+n,j]=bb;A[i,j+n]=e2*bb;A[i+n,j+n]=aa
rhs=flint.fmpz_mat(2*n,1)
for ee,(aa,bb) in polys['TARGET'].items():i=lookup[ee];rhs[i,0]=aa;rhs[i+n,0]=bb
say(f'EXACT_MATRIX {2*n} square')
sol=A.solve(rhs)
say('EXACT_SOLVE_DONE')
assert A*sol==rhs
say('EXACT_MATRIX_REPLAY_PASS')
variables=[f'c{j}' for j in range(1,T)]+['b']
cofs={k:[] for k in range(2,2*T+1)}
for j,col in enumerate(piv):
 aa=Q(str(sol[j,0]));bb=Q(str(sol[j+n,0]));k,mon=cols[col]
 aa*=scales[f'ROW {k}']/scales['TARGET'];bb*=3*scales[f'ROW {k}']/scales['TARGET']
 if not aa and not bb:continue
 mm='*'.join(v if p==1 else f'{v}^{p}' for v,p in zip(variables,mon) if p) or '1'
 cofs[k].append(f'({aa}+({bb})*d)*{mm}')
out=[f'< "{root}/controls_t{T}_raw.sing";',f'matrix linear_cofs[{2*T-1}][1];']
for k,ls in cofs.items():out.append(f'linear_cofs[{k-1},1]='+'+'.join(ls)+';' if ls else f'linear_cofs[{k-1},1]=0;')
out.extend(['poly linear_replay=0;','for(int kk=1;kk<=size(rows);kk++){linear_replay=linear_replay+rows[kk]*linear_cofs[kk,1];}',f'if(linear_replay==target^2){{print("LINEAR_COFACTOR_IDENTITY_PASS t={T}");}}else{{print("FAIL_LINEAR_COFACTOR_IDENTITY");}}','quit;'])
p=root/f'linear_t{T}_certificate.sing';p.write_text('\n'.join(out)+'\n')
(root/f'linear_t{T}_metadata.json').write_text(json.dumps({'t':T,'weight':tw,'matrix_shape':[n,len(cols)],'rank':rank,'prime_selection_only':prime,'selected_columns':piv,'exact_field':'Q(d), 3*d^2=t+1','cofactor_terms':{k:len(v) for k,v in cofs.items()},'certificate_bytes':p.stat().st_size,'elapsed_sec':time.monotonic()-start},indent=2))
say(f'CERTIFICATE_WRITTEN bytes={p.stat().st_size}')
