from fractions import Fraction as F
import json, math

out={}

# --- A. Moh Appendix II p.207 printed table: terminal-radius check -------------
# rows: (n', m', M_s', ell, printed delta_2)
appII=[("16,12 main",16,12,13,1,F(-1)),
       ("21,14 main",21,14,16,1,F(-1,2)),
       ("21,14 [br]",21,14,18,1,F(-1)),
       ("15,10 main",15,10,11,2,F(-1))]
rows=[]
for name,n,m,Ms,ell,printed in appII:
    d=F(-(ell+1),n-Ms-1)
    rows.append(dict(row=name,n=n,m=m,Ms=Ms,ell=ell,printed=str(printed),
                     formula=str(d),match=(d==printed)))
out["appendixII_terminal_radius"]=rows
out["appendixII_all_match"]=all(r["match"] for r in rows)

# --- B. Appendix II coefficient counts = total-degree counts? -----------------
tri=lambda n:(n+1)*(n+2)//2
src=[("(64,48)",64,48,3370),("(84,56)",84,56,5308),("(75,50)",75,50,4352),("(99,66)",99,66,7348)]
des=[("(16,12)",16,12,244),("(21,14)",21,14,373),("(15,10)",15,10,202)]
out["coeff_counts"]={
 "source":[dict(pair=p,n=n,m=m,printed=c,totdeg=tri(n)+tri(m),match=tri(n)+tri(m)==c) for p,n,m,c in src],
 "descendant":[dict(pair=p,n=n,m=m,printed=c,totdeg=tri(n)+tri(m),match=tri(n)+tri(m)==c) for p,n,m,c in des]}
# printed "(64,68)" alternative
out["coeff_counts"]["printed_64_68_totdeg"]=tri(64)+tri(68)

# --- C. d = -delta_s and |G_1| per campaign class -----------------------------
# (class, n', m', M_s', ell, s')  from moh-hsupport-gate-astra-20260905.md sec.8 table
cls=[("(16,12; 6,13; 3; 3)",16,12,13,3,3),
     ("(18,12; 2,9; 2; 3)",18,12,9,2,3),
     ("(24,16; -12,-2,5; 1; 4)",24,16,5,1,4),
     ("(24,16; 12,17; 1; 3)",24,16,17,1,3),
     ("(24,18; -15,14; 1; 3)",24,18,14,1,3),
     ("(24,18; 9,20; 1; 3)",24,18,20,1,3)]
cl=[]
for name,n,m,Ms,ell,sp in cls:
    d=F(ell+1,n-Ms-1); K=math.gcd(n,m)
    G1=sum(int(d*(K-a))+1 for a in range(K))          # 0<=b<=floor(d(K-a))
    G1max=[(a,int(d*(K-a))) for a in range(K)]
    cl.append(dict(cls=name,K=K,d=str(d),d_gt_1=(d>1),G1_size=G1,G1_bmax=G1max))
out["classes"]=cl

# --- D. negative control h = y(y-x^2)^3 --------------------------------------
# monomials (b,a) of h = y^4 -3x^2y^3 +3x^4y^2 -x^6 y
h=[(0,4),(2,3),(4,2),(6,1)]
def ctl(d1):
    return {"delta1":str(d1),"weights":{f"x^{b}y^{a}":str(a*d1-b) for b,a in h},
            "min":str(min(a*d1-b for b,a in h)),
            "totdeg":max(a+b for b,a in h)}
out["negative_control_y_ymx2_cubed"]={"V1_1":ctl(F(9,4)),"V1_3":ctl(F(1,2))}

print(json.dumps(out,indent=1))
