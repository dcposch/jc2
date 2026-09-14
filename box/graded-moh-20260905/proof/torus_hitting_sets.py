#!/usr/bin/env python3
"""Find exact minimum positive-x coordinate covers of c=1 target, emit full branches."""
from pathlib import Path
import json,re,itertools,hashlib
OUT=Path('box/graded-moh-20260905/proof/torus_branches')
AUDITS=Path('box/graded-moh-20260905/instrument')
TOKEN=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
TERM=re.compile(r'[+-]?[^+-]+')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def loadrows(p):
 with Path(p).open() as f:
  assert f.readline().strip()=='source_index|h_power|x_power|y_power|expr'
  for line in f:
   a=line.strip().split('|',4);yield tuple(map(int,a[:4]))+(a[4],)
def parse(expr):
 out=[]
 for term in TERM.findall(expr):
  sign=-1 if term[0]=='-' else 1;mon={};coef=sign
  for f in term.lstrip('+-').split('*'):
   mt=TOKEN.fullmatch(f)
   if mt:
    v,e=mt.groups();mon[v]=mon.get(v,0)+int(e or 1)
   else:
    assert re.fullmatch(r'\d+',f),f;coef*=int(f)
  out.append((coef,mon))
 return out
def render(terms,ones=(),mapping=None):
 result={}
 for coef,mon in terms:
  key=tuple((v,e)for v,e in mon.items() if v not in ones)
  result[key]=result.get(key,0)+coef
 ans=[]
 for key,c in result.items():
  if not c:continue
  factors=[]
  if abs(c)!=1 or not key:factors.append(str(abs(c)))
  for v,e in key:
   v=mapping[v] if mapping else v;factors.append(v+(f'^{e}'if e>1 else ''))
  ans.append(('-'if c<0 else '+')+'*'.join(factors))
 return ''.join(ans).lstrip('+') or '0'
OUT.mkdir(parents=True,exist_ok=True);reports=[]
for ap in sorted(AUDITS.glob('*_audit.json')):
 audit=json.loads(ap.read_text());stem=ap.stem[:-6];rows=list(loadrows(audit['rows_path']));weights=audit['bidegrees'];target=[r for r in rows if any(v=='c'for v,e in TOKEN.findall(r[4]))];assert len(target)==1
 terms=parse(target[0][4]);fterms=[];cpart=[]
 for coef,mon in terms:
  (cpart if 'c'in mon else fterms).append((coef,mon))
 assert len(cpart)==1 and cpart[0]==(-1,{'c':1}),cpart
 edges=[frozenset(v for v in mon if weights[v][0]<0)for coef,mon in fterms];assert all(edges)
 unique=set(edges);minimal=sorted((e for e in unique if not any(d<e for d in unique)),key=lambda e:(len(e),sorted(e)))
 forced=set().union(*(set(e)for e in minimal if len(e)==1)) if minimal else set()
 left=[e for e in minimal if not e&forced];universe=sorted(set().union(*left)) if left else []
 checked=0;chosen=None;minsize=None
 for k in range(len(universe)+1):
  for combo in itertools.combinations(universe,k):
   checked+=1;s=set(combo)|forced
   if all(e&s for e in left):chosen=sorted(s);minsize=len(s);break
  if chosen is not None:break
 assert all(set(chosen)&e for e in edges)
 # Exact coefficient identity F=Σ z*q_z, assign each term to first covering coordinate.
 multipliers={z:[] for z in chosen}
 for coef,mon in fterms:
  z=next(z for z in chosen if z in mon);quot=dict(mon);quot[z]-=1
  if quot[z]==0:del quot[z]
  multipliers[z].append((coef,quot))
 D=weights['c'][1];lp1=-weights['c'][0]
 residual={z:lp1*weights[z][1]+D*weights[z][0] for z in chosen};assert all(residual.values())
 dest=OUT/stem;dest.mkdir(exist_ok=True)
 (dest/'target_c_polynomial.txt').write_text(render(fterms)+'\n')
 certificate={z:render(multipliers[z]) for z in chosen}
 (dest/'cover_identity.json').write_text(json.dumps(dict(target_source_index=target[0][0],identity='F=sum(z*coefficient[z])',coefficient=certificate),indent=2)+'\n')
 checks='ring r=0,('+','.join(audit['variables'])+'),dp;\npoly F='+render(fterms)+';\npoly chk=F-('+ '+'.join(z+'*('+certificate[z]+')'for z in chosen)+');\nprint("COVER_IDENTITY="+string(chk==0));\nquit;\n'
 (dest/'check_cover.sing').write_text(checks)
 branches=[]
 for z in chosen:
  bd=dest/z;bd.mkdir(exist_ok=True);remaining=[v for v in audit['variables'] if v not in {'c',z}];mapping={v:f'v{i+1}'for i,v in enumerate(remaining)}
  rr=[parse(row[4])for row in rows];expr=[render(ts,{'c',z})for ts in rr]
  common='// Full completed-fibre equations under c=1 and '+z+'=1; no zero-prefix branch.\nring r=0,('+','.join(remaining)+'),dp;\noption(redSB);\nideal I=\n'+',\n'.join(expr)+';\n'
  (bd/'branch_ideal.sing').write_text(common)
  run=common+f'print("TORUS_READY variables={len(remaining)} generators={len(rows)} coordinate={z}");\nint started=timer;\nideal G=std(I);\nint isunit=(reduce(1,G)==0);\nprint("TORUS_DONE unit="+string(isunit)+" basis="+string(size(G))+" elapsed="+string(timer-started));\nif(isunit){{write(":w unit_basis.sing",string(G));}}\nquit;\n'
  (bd/'branch.sing').write_text(run)
  for prime in(0,1073741827):
   (bd/f'branch_p{prime}.ms').write_text(','.join(mapping[v]for v in remaining)+'\n'+str(prime)+'\n'+',\n'.join(render(ts,{'c',z},mapping)for ts in rr)+'\n')
  custody=dict(source_audit=str(ap),source_audit_sha256=sha(ap),source_rows=audit['rows_path'],source_rows_sha256=sha(audit['rows_path']),source_generator_indices=[r[0]for r in rows],source_generator_count=len(rows),source_field='Q',source_variables=audit['variables'],branch_field='Q',branch_variables=remaining,branch_order='dp',branch_map={v:('1'if v in {'c',z}else v)for v in audit['variables']},msolve_map=mapping,coordinate=z,residual_character=residual[z],cover_coordinates=chosen,cover_identity=str(dest/'cover_identity.json'),coverage='Every c=1 point has some cover coordinate nonzero; residual torus sets that coordinate to1. All cover branches required; no zero-prefix constraints.',files={f.name:sha(f)for f in bd.iterdir()if f.is_file()})
  (bd/'custody.json').write_text(json.dumps(custody,indent=2)+'\n');branches.append(str(bd))
 rep=dict(stem=stem,parameters=audit['parameter_count'],target_source_index=target[0][0],target_terms=len(fterms),positive_x_universe=sorted(set().union(*edges)),minimal_edges=[sorted(e)for e in minimal],forced_singletons=sorted(forced),minimum_hitting_set=chosen,minimum_size=minsize,combinations_tested=checked,residual_characters=residual,target_rows_sha256=sha(audit['rows_path']),cover_identity=str(dest/'cover_identity.json'),branches=branches)
 reports.append(rep);print(json.dumps(rep),flush=True)
(OUT/'summary.json').write_text(json.dumps(reports,indent=2)+'\n')
