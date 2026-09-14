#!/usr/bin/env python3
"""One tiny exact W-filtration generation; no CAS, source substitution or solve."""
import ast
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import resource
import time

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
SOURCE = REPO / 'box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json'
# Explicit canonical hash; the source bytes are never modified.
SOURCE_SHA = '778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea'
started = time.monotonic()

def req(b, why):
    if not b:
        raise ValueError(why)

def add(a, b, scale=Q(1)):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, Q(0)) + scale*v
        if not c[k]:
            del c[k]
    return c

def scale(a, s):
    return {k: v*s for k, v in a.items() if v*s}

def linear(n):
    if isinstance(n, ast.Constant) and type(n.value) is int:
        return {None: Q(n.value)} if n.value else {}
    if isinstance(n, ast.Name):
        return {n.id: Q(1)}
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        return scale(linear(n.operand), -1)
    if isinstance(n, ast.BinOp):
        a, b = linear(n.left), linear(n.right)
        if isinstance(n.op, ast.Add): return add(a, b)
        if isinstance(n.op, ast.Sub): return add(a, b, -1)
        if isinstance(n.op, ast.Mult):
            req(set(a) <= {None} or set(b) <= {None}, 'nonlinear source')
            return scale(b, a.get(None, 0)) if set(a) <= {None} else scale(a, b.get(None, 0))
        if isinstance(n.op, ast.Div):
            req(set(b) == {None}, 'nonconstant denominator')
            return scale(a, 1/b[None])
    raise ValueError('bad source syntax')

def read_source():
    raw = SOURCE.read_bytes()
    req(hashlib.sha256(raw).hexdigest() == SOURCE_SHA, 'source pin')
    data = json.loads(raw)
    req(data['residual_rows'] == [], 'unexpected residuals')
    source = {}
    support = set()
    for r, z, expression in data['maps']['A3']:
        p = 98-int(r)-int(z), int(z)
        req(min(p) >= 0 and p not in support, 'source support')
        support.add(p)
        row = linear(ast.parse(str(expression).replace('^', '**'), mode='eval').body)
        req(None not in row, 'affine source')
        for name, c in row.items(): source.setdefault(name, {})[p] = c
    req(len(source) == 192 and len(support) == 201, 'source census')
    req(max(map(sum, support)) == 35 and max(j for i,j in support) == 32, 'source bounds')
    req({n for n,p in source.items() if any(j == 0 for i,j in p)} == {'A3c_97_0','A3c_98_0'}, 'line columns')
    req({p:c for p,c in source['A3c_97_0'].items() if p[1] == 0} == {(1,0):Q(1)}, 'line X')
    req(source['A3c_98_0'] == {(0,0):Q(1)}, 'constant column')
    others = set()
    for key in ('h3','C2','C3','B2'):
        for _,_,e in data['maps'][key]:
            others.update(n.id for n in ast.walk(ast.parse(str(e).replace('^','**'),mode='eval')) if isinstance(n,ast.Name))
    req(not others.intersection(source), 'base dependence')
    return source

def order(p): return p[1], -p[0]
def enc_poly(p): return [[i,j,str(c)] for (i,j),c in sorted(p.items())]
def dec_poly(p): return {(i,j):Q(c) for i,j,c in p}
def enc_linear(p): return [[k,str(c)] for k,c in sorted(p.items())]
def dec_linear(p): return {k:Q(c) for k,c in p}

def gslot(u,v):
    if min(u,v) < 0: return None
    if v: return 'g_%d_%d' % (u,v)
    return {0:'s',1:'t',2:'1'}.get(u)

def entry(poly, row):
    a,b = row
    out = {}
    for (i,j),c in poly.items():
        u,v = a+1-i,b+1-j
        slot = gslot(u,v)
        z = c*(i*v-j*u)
        if slot is not None and z:
            out = add(out, {slot:z})
    return out

