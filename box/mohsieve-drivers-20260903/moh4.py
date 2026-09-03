import sys
sys.path.insert(0,'box')
import moh_skeleton_full as MS
def Av(S): return [S.A(j) for j in range(1,S.s)]
def M3(S): return all(a>=2 for a in Av(S)) and S.any10() and S.V[2]>=2
def M4(S): return all(a>=2 for a in Av(S)) and S.any10() and all(S.V[j]>=2 for j in range(2,S.s+1))
print("six rows under MOH-4:", [M4(MS.Skel(n,m,Ms,V)) for (n,m,Ms,V,_,_,_,_) in MS.MOH_TABLE])
cls=set(); rows=[]
for n in range(4,101):
    for (m,Ms,V) in MS.census(n,Kmin=1,full=True):
        S=MS.Skel(n,m,Ms,V)
        if M4(S): cls.add((n,m)); rows.append((n,m,list(Ms),dict(sorted(V.items()))))
print(f"n<=100 (Moh space) MOH-4: {len(rows)} rows in {len(cls)} classes")
print("classes:", sorted(cls))
e3=[];e4=[]; g3=g4=g13=0
for n in range(48,201):
    G13=set();G3=set();G4=set()
    for (m,Ms,V) in MS.census(n,Kmin=16,full=True):
        S=MS.Skel(n,m,Ms,V); k=(m,Ms,S.V[S.s]); G13.add(k)
        if M3(S): G3.add(k)
        if M4(S): G4.add(k)
    g13+=len(G13); g3+=len(G3); g4+=len(G4)
    if G13 and not G3: e3.append(n)
    if G13 and not G4: e4.append(n)
print(f"D=48..200 groups: (1)-(13) {g13} | MOH-3 {g3} | MOH-4 {g4}")
print("emptied by MOH-3:", e3)
print("emptied by MOH-4:", e4)
