import json,sympy as sp,re
src=json.load(open('/tmp/jc2-lane.rM5Jkj/inputs/delta2_stage8.strongest.json'))
exp=json.load(open('/tmp/jc2-lane.rM5Jkj/inputs/complete_export.json'))
maps=src['maps']; norm=src['normalization']
X,W=sp.symbols('X W')
def phys(key):
    N=norm[key]; d={}
    for r,z,e in maps[key]:
        c=sp.sympify(str(e).replace('^','**'))
        p=(N-int(r)-int(z),int(z)); d[p]=d.get(p,0)+c
    return d
def mul(a,b):
    out={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            out[(i+k,j+l)]=out.get((i+k,j+l),0)+u*v
    return out
def add(a,b):
    out=dict(a)
    for p,v in b.items(): out[p]=out.get(p,0)+v
    return out
h3,C2,C3=phys('h3'),phys('C2'),phys('C3')
h=add(add(mul(mul(h3,h3),h3),mul(C2,h3)),C3)
h={p:sp.expand(v) for p,v in h.items()}
h={p:v for p,v in h.items() if v!=0}
print("h physical support:",len(h),"max degree:",max(i+j for i,j in h))
const={p:v for p,v in h.items() if v.is_number}
nonc={p:v for p,v in h.items() if not v.is_number}
print("constant slots:",len(const),sorted(const.items()))
print("nonconstant slots:",len(nonc),"max degree of nonconstant:",max(i+j for i,j in nonc))
print("W=0 slots of h:",{p:v for p,v in h.items() if p[1]==0})
print("degree-33 part:",{p:v for p,v in h.items() if p[0]+p[1]==33})
H3=sp.Poly(sp.expand((X+W)**9*W**24),X,W).as_dict()
print("degree-33 part == H^3:",{p:v for p,v in h.items() if p[0]+p[1]==33}=={(m[0],m[1]):sp.Integer(c) for m,c in H3.items()})
print("degree-32 part:",{p:v for p,v in h.items() if p[0]+p[1]==32})
hf=[n for n in exp['coordinate_order'] if n.startswith('Hfact_')]
hfpos={(int(n.split('_')[1]),int(n.split('_')[2])) for n in hf}
print("Hfact names as (i,j)=X^i W^j equal nonconstant slots:",hfpos==set(nonc))
print("Hfact names as (W,X) swapped equal nonconstant slots:",{(b,a) for a,b in hfpos}==set(nonc))
print("max source degree of h coeffs:",max(sp.Poly(v).total_degree() for v in nonc.values()),"max coefficient terms:",max(len(sp.Poly(v).terms()) for v in nonc.values()),"total literal terms:",sum(len(sp.Poly(v).terms()) for v in nonc.values())+len(const))
print("W^33 coefficient of h:",h.get((0,33)))
