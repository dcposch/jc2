#!/usr/bin/env python3
"""Audit genuine coefficient grading; emit exact c=1 torus slices, no specialization.
The c=1 receiver is equisatisfiable over Qbar with c!=0 because c has nonzero torus weight.
No missing parameter or generator is removed. JSON records every explicit ring map.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,re,math
from pathlib import Path

BASE=Path('box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes')
OUT=Path(__file__).resolve().parent
VAR=re.compile(r'[A-Za-z][A-Za-z0-9_]*')
TERM=re.compile(r'[+-]?[^+-]+')
FACTOR=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?$')

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def weights(m):
 K=m['meta']['closed_form']['K']; cf=m['meta']['closed_form'];r=m['meta']['row']
 ww={}
 for v in m['variables']:
  if v=='c': w=(-int(cf['ell'])-1,int(r['n'])+int(r['m'])-1)
  elif v.startswith('h_'):
   _,b,a=v.split('_');w=(-int(b),int(K)-int(a))
  else:
   block,b,a=v.split('_');w=(-int(b),int(block[1:])*int(K)-int(a))
  ww[v]=w
 assert all(w[1]>0 for w in ww.values())
 return ww

def rows(p):
 with p.open() as f:
  assert f.readline().strip()=='source_index|h_power|x_power|y_power|expr'
  for line in f:
   if not line.strip():continue
   vals=line.strip().split('|',4)
   if len(vals)!=5:raise ValueError((p,line[:100]))
   yield tuple(map(int,vals[:4]))+(vals[4],)

def audit(m,p):
 ww=weights(m);K=int(m['meta']['closed_form']['K']);cw=ww['c'];summary=[]
 terms=0;degrees=collections.Counter();allvars=set();maxordinary=0;bad=[]
 for idx,h,b,a,expr in rows(p):
  expected=(-b-1,cw[1]-K*h-a);observed=set();used=set();nt=0;rowordinary=0
  for term in TERM.findall(expr):
   dx=dy=ordinary=0
   for f in term.lstrip('+-').split('*'):
    match=FACTOR.fullmatch(f)
    if match:
     v,power=match.groups();power=int(power or 1)
     if v not in ww:raise ValueError(('unknown variable',v))
     dx+=ww[v][0]*power;dy+=ww[v][1]*power;ordinary+=power;used.add(v)
    elif not re.fullmatch(r'\d+(?:/\d+)?',f):raise ValueError(('unparsed factor',f))
   observed.add((dx,dy));nt+=1;rowordinary=max(rowordinary,ordinary)
  if observed!={expected}:bad.append({'source_index':idx,'expected':expected,'observed':sorted(observed)})
  if any(ww[v][1]>expected[1] for v in used):raise ValueError('positive grading triangularity failure')
  summary.append({'source_index':idx,'h_power':h,'x_power':b,'y_power':a,'bidegree':expected,'positive_degree':expected[1],'terms':nt,'ordinary_degree':rowordinary,'used_variables':sorted(used),'contains_c':'c' in used})
  terms+=nt;degrees[expected[1]]+=1;allvars|=used;maxordinary=max(maxordinary,rowordinary)
 if not summary:raise ValueError('empty rows file')
 if bad:raise ValueError(('homogeneity failure',bad[:4]))
 crows=[r for r in summary if r['contains_c']]
 assert len(crows)==1
 hist=collections.Counter(w[1] for w in ww.values());bands=[]
 for d,count in sorted(degrees.items()):
  selected=[r for r in summary if r['positive_degree']<=d]
  bands.append({'threshold':d,'new_rows':count,'cumulative_rows':len(selected),'active_parameters':len(set().union(*(set(r['used_variables']) for r in selected))),'c_present':any(r['contains_c'] for r in selected),'all_parameters_of_weight_at_most_threshold':sum(v<=d for v in (w[1] for w in ww.values()))})
 # Finite component dimensions of Q[parameters] in bidegrees N*deg(c).
 # Store reverse x degree B=-wx for a nonnegative two-dimensional generating function.
 component=[]
 for N in (1,2,3):
  B=-N*cw[0];D=N*cw[1];arr=[[0]*(D+1) for _ in range(B+1)];arr[0][0]=1
  for wx,dy in ww.values():
   bx=-wx
   if bx>B:continue
   for b0 in range(bx,B+1):
    for d0 in range(dy,D+1):arr[b0][d0]+=arr[b0-bx][d0-dy]
  component.append({'N':N,'bidegree':[N*cw[0],D],'monomials':arr[B][D]})
 return {'metadata_path':str(next(BASE.glob(f'*/meta/{m["meta"]["row"]["key"]}.json'))),'rows_path':str(p),'rows_sha256':sha(p),'row_count':len(summary),'term_count':terms,'homogeneous_bigrading':True,'parameter_count':len(ww),'variables':list(ww),'bidegrees':ww,'positive_weights':{v:w[1] for v,w in ww.items()},'weight_min':min(w[1] for w in ww.values()),'weight_max':max(w[1] for w in ww.values()),'c_weight':cw,'weight_histogram':dict(sorted(hist.items())),'generator_degree_min':min(degrees),'generator_degree_max':max(degrees),'max_ordinary_generator_degree':maxordinary,'unused_parameters':sorted(set(ww)-allvars),'bands':bands,'rows':summary,'c_power_component_dimensions':component,'threshold_obstruction':f'Every subsystem with positive degree < {cw[1]} omits c and has origin times the full c-line. Such a subsystem cannot force c=0. All rows have degree <= {cw[1]}, so the minimal forcing threshold, IF full radical membership holds, is exactly {cw[1]}.'}

def emit(m,p,a):
 stem=m['meta']['row']['key'];dest=OUT/stem;dest.mkdir(exist_ok=True)
 vv=[v for v in m['variables'] if v!='c'];name_map={v:f'v{i+1}' for i,v in enumerate(vv)};name_map['c']='1'
 rowlist=list(rows(p));exprs=[VAR.sub(lambda x: '1' if x.group()=='c' else x.group(),r[4]) for r in rowlist]
 header='// Exact c=1 torus receiver of complete coefficient ideal; all parameters other than c retained.\n'
 ring='ring r=0,('+','.join(vv)+'),dp;\n'
 common=header+ring+'option(redSB);\nideal I=\n'+',\n'.join(exprs)+';\n'
 (dest/'slice.sing').write_text(common+'print("GRADED_READY variables='+str(len(vv))+' generators='+str(len(exprs))+'");\nint start=timer;\nideal G=std(I);\nprint("GRADED_DONE elapsed="+string(timer-start)+" basis_size="+string(size(G))+" unit="+string(reduce(1,G)==0));\nif(reduce(1,G)==0){ write(":w basis.sing",string(G)); }\nquit;\n')
 (dest/'slice_ideal.sing').write_text(common)
 for prime in (0,1073741827):
  ms=','.join(name_map[v] for v in vv)+'\n'+str(prime)+'\n'+',\n'.join(VAR.sub(lambda x:name_map[x.group()],r[4]) for r in rowlist)+'\n'
  (dest/f'slice_p{prime}.ms').write_text(ms)
 # Homogeneous input retains c; weighted global order. Exact degree bound supplied by caller.
 hring='ring r=0,('+','.join(m['variables'])+'),wp('+','.join(str(a['positive_weights'][v]) for v in m['variables'])+');\n'
 hcommon=header.replace('c=1 torus receiver','homogeneous coefficient ideal')+hring+'option(redSB);\nideal I=\n'+',\n'.join(r[4] for r in rowlist)+';\n'
 (dest/'homogeneous_ideal.sing').write_text(hcommon)
 for N in (1,2):
  D=N*a['c_weight'][1]
  (dest/f'truncate_c{N}.sing').write_text(hcommon+f'int DEGREE_BOUND={D};\ndegBound=DEGREE_BOUND;\nideal G=std(I);\npoly target=c^{N};\npoly nf=reduce(target,G);\nprint("TRUNCATION_DONE bound={D} target=c^{N} nf_zero="+string(nf==0)+" basis_size="+string(size(G)));\nif(nf==0){{degBound=0; matrix witness=lift(I,ideal(target)); matrix inputmatrix[1][size(I)]=I; matrix checkmatrix=inputmatrix*witness; print("IDENTITY_CHECK="+string(checkmatrix[1,1]==target)); write(":w identity_c{N}.sing",string(witness));}}\nquit;\n')
 custody={'source_metadata_sha256':sha(a['metadata_path']),'source_rows_sha256':sha(p),'source_ring':{'field':'Q','variables':m['variables']},'slice_ring':{'field':'Q','variables':vv,'order':'dp'},'slice_map':{v:('1' if v=='c' else v) for v in m['variables']},'msolve_variable_map':name_map,'slice_justification':'Z2 graded ideal with c nonzero character; Qbar torus orbit of each c!=0 point meets c=1. Faithful field extension equates unit ideals over Q and Qbar. No other coordinate is fixed.','generator_source_order':[r[0] for r in rowlist],'generator_count':len(rowlist),'files':{f.name:sha(f) for f in dest.iterdir() if f.is_file()}}
 (dest/'custody.json').write_text(json.dumps(custody,indent=2)+'\n')
 a['output_directory']=str(dest)
 return dest

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--counts',default='77,111,129,136');parser.add_argument('--emit',action='store_true');args=parser.parse_args();counts=set(map(int,args.counts.split(',')));reports=[]
 for mp in sorted(BASE.glob('*/meta/*json'),key=lambda p:json.loads(p.read_text()).get('parameter_count',10**9)):
  if '_union' in mp.name:continue
  m=json.loads(mp.read_text())
  if m['parameter_count'] not in counts:continue
  stem=mp.stem;original=Path(m['rows_path']);direct=original.with_name(original.stem.replace('_rows','_direct_rows')+'.tsv');local=OUT/(stem+'_direct_rows.tsv')
  p=local if local.exists() else direct if direct.exists() and direct.stat().st_size>42 else original
  a=audit(m,p)
  if args.emit:emit(m,p,a)
  (OUT/(stem+'_audit.json')).write_text(json.dumps(a,indent=2)+'\n');reports.append({k:v for k,v in a.items() if k not in ('rows','bidegrees','positive_weights','variables')})
  print(json.dumps({'stem':stem,'parameters':a['parameter_count'],'rows':a['row_count'],'terms':a['term_count'],'cweight':a['c_weight'],'degree_range':[a['generator_degree_min'],a['generator_degree_max']],'out':a.get('output_directory')}),flush=True)
 (OUT/'audit_summary.json').write_text(json.dumps(reports,indent=2)+'\n')
if __name__=='__main__':main()
