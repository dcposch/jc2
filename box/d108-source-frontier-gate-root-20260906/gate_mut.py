import json,re,ast,sympy as S,time
t0=time.monotonic()
raw=json.load(open('box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json'))
X,W=S.symbols('X W')
def split_top(text):
    parts=[];start=depth=0
    for i,ch in enumerate(text):
        if ch=='(':depth+=1
        elif ch==')':depth-=1
        elif ch=='+' and depth==0:parts.append(text[start:i]);start=i+1
    parts.append(text[start:]);return parts
maps={}
for key,N in [('h',36),('D',71),('C',107)]:
    rows=[]
    for part in split_top(raw[key+'_expr']):
        mt=re.fullmatch(r'\((.*)\)\*tt\^(\d+)\*zz\^(\d+)',part);e,r,z=mt.groups();r=int(r);z=int(z)
        rows.append((N-r-z,z,e))
    maps[key]=rows
out={}
# T1 raw bounds and faces
for k,rows in maps.items():
    out[k+'_maxX']=max(i for i,j,e in rows); out[k+'_maxwt']=max(4*i-j for i,j,e in rows); out[k+'_maxdeg']=max(i+j for i,j,e in rows); out[k+'_maxW']=max(j for i,j,e in rows)
face=S.expand(sum(S.sympify(e)*X**i*W**j for i,j,e in maps['h'] if 4*i-j==4))
out['h_face_eq_X(XW4-1)^7']=S.expand(face-X*(X*W**4-1)**7)==0
out['h_face_rows_constant']=all(S.sympify(e).free_symbols==set() for i,j,e in maps['h'] if 4*i-j==4)
out['h_X8_slots']=[(i,j,e) for i,j,e in maps['h'] if i==8]
# D,C weight-4 faces (are they parameter-dependent? irrelevant for F face since 12>8)
out['D_face_wt4_terms']=len([1 for i,j,e in maps['D'] if 4*i-j==4]); out['C_face_wt4_terms']=len([1 for i,j,e in maps['C'] if 4*i-j==4])
# lines
line={k:S.expand(sum(S.sympify(e)*X**i for i,j,e in rows if j==0)) for k,rows in maps.items()}
out['lines']={k:str(v) for k,v in line.items()}
eta,b,d1,d0=S.symbols('K2c_36_0 target_b B2c_70_0 B2c_71_0')
G0=S.expand(line['h']**2-b*line['h']/3+line['D']); out['G_line']=str(G0); out['G_line_monic_quad']=(S.Poly(G0,X).degree()==2 and S.Poly(G0,X).LC()==1)
# W^36 absent & C degree-36 W exponents
out['C_W36_slots']=[(i,j) for i,j,e in maps['C'] if j==36]; out['C_deg36_Wexps']=sorted({j for i,j,e in maps['C'] if i+j==36})
# residual independence
resnames=set()
for s in raw['residual_strings']:
    resnames|={n.id for n in ast.walk(ast.parse(s.replace('^','**'),mode='eval')) if isinstance(n,ast.Name)}