def build(source):
    echelon = {}
    for name in sorted(set(source)-{'A3c_97_0','A3c_98_0'}):
        p, transform = dict(source[name]), {name:Q(1)}
        while p:
            lead = min(p,key=order)
            if lead not in echelon:
                divisor = p[lead]
                echelon[lead] = scale(p,1/divisor), scale(transform,1/divisor)
                break
            old, old_transform = echelon[lead]
            c = p[lead]
            p, transform = add(p,old,-c), add(transform,old_transform,-c)
        else: raise ValueError('source dependence')
    basis, rows = [], []
    for lead in sorted(echelon,key=order):
        i,r = lead
        req(r > 0,'nonvanishing line active')
        p,t = echelon[lead]
        normalization = -Q(1,2*r)
        basis.append({'kind':'active','lead':list(lead),'normalization':str(normalization),
                      'poly':enc_poly(scale(p,normalization)), 'source_combination':enc_linear(scale(t,normalization))})
        rows.append([i+1,r-1])
    for name,kind in [('A3c_97_0','free_X'),('A3c_98_0','free_constant')]:
        basis.append({'kind':kind,'poly':enc_poly(source[name]),'source_combination':[[name,'1']]})
    matrix = []
    for ri,row in enumerate(rows):
        for ci,b in enumerate(basis):
            e = entry(dec_poly(b['poly']),row)
            if e: matrix.append([ri,ci,enc_linear(e)])
    return {'schema':'JC2/W190/v1','status':'PROVISIONAL_PENDING_INDEPENDENT_GATE',
            'source_sha256':SOURCE_SHA,'coordinates':['X=x','W=y-x'],
            'jacobian_convention':'P_X*G_W-P_W*G_X','source_variables':sorted(source),
            'G_line':{'2':'1','1':'t','0':'s'},'off_line_G':'all coefficients g_u_v, u>=0,v>=1 arbitrary',
            'basis':basis,'selected_rows':rows,'selected_matrix':matrix,
            'equations':'k_i + sum_j M_i_j*z_j = 0; z_190=beta, z_191=gamma',
            'reconstruction':'z_i=-k_i-sum_(j<i)M_i_j*z_j-M_i_190*beta, i=0..189',
            'residual_contract':'Keep every other positive physical Jacobian coefficient and Zj*J0-1; retain every source/monic definition; never set J0=1.'}

def independent_matrix(polys, selected):
    # Source-oriented differentiation, independent of target-oriented entry().
    # Any contributing G term has degree <= max(row degree)+1, since constants differentiate to zero.
    max_g = max(map(sum,selected))+1
    positions = {tuple(p):i for i,p in enumerate(selected)}
    gs = [(u,v,gslot(u,v)) for v in range(max_g+1) for u in range(max_g-v+1) if gslot(u,v) is not None]
    matrix = {}
    for ci,p in enumerate(polys):
        px = {(i-1,j):c*i for (i,j),c in p.items() if i}
        pw = {(i,j-1):c*j for (i,j),c in p.items() if j}
        for u,v,slot in gs:
            if v:
                for (i,j),c in px.items():
                    ri = positions.get((i+u,j+v-1))
                    if ri is not None:
                        key = ri,ci
                        matrix[key] = add(matrix.get(key,{}),{slot:c*v})
            if u:
                for (i,j),c in pw.items():
                    ri = positions.get((i+u-1,j+v))
                    if ri is not None:
                        key = ri,ci
                        matrix[key] = add(matrix.get(key,{}),{slot:-c*u})
    return {k:v for k,v in matrix.items() if v}

def verify(packet, source, expected_matrix=None):
    req(packet['source_sha256'] == SOURCE_SHA,'source pin mismatch')
    req(packet['jacobian_convention'] == 'P_X*G_W-P_W*G_X','Jacobian sign mismatch')
    req(packet['G_line'] == {'2':'1','1':'t','0':'s'},'line mismatch')
    req(packet['source_variables'] == sorted(source),'coordinate order mismatch')
    basis, rows = packet['basis'], packet['selected_rows']
    req(len(basis)==192 and len(rows)==190 and len(set(map(tuple,rows)))==190,'census mismatch')
    polys, rank_pivots = [], {}
    for ci,b in enumerate(basis):
        p = dec_poly(b['poly']); comb = dec_linear(b['source_combination']); rebuilt = {}
        for n,c in comb.items():
            req(n in source,'foreign source coordinate')
            rebuilt = add(rebuilt,source[n],c)
        req(p == rebuilt,'source reconstruction mismatch')
        v = dict(comb)
        while v:
            lead=min(v)
            if lead not in rank_pivots:
                rank_pivots[lead]=scale(v,1/v[lead]);break
            v=add(v,rank_pivots[lead],-v[lead])
        req(bool(v),'basis transform singular')
        if ci < 190:
            i,r=min(p,key=order)
            req(r>0 and b['lead']==[i,r],'W-leading mismatch')
            req(p[i,r] == -Q(1,2*r) and Q(b['normalization']) == -Q(1,2*r),'pivot normalization mismatch')
            req(rows[ci]==[i+1,r-1],'selected row mismatch')
            req(sum(rows[ci])>0,'constant row selected')
            if ci: req(order(tuple(basis[ci-1]['lead'])) < order((i,r)),'basis order mismatch')
        elif ci==190: req(p==source['A3c_97_0'],'free X mismatch')
        else: req(p=={(0,0):Q(1)},'free constant mismatch')
        polys.append(p)
    stored = {(i,j):dec_linear(v) for i,j,v in packet['selected_matrix']}
    req(len(stored)==len(packet['selected_matrix']),'duplicate matrix entry')
    actual = independent_matrix(polys,rows) if expected_matrix is None else expected_matrix
    req(stored==actual,'universal coefficient identity mismatch')
    for i in range(190):
        req(stored.get((i,i))=={'1':Q(1)},'nonunit diagonal')
        req(all((i,j) not in stored for j in range(i+1,190)),'nontriangular matrix')
        req((i,191) not in stored,'constant contributes')
    return polys,stored

