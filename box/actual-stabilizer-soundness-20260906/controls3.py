import sys, json
from fractions import Fraction as F
sys.path.insert(0,"/home/ubuntu/jc2/box/actual-stabilizer-soundness-20260906")
from verify import B, Tree, op_actual
keep = json.load(open("/home/ubuntu/jc2/box/actual-stabilizer-soundness-20260906/actual90.json"))
sub = sorted([tuple(r[0:2])+ (tuple(r[2]), tuple(r[3])) for r in keep if r[0] <= 100])
moh = sorted([(n,m,tuple(Ms),tuple(V[i] for i in sorted(V,reverse=False)))
              for (n,m,Ms,V,tag,a,b,c) in B.MOH_TABLE])
moh = sorted([(n,m,tuple(Ms),(V[2],V[3])) for (n,m,Ms,V,tag,a,b,c) in B.MOH_TABLE])
print("ACTUAL survivors n<=100 :", sub)
print("MOH p.202 table rows    :", moh)
print("SETS EQUAL:", sub == moh)
# coarse n<=100 for contrast
from verify import op_coarse
cc = []
for n in range(16,101):
    for (m,Ms,V) in B.census(n,Kmin=2,full=True):
        if op_coarse(n,m,Ms,V): cc.append((n,m,tuple(Ms),tuple(V[i] for i in range(2,len(Ms)+2))))
print("COARSE n<=100 count:", len(cc), " excess over Moh:", len(cc)-len(moh))
print("excess rows (all s>=4):", [r for r in cc if r not in moh])
