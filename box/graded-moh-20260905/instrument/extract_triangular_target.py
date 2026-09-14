#!/usr/bin/env python3
import json,re,hashlib,collections
from pathlib import Path
from graded_audit import OUT,TERM,FACTOR,VAR,sha
stem='C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6';d=OUT/stem
a=json.loads((OUT/(stem+'_audit.json')).read_text()); w=a['bidegrees'];pivots=json.loads((d/'triangular_pivots.json').read_text());eliminated={p[2] for p in pivots};remaining=[v for v in a['variables'] if v not in eliminated]
def degree(term):
 wx=wy=ordinary=0;used=set()
 for factor in term.lstrip('+-').split('*'):
  f=FACTOR.fullmatch(factor)
  if f:
   v,e=f.groups();e=int(e or 1);wx+=w[v][0]*e;wy+=w[v][1]*e;ordinary+=e;used.add(v)
  else:assert re.fullmatch(r'\d+(?:/\d+)?',factor),factor
 return (wx,wy),used,ordinary
selected=[];used=set();hist=collections.Counter();nt=0
source=(d/'triangular_reduced.txt').read_text().strip()
for idx,expr in enumerate(source.split(',')):
 first=TERM.match(expr).group();deg=degree(first)[0]
 if -deg[0]>-w['c'][0]:continue
 for term in TERM.findall(expr):
  td,uv,_=degree(term);assert td==deg;assert not uv&eliminated;used|=uv;nt+=1
 selected.append((idx,expr,deg));hist[deg[1]]+=1
variables=[v for v in remaining if v in used];weights=[w[v][1] for v in variables]
header='// Bihomogeneous triangular image of original rows of xcharge <= ell+1. All omitted parameters remain free.\n'
ring='ring r=0,('+','.join(variables)+'),wp('+','.join(map(str,weights))+');\n'
common=header+ring+'option(redSB);\nideal I=\n'+',\n'.join(x[1] for x in selected)+';\n'
(d/'triangular_N1_ideal.sing').write_text(common)
for prime in (0,1073741827):
 script=common.replace('ring r=0,',f'ring r={prime},')+f'\ndegBound={w["c"][1]};\nideal G=std(I);\npoly nf=reduce(c,G);\nprint("TRIANGULAR_N1_DONE characteristic={prime} target=c nf_zero="+string(nf==0)+" basis_size="+string(size(G)));\nif(nf==0){{degBound=0;matrix M=lift(I,ideal(c));matrix inputmatrix[1][size(I)]=I;matrix product=inputmatrix*M;print("TRIANGULAR_N1_IDENTITY="+string(product[1,1]==c));write(":w triangular_N1_p{prime}_identity.txt",string(M));}}\nquit;\n'
 (d/f'triangular_N1_p{prime}.sing').write_text(script)
 vv=[v for v in variables if v!='c'];mp={v:f'v{i+1}' for i,v in enumerate(vv)};mp['c']='1'
 ms=','.join(mp[v] for v in vv)+'\n'+str(prime)+'\n'+',\n'.join(VAR.sub(lambda z:mp[z.group()],x[1]) for x in selected)+'\n'
 (d/f'triangular_N1_slice_p{prime}.ms').write_text(ms)
B=-w['c'][0];D=w['c'][1];ar=[[0]*(D+1) for _ in range(B+1)];ar[0][0]=1
for v in variables:
 bx=-w[v][0];dy=w[v][1]
 for b in range(bx,B+1):
  for dd in range(dy,D+1):ar[b][dd]+=ar[b-bx][dd-dy]
manifest={'type':'TRIANGULAR-BIHOMOGENEOUS-C-TARGET-COMPONENT','source_triangular_sha256':sha(d/'triangular_reduced.txt'),'source_rows_sha256':a['rows_sha256'],'source_row_indices_selected':[r['source_index'] for r in a['rows'] if -r['bidegree'][0]<=B],'source_triangular_indices_selected':[x[0] for x in selected],'eliminated':sorted(eliminated),'variables':variables,'unused_free_parameters':sorted(set(remaining)-used),'bidegrees':{v:w[v] for v in variables},'row_count':len(selected),'term_count':nt,'weights_histogram':dict(sorted(hist.items())),'c_target_component_dimension':ar[B][D],'remaining_parameters':len(remaining),'active_parameters':len(variables),'original_target_component_dimension':a['c_power_component_dimensions'][0]['monomials'],'map_path':str(d/'triangular_map.txt'),'map_sha256':sha(d/'triangular_map.txt'),'pivot_path':str(d/'triangular_pivots.json'),'pivot_sha256':sha(d/'triangular_pivots.json'),'pivot_proof':'At each prescribed step a generator rel has derivative wrt pivot equal to fixed nonzero rational coeff. Positive homogeneity excludes further pivot occurrences. Map pivot -> pivot-rel/coeff fixes all other coordinates; quotient isomorphism follows and eliminated relation = coeff*(pivot-value). Original source indices remain stable until final simplify. Singular TRIANGULAR_FAIL absent and failed=0. Each pivot equation has xcharge<=2. Substitution preserves both degrees, so image of xcharge<=2 input rows equals xcharge<=2 output rows, ignoring zero rows.','scope':'Exact c membership is equivalent after xcharge truncation because all variables have nonnegative xcharge; c^N for N>1 not exhausted. Any exact-Q UNIT after c=1 still implies full chart kill, as this is a necessary equation subset with no coordinate specialization.'}
(d/'triangular_N1_custody.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({k:v for k,v in manifest.items() if k in ('row_count','term_count','c_target_component_dimension','remaining_parameters','active_parameters','original_target_component_dimension')}))
