#!/usr/bin/env python3
"""Exact bidegree-target restriction, no coordinate specialization.
For homogeneous f_j degree (x_j,y_j), c^N degree (X,Y), only x_j<=X,y_j<=Y
and parameters of individual degree <=(X,Y) can occur in a membership identity.
This emitter preserves every such source row, original ordering, and names.
"""
import argparse,hashlib,json,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('classid');p.add_argument('fibre');p.add_argument('--power',type=int,default=1);a=p.parse_args()
base=Path('box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes')/a.classid
stem=f'{a.classid}_{a.fibre}'
meta=json.loads((base/'meta'/f'{stem}.json').read_text())
row=next(r for r in json.loads((base/'class.json').read_text())['rows'] if r['stem']==stem)
K=row['K'];D=row['n_prime']+row['m_prime']-1;ell=row['ell'];X=(ell+1)*a.power;Y=D*a.power
builder=base/'builders'/f'{stem}_direct_builder.sing';rowsfile=base/'rows'/f'{stem}_direct_rows.tsv'
vs=re.search(r'ring R=0,\((.*?)\),',builder.read_text()).group(1).split(',')[2:]
def wt(v):
 if v=='c':return(ell+1,D)
 kind,b,y=v.split('_');i=1 if kind=='h' else int(kind[1:]);return(int(b),i*K-int(y))
W={v:wt(v) for v in vs};variables=[v for v in vs if W[v][0]<=X and W[v][1]<=Y]
rows=[]
for line in rowsfile.read_text().splitlines()[1:]:
 source,h,x,y,expr=line.split('|',4);wx=int(x)+1;wy=D-int(y)
 if wx<=X and wy<=Y:rows.append(dict(source=int(source),x=wx,y=wy,expr=expr))
used=set(re.findall(r'\b(?:h_\d+_\d+|[AB]\d+_\d+_\d+|c)\b','\n'.join(r['expr'] for r in rows)))
assert used<=set(variables), used-set(variables)
out=Path('box/graded-moh-20260905/truncation')/(stem+f'_N{a.power}');out.mkdir(parents=True,exist_ok=True)
info=dict(classid=a.classid,fibre=a.fibre,source_rows=str(rowsfile),source_sha256=hashlib.sha256(rowsfile.read_bytes()).hexdigest(),builder=str(builder),builder_sha256=hashlib.sha256(builder.read_bytes()).hexdigest(),power=a.power,target_bidegree=[X,Y],variables=variables,weights={v:W[v] for v in variables},selected_rows=[{k:v for k,v in r.items() if k!='expr'} for r in rows],selected_row_count=len(rows),original_variable_count=len(vs),selected_variable_count=len(variables),used_variable_count=len(used))
(out/'manifest.json').write_text(json.dumps(info,indent=2)+'\n')
(out/'input.sing').write_text('ring R=0,('+','.join(variables)+'),dp;\nideal I=\n'+',\n'.join('('+r['expr']+')' for r in rows)+';\n')
pre=f'''LIB "presolve.lib";
<"{out}/input.sing";
print("INPUT_ROWS="+string(size(I))+" INPUT_VARS="+string(nvars(R)));
list L=elimpart(I);
map phi=R,L[5];
ideal J=L[1];
poly target=phi(c^{a.power});
write(":w {out}/residual-rows.txt",string(J));
write(":w {out}/residual-variables.txt",string(simplify(L[4],2)));
write(":w {out}/target.txt",string(target));
write(":w {out}/substitutions.txt",string(L[3]));
write(":w {out}/map.txt",string(L[5]));
print("ELIMINATED="+string(size(L[2]))+" RESIDUAL_ROWS="+string(size(J))+" TARGET_ZERO="+string(target==0));
print("MAP_ORIGINAL_EQUALS_RESIDUAL="+string(phi(I)==J));
quit;
'''
(out/'preprocess.sing').write_text(pre)
print(json.dumps({k:info[k] for k in ['selected_row_count','original_variable_count','selected_variable_count','used_variable_count','target_bidegree']}))
print(out)