def mul(a,b):
    out={}
    for (i,j),c in a.items():
        for (u,v),d in b.items(): out=add(out,{(i+u,j+v):c*d})
    return out

def derivative(p,axis):
    out={}
    for ij,c in p.items():
        if ij[axis]:
            k=list(ij);k[axis]-=1;out[tuple(k)]=c*ij[axis]
    return out

def point_check(polys,rows,matrix):
    # Independent ordinary polynomial products, no universal-entry evaluator.
    G={(2,0):Q(1),(1,0):Q(3),(0,0):Q(5),(0,1):Q(1),(1,1):Q(2),(0,2):Q(3),(5,7):Q(1)}
    # H^6=(X+W)^18 W^48 has degree 66 and does not affect low selected rows.
    G.update({(18-j,48+j):Q(math.comb(18,j)) for j in range(19)})
    values={'1':Q(1),'t':Q(3),'s':Q(5)}
    values.update({'g_%d_%d'%p:c for p,c in G.items() if p[1]})
    gx,gw=derivative(G,0),derivative(G,1)
    for ci,p in enumerate(polys):
        image=add(mul(derivative(p,0),gw),mul(derivative(p,1),gx),-1)
        for ri,row in enumerate(rows):
            exact=sum(c*values.get(g,Q(0)) for g,c in matrix.get((ri,ci),{}).items())
            req(image.get(tuple(row),Q(0))==exact,'exact point mismatch')
    # Exact reconstruction including arbitrary RHS and beta at this same point.
    z=[];beta=Q(7)
    k=[Q((i*13)%17-8, (i%5)+1) for i in range(190)]
    scalar={(i,j):sum(c*values.get(g,Q(0)) for g,c in e.items()) for (i,j),e in matrix.items()}
    for i in range(190): z.append(-k[i]-sum(scalar.get((i,j),0)*z[j] for j in range(i))-scalar.get((i,190),0)*beta)
    for i in range(190): req(k[i]+sum(scalar.get((i,j),0)*z[j] for j in range(190))+scalar.get((i,190),0)*beta==0,'point reconstruction mismatch')
    return {'G_terms':len(G),'all_36480_matrix_entries_checked':True,'all_190_graph_equations_checked':True}

def mutation_controls(packet,source):
    controls=[]
    def reject(label, mutate):
        bad=copy.deepcopy(packet);mutate(bad)
        try:
            # Recompute the complete independent universal matrix: no hash-only rejection.
            verify(bad,source)
        except ValueError as e:
            controls.append({'mutation':label,'status':'REJECTED_BY_SAME_SEMANTIC_VERIFIER','reason':str(e)})
        else: raise ValueError('mutation escaped: '+label)
    reject('source transform coefficient sign',lambda p:p['basis'][0]['source_combination'][0].__setitem__(1,str(-Q(p['basis'][0]['source_combination'][0][1]))))
    reject('selected row X index',lambda p:p['selected_rows'][0].__setitem__(0,p['selected_rows'][0][0]+1))
    diagonal=next(k for k,(i,j,e) in enumerate(packet['selected_matrix']) if i==j)
    reject('diagonal coefficient 1 to 2',lambda p:p['selected_matrix'][diagonal][2][0].__setitem__(1,'2'))
    nonconstant=next((k,l) for k,(i,j,e) in enumerate(packet['selected_matrix']) for l,(g,c) in enumerate(e) if g.startswith('g_'))
    reject('off-line coefficient term deletion',lambda p:p['selected_matrix'][nonconstant[0]][2].pop(nonconstant[1]))
    reject('Jacobian convention sign',lambda p:p.__setitem__('jacobian_convention','P_W*G_X-P_X*G_W'))
    return controls

