import json,re,ast
from collections import defaultdict
src=json.load(open('/tmp/jc2-lane.rM5Jkj/inputs/delta2_stage8.strongest.json'))
exp=json.load(open('/tmp/jc2-lane.rM5Jkj/inputs/complete_export.json'))
maps=src['maps']; norm=src['normalization']
print("map keys:",list(maps.keys()),"normalization:",norm)
print("residual_rows:",src['residual_rows'])
def names(e):
    return set(re.findall(r'[A-Za-z_][A-Za-z0-9_]*',str(e)))
allnames={}
for k in maps:
    s=set()
    for r,z,e in maps[k]: s|=names(e)
    allnames[k]=s
    print(k,"rows",len(maps[k]),"distinct names",len(s),"N",norm.get(k),"max r+z",max(int(r)+int(z) for r,z,e in maps[k]),"min r",min(int(r) for r,z,e in maps[k]),"max z",max(int(z) for r,z,e in maps[k]))
base=allnames['h3']|allnames['C2']|allnames['C3']|allnames['B2']
print("base names h3,C2,C3,B2:",len(base))
print("A3 names:",len(allnames['A3']))
print("base & A3 overlap:",base&allnames['A3'])
print("non-A3c names in A3 entries:",[n for n in allnames['A3'] if not n.startswith('A3c_')])
print("non-prefixed names in base:",sorted(n for n in base if not re.match(r'(Hc|C2c|C3c|B2c)_',n)))
ffc=src['full_free_coordinates']; print("full_free_coordinates:",len(ffc))
occ=base|allnames['A3']|{'target_a','target_b'}
print("occurring incl target_a,b:",len(occ),"; declared minus occurring:",sorted(set(ffc)-occ),"; occurring minus declared:",sorted(occ-set(ffc)))
co=exp['coordinate_order']; print("export coordinate_order:",len(co))
hf=[n for n in co if n.startswith('Hfact_')]; print("Hfact count:",len(hf))
print("export non-Hfact, non-Zj:",len([n for n in co if not n.startswith('Hfact_') and n!='Zj']), " set equal to occurring?", set(n for n in co if not n.startswith('Hfact_') and n!='Zj')==occ)
# W=0 rows literal
for k in maps:
    print("W=0 rows",k,[(r,z,e) for r,z,e in maps[k] if int(z)==0], "-> monomials X^(N-r-z):",[(norm[k]-int(r)-int(z)) for r,z,e in maps[k] if int(z)==0])
# constant entries anywhere
for k in maps:
    consts=[(r,z,e) for r,z,e in maps[k] if not names(e)]
    print("constant entries in",k,":",consts)
# A3 support: degree and W-exponent
A3=maps['A3']; N=98
degs=sorted(set(N-int(r) for r,z,e in A3)); print("A3 degrees present:",degs)
print("A3 max W exp:",max(int(z) for r,z,e in A3)," rows with z=33:",[row for row in A3 if int(row[1])==33])
print("A3 degree-33 rows (r=65) W exps:",sorted(int(z) for r,z,e in A3 if int(r)==65))
print("A3 rows with X-exp 0 (r+z=98):",[(r,z,e) for r,z,e in A3 if int(r)+int(z)==98])
# h3 top (degree 11, r=0) and degree 10 (r=1)
for k in ['h3','C2','C3','B2']:
    print(k,"degrees present:",sorted(set(norm[k]-int(r) for r,z,e in maps[k])))
print("h3 r=0 rows:",[(r,z,e) for r,z,e in maps['h3'] if int(r)==0])
print("h3 r=1 rows:",[(r,z,e) for r,z,e in maps['h3'] if int(r)==1])
print("h3 r=2 rows:",[(r,z,e) for r,z,e in maps['h3'] if int(r)==2])
# identity slots for A3c_97_0, A3c_98_0 and occurrences elsewhere
for v in ['A3c_97_0','A3c_98_0']:
    print(v,"occurs in rows:",[(r,z,e) for r,z,e in A3 if v in names(e)])
