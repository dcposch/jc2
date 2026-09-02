import sys; sys.path.insert(0,'/tmp/degaf')
from am2 import semigroups, memb_array, sgp_from, am_data
from am3 import n_min_lower
def gens(gaps,N=60):
    M=memb_array(gaps,N); out=[]
    for x in range(1,N+1):
        if M[x] and not (sgp_from(out,N)[x] if out else False): out.append(x)
        if out and all(sgp_from(out,N)[y]==M[y] for y in range(N+1)): break
    return out
print("delta_aff | admissible semigroups at infinity <...> with least admissible degree")
for g in range(0,9):
    rows=[]
    for gaps in semigroups(g):
        v=n_min_lower(gaps)
        if v is not None: rows.append((v,tuple(gens(gaps))))
    rows.sort()
    print(f"  {g:2d}      "+" ; ".join(f"<{','.join(map(str,G))}> n>={v}" for v,G in rows))