def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-certificate',type=Path,help='Read-only semantic replay, including actual mutated inputs')
    parser.add_argument('--output-dir',type=Path,help='Fresh output directory for generation; refuses existing charged files')
    args=parser.parse_args()
    source=read_source()
    if args.verify_certificate:
        raw=args.verify_certificate.read_bytes()
        packet=json.loads(raw)
        polys,matrix=verify(packet,source)
        controls=mutation_controls(packet,source)
        point=point_check(polys,packet['selected_rows'],matrix)
        print(json.dumps({'status':'PASS_READ_ONLY_REPLAY','certificate_sha256':hashlib.sha256(raw).hexdigest(),
              'universal_entries':len(matrix),'mutation_controls':controls,'point':point,
              'seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
        return
    out=args.output_dir or ROOT
    req(not any((out/n).exists() for n in ('certificate.json','summary.json','selected_rows.tsv')),'refuse overwrite of existing generation')
    packet=build(source)
    build_seconds=time.monotonic()-started
    polys,matrix=verify(packet,source)
    verified_seconds=time.monotonic()-started-build_seconds
    controls=mutation_controls(packet,source)
    point=point_check(polys,packet['selected_rows'],matrix)
    charged=REPO/'box/factored-jacobian-pilot-20260906/complete_export.rows.tsv'
    charged_rows={tuple(map(int,line.split('\t')[:2])) for line in charged.read_text().splitlines()[1:]}
    req(set(map(tuple,packet['selected_rows'])) <= charged_rows,'selected rows absent from complete literal stream')
    gvariables=sorted({g for e in matrix.values() for g in e if g.startswith('g_')})
    gdegrees=[sum(map(int,g.split('_')[1:])) for g in gvariables]
    terms=sum(len(e) for e in matrix.values())
    graph_matrix_terms=sum(len(e) for (i,j),e in matrix.items() if i!=j)
    summary={'status':'PASS_PROVISIONAL_PENDING_INDEPENDENT_GATE','source_dimension':192,
     'constant_positive_pivots':190,'minor_determinant':'1','basis_physical_terms':sum(map(len,polys)),
     'basis_transform_terms':sum(len(b['source_combination']) for b in packet['basis']),
     'matrix_nonzero_entries':len(matrix),'matrix_literal_terms':terms,
     'graph_expanded_linear_coefficient_terms':190+graph_matrix_terms,
     'graph_rhs_nodes':190,'graph_product_edges':len(matrix)-190,
     'graph_new_unknowns':0,'remaining_nonconstant_C_coordinates':1,'free_constant_retained_in_contract':True,
     'off_line_G_coordinates':len(gvariables),'off_line_G_degree_min':min(gdegrees),'off_line_G_degree_max':max(gdegrees),
     'selected_physical_degree_min':min(map(sum,packet['selected_rows'])),'selected_physical_degree_max':max(map(sum,packet['selected_rows'])),
     'active_W_order_min':min(b['lead'][1] for b in packet['basis'][:190]),'active_W_order_max':max(b['lead'][1] for b in packet['basis'][:190]),
     'free_X_physical_terms':len(polys[190]),'free_X_degree':max(map(sum,polys[190])),
     'all_selected_rows_in_charged_complete_stream':True,'positive_literal_rows_before':len(charged_rows)-1,
     'retained_positive_literal_row_labels':len(charged_rows)-1-190,
     'safe_all_positive_slots_through_99':5049,'safe_remaining_positive_slots':4859,
     'exact_point_verification':point,'mutation_controls':controls,
     'build_seconds':build_seconds,'universal_verification_seconds':verified_seconds,
     'total_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     'dense_source_substitution':False,'full_residual_expansion':False,'solver_launched':False}
    raw=(json.dumps(packet,separators=(',',':'),sort_keys=True)+'\n').encode()
    (out/'certificate.json').write_bytes(raw)
    summary['certificate_bytes']=len(raw);summary['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    identities=['index\tX_power\tW_power\tleading_X\tleading_W\tnormalization\tdiagonal\tlower_entries\tliteral_coefficient_terms']
    for i,row in enumerate(packet['selected_rows']):
        b=packet['basis'][i]
        items=[e for (ri,j),e in matrix.items() if ri==i and j!=i]
        identities.append('\t'.join(map(str,[i,*row,*b['lead'],b['normalization'],1,len(items),sum(map(len,items))])))
    (out/'selected_rows.tsv').write_text('\n'.join(identities)+'\n')
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__': main()