cn=set().union(*[{n.id for n in ast.walk(ast.parse(e.replace('^','**'),mode='eval')) if isinstance(n,ast.Name)} for i,j,e in maps['C']])
out['n_residuals']=len(raw['residual_strings']); out['C_params']=len(cn); out['res_C_overlap']=sorted(resnames&cn); out['res_B2_overlap']=sorted(n for n in resnames if n.startswith('B2c')); out['res_names_count']=len(resnames)
out['gamma_only_slot']=[(i,j) for i,j,e in maps['C'] if 'A3c_107_0' in e]
# residual0 = L^2 with L = leading coeff of h(A=0,B)=h(-B,B)
hAB=sum(S.sympify(e)*(-W)**i*W**j for i,j,e in maps['h'])  # X=-B,W=B with W as B
hAB=S.expand(hAB); ph=S.Poly(hAB,W); out['h_A0_degree']=ph.degree(); L=ph.LC(); out['L']=str(L)
r0=S.sympify(raw['residual_strings'][0].replace('^','**')); out['res0_eq_L2']=S.expand(r0-L**2)==0
# how many of the h(0,B) coefficients are (up to sign) squares/ multiples of residuals? just record degree count
# T2 Euler auxiliary independent
H=X*(X*W**4-1)**7
E=S.Rational(2048,3315)*X**6*W**21-S.Rational(3584,1105)*X**5*W**17+S.Rational(448,65)*X**4*W**13-S.Rational(112,15)*X**3*W**9+S.Rational(21,5)*X**2*W**5-X*W
jac=lambda p,q:S.expand(S.diff(p,X)*S.diff(q,W)-S.diff(p,W)*S.diff(q,X))
out['J(E,H)=H']=jac(E,H)==S.expand(H)
out['J(E/3,H^3)=H^3']=S.expand(jac(E/3,H**3)-H**3)==0
Em=E+S.Rational(1,1000)*X**2*W**5; out['mut_E_fails']=jac(Em,H)!=S.expand(H)
Hm=X*(X*W**4-2)**7; out['mut_H_alpha2_fails']=jac(E,Hm)!=S.expand(Hm)
# T3 full map on a nontrivial Keller control, including linear change + swap + shears + inversion
x,y,l2,l3,l4=S.symbols('x y ell2 ell3 ell4')
def T(p): return S.expand(p.subs({X:x**4*y+l2*x**2+l3*x**3+l4*x**4-1/x, W:1/x},simultaneous=True))
jxy=lambda p,q:S.expand(S.diff(p,x)*S.diff(q,y)-S.diff(p,y)*S.diff(q,x))
F=X+W**3; G=W+(X+W**3)**2; j=jac(F,G); out['ctrl_j']=str(j)
P=T(G); Q=-T(F)/j; out['ctrl_J(P,Q)=x2']=S.simplify(jxy(P,Q)-x**2)==0
# explicit composition check: A=X+W,B=W; swap x1=B,y1=A; shear y1=y2+l2 x^-2+l3 x^-3 + l4 x^-4 ; invert x2=1/x, y2=x^4 y
A,B,x1,y1,x2,y2=S.symbols('A B x1 y1 x2 y2')
comp=lambda p: S.expand(p.subs({X:A-B,W:B},simultaneous=True).subs({A:y1,B:x1},simultaneous=True).subs({y1:y2+l2*x2**-2+l3*x2**-3+l4*x2**-4,x1:x2},simultaneous=True).subs({x2:1/x,y2:x**4*y},simultaneous=True))
out['composition_matches_T']=all(S.expand(comp(p)-T(p))==0 for p in (X,W,X*W**2))
# T4 polygon transport map
tr=lambda q:(4*q[1]-q[0],q[1])
out['poly_small_P']=sorted({tr(q) for q in [(-1,0),(0,0),(56,16),(48,14)]}); out['poly_small_Q']=sorted({tr(q) for q in [(2,1),(0,0),(84,24),(72,21)]}); out['poly_extra']=[tr((32,8)),tr((48,12))]
# where do the D108 literal (1,0)-lead and (4,-1)-edge endpoints go under swap+cut+inversion (edge only)
sw=lambda q:(q[1],q[0])
out['F_edge_swapped_endpoints']=[sw((24,84)),sw((3,0))]; out['after_cut_edge_F']=[(84,24),(72,21)]
# T5 Delta independent
hW=S.expand(sum(S.sympify(e)*X**i for i,j,e in maps['h'] if j==1)); DW=S.expand(sum(S.sympify(e)*X**i for i,j,e in maps['D'] if j==1))
xs=S.solve(S.diff(G0,X),X)[0]; out['x_star']=str(xs)
Delta=S.expand((S.diff(line['h'],X)*DW-hW*S.diff(line['D'],X)).subs(X,xs)); Delta=-Delta
out['Delta_matches_producer']=S.expand(Delta-(d1*hW+DW).subs(X,xs))==0
fr=S.Symbol('B2c_70_1'); out['Delta_monic_B2c_70_1']=S.diff(Delta,fr)==1; out['B2c_70_1_in_res']='B2c_70_1' in resnames
out['seconds']=time.monotonic()-t0
print(json.dumps(out,indent=1,default=str))
